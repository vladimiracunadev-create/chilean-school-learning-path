"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 08 (aportes vivos de culturas y visiones indígenas) y OA 09 (nociones indígenas de tiempo y espacio).

Criterio de autoría: las comunidades, los lugares, las personas y los relatos de práctica son INVENTADOS
y se rotulan así. No se afirma nada de lengua, ritos, fechas de celebraciones, arte, cosmovisión ni roles
de un pueblo concreto, ni el significado de nombres de lugar. Lo tradicional lo enseñan el educador o la
educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc3_a import FICHA_CC, FICHA_VA, L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA8, OA9 = "LC03 OA 08", "LC03 OA 09"

# ============================================================ OA 08 · Aportes vivos de culturas y visiones indígenas
L(
    OA8, 1,
    materials="Lápiz y hojas. Las tarjetas de personas están escritas aquí y son inventadas.",
    use="Aprenderé a reconocer que las culturas indígenas están vivas hoy. Sirve para no creer que son solo cosa del pasado ni quedarme con imágenes falsas.",
    prior=["Sé que los pueblos originarios viven hoy.", "Sé que cada comunidad tiene su propia manera de vivir."],
    explain=[
        "En Chile viven varios pueblos originarios. Sus integrantes viven en el campo y en la ciudad, van a la escuela, trabajan, usan tecnología y hablan castellano. Muchos también mantienen saberes, costumbres y, a veces, su lengua.",
        "Decimos que una cultura está viva cuando las personas la practican y la renuevan hoy. Una cultura viva cambia, aprende cosas nuevas y mantiene lo que valora. Por eso no se reconoce a una persona indígena por su ropa o su aspecto.",
        "Cada pueblo tiene también su forma de ver el mundo: cómo entiende la vida, la naturaleza y a las personas. Esa forma la cuenta cada comunidad; nosotros no la adivinamos. Cada comunidad es distinta. Por eso, para saber cómo vive una comunidad hoy, hay que preguntarle a ella. En esta clase usamos tarjetas de personas inventadas para practicar. No representan a ningún pueblo real.",
    ],
    vocab=[("cultura viva", "cultura que las personas practican y renuevan hoy"), ("costumbre", "manera de hacer algo que se repite en una comunidad"), ("saber", "conocimiento que una persona tiene y enseña"), ("tecnología", "aparatos e inventos que usamos hoy"), ("estereotipo", "idea simplificada y falsa sobre un grupo de personas")],
    worked=[
        W("Leer una tarjeta", "Tarjeta inventada: «Camila vive en una ciudad, va a la escuela y usa computador. Los fines de semana aprende de su abuela a cuidar la huerta de su comunidad.» ¿Qué muestra que su cultura está viva?", ["Camila usa tecnología hoy.", "Aprende de su abuela a cuidar la huerta.", "Practica un saber de su comunidad hoy."], "Aprende de su abuela a cuidar la huerta, hoy y en la ciudad."),
        W("Desarmar un estereotipo", "Un niño dice: «Una persona indígena siempre se viste con ropa tradicional». ¿Qué responderías con la tarjeta de Camila?", ["Camila va a la escuela y usa computador.", "No se dice cómo se viste.", "Una persona no se reconoce por su ropa."], "No: la tarjeta de Camila muestra que viven hoy como cualquiera y mantienen saberes."),
    ],
    mistakes=[
        M("Decir que una persona es indígena por cómo se ve.", "Es un estereotipo; la identidad no se mide por el aspecto.", "Pregunta y escucha cómo se presenta la propia persona."),
        M("Hablar de los pueblos originarios solo en pasado.", "Parece que ya no existen.", "Usa el presente: «viven», «practican»."),
    ],
    R=[
        ex("Tarjeta inventada: «Camila vive en una ciudad». ¿Dónde vive Camila?", "En una ciudad", "Lo dice la tarjeta."),
        ex("Camila aprende de su abuela a cuidar la huerta. ¿Quién le enseña?", "Su abuela", "La tarjeta lo dice."),
        ex("¿Una cultura viva se practica hoy o solo en el pasado?", "Hoy", "Una cultura viva se practica y renueva hoy."),
    ],
    C=[
        ex("Verdadero o falso: las personas indígenas no usan tecnología.", "Falso", "Viven hoy y usan lo que hay hoy."),
        ex("En Lengua y Cultura: ¿Qué es un estereotipo? A) una idea simplificada y falsa sobre un grupo B) un dato de una fuente", "A", "Simplifica a las personas."),
        ex("Verdadero o falso: se puede saber si una persona es indígena solo por su ropa.", "Falso", "La identidad no se reconoce por la ropa."),
    ],
    A=[
        ex("Tarjeta inventada de Tomás: «Estudia en una escuela, juega fútbol y ayuda a cuidar el agua de su comunidad». Escribe una cosa que hace con su comunidad.", "Ayuda a cuidar el agua", "La tarjeta lo dice."),
        ex("Clasifica en SABER DE LA COMUNIDAD o USO DE TECNOLOGÍA: a) cuidar la huerta con la abuela b) usar el computador de la escuela.", "a saber de la comunidad, b tecnología", "Cuidar la huerta se aprende en la comunidad; el computador es tecnología."),
        ex("Dos tarjetas inventadas: Camila vive en una ciudad; Tomás vive en el campo. ¿Pueden las dos personas mantener saberes de su comunidad? Responde Sí o No.", "Sí", "Se puede vivir en ciudad o campo y mantener saberes."),
        ex("Cada pueblo tiene su forma de ver el mundo. ¿Quién puede contarla mejor: la propia comunidad o alguien que solo mira una foto?", "La propia comunidad", "Solo quienes la viven pueden explicar cómo ven el mundo."),
    ],
    Z=[
        ex("Ema dibuja a todos los indígenas con plumas y sin zapatos. ¿Qué error comete?", "Usa un estereotipo", "Las personas se visten de muchas maneras."),
        ex("Pedro dice: «Si usa teléfono, ya no es de su pueblo». ¿Tiene razón? Responde Sí o No.", "No", "Se puede usar tecnología y mantener la cultura."),
    ],
    D=[
        ex("Una niña dice que conoció a un educador tradicional que usa computador y enseña la lengua de su pueblo en la escuela. ¿Qué muestra eso sobre las culturas? A) Que están vivas B) Que desaparecieron", "A", "Enseña y practica hoy."),
        ex("¿Qué haces para saber cómo vive hoy una comunidad real de tu zona? A) Le pregunto a la comunidad o al educador tradicional B) Lo adivino por una foto", "A", "Ellos son la fuente."),
    ],
    context=[ex("En una exposición de la escuela alguien propone disfrazar a un compañero de «indígena» con plumas. ¿Es buena idea? Responde Sí o No.", "No", "Es un estereotipo y una burla.")],
    selfcheck=[
        ex("Escribe qué es una cultura viva.", "Una cultura que las personas practican y renuevan hoy", "Es la definición de la lección."),
        ex("Verdadero o falso: las culturas vivas pueden cambiar.", "Verdadero", "Cambian y mantienen lo que valoran."),
        ex("En Lengua y Cultura: ¿Qué es un estereotipo?", "Una idea simplificada y falsa sobre un grupo", "Es lo que debemos evitar."),
    ],
    task=T("Lee dos tarjetas inventadas. Camila: «Vive en una ciudad, va a la escuela y aprende de su abuela a cuidar la huerta de su comunidad.» Tomás: «Vive en el campo, juega fútbol y ayuda a cuidar el agua de su comunidad.» Haz una tabla con dos filas, una por niño, y tres columnas: dónde vive, qué usa hoy y qué saber de su comunidad practica. Escribe debajo una frase que explique por qué estas tarjetas muestran culturas vivas.",
           "Camila: ciudad; escuela; cuida la huerta con su abuela. Tomás: campo; fútbol; cuida el agua. Muestran culturas vivas porque practican saberes de su comunidad hoy.",
           ["completa la tabla con datos de las tarjetas", "explica por qué están vivas", "no usa estereotipos"], ["tabla de dos filas", "frase de explicación"], ["agregar plumas o ropa a los dibujos", "usar el pasado"],
           "Revisar que cada dato esté en la tarjeta; preguntar por qué cuidar la huerta hoy muestra una cultura viva."),
    reinforce="Escribe tres cosas que una persona de una cultura viva puede hacer hoy.",
    extend="Escribe una pregunta respetuosa para el educador tradicional sobre cómo practica hoy su cultura.",
)

L(
    OA8, 2,
    materials="Lápiz y hojas. La ficha de aporte está escrita aquí y es inventada.",
    use="Aprenderé a examinar un aporte de una comunidad: qué entrega, a quién y quién lo cuenta. Sirve para valorar lo que una cultura viva da a su localidad.",
    prior=["Sé qué es una cultura viva.", "Sé usar una ficha con fuente y permiso."],
    explain=[
        "Un aporte es algo que una cultura entrega a otras personas y las enriquece. Puede ser un saber, una forma de cuidar el agua, una comida, una manera de convivir o un trabajo bien hecho. Un aporte se comparte con permiso.",
        "Un aporte situado es un aporte que tiene lugar y dueño. Decimos de qué comunidad viene, quién lo cuenta y a quién ayuda. No decimos «los pueblos aportan esto» en general, porque cada comunidad aporta cosas distintas.",
        "Para examinar un aporte hacemos tres preguntas: ¿qué es?, ¿de qué comunidad viene? y ¿a quién ayuda hoy? Si la comunidad dice que algo no se comparte, no es un aporte para copiar, y se respeta.",
    ],
    vocab=[("aporte", "algo que una cultura entrega y enriquece a otras personas"), ("situado", "con lugar, comunidad y fuente conocidos"), ("localidad", "lugar donde vive un grupo de personas, como un pueblo o un barrio"), ("compartir", "dar a otros una parte de lo que uno tiene o sabe"), ("beneficio", "ayuda o ventaja que recibe alguien")],
    worked=[
        W("Examinar un aporte", "Ficha inventada: «En Valle Alto, la comunidad organiza turnos para repartir el agua entre las huertas. Hoy la escuela del pueblo usa el mismo método para regar su huerto. Lo cuenta doña Rosa.» ¿Qué es el aporte, de quién viene y a quién ayuda?", ["Aporte: los turnos para repartir el agua.", "Viene de la comunidad de Valle Alto.", "Ayuda hoy a la escuela del pueblo."], "Turnos para repartir el agua; de Valle Alto; ayuda a la escuela."),
        W("Un aporte con límite", "Doña Rosa agrega: «Hay cantos que solo cantamos entre nosotros». ¿Son parte del aporte que se comparte con la escuela?", ["Ella dice que son solo entre nosotros.", "Eso es un límite.", "No se comparten."], "No: es un límite que la comunidad pidió respetar."),
    ],
    mistakes=[
        M("Decir «los pueblos originarios aportan todos lo mismo».", "Cada comunidad aporta cosas distintas.", "Di de qué comunidad viene cada aporte."),
        M("Copiar algo que la comunidad no compartió.", "Sin permiso es apropiarse.", "Pregunta y respeta los límites."),
    ],
    R=[
        ex("En la ficha de Valle Alto, ¿qué reparte la comunidad con turnos?", "El agua", "La ficha lo dice."),
        ex("¿Quién cuenta el aporte en la ficha?", "Doña Rosa", "Es la fuente."),
        ex("¿A qué lugar ayuda hoy este método? A) la escuela del pueblo B) un aeropuerto", "A", "La ficha lo dice."),
    ],
    C=[
        ex("¿Qué es un aporte? A) algo que una cultura entrega y enriquece a otros B) algo que se roba", "A", "Se comparte con permiso."),
        ex("Verdadero o falso: todos los pueblos aportan exactamente lo mismo.", "Falso", "Cada comunidad aporta cosas distintas."),
        ex("Verdadero o falso: si la comunidad dice «esto es solo nuestro», se puede copiar igual.", "Falso", "Se respeta el límite."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «La comunidad enseña a la escuela cómo cuidar la playa sin dejar basura. Lo cuenta don Luis.» Escribe el aporte.", "Cómo cuidar la playa sin dejar basura", "Es lo que la comunidad enseña."),
        ex("En la ficha de Costa Clara, ¿de qué comunidad viene el aporte?", "Costa Clara", "La ficha nombra la comunidad."),
        ex("Une cada pregunta con su dato. 1) ¿Qué es? 2) ¿De dónde viene? 3) ¿A quién ayuda? a) a la escuela del pueblo b) turnos de agua c) de Valle Alto", "1-b, 2-c, 3-a", "Cada dato responde una pregunta de la ficha de Valle Alto."),
    ],
    Z=[
        ex("Lía dice: «Los pueblos originarios aportan los turnos de agua en todo el país». ¿Qué error comete?", "Generaliza un aporte de una comunidad a todos", "La ficha habla de Valle Alto."),
        ex("Mateo quiere cantar en el acto los cantos que doña Rosa dijo que son solo de la comunidad. ¿Debe hacerlo? Responde Sí o No.", "No", "Hay un límite que se respeta."),
    ],
    D=[
        ex("Una escuela copia un diseño de la comunidad sin preguntar. ¿Qué debió hacer? A) Pedir permiso y atribuir la fuente B) Decir que lo inventó", "A", "Un aporte se comparte con permiso y se reconoce."),
        ex("Dos aportes inventados: 1) turnos de agua de Valle Alto, 2) cuidado de la playa de Costa Clara. ¿Son el mismo aporte? Responde Sí o No.", "No", "Son de comunidades distintas y sirven para cosas distintas."),
    ],
    context=[ex("Un grupo de vecinos quiere usar los turnos de agua de Valle Alto para su huerta comunitaria. ¿Qué paso corresponde antes? A) Preguntar a la comunidad de Valle Alto B) Usarlo sin avisar", "A", "Se pide permiso y se reconoce la fuente.")],
    selfcheck=[
        ex("Escribe las tres preguntas para examinar un aporte.", "¿Qué es?, ¿de qué comunidad viene? y ¿a quién ayuda hoy?", "Son las tres preguntas de la lección."),
        ex("Verdadero o falso: un aporte se comparte con permiso.", "Verdadero", "Sin permiso es apropiarse."),
        ex("¿Qué significa que un aporte sea situado?", "Que tiene comunidad y fuente conocidas", "Se sabe de dónde viene."),
    ],
    task=T("Lee la ficha inventada de Costa Clara: «La comunidad enseña a la escuela del pueblo a cuidar la playa: se llevan las bolsas de vuelta y se recogen los desechos. Lo cuenta don Luis. Hay historias que la comunidad no comparte.» Haz una ficha con cuatro líneas: aporte, comunidad, fuente y a quién ayuda. Escribe además un límite que respetas y una frase de agradecimiento a don Luis.",
           "Aporte: cuidar la playa llevando de vuelta las bolsas y recogiendo desechos. Comunidad: Costa Clara. Fuente: don Luis. Ayuda a: la escuela del pueblo. Límite: las historias que la comunidad no comparte. Gracias, don Luis.",
           ["completa las cuatro líneas con datos de la ficha", "nombra un límite", "agradece a la fuente"], ["ficha de cuatro líneas", "límite", "agradecimiento"], ["decir que es un aporte de todos los pueblos", "contar las historias reservadas"],
           "Preguntar de dónde sacó cada línea; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Valle Alto qué es el aporte y a quién ayuda.",
    extend="Escribe un aporte inventado de otra comunidad y respóndele las tres preguntas de la clase.",
)

L(
    OA8, 3,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a relacionar lo que aporta una comunidad con su localidad y con el país. Sirve para ver cómo la cultura indígena se une a la vida de todos.",
    prior=["Sé examinar un aporte situado.", "Sé que las culturas indígenas están vivas."],
    explain=[
        "Las comunidades viven en una localidad, que es un pueblo, un barrio o una zona. Sus saberes pueden llegar a otras personas de la localidad. Después esos saberes pueden conocerse en otras partes del país.",
        "Hay un ejemplo seguro y general: muchos nombres de lugares de Chile vienen de lenguas indígenas. Eso muestra que estas culturas forman parte del país. Pero lo que significa cada nombre lo cuentan la comunidad o una persona especialista. Nosotros no adivinamos.",
        "Cuando una cultura aporta a la localidad y al país, hablamos de intercambio: unas personas comparten y otras escuchan y agradecen. Un intercambio respetuoso reconoce de dónde viene el saber y no cambia su sentido.",
    ],
    vocab=[("localidad", "pueblo, barrio o zona donde vive un grupo de personas"), ("país", "territorio con un gobierno propio, como Chile"), ("intercambio", "dar y recibir saberes entre personas o comunidades"), ("reconocer", "decir de dónde viene algo"), ("especialista", "persona que sabe mucho de un tema")],
    worked=[
        W("De la comunidad a la localidad", "Ficha inventada: «La comunidad de Valle Alto enseñó los turnos de agua a la junta de vecinos del pueblo. Ahora todo el pueblo usa el método.» ¿Cómo llegó el aporte de la comunidad a la localidad?", ["La comunidad enseñó a la junta de vecinos.", "La junta lo adoptó.", "Ahora lo usa todo el pueblo."], "La comunidad enseñó a la junta de vecinos y ahora lo usa todo el pueblo."),
        W("Un nombre de lugar", "Una niña dice: «El nombre de mi comuna significa agua». Nadie le contó eso. ¿Se puede afirmar?", ["No hay fuente.", "Los significados los cuentan la comunidad o un especialista.", "No se puede afirmar sin fuente."], "No: falta una fuente que lo confirme."),
    ],
    mistakes=[
        M("Inventar el significado de un nombre de lugar.", "Puede ser falso y faltarle el respeto a la lengua.", "Pregunta a la comunidad o a un especialista."),
        M("Pensar que el aporte se queda solo en la comunidad.", "Muchas veces llega a la localidad y al país.", "Sigue el camino: comunidad, localidad, país."),
    ],
    R=[
        ex("¿Cuál es el orden de menor a mayor: comunidad, localidad, país?", "Comunidad, localidad, país", "Va de lo más pequeño a lo más grande."),
        ex("En la ficha de Valle Alto, ¿a quién enseñó la comunidad los turnos de agua?", "A la junta de vecinos del pueblo", "La ficha lo dice."),
        ex("¿Qué es un intercambio? A) dar y recibir saberes B) vender sin avisar", "A", "Es compartir y escuchar."),
    ],
    C=[
        ex("Verdadero o falso: muchos nombres de lugares de Chile vienen de lenguas indígenas.", "Verdadero", "Muestra que estas culturas son parte del país."),
        ex("Verdadero o falso: yo puedo decir el significado de un nombre de lugar sin preguntar a nadie.", "Falso", "Se pregunta a la comunidad o a un especialista."),
        ex("Si todo el pueblo usa un método que enseñó una comunidad, ¿el aporte llegó a la localidad? Responde Sí o No.", "Sí", "El pueblo ya lo usa."),
    ],
    A=[
        ex("Ordena de menor a mayor: a) Chile b) la comunidad de Valle Alto c) el pueblo de Valle Alto. Escribe las letras.", "b, c, a", "Primero la comunidad, luego el pueblo y al final el país."),
        ex("Ficha inventada: «La escuela de Costa Clara usa el cuidado de la playa que enseñó la comunidad. Otra escuela de otra región también lo copió con permiso.» ¿Dónde se usa el aporte, además de la comunidad?", "En dos escuelas", "Se usa en la escuela de Costa Clara y en otra escuela."),
        arith("Cuenta: en una ficha inventada, 3 escuelas y 2 juntas de vecinos usan un aporte. ¿Cuántas organizaciones lo usan?", "3+2", "Se suman escuelas y juntas."),
    ],
    Z=[
        ex("Tomás dice: «Mi comuna se llama así y significa luna» sin ninguna fuente. ¿Qué debería hacer?", "Preguntar a una fuente", "Sin fuente no se afirma."),
        ex("Ana copió un diseño de la comunidad y dijo que era suyo. ¿Qué error cometió? A) No reconoció de dónde viene B) Lo dibujó muy grande", "A", "No dio crédito a la fuente."),
    ],
    D=[
        ex("Un aporte pasa por estos lugares o grupos: comunidad, junta de vecinos, escuela, otra región. ¿Cuántos nombres hay en la lista? Escribe el número.", "4", "Son cuatro nombres en la lista."),
        ex("Dos niñas hablan del aporte: una dice «lo dijo la comunidad de Valle Alto», la otra «alguien lo dijo». ¿Cuál reconoce la fuente?", "La primera", "Nombra la comunidad."),
    ],
    context=[ex("Tu escuela quiere usar en su patio lo que enseñó Costa Clara sobre no dejar basura. ¿Qué haces? A) Pedir permiso y agradecer a la comunidad B) Usarlo sin decir nada", "A", "Es un intercambio respetuoso.")],
    selfcheck=[
        ex("Escribe el orden: comunidad, localidad y país, de menor a mayor.", "Comunidad, localidad, país", "Va de lo pequeño a lo grande."),
        ex("Verdadero o falso: puedo inventar lo que significa un nombre de lugar.", "Falso", "Se pregunta a una fuente."),
        ex("¿Qué es un intercambio respetuoso?", "Compartir y reconocer de dónde viene el saber", "Se comparte con permiso y crédito."),
    ],
    task=T("Con la ficha inventada de Valle Alto: «La comunidad enseñó los turnos de agua a la junta de vecinos. Después la escuela del pueblo los usó para su huerto. Una escuela de otra región pidió permiso para usarlos.» Dibuja una cadena de cuatro círculos: comunidad, junta de vecinos, escuela del pueblo y otra región. Escribe en cada uno qué hace. Debajo escribe una frase de agradecimiento a la comunidad.",
           "Comunidad: enseña los turnos. Junta de vecinos: los usa en el pueblo. Escuela del pueblo: los usa en su huerto. Otra región: pide permiso. Gracias a la comunidad de Valle Alto por compartir sus turnos de agua.",
           ["incluye los cuatro círculos", "las acciones salen de la ficha", "agradece a la comunidad"], ["cadena de cuatro círculos", "agradecimiento"], ["saltar el permiso", "no nombrar la comunidad"],
           "Preguntar cómo llegó el aporte a cada lugar; valorar el agradecimiento."),
    reinforce="Une con flechas comunidad, localidad y país en el orden correcto.",
    extend="Escribe una pregunta para el educador tradicional sobre un saber de tu comunidad que enriquece a tu localidad.",
)

L(
    OA8, 4,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a valorar las culturas indígenas sin apropiarme de lo que no es mío y sin tratar a todos los pueblos como iguales. Sirve para respetar de verdad.",
    prior=["Sé examinar un aporte.", "Sé que cada comunidad es distinta."],
    explain=[
        "Valorar es reconocer que algo es importante y tratarlo con respeto. Una manera de valorar es escuchar, preguntar con permiso y dar crédito. Otra es cuidar lo que la comunidad pide cuidar.",
        "Apropiarse es usar como propio algo que pertenece a otra comunidad, sin permiso y sin decir de dónde viene. Por ejemplo, copiar un diseño y decir que es tuyo, o imitar una ceremonia como juego. Eso no es valorar.",
        "Homogeneizar es tratar a todos los pueblos como si fueran iguales. Decir «los indígenas hacen esto» sin decir de qué pueblo habla borra las diferencias. Valorar es hablar de una comunidad concreta, con su fuente y su permiso.",
    ],
    vocab=[("valorar", "reconocer que algo es importante y tratarlo con respeto"), ("apropiarse", "usar como propio algo ajeno sin permiso"), ("homogeneizar", "tratar como iguales cosas que son distintas"), ("crédito", "reconocimiento a quien hizo o enseñó algo"), ("diversidad", "variedad de personas, culturas y formas de vivir")],
    worked=[
        W("Valorar o apropiarse", "Un curso ve un diseño de una comunidad inventada y lo copia para su afiche, diciendo que lo inventó. ¿Valora o se apropia?", ["Copian el diseño.", "No piden permiso ni dicen de dónde viene.", "Eso es apropiarse."], "Se apropia."),
        W("Evitar homogeneizar", "Un niño dice: «Los indígenas cosechan todos en otoño». ¿Qué le falta?", ["No dice de qué pueblo habla.", "No hay fuente.", "Hay que hablar de una comunidad concreta."], "Le falta decir de qué comunidad habla y quién lo cuenta."),
    ],
    mistakes=[
        M("Jugar a imitar una ceremonia en el recreo.", "Es usar como juego algo muy importante para otros.", "Si te interesa, pregunta al educador tradicional qué se puede aprender."),
        M("Hablar de «los indígenas» como si fueran un solo grupo.", "Hay muchos pueblos y cada uno es distinto.", "Nombra la comunidad y la fuente."),
    ],
    R=[
        ex("Copiar un diseño de una comunidad y decir que es tuyo, ¿es valorar o apropiarse?", "Apropiarse", "Usa algo ajeno sin permiso ni crédito."),
        ex("Pedir permiso, escuchar y dar crédito, ¿es valorar o apropiarse?", "Valorar", "Son acciones de respeto."),
        ex("Decir «los indígenas hacen todos lo mismo», ¿trata a los pueblos como iguales o como distintos?", "Como iguales", "Eso es homogeneizar."),
    ],
    C=[
        ex("¿Qué es homogeneizar? A) tratar como iguales cosas que son distintas B) cuidar una huerta", "A", "Borra las diferencias."),
        ex("Verdadero o falso: imitar una ceremonia como juego es una forma de valorarla.", "Falso", "Es apropiarse de algo muy importante."),
        ex("Verdadero o falso: dar crédito a quien enseñó algo es valorar.", "Verdadero", "Reconoce de dónde viene el saber."),
    ],
    A=[
        ex("Clasifica en VALORAR o APROPIARSE: a) pedir permiso para contar una historia b) usar un diseño sin decir de dónde viene c) agradecer a la comunidad.", "a valorar, b apropiarse, c valorar", "Pedir permiso y agradecer valoran; usar sin decir apropia."),
        ex("Para no homogeneizar la frase «Los indígenas tienen huertas», ¿qué dos datos agregas? A) la comunidad y la fuente B) el color y el tamaño de la huerta", "A", "Hay que decir de qué comunidad habla y quién lo cuenta."),
        ex("Cuenta cuántas son prácticas de respeto: 1) pedir permiso 2) copiar sin decir 3) dar crédito 4) imitar una ceremonia como juego.", "2", "Solo pedir permiso y dar crédito son respeto."),
    ],
    Z=[
        ex("Ema dice: «Si me gusta un diseño, puedo usarlo porque lo vi en un libro». ¿Qué error comete?", "Usa algo ajeno sin permiso", "Verlo en un libro no es tener permiso."),
        ex("Mateo dice: «Las comunidades son todas iguales, da lo mismo de cuál hablo». ¿Qué error comete?", "Homogeneiza", "Cada comunidad es distinta."),
    ],
    D=[
        ex("Un afiche tiene un diseño de una comunidad inventada, pone su nombre y agradece su permiso. ¿Valora o se apropia?", "Valora", "Hay permiso y crédito."),
        ex("Una niña propone invitar al educador tradicional para que cuente lo que quiera compartir. ¿Es una forma de valorar? Responde Sí o No.", "Sí", "Escucha a quien puede enseñar."),
    ],
    context=[ex("En el acto de la escuela quieren hacer un baile «de pueblos originarios» inventado por el curso. ¿Qué es mejor? A) Invitar al educador tradicional y escuchar qué se puede compartir B) Inventar el baile", "A", "Así se evita inventar y apropiarse.")],
    selfcheck=[
        ex("Escribe la diferencia entre valorar y apropiarse.", "Valorar es respetar con permiso y crédito; apropiarse es usar sin permiso", "Es lo central de la clase."),
        ex("Verdadero o falso: todos los pueblos hacen lo mismo.", "Falso", "Hay mucha diversidad."),
        ex("¿Qué haces si quieres usar algo de una comunidad? A) Pedir permiso B) Copiarlo", "A", "El permiso es el primer paso."),
    ],
    task=T("Lee estos tres casos inventados. Caso 1: un curso copia un diseño y dice que lo inventó. Caso 2: un curso invita al educador tradicional y le pide permiso para contar una historia. Caso 3: un niño dice «todos los pueblos hacen lo mismo». Escribe para cada caso si valora, se apropia o homogeneiza, y escribe cómo lo mejorarías en una frase.",
           "Caso 1: se apropia; mejorar: pedir permiso y dar crédito. Caso 2: valora; ya pide permiso y escucha. Caso 3: homogeneiza; mejorar: hablar de una comunidad concreta con su fuente.",
           ["clasifica correctamente los tres casos", "propone una mejora respetuosa", "no inventa datos"], ["tabla de tres casos", "frases de mejora"], ["confundir homogeneizar con apropiarse sin explicar", "no proponer mejora"],
           "Preguntar qué acción hace que cada caso sea valorar o no; reforzar la propuesta de pedir permiso."),
    reinforce="Colorea de verde las acciones que valoran y de rojo las que se apropian en la lista de la clase.",
    extend="Escribe una regla de tres frases para tu curso sobre cómo usar saberes de otras culturas.",
)

# ============================================================ OA 09 · Nociones indígenas de tiempo y espacio
L(
    OA9, 1,
    materials="Lápiz y hojas. La ficha de práctica está escrita aquí y es inventada.",
    use="Aprenderé a situar de qué pueblo y de qué fuente viene una idea de tiempo o de espacio. Sirve para no mezclar ni generalizar nociones de pueblos distintos.",
    prior=["Sé situar un territorio con una ficha.", "Sé que cada comunidad tiene su manera de vivir."],
    explain=[
        "Tiempo y espacio son maneras de ordenar lo que vivimos. El tiempo ordena cuándo pasan las cosas: días, estaciones, años. El espacio ordena dónde están las cosas: cerca, lejos, arriba, abajo. Cada pueblo puede ordenarlos a su manera.",
        "Una noción es una idea sobre algo. Cuando hablamos de la noción de tiempo de un pueblo, decimos cómo ese pueblo entiende y organiza el tiempo. Esa idea la cuenta la propia comunidad, con sus palabras.",
        "Para estudiar una noción de tiempo o espacio hay que situarla: ¿de qué pueblo es?, ¿quién la cuenta? y ¿tiene permiso? No se mezclan las ideas de pueblos distintos ni se dice que valen para todos. En esta clase usamos una ficha inventada para practicar.",
    ],
    vocab=[("noción", "idea que se tiene sobre algo"), ("tiempo", "manera de ordenar cuándo pasan las cosas"), ("espacio", "manera de ordenar dónde están las cosas"), ("perspectiva", "manera particular de mirar algo"), ("situar", "decir de quién es y quién lo cuenta")],
    worked=[
        W("Situar una noción", "Ficha inventada: «En Valle Alto los vecinos dicen que es tiempo de siembra cuando florece el árbol del patio. Lo cuenta doña Rosa. Permiso: sí.» ¿De qué comunidad es, quién cuenta y qué noción de tiempo aparece?", ["Comunidad: Valle Alto.", "Fuente: doña Rosa.", "Noción: el tiempo se reconoce por lo que pasa en la naturaleza."], "De Valle Alto; la cuenta doña Rosa; el tiempo se reconoce con lo que pasa en la naturaleza."),
        W("No mezclar", "Un niño dice: «Como en Valle Alto, todos los pueblos esperan que florezca un árbol para sembrar». ¿Qué error hay?", ["La ficha es de Valle Alto.", "No habla de otros pueblos.", "Está generalizando."], "Generaliza una ficha de una comunidad a todos los pueblos."),
    ],
    mistakes=[
        M("Decir que todos los pueblos entienden el tiempo igual.", "Cada pueblo puede organizar el tiempo a su manera.", "Nombra el pueblo y la fuente."),
        M("Pensar que la manera de la escuela de medir el tiempo es la única posible.", "Hay otras maneras de ordenar el tiempo y todas se pueden estudiar con respeto.", "Compara sin decir cuál es mejor."),
    ],
    R=[
        ex("Ficha inventada de Valle Alto: ¿quién cuenta la noción de tiempo?", "Doña Rosa", "La ficha la nombra como fuente."),
        ex("En la ficha, ¿cómo se sabe que es tiempo de siembra? A) cuando florece el árbol del patio B) cuando suena una campana", "A", "Lo dice la ficha."),
        ex("¿Qué ordena el espacio: cuándo pasan las cosas o dónde están las cosas?", "Dónde están las cosas", "Espacio es el dónde."),
    ],
    C=[
        ex("¿Qué es una noción? A) una idea sobre algo B) un tipo de comida", "A", "Es una idea."),
        ex("Verdadero o falso: todos los pueblos entienden el tiempo de la misma manera.", "Falso", "Cada pueblo puede tener su manera."),
        ex("¿Qué debes preguntar para situar una noción? A) ¿de qué pueblo es y quién la cuenta? B) ¿cuánto cuesta?", "A", "Situar es decir pueblo y fuente."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «Los pescadores saben que es tiempo de salir al mar cuando baja la marea de la tarde. Lo cuenta don Luis.» Escribe qué noción de tiempo aparece.", "El tiempo se reconoce por la marea", "Se guía por un hecho de la naturaleza."),
        ex("Clasifica en TIEMPO o ESPACIO: a) cuándo se siembra b) dónde queda la vertiente c) qué estación viene.", "a tiempo, b espacio, c tiempo", "Cuándo y estación ordenan el tiempo; dónde, el espacio."),
        ex("La ficha de Valle Alto dice: «Es tiempo de siembra cuando florece el árbol del patio». ¿Esa señal ordena el tiempo o el espacio?", "El tiempo", "Dice cuándo sembrar."),
    ],
    Z=[
        ex("Ema dice: «Si en Valle Alto esperan a que florezca un árbol, entonces ese es el calendario de todos los pueblos». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "La ficha es de una comunidad."),
        ex("Pedro mezcla la ficha de Valle Alto con la de Costa Clara y dice que en las dos la marea indica la siembra. ¿Qué error comete?", "Mezcla datos de dos comunidades", "La marea está en la ficha de Costa Clara."),
    ],
    D=[
        ex("Una niña pregunta: «¿Cómo entiende el tiempo mi comunidad?». ¿A quién conviene preguntar? A) al educador tradicional o a la comunidad B) a un buscador al azar", "A", "La noción la cuenta la propia comunidad."),
        ex("Un dato dice «en Valle Alto se siembra cuando florece el árbol del patio» y otro «la escuela tiene vacaciones en verano». ¿Son maneras de ordenar el tiempo distintas? Responde Sí o No.", "Sí", "Una usa una señal de la naturaleza y la otra el calendario."),
    ],
    context=[ex("Un libro dice que «los pueblos originarios organizan el tiempo así» y no nombra ningún pueblo ni fuente. ¿Qué haces? A) Desconfío y pregunto de qué pueblo habla B) Lo copio", "A", "Falta situar la información.")],
    selfcheck=[
        ex("Escribe qué ordena el tiempo y qué ordena el espacio.", "El tiempo ordena cuándo y el espacio ordena dónde", "Es la idea de la explicación."),
        ex("Verdadero o falso: puedo mezclar nociones de pueblos distintos.", "Falso", "Cada una se estudia por separado."),
        ex("¿Qué dos datos necesito para situar una noción?", "El pueblo y la fuente", "Son lo mínimo para situarla."),
    ],
    task=T("Lee dos fichas inventadas. Valle Alto: «Es tiempo de siembra cuando florece el árbol del patio. Lo cuenta doña Rosa. Permiso: sí.» Costa Clara: «Es tiempo de salir al mar cuando baja la marea de la tarde. Lo cuenta don Luis. Permiso: sí.» Haz una tabla con dos filas y las columnas: comunidad, fuente, cómo se reconoce el tiempo. Escribe una frase que diga por qué no debes mezclar las dos fichas.",
           "Valle Alto; doña Rosa; por la flor del árbol del patio. Costa Clara; don Luis; por la marea de la tarde. No debo mezclarlas porque son comunidades distintas con fuentes distintas.",
           ["completa la tabla con datos de las fichas", "explica por qué no mezclar", "no agrega datos"], ["tabla de dos filas", "frase de explicación"], ["decir que todas las comunidades usan las mismas señales", "agregar fechas reales"],
           "Preguntar qué dice cada ficha; reforzar la idea de que cada comunidad tiene su manera."),
    reinforce="Pinta con un color los datos de Valle Alto y con otro los de Costa Clara.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo su comunidad reconoce el tiempo.",
)

L(
    OA9, 2,
    materials="Lápiz y hojas. El calendario inventado está escrito aquí.",
    use="Aprenderé a explorar una noción de tiempo basada en ciclos, usando un ejemplo inventado. Sirve para entender que el tiempo se puede ordenar de maneras distintas.",
    prior=["Sé que cada comunidad ordena el tiempo a su manera.", "Sé nombrar las estaciones del año."],
    explain=[
        "Un ciclo es una serie de pasos que se repite. Las estaciones forman un ciclo: primavera, verano, otoño e invierno, y después otra vez primavera. El día y la noche también forman un ciclo.",
        "Hay maneras de ordenar el tiempo que se apoyan en ciclos de la naturaleza y del trabajo. La escuela usa días, meses y años, que también son ciclos. Una comunidad puede apoyarse en lo que ocurre en la huerta, el mar o el cielo.",
        "En esta clase usamos un calendario inventado de Valle Alto, con cuatro tiempos de trabajo: preparar, sembrar, cosechar y descansar. Es solo una práctica. Cómo ordena el tiempo una comunidad real lo cuenta la propia comunidad.",
    ],
    vocab=[("ciclo", "serie de pasos que se repite"), ("estación", "cada una de las cuatro partes del año"), ("calendario", "forma de ordenar los días, meses y tiempos"), ("repetir", "volver a ocurrir"), ("señal", "algo que avisa que ocurrirá otra cosa")],
    worked=[
        W("Reconocer un ciclo", "¿Es un ciclo esta serie: primavera, verano, otoño, invierno, y vuelve primavera?", ["Reviso si vuelve al inicio.", "Sí, después del invierno vuelve la primavera.", "Entonces se repite."], "Sí, es un ciclo."),
        W("Calendario inventado", "Calendario inventado de Valle Alto: preparar la tierra, sembrar, cosechar y descansar la tierra; luego vuelve a empezar. ¿Qué viene después de descansar?", ["Leo el orden.", "Después de descansar empieza otro ciclo.", "Vuelve preparar la tierra."], "Preparar la tierra."),
    ],
    mistakes=[
        M("Pensar que el tiempo solo avanza en línea y nunca vuelve.", "Muchos hechos del tiempo se repiten en ciclos.", "Busca qué se repite."),
        M("Creer que el calendario de la escuela es el único posible.", "Hay otras maneras de ordenar el tiempo.", "Compara sin decir cuál es mejor."),
    ],
    R=[
        ex("¿Cuál es la estación que sigue al invierno? A) primavera B) otoño", "A", "Después del invierno viene la primavera."),
        ex("Día, noche y luego otra vez día. ¿Es un ciclo?", "Sí", "Todo se repite."),
        ex("En el calendario de Valle Alto, ¿qué se hace primero: preparar la tierra o cosechar?", "Preparar la tierra", "Es el primer paso."),
    ],
    C=[
        ex("¿Qué es un ciclo? A) una serie de pasos que se repite B) un hecho que ocurre una sola vez", "A", "Un ciclo se repite."),
        ex("Verdadero o falso: las estaciones del año forman un ciclo.", "Verdadero", "Después del invierno vuelve la primavera."),
        ex("Verdadero o falso: solo hay una manera correcta de ordenar el tiempo.", "Falso", "Hay maneras distintas."),
    ],
    A=[
        ex("Ordena el ciclo de Valle Alto: a) cosechar b) descansar la tierra c) sembrar d) preparar la tierra. Escribe las letras.", "d, c, a, b", "Se prepara, se siembra, se cosecha y se descansa."),
        arith("Si el ciclo de Valle Alto tiene 4 tiempos y se repite 3 veces, ¿cuántos tiempos pasan en total?", "4+4+4", "Se suman 4 tiempos tres veces."),
        ex("Clasifica en CICLO o HECHO ÚNICO: a) el invierno que vuelve cada año b) mi cumpleaños número 8.", "a ciclo, b hecho único", "El invierno vuelve; el cumpleaños 8 ocurre una vez."),
    ],
    Z=[
        ex("Pedro dice: «En el calendario de Valle Alto el descanso de la tierra es una pérdida de tiempo». ¿Qué debe considerar según el calendario?", "Que el descanso es un tiempo del ciclo", "Es parte del ciclo."),
        ex("Ana afirma que el calendario inventado de Valle Alto es el de los pueblos reales. ¿Qué error comete?", "Confunde un ejemplo inventado con un pueblo real", "Es una práctica inventada."),
    ],
    D=[
        ex("Un niño dice que el calendario de la escuela es mejor que el ciclo de Valle Alto (inventado) en todo. ¿Tiene razón? Responde Sí o No.", "No", "Ordenan el tiempo para cosas distintas."),
        ex("Si cada tiempo del calendario de Valle Alto dura varias semanas, ¿el ciclo completo dura menos o más que una semana?", "Más", "Cada tiempo ya dura varias semanas."),
    ],
    context=[ex("Julia ve que su abuela espera que florezca un árbol de su casa para sembrar. ¿Qué tipo de idea del tiempo usa la abuela? A) se guía por un ciclo de la naturaleza B) se guía por un reloj", "A", "Usa una señal de la naturaleza que se repite.")],
    selfcheck=[
        ex("Escribe un ejemplo de ciclo.", "Las estaciones, el día y la noche o el ciclo de Valle Alto", "Son series que se repiten."),
        ex("Verdadero o falso: un ciclo no se repite.", "Falso", "Un ciclo se repite."),
        ex("¿Qué viene después de descansar la tierra en el calendario de Valle Alto?", "Preparar la tierra", "El ciclo empieza otra vez."),
    ],
    task=T("Dibuja un círculo dividido en cuatro partes para el calendario inventado de Valle Alto: preparar la tierra, sembrar, cosechar y descansar. Pon una flecha que vaya de una parte a la siguiente y que vuelva al inicio. Escribe una frase que explique por qué es un ciclo. Añade una pregunta para el educador tradicional sobre cómo su comunidad ordena el tiempo.",
           "Círculo con las cuatro partes en orden y una flecha final que vuelve a «preparar la tierra». Es un ciclo porque cuando termina vuelve a empezar. Pregunta: ¿cómo ordena nuestra comunidad el paso del tiempo?",
           ["dibuja las cuatro partes en orden", "la flecha vuelve al inicio", "explica por qué es un ciclo"], ["círculo con flechas", "frase de explicación", "pregunta"], ["dibujar una línea recta sin volver", "decir que es el calendario de un pueblo real"],
           "Preguntar qué pasa después de descansar; valorar que la flecha vuelva al inicio."),
    reinforce="Dibuja otro ciclo cotidiano, como el día y la noche, con flecha de regreso.",
    extend="Compara el ciclo de las estaciones con el calendario de Valle Alto: escribe una cosa igual y una distinta.",
)

L(
    OA9, 3,
    materials="Lápiz y hojas. La descripción del camino está escrita aquí y es inventada.",
    use="Aprenderé a explorar una noción de espacio: orientarme con elementos del territorio, como cerros y ríos. Sirve para entender que se puede ubicar un lugar de más de una manera.",
    prior=["Sé usar izquierda y derecha.", "Sé que el Sol sale por un lado y se pone por el otro."],
    explain=[
        "El espacio se puede ordenar con medidas, con mapas o con referencias del territorio. Una referencia es algo conocido que sirve para ubicarse, como un cerro, un río, un árbol o la salida del Sol. El Sol sale por el oriente (este) y se pone por el poniente (oeste).",
        "Una comunidad puede explicar un camino con referencias que todos conocen: «sigue el río hacia abajo» o «ten el cerro a tu izquierda». Esa manera de ubicarse es parte de cómo la comunidad entiende su espacio.",
        "En esta clase usamos un camino inventado de Valle Alto para practicar. La orientación de una comunidad real la cuenta la propia comunidad. No usamos mapas de lugares delicados ni sitios de respeto.",
    ],
    vocab=[("referencia", "algo conocido que sirve para ubicarse"), ("orientación", "manera de saber dónde estás y hacia dónde vas"), ("río arriba", "hacia el lugar de donde viene el agua"), ("río abajo", "hacia donde va el agua"), ("oriente", "lado por donde sale el Sol")],
    worked=[
        W("Seguir un camino con referencias", "Camino inventado de Valle Alto: «Desde la escuela, camina con el cerro Pelado a tu izquierda hasta el río. Cruza el puente y sigue el río hacia abajo hasta la vertiente.» ¿Cuál es el punto de llegada?", ["Leo cada indicación.", "Llego al río, cruzo el puente.", "Sigo el río hacia abajo hasta la vertiente."], "La vertiente."),
        W("Río arriba y río abajo", "El agua del río va desde el cerro hacia el valle. Si caminas hacia el cerro, ¿vas río arriba o río abajo?", ["El agua viene del cerro.", "Caminar hacia donde viene el agua es río arriba.", "Entonces es río arriba."], "Río arriba."),
    ],
    mistakes=[
        M("Confundir izquierda y derecha al seguir un camino escrito.", "Depende de hacia dónde miras.", "Imagina que caminas por el camino y usa tus manos."),
        M("Pensar que solo vale la manera del mapa de papel.", "También se ubica con referencias del territorio.", "Usa ambas maneras sin decir cuál es mejor."),
    ],
    R=[
        ex("Según el camino inventado, ¿qué cerro tienes a la izquierda? A) el cerro Pelado B) el cerro Verde", "A", "Lo dice el camino."),
        ex("¿Por dónde sale el Sol: por el oriente o por el poniente?", "Por el oriente", "El Sol sale por el oriente."),
        ex("Caminar hacia donde va el agua, ¿es río arriba o río abajo?", "Río abajo", "El agua va hacia abajo."),
    ],
    C=[
        ex("¿Qué es una referencia? A) algo conocido que sirve para ubicarse B) un papel en blanco", "A", "Un cerro o un río son referencias."),
        ex("Verdadero o falso: solo se puede ubicar un lugar con un mapa de papel.", "Falso", "También con referencias del territorio."),
        ex("Verdadero o falso: río arriba es hacia el lugar de donde viene el agua.", "Verdadero", "Es hacia el nacimiento del río."),
    ],
    A=[
        ex("Sigue el camino inventado: escuela, cerro Pelado a la izquierda, río, puente, río abajo, vertiente. Sin contar la escuela, ¿cuántas cosas del territorio nombra el camino? Escribe el número.", "4", "Nombra el cerro, el río, el puente y la vertiente."),
        ex("Si desde la vertiente quieres volver a la escuela, ¿qué sentido sigues respecto al río? A) río arriba B) río abajo", "A", "Para volver sigues al revés: río arriba."),
        ex("Estás de frente al oriente, por donde sale el Sol. ¿El poniente queda delante o detrás de ti?", "Detrás", "El poniente es el lado opuesto al oriente."),
    ],
    Z=[
        ex("Tomás dice que «hacia abajo» es siempre hacia el suelo. ¿Qué entiende mal en «río abajo»?", "Que es hacia donde va el agua", "Río abajo es hacia donde corre el agua."),
        ex("Ema dice que el camino inventado de Valle Alto es el que usa cualquier pueblo. ¿Qué error comete?", "Confunde un ejemplo con un pueblo real", "Es una práctica inventada."),
    ],
    D=[
        ex("Dos maneras de ubicar la vertiente: 1) en un mapa con una cruz, 2) «siguiendo el río hacia abajo». Un niño dice que solo la 1 es correcta. ¿Tiene razón? Responde Sí o No.", "No", "Son maneras distintas, útiles en situaciones distintas."),
        ex("Un visitante quiere mostrar en internet el camino exacto a un sitio de respeto. ¿Debe hacerlo? Responde Sí o No.", "No", "Los sitios delicados se resguardan."),
    ],
    context=[ex("Un niño de Valle Alto (inventado) le explica a su prima el camino a la vertiente con el cerro y el río. ¿Qué usa para ubicar el lugar? A) referencias del territorio B) solo números", "A", "Usa cerro y río.")],
    selfcheck=[
        ex("Escribe dos referencias del territorio.", "Dos de estas: cerro, río, árbol, puente", "Sirven para ubicarse."),
        ex("Verdadero o falso: río abajo es hacia donde viene el agua.", "Falso", "Río abajo es hacia donde va el agua."),
        ex("¿Se muestran en internet los sitios de respeto de una comunidad? Responde Sí o No.", "No", "Se resguardan siempre."),
    ],
    task=T("Lee este camino inventado: «Desde la escuela de Valle Alto, camina con el cerro Pelado a tu izquierda hasta el río. Cruza el puente y sigue el río hacia abajo hasta la vertiente.» Dibuja un esquema con la escuela, el cerro, el río, el puente y la vertiente en ese orden, con flechas. Escribe qué referencias del territorio usa el camino. No dibujes sitios de respeto.",
           "Esquema: escuela → cerro Pelado a la izquierda → río → puente → río abajo → vertiente. Referencias: cerro, río, puente.",
           ["pone los cinco lugares en el orden del texto", "nombra las referencias", "no dibuja sitios delicados"], ["esquema con flechas", "lista de referencias"], ["cambiar el orden", "inventar lugares que el texto no nombra"],
           "Verificar el orden; preguntar qué referencia ayuda a no perderse."),
    reinforce="Escribe tres instrucciones para ir del patio a la sala usando referencias.",
    extend="Compara cómo ubicas la escuela con un mapa y con referencias: escribe una ventaja de cada una.",
)

L(
    OA9, 4,
    materials="Lápiz y hojas. La tabla comparativa está escrita aquí.",
    use="Aprenderé a comparar maneras de ordenar el tiempo y el espacio sin decir cuál es mejor y diciendo hasta dónde llega lo que sé. Sirve para respetar diferencias.",
    prior=["Sé qué es un ciclo.", "Sé orientarme con referencias del territorio."],
    explain=[
        "Comparar es mirar dos cosas para ver qué se parece y qué es distinto. Al comparar maneras de ordenar el tiempo y el espacio, buscamos semejanzas y diferencias, pero no decimos que una sea mejor.",
        "Cada manera sirve para algo. El calendario de la escuela sirve para organizar las clases de la escuela. Un calendario de trabajo de la huerta de una comunidad sirve para saber cuándo sembrar. Ninguno es mejor en todo.",
        "También reconocemos los límites de lo que sabemos. Una ficha inventada o una fuente solo nos habla de una comunidad. Para conocer de verdad cómo ordena el tiempo y el espacio una comunidad, la consultamos a ella.",
    ],
    vocab=[("comparar", "mirar dos cosas para ver semejanzas y diferencias"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas son distintas"), ("jerarquizar", "decir que una cosa es mejor o más importante que otra"), ("límite", "hasta dónde llega lo que sabemos")],
    worked=[
        W("Comparar dos maneras de ordenar el tiempo", "Tabla: Escuela: semana de lunes a viernes, vacaciones en verano y en invierno. Valle Alto (inventado): preparar, sembrar, cosechar y descansar la tierra. ¿Qué tienen en común?", ["Ambas ordenan el tiempo.", "Ambas se repiten.", "Escribo la semejanza."], "Las dos son ciclos que se repiten y ordenan el tiempo."),
        W("No jerarquizar", "Un niño dice: «El calendario de la escuela es mejor porque tiene números». ¿Qué responderías?", ["Cada calendario sirve para algo distinto.", "El de la huerta sirve para saber cuándo sembrar.", "No se dice cuál es mejor."], "Que cada uno sirve para algo distinto y no hay uno mejor en todo."),
    ],
    mistakes=[
        M("Decir cuál manera de ordenar el tiempo es mejor.", "Cada manera sirve para algo distinto.", "Di semejanzas y diferencias, no premios."),
        M("Hablar de todos los pueblos con un ejemplo inventado.", "El ejemplo solo es de práctica.", "Declara el límite: «solo hablo de esta ficha»."),
    ],
    R=[
        ex("Tabla: la escuela usa semana de lunes a viernes. ¿Esto ordena el tiempo o el espacio?", "El tiempo", "La semana ordena cuándo."),
        ex("Tabla: el camino inventado usa cerro y río. ¿Esto ordena el tiempo o el espacio?", "El espacio", "Cerro y río ordenan dónde."),
        ex("¿Comparar es decir cuál es mejor o ver qué se parece y qué es distinto?", "Ver qué se parece y qué es distinto", "Comparar no es premiar."),
    ],
    C=[
        ex("Verdadero o falso: comparar dos maneras de ordenar el tiempo significa elegir la mejor.", "Falso", "Se buscan semejanzas y diferencias."),
        ex("¿Qué es jerarquizar? A) decir que una cosa es mejor que otra B) dibujar una cosa", "A", "Es poner una sobre otra."),
        ex("Verdadero o falso: una ficha inventada nos dice cómo ordenan el tiempo todos los pueblos.", "Falso", "Solo es una práctica."),
    ],
    A=[
        ex("Escribe una semejanza entre el calendario de la escuela y el ciclo de Valle Alto (inventado).", "Los dos se repiten y ordenan el tiempo", "Ambos son ciclos."),
        ex("Escribe una diferencia: la escuela marca días y semanas; Valle Alto marca tiempos de trabajo de la huerta. ¿Qué marca Valle Alto?", "Tiempos de trabajo de la huerta", "Lo dice la tabla."),
        ex("Cuenta cuántas semejanzas hay en esta lista: 1) ambos ordenan el tiempo 2) ambos se repiten 3) uno usa semana y el otro usa tiempos de trabajo.", "2", "Las dos primeras son semejanzas; la tercera es diferencia."),
    ],
    Z=[
        ex("Mía dice: «Como el ciclo inventado de Valle Alto es de trabajo, entonces el de la escuela es peor». ¿Qué error comete?", "Jerarquiza", "No se dice cuál es mejor."),
        ex("Lía presenta la comparación y no dice que es una ficha inventada. ¿Qué límite le falta?", "Decir que es solo un ejemplo inventado", "Evita que parezca real."),
    ],
    D=[
        ex("Dos niños comparan. A: «La escuela mide con reloj, la comunidad con señales de la naturaleza». B: «La escuela es moderna y la comunidad es atrasada». ¿Quién compara sin jerarquizar?", "A", "B juzga una como mejor."),
        ex("Quieres saber cómo ordena el espacio la comunidad de tu zona. ¿A quién consultas? A) al educador tradicional B) a nadie", "A", "La comunidad es la fuente."),
    ],
    context=[ex("Tu curso hace un afiche comparando el calendario escolar y el ciclo de Valle Alto (inventado). ¿Qué frase pones al final? A) «Esto es solo una práctica; cada comunidad real lo cuenta» B) «El ciclo de Valle Alto es mejor»", "A", "Declara el límite y no jerarquiza.")],
    selfcheck=[
        ex("Escribe qué es comparar.", "Mirar dos cosas para ver semejanzas y diferencias", "Es la definición de la clase."),
        ex("Verdadero o falso: un buen trabajo dice qué manera de ordenar el tiempo es la mejor.", "Falso", "No dice cuál es mejor."),
        ex("¿Qué límite debes decir al usar una ficha inventada?", "Que es solo un ejemplo de práctica", "Así no parece de un pueblo real."),
    ],
    task=T("Completa esta comparación con tus palabras. Escuela: semana de lunes a viernes y dos periodos de vacaciones. Valle Alto (inventado): ciclo de preparar, sembrar, cosechar y descansar. Escribe en una tabla una semejanza, una diferencia y una frase que diga hasta dónde llega lo que sabes (el límite). No escribas cuál es mejor.",
           "Semejanza: las dos maneras se repiten. Diferencia: la escuela cuenta días y semanas; Valle Alto cuenta tiempos de trabajo. Límite: Valle Alto es una ficha inventada, no un pueblo real.",
           ["escribe una semejanza y una diferencia", "no jerarquiza", "declara un límite"], ["tabla con tres partes"], ["decir cuál es mejor", "no declarar que es inventado"],
           "Preguntar por qué una no es mejor; valorar que declare el límite."),
    reinforce="Marca con una S las semejanzas y con una D las diferencias en la tabla de la clase.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo su comunidad ordena el espacio.",
)

"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 12 (vida en armonía e interdependencia) y OA 13 (técnicas productivas ancestrales y vida comunitaria).

Criterio de autoría: las comunidades, las personas, los relatos y las técnicas de práctica son INVENTADOS y
se rotulan así. No se afirma nada de lengua, ritos, fechas, cosmovisión ni técnicas de un pueblo concreto.
La práctica de OA 13 es una versión escolar neutra (semillas en un vaso), no una técnica ancestral real:
la técnica verdadera la enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc3_a import L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA12, OA13 = "LC03 OA 12", "LC03 OA 13"

# ============================================================ OA 12 · Vida en armonía e interdependencia
L(
    OA12, 1,
    materials="Lápiz y hojas. Los relatos están escritos aquí y son inventados.",
    use="Aprenderé a reconocer relaciones concretas entre las personas, los seres vivos y el entorno. Sirve para entender que todo está conectado.",
    prior=["Sé que las plantas necesitan agua.", "Sé que las personas usan la naturaleza para vivir."],
    explain=[
        "Interdependencia significa que unos seres dependen de otros. Las plantas necesitan agua y sol. Los animales necesitan plantas. Las personas necesitan agua, alimentos y materiales de la naturaleza.",
        "Armonía significa que cada parte está en equilibrio con las otras. Cuando una comunidad cuida el agua, la huerta da alimentos, y las personas pueden vivir bien. Si el agua falta, todo lo demás se afecta.",
        "En esta clase usamos un relato inventado de Valle Alto para reconocer relaciones concretas. Cómo entiende esta relación una comunidad real lo cuenta la propia comunidad. Nosotros no decimos que todos los pueblos piensan igual.",
    ],
    vocab=[("interdependencia", "relación en que unos seres dependen de otros"), ("armonía", "equilibrio entre las partes"), ("entorno", "lo que rodea a las personas, como plantas, agua y animales"), ("relación", "conexión entre dos cosas o seres"), ("depender", "necesitar algo para vivir")],
    worked=[
        W("Encontrar la cadena", "Relato inventado de Valle Alto: «La vertiente da agua. El agua riega la huerta. La huerta da papas. Las papas alimentan a las familias.» ¿De qué depende la huerta?", ["Busco qué le da algo a la huerta.", "El agua la riega.", "Depende del agua."], "Depende del agua de la vertiente."),
        W("Si falta una parte", "Si la vertiente se seca, ¿qué parte de la cadena se afecta primero?", ["La vertiente es el inicio.", "Sin agua no hay riego.", "Se afecta el riego y luego lo demás."], "El agua y el riego de la huerta."),
    ],
    mistakes=[
        M("Pensar que las personas no dependen de la naturaleza.", "Necesitamos agua, alimentos y materiales de ella.", "Busca qué recibe cada parte."),
        M("Decir que todos los pueblos entienden la armonía igual.", "Cada comunidad la cuenta a su manera.", "Nombra la comunidad y la fuente."),
    ],
    R=[
        ex("En el relato inventado, ¿qué da agua a la huerta? A) la vertiente B) el puente", "A", "El relato lo dice."),
        ex("La huerta da papas. ¿Quién se alimenta con ellas?", "Las familias", "El relato lo dice."),
        ex("¿Qué necesitan las plantas para crecer: agua o televisión?", "Agua", "Las plantas necesitan agua y sol."),
    ],
    C=[
        ex("¿Qué es interdependencia? A) cuando unos seres dependen de otros B) cuando un ser vive solo", "A", "Hay relación entre seres."),
        ex("Verdadero o falso: las personas no dependen de la naturaleza.", "Falso", "Necesitamos agua, alimentos y materiales."),
        ex("Verdadero o falso: si el agua falta, se afecta la huerta.", "Verdadero", "La huerta depende del riego."),
    ],
    A=[
        ex("Ordena la cadena de Valle Alto: a) las familias comen papas b) la vertiente da agua c) la huerta da papas d) el agua riega la huerta. Escribe las letras.", "b, d, c, a", "Agua, riego, papas y alimento."),
        ex("Une cada parte con lo que hace en el relato. 1) la vertiente 2) la huerta 3) las papas a) da papas b) da agua c) alimentan a las familias", "1-b, 2-a, 3-c", "El relato dice que la vertiente da agua, la huerta da papas y las papas alimentan a las familias."),
        ex("Si la vertiente se seca, ¿qué parte recibe primero menos agua: la huerta o las familias?", "La huerta", "La huerta se riega con el agua de la vertiente."),
    ],
    Z=[
        ex("Pedro dice: «La huerta no necesita la vertiente». ¿Qué error comete?", "No ve que depende del agua", "La huerta depende del agua de la vertiente."),
        ex("Ema dice que ese relato inventado explica cómo ven la armonía todos los pueblos. ¿Qué error comete?", "Generaliza un relato inventado", "Cada comunidad lo cuenta a su manera."),
    ],
    D=[
        ex("Dos cadenas: 1) lluvia, pasto, oveja, familia; 2) vertiente, huerta, papas, familia. ¿En cuál aparece un animal?", "En la 1", "La oveja es un animal."),
        ex("Si cuidamos la vertiente, ¿cómo se afecta la cadena? A) todas las partes se favorecen B) todas se dañan", "A", "El cuidado del agua ayuda a toda la cadena."),
    ],
    context=[ex("Una escuela riega su huerto con agua de lluvia que juntó. ¿Qué relación muestra? A) que el huerto depende del agua y las personas la cuidan B) que no hay relación", "A", "Hay dependencia y cuidado.")],
    selfcheck=[
        ex("Escribe qué es la interdependencia.", "Cuando unos seres dependen de otros", "Es la definición."),
        ex("Verdadero o falso: la armonía es el equilibrio entre las partes.", "Verdadero", "Cada parte está equilibrada con las otras."),
        ex("Nombra una relación entre la naturaleza y las personas.", "Las personas usan el agua o las plantas", "Es una relación concreta."),
    ],
    task=T("Lee el relato inventado: «En Valle Alto, la vertiente da agua. El agua riega la huerta. La huerta da papas. Las papas alimentan a las familias. Las familias cuidan la vertiente.» Dibuja una cadena con cinco círculos y flechas. Debajo escribe una frase que explique por qué el cuidado hace que la cadena siga funcionando. Añade una pregunta para el educador tradicional sobre cómo su comunidad cuida su entorno.",
           "Vertiente → agua → huerta → papas → familias → vuelve a la vertiente. El cuidado hace que la vertiente siga dando agua. Pregunta: ¿cómo cuida nuestra comunidad el agua y la tierra?",
           ["dibuja la cadena con los datos del relato", "explica el papel del cuidado", "formula una pregunta"], ["cadena de círculos", "frase", "pregunta"], ["cortar la cadena en la mitad", "inventar una creencia"],
           "Preguntar qué pasaría si falla una parte; valorar que conecte el final con el inicio."),
    reinforce="Escribe tres cosas de la naturaleza de las que dependes cada día.",
    extend="Dibuja otra cadena con un animal y una planta, y escribe de qué depende cada uno.",
)

L(
    OA12, 2,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a analizar la reciprocidad y sus consecuencias: dar y recibir con la naturaleza. Sirve para entender por qué cuidar es tan importante.",
    prior=["Sé que unos seres dependen de otros.", "Sé qué es una cadena de relaciones."],
    explain=[
        "La reciprocidad es dar y recibir. Cuando recibimos algo de la naturaleza, como agua o algas, también podemos dar algo: cuidado, limpieza o descanso para que siga dando. Sin dar, algo se puede acabar.",
        "Una consecuencia es lo que pasa después de una acción. Si tomamos demasiado de un lugar, hay menos para después. Si cuidamos, hay para todos más tiempo. Por eso pensar en las consecuencias ayuda a decidir.",
        "En esta clase usamos casos inventados con números pequeños para ver las consecuencias de tomar mucho o poco. No describen el cuidado de ningún pueblo real. Las formas de cuidar de cada comunidad las cuenta la propia comunidad.",
    ],
    vocab=[("reciprocidad", "dar y recibir entre personas o con la naturaleza"), ("consecuencia", "lo que pasa después de una acción"), ("cuidar", "tomar lo necesario y proteger para que siga existiendo"), ("necesario", "lo que realmente hace falta"), ("agotarse", "acabarse hasta que no queda nada")],
    worked=[
        W("Calcular una consecuencia", "Caso inventado: en la playa de Costa Clara hay 20 matas de algas. Si se recogen 5 por temporada y las demás quedan, ¿cuántas quedan?", ["Parto de 20 matas.", "Resto las 5 recogidas.", "20 − 5 = 15."], "Quedan 15 matas."),
        W("Dar y recibir", "La comunidad recoge algas y también limpia la playa. ¿Qué recibe y qué da?", ["Recibe algas.", "Da limpieza.", "Esa es la reciprocidad."], "Recibe algas y da limpieza."),
    ],
    mistakes=[
        M("Tomar todo porque «hay muchas».", "Se puede agotar.", "Toma lo necesario y deja para después."),
        M("Pensar que solo recibimos de la naturaleza y no damos.", "La relación es de dar y recibir.", "Pregunta qué cuidado puedes dar."),
    ],
    R=[
        ex("Si recibes algas de la playa, ¿qué puedes dar a cambio: limpieza o más basura?", "Limpieza", "Cuidar es dar."),
        ex("¿Qué es una consecuencia? A) lo que pasa después de una acción B) una herramienta", "A", "Es el resultado."),
        ex("Tomar demasiado de un lugar, ¿deja más o menos para después?", "Menos", "Hay menos para el futuro."),
    ],
    C=[
        ex("Verdadero o falso: la reciprocidad es solo recibir.", "Falso", "Es dar y recibir."),
        ex("¿Qué significa «agotarse»? A) acabarse hasta que no queda nada B) crecer", "A", "No queda más."),
        ex("Verdadero o falso: pensar en las consecuencias ayuda a decidir mejor.", "Verdadero", "Muestra qué pasará después."),
    ],
    A=[
        arith("En la playa inventada hay 24 matas de algas. Se recogen 6. ¿Cuántas quedan?", "24-6", "Se resta lo recogido."),
        arith("Si cada temporada se recogen 4 matas de las 20 que hay y se hacen 3 temporadas, ¿cuántas se recogen en total?", "4+4+4", "Se suman 4 matas tres veces."),
        ex("Clasifica en DAR o RECIBIR: a) limpiar la playa b) recoger algas c) cuidar el agua.", "a dar, b recibir, c dar", "Limpiar y cuidar son dar; recoger es recibir."),
    ],
    Z=[
        ex("Pedro dice: «Si hay 20 matas, me llevo las 20». ¿Qué consecuencia tendrá?", "No quedarán algas para después", "Así se agotan las algas."),
        ex("Ema dice que si recogemos la mitad, quedará la otra mitad. Hay 20 matas y recoge 10. ¿Es correcto? Responde Sí o No.", "Sí", "Quedan 10 matas."),
    ],
    D=[
        arith("En una playa inventada hay 30 matas. Se recogen 8 el primer año y 7 el segundo. ¿Cuántas matas se recogieron en total?", "8+7", "Se suman los dos años."),
        ex("Una comunidad deja descansar la playa un año. ¿Qué crees que pasa con las algas? A) tendrán tiempo de crecer B) se acabarán más rápido", "A", "El descanso permite que se renueven."),
    ],
    context=[ex("Un grupo de vecinos recoge leña de un bosque inventado. ¿Qué hace para que haya para después? A) toma solo ramas secas y poca B) corta todos los árboles", "A", "Toma lo necesario y deja crecer.")],
    selfcheck=[
        ex("Escribe qué es la reciprocidad.", "Dar y recibir", "Es la definición."),
        ex("Verdadero o falso: tomar todo siempre es lo mejor.", "Falso", "Se puede agotar."),
        ex("Escribe una consecuencia de cuidar bien un lugar.", "Hay para todos más tiempo", "El cuidado permite que dure."),
    ],
    task=T("Lee este caso inventado: «En una playa de Costa Clara hay 20 matas de algas. La comunidad recoge 5 matas por temporada y limpia la playa antes y después.» Calcula cuántas quedan después de una temporada y después de dos temporadas si no crecen más. Escribe qué recibe y qué da la comunidad. Añade una pregunta para el educador tradicional sobre cómo su comunidad cuida lo que recoge.",
           "Después de una temporada quedan 15; después de dos, 10. Recibe algas y da limpieza. Pregunta: ¿cómo cuida nuestra comunidad lo que recoge de la naturaleza?",
           ["calcula correctamente", "identifica qué recibe y qué da", "formula una pregunta"], ["cálculos", "frases", "pregunta"], ["tomar todas las algas", "no mencionar qué da"],
           "Revisar las restas; preguntar qué pasaría con tres temporadas."),
    reinforce="Escribe una acción que da y otra que recibe en tu casa.",
    extend="Inventa un caso con otro recurso, como agua o leña, y escribe su consecuencia si se toma demasiado.",
)

L(
    OA12, 3,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a comparar decisiones de cuidado y a elegir la que mejor mantiene el equilibrio. Sirve para decidir con criterios claros.",
    prior=["Sé qué es la reciprocidad.", "Sé que las acciones tienen consecuencias."],
    explain=[
        "Una decisión de cuidado es una elección que protege el entorno. Para comparar decisiones usamos criterios, que son preguntas simples. ¿Toma solo lo necesario? ¿Deja para después? ¿Devuelve algo? ¿Pregunta a quien conoce?",
        "Cuando una decisión cumple más criterios, mantiene mejor el equilibrio. Pero no se trata de ganar puntos: se trata de pensar qué pasa después. Una decisión puede parecer rápida y traer problemas.",
        "En esta clase comparamos casos inventados. Cómo decide una comunidad real lo cuenta ella misma. No decimos que un pueblo sea mejor que otro por sus decisiones.",
    ],
    vocab=[("criterio", "pregunta o regla que sirve para comparar y decidir"), ("equilibrio", "estado en que nada sobra ni falta"), ("devolver", "dar algo a cambio de lo recibido"), ("comparar", "mirar dos cosas para ver semejanzas y diferencias"), ("necesidad", "lo que realmente hace falta")],
    worked=[
        W("Comparar dos decisiones", "Decisión A: una comunidad inventada toma solo las ramas secas que necesita. Decisión B: otra corta un árbol entero «por si acaso». ¿Cuál cumple «toma solo lo necesario»?", ["Miro cada decisión.", "A toma solo lo necesario.", "B toma más de lo que necesita."], "La decisión A."),
        W("Usar varios criterios", "Decisión A además planta una semilla donde sacó leña. ¿Qué criterio cumple?", ["Plantar es devolver.", "Cumple devolver.", "Respondo."], "Devolver."),
    ],
    mistakes=[
        M("Elegir la decisión más rápida sin pensar en las consecuencias.", "Puede dañar el equilibrio.", "Revisa los criterios antes de elegir."),
        M("Decir que un pueblo es mejor porque su decisión de práctica gana.", "Los casos son inventados y no comparan pueblos.", "Compara decisiones, no pueblos."),
    ],
    R=[
        ex("Tomar solo lo necesario, ¿es una buena decisión de cuidado? Responde Sí o No.", "Sí", "Deja para después."),
        ex("Plantar una semilla donde sacaste leña, ¿es devolver o es tomar?", "Devolver", "Das algo a cambio."),
        ex("¿Qué es un criterio? A) una pregunta que sirve para comparar B) un tipo de árbol", "A", "Ayuda a decidir."),
    ],
    C=[
        ex("Verdadero o falso: una decisión rápida siempre cuida el entorno.", "Falso", "Puede dañar el entorno."),
        ex("¿Qué decisión mantiene más equilibrio? A) tomar lo necesario y devolver B) tomar todo", "A", "No agota el recurso."),
        ex("Verdadero o falso: se compara decisiones, no pueblos.", "Verdadero", "Los casos son inventados."),
    ],
    A=[
        ex("Cuenta cuántos criterios cumple la decisión: «toma solo lo necesario, deja para después y planta una semilla». Los criterios son: necesario, dejar, devolver, preguntar.", "3", "Cumple necesario, dejar y devolver."),
        ex("Clasifica en CUIDA o NO CUIDA: a) tomar solo ramas secas b) cortar un árbol entero sin necesidad c) preguntar a quien conoce.", "a cuida, b no cuida, c cuida", "Tomar poco y preguntar cuidan."),
        ex("Decisión 1: toma 5 matas de 20 y deja 15. Decisión 2: toma 18 y deja 2. ¿Cuál deja más para después?", "La decisión 1", "Deja 15, no 2."),
    ],
    Z=[
        ex("La decisión 2 toma 18 matas de 20 y deja 2. Tomás dice que es mejor porque toma más. ¿Qué error comete?", "No piensa en lo que pasará después", "Dejaría muy poco."),
        ex("Ema dice que una comunidad inventada es mejor que otra porque su decisión cumple más criterios. ¿Qué error comete?", "Compara pueblos y no decisiones", "Los casos son inventados."),
    ],
    D=[
        ex("Dos decisiones: A) pedir ayuda a una persona que conoce el lugar y tomar poco; B) tomar poco sin preguntar. ¿Cuál cumple más criterios?", "A", "Toma poco y pregunta."),
        ex("Si dos decisiones cumplen los mismos criterios, ¿se puede decir que una es mejor? Responde Sí o No.", "No", "Son igual de buenas según esos criterios."),
    ],
    context=[ex("En tu escuela hay un huerto. Un curso quiere regar con un balde que usa agua lluvia y otro con la manguera abierta mucho rato. ¿Cuál cuida más el agua? A) el balde con lluvia B) la manguera abierta", "A", "Usa poca agua.")],
    selfcheck=[
        ex("Escribe tres criterios para comparar decisiones de cuidado.", "Tomar lo necesario, dejar para después, devolver o preguntar", "Son criterios de la clase."),
        ex("Verdadero o falso: se compara pueblos con casos inventados.", "Falso", "Se comparan decisiones."),
        ex("¿Qué decisión mantiene más equilibrio?", "La que toma lo necesario y devuelve", "No agota el recurso."),
    ],
    task=T("Lee dos decisiones inventadas. A: «Una comunidad toma solo las ramas secas que necesita, deja las demás y planta un arbolito.» B: «Otra comunidad corta un árbol grande por si acaso, se lleva todas las ramas y no planta nada.» Haz una tabla con los criterios (toma lo necesario, deja para después, devuelve) y marca con ✓ o ✗ cada decisión. Escribe cuál mantiene más equilibrio y por qué. Añade una pregunta para el educador tradicional.",
           "A: ✓ ✓ ✓. B: ✗ ✗ ✗. La A mantiene más equilibrio porque toma poco, deja para después y devuelve. Pregunta: ¿cómo decide nuestra comunidad qué tomar y qué dejar?",
           ["marca los criterios correctamente", "explica cuál mantiene más equilibrio", "no compara pueblos"], ["tabla", "explicación", "pregunta"], ["decir que un pueblo es mejor", "marcar al azar"],
           "Preguntar por qué cada ✓ o ✗; valorar que compare decisiones y no pueblos."),
    reinforce="Subraya en cada decisión las palabras que muestran cuidado.",
    extend="Inventa una tercera decisión de cuidado y marca cuántos criterios cumple.",
)

L(
    OA12, 4,
    materials="Lápiz y hojas. Las opciones de acción están escritas aquí. No se usan herramientas cortantes ni productos químicos.",
    use="Aprenderé a proponer una acción concreta para cuidar el entorno en mi escuela o casa, respetando a la comunidad. Sirve para pasar de entender a actuar.",
    prior=["Sé comparar decisiones de cuidado.", "Sé qué es la reciprocidad."],
    explain=[
        "Una acción situada es una acción pensada para un lugar y unas personas concretas. No sirve una idea general; hay que decir qué se hará, quién, dónde y cuándo. Así se puede cumplir.",
        "Una buena acción de cuidado es segura, sencilla y devuelve algo al entorno. Por ejemplo, regar las plantas del patio con agua que sobró, juntar basura con guantes y bolsa, o dejar un recipiente con agua para los pájaros. No usamos herramientas filosas ni sustancias peligrosas.",
        "Antes de actuar, preguntamos a una persona adulta y, si el tema es cultural, al educador tradicional. No decidimos por la comunidad ni decimos que nuestra acción es una costumbre de un pueblo. Es nuestra propuesta.",
    ],
    vocab=[("acción", "algo que se hace para lograr un objetivo"), ("propuesta", "idea que se ofrece para que otros la consideren"), ("situada", "pensada para un lugar y personas concretas"), ("seguro", "que no pone en peligro a nadie"), ("responsable", "persona que se encarga de algo")],
    worked=[
        W("Armar la acción", "Propuesta: regar las plantas del patio con el agua que sobra de los vasos. ¿Qué datos faltan para que sea situada?", ["Digo qué: regar con agua que sobra.", "Falta quién, dónde y cuándo.", "Escribo los tres datos."], "Quién lo hace, en qué lugar y en qué momento."),
        W("Revisar la seguridad", "¿Es segura la propuesta de regar con agua sobrante de los vasos del recreo? Revisa si usa algo filoso o químico.", ["No usa nada filoso.", "No usa químicos.", "Solo agua limpia de los vasos."], "Sí, es segura."),
    ],
    mistakes=[
        M("Proponer una acción sin decir quién la hará.", "Nadie se hace cargo y no se cumple.", "Escribe un responsable."),
        M("Decir que tu acción es una costumbre de un pueblo.", "No tienes una fuente.", "Di que es tu propuesta."),
    ],
    R=[
        ex("Regar las plantas con agua que sobra, ¿cuida el agua o la gasta?", "La cuida", "Aprovecha lo que sobra."),
        ex("¿Es segura una acción que usa tijeras filosas con niños pequeños? Responde Sí o No.", "No", "Hay riesgo de cortes."),
        ex("¿Una acción situada dice quién, dónde y cuándo, o solo una idea general?", "Quién, dónde y cuándo", "Así se puede cumplir."),
    ],
    C=[
        ex("¿Qué es una propuesta? A) una idea que se ofrece para que otros la consideren B) una orden", "A", "Se ofrece a otros."),
        ex("Verdadero o falso: antes de actuar conviene preguntar a una persona adulta.", "Verdadero", "Ayuda a mantener la seguridad."),
        ex("Verdadero o falso: puedo decir que mi acción es una costumbre de un pueblo.", "Falso", "No tengo una fuente."),
    ],
    A=[
        ex("Completa la propuesta: «Regar las plantas del patio con agua que sobra. Quién: el curso. Dónde: el patio. Cuándo: ___ ». Elige. A) cada recreo B) nunca", "A", "Dice cuándo se hará."),
        ex("Una propuesta dice: «Dejar agua limpia para los pájaros. Dónde: el patio. Cuándo: cada mañana.» ¿Qué dato falta para que sea situada?", "Quién", "Faltan las personas que se harán cargo."),
        ex("Clasifica en SEGURA o NO SEGURA: a) regar con agua limpia b) usar cuchillos para limpiar plantas c) dejar agua para los pájaros.", "a segura, b no segura, c segura", "Los cuchillos son peligrosos."),
    ],
    Z=[
        ex("Pedro propone limpiar el patio quemando basura. ¿Qué error tiene la propuesta?", "No es segura", "El fuego es peligroso."),
        ex("Lía propone limpiar la playa de una comunidad sin avisar. ¿Qué debe hacer antes? A) preguntar a la comunidad B) hacerlo igual", "A", "Los lugares tienen personas que los cuidan."),
    ],
    D=[
        ex("Dos propuestas: 1) cuidar el agua en la escuela con un recipiente para las plantas; 2) cambiar el lugar de un sitio de respeto de la comunidad. ¿Cuál es adecuada para tu curso?", "La 1", "La 2 no le corresponde al curso."),
        ex("Una propuesta no dice quién la hará. ¿Está completa? Responde Sí o No.", "No", "Falta el responsable."),
    ],
    context=[ex("Tu curso quiere cuidar el agua en la escuela. ¿Qué propuesta es adecuada? A) poner un letrero para cerrar bien las llaves B) abrir las llaves al máximo", "A", "Ayuda a no desperdiciar agua.")],
    selfcheck=[
        ex("Escribe las cuatro partes de una acción situada.", "Qué, quién, dónde y cuándo", "Así se puede cumplir."),
        ex("Verdadero o falso: una acción segura usa cosas filosas.", "Falso", "Debe ser segura."),
        ex("¿Qué haces antes de actuar? A) preguntar a un adulto B) actuar sin avisar", "A", "Se cuida la seguridad."),
    ],
    task=T("Elige UNA de estas propuestas y completa los cuatro datos (qué, quién, dónde, cuándo): A) regar las plantas del patio con agua que sobra de los vasos; B) pegar un letrero para cerrar bien las llaves; C) dejar un recipiente con agua limpia para los pájaros en un lugar sombreado. Escribe cómo cuidas la seguridad. Agrega una pregunta para el educador tradicional sobre cómo cuida el entorno la comunidad de tu zona. Pide ayuda a una persona adulta.",
           "Elijo A. Qué: regar con agua que sobra. Quién: mi curso por turnos. Dónde: el patio. Cuándo: después del recreo. Seguridad: solo agua limpia. Pregunta: ¿cómo cuida el entorno nuestra comunidad?",
           ["completa los cuatro datos", "cuida la seguridad", "formula una pregunta"], ["cuatro datos", "frase de seguridad", "pregunta"], ["omitir el responsable", "proponer algo peligroso"],
           "Preguntar quién hará cada tarea; valorar que cuide la seguridad."),
    reinforce="Escribe tres formas de ahorrar agua en tu casa.",
    extend="Diseña un cartel breve para tu sala que invite a cuidar un recurso del entorno.",
)

# ============================================================ OA 13 · Técnicas productivas ancestrales y vida comunitaria
L(
    OA13, 1,
    materials="Lápiz y hojas. La ficha está escrita aquí. La comunidad, la técnica y las personas son inventadas.",
    use="Aprenderé a identificar el propósito, la fuente y el permiso de una técnica productiva. Sirve para practicar solo lo que se puede practicar con respeto.",
    prior=["Sé que una técnica tiene portadores y origen.", "Sé qué es pedir consentimiento."],
    explain=[
        "Una técnica productiva es una manera de hacer algo que entrega alimentos o materiales a la comunidad, como sembrar, cosechar o hilar. Se transmite de generación en generación y se practica hoy.",
        "Para cada técnica hay tres preguntas: ¿para qué sirve? ¿quién la enseña? ¿se me autoriza practicarla? El propósito es la razón. La fuente es la persona que enseña. El permiso es la autorización. Sin esas tres respuestas, no se practica.",
        "En esta clase usamos una ficha inventada de Valle Alto y una práctica escolar neutra. La técnica ancestral verdadera la enseñan los portadores y el educador tradicional. No la inventamos ni la copiamos.",
    ],
    vocab=[("técnica productiva", "manera de hacer algo que entrega alimentos o materiales"), ("propósito", "razón por la que se hace algo"), ("fuente", "persona que enseña o cuenta el saber"), ("autorización", "permiso para hacer algo"), ("transmitir", "pasar un saber de una persona a otra")],
    worked=[
        W("Leer la ficha", "Ficha inventada: «Técnica: cultivo de papas en la huerta de Valle Alto. Sirve para alimentar a las familias. La enseña don Pedro. Permiso: sí, a las visitas del curso.» ¿Cuál es el propósito y quién enseña?", ["Propósito: alimentar a las familias.", "Fuente: don Pedro.", "Hay permiso."], "Propósito: alimentar a las familias. Enseña don Pedro."),
        W("Sin permiso", "Otra ficha inventada dice: «Técnica: preparación de un alimento. La enseña doña Rosa. Permiso: no». ¿Se puede practicar?", ["Busco el permiso.", "Dice que no.", "Entonces no se practica."], "No se puede practicar."),
    ],
    mistakes=[
        M("Practicar una técnica que no te enseñó un portador.", "Puedes hacerlo mal o faltar al respeto.", "Pide que te enseñe quien la conoce."),
        M("Creer que si algo es útil, ya se puede usar.", "El permiso es necesario.", "Pregunta antes de practicar."),
    ],
    R=[
        ex("En la ficha del cultivo de papas, ¿quién enseña?", "Don Pedro", "La ficha lo dice."),
        ex("¿Para qué sirve el cultivo? A) alimentar a las familias B) pasear", "A", "El propósito está en la ficha."),
        ex("Si la ficha dice «Permiso: no», ¿se practica la técnica? Responde Sí o No.", "No", "Sin permiso no se practica."),
    ],
    C=[
        ex("Verdadero o falso: puedo practicar una técnica sin preguntar si me autorizan.", "Falso", "El permiso es necesario."),
        ex("¿Qué es el propósito? A) la razón por la que se hace algo B) el material", "A", "Dice para qué sirve."),
        ex("Verdadero o falso: la fuente es la persona que enseña.", "Verdadero", "Es quien conoce el saber."),
    ],
    A=[
        ex("Une cada pregunta con su dato. 1) ¿Para qué sirve? 2) ¿Quién enseña? 3) ¿Hay permiso? a) don Pedro b) alimentar a las familias c) sí", "1-b, 2-a, 3-c", "Cada dato está en la ficha."),
        ex("Una ficha dice: «Técnica: tejer. La enseña doña Marta. Permiso: no». De las tres preguntas, ¿cuál respuesta impide practicarla?", "El permiso", "Sin permiso no se practica."),
        ex("Una ficha dice: «Sirve para hilar. La enseña doña Marta. Permiso: sí». ¿Se puede practicar? Responde Sí o No.", "Sí", "Tiene propósito, fuente y permiso."),
    ],
    Z=[
        ex("Tomás aprendió una técnica por un video y dice que ya sabe la técnica de su pueblo. ¿Qué error comete?", "No la aprendió de un portador", "El video no reemplaza a quien enseña."),
        ex("Ema dice: «Esa ficha inventada muestra cómo producen todos los pueblos». ¿Qué error comete?", "Generaliza", "La ficha es de una comunidad inventada."),
    ],
    D=[
        ex("Dos niñas: una pide permiso a don Pedro para visitar la huerta; otra entra sin avisar. ¿Cuál actúa bien?", "La primera", "Pidió permiso antes."),
        ex("Quieres aprender una técnica real de tu zona. ¿A quién consultas? A) al educador tradicional B) a nadie", "A", "El educador sabe quién puede enseñar."),
    ],
    context=[ex("Tu curso visitará la huerta de la ficha inventada. ¿Qué debe tener antes? A) el permiso de don Pedro B) solo ganas", "A", "El permiso es necesario.")],
    selfcheck=[
        ex("Escribe qué es el propósito de una técnica.", "La razón por la que se hace", "Es la definición."),
        ex("Verdadero o falso: puedo practicar sin permiso si es una técnica útil.", "Falso", "El permiso es necesario."),
        ex("¿Qué tres preguntas haces antes de practicar una técnica?", "Para qué sirve, quién enseña y si hay permiso", "Son las tres de la clase."),
    ],
    task=T("Lee la ficha inventada: «Técnica: cultivo de papas en la huerta de Valle Alto. Sirve para alimentar a las familias. La enseña don Pedro. Permiso: sí, para visitas del curso. Límite: no se entra a la huerta sin que él esté.» Haz una ficha con cinco líneas: técnica, propósito, fuente, permiso y límite. Escribe una frase de agradecimiento a don Pedro. Añade una pregunta para el educador tradicional sobre una técnica real de tu zona.",
           "Técnica: cultivo de papas. Propósito: alimentar a las familias. Fuente: don Pedro. Permiso: sí. Límite: no entrar sin que él esté. Gracias, don Pedro. Pregunta: ¿qué técnicas de producción practica nuestra comunidad hoy?",
           ["completa las cinco líneas", "incluye el límite", "agradece"], ["ficha de cinco líneas", "agradecimiento", "pregunta"], ["omitir el límite", "inventar una técnica real"],
           "Preguntar qué dice cada línea; valorar el límite y el agradecimiento."),
    reinforce="Subraya el propósito con un color y la fuente con otro.",
    extend="Escribe dos fichas breves con técnicas inventadas, cada una con propósito, fuente y permiso.",
)

L(
    OA13, 2,
    materials="Lápiz y hojas. El relato de don Pedro está escrito aquí y es inventado.",
    use="Aprenderé a observar las etapas de un proceso productivo y los conocimientos que se usan en cada una. Sirve para entender que producir requiere saber y paciencia.",
    prior=["Sé que una técnica tiene propósito, fuente y permiso.", "Sé qué es un ciclo."],
    explain=[
        "Un proceso productivo tiene etapas, que son pasos en un orden. Para producir papas en una huerta hay cuatro etapas: preparar la tierra, sembrar, regar y cuidar, y cosechar. Cada etapa necesita conocimientos distintos.",
        "Un conocimiento es lo que una persona sabe y le sirve para hacer bien un trabajo. Don Pedro, nuestro personaje inventado, sabe cuándo la tierra está lista, cuánta agua necesita la planta y cuándo se cosecha.",
        "Observar etapas nos ayuda a ver que la producción es un ciclo de cuidado, no solo un resultado. En esta clase usamos un relato inventado. Los procesos y conocimientos reales los cuenta la comunidad.",
    ],
    vocab=[("etapa", "paso de un proceso"), ("proceso", "serie de pasos para lograr algo"), ("conocimiento", "lo que una persona sabe y le sirve para hacer algo"), ("sembrar", "poner semillas en la tierra"), ("cosechar", "recoger lo que creció")],
    worked=[
        W("Ordenar etapas", "Relato inventado de don Pedro: «Primero preparo la tierra, luego siembro, después riego y cuido, y al final cosecho.» ¿Qué etapa viene después de sembrar?", ["Leo el orden.", "Después de sembrar viene regar y cuidar.", "Respondo."], "Regar y cuidar."),
        W("Un conocimiento por etapa", "Don Pedro dice: «Siembro cuando la tierra está suelta y húmeda». ¿Qué conocimiento usa?", ["Sabe cómo se ve la tierra lista.", "Eso es un conocimiento.", "Lo escribo."], "Sabe cuándo la tierra está lista para sembrar."),
    ],
    mistakes=[
        M("Creer que producir es solo cosechar.", "Antes hay otras etapas.", "Nombra todas las etapas."),
        M("Inventar conocimientos de un pueblo real.", "Puede ser falso o faltar al respeto.", "Usa solo lo que dice la fuente."),
    ],
    R=[
        ex("¿Cuál es la primera etapa en el relato de don Pedro: preparar la tierra o cosechar?", "Preparar la tierra", "Es el inicio."),
        ex("¿Qué se hace en la etapa «sembrar»? A) poner semillas en la tierra B) recoger papas", "A", "Eso es sembrar."),
        ex("¿Cuál es la última etapa: sembrar o cosechar?", "Cosechar", "Es el final."),
    ],
    C=[
        ex("Verdadero o falso: producir es solo cosechar.", "Falso", "Hay varias etapas antes."),
        ex("¿Qué es un conocimiento? A) lo que una persona sabe y le sirve para hacer algo B) un objeto", "A", "Es un saber."),
        ex("Verdadero o falso: una etapa es un paso de un proceso.", "Verdadero", "Es una parte del proceso."),
    ],
    A=[
        ex("Ordena las etapas: a) cosechar b) sembrar c) preparar la tierra d) regar y cuidar. Escribe las letras.", "c, b, d, a", "Tierra, siembra, riego y cosecha."),
        ex("En el relato de don Pedro, ¿qué etapa va justo antes de cosechar?", "Regar y cuidar", "El orden es: preparar, sembrar, regar y cuidar, cosechar."),
        ex("Une cada etapa con su conocimiento. 1) preparar la tierra 2) regar 3) cosechar a) saber cuándo está maduro b) saber si está suelta c) saber cuánta agua da", "1-b, 2-c, 3-a", "Cada etapa usa un saber distinto."),
    ],
    Z=[
        ex("Pedro dice: «Cosecho antes de sembrar». ¿Qué error hay en el orden?", "La siembra va antes de la cosecha", "No se cosecha lo que no se sembró."),
        ex("Ema dice que don Pedro explica cómo producen todos los pueblos. ¿Qué error comete?", "Generaliza", "Don Pedro es un personaje inventado."),
    ],
    D=[
        ex("Si falta riego, ¿qué etapa se afecta después? A) la cosecha B) la preparación de la tierra", "A", "Sin riego se produce menos."),
        ex("¿Por qué es importante observar cada etapa? A) porque cada una tiene su cuidado B) porque son iguales", "A", "Cada una necesita conocimientos distintos."),
    ],
    context=[ex("Una familia inventada siembra una huerta, pero no la riega. ¿Qué crees que pasará con la cosecha? A) será menor B) será mayor", "A", "Las plantas necesitan agua.")],
    selfcheck=[
        ex("Escribe las cuatro etapas del relato de don Pedro.", "Preparar la tierra, sembrar, regar y cuidar, y cosechar", "Son las etapas del relato."),
        ex("Verdadero o falso: cada etapa necesita el mismo conocimiento.", "Falso", "Cada una necesita conocimientos distintos."),
        ex("¿Qué es un proceso?", "Una serie de pasos para lograr algo", "Es la definición."),
    ],
    task=T("Con el relato inventado de don Pedro («preparo la tierra, siembro, riego y cuido, cosecho»), dibuja las cuatro etapas en cuadros ordenados. Debajo de cada una escribe un conocimiento que crees que hace falta, rotulándolo como suposición tuya. Añade una pregunta para el educador tradicional sobre cómo su comunidad sabe cuándo es el momento de cada etapa.",
           "Cuadros: preparar la tierra, sembrar, regar y cuidar, cosechar. Suposición: hay que saber si la tierra está suelta, cuánta agua dar y cuándo está maduro. Pregunta: ¿cómo sabe nuestra comunidad cuándo es el momento de cada etapa?",
           ["ordena las etapas", "rotula las suposiciones", "formula una pregunta"], ["cuatro cuadros", "suposiciones", "pregunta"], ["presentar suposiciones como hechos de un pueblo", "cambiar el orden"],
           "Preguntar por qué cada etapa va en su lugar; valorar que rotule las suposiciones."),
    reinforce="Ordena las etapas de preparar un vaso con agua y flores: llenar el vaso, poner las flores, ponerlo en un lugar firme. Pide ayuda de un adulto.",
    extend="Escribe una etapa del proceso en que la comunidad podría ayudarse entre sí y por qué.",
)

L(
    OA13, 3,
    materials="Un vaso de plástico, algodón o papel absorbente, 3 semillas de poroto o lenteja y agua. Una cuchara. Las semillas NO se comen. Lávate las manos al terminar. Pide ayuda a una persona adulta.",
    use="Aprenderé a practicar una versión escolar y autorizada de sembrar y cuidar semillas, observando los cambios cada día. Sirve para entender el cuidado que requiere producir alimentos.",
    prior=["Sé que producir tiene etapas.", "Sé que las plantas necesitan agua."],
    explain=[
        "Esta práctica no es una técnica ancestral de ningún pueblo. Es una versión escolar neutra para entender el cuidado de las semillas. La técnica ancestral real la enseñan los portadores y el educador tradicional.",
        "Pon un poco de algodón húmedo en un vaso y coloca tres semillas entre el algodón y la pared del vaso, para verlas. Cada día agrega dos cucharadas de agua y observa. Anota los cambios en una tabla: día, agua y lo que ves.",
        "Una semilla germina cuando empieza a crecer: primero sale una raicita y luego un tallo. No todas germinan igual ni al mismo tiempo. Observamos y anotamos sin apurar. Las semillas no se comen ni se llevan a la boca.",
    ],
    vocab=[("germinar", "empezar a crecer una semilla"), ("raicita", "primera raíz que sale de la semilla"), ("tallo", "parte de la planta que crece hacia arriba"), ("observar", "mirar con atención y anotar"), ("registro", "tabla donde se anotan los datos")],
    worked=[
        W("Calcular el agua", "Cada día agregas 2 cucharadas de agua al vaso. ¿Cuántas cucharadas habrás agregado en 4 días?", ["Son 2 cucharadas por día.", "Son 4 días.", "2 × 4 = 8."], "8 cucharadas."),
        W("Anotar lo observado", "Día 3: ves una raicita en una semilla. ¿Qué anotas en la tabla?", ["Anoto el día: 3.", "Anoto lo que ves: una raicita en una semilla.", "No invento lo que no veo."], "Día 3: una raicita en una semilla."),
    ],
    mistakes=[
        M("Echar mucha agua hasta inundar las semillas.", "Las semillas necesitan humedad, no estar cubiertas.", "Agrega solo dos cucharadas por día."),
        M("Anotar lo que debería pasar y no lo que ves.", "Un registro cuenta lo observado.", "Anota solo lo que ves."),
    ],
    R=[
        ex("¿Cuántas semillas pones en el vaso?", "3", "La práctica usa tres semillas."),
        ex("¿Se comen las semillas de la práctica: sí o no?", "No", "No se comen ni se llevan a la boca."),
        ex("¿Qué sale primero de una semilla que germina: la raicita o el tallo?", "La raicita", "La raicita sale primero."),
    ],
    C=[
        ex("¿Qué es germinar? A) empezar a crecer una semilla B) cosechar", "A", "Es el comienzo del crecimiento."),
        ex("Verdadero o falso: esta práctica es una técnica ancestral de un pueblo.", "Falso", "Es una versión escolar neutra."),
        ex("Verdadero o falso: un registro cuenta lo que realmente ves.", "Verdadero", "No se anotan suposiciones."),
    ],
    A=[
        arith("Cada día agregas 2 cucharadas de agua. ¿Cuántas cucharadas habrás agregado en 5 días?", "2*5", "Se repite 2 cucharadas cinco días."),
        ex("Tabla: Día 1: nada. Día 2: nada. Día 3: raicita. Día 4: raicita más larga. ¿En qué día se vio la primera raicita?", "El día 3", "La tabla lo indica."),
        ex("Clasifica en OBSERVADO o SUPUESTO: a) vi una raicita b) creo que mañana tendrá hojas.", "a observado, b supuesto", "Lo que ves es observado."),
    ],
    Z=[
        ex("Tomás echó agua hasta cubrir las semillas. ¿Qué problema puede haber?", "Las semillas necesitan humedad y no estar cubiertas", "Demasiada agua las daña."),
        ex("Ema anotó «hoy salió una hoja» sin verla. ¿Qué error comete?", "Anotó algo que no observó", "El registro cuenta lo visto."),
    ],
    D=[
        ex("Dos semillas germinaron en días distintos: una en el día 3 y otra en el día 5. ¿Está mal? Responde Sí o No.", "No", "Cada semilla germina a su ritmo."),
        ex("Al terminar la práctica, ¿qué haces? A) lavarme las manos B) comer las semillas", "A", "Las semillas no se comen."),
    ],
    context=[ex("Tu amiga dice que su vaso tiene dos semillas germinadas y una no. ¿Hizo algo mal? Responde Sí o No.", "No", "No todas germinan igual.")],
    selfcheck=[
        ex("Escribe qué es germinar.", "Empezar a crecer una semilla", "Es la definición."),
        ex("Verdadero o falso: las semillas de la práctica se comen.", "Falso", "No se comen."),
        ex("¿Qué anota un buen registro?", "Lo que realmente se ve", "No se anotan suposiciones."),
    ],
    task=T("Haz la práctica escolar con tu vaso: algodón húmedo, tres semillas, dos cucharadas de agua por día. Durante cinco días anota en una tabla: día, agua agregada y lo que ves. Si no tienes semillas, usa esta tabla de práctica para completar: Día 1: nada; Día 2: nada; Día 3: una raicita; Día 4: dos raicitas; Día 5: dos raicitas y un tallo. Escribe una conclusión y una pregunta para el educador tradicional sobre cómo su comunidad cuida las semillas. Lávate las manos al terminar.",
           "Día 1: nada. Día 2: nada. Día 3: una raicita. Día 4: dos raicitas. Día 5: dos raicitas y un tallo. Conclusión: las semillas germinan a su ritmo. Pregunta: ¿cómo cuida nuestra comunidad sus semillas?",
           ["registra lo observado día por día", "escribe una conclusión", "formula una pregunta"], ["tabla de cinco días", "conclusión", "pregunta"], ["anotar lo que no ve", "comer las semillas"],
           "Preguntar qué vio cada día; valorar que no anote suposiciones."),
    reinforce="Anota en la tabla la fecha de hoy y lo que observas en la planta.",
    extend="Compara dos semillas del vaso: ¿cuál germinó antes y cuántos días de diferencia hubo?",
)

L(
    OA13, 4,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a relacionar la producción con la vida de la familia y la comunidad. Sirve para ver cómo se ayudan, se reparten tareas y comparten lo producido.",
    prior=["Sé que producir tiene etapas.", "Sé qué es la reciprocidad."],
    explain=[
        "La producción no la hace una sola persona. En una familia y en una comunidad se reparten tareas: unas personas siembran, otras riegan, otras cosechan. Cuando todos ayudan, el trabajo es más liviano.",
        "Lo que se produce se comparte. Puede repartirse entre las familias, guardarse para el invierno o regalarse en una fiesta. Cada comunidad decide cómo comparte. Nosotros usamos aquí un caso inventado.",
        "La producción también se conecta con la vida natural: el agua, la tierra y las estaciones. Y con la vida comunitaria: las reuniones, las fiestas y la ayuda mutua. Cómo lo hace una comunidad real lo cuenta ella misma.",
    ],
    vocab=[("tarea", "trabajo que le corresponde a una persona"), ("repartir", "dar a cada uno una parte"), ("ayuda mutua", "ayuda que se dan unas personas a otras"), ("familia", "grupo de personas que viven y se cuidan"), ("comunidad", "grupo de personas que viven y trabajan juntas")],
    worked=[
        W("Repartir tareas", "Caso inventado: en la huerta de Valle Alto, 3 familias siembran, 2 familias riegan y 4 familias cosechan. ¿Cuántas familias trabajan en total si ninguna repite?", ["Sumo 3 + 2 + 4.", "3 + 2 = 5.", "5 + 4 = 9."], "9 familias."),
        W("Compartir lo producido", "Se cosecharon papas y cada una de las 4 familias recibe 3 sacos. ¿Cuántos sacos se repartieron?", ["Son 4 familias.", "Cada una recibe 3.", "4 × 3 = 12."], "12 sacos."),
    ],
    mistakes=[
        M("Pensar que producir es un trabajo de una sola persona.", "Muchas personas ayudan.", "Busca quién hace cada tarea."),
        M("Decir cómo reparte todos los pueblos.", "Cada comunidad decide cómo comparte.", "Di solo lo que cuenta la fuente."),
    ],
    R=[
        ex("En el caso inventado, ¿cuántas familias cosechan?", "4", "El caso lo dice."),
        ex("¿Qué hacen las 2 familias que riegan: dan agua a la huerta o venden papas?", "Dan agua a la huerta", "Regar es dar agua."),
        ex("¿Qué es la ayuda mutua? A) ayuda que se dan unas personas a otras B) trabajar solo", "A", "Eso es colaborar."),
    ],
    C=[
        ex("Verdadero o falso: lo que se produce siempre se reparte igual en todas las comunidades.", "Falso", "Cada comunidad decide."),
        ex("Verdadero o falso: producir se conecta con la vida natural y con la comunitaria.", "Verdadero", "Depende del agua, la tierra y la ayuda de las personas."),
        ex("Si todas las familias ayudan, ¿el trabajo es más liviano o más pesado?", "Más liviano", "Se reparten las tareas."),
    ],
    A=[
        arith("3 familias siembran, 2 riegan y 4 cosechan. ¿Cuántas familias trabajan en total sin repetirse?", "3+2+4", "Se suman las familias."),
        arith("Cada una de las 4 familias recibe 3 sacos de papas. ¿Cuántos sacos se repartieron?", "4*3", "Se repite 3 sacos en cuatro familias."),
        ex("Clasifica en TAREA o REPARTO: a) regar la huerta b) entregar sacos a cada familia c) sembrar semillas.", "a tarea, b reparto, c tarea", "Entregar sacos es repartir."),
    ],
    Z=[
        ex("Pedro dice: «En el caso inventado ninguna familia ayuda, pero todas reciben sacos». ¿Se cumple la ayuda mutua? Responde Sí o No.", "No", "La ayuda mutua es que unas personas ayudan a otras."),
        ex("Ema dice que el reparto del caso inventado es el de todos los pueblos. ¿Qué error comete?", "Generaliza", "Es un caso inventado."),
    ],
    D=[
        arith("En otra huerta inventada, 5 familias reciben 2 sacos cada una y 3 familias reciben 1 saco cada una. ¿Cuántos sacos se repartieron en total?", "5*2+3*1", "Se suman los dos repartos."),
        ex("¿Qué relación muestra la fiesta de agradecimiento después de la cosecha? A) con la vida comunitaria B) con la vida solitaria", "A", "Reúne a la comunidad."),
    ],
    context=[ex("En tu curso se cuida un huerto. Julia riega, Tomás cosecha y Ema siembra. ¿Cómo se llama lo que hacen? A) repartir tareas B) trabajar solos", "A", "Cada uno hace una parte.")],
    selfcheck=[
        ex("Escribe qué es la ayuda mutua.", "Ayuda que se dan unas personas a otras", "Es la definición."),
        ex("Verdadero o falso: producir es siempre un trabajo individual.", "Falso", "Se reparte entre muchos."),
        ex("Escribe una forma de compartir lo producido.", "Repartir entre las familias, guardar o regalar en una fiesta", "Son formas de compartir."),
    ],
    task=T("Con el caso inventado de Valle Alto (3 familias siembran, 2 riegan, 4 cosechan; cada una de las 4 familias recibe 3 sacos), haz un cuadro de tareas y calcula cuántas familias trabajan y cuántos sacos se reparten. Escribe una frase que explique cómo la producción se conecta con la vida comunitaria. Añade una pregunta para el educador tradicional sobre cómo se ayudan en las tareas de producción en tu comunidad.",
           "Trabajan 3 + 2 + 4 = 9 familias. Se reparten 4 × 3 = 12 sacos. La producción une a la comunidad porque todos ayudan y comparten. Pregunta: ¿cómo se ayudan las familias de nuestra comunidad en el trabajo?",
           ["calcula correctamente", "explica la conexión con la comunidad", "formula una pregunta"], ["cuadro", "cálculos", "frase", "pregunta"], ["errores de cálculo", "decir que así lo hacen todos los pueblos"],
           "Revisar las operaciones; preguntar por qué la ayuda mutua facilita el trabajo."),
    reinforce="Escribe tres tareas de tu casa que se reparten entre varias personas.",
    extend="Inventa un caso con otros números de familias y sacos, y calcula el total repartido.",
)

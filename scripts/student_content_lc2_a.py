"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 06 (espacios significativos y visión de mundo) y OA 07 (historia local: pasado y presente).

Criterio de autoría: los lugares, las fichas de comunidad y los testimonios de práctica son inventados
(no pertenecen a ningún pueblo real) y están en castellano. Solo se usan datos generales de cultura que
se pueden afirmar con certeza. Los lugares reales, su significado y su forma de cuidarlos los enseñan
el educador/a tradicional y la comunidad; ningún ejercicio exige saber una lengua indígena.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA6, OA7 = "LC02 OA 06", "LC02 OA 07"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


F_RN = "Ficha rapa nui: pueblo de una isla del océano Pacífico. Allí están los moai, grandes figuras de piedra, y el mar rodea toda la isla."
F_KAW = "Ficha kawésqar: pueblo cuyo territorio son los canales de la Patagonia occidental, con muchas islas, mar y lluvia."
F_AYM = "Ficha aymara: pueblo del altiplano del norte de Chile. Cría llamas y alpacas, y cultiva papas y quinua entre cerros altos."

# ============================================================ OA 06 · Espacios significativos
L(
    OA6, 1,
    materials="Lápiz, hojas y colores. Las fichas con los datos están escritas en este cuaderno. Los lugares de práctica son inventados.",
    use="Aprenderé a reconocer qué es un espacio significativo y a fijarme en quién cuenta su historia. Sirve para hablar de un lugar sin inventar ni adivinar.",
    prior=["Sé qué es un río, un cerro y una plaza.", "Sé que en Chile viven distintos pueblos originarios."],
    explain=[
        "Un espacio significativo es un lugar muy importante para un pueblo o una comunidad. Puede ser importante porque allí se junta la gente, porque da agua o alimento, o porque guarda recuerdos de los abuelos. Puede ser un río, un cerro, una playa, una plaza o un camino.",
        "Para saber por qué un lugar es importante hay que preguntar a quien lo conoce. Esa persona, o ese libro, es la fuente. Una ficha buena dice tres cosas: dónde queda el lugar, para qué sirve y quién lo contó. Si falta un dato, no se puede saber y no se adivina.",
        "Algunos espacios son muy delicados y la comunidad prefiere cuidarlos en silencio. No se publica dónde están ni se va a pasear allá sin permiso. Por eso aquí usamos lugares de práctica inventados. Los lugares reales los enseña el educador o la educadora tradicional.",
    ],
    vocab=[("espacio significativo", "lugar muy importante para una comunidad"), ("fuente", "persona o texto que cuenta el dato"), ("comunidad", "grupo de personas que viven y trabajan juntas"), ("resguardar", "cuidar algo y no mostrarlo a todos"), ("ubicación", "dónde queda un lugar")],
    worked=[
        W("Leer una ficha de práctica", "Ficha inventada, que no es de ningún pueblo real: «Lugar: la vertiente de Valle Alto. Allí la gente recoge agua y conversa. Lo cuenta doña Rosa, vecina de la comunidad.» ¿Quién es la fuente y por qué el lugar es importante?", ["Busco quién cuenta: doña Rosa.", "Busco para qué sirve: da agua y reúne a la gente.", "Junto las dos ideas en una frase."], "La fuente es doña Rosa; el lugar es importante porque da agua y reúne a la gente."),
        W("Lo que dice la fuente y lo que pienso yo", "Ficha inventada: «El cerro Pelado da leña y sombra. Lo cuenta don Luis.» Un niño agrega: «Seguro tiene un tesoro». ¿Qué dato viene de la fuente?", ["Leo lo que escribió la ficha: leña y sombra.", "El tesoro no está en la ficha.", "Separo lo que dice la fuente de lo que yo imagino."], "Viene de la fuente que da leña y sombra; el tesoro es idea del niño."),
    ],
    mistakes=[
        M("Decir que un lugar es sagrado porque se ve misterioso.", "Nadie que lo conozca lo dijo; es una adivinanza.", "Pregunta a la fuente y escribe solo lo que ella cuenta."),
        M("Publicar en internet dónde queda un lugar delicado.", "La comunidad puede querer resguardarlo.", "Pregunta antes si se puede compartir y quién lo autoriza."),
    ],
    R=[
        ex("Ficha: «En la plaza de Valle Alto se juntan las familias cada primavera». ¿Qué lugar de la ficha es importante para la comunidad?", "La plaza de Valle Alto", "Es el lugar donde se juntan las familias."),
        ex("Ficha: «Lo cuenta doña Rosa». ¿Quién es la fuente?", "Doña Rosa", "La fuente es quien cuenta el dato."),
        ex("Una vertiente da agua a la comunidad. ¿Puede ser un espacio significativo? Responde Sí o No.", "Sí", "Un lugar que da agua es muy importante para vivir."),
    ],
    C=[
        ex("Verdadero o falso: si la ficha no dice quién contó el dato, podemos adivinar la fuente.", "Falso", "Sin fuente no se adivina; se pregunta."),
        ex("Ficha: «El cerro Pelado da leña y sombra». ¿Cuál frase sale de la ficha? A) Da leña y sombra B) Tiene un tesoro escondido", "A", "La frase A está escrita en la ficha."),
        ex("¿Qué tres datos tiene una buena ficha? A) dónde queda, para qué sirve y quién lo contó B) color, precio y tamaño", "A", "Esos tres datos dicen dónde, para qué y quién."),
    ],
    A=[
        ex("Ficha de Playa Larga: 1) La cuenta la abuela Marta. 2) La comunidad recoge algas allí. 3) Queda al oeste del pueblo. Escribe qué número es FUENTE, cuál USO y cuál UBICACIÓN.", "Fuente: 1; uso: 2; ubicación: 3", "La abuela cuenta, recoger algas es el uso y al oeste es dónde queda."),
        ex("Según la ficha rapa nui de este cuaderno, ¿qué rodea toda la isla? (" + F_RN + ")", "El mar", "La ficha dice que el mar rodea toda la isla."),
        ex("Ficha 1 dice: «Lo cuenta don Luis». Ficha 2 dice: «Lo escuché por ahí». ¿Cuál tiene una fuente clara?", "La ficha 1", "Solo la ficha 1 dice quién cuenta."),
    ],
    Z=[
        ex("Mateo dice: «Ese cerro de un video debe ser sagrado porque se ve misterioso». ¿Qué error comete?", "Adivina sin tener una fuente", "Para decir que es sagrado alguien que lo conoce debe contarlo."),
        ex("Una familia quiere subir a internet el mapa exacto de un lugar delicado antes de preguntar. ¿Debe hacerlo? Responde Sí o No.", "No", "La comunidad decide si se puede compartir un lugar delicado."),
    ],
    D=[
        ex("Ficha A (doña Rosa): «La vertiente da agua». Ficha B (don Luis): «En verano la gente se junta allí a conversar». ¿Se contradicen? Responde Sí o No y explica.", "No; cuentan usos distintos", "Una dice para qué da agua y la otra para qué se junta la gente."),
        ex("Una ficha dice solo: «Lugar: una playa». No dice pueblo ni fuente. ¿Podemos afirmar de qué pueblo es? Responde Sí o No.", "No", "Faltan el pueblo y la fuente."),
    ],
    context=[ex("Julia lee: «" + F_KAW + "» y dice que ese pueblo cría llamas en el altiplano. ¿Tiene razón?", "No", "La ficha habla de canales, islas y mar; las llamas están en la ficha aymara.")],
    selfcheck=[ex("Escribe con tus palabras qué es un espacio significativo.", "Un lugar muy importante para una comunidad", "Es la idea central de la explicación."), ex("Si la ficha no dice quién cuenta, ¿qué haces?", "Pregunto y no adivino", "Sin fuente no se puede afirmar."), ex("Verdadero o falso: todos los lugares delicados se pueden publicar.", "Falso", "Primero se pregunta a la comunidad.")],
    task=T("Lee esta ficha inventada: «Lugar: la vertiente de Valle Alto. Allí la gente recoge agua y conversa. Queda al pie de un cerro. Lo cuenta doña Rosa.» Haz una tabla con cuatro filas: lugar, fuente, para qué sirve y ubicación. Escribe al final UNA pregunta que le harías al educador tradicional sobre un lugar de tu zona. No dibujes ni nombres lugares sagrados reales.",
           "Lugar: la vertiente. Fuente: doña Rosa. Sirve: para recoger agua y conversar. Ubicación: al pie de un cerro. Pregunta: ¿qué lugar de nuestra zona cuida la comunidad?",
           ["escribe las cuatro filas con datos de la ficha", "no inventa datos", "formula una pregunta respetuosa"], ["tabla de cuatro filas", "pregunta escrita"], ["agregar datos que no están en la ficha", "nombrar un lugar delicado real"],
           "Pedir que muestre en la ficha de dónde sacó cada fila; si agregó algo, conversar de dónde lo supo."),
    reinforce="Subraya en la ficha de la vertiente la fuente con un color y el uso del lugar con otro.",
    extend="Compara la ficha rapa nui y la kawésqar: escribe un dato distinto de cada una.",
)

L(
    OA6, 2,
    materials="Lápiz y hojas. Las fichas están escritas en el cuaderno. Los espacios de práctica son inventados.",
    use="Aprenderé por qué un lugar puede ser importante: agua, alimento, encuentro o memoria. Sirve para entender un lugar mirando también a las personas y lo que hacen allí.",
    prior=["Sé que un espacio significativo es un lugar importante.", "Sé que una ficha tiene una fuente."],
    explain=[
        "Un lugar no es importante por sí solo. Es importante por la relación que las personas tienen con él. Hay lugares importantes porque dan agua, otros porque dan alimento, otros porque allí se encuentra la gente, y otros porque guardan la memoria de los abuelos.",
        "Para entender un lugar no basta mirarlo en una foto. Hay que saber qué hace la gente allí, en qué época del año y quién lo cuida. Por ejemplo, un río puede ser importante porque da agua y pescado, y también porque allí se cuentan historias.",
        "Cada pueblo mira el mundo a su manera, y eso se llama visión de mundo. En la ficha rapa nui, el mar rodea la isla. En la ficha aymara, los cerros altos rodean el pueblo. Cada pueblo se relaciona con su paisaje de forma distinta, y no se deben mezclar.",
    ],
    vocab=[("relación", "forma en que las personas se vinculan con un lugar"), ("visión de mundo", "manera en que un pueblo entiende y mira el mundo"), ("alimento", "lo que comemos para vivir"), ("encuentro", "momento en que la gente se junta"), ("memoria", "lo que un pueblo recuerda y cuenta")],
    worked=[
        W("Buscar la razón", "Ficha inventada: «La playa de Bahía Clara: la comunidad recoge algas y mariscos. Cada año los abuelos cuentan allí historias a los niños.» ¿Por qué es importante la playa?", ["Busco el alimento: algas y mariscos.", "Busco la memoria: los abuelos cuentan historias.", "Escribo las dos razones."], "Es importante porque da alimento y guarda la memoria."),
        W("Dos pueblos, dos paisajes", "Compara dos fichas: «" + F_RN + "» y «" + F_AYM + "». ¿Qué rodea a cada pueblo?", ["En la rapa nui leo que el mar rodea la isla.", "En la aymara leo que hay cerros altos.", "Anoto las diferencias sin mezclarlas."], "Rapa nui: el mar. Aymara: cerros altos."),
    ],
    mistakes=[
        M("Pensar que un lugar solo es importante si es muy grande.", "La importancia viene de lo que las personas hacen y recuerdan allí.", "Pregunta qué hace la gente en ese lugar."),
        M("Mezclar los datos de dos pueblos en una sola ficha.", "Cada pueblo tiene su paisaje y su manera de mirarlo.", "Lee cada ficha por separado."),
    ],
    R=[
        ex("Una vertiente da agua. ¿Es importante por agua, por alimento o por una fiesta?", "Por agua", "Una vertiente es una salida natural de agua."),
        ex("Los abuelos cuentan historias en una plaza. ¿Qué guarda esa plaza: memoria o dinero?", "Memoria", "Los relatos de los abuelos son parte de lo que la comunidad recuerda."),
        ex("Una playa da algas y mariscos. ¿Qué da la playa: alimento o ropa?", "Alimento", "Las algas y los mariscos se comen."),
    ],
    C=[
        ex("Verdadero o falso: un lugar es importante solo por lo grande que es.", "Falso", "Es importante por la relación que las personas tienen con él."),
        ex("¿Qué es la «visión de mundo»? A) La manera en que un pueblo entiende el mundo B) Un mapa del mundo", "A", "Es su forma de mirar y entender lo que lo rodea."),
        ex("Un río da agua y también se cuentan historias allí. ¿Cuántas razones de importancia hay?", "2", "Hay agua e historias."),
    ],
    A=[
        ex("Une cada lugar de práctica con su razón. 1) pozo de agua 2) huerta de papas 3) plaza de reunión. a) alimento b) encuentro c) agua", "1-c, 2-a, 3-b", "El pozo da agua, la huerta da alimento y la plaza reúne a la gente."),
        ex("Ficha: «En la quebrada de Piedra Blanca la comunidad juntaba leña. Hoy los niños la visitan con sus abuelos para conocerla». Escribe dos usos del lugar.", "Juntar leña y visitarla los niños con sus abuelos", "La ficha nombra esos dos usos."),
        ex("Según la ficha kawésqar de este cuaderno, ¿qué hay en el territorio de este pueblo? A) islas y mar B) cerros altos (" + F_KAW + ")", "A", "La ficha habla de canales, islas y mar."),
    ],
    Z=[
        ex("Pedro dice: «Ese cerro solo es una piedra grande». Ema dice: «Para la comunidad es un lugar donde se juntan». ¿Quién entiende mejor el lugar?", "Ema", "Mira lo que las personas hacen y recuerdan allí."),
        ex("Ana mezcla datos: dice que el pueblo rapa nui cultiva papas en cerros altos. ¿Qué error comete?", "Mezcla datos de dos pueblos", "Los cerros altos y las papas están en la ficha aymara."),
    ],
    D=[
        ex("Una laguna da agua en verano y en invierno es lugar de encuentro de las familias. ¿Cuántas funciones tiene en total en el año? Escribe el número.", "2", "Da agua y es lugar de encuentro."),
        ex("Dos fichas de práctica dicen: A) «El bosque da leña» y B) «En el bosque se cuentan historias». ¿El bosque es importante por una sola razón? Responde Sí o No.", "No", "Da leña y guarda historias; son dos razones."),
    ],
    context=[ex("El curso lee la ficha de Bahía Clara: la playa da algas y mariscos y los abuelos cuentan allí historias. Tomás dice que solo sirve para pasear. ¿Tiene razón?", "No", "La ficha dice que da alimento y guarda memoria.")],
    selfcheck=[ex("Nombra dos razones por las que un lugar puede ser importante.", "Agua, alimento, encuentro o memoria", "Son las razones vistas en la explicación."), ex("Escribe con tus palabras qué es una visión de mundo.", "La manera en que un pueblo mira el mundo", "Es su forma de entender lo que lo rodea."), ex("Verdadero o falso: se puede mezclar la ficha aymara con la rapa nui.", "Falso", "Cada pueblo tiene su ficha y no se mezclan.")],
    task=T("Lee la ficha inventada de Bahía Clara: «La comunidad recoge algas y mariscos en la playa. Cada año los abuelos cuentan allí historias a los niños.» Escribe en una hoja dos razones de importancia del lugar y dibuja la playa con una de ellas. Debajo, escribe una frase que explique cómo se relacionan las personas con la playa. No dibujes lugares sagrados reales.",
           "Razones: alimento (algas y mariscos) y memoria (los abuelos cuentan historias). Mi frase: la gente cuida la playa porque le da comida y recuerdos.",
           ["nombra dos razones tomadas de la ficha", "explica la relación entre personas y lugar", "no agrega datos inventados"], ["dos razones escritas", "dibujo", "frase de relación"], ["decir solo que la playa es bonita", "inventar un uso que no dice la ficha"],
           "Preguntar de qué parte de la ficha sacó cada razón; reconocer cuando la frase conecta personas y lugar."),
    reinforce="Elige tres lugares de las fichas de esta clase y escribe al lado por qué es importante cada uno.",
    extend="Escribe una frase que compare lo que rodea al pueblo rapa nui y lo que hay en el territorio kawésqar, según las fichas.",
)

L(
    OA6, 3,
    materials="Lápiz, hojas y colores. Los testimonios están escritos aquí y son inventados.",
    use="Aprenderé que los espacios significativos siguen vivos hoy y que hay personas que los conocen y los cuidan ahora. Sirve para no pensar que la cultura indígena es solo del pasado.",
    prior=["Sé qué es un espacio significativo.", "Sé que cada ficha dice quién cuenta."],
    explain=[
        "Los espacios significativos no son solo cosas del pasado. Las personas de hoy los usan, los cuidan y también los cambian. Un río que antes servía para tomar agua puede servir hoy además para hacer una fiesta de la comunidad.",
        "Las personas que conocen y cuidan estos lugares hoy se llaman portadores del conocimiento. Pueden ser abuelas, abuelos, educadores tradicionales o jóvenes. Ellos son personas actuales: viven hoy, tienen teléfono, van a la escuela y trabajan.",
        "Cuando hablamos de un pueblo originario, usamos el presente: «vive», «cuida», «celebra». Usar solo el pasado, como «vivían», puede hacer pensar que ya no existe. Los pueblos originarios existen hoy y siguen cuidando sus lugares.",
    ],
    vocab=[("portador del conocimiento", "persona que sabe, cuida y enseña algo de su cultura"), ("presente", "lo que pasa ahora"), ("pasado", "lo que pasó antes"), ("cambiar", "volverse distinto con el tiempo"), ("continuar", "seguir existiendo")],
    worked=[
        W("Pasado y presente en un testimonio", "Testimonio inventado de don Luis: «Cuando era niño íbamos al río con baldes. Hoy el río sigue siendo un lugar de encuentro, y mi nieta me ayuda a limpiarlo cada primavera.» ¿Qué cambió y qué sigue?", ["Antes se iba al río con baldes.", "Hoy sigue siendo lugar de encuentro y se limpia.", "Lo que sigue es el encuentro; lo que cambió es cómo se usa."], "Sigue siendo lugar de encuentro; hoy se limpia con ayuda de su nieta."),
        W("Usar el verbo correcto", "Quieres escribir sobre el pueblo kawésqar. ¿Dices «fue un pueblo de los canales» o «es un pueblo de los canales»? Usa la ficha: «" + F_KAW + "»", ["La ficha dice que su territorio son los canales.", "El pueblo existe hoy.", "Uso el presente: es."], "Es un pueblo de los canales"),
    ],
    mistakes=[
        M("Escribir «los pueblos originarios vivían» como si ya no existieran.", "Los pueblos originarios viven hoy.", "Usa el presente: «viven», «cuidan», «celebran»."),
        M("Pensar que si un lugar cambia ya no es importante.", "Un lugar puede cambiar y seguir siendo importante.", "Pregunta qué sigue igual y qué cambió."),
    ],
    R=[
        ex("Don Luis y su nieta limpian el río cada primavera. ¿Esto pasa en el pasado o en el presente?", "En el presente", "Lo hacen todos los años hasta hoy."),
        ex("¿Quién puede ser un portador del conocimiento: una abuela que cuida un lugar, o un objeto de museo?", "Una abuela", "El portador es una persona que sabe y enseña."),
        ex("«Cuando era niño…» ¿habla del pasado o del presente?", "Del pasado", "«Era niño» indica un tiempo que ya pasó."),
    ],
    C=[
        ex("Verdadero o falso: los pueblos originarios solo existieron antes.", "Falso", "Viven hoy y siguen cuidando sus lugares."),
        ex("Un lugar antes servía para juntar leña y hoy también sirve para una fiesta. ¿Qué pasó: se agregó un uso o se perdió el uso anterior?", "Se agregó un uso", "Hoy tiene un uso más y el anterior sigue en la historia del lugar."),
        ex("¿Qué verbo es mejor para hablar de un pueblo vivo? A) vivía B) vive", "B", "El presente muestra que el pueblo existe hoy."),
    ],
    A=[
        ex("Clasifica en PASADO o PRESENTE: a) «mi abuelo iba al río» b) «mi nieta limpia el río hoy» c) «hace mucho se juntaba leña».", "a pasado, b presente, c pasado", "Las palabras iba y hace mucho indican antes; hoy indica ahora."),
        ex("Reescribe en presente: «El pueblo aymara criaba llamas». Escribe la frase nueva.", "El pueblo aymara cría llamas", "La ficha aymara dice que cría llamas hoy."),
        ex("Testimonio inventado: «Mi tía enseña a los niños a cuidar la vertiente». ¿Quién es la portadora del conocimiento?", "La tía", "Ella enseña y cuida el lugar."),
    ],
    Z=[
        ex("Rosa dice: «Los pueblos originarios son cosa del pasado». ¿Qué le responderías con una prueba de la ficha aymara?", "Que hoy cría llamas y cultiva papas", "La ficha usa verbos en presente para el pueblo."),
        ex("Mateo dice: «Si un lugar cambia ya no sirve». Ema dice: «Puede cambiar y seguir siendo importante». ¿Quién tiene razón?", "Ema", "La comunidad puede mantener el valor del lugar aunque cambie."),
    ],
    D=[
        ex("Testimonio inventado: «Antes íbamos a pie, hoy vamos en bus, pero igual llegamos juntos al encuentro». ¿Qué sigue igual?", "Ir juntos al encuentro", "Cambió cómo van, pero siguen yendo juntos."),
        ex("Un niño dice que su vecina, educadora tradicional, es parte del pasado. ¿Es correcto? Responde Sí o No.", "No", "Ella vive hoy y enseña hoy."),
    ],
    context=[ex("En clase leen: «" + F_RN + "». Lía escribe «los rapa nui vivían en una isla». ¿Cómo mejorarías el verbo?", "Los rapa nui viven en una isla", "El pueblo existe hoy, por eso va en presente.")],
    selfcheck=[ex("¿Qué es un portador del conocimiento?", "Una persona que sabe, cuida y enseña", "Es la persona actual que guarda ese saber."), ex("¿Qué tiempo del verbo usas para hablar de un pueblo vivo?", "El presente", "Así se muestra que existe hoy."), ex("Verdadero o falso: un lugar puede cambiar y seguir siendo importante.", "Verdadero", "La comunidad puede mantener su valor.")],
    task=T("Lee este testimonio inventado: «Cuando era niña íbamos al cerro con mi abuela. Hoy llevo allí a mi hijo y le cuento lo que ella me contó. Ahora también sacamos fotos con el teléfono, pero siempre pedimos permiso.» Escribe en dos columnas: «Lo que sigue igual» y «Lo que cambió». Escribe una frase en presente sobre quién cuida el lugar hoy.",
           "Sigue igual: ir al cerro con la familia y contar lo que contó la abuela. Cambió: ahora se sacan fotos con teléfono. Hoy la mamá cuida el lugar y le cuenta a su hijo.",
           ["separa lo que sigue de lo que cambió", "usa verbos en presente", "reconoce a una persona actual"], ["dos columnas", "frase en presente"], ["escribir todo en pasado", "decir que la cultura ya no existe"],
           "Valorar el uso del presente; si usó solo pasado, preguntar quién vive hoy y qué hace."),
    reinforce="Cambia al presente tres frases que digan «vivían» o «criaban» sobre un pueblo de las fichas.",
    extend="Escribe una pregunta para una persona mayor: ¿qué ha cambiado en un lugar importante de tu zona y qué sigue igual?",
)

L(
    OA6, 4,
    materials="Lápiz y hojas. Las acciones y los casos están escritos aquí.",
    use="Aprenderé a cuidar un espacio significativo con acciones respetuosas. Sirve para devolver algo a un lugar que nos da agua, alimento o memoria.",
    prior=["Sé que un espacio significativo es importante.", "Sé que hay personas que lo cuidan hoy."],
    explain=[
        "Cuidar un lugar importante es una forma de agradecer lo que nos da. A eso se le llama reciprocidad: recibir algo y devolver algo. Si un río nos da agua, devolvemos cuidándolo limpio. Si una plaza nos reúne, la mantenemos ordenada.",
        "Hay acciones respetuosas muy simples. No botar basura, no sacar piedras ni plantas, no subir con ruido y no ir a un lugar delicado sin permiso. Antes de visitar un lugar, hay que preguntar si se puede entrar y cómo comportarse.",
        "También cuidamos con la palabra. No contamos cosas delicadas de un lugar a otros sin permiso y no decimos que sabemos cosas que no sabemos. Si algo no está claro, lo mejor es decir «no lo sé» y preguntar a la comunidad o al educador tradicional.",
    ],
    vocab=[("reciprocidad", "dar algo a cambio de lo que se recibe"), ("respeto", "tratar con cuidado a las personas y a los lugares"), ("permiso", "aprobación de quien puede darla"), ("cuidar", "mantener algo en buen estado"), ("agradecer", "mostrar que valoras lo que recibiste")],
    worked=[
        W("Elegir la acción respetuosa", "Un grupo visita una vertiente de práctica. ¿Qué hacen? a) botan basura b) se llevan piedras c) piden permiso y llevan una bolsa para su basura.", ["Pienso qué acción cuida el lugar.", "Botar basura y llevarse piedras dañan el lugar.", "Pedir permiso y llevar la basura de vuelta cuida."], "c"),
        W("Devolver lo recibido", "El río de práctica da agua a la comunidad. ¿Qué acción de reciprocidad es adecuada: dejar la basura en la orilla o limpiar la orilla juntos?", ["Reciprocidad es devolver.", "Limpiar la orilla cuida lo que nos da agua.", "Dejar basura daña al río."], "Limpiar la orilla juntos"),
    ],
    mistakes=[
        M("Llevarse una piedra como recuerdo de un lugar importante.", "Los elementos del lugar pertenecen al lugar y a la comunidad.", "Deja todo donde está y haz un dibujo."),
        M("Decir «yo sé cómo se hace» sin haber preguntado a la comunidad.", "Puedes equivocarte y faltar al respeto.", "Di «no lo sé» y pregunta al educador tradicional."),
    ],
    R=[
        ex("Antes de visitar un lugar delicado, ¿qué haces primero? A) Pedir permiso B) Sacar fotos", "A", "Primero se pregunta si se puede ir."),
        ex("Si ves basura en la orilla de un río, ¿qué acción cuida el lugar: recogerla o dejarla?", "Recogerla", "Así devuelves cuidado al lugar."),
        ex("¿La reciprocidad es dar algo a cambio de lo que se recibe? Responde Sí o No.", "Sí", "Esa es la definición de reciprocidad."),
    ],
    C=[
        ex("Verdadero o falso: llevarse una piedra de un lugar importante es una forma de cuidarlo.", "Falso", "Las cosas del lugar se dejan donde están."),
        ex("Un niño no sabe algo de un lugar. ¿Qué es mejor? A) Inventar una respuesta B) Decir «no lo sé» y preguntar", "B", "Inventar puede dar un dato falso."),
        ex("Un pozo da agua a una comunidad. Una acción de reciprocidad es mantenerlo tapado y limpio. ¿Esa acción es cuidar o dañar?", "Cuidar", "Mantenerlo limpio devuelve cuidado."),
    ],
    A=[
        ex("Marca solo las acciones respetuosas: a) pedir permiso b) gritar en el lugar c) llevar de vuelta tu basura d) pintar una piedra.", "a y c", "Pedir permiso y llevar de vuelta la basura cuidan el lugar."),
        ex("Ordena de primero a último: 1) agradezco 2) pido permiso 3) cuido el lugar durante la visita. Escribe los números en orden.", "2, 3, 1", "Primero se pide permiso, luego se cuida y al final se agradece."),
        ex("Una escuela quiere mostrar en un cartel un lugar delicado de práctica. ¿Qué debe hacer antes? A) Pedir permiso a la comunidad B) Imprimir el cartel", "A", "La comunidad decide si se puede mostrar."),
    ],
    Z=[
        ex("Ema dice: «Si tomo una flor no pasa nada». ¿Qué le dirías sobre cuidar un lugar importante?", "Que las cosas del lugar se dejan donde están", "Si todos se llevan algo, el lugar se daña."),
        ex("Pedro dice que sabe cómo era un lugar sagrado sin haber preguntado a nadie. ¿Qué haría una persona respetuosa?", "Decir que no lo sabe y preguntar", "Evita inventar un dato y respeta a la comunidad."),
    ],
    D=[
        ex("Una comunidad de práctica cuida su vertiente así: la limpia cada primavera, avisa a los visitantes y comparte el agua con los vecinos. ¿Cuántas acciones de cuidado nombra el texto?", "3", "Son limpiar, avisar y compartir el agua."),
        ex("Un visitante quiere sacar fotos de una ceremonia de práctica sin preguntar. ¿Debe hacerlo? Responde Sí o No.", "No", "Primero se pide permiso; algunos momentos no se fotografían."),
    ],
    context=[ex("El curso visita una plaza de práctica donde la comunidad se reúne. Tomás propone dejar los papeles de la merienda en el suelo. ¿Cuál es mejor idea: A) llevarlos en una bolsa B) dejarlos bajo un árbol", "A", "Llevarlos de vuelta cuida la plaza.")],
    selfcheck=[ex("¿Qué significa reciprocidad? Respóndelo con tus palabras.", "Dar algo a cambio de lo que se recibe", "Es devolver cuidado al lugar."), ex("Escribe dos acciones respetuosas al visitar un lugar.", "Pedir permiso y llevar de vuelta la basura", "Cuidan el lugar."), ex("Si no sabes algo de un lugar, ¿qué dices?", "No lo sé", "Es honesto y evita inventar.")],
    task=T("Un grupo visitará una vertiente de práctica de Valle Alto, que da agua a la comunidad. Escribe una lista de cinco reglas de cuidado para el grupo, por ejemplo qué hacer con la basura, con las piedras y con el ruido. Luego dibuja un cartel con la regla más importante, sin dibujar lugares sagrados reales.",
           "1. Pedir permiso antes de ir. 2. Llevar la basura de vuelta. 3. No sacar piedras. 4. Hablar bajito. 5. Agradecer al terminar. Mi cartel: «Llevo mi basura de vuelta».",
           ["escribe cinco reglas claras", "incluye una acción de reciprocidad", "no promueve sacar cosas del lugar"], ["lista de cinco reglas", "cartel dibujado"], ["reglas que dañan el lugar", "repetir la misma regla con otras palabras"],
           "Reconocer la regla más clara y preguntar a qué acción de reciprocidad corresponde; revisar que no haya instrucciones peligrosas."),
    reinforce="Copia tres acciones respetuosas de la clase y dibuja una de ellas.",
    extend="Escribe una frase que explique por qué cuidar un río es devolver lo que el río da.",
)

# ============================================================ OA 07 · Historia local
L(
    OA7, 1,
    materials="Lápiz y hojas. Los testimonios y las fechas son inventados y están escritos aquí.",
    use="Aprenderé a contar la historia de un lugar con fuentes. Sirve para separar lo que pasó antes de lo que pasa ahora, y para saber quién lo cuenta.",
    prior=["Sé qué es pasado y qué es presente.", "Sé que una ficha tiene una fuente."],
    explain=[
        "La historia local cuenta lo que ha pasado en un lugar y en su comunidad. Lo que pasó antes es el pasado. Lo que pasa ahora es el presente. Para saber qué ocurrió se usan fuentes, que son las personas, las fotos o los objetos que nos dan datos.",
        "Un testimonio es lo que cuenta una persona que vivió algo o lo escuchó de otros. Es una fuente muy valiosa. Por ejemplo, un abuelo puede contar cómo era el camino cuando era niño. Siempre hay que decir quién lo contó y cuándo.",
        "Una línea de tiempo ordena los hechos de antes a después. Si algo pasó «hace 40 años» y otra cosa «hace 5 años», lo de hace 40 años ocurrió primero. Si un abuelo tiene 70 años y recuerda algo de cuando tenía 10, ese hecho ocurrió hace 60 años. Para historias de pueblos originarios, el educador tradicional y la comunidad conocen mejor los hechos importantes.",
    ],
    vocab=[("historia local", "lo que ha pasado en un lugar y en su comunidad"), ("testimonio", "relato de una persona que vivió algo"), ("línea de tiempo", "dibujo que ordena hechos de antes a después"), ("fuente", "persona, foto u objeto que da un dato"), ("hace", "palabra para contar cuánto tiempo pasó")],
    worked=[
        W("Calcular hace cuánto", "Testimonio inventado de don Pedro: «Tengo 70 años. Cuando tenía 10 años, el camino al pueblo era de tierra.» ¿Hace cuántos años pasó eso?", ["Resto la edad de ahora menos la edad de entonces.", "70 − 10 = 60.", "Escribo la respuesta con la palabra «hace»."], "Hace 60 años"),
        W("Ordenar en una línea de tiempo", "Hechos inventados de Valle Alto: A) La escuela se abrió hace 40 años. B) Llegó la luz hace 25 años. C) Se abrió una biblioteca hace 5 años. ¿Cuál fue primero y cuál último?", ["Miro los números: 40, 25 y 5.", "Si pasó hace más años, ocurrió más antes.", "Hace 40 años es lo primero; hace 5 años es lo último."], "Primero A y último C"),
    ],
    mistakes=[
        M("Contar un testimonio sin decir quién lo contó.", "Sin fuente nadie sabe si es verdad.", "Escribe «lo contó…» y el nombre de la persona."),
        M("Pensar que «hace 5 años» ocurrió antes que «hace 40 años».", "Mientras más años hace, más lejos en el pasado ocurrió.", "Pon primero el hecho con el número más grande después de «hace»."),
    ],
    R=[
        ex("Lo que pasó antes es el pasado y lo que pasa ahora es el presente. ¿«Hoy hay una biblioteca» es pasado o presente?", "Presente", "La palabra hoy indica ahora."),
        ex("Un abuelo cuenta cómo era el camino cuando era niño. ¿Eso es un testimonio? Responde Sí o No.", "Sí", "Es un relato de alguien que lo vivió."),
        ex("Una escuela se abrió hace 40 años y una biblioteca hace 5 años. ¿Qué se abrió primero?", "La escuela", "Hace 40 años es más lejano en el tiempo que hace 5 años."),
    ],
    C=[
        ex("Verdadero o falso: un testimonio debe decir quién lo contó.", "Verdadero", "Así sabemos de dónde viene el dato."),
        ex("¿Qué ordena una línea de tiempo? A) Hechos de antes a después B) Colores de menor a mayor", "A", "Esa es su función."),
        ex("¿Cuál es una fuente de historia local: la foto antigua de una plaza, o una lista de compras?", "La foto antigua de una plaza", "Una foto antigua muestra cómo era el lugar."),
    ],
    A=[
        arith("Doña Marta tiene 80 años y recuerda algo de cuando tenía 12. ¿Hace cuántos años pasó?", "80-12", "Se resta la edad de entonces a la de ahora.", " años"),
        ex("Ordena de primero a último: la escuela se abrió hace 40 años, la luz llegó hace 25 años y la biblioteca se abrió hace 5 años. Escribe las letras en orden: A escuela, B luz, C biblioteca.", "A, B, C", "Hace 40 años pasó primero, luego hace 25 y al final hace 5."),
        ex("Testimonio inventado: «La escuela se abrió hace 40 años». ¿Qué debe escribir también quien lo cuenta para que sea una buena fuente?", "Quién lo contó", "Una fuente se reconoce porque tiene nombre."),
    ],
    Z=[
        ex("Julia dice: «No necesito decir quién me contó la historia». Pedro dice: «Hay que decirlo». ¿Quién tiene razón y por qué?", "Pedro; la fuente da confianza", "Si no se dice la fuente no se sabe si el dato es cierto."),
        ex("Mateo ordena una línea de tiempo así: hace 5 años, hace 25 años, hace 40 años. ¿Está bien? Responde Sí o No.", "No", "Debe ir de antes a después: hace 40, hace 25 y hace 5 años."),
    ],
    D=[
        arith("Una escuela de práctica se abrió hace 40 años y una biblioteca hace 10 años. ¿Cuántos años pasaron entre las dos?", "40-10", "Se restan los años de «hace».", " años"),
        ex("Un abuelo y una vecina cuentan cosas distintas de la plaza: él dice que antes había árboles; ella, que antes había una feria. ¿Los dos testimonios pueden ser verdaderos? Responde Sí o No.", "Sí", "Cada persona recuerda cosas distintas del mismo lugar."),
    ],
    context=[ex("Testimonio inventado de don Pedro: «Tengo 70 años; cuando tenía 10, íbamos a la escuela a pie». Lía dice que eso fue hace 70 años. ¿Está bien?", "No, fue hace 60 años", "70 menos 10 es 60.")],
    selfcheck=[ex("¿Qué es un testimonio? Respóndelo con tus palabras.", "El relato de una persona que vivió algo", "Es una fuente de historia local."), ex("Una línea de tiempo se ordena de... a...", "De antes a después", "Así se ve cómo pasó el tiempo."), ex("¿Por qué hay que decir quién contó un dato?", "Para saber de dónde viene", "La fuente da confianza.")],
    task=T("Lee estos tres hechos inventados de Valle Alto: «La escuela se abrió hace 40 años», «Llegó la luz hace 30 años», «Se abrió una biblioteca hace 10 años». Dibuja una línea de tiempo con los tres hechos en orden y escribe debajo cuántos años pasaron entre la escuela y la biblioteca. Escribe también qué fuente podrías usar para saber más.",
           "Línea: hace 40 años escuela, hace 30 años luz, hace 10 años biblioteca. Pasaron 30 años entre la escuela y la biblioteca. Fuente: preguntar a un vecino mayor que viva allí.",
           ["ordena de antes a después", "calcula bien la diferencia", "nombra una fuente"], ["línea de tiempo dibujada", "número de años", "fuente escrita"], ["ordenar al revés", "calcular mal los años"],
           "Revisar el orden y la resta; preguntar qué persona o foto serviría como fuente."),
    reinforce="Escribe tres hechos de tu escuela en orden de antes a después.",
    extend="Escribe una pregunta para un adulto mayor sobre cómo era un lugar de tu barrio cuando era niño.",
)

L(
    OA7, 2,
    materials="Lápiz y hojas. La historia de Valle Alto es inventada y está escrita aquí.",
    use="Aprenderé que los hechos de la historia local tienen causas y consecuencias. Sirve para entender por qué un lugar cambia y para no mirar un hecho solo.",
    prior=["Sé ordenar hechos de antes a después.", "Sé que un testimonio tiene una fuente."],
    explain=[
        "Los hechos de la historia no ocurren solos. Algo pasa primero y eso hace que ocurra otra cosa. La primera es la causa y la segunda es la consecuencia. Por ejemplo, si llega un camino, después pueden llegar buses y más visitantes.",
        "Para entender un hecho de la historia local, hay que preguntar qué pasó antes y qué pasó después. También hay que preguntar a distintas personas. Un abuelo, una vecina y un niño pueden recordar partes distintas del mismo hecho.",
        "Ninguna persona cuenta toda la historia sola. Cuando una persona habla de su pueblo, cuenta lo que ella conoce. Por eso, hay que decir «según don Pedro» y no «todos piensan así». Los pueblos originarios son muchos y cada comunidad tiene su propia historia.",
    ],
    vocab=[("causa", "lo que hace que algo ocurra"), ("consecuencia", "lo que ocurre después por esa causa"), ("según", "palabra para decir quién lo cuenta"), ("distinto", "que no es igual"), ("contexto", "lo que rodea a un hecho y ayuda a entenderlo")],
    worked=[
        W("Causa y consecuencia", "Historia inventada de Valle Alto: «Primero la comunidad construyó un camino. Después empezaron a llegar buses. Por eso más familias pudieron ir a la feria.» ¿Cuál es la causa y cuál la consecuencia?", ["La primera cosa que pasa es construir el camino.", "Lo que pasa después es que llegan buses y más familias.", "Causa: el camino. Consecuencia: llegan buses y familias."], "Causa: se construyó el camino. Consecuencia: llegaron buses y más familias a la feria."),
        W("Decir quién lo cuenta", "Don Pedro dice: «La feria empezó cuando llegó el camino». ¿Cómo escribes esa idea sin decir que todos opinan lo mismo?", ["Pongo el nombre de la fuente.", "Escribo «según don Pedro».", "No digo «todos»."], "Según don Pedro, la feria empezó cuando llegó el camino."),
    ],
    mistakes=[
        M("Escribir «todos piensan que…» cuando habla una sola persona.", "Una sola voz no es la voz de todo un pueblo.", "Escribe «según» y el nombre de quien lo cuenta."),
        M("Mirar un hecho de la historia sin preguntar qué pasó antes.", "Sin la causa se entiende solo la mitad.", "Pregunta siempre qué pasó antes y qué pasó después."),
    ],
    R=[
        ex("Primero se hizo un camino y después llegaron buses. ¿Cuál es la causa: el camino o los buses?", "El camino", "Lo que ocurre primero y provoca lo otro es la causa."),
        ex("«Según doña Rosa» sirve para decir quién cuenta. ¿Es verdadero o falso?", "Verdadero", "Esa frase nombra a la fuente."),
        ex("Si dos vecinos cuentan partes distintas de un hecho, ¿cuentan lo mismo o cosas distintas?", "Cosas distintas", "Cada uno recuerda partes diferentes."),
    ],
    C=[
        ex("Verdadero o falso: una sola persona cuenta toda la historia de un pueblo.", "Falso", "Cada persona cuenta lo que conoce."),
        ex("Pasó esto: llegó una escuela. Después más niños aprendieron a leer. ¿Qué es lo que pasó después?", "La consecuencia", "Lo que sigue a la causa es la consecuencia."),
        ex("¿Cómo escribes una idea de la abuela Marta? A) «Todos dicen» B) «Según la abuela Marta»", "B", "Nombrar a la fuente evita hablar por todos."),
    ],
    A=[
        ex("Une causa y consecuencia. 1) Se abrió una escuela 2) Llegó la luz 3) Se construyó un puente. a) se puede estudiar de noche b) más niños aprendieron a leer c) se cruza el río sin mojarse", "1-b, 2-a, 3-c", "Cada consecuencia es lo que pasa por esa causa."),
        ex("Ficha: «Según don Luis, antes la feria era más pequeña». Escribe quién es la fuente.", "Don Luis", "La ficha nombra a don Luis."),
        ex("Historia inventada: «Los vecinos limpiaron el río. Después volvieron los peces». Escribe la causa.", "Los vecinos limpiaron el río", "Fue lo primero que pasó."),
    ],
    Z=[
        ex("Ema dice: «Todos en la comunidad piensan que la feria es lo más importante». Solo habló con su abuelo. ¿Qué error comete?", "Habla por todos con la voz de uno", "Debería decir «según mi abuelo»."),
        ex("Tomás ve que llegó el camino y no pregunta qué pasó antes. ¿Qué le falta?", "Saber la causa", "Sin preguntar por lo anterior no entiende por qué llegó."),
    ],
    D=[
        ex("Hechos inventados: 1) La comunidad hizo una huerta 2) Hubo comida para la feria 3) Más vecinos participaron. ¿Cuál es la primera causa de la cadena?", "La comunidad hizo una huerta", "Es lo que ocurrió primero."),
        ex("Dos testimonios sobre la misma plaza: A) «Antes había árboles» y B) «Antes había una feria». ¿Qué conviene hacer para entender mejor la plaza?", "Escuchar las dos fuentes", "Cada una cuenta una parte del lugar."),
    ],
    context=[ex("El curso lee: «Se abrió una biblioteca y luego los niños leyeron más». Julia dice que la biblioteca es la consecuencia. ¿Tiene razón?", "No, es la causa", "La biblioteca ocurrió primero y provocó la lectura.")],
    selfcheck=[ex("¿Qué es una causa? Explícalo con tus palabras.", "Lo que hace que algo ocurra", "Es lo primero que pasa."), ex("¿Qué escribes en vez de «todos piensan»?", "Según y el nombre de la persona", "Así no hablas por todos."), ex("Verdadero o falso: un hecho de historia local ocurre solo, sin causa.", "Falso", "Siempre pasó algo antes.")],
    task=T("Lee esta historia inventada: «La comunidad de Valle Alto construyó un camino. Después empezaron a llegar buses. Más familias pudieron ir a la feria. Según don Pedro, la feria creció mucho.» Haz un dibujo en tres pasos: causa, hecho siguiente y consecuencia final. Escribe quién cuenta el último hecho.",
           "Paso 1: camino. Paso 2: buses. Paso 3: más familias en la feria. Quien cuenta el último hecho: don Pedro.",
           ["ordena la cadena de hechos", "identifica una causa", "nombra la fuente"], ["tres dibujos o frases", "fuente escrita"], ["invertir causa y consecuencia", "olvidar nombrar la fuente"],
           "Pedir que explique con la palabra «porque» por qué un paso lleva al siguiente."),
    reinforce="Une tres causas con tres consecuencias que inventes de tu escuela.",
    extend="Escribe una pregunta para dos personas distintas sobre un mismo hecho de tu barrio.",
)

L(
    OA7, 3,
    materials="Lápiz y hojas. Los datos del feriado están escritos aquí.",
    use="Aprenderé que la historia de los pueblos originarios sigue hoy y que hay hechos recientes y celebraciones actuales. Sirve para reconocer que los pueblos viven y cambian.",
    prior=["Sé que hay causas y consecuencias.", "Sé que un testimonio tiene fuente."],
    explain=[
        "La historia de un pueblo no termina en el pasado. Sigue ocurriendo hoy. Hay personas de pueblos originarios que son estudiantes, doctoras, profesores, artesanas y choferes. También hay celebraciones que se mantienen todos los años.",
        "En Chile hay un feriado llamado Día Nacional de los Pueblos Indígenas. Se celebra cerca del 21 de junio, cuando empieza el invierno en nuestro país. Cada comunidad decide cómo lo celebra, y el educador o la educadora tradicional puede contar cómo se vive en su zona.",
        "Para estudiar el presente de un pueblo también usamos fuentes: la voz de un educador tradicional, un diario actual o un libro nuevo. Cuando un hecho cambia con el tiempo, no decimos que se perdió. Decimos que se transformó y que sigue vivo gracias a las personas.",
    ],
    vocab=[("feriado", "día en que no hay clases ni trabajo por una fecha importante"), ("celebración", "fiesta o encuentro para recordar algo importante"), ("transformarse", "cambiar de forma sin dejar de existir"), ("actual", "de este tiempo"), ("pueblos indígenas", "pueblos que vivían en un territorio antes de los Estados actuales")],
    worked=[
        W("Pasado, presente y continuidad", "Testimonio inventado: «Antes la comunidad se juntaba en la plaza con faroles. Hoy se junta con luces eléctricas, pero sigue reuniéndose cada año.» ¿Qué cambió y qué continuó?", ["Cambió la forma de iluminar.", "Continuó la reunión cada año.", "Escribo cada cosa en su columna."], "Cambió la luz; continuó la reunión anual."),
        W("Datos del feriado", "Ficha: «El Día Nacional de los Pueblos Indígenas se celebra cerca del 21 de junio». ¿Qué estación empieza en Chile por esas fechas?", ["Pienso en el calendario de Chile.", "Junio está en el hemisferio sur y empieza el frío.", "Empieza el invierno."], "El invierno"),
    ],
    mistakes=[
        M("Decir que una tradición «se perdió» porque ahora se hace distinto.", "Cambiar no es desaparecer.", "Pregunta qué se transformó y qué continúa."),
        M("Creer que las personas de pueblos originarios solo trabajan en oficios antiguos.", "Hoy son parte de todos los trabajos.", "Pregunta a qué se dedican hoy sin generalizar."),
    ],
    R=[
        ex("El Día Nacional de los Pueblos Indígenas es un feriado. ¿Se celebra cerca del 21 de junio o del 18 de septiembre?", "Cerca del 21 de junio", "Se celebra cerca del solsticio de invierno."),
        ex("Una comunidad se junta todos los años desde hace mucho. ¿Esa reunión continúa o se perdió?", "Continúa", "Se sigue haciendo cada año."),
        ex("Una estudiante pertenece a un pueblo originario. ¿Puede ser estudiante hoy? Responde Sí o No.", "Sí", "Las personas de pueblos originarios viven y estudian hoy."),
    ],
    C=[
        ex("Verdadero o falso: si una tradición cambia de forma, desapareció.", "Falso", "Puede transformarse y seguir viva."),
        ex("¿Por qué el 21 de junio es una fecha importante en el calendario de Chile? A) Empieza el invierno B) Empieza el verano", "A", "En el hemisferio sur junio es de invierno."),
        ex("¿Qué es una celebración? A) Una fiesta o encuentro para recordar algo importante B) Un trabajo de oficina", "A", "Es un encuentro para recordar o festejar."),
    ],
    A=[
        ex("Clasifica: a) «Mi tía es profesora hoy» b) «Mi abuelo contaba cuentos a la luz de faroles» c) «El feriado de junio es este año». Escribe cuáles son del presente.", "a y c", "Hoy y este año indican ahora."),
        ex("Una comunidad antes hacía su fiesta de día y ahora también la hace de noche. ¿Qué cambió y qué continúa?", "Cambió el horario; continúa la fiesta", "La fiesta sigue, solo agregó un horario."),
        ex("Ficha: «El feriado se celebra cerca del 21 de junio». Si hoy es 21 de mayo, ¿falta más o menos un mes para esa fecha? Escribe más o menos un mes, o más de un año.", "Más o menos un mes", "De mayo a junio hay un mes."),
    ],
    Z=[
        ex("Pedro dice: «Los pueblos originarios ya no existen». ¿Qué prueba puedes darle de esta clase?", "Hay un feriado nacional que los celebra hoy", "El feriado existe hoy y reúne a comunidades."),
        ex("Ema dice: «Si una fiesta hoy usa luz eléctrica, ya no es de la comunidad». ¿Está bien?", "No", "Cambiar la luz no cambia que la comunidad se reúna."),
    ],
    D=[
        ex("Dos fichas inventadas: A) «La fiesta de Valle Alto es todos los años» y B) «Hoy hay jóvenes que ayudan a organizarla». ¿Cuál prueba continuidad en el tiempo?", "La A", "Que se hace todos los años muestra que continúa."),
        ex("Un niño dice que en su escuela hay una educadora tradicional que enseña hoy. ¿Esto muestra pasado o presente de su pueblo?", "Presente", "Ella enseña ahora."),
    ],
    context=[ex("La escuela organiza un afiche del Día Nacional de los Pueblos Indígenas. Lía escribe: «Se celebra cerca del 21 de junio». ¿Está bien escrito?", "Sí", "Es el dato del feriado.")],
    selfcheck=[ex("¿Qué decimos cuando una tradición cambia de forma pero sigue viva?", "Que se transformó", "Cambió pero continúa."), ex("¿Cerca de qué fecha es el Día Nacional de los Pueblos Indígenas?", "Cerca del 21 de junio", "Es el dato de la ficha."), ex("Verdadero o falso: hoy hay personas de pueblos originarios en todos los oficios.", "Verdadero", "Participan en todas las áreas de la sociedad.")],
    task=T("Lee este testimonio inventado: «Mi comunidad se junta cada año. Antes caminábamos horas para llegar y hoy vamos en bus. Los niños traen su teléfono, pero siempre escuchamos primero a los mayores.» Haz dos listas: «lo que cambió» y «lo que continúa». Dibuja un afiche para el Día Nacional de los Pueblos Indígenas con la frase «cerca del 21 de junio» y sin símbolos ni dibujos sagrados.",
           "Cambió: ir en bus y usar teléfono. Continúa: juntarse cada año y escuchar a los mayores. Afiche: «Día Nacional de los Pueblos Indígenas, cerca del 21 de junio».",
           ["separa cambio y continuidad", "usa la fecha correcta", "no copia símbolos sagrados"], ["dos listas", "afiche"], ["decir que todo se perdió", "copiar símbolos sagrados"],
           "Reconocer la distinción entre cambiar y desaparecer; revisar que el afiche no use símbolos restringidos."),
    reinforce="Escribe tres cosas que cambian y una que continúa en tu propia familia.",
    extend="Escribe una pregunta para el educador tradicional: ¿qué celebración de su pueblo se hace hoy en tu zona?",
)

L(
    OA7, 4,
    materials="Lápiz y hojas. Los casos y las pautas están escritos aquí.",
    use="Aprenderé a contar la historia de otras personas con respeto: pedir permiso, nombrar la fuente y devolver el trabajo. Sirve para no apropiarse de relatos que no son míos.",
    prior=["Sé decir quién cuenta un dato.", "Sé que cada comunidad tiene su historia."],
    explain=[
        "Cuando alguien comparte un recuerdo, nos hace un regalo. Para cuidarlo, hay cuatro pasos. Primero, pedir permiso. Segundo, escuchar sin interrumpir. Tercero, escribir lo que dijo sin cambiarlo. Cuarto, agradecer y mostrarle lo que escribiste.",
        "A eso también se le llama devolución: volver a la persona con lo que hicimos con su relato. Si la persona dice que algo no debe contarse, se respeta y no se escribe. Hay historias que son de una familia o de una comunidad y no se pueden usar sin autorización.",
        "No copiamos relatos de otros ni los presentamos como nuestros. Si usamos un relato, decimos de quién es. Tampoco inventamos que un relato es indígena cuando no lo es. Las historias reales las comparte el educador tradicional o la comunidad cuando corresponde.",
    ],
    vocab=[("permiso", "aprobación de la persona para usar su relato"), ("devolución", "volver a la persona con lo que hiciste con su relato"), ("autorización", "permiso formal para usar algo"), ("apropiarse", "usar algo ajeno como si fuera propio"), ("respetar", "cuidar los límites que pone la otra persona")],
    worked=[
        W("Ordenar los pasos", "Ordena para entrevistar a un abuelo: a) agradezco y le muestro mi trabajo b) pido permiso c) escucho sin interrumpir d) escribo lo que dijo sin cambiarlo.", ["Lo primero es pedir permiso.", "Después escucho y escribo.", "Al final agradezco y muestro lo que hice."], "b, c, d, a"),
        W("Un límite", "Un vecino cuenta una historia y dice: «Esta parte no se escribe». ¿Qué haces?", ["Respeto lo que dijo.", "No la escribo ni la cuento.", "Puedo preguntar qué parte sí puedo compartir."], "No la escribo y respeto su límite"),
    ],
    mistakes=[
        M("Copiar una historia de otra persona y firmarla como mía.", "La historia pertenece a quien la contó.", "Escribe «me la contó…» y el nombre."),
        M("Cambiar lo que dijo el abuelo para que quede más bonito.", "Cambias su voz y su memoria.", "Escribe lo que dijo y muéstraselo."),
    ],
    R=[
        ex("Antes de entrevistar a un abuelo, ¿qué haces primero: pedir permiso o escribir su historia?", "Pedir permiso", "Primero se pide autorización."),
        ex("Una persona dice «esta parte no se cuenta». ¿La escribes? Responde Sí o No.", "No", "Se respeta su límite."),
        ex("¿Quién es el dueño de una historia que te contó un vecino: él o tú?", "Él", "El relato es de quien lo cuenta."),
    ],
    C=[
        ex("Verdadero o falso: puedes cambiar lo que dijo el abuelo para que suene mejor.", "Falso", "Se escribe lo que dijo, sin cambiarlo."),
        ex("¿Qué es la devolución? A) Mostrar a la persona lo que hiciste con su relato B) Pedir otro permiso", "A", "Es volver con el resultado de tu trabajo."),
        ex("¿Qué escribes junto a un relato ajeno? A) «Me lo contó…» y el nombre B) Nada", "A", "Hay que nombrar a quien lo contó."),
    ],
    A=[
        ex("Ordena los cuatro pasos: a) agradezco y muestro mi trabajo b) pido permiso c) escucho sin interrumpir d) escribo lo que dijo. Escribe el orden correcto con letras.", "b, c, d, a", "Se pide permiso, se escucha, se escribe y se agradece."),
        ex("Un abuelo dice «puedes contar esto, pero no mi nombre». ¿Escribes su nombre? Responde Sí o No.", "No", "Respetas lo que autoriza."),
        ex("Mateo escribió una historia que le contó su vecina. ¿Qué debe agregar debajo? A) «Me la contó mi vecina» B) «La inventé yo»", "A", "Debe reconocer a quien la contó."),
    ],
    Z=[
        ex("Lía copia el cuento de su vecino y escribe «autora: Lía». ¿Qué error comete?", "Se apropia de un relato ajeno", "El cuento es de quien lo contó."),
        ex("Pedro dice: «Si alguien me cuenta algo, es mío». ¿Tiene razón?", "No", "Lo que alguien cuenta sigue siendo suyo."),
    ],
    D=[
        ex("Una niña graba la voz de su abuela sin pedirle permiso. ¿Qué falta?", "El permiso", "Hay que pedir autorización antes de grabar."),
        ex("Tomás quiere mostrar en el patio la historia de un vecino, pero él solo autorizó escribirla en el cuaderno. ¿Puede mostrarla? Responde Sí o No.", "No", "La autorización fue solo para el cuaderno."),
    ],
    context=[ex("El curso visita a doña Rosa y quiere preguntarle por su infancia. Ema propone grabar primero y preguntar después. ¿Está bien?", "No", "Primero se pide permiso, luego se graba.")],
    selfcheck=[ex("Escribe los cuatro pasos para compartir un relato con respeto.", "Pedir permiso, escuchar, escribir sin cambiar y agradecer", "Son los cuatro pasos de la explicación."), ex("¿Qué es apropiarse de un relato?", "Usarlo como si fuera mío", "Es no reconocer a quien lo contó."), ex("Si la persona dice «esto no se cuenta», ¿qué haces?", "Lo respeto", "Los límites del relato son de la persona.")],
    task=T("Imagina que entrevistas a don Pedro, un abuelo inventado de Valle Alto, sobre cómo era la plaza cuando era niño. Escribe tres preguntas con respeto, una nota de agradecimiento y la frase con la que pedirías permiso para escribir su relato. No uses datos reales de personas de tu zona.",
           "Preguntas: ¿Cómo era la plaza? ¿Quién la cuidaba? ¿Qué jugaban allí? Permiso: «¿Me permite escribir lo que usted me cuente?». Agradecimiento: «Gracias por contarme».",
           ["pide permiso antes de preguntar", "escribe tres preguntas respetuosas", "incluye agradecimiento"], ["tres preguntas", "frase de permiso", "nota de agradecimiento"], ["preguntas invasivas", "olvidar pedir permiso"],
           "Revisar que ninguna pregunta invada su privacidad y que haya devolución."),
    reinforce="Copia la frase de permiso y léela en voz alta a un adulto de tu casa.",
    extend="Escribe dos preguntas para un adulto sobre cómo cuidar una historia que alguien te cuenta.",
)

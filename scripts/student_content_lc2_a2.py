"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 08 (valoración cultural e identidad) y OA 09 (territorio, lengua e historia en la identidad).

Criterio de autoría: las fichas de pueblo reúnen solo datos generales y ampliamente conocidos; los casos
con personas (Sofía, Mateo, doña Rosa…) son inventados. La única expresión de lengua indígena que se
analiza es la composición mapuche «mapu» (tierra) + «che» (gente), ampliamente atestiguada. Ningún
ejercicio exige hablar una lengua indígena ni pertenecer a un pueblo; lo tradicional lo enseñan el
educador/a tradicional y la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA8, OA9 = "LC02 OA 08", "LC02 OA 09"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No pedir a nadie que represente a su pueblo."


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


G_AYM = "Pueblo aymara: vive en el altiplano del norte de Chile. Cría llamas y alpacas y cultiva papas y quinua. Su lengua es el aymara."
G_DIA = "Pueblo diaguita: vive en los valles del Norte Chico, cerca de los ríos Elqui, Limarí y Huasco. Hace cerámica con dibujos geométricos."
G_KAW = "Pueblo kawésqar: vive en los canales de la Patagonia occidental, con muchas islas, mar y lluvia. Su lengua es el kawésqar."
G_MAP = "Pueblo mapuche: vive en el centro y sur de Chile, entre bosques, ríos y volcanes. Su lengua es el mapuzugun (también se escribe mapudungun)."
G_RN = "Pueblo rapa nui: vive en la isla Rapa Nui, en el océano Pacífico. Allí están los moai, grandes figuras de piedra. Su lengua es el rapa nui."

# ============================================================ OA 08 · Valoración cultural e identidad
L(
    OA8, 1,
    materials="Lápiz, hojas y colores. Las fichas de los pueblos están escritas en el cuaderno.",
    use="Aprenderé qué es la cultura y qué es la identidad, y a reconocer aspectos de la cultura de un pueblo con una fuente. Sirve para valorar sin inventar ni generalizar.",
    prior=["Sé que en Chile viven distintos pueblos originarios.", "Sé que una ficha dice quién cuenta."],
    explain=[
        "La cultura de un pueblo es su manera de vivir. Incluye lo que come, cómo habla, qué música hace, cómo trabaja, cómo celebra y qué historias cuenta. Cada pueblo originario tiene su propia cultura, distinta de las demás.",
        "La identidad es cómo una persona o un pueblo se reconoce y se siente parte de algo. Mi identidad se forma con mi familia, mi lengua, mi lugar y lo que recuerdo. Una persona puede sentirse parte de más de un grupo a la vez.",
        "Para hablar de la cultura de un pueblo, usamos una fuente: su gente, un educador tradicional o una ficha que diga quién cuenta. No sirve mirar solo una foto ni suponer cómo es alguien por su apariencia. Cada persona decide qué quiere compartir de su cultura.",
    ],
    vocab=[("cultura", "manera de vivir de un pueblo: comida, lengua, música, trabajo y fiestas"), ("identidad", "cómo una persona o un pueblo se reconoce"), ("pertenencia", "sentirse parte de un grupo"), ("aspecto cultural", "una parte de la cultura, como la comida o la música"), ("fuente", "persona o texto que da el dato")],
    worked=[
        W("Aspectos de la cultura en una ficha", G_AYM + " Clasifica «papas y quinua» y «lengua aymara».", ["Papas y quinua se comen: es comida.", "La lengua aymara es el idioma: es lengua.", "Pongo cada dato en su aspecto."], "Papas y quinua: comida. Lengua aymara: lengua."),
        W("No suponer", "Julia ve una foto de una persona sin título. Piensa que es de un pueblo originario por su ropa. ¿Qué debe hacer?", ["No se puede saber por la apariencia.", "Debe preguntar o buscar una fuente.", "No debe afirmarlo sin fuente."], "Preguntar y no suponer"),
    ],
    mistakes=[
        M("Pensar que se reconoce a una persona de un pueblo por su apariencia.", "La identidad no se ve en una foto.", "Pregunta, si corresponde, y respeta lo que cada persona quiera contar."),
        M("Decir que todos los pueblos comen y viven igual.", "Cada pueblo tiene su propia cultura.", "Lee la ficha de cada pueblo por separado."),
    ],
    R=[
        ex("La cultura incluye lo que come un pueblo. ¿La quinua es un aspecto de comida o de ropa?", "De comida", "La quinua es un alimento."),
        ex("Un pueblo habla una lengua. ¿La lengua es un aspecto de la cultura? Responde Sí o No.", "Sí", "La lengua es parte de la manera de vivir."),
        ex("«Sentirse parte de un grupo» es la idea de pertenencia. ¿Es verdadero o falso?", "Verdadero", "Esa es la definición de pertenencia."),
    ],
    C=[
        ex("¿Qué es la identidad? A) Cómo una persona o pueblo se reconoce B) Un número de carnet", "A", "Es el modo de reconocerse y sentirse parte."),
        ex("Verdadero o falso: se puede saber el pueblo de una persona solo mirando su ropa.", "Falso", "La ropa no dice a qué pueblo pertenece una persona."),
        ex("Ficha: «Pueblo diaguita: hace cerámica con dibujos geométricos». ¿Qué aspecto cultural nombra: música o artesanía?", "Artesanía", "La cerámica es un trabajo hecho a mano."),
    ],
    A=[
        ex("Clasifica en COMIDA, LENGUA o TRABAJO: a) criar llamas b) mapuzugun c) papas. Escribe cada letra con su aspecto.", "a trabajo, b lengua, c comida", "Criar llamas es un trabajo, el mapuzugun es una lengua y las papas son comida."),
        ex("Según la ficha kawésqar de este cuaderno, ¿cuál es su lengua? (" + G_KAW + ")", "El kawésqar", "La ficha dice que su lengua es el kawésqar."),
        ex("Une pueblo y dato. 1) aymara 2) diaguita 3) rapa nui. a) moai b) llamas c) cerámica geométrica", "1-b, 2-c, 3-a", "Cada dato está en la ficha de su pueblo."),
    ],
    Z=[
        ex("Pedro dice: «Todas las personas de un pueblo son iguales». Ana dice: «Cada persona es distinta, aunque comparta una cultura». ¿Quién tiene razón?", "Ana", "Dentro de un pueblo hay personas diferentes."),
        ex("Un niño dice que sabe a qué pueblo pertenece su compañera porque tiene cierto apellido. ¿Es una buena razón? Responde Sí o No.", "No", "Un apellido no dice con certeza a qué pueblo se pertenece."),
    ],
    D=[
        ex("Ficha inventada: «En el pueblo de Valle Alto se hace pan los domingos y se cantan canciones antiguas». ¿Cuántos aspectos de la cultura nombra?", "2", "Nombra una comida y una música."),
        ex("Una persona comparte una canción de su familia y pide que no la grabes. ¿Qué haces?", "No la grabo", "Respetas lo que decide compartir."),
    ],
    context=[ex("En clase leen: «" + G_RN + "». Lía dice que ese pueblo cultiva papas en el altiplano. ¿Está bien?", "No", "Esa información corresponde a la ficha aymara.")],
    selfcheck=[ex("Escribe tres aspectos de la cultura de un pueblo.", "Comida, lengua, música, trabajo o fiestas", "Son aspectos vistos en la explicación."), ex("¿Por qué no hay que suponer el pueblo de una persona?", "Porque la apariencia no lo dice", "La identidad no se ve en la ropa."), ex("¿Quién decide qué compartir de su cultura?", "Cada persona", "Nadie debe obligar a compartir.")],
    task=T("Elige UNA ficha de este cuaderno (aymara, diaguita, kawésqar, mapuche o rapa nui). Haz una tabla con tres filas: dónde vive, lengua o arte, y un dato más de la ficha (trabajo, comida o paisaje). Escribe en cada fila un dato de la ficha. Al final escribe una pregunta para el educador tradicional. No dibujes símbolos sagrados ni lugares sagrados.",
           "Elegí la ficha aymara. Dónde vive: altiplano del norte de Chile. Lengua o arte: lengua aymara. Dato más: cría llamas y cultiva papas. Pregunta: ¿qué más puede enseñarnos sobre su pueblo?",
           ["usa datos de la ficha", "completa las tres filas", "formula una pregunta respetuosa"], ["tabla de tres filas", "pregunta escrita"], ["agregar datos inventados", "mezclar fichas"],
           "Verificar que cada dato esté en la ficha; si agregó algo, conversar de dónde lo supo."),
    reinforce="Subraya en la ficha diaguita los datos de lugar y de arte con dos colores.",
    extend="Compara dos fichas: escribe una diferencia de comida o trabajo entre dos pueblos.",
)

L(
    OA8, 2,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé cómo cada aspecto de la cultura ayuda a formar la identidad de las personas y los pueblos. Sirve para valorar la diversidad sin comparar ni burlarse.",
    prior=["Sé qué es la cultura.", "Sé que cada pueblo tiene la suya."],
    explain=[
        "Cada parte de la cultura ayuda a formar la identidad. Si una niña habla con su abuela en su lengua, siente que pertenece a su familia. Si un niño ayuda en el trabajo de su comunidad, siente que su comunidad lo necesita. Si todos cantan juntos, se sienten unidos.",
        "En Chile hay mucha diversidad cultural. Hay pueblos originarios distintos, y también familias que vienen de otros países. Todas las culturas valen lo mismo. No hay culturas mejores ni peores, solo diferentes. Valorar es reconocer que cada una tiene algo importante.",
        "Dentro de un mismo pueblo, las personas también son distintas. Una persona puede vivir en el campo y otra en la ciudad. Una puede hablar la lengua de su pueblo y otra estar aprendiéndola. Las dos pueden sentirse parte de su pueblo. No se debe juzgar a nadie por saber más o menos.",
    ],
    vocab=[("diversidad", "que hay muchas formas distintas de vivir"), ("valorar", "reconocer que algo es importante"), ("comunidad", "personas que viven y trabajan juntas"), ("juzgar", "decir que alguien es mejor o peor"), ("familia", "personas que se cuidan y viven juntas")],
    worked=[
        W("Qué aspecto forma identidad", "Sofía, personaje inventado, canta con su abuela canciones de su familia. ¿Qué aspecto cultural ayuda a su identidad y cómo la hace sentir?", ["El aspecto es la música.", "Cantar con la abuela la hace sentir parte de su familia.", "Escribo ambas ideas."], "La música; la hace sentir parte de su familia."),
        W("No juzgar", "Mateo, personaje inventado, está aprendiendo la lengua de su pueblo y dice pocas palabras. Pedro se ríe. ¿Qué debería hacer Pedro?", ["Reírse hace sentir mal a Mateo.", "Mateo sigue siendo parte de su pueblo.", "Pedro debería animarlo."], "Animarlo y no burlarse"),
    ],
    mistakes=[
        M("Decir que una cultura es mejor que otra.", "Todas las culturas valen lo mismo.", "Di qué tiene de importante cada una."),
        M("Burlarse de alguien que habla poco su lengua.", "Aprender lleva tiempo y todos pertenecen.", "Anímalo a seguir aprendiendo."),
    ],
    R=[
        ex("Si todos cantan juntos, se sienten unidos. ¿Cantar juntos ayuda a la identidad? Responde Sí o No.", "Sí", "Compartir una música hace sentir pertenencia."),
        ex("Valorar una cultura es reconocer que tiene algo importante. ¿Verdadero o falso?", "Verdadero", "Esa es la definición de valorar."),
        ex("Una niña habla con su abuela en su lengua. ¿Con quién se siente unida: con su abuela o con un desconocido?", "Con su abuela", "Habla con ella en su lengua."),
    ],
    C=[
        ex("Verdadero o falso: una cultura es mejor que otra.", "Falso", "Todas las culturas valen lo mismo."),
        ex("¿Qué es la diversidad cultural? A) Que existen muchas formas distintas de vivir B) Que todos vivan igual", "A", "Diversidad significa variedad."),
        ex("Una persona vive en la ciudad y otra en el campo, y las dos son de un mismo pueblo. ¿Las dos pueden sentirse parte de él? Responde Sí o No.", "Sí", "Se puede pertenecer viviendo en lugares distintos."),
    ],
    A=[
        ex("Une aspecto y forma de sentirse parte. 1) cantar juntos 2) ayudar en el trabajo 3) hablar con la abuela. a) soy necesario b) estoy unido c) me siento de mi familia", "1-b, 2-a, 3-c", "Cada acción da un sentimiento de pertenencia distinto."),
        ex("Marca solo lo que valora la cultura de otros: a) preguntar con respeto b) burlarse de su acento c) escuchar su canción d) decir que es rara.", "a y c", "Preguntar con respeto y escuchar son formas de valorar."),
        ex("Un curso tiene niñas y niños de familias distintas que cuentan lo que comen en sus casas. ¿Eso muestra diversidad? Responde Sí o No.", "Sí", "Hay comidas y costumbres distintas."),
    ],
    Z=[
        ex("Ema dice: «Si hablas poco tu lengua, no eres de tu pueblo». ¿Qué le responderías?", "Que aprender lleva tiempo y igual se pertenece", "La pertenencia no depende de cuánto se habla."),
        ex("Tomás dice que su comida es mejor que la de Lía. ¿Qué podría decir si quisiera valorar las dos?", "Que las dos comidas son importantes", "Valorar es reconocer lo que cada una aporta."),
    ],
    D=[
        ex("En un patio un grupo se ríe de la ropa de una compañera que viste distinto por su cultura. ¿Qué acción ayuda más? A) Reírse también B) Decir que cada ropa tiene su sentido", "B", "Explicar y respetar ayuda a valorar."),
        ex("Un niño dice «mi pueblo es el mejor». ¿Qué idea de esta clase falta en su frase?", "Que todas las culturas valen lo mismo", "No hay culturas mejores."),
    ],
    context=[ex("Una niña inventada, Sofía, canta con su abuela canciones familiares y Pedro dice que es raro. ¿Qué haces tú?", "Explico que cantar con la abuela es parte de su identidad", "Así valoras lo que ella comparte.")],
    selfcheck=[ex("¿Por qué ayudar en el trabajo de la comunidad ayuda a la identidad?", "Porque uno se siente necesario", "Es una forma de sentirse parte."), ex("Verdadero o falso: dentro de un pueblo todas las personas son idénticas.", "Falso", "Cada persona es distinta."), ex("¿Qué haces si alguien habla poco su lengua?", "Lo animo", "Aprender lleva tiempo.")],
    task=T("Lee este caso inventado: «Sofía canta canciones de su familia con su abuela. Mateo ayuda a su comunidad a limpiar el río. Pedro cocina pan con su mamá.» Escribe para cada niño qué aspecto de la cultura aparece y cómo creerías que se siente parte de su grupo. Escribe una frase para valorar a cada uno. No escribas datos de tus compañeros.",
           "Sofía: música; se siente unida a su familia. Mateo: trabajo; se siente necesario. Pedro: comida; se siente parte de su casa. Valoro a Sofía diciendo: «Qué bonita tradición».",
           ["identifica un aspecto por niño", "explica cómo ayuda a la identidad", "escribe frases de valoración"], ["tres filas", "tres frases"], ["comparar quién es mejor", "burlarse"],
           "Reconocer frases respetuosas; si hay comparaciones, conversar sobre diversidad."),
    reinforce="Copia tres aspectos de la cultura y escribe una frase que los valore.",
    extend="Escribe una frase que explique por qué todas las culturas valen lo mismo.",
)

L(
    OA8, 3,
    materials="Lápiz y hojas. Los casos y testimonios son inventados.",
    use="Aprenderé que la cultura de un pueblo vive y cambia, y que tiene personas actuales que la llevan adelante. Sirve para no ver la cultura como un objeto de museo.",
    prior=["Sé que la cultura forma identidad.", "Sé que todas las culturas valen lo mismo."],
    explain=[
        "La cultura no está quieta. Cambia con el tiempo, pero sigue viva. Una canción antigua puede cantarse hoy con otros instrumentos. Un oficio antiguo puede hacerse con nuevas herramientas. Lo que importa es que las personas lo sigan haciendo con sentido.",
        "Hoy hay personas de pueblos originarios que son profesoras, cantantes, médicas, artesanas y estudiantes. Ellas llevan su cultura adelante en su vida diaria. En muchas escuelas de Chile existe una asignatura de lengua y cultura de los pueblos originarios, con apoyo de educadores tradicionales.",
        "Cuando hablamos de cultura, es importante usar el presente: «el pueblo mapuche vive», «el pueblo aymara cría». También es importante reconocer a las personas de hoy. La cultura no se guarda en una vitrina, se vive todos los días con la gente.",
    ],
    vocab=[("cambio", "cuando algo se vuelve distinto con el tiempo"), ("continuidad", "cuando algo sigue existiendo"), ("oficio", "trabajo que se aprende y se hace con las manos"), ("educador tradicional", "persona de la comunidad que enseña saberes de su pueblo"), ("vitrina", "caja de vidrio donde se muestran objetos antiguos")],
    worked=[
        W("Cambio y continuidad", "Caso inventado: «Mi tía teje como la enseñó mi abuela, pero hoy usa lana de colores nuevos». ¿Qué cambió y qué sigue igual?", ["Cambió el color de la lana.", "Sigue igual la forma de tejer.", "Escribo cada cosa por separado."], "Cambió el color de la lana; sigue igual la forma de tejer."),
        W("Persona actual", "Una niña dice: «Mi profesora es educadora tradicional». ¿Es una persona del pasado o de hoy?", ["Ella enseña a la niña ahora.", "Entonces es una persona actual.", "Su saber se transmite hoy."], "De hoy"),
    ],
    mistakes=[
        M("Pensar que la cultura indígena solo está en los museos.", "Se vive hoy con personas reales.", "Busca a las personas que la practican hoy."),
        M("Creer que si algo cambia, ya no es auténtico.", "Una cultura viva siempre cambia un poco.", "Pregunta qué sigue igual y qué cambió."),
    ],
    R=[
        ex("Una profesora enseña hoy la lengua de su pueblo. ¿Es una persona actual? Responde Sí o No.", "Sí", "Ella enseña hoy."),
        ex("Una canción antigua se canta hoy. ¿La cultura sigue viva o no?", "Sigue viva", "La gente la canta ahora."),
        ex("Un museo guarda objetos antiguos. ¿Toda la cultura de un pueblo está solo en el museo? Responde Sí o No.", "No", "La cultura se vive hoy con la gente."),
    ],
    C=[
        ex("Verdadero o falso: si una cultura cambia un poco, deja de existir.", "Falso", "Puede cambiar y seguir viva."),
        ex("Una artesana usa lana de colores nuevos pero teje igual que su abuela. ¿Qué continúa? A) La forma de tejer B) El color", "A", "La técnica sigue igual."),
        ex("¿Dónde existe hoy una asignatura de lengua y cultura de los pueblos originarios? A) En muchas escuelas de Chile B) En ninguna", "A", "Existe en muchas escuelas con educadores tradicionales."),
    ],
    A=[
        ex("Clasifica como CAMBIÓ o CONTINÚA: a) hoy se graba con teléfono b) se sigue cantando en familia c) la comida se prepara igual.", "a cambió, b continúa, c continúa", "Solo el teléfono es nuevo."),
        ex("Escribe en presente: «El pueblo mapuche vivía entre bosques». Escribe la frase corregida.", "El pueblo mapuche vive entre bosques", "La ficha mapuche usa el presente porque el pueblo existe hoy."),
        ex("Une persona de hoy y su trabajo. 1) educador tradicional 2) artesana 3) estudiante. a) hace objetos con sus manos b) aprende en la escuela c) enseña saberes de su pueblo", "1-c, 2-a, 3-b", "Cada persona de hoy hace una cosa distinta."),
    ],
    Z=[
        ex("Rosa dice: «La cultura mapuche solo está en el pasado». ¿Qué ficha de este cuaderno usarías para responderle?", "La ficha mapuche: vive en el centro y sur de Chile", "La ficha usa el presente: el pueblo vive hoy."),
        ex("Pedro dice: «Ese oficio ya no es auténtico porque usa herramientas nuevas». Ana dice: «Sigue siendo suyo». ¿Quién tiene razón?", "Ana", "La cultura puede cambiar sus herramientas y continuar."),
    ],
    D=[
        ex("Un abuelo enseña una canción a su nieta y ella la graba en su teléfono con permiso. ¿Qué cambió y qué continúa?", "Cambió el medio de guardarla; continúa la enseñanza", "Se usa un teléfono, pero el abuelo sigue transmitiendo."),
        ex("Un niño dice que va a dibujar una persona de un pueblo originario con ropa antigua porque hoy ya no existen. ¿Qué error comete?", "Piensa que ya no existen", "Los pueblos originarios viven hoy."),
    ],
    context=[ex("La escuela invita a un educador tradicional. Julia pregunta si él es parte del pasado. ¿Qué le respondes?", "No, enseña hoy", "Es una persona actual que enseña ahora.")],
    selfcheck=[ex("¿Qué significa que una cultura está viva?", "Que las personas la practican hoy", "Se vive todos los días."), ex("¿Qué tiempo verbal usas para hablar de un pueblo que existe?", "El presente", "Así muestras que existe."), ex("Verdadero o falso: cambiar herramientas es dejar de ser auténtico.", "Falso", "La cultura puede cambiar y seguir viva.")],
    task=T("Lee este caso inventado: «Doña Rosa enseña a hilar lana como le enseñó su mamá. Ahora también muestra su trabajo en una feria y vende con un teléfono.» Haz dos columnas: «continúa» y «cambió». Luego escribe dos frases en presente sobre doña Rosa. No dibujes símbolos sagrados.",
           "Continúa: enseñar a hilar como su mamá. Cambió: usa teléfono para vender. Frases: Doña Rosa enseña a hilar. Doña Rosa muestra su trabajo en la feria.",
           ["separa lo que continúa de lo que cambió", "usa verbos en presente", "reconoce a una persona actual"], ["dos columnas", "dos frases"], ["escribir todo en pasado", "decir que cambiar es perder"],
           "Valorar el uso del presente y la distinción cambio-continuidad."),
    reinforce="Escribe tres frases en presente sobre un pueblo de las fichas.",
    extend="Escribe una pregunta para un educador tradicional: ¿qué ha cambiado y qué sigue igual en la forma de enseñar?",
)

L(
    OA8, 4,
    materials="Lápiz, hojas y colores. Los casos están escritos aquí.",
    use="Aprenderé a valorar la cultura de otros con acciones concretas: escuchar, no burlarse y no usar cosas sagradas como disfraz. Sirve para convivir con respeto.",
    prior=["Sé que todas las culturas valen lo mismo.", "Sé que la cultura está viva."],
    explain=[
        "Valorar la cultura de otras personas se nota en lo que hacemos. Escuchar con atención, preguntar con respeto y agradecer cuando alguien comparte algo. No burlarse de un acento, de una comida o de una ropa distinta. Eso es parte de la convivencia.",
        "Hay cosas que no se deben usar como disfraz ni como juego. Las prendas y los símbolos importantes de un pueblo tienen un sentido especial. Usarlos sin saber puede ofender. Si queremos conocerlos, pedimos que una persona de la comunidad nos los explique.",
        "Tampoco hay que pedirle a un compañero que hable por todo su pueblo. Una persona solo puede contar su experiencia. Y no hay que pedir que muestre o haga cosas de su cultura como espectáculo. Quien quiere compartir, lo hace cuando está listo.",
    ],
    vocab=[("convivencia", "vivir juntos con respeto"), ("símbolo", "dibujo u objeto que representa una idea importante"), ("disfraz", "ropa que se usa para parecer otra cosa"), ("ofender", "hacer sentir mal a alguien"), ("espectáculo", "algo que se muestra solo para que otros miren")],
    worked=[
        W("Elegir la acción respetuosa", "Un compañero trae una comida típica de su pueblo. ¿Qué haces? a) me burlo de su olor b) le pregunto cómo se llama y le agradezco c) le digo que es rara.", ["Burlarse y decir que es rara ofenden.", "Preguntar y agradecer valora.", "Elijo la acción respetuosa."], "b"),
        W("Disfraz", "Para una fiesta escolar, un grupo propone disfrazarse de «indígenas» con símbolos que no conocen. ¿Qué es mejor hacer?", ["Usar símbolos sin conocerlos puede ofender.", "Es mejor invitar a una persona de la comunidad.", "Así aprendemos con respeto."], "Invitar a una persona de la comunidad que explique"),
    ],
    mistakes=[
        M("Usar símbolos de un pueblo como disfraz.", "Tienen un sentido especial para ese pueblo.", "Pide que una persona de la comunidad los explique."),
        M("Pedir a un compañero que hable por todo su pueblo.", "Solo puede contar su propia experiencia.", "Pregunta solo si quiere compartir y escucha sin presionar."),
    ],
    R=[
        ex("Cuando alguien comparte una comida de su cultura, ¿qué es mejor: agradecer o burlarse?", "Agradecer", "Agradecer muestra respeto."),
        ex("Un símbolo importante de un pueblo se usa como disfraz. ¿Está bien? Responde Sí o No.", "No", "Puede ofender porque tiene un sentido especial."),
        ex("Si un compañero no quiere contar algo de su cultura, ¿lo obligas? Responde Sí o No.", "No", "Cada persona decide cuándo compartir."),
    ],
    C=[
        ex("Verdadero o falso: un compañero debe hablar por todo su pueblo.", "Falso", "Solo puede hablar de su propia experiencia."),
        ex("¿Qué haces si no entiendes un símbolo? A) Pregunto a una persona de la comunidad B) Lo uso igual", "A", "Preguntar evita ofender."),
        ex("Burlarse de un acento es una acción: A) respetuosa B) que ofende", "B", "Hace sentir mal a la otra persona."),
    ],
    A=[
        ex("Marca las acciones que valoran la cultura: a) escuchar con atención b) disfrazarse con símbolos sagrados c) agradecer d) reírse de la comida.", "a y c", "Escuchar y agradecer valoran."),
        ex("Ordena para recibir a un educador tradicional: 1) agradecerle al final 2) saludar con respeto 3) escuchar sin interrumpir. Escribe el orden.", "2, 3, 1", "Primero se saluda, luego se escucha y al final se agradece."),
        ex("Una niña trae un tejido de su familia. ¿Qué le pides? A) Que me deje tocarlo sin preguntar B) Que me cuente lo que quiera sobre él", "B", "Respetas su ritmo y su permiso."),
    ],
    Z=[
        ex("Tomás dice: «Me disfrazo de indígena porque me gusta». ¿Qué le dirías sobre símbolos y respeto?", "Que algunos símbolos tienen un sentido especial y hay que preguntar", "Usarlos sin saber puede ofender."),
        ex("Ema le dice a una compañera: «Cuéntanos todo lo de tu pueblo». ¿Qué error comete?", "Le pide hablar por todo su pueblo", "Una persona no representa a todos."),
    ],
    D=[
        ex("Un curso quiere hacer una fiesta de la cultura. Tres ideas: a) invitar a un educador tradicional b) que todos se disfracen con símbolos sagrados c) compartir comidas que cada familia quiera traer. ¿Cuáles respetan las culturas?", "a y c", "Invitar y compartir libremente respetan."),
        ex("Una persona no quiere que tomes fotos de su ropa tradicional. ¿Sacas la foto de todos modos? Responde Sí o No.", "No", "Se respeta su decisión."),
    ],
    context=[ex("Tu curso hará un cartel «Respetamos las culturas». Lía propone dibujar un símbolo sagrado que vio en un libro. ¿Qué le dices?", "Que mejor pregunte a un educador tradicional", "Los símbolos sagrados no se usan sin permiso.")],
    selfcheck=[ex("Escribe dos acciones que valoran la cultura de otros.", "Escuchar con atención y agradecer", "Son acciones de respeto."), ex("¿Por qué no se debe usar un símbolo sagrado como disfraz?", "Porque tiene un sentido especial", "Puede ofender si se usa sin saber."), ex("¿Qué haces si un compañero no quiere compartir algo?", "Lo respeto", "Cada uno decide.")],
    task=T("Crea un cartel de curso con el título «Respetamos las culturas». Escribe cuatro reglas de convivencia, por ejemplo cómo escuchar, qué no decir y cómo agradecer. Decóralo con dibujos de tu propio invento, sin copiar símbolos sagrados. Después escribe cómo pedirías a un educador tradicional que te explique un símbolo.",
           "1. Escuchamos sin interrumpir. 2. No nos burlamos. 3. Preguntamos con respeto. 4. Agradecemos. Pedido: «¿Podría explicarme qué significa este símbolo, por favor?».",
           ["escribe cuatro reglas", "incluye una forma de agradecer", "evita copiar símbolos sagrados"], ["cartel", "frase de pedido"], ["reglas que ofenden", "copiar símbolos sagrados"],
           "Revisar que ninguna regla excluya o ridiculice y que el pedido sea respetuoso."),
    reinforce="Copia dos reglas de convivencia del cartel y dibuja una.",
    extend="Escribe una regla más que ayude a valorar la cultura de otra persona.",
)

# ============================================================ OA 09 · Territorio, lengua e historia en la identidad
L(
    OA9, 1,
    materials="Lápiz y hojas. Las fichas de los pueblos están escritas en el cuaderno.",
    use="Aprenderé que el territorio, la lengua y la historia ayudan a formar la identidad de un pueblo. Sirve para ver cómo estas tres cosas se relacionan.",
    prior=["Sé qué es la identidad.", "Sé que una ficha tiene una fuente."],
    explain=[
        "Tres cosas ayudan a formar la identidad de un pueblo. El territorio es el lugar donde vive. La lengua es el idioma que habla. La historia es lo que recuerda y cuenta de su pasado. Las tres se mezclan y se necesitan.",
        "Por ejemplo, el territorio es el lugar donde se aprenden los nombres de los cerros y los ríos. La lengua sirve para nombrar y contar ese territorio. La historia guarda los recuerdos de quienes vivieron allí. Así se forma la identidad.",
        "No todo pueblo tiene los mismos territorios, lenguas e historias. Cada ficha cuenta algo distinto. Para saberlo se usan fuentes: personas de la comunidad, educadores tradicionales o fichas que digan quién cuenta. Y la identidad no se reduce a una lista: es algo vivo.",
    ],
    vocab=[("territorio", "lugar donde vive un pueblo"), ("lengua", "idioma que habla un pueblo"), ("historia", "lo que un pueblo recuerda de su pasado"), ("identidad", "cómo un pueblo se reconoce"), ("relación", "forma en que dos cosas se unen")],
    worked=[
        W("Ordenar los datos de una ficha", G_MAP + " Escribe el territorio, la lengua y un dato de paisaje.", ["Territorio: centro y sur de Chile.", "Lengua: mapuzugun.", "Paisaje: bosques, ríos y volcanes."], "Territorio: centro y sur de Chile. Lengua: mapuzugun. Paisaje: bosques, ríos y volcanes."),
        W("No mezclar pueblos", "Ema lee la ficha kawésqar y la ficha aymara. Escribe que el pueblo kawésqar habla aymara. ¿Qué error comete?", ["La ficha kawésqar dice que su lengua es el kawésqar.", "El aymara es la lengua del pueblo aymara.", "Mezcló dos fichas."], "Mezcló lenguas de dos pueblos"),
    ],
    mistakes=[
        M("Pensar que todos los pueblos hablan la misma lengua.", "Cada pueblo tiene su propia lengua.", "Lee la ficha de cada pueblo."),
        M("Reducir la identidad a una lista de datos.", "La identidad también incluye lo que las personas sienten y viven.", "Usa la ficha como ayuda, pero recuerda que hay personas reales."),
    ],
    R=[
        ex("El lugar donde vive un pueblo es su territorio. ¿Es verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿El idioma que habla un pueblo es su lengua o su ropa?", "Su lengua", "La lengua es el idioma."),
        ex("¿Lo que un pueblo recuerda de su pasado es su historia o su comida?", "Su historia", "La historia guarda los recuerdos."),
    ],
    C=[
        ex("¿Qué tres cosas ayudan a formar la identidad de un pueblo? A) territorio, lengua e historia B) dinero, auto y casa", "A", "Son las tres ideas de la clase."),
        ex("Verdadero o falso: todos los pueblos hablan la misma lengua.", "Falso", "Cada pueblo tiene su propia lengua."),
        ex("Según la ficha aymara de este cuaderno, ¿cuál es su lengua? (" + G_AYM + ")", "El aymara", "La ficha dice que su lengua es el aymara."),
    ],
    A=[
        ex("Ficha mapuche: " + G_MAP + " Une dato y aspecto. 1) centro y sur de Chile 2) mapuzugun 3) bosques, ríos y volcanes. a) lengua b) paisaje c) territorio", "1-c, 2-a, 3-b", "Cada dato corresponde a ese aspecto."),
        ex("Une pueblo y lengua. 1) aymara 2) kawésqar 3) mapuche. a) kawésqar b) mapuzugun c) aymara", "1-c, 2-a, 3-b", "Cada ficha dice la lengua de su pueblo."),
        ex("Ficha rapa nui: " + G_RN + " ¿Cuál es el territorio de este pueblo?", "La isla Rapa Nui, en el océano Pacífico", "La ficha dice dónde vive el pueblo."),
    ],
    Z=[
        ex("Pedro dice: «Con saber el territorio ya conozco la identidad de un pueblo». ¿Qué le falta?", "La lengua y la historia", "La identidad tiene tres partes."),
        ex("Lía lee la ficha kawésqar y dice que ese pueblo no tiene territorio porque no vive en una ciudad. ¿Es correcto? Responde Sí o No.", "No", "La ficha dice que vive en los canales de la Patagonia occidental."),
    ],
    D=[
        ex("Ficha inventada: «Los abuelos de Valle Alto cuentan historias en su lengua mientras caminan por los cerros». ¿Qué tres cosas aparecen juntas?", "Historia, lengua y territorio", "Se cuentan historias, en una lengua, en un lugar."),
        ex("Una niña dice que no necesita saber la historia de su pueblo para sentirse parte. Otra dice que ayuda mucho. ¿Qué hace la historia por la identidad?", "Guarda los recuerdos de quienes vivieron antes", "Da un pasado compartido."),
    ],
    context=[ex("El curso arma un cartel con la ficha mapuche, la aymara y la kawésqar. Tomás escribe que las tres lenguas se llaman igual. ¿Está bien?", "No", "Cada ficha dice una lengua distinta.")],
    selfcheck=[ex("Escribe qué es el territorio, con tus palabras.", "El lugar donde vive un pueblo", "Es la definición."), ex("¿Por qué la lengua ayuda a la identidad?", "Porque sirve para nombrar y contar", "Con ella se habla del territorio y la historia."), ex("Verdadero o falso: la identidad es solo una lista de datos.", "Falso", "También es lo que las personas viven y sienten.")],
    task=T("Elige UNA ficha de este cuaderno (aymara, kawésqar, mapuche o rapa nui). Dibuja un triángulo con tres vértices: territorio, lengua e historia. Escribe en cada vértice un dato de la ficha. En historia puedes escribir «pregunta al educador tradicional» si la ficha no trae el dato. No inventes datos.",
           "Elegí la ficha mapuche. Territorio: centro y sur de Chile. Lengua: mapuzugun. Historia: pregunta al educador tradicional qué historias cuenta su comunidad.",
           ["usa tres vértices", "escribe datos de la ficha", "no inventa la historia"], ["triángulo con tres datos"], ["inventar historia", "mezclar fichas"],
           "Reconocer cuando señala que falta la fuente en lugar de inventar."),
    reinforce="Subraya en cada ficha el territorio con un color y la lengua con otro.",
    extend="Escribe una pregunta sobre la historia de un pueblo para un educador tradicional.",
)

L(
    OA9, 2,
    materials="Lápiz y hojas. Los datos sobre las palabras mapuche están escritos aquí.",
    use="Aprenderé cómo se relacionan el territorio, la lengua y la historia. Sirve para entender por qué un nombre o una palabra guarda memoria de un lugar.",
    prior=["Sé que el territorio, la lengua y la historia forman la identidad.", "Sé que no se inventan significados."],
    explain=[
        "El territorio, la lengua y la historia están conectados. Los nombres de los lugares se dicen en una lengua. Esa lengua sirve para nombrar y contar el territorio. Y las historias de un pueblo se cuentan en su lengua y dentro de su territorio.",
        "Un ejemplo seguro es la palabra mapuche. «Mapu» quiere decir tierra y «che» quiere decir gente. Entonces mapuche se puede entender como gente de la tierra. Así, el nombre del pueblo nos muestra su unión con el territorio.",
        "Otro ejemplo es Rapa Nui. Es el nombre de la isla, del pueblo y de su lengua. Los tres están unidos con el mismo nombre. No debemos inventar significados de otras palabras. Si queremos saberlos, preguntamos al educador tradicional o a la comunidad.",
    ],
    vocab=[("mapu", "tierra, en mapuzugun"), ("che", "gente, en mapuzugun"), ("mapuche", "gente de la tierra"), ("conectado", "unido con otra cosa"), ("guardar memoria", "mantener los recuerdos de un pueblo")],
    worked=[
        W("Armar el significado", "En mapuzugun «mapu» es tierra y «che» es gente. ¿Qué quiere decir «mapuche»?", ["Junto las dos palabras.", "Tierra + gente.", "Se entiende como gente de la tierra."], "Gente de la tierra"),
        W("Un nombre con tres usos", "Rapa Nui es el nombre de la isla, del pueblo y de su lengua. ¿Cuántas cosas nombra?", ["Primero la isla.", "Después el pueblo.", "Al final la lengua."], "3 cosas"),
    ],
    mistakes=[
        M("Inventar el significado de una palabra que suena indígena.", "Puede ser falso y faltar al respeto.", "Pregunta a una fuente confiable."),
        M("Creer que la lengua y el territorio no tienen relación.", "La lengua nombra y cuenta el territorio.", "Piensa en los nombres de los lugares."),
    ],
    R=[
        ex("En mapuzugun, «mapu» es tierra. ¿Qué significa «mapu»?", "Tierra", "Es el significado dado."),
        ex("En mapuzugun, «che» es gente. ¿Qué significa «che»?", "Gente", "Es el significado dado."),
        ex("Rapa Nui nombra a la isla, al pueblo y a la lengua. ¿Es verdadero o falso?", "Verdadero", "Los tres tienen el mismo nombre."),
    ],
    C=[
        ex("¿Qué quiere decir «mapuche»? A) Gente de la tierra B) Gente del mar", "A", "Se forma con «mapu» (tierra) y «che» (gente)."),
        ex("Verdadero o falso: se puede inventar el significado de una palabra que suena indígena.", "Falso", "Solo una fuente confiable puede decir lo que significa."),
        ex("¿Qué parte del nombre mapuche se refiere a la tierra: «mapu» o «che»?", "Mapu", "«Mapu» significa tierra."),
    ],
    A=[
        ex("Une palabra y significado. 1) mapu 2) che 3) mapuche. a) gente de la tierra b) tierra c) gente", "1-b, 2-c, 3-a", "Cada palabra significa lo que se explicó."),
        ex("Si «mapu» es tierra y «che» es gente, ¿qué palabra formarías para decir «gente de la tierra» en mapuzugun?", "Mapuche", "Se unen mapu y che."),
        ex("Un lugar de práctica se llama Cerro Alto. ¿En qué lengua están sus palabras?", "En español", "«Cerro» y «alto» son palabras españolas."),
    ],
    Z=[
        ex("Julia dice: «No necesitamos la lengua para entender el territorio». ¿Qué ejemplo de esta clase le muestra que están unidos?", "Mapuche: mapu (tierra) y che (gente)", "El nombre del pueblo habla de su unión con la tierra."),
        ex("Tomás dice que «Rapa Nui» solo es el nombre de la isla. ¿Qué otras dos cosas nombra?", "El pueblo y su lengua", "Rapa Nui nombra tres cosas."),
    ],
    D=[
        ex("Un niño oye un nombre desconocido de un cerro y dice: «Seguro significa gran montaña». ¿Qué debería hacer?", "Preguntar a una fuente confiable", "No se puede adivinar el significado."),
        ex("Un abuelo de práctica cuenta una historia del río. ¿Qué tres cosas se unen cuando la cuenta en su lengua cerca del río?", "Historia, lengua y territorio", "Se cuenta un recuerdo, en un idioma, en un lugar."),
    ],
    context=[ex("Durante la clase de lengua y cultura, el educador tradicional explica que «mapuche» une tierra y gente. Mateo dice que eso muestra la unión con el territorio. ¿Tiene razón?", "Sí", "El nombre une tierra y gente.")],
    selfcheck=[ex("¿Qué significan «mapu» y «che»?", "Tierra y gente", "Son los significados de esta clase."), ex("¿Por qué no inventamos significados?", "Porque pueden ser falsos", "Solo una fuente confiable los sabe."), ex("Verdadero o falso: la lengua sirve para nombrar y contar el territorio.", "Verdadero", "Con ella se nombra y se cuenta el lugar.")],
    task=T("Con las palabras «mapu» (tierra) y «che» (gente), arma una tarjeta que diga qué significa «mapuche». Dibuja a una persona junto a un paisaje de bosque y río. Debajo, escribe una frase que explique cómo el nombre muestra la unión entre gente y territorio. No escribas otras palabras de mapuzugun sin preguntar al educador tradicional.",
           "Tarjeta: mapuche = mapu (tierra) + che (gente) = gente de la tierra. Dibujo: una persona junto a un río. Frase: el nombre une a las personas con su tierra.",
           ["explica mapuche con mapu y che", "relaciona nombre y territorio", "no agrega palabras inventadas"], ["tarjeta", "dibujo", "frase"], ["inventar otras palabras", "escribir palabras sin fuente"],
           "Verificar que solo use las palabras dadas; si agregó otras, pedir que confirme con el educador tradicional."),
    reinforce="Escribe tres veces el significado de mapu, che y mapuche.",
    extend="Escribe una pregunta para el educador tradicional sobre el nombre de un lugar de tu zona.",
)

L(
    OA9, 3,
    materials="Lápiz y hojas. Los casos están escritos aquí.",
    use="Aprenderé que las lenguas y las historias de los pueblos siguen vivas, que algunas necesitan cuidado y que hay personas que las enseñan hoy. Sirve para valorar la lengua como parte de la identidad.",
    prior=["Sé que la lengua es parte de la identidad.", "Sé que hay educadores tradicionales."],
    explain=[
        "Las lenguas de los pueblos originarios siguen vivas. Se hablan, se enseñan y se aprenden hoy. Algunas las hablan muchas personas y otras las hablan pocas. Cuando una lengua la hablan pocas personas, es importante cuidarla para que no se pierda.",
        "Hay muchas formas de cuidar una lengua. Los niños pueden escuchar a los abuelos, los educadores tradicionales pueden enseñar en las escuelas, y las familias pueden hablar en esa lengua en casa. Cada persona puede ayudar con respeto, aprendiendo lo que los mayores quieran enseñar.",
        "La historia también se cuida contándola. Cuando los abuelos cuentan y los jóvenes escuchan, la memoria sigue viva. Nadie tiene que saber todo. Cada persona aporta lo que sabe. Aprender una lengua o una historia lleva tiempo y se hace con paciencia.",
    ],
    vocab=[("lengua viva", "idioma que se sigue hablando"), ("cuidar una lengua", "ayudar a que siga hablándose"), ("transmitir", "pasar un saber de una persona a otra"), ("paciencia", "calma para aprender sin apuro"), ("memoria", "lo que un pueblo recuerda")],
    worked=[
        W("Formas de cuidar", "Caso inventado: la lengua de una comunidad la hablan pocas personas. ¿Qué ayudaría? a) que los niños escuchen a los abuelos b) que nadie la hable c) que se prohíba cantarla.", ["Una lengua se mantiene hablándola.", "Escuchar a los abuelos la mantiene.", "Elijo la acción que ayuda."], "a"),
        W("Paciencia al aprender", "Mateo, personaje inventado, aprende una lengua y se equivoca. ¿Qué es mejor decirle?", ["Todos aprenden poco a poco.", "No debo burlarme.", "Lo animo."], "Que siga intentando"),
    ],
    mistakes=[
        M("Creer que las lenguas indígenas ya no existen.", "Hoy se hablan y se enseñan.", "Pregunta qué personas las hablan y las enseñan hoy."),
        M("Pensar que cuidar una lengua es solo tarea de los especialistas.", "Todas las personas pueden ayudar escuchando con respeto.", "Escucha a los mayores y valora lo que enseñan."),
    ],
    R=[
        ex("Una lengua viva es un idioma que se sigue hablando. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Los niños escuchan a los abuelos hablar su lengua. ¿Esto ayuda a cuidar la lengua? Responde Sí o No.", "Sí", "La escucha mantiene viva la lengua."),
        ex("¿Aprender una lengua lleva poco o mucho tiempo?", "Mucho tiempo", "Se aprende con paciencia."),
    ],
    C=[
        ex("Verdadero o falso: las lenguas indígenas ya no se hablan en Chile.", "Falso", "Se hablan y se enseñan hoy."),
        ex("Si una lengua la hablan pocas personas, ¿qué conviene? A) Cuidarla B) Olvidarla", "A", "Cuidarla evita que se pierda."),
        ex("¿Qué significa transmitir un saber? A) Pasarlo de una persona a otra B) Guardarlo en secreto", "A", "Transmitir es compartir y enseñar."),
    ],
    A=[
        ex("Marca solo lo que ayuda a cuidar una lengua: a) escuchar a los abuelos b) burlarse del acento c) aprender con un educador tradicional d) prohibir hablarla.", "a y c", "Escuchar y aprender mantienen viva la lengua."),
        ex("Une persona y acción. 1) abuela 2) educador tradicional 3) niño. a) enseña en la escuela b) cuenta historias c) escucha y aprende", "1-b, 2-a, 3-c", "Cada una cumple un papel en cuidar la lengua."),
        ex("Una familia habla una lengua en casa los domingos. ¿Eso ayuda a cuidarla? Responde Sí o No.", "Sí", "Usarla en familia la mantiene viva."),
    ],
    Z=[
        ex("Pedro dice: «Si hablo poco la lengua, no puedo ayudar». ¿Qué le dirías?", "Que escuchar y aprender con respeto también ayuda", "Todos pueden cuidar la lengua."),
        ex("Rosa dice que una lengua que hablan pocos ya no importa. ¿Qué idea de la clase la contradice?", "Que hay que cuidarla para que no se pierda", "Una lengua con pocos hablantes necesita más cuidado."),
    ],
    D=[
        ex("Una escuela invita cada mes a una abuela de práctica a contar historias en su lengua. ¿Qué dos cosas se cuidan?", "La lengua y la memoria", "Se usa la lengua y se cuentan recuerdos."),
        ex("Un niño de práctica se equivoca al decir una palabra y otro se ríe. ¿Qué efecto puede tener la burla en aprender una lengua?", "Puede quitarle ganas de seguir aprendiendo", "La burla desanima."),
    ],
    context=[ex("Tu curso invita a una educadora tradicional. Ema propone grabarla sin avisar para tener la lengua. ¿Qué debe hacer primero?", "Pedir permiso", "Se graba solo con autorización.")],
    selfcheck=[ex("Escribe dos formas de cuidar una lengua.", "Escuchar a los mayores y aprender con un educador", "Mantienen la lengua en uso."), ex("¿Por qué hay que tener paciencia al aprender una lengua?", "Porque lleva tiempo", "Nadie aprende de golpe."), ex("Verdadero o falso: solo los especialistas pueden ayudar a cuidar una lengua.", "Falso", "Todos pueden ayudar con respeto.")],
    task=T("Lee este caso inventado: «En Valle Alto solo algunas personas mayores hablan la lengua de su comunidad. Los niños quieren ayudar.» Escribe tres ideas de qué pueden hacer los niños con respeto, sin grabar ni publicar nada sin permiso. Luego dibuja a un niño escuchando a un abuelo. No inventes palabras de ninguna lengua.",
           "Ideas: escuchar a los abuelos; pedir permiso para aprender; agradecer. Dibujo: un niño sentado junto a su abuelo escuchando.",
           ["escribe tres ideas respetuosas", "incluye permiso", "no inventa palabras de una lengua"], ["tres ideas", "dibujo"], ["grabar sin permiso", "inventar palabras"],
           "Revisar que ninguna idea implique grabar o publicar sin autorización."),
    reinforce="Escribe dos formas de ayudar a cuidar una lengua en tu familia.",
    extend="Escribe una pregunta para un educador tradicional sobre cómo cuidar la lengua de su pueblo.",
)

L(
    OA9, 4,
    materials="Lápiz y hojas. Los casos están escritos aquí.",
    use="Aprenderé a respetar la identidad de las personas sin exigirles hablar una lengua ni contar su historia. Sirve para convivir con respeto en el curso.",
    prior=["Sé que el territorio, la lengua y la historia forman la identidad.", "Sé que cuidar una lengua lleva paciencia."],
    explain=[
        "La identidad no se mide por cuánto se sabe. Una persona puede sentirse parte de su pueblo aunque no hable su lengua o no conozca toda su historia. Muchas personas están aprendiendo y eso es valioso. Nadie debe sentirse menos por saber poco.",
        "Por eso, no se le exige a nadie que hable una lengua indígena para demostrar quién es. Tampoco se le pregunta a una persona de qué pueblo es si no quiere decirlo. La identidad de cada persona es privada, y cada una decide cuándo y cómo contarla.",
        "Para respetar, escuchamos sin juzgar, preguntamos solo cuando la otra persona quiere compartir, y agradecemos lo que cuenta. Si usamos palabras de una lengua, las usamos con permiso y correctamente. Si no estamos seguros, preguntamos al educador tradicional.",
    ],
    vocab=[("privado", "que no tiene por qué contarse a todos"), ("exigir", "pedir algo como obligación"), ("juzgar", "decir que alguien es mejor o peor"), ("compartir", "contar o dar algo a otros por voluntad propia"), ("respeto", "cuidar la forma en que alguien decide mostrarse")],
    worked=[
        W("No exigir", "Un niño dice: «Si eres de tal pueblo, di una palabra en su lengua». Su compañera no quiere. ¿Qué debe hacer el niño?", ["Nadie debe demostrar su identidad hablando.", "La compañera decide qué compartir.", "El niño no insiste."], "No insistir"),
        W("Preguntar con permiso", "Quieres saber algo sobre la cultura de un compañero. ¿Qué haces primero?", ["Pregunto si quiere contarlo.", "Si dice no, lo acepto.", "Si dice sí, escucho."], "Pregunto si quiere compartir"),
    ],
    mistakes=[
        M("Exigir a alguien que hable una lengua para creerle.", "La identidad no se demuestra hablando.", "Respeta lo que la persona quiera compartir."),
        M("Preguntar a una persona de qué pueblo es sin motivo.", "Es un dato privado.", "Espera a que ella quiera contarlo."),
    ],
    R=[
        ex("¿Se debe exigir a alguien hablar una lengua indígena para demostrar quién es? Responde Sí o No.", "No", "La identidad no se demuestra así."),
        ex("Si un compañero dice «no quiero contar», ¿lo aceptas? Responde Sí o No.", "Sí", "Se respeta su decisión."),
        ex("La identidad de cada persona es privada. ¿Verdadero o falso?", "Verdadero", "Cada una decide cuándo contarla."),
    ],
    C=[
        ex("Verdadero o falso: una persona que sabe poco de su lengua no puede sentirse parte de su pueblo.", "Falso", "Puede sentirse parte aunque esté aprendiendo."),
        ex("¿Qué haces antes de preguntar algo personal a un compañero? A) Pedir permiso B) Insistir", "A", "Pedir permiso respeta su decisión."),
        ex("Si no estás seguro de cómo se dice una palabra de una lengua, ¿qué haces? A) La invento B) Pregunto al educador tradicional", "B", "Evitas equivocarte y faltar al respeto."),
    ],
    A=[
        ex("Marca las acciones respetuosas: a) escuchar sin juzgar b) obligar a hablar la lengua c) agradecer lo que cuenta d) preguntar de qué pueblo es sin motivo.", "a y c", "Escuchar y agradecer respetan."),
        ex("Ordena: 1) agradezco 2) pregunto si quiere contar 3) escucho. Escribe el orden.", "2, 3, 1", "Primero pregunto, luego escucho y al final agradezco."),
        ex("Un compañero dice que su abuelo habla una lengua indígena pero él no la sabe. ¿Puede sentirse parte de su pueblo? Responde Sí o No.", "Sí", "La pertenencia no depende de saber la lengua."),
    ],
    Z=[
        ex("Tomás le dice a una compañera: «Di algo en tu lengua para creerte». ¿Qué error comete?", "Le exige demostrar su identidad", "No hay que probar nada."),
        ex("Ana dice: «Prefiero no contar de qué pueblo vengo». ¿Qué le responde una persona respetuosa?", "Está bien, gracias por decírmelo", "Respeta su decisión."),
    ],
    D=[
        ex("Un curso hace un mural de identidades. Un niño quiere que cada compañero escriba de qué pueblo es. ¿Qué cambio lo hace más respetuoso?", "Que cada uno escriba solo lo que quiera compartir", "Respeta la privacidad."),
        ex("Un adulto cuenta una historia de su pueblo y pide que no se publique. ¿La publicas? Responde Sí o No.", "No", "Se respeta su límite."),
    ],
    context=[ex("En clase, Julia dice que su abuela habla una lengua indígena pero ella no. Pedro le dice que entonces no es de su pueblo. ¿Qué le responderías a Pedro?", "Que se puede pertenecer aunque se esté aprendiendo", "La identidad no depende de hablar.")],
    selfcheck=[ex("¿Se debe exigir a alguien que demuestre su identidad?", "No", "Es privada y no se prueba."), ex("¿Qué haces si alguien no quiere contar algo?", "Respeto su decisión", "Cada persona decide."), ex("Verdadero o falso: se puede usar palabras de una lengua sin permiso ni cuidado.", "Falso", "Se usan con permiso y con cuidado.")],
    task=T("Escribe una carta corta para un compañero inventado, Mateo, que está aprendiendo la lengua de su pueblo. Incluye tres frases: una para animarlo, una para agradecer que comparta y una para decirle que no tiene que demostrar nada. Dibuja una tarjeta con un paisaje de tu propio invento. No uses palabras de ninguna lengua indígena.",
           "Querido Mateo: sigue aprendiendo, vas muy bien. Gracias por compartir lo que sabes. No tienes que demostrar nada para ser parte de tu pueblo. Tu amigo.",
           ["escribe tres frases respetuosas", "no exige demostrar identidad", "evita palabras inventadas"], ["carta", "dibujo"], ["exigir demostraciones", "burlarse"],
           "Valorar frases de ánimo y respeto; corregir cualquier comparación entre personas."),
    reinforce="Escribe dos frases que animen a alguien que está aprendiendo.",
    extend="Escribe una regla del curso para respetar la identidad de todos.",
)

"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 16 (relación entre ser humano, naturaleza y cosmos) y OA 17 (expresiones de arte indígena).

Todos los personajes, fichas y relatos de práctica son inventados y están en castellano; no
pertenecen a ningún pueblo. Solo se nombran hechos generales y ampliamente conocidos (pueblos
reconocidos en Chile, ubicación general de su territorio, tipos de arte conocidos). El saber, la
lengua y los significados de cada pueblo los enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA16 = "LC02 OA 16"
OA17 = "LC02 OA 17"

# ================================================================ OA 16
register(
    OA16, 1,
    materials="Este cuaderno y lápiz. Las fichas están escritas aquí; los personajes son inventados. El saber de cada pueblo lo comparte su educador/a tradicional.",
    use="Aprenderé a anotar de dónde viene lo que aprendo sobre la naturaleza y el cielo: el pueblo, el territorio y quién lo enseña. Sirve para no mezclar pueblos ni inventar.",
    prior=["Sé que en Chile viven varios pueblos originarios.", "Sé escuchar con respeto."],
    explain=[
        "En Chile hay varios pueblos originarios, entre ellos el Aymara, el Quechua, el Mapuche, el Rapa Nui, el Kawésqar y el Yagán. Cada pueblo tiene su territorio, que es el lugar donde vive o vivió. Cada uno mira la naturaleza y el cielo a su manera. Por eso no se dice «todos piensan igual».",
        "En algunas comunidades se enseña que las personas, la tierra, el agua, los animales y el cielo están unidos. Cada comunidad lo explica a su manera. A esa unión se le llama relación entre ser humano, naturaleza y cosmos. El cosmos es el cielo, el sol, la luna y las estrellas junto con todo lo que existe. Para aprender esto necesitas una fuente, que es la persona o el libro de donde viene lo que sabes.",
        "La mejor fuente es una persona de la comunidad, como un educador o educadora tradicional. Sigue tres pasos. Primero pide permiso. Después escucha con atención. Al final anota el pueblo, el territorio y quién te enseñó. Si no sabes un dato, pregúntalo y no lo inventes.",
    ],
    vocab=[("ser humano", "persona"), ("naturaleza", "la tierra, el agua, las plantas y los animales"), ("cosmos", "el cielo y todo lo que existe en él"), ("fuente", "persona o libro de donde viene lo que sabes"), ("territorio", "lugar donde vive o vivió un pueblo")],
    worked=[
        {"title": "Completar una ficha", "problem": "Don Mateo, personaje inventado, es educador tradicional de un pueblo. Hoy cuenta cómo cuida la quebrada que pasa junto a su casa, en el sur de Chile. Dice: «Pueden anotar lo que digo». ¿Qué anotas en tu ficha?", "steps": ["Pueblo: el que dice Don Mateo cuando se presenta.", "Territorio: el sur de Chile, cerca de la quebrada.", "Quién enseña: Don Mateo, educador tradicional.", "Permiso: sí, porque dijo que podemos anotar."], "answer": "Pueblo, territorio (sur de Chile), quién enseña (Don Mateo) y permiso (sí)"},
        {"title": "Detectar lo que falta", "problem": "Una ficha dice: «Pueblo: Aymara. Enseña: una educadora tradicional. Permiso: sí». ¿Qué dato falta?", "steps": ["Reviso los tres datos: pueblo, territorio y quién enseña.", "Pueblo aparece y quién enseña aparece.", "El territorio no aparece, así que lo pregunto."], "answer": "Falta el territorio"},
    ],
    mistakes=[
        {"wrong": "Decir «todos los pueblos originarios creen lo mismo».", "why": "Cada pueblo tiene su territorio, su historia y su manera de mirar la naturaleza.", "fix": "Di de qué pueblo y de qué lugar es lo que escuchaste."},
        {"wrong": "Poner un territorio al azar cuando no lo sabes.", "why": "Un dato inventado deja la ficha falsa y no respeta a la comunidad.", "fix": "Pregunta a quien enseña y anota solo lo que te respondió."},
    ],
    tiers={
        "recovery": [
            ex("Quieres aprender cómo una comunidad cuida el agua. ¿Cuál es mejor fuente: una persona de esa comunidad o un dibujo sin autor?", "Una persona de esa comunidad", "Quien vive el saber puede explicarlo y dar permiso."),
            ex("De esta lista, ¿cuáles son los tres datos que anotas antes de aprender: pueblo, territorio, quién enseña, color favorito, edad del vecino?", "Pueblo, territorio y quién enseña", "Esos tres datos dicen de dónde viene lo que aprendes."),
            ex("En la ficha «Pueblo: Rapa Nui. Quién enseña: un educador tradicional», ¿qué dato falta?", "El territorio", "Hay pueblo y quién enseña, pero no dónde vive el pueblo."),
        ],
        "understand": [
            ex("¿Qué frase es correcta: «todos los pueblos originarios piensan igual» o «cada pueblo tiene su propia mirada»?", "Cada pueblo tiene su propia mirada", "Cada pueblo tiene territorio e historia propios."),
            ex("En la frase «la lluvia cae de las nubes sobre la tierra y riega las plantas del huerto», ¿qué parte viene del cielo?", "La lluvia que cae de las nubes", "Las nubes y la lluvia están en el cielo; la tierra y las plantas están abajo."),
            ex("Una ficha dice: «Pueblo: Yagán. Territorio: canales del sur. Enseña: un libro sin autor ni año». ¿Qué parte de la ficha es débil?", "La fuente, porque el libro no tiene autor ni año", "No sabemos quién lo escribió ni cuándo, así que no se puede confiar mucho."),
        ],
        "apply": [
            ex("Ficha A: «Pueblo: Quechua. Territorio: norte de Chile. Enseña: una educadora tradicional». Ficha B: «Enseña: alguien. Territorio: no sé». ¿Cuál ficha tiene los tres datos?", "La ficha A", "La A trae pueblo, territorio y quién enseña; la B no."),
            arith("Cada ficha completa lleva 4 datos: pueblo, territorio, quién enseña y permiso. Si completas 3 fichas, ¿cuántos datos anotas en total?", "4*3", "Se suman 4 datos tres veces."),
            ex("Ordena estos pasos: a) escucho con atención, b) pido permiso a la persona, c) anoto pueblo, territorio y fuente. Escribe las letras en orden.", "b, a, c", "Primero se pide permiso, después se escucha y al final se anota."),
        ],
        "reason": [
            ex("Tomás dice: «Mi vecino me contó algo de su comunidad, así que vale para todos los pueblos». ¿Por qué se equivoca?", "Porque cada pueblo y cada comunidad tiene su propia mirada", "Lo que cuenta una comunidad no se puede aplicar a otras sin preguntar."),
            ex("Sofía no sabía el territorio y escribió uno al azar. ¿Qué debió hacer?", "Preguntar a la persona que enseña", "Solo quien enseña puede decir el dato correcto."),
        ],
        "challenge": [
            ex("Lee: «Hoy vino Doña Rosa, educadora tradicional del pueblo Quechua, a contarnos cómo su familia cuida la tierra de cultivo en el norte. Nos dio permiso para anotar». ¿Cuál es el pueblo y hay permiso?", "Pueblo Quechua; sí hay permiso", "El texto nombra al pueblo Quechua y dice que dio permiso."),
            ex("Una ficha dice: «Pueblo: Yagán. Territorio: canales del sur. Enseña: una sabia de la comunidad. Permiso: no». ¿Puedes anotar y compartir lo que escuchaste? Responde sí o no y por qué.", "No, porque falta el permiso", "Sin permiso de la comunidad no se comparte lo que se escuchó."),
        ],
    },
    context=[ex("Tu curso recibe a una educadora tradicional. Ema quiere sacar fotos sin preguntar. ¿Qué paso se saltó?", "Pedir permiso", "El primer paso es pedir permiso antes de anotar, grabar o fotografiar.")],
    selfcheck=[
        ex("¿Qué es el territorio de un pueblo?", "El lugar donde vive o vivió", "Territorio es el lugar donde vive o vivió un pueblo."),
        ex("¿Qué haces si no sabes un dato de la ficha?", "Lo pregunto", "No se inventa: se pregunta a quien enseña."),
        ex("¿Qué es el cosmos?", "El cielo y todo lo que existe en él", "Incluye el sol, la luna y las estrellas."),
    ],
    open_task=task(
        "Lee esta visita inventada: «La educadora tradicional Doña Elena, del pueblo Aymara, vino al curso y nos contó cómo su comunidad cuida las vertientes del norte. Nos dijo que podíamos anotar». Completa una ficha con cuatro líneas: Pueblo, Territorio, Quién enseña y Permiso. Después escribe una pregunta que le harías a Doña Elena.",
        "Pueblo: Aymara. Territorio: norte de Chile. Quién enseña: Doña Elena, educadora tradicional. Permiso: sí. Pregunta: ¿Qué cuidados hay que tener en una vertiente?",
        ["escribe las cuatro líneas de la ficha", "los datos coinciden con la visita", "escribe una pregunta respetuosa", "no agrega datos que no están en el texto"],
        ["ficha de cuatro líneas", "pregunta escrita"],
        ["inventar un territorio distinto", "copiar lo que dice un pueblo y atribuirlo a otro"],
        "Reconoce la ficha completa y recuérdale que Doña Elena es un personaje inventado: el saber real lo enseña la educadora tradicional de tu comunidad.",
    ),
    reinforce="Anota en tu cuaderno el nombre de un lugar que conozcas y qué persona de tu familia te lo enseñó.",
    extend="Dibuja una ficha con las cuatro líneas y llénala con una visita inventada por ti.",
)

register(
    OA16, 2,
    materials="Este cuaderno y lápiz. Los relatos de práctica son inventados y están en castellano.",
    use="Aprenderé a explicar una relación entre el cielo, la tierra y los seres vivos sin sacarla de su lugar. Sirve para entender que mirar la naturaleza con atención también es una forma de saber.",
    prior=["Sé quién es la fuente de lo que aprendo.", "Sé distinguir cielo, tierra y agua."],
    explain=[
        "Muchas comunidades observan la naturaleza con mucha atención, durante muchos años. Miran el sol, la luna, las estrellas, el viento, las plantas y los animales. Así aprenden señales, por ejemplo cuándo viene la lluvia. Observar, recordar y compartir entre generaciones es una manera de saber. Cómo la entiende cada pueblo y cómo la llama lo explica su educador o educadora tradicional.",
        "Una relación es un vínculo entre dos cosas. Cuando llueve, la tierra se moja y la semilla crece: el cielo, la tierra y las plantas se relacionan. Para explicar una relación no basta decir la palabra. Debes decir quién lo cuenta, dónde ocurre y para qué le sirve a esa comunidad.",
        "Cada comunidad explica las relaciones a su manera, con su lengua y su historia. No agregues significados que no escuchaste ni pases lo de un pueblo a otro. Si algo no se entiende, se le pregunta al educador o educadora tradicional.",
    ],
    vocab=[("observación", "mirar con atención y recordar lo que pasa"), ("relación", "vínculo entre dos cosas"), ("señal", "algo que se ve y avisa lo que puede pasar"), ("perspectiva", "manera de mirar algo"), ("conocimiento", "lo que se sabe y se enseña")],
    worked=[
        {"title": "Explicar una relación", "problem": "Doña Rosa, personaje inventado, mira el cielo cada mañana. Hoy hay nubes oscuras y hace frío. Dice que probablemente lloverá y que debe cubrir las semillas. ¿Qué relación explica?", "steps": ["Observa el cielo: nubes oscuras.", "Siente el frío en el aire.", "Relaciona esas señales con la lluvia y cuida las semillas de la tierra."], "answer": "Relación entre el cielo (nubes y frío), la lluvia y las semillas en la tierra"},
        {"title": "No sacar del lugar", "problem": "Un niño dice: «Doña Rosa mira las nubes, así que todos los pueblos hacen lo mismo». ¿Qué debe agregar para explicar bien?", "steps": ["Doña Rosa es una persona de una comunidad.", "Debo decir quién lo cuenta y dónde vive.", "No puedo asegurar que otros pueblos lo hagan igual."], "answer": "Debe decir quién lo cuenta y de qué comunidad es, sin generalizar"},
    ],
    mistakes=[
        {"wrong": "Decir que las nubes oscuras significan lo mismo para todos los pueblos.", "why": "Cada comunidad tiene su propia experiencia del lugar donde vive.", "fix": "Explica solo lo que contó la persona y de qué comunidad es."},
        {"wrong": "Agregar un significado que tú imaginaste.", "why": "Eso no lo dijo la fuente y puede ser falso.", "fix": "Cuenta lo que escuchaste y pregunta lo que no entendiste."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál de estas cosas pertenece al cielo: río, nube o piedra?", "Nube", "Las nubes están en el cielo; el río y la piedra están en la tierra."),
            ex("Observar es mirar con atención y recordar. Si miras cada día cómo cambia la luna, ¿estás observando?", "Sí", "Miras con atención y puedes recordar los cambios."),
            ex("La lluvia moja la tierra y la semilla crece. ¿Qué dos cosas ayudan a que crezca la semilla?", "La lluvia y la tierra", "La semilla necesita agua de lluvia y tierra para crecer."),
        ],
        "understand": [
            ex("«Cuando suben nubes negras, hay que guardar la ropa». ¿Qué señal avisa la lluvia?", "Las nubes negras", "La señal es lo que se ve y avisa lo que puede pasar."),
            ex("¿Qué dice una buena explicación de una relación: solo la palabra, o quién lo cuenta, dónde ocurre y para qué sirve?", "Quién lo cuenta, dónde ocurre y para qué sirve", "Eso evita sacar el saber de su lugar."),
            ex("Una abuela cuenta lo que su familia sabe del viento desde hace muchos años. ¿Este saber es nuevo o pasa de generación en generación?", "Pasa de generación en generación", "Lo sabe su familia desde hace muchos años y lo enseña."),
        ],
        "apply": [
            ex("Lee: «El sol sale, calienta la tierra, la planta abre sus hojas y las abejas llegan a las flores». ¿Cuántas cosas distintas se nombran: sol, tierra, planta, hojas, abejas y flores?", "6", "Se cuentan sol, tierra, planta, hojas, abejas y flores: seis."),
            ex("Observación de Ana durante 3 días: lunes nubes grises y lluvia; martes nubes grises y lluvia; miércoles cielo azul y sin lluvia. ¿Qué señal se repitió con la lluvia?", "Las nubes grises", "En los dos días de lluvia hubo nubes grises."),
            ex("Doña Rosa dice: «Cuando florece el árbol de mi patio, empieza la primavera». ¿Qué relación explica entre la naturaleza y el tiempo del año?", "El florecer del árbol avisa que empieza la primavera", "El árbol florece y esa señal marca la estación."),
        ],
        "reason": [
            ex("Pedro cuenta que «las estrellas guían a todos los pueblos de Chile». La fuente solo habló de una comunidad. ¿Qué error cometió?", "Generalizar a todos los pueblos", "La fuente habló de una sola comunidad."),
            ex("Una niña no entendió el significado de una señal. ¿Qué es mejor: inventar uno o preguntar a la persona que enseña?", "Preguntar a la persona que enseña", "Solo quien lo enseña conoce el significado verdadero."),
        ],
        "challenge": [
            ex("Lee: «Mi abuelo mira cómo se mueven las nubes por la mañana y recuerda lo que pasó otros años. Así decide cuándo regar. Sus hijos aprendieron mirando con él». ¿Qué tres cosas hacen que esto sea una forma de saber: observar, recordar y compartir?", "Observar las nubes, recordar otros años y enseñar a sus hijos", "Mira, recuerda y comparte lo que sabe."),
            ex("Dos amigos explican la lluvia. Beto dice solo «las nubes avisan». Lía dice: «Mi vecina Rosa, de su comunidad, mira las nubes en la mañana para cuidar sus semillas». ¿Quién explicó la relación sin sacarla de su lugar?", "Lía", "Lía dice quién lo cuenta, de dónde y para qué sirve."),
        ],
    },
    context=[ex("Tu vecina dice que cuando el viento cambia hace más frío por la noche. ¿Cómo le preguntas respetuosamente cómo lo sabe?", "Preguntando cómo lo aprendió y quién se lo enseñó", "Preguntar por la fuente muestra respeto por su saber.")],
    selfcheck=[
        ex("¿Qué es una señal de la naturaleza?", "Algo que se ve y avisa lo que puede pasar", "Una señal ayuda a anticipar lo que ocurrirá."),
        ex("¿Qué debes decir al explicar una relación además de la palabra?", "Quién lo cuenta y dónde ocurre", "Así no se saca el saber de su lugar."),
        ex("Si no entiendes un significado, ¿qué haces?", "Pregunto al educador o educadora tradicional", "No se inventan significados."),
    ],
    open_task=task(
        "Lee este relato inventado: «Doña Rosa, de una comunidad del sur, mira el cielo cada mañana. Si hay nubes oscuras, cubre sus semillas. Dice que su abuela le enseñó a mirar el cielo». Escribe en tres líneas: 1) qué observa, 2) qué relación explica y 3) quién se lo enseñó. Agrega una pregunta que le harías.",
        "1) Observa nubes oscuras. 2) Relaciona el cielo con la lluvia y las semillas en la tierra. 3) Se lo enseñó su abuela. Pregunta: ¿Qué otras señales usan en su comunidad?",
        ["escribe qué observa", "explica la relación con cielo y tierra", "dice quién se lo enseñó", "no agrega significados que el relato no dice"],
        ["tres líneas escritas", "pregunta escrita"],
        ["generalizar a todos los pueblos", "inventar significados"],
        "Reconoce que usó solo los datos del relato y que no mezcló pueblos. Recuerda que Doña Rosa es un personaje inventado.",
    ),
    reinforce="Mira el cielo tres mañanas seguidas y anota cómo estaba: despejado, nublado o con lluvia.",
    extend="Pregunta a un adulto qué señal de la naturaleza conoce para saber que va a llover y anota su respuesta con su nombre.",
)

register(
    OA16, 3,
    materials="Este cuaderno y lápiz. Los textos de práctica son inventados.",
    use="Aprenderé que el conocimiento de los pueblos originarios está vivo: cambia, se enseña hoy y tiene personas que lo cuidan. Sirve para no pensar que los pueblos son solo del pasado.",
    prior=["Sé que el saber se enseña de personas a personas.", "Sé pedir permiso."],
    explain=[
        "Los pueblos originarios no son solo del pasado. Hoy hay niñas, niños, jóvenes y personas mayores que viven, hablan y enseñan lo que su pueblo sabe. A ellos se les llama portadores del conocimiento, porque lo llevan y lo cuidan.",
        "El conocimiento está vivo porque se sigue usando y se sigue enseñando. Puede cambiar con el tiempo: hoy una abuela puede enseñar en una conversación y un joven puede grabar con permiso lo que ella dice. Cambiar la forma de enseñar no quiere decir que el saber se pierda.",
        "Quien graba, fotografía o escribe lo que dice una persona de la comunidad debe pedir permiso antes. También debe decir su nombre cuando cuente lo que aprendió. El saber tiene dueños y no se usa como si fuera de nadie.",
    ],
    vocab=[("portador", "persona que lleva y cuida un saber"), ("generación", "grupo de personas de edad parecida"), ("presente", "el tiempo de hoy"), ("permiso", "aprobación para usar o compartir algo"), ("vivo", "que se sigue usando y enseñando")],
    worked=[
        {"title": "Saber vivo", "problem": "Valentina, personaje inventado, aprende de su abuela cómo cuidar un huerto. Ahora Valentina se lo enseña a su hermano pequeño. ¿El saber está vivo? ¿Quiénes son los portadores?", "steps": ["La abuela enseñó el saber.", "Valentina lo aprendió y hoy lo enseña.", "Se sigue usando y enseñando, así que está vivo."], "answer": "Sí, está vivo; los portadores son la abuela y Valentina"},
        {"title": "Cambiar la forma, cuidar el saber", "problem": "Un joven quiere grabar en su teléfono la explicación de un educador tradicional. ¿Qué debe hacer antes?", "steps": ["Antes de grabar debe pedir permiso.", "Si la persona dice que sí, graba.", "Después dice de quién es lo que aprendió."], "answer": "Pedir permiso antes de grabar y decir de quién es el saber"},
    ],
    mistakes=[
        {"wrong": "Decir que los pueblos originarios «ya no existen».", "why": "Hoy hay personas, familias y comunidades de esos pueblos en Chile.", "fix": "Di que los pueblos originarios viven hoy y enseñan su saber."},
        {"wrong": "Grabar a una persona de la comunidad sin avisarle.", "why": "El saber tiene dueños y se necesita su permiso.", "fix": "Pregunta primero y graba solo si responde que sí."},
    ],
    tiers={
        "recovery": [
            ex("¿Los pueblos originarios son solo del pasado o también de hoy?", "También de hoy", "Hoy hay personas y comunidades de esos pueblos que viven y enseñan."),
            ex("Una abuela enseña un saber a su nieta. ¿Quién es la portadora del saber en ese momento?", "La abuela", "Ella lo lleva, lo cuida y lo enseña."),
            ex("Antes de grabar a una persona de la comunidad, ¿qué debes hacer: pedir permiso o grabar rápido?", "Pedir permiso", "Se pide permiso antes de grabar."),
        ],
        "understand": [
            ex("«Mi tío enseña a su hijo lo que aprendió de su abuelo». ¿Cuántas generaciones se nombran: abuelo, tío e hijo?", "3", "Abuelo, tío e hijo son tres generaciones."),
            ex("Un saber cambia de cuaderno a una grabación con permiso. ¿El saber se pierde o solo cambia la forma?", "Solo cambia la forma", "Se sigue usando y enseñando de otra manera."),
            ex("¿Por qué se dice que el conocimiento está «vivo»?", "Porque se sigue usando y enseñando", "Lo usan y lo enseñan personas de hoy."),
        ],
        "apply": [
            arith("Una escuela tiene 3 cursos y cada curso invita a 2 educadores tradicionales durante el año. ¿Cuántas visitas hay en total?", "3*2", "Se suman 2 visitas tres veces."),
            ex("Lee: «Hoy Camila, de 8 años, escucha a su abuelo. Mañana Camila le contará a su prima». ¿Quién es portador del saber hoy y mañana?", "Hoy el abuelo y mañana Camila", "El abuelo lo enseña hoy y Camila lo llevará mañana."),
            ex("Un niño dice: «Mi abuela me dejó anotar lo que contó». Para citar la fuente en su cuaderno, ¿qué nombre debe escribir?", "El nombre de su abuela", "Ella es quien enseñó y debe quedar mencionada como fuente."),
        ],
        "reason": [
            ex("Teo dijo: «Los pueblos originarios viven solo en libros». ¿Qué ejemplo de la vida de hoy lo contradice?", "Una abuela o educador tradicional que enseña hoy", "Hay personas que enseñan hoy a niñas y niños."),
            ex("Una joven graba a un educador sin permiso «porque es para el colegio». ¿Es correcto?", "No", "Aunque sea para el colegio, el permiso es necesario."),
        ],
        "challenge": [
            ex("Lee: «Hace 20 años, Don Juan aprendía solo oyendo. Hoy sus nietos también lo graban, con su permiso. Don Juan sigue enseñando lo mismo». ¿Qué cambió y qué se mantiene?", "Cambió la forma de guardar el saber; se mantiene el saber y el permiso", "Ahora hay grabación, pero el saber sigue y se pide permiso."),
            ex("Mía cuenta lo que aprendió y dice «esto lo dijo mi vecina Ana, con su permiso». Ema cuenta lo mismo sin nombrar a nadie. ¿Quién cuidó mejor el saber?", "Mía", "Mía dijo quién lo enseñó y que había permiso."),
        ],
    },
    context=[ex("Tu amigo quiere publicar en una red social la explicación de una abuela de la comunidad. ¿Qué le recomiendas primero?", "Preguntarle a la abuela si da permiso", "Solo ella decide si su saber se comparte.")],
    selfcheck=[
        ex("¿Qué es un portador del saber?", "Persona que lleva y cuida un saber", "Lo conserva y lo enseña."),
        ex("¿Qué haces antes de grabar a una persona de la comunidad?", "Pedir permiso", "Sin permiso no se graba."),
        ex("En Lengua y Cultura: ¿Los pueblos originarios existen hoy?", "Sí", "Hoy hay familias y comunidades de esos pueblos."),
    ],
    open_task=task(
        "Lee este caso inventado: «Rodrigo, de 8 años, vive con su abuela Nora. Ella le enseña lo que su comunidad sabe sobre cuidar el agua. Rodrigo quiere grabarla con su teléfono para mostrarlo en clases». Escribe tres frases: qué debe hacer Rodrigo antes de grabar, quién es la portadora del saber y qué debe decir en clases cuando lo muestre.",
        "Rodrigo debe pedir permiso a su abuela Nora antes de grabar. La portadora del saber es Nora. En clases debe decir que lo aprendió de su abuela, con su permiso.",
        ["dice que pide permiso antes de grabar", "nombra a Nora como portadora", "dice que cita la fuente en clases"],
        ["tres frases escritas"],
        ["grabar sin preguntar", "no nombrar a quién enseñó"],
        "Reconoce que respetó el permiso y la fuente. Recuérdale que Rodrigo y Nora son personajes inventados.",
    ),
    reinforce="Pregunta a un adulto de tu casa qué cosa aprendió de una persona mayor y anota su nombre como fuente.",
    extend="Dibuja a dos personas: una que enseña un saber y otra que lo aprende. Escribe quiénes son.",
)

register(
    OA16, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a elegir acciones respetuosas con la naturaleza y con el saber de las comunidades. Sirve para cuidar y devolver algo a la tierra y a las personas que me enseñan.",
    prior=["Sé que el saber tiene dueños.", "Sé que el conocimiento está vivo."],
    explain=[
        "Reciprocidad quiere decir dar algo a cambio de lo que se recibe. Todas las personas recibimos de la tierra, del agua y de los animales alimento, agua y vida. Cuidar es una forma de devolver. Este cuaderno cuenta la idea en general. Cómo lo entiende y lo practica cada pueblo lo enseña su educador o educadora tradicional.",
        "Tú también puedes cuidar. Puedes ahorrar agua, no botar basura, no arrancar plantas sin necesidad y no molestar a los animales. También cuidas cuando respetas el saber de otras personas: pides permiso, escuchas, dices quién te enseñó y no lo usas para burlarte.",
        "Para elegir una acción respetuosa hazte tres preguntas. Primero: ¿cuida la naturaleza? Segundo: ¿respeta a las personas que enseñaron? Tercero: ¿pedí permiso si usé su saber? Si respondes sí a las tres, la acción es respetuosa.",
    ],
    vocab=[("reciprocidad", "dar algo a cambio de lo que se recibe"), ("cuidar", "proteger para que no se dañe"), ("respeto", "tratar con cuidado a personas, saberes y seres vivos"), ("agradecer", "decir o mostrar que se valora lo recibido"), ("acción", "algo que se hace")],
    worked=[
        {"title": "Elegir la acción respetuosa", "problem": "Luis puede: a) cortar flores de una plaza para su mesa, b) regar con un vaso de agua una planta seca del patio. ¿Cuál acción cuida la naturaleza?", "steps": ["Pregunta 1: ¿cuida la naturaleza? La a) corta plantas; la b) las cuida.", "La acción b) ayuda a la planta a vivir."], "answer": "La b) regar la planta seca"},
        {"title": "Devolver al que enseña", "problem": "Una educadora tradicional te enseñó un saber en clase. ¿Cómo puedes agradecerle y respetar su saber?", "steps": ["Le digo gracias y la escucho con atención.", "Cuando cuento lo que aprendí, digo su nombre.", "No lo cambio ni me burlo."], "answer": "Dándole las gracias, diciendo su nombre y sin cambiar su saber"},
    ],
    mistakes=[
        {"wrong": "Cuidar la naturaleza pero copiar el saber de otros sin decir quién lo enseñó.", "why": "El respeto incluye a la naturaleza y a las personas.", "fix": "Cuida las plantas y también di el nombre de quien te enseñó."},
        {"wrong": "Pensar que reciprocidad es solo recibir.", "why": "Reciprocidad es recibir y también devolver.", "fix": "Piensa qué puedes dar o cuidar a cambio."},
    ],
    tiers={
        "recovery": [
            ex("Reciprocidad quiere decir dar algo a cambio de lo que se recibe. Si la tierra te da alimento, ¿qué puedes hacer: cuidarla o ensuciarla?", "Cuidarla", "Cuidar la tierra es una forma de devolver."),
            ex("¿Cuál acción cuida el agua: dejar la llave abierta o cerrarla al lavarte los dientes?", "Cerrarla al lavarte los dientes", "Así no se desperdicia agua."),
            ex("Una educadora te enseñó un saber. ¿Qué es una buena forma de agradecer: decir gracias o irse sin decir nada?", "Decir gracias", "Agradecer muestra que valoras lo que recibiste."),
        ],
        "understand": [
            ex("De estas acciones, ¿cuáles cuidan la naturaleza: botar un papel al suelo, guardar el papel en un bolsillo o arrancar una planta por jugar?", "Guardar el papel en un bolsillo", "Así no se ensucia el lugar."),
            ex("Las tres preguntas para elegir una acción son: ¿cuida la naturaleza?, ¿respeta a quienes enseñaron? y ¿pedí permiso? ¿Cuántas preguntas son?", "3", "Se cuentan tres preguntas."),
            ex("Sofía usó un saber de una abuela, dijo su nombre y pidió permiso. ¿Cumplió las preguntas sobre las personas?", "Sí", "Respetó a quien enseñó y pidió permiso."),
        ],
        "apply": [
            arith("En el huerto de la escuela, cada grupo riega 4 plantas. Hay 5 grupos. ¿Cuántas plantas se cuidan?", "4*5", "Se suman 4 plantas cinco veces."),
            ex("Mateo quiere tomar fotos de un cerro de la zona y de una abuela de la comunidad. ¿A quién debe pedir permiso primero?", "A la abuela", "Una persona decide si quiere salir en una foto."),
            ex("Elige la acción más respetuosa: a) llevar piedras de un lugar sagrado como recuerdo, b) mirar el lugar en silencio y no llevarte nada. Responde con la letra.", "b", "Así no se daña ni se toma algo que no es tuyo."),
        ],
        "reason": [
            ex("Un niño dice «cuido la naturaleza, así que no necesito pedir permiso para grabar a la educadora». ¿Qué le falta cuidar?", "El respeto a la persona que enseña", "El respeto también incluye a las personas y su saber."),
            ex("Una clase planta un árbol y agradece a la persona de la comunidad que les enseñó cómo cuidarlo. ¿Qué dos formas de devolver hicieron?", "Cuidar la naturaleza y agradecer a quien enseñó", "Plantaron un árbol y dieron las gracias."),
        ],
        "challenge": [
            ex("Un curso tiene tres ideas: 1) recoger basura del patio, 2) copiar un dibujo de una comunidad sin avisar, 3) invitar a un educador tradicional y agradecerle. ¿Cuáles dos acciones son respetuosas?", "La 1 y la 3", "Cuidan la naturaleza y a las personas; la 2 copia sin permiso."),
            ex("Lía regó una planta y después contó lo que aprendió de su vecina, diciendo su nombre y con su permiso. ¿Qué tres preguntas respondió con sí?", "Cuida la naturaleza, respeta a quien enseñó y pidió permiso", "Cuidó la planta, nombró a su vecina y tenía su permiso."),
        ],
    },
    context=[ex("En el recreo, un compañero quiere pisar un nido que encontró. ¿Qué le dices para cuidar la naturaleza?", "Que no lo pise y avise a un adulto", "Los animales y sus nidos se protegen y no se dañan.")],
    selfcheck=[
        ex("¿Qué es la reciprocidad?", "Dar algo a cambio de lo que se recibe", "Es devolver lo recibido."),
        ex("¿Cuáles son dos formas de cuidar?", "Cuidar la naturaleza y respetar a las personas", "Incluye el entorno y a quienes enseñan."),
        ex("¿Qué haces antes de usar el saber de una persona?", "Pedir permiso", "Ella decide si se comparte."),
    ],
    open_task=task(
        "Tienes estas cuatro ideas ya escritas: A) regar una planta de tu casa, B) dibujar un diseño tomado de una comunidad sin avisar, C) ahorrar agua al lavarte las manos, D) agradecer a quien te enseñó algo. Escribe las letras de las acciones respetuosas y elige una para hacer esta semana. Anota qué harás, cuándo y cómo sabrás que la hiciste.",
        "Respetuosas: A, C y D. Haré la C: cerraré la llave mientras me enjabono las manos, todos los días de esta semana. Marcaré una cruz cada día.",
        ["identifica las acciones A, C y D", "no incluye la B", "anota qué hará y cuándo", "dice cómo comprobará que la hizo"],
        ["letras escritas", "plan de una acción"],
        ["incluir la acción B", "no decir cómo comprobará"],
        "Reconoce la elección correcta y ayúdale a escribir un plan que pueda cumplir y marcar en su cuaderno.",
    ),
    reinforce="Cierra la llave del agua mientras te enjabonas las manos durante un día y cuenta cuántas veces lo hiciste.",
    extend="Escribe una nota de agradecimiento de tres líneas a una persona que te enseñó algo.",
)

# ================================================================ OA 17
register(
    OA17, 1,
    materials="Este cuaderno y lápiz. Las fichas de arte están escritas aquí. Los diseños y su significado los enseña la comunidad.",
    use="Aprenderé a reconocer expresiones de arte de pueblos originarios y a anotar de dónde vienen. Sirve para valorar el arte sin copiarlo sin permiso.",
    prior=["Sé que cada pueblo tiene su territorio.", "Sé pedir permiso."],
    explain=[
        "El arte indígena es la manera en que los pueblos originarios expresan lo que piensan, sienten y viven. Puede ser un tejido, una cerámica, una joya de plata, una talla en madera, un canasto, un canto o una danza. Una expresión es una forma de mostrar una idea o un sentimiento.",
        "Cada pueblo tiene sus propias expresiones de arte, con sus técnicas y sus significados. Qué obras hace un pueblo y cómo se llaman lo cuenta su comunidad, no una lista de un cuaderno. En las fichas de práctica de este cuaderno usamos «Pueblo A» y «Pueblo B» para no atribuir un arte a un pueblo real.",
        "Para conocer un arte, anota el pueblo, el territorio y la persona que lo hace: su autor o autora. Si no sabes uno de esos datos, no lo inventes y pregúntalo. Recuerda que muchos diseños tienen un significado propio que cuenta la comunidad.",
    ],
    vocab=[("arte", "obra o práctica creada para expresar ideas o sentimientos"), ("expresión", "forma de mostrar una idea o un sentimiento"), ("autoría", "quién creó una obra"), ("textil", "tejido hecho con hilos o lana"), ("cerámica", "objeto hecho con barro cocido")],
    worked=[
        {"title": "Anotar una expresión de arte", "problem": "En el museo ves una vasija de cerámica. La ficha de práctica dice: «Pueblo A. Hecha por una artesana de la comunidad». ¿Qué datos anotas?", "steps": ["Tipo de arte: cerámica.", "Pueblo: Pueblo A.", "Autoría: una artesana de la comunidad."], "answer": "Cerámica, Pueblo A, hecha por una artesana de la comunidad"},
        {"title": "Reconocer lo que falta", "problem": "Una foto dice solo «tejido bonito». ¿Qué datos faltan para anotarla bien?", "steps": ["No dice el pueblo.", "No dice quién la hizo.", "No dice dónde vive ese pueblo."], "answer": "Faltan el pueblo, la autoría y el territorio"},
    ],
    mistakes=[
        {"wrong": "Decir que un tejido es de cualquier pueblo porque «se parece».", "why": "Dos obras pueden parecerse y venir de lugares distintos.", "fix": "Pregunta el pueblo y la autoría antes de anotarlo."},
        {"wrong": "Llamar «adorno» a lo que tiene significado para la comunidad.", "why": "Muchos diseños cuentan algo importante para quien los hace.", "fix": "Pregunta cuál es su significado y úsalo solo como lo enseña la comunidad."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál de estas es una expresión de arte: un tejido, un lápiz roto o una mesa vacía?", "Un tejido", "El tejido puede expresar ideas y sentimientos."),
            ex("La cerámica se hace con barro. Si un objeto se hizo con barro cocido, ¿es de cerámica o textil?", "Cerámica", "La cerámica es barro cocido; el textil es de hilos."),
            ex("En un museo, la ficha de práctica de una obra dice «Pueblo A. Talla en madera». ¿Cuál es el tipo de arte?", "Talla en madera", "La ficha dice el tipo de arte al final."),
        ],
        "understand": [
            ex("Una ficha de práctica dice: «Pueblo A: textiles. Pueblo B: cerámica». ¿Qué pueblo de la ficha hace cerámica?", "El Pueblo B", "Así lo dice la ficha."),
            ex("¿Por qué no basta decir «es un tejido bonito» para conocerlo?", "Porque faltan el pueblo y la autoría", "Hay que saber quién lo hizo y de qué pueblo es."),
            ex("Un canasto fue hecho por una persona de la comunidad del Pueblo A. ¿Cómo se llama la persona que crea una obra?", "Autor o autora", "Autoría es quién creó una obra."),
        ],
        "apply": [
            ex("Ficha 1: «Pueblo A. Textil. Tejido por una artesana». Ficha 2: «Pueblo B. Platería. Hecha por un artesano». ¿Cuál ficha es de un textil?", "La ficha 1", "Solo la ficha 1 dice textil."),
            ex("En una ficha de práctica dice: «Cerámica del Pueblo A, hecha por una artesana». Escribe en una línea los tres datos: tipo de arte, pueblo y autoría.", "Cerámica; Pueblo A; una artesana", "Tipo: cerámica; pueblo: Pueblo A; autoría: una artesana."),
            arith("En una sala hay 3 vitrinas de cerámica y 2 vitrinas de textiles. ¿Cuántas vitrinas hay en total?", "3+2", "Se suman las vitrinas de cerámica y de textiles."),
        ],
        "reason": [
            ex("Un niño dice «este diseño es igual al de otro pueblo, así que es del mismo». ¿Por qué puede equivocarse?", "Porque dos obras pueden parecerse y ser de pueblos distintos", "Por parecerse no se sabe quién la hizo."),
            ex("Si no sabes el pueblo que hizo una obra, ¿es mejor inventar uno o preguntar a la persona del museo?", "Preguntar a la persona del museo", "Inventar deja una ficha falsa."),
        ],
        "challenge": [
            ex("Lee: «Hoy vimos una canasta del Pueblo A y una talla de madera del Pueblo B. Nos explicó una guía del museo». Escribe los pueblos, los tipos de arte y quién nos explicó.", "Pueblo A: canasta; Pueblo B: talla en madera; explicó una guía del museo", "Cada pueblo se une a su tipo de arte y la fuente es la guía."),
            ex("En un museo, la ficha de un textil dice «Pueblo A. Tejido por una artesana de la comunidad. Se pide no fotografiar». ¿Puedes tomar una foto?", "No", "La ficha pide no fotografiar y se respeta."),
        ],
    },
    context=[ex("Visitas una feria de artesanía con tu familia. Quieres comprar un tejido y preguntar quién lo hizo. ¿Qué dato le pides a la persona que vende?", "Quién lo hizo y de qué pueblo es", "Autoría y pueblo son los datos importantes.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es la autoría?", "Quién creó una obra", "Es la persona que hizo la obra."),
        ex("¿Qué tres datos anotas de una expresión de arte?", "Tipo de arte, pueblo y autoría", "Dicen qué es y de dónde viene."),
        ex("¿Qué haces si no sabes el pueblo de una obra?", "Pregunto", "No se inventa."),
    ],
    open_task=task(
        "Lee esta ficha inventada de un museo: «Objeto: vasija. Material: barro cocido. Pueblo: Pueblo A. Hecha por una artesana de la comunidad. Pide: no tocar». Escribe tres líneas: tipo de arte, pueblo y autoría. Después escribe una pregunta que le harías a la guía del museo.",
        "Tipo de arte: cerámica. Pueblo: Pueblo A. Autoría: una artesana de la comunidad. Pregunta: ¿Para qué se usa la vasija en la comunidad?",
        ["escribe tipo de arte", "escribe pueblo", "escribe autoría", "escribe una pregunta respetuosa"],
        ["tres líneas y una pregunta"],
        ["inventar un pueblo", "olvidar la autoría"],
        "Reconoce que copió los datos de la ficha sin agregar otros. Recuérdale que la ficha pedía no tocar la vasija.",
    ),
    reinforce="Mira un objeto hecho a mano en tu casa y anota qué es y quién lo hizo, si lo sabes.",
    extend="Dibuja una vitrina de museo con tres objetos de arte y escribe la ficha de uno de ellos.",
)

register(
    OA17, 2,
    materials="Este cuaderno, lápices de colores o grafito. Los diseños de práctica son inventados y no pertenecen a ningún pueblo.",
    use="Aprenderé que en el arte indígena los diseños tienen significados, y que ese significado lo explica la comunidad. Sirve para no inventar sentidos ni copiar símbolos sin permiso.",
    prior=["Sé anotar tipo de arte, pueblo y autoría.", "Sé que algunos saberes se piden con permiso."],
    explain=[
        "En el arte indígena los colores, las líneas y las figuras pueden tener un significado para la comunidad que los crea. Una convención es un acuerdo sobre lo que algo significa. Por ejemplo, en el curso podrían acordar que una línea ondulada quiere decir «agua». Ese acuerdo vale para el curso y no para otro pueblo.",
        "Los pueblos originarios también tienen sus acuerdos, que son muy antiguos. Cada obra se hace en un momento y en un espacio: algunas se usan en una ceremonia, otras en la casa o en una fiesta. El momento y el espacio cambian el sentido de la obra. Por eso se explica con la comunidad y no por adivinanza.",
        "Algunos símbolos son restringidos: la comunidad no quiere que todos los usen. Si no estás seguro, no lo copies. Puedes pedir permiso o crear un diseño propio con tus colores y líneas, sin decir que es de un pueblo.",
    ],
    vocab=[("convención", "acuerdo sobre lo que algo significa"), ("significado", "lo que quiere decir una figura o un color"), ("símbolo", "figura que representa una idea"), ("momento", "cuándo se usa o se hace una obra"), ("espacio", "lugar donde se usa o se muestra una obra")],
    worked=[
        {"title": "Una convención del curso", "problem": "En tu curso acuerdan que una línea ondulada quiere decir «agua» y un círculo, «sol». Ves un dibujo con un círculo arriba y una línea ondulada abajo. ¿Qué dice según el acuerdo?", "steps": ["El círculo es «sol».", "La línea ondulada es «agua».", "Arriba está el sol y abajo el agua."], "answer": "El sol arriba y el agua abajo"},
        {"title": "El significado lo da la comunidad", "problem": "Un niño cree que una figura de un tejido significa «felicidad» porque a él le parece alegre. ¿Cómo puede saber el significado real?", "steps": ["Su idea es una suposición.", "El significado lo da la comunidad que hizo el tejido.", "Debe preguntar a la persona que lo creó."], "answer": "Preguntando a la comunidad o a quien creó el tejido"},
    ],
    mistakes=[
        {"wrong": "Decir qué significa un símbolo de otro pueblo sin haberlo preguntado.", "why": "Un significado adivinado puede ser falso.", "fix": "Pregunta a la comunidad o a quien lo hizo."},
        {"wrong": "Copiar un símbolo restringido porque se ve bonito.", "why": "La comunidad puede no querer que todos lo usen.", "fix": "No lo copies, pide permiso o crea un diseño propio."},
    ],
    tiers={
        "recovery": [
            ex("En el curso acuerdan que un triángulo quiere decir «montaña». Si dibujas un triángulo, ¿qué quieres decir?", "Montaña", "Así fue el acuerdo."),
            ex("Una convención es un acuerdo sobre lo que algo significa. Si acuerdas con un amigo que una estrella dibujada es «amigos», ¿es una convención?", "Sí", "Es un acuerdo sobre el significado."),
            ex("Un símbolo restringido es uno que la comunidad no quiere que todos usen. ¿Debes copiarlo sin preguntar?", "No", "Hay que pedir permiso o no copiarlo."),
        ],
        "understand": [
            ex("Acuerdo del curso: círculo es «sol», línea ondulada es «agua», triángulo es «montaña». Un dibujo tiene un triángulo y una línea ondulada. ¿Qué dos cosas dice?", "Montaña y agua", "El triángulo es montaña y la línea ondulada, agua."),
            ex("Una obra se usa en una ceremonia de una comunidad y otra se usa en la casa. ¿Cambia el momento o el espacio?", "Cambian el momento y el espacio", "Una se usa en la ceremonia y otra en la casa."),
            ex("¿Quién da el significado real de un símbolo de un tejido: cualquier persona que lo mire o la comunidad que lo creó?", "La comunidad que lo creó", "Ella sabe lo que quiere decir su obra."),
        ],
        "apply": [
            ex("Con el acuerdo «círculo = sol, línea ondulada = agua, triángulo = montaña», ¿cuántos símbolos hay en «círculo, círculo, línea ondulada, triángulo»?", "4", "Se cuentan 2 círculos, 1 línea ondulada y 1 triángulo."),
            ex("Mira esta lista: «triángulo, triángulo, línea ondulada, círculo, triángulo». ¿Cuántas montañas se ven si el triángulo significa «montaña»?", "3", "Aparecen tres triángulos."),
            ex("Beto quiere copiar una figura de un tejido de una comunidad sin avisar. ¿Qué dos cosas puede hacer en vez de copiarla?", "Pedir permiso o crear un diseño propio", "Son las dos opciones respetuosas."),
        ],
        "reason": [
            ex("Ema inventó que un símbolo de un tejido significa «tristeza» porque es azul. ¿Por qué eso no es un dato confiable?", "Porque lo adivinó y no lo dijo la comunidad", "El significado lo da quien creó la obra."),
            ex("Dos cursos acordaron cosas distintas: en uno el círculo es «sol», en otro es «luna». ¿Por qué ambos pueden estar bien?", "Porque cada curso hizo su propio acuerdo", "Una convención vale para quien la acuerda."),
        ],
        "challenge": [
            ex("Un tejido de práctica se usa en una fiesta en la plaza. Otro igual se usa en una casa. ¿Qué dos cosas cambian: el momento y el espacio, o los colores y el hilo?", "El momento y el espacio", "La fiesta en la plaza y la casa son otros espacios y momentos."),
            ex("Creaste un diseño con tus propias figuras. ¿Puedes decir que es de un pueblo originario? Responde sí o no y por qué.", "No, porque es tu propio diseño", "No es un diseño de la comunidad."),
        ],
    },
    context=[ex("En una feria ves una figura en un tejido y piensas que es bonita para tu cuaderno. ¿Cómo actúas con respeto?", "Preguntar si puedes usarla y cómo se llama", "Pides permiso y reconoces a quien la creó.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es una convención?", "Un acuerdo sobre lo que algo significa", "Es un acuerdo."),
        ex("¿Quién explica el significado de un símbolo de un pueblo?", "La comunidad", "Ella sabe lo que quiere decir su obra."),
        ex("¿Qué haces con un símbolo restringido?", "No lo copio", "No se usa sin permiso."),
    ],
    open_task=task(
        "Con tu familia o con un compañero acuerden una convención con estas cuatro figuras ya dadas: círculo, línea ondulada, triángulo y cuadrado. Escriban qué significará cada una (por ejemplo «sol», «agua», «montaña», «casa»). Luego dibuja un diseño de seis figuras con tu convención. Escribe una frase: «Este diseño es mío y no pertenece a ningún pueblo».",
        "Círculo es sol, línea ondulada es agua, triángulo es montaña, cuadrado es casa. Diseño: círculo, línea ondulada, triángulo, triángulo, cuadrado, línea ondulada. Este diseño es mío y no pertenece a ningún pueblo.",
        ["escribe significado para las cuatro figuras", "dibuja seis figuras", "escribe la frase de autoría propia", "no copia símbolos de un pueblo"],
        ["lista de la convención", "diseño dibujado"],
        ["copiar figuras de un tejido de una comunidad", "decir que el diseño es de un pueblo"],
        "Reconoce que su convención es propia y válida para su grupo. Recuérdale que los símbolos de un pueblo los explica la comunidad.",
    ),
    reinforce="Inventa un acuerdo de dos figuras y explícalo a alguien de tu casa.",
    extend="Compara dos dibujos tuyos y di qué cambia si se muestran en la casa o en la escuela.",
)

register(
    OA17, 3,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé que el arte indígena se sigue haciendo hoy, que sus artistas son personas de ahora y que hay que reconocer su autoría. Sirve para respetar a los artistas vivos y su trabajo.",
    prior=["Sé que el saber está vivo.", "Sé quién es la autoría de una obra."],
    explain=[
        "El arte de los pueblos originarios no es solo de museos. Hoy hay artistas de esos pueblos que tejen, hacen cerámica, esculpen, cantan y bailan. Algunos usan técnicas muy antiguas y otros mezclan técnicas antiguas con materiales nuevos. Cuando una obra cambia, sigue siendo suya si la hace la comunidad o su artista.",
        "La autoría es quién creó una obra. Si una artista hace un tejido, su nombre debe aparecer cuando se muestra. Algunas obras pertenecen a toda una comunidad y no a una sola persona; en ese caso se nombra a la comunidad. Mostrar el nombre es una forma de respeto.",
        "Cuando compras o ves una obra, puedes preguntar por la autoría. Si quieres usarla en un trabajo escolar, pide permiso y escribe la fuente. No la presentes como tuya ni la vendas sin acuerdo de su autora.",
    ],
    vocab=[("artista", "persona que crea obras de arte"), ("autoría", "quién creó una obra"), ("técnica", "forma de hacer una obra"), ("comunidad", "grupo de personas que viven y trabajan juntas"), ("fuente", "dato de dónde viene la obra o la idea")],
    worked=[
        {"title": "Arte de hoy", "problem": "Una artesana de un pueblo originario teje hoy con una técnica antigua de su comunidad, pero usa lana de colores nuevos. ¿Sigue siendo arte de su pueblo?", "steps": ["Usa una técnica que viene de su pueblo.", "Cambió el color de la lana.", "La obra la hace ella, que es parte de su pueblo, así que sigue siendo suya."], "answer": "Sí, sigue siendo suya porque la hace su artista con una técnica de su pueblo"},
        {"title": "Citar la autoría", "problem": "Quieres mostrar en clase una foto del cuaderno de tu vecina Rosa, que dibuja diseños propios. ¿Qué haces antes y qué dices al mostrarla?", "steps": ["Antes le pido permiso a Rosa.", "Al mostrarla digo: «Este diseño es de Rosa, con su permiso»."], "answer": "Pido permiso y digo que el diseño es de Rosa"},
    ],
    mistakes=[
        {"wrong": "Mostrar la obra de una artista sin decir su nombre.", "why": "La autoría es parte de la obra.", "fix": "Escribe el nombre de la artista y la fuente."},
        {"wrong": "Pensar que si una obra cambia ya no es de su pueblo.", "why": "El arte vivo puede cambiar y seguir siendo de su pueblo.", "fix": "Pregunta a la comunidad o a quien la hizo."},
    ],
    tiers={
        "recovery": [
            ex("¿Hoy hay artistas de pueblos originarios que crean obras?", "Sí", "Hay personas que tejen, esculpen, cantan y bailan hoy."),
            ex("La autoría es quién creó una obra. Si Rosa hizo un dibujo, ¿quién tiene la autoría?", "Rosa", "Ella lo creó."),
            ex("Al mostrar la obra de una artista, ¿debes decir su nombre o no decirlo?", "Decir su nombre", "Mostrar su nombre es una forma de respeto."),
        ],
        "understand": [
            ex("Una artista usa una técnica antigua y lana nueva. ¿Qué cambió: la técnica o el material?", "El material", "La lana nueva es el cambio; la técnica es antigua."),
            ex("Una obra la hizo toda una comunidad entre muchas personas. ¿A quién se nombra como autoría?", "A la comunidad", "Fue hecha entre todos."),
            ex("¿Por qué no se debe presentar la obra de otra persona como propia?", "Porque no es tuya y no respetas a su autora", "Sería quitarle el reconocimiento."),
        ],
        "apply": [
            ex("Quieres mostrar el dibujo de tu vecino Luis. Ordena: a) digo su nombre, b) le pido permiso, c) muestro el dibujo. Escribe las letras en orden.", "b, c, a", "Primero se pide permiso, luego se muestra y se dice su nombre."),
            arith("Una feria tiene 4 puestos de textiles con 6 tejidos cada uno. ¿Cuántos tejidos hay en total?", "4*6", "Se suman 6 tejidos cuatro veces."),
            ex("En una ficha dice: «Tejido de la comunidad de un pueblo del norte, hecho por Doña Elena». ¿Quién es la autora?", "Doña Elena", "La ficha dice que lo hizo ella."),
        ],
        "reason": [
            ex("Pedro dijo que una cerámica nueva «ya no es de su pueblo» porque tiene un color nuevo. ¿Por qué es una idea débil?", "Porque el arte vivo cambia y sigue siendo de quien lo crea", "Una obra puede cambiar y mantener su origen."),
            ex("Una niña usó un diseño de una artista en un afiche escolar y escribió «idea de la artista X, con su permiso». ¿Qué hizo bien?", "Pidió permiso y dijo la autoría", "Reconoció a la artista y pidió permiso."),
        ],
        "challenge": [
            ex("Lee: «Doña Elena enseñó a su nieta a hilar. La nieta hizo una bufanda y dijo: Esto lo hice yo, pero lo aprendí con mi abuela Elena». ¿Qué parte es de la nieta y qué parte de la abuela?", "La bufanda es de la nieta; el aprendizaje, de la abuela", "La nieta hizo la obra y reconoció a quien le enseñó."),
            ex("En un colegio se vende un tejido hecho por un curso, usando un diseño que enseñó una artesana, sin avisarle. ¿Qué debieron hacer antes?", "Pedir permiso y reconocer su autoría", "El diseño es de la artesana."),
        ],
    },
    context=[ex("En una feria, una vendedora te muestra un tejido. ¿Qué pregunta hace que conozcas el arte con respeto?", "¿Quién lo hizo y de qué pueblo es?", "Pregunta por la autoría y el pueblo.")],
    selfcheck=[
        ex("¿Qué es una técnica?", "Una forma de hacer una obra", "Cómo se hace algo."),
        ex("¿Qué haces antes de mostrar la obra de otra persona?", "Pedir permiso", "Ella decide si se muestra."),
        ex("¿Una obra con material nuevo puede ser de un pueblo originario?", "Sí", "El arte vivo cambia."),
    ],
    open_task=task(
        "Observa esta ficha inventada: «Obra: bufanda tejida. Artista: Doña Elena, de una comunidad del norte. Técnica: hilado a mano. Material: lana. Fecha: este año». Escribe un cartel de museo de tres líneas con el nombre de la obra, la autoría y la técnica. Después escribe qué permiso pedirías si quisieras mostrarla en tu curso.",
        "Bufanda tejida. Autoría: Doña Elena, de una comunidad del norte. Técnica: hilado a mano. Pediría permiso a Doña Elena para mostrarla en mi curso.",
        ["escribe nombre de la obra", "escribe la autoría", "escribe la técnica", "dice que pide permiso a la artista"],
        ["cartel de tres líneas", "frase de permiso"],
        ["olvidar la autoría", "decir que es una obra del pasado"],
        "Reconoce el cartel completo y felicítale por dar la autoría. Doña Elena es un personaje inventado.",
    ),
    reinforce="Pregunta en tu casa quién hizo un objeto hecho a mano y anota su nombre.",
    extend="Haz un cartel de museo para un dibujo tuyo con título, autoría y fecha.",
)

register(
    OA17, 4,
    materials="Este cuaderno, lápices de colores o grafito.",
    use="Aprenderé a crear un diseño propio sin copiar símbolos de un pueblo, y a agradecer y reconocer a las personas que me enseñan. Sirve para hacer arte con respeto.",
    prior=["Sé que hay símbolos restringidos.", "Sé que la autoría se reconoce."],
    explain=[
        "Puedes inspirarte en el arte indígena sin copiarlo. Inspirarte es mirar y pensar en una idea y después crear algo tuyo. Copiar es hacer igual un diseño o un símbolo de otra persona. Si copias un símbolo de una comunidad, puedes dañar algo que para ella es importante.",
        "Para crear con respeto sigue tres reglas. Primera: pide permiso si vas a usar algo de una comunidad. Segunda: reconoce y nombra a quien te enseñó. Tercera: haz tu propio diseño, con tus figuras, sin decir que es de un pueblo. Así valoras el arte sin quitárselo a nadie.",
        "También puedes devolver. Puedes agradecer a la artista con una carta, invitarla a mostrar su obra en el curso si ella quiere, o cuidar su trabajo al exponerlo. Devolver es parte de aprender de otra persona.",
    ],
    vocab=[("inspirarse", "mirar una idea y crear algo propio"), ("copiar", "hacer igual la obra de otra persona"), ("reconocer", "decir quién hizo algo"), ("agradecer", "decir que se valora lo recibido"), ("propio", "que es tuyo")],
    worked=[
        {"title": "Inspirarse sin copiar", "problem": "Viste un tejido con muchas líneas rectas de colores. Quieres hacer un dibujo. ¿Qué haces para inspirarte sin copiar?", "steps": ["Pienso en la idea: líneas y colores.", "Dibujo mis propias líneas, con mis colores y mi orden.", "No digo que es de un pueblo."], "answer": "Hago un diseño propio con mis líneas y colores, sin decir que es de un pueblo"},
        {"title": "Agradecer a quien enseñó", "problem": "Una artesana vino a tu curso a mostrar su trabajo. ¿Qué dos acciones sirven para agradecer?", "steps": ["Escribimos una carta de agradecimiento.", "Decimos su nombre cuando contamos lo que aprendimos."], "answer": "Escribir una carta y nombrarla cuando contamos lo que aprendimos"},
    ],
    mistakes=[
        {"wrong": "Copiar el dibujo de un tejido y decir «es mío».", "why": "No lo creaste y pasas por encima de la autoría.", "fix": "Haz tu propio diseño y nombra a quien te inspiró, si pidió que se la nombrara."},
        {"wrong": "Decir «mi diseño es de un pueblo originario» solo porque se parece.", "why": "Un diseño propio no pertenece a ningún pueblo.", "fix": "Di «mi diseño propio, inspirado en una visita»."},
    ],
    tiers={
        "recovery": [
            ex("Si miras un tejido y haces un dibujo con tus propias líneas, ¿te inspiraste o copiaste?", "Me inspiré", "Creaste algo propio."),
            ex("Si copias exacto el símbolo de una comunidad, ¿respetas su trabajo?", "No", "Copiar sin permiso no respeta su trabajo."),
            ex("Una artista vino a tu curso. ¿Qué es una forma de agradecer: una carta o romper su obra?", "Una carta", "La carta muestra que valoras su visita."),
        ],
        "understand": [
            ex("Las tres reglas son: pedir permiso, reconocer a quien enseñó y hacer un diseño propio. ¿Cuántas reglas son?", "3", "Se cuentan tres reglas."),
            ex("Beto hizo un dibujo propio con triángulos de colores. ¿Puede decir que es un diseño de un pueblo originario?", "No", "Es su propio diseño."),
            ex("¿Para qué sirve reconocer a quien te enseñó?", "Para mostrar respeto y decir de dónde viene lo que aprendiste", "Reconocer es decir quién enseñó."),
        ],
        "apply": [
            ex("Elige la idea más respetuosa: a) copiar el símbolo de un tejido, b) dibujar tus propias figuras después de ver una exposición. Responde con la letra.", "b", "Es un diseño propio y no copia."),
            arith("Un curso de 30 estudiantes agradece a una artista con una carta por cada 5 estudiantes. ¿Cuántas cartas son?", "30//5", "Se reparten 30 estudiantes en grupos de 5."),
            ex("Escribe una frase para poner bajo tu dibujo propio. Debe decir que es tuyo y que no es de un pueblo. Elige entre: a) «Diseño propio, no pertenece a ningún pueblo» o b) «Diseño de un pueblo». Letra:", "a", "Dice que es propio."),
        ],
        "reason": [
            ex("Mía copió el símbolo de un tejido «porque se veía lindo». ¿Qué debió hacer?", "Pedir permiso o hacer un diseño propio", "Son las opciones respetuosas."),
            ex("Una niña dibujó un diseño propio y escribió: «inspirado en la visita de la artesana Elena». ¿Cumplió las reglas?", "Sí", "Hizo algo propio y reconoció su inspiración."),
        ],
        "challenge": [
            ex("Tres compañeros: Ana copió un símbolo, Lía hizo un diseño propio y Teo hizo un diseño propio y agradeció a la artista. ¿Quién cumplió mejor las tres reglas?", "Teo", "Hizo algo propio y reconoció a quien enseñó."),
            ex("Una profesora quiere exponer los trabajos del curso. ¿Qué dos datos debe poner en cada cartel para ser respetuosa?", "Quién hizo el diseño y que es un diseño propio", "Dice la autoría y evita atribuirlo a un pueblo."),
        ],
    },
    context=[ex("Quieres regalar a tu abuela una tarjeta con un diseño tomado de una artesana que conociste. ¿Qué haces primero?", "Pedirle permiso a la artesana o hacer un diseño propio", "Son las formas respetuosas.")],
    selfcheck=[
        ex("¿Qué es inspirarse?", "Mirar una idea y crear algo propio", "Es crear algo propio."),
        ex("¿Qué haces con un símbolo que no sabes si puedes usar?", "No lo copio y pregunto", "Se pregunta y no se copia."),
        ex("¿Cómo puedes agradecer a una artista?", "Con una carta o diciendo su nombre", "Son formas de reconocer."),
    ],
    open_task=task(
        "Mira esta descripción de una visita inventada: «Doña Nora, artesana, mostró un tejido de líneas rojas y azules». Crea un dibujo propio con líneas de otros dos colores que tú elijas de tu caja de lápices (por ejemplo verde y amarillo), sin copiar el orden de Doña Nora. Escribe dos frases: una que diga que el diseño es propio y otra de agradecimiento para ella.",
        "Hice un dibujo de líneas verdes y amarillas en un orden distinto. Frases: «Este diseño es propio y no pertenece a ningún pueblo». «Gracias, Doña Nora, por mostrarnos su trabajo».",
        ["crea un diseño con colores distintos", "escribe una frase de diseño propio", "escribe una frase de agradecimiento"],
        ["dibujo", "dos frases"],
        ["copiar el orden del tejido", "decir que su diseño es de un pueblo"],
        "Reconoce el diseño propio y la frase de agradecimiento. Doña Nora es un personaje inventado.",
    ),
    reinforce="Haz un dibujo de 5 líneas de colores y escribe debajo «diseño propio».",
    extend="Escribe una carta corta de agradecimiento a alguien que te enseñó algo.",
)

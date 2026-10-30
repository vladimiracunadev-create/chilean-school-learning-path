"""Material del estudiante de 2.º básico, Historia, Geografía y Ciencias Sociales: OA 02 (continuidades y cambios en pueblos indígenas actuales)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA = "HI02 OA 02"

# ---------------------------------------------------------------- clase 1
FUE = ("Fuentes de ejemplo creadas para esta clase: A) objeto de telar encontrado en un museo, de hace 600 años. B) fotografía de una escuela con niños, de hace 5 años. "
       "C) dibujo de un viajero, de hace 150 años. En todas se habla de personas de un mismo pueblo, el mapuche.")
register(
    OA, 1,
    materials="Lápiz y papel. Las fuentes de ejemplo están escritas en cada ejercicio.",
    use="Aprenderé a ordenar fuentes del pasado y del presente de un mismo pueblo. Sirve para ver que los pueblos originarios tienen una historia larga y que siguen presentes.",
    prior=["Sé qué es el periodo precolombino.", "Sé comparar números: mayor y menor."],
    explain=[
        "Un mismo pueblo puede aparecer en fuentes de épocas distintas. Hay fuentes del tiempo precolombino, como objetos antiguos, y fuentes del presente, como fotografías o testimonios de hoy. Las dos nos enseñan cosas distintas.",
        "Para ordenar fuentes, miramos cuánto tiempo hace que se hicieron. Una fuente de hace 600 años es más antigua que una de hace 150 años. Cuando el número de años es mayor, la fuente es más antigua. Una fuente de hace 5 años es la más reciente.",
        "Los pueblos mapuche, aimara y rapa nui existieron antes de la llegada de los españoles y existen hoy. Cuando comparamos el pasado con el presente, no juzgamos si una fuente es más auténtica que otra. Solo vemos qué muestra cada una, de cuándo es y de quién habla.",
    ],
    vocab=[("fuente", "algo que da información sobre el pasado o el presente"), ("antiguo", "que existe desde hace mucho tiempo"), ("reciente", "que ocurrió hace poco tiempo"), ("presente", "el tiempo en que vivimos ahora"), ("época", "periodo de la historia")],
    worked=[
        {"title": "Ordenar por antigüedad", "problem": f"{FUE} ¿Cuál es la fuente más antigua?", "steps": ["Miro los años: 600, 5 y 150.", "El número mayor es 600, que es más antiguo."], "answer": "La fuente A, el objeto de telar"},
        {"title": "Pasado o presente", "problem": f"{FUE} ¿Cuál fuente es del presente?", "steps": ["El presente es el tiempo de ahora.", "La fuente de hace 5 años es la más reciente."], "answer": "La fuente B, la fotografía"},
    ],
    mistakes=[
        {"wrong": "Pensar que la fuente con el número más chico es la más antigua.", "why": "Se confunde «hace cuántos años» con «el año».", "fix": "Entre más años hace, más antigua es la fuente. Hace 600 años es más antiguo que hace 5."},
        {"wrong": "Decir que solo la fuente antigua muestra al pueblo «verdadero».", "why": "Se piensa que el pasado es más auténtico.", "fix": "Cada fuente muestra al pueblo en su época. Las dos son válidas."},
    ],
    tiers={
        "recovery": [
            ex(f"{FUE} ¿La fuente B es del pasado lejano o del presente?", "del presente", "Tiene solo 5 años."),
            ex("Entre «hace 600 años» y «hace 150 años», ¿qué es más antiguo?", "hace 600 años", "600 es mayor que 150."),
            ex("¿El pueblo mapuche existía antes de los españoles y existe hoy?", "sí", "Es un pueblo con una historia larga que sigue vivo."),
        ],
        "understand": [
            ex(f"{FUE} Ordena las fuentes de la más antigua a la más reciente.", "A, C, B", "Hace 600, hace 150 y hace 5 años, en ese orden."),
            ex(f"{FUE} ¿Qué muestra la fuente B?", "una escuela con niños de hoy", "Es una fotografía de una escuela de hace 5 años."),
            ex("¿Qué significa «reciente»?", "que ocurrió hace poco", "Reciente es lo que pasó hace poco."),
        ],
        "apply": [
            ex(f"{FUE} ¿Qué fuente es más antigua: C o B?", "C", "Hace 150 años es mayor que hace 5."),
            ex("Ordena de más antigua a más reciente: hace 20 años, hace 400 años, hace 90 años.", "hace 400 años, hace 90 años, hace 20 años", "Se ordenan de mayor a menor número de años."),
            ex(f"{FUE} ¿Cuál de las fuentes es probable que muestre vida precolombina: A o B?", "A", "Hace 600 años es mucho antes de la llegada de los españoles."),
        ],
        "reason": [
            ex("Daniela dice: «La fotografía de hoy no sirve porque no es antigua». ¿Qué respondes?", "Sirve porque muestra cómo vive el pueblo hoy", "El presente también es historia del pueblo."),
            ex("Un compañero dice: «Como el telar es muy antiguo, el pueblo mapuche desapareció». ¿Es correcto?", "No; la fotografía de hoy muestra que el pueblo existe", "Una fuente antigua no prueba que algo ya no exista."),
        ],
        "challenge": [
            ex(f"{FUE} Escribe qué fuente es del medio y explica por qué.", "C, porque hace 150 años queda entre 600 y 5", "150 es menor que 600 y mayor que 5."),
            ex("Una fuente nueva dice «hace 1.000 años». ¿Es más antigua que A, que dice hace 600 años?", "sí", "1.000 es mayor que 600, así que hace más tiempo."),
        ],
    },
    context=[ex("En un museo hay tres carteles: «hace 300 años», «hace 3 años» y «hace 75 años». ¿Cuál debe ir primero en una fila de la más antigua a la más reciente?", "hace 300 años", "300 es el mayor número de años.")],
    selfcheck=[
        ex("¿Una fuente de hace 10 años es antigua o reciente comparada con una de hace 500 años?", "reciente", "Hace 10 años es mucho menos tiempo."),
        ex("¿Qué es una fuente?", "algo que da información", "Una fuente informa sobre un hecho o pueblo."),
        ex("¿Los pueblos originarios existen hoy?", "sí", "Hay personas de esos pueblos en Chile hoy."),
    ],
    open_task=task(
        "Ordena en una fila tres tarjetas: tarjeta 1 «Telar de hace 500 años», tarjeta 2 «Foto de una fiesta de hace 8 años», tarjeta 3 «Dibujo de hace 120 años». Escribe un número 1, 2 o 3 en cada una según su antigüedad y una frase para decir si habla del pasado o del presente.",
        "Orden: Telar de hace 500 años (1), Dibujo de hace 120 años (2), Foto de una fiesta de hace 8 años (3). El telar es del pasado antiguo y la foto es del presente.",
        ["orden correcto por antigüedad", "una frase de pasado o presente por tarjeta", "no juzga cuál fuente es más auténtica"], ["tarjetas ordenadas", "frases escritas"], ["ordenar al revés", "decir que la foto no sirve"],
        "Pregunta cómo supo cuál era más antigua. Debe mencionar el número de años."),
    reinforce="Ordena tres fotografías de tu familia de la más antigua a la más reciente, sin mostrar a personas ni lugares privados.",
    extend="Escribe una pregunta que te gustaría hacer a una persona mapuche de hoy sobre su pueblo.",
)

# ---------------------------------------------------------------- clase 2
CON = ("Ficha de continuidades de ejemplo: el mapuzugun, idioma mapuche, y el aimara se siguen hablando hoy y también se enseñan en algunas escuelas. "
       "Los telares mapuche y aimara se siguen usando para hacer tejidos. Cerca del 21 de junio, el pueblo mapuche celebra el We Tripantu y el pueblo aimara celebra el Año Nuevo Andino. "
       "En Rapa Nui se mantiene el idioma rapa nui y se celebra la fiesta Tapati en febrero. "
       "Los mapuche siguen haciendo el ngillatun, una ceremonia para agradecer a la naturaleza. En el altiplano se sigue comiendo quinua.")
register(
    OA, 2,
    materials="Lápiz y papel. La ficha de continuidades está escrita en cada ejercicio.",
    use="Aprenderé qué costumbres de los pueblos originarios se mantienen hasta hoy, aunque hayan cambiado un poco. Sirve para entender que su cultura sigue viva.",
    prior=["Sé que hay pueblos mapuche, aimara y rapa nui.", "Sé qué es una fuente."],
    explain=[
        "Una continuidad es algo que se mantiene a través del tiempo. Muchos pueblos originarios han mantenido su idioma, sus tejidos y sus celebraciones durante siglos. Por eso decimos que su cultura sigue viva.",
        "Hoy el idioma mapuzugun, el idioma aimara y el idioma rapa nui se siguen hablando. Los telares se siguen usando para tejer. Cerca del 21 de junio el pueblo mapuche celebra el We Tripantu y el pueblo aimara celebra el Año Nuevo Andino. En Rapa Nui se celebra la fiesta Tapati en febrero. Los mapuche siguen haciendo el ngillatun, una ceremonia para agradecer a la naturaleza, y en el altiplano se sigue comiendo quinua.",
        "Una continuidad no significa que todo sea igual al pasado. Un idioma puede enseñarse hoy en una escuela. Un tejido puede hacerse con lanas nuevas. Una celebración puede cambiar un poco. Por eso hay que usar frases cuidadosas: «se mantiene», no «todo sigue igual».",
    ],
    vocab=[("continuidad", "algo que se mantiene a través del tiempo"), ("tradición", "costumbre que pasa de generación en generación"), ("idioma", "lengua que habla un pueblo"), ("celebración", "fiesta o ceremonia de un grupo"), ("transformación", "cambio en la forma de algo")],
    worked=[
        {"title": "Encontrar una continuidad", "problem": f"{CON} Nombra una continuidad del pueblo rapa nui.", "steps": ["Busco Rapa Nui en la ficha.", "Dice que se mantiene el idioma rapa nui y se celebra la fiesta Tapati."], "answer": "El idioma rapa nui o la fiesta Tapati"},
        {"title": "Frase cuidadosa", "problem": "¿Qué frase es más cuidadosa: «El tejido mapuche sigue igual que hace 500 años» o «El tejido mapuche se mantiene, aunque cambian algunos materiales»?", "steps": ["La primera dice que nada cambió, lo que es difícil de probar.", "La segunda reconoce que hay continuidad y cambio."], "answer": "La segunda"},
    ],
    mistakes=[
        {"wrong": "Decir que todo sigue igual que en el pasado.", "why": "Se piensa que una cultura no puede cambiar.", "fix": "Di «se mantiene» y agrega si algo cambió."},
        {"wrong": "Decir que los idiomas originarios ya no se hablan.", "why": "No se mira el presente.", "fix": "Lee la ficha: hoy se siguen hablando y se enseñan en algunas escuelas."},
    ],
    tiers={
        "recovery": [
            ex(f"{CON} ¿Qué pueblo celebra el We Tripantu?", "el pueblo mapuche", "La ficha lo indica."),
            ex(f"{CON} ¿Qué pueblo celebra la fiesta Tapati en febrero?", "el pueblo rapa nui", "La ficha lo dice."),
            ex("Una continuidad, ¿es algo que se mantiene o algo que desaparece?", "algo que se mantiene", "Continuidad significa que sigue en el tiempo."),
        ],
        "understand": [
            ex(f"{CON} ¿Qué idiomas se siguen hablando hoy según la ficha?", "mapuzugun, aimara y rapa nui", "La ficha cita los tres."),
            ex(f"{CON} ¿Para qué se siguen usando los telares?", "para hacer tejidos", "La ficha dice que se usan para tejer."),
            ex(f"{CON} ¿Qué alimento del altiplano se sigue comiendo hoy, según la ficha?", "la quinua", "La ficha lo indica."),
        ],
        "apply": [
            ex(f"{CON} Escribe una continuidad que sea una celebración.", "We Tripantu, Año Nuevo Andino o Tapati", "Las tres son celebraciones de la ficha."),
            ex(f"{CON} ¿Qué ceremonia mapuche se sigue haciendo hoy, según la ficha?", "el ngillatun", "La ficha dice que los mapuche siguen haciendo el ngillatun."),
            ex("Completa: «El tejido se mantiene, aunque ___ algunos materiales». Elige: A) cambian, B) desaparecen todos.", "A", "Hay continuidad con cambios pequeños."),
        ],
        "reason": [
            ex("Sofía dice: «Si una celebración cambia un poco, ya no es la misma». ¿Qué puedes responder?", "Puede mantenerse aunque cambie un poco", "Las tradiciones se transforman y siguen."),
            ex(f"{CON} ¿Por qué es mejor decir «el idioma se mantiene» que «todo sigue igual»?", "Porque habla de una continuidad sin negar los cambios", "Es una frase más precisa."),
        ],
        "challenge": [
            ex(f"{CON} Escribe una frase cuidadosa sobre el tejido.", "Los telares se siguen usando para tejer, aunque pueden usarse materiales nuevos", "Combina continuidad y posible cambio."),
            ex("¿Qué dos pueblos celebran algo cerca del 21 de junio, según la ficha?", "el mapuche y el aimara", "El We Tripantu y el Año Nuevo Andino."),
        ],
    },
    context=[ex("En una escuela de una región del norte, un profesor enseña palabras en aimara a su curso. ¿Qué continuidad muestra esta situación?", "que el idioma aimara se mantiene y se enseña", "La ficha dice que algunas escuelas lo enseñan.")],
    selfcheck=[
        ex("¿Qué pueblo celebra el Año Nuevo Andino?", "el pueblo aimara", "La ficha lo indica."),
        ex("¿Qué es una tradición?", "una costumbre que pasa de generación en generación", "Se transmite entre generaciones."),
        ex("¿Una continuidad significa que no cambió nada?", "no", "Puede cambiar un poco y mantenerse."),
    ],
    open_task=task(
        f"Elige una continuidad de la ficha y dibújala. {CON} Debajo escribe: de qué pueblo es, qué se mantiene y una frase con «se mantiene» (no «todo sigue igual»).",
        "Dibujo de un telar. Pueblo: mapuche. Se mantiene el uso del telar para hacer tejidos. Frase: El telar mapuche se mantiene hasta hoy.",
        ["continuidad de la ficha", "pueblo correcto", "frase cuidadosa"], ["dibujo", "frase escrita"], ["decir que todo sigue igual", "mezclar pueblos"],
        "Pide que explique qué podría haber cambiado aunque la tradición se mantenga."),
    reinforce="Di en voz alta dos continuidades de pueblos originarios y a qué pueblo pertenecen.",
    extend="Escribe una pregunta que le harías a alguien que celebra el We Tripantu o el Año Nuevo Andino.",
)

# ---------------------------------------------------------------- clase 3
CAM = ("Ficha de cambios de ejemplo: antes de la llegada de los españoles, la vivienda mapuche tradicional era la ruka de madera y paja. Hoy muchas familias mapuche viven en casas de material sólido y en ciudades, y la ruka se usa también para reuniones y ceremonias. "
       "Para viajar, los pueblos andinos caminaban y cargaban en llamas. Los caballos llegaron con los españoles. Hoy muchas personas usan bus, auto y bicicleta.")
register(
    OA, 3,
    materials="Lápiz y papel. La ficha de cambios está escrita en cada ejercicio.",
    use="Aprenderé a describir un cambio y a pensar por qué pudo ocurrir. Sirve para entender que las culturas cambian y que explicar es distinto de mostrar la evidencia.",
    prior=["Sé qué es una continuidad.", "Sé qué es una fuente."],
    explain=[
        "Un cambio es algo que ya no es igual que antes. Las viviendas y los transportes de los pueblos originarios cambiaron con el tiempo. Muchas familias mapuche viven hoy en casas de material sólido, y la ruka se usa también para reuniones y ceremonias.",
        "Los pueblos andinos viajaban a pie y cargaban en llamas. Los caballos llegaron con los españoles. Hoy se usan buses, autos y bicicletas. Estos son cambios, y cada uno pudo ocurrir por razones distintas, como la llegada de nuevos animales, el uso de materiales nuevos o el vivir en ciudades.",
        "Hay que separar dos cosas. La evidencia es lo que muestra una fuente: por ejemplo, «llegaron caballos con los españoles». Una explicación posible es una idea sobre el porqué: «tal vez se usó el caballo porque era más rápido». Una explicación posible necesita más fuentes para confirmarse.",
    ],
    vocab=[("cambio", "algo que ya no es igual que antes"), ("evidencia", "lo que muestra una fuente"), ("explicación posible", "idea sobre el porqué, que aún debe comprobarse"), ("transporte", "forma de llevar personas o cosas de un lugar a otro"), ("material sólido", "material duro, como ladrillo o cemento")],
    worked=[
        {"title": "Describir un cambio", "problem": f"{CAM} Describe un cambio en la vivienda mapuche.", "steps": ["Antes: la ruka de madera y paja.", "Hoy: muchas familias viven en casas de material sólido."], "answer": "Antes vivían en ruka; hoy muchas familias viven en casas de material sólido"},
        {"title": "Evidencia o explicación", "problem": "«Llegaron caballos con los españoles» y «Tal vez los caballos se usaron porque eran rápidos». ¿Cuál es evidencia?", "steps": ["La primera se apoya en la ficha.", "La segunda comienza con tal vez, así que es una idea."], "answer": "La primera es evidencia; la segunda es una explicación posible"},
    ],
    mistakes=[
        {"wrong": "Decir que si algo cambió, el pueblo dejó de ser quien era.", "why": "Se confunde cambio con desaparición.", "fix": "Las personas pueden cambiar su casa y seguir siendo parte de su pueblo."},
        {"wrong": "Escribir una explicación como si fuera un hecho seguro.", "why": "No se separa evidencia de idea.", "fix": "Usa «tal vez» o «posiblemente» para las explicaciones."},
    ],
    tiers={
        "recovery": [
            ex(f"{CAM} ¿Qué vivienda mapuche tradicional se menciona?", "la ruka", "La ficha habla de la ruka de madera y paja."),
            ex(f"{CAM} ¿Con qué llegaron los caballos a Chile?", "con los españoles", "La ficha lo indica."),
            ex("Un cambio, ¿es algo que sigue igual o algo que ya no es igual?", "algo que ya no es igual", "Eso significa cambio."),
        ],
        "understand": [
            ex(f"{CAM} ¿En qué cargaban sus cosas los pueblos andinos?", "en llamas", "La ficha cita las llamas."),
            ex(f"{CAM} ¿Para qué se usa también la ruka hoy?", "para reuniones y ceremonias", "La ficha lo dice."),
            ex("¿Qué significa «explicación posible»?", "una idea sobre el porqué que aún debe comprobarse", "No es un hecho seguro."),
        ],
        "apply": [
            ex(f"{CAM} Escribe un cambio en el transporte.", "antes caminaban y cargaban en llamas; hoy hay bus, auto y bicicleta", "La ficha muestra ese contraste."),
            ex("Clasifica como evidencia o explicación posible: «Hoy muchas personas usan buses».", "evidencia", "Se apoya en la ficha."),
            ex("Clasifica como evidencia o explicación posible: «Tal vez las familias se mudaron a la ciudad por trabajo».", "explicación posible", "Empieza con tal vez y es una idea."),
        ],
        "reason": [
            ex("Ana dice: «Si hoy las familias viven en casas de ladrillo, ya no son mapuche». ¿Qué respondes?", "Pueden cambiar su casa y seguir siendo mapuche", "Cambiar de vivienda no cambia el pueblo."),
            ex(f"{CAM} Escribe una explicación posible del uso de caballos, usando «tal vez».", "Tal vez se usaron porque los caballos eran rápidos para viajar", "Es una idea sobre el porqué."),
        ],
        "challenge": [
            ex(f"{CAM} ¿Qué dato de la ficha NO prueba por sí solo por qué cambió la vivienda?", "Que hoy hay casas de material sólido; falta decir el motivo", "La ficha muestra el cambio, pero no da la causa."),
            ex("Para comprobar una explicación posible, ¿qué necesitamos?", "más fuentes", "Una sola idea no basta."),
        ],
    },
    context=[ex("Un museo muestra una ruka reconstruida y un cartel dice: «Hoy se usa en ceremonias». ¿Qué cambio de uso muestra este cartel?", "pasó de ser solo vivienda a usarse también en ceremonias y reuniones", "Su uso se amplió a nuevos fines.")],
    selfcheck=[
        ex("¿Los caballos existían en Chile antes de los españoles?", "no", "Los caballos llegaron con los españoles."),
        ex("En esta clase, ¿qué llamamos evidencia de un cambio?", "lo que muestra una fuente", "Se apoya en información de la fuente."),
        ex("¿«Tal vez» introduce un hecho seguro o una explicación posible?", "una explicación posible", "Tal vez indica duda."),
    ],
    open_task=task(
        f"Haz una tabla con dos columnas: antes y ahora. {CAM} Escribe en ella el cambio de la vivienda y el cambio del transporte. Después escribe una explicación posible con «tal vez» para uno de los cambios.",
        "Vivienda: antes, ruka de madera y paja; ahora, muchas casas de material sólido. Transporte: antes, caminar y llamas; ahora, bus, auto y bicicleta. Tal vez hoy se usa el bus porque llega más lejos.",
        ["dos cambios en la tabla", "columnas antes y ahora", "explicación posible con tal vez"], ["tabla escrita"], ["escribir la explicación como hecho", "decir que el pueblo desapareció"],
        "Pregunta cuál parte de la tabla es evidencia y cuál es una idea."),
    reinforce="Nombra un cambio entre la vida de hace mucho tiempo y la de hoy, y di si es evidencia o explicación.",
    extend="Piensa en otro cambio posible, como la ropa, y escríbelo con «tal vez» y una pregunta para confirmarlo.",
)

# ---------------------------------------------------------------- clase 4
TES = ("Testimonio de ejemplo creado para esta clase (no es una persona real): «Soy Rosa. Vivo en Santiago y mi familia es mapuche. Mi abuela me enseñó a decir mari mari, que es un saludo en mapuzugun. "
       "En mi casa tenemos un telar chico. Yo voy a una escuela donde aprendo mi idioma una vez por semana».")
register(
    OA, 4,
    materials="Lápiz y papel. El testimonio de ejemplo está escrito en cada ejercicio.",
    use="Aprenderé a leer el testimonio de una persona de hoy y a decir qué nos cuenta y qué no. Sirve para escuchar con respeto sin decir que una persona representa a todo su pueblo.",
    prior=["Sé qué es una fuente.", "Sé qué es una continuidad y un cambio."],
    explain=[
        "Un testimonio es lo que una persona cuenta sobre su vida. Es una fuente contemporánea porque viene de alguien que vive hoy. Nos cuenta cómo esa persona vive su cultura, pero no habla por todo su pueblo.",
        "Al leer un testimonio hacemos dos preguntas. ¿Qué sabemos? Sabemos lo que la persona dice. ¿Qué no sabemos? No sabemos si todas las personas de su pueblo viven igual. Cada persona tiene su propia perspectiva, que es su forma de ver y contar las cosas.",
        "Por ejemplo, Rosa dice que vive en Santiago, que aprendió a saludar con mari mari y que tiene un telar chico. Eso nos muestra continuidades y también un cambio, como vivir en una ciudad. No podemos decir que todas las personas mapuche viven en Santiago.",
    ],
    vocab=[("testimonio", "lo que una persona cuenta de su vida"), ("contemporáneo", "de nuestra época, de hoy"), ("perspectiva", "forma de ver y contar algo"), ("generalizar", "decir que algo es igual para todos"), ("saludo", "palabra que decimos al encontrarnos con alguien")],
    worked=[
        {"title": "Qué sabemos", "problem": f"{TES} Escribe un dato que sabemos gracias al testimonio.", "steps": ["Busco algo que Rosa dice claramente.", "Dice que vive en Santiago."], "answer": "Rosa vive en Santiago"},
        {"title": "Qué no sabemos", "problem": f"{TES} ¿Sabemos cómo viven todas las personas mapuche?", "steps": ["El testimonio es de una sola persona.", "No sabemos nada de todas las demás."], "answer": "No; solo sabemos lo que cuenta Rosa"},
    ],
    mistakes=[
        {"wrong": "Decir que Rosa representa a todo el pueblo mapuche.", "why": "Se generaliza desde una sola persona.", "fix": "Di «Rosa cuenta que...», no «todas las personas mapuche...»."},
        {"wrong": "Pensar que un testimonio de hoy no es historia.", "why": "Se piensa que solo el pasado cuenta.", "fix": "El presente también es historia y los testimonios son fuentes."},
    ],
    tiers={
        "recovery": [
            ex(f"{TES} ¿En qué ciudad vive Rosa?", "Santiago", "El testimonio lo dice."),
            ex(f"{TES} ¿Qué saludo aprendió Rosa?", "mari mari", "Es un saludo en mapuzugun."),
            ex("Un testimonio, ¿es lo que una persona cuenta de su vida o un mapa?", "lo que una persona cuenta de su vida", "Esa es su definición."),
        ],
        "understand": [
            ex(f"{TES} ¿Quién le enseñó el saludo a Rosa?", "su abuela", "El testimonio lo dice."),
            ex(f"{TES} ¿Qué aprende Rosa una vez por semana?", "su idioma", "El testimonio lo menciona."),
            ex("¿Qué significa «perspectiva»?", "la forma de ver y contar algo", "Cada persona tiene la suya."),
        ],
        "apply": [
            ex(f"{TES} Escribe dos cosas que sabemos de la vida de Rosa.", "vive en Santiago; tiene un telar chico (u otras del texto)", "Son datos que Rosa cuenta."),
            ex(f"{TES} Rosa dice que tiene un telar chico. ¿Qué continuidad muestra?", "que el telar se sigue usando", "El telar mapuche sigue presente."),
            ex(f"{TES} Rosa vive en una ciudad. ¿Qué cambio puede mostrar?", "que muchas familias mapuche viven hoy en ciudades", "Vivir en la ciudad es un cambio de lugar."),
        ],
        "reason": [
            ex("Un compañero dice: «Según Rosa, todos los mapuche viven en Santiago». ¿Qué error tiene?", "Generaliza: Rosa solo habla de ella y su familia", "Un testimonio habla de una persona."),
            ex(f"{TES} ¿Qué NO sabemos por este testimonio?", "cómo viven todas las personas mapuche", "Solo habla de Rosa."),
        ],
        "challenge": [
            ex(f"{TES} Escribe una frase cuidadosa sobre este testimonio, usando «Rosa cuenta que».", "Rosa cuenta que aprende su idioma en la escuela", "Empieza con la fuente y habla de ella."),
            ex(f"{TES} Escribe una pregunta que le harías a Rosa, que no esté respondida en su relato.", "¿Qué fiestas celebra tu familia?", "Debe ser una pregunta nueva."),
        ],
    },
    context=[ex("Un periodista lee el testimonio de una persona aimara y escribe: «Todos los aimara hacen lo mismo que ella». ¿Qué debería cambiar?", "decir que ella cuenta cómo vive, sin hablar por todos", "Un testimonio es una perspectiva.")],
    selfcheck=[
        ex("¿Qué es un testimonio?", "lo que una persona cuenta de su vida", "Es una fuente de la persona."),
        ex("¿Una fuente contemporánea es de hoy o de hace mucho?", "de hoy", "Contemporáneo significa de nuestra época."),
        ex("¿Se puede decir que una persona habla por todo su pueblo?", "no", "Cada persona tiene su perspectiva."),
    ],
    open_task=task(
        f"Lee el testimonio de Rosa y escribe tres cosas en una tabla: una que sabemos, una que no sabemos y una pregunta nueva para ella. {TES}",
        "Sabemos: Rosa vive en Santiago y aprende su idioma. No sabemos: cómo viven todos los mapuche. Pregunta: ¿qué fiestas celebran en tu familia?",
        ["un dato del testimonio", "una cosa que no se sabe", "una pregunta respetuosa"], ["tabla escrita"], ["generalizar a todo el pueblo", "inventar datos no dichos"],
        "Pregunta cómo supo que algo no se sabe. Debe decir que el testimonio habla de una sola persona."),
    reinforce="Cuenta en tres frases algo de tu vida; luego di qué no sabrías de otras personas por ese relato.",
    extend="Escribe una pregunta respetuosa para conocer mejor la perspectiva de una persona de otro pueblo.",
)

# ---------------------------------------------------------------- clase 5
TAB = ("Tabla de ejemplo, pueblo aimara. Antes: hablaban el aimara; cultivaban terrazas; criaban llamas y alpacas; viajaban a pie. "
       "Hoy: se sigue hablando el aimara; se siguen usando terrazas en algunos valles; muchas personas viven en ciudades; se usan buses y autos.")
register(
    OA, 5,
    materials="Lápiz y papel. La tabla de ejemplo está escrita en cada ejercicio.",
    use="Aprenderé a comparar antes y ahora de un pueblo, y a decir qué permanece y qué cambia. Sirve para hablar de los pueblos con respeto, sin decir que están congelados en el pasado.",
    prior=["Sé qué es una continuidad.", "Sé qué es un cambio."],
    explain=[
        "Para comparar el pasado y el presente de un pueblo podemos usar una tabla de cuatro partes: antes, ahora, qué permanece y qué cambia. Así vemos con claridad lo que sigue y lo que es distinto.",
        "En la tabla del pueblo aimara, el idioma permanece. También permanecen las terrazas en algunos valles. Cambia el lugar donde vive mucha gente, ahora en ciudades, y cambia el transporte, con buses y autos. Un pueblo puede cambiar muchas cosas y seguir siendo el mismo pueblo.",
        "Hay que cuidar las generalizaciones. Frases como «todos los aimara viven en ciudades» o «los aimara ya no cultivan» no son ciertas y no coinciden con la tabla. Usa palabras como «algunos», «muchas personas» o «en algunos valles» cuando no sabes que algo ocurre en todos los casos.",
    ],
    vocab=[("permanece", "sigue estando, no cambia"), ("comparar", "mirar dos cosas para ver en qué se parecen y en qué se diferencian"), ("generalización", "frase que dice que algo es igual para todos"), ("algunos", "no todos, solo una parte"), ("congelado", "que no cambia, como si el tiempo se hubiera detenido")],
    worked=[
        {"title": "Qué permanece", "problem": f"{TAB} Nombra una cosa que permanece.", "steps": ["Busco algo que está en antes y en hoy.", "El idioma aimara aparece en las dos partes."], "answer": "El idioma aimara"},
        {"title": "Revisar una generalización", "problem": f"{TAB} «Todos los aimara viven hoy en ciudades». ¿Es correcto?", "steps": ["La tabla dice que muchas personas viven en ciudades.", "Muchas no es todas."], "answer": "No; se debe decir muchas personas, no todas"},
    ],
    mistakes=[
        {"wrong": "Decir que un pueblo solo vive en el pasado.", "why": "Se piensa que los pueblos originarios están congelados en el tiempo.", "fix": "Revisa la columna ahora: los pueblos viven hoy."},
        {"wrong": "Usar «todos» sin tener una fuente.", "why": "Se generaliza para no mirar los datos.", "fix": "Usa «algunos» o «muchas personas»."},
    ],
    tiers={
        "recovery": [
            ex(f"{TAB} ¿Qué idioma hablaban antes y hablan hoy?", "el aimara", "La tabla lo repite en antes y ahora."),
            ex(f"{TAB} ¿Cómo viajaban antes?", "a pie", "La tabla lo dice."),
            ex("Permanece, ¿quiere decir que sigue estando o que cambió?", "que sigue estando", "Permanecer es seguir igual."),
        ],
        "understand": [
            ex(f"{TAB} ¿Qué se usa hoy para viajar?", "buses y autos", "La tabla lo dice."),
            ex(f"{TAB} ¿Qué animales criaban antes?", "llamas y alpacas", "La tabla lo indica."),
            ex("¿Por qué conviene usar la palabra «algunos»?", "Porque no todo ocurre en todos los casos", "Así se evita generalizar."),
        ],
        "apply": [
            ex(f"{TAB} Clasifica como permanece o cambia: el idioma.", "permanece", "Aparece en antes y ahora."),
            ex(f"{TAB} Clasifica como permanece o cambia: el transporte.", "cambia", "Antes a pie; ahora buses y autos."),
            ex(f"{TAB} Clasifica como permanece o cambia: vivir en ciudades.", "cambia", "Hoy muchas personas viven en ciudades."),
        ],
        "reason": [
            ex(f"{TAB} Camilo dice: «Los aimara ya no cultivan». Usa la tabla para revisar su frase.", "Incorrecta; se siguen usando terrazas en algunos valles", "La tabla muestra cultivo hoy."),
            ex("Una compañera dice: «Como cambió su transporte, ya no son aimara». ¿Qué respondes?", "Puede cambiar el transporte y seguir siendo aimara", "El idioma y otras costumbres permanecen."),
        ],
        "challenge": [
            ex(f"{TAB} Escribe una frase con «permanece» y otra con «cambia» sobre el pueblo aimara.", "El idioma permanece. El transporte cambia", "Usa datos de la tabla."),
            ex("Escribe una frase cuidadosa para hablar de dónde viven los aimara hoy.", "Algunos viven en valles y muchas personas viven en ciudades", "Usa palabras que no generalizan."),
        ],
    },
    context=[ex("En un cartel dice: «Los aimara ya no cultivan la tierra». Una guía de museo lo corrige con la tabla. ¿Qué dato de la tabla usará?", "que se siguen usando terrazas en algunos valles", "Es el dato que muestra que hoy se cultiva.")],
    selfcheck=[
        ex("¿Qué permanece según la tabla: el idioma o el transporte?", "el idioma", "El idioma se mantiene."),
        ex("¿Qué palabra evita decir que algo ocurre en todos los casos?", "algunos", "«Algunos» no generaliza."),
        ex("¿Un pueblo congelado en el pasado es una buena forma de describirlo?", "no", "Los pueblos viven en el presente."),
    ],
    open_task=task(
        f"Copia esta tabla en tu hoja con cuatro columnas: antes, ahora, permanece, cambia. {TAB} Llena la tabla con dos datos por columna y escribe una frase cuidadosa con la palabra «algunos».",
        "Antes: aimara y llamas. Ahora: aimara y buses. Permanece: idioma. Cambia: transporte. Frase: Algunas personas aimara viven hoy en ciudades.",
        ["cuatro columnas", "dos datos por columna", "frase con algunos"], ["tabla completa"], ["decir que todos viven igual", "poner el idioma como cambio"],
        "Pide que lea una frase y diga si generaliza. Si usa «todos», pregunta qué fuente lo prueba."),
    reinforce="Elige un objeto de tu casa que ha cambiado desde hace mucho y di qué permanece y qué cambió.",
    extend="Haz la misma tabla para otro pueblo de la clase 2, usando solo los datos que ya conoces.",
)

"""Material del estudiante de 2.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (patrimonio cultural) y OA 06 (planos simples)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA5, OA6 = "HI02 OA 05", "HI02 OA 06"

# ================================================================ OA 05
P1 = ("Casos de ejemplo: A) Una receta de sopaipillas que una familia prepara cada día de lluvia y que la abuela enseña a los nietos. B) Una iglesia de madera de Chiloé que la comunidad cuida y que visitan personas de muchos lugares. "
      "C) Una canción que se canta en una fiesta de un pueblo desde hace muchos años. D) Un lápiz nuevo comprado ayer.")
register(
    OA5, 1,
    materials="Lápiz y papel. Los casos de ejemplo están escritos en cada ejercicio.",
    use="Aprenderé qué es el patrimonio cultural y cómo distinguir un objeto común de algo que una comunidad valora y cuida. Sirve para reconocer lo que queremos conservar.",
    prior=["Sé qué es una tradición.", "Sé qué es una comunidad."],
    explain=[
        "El patrimonio cultural es el conjunto de cosas y costumbres que recibimos de quienes vivieron antes y que una comunidad valora, cuida y quiere transmitir. Puede ser un edificio, una fiesta, una canción, una comida, una leyenda o un idioma. Lo que se puede tocar, como un edificio, se llama tangible. Lo que no se puede tocar, como una canción o una fiesta, se llama intangible.",
        "No todo objeto es patrimonio. Un lápiz nuevo es un objeto común. En cambio, una iglesia de madera que una comunidad cuida desde hace muchos años, o una canción que se transmite en una fiesta, tienen valor para muchas personas. Para decidir, preguntamos: ¿quién lo valora?, ¿quién lo transmite? y ¿se quiere conservar?",
        "El patrimonio puede ser de una familia, de un pueblo, de una región o de todo el país. Una receta que una abuela enseña a sus nietos es un patrimonio familiar. Cuando muchas personas la comparten y la valoran, también puede ser patrimonio de la comunidad.",
    ],
    vocab=[("patrimonio", "cosas y costumbres heredadas que una comunidad valora y cuida"), ("heredar", "recibir algo de quienes vivieron antes"), ("transmitir", "pasar algo de una persona o generación a otra"), ("valorar", "darle importancia a algo"), ("conservar", "mantener algo para que no se pierda"), ("intangible", "que no se puede tocar")],
    worked=[
        {"title": "Patrimonio o no", "problem": f"{P1} ¿Es el caso D patrimonio?", "steps": ["Pregunto quién lo valora y lo transmite.", "Un lápiz nuevo no se hereda ni se transmite."], "answer": "No; es un objeto común"},
        {"title": "Quién lo valora", "problem": f"{P1} ¿Quién valora y transmite el caso A?", "steps": ["La receta la prepara una familia.", "La abuela la enseña a los nietos."], "answer": "La familia, la abuela y los nietos"},
    ],
    mistakes=[
        {"wrong": "Decir que algo es patrimonio solo porque es antiguo.", "why": "Se mira la edad y no el valor para la comunidad.", "fix": "Pregunta quién lo valora y quién lo transmite."},
        {"wrong": "Pensar que el patrimonio son solo edificios.", "why": "Se olvidan las fiestas, canciones y recetas.", "fix": "El patrimonio incluye cosas que se tocan y también costumbres que se hacen."},
    ],
    tiers={
        "recovery": [
            ex(f"{P1} ¿El caso D es un objeto común o patrimonio?", "un objeto común", "No tiene historia ni valor colectivo."),
            ex(f"{P1} ¿Qué cuida la comunidad en el caso B?", "una iglesia de madera de Chiloé", "El caso B lo dice."),
            ex("Transmitir, ¿es pasar algo a otra persona o guardarlo para siempre sin mostrarlo?", "pasar algo a otra persona o generación", "Esa es su definición."),
        ],
        "understand": [
            ex("Explica con tus palabras qué es patrimonio cultural.", "cosas y costumbres que una comunidad valora y quiere cuidar", "Esa es la idea central."),
            ex(f"{P1} ¿Qué caso es una canción de fiesta?", "el caso C", "El caso C describe la canción."),
            ex("¿Qué tres preguntas ayudan a decidir si algo es patrimonio?", "¿Quién lo valora?, ¿quién lo transmite?, ¿se quiere conservar?", "Son las preguntas de la clase."),
        ],
        "apply": [
            ex(f"{P1} Clasifica el caso A: ¿patrimonio familiar o patrimonio nacional?", "patrimonio familiar", "Lo valora y lo transmite una familia."),
            ex(f"{P1} Ordena de más cercano a la familia a más amplio: B, A.", "A, B", "La receta es familiar; la iglesia es de una comunidad."),
            ex(f"{P1} ¿Cuántos casos de los cuatro son patrimonio?", "3", "A, B y C se valoran y se transmiten."),
        ],
        "reason": [
            ex("Un niño dice: «Mi celular es nuevo y caro, así que es patrimonio». ¿Qué respondes?", "Es un objeto común; el patrimonio se hereda y una comunidad lo valora", "Que algo sea caro no lo hace patrimonio."),
            ex("Una niña dice: «Si es muy antiguo, ya es patrimonio». Da un ejemplo que muestre que no basta.", "Una piedra vieja que nadie valora no es patrimonio", "También hay que valorarlo y transmitirlo."),
        ],
        "challenge": [
            ex(f"{P1} Escribe qué caso es patrimonio tangible, que se puede tocar, y cuál es intangible.", "Tangible: la iglesia de madera. Intangible: la canción de fiesta (o la receta)", "La iglesia se puede tocar; la canción se canta."),
            ex("¿Puede una receta familiar convertirse en patrimonio de un pueblo?", "sí, si muchas personas la comparten y la valoran", "El patrimonio crece cuando es de la comunidad."),
        ],
    },
    context=[ex("En un pueblo, todos los años hacen una fiesta en una plaza con una banda y una comida típica, y los niños aprenden los bailes. ¿Qué dos acciones muestran que es patrimonio: transmitir y valorar, o comprar y botar?", "transmitir y valorar", "Enseñar a los niños y repetir cada año muestra que se valora.")],
    selfcheck=[
        ex("¿Un lápiz nuevo es patrimonio?", "no", "No se hereda ni se valora colectivamente."),
        ex("¿Qué significa conservar?", "mantener algo para que no se pierda", "Es cuidar para que dure."),
        ex("¿Una canción de fiesta puede ser patrimonio?", "sí", "Si se transmite y se valora, sí."),
    ],
    open_task=task(
        f"Haz una tabla con tres filas: receta familiar, iglesia de madera de Chiloé, canción de fiesta. En columnas escribe: quién lo valora, quién lo transmite y si se puede tocar. {P1}",
        "Receta familiar: valora la familia; la transmite la abuela; no se toca (se cocina). Iglesia: la valora la comunidad; la cuidan sus habitantes; sí se toca. Canción: la valora el pueblo; la transmiten los mayores; no se toca.",
        ["tres filas", "quién valora y quién transmite", "tangible o no"], ["tabla escrita"], ["decir que es patrimonio por ser antiguo", "dejar columnas vacías"],
        "Pregunta cuál sería un ejemplo de objeto común y por qué."),
    reinforce="Nombra dos cosas de tu casa o barrio que una familia valore y transmita, sin dar datos privados.",
    extend="Escribe una razón por la que cuidar el patrimonio ayuda a una comunidad.",
)

P2 = ("Fotografía de ejemplo: una iglesia de madera con una torre, techo de tejuelas y paredes de tablas, cerca del mar. "
      "Placa de ejemplo: «Iglesia de madera de Chiloé. Las Iglesias de Chiloé fueron declaradas Patrimonio de la Humanidad el año 2000».")
register(
    OA5, 2,
    materials="Lápiz y papel. La descripción de la fotografía y la placa están escritas en cada ejercicio.",
    use="Aprenderé a leer una fotografía y una placa de un sitio histórico y a decir solo lo que se puede comprobar. Sirve para describir el patrimonio tangible con evidencia.",
    prior=["Sé qué es el patrimonio.", "Sé qué es una fuente."],
    explain=[
        "El patrimonio tangible es el que se puede tocar: edificios, iglesias, monumentos, sitios y objetos. En Chile hay muchos, como las Iglesias de Chiloé, el barrio histórico de Valparaíso y el Parque Nacional Rapa Nui. Algunos son Patrimonio de la Humanidad, un reconocimiento mundial.",
        "Para leer una fotografía y una placa, primero observamos lo que se ve: material, forma, lugar. Luego leemos lo que dice la placa. En el ejemplo vemos una iglesia de madera con torre y techo de tejuelas, cerca del mar. La placa dice que las Iglesias de Chiloé fueron declaradas Patrimonio de la Humanidad en el año 2000.",
        "Hay que decir solo lo que sabemos. La fotografía no dice quién construyó la iglesia ni cuántos años tiene. Eso no lo sabemos con estas fuentes. Si alguien lo afirma, pedimos una fuente que lo compruebe.",
    ],
    vocab=[("tangible", "que se puede tocar"), ("monumento", "construcción o escultura que recuerda algo importante"), ("sitio histórico", "lugar donde ocurrió algo importante del pasado"), ("placa", "cartel de metal o piedra con información"), ("Patrimonio de la Humanidad", "reconocimiento mundial a un lugar muy valioso")],
    worked=[
        {"title": "Lo que se ve", "problem": f"{P2} Escribe dos cosas que se ven en la fotografía.", "steps": ["Observo la iglesia en la descripción.", "Tiene torre y techo de tejuelas."], "answer": "Torre y techo de tejuelas"},
        {"title": "Lo que no se puede afirmar", "problem": f"{P2} ¿Sabemos cuántos años tiene la iglesia?", "steps": ["Reviso la fotografía y la placa.", "Ninguna dice la edad de la iglesia."], "answer": "No; las fuentes no lo dicen"},
    ],
    mistakes=[
        {"wrong": "Decir cosas que la fotografía no muestra, como quién la construyó.", "why": "Se inventa lo que no se ve.", "fix": "Escribe solo lo que se ve o lo que dice la placa."},
        {"wrong": "Pensar que el patrimonio tangible son solo edificios.", "why": "Se olvidan sitios y monumentos.", "fix": "También son tangibles los sitios, monumentos y objetos."},
    ],
    tiers={
        "recovery": [
            ex(f"{P2} ¿De qué material es la iglesia?", "de madera", "La fotografía y la placa lo dicen."),
            ex(f"{P2} ¿Qué año se declaró a las Iglesias de Chiloé Patrimonio de la Humanidad?", "2000", "La placa lo dice."),
            ex("Tangible, ¿es lo que se puede tocar o lo que solo se puede cantar?", "lo que se puede tocar", "Esa es su definición."),
        ],
        "understand": [
            ex(f"{P2} ¿Qué dice la placa sobre las iglesias de Chiloé?", "que son Patrimonio de la Humanidad", "Así lo indica la placa."),
            ex("¿Qué es una placa?", "un cartel de metal o piedra con información", "Se pone en sitios importantes."),
            ex("Nombra dos ejemplos de patrimonio tangible de Chile.", "Iglesias de Chiloé y barrio histórico de Valparaíso", "Son construcciones y barrios que se pueden tocar."),
        ],
        "apply": [
            ex(f"{P2} Clasifica como se ve o no se sabe: «la iglesia tiene torre».", "se ve", "La fotografía muestra la torre."),
            ex(f"{P2} Clasifica como se ve o no se sabe: «la iglesia la construyeron hace 300 años».", "no se sabe", "Ninguna fuente lo dice."),
            ex(f"{P2} Clasifica como se ve o no se sabe: «el techo es de tejuelas».", "se ve", "La fotografía lo muestra."),
        ],
        "reason": [
            ex("Pedro dice: «Se ve que esa iglesia es la más antigua de Chile». ¿Qué respondes?", "Eso no se puede saber con la fotografía ni con la placa", "Solo debemos decir lo que podemos comprobar."),
            ex(f"{P2} ¿Qué dato de la placa muestra que la iglesia es valiosa para el mundo?", "Que es Patrimonio de la Humanidad", "Es un reconocimiento mundial."),
        ],
        "challenge": [
            ex(f"{P2} Escribe una frase con un dato de la fotografía y uno de la placa.", "La iglesia es de madera con torre y es Patrimonio de la Humanidad", "Usa evidencia de ambas fuentes."),
            ex("Escribe una pregunta que no se pueda responder con la fotografía.", "¿Quién construyó la iglesia?", "Es algo que las fuentes no muestran."),
        ],
    },
    context=[ex("Una compañera mira una fotografía del barrio histórico de Valparaíso y dice que tiene casas de colores en cerros. Otra añade: «Seguro las pintaron hace 10 años». ¿Qué parte de la frase no se sabe?", "hace cuánto las pintaron", "La fotografía no dice cuándo se pintaron.")],
    selfcheck=[
        ex(f"{P2} ¿Cerca de qué está la iglesia?", "del mar", "La descripción lo dice."),
        ex("¿Qué es un monumento?", "una construcción o escultura que recuerda algo importante", "Recuerda algo del pasado."),
        ex(f"{P2} ¿Cuántos años tiene la iglesia?", "no se sabe con estas fuentes", "Ninguna fuente lo dice."),
    ],
    open_task=task(
        f"Mira esta descripción y completa una tabla con dos columnas: «lo que se ve» y «lo que no sabemos». {P2} Escribe tres cosas en cada columna.",
        "Se ve: iglesia de madera; torre; techo de tejuelas. No sabemos: quién la construyó; cuántos años tiene; cuántas personas la visitan.",
        ["tres cosas que se ven", "tres que no se saben", "sin inventar"], ["tabla escrita"], ["poner la edad como dato", "inventar al constructor"],
        "Pide que mire cada afirmación y diga en qué fuente la vio."),
    reinforce="Mira una foto de un monumento y escribe tres cosas que se ven.",
    extend="Escribe una pregunta para investigar con un adulto sobre un monumento cercano.",
)

P3 = ("Casos de ejemplo: 1) La leyenda del Caleuche, un barco fantasma que navega de noche por el mar de Chiloé, que los abuelos cuentan a los niños. "
      "2) El baile chino, un baile religioso de la zona central de Chile, reconocido por la UNESCO. 3) Los alfareros de Pomaire, que enseñan a trabajar el barro a las nuevas generaciones. "
      "4) La cueca, el baile nacional de Chile. 5) El mapuzugun, el idioma mapuche, que se habla en comunidades y se enseña en algunas escuelas.")
register(
    OA5, 3,
    materials="Lápiz y papel. Los casos de ejemplo están escritos en cada ejercicio.",
    use="Aprenderé que el patrimonio también incluye cosas que no se tocan, como leyendas, bailes y oficios. Sirve para reconocer saberes que viven cuando las personas los practican.",
    prior=["Sé qué es el patrimonio tangible.", "Sé qué es una tradición."],
    explain=[
        "El patrimonio intangible es el que no se puede tocar: leyendas, canciones, bailes, fiestas, oficios y saberes. Vive cuando las personas lo practican y lo enseñan. Si nadie lo cuenta, lo baila o lo practica, se puede perder.",
        "En los casos de ejemplo, la leyenda del Caleuche se transmite por tradición oral, es decir, hablando. El baile chino y la cueca se aprenden bailando con otras personas. Los alfareros de Pomaire enseñan su oficio a las nuevas generaciones. El mapuzugun, un idioma, vive porque se habla y se enseña. Todos esos saberes se mantienen porque alguien los enseña.",
        "Algunas prácticas son religiosas o ceremoniales y merecen respeto. No deben convertirse en un espectáculo ni grabarse sin permiso. Antes de mirar o grabar una fiesta o ceremonia, se pide permiso a quienes la realizan y se observa con respeto.",
    ],
    vocab=[("intangible", "que no se puede tocar"), ("tradición oral", "historias que se pasan hablando"), ("oficio", "trabajo que se aprende y se practica con las manos"), ("leyenda", "historia tradicional con elementos de fantasía"), ("generación", "grupo de personas de una misma edad aproximada")],
    worked=[
        {"title": "Clasificar", "problem": f"{P3} ¿La leyenda del Caleuche es tangible o intangible?", "steps": ["Una leyenda se cuenta, no se toca.", "Se transmite hablando."], "answer": "Intangible"},
        {"title": "Cómo se mantiene", "problem": f"{P3} ¿Cómo se mantiene el oficio de los alfareros de Pomaire?", "steps": ["Los alfareros enseñan a las nuevas generaciones.", "Si se deja de enseñar, se podría perder."], "answer": "Porque lo enseñan a las nuevas generaciones"},
    ],
    mistakes=[
        {"wrong": "Pensar que lo intangible no es patrimonio porque no se toca.", "why": "Se piensa solo en edificios.", "fix": "También son patrimonio los saberes y costumbres que se practican."},
        {"wrong": "Grabar o fotografiar una ceremonia sin pedir permiso.", "why": "Se la trata como un espectáculo.", "fix": "Pide permiso y observa con respeto."},
    ],
    tiers={
        "recovery": [
            ex(f"{P3} ¿Qué barco aparece en la leyenda del Caleuche?", "un barco fantasma", "El caso 1 lo dice."),
            ex(f"{P3} ¿Qué baile es el baile nacional de Chile?", "la cueca", "El caso 4 lo dice."),
            ex("Intangible, ¿es lo que no se puede tocar o lo que se puede tocar?", "lo que no se puede tocar", "Esa es su definición."),
        ],
        "understand": [
            ex(f"{P3} ¿Qué trabajo aprenden las nuevas generaciones en Pomaire?", "trabajar el barro", "El caso 3 lo explica."),
            ex("¿Qué es la tradición oral?", "historias que se pasan hablando", "Se transmite con la voz."),
            ex("¿Por qué el patrimonio intangible se puede perder?", "Si nadie lo practica ni lo enseña", "Vive cuando se practica."),
        ],
        "apply": [
            ex(f"{P3} Clasifica en leyenda, baile u oficio: el caso 3.", "oficio", "Es un trabajo que se aprende."),
            ex(f"{P3} Clasifica en leyenda, baile u oficio: el caso 2.", "baile", "El baile chino es un baile."),
            ex(f"{P3} ¿Cuántos de los cinco casos son bailes?", "2", "El baile chino y la cueca."),
        ],
        "reason": [
            ex("Si un abuelo cuenta la leyenda del Caleuche y los niños la repiten, ¿qué le pasa a la leyenda?", "se mantiene viva", "Se transmite de generación en generación."),
            ex("Camila quiere grabar con su celular una ceremonia religiosa sin avisar. ¿Qué debería hacer primero?", "Pedir permiso a quienes la realizan", "Hay que respetar el significado de la ceremonia."),
        ],
        "challenge": [
            ex(f"{P3} Escribe un caso tangible y uno intangible relacionados con Chiloé.", "Tangible: las iglesias de madera. Intangible: la leyenda del Caleuche", "Uno se toca y el otro se cuenta."),
            ex("Explica por qué una fiesta religiosa no es un espectáculo.", "Porque para quienes participan tiene un significado especial", "Merece respeto por su significado."),
        ],
    },
    context=[ex("En una escuela, una artesana enseña a los niños a hacer una vasija de barro y los alumnos la repiten. ¿Qué patrimonio muestra esta actividad: tangible o intangible?", "intangible, porque es un oficio que se enseña", "Lo que se transmite es el saber de hacer la vasija.")],
    selfcheck=[
        ex(f"{P3} ¿El idioma mapuzugun es tangible o intangible?", "intangible", "Un idioma no se toca: vive cuando se habla y se enseña."),
        ex("¿Qué es un oficio?", "un trabajo que se aprende y se practica con las manos", "Se aprende y se enseña."),
        ex("¿Se debe pedir permiso para grabar una ceremonia?", "sí", "Hay que respetar a quienes la realizan."),
    ],
    open_task=task(
        f"Elige una leyenda, un baile, un oficio o un idioma de esta lista y escribe tres frases: qué es, cómo se transmite y qué haría una persona respetuosa al observarlo. {P3}",
        "Leyenda del Caleuche. Es un barco fantasma que navega de noche en Chiloé. Los abuelos la cuentan a los niños. Escucharé en silencio y no la contaré como si fuera un chiste.",
        ["práctica elegida", "cómo se transmite", "conducta respetuosa"], ["tres frases escritas"], ["decir que es solo para turistas", "olvidar la transmisión"],
        "Pregunta qué pasaría si dejaran de enseñar esa práctica."),
    reinforce="Pide a un adulto que te cuente una historia tradicional y repítela con tus palabras.",
    extend="Escribe qué harías para que un oficio no se pierda.",
)

P4 = ("Tabla de ejemplos por región (dada por la clase): Arica y Parinacota: momias Chinchorro, patrimonio tangible reconocido como Patrimonio de la Humanidad el año 2021. "
      "Tarapacá: fiesta de La Tirana, intangible, cada julio. Coquimbo: Fiesta Grande de Andacollo, intangible, en diciembre. "
      "Valparaíso: barrio histórico, tangible, Patrimonio de la Humanidad el año 2003; y Parque Nacional Rapa Nui, en la isla Rapa Nui, que es parte de esta región, tangible, Patrimonio de la Humanidad el año 1995. "
      "Región Metropolitana: Palacio de La Moneda, tangible, edificio de gobierno. O'Higgins: Sewell, antigua ciudad minera en la cordillera, tangible, Patrimonio de la Humanidad el año 2006. Los Lagos: iglesias de madera de Chiloé, tangibles, y leyenda del Caleuche, intangible.")
register(
    OA5, 4,
    materials="Lápiz y papel. La tabla de ejemplos por región está escrita en cada ejercicio.",
    use="Aprenderé a ubicar y describir ejemplos de patrimonio de distintas regiones de Chile. Sirve para conocer el patrimonio de mi región y de otras.",
    prior=["Sé qué es patrimonio tangible e intangible.", "Sé que Chile tiene regiones."],
    explain=[
        "Cada región de Chile tiene su propio patrimonio. En Arica y Parinacota están las momias Chinchorro, un patrimonio tangible de la humanidad. En Tarapacá se celebra cada julio la fiesta de La Tirana. En Coquimbo se celebra en diciembre la Fiesta Grande de Andacollo. En Valparaíso están el barrio histórico y el Parque Nacional Rapa Nui, en una isla del Pacífico. En O'Higgins está Sewell, una antigua ciudad minera. En la Región Metropolitana está el Palacio de La Moneda. En Los Lagos están las iglesias de madera de Chiloé y la leyenda del Caleuche.",
        "Para investigar un ejemplo de patrimonio hacemos tres pasos: lo ubicamos, es decir, decimos en qué región está; lo describimos, que es decir si es tangible o intangible y qué es; y hacemos una pregunta que aún no sabemos responder. Así aprendemos más.",
        "Puedes investigar un ejemplo de tu región o de otra región, según las fuentes que tengas. No es necesario hablar de tu familia ni de tu casa. Lo importante es usar datos de una fuente y no inventar.",
    ],
    vocab=[("región", "gran parte del territorio de Chile con su propia capital regional"), ("ubicar", "decir dónde está algo"), ("describir", "decir cómo es algo"), ("tangible", "que se puede tocar"), ("intangible", "que no se puede tocar")],
    worked=[
        {"title": "Ubicar", "problem": f"{P4} ¿En qué región está la fiesta de La Tirana?", "steps": ["Busco La Tirana en la tabla.", "Está en Tarapacá."], "answer": "En Tarapacá"},
        {"title": "Describir", "problem": f"{P4} Describe el Palacio de La Moneda.", "steps": ["Busco su fila.", "Es tangible y es un edificio de gobierno en la Región Metropolitana."], "answer": "Tangible; edificio de gobierno en la Región Metropolitana"},
    ],
    mistakes=[
        {"wrong": "Decir que el patrimonio solo existe en la capital.", "why": "Se piensa que lo importante está solo en la ciudad más grande.", "fix": "Cada región tiene patrimonio."},
        {"wrong": "Confundir la región con la ciudad.", "why": "Se mezclan los niveles.", "fix": "Una región tiene varias ciudades y pueblos."},
    ],
    tiers={
        "recovery": [
            ex(f"{P4} ¿En qué región están las momias Chinchorro?", "Arica y Parinacota", "La tabla lo dice."),
            ex(f"{P4} ¿Es tangible o intangible la fiesta de La Tirana?", "intangible", "La tabla lo indica."),
            ex(f"{P4} ¿En qué región está Sewell, la antigua ciudad minera?", "O'Higgins", "La tabla lo dice."),
        ],
        "understand": [
            ex(f"{P4} ¿Qué dos patrimonios se mencionan para Los Lagos?", "las iglesias de madera de Chiloé y la leyenda del Caleuche", "La tabla los nombra."),
            ex(f"{P4} ¿En qué año el barrio histórico de Valparaíso fue Patrimonio de la Humanidad?", "2003", "La tabla lo indica."),
            ex("¿Qué tres pasos seguimos para investigar un ejemplo de patrimonio?", "ubicar, describir y preguntar", "Son los tres pasos de la clase."),
        ],
        "apply": [
            ex(f"{P4} Une: 1) barrio histórico, 2) La Tirana. A) Tarapacá, B) Valparaíso.", "1 con B; 2 con A", "Cada patrimonio se une con su región."),
            ex(f"{P4} Clasifica como tangible o intangible: leyenda del Caleuche.", "intangible", "Se cuenta, no se toca."),
            ex(f"{P4} ¿Cuántos ejemplos tangibles aparecen en la tabla?", "6", "Chinchorro, barrio histórico, Parque Nacional Rapa Nui, La Moneda, Sewell e iglesias de madera."),
        ],
        "reason": [
            ex("Un compañero dice: «El patrimonio de Chile está todo en Santiago». Usa la tabla para corregirlo.", "Hay patrimonio en Arica y Parinacota, Tarapacá, Coquimbo, Valparaíso, O'Higgins y Los Lagos", "La tabla muestra otras regiones."),
            ex(f"{P4} ¿Qué dato de la tabla muestra que las momias Chinchorro son valiosas para el mundo?", "Que son Patrimonio de la Humanidad del año 2021", "Es un reconocimiento mundial."),
        ],
        "challenge": [
            ex(f"{P4} Escribe una ficha para un ejemplo: región, tipo, qué es y una pregunta pendiente.", "Los Lagos; tangible; iglesias de madera de Chiloé; ¿cuántas hay?", "Incluye los cuatro datos."),
            ex(f"{P4} Elige una región y escribe un ejemplo tangible y uno intangible si los hay.", "Los Lagos: iglesias de madera (tangible) y Caleuche (intangible)", "Es la única región de la tabla con ambos."),
        ],
    },
    context=[ex("Una niña vive en Valparaíso y quiere investigar un patrimonio cercano. ¿Cuál puede elegir de la tabla?", "el barrio histórico de Valparaíso", "La tabla lo ubica en Valparaíso.")],
    selfcheck=[
        ex(f"{P4} ¿En qué región se celebra la Fiesta Grande de Andacollo?", "Coquimbo", "La tabla lo dice."),
        ex("¿Qué es una región?", "una gran parte del territorio de Chile con su propia capital regional", "Chile se divide en regiones."),
        ex("¿Para investigar patrimonio hay que hablar de tu familia?", "no", "Se puede usar una fuente sobre una región."),
    ],
    open_task=task(
        f"Elige un ejemplo de la tabla y haz una ficha con: nombre, región, si es tangible o intangible, una frase que lo describa y una pregunta. {P4}",
        "Nombre: barrio histórico. Región: Valparaíso. Tangible. Es un barrio de casas en cerros, Patrimonio de la Humanidad desde 2003. Pregunta: ¿cómo se cuidan las casas?",
        ["ejemplo de la tabla", "región correcta", "tipo correcto", "una pregunta"], ["ficha escrita"], ["inventar datos", "confundir región con ciudad"],
        "Pregunta cómo supo la región. Debe decir que lo leyó en la tabla."),
    reinforce="Nombra tres ejemplos de patrimonio de la tabla con su región.",
    extend="Escribe una pregunta para investigar un patrimonio de tu región con ayuda de un adulto.",
)

P5 = ("Casos de ejemplo: caso 1) Una iglesia de madera tiene una gotera en el techo y puede dañarse. caso 2) Un sitio histórico no tiene carteles y los visitantes no saben cómo cuidarlo. "
      "caso 3) Una leyenda que solo recuerdan tres abuelos puede perderse. caso 4) A un lugar sagrado llegan muchas personas al mismo tiempo y se pisa el suelo. "
      "Medidas: restaurar (arreglar), señalizar (poner carteles), registrar (anotar y grabar con permiso) y regular visitas (limitar cuántas personas entran).")
register(
    OA5, 5,
    materials="Lápiz y papel. Los casos y las medidas están escritos en cada ejercicio.",
    use="Aprenderé a elegir una medida para cuidar el patrimonio con la comunidad, respetando su uso y su significado. Sirve para proteger lo que valoramos sin dañarlo.",
    prior=["Sé qué es el patrimonio tangible e intangible.", "Sé qué es una comunidad."],
    explain=[
        "Cuidar el patrimonio es proteger lo que una comunidad valora para que dure en el tiempo. Hay varias medidas: restaurar, que es arreglar lo que se dañó; señalizar, que es poner carteles que explican cómo cuidar; registrar, que es anotar o grabar con permiso; y regular visitas, que es limitar cuántas personas entran.",
        "Cada caso necesita una medida distinta. Si una iglesia tiene una gotera, hay que restaurar. Si un sitio no tiene carteles, se puede señalizar. Si una leyenda solo la recuerdan tres abuelos, conviene registrarla con su permiso. Si un lugar sagrado recibe demasiadas personas, se regulan las visitas.",
        "Las decisiones deben respetar el uso, el acceso y el significado. Uso es para qué se usa el lugar. Acceso es quién puede entrar. Significado es lo que significa para la comunidad. Por eso se pregunta a la comunidad antes de decidir y no se toman objetos de un sitio.",
    ],
    vocab=[("restaurar", "arreglar algo dañado para que dure"), ("señalizar", "poner carteles que informan o avisan"), ("registrar", "anotar o grabar para guardar el recuerdo"), ("regular", "poner reglas para cuidar"), ("significado", "lo que algo quiere decir para las personas")],
    worked=[
        {"title": "Elegir una medida", "problem": f"{P5} ¿Qué medida conviene para el caso 1?", "steps": ["El caso 1 tiene una gotera.", "Una gotera es un daño que se arregla."], "answer": "Restaurar"},
        {"title": "Cuidar el significado", "problem": f"{P5} ¿Qué medida conviene para el caso 4 y por qué?", "steps": ["Muchas personas pisan el suelo de un lugar sagrado.", "Regular visitas limita cuántas personas entran."], "answer": "Regular visitas, para no dañar el lugar"},
    ],
    mistakes=[
        {"wrong": "Elegir una medida sin preguntar a la comunidad.", "why": "Se piensa que solo las autoridades saben.", "fix": "Pregunta a la comunidad por el uso, el acceso y el significado."},
        {"wrong": "Llevarse un objeto de un sitio como recuerdo.", "why": "Se cree que un pedacito no hace daño.", "fix": "Los objetos de un sitio se dejan donde están."},
    ],
    tiers={
        "recovery": [
            ex(f"{P5} ¿Qué significa restaurar?", "arreglar algo dañado", "Las medidas lo explican."),
            ex(f"{P5} ¿Qué significa señalizar?", "poner carteles", "Las medidas lo explican."),
            ex(f"{P5} ¿Qué significa registrar?", "anotar y grabar con permiso", "Las medidas lo explican."),
        ],
        "understand": [
            ex(f"{P5} ¿Qué medida limita cuántas personas entran?", "regular visitas", "Esa es su definición."),
            ex("¿Por qué se pregunta a la comunidad antes de decidir una medida?", "Porque conoce el uso y el significado del patrimonio", "La comunidad sabe qué es valioso para ella."),
            ex("Uso, acceso y significado: ¿qué es el acceso?", "quién puede entrar", "Así se definió en la clase."),
        ],
        "apply": [
            ex(f"{P5} ¿Qué medida conviene para el caso 2?", "señalizar", "Hacen falta carteles."),
            ex(f"{P5} ¿Qué medida conviene para el caso 3?", "registrar con permiso", "Así la leyenda no se pierde."),
            ex(f"{P5} Une cada caso con su medida: 1) caso 1, 2) caso 4. A) regular visitas, B) restaurar.", "1 con B; 2 con A", "Gotera: restaurar. Muchas personas: regular visitas."),
        ],
        "reason": [
            ex("Un niño quiere llevarse una piedra de un sitio histórico como recuerdo. ¿Qué le dices?", "Que no, porque el objeto debe quedar donde está", "Llevarse cosas daña el sitio."),
            ex(f"{P5} En el caso 3, ¿por qué es importante pedir permiso a los abuelos para grabar?", "Porque la leyenda es de ellos y de su comunidad", "Se respeta a las personas."),
        ],
        "challenge": [
            ex(f"{P5} Escribe una medida distinta para el caso 4 que no sea limitar visitas y explica el motivo.", "Señalizar, para avisar cómo cuidar el suelo", "Los carteles también protegen."),
            ex("Una medida cuida el uso, pero no respeta el significado. ¿Es una buena medida?", "no", "Debe respetar uso, acceso y significado."),
        ],
    },
    context=[ex("En un pueblo, una iglesia vieja tiene el techo roto y no hay carteles. La comunidad decide arreglar el techo primero. ¿Qué medida eligió?", "restaurar", "Arreglar el techo es restaurar.")],
    selfcheck=[
        ex("¿Qué medida pone carteles que informan?", "señalizar", "Esa es su definición."),
        ex("¿Se puede llevar un objeto de un sitio histórico?", "no", "Debe quedar en su lugar."),
        ex("¿Con quién se debe consultar antes de cuidar un patrimonio?", "con la comunidad", "Ella conoce su significado."),
    ],
    open_task=task(
        f"Elige uno de los cuatro casos y escribe una mini propuesta con: medida, motivo y cómo se respetaría el significado. {P5}",
        "Caso 4. Medida: regular visitas. Motivo: muchas personas pisan el suelo. Pregunto a la comunidad cuántas personas pueden entrar sin dañar y respeto el significado del lugar sagrado.",
        ["caso elegido", "medida adecuada", "motivo", "respeto al significado"], ["propuesta escrita"], ["tomar objetos como recuerdo", "decidir sin la comunidad"],
        "Pregunta quién debería decidir la medida. Debe incluir a la comunidad."),
    reinforce="Elige una cosa que quieras cuidar en tu escuela y di qué medida usarías.",
    extend="Escribe un cartel corto que explique cómo cuidar un lugar importante.",
)

# ================================================================ OA 06
V1 = ("Descripciones de objetos vistos desde arriba (dadas por la clase): mesa redonda = círculo; mesa de escritorio = rectángulo; silla = cuadrado pequeño; cama = rectángulo largo; puerta = hueco en la pared con una línea curva; ventana = línea doble en la pared.")
register(
    OA6, 1,
    materials="Lápiz, papel y regla. Las descripciones de los objetos están escritas en cada ejercicio.",
    use="Aprenderé a ver objetos desde arriba, como en un plano. Sirve para dibujar una pieza o una sala como la ve un pájaro.",
    prior=["Sé reconocer círculo, cuadrado y rectángulo.", "Sé qué es izquierda y derecha."],
    explain=[
        "Un plano es un dibujo de un lugar visto desde arriba. Es como si fueras un pájaro mirando la sala desde el techo. En un plano no vemos las patas ni el respaldo de las cosas, solo su forma desde arriba.",
        "Esa forma vista desde arriba se llama vista superior. Una mesa redonda se ve como un círculo. Una mesa de escritorio se ve como un rectángulo. Una silla se ve como un cuadrado pequeño y una cama como un rectángulo largo.",
        "Las puertas y ventanas también se dibujan. La puerta es un hueco en la pared con una línea curva que muestra cómo se abre. La ventana es una línea doble en la pared. Así, otra persona entiende tu plano sin necesidad de explicarlo.",
    ],
    vocab=[("plano", "dibujo de un lugar visto desde arriba"), ("vista superior", "forma de un objeto visto desde arriba"), ("símbolo", "dibujo simple que representa algo"), ("rectángulo", "figura con cuatro lados, dos largos y dos cortos"), ("círculo", "figura redonda")],
    worked=[
        {"title": "Elegir la forma", "problem": f"{V1} ¿Cómo se dibuja una mesa redonda en un plano?", "steps": ["Pienso cómo se ve desde arriba.", "Una mesa redonda se ve como un círculo."], "answer": "Un círculo"},
        {"title": "Emparejar", "problem": f"{V1} ¿Qué objeto es un cuadrado pequeño?", "steps": ["Busco cuadrado pequeño en las descripciones.", "Es la silla."], "answer": "La silla"},
    ],
    mistakes=[
        {"wrong": "Dibujar la silla de lado, con patas.", "why": "Se dibuja como se ve de frente.", "fix": "Dibuja solo la forma que se ve desde arriba: un cuadrado."},
        {"wrong": "No dibujar la puerta ni las ventanas.", "why": "Se piensa que solo importan los muebles.", "fix": "Dibuja la puerta y las ventanas para que se entienda el lugar."},
    ],
    tiers={
        "recovery": [
            ex(f"{V1} ¿Qué figura es una mesa redonda vista desde arriba?", "un círculo", "Las descripciones lo indican."),
            ex(f"{V1} ¿Qué figura es una cama?", "un rectángulo largo", "Las descripciones lo indican."),
            ex("Un plano, ¿es un dibujo visto desde arriba o de frente?", "desde arriba", "Esa es su definición."),
        ],
        "understand": [
            ex(f"{V1} ¿Cómo se dibuja una ventana?", "con una línea doble en la pared", "Las descripciones lo indican."),
            ex(f"{V1} ¿Cómo se dibuja la puerta?", "con un hueco en la pared y una línea curva", "Las descripciones lo indican."),
            ex("¿Por qué en un plano no vemos las patas de una silla?", "Porque se ve desde arriba", "Desde arriba no se ven las patas."),
        ],
        "apply": [
            ex(f"{V1} Une: 1) silla, 2) mesa de escritorio. A) rectángulo, B) cuadrado pequeño.", "1 con B; 2 con A", "Silla es cuadrada y escritorio es rectángulo."),
            ex("Un tapete redondo de la sala, visto desde arriba, ¿qué figura es?", "un círculo", "Redondo se ve como círculo desde arriba."),
            ex(f"{V1} Si dibujas una sala con dos sillas y una mesa redonda, ¿cuántas figuras tendrá?", "3", "Dos cuadrados pequeños y un círculo."),
        ],
        "reason": [
            ex("Una niña dibuja una mesa redonda como un rectángulo. ¿Qué error cometió?", "Cambió la forma que se ve desde arriba", "Una mesa redonda se ve circular."),
            ex(f"{V1} ¿Por qué conviene dibujar la puerta en un plano?", "Para saber por dónde se entra", "La puerta muestra la entrada."),
        ],
        "challenge": [
            ex(f"{V1} Describe en palabras el plano de una pieza con una cama, una ventana y una puerta.", "Un rectángulo largo, una línea doble en la pared y un hueco con línea curva", "Usa los símbolos de las descripciones."),
            ex("Un balón visto desde arriba, ¿qué figura es?", "un círculo", "Una esfera se ve circular."),
        ],
    },
    context=[ex("Una niña hace el plano de su comedor: mesa redonda, cuatro sillas, una puerta y una ventana. ¿Cuántos símbolos dibujó en total?", "7", "Una mesa, cuatro sillas, una puerta y una ventana: 1 + 4 + 1 + 1 = 7.")],
    selfcheck=[
        ex(f"{V1} ¿Cómo se ve una silla desde arriba?", "como un cuadrado pequeño", "Las descripciones lo indican."),
        ex("¿Qué es la vista superior?", "la forma de un objeto visto desde arriba", "Eso es mirar desde arriba."),
        ex(f"{V1} ¿Qué se dibuja con una línea doble en la pared?", "la ventana", "Las descripciones lo indican."),
    ],
    open_task=task(
        f"Dibuja un plano de una pieza con: una cama, una mesa redonda, dos sillas, una puerta y una ventana. {V1} Usa solo los símbolos de las descripciones.",
        "Cama: rectángulo largo contra una pared. Mesa: círculo en el medio. Sillas: dos cuadrados pequeños. Puerta: hueco con línea curva. Ventana: línea doble en otra pared.",
        ["cinco elementos", "formas correctas", "puerta y ventana en la pared"], ["plano dibujado"], ["dibujar los objetos de frente", "olvidar la puerta"],
        "Pregunta qué figura usó para cada objeto y por qué."),
    reinforce="Mira tu mesa desde arriba y dibuja su figura.",
    extend="Elige otro objeto de tu casa y escribe qué figura tendría en un plano.",
)

R2 = ("Plano de la biblioteca del curso (descripción dada): estás de pie en la entrada, mirando hacia el fondo de la sala. A tu derecha está el estante de cuentos. A tu izquierda está el escritorio de la profesora. "
      "Al fondo, frente a ti, está la pizarra. Entre el estante y la pizarra hay una mesa redonda. El estante está cerca de la entrada y la pizarra está lejos de ella.")
register(
    OA6, 2,
    materials="Lápiz y papel. La descripción de la biblioteca está escrita en cada ejercicio.",
    use="Aprenderé a ubicar un lugar respecto de un punto de referencia usando derecha, izquierda, delante, detrás, al lado y entre. Sirve para explicar dónde está algo.",
    prior=["Sé qué es izquierda y derecha.", "Sé qué es un plano."],
    explain=[
        "Un punto de referencia es un lugar conocido desde el cual describimos dónde está otra cosa. Por ejemplo, la entrada de la sala. Para ubicar algo usamos palabras de posición: a la derecha, a la izquierda, delante, detrás, al lado, entre, cerca y lejos.",
        "En la descripción de la biblioteca, estás en la entrada mirando hacia el fondo. El estante de cuentos queda a tu derecha. El escritorio de la profesora queda a tu izquierda. La pizarra queda al fondo, frente a ti. Entre el estante y la pizarra hay una mesa redonda.",
        "Si cambias el punto de referencia, cambia la descripción. Si caminas hasta la pizarra y te das vuelta para mirar hacia la entrada, lo que estaba a tu derecha ahora queda a tu izquierda. Por eso es importante decir desde dónde estás mirando.",
    ],
    vocab=[("punto de referencia", "lugar conocido desde el cual describimos otros"), ("posición relativa", "dónde está algo en relación con otra cosa"), ("derecha", "el lado de la mano con que muchos escriben"), ("izquierda", "el lado contrario a la derecha"), ("entre", "en medio de dos cosas")],
    worked=[
        {"title": "Describir desde la entrada", "problem": f"{R2} ¿Dónde está el estante de cuentos?", "steps": ["Estoy en la entrada mirando al fondo.", "El estante queda a mi derecha."], "answer": "A la derecha"},
        {"title": "Cambiar el referente", "problem": f"{R2} Si caminas hasta la pizarra y te das vuelta para mirar hacia la entrada, ¿dónde queda ahora el escritorio de la profesora?", "steps": ["Antes, desde la entrada, estaba a mi izquierda.", "Al darme vuelta, la izquierda pasa a ser derecha."], "answer": "A la derecha"},
    ],
    mistakes=[
        {"wrong": "Decir «allá» o «ahí» sin decir desde dónde.", "why": "No se da un punto de referencia.", "fix": "Di «desde la entrada, a la derecha»."},
        {"wrong": "Olvidar que la derecha cambia si te das vuelta.", "why": "Se piensa que derecha es siempre el mismo lado de la sala.", "fix": "Derecha e izquierda dependen de hacia dónde miras."},
    ],
    tiers={
        "recovery": [
            ex(f"{R2} ¿Qué hay al fondo, frente a ti?", "la pizarra", "La descripción lo dice."),
            ex(f"{R2} ¿Qué queda a tu izquierda?", "el escritorio de la profesora", "La descripción lo dice."),
            ex(f"{R2} ¿Qué queda lejos de la entrada: la pizarra o el estante de cuentos?", "la pizarra", "La descripción dice que la pizarra está lejos de la entrada."),
        ],
        "understand": [
            ex(f"{R2} ¿Qué hay entre el estante y la pizarra?", "una mesa redonda", "La descripción lo dice."),
            ex("En Historia: ¿Qué es un punto de referencia?", "un lugar conocido desde el cual describimos otros", "Sirve para ubicar."),
            ex("¿Por qué conviene decir desde dónde miras?", "Porque cambia la derecha y la izquierda", "Cambia la descripción."),
        ],
        "apply": [
            ex(f"{R2} Estás frente a la pizarra mirando hacia la entrada. ¿Dónde queda el estante de cuentos?", "a la izquierda", "Al darte vuelta, la derecha pasa a ser izquierda."),
            ex(f"{R2} Completa: «Desde la entrada, la ___ queda al fondo, frente a ti».", "pizarra", "La descripción ubica la pizarra al fondo."),
            ex(f"{R2} Completa: «La mesa redonda está ___ el estante y la pizarra».", "entre", "La descripción usa entre."),
        ],
        "reason": [
            ex("Una niña dice: «El estante está a la derecha» sin decir desde dónde. ¿Qué le falta?", "Un punto de referencia", "Debe decir desde dónde mira."),
            ex(f"{R2} Un compañero dice que el escritorio queda a la derecha. ¿Cuándo sería correcto?", "Cuando estás en la pizarra mirando hacia la entrada", "Al darte vuelta cambia el lado."),
        ],
        "challenge": [
            ex(f"{R2} ¿Cuántos muebles u objetos nombra la descripción en total?", "4", "Nombra el estante, el escritorio, la pizarra y la mesa redonda."),
            ex(f"{R2} Escribe una frase con un punto de referencia y una palabra de posición.", "Desde la entrada, el estante está a la derecha", "Tiene referente y posición."),
        ],
    },
    context=[ex("En un plano de la sala, la puerta está en la parte baja y la pizarra arriba. Si estás en la puerta mirando hacia arriba del plano, ¿qué tienes frente a ti?", "la pizarra", "Miras hacia arriba del plano, donde está la pizarra.")],
    selfcheck=[
        ex(f"{R2} ¿Qué queda a tu derecha desde la entrada?", "el estante de cuentos", "La descripción lo dice."),
        ex("¿Qué es la posición relativa?", "dónde está algo en relación con otra cosa", "Siempre se compara con un referente."),
        ex("Si te das vuelta, ¿la derecha cambia?", "sí", "Derecha depende de hacia dónde miras."),
    ],
    open_task=task(
        f"Escribe cuatro frases para describir la biblioteca, cada una con un punto de referencia y una palabra de posición. {R2} Después cambia el punto de referencia y escribe una frase.",
        "Desde la entrada: el estante está a la derecha. Desde la entrada: el escritorio está a la izquierda. Desde la entrada: la pizarra está al fondo. La mesa está entre el estante y la pizarra. Desde la pizarra mirando la entrada, el estante queda a la izquierda.",
        ["cuatro frases", "punto de referencia", "palabras de posición", "frase con referente cambiado"], ["frases escritas"], ["no decir desde dónde", "no cambiar derecha e izquierda al dar la vuelta"],
        "Pide que muestre con su cuerpo hacia dónde miraba al hacer cada frase."),
    reinforce="Describe a un adulto dónde está tu cama desde la puerta de tu pieza.",
    extend="Haz un dibujo simple de la biblioteca y marca la entrada con una flecha.",
)

L3 = ("Plano del patio (descripción dada): hay 3 círculos, 2 cuadrados y 1 triángulo. Leyenda: círculo = árbol; cuadrado = banca; triángulo = juego de columpios.")
register(
    OA6, 3,
    materials="Lápiz y papel. La descripción del patio y su leyenda están escritas en cada ejercicio.",
    use="Aprenderé a crear símbolos simples y a explicarlos en una leyenda. Sirve para que otra persona entienda mi plano.",
    prior=["Sé qué es un plano.", "Sé contar hasta 20."],
    explain=[
        "Un símbolo es un dibujo simple que representa algo. En un plano usamos símbolos para no dibujar todos los detalles. Un círculo puede ser un árbol, un cuadrado una banca y un triángulo un juego de columpios. Esos son símbolos geométricos. También hay símbolos pictóricos, que son dibujos pequeños que se parecen a lo que representan, como un arbolito para un árbol o una casita para una casa.",
        "La leyenda es una lista que dice qué significa cada símbolo. Sin la leyenda, otra persona no sabe si un círculo es un árbol, una mesa o una fuente. Por eso la leyenda es parte del plano y se escribe en una esquina.",
        "Los símbolos deben ser simples y distintos entre sí. Así no se confunden. Si el árbol y la banca fueran parecidos, no sabríamos cuál es cuál. Un buen plano tiene símbolos claros y una leyenda completa.",
    ],
    vocab=[("símbolo", "dibujo simple que representa algo"), ("leyenda", "lista que explica el significado de los símbolos"), ("detalle", "parte pequeña de algo"), ("claro", "fácil de entender"), ("esquina", "lugar donde se juntan dos bordes"), ("símbolo pictórico", "dibujo pequeño que se parece a lo que representa")],
    worked=[
        {"title": "Leer la leyenda", "problem": f"{L3} ¿Qué representa un cuadrado?", "steps": ["Busco cuadrado en la leyenda.", "Dice: cuadrado = banca."], "answer": "Una banca"},
        {"title": "Contar símbolos", "problem": f"{L3} ¿Cuántos árboles hay en el patio?", "steps": ["Los árboles son círculos.", "Hay 3 círculos."], "answer": "3 árboles"},
    ],
    mistakes=[
        {"wrong": "Dibujar un plano sin leyenda.", "why": "Se piensa que todos entenderán los símbolos.", "fix": "Escribe la leyenda con cada símbolo y su significado."},
        {"wrong": "Usar el mismo símbolo para dos cosas distintas.", "why": "Se quiere dibujar rápido.", "fix": "Usa un símbolo distinto para cada cosa."},
    ],
    tiers={
        "recovery": [
            ex(f"{L3} ¿Qué representa un triángulo?", "un juego de columpios", "La leyenda lo dice."),
            ex(f"{L3} ¿Cuántos círculos hay?", "3", "La descripción lo dice."),
            ex("Una leyenda, ¿explica los símbolos o cuenta un cuento?", "explica los símbolos", "Esa es su función."),
        ],
        "understand": [
            ex(f"{L3} ¿Cuántas bancas hay en el patio?", "2", "Hay 2 cuadrados y cada uno es una banca."),
            ex("¿Por qué necesita un plano una leyenda?", "Para saber qué significa cada símbolo", "Sin ella no se entiende."),
            ex("Un símbolo pictórico para un árbol, ¿es un arbolito dibujado o un triángulo?", "un arbolito dibujado", "Un símbolo pictórico se parece a lo que representa."),
        ],
        "apply": [
            ex(f"{L3} ¿Cuántos símbolos hay en total en el plano?", "6", "3 círculos más 2 cuadrados más 1 triángulo: 3 + 2 + 1 = 6."),
            ex("Quieres agregar una fuente de agua al plano sin repetir símbolos. ¿Cuál figura sirve: círculo, cuadrado, triángulo o estrella?", "estrella", "Las otras tres ya significan árbol, banca y columpios."),
            ex(f"{L3} Escribe la leyenda que dice qué es un círculo y qué es un triángulo.", "círculo = árbol; triángulo = juego de columpios", "Es el contenido de la leyenda."),
        ],
        "reason": [
            ex("Si un plano usa el mismo círculo para un árbol y para una fuente, ¿qué problema hay?", "No se sabe cuál es cuál", "Cada cosa necesita un símbolo distinto."),
            ex("Una niña usa una casita dibujada para una casa y un cuadrado para una banca. ¿Cuál de los dos es un símbolo pictórico?", "la casita dibujada", "Se parece a la casa que representa."),
        ],
        "challenge": [
            ex(f"{L3} Si se agrega una nueva banca, ¿cuántos cuadrados tendría el plano?", "3", "2 bancas más 1 banca: 2 + 1 = 3."),
            ex("Dibuja en palabras una leyenda con tres símbolos para una sala: puerta, ventana y mesa.", "puerta = hueco con línea curva; ventana = línea doble; mesa = rectángulo", "Cada símbolo tiene su significado."),
        ],
    },
    context=[ex("En el plano de una plaza hay 4 círculos que representan árboles y 2 triángulos que representan juegos. ¿Cuántos símbolos hay en total?", "6", "4 + 2 = 6.")],
    selfcheck=[
        ex("En Historia: ¿Qué es un símbolo?", "un dibujo simple que representa algo", "Reemplaza muchos detalles."),
        ex(f"{L3} ¿Qué representa un círculo?", "un árbol", "La leyenda lo dice."),
        ex("¿Dos cosas distintas pueden tener el mismo símbolo?", "no", "Las personas se confundirían."),
    ],
    open_task=task(
        f"Dibuja un plano del patio con 3 árboles, 2 bancas y 1 juego de columpios. Crea tus propios símbolos simples, geométricos o pictóricos, y escribe una leyenda en una esquina. {L3}",
        "Planos con 3 círculos, 2 cuadrados y 1 triángulo. Leyenda: círculo = árbol; cuadrado = banca; triángulo = juego de columpios.",
        ["seis símbolos", "símbolos distintos", "leyenda completa"], ["plano y leyenda dibujados"], ["no hacer la leyenda", "usar el mismo símbolo para dos cosas"],
        "Pregunta a alguien si entiende el plano solo con la leyenda."),
    reinforce="Inventa un símbolo para una casa y otro para un árbol y explícalos.",
    extend="Haz una leyenda de tres símbolos para el plano de tu pieza.",
)

RU4 = ("Ruta de ejemplo (dada por la clase): sales de la sala por la puerta. Caminas 4 pasos hacia adelante hasta la escalera. Giras a la derecha. Caminas 3 pasos hasta la puerta del patio. "
       "Referencias del camino: puerta de la sala, escalera, puerta del patio.")
register(
    OA6, 4,
    materials="Lápiz y papel. La ruta de ejemplo está escrita en cada ejercicio.",
    use="Aprenderé a dibujar un plano con una ruta que otra persona pueda seguir. Sirve para explicar cómo llegar de un lugar a otro.",
    prior=["Sé qué es un plano y una leyenda.", "Sé usar derecha e izquierda."],
    explain=[
        "Una ruta es el camino para ir de un lugar a otro. Para explicarla, se usan puntos de referencia, números de pasos y giros a la derecha o a la izquierda. Por ejemplo: sales de la sala, caminas 4 pasos, giras a la derecha y caminas 3 pasos.",
        "Una buena ruta es clara. Dice por dónde empezar, cuántos pasos dar y hacia dónde girar. No usa palabras como «un poco más allá», porque cada persona entiende algo distinto. Es mejor decir «4 pasos».",
        "Para saber si la ruta funciona, otra persona la sigue. Si se confunde, marcamos lo que no era claro y lo corregimos. Una ruta debe ser también segura: no pasar por lugares peligrosos y no correr.",
    ],
    vocab=[("ruta", "camino para ir de un lugar a otro"), ("giro", "cambio de dirección hacia la derecha o la izquierda"), ("paso", "unidad para medir distancias cortas caminando"), ("ambigüedad", "cuando algo puede entenderse de dos formas"), ("seguro", "que no tiene peligro")],
    worked=[
        {"title": "Seguir una ruta", "problem": f"{RU4} ¿A dónde llegas si sigues la ruta completa?", "steps": ["Salgo de la sala y camino 4 pasos hasta la escalera.", "Giro a la derecha y camino 3 pasos.", "Llego a la puerta del patio."], "answer": "A la puerta del patio"},
        {"title": "Encontrar una ambigüedad", "problem": "En una ruta dice: «Camina un poco y gira». ¿Qué no está claro?", "steps": ["No dice cuántos pasos.", "Tampoco dice hacia dónde girar."], "answer": "No dice cuántos pasos ni hacia dónde girar"},
    ],
    mistakes=[
        {"wrong": "Escribir una ruta con «un poco» o «por ahí».", "why": "Parece fácil de decir.", "fix": "Usa números de pasos y giros a la derecha o a la izquierda."},
        {"wrong": "No probar la ruta con otra persona.", "why": "Se cree que ya está clara.", "fix": "Pide que alguien la siga y marca dónde se confunde."},
    ],
    tiers={
        "recovery": [
            ex(f"{RU4} ¿Cuántos pasos caminas hasta la escalera?", "4", "La ruta lo dice."),
            ex(f"{RU4} ¿Hacia dónde giras en la escalera?", "a la derecha", "La ruta lo dice."),
            ex("Una ruta, ¿es un camino para ir de un lugar a otro o una pared?", "un camino para ir de un lugar a otro", "Esa es su definición."),
        ],
        "understand": [
            ex(f"{RU4} ¿Cuántos pasos caminas después de girar?", "3", "La ruta lo dice."),
            ex("¿Por qué «camina un poco» no es una buena indicación?", "Porque cada persona lo entiende distinto", "No es una medida clara."),
            ex(f"{RU4} Nombra las tres referencias del camino.", "puerta de la sala, escalera y puerta del patio", "Están al final de la ruta."),
        ],
        "apply": [
            ex(f"{RU4} ¿Cuántos pasos caminas en total?", "7", "4 pasos más 3 pasos: 4 + 3 = 7."),
            ex("Una ruta dice: sales de la sala y caminas 5 pasos. La biblioteca queda a tu izquierda. ¿Hacia dónde debes girar?", "a la izquierda", "Debes girar hacia el lado donde queda la biblioteca."),
            ex(f"{RU4} Escribe la ruta en una sola frase.", "Salgo de la sala, camino 4 pasos, giro a la derecha y camino 3 pasos hasta el patio", "Incluye pasos y giros."),
        ],
        "reason": [
            ex("Un compañero sigue «camina hacia el árbol y gira» y se pierde. ¿Qué dos datos faltan?", "cuántos pasos y hacia dónde girar", "Sin ellos la ruta es ambigua."),
            ex("¿Por qué una ruta de la sala al patio debe ser segura?", "Para no pasar por lugares peligrosos", "Cuidar a las personas es lo primero."),
        ],
        "challenge": [
            ex(f"{RU4} Si después de la escalera giras a la izquierda en vez de a la derecha, ¿llegas a la puerta del patio?", "no", "La ruta indica girar a la derecha."),
            ex("Una ruta dice: camina 2 pasos, gira a la derecha y camina 5 pasos. ¿Cuántos pasos camina en total?", "7", "Se suman 2 pasos y 5 pasos: 2 + 5 = 7."),
        ],
    },
    context=[ex("Una niña dibuja una ruta con una flecha desde la sala hasta el patio y escribe «4 pasos» y «3 pasos». Su amigo la sigue y llega bien. ¿Qué muestra eso de la ruta?", "que era clara", "Cuando alguien la sigue sin errores, la ruta funciona.")],
    selfcheck=[
        ex("¿Qué es un giro?", "un cambio de dirección", "Se gira a la derecha o a la izquierda."),
        ex(f"{RU4} ¿A dónde lleva la ruta?", "a la puerta del patio", "Es el destino de la ruta."),
        ex("¿Por qué conviene probar la ruta con otra persona?", "Para ver si se entiende", "Así se encuentran las ambigüedades."),
    ],
    open_task=task(
        f"Dibuja un plano con una ruta desde tu pieza hasta la puerta de calle de tu casa. Marca tres puntos de referencia, los pasos y los giros. {RU4} Pide a un adulto que la siga con el dedo.",
        "Pieza, 5 pasos hacia adelante hasta el pasillo, giro a la derecha, 4 pasos hasta la puerta de calle. Referencias: puerta de la pieza, pasillo, puerta de calle.",
        ["ruta dibujada", "pasos y giros", "tres referencias"], ["plano con ruta"], ["usar un poco o por ahí", "no probar la ruta"],
        "Pregunta dónde se confundió la persona que la siguió y cómo lo corregiría."),
    reinforce="Explica a alguien cómo ir de la cocina al baño de tu casa con pasos y giros.",
    extend="Agrega a tu plano una segunda ruta más corta si existe.",
)

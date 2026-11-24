"""Inglés EPJA Nivel 2, módulo 1 (parte 4): OAD-04, presentarse y presentar a una persona cercana frente a la clase. Todos los textos y guiones son inventados y se leen en papel."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-04"

F1 = ("Transcripción de una presentación oral de ejemplo (inventada): Good morning, everyone. My name is Rosa. I'm from Chile. I'm a baker. I'm forty years old. I like music and plants. Thank you.")

F2 = ("Transcripción de una presentación de ejemplo (inventada): Hello, everyone. Let me introduce my neighbor, Carmen. She is forty-five years old. She is from Peru. She is a nurse. She likes music. "
      "Her daughter is Ana. Her son is Pedro.")

F3 = ("Presentación de ejemplo (inventada): Good afternoon, everyone. This is Marcos. He is my friend. He is from Colombia. He is thirty-eight years old. He works in a restaurant. "
      "He lives in my neighborhood. He likes soccer, but he doesn't like cooking. Thank you.")

F4 = ("Presentación desordenada de ejemplo (inventada), oraciones numeradas: 1) Thank you. 2) This is my friend, Lucía. 3) Good morning, everyone. 4) She is thirty-three years old. 5) She likes dancing. 6) She is from Bolivia.")

F5 = ("Tarjeta de datos de ejemplo (inventada) para preparar una presentación: Person: my friend. Name: Luis Rojas. From: Chile. Age: 52. Job: driver. Place of work: a bus company. Likes: soccer and music. Doesn't like: cooking.")

F6 = ("Presentación de un compañero de ejemplo (inventada): Good evening, everyone. This is my brother, Diego. He is from Chile. He is twenty-nine years old. He works in a store. "
      "He likes walking, but he doesn't like reading. Thank you. "
      "Pauta para escuchar: 1 saludo. 2 nombre. 3 país. 4 edad. 5 oficio o lugar de trabajo. 6 gustos. 7 cierre.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy conozco la estructura de una presentación oral breve en inglés: inicio, datos y cierre.",
    prior=["Me presento con mi nombre, país, oficio y edad.", "Digo lo que me gusta.", "Conozco los saludos según la hora."],
    explain=[
        "Presentarse frente a la clase da nervios a muchas personas, y es normal. Una estructura clara ayuda. Una presentación oral breve tiene tres partes: inicio, datos y cierre. Hoy escuchas, leyendo el guion, un modelo con las tres.",
        "En el inicio saludas y dices tu nombre: Good morning, everyone. My name is Rosa. En los datos das cuatro cosas: país, oficio, edad y gustos. En el cierre agradeces: Thank you. Con esta estructura sabes qué viene después.",
        "Antes de hablar, escribe notas cortas con palabras clave, no el texto completo. Habla despacio, mira a la clase y respira. Tú ya sabes todas las frases: solo las ordenas. Si te equivocas, sigue; en una presentación lo importante es que te entiendan.",
    ],
    vocab=[("everyone", "todos, todas"), ("Good morning, everyone.", "Buenos días a todos."), ("my name is", "mi nombre es"), ("I'm from", "soy de"), ("years old", "años de edad"), ("I like", "me gusta"), ("thank you", "gracias"), ("today", "hoy")],
    worked=[
        ("Reconocer las tres partes", "Presentación: «Good morning, everyone. My name is Rosa. I'm a baker. Thank you.» ¿Cuál es el inicio, los datos y el cierre?", ["El inicio es el saludo y el nombre: Good morning, everyone. My name is Rosa.", "Los datos dicen el oficio: I'm a baker.", "El cierre es Thank you."], "Inicio: saludo y nombre. Datos: oficio. Cierre: Thank you."),
        ("Armar mi inicio", "Son las 4 de la tarde y debes saludar a la clase y decir que te llamas Pedro.", ["Elijo el saludo de la tarde: Good afternoon.", "Agrego a todos: everyone.", "Digo mi nombre: My name is Pedro."], "Good afternoon, everyone. My name is Pedro."),
    ],
    mistakes=[("Empezar con «Thank you» o con la edad.", "No se piensa el orden de la presentación.", "Empieza con el saludo y el nombre, y deja Thank you para el final."),
              ("Querer memorizar todo palabra por palabra.", "Se cree que hay que decir un texto perfecto.", "Usa notas con palabras clave y habla con tus propias frases cortas.")],
    T=[
        ("abc", "{F} ¿Cómo comienza Rosa su presentación?", "Con un saludo a todos", "Con su edad", "Con una despedida", "Rosa empieza con Good morning, everyone."),
        ("abc", "{F} ¿Cómo termina la presentación?", "Con Thank you", "Con su país", "Con su nombre", "El cierre es la frase Thank you, gracias."),
        ("{F} ¿Qué oficio dice Rosa? Escribe una palabra en inglés.", "baker", "Rosa dice I'm a baker, es decir, es panadera."),
        ("{F} ¿Cuántos años dice Rosa que tiene? Escribe solo el número.", "40", "Rosa dice forty years old, que significa cuarenta años."),
        ("abc", "{F} ¿Qué dos gustos nombra Rosa?", "La música y las plantas", "El fútbol y la lectura", "Cocinar y bailar", "Rosa dice I like music and plants."),
        ("abc", "¿En qué parte de la presentación dices tu nombre?", "Al inicio, después del saludo", "Al final", "No se dice", "El nombre va en el inicio, junto con el saludo."),
        ("ab", "Para saludar a un grupo en la mañana dices...", "Good morning, everyone.", "Good night, everyone.", "Good morning se usa en la mañana; good night es una despedida."),
        ("abc", "Para agradecer al final de tu presentación dices...", "Thank you.", "Nice to meet you.", "See you later.", "Thank you es la fórmula de cierre y agradecimiento."),
        ("Ordena las palabras: from / I'm / Chile", "I'm from Chile.", "El orden es I'm, luego from y al final el país."),
        ("abc", "¿Qué ayuda más al hablar frente a la clase?", "Usar notas cortas con palabras clave", "Leer todo muy rápido sin mirar", "Memorizar sin entender", "Las notas con palabras clave guían sin que leas todo."),
        ("abc", "Rosa dice «I'm forty years old». ¿Qué dato da?", "La edad", "El país", "El oficio", "Years old indica la edad de la persona."),
        ("ab", "Alguien empieza su presentación con «Thank you». ¿Es el mejor orden?", "No: thank you va al final", "Sí: thank you va al inicio", "Thank you es el cierre y va al final de la presentación."),
        ("abc", "¿Cuál es el orden de las tres partes de una presentación?", "Saludo y nombre, datos, cierre", "Cierre, datos, saludo", "Datos, saludo, cierre", "El orden natural es inicio, datos y cierre."),
    ],
    ctx=("abc", "Vas a presentarte ante la clase a las 9 de la mañana y quieres comenzar bien. ¿Qué dices?", "Good morning, everyone. My name is Pedro.", "Thank you, everyone. Goodbye.", "I'm forty years old. Good night.", "Se empieza con un saludo según la hora y el nombre."),
    sc=[("abc", "En Inglés: ¿cuáles son las tres partes de una presentación?", "Inicio, datos y cierre", "Pregunta, respuesta y firma", "Título, texto y dibujo", "Una presentación breve tiene inicio, datos y cierre."),
        ("abc", "En Inglés: ¿qué frase sirve para cerrar?", "Thank you.", "Good morning.", "Where are you from?", "Thank you cierra y agradece a la audiencia."),
        ("abc", "En Inglés: ¿qué conviene usar al presentar?", "Notas cortas con palabras clave", "Un texto largo leído sin mirar", "Ninguna preparación", "Las notas cortas ayudan a hablar con tus propias frases.")],
    op=("Escribe en tu cuaderno tu presentación de ejemplo en cinco líneas: saludo y nombre, país, oficio, edad y gustos, y cierre. Puedes inventar los datos. Léela en voz alta a otra persona o grábala, si quieres.",
        "Good morning, everyone. My name is Pedro. I'm from Chile. I'm a driver. I'm thirty years old. I like soccer. Thank you.",
        ["tiene saludo y nombre", "da país, oficio, edad y un gusto", "termina con Thank you"],
        ["una presentación de cinco líneas"],
        ["empezar con Thank you", "olvidar el saludo"],
        "Pregunta: «¿Tiene inicio, datos y cierre?»; revisa el orden."),
    reinforce="Lee en voz alta el modelo de esta clase y marca con colores el inicio, los datos y el cierre.",
    extend="Escribe dos inicios distintos de presentación, uno de mañana y uno de tarde.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras para presentar a una persona cercana: familia, vecinos y compañeros.",
    prior=["Me presento ante la clase.", "Uso he y she con to be.", "Conozco my, his y her."],
    explain=[
        "Para presentar a una persona cercana primero dices quién es para ti: my friend, my neighbor, my sister, my brother, my mother, my son, my daughter, my coworker. Coworker es compañero o compañera de trabajo.",
        "Una frase muy útil es Let me introduce my... Significa permíteme presentar a mi... Es una expresión completa: Let me introduce my neighbor, Carmen. Después das los datos con he o she: She is forty-five years old. She is from Peru.",
        "Para hablar de la familia de esa persona usa los posesivos: her son, her daughter, his sister. Fíjate en el posesivo: se elige según quien tiene la relación. Her son is Pedro significa el hijo de ella es Pedro.",
    ],
    vocab=[("friend", "amigo o amiga"), ("neighbor", "vecino o vecina"), ("sister", "hermana"), ("brother", "hermano"), ("mother", "madre"), ("son", "hijo"), ("daughter", "hija"), ("coworker", "compañero o compañera de trabajo")],
    worked=[
        ("Presentar a una persona", "Imagina que Luis es tu hermano, es conductor y debes presentarlo.", ["Uso la expresión: Let me introduce my brother, Luis.", "Digo el oficio con he: He is a driver.", "Reviso que he sea correcto para un hombre."], "Let me introduce my brother, Luis. He is a driver."),
        ("Usar el posesivo", "Carmen tiene una hija, Ana. ¿Cómo lo dices?", ["Carmen es mujer: uso her.", "El posesivo va antes del sustantivo: her daughter.", "Armo la oración: Her daughter is Ana."], "Her daughter is Ana."),
    ],
    mistakes=[("Decir «This is my neighbor, he» para una mujer.", "Se elige el pronombre equivocado.", "Para una mujer usa she: She is from Peru."),
              ("Decir «Let me introduce I brother».", "Se usa el pronombre I en vez del posesivo.", "Usa my antes del sustantivo: my brother.")],
    T=[
        ("abc", "{F} ¿Quién es Carmen para quien habla?", "Su vecina", "Su hermana", "Su madre", "El texto dice Let me introduce my neighbor, Carmen."),
        ("{F} ¿Cuántos años tiene Carmen? Escribe solo el número.", "45", "El texto dice forty-five years old."),
        ("abc", "{F} ¿Cuál es el oficio de Carmen?", "nurse", "driver", "baker", "El texto dice She is a nurse."),
        ("abc", "{F} ¿Quiénes son Ana y Pedro?", "Los hijos de Carmen", "Los hermanos de quien habla", "Los vecinos de Carmen", "El texto dice Her daughter is Ana y Her son is Pedro."),
        ("abc", "¿Qué significa «Let me introduce my...»?", "Permíteme presentar a mi...", "Quiero salir de aquí", "Necesito ayuda", "Es una expresión para presentar a alguien."),
        ("abc", "¿Cómo se dice «mi hija»?", "my daughter", "my sister", "my son", "Daughter es hija, y my va antes del sustantivo."),
        ("ab", "¿Cómo se dice «mi hijo»?", "my son", "my sun", "Son es hijo; sun significa sol y no corresponde."),
        ("abc", "Completa: «Marta is my sister. ___ is a cook.»", "She", "He", "I", "Marta es mujer, así que se usa she."),
        ("abc", "Completa: «This is my ___, Juan. We work together.»", "coworker", "neighbor", "daughter", "Coworker es la persona con quien trabajas."),
        ("abc", "¿Cuál oración presenta bien a un vecino llamado Luis?", "This is my neighbor, Luis.", "This is my neighbor, she.", "Luis is neighbor me.", "La presentación correcta usa this is, my y el nombre."),
        ("ab", "{F} Sobre el texto: «Her son is Pedro.» ¿De quién es hijo Pedro?", "De Carmen", "De quien habla", "Her significa de ella, y ella es Carmen."),
        ("abc", "Pedro es el hijo de Carmen. ¿Qué pronombre usas para hablar de él?", "He", "She", "They", "Pedro es un hombre, entonces se usa he."),
        ("abc", "{F} ¿Qué oración es falsa según el texto?", "Carmen is from Chile.", "Carmen is a nurse.", "Carmen likes music.", "El texto dice She is from Peru, no de Chile."),
    ],
    ctx=("abc", "Imagina que Luis es tu hermano y es conductor. Lo presentas a un grupo de compañeros. ¿Qué dices?", "Let me introduce my brother, Luis. He is a driver.", "Let me introduce my brother, Luis. She is a driver.", "Let me introduce I brother, Luis. He driver.", "La presentación correcta usa my, he para un hombre y el oficio."),
    sc=[("abc", "En Inglés: ¿qué significa «my neighbor»?", "Mi vecino o mi vecina", "Mi hermano", "Mi compañero de trabajo", "Neighbor es la persona que vive cerca de ti."),
        ("abc", "En Inglés: ¿cuál es el posesivo para una mujer?", "her", "his", "my", "Her se usa para algo de una mujer."),
        ("abc", "En Inglés: ¿cuál es una expresión para presentar a alguien?", "Let me introduce my friend.", "Where is my friend?", "I am my friend.", "Let me introduce... sirve para presentar a otra persona.")],
    op=("Escribe en tu cuaderno cinco oraciones para presentar a una persona cercana de ejemplo: quién es para ti, país, edad, oficio y un familiar suyo. Usa Let me introduce, he o she y un posesivo. Puedes decirlas en voz alta.",
        "Let me introduce my friend, Marcos. He is from Colombia. He is thirty-eight years old. He is a cook. His daughter is Lucía.",
        ["usa Let me introduce y my", "usa he o she correctamente", "usa un posesivo"],
        ["cinco oraciones sobre una persona"],
        ["usar he para una mujer", "olvidar my"],
        "Pregunta: «¿Elegiste he o she según la persona?»; revisa los posesivos."),
    reinforce="Di en voz baja quién es para ti cada persona cercana (familia, amistades, vecinos), con my.",
    extend="Escribe tres presentaciones breves de tres personas distintas, con una relación diferente cada vez.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy armo paso a paso la presentación de una persona cercana usando he o she, el verbo con -s y datos de trabajo y de vida.",
    prior=["Presento a otra persona con this is y he o she.", "Agrego -s con he y she.", "Niego con doesn't."],
    explain=[
        "Una presentación de otra persona sigue pasos. Paso 1, saludo: Good afternoon, everyone. Paso 2, quién es: This is Marcos. He is my friend. Paso 3, datos: país y edad con to be. Paso 4, trabajo y vida: He works in a restaurant. He lives in my neighborhood.",
        "Paso 5, gustos: He likes soccer, but he doesn't like cooking. Paso 6, cierre: Thank you. Fíjate en la -s final de works, lives y likes: con he y she el verbo lleva -s, y después de doesn't vuelve a la forma base.",
        "Para decir el lugar usa in o at: He works in a restaurant. She works at a hospital. Para el barrio usa in: He lives in my neighborhood. Estas pequeñas palabras de lugar se aprenden con ejemplos, no con reglas largas.",
    ],
    vocab=[("works", "trabaja"), ("lives", "vive"), ("restaurant", "restaurante"), ("neighborhood", "barrio"), ("in", "en (dentro de)"), ("at", "en (un lugar de trabajo)"), ("but", "pero"), ("hospital", "hospital")],
    worked=[
        ("Decir dónde trabaja", "Carmen trabaja en un hospital. ¿Cómo lo dices?", ["Es ella, entonces el verbo lleva -s: works.", "Para el lugar uso at o in: at a hospital.", "Armo la oración."], "She works at a hospital."),
        ("Negar un gusto", "A Marcos no le gusta cocinar, pero sí el fútbol.", ["Digo el gusto con -s: He likes soccer.", "Niego con doesn't y el verbo sin -s: he doesn't like cooking.", "Uno con but."], "He likes soccer, but he doesn't like cooking."),
    ],
    mistakes=[("Decir «Marcos live in my neighborhood».", "Se olvida la -s con Marcos, que es él.", "Con he y con un nombre de una persona agrega -s: Marcos lives in my neighborhood."),
              ("Decir «He is work in a restaurant».", "Se mezcla is con el verbo work.", "Di He works in a restaurant, sin is.")],
    T=[
        ("abc", "{F} ¿De dónde es Marcos?", "Colombia", "Chile", "Peru", "El texto dice He is from Colombia."),
        ("{F} ¿Cuántos años tiene Marcos? Escribe solo el número.", "38", "El texto dice thirty-eight years old."),
        ("abc", "{F} ¿Dónde trabaja Marcos?", "En un restaurante", "En un hospital", "En una tienda", "El texto dice He works in a restaurant."),
        ("abc", "{F} ¿Dónde vive Marcos?", "En el barrio de quien habla", "En otra ciudad", "En Colombia", "El texto dice He lives in my neighborhood."),
        ("abc", "Completa: «She ___ in a bakery.» (trabaja)", "works", "work", "working", "Con she el verbo lleva -s: works."),
        ("abc", "Completa: «They ___ in my neighborhood.» (viven)", "live", "lives", "living", "Con they el verbo no lleva -s."),
        ("ab", "Corrige: «Marcos live near my house.»", "Marcos lives near my house.", "Marcos is live near my house.", "Con un nombre de una sola persona el verbo lleva -s."),
        ("abc", "¿Cuál es el orden correcto de una presentación de otra persona?", "Saludo, quién es, datos, gustos, gracias", "Gracias, datos, saludo", "Gustos, saludo, edad", "El orden natural va del saludo al cierre."),
        ("Ordena las palabras: works / She / a / in / hospital", "She works in a hospital.", "El orden es sujeto, verbo con -s, el artículo y el lugar."),
        ("abc", "¿Cuál es la negativa de «He likes cooking»?", "He doesn't like cooking.", "He doesn't likes cooking.", "He don't like cooking.", "Con he se usa doesn't y el verbo en forma base."),
        ("abc", "{F} ¿Cuál oración es verdadera?", "Marcos doesn't like cooking.", "Marcos likes cooking.", "Marcos is from Peru.", "El texto dice he doesn't like cooking."),
        ("ab", "Quieres presentar a una amiga. ¿Qué pronombre usas?", "She", "He", "Para una mujer se usa she."),
        ("abc", "En «He works in a restaurant», ¿qué palabras indican el lugar?", "in a restaurant", "works", "He", "El lugar se dice con in y el nombre del sitio."),
    ],
    ctx=("abc", "Presentas a tu vecina Carmen: es de Peru, tiene 45 años, es enfermera y trabaja en un hospital. ¿Qué dices después del saludo?", "This is my neighbor, Carmen. She is from Peru. She is forty-five. She works in a hospital.", "This is my neighbor, Carmen. He is from Peru. She work in a hospital.", "Carmen is I neighbor. She are from Peru.", "La presentación correcta usa this is, she, to be y works con -s."),
    sc=[("abc", "En Inglés: ¿cuál es correcta?", "She works in a hospital.", "She work in a hospital.", "She is work in a hospital.", "Con she el verbo lleva -s y no lleva is."),
        ("abc", "En Inglés: ¿cómo dices «él vive en mi barrio»?", "He lives in my neighborhood.", "He live in my neighborhood.", "He is live my neighborhood.", "Con he el verbo lives lleva -s."),
        ("abc", "En Inglés: ¿cómo cierras tu presentación?", "Thank you.", "Good morning.", "Where is she?", "La frase Thank you agradece y termina la presentación.")],
    op=("Escribe en tu cuaderno una presentación de siete oraciones de una persona cercana de ejemplo, con los seis pasos: saludo, quién es, país y edad, trabajo, vida y gustos, y cierre. Léela en voz alta a otra persona.",
        "Good morning, everyone. This is Carmen. She is my neighbor. She is from Peru. She is forty-five years old. She works at a hospital. She likes music. Thank you.",
        ["tiene saludo, datos y cierre", "usa -s en works o lives", "usa he o she correctamente"],
        ["una presentación de siete a ocho oraciones"],
        ["olvidar la -s", "usar he para una mujer"],
        "Pregunta: «¿Tienes los seis pasos?»; revisa las -s."),
    reinforce="Cuenta en voz baja los seis pasos de una presentación y di una frase para cada uno.",
    extend="Escribe dos presentaciones breves de dos personas con trabajos distintos.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico ordenando una presentación, corrigiendo errores y escuchando con atención a otras personas.",
    prior=["Conozco los seis pasos de una presentación.", "Uso -s y doesn't.", "Reconozco números como forty-five o sixty-eight."],
    explain=[
        "Para practicar, ordena las oraciones de una presentación: saludo, quién es, país, edad, gustos y cierre. Si una oración está fuera de lugar, la presentación se entiende peor. Fíjate en las palabras clave de cada oración para saber su lugar.",
        "También practica corregir errores comunes: la -s con he y she (She likes), el verbo to be para la edad (She is thirty-three), y los posesivos (her, his). Cada error corregido te hace hablar con más seguridad.",
        "Hablar bien también es escuchar. Mira a quien presenta, no hables mientras alguien habla y agradece al final. Si no entiendes, pide con cortesía: Can you repeat that, please? Esa expresión completa sirve en el trabajo y en la vida diaria.",
    ],
    vocab=[("greeting", "saludo"), ("closing", "cierre"), ("order", "orden"), ("listen", "escuchar"), ("repeat", "repetir"), ("please", "por favor"), ("Can you repeat that, please?", "¿Puedes repetir eso, por favor?"), ("age", "edad")],
    worked=[
        ("Ordenar oraciones", "Oraciones: «Thank you. / This is my friend, Lucía. / Good morning, everyone.» Ordénalas.", ["El saludo va primero: Good morning, everyone.", "Después va quién es: This is my friend, Lucía.", "El cierre va al final: Thank you."], "Good morning, everyone. This is my friend, Lucía. Thank you."),
        ("Corregir un error", "Un compañero dice: «She like dancing. She have thirty-three.» Corrígelo.", ["Con she el verbo lleva -s: She likes dancing.", "La edad se dice con to be: She is thirty-three.", "Reviso las dos oraciones."], "She likes dancing. She is thirty-three."),
    ],
    mistakes=[("Poner el cierre en medio de la presentación.", "No se piensa en el orden de las partes.", "Deja Thank you para el final."),
              ("Interrumpir mientras otra persona presenta.", "Se quiere ayudar o comentar de inmediato.", "Escucha hasta el final y luego agradece o pregunta con cortesía.")],
    T=[
        ("abc", "{F} ¿Qué oración va primero?", "Good morning, everyone.", "Thank you.", "She likes dancing.", "El saludo es la primera parte y abre la presentación."),
        ("abc", "{F} ¿Qué oración va en último lugar?", "Thank you.", "She is from Bolivia.", "This is my friend, Lucía.", "El cierre es la última parte y va al final."),
        ("abc", "{F} ¿Qué oración presenta a Lucía?", "This is my friend, Lucía.", "She is thirty-three years old.", "She likes dancing.", "Esa oración dice quién es Lucía para quien habla."),
        ("{F} ¿Cuántos años tiene Lucía? Escribe solo el número.", "33", "La oración 4 dice thirty-three years old."),
        ("{F} ¿De qué país es Lucía? Escribe una palabra.", "Bolivia", "La oración 6 dice She is from Bolivia."),
        ("ab", "{F} Entre las oraciones 2 y 3, ¿cuál va primero?", "La 3: Good morning, everyone.", "La 2: This is my friend, Lucía.", "El saludo va antes que la presentación de la persona."),
        ("abc", "Completa: «She ___ thirty-three.» (tiene 33 años)", "is", "has", "does", "La edad se dice con to be: she is."),
        ("abc", "Corrige el error: «She like dancing.»", "She likes dancing.", "She is like dancing.", "She do like dancing.", "Con she el verbo lleva -s."),
        ("ab", "No escuchaste bien la presentación de un compañero. ¿Qué dices?", "Can you repeat that, please?", "You repeat now.", "Can you repeat that, please? pide con cortesía que repitan."),
        ("abc", "Un compañero termina su presentación. ¿Qué haces como audiencia?", "Escuchar con respeto y agradecer", "Hablar fuerte con otra persona", "Salir de la sala", "Escuchar y agradecer es respetuoso con quien presenta."),
        ("Ordena las palabras: likes / She / dancing", "She likes dancing.", "El orden es sujeto, verbo con -s y la actividad."),
        ("abc", "Marcos is from Colombia. ¿Qué pregunta responde esto?", "Where is he from?", "How old is he?", "What does he like?", "Is from Colombia da el origen, y el origen se pregunta con where."),
        ("abc", "¿Qué número es «sixty-eight»?", "68", "86", "18", "Sixty es 60 y eight es 8; juntos son 68."),
    ],
    ctx=("abc", "Preparas la presentación de una vecina y quieres terminar bien. ¿Qué oración eliges para el cierre?", "Thank you.", "Good morning.", "Where are you from?", "El cierre agradece a la audiencia."),
    sc=[("abc", "En Inglés: ¿qué oración va primero en una presentación?", "El saludo", "El cierre", "Los gustos", "El saludo es la primera parte y abre la presentación."),
        ("abc", "En Inglés: ¿cuál es correcta?", "She is thirty-three.", "She has thirty-three.", "She do thirty-three.", "La edad se dice con to be."),
        ("abc", "En Inglés: ¿qué frase usas para pedir que repitan?", "Can you repeat that, please?", "Where is she from?", "Thank you very much.", "Esa frase pide con cortesía que repitan.")],
    op=("Escribe en tu cuaderno una presentación de seis oraciones de una persona cercana de ejemplo, pero en desorden. Dásela a otra persona para que la ordene (o ordénala tú después de un rato) y anota si el orden final es correcto.",
        "Desordenado: Thank you. / He likes soccer. / Good morning, everyone. / This is my brother, Diego. / He is from Chile. / He is twenty-nine. Ordenado: Good morning, everyone. This is my brother, Diego. He is from Chile. He is twenty-nine. He likes soccer. Thank you.",
        ["las oraciones cubren saludo, quién es, país, edad, gustos y cierre", "el orden final es correcto", "usa he o she bien"],
        ["una presentación desordenada y su orden correcto"],
        ["poner el cierre en medio", "olvidar la -s"],
        "Pregunta: «¿El saludo quedó primero y el cierre al final?»; revisa las -s."),
    reinforce="Corrige en voz baja tres oraciones con errores de -s o de to be que escribas tú mismo.",
    extend="Escribe una lista de cinco cosas que haces cuando escuchas la presentación de otra persona.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy preparo una presentación de una persona cercana a partir de una tarjeta de datos y la practico para decirla frente a la clase.",
    prior=["Conozco los seis pasos de una presentación.", "Uso he o she, -s y doesn't.", "Sé usar notas con palabras clave."],
    explain=[
        "Para preparar tu presentación, empieza con una tarjeta de datos: nombre, país, edad, oficio, lugar de trabajo y gustos. Después escribe una oración corta con cada dato, usando he o she. Así tienes tu texto sin copiar uno ajeno.",
        "Luego practica en voz alta tres veces: la primera con el texto, la segunda con notas de palabras clave y la tercera mirando a la persona que te escucha. Habla despacio: speak slowly es una expresión útil. Si quieres, grábate; es opcional.",
        "El día de la presentación, saluda, di quién es esa persona, entrega los datos y cierra con Thank you. Prepárate para una pregunta sencilla del grupo, como Does he like music? y responde con una respuesta corta. Usa datos de ejemplo si no quieres hablar de una persona real.",
    ],
    vocab=[("card", "tarjeta"), ("company", "empresa"), ("notes", "notas"), ("slowly", "despacio"), ("clearly", "con claridad"), ("question", "pregunta"), ("ready", "listo, lista"), ("practice", "practicar, práctica")],
    worked=[
        ("De la tarjeta a las oraciones", "Tarjeta: name: Rosa; from: Peru; age: 29; job: baker. ¿Cómo la conviertes en oraciones?", ["Nombre: This is my neighbor, Rosa.", "País y edad: She is from Peru. She is twenty-nine years old.", "Oficio: She is a baker."], "This is my neighbor, Rosa. She is from Peru. She is twenty-nine years old. She is a baker."),
        ("Responder una pregunta", "Un compañero pregunta: «Does Rosa like plants?». Rosa, según tu tarjeta, ama las plantas.", ["Es ella, entonces la pregunta es con Does.", "La respuesta corta es Yes, she does.", "Puedo agregar: She loves plants."], "Yes, she does."),
    ],
    mistakes=[("Escribir la presentación y leerla sin mirar a nadie.", "Se teme olvidar las frases.", "Usa notas con palabras clave y mira a la clase de vez en cuando."),
              ("Hablar muy rápido por los nervios.", "Se quiere terminar pronto.", "Respira y habla despacio: slowly. Es mejor que te entiendan.")],
    T=[
        ("abc", "{F} ¿Cuál oración usa bien la tarjeta sobre el país de Luis?", "He is from Chile.", "He is from Peru.", "She is from Chile.", "La tarjeta dice From: Chile y Luis es un hombre."),
        ("abc", "{F} ¿Cuál oración expresa su edad?", "He is fifty-two years old.", "He is twenty-five years old.", "He has fifty-two years.", "La tarjeta dice Age: 52, que se dice fifty-two."),
        ("{F} ¿Qué oficio tiene Luis? Escribe una palabra en inglés.", "driver", "La tarjeta dice Job: driver, que significa conductor."),
        ("abc", "{F} ¿Dónde trabaja Luis?", "En una empresa de buses", "En un restaurante", "En un hospital", "La tarjeta dice Place of work: a bus company."),
        ("abc", "{F} ¿Qué oración dice que a Luis no le gusta cocinar?", "He doesn't like cooking.", "He don't like cooking.", "He not like cooking.", "Con he la negación es doesn't y el verbo sin -s."),
        ("abc", "{F} ¿Qué oración dice sus gustos?", "He likes soccer and music.", "He like soccer and music.", "He is like soccer and music.", "Con he el verbo lleva -s: likes."),
        ("ab", "Antes de la presentación, ¿qué ayuda más?", "Practicar en voz alta tres veces", "Leer solo una vez en silencio", "Practicar en voz alta ayuda a decir las frases con confianza."),
        ("abc", "Un compañero te pregunta «Does Luis like music?». ¿Cuál es la respuesta correcta según la tarjeta?", "Yes, he does.", "No, he doesn't.", "Yes, he is.", "La tarjeta dice Likes: soccer and music, así que la respuesta es yes."),
        ("Ordena las palabras: at / works / He / a / bus / company", "He works at a bus company.", "El orden es sujeto, verbo con -s, el lugar y el nombre del sitio."),
        ("abc", "Eres audiencia. ¿Qué pregunta de seguimiento haces a quien presentó a Luis?", "Does he like soccer?", "Is he from Luis?", "Do he like music?", "Con he se usa Does y el verbo sin -s."),
        ("ab", "Presentas a Luis así: «This is Luis. He is fifty-two. Thank you.» ¿Qué falta para estar completa?", "El país, el oficio y los gustos", "Nada, está completa", "Una presentación completa da varios datos antes del cierre."),
        ("abc", "¿Cuál oración está bien escrita?", "He works at a bus company.", "He work at a bus company.", "He is work at a bus company.", "Con he el verbo lleva -s y no lleva is."),
        ("{F} ¿Cuál es el apellido de Luis? Escríbelo.", "Rojas", "La tarjeta dice Name: Luis Rojas, así que el apellido es Rojas."),
    ],
    ctx=("abc", "Presentarás a tu vecina Rosa (tarjeta de ejemplo: from Peru, 29, baker, likes plants). ¿Qué dices al empezar?", "Good morning, everyone. This is my neighbor, Rosa.", "Thank you, everyone. Goodbye.", "My neighbor Rosa I am.", "El inicio saluda y presenta a la persona con this is."),
    sc=[("abc", "En Inglés: ¿qué haces antes de presentar?", "Prepararte con una tarjeta de datos y practicar en voz alta", "Memorizar sin practicar", "Improvisar sin notas", "Una tarjeta y práctica en voz alta te dan seguridad."),
        ("abc", "En Inglés: ¿cómo hablas cuando presentas?", "Despacio y con claridad", "Muy rápido", "Muy bajo", "Despacio y con claridad ayuda a que te entiendan."),
        ("abc", "En Inglés: ¿cuál respuesta corta es correcta para «Does she like plants?»?", "Yes, she does.", "Yes, she likes.", "Yes, she is.", "La respuesta corta repite la ayuda does de la pregunta.")],
    op=("Prepara en tu cuaderno una tarjeta de datos de una persona cercana de ejemplo (nombre, país, edad, oficio, gustos) y escribe siete oraciones de presentación a partir de ella. Practica en voz alta tres veces con una persona de confianza; si quieres, grábate. Usa datos de ejemplo.",
        "Card: Name: Rosa. From: Peru. Age: 29. Job: baker. Likes: plants. Text: Good morning, everyone. This is my neighbor, Rosa. She is from Peru. She is twenty-nine years old. She is a baker. She likes plants. Thank you.",
        ["tiene tarjeta con cinco datos", "las oraciones usan he o she y la -s", "tiene inicio y cierre", "se practicó tres veces"],
        ["una tarjeta de datos y siete oraciones"],
        ["olvidar la -s", "no practicar en voz alta"],
        "Pregunta: «¿Qué frase te costó más y cómo la mejorarías?»; escucha una pregunta de la persona que te escucha."),
    reinforce="Practica la presentación una vez más en voz alta con tus notas, hablando despacio.",
    extend="Prepara una segunda tarjeta y presentación de otra persona de ejemplo con un oficio distinto.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy escucho y comento la presentación de un compañero con una pauta, me autoevalúo y decido qué practicar.",
    prior=["Presento a una persona con seis pasos.", "Hago preguntas con Do y Does.", "Respeto a quien habla."],
    explain=[
        "Para revisar una presentación usa una pauta simple: saludo, nombre, país, edad, oficio o trabajo, gustos y cierre. Mientras escuchas, marca con un visto cada parte que oyes. Así sabes qué tan completa fue.",
        "Cuando comentes, empieza por lo que salió bien: She speaks clearly, por ejemplo. Después da una sugerencia amable: Please speak slowly. Los comentarios son para ayudar, no para juzgar a la persona. Agradece siempre al final.",
        "Para decidir tus próximos pasos, anota tres cosas que haces bien y una que quieres practicar: la -s, los números, los saludos. Practicar con personas reales, aunque sea poco cada día, mejora tu inglés más que memorizar listas.",
    ],
    vocab=[("clearly", "con claridad"), ("slowly", "despacio"), ("greeting", "saludo"), ("closing", "cierre"), ("store", "tienda"), ("brother", "hermano"), ("walking", "caminar"), ("reading", "leer")],
    worked=[
        ("Marcar la pauta", "Escuchas: «Good evening, everyone. This is my brother, Diego. He is from Chile.» ¿Qué partes de la pauta oyes?", ["Oigo el saludo: Good evening, everyone.", "Oigo el nombre y quién es: my brother, Diego.", "Oigo el país: from Chile."], "Saludo, nombre y país"),
        ("Dar un comentario amable", "Un compañero habló muy rápido pero dijo todo bien. ¿Qué dices?", ["Primero lo que salió bien: Your information is clear.", "Luego una sugerencia: Please speak slowly.", "Termino agradeciendo: Thank you."], "Your information is clear. Please speak slowly. Thank you."),
    ],
    mistakes=[("Comentar solo lo que estuvo mal.", "Se cree que corregir es lo más importante.", "Empieza por algo que salió bien y luego agrega una sugerencia."),
              ("No marcar nada al escuchar.", "Se confía en la memoria.", "Usa la pauta y marca cada parte que oyes.")],
    T=[
        ("abc", "{F} ¿Cómo se llama el hermano de quien habla?", "Diego", "Marcos", "Luis", "El texto dice This is my brother, Diego."),
        ("abc", "{F} ¿De qué país es Diego?", "Chile", "Peru", "Bolivia", "El texto dice He is from Chile."),
        ("{F} ¿Cuántos años tiene Diego? Escribe solo el número.", "29", "El texto dice twenty-nine years old."),
        ("abc", "{F} ¿Dónde trabaja Diego?", "En una tienda", "En un hospital", "En un restaurante", "El texto dice He works in a store."),
        ("abc", "{F} ¿Qué no le gusta a Diego?", "Leer", "Caminar", "Escuchar música", "El texto dice he doesn't like reading."),
        ("abc", "{F} ¿Qué partes de la pauta NO aparecen en el texto?", "Ninguna: están todas", "El cierre", "El saludo", "El texto trae saludo, nombre, país, edad, trabajo, gustos y cierre."),
        ("ab", "{F} ¿Cuál oración es verdadera?", "Diego likes walking.", "Diego likes reading.", "El texto dice He likes walking, but he doesn't like reading."),
        ("abc", "Completa: «My brother ___ in a store.» (trabaja)", "works", "work", "working", "Con una sola persona, my brother, el verbo lleva -s."),
        ("Ordena las palabras para un comentario amable que empiece con Please: slowly / speak / Please", "Please speak slowly.", "La cortesía empieza con Please y sigue la instrucción."),
        ("abc", "Un compañero presentó muy bien. ¿Qué comentario amable haces?", "You speak clearly. Thank you.", "Your English is bad.", "I don't like it.", "Un comentario amable resalta algo bueno y agradece."),
        ("ab", "¿Cuál es correcta?", "He doesn't like reading.", "He doesn't likes reading.", "Después de doesn't el verbo vuelve a la forma base."),
        ("abc", "¿Cuál es el mejor saludo para una presentación a las 7 de la noche?", "Good evening, everyone.", "Good morning, everyone.", "Good night, everyone.", "A esa hora se usa good evening."),
        ("abc", GUION + "My mother is from Peru. She is sixty-two years old. She works in a bakery. ¿Dónde trabaja la madre?", "Una panadería", "Un hospital", "Una tienda", "El guion dice She works in a bakery."),
    ],
    ctx=("abc", "Después de la presentación de un compañero, ¿cuál es el mejor comentario?", "Your presentation is clear. Please speak slowly. Thank you.", "It's bad. Stop.", "I don't listen.", "El comentario correcto resalta algo bueno, sugiere y agradece."),
    sc=[("abc", "En Inglés: ¿qué frase sirve para cerrar una presentación?", "Thank you.", "Good morning.", "I'm from Chile.", "La frase Thank you cierra y agradece a la audiencia."),
        ("abc", "En Inglés: ¿cómo pides con cortesía que hablen más despacio?", "Please speak slowly.", "Speak now.", "You speak fast.", "Please speak slowly es una petición cortés."),
        ("abc", "En Inglés: ¿qué haces al escuchar con una pauta?", "Marcar cada parte que oyes", "Memorizar todo", "Hablar con otro", "La pauta ayuda a notar si la presentación está completa.")],
    op=("Presenta en voz alta, ante la clase o ante una persona de confianza, a una persona cercana de ejemplo en siete oraciones: saludo, nombre, país, edad, trabajo, gustos y cierre. Pide a quien te escucha que marque la pauta y que te diga una cosa buena y una sugerencia. Anota qué quieres practicar. Si quieres, grábate.",
        "Good evening, everyone. This is my sister, Marta. She is from Chile. She is thirty-five years old. She works in a store. She likes plants, but she doesn't like cooking. Thank you.",
        ["tiene saludo, datos y cierre", "usa he o she, la -s y doesn't", "habla despacio y con claridad", "anota qué practicar"],
        ["una presentación de siete oraciones, la pauta marcada y una nota de qué practicar"],
        ["olvidar la -s", "hablar demasiado rápido"],
        "Pregunta: «¿Qué dos cosas hiciste bien y qué quieres practicar?»; si es posible, escucha la grabación y compárala con la pauta."),
    reinforce="Vuelve a decir tu presentación una vez más, hablando más despacio.",
    extend="Prepara y practica una presentación de otra persona cercana en diez oraciones.",
)

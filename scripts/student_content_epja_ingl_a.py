"""Inglés EPJA Nivel 2, módulo 1 (parte 1): OAD-01, saludar y entregar información básica sobre sí mismos y otras personas. Todos los textos y guiones son inventados y se leen en papel."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-01"

F1 = ("Transcripción de un diálogo de ejemplo (inventado), primer día en un taller: Carlos: Good morning! My name is Carlos. / Marta: Hello, Carlos. I'm Marta. Nice to meet you. / "
      "Carlos: Nice to meet you, too. How are you? / Marta: I'm fine, thanks. And you? / Carlos: I'm fine. See you later, Marta! / Marta: Goodbye, Carlos.")

F2 = ("Transcripción de un mensaje de bienvenida (inventado): Hello, everyone. I'm Ana. I'm from Chile. I'm a cook. I'm thirty-two years old. This is Mr. Lopez. "
      "He's a driver. He's from Peru. He's fifty years old. "
      "Formulario de ejemplo: Name: Rosa Diaz / Country: Bolivia / Job: baker / Age: 41.")

F3 = ("Presentación de ejemplo (inventada): Carlos: Rosa, this is my friend, Mary. She's from Colombia. She isn't a nurse. She's a baker. / Rosa: Hello, Mary! Are you new here? / Mary: Yes, I am. Nice to meet you.")

F4 = ("Transcripción de una llamada de ejemplo (inventada): Receptionist: What's your name? / Caller: My name is Peter Moreno. / Receptionist: How do you spell your last name? / Caller: M-O-R-E-N-O. / "
      "Receptionist: How old are you? / Caller: I'm forty-five years old. / Receptionist: Thank you, Peter.")

F5 = ("Transcripción de un mensaje de voz de ejemplo (inventado): Hello, Mr. Lopez. This is Ana from the warehouse. Good afternoon! I'm at the door. The meeting is at nine o'clock. "
      "It's cold and rainy today. Please wait. See you soon. "
      "Gafete de ejemplo: Name: Peter Moreno / Job: driver / Country: Chile / Age: 38.")

F6 = ("Tarjeta de bienvenida de ejemplo (inventada): Hello! I'm Marta. I'm forty years old. I'm from Bolivia. I'm a cook. This is John. He's a driver. He's thirty-six. Good morning, Peter. Nice to meet you.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy saludo según la hora del día, me presento con mi nombre y reconozco frases de despedida en un diálogo corto.",
    prior=["Reconozco palabras en inglés que veo en la calle, como hello o bye.", "Sé decir mi nombre en voz alta.", "Puedo leer un texto corto con ayuda de otra persona."],
    explain=[
        "Tú ya usas el inglés más de lo que crees: hello, ok, bye. Hoy lo ordenamos. En inglés, el saludo cambia según la hora: good morning se usa en la mañana, good afternoon en la tarde y good evening al caer la tarde y en la noche.",
        "Para presentarte di my name is y tu nombre, o la forma corta I'm y tu nombre. Para responder a una presentación di nice to meet you, que significa mucho gusto. Si alguien pregunta how are you?, puedes decir I'm fine, thanks.",
        "Para despedirte usa goodbye, see you later (hasta luego) o good night cuando alguien se va a dormir. Antes de leer o escuchar un diálogo, mira el título y predice de qué tratará: eso ayuda a entender las palabras clave.",
    ],
    vocab=[("hello", "hola"), ("good morning", "buenos días (en la mañana)"), ("good afternoon", "buenas tardes (después del mediodía)"), ("good evening", "buenas tardes o noches (al caer el día)"), ("my name is", "mi nombre es"), ("nice to meet you", "mucho gusto"), ("goodbye", "adiós"), ("see you later", "hasta luego")],
    worked=[
        ("Elegir el saludo", "Llegas a un taller a las 9 de la mañana y saludas a un compañero. ¿Qué dices?", ["Miro la hora: 9 de la mañana es la mañana.", "El saludo de la mañana es good morning.", "Agrego mi nombre: My name is Rosa."], "Good morning! My name is Rosa."),
        ("Responder a una presentación", "Una persona nueva dice: «I'm Peter. Nice to meet you.» Quieres responder con cortesía.", ["Entiendo que Peter se presenta y dice mucho gusto.", "Respondo con la misma cortesía: nice to meet you, too.", "Digo mi nombre: I'm Ana."], "Nice to meet you, too. I'm Ana."),
    ],
    mistakes=[("Decir «Good night» al llegar a una reunión de la tarde.", "En español «buenas noches» sirve al llegar; en inglés good night es para despedirse o ir a dormir.", "Al llegar de noche di good evening; good night déjalo para la despedida."),
              ("Decir «My name are Ana».", "Se mezcla el verbo con el plural; name es una sola cosa.", "Con name usa is: My name is Ana.")],
    T=[
        ("ab", "{F} En el diálogo, ¿cómo se presenta Carlos?", "My name is Carlos.", "My name are Carlos.", "Con name, una sola cosa, el verbo es is y no are."),
        ("abc", "{F} ¿Qué momento del día indica el saludo Good morning?", "La mañana", "La tarde", "La noche", "Morning significa mañana, la primera parte del día."),
        ("{F} Marta responde a la pregunta How are you? con I'm ... Escribe la palabra que falta, en inglés.", "fine", "En el diálogo Marta dice I'm fine, thanks, es decir, estoy bien."),
        ("abc", "Entras a una oficina a las 3 de la tarde. ¿Qué saludo usas?", "Good afternoon", "Good morning", "Good night", "Después del mediodía y antes del atardecer se dice good afternoon."),
        ("abc", "Alguien te presenta a una persona y quieres decir «mucho gusto». ¿Qué dices?", "Nice to meet you.", "See you later.", "Good night.", "Nice to meet you es la fórmula para decir mucho gusto."),
        ("ab", "Llegas a una reunión a las 7 de la noche. ¿Qué saludo usas?", "Good evening.", "Good morning.", "Good evening se usa al caer el día y en la noche; good morning solo en la mañana."),
        ("abc", "Un diálogo se llama «First day at work». Antes de leerlo, ¿qué es más probable que encuentres?", "Saludos y presentaciones de personas nuevas", "Una receta de cocina", "Un pronóstico del tiempo", "Predecir con el título ayuda: un primer día de trabajo trae saludos y presentaciones."),
        ("abc", "Mary dice «Goodbye, Mr. Lopez!». ¿Qué hace Mary?", "Se despide", "Saluda por primera vez", "Pregunta cómo está", "Goodbye es una despedida, no un saludo de llegada."),
        ("abc", "Completa: «Hello! My ___ is Ana.»", "name", "you", "fine", "La frase para presentarse es my name is más el nombre."),
        ("Ordena las palabras para presentarte: is / My / John / name", "My name is John.", "La frase empieza con My, sigue name, luego is y al final el nombre."),
        ("ab", "Rosa dice «Good morning» a las 4 de la tarde al llegar a la oficina. ¿Es correcto?", "No: a esa hora corresponde good afternoon", "Sí: good morning sirve para todo el día", "Good morning se usa solo hasta cerca del mediodía; después se cambia el saludo."),
        ("abc", "Alguien te dice «Nice to meet you, Ana». ¿Qué respuesta es natural?", "Nice to meet you, too.", "Good morning.", "I'm fine, thanks.", "Se responde con la misma fórmula y se agrega too, que significa también."),
        ("abc", "{F} Según el diálogo, ¿quién dice «See you later»?", "Carlos", "Marta", "Nadie", "Carlos se despide con See you later, y Marta responde con Goodbye."),
    ],
    ctx=("abc", "Primer día en una bodega, 8 de la mañana. Un nuevo compañero te dice: «Hello, I'm Peter. Nice to meet you.» ¿Qué respuesta es completa y natural?", "Good morning, Peter. I'm Rosa. Nice to meet you, too.", "Good night, Peter. Nice to meet you.", "See you later, Peter. I'm fine.", "La respuesta correcta saluda según la hora, dice el nombre y devuelve la cortesía."),
    sc=[("En Inglés: ¿qué saludo corresponde a la mañana?", "Good morning", "Morning significa mañana y se usa hasta cerca del mediodía."),
        ("En Inglés: ¿qué frase sirve para presentarte?", "My name is... o I'm...", "Estas dos formas dan tu nombre al presentarte."),
        ("En Inglés: antes de escuchar un diálogo, ¿qué estrategia ayuda a entenderlo?", "Mirar el título y predecir de qué tratará", "Predecir activa lo que ya sabes y prepara para las palabras clave.")],
    op=("Escribe en tu cuaderno un diálogo de cuatro líneas entre tú y una persona nueva en un taller a las 10 de la mañana: saludo, tu nombre, nice to meet you y una despedida. Léelo en voz alta si quieres; puedes grabarlo, no es obligatorio. Usa un nombre de ejemplo.",
        "Rosa: Good morning! My name is Rosa. / Pedro: Hello, Rosa. I'm Pedro. Nice to meet you. / Rosa: Nice to meet you, too. See you later! / Pedro: Goodbye!",
        ["usa el saludo de la mañana", "dice su nombre con My name is o I'm", "responde con nice to meet you", "termina con una despedida"],
        ["un diálogo de cuatro líneas con las cuatro frases"],
        ["usar good night para llegar", "olvidar el verbo is o am"],
        "Pregunta: «¿El saludo corresponde a la hora?»; si el diálogo está completo, escribe una segunda versión a las 6 de la tarde."),
    reinforce="Saluda en inglés, en voz baja, a tres personas distintas de tu día y di tu nombre cada vez.",
    extend="Escribe cómo saludarías a las 8 de la mañana, a las 2 de la tarde y a las 8 de la noche.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras para decir de qué país soy, a qué me dedico y cuántos años tengo.",
    prior=["Sé decir mi nombre en inglés.", "Conozco los saludos según la hora del día.", "Sé decir en español de dónde soy y a qué me dedico."],
    explain=[
        "Para dar información básica en inglés usamos tres frases con I am o su forma corta I'm. Para el país: I'm from Chile. Para el oficio: I'm a cook. Para la edad: I'm thirty-two years old.",
        "Fíjate en dos diferencias con el español. Antes del oficio va a: I'm a driver, no I'm driver. Y para la edad se usa el verbo to be: I'm thirty years old, no I have thirty years.",
        "En un formulario aparecen las palabras name (nombre), country (país), job (oficio) y age (edad). En esta clase leemos un mensaje de bienvenida y un formulario de ejemplo. Subraya las palabras clave: país, oficio y número.",
    ],
    vocab=[("country", "país"), ("job", "trabajo, oficio"), ("from", "de (origen)"), ("cook", "cocinero o cocinera"), ("driver", "conductor o conductora"), ("baker", "panadero o panadera"), ("nurse", "enfermero o enfermera"), ("years old", "años de edad")],
    worked=[
        ("Leer un formulario", "Formulario de ejemplo: Name: Rosa Diaz / Country: Bolivia / Job: baker / Age: 41. ¿Cómo lo dice Rosa en una oración?", ["Busco country: Bolivia, entonces I'm from Bolivia.", "Busco job: baker, entonces I'm a baker.", "Busco age: 41, entonces I'm forty-one years old."], "I'm from Bolivia. I'm a baker. I'm forty-one years old."),
        ("Decir mis datos", "Imagina que eres panadero o panadera, de Chile, y que tienes 29 años. ¿Cómo lo dices?", ["Para el país uso I'm from Chile.", "Para el oficio pongo a antes: I'm a baker.", "Para la edad uso to be: I'm twenty-nine years old."], "I'm from Chile. I'm a baker. I'm twenty-nine years old."),
    ],
    mistakes=[("Decir «I have thirty years».", "En español se tiene edad; en inglés se es una edad.", "Usa to be: I'm thirty years old."),
              ("Decir «I'm driver».", "En español no usamos un antes del oficio; en inglés sí.", "Pon a antes del oficio: I'm a driver.")],
    T=[
        ("abc", "{F} ¿De qué país es Ana?", "Chile", "Peru", "Bolivia", "En el mensaje Ana dice I'm from Chile."),
        ("abc", "{F} ¿Cuál es el oficio de Mr. Lopez?", "driver", "cook", "baker", "El mensaje dice He's a driver, es decir, es conductor."),
        ("{F} ¿Cuántos años tiene Ana? Escribe solo el número.", "32", "Ana dice thirty-two years old, que es treinta y dos."),
        ("ab", "{F} ¿Qué dice el formulario sobre Rosa Diaz?", "She is a baker from Bolivia.", "She is a nurse from Bolivia.", "El formulario anota Job: baker y Country: Bolivia."),
        ("abc", "¿Cómo se dice «Tengo cuarenta años» en inglés?", "I'm forty years old.", "I have forty years old.", "I'm forty year.", "En inglés la edad se dice con to be y se agrega years old."),
        ("abc", "Completa: «I'm ___ Peru.» (soy de Perú)", "from", "to", "by", "La palabra from indica el origen o país de procedencia."),
        ("ab", "Marta es enfermera. ¿Cómo lo dice?", "I'm a nurse.", "I'm nurse.", "En inglés se usa a antes de un oficio contable."),
        ("Escribe en inglés sin contracciones: «Tú eres conductor» (usa driver).", "You are a driver.", "Con you el verbo to be es are y antes del oficio va a."),
        ("abc", "{F} Mr. Lopez tiene cincuenta años. ¿Cómo se escribe 50 en inglés?", "fifty", "fifteen", "five", "Fifty termina en -ty y es 50; fifteen, con -teen, es 15."),
        ("abc", "En un formulario aparece «Job: baker». ¿Qué dato se pide en Job?", "El oficio", "El país", "La edad", "En un formulario, job significa trabajo u oficio de la persona."),
        ("abc", "Un formulario dice «Country: cook». ¿Qué error hay?", "Se puso un oficio donde se pide el país", "Se puso la edad donde se pide el oficio", "No hay ningún error", "Cook es un oficio y country pide el país, como Chile."),
        ("abc", "{F} En «He's a driver», ¿qué palabra reemplaza a Mr. Lopez?", "He", "She", "I", "He se usa para un hombre y reemplaza su nombre."),
        ("abc", GUION + "I'm thirty years old. ¿Qué edad se dice?", "30", "13", "3", "Thirty con -ty es 30; thirteen, con -teen, es 13."),
    ],
    ctx=("abc", "En una agencia de empleo de ejemplo te dicen: «Tell me about you.» ¿Qué respuesta es la más completa y correcta?", "I'm Rosa. I'm from Chile. I'm a cook. I'm thirty-five years old.", "I Rosa. I from Chile. I cook. I have thirty-five years.", "My name Chile. I'm cook. Thirty-five.", "La buena respuesta usa I'm, el país con from, a antes del oficio y la edad con years old."),
    sc=[("abc", "En Inglés: ¿cómo se dice «soy de Chile»?", "I'm from Chile.", "I'm of Chile.", "I have Chile.", "Para el origen se usa from."),
        ("abc", "En Inglés: ¿cuál es correcta para decir que eres conductor?", "I'm a driver.", "I'm driver.", "I have driver.", "Antes del oficio va la palabra a."),
        ("En Inglés: ¿cómo se dice «tengo veinte años»?", "I'm twenty years old.", "La edad se expresa con to be y years old.")],
    op=("Escribe en tu cuaderno tus datos de ejemplo en tres frases en inglés: de qué país eres, a qué te dedicas y cuántos años tienes. Puedes inventar los datos. Léelas en voz alta si quieres.",
        "I'm from Chile. I'm a cook. I'm thirty-two years old.",
        ["usa I'm from con un país", "pone a antes del oficio", "dice la edad con years old"],
        ["tres frases escritas con datos de ejemplo"],
        ["escribir I have y la edad", "olvidar a antes del oficio"],
        "Pregunta: «¿Dijiste la edad con to be?»; revisa la frase del oficio."),
    reinforce="Lee en voz alta el formulario de ejemplo de esta clase y di cada dato en una oración completa.",
    extend="Escribe los datos de dos personas de ejemplo (país, oficio y edad) con tres oraciones cada una.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo el verbo to be paso a paso: afirmo, niego y pregunto, y presento a otra persona con he o she.",
    prior=["Digo mi país, oficio y edad con I'm.", "Conozco la frase My name is.", "Sé que en español hay ser y estar."],
    explain=[
        "El verbo to be significa ser o estar y cambia según quién habla: I am, you are, he is, she is, we are, they are. En conversación usamos formas cortas: I'm, you're, he's, she's, we're, they're.",
        "Para negar agrega not después del verbo: She is not o She isn't. Para preguntar, el verbo pasa al principio: You are new, y la pregunta es Are you new? La respuesta corta repite el verbo: Yes, I am. No, I'm not.",
        "Para presentar a otra persona, di this is y el nombre. Después usa he para un hombre y she para una mujer: This is Pedro. He is a driver. Así hablas de otras personas con datos básicos.",
    ],
    vocab=[("am / is / are", "formas de to be (ser o estar)"), ("I'm", "forma corta de I am"), ("isn't", "forma corta de is not (no es, no está)"), ("this is", "este es, esta es (para presentar)"), ("friend", "amigo o amiga"), ("new", "nuevo o nueva"), ("he", "él"), ("she", "ella")],
    worked=[
        ("Afirmar, negar y preguntar", "Parte de la oración: «Pedro is a driver». Escribe la negativa y la pregunta.", ["Para negar pongo not después de is: Pedro isn't a driver.", "Para preguntar paso is al principio: Is Pedro a driver?", "La respuesta corta es Yes, he is. o No, he isn't."], "Pedro isn't a driver. Is Pedro a driver?"),
        ("Presentar a otra persona", "Debes presentar a Ana, una cocinera de Chile.", ["Empiezo con this is y el nombre: This is Ana.", "Uso she porque es mujer: She is from Chile.", "Agrego el oficio con a: She is a cook."], "This is Ana. She is from Chile. She is a cook."),
    ],
    mistakes=[("Decir «Is you new here?».", "Se usa el verbo de otra persona con you.", "Con you, el verbo es are: Are you new here?"),
              ("Decir «This is Mary. He is from Colombia.»", "Se elige el pronombre equivocado.", "Para una mujer usa she: She is from Colombia.")],
    T=[
        ("abc", "Completa: «She ___ a nurse.»", "is", "am", "are", "Con she, el verbo to be es is."),
        ("abc", "Completa: «We ___ from Chile.»", "are", "is", "am", "Con we, el verbo to be es are."),
        ("ab", "Completa: «I ___ a driver.»", "am", "is", "Con I se usa siempre am, o la forma corta I'm."),
        ("abc", "{F} ¿De dónde es Mary?", "Colombia", "Chile", "Peru", "Carlos dice que Mary is from Colombia."),
        ("ab", "{F} ¿Qué dice el diálogo sobre el oficio de Mary?", "She's a baker.", "She's a nurse.", "Carlos dice She isn't a nurse. She's a baker."),
        ("abc", "¿Cuál es la forma negativa de «He is a cook»?", "He isn't a cook.", "He no is a cook.", "He not are a cook.", "La negación va con not después de is, y se acorta a isn't."),
        ("abc", "¿Cuál es la pregunta correcta para «You are new here»?", "Are you new here?", "Do you are new here?", "Is you new here?", "En la pregunta con to be, el verbo va al principio y con you es are."),
        ("ab", "Te preguntan: «Is Mr. Lopez a driver?» y la respuesta es sí. ¿Cuál es la respuesta corta?", "Yes, he is.", "Yes, he does.", "La respuesta corta repite el verbo de la pregunta, que es is."),
        ("Ordena las palabras: is / a / She / baker", "She is a baker.", "Primero va el sujeto She, luego is, luego a y el oficio."),
        ("abc", "¿Cuál es la forma corta de I am?", "I'm", "I'am", "Is'm", "El apóstrofo reemplaza la letra a de am: I'm."),
        ("ab", "Carlos dice: «This is Mary. He is from Colombia.» ¿Qué error hay?", "Mary es una mujer: debe decir she", "This is no se usa para presentar", "Para una mujer se usa she, no he; This is sí sirve para presentar."),
        ("abc", "Pedro es conductor. ¿Cuál es la presentación correcta?", "This is Pedro. He's a driver.", "This is Pedro. She's a driver.", "This are Pedro. He's driver.", "Se usa this is, el pronombre he para un hombre y a antes del oficio."),
        ("abc", "Rosa pregunta a Mary «Are you new here?». Mary quiere decir que no. ¿Qué responde?", "No, I'm not.", "No, I don't.", "No, I isn't.", "Con la pregunta en to be se responde con to be: No, I'm not."),
    ],
    ctx=("abc", "Un supervisor te pide presentar a tu compañera Ana, de Chile, que es cocinera. ¿Qué dices?", "This is Ana. She is from Chile. She is a cook.", "This is Ana. He is from Chile. He is cook.", "Ana is me. She are a cook.", "La presentación correcta usa this is, she para una mujer, is y a antes del oficio."),
    sc=[("En Inglés: ¿qué verbo va con she?", "is", "She, he e it van con is."),
        ("En Inglés: ¿cuál es la negativa de «I am a nurse»?", "I'm not a nurse.", "La negación se forma con not después de am."),
        ("abc", "En Inglés: ¿cómo presentas a un amigo llamado Pedro?", "This is Pedro.", "Pedro is me.", "I am Pedro his.", "This is sirve para presentar a una persona.")],
    op=("Escribe en tu cuaderno cómo presentarías a una persona de ejemplo (nombre, país y oficio) con tres oraciones usando this is, he o she, y una pregunta con to be. Puedes decirlo en voz alta.",
        "This is Carlos. He is from Peru. He is a driver. Is he new here?",
        ["usa this is al presentar", "elige he o she correctamente", "escribe una pregunta con to be"],
        ["tres oraciones y una pregunta"],
        ["usar he para una mujer", "olvidar a antes del oficio"],
        "Pregunta: «¿Elegiste he o she según la persona?»; revisa el verbo en la pregunta."),
    reinforce="Presenta en voz alta a tres personas que conoces, con this is y he o she.",
    extend="Escribe dos oraciones negativas y dos preguntas con to be sobre personas de tu trabajo (datos de ejemplo).",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico deletrear un nombre, decir números y la edad, y pedir que repitan lo que no entendí.",
    prior=["Digo mi nombre y mi edad con to be.", "Sé que hay palabras que cuesta oír bien.", "Conozco algunos números en inglés."],
    explain=[
        "Al llamar por teléfono o llenar un formulario te piden: How do you spell your last name? Respondes letra por letra. Aquí aparece escrito con guiones, por ejemplo M-O-R-E-N-O. Para practicar el sonido de cada letra, pide a una persona que conozca el abecedario en inglés que lo diga contigo.",
        "Los números del 0 al 20 son: zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. Los números de decenas terminan en -ty: thirty, forty, fifty, sixty, seventy, eighty. Ojo: thirteen termina en -teen y thirty en -ty.",
        "La edad se pregunta con How old are you? y se responde I'm forty-five years old. Si no entiendes, usa la frase útil Can you repeat that, please? (¿puede repetir, por favor?). Es una expresión completa, no hace falta aprender más gramática.",
    ],
    vocab=[("spell", "deletrear"), ("last name", "apellido"), ("phone number", "número de teléfono"), ("how old", "qué edad (se pregunta con how old)"), ("zero", "cero"), ("twenty", "veinte"), ("thirty", "treinta"), ("Can you repeat that, please?", "¿Puede repetir eso, por favor?")],
    worked=[
        ("Anotar un apellido", "Una persona dice: «R-O-J-A-S». ¿Cuál es el apellido?", ["Anoto cada letra: R, O, J, A, S.", "Las junto sin guiones: ROJAS.", "Escribo con mayúscula inicial: Rojas."], "Rojas"),
        ("Distinguir -teen de -ty", "Escuchas «I'm sixteen» y luego «I'm sixty». ¿Quién es mayor?", ["Sixteen termina en -teen y es 16.", "Sixty termina en -ty y es 60.", "60 es mayor que 16."], "La persona de sixty (60 años)"),
    ],
    mistakes=[("Confundir thirteen y thirty.", "Los dos suenan parecido y el final cambia el número.", "Fíjate: -teen es 13 a 19 y -ty son las decenas, como 30."),
              ("Decir «I have twenty years».", "En español se tienen años; en inglés se es una edad.", "Di I'm twenty years old.")],
    T=[
        ("{F} ¿Cuál es el apellido del llamante? Escribe la palabra completa con mayúscula inicial.", "Moreno", "El llamante deletrea las letras M-O-R-E-N-O, que forman el apellido."),
        ("abc", "{F} ¿Cómo se pregunta cómo se deletrea un apellido?", "How do you spell your last name?", "How are you last name?", "What spell is your name?", "La pregunta usa how do you spell y last name."),
        ("{F} ¿Cuántos años tiene el llamante? Escribe solo el número.", "45", "Forty-five years old es 45 años."),
        ("abc", "¿Qué número es «fourteen»?", "14", "40", "4", "Fourteen termina en -teen y es 14."),
        ("abc", "¿Qué número es «forty»?", "40", "14", "4", "Forty termina en -ty y es 40; recuerda que se escribe sin la u."),
        ("Escribe con letras, en inglés, el número 12.", "twelve", "El número 12 se escribe twelve."),
        ("ab", "¿Cómo se escribe 30 en inglés?", "thirty", "thirteen", "Thirty con -ty es 30; thirteen, con -teen, es 13."),
        ("Una persona deletrea M-A-R-Y. ¿Qué nombre es? Escríbelo.", "Mary", "Al juntar las letras M, A, R, Y se forma Mary."),
        ("Alguien dice los números «five, five, five, zero, one, four, two». Escríbelos como cifras, sin espacios.", "5550142", "Cada palabra es un dígito: 5, 5, 5, 0, 1, 4 y 2."),
        ("ab", "Ana dice «I'm eighteen» y Luis dice «I'm eighty». ¿Quién es mayor?", "Luis", "Ana", "Eighty, con -ty, es 80, y eighteen, con -teen, es 18."),
        ("abc", "¿Qué error hay en «I have twenty years»?", "En inglés se dice I'm twenty years old", "Falta la palabra the", "Twenty se escribe twenti", "La edad se dice con to be y años en years old."),
        ("abc", "Imagina que tienes 19 años. ¿Cómo lo dices?", "I'm nineteen years old.", "I'm ninety years old.", "I have nineteen years.", "Nineteen es 19 y ninety es 90; la edad usa to be."),
        ("abc", "{F} No entendiste el apellido. ¿Qué frase útil usas para pedir que repitan?", "Can you repeat that, please?", "You repeat now.", "I am repeat.", "Can you repeat that, please? es una expresión cortés para pedir que repitan."),
    ],
    ctx=("abc", "Inscribes a un compañero en un curso de ejemplo. Dice: «My last name is Rojas. R-O-J-A-S. I'm twenty-six.» ¿Qué anotas?", "Rojas, 26", "Rojaz, 26", "Rojas, 62", "Se anotan las letras que deletreó y twenty-six es 26."),
    sc=[("En Inglés: ¿cómo preguntas la edad de una persona?", "How old are you?", "La pregunta de la edad usa how old."),
        ("En Inglés: ¿qué número es «seventeen»?", "17", "Seventeen termina en -teen y es 17."),
        ("En Inglés: ¿qué dices si no entendiste y quieres que repitan?", "Can you repeat that, please?", "Es una expresión cortés para pedir que repitan.")],
    op=("Escribe en tu cuaderno un mini diálogo de seis líneas entre una recepcionista y una persona que da su nombre, deletrea su apellido y dice su edad. Usa nombres de ejemplo. Puedes leerlo en voz alta con otra persona.",
        "Receptionist: What's your name? / Ana: My name is Ana Rojas. / Receptionist: How do you spell your last name? / Ana: R-O-J-A-S. / Receptionist: How old are you? / Ana: I'm twenty-eight years old.",
        ["pregunta el nombre", "deletrea el apellido con letras", "dice la edad con years old"],
        ["un diálogo de seis líneas"],
        ["confundir thirteen y thirty", "olvidar years old"],
        "Pregunta: «¿Deletreaste el apellido letra por letra?»; revisa el número que escribiste."),
    reinforce="Deletrea tu nombre y tu apellido, con letras separadas, en voz baja.",
    extend="Escribe cinco edades de ejemplo con letras en inglés, entre 13 y 90 (incluye ninety).",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico saludos, la hora, el clima y datos personales en un mensaje de voz y en un gafete de trabajo.",
    prior=["Uso saludos según la hora.", "Digo país, oficio y edad.", "Sé usar to be con él, ella y yo."],
    explain=[
        "En el trabajo escuchas mensajes cortos: un saludo, un dato, una hora y una petición. Para decir la hora usa It's y el número: It's nine o'clock significa son las nueve en punto. Para preguntar, di What time is it?",
        "También se habla del clima con It's: It's sunny (hace sol), It's rainy (llueve), It's cold (hace frío). Para pedir algo con cortesía usa please: Please wait significa por favor espere. Es una expresión completa y sirve como instrucción.",
        "Cuando escuches o leas un mensaje, subraya palabras clave: nombres, números, lugares. Con ellas respondes preguntas como quién llama, a qué hora es la reunión y cómo está el clima. Tu atención va a la idea general, no a cada palabra.",
    ],
    vocab=[("o'clock", "en punto (hora)"), ("meeting", "reunión"), ("cold", "frío"), ("rainy", "lluvioso"), ("warehouse", "bodega"), ("please", "por favor"), ("What time is it?", "¿Qué hora es?"), ("It's...", "Es o está (hora y clima)")],
    worked=[
        ("Entender un mensaje", "Un mensaje dice: «Hello, Ana. The meeting is at seven o'clock. Please wait.» ¿A qué hora es la reunión?", ["Busco la palabra clave de la hora: seven o'clock.", "Seven es 7 y o'clock es en punto.", "La reunión es a las 7 en punto."], "A las 7 en punto"),
        ("Pedir la hora", "Quieres saber la hora a una compañera.", ["Uso la pregunta What time is it?", "Ella puede responder It's two o'clock.", "El número va antes de o'clock."], "What time is it?"),
    ],
    mistakes=[("Decir «I'm seven o'clock».", "Se usa el verbo para la hora con la persona en lugar de it.", "Para la hora y el clima usa It's: It's seven o'clock."),
              ("Decir «Good night» en un mensaje de las 3 de la tarde.", "Good night es una despedida nocturna, no un saludo.", "Para la tarde di good afternoon.")],
    T=[
        ("abc", "{F} ¿Quién llama?", "Ana, de la bodega", "Mr. Lopez", "Peter", "El mensaje dice This is Ana from the warehouse."),
        ("{F} ¿A qué hora es la reunión? Escribe solo el número.", "9", "El mensaje dice nine o'clock, que es 9."),
        ("abc", "{F} ¿Cómo está el clima hoy?", "Hace frío y llueve", "Hace sol y calor", "Hay mucho viento y calor", "Ana dice It's cold and rainy today."),
        ("ab", "{F} ¿Qué pide Ana?", "Que Mr. Lopez espere", "Que Mr. Lopez salga de inmediato", "Please wait significa por favor espere."),
        ("abc", "¿Cómo dices que son las 7 en punto?", "It's seven o'clock.", "It's seven clock.", "I'm seven o'clock.", "Para la hora se usa It's más el número y o'clock."),
        ("abc", "{F} Según el gafete, ¿qué oficio tiene Peter Moreno?", "driver", "cook", "nurse", "El gafete anota Job: driver, que significa conductor."),
        ("ab", "{F} Según el gafete, ¿cuál oración es verdadera?", "Peter is thirty-eight years old.", "Peter is eighty-three years old.", "El gafete anota Age: 38, que se dice thirty-eight."),
        ("abc", "¿Qué pregunta usas para saber la hora?", "What time is it?", "How old is it?", "Where time is?", "La pregunta para la hora es What time is it?"),
        ("Ordena las palabras para dar la hora: o'clock / It's / two", "It's two o'clock.", "Primero va It's, después el número y al final o'clock."),
        ("abc", "Quieres pedir a un compañero nuevo que espere un momento. ¿Qué frase es cortés?", "Please wait here.", "Wait now!", "You wait no.", "Please agrega cortesía a la instrucción."),
        ("ab", "Mary escribe «Good evening, Mr. Lopez» en un correo a las 10 de la mañana. ¿Qué recomiendas?", "Cambiar a good morning", "Dejarlo igual", "A las 10 de la mañana el saludo correcto es good morning."),
        ("abc", "Un mensaje dice: «Hello, I'm Peter. I'm a driver. It's eight o'clock.» ¿Cuál es la idea principal?", "Peter se presenta y dice la hora", "Peter pide un taxi", "Peter anuncia un feriado", "El mensaje trae su nombre, su oficio y la hora."),
        ("abc", GUION + "It's sunny. It's ten o'clock. Good morning! ¿Qué hora se dijo?", "Las 10 en punto", "Las 2 en punto", "Las 12 en punto", "Ten es 10; two es 2, y no se dice nada de las 12."),
    ],
    ctx=("abc", "Llegas a la bodega y el guardia dice: «Good morning. Name, please?» ¿Cómo respondes?", "Good morning. My name is Rosa Diaz.", "Good night. I'm fine.", "See you later.", "El guardia pide tu nombre; respondes con saludo y My name is."),
    sc=[("En Inglés: ¿cómo preguntas la hora?", "What time is it?", "Esa es la pregunta habitual para pedir la hora."),
        ("En Inglés: ¿qué significa «It's rainy»?", "Está lloviendo o es un día lluvioso", "La palabra rainy significa lluvioso, como un día con lluvia."),
        ("En Inglés: ¿para qué sirve la palabra please?", "Para pedir algo con cortesía", "La palabra please equivale a por favor en español.")],
    op=("Escribe en tu cuaderno un mensaje de voz de cinco líneas de ejemplo para un compañero: saludo según la hora, quién eres, a qué hora es la reunión, cómo está el clima y please. Puedes grabarlo si quieres, no es obligatorio.",
        "Good morning, Pedro. This is Rosa. The meeting is at ten o'clock. It's cold today. Please wait here.",
        ["usa un saludo correcto", "dice quién habla", "dice una hora con o'clock", "da una instrucción con please"],
        ["un mensaje de cinco líneas"],
        ["saludar con good night", "olvidar o'clock"],
        "Pregunta: «¿Quién entiende tu mensaje sin explicación?»; revisa el saludo."),
    reinforce="Mira un reloj y di en voz baja la hora en inglés con o'clock durante la jornada.",
    extend="Escribe un mensaje de voz de ejemplo con dos horas y dos datos del clima.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso todo lo aprendido en este desempeño, me autoevalúo y decido qué repasar.",
    prior=["Saludo según la hora y me presento.", "Digo país, oficio, edad y hora.", "Presento a otra persona con he o she."],
    explain=[
        "Para revisar, usa esta lista: saludo según la hora, mi nombre, país, oficio y edad, presentar a otra persona con he o she, deletrear un apellido, números y la hora. Marca lo que ya haces bien y lo que quieres repasar.",
        "Si algo falla, busca la causa. ¿Confundiste el verbo to be? ¿Pusiste el saludo equivocado? ¿Mezclaste thirteen y thirty? Anota el error y corrígelo con un ejemplo propio. Equivocarse es una forma de aprender.",
        "Para seguir, practica con personas reales: saluda y preséntate en voz alta, lee carteles con nombres y números, y repite las frases útiles. Así pasas de reconocer a usar el inglés en tu trabajo, tu hogar y tu comunidad.",
    ],
    vocab=[("introduce yourself", "preséntate (expresión completa)"), ("country", "país"), ("job", "oficio o trabajo"), ("age", "edad"), ("spell", "deletrear"), ("o'clock", "en punto"), ("friend", "amigo o amiga"), ("new", "nuevo o nueva")],
    worked=[
        ("Revisar una presentación", "Marta dice: «I'm Marta. I'm from Bolivia. I'm a cook. I have forty years.» Revisa y corrige.", ["Reviso el nombre y el país: están correctos.", "Reviso el oficio: está correcto con a.", "Reviso la edad: se dice I'm forty years old."], "I'm Marta. I'm from Bolivia. I'm a cook. I'm forty years old."),
        ("Elegir el saludo", "A las 6 de la tarde llegas a una reunión. ¿Qué saludo usas?", ["Miro la hora: 6 de la tarde es cerca del atardecer.", "El saludo que sirve es good evening.", "Good night no se usa al llegar."], "Good evening."),
    ],
    mistakes=[("Usar he para presentar a una mujer.", "Se piensa en el nombre y no en quién es la persona.", "Para una mujer usa she; para un hombre, he."),
              ("Traducir palabra por palabra una frase de edad.", "Se aplica la estructura del español al inglés.", "Aprende la frase completa: I'm thirty years old.")],
    T=[
        ("abc", "{F} ¿De dónde es Marta?", "Bolivia", "Chile", "Peru", "La tarjeta de Marta dice I'm from Bolivia, es decir, soy de Bolivia."),
        ("{F} ¿Cuántos años tiene Marta? Escribe solo el número.", "40", "Marta dice forty years old, que es 40."),
        ("abc", "{F} ¿Qué oficio tiene John?", "driver", "cook", "baker", "La tarjeta dice He's a driver."),
        ("ab", "{F} ¿Cuál oración es verdadera?", "John is thirty-six.", "John is sixty-three.", "La tarjeta dice He's thirty-six, es decir, 36."),
        ("abc", "{F} ¿A qué momento del día corresponde el saludo a Peter?", "La mañana", "La tarde", "La noche", "El texto dice Good morning, Peter."),
        ("abc", "Completa: «John and Marta ___ at work.»", "are", "is", "am", "Con dos personas se usa are."),
        ("ab", "John dice sobre Ana: «She are a nurse.» ¿Cuál es la corrección?", "She is a nurse.", "She am a nurse.", "Con she el verbo to be es is."),
        ("Una persona deletrea B-O-L-I-V-I-A. ¿Qué país es? Escríbelo.", "Bolivia", "Al juntar las letras se forma Bolivia."),
        ("abc", "¿Cuál es una presentación natural?", "Hello. I'm Rosa. I'm from Chile. Nice to meet you.", "Nice to meet you. Chile. Hello. I'm.", "I Rosa from. Hello you meet.", "La presentación natural va en orden: saludo, nombre, país y cortesía."),
        ("abc", "¿Qué número es «seventeen»?", "17", "70", "7", "Seventeen termina en -teen y es 17."),
        ("ab", "A las 9 de la noche alguien dice «Good afternoon» al llegar a una reunión. ¿Qué saludo suena más natural a esa hora?", "Good evening", "Good morning", "A las 9 de la noche el saludo natural es good evening; good morning no corresponde."),
        ("abc", "Para entender un diálogo largo, ¿qué estrategia sirve?", "Subrayar palabras clave como nombres y números", "Traducir todo palabra por palabra", "Memorizarlo sin leerlo", "Las palabras clave dan la idea general sin traducir todo."),
        ("abc", GUION + "My name is Rosa. I'm from Chile. I'm a baker. I'm twenty-nine. ¿Cuál es el oficio?", "baker", "cook", "nurse", "En el guion Rosa dice I'm a baker, que significa panadera."),
    ],
    ctx=("abc", "En una entrevista de ejemplo, a las 9 de la mañana, la persona dice: «Please introduce yourself.» ¿Cuál es la mejor respuesta?", "Good morning. I'm Pedro. I'm from Chile. I'm a driver. I'm thirty years old.", "Good night. I'm Pedro. I'm driver. I have thirty years.", "Pedro. Chile. I'm a. Thirty.", "La respuesta ordenada usa el saludo, I'm y a antes del oficio."),
    sc=[("abc", "En Inglés: ¿cómo presentas a una amiga llamada Ana?", "This is Ana. She is my friend.", "This is Ana. He is my friend.", "This are Ana. She friend.", "This is sirve para presentar y she, para una mujer."),
        ("En Inglés: ¿cómo dices que tienes treinta años?", "I'm thirty years old.", "La edad se dice con to be."),
        ("abc", "En Inglés: ¿cuál de estas frases es una despedida?", "See you later.", "Nice to meet you.", "Good morning.", "See you later significa hasta luego.")],
    op=("Prepara en tu cuaderno una presentación breve de ti mismo con datos de ejemplo (saludo, nombre, país, oficio y edad) y una presentación de una persona cercana de ejemplo con he o she. Léela en voz alta a otra persona. Después anota qué quieres repasar.",
        "Good evening. I'm Rosa. I'm from Chile. I'm a cook. I'm thirty-five years old. This is Pedro. He is a driver. He is forty years old. See you later!",
        ["usa un saludo según la hora", "presenta sus datos con I'm", "presenta a otra persona con he o she", "anota qué repasar"],
        ["una presentación de ocho oraciones y una lista de qué repasar"],
        ["usar he para una mujer", "olvidar a antes del oficio"],
        "Pregunta: «¿Qué dos frases te salieron mejor y cuál quieres repetir?». Si es posible, graba y escucha si se entiende."),
    reinforce="Elige una frase de cada clase y dila en voz alta tres veces.",
    extend="Escribe un mini diálogo de ocho líneas con saludo, nombres, países, oficios, edades y despedida.",
)

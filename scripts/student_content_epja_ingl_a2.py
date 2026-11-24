"""Inglés EPJA Nivel 2, módulo 1 (parte 2): OAD-02, preguntar por información personal y describirse y describir a otros física y emocionalmente. Todos los textos y guiones son inventados y se leen en papel."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-02"

F1 = ("Transcripción de una entrevista de ejemplo (inventada) en un centro comunitario: Interviewer: What's your name? / Luis: My name is Luis Soto. / Interviewer: Where are you from? / Luis: I'm from Peru. / "
      "Interviewer: How old are you? / Luis: I'm thirty-four. / Interviewer: Who is Ana? / Luis: Ana is my sister.")

F2 = ("Descripción de ejemplo (inventada), en un centro comunitario: Ana is tall. She is happy today. Pedro is short. He is tired and hungry. Mr. Lopez is worried, but he is not sad. Mrs. Diaz is busy.")

F3 = ("Diálogo de ejemplo (inventado) en objetos perdidos: Clerk: Is this your jacket? / Marta: No, it isn't. My jacket is blue. / Clerk: Is that his bag, over there? / Marta: Yes, it is. His name is Pedro. / "
      "Clerk: And these? Are these her gloves? / Marta: Yes, they are. Her name is Ana.")

F4 = ("Texto de ejemplo (inventado), en un consultorio: Rosa is first in line. Carlos is second. Mary is third. Pedro is fourth. Today is the fifth day of the course. The class is on the second floor, in room ten.")

F5 = ("Transcripción de un aviso por altavoz de ejemplo (inventado) en un terminal: Attention, please. Mr. Lopez is looking for his friend, Rosa. Rosa is tall. She is wearing a green jacket. "
      "She is waiting next to the door. She is not tired, but she is worried. Please help.")

F6 = ("Descripción de ejemplo (inventada): This is Carmen. She is first in line. She is tall, and she is wearing a red jacket. She is happy today. Her bag is on the chair. Those keys are her keys. "
      "Her brother is Diego. He is short, and he is tired. He is second in line.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy aprendo a preguntar información personal con What, Where, Who y How old, y a responder con frases completas.",
    prior=["Me presento con My name is e I'm.", "Digo mi país, mi oficio y mi edad.", "Uso el verbo to be con I, you, he y she."],
    explain=[
        "En un trámite o en un trabajo nuevo te hacen preguntas personales. En inglés las preguntas comienzan con una palabra clave: What (qué, cuál), Where (dónde), Who (quién), How old (qué edad) y How (cómo).",
        "La estructura básica es: palabra de pregunta, el verbo to be y la persona. Por ejemplo: What is your name? Where are you from? Who is she? How old are you? Fíjate que el verbo va antes de you, no después.",
        "Para responder, usa una frase completa y corta: My name is Ana. I'm from Chile. She is my sister. I'm thirty years old. Escucha primero la palabra de pregunta: te dice qué dato te piden, como nombre, lugar, persona o edad.",
    ],
    vocab=[("what", "qué, cuál"), ("where", "dónde"), ("who", "quién"), ("how old", "qué edad"), ("your", "tu, su (de usted)"), ("my", "mi"), ("sister", "hermana"), ("brother", "hermano")],
    worked=[
        ("Elegir la respuesta", "Alguien pregunta: «Where are you from?». ¿Qué dato te piden?", ["Miro la palabra de pregunta: where.", "Where pregunta por un lugar.", "Respondo con el país: I'm from Chile."], "I'm from Chile."),
        ("Armar una pregunta", "Quieres saber la edad de una persona. Arma la pregunta con you.", ["Uso How old para preguntar por la edad.", "Agrego el verbo to be con you: are.", "Pongo el verbo antes de you: How old are you?"], "How old are you?"),
    ],
    mistakes=[("Decir «How old you are?».", "Se deja el verbo después de you, como en una oración afirmativa.", "En la pregunta el verbo va antes: How old are you?"),
              ("Responder «I'm thirty» a la pregunta Where are you from?", "No se mira la palabra de pregunta.", "Primero lee la palabra de pregunta y responde con lo que pide: un lugar.")],
    T=[
        ("abc", "{F} ¿De qué país es Luis?", "Peru", "Chile", "Bolivia", "Luis responde I'm from Peru a la pregunta Where are you from?"),
        ("{F} ¿Cuántos años tiene Luis? Escribe solo el número.", "34", "Luis dice thirty-four, que significa treinta y cuatro."),
        ("abc", "{F} ¿Quién es Ana?", "La hermana de Luis", "La profesora de Luis", "La vecina de Luis", "Luis dice Ana is my sister, es decir, Ana es mi hermana."),
        ("abc", "¿Qué palabra de pregunta se usa para un lugar?", "Where", "Who", "What", "Where pregunta por el lugar o el origen."),
        ("abc", "¿Qué palabra de pregunta se usa para una persona?", "Who", "Where", "How old", "Who pregunta por una persona: quién es."),
        ("ab", "¿Cómo se pregunta la edad?", "How old are you?", "What old are you?", "Para la edad se usa how old y no what."),
        ("abc", "Completa: «___ is your name?»", "What", "Where", "Who", "Para preguntar el nombre se usa what: What is your name?"),
        ("abc", "Completa: «___ are you from?»", "Where", "Who", "How old", "Para preguntar el origen se usa where."),
        ("Ordena las palabras para formar una pregunta: from / Where / you / are", "Where are you from?", "La palabra de pregunta va primero, luego are y después you."),
        ("ab", "Te preguntan «Where is Mary from?». ¿Cuál es la respuesta correcta?", "She is from Colombia.", "She is thirty.", "Where pide un lugar, no una edad."),
        ("abc", "Alguien responde «I'm a cook». ¿Qué pregunta responde?", "What is your job?", "Where are you from?", "How old are you?", "I'm a cook da el oficio, y para el oficio se pregunta con what."),
        ("abc", "¿Qué error hay en «How old you are?»?", "El verbo are debe ir antes de you", "Falta la palabra who", "Old se escribe olt", "En una pregunta con to be, el verbo va antes de la persona."),
        ("{F} ¿Cuál es el apellido de Luis? Escríbelo.", "Soto", "Luis dice My name is Luis Soto, entonces su apellido es Soto."),
    ],
    ctx=("abc", "En el registro de un consultorio de ejemplo te preguntan «Where are you from?». ¿Qué respuesta es correcta?", "I'm from Chile.", "I'm thirty.", "I'm a baker.", "Where pregunta por el origen; la respuesta debe dar un país o un lugar."),
    sc=[("abc", "En Inglés: ¿qué palabra pregunta por la edad?", "How old", "Where", "Who", "How old pregunta qué edad se tiene."),
        ("abc", "En Inglés: ¿cuál pregunta es correcta?", "What is your name?", "What your name is?", "Where is your name?", "En la pregunta el verbo is va antes de your name."),
        ("abc", "En Inglés: ¿cómo respondes a «Who is Ana?»?", "She is my sister.", "She is thirty.", "She is in Chile.", "Who pide la identidad de una persona.")],
    op=("Escribe en tu cuaderno una entrevista de seis líneas entre una persona que hace preguntas y otra que responde. Usa What, Where, Who y How old, con datos de ejemplo. Puedes leerla en voz alta con otra persona.",
        "A: What is your name? / B: My name is Rosa. / A: Where are you from? / B: I'm from Chile. / A: How old are you? / B: I'm thirty-two years old.",
        ["usa tres palabras de pregunta distintas", "el verbo is o are va antes del sujeto", "las respuestas son frases completas"],
        ["una entrevista de seis líneas"],
        ["decir How old you are", "responder con un dato que no corresponde a la pregunta"],
        "Pregunta: «¿Cada respuesta contesta lo que se pregunta?»; revisa dónde pusiste el verbo."),
    reinforce="Haz en voz baja las tres preguntas What, Where y How old a un vecino imaginario y responde tú mismo.",
    extend="Escribe cuatro preguntas personales de ejemplo con Who y What y sus respuestas.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy conozco ocho adjetivos para describir el aspecto y las emociones de una persona.",
    prior=["Pregunto datos con What, Where y Who.", "Uso is y are con personas.", "Sé decir cómo estoy en español."],
    explain=[
        "Un adjetivo dice cómo es o cómo está una persona. Aquí vemos aspecto (tall, short) y emociones o estados (tired, happy, worried, hungry, busy, sad). Se usan con to be: She is tall. He is tired.",
        "Hay dos cosas fáciles de recordar. El adjetivo no cambia con el género ni con el plural: She is tall, He is tall, They are tall. Y cuando acompaña a un sustantivo, va antes de él: a tall man, un hombre alto.",
        "Para preguntar cómo está una persona, usa How: How are you? How is Pedro? Y para negar, agrega not: He is not sad o He isn't sad. En esta clase leemos una descripción de ejemplo y marcamos las palabras clave.",
    ],
    vocab=[("tall", "alto o alta"), ("short", "bajo o baja (de estatura)"), ("tired", "cansado o cansada"), ("happy", "feliz, contento"), ("worried", "preocupado o preocupada"), ("hungry", "con hambre"), ("busy", "ocupado u ocupada"), ("sad", "triste")],
    worked=[
        ("Describir a una persona", "Ana mide más que su vecina y hoy está contenta. ¿Cómo la describes?", ["Uso She is porque habla de una mujer.", "Para la estatura uso tall.", "Para la emoción agrego happy: She is happy."], "She is tall. She is happy."),
        ("Negar un adjetivo", "Pedro no está triste, está cansado. Escríbelo.", ["Con not niego el adjetivo sad: He isn't sad.", "Agrego el estado real: He is tired.", "Junto las dos ideas."], "He isn't sad. He is tired."),
    ],
    mistakes=[("Decir «They are talls».", "En español el adjetivo cambia a alto o altos y se cree que en inglés también.", "En inglés el adjetivo no cambia: They are tall."),
              ("Decir «a man tall».", "Se copia el orden del español: hombre alto.", "En inglés el adjetivo va antes: a tall man.")],
    T=[
        ("abc", "{F} ¿Quién está cansado?", "Pedro", "Ana", "Mrs. Diaz", "El texto dice He is tired and hungry sobre Pedro."),
        ("abc", "{F} ¿Cómo está Ana hoy?", "Feliz", "Triste", "Con hambre", "El texto dice She is happy today."),
        ("{F} Mr. Lopez is worried, but he is not ___. Escribe la palabra que falta.", "sad", "El texto dice que Mr. Lopez está preocupado pero no triste."),
        ("abc", "¿Qué significa tall?", "Alto", "Bajo", "Cansado", "Tall describe a una persona de mucha estatura."),
        ("abc", "¿Qué significa tired?", "Cansado", "Feliz", "Ocupado", "La palabra tired significa cansado, sin fuerzas para seguir."),
        ("abc", "Completa: «Ana is ___.» (alta)", "tall", "talls", "a tall", "El adjetivo no cambia y se usa solo después del verbo."),
        ("abc", "¿Cuál es la oración correcta para «Ellos son bajos»?", "They are short.", "They are shorts.", "They short are.", "El adjetivo no lleva s en plural."),
        ("ab", "¿Cómo se dice «un hombre alto»?", "a tall man", "a man tall", "En inglés el adjetivo va antes del sustantivo."),
        ("Ordena las palabras: hungry / is / He", "He is hungry.", "El orden es sujeto, verbo y luego el adjetivo."),
        ("abc", "{F} Si preguntan «How is Pedro?», ¿cuál es la respuesta correcta?", "He is tired and hungry.", "He is short and tall.", "He is Ana.", "El texto da cómo está Pedro: cansado y con hambre."),
        ("ab", "{F} Alguien dice «Mrs. Diaz is sad». Según el texto, ¿es correcto?", "No: el texto dice que Mrs. Diaz está ocupada", "Sí: Mrs. Diaz está triste", "El texto dice Mrs. Diaz is busy, no sad."),
        ("abc", "¿Cuál palabra describe una emoción?", "worried", "tall", "short", "Worried describe cómo se siente una persona; tall y short, su estatura."),
        ("abc", "Alguien dice «I'm worried» porque mañana tiene una entrevista de trabajo. ¿Cómo está?", "Preocupado o preocupada", "Feliz", "Con hambre", "La palabra worried significa preocupado o preocupada por algo."),
    ],
    ctx=("abc", "Un compañero de turno te pregunta «How are you?» y estás muy cansado después de trabajar. ¿Qué respondes?", "I'm tired, thanks.", "I'm tall, thanks.", "I'm from Chile, thanks.", "How are you pregunta por el estado; respondes con un adjetivo de estado como tired."),
    sc=[("abc", "En Inglés: ¿qué significa hungry?", "Con hambre", "Con sueño", "Enfermo", "Hungry describe a quien necesita comer."),
        ("abc", "En Inglés: ¿cuál es correcta?", "She is tall.", "She tall is.", "She are tall.", "Con she el verbo es is y después va el adjetivo."),
        ("abc", "En Inglés: ¿cómo dices «él no está triste»?", "He isn't sad.", "He no is sad.", "He not sad is.", "La negación usa isn't después del sujeto.")],
    op=("Escribe en tu cuaderno cinco oraciones que describan a dos personas de ejemplo: aspecto (tall o short) y cómo se sienten hoy (tired, happy, worried, hungry, busy o sad). Puedes decirlas en voz alta.",
        "Rosa is tall. She is happy today. Pedro is short. He is tired. He isn't sad.",
        ["usa el verbo to be en cada oración", "incluye al menos un adjetivo de aspecto y uno de emoción", "usa he o she correctamente"],
        ["cinco oraciones sobre dos personas"],
        ["agregar s al adjetivo", "poner el adjetivo después del sustantivo"],
        "Pregunta: «¿Escribiste el verbo en todas las oraciones?»; revisa he y she."),
    reinforce="Describe en voz baja a tres personas conocidas con un adjetivo de aspecto y uno de emoción.",
    extend="Escribe cómo estás cada día de la semana usando un adjetivo distinto.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo a decir de quién es algo con my, your, his y her, y a señalar con this, that, these y those.",
    prior=["Uso el verbo to be.", "Describo personas con adjetivos.", "Sé decir mi nombre y datos básicos."],
    explain=[
        "Los posesivos dicen de quién es algo y van antes del sustantivo: my bag (mi bolsa), your jacket (tu chaqueta), his phone (el teléfono de él), her gloves (los guantes de ella). Se elige según el dueño, no según el objeto.",
        "Los demostrativos señalan algo. This (este, esta) y these (estos, estas) son para lo que está cerca. That (ese, aquel) y those (esos, aquellos) son para lo que está lejos. This y that son singulares; these y those son plurales.",
        "Con singular usa is: This is my bag. Con plural usa are: These are my keys. La pregunta pone el verbo primero: Is this your jacket? Are these her gloves? Responde con respuestas cortas: Yes, it is. No, it isn't. Yes, they are.",
    ],
    vocab=[("my", "mi, mis"), ("your", "tu, tus, su (de usted)"), ("his", "su (de él)"), ("her", "su (de ella)"), ("this", "este o esta (cerca)"), ("that", "ese o esa (lejos)"), ("these", "estos o estas (cerca)"), ("those", "esos o esas (lejos)")],
    worked=[
        ("Elegir el posesivo", "Pedro tiene un auto blanco. ¿Cómo dices «su auto es blanco»?", ["Pedro es un hombre: uso his.", "El posesivo va antes del sustantivo: his car.", "Armo la oración con is."], "His car is white."),
        ("Elegir el demostrativo", "Señalas dos llaves que están cerca de ti. ¿Qué dices?", ["Son dos objetos: uso plural.", "Están cerca: uso these.", "Con plural uso are."], "These are my keys."),
    ],
    mistakes=[("Decir «This is she bag».", "Se usa el pronombre she en lugar del posesivo.", "Para ella como dueña usa her: This is her bag."),
              ("Decir «Those is my keys».", "No concuerda el plural con el verbo.", "Con those usa are: Those are my keys.")],
    T=[
        ("abc", "{F} ¿De qué color es la chaqueta de Marta?", "Azul", "Verde", "Roja", "Marta dice My jacket is blue."),
        ("abc", "{F} Según Marta, ¿de quién es la bolsa que señala el empleado?", "De Pedro", "De Marta", "De Ana", "Marta dice que la bolsa es his, y que su nombre es Pedro."),
        ("{F} ¿Cómo se llama la dueña de los guantes? Escribe solo el nombre.", "Ana", "Marta dice Her name is Ana al hablar de los guantes."),
        ("abc", "Completa: «___ bag is red.» (mi bolsa)", "My", "Me", "I", "My es el posesivo que va antes del sustantivo."),
        ("abc", "Completa: «Pedro is a driver. ___ car is white.»", "His", "Her", "My", "Pedro es hombre, entonces el posesivo es his."),
        ("abc", "Completa: «Ana is a nurse. ___ job is hard.»", "Her", "His", "Your", "Ana es mujer, entonces el posesivo es her."),
        ("ab", "Tienes un libro en la mano. ¿Qué dices? «___ is my book.»", "This", "That", "This señala lo que está cerca; that, lo que está lejos."),
        ("abc", "Señalas dos llaves que están lejos de ti: «___ are my keys.»", "Those", "That", "This", "Those es el plural para lo que está lejos."),
        ("abc", "¿Qué significa «these» en «Are these your gloves?»?", "Estos o estas, cerca y en plural", "Ese o esa, lejos", "Mi, mis", "La palabra these señala varias cosas que están cerca."),
        ("ab", "Marta dice «This is she bag». ¿Cuál es la corrección?", "This is her bag.", "This is hers bag.", "Para señalar a la dueña ella se usa her antes del sustantivo."),
        ("abc", "¿Cuál oración es correcta?", "That is his jacket.", "That are his jacket.", "Those is his jacket.", "That es singular, entonces va con is."),
        ("abc", "Pedro habla de Ana: «Ana is ___ friend.» (mi amiga)", "my", "I", "me", "Para decir mi amiga se usa my antes del sustantivo."),
        ("abc", "{F} ¿Qué demostrativo usa el empleado para preguntar por un objeto lejano?", "That", "These", "My", "El empleado dice Is that his bag, over there, con that."),
    ],
    ctx=("abc", "En objetos perdidos de un terminal de ejemplo, un empleado te muestra una chaqueta que tiene en la mano. ¿Qué pregunta hace?", "Is this your jacket?", "Are these your jacket?", "Is that my jacket?", "Es una sola chaqueta cercana, por eso is this."),
    sc=[("abc", "En Inglés: ¿qué posesivo se usa para una mujer?", "her", "his", "my", "Her es el posesivo para una mujer."),
        ("abc", "En Inglés: ¿qué demostrativo es plural y cercano?", "these", "that", "those", "These es plural y para lo que está cerca."),
        ("abc", "En Inglés: ¿cómo se dice «tus llaves»?", "your keys", "you keys", "yours key", "Your va antes del sustantivo para decir tu o tus.")],
    op=("Escribe en tu cuaderno cinco oraciones sobre objetos de una persona de ejemplo en una oficina: dos con my o your, una con his o her, una con this o that y una con these o those. Puedes señalar objetos reales mientras las dices.",
        "This is my bag. That is your jacket. His phone is black. Her keys are on the table. These are my gloves.",
        ["usa dos posesivos distintos", "usa un demostrativo singular y uno plural", "usa is con singular y are con plural"],
        ["cinco oraciones sobre objetos"],
        ["usar she en lugar de her", "no concordar is y are"],
        "Pregunta: «¿Elegiste el posesivo según el dueño?»; revisa is y are."),
    reinforce="Señala cinco objetos de tu casa y di una oración con this, that, these o those para cada uno.",
    extend="Escribe un diálogo de objetos perdidos de seis líneas con dos objetos y dos dueños.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico números cardinales y ordinales para decir lugares en una fila, pisos y días.",
    prior=["Conozco los números del 1 al 20 en inglés.", "Sé decir mi edad.", "Uso is y are."],
    explain=[
        "Los números cardinales cuentan: one, two, three. Los ordinales dan orden o lugar: first, second, third. Sirven para una fila, los pisos de un edificio, el número de una clase o los días de un curso.",
        "Los ordinales de 1 a 3 son irregulares: first, second, third. Del 4 al 10 casi todos agregan -th: fourth, fifth, sixth, seventh, eighth, ninth, tenth. Ojo con fifth (no fiveth), eighth y ninth (sin e).",
        "En una oración se usan con the o con el verbo to be: She is first in line. The class is on the second floor. Today is the fifth day of the course. Un cardinal sirve para el número de una sala: room ten.",
    ],
    vocab=[("first", "primero o primera"), ("second", "segundo o segunda"), ("third", "tercero o tercera"), ("fourth", "cuarto o cuarta"), ("fifth", "quinto o quinta"), ("ninth", "noveno o novena"), ("tenth", "décimo o décima"), ("in line", "en la fila")],
    worked=[
        ("Decir un lugar en la fila", "Eres el tercero en la fila. ¿Cómo lo dices?", ["Para un lugar uso un ordinal.", "El ordinal de tres es third.", "Armo la oración con I'm."], "I'm third in line."),
        ("Cardinal u ordinal", "Una persona dice «room ten» y otra «the tenth floor». ¿Qué número es cada uno?", ["En room ten, ten es cardinal: el número de la sala.", "En the tenth floor, tenth es ordinal: el lugar del piso.", "Uno cuenta y el otro ordena."], "Ten es cardinal y tenth es ordinal"),
    ],
    mistakes=[("Escribir «fiveth» o «nineth».", "Se agrega -th al número sin cambiar la palabra.", "Escribe fifth y ninth."),
              ("Decir «I'm the three in line».", "Se usa el cardinal para dar un lugar.", "Para un lugar usa el ordinal: I'm third in line.")],
    T=[
        ("abc", "{F} ¿Quién está primero en la fila?", "Rosa", "Carlos", "Mary", "El texto dice Rosa is first in line."),
        ("abc", "{F} ¿Qué lugar ocupa Mary en la fila?", "Tercero", "Segundo", "Cuarto", "El texto dice Mary is third."),
        ("{F} ¿En qué piso está la clase? Escribe la palabra en inglés.", "second", "El texto dice The class is on the second floor."),
        ("abc", "¿Cómo se dice primero en inglés?", "first", "one", "second", "First es el ordinal de uno; one es el cardinal."),
        ("abc", "¿Qué lugar es «fifth»?", "El quinto", "El cuarto", "El sexto", "Fifth es el ordinal de cinco."),
        ("ab", "¿Cuál se escribe bien?", "ninth", "nineth", "El ordinal de nueve pierde la e: ninth."),
        ("abc", "Estás en el décimo piso. Completa: «I'm on the ___ floor.»", "tenth", "ten", "tent", "Para el lugar del piso se usa el ordinal tenth."),
        ("abc", "Completa: «Today is my ___ week of classes.» (cuarta)", "fourth", "four", "forth", "Fourth es el ordinal de cuatro; forth es otra palabra."),
        ("Ordena las palabras: line / in / is / She / first", "She is first in line.", "El orden es sujeto, verbo, ordinal y lugar."),
        ("abc", "En «I'm in room three», la palabra three es...", "Un cardinal", "Un ordinal", "Una emoción", "Three solo nombra el número de la sala, no un orden."),
        ("ab", "Pedro dice «I'm the three in line». ¿Cuál es la corrección?", "I'm third in line.", "I'm threeth in line.", "Para dar un lugar se usa el ordinal irregular third."),
        ("abc", "{F} ¿Cuántas personas ordenadas se nombran en la fila?", "4", "3", "5", "Se nombran Rosa, Carlos, Mary y Pedro: cuatro personas."),
        ("abc", "Marta llega justo después de la novena persona de la fila. ¿Qué lugar ocupa?", "Tenth", "Eighth", "Ninth", "Después de ninth viene tenth, el décimo lugar."),
    ],
    ctx=("abc", "En un consultorio de ejemplo te dicen: «Your room is on the sixth floor.» ¿En qué piso está?", "El sexto", "El quinto", "El tercero", "Sixth es el ordinal de seis, es decir, el sexto piso."),
    sc=[("abc", "En Inglés: ¿cuál es el ordinal de tres?", "third", "three", "threeth", "El ordinal irregular de tres es third."),
        ("abc", "En Inglés: ¿cómo se dice «segundo piso»?", "second floor", "two floor", "twoth floor", "El ordinal de dos es second."),
        ("abc", "En Inglés: ¿qué significa «in line»?", "En la fila", "En la casa", "En el piso", "In line quiere decir formado en una fila.")],
    op=("Escribe en tu cuaderno una fila de cinco personas de ejemplo con sus lugares (first a fifth) en cinco oraciones. Después escribe dos oraciones con un piso y un número de sala. Puedes decirlas en voz alta.",
        "Ana is first in line. Pedro is second. Rosa is third. Carlos is fourth. Mary is fifth. The class is on the third floor, in room twelve.",
        ["usa ordinales de first a fifth", "escribe el piso con ordinal y la sala con cardinal", "usa is en todas las oraciones"],
        ["siete oraciones sobre la fila, el piso y la sala"],
        ["escribir fiveth", "usar un cardinal para el lugar"],
        "Pregunta: «¿Escribiste bien fifth y third?»; revisa el cardinal de la sala."),
    reinforce="Cuenta en voz baja de first a tenth y vuelve a empezar sin mirar.",
    extend="Escribe cinco lugares de tu ciudad con su piso o su número en ordinales y cardinales.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy describo a una persona que debo encontrar y digo qué está haciendo ahora con el presente continuo.",
    prior=["Describo personas con adjetivos.", "Uso posesivos como his y her.", "Conozco is y are."],
    explain=[
        "Cuando buscas a alguien describes cómo es y qué está haciendo en ese momento. Para lo que ocurre ahora usamos el presente continuo: to be más un verbo terminado en -ing. She is waiting. They are wearing hats.",
        "Para formar el -ing agrega -ing al verbo: wait, waiting; look, looking; wear, wearing. Para preguntar, el verbo to be va primero: Is she waiting? Para negar, usa not: She isn't waiting. Con I se usa am: I am looking for my friend.",
        "Para decir dónde está alguien, usa palabras de lugar como next to (al lado de). En un aviso, ordena la información: quién busca, a quién busca, cómo es, qué lleva puesto y dónde espera. Marca esas palabras clave al leer.",
    ],
    vocab=[("look for", "buscar"), ("wear", "llevar puesto"), ("wait", "esperar"), ("next to", "al lado de"), ("door", "puerta"), ("jacket", "chaqueta"), ("green", "verde"), ("help", "ayuda, ayudar")],
    worked=[
        ("Decir qué hace alguien ahora", "Rosa espera junto a la puerta. ¿Cómo lo dices en presente continuo?", ["Uso She is porque habla de una mujer.", "Agrego -ing al verbo wait: waiting.", "Digo el lugar con next to: next to the door."], "She is waiting next to the door."),
        ("Describir para encontrar", "Debes describir a Pedro: alto, chaqueta azul. ¿Qué dices?", ["Primero el aspecto: He is tall.", "Después lo que lleva: He is wearing a blue jacket.", "Junto las dos oraciones."], "He is tall. He is wearing a blue jacket."),
    ],
    mistakes=[("Decir «He is wear a hat».", "Se usa la forma base del verbo después de is.", "Con el presente continuo el verbo lleva -ing: He is wearing a hat."),
              ("Decir «He wearing a hat» sin is.", "Se olvida el verbo to be.", "Agrega is: He is wearing a hat.")],
    T=[
        ("abc", "{F} ¿A quién busca Mr. Lopez?", "A Rosa", "A Ana", "A Carlos", "El aviso dice Mr. Lopez is looking for his friend, Rosa."),
        ("abc", "{F} ¿Qué lleva puesto Rosa?", "Una chaqueta verde", "Un gorro rojo", "Una bufanda azul", "El aviso dice She is wearing a green jacket."),
        ("abc", "{F} ¿Dónde espera Rosa?", "Al lado de la puerta", "En el piso diez", "En la fila", "El aviso dice She is waiting next to the door."),
        ("abc", "{F} ¿Cómo se siente Rosa?", "Preocupada, no cansada", "Feliz y cansada", "Triste y con hambre", "El aviso dice She is not tired, but she is worried."),
        ("abc", "¿Cuál es el presente continuo correcto para «Ella espera»?", "She is waiting.", "She waiting is.", "She wait.", "El presente continuo usa is y el verbo con -ing."),
        ("ab", "¿Cuál es correcta para «Ellos esperan»?", "They are waiting.", "They is waiting.", "Con they el verbo to be es are."),
        ("abc", "Completa: «I am ___ for my friend.» (busco)", "looking", "look", "looks", "Con am se usa el verbo con -ing: looking."),
        ("Escribe la forma con -ing de wear (llevar puesto).", "wearing", "Al verbo wear se le agrega -ing para el presente continuo."),
        ("abc", "Pedro es alto, lleva una chaqueta azul y está junto a la puerta. ¿Cuál es la mejor descripción?", "He is tall. He is wearing a blue jacket. He is next to the door.", "He tall. He wear blue jacket. He door next.", "He is tall. He wear a blue jacket. He are next to door.", "La mejor descripción usa is, -ing y las palabras de lugar completas."),
        ("ab", "Mr. Lopez dice «He is wear a hat». ¿Cuál es la corrección?", "He is wearing a hat.", "He wearing is a hat.", "Después de is el verbo lleva -ing."),
        ("abc", "{F} ¿Qué palabra del aviso muestra una acción que ocurre ahora?", "waiting", "tall", "green", "Waiting lleva -ing y es una acción en curso."),
        ("abc", "Quieres pedir ayuda con cortesía. ¿Qué frase usas?", "Please help.", "Help now no.", "You are help.", "Please help es una expresión cortés para pedir ayuda."),
        ("abc", "{F} ¿Qué dos datos de Rosa sirven para reconocerla entre mucha gente?", "Es alta y lleva una chaqueta verde", "Está cansada y tiene hambre", "Es panadera y tiene 40 años", "Aspecto y ropa son claves para reconocer a alguien a la distancia."),
    ],
    ctx=("abc", "En un terminal de ejemplo buscas a un compañero de trabajo: es bajo, lleva un sombrero negro y espera junto a la puerta. ¿Qué dices a un guardia?", "He is short. He is wearing a black hat. He is waiting next to the door.", "He short. He wear a black hat. He wait next door.", "He is shorts. He is wear black. He waiting.", "La respuesta correcta usa is, el verbo con -ing y next to the door."),
    sc=[("abc", "En Inglés: ¿cómo se forma el presente continuo?", "Con to be y un verbo con -ing", "Con do y el verbo", "Solo con el verbo en infinitivo", "El presente continuo lleva am, is o are más el verbo con -ing."),
        ("abc", "En Inglés: ¿cómo dices «estoy buscando mi chaqueta»?", "I am looking for my jacket.", "I looking for my jacket.", "I am look my jacket.", "Con am se usa looking y la preposición for."),
        ("abc", "En Inglés: ¿qué significa «next to»?", "Al lado de", "Detrás de", "Encima de", "Next to indica que algo está junto a otra cosa.")],
    op=("Escribe en tu cuaderno un aviso de seis líneas para encontrar a una persona de ejemplo: cómo es (aspecto y emoción), qué lleva puesto y dónde espera. Usa is, el verbo con -ing y next to. Puedes leerlo en voz alta.",
        "Attention, please. Mr. Diaz is looking for his friend, Marta. She is tall. She is wearing a red jacket. She is waiting next to the door. She is happy.",
        ["usa is y el verbo con -ing", "dice cómo es la persona", "dice dónde espera con next to"],
        ["un aviso de seis líneas"],
        ["olvidar el verbo is", "usar el verbo sin -ing"],
        "Pregunta: «¿Podría alguien encontrar a la persona con tu aviso?»; revisa los verbos."),
    reinforce="Describe en voz baja a una persona que ves pasar usando is y un verbo con -ing.",
    extend="Escribe una descripción de ejemplo de tres personas en una fila, con aspecto, ropa y acción.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo aprendido: preguntar datos, describir, posesivos, ordinales y el presente continuo.",
    prior=["Hago preguntas con What, Where, Who y How old.", "Describo personas y objetos.", "Uso ordinales y cardinales."],
    explain=[
        "Para revisar, usa esta lista: preguntas personales, adjetivos de aspecto y emoción, posesivos y demostrativos, ordinales y el presente continuo. En cada punto marca lo que haces bien y lo que quieres repasar.",
        "Si algo no sale, busca el motivo. ¿Olvidaste el verbo to be? ¿Pusiste el adjetivo después del sustantivo? ¿Usaste el cardinal donde iba el ordinal? Corrige con tu propio ejemplo y repítelo en voz alta.",
        "Para avanzar usa el inglés fuera de clase: describe a las personas de tu entorno, di de quién son los objetos de tu casa y cuenta lugares en una fila. Pedir ayuda a otra persona forma parte del aprendizaje.",
    ],
    vocab=[("in line", "en la fila"), ("first", "primero o primera"), ("second", "segundo o segunda"), ("tall", "alto o alta"), ("short", "bajo o baja"), ("tired", "cansado o cansada"), ("her", "su (de ella)"), ("his", "su (de él)")],
    worked=[
        ("Revisar una descripción", "Un compañero escribe: «Carmen tall. She is wear red jacket». Revisa y corrige.", ["Falta el verbo en Carmen tall: Carmen is tall.", "Después de is el verbo lleva -ing: wearing.", "Falta el artículo a: a red jacket."], "Carmen is tall. She is wearing a red jacket."),
        ("Elegir el posesivo", "Diego es hermano de Carmen. ¿Cómo dices «su hermano» sobre Carmen?", ["Carmen es mujer: uso her.", "El posesivo va antes del sustantivo: her brother.", "Lo uso en una oración con is."], "Her brother is Diego."),
    ],
    mistakes=[("Poner el adjetivo después del sustantivo.", "Se copia el orden del español.", "Pon el adjetivo antes: a tall woman."),
              ("Confundir his y her.", "Se mira al objeto y no al dueño.", "Elige el posesivo según el dueño: his para un hombre, her para una mujer.")],
    T=[
        ("abc", "{F} ¿Quién está primera en la fila?", "Carmen", "Diego", "Marta", "El texto dice This is Carmen. She is first in line."),
        ("abc", "{F} ¿Qué lleva puesto Carmen?", "Una chaqueta roja", "Una chaqueta verde", "Un abrigo azul", "El texto dice She is wearing a red jacket."),
        ("abc", "{F} ¿Cómo está Diego?", "Cansado", "Feliz", "Preocupado", "El texto dice He is short, and he is tired."),
        ("ab", "{F} ¿Cuál oración es verdadera?", "Diego is second in line.", "Diego is first in line.", "El texto dice He is second in line sobre Diego."),
        ("abc", "{F} ¿Qué palabra señala las llaves que están lejos?", "Those", "These", "My", "El texto dice Those keys are her keys."),
        ("abc", "Completa: «Marta and Pedro ___ in line.»", "are", "is", "am", "Con dos personas se usa are."),
        ("ab", "Alguien dice «She are tall». ¿Cuál es la corrección?", "She is tall.", "She am tall.", "Con she el verbo to be es is."),
        ("Escribe en inglés la pregunta para saber el origen de una persona. Usa you.", "Where are you from?", "El origen se pregunta con where y el verbo are antes de you."),
        ("abc", "Estás cuarto en la fila. ¿Cómo lo dices?", "I'm fourth in line.", "I'm four in line.", "I'm forth in line.", "Se usa el ordinal fourth para el lugar en la fila."),
        ("abc", "Marta tiene una bolsa azul. ¿Cuál oración es correcta?", "Her bag is blue.", "She bag is blue.", "Hers bag is blue.", "Her es el posesivo que va antes del sustantivo."),
        ("ab", "¿Qué orden es correcto?", "a short man", "a man short", "En inglés el adjetivo va antes del sustantivo."),
        ("abc", "¿Qué frase es presente continuo?", "He is waiting.", "He waits.", "He waited.", "El presente continuo usa is y un verbo con -ing."),
        ("abc", GUION + "Pedro is wearing a blue jacket. He is waiting next to the door. ¿Dónde espera Pedro?", "Al lado de la puerta", "En el piso diez", "En la fila", "La pista es next to the door."),
    ],
    ctx=("abc", "Una compañera de trabajo te pregunta cómo es un amigo que va a buscarte al terminal, para reconocerlo. Es hombre, alto, está cansado y lleva una chaqueta negra. ¿Qué respondes?", "He is tall. He is tired. He is wearing a black jacket.", "He tall. He tired. He wear black jacket.", "She is tall. She is tired. She wearing black.", "La respuesta usa he para un hombre, el verbo is y el presente continuo."),
    sc=[("abc", "En Inglés: ¿cuál es la forma correcta?", "What is your name?", "What your name is?", "Where is your name?", "En la pregunta el verbo va antes del sujeto."),
        ("abc", "En Inglés: ¿cómo se dice «el tercer piso»?", "the third floor", "the three floor", "the threeth floor", "El ordinal de tres es third."),
        ("abc", "En Inglés: ¿qué significa «these»?", "Estos o estas, cerca", "Esos o esas, lejos", "Mi o mis", "La palabra these señala varias cosas que están cerca.")],
    op=("Escribe en tu cuaderno una descripción de siete oraciones de una persona de ejemplo: una pregunta y su respuesta sobre su origen, aspecto, cómo está, de quién es una cosa, su lugar en una fila y qué hace ahora. Léela en voz alta si quieres. Después anota qué quieres repasar.",
        "Where is Rosa from? She is from Chile. She is tall. She is happy. This is her bag. She is third in line. She is waiting next to the door.",
        ["usa una pregunta y su respuesta", "usa un adjetivo y un posesivo", "usa un ordinal y el presente continuo", "anota qué quiere repasar"],
        ["siete oraciones y una lista de qué repasar"],
        ["olvidar el verbo to be", "usar el verbo sin -ing"],
        "Pregunta: «¿Qué oración quedó más clara?»; si te cuesta, repite solo la parte más difícil."),
    reinforce="Elige una frase de cada clase y dila en voz alta tres veces.",
    extend="Escribe una descripción de tres personas de tu entorno con aspecto, emoción y posesivos.",
)

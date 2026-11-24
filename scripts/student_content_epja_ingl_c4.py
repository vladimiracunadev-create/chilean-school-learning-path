"""Inglés EPJA Nivel 2, módulo 3 (parte 4): OAD-12, presentar un referente personal frente a la clase (datos básicos, rutina, proyectos): preparar, ordenar y presentar. Todos los textos son inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-12"

F1 = ("Presentación de ejemplo de Luis: «Hello. I'm going to talk about my aunt Carmen. She is fifty-eight years old. She is a nurse. She lives in the south. "
      "I admire her because she helps many people.»")

F2 = ("Presentación de ejemplo de Marta: «Today I'm going to talk about Mr. Soto. He is a baker. He is very kind and hard-working. He is also funny. "
      "He helps his neighbors. He is tall and strong. I admire him because he always works with a smile.»")

F3 = ("Esquema de ejemplo de una presentación breve: 1) «Hello. My name is Ana. Today I'm going to talk about Mrs. Rojas.» "
      "2) «She is sixty years old. She is a teacher.» 3) «She wakes up at six. She usually walks to school.» "
      "4) «She wants to write a book.» 5) «Thank you. Do you have questions?»")

F4 = (GUION + "Transcripción de una presentación de ejemplo, leída en voz alta: «Hello. My name is Carlos. Today I'm going to talk about my neighbor, Mrs. Diaz. "
      "She is seventy years old. She is a gardener. She is kind and funny. She wakes up at five. She always waters the plants first. "
      "She would like to teach children to plant tomatoes. Thank you.»")

F5 = ("Notas de ejemplo, desordenadas, para una presentación sobre Mr. Perez: (a) «Thank you. Do you have questions?» (b) «He wants to open a bike shop.» "
      "(c) «Hello. My name is Pedro. Today I'm going to talk about Mr. Perez.» (d) «He is forty years old. He is a mechanic.» (e) «He wakes up at six. He usually works until six.»")

F6 = ("Presentación de repaso de Rosa: «Hello, my name is Rosa. Today I'm going to talk about Mrs. Vera. She is sixty-two years old. She is a seamstress. "
      "She is patient and generous. She wakes up at six. First, she makes tea. Then she sews. She doesn't work on Sunday. "
      "She wants to teach sewing in my neighborhood. Thank you.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy conozco cómo suena una presentación breve en inglés sobre una persona que admiro y la entiendo.",
    prior=["Hablo de mi familia y de mi barrio en español.", "Digo la edad y la profesión de una persona.", "Conozco verbos de la rutina."],
    explain=[
        "Un referente personal es una persona que admiras: alguien de tu familia, de tu barrio o de tu trabajo. Hoy escuchas cómo se presenta a esa persona en inglés, de manera breve y clara frente a un grupo.",
        "Una presentación tiene tres partes: un saludo y el nombre de la persona, algunos datos básicos (edad, profesión, dónde vive) y un cierre con una razón para admirarla. Se usan oraciones simples con is y verbos en presente: «She is a nurse», «She lives in the south».",
        "La expresión «I admire her because…» quiere decir la admiro porque… y sirve para dar una razón. Hoy no se pide hablar perfecto: se pide entender y reconocer las partes. Subraya el saludo, los datos y la razón en el texto.",
    ],
    vocab=[("aunt", "tía"), ("nurse", "enfermera, enfermero"), ("years old", "años de edad"), ("live", "vivir"), ("I admire her", "la admiro"), ("because", "porque"), ("talk about", "hablar de")],
    worked=[
        ("Encontrar los datos básicos", "Texto de ejemplo: «She is fifty-eight years old. She is a nurse.»", ["Subrayo la edad: fifty-eight years old.", "Subrayo la profesión: nurse.", "Confirmo quién es: she, la tía."], "Tiene 58 años y es enfermera"),
        ("Encontrar la razón", "Oración de ejemplo: «I admire her because she helps many people.»", ["Busco because.", "Lo que sigue es la razón: she helps many people.", "Concluyo por qué la admira."], "La admira porque ayuda a muchas personas"),
    ],
    mistakes=[("Decir «She has fifty-eight years».", "Se traduce «tiene 58 años» palabra por palabra.", "En inglés se dice «She is fifty-eight years old»."),
              ("Decir «I admire she».", "Después de admire se usa her, no she.", "Se dice «I admire her»; her es la forma para ella.")],
    T=[
        ("abc", "{F} ¿De quién va a hablar Luis?", "De su tía Carmen", "De su mamá", "De su vecina", "Luis dice «I'm going to talk about my aunt Carmen»."),
        ("ab", "{F} ¿Qué profesión tiene Carmen?", "Enfermera", "Profesora", "Luis dice que Carmen is a nurse."),
        ("{F} ¿Cuántos años tiene Carmen? Escribe solo el número.", "58", "El texto dice fifty-eight years old, o sea cincuenta y ocho."),
        ("abc", "{F} ¿Dónde vive Carmen?", "En el sur", "En el norte", "En el centro", "El texto dice «She lives in the south»."),
        ("abc", "{F} ¿Por qué Luis admira a Carmen?", "Porque ayuda a muchas personas", "Porque es rica", "Porque es joven", "El texto dice «because she helps many people»."),
        ("abc", "{F} ¿Qué palabra introduce la razón?", "because", "years", "about", "Because quiere decir porque y abre la razón."),
        ("abc", "Completa: She ___ fifty-eight years old.", "is", "has", "are", "Para la edad en inglés se usa is, no has."),
        ("abc", "Elige la oración correcta para «La admiro».", "I admire her.", "I admire she.", "I admire hers.", "Her es la forma que va después del verbo."),
        ("Ordena las palabras: a / is / she / nurse.", "She is a nurse.", "La estructura es sujeto, is, a y la profesión."),
        ("ab", "Verdadero o falso razonado: Carmen es profesora según {F}", "Falso: es enfermera", "Verdadero: enseña", "El texto dice que Carmen is a nurse."),
        ("ab", "¿Qué frase sirve para comenzar una presentación?", "Hello. I'm going to talk about my aunt.", "Goodbye. I admire her.", "Hello abre la presentación y dice de quién se va a hablar."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Carmen is a teacher.", "Carmen is a nurse.", "Carmen lives in the south.", "El texto dice que Carmen es enfermera, no profesora."),
        ("abc", "¿Cuál oración tiene un error?", "She has sixty years.", "She is sixty years old.", "He is forty years old.", "En inglés la edad se dice con is y years old."),
    ],
    ctx=("abc", "En tu curso de inglés de ejemplo la profesora pide que cuentes en una oración por qué admiras a una vecina de ejemplo, que ayuda a las personas mayores. ¿Qué dices?", "I admire her because she helps older people.", "I admire she because help older people.", "I admire her because helps.", "La estructura es I admire her because más una oración completa."),
    sc=[("En Inglés: ¿cómo se dice «tiene 40 años» de un hombre?", "He is forty years old", "La edad se dice con is y years old."),
        ("En Inglés: ¿qué significa «because»?", "porque", "Because introduce la razón de lo que se dice."),
        ("En Inglés: ¿cómo dices «Voy a hablar de mi vecina»?", "I'm going to talk about my neighbor", "I'm going to talk about es una expresión de inicio.")],
    op=("Con {F} como modelo, escribe o di tres oraciones sobre una persona que admiras (usa datos inventados si lo prefieres): su nombre, su profesión y por qué la admiras.",
        "I'm going to talk about my neighbor Mrs. Silva. She is a gardener. I admire her because she is always kind.",
        ["dice el nombre o parentesco", "dice la profesión", "da una razón con because"],
        ["tres oraciones dichas o escritas"],
        ["decir has en lugar de is", "olvidar because"],
        "Pregunta: «¿Por qué admiras a esa persona?»"),
    reinforce="Escribe en tarjetas las palabras de la clase y su significado.",
    extend="Anota los datos básicos de una persona que admiras en español y trata de decir dos en inglés.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo adjetivos para describir a una persona y los uso para presentar un referente.",
    prior=["Reconozco los datos básicos de una presentación.", "Uso is con he y she.", "Sé hablar de profesiones simples."],
    explain=[
        "Para presentar a una persona se usan adjetivos, que son palabras que dicen cómo es: kind (amable), hard-working (trabajador), funny (divertido), tall (alto), strong (fuerte) y helpful (servicial). Se ponen después de is: «He is kind».",
        "Si quieres dar más fuerza, se agrega very: «He is very kind». Para sumar otra característica se usa and o also: «He is kind and funny», «He is also tall». No cambian cuando hablas de hombres o mujeres: «She is kind», «He is kind».",
        "Al escuchar o leer una presentación, subraya los adjetivos: te dicen cómo es la persona. Así puedes explicar por qué la admiran. Recuerda: «He helps his neighbors» quiere decir ayuda a sus vecinos; el verbo con he lleva -s.",
    ],
    vocab=[("kind", "amable"), ("hard-working", "trabajador"), ("funny", "divertido"), ("tall", "alto"), ("strong", "fuerte"), ("baker", "panadero"), ("neighbor", "vecino")],
    worked=[
        ("Reconocer los adjetivos", "Oración de ejemplo: «He is very kind and hard-working.»", ["Subrayo kind y hard-working.", "Very refuerza kind.", "Los adjetivos dicen cómo es: amable y trabajador."], "Es muy amable y trabajador"),
        ("Armar una descripción", "Dato de ejemplo: ella es divertida y fuerte.", ["Empiezo con She is.", "Agrego los dos adjetivos con and.", "Reviso que no cambien."], "She is funny and strong"),
    ],
    mistakes=[("Escribir «He is kinds».", "Se agrega -s al adjetivo como si fuera plural.", "El adjetivo no cambia: «He is kind»."),
              ("Poner el adjetivo antes de is.", "El orden del español pasa al inglés.", "Se dice «He is kind», no «He kind is».")],
    T=[
        ("abc", "{F} ¿Qué profesión tiene Mr. Soto?", "Panadero", "Mecánico", "Profesor", "El texto dice «He is a baker»."),
        ("ab", "{F} ¿Cuál adjetivo dice que Mr. Soto trabaja mucho?", "hard-working", "funny", "Hard-working quiere decir trabajador, que se esfuerza mucho."),
        ("abc", "{F} ¿Qué dice el texto sobre cómo es Mr. Soto físicamente?", "Que es alto y fuerte", "Que es bajo", "Que es delgado", "El texto dice «He is tall and strong»."),
        ("abc", "{F} ¿A quién ayuda Mr. Soto?", "A sus vecinos", "A sus hijos", "A sus jefes", "El texto dice «He helps his neighbors»."),
        ("abc", "{F} ¿Por qué lo admira Marta?", "Porque siempre trabaja con una sonrisa", "Porque es rico", "Porque es famoso", "El texto dice «because he always works with a smile»."),
        ("{F} ¿Qué adjetivo significa «divertido»? Escríbelo en inglés.", "funny", "El texto dice que Mr. Soto is also funny."),
        ("abc", "Completa: She is ___ kind.", "very", "much", "many", "Very se pone antes del adjetivo para reforzarlo."),
        ("abc", "Elige la oración correcta.", "He is tall and strong.", "He tall and strong is.", "He is talls and strongs.", "El adjetivo va después de is y no cambia."),
        ("Ordena las palabras: kind / is / very / she.", "She is very kind.", "Very va antes del adjetivo kind, después de is."),
        ("ab", "Verdadero o falso razonado: «tall» significa «bajo».", "Falso: tall significa alto", "Verdadero: significa bajo", "Tall es alto, lo contrario de short."),
        ("ab", "¿Qué frase dice que a una mujer le gusta ayudar?", "She is helpful", "She is hungry", "Helpful quiere decir servicial, que ayuda a otros."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Mr. Soto is a mechanic.", "Mr. Soto is funny.", "Mr. Soto is kind.", "El texto dice que Mr. Soto es panadero, no mecánico."),
        ("abc", "¿Cuál oración tiene un error?", "She is kinds.", "She is kind.", "He is kind and funny.", "El adjetivo no lleva -s en inglés."),
    ],
    ctx=("abc", "Tu compañera de curso dice: «My grandmother is… (ella es muy amable)». ¿Cómo completas la frase en inglés?", "very kind.", "kinds very.", "is kind very.", "Very kind es el adjetivo reforzado, sin cambios."),
    sc=[("En Inglés: ¿qué significa «hard-working»?", "trabajador", "Describe a una persona que trabaja con esfuerzo."),
        ("En Inglés: ¿cómo dices «ella es amable»?", "She is kind", "Is más el adjetivo, sin cambios."),
        ("En Inglés: ¿qué significa «tall»?", "alto", "Tall describe la altura de una persona.")],
    op=("Con {F} como modelo, escribe o di cuatro oraciones sobre una persona que admiras (nombre de ejemplo): su oficio y tres adjetivos que la describen.",
        "Today I'm going to talk about Mrs. Vera. She is a baker. She is kind and hard-working. She is also very funny.",
        ["dice el oficio", "usa tres adjetivos", "usa is con ella o él"],
        ["cuatro oraciones dichas o escritas"],
        ["agregar -s al adjetivo", "poner el adjetivo antes de is"],
        "Pregunta: «¿Qué adjetivo describe mejor a esa persona?»"),
    reinforce="Haz una tabla con los seis adjetivos y una oración con cada uno.",
    extend="Escribe cinco adjetivos de una persona que admiras y trata de unirlos con and.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo, paso a paso, cómo se arma una presentación breve: saludo, datos, rutina, proyecto y cierre.",
    prior=["Describo a una persona con adjetivos.", "Conozco los datos básicos y la rutina.", "Uso I'm going to y she wants to."],
    explain=[
        "Una presentación breve en inglés tiene cinco pasos. Primero, el saludo y el nombre de la persona: «Hello. My name is Ana. Today I'm going to talk about Mrs. Rojas». Segundo, los datos básicos: edad y profesión.",
        "Tercero, una o dos oraciones de su rutina: «She wakes up at six. She usually walks to school». Cuarto, un proyecto: «She wants to write a book». Y quinto, el cierre: «Thank you. Do you have questions?». Con este orden, la persona que escucha te sigue fácilmente.",
        "Para hablar bien frente al grupo: habla despacio, mira a las personas y no tengas miedo de repetir una frase. Si olvidas una palabra, usa otra que conozcas. Una presentación corta y clara vale más que una larga y confusa.",
    ],
    vocab=[("Today I'm going to talk about…", "Hoy voy a hablar de…"), ("teacher", "profesor, profesora"), ("write a book", "escribir un libro"), ("Thank you.", "Gracias."), ("Do you have questions?", "¿Tienen preguntas?"), ("slowly", "despacio")],
    worked=[
        ("Reconocer el orden", "Esquema de ejemplo: saludo, datos, rutina, proyecto, cierre.", ["El saludo va primero.", "Los datos van antes de la rutina.", "El cierre va al final."], "Saludo, datos, rutina, proyecto y cierre"),
        ("Armar el inicio", "Quiero presentar a Mrs. Rojas.", ["Empiezo con Hello.", "Digo mi nombre: My name is Ana.", "Agrego Today I'm going to talk about."], "Hello. My name is Ana. Today I'm going to talk about Mrs. Rojas"),
    ],
    mistakes=[("Empezar la presentación por la rutina sin saludar.", "Se parte por el dato más fácil y se omite el saludo.", "Empieza con Hello y el nombre de la persona."),
              ("Cerrar sin decir gracias.", "Se termina de golpe y la audiencia no sabe que acabaste.", "Cierra con «Thank you. Do you have questions?».")],
    T=[
        ("abc", "{F} ¿De quién va a hablar Ana?", "De Mrs. Rojas", "De su mamá", "De su vecina", "El esquema dice «I'm going to talk about Mrs. Rojas»."),
        ("ab", "{F} ¿Qué profesión tiene Mrs. Rojas?", "Profesora", "Enfermera", "El esquema dice «She is a teacher»."),
        ("{F} ¿Cuántos años tiene Mrs. Rojas? Escribe solo el número.", "60", "El esquema dice «She is sixty years old»."),
        ("abc", "{F} ¿Cómo va Mrs. Rojas normalmente a la escuela?", "Caminando", "En bus", "En auto", "El esquema dice «She usually walks to school»."),
        ("abc", "{F} ¿Qué quiere hacer Mrs. Rojas?", "Escribir un libro", "Viajar", "Abrir una tienda", "El esquema dice «She wants to write a book»."),
        ("abc", "{F} ¿Con qué frase cierra la presentación?", "Thank you. Do you have questions?", "Hello. My name is Ana.", "She wakes up at six.", "El quinto paso es el cierre con gracias y una invitación a preguntar."),
        ("abc", "¿Qué paso va primero en una presentación?", "El saludo y el nombre", "Los proyectos", "El cierre", "Se parte por el saludo y se dice de quién se va a hablar."),
        ("abc", "¿Qué frase sirve para presentar el tema?", "Today I'm going to talk about my neighbor.", "Goodbye, my neighbor.", "I am neighbor today.", "La frase indica el tema de la presentación."),
        ("Ordena las palabras: about / talk / going / I'm / to / Mrs. Rojas.", "I'm going to talk about Mrs. Rojas.", "La expresión I'm going to talk about abre el tema."),
        ("ab", "Verdadero o falso razonado: el cierre debe ir antes de los datos básicos.", "Falso: el cierre va al final", "Verdadero: va antes", "El cierre termina la presentación y va último."),
        ("ab", "¿Dónde va la frase «She wakes up at six»?", "En la parte de la rutina", "En el saludo", "Habla de la rutina diaria de la persona."),
        ("abc", "{F} ¿Cuál oración no está en el esquema?", "She likes to travel.", "She is a teacher.", "She wants to write a book.", "El esquema no menciona nada sobre viajar."),
        ("abc", "¿Cuál oración tiene un error?", "She want to write a book.", "She wants to write a book.", "I want to write a book.", "Con she el verbo want lleva -s."),
    ],
    ctx=("abc", "Imagina que presentas a un vecino de ejemplo frente a tu clase de inglés. ¿Cómo empiezas?", "Hello. My name is Pedro. Today I'm going to talk about my neighbor.", "Thank you. I'm going to talk about my neighbor.", "My neighbor wakes up at six. Hello.", "La presentación comienza con el saludo, tu nombre y el tema."),
    sc=[("En Inglés: ¿cuál es el último paso de la presentación?", "Thank you. Do you have questions?", "El cierre agradece y invita a preguntar."),
        ("En Inglés: ¿cómo dices «Hoy voy a hablar de mi tía»?", "Today I'm going to talk about my aunt", "Es la frase para anunciar el tema."),
        ("En Inglés: ¿cuál palabra significa «despacio»?", "slowly", "Slowly es hablar despacio para que te entiendan.")],
    op=("Con {F} como modelo, escribe el saludo y los datos básicos (nombre de la persona, edad y profesión) de una persona de ejemplo en tres oraciones. Después léelas en voz alta.",
        "Hello. My name is Pedro. Today I'm going to talk about Mrs. Vega. She is fifty years old. She is a baker.",
        ["tiene saludo y tema", "tiene edad y profesión", "usa is con she"],
        ["tres a cinco oraciones escritas y leídas"],
        ["olvidar el saludo", "usar has en vez de is para la edad"],
        "Pregunta: «¿Hablaste despacio y mirando a las personas?»"),
    reinforce="Copia los cinco pasos de la presentación en una hoja y léelos en voz alta.",
    extend="Pide a otra persona que te escuche y te diga qué entendió de tu inicio.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: escucho una presentación completa (leída en voz alta) y respondo preguntas sobre ella.",
    prior=["Conozco las partes de una presentación.", "Uso adjetivos y verbos con -s.", "Entiendo un texto breve."],
    explain=[
        "En esta clase practicas la escucha sin audio: otra persona lee el guion en voz alta, o lo lees tú en voz baja, despacio. Primero escucha toda la presentación y piensa de quién habla. Después escucha otra vez y anota los datos.",
        "Para tomar apuntes, usa una tabla con cuatro filas: nombre, datos básicos, rutina y proyecto. Anota palabras clave, no oraciones completas. Con eso puedes responder preguntas sin releer todo.",
        "Hoy aparece la expresión «would like to teach», que quiere decir le gustaría enseñar. También aparece «waters the plants», que quiere decir riega las plantas. Responde siempre con oraciones completas y usa los datos del guion.",
    ],
    vocab=[("neighbor", "vecina, vecino"), ("gardener", "jardinero, jardinera"), ("water the plants", "regar las plantas"), ("teach", "enseñar"), ("tomatoes", "tomates"), ("seventy", "setenta")],
    worked=[
        ("Tomar apuntes", "Frase del guion: «She is seventy years old. She is a gardener.»", ["Fila datos básicos: 70 años.", "Profesión: jardinera.", "Anoto solo palabras clave."], "Datos básicos: 70 años y jardinera"),
        ("Responder con oración completa", "Pregunta de ejemplo: «What does she do first?»", ["Busco en la rutina: she always waters the plants first.", "Uso she y el verbo con -s.", "Armo la oración."], "She waters the plants first"),
    ],
    mistakes=[("Responder con una sola palabra: «Gardener».", "Parece una respuesta incompleta y poco clara.", "Responde con oración completa: «She is a gardener»."),
              ("Confundir «seventy» con «seventeen».", "Se parecen y se oyen casi igual.", "Seventy es 70; seventeen es 17. Revisa la edad en el contexto.")],
    T=[
        ("abc", "{F} ¿De quién habla Carlos?", "De su vecina Mrs. Diaz", "De su mamá", "De su jefa", "Carlos dice «my neighbor, Mrs. Diaz»."),
        ("ab", "{F} ¿Qué profesión tiene Mrs. Diaz?", "Jardinera", "Profesora", "El guion dice «She is a gardener»."),
        ("{F} ¿Cuántos años tiene Mrs. Diaz? Escribe solo el número.", "70", "El guion dice seventy years old, o sea setenta."),
        ("abc", "{F} ¿Cómo es Mrs. Diaz?", "Amable y divertida", "Seria y callada", "Fuerte y alta", "El guion dice «She is kind and funny»."),
        ("abc", "{F} ¿A qué hora se despierta Mrs. Diaz?", "A las cinco", "A las seis", "A las ocho", "El guion dice «She wakes up at five»."),
        ("abc", "{F} ¿Qué hace Mrs. Diaz primero?", "Riega las plantas", "Cocina", "Va al mercado", "El guion dice «She always waters the plants first»."),
        ("abc", "{F} ¿Qué le gustaría hacer a Mrs. Diaz?", "Enseñar a plantar tomates a los niños", "Vender tomates", "Cerrar su huerta", "El guion dice que le gustaría enseñar a plantar tomates a niños."),
        ("abc", "Completa: She ___ the plants first.", "waters", "water", "watering", "Con she el verbo lleva -s."),
        ("Ordena las palabras (empieza con She): at / wakes up / five / she.", "She wakes up at five.", "El orden es sujeto, verbo y la hora con at."),
        ("ab", "Verdadero o falso razonado: Mrs. Diaz trabaja con maquinaria según {F}", "Falso: es jardinera y riega plantas", "Verdadero: es mecánica", "El guion dice que riega plantas, no que use maquinaria."),
        ("ab", "¿Qué fila de apuntes usarías para «She would like to teach children»?", "La de proyecto", "La de rutina", "Would like to expresa un deseo para el futuro."),
        ("abc", "{F} ¿Cuál resumen es correcto?", "Mrs. Diaz is a kind gardener who wants to teach children.", "Mrs. Diaz is a young teacher.", "Mrs. Diaz is a mechanic.", "El guion dice que es jardinera, amable y quiere enseñar."),
        ("abc", "¿Cuál oración tiene un error?", "She would like teach children.", "She would like to teach children.", "I would like to teach children.", "Falta to entre would like y teach."),
    ],
    ctx=("abc", "Tu compañero presenta a su vecino y dice una edad que suena como «seventy» o «seventeen». No estás seguro. ¿Qué haces?", "Pedirle que repita: «Sorry, can you repeat, please?»", "Anotar cualquier número", "No anotar nada", "Pedir que repita es una estrategia útil para asegurar el dato."),
    sc=[("En Inglés: ¿cómo escribes 70 en inglés?", "seventy", "Seventy es setenta, y seventeen es diecisiete."),
        ("En Inglés: ¿qué significa «water the plants»?", "regar las plantas", "Water como verbo quiere decir regar las plantas."),
        ("En Inglés: ¿cómo dices «le gustaría enseñar»?", "would like to teach", "Would like to más verbo simple.")],
    op=("Pide a otra persona que lea en voz alta {F} Escribe una tabla de cuatro filas (nombre, datos, rutina, proyecto) con palabras clave y después cuenta la presentación con tus palabras en tres oraciones.",
        "Nombre: Mrs. Diaz. Datos: 70 años, jardinera. Rutina: 5, riega las plantas. Proyecto: enseñar a plantar. Mrs. Diaz is seventy and is a gardener. She wakes up at five. She would like to teach children.",
        ["la tabla tiene las cuatro filas", "tres oraciones correctas", "usa -s con she"],
        ["una tabla y tres oraciones"],
        ["confundir seventy con seventeen", "olvidar la -s"],
        "Pregunta: «¿Qué parte de la presentación te costó más oír?»"),
    reinforce="Lee el guion tres veces y subraya cada dato que puedas.",
    extend="Escribe tu propia versión del guion con otra persona y pide a alguien que la lea en voz alta.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy preparo mi presentación: ordeno las partes y la ensayo en voz alta para presentar a una persona de mi comunidad.",
    prior=["Conozco los cinco pasos.", "Uso adjetivos y verbos con -s.", "Escribo oraciones simples."],
    explain=[
        "Para presentar frente a la clase, se prepara y se ensaya. Primero ordena las ideas en los cinco pasos: saludo, datos, rutina, proyecto y cierre. Si tus notas están desordenadas, numera cada una según el orden correcto antes de leer.",
        "Después escribe frases cortas con una idea en cada una. Cuenta las palabras: si una frase tiene más de doce, divídela en dos. Frases cortas son más fáciles de decir y de entender. Ensaya en voz alta, primero solo y luego frente a otra persona.",
        "Mientras ensayas, cuida tres cosas: hablar despacio, decir con claridad la -s de he y she, y terminar con «Thank you». También puedes grabarte, si quieres; no es obligatorio. Lo importante es que te sientas cómodo o cómoda con tu texto.",
    ],
    vocab=[("mechanic", "mecánico"), ("bike shop", "tienda de bicicletas"), ("until", "hasta"), ("practice", "practicar"), ("notes", "notas"), ("ready", "listo, lista")],
    worked=[
        ("Ordenar las notas", "Notas: cierre, saludo, datos.", ["Primero va el saludo.", "Luego los datos.", "Al final el cierre."], "Saludo, datos y cierre"),
        ("Dividir una frase larga", "Frase de ejemplo: «He is forty and he is a mechanic and he works until six».", ["Separo la edad.", "Separo la profesión.", "Separo el horario."], "He is forty. He is a mechanic. He works until six."),
    ],
    mistakes=[("Escribir todo en una sola oración larga.", "Se traduce idea por idea del español sin cortar.", "Escribe una idea por oración."),
              ("Leer sin ensayar.", "Se confía en que saldrá bien en el momento.", "Ensaya al menos tres veces en voz alta.")],
    T=[
        ("abc", "{F} ¿Qué nota va primero en la presentación?", "(c) El saludo con el nombre", "(a) El cierre", "(e) La rutina", "El saludo y el tema abren la presentación."),
        ("ab", "{F} ¿Qué nota va al final?", "(a) Thank you. Do you have questions?", "(b) He wants to open a bike shop.", "El cierre siempre va al final."),
        ("abc", "{F} ¿Qué nota habla del proyecto de Mr. Perez?", "(b)", "(d)", "(e)", "La nota (b) dice que quiere abrir una tienda de bicicletas."),
        ("{F} ¿Qué profesión tiene Mr. Perez? Escribe la palabra en inglés.", "mechanic", "La nota (d) dice que Mr. Perez es mecánico."),
        ("abc", "{F} ¿Cuál es el orden correcto de las notas?", "(c), (d), (e), (b), (a)", "(a), (b), (c), (d), (e)", "(d), (c), (a), (b), (e)", "El orden es saludo, datos, rutina, proyecto y cierre."),
        ("abc", "{F} ¿Hasta qué hora trabaja Mr. Perez usually?", "Hasta las seis", "Hasta las dos", "Hasta las nueve", "La nota (e) dice «usually works until six»."),
        ("abc", "Completa: He wants ___ open a bike shop.", "to", "of", "for", "Después de wants va to y el verbo simple."),
        ("abc", "¿Qué hacer si una frase es muy larga?", "Dividirla en dos oraciones cortas", "Decirla más rápido", "Eliminar el cierre", "Las frases cortas son más fáciles de decir y de entender."),
        ("Ordena las palabras: forty / is / he / years old.", "He is forty years old.", "La estructura es sujeto, is, la edad y years old."),
        ("ab", "Verdadero o falso razonado: es mejor ensayar tres veces que leer sin ensayar.", "Verdadero: ensayar da seguridad", "Falso: leer sin ensayar es mejor", "El ensayo ayuda a hablar con claridad y calma."),
        ("ab", "¿Qué frase termina bien una presentación?", "Thank you. Do you have questions?", "Hello, my name is Pedro.", "Esta frase agradece y abre las preguntas."),
        ("abc", "{F} ¿Cuál oración sobre Mr. Perez es falsa?", "Mr. Perez is a teacher.", "Mr. Perez is forty years old.", "Mr. Perez wants to open a bike shop.", "La nota dice que es mecánico, no profesor."),
        ("abc", "¿Cuál oración tiene un error?", "He wake up at six.", "He wakes up at six.", "I wake up at six.", "Con he el verbo lleva -s."),
    ],
    ctx=("abc", "En un taller de comunicación de ejemplo debes presentar a una persona de tu comunidad. Tienes cinco notas desordenadas. ¿Qué haces primero?", "Numerarlas en el orden saludo, datos, rutina, proyecto y cierre", "Leerlas todas rápido", "Borrar las notas", "Ordenar las notas es el primer paso para preparar."),
    sc=[("En Inglés: ¿cuál es el primer paso de la presentación?", "El saludo y el nombre de la persona", "El saludo abre la presentación y presenta a la persona."),
        ("En Inglés: ¿cómo dices «Gracias»?", "Thank you", "Thank you cierra la presentación con cortesía y gratitud."),
        ("En Inglés: ¿qué significa «practice»?", "practicar", "Practice es ensayar varias veces para ganar seguridad.")],
    op=("Con {F} como modelo, prepara tu presentación sobre una persona de tu comunidad (datos inventados). Escribe cinco notas, una por paso, en inglés, y ensáyalas en voz alta.",
        "Hello. My name is Ana. Today I'm going to talk about Mrs. Soto. She is sixty years old. She is a baker. She wakes up at five. She wants to open a school. Thank you.",
        ["cinco notas, una por paso", "oraciones cortas", "usa -s con she o he"],
        ["cinco notas escritas y leídas en voz alta"],
        ["olvidar un paso", "oraciones muy largas"],
        "Pregunta: «¿Cuántas veces ensayaste tu presentación?»"),
    reinforce="Ensaya tu presentación tres veces frente a un espejo o a otra persona.",
    extend="Graba tu presentación, si quieres, y escúchala; anota una cosa que quieras mejorar.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy presento un referente personal, reviso lo logrado en el módulo y decido qué seguir practicando.",
    prior=["Preparo las cinco partes de una presentación.", "Uso adjetivos y verbos con -s.", "Ensayo en voz alta."],
    explain=[
        "En este desempeño aprendiste a presentar a una persona que admiras: saludo, datos básicos, adjetivos, rutina, proyecto y cierre. También practicaste escuchar una presentación y tomar apuntes.",
        "Para presentarla, usa las oraciones cortas que preparaste, habla despacio y mira a las personas. Después, escucha las preguntas: si no entiendes, di «Sorry, can you repeat, please?». Es normal equivocarse; repite o corrige con calma.",
        "Para decidir qué practicar, revisa: ¿olvidas la -s con he o she?, ¿mezclas has e is para la edad?, ¿hablas muy rápido? Elige una cosa y practícala con otra persona esta semana. Cada presentación te da más confianza para hablar en inglés.",
    ],
    vocab=[("seamstress", "costurera"), ("patient", "paciente"), ("generous", "generosa"), ("sew", "coser"), ("tea", "té"), ("neighborhood", "barrio")],
    worked=[
        ("Revisar una presentación", "Oración de ejemplo: «She have sixty years».", ["Veo la edad: se dice con is.", "Cambio have por is.", "Agrego years old."], "She is sixty years old"),
        ("Unir adjetivo y razón", "Dato de ejemplo: ella es paciente y por eso la admiras.", ["Digo cómo es: She is patient.", "Agrego la razón con because.", "Uno las dos ideas."], "I admire her because she is patient"),
    ],
    mistakes=[("Hablar muy rápido y no se entiende.", "Los nervios hacen que se apure.", "Respira y habla despacio, una frase a la vez."),
              ("Cambiar «she» por «he» a mitad de la presentación.", "Se pierde el hilo.", "Revisa la nota: usa el mismo pronombre en todo el texto.")],
    T=[
        ("abc", "{F} ¿Qué profesión tiene Mrs. Vera?", "Costurera", "Cocinera", "Profesora", "El texto dice «She is a seamstress»."),
        ("ab", "{F} ¿Cuántos años tiene Mrs. Vera?", "62", "26", "Sixty-two quiere decir sesenta y dos."),
        ("abc", "{F} ¿Cómo es Mrs. Vera?", "Paciente y generosa", "Seria y callada", "Alta y fuerte", "El texto dice «She is patient and generous»."),
        ("abc", "{F} ¿Qué hace primero Mrs. Vera?", "Prepara té", "Cose", "Va al mercado", "El texto dice «First, she makes tea»."),
        ("abc", "{F} ¿Qué día no trabaja Mrs. Vera?", "El domingo", "El lunes", "El sábado", "El texto dice «She doesn't work on Sunday»."),
        ("{F} ¿Qué verbo significa «coser»? Escríbelo en inglés.", "sew", "El texto dice «Then she sews», o sea luego cose."),
        ("abc", "Completa: She doesn't ___ on Sunday.", "work", "works", "working", "Después de doesn't el verbo queda simple."),
        ("abc", "Elige la oración correcta.", "She wants to teach sewing.", "She want to teach sewing.", "She wants teach sewing.", "Con she va wants y luego to más el verbo simple."),
        ("Ordena las palabras: tea / she / first, / makes.", "First, she makes tea.", "First va al comienzo, con coma."),
        ("ab", "Verdadero o falso razonado: Mrs. Vera trabaja los siete días según {F}", "Falso: no trabaja el domingo", "Verdadero: trabaja todos los días", "El texto dice que no trabaja el domingo."),
        ("ab", "¿Qué frase es el cierre adecuado?", "Thank you.", "Hello.", "Thank you cierra la presentación con cortesía."),
        ("abc", "{F} ¿Cuál oración es falsa?", "Mrs. Vera is a cook.", "Mrs. Vera is patient.", "Mrs. Vera wants to teach sewing.", "El texto dice que es costurera, no cocinera."),
        ("abc", "¿Cuál oración tiene dos errores?", "She have sixty years and sew.", "She is sixty years old.", "She sews every day.", "Faltan is y years old, y sew debe llevar -s."),
    ],
    ctx=("abc", "Después de tu presentación, una compañera te pregunta en inglés «What time does she wake up?». Tú no estás seguro de la hora. ¿Qué respondes?", "Sorry, can you repeat, please?", "I am not.", "Yes, she does.", "Pedir que repitan es una estrategia útil cuando no entiendes."),
    sc=[("En Inglés: ¿cómo dices «Gracias» al terminar?", "Thank you", "Es la forma de cerrar con cortesía."),
        ("En Inglés: ¿cómo dices «ella tiene 62 años»?", "She is sixty-two years old", "La edad se dice con is."),
        ("En Inglés: ¿qué significa «patient»?", "paciente", "Patient describe a quien espera con calma.")],
    op=("Presentación oral o escrita. Con {F} como modelo, presenta a una persona de tu comunidad (datos inventados) en siete oraciones con los cinco pasos, y escribe una frase sobre qué quieres practicar.",
        "Hello. My name is Pedro. Today I'm going to talk about Mrs. Rojas. She is fifty years old. She is a teacher. She is kind and funny. She wakes up at six. She wants to write a book. Thank you. Next, I want to practice the -s.",
        ["tiene los cinco pasos", "usa adjetivos y -s", "dice qué practicar"],
        ["siete oraciones y una frase de siguiente paso"],
        ["olvidar un paso", "no decir qué practicar"],
        "Pregunta: «¿Qué fue lo que mejor te salió en tu presentación?»"),
    reinforce="Elige tu error más frecuente y escribe tres oraciones correctas.",
    extend="Presenta a una persona de tu familia a otra persona, en voz alta, con los cinco pasos.",
)

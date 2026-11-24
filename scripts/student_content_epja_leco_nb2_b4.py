"""Lenguaje y Comunicación EPJA Nivel 2 básico, módulo 2 (parte 4): OAD-08, exponer oralmente ideas respaldadas de forma clara y efectiva. Todo se resuelve en papel: las exposiciones se describen y se ensayan con guion; no hay audio ni público real (vacío declarado)."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-08"

F1 = ("Situación de ejemplo (inventada): En una reunión de vecinos, una persona expone tres minutos sobre un contenedor de reciclaje. Dice: «Buenas tardes. Hoy les hablaré del reciclaje en nuestra cuadra. "
      "Cada semana se juntan unas 40 bolsas de basura, y casi la mitad es papel y envases. Si separamos, la basura baja. Les propongo instalar un contenedor en la esquina.»")
F2 = ("Dos formas de decir lo mismo (de ejemplo). Forma A: «Oye, ¿cachai que van a poner un contenedor en la esquina?». "
      "Forma B: «Les informo que se propone instalar un contenedor en la esquina». Descripciones de una exposición de ejemplo: Persona 1 habla muy bajo y mira el suelo. Persona 2 habla con voz clara, a ritmo pausado, mirando al público.")
F3 = ("Guion de ejemplo (datos inventados). Inicio: «Buenas tardes. Hablaré de por qué la biblioteca debería abrir los sábados». "
      "Desarrollo: «Primero, hoy cierra a las 18:00, según el aviso de la puerta. Segundo, en una encuesta de la sede, 32 de 50 personas dijeron que irían un sábado. Tercero, abrir el sábado significaría 4 horas más de atención». "
      "Cierre: «Por eso propongo abrir los sábados de 10:00 a 14:00».")
F4 = ("Seis ideas para exponer sobre un taller de huerta (de ejemplo). 1) El taller tiene 12 cupos. 2) La profesora usa sombrero de paja. 3) Creo que es una gran oportunidad. "
      "4) Se hace los miércoles a las 17:00 en la sede. 5) En una huerta se pueden cultivar lechugas, tomates y cilantro. 6) Todo el mundo sabe que es lo mejor del barrio.")
F5 = ("Situación de ejemplo (inventada): una persona tiene 3 minutos para exponer en una reunión. Distribuye así: inicio 30 segundos, desarrollo 2 minutos y cierre 30 segundos. "
      "Su guion marcado: «Buenas tardes (pausa). Les presento los resultados de una encuesta (pausa corta). De 50 personas, 32 (énfasis) respondieron que sí. Por eso propongo abrir los sábados (pausa). ¿Alguna pregunta?»")
F6 = ("Pauta de ejemplo con seis criterios: saludó y dijo el tema; ordenó las ideas con inicio, desarrollo y cierre; respaldó cada idea con un dato; usó un registro adecuado; cuidó volumen y ritmo; cerró con una propuesta o resumen. "
      "Exposición descrita (de ejemplo): saludó y dijo el tema, dio dos ideas con su dato, habló bajo en la segunda parte, miró sus papeles todo el tiempo y cerró repitiendo la propuesta.")

build(
    O, 1, F1,
    use="Hoy descubro cómo se prepara una exposición oral: tema, propósito, público e ideas con respaldo.",
    prior=["Puedo explicar algo a otra persona.", "Sé qué es un hecho y qué es una opinión.", "Sé contar algo con inicio y final."],
    explain=[
        "Exponer es hablar ante una audiencia, que son las personas que escuchan, para comunicar un tema. A diferencia de una conversación, la exposición se prepara. Antes de hablar, defines el tema, el propósito y quién te escuchará. Hablar ante otras personas es algo común en reuniones y trámites; ahora lo hacemos con un método.",
        "Una idea respaldada es una idea que acompañas con algo que la apoye: un dato, un ejemplo o una fuente. Si dices que la plaza necesita luz, un respaldo es «tres de las cinco luminarias están apagadas». Sin respaldo, la idea queda como simple opinión.",
        "También importa la información fidedigna, que es la que viene de una fuente identificable y se puede comprobar. Si dices un número, que se sepa de dónde sale. Así la audiencia confía en lo que escucha y puede preguntar con claridad.",
    ],
    vocab=[("exponer", "hablar ante una audiencia para comunicar un tema"), ("audiencia", "las personas que escuchan"), ("idea respaldada", "idea apoyada con un dato, un ejemplo o una fuente"), ("información fidedigna", "información que viene de una fuente identificable y se puede comprobar")],
    worked=[
        ("Tema, propósito y audiencia", "Exposición de ejemplo (datos inventados): «Buenas tardes. Hoy les hablaré de las filas en el consultorio. En una semana se contaron 120 personas en la fila de la mañana y 45 esperaron más de una hora. Propongo abrir un segundo mesón».", ["Tema: las filas en el consultorio.", "Propósito: proponer abrir un segundo mesón.", "Audiencia: las personas presentes en la reunión."], "Tema: filas; propósito: proponer un segundo mesón; audiencia: quienes asisten."),
        ("Idea con respaldo", "La misma exposición de las filas.", ["Idea: la espera es larga.", "Respaldo: 45 de 120 personas esperaron más de una hora.", "La idea con el dato forma una idea respaldada."], "Idea: la espera es larga; respaldo: 45 de 120 esperaron más de una hora."),
    ],
    mistakes=[
        ("Hablar sin preparar el tema ni el propósito.", "La audiencia no entiende para qué se les habla.", "Define tema, propósito y público antes de empezar."),
        ("Dar una idea sin ningún respaldo.", "Parece solo una opinión personal.", "Agrega un dato, un ejemplo o una fuente."),
    ],
    T=[
        ("abc", "{F} ¿De qué trata la exposición?", "Del reciclaje en la cuadra", "Del transporte público", "De un taller de costura", "La persona anuncia que hablará del reciclaje."),
        ("ab", "{F} ¿Cuál es su propósito?", "Proponer instalar un contenedor en la esquina", "Contar un chiste", "La última oración presenta la propuesta."),
        ("{F} ¿Cuántas bolsas de basura se juntan cada semana según la exposición? (un número)", "40", "La persona dice que se juntan unas 40 bolsas."),
        ("abc", "{F} ¿Quién es la audiencia?", "Vecinos reunidos", "Un tribunal", "Una radio", "La exposición ocurre en una reunión de vecinos, que es la audiencia."),
        ("=", "{F} Si casi la mitad de 40 bolsas es papel y envases, ¿cuántas bolsas serían más o menos la mitad exacta?", "40/2", "La mitad de 40 es 20 bolsas.", "bolsas"),
        ("ab", "{F} ¿«Casi la mitad es papel y envases» es un dato o una opinión?", "Un dato que respalda la idea", "Una opinión personal", "Se puede comprobar revisando las bolsas."),
        ("abc", "{F} ¿Qué es una idea respaldada?", "Una idea apoyada en un dato, ejemplo o fuente", "Una idea sin razón", "Una idea muy larga", "El respaldo da fuerza a la idea."),
        ("ab", "{F} ¿«Les propongo instalar un contenedor» es parte del propósito?", "Sí, muestra qué quiere lograr", "No, es un dato", "Es la propuesta que la exposición busca lograr."),
        ("abc", "En Lenguaje EPJA: ¿qué es información fidedigna en una exposición?", "La que viene de una fuente identificable y se puede comprobar", "La que escuché en la calle sin autor", "La que me parece más lógica", "Se puede verificar y se sabe de dónde sale."),
        ("ab", "Una persona dice: «Según el registro de la sede, vinieron 60 personas». ¿Qué tiene de bueno?", "Nombra la fuente del dato", "Es muy corta", "La fuente permite comprobar el número."),
        ("abc", "Antes de exponer, ¿qué conviene definir?", "Tema, propósito y audiencia", "Solo la ropa", "Solo la hora de llegada", "Con esos tres elementos se arma el discurso."),
        ("ab", "Idea de ejemplo: «El bus se atrasa mucho». ¿Cuál es un respaldo mejor?", "En marzo, 8 de 10 viajes se atrasaron más de 10 minutos", "Todo el mundo lo sabe", "El dato concreto apoya la idea y se puede comprobar."),
        ("abc", "Una exposición se diferencia de una conversación porque...", "se prepara con un tema y un propósito", "no se habla", "dura siempre una hora", "Se piensa de antemano qué decir y para qué."),
    ],
    ctx=("abc", "En una reunión de vecinos se debe pedir que la sede preste las sillas para un evento. ¿Qué respaldo es más útil en la exposición?", "Un dato de cuántas sillas hay y cuántas se necesitan", "Que las sillas son bonitas", "Que todo el mundo quiere sillas", "El dato permite decidir y se puede comprobar."),
    sc=[("En Lenguaje EPJA: ¿qué es la audiencia?", "Las personas que escuchan", "A ellas se dirige lo que se dice."),
        ("¿Qué es una idea respaldada?", "Una idea con dato, ejemplo o fuente", "El respaldo con un dato da confianza porque la idea se puede comprobar."),
        ("¿Qué defino antes de exponer?", "Tema, propósito y audiencia", "Esos tres elementos ordenan la preparación.")],
    op=("Elige uno de estos temas de ejemplo: a) abrir la sede un día más, b) cambiar el horario de la feria, c) instalar más basureros en la plaza. Escribe: tema, propósito, audiencia y dos ideas, cada una con su respaldo (un dato inventado y rotulado «de ejemplo»).",
        "Tema: instalar más basureros en la plaza. Propósito: pedir 3 basureros más. Audiencia: junta de vecinos. Idea 1: la basura queda en el suelo; respaldo (dato de ejemplo): los 2 basureros actuales se llenan los sábados. Idea 2: la plaza se ve más limpia con más basureros; respaldo (dato de ejemplo): en otra plaza con 5 hay menos basura en el suelo.",
        ["define tema, propósito y audiencia", "escribe dos ideas", "da un respaldo a cada idea y rotula el dato como de ejemplo"],
        ["una ficha con tres definiciones y dos ideas respaldadas"],
        ["no dar respaldo", "copiar datos reales sin fuente"],
        "Pregunta: «¿Cada idea tiene algo que la apoye?»."),
    reinforce="Escribe una oración con un propósito (para qué hablarás) sobre un tema que conozcas.",
    extend="Prepara dos ideas respaldadas sobre un tema de tu barrio y contáselas a alguien.",
)

build(
    O, 2, F2,
    use="Hoy distingo el registro formal e informal, conozco los elementos de la voz y del cuerpo al exponer y amplío vocabulario con sinónimos.",
    prior=["Sé preparar una exposición.", "Sé que se habla distinto según con quién se conversa.", "Conozco sinónimos."],
    explain=[
        "El registro es la manera de hablar según la situación. El registro informal se usa con personas cercanas y es más relajado: «Oye, ¿cachai que van a poner un contenedor?». El registro formal se usa en reuniones o trámites: «Les informo que se propone instalar un contenedor». Ambos son válidos; lo importante es elegir el adecuado.",
        "Al exponer también cuenta cómo hablas. El tono es la actitud de la voz, como serio o cordial. El volumen es qué tan fuerte se habla. La inflexión es el subir y bajar de la voz. El ritmo es la velocidad y las pausas. Los gestos son los movimientos de las manos, la cara y la mirada.",
        "Para decir las cosas con precisión, usa sinónimos y evita repetir. «Proponer» y «sugerir» son parecidos, pero «exigir» es más fuerte. En esta actividad no hay audio: imagina cada voz a partir de la descripción escrita.",
    ],
    vocab=[("registro formal", "manera de hablar adecuada a reuniones o trámites"), ("registro informal", "manera de hablar relajada con personas cercanas"), ("inflexión", "subir y bajar de la voz al hablar"), ("ritmo", "velocidad y pausas con que se habla")],
    worked=[
        ("Reconocer el registro", "Frase A: «Ya poh, vengan todos mañana a la sede». Frase B: «Los invitamos a asistir mañana a la sede».", ["La frase A usa «ya poh», una expresión de conversación cercana.", "La frase B usa «los invitamos a asistir», más cuidada.", "Para una reunión conviene la frase B."], "A es informal y B es formal."),
        ("Mejorar la voz", "Descripción de ejemplo: la persona 3 habla tan rápido que casi no se entiende y no hace pausas.", ["El ritmo es demasiado rápido.", "Debe hablar más pausado.", "También debe hacer una pausa después de cada idea."], "Bajar el ritmo y hacer pausas."),
    ],
    mistakes=[
        ("Creer que el registro informal es incorrecto.", "Es adecuado con personas cercanas.", "Úsalo según la situación y la audiencia."),
        ("Hablar muy rápido para terminar pronto.", "La audiencia no alcanza a entender.", "Haz pausas y habla pausado."),
    ],
    T=[
        ("abc", "{F} ¿Qué forma es más adecuada para una reunión formal?", "La forma B", "La forma A", "Ambas igual", "La forma B usa un vocabulario cuidado."),
        ("ab", "{F} ¿Qué palabra de la forma A marca un registro informal?", "cachai", "informo", "«Cachai» es una expresión de conversación cercana."),
        ("ab", "{F} La forma B, ¿es formal o informal?", "Formal", "Informal", "Usa «Les informo» y «se propone»."),
        ("abc", "{F} ¿Qué problema tiene la persona 1?", "Habla muy bajo", "Habla demasiado fuerte", "No dice nada", "La descripción dice que habla muy bajo."),
        ("ab", "{F} ¿Qué hace bien la persona 2 con la mirada?", "Mira al público", "Mira el suelo", "Mira al público y así conecta con la audiencia."),
        ("abc", "{F} ¿Cuál es el ritmo de la persona 2?", "Pausado", "Muy rápido", "Entrecortado", "El texto dice que habla a ritmo pausado."),
        ("abc", "En Lenguaje EPJA: ¿qué es el volumen al exponer?", "Qué tan fuerte se habla", "La velocidad", "La altura de la persona", "Es la intensidad de la voz."),
        ("ab", "¿Qué es la inflexión?", "El subir y bajar de la voz", "Los gestos de las manos", "Es la entonación variable al hablar."),
        ("abc", "¿Qué son los gestos?", "Movimientos de manos, cara y mirada", "Palabras del guion", "La hora de la reunión", "Los gestos acompañan lo que se dice y ayudan a que se entienda."),
        ("ab", "¿Qué conviene si te dicen que se te oye poco?", "Subir un poco el volumen", "Hablar en secreto", "Un volumen adecuado permite que todos escuchen."),
        ("abc", "¿Qué sinónimo de «proponer» es más suave que «exigir»?", "sugerir", "ordenar", "obligar", "«Sugerir» invita a hacer algo sin presionar, a diferencia de «exigir»."),
        ("ab", "Entre las dos frases, ¿cuál es formal? «Chao, nos vemos» o «Hasta luego, quedamos en contacto».", "Hasta luego, quedamos en contacto", "Chao, nos vemos", "Es más cuidada y apropiada para una reunión."),
        ("abc", "Frase de ejemplo: «Estimados vecinos, solicito su atención». ¿Qué registro usa?", "Formal", "Informal", "Ninguno", "«Estimados» y «solicito» son propios del registro formal."),
    ],
    ctx=("abc", "Se debe presentar una propuesta ante la junta de vecinos y también conversar con un amigo de la cuadra sobre lo mismo. ¿Cómo se adecua el registro?", "Formal ante la junta e informal con el amigo", "Informal siempre", "Formal siempre", "El registro depende de la situación."),
    sc=[("En Lenguaje EPJA: ¿qué es el registro?", "La manera de hablar según la situación", "El registro puede ser formal o informal según la situación y quién escucha."),
        ("¿Qué es la inflexión?", "El subir y bajar de la voz", "Da vida a lo que se dice."),
        ("En Lenguaje EPJA: ¿qué es el ritmo al exponer en voz alta?", "Velocidad y pausas", "Un ritmo pausado, con pausas, permite que la audiencia entienda lo que se dice.")],
    op=("Reescribe en registro formal estas dos frases informales: «Oye, junten las firmas pa' mañana». «Los de la junta no nos pescan». Después describe en dos líneas cómo dirías la primera con tono, volumen y gestos adecuados para una reunión.",
        "Formal 1: «Les solicito reunir las firmas para mañana». Formal 2: «La junta de vecinos no ha atendido nuestro pedido». Descripción: tono cordial, volumen medio, ritmo pausado, mirando a quien escucha.",
        ["reescribe las dos frases en registro formal", "describe tono, volumen y gestos", "mantiene el sentido"],
        ["dos frases reescritas y una descripción"],
        ["mantener palabras informales", "cambiar el sentido"],
        "Pregunta: «¿Esta frase se diría en una reunión formal?»."),
    reinforce="Anota tres frases informales y escribe cómo las dirías en registro formal.",
    extend="Escribe cómo cambiarías tu forma de hablar al explicar algo a un grupo grande y a una sola persona.",
)

build(
    O, 3, F3,
    use="Hoy aprendo a ordenar una exposición con inicio, desarrollo y cierre, respaldando cada idea con información fidedigna.",
    prior=["Sé qué es una idea respaldada.", "Distingo registro formal e informal.", "Sé ordenar ideas con conectores."],
    explain=[
        "Una exposición clara tiene tres partes. En el inicio saludas, dices el tema y el propósito. En el desarrollo presentas las ideas, cada una con su respaldo. En el cierre resumes y haces una propuesta o una pregunta. Así la audiencia sabe en qué parte está.",
        "La progresión temática es el orden en que avanzan las ideas: cada una continúa la anterior sin saltos. Para marcarla se usan palabras de orden como «primero», «segundo», «tercero» y «por eso». En un buen guion, las ideas siguen un camino: el problema, la evidencia y la propuesta.",
        "Cada idea del desarrollo debe tener su respaldo y su fuente. «Según el registro de la municipalidad» o «en una encuesta de la junta» indican de dónde sale el dato. Eso hace que tu información sea fidedigna y que la audiencia pueda confiar.",
    ],
    vocab=[("inicio", "parte donde se saluda y se presenta el tema"), ("desarrollo", "parte donde se explican las ideas con sus respaldos"), ("cierre", "parte final que resume o propone"), ("progresión temática", "orden en que las ideas avanzan sin saltos")],
    worked=[
        ("Reconocer las partes", "Guion de ejemplo (datos inventados): «Buenas tardes. Hablaré de reparar las luminarias de la plaza. Primero, hay 3 luminarias apagadas, según el registro de la municipalidad. Segundo, en una encuesta de la junta, 18 de 30 vecinos dijeron que evitan la plaza de noche. Por eso propongo repararlas».", ["Inicio: «Buenas tardes. Hablaré de reparar las luminarias de la plaza».", "Desarrollo: dos ideas con «primero» y «segundo».", "Cierre: «Por eso propongo repararlas»."], "Las tres partes están claras."),
        ("Ver el respaldo", "El mismo guion de las luminarias.", ["Idea: hay luminarias apagadas.", "Respaldo: «3 luminarias apagadas, según el registro de la municipalidad».", "Idea: los vecinos evitan la plaza.", "Respaldo: «18 de 30 vecinos, en una encuesta de la junta»."], "Cada idea del desarrollo trae un dato con su fuente."),
    ],
    mistakes=[
        ("Empezar sin saludo ni tema.", "La audiencia no sabe de qué se hablará.", "Saluda, di el tema y el propósito."),
        ("Cambiar de tema entre ideas.", "Rompe la progresión y confunde.", "Haz que cada idea continúe a la anterior."),
    ],
    T=[
        ("abc", "{F} ¿De qué trata el guion?", "De abrir la biblioteca los sábados", "De cerrar la biblioteca", "De comprar libros", "El inicio del guion dice de qué trata: abrir la biblioteca los sábados."),
        ("=", "{F} Si la biblioteca abriría de 10:00 a 14:00 los sábados, ¿cuántas horas de atención serían?", "14-10", "De 10 a 14 hay 4 horas, porque 14 menos 10 es 4.", "horas"),
        ("ab", "{F} ¿A qué hora cierra la biblioteca hoy según el aviso de la puerta?", "A las 18:00", "A las 14:00", "El guion cita el aviso de la puerta."),
        ("abc", "{F} ¿Cuántas personas respondieron en la encuesta?", "50", "32", "18", "Se dice «32 de 50 personas», es decir, 50 respondieron."),
        ("=", "{F} ¿Cuántas de las 50 personas encuestadas NO dijeron que irían un sábado?", "50-32", "50 menos 32 son 18 personas.", "personas"),
        ("ab", "{F} ¿Qué parte del guion es «Buenas tardes. Hablaré de por qué…»?", "El inicio", "El cierre", "Es el saludo y la presentación del tema."),
        ("abc", "{F} ¿Qué palabras marcan el orden de las ideas del desarrollo?", "Primero, segundo y tercero", "Buenas tardes", "Por eso", "Son las palabras de orden del guion."),
        ("ab", "{F} ¿«Por eso propongo abrir los sábados» es parte del...?", "cierre", "inicio", "Resume lo dicho y propone algo."),
        ("abc", "{F} ¿Qué fuente tiene el dato de los 32 de 50?", "Una encuesta de la sede", "Un rumor del barrio", "Una publicidad", "El guion lo dice con claridad."),
        ("ab", "¿Qué es una idea sin respaldo?", "Una afirmación sin dato ni fuente", "Una idea con datos", "No se apoya en nada comprobable."),
        ("abc", "Frase de ejemplo: «Según el registro de ventas, se vendieron 120 canastas». ¿Qué mejora la información?", "Nombrar la fuente: el registro de ventas", "Quitar el número", "Hablar más rápido", "La fuente permite comprobar el dato."),
        ("ab", "¿Qué conviene en el cierre?", "Resumir y proponer", "Empezar un tema nuevo", "Un cierre claro deja una idea final."),
        ("abc", "Si una exposición pasa de la feria al gasto del gas sin conexión, ¿qué falla?", "La progresión temática", "El volumen", "La mirada", "Las ideas dan un salto sin relación."),
    ],
    ctx=("abc", "Una persona prepara una exposición sobre pedir más horas para el taller de computación. ¿Cuál es el mejor orden de ideas?", "Saludo y tema, problema con dato, solución con dato, cierre con propuesta", "Cierre, solución, problema", "Solo la propuesta", "Sigue la estructura de inicio, desarrollo y cierre."),
    sc=[("En Lenguaje EPJA: ¿cuáles son las tres partes de una exposición oral?", "Inicio, desarrollo y cierre", "Esas tres partes estructuran lo que se dice y orientan a la audiencia."),
        ("En Lenguaje EPJA: ¿qué es la progresión temática?", "El orden en que las ideas avanzan sin saltos", "Cada idea continúa a la anterior."),
        ("¿Qué respalda cada idea del desarrollo?", "Un dato con su fuente", "Un dato con su fuente le da fuerza a la idea y confianza a la audiencia.")],
    op=("Escribe un guion corto de tres partes para este tema de ejemplo: «Pedir que el consultorio atienda una hora más por la tarde». Datos de ejemplo: hoy cierra a las 17:00; en una encuesta de ejemplo, 24 de 40 personas piden atención hasta las 18:00. Incluye inicio, desarrollo con dos ideas y su respaldo, y cierre con una propuesta.",
        "Inicio: Buenas tardes. Hablaré de pedir que el consultorio atienda una hora más por la tarde. Desarrollo: Primero, hoy cierra a las 17:00, según el aviso de la puerta. Segundo, en una encuesta de ejemplo, 24 de 40 personas piden atención hasta las 18:00. Cierre: Por eso propongo que atienda hasta las 18:00.",
        ["incluye inicio, desarrollo y cierre", "respalda cada idea con un dato y su fuente", "usa palabras de orden", "mantiene el tema"],
        ["un guion de tres partes"],
        ["omitir el cierre", "dar datos sin fuente"],
        "Pregunta: «¿Cada idea continúa a la anterior?»."),
    reinforce="Divide un texto breve en inicio, desarrollo y cierre.",
    extend="Reordena un guion desordenado de cinco frases y explica por qué.",
)

build(
    O, 4, F4,
    use="Hoy practico elegir y ordenar las ideas de una exposición: relevantes, accesorias, hechos y opiniones respaldadas.",
    prior=["Conozco inicio, desarrollo y cierre.", "Distingo hechos y opiniones.", "Sé qué es información relevante y accesoria."],
    explain=[
        "Al preparar una exposición no puedes decir todo. Debes elegir las ideas que sirven a tu propósito. La información relevante es la que ayuda a entender o a decidir. La información accesoria es un detalle que no cambia lo esencial, como el sombrero de quien enseña un taller.",
        "En una exposición puedes dar hechos y también opiniones. Los hechos informan y se pueden comprobar. Las opiniones muestran tu punto de vista y deben decirse como tales, con una razón. Cuidado con las frases como «todo el mundo sabe que», porque ocultan una opinión como si fuera un dato.",
        "Una vez elegidas las ideas, ordénalas. Primero lo que presenta el tema, luego los datos más importantes y al final la opinión con su razón. Así la audiencia primero sabe qué pasa y después entiende por qué lo piensas.",
    ],
    vocab=[("idea relevante", "idea que sirve al propósito de la exposición"), ("idea accesoria", "detalle que no cambia lo esencial"), ("opinión respaldada", "opinión que se apoya en un hecho o una razón"), ("cupo", "lugar disponible para una persona")],
    worked=[
        ("Elegir lo relevante", "Propósito: invitar a una charla de primeros auxilios. Ideas (de ejemplo): a) es el jueves a las 18:00 en la sede; b) el expositor usa chaleco verde; c) hay 25 cupos.", ["Relevantes: a) día, hora y lugar; c) cupos.", "Accesorio: b) el chaleco verde.", "Elijo los datos que ayudan a decidir si ir."], "Las ideas a y c son relevantes; la b es accesoria."),
        ("Opinión y opinión disfrazada", "Frases de ejemplo: «Creo que es una charla muy útil» y «Todos saben que es la mejor charla».", ["La primera se dice como opinión, con «creo que».", "La segunda parece dato, pero no lo es.", "La primera es honesta; la segunda esconde la opinión."], "La primera es opinión honesta; la segunda es opinión disfrazada."),
    ],
    mistakes=[
        ("Incluir todos los detalles que conozco.", "La exposición se alarga y se pierde lo principal.", "Elige lo relevante para el propósito."),
        ("Presentar una opinión como si fuera un hecho.", "La audiencia puede sentirse engañada.", "Dila como opinión y da la razón."),
    ],
    T=[
        ("abc", "{F} ¿Cuántos cupos tiene el taller?", "12", "17", "5", "La idea 1 de la lista dice que el taller tiene 12 cupos."),
        ("ab", "{F} ¿Cuándo es el taller?", "Los miércoles a las 17:00", "Los sábados a las 10:00", "La idea 4 da el día y la hora."),
        ("abc", "{F} ¿Qué idea es accesoria?", "La 2: la profesora usa sombrero de paja", "La 1: tiene 12 cupos", "La 4: se hace los miércoles", "El sombrero no cambia lo que se necesita saber."),
        ("ab", "{F} ¿La idea 3 es hecho u opinión?", "Opinión", "Hecho", "«Gran oportunidad» expresa un juicio personal, no un dato comprobable."),
        ("abc", "{F} ¿Qué idea parece dato pero en realidad es una opinión disfrazada?", "La 6", "La 5", "La 1", "«Todo el mundo sabe que es lo mejor» no trae dato."),
        ("ab", "{F} ¿La idea 5 es un dato?", "Sí, se puede comprobar", "No, es una opinión", "Qué se puede cultivar se verifica en una huerta."),
        ("abc", "{F} Para invitar al taller, ¿qué ideas conviene incluir?", "1, 4 y 5", "Solo la 2", "Solo la 6", "Dan los datos útiles para decidir ir."),
        ("=", "{F} Si ya se inscribieron 7 personas, ¿cuántos cupos quedan?", "12-7", "De 12 cupos, 7 ocupados dejan 5 cupos.", "cupos"),
        ("ab", "{F} ¿Cuál es el mejor orden para exponer?", "Datos primero y opinión con razón al final", "Opinión primero y sin razón", "Los datos dan contexto antes de la opinión."),
        ("abc", "Idea de ejemplo: «Creo que conviene inscribirse luego, porque quedan pocos cupos». ¿Qué tiene?", "Una opinión con razón", "Un hecho puro", "Una idea accesoria", "Da su punto de vista y lo apoya."),
        ("ab", "Frase de ejemplo: «El expositor habló diez minutos con corbata azul». ¿Qué parte es accesoria?", "La corbata azul", "Los diez minutos", "El color de la corbata no cambia el mensaje."),
        ("abc", "Antes de exponer, si tienes diez ideas y poco tiempo, ¿qué haces?", "Elijo las que sirven al propósito", "Digo todas rápido", "Elimino los datos", "Con poco tiempo se prioriza lo relevante para el propósito de la exposición."),
        ("ab", "Frase de ejemplo: «Nadie duda de que es la mejor feria». ¿Qué debe hacer quien expone?", "Dar un dato o decirlo como opinión", "Repetirla con más fuerza", "Una opinión disfrazada pide respaldo o una aclaración."),
    ],
    ctx=("abc", "Una persona tiene dos minutos para invitar al taller de huerta ante una junta de vecinos. ¿Qué ideas elige?", "Cupos, día y hora, qué se cultiva y una opinión con razón", "Todo lo que sabe del taller en detalle", "Solo el color de los delantales", "Ordena lo relevante y cuida el tiempo."),
    sc=[("¿Qué es una idea relevante?", "La que sirve al propósito", "Es necesaria para entender o decidir."),
        ("¿Cómo debo decir mi opinión?", "Como opinión, con una razón", "Así es honesta y se puede debatir."),
        ("¿Qué hago con un detalle accesorio?", "Lo dejo fuera si no hay tiempo", "Un detalle accesorio no es esencial para el mensaje y puede quedar fuera.")],
    op=("Prepara una exposición de un minuto sobre este tema de ejemplo: «Invitar a una jornada de limpieza de la plaza». Datos de ejemplo: el sábado, de 10:00 a 12:00; hay 20 guantes disponibles; un vecino ofreció prestar una carretilla de color rojo. Elige las ideas relevantes, descarta una accesoria y agrega una opinión con razón.",
        "Ideas relevantes: sábado de 10:00 a 12:00; 20 guantes disponibles. Descarto: el color rojo de la carretilla. Opinión: me parece una buena manera de cuidar la plaza, porque entre muchos termina antes.",
        ["elige ideas relevantes", "descarta una accesoria", "agrega una opinión con razón"],
        ["una lista de ideas y la opinión"],
        ["incluir el detalle accesorio", "dar una opinión sin razón"],
        "Pregunta: «¿Esta idea sirve al propósito de mi exposición?»."),
    reinforce="De un aviso, anota dos ideas relevantes y una accesoria.",
    extend="Escribe una opinión con razón sobre tu barrio y dos hechos que la respalden.",
)

build(
    O, 5, F5,
    use="Hoy preparo una exposición para una reunión: reparto el tiempo, marco el guion y practico responder preguntas.",
    prior=["Sé armar inicio, desarrollo y cierre.", "Sé elegir ideas relevantes.", "Conozco el registro formal."],
    explain=[
        "En una reunión suele haber poco tiempo. Por eso se reparte: un inicio breve, un desarrollo con las ideas esenciales y un cierre corto. En la situación de ejemplo, 3 minutos se reparten en 30 segundos de inicio, 2 minutos de desarrollo y 30 segundos de cierre.",
        "Marcar el guion ayuda a decirlo con claridad. Una pausa indica dónde respirar y dejar que la idea se asiente. Un énfasis marca la palabra o el dato clave. Por ejemplo, en «De 50 personas, 32 respondieron que sí», se destaca el número 32. Practicar en voz alta con otra persona ayuda a ajustar el ritmo.",
        "Al terminar, la audiencia puede preguntar. Escucha la pregunta completa, repítela si es necesario y responde con el dato que tienes. Si no sabes algo, dilo con honestidad y ofrece averiguarlo. En esta actividad se ensaya con guion escrito: no hay audio ni público real.",
    ],
    vocab=[("pausa", "detenerse un momento al hablar"), ("énfasis", "decir con más fuerza una palabra o dato clave"), ("guion", "texto preparado para exponer, con marcas"), ("encuesta", "serie de preguntas que se hace a varias personas")],
    worked=[
        ("Repartir el tiempo", "Situación de ejemplo: una persona tiene 5 minutos; el inicio dura 30 segundos y el cierre 30 segundos.", ["Tengo 5 minutos: 5 × 60 = 300 segundos.", "Inicio 30 s + cierre 30 s = 60 s.", "Para el desarrollo quedan 300 − 60 = 240 segundos, es decir, 4 minutos."], "El desarrollo dura 4 minutos."),
        ("Marcar el dato clave", "Frase de ejemplo: «De 40 personas, 24 respondieron que sí».", ["El dato clave es el 24.", "Marco el énfasis en 24 y hago una pausa corta después."], "Se pone énfasis en 24."),
    ],
    mistakes=[
        ("Preparar más ideas de las que caben en el tiempo.", "Hay que apurar o cortar y se pierde el cierre.", "Calcula el tiempo y elige menos ideas."),
        ("Responder una pregunta inventando un dato.", "Se pierde la confianza si luego se descubre.", "Di «no lo sé, lo averiguaré» si no tienes el dato."),
    ],
    T=[
        ("=", "{F} ¿Cuántos segundos tiene el tiempo total de 3 minutos?", "3*60", "Cada minuto tiene 60 segundos y 3 por 60 son 180.", "segundos"),
        ("=", "{F} Si el inicio dura 30 s y el cierre 30 s, ¿cuántos segundos quedan para el desarrollo?", "180-30-30", "180 menos 30 menos 30 son 120 segundos.", "segundos"),
        ("abc", "{F} ¿Cuántos minutos dura el desarrollo?", "2", "1", "3", "120 segundos equivalen a 2 minutos porque cada minuto tiene 60 segundos."),
        ("ab", "{F} ¿Dónde se pone el énfasis en el guion?", "En 32", "En «Buenas tardes»", "El número 32 es el dato clave."),
        ("abc", "{F} ¿Para qué sirve «(pausa)»?", "Para detenerse un momento", "Para gritar", "Para hablar más rápido", "La pausa indica un breve descanso al hablar para que la idea se asiente."),
        ("=", "{F} Si las ideas del desarrollo son 2 y cada una dura lo mismo, ¿cuántos segundos dura cada una?", "120/2", "120 segundos divididos en 2 ideas son 60 segundos cada una.", "segundos"),
        ("ab", "{F} ¿Con qué frase cierra el guion?", "¿Alguna pregunta?", "Buenas tardes", "La frase final invita a la audiencia a preguntar antes de terminar."),
        ("abc", "{F} ¿Qué propone el guion?", "Abrir los sábados", "Cerrar los sábados", "Cambiar el nombre", "La frase «Por eso propongo abrir los sábados» lo dice."),
        ("ab", "Si no sabes la respuesta a una pregunta, ¿qué conviene?", "Decir que lo averiguarás", "Inventar un dato", "Reconocer que no se sabe una cifra mantiene la confianza de quien escucha."),
        ("abc", "Antes de responder una pregunta, ¿qué haces?", "Escucho la pregunta completa", "Interrumpo", "Me voy", "Escuchar completa la pregunta permite responder lo que realmente preguntaron."),
        ("ab", "¿Qué registro conviene en una reunión de la junta?", "Formal", "Informal", "Una reunión de la junta es una situación formal que pide registro formal."),
        ("abc", "Un guion tiene 5 ideas y solo caben 2 en el tiempo. ¿Qué haces?", "Elijo las 2 más relevantes", "Digo las 5 muy rápido", "Cambio el tema", "Cuando el tiempo no alcanza se prioriza lo esencial y se dejan las demás ideas."),
        ("ab", "Practicar en voz alta con otra persona sirve para...", "Ajustar el ritmo y las pausas", "Memorizar sin entender", "Permite probar el guion y mejorarlo."),
    ],
    ctx=("abc", "Una persona tiene 4 minutos en una reunión y la audiencia puede hacer preguntas al final. ¿Cómo se organiza mejor?", "Inicio breve, desarrollo con ideas esenciales, cierre y un tiempo para preguntas", "Hablar los 4 minutos sin cerrar", "Solo hacer preguntas", "Reparte el tiempo y considera las preguntas."),
    sc=[("¿Para qué sirve el énfasis?", "Para destacar un dato clave", "El énfasis es decir con más fuerza el dato clave para que la audiencia lo recuerde."),
        ("¿Qué hago si no sé una respuesta?", "Digo que lo averiguaré", "La honestidad ante una duda mantiene la confianza de la audiencia."),
        ("¿Qué reparto antes de exponer?", "El tiempo", "Repartir el tiempo evita quedarse sin cierre o sin tiempo para las preguntas.")],
    op=("Prepara un guion marcado para 2 minutos sobre este tema de ejemplo: «Pedir que el consultorio cuente con más sillas en la sala de espera». Datos de ejemplo: hay 10 sillas; en una encuesta de ejemplo, 18 de 30 personas esperan de pie. Reparte el tiempo (inicio, desarrollo, cierre), marca dos pausas y un énfasis y escribe una respuesta a la pregunta «¿Cuánto costaría?» sin inventar el dato.",
        "Tiempo: inicio 20 s, desarrollo 80 s, cierre 20 s. Guion: Buenas tardes (pausa). Hablaré de las sillas del consultorio. Hay 10 sillas y 18 de 30 personas (énfasis en 18) esperan de pie (pausa). Por eso pido más sillas. Respuesta: no tengo ese dato, lo averiguaré y lo informaré.",
        ["reparte el tiempo y suma bien", "marca pausas y un énfasis", "responde con honestidad una pregunta que no sabe"],
        ["un guion marcado y una respuesta"],
        ["no sumar bien el tiempo", "inventar el costo"],
        "Pregunta: «¿Los tiempos suman exactamente el total?»."),
    reinforce="Marca con una raya las pausas y subraya el dato clave en un texto breve.",
    extend="Escribe tres preguntas que podría hacer la audiencia y una respuesta posible para cada una.",
)

build(
    O, 6, F6,
    use="Hoy reviso una exposición con una pauta, doy y recibo comentarios y decido qué mejorar.",
    prior=["Sé armar y marcar un guion.", "Cuido registro, voz y respaldo.", "Sé que mejorar lleva práctica."],
    explain=[
        "Revisar una exposición es comparar lo que hiciste con una pauta de criterios claros. La pauta ayuda a mirar con orden: saludo y tema, estructura, respaldo, registro, voz y cierre. No se trata de juzgar a la persona, sino de ver qué se logró y qué se puede mejorar.",
        "Un buen comentario tiene tres partes: qué hizo bien, qué podría mejorar y una sugerencia concreta. Por ejemplo: «Tu saludo y tu tema fueron claros. En la parte final hablaste muy rápido. Prueba hacer una pausa antes de la propuesta». Así la persona sabe qué hacer.",
        "Al recibir comentarios, escucha completo, agradece y elige uno o dos puntos para trabajar. Para mejorar basta una práctica con intención: ensayar en voz alta, con otra persona o ante un espejo. En esta actividad no hay audiencia real ni audio, por eso la pauta se aplica a una descripción escrita.",
    ],
    vocab=[("pauta", "lista de criterios para evaluar algo"), ("comentario", "opinión sobre lo que se hizo, para ayudar a mejorar"), ("sugerencia", "propuesta concreta para mejorar"), ("ensayar", "practicar algo antes de hacerlo ante otras personas")],
    worked=[
        ("Aplicar la pauta", "Exposición descrita (de ejemplo): saludó y dijo el tema, dio tres ideas sin ningún dato, habló con volumen adecuado y cerró resumiendo.", ["Saludó y dijo el tema: logrado.", "Dio tres ideas sin dato: por mejorar el respaldo.", "Volumen adecuado: logrado.", "Cerró resumiendo: logrado."], "Logrados: saludo y tema, volumen y cierre. Por mejorar: respaldo con datos."),
        ("Dar un buen comentario", "La misma exposición descrita.", ["Qué hizo bien: habló claro y con buen volumen.", "Qué mejorar: las ideas no tenían datos.", "Sugerencia: anotar un dato por cada idea antes de exponer."], "Comentario con logro, punto a mejorar y sugerencia."),
    ],
    mistakes=[
        ("Dar un comentario como «Estuvo mal».", "No dice qué ni cómo mejorar.", "Señala qué estuvo bien, qué mejorar y una sugerencia."),
        ("Querer cambiar diez cosas a la vez.", "Es difícil y se desanima.", "Elige uno o dos puntos para la próxima vez."),
    ],
    T=[
        ("abc", "{F} ¿Cuántos criterios tiene la pauta?", "6", "4", "8", "La pauta de la ficha lista seis criterios, desde el saludo hasta el cierre."),
        ("ab", "{F} ¿Se cumplió el criterio «saludó y dijo el tema»?", "Sí", "No", "La exposición descrita dice que saludó y dijo el tema."),
        ("ab", "{F} ¿Se cumplió el criterio «cuidó volumen y ritmo»?", "No del todo, habló bajo en la segunda parte", "Sí, totalmente", "Hubo un tramo con volumen bajo."),
        ("=", "{F} La pauta tiene 6 criterios. Si la exposición cumplió bien 4, ¿cuántos quedan por mejorar?", "6-4", "De 6 criterios, 4 logrados dejan 2 por mejorar.", "criterios"),
        ("abc", "{F} ¿Qué sugerencia concreta ayudaría con la mirada?", "Mirar al público al decir cada dato clave", "Hablar más rápido", "Leer sin levantar la cabeza", "Es una acción específica y posible."),
        ("ab", "{F} ¿Respaldó sus ideas?", "Sí, dio dos ideas con su dato", "No dio datos", "La descripción dice que dio dos ideas con su dato."),
        ("abc", "¿Qué parte NO debe faltar en un buen comentario?", "Una sugerencia concreta", "Una burla", "Una comparación con otras personas", "Con una sugerencia la persona sabe qué hacer."),
        ("ab", "Comentario de ejemplo: «Estuvo mal». ¿Qué le falta?", "Decir qué mejorar y cómo", "Más palabras agresivas", "Decir solo «estuvo mal» no orienta a la persona sobre qué mejorar."),
        ("abc", "Si recibes un comentario sobre tu volumen, ¿qué haces?", "Escucho, agradezco y practico subir un poco", "Me enojo", "Dejo de exponer", "Se acepta como ayuda para mejorar."),
        ("ab", "¿Cuántos puntos conviene trabajar a la vez?", "Uno o dos", "Diez", "Pocos objetivos son más fáciles de lograr."),
        ("abc", "En Lenguaje EPJA: ¿qué es ensayar una exposición?", "Practicarla antes de presentarla", "Aprenderla de memoria sin entenderla", "Leerla una vez", "Ayuda a ajustar tiempo y voz."),
        ("ab", "¿Qué no incluye esta actividad escrita?", "Audio ni público real", "Texto escrito", "Solo se trabaja con descripciones escritas."),
        ("abc", "Frase de ejemplo: «Hablaste claro y ordenado; te sugiero cuidar el ritmo». ¿Qué incluye?", "Un logro y una sugerencia", "Solo una crítica", "Solo una burla", "Reconoce lo bueno y propone mejorar."),
    ],
    ctx=("abc", "Después de una reunión, otra persona le comenta a quien expuso: «Tus datos fueron claros; te hizo falta mirarnos más. Prueba apoyar cada dato mirando a alguien». ¿Qué conviene hacer a quien expuso?", "Agradecer y ensayar mirando al público", "Defenderse y discutir", "No volver a exponer", "Es un comentario útil que puede aplicarse."),
    sc=[("En Lenguaje EPJA: ¿para qué sirve una pauta?", "Para evaluar con criterios claros", "Ordena la mirada sobre lo que se hizo."),
        ("¿Qué tiene un buen comentario?", "Un logro, algo por mejorar y una sugerencia", "Un comentario con un logro y una sugerencia es respetuoso y útil."),
        ("¿Cómo mejoro una exposición?", "Ensayando con intención", "La práctica guiada, con intención y comentarios, ayuda a mejorar paso a paso.")],
    op=("Aplica la pauta de la ficha a esta exposición descrita de ejemplo: «La persona saludó, dijo el tema, ordenó tres ideas con sus datos, usó un registro formal, habló con volumen adecuado y terminó sin proponer nada». Marca cada criterio como logrado o por mejorar y escribe un comentario con un logro, un punto por mejorar y una sugerencia. Cierra con una oración sobre qué aprendiste en estas seis clases.",
        "Logrados: saludo y tema, estructura, respaldo, registro, volumen. Por mejorar: cierre. Comentario: «Tus datos y tu orden fueron muy claros. Te faltó cerrar con una propuesta. Termina con una frase como «Por eso propongo...»». Aprendí a respaldar mis ideas y ordenarlas.",
        ["marca los seis criterios", "escribe un comentario con tres partes", "cierra con lo aprendido"],
        ["una pauta marcada, un comentario y una oración"],
        ["comentar sin sugerencia", "no marcar todos los criterios"],
        "Pregunta: «¿Mi sugerencia dice qué hacer concretamente?»."),
    reinforce="Escribe un comentario de tres partes para una presentación imaginaria.",
    extend="Arma tu propia pauta de cinco criterios para una exposición breve.",
)

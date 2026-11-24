"""Lenguaje y Comunicación EPJA Nivel 2 (5.º y 6.º), módulo 3: OAD-12, comunicar por medio de una presentación oral clara y efectiva.
Todo se resuelve en papel: la voz, el tono y los gestos se describen por escrito (no hay audio ni video reales). Los datos son inventados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los guiones, fichas y datos están escritos en cada ejercicio y son inventados para este cuaderno: "
    "no necesitas audio, video ni internet. Para practicar en voz alta, lee el guion con el tono indicado, a solas o ante una persona de confianza. "
    "Si te da nervios hablar, empieza en voz baja y avanza de a poco: es normal. No escribas datos personales reales."
)

build = make_build(MATERIALS)

O = "EPJA-LECO-NB2-OAD-12"

P1 = ("Dos intervenciones de ejemplo en una reunión de vecinos sobre una plaza. Intervención A (voz baja, mira al suelo): «Eh… bueno… yo quería decir… como que la plaza… no sé, está mal, o algo así.» "
      "Intervención B (voz firme, volumen medio, mira a los presentes): «Buenas tardes. Quiero proponer que arreglemos la plaza. Tiene dos bancas rotas y una luminaria apagada. Propongo que pidamos ayuda a la municipalidad.»")
P2 = ("Presentación de ejemplo con vocabulario impreciso: «Hay un problema con la cosa de la esquina. La cosa no funciona y hay que arreglar eso. Es muy malo para la gente.» "
      "Versión precisa: «El semáforo de la esquina no funciona y los peatones cruzan con riesgo. Pedimos a la municipalidad que lo repare.»")
P3 = ("Datos de ejemplo para una presentación sobre ahorro de agua en casa. Fuente 1 (boletín de ejemplo de una empresa sanitaria de ejemplo, 2024): «Una llave que gotea desperdicia agua todos los días.» "
      "Fuente 2 (blog sin autor ni fecha): «Dicen que con gotear no pasa nada.» Esquema previsto: inicio (tema), desarrollo (problema, causa, solución) y cierre.")
P4 = ("Guion de ejemplo con marcas: «Buenas tardes, / les voy a hablar de las llaves que gotean. // Una llave que gotea / desperdicia agua todos los días. // "
      "Revisen sus llaves / y pidan que las reparen. // Gracias.» (/ = pausa corta; // = pausa larga). Otro guion de ejemplo tiene 240 palabras y se lee a 120 palabras por minuto.")
P5 = ("Guion de ejemplo de una presentación de un minuto en una reunión de vecinos. Inicio: «Buenas tardes, vecinos. Voy a hablar de cómo separar la basura en el pasaje.» "
      "Desarrollo: «Primero, separamos los envases limpios. Segundo, los llevamos al contenedor azul. Tercero, dejamos la basura orgánica en una bolsa aparte.» "
      "Cierre: «Si todos separamos, el pasaje se mantiene limpio. Gracias por escuchar.» Fuente de ejemplo: guía de reciclaje de una junta de vecinos de ejemplo, 2024.")
P6 = ("Rúbrica de ejemplo para una presentación (0 a 2 puntos por criterio): 1) inicio que presenta el tema, 2) ideas ordenadas, 3) información con fuente, 4) voz y gestos adecuados, 5) cierre. "
      "Presentación de ejemplo: inicio 2, ideas ordenadas 2, fuente 1, voz y gestos 1, cierre 2.")

# ============================================================ clase 1
build(
    O, 1, P1,
    use="Hoy descubro qué hace clara una presentación oral, a partir de situaciones como hablar en una reunión de vecinos.",
    prior=["Sé decir lo que pienso a otra persona.", "Conozco tono, volumen y gestos.", "Sé ordenar ideas en un mapa o una lista."],
    explain=[
        "Una presentación oral es un mensaje que se dice en voz alta frente a una audiencia, es decir, frente a las personas que escuchan. Ocurre cuando alguien habla en una reunión, pide algo en una oficina o explica una tarea a otra persona.",
        "Una presentación clara tiene un propósito (para qué hablo), un orden (inicio, desarrollo y cierre) y datos concretos. La voz y el cuerpo también comunican: un volumen adecuado, un ritmo calmado y mirar a las personas dan seguridad y ayudan a entender.",
        "Hay palabras que conviene evitar: las muletillas, que son palabras o sonidos que se repiten sin aportar, como «eh» o «como que». No se trata de hablar perfecto, sino de que el mensaje llegue. Con práctica, todas las personas mejoran.",
    ],
    vocab=[("presentación oral", "mensaje dicho en voz alta ante una audiencia"), ("audiencia", "personas que escuchan"), ("propósito", "para qué se habla"), ("muletilla", "palabra o sonido que se repite sin aportar"), ("progresión", "orden en que avanzan las ideas")],
    worked=[
        ("Comparar dos intervenciones", "Intervención C (voz baja, mira el suelo): «Es que… no sé… el consultorio… como que demora». Intervención D (voz firme, mira a los presentes): «Buenas tardes. Quiero plantear que la espera en el consultorio es larga. Ayer se atendió a 20 personas en cuatro horas (dato de ejemplo). Propongo pedir un segundo mesón».", ["C no dice qué quiere: usa muletillas y frases vagas.", "D saluda, plantea el problema, da un dato concreto y propone una acción.", "La voz firme y la mirada de D refuerzan su mensaje."], "D es más clara: tiene propósito, orden y datos"),
        ("Partes de una presentación", "Una persona presenta: «Buenas tardes. Hoy hablaré de la feria. Hay dos puestos de verduras y uno de pan. Gracias».", ["Inicio: «Buenas tardes. Hoy hablaré de la feria».", "Desarrollo: los dos datos de los puestos.", "Cierre: «Gracias»."], "Tiene inicio, desarrollo y cierre"),
    ],
    mistakes=[("Pensar que hablar bien es hablar mucho o con palabras difíciles.", "Importa que el mensaje se entienda, no que sea largo ni complicado.", "Usa frases cortas, datos concretos y un orden claro."),
              ("Creer que las muletillas son un defecto que no se puede cambiar.", "Con práctica y pausas se reducen.", "En vez de «eh», haz una pausa corta y respira.")],
    T=[
        ("abc", "{F} ¿Cuál intervención dice con claridad lo que se quiere?", "La B", "La A", "Las dos por igual", "B plantea una propuesta concreta; A no dice qué quiere."),
        ("ab", "{F} ¿Qué rasgo tiene la voz de la intervención A?", "Es baja, y la persona mira al suelo", "Es firme, y mira a los presentes", "Así lo indica el guion de A."),
        ("{F} ¿Qué se propone arreglar en la intervención B? Responde con una palabra o dos.", "la plaza", "B dice «proponer que arreglemos la plaza»."),
        ("abc", "{F} ¿Qué datos concretos entrega B?", "Dos bancas rotas y una luminaria apagada", "Que la plaza es bonita", "Que a todos les gusta el parque", "Son hechos que se pueden comprobar."),
        ("ab", "{F} ¿Cuál es el propósito de B?", "Proponer una acción y pedir ayuda", "Contar un chiste", "Termina pidiendo que se solicite ayuda a la municipalidad."),
        ("abc", "{F} ¿Qué dificulta entender a A?", "Las muletillas y la falta de datos", "Que habla de la plaza", "Que saluda al inicio", "«Eh», «como que» y «algo así» no aportan información."),
        ("ab", "¿Qué es una muletilla?", "Una palabra o sonido que se repite sin aportar", "Una frase importante", "Son palabras o sonidos que se repiten sin aportar, como «eh» o «como que»."),
        ("abc", "¿Por qué ayuda mirar a las personas que escuchan?", "Da cercanía y muestra seguridad", "Evita preparar el tema", "Reemplaza los datos", "El contacto visual conecta con la audiencia."),
        ("abc", "{F} Si B hablara muy rápido y en voz baja, ¿qué pasaría?", "Se perdería claridad, aunque el contenido sea bueno", "Se entendería mejor", "Nada cambiaría", "La forma de decirlo también afecta lo que se entiende."),
        ("ab", "{F} ¿Qué registro usa B?", "Formal, con un saludo cuidado", "Muy informal", "«Buenas tardes» y «proponer» son propios de una reunión con vecinos."),
        ("abc", "{F} ¿Cuál es el orden de las ideas en B?", "Saludo, propuesta, datos y petición", "Petición, saludo, datos", "Datos, despedida, saludo", "Así avanzan las frases en el guion."),
        ("abc", "{F} ¿Qué mejoraría la intervención B?", "Decir cuándo se pedirá la ayuda", "Hablar más fuerte siempre", "Agregar un chiste", "Un plazo concreto la haría más útil."),
        ("ab", "Ana dice que hablar bien es hablar mucho. Luis dice que es hablar claro y ordenado. ¿Quién tiene razón?", "Luis", "Ana", "La claridad y el orden importan más que la cantidad."),
    ],
    ctx=("abc", "En una reunión de una organización, una persona debe avisar que el horario cambiará. ¿Qué es lo más claro?", "Decir qué cambia, desde cuándo y a quién consultar, en pocas frases ordenadas", "Hablar sin orden para no apurarse", "Leer todo muy rápido", "Una presentación clara informa lo esencial en orden."),
    sc=[("En Lenguaje: ¿qué es la audiencia?", "Las personas que escuchan", "El mensaje se adapta a las personas que escuchan y a lo que necesitan saber."),
        ("En Lenguaje oral: ¿qué es una muletilla al hablar?", "Una palabra o sonido que se repite sin aportar", "Un ejemplo común es decir «eh» entre frases."),
        ("¿Qué partes tiene una presentación?", "Inicio, desarrollo y cierre", "Inicio, desarrollo y cierre dan orden al mensaje y ayudan a seguirlo.")],
    op=("Imagina que quieres pedir, en una reunión de vecinos, que se pode un árbol que tapa una luminaria. Escribe, con tus palabras, un saludo, la propuesta, dos datos concretos (inventados) y una petición. Léelo en voz alta con tono firme, volumen medio y mirando al frente.",
        "Buenas tardes. Quiero proponer que se pode el árbol de la esquina. Tapa la luminaria y la calle queda oscura de noche. Pido que lo solicitemos a la municipalidad.",
        ["tiene saludo, propuesta, datos y petición", "usa frases cortas y sin muletillas", "se puede leer con voz clara"],
        ["un guion escrito de cuatro a cinco frases"],
        ["escribir frases vagas sin datos", "no incluir una petición"],
        "Pregunta: «¿Qué quieres que haga quien te escucha?»."),
    reinforce="Elige un tema que conozcas y cuéntalo en tres frases ordenadas ante una persona de confianza.",
    extend="Explica por qué la misma propuesta puede sonar distinta con la voz firme o con la voz baja.",
)

# ============================================================ clase 2
build(
    O, 2, P2,
    use="Hoy aprendo las palabras clave de una presentación: audiencia, registro, vocabulario preciso, información fidedigna y progresión.",
    prior=["Sé que una presentación tiene inicio, desarrollo y cierre.", "Conozco sinónimos y antónimos.", "Distingo registro formal e informal."],
    explain=[
        "El vocabulario preciso usa la palabra exacta en vez de palabras vagas como «cosa» o «eso». Decir «el semáforo no funciona» informa más que «la cosa no funciona». El vocabulario variado evita repetir siempre la misma palabra: puedes usar sinónimos como «arreglar» y «reparar».",
        "La información fidedigna es la que viene de una fuente confiable y se puede comprobar. La progresión temática es el avance ordenado de las ideas: cada idea se apoya en la anterior y todas apuntan al tema.",
        "Además, elige el registro según tu audiencia. Con personas que no conoces o en una reunión, se usa un registro formal: «Buenas tardes, les informo…». Con amistades, uno informal: «Hola, les cuento…». La voz suma: el tono dice cómo te sientes, el volumen te hace oír y el ritmo permite seguirte.",
    ],
    vocab=[("vocabulario preciso", "la palabra exacta para cada idea"), ("vocabulario variado", "uso de distintas palabras para no repetir"), ("información fidedigna", "información confiable que se puede comprobar"), ("progresión temática", "avance ordenado de las ideas hacia el tema"), ("registro", "modo de hablar según la situación"), ("riesgo", "posibilidad de que ocurra un daño")],
    worked=[
        ("Hacer preciso un texto", "Texto impreciso: «Hay un problema con ese aparato del pasillo. No sirve y hay que cambiarlo. Es muy feo para todos». Versión precisa: «El ascensor del edificio no funciona y algunas personas no pueden subir. Pedimos a la administración que lo repare».", ["«Ese aparato» es vago: se reemplaza por «el ascensor del edificio».", "«Hay que cambiarlo» se reemplaza por «Pedimos que lo repare».", "«Muy feo para todos» se precisa: «algunas personas no pueden subir»."], "La versión precisa informa mejor y se entiende sin adivinar"),
        ("Registro", "Dos inicios de ejemplo: «Buenas tardes, les informo que mañana habrá reunión» y «Amigos, mañana nos juntamos, ¿ya?».", ["El primero es cuidado y respetuoso: formal.", "El segundo es cercano y coloquial: informal."], "El primero es formal; el segundo, informal"),
    ],
    mistakes=[("Usar «cosa», «eso» o «esto» para todo.", "La audiencia no sabe a qué te refieres.", "Nombra con la palabra exacta lo que quieres decir."),
              ("Repetir una misma palabra muchas veces.", "Cansa a la audiencia y empobrece el mensaje.", "Usa sinónimos que mantengan el sentido.")],
    T=[
        ("abc", "{F} ¿Qué palabra vaga se repite en la versión imprecisa?", "cosa", "semáforo", "esquina", "«La cosa» aparece dos veces sin decir qué es."),
        ("ab", "{F} ¿Qué dice con precisión la versión precisa?", "Que el semáforo de la esquina no funciona", "Que hay un problema", "Nombra el objeto exacto: el semáforo."),
        ("abc", "{F} ¿Qué información nueva aporta «los peatones cruzan con riesgo»?", "Las personas afectadas y el peligro", "El color del semáforo", "La hora del día", "Explica por qué importa el problema."),
        ("abc", "Un sinónimo de «reparar» es:", "arreglar", "romper", "ensuciar", "Reparar y arreglar significan casi lo mismo."),
        ("ab", "¿Qué es información fidedigna?", "La que viene de una fuente confiable y se puede comprobar", "La que se escucha a lo lejos", "Fidedigna significa digna de fe, es decir, confiable."),
        ("abc", "Un antónimo de «riesgo» es:", "seguridad", "peligro", "problema", "Riesgo es posibilidad de daño; seguridad es lo contrario."),
        ("ab", "¿Qué saludo corresponde a una reunión con personas que no conoces?", "Buenas tardes, les informo…", "Hola, qué tal po…", "Ese saludo es cuidado y respetuoso, propio de una reunión con personas desconocidas."),
        ("abc", "¿Qué es la progresión temática?", "El avance ordenado de las ideas hacia el tema", "La rapidez al hablar", "El volumen de la voz", "Cada idea se apoya en la anterior."),
        ("abc", "Un orador dice «tema, ejemplo, tema, otro ejemplo, de nuevo el tema». ¿Qué le falta?", "Una progresión clara: orden de inicio, desarrollo y cierre", "Más volumen", "Más muletillas", "Las ideas van y vienen sin avanzar."),
        ("ab", "Una persona dice «hay un problema con eso» sin aclarar a qué se refiere. ¿Qué conviene?", "Reemplazar «eso» por la palabra exacta", "Repetirlo más fuerte", "Nombrar con una palabra exacta lo que se quiere decir evita confusiones."),
        ("abc", "{F} ¿Qué cambio de palabra mejora más la frase «Hay que arreglar eso»?", "«Hay que reparar el semáforo»", "«Hay que arreglar cosas»", "«Hay que arreglar eso ya»", "Nombra el objeto y usa una acción precisa."),
        ("ab", "¿Cuál es el registro de «Les cuento una cosa, ¿ya?»?", "Informal", "Formal", "Es un modo cercano y coloquial."),
        ("abc", "Una persona habla con tono triste, volumen muy bajo y ritmo lento sobre una buena noticia. ¿Qué ocurre?", "El mensaje y la forma de decirlo no coinciden", "Todo coincide", "Se entiende mejor", "El tono debe acompañar el contenido."),
    ],
    ctx=("abc", "Alguien va a pedir en la municipalidad el arreglo de una calle. ¿Qué frase es más precisa?", "«La calle Los Olmos tiene un hoyo grande frente al número 120»", "«Hay un problema por ahí»", "«Hay cosas rotas»", "Indica la calle y el problema exacto (de ejemplo)."),
    sc=[("En Lenguaje: ¿qué es el vocabulario preciso?", "La palabra exacta para cada idea", "El vocabulario preciso evita las palabras vagas como «cosa» o «eso»."),
        ("¿Qué es información fidedigna?", "La que viene de una fuente confiable y se puede comprobar", "Se puede comprobar y merece confianza."),
        ("En una presentación: ¿para qué sirve elegir el registro?", "Para adecuar el modo de hablar a la audiencia", "Cambia según con quién se habla.")],
    op=("Reescribe con vocabulario preciso este texto de ejemplo: «Hay un problema con la cosa del pasaje. Esa cosa se rompió y es muy peligroso para la gente. Hay que hacer algo con eso.» Elige tú qué es la «cosa» (por ejemplo, una luminaria o una reja) y escribe tres frases. Usa un sinónimo para no repetir una palabra.",
        "La luminaria del pasaje se quemó y los vecinos caminan a oscuras. Es peligroso para quienes llegan de noche. Pedimos que la municipalidad la reemplace.",
        ["reemplaza «cosa» y «eso» por palabras exactas", "agrega quién se afecta", "usa un sinónimo"],
        ["tres frases reescritas"],
        ["cambiar solo una palabra", "repetir la misma palabra"],
        "Pregunta: «¿Alguien que no conoce el pasaje entendería qué ocurre?»."),
    reinforce="Anota tres palabras vagas que uses a veces y escribe su versión precisa.",
    extend="Escribe dos saludos de inicio: uno formal y otro informal, para invitar a una reunión.",
)

# ============================================================ clase 3
build(
    O, 3, P3,
    use="Hoy sigo cinco pasos para preparar una presentación: propósito, fuentes confiables, esquema, guion y ensayo.",
    prior=["Sé qué es una fuente confiable.", "Sé hacer un esquema o mapa.", "Conozco las partes de una presentación."],
    explain=[
        "Preparar una presentación se hace en cinco pasos. Paso 1: define el propósito (qué quiero lograr) y la audiencia. Paso 2: busca información en fuentes confiables y anota de dónde sale. Paso 3: sintetiza las ideas en un esquema corto, por ejemplo un mapa. Paso 4: escribe un guion con palabras clave. Paso 5: ensaya en voz alta.",
        "Una fuente confiable dice quién la publica, cuándo y con qué respaldo. Una publicación sin autor ni fecha, o que solo dice «dicen que…», no sirve para sostener un dato. Cuando uses una fuente, menciónala: «según el boletín de ejemplo de 2024…».",
        "Escribe el guion con palabras clave, no con todas las frases, para no leer de corrido. Revisa la ortografía: «presentación» lleva tilde por ser aguda terminada en n; «después» también. Y cuida los verbos: «voy a hablar», «hablé», «hablaré».",
    ],
    vocab=[("propósito", "lo que quiero lograr al hablar"), ("esquema", "resumen ordenado de las ideas"), ("palabra clave", "palabra que recuerda una idea"), ("ensayar", "practicar antes de presentar"), ("citar", "decir de dónde sale un dato")],
    worked=[
        ("Elegir fuentes", "Fuente A (guía de ejemplo de una municipalidad de ejemplo, 2024): «Los envases se depositan limpios en el contenedor.» Fuente B (publicación sin autor ni fecha): «Dicen que da lo mismo cómo se tiren».", ["La Fuente A dice quién la publica y el año: es confiable.", "La Fuente B no tiene autor ni fecha y dice «dicen que»: no sirve.", "Uso solo la Fuente A para el dato."], "Se usa la Fuente A y se descarta la Fuente B"),
        ("Esquema con palabras clave", "Esquema de ejemplo: inicio: saludo y tema; desarrollo: problema (basura en el suelo), causa (pocos basureros), solución (más basureros); cierre: invitación a cuidar la plaza.", ["Cada parte tiene palabras clave.", "El orden va del problema a la solución."], "El esquema ordena la presentación en tres partes"),
    ],
    mistakes=[("Escribir todo el discurso y leerlo de corrido.", "Se pierde contacto con la audiencia y suena monótono.", "Usa palabras clave y mira a las personas."),
              ("Usar un dato sin saber de dónde sale.", "No se puede comprobar ni citar.", "Anota la fuente cuando tomes el dato.")],
    T=[
        ("abc", "{F} ¿Cuál es el tema de la presentación prevista?", "El ahorro de agua en casa", "El valor de la leche", "Una receta de cocina", "El título y el dato hablan de ahorrar agua."),
        ("ab", "{F} ¿Qué fuente conviene usar?", "La Fuente 1", "La Fuente 2", "La Fuente 1 indica institución y año; la Fuente 2 no tiene autor ni fecha."),
        ("{F} ¿Qué frase de la Fuente 2 muestra poca confiabilidad? Responde con dos palabras.", "dicen que", "La frase «dicen que» no nombra quién lo dice, así que no se puede comprobar."),
        ("abc", "¿Qué se hace en el paso 1?", "Definir el propósito y la audiencia", "Ensayar en voz alta", "Escribir todo el discurso", "Se parte por saber para qué y para quién se habla."),
        ("ab", "¿Qué se hace en el paso 5?", "Ensayar en voz alta", "Buscar fuentes", "Después de escribir el guion se practica leyéndolo en voz alta."),
        ("abc", "{F} En el esquema, ¿qué partes tiene el desarrollo?", "Problema, causa y solución", "Saludo, tema y cierre", "Fuente 1, fuente 2 y blog", "Así lo indica el esquema previsto."),
        ("ab", "¿Cómo se menciona bien la Fuente 1?", "«Según el boletín de ejemplo de 2024…»", "«Dicen que…»", "La mención dice quién y cuándo."),
        ("abc", "¿Qué conviene llevar escrito para hablar?", "Palabras clave", "Todo el discurso", "Nada", "Las palabras clave recuerdan las ideas sin leer de corrido."),
        ("abc", "¿Cuál palabra lleva tilde?", "presentación", "presentacion", "presentasión", "Es aguda y termina en n; además se escribe con c."),
        ("ab", "Completa con el futuro de «hablar» (yo): «Mañana _____ del ahorro de agua».", "hablaré", "hablé", "«Hablaré» está en futuro e indica algo que ocurrirá mañana."),
        ("abc", "{F} Una persona agrega «Todos los vecinos desperdician agua» sin fuente. ¿Qué conviene?", "Quitarlo o respaldarlo con una fuente confiable", "Dejarlo porque suena bien", "Decirlo más fuerte", "Un dato sin respaldo puede ser falso."),
        ("abc", "{F} ¿Qué orden de pasos es el correcto?", "Propósito, fuentes, esquema, guion, ensayo", "Ensayo, guion, fuentes, propósito", "Guion, ensayo, propósito, fuentes", "Primero se planifica y se reúne la información, y al final se practica."),
        ("ab", "¿Por qué conviene ensayar en voz alta?", "Porque se descubren tropiezos de ritmo y de palabras", "Porque no hace falta preparar nada", "Hablar en voz alta revela lo que no se nota al leer en silencio."),
    ],
    ctx=("abc", "Una persona prepara una presentación de ejemplo sobre seguridad en la calle para su organización. Encuentra un folleto de una institución de ejemplo (2024) y un mensaje reenviado sin autor. ¿Qué hace?", "Usa el folleto, lo cita y descarta el mensaje sin autor", "Usa solo el mensaje", "Usa ambos sin citar", "El folleto indica quién y cuándo; el mensaje no se puede comprobar."),
    sc=[("En un guion oral: ¿qué es una palabra clave?", "Una palabra que recuerda una idea", "Sirve para no leer de corrido."),
        ("En Lenguaje: ¿qué es ensayar?", "Practicar antes de presentar", "Ensayar permite corregir el ritmo y las palabras que cuestan antes de presentar."),
        ("En una presentación: ¿qué datos lleva la cita de una fuente?", "Quién, título o tipo y año", "Con esos datos otra persona puede comprobar el dato en la fuente.")],
    op=("Prepara una presentación de ejemplo sobre «cómo evitar accidentes en casa» (por ejemplo, objetos en el suelo). Escribe: tu propósito, un esquema de tres partes con palabras clave y una cita de ejemplo inventada (institución, título y año). No hace falta que los datos sean reales: márcalos como de ejemplo.",
        "Propósito: avisar cómo evitar caídas. Inicio: saludo y tema. Desarrollo: objetos en el suelo, luz, pasillos libres. Cierre: invitar a revisar. Cita: Organización de ejemplo, «Hogar seguro», 2024.",
        ["define propósito y audiencia", "esquema con inicio, desarrollo y cierre", "incluye una fuente citada"],
        ["un propósito, un esquema y una cita escritos"],
        ["escribir todo el discurso", "no citar la fuente"],
        "Pregunta: «¿Qué idea es la central de tu presentación?»."),
    reinforce="Haz el esquema de una presentación breve sobre un tema que conozcas bien.",
    extend="Escribe tres preguntas que harías para saber si una fuente es confiable.",
)

# ============================================================ clase 4
build(
    O, 4, P4,
    use="Hoy practico con apoyo: marco pausas, calculo el tiempo de una presentación y corrijo un guion.",
    prior=["Sé armar un esquema y un guion con palabras clave.", "Distingo tono, volumen, ritmo y gestos.", "Sé multiplicar y dividir cantidades pequeñas."],
    explain=[
        "Practicar con apoyo significa ensayar con marcas y con pistas. En un guion se pueden marcar las pausas: una barra / para una pausa corta y dos barras // para una pausa larga. Las pausas dan tiempo para respirar y para que la audiencia entienda.",
        "El ritmo es la rapidez al hablar. Una forma de calcular cuánto dura una presentación es dividir el total de palabras por las palabras por minuto. Si un texto tiene 180 palabras y lo lees a 90 palabras por minuto, dura 2 minutos. Son cifras de ejemplo: cada persona tiene su ritmo.",
        "Para ensayar, léelo en voz alta, anota dónde tropiezas, y repite. También ayuda decir las ideas con otras palabras, sin leer. La inflexión, el cambio de voz hacia arriba o abajo, marca preguntas y énfasis: una pregunta sube al final.",
    ],
    vocab=[("pausa", "pequeño silencio al hablar"), ("énfasis", "fuerza especial en una palabra importante"), ("inflexión", "subida o bajada de la voz"), ("ritmo", "rapidez al hablar")],
    worked=[
        ("Marcar pausas", "Guion de ejemplo: «Hola a todos. Hoy les presento el horario de la sede. Abrimos de lunes a viernes. Gracias».", ["Marco una pausa corta tras «Hola a todos» y tras «sede».", "Marco una pausa larga al terminar cada idea completa.", "Respiro en las pausas largas."], "Hola a todos, / hoy les presento el horario de la sede. // Abrimos de lunes a viernes. // Gracias."),
        ("Calcular el tiempo", "Un guion de ejemplo tiene 300 palabras y se lee a 150 palabras por minuto.", ["Divido 300 por 150.", "El resultado es 2.", "Dura 2 minutos."], "Dura 2 minutos"),
    ],
    mistakes=[("Hablar sin pausas para «terminar rápido».", "La audiencia no alcanza a entender.", "Marca pausas y respétalas."),
              ("Dar por seguro el tiempo sin ensayar.", "Cada persona habla a un ritmo distinto.", "Mide el tiempo ensayando en voz alta.")],
    T=[
        ("abc", "{F} ¿Qué significa «/» en el guion?", "Pausa corta", "Pausa larga", "Subir el volumen", "El guion lo indica: / = pausa corta."),
        ("ab", "{F} ¿Qué significa «//» en el guion?", "Pausa larga", "Pausa corta", "Doble barra equivale a una pausa mayor."),
        ("{F} ¿Con qué frase empieza el guion de ejemplo? Responde con las dos primeras palabras.", "Buenas tardes", "El guion empieza con el saludo «Buenas tardes», que abre la presentación."),
        ("abc", "{F} ¿Qué dato de la Fuente da el guion sobre las llaves?", "Una llave que gotea desperdicia agua todos los días", "Las llaves son de metal", "Las llaves cuestan caro", "Es la idea central del guion."),
        ("=", "{F} Un guion de 240 palabras se lee a 120 palabras por minuto. ¿Cuántos minutos dura?", "240//120", "Se divide el total de palabras por las palabras de cada minuto.", "minutos"),
        ("=", "{F} Si una persona lee 120 palabras por minuto durante 3 minutos, ¿cuántas palabras lee?", "120*3", "Se multiplican las palabras de un minuto por los minutos.", "palabras"),
        ("ab", "¿Para qué sirven las pausas?", "Para respirar y que la audiencia entienda", "Para gastar tiempo", "Permiten procesar lo que se dijo."),
        ("abc", "En una pregunta, ¿cómo suele moverse la voz al final?", "Sube", "Baja", "Se mantiene igual", "Esa subida de la voz al final de una pregunta se llama inflexión."),
        ("ab", "Una persona lee 360 palabras en 2 minutos. ¿Es más rápida o más lenta que 120 palabras por minuto?", "Más rápida", "Más lenta", "Lee 180 por minuto, más de 120."),
        ("abc", "Un compañero termina en 1 minuto lo que debía durar 3. ¿Qué conviene?", "Hablar más despacio, con pausas y más desarrollo", "Hablar aún más rápido", "No volver a ensayar", "Ensayar ayuda a ajustar el ritmo."),
        ("ab", "¿Cuál palabra lleva tilde?", "después", "ensayo", "Después es aguda y termina en s; ensayo es grave y termina en vocal."),
        ("abc", "{F} Para destacar la palabra «todos» en «desperdicia agua todos los días», ¿qué conviene?", "Darle más fuerza a esa palabra", "Susurrarla", "Saltarla", "Dar más fuerza a una palabra es el énfasis y marca lo importante."),
        ("abc", "{F} ¿Cuál es una pausa mejor ubicada?", "«Una llave que gotea / desperdicia agua»", "«Una llave / que gotea desperdicia / agua»", "«Una / llave que gotea desperdicia agua»", "La pausa debe separar partes con sentido, no cortar una idea al medio."),
    ],
    ctx=("abc", "Una persona debe hablar 2 minutos en una reunión y su guion tiene 360 palabras. Ensayando, lee 120 palabras por minuto (cifra de ejemplo). ¿Qué ocurre?", "Se pasará: 360 palabras duran 3 minutos, así que debe acortar el guion", "Le sobrará tiempo", "Le calzará justo", "Se calcula 360 ÷ 120 = 3 minutos; son más de los 2 que tiene."),
    sc=[("¿Qué marca «//» en un guion?", "Una pausa larga", "Separa una idea completa de la siguiente."),
        ("En Lenguaje: ¿qué es la inflexión?", "La subida o bajada de la voz", "La inflexión marca las preguntas y da énfasis a lo importante."),
        ("¿Cómo se calcula la duración de un texto?", "Dividiendo las palabras entre las palabras por minuto", "Con datos de ritmo de ejemplo.")],
    op=("Toma este guion de ejemplo: «Buenas tardes. Hoy hablaré de cómo ordenar los documentos. Primero, separen los papeles importantes. Segundo, guárdenlos en una carpeta. Tercero, anoten dónde la dejaron. Gracias». Cópialo y marca pausas cortas (/) y largas (//), subraya dos palabras con énfasis y ensáyalo en voz alta una vez.",
        "Buenas tardes. // Hoy hablaré de cómo ordenar los documentos. // Primero, / separen los papeles IMPORTANTES. // Segundo, / guárdenlos en una carpeta. // Tercero, / anoten dónde la dejaron. // Gracias.",
        ["marca pausas con sentido", "elige dos palabras para enfatizar", "ensaya en voz alta"],
        ["un guion marcado en el cuaderno"],
        ["poner pausas en medio de una idea", "no ensayar en voz alta"],
        "Pregunta: «¿La pausa corta una idea o la separa bien?»."),
    reinforce="Cronometra una lectura en voz alta de un párrafo y calcula tu ritmo en palabras por minuto.",
    extend="Explica cómo ajustarías un guion de 5 minutos para que dure 3.",
)

# ============================================================ clase 5
build(
    O, 5, P5,
    use="Hoy aplico lo aprendido: reviso y mejoro una presentación de un minuto para una reunión de vecinos.",
    prior=["Sé preparar un esquema y un guion.", "Sé marcar pausas y énfasis.", "Sé citar una fuente."],
    explain=[
        "Aplicar significa llevar la preparación a una situación real: una reunión de vecinos, una charla en el lugar de trabajo o una presentación en un grupo de estudio. Allí cuentan el contenido, el orden y la voz.",
        "Al revisar un guion pregúntate: ¿el inicio presenta el tema?, ¿el desarrollo avanza en orden?, ¿el cierre resume o invita a actuar?, ¿hay una fuente?, ¿las palabras son precisas? También verifica el tiempo: las partes deben sumar lo que dura la presentación.",
        "Si la audiencia hace preguntas, escucha completa la pregunta, responde con calma y si no sabes, dilo: «No lo sé; lo reviso y les respondo». Eso da confianza. Cuida el registro formal y no uses muletillas.",
    ],
    vocab=[("pregunta de la audiencia", "duda que plantea quien escucha"), ("desarrollo", "parte central, donde se explican las ideas"), ("cierre", "parte final que resume o invita a actuar"), ("orden", "secuencia lógica de las ideas")],
    worked=[
        ("Revisar el guion", "Guion de ejemplo: «Buenas tardes. Voy a hablar de cuidar los basureros de la plaza. Primero, los usamos. Segundo, los mantenemos cerrados. Tercero, avisamos si están rotos. Si todos cuidamos, la plaza se ve mejor. Gracias». Fuente de ejemplo: folleto de un municipio de ejemplo, 2024.", ["Inicio: saluda y dice el tema.", "Desarrollo: tres pasos ordenados con «primero», «segundo» y «tercero».", "Cierre: resume y agradece.", "Fuente: folleto de ejemplo de un municipio, 2024."], "El guion tiene orden, datos y fuente"),
        ("Responder una pregunta", "Una persona pregunta: «¿Qué pasa con las pilas usadas?» y el orador no tiene el dato.", ["Reconoce que no lo sabe.", "Ofrece averiguarlo.", "No inventa una respuesta."], "«No lo sé; lo reviso y les respondo»: es honesto y confiable"),
    ],
    mistakes=[("Inventar una respuesta para no quedar mal.", "Puede entregar información falsa.", "Di que lo averiguarás y cumple."),
              ("Pasarse del tiempo por querer decirlo todo.", "La audiencia pierde el hilo.", "Elige lo esencial y ensaya con reloj.")],
    T=[
        ("abc", "{F} ¿Cuál es el tema de la presentación?", "Cómo separar la basura en el pasaje", "Cómo cocinar", "Cómo pedir una hora médica", "El inicio del guion dice el tema: cómo separar la basura en el pasaje."),
        ("ab", "{F} ¿Qué palabras ordenan el desarrollo?", "Primero, segundo y tercero", "Además, tampoco y nunca", "«Primero, segundo y tercero» muestran la secuencia de pasos del desarrollo."),
        ("{F} ¿De qué color es el contenedor mencionado? Responde con una palabra.", "azul", "El segundo paso del desarrollo nombra el contenedor azul."),
        ("abc", "{F} ¿Qué se hace con la basura orgánica?", "Dejarla en una bolsa aparte", "Llevarla al contenedor azul", "Quemarla", "El tercer paso dice que la basura orgánica va en una bolsa aparte."),
        ("ab", "{F} ¿Qué hace el cierre?", "Resume y agradece", "Presenta el tema", "El cierre del guion resume la idea y agradece a quienes escucharon."),
        ("=", "{F} Si el inicio dura 10 segundos, el desarrollo 35 y el cierre 15, ¿cuántos segundos dura toda la presentación?", "10+35+15", "Se suman los tres tiempos.", "segundos"),
        ("abc", "{F} ¿Cuántos minutos son esos 60 segundos? Responde con un número.", "1", "2", "10", "Un minuto tiene 60 segundos, así que 60 segundos son 1 minuto."),
        ("ab", "Una persona pregunta algo que el orador no sabe. ¿Qué respuesta es mejor?", "«No lo sé; lo reviso y les respondo»", "Inventar un dato", "Reconocer los límites es honesto y da confianza."),
        ("abc", "{F} ¿Qué registro usa el guion?", "Formal y cercano", "Muy informal", "Con groserías", "Saluda con respeto y usa frases claras."),
        ("abc", "{F} ¿Qué mejoraría el guion?", "Decir cuántos contenedores hay y dónde están (con datos de ejemplo)", "Hablar más rápido", "Quitar el cierre", "Un dato concreto lo hace más útil."),
        ("ab", "¿Cuál es el verbo correcto? «Mañana yo _____ la presentación».", "ensayaré", "ensayé", "«Ensayaré» está en futuro y expresa algo que se hará mañana."),
        ("abc", "{F} ¿Cuál es un cierre que invita a actuar?", "«Si todos separamos, el pasaje se mantiene limpio»", "«Eso era todo»", "«No sé qué más decir»", "Invita a un comportamiento con un resultado."),
        ("ab", "¿Cuál palabra está bien escrita?", "separación", "separacion", "Es aguda, termina en n y se escribe con c: separación."),
    ],
    ctx=("abc", "En una reunión de un grupo de estudio, alguien debe explicar en un minuto cómo está organizado el curso. ¿Cuál es el mejor plan?", "Saludar, explicar tres puntos ordenados y cerrar con una invitación", "Leer todo el programa", "Hablar sin orden", "Un minuto exige un esquema corto y claro."),
    sc=[("¿Qué debe hacer el desarrollo?", "Explicar las ideas en orden", "El desarrollo es la parte central, donde se explican las ideas en orden."),
        ("En Lenguaje: ¿qué hago si no sé una respuesta?", "Lo reconozco y ofrezco averiguarlo", "Reconocer lo que no se sabe es honesto y da confianza a quien pregunta."),
        ("En una presentación de un minuto: ¿cuántos segundos dura?", "60", "Un minuto equivale a 60 segundos, que es la medida con que se reparte el tiempo.")],
    op=("Escribe un guion de una presentación de un minuto para una reunión de vecinos sobre «cuidar la plaza» (con datos inventados rotulados como de ejemplo). Debe tener inicio, desarrollo con tres pasos, cierre y una fuente de ejemplo. Anota cuánto dura cada parte (suma 60 segundos). Ensáyalo en voz alta.",
        "Inicio (10 s): saludo y tema. Desarrollo (35 s): tres pasos. Cierre (15 s): resumen y gracias. Fuente: guía de ejemplo, 2024.",
        ["tiene inicio, desarrollo con tres pasos y cierre", "los tiempos suman 60 segundos", "incluye una fuente de ejemplo"],
        ["un guion y una tabla de tiempos"],
        ["pasarse de tiempo", "no ordenar los pasos"],
        "Pregunta: «¿Qué quitarías si te falta tiempo?»."),
    reinforce="Ensaya tu guion ante una persona de confianza y pídele que anote una cosa clara y una por mejorar.",
    extend="Escribe dos posibles preguntas de la audiencia y cómo las responderías.",
)

# ============================================================ clase 6
build(
    O, 6, P6,
    use="Hoy reviso lo logrado con una rúbrica y decido qué quiero seguir practicando.",
    prior=["Sé preparar y ensayar una presentación.", "Sé citar una fuente.", "Sé sumar cantidades pequeñas."],
    explain=[
        "Para cerrar, revisamos lo aprendido con una rúbrica, que es una lista de criterios con puntajes. Sirve para ver qué hiciste bien y qué puedes mejorar. Una rúbrica no mide a la persona: mide la presentación.",
        "Una buena presentación tiene un inicio que presenta el tema, ideas ordenadas, información confiable con fuente, voz y gestos adecuados y un cierre. Estos criterios reúnen lo trabajado: propósito, progresión temática, vocabulario preciso, registro y recursos de la voz.",
        "Después de evaluarte, elige uno o dos puntos para seguir practicando. Puedes pedir la opinión de otra persona de confianza: una coevaluación, es decir, una evaluación hecha entre dos. Anota lo que te sirvió y lo que cambiarías la próxima vez.",
    ],
    vocab=[("rúbrica", "lista de criterios con puntajes"), ("coevaluación", "evaluación hecha entre dos personas"), ("autoevaluación", "evaluación que uno hace de su propio trabajo"), ("criterio", "aspecto que se mira para juzgar")],
    worked=[
        ("Sumar la rúbrica", "Con la misma rúbrica, otra presentación de ejemplo: inicio 1, ideas ordenadas 1, fuente 2, voz y gestos 2, cierre 0.", ["Los puntajes son 1, 1, 2, 2 y 0.", "Se suman: 1 + 1 + 2 + 2 + 0 = 6.", "El máximo es 5 criterios por 2 puntos, es decir, 10."], "6 de 10 puntos"),
        ("Elegir qué mejorar", "Con esa otra presentación: los criterios con menos puntos son el cierre (0), el inicio (1) y las ideas ordenadas (1).", ["Los puntajes más bajos muestran dónde mejorar.", "Elijo practicar primero el cierre y el inicio."], "Mejorar el cierre y el inicio"),
    ],
    mistakes=[("Poner el máximo en todo para quedar bien.", "No ayuda a mejorar.", "Evalúa con honestidad y pide la mirada de otra persona."),
              ("Tomar un puntaje bajo como una falla personal.", "La rúbrica evalúa la presentación, no a ti.", "Úsala como guía para practicar.")],
    T=[
        ("=", "{F} ¿Cuántos puntos suma la presentación de ejemplo?", "2+2+1+1+2", "Se suman los cinco criterios.", "puntos"),
        ("=", "{F} ¿Cuál es el puntaje máximo posible?", "5*2", "Son cinco criterios de hasta 2 puntos.", "puntos"),
        ("ab", "{F} ¿En qué dos criterios obtuvo 1 punto?", "Fuente y voz y gestos", "Inicio y cierre", "Los criterios con 1 punto son fuente y voz y gestos; inicio y cierre tienen 2."),
        ("abc", "{F} ¿Qué criterio obtuvo el máximo y trata del orden?", "Ideas ordenadas", "Fuente", "Voz y gestos", "Obtuvo 2 puntos el criterio de ideas ordenadas."),
        ("ab", "{F} ¿Qué puntaje significa que el criterio se cumple bien?", "2", "0", "Según la rúbrica, 2 es cumple bien."),
        ("=", "{F} ¿Cuántos puntos le faltan para llegar al máximo?", "10-8", "Se resta lo obtenido del máximo.", "puntos"),
        ("abc", "¿Qué es una autoevaluación?", "La evaluación de mi propio trabajo", "La evaluación de otra persona", "Un examen sin criterios", "Es evaluarse a uno mismo con honestidad."),
        ("ab", "¿Qué es una coevaluación?", "Una evaluación hecha entre dos personas", "Una evaluación sin criterios", "En una coevaluación dos personas comparten opiniones usando criterios."),
        ("abc", "{F} ¿Cuál es una buena acción de mejora?", "Agregar y citar una fuente confiable y ensayar la voz", "Hablar más rápido", "Acortar el inicio a cero", "Apunta a los criterios con 1 punto."),
        ("ab", "Un compañero obtiene 10 de 10 y dice que ya no necesita practicar. ¿Qué es más razonable?", "Seguir practicando con nuevas situaciones", "No hacer nada", "La práctica ayuda a mantener y adaptar lo aprendido."),
        ("=", "{F} Si la presentación mejora «fuente» de 1 a 2 y «voz y gestos» de 1 a 2, ¿cuántos puntos tendría en total?", "8+1+1", "Cada mejora suma 1 punto a los 8 actuales.", "puntos"),
        ("ab", "¿Cuál palabra lleva tilde?", "rúbrica", "criterio", "Rúbrica es esdrújula; criterio es grave y termina en vocal."),
        ("abc", "Una persona escribe «Mejoré mi inicio, pero me falta citar fuentes». ¿Qué hace?", "Reconoce un logro y un punto por mejorar", "Se castiga", "Evita evaluar", "Una buena autoevaluación nombra un logro y también un punto por mejorar."),
    ],
    ctx=("abc", "Una persona terminó su presentación en el grupo de estudio y quiere mejorar. ¿Qué es lo más útil?", "Pedir a alguien de confianza que use la rúbrica y comparar con su propia nota", "No volver a presentar", "Decir que todo salió perfecto", "La coevaluación aporta otra mirada que ayuda a ver lo que uno no nota."),
    sc=[("En Lenguaje: ¿qué es una rúbrica?", "Una lista de criterios con puntajes", "Una rúbrica sirve para evaluar con orden, criterio por criterio."),
        ("¿Qué mide la rúbrica?", "La presentación, no a la persona", "La rúbrica evalúa la presentación y se usa para mejorarla, no para juzgar a la persona."),
        ("¿Qué hago después de evaluarme?", "Elijo uno o dos puntos para practicar", "Es un plan de mejora concreto.")],
    op=("Haz tu plan de mejora. Escribe tu autoevaluación con la rúbrica de la clase (0, 1 o 2 puntos por criterio) para una presentación que hayas ensayado, suma tu total y elige dos criterios para practicar esta semana. Si puedes, pide a otra persona de confianza que la evalúe y compara.",
        "Inicio 2, ideas 2, fuente 1, voz 1, cierre 2: 8 de 10. Practicar: fuente y voz y gestos.",
        ["asigna puntajes a los cinco criterios", "suma bien", "elige dos puntos y una acción para cada uno"],
        ["una rúbrica completada y un plan de dos líneas"],
        ["poner 2 en todo sin pensar", "no elegir qué practicar"],
        "Pregunta: «¿Qué harás primero para mejorar?»."),
    reinforce="Ensaya de nuevo tu presentación pensando solo en el criterio con menor puntaje.",
    extend="Escribe un criterio nuevo para la rúbrica y explica por qué lo agregas.",
)

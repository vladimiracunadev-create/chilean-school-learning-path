"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 20 (opinar y argumentar con fundamentos)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA20 = "HI05 OA 20"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA20, 1,
    materials="Este cuaderno y un lápiz. Los casos y los datos están escritos en los ejercicios.",
    use="Aprenderé a ubicar un tema en el tiempo y en el espacio antes de opinar sobre él. Sirve para que mis opiniones sean justas y no juzguen el pasado solo con las ideas o los objetos de hoy.",
    prior=["Sé distinguir un hecho de una opinión.", "Sé dar una razón con «porque».", "Sé leer una línea de tiempo y ubicar lugares con puntos cardinales."],
    explain=[
        "Antes de opinar con fundamentos conviene ubicar el tema. Me pregunto tres cosas: ¿cuándo ocurre?, ¿dónde ocurre? y ¿quiénes participan? Las respuestas forman el contexto, es decir, las circunstancias de tiempo, de lugar y de personas que rodean un hecho. Una opinión sin contexto puede equivocarse, porque habla de algo que no se ha entendido bien.",
        "El tiempo importa. Hace más de cien años no existían los celulares ni la televisión, y la gente se informaba y se comunicaba de otras maneras. Si digo «las personas de entonces fueron descuidadas por no mandar un mensaje de texto», cometo un anacronismo: juzgo el pasado con objetos o ideas que solo existen hoy. Para opinar sobre el pasado, primero pregunto cómo se vivía en esa época y qué posibilidades había.",
        "El espacio también importa. En el norte de Chile hay desierto y el agua es escasa; en el sur llueve mucho. Una opinión sobre el uso del agua cambia según el lugar. Por eso, al argumentar, digo de qué época y de qué territorio hablo. Así mis razones se pueden entender y comprobar, y no se aplican a todo sin distinguir.",
    ],
    vocab=[("contexto", "circunstancias de tiempo, lugar y personas que rodean un hecho"), ("anacronismo", "error de juzgar una época con cosas o ideas de otra"), ("territorio", "espacio con rasgos propios donde viven personas"), ("época", "período de la historia con rasgos propios"), ("fundamento", "razón o dato sobre el que se apoya una opinión")],
    worked=[
        W("Detectar un anacronismo", "Alguien opina: «Hace 120 años las familias eran poco previsoras, porque no revisaban el pronóstico del tiempo en el celular». ¿Qué error tiene?",
          ["Busco el objeto que hoy existe.", "El celular no existía hace 120 años.", "Se juzga el pasado con algo de hoy."], "Es un anacronismo: usa el celular para juzgar una época en que no existía"),
        W("Ubicar antes de opinar", "Tema: «Hay que ahorrar agua en la casa». Datos: vivienda en un pueblo del desierto del norte de Chile, en la actualidad. ¿Cuándo, dónde y quiénes?",
          ["Cuándo: en la actualidad.", "Dónde: un pueblo del desierto del norte de Chile.", "Quiénes: las familias que viven allí."], "Actualidad; desierto del norte; las familias del pueblo"),
    ],
    mistakes=[
        M("Opinar sobre el pasado sin preguntar cómo se vivía entonces.", "Se cae en el anacronismo y la opinión queda injusta.", "Pregunta qué existía, qué se sabía y qué se podía hacer en esa época."),
        M("Creer que una opinión sirve igual para todos los lugares.", "Los territorios tienen rasgos distintos, como clima o recursos.", "Di de qué lugar hablas antes de dar tus razones."),
    ],
    tiers=tiers(
        [ex("¿Qué tres preguntas ayudan a ubicar un tema antes de opinar?", "Cuándo, dónde y quiénes participan", "Forman el contexto del tema."),
         ex("«El año pasado, en la plaza de Valdivia, el club de vecinos plantó 20 árboles». ¿Qué dato de lugar entrega la frase?", "La plaza de Valdivia", "Responde a la pregunta dónde."),
         ex("En la misma frase del club de vecinos, ¿quiénes participaron?", "El club de vecinos", "Responde a la pregunta quiénes.")],
        [ex("¿Por qué una opinión sin contexto puede equivocarse?", "Porque habla de algo que no se ha entendido bien", "Sin tiempo, lugar y personas falta información."),
         ex("¿Qué es un anacronismo?", "Juzgar una época con objetos o ideas de otra", "Se mezclan tiempos distintos."),
         ex("¿Por qué conviene decir de qué lugar hablo cuando opino sobre el agua?", "Porque el norte tiene agua escasa y el sur recibe mucha lluvia", "El territorio cambia la situación.")],
        [ex("Elige el anacronismo: A) «En 1900 se viajaba en tren y en carreta.» B) «En 1900 la gente debió pedir el taxi con una aplicación del celular.»", "B", "En 1900 no existían las aplicaciones de celular."),
         ex("Una opinión dice: «Un pueblo pesquero de la costa debe cuidar el mar porque de él vive». ¿Qué parte nombra el tipo de lugar: «pueblo pesquero de la costa» o «de él vive»?", "Pueblo pesquero de la costa", "Nombra el territorio de la opinión."),
         ex("Ordena de más general a más preciso el lugar: A) Valparaíso, B) Chile, C) un cerro de Valparaíso.", "B, A, C", "Va del país a la ciudad y luego al cerro.")],
        [ex("Lucas dice: «Los niños de hace 150 años no tenían excusa para no ver videos educativos». ¿Qué le respondes?", "Hace 150 años no existían los videos, así que su juicio es injusto", "Ubicar la época evita el anacronismo."),
         ex("Sara afirma: «En todo Chile conviene regar el jardín cada día». ¿Qué falta para que su opinión sea justa?", "Decir el lugar, porque el clima cambia entre norte y sur", "El territorio afecta la razón.")],
        [ex("Quieres opinar sobre cómo se informaba la gente hace más de cien años, antes de la televisión. ¿Qué medio de esa época sirve como ejemplo: el periódico impreso o la cuenta de una red social?", "Periódico impreso", "Las cuentas de red social no existían entonces."),
         ex("Dos vecinos opinan sobre el agua: uno vive en un pueblo del desierto del norte y otro en una zona lluviosa del sur. ¿Por qué pueden pensar distinto con buenas razones?", "Porque sus territorios tienen distinta cantidad de agua", "El lugar cambia las razones.")],
    ),
    context=[ex("En la escuela alguien dice: «Esa plaza debería tener juegos». Tú preguntas cuándo, dónde y quiénes. ¿Qué buscas con esas preguntas?", "Ubicar el contexto del tema para opinar con fundamentos", "Conocer tiempo, lugar y personas aclara la opinión.")],
    selfcheck=[ex("En Historia: ¿qué es el contexto de un hecho?", "Las circunstancias de tiempo, lugar y personas que lo rodean", "Es la idea central de la clase."), ex("¿Qué error comete quien juzga el pasado con objetos de hoy?", "Un anacronismo", "Mezcla épocas distintas."), ex("¿Qué tres datos forman la ubicación de un tema?", "Cuándo, dónde y quiénes", "Son las preguntas de contexto.")],
    open_task=task("Elige un tema: A) la plaza de un barrio de Santiago hoy, B) cómo se informaba la gente hace más de cien años, C) el uso del agua en un pueblo del norte de Chile. Escribe cuándo, dónde y quiénes. Luego escribe tu opinión con una razón que use esa ubicación y una frase que muestre que evitaste un anacronismo.", "Tema C. Cuándo: hoy. Dónde: un pueblo del desierto. Quiénes: sus familias. Opino que deben ahorrar agua porque allí llueve muy poco. No uso ejemplos de lugares lluviosos.", ["cuándo, dónde y quiénes", "opinión con razón", "sin anacronismo"], ["tres datos de ubicación y una opinión con razón"], ["opinar sin decir de qué lugar hablas", "juzgar una época con objetos de hoy"], "Lee tu texto a una persona de tu casa y pídele que diga si falta algún dato de ubicación."),
    reinforce="Elige un hecho de tu barrio y di cuándo, dónde y quiénes participaron.",
    extend="Escribe un ejemplo propio de anacronismo y explica cómo corregirlo.",
)

register(
    OA20, 2,
    materials="Este cuaderno y un lápiz. Las fuentes breves están escritas en los ejercicios.",
    use="Aprenderé a preguntar de dónde viene una fuente antes de usarla para opinar. Sirve para elegir información confiable y no repetir lo primero que leo.",
    prior=["Sé ubicar un tema en el tiempo y el espacio.", "Sé que una razón fuerte se apoya en evidencia."],
    explain=[
        "Una fuente es cualquier cosa de donde saco información: un libro, una carta, una foto, un mapa o un sitio de internet. Una fuente primaria nace en el tiempo que estudio: una carta de esa época o una foto tomada entonces. Una fuente secundaria habla de ese tiempo después, como un libro de texto. Ambas sirven, pero se usan distinto.",
        "Para decidir si una fuente me sirve pregunto por su procedencia: ¿quién la hizo?, ¿cuándo?, ¿para qué? Una fuente hecha para vender algo puede mostrar solo lo bueno. Una fuente sin autor ni fecha es difícil de comprobar. Una fuente hecha por alguien que estuvo presente puede aportar detalles, pero también mostrar solo su mirada.",
        "Para argumentar, cito la fuente: digo quién es y qué dice. Por ejemplo: «Según el informe de la biblioteca municipal del año pasado, el 60 % de los libros se prestó a niños». Así otras personas pueden revisar mi dato. Si dos fuentes distintas dicen lo mismo, mi razón es más fuerte; si se contradicen, debo buscar una tercera y decir que hay dudas.",
    ],
    vocab=[("fuente", "origen de la información"), ("fuente primaria", "fuente creada en la época que se estudia"), ("fuente secundaria", "fuente que habla de una época después de que ocurrió"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("citar", "decir de qué fuente viene un dato")],
    worked=[
        W("Primaria o secundaria", "Una carta escrita por una niña en 1910 y un libro de texto de 2020 sobre ese año. ¿Cuál es fuente primaria?",
          ["Pregunto cuál nace en el tiempo estudiado.", "La carta se escribió en 1910.", "El libro habla de 1910 después."], "La carta de 1910"),
        W("Revisar la procedencia", "Un afiche sin autor ni fecha dice: «Este jugo es el mejor del mundo». ¿Es buena fuente para opinar sobre alimentación sana?",
          ["No dice quién lo hizo ni cuándo.", "Busca vender el jugo.", "No entrega datos que se comprueben."], "No, porque no tiene autor ni fecha y busca vender"),
    ],
    mistakes=[
        M("Creer cualquier dato porque aparece escrito.", "Escribir algo no lo hace verdadero.", "Pregunta quién lo hizo, cuándo y para qué."),
        M("Usar un dato sin decir de qué fuente salió.", "Nadie puede comprobarlo.", "Cita quién lo dice antes de usarlo."),
    ],
    tiers=tiers(
        [ex("¿Qué es una fuente de información?", "El origen de donde saco información", "Puede ser un libro, una foto o un mapa."),
         ex("Una foto tomada durante una fiesta de barrio en 1980, ¿es fuente primaria o secundaria para estudiar esa fiesta?", "Primaria", "Se creó en el tiempo estudiado."),
         ex("Un artículo de 2023 que cuenta cómo se vivía en 1900, ¿es fuente primaria o secundaria sobre 1900?", "Secundaria", "Habla de esa época después de que pasó.")],
        [ex("Nombra las tres preguntas de procedencia.", "Quién la hizo, cuándo y para qué", "Permiten juzgar si sirve."),
         ex("¿Por qué una fuente hecha para vender puede no ser buena para opinar?", "Porque puede mostrar solo lo bueno", "Su propósito la hace parcial."),
         ex("¿Por qué conviene citar la fuente de un dato?", "Para que otros puedan comprobarlo", "Citar da transparencia.")],
        [ex("Elige la fuente con mejor procedencia para hablar del uso de la biblioteca: A) un cartel sin firma que dice «Nadie lee» o B) el informe fechado de la biblioteca con los préstamos del mes.", "B", "Tiene autor, fecha y datos."),
         ex("Dos fuentes distintas, A y B, dicen que el parque tiene 40 árboles. ¿Esa razón queda más fuerte o más débil?", "Más fuerte", "Dos fuentes coinciden."),
         ex("Entre estas dos fuentes, 1) diario de una persona escrito en 1920, 2) libro actual que lo comenta. ¿Cuál es primaria?", "El diario de 1920", "Nació en la época estudiada.")],
        [ex("Un compañero dice: «Es cierto porque salió escrito en un papel pegado en la pared». ¿Qué le preguntas?", "Quién lo escribió, cuándo y para qué", "El papel no prueba nada por sí solo."),
         ex("Una fuente dice que se plantaron 50 árboles y otra dice 20. ¿Qué haces antes de opinar?", "Buscar una tercera fuente y decir que hay dudas", "Las fuentes se contradicen.")],
        [ex("Ordena las dos partes para que la frase empiece citando la fuente: A) el 60 % de los libros se prestó a niños, B) según el informe de la biblioteca del año pasado.", "B, A", "La fuente va primero y el dato después."),
         ex("Un testigo que estuvo presente cuenta un hecho. ¿Qué ventaja y qué límite tiene su relato?", "Aporta detalles, pero muestra solo su mirada", "Estar presente da datos y también un punto de vista.")],
    ),
    context=[ex("Para opinar sobre cuidar un humedal, encuentras un informe de una universidad con fecha y un mensaje anónimo en una red. ¿Cuál usas primero?", "El informe con fecha", "Tiene autor, fecha y propósito claros.")],
    selfcheck=[ex("En Historia: ¿qué es una fuente primaria?", "Una fuente creada en la época que se estudia", "Nace en ese tiempo."), ex("¿Qué es la procedencia de una fuente?", "Quién la hizo, cuándo y para qué", "Permite juzgar la fuente."), ex("¿Qué haces si dos fuentes se contradicen?", "Busco otra y digo que hay dudas", "Así no afirmo de más.")],
    open_task=task("Lee estas tres fuentes inventadas sobre una biblioteca de barrio. Fuente 1: informe fechado de la biblioteca, dice que el mes pasado se prestaron 300 libros. Fuente 2: cartel sin firma, dice que nadie va. Fuente 3: carta de una vecina, dice que ella va cada semana. Escribe cuál usarías para opinar sobre el uso de la biblioteca y por qué (procedencia), si esa fuente es primaria para estudiar el uso de la biblioteca de ese mes y qué opinión darías con una cita.", "Uso la fuente 1 porque tiene autor, fecha y datos. Es primaria para estudiar el uso de ese mes, porque la biblioteca la hizo en ese tiempo. Según el informe, se prestaron 300 libros el mes pasado, así que creo que la biblioteca se usa.", ["elige una fuente y explica su procedencia", "dice si es primaria", "cita quién dice qué", "opinión coherente con la fuente"], ["fuente elegida, cita y opinión"], ["usar un cartel sin firma como prueba", "no citar la fuente"], "Muestra tu texto a una persona de tu casa y pídele que encuentre la cita."),
    reinforce="Mira un objeto de tu casa con fecha y di si sería fuente primaria de su tiempo.",
    extend="Escribe dos preguntas de procedencia para una noticia que hayas escuchado.",
)

register(
    OA20, 3,
    materials="Este cuaderno y un lápiz. La situación de la comuna inventada está escrita en los ejercicios.",
    use="Aprenderé a relacionar causas, actores y consecuencias para opinar con fundamentos. Sirve para entender un problema completo y no culpar a una sola persona o razón.",
    prior=["Sé ubicar un tema y revisar la procedencia de una fuente.", "Sé que un hecho puede tener más de una causa."],
    explain=[
        "Cuando ocurre algo importante pregunto tres cosas: ¿por qué pasó?, ¿quiénes participaron? y ¿qué cambió después? Las causas son las razones que hicieron que algo ocurriera. Los actores son las personas o grupos que participan, como vecinos, autoridades o empresas. Las consecuencias son lo que sucede a raíz del hecho. Con estas tres ideas mi opinión se apoya en algo más que en una sola razón.",
        "Casi siempre hay varias causas y varias consecuencias, y algunas llegan a corto plazo y otras más tarde. Por ejemplo, en una comuna inventada llamada Valle Claro, un arroyo se llenó de basura. Causas: no había suficientes basureros y se botaba basura en la orilla. Actores: vecinos, el municipio y los dueños de negocios. Consecuencia: los peces desaparecieron y huele mal.",
        "Al argumentar puedo decir: «Opino que hay que limpiar el arroyo porque la basura mató a los peces y afecta a los vecinos». Aquí aparece una consecuencia como razón. Es más completo agregar una causa: «y la causa fue la falta de basureros». Las opiniones sobre un problema deben considerar a varios actores, porque cada uno vive la situación de manera distinta.",
    ],
    vocab=[("causa", "razón que hace que algo ocurra"), ("consecuencia", "lo que sucede a raíz de un hecho"), ("actor", "persona o grupo que participa en un hecho"), ("corto plazo", "que ocurre pronto"), ("largo plazo", "que ocurre mucho después")],
    worked=[
        W("Separar causa y consecuencia", "En Valle Claro (comuna inventada) no hay basureros junto al arroyo y los peces murieron. ¿Cuál es la causa y cuál la consecuencia?",
          ["Pregunto qué ocurrió primero.", "La falta de basureros llevó a botar basura al arroyo.", "Luego murieron los peces."], "Causa: no hay basureros; consecuencia: murieron los peces"),
        W("Nombrar actores", "En el mismo caso participan: vecinos que botan basura, el municipio que instala basureros y un almacén que vende bolsas plásticas. ¿Quiénes son los actores?",
          ["Busco personas o grupos que participan.", "Vecinos.", "Municipio y almacén."], "Los vecinos, el municipio y el almacén"),
    ],
    mistakes=[
        M("Culpar a una sola persona de todo el problema.", "Los problemas tienen varias causas y varios actores.", "Busca al menos dos causas y nombra a todos los actores."),
        M("Confundir la consecuencia con la causa.", "La causa viene antes y la consecuencia después.", "Pregunta qué pasó primero y qué pasó luego."),
    ],
    tiers=tiers(
        [ex("En Historia: ¿qué es una causa?", "Una razón que hace que algo ocurra", "Explica por qué pasó algo."),
         ex("¿Qué es un actor en un hecho?", "Una persona o un grupo que participa", "Hay actores en todo hecho."),
         ex("En Valle Claro, el arroyo huele mal porque se botó basura. ¿Qué es «huele mal»: causa o consecuencia?", "Consecuencia", "Ocurrió después de botar la basura.")],
        [ex("¿Por qué es mejor mirar varias causas que una sola?", "Porque los problemas suelen tener más de una causa", "Una sola causa deja la explicación incompleta."),
         ex("¿Cuál de estas consecuencias ocurre a corto plazo? A) Un arroyo sucio mata peces esta semana. B) Unos árboles plantados hoy darán sombra dentro de veinte años.", "A", "Ocurre muy pronto, esta semana."),
         ex("¿Por qué conviene considerar a varios actores al opinar sobre un problema?", "Porque cada uno vive el problema de manera distinta", "Así la opinión no es parcial.")],
        [ex("En Valle Claro, el almacén vende bolsas, el municipio no puso basureros y algunos vecinos botan basura. Clasifica «el municipio» como causa, actor o consecuencia.", "Actor", "Es un grupo que participa."),
         ex("Elige la opinión que usa una consecuencia: A) «Hay que limpiar el arroyo porque me da pena.» B) «Hay que limpiar el arroyo porque murieron los peces y huele mal.»", "B", "Da consecuencias como razón."),
         ex("Une la causa con su consecuencia: causa «no hay basureros»; consecuencias: A) botan basura al arroyo o B) hay más árboles.", "A", "Sin basureros, la gente bota la basura en cualquier parte.")],
        [ex("Pablo dice: «La culpa es solo de los vecinos». ¿Qué le preguntas para revisar su opinión?", "Qué otros actores y causas hay", "El problema tiene varios actores."),
         ex("Ana afirma: «Los peces murieron, así que no había basureros». ¿Qué confundió?", "La consecuencia con la causa", "Los peces murieron después.")],
        [ex("Completa con otra causa: «El arroyo se llenó de basura porque no había basureros y porque ______». Elige: A) se botaba basura en la orilla, B) los peces murieron.", "A", "B es una consecuencia, no una causa."),
         ex("Ordena una opinión completa: A) la causa fue la falta de basureros, B) opino que hay que limpiar el arroyo, C) porque murieron los peces.", "B, C, A", "Opinión, consecuencia como razón y causa.")],
    ),
    context=[ex("En tu curso se rompió el cuaderno de asistencia porque nadie lo guardó. ¿Cuál es la causa y cuál la consecuencia?", "Causa: nadie lo guardó; consecuencia: se rompió", "La causa ocurre antes.")],
    selfcheck=[ex("En Historia: ¿qué es una consecuencia?", "Lo que sucede a raíz de un hecho", "Ocurre después del hecho."), ex("¿Qué es un actor?", "Un grupo o persona que participa en un hecho", "Hay varios actores."), ex("¿Qué se pregunta para hallar causas?", "Por qué pasó", "Busca las razones.")],
    open_task=task("Elige un problema inventado: A) un parque con plantas secas en Valle Claro, B) una cancha sin uso en un barrio, C) una biblioteca de curso que se desordena. Escribe dos causas, tres actores y dos consecuencias. Luego escribe una opinión con una razón basada en una consecuencia.", "Tema A. Causas: no hay riego y hace calor. Actores: vecinos, municipio y colegio. Consecuencias: las plantas mueren y el parque se ve triste. Opino que hay que regarlo porque las plantas mueren.", ["dos causas", "tres actores", "dos consecuencias", "opinión con razón"], ["lista de causas, actores y consecuencias y una opinión"], ["culpar a una sola persona", "confundir causa y consecuencia"], "Muestra tu lista a una persona de tu casa y pídele que revise si cada causa viene antes."),
    reinforce="Piensa en un problema de tu cuadra y di una causa y una consecuencia.",
    extend="Explica por qué una consecuencia puede ser causa de otro problema.",
)

register(
    OA20, 4,
    materials="Este cuaderno y un lápiz. Las dos opiniones del caso están escritas en los ejercicios.",
    use="Aprenderé a comparar perspectivas o lugares distintos sobre un mismo tema y a responder con respeto. Sirve para conversar y debatir sin pelear, y para mejorar mi opinión.",
    prior=["Sé relacionar causas, actores y consecuencias.", "Sé ubicar un tema en el tiempo y el espacio."],
    explain=[
        "Una perspectiva es la manera de mirar un tema según quién eres, dónde vives y qué necesitas. Dos personas pueden ver el mismo hecho de manera distinta. Por ejemplo, ante un nuevo paseo junto al río, un comerciante puede decir que traerá clientes y un vecino puede decir que traerá ruido. Ambos pueden tener razones válidas desde su perspectiva.",
        "Para comparar perspectivas hago una lista con tres columnas: qué opina cada uno, qué razón da y qué necesita o teme. Luego busco en qué coinciden y en qué se diferencian. Compruebo si cada razón es un dato o una opinión, y si usa fuentes. También puedo comparar territorios: lo que sirve para una ciudad grande puede no servir para un pueblo pequeño.",
        "Responder con respeto significa criticar la idea y no a la persona: «Entiendo tu razón, pero yo veo otro problema». También es importante cambiar de opinión cuando escucho una razón mejor. Cambiar de opinión con buenos motivos no es perder, es aprender. Si no cambio, debo explicar por qué mis razones siguen siendo más fuertes.",
    ],
    vocab=[("perspectiva", "manera de mirar un tema según quién eres y dónde vives"), ("coincidir", "estar de acuerdo en algo"), ("diferir", "pensar distinto"), ("contraargumento", "razón que responde a otra opinión"), ("respeto", "tratar con consideración a quien piensa distinto")],
    worked=[
        W("Comparar dos perspectivas", "Paseo nuevo junto al río. Comerciante: «Traerá clientes». Vecino: «Traerá ruido de noche». ¿Qué necesita o teme cada uno?",
          ["Miro quién habla.", "El comerciante necesita vender.", "El vecino teme el ruido."], "Comerciante: clientes; vecino: tranquilidad"),
        W("Responder con respeto", "Una compañera dice: «No hay que hacer el paseo, porque traerá ruido». Tú no estás de acuerdo. Escribe una respuesta respetuosa.",
          ["Reconozco su razón.", "Critico la idea, no a ella.", "Doy mi razón."], "Entiendo tu razón del ruido, pero creo que el paseo ayudará a los comerciantes"),
    ],
    mistakes=[
        M("Responder con insultos a quien piensa distinto.", "Se ataca a la persona y no se debate la idea.", "Responde a su razón con otra razón, con respeto."),
        M("Creer que cambiar de opinión es perder.", "Cambiar con buenas razones muestra que escuchaste.", "Revisa si la razón nueva es mejor y cámbiala si lo es."),
    ],
    tiers=tiers(
        [ex("¿Qué es una perspectiva?", "La manera de mirar un tema según quién eres y dónde vives", "Cambia de persona en persona."),
         ex("¿Qué significa «coincidir» en un debate?", "Estar de acuerdo en algo", "Es lo contrario de diferir."),
         ex("¿Qué se critica en un buen debate: la idea o la persona?", "La idea", "El respeto exige no atacar a las personas.")],
        [ex("¿Por qué dos personas pueden opinar distinto con buenas razones sobre el mismo hecho?", "Porque tienen perspectivas y necesidades distintas", "Cada una mira desde su lugar."),
         ex("¿Qué tres columnas sirven para comparar dos opiniones?", "Qué opina, qué razón da y qué necesita o teme", "Ordenan la comparación."),
         ex("¿Qué debe hacer alguien que no cambia de opinión después de escuchar otra?", "Explicar por qué sus razones siguen siendo más fuertes", "Mantener una opinión exige fundamentos.")],
        [ex("Elige la respuesta respetuosa: A) «Eres tonto por pensar eso.» B) «Entiendo tu razón, pero yo veo otro problema.»", "B", "Critica la idea y no a la persona."),
         ex("Una ciudad grande y un pueblo pequeño quieren copiar una línea de buses que funciona en otra comuna. Antes de decidir, ¿qué conviene comparar entre los territorios?", "Las características de cada territorio", "Lo que sirve en un lugar puede no servir en otro."),
         ex("Dos vecinos opinan: A) «Más luz en la plaza» y B) «Plaza más iluminada». ¿Coinciden o difieren?", "Coinciden", "Piden lo mismo con otras palabras.")],
        [ex("Rosa dice: «Cambié de opinión porque ahora entiendo que el ruido molesta a los vecinos». ¿Es eso perder el debate?", "No, porque cambió con una razón mejor", "Aprender es parte de debatir."),
         ex("Julián copia la opinión de su amigo sin revisar sus razones. ¿Qué debería hacer antes?", "Revisar si las razones son buenas", "Una opinión se apoya en fundamentos propios.")],
        [ex("Ordena una respuesta con respeto: A) pero yo creo que el paseo traerá turistas, B) entiendo que te preocupa el ruido, C) además, propongo un horario de cierre.", "B, A, C", "Primero reconoce, luego discrepa y propone."),
         ex("Un comerciante y un vecino coinciden en que el paseo debe ser seguro. ¿Qué punto de acuerdo se puede usar para buscar una solución?", "La seguridad del paseo", "Parte de lo que comparten.")],
    ),
    context=[ex("En una reunión de curso, Camila y Tomás discuten si el recreo largo debe ser en la mañana o en la tarde. ¿Qué haces primero para comparar sus perspectivas?", "Preguntar qué razón y qué necesidad tiene cada uno", "Entender antes de decidir.")],
    selfcheck=[ex("En Historia: ¿qué es una perspectiva?", "Una manera de mirar un tema según quién eres", "Es una idea central."), ex("¿Qué es un contraargumento?", "Una razón que responde a otra opinión", "Sirve para debatir."), ex("¿Qué debe tener una respuesta respetuosa?", "Una crítica a la idea y no a la persona", "Así el debate no hiere.")],
    open_task=task("Elige un tema: A) construir una ciclovía en una calle angosta, B) cerrar un patio para plantar un huerto, C) hacer una feria de libros. Escribe la opinión de dos personas distintas con su razón y lo que necesita o teme cada una. Escribe en qué coinciden y una respuesta respetuosa que reconozca una razón.", "Tema A. Ciclista: seguridad. Vecino: menos estacionamientos. Coinciden: quieren calles seguras. Respuesta: entiendo que faltarán lugares, pero la ciclovía evita choques.", ["dos perspectivas", "razones distintas", "punto de acuerdo", "respuesta respetuosa"], ["comparación de dos perspectivas y una respuesta"], ["atacar a la persona", "no reconocer ninguna razón del otro"], "Lee tu comparación a una persona de tu casa y pídele que diga qué perspectiva falta."),
    reinforce="Con una persona de tu casa, comparen dos formas de pasar la tarde y digan en qué coinciden.",
    extend="Escribe una frase para cambiar de opinión con respeto cuando escuchas una razón mejor.",
)

register(
    OA20, 5,
    materials="Este cuaderno y un lápiz. Los datos del caso están escritos en los ejercicios.",
    use="Aprenderé a escribir una opinión argumentada con afirmación, evidencia y explicación. Sirve para participar en debates y trabajos de la asignatura con ideas bien apoyadas.",
    prior=["Sé comparar perspectivas y responder con respeto.", "Sé que una razón fuerte usa evidencia de una fuente."],
    explain=[
        "Una opinión argumentada con fundamentos tiene tres partes. La afirmación dice lo que pienso. La evidencia es el dato, el ejemplo o la fuente que lo apoya. La explicación muestra por qué esa evidencia apoya mi afirmación. Por ejemplo: «Creo que el patio necesita más sombra (afirmación). Esta semana, a mediodía, 12 estudiantes se sentaron bajo el único árbol (evidencia). Eso muestra que falta sombra para todos (explicación)».",
        "También conviene mirar el contraargumento, que es la razón del que piensa distinto. Puedo escribir: «Algunos dicen que la sombra cuesta dinero, pero se pueden plantar árboles con ayuda de las familias». Reconocer la otra razón y responderla vuelve mi opinión más sólida. Así muestro que pensé en varios actores y no solo en mí.",
        "Hay razones que parecen buenas, pero no lo son. «Todos lo piensan» no prueba nada. «Siempre se hizo así» no explica si es justo. «Lo dijo una persona importante» no basta si no da datos. Una buena evidencia es concreta, se puede comprobar y viene de una fuente. Termino con una conclusión que repite mi afirmación y propone algo.",
    ],
    vocab=[("afirmación", "idea principal que sostengo"), ("evidencia", "dato, ejemplo o fuente que apoya la afirmación"), ("explicación", "razonamiento que une la evidencia con la afirmación"), ("contraargumento", "razón de quien piensa distinto"), ("conclusión", "cierre que resume la opinión y propone algo")],
    worked=[
        W("Reconocer las tres partes", "«Creo que el patio necesita más sombra. Esta semana, a mediodía, 12 estudiantes se sentaron bajo el único árbol. Eso muestra que falta sombra para todos». Señala la evidencia.",
          ["La afirmación es la primera frase.", "La evidencia es el dato de 12 estudiantes.", "La explicación es la última."], "La evidencia es que 12 estudiantes se sentaron bajo el único árbol"),
        W("Responder un contraargumento", "Alguien dice: «Plantar árboles cuesta dinero». Redacta una respuesta.",
          ["Reconozco la razón.", "Propongo una solución.", "Mantengo mi afirmación."], "Cuesta dinero, pero se puede plantar con ayuda de las familias"),
    ],
    mistakes=[
        M("Dar la afirmación sin evidencia.", "Parece un gusto personal y no convence.", "Agrega un dato, un ejemplo o una fuente."),
        M("Usar «todos lo piensan» como evidencia.", "Cuántos lo repiten no prueba que sea cierto.", "Usa un dato que se pueda comprobar."),
    ],
    tiers=tiers(
        [ex("¿Cuáles son las tres partes de una opinión argumentada?", "Afirmación, evidencia y explicación", "Es la estructura de la clase."),
         ex("¿Qué es la evidencia?", "Un dato, ejemplo o fuente que apoya la afirmación", "Sostiene la idea principal."),
         ex("«Todos lo piensan», ¿es una buena evidencia?", "No", "No se puede comprobar con un dato.")],
        [ex("¿Para qué sirve la explicación en un argumento?", "Para mostrar por qué la evidencia apoya la afirmación", "Une la evidencia con la idea."),
         ex("¿Qué logra quien responde un contraargumento?", "Hace su opinión más sólida", "Muestra que pensó en la otra razón."),
         ex("¿Qué debe incluir una conclusión?", "La afirmación repetida y una propuesta", "Cierra y ofrece una acción.")],
        [ex("En «Creo que la biblioteca de curso necesita más libros. En ella hay 8 libros para 30 estudiantes», ¿qué parte es «hay 8 libros para 30 estudiantes»?", "La evidencia", "Es un dato que se comprueba."),
         ex("Elige la evidencia más fuerte: A) «Siempre ha sido así.» B) «En la encuesta del curso, 20 de 30 pidieron más libros.»", "B", "Es un dato concreto."),
         ex("Elige la explicación que une el dato «12 estudiantes se sentaron bajo un solo árbol» con la afirmación «falta sombra»: A) «Eso muestra que no alcanza la sombra.» B) «Me gustan los árboles.»", "A", "Relaciona el dato con la idea.")],
        [ex("Diego dice: «Hay que cerrar la cancha porque lo dijo una persona famosa». ¿Qué le falta a su argumento?", "Evidencia concreta que se pueda comprobar", "Lo dijo alguien famoso no prueba nada."),
         ex("Elena usa solo «siempre se hizo así». ¿Por qué es una razón débil?", "Porque no explica si es justo o útil", "La costumbre no es evidencia.")],
        [ex("Ordena el argumento: A) eso muestra que falta sombra, B) creo que el patio necesita más sombra, C) 12 estudiantes se sentaron bajo un solo árbol.", "B, C, A", "Afirmación, evidencia y explicación."),
         ex("Completa con un contraargumento y una respuesta: «Algunos dicen que sembrar árboles es caro, pero ______». Elige la mejor: A) se puede pedir ayuda a las familias, B) todos piensan que no importa.", "A", "Responde con una propuesta.")],
    ),
    context=[ex("En una reunión de curso, una compañera dice: «Debemos tener un día sin celulares porque yo lo digo». ¿Qué le sugieres agregar?", "Una evidencia que apoye su afirmación", "Una afirmación necesita datos o ejemplos.")],
    selfcheck=[ex("En Historia: ¿qué es argumentar con evidencia?", "Apoyar una opinión con datos o fuentes", "Es el fin de la clase."), ex("¿Qué es un contraargumento?", "La razón de quien piensa distinto", "Se responde con respeto."), ex("¿Qué cierra una buena opinión?", "Una conclusión con propuesta", "Termina con una acción.")],
    open_task=task("Elige un tema: A) más sombra en el patio, B) más libros en la biblioteca del curso, C) un día de limpieza del barrio. Escribe una opinión con afirmación, una evidencia (puedes inventar un dato razonable y escribir que es «dato de ejemplo»), una explicación, un contraargumento con tu respuesta y una conclusión con propuesta.", "Tema B. Creo que necesitamos más libros. En la biblioteca de ejemplo hay 8 libros para 30 estudiantes. Eso no alcanza para todos. Algunos dicen que son caros, pero se pueden recibir donaciones. Propongo una campaña de libros usados.", ["afirmación clara", "evidencia concreta (si es inventada, dice «dato de ejemplo»)", "explicación", "contraargumento respondido", "conclusión con propuesta"], ["texto de seis partes en orden"], ["sin evidencia", "atacar a quien piensa distinto"], "Lee tu texto a una persona de tu casa y pídele que marque las tres partes del argumento."),
    reinforce="Di una opinión sobre tu colegio con un dato y una explicación.",
    extend="Elige una razón débil que hayas escuchado y escríbela de nuevo con evidencia.",
)

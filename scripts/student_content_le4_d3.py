"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 26 (convenciones sociales según la situación)."""
from __future__ import annotations

from student_content_le4_d import E, reg
from student_lessons import arith

OA26 = "LE04 OA 26"

# ================================================================ OA 26 · clase 1
reg(
    OA26, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar las presentaciones.",
    "Aprenderé a presentarme y a presentar a otras personas con fórmulas de cortesía claras. Sirve para empezar bien una conversación con personas que no conozco o que no se conocen entre sí.",
    ["Sé decir mi nombre y saludar.", "Sé hablar con voz clara."],
    [
        "Presentarse es decir quién eres para que otra persona te conozca. Una presentación breve incluye un saludo, tu nombre y, si quieres, un dato que ayude a conversar, como algo que te gusta hacer. Por ejemplo: «Hola, me llamo Leo y me gusta nadar». No hace falta decir datos privados, como la dirección de tu casa o tu número de teléfono, a una persona que recién conoces.",
        "También podemos presentar a otras personas que no se conocen. Decimos el nombre de ambas y, si sirve, un dato que las conecte: «Ema, te presento a Tomás, que también juega ajedrez». Con una persona mayor o con alguien a quien queremos mostrar respeto, usamos «le» y nombramos primero a esa persona: «Profesor Mario, le presento a mi compañera Rosa».",
        "Después de presentar, quien escucha puede responder «Mucho gusto» o «Encantada» y repetir el nombre. Repetir el nombre ayuda a recordarlo. Una presentación respetuosa se dice con voz clara, mirando a la persona.",
    ],
    [("presentarse", "decir quién eres a alguien que no te conoce"), ("presentar", "decir quién es una persona a otra que no la conoce"), ("fórmula de cortesía", "frase amable que se usa en situaciones sociales"), ("dato privado", "información personal que no conviene decir a desconocidos"), ("respeto", "trato amable hacia las otras personas")],
    [
        ("Presentarse", "Leo llega a un taller y quiere presentarse. ¿Qué frase sirve: a) «Hola, me llamo Leo y me gusta nadar» b) «Hola, vivo en la calle Los Olmos 123»?", ["Busco la presentación que dice el nombre y algo que gusta.", "La b da una dirección, que es un dato privado.", "La a es la presentación adecuada."], "a."),
        ("Presentar a otra persona", "Quieres presentar a tu compañera Rosa al profesor Mario. ¿Qué frase es correcta: a) «Profesor Mario, le presento a mi compañera Rosa.» b) «Rosa, ese es el profe.»", ["Veo que incluya los dos nombres.", "La a nombra a ambos y trata con respeto al profesor.", "La b no dice el nombre del profesor."], "a."),
    ],
    [("Presentarse con una frase que solo dice «Soy yo».", "Se cree que la otra persona ya sabe quién es.", "Di tu nombre y un saludo: «Hola, me llamo…»."), ("Dar la dirección o el teléfono al presentarse.", "Se confunde presentarse con dar todos los datos.", "Di tu nombre y algo que te gusta; los datos privados no se dan a desconocidos.")],
    [
        E("¿Qué dato se dice primero al presentarse: tu nombre o tu dirección?", "Tu nombre", "El nombre es lo básico para presentarse."),
        E("Frase: «Ema, te presento a Tomás». ¿A quién se presenta a Ema?", "A Tomás", "La frase dice «te presento a Tomás»."),
        E("¿Conviene decir tu dirección a una persona que recién conoces?", "No", "Es un dato privado."),
    ],
    [
        E("¿Qué incluye una presentación breve: un saludo, tu nombre y un dato que ayude a conversar?", "Sí", "Esas partes bastan para empezar."),
        E("Quieres presentar a una amiga con tu abuela. ¿Qué frase incluye los dos nombres: a) «Abuela, te presento a mi amiga Ema» b) «Esta es mi amiga»?", "a", "La a nombra a Ema y deja claro a quién se dirige."),
        E("¿Por qué es útil repetir el nombre de la persona después de que te la presentan?", "Para recordarlo", "Repetir ayuda a fijar el nombre."),
    ],
    [
        E("Ordena una presentación: a) me gusta dibujar, b) Hola, c) me llamo Ema. Escribe las letras.", "b, c, a", "Primero saludas, luego dices tu nombre y después un dato."),
        E("Completa con «te» o «le»: «Profesor Mario, ___ presento a mi compañera Rosa». Escribe la palabra.", "le", "Con una persona a quien se trata con respeto se usa «le»."),
        E("En «Hola, me llamo Leo, soy de cuarto básico y me gusta nadar», ¿cuántos datos dice Leo sobre sí mismo?", "Tres", "Nombre, curso y gusto."),
    ],
    [
        E("Presentación A: «Soy Tomás, vivo en Los Olmos 123 y mi teléfono es largo». Presentación B: «Me llamo Tomás y me gusta jugar al fútbol». ¿Cuál es más adecuada para alguien que recién conoces?", "La B", "No da datos privados."),
        E("Dices: «Este es mi amigo». ¿Qué falta para presentarlo bien?", "Su nombre", "Una presentación incluye el nombre de la persona."),
    ],
    [
        E("Una compañera nueva llega al curso. Carla quiere presentarla a Pablo, a quien también le gusta dibujar. ¿Qué frase es mejor: a) «Pablo, te presento a Lía; a ella también le gusta dibujar» b) «Pablo, esta es una niña»?", "a", "Incluye los nombres y un dato en común."),
        E("Después de que te presentan a alguien, ¿qué respuesta cortés sirve: a) «Mucho gusto, Lía» b) «Qué raro»?", "a", "Es cortés y repite el nombre."),
    ],
    [E("Estás en un taller de ajedrez y llegan dos niños que no se conocen: Ema y Tomás. A ambos les gusta el ajedrez. Eliges esta presentación: «Ema, te presento a Tomás, que también juega ajedrez». ¿Qué cumple esa frase: a) incluye los dos nombres y un dato en común b) solo dice un saludo?", "a", "Nombra a ambos y los conecta.")],
    [
        E("¿Presentarse es decir quién eres?", "Sí", "Así otras personas te conocen."),
        E("¿Hay que dar tu número de teléfono al presentarte a un desconocido?", "No", "Es un dato privado."),
        E("Para presentar a dos personas, ¿conviene decir el nombre de ambas?", "Sí", "Así se conocen."),
    ],
    ("Practica presentaciones. Lee estas dos situaciones. Situación 1: llegas a un taller de pintura donde nadie te conoce. Situación 2: tu amigo Mateo se encuentra con tu profesora Ana y no se conocen. Escribe o di: 1) cómo te presentas en la situación 1 con saludo, nombre y un dato que te guste, 2) cómo presentas a Mateo con la profesora Ana, usando «le» y el dato de que a Mateo le gusta dibujar. Practícalo en voz alta con una persona de tu casa.",
     "1) Hola, me llamo Leo y me gusta pintar con acuarela. 2) Profesora Ana, le presento a mi amigo Mateo, a quien le gusta dibujar.",
     ["la presentación tiene saludo y nombre", "usa un dato adecuado y no privado", "presenta a Mateo con los dos nombres", "usa «le» con la profesora"], ["texto escrito u oral"], ["dar datos privados", "olvidar el nombre de alguien"],
     "Si algo falta, revisa: ¿dije el nombre de cada persona? ¿usé una fórmula respetuosa?"),
    "Practica con tu familia decir tu nombre y un dato que te guste en voz clara.",
    "Escribe una presentación para un compañero nuevo que llega a tu curso, incluyendo un dato que los conecte.",
)

# ================================================================ OA 26 · clase 2
reg(
    OA26, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar saludos distintos.",
    "Aprenderé a saludar y despedirme de manera adecuada según con quién hablo y en qué momento. Sirve para tratar con cortesía a amigos, familia y personas adultas.",
    ["Sé saludar con «hola».", "Sé que se puede hablar de «tú» o de «usted»."],
    [
        "Saludar es la primera forma de cortesía. Cambiamos el saludo según la situación. Con amigos y compañeros usamos un trato informal: «Hola, ¿cómo estás?». Con personas adultas que no conocemos bien, como un profesor, una vecina o una persona que atiende en una tienda, usamos un trato más formal: «Buenos días, ¿cómo está usted?».",
        "También cambiamos el saludo según el momento del día. Por la mañana decimos «buenos días». Durante la tarde decimos «buenas tardes». Cuando ya es de noche decimos «buenas noches», que además sirve para despedirse antes de dormir. Para despedirnos podemos decir «adiós», «hasta luego» o «hasta mañana», según cuándo volvamos a vernos.",
        "El tono y el gesto acompañan al saludo: mirar a la persona, sonreír y hablar con voz clara. Si una persona saluda, lo cortés es responder. Y si no sabemos si usar «tú» o «usted», en una situación formal es mejor usar «usted».",
    ],
    [("saludo", "palabra o frase con que empezamos a hablar con alguien"), ("trato formal", "manera respetuosa de hablar, como con «usted»"), ("trato informal", "manera cercana de hablar, como con «tú»"), ("despedida", "palabra o frase con que terminamos de hablar"), ("contexto", "situación en que ocurre una conversación")],
    [
        ("Saludo según el momento", "Entras a la biblioteca por la mañana. ¿Qué saludo dices a la bibliotecaria: a) «Buenos días» b) «Buenas noches»?", ["Pienso en el momento del día.", "Es por la mañana.", "Corresponde «buenos días»."], "a."),
        ("Saludo según la persona", "Te encuentras con tu profesor Mario por la tarde. ¿Qué saludo es más adecuado: a) «Buenas tardes, profesor, ¿cómo está usted?» b) «Hola, ¿qué onda?»", ["Pienso en quién es la persona.", "Un profesor es una persona adulta a quien tratamos con respeto.", "La a usa «buenas tardes» y «usted»."], "a."),
    ],
    [("Usar el mismo saludo con todas las personas.", "Se olvida que el trato cambia con la situación.", "Con adultos o en situaciones formales usa «usted» y un saludo completo."), ("Despedirse con «buenos días» cuando se va a dormir.", "Se confunden los saludos de cada momento.", "Para la noche usa «buenas noches».")],
    [
        E("¿Qué saludo corresponde por la mañana?", "Buenos días", "Es el saludo de la mañana."),
        E("¿Qué saludo corresponde cuando ya es de noche?", "Buenas noches", "Se usa en la noche."),
        E("Con un amigo, ¿usamos el trato informal o el formal?", "El informal", "Entre amigos usamos «tú»."),
    ],
    [
        E("¿Qué trato usas con una persona adulta a la que recién conoces: «tú» o «usted»?", "Usted", "Es una forma de respeto."),
        E("Terminas de hablar con tu compañero y lo verás mañana en la escuela. ¿Qué despedida sirve: a) «Hasta mañana» b) «Hasta nunca»?", "a", "La a es amable y dice cuándo se verán."),
        E("¿Por qué conviene responder cuando alguien saluda?", "Porque es una muestra de cortesía", "Responder reconoce a la otra persona."),
    ],
    [
        E("Llegas a una tienda por la tarde y debes saludar a quien atiende. ¿Cuál saludo es mejor: a) «Buenas tardes, ¿cómo está?» b) «Ey, ¿qué hay?»", "a", "La a es cortés y se ajusta al momento y a la persona."),
        E("Tu vecina sale por la mañana a regar. ¿Cómo la saludas: a) «Buenos días, doña Rosa» b) «Buenas noches, doña Rosa»?", "a", "Es por la mañana."),
        E("Ordena: a) Buenas tardes, b) ¿cómo está usted?, c) profesor. Escribe las letras para decir «Buenas tardes, profesor, ¿cómo está usted?».", "a, c, b", "Primero el saludo, luego el nombre y después la pregunta."),
    ],
    [
        E("Un compañero saluda a su abuela diciendo «Ey, tú, ven para acá». ¿Es un saludo adecuado para mostrar respeto?", "No", "Es poco cortés para una persona mayor."),
        E("Dos niños se saludan en el recreo: «Hola, ¿cómo estás?». Ahora uno saluda a la directora: «Hola, ¿cómo estás?». ¿Qué cambiarías en el saludo a la directora?", "Usar «buenos días» o «buenas tardes» y «usted»", "Es una situación más formal."),
    ],
    [
        E("Un niño llega por la mañana a la sala y dice «buenas noches». ¿Qué error cometió?", "Usó un saludo de otro momento del día", "Debió decir «buenos días»."),
        E("Después de la cena, sales de casa de tu amiga. ¿Qué despedida es adecuada: a) «Buenas noches, gracias por todo» b) «Buenos días, adiós»?", "a", "Es de noche."),
    ],
    [E("Escena: Una doctora sale a recibirte a las 10 de la mañana. ¿Cuál saludo es mejor: a) «Buenos días, doctora, ¿cómo está?» b) «Hola, ¿qué tal, amiga?»", "a", "Combina el momento del día y el trato formal.")],
    [
        E("¿Saludamos igual a un amigo que a una persona adulta que no conocemos?", "No", "Cambia el trato."),
        E("¿«Buenas tardes» se usa en la tarde?", "Sí", "Es el saludo de ese momento del día."),
        E("¿Responder a un saludo es cortés?", "Sí", "Muestra respeto a la otra persona."),
    ],
    ("Practica saludos y despedidas. Lee tres situaciones: 1) por la mañana llegas a la escuela y ves a la directora; 2) por la tarde encuentras a un compañero en la plaza; 3) de noche, antes de dormir, te despides de una persona de tu casa. Escribe o di el saludo o la despedida que usarías en cada una y el trato (tú o usted) que corresponde. Practícalos en voz alta con una persona de tu casa.",
     "1) Buenos días, directora, ¿cómo está usted? 2) Hola, ¿cómo estás? 3) Buenas noches, hasta mañana.",
     ["ajusta el saludo al momento del día", "ajusta el trato a la persona", "usa una despedida adecuada"], ["tres frases escritas u orales"], ["usar el mismo saludo para todos", "mezclar saludos de otros momentos del día"],
     "Si dudas, pregúntate: ¿quién es la persona y qué hora es?"),
    "Haz una lista de tres personas que conoces y escribe cómo las saludarías.",
    "Escribe un diálogo de cuatro líneas entre un niño y un vecino adulto que se saludan y se despiden.",
)

# ================================================================ OA 26 · clase 3
reg(
    OA26, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar preguntas y permisos.",
    "Aprenderé a hacer preguntas claras y a pedir permiso con fórmulas de cortesía como «por favor» y «con permiso». Sirve para conseguir lo que necesito sin molestar a los demás.",
    ["Sé saludar según el momento y la persona.", "Sé decir «por favor» y «gracias»."],
    [
        "Preguntar es pedir información: «¿A qué hora empieza la función?». Una pregunta clara dice qué queremos saber, es corta y se hace en el momento adecuado, por ejemplo cuando la otra persona terminó de hablar. Para empezar con cortesía podemos usar «disculpe» o «perdón, ¿podría decirme…?».",
        "Pedir permiso es preguntar si podemos hacer algo antes de hacerlo. Usamos fórmulas como «¿Puedo…?», «¿Me permite…?» y «con permiso». Decimos «con permiso» al pasar por un lugar estrecho o al entrar a un sitio. Agregamos «por favor» al pedir algo, y esperamos la respuesta. Si la respuesta es «no», aceptamos con respeto.",
        "Según con quién hablemos, ajustamos el trato. A un amigo le decimos: «¿Me prestas el lápiz, por favor?». A una persona adulta que no conocemos: «¿Me podría prestar su lápiz, por favor?». Un permiso también se pide con tiempo, no cuando ya hicimos lo que queríamos.",
    ],
    [("pedir permiso", "preguntar si se puede hacer algo antes de hacerlo"), ("con permiso", "fórmula para pasar o entrar sin molestar"), ("por favor", "fórmula de cortesía al pedir algo"), ("disculpe", "palabra para llamar la atención con respeto"), ("pregunta clara", "pregunta corta que dice exactamente lo que se quiere saber")],
    [
        ("Pedir permiso", "Quieres salir de la sala para ir al baño. ¿Qué dices a la profesora: a) «¿Puedo ir al baño, por favor?» b) «Voy al baño»?", ["Pienso en pedir antes de hacer.", "La a pregunta y usa «por favor».", "La b informa, no pide permiso."], "a."),
        ("Pregunta clara y cortés", "Quieres saber qué hora es y hay una persona adulta a tu lado. ¿Qué dices: a) «Disculpe, ¿me podría decir la hora, por favor?» b) «¿Hora?»", ["Busco la pregunta completa y cortés.", "La a usa disculpe, podría y por favor.", "La b es muy corta y seca."], "a."),
    ],
    [("Hacer lo que queremos y avisar después.", "Se confunde avisar con pedir permiso.", "Pregunta antes y espera la respuesta."), ("Pedir algo sin «por favor» y en tono de orden.", "Se piensa que es más rápido.", "Agrega «por favor» y usa un tono amable.")],
    [
        E("¿Qué se dice al pasar por un lugar estrecho donde hay una persona?", "Con permiso", "Avisa con cortesía que vas a pasar."),
        E("¿Pedir permiso es preguntar antes o después de hacer algo?", "Antes", "Si se pregunta después, ya no es permiso."),
        E("¿Qué fórmula de cortesía agregamos al pedir algo?", "Por favor", "Hace el pedido más amable."),
    ],
    [
        E("Quieres tomar prestado el borrador de un compañero. ¿Qué dices: a) «¿Me prestas el borrador, por favor?» b) «Dame el borrador»?", "a", "La a pide con cortesía."),
        E("¿Qué hacemos si nos responden «no» a un permiso?", "Aceptar con respeto", "Es parte de la cortesía."),
        E("¿Para qué sirve una pregunta clara?", "Para obtener la información que necesitamos", "Dice exactamente lo que queremos saber."),
    ],
    [
        E("A una persona adulta que no conoces le pides un lápiz. ¿Cuál frase usa mejor el trato: a) «¿Me podría prestar su lápiz, por favor?» b) «Dame tu lápiz»", "a", "Usa «usted» y «por favor»."),
        E("Quieres entrar a la sala de computación. ¿Qué dices a la encargada: a) «Con permiso, ¿puedo pasar?» b) «Ya entré»?", "a", "Pide permiso para entrar."),
        E("Ordena para armar una pregunta cortés: a) por favor, b) ¿me podría ayudar, c) Disculpe. Escribe las letras.", "c, b, a", "Disculpe, ¿me podría ayudar, por favor?"),
    ],
    [
        E("Rosa quiere saber a qué hora cierra la biblioteca y dice: «¿Cierran?». ¿Qué le falta a su pregunta para ser clara?", "Decir qué quiere saber: la hora de cierre", "«¿Cierran?» no dice qué se pregunta."),
        E("Un niño ya se sentó en el puesto de otro y luego pregunta: «¿Puedo sentarme?». ¿Pidió permiso a tiempo?", "No", "Preguntó después de hacerlo."),
    ],
    [
        E("Quieres saber si puedes usar el columpio y la persona responde: «Ahora está ocupado». ¿Cuál es la mejor reacción: a) «Entonces espero, gracias» b) «Igual lo uso»?", "a", "Acepta la respuesta con respeto."),
        E("Quieres sacar un libro de la estantería alta y no alcanzas. ¿Cómo pides ayuda a un adulto de la biblioteca: a) «Disculpe, ¿me ayuda a bajar ese libro, por favor?» b) «Bájame ese libro»?", "a", "Es cortés y clara."),
    ],
    [E("Estás en un bus y quieres bajar, pero hay una persona de pie en el pasillo. ¿Qué dices al pasar: a) «Con permiso» b) «Muévase»?", "a", "Pide pasar con cortesía.")],
    [
        E("Antes de usar algo que no es mío, ¿pido permiso?", "Sí", "Es una norma de respeto."),
        E("¿«Con permiso» sirve para pasar o entrar?", "Sí", "Avisa con cortesía."),
        E("¿Una pregunta clara dice lo que quiero saber?", "Sí", "Por eso se entiende."),
    ],
    ("Practica preguntas y permisos. Lee tres situaciones: 1) necesitas un lápiz y tu compañero tiene dos; 2) quieres pasar entre dos personas que conversan en un pasillo; 3) quieres saber a qué hora termina la clase de Música y le preguntas a la profesora. Escribe lo que dirías en cada una, con una fórmula de cortesía y con un trato adecuado a la persona. Luego practícalas en voz alta.",
     "1) ¿Me prestas un lápiz, por favor? 2) Con permiso, ¿puedo pasar? 3) Disculpe, profesora, ¿a qué hora termina la clase de Música?",
     ["usa una fórmula de cortesía en cada caso", "pide antes de actuar", "ajusta el trato a la persona", "la pregunta es clara"], ["tres frases escritas u orales"], ["avisar en vez de pedir", "olvidar el «por favor»"],
     "Si suenan como orden, agrega «por favor» y cambia el tono."),
    "Escribe tres frases para pedir cosas a personas distintas de tu casa.",
    "Escribe un diálogo de cuatro líneas en que alguien pide permiso y recibe un «no».",
)

# ================================================================ OA 26 · clase 4
reg(
    OA26, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar frases.",
    "Aprenderé a expresar lo que opino y lo que siento de manera respetuosa. Sirve para decir lo que me molesta, me alegra o pienso sin ofender a nadie.",
    ["Sé pedir permiso y preguntar con cortesía.", "Sé reconocer emociones como alegría, enojo o pena."],
    [
        "Todas las personas tenemos opiniones y sentimientos, y es sano expresarlos. Una opinión es lo que pensamos sobre algo; un sentimiento es lo que sentimos, como alegría, pena, enojo o vergüenza. Para decirlos con respeto, hablamos de nosotros mismos y no acusamos al otro. Una forma útil es: «Yo me siento… cuando…, porque…».",
        "Por ejemplo, en lugar de decir «Tú siempre tomas mis cosas», podemos decir: «Me siento molesta cuando usas mi estuche sin preguntar, porque lo necesito. ¿Podrías pedírmelo antes?». Así el otro entiende qué pasó y qué necesitamos, y no se siente atacado.",
        "Para dar una opinión usamos frases como «Pienso que…», «Me parece que…» o «En mi opinión…». Cuidamos el tono de voz, el volumen y no usamos insultos ni burlas. Si el otro opina distinto, escuchamos hasta el final. Expresar un sentimiento con respeto no significa guardárselo: significa decirlo de una forma que el otro pueda escuchar.",
    ],
    [("opinión", "lo que pensamos sobre algo"), ("sentimiento", "lo que sentimos, como alegría o pena"), ("mensaje en primera persona", "frase que habla de lo que yo siento, como «me siento…»"), ("acusar", "culpar a alguien con tono de reproche"), ("tono", "manera de decir algo con la voz")],
    [
        ("Cambiar una acusación", "Ema dice: «Tú siempre tomas mis cosas». Quiere decirlo con respeto. ¿Qué frase es mejor: a) «Me siento molesta cuando usas mi estuche sin preguntar» b) «Eres un ladrón»?", ["Busco la frase que habla de lo que Ema siente.", "La a dice «me siento» y cuenta qué pasó.", "La b insulta."], "a."),
        ("Dar una opinión", "Quieres decir lo que piensas de la propuesta de salir al patio. ¿Qué frase sirve: a) «Pienso que es buena idea porque hay sol» b) «Qué idea tan tonta»?", ["Busco la frase con razón y sin insulto.", "La a dice «pienso» y da una razón.", "La b descalifica."], "a."),
    ],
    [("Decir «tú siempre…» o «tú nunca…».", "Se acusa a la persona en vez de contar lo que sentimos.", "Habla de ti: «Me siento… cuando…»."), ("Guardarse lo que sentimos para no molestar.", "Se cree que expresarlo es una falta de respeto.", "Dilo con calma y de forma que el otro pueda escuchar.")],
    [
        E("¿Qué es un sentimiento: lo que pensamos o lo que sentimos?", "Lo que sentimos", "Alegría y pena son ejemplos."),
        E("¿«Pienso que…» sirve para dar una opinión?", "Sí", "Presenta lo que pensamos."),
        E("¿Insultar es una forma respetuosa de expresar un enojo?", "No", "Ofende al otro."),
    ],
    [
        E("¿Cuál es un mensaje en primera persona: «Me siento triste cuando me dejan afuera» o «Tú siempre me dejas afuera»?", "Me siento triste cuando me dejan afuera", "Habla de lo que siente quien lo dice."),
        E("¿Por qué conviene explicar qué necesitamos al decir un sentimiento?", "Para que el otro entienda qué puede hacer", "La necesidad ayuda a resolver."),
        E("Elige la forma completa: a) «Yo me siento… cuando…, porque…» b) «Tú… siempre…»", "a", "La a explica el sentimiento, la situación y la razón."),
    ],
    [
        E("Un compañero habla muy fuerte y te molesta. ¿Cuál es una forma respetuosa de decirlo: a) «Me molesta el ruido fuerte; ¿podrías hablar más bajito?» b) «¡Cállate!»?", "a", "Cuenta lo que siente y pide algo."),
        E("Quieres decir que te alegró que te invitaran al juego. ¿Qué frase sirve: a) «Me sentí contento cuando me invitaron a jugar» b) «Me da lo mismo»?", "a", "Expresa el sentimiento."),
        E("Ordena: a) porque lo necesito, b) cuando usas mi estuche sin preguntar, c) Me siento molesta. Escribe las letras.", "c, b, a", "Primero el sentimiento, luego la situación y después la razón."),
    ],
    [
        E("Luis dice: «Me parece que podemos usar la pizarra para anotar las ideas, porque así todos las ven». Marta dice: «Todo lo que dices es tonto». ¿Quién dio una opinión con respeto?", "Luis", "Opinó con razón y sin insultar."),
        E("«Me da pena que no me esperaran». ¿Es un sentimiento o una opinión?", "Un sentimiento", "Dice lo que siente quien habla."),
    ],
    [
        E("Un amigo dice: «Siento vergüenza cuando me corrigen frente a todos». ¿Qué respuesta es respetuosa: a) «Gracias por contarlo; la próxima vez te lo diré en privado» b) «No seas llorón»?", "a", "Escucha y propone una solución."),
        E("Rosa quiere decir que no le gustó una broma. ¿Qué frase es mejor: a) «Esa broma me hizo sentir mal; prefiero que no la repitas» b) «Eres malo»?", "a", "Cuenta lo que siente y pide un cambio."),
    ],
    [E("Un compañero te pidió prestado tu estuche, lo usó y lo dejó sucio. Quieres decirle cómo te sientes. ¿Qué frase es la mejor: a) «Me siento molesto cuando el estuche vuelve sucio, porque lo uso para estudiar; ¿puedes limpiarlo?» b) «Siempre dejas todo sucio»?", "a", "Expresa un sentimiento con respeto y una petición.")],
    [
        E("¿Los sentimientos se pueden expresar con respeto?", "Sí", "Con frases en primera persona."),
        E("¿Conviene escuchar hasta el final cuando otro opina distinto?", "Sí", "Es parte del respeto."),
        E("¿Un insulto es una opinión respetuosa?", "No", "Descalifica a la persona."),
    ],
    ("Practica expresar sentimientos y opiniones con respeto. Lee tres situaciones: 1) un compañero te interrumpe mientras hablas; 2) te alegró que un amigo te ayudara con una tarea; 3) opinas que es mejor leer en la sala que en el patio, porque hay menos ruido. Escribe o di lo que dirías en cada caso, con una frase que empiece con «Me siento…» o «Pienso que…», y con una razón. Practícalas en voz alta con una persona de tu casa.",
     "1) Me siento molesto cuando me interrumpen, porque pierdo lo que quería decir. 2) Me sentí feliz cuando me ayudaste, porque pude terminar. 3) Pienso que es mejor leer en la sala, porque hay menos ruido.",
     ["usa frases en primera persona", "da una razón", "no acusa ni insulta"], ["tres frases escritas u orales"], ["usar «tú siempre»", "insultar"],
     "Si la frase suena a acusación, cámbiala por «Me siento… cuando…»."),
    "Escribe dos sentimientos y una frase con respeto para cada uno.",
    "Escribe un diálogo de cuatro líneas en que una persona dice un sentimiento con respeto y la otra la escucha.",
)

# ================================================================ OA 26 · clase 5
reg(
    OA26, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar disculpas.",
    "Aprenderé a agradecer, a pedir disculpas y a reparar un error con fórmulas de cortesía. Sirve para cuidar las relaciones con otras personas cuando recibimos ayuda o cuando nos equivocamos.",
    ["Sé decir «gracias» y «perdón».", "Sé expresar sentimientos con respeto."],
    [
        "Agradecer es reconocer algo bueno que otra persona hizo por nosotros. Decimos «gracias» y, mejor aún, decimos por qué: «Gracias por ayudarme a cargar la mochila». La respuesta cortés a un agradecimiento es «de nada» o «con gusto». Un agradecimiento claro hace sentir valorada a la otra persona.",
        "Pedir disculpas es reconocer que nos equivocamos o que lastimamos a alguien. Una disculpa sincera tiene tres partes: reconocer lo que hicimos («Perdón por empujarte»), decir que lo sentimos («Lamento que te hayas lastimado») y ofrecer reparar («¿Puedo ayudarte a recoger tus cosas?»). Reparar es hacer algo para arreglar el daño. La frase «perdón, pero tú también…» no es una disculpa, porque pone la culpa en el otro.",
        "Cuando alguien se disculpa, podemos decir «gracias por decírmelo» o «está bien» si de verdad lo sentimos. A veces necesitamos tiempo; podemos decir que lo pensaremos. Pedir disculpas y agradecer no nos hace menos: nos hace más confiables.",
    ],
    [("agradecer", "reconocer lo bueno que alguien hizo por nosotros"), ("disculpa", "reconocimiento de un error para pedir perdón"), ("reparar", "hacer algo para arreglar el daño que causamos"), ("sincero", "que se dice de verdad, sin excusas"), ("fórmula de cortesía", "frase amable de uso social")],
    [
        ("Agradecer con razón", "Un compañero te ayudó a recoger tus lápices del suelo. ¿Qué frase agradece mejor: a) «Gracias por ayudarme a recoger los lápices» b) «Gracias»?", ["Busco la frase que dice por qué se agradece.", "La a nombra la ayuda.", "La b es correcta, pero no dice por qué."], "a."),
        ("Pedir disculpas y reparar", "Sin querer, empujas a Lía y se le caen los cuadernos. ¿Qué disculpa tiene las tres partes: a) «Perdón por empujarte; lamento que se cayeran tus cuadernos. ¿Te ayudo a recogerlos?» b) «Perdón, pero estabas en el camino»?", ["Busco reconocer, lamentar y reparar.", "La a reconoce el empujón, lo lamenta y ofrece ayudar.", "La b pone la culpa en Lía."], "a."),
    ],
    [("Decir «perdón, pero tú…» al disculparse.", "Se quiere defender y se culpa al otro.", "Reconoce lo que hiciste y ofrece reparar, sin excusas."), ("Decir solo «perdón» sin hacer nada.", "Se cree que la palabra basta.", "Agrega una acción para reparar, si se puede.")],
    [
        E("¿Qué respuesta cortés sigue a un «gracias»: «de nada» o «ni te acerques»?", "De nada", "Es la respuesta cortés."),
        E("En Lenguaje: ¿Qué significa reparar?", "Hacer algo para arreglar el daño", "Se trata de arreglar lo que se rompió o dolió."),
        E("¿«Perdón, pero tú también…» es una buena disculpa?", "No", "Pone la culpa en el otro."),
    ],
    [
        E("Una disculpa sincera tiene tres partes: reconocer lo que hicimos, decir que lo sentimos y ofrecer reparar. ¿Cuántas partes tiene?", "Tres", "Son reconocer, lamentar y reparar."),
        E("¿Por qué conviene decir por qué agradecemos?", "Porque muestra qué valoramos de lo que hizo la otra persona", "La razón hace el agradecimiento más claro."),
        E("Escuchas: «Perdón por llegar tarde; no volverá a pasar y traeré los materiales». ¿Qué parte repara: «no volverá a pasar» o «traeré los materiales»?", "Traeré los materiales", "Es una acción concreta."),
    ],
    [
        E("Una vecina te prestó su paraguas. Elige la mejor frase de agradecimiento: a) «Gracias por prestarme el paraguas, me sirvió mucho» b) «Chao»", "a", "Dice por qué agradece."),
        E("Rompiste sin querer el vaso de plástico de un amigo. ¿Qué frase ofrece reparar: a) «Perdón; te ayudo a limpiar y mañana te traigo uno» b) «Los vasos se rompen»?", "a", "Reconoce y ofrece arreglar."),
        E("Ordena una disculpa: a) ¿Te ayudo a recoger tus cosas?, b) Perdón por empujarte, c) Lamento que se te cayeran los lápices. Escribe las letras.", "b, c, a", "Reconoce, lamenta y repara."),
    ],
    [
        E("Dos disculpas: 1) «Perdón por romper tu dibujo; lo dibujo de nuevo contigo». 2) «Perdón, pero lo dejaste en el piso». ¿Cuál es sincera?", "La 1", "Reconoce su acto y repara."),
        E("Una niña dice «gracias» sin mirar y sin decir por qué. ¿Qué podría agregar para que sea más claro?", "Por qué agradece", "La razón hace claro el agradecimiento."),
    ],
    [
        E("Un amigo te pide perdón por haber roto tu lápiz y te trae uno nuevo. Aceptas la disculpa. ¿Qué respuesta sirve: a) «Gracias por decírmelo y por el lápiz» b) «No quiero nada tuyo»?", "a", "Acepta la disculpa y agradece."),
        E("Una compañera te dice «Perdón» por empujarte, pero tú aún estás molesto. ¿Qué respuesta es respetuosa: a) «Gracias por decírmelo; necesito un rato para calmarme» b) «Eres una mala persona»?", "a", "Es honesta sin ofender."),
    ],
    [E("Tropiezas con Mateo y su vaso de agua se derrama sobre su cuaderno. Es un accidente. ¿Qué dices y haces: a) «Perdón, no fue mi intención; te ayudo a secar el cuaderno» b) «No era mi culpa, estaba en medio»?", "a", "Reconoce el hecho y repara.")],
    [
        E("¿Agradecer reconoce algo bueno que alguien hizo?", "Sí", "Muestra que lo valoramos."),
        E("¿Reparar puede ser ayudar a arreglar lo que se rompió?", "Sí", "Es hacer algo por el daño."),
        E("¿«De nada» es una respuesta cortés a un agradecimiento?", "Sí", "Es la fórmula habitual."),
    ],
    ("Practica agradecer y disculparte. Lee tres situaciones: 1) una vecina te devolvió tu pelota que había caído en su patio; 2) cerraste una puerta con fuerza y asustaste a alguien; 3) rompiste sin querer un lápiz de color de un compañero. Escribe o di: una frase de agradecimiento con razón para la 1, y una disculpa con reconocimiento, lamento y reparación para la 2 y la 3. Practícalas en voz alta.",
     "1) Gracias por devolverme la pelota; la estaba buscando. 2) Perdón por cerrar fuerte la puerta; lamento haberte asustado. La próxima vez la cierro despacio. 3) Perdón por romper tu lápiz; lamento que lo necesitaras. Te regalo uno mío.",
     ["agradece diciendo por qué", "reconoce lo que hizo", "dice que lo siente", "ofrece reparar"], ["tres frases escritas u orales"], ["usar «perdón, pero…»", "disculparse sin reparar"],
     "Si falta una parte de la disculpa, revisa: ¿reconocí, lamenté y ofrecí reparar?"),
    "Escribe un agradecimiento para alguien de tu casa por algo concreto que hizo.",
    "Escribe un diálogo de cuatro líneas en que alguien se disculpa y la otra persona responde.",
)

# ================================================================ OA 26 · clase 6
reg(
    OA26, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar la situación completa.",
    "Aprenderé a juntar lo que aprendí sobre convenciones sociales: presentarse, saludar, preguntar, opinar, agradecer y disculparse. Sirve para elegir la fórmula adecuada en una situación completa y decidir qué practicar después.",
    ["Sé presentarme y presentar a otros.", "Sé saludar, pedir permiso, opinar con respeto, agradecer y disculparme."],
    [
        "Las convenciones sociales son formas de comportarnos que ayudan a convivir. En una misma situación podemos necesitar varias a la vez. Por ejemplo, al llegar a una biblioteca nueva saludamos, pedimos ayuda con cortesía, agradecemos y, si hay un error, nos disculpamos. Elegir bien depende de quién es la persona, qué momento es y qué queremos lograr.",
        "Para revisar nuestra manera de actuar podemos hacernos tres preguntas: ¿saludé según el momento y la persona?, ¿pedí con respeto lo que necesitaba?, ¿agradecí o me disculpé cuando correspondía? Si respondemos que no a alguna, ese es nuestro próximo paso: una fórmula que queremos practicar esta semana.",
        "Un buen cierre es resumir lo que descubrimos. Por ejemplo: «Descubrí que me cuesta pedir disculpas sin decir “pero”. Mi próximo paso es practicar la disculpa de tres partes». Así convertimos lo aprendido en un compromiso personal.",
    ],
    [("convención social", "forma de comportarse que ayuda a convivir"), ("situación", "momento y lugar en que ocurre algo"), ("fórmula", "frase que se usa en ciertas situaciones sociales"), ("compromiso", "decisión de hacer algo que hemos dicho"), ("próximo paso", "acción siguiente para mejorar")],
    [
        ("Una situación completa", "Llegas por la tarde a una biblioteca que no conoces, buscas un libro y la bibliotecaria te ayuda. ¿Qué secuencia es adecuada: a) saludar, pedir ayuda con cortesía, agradecer b) pedir ayuda sin saludar y irte sin decir nada?", ["Pienso en cada momento de la situación.", "Se saluda al llegar, se pide con cortesía y se agradece.", "La a lo hace."], "a."),
        ("Elegir próximo paso", "Después de una conversación, Ema se da cuenta de que no pidió permiso antes de tomar un libro. ¿Qué próximo paso le conviene: a) practicar «¿Puedo…?» antes de usar algo de otros b) no ir más a la biblioteca?", ["Busco una acción que mejore lo que falló.", "Practicar pedir permiso mejora lo que no hizo.", "No ir más no lo arregla."], "a."),
    ],
    [("Usar una sola fórmula para todas las situaciones.", "Se olvida que el momento y la persona cambian lo adecuado.", "Pregunta: ¿quién es?, ¿qué momento es?, ¿qué necesito?"), ("Decir que ya lo sabemos todo y no tener un próximo paso.", "Se cree que no hay nada que mejorar.", "Elige una fórmula concreta para practicar.")],
    [
        E("Llegas por la mañana a la escuela y ves a la directora. ¿Qué saludo usas: «Buenos días, directora» o «Buenas noches, directora»?", "Buenos días, directora", "Es por la mañana y se trata a una autoridad con respeto."),
        E("¿Qué fórmula usas para pasar entre dos personas: «Con permiso» o «Hasta luego»?", "Con permiso", "Avisa con cortesía que vas a pasar."),
        E("Recibes ayuda para cargar una caja. ¿Qué dices: «Gracias por ayudarme» o «Nada»?", "Gracias por ayudarme", "Agradece la ayuda."),
    ],
    [
        E("Llegas a una oficina: saludas, preguntas por un papel y recibes ayuda. ¿Qué fórmula falta al final: el agradecimiento o la presentación?", "El agradecimiento", "Tras recibir ayuda se agradece."),
        E("Para revisar mi manera de actuar me pregunto: ¿saludé bien?, ¿pedí con respeto?, ¿agradecí o me disculpé? ¿Cuántas preguntas son?", "Tres", "Se cuentan las tres preguntas."),
        E("Si me di cuenta de que no pido disculpas bien, ¿cuál es mi próximo paso: practicar la disculpa de tres partes o dejar de hablar?", "Practicar la disculpa de tres partes", "Es una acción para mejorar."),
    ],
    [
        E("Llegas a una tienda por la tarde, pides una libreta y recibes ayuda. Ordena: a) Gracias por su ayuda, b) Buenas tardes, c) ¿Me podría mostrar las libretas, por favor? Escribe las letras.", "b, c, a", "Saludar, pedir y agradecer."),
        E("Un niño nuevo se acerca y no conoce a nadie. ¿Qué haces: a) me presento con mi nombre y le pregunto el suyo b) paso sin saludar?", "a", "Presentarse crea confianza."),
        E("Por distracción pisas a alguien en el bus. ¿Qué dices: a) «Perdón por pisarte; ¿te duele? ¿Puedo ayudarte?» b) «Estabas ahí»?", "a", "Reconoce, lamenta y ofrece ayudar."),
    ],
    [
        E("Un niño se presenta, pide con cortesía lo que necesita, recibe ayuda y se va sin decir nada. ¿Qué fórmula le faltó?", "Agradecer", "Debió decir gracias."),
        E("Dos compañeros discutieron y uno dijo «Me siento mal cuando me interrumpen, porque quiero terminar de hablar». ¿Qué hizo: expresar un sentimiento con respeto o descalificar?", "Expresó un sentimiento con respeto", "Habló de lo que siente y pidió algo."),
    ],
    [
        E("Lee: Tomás saluda a la profesora con «Hola, ¿cómo estás?». Luego pide un lápiz sin decir «por favor» y se va sin agradecer. ¿Cuántas fórmulas de cortesía le faltan (saludo formal, «por favor» y agradecimiento)?", "Tres", "Falta cada una de ellas."),
        E("Eliges practicar una sola fórmula esta semana. ¿Cuál de estas es una buena meta: a) «pedir permiso antes de usar cosas ajenas» b) «ser perfecto»?", "a", "La a es concreta y se puede practicar."),
    ],
    [E("Situación: llegas de noche a casa de una amiga para estudiar. Quieres entrar, ayudar con la mesa y despedirte al terminar. ¿Qué serie de frases es adecuada: a) «Buenas noches; con permiso; ¿te ayudo con la mesa?; gracias por recibirme; hasta mañana» b) «Hola; ya estoy; chao»?", "a", "Reúne saludo, permiso, ayuda, agradecimiento y despedida.")],
    [
        E("Una convención social, ¿ayuda a convivir?", "Sí", "Da formas de tratarnos con respeto."),
        E("¿Puedo cambiar mi fórmula según la persona y el momento?", "Sí", "Eso es ajustar al contexto."),
        E("Un próximo paso, ¿debe ser concreto?", "Sí", "Así se puede practicar."),
    ],
    ("Haz una síntesis de tu aprendizaje. Lee esta situación: llegas por la tarde a una sala de ciencias para una actividad. Hay una profesora que no conoces, un compañero nuevo y se cae un material que rompes sin querer. Escribe lo que dirías en orden: saludo, presentación (tuya o del compañero nuevo), un permiso o pregunta, una disculpa por el material y un agradecimiento. Al final escribe una frase con tu próximo paso: qué fórmula quieres practicar más.",
     "Buenas tardes, profesora. Me llamo Leo y él es Tomás, que llegó nuevo. ¿Podemos sentarnos aquí, por favor? Perdón por romper el material; lamento el desorden y ayudo a recoger. Gracias por su paciencia. Próximo paso: practicar la disculpa de tres partes.",
     ["incluye todas las fórmulas pedidas", "las ajusta a la persona y al momento", "escribe un próximo paso concreto"], ["texto escrito u oral con las seis frases"], ["olvidar alguna fórmula", "próximo paso demasiado general"],
     "Si falta una frase, revisa el orden: saludo, presentación, permiso, disculpa, agradecimiento, próximo paso."),
    "Escoge una fórmula de esta unidad y úsala hoy con una persona de tu casa.",
    "Escribe una lista de cinco fórmulas de cortesía y en qué situaciones las usarías.",
)

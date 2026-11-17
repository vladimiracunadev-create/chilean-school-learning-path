"""Servicios de Turismo TP 3.º y 4.º medio: OAE-07 (comunicarse en inglés básico con los turistas). Frases breves originales; todo en papel; datos de ejemplo."""
from __future__ import annotations

from tp_setu_common import build

O7 = "TP-SETU-3y4-OAE-07"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (de ejemplo, inventada). Situaciones en que la agencia «Viajes Brisa» usa inglés básico: (1) en el mostrador, un turista dice «Where is the bus stop?»; (2) por teléfono, una turista dice «I have a reservation for Saturday»; "
     "(3) durante un paseo, un turista dice «Sorry, I do not understand». Reglas de la agencia: hablar despacio con frases cortas, confirmar números y horas también por escrito, no inventar una respuesta si no se entendió, "
     "no pedir datos personales que no hacen falta y tratar con respeto a todas las personas, hablen como hablen.")
build(
    O7, 1, F,
    use="Aprenderé en qué situaciones se usa inglés básico con turistas, qué riesgos tiene un malentendido y varias frases breves para saludar, ofrecer ayuda, pedir que repitan y despedirse con respeto.",
    prior=["Sé saludar y despedirme en español.", "Sé que debo tratar con respeto a todas las personas.", "Sé leer horas y números."],
    explain=[
        "En turismo se usa inglés básico en el mostrador, por teléfono y durante los paseos. El objetivo no es hablar perfecto, sino entenderse con frases cortas y claras. Un malentendido es cuando una persona entiende algo distinto de lo que se quiso decir; puede producir errores en una hora, un precio o una indicación de seguridad. Por eso se habla despacio, se usan frases cortas y se confirman las horas y los números también por escrito.",
        "Frases útiles: «Hello, welcome» (Hola, bienvenido), «How can I help you?» (¿En qué puedo ayudarle?), «One moment, please» (Un momento, por favor), «Could you repeat that, please?» (¿Podría repetirlo, por favor?), «Could you speak more slowly, please?» (¿Podría hablar más despacio, por favor?) y «Thank you» (Gracias), a lo que se responde «You are welcome» (De nada). Si no entiendes, se pide que repita y no se inventa una respuesta.",
        "Se respeta a todas las personas, sin burlarse del acento ni del nivel de inglés de nadie, y no se piden datos personales que no hacen falta. Si el tema es de seguridad en un paseo, lo explica un guía autorizado; este cuaderno es aprendizaje en papel y no te habilita para guiar.",
    ],
    vocab=[("Hello, welcome", "Hola, bienvenido"), ("How can I help you?", "¿En qué puedo ayudarle?"), ("One moment, please", "Un momento, por favor"), ("Could you repeat that, please?", "¿Podría repetirlo, por favor?"), ("Could you speak more slowly, please?", "¿Podría hablar más despacio, por favor?"), ("Sorry, I do not understand", "Perdón, no entiendo"), ("You are welcome", "De nada"), ("malentendido", "cuando se entiende algo distinto de lo que se quiso decir")],
    worked=[
        ("Responder un agradecimiento", "Una turista de ejemplo te dice «Thank you». ¿Qué respondes en inglés?", ["«Thank you» es «gracias».", "La respuesta cortés es «You are welcome», que significa «de nada»."], "You are welcome"),
        ("Pedir que lo escriban", "No entiendes un número que dijo un turista de ejemplo. ¿Qué puedes decirle?", ["En vez de adivinar, se le pide que lo escriba.", "«Could you write it down, please?» significa «¿Podría escribirlo, por favor?»."], "Could you write it down, please?"),
    ],
    mistakes=[("Responder «yes» a todo para no quedar mal.", "Si no entendiste, puedes dar una información falsa sobre una hora, un precio o una norma.", "Pide con amabilidad que repita o que lo escriba."),
              ("Hablar más fuerte cuando el turista no entiende.", "Subir la voz no ayuda a comprender y puede sonar molesto.", "Habla más despacio, con frases cortas y apoyos como un mapa o un papel.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿para qué se usa el inglés básico con los turistas?", "Para entenderse con frases cortas y claras en situaciones como el mostrador o un paseo", "Para hablar de forma perfecta, sin errores", "Para evitar hablar con turistas de otros países", "El inglés básico busca comunicar con claridad, no la perfección."),
        ("abc", "En Servicios de Turismo: ¿qué es un malentendido?", "Cuando una persona entiende algo distinto de lo que se quiso decir", "Cuando dos personas hablan al mismo tiempo", "Cuando un turista se despide", "Un malentendido es una diferencia entre lo dicho y lo entendido."),
        ("abc", "Si no entiendes lo que dice un turista, ¿qué conviene hacer?", "Pedirle con amabilidad que repita, por ejemplo «Could you repeat that, please?»", "Responder cualquier cosa para no quedar mal", "Ignorarlo y atender a otra persona", "Pedir que repita evita dar información falsa."),
        ("abc", "{F} ¿Qué significa «Where is the bus stop?»?", "¿Dónde está el paradero de buses?", "¿A qué hora sale el bus?", "¿Cuánto cuesta el pasaje?", "«Where is» pregunta por un lugar y «bus stop» es el paradero."),
        ("abc", "{F} La turista dice «I have a reservation for Saturday». ¿Qué quiere decir?", "Tengo una reserva para el sábado", "Quiero cancelar mi reserva del sábado", "Quiero hacer una reserva para el domingo", "«I have a reservation» significa tengo una reserva, y «Saturday» es sábado."),
        ("abc", "{F} ¿Qué significa «Sorry, I do not understand»?", "Perdón, no entiendo", "Perdón, llegué tarde", "Gracias, entiendo todo", "«I do not understand» significa no entiendo."),
        ("abc", "{F} Según las reglas de la agencia, ¿cómo se confirman las horas y los números?", "También por escrito, además de decirlos", "Solo en voz alta, rápido", "No se confirman, porque el turista ya sabe", "Escribirlos evita confusiones entre números parecidos."),
        ("ab", "Un turista dice «Good morning». ¿Cuál es una respuesta cortés?", "Good morning. How can I help you?", "Goodbye. See you tomorrow.", "«Good morning» es un saludo de la mañana; se responde con otro saludo y se ofrece ayuda."),
        ("abc", "{F} Un turista habla muy rápido y no lo entiendes. ¿Qué frase le dices?", "Could you speak more slowly, please?", "Thank you, goodbye.", "I am sorry, the museum is closed.", "La primera frase pide hablar más despacio; las otras no resuelven el problema."),
        ("abc", "{F} Una turista pregunta por una excursión de aventura y no sabes explicar en inglés las reglas de seguridad. ¿Qué corresponde?", "Derivar a un guía o coordinador autorizado que pueda explicarlas con claridad", "Inventar las reglas con las palabras que conoces", "Decirle que no hay reglas", "La seguridad se explica con precisión por quien está autorizado."),
        ("abc", "Un compañero se burla del acento de un turista. ¿Qué corresponde?", "Pedirle respeto, porque todas las personas merecen buen trato, hablen como hablen", "Reírse, si el turista no entiende español", "No decir nada, porque es una broma", "El respeto no depende del acento ni del nivel de inglés."),
        ("abc", "Un turista pregunta «Is breakfast included?» y no estás seguro del significado. ¿Qué haces?", "Pedir que repita o mostrar la ficha de la reserva para confirmar antes de responder", "Responder «yes» por si acaso", "Responder «no» por si acaso", "Adivinar puede dar información falsa; se confirma primero."),
        ("abc", "{F} Una turista, para reservar, dice que prefiere dar su correo y no su celular. ¿Qué corresponde?", "Aceptar el medio de contacto que ella prefiere, sin pedir datos que no hacen falta", "Insistir en que debe dar el celular", "Pedirle su número de pasaporte «por si acaso»", "Se piden solo los datos necesarios y se respeta el medio que ella elige."),
    ],
    ctx=("abc", "{F} Un turista dice «Sorry, I do not understand» después de que le explicaste una hora. ¿Qué corresponde?", "Repetir más despacio, con frases cortas, y escribir la hora para mostrársela", "Repetir lo mismo más fuerte", "Decirle que aprenda español", "Hablar despacio y apoyarse en lo escrito ayuda a comprender."),
    sc=[
        ("En Servicios de Turismo: ¿qué significa «Could you repeat that, please?»", "¿Podría repetirlo, por favor?", "Es una forma cortés de pedir que repitan."),
        ("¿Cómo se dice «Un momento, por favor» en inglés?", "One moment, please", "Es una forma cortés de pedir que esperen."),
        ("¿Qué haces si no entiendes una cifra?", "Pido que la escriba o la repita", "Adivinar puede producir un error en el precio."),
    ],
    op=("Escribe un mini diálogo de seis líneas, en inglés básico, entre una persona de la agencia y un turista que pregunta dónde está el paradero de buses. Usa al menos cuatro frases de la lección y agrega al lado la traducción al español de cada línea.",
        "Staff: Hello, welcome. How can I help you? (Hola, bienvenido. ¿En qué puedo ayudarle?). Tourist: Where is the bus stop? (¿Dónde está el paradero?). Staff: Sorry, one moment, please. (Perdón, un momento, por favor). Tourist: Thank you. (Gracias). Staff: You are welcome. (De nada). Tourist: Goodbye. (Adiós).",
        ["usa al menos cuatro frases de la lección", "las frases en inglés son correctas y cortas", "agrega la traducción de cada línea"],
        ["diálogo de seis líneas con traducción"],
        ["usar frases que no están en la lección sin revisarlas", "olvidar la traducción", "dejar sin respuesta cortés el agradecimiento"],
        "Pregunta: «¿qué frase usas si no entiendes?». Si no responde, repasa «Could you repeat that, please?»."),
    reinforce="Escribe en un papel cinco frases de la lección con su significado y léelas en voz alta despacio.",
    extend="Explica con un ejemplo inventado qué problema puede causar responder «yes» sin haber entendido.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Vocabulario de la agencia «Viajes Brisa». Lugares: hotel (hotel), museum (museo), beach (playa), bus stop (paradero de buses), bank (banco). Direcciones: left (izquierda), right (derecha), straight (recto). "
     "Números: thirteen (13), thirty (30), fifteen (15), fifty (50). Horas: nine o'clock (9:00), half past nine (9:30), quarter past nine (9:15), quarter to ten (9:45). "
     "Documentos: map (mapa), ticket (entrada), brochure (folleto), reservation (reserva). Roles: guide (guía), receptionist (recepcionista) y tourist (turista).")
build(
    O7, 2, F,
    use="Aprenderé vocabulario básico de turismo en inglés (lugares, direcciones, números, horas, documentos y roles) y cómo evitar confundir números parecidos como thirteen y thirty.",
    prior=["Sé las frases básicas de saludo y ayuda en inglés.", "Sé leer horas y minutos.", "Sé restar números enteros."],
    explain=[
        "El vocabulario básico de turismo incluye lugares (hotel, museum, beach, bus stop, bank), direcciones (left, right, straight) y documentos (map, ticket, brochure, reservation). Los roles son guide, que conduce a los turistas; receptionist, que atiende en el mostrador de la oficina; y tourist, la persona que viaja. Usar estas palabras con frases cortas permite orientar sin errores.",
        "Los números parecidos se confunden con facilidad. Los que terminan en -teen son del 13 al 19 (thirteen es 13, fifteen es 15) y los que terminan en -ty son decenas (thirty es 30, fifty es 50). Para no equivocarse, se escribe el número y se muestra. En las horas, «half past nine» es 9:30, «quarter past nine» es 9:15 y «quarter to ten» es 9:45.",
        "Pedidos típicos: «A map, please» (Un mapa, por favor) y «Two tickets, please» (Dos entradas, por favor). Se responde «Here you are» (Aquí tiene) y se confirma lo entregado.",
    ],
    vocab=[("museum", "museo"), ("bus stop", "paradero de buses"), ("brochure", "folleto"), ("ticket", "entrada"), ("left / right / straight", "izquierda / derecha / recto"), ("thirteen / thirty", "13 / 30"), ("half past nine", "nueve y media (9:30)"), ("quarter to ten", "diez menos cuarto (9:45)")],
    worked=[
        ("Decenas y -teen", "Un turista de ejemplo dice «fifteen». ¿Qué número es?", ["Termina en -teen, así que está entre 13 y 19.", "Fifteen es 15."], "15"),
        ("Leer una hora", "Un cartel de ejemplo dice «half past eight». ¿Qué hora es?", ["«Half past» significa y media, es decir, 30 minutos.", "Es 8:30."], "8:30"),
    ],
    mistakes=[("Entender «fifty» cuando el turista dijo «fifteen».", "Terminan distinto: -ty es una decena (50) y -teen es del 13 al 19 (15).", "Escucha el final de la palabra y confirma el número por escrito."),
              ("Entender «quarter to ten» como 10:15.", "«To» indica que falta un cuarto para las diez, o sea, 9:45.", "Recuerda: «to» antes de la hora y «past» después de la hora.")],
    T=[
        ("abc", "{F} ¿Qué significa «brochure»?", "Folleto", "Mapa", "Reserva", "«Brochure» es el folleto con información; el mapa es «map»."),
        ("abc", "{F} ¿Qué significa «bus stop»?", "Paradero de buses", "Playa", "Banco", "«Bus stop» es el lugar donde se detiene el bus."),
        ("abc", "{F} ¿Cuál de estas palabras indica una dirección?", "Straight", "Museum", "Ticket", "«Straight» significa recto, es decir, seguir derecho."),
        ("ab", "{F} ¿Qué número es «thirteen»?", "13", "30", "Termina en -teen: es del 13 al 19; thirty termina en -ty y es 30."),
        ("ab", "{F} ¿Qué número es «fifty»?", "50", "15", "Termina en -ty: es una decena; fifteen termina en -teen y es 15."),
        ("abc", "{F} «Half past nine» significa", "9:30", "9:15", "9:45", "«Half past» significa y media, por lo tanto es 9:30."),
        ("abc", "{F} «Quarter to ten» significa", "9:45", "10:15", "9:15", "«Quarter to ten» es un cuarto antes de las diez, o sea, 9:45."),
        ("=", "{F} ¿Cuántos minutos hay entre «half past nine» y «quarter to ten»?", "(9*60+45)-(9*60+30)", "Se restan las dos horas pasadas a minutos.", " minutos"),
        ("=", "{F} Un turista dice «fifteen thousand pesos» y entiendes «fifty thousand pesos». ¿Cuántos pesos de diferencia hay entre ambas cifras?", "50000-15000", "Se resta la cifra menor a la mayor.", ""),
        ("abc", "{F} Para no confundir fifteen y fifty, ¿qué haces?", "Pedir que lo escriba, o escribirlo y mostrárselo para confirmar", "Elegir una de las dos al azar", "Decir «yes» a todo", "Confirmar por escrito evita errores entre números parecidos."),
        ("abc", "{F} ¿Qué rol cumple la persona que recibe a los visitantes en el mostrador de la oficina?", "Receptionist", "Tourist", "Guide", "El receptionist atiende en el mostrador; el guide conduce el recorrido."),
        ("abc", "{F} Un turista dice «A map and two tickets, please». ¿Qué le entregas?", "Un mapa y dos entradas", "Un folleto y dos reservas", "Un mapa y dos folletos", "«Map» es mapa y «tickets» son entradas."),
        ("abc", "{F} Un turista pregunta dónde está el banco y respondes «straight and then left». ¿Qué indicación diste?", "Seguir recto y luego doblar a la izquierda", "Doblar a la derecha y luego seguir recto", "Quedarse en el mismo lugar", "«Straight» es recto y «left» es izquierda."),
    ],
    ctx=("abc", "{F} Un turista dice «The tour starts at quarter past nine» y tú anotas 9:45. ¿Qué haces?", "Corregir la hora a 9:15 y confirmarla con el turista por escrito", "Dejar 9:45, porque el cuarto es siempre antes", "Preguntar el precio en lugar de la hora", "«Quarter past nine» es 9:15; se corrige y se confirma para evitar que llegue tarde o temprano."),
    sc=[
        ("En Servicios de Turismo: ¿qué significa «ticket»?", "Entrada", "Es el documento para entrar a un lugar o actividad."),
        ("¿Cómo distingues thirteen de thirty?", "Por el final: -teen o -ty", "El final -teen indica del 13 al 19."),
        ("¿Qué hora es «half past nine»?", "9:30", "«Half past» significa y media, es decir, 30 minutos."),
    ],
    op=("Prepara una tarjeta de vocabulario para tu mostrador con ocho palabras o frases de la ficha (dos lugares, dos direcciones, dos documentos y dos horas), escribe cada una en inglés con su significado en español y agrega una frase corta en inglés usando dos de ellas.",
        "Lugares: museum (museo), bank (banco). Direcciones: left (izquierda), straight (recto). Documentos: map (mapa), ticket (entrada). Horas: half past nine (9:30), quarter to ten (9:45). Frase: «The bank is on the left».",
        ["incluye las ocho palabras con su significado", "las traducciones son correctas", "la frase en inglés es breve y correcta"],
        ["tarjeta de vocabulario con una frase"],
        ["confundir quarter past con quarter to", "traducir mal una dirección", "escribir una frase demasiado larga"],
        "Pregunta: «¿cómo dices 9:45 en inglés?». Si no responde, repasa «quarter to ten»."),
    reinforce="Escribe tres números del 13 al 19 y tres decenas en inglés, y léelos en voz alta.",
    extend="Explica con un ejemplo inventado por qué confundir quarter past y quarter to puede afectar a un turista.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (de ejemplo, inventada). Diálogo escrito en el mostrador. Tourist: Good morning. What time does the museum open? "
     "Staff: Good morning. It opens at nine o'clock in the morning and closes at five o'clock in the afternoon. "
     "Tourist: How much is the ticket? Staff: It costs three thousand pesos for adults. Students pay one thousand five hundred pesos. "
     "Tourist: Do you have a map? Staff: Yes, here is the map. The museum is on the right, next to the bank. Tourist: Thank you.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un diálogo escrito en inglés básico: encontrar horas, precios y direcciones, detectar errores de gramática simples y reaccionar cuando falta información.",
    prior=["Sé el vocabulario básico de turismo en inglés.", "Sé leer horas y números.", "Sé multiplicar y sumar con números enteros."],
    explain=[
        "Analizar un diálogo es leerlo completo y extraer los datos: qué se pregunta, qué se responde, y qué falta. En el diálogo de la ficha hay una hora de apertura y de cierre, un precio para adultos y otro para estudiantes, y una dirección. Para decir la hora se usa «at»: «at nine o'clock». Para decir de la mañana o de la tarde se usa «in the morning» y «in the afternoon».",
        "En frases como «The museum opens at nine», el verbo lleva -s con «it» o con un solo sujeto: «opens», «closes», «costs». Es un error común escribir «close» cuando se habla de un solo lugar. Si no tienes un dato, se dice con cortesía «I am sorry, I will check» (Lo siento, voy a averiguar) y se consulta antes de responder.",
        "También se cuida la privacidad: para vender una entrada no hace falta pedir el pasaporte ni otros datos personales. Y se confirma lo importante por escrito, como los precios.",
    ],
    vocab=[("opens / closes", "abre / cierra"), ("it costs", "cuesta"), ("in the morning / in the afternoon", "de la mañana / de la tarde"), ("next to", "junto a"), ("Here is the map", "Aquí está el mapa"), ("I am sorry, I will check", "Lo siento, voy a averiguar"), ("It starts / it lasts", "empieza / dura"), ("Is the museum open on Sunday?", "¿Está abierto el museo el domingo?"), ("You are welcome", "De nada")],
    worked=[
        ("Extraer un precio", "En un diálogo de ejemplo se dice «The ticket costs two thousand pesos». ¿Cuánto cuesta la entrada?", ["El verbo «costs» indica el precio de algo.", "«Two thousand» es dos mil."], "$2.000"),
        ("Corregir un verbo", "Un compañero escribe «The shop close at six». ¿Qué corrección necesita?", ["El sujeto es singular («the shop»).", "El verbo debe llevar -s: «closes»."], "The shop closes at six."),
    ],
    mistakes=[("Escribir «The museum open at nine».", "Con un solo lugar el verbo lleva -s: «opens».", "Escribe «The museum opens at nine»."),
              ("Responder «yes» a una pregunta cuyo dato no tienes.", "Se puede dar una información falsa y perjudicar al turista.", "Di «I am sorry, I will check» y averigua.")],
    T=[
        ("abc", "{F} ¿A qué hora abre el museo, según el diálogo?", "A las 9:00 de la mañana", "A las 5:00 de la tarde", "A las 9:30 de la mañana", "«Nine o'clock in the morning» es las 9:00 de la mañana."),
        ("abc", "{F} ¿A qué hora cierra el museo, según el diálogo?", "A las 17:00", "A las 15:00", "A las 9:00", "«Five o'clock in the afternoon» es las 17:00."),
        ("=", "{F} ¿Cuántas horas está abierto el museo?", "17-9", "Se resta la hora de apertura a la de cierre.", " horas"),
        ("abc", "{F} ¿Cuál es el precio de la entrada de adulto?", "$3.000", "$1.500", "$30.000", "«Three thousand pesos» son 3.000 pesos."),
        ("=", "{F} Llegan 2 adultos y 3 estudiantes. ¿Cuántos pesos pagan en total?", "2*3000+3*1500", "Se suma el costo de los adultos y el de los estudiantes.", ""),
        ("abc", "{F} ¿Dónde está el museo, según el personal?", "A la derecha, junto al banco", "A la izquierda, junto al hotel", "Recto, junto a la playa", "«On the right, next to the bank» significa a la derecha, junto al banco."),
        ("abc", "{F} ¿Qué significa «Do you have a map?»?", "¿Tiene un mapa?", "¿Dónde está el mapa?", "¿Cuánto cuesta el mapa?", "«Do you have» pregunta si la persona tiene algo."),
        ("abc", "{F} El turista dice «Thank you». ¿Qué le respondes?", "You are welcome.", "Good morning.", "I am sorry.", "«You are welcome» es la respuesta cortés a un agradecimiento."),
        ("abc", "{F} Para estar seguro del precio, el personal escribe «3.000» en un papel y se lo muestra. ¿Qué técnica usa?", "Confirmar el número por escrito", "Subir la voz", "Cambiar de tema", "El papel evita confundir números parecidos."),
        ("abc", "{F} El personal le pide al turista su número de pasaporte «para vender la entrada». ¿Qué corresponde?", "No pedirlo: es un dato innecesario para vender una entrada", "Pedirlo, porque toda venta lo exige", "Pedirlo y anotarlo en un papel suelto", "Se piden solo los datos necesarios para el servicio."),
        ("ab", "{F} ¿Cuál frase significa «Aquí está el mapa»?", "Here is the map.", "Where is the map?", "«Here is» indica entregar algo; «where is» pregunta por un lugar."),
        ("abc", "{F} El turista pregunta «Is the museum open on Sunday?» y el diálogo no dice los días. ¿Qué corresponde?", "Decir «I am sorry, I will check» y consultar al museo antes de responder", "Responder «yes» para quedar bien", "Responder «no» para evitar problemas", "Sin el dato, se averigua y no se adivina."),
        ("abc", "{F} Un compañero escribe «The museum opens at nine and close at five». ¿Qué corrección necesita?", "Cambiar «close» por «closes»", "Cambiar «opens» por «open»", "Cambiar «at five» por «in five»", "Con «the museum» el verbo lleva -s en las dos acciones."),
    ],
    ctx=("abc", "{F} Una turista sorda llega al mostrador y muestra su teléfono con la pregunta escrita «How much is the ticket?». ¿Qué corresponde?", "Responder por escrito el precio «3.000 pesos for adults» y preguntarle si necesita algo más", "Hablarle muy fuerte", "Pedirle que vuelva con un acompañante", "Se usa el medio que la persona eligió; responder por escrito respeta su autonomía."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se dice «cuesta tres mil pesos» en inglés?", "It costs three thousand pesos", "El verbo «costs» indica el precio de algo."),
        ("¿Cómo se corrige «The tour start at ten»?", "The tour starts at ten", "Con un solo sujeto el verbo lleva -s."),
        ("¿Qué dices si no tienes un dato?", "I am sorry, I will check", "Averiguar evita dar información falsa al turista."),
    ],
    op=("Lee este diálogo de ejemplo: Tourist: What time does the tour start? Staff: It starts at half past ten. Tourist: How long is it? Staff: It lasts two hours. Tourist: How much is it? Staff: It costs eight thousand pesos per person. Escribe en español los tres datos (hora, duración, precio), calcula cuánto pagan 3 personas y escribe en inglés una respuesta corta para decir que el punto de encuentro está junto a la fuente (next to the fountain).",
        "Hora de inicio: 10:30. Duración: 2 horas. Precio: 8.000 pesos por persona. Para 3 personas: 3 × 8.000 = 24.000 pesos. Respuesta: «We meet next to the fountain».",
        ["extrae bien los tres datos del diálogo", "calcula correctamente el total", "la frase en inglés es corta y correcta"],
        ["datos, cálculo y frase en inglés"],
        ["confundir half past ten con 10:15", "olvidar multiplicar por las personas", "escribir una frase con errores de verbo"],
        "Pregunta: «¿cómo dices que cuesta ocho mil pesos?». Si no responde, repasa «it costs»."),
    reinforce="Escribe un diálogo de cuatro líneas, en inglés, para preguntar el horario de una tienda.",
    extend="Explica con un ejemplo inventado por qué se confirma un precio por escrito.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (de ejemplo, inventada). Tour «City Walk» (paseo por el centro): sale a las 10:30 desde un punto de encuentro junto a la fuente; dura 2 horas; cuesta $8.000 por persona; hoy asiste un grupo de 4 personas. "
     "El punto de encuentro queda a 5 minutos caminando de la estación de buses. Frases útiles: «The tour starts at half past ten», «It lasts two hours», «It costs eight thousand pesos per person», «We meet next to the fountain».")
build(
    O7, 4, F,
    use="Aprenderé a responder en inglés básico a un turista usando los datos de una ficha: hora, duración, precio, lugar de encuentro y distancia, con cortesía y sin inventar.",
    prior=["Sé el vocabulario básico y las horas en inglés.", "Sé analizar un diálogo escrito.", "Sé multiplicar y sumar con números enteros."],
    explain=[
        "Para responder a un turista se usan los datos de la ficha y frases cortas y correctas. Hora: «The tour starts at half past ten». Duración: «It lasts two hours». Precio: «It costs eight thousand pesos per person». Lugar: «We meet next to the fountain». La distancia se puede decir como «It is five minutes from the bus station on foot». Se responde primero y después se agrega un dato.",
        "Cuando falta un dato, no se inventa. Si un turista pregunta por la seguridad de los niños o por la accesibilidad, y la ficha no lo dice, se responde con cortesía «I am sorry, I will check with the coordinator and tell you» y se consulta. Para despedirse se dice «Thank you. Have a nice day».",
        "Los avisos de seguridad no se traducen sin revisar con quien sabe inglés; un error puede confundir. Y se trata a todas las personas con el mismo respeto, preguntando qué apoyo necesitan.",
    ],
    vocab=[("The tour starts at...", "El paseo empieza a las..."), ("It lasts two hours", "Dura dos horas"), ("It costs ... per person", "Cuesta ... por persona"), ("We meet next to...", "Nos reunimos junto a..."), ("on foot", "a pie"), ("Is it far?", "¿Queda lejos?"), ("thirty-two thousand", "treinta y dos mil"), ("Have a nice day", "Que tenga un buen día")],
    worked=[
        ("Armar una respuesta", "Un turista de ejemplo pregunta «How long is the walk?». La ficha dice que dura 90 minutos. ¿Qué respondes en inglés simple?", ["Se informa la duración.", "«It lasts ninety minutes»."], "It lasts ninety minutes."),
        ("Cuando falta el dato", "Un turista de ejemplo pregunta «Is there a bathroom?» y la ficha no dice nada. ¿Qué respondes?", ["No se inventa.", "«I am sorry, I will check and tell you»."], "I am sorry, I will check and tell you."),
    ],
    mistakes=[("Responder «yes, of course» sobre la accesibilidad sin revisar.", "Si no es cierto, la persona llega y no puede participar.", "Di que vas a averiguar y consulta al coordinador."),
              ("Traducir un aviso de seguridad con una aplicación y entregarlo sin revisar.", "Un error de traducción puede confundir en un tema importante.", "Revísalo con alguien que sepa inglés o con el coordinador.")],
    T=[
        ("abc", "{F} ¿Qué frase informa correctamente la hora de salida?", "The tour starts at half past ten.", "The tour starts at quarter past ten.", "The tour starts at half past nine.", "«Half past ten» es las 10:30."),
        ("abc", "{F} ¿Qué frase informa el lugar de encuentro?", "We meet next to the fountain.", "We meet next to the museum.", "We meet at the bank.", "La ficha dice que el punto de encuentro está junto a la fuente."),
        ("abc", "{F} ¿Qué frase informa la duración?", "It lasts two hours.", "It lasts two days.", "It starts two hours.", "«Lasts» indica cuánto dura, y la ficha dice 2 horas."),
        ("=", "{F} ¿Cuántos minutos después de las 10:00 termina el tour?", "30+2*60", "Se suman los 30 minutos de la salida y las 2 horas pasadas a minutos.", " minutos"),
        ("=", "{F} ¿Cuántos pesos pagan en total las 4 personas del grupo?", "4*8000", "Se multiplica el precio por persona por 4.", ""),
        ("abc", "{F} Un turista pregunta «How much is it for four people?». ¿Qué respuesta es correcta?", "It is thirty-two thousand pesos in total.", "It is eight thousand pesos in total.", "It is twenty thousand pesos in total.", "4 × 8.000 = 32.000, o sea, thirty-two thousand."),
        ("ab", "¿Cuál es la frase más cortés para pedir que alguien espere?", "One moment, please.", "Wait.", "«Please» y el tono amable muestran respeto; una orden seca no."),
        ("abc", "{F} Un turista pregunta «Is it far?» desde la estación. ¿Qué respuesta es correcta?", "It is five minutes from the bus station on foot.", "Yes, it is very far.", "I do not know.", "La ficha dice que queda a 5 minutos a pie de la estación."),
        ("=", "{F} Si 6 personas más se unen al grupo, ¿cuántos pesos pagan en total las 10 personas?", "10*8000", "Se multiplica el precio por persona por 10.", ""),
        ("abc", "{F} Un turista pregunta «Is the tour safe for children?» y la ficha no dice edades. ¿Qué corresponde?", "Decir en inglés que consultarás con el coordinador y no asegurar nada", "Responder «Yes, very safe»", "Responder «No children allowed»", "Sin el dato no se asegura ni se niega; se consulta."),
        ("abc", "{F} Al despedirse, el turista dice «Thank you, goodbye». ¿Qué respondes?", "You are welcome. Have a nice day.", "Please wait here.", "Where is the bus stop?", "Es una despedida cortés; las otras frases no corresponden."),
        ("abc", "{F} Un compañero propone traducir el aviso de seguridad con una aplicación y entregarlo sin revisar. ¿Qué corresponde?", "Revisarlo con alguien que sepa inglés o con el coordinador, porque un error podría confundir", "Entregarlo, porque la aplicación nunca se equivoca", "No entregar ningún aviso", "Un error de traducción en seguridad podría causar confusión."),
        ("abc", "{F} Un turista que usa silla de ruedas pregunta «Is the tour accessible?». ¿Qué respondes?", "I am sorry, I will check with the coordinator and tell you.", "Yes, of course.", "No, the tour is not for you.", "No se asume nada: se consulta y se responde con respeto."),
    ],
    ctx=("abc", "{F} Una turista se acerca y dice «Hello! I want information about the tour». ¿Qué respondes?", "Hello, welcome. The tour starts at half past ten. We meet next to the fountain.", "Goodbye. Come tomorrow.", "I do not know, ask someone else.", "Un saludo y los datos clave de la ficha responden a su pedido con cortesía."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se dice «Cuesta ocho mil pesos por persona»?", "It costs eight thousand pesos per person", "«Per person» significa que el precio es por cada persona."),
        ("¿Qué haces si falta un dato en la ficha?", "Digo «I am sorry, I will check» y consulto", "Los datos que faltan no se inventan nunca."),
        ("¿Cómo dices «Que tenga un buen día»?", "Have a nice day", "Es una despedida cortés y amable para el turista."),
    ],
    op=("Escribe una respuesta de tres frases en inglés básico para una turista que pregunta por el tour «City Walk» de la ficha: hora, duración y lugar de encuentro. Agrega una frase de cortesía al final, la traducción al español de cada frase, y calcula cuánto pagan 5 personas.",
        "The tour starts at half past ten (El paseo empieza a las 10:30). It lasts two hours (Dura dos horas). We meet next to the fountain (Nos reunimos junto a la fuente). Have a nice day (Que tenga un buen día). Cinco personas pagan 5 × 8.000 = 40.000 pesos.",
        ["usa las frases correctas con los datos de la ficha", "agrega una frase de cortesía y la traducción de cada frase", "calcula bien el total de 5 personas"],
        ["tres frases, cortesía, traducciones y cálculo"],
        ["decir half past nine en vez de ten", "olvidar la cortesía", "inventar un dato que no está en la ficha"],
        "Pregunta: «¿qué haces si la turista pregunta por la accesibilidad?». Si no responde, repasa la frase de averiguar."),
    reinforce="Escribe en inglés dos frases con la hora, el precio y el lugar de encuentro de una actividad que conozcas.",
    extend="Explica con un ejemplo inventado por qué es mejor decir «I will check» que adivinar una respuesta.",
)

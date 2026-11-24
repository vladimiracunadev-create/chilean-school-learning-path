"""Inglés EPJA Nivel 2, módulo 4 (parte 2): OAD-14, expresarse sobre actividades relajantes y crear una actividad inusual y relajante. Los guiones de escucha están escritos."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-14"

F1 = ("Text (example): After work, Marta relaxes in different ways. On Mondays she reads a book. On Wednesdays she walks in the park. "
      "On Fridays she listens to music and cooks soup. Her husband, Hugo, works in the garden every Saturday. He doesn't read books; he listens to the radio.")

F2 = (GUION + "«Hello, my name is Rosa. I'm 58 years old. In the evening I relax. I drink tea and I listen to music. "
      "On Saturdays I cook with my sister, and on Sundays I walk in the quiet park near my house. I don't watch TV at night. I think a calm evening is good for me.»")

F3 = ("Steps for a relaxing evening (example). 1. Boil water. 2. Put a tea bag in a cup. 3. Wait three minutes. 4. Sit near a window. 5. Drink slowly. 6. Don't use your phone.")

F4 = (GUION + "Dialogue (example). «Mr. Perez: Hello, Lucía. Do you relax after work? Lucía: Yes, I do. I walk in the park and I listen to music. "
      "Mr. Perez: Does your brother walk with you? Lucía: No, he doesn't. He works in the garden. Mr. Perez: Nice. I read a book every night. Lucía: That's a good habit!»")

F5 = ("Poster at a community center (example): RELAXING HOUR. Every Thursday, 6:00 p.m., in the garden of the center. Come and relax with us! Listen to music. Drink tea. "
      "Walk slowly in the garden. Don't bring your phone. Bring a chair or a blanket. It's free for neighbors. Ask Mrs. Díaz at the front desk.")

F6 = ("Model text (example), an unusual relaxing activity: Rain Listening. Find a quiet place near a window. Sit down. Close your eyes. Listen to the rain for five minutes. "
      "Breathe slowly. Don't use your phone. Rain Listening is relaxing because it is quiet and calm. Mr. Soto, 63, does it every rainy afternoon.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que hago para descansar después del trabajo y leo un texto sobre actividades relajantes.",
    prior=["Digo mis hábitos con el presente simple.", "Sé usar la «-s» con he y she.", "Sé que descansar es parte de una vida saludable."],
    explain=[
        "Una actividad relajante es algo que haces para descansar y sentirte tranquilo o tranquila: leer, caminar, escuchar música, cocinar o trabajar en el jardín. Cada persona descansa a su manera, y todas las formas valen.",
        "Para contar lo que haces usa el presente simple, igual que con los hábitos: I read a book. Con he, she e it el verbo lleva «-s»: She reads a book. Para negar usa don't o doesn't: He doesn't read books.",
        "Los días de la semana con «on» dicen cuándo: on Mondays, «los lunes». Al leer, subraya el día, la persona y la actividad. Con esas tres cosas entiendes de qué trata el texto.",
    ],
    vocab=[("relax", "relajarse, descansar"), ("read", "leer"), ("walk", "caminar"), ("listen to music", "escuchar música"), ("garden", "jardín; hacer jardinería"), ("cook", "cocinar")],
    worked=[
        ("Decir una actividad con el día", "Marta lee un libro los lunes.", ["Sujeto: Marta, que es she.", "Verbo con «-s»: reads.", "Agrego on Mondays."], "Marta reads a book on Mondays."),
        ("Negar una actividad", "Hugo no lee libros.", ["Con he uso doesn't.", "El verbo queda sin «-s»: read."], "Hugo doesn't read books."),
    ],
    mistakes=[("Escribir «Marta listen to music on Fridays».", "Con she el presente simple lleva «-s»: listens.", "Revisa el sujeto antes de escribir el verbo."),
              ("Escribir «Hugo doesn't reads books».", "Después de doesn't el verbo queda sin «-s».", "Escribe doesn't read.")],
    T=[
        ("abc", "{F} Which activity does Marta do on Wednesdays?", "She walks in the park", "She reads a book", "She cooks soup", "El texto dice que los miércoles camina en el parque."),
        ("ab", "{F} What does Marta do on Mondays?", "She reads a book", "She works in the garden", "El texto dice «On Mondays she reads a book»."),
        ("{F} How many things does Marta do on Fridays? Write the number.", "2", "Los viernes ella escucha música y cocina sopa."),
        ("abc", "{F} Who works in the garden?", "Hugo", "Marta", "Both Marta and Hugo", "El texto dice que su esposo Hugo trabaja en el jardín."),
        ("ab", "{F} When does Hugo work in the garden?", "Every Saturday", "Every Monday", "El texto dice que Hugo trabaja en el jardín every Saturday."),
        ("abc", "{F} Which sentence is true?", "Hugo doesn't read books", "Hugo reads books every day", "Hugo cooks soup on Fridays", "El texto dice que Hugo no lee libros y escucha la radio."),
        ("abc", "Complete: Marta ___ a book on Mondays.", "reads", "read", "reading", "Con Marta (she) el verbo lleva «-s»."),
        ("abc", "Complete: Hugo ___ in the garden every Saturday.", "works", "work", "working", "Con Hugo (he) el verbo lleva «-s»."),
        ("abc", "Complete: I ___ to music after work.", "listen", "listens", "listening", "Con I el verbo no lleva «-s»."),
        ("Complete with one verb: She ___ soup on Fridays. (cocinar)", "cooks", "Con she el verbo cook lleva «-s»."),
        ("abc", "What does «relax» mean?", "Relajarse", "Trabajar", "Comprar", "Relax significa descansar y sentirse tranquilo."),
        ("ab", "Choose the correct sentence.", "Hugo doesn't read books", "Hugo doesn't reads books", "Después de doesn't el verbo queda sin «-s»."),
        ("abc", "Put the words in order: walks / in the park / Marta / on Wednesdays", "Marta walks in the park on Wednesdays", "Marta walk in the park on Wednesdays", "Walks Marta in the park on Wednesdays", "El orden es sujeto, verbo, lugar y día."),
    ],
    ctx=("abc", "En la hora de almuerzo, una compañera te pregunta cómo descansas. Quieres decir que los domingos caminas en el parque. ¿Qué dices?", "I walk in the park on Sundays", "I walks in the park on Sundays", "I am walk in the park on Sundays", "Con I el verbo no lleva «-s» ni am."),
    sc=[("En Inglés: ¿cómo se dice «escuchar música»?", "Listen to music", "Con el verbo listen se usa la palabra to antes de music."),
        ("En Inglés: ¿qué significa «on Fridays»?", "Los viernes", "On Fridays indica el día en que ocurre algo."),
        ("En Inglés: ¿cómo niegas «He reads books»?", "He doesn't read books", "Doesn't marca la negación y el verbo queda sin «-s».")],
    op=("Escribe en tu cuaderno cuatro oraciones sobre cómo descansas tú o una persona inventada. Usa un día de la semana y una actividad distinta en cada oración.",
        "I walk in the park on Sundays. I listen to music on Fridays. My friend Ana reads a book on Mondays. She doesn't cook on Tuesdays.",
        ["usa cuatro actividades distintas", "usa on con un día", "agrega la «-s» con he o she"],
        ["cuatro oraciones escritas"],
        ["olvidar la «-s» con he o she", "poner datos personales reales"],
        "Pregunta: «¿Qué actividad de descanso me gustaría hacer más?»."),
    reinforce="Di en voz alta tres actividades con las que descansas.",
    extend="Escribe una semana de descanso de una persona inventada, con una actividad por día.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy escucho un texto corto sobre las tardes de Rosa, reconozco el tema y aprendo palabras para hablar de descansar.",
    prior=["Sé decir actividades de descanso.", "Entiendo oraciones con I y con she.", "Puedo escuchar un texto y sacar la idea principal."],
    explain=[
        "Escuchar es entender la idea principal y las palabras clave. Antes de escuchar, mira el título y haz una predicción: ¿de qué trata? Mientras escuchas, anota números, nombres y verbos.",
        "El texto de hoy lo lee otra persona en voz alta, o lo lees tú en voz baja y despacio. Es un guion escrito; no necesitas audio. Las palabras nuevas son quiet, calm, evening y relax.",
        "Quiet significa tranquilo o silencioso. Calm es calmado. Evening es el final de la tarde y el comienzo de la noche. Relax es relajarse. Después de escuchar, responde: ¿quién habla?, ¿de qué habla?, ¿qué hace y cuándo lo hace?",
    ],
    vocab=[("evening", "tarde-noche, atardecer"), ("relax", "relajarse"), ("quiet", "tranquilo, silencioso"), ("calm", "calmado"), ("tea", "té"), ("near", "cerca de")],
    worked=[
        ("Sacar la idea principal", "Escuchas que Rosa toma té, escucha música, cocina y camina por el parque.", ["Todas son actividades que ella hace para descansar.", "El tema común es relajarse en la tarde y los fines de semana."], "El texto trata de cómo Rosa se relaja"),
        ("Buscar un dato", "¿Qué hace Rosa los domingos?", ["Busco Sundays en el guion.", "Leo la oración: walk in the quiet park."], "Camina en el parque tranquilo"),
    ],
    mistakes=[("Responder con lo que supones y no con lo que dice el guion.", "La respuesta debe estar en el texto.", "Vuelve a leer y busca la palabra clave."),
              ("Confundir quiet con quit o con cuiet.", "Quiet significa tranquilo; se escribe q-u-i-e-t.", "Fíjate en las letras de la palabra y en su contexto.")],
    T=[
        ("{F} How old is Rosa? Write the number.", "58", "El guion dice «I'm 58 years old»."),
        ("abc", "{F} What does Rosa drink in the evening?", "Tea", "Coffee", "Juice", "El guion dice «I drink tea»."),
        ("ab", "{F} What does Rosa do on Sundays?", "She walks in the quiet park", "She cooks with her sister", "Los domingos camina; los sábados cocina con su hermana."),
        ("abc", "{F} Who does Rosa cook with on Saturdays?", "Her sister", "Her mother", "Her neighbor", "El guion dice «I cook with my sister»."),
        ("ab", "{F} Which sentence is true?", "Rosa doesn't watch TV at night", "Rosa watches TV every night", "Ella dice «I don't watch TV at night»."),
        ("abc", "What does «quiet» mean?", "Tranquilo, silencioso", "Muy rápido", "Muy grande", "Quiet describe un lugar sin ruido."),
        ("abc", "What does «evening» mean?", "Atardecer o tarde-noche", "Mañana temprano", "Mediodía", "Evening es el final de la tarde y el comienzo de la noche."),
        ("abc", "What does «calm» mean?", "Calmado", "Cansado", "Caliente", "Calm describe algo tranquilo y sin tensión."),
        ("abc", "{F} What is the main idea of the text?", "How Rosa relaxes in the evening and on weekends", "How to get a job interview", "How to go to the bank", "Rosa cuenta sus actividades para descansar."),
        ("ab", "{F} The text is about...", "relaxing activities", "a work schedule", "Rosa habla de tomar té, escuchar música y caminar."),
        ("abc", "Complete: Rosa ___ in the evening.", "relaxes", "relax", "relaxing", "Con Rosa (she) el verbo lleva «-s»."),
        ("ab", "Choose the correct sentence.", "I listen to music in the evening", "I listen music in the evening", "Con listen se necesita to antes de music."),
        ("abc", "Which place is relaxing in the text?", "The quiet park", "The busy street", "The warehouse", "El texto llama al parque quiet, tranquilo."),
    ],
    ctx=("abc", "Una compañera de trabajo te pregunta qué haces en las tardes. Quieres decir que bebes té y escuchas música. ¿Qué respondes?", "I drink tea and I listen to music", "I drinks tea and I listens music", "I am drink tea and listen music", "Con I el verbo queda sin «-s» y listen necesita to."),
    sc=[("En Inglés: ¿qué haces antes de escuchar un texto?", "Mirar el título y predecir el tema", "Predecir ayuda a entender lo que escuchas."),
        ("En Inglés: ¿qué significa «quiet»?", "Tranquilo, silencioso", "Quiet describe algo sin ruido ni tensión."),
        ("En Inglés: ¿qué significa «evening»?", "Atardecer o tarde-noche", "Evening es la parte final de la tarde.")],
    op=("Pide a otra persona que lea en voz alta este guion y escribe tres datos que entiendas: {F} Después escribe dos oraciones sobre cómo tú te relajas en la tarde.",
        "Datos: Rosa is 58. She drinks tea. She walks in the park on Sundays. Mis oraciones: I drink tea in the evening. I listen to music.",
        ["escribe tres datos correctos del guion", "escribe dos oraciones propias", "usa un verbo con I"],
        ["tres datos y dos oraciones escritas"],
        ["responder con datos que no están en el guion", "olvidar to después de listen"],
        "Pregunta: «¿Qué palabra clave me ayudó a entender el texto?»."),
    reinforce="Lee el guion en voz baja y subraya las palabras que ya conocías.",
    extend="Escribe cinco preguntas sobre el guion para hacerle a otra persona.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a dar instrucciones cortas para una actividad relajante con el imperativo.",
    prior=["Sé decir actividades relajantes.", "Reconozco los verbos en presente simple.", "He seguido instrucciones escritas, como una receta."],
    explain=[
        "Para dar una instrucción en inglés usamos el verbo solo, en su forma básica: Sit down. Wait three minutes. Es la expresión del imperativo, y no lleva sujeto ni «-s». Para decir lo que no se debe hacer, usa Don't + verbo: Don't use your phone.",
        "Paso 1: escribe el verbo, por ejemplo boil, put, wait, sit o drink. Paso 2: agrega el objeto o el lugar: boil water, sit near a window. Paso 3: agrega cómo, como slowly. Si quieres ser amable, puedes empezar con Please.",
        "Los pasos de una actividad se numeran. En un texto de instrucciones busca primero los verbos al comienzo de cada línea: ellos te dicen qué hacer, en qué orden y qué evitar.",
    ],
    vocab=[("boil", "hervir"), ("wait", "esperar"), ("sit", "sentarse"), ("slowly", "despacio"), ("cup", "taza"), ("take a deep breath", "respirar profundo")],
    worked=[
        ("Dar una instrucción", "Quieres decir a alguien que se siente cerca de la ventana.", ["Verbo en forma básica: sit.", "Agrego el lugar: near a window."], "Sit near a window."),
        ("Decir lo que no se hace", "Quieres decir que no use el teléfono.", ["Empiezo con Don't.", "Agrego el verbo sin «-s»: use.", "Agrego your phone."], "Don't use your phone."),
    ],
    mistakes=[("Escribir «Sits near a window» como instrucción.", "La instrucción usa el verbo básico, sin «-s» ni sujeto.", "Escribe Sit near a window."),
              ("Escribir «Doesn't use your phone».", "En instrucciones se usa Don't, no doesn't.", "Escribe Don't + verbo.")],
    T=[
        ("{F} How many minutes do you wait? Write the number.", "3", "El paso 3 dice «Wait three minutes»."),
        ("abc", "{F} What do you put in the cup?", "A tea bag", "Coffee", "Sugar", "El paso 2 dice «Put a tea bag in a cup»."),
        ("ab", "{F} What is the last instruction?", "Don't use your phone", "Drink slowly", "El paso 6 dice «Don't use your phone»."),
        ("abc", "{F} Which step comes after «Wait three minutes»?", "Sit near a window", "Boil water", "Drink slowly", "El paso 4 viene después del paso 3."),
        ("ab", "{F} Where do you sit?", "Near a window", "In the kitchen", "El paso 4 dice «Sit near a window»."),
        ("abc", "Which sentence is an instruction?", "Sit near a window", "She sits near a window", "She is sitting near a window", "La instrucción usa el verbo básico y no tiene sujeto."),
        ("abc", "Complete: ___ use your phone while you drink tea.", "Don't", "Doesn't", "Not", "Para prohibir se usa Don't antes del verbo."),
        ("abc", "Complete: ___ three minutes.", "Wait", "Waits", "Waiting", "La instrucción usa el verbo básico."),
        ("ab", "What do you say to a friend to tell him how to drink tea?", "Drink slowly", "Drinks slowly", "La instrucción no lleva «-s» al final del verbo."),
        ("abc", "Put the words in order: tea / Drink / slowly", "Drink tea slowly", "Tea drink slowly", "Slowly tea drink", "El orden es verbo, objeto y modo."),
        ("ab", "What does «slowly» mean?", "Despacio", "Rápido", "Slowly describe cómo se hace algo con calma."),
        ("abc", "Which sentence is an instruction to relax?", "Close your eyes and take a deep breath", "Rosa closes her eyes", "We are closing the door", "Solo la primera da una orden al lector."),
        ("ab", "Spot the error and choose the correct sentence: «Don't uses your phone.»", "Don't use your phone", "Doesn't use your phone", "Después de Don't el verbo queda sin «-s»."),
    ],
    ctx=("abc", "Una vecina te pide que le expliques cómo preparar un té tranquilo. Quieres decirle el primer paso. ¿Qué le dices?", "Boil water", "Boils water", "You boiling water", "La instrucción usa el verbo en forma básica."),
    sc=[("En Inglés: ¿cómo se forma una instrucción?", "Con el verbo en forma básica", "El imperativo usa el verbo básico, sin sujeto."),
        ("En Inglés: ¿cómo prohíbes algo en una instrucción?", "Don't + verbo", "Don't indica lo que no se debe hacer."),
        ("En Inglés: ¿qué significa «slowly»?", "Despacio", "Slowly explica cómo se hace una acción.")],
    op=("Escribe en tu cuaderno cinco instrucciones numeradas para una actividad relajante simple, como caminar al atardecer. Incluye una con Don't.",
        "1. Put on comfortable shoes. 2. Walk slowly. 3. Take a deep breath. 4. Look at the sky. 5. Don't use your phone.",
        ["usa cinco verbos en forma básica", "una instrucción lleva Don't", "los pasos están numerados"],
        ["cinco instrucciones escritas"],
        ["usar la «-s» en las instrucciones", "olvidar el orden de los pasos"],
        "Pregunta: «¿En qué orden harías los pasos y por qué?»."),
    reinforce="Escribe tres instrucciones para preparar un té, con el verbo básico.",
    extend="Escribe cuatro instrucciones para otra actividad relajante, con una instrucción negativa.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: escucho un diálogo sobre cómo descansamos y respondo preguntas con Do y Does.",
    prior=["Entiendo oraciones sobre actividades relajantes.", "Sé usar doesn't con he y she.", "Sé escuchar buscando la idea principal."],
    explain=[
        "Para preguntar por un hábito, el presente simple usa Do con I, you, we y they: Do you relax after work? Con he, she e it usa Does y el verbo queda sin «-s»: Does your brother walk with you?",
        "La respuesta corta repite el verbo auxiliar. Si es sí: Yes, I do. Yes, he does. Si es no: No, I don't. No, he doesn't. No se repite el verbo principal.",
        "Escucha primero el diálogo completo una vez, luego busca quién pregunta y quién responde. Anota el nombre de cada persona y una actividad. El diálogo lo lee otra persona en voz alta; es un guion, no un audio.",
    ],
    vocab=[("Do you...?", "¿Tú...? (pregunta de hábito)"), ("Does he...?", "¿Él...? (pregunta de hábito)"), ("Yes, I do", "Sí, lo hago"), ("No, he doesn't", "No, él no lo hace"), ("habit", "hábito")],
    worked=[
        ("Hacer una pregunta", "Quieres saber si el hermano de Lucía camina.", ["Sujeto he: uso Does.", "Verbo sin «-s»: walk.", "Agrego el resto."], "Does your brother walk with you?"),
        ("Responder corto", "Pregunta: Does your brother walk with you? La respuesta es no.", ["Uso No.", "Repito el sujeto: he.", "Uso doesn't."], "No, he doesn't."),
    ],
    mistakes=[("Preguntar «Does he walks?» con «-s».", "Does ya marca la tercera persona; el verbo queda sin «-s».", "Escribe Does he walk?"),
              ("Responder «No, he don't».", "Con he la respuesta usa doesn't.", "Responde No, he doesn't.")],
    T=[
        ("abc", "{F} What does Lucía do after work?", "She walks in the park and listens to music", "She works in the garden", "She reads a book", "Lucía dice «I walk in the park and I listen to music»."),
        ("ab", "{F} Does Lucía's brother walk with her?", "No, he doesn't", "Yes, he does", "Lucía responde que su hermano no camina con ella: No, he doesn't."),
        ("abc", "{F} What does her brother do?", "He works in the garden", "He reads a book", "He listens to the radio", "Lucía dice «He works in the garden»."),
        ("{F} Mr. Perez reads a ___ every night. Write the missing word.", "book", "El señor Pérez dice «I read a book every night»."),
        ("ab", "{F} Which sentence is true?", "Mr. Perez reads a book every night", "Lucía reads a book every night", "El hábito de leer es del señor Pérez."),
        ("abc", "Complete: ___ you relax after work?", "Do", "Does", "Are", "Con you se usa Do en el presente simple."),
        ("abc", "Complete: ___ your brother work in the garden?", "Does", "Do", "Is", "Con your brother (he) se usa Does."),
        ("ab", "Choose the correct short answer to «Do you walk in the park?» (yes).", "Yes, I do", "Yes, I am", "La respuesta repite el auxiliar do."),
        ("abc", "Choose the correct short answer to «Does Marta cook?» (no).", "No, she doesn't", "No, she don't", "No, she isn't", "Con she la respuesta negativa es doesn't."),
        ("abc", "Choose the correct question.", "Does Hugo read books?", "Does Hugo reads books?", "Do Hugo read books?", "Con Hugo (he) se usa Does y el verbo sin «-s»."),
        ("ab", "Put the words in order: you / Do / music / listen to", "Do you listen to music?", "Listen to music do you?", "La pregunta empieza con Do y sigue el sujeto."),
        ("abc", "{F} Who says «That's a good habit!»?", "Lucía", "Mr. Perez", "Lucía's brother", "Lucía responde con esa frase al hábito del señor Pérez."),
        ("abc", "Which question asks about another person's habit?", "Does your brother walk with you?", "Do you relax after work?", "Are you tired?", "La que habla del hermano pregunta por el hábito de otra persona."),
    ],
    ctx=("abc", "Quieres saber si tu vecina Carmen camina en el parque los domingos. ¿Qué le preguntas a una amiga que la conoce?", "Does she walk in the park on Sundays?", "Does she walks in the park on Sundays?", "Do she walk in the park on Sundays?", "Con she se usa Does y el verbo queda sin «-s»."),
    sc=[("En Inglés: ¿qué auxiliar se usa con he o she en una pregunta?", "Does", "Does va con he, she e it."),
        ("En Inglés: ¿cómo respondes «No» a «Do you walk?»", "No, I don't", "La respuesta corta repite el auxiliar."),
        ("En Inglés: ¿lleva «-s» el verbo después de Does?", "No", "Does ya marca la tercera persona.")],
    op=("Escribe un diálogo de seis líneas con nombres inventados en que una persona pregunta a otra cómo descansa. Usa Do you...?, Does he/she...? y respuestas cortas.",
        "Ana: Do you relax after work? Pedro: Yes, I do. I walk in the park. Ana: Does your wife walk with you? Pedro: No, she doesn't. She reads a book.",
        ["usa Do y Does en preguntas", "responde con Yes, I do o No, she doesn't", "el verbo queda sin «-s» después de Do y Does"],
        ["diálogo escrito de seis líneas"],
        ["usar la «-s» después de Does", "usar datos personales reales"],
        "Pregunta: «¿Qué pregunta hice y qué respuesta corta usé?»."),
    reinforce="Lee el diálogo en voz alta con otra persona, una línea cada una.",
    extend="Escribe cinco preguntas con Do o Does sobre cómo descansa una persona que conoces.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a la vida de la comunidad: leo un afiche y escribo una invitación breve con instrucciones.",
    prior=["Sé dar instrucciones con el verbo básico.", "Sé usar Don't.", "He visto afiches y avisos en mi barrio."],
    explain=[
        "En la comunidad, un afiche invita a participar. Lleva el nombre de la actividad, el día, la hora, el lugar y algunas instrucciones. Para leerlo, busca esas cinco cosas: qué, cuándo, a qué hora, dónde y qué debes hacer.",
        "Las instrucciones del afiche usan el verbo básico: Listen to music. Bring a chair. Don't bring your phone. La frase Every Thursday significa «todos los jueves» y se usa para actividades que se repiten.",
        "Para escribir tu propia invitación, copia el modelo y cambia los datos: nombre de la actividad, día, hora y lugar. Usa datos inventados y no pongas teléfonos ni direcciones reales.",
    ],
    vocab=[("community center", "centro comunitario"), ("every Thursday", "todos los jueves"), ("free", "gratis"), ("bring", "traer"), ("chair", "silla"), ("blanket", "manta")],
    worked=[
        ("Leer un afiche", "El afiche dice: «Every Thursday, 6:00 p.m.».", ["Every Thursday es el día que se repite.", "6:00 p.m. es la hora."], "Es todos los jueves a las 6 de la tarde"),
        ("Escribir una instrucción", "Quieres pedir que traigan una silla.", ["Verbo básico: bring.", "Agrego a chair."], "Bring a chair."),
    ],
    mistakes=[("Confundir Thursday con Tuesday.", "Son dos días distintos y se parecen al escribir.", "Lee la palabra completa letra por letra."),
              ("Escribir «Brings a chair» como instrucción.", "La instrucción usa el verbo básico.", "Escribe Bring a chair.")],
    T=[
        ("{F} What time is the Relaxing Hour? Write only the hour number.", "6", "El afiche dice 6:00 p.m., es decir, las seis de la tarde."),
        ("abc", "{F} On which day is the Relaxing Hour?", "Thursday", "Tuesday", "Saturday", "El afiche dice que la actividad es Every Thursday, todos los jueves."),
        ("ab", "{F} Where is the Relaxing Hour?", "In the garden of the center", "In the front desk", "El afiche dice «in the garden of the center»."),
        ("abc", "{F} What shouldn't you bring?", "Your phone", "A chair", "A blanket", "El afiche dice «Don't bring your phone»."),
        ("abc", "{F} What can you bring?", "A chair or a blanket", "Soup and bread", "A radio", "El afiche dice «Bring a chair or a blanket»."),
        ("ab", "{F} Is the activity free for neighbors?", "Yes, it is", "No, it isn't", "El afiche dice «It's free for neighbors»."),
        ("abc", "{F} Who should you ask at the front desk?", "Mrs. Díaz", "Mr. Perez", "Rosa", "El afiche dice «Ask Mrs. Díaz at the front desk»."),
        ("abc", "{F} Which sentence is an instruction from the poster?", "Listen to music", "Neighbors listen to music", "Music is relaxing", "La instrucción usa el verbo en forma básica."),
        ("abc", "Complete: ___ your phone.", "Don't bring", "Doesn't bring", "No bringing", "Para prohibir se usa Don't y el verbo básico."),
        ("ab", "Choose the correct instruction.", "Bring a chair", "Brings a chair", "La instrucción no lleva «-s» al final del verbo."),
        ("abc", "{F} What is the main idea of the poster?", "It invites neighbors to a relaxing hour at the center", "It sells tea at the center", "It explains a job interview", "El afiche invita a una actividad de descanso."),
        ("abc", "What does «free» mean in the poster?", "Gratis", "Libre de trabajo", "Lento", "En el afiche, free significa que no se paga."),
        ("ab", "What does «every Thursday» mean?", "Todos los jueves", "Un jueves de este mes", "Every indica que algo se repite."),
    ],
    ctx=("abc", "Tu vecino organiza una hora de música tranquila en la sede del barrio y te pide que lo invites por escrito. ¿Qué frase sirve para decir que es todos los viernes?", "Every Friday at 7:00 p.m.", "Every Fridays at 7:00 p.m.", "Friday every at 7:00 p.m.", "Every va antes del día en singular y indica que se repite."),
    sc=[("En Inglés: ¿qué datos lleva un afiche?", "Qué, cuándo, hora, lugar e instrucciones", "Esos datos permiten entender la invitación."),
        ("En Inglés: ¿cómo dices «Trae una silla»?", "Bring a chair", "El imperativo usa el verbo básico."),
        ("En Inglés: ¿qué significa «every Thursday»?", "Todos los jueves", "Every indica que se repite cada jueves.")],
    op=("Escribe en tu cuaderno un afiche de seis líneas para una actividad relajante inventada en tu comunidad. Incluye día, hora, lugar y tres instrucciones (una con Don't). No uses direcciones ni teléfonos reales.",
        "Quiet Walk. Every Sunday, 5:00 p.m., in the park of the neighborhood. Walk slowly. Listen to the birds. Don't use your phone.",
        ["incluye día, hora y lugar", "tres instrucciones con verbo básico", "una instrucción con Don't"],
        ["afiche escrito de seis líneas"],
        ["olvidar la hora o el lugar", "poner datos reales"],
        "Pregunta: «¿Qué dato falta para que una persona llegue a la actividad?»."),
    reinforce="Copia el afiche y subraya el día, la hora y el lugar.",
    extend="Diseña un segundo afiche para otra actividad relajante con otro día y otras tres instrucciones.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo aprendido: leo la descripción de una actividad inusual y relajante, escribo la mía y decido qué sigo practicando.",
    prior=["Escribo instrucciones con el verbo básico.", "Uso Don't.", "Sé presentar una actividad con día, hora y lugar."],
    explain=[
        "Una actividad inusual es algo poco común, pero posible y segura. En Rain Listening alguien se sienta junto a una ventana a escuchar la lluvia. Puedes crear una actividad así: elige un nombre y una razón.",
        "Un texto breve sobre una actividad lleva cuatro partes: el nombre, dónde se hace, los pasos con el verbo básico y por qué es relajante. La razón se une con because: It is relaxing because it is quiet.",
        "Antes de escribir, planifica en español y luego pasa a inglés oración por oración. Después revisa: ¿puse verbos básicos?, ¿puse Don't?, ¿expliqué por qué relaja? Este módulo se cierra con tu texto y con lo que quieres seguir practicando.",
    ],
    vocab=[("unusual", "poco común"), ("rain", "lluvia"), ("breathe", "respirar"), ("because", "porque"), ("eyes", "ojos"), ("afternoon", "tarde")],
    worked=[
        ("Dar la razón", "Quieres explicar que la actividad es tranquila.", ["Digo la idea: It is relaxing.", "Uno la razón con because.", "Agrego it is quiet."], "It is relaxing because it is quiet."),
        ("Escribir un paso", "Quieres decir que se cierren los ojos.", ["Verbo básico: close.", "Agrego your eyes."], "Close your eyes."),
    ],
    mistakes=[("Escribir «because» sin una oración después.", "Because necesita una razón completa.", "Escribe because + sujeto + verbo."),
              ("Escribir «Mr. Soto do it every day».", "Con he el verbo do cambia a does.", "Escribe Mr. Soto does it every day.")],
    T=[
        ("{F} How many minutes do you listen to the rain? Write the number.", "5", "El texto dice «for five minutes»."),
        ("abc", "{F} Where do you sit?", "In a quiet place near a window", "In the warehouse", "On a bus", "El texto dice «Find a quiet place near a window. Sit down»."),
        ("ab", "{F} What shouldn't you use?", "Your phone", "Your eyes", "El texto dice «Don't use your phone»."),
        ("abc", "{F} Why is Rain Listening relaxing?", "Because it is quiet and calm", "Because it is fast", "Because it is expensive", "El texto da esa razón con because."),
        ("abc", "{F} Who does Rain Listening every rainy afternoon?", "Mr. Soto", "Marta", "Rosa", "El texto dice «Mr. Soto, 63, does it every rainy afternoon»."),
        ("ab", "{F} How old is Mr. Soto?", "63", "36", "El texto dice «Mr. Soto, 63»."),
        ("abc", "{F} Which sentence is an instruction in the text?", "Close your eyes", "Mr. Soto closes his eyes", "People are closing their eyes", "La instrucción usa el verbo básico."),
        ("abc", "Complete: Mr. Soto ___ Rain Listening every rainy afternoon.", "does", "do", "doing", "Con he el verbo do cambia a does."),
        ("abc", "Complete: ___ slowly.", "Breathe", "Breathes", "Breathing", "La instrucción usa el verbo básico."),
        ("ab", "Which sentence gives the reason?", "It is relaxing because it is quiet", "It is relaxing because it is noisy", "El texto explica la razón con quiet y calm."),
        ("abc", "Put the words in order: eyes / Close / your", "Close your eyes", "Your eyes close", "Eyes your close", "La instrucción empieza con el verbo."),
        ("ab", "Spot the error and choose the correct sentence: «Mr. Soto do it every day.»", "Mr. Soto does it every day", "Mr. Soto do it every days", "Con he, do cambia a does."),
        ("abc", "Which sentence is a negative instruction?", "Don't use your phone", "Mr. Soto doesn't use his phone", "You are not using your phone", "La orden negativa empieza con Don't."),
    ],
    ctx=("abc", "En el taller del centro te piden presentar una actividad inusual y relajante. Quieres decir por qué es tranquila. ¿Qué escribes?", "It is relaxing because it is calm", "It is relaxing because calm", "It relaxing because is calm", "Because une una razón completa con sujeto y verbo."),
    sc=[("En Inglés: ¿qué partes tiene un texto sobre una actividad?", "Nombre, lugar, pasos y razón", "Esas partes dan un texto claro y completo."),
        ("En Inglés: ¿cómo uno una razón?", "Con because", "Because introduce la razón de algo."),
        ("En Inglés: ¿cómo escribo una instrucción negativa?", "Don't + verbo", "Don't indica lo que no se debe hacer.")],
    op=("Escribe un texto de seis a siete oraciones sobre una actividad inusual y relajante que inventes: nombre, lugar, cuatro pasos con verbo básico (uno con Don't) y una razón con because. Léelo en voz alta a alguien.",
        "Window Reading. Find a quiet place near a window. Sit down. Open a book. Read one page slowly. Don't use your phone. It is relaxing because it is calm.",
        ["incluye nombre y lugar", "cuatro pasos con verbo básico", "una instrucción con Don't y una razón con because"],
        ["texto de seis a siete oraciones y lectura en voz alta"],
        ["olvidar la razón con because", "usar la «-s» en las instrucciones"],
        "Pregunta: «¿Por qué mi actividad relaja y qué paso es el más importante?»."),
    reinforce="Escribe tres pasos de una actividad relajante, con el verbo básico.",
    extend="Escribe la segunda versión de tu texto con otro nombre, otros pasos y otra razón.",
)

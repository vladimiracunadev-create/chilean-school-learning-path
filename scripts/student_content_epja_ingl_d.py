"""Inglés EPJA Nivel 2, módulo 4 (parte 1): OAD-13, entregar información y consejos sobre hábitos y diferentes generaciones. Todos los textos son inventados y se leen en papel."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-13"

F1 = ("Text (example): Carlos is 45 years old. He works at a warehouse. Every morning he drinks a glass of water and walks to work. He eats fruit at lunch. "
      "He sleeps eight hours every night. Carlos's mother, Mrs. Rosa, is 72. She drinks tea in the morning and walks in the park every afternoon. She doesn't eat fast food.")

F2 = ("Family list (example): Mr. Lopez is the grandfather. He is 70 years old. His daughter, Marta, is 40. Marta's son, Tomás, is 18. "
      "Mr. Lopez is older than Marta. Tomás is younger than Marta. Mr. Lopez is old, and Tomás is young.")

F3 = ("Dialogue (example). Ana: I'm tired every morning. Joe: How many hours do you sleep? Ana: Five hours. "
      "Joe: You should sleep seven or eight hours. You shouldn't drink coffee at night. You should walk after dinner.")

F4 = ("Text (example): My neighbor, Elena, is 78 years old. She wakes up at five. She drinks tea, makes bread and listens to the radio. "
      "My coworker, Diego, is 19. He wakes up at eight. He drinks juice, checks his phone and goes to work by bus. "
      "Elena doesn't use a phone. Diego doesn't listen to the radio. Elena is older than Diego. Diego is younger than Elena.")

F5 = ("Note at a workplace (example). From Mr. Silva, supervisor, to Pedro, a new worker: «Pedro, welcome. You should arrive at 7:45. You shouldn't use your phone in the warehouse. "
      "You should drink water every hour. Ask Mrs. Vera if you have a question. She is older than you, and she knows the job well.» "
      "Reply from Pedro: «Thank you, Mr. Silva. I usually arrive early. I don't use my phone at work.»")

F6 = ("Text (example), two neighbors: Mrs. Inés is 66 years old. She wakes up at six, walks in the park and cooks lunch at home. She doesn't eat fast food. "
      "Kevin is 24. He works at night, sleeps in the morning and eats fast food on weekdays. "
      "Mrs. Inés says to Kevin: «You should cook at home. You shouldn't eat fast food every day. You should walk with me on Sunday!»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya hago cada día y leo un texto corto sobre los hábitos de dos personas de edades distintas.",
    prior=["Reconozco palabras en inglés de la calle, del trabajo y de los mensajes.", "Sé decir lo que hago en un día normal.", "He conversado con personas mayores y más jóvenes sobre sus costumbres."],
    explain=[
        "Un hábito es algo que haces con frecuencia, casi sin pensarlo: tomar agua en la mañana, caminar al trabajo, dormir a una hora fija. Tú ya tienes muchos hábitos y los puedes contar en inglés con oraciones cortas.",
        "Para hablar de hábitos se usa el presente simple. Con I, you, we y they el verbo no cambia: I drink water. Con he, she e it el verbo lleva una «-s» al final: He drinks water. Para negar se usa don't o doesn't: She doesn't eat fast food (el verbo queda sin «-s»).",
        "Las palabras every morning, every day y every night dicen cada cuánto ocurre el hábito. Al leer, busca primero esas palabras y los verbos: así entiendes quién hace qué. Estos textos son ejemplos de vida diaria y no reemplazan el consejo de un profesional de la salud.",
    ],
    vocab=[("habit", "hábito, algo que haces con frecuencia"), ("healthy", "sano, bueno para la salud"), ("every morning", "cada mañana"), ("walk", "caminar"), ("sleep", "dormir"), ("fast food", "comida rápida")],
    worked=[
        ("Contar un hábito", "Quieres decir que una amiga camina al paradero cada día.", ["Elijo el verbo: walk.", "Mi amiga es «she», así que agrego «-s»: walks.", "Agrego el lugar y la frecuencia."], "My friend walks to the bus stop every day."),
        ("Negar un hábito", "Texto: Mrs. Rosa no come comida rápida.", ["Con «she» uso doesn't.", "Después de doesn't el verbo queda sin «-s»: eat.", "Completo la oración."], "She doesn't eat fast food."),
    ],
    mistakes=[("Escribir «Carlos drink water» sin la «-s».", "Con he, she e it el verbo del presente simple lleva «-s».", "Revisa el sujeto: si es he, she o it, escribe drinks."),
              ("Escribir «She doesn't eats fast food».", "Después de doesn't el verbo vuelve a su forma sin «-s», porque doesn't ya marca el he/she/it.", "Con doesn't, usa el verbo solo: doesn't eat.")],
    T=[
        ("abc", "{F} Which is a healthy habit of Carlos?", "He drinks a glass of water every morning", "He eats fast food every day", "He sleeps four hours at night", "El texto dice que bebe agua cada mañana y duerme ocho horas."),
        ("ab", "{F} How does Carlos go to work?", "He walks", "He takes a bus", "El texto dice «walks to work»: va a pie."),
        ("{F} How many hours does Carlos sleep every night? Write the number.", "8", "El texto dice que Carlos duerme eight hours, es decir, ocho horas."),
        ("abc", "{F} Who walks in the park every afternoon?", "Mrs. Rosa", "Carlos", "Carlos and Mrs. Rosa", "Carlos camina al trabajo; solo Mrs. Rosa camina en el parque."),
        ("ab", "{F} Which sentence is true?", "Mrs. Rosa doesn't eat fast food", "Mrs. Rosa eats fast food every day", "El texto dice «She doesn't eat fast food»."),
        ("abc", "Complete: Carlos ___ water every morning.", "drinks", "drink", "drinking", "Con Carlos (he) el presente simple lleva «-s»."),
        ("abc", "Complete: My neighbors ___ in the park every Sunday.", "walk", "walks", "walking", "Con «my neighbors» (they) el verbo no lleva «-s»."),
        ("abc", "Marta says: «Reading before bed is my favorite habit.» What does «habit» mean?", "Algo que haces con frecuencia", "Un lugar para leer", "Una comida de la noche", "Habit significa hábito: una costumbre que se repite."),
        ("Complete with one verb: I ___ eight hours every night. (dormir)", "sleep", "Con «I» el verbo no lleva «-s»: I sleep."),
        ("abc", "Which sentence is correct?", "My friend walks to the bus stop every day", "My friend walk to the bus stop every day", "My friend walking to the bus stop every day", "Con «my friend» (she) el verbo walk lleva «-s»."),
        ("ab", "Spot the error and choose the correct sentence: «Mrs. Rosa drink tea every morning.»", "Mrs. Rosa drinks tea every morning", "Mrs. Rosa drinking tea every morning", "Con she, el verbo del presente simple lleva «-s»."),
        ("abc", "Put the words in order: walks / Ana / to the market / every day", "Ana walks to the market every day", "Ana walk to the market every day", "Walks Ana to the market every day", "El orden es sujeto, verbo, lugar y frecuencia."),
        ("ab", "Make this sentence negative: «Carlos eats fruit at lunch.»", "Carlos doesn't eat fruit at lunch", "Carlos doesn't eats fruit at lunch", "Después de doesn't el verbo queda sin «-s»."),
    ],
    ctx=("abc", "En la pausa del trabajo, tu compañero Luis te pregunta por tus hábitos. Quieres decir que tomas agua todos los días. ¿Qué oración usas?", "I drink water every day", "I drinks water every day", "I am drink water every day", "Con «I» el verbo queda sin «-s» y sin «am»."),
    sc=[("En Inglés: ¿el verbo lleva «-s» en presente simple con he, she o it?", "Sí: He drinks, she walks", "Con he, she e it el verbo termina en «-s»."),
        ("En Inglés: ¿cómo se niega «She eats fast food»?", "She doesn't eat fast food", "Doesn't marca la negación y el verbo queda sin «-s»."),
        ("En Inglés: ¿qué significa «every morning»?", "Cada mañana", "Every indica que se repite y morning es la mañana.")],
    op=("Escribe en tu cuaderno tres oraciones en inglés sobre tus hábitos y una sobre el hábito de una persona cercana (usa un nombre inventado). Usa every day, every morning o every night.",
        "I wake up at six every morning. I drink water and I walk to work. My friend Ana drinks tea every night.",
        ["escribe tres oraciones con I y una con he o she", "agrega la «-s» con he o she", "usa una palabra de frecuencia"],
        ["cuatro oraciones escritas"],
        ["olvidar la «-s» con he o she", "poner datos personales reales"],
        "Pregunta: «¿Qué verbo usé y a quién se lo atribuí?»."),
    reinforce="Escribe tres hábitos tuyos con I y dilos en voz alta.",
    extend="Escribe dos hábitos de una persona mayor que conoces, con un nombre inventado, usando he o she.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo las palabras old, young, older y younger para hablar de generaciones y de las edades de una familia.",
    prior=["Sé decir hábitos con el presente simple.", "Conozco los números hasta 100.", "Hablo de mi familia en español."],
    explain=[
        "Una generación es el grupo de personas de edades parecidas: abuelos, padres, hijos, nietos. Para describirlas usamos adjetivos. Old significa mayor o de más edad, y young significa joven. Se dicen con respeto: Mr. Lopez is old.",
        "Para comparar a dos personas usamos older than, «mayor que», y younger than, «menor que». La palabra than va siempre después y se traduce como «que»: My father is older than my uncle. En esta clase tomamos older y younger como palabras completas, sin teoría de comparativos.",
        "La edad se dice con el verbo to be: He is 70 years old. Para preguntar: How old is he? Familia en inglés: grandfather, grandmother, grandson, daughter, son. Lee la lista de familia y subraya los nombres y los números.",
    ],
    vocab=[("old", "mayor, de más edad"), ("young", "joven"), ("older than", "mayor que"), ("younger than", "menor que"), ("grandfather", "abuelo"), ("grandson", "nieto"), ("daughter", "hija")],
    worked=[
        ("Comparar dos edades", "Doña Carmen tiene 80 años y su hija 55.", ["Comparo los números: 80 es más que 55.", "Carmen es la persona mayor: older.", "Uso than antes de la otra persona."], "Carmen is older than her daughter."),
        ("Decir la edad", "Tomás tiene 18 años.", ["Uso to be: is.", "Digo el número y years old."], "Tomás is 18 years old."),
    ],
    mistakes=[("Decir «more young than» para comparar.", "En inglés se usa la palabra younger, que ya contiene la idea de «más joven».", "Escribe younger than y older than."),
              ("Escribir «older that» en vez de «older than».", "Para comparar se necesita than; that significa otra cosa.", "Después de older o younger escribe than.")],
    T=[
        ("abc", "{F} Who is older, Mr. Lopez or Marta?", "Mr. Lopez", "Marta", "Tomás", "Mr. Lopez tiene 70 años y Marta 40, así que él es mayor."),
        ("ab", "{F} Tomás is ___ than Marta.", "younger", "older", "Tomás tiene 18 y Marta 40, entonces él es menor."),
        ("{F} How old is Tomás? Write the number.", "18", "El texto dice que Marta's son, Tomás, is 18."),
        ("abc", "{F} What does «grandson» mean?", "Nieto", "Abuelo", "Hijo", "Grandson es el nieto: el hijo de un hijo o hija."),
        ("abc", "{F} Mr. Lopez is Tomás's ___.", "grandfather", "grandson", "daughter", "Mr. Lopez es el papá de Marta y por eso el abuelo de Tomás."),
        ("ab", "{F} Which sentence is true?", "Marta is younger than Mr. Lopez", "Marta is older than Mr. Lopez", "Marta tiene 40 años y Mr. Lopez tiene 70."),
        ("abc", "Complete: Carmen is 80 and her daughter is 55. Carmen is ___ than her daughter.", "older", "younger", "tired", "Ochenta es más que cincuenta y cinco, entonces es mayor: older."),
        ("abc", "Complete: Ana is 22 and her brother is 17. Her brother is ___ than Ana.", "younger", "older", "taller", "El hermano tiene menos años: younger."),
        ("{F} What is the name of Mr. Lopez's daughter? Write one word.", "Marta", "El texto dice «His daughter, Marta, is 40»."),
        ("ab", "Choose the correct sentence.", "My father is older than my uncle", "My father is older that my uncle", "En las comparaciones se usa than, no that."),
        ("abc", "What is the opposite of «young»?", "old", "tall", "happy", "El opuesto de joven es old, mayor."),
        ("abc", "{F} Which sentence matches the text?", "Mr. Lopez is old and Tomás is young", "Mr. Lopez is young and Tomás is old", "Mr. Lopez and Tomás are both young", "Mr. Lopez tiene 70 años y Tomás 18."),
        ("ab", "Choose the correct sentence.", "Tomás is younger than Marta", "Tomás is more young than Marta", "Se dice younger, no more young."),
    ],
    ctx=("abc", "En una reunión de vecinos, Camila presenta a su papá de 68 años y a su hijo de 15. Quiere decir que su papá es mayor que su hijo. ¿Qué dice?", "My father is older than my son", "My father is younger than my son", "My father is old that my son", "Older than significa mayor que, es decir, con más edad."),
    sc=[("En Inglés: ¿qué significa «younger than»?", "Menor que", "Younger indica que alguien tiene menos edad."),
        ("En Inglés: ¿cómo se dice «abuelo»?", "Grandfather", "Grandfather es el padre de tu padre o de tu madre."),
        ("En Inglés: ¿qué palabra va después de older o younger?", "than", "Than une la comparación y se traduce como que.")],
    op=("Escribe cuatro oraciones sobre tu familia o sobre una familia inventada. Usa old, young, older than y younger than, y la edad con years old.",
        "My grandmother is 80 years old. My mother is 55. My grandmother is older than my mother. My nephew is young.",
        ["usa older than o younger than correctamente", "escribe una edad con years old", "usa la forma is"],
        ["cuatro oraciones escritas"],
        ["escribir that en vez de than", "usar edades reales de personas"],
        "Pregunta: «¿Quién es mayor y cómo lo dije en inglés?»."),
    reinforce="Mira la lista de familia y di en voz alta quién es older y quién es younger.",
    extend="Escribe tres oraciones comparando a tres personas inventadas de distintas edades.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a dar un consejo en inglés con las expresiones You should y You shouldn't.",
    prior=["Sé hablar de hábitos con el presente simple.", "Sé decir older y younger.", "He dado consejos a personas de mi familia o del trabajo."],
    explain=[
        "Para dar un consejo usamos la expresión completa You should + un verbo: You should sleep more, «deberías dormir más». Para decir lo que no conviene hacer usamos You shouldn't + verbo: You shouldn't eat fast food every day.",
        "Paso 1: empieza con You should o You shouldn't. Paso 2: escribe el verbo sin «-s» y sin «to»: You should walk, nunca You should walks ni You should to walk. Paso 3: agrega cuándo o dónde: after dinner, at night, every day.",
        "En esta clase los consejos son de la vida diaria, como dormir, caminar y tomar agua. No son consejos médicos: si tienes una duda de salud, conversa con una persona profesional del consultorio. La expresión should no es un tiempo nuevo; la aprendemos completa.",
    ],
    vocab=[("advice", "consejo"), ("You should...", "deberías..."), ("You shouldn't...", "no deberías..."), ("at night", "en la noche"), ("after dinner", "después de la cena"), ("coffee", "café")],
    worked=[
        ("Dar un consejo", "Tu compañero duerme poco y quieres decirle que duerma siete horas.", ["Empiezo con You should.", "Agrego el verbo sin «-s»: sleep.", "Agrego el resto: seven hours."], "You should sleep seven hours."),
        ("Decir lo que no conviene", "Quieres decirle a un amigo que no tome café en la noche.", ["Empiezo con You shouldn't.", "Verbo sin «-s»: drink.", "Agrego coffee at night."], "You shouldn't drink coffee at night."),
    ],
    mistakes=[("Escribir «You should to walk».", "Después de should el verbo va solo, sin to.", "Usa You should + verbo: You should walk."),
              ("Escribir «You should eats vegetables».", "Should no cambia y el verbo siguiente queda sin «-s».", "Escribe You should eat vegetables.")],
    T=[
        ("abc", "{F} Which advice does Joe give Ana?", "She should sleep seven or eight hours", "She should drink more coffee", "She should sleep five hours", "Joe dice «You should sleep seven or eight hours»."),
        ("{F} How many hours does Ana sleep? Write the number.", "5", "Ana responde que duerme five hours."),
        ("ab", "{F} What shouldn't Ana do at night?", "Drink coffee", "Sleep", "Joe dice «You shouldn't drink coffee at night»."),
        ("abc", "Complete: You ___ drink water every day.", "should", "shoulds", "are should", "Should no cambia y va antes del verbo."),
        ("abc", "Complete the negative advice: You ___ eat fast food every day.", "shouldn't", "should", "don't should", "Para decir lo que no conviene usamos shouldn't."),
        ("abc", "Which sentence is correct?", "You should walk after dinner", "You should walks after dinner", "You should to walk after dinner", "Después de should el verbo va sin «-s» y sin to."),
        ("ab", "Choose the correct sentence.", "You should eat vegetables", "You should eats vegetables", "El verbo después de should queda sin «-s»."),
        ("abc", "Put the words in order: should / sleep / You / early", "You should sleep early", "You sleep should early", "Sleep you should early", "El orden es You, should, verbo y complemento."),
        ("abc", "Your coworker says: «I'm tired all day.» Which advice is correct?", "You should sleep more", "You should sleeps more", "You should to sleep more", "El consejo correcto usa should y el verbo sin «-s»."),
        ("ab", "What does «You shouldn't» mean?", "No deberías", "Deberías", "Shouldn't es la forma negativa de should."),
        ("ab", "{F} According to Joe, which sentence is true?", "Ana shouldn't drink coffee at night", "Ana should drink coffee at night", "Joe aconseja no tomar café en la noche."),
        ("abc", "{F} What should Ana do after dinner?", "Walk", "Sleep", "Drink coffee", "Joe dice «You should walk after dinner»."),
        ("abc", "A friend watches TV until 3 a.m. and wakes up at 6. Complete the advice to go to bed earlier: You ___ go to bed earlier.", "should", "shouldn't", "are", "El consejo útil es ir a dormir más temprano: should."),
    ],
    ctx=("abc", "Una vecina nueva te pregunta cómo estar más descansada en las mañanas. Quieres aconsejarle que duerma más. ¿Qué dices?", "You should sleep more", "You should sleeps more", "You are should sleep more", "La estructura es You should + verbo."),
    sc=[("En Inglés: ¿cómo das un consejo con la expresión completa?", "You should + verbo", "You should se usa antes de un verbo sin «-s»."),
        ("En Inglés: ¿cómo dices «no deberías comer comida rápida»?", "You shouldn't eat fast food", "Shouldn't se usa para decir lo que no conviene."),
        ("En Inglés: ¿lleva «to» el verbo después de should?", "No", "Después de should el verbo va solo.")],
    op=("Escribe en tu cuaderno cuatro consejos para un compañero de trabajo que llega cansado cada día. Usa dos con You should y dos con You shouldn't.",
        "You should sleep seven hours. You should drink water. You shouldn't drink coffee at night. You shouldn't use your phone in bed.",
        ["usa dos veces You should y dos veces You shouldn't", "el verbo va sin «-s» ni to", "los consejos son de vida diaria"],
        ["cuatro consejos escritos"],
        ["escribir should to + verbo", "dar consejos médicos o de medicamentos"],
        "Pregunta: «¿Qué verbo usé después de should y por qué no tiene -s?»."),
    reinforce="Di en voz alta tres consejos que le darías a un amigo que duerme poco.",
    extend="Escribe un diálogo de cuatro líneas, con nombres inventados, en que una persona pide un consejo y otra responde con You should.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: leo el texto de una vecina mayor y un compañero joven, comparo sus hábitos y completo oraciones.",
    prior=["Sé usar el presente simple con he y she.", "Entiendo older y younger.", "Puedo dar consejos con You should."],
    explain=[
        "Cuando comparas los hábitos de dos generaciones, lees un texto, buscas los verbos y los pones en una tabla mental: quién hace qué y a qué hora. Subraya las horas, los verbos y los nombres.",
        "Para decir lo que alguien no hace usa doesn't con he o she: Elena doesn't use a phone. Para contrastar dos hábitos usa but, «pero»: Elena wakes up at five, but Diego wakes up at eight.",
        "Después de leer, responde las preguntas con la información del texto, no con lo que tú supones. Si una respuesta no aparece, vuelve a leer. Trabaja en pareja si puedes: uno lee en voz alta y otro subraya.",
    ],
    vocab=[("wake up", "despertarse"), ("radio", "radio"), ("phone", "teléfono"), ("but", "pero"), ("juice", "jugo"), ("by bus", "en bus")],
    worked=[
        ("Contrastar dos hábitos", "Elena se despierta a las cinco y Diego a las ocho.", ["Escribo el hábito de Elena con wakes up.", "Uso but para contrastar.", "Escribo el hábito de Diego con wakes up."], "Elena wakes up at five, but Diego wakes up at eight."),
        ("Negar con doesn't", "Diego no escucha radio.", ["Con he uso doesn't.", "El verbo queda sin «-s»: listen."], "Diego doesn't listen to the radio."),
    ],
    mistakes=[("Escribir «Elena wake up at five».", "Con she el verbo del presente simple lleva «-s»: wakes.", "Revisa el sujeto antes de escribir el verbo."),
              ("Escribir «Diego don't use a phone».", "Con he o she la negación es doesn't, no don't.", "Usa doesn't con he, she e it.")],
    T=[
        ("{F} What time does Elena wake up? Write the number.", "5", "El texto dice que Elena wakes up at five."),
        ("{F} What time does Diego wake up? Write the number.", "8", "El texto dice que Diego wakes up at eight."),
        ("ab", "{F} Who listens to the radio?", "Elena", "Diego", "El texto dice que Elena lo hace y que Diego no lo hace."),
        ("abc", "{F} What does Diego do after he drinks juice?", "He checks his phone", "He makes bread", "He listens to the radio", "El texto dice «drinks juice, checks his phone»."),
        ("abc", "{F} Which habit is Elena's?", "She makes bread", "She goes to work by bus", "She checks her phone every hour", "Elena toma té, hace pan y escucha la radio."),
        ("ab", "{F} Which sentence is true?", "Diego doesn't listen to the radio", "Diego listens to the radio every morning", "El texto dice que Diego no escucha radio."),
        ("abc", "Complete: Elena ___ up at five.", "wakes", "wake", "waking", "Con Elena (she) el verbo lleva «-s»."),
        ("abc", "Complete: Elena doesn't ___ a phone.", "use", "uses", "using", "Después de doesn't el verbo queda sin «-s»."),
        ("abc", "{F} Which sentence about the text is correct?", "Diego is younger than Elena", "Diego is older than Elena", "Diego and Elena are the same age", "Diego tiene 19 y Elena 78."),
        ("ab", "{F} Which sentence is correct?", "Elena wakes up at five, but Diego wakes up at eight", "Elena wakes up at eight, but Diego wakes up at five", "Los horarios del texto son cinco para Elena y ocho para Diego."),
        ("abc", "Diego wants to give advice to a person who sits all day. Which advice is correct?", "You should walk in the park", "You should walks in the park", "You should to walk in the park", "Después de should el verbo va sin «-s» y sin to."),
        ("ab", "Choose the correct sentence.", "Diego doesn't listen to the radio", "Diego don't listen to the radio", "Con he la negación es doesn't."),
        ("abc", "What does «Elena is older than Diego» mean?", "Elena es mayor que Diego", "Elena es menor que Diego", "Elena y Diego tienen la misma edad", "Older than significa mayor que, es decir, con más edad."),
    ],
    ctx=("abc", "En tu trabajo, una colega mayor llega a las cinco y un colega joven a las ocho. Quieres decir que ella llega a las cinco pero él a las ocho. ¿Qué dices?", "She arrives at five, but he arrives at eight", "She arrive at five, but he arrive at eight", "She arrives at five, and he arrives at five", "Con she y he el verbo lleva «-s» y but contrasta."),
    sc=[("En Inglés: ¿qué palabra se usa para contrastar dos hábitos?", "but", "But significa pero y une dos ideas distintas."),
        ("En Inglés: ¿cómo se niega «He uses a phone»?", "He doesn't use a phone", "Doesn't lleva el verbo sin «-s»."),
        ("En Inglés: ¿qué significa «Diego is younger than Elena»?", "Diego es menor que Elena", "Younger than indica que alguien tiene menos años.")],
    op=("Escribe en tu cuaderno cuatro oraciones que comparen los hábitos de una persona mayor y una joven que inventes. Usa but, doesn't y una hora.",
        "My uncle wakes up at six, but my cousin wakes up at nine. My uncle doesn't use social media. My cousin doesn't read the newspaper.",
        ["compara dos personas con but", "usa doesn't con he o she", "escribe una hora"],
        ["cuatro oraciones escritas"],
        ["escribir don't con he o she", "olvidar la «-s» del verbo"],
        "Pregunta: «¿Qué diferencia de hábitos mostré entre las dos personas?»."),
    reinforce="Lee el texto en voz alta y subraya los verbos con «-s».",
    extend="Agrega al texto dos hábitos más de Elena y dos de Diego, con oraciones completas en inglés.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una situación de trabajo: leo una nota con consejos y respondo de manera respetuosa.",
    prior=["Doy consejos con You should y You shouldn't.", "Sé comparar edades.", "He recibido instrucciones en un trabajo nuevo."],
    explain=[
        "En el trabajo, los consejos aparecen en notas, carteles y mensajes. Una persona con más experiencia suele dar consejos a quien llega: You should arrive at 7:45. Para responder con respeto, agradece y cuenta tus hábitos: Thank you. I usually arrive early.",
        "Las palabras de frecuencia usually y generally significan «por lo general». Se ponen antes del verbo: I usually arrive early. Con he o she el verbo lleva «-s»: She usually arrives early.",
        "Al leer una nota, busca primero quién escribe, a quién y para qué. Después subraya los consejos: lo que sí se debe hacer y lo que no. Esa es la idea general del texto. Las horas se escriben con dos puntos: 7:45.",
    ],
    vocab=[("welcome", "bienvenido"), ("arrive", "llegar"), ("warehouse", "bodega"), ("every hour", "cada hora"), ("usually", "por lo general"), ("question", "pregunta"), ("Thank you", "gracias")],
    worked=[
        ("Entender una nota", "Mr. Silva escribe: «You shouldn't use your phone in the warehouse».", ["Veo quién escribe: Mr. Silva, el supervisor.", "Veo el consejo negativo: You shouldn't.", "Entiendo qué evitar: usar el teléfono en la bodega."], "No debes usar el teléfono en la bodega"),
        ("Responder con respeto", "Quieres agradecer y decir que llegas temprano.", ["Empiezo con Thank you.", "Agrego usually y el verbo."], "Thank you. I usually arrive early."),
    ],
    mistakes=[("Poner usually después del verbo: «I arrive usually early».", "Las palabras de frecuencia van antes del verbo principal.", "Escribe I usually arrive early."),
              ("Escribir «You shouldn't to use your phone».", "Después de shouldn't el verbo va solo.", "Escribe You shouldn't use your phone.")],
    T=[
        ("{F} What time should Pedro arrive? Write the time with numbers.", "7:45", "La nota dice «You should arrive at 7:45»."),
        ("abc", "{F} What shouldn't Pedro use in the warehouse?", "His phone", "Water", "A radio", "La nota dice «You shouldn't use your phone in the warehouse»."),
        ("ab", "{F} How often should Pedro drink water?", "Every hour", "Every day", "La nota dice «drink water every hour»."),
        ("abc", "{F} Who should Pedro ask if he has a question?", "Mrs. Vera", "Mr. Silva", "Pedro", "La nota dice «Ask Mrs. Vera if you have a question»."),
        ("ab", "{F} Which sentence is true?", "Mrs. Vera is older than Pedro", "Mrs. Vera is younger than Pedro", "La nota dice que ella es older than you."),
        ("abc", "Complete Pedro's reply: «I ___ use my phone at work.»", "don't", "doesn't", "shouldn't to", "Con I la negación es don't."),
        ("abc", "What does «usually» mean?", "Por lo general", "Nunca", "Casi nunca", "Usually indica lo que ocurre casi siempre."),
        ("ab", "Pedro says: «I don't use my phone at work.» Which advice does this follow?", "You shouldn't use your phone at work", "You should use your phone at work", "Su hábito coincide con el consejo negativo."),
        ("abc", "Complete the negative advice: You ___ arrive late to your appointment.", "shouldn't", "should", "don't should", "Llegar tarde a una cita no conviene, por eso va shouldn't."),
        ("abc", "Put the words in order: wash / should / hands / You / your", "You should wash your hands", "You wash should your hands", "Should wash you your hands", "El orden correcto es You, should, verbo y complemento."),
        ("ab", "Spot the error and choose the correct sentence: «You shouldn't to use your phone.»", "You shouldn't use your phone", "You shouldn't uses your phone", "Después de shouldn't el verbo va sin to y sin «-s»."),
        ("{F} What is the supervisor's last name? Write one word.", "Silva", "La nota está firmada por Mr. Silva, el supervisor."),
        ("abc", "{F} Pedro says: «I usually arrive early.» Which sentence is true?", "He generally arrives before the start time", "He always arrives late", "He never arrives early", "Usually significa por lo general: llega temprano."),
    ],
    ctx=("abc", "Tu supervisor te recomienda por escrito llegar a las ocho en punto. Quieres agradecer y decir que normalmente llegas temprano. ¿Qué respondes?", "Thank you. I usually arrive early", "Thank you. I arrive usually early", "Thanks you. I usuallys arrive early", "Usually va antes del verbo y el agradecimiento es Thank you."),
    sc=[("En Inglés: ¿dónde va usually en la oración?", "Antes del verbo principal", "I usually arrive early: usually va antes de arrive."),
        ("En Inglés: ¿cómo agradeces a tu supervisor por una nota?", "Thank you", "Thank you es la expresión de agradecimiento."),
        ("En Inglés: ¿cómo se dice «no deberías usar tu teléfono»?", "You shouldn't use your phone", "Shouldn't marca lo que no conviene hacer.")],
    op=("Escribe una nota breve, de cuatro oraciones, de una persona con experiencia a una persona nueva en un trabajo inventado. Incluye dos consejos con You should, uno con You shouldn't y una hora.",
        "Welcome, Ana. You should arrive at 8:00. You should ask Mr. Perez if you have a question. You shouldn't leave the door open.",
        ["incluye dos You should y un You shouldn't", "los verbos van sin «-s» ni to", "incluye una hora"],
        ["nota escrita de cuatro oraciones"],
        ["usar to después de should", "olvidar la hora"],
        "Pregunta: «¿Qué consejo es más importante en mi nota y por qué?»."),
    reinforce="Lee la nota de Mr. Silva en voz alta y marca los tres consejos.",
    extend="Escribe una respuesta de Pedro con cuatro oraciones: agradecer, decir un hábito y hacer una pregunta.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo aprendido: comparo dos generaciones, doy consejos y decido qué sigo practicando.",
    prior=["Uso el presente simple con he y she.", "Doy consejos con You should.", "Sé comparar edades con older y younger."],
    explain=[
        "En este módulo aprendiste a hablar de hábitos, comparar generaciones y dar consejos. Hoy lees un texto de dos vecinos y lo reúnes todo: verbos con «-s», doesn't, older than y You should.",
        "Para revisar tu avance, pregúntate: ¿entiendo quién hace qué?, ¿puedo dar un consejo corto?, ¿puedo comparar a dos personas? Marca lo que ya haces bien y lo que aún quieres practicar.",
        "Los pasos siguientes son pequeños: leer un cartel o un mensaje en inglés cada día, anotar tres hábitos nuevos y decirlos en voz alta. Las personas jóvenes y adultas aprenden con constancia, no con perfección.",
    ],
    vocab=[("neighbor", "vecino o vecina"), ("weekdays", "días de semana"), ("cook", "cocinar"), ("at home", "en casa"), ("on Sunday", "el domingo")],
    worked=[
        ("Combinar hábitos y consejo", "Mrs. Inés cocina en casa y le aconseja a Kevin que haga lo mismo.", ["Hábito con she: cooks at home.", "Consejo con You should: cook at home."], "She cooks at home. You should cook at home too."),
        ("Comparar edades", "Mrs. Inés tiene 66 y Kevin 24.", ["Compruebo quién tiene más años.", "Uso older than."], "Mrs. Inés is older than Kevin."),
    ],
    mistakes=[("Mezclar «doesn't» con un verbo con «-s».", "Doesn't ya marca he, she o it; el verbo queda sin «-s».", "Escribe doesn't eat, no doesn't eats."),
              ("Usar «to» después de should.", "Should va con el verbo solo.", "Escribe You should walk.")],
    T=[
        ("{F} How old is Mrs. Inés? Write the number.", "66", "El texto dice «Mrs. Inés is 66 years old»."),
        ("abc", "{F} Who cooks lunch at home?", "Mrs. Inés", "Kevin", "Both of them", "El texto dice que Mrs. Inés cooks lunch at home."),
        ("ab", "{F} Kevin is ___ than Mrs. Inés.", "younger", "older", "Kevin tiene 24 y ella 66."),
        ("abc", "{F} What does Kevin do on weekdays?", "He eats fast food", "He walks in the park", "He cooks at home", "El texto dice que come comida rápida los días de semana."),
        ("abc", "{F} Which is one piece of advice from Mrs. Inés?", "You should cook at home", "You should eat fast food", "You should work at night", "Mrs. Inés aconseja a Kevin cocinar en casa."),
        ("ab", "{F} What shouldn't Kevin do every day?", "Eat fast food", "Walk with Mrs. Inés", "Ella dice «You shouldn't eat fast food every day»."),
        ("abc", "Complete: Mrs. Inés ___ eat fast food.", "doesn't", "don't", "isn't", "Con she la negación es doesn't."),
        ("abc", "Complete: Kevin ___ at night.", "works", "work", "working", "Con Kevin (he) el verbo lleva «-s»."),
        ("abc", "Which sentence is correct?", "Mrs. Inés is older than Kevin", "Mrs. Inés is more old than Kevin", "Mrs. Inés is old that Kevin", "Se usa older than para comparar."),
        ("ab", "Spot the error and choose the correct sentence: «Kevin shoulds sleep more.»", "Kevin should sleep more", "Kevin shoulds sleeps more", "Should no lleva «-s» y el verbo va sin «-s»."),
        ("abc", "Which advice would you give to someone who sleeps four hours?", "You should sleep more", "You should sleeps more", "You should to sleep more", "El consejo correcto usa should y el verbo sin «-s»."),
        ("ab", "Which question asks about habits?", "What do you do every morning?", "What you do every morning?", "En una pregunta se usa do antes del sujeto."),
        ("abc", "Put the words in order: walk / You / Sunday / should / on", "You should walk on Sunday", "You walk should on Sunday", "Should walk you on Sunday", "El orden es You, should, verbo y complemento."),
    ],
    ctx=("abc", "Tu vecino joven te cuenta que come comida rápida a diario y quieres aconsejarle cocinar en casa algunos días. ¿Qué dices?", "You should cook at home", "You should cooks at home", "You should to cook at home", "La estructura correcta es You should + verbo."),
    sc=[("En Inglés: ¿puedo dar un consejo con You should + verbo?", "Sí, con el verbo sin «-s» y sin to", "La estructura es You should + verbo."),
        ("En Inglés: ¿puedo negar con doesn't con he o she?", "Sí, y el verbo queda sin «-s»", "Doesn't marca la negación en tercera persona."),
        ("En Inglés: ¿puedo decir quién es older o younger?", "Sí, con older than y younger than", "Para comparar dos edades se usa than, que significa que.")],
    op=("Escribe un texto breve de cinco oraciones sobre dos personas inventadas de edades distintas: hábitos, una comparación de edad y un consejo. Luego léelo en voz alta a alguien de confianza.",
        "Mr. Reyes is 70. He walks every morning. Lucía is 25. She works at night. Mr. Reyes is older than Lucía. He says: You should sleep at night.",
        ["compara dos edades con older o younger", "usa el verbo con «-s» con he o she", "incluye un consejo con You should"],
        ["texto de cinco oraciones y lectura en voz alta"],
        ["olvidar la «-s» del verbo", "usar datos reales de personas"],
        "Pregunta: «¿Qué parte de mi texto fue más fácil y cuál quiero practicar?»."),
    reinforce="Escribe tres consejos para alguien que duerme poco, con You should.",
    extend="Anota tres hábitos de una persona mayor y tres de una persona joven que inventes, y compáralos en seis oraciones.",
)

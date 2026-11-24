"""Inglés EPJA Nivel 2, módulo 2 (OAD-06): comprender la transcripción de un video sobre ciudades y clima, y describir la ciudad de origen y sus desafíos climáticos. Textos inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-06"

F1 = ("Video transcript (example), weather report: Good morning. Today it's sunny in the north and rainy in the south. "
      "In the center, it's cloudy and windy. The temperature is 20 degrees Celsius in the north and 8 degrees Celsius in the south.")

F2 = ("Video transcript (example), Mr. Silva, a farmer: In my town, summer is very hot and dry. This year there is a drought: there is no water for the plants. "
      "In winter, sometimes there is a flood. The river is high and the streets are wet. Climate challenges are hard for families.")

F3 = ("Rule card (example): Now: It's raining. It's snowing. It isn't raining. Is it raining? Yes, it is. No, it isn't. "
      "Habits: It rains in winter. It doesn't rain in summer. Does it rain a lot? Yes, it does. Time words: now, at the moment, in winter, every year.")

F4 = ("Video transcript (example), two friends: Carlos: My city is Valdivia. It's green and quiet. It's rainy in winter and cool in summer. "
      "Mary: My city is Calama. It's dry and sunny. At noon it's very hot, and at night it's very cold.")

F5 = ("Message (example) from a coworker: Hi Ana! This week the weather is bad. It's raining and it's windy. We can't work outside on Wednesday. "
      "Bring your coat. The temperature is 9 degrees Celsius. See you at 8:00.")

F6 = ("Video transcript (example), Tom: Hello. I'm Tom. My city is in the south of Chile. It's cold and windy. It's snowing at the moment. "
      "In winter it snows a lot. In summer it's cool. A challenge is the wind: sometimes it is very strong and people stay home. I like my city.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de las palabras del tiempo que ya conozco y comprendo la transcripción de un parte meteorológico en inglés.",
    prior=["Sé decir si hace frío o calor.", "Conozco algunas ciudades y zonas de mi país.", "Puedo leer números como 8 o 20."],
    explain=[
        "Todos los días hablamos del clima: si llueve, si hace calor o si hay viento. Esa experiencia te ayuda a entender un parte del tiempo en inglés.",
        "Este cuaderno no tiene video. Trabajamos con la transcripción escrita de un video de ejemplo: es un límite que declaramos, y sirve para practicar lo mismo.",
        "Antes de leer, haz una predicción: mira el título y piensa qué palabras esperas. En un parte del tiempo esperas palabras como sunny, rainy, cold y números de temperatura.",
        "En inglés, para hablar del clima usamos it's + una palabra: It's sunny, It's cold. Es el verbo to be, que ya conoces.",
    ],
    vocab=[("sunny", "soleado"), ("rainy", "lluvioso"), ("cloudy", "nublado"), ("windy", "con viento"), ("cold", "frío"), ("hot", "caluroso"), ("today", "hoy")],
    worked=[
        ("Hacer una predicción", "Ves el título «Weather report». Quieres predecir qué palabras hay.", ["Weather significa clima o tiempo.", "Espero palabras como sunny, rainy, cold.", "Espero números de temperatura."], "Predigo palabras del clima y números"),
        ("Decir el clima de un lugar", "Quieres decir que hoy hace frío.", ["Uso it's, que es it is.", "Agrego la palabra del clima: cold.", "Agrego today al final."], "It's cold today."),
    ],
    mistakes=[("Decir «It has cold» para «hace frío».", "En inglés no se usa has: se usa el verbo to be, como en it is cold.", "Escribe It's cold."),
              ("Querer entender cada palabra del parte.", "Se pierde la idea general; el parte repite pocas palabras clave.", "Subraya lugar, clima y número, y sigue leyendo.")],
    T=[
        ("abc", "{F} What is the report about?", "The weather in three parts of the country", "A recipe for dinner", "A list of bus times", "El parte menciona norte, sur y centro con su clima."),
        ("abc", "{F} How is the weather in the north?", "Sunny", "Rainy", "Windy", "El texto dice «sunny in the north»."),
        ("ab", "{F} How is the weather in the south?", "Rainy", "Sunny", "El texto dice «rainy in the south»."),
        ("{F} What is the temperature in the south? Escribe solo el número.", "8", "La temperatura del sur es de 8 grados."),
        ("abc", "{F} How is the weather in the center?", "Cloudy and windy", "Sunny and hot", "Rainy and cold", "El texto dice «cloudy and windy» para el centro."),
        ("abc", "Hoy hace frío en tu barrio (ejemplo). ¿Cómo lo dices en inglés?", "It's cold today.", "It has cold today.", "He is cold today.", "Para el clima se usa it is y la palabra cold."),
        ("ab", "En el parte, «sunny» significa:", "Soleado", "Lluvioso", "Sun es sol, y sunny describe un día con sol."),
        ("abc", "Antes de leer un parte titulado «Weather report», ¿qué palabras predices?", "Sunny, rainy, cold", "Bread, rice, eggs", "Bus, taxi, bike", "Un parte del tiempo habla del clima, no de comida ni de transporte."),
        ("ab", "{F} Elige la oración verdadera.", "It's 20 degrees in the north.", "It's 8 degrees in the north.", "Los 20 grados son del norte y los 8 son del sur."),
        ("abc", "{F} ¿En qué lugar hay 8 grados?", "In the south", "In the north", "In the center", "El texto dice que en el sur la temperatura es de 8 grados."),
        ("abc", "Un amigo escribe «It's cloudy». ¿Cómo está el cielo?", "Nublado", "Soleado", "Con viento", "Cloudy viene de cloud, que significa nube."),
        ("abc", "Completa: The weather ___ cloudy in the center.", "is", "are", "am", "Weather es singular, y con él se usa is."),
        ("ab", "Elige la oración correcta.", "It is rainy in the south.", "It are rainy in the south.", "Con it se usa is, la forma de to be."),
    ],
    ctx=("abc", "Lees en un sitio de noticias (ejemplo) el parte del tiempo en inglés: «Tomorrow: rainy and cold.» Debes decidir qué abrigo llevar. ¿Cómo estará el clima?", "Lluvioso y frío", "Soleado y caluroso", "Con viento y calor", "Rainy es lluvioso y cold es frío."),
    sc=[("¿Qué significa «windy»?", "Con viento", "Windy viene de wind, que es viento."),
        ("¿Qué hago antes de leer un texto para predecir su contenido?", "Miro el título y pienso qué palabras espero", "Predecir ayuda a entender más rápido."),
        ("¿Cómo se dice «hoy está nublado»?", "It's cloudy today.", "Se usa it's más la palabra cloudy.")],
    op=("Lee el parte del tiempo: {F} Escribe en tu cuaderno tres oraciones sobre el clima de tu ciudad hoy (datos de ejemplo), con it's y una palabra como sunny, cold o windy.",
        "It's sunny today. It's cold in the morning. It's windy at night.",
        ["escribe tres oraciones", "usa it's y una palabra del clima", "agrega today o un momento del día"],
        ["tres oraciones con it's"],
        ["escribir «It has cold»", "olvidar el verbo to be"],
        "Pregunta: «¿Cómo está el clima en tu ciudad ahora?»."),
    reinforce="Mira por la ventana y escribe, en inglés, cómo está el clima en este momento.",
    extend="Anota el clima de tres lugares que conoces usando sunny, rainy, cloudy o windy.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy reconozco el vocabulario de la transcripción de un video sobre sequía, inundación y calor, y entiendo la idea principal.",
    prior=["Conozco palabras del clima como sunny y rainy.", "Sé subrayar palabras clave.", "Conozco el verbo to be."],
    explain=[
        "El clima no siempre es agradable: a veces trae problemas. Los desafíos climáticos más conocidos son la sequía (drought), la inundación (flood) y el calor extremo (heat).",
        "En la transcripción, el agricultor Mr. Silva habla de su pueblo. Para entender su idea principal, subraya los problemas que menciona y las épocas del año en que ocurren.",
        "Las palabras hot y heat se parecen pero no son iguales. Hot es un adjetivo: It's hot. Heat es un sustantivo: The heat is strong.",
        "Los adjetivos describen cómo es algo: hot, dry, wet, high. Se escriben antes del sustantivo o después de to be: «a high river» o «The river is high».",
    ],
    vocab=[("heat", "calor (sustantivo)"), ("drought", "sequía"), ("flood", "inundación"), ("river", "río"), ("dry", "seco"), ("wet", "mojado"), ("farmer", "agricultor o agricultora")],
    worked=[
        ("Reconocer un desafío", "Frase (example): «There is a drought: there is no water for the plants.»", ["Subrayo drought: es una sequía.", "Veo no water: no hay agua.", "Concluyo: el problema es la falta de agua."], "Desafío: sequía, falta de agua"),
        ("Usar hot y heat", "Quieres decir «El calor es fuerte» y «Hoy hace calor».", ["El calor (cosa) es heat: The heat is strong.", "Hace calor (descripción) usa hot: It's hot today."], "The heat is strong. It's hot today."),
    ],
    mistakes=[("Escribir «It's very heat today».", "Heat es un sustantivo y después de it's va un adjetivo.", "Escribe It's very hot today."),
              ("Confundir drought con flood.", "Una es falta de agua y la otra es exceso de agua.", "Recuerda: drought, sin agua; flood, mucha agua.")],
    T=[
        ("abc", "{F} What is the video about?", "Weather problems in a farmer's town", "A cooking show", "A job interview", "El agricultor habla de sequía e inundación en su pueblo."),
        ("abc", "{F} What is a problem in summer?", "A drought", "A flood", "A snowstorm", "El texto dice que este año hay sequía en verano."),
        ("ab", "{F} What happens sometimes in winter?", "A flood", "A drought", "El texto dice que en invierno, a veces, hay una inundación."),
        ("abc", "En la transcripción, «drought» significa:", "Sequía", "Inundación", "Viento", "Drought es la falta de agua por mucho tiempo."),
        ("abc", "En la transcripción, «flood» significa:", "Inundación", "Sequía", "Calor", "Flood es cuando el agua cubre calles y campos."),
        ("ab", "{F} «Summer is very hot and dry» significa:", "El verano es muy caluroso y seco", "El verano es muy frío y húmedo", "Hot es caluroso y dry es seco."),
        ("abc", "{F} Who is speaking?", "A farmer", "A bus driver", "A doctor", "El texto dice «Mr. Silva, a farmer»."),
        ("ab", "{F} During the flood, the river is:", "High", "Low", "El texto dice «The river is high»."),
        ("abc", "Traduce: «El verano es muy caluroso».", "Summer is very hot.", "Summer is very heat.", "Summer has very hot.", "Hot es el adjetivo y va después de is very."),
        ("abc", "{F} Completa: In winter the streets ___ wet.", "are", "is", "am", "Streets es plural, y con plural se usa are."),
        ("{F} ¿Qué no tienen las plantas? Escribe una palabra en inglés.", "water", "El texto dice «there is no water for the plants»."),
        ("abc", "{F} «Climate challenges are hard for families» significa:", "Los desafíos del clima son difíciles para las familias", "Los desafíos del clima son fáciles", "Las familias no tienen problemas", "Hard es difícil y challenges son desafíos."),
        ("ab", "Elige la oración correcta.", "It's very hot today.", "It's very heat today.", "Después de it's va un adjetivo, y heat es un sustantivo."),
    ],
    ctx=("abc", "En una reunión de tu comunidad (ejemplo) alguien dice en inglés: «We have a drought.» ¿Qué problema tiene la comunidad?", "Falta de agua por mucho tiempo", "Mucha agua en las calles", "Demasiado viento", "Drought es sequía, es decir, falta de agua."),
    sc=[("¿Qué significa «flood»?", "Inundación", "Flood es agua que cubre calles y campos."),
        ("¿Cuál es el adjetivo: hot o heat?", "Hot", "Hot es adjetivo, y heat es sustantivo."),
        ("Completa: The river ___ high.", "is", "River es singular y con él se usa is.")],
    op=("Lee la transcripción del agricultor: {F} Escribe en tu cuaderno tres oraciones sobre un desafío climático de un lugar que conoces (datos de ejemplo): qué problema es y cómo es el clima.",
        "In my town, there is a drought. Summer is hot and dry. The river is low.",
        ["escribe tres oraciones", "nombra un desafío (drought, flood o heat)", "usa un adjetivo como hot, dry o wet"],
        ["tres oraciones sobre un desafío climático"],
        ["usar heat como adjetivo", "confundir drought con flood"],
        "Pregunta: «¿Cuál es el desafío más fuerte en tu lugar?»."),
    reinforce="Haz una tabla con las palabras drought, flood y heat y anota su significado.",
    extend="Busca en el diario o la radio un desafío del clima y cuéntalo con dos oraciones en inglés.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a decir qué clima hay ahora (presente continuo) y cómo es habitualmente (presente simple).",
    prior=["Uso it's con palabras del clima.", "Uso doesn't y don't en negativo.", "Conozco ahora y todos los días."],
    explain=[
        "Para hablar de lo que ocurre ahora usamos el presente continuo: it is + verbo con -ing. Por ejemplo: It's raining (Está lloviendo), It's snowing (Está nevando).",
        "Para hablar de lo que ocurre siempre o cada año usamos el presente simple: It rains in winter. En negativo: It doesn't rain in summer. En pregunta: Does it rain a lot?",
        "Las palabras de tiempo ayudan a elegir. Con now y at the moment usa -ing. Con in winter, every year, every day usa el presente simple.",
        "Pregunta con presente continuo: Is it raining? Respuestas cortas: Yes, it is. No, it isn't. Con presente simple: Does it rain? Yes, it does.",
    ],
    vocab=[("raining", "lloviendo"), ("snowing", "nevando"), ("now", "ahora"), ("at the moment", "en este momento"), ("in winter", "en invierno"), ("every year", "cada año")],
    worked=[
        ("Elegir la forma", "Quieres decir: «Ahora está lloviendo».", ["Ahora pide presente continuo.", "It is + raining.", "Escribo: It's raining now."], "It's raining now."),
        ("Hablar de un hábito", "Quieres decir: «En invierno llueve».", ["En invierno es una costumbre.", "Uso presente simple: rains.", "Escribo: It rains in winter."], "It rains in winter."),
    ],
    mistakes=[("Decir «It rains now» cuando está pasando ahora.", "Con now el inglés usa el presente continuo.", "Escribe It's raining now."),
              ("Escribir «It's rain».", "Falta la terminación -ing después de it's.", "Escribe It's raining.")],
    T=[
        ("abc", "{F} Completa: Look! It ___ now.", "is raining", "rains", "rain", "Con now el clima se dice con el presente continuo."),
        ("abc", "{F} Completa: In winter it ___ a lot in Valdivia (ejemplo).", "rains", "is raining", "rain", "In winter indica un hábito, entonces se usa el presente simple."),
        ("ab", "{F} ¿Qué palabra de tiempo va con «It's raining»?", "At the moment", "Every year", "At the moment pide el presente continuo."),
        ("abc", "{F} Completa: It ___ raining at the moment.", "isn't", "doesn't", "not", "Con -ing la negación es isn't."),
        ("abc", "{F} Completa: It ___ rain in summer here.", "doesn't", "isn't", "aren't", "Con presente simple en negativo se usa doesn't."),
        ("abc", "{F} Completa la pregunta: ___ it raining?", "Is", "Does", "Do", "Con -ing la pregunta empieza con Is."),
        ("abc", "{F} Completa la pregunta: ___ it rain a lot in your city?", "Does", "Is", "Are", "Con presente simple, con it, se usa Does."),
        ("ab", "{F} Is it windy now? Elige la respuesta corta para «sí».", "Yes, it is.", "Yes, it does.", "Se responde con la misma forma de la pregunta: is."),
        ("Ordena las palabras: raining / at the moment / It's. Empieza con It's y escribe la oración.", "It's raining at the moment.", "El orden es it's, el verbo con -ing y la expresión de tiempo."),
        ("Traduce: «Ahora está lloviendo». Escribe la oración en inglés.", "It's raining now.", "Se usa it's y raining con la palabra de tiempo now."),
        ("ab", "¿Cuál es el error en «It's rain now»?", "Falta -ing: raining", "Sobra now", "Después de it's necesitamos el verbo con -ing."),
        ("abc", "¿Qué oración describe un hábito?", "It snows in winter.", "It's snowing now.", "It's snowing at the moment.", "Solo la primera habla de lo que ocurre en general en invierno."),
        ("ab", "Is it snowing? Elige la respuesta corta para «no».", "No, it isn't.", "No, it doesn't.", "La pregunta usa is, así que la respuesta usa isn't."),
    ],
    ctx=("abc", "Hablas por teléfono con una amiga (ejemplo), que vive lejos. Ella pregunta cómo está el clima ahora donde tú estás, y está lloviendo. ¿Qué dices?", "It's raining now.", "It rains now.", "It rain now.", "Para lo que ocurre ahora se usa it's más -ing."),
    sc=[("¿Qué forma uso con «now»?", "El presente continuo, con -ing", "Now indica algo que ocurre en este momento."),
        ("Completa: It ___ rain in summer.", "doesn't", "Con presente simple en negativo, con it, se usa doesn't."),
        ("¿Cómo respondo «Is it raining?» si es que sí?", "Yes, it is.", "Se repite is en la respuesta corta.")],
    op=("Revisa la tarjeta de reglas: {F} Escribe en tu cuaderno cuatro oraciones: dos sobre el clima de ahora (it's + -ing) y dos sobre el clima de tu ciudad en general (presente simple).",
        "It's raining now. It isn't windy. In winter it rains a lot. It doesn't snow in summer.",
        ["escribe cuatro oraciones", "dos con it's + -ing", "dos con presente simple"],
        ["cuatro oraciones: dos con -ing y dos con presente simple"],
        ["usar rains con now", "olvidar -ing"],
        "Pregunta: «¿Qué ocurre ahora y qué ocurre siempre?»."),
    reinforce="Mira por la ventana y escribe dos oraciones con it's y -ing sobre lo que ves ahora.",
    extend="Escribe tres preguntas con Is it...? o Does it...? sobre el clima y pide a otra persona que las responda.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: leo la transcripción de dos amigos, comparo sus ciudades y describo una ciudad con adjetivos.",
    prior=["Uso it's con palabras del clima.", "Conozco hot, cold, dry y wet.", "Sé distinguir ahora de siempre."],
    explain=[
        "Para describir una ciudad usamos adjetivos: green, quiet, dry, sunny, hot, cold. Un adjetivo dice cómo es algo. En inglés el adjetivo va después de is o antes del sustantivo.",
        "Los posesivos muestran de quién es algo: my city (mi ciudad), his city (su ciudad, de él), her city (su ciudad, de ella). En la transcripción, Carlos habla de my city y Mary de my city; tú hablas de his city y her city.",
        "This y that son demostrativos. This señala algo cerca: This is my city (en una foto en mi mano). That señala algo lejos: That is a river (allá lejos).",
        "Para practicar con apoyo, lee, subraya y responde con otra persona. Si algo no queda claro, vuelve a la frase del texto.",
    ],
    vocab=[("green", "verde"), ("quiet", "tranquilo"), ("cool", "fresco"), ("noon", "mediodía"), ("night", "noche"), ("his", "su (de él)"), ("her", "su (de ella)")],
    worked=[
        ("Describir con adjetivos", "Carlos dice: «My city is green and quiet.»", ["Busco la ciudad: Valdivia.", "Busco los adjetivos: green, quiet.", "Describo: Carlos's city is green and quiet."], "Verde y tranquila"),
        ("Usar his y her", "Quieres decir: «Su ciudad es seca» sobre Mary.", ["Mary es ella: her.", "Ciudad: city.", "Escribo: Her city is dry."], "Her city is dry."),
    ],
    mistakes=[("Decir «His city» cuando hablas de Mary.", "His es de él y her es de ella.", "Para Mary usa her city."),
              ("Usar that para algo que tienes en la mano.", "That se usa para algo lejos; para algo cerca se usa this.", "Usa This is my city.")],
    T=[
        ("abc", "{F} What is Carlos's city?", "Valdivia", "Calama", "Santiago", "El texto dice «My city is Valdivia»."),
        ("abc", "{F} How is Carlos's city?", "Green and quiet", "Dry and sunny", "Hot and noisy", "Carlos describe su ciudad como green and quiet."),
        ("ab", "{F} Is it rainy in Valdivia in winter?", "Yes, it is.", "No, it isn't.", "Carlos dice que su ciudad es «rainy in winter»."),
        ("abc", "{F} How is Mary's city?", "Dry and sunny", "Green and quiet", "Rainy and cool", "Mary describe su ciudad con las palabras «dry and sunny»."),
        ("ab", "{F} At noon in Mary's city, it is:", "Very hot", "Very cold", "El texto dice «At noon it's very hot»."),
        ("abc", "{F} What is it like at night in Mary's city?", "Very cold", "Very hot", "Rainy", "Mary dice «at night it's very cold»."),
        ("abc", "{F} Whose city is quiet?", "Carlos's city", "Mary's city", "Both cities", "Solo Carlos dice que su ciudad es tranquila."),
        ("abc", "{F} Mary dice «my city». Para hablar de ella tú dices:", "Her city", "His city", "Our city", "Her es el posesivo de she."),
        ("abc", "{F} Para hablar de la ciudad de Carlos dices:", "His city", "Her city", "Their city", "His es el posesivo de he."),
        ("ab", "Elige la oración correcta.", "Her city is dry.", "She city is dry.", "Antes de city va el posesivo her, no el pronombre she."),
        ("abc", "Mary tiene una foto de su ciudad en la mano. Dice: «___ is my city.»", "This", "That", "These", "This se usa para algo que está cerca."),
        ("abc", "Un adjetivo opuesto a «hot» es:", "Cold", "Dry", "Quiet", "Hot significa caluroso y cold significa frío, son opuestos."),
        ("{F} How many cities do the friends talk about? Escribe el número.", "2", "Carlos habla de Valdivia y Mary de Calama."),
    ],
    ctx=("abc", "En tu clase de inglés (ejemplo), una compañera te muestra una foto en su mano de su pueblo y dice «___ is my town». ¿Qué palabra falta?", "This", "That", "Those", "This sirve para señalar algo cercano, como una foto en la mano."),
    sc=[("¿Qué palabra uso para hablar de algo de una mujer?", "Her", "Her es el posesivo de she."),
        ("¿Qué significa «quiet»?", "Tranquilo", "Quiet describe un lugar sin mucho ruido."),
        ("¿Cuándo uso «this»?", "Para algo cercano", "This señala algo que está cerca de quien habla.")],
    op=("Lee la transcripción de los dos amigos: {F} Escribe en tu cuaderno cuatro oraciones sobre una ciudad que conoces (datos de ejemplo): su nombre, dos adjetivos y el clima.",
        "My city is Valdivia. It's green and quiet. It's rainy in winter. It's cool in summer.",
        ["escribe cuatro oraciones", "usa dos adjetivos", "usa it's para el clima"],
        ["cuatro oraciones sobre una ciudad"],
        ["escribir «She city»", "olvidar el verbo is"],
        "Pregunta: «¿Cómo es esa ciudad y cómo es su clima?»."),
    reinforce="Escribe dos oraciones sobre la ciudad de Carlos y dos sobre la ciudad de Mary, con his y her.",
    extend="Compara con una persona de tu curso dos ciudades distintas, usando adjetivos y clima.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una situación de trabajo: leo un mensaje sobre el clima de la semana y describo el clima y los desafíos de mi ciudad de origen.",
    prior=["Describo el clima con it's.", "Distingo ahora de siempre.", "Uso adjetivos como hot, cold, dry y wet."],
    explain=[
        "El clima influye en el trabajo: se puede trabajar o no afuera, qué ropa llevar, a qué hora llegar. Los mensajes de trabajo suelen ser cortos: clima, aviso y hora.",
        "En este mensaje hay frases útiles. «We can't work outside» significa que no podemos trabajar afuera. «Bring your coat» es una instrucción: trae tu abrigo.",
        "Después de leer, presenta tu ciudad de origen con datos de ejemplo: My city is hot and dry. It rains in winter. A challenge is the heat.",
        "Usa los dos tiempos que aprendiste: It's raining now para el momento y It rains in winter para el hábito.",
    ],
    vocab=[("weather", "tiempo, clima"), ("this week", "esta semana"), ("coat", "abrigo"), ("outside", "afuera"), ("bring", "traer"), ("bad", "malo")],
    worked=[
        ("Leer un mensaje de trabajo", "Message (example): «We can't work outside on Wednesday.»", ["Busco el día: Wednesday.", "Entiendo: no se puede trabajar afuera.", "Deduzco: hay mal tiempo."], "No se trabaja afuera el miércoles"),
        ("Presentar mi ciudad", "Quieres decir: «Mi ciudad es calurosa. Llueve en invierno».", ["Mi ciudad es calurosa: My city is hot.", "Llueve en invierno: It rains in winter.", "Uno las dos ideas."], "My city is hot. It rains in winter."),
    ],
    mistakes=[("Entender «can't work» como «puedo trabajar».", "El apóstrofo indica negación: can't es no puede.", "Lee la palabra completa: can't = cannot, no se puede."),
              ("Decir «It's rain in winter».", "En un hábito se usa el verbo sin -ing: rains.", "Escribe It rains in winter.")],
    T=[
        ("{F} What is the temperature? Escribe solo el número.", "9", "El mensaje dice «The temperature is 9 degrees Celsius»."),
        ("abc", "{F} How is the weather this week?", "Rainy and windy", "Sunny and hot", "Snowy and cold", "El mensaje dice «It's raining and it's windy»."),
        ("ab", "{F} Can the team work outside on Wednesday?", "No, they can't.", "Yes, they can.", "El mensaje dice «We can't work outside on Wednesday»."),
        ("abc", "{F} What should Ana bring?", "Her coat", "Her lunch", "Her umbrella", "El mensaje dice «Bring your coat»."),
        ("{F} ¿A qué hora dice el mensaje «See you»? Escribe solo la hora, por ejemplo 9:00.", "8:00", "El mensaje termina con «See you at 8:00»."),
        ("abc", "Traduce: «Hoy está lloviendo y hace viento».", "It's raining and it's windy today.", "It rains and it is wind today.", "It's rain and windy today.", "Se usa it's raining para ahora y it's windy con to be."),
        ("ab", "Elige la oración correcta para decir que en tu ciudad llueve poco.", "It doesn't rain a lot.", "It don't rain a lot.", "Con it la negación del presente simple es doesn't."),
        ("abc", "Completa: My city ___ cold in winter.", "is", "are", "am", "City es singular y con él se usa is."),
        ("ab", "¿Cuál de estas afirmaciones sobre los desafíos climáticos es correcta?", "Una sequía es un largo tiempo sin lluvia.", "Una inundación es un largo tiempo sin lluvia.", "La sequía es la falta de lluvia y la inundación es exceso de agua."),
        ("Ordena las palabras: hot / My / is / city. Escribe la oración.", "My city is hot.", "El orden es posesivo, sustantivo, verbo to be y adjetivo."),
        ("abc", "¿Cuál es la oración correcta?", "It rains a lot in winter in my city.", "It is rain a lot in my city.", "It rain a lot in winter in my city.", "Para un hábito se usa el presente simple: rains."),
        ("abc", "{F} ¿Para qué sirve este mensaje?", "Para avisar del mal tiempo y los planes de trabajo", "Para vender abrigos", "Para contar un cuento", "Es un aviso de trabajo con clima, indicación y hora."),
        ("abc", "{F} En «We can't work outside», ¿qué significa «outside»?", "Afuera", "Adentro", "Mañana", "Outside es lo contrario de inside, o sea, afuera."),
    ],
    ctx=("abc", "Un compañero de trabajo (ejemplo) te escribe: «Is it raining in your city?» Sí está lloviendo ahora. ¿Qué respondes?", "Yes, it is.", "Yes, it does.", "Yes, it rains.", "La pregunta usa is, entonces la respuesta usa is."),
    sc=[("En el mensaje del trabajo, ¿qué significa «We can't work outside»?", "No podemos trabajar afuera", "Can't es la forma corta de cannot."),
        ("Completa: It ___ in winter in my city. (llueve, hábito)", "rains", "Con un hábito y it se usa el presente simple con -s."),
        ("¿Qué es una sequía en inglés?", "A drought", "Drought es falta de agua por mucho tiempo.")],
    op=("Mira el mensaje del compañero: {F} Escribe en tu cuaderno una respuesta de cuatro oraciones: di cómo está el clima en tu ciudad ahora, cómo es en general y un desafío climático. Usa datos de ejemplo.",
        "It's windy now. My city is cold in winter. It rains a lot. A challenge is the flood.",
        ["escribe cuatro oraciones", "usa it's + -ing o it's + adjetivo", "nombra un desafío"],
        ["una respuesta de cuatro oraciones"],
        ["confundir ahora con siempre", "dejar sin desafío"],
        "Pregunta: «¿Cómo afecta el clima a tu trabajo?»."),
    reinforce="Escribe un mensaje corto a un compañero diciendo cómo está el clima hoy y qué debe llevar.",
    extend="Describe, en cinco oraciones, la ciudad de origen de una persona que conoces (datos de ejemplo).",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado sobre ciudades, clima y desafíos, hago una autoevaluación y decido qué practicar después.",
    prior=["Describí el clima con it's.", "Distingo el presente continuo del presente simple.", "Describí una ciudad con adjetivos."],
    explain=[
        "Revisar lo logrado es comprobar qué puedes hacer ahora: entender la transcripción de un video sobre una ciudad, decir qué clima hay ahora y cómo es en general, y presentar un desafío climático.",
        "Para revisar un texto tuyo, mira tres cosas: ¿usé it's + -ing para ahora?, ¿usé presente simple para hábitos con -s en rains y snows?, ¿usé adjetivos y posesivos bien?",
        "Los siguientes pasos pueden ser pequeños: practicar tres palabras del clima nuevas cada semana, escribir un mensaje del clima o escuchar a otra persona leer el parte en voz alta.",
        "Recuerda que sin audio no puedes comprobar la pronunciación. Pide a otra persona que lea la transcripción y repite despacio las frases más difíciles.",
    ],
    vocab=[("snow", "nieve o nevar"), ("strong", "fuerte"), ("stay home", "quedarse en casa"), ("sometimes", "a veces"), ("challenge", "desafío"), ("people", "personas")],
    worked=[
        ("Revisar un texto propio", "Alguien escribe: «It rain in winter».", ["Es un hábito: presente simple.", "Con it el verbo lleva -s: rains.", "Corrijo: It rains in winter."], "It rains in winter."),
        ("Responder con datos", "Pregunta sobre el texto: «What is the challenge in Tom's city?»", ["Busco challenge en el texto.", "Leo: «A challenge is the wind».", "Respondo: the wind."], "The wind"),
    ],
    mistakes=[("Decir «It snows at the moment».", "At the moment pide presente continuo.", "Escribe It's snowing at the moment."),
              ("Entender «strong wind» como viento suave.", "Strong significa fuerte.", "Revisa el significado de cada adjetivo antes de responder.")],
    T=[
        ("abc", "{F} Where is Tom's city?", "In the south of Chile", "In the north of Chile", "In the center of Chile", "El texto dice «in the south of Chile»."),
        ("abc", "{F} What is the weather at the moment?", "Cold, windy and snowing", "Hot and sunny", "Cloudy and dry", "El texto dice «cold and windy. It's snowing at the moment»."),
        ("ab", "{F} Does it snow a lot in winter?", "Yes, it does.", "No, it doesn't.", "El texto dice «In winter it snows a lot»."),
        ("abc", "{F} How is the weather in summer?", "Cool", "Hot", "Rainy", "Tom dice «In summer it's cool»."),
        ("abc", "{F} What is the challenge in Tom's city?", "The wind", "The drought", "The heat", "Tom dice «A challenge is the wind»."),
        ("ab", "{F} When do people stay home?", "When the wind is very strong", "When it is sunny", "El texto dice que si el viento es muy fuerte, las personas se quedan en casa."),
        ("{F} How many seasons does Tom name (winter, summer...)? Escribe el número.", "2", "Tom nombra winter y summer, que son dos estaciones del año."),
        ("abc", "Tom dice «I like my city». ¿Qué significa?", "Me gusta mi ciudad", "Vivo en mi ciudad", "Odio mi ciudad", "Like en esta frase significa gustar."),
        ("abc", "Completa: It's raining now. In winter it ___ a lot.", "rains", "is raining", "rain", "In winter es un hábito, entonces se usa el presente simple."),
        ("ab", "Corrige: «It rains at the moment».", "It's raining at the moment.", "It raining at the moment.", "Con at the moment se necesita is y el verbo con -ing."),
        ("Traduce: «Mi ciudad es tranquila y fresca». Escribe la oración en inglés con quiet y cool.", "My city is quiet and cool.", "Se usa my city, el verbo to be y los adjetivos quiet y cool."),
        ("abc", "¿Cuál de estas oraciones tiene un error?", "It don't snow in summer.", "It doesn't snow in summer.", "It's snowing now.", "Con it se usa doesn't, no don't."),
        ("abc", "{F} ¿Cuál es la palabra de tiempo que indica «ahora»?", "At the moment", "In summer", "In winter", "At the moment significa en este momento, o sea, ahora."),
    ],
    ctx=("abc", "En un taller de tu centro (ejemplo), una compañera dice en inglés: «Look! It's snowing.» ¿Qué está ocurriendo?", "Está nevando ahora", "Nieva todos los inviernos", "No hay nieve", "El presente continuo se usa para algo que ocurre ahora."),
    sc=[("¿Cómo digo «ahora está nevando»?", "It's snowing now.", "Ahora pide el presente continuo con -ing."),
        ("¿Qué forma uso para «en invierno nieva mucho»?", "It snows a lot in winter.", "Un hábito se dice en presente simple."),
        ("¿Qué quiero practicar la próxima semana?", "Elijo un tema y lo anoto", "Una meta propia ayuda a seguir aprendiendo.")],
    op=("Haz la revisión final: {F} Escribe en tu cuaderno un párrafo de cinco oraciones sobre tu ciudad de origen (datos de ejemplo): clima ahora, clima en general, adjetivos y un desafío. Después anota un logro y un paso siguiente.",
        "My city is hot and dry. It's sunny now. It doesn't rain a lot. A challenge is the drought. Achieved: it's + -ing. Next: more weather words.",
        ["escribe cinco oraciones", "usa los dos tiempos correctamente", "anota un logro y un paso siguiente"],
        ["cinco oraciones y dos frases de autoevaluación"],
        ["no anotar el paso siguiente", "mezclar presente continuo y simple"],
        "Pregunta: «¿Qué te cuesta más: ahora o siempre?»."),
    reinforce="Repasa la tarjeta de reglas de la clase 3 y escribe cuatro oraciones con now y con in winter.",
    extend="Escribe un parte del tiempo de ejemplo con tres lugares y léelo en voz alta a otra persona.",
)

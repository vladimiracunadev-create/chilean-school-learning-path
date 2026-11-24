"""Inglés EPJA Nivel 2, módulo 4 (parte 3): OAD-15, expresarse e investigar sobre nuevas maneras de alimentarse (leer, preguntar y escribir datos). Todos los textos son inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-15"

F1 = ("Text (example): Ana is 38 years old. For lunch she eats rice, chicken and salad. She wants to eat less sugar. Now she drinks water, not soda. "
      "Her neighbor, Mr. Reyes, is 64. He eats more vegetables and beans. He cooks at home every day. He doesn't eat fast food.")

F2 = ("Glossary (example). Plant-based food: food from plants, like vegetables, fruit, beans, lentils and rice. Less sugar: a smaller amount of sugar. "
      "Eat slowly: don't eat fast. Cook at home: make food in your own kitchen. "
      "Four new ways to eat (example). 1. Plant-based meals: eat beans and vegetables two days a week. 2. Less sugar: drink water or tea without sugar. "
      "3. Eat slowly: take twenty minutes for lunch. 4. Cook at home: use fresh vegetables.")

F3 = ("Survey form (example). Question 1: What do you eat for breakfast? Answer by Marta: I eat bread and tea. "
      "Question 2: Do you eat vegetables every day? Answer: Yes, I do. I eat salad at lunch. "
      "Question 3: How many glasses of water do you drink? Answer: I drink five glasses. "
      "Question 4: Do you drink soda? Answer: No, I don't.")

F4 = ("Class survey report (example). Five people answer our questions. Two people eat vegetables every day. Three people drink soda on weekends. "
      "Four people cook at home. One person eats plant-based food on Mondays. Nobody eats fast food every day.")

F5 = ("Notice in a workplace cafeteria (example). New menu on Tuesdays and Thursdays: plant-based lunch with beans, rice and salad. Price: 2,500 pesos (example price). "
      "Less sugar in the juice this month. Eat slowly: lunch time is 40 minutes. Ask Mrs. Rojas for more information.")

F6 = ("Mini report (example), «New ways to eat in my family». My mother eats more vegetables now. My brother drinks water, not soda. "
      "We cook at home on Sundays. We eat slowly at dinner. Conclusion: small changes are possible and useful.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya como cada día y leo un texto sobre dos personas que cambian su manera de alimentarse.",
    prior=["Digo hábitos con el presente simple.", "Conozco palabras de comida en inglés, como rice y bread.", "Sé que las costumbres de alimentación pueden cambiar."],
    explain=[
        "Alimentarse es parte de la vida diaria, y muchas personas quieren probar maneras nuevas de comer: más verduras, menos azúcar o cocinar en casa. Un texto sobre eso se lee igual que los otros: busca quién es, qué come y qué cambia.",
        "Para hablar de lo que comes usa el presente simple: She eats rice. He cooks at home every day. Con he, she e it el verbo lleva «-s». La expresión She wants to eat less sugar se aprende completa: significa «ella quiere comer menos azúcar».",
        "Las palabras more y less significan «más» y «menos». More vegetables es más verduras; less sugar es menos azúcar. Los textos de este cuaderno son ejemplos de vida diaria y no reemplazan la orientación de una persona profesional de la salud.",
    ],
    vocab=[("vegetables", "verduras"), ("beans", "porotos"), ("sugar", "azúcar"), ("soda", "bebida gaseosa"), ("more", "más"), ("less", "menos")],
    worked=[
        ("Decir una comida", "Ana come arroz, pollo y ensalada al almuerzo.", ["Sujeto she: el verbo lleva «-s»: eats.", "Agrego los alimentos y el momento."], "Ana eats rice, chicken and salad for lunch."),
        ("Decir un cambio", "El señor Reyes come más verduras.", ["Uso el verbo con «-s»: eats.", "Agrego more y vegetables."], "Mr. Reyes eats more vegetables."),
    ],
    mistakes=[("Escribir «He cook at home» sin la «-s».", "Con he el verbo del presente simple lleva «-s».", "Escribe He cooks at home."),
              ("Confundir more con less.", "More significa más y less significa menos, son contrarios.", "Revisa cuál de las dos palabras dice el texto.")],
    T=[
        ("abc", "{F} What does Ana eat for lunch?", "Rice, chicken and salad", "Beans and bread", "Fast food and soda", "El texto dice que ella come arroz, pollo y ensalada."),
        ("ab", "{F} What does Ana drink now?", "Water", "Soda", "El texto dice que ahora ella bebe agua y no gaseosa."),
        ("{F} How old is Mr. Reyes? Write the number.", "64", "El texto dice «Mr. Reyes, is 64»."),
        ("abc", "{F} What does Mr. Reyes eat more of?", "Vegetables and beans", "Sugar", "Chicken", "El texto dice que come más verduras y porotos."),
        ("ab", "{F} Where does Mr. Reyes cook every day?", "At home", "At work", "El texto dice «He cooks at home every day»."),
        ("abc", "{F} Which sentence is true?", "Mr. Reyes doesn't eat fast food", "Ana eats fast food every day", "Ana doesn't eat rice", "El texto dice que el señor Reyes no come comida rápida."),
        ("abc", "Complete: Ana ___ rice for lunch.", "eats", "eat", "eating", "Con Ana (she) el verbo lleva «-s»."),
        ("abc", "Complete: Mr. Reyes ___ more vegetables.", "eats", "eat", "eating", "Con Mr. Reyes (he) el verbo lleva «-s»."),
        ("abc", "What does «less sugar» mean?", "Menos azúcar", "Más azúcar", "Azúcar sin agua", "Less significa menos, entonces less sugar es menos azúcar."),
        ("Complete with one word: I want to eat ___ vegetables this week. (más)", "more", "Más se dice more en inglés."),
        ("ab", "Choose the correct sentence.", "He cooks at home every day", "He cook at home every day", "Con he el verbo cook lleva «-s»."),
        ("abc", "Put the words in order: eats / Ana / salad / for lunch", "Ana eats salad for lunch", "Ana eat salad for lunch", "Eats Ana salad for lunch", "El orden es sujeto, verbo, objeto y momento."),
        ("ab", "Make this sentence negative: «Ana drinks soda.»", "Ana doesn't drink soda", "Ana doesn't drinks soda", "Después de doesn't el verbo queda sin «-s»."),
    ],
    ctx=("abc", "En la fila del casino de tu trabajo, un compañero te pregunta qué cambias en tu comida. Quieres decir que comes más verduras. ¿Qué dices?", "I eat more vegetables", "I eats more vegetables", "I am eat more vegetables", "Con I el verbo no lleva «-s» ni am."),
    sc=[("En Inglés: ¿qué significan more y less?", "Más y menos", "More indica más cantidad y less indica menos cantidad."),
        ("En Inglés: ¿cómo escribes «Él cocina en casa»?", "He cooks at home", "Con he el verbo lleva «-s»."),
        ("En Inglés: ¿cómo niegas «She eats fast food»?", "She doesn't eat fast food", "Doesn't marca la negación y el verbo queda sin «-s».")],
    op=("Escribe en tu cuaderno cuatro oraciones sobre lo que comes o bebes y un cambio que te gustaría hacer. Usa more o less en una oración. No uses datos de salud reales.",
        "I eat rice and salad for lunch. I drink water every day. I want to eat less sugar. I eat more vegetables on Sundays.",
        ["usa cuatro oraciones con presente simple", "usa more o less en una", "el verbo va correcto con I"],
        ["cuatro oraciones escritas"],
        ["usar la «-s» con I", "dar consejos de salud o dietas"],
        "Pregunta: «¿Qué cambio pequeño me gustaría probar?»."),
    reinforce="Escribe tres alimentos que comes cada semana, con I eat.",
    extend="Escribe cuatro oraciones sobre los hábitos de comida de una persona inventada, con more y less.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo el vocabulario de las nuevas maneras de alimentarse: plant-based, less sugar, eat slowly y cook at home.",
    prior=["Digo lo que como y bebo.", "Reconozco more y less.", "Sé usar el presente simple con he y she."],
    explain=[
        "Las nuevas maneras de alimentarse son cambios pequeños de costumbre. Plant-based food es comida hecha con plantas: verduras, frutas, porotos, lentejas y arroz. Less sugar es usar menos azúcar. Eat slowly es comer despacio. Cook at home es cocinar en tu cocina.",
        "Para leer un glosario, busca la palabra que está al comienzo y lee su definición. En este texto, la palabra va seguida de dos puntos y de una explicación corta. Subraya la palabra clave de cada definición.",
        "Las cuatro maneras nuevas se escriben con el verbo básico: Eat beans, Drink water, Take twenty minutes, Use fresh vegetables. Es la expresión de instrucción que ya conoces, sin «-s». Cada una trae un dato con número, como two days a week.",
    ],
    vocab=[("plant-based", "hecho con plantas"), ("fruit", "fruta"), ("lentils", "lentejas"), ("fresh", "fresco"), ("slowly", "despacio"), ("kitchen", "cocina")],
    worked=[
        ("Leer una definición", "Texto: «Cook at home: make food in your own kitchen».", ["La palabra es cook at home.", "La definición dice make food in your own kitchen."], "Cocinar en casa es hacer comida en tu cocina"),
        ("Buscar un dato", "¿Cuántos minutos se toman para comer despacio?", ["Busco Eat slowly en el texto.", "Leo take twenty minutes for lunch."], "Veinte minutos"),
    ],
    mistakes=[("Pensar que plant-based significa «plantas para decorar».", "Aquí plant-based describe comida hecha con plantas.", "Lee la definición completa del glosario."),
              ("Confundir slowly con slow.", "Slowly explica cómo se hace algo; slow describe algo lento.", "Usa slowly después del verbo: Eat slowly.")],
    T=[
        ("abc", "{F} What is plant-based food?", "Food from plants, like vegetables and beans", "Food with a lot of sugar", "Food from a restaurant", "El glosario dice que es comida de plantas, como verduras y porotos."),
        ("ab", "{F} What does «less sugar» mean?", "A smaller amount of sugar", "A bigger amount of sugar", "El glosario define less sugar como una cantidad menor de azúcar."),
        ("{F} How many days a week do you eat plant-based meals in the example? Write the number.", "2", "La recomendación dice beans and vegetables two days a week."),
        ("abc", "{F} How many minutes do you take for lunch to eat slowly?", "Twenty", "Ten", "Forty", "El texto dice take twenty minutes for lunch."),
        ("abc", "{F} What do you drink for less sugar?", "Water or tea without sugar", "Soda", "Juice with sugar", "La segunda manera dice que bebas agua o té sin azúcar."),
        ("ab", "{F} What does «cook at home» mean?", "Make food in your own kitchen", "Buy food at a restaurant", "El glosario define cook at home como hacer comida en tu cocina."),
        ("abc", "What does «lentils» mean?", "Lentejas", "Lechugas", "Limones", "Lentils son lentejas, un alimento de plantas."),
        ("abc", "What does «fresh» mean?", "Fresco", "Frito", "Frío", "Fresh describe comida natural y en buen estado."),
        ("ab", "Choose the correct sentence.", "Eat slowly", "Eats slowly", "La instrucción usa el verbo básico, sin «-s»."),
        ("abc", "Complete: Mr. Reyes ___ plant-based meals on Mondays.", "eats", "eat", "eating", "Con Mr. Reyes (he) el verbo lleva «-s»."),
        ("abc", "{F} Which is one of the four new ways to eat?", "Cook at home", "Eat fast food", "Drink soda", "Cook at home es la cuarta manera nueva del texto."),
        ("ab", "{F} Which sentence is correct about the text?", "Plant-based meals include beans and vegetables", "Plant-based meals include only meat", "El texto relaciona lo plant-based con porotos y verduras."),
        ("abc", "Put the words in order: fresh / Use / vegetables", "Use fresh vegetables", "Fresh use vegetables", "Vegetables fresh use", "La instrucción empieza con el verbo y sigue el objeto."),
    ],
    ctx=("abc", "En el almuerzo del trabajo, una colega te pregunta qué es «plant-based». Quieres explicarle en inglés que es comida de plantas. ¿Qué dices?", "It is food from plants", "It is food from animals", "It is a place to cook", "Plant-based es comida hecha con plantas, como verduras y porotos."),
    sc=[("En Inglés: ¿qué significa «plant-based»?", "Hecho con plantas", "Plant-based describe comida de origen vegetal."),
        ("En Inglés: ¿cómo dices «cocinar en casa»?", "Cook at home", "Cook es cocinar y at home es en casa."),
        ("En Inglés: ¿qué significa «slowly»?", "Despacio", "Slowly explica cómo se hace una acción.")],
    op=("Escribe en tu cuaderno cuatro frases con las palabras nuevas de la clase: plant-based, less sugar, eat slowly y cook at home, cada una en una oración.",
        "I eat plant-based meals on Tuesdays. I want less sugar in my tea. Eat slowly at lunch. I cook at home on Sundays.",
        ["usa las cuatro expresiones", "las oraciones tienen sujeto y verbo", "el verbo va con «-s» solo con he, she o it"],
        ["cuatro oraciones escritas"],
        ["olvidar la «-s» con he o she", "copiar sin entender"],
        "Pregunta: «¿Cuál de estas expresiones uso más en mi vida diaria?»."),
    reinforce="Copia las cuatro maneras nuevas de comer y subraya el verbo de cada una.",
    extend="Escribe cinco alimentos de plantas que conoces con su nombre en inglés.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a investigar: hacer preguntas sobre la alimentación y anotar las respuestas en oraciones completas.",
    prior=["Entiendo vocabulario de alimentación.", "Sé usar Do y Does en preguntas.", "He preguntado a personas cercanas sobre sus costumbres."],
    explain=[
        "Investigar es juntar datos con preguntas. En inglés hay tres tipos de pregunta útiles hoy: What do you eat for breakfast? (qué), Do you drink soda? (sí o no) y How many glasses of water do you drink? (cuántos). How many se usa para contar cosas.",
        "Paso 1: escribe la pregunta con What, Do o How many. Paso 2: hazla a una persona de tu confianza. Paso 3: anota la respuesta en una oración completa, por ejemplo I drink five glasses. Si la respuesta es sí o no, usa la respuesta corta: Yes, I do. No, I don't.",
        "No preguntes datos personales delicados: tu investigación es sobre comidas y hábitos, no sobre dinero, enfermedades ni direcciones. Los datos de este cuaderno son inventados.",
    ],
    vocab=[("breakfast", "desayuno"), ("glass of water", "vaso de agua"), ("How many...?", "¿Cuántos o cuántas...?"), ("What do you eat?", "¿Qué comes?"), ("survey", "encuesta"), ("answer", "respuesta")],
    worked=[
        ("Hacer una pregunta de cantidad", "Quieres saber cuántos vasos de agua bebe una persona.", ["Empiezo con How many.", "Agrego glasses of water.", "Uso do you drink."], "How many glasses of water do you drink?"),
        ("Anotar una respuesta", "Marta dice que bebe cinco vasos.", ["Uso I drink.", "Agrego el número y glasses."], "I drink five glasses."),
    ],
    mistakes=[("Escribir «How many glasses do you drinks?».", "Después de do el verbo queda sin «-s».", "Escribe do you drink."),
              ("Anotar solo «five» sin oración.", "Una oración completa deja claro el dato para quien lea.", "Escribe I drink five glasses.")],
    T=[
        ("abc", "{F} What does Marta eat for breakfast?", "Bread and tea", "Rice and soda", "Salad", "Marta responde I eat bread and tea."),
        ("{F} How many glasses of water does Marta drink? Write the number.", "5", "Ella responde I drink five glasses."),
        ("ab", "{F} Does Marta eat vegetables every day?", "Yes, she does", "No, she doesn't", "Marta responde Yes, I do. I eat salad at lunch."),
        ("abc", "{F} When does Marta eat salad?", "At lunch", "At breakfast", "At dinner", "Ella dice I eat salad at lunch."),
        ("ab", "{F} Does Marta drink soda?", "No, she doesn't", "Yes, she does", "Marta responde con una negación corta: No, I don't."),
        ("abc", "Which question asks about a number?", "How many glasses of water do you drink?", "What do you eat for breakfast?", "Do you drink soda?", "How many se usa para preguntar cantidades."),
        ("abc", "Complete: ___ you eat vegetables every day?", "Do", "Does", "Are", "Con you se usa Do en el presente simple."),
        ("abc", "Complete: What ___ you eat for breakfast?", "do", "does", "are", "Con you se usa do en preguntas con What."),
        ("ab", "Choose the correct sentence to write Marta's answer.", "She drinks five glasses of water", "She drink five glasses of water", "Con she el verbo lleva «-s»."),
        ("abc", "Put the words in order: many / How / do / glasses / you / drink", "How many glasses do you drink", "How glasses many do you drink", "Many how glasses you do drink", "La pregunta empieza con How many y sigue do you."),
        ("ab", "Choose the correct short answer to «Do you drink soda?» (no).", "No, I don't", "No, I doesn't", "Con I la respuesta negativa es don't."),
        ("abc", "Spot the error: «Do you eats vegetables every day?» Which sentence corrects it?", "Do you eat vegetables every day?", "Does you eat vegetables every day?", "Do you eating vegetables every day?", "Después de Do el verbo queda sin «-s»."),
        ("abc", "Your neighbor Rosa says «I drink three glasses of water.» Which sentence reports the data?", "She drinks three glasses of water", "She drink three glasses of water", "She is three glasses of water", "Con she el verbo drink lleva «-s»."),
    ],
    ctx=("abc", "Para la encuesta del curso quieres preguntar a un compañero cuántos vasos de jugo toma en la semana. ¿Qué preguntas?", "How many glasses of juice do you drink in a week?", "How many glasses of juice you drink in a week?", "How many glasses of juice does you drink in a week?", "La pregunta usa How many y do you."),
    sc=[("En Inglés: ¿cuándo usas How many?", "Para preguntar cantidades", "How many se usa con cosas que se pueden contar."),
        ("En Inglés: ¿cómo respondes sí a «Do you eat vegetables?»", "Yes, I do", "La respuesta corta repite el auxiliar."),
        ("En Inglés: ¿lleva «-s» el verbo después de Do you?", "No", "Do ya marca la pregunta y el verbo queda básico.")],
    op=("Escribe cuatro preguntas para una encuesta de alimentación con What, Do y How many. Hazlas a una persona de confianza y anota las respuestas en oraciones completas.",
        "What do you eat for lunch? Do you drink soda? How many glasses of water do you drink? Do you cook at home? Respuesta: I eat rice and salad.",
        ["usa What, Do y How many", "las preguntas están bien formadas", "anota respuestas en oraciones completas"],
        ["cuatro preguntas y cuatro respuestas escritas"],
        ["usar la «-s» después de Do", "preguntar datos delicados"],
        "Pregunta: «¿Qué dato de la encuesta me sorprendió?»."),
    reinforce="Escribe tres preguntas con Do you... sobre comida.",
    extend="Inventa cinco respuestas de una persona a tu encuesta, con oraciones completas.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: leo un informe de encuesta, saco datos y escribo oraciones con números.",
    prior=["Sé preguntar con What, Do y How many.", "Entiendo los números hasta 20.", "Sé escribir respuestas completas."],
    explain=[
        "Un informe de encuesta dice cuántas personas respondieron y qué respondieron. Se escribe con números y verbos en presente simple: Two people eat vegetables every day. Con people el verbo no lleva «-s».",
        "Los números pequeños se escriben con palabra: one, two, three, four, five. La palabra nobody significa «nadie» y lleva el verbo con «-s»: Nobody eats fast food every day. Al leer, anota cada número con su dato.",
        "Para comparar datos usa more y less: More people drink soda on weekends than eat plant-based food. Aquí lo aprendes como expresión y lees los datos sin cálculos difíciles. Todos los datos son inventados.",
    ],
    vocab=[("people", "personas"), ("nobody", "nadie"), ("on weekends", "los fines de semana"), ("survey", "encuesta"), ("report", "informe"), ("answer", "responder")],
    worked=[
        ("Leer un dato", "El informe dice: «Two people eat vegetables every day».", ["Two es el número de personas.", "El verbo eat va sin «-s» con people."], "Dos personas comen verduras cada día"),
        ("Escribir un dato", "De cinco personas, tres toman gaseosa los fines de semana.", ["Número: three.", "Sujeto: people, verbo drink.", "Agrego on weekends."], "Three people drink soda on weekends."),
    ],
    mistakes=[("Escribir «Two people eats vegetables».", "Con people el verbo no lleva «-s».", "Escribe Two people eat vegetables."),
              ("Mezclar los números dos y tres.", "Two y three son distintos y se parecen al leer rápido.", "Anota el número con letra y con cifra: two, 2.")],
    T=[
        ("{F} How many people answer the survey? Write the number.", "5", "El informe dice Five people answer our questions."),
        ("{F} How many people eat vegetables every day? Write the number.", "2", "El informe dice que dos personas comen verduras cada día."),
        ("abc", "{F} How many people drink soda on weekends?", "Three", "Two", "Four", "El informe dice Three people drink soda on weekends."),
        ("abc", "{F} How many people cook at home?", "Four", "One", "Five", "El informe dice Four people cook at home."),
        ("ab", "{F} Who eats plant-based food on Mondays?", "One person", "Nobody", "El informe dice que una persona come comida de plantas los lunes."),
        ("ab", "{F} Which sentence is true?", "Nobody eats fast food every day", "Everyone eats fast food every day", "El informe dice Nobody eats fast food every day."),
        ("abc", "Complete: Two people ___ vegetables every day.", "eat", "eats", "eating", "Con people el verbo no lleva «-s»."),
        ("abc", "Complete: Nobody ___ fast food every day.", "eats", "eat", "eating", "Con nobody el verbo lleva «-s»."),
        ("abc", "What does «nobody» mean?", "Nadie", "Todos", "Alguien", "Nobody significa que ninguna persona hace algo."),
        ("ab", "{F} Which sentence is correct?", "More people cook at home than drink soda on weekends", "More people drink soda than cook at home", "Cuatro personas cocinan en casa y tres toman gaseosa."),
        ("abc", "Write the data in a correct sentence: 3 of 5 people drink water every day.", "Three people drink water every day", "Three people drinks water every day", "Three people is drink water every day", "Con people el verbo queda sin «-s»."),
        ("abc", "Put the words in order: cook / Four / at home / people", "Four people cook at home", "Four people cooks at home", "People four cook at home", "El orden es número, sujeto, verbo y lugar."),
        ("ab", "Spot the error and choose the correct sentence: «One person eat plant-based food.»", "One person eats plant-based food", "One person eating plant-based food", "Con one person (she o he) el verbo lleva «-s»."),
    ],
    ctx=("abc", "En tu curso, 4 de 6 compañeros llegan en bus al centro. Quieres escribirlo en el informe de la encuesta. ¿Qué escribes?", "Four people come to the center by bus", "Four people comes to the center by bus", "Four people is come to the center by bus", "Con people el verbo queda sin «-s»."),
    sc=[("En Inglés: ¿lleva «-s» el verbo con people?", "No", "People es plural y su verbo no lleva «-s»."),
        ("En Inglés: ¿cómo se dice «nadie»?", "Nobody", "Nobody significa que ninguna persona hace algo."),
        ("En Inglés: ¿cómo escribes 3 con palabra?", "Three", "Los números del 1 al 5 son one, two, three, four y five.")],
    op=("Escribe un informe de cinco oraciones con datos inventados de una encuesta a seis personas sobre lo que comen y beben. Usa números con palabras y People.",
        "Six people answer our survey. Four people eat vegetables every day. Two people drink soda on weekends. Five people cook at home. Nobody eats fast food every day.",
        ["incluye cinco oraciones con números", "usa people sin «-s»", "usa nobody una vez"],
        ["informe escrito de cinco oraciones"],
        ["usar la «-s» con people", "usar datos reales de personas"],
        "Pregunta: «¿Qué dato de mi informe es el más importante?»."),
    reinforce="Lee el informe y subraya los números con un lápiz de color.",
    extend="Agrega al informe dos datos inventados sobre bebidas.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a un contexto de trabajo: leo un aviso de un casino y escribo una pregunta e información para compañeros.",
    prior=["Leo datos con números y precios.", "Sé preguntar con What y How many.", "Entiendo vocabulario de alimentación."],
    explain=[
        "En muchos trabajos hay un casino o un lugar para almorzar con avisos sobre el menú. Un aviso dice qué hay, cuándo, cuánto cuesta y a quién consultar. Lee primero los días y los precios.",
        "Los días van con on: on Tuesdays and Thursdays. El precio va con pesos: 2,500 pesos, que es un precio de ejemplo y no uno real. La frase Ask Mrs. Rojas for more information es una instrucción: usa el verbo básico.",
        "Si quieres más información, puedes escribir una pregunta breve: What time is lunch? How much is the plant-based lunch? How much sirve para preguntar el precio. Es una expresión completa que aprendes hoy.",
    ],
    vocab=[("menu", "menú"), ("price", "precio"), ("How much is...?", "¿Cuánto cuesta...?"), ("lunch time", "hora de almuerzo"), ("information", "información"), ("this month", "este mes")],
    worked=[
        ("Leer un precio", "El aviso dice: «Price: 2,500 pesos (example price)».", ["Price es precio.", "2,500 es el número.", "Example price avisa que es un ejemplo."], "El precio de ejemplo es 2.500 pesos"),
        ("Preguntar el precio", "Quieres saber cuánto cuesta el almuerzo de plantas.", ["Empiezo con How much is.", "Agrego the plant-based lunch."], "How much is the plant-based lunch?"),
    ],
    mistakes=[("Escribir «How many is the lunch?» para preguntar el precio.", "How many se usa para contar cosas; para precio se usa How much.", "Usa How much is...? para preguntar cuánto cuesta."),
              ("Olvidar on antes del día.", "Con días de la semana se usa on.", "Escribe on Tuesdays.")],
    T=[
        ("abc", "{F} On which days is the plant-based lunch?", "Tuesdays and Thursdays", "Mondays and Fridays", "Every day", "El aviso dice New menu on Tuesdays and Thursdays."),
        ("ab", "{F} What is the main food of the plant-based lunch?", "Beans, rice and salad", "Chicken and soda", "El aviso lista porotos, arroz y ensalada."),
        ("{F} How many minutes is lunch time? Write the number.", "40", "El aviso dice lunch time is 40 minutes."),
        ("abc", "{F} Who should you ask for more information?", "Mrs. Rojas", "Mr. Reyes", "Ana", "El aviso dice Ask Mrs. Rojas for more information."),
        ("ab", "{F} What changes in the juice this month?", "It has less sugar", "It has more sugar", "El aviso dice Less sugar in the juice this month."),
        ("abc", "{F} Which sentence is an instruction in the notice?", "Eat slowly", "The menu is new", "Lunch is plant-based", "La instrucción usa el verbo en forma básica."),
        ("abc", "What does «price» mean?", "Precio", "Premio", "Presión", "Price es el valor que se paga por algo."),
        ("abc", "Complete: ___ is the plant-based lunch?", "How much", "How many", "How old", "How much se usa para preguntar el precio."),
        ("ab", "Choose the correct question.", "How much is the juice?", "How many is the juice?", "Para el precio se usa How much."),
        ("abc", "Complete: The new menu is ___ Tuesdays.", "on", "at", "in", "Con días de la semana se usa on."),
        ("ab", "Choose the correct sentence.", "Ask Mrs. Rojas for more information", "Asks Mrs. Rojas for more information", "La instrucción usa el verbo básico sin «-s»."),
        ("abc", "{F} What is the main idea of the notice?", "A new plant-based lunch and less sugar at the cafeteria", "A job offer", "A sale of cooking tools", "El aviso informa un menú nuevo con menos azúcar."),
        ("abc", "Put the words in order: the / is / lunch / How much / ?", "How much is the lunch?", "How is much the lunch?", "Much how is the lunch?", "La pregunta empieza con How much y sigue is."),
    ],
    ctx=("abc", "En el casino de tu trabajo hay un menú nuevo y quieres saber cuánto cuesta el almuerzo. ¿Qué preguntas a la encargada?", "How much is the lunch?", "How many is the lunch?", "How is the lunch much?", "How much se usa para preguntar el precio."),
    sc=[("En Inglés: ¿cómo preguntas el precio?", "How much is...?", "How much sirve para preguntar cuánto cuesta algo."),
        ("En Inglés: ¿qué preposición usas con los días?", "on", "Se dice on Tuesdays y on Mondays."),
        ("En Inglés: ¿qué significa «this month»?", "Este mes", "This month indica el mes actual.")],
    op=("Escribe un aviso de cinco líneas para el casino de un trabajo inventado: un menú nuevo, los días, un precio de ejemplo, una instrucción y a quién preguntar. Escribe también una pregunta con How much.",
        "New plant-based menu on Wednesdays: beans, rice and salad. Price: 2,000 pesos (example price). Eat slowly. Ask Mr. Díaz. Pregunta: How much is the juice?",
        ["incluye días con on y un precio de ejemplo", "una instrucción con verbo básico", "una pregunta con How much"],
        ["aviso y pregunta escritos"],
        ["usar How many para el precio", "olvidar que el precio es de ejemplo"],
        "Pregunta: «¿Qué información dejaría claro mi aviso a una persona nueva?»."),
    reinforce="Lee el aviso y copia el precio, el día y la hora.",
    extend="Escribe una segunda pregunta para Mrs. Rojas sobre el menú, con What time o How much.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo aprendido: leo un informe breve de alimentación, escribo el mío con datos propios y decido qué sigo practicando.",
    prior=["Pregunto con What, Do y How many.", "Escribo datos con presente simple.", "Entiendo more y less."],
    explain=[
        "Un informe breve de alimentación tiene un título, tres o cuatro datos y una conclusión. Los datos usan el presente simple y números. La conclusión resume lo más importante: Small changes are possible and useful.",
        "Para escribirlo, haz tres pasos: elige un título, escribe los datos que juntaste con tu encuesta y termina con una conclusión de una línea. Revisa: ¿puse la «-s» con he o she?, ¿escribí los números con palabra?, ¿mi conclusión se apoya en los datos?",
        "Este módulo termina con tu informe. No hay un solo cambio correcto: cada familia y cada persona decide. Lo importante es leer, investigar y escribir con claridad. Tus próximos pasos pueden ser leer etiquetas en inglés o preguntar a un compañero.",
    ],
    vocab=[("conclusion", "conclusión"), ("small", "pequeño"), ("changes", "cambios"), ("family", "familia"), ("useful", "útil")],
    worked=[
        ("Escribir un dato con he o she", "Mi hermano toma agua y no gaseosa.", ["Sujeto he: el verbo lleva «-s»: drinks.", "Agrego water, not soda."], "My brother drinks water, not soda."),
        ("Escribir una conclusión", "Quieres decir que los cambios pequeños sirven.", ["Escribo Small changes.", "Agrego are possible and useful."], "Small changes are possible and useful."),
    ],
    mistakes=[("Escribir «We cooks at home on Sundays».", "Con we el verbo no lleva «-s».", "Escribe We cook at home on Sundays."),
              ("Terminar el informe sin conclusión.", "La conclusión dice qué significan los datos.", "Agrega una oración final que resuma.")],
    T=[
        ("abc", "{F} What does the writer's mother eat more now?", "Vegetables", "Sugar", "Fast food", "El informe dice que su mamá come más verduras ahora."),
        ("ab", "{F} What does the writer's brother drink?", "Water, not soda", "Soda, not water", "El informe dice que su hermano bebe agua y no gaseosa."),
        ("abc", "{F} When does the family cook at home?", "On Sundays", "On Mondays", "Every day", "El informe dice We cook at home on Sundays."),
        ("ab", "{F} How does the family eat at dinner?", "Slowly", "Fast", "El informe dice We eat slowly at dinner."),
        ("abc", "{F} What is the conclusion of the report?", "Small changes are possible and useful", "Nobody changes", "Big changes cost a lot", "La conclusión dice que los cambios pequeños sirven."),
        ("abc", "{F} Which sentence is true?", "The family eats slowly at dinner", "The family eats fast at dinner", "The family never cooks", "El informe afirma que cenan despacio."),
        ("abc", "Complete: My mother ___ more vegetables now.", "eats", "eat", "eating", "Con my mother (she) el verbo lleva «-s»."),
        ("abc", "Complete: We ___ at home on Sundays.", "cook", "cooks", "cooking", "Con we el verbo no lleva «-s»."),
        ("ab", "Choose the correct sentence.", "My brother drinks water", "My brother drink water", "Con my brother (he) el verbo lleva «-s»."),
        ("abc", "Which sentence is a good conclusion for a food report?", "Small changes are useful", "The price is 2,000 pesos", "Ask Mrs. Rojas", "Una conclusión resume el sentido de los datos."),
        ("ab", "Spot the error and choose the correct sentence: «We cooks at home on Sundays.»", "We cook at home on Sundays", "We cooking at home on Sundays", "Con we el verbo no lleva «-s»."),
        ("abc", "Put the words in order: slowly / We / eat / at dinner", "We eat slowly at dinner", "We eats slowly at dinner", "Slowly we at dinner eat", "El orden es sujeto, verbo, modo y momento."),
        ("abc", "What does «useful» mean?", "Útil", "Usual", "Inútil", "Useful describe algo que sirve para algo."),
    ],
    ctx=("abc", "Para el informe final del curso, quieres escribir, con datos de ejemplo, que en tu grupo comen más despacio en la cena. ¿Qué escribes?", "We eat slowly at dinner", "We eats slowly at dinner", "We are eat slowly at dinner", "Con we el verbo no lleva «-s» ni are."),
    sc=[("En Inglés: ¿qué partes tiene un informe breve?", "Título, datos y conclusión", "Esas tres partes hacen un informe claro."),
        ("En Inglés: ¿cómo dices «Mi hermano toma agua»?", "My brother drinks water", "Con he el verbo lleva «-s»."),
        ("En Inglés: ¿qué significa «small changes»?", "Cambios pequeños", "Small es pequeño y changes son cambios.")],
    op=("Escribe en tu cuaderno un informe de seis a siete oraciones: título, cuatro datos de tu encuesta o inventados (con he, she o we) y una conclusión. Léelo a alguien de confianza.",
        "New ways to eat in my neighborhood. My neighbor eats more beans. Her son drinks water, not soda. We cook at home on Sundays. Nobody eats fast food every day. Conclusion: small changes are useful.",
        ["incluye título, cuatro datos y conclusión", "usa bien la «-s» con he o she", "usa números con palabra"],
        ["informe escrito y leído en voz alta"],
        ["olvidar la conclusión", "usar datos personales reales"],
        "Pregunta: «¿Qué cambio de mi informe es el que más me gusta?»."),
    reinforce="Corrige tu informe revisando todos los verbos con he o she.",
    extend="Escribe una segunda conclusión para el mismo informe con otras palabras.",
)

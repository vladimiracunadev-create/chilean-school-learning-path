"""Inglés EPJA Nivel 2, módulo 2 (OAD-05): leer y comentar un texto sobre hábitos de alimentación y presentar los propios y los de alguien cercano. Textos inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-05"

F1 = ("Text 1 (example): Carlos works at a warehouse. He gets up at 6:00. For breakfast he eats bread and drinks tea. "
      "At 1:00 he has lunch: rice, chicken and vegetables. He drinks water, not soda. At night he has a light dinner with his wife, Ana.")

F2 = ("Shopping list (example), Marta's family: 1 kilogram of rice. 1 kilogram of bread. 6 eggs. 3 bottles of water. "
      "A lot of vegetables: carrots, tomatoes and onions. Some fruit. No soda.")

F3 = ("Rule card (example): I eat, you eat, we eat, they eat. He eats, she eats, it eats. "
      "Negative: I don't eat meat. She doesn't eat meat. Questions: Do you eat fish? Does he eat fish? Short answers: Yes, I do. No, he doesn't.")

F4 = ("Text 2 (example), Marta's habits: My name is Marta. I'm a cook at a small restaurant. I eat breakfast at 7:00. I eat bread with cheese and I drink coffee. "
      "For lunch I eat soup and salad. I don't eat meat. My son Luis eats breakfast at 8:00. He doesn't drink coffee; he drinks milk. We eat dinner together at 8:30.")

F5 = ("Notice (example), Community Kitchen: Monday to Friday. Lunch is at 1:00. Today: rice, beans and salad. Drinks: water or juice. "
      "Please bring your own cup. No takeout. Volunteers eat at 12:30.")

F6 = ("Text 3 (example): Mary is from Chile. She eats a big lunch at 2:00: rice, chicken and salad. She doesn't eat dinner late. "
      "Her brother John is a bus driver. He eats breakfast at 5:30 and drinks a lot of coffee. He doesn't eat bread. At home they drink water with every meal.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy leo un texto corto en inglés sobre comidas, busco las palabras clave y digo de qué trata, partiendo de lo que ya sé.",
    prior=["Conozco palabras de comida que se usan en la calle y en los envases.", "Sé leer una hora, como 6:00.", "Puedo decir de qué trata un texto en español."],
    explain=[
        "Tú ya sabes mucho sobre comida: qué comes, a qué hora y con quién. Eso te ayuda a entender un texto en inglés aunque no conozcas todas las palabras.",
        "Para leer un texto nuevo, usa tres pasos. Primero lee el título y mira los números. Segundo, subraya las palabras clave: nombres de comidas, bebidas y horas. Tercero, pregúntate de qué trata en general.",
        "Un texto sencillo sobre hábitos cuenta qué hace una persona cada día. En este texto, Carlos come pan, arroz y verduras. Con eso ya sabes que el tema son las comidas del día.",
        "Hoy también repasamos el verbo to be: «Carlos is a worker» (Carlos es trabajador). No hace falta entender cada palabra para entender la idea general.",
    ],
    vocab=[("breakfast", "desayuno"), ("lunch", "almuerzo"), ("dinner", "cena"), ("bread", "pan"), ("rice", "arroz"), ("water", "agua"), ("vegetables", "verduras")],
    worked=[
        ("Subrayar palabras clave", "Text 1 (example): «He eats bread and drinks tea.»", ["Busco las comidas y bebidas: bread (pan) y tea (té).", "Busco el verbo: eats (come), drinks (toma).", "Entiendo la idea: come pan y toma té."], "Palabras clave: bread, tea"),
        ("Decir de qué trata", "Text 1 (example), todo el texto.", ["Veo palabras como breakfast, lunch y dinner.", "Veo comidas y horas.", "Concluyo: el texto trata de las comidas de Carlos durante el día."], "Tema general: las comidas de un día"),
    ],
    mistakes=[("Detenerme en cada palabra que no conozco.", "Se pierde la idea general y la lectura se vuelve muy lenta.", "Sigue leyendo, subraya lo que sí entiendes y vuelve después a la palabra difícil."),
              ("Escribir «Carlos are a worker».", "El verbo to be cambia con la persona: con he, she, it se usa is.", "Con Carlos (he) escribe is: «Carlos is a worker».")],
    T=[
        ("abc", "{F} What is the text about?", "Carlos's meals and drinks during the day", "A recipe for chicken", "A list of jobs in a warehouse", "El texto nombra breakfast, lunch y dinner, así que habla de las comidas del día."),
        ("ab", "{F} What does Carlos eat for breakfast?", "Bread", "Rice", "El texto dice que en el desayuno come pan; el arroz es del almuerzo."),
        ("{F} What time does Carlos get up? Escribe solo la hora, por ejemplo 9:00.", "6:00", "La primera hora del texto es la de levantarse: 6:00."),
        ("abc", "{F} What does Carlos drink with lunch?", "Water", "Soda", "Tea", "El texto dice «He drinks water, not soda»; el té es del desayuno."),
        ("ab", "{F} Which sentence is true?", "Carlos has dinner with his wife.", "Carlos has dinner alone.", "El texto dice que cena con su esposa Ana, por lo tanto no está solo."),
        ("abc", "{F} En el texto, «dinner» es la comida de la noche. ¿Cómo se dice en español?", "Cena", "Desayuno", "Almuerzo", "Dinner es la comida de la noche, es decir, la cena."),
        ("abc", "Lees una nota pegada en la cocina de tu trabajo (ejemplo): «Lunch today: soup and bread. Drink: juice.» ¿Cuál es la bebida?", "Juice", "Soup", "Bread", "Después de Drink aparece juice; soup y bread son comidas."),
        ("abc", "{F} Quieres saber qué come Carlos en el almuerzo. ¿Qué palabras subrayas?", "rice, chicken and vegetables", "6:00 and warehouse", "wife and Ana", "Las palabras clave del almuerzo siguen a «lunch»: arroz, pollo y verduras."),
        ("abc", "Alguien dice en español: «Él come pan». ¿Cuál es la oración correcta en inglés?", "He eats bread.", "He drinks bread.", "I eat bread.", "He es él y eats es come; drinks no sirve con bread."),
        ("{F} How many meals does the text name (breakfast, lunch, dinner)? Escribe el número.", "3", "Se nombran tres comidas: breakfast, lunch y dinner."),
        ("ab", "{F} Does Carlos drink soda with lunch?", "No, he drinks water.", "Yes, he drinks soda.", "El texto dice «water, not soda», o sea que no toma bebida gaseosa."),
        ("abc", "{F} Who is Ana?", "Carlos's wife", "Carlos's boss", "Carlos's sister", "El texto dice «with his wife, Ana», entonces Ana es su esposa."),
        ("ab", "Elige la oración con to be correcta para presentar a Carlos.", "Carlos is a worker.", "Carlos are a worker.", "Con he, she e it el verbo to be es is, no are."),
    ],
    ctx=("abc", "En tu trabajo hay un cartel (ejemplo) en inglés en el comedor: «Rice, chicken, salad. Water or juice.» Quieres saber qué bebidas hay. ¿Cuáles son?", "Water or juice", "Rice or chicken", "Salad or juice and rice", "Las bebidas son las palabras que siguen a la comida: water y juice."),
    sc=[("En inglés, ¿qué significa «lunch»?", "Almuerzo", "Lunch es la comida del mediodía."),
        ("¿Qué haces primero para entender un texto nuevo en inglés?", "Leo el título, miro números y subrayo palabras clave", "Esos pasos ayudan a captar la idea general sin leer cada palabra."),
        ("Completa con is o are: Ana ___ a cook.", "is", "Con Ana (she) se usa is, la forma de to be para una persona.")],
    op=("Lee otra vez el Text 1: {F} Escribe en tu cuaderno tres oraciones simples sobre tus comidas, por ejemplo con «I eat...» y «I drink...». Usa datos de ejemplo si prefieres no contar los tuyos.",
        "I eat bread for breakfast. I drink tea. I eat rice for lunch.",
        ["escribe tres oraciones en inglés", "usa I eat / I drink con una comida o bebida", "usa al menos una palabra del vocabulario"],
        ["tres oraciones cortas"],
        ["escribir «I eats»", "dejar la oración sin comida o bebida"],
        "Pregunta: «¿Qué comes tú en el desayuno y qué tomas?»."),
    reinforce="Lee de nuevo el Text 1 y subraya tres comidas y dos bebidas.",
    extend="Busca en un envase o cartel de tu casa dos palabras de comida en inglés y anótalas con su significado.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras de comidas y cantidades para leer una lista de compras y decir cuánto necesito.",
    prior=["Sé nombrar comidas y bebidas básicas.", "Sé contar hasta diez en inglés.", "Entiendo una lista de compras sencilla."],
    explain=[
        "Para hablar de alimentos necesitas palabras de comida y palabras de cantidad. Algunas cantidades son números: one kilogram, six eggs, three bottles. Otras son expresiones: some y a lot of.",
        "«Some» significa algo de o algunos: some fruit, some carrots. «A lot of» significa mucho o muchos: a lot of vegetables. «No» significa nada de: no soda.",
        "Para medir líquidos y alimentos usamos «of»: a kilogram of rice, a bottle of water, a glass of milk. Después de «of» va la comida: a bottle of water.",
        "Sobre el peso: en Chile se compra por kilogramo (kilo, kg). En Estados Unidos se usa la libra (pound, lb): a pound of rice son unos 450 gramos. En este cuaderno usamos kilogram, que se entiende en todas partes.",
        "Los alimentos que se cuentan llevan -s con varios: one egg, six eggs; one tomato, three tomatoes. El arroz o el agua no se cuentan: no decimos «three rices».",
    ],
    vocab=[("eggs", "huevos"), ("carrots", "zanahorias"), ("tomatoes", "tomates"), ("onions", "cebollas"), ("some", "algo de, algunos"), ("a lot of", "mucho, muchos"), ("a bottle of", "una botella de"), ("a kilogram of", "un kilogramo (un kilo) de")],
    worked=[
        ("Leer cantidades", "Shopping list (example): «6 eggs. 3 bottles of water.»", ["6 eggs: seis huevos.", "3 bottles of water: tres botellas de agua.", "Eggs y bottles llevan -s porque son varios."], "Seis huevos y tres botellas de agua"),
        ("Usar some y a lot of", "Quieres decir: «Necesito algo de fruta y muchas verduras».", ["Algo de fruta: some fruit.", "Muchas verduras: a lot of vegetables.", "Uno las dos ideas: I need some fruit and a lot of vegetables."], "I need some fruit and a lot of vegetables."),
    ],
    mistakes=[("Escribir «three tomato».", "Con tres o más, el sustantivo que se cuenta lleva -s.", "Escribe three tomatoes."),
              ("Decir «a bottle water».", "Falta la palabra «of» entre la medida y la comida.", "Escribe a bottle of water.")],
    T=[
        ("{F} How many eggs are on the list? Escribe el número.", "6", "La lista dice «6 eggs», es decir, seis huevos."),
        ("abc", "{F} How much rice is on the list?", "One kilogram", "Three kilograms", "Six kilograms", "La lista dice «1 kilogram of rice», o sea, un kilogramo."),
        ("ab", "{F} How many bottles of water are on the list?", "Three bottles", "Six bottles", "Dice «3 bottles of water», tres botellas; el seis son los huevos."),
        ("abc", "{F} Which vegetables are on the list?", "Carrots, tomatoes and onions", "Rice, bread and eggs", "Water, juice and soda", "Después de «vegetables» la lista nombra zanahorias, tomates y cebollas."),
        ("ab", "{F} «A lot of vegetables» significa:", "Muchas verduras", "Pocas verduras", "A lot of expresa una cantidad grande, no pequeña."),
        ("abc", "{F} En «Some fruit», la palabra «some» significa:", "Algo de", "Ninguna", "Muchísima", "Some indica una cantidad que no es grande ni cero: algo de fruta."),
        ("ab", "{F} «No soda» significa que:", "No hay gaseosa en la lista", "Hay mucha gaseosa en la lista", "La palabra «no» indica que no se necesita esa comida."),
        ("abc", "Compras para una fiesta de barrio. Quieres decir «tres huevos». ¿Cómo se escribe?", "Three eggs", "Three egg", "Threes eggs", "Con tres, el sustantivo va en plural con -s: eggs."),
        ("abc", "Completa: I drink a glass of ___ with lunch.", "water", "carrots", "bread", "Un vaso de se usa con líquidos como water."),
        ("ab", "Elige la oración correcta.", "I eat three tomatoes.", "I eat three rice.", "El arroz no se cuenta, pero los tomates sí se cuentan."),
        ("abc", "Marta dice: «We eat a lot of vegetables.» ¿Qué come su familia?", "Muchas verduras", "Pocas verduras", "Ninguna verdura", "A lot of significa mucho, así que comen muchas verduras."),
        ("{F} En la lista de Marta, ¿cómo se escribe «arroz» en inglés? Escribe una palabra.", "rice", "La lista dice «1 kilogram of rice»; arroz es rice."),
        ("ab", "Elige la oración correcta para pedir la compra.", "We need some carrots.", "We need a lot carrots.", "Antes de un sustantivo, a lot necesita «of»: a lot of carrots."),
    ],
    ctx=("abc", "En el almacén del barrio (ejemplo) ves un cartel: «Onions: one kilogram. Eggs: six.» Quieres comprar lo mismo que dice el cartel. ¿Qué compras?", "Un kilo de cebollas y seis huevos", "Seis kilos de cebollas y un huevo", "Un kilo de huevos y seis cebollas", "El cartel asocia one kilogram con onions y six con eggs."),
    sc=[("¿Qué significa «a lot of» en inglés?", "Mucho o muchos", "A lot of se usa para cantidades grandes."),
        ("¿Cómo se dice «una botella de agua»?", "A bottle of water", "Entre la botella y el agua va la palabra of."),
        ("Completa: three ___ (tomato).", "tomatoes", "Con tres o más se usa el plural, que en tomato se forma con -es.")],
    op=("Mira la lista de Marta: {F} Escribe en tu cuaderno una lista de compras de ejemplo para tu casa con cinco cosas: usa números, some y a lot of, y por lo menos una vez «of».",
        "Shopping list (example): 1 kilogram of rice. 4 eggs. 2 bottles of water. Some fruit. A lot of onions.",
        ["escribe cinco cosas", "usa al menos un número y some o a lot of", "usa of una vez"],
        ["una lista de cinco líneas"],
        ["escribir «a bottle water»", "olvidar el plural en eggs o tomatoes"],
        "Pregunta: «¿Qué cosas necesitas más y cuáles menos?»."),
    reinforce="Mira la despensa de tu casa y escribe tres comidas con su cantidad, como «two kilograms of rice».",
    extend="Escribe una lista de compras para una once de cuatro personas, usando some y a lot of.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a decir lo que como y lo que no como con el presente simple, en afirmativo, negativo y pregunta.",
    prior=["Sé decir «I eat» y «I drink».", "Conozco las personas: I, you, he, she, we, they.", "Puedo decir si una oración es afirmación o pregunta."],
    explain=[
        "El presente simple sirve para hablar de hábitos: lo que haces siempre o cada día. En afirmativo, el verbo queda igual con I, you, we y they: I eat, they eat.",
        "Con he, she e it, el verbo termina en -s: he eats, she drinks. Esa -s final es muy importante en inglés: no la olvides al escribir ni al decir la frase.",
        "Para decir que no, usa don't con I, you, we, they y doesn't con he, she, it: I don't eat meat, she doesn't eat meat. Después de don't y doesn't el verbo no lleva -s.",
        "Para preguntar, empieza con Do o Does: Do you eat fish? Does he eat fish? La respuesta corta es Yes, I do. o No, he doesn't.",
    ],
    vocab=[("eat", "comer"), ("drink", "tomar, beber"), ("meat", "carne"), ("fish", "pescado"), ("don't", "no (con I, you, we, they)"), ("doesn't", "no (con he, she, it)")],
    worked=[
        ("Afirmación con -s", "Quieres decir: «Ana toma té».", ["Ana es she.", "El verbo drink con she lleva -s: drinks.", "Escribo: Ana drinks tea."], "Ana drinks tea."),
        ("De afirmación a negación", "Cambia «She eats meat» a negativo.", ["Con she uso doesn't.", "Quito la -s del verbo: eat.", "Resultado: She doesn't eat meat."], "She doesn't eat meat."),
    ],
    mistakes=[("Escribir «She doesn't eats meat».", "Después de doesn't el verbo vuelve a su forma base, sin -s.", "Escribe She doesn't eat meat."),
              ("Contestar «No, he don't».", "Con he se usa doesn't; don't es para I, you, we y they.", "Contesta No, he doesn't.")],
    T=[
        ("abc", "{F} Completa: She ___ rice every day.", "eats", "eat", "eating", "Con she, el verbo en afirmativo lleva -s."),
        ("abc", "{F} Completa: They ___ bread for breakfast.", "eat", "eats", "is eat", "Con they el verbo queda igual, sin -s."),
        ("ab", "{F} Elige la oración correcta.", "He drinks tea.", "He drink tea.", "Con he, el verbo del presente simple lleva -s."),
        ("abc", "{F} Completa: Ana ___ eat meat.", "doesn't", "don't", "isn't", "Ana es she, y con she la negación es doesn't."),
        ("abc", "{F} Completa: I ___ drink soda.", "don't", "doesn't", "not", "Con I la negación del presente simple es don't."),
        ("abc", "{F} Completa la pregunta: ___ you eat breakfast?", "Do", "Does", "Are", "Con you las preguntas del presente simple empiezan con Do."),
        ("abc", "{F} Completa la pregunta: ___ Carlos eat lunch at work?", "Does", "Do", "Is", "Carlos es he, así que la pregunta empieza con Does."),
        ("ab", "{F} Does Marta eat fish? Elige la respuesta corta para «no».", "No, she doesn't.", "No, she don't.", "Con she la respuesta corta usa doesn't."),
        ("Ordena las palabras: doesn't / She / fish / eat. Escribe la oración.", "She doesn't eat fish.", "Con she va doesn't y el verbo eat queda en forma base."),
        ("Traduce: «Ella no come carne». Escribe la oración en inglés con contracción.", "She doesn't eat meat.", "Con she la negación es doesn't y el verbo va sin -s."),
        ("ab", "¿Cuál es el error en «Mr. Lopez don't eat sugar»?", "Debe decir doesn't", "Debe decir sugars", "Mr. Lopez es he, y con he la negación es doesn't, no don't."),
        ("abc", "{F} Después de doesn't, el verbo va:", "En forma base, sin -s", "Con -s", "Con -ing", "Doesn't ya lleva la marca de tercera persona, por eso el verbo queda en base."),
        ("ab", "{F} Do they eat dinner together? Elige la respuesta corta para «sí».", "Yes, they do.", "Yes, they does.", "Con they se usa do, no does."),
    ],
    ctx=("abc", "Una compañera de trabajo (ejemplo) te pregunta: «Do you eat meat?» Tú sí comes carne. ¿Qué respondes?", "Yes, I do.", "Yes, I does.", "Yes, you do.", "La respuesta corta repite do porque la pregunta empezó con Do."),
    sc=[("¿Qué terminación lleva el verbo con he, she, it en afirmativo?", "-s", "En tercera persona del presente simple el verbo termina en -s."),
        ("Completa: He ___ eat fish.", "doesn't", "Con he la negación es doesn't."),
        ("¿Cómo preguntas «¿Come ella pan?»", "Does she eat bread?", "Con she se usa Does y el verbo queda sin -s.")],
    op=("Revisa la tarjeta de reglas: {F} Escribe en tu cuaderno cuatro oraciones sobre ti y una persona cercana (datos de ejemplo): dos afirmativas y dos negativas, con eat o drink.",
        "I eat bread. I don't eat fish. My sister drinks coffee. She doesn't drink soda.",
        ["escribe cuatro oraciones", "usa -s con he o she en afirmativo", "usa don't o doesn't en negativo, con el verbo sin -s"],
        ["cuatro oraciones: dos afirmativas y dos negativas"],
        ["escribir «She doesn't eats»", "usar don't con he o she"],
        "Pregunta: «¿Qué no come esa persona?»."),
    reinforce="Escribe tres oraciones afirmativas con he o she y subraya la -s final del verbo.",
    extend="Haz tres preguntas con Do o Does sobre comidas y pídele a otra persona que las responda con una respuesta corta.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy leo en pareja un texto de hábitos de alimentación, respondo preguntas y reviso lo que dice de dos personas.",
    prior=["Uso I eat, he eats y las negaciones don't y doesn't.", "Sé leer horas como 7:00.", "Sé subrayar palabras clave."],
    explain=[
        "Practicar con apoyo significa leer el texto, responder preguntas y comprobar con otra persona. Una buena respuesta se apoya en una frase del texto, no solo en la memoria.",
        "Para responder a una pregunta de comprensión, primero mira la palabra que pregunta: What (qué), What time (a qué hora), Who (quién). Después busca en el texto la frase que tiene esa información.",
        "Este texto habla de dos personas: Marta (I) y su hijo Luis (he). Cuando cambia la persona, el verbo cambia: I eat, pero Luis eats. Fíjate siempre en quién hace la acción.",
        "Si no estás seguro, subraya la frase en el texto y léela con otra persona. Equivocarse al comienzo es normal: sirve para aprender.",
    ],
    vocab=[("cook", "cocinera o cocinero"), ("restaurant", "restaurante"), ("soup", "sopa"), ("salad", "ensalada"), ("milk", "leche"), ("coffee", "café"), ("together", "juntos")],
    worked=[
        ("Buscar la hora", "Pregunta sobre el Text 2: «What time does Marta eat breakfast?»", ["La pregunta pide una hora: what time.", "Busco breakfast en el texto: «I eat breakfast at 7:00».", "La hora es 7:00."], "7:00"),
        ("Cambiar de persona", "Pregunta: «What does Luis drink?»", ["Luis es he.", "Busco: «He doesn't drink coffee; he drinks milk».", "La respuesta es milk."], "Milk"),
    ],
    mistakes=[("Responder con lo que hace Marta cuando preguntan por Luis.", "Se mezcla a las dos personas del texto.", "Mira el nombre de la pregunta y busca la frase de esa persona."),
              ("Olvidar la -s en «Luis eat breakfast».", "Luis es he y el verbo en afirmativo lleva -s.", "Escribe Luis eats breakfast.")],
    T=[
        ("{F} What time does Marta eat breakfast? Escribe solo la hora, por ejemplo 9:00.", "7:00", "El texto dice «I eat breakfast at 7:00»."),
        ("abc", "{F} What does Marta drink for breakfast?", "Coffee", "Milk", "Tea", "Marta dice «I drink coffee»; la leche es de Luis."),
        ("ab", "{F} Does Marta eat meat?", "No, she doesn't.", "Yes, she does.", "El texto dice «I don't eat meat»."),
        ("abc", "{F} Who drinks milk?", "Luis", "Marta", "The restaurant", "Se dice «he drinks milk» y he es Luis."),
        ("{F} What time does Luis eat breakfast? Escribe solo la hora, por ejemplo 9:00.", "8:00", "Se dice que Luis eats breakfast at 8:00."),
        ("abc", "{F} What does Marta eat for lunch?", "Soup and salad", "Bread and cheese", "Rice and chicken", "El pan con queso es del desayuno; en el almuerzo come sopa y ensalada."),
        ("ab", "{F} Which sentence is true?", "Marta and Luis eat dinner together.", "Marta eats dinner alone.", "El texto dice «We eat dinner together at 8:30»."),
        ("abc", "{F} What time do they eat dinner?", "8:30", "7:00", "8:00", "La cena es a las 8:30; las otras horas son desayunos."),
        ("abc", "{F} Completa: Luis ___ coffee.", "doesn't drink", "don't drink", "doesn't drinks", "Con Luis (he) se usa doesn't y el verbo en forma base."),
        ("ab", "{F} Elige la pregunta correcta.", "Does Luis drink milk?", "Do Luis drink milk?", "Luis es he, y con he la pregunta empieza con Does."),
        ("abc", "{F} What is Marta's job?", "She is a cook at a small restaurant.", "She is a bus driver.", "She is a teacher at a school.", "El texto dice «I'm a cook at a small restaurant»."),
        ("abc", "{F} Completa: ___ eats breakfast at 8:00.", "He", "I", "They", "El que come a las 8:00 es Luis, y para Luis usamos he."),
        ("abc", "{F} Marta dice «We eat dinner together». ¿Quiénes son «we»?", "Marta and Luis", "Only Marta", "Only Luis", "We incluye a la persona que habla y a otra: Marta y Luis."),
    ],
    ctx=("abc", "En un taller de la comunidad te dan un texto de hábitos (ejemplo) y te preguntan: «Does Mr. Lopez eat breakfast at home?» En el ejemplo, el señor Lopez desayuna en casa. ¿Qué dices?", "Yes, he does.", "Yes, he do.", "Yes, I does.", "La respuesta corta repite Does de la pregunta: Yes, he does."),
    sc=[("¿Qué pregunta usas para pedir una hora?", "What time...?", "What time pregunta a qué hora ocurre algo."),
        ("Completa: My mother ___ coffee.", "drinks", "Con my mother (she) el verbo lleva -s."),
        ("¿Cómo respondes bien una pregunta de comprensión?", "Busco la frase del texto que tiene la información", "La respuesta se apoya en lo que dice el texto.")],
    op=("Lee el Text 2: {F} Escribe en tu cuaderno cinco preguntas sobre Marta y Luis (What, What time, Who, Does...) y respóndelas con una oración completa.",
        "What time does Marta eat breakfast? She eats breakfast at 7:00. Does Luis drink coffee? No, he doesn't.",
        ["escribe cinco preguntas y sus respuestas", "las respuestas usan datos del texto", "usa doesn't o -s con he y she"],
        ["cinco preguntas con sus respuestas"],
        ["responder con datos que no están en el texto", "mezclar a Marta y Luis"],
        "Pregunta: «¿En qué frase del texto está tu respuesta?»."),
    reinforce="Vuelve a leer el Text 2 y subraya con dos colores lo que hace Marta y lo que hace Luis.",
    extend="Escribe tres preguntas más sobre el Text 2 y pide a otra persona que las responda de memoria.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy leo un aviso de un comedor comunitario y lo uso para presentar mis hábitos de alimentación y los de una persona cercana.",
    prior=["Sé decir lo que como y bebo.", "Uso he y she con -s.", "Leo avisos cortos con ayuda de palabras clave."],
    explain=[
        "Los avisos de la vida real, como el de un comedor comunitario, son textos cortos con datos clave: días, horas, comidas y reglas. Se leen buscando esos datos.",
        "Aquí aparecen expresiones útiles. «Please bring your own cup» es una petición amable: por favor trae tu propio vaso. «No takeout» significa que no se puede llevar comida para la casa (en inglés estadounidense, takeout es comida para llevar).",
        "Después de leer, puedes presentar tus hábitos con oraciones simples: I eat lunch at 1:00. Y puedes presentar a alguien cercano: My brother eats lunch at 2:00.",
        "Recuerda que, con una persona cercana, el verbo lleva -s: My mother drinks tea, My neighbor eats dinner at 9:00. Usa datos de ejemplo, sin nombres ni direcciones reales.",
    ],
    vocab=[("notice", "aviso"), ("kitchen", "cocina"), ("beans", "porotos"), ("juice", "jugo"), ("cup", "taza o vaso"), ("volunteers", "voluntarios"), ("please", "por favor")],
    worked=[
        ("Leer un aviso", "Notice (example): «Lunch is at 1:00. Today: rice, beans and salad.»", ["Busco la hora: 1:00.", "Busco la comida: rice, beans and salad.", "Entiendo: el almuerzo es a la 1:00 y hoy hay arroz, porotos y ensalada."], "Almuerzo a la 1:00: arroz, porotos y ensalada"),
        ("Presentar a alguien cercano", "Quieres decir: «Mi hermano almuerza a las 2:00».", ["Mi hermano es he.", "Almorzar: eat lunch, con -s: eats.", "Escribo: My brother eats lunch at 2:00."], "My brother eats lunch at 2:00."),
    ],
    mistakes=[("Entender «No takeout» como «No hay comida».", "Se cambia el sentido: el aviso dice que no se puede llevar la comida.", "Lee cada parte: no takeout = no se puede llevar comida a casa."),
              ("Escribir «My mother drink tea».", "Con my mother (she) el verbo lleva -s.", "Escribe My mother drinks tea.")],
    T=[
        ("{F} What time is lunch? Escribe solo la hora, por ejemplo 9:00.", "1:00", "El aviso dice «Lunch is at 1:00»."),
        ("abc", "{F} What is today's meal?", "Rice, beans and salad", "Soup and bread", "Chicken and potatoes", "El aviso dice «Today: rice, beans and salad»."),
        ("ab", "{F} Can people take food home?", "No, takeout food is not allowed.", "Yes, they can take food home.", "«No takeout» quiere decir que no se puede llevar la comida a la casa."),
        ("abc", "{F} What should people bring?", "Their own cup", "Their own rice", "Their own chair", "El aviso pide «bring your own cup»."),
        ("abc", "{F} When do the volunteers eat?", "At 12:30", "At 1:00", "At 2:00", "La frase final dice «Volunteers eat at 12:30»."),
        ("ab", "Traduce: «Los voluntarios comen a las 12:30».", "Volunteers eat at 12:30.", "Volunteers eats at 12:30.", "Volunteers es plural, entonces el verbo queda sin -s."),
        ("abc", "Completa para hablar de tu hermano (ejemplo): My brother ___ rice every day.", "eats", "eat", "eating", "My brother es he y el verbo lleva -s."),
        ("abc", "Completa para hablar de tu hermana (ejemplo): My sister ___ drink soda.", "doesn't", "don't", "isn't", "My sister es she y la negación correcta es doesn't."),
        ("Ordena las palabras: lunch / My / at / eats / 2:00 / mother. Escribe la oración.", "My mother eats lunch at 2:00.", "El orden en inglés es sujeto, verbo, objeto y hora."),
        ("ab", "Elige la oración correcta para presentar a un vecino (ejemplo).", "My neighbor eats dinner at 9:00.", "My neighbor eat dinner at 9:00.", "Con my neighbor (he o she) el verbo lleva -s."),
        ("abc", "Traduce: «El vecino toma leche en el desayuno».", "The neighbor drinks milk for breakfast.", "The neighbor drink milk for breakfast.", "The neighbor drinks milk for dinner.", "Con the neighbor (he o she) el verbo lleva -s, y breakfast es el desayuno."),
        ("abc", "{F} «Water or juice» significa que:", "Eliges una bebida entre agua y jugo", "Tomas las dos al mismo tiempo", "No hay bebidas", "La palabra or une dos opciones entre las que eliges."),
        ("abc", "{F} ¿Para qué sirve este texto?", "Para avisar el horario, el menú y las reglas del almuerzo", "Para vender comida", "Para contar una historia de amor", "Un aviso informa datos útiles a quien lo lee."),
    ],
    ctx=("abc", "Conoces a una voluntaria del comedor (ejemplo). Quieres decirle a otra persona cuándo come la vecina Mrs. Rojas (ejemplo), que almuerza a las 12:00. ¿Qué dices?", "Mrs. Rojas eats lunch at 12:00.", "Mrs. Rojas eat lunch at 12:00.", "Mrs. Rojas is lunch at 12:00.", "Mrs. Rojas es she, y con she el verbo eat lleva -s."),
    sc=[("¿Qué significa «Please bring your own cup»?", "Por favor trae tu propio vaso", "Please es por favor y bring es traer."),
        ("Completa: My brother ___ breakfast at 7:00.", "eats", "Con my brother (he) el verbo lleva -s."),
        ("Si un aviso dice «No takeout», ¿puedes llevarte comida a casa?", "No", "No takeout prohíbe llevarse la comida.")],
    op=("Mira el aviso del comedor: {F} Escribe en tu cuaderno un párrafo de cuatro oraciones: dos sobre tus hábitos de alimentación y dos sobre una persona cercana (datos de ejemplo). Después preséntalo en voz alta a otra persona.",
        "I eat breakfast at 7:00. I drink tea. My sister eats lunch at 1:00. She doesn't eat meat.",
        ["escribe cuatro oraciones", "dos con I y dos con he o she", "usa -s o doesn't con he o she"],
        ["cuatro oraciones y una presentación oral breve"],
        ["usar datos reales personales", "olvidar la -s con he o she"],
        "Pregunta: «¿Qué come esa persona y a qué hora?»."),
    reinforce="Escribe tres oraciones sobre las comidas de una persona de tu familia, usando datos de ejemplo.",
    extend="Prepara un breve aviso de ejemplo para tu barrio con día, hora y comida, como el del comedor comunitario.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy repaso lo aprendido sobre textos de alimentación, reviso mis avances y decido qué quiero practicar después.",
    prior=["Leí textos sobre comidas y subrayé palabras clave.", "Uso el presente simple con I, he y she.", "Presenté mis hábitos y los de alguien cercano."],
    explain=[
        "Revisar lo logrado significa mirar qué ya sabes hacer y qué te falta. En este módulo aprendiste a leer textos de comidas, usar cantidades, decir lo que comes y lo que no comes, y presentar a otra persona.",
        "Una buena revisión sigue tres pasos: leo el texto, respondo con datos del texto y compruebo mis verbos (-s con he o she, don't o doesn't en negativo).",
        "Para decidir los pasos siguientes, pregúntate: ¿qué parte fue fácil?, ¿qué parte me costó?, ¿qué puedo practicar esta semana? Anota una meta pequeña y posible.",
        "Recuerda: este cuaderno no tiene audio. Cuando puedas, pide a otra persona que lea en voz alta y repite tú las frases para practicar la pronunciación.",
    ],
    vocab=[("habit", "hábito"), ("every day", "todos los días"), ("late", "tarde"), ("big", "grande"), ("driver", "conductor"), ("at home", "en casa")],
    worked=[
        ("Revisar una respuesta", "Alguien escribe: «Mary eat lunch at 2:00».", ["Mary es she.", "Con she el verbo lleva -s.", "Corrijo: Mary eats lunch at 2:00."], "Mary eats lunch at 2:00."),
        ("Responder con datos del texto", "Pregunta sobre el Text 3: «Does John eat bread?»", ["Busco a John: «He doesn't eat bread».", "La respuesta corta es No, he doesn't."], "No, he doesn't."),
    ],
    mistakes=[("Copiar una respuesta sin revisarla con el texto.", "Puede tener un dato equivocado, como una hora que no es la del texto.", "Comprueba cada dato volviendo a la frase del texto."),
              ("No revisar los verbos al final.", "Se escapan errores como «She eat» o «He don't».", "Antes de terminar, lee cada verbo y mira si necesita -s o doesn't.")],
    T=[
        ("abc", "{F} What time does Mary eat lunch?", "At 2:00", "At 5:30", "At 1:00", "El texto dice «She eats a big lunch at 2:00»."),
        ("abc", "{F} What does Mary eat for lunch?", "Rice, chicken and salad", "Soup and bread", "Eggs and milk", "El texto nombra arroz, pollo y ensalada."),
        ("ab", "{F} Does Mary eat dinner late?", "No, she doesn't.", "Yes, she does.", "El texto dice «She doesn't eat dinner late»."),
        ("abc", "{F} What is John's job?", "He is a bus driver.", "He is a cook.", "He is a doctor.", "El texto dice «Her brother John is a bus driver»."),
        ("{F} What time does John eat breakfast? Escribe solo la hora, por ejemplo 9:00.", "5:30", "El texto dice «He eats breakfast at 5:30», y ese es el dato que pide la pregunta."),
        ("abc", "{F} What does John drink a lot of?", "Coffee", "Milk", "Juice", "«A lot of» indica mucha cantidad, y el texto lo usa con coffee; milk y juice no aparecen."),
        ("ab", "{F} Does John eat bread?", "No, he doesn't.", "Yes, he does.", "El texto dice «He doesn't eat bread»."),
        ("abc", "{F} Who is John?", "Mary's brother", "Mary's son", "Mary's boss", "El texto dice «Her brother John»."),
        ("abc", "{F} What do Mary and John drink at home with every meal?", "Water", "Coffee", "Milk", "La última oración dice que en casa beben agua con cada comida."),
        ("abc", "Completa: My cousin ___ (eat) rice every day.", "eats", "eat", "are eating", "My cousin es he o she y el verbo lleva -s."),
        ("ab", "Corrige el error: «He don't drink soda».", "He doesn't drink soda.", "He doesn't drinks soda.", "Con he se usa doesn't y el verbo queda sin -s."),
        ("Traduce: «Yo desayuno a las 7:00». Escribe la oración en inglés con el verbo eat.", "I eat breakfast at 7:00.", "Con I el verbo eat va sin -s y la hora lleva at."),
        ("abc", "¿Cuál de estas oraciones tiene un error?", "She eat lunch at 2:00.", "She eats lunch at 2:00.", "She doesn't eat dinner late.", "Con she, en afirmativo, el verbo debe terminar en -s."),
    ],
    ctx=("abc", "En una charla de tu barrio (ejemplo) una persona dice: «I eat a lot of vegetables and I don't eat meat.» Tú quieres contarlo a otra persona. ¿Qué dices de ella?", "She eats a lot of vegetables and she doesn't eat meat.", "She eat a lot of vegetables and she don't eat meat.", "She is eat a lot of vegetables.", "Al contar de otra persona cambia I por she y se usan eats y doesn't."),
    sc=[("¿Qué debo mirar en cada verbo con he o she?", "Si lleva -s en afirmativo o doesn't en negativo", "Esos son los cambios clave del presente simple."),
        ("Completa con don't o doesn't: They ___ eat meat.", "don't", "They es plural, y con plural la negación es don't."),
        ("¿Qué hago para mejorar mi inglés esta semana?", "Elijo una meta pequeña y la practico", "Una meta pequeña y concreta se puede lograr.")],
    op=("Haz la revisión final: {F} Escribe en tu cuaderno un párrafo de cinco oraciones que presente tus hábitos de alimentación y los de una persona cercana (datos de ejemplo). Después anota una cosa que lograste y una que quieres practicar.",
        "I eat breakfast at 7:00 and I drink tea. I eat a lot of vegetables. My mother eats lunch at 1:00. She doesn't eat meat. I achieved: -s with she. I want to practice: questions with Does.",
        ["escribe cinco oraciones", "usa -s o doesn't con he o she", "anota un logro y un siguiente paso"],
        ["cinco oraciones y dos frases de autoevaluación"],
        ["usar datos personales reales", "no escribir el siguiente paso"],
        "Pregunta: «¿Qué quieres practicar esta semana?»."),
    reinforce="Repasa la tarjeta de reglas de la clase 3 y escribe tres oraciones con don't o doesn't.",
    extend="Escribe un texto de seis oraciones con tus comidas de un día y compártelo con una persona de confianza.",
)

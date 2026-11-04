"""Cuaderno del estudiante, 1.º medio Inglés (oficial): IN1M OA 15, escribir para explicar, narrar y opinar.

Variedad de palabras, oraciones y estructuras; conectores; ortografía de palabras frecuentes y apóstrofe.
Todos los textos son originales, con glosario en español dentro del enunciado.
"""
from __future__ import annotations

from student_content_in_m1_b import MAT, lesson, mc, task
from student_lessons import arith, ex

OA = "IN1M OA 15"

# ============================================================ clase 1: propósito (explicar, narrar, opinar)
EXP1 = "«Bees help plants grow. They carry pollen from one flower to another. Because of this, fruit and seeds can form.»"
GEXP1 = "(bees = abejas; carry = llevan; pollen = polen; flower = flor; fruit = fruta; seeds = semillas; form = formarse)"
NAR1 = "«Last Saturday, Pedro and his sister found a small kitten under a bench. They carried it to a vet, and the vet gave it some milk.»"
GNAR1 = "(kitten = gatito; bench = banca; carried = llevaron; vet = veterinario; milk = leche)"
OP1 = "«In my opinion, schools should start later. Teenagers feel tired in the morning, so they cannot concentrate. For this reason, nine o'clock is better than eight.»"
GOP1 = "(opinion = opinión; schools = colegios; should = deberían; start = empezar; later = más tarde; teenagers = adolescentes; concentrate = concentrarse; reason = razón)"
EXP2 = "«Rain forms when water vapor rises, cools and turns into small drops. The drops join together in clouds. When they are heavy, they fall as rain.»"
GEXP2 = "(forms = se forma; vapor = vapor; rises = sube; cools = se enfría; drops = gotas; join = se unen; heavy = pesadas; fall = caen)"
NAR2 = "«Yesterday, Isidora lost her key. She searched in her bag, then she called her neighbor. Finally, she found the key in her coat pocket.»"
GNAR2 = "(lost = perdió; key = llave; searched = buscó; neighbor = vecina; coat pocket = bolsillo del abrigo)"
OP2 = "«I think reading comics is a good habit. They have pictures, so they help me understand new words. However, I also read novels.»"
GOP2 = "(comics = cómics; habit = hábito; pictures = imágenes; understand = entender; novels = novelas)"

lesson(
    OA, 1, MAT,
    "Aprenderé a distinguir tres propósitos de escritura: explicar, narrar y opinar, y qué estructuras usa cada uno. Sirve para elegir las palabras y los tiempos verbales adecuados al escribir.",
    ["Sé escribir oraciones con because y so.", "Conozco el presente simple y el pasado simple."],
    [
        "Cuando escribes, el propósito (purpose) decide cómo escribes. Para explicar (explain) das hechos (facts) y causas: usas el presente simple, palabras como because, so, for example y because of this, y un orden lógico. Para narrar (narrate) cuentas lo que pasó: usas el pasado simple, personajes, tiempo y lugar, y palabras de orden como last Saturday, then y finally. Para opinar (give an opinion) dices lo que piensas y lo apoyas con razones: usas I think, In my opinion, because y for this reason.",
        "Un hecho se puede comprobar: Santiago is the capital of Chile. Una opinión es lo que alguien piensa y no se puede comprobar: Santiago is the most beautiful city. Una opinión sin razones convence poco; una opinión con razón (reason) convence más: I think cycling is great because it is cheap.",
        "Antes de escribir, responde tres preguntas: ¿quiero explicar, narrar u opinar?, ¿qué tiempo verbal corresponde?, ¿qué palabras de conexión necesito? Si explicas un hecho general, el presente es la regla; si cuentas algo que terminó, el pasado. Un texto puede mezclar propósitos, pero cada párrafo tiene uno principal.",
    ],
    [("explain", "explicar"), ("narrate", "narrar"), ("give an opinion", "dar una opinión"), ("fact", "hecho comprobable"), ("opinion", "opinión: lo que alguien piensa"), ("reason", "razón"), ("In my opinion / I think", "en mi opinión / creo que")],
    [
        ("Reconocer un texto que explica", f"Texto: {EXP1} {GEXP1} ¿Qué propósito tiene y qué tiempo verbal usa?",
         ["Da un hecho general y una causa: Because of this.", "Los verbos help, carry y can form están en presente.", "Por eso su propósito es explicar."], "Explica; usa el presente simple"),
        ("Reconocer un texto que narra", f"Texto: {NAR1} {GNAR1} ¿Qué propósito tiene y qué pistas muestran que es narración?",
         ["Cuenta algo que pasó: Last Saturday.", "Los verbos found, carried y gave están en pasado.", "Hay personajes y una secuencia de hechos."], "Narra; usa pasado, personajes y una secuencia de hechos"),
    ],
    [
        ("Dar una opinión sin ninguna razón: «Homework is bad».", "Una opinión sin razón convence poco.", "Agrega because y una razón concreta."),
        ("Explicar un hecho general en pasado: «Bees helped plants grow» cuando se habla de lo que siempre ocurre.", "Los hechos generales se explican en presente.", "Usa el presente simple: bees help plants grow."),
    ],
    [
        mc("Para explicar un hecho general, el tiempo verbal habitual es", "el presente simple", ["el pasado simple", "el futuro lejano"], "Los hechos generales se escriben en presente."),
        mc("Para narrar algo que terminó se usa", "el pasado simple", ["el presente simple", "la orden"], "Las acciones terminadas van en pasado."),
        mc("¿Con qué frase se introduce una opinión?", "In my opinion", ["Last Saturday", "For example"], "In my opinion presenta lo que piensa quien escribe."),
    ],
    [
        mc(f"Lee: {OP1} {GOP1} ¿Cuál es el propósito del texto?", "Dar una opinión", ["Narrar un viaje", "Explicar cómo se forma la lluvia"], "Usa In my opinion y un deseo de cambio."),
        mc(f"Lee: {OP1} {GOP1} ¿Qué frase introduce la opinión?", "In my opinion", ["Teenagers feel", "For this reason"], "Es la frase que muestra el punto de vista."),
        mc(f"Lee: {OP1} {GOP1} ¿Cuál es la razón que apoya la opinión?", "Teenagers feel tired in the morning and cannot concentrate", ["Schools have eight classrooms", "Eight o'clock is the usual time for lunch"], "La razón explica por qué conviene empezar más tarde."),
    ],
    [
        mc(f"Lee: {EXP2} {GEXP2} ¿Qué propósito tiene?", "Explicar cómo se forma la lluvia", ["Narrar un viaje", "Dar una opinión sobre el clima"], "Describe un proceso en presente."),
        mc(f"Lee: {NAR2} {GNAR2} ¿Qué palabras muestran el orden de los hechos?", "Then y finally", ["Yesterday y key", "Lost y coat"], "Then y finally ordenan las acciones."),
        mc(f"Lee: {OP2} {GOP2} ¿Qué oración da una razón para la opinión?", "They have pictures, so they help me understand new words", ["However, I also read novels", "Comics are fun"], "Explica por qué leer cómics es un buen hábito."),
    ],
    [
        mc("¿Cuál de estas oraciones es un hecho y no una opinión?", "Santiago is the capital of Chile", ["Santiago is the most beautiful city", "Santiago has the best food"], "Un hecho se puede comprobar."),
        mc("Una estudiante escribe «Bees helped plants grow» para explicar lo que las abejas hacen siempre. ¿Qué corrección haces?", "Bees help plants grow, porque es un hecho general y va en presente", ["Bees will help plants grow, porque va en futuro", "No cambio nada, porque pasado siempre sirve"], "Los hechos generales se escriben en presente."),
    ],
    [
        mc("¿Cuál opinión está mejor apoyada?", "I think cycling is great because it is cheap and healthy", ["I think cycling is great", "Cycling is great, I think maybe"], "Tiene una razón con because."),
        mc("¿Qué texto narra y no explica?", "«Last night, Eli missed the bus, so she walked home.»", ["«Buses carry many people every day.»", "«A bus has wheels and an engine.»"], "Cuenta un hecho pasado con personajes."),
    ],
    [mc("La revista del colegio pide: «Tell us what happened at the sports day.» (sports day = día del deporte) ¿Qué propósito y tiempo verbal usas?", "Narrar, en pasado simple", ["Explicar, en presente simple", "Opinar, en futuro"], "Se pide contar algo que ya ocurrió.")],
    [
        mc("¿Qué es una opinión?", "Lo que alguien piensa y se puede apoyar con razones", ["Un dato comprobable"], "No es lo mismo que un hecho."),
        mc("Para decir una razón en una opinión se puede usar", "because", ["yesterday"], "Because introduce la razón."),
        ("Escribe en inglés la palabra que significa «opinión».", "Opinion", "Opinion es lo que alguien piensa."),
    ],
    task("Escribe tres oraciones sobre el uso del celular en la sala de clases, una para cada propósito: (1) un hecho que explique (en presente), (2) algo que narre lo que pasó ayer (en pasado), (3) una opinión con In my opinion y because. Palabras de apoyo: phone, class, ring, teacher, silent. (phone = celular; ring = sonar; silent = en silencio)",
         "(1) Phones can ring in class. (2) Yesterday, a phone rang and the teacher stopped the lesson. (3) In my opinion, phones should be silent in class because they distract students.",
         ["la primera oración está en presente y es un hecho", "la segunda está en pasado", "la tercera usa In my opinion y because"],
         ["tres oraciones numeradas en la hoja"],
         ["usar presente en la oración que narra", "dar una opinión sin because"],
         "Pide que explique en voz alta cuál es el propósito de cada oración."),
    "Copia los siete términos del vocabulario y escribe un ejemplo en español de cada propósito.",
    "Escribe tres frases en español sobre el recreo: un hecho, un hecho que ocurrió ayer y una opinión con su razón.",
)

# ============================================================ clase 2: conectores
lesson(
    OA, 2, MAT,
    "Aprenderé a elegir y usar conectores que unen mis ideas: suma, contraste, causa, resultado, ejemplo y orden. Sirve para que mis textos no sean una lista de oraciones sueltas.",
    ["Sé usar and, but, because y so en oraciones simples.", "Conozco first, then y finally."],
    [
        "Los conectores (connectors) unen ideas y muestran la relación entre ellas. Para sumar: and, also, in addition. Para contrastar: but, however, although. Para la causa (por qué ocurre): because. Para el resultado (qué ocurre después): so, as a result. Para dar un ejemplo: for example. Para ordenar: first, then, after that, finally. Para una alternativa: or.",
        "Cada conector tiene su lugar. But y so van en medio de una oración, después de una coma: It was cold, so we wore jackets. However va al comienzo de una oración nueva, con coma después: It was cheap. However, I did not buy it. Although introduce la idea más débil y no se usa con but: Although it was cheap, I did not buy it. Because explica la causa: She stayed home because she was sick.",
        "Para elegir el conector, pregúntate qué relación hay entre las dos ideas. ¿La segunda es una causa, un resultado, un contraste, un ejemplo o un paso más? He is tired because he stayed up late y He stayed up late, so he is tired dicen lo mismo desde dos lados: con because la causa va al final; con so, la causa va primero y el resultado después. Si eliges el conector equivocado, la oración cambia de sentido o deja de tener sentido.",
    ],
    [("connector", "conector: palabra que une ideas"), ("because", "porque: causa"), ("so / as a result", "así que / como resultado: resultado"), ("but / however / although", "pero / sin embargo / aunque: contraste"), ("for example", "por ejemplo"), ("in addition / also", "además"), ("or", "o: alternativa")],
    [
        ("Elegir un conector de contraste", "Completa: «I wanted to go out, ___ it was raining.» (go out = salir)",
         ["Las dos ideas se oponen: quería salir y estaba lloviendo.", "Para contrastar uso but.", "La oración queda: I wanted to go out, but it was raining."], "but"),
        ("Elegir un conector de resultado", "Completa: «She studied hard, ___ she passed the test.» (studied = estudió; passed = aprobó)",
         ["Estudiar mucho es la causa y aprobar es el resultado.", "El resultado se introduce con so.", "La oración queda: She studied hard, so she passed the test."], "so"),
    ],
    [
        ("Escribir «Although it was cheap, but I did not buy it».", "Although y but expresan lo mismo y no se usan juntos.", "Usa solo uno: Although it was cheap, I did not buy it."),
        ("Poner However en medio de una oración sin punto: «It was cheap however I did not buy it».", "However inicia una oración nueva.", "Escribe: It was cheap. However, I did not buy it."),
    ],
    [
        mc("Because introduce", "la causa", ["el resultado", "una alternativa"], "Explica por qué ocurre algo."),
        mc("But marca", "un contraste", ["un ejemplo", "un orden"], "Une dos ideas que se oponen."),
        mc("For example introduce", "un ejemplo", ["una causa", "un contraste"], "Presenta un caso concreto."),
    ],
    [
        mc("Completa: «Tom is tired ___ he stayed up late.»", "because", ["so", "but"], "Quedarse despierto es la causa del cansancio."),
        mc("Completa: «It was cold, ___ we wore jackets.»", "so", ["because", "or"], "Usar chaquetas es el resultado del frío."),
        mc("Completa: «She likes tea, ___ her brother prefers coffee.» (prefers = prefiere)", "but", ["so", "because"], "Los gustos se oponen."),
    ],
    [
        mc("Completa: «You can take the bus ___ walk to school.»", "or", ["but", "so"], "Presenta dos opciones."),
        mc("Completa: «Many animals sleep in winter. ___, bears stay in caves for months.» (caves = cuevas)", "For example", ["However", "Because"], "El oso es un ejemplo del grupo de animales."),
        mc("Completa: «___ it was raining, we played outside.»", "Although", ["Because", "So"], "Hay un contraste: llovía y aun así jugaron."),
    ],
    [
        mc("¿Cuál oración está bien escrita?", "Although it was cheap, I did not buy it", ["Although it was cheap, but I did not buy it", "Although it was cheap, so I did not buy it"], "Con although no se usa but."),
        mc("«Cycling is healthy. ___, it is cheap.» ¿Qué conector agrega una segunda ventaja?", "In addition", ["However", "Although"], "In addition suma una idea del mismo tipo."),
    ],
    [
        mc("Completa los dos espacios: «It was late, ___ we hurried. We got to the theater; ___, the movie had already started.» (movie = película; hurried = nos apuramos; theater = cine)", "so ... however", ["because ... so", "but ... because"], "Primero hay un resultado y después un contraste."),
        mc("Elige el párrafo con los conectores en orden lógico.", "First, Ana made a list. Then she bought apples. Finally, she cooked", ["Finally, Ana made a list. Then she cooked. First, she bought apples", "Then, Ana cooked. First, she made a list. Finally, she bought apples"], "First, then y finally siguen el orden real de las acciones."),
    ],
    [mc("En un correo a un amigo escribes: «The museum was small. ___, it was very interesting.» ¿Qué conector es el mejor?", "However", ["Because", "So"], "Pequeño e interesante se oponen.")],
    [
        mc("¿Qué conector expresa resultado?", "So", ["Because"], "So introduce el resultado."),
        mc("¿Qué conector marca contraste entre dos oraciones separadas?", "However", ["Also"], "However se usa al comenzar una oración nueva."),
        ("Escribe en inglés el conector que significa «porque».", "Because", "Because introduce la causa."),
    ],
    task("Une las dos ideas de cada par con el conector indicado y escribe las tres oraciones: (1) It was sunny / we went to the beach (so). (2) We were hungry / we had no money (but). (3) Lucía was late / the bus was slow (because). (sunny = soleado; beach = playa; hungry = con hambre; slow = lento)",
         "(1) It was sunny, so we went to the beach. (2) We were hungry, but we had no money. (3) Lucía was late because the bus was slow.",
         ["usa cada conector en el par indicado", "la coma está en su lugar", "el sentido de cada oración es lógico"],
         ["tres oraciones en la hoja"],
         ["poner because donde va so", "olvidar la coma antes de so y but"],
         "Pide que cambie un conector y explique cómo cambia el sentido."),
    "Copia los siete conectores y escribe una oración con cada uno.",
    "Escribe en español cuatro frases con conectores diferentes (porque, así que, pero, por ejemplo) y márcalas.",
)

# ============================================================ clase 3: variedad de palabras y estructuras
lesson(
    OA, 3, MAT,
    "Aprenderé a variar mis palabras y mis oraciones: cambiar palabras repetidas por sinónimos, unir oraciones cortas y usar estructuras con when e if. Sirve para que mis textos suenen más ricos y menos repetitivos.",
    ["Sé usar adjetivos como big, small y good.", "Conozco and, but, so y because."],
    [
        "Para escribir con variedad, primero cambia las palabras repetidas por sinónimos (synonyms), que son palabras de significado parecido. Good puede ser great, excellent o useful; big puede ser huge; small puede ser tiny; very tired puede ser exhausted; nice puede ser friendly o pleasant; said puede ser whispered, shouted o answered. Elige el sinónimo que mejor calza con el contexto: un vecino es friendly, pero una película no.",
        "Segundo, varía la longitud y la forma de las oraciones. Muchas oraciones cortas seguidas suenan entrecortadas: Luis is tired. He has practice. He goes anyway. Puedes unirlas con conectores: Luis is tired, but he goes to practice anyway. También puedes empezar con palabras de tiempo o con when y if: When it rains, we stay home. If you study, you will pass.",
        "Tercero, agrega detalles con adjetivos y adverbios (adverbs), que dicen cómo ocurre una acción: quickly, slowly, carefully. Compara The girl walked con The shy girl walked slowly into the crowded classroom. Cuidado con if: se escribe If it rains tomorrow, we will study at home; no If it will rain. En el bloque if no se usa will.",
    ],
    [("synonym", "sinónimo"), ("exhausted", "agotado"), ("whispered / shouted", "susurró / gritó"), ("adverb", "adverbio: dice cómo ocurre la acción"), ("when / if", "cuando / si"), ("detail", "detalle")],
    [
        ("Cambiar una palabra repetida", "Mejora: «The movie was good. The actors were good. The music was good.» (movie = película; actors = actores; music = música)",
         ["Good se repite tres veces.", "Cambio cada good por un sinónimo que calce: great, excellent y beautiful.", "Queda: The movie was great, the actors were excellent and the music was beautiful."], "The movie was great, the actors were excellent and the music was beautiful"),
        ("Unir oraciones cortas", "Une en una sola oración: «Luis is tired. He has soccer practice. He goes anyway.» (practice = entrenamiento; anyway = igual)",
         ["Las dos primeras ideas se oponen a la tercera.", "Uso but para el contraste.", "Queda: Luis is tired, but he goes to soccer practice anyway."], "Luis is tired, but he goes to soccer practice anyway"),
    ],
    [
        ("Repetir la palabra nice cinco veces en un párrafo.", "El texto suena repetitivo y poco preciso.", "Cambia por sinónimos: friendly, pleasant, kind."),
        ("Escribir «If it will rain tomorrow, we will study at home».", "En la cláusula con if no se usa will.", "Escribe If it rains tomorrow, we will study at home."),
    ],
    [
        mc("Un sinónimo (synonym) de big es", "huge", ["tiny", "heavy"], "Huge significa muy grande."),
        mc("«Said» puede cambiarse por una palabra más precisa cuando alguien habla muy bajo: ", "whispered", ["shouted", "ran"], "Whispered significa susurró."),
        mc("Para unir dos ideas que se suman se puede usar", "and", ["although", "yesterday"], "And suma ideas."),
    ],
    [
        mc("La mejor forma de decir «very tired» con más precisión es", "exhausted", ["delighted", "enormous"], "Exhausted significa agotado."),
        mc("Reemplaza «nice» en «The teacher is nice» por una palabra que describa su forma de ser.", "friendly", ["expensive", "noisy"], "Friendly describe a una persona amable."),
        mc("Completa con la palabra más precisa: «Don't shout in the library,» she ___ quietly.", "whispered", ["ran", "shouted"], "Whispered calza con quietly."),
    ],
    [
        mc("Une las dos ideas: «Ana is happy. She won the contest.»", "Ana is happy because she won the contest", ["Ana is happy but she won the contest", "Ana is happy or she won the contest"], "La segunda idea es la causa de la primera."),
        mc("Une las dos ideas empezando con una causa: «It was raining. We stayed home.»", "Because it was raining, we stayed home", ["Because we stayed home, it was raining", "It was raining or we stayed home"], "Because introduce la causa y va primero."),
        mc("Une las dos ideas: «I like tennis. My brother likes soccer.»", "I like tennis, but my brother likes soccer", ["I like tennis, so my brother likes soccer", "I like tennis because my brother likes soccer"], "Los gustos se oponen."),
    ],
    [
        mc("Un párrafo empieza así: «I woke up. I had breakfast. I went to school. I saw my friend.» ¿Qué cambio mejora la variedad?", "Empezar con «On Saturday morning, I woke up early and had breakfast»", ["Escribir cuatro veces I woke up", "Empezar cada oración con I y no cambiar nada más"], "Unir ideas y agregar un tiempo hace más rica la redacción."),
        mc("¿Cuál oración con if está bien escrita?", "If it rains tomorrow, we will study at home", ["If it will rain tomorrow, we will study at home", "If it rained tomorrow, we study at home"], "En el bloque con if va el presente simple."),
    ],
    [
        mc("¿Cuál versión enriquece más «The girl walked.»?", "The shy girl walked slowly into the crowded classroom", ["The girl walked and walked", "The girl walked the girl walked"], "Agrega adjetivos, un adverbio y un lugar."),
        mc("¿Qué versión evita la repetición y mantiene el significado de «The park is nice. The park is nice and big»? (pleasant = agradable; spacious = amplio)", "The park is pleasant and spacious", ["The park is nice and nice", "The park is nice, nice and big"], "Usa dos palabras distintas con el mismo sentido."),
    ],
    [mc("Escribes una reseña de un restaurante. Tu borrador dice: «The food was good, the waiter was good and the music was good.» (waiter = garzón) ¿Cuál es la mejor versión?", "The food was delicious, the waiter was friendly and the music was pleasant", ["The food was good, the waiter was good and the music was good", "The food, the waiter and the music good"], "Cambia cada good por un sinónimo preciso.")],
    [
        mc("Un sinónimo es una palabra", "de significado parecido a otra", ["que rima con otra"], "Sirve para no repetir."),
        mc("Un adverbio como quickly dice", "cómo ocurre una acción", ["quién la hace"], "Quickly es rápidamente."),
        ("Escribe en inglés el sinónimo de «small» que significa «muy pequeño» (una palabra de cuatro letras).", "Tiny", "Tiny significa muy pequeño."),
    ],
    task("Mejora este párrafo de tu hoja cambiando las palabras repetidas y uniendo oraciones cortas: «The beach is nice. The water is nice. The sand is nice. We play. We swim. We go home.» (sand = arena; swim = nadar) Escribe una versión de tres oraciones con sinónimos y al menos un conector.",
         "The beach is beautiful and the water is clean. The sand is warm, so we play and swim. When the sun goes down, we go home.",
         ["cambia nice por al menos dos sinónimos distintos", "une oraciones con un conector o con when", "conserva las ideas del párrafo"],
         ["párrafo mejorado de tres oraciones en la hoja"],
         ["usar el mismo sinónimo tres veces", "agregar ideas que no estaban en el original"],
         "Pide que subraye los sinónimos y los conectores que agregó."),
    "Copia los sinónimos del texto y dibuja un símbolo para cada uno.",
    "Elige un párrafo en español de tu cuaderno y marca tres palabras que se repiten; escribe sus sinónimos.",
)

# ============================================================ clase 4: ortografía y apóstrofe (brecha de información)
DRA1 = "«Draft: (1) I dont like rain. (2) Ana's freind lives near the park.»"
FIX1 = "«Correct forms: (1) don't; (2) friend.»"
DRA2 = "«Draft: (1) Its a beautifull day. (2) The dog wagged it's tail.»"
FIX2 = "«Correct forms: (1) It's, beautiful; (2) its.»"
DRA3 = "«Draft: (1) We are diferent but we are freinds. (2) Tomorow is Wednesday and they're bags are here.»"
FIX3 = "«Correct forms: (1) different, friends; (2) Tomorrow, their.»"
GDRA = "(draft = borrador; rain = lluvia; park = parque; beautiful = hermoso; wagged = movió; tail = cola; different = distintos; bags = bolsos)"
DRA4 = "«Draft: (1) My sisters bike is red. (2) The students books are on the desk. (3) Their going to the libary.»"
FIX4 = "«Correct forms: (1) sister's; (2) students'; (3) They're, library.»"
GDRA4 = "(sister's = de mi hermana; students' = de los estudiantes; library = biblioteca)"

lesson(
    OA, 4, MAT,
    "Aprenderé a escribir bien palabras frecuentes y a usar el apóstrofe (') en contracciones y en posesión, y a revisar un borrador con la ayuda de la tarjeta de un compañero. Sirve para que mis textos no pierdan puntos por errores pequeños.",
    ["Sé usar el verbo to be y el presente simple.", "Conozco its, it's, their y they're de oído."],
    [
        "El apóstrofe (apostrophe) tiene dos usos. El primero es la contracción (contraction): junta dos palabras y reemplaza letras que faltan. I am es I'm, do not es don't, it is es it's, they are es they're, cannot es can't. El segundo es la posesión (possession): 's después de un nombre singular indica que algo pertenece a esa persona (Ana's bag, my sister's bike). En un plural regular se agrega solo el apóstrofe después de la s (the students' books).",
        "Hay pares que confunden. It's significa it is; its es el posesivo de las cosas o animales (the dog wagged its tail) y no lleva apóstrofe. They're significa they are; their significa de ellos (their bags); there indica lugar. You're significa you are y your significa tu. Tampoco existe it'is.",
        "También hay palabras frecuentes que se escriben con letras que no suenan: because, friend, beautiful, different, tomorrow, people, together, interesting y Wednesday. Cuando trabajas con una tarjeta (card) de un compañero, él tiene las formas correctas (correct forms) y tú tienes el borrador (draft): lee tu tarjeta, pide la forma que falta y corrige.",
    ],
    [("apostrophe", "apóstrofe: el signo '"), ("contraction", "contracción: dos palabras unidas"), ("possession", "posesión: 's"), ("it's / its", "es / su (de una cosa)"), ("they're / their", "ellos son / de ellos"), ("draft", "borrador"), ("correct forms", "formas correctas")],
    [
        ("Corregir con la tarjeta del compañero", f"Tarjeta A: {DRA1} Tarjeta B: {FIX1} (rain = lluvia; park = parque) Corrige las dos oraciones.",
         ["La forma correcta (1) es don't, que lleva apóstrofe.", "La forma correcta (2) es friend, con i antes de e.", "Las oraciones quedan: I don't like rain. Ana's friend lives near the park."], "I don't like rain. Ana's friend lives near the park."),
        ("Elegir its o it's", "Completa: «The dog wagged ___ tail.» (wagged = movió)",
         ["Its es el posesivo de una cosa o animal.", "It's significa it is: the dog wagged it is tail no tiene sentido.", "Por eso se escribe its."], "its"),
    ],
    [
        ("Escribir «it's tail» para decir la cola del perro.", "It's significa it is; el posesivo de las cosas es its, sin apóstrofe.", "Prueba: ¿se puede decir it is? Si no, es its."),
        ("Escribir «freind» o «becuase».", "Se cambia el orden de las letras de palabras frecuentes.", "Aprende friend y because con su forma exacta."),
    ],
    [
        mc("I do not se contrae en", "I don't", ["I do'nt", "I dont'"], "El apóstrofe va donde falta la o de not."),
        mc("It is se contrae en", "it's", ["its", "it'is"], "It's reemplaza la i de is."),
        mc("¿Cómo se escribe bien la palabra «amigo»?", "Friend", ["Freind", "Fiend"], "Friend lleva i antes de e."),
    ],
    [
        mc(f"Tarjetas: {DRA2} {FIX2} {GDRA} ¿Cómo queda bien escrita la oración (1)?", "It's a beautiful day", ["Its a beautifull day", "It's a beautifull day"], "Hay que corregir el apóstrofe y la ortografía de beautiful."),
        mc(f"Tarjetas: {DRA2} {FIX2} {GDRA} ¿Cómo queda bien escrita la oración (2)?", "The dog wagged its tail", ["The dog wagged it's tail", "The dog wagged its' tail"], "El posesivo its no lleva apóstrofe."),
        mc(f"Tarjetas: {DRA2} {FIX2} Solo tienes la tarjeta con el borrador. ¿Qué le preguntas a tu compañero para la oración (1)?", "What are the correct forms for number 1?", ["Where is the dog?", "Who is Ana?"], "Las formas correctas están en su tarjeta."),
    ],
    [
        mc(f"Tarjetas: {DRA3} {FIX3} {GDRA} ¿Cómo queda bien escrita la oración (1)?", "We are different but we are friends", ["We are diferent but we are friends", "We are different but we are freinds"], "Hay que corregir different y friends."),
        mc(f"Tarjetas: {DRA3} {FIX3} ¿Cómo queda bien escrita la oración (2)?", "Tomorrow is Wednesday and their bags are here", ["Tomorow is Wednesday and their bags are here", "Tomorrow is Wednesday and they're bags are here"], "Their significa de ellos y tomorrow lleva dos r."),
        mc(f"Tarjetas: {DRA4} {FIX4} {GDRA4} ¿Cómo queda la oración (1)?", "My sister's bike is red", ["My sisters bike is red", "My sisters' bike is red"], "Una hermana singular lleva 's."),
    ],
    [
        mc(f"Tarjetas: {DRA4} {FIX4} {GDRA4} ¿Cómo queda la oración (2)?", "The students' books are on the desk", ["The student's books are on the desk", "The students books are on the desk"], "Los libros son de varios estudiantes, con apóstrofe después de la s."),
        mc(f"Tarjetas: {DRA4} {FIX4} {GDRA4} Un compañero corrige la oración (3) como «Their going to the library». ¿Qué le dices?", "Falta they're: They're going to the library", ["Está bien", "Se escribe there going"], "They're es they are; their es de ellos."),
    ],
    [
        mc(f"Tarjetas: {DRA3} {FIX3} Tu compañero dice que la tarjeta B tiene correcciones de tres palabras en (1). ¿Qué compruebas?", "Que la tarjeta dice dos formas en (1): different y friends", ["Que la tarjeta no tiene nada", "Que la tarjeta cambia el significado de Wednesday"], "Hay que leer lo que dice la tarjeta, no suponerlo."),
        mc("Tienes un borrador con 5 palabras mal escritas y tu compañero te lee 4 formas correctas. ¿Qué haces con la quinta?", "Pregunto a mi compañero o uso un diccionario", ["La invento", "La dejo sin revisar"], "Si falta un dato se pregunta o se consulta."),
    ],
    [mc("Escribes un mensaje para el diario mural: «Their is a book fair tomorow.» (book fair = feria del libro) ¿Cuál es la versión correcta?", "There is a book fair tomorrow", ["Their is a book fair tomorrow", "There is a book fair tomorow"], "Corrige there (lugar o existencia) y la ortografía de tomorrow.")],
    [
        mc("¿Cómo se escribe «ellos son» en forma contraída?", "They're", ["Their"], "They're es they are."),
        mc("El posesivo de una cosa o animal es", "its, sin apóstrofe", ["it's, con apóstrofe"], "Su significado es de él o de ella (cosa)."),
        ("Escribe correctamente en inglés la palabra «porque».", "Because", "Because es una palabra frecuente que se escribe con be-cause."),
    ],
    task("Corrige este mensaje con la ayuda de las formas correctas y copia la versión final en tu hoja: «Draft: Its Wednesday and I dont have my book. My freinds house is near, so Im going there.» Correct forms: it's, don't, friend's, I'm. (friend's house = casa de mi amigo)",
         "It's Wednesday and I don't have my book. My friend's house is near, so I'm going there.",
         ["usa cada forma correcta de la lista", "pone el apóstrofe en su lugar", "mantiene el sentido original"],
         ["versión final en la hoja"],
         ["escribir its en vez de it's", "olvidar el apóstrofe en I'm"],
         "Pide que subraye cada palabra corregida y diga qué regla aplicó."),
    "Copia las nueve palabras frecuentes y escríbelas dos veces cada una sin mirar.",
    "Escribe en inglés cinco oraciones con don't, it's, its, they're y friend's.",
)

# ============================================================ clase 5: escritura independiente
PAR1 = "«Last weekend my freind and I went to the park. It was beautiful, because the sun was out. We played soccer, but it's goal was too small. Tomorrow we will go again.»"
GPAR1 = "(weekend = fin de semana; goal = arco; sun was out = había sol; too small = muy pequeño; again = otra vez)"
OP3 = "«I think students should wear comfortable shoes. First, they walk and run a lot during the day. In addition, comfortable shoes protect their feet. As a result, they feel better and learn better.»"
GOP3 = "(comfortable = cómodos; shoes = zapatos; protect = proteger; feet = pies; feel better = sentirse mejor; learn = aprender)"

lesson(
    OA, 5, MAT,
    "Aprenderé a escribir por mi cuenta un párrafo para explicar, narrar u opinar, con palabras variadas, conectores, buena ortografía y apóstrofe. Sirve para producir un texto completo y revisarlo con un criterio.",
    ["Sé usar conectores, sinónimos, apóstrofe y ortografía de palabras frecuentes."],
    [
        "Para escribir un párrafo por tu cuenta, decide el propósito (explicar, narrar u opinar) y escribe una oración principal. Después agrega dos o tres oraciones de apoyo con conectores adecuados y una oración final. Si narras, usa el pasado; si explicas o opinas sobre algo general, usa el presente. Una opinión debe tener al menos una razón con because, so o as a result.",
        "Revisa tu párrafo con una lista de comprobación: ¿está claro el propósito?, ¿usé al menos dos conectores distintos?, ¿cambié las palabras repetidas por sinónimos?, ¿escribí bien las palabras frecuentes?, ¿puse el apóstrofe en las contracciones y en la posesión?, ¿usé its y it's, their y they're donde corresponde?",
        "Al terminar, léelo en voz baja como si fueras otra persona. Si algo suena raro, probablemente falta un conector o hay una palabra repetida. Cada corrección debe mantener el significado original.",
    ],
    [("paragraph", "párrafo"), ("main sentence", "oración principal"), ("supporting sentence", "oración de apoyo"), ("checklist", "lista de comprobación"), ("as a result", "como resultado")],
    [
        ("Revisar un párrafo narrativo", f"Texto: {PAR1} {GPAR1} Corrige los dos errores de ortografía y apóstrofe.",
         ["Freind se escribe friend.", "It's goal es incorrecto: la posesión de una cosa es its.", "El texto corregido dice: my friend ... its goal."], "friend; its goal"),
        ("Identificar los conectores", f"Texto: {OP3} {GOP3} ¿Qué conectores usa para sumar y para dar un resultado?",
         ["Para sumar una razón usa In addition.", "Para el resultado usa As a result.", "También usa First para ordenar."], "In addition suma; as a result da el resultado"),
    ],
    [
        ("Terminar una opinión sin dar ninguna razón.", "No convence a quien lee.", "Agrega al menos una razón con because, so o as a result."),
        ("Cambiar un sinónimo y alterar el significado.", "El sinónimo debe calzar con el contexto.", "Elige una palabra de significado parecido y relee la oración."),
    ],
    [
        mc(f"Lee: {PAR1} {GPAR1} ¿Qué propósito tiene el párrafo?", "Narrar lo que pasó el fin de semana", ["Explicar cómo funciona un parque", "Dar una opinión sobre el fútbol"], "Cuenta un hecho pasado con Last weekend."),
        mc(f"Lee: {OP3} {GOP3} ¿Cuál es la opinión principal?", "Los estudiantes deberían usar zapatos cómodos", ["Los estudiantes deberían correr menos", "Los zapatos cuestan caro"], "La oración principal dice I think students should wear comfortable shoes."),
        mc(f"Lee: {OP3} ¿Qué conector introduce la primera razón?", "First", ["As a result", "Although"], "First ordena la primera razón."),
    ],
    [
        mc(f"Lee: {PAR1} ¿Cuál es el conector de contraste del párrafo?", "But", ["Because", "Tomorrow"], "But une una idea positiva con un problema: jugaron, pero el arco era pequeño."),
        mc(f"Lee: {PAR1} ¿Qué oración está en futuro?", "Tomorrow we will go again", ["We played soccer", "It was beautiful"], "Will go indica futuro."),
        mc(f"Lee: {OP3} {GOP3} ¿Qué oración es el resultado?", "They feel better and learn better", ["They walk and run a lot", "Comfortable shoes protect their feet"], "As a result introduce lo que ocurre al final."),
    ],
    [
        mc(f"Lee: {PAR1} Un compañero cambia «It was beautiful» por «It was tiny». ¿Es un buen sinónimo?", "No, porque tiny significa muy pequeño y cambia el sentido", ["Sí, porque tiny también significa hermoso", "Sí, porque cambia una palabra"], "El sinónimo debe calzar con el contexto."),
        mc(f"Lee: {OP3} ¿Qué razón agregarías para apoyar la opinión?", "Comfortable shoes help students stay active all day", ["Pizza is delicious on Fridays", "The school has two entrances"], "La razón debe estar relacionada con el tema."),
        mc(f"Lee: {PAR1} Quieres evitar repetir «played». ¿Qué cambio mantiene el significado de «We played soccer»?", "We enjoyed a soccer game", ["We watched a soccer game on TV", "We coached a soccer team"], "Enjoyed a soccer game conserva la actividad de jugar."),
    ],
    [
        mc("¿Cuál es el párrafo mejor revisado según la lista de comprobación?", "Last Friday, my friend and I visited a museum. It was interesting, so we stayed two hours. However, the shop was closed", ["Last Friday, my freind and I visited a museum. It's was interesting. We stayed two hours. However the shop were closed", "Friday museum. Interesting. Two hours. Closed"], "Tiene ortografía correcta, conectores y oraciones completas."),
        mc("«I think homework is useful.» ¿Qué oración agrega la mejor razón?", "It helps me remember what I learn", ["It is given every Friday", "Some students do it at home"], "Es una razón relacionada con la opinión."),
    ],
    [
        mc("Un compañero escribe: «Although it was raining, but we played soccer.» Quieres corregir el conector. ¿Cuál es la versión correcta?", "Although it was raining, we played soccer", ["Although it was raining, but we played soccer", "Although it was raining, because we played soccer"], "Con although no se usa but."),
        mc("Tienes que cambiar «It's tail is long» en un texto sobre un perro. ¿Cuál es la versión correcta?", "Its tail is long", ["It's tail is long", "Its' tail is long"], "Its es el posesivo de un animal y no lleva apóstrofe."),
    ],
    [mc("Debes escribir un párrafo de opinión para la revista del colegio sobre el uso de la biblioteca. ¿Qué plan cumple mejor el criterio?", "Opinión con In my opinion, dos razones con because e In addition y una oración final", ["Cuatro oraciones sin conectores", "Solo tres palabras"], "Cumple propósito, razón y conectores.")],
    [
        mc("Antes de escribir, hay que decidir", "si voy a explicar, narrar u opinar", ["el color del lápiz"], "El propósito guía el tiempo verbal y las palabras."),
        mc("Una opinión debe tener", "al menos una razón", ["siete adjetivos"], "Sin razón convence poco."),
        ("Escribe en inglés «como resultado» (tres palabras).", "As a result", "As a result introduce lo que ocurre al final."),
    ],
    task("Escribe un párrafo de cinco oraciones en inglés sobre uno de estos temas (elige uno): (A) Explicar por qué es bueno dormir ocho horas. (B) Narrar lo que hiciste ayer después del colegio. (C) Dar tu opinión sobre usar uniforme. Usa al menos dos conectores distintos, un sinónimo para no repetir una palabra, un apóstrofe y cuida la ortografía de because y friend.",
         "(C) In my opinion, a uniform is useful. First, it makes mornings easier because you don't choose clothes. In addition, it's cheaper for many families. However, some students want more freedom. As a result, I think a simple uniform is a good idea.",
         ["el propósito es claro", "usa al menos dos conectores distintos", "incluye un apóstrofe correcto", "escribe bien because y friend si los usa"],
         ["párrafo de cinco oraciones en la hoja"],
         ["no dar ninguna razón en la opinión", "repetir la misma palabra cuatro veces"],
         "Pide que subraye los conectores y revise con la lista de comprobación."),
    "Copia la lista de comprobación y cuélgala donde escribes tus tareas.",
    "Escribe en inglés cinco oraciones de opinión sobre un tema de tu elección y agrégales una razón con because.",
)

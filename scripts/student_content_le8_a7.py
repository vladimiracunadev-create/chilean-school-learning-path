"""Cuaderno del estudiante, 8.º básico Lengua y Literatura, OA 07 (comedia teatral y crítica social).

Las escenas «La inauguración» y «El banco» son originales, escritas para este cuaderno; el pueblo y los personajes son imaginarios.
Cada ejercicio trae las líneas que necesita.
"""
from __future__ import annotations

from student_content_le8_a import E, L, MAT

OA7 = "LE08 OA 07"

ALC = ("(Plaza de un pueblo imaginario. Un cartel enorme dice «PUENTE NUEVO». No hay puente: solo una cinta atada entre dos postes.) "
       "ALCALDE: (Inflando el pecho.) ¡Vecinos! Hoy inauguro el puente más largo, más firme y más hermoso... ¡de este lado de la plaza! "
       "SECRETARIA: (Entre dientes.) Y el único. "
       "VECINO: Señor alcalde, ¿dónde está el puente? "
       "ALCALDE: Lo está usted mirando. "
       "VECINO: (Mirando el suelo.) ¿Eso es el puente? "
       "ALCALDE: Eso es la primera piedra. Una obra tan grande necesita años de trabajo. ¿Cuántos años necesita, secretaria? "
       "SECRETARIA: Los que dure su cargo, señor alcalde. "
       "ALCALDE: (Encantado.) ¡Exacto! ¡Por eso hay que reelegirme! "
       "(Los vecinos aplauden sin convicción. La secretaria corta la cinta con unas tijeras de papel.)")
BAN = ("(Un parque. ROSA, con un sobre en la mano, se acerca a un JOVEN sentado en un banco.) "
       "ROSA: Disculpe, ¿me puede indicar dónde queda el banco? "
       "JOVEN: (Se para y se aparta.) Aquí lo tiene. Siéntese. "
       "ROSA: No, no, yo necesito depositar este dinero. "
       "JOVEN: ¿Depositar dinero en un banco de madera? "
       "ROSA: ¡En el de las monedas, el que paga intereses! "
       "JOVEN: (Mira el banco.) Este nunca ha pagado intereses... solo dolor de espalda.")
A1 = "ALCALDE: (Inflando el pecho.) ¡Vecinos! Hoy inauguro el puente más largo, más firme y más hermoso... ¡de este lado de la plaza!"
A2 = "SECRETARIA: (Entre dientes.) Y el único."
A3 = "SECRETARIA: Los que dure su cargo, señor alcalde."
A4 = "ALCALDE: (Encantado.) ¡Exacto! ¡Por eso hay que reelegirme!"

# ------------------------------------------------------------------ OA 07 · clase 1
L(OA7, 1,
  MAT,
  "Aprenderé a reconocer los mecanismos de la comedia (equívoco, ironía, exageración y contraste) en un texto teatral y a explicar por qué provocan risa.",
  ["Reconozco diálogos y acotaciones.", "Conozco conflicto, personajes tipo e hipérbole."],
  ["La comedia es un género dramático que busca provocar risa a partir de situaciones, personajes y palabras. Suele mostrar conflictos que no son trágicos, y muchas veces termina con la situación aclarada o resuelta; pero no todas las comedias tienen un final feliz, y un final feliz por sí solo no hace comedia. Lo que la define es cómo se produce la risa.",
   "Los mecanismos más frecuentes son cuatro. El equívoco es un malentendido que nace de una palabra con dos sentidos, como «banco» (asiento o institución). La ironía consiste en decir una cosa para dar a entender otra o en mostrar una contradicción entre lo dicho y la realidad. La exageración agranda algo hasta hacerlo ridículo. El contraste muestra una distancia entre lo que se anuncia y lo que ocurre, como un cartel que dice «PUENTE NUEVO» frente a una cinta entre dos postes.",
   "Para explicar un mecanismo se cita la línea y se dice qué dos cosas chocan. En «La inauguración», el alcalde anuncia «el puente más largo… de este lado de la plaza» y la secretaria responde «Y el único»: la exageración del alcalde se desinfla con una ironía. Reconocer el mecanismo permite entender que la risa tiene causa y, a veces, una intención más allá del chiste."],
  [("comedia", "género dramático que busca provocar risa con situaciones, personajes y palabras"), ("equívoco", "malentendido por una palabra con dos sentidos"), ("ironía", "decir una cosa para dar a entender otra o mostrar una contradicción"), ("contraste", "distancia entre lo que se anuncia y lo que ocurre")],
  [("Reconocer el equívoco", BAN + " ¿Qué palabra produce el equívoco?",
    ["Rosa pregunta por «el banco» para depositar dinero.", "El joven entiende un asiento.", "La palabra es «banco»."],
    "«banco»"),
   ("Reconocer la ironía", A1 + " " + A2 + " ¿Qué efecto tiene la respuesta de la secretaria?",
    ["El alcalde exagera.", "La secretaria agrega «Y el único», que revela que solo hay uno.", "Es una ironía que desinfla la exageración."],
    "Ironía: desinfla la exageración")],
  [("Pensar que comedia significa solo final feliz.", "Se confunde género con desenlace.", "Busca qué mecanismos provocan la risa."),
   ("Citar el chiste sin explicar qué choca.", "Se confía en que la risa se entiende sola.", "Explica qué dos ideas se contradicen.")],
  ([E("En «El banco», ROSA y el JOVEN entienden de distinta forma la palabra «banco». ¿Qué mecanismo es: equívoco o contraste?", "Equívoco", "Un mismo término tiene dos sentidos."),
    E("El alcalde anuncia «el puente más largo, más firme y más hermoso». ¿Qué mecanismo domina en esa frase: exageración o equívoco?", "Exageración", "Agranda el puente hasta hacerlo ridículo, sin que haya una palabra con dos sentidos."),
    E("El cartel dice «PUENTE NUEVO» y solo hay una cinta entre dos postes. ¿Qué mecanismo es: contraste o rima?", "Contraste", "Lo anunciado no coincide con lo que se ve.")],
   [E("Escena: " + A3 + " ¿Qué mecanismo hay en «Los que dure su cargo»: ironía o equívoco?", "Ironía", "Sugiere que la obra nunca terminará mientras el alcalde siga en su puesto."),
    E("JOVEN: «Este nunca ha pagado intereses... solo dolor de espalda». ¿Qué sentido de «banco» usa el joven? A) asiento B) institución financiera C) árbol", "A) asiento", "Habla de sentarse y de dolor de espalda."),
    E("¿Cuál NO es un mecanismo de comedia de la clase? A) equívoco B) invocación a las musas C) ironía", "B) invocación a las musas", "Es un rasgo de la epopeya, no de la comedia.")],
   [E("Clasifica con E (equívoco), I (ironía) o X (exageración): 1) «el puente más largo… de este lado de la plaza», 2) «Y el único», 3) «¿depositar dinero en un banco de madera?». Escribe las tres letras en orden.", "X, I, E", "El primero agranda, el segundo contradice con ironía y el tercero juega con dos sentidos de «banco»."),
    E("Comedia: un personaje anuncia con gran ceremonia una fiesta y luego aparece con un pastel sin velas y sin invitados. ¿Qué mecanismo domina: contraste o equívoco?", "Contraste", "Lo anunciado y lo que ocurre no coinciden."),
    E("¿Por qué una comedia puede no tener final feliz? A) porque lo que define la comedia es cómo provoca risa B) porque en realidad siempre termina en tragedia C) porque el final no importa en ningún género", "A) porque lo que define la comedia es cómo provoca risa", "Los mecanismos y no el final definen el género.")],
   [E("Un lector dice: «La inauguración no es comedia porque el alcalde no se casa al final». ¿Qué error comete?", "Confunde comedia con final feliz", "El género se define por los mecanismos de la risa."),
    E("En «La inauguración», ¿qué dos cosas chocan en «el puente más largo… de este lado de la plaza»? A) lo grandioso del anuncio y lo pequeño del espacio B) la hora y el lugar C) el alcalde y la secretaria", "A) lo grandioso del anuncio y lo pequeño del espacio", "La frase promete mucho y aclara un límite ridículo.")],
   [E("El alcalde pregunta: «Una obra tan grande necesita años de trabajo. ¿Cuántos años necesita, secretaria?». ¿Qué prepara su pregunta: la ironía de la secretaria o el equívoco del banco?", "La ironía de la secretaria", "Su respuesta, «Los que dure su cargo», nace de esa pregunta."),
    E("Si la secretaria solo dijera «Sí, señor alcalde» y no agregara «Y el único», ¿se perdería el efecto cómico que desinfla la exageración?", "Sí", "La ironía de «Y el único» es la que revela la contradicción con la realidad.")]),
  [E("En una función escolar, un personaje dice: «Voy a dar un discurso breve» y habla durante una hora. ¿Qué mecanismo domina: contraste o equívoco?", "Contraste", "Lo anunciado (breve) contradice lo que ocurre.")],
  [E("¿Qué es un equívoco?", "Un malentendido por una palabra con dos sentidos", "Produce confusión y risa."),
   E("¿Qué es la ironía?", "Decir una cosa para dar a entender otra", "Muestra una contradicción."),
   E("¿Una comedia siempre tiene final feliz?", "No", "Lo que la define es el mecanismo de la risa.")],
  ("Con la escena «La inauguración» (" + ALC + "), escribe tres mecanismos de comedia con su cita y explica en una frase por qué provocan risa.",
   "Exageración: «el puente más largo… de este lado de la plaza». Ironía: «Y el único». Contraste: el cartel «PUENTE NUEVO» y una cinta entre postes. Provocan risa porque lo que se dice choca con lo que se ve.",
   ["identifica tres mecanismos", "cita cada uno", "explica por qué chocan"], ["tres citas y una frase"], ["citar sin explicar"], "Comprueba que cada mecanismo tenga cita exacta."),
  "Piensa en un chiste de equívoco que conozcas y explica a alguien de tu casa por qué funciona.",
  "Escribe un diálogo de cuatro líneas con un equívoco usando la palabra «llama».")

# ------------------------------------------------------------------ OA 07 · clase 2
L(OA7, 2,
  MAT,
  "Aprenderé a analizar el conflicto cómico y el desarrollo de un equívoco: cómo nace, cómo se acumula y cómo se aclara.",
  ["Reconozco mecanismos de la comedia.", "Delimito conflictos en un texto dramático."],
  ["En una comedia, el conflicto suele ser una dificultad poco grave que enreda a los personajes. Un personaje quiere algo, y algo (un malentendido, su propia torpeza, una contradicción) se lo complica de manera divertida. En «El banco», Rosa quiere depositar dinero y el joven le muestra un asiento. El conflicto cómico no amenaza a nadie: lo que está en juego es salir del enredo.",
   "El equívoco se desarrolla en tres pasos. Primero nace: una palabra con dos sentidos («banco») se interpreta de manera distinta. Luego se acumula: cada respuesta agrega confusión («¿Depositar dinero en un banco de madera?»). Finalmente se aclara: Rosa explica que habla del banco «que paga intereses». Lo cómico depende de que el público conozca los dos sentidos y vea el malentendido antes que los personajes.",
   "Para analizar un conflicto cómico se pregunta: ¿qué quiere cada personaje?, ¿qué lo complica?, ¿quién sabe más, los personajes o el público?, ¿cómo se resuelve? A veces la resolución es una frase ingeniosa, como la del joven: «Este nunca ha pagado intereses... solo dolor de espalda». Esa frase cierra el enredo con un nuevo juego de ideas y deja la sensación de que la situación fue entendida por todos."],
  [("conflicto cómico", "dificultad poco grave que enreda a los personajes de manera divertida"), ("malentendido", "interpretación equivocada de lo que otro dijo"), ("aclaración", "momento en que se resuelve el equívoco"), ("público", "personas que ven la obra y pueden saber más que los personajes")],
  [("Tres pasos del equívoco", BAN + " ¿Cuándo nace el equívoco?",
    ["Nace con la pregunta por «el banco».", "El joven entiende un asiento.", "Nace en la primera pregunta de Rosa."],
    "Cuando Rosa pregunta dónde queda el banco"),
   ("La aclaración", "ROSA: «¡En el de las monedas, el que paga intereses!» ¿Qué cumple esta línea en el equívoco?",
    ["Rosa aclara el sentido que ella usaba.", "Resuelve el malentendido.", "Es la aclaración."],
    "Aclara el malentendido")],
  [("Creer que el conflicto cómico es peligroso para los personajes.", "Se confunde con un conflicto dramático grave.", "Observa que el enredo se resuelve con una aclaración."),
   ("Explicar el chiste sin decir qué sentidos chocan.", "Se omite el análisis.", "Señala los dos sentidos de la palabra.")],
  ([E("En «El banco», ¿qué quiere ROSA: depositar dinero o sentarse?", "Depositar dinero", "Lo dice: «necesito depositar este dinero»."),
    E("¿Qué entiende el JOVEN al principio: un asiento o una institución?", "Un asiento", "Se aparta y le ofrece sentarse."),
    E("¿Cómo termina el equívoco: con una aclaración o con una pelea?", "Con una aclaración", "Rosa explica a qué banco se refiere.")],
   [E("«¿Depositar dinero en un banco de madera?» ¿Qué paso del equívoco es: nacimiento, acumulación o aclaración?", "Acumulación", "Agrega más confusión al malentendido."),
    E("El público conoce los dos sentidos de «banco». ¿Quién sabe más al inicio: el público o los personajes?", "El público", "Entiende el doble sentido antes que Rosa y el joven."),
    E("«Este nunca ha pagado intereses... solo dolor de espalda.» ¿Qué sentido de banco usa? A) el asiento B) el financiero", "A) el asiento", "Habla del banco de madera donde se sienta.")],
   [E("Escena: «Quiero una cuenta». «Aquí tiene: uno, dos, tres...». ¿Qué dos sentidos de «cuenta» producen el equívoco? A) cuenta de banco y contar números B) cuenta de agua y cuenta de luz C) cuenta de collar y cuenta de pan", "A) cuenta de banco y contar números", "Una persona pide una cuenta bancaria y otra empieza a contar."),
    E("Ordena los pasos de un equívoco: (a) aclaración, (b) acumulación, (c) nacimiento. Escribe el orden correcto.", "c, b, a", "Primero nace, luego se acumula y finalmente se aclara."),
    E("Si Rosa hubiera dicho desde el principio «necesito un banco para depositar», ¿se habría producido el equívoco igual?", "No", "La aclaración inicial lo evitaría.")],
   [E("Un lector afirma: «El conflicto de “El banco” es que Rosa corre peligro». ¿Qué responde la clase? A) es un conflicto cómico poco grave que se resuelve con una aclaración B) tiene razón C) no hay conflicto porque nadie discute", "A) es un conflicto cómico poco grave que se resuelve con una aclaración", "Nada amenaza a Rosa."),
    E("El joven dice «solo dolor de espalda». ¿Qué efecto tiene esta frase final: cierra el enredo con humor o abre otro conflicto?", "Cierra el enredo con humor", "Vuelve al sentido del asiento como remate.")],
   [E("Cuenta las intervenciones que hay en «El banco» (cada línea con nombre y dos puntos): «" + BAN + "»", "6", "ROSA habla tres veces y el JOVEN tres veces: seis en total.", "6"),
    E("¿Cuántas intervenciones tiene el JOVEN en «El banco»?", "3", "Habla en tres ocasiones.", "3")]),
  [E("En tu curso, alguien pide «la regla» para dibujar y le entregan el reglamento del colegio. ¿Qué mecanismo cómico ocurre: equívoco o ironía?", "Equívoco", "La palabra «regla» tiene dos sentidos.")],
  [E("¿Cómo se llama el momento en que se resuelve un equívoco?", "Aclaración", "Termina el malentendido."),
   E("¿Quién conoce los dos sentidos de la palabra al inicio: el público o los personajes?", "El público", "Ve el enredo antes."),
   E("¿El conflicto cómico suele ser grave?", "No", "Es una dificultad poco grave.")],
  ("Con «El banco» (" + BAN + "), escribe: 1) lo que quiere cada personaje, 2) cómo nace el equívoco, 3) cómo se acumula y se aclara, con una cita para cada paso.",
   "Rosa quiere depositar dinero; el joven quiere ayudar a una persona. El equívoco nace en «¿me puede indicar dónde queda el banco?». Se acumula en «¿Depositar dinero en un banco de madera?» y se aclara en «el que paga intereses».",
   ["delimita qué quiere cada personaje", "describe los tres pasos", "cita cada paso"], ["tres respuestas con cita"], ["no distinguir los sentidos"], "Verifica que cada paso tenga su cita."),
  "Inventa un equívoco con la palabra «sierra» y escríbelo en tres líneas.",
  "Escribe un diálogo de cinco líneas con un equívoco que se aclare al final.")

# ------------------------------------------------------------------ OA 07 · clase 3
L(OA7, 3,
  MAT,
  "Aprenderé a examinar personajes tipo de la comedia sin naturalizarlos, distinguiendo reírse de una conducta de burlarse de un grupo de personas.",
  ["Reconozco mecanismos y conflicto cómico.", "Conozco personajes tipo."],
  ["La comedia usa personajes tipo: figuras que repiten rasgos fáciles de reconocer. En «La inauguración» aparecen el fanfarrón o vanidoso (el alcalde, que exagera sus logros), la secretaria avispada (que desinfla las exageraciones con ironía) y el vecino ingenuo (que pregunta lo que otros callan). Estos tipos son moldes literarios que sirven para mostrar conductas: la vanidad, la astucia, la ingenuidad.",
   "Naturalizar un tipo es presentarlo como si fuera así por naturaleza o como si todas las personas de un grupo fueran así. Eso daña. La risa puede dirigirse a una conducta (prometer una obra que no existe) o a una identidad (reírse de las personas por su edad, su origen, su género o su oficio). La primera ayuda a pensar. La segunda reproduce estereotipos. En «La inauguración» la risa recae en la vanidad del alcalde, no en los alcaldes como grupo.",
   "Para analizar un personaje tipo se hacen cuatro preguntas. ¿Qué rasgo repite? ¿Qué conducta se critica? ¿La risa recae en la conducta o en una identidad? ¿Se podría lograr el mismo efecto sin ofender a un grupo? Un buen texto cómico puede usar tipos y, a la vez, darles matices que eviten el estereotipo: la secretaria no es simplemente «la lista»: su ironía es una forma de crítica al poder."],
  [("personaje tipo", "personaje que repite rasgos conocidos"), ("naturalizar", "presentar algo como si fuera natural o propio de todo un grupo"), ("fanfarrón", "persona que presume de lo que no tiene o no hizo"), ("estereotipo", "imagen simplificada y fija de un grupo")],
  [("Reconocer el tipo", A1 + " ¿Qué tipo de personaje es el alcalde?",
    ["Presume de lo que no existe.", "Exagera sus logros.", "Es un fanfarrón."],
    "Un fanfarrón o vanidoso"),
   ("¿Conducta o identidad?", "Un chiste dice: «Los alcaldes prometen mucho y cumplen poco, como este». Otro dice: «Los adultos mayores no entienden nada». ¿Cuál se ríe de una conducta y cuál de una identidad?",
    ["El primero señala una conducta: prometer sin cumplir.", "El segundo se burla de un grupo por su edad.", "Primero: conducta; segundo: identidad."],
    "Primero conducta; segundo identidad")],
  [("Pensar que un personaje tipo describe a todas las personas de un grupo.", "Se confunde molde literario con realidad.", "Pregunta qué conducta se critica y si la risa recae en un grupo."),
   ("Defender un chiste ofensivo diciendo «es solo comedia».", "Se ignora el efecto en las personas.", "Propón una versión que logre la risa sin ofender.")],
  ([E("¿Un personaje que presume de lo que no tiene es un fanfarrón o un ingenuo?", "Un fanfarrón", "Presume sin respaldo."),
    E("El vecino que pregunta «¿dónde está el puente?» ¿es el ingenuo o el vanidoso?", "El ingenuo", "Pregunta lo que otros callan."),
    E("La secretaria que responde con ironía, ¿desinfla las exageraciones o las aplaude?", "Las desinfla", "Con «Y el único» revela la realidad.")],
   [E("En «La inauguración», ¿qué conducta se critica: prometer obras que no existen o ser secretaria?", "Prometer obras que no existen", "La risa recae en la conducta del alcalde."),
    E("Un chiste dice: «Las personas de tal oficio son todas torpes». ¿Se ríe de una conducta o de un grupo?", "De un grupo", "Atribuye un rasgo a todas las personas de un oficio."),
    E("¿Qué significa naturalizar un tipo? A) presentarlo como si todos los de un grupo fueran así B) darle un nombre propio C) ponerlo en la primera escena", "A) presentarlo como si todos los de un grupo fueran así", "Convierte un molde en una supuesta verdad.")],
   [E("Un guion cambia el chiste «Los políticos mienten» por «Este político prometió un puente y no hay ni una piedra». ¿Cuál es más específico y menos generalizador?", "El segundo", "Señala un hecho concreto y no a todo un grupo."),
    E("Un personaje dice: «Los del curso de al lado siempre llegan tarde». ¿Se ríe de una conducta o de un grupo?", "De un grupo", "Atribuye un rasgo a todo un grupo de personas."),
    E("¿Cuál reescritura mantiene la risa sin ofender a un grupo? A) «Este alcalde tarda tanto que el puente ya es una leyenda» B) «Los alcaldes son todos unos farsantes» C) «Las secretarias son listillas por naturaleza»", "A) «Este alcalde tarda tanto que el puente ya es una leyenda»", "Se ríe de una conducta concreta de un personaje.")],
   [E("Un lector dice: «La secretaria es solo la lista de siempre». ¿Qué matiz le aporta la crítica? A) su ironía revela el abuso del poder B) su cargo de secretaria C) que obedece siempre al alcalde", "A) su ironía revela el abuso del poder", "No es un adorno, sino una voz crítica."),
    E("Un compañero dice: «Es solo comedia, no importa a quién ofenda». ¿Qué responde la clase? A) el humor puede criticar conductas sin ofender a un grupo B) tiene razón C) las comedias no tienen efectos", "A) el humor puede criticar conductas sin ofender a un grupo", "La risa tiene efectos en las personas.")],
   [E("Clasifica con C (se ríe de una conducta) o G (se ríe de un grupo): 1) «El alcalde infla sus logros», 2) «Los jóvenes nunca hacen nada», 3) «El vecino ingenuo pregunta lo evidente». Escribe las tres letras en orden.", "C, G, C", "El segundo atribuye un rasgo fijo a todo un grupo."),
    E("De los tres personajes tipo de la escena (fanfarrón, secretaria avispada, vecino ingenuo), ¿cuál funciona como voz crítica?", "La secretaria avispada", "Su ironía muestra la contradicción del alcalde.")]),
  [E("Para el día del curso, un grupo prepara un sketch sobre un director de colegio que presume de logros inexistentes. Otro compañero propone burlarse de los profesores de cierta asignatura. ¿Cuál propuesta evita naturalizar un estereotipo?", "La del director que presume de logros inexistentes", "Se ríe de una conducta, no de un grupo.")],
  [E("¿Un personaje tipo es un molde literario o una persona real?", "Un molde literario", "Repite rasgos para mostrar conductas."),
   E("¿La risa puede recaer en una conducta o en una identidad?", "Sí", "Conviene dirigirla a la conducta."),
   E("¿Qué pregunta ayuda a evitar un estereotipo?", "¿La risa recae en una conducta o en un grupo?", "Orienta la crítica.")],
  ("Reescribe este chiste para que se ría de una conducta y no de un grupo: «Las secretarias siempre son más inteligentes que sus jefes». Usa la escena (" + ALC + ") como modelo y escribe también por qué tu versión es mejor.",
   "«Esta secretaria sabe tan bien lo que ocurre que cada respuesta suya desinfla una promesa». Es mejor porque ya no generaliza sobre todas las secretarias; se ríe de la distancia entre lo prometido y lo real.",
   ["elimina la generalización", "mantiene una conducta concreta", "explica el cambio"], ["chiste reescrito y una frase"], ["mantener el estereotipo"], "Verifica que tu versión no use «todas», «siempre» ni «nunca» sobre un grupo."),
  "Conversa con alguien de tu casa sobre una vez en que un chiste molestó a alguien y por qué.",
  "Escribe un diálogo de cinco líneas con un personaje fanfarrón y otro que lo desinfla con ironía.")

# ------------------------------------------------------------------ OA 07 · clase 4
L(OA7, 4,
  MAT,
  "Aprenderé a relacionar el humor con la crítica: qué se critica, a quién, con qué recurso y para qué.",
  ["Reconozco mecanismos cómicos y personajes tipo.", "Distingo conducta e identidad."],
  ["La comedia no solo busca hacer reír: puede criticar costumbres, vicios o abusos de una sociedad. Esta función se llama crítica social. El humor suaviza el golpe y permite que el público mire de frente algo que quizá incomoda. En «La inauguración», se critica una conducta de las autoridades: prometer obras enormes que nunca se terminan para conseguir más tiempo en el cargo.",
   "Para analizar la crítica se responden cuatro preguntas. ¿Qué se critica? Aquí, las promesas vacías. ¿Quién la representa? El alcalde, un personaje inventado. ¿Con qué recurso? Exageración («el puente más largo»), ironía («Los que dure su cargo») y contraste (cartel y cinta). ¿Para qué? Para hacer pensar en la distancia entre lo que se promete y lo que se hace. La crítica se apoya en citas, no en suposiciones.",
   "La sátira es una forma de comedia que critica de manera directa vicios o abusos con humor. No debe confundirse con la burla de personas concretas. La crítica de «La inauguración» no se dirige a una persona real, sino a una conducta posible en cualquier lugar. Un criterio útil: la crítica es sólida cuando se puede explicar con evidencia del texto y respeta a las personas reales, y es débil cuando solo insulta."],
  [("crítica social", "señalamiento de defectos, abusos o costumbres de una sociedad"), ("sátira", "forma de comedia que critica vicios o abusos con humor"), ("promesa vacía", "oferta que no se piensa cumplir"), ("recurso", "medio que usa el texto para producir un efecto")],
  [("Qué se critica", ALC + " ¿Qué se critica en la escena?",
    ["El alcalde anuncia un puente inexistente.", "Pide años y luego más años en el cargo.", "Se critica prometer obras que no se cumplen."],
    "Las promesas vacías de las autoridades"),
   ("Con qué recurso", A3 + " " + A4 + " ¿Qué recurso refuerza la crítica?",
    ["La secretaria dice «los que dure su cargo».", "El alcalde lo celebra sin ver la ironía.", "Es una ironía: la obra no terminará mientras él siga."],
    "Ironía")],
  [("Pensar que el humor no puede criticar.", "Se cree que la risa es solo entretención.", "Pregunta qué se critica y con qué recurso."),
   ("Confundir crítica con insulto.", "Se pierde el apoyo en el texto.", "Explica la crítica con una cita.")],
  ([E("En «La inauguración», ¿qué se critica: las promesas vacías o la pintura de los postes?", "Las promesas vacías", "Se muestra una obra anunciada que no existe."),
    E("¿Quién representa la conducta criticada: el alcalde o el vecino?", "El alcalde", "Es quien promete y exagera."),
    E("La sátira, ¿critica con humor o solo insulta?", "Critica con humor", "Es su definición.")],
   [E("«Los que dure su cargo». ¿Qué crítica hace la secretaria? A) que la obra no termina mientras él siga B) que el puente es muy grande C) que el cartel es feo", "A) que la obra no termina mientras él siga", "Es una ironía sobre el uso de la obra para prolongar el cargo."),
    E("El cartel «PUENTE NUEVO» frente a una cinta entre postes critica... ¿la distancia entre lo anunciado y lo hecho o el precio de un cartel?", "La distancia entre lo anunciado y lo hecho", "Es un contraste que revela una promesa vacía."),
    E("«Por eso hay que reelegirme.» ¿Qué muestra del alcalde: su deseo de seguir en el cargo o su deseo de terminar la obra?", "Su deseo de seguir en el cargo", "Usa la obra como excusa.")],
   [E("Clasifica con Q (qué se critica), R (recurso) o P (para qué): 1) promesas vacías, 2) hacer pensar en la distancia entre lo prometido y lo hecho, 3) ironía y contraste. Escribe las tres letras en orden.", "Q, P, R", "Las promesas vacías son lo criticado; hacer pensar es el propósito; ironía y contraste son los recursos."),
    E("Un sketch exagera que un delegado de curso promete «un recreo de tres horas» y nunca lo logra. ¿Qué crítica social tiene, en pequeño? A) las promesas vacías B) la rima C) la acotación", "A) las promesas vacías", "Es la misma conducta que la escena."),
    E("¿La crítica de la escena apunta a una persona real o a una conducta posible?", "A una conducta posible", "El pueblo y los personajes son imaginarios.")],
   [E("Un lector dice: «La escena insulta a los alcaldes». ¿Qué responde la clase? A) critica una conducta con humor, no insulta a las personas B) tiene razón C) no hay crítica", "A) critica una conducta con humor, no insulta a las personas", "La sátira se dirige a una conducta."),
    E("¿Cuándo es sólida la crítica de una comedia: cuando se explica con citas y respeta a las personas, o cuando insulta fuerte?", "Cuando se explica con citas y respeta a las personas", "La evidencia da peso a la crítica.")],
   [E("Al final, los vecinos aplauden sin convicción. ¿Qué hace ese gesto: confirma la promesa del alcalde o la cuestiona en silencio?", "La cuestiona en silencio", "La acotación «sin convicción» muestra que no creen en lo prometido."),
    E("Si la secretaria no dijera «Los que dure su cargo», ¿la crítica de la escena sería igual de fuerte?", "No", "Su ironía revela el uso político de la obra.")]),
  [E("Un programa escolar de humor satiriza a un centro de alumnos que anuncia un gimnasio y solo entrega una pelota. ¿Qué mecanismo de la escena imita: el contraste entre lo anunciado y lo entregado o el equívoco?", "El contraste entre lo anunciado y lo entregado", "Es la distancia entre la promesa y el hecho.")],
  [E("¿Qué es la sátira?", "Una comedia que critica vicios o abusos con humor", "Une risa y crítica."),
   E("¿Qué cuatro preguntas ayudan a analizar la crítica?", "Qué, quién, con qué recurso y para qué", "Permiten explicar con evidencia."),
   E("¿La crítica debe apoyarse en citas?", "Sí", "No en suposiciones.")],
  ("Analiza la crítica de «La inauguración» (" + ALC + ") con las cuatro preguntas (qué, quién, recurso, para qué), cada una con una cita, y escribe una frase final sobre por qué esta crítica no ataca a una persona real.",
   "Qué: las promesas vacías. Quién: el alcalde. Recurso: la ironía «Los que dure su cargo» y el contraste del cartel. Para qué: hacer pensar en la distancia entre prometer y cumplir. No ataca a una persona real porque el pueblo y los personajes son imaginarios y la crítica es a una conducta.",
   ["responde las cuatro preguntas", "cita cada recurso", "distingue conducta y persona"], ["cuatro respuestas y una frase"], ["insultar", "criticar sin citas"], "Verifica que cada respuesta tenga cita."),
  "Piensa en una promesa que se hizo en tu entorno y no se cumplió, y escribe una frase irónica sobre ella sin nombrar a nadie.",
  "Escribe una escena de cuatro líneas que critique con humor una conducta escolar.")

# ------------------------------------------------------------------ OA 07 · clase 5
L(OA7, 5,
  MAT,
  "Aprenderé a interpretar una comedia desde su contexto: qué dato de época, lugar o costumbre se necesita para entender el humor y cómo cambia la risa con el tiempo.",
  ["Analizo mecanismos, personajes y crítica.", "Distingo contexto y evidencia del texto."],
  ["El humor depende del contexto: de lo que el público conoce, de las costumbres, de las instituciones y de las palabras de su época. Una broma que hoy funciona puede no entenderse dentro de cincuenta años, y una comedia escrita hace mucho puede requerir una explicación para que hoy se comprenda. Interpretar desde el contexto significa preguntar qué sabe el público de esa época y qué critica la obra en su momento.",
   "Las comedias de épocas pasadas solían burlarse de vicios muy conocidos, como la vanidad, la avaricia o el engaño, y de situaciones de su tiempo. Para leerlas hoy se investiga el contexto con una ficha: época, lugar, público, costumbres y fuentes. Para este cuaderno hay una ficha inventada de «La inauguración»: se escribió para un pueblo imaginario donde las obras públicas se anunciaban con carteles. Es una ficha de ejemplo, no un hecho histórico.",
   "El contexto ayuda, pero no reemplaza el análisis del texto. Hay que distinguir entre lo que el texto dice y lo que suponemos de su época. Además, al leer una comedia antigua conviene preguntar si todas las bromas se pueden defender hoy: algunas se apoyan en prejuicios que hoy se cuestionan. Reconocerlo no obliga a descartar la obra; permite leerla de manera crítica y respetuosa, separando el valor de sus mecanismos del daño de ciertos estereotipos."],
  [("contexto", "circunstancias de época, lugar y costumbres en que se crea y se recibe una obra"), ("público", "personas a quienes se dirige la obra"), ("ficha de contexto", "resumen de datos de época, lugar y fuente de una obra"), ("vigencia", "capacidad de una obra de seguir teniendo sentido hoy")],
  [("Necesito un dato de contexto", "En una comedia antigua, un personaje dice: «No me cobres con moneda de plata, que ya no vale nada». ¿Qué dato de contexto necesitas para entender el chiste?",
    ["El chiste se apoya en el valor de una moneda.", "Hay que saber qué pasaba con ese dinero en esa época.", "Necesito datos sobre la moneda de esa época."],
    "Qué valor tenía esa moneda en la época de la obra"),
   ("Vigencia", ALC + " ¿Por qué esta crítica puede seguir vigente?",
    ["Prometer obras que no se cumplen puede ocurrir en distintas épocas.", "No depende de una moneda ni de una costumbre específica.", "Sigue vigente porque la conducta es reconocible hoy."],
    "Porque prometer sin cumplir es una conducta reconocible en distintas épocas")],
  [("Suponer datos de época sin fuente.", "Se confía en la intuición.", "Rotula lo que supones y busca una fuente."),
   ("Usar el contexto para reemplazar la evidencia del texto.", "Se cree que el contexto explica todo.", "Cita el texto y luego agrega el contexto.")],
  ([E("El humor depende del contexto: ¿verdadero o falso?", "Verdadero", "Depende de lo que el público conoce."),
    E("Una ficha de contexto resume... ¿época y lugar de una obra o el color de su portada?", "Época y lugar de una obra", "Entrega datos útiles para leerla."),
    E("La ficha de «La inauguración» de este cuaderno, ¿es histórica o inventada?", "Inventada", "El pueblo y la ficha son imaginarios.")],
   [E("Una comedia antigua incluye un chiste sobre una costumbre que ya no existe. ¿Qué necesitas para entenderlo: una ficha de contexto o el nombre del autor?", "Una ficha de contexto", "Explica la costumbre."),
    E("«Hay que reelegirme.» ¿Depende este chiste de una costumbre de época o de una conducta reconocible hoy?", "De una conducta reconocible hoy", "Prometer para seguir en el cargo se entiende sin datos especiales."),
    E("¿Las comedias de épocas pasadas solían burlarse de vicios como la vanidad o de la cordura?", "De vicios como la vanidad", "Eran temas comunes en el humor teatral.")],
   [E("Un chiste antiguo se ríe de las personas por su origen. Hoy se cuestiona ese tipo de burla. ¿Qué debe hacer un lector crítico? A) reconocer el mecanismo y cuestionar el estereotipo B) reírse sin pensar C) borrar la obra", "A) reconocer el mecanismo y cuestionar el estereotipo", "Se puede analizar sin justificar el prejuicio."),
    E("Dos lectores: Ana dice que una comedia antigua «no sirve» porque no entiende el contexto; Beto investiga la ficha de contexto. ¿Quién sigue la clase?", "Beto", "Investiga antes de descartar."),
    E("¿Qué conviene indicar sobre un dato de contexto sin fuente? A) que es una suposición B) que es seguro C) que no importa", "A) que es una suposición", "Es la manera honesta de presentarlo.")],
   [E("Un texto escribe: «El contexto prueba que el autor pensaba así». ¿Qué falta? A) evidencia del texto B) más datos de épocas distintas C) la opinión de otros lectores", "A) evidencia del texto", "El contexto no reemplaza el análisis."),
    E("Un chiste se apoya en una palabra que cambió de significado con el tiempo. ¿Qué tipo de dato de contexto necesitas: lingüístico o geográfico?", "Lingüístico", "Es el significado de las palabras en esa época.")],
   [E("Ordena los pasos de una lectura contextual: (a) leer el texto y marcar chistes, (b) investigar la ficha de contexto, (c) explicar el efecto con cita y dato. Escribe el orden.", "a, b, c", "Primero se lee, luego se investiga el contexto y al final se explica."),
    E("¿Qué dos cosas debe incluir la explicación final: cita del texto y dato de contexto, o solo el dato?", "Cita del texto y dato de contexto", "Ambas se apoyan mutuamente.")]),
  [E("Quieres entender una comedia escolar de hace muchos años. En una conversación con alguien mayor te cuentan cómo se organizaba el curso. ¿Qué tipo de fuente obtuviste: un testimonio o un documento oficial?", "Un testimonio", "Es información contada por una persona que vivió esa época.")],
  [E("En Lenguaje: ¿Qué es el contexto?", "Las circunstancias de época, lugar y costumbres de una obra", "Ayuda a entender el humor."),
   E("¿Un dato de contexto sin fuente es una suposición?", "Sí", "Debe rotularse como tal."),
   E("¿El contexto reemplaza al texto?", "No", "Se usa junto con las citas.")],
  ("Escribe una interpretación de «La inauguración» (" + ALC + ") en seis líneas con: 1) un chiste citado, 2) qué dato de contexto de la ficha inventada ayudaría, 3) por qué la crítica sigue vigente, 4) una advertencia sobre lo que no sabemos.",
   "Chiste: «Los que dure su cargo». La ficha dice que en el pueblo imaginario se anunciaban obras con carteles, lo que explica el contraste. La crítica sigue vigente porque prometer sin cumplir se reconoce en cualquier época. No sabemos si en el pueblo real existió algo parecido, porque la ficha es inventada.",
   ["cita un chiste", "usa un dato de contexto rotulado", "señala vigencia y límite"], ["interpretación de seis líneas"], ["tratar la ficha como real"], "Marca la parte inventada de la ficha."),
  "Pregunta a alguien de tu casa qué chiste de su juventud ya no se entendería hoy y por qué.",
  "Escribe tres preguntas de contexto que harías antes de leer una comedia antigua.")

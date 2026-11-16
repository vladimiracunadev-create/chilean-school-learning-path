"""Cuaderno del estudiante, 3.º medio Inglés (Formación General), OA 03 (recursos del inglés) y OA 04 (interacción, visiones de mundo e identidad).

Los títulos de clase del plan son genéricos; aquí se aplican así.
OA 03: 1 tiempos verbales según el propósito, 2 referencias, formación de palabras y falsos amigos, 3 modales y condicionales, 4 postura, registro y colocaciones.
OA 04: 1 presentarse e interactuar, 2 significado implícito y cortesía, 3 estrategias de fluidez, 4 intercambiar visiones de mundo, 5 reparar y reflexionar sobre la identidad.
Textos originales, glosados, en inglés americano.
"""
from __future__ import annotations

from fg_ingl_common import ADULT, MAT_L, MAT_R, arith, ex, lesson, mc, ml, mr, task

OA3 = "FG-INGL-3M-OAC-03"
OA4 = "FG-INGL-3M-OAC-04"


def sc(oa, n, rows):
    return [(f"En Inglés de 3.º medio (OA {oa}, clase {n}): {q}", a, w) for q, a, w in rows]


# ------------------------------------------------------------------ OA 03 clase 1: tiempos verbales según el propósito
GUIT = "«My brother plays the guitar every evening. Right now he is learning a new song. Last year he lost his first guitar, so he has saved money for a new one since March. Next month he will buy it.» (plays = toca, learning = aprendiendo, lost = perdió, saved = ahorrado, since = desde, will buy = comprará)"

lesson(
    OA3, 1, MAT_R,
    "Aprenderé a elegir el tiempo verbal según lo que quiero comunicar: hábitos, acciones en curso, hechos terminados, resultados actuales y planes. Sirve para entender y producir textos claros en los que el momento de cada acción importa.",
    ["Sé usar el presente simple y el pasado simple.", "Conozco las palabras every day, yesterday y tomorrow."],
    [
        "El presente simple (plays, boils) expresa hábitos y verdades generales: My brother plays the guitar every evening; water boils at 100 degrees Celsius at sea level. El presente continuo (is learning) expresa una acción que ocurre ahora o de manera temporal: Right now he is learning a new song. El pasado simple (lost, watched) cuenta un hecho terminado en un momento pasado: Last year he lost his guitar.",
        "El presente perfecto (has saved, have lived) se forma con have o has más participio. Une el pasado con el presente: la acción empezó antes y sigue hasta ahora (for, since), o tiene un resultado que importa hoy (The council has approved a new bike path). Se usa con for + duración, since + punto de inicio, already, yet, ever y never. No se usa con una fecha terminada: se dice Yesterday we visited, no Yesterday we have visited.",
        "El futuro con will expresa decisiones o predicciones: Next month he will buy it. Para elegir el tiempo, pregúntate qué quiero mostrar: ¿un hábito?, ¿algo en este momento?, ¿un hecho terminado?, ¿un resultado actual?, ¿un plan? Las marcas de tiempo (every, right now, last year, since, next month) son las pistas más fiables. Adaptar el tiempo al propósito vale más que memorizar la forma.",
    ],
    [("present simple", "hábitos y verdades generales"), ("present continuous", "acción en curso o temporal"), ("past simple", "hecho terminado en el pasado"), ("present perfect", "pasado con relación al presente"), ("for / since", "durante / desde"), ("will", "futuro: decisión o predicción")],
    [
        ("Elegir según la pista", GUIT + " ¿Qué tiempo expresa que el hermano toca cada noche?", ["Busco la marca every evening.", "Marca un hábito.", "El verbo plays está en presente simple."], "Presente simple (plays)"),
        ("Presente perfecto con since", GUIT + " ¿Por qué se usa has saved y no saved?", ["Since March indica el inicio de la acción.", "La acción continúa hasta ahora.", "Eso exige presente perfecto."], "Porque ahorra desde marzo hasta ahora"),
    ],
    [
        ("Decir Yesterday we have visited.", "Con una fecha terminada se usa pasado simple.", "Si dices yesterday o last year, usa visited."),
        ("Usar presente simple para algo que ocurre ahora, como He learns a song right now.", "Right now pide presente continuo.", "Usa is learning."),
    ],
    [
        mr(GUIT, "¿Qué forma muestra un hábito?", "plays", ["is learning", "will buy"], "Every evening marca una acción repetida."),
        mr(GUIT, "¿Qué forma muestra una acción en curso?", "is learning", ["plays", "lost"], "Right now indica que ocurre en este momento."),
        mr(GUIT, "¿Qué forma indica un hecho terminado en el pasado?", "lost", ["has saved", "will buy"], "Last year ubica el hecho en el pasado."),
    ],
    [
        mr(GUIT, "¿Qué tiempo se usa en Next month he will buy it?", "futuro con will", ["presente perfecto", "pasado simple"], "Next month apunta al futuro y will lo marca."),
        mc("Completa con la forma correcta: 'I ___ in this city since I was ten.'", "have lived", ["live", "am living"], "Since + punto de inicio exige presente perfecto."),
        mc("¿Qué oración usa el presente perfecto para un resultado importante hoy?", "The council has approved a new bike path", ["The council approved a new bike path last year", "The council approves a new bike path every year"], "Has approved presenta el resultado actual."),
    ],
    [
        mc("Completa: 'Water ___ at 100 degrees Celsius at sea level.'", "boils", ["is boiling", "boiled"], "Es una verdad general, así que va en presente simple."),
        mc("Completa: 'Look! It ___ outside.'", "is raining", ["rains", "rained"], "Look! indica que ocurre ahora."),
        mc("Completa: 'Yesterday we ___ a documentary.'", "watched", ["have watched", "watch"], "Yesterday es una marca de pasado terminado."),
    ],
    [
        mc("Sofía escribe dos oraciones. 1) I live with my aunt. 2) I am living with my aunt this month. ¿Cuál sugiere algo temporal?", "la segunda, por el presente continuo", ["la primera, por el presente simple", "ninguna, las dos significan lo mismo"], "El presente continuo suele marcar situaciones temporales."),
        mc("Un compañero dice que se puede escribir 'I have seen that film yesterday'. ¿Qué le respondes?", "no: con yesterday se usa el pasado simple, I saw that film yesterday", ["no: se debe usar will, I will see that film yesterday", "sí, el presente perfecto sirve para todo tipo de fechas"], "Yesterday es una fecha terminada."),
    ],
    [
        mc("Elige la pareja correcta: 'I ___ English for six years, and I ___ a test last week.'", "have studied / took", ["studied / have taken", "study / take"], "For + duración usa presente perfecto y last week usa pasado."),
        mc("Escribes una entrada de diario sobre algo terminado. ¿Qué oración sirve?", "Yesterday we visited a museum", ["Yesterday we have visited a museum", "Yesterday we visit a museum"], "Un hecho terminado con yesterday va en pasado simple."),
    ],
    [mc("Lees: «Our school has opened a new gym. Classes start next week.» (gym = gimnasio). ¿Qué verbo señala un resultado vigente hoy?", "has opened", ["start", "next"], "El gimnasio ya está abierto: resultado actual.")],
    sc(3, 1, [
        ("¿Para qué se usa el presente perfecto?", "Para unir un hecho pasado con el presente", "Se usa con for, since, already y resultados actuales."),
        ("¿Qué pista de tiempo acompaña al presente simple de hábito?", "Every day o every evening", "Marca una acción repetida."),
        ("¿Qué tiempo se usa con yesterday?", "El pasado simple", "Yesterday es una fecha terminada."),
    ]),
    task("Lee este mensaje de ejemplo: «Hi Carla, I am writing from the library. I have studied here since two o'clock. Yesterday I finished my project, but today I am revising it. Tomorrow I will present it.» (revising = revisando, present = presentar). Anota en español la acción que muestra un hábito o un resultado, una acción en curso y un plan, y escribe el tiempo de cada una.", "Resultado desde un punto: I have studied here since two o'clock (presente perfecto). En curso: I am revising it (presente continuo). Plan: I will present it (futuro con will). Terminado: I finished my project (pasado simple).", ["identifica al menos tres tiempos", "cita la pista de cada uno", "explica qué comunica cada tiempo"], ["hoja con tres líneas"], ["decir que todos los verbos son pasado", "no citar la pista"], "Subraya la pista (since, today, tomorrow) y vuelve a asociar cada tiempo con ella."),
    "Escribe una oración sobre ti en cada tiempo: presente simple, presente continuo, pasado simple, presente perfecto y futuro con will.",
    "Escribe en español qué comunica cada tiempo verbal.",
)

# ------------------------------------------------------------------ OA 03 clase 2: referencias, formación de palabras y falsos amigos
APPS = "«Many students use apps to study. They are free and easy to download. This helps students who have little money. However, some apps are unreliable, which means that students cannot trust them completely.» (apps = aplicaciones, download = descargar, little money = poco dinero, trust = confiar)"

lesson(
    OA3, 2, MAT_R,
    "Aprenderé a seguir las palabras que remiten a otras (they, this, which), a deducir significados con prefijos y sufijos (un-, dis-, -able, -less) y a evitar falsos amigos. Sirve para comprender textos sin traducir cada palabra y para escribir con vocabulario preciso.",
    ["Sé reconocer una idea central.", "Conozco pronombres como it, they y this."],
    [
        "Las palabras de referencia (reference words) evitan repetir ideas: they y them remiten a personas o cosas en plural, it a algo singular, this y these a una idea ya dicha, y which a toda la idea anterior. En 'Many students use apps. They are free', they se refiere a apps. En 'They are free and easy to download. This helps students', this se refiere a la idea de que las apps son gratis. Para encontrar el referente, vuelve atrás y busca qué encaja en número y sentido.",
        "Muchas palabras se forman con prefijos (al inicio) y sufijos (al final). Prefijos: un-, dis-, im-, in- (no, lo contrario: unreliable, disagree, impossible), re- (de nuevo: rebuild), mis- (mal: misunderstand). Sufijos: -able (que puede: reliable), -ful (lleno de: helpful), -less (sin: careless), -ness (cualidad: kindness), -ment (resultado: improvement). Así, unreliable es no fiable, careless es sin cuidado y kindness es amabilidad.",
        "Los falsos amigos (false friends) se parecen al español pero significan otra cosa: actually es en realidad (no actualmente, que se dice currently), sensible es sensato (no sensible), embarrassed es avergonzado (no embarazada), carpet es alfombra (no carpeta), exit es salida (no éxito, que se dice success), realize es darse cuenta, assist es ayudar (asistir a una clase se dice attend) y parents son los padres (parientes se dice relatives).",
    ],
    [("reference word", "palabra de referencia: they, this, which"), ("prefix", "prefijo: al inicio de la palabra"), ("suffix", "sufijo: al final de la palabra"), ("false friend", "falso amigo"), ("unreliable", "no confiable"), ("currently", "actualmente")],
    [
        ("Buscar el referente", APPS + " ¿A qué se refiere They en la segunda oración?", ["Busco un plural anterior.", "Students y apps son plurales, pero lo que es free and easy to download es apps.", "They se refiere a apps."], "A las apps (aplicaciones)"),
        ("Deducir con un prefijo", APPS + " ¿Qué significa unreliable?", ["Reliable viene de rely, que es confiar.", "El sufijo -able indica que se puede y el prefijo un- niega.", "Unreliable es que no se puede confiar, lo confirma cannot trust."], "No confiable"),
    ],
    [
        ("Leer actually como actualmente.", "Es un falso amigo: actually es en realidad.", "Usa currently para actualmente."),
        ("Pensar que this se refiere a la última palabra.", "This resume la idea completa anterior.", "Pregunta qué idea completa se acaba de decir."),
    ],
    [
        mr(APPS, "¿A qué se refiere This en 'This helps students who have little money'?", "a que las apps son gratis y fáciles de descargar", ["a que algunas apps no son confiables", "a que los estudiantes estudian"], "This remite a la idea anterior sobre apps gratis."),
        mr(APPS, "¿A qué se refiere which en 'which means that students cannot trust them completely'?", "a que algunas apps no son confiables", ["a que las apps son gratis", "a que los estudiantes tienen poco dinero"], "Which retoma la idea inmediata: some apps are unreliable."),
        mc("¿Qué significa careless?", "sin cuidado", ["lleno de cuidado", "cuidado de nuevo"], "El sufijo -less significa sin."),
    ],
    [
        mc("¿Qué significa rebuild?", "construir de nuevo", ["construir mal", "no construir"], "El prefijo re- significa de nuevo."),
        mc("¿Qué significa helpful?", "que ayuda", ["que no ayuda", "ayuda de nuevo"], "El sufijo -ful significa lleno de, es decir, útil."),
        mc("¿Cuál palabra significa lo contrario de agree?", "disagree", ["reagree", "agreeful"], "El prefijo dis- indica lo contrario."),
    ],
    [
        mc("Completa: 'It is ___ to finish this project in one hour.' (imposible)", "impossible", ["unpossible", "dispossible"], "Con possible se usa el prefijo im-."),
        mc("Completa: 'Her ___ to us was great.' (cualidad de ser amable)", "kindness", ["kindful", "kindless"], "El sufijo -ness forma sustantivos de cualidad."),
        mc("Completa: 'I misunderstood the question' significa que:", "entendí mal la pregunta", ["entendí bien la pregunta", "no hice la pregunta"], "El prefijo mis- indica error."),
    ],
    [
        mc("Un alumno lee 'I actually live in Chile' y traduce 'actualmente vivo en Chile'. ¿Cuál es el error y la corrección?", "actually es en realidad; para actualmente se usa currently", ["actually es siempre; no hay ninguna corrección que hacer", "live es un falso amigo y se traduce como vivo"], "Es un falso amigo."),
        mc("Un compañero escribe 'I put the papers in the carpet'. ¿Qué quiso decir?", "carpeta, pero carpet significa alfombra: debía decir folder", ["alfombra, y la oración está correcta tal como está", "mochila, pero debía decir bag en lugar de carpet"], "Carpet es falso amigo de carpeta."),
    ],
    [
        mc("Traduce bien: 'My parents are coming to the show.'", "Mis padres vienen al espectáculo", ["Mis parientes vienen al espectáculo", "Mis amigos vienen al espectáculo"], "Parents son los padres; relatives son parientes."),
        mc("Un compañero dice 'I was very embarrassed' y su amigo entiende 'estaba embarazada'. ¿Qué significa la palabra?", "avergonzado", ["embarazada", "emocionado"], "Embarrassed es un falso amigo de embarazada."),
    ],
    [mc("En un letrero ves 'Exit'. ¿Qué indica?", "la salida", ["el éxito", "la entrada"], "Exit es salida; éxito es success.")],
    sc(3, 2, [
        ("¿Qué indica el prefijo un-?", "Negación o lo contrario", "Unreliable es lo contrario de reliable."),
        ("¿Cómo se dice actualmente en inglés?", "Currently", "Actually es otro significado."),
        ("¿Cómo se dice parientes en inglés?", "Relatives", "Parents son los padres."),
    ]),
    task("Lee: «The new bus line is unreliable. It sometimes arrives late, which is a problem for workers. They have asked the city for improvement.» (bus line = recorrido de bus, arrives = llega, workers = trabajadores, city = municipalidad). Escribe en español a qué se refieren They y which, qué significa unreliable y qué sufijo tiene improvement.", "They se refiere a los trabajadores. Which se refiere a que el bus llega tarde. Unreliable es no confiable. Improvement lleva el sufijo -ment (resultado de mejorar).", ["identifica los dos referentes", "deduce el significado con el prefijo", "reconoce el sufijo"], ["cuatro respuestas en español"], ["decir que They se refiere al bus", "no mencionar el prefijo"], "Vuelve atrás a la oración anterior y busca qué encaja en número y sentido."),
    "Escribe tres palabras con prefijo y tres con sufijo de la clase y su significado.",
    "Busca en tu casa un envase con un texto en inglés y subraya una palabra de referencia y una con prefijo.",
)

# ------------------------------------------------------------------ OA 03 clase 3: modales y condicionales
RULES = "«Library rules: You must be quiet. You don't have to buy a membership, because it is free. You mustn't eat or drink at the computers. You can borrow up to five books. If you return a book late, you will pay a small fine.» (rules = reglas, membership = socio, borrow = pedir prestado, late = atrasado, fine = multa)"

lesson(
    OA3, 3, MAT_R,
    "Aprenderé a usar y entender los modales (should, must, mustn't, don't have to, might) y los condicionales de primer y segundo tipo (if + presente, will; if + pasado, would). Sirve para dar consejos, expresar reglas y posibilidades, y presentar una postura con condiciones.",
    ["Sé usar el presente simple y el pasado simple.", "Conozco can y will."],
    [
        "Los modales no cambian con el sujeto y van con el verbo base. Should expresa consejo: You should sleep more. Must y have to expresan obligación: You must be quiet. Mustn't expresa prohibición: You mustn't eat here. Don't have to expresa que no es necesario: You don't have to buy a membership. Might y could expresan posibilidad: It might rain. Can expresa capacidad o permiso. La diferencia entre mustn't (prohibido) y don't have to (no hace falta) es muy importante.",
        "El primer condicional (first conditional) habla de situaciones reales y posibles: If + presente simple, will + verbo. If you return a book late, you will pay a fine. El segundo condicional (second conditional) habla de situaciones imaginarias o poco probables: If + pasado simple, would + verbo. If I had more time, I would learn Italian. Para consejos se usa If I were you, I would... (con were para todas las personas).",
        "Los condicionales sirven para argumentar con condiciones y consecuencias: If schools offered cooking classes, students would learn healthy habits. Esa frase presenta una postura con una razón y la imagina como posible. En un argumento, el primer condicional suena más seguro y el segundo más hipotético y respetuoso: invita a pensar sin imponer.",
    ],
    [("should", "debería: consejo"), ("must / have to", "debe: obligación"), ("mustn't", "no debe: prohibición"), ("don't have to", "no hace falta"), ("first conditional", "if + presente, will: situación real"), ("second conditional", "if + pasado, would: situación imaginaria")],
    [
        ("Prohibición y falta de necesidad", RULES + " ¿Qué diferencia hay entre You mustn't eat y You don't have to buy a membership?", ["Mustn't expresa prohibición.", "Don't have to expresa que no es necesario.", "Una prohíbe y la otra no exige."], "Mustn't prohíbe; don't have to dice que no hace falta"),
        ("Primer condicional", RULES + " ¿Qué tipo de condicional es 'If you return a book late, you will pay a small fine'?", ["Tiene if + presente simple.", "Después va will + verbo.", "Expresa una situación real y posible: primer condicional."], "Primer condicional"),
    ],
    [
        ("Decir You mustn't buy a membership para decir que no es necesario.", "Mustn't prohíbe; no es lo mismo que no hace falta.", "Usa don't have to."),
        ("Escribir If I will have time, I will go.", "Después de if no se usa will en el condicional de situación real.", "Escribe If I have time, I will go."),
    ],
    [
        mr(RULES, "¿Qué norma se debe cumplir siempre?", "estar en silencio", ["comprar una membresía", "comer en los computadores"], "You must be quiet es una obligación."),
        mr(RULES, "¿Qué está prohibido?", "comer o beber en los computadores", ["pedir libros prestados", "devolver un libro"], "You mustn't eat or drink prohíbe comer."),
        mr(RULES, "¿Qué no es necesario hacer?", "comprar una membresía", ["estar en silencio", "no comer ni beber en los computadores"], "You don't have to buy a membership: es gratis."),
    ],
    [
        mc("¿Cuál oración da un consejo?", "You should drink more water", ["You must drink water at 3 p.m.", "You mustn't drink water"], "Should expresa consejo."),
        mc("¿Cuál es la forma correcta del primer condicional?", "If it rains, we will stay home", ["If it will rain, we stay home", "If it rained, we will stay home"], "If + presente simple, will + verbo."),
        mc("¿Cuál es la forma correcta del segundo condicional?", "If I had more time, I would learn Italian", ["If I have more time, I would learn Italian", "If I had more time, I will learn Italian"], "If + pasado, would + verbo."),
    ],
    [
        mc("Completa: 'You ___ wear a uniform in this school.' (es una obligación)", "must", ["mustn't", "might"], "Must expresa obligación."),
        mc("Completa: 'You ___ park here.' (está prohibido)", "mustn't", ["don't have to", "should"], "Mustn't expresa prohibición."),
        mc("Completa: 'On Sunday you ___ get up early.' (no es necesario)", "don't have to", ["mustn't", "must"], "Don't have to indica que no hace falta."),
    ],
    [
        mc("Un amigo duda entre dos carreras. Quieres aconsejarlo: ¿qué frase usas?", "If I were you, I would visit both campuses first", ["If I was you, I will visit both campuses first", "If I am you, I will go to both campuses first"], "If I were you, I would... es la forma del consejo."),
        mc("¿Qué oración presenta una postura con una condición imaginaria?", "If schools offered cooking classes, students would learn healthy habits", ["Schools offer cooking classes and students learn healthy habits", "Schools offered cooking classes, so students learned healthy habits"], "Es segundo condicional con postura implícita."),
    ],
    [
        mc("Estás argumentando por buses gratis para estudiantes y quieres sonar hipotético y respetuoso. ¿Qué frase elegirías?", "If buses were free, more students would arrive on time", ["Buses must be free so that students arrive on time", "Buses are free and more students arrive on time"], "El segundo condicional invita a pensar sin imponer."),
        mc("Un alumno dice 'I must to study'. ¿Cuál es el error?", "después de must va el verbo base sin to", ["debe ser mustn't porque la frase es negativa", "falta un if para que la frase tenga sentido"], "Los modales van con verbo base: I must study."),
    ],
    [mc("Lees: 'You might need an umbrella.' ¿Qué comunica might?", "posibilidad: tal vez necesites uno", ["obligación: debes llevar uno", "prohibición: no lo uses"], "Might expresa posibilidad.")],
    sc(3, 3, [
        ("¿Cuál es la fórmula del primer condicional?", "If + presente simple, will + verbo", "Expresa situaciones reales."),
        ("¿Qué significa don't have to?", "No hace falta", "No es obligatorio."),
        ("¿Para qué sirve If I were you, I would...?", "Para dar un consejo", "Se usa para aconsejar."),
    ]),
    task("Escribe en inglés cuatro oraciones sobre tu colegio, de ejemplo: una con must, una con mustn't, una con don't have to y un condicional con if (de primer o segundo tipo).", "Students must wear a uniform. Students mustn't use phones in tests. Students don't have to bring lunch. If the cafeteria were cheaper, more students would buy lunch.", ["usa los cuatro elementos", "cada modal expresa su sentido correcto", "usa la estructura del condicional"], ["cuatro oraciones"], ["confundir mustn't y don't have to", "usar will después de if"], "Marca cada modal y revisa su sentido; corrige las confusiones con la explicación."),
    "Escribe un consejo con should y otro con If I were you.",
    "Escribe una predicción con might y una decisión con will.",
)

# ------------------------------------------------------------------ OA 03 clase 4: postura, registro y colocaciones
OPIN = "«Unfortunately, many young people do not read the news. Clearly, this is a problem for democracy. Surprisingly, a short daily habit can change that. It seems that ten minutes a day is enough to stay informed.» (unfortunately = lamentablemente, clearly = claramente, surprisingly = sorprendentemente, democracy = democracia, enough = suficiente, informed = informado)"

lesson(
    OA3, 4, MAT_R,
    "Aprenderé a usar adverbios de postura (unfortunately, clearly), expresiones que suavizan (it seems that, probably), el registro formal e informal y colocaciones comunes (make a decision, take a break). Sirve para construir y expresar una postura crítica con el inglés adecuado a cada texto.",
    ["Sé usar tiempos verbales y modales.", "Sé expresar una postura con una razón."],
    [
        "Los adverbios de postura muestran lo que el autor piensa sobre lo que dice: unfortunately (lamentablemente), fortunately, clearly, surprisingly, honestly, obviously. Aparecen al inicio de la oración, con coma: Unfortunately, many young people do not read the news. Muestran evaluación, así que reconócelos como opinión del autor, no como un hecho. Las expresiones it seems that, it appears that, probably y perhaps suavizan una afirmación porque marcan que no es completamente segura.",
        "El registro (register) es el grado de formalidad. En un texto formal se usan palabras como children, obtain, I would like to ask y se evitan contracciones. En uno informal aparecen kids, get, can I..., wanna y contracciones como don't. La misma idea cambia según la audiencia: Dear Ms. Rojas, I would like to ask for permission (formal) frente a Hi, can I leave early? (informal). Elegir bien el registro es parte de ser claro y respetuoso.",
        "Las colocaciones (collocations) son combinaciones de palabras que suenan naturales: make a decision, make a mistake, do homework, do research, take a break, take part in, pay attention, give an opinion, have a look. No se traducen palabra por palabra: en español se dice hacer una pausa, pero en inglés se dice take a break. Aprenderlas permite escribir como una persona que domina el inglés.",
    ],
    [("unfortunately / clearly", "lamentablemente / claramente"), ("it seems that", "parece que"), ("register", "registro: grado de formalidad"), ("formal / informal", "formal / informal"), ("collocation", "colocación: palabras que van juntas"), ("take a break", "tomar un descanso")],
    [
        ("Detectar la postura del autor", OPIN + " ¿Qué muestra la palabra unfortunately?", ["Es un adverbio de postura.", "Expresa que el autor lamenta lo que dice.", "Es una evaluación, no un dato."], "Que el autor lamenta el hecho: es una evaluación"),
        ("Elegir una colocación", "Completa: 'I have to ___ a decision about my studies.' A) make B) do", ["Con decision se usa make.", "Se dice make a decision.", "Do a decision no es la combinación que se usa en inglés."], "A) make"),
    ],
    [
        ("Decir do a break por hacer un descanso.", "La colocación en inglés es take a break.", "Aprende cada colocación como un bloque."),
        ("Usar kids y wanna en una carta a una autoridad.", "Son informales y no corresponden al registro formal.", "Usa children y want to."),
    ],
    [
        mr(OPIN, "¿Qué palabra muestra una sorpresa del autor?", "Surprisingly", ["Clearly", "Unfortunately"], "Surprisingly significa sorprendentemente."),
        mc("¿Cuál de estas es una colocación correcta?", "take a break", ["do a break", "make a break"], "En inglés se dice take a break."),
        mc("¿Cuál es el registro formal de 'Hey, send me the report'?", "Could you please send me the report?", ["Gimme the report as soon as you can", "Send it to me, kid, and be quick"], "Could you please es cortés y formal."),
    ],
    [
        mr(OPIN, "¿Cuál es una expresión que suaviza una afirmación?", "It seems that", ["Clearly", "Unfortunately"], "It seems that marca que no es completamente seguro."),
        mc("¿Qué par es una colocación correcta?", "pay attention", ["give attention", "make attention"], "Se dice pay attention."),
        mc("¿Qué palabra es formal?", "children", ["kids", "guys"], "Children es formal; kids es informal."),
    ],
    [
        mc("Completa: 'Please ___ part in the survey.'", "take", ["make", "do"], "Take part in significa participar."),
        mc("Completa: 'I have to ___ research for my project.'", "do", ["make", "take"], "Do research es la colocación."),
        mc("En un correo formal, ¿cuál oración es mejor?", "I would like to obtain more information", ["I wanna get more info about the course", "Gimme more info about the course please"], "Es formal y completa."),
    ],
    [
        mc("Una alumna dice que 'Clearly, this is a problem' es un hecho. ¿Cuál es la mejor respuesta?", "Clearly es una opinión del autor; no necesariamente un hecho", ["tiene razón, clearly prueba que se trata de un hecho", "Clearly es una pregunta que el autor hace al lector"], "Los adverbios de postura expresan evaluación."),
        mc("Un compañero escribe 'It seems that ten minutes a day is enough'. ¿Qué actitud muestra?", "cautela: no lo afirma con total seguridad", ["certeza absoluta: lo afirma con total seguridad", "rechazo: está en contra de lo que se dice"], "It seems que suaviza."),
    ],
    [
        mc("Para opinar sobre las noticias en un blog juvenil, ¿qué registro y adverbio conviene?", "informal, con un adverbio como honestly", ["muy formal, con palabras jurídicas", "ninguno"], "Un blog juvenil admite un tono cercano."),
        mc("Corrige: 'I did a mistake in the test.'", "I made a mistake in the test", ["I took a mistake in the test", "I gave a mistake in the test"], "La colocación es make a mistake."),
    ],
    [mc("Quieres escribir un texto que tu profesora lea. ¿Qué elección de registro es mejor?", "formal, sin contracciones", ["muy informal, con wanna", "solo emojis"], "La audiencia es una autoridad.")],
    sc(3, 4, [
        ("¿Qué indica unfortunately?", "Una evaluación negativa del autor", "No es un dato, es una opinión."),
        ("¿Cómo se dice tomar un descanso en inglés?", "Take a break", "Es una colocación."),
        ("¿Qué es el registro de un texto?", "Su grado de formalidad", "Depende de la audiencia."),
    ]),
    task("Escribe dos versiones de una misma petición, una formal y una informal: quieres pedir un día más para entregar un trabajo. Usa un adverbio de postura o it seems that en una de las versiones y la colocación make a request o take a break.", "Formal: Dear Mr. Vera, I would like to make a request. Unfortunately, I have not finished my project; could I have one more day? Informal: Hi, can I have one more day? I need it.", ["dos versiones", "el registro es coherente", "incluye un adverbio de postura"], ["dos mensajes"], ["mezclar registros", "traducir palabra por palabra"], "Subraya las palabras de registro y reemplaza las que no corresponden."),
    "Escribe cinco colocaciones con make, do o take y una oración con cada una.",
    "Cambia un mensaje informal tuyo a registro formal.",
)

# ================================================================= OA 04: interacción, visiones de mundo e identidad
# ------------------------------------------------------------------ clase 1: presentarse e interactuar
EXCH1 = "«Ana: Hi, I'm Ana. I'm from Chile. I'm seventeen. Jo: Nice to meet you, Ana. I'm Jo. I grew up in a small town near the sea. What about you? Ana: I grew up in the city, but my grandparents live in the countryside. Jo: Cool! Do you speak any other languages? Ana: I speak Spanish and English, and I'm learning a little French.» (grew up = crecí, grandparents = abuelos, countryside = campo, any other = otros)"

lesson(
    OA4, 1, MAT_L,
    "Aprenderé a presentarme, preguntar y mantener una conversación en inglés con alguien de otra cultura: saludos, preguntas abiertas, turnos de habla y frases para hablar de mi origen e identidad. Sirve para interactuar con fluidez y empezar a reconocer mi propia identidad.",
    ["Sé saludar y decir de dónde soy.", "Conozco do/does y las preguntas con who, where y what."],
    [
        "Al conocer a alguien se usan saludos y frases de presentación: Hi, I'm Ana; Nice to meet you; I'm from Chile; I grew up in...; My family comes from...; I speak Spanish and some English; I'm learning French. Para hablar de identidad (identity) se pueden mencionar origen, familia, lengua, intereses y valores, sin obligación de contar todo. Basta lo que quieras compartir.",
        "Una conversación funciona por turnos (turns): hablas, preguntas y escuchas. Las preguntas cerradas (Do you speak French?) se responden con yes o no. Las preguntas abiertas (What do you like about your town? How do you celebrate...?) invitan a explicar más. Para devolver el turno usa What about you? y How about you? Para mostrar interés, reacciona: Cool!, Really?, That sounds interesting.",
        "Escucha con atención y responde a lo que dijo la otra persona antes de cambiar de tema. No necesitas un acento perfecto: lo importante es que el mensaje sea claro y que la otra persona se sienta escuchada. Evita preguntas que sean invasivas y los estereotipos. Con la fluidez no se mide la velocidad, sino que la conversación avance con claridad.",
    ],
    [("I grew up in", "crecí en"), ("What about you?", "¿y tú?"), ("open question", "pregunta abierta"), ("turn", "turno de habla"), ("identity", "identidad"), ("That sounds interesting", "suena interesante")],
    [
        ("Reconocer información de identidad", ADULT + EXCH1 + " ¿Dónde creció Jo?", ["Busco I grew up in en las palabras de Jo.", "Dice a small town near the sea.", "Ese es el lugar donde creció."], "En un pueblo pequeño cerca del mar"),
        ("Preguntas abiertas y cerradas", "«Do you speak French?» es una pregunta A) cerrada o B) abierta.", ["Se responde con yes o no.", "No pide explicación.", "Es cerrada."], "A) cerrada"),
    ],
    [
        ("Responder solo con yes o no y quedarse en silencio.", "La conversación no avanza.", "Agrega una frase y devuelve el turno con What about you?"),
        ("Cambiar de tema sin responder a lo que se dijo.", "La otra persona no se siente escuchada.", "Reacciona con Really? o That sounds interesting."),
    ],
    [
        ml(EXCH1, "¿De dónde es Ana?", "de Chile", ["de Francia", "de un pueblo cerca del mar"], "Dice I'm from Chile."),
        ml(EXCH1, "¿Cuántos años tiene Ana?", "diecisiete", ["quince", "veintisiete"], "Dice I'm seventeen."),
        ml(EXCH1, "¿Qué idioma está aprendiendo Ana?", "un poco de francés", ["alemán", "portugués"], "Dice I'm learning a little French."),
    ],
    [
        ml(EXCH1, "¿Dónde viven los abuelos de Ana?", "en el campo", ["en la ciudad", "cerca del mar"], "Dice my grandparents live in the countryside."),
        mc("¿Qué frase devuelve el turno a la otra persona?", "What about you?", ["I don't know", "Goodbye"], "What about you? invita a responder."),
        mc("¿Cuál de estas es una pregunta abierta?", "How do you celebrate your birthday?", ["Do you like birthdays in your family", "Is it your birthday this month"], "How do you... pide una explicación."),
    ],
    [
        mc("Completa para presentarte: 'Hi, I'm Ben. I ___ in a small city.'", "grew up", ["grow up", "have grew up"], "Grew up es el pasado de grow up."),
        mc("Te cuentan algo interesante. ¿Qué reacción es adecuada?", "Really? That sounds interesting", ["Mm. And what is the next topic", "OK. I prefer to talk about me"], "Muestra interés genuino por lo que dijo la otra persona."),
        mc("¿Qué pregunta invita a explicar más?", "What do you like about your town?", ["Do you live in a town?", "Is your town big?"], "What do you like... es abierta."),
    ],
    [
        mc("Jo dice 'I grew up in a small town' y Ana pasa a hablar de su deporte favorito sin comentar. ¿Qué problema hay?", "no responde a lo que Jo dijo y no mantiene el turno", ["usa mal el pasado del verbo grow up", "habla demasiado lento para la conversación"], "Interactuar es responder a la otra persona."),
        mc("Un alumno dice que para hablar bien inglés hay que imitar el acento de otra cultura. Según lo estudiado, ¿qué es correcto?", "lo importante es ser claro y que la conversación avance", ["el acento perfecto es obligatorio para hablar bien", "hablar rápido es lo único que importa en inglés"], "La fluidez es claridad y avance de la conversación."),
    ],
    [
        mc("Quieres saber más sobre las tradiciones de una amiga extranjera sin invadir su privacidad. ¿Qué pregunta es mejor?", "Are there any traditions you enjoy in your family?", ["How much money does your family have?", "Why is your family so strange?"], "Es abierta, respetuosa y no invasiva."),
        mc("¿Cuál respuesta aporta más información y devuelve el turno?", "I like music. What about you?", ["I like music, and that is all", "Yes, I like music a lot"], "Agrega una frase y pregunta."),
    ],
    [mc("Alguien te dice 'Nice to meet you'. ¿Qué respondes?", "Nice to meet you too", ["Goodbye", "I don't know"], "Es la respuesta habitual.")],
    sc(4, 1, [
        ("¿Para qué sirve What about you?", "Para devolver el turno a la otra persona", "Mantiene la conversación."),
        ("¿Qué es una pregunta abierta?", "Una pregunta que se responde con explicación", "No se contesta con yes o no."),
        ("¿Qué mide la fluidez en una conversación?", "Que se entienda y avance, no la velocidad ni el acento", "La claridad importa más."),
    ]),
    task("Escribe en inglés un diálogo de seis líneas entre tú y una persona de otro país. Debe incluir saludo, I'm from..., una pregunta abierta, What about you? y una reacción como Really? Usa solo datos que quieras compartir.", "A: Hi, I'm Luis. I'm from Chile. B: Nice to meet you. I'm Sam. A: What do you like to do after school? B: I play music. What about you? A: I read and play soccer. B: Really? That sounds fun.", ["usa el saludo y la presentación", "incluye una pregunta abierta", "devuelve el turno y reacciona"], ["diálogo de seis líneas"], ["preguntas solo cerradas", "no reaccionar"], "Marca la pregunta abierta y la reacción; agrega las que falten."),
    "Practica el diálogo en voz alta con una persona de tu casa o con un espejo.",
    "Escribe tres preguntas abiertas para conocer a alguien.",
)

# ------------------------------------------------------------------ clase 2: significado implícito y cortesía
POL1 = "«Host: Would you like some more soup? Guest: It was delicious, thank you, but I'm full. Host: Are you sure? Guest: Yes, I couldn't eat another bite.» (host = anfitrión, guest = invitado, delicious = delicioso, full = lleno, couldn't eat another bite = no podría comer más)"
POL2 = "«Student: Could I ask a question? Teacher: Of course. Student: I'm not sure I understood the instructions. Would you mind explaining them again? Teacher: Certainly. Let's go step by step.» (instructions = instrucciones, would you mind = ¿te importaría, explaining = explicar, step by step = paso a paso)"

lesson(
    OA4, 2, MAT_L,
    "Aprenderé a escuchar lo que se dice y lo que se da a entender, a reconocer la cortesía (Could I..., Would you mind...) y a notar cómo el énfasis en una palabra cambia el sentido. Sirve para entender a personas de otras culturas sin malentendidos.",
    ["Sé presentarme e interactuar con preguntas abiertas.", "Sé usar can y could."],
    [
        "No todo lo que se quiere decir está en las palabras. A veces se dice de manera indirecta (indirectness): That might be difficult puede significar No, no puedo; I'm full, thank you es una forma cortés de rechazar más comida; Maybe we can see about it later puede ser una forma suave de decir que no. El significado implícito (implied meaning) depende de la situación, de la relación y de la cultura.",
        "La cortesía (politeness) se marca con expresiones como Could I..., Would you mind + verbo con -ing, Would it be possible to..., Thank you, but... y Sorry to bother you. Para pedir algo: Could you help me? es más amable que Help me. Para rechazar con cortesía: Thank you, but I can't. Para pedir repetir: Sorry, could you say that again?",
        "El énfasis (stress) también cambia el significado. En el texto escrito se marca con mayúsculas: I didn't say HE took the pen (dije que lo tomó otra persona), I didn't say he TOOK the pen (dije que hizo otra cosa con él), I didn't SAY he took the pen (lo insinué, pero no lo dije). Lee con calma, pregunta si dudas y no supongas que una respuesta indirecta es una mentira: en muchas culturas es una forma de cuidar al otro.",
    ],
    [("indirectness", "indirección: decir sin decir directamente"), ("implied meaning", "significado implícito"), ("politeness", "cortesía"), ("Would you mind...?", "¿te importaría...?"), ("stress", "énfasis en una palabra"), ("host / guest", "anfitrión / invitado")],
    [
        ("Rechazo cortés", ADULT + POL1 + " ¿Qué quiere decir realmente el invitado con I'm full?", ["El invitado agradece primero.", "Luego dice que está lleno.", "Quiere decir que no desea más comida."], "Que no quiere más sopa, de forma cortés"),
        ("Pedir una explicación con cortesía", ADULT + POL2 + " ¿Qué frase usa el estudiante para pedir repetir la explicación?", ["Busco una forma cortés de pedir un favor.", "Would you mind explaining them again? usa Would you mind + ing.", "Es una petición amable."], "Would you mind explaining them again?"),
    ],
    [
        ("Pensar que I'm full es una mentira.", "Es una forma cortés de rechazar, no un engaño.", "Interpreta la intención en su contexto."),
        ("Leer 'I didn't say HE took it' sin notar el énfasis.", "El énfasis cambia el sentido y se pierde.", "Fíjate en las mayúsculas."),
    ],
    [
        ml(POL1, "¿Qué ofrece el anfitrión?", "más sopa", ["más pan", "más jugo"], "Dice Would you like some more soup?"),
        ml(POL2, "¿Qué pide el estudiante?", "que le expliquen otra vez las instrucciones", ["otro trabajo para mejorar su nota", "más tiempo para el examen de la clase"], "Dice Would you mind explaining them again?"),
        mc("¿Cuál es la forma más cortés de pedir ayuda?", "Could you help me, please?", ["Help me now, I am in a hurry", "You help me with this"], "Could you es una petición amable."),
    ],
    [
        mc("¿Qué significa Would you mind opening the window?", "¿te importaría abrir la ventana?", ["¿te gustaría la ventana?", "abre la ventana"], "Would you mind es una petición cortés."),
        ml(POL1, "¿Cómo responde el invitado a la sopa?", "agradece y dice que está lleno", ["se queja de la sopa", "pide la receta"], "It was delicious, thank you, but I'm full."),
        mc("Un colega dice 'That might be difficult'. ¿Cómo puede entenderse?", "como un rechazo suave", ["como una aceptación inmediata", "como una pregunta"], "Es una forma indirecta de decir que no es fácil o probable."),
    ],
    [
        mc("Lee con énfasis: 'I didn't tell HER about the party.' ¿Qué da a entender?", "que se lo conté a otra persona", ["que no hubo fiesta", "que no me gusta la fiesta"], "El énfasis en HER contrasta con otra persona."),
        mc("¿Cuál frase rechaza una invitación con cortesía?", "Thank you, but I can't come on Saturday", ["No, I can't come, and that is all", "I don't like that plan on Saturday"], "Agradece y da el rechazo con suavidad."),
        mc("¿Qué frase pide repetir con cortesía?", "Sorry, could you say that again?", ["What? I did not hear you", "Say it again, I could not hear"], "Es una petición educada."),
    ],
    [
        mc("Tu anfitriona dice 'Maybe we can see about it later' cuando pides ir a una fiesta. ¿Qué conviene hacer?", "preguntar con cortesía si es posible o no, sin molestarte", ["asumir que es una promesa segura de ir a la fiesta con ellos", "enojarte de inmediato por una respuesta que no te gusta nada"], "Puede ser un rechazo suave; preguntar aclara."),
        mc("Un compañero dice 'I didn't SAY she was late'. ¿Qué parece decir?", "que lo insinuó, pero no lo dijo", ["que ella llegó temprano", "que no la vio"], "Se enfatiza SAY: la acción de decirlo."),
    ],
    [
        mc("Escuchas: 'It was delicious, but I couldn't eat another bite.' (couldn't eat another bite = no podría comer más). El anfitrión insiste otra vez. ¿Qué es lo más respetuoso?", "aceptar el rechazo y no insistir", ["servir más sin preguntar", "enojarse"], "Respetar la respuesta del invitado."),
        mc("Un amigo extranjero responde con una frase indirecta y tú no entiendes. ¿Qué haces?", "preguntar: Do you mean you prefer not to?", ["asumir que miente y dejar de hablarle", "ignorarlo y esperar que se explique solo"], "Aclarar con cortesía evita malentendidos."),
    ],
    [mc("Quieres pedir el lápiz a un compañero. ¿Qué opción es más cortés?", "Could I borrow your pencil, please?", ["Give me your pencil, I need it now", "Pencil now, please, I am in a hurry"], "Could I... please es la forma cortés.")],
    sc(4, 2, [
        ("¿Qué es el significado implícito?", "Lo que se da a entender sin decirlo directamente", "Depende de la situación y la cultura."),
        ("¿Qué significa Would you mind...?", "¿Te importaría...?", "Es una petición cortés."),
        ("¿Cómo se marca el énfasis en un texto escrito?", "Con mayúsculas en la palabra", "Muestra qué palabra se destaca."),
    ]),
    task("Lee este diálogo de ejemplo: «A: Would you like to join us on Friday? B: Thank you for asking, but I have family plans. A: No problem. Maybe another time!» (join = unirse, plans = planes). Escribe en español qué le dice B a A, si es un rechazo, y dos frases que lo hacen cortés.", "B rechaza la invitación con cortesía. Frases: Thank you for asking y but I have family plans. A responde con No problem. Maybe another time!, lo que muestra respeto.", ["identifica el rechazo", "cita dos frases corteses", "describe la respuesta de A"], ["tres respuestas en español"], ["decir que B es descortés", "no citar frases"], "Subraya el agradecimiento y la razón; ambas hacen cortés el rechazo."),
    "Escribe tres formas de decir no con cortesía en inglés.",
    "Escribe una oración con tres significados distintos según la palabra que enfatices.",
)

# ------------------------------------------------------------------ clase 3: estrategias de fluidez
FLU = "«Tom: What do you call the thing you use to open a can? Mia: A can opener. Tom: Right! Sorry, I forgot the word. Mia: No problem. Well, let me think... in my country, we also say 'tin opener', you know? Tom: Oh, I see. Do you know what I mean?» (can opener = abrelatas, forgot = olvidé, tin = lata, let me think = déjame pensar, I see = ya veo)"

lesson(
    OA4, 3, MAT_R,
    "Aprenderé estrategias para hablar con fluidez aunque no sepa todas las palabras: rellenos (well, let me think), paráfrasis (the thing you use to...), comprobación (Do you know what I mean?) y chunks. Sirve para que la conversación avance y para interactuar con seguridad.",
    ["Sé presentarme y preguntar.", "Sé pedir cortésmente que repitan."],
    [
        "Fluidez no es hablar rápido ni sin errores, sino comunicarte de modo que la conversación avance. Cuando te falta una palabra, usa estrategias. La paráfrasis o circunlocución (paraphrase) explica la idea con otras palabras: the thing you use to open a can, it's like a big tree but small, a person who fixes cars. Los rellenos (fillers) como well, let me think, you know, I mean, so... te dan tiempo de pensar sin silencio largo.",
        "Los chunks (bloques) son frases hechas que se aprenden completas: I'd like to..., What do you think about...?, As far as I know..., That's a good point, It depends on... Con ellos hablas más rápido porque no armas cada frase palabra por palabra. Para asegurarte de que te entienden usa comprobaciones (comprehension checks): Do you know what I mean?, Is that clear?, Does that make sense?",
        "También puedes pedir ayuda: How do you say ___ in English?, What's the word for...? Evita callarte o cambiar de idioma por completo. Cuida el equilibrio: demasiados rellenos hacen difícil entender. Practica con tarjetas de chunks y con diálogos cortos, y no te preocupes por imitar un acento, porque la claridad vale más.",
    ],
    [("paraphrase", "parafrasear: explicar con otras palabras"), ("filler", "relleno: well, you know"), ("chunk", "bloque de palabras que se aprende completo"), ("comprehension check", "comprobar que te entienden"), ("What's the word for...?", "¿cuál es la palabra para...?"), ("It depends on", "depende de")],
    [
        ("Parafrasear", FLU + " ¿Qué hace Tom cuando olvida la palabra can opener?", ["Describe el objeto con otras palabras.", "Dice the thing you use to open a can.", "Eso es una paráfrasis."], "Parafrasea: describe lo que hace el objeto"),
        ("Rellenos", FLU + " ¿Qué dos expresiones de Mia le dan tiempo para pensar?", ["Busco expresiones que no cambian el significado.", "Dice Well, let me think...", "También usa you know."], "Well, let me think y you know"),
    ],
    [
        ("Quedarse en silencio cuando falta una palabra.", "La conversación se detiene.", "Describe la idea con otras palabras."),
        ("Llenar cada oración de rellenos.", "Se hace difícil entender el mensaje.", "Usa rellenos con medida."),
    ],
    [
        mr(FLU, "¿Cuál es la frase de Tom que comprueba la comprensión?", "Do you know what I mean?", ["I forgot the word", "Right!"], "Pregunta si la otra persona entendió."),
        mc("¿Cuál es una forma de pedir una palabra que no sabes?", "How do you say 'abrelatas' in English?", ["I do not speak English well enough to ask", "Say it for me, because I forgot the word"], "Es una petición clara."),
        mc("¿Cuál frase es un chunk para dar tu opinión?", "As far as I know", ["According to me opinion", "In my point view"], "Es una frase hecha para opinar con cautela."),
    ],
    [
        mc("Parafrasea 'a bicycle' si no recuerdas la palabra:", "a vehicle with two wheels that you pedal", ["a vehicle with four wheels and an engine", "a place where you keep bikes"], "La paráfrasis explica la función y la forma."),
        mr(FLU, "¿Qué palabra alternativa propone Mia para can opener?", "tin opener", ["bottle opener", "key"], "Dice we also say 'tin opener'."),
        mc("¿Cuál frase usa un relleno?", "Well, let me think about it", ["I ate lunch", "The library closes at six"], "Well, let me think da tiempo para pensar."),
    ],
    [
        mc("Quieres dar una opinión cautelosa en una charla. ¿Qué chunk usas?", "It depends on the situation", ["I always know what is best", "Nobody really knows about that"], "Es una expresión que evita absolutos."),
        mc("No recuerdas la palabra 'umbrella'. ¿Qué paráfrasis sirve?", "the thing you open when it rains", ["the thing you wear on your head", "the thing you use to cut paper"], "Describe la función."),
        mc("Después de explicar algo largo, ¿cómo compruebas que te entienden?", "Does that make sense?", ["Do you hate it?", "Why?"], "Es una comprobación de comprensión."),
    ],
    [
        mc("Un compañero dice que fluidez es hablar sin parar y sin pausas. ¿Qué respuesta es correcta?", "la fluidez es comunicarse con claridad aunque haya pausas y errores", ["solo importa el acento que se tenga al hablar con otras personas", "tiene razón: fluidez es hablar con mucha velocidad y sin pausas"], "Lo central es que la conversación avance."),
        mc("¿Qué es mejor cuando te falta una palabra durante una charla?", "parafrasear o pedir ayuda y seguir hablando", ["decir que no sabes y callar", "cambiar a otro idioma sin avisar"], "Mantiene la comunicación."),
    ],
    [
        mc("Tu compañera dice 'It's like a... a thing. You use it to cut paper.' ¿Qué intenta decir?", "scissors (tijeras)", ["a pen", "a book"], "Describe la función de cortar papel."),
        mc("Dos amigos conversan. Uno usa 'you know' al final de cada frase. ¿Qué efecto tiene?", "demasiados rellenos hacen difícil seguir el mensaje", ["es el único chunk útil para conversar", "mejora siempre la claridad del mensaje"], "El equilibrio importa."),
    ],
    [mc("Quieres pedir que te ayuden con una palabra: ¿qué frase sirve?", "What's the word for 'sombrero' in English?", ["Sombrero what in English, please", "I don't know the word, so I stop"], "Es una petición clara y cortés.")],
    sc(4, 3, [
        ("¿Qué es parafrasear?", "Explicar una idea con otras palabras", "Sirve cuando falta una palabra."),
        ("¿Para qué sirven los rellenos como well o let me think?", "Para ganar tiempo para pensar sin silencio", "Mantienen la conversación."),
        ("¿Qué es un chunk?", "Una frase hecha que se aprende completa", "Permite hablar más rápido."),
    ]),
    task("Imagina que olvidas estas palabras: A) a calendar, B) a backpack, C) a toothbrush. Escribe en inglés una paráfrasis para cada una, de una oración, sin decir la palabra, y una comprobación al final: Do you know what I mean?", "A) It is a paper or screen with the days and months of the year. B) It is a bag you carry on your back to take books to school. C) It is a thing you use to clean your teeth every day. Do you know what I mean?", ["no usa la palabra original", "explica la función o la forma", "incluye la comprobación"], ["tres paráfrasis y una pregunta"], ["decir solo it is a thing", "no incluir la comprobación"], "Agrega la función o la forma si tu descripción es muy general."),
    "Practica en voz alta con una persona de tu casa las tres paráfrasis y pídele que adivine.",
    "Escribe cinco chunks que quieras aprender y una oración con cada uno.",
)

# ------------------------------------------------------------------ clase 4: intercambiar visiones de mundo
PEN1 = "«Hi Sam, I'm writing to tell you about a tradition in my home. In September, many families in Chile get together to celebrate national holidays. We eat traditional food, listen to music and spend time with relatives. It is not the same in every home, but for my family it is a time to feel united. What traditions do you have in your home? Ana» (get together = reunirse, national holidays = fiestas patrias, traditional food = comida típica, relatives = parientes, united = unidos)"
PEN2 = "«Dear Ana, thank you for your message. In my family, we celebrate a harvest festival in autumn. We cook a big meal and thank our neighbors for their help during the year. I think we also value being united, but we do it in a different way. I would like to learn more about your music. Sam» (harvest festival = fiesta de la cosecha, autumn = otoño, thank = agradecer, value = valorar, different = diferente)"

lesson(
    OA4, 4, MAT_R,
    "Aprenderé a describir una tradición propia y preguntar por la de otra persona, a comparar visiones de mundo con respeto y a usar un lenguaje que evita los estereotipos. Sirve para interactuar con alguien de otra cultura y tomar conciencia de mi propia identidad.",
    ["Sé presentarme y hacer preguntas abiertas.", "Sé comparar costumbres con both, whereas y similarly."],
    [
        "Una visión de mundo (worldview) es la manera en que una persona o un grupo entiende la vida, lo importante y lo normal. Las tradiciones (traditions) muestran valores: unirse en familia, agradecer, celebrar la cosecha. Al hablar de tu cultura, usa un lenguaje cuidadoso: In my home..., Many families in my country..., It is not the same in every home. Así evitas decir que todos son iguales.",
        "Para escribir o decir un intercambio cultural usa esta estructura: saludo, descripción de una tradición (qué se hace, cuándo, con quién), el valor que representa para ti (for my family it is a time to feel united), y una pregunta abierta para la otra persona (What traditions do you have in your home?). Al responder, agradece, describe lo tuyo, compara con similarly o however y muestra interés: I would like to learn more about...",
        "La identidad (identity) incluye de dónde vengo, qué valoro y cómo me ven. Al compartirla no hace falta justificar tus costumbres ni juzgar las ajenas. Tu cultura no define a toda persona de tu país, ni la de otra persona define a todos los suyos. No hables de una costumbre ajena con palabras como weird; usa different. Si no estás seguro de un dato cultural, pregunta y no supongas.",
    ],
    [("worldview", "visión de mundo"), ("tradition", "tradición"), ("get together", "reunirse"), ("It is not the same in every home", "no es igual en todos los hogares"), ("value", "valorar / valor"), ("different, not weird", "diferente, no raro")],
    [
        ("Describir una tradición", PEN1 + " ¿Qué tres cosas se hacen en la tradición descrita?", ["Busco qué hacen las familias.", "Comen comida típica, escuchan música y pasan tiempo con parientes.", "Esas son las tres acciones."], "Comer comida típica, escuchar música y estar con parientes"),
        ("Comparar con respeto", PEN2 + " ¿Qué tienen en común las tradiciones de Ana y de la persona que responde?", ["Ana valora estar unidos.", "La persona dice I think we also value being united.", "Comparten el valor de estar unidos."], "Ambas valoran estar unidos, de maneras distintas"),
    ],
    [
        ("Decir 'In my country everybody celebrates the same way'.", "Es un estereotipo: no todos son iguales.", "Di Many families... o In my home..."),
        ("Decir que la tradición de otra persona es weird.", "Es un juicio sin respeto.", "Usa different y pregunta."),
    ],
    [
        mr(PEN1, "¿Qué tradición describe Ana?", "una reunión familiar en septiembre con comida, música y parientes", ["una fiesta de la cosecha en otoño con vecinos", "una carrera de bicicletas entre varias familias"], "Habla de national holidays en septiembre."),
        mr(PEN2, "¿Qué fiesta celebra la familia de la persona que responde?", "una fiesta de la cosecha en otoño", ["las fiestas patrias de Chile", "un cumpleaños de verano"], "Dice a harvest festival in autumn."),
        mr(PEN1, "¿Qué frase evita generalizar?", "It is not the same in every home", ["Everybody celebrates the same way", "All families eat the same food"], "Reconoce diferencias entre hogares."),
    ],
    [
        mr(PEN1, "¿Qué valor representa la tradición para la familia de Ana?", "sentirse unidos", ["ganar dinero", "ser puntuales"], "Dice for my family it is a time to feel united."),
        mr(PEN2, "¿Qué hacen para agradecer en la fiesta de la cosecha?", "agradecen a los vecinos por su ayuda", ["viajan a otra ciudad para celebrar juntos", "compran regalos caros para los invitados"], "Dice thank our neighbors for their help during the year."),
        mc("¿Cuál pregunta abierta puedes agregar al final de tu mensaje?", "What traditions do you have in your home?", ["Do you like traditions in your home", "Is it the same in your home"], "Es abierta y pide explicación."),
    ],
    [
        mc("Completa: 'In my home, we ___ food and share stories.' (preparamos)", "prepare", ["prepares", "preparing"], "Con we se usa el verbo base."),
        mc("Para comparar tu tradición con la de Sam, ¿qué conector sirve?", "Similarly, we also value being united", ["Because we also value being united", "Unlike, we also value being united"], "La semejanza se marca con similarly; because marca causa y unlike marca diferencia."),
        mc("¿Qué frase muestra interés por aprender de otra cultura?", "I would like to learn more about your music", ["Your music is weird, but I will listen", "I already know everything about your music"], "Muestra curiosidad respetuosa."),
    ],
    [
        mc("Un compañero dice que su tradición es la única normal. ¿Cuál es la mejor respuesta?", "Interesting; in my home it is different, and I would like to learn why yours matters", ["That's weird; in my home we do it the right way, so yours is odd", "You are wrong; in my home nobody does that, and I think it is strange"], "Reconoce, describe y pregunta."),
        mc("Una persona extranjera dice 'In Chile, everybody eats the same'. ¿Cómo aclaras sin ofender?", "In many homes it is similar, but it depends on the family", ["That is false; nobody there eats the same", "Of course, they always eat the same food"], "Matiza sin atacar."),
    ],
    [
        mc("Quieres describir una tradición familiar sin inventar datos. ¿Qué es lo mejor?", "usar solo lo que tu familia realmente hace y decir In my home", ["inventar una costumbre más interesante para impresionar", "copiar el texto de otra persona que escribió bien"], "Habla desde tu experiencia."),
        mc("¿Qué elemento NO suele ser necesario al presentar una tradición?", "justificar por qué tu costumbre es mejor", ["describir lo que se hace en tu casa", "decir con quién y cuándo se hace"], "No hace falta comparar para ganar; basta compartir."),
    ],
    [mc("Escribe una frase de cierre para un correo a un amigo extranjero:", "I hope to hear about your traditions soon", ["Answer me now about your traditions", "That is all for now, goodbye then"], "Es cálida y mantiene el intercambio.")],
    sc(4, 4, [
        ("¿Qué es una visión de mundo?", "La manera de entender la vida y lo importante", "Incluye valores y costumbres."),
        ("¿Por qué conviene decir In my home y no In my country everybody?", "Porque evita generalizar", "No todos son iguales."),
        ("¿Qué palabra conviene usar en lugar de weird?", "Different", "No juzga la costumbre ajena."),
    ]),
    task("Escribe un mensaje de cinco oraciones en inglés a una persona de otro país: saluda, describe una tradición de tu casa (qué se hace, cuándo, con quién), di qué valor representa y haz una pregunta abierta sobre las tradiciones de la otra persona. Usa In my home o Many families.", "Hi Alex, in my home we celebrate birthdays with a lunch. Many families do something similar, but not all. We cook together and spend the afternoon talking. For me it is a time to feel close. What traditions do you have in your home?", ["describe la tradición con claridad", "evita generalizar", "incluye una pregunta abierta"], ["mensaje de cinco oraciones"], ["generalizar a todo el país", "no hacer preguntas"], "Cambia las generalizaciones por In my home o Many families y agrega la pregunta."),
    "Lee en voz alta tu mensaje y marca las frases que evitan generalizar.",
    "Escribe una tradición que te gustaría conocer de otra cultura y una pregunta para hacer sobre ella.",
)

# ------------------------------------------------------------------ clase 5: reparar y reflexionar sobre la identidad
REP = "«A: I think the festival is on the thirteenth. B: Sorry, did you say thirteenth or thirtieth? A: Thirteenth, one-three. B: Oh, I see! Thank you. A: No problem. B: Let me check: you mean the thirteenth of this month, right? A: Exactly.» (festival = fiesta, thirteenth = trece, thirtieth = treinta, check = confirmar, exactly = exacto)"

lesson(
    OA4, 5, MAT_L,
    "Aprenderé a reparar un malentendido (pedir aclaración, corregirme, reformular, confirmar) y a reflexionar sobre lo aprendido de otra cultura y de mi propia identidad. Sirve para interactuar con fluidez y cerrar la conversación con conciencia de quién soy.",
    ["Sé pedir repetición con cortesía.", "Sé parafrasear y comprobar la comprensión."],
    [
        "Los malentendidos son normales en una conversación entre culturas. Para reparar (repair) hay tres caminos. Pedir aclaración: Sorry, did you say thirteenth or thirtieth?; Could you say that again?; What do you mean by...? Confirmar lo que entendiste: You mean the thirteenth, right?; So you are saying that... Corregirte o reformular: I mean...; Sorry, let me say that again; In other words,...",
        "Fíjate en pares de números que suenan parecidos: thirteen y thirty, fifteen y fifty, sixteen y sixty. En -teen la sílaba final tiene fuerza; en -ty la fuerza está al inicio. Si hay duda, confirma con los números dígito por dígito: one-three. También confirma fechas, horas y lugares, porque un error pequeño puede cambiar todo.",
        "Después de interactuar, reflexiona: ¿qué aprendí de la otra cultura?, ¿qué descubrí de mi propia identidad?, ¿qué suposición mía cambió? Puedes escribir I learned that..., I used to think that..., but now I see that..., One thing I value in my own culture is... Reflexionar no significa elegir una cultura mejor: significa mirar con curiosidad las diferencias y ver lo propio con más claridad.",
    ],
    [("repair", "reparar un malentendido"), ("Could you say that again?", "¿podrías repetirlo?"), ("You mean ..., right?", "quieres decir..., ¿verdad?"), ("I mean / in other words", "quiero decir / en otras palabras"), ("thirteen / thirty", "trece / treinta"), ("I learned that", "aprendí que")],
    [
        ("Pedir aclaración", ADULT + REP + " ¿Qué duda tiene B?", ["Busco la pregunta de B.", "Pregunta si A dijo thirteenth o thirtieth.", "La duda es entre trece y treinta."], "Si la fecha es el trece o el treinta"),
        ("Confirmar", ADULT + REP + " ¿Cómo confirma B lo que entendió?", ["Busco una frase con you mean.", "Dice you mean the thirteenth of this month, right?", "Eso confirma la fecha."], "You mean the thirteenth of this month, right?"),
    ],
    [
        ("Asentir sin haber entendido.", "El malentendido queda sin reparar.", "Pide aclaración con cortesía."),
        ("Pensar que reflexionar es elegir la cultura mejor.", "Reflexionar es comprender las diferencias.", "Escribe qué aprendiste, no cuál es mejor."),
    ],
    [
        ml(REP, "¿Cuál es la fecha que se confirma?", "el trece de este mes", ["el treinta de este mes", "el quince de este mes"], "Thirteenth es trece y B lo confirma con you mean the thirteenth."),
        mc("¿Qué frase pide aclaración con cortesía?", "Sorry, could you say that again?", ["What? I did not hear you", "Say it again, I could not hear"], "Es una petición educada."),
        mc("¿Qué expresión sirve para reformular lo que dijiste?", "In other words,", ["Finally,", "Therefore,"], "In other words dice lo mismo de otro modo."),
    ],
    [
        ml(REP, "¿Qué hace A después de la duda de B?", "repite el número separando los dígitos", ["cambia de tema para evitar la duda", "se enoja porque no la entendieron"], "Dice Thirteenth, one-three."),
        mc("¿Cuál número suena más fuerte en la sílaba final: fifteen o fifty?", "fifteen", ["fifty", "los dos igual"], "En -teen la sílaba final lleva fuerza."),
        mc("¿Qué opción es una autocorrección cortés?", "Sorry, I mean the thirteenth", ["No, you are wrong", "Never mind"], "I mean corrige lo dicho."),
    ],
    [
        mc("Alguien dice por teléfono 'Take bus number fifteen'. Tú entendiste 'fifty'. ¿Qué haces?", "confirmar: Do you mean fifteen or fifty?", ["subir al bus 50 sin preguntar", "no tomar ningún bus"], "Confirmar evita un error de número."),
        mc("Completa para reflexionar: 'I used to think that my way was the only one, but now I ___ that other ways also show care.'", "see", ["sees", "saw see"], "I see that es la forma natural."),
        mc("¿Qué frase expresa un aprendizaje?", "I learned that families can show love in different ways", ["I told that families are all the same everywhere in the world", "I knew nothing about it and I really did not care at all"], "Expresa un aprendizaje y respeto."),
    ],
    [
        mc("Una compañera dice que, después de un intercambio, 'ya sé cuál cultura es mejor'. ¿Qué respuesta es adecuada?", "reflexionar es ver diferencias con curiosidad, no elegir una mejor", ["tiene razón, hay una cultura mejor que otra y hay que decirlo", "no hay nada que aprender de otra cultura después de un intercambio"], "Se aprende a comprender, no a ranquear."),
        ml(REP, "¿Qué hizo B para evitar un error?", "confirmó la fecha antes de seguir", ["no hizo nada ante la duda de A", "cambió la fecha por otra distinta"], "Una confirmación evita un error posible."),
    ],
    [
        mc("Escribes una reflexión sobre una conversación con un estudiante de otro país. ¿Qué es lo mejor?", "describir qué aprendiste de su cultura y qué notaste de la tuya", ["inventar datos que suenen interesantes para que se lea mejor", "juzgar a la persona por lo que dijo durante la conversación"], "La reflexión mira lo aprendido y lo propio."),
        mc("En una videollamada hay ruido y no oyes una palabra. ¿Cuál es la mejor reparación?", "Sorry, the sound is bad. Could you repeat the last word?", ["I'm leaving the call because I cannot hear anything at all", "Nothing, I will pretend I understood so I do not bother them"], "Explica el problema y pide repetir."),
    ],
    [mc("Quieres cerrar una conversación con respeto. ¿Qué frase sirve?", "It was great talking to you. I learned a lot", ["That's enough talking for today, I have to go now", "Bye, whatever, I am in a hurry and I have no time"], "Agradece y valora la conversación.")],
    sc(4, 5, [
        ("¿Para qué sirve You mean ..., right?", "Para confirmar lo que entendiste", "Así se evitan los malentendidos."),
        ("¿Qué frase sirve para empezar una reflexión sobre lo aprendido?", "I learned that...", "Expresa un aprendizaje."),
        ("¿Por qué conviene confirmar fechas y horas?", "Porque un error pequeño puede cambiar todo", "Hay números que suenan parecidos."),
    ]),
    task("Escribe una reflexión de cuatro oraciones en inglés después de una conversación (de ejemplo) con un estudiante de otro país sobre sus tradiciones: una oración con I learned that..., una con I used to think that..., una sobre algo que valoras de tu propia cultura y una frase para cerrar con respeto.", "I learned that many families like to share a meal together. I used to think that everyone celebrated in the same way. One thing I value in my own culture is spending time with relatives. It was great talking to you.", ["usa las cuatro estructuras", "no juzga a la otra cultura", "habla de lo propio"], ["cuatro oraciones"], ["decir cuál cultura es mejor", "no incluir lo propio"], "Revisa las cuatro estructuras y reemplaza los juicios por descripciones."),
    "Practica con una persona de tu casa una conversación donde ella dice un número y tú confirmas con You mean...?",
    "Escribe tres frases de reparación que quieras recordar.",
)

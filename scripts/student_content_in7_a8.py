"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 08 (funciones del lenguaje del año: cantidades, descripciones,
obligación y prohibición, intenciones, posesión, tiempo y modo, preguntas, causa y efecto, pasado, acciones simultáneas).
Cada regla se explica en la clase antes de usarla; los ejercicios son cerrados y se resuelven con lo escrito.
"""
from __future__ import annotations

from student_content_in7_a import lesson, task
from student_lessons import arith

OA8 = "IN07 OA 08"
MAT = "Los datos, diálogos y frases escritos en cada ejercicio, lápiz y, para practicar en voz alta, una persona de tu casa que te escuche."

SHOP = "«At the sports shop. Seller: Good morning. Can I help you? Ana: Yes. I need a helmet and knee pads for my brother. He is nervous because he is learning to skate. Seller: These helmets are red and those are blue. There are twenty helmets on sale. Ana: How much is the red one? Seller: Twelve thousand pesos. Remember: he mustn't skate without a helmet. Ana: I'll take the red one. Yesterday he fell and hurt his knee, so we also need the knee pads.» (shop = tienda, helmet = casco, knee pads = rodilleras, skate = patinar, on sale = en oferta, fell = se cayó, hurt = lastimó, knee = rodilla)"
RAIN = "«Yesterday, Tom was cycling when suddenly a dog crossed the road. He stopped quickly. While he was waiting, a woman was walking the dog back. Today Tom is going to take a different road.» (cycling = andando en bicicleta, suddenly = de pronto, crossed = cruzó, road = camino, waiting = esperando, different = distinto)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA8, 1, MAT,
    "Aprenderé a expresar cantidades, contar y enumerar con there is, there are, many, much, some, a lot of, a little, a few y números hasta cien. Sirve para decir cuántas cosas o cuánta cantidad hay.",
    ["Sé contar hasta cien en inglés.", "Conozco palabras como students, water y books."],
    [
        "Para decir que algo existe y cuánto hay usa There is con una sola cosa o con algo que no se cuenta (water, milk) y There are con varias cosas. Ejemplos: There is some water in the bottle. There are eighty students in the gym. Some significa algunos o algo de, y se usa en frases afirmativas.",
        "Las palabras de cantidad dependen del tipo de sustantivo. Many se usa con cosas que se cuentan en plural: many students, many books. Much se usa con cosas que no se cuentan, sobre todo en preguntas y negaciones: How much water is there? There isn't much milk. A lot of sirve para los dos tipos en frases afirmativas. A few es «unos pocos» con cosas contables (a few chairs) y a little es «un poco» con no contables (a little sugar).",
        "Los números: eighty es 80 y ninety es 90; thirteen termina en -teen (13) y thirty termina en -ty (30), con el acento en distinto lugar. A hundred es cien. Too, al final de una oración, significa «también»: I like that film too. Antes de many o much, too significa «demasiado»: too many cars, too much noise. Para grados usa very (muy) y a bit o a little (un poco): he is very tired o he is a bit tired.",
    ],
    [("There is / There are", "hay (singular o no contable / plural)"), ("many / much", "muchos (contables) / mucho (no contable)"), ("a few / a little", "unos pocos / un poco"), ("a lot of", "mucho, muchos"), ("eighty / a hundred", "ochenta / cien"), ("too", "también (al final de la oración)")],
    [
        ("There is o there are", "Completa: «There ___ a hundred students in the gym.» (is / are)", ["Students es plural.", "Con plural se usa are.", "There are a hundred students."], "are"),
        ("Many o much", "Completa: «How ___ water is there in the bottle?» (many / much)", ["Water no se cuenta.", "Con no contables se usa much.", "How much water is there?"], "much"),
    ],
    [
        ("Usar many con agua o leche.", "Se olvida que las cosas no contables no llevan many.", "Usa much o a lot of."),
        ("Confundir thirteen con thirty.", "Los dos números suenan parecidos.", "Thirteen termina en -teen (13) y thirty en -ty (30)."),
    ],
    [
        ("Completa: «There ___ ninety books in the library.» (is / are)", "are", "Books es plural."),
        ("Completa: «There ___ some water in the bottle.» (is / are)", "is", "Water no se cuenta."),
        ("Hay 40 personas en una sala para 20. Completa: «There are ___ people in the room.» (too many / too much)", "too many", "People se cuenta, así que se usa too many."),
    ],
    [
        ("Completa: «How ___ students are there in the room?» (many / much)", "many", "Students se cuenta."),
        ("Elige la oración correcta. a) There are some oranges. b) There is some oranges.", "a) There are some oranges.", "Oranges es plural y exige are."),
        ("¿Qué número es 30? a) thirty b) thirteen", "a) thirty", "Thirty termina en -ty."),
    ],
    [
        ("Hay una bandeja con 12 manzanas. Completa: «There ___ twelve apples on the tray.» (is / are)", "are", "Apples es plural."),
        arith("En 7A hay 28 estudiantes y en 7B hay 30. ¿Cuántos estudiantes hay entre los dos cursos?", "28+30", "Se suman los dos cursos.", " estudiantes"),
        ("¿Qué significa «too» en «I like that film too»?", "También", "Al final de una oración significa también."),
    ],
    [
        ("Elige la oración correcta. a) There isn't much milk. b) There isn't many milk.", "a) There isn't much milk.", "Milk no se cuenta."),
        ("Completa con a little o a few: «There are ___ chairs in the room.»", "a few", "Chairs se cuenta."),
        ("Completa con a little o a few: «There is ___ sugar in the cup.»", "a little", "Sugar no se cuenta."),
    ],
    [
        arith("Una caja tiene 100 lápices. Se usan 35. ¿Cuántos lápices quedan?", "100-35", "Se restan los usados al total.", " lápices"),
        ("¿Cuál muestra menos cansancio? a) He is a bit tired. b) He is very tired.", "a) He is a bit tired.", "A bit es un poco y very es mucho."),
    ],
    [("En el gimnasio hay noventa estudiantes y mucho ruido. ¿Cuál frase es correcta? a) There are ninety students and there is a lot of noise. b) There is ninety students and there are a lot of noise.", "a) There are ninety students and there is a lot of noise.", "Students es plural y exige are; noise no se cuenta y lleva is.")],
    [
        ("¿Qué se usa con cosas que se cuentan: many o much?", "Many", "Con plurales contables."),
        ("En Inglés de 7.º (OA 8, clase 1): ¿Qué significa «a lot of»?", "Mucho o muchos", "Sirve para contables y no contables."),
        ("¿Qué número es «a hundred»?", "100", "A hundred es cien."),
    ],
    task("Mira tu pieza o la cocina de tu casa y escribe cuatro frases en inglés sobre lo que hay: una con There is, una con There are, una con many o much y otra con a few o a little. Sin usar datos personales: hablas de objetos.", "There is a table. There are three chairs. There aren't many books. There is a little milk.", ["usa There is y There are correctamente", "usa many o much bien", "usa a few o a little bien"], ["hoja con cuatro frases", "nota de la persona que revisó"], ["there is con plurales", "many con no contables"], "Reconoce las frases correctas y ayuda a corregir la concordancia."),
    "Cuenta en voz alta de uno en uno hasta cien y marca con un lápiz el treinta y el trece.",
    "Escribe una pregunta con How many y otra con How much sobre tu casa y responde con una frase.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA8, 2, MAT,
    "Aprenderé a identificar y describir personas, objetos y actividades con these/those, adjetivos, adverbios y posesivos. Sirve para decir cómo son las cosas, cómo se ve alguien y cómo se hace una acción.",
    ["Sé usar there is y there are.", "Conozco adjetivos como fast, big y tired."],
    [
        "These (estos) se usa para varias cosas cerca de ti y those (esos o aquellos) para varias cosas lejos: These cars are fast. Those cars are red. Para el singular se usa this y that. Para decir de qué material es algo pon el adjetivo antes del sustantivo: It's a plastic bottle. Para hablar de actividades usa el verbo con -ing como sujeto: Skating is cool. Riding is boring.",
        "Para describir cómo se ve alguien, usa look + adjetivo: He looks tired, She looks hungry, They look nervous. Después de look va un adjetivo, no un adverbio: He looks nervous. Para el estado de ánimo usa I'm angry about (enojado por algo) o I'm angry with (enojado con una persona). Los adverbios de modo (adverbs) cuentan cómo se hace una acción y suelen terminar en -ly: She sings quietly. They run very fast.",
        "Para la posesión agrega 's a una persona: the student's book (el libro de un estudiante). Si son varios y el plural termina en -s, agrega solo el apóstrofo: the students' instruments (los instrumentos de los estudiantes). Practica mirando una foto y diciendo tres frases: qué hay, cómo se ven las personas y qué hacen.",
    ],
    [("these / those", "estos / aquellos (varias cosas)"), ("looks tired", "se ve cansado"), ("angry about / with", "enojado por algo / con alguien"), ("quietly", "en silencio, en voz baja"), ("student's / students'", "de un estudiante / de varios estudiantes"), ("plastic", "plástico")],
    [
        ("Cerca y lejos", "Señalas autos que están cerca de ti. Completa: «___ cars are fast.» (These / Those)", ["Los autos están cerca.", "Para varias cosas cerca se usa these.", "These cars are fast."], "These"),
        ("Estado de ánimo", "Completa con un adjetivo: «He looks ___ after a long run.» (tired / tiredly)", ["Después de look va un adjetivo.", "Tired es el adjetivo.", "He looks tired."], "tired"),
    ],
    [
        ("Usar un adverbio después de look: «He looks nervously».", "Se confunde adjetivo con adverbio.", "Después de look usa un adjetivo: He looks nervous."),
        ("Escribir students' book cuando hay un solo estudiante.", "El apóstrofo va antes de la s en el singular.", "El libro de un estudiante es the student's book."),
    ],
    [
        ("Señalas autos cerca de ti. Completa: «___ cars are fast.» (These / Those)", "These", "These es para varias cosas cerca."),
        ("En «It's a plastic bottle», ¿de qué material es la botella?", "De plástico", "Plastic es plástico."),
        ("¿Qué significa «He looks tired»?", "Se ve cansado", "Looks tired describe su aspecto."),
    ],
    [
        ("Señalas libros que están lejos. Completa: «___ books are old.» (These / Those)", "Those", "Those es para varias cosas lejos."),
        ("En «Skating is boring», ¿qué opina la persona de patinar?", "Que es aburrido", "Boring es aburrido."),
        ("Completa: «She is angry ___ her friend because he was late.» (about / with)", "with", "Se usa with con una persona."),
    ],
    [
        ("Una niña con una mochila pesada bosteza y tiene los ojos cerrados. Completa: «She looks ___.» (tired / hungry)", "tired", "Bostezar y cerrar los ojos indican cansancio."),
        ("Convierte el adjetivo en adverbio: «She sings (quiet).» Escribe la palabra correcta.", "quietly", "El adverbio de quiet es quietly."),
        ("Escribe la forma posesiva: «the instruments of the students».", "the students' instruments", "Varios estudiantes: el apóstrofo va después de la s."),
    ],
    [
        ("¿Por qué se usa these y no those cuando las cosas están cerca? a) porque these indica cercanía b) porque those es singular", "a) porque these indica cercanía", "Those indica lejanía."),
        ("Elige la oración correcta. a) He looks nervous before the test. b) He looks nervously before the test.", "a) He looks nervous before the test.", "Después de look va un adjetivo."),
    ],
    [
        ("En «They run very fast», ¿qué indica very? a) grado: mucho b) tiempo: ayer", "a) grado: mucho", "Very intensifica a fast y dice cuánto."),
        ("En «the students' instruments», ¿cuántos estudiantes hay? a) varios b) uno", "a) varios", "El apóstrofo después de la s indica plural."),
    ],
    [("Describe lo que ves: dos niños cerca de ti andan en patineta y dos bicicletas lejos son rojas. ¿Qué frases son correctas? a) These children are skating. Those bikes are red. b) Those children are skating. These bikes are red.", "a) These children are skating. Those bikes are red.", "These indica cercanía y those lejanía.")],
    [
        ("¿Qué se usa para varias cosas cerca?", "These", "These es estos."),
        ("En Inglés de 7.º (OA 8, clase 2): ¿Qué significa «quietly»?", "En voz baja o en silencio", "Es un adverbio de modo."),
        ("¿Cómo se dice «de un estudiante»?", "The student's", "El apóstrofo va antes de la s."),
    ],
    task("Observa una fotografía o tu entorno. Escribe cuatro frases en inglés: una con these o those, una con look + adjetivo, una con un adverbio terminado en -ly y una con posesión ('s o s'). Léelas a una persona de tu casa.", "These shoes are blue. My cousin looks happy. She walks quietly. This is Tom's bag.", ["usa these o those bien", "usa look + adjetivo", "usa un adverbio y un posesivo"], ["hoja con cuatro frases", "nota de la persona que revisó"], ["usar adverbio con look", "mal apóstrofo"], "Reconoce las frases correctas y revisa con la persona de tu casa el uso del apóstrofo."),
    "Señala objetos cercanos y lejanos de tu casa y di una frase con these o those para cada uno.",
    "Escribe una descripción de seis frases de un parque, con dos adjetivos, dos adverbios y un posesivo.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA8, 3, MAT,
    "Aprenderé a expresar obligación, prohibición, sugerencias, necesidades e intenciones con must, mustn't, could, don't, need to, want to y forget to. Sirve para dar reglas, proponer ideas y decir lo que quiero o necesito.",
    ["Sé usar there is y there are.", "Conozco palabras como helmet, rule y practice."],
    [
        "Para hablar de una obligación fuerte usa must (debo, debes): I must practice every day. You must wear a helmet. Para una prohibición usa mustn't (no debes, está prohibido): You mustn't ride without a helmet. Después de must y mustn't el verbo queda en forma simple: must practice, mustn't run. Para una orden negativa directa usa Don't + verbo: Don't run in the corridor.",
        "Para hacer una sugerencia usa could o we could: We could practice together (podríamos practicar juntos). Es más suave que una orden. Para hablar de intenciones y necesidades usa want to (querer), need to (necesitar) y forget to (olvidar): We need to recycle. I want to learn English. Don't forget to bring your notebook.",
        "Elige la expresión según lo que quieres comunicar. Si es una regla importante, usa must o mustn't. Si propones una idea, usa could. Si hablas de lo que deseas o requieres, usa want to o need to. Cuando des una regla, di la razón con because: You mustn't touch the stove because it is hot.",
    ],
    [("must", "debo, debes (obligación)"), ("mustn't", "no debes, está prohibido"), ("could", "podría, podríamos (sugerencia)"), ("Don't + verbo", "no hagas"), ("need to", "necesitar"), ("forget to", "olvidar hacer algo")],
    [
        ("Obligación", "Completa: «I ___ practice every day if I want to win.» (must / mustn't)", ["Practicar es necesario para ganar.", "Es una obligación, no una prohibición.", "I must practice."], "must"),
        ("Prohibición", "Completa: «You ___ ride without a helmet.» (must / mustn't)", ["Montar sin casco es peligroso.", "Se prohíbe.", "You mustn't ride without a helmet."], "mustn't"),
    ],
    [
        ("Usar must para algo que está prohibido.", "Se confunde obligación con prohibición.", "Si no se puede hacer, usa mustn't."),
        ("Conjugar el verbo después de must: «must to run».", "Después de must no va to.", "Escribe must + verbo simple."),
    ],
    [
        ("Completa: «You ___ ride without a helmet.» (must / mustn't)", "mustn't", "Es una prohibición de seguridad."),
        ("Completa: «I ___ practice every day to win.» (must / mustn't)", "must", "Es una obligación para lograr una meta."),
        ("¿Qué significa «Don't run in the corridor»?", "No corras en el pasillo", "Don't + verbo es una orden negativa."),
    ],
    [
        ("«We could cook pasta tonight». ¿Qué expresa? a) una sugerencia b) una obligación", "a) una sugerencia", "Could propone una idea."),
        ("¿Qué significa «We need to recycle»?", "Necesitamos reciclar", "Need to es necesitar."),
        ("¿Qué significa «Don't forget to bring your notebook»?", "No olvides traer tu cuaderno", "Forget to es olvidar hacer algo."),
    ],
    [
        ("Un cartel dice «No running». ¿Cuál frase lo expresa? a) You mustn't run. b) You must run.", "a) You mustn't run.", "No running prohíbe correr."),
        ("Tienes hambre y propones a tu amigo: «We ___ eat a sandwich.» (could / mustn't)", "could", "Could sugiere una idea."),
        ("Si no tienes lápiz y debes escribir, dices «I ___ a pencil». (need / forget)", "need", "Need expresa una necesidad."),
    ],
    [
        ("¿Cuál frase expresa una prohibición? a) You mustn't touch the stove. b) You must wash your hands.", "a) You mustn't touch the stove.", "Mustn't prohíbe una acción."),
        ("Un cartel dice «You must wear a helmet». ¿Es obligación o prohibición?", "Obligación", "Must expresa que es necesario usarlo."),
    ],
    [
        ("En «You must wear goggles. You mustn't eat. You must wash your hands.» (goggles = lentes de seguridad), ¿cuántas reglas son obligaciones?", "2", "Las dos con must; mustn't es una prohibición."),
        ("Ordena las palabras (empieza con You): mustn't / run / the / lab / in", "You mustn't run in the lab.", "Sujeto, mustn't y verbo simple."),
    ],
    [("La regla de la biblioteca dice «You mustn't eat or drink here». ¿Qué no puedes hacer? a) comer ni beber b) leer", "a) comer ni beber", "Mustn't prohíbe comer o beber.")],
    [
        ("¿Qué expresa mustn't?", "Una prohibición", "Dice que no se puede hacer."),
        ("¿Qué expresa could?", "Una sugerencia", "Propone una idea."),
        ("¿Qué va después de must?", "El verbo simple", "Sin la palabra to."),
    ],
    task("Escribe cinco frases para una piscina del colegio: dos obligaciones con must, dos prohibiciones con mustn't y una sugerencia con could. Lee las reglas en voz alta a una persona de tu casa.", "You must shower first. You must wear a swimming cap. You mustn't run. You mustn't dive. We could swim in pairs.", ["usa must y mustn't correctamente", "agrega una sugerencia con could", "los verbos van en forma simple"], ["hoja con cinco frases", "nota de la persona que revisó"], ["decir must to", "usar must para una prohibición"], "Reconoce las reglas correctas y comprueba que la prohibición se entienda."),
    "Lee en voz alta cinco reglas de tu casa y di si son obligaciones o prohibiciones.",
    "Escribe tres consejos para un amigo que quiere aprender a andar en bicicleta, usando must, mustn't y could.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA8, 4, MAT,
    "Aprenderé a hablar de acciones habituales, pasadas, simultáneas y de planes futuros con every week, yesterday, was/were + -ing, when, while, suddenly, did/didn't y going to. Sirve para contar qué pasó y qué va a pasar.",
    ["Sé el pasado de verbos como play, go y fall.", "Conozco when y while."],
    [
        "Para rutinas usa el presente con palabras como every week: She visits her grandma every week. Para hechos terminados usa el pasado con yesterday o last: Yesterday I played football; he won the race. Para preguntar por el pasado usa did + verbo simple: Did he cook? Yes, he did. No, he didn't. Para el presente usa does: Does he cook? Yes, he does. No, he doesn't.",
        "Para una acción larga que fue interrumpida usa was/were + -ing y when: I was playing football in the yard when it started to rain. Para dos acciones al mismo tiempo usa while: While he was cycling, she was listening to music. Suddenly (de pronto) indica un cambio inesperado. Para planes futuros usa going to: Tomorrow we are going to visit the museum.",
        "También puedes expresar causa y efecto con if: Ice melts if you heat it. La causa es lo que viene después de if (heat it) y el efecto es lo que ocurre (ice melts). Para ordenar una historia usa first, next, finally. Cuando cuentes algo, decide si es hábito, hecho terminado, acción en curso o plan, y elige el tiempo verbal correcto.",
    ],
    [("every week", "cada semana (rutina)"), ("yesterday", "ayer"), ("was / were + -ing", "estaba haciendo algo"), ("when / while", "cuando / mientras"), ("suddenly", "de pronto"), ("going to", "voy a (plan futuro)")],
    [
        ("Pasado simple", "Completa: «Yesterday I ___ football.» (play / played)", ["Yesterday indica pasado.", "El pasado de play es played.", "Yesterday I played football."], "played"),
        ("Pregunta y respuesta corta", "Completa la respuesta: «Did he cook? Yes, he ___.» (did / does)", ["La pregunta usa did.", "La respuesta corta repite did.", "Yes, he did."], "did"),
    ],
    [
        ("Usar el presente con yesterday: «Yesterday I play».", "Se olvida el tiempo pasado.", "Con yesterday usa el pasado: played."),
        ("Usar did con el verbo en pasado: «Did he cooked?».", "Se marca el pasado dos veces.", "Después de did el verbo va simple: Did he cook?"),
    ],
    [
        ("Completa: «Yesterday I ___ football.» (play / played)", "played", "Yesterday pide el pasado."),
        ("Completa: «Did he cook? Yes, he ___.» (did / does)", "did", "La respuesta repite el auxiliar de la pregunta."),
        ("Completa con el presente: «She ___ her grandma every week.» (visit / visits)", "visits", "Con she, el verbo lleva -s."),
    ],
    [
        ("«I was playing football when it started to rain». ¿Qué acción interrumpe a la otra?", "La lluvia", "Started to rain interrumpe el juego."),
        ("«While he was cycling, she was listening to music». ¿Las dos acciones ocurren al mismo tiempo? Responde sí o no.", "Sí", "While indica acciones simultáneas."),
        ("¿Qué significa «suddenly»?", "De pronto", "Indica un cambio inesperado."),
    ],
    [
        ("Completa: «I ___ playing in the yard when it started to rain.» (was / were)", "was", "Con I se usa was."),
        ("Completa: «While she was cycling, he ___ listening to music.» (was / were)", "was", "He va con was."),
        ("Completa la respuesta: «Does he cook? No, he ___.» (doesn't / didn't)", "doesn't", "La pregunta está en presente."),
    ],
    [
        ("En «I was playing football when it started to rain», ¿qué ocurrió primero? a) el juego b) la lluvia", "a) el juego", "El juego ya estaba en curso cuando empezó la lluvia."),
        ("En «Ice melts if you heat it», ¿cuál es la causa? a) heat it b) ice melts", "a) heat it", "Lo que viene después de if es la causa."),
    ],
    [
        ("Completa un plan futuro: «Tomorrow we ___ visit the museum.» a) are going to b) went to", "a) are going to", "Tomorrow se une a going to."),
        arith("El viaje duró 3 días y cada día caminaron 4 horas. ¿Cuántas horas caminaron en total?", "3*4", "Se multiplican los días por las horas diarias.", " horas"),
    ],
    [(RAIN + " ¿Qué hacía Tom cuando apareció el perro?", "Andaba en bicicleta", "Dice Tom was cycling.")],
    [
        ("En Inglés de 7.º (OA 8, clase 4): ¿Qué auxiliar se usa en preguntas en pasado?", "Did", "Después de did el verbo va simple."),
        ("En Inglés de 7.º (OA 8, clase 4): ¿Qué indica «while»?", "Que dos acciones ocurren a la vez", "Une acciones simultáneas."),
        ("¿Qué significa «going to»?", "Voy a (plan futuro)", "Expresa un plan."),
    ],
    task("Escribe cuatro frases en inglés sobre tu semana: una rutina con every week, un hecho de ayer con el pasado, una acción en curso interrumpida con was/were + -ing y when, y un plan con going to. Léelas en voz alta a una persona de tu casa.", "I play chess every week. Yesterday I read a book. I was reading when the phone rang. Tomorrow I am going to visit a museum.", ["usa el tiempo correcto en cada frase", "usa when o while correctamente", "las lee en voz alta"], ["hoja con cuatro frases", "nota de la persona que revisó"], ["did con verbo en pasado", "olvidar was/were con -ing"], "Reconoce los tiempos correctos y revisa con la persona de tu casa las formas del pasado."),
    "Cuenta en voz alta qué hiciste ayer en tres frases en pasado y qué harás mañana en una con going to.",
    "Escribe una historia de cinco frases con un hecho inesperado (suddenly), una acción en curso y una pregunta con did.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA8, 5, MAT,
    "Aprenderé a combinar varias funciones del lenguaje (cantidades, descripciones, reglas, necesidades, pasado y causa) en una interacción real, como comprar en una tienda. Sirve para comunicarme en situaciones completas.",
    ["Sé usar there is, these/those, must/mustn't y el pasado.", "Conozco palabras como helmet y price."],
    [
        "Las conversaciones reales mezclan varias funciones. En una tienda se pide ayuda (Can I help you?), se expresa una necesidad (I need a helmet), se describe (He is nervous), se señalan objetos (These helmets are red and those are blue), se dicen cantidades (There are twenty helmets), se pregunta un precio (How much is it?), se advierten reglas (He mustn't skate without a helmet) y se explican causas con so o because.",
        "Para participar bien, escucha primero qué función quiere cumplir cada frase y escoge el tiempo y las palabras adecuadas. Una necesidad usa need to o I need; una prohibición usa mustn't; un hecho pasado usa el pasado; una causa usa so o because. Si necesitas ayuda para continuar, usa un relleno como well o so y sigue con una idea.",
        "Antes de hablar, prepara los chunks más probables de la situación. Después de la conversación, repásala: ¿usaste bien los tiempos?, ¿hubo una frase que no se entendió? Eso te ayuda a corregir. Algunas expresiones de uso común se aprenden como bloque: have fun o have a good time (pasarlo bien), make friends (hacer amigos), make plans (hacer planes), make a mistake (cometer un error), laugh at (reírse de), ask for (pedir), give advice on (dar consejos sobre), afraid of flying (miedo a volar). Las palabras compuestas juntan dos palabras: outdoor (al aire libre), indoor (bajo techo), notebook (cuaderno), sports shop (tienda de deportes). En esta clase vas a trabajar con un diálogo completo en una tienda y con situaciones nuevas parecidas.",
    ],
    [("Can I help you?", "¿puedo ayudarle?"), ("I'll take it", "me lo llevo"), ("on sale", "en oferta"), ("so", "por eso, entonces"), ("function", "función: lo que quiero lograr al hablar"), ("knee pads", "rodilleras"), ("have fun / make friends", "pasarlo bien / hacer amigos"), ("outdoor / indoor", "al aire libre / bajo techo")],
    [
        ("Información del diálogo", SHOP + " ¿Qué necesita Ana?", ["Busco I need.", "Dice a helmet and knee pads.", "Necesita un casco y rodilleras."], "Un casco y rodilleras"),
        ("Identificar la función", SHOP + " La vendedora dice «he mustn't skate without a helmet». ¿Qué función cumple?", ["Mustn't indica una prohibición.", "Advierte sobre seguridad.", "Es una regla."], "Una prohibición o regla de seguridad"),
    ],
    [
        ("Elegir el tiempo verbal sin pensar en la función.", "Se mezclan pasado, presente y futuro.", "Pregúntate qué quieres comunicar antes de elegir el tiempo."),
        ("Olvidar la causa que explica una compra.", "El diálogo parece desconectado.", "Usa so o because para unir la causa con la acción."),
    ],
    [
        (SHOP + " ¿Cuánto cuesta el casco rojo?", "12.000 pesos", "Dice twelve thousand pesos."),
        (SHOP + " ¿Cuántos cascos hay en oferta?", "20", "Dice There are twenty helmets on sale."),
        ("¿Qué significa «outdoor» en «outdoor games»? a) al aire libre b) bajo techo", "a) al aire libre", "Out es afuera y door es puerta: juegos de afuera. Indoor es lo contrario."),
    ],
    [
        (SHOP + " ¿Por qué está nervioso el hermano de Ana?", "Porque está aprendiendo a patinar", "Dice because he is learning to skate."),
        ("Completa con make o have: «I want to ___ new friends at the club.»", "make", "Make friends es la expresión para conocer amigos nuevos."),
        (SHOP + " ¿Qué prohíbe la vendedora? a) patinar sin casco b) comprar rodilleras", "a) patinar sin casco", "Dice he mustn't skate without a helmet."),
    ],
    [
        (SHOP + " En «Yesterday he fell and hurt his knee», ¿qué tiempo verbal se usa? a) pasado b) futuro", "a) pasado", "Fell y hurt son pasados."),
        ("Completa con make o have: «We ___ fun at the outdoor games.»", "have", "Have fun es la expresión para pasarlo bien."),
        arith(SHOP + " Si Ana compra dos cascos rojos, ¿cuántos pesos paga?", "2*12000", "Cada casco rojo cuesta 12.000 pesos.", " pesos"),
    ],
    [
        (SHOP + " ¿Por qué compra Ana las rodilleras? a) porque su hermano se cayó y se lastimó la rodilla b) porque estaban en oferta", "a) porque su hermano se cayó y se lastimó la rodilla", "Dice so we also need the knee pads."),
        (SHOP + " ¿Qué frase aconseja usar siempre el casco? a) he mustn't skate without a helmet b) I'll take the red one", "a) he mustn't skate without a helmet", "Es la regla de seguridad."),
    ],
    [
        ("Ordena el diálogo. A) Can I help you? B) I need a helmet. C) I'll take the red one.", "A, B, C", "Primero se ofrece ayuda, luego se pide y al final se decide."),
        arith(SHOP + " Si Ana paga el casco rojo con un billete de $20.000, ¿cuántos pesos de vuelto recibe?", "20000-12000", "Se resta el precio del casco al billete.", " pesos"),
    ],
    [("Tu hermano pequeño está nervioso por una prueba. Dale una sugerencia con could. a) We could practice together. b) You mustn't be nervous.", "a) We could practice together.", "Could ofrece una idea amable.")],
    [
        ("¿Qué función cumple «Can I help you?»", "Ofrecer ayuda", "Se dice al atender a un cliente."),
        ("¿Para qué sirve «so» en una explicación?", "Para unir una causa con su efecto", "Une la razón y la consecuencia."),
        ("¿Qué expresa «I'll take it»?", "Que decido comprar algo", "Se usa al decidir una compra."),
    ],
    task("Representa con una persona de tu casa una compra de mochila escolar. Escribe seis frases en inglés: ofrecer ayuda, decir lo que necesitas, describir con these o those, preguntar el precio, decir una regla con must o mustn't y explicar una causa con because o so. Léelas como un diálogo.", "Can I help you? I need a backpack. These bags are blue and those are green. How much is it? You mustn't carry too much weight. I'll take it because it is light.", ["incluye seis funciones distintas", "usa bien los tiempos y palabras de la clase", "lo representa en voz alta"], ["hoja con seis frases", "nota de la persona que participó"], ["repetir la misma función", "errores de concordancia"], "Reconoce las funciones logradas y trabaja con la persona de tu casa la función que faltó."),
    "Lee el diálogo de la tienda de deportes con una persona de tu casa, cada uno con un papel.",
    "Escribe un diálogo de ocho líneas en una panadería con una cantidad, una descripción, un precio y una causa.",
)

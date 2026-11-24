"""Inglés EPJA Nivel 2, módulo 3 (parte 1): OAD-09, informar con qué frecuencia se hacen ciertas acciones (always, usually, often, sometimes, never). Todos los textos son inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-09"

F1 = ("Texto de ejemplo, Carlos habla de su semana: «I always get up at six. I usually take the bus to work. I often eat lunch at the shop. "
      "I sometimes call my sister on Sunday. I never drink coffee at night.»")

F2 = ("Texto de ejemplo, la semana de Luis: «Luis cooks dinner every day. He walks to work on Monday and Tuesday. He cleans the house on Saturday. "
      "He calls his mother on Monday, Wednesday, Friday and Sunday. He never plays soccer, because his knee hurts.» "
      "Guía de este cuaderno: 7 de 7 días = always; 5 o 6 días = usually; 4 días = often; de 1 a 3 días = sometimes; 0 días = never.")

F3 = ("Diálogo de ejemplo. Mary: How often do you take the bus? / John: I usually take the bus, but I sometimes walk. / Mary: Does your wife take the bus? / "
      "John: No, she doesn't. She always rides a bike.")

F4 = (GUION + "Transcripción de un diálogo de ejemplo. Ana: How often does Pedro cook? / Marta: He cooks every day. He always cooks dinner. / Ana: And you? / "
      "Marta: I usually cook on weekends. I never cook on Monday, because I work late. / Ana: Do you often work late? / Marta: Yes, I often work late.")

F5 = ("Entrevista de trabajo de ejemplo. Mr. Lopez: How often do you work on Saturday? / Carlos: I sometimes work on Saturday. I usually finish at five. / "
      "Mr. Lopez: Do you arrive late? / Carlos: No, I never arrive late. I always arrive at 7:50.")

F6 = ("Texto de repaso, la semana de Rosa: «I always make breakfast for my children. I usually take them to school. I often work in the afternoon. "
      "I sometimes visit my aunt. I never go out on Monday night.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco palabras que dicen con qué frecuencia hago algo y las encuentro en un texto corto en inglés.",
    prior=["Ya cuento mi rutina en español: lo que hago siempre, a veces o nunca.", "He visto palabras en inglés en el trabajo y en la calle.", "Sé decir mi nombre y qué hago en un día normal."],
    explain=[
        "Tú ya sabes decir con qué frecuencia haces las cosas: «siempre llego temprano», «a veces camino al trabajo», «nunca tomo café de noche». En inglés se usan palabras parecidas, que se llaman adverbios de frecuencia.",
        "Las cinco más útiles para empezar son always (siempre), usually (normalmente), often (a menudo), sometimes (a veces) y never (nunca). Van antes del verbo: «I always get up at six». Todavía no hace falta saber más reglas: hoy solo vas a reconocerlas y entender su sentido.",
        "Para leer en inglés, subraya primero las palabras que ya conoces y las de frecuencia. Con eso puedes responder: ¿quién habla?, ¿qué hace?, ¿cada cuánto? Si una palabra no la conoces, sigue leyendo: casi siempre el resto de la oración te da una pista.",
    ],
    vocab=[("always", "siempre"), ("usually", "normalmente"), ("often", "a menudo"), ("sometimes", "a veces"), ("never", "nunca"), ("work", "trabajo, trabajar")],
    worked=[
        ("Leer una oración con frecuencia", "Oración de ejemplo: «Marta always walks to the market.»", ["Subrayo la palabra de frecuencia: always.", "Always significa siempre.", "Entiendo que Marta camina al mercado todas las veces, sin excepción."], "Marta siempre camina al mercado"),
        ("Distinguir dos frecuencias", "Oraciones de ejemplo: «Ana sometimes cooks» y «Ana never cooks».", ["Sometimes quiere decir a veces: cocina algunas veces.", "Never quiere decir nunca: no cocina ninguna vez.", "Comparo: la primera sí cocina, la segunda no."], "En la primera Ana cocina a veces; en la segunda, nunca"),
    ],
    mistakes=[("Creer que «often» significa «nunca» porque se parece a «off».", "Se confunde por el parecido de letras, no por el sentido.", "Aprende often junto a su ejemplo: «I often work» = trabajo a menudo."),
              ("Traducir «sometimes» como «algunas veces siempre».", "Se mezclan dos ideas de frecuencia distintas.", "Sometimes es solo «a veces»; para «siempre» se usa always.")],
    T=[
        ("abc", "{F} En la primera oración, ¿qué significa «always»?", "siempre", "nunca", "a veces", "Always indica que la acción ocurre todas las veces, sin excepción."),
        ("ab", "{F} ¿Cómo va Carlos normalmente al trabajo?", "En bus, porque dice «usually take the bus»", "A pie, porque dice «never take the bus»", "Usually significa normalmente, así que el bus es su forma habitual."),
        ("{F} ¿A qué hora se levanta Carlos siempre? Escribe solo el número.", "6", "El texto dice «I always get up at six», o sea a las seis."),
        ("abc", "{F} ¿Qué cosa no hace Carlos en ninguna ocasión?", "Tomar café en la noche", "Llamar a su hermana", "Almorzar en el local", "Never drink coffee at night significa que nunca toma café de noche."),
        ("ab", "{F} ¿Con qué frecuencia llama Carlos a su hermana?", "A veces, los domingos", "Siempre, todos los días", "Sometimes quiere decir a veces, no todos los días."),
        ("abc", "{F} ¿Cuál palabra del texto significa «a menudo»?", "often", "never", "always", "Often aparece en la oración sobre el almuerzo y quiere decir a menudo."),
        ("abc", "Marta no come carne ninguna vez. ¿Cuál oración en inglés lo dice bien?", "I never eat meat.", "I always eat meat.", "I eat never meat.", "Never va antes del verbo y significa que no come carne ninguna vez."),
        ("abc", "Ana lava la ropa todos los sábados, sin falta. Completa: Ana ___ washes her clothes on Saturday.", "always", "never", "sometimes", "Sin falta quiere decir todas las veces, y eso es always."),
        ("Ordena las palabras para formar una oración: take / I / usually / the bus.", "I usually take the bus.", "La palabra usually va antes del verbo take."),
        ("ab", "Dos personas dicen: «I sometimes cook dinner» y «I always cook dinner». ¿Quién cocina más seguido?", "La segunda, porque always es todas las veces", "La primera, porque sometimes es más fuerte", "Always significa siempre, y sometimes solo a veces."),
        ("ab", "Texto de ejemplo: «Mr. Lopez never works on Sunday.» ¿Es cierto que Mr. Lopez a veces trabaja el domingo?", "No: never significa que no trabaja ningún domingo", "Sí: never significa a veces", "Never quiere decir nunca, no «a veces»."),
        ("abc", "{F} ¿Cuál oración sería falsa según el texto?", "Carlos often drinks coffee at night.", "Carlos usually takes the bus to work.", "Carlos sometimes calls his sister.", "El texto dice que nunca toma café de noche, no a menudo."),
        ("abc", "¿Cuál de estas oraciones tiene el adverbio mal ubicado?", "I eat always breakfast.", "I always eat breakfast.", "I never eat breakfast.", "El adverbio de frecuencia va antes del verbo eat, no después."),
    ],
    ctx=("abc", "En tu trabajo te preguntan por escrito: «Do you work on Saturdays?». Tú trabajas algunos sábados, no todos. ¿Qué respondes?", "Yes, I sometimes work on Saturdays.", "No, I never work on Saturdays.", "Yes, I always work on Saturdays.", "Algunos sábados, no todos, se dice con sometimes."),
    sc=[("En Inglés: ¿qué significa «usually»?", "normalmente", "Usually describe lo que ocurre casi todas las veces."),
        ("En Inglés: ¿cuál palabra significa «nunca»?", "never", "Never indica que la acción no ocurre ninguna vez."),
        ("En Inglés: ¿dónde va la palabra «always» en «I ___ get up early»?", "Antes del verbo: I always get up early", "El adverbio de frecuencia se pone antes del verbo principal.")],
    op=("Lee otra vez {F} Di en voz alta, o escribe en papel, tres oraciones en inglés sobre ti con palabras de frecuencia (always, usually, often, sometimes o never). Usa datos de ejemplo si no quieres contar los reales.",
        "I always drink water in the morning. I sometimes walk to the store. I never eat late at night.",
        ["usa al menos tres palabras de frecuencia distintas", "pone la palabra de frecuencia antes del verbo", "las oraciones se entienden"],
        ["tres oraciones dichas o escritas"],
        ["poner la palabra de frecuencia al final", "usar never con una idea que sí hace"],
        "Pregunta: «¿Cuál de tus tres oraciones ocurre más veces en la semana?»"),
    reinforce="Escribe en un papel las cinco palabras de frecuencia con su significado y pégalo donde lo veas a diario.",
    extend="Lee un aviso o mensaje corto en inglés que encuentres y subraya cualquier palabra que ya conozcas.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy ordeno las palabras de frecuencia según cuántas veces ocurre algo y aprendo verbos de la rutina.",
    prior=["Reconozco always, often, sometimes y never.", "Sé contar los días de la semana.", "Cuento lo que hago en casa y en el trabajo."],
    explain=[
        "Las palabras de frecuencia forman una escala, de más a menos veces: always, usually, often, sometimes, never. Para no dudar, en este cuaderno usamos una guía: siete de siete días es always, cinco o seis es usually, cuatro es often, de uno a tres es sometimes y cero es never.",
        "Para hablar de tu rutina necesitas verbos de todos los días. Hoy trabajas con cook (cocinar), clean (limpiar), walk (caminar), call (llamar) y play (jugar). Con he o she, el verbo lleva -s: «he cooks», «she cleans».",
        "Al leer un texto, cuenta los días que menciona y busca la palabra que corresponde en la escala. Aparece también la expresión every day, que quiere decir todos los días: es lo mismo que always.",
    ],
    vocab=[("cook", "cocinar"), ("clean", "limpiar"), ("walk", "caminar"), ("call", "llamar por teléfono"), ("play", "jugar"), ("every day", "todos los días")],
    worked=[
        ("Elegir la palabra por el número de días", "Dato de ejemplo: Rosa limpia su pieza 4 días a la semana.", ["Cuento los días: son 4.", "Miro la guía: 4 días es often.", "Armo la oración: Rosa often cleans her room."], "Rosa often cleans her room"),
        ("Pasar de «todos los días» a una palabra", "Dato de ejemplo: Pedro camina al trabajo todos los días.", ["Todos los días es siete de siete.", "Siete de siete es always.", "Con Pedro, el verbo lleva -s: walks."], "Pedro always walks to work"),
    ],
    mistakes=[("Escribir «Luis cook dinner» con he/she.", "Se olvida la -s del verbo con he, she o it.", "Con una sola persona que no es yo ni tú: «Luis cooks»."),
              ("Poner never y además una negación: «I never don't eat».", "Never ya significa nunca; la negación se duplica.", "Usa never con verbo afirmativo: «I never eat late».")],
    T=[
        ("abc", "{F} ¿Qué palabra describe lo que Luis hace con la comida?", "always, porque cocina los siete días", "never, porque no cocina", "sometimes, porque cocina un día", "Cocina every day, o sea siete de siete días, y eso es always."),
        ("ab", "{F} ¿Con qué frecuencia llama Luis a su mamá?", "Often, porque la llama cuatro días", "Never, porque no la llama", "Cuatro días de siete se escribe often en nuestra guía."),
        ("abc", "{F} ¿Cuál es la palabra para «limpiar» en el texto?", "clean", "cook", "walk", "Luis cleans the house quiere decir que Luis limpia la casa."),
        ("abc", "{F} ¿Qué verbo del texto significa «jugar»?", "play", "call", "clean", "En «He plays soccer» el verbo play es jugar."),
        ("ab", "{F} Con las palabras de la guía, ¿cómo se dice que Luis camina al trabajo dos días?", "Luis sometimes walks to work", "Luis always walks to work", "Dos de siete días queda entre uno y tres, o sea sometimes."),
        ("{F} ¿Qué día limpia Luis la casa? Escribe el día en inglés.", "Saturday", "El texto dice «cleans the house on Saturday», o sea el sábado."),
        ("abc", "Pedro juega fútbol seis días a la semana. Según la guía, ¿qué palabra va? Pedro ___ plays soccer.", "usually", "never", "sometimes", "Seis días de siete entra en cinco o seis días, que es usually."),
        ("abc", "Ana nunca limpia el auto porque no tiene auto. Completa: Ana ___ cleans a car.", "never", "always", "often", "Cero veces en la semana se dice never."),
        ("Escribe en inglés con la guía: Marta llama a su hermana todos los días. Marta ___ calls her sister.", "always", "Todos los días es siete de siete, que se dice always."),
        ("ab", "Rosa dice «I walk to work every day». ¿Qué otra frase significa lo mismo?", "I always walk to work", "I sometimes walk to work", "Every day equivale a siete de siete, o sea always."),
        ("ab", "Una persona cocina tres días y otra seis días. ¿Cuál describe a la segunda?", "She usually cooks", "She sometimes cooks", "Seis días cae en usually; tres días es sometimes."),
        ("abc", "{F} ¿Cuál afirmación es correcta según el texto y la guía?", "Luis never plays soccer", "Luis always plays soccer", "Luis often cleans the house", "El texto dice que no juega fútbol nunca, por la rodilla."),
        ("abc", "¿Cuál oración tiene un error de -s con he?", "He cook dinner every day.", "He cooks dinner every day.", "She walks to work.", "Con he el verbo lleva -s: debería decir cooks."),
    ],
    ctx=("abc", "En un formulario de salud de ejemplo piden: «How often do you walk?». Caminas cinco días a la semana. ¿Qué respuesta usas?", "I usually walk.", "I never walk.", "I sometimes walk.", "Cinco días de siete entra en usually según la guía."),
    sc=[("En Inglés: según la guía, ¿qué palabra va con cuatro días de siete?", "often", "Cuatro días a la semana se llama often en nuestra guía."),
        ("En Inglés: ¿cómo se dice «cocinar» en inglés?", "cook", "Cook es el verbo para preparar comida."),
        ("En Inglés: ¿cuál frase quiere decir «todos los días»?", "every day", "Every day es la expresión para siete de siete días.")],
    op=("Haz una lista de ejemplo con tres cosas que una persona hace en la semana. Escribe tres oraciones en inglés con el verbo y una palabra de frecuencia, usando la guía de {F} Usa un nombre inventado.",
        "Carmen always cooks dinner. Carmen sometimes plays cards. Carmen never cleans the car.",
        ["usa tres verbos distintos", "elige la frecuencia según los días", "el verbo lleva -s con she"],
        ["tres oraciones escritas con nombre inventado"],
        ["olvidar la -s con she", "poner la palabra de frecuencia que no corresponde a los días"],
        "Pregunta: «¿Cuántos días hace cada cosa?»"),
    reinforce="Haz una tabla de cinco filas con la palabra de frecuencia y los días que le corresponden.",
    extend="Anota durante tres días lo que haces y di en inglés con qué palabra lo describirías.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo dónde va la palabra de frecuencia y cómo preguntar «How often...?» y responder.",
    prior=["Conozco always, usually, often, sometimes y never.", "Sé qué es una pregunta y una respuesta.", "Cuento mi rutina en español."],
    explain=[
        "En inglés, la palabra de frecuencia va antes del verbo principal: «I usually take the bus». Pero con el verbo to be (am, is, are) va después: «She is never late». Esta es la regla que más ayuda a escribir bien.",
        "Para preguntar cada cuánto se hace algo, se usa How often: «How often do you take the bus?». Con he, she o it se cambia do por does: «How often does she cook?». La respuesta usa una palabra de frecuencia: «She usually cooks».",
        "Para decir que no lo hace, se usa don't con I, you, we, they y doesn't con he, she, it: «She doesn't take the bus». Observa que después de does o doesn't el verbo no lleva -s: «does she take», no «does she takes».",
    ],
    vocab=[("How often", "¿cada cuánto?, ¿con qué frecuencia?"), ("do / does", "ayudante para preguntar"), ("don't / doesn't", "no (con verbos)"), ("ride", "andar en (bicicleta)"), ("but", "pero"), ("wife", "esposa")],
    worked=[
        ("Ubicar la palabra de frecuencia", "Ordena: John / take / usually / the bus.", ["Identifico el sujeto: John.", "Con un verbo común, la frecuencia va antes del verbo: usually take.", "Con John (he) el verbo lleva -s: takes."], "John usually takes the bus"),
        ("Hacer la pregunta con he/she", "Pregunta sobre Mary: cuánto cocina.", ["Empiezo con How often.", "Con Mary (she) uso does.", "El verbo queda sin -s: cook."], "How often does Mary cook?"),
    ],
    mistakes=[("Escribir «Does she takes the bus?».", "Se pone -s dos veces: en does y en el verbo.", "Después de does el verbo va sin -s: «Does she take the bus?»."),
              ("Escribir «She never is late».", "Con to be la frecuencia va después de is, no antes.", "Escribe «She is never late».")],
    T=[
        ("abc", "{F} ¿Con qué frecuencia usa John el bus?", "Usually, normalmente", "Never, nunca", "Always, siempre", "John dice «I usually take the bus», o sea normalmente."),
        ("ab", "{F} ¿Qué hace John a veces en vez de tomar el bus?", "Walks, o sea camina", "Rides a bike", "Dice «I sometimes walk», o sea que a veces camina."),
        ("abc", "{F} ¿Cómo va la esposa de John?", "En bicicleta, siempre", "En bus, siempre", "A pie, nunca", "Mary pregunta por ella y John dice «She always rides a bike»."),
        ("abc", "¿Cuál oración está bien escrita?", "She is never late.", "She never is late.", "She is late never.", "Con el verbo to be la palabra de frecuencia va después de is."),
        ("abc", "¿Cuál pregunta está bien escrita?", "How often does he cook?", "How often does he cooks?", "How often do he cook?", "Con he se usa does y el verbo vuelve a su forma simple."),
        ("Ordena las palabras: often / work / I / on Saturday.", "I often work on Saturday.", "Often va antes del verbo work, después del sujeto I."),
        ("abc", "Completa con la forma correcta: How often ___ your sister call you?", "does", "do", "is", "Sister es una sola persona (she), por eso se usa does."),
        ("abc", "Completa: My brother doesn't ___ coffee.", "drink", "drinks", "drinking", "Después de doesn't el verbo va sin -s."),
        ("ab", "Responde la pregunta «Does your wife take the bus?» según {F}", "No, she doesn't", "Yes, she does", "John dice que ella siempre anda en bicicleta, entonces no toma el bus."),
        ("ab", "Una persona dice: «He sometimes plays cards». Otra dice «He never plays cards». ¿Quién dice que alguna vez juega?", "La primera, con sometimes", "La segunda, con never", "Sometimes es a veces y never es nunca."),
        ("ab", "¿Cuál es la respuesta posible a «How often do you clean the kitchen?»?", "I clean it every day", "I am in the kitchen", "How often pide una frecuencia, y every day lo da."),
        ("abc", "¿Cuál oración tiene un error?", "Does she takes the bus?", "Does she take the bus?", "She doesn't take the bus.", "Después de does el verbo no lleva -s."),
        ("abc", "¿Cuál oración tiene la palabra de frecuencia mal ubicada?", "She never is late.", "She is never late.", "I never eat meat.", "Con el verbo to be la palabra de frecuencia va después de is."),
    ],
    ctx=("abc", "Tu vecina te pregunta en inglés: «How often do you take the bus?». Tú lo tomas todos los días. ¿Qué respondes?", "I always take the bus.", "I take always the bus.", "I never take the bus.", "Con un verbo común la palabra de frecuencia va antes del verbo."),
    sc=[("En Inglés: ordena las palabras: often / tired / is / He.", "He is often tired.", "Con to be la palabra de frecuencia va después de is."),
        ("En Inglés: ¿cómo se dice «¿Con qué frecuencia cocinas?»?", "How often do you cook?", "How often abre la pregunta y do acompaña a you."),
        ("En Inglés: completa «She doesn't ___ coffee».", "drink", "Después de doesn't el verbo va sin -s.")],
    op=("Imagina que una compañera te pregunta en inglés «How often do you walk to work?». Escribe o di tu respuesta en dos oraciones, y después haz tú la misma pregunta para otra persona. Usa datos de ejemplo.",
        "I usually walk to work. How often do you walk to work?",
        ["usa una palabra de frecuencia", "la ubica bien", "hace la pregunta con do o does"],
        ["dos oraciones y una pregunta dichas o escritas"],
        ["poner does con el verbo con -s", "olvidar how often"],
        "Pregunta: «¿Usaste do con you y does con he o she?»"),
    reinforce="Escribe cinco preguntas con How often y respóndelas con una palabra de frecuencia.",
    extend="Pregunta a una persona cercana, en español, con qué frecuencia hace tres cosas y escribe sus respuestas en inglés.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: escucho un diálogo (leído en voz alta) y respondo con palabras de frecuencia.",
    prior=["Ubico la palabra de frecuencia antes del verbo.", "Sé preguntar How often...?", "Puedo leer un diálogo corto."],
    explain=[
        "En esta clase practicas escuchar. Como no hay audio, otra persona lee en voz alta el guion, o lo lees tú en voz baja, despacio. Primero lee una vez completa y solo busca de qué trata. Después lee otra vez y subraya las palabras de frecuencia.",
        "Para entender un diálogo, hazte tres preguntas: ¿quiénes hablan?, ¿de qué hablan?, ¿con qué frecuencia hace cada uno lo que cuenta? Las palabras always, usually, often, sometimes y never te lo dicen.",
        "Cuando alguien pregunta «Do you...?», se responde con «Yes, I do» o «No, I don't». Cuando la pregunta es con he o she: «Yes, he does» o «No, he doesn't». Practica con frases cortas y completas.",
    ],
    vocab=[("weekend", "fin de semana"), ("late", "tarde"), ("work late", "trabajar hasta tarde"), ("because", "porque"), ("Yes, I do", "Sí, lo hago"), ("No, I don't", "No, no lo hago")],
    worked=[
        ("Responder la pregunta del diálogo", "Pregunta de ejemplo: «How often does Pedro cook?» (Pedro cocina todos los días).", ["Busco la frecuencia: every day es siempre.", "Pedro es he: uso cooks.", "Armo: He always cooks."], "He always cooks"),
        ("Responder sí o no", "Pregunta de ejemplo: «Do you often work late?» (alguien que trabaja tarde a menudo).", ["La pregunta es con you.", "La persona sí lo hace.", "Respondo corto: Yes, I do."], "Yes, I do"),
    ],
    mistakes=[("Responder «Yes, I does».", "Does va solo con he, she o it.", "Con I y you se usa do: «Yes, I do»."),
              ("Confundir weekend (fin de semana) con week (semana).", "Las palabras se parecen y se leen apuradas.", "Weekend es sábado y domingo; week son los siete días.")],
    T=[
        ("abc", "{F} ¿Qué hace Pedro todos los días según Marta?", "Cocina", "Limpia", "Camina", "Marta dice que Pedro cooks every day y always cooks dinner."),
        ("ab", "{F} ¿Con qué frecuencia cocina Marta los fines de semana?", "Usually", "Never", "Marta dice «I usually cook on weekends»."),
        ("abc", "{F} ¿Qué día nunca cocina Marta?", "El lunes", "El sábado", "El domingo", "Marta dice «I never cook on Monday», o sea el lunes."),
        ("abc", "{F} ¿Por qué Marta nunca cocina el lunes?", "Porque trabaja hasta tarde", "Porque está enferma", "Porque viaja", "El texto dice «because I work late», o sea porque trabaja tarde."),
        ("ab", "{F} ¿Cuál es la respuesta de Marta a «Do you often work late?»?", "Yes, I often work late", "No, I never work late", "Marta responde que sí, y que a menudo."),
        ("{F} ¿Cuántos días a la semana cocina Pedro, según el diálogo? Escribe solo el número.", "7", "Every day son los siete días de la semana."),
        ("abc", "Completa la respuesta: «Does Pedro cook?» «Yes, he ___.»", "does", "do", "is", "Con he se responde con does."),
        ("abc", "Completa la respuesta: «Do you cook on Monday?» «No, I ___.»", "don't", "doesn't", "isn't", "Con I se usa don't en la respuesta negativa."),
        ("Ordena las palabras: never / on Monday / cook / I.", "I never cook on Monday.", "Never va antes del verbo cook."),
        ("ab", "{F} Verdadero o falso: Marta always cooks.", "Falso: ella cocina usually los fines de semana y nunca el lunes", "Verdadero: ella cocina todos los días", "Marta no cocina siempre; el texto dice usually y never."),
        ("ab", "{F} Verdadero o falso: Pedro cocina todos los días.", "Verdadero, every day quiere decir todos los días", "Falso, Pedro nunca cocina", "El texto lo dice con las palabras every day."),
        ("abc", "{F} ¿Cuál oración resume mejor lo que dice Marta sobre su trabajo?", "She often works late", "She never works late", "She always works at night", "La respuesta es «Yes, I often work late»."),
        ("abc", "¿Qué respuesta es incorrecta para «Does Ana work on Sunday?»?", "Yes, she do.", "Yes, she does.", "No, she doesn't.", "Con she se usa does o doesn't, no do."),
    ],
    ctx=("abc", "Un compañero te lee: «How often do you clean the kitchen?». Lo haces dos veces a la semana. ¿Qué respuesta es mejor?", "I sometimes clean the kitchen.", "I never clean the kitchen.", "I always clean the kitchen.", "Dos veces a la semana está entre uno y tres días: sometimes."),
    sc=[("En Inglés: ¿cómo respondes con sí a «Do you work late?»?", "Yes, I do", "Con I y do se responde Yes, I do."),
        ("En Inglés: ¿cómo respondes que no a «Does he cook?»?", "No, he doesn't", "Con he se usa doesn't para decir no."),
        ("En Inglés: ¿qué significa «weekend»?", "fin de semana", "Weekend quiere decir sábado y domingo juntos.")],
    op=("Pide a otra persona que lea en voz alta {F} Luego, en tu cuaderno, escribe tres respuestas cortas: una con Pedro, una con Marta y una con tu propio ejemplo inventado.",
        "Pedro always cooks dinner. Marta never cooks on Monday. I sometimes cook rice.",
        ["una oración con Pedro", "una con Marta", "una propia con frecuencia"],
        ["tres oraciones escritas"],
        ["usar la persona equivocada", "olvidar la -s con he o she"],
        "Pregunta: «¿Qué palabras de frecuencia aparecieron en el diálogo?»"),
    reinforce="Lee el diálogo en voz baja tres veces y anota cada palabra de frecuencia que oigas.",
    extend="Inventa un diálogo de cuatro líneas con How often y respuestas con frecuencia.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una entrevista de trabajo de ejemplo y a mi propia rutina laboral.",
    prior=["Uso palabras de frecuencia bien ubicadas.", "Sé preguntar con How often.", "Sé leer un diálogo corto."],
    explain=[
        "En el trabajo se pregunta mucho por la frecuencia: ¿cuántos sábados trabajas?, ¿llegas tarde?, ¿a qué hora terminas? En una entrevista en inglés puedes responder con frases cortas y claras usando always, usually, sometimes y never.",
        "Las horas se dicen con at: «I arrive at eight», «I finish at five». Para decir 7:50 se dice seven fifty. La palabra o'clock se usa con las horas en punto: «at eight o'clock».",
        "Responde siempre con una oración completa y la palabra de frecuencia. Si no entiendes una pregunta, puedes decir «Sorry, can you repeat that, please?». Es una expresión útil: aprenderla completa te ayuda a no quedarte callado o callada.",
    ],
    vocab=[("finish", "terminar"), ("arrive", "llegar"), ("late", "tarde (hora)"), ("at five", "a las cinco"), ("Sorry, can you repeat that, please?", "Perdón, ¿puede repetir, por favor?"), ("shift", "turno")],
    worked=[
        ("Responder en la entrevista", "Pregunta: «How often do you work on Saturday?» (trabajas algunos sábados).", ["Elijo la palabra: sometimes.", "Ubico antes del verbo: sometimes work.", "Agrego el día: on Saturday."], "I sometimes work on Saturday"),
        ("Decir la hora de llegada", "Dato de ejemplo: llegas todos los días a las 7:50.", ["Todos los días es always.", "La hora con at: at 7:50.", "El verbo es arrive."], "I always arrive at 7:50"),
    ],
    mistakes=[("Decir «I arrive in eight».", "La preposición para la hora es at, no in.", "Se dice «I arrive at eight»."),
              ("Responder solo «Sometimes» a una entrevista.", "Una sola palabra parece poco clara y poco cuidada.", "Responde con la oración completa: «I sometimes work on Saturday».")],
    T=[
        ("abc", "{F} ¿Con qué frecuencia trabaja Carlos los sábados?", "Sometimes", "Always", "Never", "Carlos dice «I sometimes work on Saturday»."),
        ("ab", "{F} ¿A qué hora termina Carlos normalmente?", "A las cinco", "A las ocho", "Usually I finish at five significa que termina a las cinco."),
        ("{F} ¿A qué hora llega Carlos siempre? Escribe la hora con números, como 7:50.", "7:50", "Él dice «I always arrive at 7:50»."),
        ("abc", "{F} ¿Qué responde Carlos a la pregunta «Do you arrive late?»?", "No, I never arrive late", "Yes, I often arrive late", "Yes, I always arrive late", "Carlos dice que nunca llega tarde, con never."),
        ("ab", "{F} Verdadero o falso: Carlos trabaja todos los sábados.", "Falso: dice sometimes, o sea a veces", "Verdadero: dice always", "Sometimes no es todos los sábados."),
        ("abc", "{F} ¿Quién hace las preguntas en el diálogo?", "Mr. Lopez", "Carlos", "Mary", "Las preguntas las hace Mr. Lopez, el entrevistador."),
        ("abc", "Completa la hora: I finish ___ five.", "at", "in", "on", "Para decir la hora se usa at."),
        ("abc", "¿Cuál oración dice bien «Siempre llego a las ocho»?", "I always arrive at eight.", "I arrive always at eight.", "I always am arrive eight.", "Always va antes del verbo arrive, y la hora lleva at."),
        ("Ordena las palabras: I / on Saturday / sometimes / work.", "I sometimes work on Saturday.", "Sometimes va antes del verbo work."),
        ("ab", "Un jefe pregunta «Do you work at night?». Tú nunca trabajas de noche. ¿Qué respondes?", "No, I never work at night", "Yes, I never work at night", "Never ya es una negación; con Yes la respuesta se contradice."),
        ("ab", "Si no entiendes la pregunta, ¿qué frase es adecuada?", "Sorry, can you repeat that, please?", "I am never repeat", "Es la expresión completa para pedir que repitan."),
        ("abc", "{F} ¿Qué oración dice algo falso sobre Carlos?", "Carlos often arrives late.", "Carlos always arrives at 7:50.", "Carlos usually finishes at five.", "El texto dice que Carlos nunca llega tarde."),
        ("abc", "¿Cuál oración tiene un error?", "She arrive at nine every day.", "She arrives at nine every day.", "We arrive at nine.", "Con she el verbo debe llevar -s: arrives."),
    ],
    ctx=("abc", "En una entrevista de ejemplo te preguntan: «How often do you work on Sunday?». Tú nunca trabajas los domingos. ¿Qué respondes?", "I never work on Sunday.", "I always work on Sunday.", "I work never on Sunday.", "Never va antes del verbo para decir que no ocurre ninguna vez."),
    sc=[("En Inglés: ¿cómo dices «a las seis» en inglés?", "at six", "Para la hora se usa la preposición at."),
        ("En Inglés: ¿qué significa «shift»?", "turno", "Shift es el turno de trabajo."),
        ("En Inglés: ¿cómo pides que repitan?", "Sorry, can you repeat that, please?", "Es la expresión completa para pedir que repitan.")],
    op=("Imagina una entrevista de trabajo de ejemplo con Mr. Lopez. Escribe tus respuestas en inglés a estas dos preguntas, como en {F} «How often do you work on Saturday?» y «When do you finish?». Usa datos inventados.",
        "I usually work on Saturday. I finish at six.",
        ["responde las dos preguntas", "usa una palabra de frecuencia", "usa at con la hora"],
        ["dos respuestas escritas o dichas"],
        ["no usar la hora con at", "responder con una sola palabra"],
        "Pregunta: «¿Tu respuesta es una oración completa?»"),
    reinforce="Practica en voz alta, tres veces, la frase «I always arrive at…» con una hora de ejemplo.",
    extend="Escribe cuatro oraciones sobre tu rutina laboral real, sin dar datos que no quieras compartir.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado sobre frecuencia, me autoevalúo y decido qué practicar después.",
    prior=["Uso always, usually, often, sometimes y never.", "Sé preguntar How often...?", "Respondo con oraciones completas."],
    explain=[
        "Hoy revisas todo lo del desempeño. Lo que ya puedes hacer: reconocer las cinco palabras de frecuencia, ubicarlas antes del verbo (y después de to be), preguntar con How often, responder con sí o no y decir la hora con at.",
        "También sabes que con he, she o it el verbo lleva -s, y que después de does o doesn't el verbo vuelve a su forma simple. Estas ideas son la base para hablar de tus rutinas.",
        "Para decidir qué seguir practicando, mira qué errores repites: ¿olvidas la -s?, ¿pones la palabra de frecuencia al final?, ¿confundes sometimes con always? Elige uno y practícalo diez minutos al día esta semana; con poco y seguido se aprende bien.",
    ],
    vocab=[("week", "semana"), ("visit", "visitar"), ("children", "hijos, niños"), ("make breakfast", "preparar el desayuno"), ("go out", "salir"), ("school", "colegio")],
    worked=[
        ("Revisar un texto y detectar el error", "Oración de ejemplo: «She always is happy».", ["Veo el verbo to be: is.", "Con to be la frecuencia va después.", "Corrijo: is always."], "She is always happy"),
        ("Contar la frecuencia en un texto", "Texto de ejemplo: «I visit my aunt on Sunday and on Wednesday».", ["Cuento: dos días de siete.", "Dos días es sometimes.", "Armo la oración."], "I sometimes visit my aunt"),
    ],
    mistakes=[("Poner la frecuencia siempre al final.", "En español a veces va al final y se traslada al inglés.", "En inglés va antes del verbo común."),
              ("Olvidar la -s con he o she en la rutina de otra persona.", "Con I y you el verbo no cambia y se generaliza.", "Con he, she o it agrega -s.")],
    T=[
        ("abc", "{F} ¿Qué hace Rosa siempre?", "Prepara el desayuno de sus hijos", "Visita a su tía", "Trabaja en la tarde", "El texto dice «I always make breakfast for my children»."),
        ("ab", "{F} ¿Con qué frecuencia lleva Rosa a sus hijos al colegio?", "Usually, normalmente", "Never, nunca", "El texto dice «I usually take them to school»."),
        ("abc", "{F} ¿Qué noche nunca sale Rosa?", "El lunes", "El viernes", "El domingo", "El texto dice «I never go out on Monday night»."),
        ("abc", "{F} ¿Cuál palabra del texto significa «a veces»?", "sometimes", "often", "usually", "Sometimes aparece en «I sometimes visit my aunt»."),
        ("ab", "{F} ¿Qué hace Rosa a menudo en la tarde?", "Trabaja", "Duerme", "Often work in the afternoon significa que trabaja a menudo en la tarde."),
        ("{F} ¿A quién visita Rosa a veces? Responde en español.", "A su tía", "El texto dice «I sometimes visit my aunt»."),
        ("abc", "Escribe bien: Marta come arroz todos los días. Marta ___ eats rice.", "always", "never", "sometimes", "Todos los días es siete de siete, y eso es always."),
        ("abc", "Elige la oración correcta.", "He usually walks to work.", "He usually walk to work.", "He walks usually to work.", "Con he el verbo lleva -s y la frecuencia va antes."),
        ("Ordena las palabras: never / is / late / Mr. Lopez.", "Mr. Lopez is never late.", "Con to be la frecuencia va después de is."),
        ("ab", "Una persona dice «I sometimes work on Monday» y otra «I often work on Monday». ¿Quién trabaja más lunes?", "La segunda, con often", "La primera, con sometimes", "Often es más veces que sometimes."),
        ("ab", "Verdadero o falso razonado: «Does she works?» está bien escrita.", "Falso: después de does el verbo va sin -s", "Verdadero: con she va -s", "Does ya lleva la -s; el verbo queda works → work."),
        ("abc", "¿Cuál de estas oraciones tiene dos errores?", "She always are late.", "She is always late.", "She is never late.", "Con she se usa is, y con to be la frecuencia va después."),
        ("abc", "¿Cuál pregunta es correcta para saber cuántas veces cocina tu amigo?", "How often does he cook?", "How often he cooks?", "How does he often cook?", "How often abre la pregunta y does acompaña a he."),
    ],
    ctx=("abc", "Un compañero de curso te escribe: «How often do you study English?». Estudias dos veces a la semana. ¿Qué respondes?", "I sometimes study English.", "I always study English.", "I never study English.", "Dos veces a la semana cae en sometimes."),
    sc=[("En Inglés: con to be, ¿dónde va «never»: antes o después de is?", "Después de is: She is never late", "Con to be la palabra va después del verbo."),
        ("En Inglés: ¿cómo cambias «cook» con she?", "cooks", "Con she se agrega -s al verbo."),
        ("En Inglés: ¿cómo preguntas con frecuencia sobre he?", "How often does he...?", "Does acompaña a he, she o it.")],
    op=("Autoevaluación escrita u oral. Con {F} como modelo, cuenta tu semana en cuatro oraciones y escribe una frase sobre qué quieres practicar. Usa datos de ejemplo si prefieres.",
        "I always get up at six. I usually cook dinner. I sometimes visit a friend. I never work on Sunday. Next, I practice the -s with he and she.",
        ["usa cuatro palabras de frecuencia distintas", "las ubica bien", "dice qué practicar"],
        ["cuatro oraciones y una frase de siguiente paso"],
        ["repetir la misma frecuencia", "olvidar la frase de siguiente paso"],
        "Pregunta: «¿Qué error vas a revisar primero?»"),
    reinforce="Elige el error que más repites y escribe tres oraciones correctas sobre él.",
    extend="Prepara cinco oraciones sobre la rutina de una persona cercana, con he o she y una palabra de frecuencia.",
)

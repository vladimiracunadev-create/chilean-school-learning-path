"""Inglés EPJA Nivel 2, módulo 3 (parte 3): OAD-11, describir y preguntar por rutinas diarias propias y de otros (presente simple, horas, first/then/after that). Todos los textos son inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-11"

F1 = ("Texto de ejemplo, el día de Marta: «I wake up at six. I take a shower. I have breakfast. I go to work at seven thirty. I come home at six in the evening.»")

F2 = ("Texto de ejemplo, el día de Carlos: «Carlos wakes up at five thirty. He takes a shower and has breakfast. He goes to work at seven. "
      "He has lunch at noon. He comes home at five. He cooks dinner at six and goes to bed at ten.»")

F3 = ("Texto de ejemplo, el día de Ana: «Ana wakes up at six. First, she takes a shower. Then she has breakfast. After that, she goes to the market. "
      "She doesn't work in the afternoon. Does she cook dinner? Yes, she does.»")

F4 = (GUION + "Transcripción de un diálogo de ejemplo. Mary: What time do you wake up, John? / John: I wake up at five. / Mary: Do you have breakfast at home? / "
      "John: No, I don't. I have breakfast at work. / Mary: What time does your wife go to work? / John: She goes to work at eight. She doesn't wake up early.")

F5 = ("Rutina de trabajo de ejemplo, la panadería de Mr. Lopez: «First, Mr. Lopez opens the shop at six. Then he makes the bread. After that, "
      "he sells bread from eight to noon. At one he has lunch. He closes the shop at seven.»")

F6 = ("Texto de repaso, el día de Rosa: «I wake up at five thirty. First, I make breakfast for my children. Then I take them to school. "
      "After that, I go to work. I come home at six. My husband doesn't cook, so I cook dinner.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco, en un texto corto, las acciones de un día normal y las horas en que ocurren.",
    prior=["Cuento mi día en español: me levanto, desayuno, voy al trabajo.", "Sé decir algunas horas, como las seis o las ocho.", "Reconozco los verbos de la vida diaria."],
    explain=[
        "Tu día tiene una rutina: te despiertas, te bañas, desayunas, vas al trabajo y vuelves a casa. En inglés, estas acciones se dicen con verbos de uso diario, en presente simple: «I wake up», «I take a shower», «I have breakfast», «I go to work».",
        "Fíjate en que «take a shower» y «have breakfast» no se traducen palabra por palabra: take a shower quiere decir bañarse con ducha, y have breakfast, desayunar. Son expresiones completas y conviene aprenderlas así.",
        "Para decir la hora se usa at: «at six», «at seven thirty». «Thirty» quiere decir treinta, o sea y media. Al leer un texto sobre una rutina, subraya cada verbo y cada hora. Así sabes qué hace la persona y cuándo.",
    ],
    vocab=[("wake up", "despertarse"), ("take a shower", "ducharse"), ("have breakfast", "desayunar"), ("go to work", "ir al trabajo"), ("come home", "volver a casa"), ("at six", "a las seis"), ("in the evening", "en la tarde-noche")],
    worked=[
        ("Leer una acción con hora", "Oración de ejemplo: «I go to work at seven thirty.»", ["Subrayo el verbo: go to work.", "Subrayo la hora: at seven thirty.", "Thirty es treinta: son las siete y media."], "Voy al trabajo a las siete y media"),
        ("Ordenar dos acciones", "Texto de ejemplo: «I wake up at six. I have breakfast.»", ["Primero ocurre wake up.", "Después ocurre have breakfast.", "Las horas me ayudan a ordenar."], "Primero se despierta y después desayuna"),
    ],
    mistakes=[("Traducir «have breakfast» como «tener desayuno».", "Se traduce palabra por palabra.", "En inglés se dice «have breakfast» y quiere decir desayunar."),
              ("Decir «I go at work».", "Para ir al trabajo se dice go to work.", "Se dice «I go to work»; para la hora, at.")],
    T=[
        ("abc", "{F} ¿A qué hora se despierta Marta?", "A las seis", "A las siete", "A las cinco", "El texto dice «I wake up at six»."),
        ("ab", "{F} ¿Qué hace Marta después de despertarse?", "Se ducha", "Se va a trabajar", "El texto sigue con «I take a shower»."),
        ("abc", "{F} ¿Qué significa «have breakfast»?", "desayunar", "almorzar", "cenar", "Breakfast es el desayuno y have se usa para comer."),
        ("abc", "{F} ¿A qué hora va Marta al trabajo?", "A las siete y media", "A las seis", "A las ocho", "El texto dice at seven thirty, o sea a las siete y media."),
        ("abc", "{F} ¿Cuándo vuelve Marta a casa?", "A las seis de la tarde", "A las seis de la mañana", "A las siete", "El texto dice at six in the evening."),
        ("{F} ¿Qué verbo en inglés significa «despertarse»? Escribe las dos palabras.", "wake up", "El texto usa wake up para decir que se despierta."),
        ("abc", "Completa: I ___ a shower at seven.", "take", "make", "put", "La expresión para ducharse es take a shower."),
        ("abc", "Elige la oración correcta para «Voy al trabajo».", "I go to work.", "I go at work.", "I am go work.", "La expresión completa es go to work."),
        ("Ordena las palabras (empieza con I): at / I / six / up / wake.", "I wake up at six.", "La estructura es sujeto, verbo, up y la hora con at."),
        ("ab", "¿Qué hora es «seven thirty»?", "7:30", "7:13", "Thirty es treinta, o sea y media."),
        ("ab", "Verdadero o falso razonado: «come home» significa «salir de casa».", "Falso: significa volver a casa", "Verdadero: significa salir", "Come home es llegar a casa, no salir."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Marta wakes up at seven.", "Marta takes a shower.", "Marta goes to work at seven thirty.", "El texto dice que se despierta a las seis, no a las siete."),
        ("abc", "¿Cuál oración tiene un error?", "I take shower at six.", "I take a shower at six.", "I have breakfast at seven.", "Falta el artículo a en take a shower."),
    ],
    ctx=("abc", "En una ficha de ejemplo de un curso de capacitación piden: «Write your morning routine». Te levantas a las seis y desayunas. ¿Qué escribes?", "I wake up at six. I have breakfast.", "I wake up at six. I breakfast have.", "I am wake up at six.", "Se usan los verbos wake up y have con la hora y el orden correcto."),
    sc=[("En Inglés: ¿cómo se dice «ducharse»?", "take a shower", "La expresión completa es take a shower."),
        ("En Inglés: ¿qué significa «go to work»?", "ir al trabajo", "Es la expresión para ir al lugar de trabajo."),
        ("En Inglés: ¿cómo se dice «a las seis»?", "at six", "Para la hora se usa at más el número.")],
    op=("Con {F} como modelo, escribe o di cuatro oraciones sobre tu mañana (reales o de ejemplo), con acciones y horas. Evita datos que no quieras compartir.",
        "I wake up at six. I take a shower. I have breakfast at seven. I go to work at eight.",
        ["cuatro acciones distintas", "usa horas con at", "los verbos van bien"],
        ["cuatro oraciones dichas o escritas"],
        ["olvidar at antes de la hora", "traducir palabra por palabra"],
        "Pregunta: «¿Qué haces primero en tu mañana?»"),
    reinforce="Escribe en tarjetas los siete verbos de la clase con su significado.",
    extend="Anota tu rutina de ayer en español y trata de decir tres acciones en inglés.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo más verbos de la rutina y cómo hablar de otra persona, con he y she.",
    prior=["Reconozco wake up, take a shower, have breakfast y go to work.", "Digo horas con at.", "Sé leer un texto breve."],
    explain=[
        "Para hablar de la rutina de otra persona, el verbo cambia: con he o she se agrega -s. Así, «I wake up» pasa a «he wakes up», y «I take» pasa a «she takes». Esta es la -s de la tercera persona, y es muy importante en inglés.",
        "Dos verbos son especiales: «go» se transforma en «goes» (he goes) y «have» en «has» (she has). Son irregulares y conviene aprenderlos de memoria. Nuevos verbos de la clase: cook (cocinar), come (venir, llegar), go to bed (acostarse).",
        "Al leer, subraya cada verbo con -s y cada hora. Si el texto habla de Carlos, entiende que he es Carlos. Además hoy aparece «noon», que quiere decir mediodía, y «at ten», que quiere decir a las diez.",
    ],
    vocab=[("cook dinner", "preparar la cena"), ("go to bed", "acostarse"), ("noon", "mediodía"), ("he wakes up", "él se despierta"), ("she has", "ella tiene, ella toma"), ("he goes", "él va")],
    worked=[
        ("Pasar de I a he", "Oración de ejemplo: «I take a shower».", ["Con he agrego -s al verbo take.", "Queda takes.", "El resto no cambia."], "He takes a shower"),
        ("Los verbos especiales", "Oración de ejemplo: «I go to work».", ["Con he, go cambia a goes.", "Escribo goes y no «gos».", "Queda la oración completa."], "He goes to work"),
    ],
    mistakes=[("Escribir «He wake up at five».", "Se olvida la -s con he.", "Escribe «He wakes up at five»."),
              ("Escribir «She haves breakfast».", "Have es irregular y se transforma en has.", "Escribe «She has breakfast».")],
    T=[
        ("abc", "{F} ¿A qué hora se despierta Carlos?", "A las cinco y media", "A las seis", "A las siete", "El texto dice «Carlos wakes up at five thirty»."),
        ("ab", "{F} ¿A qué hora va Carlos al trabajo?", "A las siete", "A las cinco", "El texto dice «He goes to work at seven»."),
        ("abc", "{F} ¿Qué hace Carlos al mediodía?", "Almuerza", "Duerme", "Cocina", "El texto dice «He has lunch at noon»."),
        ("abc", "{F} ¿A qué hora se acuesta Carlos?", "A las diez", "A las seis", "A las cinco", "El texto dice «goes to bed at ten»."),
        ("abc", "{F} ¿Qué hace Carlos a las seis?", "Cocina la cena", "Se despierta", "Va al trabajo", "El texto dice «He cooks dinner at six»."),
        ("{F} ¿A qué hora vuelve Carlos a casa? Escribe solo el número.", "5", "El texto dice «He comes home at five»."),
        ("abc", "Completa: She ___ breakfast at seven.", "has", "have", "haves", "Con she el verbo have se transforma en has."),
        ("abc", "Completa: My brother ___ to work by bus.", "goes", "go", "gos", "Con he o un solo hombre el verbo go se escribe goes."),
        ("Escribe en inglés con he: «Él cocina la cena a las seis.» Empieza con He.", "He cooks dinner at six.", "Con he el verbo cook lleva -s: cooks."),
        ("ab", "Verdadero o falso razonado: «She wake up at six» está bien escrita.", "Falso: falta la -s en wakes", "Verdadero: así se escribe con she", "Con she el verbo debe llevar -s."),
        ("ab", "¿Qué frase dice que una persona se levanta al mediodía?", "She wakes up at noon", "She wakes up at nine", "Noon significa mediodía, las doce del día."),
        ("abc", "{F} ¿Cuál oración es falsa?", "Carlos has lunch at noon.", "Carlos cooks dinner at six.", "Carlos goes to bed at eight.", "El texto dice que se acuesta a las diez, no a las ocho."),
        ("abc", "¿Cuál oración tiene un error?", "He have breakfast at six.", "He has breakfast at six.", "I have breakfast at six.", "Con he se usa has, no have."),
    ],
    ctx=("abc", "En un formulario de ejemplo de una oficina de ayuda familiar escribes la rutina de un hermano de ejemplo: él se levanta a las seis. ¿Qué escribes?", "He wakes up at six.", "He wake up at six.", "He wakes at up six.", "Con he el verbo lleva -s: wakes up."),
    sc=[("En Inglés: ¿cómo se escribe «ella va» en inglés?", "she goes", "Go se transforma en goes con she."),
        ("En Inglés: ¿cómo se escribe «él tiene» en inglés?", "he has", "Have se transforma en has con he."),
        ("En Inglés: ¿qué significa «noon»?", "mediodía", "Noon es las doce del día.")],
    op=("Con {F} como modelo, escribe cinco oraciones sobre el día de otra persona (un nombre de ejemplo), con verbos con -s y horas.",
        "Ana wakes up at six. She takes a shower. She has breakfast. She goes to work at eight. She comes home at five.",
        ["usa -s con he o she", "usa has y goes", "usa horas con at"],
        ["cinco oraciones escritas"],
        ["olvidar la -s", "escribir haves o gos"],
        "Pregunta: «¿Todos tus verbos con she llevan -s?»"),
    reinforce="Escribe tres oraciones con he y subraya la -s de cada verbo.",
    extend="Cuenta en inglés la rutina de una persona cercana usando los verbos de la clase.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a decir lo que no hace una persona, a preguntar por su rutina y a ordenar con first, then y after that.",
    prior=["Uso la -s con he y she.", "Digo horas con at.", "Reconozco los verbos de la rutina."],
    explain=[
        "Para ordenar acciones se usan las palabras first (primero), then (luego) y after that (después de eso). Se ponen al comienzo de la oración y llevan coma: «First, she takes a shower. Then she has breakfast.».",
        "Para decir que no hace algo se usa doesn't con he, she o it, y don't con los demás. Después de doesn't el verbo va sin -s: «She doesn't work in the afternoon». Para preguntar se usa Does: «Does she cook dinner?», y se responde «Yes, she does» o «No, she doesn't».",
        "Paso a paso: 1) escribe el sujeto; 2) agrega does o doesn't si preguntas o niegas; 3) deja el verbo simple; 4) completa con la hora o el lugar. La -s se queda en does, no en el verbo.",
    ],
    vocab=[("first", "primero"), ("then", "luego"), ("after that", "después de eso"), ("doesn't", "no (con he, she, it)"), ("Does she…?", "¿ella…?"), ("market", "feria, mercado")],
    worked=[
        ("Decir lo que no hace", "Dato de ejemplo: Ana no trabaja en la tarde.", ["Uso doesn't con Ana.", "El verbo queda simple: work.", "Agrego el momento: in the afternoon."], "Ana doesn't work in the afternoon"),
        ("Preguntar por su rutina", "Quiero preguntar si ella cocina la cena.", ["Empiezo con Does.", "Agrego she y el verbo simple cook.", "Termino con dinner."], "Does she cook dinner?"),
    ],
    mistakes=[("Escribir «She doesn't works».", "Se pone -s dos veces: en doesn't y en el verbo.", "Escribe «She doesn't work»."),
              ("Olvidar la coma después de first.", "No se separa la palabra que ordena.", "Escribe «First, she takes a shower»; la coma separa la palabra de orden.")],
    T=[
        ("abc", "{F} ¿Qué hace Ana primero?", "Se ducha", "Desayuna", "Va al mercado", "El texto dice «First, she takes a shower»."),
        ("ab", "{F} ¿Qué hace Ana después de desayunar?", "Va al mercado", "Se acuesta", "El texto dice «After that, she goes to the market»."),
        ("abc", "{F} ¿Qué dice el texto de la tarde de Ana?", "Que no trabaja", "Que trabaja", "Que viaja", "El texto dice «She doesn't work in the afternoon»."),
        ("abc", "{F} ¿Cocina Ana la cena?", "Sí, la cocina", "No, no la cocina", "No se sabe", "El texto responde «Yes, she does»."),
        ("abc", "¿Qué palabra de orden significa «luego»?", "then", "first", "never", "Then se usa para la acción que sigue a la primera."),
        ("{F} ¿A qué hora se despierta Ana? Escribe solo el número.", "6", "El texto dice que Ana wakes up at six."),
        ("abc", "Completa: She doesn't ___ in the afternoon.", "work", "works", "working", "Después de doesn't el verbo queda simple."),
        ("abc", "Elige la pregunta correcta.", "Does he cook dinner?", "Does he cooks dinner?", "Do he cook dinner?", "Con he se usa does y el verbo vuelve a su forma simple."),
        ("Ordena las palabras: then / she / breakfast / has.", "Then she has breakfast.", "Then va al comienzo y has acompaña a she."),
        ("ab", "Una persona dice «He doesn't works» y otra «He doesn't work». ¿Cuál está bien?", "He doesn't work", "He doesn't works", "Después de doesn't el verbo no lleva -s."),
        ("ab", "Verdadero o falso razonado: «Does she goes to work?» está bien escrita.", "Falso: después de does el verbo queda go", "Verdadero: con she va goes", "La -s ya está en does; el verbo queda simple."),
        ("abc", "{F} ¿Cuál afirmación es correcta?", "Ana goes to the market after breakfast.", "Ana goes to the market before the shower.", "Ana works in the afternoon.", "El orden es primero ducha, luego desayuno, después mercado."),
        ("abc", "¿Cuál oración tiene un error?", "She don't cook.", "She doesn't cook.", "They don't cook.", "Con she se usa doesn't, no don't."),
    ],
    ctx=("abc", "Una compañera de trabajo te pregunta en inglés por la rutina de un hermano de ejemplo: «Does he work at night?». Él no trabaja de noche. ¿Qué respondes?", "No, he doesn't.", "No, he don't.", "No, he isn't work.", "Con he, la respuesta negativa corta usa doesn't."),
    sc=[("En Inglés: ¿cómo se dice «Ella no trabaja»?", "She doesn't work", "Doesn't con she y el verbo simple."),
        ("En Inglés: ¿qué significa «after that»?", "después de eso", "Es una palabra de orden para la acción siguiente."),
        ("En Inglés: ¿cómo respondes sí a «Does she cook?»?", "Yes, she does", "Con does se responde con does.")],
    op=("Con {F} como modelo, escribe cuatro oraciones con first, then y after that sobre la rutina de otra persona, y una con doesn't. Usa datos de ejemplo.",
        "First, he wakes up at five. Then he takes a shower. After that, he goes to work. He doesn't have breakfast at home.",
        ["usa first, then y after that", "usa doesn't con verbo simple", "usa -s en los otros verbos"],
        ["cuatro oraciones escritas"],
        ["poner -s después de doesn't", "olvidar la coma"],
        "Pregunta: «¿Se entiende el orden de las acciones?»"),
    reinforce="Escribe tu rutina con first, then y after that, tres acciones.",
    extend="Haz tres preguntas con Does sobre la rutina de alguien de tu familia y escribe las respuestas.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: escucho un diálogo sobre rutinas y respondo preguntas con do y does.",
    prior=["Uso las formas con -s y doesn't.", "Sé preguntar What time…?", "Entiendo un diálogo breve."],
    explain=[
        "En esta clase practicas la escucha sin audio: otra persona lee el guion en voz alta, o lo lees tú en voz baja. Primero busca de qué trata y quiénes hablan. Después subraya las horas y los verbos.",
        "Aparece la pregunta «What time…?», que quiere decir ¿a qué hora…?. Con you se usa do: «What time do you wake up?». Con he o she se usa does: «What time does she go to work?». Las respuestas se arman con la hora: «I wake up at five».",
        "Otra pregunta útil es «Do you have breakfast at home?». Se responde con «Yes, I do» o «No, I don't». Con otra persona, «Yes, she does» o «No, she doesn't». Recuerda que el verbo vuelve a su forma simple después de do o does.",
    ],
    vocab=[("What time…?", "¿A qué hora…?"), ("early", "temprano"), ("at home", "en casa"), ("at work", "en el trabajo"), ("wife", "esposa"), ("Yes, I do", "Sí, lo hago")],
    worked=[
        ("Responder la hora", "Pregunta de ejemplo: «What time do you wake up?» (a las cinco).", ["Uso I wake up.", "Agrego at y la hora: at five.", "La oración queda completa."], "I wake up at five"),
        ("Responder con otra persona", "Pregunta de ejemplo: «What time does your wife go to work?» (a las ocho).", ["Con wife uso she.", "El verbo go se transforma en goes.", "Agrego la hora: at eight."], "She goes to work at eight"),
    ],
    mistakes=[("Responder «Yes, he do» a «Does he work?».", "Con he se usa does en la respuesta.", "Responde «Yes, he does»."),
              ("Decir «What time does she goes?».", "Se pone -s dos veces.", "Di «What time does she go?».")],
    T=[
        ("abc", "{F} ¿A qué hora se despierta John?", "A las cinco", "A las seis", "A las ocho", "John dice «I wake up at five»."),
        ("ab", "{F} ¿Dónde desayuna John?", "En el trabajo", "En su casa", "John dice «I have breakfast at work»."),
        ("abc", "{F} ¿A qué hora va la esposa de John al trabajo?", "A las ocho", "A las cinco", "A las siete", "John dice «She goes to work at eight»."),
        ("abc", "{F} ¿Qué dice John de su esposa y la mañana?", "Que no se levanta temprano", "Que se levanta a las cinco", "Que desayuna en el trabajo", "John dice «She doesn't wake up early»."),
        ("abc", "{F} ¿Quién pregunta en el diálogo?", "Mary", "John", "La esposa de John", "Mary hace las preguntas y John responde."),
        ("{F} ¿Cuántas horas distintas se nombran en el diálogo? Escribe el número.", "2", "Se nombran las cinco, en que se despierta John, y las ocho, en que su esposa va al trabajo."),
        ("abc", "Completa: What time ___ you wake up?", "do", "does", "are", "Con you se usa do para preguntar."),
        ("abc", "Completa: What time ___ she go to work?", "does", "do", "is", "Con she se usa does para preguntar."),
        ("Ordena las palabras (empieza con He): at / he / eight / work / goes / to.", "He goes to work at eight.", "La estructura es sujeto, goes to work y la hora con at."),
        ("ab", "Responde «Do you have breakfast at home?» para John según {F}", "No, I don't", "Yes, I do", "John desayuna en el trabajo, no en casa."),
        ("ab", "Verdadero o falso razonado: la esposa de John se levanta temprano según {F}", "Falso: John dice que no se levanta temprano", "Verdadero: se levanta a las cinco", "El guion dice She doesn't wake up early."),
        ("abc", "{F} ¿Cuál oración resume el diálogo?", "John wakes up early and has breakfast at work.", "John wakes up late and has breakfast at home.", "John's wife wakes up at five.", "John se despierta a las cinco y desayuna en el trabajo."),
        ("abc", "¿Cuál pregunta tiene un error?", "What time does she goes to work?", "What time does she go to work?", "What time do you wake up?", "Después de does el verbo queda go, sin -es."),
    ],
    ctx=("abc", "En la fila de un consultorio de ejemplo, otra persona te pregunta en inglés: «What time do you wake up?». Tú te despiertas a las siete. ¿Qué respondes?", "I wake up at seven.", "I wakes up at seven.", "I am wake up seven.", "Con I el verbo queda simple y la hora lleva at."),
    sc=[("En Inglés: ¿cómo preguntas «¿A qué hora te despiertas?»?", "What time do you wake up?", "What time y do con you forman la pregunta."),
        ("En Inglés: ¿cómo respondes que no a «Does she cook?»?", "No, she doesn't", "Con she se usa doesn't para negar la acción."),
        ("En Inglés: ¿qué significa «early»?", "temprano", "Early es lo contrario de late.")],
    op=("Pide a otra persona que lea en voz alta {F} Escribe tres respuestas sobre la rutina de John y su esposa y una pregunta tuya con What time.",
        "John wakes up at five. His wife goes to work at eight. She doesn't wake up early. What time do you go to work?",
        ["tres oraciones sobre John y su esposa", "una pregunta con What time", "usa -s con he y she"],
        ["tres oraciones y una pregunta escritas"],
        ["olvidar -s", "usar do con she"],
        "Pregunta: «¿Cuál es la diferencia entre la rutina de John y la de su esposa?»"),
    reinforce="Lee el guion tres veces y anota cada hora que escuches.",
    extend="Inventa un diálogo de cuatro líneas sobre la hora en que se despiertan dos personas.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico la rutina a una situación de trabajo: un horario y los pasos del día de una panadería de ejemplo.",
    prior=["Uso first, then y after that.", "Digo horas con at.", "Uso -s con he o she."],
    explain=[
        "En el trabajo, las rutinas se escriben en listas: horarios, turnos, pasos para abrir o cerrar un local. En inglés, un texto de rutina laboral usa verbos en presente simple y las palabras first, then y after that.",
        "Para decir un rango de tiempo se usa from… to…: «from eight to noon» quiere decir desde las ocho hasta el mediodía. Para una hora exacta se usa at: «at one» quiere decir a la una. Y «open» y «close» son abrir y cerrar.",
        "Para entender un texto laboral, subraya cada verbo con -s y cada hora. Después arma la secuencia: qué ocurre primero, qué después y qué al final. Así puedes explicar el turno de otra persona con claridad y respeto.",
    ],
    vocab=[("open", "abrir"), ("close", "cerrar"), ("make bread", "hacer pan"), ("sell", "vender"), ("from… to…", "desde… hasta…"), ("shop", "tienda")],
    worked=[
        ("Ordenar los pasos", "Texto de ejemplo: «First, he opens. Then he makes bread. After that, he sells.»", ["First: opens.", "Then: makes bread.", "After that: sells."], "Abre, hace pan y vende, en ese orden"),
        ("Decir un rango", "Dato de ejemplo: vende pan desde las ocho hasta el mediodía.", ["Uso from… to…", "La primera hora es eight.", "La segunda es noon."], "He sells bread from eight to noon"),
    ],
    mistakes=[("Escribir «from eight at noon».", "Se confunde from… to… con at.", "Escribe «from eight to noon»."),
              ("Escribir «He open the shop».", "Falta la -s con he.", "Escribe «He opens the shop».")],
    T=[
        ("abc", "{F} ¿A qué hora abre Mr. Lopez la tienda?", "A las seis", "A las ocho", "A la una", "El texto dice «opens the shop at six»."),
        ("ab", "{F} ¿Qué hace Mr. Lopez después de abrir?", "Hace el pan", "Cierra la tienda", "El texto dice «Then he makes the bread»."),
        ("abc", "{F} ¿Cuándo vende pan Mr. Lopez?", "Desde las ocho hasta el mediodía", "Desde las seis hasta las ocho", "Desde la una hasta las siete", "El texto dice «from eight to noon»."),
        ("abc", "{F} ¿Qué hace a la una?", "Almuerza", "Hace pan", "Cierra", "El texto dice «At one he has lunch»."),
        ("abc", "{F} ¿A qué hora cierra Mr. Lopez la tienda?", "A las siete", "A las seis", "A las ocho", "El texto dice «closes the shop at seven»."),
        ("{F} ¿Cuántas acciones aparecen con first, then y after that? Escribe el número.", "3", "First, Then y After that marcan tres acciones: abre, hace pan y vende."),
        ("abc", "Completa: He sells bread ___ eight to noon.", "from", "at", "in", "Para un rango se usa from… to…."),
        ("abc", "Elige la oración correcta.", "He closes the shop at seven.", "He close the shop at seven.", "He closing the shop at seven.", "Con he el verbo lleva -s."),
        ("Ordena las palabras: opens / first, / he / the shop.", "First, he opens the shop.", "First va al comienzo, con coma."),
        ("ab", "Verdadero o falso: Mr. Lopez sells bread in the morning, según {F}", "Verdadero: de ocho a mediodía", "Falso: solo vende en la noche", "El texto indica que vende desde las ocho hasta el mediodía."),
        ("ab", "¿Qué frase dice que una mujer no almuerza a la una?", "She doesn't have lunch at one", "She doesn't has lunch at one", "Doesn't lleva el verbo en su forma simple."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Mr. Lopez closes the shop at noon.", "Mr. Lopez opens the shop at six.", "Mr. Lopez has lunch at one.", "El texto dice que cierra a las siete, no al mediodía."),
        ("abc", "¿Cuál oración tiene un error?", "He sell bread from eight to noon.", "He sells bread from eight to noon.", "She sells bread from eight to noon.", "Con he el verbo debe llevar -s."),
    ],
    ctx=("abc", "En un horario de ejemplo de un restaurante ves: «Marta cooks from ten to two». ¿Qué significa?", "Marta cocina desde las diez hasta las dos.", "Marta cocina a las diez.", "Marta cocina a las dos.", "From… to… indica desde una hora hasta otra."),
    sc=[("En Inglés: ¿qué significa «from eight to noon»?", "desde las ocho hasta el mediodía", "From… to… indica un rango de tiempo."),
        ("En Inglés: ¿cómo se dice «cerrar»?", "close", "Close es cerrar, lo contrario de open."),
        ("En Inglés: ¿cómo dices «primero abre»?", "First, he opens", "First, con coma, abre la lista de pasos.")],
    op=("Con {F} como modelo, escribe la rutina de trabajo de una persona de ejemplo en cinco oraciones, con first, then, after that y al menos dos horas.",
        "First, Ana opens the office at eight. Then she answers the phone. After that, she writes reports. She has lunch at one. She closes the office at five.",
        ["usa first, then y after that", "usa -s con ella o él", "usa al menos dos horas con at"],
        ["cinco oraciones escritas"],
        ["olvidar -s", "no ordenar las acciones"],
        "Pregunta: «¿Se entiende qué hace primero y qué hace al final?»"),
    reinforce="Escribe los pasos de tu propio trabajo o de una tarea de casa con first, then y after that.",
    extend="Lee en voz alta tu texto a otra persona y pídele que te diga el orden de las acciones.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado sobre rutinas, me autoevalúo y decido qué seguir practicando.",
    prior=["Describo mi rutina y la de otra persona.", "Uso doesn't y Does.", "Ordeno acciones con first, then y after that."],
    explain=[
        "En este desempeño aprendiste a describir tu rutina diaria con verbos como wake up, take a shower, have breakfast y go to work, a decir la hora con at y a ordenar acciones con first, then y after that.",
        "También aprendiste a hablar de otras personas con la -s de he y she (wakes, takes, goes, has), a negar con doesn't y a preguntar con Does y What time.",
        "Para decidir qué practicar, revisa tus errores: ¿olvidas la -s?, ¿pones -s después de does?, ¿olvidas at con la hora? Escoge uno y practícalo diez minutos al día. Contar tu rutina a otra persona, aunque sea poco a poco, te ayuda a ganar confianza.",
    ],
    vocab=[("husband", "esposo"), ("children", "hijos"), ("school", "colegio"), ("so", "por eso"), ("in the evening", "en la tarde-noche"), ("make breakfast", "preparar el desayuno")],
    worked=[
        ("Corregir una oración", "Oración de ejemplo: «She doesn't works at night».", ["Veo doesn't.", "Después de doesn't el verbo va simple.", "Corrijo works por work."], "She doesn't work at night"),
        ("Unir acciones con first y then", "Dato de ejemplo, en primera persona: preparo el desayuno y luego llevo a los niños al colegio.", ["Primero: First, I make breakfast.", "Luego: Then I take the children to school.", "Mantengo los verbos con I simples."], "First, I make breakfast. Then I take the children to school"),
    ],
    mistakes=[("Poner -s con I: «I wakes up».", "Se generaliza la -s a todas las personas.", "La -s va solo con he, she e it."),
              ("Decir «He don't cook».", "Con he se usa doesn't.", "Di «He doesn't cook».")],
    T=[
        ("abc", "{F} ¿A qué hora se despierta Rosa?", "A las cinco y media", "A las seis", "A las siete", "El texto dice «I wake up at five thirty»."),
        ("ab", "{F} ¿Qué hace Rosa primero?", "Prepara el desayuno de sus hijos", "Va al trabajo", "El texto dice «First, I make breakfast for my children»."),
        ("abc", "{F} ¿Qué hace Rosa después de llevar a sus hijos al colegio?", "Va al trabajo", "Cocina", "Duerme", "El texto dice «After that, I go to work»."),
        ("abc", "{F} ¿Quién no cocina?", "El esposo de Rosa", "Rosa", "Sus hijos", "El texto dice «My husband doesn't cook»."),
        ("abc", "{F} ¿Por qué cocina Rosa la cena?", "Porque su esposo no cocina", "Porque tiene tiempo", "Porque le gusta", "El texto dice «so I cook dinner»."),
        ("{F} ¿A qué hora vuelve Rosa a su casa? Escribe solo el número.", "6", "El texto dice «I come home at six»."),
        ("abc", "Completa: My husband ___ cook.", "doesn't", "don't", "isn't", "Con husband (he) se usa doesn't."),
        ("abc", "Elige la oración correcta.", "She wakes up at six.", "She wake up at six.", "She wakes at up six.", "Con she el verbo lleva -s y la hora va con at."),
        ("Ordena las palabras: first, / breakfast / I / make.", "First, I make breakfast.", "First va al comienzo, con coma."),
        ("ab", "¿Cuál oración habla de lo que hace otra persona?", "He goes to work at seven", "I go to work at seven", "Goes lleva -es porque habla de él."),
        ("ab", "Verdadero o falso razonado: «Does she goes to work?» está bien.", "Falso: después de does, go sin -es", "Verdadero: con she va goes", "Con does el verbo queda en su forma simple."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Rosa wakes up at seven.", "Rosa takes her children to school.", "Rosa's husband doesn't cook.", "El texto dice que se despierta a las cinco y media, no a las siete."),
        ("abc", "¿Cuál oración tiene dos errores?", "She don't goes to work.", "She doesn't go to work.", "I don't go to work.", "Con she se usa doesn't, y después va el verbo simple."),
    ],
    ctx=("abc", "En una charla de ejemplo de un centro comunitario cuentas en inglés qué hace una vecina de ejemplo en la mañana: se despierta temprano y prepara el desayuno. ¿Qué dices?", "She wakes up early and makes breakfast.", "She wake up early and make breakfast.", "She is wake up early.", "Con she los dos verbos llevan -s."),
    sc=[("En Inglés: ¿cómo dices «él no trabaja»?", "He doesn't work", "Doesn't con he y el verbo simple."),
        ("En Inglés: ¿cómo preguntas «¿A qué hora ella va al trabajo?»?", "What time does she go to work?", "What time y does con she, y el verbo simple."),
        ("En Inglés: ¿qué palabra de orden significa «luego»?", "then", "Then marca la acción que sigue.")],
    op=("Autoevaluación oral o escrita. Con {F} como modelo, cuenta tu rutina de la mañana en cuatro oraciones y la de otra persona en tres, y escribe qué quieres practicar.",
        "I wake up at six. First, I take a shower. Then I have breakfast. I go to work at seven. My brother wakes up at eight. He doesn't take a shower in the morning. He goes to school at nine. Next, I practice the -s.",
        ["cuatro oraciones sobre ti", "tres oraciones sobre otra persona con -s", "dice qué practicar"],
        ["siete oraciones y una frase de siguiente paso"],
        ["olvidar la -s", "no decir qué practicar"],
        "Pregunta: «¿Cuál es la diferencia entre tu rutina y la de la otra persona?»"),
    reinforce="Elige tu error más frecuente y escribe tres oraciones correctas.",
    extend="Cuenta en inglés, a una persona cercana, el día de otra persona de tu familia.",
)

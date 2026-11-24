"""Inglés EPJA Nivel 2, módulo 1 (parte 3): OAD-03, describir y preguntar por intereses propios y de otras personas. Todos los textos y guiones son inventados y se leen en papel."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-03"

F1 = ("Texto de ejemplo (inventado), mensaje en un grupo de vecinos: Hi! My name is Marta. I like music. I like plants, too. I love cooking. I don't like soccer. What do you like?")

F2 = ("Ficha de un club de vecinos (inventada). Activities: cooking, gardening, walking, reading, dancing, music. Monday: cooking. Wednesday: gardening and plants. Friday: music and dancing. Saturday: a walk in the park.")

F3 = ("Texto de ejemplo (inventado) sobre un compañero: Pedro is my neighbor. He likes soccer, but he doesn't like cooking. Rosa is his sister. She likes plants. She doesn't like soccer. They both love music.")

F4 = ("Entrevista de ejemplo (inventada) en una clase: Ana: Do you like soccer, Luis? / Luis: No, I don't. I like walking. / Ana: Does your brother like walking? / "
      "Luis: Yes, he does. He enjoys walking in the park. / Ana: Do your neighbors like music? / Luis: Yes, they do.")

F5 = ("Cartel de ejemplo (inventado) de un centro comunitario: Community Club. Do you like music? Do you enjoy plants? Come on Thursday at six o'clock. We have two groups. "
      "Group 1: music and dancing. Group 2: gardening and plants. It is free. Welcome!")

F6 = ("Texto de ejemplo (inventado), perfil de un compañero: Carlos is my classmate. He likes soccer, and he loves cooking. He doesn't like dancing. Does he enjoy music? Yes, he does. "
      "He enjoys music at home. Do you like cooking, too?")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy digo qué cosas me gustan y cuáles no, y reconozco el propósito de un mensaje corto.",
    prior=["Me presento y digo mis datos.", "Uso el verbo to be.", "Sé decir en español lo que me gusta."],
    explain=[
        "Para decir que algo te gusta usa I like y la cosa: I like music. Para decir que te gusta mucho usa I love: I love cooking. Para decir que no te gusta usa I don't like: I don't like soccer. Soccer es el fútbol en inglés de Estados Unidos.",
        "Después de like o love puedes poner un sustantivo (music, plants) o una actividad con -ing (cooking, walking). Al final de una oración, too significa también: I like plants, too. Para preguntar a otra persona di What do you like?",
        "Al leer un mensaje, primero pregúntate para qué sirve: ¿presentar a alguien?, ¿invitar?, ¿avisar? En este mensaje Marta se presenta y pregunta qué les gusta a los demás. Subraya las palabras clave y las ideas generales.",
    ],
    vocab=[("like", "gustar"), ("love", "encantar, amar"), ("don't like", "no gustar"), ("music", "música"), ("plants", "plantas"), ("cooking", "cocinar, la cocina"), ("soccer", "fútbol"), ("too", "también (al final de la oración)")],
    worked=[
        ("Decir un gusto", "Te gusta la música y no te gusta el fútbol. ¿Cómo lo dices?", ["Para un gusto uso I like: I like music.", "Para lo que no me gusta uso I don't like.", "Junto las dos oraciones."], "I like music. I don't like soccer."),
        ("Reconocer el propósito", "Un mensaje dice: «Hi! I'm Pedro. I like walking. What do you like?» ¿Para qué sirve?", ["Pedro se presenta con su nombre.", "Dice un gusto: I like walking.", "Pregunta What do you like? para conocer los gustos de los demás."], "Para presentarse y preguntar por los gustos"),
    ],
    mistakes=[("Decir «I no like soccer».", "Se traduce no gusto como en español.", "En inglés se usa don't: I don't like soccer."),
              ("Decir «I am like music».", "Se confunde el verbo to be con el verbo like.", "Di directamente I like music, sin am.")],
    T=[
        ("abc", "{F} ¿Qué le gusta a Marta?", "La música y las plantas", "El fútbol y la lectura", "La pesca y la danza", "Marta dice I like music y I like plants, too."),
        ("abc", "{F} ¿Qué actividad ama Marta?", "Cocinar", "Bailar", "Correr", "Marta dice I love cooking, que significa me encanta cocinar."),
        ("abc", "{F} ¿Qué deporte no le gusta a Marta?", "El fútbol (soccer)", "El tenis", "La natación", "Marta dice I don't like soccer, es decir, no me gusta el fútbol."),
        ("abc", "{F} ¿Para qué sirve el mensaje?", "Presentarse y preguntar qué les gusta a los demás", "Vender plantas", "Avisar un corte de luz", "Marta se presenta y termina con What do you like?"),
        ("abc", "¿Cómo se dice «me gusta la música»?", "I like music.", "I am like music.", "Me like music.", "Para un gusto se usa I like y la cosa que gusta."),
        ("abc", "¿Cómo se dice «no me gusta el fútbol»?", "I don't like soccer.", "I no like soccer.", "I not like soccer.", "La negación del verbo like se hace con don't."),
        ("ab", "¿Cómo se dice «me encanta cocinar»?", "I love cooking.", "I am love cooking.", "Love es el verbo; no necesita am."),
        ("abc", "Completa: «I ___ plants.» (me gustan las plantas)", "like", "am like", "likes", "Con I el verbo like no lleva s ni am."),
        ("Ordena las palabras: like / I / music", "I like music.", "El orden es sujeto, verbo y lo que gusta."),
        ("abc", "En «I like plants, too», ¿qué significa too?", "También", "Demasiado", "Dos", "Aquí too va al final y significa también."),
        ("abc", "¿Qué palabra expresa que algo te gusta mucho?", "love", "don't", "too", "Love expresa un gusto fuerte, como me encanta."),
        ("ab", "Alguien te pregunta «What do you like?». ¿Cuál es una respuesta posible?", "I like walking.", "I'm from Chile.", "What pregunta por gustos, no por el país."),
        ("abc", "{F} ¿Qué oración contradice el mensaje?", "Marta likes soccer.", "Marta loves cooking.", "Marta likes plants.", "Marta dice I don't like soccer, así que la primera es falsa."),
    ],
    ctx=("abc", "En una reunión de vecinos de ejemplo te preguntan «What do you like?». Te gusta la jardinería y no te gusta correr. ¿Qué respondes?", "I like gardening. I don't like running.", "I like gardening. I no like running.", "I'm gardening. I don't running.", "La respuesta usa I like y I don't like con las actividades con -ing."),
    sc=[("abc", "En Inglés: ¿cómo se dice «me gusta cocinar»?", "I like cooking.", "I am like cooking.", "I likes cooking.", "Con I el verbo like va sin s y sin am."),
        ("abc", "En Inglés: ¿qué significa «I love music»?", "Me encanta la música", "No me gusta la música", "Escucho música ahora", "Love expresa un gusto muy fuerte."),
        ("abc", "En Inglés: ¿qué pregunta sirve para saber los gustos de otra persona?", "What do you like?", "Where are you from?", "How old are you?", "What do you like? pregunta por los gustos.")],
    op=("Escribe en tu cuaderno un mensaje breve de cinco líneas para un grupo de vecinos de ejemplo: tu nombre, dos cosas que te gustan, una que amas, una que no te gusta y la pregunta What do you like? Puedes leerlo en voz alta.",
        "Hi! My name is Rosa. I like music. I like plants, too. I love walking. I don't like soccer. What do you like?",
        ["dice su nombre", "usa like, love y don't like", "termina con una pregunta de gustos"],
        ["un mensaje de cinco líneas"],
        ["decir I no like", "usar am con like"],
        "Pregunta: «¿Se entiende lo que te gusta y lo que no?»; revisa don't."),
    reinforce="Di en voz baja tres cosas que te gustan y una que no te gusta, con I like y I don't like.",
    extend="Escribe una lista de seis gustos de ejemplo con like y love, y dos con don't like.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras de actividades y gustos, y uso enjoy y like con actividades con -ing.",
    prior=["Digo lo que me gusta con I like.", "Conozco los días de la semana en español.", "Uso and para unir ideas."],
    explain=[
        "Las actividades que hacemos por gusto se nombran con -ing: cooking, gardening, walking, reading, dancing. También hay sustantivos como music y plants. Después de like, love y enjoy puedes usar un sustantivo o una actividad con -ing.",
        "Enjoy significa disfrutar: I enjoy gardening. Es otra forma de decir que algo te gusta. Para unir dos gustos usa and: I like cooking and gardening. Los días se escriben con mayúscula: Monday, Wednesday, Friday, Saturday.",
        "En una ficha o cartel de actividades busca días, horas y lugares. Esas palabras clave te dicen qué se hace y cuándo. También sirve predecir: si la ficha dice Activities, esperas verbos con -ing y nombres de cosas.",
    ],
    vocab=[("cooking", "cocinar"), ("gardening", "jardinería"), ("walking", "caminar"), ("reading", "leer, la lectura"), ("dancing", "bailar"), ("music", "música"), ("enjoy", "disfrutar"), ("park", "parque")],
    worked=[
        ("Unir dos gustos", "Te gusta cocinar y la jardinería. ¿Cómo lo dices en una oración?", ["Uso I like para el gusto.", "Pongo las dos actividades con -ing.", "Las uno con and."], "I like cooking and gardening."),
        ("Usar enjoy", "Quieres decir que disfrutas caminar en el parque.", ["Uso I enjoy para disfrutar.", "Después va la actividad con -ing: walking.", "Agrego el lugar: in the park."], "I enjoy walking in the park."),
    ],
    mistakes=[("Decir «I enjoy cook».", "Se deja el verbo sin -ing después de enjoy.", "Después de enjoy usa la forma con -ing: I enjoy cooking."),
              ("Escribir los días con minúscula, como monday.", "En español los días van con minúscula.", "En inglés los días se escriben con mayúscula: Monday.")],
    T=[
        ("abc", "{F} ¿Qué día es la actividad de cocina?", "Monday", "Friday", "Saturday", "La ficha dice Monday: cooking, así que el lunes se cocina."),
        ("abc", "{F} ¿Qué se hace el miércoles?", "Jardinería y plantas", "Música y baile", "Una caminata en el parque", "La ficha dice Wednesday: gardening and plants."),
        ("{F} ¿Qué actividad se hace el viernes además de la música? Escribe la palabra en inglés.", "dancing", "La ficha dice Friday: music and dancing."),
        ("abc", "¿Qué significa gardening?", "Jardinería", "Cocina", "Lectura", "Gardening es cuidar un jardín o plantas."),
        ("abc", "¿Qué significa reading?", "Leer", "Escribir", "Caminar", "Reading es la actividad de leer."),
        ("abc", "¿Qué significa enjoy?", "Disfrutar", "Evitar", "Pagar", "Enjoy expresa que algo te da gusto."),
        ("ab", "Completa: «I enjoy ___.» (disfruto cocinar)", "cooking", "cook", "Después de enjoy va la actividad con -ing."),
        ("abc", "¿Cuál oración es correcta?", "We enjoy walking in the park.", "We enjoy walk in the park.", "We enjoying walking in the park.", "Con we el verbo enjoy va sin cambios y la actividad con -ing."),
        ("Ordena las palabras: gardening / I / love", "I love gardening.", "El orden es sujeto, verbo y la actividad."),
        ("abc", "{F} Un compañero dice: «On Saturday, we are cooking.» Según la ficha, ¿es correcto?", "No: el sábado es una caminata en el parque", "Sí: el sábado es cocina", "El sábado no hay actividad", "La ficha dice Saturday: a walk in the park."),
        ("abc", "Completa: «I like cooking ___ gardening.»", "and", "so", "to", "And une dos gustos que se suman."),
        ("abc", "{F} ¿Cuántas actividades se nombran en la lista Activities?", "6", "5", "7", "Son cooking, gardening, walking, reading, dancing y music."),
        ("abc", "Quieres decir que te gusta caminar en el parque. ¿Qué frase usas?", "I like walking in the park.", "I like walk park.", "I am like walking the park.", "Después de like va la actividad con -ing y el lugar con in the."),
    ],
    ctx=("abc", "En la sede comunitaria ves el cartel del club. Quieres decir que te gustan la jardinería y la música. ¿Qué dices?", "I like gardening and music.", "I gardening and music like.", "I'm gardening music.", "La frase correcta pone I like y une las dos actividades con and."),
    sc=[("abc", "En Inglés: ¿qué significa «I enjoy reading»?", "Disfruto leer", "Necesito leer", "No puedo leer", "La palabra enjoy significa disfrutar de algo que gusta."),
        ("abc", "En Inglés: ¿cómo se escribe correctamente el día?", "Wednesday", "wednesday", "Wensday", "Los días llevan mayúscula y se escriben Wednesday."),
        ("abc", "En Inglés: ¿cuál es correcta?", "I like cooking.", "I like cook.", "I likes cooking.", "Después de like se usa la actividad con -ing.")],
    op=("Escribe en tu cuaderno una ficha de ejemplo para un club de tu barrio con cuatro actividades y sus días de la semana, y una oración con I like, otra con I enjoy y otra con I love. Puedes leerla en voz alta.",
        "Activities: cooking, music, gardening, walking. Monday: cooking. Tuesday: music. Thursday: gardening. Sunday: walking. I like cooking. I enjoy gardening. I love music.",
        ["escribe días con mayúscula", "usa actividades con -ing", "usa like, enjoy y love"],
        ["una ficha y tres oraciones"],
        ["escribir los días con minúscula", "usar enjoy con el verbo sin -ing"],
        "Pregunta: «¿Usaste -ing después de enjoy?»; revisa las mayúsculas de los días."),
    reinforce="Di en voz baja cuatro actividades con -ing que haces en la semana.",
    extend="Escribe cinco oraciones con enjoy sobre actividades de tu barrio.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy uso el presente simple con he y she: agrego -s y niego con doesn't.",
    prior=["Digo gustos con I like.", "Conozco las personas he y she.", "Niego con don't."],
    explain=[
        "Con I, you, we y they el verbo no cambia: I like, they like. Con he y she (y it) se agrega -s: he likes, she loves, he enjoys. Esa -s final es importante cuando hablamos de otra persona.",
        "Para negar con he y she se usa doesn't y el verbo vuelve a su forma base, sin -s: She doesn't like soccer. No se dice «She doesn't likes». Con I, you, we y they se usa don't: They don't like soccer.",
        "El presente simple sirve para gustos, hábitos y datos que no cambian. En la lectura de un texto sobre otra persona busca la -s final, el nombre y las palabras clave de gusto: likes, loves, doesn't like. Así entiendes quién hace qué.",
    ],
    vocab=[("likes", "le gusta (con he, she)"), ("doesn't like", "no le gusta (con he, she)"), ("don't like", "no me gusta o no les gusta"), ("neighbor", "vecino o vecina"), ("sister", "hermana"), ("brother", "hermano"), ("both", "ambos, los dos"), ("but", "pero")],
    worked=[
        ("Agregar la -s", "Rosa loves plants. Quieres decir lo mismo de ti y de ella.", ["Con I el verbo no cambia: I love plants.", "Con she agrego -s: She loves plants.", "Reviso que la -s esté al final."], "I love plants. She loves plants."),
        ("Negar con doesn't", "A Pedro no le gusta cocinar. ¿Cómo lo dices?", ["Es él, entonces uso doesn't.", "Después de doesn't el verbo va sin -s: like.", "Agrego la actividad: cooking."], "He doesn't like cooking."),
    ],
    mistakes=[("Decir «She like music».", "Se olvida la -s con she.", "Con he y she agrega -s: She likes music."),
              ("Decir «She doesn't likes soccer».", "Se pone -s en el verbo aunque ya está doesn't.", "Después de doesn't el verbo va sin -s: She doesn't like soccer.")],
    T=[
        ("abc", "{F} ¿Qué le gusta a Pedro?", "El fútbol", "Cocinar", "Las plantas", "El texto dice He likes soccer."),
        ("abc", "{F} ¿Qué no le gusta a Pedro?", "Cocinar", "El fútbol", "La música", "El texto dice He doesn't like cooking."),
        ("{F} ¿Quién es Rosa de Pedro? Escribe una palabra en inglés.", "sister", "El texto dice Rosa is his sister."),
        ("abc", "{F} ¿A quién le gustan las plantas?", "A Rosa", "A Pedro", "A los dos", "El texto dice She likes plants hablando de Rosa."),
        ("abc", "Completa: «She ___ music.» (le gusta)", "likes", "like", "liking", "Con she el verbo lleva -s: likes."),
        ("abc", "Completa: «They ___ cooking.» (les gusta)", "like", "likes", "liking", "Con they el verbo va sin -s."),
        ("ab", "¿Cuál es la negativa de «He likes soccer»?", "He doesn't like soccer.", "He doesn't likes soccer.", "Después de doesn't el verbo vuelve a la forma base, sin -s."),
        ("abc", "¿Cuál es la negativa de «We like plants»?", "We don't like plants.", "We doesn't like plants.", "We not like plants.", "Con we la negación de like es don't."),
        ("Ordena las palabras: doesn't / like / She / soccer", "She doesn't like soccer.", "El orden es sujeto, doesn't, el verbo base y lo que no gusta."),
        ("abc", "{F} ¿Qué les gusta a Pedro y a Rosa a los dos?", "La música", "El fútbol", "Cocinar", "El texto dice They both love music."),
        ("ab", "Corrige: «Rosa don't like soccer.»", "Rosa doesn't like soccer.", "Rosa don't likes soccer.", "Con Rosa, que es ella, se usa doesn't."),
        ("abc", "¿Cuál oración es correcta?", "He enjoys walking.", "He enjoy walking.", "He enjoys walk.", "Con he el verbo lleva -s y la actividad lleva -ing."),
        ("abc", "Un compañero dice «My neighbor like music». ¿Qué le falta?", "La -s: likes", "La palabra the", "La palabra don't", "Con una sola persona, my neighbor, el verbo lleva -s."),
    ],
    ctx=("abc", "Quieres contar a un compañero que una vecina ama la jardinería, pero no le gusta cocinar. ¿Qué dices?", "My neighbor loves gardening, but she doesn't like cooking.", "My neighbor love gardening, but she don't like cooking.", "My neighbor loves gardening, but she doesn't likes cooking.", "La frase correcta pone -s en loves y usa doesn't con el verbo base."),
    sc=[("abc", "En Inglés: ¿qué se agrega al verbo con he y she?", "Una -s final", "Una -ing", "Nada", "En el presente simple he y she llevan -s en el verbo."),
        ("abc", "En Inglés: ¿qué palabra usas para negar con she?", "doesn't", "don't", "isn't", "Con he y she la negación del presente simple es doesn't."),
        ("abc", "En Inglés: ¿cuál es correcta?", "He doesn't like cooking.", "He doesn't likes cooking.", "He don't like cooking.", "Después de doesn't el verbo no lleva -s.")],
    op=("Escribe en tu cuaderno cuatro oraciones sobre los gustos de una persona cercana de ejemplo (un vecino o una hermana inventada): dos afirmativas con -s y dos negativas con doesn't. Puedes decirlas en voz alta.",
        "My neighbor likes music. He enjoys walking. He doesn't like soccer. He doesn't like cooking.",
        ["usa -s en el verbo afirmativo", "usa doesn't con el verbo base", "habla de una sola persona"],
        ["cuatro oraciones sobre una persona"],
        ["olvidar la -s", "decir doesn't likes"],
        "Pregunta: «¿Hay -s en las afirmativas y no hay -s tras doesn't?»; revisa cada verbo."),
    reinforce="Di en voz baja tres cosas que le gustan a una persona que conoces, con -s en el verbo.",
    extend="Escribe un texto de seis oraciones sobre los gustos de una persona de ejemplo, con afirmativas y negativas.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy pregunto con Do y Does por los intereses de otras personas y respondo con respuestas cortas.",
    prior=["Digo gustos propios y de otras personas.", "Agrego -s con he y she.", "Niego con don't y doesn't."],
    explain=[
        "Para preguntar por gustos en presente simple usa Do o Does al principio. Con I, you, we y they: Do you like cooking? Con he y she: Does she like music? El verbo principal va sin -s, porque does ya muestra a quien se refiere.",
        "Las respuestas cortas repiten la ayuda do o does: Yes, I do. No, I don't. Yes, he does. No, she doesn't. Así contestas sin repetir toda la oración. Para decir que algo te gusta mucho, agrega love o enjoy en tu respuesta.",
        "En una entrevista escrita, mira quién pregunta y quién responde, y subraya las respuestas cortas. Así reconoces cuándo el entrevistado dice que sí o que no. Practica hacer preguntas a personas cercanas y anotar sus respuestas.",
    ],
    vocab=[("Do you like...?", "¿Te gusta...?"), ("Does he like...?", "¿Le gusta a él...?"), ("Yes, I do.", "Sí, me gusta."), ("No, I don't.", "No, no me gusta."), ("Yes, he does.", "Sí, le gusta."), ("No, she doesn't.", "No, no le gusta."), ("neighbors", "vecinos"), ("brother", "hermano")],
    worked=[
        ("Preguntar y responder", "Quieres saber si a tu vecina le gusta la música. Pregunta y da una respuesta corta afirmativa.", ["Es ella, entonces uso Does.", "El verbo va sin -s: Does she like music?", "La respuesta corta repite does: Yes, she does."], "Does she like music? Yes, she does."),
        ("Responder en negativo", "Te preguntan: «Do you like plants?» y no te gustan.", ["Respondo con la ayuda do: No, I don't.", "Puedo agregar una frase más: I don't like plants.", "No repito la pregunta completa."], "No, I don't."),
    ],
    mistakes=[("Decir «Does she likes plants?».", "Se agrega la -s al verbo aunque ya está does.", "Después de does el verbo va sin -s: Does she like plants?"),
              ("Responder «Yes, I like» a una pregunta con Do.", "No se usa la respuesta corta.", "Responde Yes, I do. o Yes, I like plants.")],
    T=[
        ("abc", "{F} ¿A Luis le gusta el fútbol?", "No", "Sí", "No se sabe", "Luis responde No, I don't a la pregunta de Ana."),
        ("abc", "{F} ¿Qué le gusta hacer a Luis?", "Caminar", "Bailar", "Cocinar", "Luis responde y dice I like walking, me gusta caminar."),
        ("abc", "{F} ¿Dónde disfruta caminar su hermano?", "En el parque", "En el trabajo", "En la plaza", "Luis dice He enjoys walking in the park."),
        ("{F} Ana pregunta: «Do your neighbors like music?». Luis responde: Yes, they ___. Escribe la palabra que falta.", "do", "La respuesta corta con they repite la ayuda do."),
        ("abc", "¿Cuál es la pregunta para «¿Te gusta cocinar?»?", "Do you like cooking?", "Does you like cooking?", "Are you like cooking?", "Con you se usa Do y el verbo va sin -s."),
        ("abc", "¿Cuál es la pregunta para «¿Le gusta a ella la música?»?", "Does she like music?", "Do she like music?", "Does she likes music?", "Con she se usa Does y el verbo like sin -s."),
        ("ab", "¿Cuál es la respuesta corta afirmativa a «Does he like soccer?»?", "Yes, he does.", "Yes, he is.", "La respuesta repite la ayuda de la pregunta, que es does."),
        ("abc", "¿Cuál es la respuesta corta negativa a «Do you like plants?»?", "No, I don't.", "No, I'm not.", "No, I doesn't.", "La respuesta repite do con la negación: No, I don't."),
        ("Ordena las palabras para hacer una pregunta: you / Do / like / music", "Do you like music?", "La pregunta empieza con Do, sigue you y termina con el verbo y el tema."),
        ("abc", "¿Qué error hay en «Does she likes plants?»?", "Después de does el verbo no lleva -s", "Falta la palabra the", "No hay error", "La ayuda does ya indica a ella, así que el verbo queda en forma base."),
        ("ab", "{F} ¿Cuál oración es verdadera?", "Luis doesn't like soccer.", "Luis likes soccer.", "Luis dice No, I don't a la pregunta sobre el fútbol."),
        ("abc", "Quieres saber si a tu vecina le gusta la jardinería y se lo preguntas a ella directamente. ¿Qué dices?", "Do you like gardening?", "Are you like gardening?", "Does you like gardening?", "Con you se usa Do, no does ni to be."),
        ("abc", "¿Con qué personas se usa does?", "He, she e it", "I y you", "We y they", "Does acompaña a la tercera persona singular: he, she, it."),
    ],
    ctx=("abc", "Una compañera te pregunta «Do you enjoy walking?» y a ti sí te gusta. ¿Qué respondes?", "Yes, I do.", "Yes, I am.", "Yes, I walking.", "La respuesta corta repite la ayuda de la pregunta, do."),
    sc=[("abc", "En Inglés: ¿qué palabra va al inicio de la pregunta con he?", "Does", "Do", "Is", "Con he, ella o él, la pregunta empieza con Does."),
        ("abc", "En Inglés: ¿cuál es la respuesta corta para «Does she like cooking?»?", "Yes, she does.", "Yes, she likes.", "Yes, she is.", "La respuesta corta repite la ayuda does de la pregunta."),
        ("abc", "En Inglés: ¿cuál pregunta es correcta?", "Do they like music?", "Does they like music?", "Do they likes music?", "Con they se usa Do y el verbo sin -s.")],
    op=("Escribe en tu cuaderno una entrevista de seis líneas entre dos personas de ejemplo sobre sus gustos: dos preguntas con Do, una con Does y sus respuestas cortas. Puedes leerla en voz alta con otra persona.",
        "Rosa: Do you like cooking? / Pedro: Yes, I do. / Rosa: Does your sister like plants? / Pedro: Yes, she does. / Rosa: Do you like soccer? / Pedro: No, I don't.",
        ["usa Do y Does correctamente", "el verbo principal va sin -s", "las respuestas cortas repiten do o does"],
        ["una entrevista de seis líneas"],
        ["poner -s después de does", "responder sin la ayuda do"],
        "Pregunta: «¿Usaste Does con él o ella?»; revisa las respuestas cortas."),
    reinforce="Haz en voz baja tres preguntas de gustos a una persona imaginaria y responde con respuestas cortas.",
    extend="Escribe cinco preguntas de gustos para entrevistar a un vecino y las respuestas posibles.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy leo un cartel de un club comunitario, entiendo su propósito y elijo un grupo según mis intereses.",
    prior=["Pregunto por gustos con Do y Does.", "Sé qué significan like, love y enjoy.", "Reconozco palabras clave en un texto."],
    explain=[
        "Para entender un cartel, pregúntate primero: ¿para qué sirve?, ¿de qué trata?, ¿quién está invitado? Este cartel invita a un club y pregunta por los gustos: Do you like music? Do you enjoy plants? Esa es la idea general.",
        "Después busca la información práctica: el día (Thursday), la hora (six o'clock), los grupos (Group 1 y Group 2) y el costo (free). Subrayar estas palabras clave te permite responder preguntas y decidir si te sirve.",
        "Para decidir, relaciona tus gustos con la información: si te gusta bailar, eliges el grupo de music and dancing. Si disfrutas las plantas, eliges gardening and plants. En tu respuesta puedes escribir una oración corta: I like music, so I choose Group 1.",
    ],
    vocab=[("come", "venir"), ("group", "grupo"), ("free", "gratis"), ("Thursday", "jueves"), ("club", "club, asociación"), ("welcome", "bienvenido o bienvenida"), ("o'clock", "en punto"), ("so", "entonces, por eso")],
    worked=[
        ("Elegir un grupo", "Te gustan las plantas. El cartel tiene Group 1: music and dancing y Group 2: gardening and plants. ¿Qué eliges?", ["Busco la palabra clave plants.", "Está en Group 2: gardening and plants.", "Escribo una oración: I like plants, so I choose Group 2."], "Group 2"),
        ("Hallar la información práctica", "Quieres saber cuándo es la reunión y si cuesta dinero.", ["Busco el día y la hora: Thursday, six o'clock.", "Busco el costo: it is free.", "Resumo: jueves a las 6, gratis."], "El jueves a las 6, gratis"),
    ],
    mistakes=[("Traducir palabra por palabra y no buscar la idea general.", "Se detiene en cada palabra desconocida.", "Lee primero todo el cartel y subraya palabras clave como días y horas."),
              ("Leer solo el título y decidir sin leer los grupos.", "Se supone el contenido sin leerlo.", "Lee los grupos y elige según tus gustos.")],
    T=[
        ("abc", "{F} ¿Cuál es el propósito del cartel?", "Invitar a un club comunitario", "Vender plantas", "Avisar un cierre", "El cartel dice Come on Thursday y pregunta por los gustos, así que invita."),
        ("abc", "{F} ¿Qué día es la reunión?", "Thursday", "Monday", "Sunday", "El cartel dice Come on Thursday."),
        ("{F} ¿A qué hora es la reunión? Escribe solo el número.", "6", "El cartel dice at six o'clock, que es a las 6."),
        ("abc", "{F} ¿Cuánto cuesta participar?", "Nada, es gratis", "Cuesta mucho", "El cartel no dice nada", "El cartel dice It is free, es decir, es gratis."),
        ("abc", "{F} Te gusta bailar. ¿Qué grupo eliges?", "Group 1", "Group 2", "Ninguno", "El Group 1 es de music and dancing, y bailar es dancing."),
        ("abc", "{F} Disfrutas la jardinería. ¿Qué grupo eliges?", "Group 2", "Group 1", "Ninguno", "El Group 2 es de gardening and plants."),
        ("ab", "{F} ¿Qué pregunta aparece en el cartel?", "Do you like music?", "Where are you from?", "El cartel pregunta por gustos con Do you like music?"),
        ("abc", "¿Qué significa free en el cartel?", "Gratis", "Cerrado", "Lejos", "En este cartel free habla del costo y significa gratis."),
        ("abc", "¿Qué significa come?", "Venir", "Cocinar", "Esperar", "Come es venir, como en Come on Thursday."),
        ("ab", "Una persona dice: «I like music, so I choose Group 1.» ¿Es coherente con el cartel?", "Sí, porque Group 1 es música y baile", "No, porque Group 1 es jardinería", "El Group 1 tiene music and dancing, así que la elección coincide con su gusto."),
        ("Ordena las palabras: on / Come / Thursday", "Come on Thursday.", "La invitación empieza con Come, sigue on y termina con el día."),
        ("abc", "Un vecino responde: «Yes, I do. I love plants.» ¿A qué pregunta del cartel responde?", "Do you enjoy plants?", "Do you like music?", "Is it free?", "Yes, I do responde a una pregunta con Do y I love plants nombra el tema."),
        ("abc", "{F} ¿Cuál es la idea principal?", "Un club ofrece dos grupos para gustos distintos", "Un museo cierra los jueves", "Una tienda hace ofertas", "El cartel presenta el club y dos grupos según los intereses."),
    ],
    ctx=("abc", "Quieres inscribirte en el Group 1 porque te gustan la música y el baile. ¿Cuál es el mensaje correcto?", "Hello! I like music and dancing. I choose Group 1.", "Hello! I likes music and dance. I chooses Group 1.", "Hello! I'm like music. Group 1 I am.", "El mensaje correcto usa I like y I choose, sin -s con I."),
    sc=[("abc", "En Inglés: ¿qué haces primero al leer un cartel?", "Pensar para qué sirve y leerlo completo", "Traducir cada palabra", "Mirar solo el precio", "Leer el cartel completo muestra el propósito y las ideas."),
        ("abc", "En Inglés: ¿qué significa «It is free»?", "Es gratis", "Está cerrado", "Es difícil", "Free se refiere al precio, no al tiempo."),
        ("abc", "En Inglés: ¿qué palabra sirve para invitar a venir?", "Come", "Go", "Wait", "La palabra come significa venir a un lugar.")],
    op=("Escribe en tu cuaderno un cartel de ejemplo de seis líneas para invitar a un club de tu barrio: dos preguntas de gustos con Do, un día, una hora, dos grupos y la palabra free. Puedes leerlo en voz alta.",
        "Neighbors Club. Do you like walking? Do you enjoy reading? Come on Saturday at ten o'clock. Group 1: walking. Group 2: reading. It is free.",
        ["tiene preguntas con Do", "tiene un día y una hora", "describe dos grupos con gustos distintos"],
        ["un cartel de seis líneas"],
        ["no decir día ni hora", "olvidar el signo de pregunta"],
        "Pregunta: «¿Alguien sabe cuándo y a qué viene con tu cartel?»; revisa el día y la hora."),
    reinforce="Mira un cartel o aviso de tu barrio y busca cuatro palabras clave, aunque esté en español.",
    extend="Escribe un cartel de ejemplo con tres grupos para tres tipos de intereses.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso cómo hablo de mis gustos y los de otros, me autoevalúo y decido qué repasar.",
    prior=["Digo gustos con like, love y enjoy.", "Uso -s, don't y doesn't.", "Pregunto con Do y Does."],
    explain=[
        "Para revisar usa esta lista: decir gustos con I like y I love, agregar -s con he y she, negar con don't y doesn't, y preguntar con Do y Does. Marca lo que ya haces bien y lo que quieres repasar.",
        "Si algo falla, busca el motivo. ¿Olvidaste la -s con he? ¿Pusiste -s después de does? ¿Usaste to be donde no corresponde? Escribe el error y una frase correcta, y dila en voz alta.",
        "Para avanzar, usa tus gustos para conversar: pregunta a alguien Do you like...? y anota sus respuestas. Un buen siguiente paso es presentar a una persona cercana y hablar de sus gustos, tema del próximo desempeño.",
    ],
    vocab=[("likes", "le gusta"), ("loves", "le encanta"), ("enjoys", "disfruta"), ("doesn't like", "no le gusta"), ("classmate", "compañero o compañera de clase"), ("at home", "en casa"), ("Does he like...?", "¿Le gusta a él...?"), ("too", "también")],
    worked=[
        ("Revisar un texto", "Un compañero escribe: «Carlos like soccer. He don't like dancing». Corrígelo.", ["Con Carlos, él, falta la -s: likes.", "Con él la negación es doesn't: He doesn't like dancing.", "Reviso que no haya -s después de doesn't."], "Carlos likes soccer. He doesn't like dancing."),
        ("Preguntar por los gustos de otro", "Quieres saber si a Carlos le gusta la música.", ["Es él, entonces uso Does.", "El verbo va sin -s: Does he like music?", "La respuesta corta es Yes, he does o No, he doesn't."], "Does he like music?"),
    ],
    mistakes=[("Poner -s al verbo después de does.", "Se piensa que con él siempre hay -s.", "Después de does el verbo va sin -s: Does he like music?"),
              ("Responder «Yes, I like» a Do you like...?", "No se usa la respuesta corta.", "Responde Yes, I do. o Yes, I like it.")],
    T=[
        ("abc", "{F} ¿Qué le gusta a Carlos?", "El fútbol", "Bailar", "Leer", "El texto dice He likes soccer."),
        ("abc", "{F} ¿Qué le encanta a Carlos?", "Cocinar", "El fútbol", "La música", "El texto dice he loves cooking."),
        ("abc", "{F} ¿Qué actividad no le gusta a Carlos?", "Bailar", "Cocinar", "El fútbol", "El texto dice He doesn't like dancing."),
        ("ab", "{F} ¿Dónde disfruta Carlos la música?", "En su casa", "En el trabajo", "El texto dice He enjoys music at home."),
        ("abc", "{F} ¿Cuál es la respuesta a «Does he enjoy music?»", "Yes, he does.", "Yes, he is.", "Yes, I do.", "La respuesta corta repite does y habla de él."),
        ("abc", "Completa: «My brother ___ plants.» (le gustan)", "likes", "like", "liking", "Con una sola persona, my brother, el verbo lleva -s."),
        ("ab", "Corrige: «She don't like cooking.»", "She doesn't like cooking.", "She don't likes cooking.", "Con she la negación del presente simple es doesn't."),
        ("Ordena las palabras para una pregunta: she / Does / music / like", "Does she like music?", "La pregunta empieza con Does, sigue she y termina con el verbo y el tema."),
        ("abc", "¿Cuál oración es correcta?", "They enjoy walking.", "They enjoys walking.", "They enjoy walk.", "Con they el verbo no lleva -s y la actividad lleva -ing."),
        ("abc", "¿Qué responde a «Do you like plants?» alguien a quien no le gustan?", "No, I don't.", "No, I doesn't.", "No, I'm not.", "La respuesta corta negativa con I es don't."),
        ("ab", "¿Cuál oración usa bien enjoy?", "We enjoy dancing.", "We enjoy dance.", "Después de enjoy va una actividad con -ing."),
        ("abc", "Al leer un cartel sobre un club, ¿qué estrategia sirve para entenderlo?", "Subrayar días, horas y palabras clave", "Traducir cada palabra", "Leer solo el título", "Las palabras clave dan la idea general sin traducir todo."),
        ("abc", GUION + "Rosa likes plants. She doesn't like soccer. ¿Qué no le gusta a Rosa?", "El fútbol", "Las plantas", "La música", "El guion dice She doesn't like soccer."),
    ],
    ctx=("abc", "En una reunión de vecinos le preguntan a Pedro «Does your sister like music?». Su hermana ama la música. ¿Qué responde Pedro?", "Yes, she does. She loves music.", "Yes, she is. She love music.", "Yes, she do. She loves musics.", "La respuesta corta usa does y la oración extra lleva -s con she."),
    sc=[("abc", "En Inglés: ¿cuál es correcta para «le gusta la música»?", "He likes music.", "He like music.", "He liking music.", "Con he el verbo lleva -s."),
        ("abc", "En Inglés: ¿cómo preguntas si a una persona le gusta cocinar?", "Does she like cooking?", "Do she likes cooking?", "Is she like cooking?", "Con she se usa Does y el verbo sin -s."),
        ("abc", "En Inglés: ¿qué significa «I enjoy walking»?", "Disfruto caminar", "Debo caminar", "No puedo caminar", "La palabra enjoy significa disfrutar de algo que gusta.")],
    op=("Escribe en tu cuaderno un texto de ocho oraciones sobre los gustos de una persona cercana de ejemplo: tres afirmativas, dos negativas y una pregunta con Does y su respuesta corta. Después léelo en voz alta y anota qué quieres repasar.",
        "My neighbor is Rosa. She likes plants. She loves cooking. She enjoys walking. She doesn't like soccer. She doesn't like dancing. Does she like music? Yes, she does.",
        ["usa -s en las afirmativas", "usa doesn't en las negativas", "incluye una pregunta con Does y respuesta corta", "anota qué repasar"],
        ["un texto de ocho oraciones y una lista de qué repasar"],
        ["olvidar la -s", "poner -s después de doesn't"],
        "Pregunta: «¿Qué oración te salió mejor?»; revisa la -s en cada verbo."),
    reinforce="Escribe cinco oraciones sobre los gustos de personas que conoces, con -s y doesn't.",
    extend="Entrevista a tres personas (con datos de ejemplo si prefieres) con Do you like...? y escribe sus respuestas cortas.",
)

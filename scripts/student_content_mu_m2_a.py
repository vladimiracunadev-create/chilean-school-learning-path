"""Student material for 2.º medio Música, OA 01 (valoración crítica de músicas de Chile y el mundo de tradición oral, escrita y popular, con fundamentos verbales, visuales, sonoros y corporales).

Todas las músicas de los ejercicios son descripciones inventadas («de ejemplo»); no se reproducen letras ni partituras con derechos. Las audiciones reales las selecciona y pone el docente.
Este módulo define el ayudante L que usan los demás módulos mu_m2_*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "MU2M OA 01"


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1 (rasgos audibles, contexto y opinión)
L(
    OA1, 1,
    "Lápiz y papel. Las músicas están descritas con palabras en los ejercicios (son de ejemplo). Si tu docente pone una audición real, sirve para practicar la ficha.",
    "Aprenderé a describir lo que se oye en una música (rasgos audibles) y a separarlo de su contexto y de mi opinión. Sirve para que una valoración crítica de músicas de Chile y del mundo se apoye en evidencia.",
    ["Distingo tradición oral, escrita y popular (1.º medio).", "Conozco pulso, melodía, timbre, textura y forma.", "Sé que una opinión necesita una razón."],
    [
        "Valorar críticamente una música es juzgar su valor con razones, no solo decir si te gusta. El primer paso es describir lo que se oye: el pulso y el tempo (qué tan rápido avanza), la melodía (si sube, baja o se repite), el timbre (cómo suena cada voz o instrumento), la textura (cuántas capas suenan a la vez) y la forma (cómo se ordenan las partes, por ejemplo estrofa y estribillo).",
        "Conviene separar tres tipos de afirmación. Un rasgo audible se puede comprobar escuchando: «la voz canta sola, sin acompañamiento». Un dato de contexto se sabe por otras fuentes: quién la creó, para qué se usa y si es de tradición oral, escrita o popular. Una opinión expresa gusto: «me parece aburrida». La opinión no es un error, pero sola no sirve como fundamento.",
        "Las músicas de Chile y del mundo se valoran con los mismos pasos, pero cada una pide su contexto: una tonada para cantar en una reunión no tiene el mismo propósito que una sinfonía para una sala de conciertos. Por eso la calidad no se mide por el volumen, la velocidad ni la cantidad de instrumentos, sino por lo que la música logra con los recursos que usa.",
    ],
    [("tempo", "qué tan rápido avanza el pulso"), ("rasgo audible", "característica que se comprueba escuchando"), ("dato de contexto", "información sobre autor, época, uso o tradición que no se oye directamente"), ("opinión", "juicio de gusto personal, sin razones"), ("fundamento", "razón apoyada en evidencia"), ("textura", "cuántas capas o voces suenan a la vez y cómo se relacionan")],
    [
        ("Separar tres tipos de afirmación", "De una pieza de ejemplo se dicen tres frases: (1) «Una guitarra acompaña a una voz y el pulso es tranquilo.» (2) «Se canta en reuniones y se aprende de oído.» (3) «Es hermosa.» Clasifica cada una.", ["La 1 se puede comprobar escuchando.", "La 2 habla de uso y de transmisión: viene de otra fuente.", "La 3 solo expresa gusto."], "1 rasgo audible; 2 dato de contexto; 3 opinión"),
        ("Completar una ficha de escucha", "Pieza de ejemplo: una cantante sola, sin instrumentos, canta frases cortas que se repiten tres veces; en la última repetición va más lento. Describe tres rasgos audibles.", ["Textura: se oye una voz sola.", "Forma: una frase corta que se repite tres veces.", "Tempo: se hace más lento al final."], "Voz sola, frase repetida tres veces y tempo que se frena al final"),
    ],
    [
        ("Escribir «es muy buena» como si fuera una descripción.", "Es una opinión: no dice qué se oye ni permite que otra persona lo compruebe.", "Escribe primero el rasgo audible y después tu juicio, unidos por «porque»."),
        ("Decir que una pieza vale más porque suena más fuerte o más rápida.", "El volumen y la velocidad no miden la calidad; hay músicas valiosas muy suaves o muy lentas.", "Valora lo que la pieza logra con sus recursos, según su propósito."),
    ],
    [
        ex("¿Cuál de estas frases describe un rasgo audible? A) «Los violines tocan notas largas y suaves.» B) «Es la mejor música de todas.»", "A", "Se puede comprobar escuchando; la otra es una opinión."),
        ex("¿Qué tipo de afirmación es «se baila en fiestas y se aprende viendo a otras personas»? A) Rasgo audible. B) Dato de contexto.", "B", "Habla del uso y de cómo se transmite, no de lo que se oye."),
        ex("¿Qué elemento describe «dos voces cantan a la vez y una guitarra las acompaña»? A) La forma. B) La textura.", "B", "La textura indica cuántas capas suenan juntas."),
    ],
    [
        ex("Una estudiante escribe: «Es mala porque suena lenta.» ¿Por qué no es buen fundamento? A) Porque confunde calidad con velocidad y no dice qué logra la música. B) Porque las músicas lentas no se pueden valorar.", "A", "La velocidad es un rasgo, no una medida de calidad."),
        ex("¿Para qué sirve un dato de contexto en una valoración crítica? A) Para reemplazar lo que se oye. B) Para entender el propósito de la música antes de juzgarla.", "B", "El contexto ayuda a juzgar según lo que la música busca."),
        ex("Una pieza de ejemplo repite una melodía tres veces y luego presenta otra distinta. ¿Qué elemento describe esa organización? A) El timbre. B) La forma. C) El tempo.", "B", "La forma es el orden de las partes."),
    ],
    [
        ex("¿Cuántas de estas frases son rasgos audibles? (1) El tambor mantiene un pulso constante. (2) La compuso un grupo del sur de Chile. (3) Me da sueño. (4) El coro canta la misma melodía a la vez.", "2", "Son la 1 y la 4; la 2 es contexto y la 3, opinión."),
        ex("Pieza de ejemplo: una flauta sola toca una melodía que sube de a poco y luego baja. ¿Qué textura tiene? A) Una voz sola, sin acompañamiento. B) Varias capas a la vez.", "A", "Solo se oye una línea melódica."),
        ex("¿Qué frase es un dato de contexto sobre una canción de cuna de ejemplo? A) «Se canta para dormir a un bebé.» B) «Tiene un pulso suave.»", "A", "Indica el uso; la otra describe lo que se oye."),
    ],
    [
        ex("Ana dice: «Me gusta porque tiene mucho volumen.» Beto dice: «Sirve para bailar porque el pulso es marcado y el tempo se mantiene.» ¿Quién se acerca más a una valoración crítica? A) Ana. B) Beto.", "B", "Beto apoya su juicio en rasgos audibles y en el propósito."),
        ex("¿Se puede decir que una orquesta de cuarenta instrumentos es mejor que un cantor con guitarra solo por tener más instrumentos? A) Sí: más instrumentos suenan mejor. B) No: se valora lo que cada música logra con sus recursos.", "B", "La cantidad de instrumentos no mide la calidad."),
    ],
    [
        ex("Un estudiante escribe: «La pieza se aprende de memoria, así que suena improvisada.» ¿Qué error comete? A) Confunde la forma con el timbre. B) Deduce un rasgo audible a partir de un dato de contexto sin comprobarlo escuchando.", "B", "Aprenderse de memoria no implica que suene improvisada."),
        ex("¿Qué orden sigue una valoración crítica bien hecha? A) Describir lo que se oye, buscar el contexto y recién después juzgar. B) Juzgar primero, describir después y olvidar el contexto.", "A", "El juicio se apoya en descripción y contexto previos."),
    ],
    [ex("En un centro de estudiantes alguien propone: «Pongamos la pieza X en el acto porque es la más rápida». ¿Qué pregunta ayuda a pasar de opinión a fundamento? A) ¿Qué propósito tiene el acto y qué rasgos de la pieza le sirven? B) ¿Cuántos instrumentos usa?", "A", "Relaciona propósito y rasgos audibles.")],
    [
        ex("¿Qué debe cumplir un rasgo audible? A) Poder comprobarse escuchando. B) Ser dicho por una persona que conoce al autor.", "A", "Lo audible se verifica en la propia escucha."),
        ex("¿Verdadero o falso? Una opinión sola basta como fundamento de una valoración crítica.", "Falso", "Necesita rasgos y razones que la apoyen."),
        ex("¿Qué lista reúne los elementos que se describen en una ficha de escucha? A) Tempo, melodía, timbre, textura y forma. B) Autor, fecha, lugar, precio y público.", "A", "Son elementos del lenguaje musical audibles."),
    ],
    (
        "Pieza de ejemplo: un grupo de cinco personas canta una melodía con voces y bombo; el pulso es marcado, el tempo es rápido y hay dos estrofas con un estribillo que todos cantan. Se usa para animar una fiesta. Escribe: a) tres rasgos audibles, b) un dato de contexto, c) una opinión tuya separada, d) una frase de valoración que una un rasgo con el propósito.",
        "a) Voces y bombo; pulso marcado; estrofas y estribillo. b) Se usa para animar una fiesta. c) Me parece alegre. d) Funciona bien para animar la fiesta porque el pulso marcado invita a seguir el ritmo.",
        ["escribe tres rasgos que se pueden comprobar escuchando", "separa contexto y opinión", "une un rasgo con el propósito mediante «porque»"],
        ["ficha con a), b), c) y d)", "frase final con «porque»"],
        ["poner opiniones como rasgos", "decir que es buena por ser rápida"],
        "Reconoce la ficha y pide cambiar una opinión suelta por una frase que cite un rasgo audible.",
    ),
    "Escucha una canción que te guste y anota tres rasgos audibles, un dato de contexto y tu opinión en líneas separadas.",
    "Elige una música de tradición oral de tu familia o región y una popular, y compara tres rasgos audibles de cada una.",
)

# ---------------------------------------------------------------- OA 01 · clase 2 (contexto, función y propósito)
L(
    OA1, 2,
    "Lápiz y papel. Los casos son de ejemplo y están escritos en cada ejercicio.",
    "Aprenderé a relacionar una música con su contexto y su función (para qué se usa) y a elegir criterios de valoración según ese propósito. Sirve para no juzgar igual una canción de cuna y una pieza para bailar.",
    ["Separo rasgos audibles, contexto y opinión.", "Sé que hay músicas de tradición oral, escrita y popular.", "Sé que una música puede tener varios usos."],
    [
        "La función es el papel que cumple una música en la vida de las personas: acompañar el baile, calmar a un bebé, marcar el paso de un desfile, contar una historia, expresar una protesta, celebrar una fiesta o simplemente invitar a escuchar con atención. Para descubrirla se pregunta: ¿quién la hace?, ¿para quién?, ¿dónde se escucha?, ¿en qué momento? y ¿con qué fin?",
        "El contexto explica muchas decisiones musicales. Un arrullo usa un tempo lento y una dinámica suave porque busca calmar. Una pieza para bailar usa un pulso marcado porque busca mover el cuerpo. El canto a lo poeta, que combina versos cantados con guitarra, pone en primer plano las palabras. Entender esto evita juzgar con un solo criterio músicas que nacieron para cosas distintas.",
        "Un criterio es una pauta para juzgar. Un buen criterio depende del propósito: si la música es para bailar, importa si el pulso se siente; si es para calmar, importa si la dinámica es suave; si es para contar una historia, importa si el texto se entiende. Elegir el criterio antes de escuchar ayuda a ser justo y a fundamentar mejor.",
    ],
    [("función", "papel que cumple una música en la vida de las personas"), ("propósito", "fin con que se hace o se usa una música"), ("contexto", "lugar, momento, personas y situación en que una música se crea o se escucha"), ("criterio", "pauta que se usa para juzgar"), ("dinámica", "grado de fuerza del sonido, de suave a fuerte"), ("canto a lo poeta", "tradición chilena de versos cantados con guitarra o guitarrón")],
    [
        ("Relacionar propósito y recurso", "Una pieza de ejemplo se usa para marchar en un desfile escolar. Es rápida, con tambores y un pulso muy marcado. ¿Qué recurso sirve a su propósito?", ["El propósito es mantener el paso de muchas personas.", "El pulso marcado permite caminar al mismo tiempo."], "El pulso marcado, porque ayuda a mantener el paso"),
        ("Elegir criterios según el propósito", "Quieres valorar una canción de cuna de ejemplo y una pieza de baile de ejemplo. ¿Usarías el mismo criterio central en ambas?", ["La cuna busca calmar: importa la dinámica suave y el tempo lento.", "El baile busca mover el cuerpo: importa el pulso marcado."], "No: cada pieza se valora con criterios según su propósito"),
    ],
    [
        ("Juzgar todas las músicas con el mismo criterio, por ejemplo «cuántos instrumentos tiene».", "Cada música nace con un propósito distinto y ese criterio no sirve para todas.", "Primero pregunta para qué se usa y después elige el criterio."),
        ("Pensar que el contexto es un adorno y que solo importa lo que suena.", "El contexto explica por qué se tomaron ciertas decisiones musicales.", "Relaciona cada rasgo audible con el propósito de la música."),
    ],
    [
        ex("Una pieza de ejemplo se canta para calmar a un bebé. ¿Cuál es su función? A) Calmar y acompañar el sueño. B) Marcar el paso en un desfile.", "A", "La función es el papel que cumple en el uso."),
        ex("¿Qué pregunta ayuda a descubrir el contexto de una música? A) ¿En qué momento y para quién se escucha? B) ¿Cuántas notas tiene la melodía?", "A", "El contexto habla de personas, lugar y momento."),
        ex("¿Qué es un criterio de valoración? A) Una pauta para juzgar. B) Un dato sobre el autor de la pieza.", "A", "Es la pauta que se usa al juzgar."),
    ],
    [
        ex("Una melodía de ejemplo para dormir tiene tempo lento y dinámica suave. ¿Por qué esas decisiones tienen sentido? A) Porque buscan calmar. B) Porque buscan mover mucho el cuerpo.", "A", "El propósito explica los recursos."),
        ex("En el canto a lo poeta, ¿qué suele ocupar el primer plano? A) Las palabras de los versos cantados. B) Los efectos electrónicos.", "A", "Los versos cantados son el centro, con guitarra o guitarrón de apoyo."),
        ex("¿Por qué conviene elegir el criterio antes de escuchar? A) Para que el juicio sea más justo y esté orientado al propósito. B) Para juzgar sin considerar el propósito.", "A", "El criterio dirige la atención hacia lo relevante."),
    ],
    [
        ex("Pieza de ejemplo para bailar en una fiesta: ¿qué criterio central es el más adecuado? A) Si el pulso se siente y permite bailar. B) Si dura más de diez minutos. C) Si usa el mayor número de instrumentos.", "A", "El baile exige un pulso claro."),
        ex("Una canción de ejemplo cuenta una historia en cuatro estrofas con voz y guitarra. ¿Qué criterio es más pertinente? A) Que el texto se entienda y la música lo acompañe. B) Que la música suene más fuerte que la voz.", "A", "El propósito es narrar."),
        ex("Una cantora de ejemplo dirige un canto de trabajo en el campo: todos responden al mismo ritmo para coordinar la tarea. ¿Cuál es su función? A) Coordinar el trabajo en grupo. B) Presentar una obra de concierto.", "A", "El canto sirve para trabajar juntos."),
    ],
    [
        ex("Dos estudiantes valoran una canción de cuna de ejemplo. Lía: «No sirve, porque no se puede bailar.» Teo: «Funciona, porque el tempo lento y la dinámica suave calman.» ¿Quién usa un criterio coherente con el propósito? A) Lía. B) Teo.", "B", "Teo juzga según la función de calmar."),
        ex("Una profesora dice: «Esa marcha es mala porque no es suave.» ¿Qué error comete? A) Aplica un criterio de arrullo a una pieza hecha para marchar. B) Confunde el pulso con la melodía.", "A", "El criterio no corresponde al propósito."),
    ],
    [
        ex("Una misma melodía de ejemplo se toca lenta y suave en la casa para dormir, y rápida y con tambores en un desfile. ¿Qué muestra esto? A) Que el contexto lleva a cambiar los recursos. B) Que son dos melodías distintas sin relación.", "A", "El propósito cambia tempo, dinámica y timbres."),
        arith("Un desfile de ejemplo dura 18 minutos y cada pieza de marcha dura 3 minutos. ¿Cuántas piezas caben, una tras otra, sin pausas?", "18//3", "Se divide el tiempo total por la duración de cada pieza.", " piezas"),
    ],
    [ex("Tu curso prepara un acto para recibir a estudiantes nuevos y necesita música de bienvenida. ¿Qué criterio es más útil para elegirla? A) Que invite a participar y se sienta alegre. B) Que sea lo más suave posible.", "A", "Debe cumplir el propósito del acto.")],
    [
        ex("¿Qué decide el criterio que usarás? A) El propósito de la música. B) El nombre del compositor.", "A", "El criterio sale de la función."),
        ex("¿Verdadero o falso? El contexto ayuda a explicar por qué una música suena como suena.", "Verdadero", "Los recursos responden al uso."),
        ex("Una pieza de ejemplo se canta para protestar en una marcha pacífica: ¿qué se valora como función? A) Dar fuerza al mensaje compartido. B) Calmar para dormir.", "A", "La función es expresar un mensaje en grupo."),
    ],
    (
        "Elige una pieza de ejemplo propia (inventada o recordada, sin copiar letras) y completa: a) quién la hace y para quién, b) para qué se usa, c) dos criterios que usarías para valorarla, d) un juicio de dos frases que una un rasgo audible con el propósito.",
        "a) La cantan vecinas para sus hijos. b) Para dormir. c) Tempo lento y dinámica suave. d) Cumple su propósito porque el tempo lento invita a la calma. Un cambio de tempo la haría menos adecuada.",
        ["indica quién, para quién y para qué", "elige criterios coherentes con el propósito", "une un rasgo audible con la función"],
        ["ficha con a), b), c) y d)", "juicio de dos frases"],
        ["usar un criterio que no corresponde al propósito", "no mencionar ningún rasgo audible"],
        "Reconoce la ficha y pide cambiar un criterio vago («me gusta») por uno ligado al propósito.",
    ),
    "Anota tres músicas que escuches en un día y para qué se usa cada una.",
    "Compara el propósito de una música de tradición oral y el de una popular que conozcas, y qué criterio elegirías para cada una.",
)

# ---------------------------------------------------------------- OA 01 · clase 3 (fundamentar un juicio)
L(
    OA1, 3,
    "Lápiz y papel. Los juicios que aparecen son de estudiantes ficticios.",
    "Aprenderé a construir y a mejorar un juicio con tres partes: afirmación, evidencia audible y criterio. Sirve para valorar músicas de Chile y del mundo con razones que otras personas puedan comprobar.",
    ["Describo rasgos audibles.", "Relaciono propósito y criterio.", "Distingo opinión de fundamento."],
    [
        "Un juicio fundamentado tiene tres partes. La afirmación dice qué valoras: «esta pieza logra crear calma». La evidencia audible muestra qué se oye que lo prueba: «el tempo es lento y la voz canta suave». El criterio explica con qué pauta juzgas: «una pieza para dormir debe calmar». Con las tres partes, otra persona puede escuchar, comprobar y hasta discrepar con razones.",
        "Un juicio débil suele fallar en una de las partes. Puede quedarse en la afirmación («es lindo»), dar evidencia que no se oye («tiene buen mensaje», sin citar nada), usar un criterio que no corresponde («está mal porque es lenta», para una pieza que debe calmar) o confundir calidad con volumen, velocidad o cantidad de instrumentos. Revisar cada parte es la forma de corregirlo.",
        "También se puede valorar con matices. Puedes reconocer una fortaleza y una debilidad de la misma pieza: «el estribillo se recuerda fácil, pero la segunda estrofa casi no cambia». Un juicio crítico no es un elogio ni un ataque; es una valoración justa, con razones, que reconoce la identidad cultural de la música y respeta a quienes la hicieron.",
    ],
    [("afirmación", "lo que se sostiene al valorar"), ("evidencia audible", "lo que se oye y prueba la afirmación"), ("juicio fundamentado", "valoración con afirmación, evidencia y criterio"), ("matiz", "reconocer a la vez aspectos fuertes y débiles"), ("identidad", "rasgos con los que un grupo se reconoce, que una música puede expresar")],
    [
        ("Armar un juicio de tres partes", "Pieza de ejemplo: coro de voces femeninas, tempo lento, dinámica suave, se canta para despedir un día de trabajo. Escribe un juicio con afirmación, evidencia y criterio.", ["Afirmación: crea un ambiente de calma.", "Evidencia: tempo lento y dinámica suave.", "Criterio: una música de cierre debe calmar."], "Crea calma porque el tempo es lento y la dinámica suave, como pide una música de cierre"),
        ("Corregir un juicio débil", "Juicio: «Esa cueca es mala porque nadie la conoce». ¿Qué parte falla y cómo se mejora?", ["Que nadie la conozca no es un rasgo audible.", "Falta evidencia que se oiga y un criterio ligado al propósito de bailar."], "Falla la evidencia; se mejora citando el pulso y el tempo y juzgando si permiten bailar"),
    ],
    [
        ("Pensar que «tiene buen mensaje» es evidencia audible.", "El mensaje es una idea; la evidencia debe poder oírse, como un texto claro o una melodía que lo refuerce.", "Cita qué se oye que muestra ese mensaje."),
        ("Creer que un juicio crítico solo puede ser negativo.", "Valorar críticamente es juzgar con razones, y también reconoce fortalezas.", "Incluye una fortaleza y, si corresponde, una debilidad, ambas con evidencia."),
    ],
    [
        ex("¿Cuáles son las tres partes de un juicio fundamentado? A) Afirmación, evidencia audible y criterio. B) Título, autor, fecha y lugar.", "A", "Son las partes que permiten comprobar el juicio."),
        ex("En «el tempo es lento y la voz canta suave», ¿qué parte del juicio aparece? A) La evidencia audible. B) La opinión sin razón.", "A", "Describe lo que se oye."),
        ex("En «una pieza para dormir debe calmar», ¿qué parte del juicio aparece? A) El criterio. B) La afirmación sobre el volumen.", "A", "Es la pauta con que se juzga."),
    ],
    [
        ex("¿Por qué «es mala porque es lenta» es un juicio débil? A) Porque la velocidad no mide la calidad y no se relaciona con el propósito. B) Porque lo lento siempre es de peor calidad.", "A", "Usa velocidad como criterio sin ligarla al propósito."),
        ex("¿Qué agrega el matiz a una valoración? A) Reconoce a la vez una fortaleza y una debilidad. B) Hace que el juicio sea solo negativo.", "A", "El matiz equilibra, pero sigue pidiendo evidencia."),
        ex("¿Para qué sirve que la evidencia sea audible? A) Para que otras personas puedan comprobarla escuchando. B) Para que el juicio dependa del gusto de cada quien.", "A", "La comprobación hace discutible el juicio con razones."),
    ],
    [
        ex("Juicio: «Esta pieza coral de ejemplo es valiosa». ¿Cuál es la mejor evidencia audible para completarlo? A) «Las cuatro voces se escuchan claras y se reparten la melodía.» B) «La compuso alguien famoso.» C) «Se oyó en un teatro grande.»", "A", "Las otras dos no se oyen en la pieza."),
        ex("Un juicio dice: «El estribillo se recuerda fácil porque repite la melodía cuatro veces con las mismas palabras». ¿Qué parte es la evidencia? A) «Repite la melodía cuatro veces con las mismas palabras.» B) «El estribillo se recuerda fácil.»", "A", "Lo que se puede comprobar es la repetición."),
        ex("Elige el criterio coherente para valorar una pieza de ejemplo hecha para acompañar una caminata larga en grupo. A) Que el pulso sea constante y fácil de seguir. B) Que sea muy fuerte en cada frase.", "A", "Una caminata necesita un paso regular."),
    ],
    [
        ex("Dos juicios sobre la misma pieza de ejemplo. 1: «Es lo mejor, porque suena muy fuerte.» 2: «Logra energía porque el bombo marca el pulso y el tempo es rápido.» ¿Cuál es más sólido? A) El 1. B) El 2.", "B", "El 2 cita rasgos audibles y los une a un efecto."),
        ex("Un estudiante dice: «Esa música de otro país no vale, porque no la entiendo.» ¿Qué conviene hacer antes de juzgar? A) Buscar su contexto y describir lo que se oye. B) Decir que su gusto personal es suficiente.", "A", "No entender no es un criterio; hay que informarse."),
    ],
    [
        ex("Una pieza de ejemplo repite la misma frase ocho veces sin cambios en 4 minutos. Elige el juicio con matiz. A) «La repetición da identidad al tema, pero la falta de cambios hace larga la parte central.» B) «Es perfecta, no hay nada que decir.»", "A", "Reconoce fortaleza y debilidad con evidencia."),
        arith("En un taller, cada estudiante escribe 3 juicios fundamentados y cada juicio tiene 3 partes. Si participan 14 estudiantes, ¿cuántas partes se escriben en total?", "14*3*3", "Se multiplica estudiantes por juicios y por partes de cada juicio.", " partes"),
    ],
    [ex("Tu curso discute si una música tradicional de una región «es anticuada». ¿Qué respuesta usa fundamento? A) «Se puede valorar su función y su identidad actual: ¿qué rasgos oímos y para qué se usa hoy?» B) «Si es antigua, ya no tiene nada que valorar.»", "A", "Pide evidencia y contexto, no prejuicio.")],
    [
        ex("¿Qué parte de un juicio indica qué se oye? A) La evidencia. B) La afirmación.", "A", "La evidencia es lo audible."),
        ex("¿Verdadero o falso? Un juicio crítico puede reconocer fortalezas.", "Verdadero", "Valorar no es solo criticar."),
        ex("¿Cuál es un criterio para una pieza que debe animar una fiesta? A) Que la música invite a participar y a seguir el pulso. B) Que sea de tempo muy lento.", "A", "Debe cumplir su propósito de animar."),
    ],
    (
        "Pieza de ejemplo: voz y guitarra, dos estrofas iguales y un estribillo que se repite tres veces con más fuerza, tempo moderado, usada para cantar en grupo en una celebración. Escribe un juicio fundamentado con afirmación, evidencia audible y criterio, y agrega una debilidad con su evidencia.",
        "Afirmación: invita a cantar en grupo. Evidencia: el estribillo se repite tres veces con más fuerza y el tempo es moderado. Criterio: una música de celebración debe poder cantarse entre todos. Debilidad: las dos estrofas son idénticas, por eso no aportan novedad.",
        ["incluye afirmación, evidencia y criterio", "la evidencia es audible", "agrega una debilidad con evidencia"],
        ["juicio escrito en tres partes", "debilidad con evidencia"],
        ["usar solo opiniones", "criticar por velocidad o volumen"],
        "Reconoce el juicio y pide reemplazar una frase que no se puede comprobar por un rasgo que se oiga.",
    ),
    "Reescribe tres opiniones que hayas dicho sobre música en juicios de tres partes.",
    "Pide a una compañera o compañero que lea tu juicio y diga si la evidencia se puede comprobar escuchando.",
)

# ---------------------------------------------------------------- OA 01 · clase 4 (comunicar por medios verbales, visuales, sonoros y corporales)
L(
    OA1, 4,
    "Lápiz, hojas y espacio libre para moverte con seguridad. Los casos son de ejemplo. Los movimientos son suaves y no requieren saltos ni esfuerzo.",
    "Aprenderé a comunicar los fundamentos de mi valoración por medios verbales, visuales, sonoros y corporales. Sirve para explicar lo que oigo de modos que todas las personas puedan comprender, también quien se expresa mejor sin palabras.",
    ["Construyo juicios con afirmación, evidencia y criterio.", "Describo rasgos como tempo, melodía y dinámica.", "Sé que hay distintas formas de expresar una idea."],
    [
        "Los fundamentos de una valoración se pueden comunicar de cuatro modos. Verbal: hablar o escribir con precisión. Visual: dibujar una línea que sube y baja con la melodía, usar colores para las partes de la forma o armar un mapa con las estrofas y el estribillo. Sonoro: cantar, tocar o palmear el rasgo que quieres mostrar. Corporal: mover los brazos o dar pasos suaves al pulso para mostrar el tempo y la dinámica.",
        "Cada medio muestra mejor ciertos rasgos. La línea melódica dibujada muestra cuándo la melodía sube o baja. Palmear muestra el pulso y el ritmo. Un movimiento amplio de los brazos puede mostrar una dinámica fuerte y uno pequeño, una dinámica suave. Las palabras conectan todo con el propósito y el criterio. Combinar medios hace más claro el fundamento que usar uno solo.",
        "Comunicar bien exige cuidado. El medio debe corresponder al rasgo: no sirve dibujar el timbre con una línea que sube, ni bailar sin decir qué rasgo muestras. Los movimientos deben ser seguros y adecuados al espacio. Y se debe respetar a las demás personas: se escucha el juicio ajeno, se discrepa con razones y se cuida el volumen para no molestar ni dañar el oído.",
    ],
    [("medio verbal", "comunicar con palabras habladas o escritas"), ("medio visual", "comunicar con dibujos, colores, esquemas o mapas"), ("medio sonoro", "comunicar cantando, tocando o palmeando"), ("medio corporal", "comunicar con gestos y movimientos"), ("línea melódica", "dibujo que sube y baja siguiendo la melodía")],
    [
        ("Elegir el medio según el rasgo", "Quieres mostrar a tu curso que una melodía de ejemplo sube de a poco y luego cae. ¿Qué medio visual conviene?", ["El rasgo es el movimiento de la melodía.", "Una línea que sube y luego baja lo representa."], "Una línea melódica dibujada que sube y luego baja"),
        ("Combinar medios", "Quieres comunicar que una pieza de ejemplo tiene pulso marcado y dinámica fuerte en el estribillo. Propón dos medios y qué mostrarían.", ["Sonoro: palmear el pulso muestra que es marcado.", "Corporal: movimientos amplios muestran la dinámica fuerte."], "Palmear el pulso y mover los brazos con amplitud en el estribillo"),
    ],
    [
        ("Dibujar lo que no corresponde: usar una línea que sube para mostrar el timbre.", "El timbre es el color del sonido y no sube ni baja como la melodía.", "Elige un medio ligado al rasgo, por ejemplo colores o palabras para el timbre."),
        ("Mostrar solo con movimiento y no decir qué rasgo se muestra.", "Sin palabras, la audiencia puede entender otra cosa.", "Explica con una frase qué rasgo muestras y por qué."),
    ],
    [
        ex("¿Qué medio usas al palmear el pulso de una pieza? A) Sonoro. B) Verbal.", "A", "El palmeo es un sonido que muestra el pulso."),
        ex("¿Qué medio usas al dibujar una línea que sube y baja con la melodía? A) Visual. B) Corporal.", "A", "Es un dibujo."),
        ex("¿Qué medio usas al mover los brazos con amplitud para mostrar una dinámica fuerte? A) Corporal. B) Verbal.", "A", "El gesto con el cuerpo muestra la dinámica."),
    ],
    [
        ex("¿Por qué conviene combinar medios? A) Porque cada medio muestra mejor ciertos rasgos y juntos hacen más claro el fundamento. B) Porque los medios verbales no sirven.", "A", "Combinar complementa, sin negar que uno solo sirva."),
        ex("Quieres mostrar las partes de la forma (estrofa, estribillo, estrofa). ¿Qué medio visual sirve? A) Un mapa con un color para cada parte. B) Una línea que sube y baja.", "A", "El mapa de colores muestra la forma."),
        ex("¿Qué debe hacer una persona que baila para comunicar un fundamento? A) Decir con una frase qué rasgo está mostrando. B) Bailar con más energía para que se note.", "A", "Las palabras aclaran qué rasgo se muestra."),
    ],
    [
        ex("Una melodía de ejemplo sube tres notas, se mantiene y baja cinco. ¿Cuál dibujo la representa? A) Una línea que sube un poco, queda plana y baja más. B) Una línea que baja primero y luego sube.", "A", "Debe seguir el orden: sube, se mantiene, baja."),
        ex("Para mostrar que una pieza de ejemplo se hace cada vez más lenta, ¿qué movimiento corporal sirve? A) Pasos suaves cada vez más espaciados. B) Pasos cada vez más rápidos.", "A", "El espaciamiento muestra el tempo que baja."),
        ex("Quieres que el curso escuche el rasgo «la melodía se repite dos veces». ¿Qué medio sonoro es adecuado? A) Cantar o tararear la frase dos veces seguidas. B) Dibujar una línea que sube y baja una vez.", "A", "Repetir la frase muestra el rasgo."),
    ],
    [
        ex("Una compañera presenta un juicio con una línea dibujada, pero no explica qué muestra. ¿Qué le falta? A) Una frase que conecte el dibujo con el rasgo y el propósito. B) Más colores.", "A", "Falta el medio verbal que explique."),
        ex("Un grupo baila con saltos fuertes en una sala pequeña para mostrar la dinámica. ¿Qué cambio es más seguro? A) Usar movimientos amplios de brazos sin saltos, con espacio libre. B) Aumentar la velocidad.", "A", "La seguridad es parte de comunicar bien."),
    ],
    [
        ex("Un estudiante quiere mostrar tres rasgos: tempo rápido, melodía que sube y timbre brillante. Si usa un medio distinto para cada uno, ¿cuántos medios usa? A) Tres. B) Cuatro.", "A", "Un medio por rasgo son tres."),
        arith("Una presentación de ejemplo tiene 6 grupos y cada grupo usa 2 medios distintos. ¿Cuántos medios se usan en total entre todos los grupos?", "6*2", "Se multiplican los grupos por los medios de cada uno.", " medios"),
    ],
    [ex("Tu curso presenta un juicio sobre una música de tradición oral para otro curso. Una persona del grupo es tímida con la voz. ¿Qué propuesta es buena? A) Que muestre el rasgo con un dibujo o un movimiento y otra persona lo explique con palabras. B) Que se quede en silencio sin participar.", "A", "Hay varios medios y se pueden repartir los roles.")],
    [
        ex("¿Qué medio muestra mejor el color de un sonido, es decir, el timbre? A) Palabras o colores. B) Una línea que sube y baja.", "A", "El timbre se describe con adjetivos o se representa con colores."),
        ex("¿Verdadero o falso? Los movimientos corporales deben ser seguros para el espacio disponible.", "Verdadero", "La seguridad va antes del efecto."),
        ex("¿Cuáles son los cuatro medios de esta clase? A) Verbal, visual, sonoro y corporal. B) Oral, escrito, popular y digital.", "A", "Son los medios de comunicar fundamentos."),
    ],
    (
        "Pieza de ejemplo: voz y guitarra, tempo moderado, la melodía sube en la primera mitad de cada estrofa y baja en la segunda; el estribillo es más fuerte. Prepara un juicio de dos frases y elige tres medios (de los cuatro) para comunicarlo: indica qué rasgo muestra cada uno.",
        "Juicio: la pieza crea tensión y alivio porque la melodía sube y baja en cada estrofa y el estribillo es más fuerte. Visual: línea melódica. Sonoro: tararear una estrofa. Corporal: brazos que suben y bajan suavemente, más amplios en el estribillo.",
        ["escribe un juicio con evidencia audible", "elige tres medios y los une a rasgos", "propone movimientos seguros"],
        ["juicio de dos frases", "lista de tres medios con su rasgo"],
        ["elegir un medio que no se relaciona con el rasgo", "no explicar con palabras"],
        "Reconoce el plan y pide agregar una frase que diga qué mostrará cada medio.",
    ),
    "Dibuja la línea melódica de una frase que conozcas y explica con dos oraciones lo que muestra.",
    "Elige un rasgo de una música (tempo, dinámica o forma) y prepáralo para mostrarlo con dos medios distintos.",
)

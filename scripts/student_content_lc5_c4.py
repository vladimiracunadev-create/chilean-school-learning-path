"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS02 (desarrollar diálogos, conversaciones y exposiciones breves referidos a distintos aspectos de la propia cultura,
incorporando algunas palabras en lengua indígena o en castellano, culturalmente significativas).

Criterio de autoría: los diálogos, fichas, escuelas y personas son inventados solo para practicar y están rotulados como
tales. «La propia cultura» puede ser la de la familia, la escuela, el barrio o un pueblo; no se supone la cultura de
ningún estudiante ni se le pide hablar de la suya. Las únicas palabras en lengua indígena son «mari mari» (saludo) y
«chaltumay» (gracias), ambas en mapuzugun. Las palabras del castellano de Chile usadas (minga, once) se explican en
la ficha. No se inventa gramática ni pronunciación: cómo se dicen las palabras de una lengua lo enseña el educador/a
tradicional. No se piden datos personales ni de la familia.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS2 = "LC05 OA LS02"

CONSULT = " Recuerda: cómo se dicen y cuándo se usan las palabras de una lengua indígena lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado. Puedes hablar de la cultura que tú elijas y no estás obligado a contar nada de tu familia."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. Ningún estudiante debe representar a su pueblo ni explicar su cultura si no lo desea."

PAL = "Ficha de palabras (de práctica): «mari mari» es un saludo en mapuzugun que se dice al encontrarse con alguien. «Chaltumay» quiere decir «gracias» en mapuzugun. «Minga» es una palabra del castellano de Chile para un trabajo en que varias personas ayudan juntas. «Once» es, en Chile, la comida liviana de la tarde."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ============================================================ LS02 clase 1 · situar tema, cultura y fuente
TEMAS = "Tres temas de práctica (inventados): Tema 1, cómo se organiza una minga en el barrio de la Escuela Ejemplo (fuente: una vecina que participó y autoriza contarlo). Tema 2, cómo es una once en un curso de la Escuela Muestra (fuente: el propio curso). Tema 3, cómo se saluda al comenzar un taller de lengua mapuche (fuente: la educadora tradicional de la escuela, que autoriza contar el saludo «mari mari»)."

L(
    LS2, 1,
    materials="Lápiz y hoja. Las fichas están escritas aquí y son inventadas para practicar. No necesitas dispositivos.",
    use="Aprenderé a elegir un aspecto de una cultura para conversar o exponer, ubicando de qué cultura habla, cuál es la fuente y qué palabras significativas puedo incluir. Sirve para hablar de la cultura con claridad y respeto.",
    prior=["Sé ubicar pueblo, territorio y fuente.", "Sé que las palabras de una lengua indígena se copian como las enseñó su fuente."],
    explain=[
        "Un diálogo es una conversación entre dos personas, una conversación puede tener más personas y una exposición breve es cuando una persona explica un tema a otros durante unos minutos. En las tres puedo hablar de aspectos de la propia cultura: una costumbre, una comida, un saludo, una forma de trabajar. La propia cultura puede ser la de mi familia, mi barrio, mi escuela o mi pueblo. Cada persona elige de cuál habla y qué comparte.",
        "Para empezar elijo un tema y lo ubico: ¿de qué cultura o comunidad hablo?, ¿quién es mi fuente?, ¿autoriza que lo cuente? También elijo algunas palabras significativas, es decir, que tienen valor para esa cultura. Pueden ser de una lengua indígena, como «mari mari» y «chaltumay» en mapuzugun, o del castellano de Chile, como «minga» y «once».",
        "No necesito usar muchas palabras. Es mejor usar pocas, bien explicadas y con su fuente. Si una palabra es de una lengua indígena, la copio tal como me la enseñaron y digo quién la enseñó. Si no estoy seguro de cómo se dice o cuándo se usa, no la uso y pregunto al educador o educadora tradicional.",
    ],
    vocab=[("diálogo", "conversación entre dos personas"), ("exposición breve", "explicación de un tema a otros durante pocos minutos"), ("propia cultura", "la cultura de mi familia, barrio, escuela o pueblo"), ("palabra significativa", "palabra con valor para una cultura"), ("tema", "de qué se va a hablar")],
    worked=[
        W("Elegir el tema con fuente", TEMAS + " ¿Cuál tema tiene como fuente a una educadora tradicional?", ["Leo la fuente de cada tema.", "El tema 3 nombra a la educadora tradicional de la escuela.", "Los otros temas tienen otras fuentes."], "el tema 3"),
        W("Elegir las palabras", PAL + " Quiero conversar sobre un saludo mapuche. ¿Qué palabra de la ficha me sirve?", ["Busco una palabra que sea un saludo.", "«Mari mari» es un saludo en mapuzugun.", "La copio tal cual la ficha y nombro a la fuente."], "«mari mari»"),
    ],
    mistakes=[
        M("Exponer sobre la cultura de una compañera sin que ella lo haya pedido.", "Cada persona decide qué comparte de su cultura.", "Hablo de una cultura que conozco o de una fuente que autoriza."),
        M("Llenar la exposición de palabras indígenas para que «se note» la cultura.", "Pueden estar mal usadas.", "Uso pocas palabras, bien explicadas y con su fuente."),
    ],
    R=[
        ex(TEMAS + " ¿De qué trata el tema 2?", "cómo es una once en un curso", "El tema 2 lo dice."),
        ex(PAL + " ¿Qué quiere decir «chaltumay»?", "gracias", "La ficha lo dice."),
        ex("Un diálogo, ¿es una conversación entre dos personas o una explicación larga de una sola persona?", "una conversación entre dos personas", "Así se definió diálogo."),
    ],
    C=[
        ex(PAL + " ¿«Minga» es una palabra del mapuzugun o del castellano de Chile?", "del castellano de Chile", "La ficha lo indica."),
        ex(TEMAS + " Verdadero o falso: el tema 1 tiene como fuente a una vecina que autoriza contar la minga.", "Verdadero", "El tema 1 lo dice."),
        ex("Una exposición breve, ¿explica un tema a otros en pocos minutos o es una conversación entre amigos?", "explica un tema a otros en pocos minutos", "Así se definió exposición breve."),
    ],
    A=[
        ex(TEMAS + " " + PAL + " Une cada tema con la palabra significativa de la ficha que le corresponde: A) tema 1, B) tema 2, C) tema 3. Palabras: 1) «once», 2) «mari mari», 3) «minga». Escribe los tres pares.", "A-3, B-1, C-2", "El tema 1 es una minga, el 2 es una once y el 3 es un saludo."),
        arith("Una exposición breve dura 3 minutos. Un grupo hace 4 exposiciones seguidas. ¿Cuántos minutos duran en total?", "3*4", "Se multiplican los minutos por la cantidad de exposiciones."),
        ex("Ordena para preparar una exposición: A) elijo las palabras y su fuente. B) elijo el tema. C) ubico la cultura y la fuente. Escribe las letras en orden.", "B, C, A", "Primero el tema, luego la cultura y la fuente y después las palabras."),
    ],
    Z=[
        ex("Un niño no quiere hablar de la cultura de su familia. ¿Qué es mejor: A) obligarlo a contar algo o B) dejar que elija otro aspecto de una cultura que conozca, con fuente?", "B", "Cada persona decide qué comparte."),
        ex("Una niña dice: «Si uso diez palabras indígenas, mi exposición será mejor». ¿Es necesariamente cierto? Sí o No.", "No", "Importa usarlas bien y con fuente, no la cantidad."),
    ],
    D=[
        ex(TEMAS + " ¿Qué tema necesita además la autorización de la educadora para contar un saludo?", "el tema 3", "Solo el tema 3 incluye el saludo «mari mari»."),
        ex("Un tema de práctica dice: «Cómo se baila en un pueblo». No dice de qué pueblo ni la fuente. ¿Qué haces: A) lo expones igual o B) pides los datos que faltan antes?", "B", "Sin pueblo ni fuente no se debe exponer."),
    ],
    context=[ex("Tu curso hará una exposición sobre una costumbre del barrio. ¿Eliges el tema y ubicas la fuente antes de preparar las palabras o empiezas por las palabras?", "eliges el tema y ubicas la fuente antes de preparar las palabras", "Las palabras se eligen según el tema y su fuente.")],
    selfcheck=[
        ex("¿La propia cultura puede ser la de mi barrio o escuela? Sí o No.", "Sí", "Puede ser la de mi familia, barrio, escuela o pueblo."),
        ex("¿Está bien usar una palabra indígena sin saber cómo se usa? Sí o No.", "No", "Se pregunta antes al educador o educadora tradicional."),
        ex("Una palabra significativa, ¿tiene valor para una cultura o es una palabra cualquiera?", "tiene valor para una cultura", "Así se definió palabra significativa."),
    ],
    task=T(
        "Lee estos tres temas de práctica: A) cómo se hace una minga para arreglar una plaza; B) cómo es una once con el curso; C) cómo se saluda al empezar un taller de lengua mapuche. Elige uno y escribe en tu cuaderno una ficha de cuatro líneas: tema, cultura o comunidad de la que hablas, fuente y una palabra significativa de la ficha de palabras con su significado. Si no sabes un dato, escribe «por preguntar». Termina con una pregunta que le harías a una persona de tu comunidad o a tu educador o educadora tradicional.",
        "Tema: cómo se saluda al empezar un taller de lengua mapuche. Cultura: mapuche, según la ficha. Fuente: la educadora tradicional. Palabra: «mari mari», saludo en mapuzugun. Pregunta: ¿en qué otros momentos se usa este saludo?",
        ["elige un tema", "ubica cultura y fuente", "incluye una palabra con su significado", "usa «por preguntar» donde no sabe"],
        ["ficha de cuatro líneas", "pregunta escrita o dicha en voz alta"],
        ["inventar la fuente", "usar una palabra sin significado"],
        "Verifica que la palabra elegida esté en la ficha y que la fuente no sea inventada.",
    ),
    reinforce="Relee la ficha de palabras y copia cada palabra con su significado en una tarjeta.",
    extend="Escribe una ficha de cuatro líneas para otro tema de tu barrio, con una palabra significativa del castellano de Chile y su explicación.",
)

# ============================================================ LS02 clase 2 · escuchar con límites declarados
DIAL = "Diálogo de práctica (inventado). Estudiante 1: «Mari mari. ¿Me cuentas cómo fue la minga de tu barrio?». Estudiante 2: «Mari mari. Fue un sábado: entre todos barrimos la plaza y plantamos flores. Mi vecina dijo que así se cuida el lugar donde vivimos». Estudiante 1: «¿Esa minga se hace igual en otros barrios?». Estudiante 2: «No lo sé: te cuento solo la de mi barrio». Estudiante 1: «Chaltumay por contarme». (Las palabras «mari mari» y «chaltumay» son del mapuzugun y las enseñó la educadora tradicional de la escuela.)"

L(
    LS2, 2,
    materials="Lápiz y hoja. El diálogo está escrito aquí y es inventado para practicar. Puede leerlo en voz alta con otra persona.",
    use="Aprenderé a escuchar un diálogo o una exposición breve sobre una cultura y a distinguir qué dice cada persona, qué palabras significativas usa y qué límites declara. Sirve para conversar con atención y respeto.",
    prior=["Sé elegir un tema con su fuente.", "Sé que las palabras indígenas se usan con su fuente."],
    explain=[
        "Escuchar bien en un diálogo es parte de conversar. Miro a quien habla, espero mi turno y no interrumpo. Después puedo preguntar para entender mejor. Una buena pregunta aclara algo que la otra persona dijo, como «¿esa minga se hace igual en otros barrios?». Una pregunta respetuosa no corrige ni cuestiona la cultura del otro.",
        "En el diálogo de práctica aparecen dos palabras en mapuzugun, «mari mari» y «chaltumay», con su fuente: la educadora tradicional. También aparece una palabra del castellano de Chile, «minga». El Estudiante 2 declara un límite: «te cuento solo la de mi barrio». Escucho ese límite y no uso su relato para hablar de todos los barrios.",
        "Al escuchar anoto tres cosas: qué contó la persona, qué palabras significativas usó y qué límite declaró. Si no entiendo una palabra, lo digo con respeto y pregunto. Y si me cuentan algo de su cultura, lo agradezco. Así la conversación es un intercambio y no una prueba.",
    ],
    vocab=[("turno", "momento en que me toca hablar"), ("interrumpir", "hablar cuando otra persona está hablando"), ("aclarar", "hacer más claro algo que no se entendió"), ("límite declarado", "aviso de lo que la persona no cuenta o no sabe"), ("intercambio", "dar y recibir ideas")],
    worked=[
        W("Reconocer lo que contó", DIAL + " ¿Qué hicieron en la minga, según el Estudiante 2?", ["Busco lo que cuenta el Estudiante 2.", "Dice que barrieron la plaza.", "Y plantaron flores."], "barrieron la plaza y plantaron flores"),
        W("Reconocer el límite", DIAL + " ¿Qué límite declara el Estudiante 2?", ["Busco la frase donde dice lo que no sabe.", "Dice: «No lo sé: te cuento solo la de mi barrio».", "Ese es su límite."], "solo cuenta la minga de su barrio y no sabe cómo es en otros"),
    ],
    mistakes=[
        M("Interrumpir para corregir cómo cuenta alguien su cultura.", "Cada persona cuenta lo que vive.", "Espero mi turno y pregunto con respeto."),
        M("Usar lo que dijo el Estudiante 2 para hablar de todos los barrios.", "Él declaró que solo cuenta el suyo.", "Respeto el límite y hablo solo de su barrio."),
    ],
    R=[
        ex(DIAL + " ¿Qué día fue la minga?", "un sábado", "El diálogo lo dice."),
        ex(DIAL + " ¿Qué plantaron en la plaza?", "flores", "El diálogo lo dice."),
        ex(DIAL + " ¿Qué saludo usan al comenzar?", "mari mari", "Lo dicen ambos al comienzo."),
    ],
    C=[
        ex(DIAL + " ¿Quién enseñó las palabras en mapuzugun, según el diálogo?", "la educadora tradicional de la escuela", "El diálogo lo aclara entre paréntesis."),
        ex(DIAL + " Verdadero o falso: el Estudiante 2 dice que la minga se hace igual en todos los barrios.", "Falso", "Dice que no lo sabe."),
        ex(DIAL + " ¿Por qué agradece el Estudiante 1 con «chaltumay»?", "por contarle cómo fue la minga", "Dice «chaltumay por contarme»."),
    ],
    A=[
        ex(DIAL + " Cuenta las veces que aparece «mari mari» en el diálogo (solo en las frases habladas, sin contar la nota final).", "2", "Aparece una vez por cada estudiante.", "1+1"),
        ex(DIAL + " Ordena las partes del diálogo: A) pregunta si se hace igual en otros barrios. B) saludan. C) agradece. Escribe las letras en orden.", "B, A, C", "Primero saludan, luego preguntan y al final agradecen."),
        ex(DIAL + " ¿Qué palabra del castellano de Chile aparece: minga o once?", "minga", "El diálogo habla de la minga."),
    ],
    Z=[
        ex("En un diálogo, alguien cuenta una costumbre de su familia que tú no conocías. ¿Qué es mejor: A) decir «eso está mal» o B) preguntar con respeto para entenderla?", "B", "Una pregunta respetuosa aclara sin cuestionar."),
        ex(DIAL + " Un compañero dice que, según el diálogo, en todos los barrios se barre la plaza. ¿Respeta el límite del Estudiante 2? Sí o No.", "No", "El estudiante contó solo la de su barrio."),
    ],
    D=[
        ex(DIAL + " Elige la mejor pregunta para aclarar: A) «¿Quién decidió qué día se hizo la minga?». B) «Tu cultura es rara, ¿verdad?». Escribe la letra.", "A", "A aclara sin juzgar."),
        ex("Una exposición breve dura 2 minutos. Después hay 1 minuto para preguntas. ¿Cuántos minutos son en total?", "3", "Dos minutos más uno.", "2+1"),
    ],
    context=[ex("Un compañero expone sobre una costumbre y usa una palabra que no conoces. ¿Esperas el final y preguntas con respeto o lo interrumpes para decirle que está equivocado?", "esperas el final y preguntas con respeto", "Se espera el turno y se aclara sin juzgar.")],
    selfcheck=[
        ex("¿Debo esperar mi turno para hablar? Sí o No.", "Sí", "No se interrumpe a quien habla."),
        ex("Una pregunta respetuosa, ¿aclara o corrige la cultura del otro?", "aclara", "No cuestiona su cultura."),
        ex("Si alguien declara un límite, ¿lo respeto? Sí o No.", "Sí", "Ese límite avisa hasta dónde vale su relato."),
    ],
    task=T(
        "Lee este diálogo inventado: Estudiante 1: «Mari mari. ¿Cómo es una once en tu curso?». Estudiante 2: «Mari mari. Traemos cosas para compartir y nos sentamos juntos a las cuatro. No sé cómo es en otros cursos». Estudiante 1: «Chaltumay por contarme». (Las palabras en mapuzugun las enseñó una educadora tradicional inventada.) En tu cuaderno escribe: qué contó el Estudiante 2, qué palabras significativas usan y con qué fuente, y qué límite declaró. Luego escribe una pregunta de aclaración respetuosa que le harías.",
        "Contó que en su curso traen cosas para compartir y se sientan juntos a las cuatro. Palabras: «mari mari» y «chaltumay», enseñadas por la educadora tradicional; «once», del castellano de Chile. Límite: no sabe cómo es en otros cursos. Pregunta: ¿qué sueles llevar tú para compartir?",
        ["recoge lo que contó", "nombra las palabras con su fuente", "nombra el límite", "escribe una pregunta respetuosa"],
        ["respuesta escrita", "pregunta de aclaración"],
        ["olvidar el límite", "preguntar con juicio"],
        "Cuida que la pregunta de aclaración no juzgue.",
    ),
    reinforce="Lee el diálogo en voz alta con otra persona, cada una en su turno, y subraya las palabras significativas.",
    extend="Escribe un diálogo de seis turnos sobre otra costumbre de tu barrio, con un saludo, una pregunta de aclaración y un agradecimiento.",
)

# ============================================================ LS02 clase 3 · relaciones culturales: cuándo y para qué se usa cada palabra
USOS = "Ficha de usos (de práctica): «Mari mari» se usa para saludar a alguien al encontrarse. «Chaltumay» se usa para agradecer. «Minga» se usa para nombrar un trabajo en que varias personas ayudan juntas. «Once» se usa para nombrar la comida liviana de la tarde. Cada palabra se usa en su situación y siempre se pregunta al educador o educadora tradicional cómo se usa en la comunidad."

L(
    LS2, 3,
    materials="Lápiz y hoja. La ficha está escrita aquí y es de práctica. No necesitas dispositivos.",
    use="Aprenderé a relacionar cada palabra significativa con la situación en que se usa y con el valor que tiene para la cultura. Sirve para usar las palabras en el momento adecuado dentro de un diálogo o una exposición.",
    prior=["Sé elegir un tema con su fuente.", "Sé escuchar un diálogo y reconocer límites."],
    explain=[
        "Cada palabra significativa se usa en una situación. Un saludo se dice al encontrarse con alguien; una palabra de agradecimiento se dice cuando recibo algo o alguien me ayudó; una palabra que nombra un trabajo en común se usa para hablar de ese trabajo. Si uso una palabra en el momento equivocado, puede sonar extraño o faltar el respeto.",
        "Además, las palabras tienen valor para quienes las usan. Un saludo en la lengua de un pueblo muestra respeto y reconocimiento. «Minga» en el castellano de Chile recuerda la ayuda entre vecinos. «Once» recuerda un momento compartido. No digo más de lo que la fuente me enseñó: no explico significados profundos ni ritos que no conozco.",
        "Para usar una palabra en un diálogo, me hago tres preguntas: ¿qué quiere decir?, ¿cuándo se usa?, ¿quién me la enseñó? Por ejemplo, «chaltumay» la uso después de que alguien me contó algo, no al comenzar. Y siempre pregunto al educador o educadora tradicional cómo se dice y cuándo se usa en nuestra comunidad.",
    ],
    vocab=[("situación", "momento o lugar en que algo ocurre"), ("saludo", "palabra o gesto al encontrarse con alguien"), ("agradecimiento", "palabra o gesto con que se da las gracias"), ("reconocimiento", "valorar a una persona o cultura"), ("usar en su contexto", "decir la palabra en el momento que corresponde")],
    worked=[
        W("Elegir la palabra por la situación", USOS + " Alguien te acaba de explicar cómo es su costumbre. ¿Qué palabra de la ficha usas para agradecer?", ["Busco la palabra que sirve para agradecer.", "La ficha dice que «chaltumay» se usa para agradecer.", "La uso al final, tal como está escrita."], "«chaltumay»"),
        W("Detectar un uso equivocado", USOS + " Un niño dice «chaltumay» al llegar a la sala para saludar. ¿Es el uso que dice la ficha?", ["La ficha dice que «chaltumay» se usa para agradecer.", "Para saludar se usa «mari mari».", "No es el uso de la ficha."], "no: «chaltumay» es para agradecer; para saludar se usa «mari mari»"),
    ],
    mistakes=[
        M("Usar «chaltumay» para saludar.", "Cada palabra tiene su situación.", "Uso «mari mari» para saludar y «chaltumay» para agradecer."),
        M("Explicar significados profundos de una palabra sin que me los hayan enseñado.", "Podría decir algo falso o faltar el respeto.", "Digo solo lo que la fuente enseñó."),
    ],
    R=[
        ex(USOS + " ¿Para qué se usa «mari mari»?", "para saludar a alguien al encontrarse", "La ficha lo dice."),
        ex(USOS + " ¿Para qué se usa «chaltumay»?", "para agradecer", "La ficha lo dice."),
        ex(USOS + " ¿Qué nombra la palabra «once»?", "la comida liviana de la tarde", "La ficha lo dice."),
    ],
    C=[
        ex(USOS + " ¿Qué palabra nombra un trabajo en que varias personas ayudan juntas?", "minga", "La ficha lo dice."),
        ex("Verdadero o falso: puedo decir «chaltumay» para saludar porque me gusta cómo suena.", "Falso", "Se usa para agradecer."),
        ex("Un saludo, ¿se dice al encontrarse con alguien o al despedirse para siempre?", "al encontrarse con alguien", "Así se definió saludo."),
    ],
    A=[
        ex("Une cada situación con la palabra: A) llego a la sala y saludo, B) alguien me explicó algo y agradezco, C) hablamos del trabajo de vecinos de la plaza. Palabras: 1) «minga», 2) «chaltumay», 3) «mari mari». Escribe los tres pares.", "A-3, B-2, C-1", "Cada palabra se usa en su situación."),
        arith("Un diálogo usa 2 palabras indígenas y 3 palabras del castellano de Chile. ¿Cuántas palabras significativas usa en total?", "2+3", "Se suman las dos clases de palabras."),
        ex("Ordena un diálogo corto: A) agradezco con la palabra de la ficha. B) saludo con la palabra de la ficha. C) pregunto por la costumbre. Escribe las letras en orden.", "B, C, A", "Saludo, pregunto y agradezco."),
    ],
    Z=[
        ex("Una niña dice: «Si digo mari mari al despedirme, es igual». Según la ficha, ¿es correcto? Sí o No.", "No", "La ficha lo da como saludo al encontrarse."),
        ex("No sabes cuándo se usa una palabra indígena en tu comunidad. ¿Qué es mejor: A) preguntar al educador o educadora tradicional o B) usarla donde te parezca?", "A", "Quien conoce la lengua enseña su uso."),
    ],
    D=[
        ex(USOS + " Un niño dice: «Minga también es un saludo». ¿Dice eso la ficha? Sí o No.", "No", "La ficha dice que nombra un trabajo en común."),
        ex("Un estudiante escribe en su exposición: «Chaltumay solo se usa en ceremonias». ¿Esa explicación viene de la ficha? Sí o No.", "No", "La ficha solo dice que se usa para agradecer."),
    ],
    context=[ex("Una persona de tu comunidad te enseña cómo se dice una palabra y te cuenta cuándo se usa. ¿La usas después como te explicó o la cambias a tu gusto?", "la usas después como te explicó", "Se respeta el uso que enseñó la fuente.")],
    selfcheck=[
        ex("¿«Mari mari» es para saludar o para agradecer?", "para saludar", "Así lo dice la ficha."),
        ex("¿Una palabra se usa en cualquier situación? Sí o No.", "No", "Cada palabra tiene su situación."),
        ex("¿Quién me enseña cómo se usa una palabra indígena: el educador o educadora tradicional o mi imaginación?", "el educador o educadora tradicional", "Es quien conoce la lengua."),
    ],
    task=T(
        "Usa la ficha de usos de esta clase. En tu cuaderno escribe un diálogo de práctica de cinco turnos entre dos personas que se encuentran para hablar de una once con el curso. Debe incluir un saludo con la palabra que corresponde, una pregunta, una respuesta que use la palabra «once» y un agradecimiento con la palabra que corresponde. Subraya cada palabra significativa y escribe al lado su significado. Termina con una pregunta para el educador o educadora tradicional.",
        "1: Mari mari. ¿Cómo es la once en tu curso? 2: Mari mari. Compartimos lo que cada uno trae y nos sentamos juntos. 1: ¿Quién decide qué se trae? 2: Lo acordamos entre todos. 1: Chaltumay por contarme. Significados: mari mari (saludo), once (comida liviana de la tarde), chaltumay (gracias). Pregunta: ¿se usa chaltumay también en otros momentos en nuestra comunidad?",
        ["usa cada palabra en su situación", "incluye saludo, pregunta, respuesta con «once» y agradecimiento", "escribe los significados", "formula una pregunta"],
        ["diálogo de cinco turnos", "significados escritos"],
        ["usar chaltumay para saludar", "agregar significados no enseñados"],
        "Revisa que cada palabra aparezca en el turno que corresponde.",
    ),
    reinforce="Copia la ficha de usos y dibuja un símbolo simple al lado de cada palabra para recordar su situación.",
    extend="Escribe un diálogo de seis turnos que incluya las cuatro palabras de la ficha en su situación y una pregunta de aclaración.",
)

# ============================================================ LS02 clase 4 · exposición breve atribuida
EXPO = "Esquema de exposición de práctica (inventado): 1) Saludo: «Mari mari». 2) Tema: cómo se organiza una minga en el barrio. 3) Dato con fuente: según una vecina que participó, se juntaron doce personas. 4) Palabra significativa: «minga», trabajo en que varias personas ayudan juntas. 5) Límite: lo que cuento es de mi barrio. 6) Cierre: «Chaltumay por escucharme»."

L(
    LS2, 4,
    materials="Lápiz y hoja. El esquema está escrito aquí y es de práctica. Puedes practicar frente a una persona de tu casa o a un espejo.",
    use="Aprenderé a preparar una exposición breve sobre un aspecto de una cultura, con saludo, tema, dato con fuente, palabras significativas, límite y cierre. Sirve para hablar con orden y atribuyendo lo que cuento.",
    prior=["Sé escuchar con límites y usar palabras en su situación.", "Sé atribuir un dato a su fuente."],
    explain=[
        "Una exposición breve tiene un orden. Empieza con un saludo y el tema. Sigue con uno o dos datos, cada uno con su fuente: «según una vecina que participó…». Después incluye la palabra significativa con su explicación. Luego declara un límite: «lo que cuento es de mi barrio». Termina con un cierre, que puede incluir un agradecimiento.",
        "Preparo la exposición con un esquema de seis pasos y lo practico en voz alta. Hablo despacio, miro al público y uso mis palabras. Puedo llevar un papel con las ideas, pero no leo de corrido. Si uso una palabra de una lengua indígena, la digo y la escribo como me la enseñaron, y menciono quién la enseñó. Si no estoy seguro de cómo se dice, no la uso.",
        "Después de la exposición, escucho preguntas con respeto. Si me preguntan algo que no sé, digo «no lo sé» y anoto la pregunta para consultarla con una persona de mi comunidad o con el educador tradicional. Así mi exposición es honesta y sigue enseñando después de terminar.",
    ],
    vocab=[("esquema", "plan breve con los pasos de lo que voy a decir"), ("cierre", "final de una exposición"), ("público", "personas que escuchan"), ("dato con fuente", "información que dice quién la contó"), ("practicar", "repetir para hacerlo mejor")],
    worked=[
        W("Leer el esquema", EXPO + " ¿Cuál es el dato con fuente?", ["Busco el paso 3.", "Dice: según una vecina que participó, se juntaron doce personas.", "Ese es el dato con fuente."], "según una vecina que participó, se juntaron doce personas"),
        W("Completar un paso faltante", "Un esquema inventado tiene: saludo, tema, palabra significativa y cierre. ¿Qué dos pasos faltan para ser como el esquema de seis pasos?", ["Los seis pasos son saludo, tema, dato con fuente, palabra, límite y cierre.", "En el esquema aparecen saludo, tema, palabra y cierre.", "Faltan el dato con fuente y el límite."], "faltan el dato con fuente y el límite"),
    ],
    mistakes=[
        M("Leer la exposición de corrido sin mirar al público.", "No se conecta con quienes escuchan.", "Uso un esquema, hablo con mis palabras y miro al público."),
        M("Dar un dato sin decir quién lo contó.", "No se sabe de dónde viene.", "Agrego «según…» antes del dato."),
    ],
    R=[
        ex(EXPO + " ¿Qué palabra se usa en el saludo?", "mari mari", "El paso 1 la dice."),
        ex(EXPO + " ¿De qué trata el tema?", "cómo se organiza una minga en el barrio", "El paso 2 lo dice."),
        ex(EXPO + " ¿Con qué palabra se agradece al final?", "chaltumay", "El paso 6 la dice."),
    ],
    C=[
        ex(EXPO + " ¿Cuántas personas se juntaron según la vecina?", "doce", "El paso 3 lo dice."),
        ex(EXPO + " ¿Qué límite declara el esquema?", "lo que cuento es de mi barrio", "El paso 5 lo dice."),
        ex("Verdadero o falso: en una exposición puedo dar datos sin decir quién los contó.", "Falso", "Cada dato lleva su fuente."),
    ],
    A=[
        ex("Ordena los pasos de la exposición: A) límite. B) tema. C) saludo. D) cierre. E) palabra significativa. F) dato con fuente. Escribe las letras en el orden del esquema.", "C, B, F, E, A, D", "Sigue el orden del esquema de seis pasos."),
        arith("Una exposición dura 3 minutos y el saludo, el límite y el cierre usan 1 minuto en total. ¿Cuántos minutos quedan para el tema, el dato y la palabra?", "3-1", "Se restan los minutos del saludo, límite y cierre del total."),
        ex(EXPO + " Elige el mejor dato con fuente: A) «Según una vecina que participó, se juntaron doce personas». B) «Se juntó muchísima gente en todos los barrios». Escribe la letra.", "A", "A tiene fuente y no generaliza."),
    ],
    Z=[
        ex("Un niño se queda en blanco ante una pregunta. ¿Qué es mejor: A) inventar una respuesta o B) decir «no lo sé» y anotar la pregunta para averiguarla?", "B", "Ser honesto es parte de exponer bien."),
        ex(EXPO + " Si el expositor quita el paso 5, el límite, ¿se entiende que lo que cuenta vale solo para su barrio? Sí o No.", "No", "Sin el límite podría parecer que vale para todos."),
    ],
    D=[
        ex("Dos exposiciones: la 1 tiene fuente y límite; la 2 tiene muchas palabras indígenas sin fuente. ¿Cuál cumple mejor con lo que se pide en esta clase: 1 o 2?", "1", "Pocas palabras con fuente y límite son mejores."),
        ex("Un expositor quiere usar «chaltumay» al cierre. ¿Qué debe saber: A) cuándo se usa y quién se la enseñó, o B) solo que suena bonito?", "A", "Debe usarla en su situación y nombrar su fuente."),
    ],
    context=[ex("Vas a exponer en tu curso sobre una costumbre. Antes de hablar, ¿practicas en voz alta con un esquema o improvisas todo?", "practicas en voz alta con un esquema", "Practicar con un esquema ayuda a hablar con orden.")],
    selfcheck=[
        ex("¿Cuántos pasos tiene el esquema de esta clase: 6 o 3?", "6", "Saludo, tema, dato, palabra, límite y cierre.", "3*2"),
        ex("Si no sé la respuesta a una pregunta, ¿digo «no lo sé»? Sí o No.", "Sí", "Es honesto y respetuoso."),
        ex("Un dato con fuente, ¿dice quién lo contó? Sí o No.", "Sí", "Así se definió dato con fuente."),
    ],
    task=T(
        "Prepara una exposición breve de práctica sobre una once con el curso. Usa este dato inventado: «Según una profesora inventada de la Escuela Muestra, el curso comparte la once los viernes a las cuatro». En tu cuaderno escribe el esquema de seis pasos: saludo con la palabra que corresponde, tema, dato con fuente, palabra significativa («once» con su explicación), límite y cierre con agradecimiento. Practica en voz alta frente a una persona de tu casa o a un espejo. Termina con una pregunta para tu educador o educadora tradicional.",
        "1) Mari mari. 2) Tema: cómo compartimos la once en el curso. 3) Según una profesora de la Escuela Muestra, compartimos la once los viernes a las cuatro. 4) Once es la comida liviana de la tarde. 5) Lo que cuento es de mi curso. 6) Chaltumay por escucharme. Pregunta: ¿cómo se agradece en nuestra comunidad después de compartir una comida?",
        ["sigue los seis pasos", "atribuye el dato", "usa las palabras en su situación", "declara el límite"],
        ["esquema de seis pasos", "práctica en voz alta"],
        ["omitir el límite", "olvidar la fuente del dato"],
        "Escucha la práctica y pregunta qué paso fue el más difícil.",
    ),
    reinforce="Copia el esquema de seis pasos en una tarjeta y repítelo en voz alta sin mirarlo.",
    extend="Prepara el esquema de una segunda exposición sobre otro tema de tu barrio, con un dato y su fuente.",
)

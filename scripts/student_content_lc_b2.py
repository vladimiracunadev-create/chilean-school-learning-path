"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF02 (sonidos propios de la lengua indígena, fortalecimiento de la lengua).

Los ejercicios entrenan la escucha y la producción de sonidos con palabras en castellano como
práctica. No se inventa ninguna palabra ni sonido de lengua indígena: el modelo de pronunciación
lo da siempre el educador/a tradicional o un hablante competente de la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA = "LC01 OA LF02"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- Clase 1
register(
    OA, 1,
    materials="Este cuaderno y lápiz. Las palabras de práctica están en castellano. Para los sonidos de la lengua indígena escuchas al educador/a tradicional.",
    use="Aprenderé a escuchar bien un sonido antes de repetirlo y a reconocerlo dentro de una palabra o frase. Sirve para pronunciar con respeto la lengua de un pueblo.",
    prior=["Sé quedarme en silencio y escuchar.", "Sé decir si dos sonidos suenan igual o distinto."],
    explain=[
        "Antes de repetir un sonido hay que escucharlo con mucha atención. Si repites enseguida, es fácil cambiarlo por un sonido parecido que ya conoces. Escuchar primero te ayuda a oír cómo lo dice una persona que habla esa lengua.",
        "Un sonido se distingue en el contexto, es decir, dentro de una palabra o una frase, no solo suelto. Por ejemplo, en «sol» y «mar» oyes un sonido al comienzo que es distinto: la «s» y la «m». Escuchas qué cambia cuando cambia el sonido.",
        "El modelo de los sonidos de la lengua indígena es el educador o educadora tradicional, o un hablante competente. Tú escuchas, pides que lo repita las veces que necesites y recién después lo ensayas en voz baja. No te burlas ni lo cambias por otro.",
    ],
    vocab=[("sonido", "lo que oigo cuando alguien habla"), ("contexto", "la palabra o frase donde está un sonido"), ("distinguir", "notar que dos sonidos son distintos"), ("modelo", "la persona que dice el sonido como corresponde"), ("hablante competente", "persona que habla bien una lengua")],
    worked=[
        {"title": "Distinguir dos sonidos", "problem": "Escuchas dos palabras en castellano: «sol» y «mol». ¿Cuál sonido cambia?", "steps": ["Oigo «sol» y luego «mol».", "El final «ol» suena igual.", "Cambia el sonido del comienzo: «s» y «m»."], "answer": "Cambia el sonido del comienzo: s y m"},
        {"title": "Escuchar antes de repetir", "problem": "La educadora dice una palabra de la lengua de su pueblo que no conoces. ¿Qué haces primero?", "steps": ["Me quedo en silencio.", "Escucho la palabra completa.", "Pido que la repita si no la oí bien.", "Después la ensayo en voz baja."], "answer": "Escucho con atención y pido que la repita antes de ensayar"},
    ],
    mistakes=[
        {"wrong": "Repetir enseguida sin escuchar bien.", "why": "Cambias el sonido por uno parecido que ya conoces.", "fix": "Escucha entero y pide que lo repita antes de ensayar."},
        {"wrong": "Reírse de un sonido que no existe en castellano.", "why": "Es una forma de falta de respeto a la lengua y a quien la habla.", "fix": "Escucha con atención; todos aprendemos sonidos nuevos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué haces primero con un sonido nuevo: escuchar o repetir?", "Escuchar", "Se escucha antes de repetir."),
            ex("En «pato» y «gato», ¿cambia el sonido del comienzo o del final?", "Del comienzo", "Cambian «p» y «g»; «ato» suena igual."),
            ex("¿Quién da el modelo de los sonidos de una lengua indígena: un hablante competente o un compañero que adivina?", "Un hablante competente", "Quien habla bien la lengua es el modelo."),
        ],
        "understand": [
            ex("¿Qué quiere decir «distinguir un sonido en contexto»?", "Notarlo dentro de una palabra o frase", "El contexto es la palabra o frase donde está el sonido."),
            ex("¿Por qué conviene escuchar antes de repetir?", "Para no cambiar el sonido por uno parecido", "Escuchar bien evita sustituirlo por otro."),
            ex("Si no oíste bien una palabra, ¿qué le pides al educador/a tradicional?", "Que la repita", "Repetir ayuda a oírla mejor."),
        ],
        "apply": [
            ex("Escucha «mesa» y «pesa». ¿Qué sonido cambia: el primero o el último?", "El primero", "Cambian «m» y «p»; «esa» es igual."),
            ex("Escucha «casa» y «cama». ¿Cuál sonido cambia: el del comienzo o el del medio?", "El del medio: «s» y «m»", "En ca-sa y ca-ma cambia el sonido del medio."),
            ex("Escucha «toma» y «Toma». ¿Suenan igual o distinto?", "Igual", "La mayúscula no cambia el sonido."),
        ],
        "reason": [
            ex("Un niño repitió una palabra de la lengua indígena que no escuchó bien. Dijo otra distinta que sonaba parecida. ¿Qué pasó?", "Cambió el sonido por uno conocido", "Sin escuchar bien, se sustituye por un sonido parecido."),
            ex("Dos amigas oyen «casa» y «caza» y dicen que suenan igual. ¿Es posible en el castellano de Chile?", "Sí", "En Chile la «s» y la «z» suenan igual."),
        ],
        "challenge": [
            ex("Escucha estas tres palabras: «luna», «cuna», «runa». ¿Cuál sonido cambia en las tres?", "El primero", "Empiezan con «l», «c» y «r»; el resto suena igual."),
            ex("Escribe una palabra en castellano que empiece con un sonido distinto de «sol».", "Cualquier palabra que no empiece con «s»", "Se acepta toda palabra que empiece con otro sonido."),
        ],
    },
    context=[ex("Llega la educadora tradicional y dice una palabra de su lengua por primera vez. Ana empieza a repetirla en voz alta enseguida. ¿Qué podría hacer mejor?", "Escuchar con atención hasta que termine", "Escuchar primero permite repetir el sonido como corresponde.")],
    selfcheck=[
        ex("¿Se repite un sonido antes o después de escucharlo bien?", "Después", "Primero se escucha."),
        ex("¿Qué es el contexto de un sonido?", "La palabra o frase donde está", "Es el lugar donde aparece el sonido."),
        ex("¿Quién es el modelo para los sonidos de una lengua indígena?", "El educador/a tradicional o un hablante competente", "Ellos hablan la lengua."),
    ],
    open_task=task(
        "Con un adulto de tu casa juega a distinguir sonidos en castellano. Él dice estos pares, uno por uno: «mesa / pesa», «sol / mol» y «pato / gato». Tú dices en cuál sonido cambian (el del comienzo o el del medio). Anota tus tres respuestas. Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿cuáles son los primeros sonidos de la lengua de su pueblo que debemos aprender a escuchar?",
        "Mesa y pesa cambian en el comienzo. Sol y mol cambian en el comienzo. Pato y gato cambian en el comienzo. Mi pregunta: ¿qué sonidos de la lengua debemos escuchar primero?",
        ["escucha antes de decir", "distingue dónde cambia el sonido", "escribe una pregunta para el educador/a tradicional"],
        ["tres respuestas anotadas", "pregunta escrita"],
        ["responder sin escuchar completo", "burlarse de sonidos nuevos"],
        "Reconoce que distinguió el sonido en contexto y pide anotar la pregunta para quien habla la lengua.",
    ),
    reinforce="Pide a alguien que diga tres pares de palabras parecidas y di en cuál sonido cambian.",
    extend="Inventa tres pares de palabras en castellano que cambien solo en el primer sonido y léelos a un adulto.",
)

# ---------------------------------------------------------------- Clase 2
register(
    OA, 2,
    materials="Este cuaderno, lápiz y, si tienes, un espejo pequeño. Los sonidos de práctica son del castellano.",
    use="Aprenderé a observar cómo se produce un sonido con la boca, los labios, la lengua y el aire, sin hacer burla. Sirve para ensayar sonidos nuevos con cuidado y respeto.",
    prior=["Sé escuchar un sonido con atención.", "Sé mover los labios y la lengua."],
    explain=[
        "Los sonidos se producen con la boca. Los labios se juntan para decir «m» y «p». La lengua toca detrás de los dientes para «t». Para la «s», el aire sale por los dientes como un soplido suave. Observar esto te ayuda a ensayar.",
        "Puedes observar mirando a quien habla o mirándote en un espejo. Fíjate si los labios están juntos o separados, si la boca está muy abierta o casi cerrada, y si sale aire fuerte o suave. No hace falta exagerar ni hacer muecas.",
        "No caricaturizar significa no imitar de forma graciosa ni exagerada cómo habla una persona o un pueblo. Cuando ensayas un sonido de una lengua indígena, lo haces con seriedad y con la guía del hablante. Así cuidas la lengua y a quien la habla.",
    ],
    vocab=[("articulación", "cómo se mueven la boca, la lengua y los labios para hacer un sonido"), ("labios", "los bordes de la boca"), ("lengua", "parte blanda dentro de la boca que se mueve"), ("aire", "lo que sale al hablar"), ("caricaturizar", "imitar de forma exagerada para hacer burla")],
    worked=[
        {"title": "Observar la «m»", "problem": "Mírate al espejo y di «mamá». ¿Qué hacen los labios en la «m»?", "steps": ["Digo «mamá» despacio.", "Miro mis labios.", "Se juntan y se separan al decir «m»."], "answer": "Los labios se juntan"},
        {"title": "Imitar con respeto", "problem": "Un niño imita con muecas graciosas cómo habla la educadora tradicional. ¿Qué pasó?", "steps": ["Exagera su forma de hablar para hacer reír.", "Eso es caricaturizar.", "Debe observar con seriedad y ensayar con cuidado."], "answer": "Caricaturizó; debe ensayar con seriedad"},
    ],
    mistakes=[
        {"wrong": "Exagerar la boca para imitar a un hablante.", "why": "Es caricaturizar y puede ofender.", "fix": "Observa los movimientos sin exagerar."},
        {"wrong": "Ensayar un sonido sin mirar cómo lo hace el hablante.", "why": "Pierdes la pista de dónde van los labios y la lengua.", "fix": "Mira primero a quien habla, luego ensaya."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué hacen los labios al decir «p»?", "Se juntan", "La «p» se hace juntando los labios."),
            ex("Para decir «t», ¿dónde toca la lengua: detrás de los dientes o en la nariz?", "Detrás de los dientes", "La lengua toca arriba, detrás de los dientes."),
            ex("¿Qué significa caricaturizar?", "Imitar de forma exagerada para burlarse", "Caricaturizar exagera para hacer burla."),
        ],
        "understand": [
            ex("¿Por qué no hay que hacer muecas al ensayar sonidos de otra lengua?", "Porque es caricaturizar y falta el respeto", "Las muecas exageran y pueden ofender."),
            ex("¿Cómo puedes observar cómo se produce un sonido: con un espejo o mirando a quien habla?", "Con las dos formas", "Ambas permiten ver labios y boca."),
            ex("En la «s», ¿qué sale por los dientes?", "El aire", "La «s» es aire que sale suave."),
        ],
        "apply": [
            ex("Di «ofa» (la sílaba «fa»). ¿Qué dientes tocan el labio de abajo en la «f»?", "Los dientes de arriba", "En la «f» los dientes de arriba tocan el labio inferior."),
            ex("Di «ma» y «pa». ¿Qué hacen igual los labios en las dos?", "Se juntan", "Ambas empiezan con los labios juntos."),
            ex("Di «a», «i», «u». ¿En cuál la boca está más abierta?", "En la «a»", "La «a» necesita la boca más abierta."),
        ],
        "reason": [
            ex("Pedro imita la forma de hablar de un hablante y los demás se ríen. ¿Está bien?", "No", "Es burlarse de la persona y de su lengua."),
            ex("Una niña observa los labios del educador tradicional con atención y después ensaya en voz baja. ¿Hizo bien?", "Sí", "Observó primero y ensayó con cuidado."),
        ],
        "challenge": [
            ex("Di «m», «p» y «b». ¿En cuántas de las tres se juntan los labios?", "3", "En las tres los labios se juntan."),
            ex("Escribe una cosa que observes en tu boca al decir «sol».", "Por ejemplo, el aire sale por los dientes", "Se acepta una observación real de dientes, lengua o aire."),
        ],
    },
    context=[ex("Un invitado habla una lengua indígena y Tomás dice: «Mira cómo suena, qué raro». ¿Qué le dirías?", "Que escuche con respeto sin burlarse", "Una lengua distinta no es algo para reírse.")],
    selfcheck=[
        ex("¿Qué hacen los labios al decir «m»?", "Se juntan", "La «m» se hace con los labios juntos."),
        ex("¿Está bien exagerar una forma de hablar para hacer reír?", "No", "Eso es caricaturizar."),
        ex("¿Qué usas para observar tu boca: un espejo o un cuchillo?", "Un espejo", "El espejo permite ver los labios."),
    ],
    open_task=task(
        "Mírate al espejo, o pide a un adulto que te mire, y di estas tres palabras en castellano muy despacio: «mamá», «tomate» y «fuego». Anota qué haces con la boca en la primera letra de cada una (labios juntos, dientes de arriba en el labio de abajo, o lengua detrás de los dientes). Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿cómo debo mover la boca para ensayar los sonidos de la lengua de su pueblo sin burlarme?",
        "En mamá los labios se juntan. En tomate la lengua toca detrás de los dientes. En fuego los dientes de arriba tocan el labio de abajo. Mi pregunta: ¿cómo debo mover la boca para ensayar los sonidos de la lengua?",
        ["observa sin exagerar", "describe labios, lengua o aire", "pregunta al educador/a tradicional"],
        ["tres observaciones anotadas", "pregunta escrita"],
        ["hacer muecas", "imitar para reírse"],
        "Reconoce la observación de la articulación y pide ensayar con la guía de quien habla la lengua.",
    ),
    reinforce="Di tres palabras frente a un espejo y describe lo que hacen tus labios en la primera letra.",
    extend="Compara cómo se mueve tu boca en la «a» y en la «u» y dibuja las dos bocas.",
)

# ---------------------------------------------------------------- Clase 3
register(
    OA, 3,
    materials="Este cuaderno, lápiz y tarjetas que puedes dibujar con una palabra y su significado. La palabra verificada por el educador la escribe el educador.",
    use="Aprenderé a relacionar un sonido o palabra con su significado cuando la verifica el educador/a tradicional. Sirve para saber qué dice una palabra y no solo cómo suena.",
    prior=["Sé que las palabras tienen un significado.", "Sé escuchar un sonido con atención."],
    explain=[
        "Una palabra no es solo un sonido: tiene un significado. Para entenderla hay que saber qué quiere decir y cuándo se usa. Por eso se dibuja o se muestra junto a un objeto, un gesto o una situación.",
        "Una palabra verificada es una palabra que el educador tradicional, un hablante competente o la comunidad confirmó. Solo con esa verificación puedes asegurar su significado. Si no estás seguro, no la uses ni adivines lo que quiere decir.",
        "Una buena tarjeta de significado tiene tres partes: la palabra tal como la enseñó quien habla la lengua, un dibujo o gesto que muestra su significado, y el nombre de quién la verificó. Así sabes de dónde viene y a quién preguntar.",
    ],
    vocab=[("significado", "lo que quiere decir una palabra"), ("palabra verificada", "palabra confirmada por un hablante o por la comunidad"), ("tarjeta de significado", "ficha con palabra, dibujo y quién la verificó"), ("adivinar", "decir sin saber lo que creo que es"), ("fuente", "persona o lugar de donde viene lo que sé")],
    worked=[
        {"title": "Saludo verificado", "problem": "En una comunidad mapuche, la educadora tradicional saluda al curso con «mari mari» y dice que es un saludo. ¿Qué significa para tu tarjeta?", "steps": ["La educadora dijo «mari mari».", "Ella explicó que es un saludo.", "Puedo anotar: palabra «mari mari», significado: saludo, fuente: la educadora."], "answer": "«mari mari» es un saludo, según la educadora"},
        {"title": "No adivinar", "problem": "Oyes una palabra nueva que nadie te explicó. Un compañero dice: «Seguro significa casa». ¿Qué haces?", "steps": ["Nadie verificó ese significado.", "Adivinar puede ser un error.", "Pregunto al educador/a tradicional qué quiere decir."], "answer": "No lo anoto; pregunto al educador/a tradicional"},
    ],
    mistakes=[
        {"wrong": "Adivinar el significado de una palabra por cómo suena.", "why": "Puede significar algo muy distinto.", "fix": "Pregunta a quien la habla y anota que él la verificó."},
        {"wrong": "Escribir una tarjeta sin anotar quién verificó la palabra.", "why": "No se sabe de dónde viene la información.", "fix": "Anota la fuente en la tarjeta."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es el significado de una palabra?", "Lo que quiere decir", "El significado es lo que la palabra quiere decir."),
            ex("¿Qué dice «mari mari» según la educadora de la comunidad mapuche del ejemplo?", "Es un saludo", "La educadora explicó que es un saludo."),
            ex("¿Qué debes hacer si no sabes qué significa una palabra: adivinar o preguntar?", "Preguntar", "Adivinar puede equivocar el significado."),
        ],
        "understand": [
            ex("¿Qué es una palabra verificada?", "Una palabra confirmada por un hablante o la comunidad", "Alguien que la habla confirmó su significado."),
            ex("¿Por qué anotar la fuente en la tarjeta?", "Para saber quién la verificó", "La fuente dice de dónde viene el dato."),
            ex("¿Cuántas partes tiene una buena tarjeta de significado: dos, tres o diez?", "Tres", "Tiene palabra, dibujo o gesto, y fuente."),
        ],
        "apply": [
            ex("La tarjeta dice: palabra «agua», dibujo de un vaso con agua, fuente: la profesora. ¿Qué significa «agua» en la tarjeta?", "Lo que se ve en el dibujo: agua", "El dibujo muestra el significado."),
            ex("Completa: «La educadora dijo que _______ es un saludo». Escribe la palabra que dijo la educadora del ejemplo.", "mari mari", "Es el saludo que dijo en el ejemplo."),
            ex("Ordena para hacer una tarjeta: a) dibujo del significado, b) palabra como la enseñó el hablante, c) nombre de quien la verificó. Escribe las letras en orden.", "b, a, c", "Primero va la palabra, luego el dibujo y al final la fuente."),
        ],
        "reason": [
            ex("Un compañero dice que una palabra nueva significa «perro» porque sonó parecido a otra. ¿Por qué no sirve?", "Porque nadie verificó su significado", "Por cómo suena no se puede asegurar qué significa."),
            ex("Una niña anota «mari mari: saludo» y dice: «me lo dijo la educadora». ¿Su tarjeta está bien hecha?", "Sí", "Tiene palabra, significado y fuente."),
        ],
        "challenge": [
            ex("Tienes tres tarjetas de práctica con palabras en castellano: «luna», «agua» y «árbol». ¿Cuántos dibujos necesitas para mostrar el significado de las tres?", "3", "Se necesita un dibujo por cada palabra."),
            ex("Escribe qué tres cosas debe tener tu tarjeta de significado.", "Palabra, dibujo o gesto y fuente", "Esas son las tres partes de la tarjeta."),
        ],
    },
    context=[ex("El educador tradicional te enseña un saludo. Quieres anotarlo en una tarjeta. ¿Qué anotas además de la palabra?", "Su significado y quién lo verificó", "Una tarjeta incluye significado y fuente.")],
    selfcheck=[
        ex("¿Qué significa «mari mari» en el ejemplo?", "Un saludo", "La educadora lo explicó."),
        ex("¿Adivinas el significado o lo preguntas?", "Lo pregunto", "Preguntar evita equivocarse."),
        ex("¿Qué parte de la tarjeta dice de dónde viene la palabra?", "La fuente", "La fuente nombra quién la verificó."),
    ],
    open_task=task(
        "Haz tres tarjetas de significado con palabras en castellano: «luna», «agua» y «mano». En cada una escribe la palabra, dibuja su significado y escribe quién la verificó (un adulto de tu casa). Después anota una pregunta para el educador/a tradicional o la comunidad: ¿qué palabras de la lengua de su pueblo puedo aprender primero, y cómo las anoto con su significado y su fuente?",
        "Mi tarjeta: palabra «luna», dibujo de una luna, fuente: mi mamá. Mi pregunta: ¿qué palabras de la lengua puedo aprender primero y cómo las anoto?",
        ["escribe la palabra", "dibuja su significado", "anota la fuente"],
        ["tres tarjetas", "pregunta escrita"],
        ["adivinar significados", "no anotar la fuente"],
        "Reconoce las tarjetas completas y sugiere pedir las palabras de la lengua directamente al educador/a tradicional.",
    ),
    reinforce="Haz una tarjeta de significado para una palabra que te enseñe un adulto y anota quién la verificó.",
    extend="Haz una tarjeta con un gesto en vez de dibujo para la palabra «saludo».",
)

# ---------------------------------------------------------------- Clase 4
register(
    OA, 4,
    materials="Este cuaderno y lápiz. Las palabras de práctica están en castellano.",
    use="Aprenderé a notar que las letras del castellano no siempre muestran bien un sonido de otra lengua. Sirve para no escribir ni decir un sonido como si fuera castellano cuando no lo es.",
    prior=["Sé que una letra y un sonido no son lo mismo.", "Sé escuchar un sonido con atención."],
    explain=[
        "En castellano, las letras y los sonidos no siempre coinciden. La palabra «queso» tiene cinco letras, pero cuatro sonidos, porque la «u» no se pronuncia. La palabra «hola» tiene cuatro letras, pero tres sonidos, porque la «h» no suena.",
        "Si pasa esto en castellano, también puede pasar con otras lenguas. Muchas lenguas indígenas tienen sonidos que el castellano no tiene. Si los escribes con letras castellanas, puedes cambiarlos sin darte cuenta y perder lo que la lengua quiere decir.",
        "Por eso, cuando escuches un sonido de una lengua indígena, no lo traduzcas a las letras que ya conoces. Escucha al hablante y pregunta cómo se escribe en la lengua. Muchos pueblos tienen su propia forma de escribir su lengua, y esa forma la enseña la comunidad.",
    ],
    vocab=[("letra", "signo que se escribe"), ("sonido", "lo que se oye al hablar"), ("coincidir", "ser lo mismo"), ("traducir", "pasar de una lengua a otra"), ("forma de escribir", "manera en que un pueblo escribe su lengua")],
    worked=[
        {"title": "Letras y sonidos en «queso»", "problem": "Cuenta las letras y los sonidos de «queso». Los sonidos son k, e, s, o.", "steps": ["Letras: q, u, e, s, o = 5.", "Sonidos: k, e, s, o = 4.", "La «u» no suena."], "answer": "5 letras y 4 sonidos"},
        {"title": "No traducir el sonido", "problem": "Un niño oye un sonido que no existe en castellano y escribe una letra castellana parecida. ¿Qué riesgo hay?", "steps": ["El sonido no es el mismo que el de la letra.", "Al escribirlo así, cambia el sonido.", "Debe preguntar al hablante cómo se escribe en su lengua."], "answer": "Cambia el sonido; debe preguntar cómo se escribe en la lengua"},
    ],
    mistakes=[
        {"wrong": "Pensar que cada letra del castellano suena siempre igual.", "why": "En «hola» la «h» no suena.", "fix": "Escucha el sonido y no solo mires la letra."},
        {"wrong": "Escribir un sonido de otra lengua con una letra castellana «parecida».", "why": "No es el mismo sonido.", "fix": "Pregunta al hablante cómo se escribe en su lengua."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas letras tiene «hola»?", "4", "Son h, o, l, a."),
            ex("¿Cuántos sonidos tiene «hola», si la «h» no suena?", "3", "Suenan o, l, a."),
            ex("¿Son iguales una letra y un sonido?", "No", "La letra se escribe y el sonido se oye."),
        ],
        "understand": [
            ex("¿Por qué «queso» tiene más letras que sonidos?", "Porque la «u» no suena", "La «u» se escribe pero no se pronuncia."),
            ex("¿Puede una lengua tener un sonido que el castellano no tiene?", "Sí", "Muchas lenguas tienen sonidos propios."),
            ex("¿Quién enseña cómo se escribe la lengua de un pueblo?", "La comunidad o el educador/a tradicional", "Ellos conocen cómo se escribe su lengua."),
        ],
        "apply": [
            ex("Cuenta las letras de «chico». Luego cuenta los sonidos si «ch» suena como uno solo: ch, i, k, o. Escribe: letras / sonidos.", "5 / 4", "Son 5 letras y 4 sonidos porque «ch» es un solo sonido."),
            ex("Cuenta las letras de «llave». Luego los sonidos si «ll» es uno solo: ll, a, v, e. Escribe: letras / sonidos.", "5 / 4", "«ll» son dos letras y un solo sonido."),
            ex("¿«Kilo» y «quilo» empiezan con el mismo sonido?", "Sí", "La «k» y la «qu» suenan igual."),
        ],
        "reason": [
            ex("Un niño oyó un sonido nuevo y escribió la letra «s» porque le pareció parecido. ¿Qué puede pasar?", "Que cambie el sonido sin darse cuenta", "La «s» castellana no es el sonido que oyó."),
            ex("Una compañera dice: «Si lo escribo con letras castellanas, ya lo escribí bien». ¿Tiene razón?", "No siempre", "Las letras castellanas no siempre muestran el sonido de otra lengua."),
        ],
        "challenge": [
            ex("En «guerra» la «u» no suena y la «rr» es un solo sonido (g, e, rr, a). Escribe: letras / sonidos.", "6 / 4", "Tiene 6 letras, pero suenan 4 sonidos."),
            ex("Escribe una palabra en castellano que tenga más letras que sonidos.", "Por ejemplo, queso, hola o chico", "Se acepta una palabra con h muda, ch, ll o qu."),
        ],
    },
    context=[ex("Un niño oye un sonido nuevo de la lengua indígena y dice: «Lo escribo con la letra más parecida». ¿Qué podrías sugerirle?", "Que pregunte cómo se escribe en la lengua", "Quien habla la lengua enseña cómo se escribe.")],
    selfcheck=[
        ex("¿Cuántos sonidos tiene «queso»?", "4", "Suenan k, e, s, o."),
        ex("¿La «h» de «hola» suena?", "No", "La «h» es muda en castellano."),
        ex("¿Se traduce el sonido a letras castellanas o se pregunta al hablante?", "Se pregunta al hablante", "Quien habla la lengua conoce el sonido."),
    ],
    open_task=task(
        "Cuenta con un adulto las letras y los sonidos de estas palabras en castellano: «queso» (5 letras, 4 sonidos), «hola», «llave» y «chico». Anota en una tabla letras y sonidos de cada una y marca cuál letra no suena o suena unida a otra. Luego pregunta al educador/a tradicional o a la comunidad: ¿cómo se escribe la lengua de su pueblo y qué sonidos no existen en castellano?",
        "Hola: 4 letras y 3 sonidos, la h no suena. Llave: 5 letras y 4 sonidos, ll es un sonido. Mi pregunta: ¿cómo se escribe la lengua del pueblo?",
        ["cuenta letras y sonidos", "marca la letra que no suena", "no traduce sonidos de otra lengua"],
        ["tabla de cuatro palabras", "pregunta escrita"],
        ["pensar que letra y sonido son lo mismo", "escribir sonidos de otra lengua con letras castellanas"],
        "Reconoce que letras y sonidos no coinciden y sugiere preguntar a quien habla la lengua.",
    ),
    reinforce="Elige tres palabras de tu casa y cuenta letras y sonidos de cada una.",
    extend="Busca una palabra con dos letras que suenan como un solo sonido y explica por qué.",
)

# ---------------------------------------------------------------- Clase 5
register(
    OA, 5,
    materials="Este cuaderno y lápiz. Las prácticas son con palabras en castellano y con lo que enseñe el educador/a tradicional.",
    use="Aprenderé a ensayar un sonido con apoyo y a respetar mi etapa de aprendizaje. Sirve para mejorar de a poco sin avergonzarme y sin burlarme de otros.",
    prior=["Sé escuchar un sonido con atención.", "Sé observar cómo se mueve la boca."],
    explain=[
        "Aprender a decir un sonido nuevo toma tiempo. Se hace por pasos: primero escuchas, luego lo dices muy bajito, después lo dices con el hablante y por último lo dices solo. No todos aprenden al mismo ritmo y eso está bien.",
        "Con apoyo quiere decir que alguien te ayuda: el educador tradicional dice el sonido, tú lo repites y él te dice si lo mejoraste. También puedes usar un espejo, tarjetas o señales como un pulgar arriba para saber si vas bien.",
        "Respetar tu etapa significa no exigirte que suene perfecto el primer día. Se mejora ensayando muchas veces. Y también respetas la etapa de tus compañeros: no te ríes si alguien se equivoca, porque todos están aprendiendo.",
    ],
    vocab=[("ensayar", "practicar algo varias veces"), ("apoyo", "ayuda de alguien"), ("etapa", "momento del aprendizaje en que estoy"), ("mejorar", "hacerlo cada vez un poco mejor"), ("equivocarse", "decir algo distinto de lo correcto")],
    worked=[
        {"title": "Pasos para ensayar", "problem": "El educador tradicional te enseña un sonido. Ordena los pasos: decirlo solo, escucharlo, decirlo con el hablante, decirlo bajito.", "steps": ["Primero escucho el sonido.", "Luego lo digo bajito.", "Después lo digo con el hablante.", "Por último lo digo solo."], "answer": "Escuchar, decir bajito, decir con el hablante, decir solo"},
        {"title": "Apoyar a un compañero", "problem": "Un compañero se equivoca al ensayar un sonido y alguien se ríe. ¿Qué debes hacer?", "steps": ["Reírse no ayuda a aprender.", "Todos estamos en etapas distintas.", "Puedo decir «tú puedes, inténtalo otra vez»."], "answer": "Animarlo y no reírme"},
    ],
    mistakes=[
        {"wrong": "Querer decir el sonido perfecto el primer día.", "why": "El aprendizaje toma tiempo.", "fix": "Ensaya poco a poco y celebra cada avance."},
        {"wrong": "Reírse cuando otro se equivoca.", "why": "Hace que los demás tengan vergüenza de ensayar.", "fix": "Anima con una frase amable."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué haces primero para ensayar un sonido: escucharlo o decirlo solo?", "Escucharlo", "Primero se escucha."),
            ex("¿Está bien equivocarse al ensayar un sonido nuevo?", "Sí", "Equivocarse es parte de aprender."),
            ex("Si un compañero se equivoca, ¿te ríes o lo animas?", "Lo animo", "Animar ayuda a aprender."),
        ],
        "understand": [
            ex("¿Qué quiere decir «con apoyo»?", "Que alguien me ayuda", "El apoyo es la ayuda de otra persona."),
            ex("¿Qué significa respetar mi etapa?", "No exigirme que suene perfecto el primer día", "Cada uno está en un momento distinto."),
            ex("¿Todos aprenden al mismo ritmo?", "No", "Cada persona aprende a su ritmo."),
        ],
        "apply": [
            ex("Ordena: a) decir solo, b) escuchar, c) decir con el hablante, d) decir bajito. Escribe las letras en orden.", "b, d, c, a", "Se pasa de escuchar a decir cada vez con más independencia."),
            ex("La educadora dice un sonido tres veces. Tú lo repites una vez después de cada una. ¿Cuántas veces lo repites?", "3", "Una repetición por cada vez que ella lo dice."),
            ex("Si ensayas un sonido 2 veces cada día durante 5 días, ¿cuántas veces ensayaste en total?", "10", "2 + 2 + 2 + 2 + 2 = 10."),
        ],
        "reason": [
            ex("Ema no quiere ensayar porque teme equivocarse. ¿Qué le dirías?", "Que todos aprendemos poco a poco", "Equivocarse es normal y no debe dar vergüenza."),
            ex("Dos niños dicen un sonido con distinto avance. ¿Alguno está haciendo algo mal?", "No", "Cada uno está en su etapa."),
        ],
        "challenge": [
            ex("Un niño ensayó un sonido 3 veces el lunes, 4 el martes y 5 el miércoles. ¿Cuántas veces ensayó en total?", "12", "3 + 4 + 5 = 12."),
            ex("Escribe una frase amable para animar a alguien que ensaya un sonido.", "Cualquier frase amable", "Se acepta una frase que anime sin burlarse."),
        ],
    },
    context=[ex("En clase, la educadora tradicional enseña un sonido. Juan lo dice distinto y un compañero se ríe. ¿Qué podría hacer la clase?", "Animar a Juan e intentarlo de nuevo", "La clase aprende apoyándose entre todos.")],
    selfcheck=[
        ex("¿Qué es ensayar?", "Practicar varias veces", "Ensayar es repetir para mejorar."),
        ex("¿Qué haces si alguien se equivoca?", "Lo animo", "Animar ayuda a seguir aprendiendo."),
        ex("¿Se puede mejorar con el tiempo?", "Sí", "Con práctica se mejora."),
    ],
    open_task=task(
        "Elige un sonido en castellano que te cueste, por ejemplo la «r» fuerte de «perro» o la «ch» de «chico», y ensáyalo cinco veces con un adulto que te anime. Anota con una marca cada vez que lo ensayaste y cómo te sentiste. Pregunta al educador/a tradicional o a la comunidad qué sonido de la lengua de su pueblo debes ensayar primero y quién puede ayudarte.",
        "Ensayé la «r» de perro cinco veces con mi papá (marqué cinco rayitas). Me sentí contento. Mi pregunta: ¿qué sonido de la lengua debo ensayar primero?",
        ["ensaya varias veces", "respeta su etapa", "pregunta al educador/a tradicional"],
        ["cinco marcas", "nota de cómo se sintió", "pregunta escrita"],
        ["querer sonar perfecto de inmediato", "reírse de otros"],
        "Reconoce el ensayo repetido y valora la pregunta al educador/a tradicional.",
    ),
    reinforce="Ensaya un sonido de tu casa tres días seguidos y marca cuántas veces lo hiciste.",
    extend="Anima a un compañero o familiar que ensaye un sonido nuevo con una frase amable.",
)

# ---------------------------------------------------------------- Clase 6
register(
    OA, 6,
    materials="Este cuaderno y lápiz. La expresión que se usa la valida el educador/a tradicional del curso.",
    use="Aprenderé a usar una expresión breve de la lengua indígena solo cuando fue validada y en el momento correcto. Sirve para saludar y participar con respeto.",
    prior=["Sé escuchar y ensayar un sonido con apoyo.", "Sé que una palabra tiene significado y fuente."],
    explain=[
        "Una expresión breve es una frase corta, como un saludo. «Mari mari» es un saludo en mapuzugun, la lengua del pueblo mapuche. Otras lenguas tienen sus propios saludos y los enseñan sus hablantes. No se mezclan ni se inventan.",
        "Solo se usa una expresión cuando fue validada, es decir, cuando el educador tradicional o la comunidad dijo que está bien dicha y que se puede usar. También hay que saber cuándo: un saludo se usa al encontrarse con alguien, no en cualquier momento.",
        "Si no estás seguro de si puedes usar la expresión, pregunta antes. Usar una frase fuera de contexto, por broma o con otro significado puede ofender. Cuando usas bien la expresión, muestras respeto por la lengua y por las personas que la hablan.",
    ],
    vocab=[("expresión", "frase corta que se usa en una situación"), ("validar", "confirmar que algo está bien y se puede usar"), ("ocasión", "el momento adecuado para usar una expresión"), ("saludo", "palabra o frase para recibir a alguien"), ("broma", "algo que se dice para reír")],
    worked=[
        {"title": "Usar el saludo validado", "problem": "La educadora tradicional mapuche enseñó «mari mari» como saludo y dijo que el curso puede decirlo al verla. Llega la educadora. ¿Qué haces?", "steps": ["El saludo está validado por ella.", "Es el momento correcto: nos encontramos.", "Digo «mari mari» con respeto y miro a la persona."], "answer": "Digo «mari mari» al verla"},
        {"title": "No usar fuera de contexto", "problem": "Tomás dice «mari mari» riéndose cuando se le cae un lápiz. ¿Qué está mal?", "steps": ["«Mari mari» es un saludo.", "Se cayó un lápiz, no hay un encuentro.", "Lo usa por broma y sin respeto."], "answer": "Lo usó fuera de contexto y como broma"},
    ],
    mistakes=[
        {"wrong": "Usar la expresión en cualquier momento.", "why": "Cada expresión tiene una ocasión.", "fix": "Úsala solo cuando corresponde, por ejemplo al saludar."},
        {"wrong": "Decirla de broma.", "why": "Burla de la lengua y de quienes la hablan.", "fix": "Dila con seriedad y respeto."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es «mari mari»?", "Un saludo en mapuzugun", "Es un saludo de la lengua mapuche."),
            ex("¿Cuándo se usa un saludo: al encontrarte con alguien o cuando se cae un lápiz?", "Al encontrarte con alguien", "Un saludo es para recibir a alguien."),
            ex("¿Quién dice si una expresión se puede usar: la educadora tradicional o un compañero?", "La educadora tradicional", "Ella la valida."),
        ],
        "understand": [
            ex("¿Qué significa que una expresión está validada?", "Que fue confirmada por la educadora o la comunidad", "Alguien que conoce la lengua dijo que se puede usar."),
            ex("¿Por qué no se usa una expresión de broma?", "Porque falta el respeto a la lengua", "Es burla de las personas que la hablan."),
            ex("¿Qué debes hacer si no sabes cuándo usar una expresión?", "Preguntar", "Preguntar evita errores."),
        ],
        "apply": [
            ex("Llega la educadora al curso. ¿Dices «mari mari» o dices algo inventado?", "«mari mari»", "Solo se usa lo validado."),
            ex("Termina la clase y la educadora se va. ¿Inventas una despedida en su lengua o esperas a que ella te enseñe cómo despedirte?", "Espero a que me enseñen", "No se inventa una despedida."),
            ex("Hay 4 niñas que saludan a la educadora una por una con «mari mari». ¿Cuántas veces se escucha el saludo?", "4", "Una vez por cada niña."),
        ],
        "reason": [
            ex("Un niño usa «mari mari» para hacer reír a sus amigos. ¿Qué le dirías?", "Que es un saludo y se usa con respeto", "No es una broma."),
            ex("Una niña pregunta si puede usar un saludo que oyó en un video. ¿Qué debe hacer?", "Preguntar al educador/a tradicional", "No sabe si está validado ni de qué pueblo es."),
        ],
        "challenge": [
            ex("Hay tres situaciones: a) llega la educadora, b) se cae un lápiz, c) un amigo llega a la sala. ¿En cuáles puedes usar un saludo validado? Escribe las letras.", "a y c", "El saludo se usa al encontrarte con alguien."),
            ex("Escribe una frase que explique cuándo se usa un saludo.", "Cualquier frase que diga que se usa al encontrarse con alguien", "Se acepta una frase que relacione saludo y encuentro."),
        ],
    },
    context=[ex("Tu curso recibe al educador tradicional. Una niña no sabe si puede saludarlo con «mari mari». ¿Qué debe hacer?", "Preguntar si ese es el saludo de su pueblo y si puede usarlo", "Cada pueblo tiene su saludo y se pregunta antes.")],
    selfcheck=[
        ex("¿«Mari mari» es una broma o un saludo?", "Un saludo", "Se usa para recibir a alguien."),
        ex("¿Quién valida una expresión de la lengua?", "El educador/a tradicional o la comunidad", "Ellos conocen la lengua."),
        ex("¿Usas el saludo en cualquier momento o al encontrarte con alguien?", "Al encontrarme con alguien", "Es la ocasión del saludo."),
    ],
    open_task=task(
        "Con un adulto practica el saludo de la clase: tú entras a una habitación, el adulto está ahí y tú lo saludas con respeto. Si tu curso aprendió «mari mari» con el educador/a tradicional, úsalo; si no, usa el saludo que él te enseñó. Si todavía no tienes uno, practica un saludo en castellano con calma. Escribe cuándo usaste el saludo y qué cuidaste. Pregunta al educador/a tradicional o a la comunidad cuál es el saludo del pueblo de tu territorio y en qué momentos se usa.",
        "Entré a la cocina y saludé a mi abuela con respeto. Cuidé mirarla y no reírme. Mi pregunta: ¿cuál es el saludo del pueblo de mi territorio y cuándo se usa?",
        ["usa una expresión validada", "la usa en el momento adecuado", "pregunta al educador/a tradicional"],
        ["nota de cuándo la usó", "pregunta escrita"],
        ["usarla de broma", "inventar una expresión"],
        "Valora el saludo en el momento adecuado y el cuidado puesto, y recuerda preguntar al educador/a tradicional.",
    ),
    reinforce="Saluda con respeto a tres personas de tu casa, mirándolas a los ojos.",
    extend="Explica a un familiar por qué un saludo no se usa de broma.",
)

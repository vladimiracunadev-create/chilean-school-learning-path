"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS01 (disfrutar y comprender relatos fundacionales o cosmogónicos de diferentes pueblos indígenas en Chile y de
otras culturas significativas para su contexto, comentando la importancia que tienen para los pueblos a los que
pertenecen).

Criterio de autoría: NO se reproduce ni se adapta ningún relato real de ningún pueblo. Todos los relatos del cuaderno son
inventados solo para practicar, están rotulados como tales y no pertenecen a ningún pueblo. Se nombran únicamente, como
datos generales, dos relatos muy difundidos: el relato mapuche de Tren Tren y Kai Kai (dos serpientes, asociado a una
gran inundación) y la tradición rapa nui de la llegada del jefe Hotu Matu'a a la isla; no se cuenta su contenido ni se
explican sus sentidos, que enseñan el educador/a tradicional y la comunidad. No se interpretan significados espirituales.
Los textos reales de relatos (y de otras culturas) quedan para el docente, con permiso de la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS1 = "LC05 OA LS01"

CONSULT = " Recuerda: los relatos de cada pueblo los cuentan y explican el educador o la educadora tradicional y las personas de la comunidad. Pregúntales antes de dar tu trabajo por terminado, y no uses un relato real sin su permiso."
FEEDBACK_ADD = " Si surge una duda sobre un relato real o su sentido, no responder desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No pedir a ningún estudiante que cuente el relato de su familia."


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


RA = "Relato de práctica A (inventado; no es de ningún pueblo): Cuentan que al principio solo existía la neblina. De la neblina nació una montaña, y de la montaña bajó un río. El río llegó a un valle y de sus orillas salieron las primeras personas. Por eso, dicen, la gente cuida el río: es su origen."
RB = "Relato de práctica B (inventado; no es de ningún pueblo): Se dice que al principio el mundo era un mar oscuro. Una gran ave dejó caer una pluma y la pluma se hizo isla. En la isla crecieron los primeros árboles y a su sombra aparecieron las primeras personas. Por eso, dicen, la gente no corta un árbol sin agradecerle."

# ============================================================ LS01 clase 1 · situar pueblo, territorio y fuente
L(
    LS1, 1,
    materials="Lápiz y hoja. Los relatos están escritos aquí y son inventados para practicar. Los relatos reales los cuenta el educador o la educadora tradicional.",
    use="Aprenderé qué es un relato fundacional o cosmogónico y cómo ubicar de qué pueblo, territorio y fuente viene. Sirve para escuchar relatos con respeto y sin mezclar pueblos.",
    prior=["Sé ubicar pueblo, territorio y fuente.", "Sé que cada pueblo tiene su propia lengua y sus propias narraciones."],
    explain=[
        "Un relato fundacional cuenta cómo nació o se fundó un pueblo o un lugar. Un relato cosmogónico cuenta cómo se originó el mundo, es decir, de dónde vino todo lo que existe. Muchos pueblos indígenas de Chile y muchas otras culturas tienen relatos así. Se transmiten sobre todo por la oralidad: personas mayores o educadores tradicionales los cuentan a las nuevas generaciones.",
        "Para conocer un relato real, primero lo ubico: ¿de qué pueblo es?, ¿de qué territorio?, ¿quién me lo cuenta y con qué permiso? Por ejemplo, el relato de Tren Tren y Kai Kai es muy conocido en el pueblo mapuche, y la tradición oral rapa nui recuerda la llegada del jefe Hotu Matu'a a la isla. Cómo se cuentan y qué significan esos relatos lo enseñan sus educadores tradicionales, no yo.",
        "En este cuaderno practico con relatos inventados, que están rotulados y no pertenecen a ningún pueblo. Así aprendo a leerlos sin copiar ni cambiar relatos reales. Si me preguntan por un relato de otro pueblo o cultura, digo de dónde viene y cuál es mi fuente. Si no la tengo, digo «no lo sé» y pregunto.",
    ],
    vocab=[("relato fundacional", "cuenta cómo nació o se fundó un pueblo o un lugar"), ("relato cosmogónico", "cuenta cómo se originó el mundo"), ("oralidad", "transmitir saberes hablando, de persona a persona"), ("tradición oral", "relatos y saberes que pasan de generación en generación hablando"), ("origen", "el comienzo de algo")],
    worked=[
        W("Clasificar un relato", RA + " ¿Es un relato fundacional, cosmogónico o ambos?", ["Cuenta cómo se originó el mundo: la neblina, la montaña, el río.", "También cuenta cómo aparecieron las primeras personas.", "Tiene origen del mundo y de la gente."], "es cosmogónico (origen del mundo) y fundacional (origen de las primeras personas)"),
        W("Ubicar la fuente", "Un niño dice: «Mi vecina me contó un relato de origen, pero no sé de qué pueblo ni dónde». ¿Qué falta para ubicar el relato?", ["Reviso los datos que se piden: pueblo, territorio, fuente y permiso.", "Tiene fuente (la vecina), pero no pueblo ni territorio.", "Faltan pueblo y territorio, y el permiso."], "faltan pueblo, territorio y permiso"),
    ],
    mistakes=[
        M("Decir que un relato inventado de este cuaderno es un relato mapuche o de otro pueblo.", "Está rotulado como inventado y no pertenece a nadie.", "Digo «relato de práctica» y no lo asigno a ningún pueblo."),
        M("Contar un relato real de memoria, como lo recuerdo, sin permiso.", "Puedo cambiarlo y los relatos tienen quienes los cuentan.", "Pido que lo cuente el educador tradicional o la comunidad."),
    ],
    R=[
        ex(RA + " ¿Qué había al principio, según el relato A?", "solo neblina", "La primera oración lo dice."),
        ex(RA + " ¿Qué bajó de la montaña?", "un río", "El relato lo dice."),
        ex("Un relato cosmogónico, ¿cuenta cómo se originó el mundo o cómo se prepara una comida?", "cómo se originó el mundo", "Así se definió cosmogónico."),
    ],
    C=[
        ex("¿Un relato fundacional cuenta cómo nació o se fundó un pueblo o un lugar, o cuenta un partido de fútbol?", "cómo nació o se fundó un pueblo o un lugar", "Así se definió fundacional."),
        ex("¿Los relatos del cuaderno A y B pertenecen a algún pueblo indígena? Sí o No.", "No", "Están rotulados como inventados."),
        ex("El relato de Tren Tren y Kai Kai es muy conocido en un pueblo de Chile. ¿Cuál: mapuche o aymara?", "mapuche", "Así lo dice la explicación."),
    ],
    A=[
        ex(RB + " ¿Qué dejó caer la gran ave?", "una pluma", "El relato B lo dice."),
        ex("Une cada relato con su origen que cuenta: A) relato A, B) relato B. Orígenes: 1) una pluma que se hizo isla, 2) una montaña de la que baja un río. Escribe los dos pares.", "A-2, B-1", "El relato A tiene la montaña y el relato B la pluma."),
        arith("Un curso lee 4 relatos inventados el lunes y 3 el martes. ¿Cuántos relatos leyó en los dos días?", "4+3", "Se suman los de los dos días."),
    ],
    Z=[
        ex("Una niña escribe: «Todos los pueblos indígenas cuentan el mismo relato del origen». ¿Es una generalización? Sí o No.", "Sí", "Cada pueblo tiene sus propios relatos."),
        ex("Quieres conocer un relato real de tu comunidad. ¿Qué es mejor: A) pedir al educador o educadora tradicional que lo cuente o B) escribirlo tú de memoria?", "A", "Quien conoce el relato lo cuenta con su sentido."),
    ],
    D=[
        ex(RA + " " + RB + " ¿En cuál de los dos relatos aparecen árboles: A o B?", "B", "El relato B dice que en la isla crecieron los primeros árboles; el A no los nombra."),
        ex("Ordena para ubicar un relato real: A) cuento solo lo que me autorizan. B) pregunto de qué pueblo y territorio es. C) pregunto quién lo cuenta. Escribe las letras en orden.", "B, C, A", "Primero ubico pueblo y territorio, luego la fuente y al final cuento con permiso."),
    ],
    context=[ex("Una familia de tu escuela cuenta un relato de su cultura. ¿Escuchas con atención y preguntas respetuosamente o lo corriges porque no es como tú lo sabes?", "escuchas con atención y preguntas respetuosamente", "Cada familia o comunidad tiene su forma de contar.")],
    selfcheck=[
        ex("¿Un relato que explica cómo se originó el mundo es cosmogónico o fundacional?", "cosmogónico", "Cosmogónico habla del origen del mundo."),
        ex("Los relatos de este cuaderno, ¿son inventados para practicar? Sí o No.", "Sí", "Están rotulados así."),
        ex("Si no sé de qué pueblo es un relato, ¿lo cuento igual? Sí o No.", "No", "Sin pueblo ni fuente no se debe contar."),
    ],
    task=T(
        "Lee el relato de práctica C (inventado; no es de ningún pueblo): «Dicen que en el principio solo había viento. El viento sopló y levantó una duna. Detrás de la duna se abrió una laguna y a su orilla nacieron las primeras personas.» En tu cuaderno completa una ficha: ¿es fundacional, cosmogónico o ambos?, ¿qué origen cuenta?, ¿qué dato falta para ubicarlo como un relato de un pueblo real? Termina con una pregunta que le harías al educador o educadora tradicional sobre los relatos de tu comunidad.",
        "Es cosmogónico y fundacional: cuenta el origen del mundo (viento, duna, laguna) y de las primeras personas. Falta el pueblo, el territorio y la fuente, porque es un relato de práctica. Pregunta: ¿qué relatos de origen se cuentan en nuestra comunidad y quién puede contarlos?",
        ["clasifica el relato", "dice qué origen cuenta", "nombra los datos que faltan", "formula una pregunta"],
        ["ficha de tres respuestas", "pregunta escrita o dicha en voz alta"],
        ["asignarlo a un pueblo real", "inventar fuente"],
        "Si lo asignó a un pueblo, pídele que explique por qué no puede saberlo.",
    ),
    reinforce="Relee los relatos A y B y subraya con lápiz qué origen cuenta cada uno.",
    extend="Inventa un relato de práctica de cuatro oraciones sobre el origen de una laguna y rotúlalo como inventado.",
)

# ============================================================ LS01 clase 2 · escuchar o leer con límites declarados
RC2 = "Relato de práctica D (inventado; no es de ningún pueblo): Dicen las personas mayores de un valle inventado que el primer sol salió de una laguna. Cuando salió, el valle se llenó de luz y los animales despertaron. Desde entonces, cuentan, la gente saluda al día con respeto. Una abuela inventada aclara: «Así me lo contaron a mí; otras familias lo cuentan de otra manera»."

L(
    LS1, 2,
    materials="Lápiz y hoja. El relato está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta en voz alta.",
    use="Aprenderé a escuchar o leer un relato fundacional con atención, a disfrutarlo y a distinguir lo que cuenta, quién lo cuenta y qué límites declara. Sirve para comprender un relato sin cambiarlo.",
    prior=["Sé que un relato fundacional cuenta un origen.", "Sé que los relatos se transmiten oralmente."],
    explain=[
        "Escuchar un relato es una forma de respeto. Primero escucho completo sin interrumpir. Después recuerdo el orden de lo que pasa: qué ocurrió primero, qué después y cómo termina. Un relato fundacional suele tener una secuencia: un comienzo, un cambio y una consecuencia, que explica por qué hoy la gente hace algo.",
        "En un relato aparecen señales de que es contado por la tradición: «dicen», «cuentan», «se dice». Esas palabras muestran que el relato viene de otras personas y no lo inventó quien lo cuenta. También hay límites declarados: la abuela del relato D aclara que es la versión que ella escuchó y que otras familias lo cuentan distinto. Respeto ese límite.",
        "Puedo disfrutar un relato: imaginar el valle, la laguna y la luz, y decir qué me gustó. Lo que no hago es agregar explicaciones espirituales ni significados que nadie me dijo. Si quiero saber qué significa algo para el pueblo al que pertenece, lo pregunto a quien lo cuenta o al educador o educadora tradicional.",
    ],
    vocab=[("secuencia", "orden en que ocurren los hechos"), ("consecuencia", "lo que ocurre después de un hecho"), ("versión", "forma en que una familia o comunidad cuenta un relato"), ("límite declarado", "aviso de hasta dónde vale lo que se cuenta"), ("disfrutar", "sentir gusto al escuchar o leer")],
    worked=[
        W("Ordenar la secuencia", RC2 + " ¿Qué pasa justo después de que sale el primer sol?", ["Busco la parte donde sale el sol.", "Dice que el valle se llenó de luz.", "Y los animales despertaron."], "el valle se llenó de luz y los animales despertaron"),
        W("Reconocer el límite", RC2 + " ¿Qué límite declara la abuela?", ["Busco lo que ella aclara.", "Dice que así se lo contaron a ella.", "Y que otras familias lo cuentan de otra manera."], "es la versión que ella escuchó y otras familias lo cuentan distinto"),
    ],
    mistakes=[
        M("Agregar «y esto significa que el sol es sagrado» porque me parece lógico.", "Nadie lo dijo en el relato.", "Cuento solo lo que dice y pregunto por el sentido a quien lo enseña."),
        M("Pensar que mi versión de un relato es la única verdadera.", "Otras familias lo cuentan de otra manera.", "Digo «según como me lo contaron»."),
    ],
    R=[
        ex(RC2 + " ¿De dónde salió el primer sol, según el relato D?", "de una laguna", "El relato lo dice."),
        ex(RC2 + " ¿Qué hicieron los animales cuando salió el sol?", "despertaron", "El relato lo dice."),
        ex(RC2 + " ¿Quién aclara que otras familias lo cuentan distinto: una abuela o un niño?", "una abuela", "El relato nombra a la abuela."),
    ],
    C=[
        ex(RC2 + " Según el relato, ¿qué hace la gente desde entonces?", "saluda al día con respeto", "Esa es la consecuencia que cuenta."),
        ex("En un relato, las palabras «dicen» o «cuentan», ¿muestran que viene de la tradición o que lo inventó quien lo cuenta?", "que viene de la tradición", "Señalan que otras personas lo contaron antes."),
        ex(RC2 + " Verdadero o falso: el relato dice que todas las familias lo cuentan igual.", "Falso", "La abuela dice que otras lo cuentan de otra manera."),
    ],
    A=[
        ex("Ordena los hechos del relato D: A) los animales despiertan. B) el primer sol sale de la laguna. C) el valle se llena de luz. Escribe las letras en orden.", "B, C, A", "El sol sale, el valle se ilumina y los animales despiertan."),
        ex(RC2 + " Clasifica con H (hecho que cuenta el relato) o I (interpretación mía): 1) el sol salió de una laguna. 2) el sol es el dios de ese pueblo. 3) el valle se llenó de luz. Escribe las tres letras.", "1 H, 2 I, 3 H", "La 2 no aparece en el relato."),
        arith("Un relato tiene 5 oraciones. El curso subraya 3 como las más importantes. ¿Cuántas oraciones quedan sin subrayar?", "5-3", "Se restan las subrayadas del total."),
    ],
    Z=[
        ex(RC2 + " Una niña dice: «Este relato prueba lo que cree un pueblo indígena real». ¿Puede decir eso si el relato es inventado y no es de ningún pueblo? Sí o No.", "No", "No pertenece a ningún pueblo."),
        ex("Escuchas un relato real y no entiendes una palabra. ¿Qué es mejor: A) preguntar a quien lo cuenta o al educador tradicional, B) inventar qué quiere decir?", "A", "El sentido de las palabras lo enseña quien las conoce."),
    ],
    D=[
        ex(RC2 + " Elige el mejor resumen: A) «Según el relato D, el primer sol salió de una laguna, el valle se llenó de luz y desde entonces la gente saluda al día; la abuela aclara que otras familias lo cuentan distinto». B) «El relato prueba que el sol es sagrado». Escribe la letra.", "A", "A resume sin agregar ideas y mantiene el límite."),
        ex("Un compañero cuenta el relato D cambiando «laguna» por «mar». ¿Qué es lo correcto: A) corregirle con respeto según el texto o B) aceptar el cambio porque da igual?", "A", "El relato dice laguna y se cuenta como está escrito."),
    ],
    context=[ex("Una persona mayor cuenta un relato en tu escuela y dice «así lo escuché yo». ¿Repites luego «es el relato de todos» o dices «según como lo contó ella»?", "dices «según como lo contó ella»", "Respeta el límite que ella declaró.")],
    selfcheck=[
        ex("La secuencia de un relato, ¿es el orden en que ocurren los hechos? Sí o No.", "Sí", "Así se definió secuencia."),
        ex("¿Puedo agregar significados espirituales que nadie dijo? Sí o No.", "No", "Los significados los enseña quien corresponde."),
        ex("¿Qué palabra indica que algo viene de la tradición: «dicen» o «yo creo»?", "dicen", "«Dicen» muestra que otras personas lo cuentan."),
    ],
    task=T(
        "Lee este relato de práctica E (inventado; no es de ningún pueblo): «Cuentan que la primera lluvia cayó sobre una piedra grande. La piedra se abrió y salió una vertiente. De la vertiente nació una quebrada y a su orilla se formó el primer poblado. Una anciana inventada dice: «Así lo cuenta mi familia».» En tu cuaderno escribe: 1) los tres hechos en orden, 2) el límite que declara la anciana, 3) una frase que diga qué te gustó, marcada con «yo pienso». Termina con una pregunta para el educador o educadora tradicional.",
        "Hechos: cae la primera lluvia sobre una piedra; la piedra se abre y sale una vertiente; nace una quebrada y se forma el primer poblado. Límite: así lo cuenta su familia. Yo pienso que me gustó la imagen de la piedra que se abre. Pregunta: ¿cómo se cuentan los relatos de origen en nuestra comunidad?",
        ["ordena los hechos", "nombra el límite", "marca lo propio con «yo pienso»", "formula una pregunta"],
        ["tres hechos ordenados", "frase de «yo pienso»", "pregunta"],
        ["agregar significados", "borrar el límite"],
        "Verifica que cada hecho esté en el texto y que lo personal esté marcado.",
    ),
    reinforce="Relee el relato D y numera con 1, 2 y 3 los hechos en orden.",
    extend="Cuenta en voz alta a una persona de tu casa el relato D con tus palabras, sin cambiar los hechos, y dile el límite que declara la abuela.",
)

# ============================================================ LS01 clase 3 · relaciones culturales: importancia para un pueblo
TABLA3 = "Tabla de práctica (inventada): Relato A: origen en un río. Costumbre que explica: la gente cuida el río. Relato B: origen en una pluma que se hizo isla y en árboles. Costumbre que explica: la gente agradece a un árbol antes de cortarlo. Relato D: origen en el primer sol. Costumbre que explica: la gente saluda al día con respeto."

L(
    LS1, 3,
    materials="Lápiz y hoja. La tabla y los relatos están escritos aquí y son inventados para practicar. No necesitas dispositivos.",
    use="Aprenderé a comentar por qué un relato fundacional es importante para el pueblo que lo cuenta: qué explica, qué cuida y qué une a las personas. Sirve para explicar la importancia de los relatos con respeto.",
    prior=["Sé ubicar un relato con su fuente.", "Sé leer un relato con sus límites."],
    explain=[
        "Un relato fundacional no solo cuenta un origen. También conecta a las personas con su territorio, con su historia y entre ellas. Un pueblo puede ver en un relato su identidad: aquello que lo hace sentirse parte de algo común. Por eso los relatos son importantes y se cuentan con cuidado.",
        "Para comentar la importancia de un relato me hago tres preguntas. Primero, ¿qué origen cuenta? Segundo, ¿qué costumbre o cuidado se relaciona con él? Tercero, ¿a quién une o qué cuida? En la tabla de práctica, el relato A se relaciona con el cuidado del río: la gente cuida lo que considera su origen. Es un ejemplo inventado que me sirve para aprender a preguntar.",
        "Cuando se trata de un relato real, la importancia la dicen las personas del pueblo que lo cuentan. Yo no la adivino. Comento con frases como «según el educador tradicional, este relato es importante porque…». Y si no sé, digo «no lo sé» y pregunto. Así valoro el relato sin hablar en nombre de otros.",
    ],
    vocab=[("identidad", "lo que un pueblo reconoce como propio"), ("costumbre", "algo que una comunidad hace y repite"), ("cuidado", "acción para proteger algo"), ("comentar", "decir lo que pienso sobre algo con razones"), ("conectar", "unir una cosa con otra")],
    worked=[
        W("Relacionar relato y costumbre", TABLA3 + " ¿Qué costumbre explica el relato B?", ["Busco el relato B en la tabla.", "Dice: la gente agradece a un árbol antes de cortarlo.", "Esa es la costumbre."], "la gente agradece a un árbol antes de cortarlo"),
        W("Comentar la importancia", RA + " ¿Por qué podría ser importante este relato para la gente que lo cuenta?", ["El relato dice que el río es el origen de las personas.", "Por eso la gente cuida el río.", "Entonces el relato conecta a las personas con el río y con su cuidado."], "porque conecta a las personas con el río y con su cuidado"),
    ],
    mistakes=[
        M("Decir qué significa un relato real sin preguntar al pueblo que lo cuenta.", "La importancia la dicen las personas del pueblo.", "Uso frases como «según el educador tradicional…»."),
        M("Creer que un relato solo sirve para entretener.", "También conecta con el territorio, la identidad y los cuidados.", "Pregunto qué origen cuenta y qué cuida."),
    ],
    R=[
        ex(TABLA3 + " ¿Qué costumbre explica el relato A?", "la gente cuida el río", "La tabla lo dice."),
        ex(TABLA3 + " ¿Qué relato se relaciona con saludar al día con respeto?", "el relato D", "La tabla lo dice."),
        ex("Una costumbre, ¿es algo que una comunidad hace y repite o algo que ocurre una sola vez?", "algo que una comunidad hace y repite", "Así se definió costumbre."),
    ],
    C=[
        ex(TABLA3 + " ¿Qué origen cuenta el relato B?", "una pluma que se hizo isla y árboles", "La tabla lo dice."),
        ex("Verdadero o falso: un relato fundacional conecta a las personas con su territorio y su historia.", "Verdadero", "Eso explica la clase."),
        ex("¿La importancia de un relato real la dicen las personas del pueblo que lo cuentan o la inventa quien lo escucha?", "las personas del pueblo que lo cuentan", "Ellas conocen su sentido."),
    ],
    A=[
        ex("Une cada relato con su costumbre: A) relato A, B) relato B, C) relato D. Costumbres: 1) saludar al día, 2) cuidar el río, 3) agradecer a un árbol. Escribe los tres pares.", "A-2, B-3, C-1", "La tabla relaciona cada relato con su costumbre."),
        arith("Un curso lee los 3 relatos de la tabla por la mañana y 2 relatos más por la tarde. ¿Cuántos relatos leyó en total?", "3+2", "Se suman los de la mañana y los de la tarde."),
        ex("Elige la frase que comenta la importancia con respeto: A) «Según el educador tradicional, este relato es importante porque une a la comunidad». B) «Ese relato no sirve para nada». Escribe la letra.", "A", "A atribuye la importancia a la fuente y valora el relato."),
    ],
    Z=[
        ex(RB + " Un niño dice: «Si la gente agradece al árbol, entonces ese relato es de todas las culturas». ¿Es correcto? Sí o No.", "No", "Es un relato inventado y no puede atribuirse a todas."),
        ex("Una niña dice: «No me importa la importancia de los relatos de otros pueblos». ¿Qué le responderías: A) cada relato importa a quienes lo cuentan, o B) tiene razón?", "A", "Los relatos son importantes para los pueblos a los que pertenecen."),
    ],
    D=[
        ex(TABLA3 + " Si una comunidad inventada dejara de contar el relato A, ¿qué podría perder según la tabla: la conexión con el cuidado del río o el nombre de la quebrada?", "la conexión con el cuidado del río", "La tabla relaciona el relato con ese cuidado."),
        ex("Ordena para comentar un relato: A) digo a quién une o qué cuida. B) cuento el origen que presenta. C) nombro la costumbre relacionada. Escribe las letras en orden.", "B, C, A", "Primero el origen, luego la costumbre y al final lo que une o cuida."),
    ],
    context=[ex("Una persona mayor te cuenta por qué un relato de su pueblo es importante para ella. ¿Dices después «según ella» o dices «yo ya lo sabía»?", "dices «según ella»", "La importancia la dice quien la vive.")],
    selfcheck=[
        ex("¿Un relato fundacional puede conectar a las personas con su territorio? Sí o No.", "Sí", "Así lo explica la clase."),
        ex("¿Quién dice la importancia de un relato real: las personas del pueblo o quien lo escucha?", "las personas del pueblo", "Ellas lo conocen."),
        ex("¿Qué palabra uso para atribuir la importancia a quien la dice: «según» o «seguro»?", "según", "Según atribuye lo dicho a su fuente."),
    ],
    task=T(
        "Lee este relato de práctica F (inventado; no es de ningún pueblo): «Dicen que las primeras personas llegaron a un cerro siguiendo el vuelo de un pájaro. Allí construyeron sus casas. Desde entonces, cuentan, cada primavera suben al cerro a dar las gracias.» En tu cuaderno completa tres frases: el origen que cuenta, la costumbre relacionada y qué podría unir o cuidar este relato. Escribe también una frase de «yo pienso» sobre qué te gustó. Termina con una pregunta para el educador o educadora tradicional.",
        "Origen: las primeras personas siguieron a un pájaro hasta un cerro. Costumbre: subir al cerro cada primavera a dar las gracias. Une o cuida: une a las personas con su cerro. Yo pienso que me gustó la idea de dar las gracias. Pregunta: ¿qué relatos de nuestra comunidad se relacionan con un lugar?",
        ["nombra el origen", "relaciona la costumbre", "dice qué une o cuida", "marca lo propio con «yo pienso»", "formula una pregunta"],
        ["tres frases", "frase de «yo pienso»", "pregunta"],
        ["afirmar que es de un pueblo real", "inventar significados espirituales"],
        "Si atribuye el relato a un pueblo real, recuerda que es de práctica.",
    ),
    reinforce="Copia la tabla de práctica y agrega una columna con tu frase «yo pienso» para cada relato.",
    extend="Escribe un párrafo de cinco oraciones sobre por qué los relatos de origen son importantes para los pueblos que los cuentan, sin contar ningún relato real.",
)

# ============================================================ LS01 clase 4 · respuesta atribuida
FICHA4 = "Ficha de fuente (inventada): Un educador tradicional inventado de la Escuela Ejemplo cuenta a un curso el relato de práctica A. Dice que en su comunidad el relato se cuenta en las tardes de invierno. Aclara que es la versión de su comunidad. Cuando termina, dice que el relato es importante porque recuerda que las personas cuidan el río."

L(
    LS1, 4,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a escribir una respuesta corta sobre un relato fundacional, diciendo quién lo contó, qué cuenta, por qué es importante y hasta dónde vale. Sirve para explicar un relato sin quitarle la voz a quien lo contó.",
    prior=["Sé separar hechos, interpretación y límites.", "Sé comentar la importancia de un relato."],
    explain=[
        "Una respuesta atribuida sobre un relato tiene cuatro partes. Primero, la atribución: «Según el educador tradicional de la Escuela Ejemplo…». Segundo, lo que cuenta: «…el relato dice que de la montaña bajó un río». Tercero, la importancia: «…y es importante porque recuerda que las personas cuidan el río». Cuarto, el límite: «Es la versión de su comunidad».",
        "Cuando escribo, uso mis palabras para resumir pero no cambio los hechos. No agrego significados espirituales que el relato o la fuente no dijeron. Si quiero decir lo que sentí, lo escribo aparte con «yo pienso». También puedo decir que disfruté el relato, porque disfrutar un relato es parte de aprender de él, pero mi opinión no reemplaza lo que dijo la fuente.",
        "Antes de entregar, reviso con tres preguntas. ¿Se entiende quién lo contó? ¿Están los hechos tal como los dijo? ¿Aparece el límite? Si algo falta, lo agrego. Y si el relato es real y no de práctica, pido que el educador tradicional o la comunidad lo revise antes de mostrarlo.",
    ],
    vocab=[("atribución", "decir quién es la fuente"), ("resumir", "decir lo principal con menos palabras"), ("versión", "forma en que una comunidad cuenta un relato"), ("opinión", "lo que yo pienso o siento"), ("revisar", "mirar de nuevo para corregir")],
    worked=[
        W("Armar la atribución", FICHA4 + " Escribe la parte de atribución de la respuesta.", ["La atribución nombra a quien lo contó.", "Es un educador tradicional de la Escuela Ejemplo.", "Empiezo con «Según»."], "Según un educador tradicional de la Escuela Ejemplo,"),
        W("Detectar la parte que falta", "Una respuesta dice: «Según una vecina, de la montaña bajó un río. Es importante porque une al pueblo». ¿Qué parte de las cuatro falta?", ["Hay atribución, hay lo que cuenta y hay importancia.", "No dice de qué versión se trata ni hasta dónde vale.", "Falta el límite."], "falta el límite"),
    ],
    mistakes=[
        M("Escribir el resumen sin decir quién contó el relato.", "No se puede comprobar de dónde sale.", "Empiezo con «Según…»."),
        M("Cambiar los hechos del relato para que quede más lindo.", "El relato es de quien lo cuenta y no se modifica.", "Resumo con mis palabras pero mantengo los hechos."),
    ],
    R=[
        ex(FICHA4 + " ¿Qué relato cuenta el educador?", "el relato de práctica A", "La ficha lo dice."),
        ex(FICHA4 + " ¿Cuándo se cuenta el relato en su comunidad?", "en las tardes de invierno", "La ficha lo dice."),
        ex("La atribución en una respuesta, ¿dice quién es la fuente o dice mi opinión?", "dice quién es la fuente", "Así se definió atribución."),
    ],
    C=[
        ex(FICHA4 + " ¿Qué límite declara el educador?", "es la versión de su comunidad", "La ficha lo dice."),
        ex(FICHA4 + " Según el educador, ¿por qué es importante el relato?", "porque recuerda que las personas cuidan el río", "La ficha da esa razón."),
        ex("¿Qué parte de la respuesta atribuida dice por qué el relato es importante: la atribución, la importancia o el límite?", "la importancia", "La tercera parte explica por qué importa el relato."),
    ],
    A=[
        ex("Ordena las partes de la respuesta: A) límite. B) importancia. C) atribución. D) lo que cuenta. Escribe las letras en orden.", "C, D, B, A", "Atribuyo, cuento, explico la importancia y declaro el límite."),
        ex(FICHA4 + " Elige la mejor respuesta: A) «Según un educador tradicional de la Escuela Ejemplo, de la montaña bajó un río; el relato recuerda que las personas cuidan el río. Es la versión de su comunidad». B) «El relato prueba que todos cuidan el río». Escribe la letra.", "A", "A atribuye, resume, da la importancia y el límite."),
        arith("Una respuesta tiene 4 partes y una estudiante escribió 3. ¿Cuántas partes le faltan?", "4-3", "Se resta lo escrito al total."),
    ],
    Z=[
        ex("Una niña dice: «Me gustó mucho cómo se cuenta el relato». ¿Dónde debe ir esa frase: marcada con «yo pienso» o mezclada con lo que dijo el educador?", "marcada con «yo pienso»", "Su opinión no debe confundirse con lo dicho por la fuente."),
        ex("Un niño cambia «montaña» por «cerro» en su resumen del relato A. ¿Respeta los hechos del relato? Sí o No.", "No", "El relato A dice montaña."),
    ],
    D=[
        ex("Una respuesta dice: «Según un educador, el sol salió de una laguna. Es importante porque el pueblo es muy antiguo». ¿Qué problema tiene: inventa una razón que la fuente no dio o le falta el título?", "inventa una razón que la fuente no dio", "La importancia debe venir de la fuente."),
        ex("Dos estudiantes resumen el mismo relato real con permiso. Uno dice «Según la educadora…». El otro no cita a nadie. ¿Cuál respuesta es más confiable?", "la que cita a la educadora", "Se puede comprobar la fuente."),
    ],
    context=[ex("Vas a contar a tu familia un relato que te explicó el educador tradicional. ¿Empiezas con «Según el educador…» o como si lo hubieras inventado?", "con «Según el educador…»", "Así se reconoce a quien lo contó.")],
    selfcheck=[
        ex("¿Cuál es la última parte de la respuesta: el límite o la atribución?", "el límite", "Primero atribuyo y al final declaro el límite."),
        ex("¿Puedo cambiar los hechos del relato para resumirlo mejor? Sí o No.", "No", "Los hechos se mantienen."),
        ex("Mi opinión sobre el relato, ¿la marco con «yo pienso»? Sí o No.", "Sí", "Así se distingue de lo que dijo la fuente."),
    ],
    task=T(
        "Lee esta ficha inventada: «Una educadora tradicional inventada cuenta el relato de práctica D en la Escuela Muestra. Dice que se cuenta al amanecer. Aclara que es la versión que aprendió de su familia. Explica que es importante porque enseña a saludar al día con respeto.» En tu cuaderno escribe una respuesta de cuatro oraciones con atribución, lo que cuenta, importancia y límite. Agrega una frase de «yo pienso». Termina con una pregunta para el educador o educadora tradicional.",
        "Según una educadora tradicional de la Escuela Muestra, el primer sol salió de una laguna y el valle se llenó de luz. El relato es importante porque enseña a saludar al día con respeto. Es la versión que ella aprendió de su familia. Yo pienso que me gustó la imagen de la luz. Pregunta: ¿cómo puedo escuchar relatos de nuestra comunidad con respeto?",
        ["tiene atribución", "cuenta los hechos sin cambiarlos", "da la importancia que dijo la fuente", "declara el límite y marca lo propio"],
        ["respuesta de cuatro oraciones", "frase de «yo pienso»"],
        ["cambiar hechos", "agregar significados no dichos"],
        "Compara cada hecho con el relato; si algo no está en la ficha, debe marcarse como idea propia.",
    ),
    reinforce="Copia la respuesta modelo y subraya con distintos colores sus cuatro partes.",
    extend="Escribe dos respuestas atribuidas sobre el relato B: una completa y otra sin límite, y explica cuál es mejor.",
)

# ============================================================ LS01 clase 5 · contrastar sin jerarquizar
DOSREL = "Dos relatos de práctica (inventados; no son de ningún pueblo) sobre el origen de un mismo lago. Relato G (valle inventado del norte): el lago nació de una lágrima de una montaña que lloraba por la sequía. Relato H (valle inventado del sur): el lago nació cuando un gran pez golpeó la tierra con su cola. En ambos valles, la gente cuida el lago y no pesca en la época de reproducción de los peces."

L(
    LS1, 5,
    materials="Lápiz y hoja. Los relatos están escritos aquí y son inventados para practicar. No necesitas dispositivos.",
    use="Aprenderé a contrastar relatos de origen de distintos pueblos o culturas sin decir que uno es mejor, más antiguo o más verdadero. Sirve para valorar la diversidad de relatos.",
    prior=["Sé comentar la importancia de un relato.", "Sé escribir una respuesta atribuida con límite."],
    explain=[
        "Distintos pueblos y culturas cuentan relatos de origen diferentes. Pueden explicar el mismo fenómeno, por ejemplo cómo nació un lago, de maneras muy distintas. Eso no los hace mejores ni peores. Cada relato pertenece a quienes lo cuentan, a su territorio y a su historia. Contrasto para comprender, no para elegir ganadores.",
        "Para contrastar uso una tabla de tres columnas: qué tienen igual, qué tienen distinto y qué cuida o enseña cada uno. En los relatos G y H, ambos explican el nacimiento de un lago, pero uno habla de una lágrima y otro de un pez. Los dos relatos terminan con un cuidado del lago. Eso es lo que tienen en común.",
        "Los relatos de origen y la ciencia responden a preguntas distintas. El relato transmite sentido, identidad y cuidados para un pueblo. La ciencia explica con observaciones y evidencias cómo se formó un lugar. Son maneras diferentes de conocer y no compiten. Y también hay relatos de otras culturas significativas para mi contexto, que respeto de la misma manera.",
    ],
    vocab=[("contrastar", "comparar para ver parecidos y diferencias"), ("diversidad", "variedad de formas de ser, contar o vivir"), ("jerarquizar", "ordenar en mejor y peor"), ("en común", "lo que dos cosas tienen igual"), ("evidencia", "dato que se puede observar o comprobar")],
    worked=[
        W("Buscar lo común", DOSREL + " ¿Qué tienen en común los dos relatos?", ["Miro cómo terminan ambos.", "Los dos explican el origen de un lago.", "Y en ambos la gente cuida el lago."], "explican el origen de un lago y en ambos la gente cuida el lago"),
        W("Comparar sin jerarquizar", DOSREL + " Un niño dice: «El relato G es mejor que el H». ¿Cómo lo corriges?", ["Los relatos no se ordenan en mejores y peores.", "Cada uno es de su valle y su gente.", "Reescribo: «El relato G habla de una lágrima y el H de un pez»."], "los relatos no se ordenan en mejores o peores; solo se describen sus diferencias"),
    ],
    mistakes=[
        M("Decir que un relato es más verdadero que otro.", "Cada relato tiene su sentido para quienes lo cuentan.", "Describo qué cuenta cada uno sin ordenarlos."),
        M("Pensar que el relato y la ciencia compiten por la misma respuesta.", "Responden a preguntas distintas: sentido y evidencia.", "Explico qué enseña cada uno."),
    ],
    R=[
        ex(DOSREL + " ¿Qué fenómeno explican los dos relatos?", "el nacimiento de un lago", "Los dos hablan del origen de un lago."),
        ex(DOSREL + " ¿Qué origen da el relato G?", "una lágrima de una montaña", "El relato G lo dice."),
        ex(DOSREL + " ¿Qué origen da el relato H?", "un pez que golpeó la tierra con su cola", "El relato H lo dice."),
    ],
    C=[
        ex(DOSREL + " Verdadero o falso: según el texto, los dos relatos cuentan exactamente el mismo origen.", "Falso", "Uno habla de una lágrima y otro de un pez."),
        ex("Contrastar, ¿es comparar para ver parecidos y diferencias o elegir el mejor?", "comparar para ver parecidos y diferencias", "Así se definió contrastar."),
        ex(DOSREL + " ¿Qué hace la gente de ambos valles en la época de reproducción de los peces?", "no pesca", "El texto lo dice al final."),
    ],
    A=[
        ex("Clasifica con I (igual) o D (distinto): 1) ambos explican el origen de un lago. 2) uno habla de una lágrima y otro de un pez. 3) en ambos la gente cuida el lago. Escribe las tres letras.", "1 I, 2 D, 3 I", "La 2 es la diferencia."),
        arith("En la tabla hay 6 filas. 3 son «igual». ¿Cuántas son «distinto»?", "6-3", "Se restan las iguales del total."),
        ex(DOSREL + " Elige la frase que compara sin jerarquizar: A) «El relato G habla de una lágrima y el H de un pez; en ambos se cuida el lago». B) «El relato H es más verdadero». Escribe la letra.", "A", "A solo describe."),
    ],
    Z=[
        ex("Una niña dice: «La ciencia explica cómo se formó un lago con evidencias y el relato transmite sentido a un pueblo; ninguno reemplaza al otro». ¿Estás de acuerdo con esa idea según la clase? Sí o No.", "Sí", "Responden a preguntas distintas."),
        ex("Un niño dice: «Mi cultura tiene el mejor relato». ¿Qué es mejor responder: A) cada pueblo valora sus relatos y se pueden conocer sin compararlos como mejores, o B) tiene razón?", "A", "No se jerarquizan las culturas."),
    ],
    D=[
        ex(DOSREL + " ¿Cuál de estas afirmaciones ordena los relatos en mejor y peor, o dice algo que los textos no dicen? A) el G habla de una lágrima. B) el H es más antiguo y por eso vale más. C) en ambos se cuida el lago. Escribe la letra.", "B", "Los textos no dicen cuál es más antiguo y ordenar por antigüedad es jerarquizar."),
        ex("Un curso compara un relato de práctica con un relato de otra cultura significativa para su contexto, con permiso de una familia. ¿Qué debe hacer: A) describir diferencias y semejanzas y citar la fuente, o B) decir cuál es mejor?", "A", "Se contrasta con respeto y fuente."),
    ],
    context=[ex("Dos familias de tu escuela cuentan de manera distinta cómo nació un lugar de su cultura. ¿Escuchas ambas con respeto o decides cuál es la correcta?", "escuchas ambas con respeto", "Cada versión pertenece a quienes la cuentan.")],
    selfcheck=[
        ex("¿Se puede decir que un relato es mejor que otro? Sí o No.", "No", "Cada relato tiene su sentido."),
        ex("¿Qué columna de la tabla muestra lo que tienen en común los relatos: igual o distinto?", "igual", "Igual muestra lo común."),
        ex("El relato y la ciencia, ¿responden a preguntas distintas? Sí o No.", "Sí", "Una da sentido y la otra evidencias."),
    ],
    task=T(
        "Lee estos dos relatos de práctica (inventados; no son de ningún pueblo). Relato I: la primera fogata nació cuando dos piedras se tocaron en una noche sin luna (se cuenta que de ahí viene el cuidado del fuego en la comunidad). Relato J: la primera luz nació de una semilla que brilló bajo la tierra (se cuenta que de ahí viene el cuidado de las semillas). En tu cuaderno haz una tabla de tres columnas: igual, distinto y qué cuida cada relato. Escribe dos frases que comparen sin decir cuál es mejor. Termina con una pregunta para el educador o educadora tradicional.",
        "Igual: ambos explican un origen (de la fogata y de la luz) y lo relacionan con un cuidado. Distinto: el relato I habla de piedras y el relato J de una semilla; uno cuida el fuego y el otro las semillas. Frases: El relato I explica la luz con dos piedras y el cuidado del fuego. El relato J la explica con una semilla y el cuidado de las semillas. Pregunta: ¿cómo se pueden conocer varios relatos con respeto?",
        ["identifica lo igual y lo distinto", "nombra lo que cuida cada uno", "compara sin jerarquizar", "formula una pregunta"],
        ["tabla de tres columnas", "dos frases comparativas"],
        ["decir cuál es mejor", "mezclar los relatos"],
        "Si hay un juicio de valor, pídele que lo reemplace por una descripción.",
    ),
    reinforce="Relee los relatos G y H y subraya con un color lo común y con otro lo distinto.",
    extend="Escribe un párrafo de cinco oraciones sobre por qué es importante conocer relatos de distintas culturas sin compararlos como mejores o peores.",
)

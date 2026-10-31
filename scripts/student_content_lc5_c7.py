"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS05 (reconocer los usos de la lengua indígena en los espacios comunitarios, valorando su importancia para la
identidad del pueblo que corresponda).

Criterio de autoría: todas las comunidades, personas, sedes y testimonios son inventados solo para practicar y están
rotulados como tales; no se atribuye a ningún pueblo real una costumbre ni un uso concreto salvo el saludo «mari mari»
del mapuzugun. No se escribe ninguna palabra de lengua indígena fuera de «mari mari» y «chaltumay». No se afirma nada
sobre cuántas personas hablan una lengua. La pertenencia a un pueblo nunca se mide por cuánto se habla la lengua. Cada
tarea abierta remite al educador/a tradicional o a la comunidad. Este OA se distingue del OA LR05 del mismo nivel en que
aquí el foco es la valoración y las actitudes respecto de la identidad, no la revitalización.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS5 = "LC05 OA LS05"

CONSULT = " Recuerda: cómo se usa la lengua en tu comunidad lo enseñan el educador o la educadora tradicional y las personas de tu comunidad. Pregúntales antes de dar tu trabajo por terminado. Nadie está obligado a hablar de su familia ni de su pueblo."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. Nunca evaluar la identidad ni el origen de un estudiante."


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


CB = "Ficha de la Comunidad Brisa (inventada para practicar; no es de ningún pueblo real): Espacio 1, la sede social: las reuniones comienzan con un saludo en la lengua. Espacio 2, la feria del sábado: hay un cartel de bienvenida en la lengua y en castellano. Espacio 3, la escuela: un taller semanal con una educadora tradicional. Espacio 4, un grupo de vecinos que se junta a conversar: practican la lengua entre ellos. Espacio 5, la radio de la comunidad: una persona lee avisos en la lengua."

# ============================================================ LS05 clase 1 · situar espacios, pueblo y fuente
L(
    LS5, 1,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a identificar espacios de la comunidad donde se usa una lengua indígena y a ubicar de qué pueblo, territorio y fuente hablo. Sirve para reconocer los usos de la lengua sin mezclar comunidades.",
    prior=["Sé que cada pueblo tiene su propia lengua.", "Sé ubicar pueblo, territorio y fuente."],
    explain=[
        "Un espacio comunitario es un lugar o un grupo donde las personas de una comunidad se reúnen y comparten. Puede ser una sede social, una feria, una escuela, un grupo de vecinos o una radio. En algunos de esos espacios se usa la lengua indígena del pueblo. Reconocer esos usos es el primer paso para valorar la lengua.",
        "Para reconocer un uso, ubico el espacio y pregunto quién cuenta. En la ficha de la Comunidad Brisa, inventada, aparecen cinco espacios. No sé de qué pueblo es, porque la ficha no lo dice. Si fuera un caso real, tendría que preguntar el pueblo, el territorio y la fuente. Una ficha que no indica esos datos está incompleta.",
        "También reconozco que cada comunidad tiene sus propios espacios. Una comunidad puede tener radio y otra no. Una puede tener taller en la escuela y otra, un grupo de vecinos. Por eso no digo que todas las comunidades usan la lengua del mismo modo. Cuento lo que dice mi fuente y declaro sus límites.",
    ],
    vocab=[("espacio comunitario", "lugar o grupo donde la comunidad se reúne y comparte"), ("sede social", "lugar donde una comunidad hace sus reuniones"), ("uso de la lengua", "situación en que se habla o se escribe la lengua"), ("ficha incompleta", "ficha a la que le faltan datos"), ("fuente", "persona o documento de donde viene un dato")],
    worked=[
        W("Reconocer un uso", CB + " ¿Qué uso de la lengua hay en la sede social?", ["Busco el espacio 1.", "Dice que las reuniones comienzan con un saludo en la lengua.", "Ese es el uso."], "las reuniones comienzan con un saludo en la lengua"),
        W("Detectar datos que faltan", CB + " ¿Qué datos no entrega la ficha para ubicarla bien?", ["Recuerdo los datos de una ficha: pueblo, territorio, fuente y autorización.", "La ficha solo dice «Comunidad Brisa» y los espacios.", "No dice el pueblo, el territorio, quién cuenta ni si autoriza."], "faltan el pueblo, el territorio, la fuente y la autorización"),
    ],
    mistakes=[
        M("Decir que todas las comunidades tienen radio porque una ficha la menciona.", "Una ficha describe una sola comunidad.", "Digo «en la Comunidad Brisa hay una radio»."),
        M("Usar una ficha incompleta como si fuera segura.", "No sé de qué pueblo es ni quién la contó.", "Pido los datos que faltan antes de usarla."),
    ],
    R=[
        ex(CB + " ¿Qué espacio tiene un taller semanal con una educadora tradicional?", "la escuela", "El espacio 3 lo dice."),
        ex(CB + " ¿Qué uso de la lengua hay en la radio?", "una persona lee avisos en la lengua", "El espacio 5 lo dice."),
        ex("Un espacio comunitario, ¿es un lugar o grupo donde la comunidad se reúne y comparte o un lugar vacío?", "un lugar o grupo donde la comunidad se reúne y comparte", "Así se definió espacio comunitario."),
    ],
    C=[
        ex(CB + " ¿Cuántos espacios menciona la ficha?", "5", "Se cuentan los espacios 1 a 5."),
        ex(CB + " Verdadero o falso: según la ficha, la feria tiene un cartel solo en castellano.", "Falso", "El cartel está en la lengua y en castellano."),
        ex(CB + " ¿Dice la ficha de qué pueblo es la Comunidad Brisa? Sí o No.", "No", "La ficha no indica el pueblo."),
    ],
    A=[
        ex("Une cada espacio con su uso: A) la sede social, B) la feria, C) el grupo de vecinos. Usos: 1) practican la lengua conversando, 2) hay un cartel de bienvenida, 3) las reuniones empiezan con un saludo. Escribe los tres pares.", "A-3, B-2, C-1", "La ficha relaciona cada espacio con su uso."),
        arith("La ficha menciona 5 espacios. En 2 de ellos aparece algo escrito o leído en la lengua (el cartel y la radio). ¿En cuántos espacios la ficha no menciona nada escrito ni leído?", "5-2", "Se restan los dos espacios con lectura o escritura."),
        ex("Ordena para ubicar un uso en una ficha real: A) anoto el uso. B) pregunto el pueblo y el territorio. C) pregunto quién cuenta y si autoriza. Escribe las letras en orden.", "B, C, A", "Primero ubico pueblo y territorio, luego fuente y al final el uso."),
    ],
    Z=[
        ex("Un estudiante escribe: «En todas las comunidades indígenas hay una radio como la de Brisa». ¿Qué falla: generaliza o contradice la ficha? Escribe la que corresponde.", "generaliza", "Una ficha no habla de todas las comunidades."),
        ex("Quieres contar un uso de la lengua que viste en una sede, pero no sabes quién te lo contó. ¿Qué es mejor: A) contarlo igual o B) averiguar la fuente antes?", "B", "Sin fuente no se debe contar."),
    ],
    D=[
        ex(CB + " ¿En qué espacio es más probable que escuchen la lengua personas que no están en la sede: la radio o el grupo de vecinos que se junta a conversar? Piensa en a cuántas personas llega.", "la radio", "La radio puede llegar a más personas que un grupo pequeño."),
        ex("Dos fichas dicen cosas distintas de dos comunidades: una tiene radio y la otra, no. ¿Se contradicen? Sí o No.", "No", "Describen comunidades distintas."),
    ],
    context=[ex("Una vecina te cuenta cómo se usa la lengua en su comunidad. ¿Anotas quién es, de qué comunidad habla y si autoriza que lo cuentes, o solo recuerdas lo que dijo?", "anotas quién es, de qué comunidad habla y si autoriza que lo cuentes", "La fuente y el permiso se anotan.")],
    selfcheck=[
        ex("¿Una feria puede ser un espacio comunitario? Sí o No.", "Sí", "Es un lugar donde la comunidad se reúne."),
        ex("¿Todas las comunidades usan la lengua en los mismos espacios? Sí o No.", "No", "Cada comunidad tiene sus propios espacios."),
        ex("Una ficha sin pueblo ni fuente, ¿está completa? Sí o No.", "No", "Le faltan datos."),
    ],
    task=T(
        "Lee esta ficha inventada: «Comunidad Aurora, que no existe. Espacios: la sede (las reuniones comienzan con un saludo), el patio de la escuela (un juego en que se cuenta hasta diez en la lengua, que enseñó la educadora tradicional) y una vitrina con un letrero de bienvenida.» En tu cuaderno haz una tabla de tres filas y tres columnas: espacio, uso y qué datos faltan para ubicarla bien (pueblo, territorio, fuente). Después escribe una pregunta que le harías al educador o educadora tradicional de tu escuela.",
        "Sede / reuniones con un saludo / faltan pueblo, territorio y fuente. Patio / juego de contar hasta diez, enseñado por la educadora tradicional / faltan pueblo y territorio (la fuente es la educadora). Vitrina / letrero de bienvenida / faltan pueblo, territorio y fuente. Pregunta: ¿qué espacios de nuestra comunidad usan la lengua?",
        ["identifica los tres espacios y sus usos", "reconoce datos faltantes", "no generaliza", "formula una pregunta"],
        ["tabla de tres filas", "pregunta"],
        ["afirmar que todas las comunidades hacen lo mismo", "inventar los datos faltantes"],
        "Verifica que los datos faltantes se marquen como «por preguntar» y no se inventen.",
    ),
    reinforce="Relee la ficha de la Comunidad Brisa y numera los espacios del 1 al 5 con su uso al lado.",
    extend="Escribe una ficha inventada de tres espacios de una comunidad, con su uso, marcada como inventada.",
)

# ============================================================ LS05 clase 2 · escuchar un testimonio con límites
TES = "Testimonio de práctica (inventado): Una dirigenta de la Comunidad Brisa cuenta: «En mi niñez, la lengua se escuchaba en las reuniones de los mayores. Hoy los niños la aprenden en un taller y la oyen en la radio. Para mí, hablarla es una forma de sentirme unida a mi pueblo, pero mis hijos la entienden poco y igual son parte de nuestra comunidad. Hablo por mí; otras personas lo viven distinto»."

L(
    LS5, 2,
    materials="Lápiz y hoja. El testimonio está escrito aquí y es inventado para practicar. Puede leerlo en voz alta una persona adulta.",
    use="Aprenderé a escuchar o leer un testimonio sobre el uso de la lengua, separando lo que cuenta, lo que opina y los límites que declara. Sirve para reconocer usos de la lengua y valorar lo que dice la persona sin cambiarlo.",
    prior=["Sé separar hechos, opiniones y límites.", "Sé que la pertenencia no se mide por hablar la lengua."],
    explain=[
        "Un testimonio es lo que una persona cuenta sobre lo que vivió. Al escucharlo, anoto tres cosas. Los hechos que cuenta: «la lengua se escuchaba en las reuniones de los mayores». Las opiniones o sentimientos: «hablarla es una forma de sentirme unida a mi pueblo». Y los límites: «hablo por mí; otras personas lo viven distinto».",
        "En este testimonio también aparece una idea importante: los hijos de la dirigenta entienden poco la lengua y aun así son parte de la comunidad. Eso muestra que la pertenencia a un pueblo no depende de cuánto se habla la lengua. Cada persona tiene su historia y su forma de vivir su identidad. No comparo ni juzgo a las personas por lo que hablan.",
        "Al comentar un testimonio, uso «según la dirigenta» y respeto sus palabras. No digo que todas las personas de su pueblo sienten lo mismo, porque ella misma lo aclara. Si quiero saber más, hago preguntas respetuosas y pido permiso para anotar lo que me cuenta.",
    ],
    vocab=[("testimonio", "lo que una persona cuenta de lo que vivió"), ("sentimiento", "lo que una persona siente"), ("dirigenta", "mujer que dirige o representa a una comunidad"), ("identidad", "lo que una persona o pueblo reconoce como propio"), ("pertenecer", "ser parte de una comunidad")],
    worked=[
        W("Separar hecho y sentimiento", TES + " ¿«Hoy los niños la aprenden en un taller» es un hecho o un sentimiento?", ["Busco la frase.", "Cuenta algo que ocurre hoy.", "No dice «siento» ni «creo»."], "es un hecho"),
        W("Reconocer el límite", TES + " ¿Qué límite declara la dirigenta?", ["Busco una frase que avise de qué habla.", "Dice: «Hablo por mí; otras personas lo viven distinto».", "Ese es el límite."], "habla por sí misma y otras personas lo viven distinto"),
    ],
    mistakes=[
        M("Pensar que los hijos de la dirigenta no pertenecen a su comunidad porque entienden poco la lengua.", "La pertenencia no se mide por cuánto se habla.", "Digo que son parte de la comunidad, como dice ella."),
        M("Decir que todas las personas de su pueblo sienten lo mismo que ella.", "Ella aclara que otras lo viven distinto.", "Respeto el límite: hablo de lo que ella cuenta."),
    ],
    R=[
        ex(TES + " ¿Dónde se escuchaba la lengua en la niñez de la dirigenta?", "en las reuniones de los mayores", "El testimonio lo dice."),
        ex(TES + " ¿Dónde la aprenden hoy los niños, según el testimonio?", "en un taller", "El testimonio lo dice."),
        ex(TES + " ¿Dónde la oyen también hoy?", "en la radio", "El testimonio lo dice."),
    ],
    C=[
        ex(TES + " ¿«Hablarla es una forma de sentirme unida a mi pueblo» es un hecho o un sentimiento?", "un sentimiento", "Habla de lo que ella siente."),
        ex(TES + " Verdadero o falso: según la dirigenta, sus hijos entienden mucho la lengua.", "Falso", "Dice que la entienden poco."),
        ex(TES + " Según la dirigenta, ¿sus hijos son parte de la comunidad? Sí o No.", "Sí", "Dice que igual son parte de la comunidad."),
    ],
    A=[
        ex(TES + " Clasifica con H (hecho), S (sentimiento) o L (límite): 1) la lengua se escuchaba en las reuniones. 2) hablarla me hace sentir unida. 3) hablo por mí. Escribe las tres letras.", "1 H, 2 S, 3 L", "Cada frase es de un tipo distinto."),
        arith("En el testimonio hay 3 espacios de uso: las reuniones, el taller y la radio. Si se agrega 1 espacio más en la ficha de la comunidad, ¿cuántos espacios hay en total?", "3+1", "Se suma el espacio nuevo."),
        ex(TES + " Elige el mejor resumen: A) «Según una dirigenta de la Comunidad Brisa, hoy los niños aprenden la lengua en un taller y la oyen en la radio; ella habla por sí misma». B) «Todas las personas de su pueblo hablan la lengua». Escribe la letra.", "A", "A atribuye y respeta el límite."),
    ],
    Z=[
        ex("Un niño dice: «Si alguien no habla la lengua de su pueblo, no es parte de él». Según el testimonio, ¿tiene razón? Sí o No.", "No", "La dirigenta dice que sus hijos igual son parte de la comunidad."),
        ex(TES + " Una niña concluye: «Todas las dirigentas sienten lo mismo». ¿Lo dice el testimonio? Sí o No.", "No", "Ella dice que otras personas lo viven distinto."),
    ],
    D=[
        ex(TES + " Elige la mejor pregunta respetuosa: A) «¿Qué le gustaría que los niños aprendieran del taller?». B) «¿Por qué sus hijos no hablan bien la lengua?». Escribe la letra.", "A", "A pregunta sin juzgar."),
        ex("Quieres anotar lo que te cuenta una persona mayor de tu comunidad. ¿Qué haces primero: A) pedirle permiso o B) anotar en secreto?", "A", "Se pide permiso para anotar lo que cuenta."),
    ],
    context=[ex("Una compañera cuenta que entiende poco la lengua de su pueblo. ¿Le dices que sigue siendo parte de su pueblo o que no pertenece?", "le dices que sigue siendo parte de su pueblo", "La pertenencia no se mide por cuánto se habla la lengua.")],
    selfcheck=[
        ex("Un testimonio, ¿es lo que una persona cuenta de lo que vivió? Sí o No.", "Sí", "Así se definió testimonio."),
        ex("¿La pertenencia depende de cuánto se habla la lengua? Sí o No.", "No", "Cada persona vive su identidad a su manera."),
        ex("¿Qué palabra uso para atribuir lo que dijo: «según» o «seguro»?", "según", "Según atribuye a la fuente."),
    ],
    task=T(
        "Lee este testimonio inventado: «Un joven de la Comunidad Aurora cuenta: «Mi abuelo conversa en la lengua con sus amigos en la sede. A mí me gusta escucharlos aunque entiendo poco. Siento que escucharlos me acerca a mi comunidad. Esto es lo que yo vivo; otros jóvenes lo viven distinto».» En tu cuaderno escribe: un hecho, un sentimiento, el límite y una frase que empiece con «Según…» y que respete el límite. Agrega una pregunta respetuosa que le harías. Termina con una pregunta para el educador o educadora tradicional.",
        "Hecho: su abuelo conversa en la lengua con sus amigos en la sede. Sentimiento: escucharlos lo acerca a su comunidad. Límite: otros jóvenes lo viven distinto. Frase: Según un joven de la Comunidad Aurora, escuchar a su abuelo le hace sentir cerca de su comunidad; él habla de lo que vive. Pregunta: ¿qué te gustaría escuchar en la sede? Pregunta al educador: ¿cómo puedo escuchar con respeto?",
        ["separa hecho, sentimiento y límite", "usa «según»", "no juzga la pertenencia", "formula preguntas respetuosas"],
        ["tres datos y frase", "dos preguntas"],
        ["juzgar a quien entiende poco", "borrar el límite"],
        "Si la frase generaliza, pídele que agregue el límite.",
    ),
    reinforce="Relee el testimonio y subraya con tres colores los hechos, los sentimientos y el límite.",
    extend="Escribe tres frases sobre un uso de la lengua: un hecho, un sentimiento y un límite, sobre una situación inventada.",
)

# ============================================================ LS05 clase 3 · relaciones culturales: identidad, generaciones y actitudes
ACT = "Ficha de actitudes (de práctica): Actitudes que valoran la lengua: escuchar con atención, pedir permiso para anotar o grabar, agradecer a quien enseña, usar solo las palabras que la fuente enseñó, respetar el ritmo de quien está aprendiendo. Actitudes que no la valoran: burlarse de cómo alguien habla, exigir que alguien hable o hablarlo en su lugar, usar palabras sin permiso, decir que alguien no pertenece por hablar poco."

L(
    LS5, 3,
    materials="Lápiz y hoja. La ficha está escrita aquí y es de práctica. No necesitas dispositivos.",
    use="Aprenderé a relacionar el uso de la lengua con la identidad de un pueblo, con la transmisión entre generaciones y con actitudes de respeto. Sirve para valorar la lengua con acciones concretas.",
    prior=["Sé reconocer espacios de uso de la lengua.", "Sé que la pertenencia no se mide por cuánto se habla."],
    explain=[
        "La identidad de un pueblo se expresa en su historia, su territorio, sus formas de vivir y también en su lengua. Cuando la lengua se usa en los espacios comunitarios, ayuda a que las personas se reconozcan como parte de algo compartido. La transmisión entre generaciones, es decir, que las personas mayores enseñen y las más jóvenes aprendan, cuida esa identidad.",
        "Valorar la lengua es tener actitudes de respeto. La ficha de actitudes dice que valoran la lengua: escuchar con atención, pedir permiso, agradecer a quien enseña, usar solo las palabras que la fuente enseñó y respetar el ritmo de quien está aprendiendo. No la valoran: burlarse, exigir que alguien hable, usar palabras sin permiso o decir que alguien no pertenece por hablar poco.",
        "Las relaciones entre uso, identidad y actitudes son claras: si en un espacio se burlan de quien habla, esa persona puede dejar de hablar, y la lengua pierde un espacio. En cambio, si hay respeto y paciencia, las personas se animan a usar la lengua. Mis actitudes cuentan, y puedo elegir cuidar los espacios donde se usa.",
    ],
    vocab=[("transmisión", "paso de un saber de una generación a otra"), ("generación", "grupo de personas de edades parecidas"), ("actitud", "forma de actuar frente a algo"), ("burlarse", "reírse de alguien para dejarlo mal"), ("valorar", "reconocer que algo importa y cuidarlo")],
    worked=[
        W("Clasificar una actitud", ACT + " ¿«Agradecer a quien enseña» valora o no valora la lengua?", ["Busco la actitud en la ficha.", "Está en la lista de las que valoran.", "Entonces valora."], "valora la lengua"),
        W("Relacionar actitud y espacio", "En un taller inventado, un niño se burla de cómo un compañero dice una palabra. El compañero deja de participar. ¿Qué pasa con el espacio donde se usa la lengua?", ["La burla hace sentir mal a quien habla.", "El compañero deja de participar.", "El espacio pierde a una persona que practicaba."], "el espacio pierde a una persona que practicaba"),
    ],
    mistakes=[
        M("Pensar que valorar la lengua es solo hablarla.", "También es escuchar, pedir permiso y respetar.", "Reviso las actitudes de la ficha."),
        M("Burlarse de cómo habla alguien porque «es un chiste».", "Puede hacerle dejar de usar la lengua.", "Escucho con respeto y animo a practicar."),
    ],
    R=[
        ex(ACT + " ¿«Escuchar con atención» valora o no valora la lengua?", "valora la lengua", "Está en la lista que la valora."),
        ex(ACT + " ¿«Burlarse de cómo alguien habla» valora o no valora?", "no valora la lengua", "Está en la lista que no la valora."),
        ex("La transmisión, ¿es el paso de un saber de una generación a otra o un viaje en bus?", "el paso de un saber de una generación a otra", "Así se definió transmisión."),
    ],
    C=[
        ex(ACT + " Verdadero o falso: según la ficha, pedir permiso para grabar valora la lengua.", "Verdadero", "Está en la lista de actitudes que la valoran."),
        ex(ACT + " ¿«Decir que alguien no pertenece por hablar poco» valora o no valora la lengua?", "no valora la lengua", "Está en la lista que no la valora."),
        ex("Verdadero o falso: la identidad de un pueblo es solo su lengua.", "Falso", "También incluye historia, territorio y formas de vivir."),
    ],
    A=[
        ex(ACT + " Clasifica con V (valora) o N (no valora): 1) respetar el ritmo de quien aprende. 2) exigir que alguien hable. 3) agradecer a quien enseña. Escribe las tres letras.", "1 V, 2 N, 3 V", "La 2 no respeta a la persona."),
        arith("La ficha nombra 5 actitudes que valoran y 4 que no valoran. ¿Cuántas actitudes nombra en total?", "5+4", "Se suman las dos listas."),
        ex("Elige la acción que cuida la transmisión: A) una abuela inventada enseña un saludo y un niño lo practica con paciencia. B) un niño se burla de cómo dice el saludo. Escribe la letra.", "A", "En A hay transmisión respetuosa."),
    ],
    Z=[
        ex("Un niño dice: «Si valoro la lengua, tengo que hablarla perfecto». Según la clase, ¿tiene razón? Sí o No.", "No", "Valorar incluye escuchar, respetar y agradecer, no solo hablar."),
        ex("Una niña escucha a un mayor que usa una palabra de la lengua. ¿Qué es mejor: A) agradecerle y preguntar con respeto cómo se usa o B) corregirle su forma de decirla?", "A", "El mayor es quien conoce el uso."),
    ],
    D=[
        ex("Un grupo inventado se burla de quien dice mal una palabra. Con el tiempo nadie más practica en ese grupo. ¿Qué relación muestra esto entre actitud y uso de la lengua: que la burla reduce el uso o que no cambia nada?", "que la burla reduce el uso", "Las personas dejan de practicar."),
        ex("Dos formas de ayudar a la transmisión: A) invitar a una persona mayor a contar y agradecerle. B) grabarla sin avisar. ¿Cuál valora la lengua: A o B?", "A", "B no pide permiso."),
    ],
    context=[ex("En tu patio, un compañero intenta decir un saludo en una lengua indígena y se equivoca. ¿Le dices amablemente que pregunte al educador tradicional o te ríes?", "le dices amablemente que pregunte al educador tradicional", "Se respeta y se anima a aprender.")],
    selfcheck=[
        ex("¿Agradecer a quien enseña valora la lengua? Sí o No.", "Sí", "Está en la lista de actitudes que la valoran."),
        ex("¿Debo burlarme si alguien habla distinto? Sí o No.", "No", "La burla no valora la lengua."),
        ex("La transmisión entre generaciones, ¿ayuda a cuidar la identidad? Sí o No.", "Sí", "Los saberes pasan de unos a otros."),
    ],
    task=T(
        "Lee esta situación inventada: «En un taller, una niña se atreve a decir un saludo en la lengua y duda en una parte. Un compañero sonríe con burla. Otro compañero le dice «gracias por probar» y una educadora tradicional le muestra con paciencia cómo se dice.» En tu cuaderno haz una tabla de dos columnas: actitud y si valora o no valora la lengua. Incluye al menos tres actitudes de la situación. Luego escribe una frase que explique cómo se relacionan esas actitudes con que la niña siga usando la lengua. Termina con una pregunta para el educador o educadora tradicional.",
        "Sonreír con burla / no valora. Decir «gracias por probar» / valora. Mostrar con paciencia cómo se dice / valora. Frase: Cuando hay respeto y paciencia, la niña se anima a seguir usando la lengua; la burla puede hacer que deje de hacerlo. Pregunta: ¿cómo podemos crear un espacio respetuoso para practicar?",
        ["clasifica al menos tres actitudes", "explica la relación con el uso de la lengua", "no juzga la pertenencia", "formula una pregunta"],
        ["tabla de dos columnas", "frase explicativa"],
        ["clasificar mal una actitud", "no explicar la relación"],
        "Si clasifica mal una actitud, pídele que la compare con la ficha.",
    ),
    reinforce="Copia la ficha de actitudes y marca con un visto las que valoras y con una cruz las que no.",
    extend="Escribe un acuerdo de cinco actitudes para tu curso que cuide los espacios donde se usa una lengua.",
)

# ============================================================ LS05 clase 4 · valoración atribuida
FV = "Ficha de fuente (inventada): Un educador tradicional inventado de la Escuela Ejemplo cuenta que en su comunidad la lengua se usa en las reuniones, en el taller de la escuela y en un grupo de conversación de los viernes. Dice que usarla ayuda a que las niñas y los niños se sientan parte de su pueblo y que él habla de su comunidad. Aclara que las personas que no hablan la lengua también pertenecen."

L(
    LS5, 4,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a escribir una valoración corta: qué usos de la lengua reconozco, por qué son importantes para la identidad, cuál es mi fuente y qué puedo hacer yo. Sirve para expresar lo que aprendí sin hablar por otros.",
    prior=["Sé reconocer usos y límites.", "Sé relacionar uso, identidad y actitudes."],
    explain=[
        "Una valoración atribuida es un texto breve que dice qué usos de la lengua reconozco, por qué son importantes y de quién es la información. Tiene cinco partes. Primero, atribuyo: «Según un educador tradicional de la Escuela Ejemplo…». Segundo, cuento los usos: «…la lengua se usa en reuniones, en un taller y en un grupo de conversación». Tercero, explico por qué son importantes para la identidad.",
        "Cuarto, declaro el límite: «él habla de su comunidad». Quinto, digo qué puedo hacer yo para valorar la lengua. Mi acción debe ser realista y respetuosa: por ejemplo, escuchar con atención, agradecer a quien enseña o pedir permiso antes de anotar. No prometo hablar perfecto ni hablo en nombre de otras personas.",
        "Antes de entregar, reviso mi texto con cuatro preguntas: ¿dije quién es mi fuente?, ¿conté solo los usos que dijo?, ¿expliqué la importancia con sus palabras, sin inventar?, ¿declaré el límite? Si falta algo, lo agrego. Y si el texto trata de una comunidad real, pido que el educador tradicional lo revise antes de mostrarlo.",
    ],
    vocab=[("valoración", "texto en que digo por qué algo importa"), ("atribución", "decir quién es la fuente"), ("acción", "algo concreto que puedo hacer"), ("realista", "que se puede cumplir"), ("importancia", "razón por la que algo vale")],
    worked=[
        W("Leer la fuente", FV + " ¿Qué tres usos de la lengua cuenta el educador?", ["Busco los usos en la ficha.", "Reuniones, taller de la escuela y grupo de conversación de los viernes.", "Son tres."], "reuniones, taller de la escuela y grupo de conversación de los viernes"),
        W("Armar la acción", FV + " Escribe una acción realista para valorar la lengua.", ["Pienso en algo concreto que yo pueda hacer.", "Puedo escuchar con atención y agradecer al educador.", "Esa acción es realista."], "escuchar con atención y agradecer al educador"),
    ],
    mistakes=[
        M("Escribir acciones que no puedo cumplir, como «hablaré perfecto desde mañana».", "No es realista y presiona.", "Elijo una acción concreta que pueda cumplir."),
        M("Hablar en nombre de todo el pueblo.", "El educador habla de su comunidad.", "Atribuyo y declaro el límite."),
    ],
    R=[
        ex(FV + " ¿Quién cuenta lo que dice la ficha?", "un educador tradicional de la Escuela Ejemplo", "La ficha lo dice."),
        ex(FV + " ¿Qué día es el grupo de conversación?", "los viernes", "La ficha lo dice."),
        ex(FV + " Según el educador, ¿las personas que no hablan la lengua pertenecen también a su pueblo? Sí o No.", "Sí", "Lo aclara al final."),
    ],
    C=[
        ex(FV + " ¿Por qué es importante usar la lengua, según el educador?", "ayuda a que niñas y niños se sientan parte de su pueblo", "La ficha da esa razón."),
        ex(FV + " ¿Qué límite declara el educador?", "habla de su comunidad", "La ficha lo dice."),
        ex("¿Qué parte de la valoración dice lo que yo puedo hacer para valorar la lengua: la acción o el límite?", "la acción", "La quinta parte es mi acción."),
    ],
    A=[
        ex("Ordena las partes de la valoración: A) acción. B) límite. C) atribución. D) importancia. E) usos. Escribe las letras en orden.", "C, E, D, B, A", "Atribuyo, cuento los usos, explico la importancia, declaro el límite y propongo mi acción."),
        arith("Una valoración tiene 5 partes y un estudiante escribió 3. ¿Cuántas le faltan?", "5-3", "Se resta lo escrito al total."),
        ex(FV + " Elige la mejor valoración: A) «Según un educador tradicional de la Escuela Ejemplo, la lengua se usa en reuniones, en un taller y en un grupo de conversación; ayuda a que las niñas y los niños se sientan parte de su pueblo. Él habla de su comunidad. Yo voy a escuchar con atención y agradecer». B) «Todos los pueblos usan la lengua igual». Escribe la letra.", "A", "A tiene las cinco partes."),
    ],
    Z=[
        ex("Un niño escribe como acción: «Voy a decirle a todos los de mi pueblo que hablen la lengua». ¿Es realista y respetuosa? Sí o No.", "No", "No puedo exigir a otros ni hablar por ellos."),
        ex(FV + " Una niña agrega: «El educador dijo que hablar la lengua obliga a pertenecer». ¿Lo dice la ficha? Sí o No.", "No", "La ficha dice lo contrario."),
    ],
    D=[
        ex("Dos acciones de estudiantes: 1) «Agradeceré a quien me enseñe y pediré permiso antes de anotar». 2) «Grabaré a mis vecinos sin avisar para aprender». ¿Cuál es respetuosa: 1 o 2?", "1", "La 2 no pide permiso."),
        ex("Una valoración dice: «Según un educador, la lengua se usa en reuniones. Es importante porque une al pueblo. Voy a escuchar con atención». ¿Qué parte falta: el límite o la atribución?", "el límite", "Tiene atribución, usos, importancia y acción."),
    ],
    context=[ex("Vas a escribir qué aprendiste de lo que te contó una persona de tu comunidad sobre la lengua. ¿Empiezas con «Según…» o como si lo supieras desde siempre?", "con «Según…»", "Así se atribuye a la fuente.")],
    selfcheck=[
        ex("¿Cuál es la última parte de la valoración: la acción o la atribución?", "la acción", "Termino con lo que yo haré."),
        ex("¿Puedo prometer lo que no puedo cumplir? Sí o No.", "No", "La acción debe ser realista."),
        ex("¿Debo declarar el límite de mi fuente? Sí o No.", "Sí", "Avisa hasta dónde vale lo que se cuenta."),
    ],
    task=T(
        "Lee esta ficha inventada: «Una vecina de la Comunidad Aurora cuenta que la lengua se usa en la sede los jueves y en un programa de radio los domingos. Dice que usarla ayuda a que los niños conozcan a su comunidad y que ella habla por sí misma.» En tu cuaderno escribe una valoración de cinco oraciones con atribución, usos, importancia, límite y una acción tuya, realista y respetuosa. Termina con una pregunta para el educador o educadora tradicional.",
        "Según una vecina de la Comunidad Aurora, la lengua se usa en la sede los jueves. También se usa en un programa de radio los domingos. Ella dice que usarla ayuda a que los niños conozcan a su comunidad. Habla por sí misma. Yo voy a escuchar con atención y agradecer a quien me enseñe. Pregunta: ¿cómo puedo apoyar el uso de la lengua en la escuela?",
        ["tiene atribución, usos, importancia, límite y acción", "la acción es realista y respetuosa", "no juzga la pertenencia", "formula una pregunta"],
        ["valoración de cinco oraciones", "pregunta"],
        ["acciones irreales", "hablar por otros"],
        "Si la acción es irreal, pídele que elija una más concreta.",
    ),
    reinforce="Copia la valoración modelo y subraya con distintos colores sus cinco partes.",
    extend="Escribe dos acciones realistas más para valorar la lengua y explica por qué se pueden cumplir.",
)

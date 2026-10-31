"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 07 (procesos que han afectado el territorio) y OA 08 (memoria histórica de los pueblos indígenas).

Criterio de autoría: las comunidades, los lugares, las personas, los testimonios y los textos escolares de los
ejercicios son INVENTADOS (no pertenecen a ningún pueblo real) y se rotulan así. No se afirma nada de lengua,
ritos, fechas de celebraciones, arte, cosmovisión ni roles de un pueblo concreto, salvo datos generales de amplio
consenso. Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad; ningún ejercicio exige
saber una lengua indígena. Los otros módulos lc6_* importan los ayudantes de este archivo.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA7, OA8 = "LC06 OA 07", "LC06 OA 08"

CONSULT = " Recuerda: lo tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."


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


MAT = "Lápiz y hojas. Las fichas y los testimonios están escritos en este cuaderno. Las comunidades, los lugares y las personas son inventados."

# ------------------------------------------------------------------ OA 07
FCA = ("Ficha situada (inventada). Comunidad: Cerro Azul (no es un pueblo real). Territorio: cerros de pastoreo, una vertiente y un camino de tierra. "
       "Fuente y responsable: doña Rosa, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Rosa autorizó usar esta ficha en la escuela. "
       "Límite: no se cuenta dónde está la vertiente que la comunidad cuida.")
FCB = ("Ficha situada (inventada). Comunidad: Caleta Brisa (no es un pueblo real). Territorio: una caleta, una playa donde se varan los botes y un puerto cercano. "
       "Fuente y responsable: don Patricio, pescador de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Patricio autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan los lugares de pesca que la comunidad cuida.")
TCA = ("Testimonio inventado de doña Rosa, de Cerro Azul: «Mis abuelos pastoreaban en cerros que eran de todos. En 1930 un loteo dividió esos cerros en parcelas separadas. "
       "En 1965 una empresa compró una parte para plantar pinos. En 1980 muchos jóvenes se fueron a la ciudad a buscar trabajo. En 2005 la comunidad logró inscribir una parte de los cerros a su nombre.»")
TCB = ("Testimonio inventado de don Patricio, de Caleta Brisa: «En 1970 se construyó un puerto grande junto a la caleta. Los botes perdieron parte de la playa donde se varaban. "
       "En 1990 muchas familias se fueron a trabajar al puerto. En 2010 los pescadores se organizaron para pedir un sector de la playa para sus botes.»")

L(
    OA7, 1, materials=MAT,
    use="Aprenderé a situar un territorio antes de reflexionar sobre lo que le ocurrió: de qué comunidad es, quién lo cuenta y qué no se puede contar. Sirve para estudiar los procesos que afectaron un territorio sin hablar por otros.",
    prior=["Sé leer una ficha situada con comunidad, fuente, permiso y límite.", "Sé que cada comunidad cuenta su territorio a su manera y que una ficha no vale para todos los pueblos."],
    explain=[
        "En Lengua y Cultura, un proceso es una serie de hechos que ocurren a lo largo del tiempo y que van cambiando un lugar y la vida de quienes lo habitan. Un solo hecho, como un loteo de terrenos, puede ser parte de un proceso más largo, como la pérdida del uso común de unos cerros.",
        "Los pueblos indígenas han vivido muchos procesos que afectaron sus territorios: la división o pérdida de tierras, la llegada de caminos, puertos o empresas, y la salida de familias hacia las ciudades. También han vivido procesos de defensa y recuperación. Sus consecuencias se notan hoy en la situación actual de cada pueblo.",
        "Para reflexionar con respeto primero hay que situar. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es el relato. Lo que cuenta una comunidad no se puede aplicar tal cual a todos los pueblos, porque cada uno tiene su propia historia.",
    ],
    vocab=[("proceso", "serie de hechos a lo largo del tiempo que cambian un lugar y la vida de las personas"), ("consecuencia", "lo que ocurre después, como resultado de un hecho"), ("situación actual", "cómo vive hoy una comunidad"), ("loteo", "división de un terreno grande en parcelas separadas"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FCA + " ¿De quién es el relato y qué no se puede contar?", ["La comunidad es Cerro Azul y la fuente es doña Rosa.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuenta dónde está la vertiente."], "El relato es de doña Rosa, de Cerro Azul; no se cuenta la ubicación de la vertiente."),
        W("Hecho y proceso", "Doña Rosa cuenta que en 1930 se loteó un cerro común y que después las familias ya no pudieron pastorear juntas. ¿Qué es el loteo y qué es el proceso?", ["El loteo ocurrió en un momento: es un hecho.", "Que las familias dejaran de pastorear juntas se fue dando con los años.", "Ese cambio gradual del uso de los cerros es el proceso."], "El loteo es un hecho; el cambio gradual del uso común de los cerros es el proceso."),
    ],
    mistakes=[
        M("Pensar que un proceso es un solo día o un solo hecho.", "Un proceso se forma con varios hechos durante años.", "Busca los hechos y mira cómo cambian el lugar con el tiempo."),
        M("Decir «en Cerro Azul pasó lo mismo que a todos los pueblos indígenas».", "La ficha habla de una sola comunidad.", "Escribe siempre el nombre de la comunidad y de la fuente."),
    ],
    R=[
        ex("Según la ficha de Cerro Azul, ¿quién es la fuente?", "Doña Rosa", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Caleta Brisa? A) cerros de pastoreo y una vertiente B) una caleta, una playa de varado y un puerto cercano", "B", "Los cerros y la vertiente son de Cerro Azul."),
        ex("La ficha de Cerro Azul dice que no se cuenta dónde está la vertiente. ¿Puedes marcarla en un mapa de tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es un proceso que afectó un territorio? A) un cuento sobre un cerro B) una serie de hechos a lo largo del tiempo que cambiaron el lugar", "B", "Un proceso reúne varios hechos y sus cambios."),
        ex("Verdadero o falso: un loteo en 1930 puede formar parte de un proceso más largo de pérdida del uso común.", "Verdadero", "Un hecho puede ser el inicio de un cambio que dura años."),
        ex("Verdadero o falso: la situación actual de una comunidad puede tener relación con hechos del pasado.", "Verdadero", "Las consecuencias de un proceso pueden notarse hoy."),
    ],
    A=[
        ex("Doña Rosa cuenta: «En 1930 un loteo dividió los cerros comunes en parcelas separadas». ¿Qué cambió? A) los cerros pasaron de ser de todos a estar divididos B) los cerros se hicieron más altos", "A", "El testimonio habla de la división del uso común."),
        ex("Una compañera trae una ficha con comunidad, territorio y fuente, pero sin límite. ¿Qué falta? A) el nombre de la escuela B) lo que no se puede contar", "B", "El límite dice qué no se cuenta."),
        ex("Clasifica en DATO DE LA FICHA o IDEA MÍA: a) el territorio de Caleta Brisa incluye una playa donde se varan los botes b) seguro la playa era más grande hace mucho.", "a dato de la ficha, b idea mía", "La primera está escrita; la segunda es una suposición."),
    ],
    Z=[
        ex("Camilo escribe: «En Cerro Azul pasó lo mismo que a todos los pueblos indígenas». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una comunidad no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de reflexionar sobre un proceso? A) porque un relato es la mirada de una persona de una comunidad B) para saber quién escribió más rápido", "A", "Situar muestra de quién es la mirada."),
    ],
    D=[
        ex("Alguien escribe: «El límite dice que no se cuentan los lugares de pesca». ¿De cuál ficha viene el dato: Cerro Azul o Caleta Brisa?", "Caleta Brisa", "Solo la ficha de Caleta Brisa nombra lugares de pesca."),
        ex("Una ficha dice solo: «Comunidad: Cerro Azul. Territorio: cerros». ¿Qué datos de una ficha situada faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
    ],
    context=[ex("Un afiche escolar cuenta cómo una comunidad perdió sus pastos, pero no dice de qué comunidad habla. ¿Puedes usarlo para explicar el caso de Cerro Azul? Responde Sí o No.", "No", "No se sabe si el afiche se refiere a Cerro Azul.")],
    selfcheck=[
        ex("Escribe tres datos que debe tener una ficha situada.", "Tres entre: comunidad, territorio, fuente, permiso, límite", "Son los datos que permiten situar el relato."),
        ex("Verdadero o falso: lo que cuenta la ficha de Cerro Azul vale para todos los pueblos indígenas.", "Falso", "Cada pueblo tiene su propia historia."),
        ex("Tema: el territorio. Ante una duda sobre una comunidad real, ¿qué haces? A) pregunto al educador tradicional o a la comunidad B) lo supongo", "A", "Ellos son la fuente."),
    ],
    task=T("Lee este testimonio inventado de don Patricio: «Mi caleta tiene una playa donde varamos los botes. Cerca de la caleta hay un puerto. Hay lugares de pesca que cuidamos entre todos.» Haz una ficha con: comunidad, territorio, fuente, qué dice la fuente y un límite. Después escribe una frase con «Yo pienso que…» sobre por qué un puerto cercano podría cambiar la vida de una caleta.",
           "Comunidad: Caleta Brisa. Territorio: caleta, playa de varado y puerto cercano. Fuente: don Patricio. Dice: varan los botes en la playa y cuidan lugares de pesca. Límite: no sé dónde están esos lugares. Yo pienso que un puerto cercano podría cambiar el uso de la playa.",
           ["completa la ficha con datos del testimonio", "separa lo que dice la fuente de lo que piensa", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["agregar datos que el testimonio no dice", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea del testimonio está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Subraya en la ficha de Cerro Azul la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué el loteo de 1930 puede ser parte de un proceso y no solo un hecho aislado.",
)

L(
    OA7, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre un proceso que afectó un territorio, con los límites a la vista: qué dice la fuente, qué consecuencia cuenta, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que un proceso es una serie de hechos en el tiempo."],
    explain=[
        "Un testimonio sobre un proceso mezcla hechos, fechas y consecuencias. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. La consecuencia que la fuente cuenta, como «los botes perdieron parte de la playa». Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "Una interpretación puede ser razonable, pero no es un dato de la fuente. Por eso se marca con «yo pienso que». También cuidamos no atribuir sentimientos que nadie dijo, como «odia a la empresa», porque la fuente no los contó. Y si la fuente no explica una razón, escribimos «el testimonio no lo dice».",
        "Leer con límites declarados significa cerrar el trabajo diciendo hasta dónde llega lo que afirmamos. Si queremos saber más sobre un proceso que afectó a una comunidad real, preguntamos al educador o a la educadora tradicional. Nunca rellenamos los vacíos con ideas inventadas.",
    ],
    vocab=[("testimonio", "relato de una persona sobre lo que vivió o sabe"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("atribuir", "decir de quién viene un dato"), ("límite", "lo que no se cuenta o no se sabe"), ("consecuencia", "lo que ocurre como resultado de un hecho")],
    worked=[
        W("Separar cuatro cosas", TCB + " Separa lo que dice, la consecuencia, lo que interpreto y lo que no se cuenta sobre el puerto.", ["Dice: en 1970 se construyó un puerto junto a la caleta.", "Consecuencia contada: los botes perdieron parte de la playa donde se varaban.", "Interpreto: yo pienso que los pescadores tuvieron que cambiar su forma de trabajar.", "No se cuenta: cuánta playa se perdió."], "Dice: se construyó un puerto. Consecuencia: los botes perdieron parte de la playa. Interpreto: tuvieron que cambiar su trabajo. No se cuenta: cuánta playa se perdió."),
        W("Corregir una frase", "Un niño escribe: «Don Patricio cuenta que el puerto arruinó la caleta para siempre». ¿Está bien?", ["Reviso el testimonio: dice que los botes perdieron parte de la playa.", "«Arruinó para siempre» es idea del niño.", "Debería escribir «yo pienso que» o usar las palabras de la fuente."], "No: esa frase mezcla la idea del niño con lo que dijo don Patricio."),
    ],
    mistakes=[
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
        M("Atribuir sentimientos o razones que el testimonio no cuenta.", "La fuente solo contó hechos y consecuencias.", "Escribe «el testimonio no lo dice» y deja la razón sin completar."),
    ],
    R=[
        ex("Testimonio de doña Rosa: «En 1980 muchos jóvenes se fueron a la ciudad a buscar trabajo». ¿Qué hicieron los jóvenes? A) compraron los cerros B) se fueron a la ciudad a buscar trabajo", "B", "El testimonio lo dice así."),
        ex("Tema: el territorio. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no dice por qué una empresa quiso comprar los cerros, ¿qué escribes? A) lo hizo por dinero B) el testimonio no lo dice", "B", "No se inventan razones que la fuente no contó."),
    ],
    C=[
        ex("Verdadero o falso: escribir «yo pienso que…» ayuda a no confundir mi idea con la voz de la fuente.", "Verdadero", "La marca separa la interpretación del dato."),
        ex("Don Patricio dice: «Los botes perdieron parte de la playa donde se varaban». ¿Qué es esa frase? A) una causa del puerto inventada por mí B) una consecuencia del puerto contada por la fuente", "B", "Es lo que ocurrió después de construirse el puerto."),
        ex("Verdadero o falso: una consecuencia que cuenta la fuente y una que yo supongo valen igual como dato.", "Falso", "Lo supuesto es interpretación y no dato de la fuente."),
    ],
    A=[
        ex("Don Patricio dice: «En 1990 muchas familias se fueron a trabajar al puerto». Clasifica en DICE LA FUENTE o INTERPRETO: a) muchas familias se fueron a trabajar al puerto b) la caleta quedó con menos pescadores.", "a dice la fuente, b interpreto", "La primera está escrita; la segunda es una deducción de quien lee."),
        ex("Doña Rosa dice: «Mis abuelos pastoreaban en cerros que eran de todos. En 1930 un loteo dividió esos cerros en parcelas separadas». ¿Qué cambió en el uso de los cerros? A) pasaron de ser de todos a dividirse en parcelas B) pasaron a ser más bajos", "A", "El loteo separó terrenos que antes eran comunes."),
        arith("Doña Rosa cuenta que en 1965 una empresa compró parte de los cerros y que en 2005 la comunidad inscribió una parte a su nombre. ¿Cuántos años pasaron entre ambos hechos?", "2005-1965", "Se restan los años."),
    ],
    Z=[
        ex("Pedro escribe: «Por culpa del loteo, doña Rosa odia a la empresa». ¿Qué problema tiene la frase?", "Atribuye un sentimiento que el testimonio no dice", "La fuente no contó lo que siente."),
        ex("La ficha de Cerro Azul dice: «No se cuenta dónde está la vertiente». ¿Por qué no la ubicas en tu trabajo? A) porque el límite de la ficha lo pide B) porque está lejos", "A", "Respetar el límite también es respetar a la comunidad."),
    ],
    D=[
        ex("Dos frases sobre don Patricio. 1) «En 1970 se construyó un puerto junto a la caleta». 2) «El puerto destruyó para siempre la vida de Caleta Brisa». ¿Cuál se queda en lo que dice la fuente?", "La primera", "La segunda agrega una conclusión que el testimonio no contiene."),
        ex("El testimonio no dice cuántos botes perdieron la playa. ¿Qué pones en la columna «No se cuenta»? A) que perdieron la playa B) cuántos botes perdieron la playa", "B", "Lo que el testimonio no precisa va en esa columna."),
    ],
    context=[ex("Debes explicar a tu curso qué le pasó a Caleta Brisa con el puerto. ¿Qué comienzo respeta el testimonio? A) «Don Patricio cuenta que en 1970 se construyó un puerto junto a la caleta…» B) «Todos saben que los puertos destruyen las caletas…»", "A", "El primero atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre un proceso.", "Lo que dice la fuente, la consecuencia que cuenta, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Verdadero o falso: puedo completar con mi imaginación lo que la fuente no contó.", "Falso", "Eso sería inventar."),
        ex("¿Qué escribes cuando el testimonio no explica una razón? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Rosa: «Cuando yo era niña, mi familia llevaba las cabras al cerro común. Después el cerro se dividió y cada familia quedó con su parcela. Hoy llevamos pocos animales. De la vertiente no hablamos con visitas.» Haz cuatro columnas: «La fuente dice», «Consecuencia que cuenta», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: el cerro común se dividió en parcelas. Consecuencia que cuenta: hoy llevan pocos animales. Yo interpreto: yo pienso que con parcelas separadas es más difícil pastorear juntos. No se cuenta: cómo se hizo la división y dónde está la vertiente. Límite: no sé por qué se dividió.",
           ["separa cuatro columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar la razón de la división"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Rosa.",
    extend="Explica por qué «el testimonio no lo dice» es una respuesta más honesta que inventar una razón.",
)

L(
    OA7, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre un proceso que afectó un territorio y la situación actual de una comunidad, y a comparar dos casos sin decir que uno es peor que otro.",
    prior=["Sé separar lo que dice la fuente de lo que interpreto.", "Sé qué es un proceso y qué es una consecuencia."],
    explain=[
        "Una relación causa-consecuencia une un hecho con lo que vino después. Por ejemplo: «se construyó un puerto» (hecho) y «los botes perdieron parte de la playa» (consecuencia). Cuando la fuente cuenta cómo vive hoy la comunidad, podemos relacionar esa situación actual con los hechos de su pasado, pero siempre diciendo que es una relación que la fuente nombra o que yo propongo.",
        "Comparamos dos comunidades inventadas: Cerro Azul, que vivió la división de sus cerros, y Caleta Brisa, que vivió la construcción de un puerto. Ambas vieron cambios en su territorio y en la salida de familias hacia otros trabajos. También hay diferencias: una perdió pastos y la otra, parte de la playa.",
        "Para comparar usamos los mismos criterios en las dos tablas: qué hecho ocurrió, qué consecuencia contó la fuente y qué hizo la comunidad después. No se ordenan de «más grave» a «menos grave», porque cada comunidad vive su propio proceso. Y dos casos no bastan para decir que todos los pueblos vivieron lo mismo.",
    ],
    vocab=[("causa", "hecho que provoca otro"), ("consecuencia", "lo que ocurre después de un hecho"), ("semejanza", "algo parecido entre dos casos"), ("diferencia", "algo distinto entre dos casos"), ("criterio", "punto de comparación igual para los dos casos")],
    worked=[
        W("Relacionar un hecho con su consecuencia", TCB + " ¿Qué consecuencia cuenta don Patricio del puerto?", ["El hecho: en 1970 se construyó un puerto grande junto a la caleta.", "Lo que vino después, según la fuente: los botes perdieron parte de la playa.", "Entonces la consecuencia contada es perder parte de la playa de varado."], "La consecuencia que cuenta don Patricio es la pérdida de parte de la playa donde se varaban los botes."),
        W("Comparar con un criterio", "Criterio: «qué hizo la comunidad después». Cerro Azul: inscribió una parte de los cerros a su nombre en 2005. Caleta Brisa: los pescadores se organizaron en 2010 para pedir un sector de la playa. ¿Qué semejanza hay?", ["Cerro Azul actuó en 2005 para recuperar un espacio.", "Caleta Brisa actuó en 2010 para pedir un espacio.", "Las dos comunidades se organizaron para defender un espacio de su territorio."], "Semejanza: ambas se organizaron para defender o recuperar un espacio de su territorio."),
    ],
    mistakes=[
        M("Decir que el proceso de una comunidad fue peor que el de otra.", "Comparar no es ordenar de más grave a menos grave.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todos los pueblos vivieron lo mismo porque dos casos se parecen.", "Dos ejemplos no representan a todos los pueblos.", "Escribe «en estas dos comunidades» y no más."),
    ],
    R=[
        ex("En Cerro Azul, ¿qué hecho ocurrió en 1930? A) un loteo dividió los cerros B) se construyó un puerto", "A", "El puerto es de Caleta Brisa."),
        ex("En Caleta Brisa, ¿qué hicieron los pescadores en 2010? A) se organizaron para pedir un sector de la playa B) vendieron sus botes", "A", "El testimonio dice que se organizaron."),
        ex("¿Qué perdió Caleta Brisa con el puerto: parte de la playa de varado o parte de los pastos?", "Parte de la playa de varado", "Los pastos son de Cerro Azul."),
    ],
    C=[
        ex("Verdadero o falso: comparar dos comunidades significa decir cuál sufrió más.", "Falso", "Comparar es buscar semejanzas y diferencias con los mismos criterios."),
        ex("¿Qué es un criterio de comparación? A) la opinión de quien compara B) un punto igual para los dos casos, como «qué hizo la comunidad después»", "B", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: si dos comunidades se parecen en algo, todos los pueblos indígenas vivieron lo mismo.", "Falso", "Dos casos no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «qué dejó la salida de familias». Cerro Azul: en 1980 muchos jóvenes se fueron a la ciudad. Caleta Brisa: en 1990 muchas familias se fueron a trabajar al puerto. ¿Qué semejanza hay? A) en ninguna salió nadie B) en ambas hubo salida de personas a otros trabajos", "B", "En las dos comunidades salieron personas a buscar trabajo."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) las dos comunidades se organizaron después de perder espacio b) una perdió pastos y la otra, parte de una playa.", "a semejanza, b diferencia", "La primera es algo en común; la segunda, algo distinto."),
        arith("Cerro Azul: el loteo fue en 1930 y la inscripción de los cerros, en 2005. ¿Cuántos años pasaron entre ambos hechos?", "2005-1930", "Se restan los años."),
    ],
    Z=[
        ex("Ana dice: «El proceso de Caleta Brisa fue más injusto que el de Cerro Azul». ¿Qué falla en su comparación?", "Ordena dos casos sin un criterio común", "Comparar no es jerarquizar los procesos."),
        ex("Un compañero escribe: «Como pasó en Cerro Azul y en Caleta Brisa, pasó en todos los pueblos». ¿Qué debería escribir? A) «en todos los pueblos» B) «en estas dos comunidades»", "B", "Dos casos no permiten hablar de todos los pueblos."),
    ],
    D=[
        arith("Caleta Brisa: el puerto se construyó en 1970 y los pescadores se organizaron en 2010. ¿Cuántos años pasaron entre ambos hechos?", "2010-1970", "Se restan los años."),
        ex("Alguien relaciona así: «Como se fueron familias al puerto, la caleta quedó vacía». La fuente solo dice que muchas familias se fueron a trabajar al puerto. ¿Qué parte es interpretación?", "Que la caleta quedó vacía", "La fuente no dice que quedara vacía."),
    ],
    context=[ex("Tu curso arma un panel con la historia de dos comunidades. Una compañera quiere titularlo «Los pueblos indígenas perdieron todo». ¿Qué título respeta mejor lo aprendido? A) «Dos comunidades, dos procesos que afectaron su territorio» B) «La verdad sobre todos los pueblos»", "A", "El título A nombra solo los casos estudiados.")],
    selfcheck=[
        ex("Escribe un ejemplo de causa y su consecuencia con el puerto de Caleta Brisa.", "Se construyó un puerto y los botes perdieron parte de la playa", "Une el hecho con lo que vino después."),
        ex("Verdadero o falso: puedo ordenar dos procesos de «más grave» a «menos grave».", "Falso", "Cada comunidad vive su propio proceso."),
        ex("Nombra un criterio de comparación para dos comunidades.", "Por ejemplo: qué hizo la comunidad después", "Debe ser un punto igual para ambas."),
    ],
    task=T("Compara Cerro Azul y Caleta Brisa con estos datos inventados. Cerro Azul: pérdida del uso común de los cerros (1930); salida de jóvenes (1980); inscripción de cerros (2005). Caleta Brisa: puerto junto a la caleta (1970); salida de familias al puerto (1990); organización de pescadores (2010). Haz una tabla con tres criterios: «qué hecho cambió el territorio», «qué salió de la comunidad» y «qué hizo la comunidad después». Escribe una semejanza y una diferencia, y una frase que termine con «en estas dos comunidades».",
           "Hecho que cambió el territorio: Cerro Azul, loteo de cerros; Caleta Brisa, puerto. Qué salió: jóvenes y familias a otros trabajos. Qué hizo la comunidad: inscribió cerros; pidió un sector de playa. Semejanza: ambas se organizaron para defender un espacio. Diferencia: una perdió pastos y la otra, parte de la playa. Esto ocurrió en estas dos comunidades.",
           ["usa los mismos criterios para ambas", "distingue semejanza y diferencia", "no jerarquiza"], ["tabla de tres criterios", "semejanza y diferencia"], ["decir cuál proceso fue peor", "generalizar a todos los pueblos"],
           "Pedir que muestre en la tabla la fila que respalda cada semejanza; valorar que no ordene los procesos."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «qué sigue cuidando la comunidad») y explica por qué debes pedirlo con permiso a la fuente.",
)

L(
    OA7, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida: una reflexión sobre un proceso que afectó un territorio y sus consecuencias hoy, que dice de quién viene cada dato y hasta dónde llega.",
    prior=["Sé relacionar un hecho con su consecuencia.", "Sé comparar dos comunidades con los mismos criterios y sin jerarquizar."],
    explain=[
        "Una respuesta atribuida tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Rosa cuenta que…». Segundo, el proceso y su consecuencia en la situación actual. Tercero, tu reflexión, marcada con «yo pienso que». Cuarto, un límite. Quinto, una pregunta para el educador o la educadora tradicional.",
        "En Chile existen leyes que se refieren a los pueblos indígenas. La Ley Indígena, número 19.253, se dictó en 1993 y reconoce a los pueblos indígenas y se ocupa de proteger sus tierras. Qué significó esa ley para un pueblo concreto lo cuentan las fuentes de ese pueblo; aquí solo la usamos como dato general.",
        "Una buena reflexión no culpa a personas concretas, no dice que todos los pueblos vivieron lo mismo y no inventa lo que la fuente calló. Se queda en lo que sabemos y deja una pregunta para seguir aprendiendo con quienes conocen su propio territorio. Al final, la devolvemos a la comunidad o al educador para que la revise.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("reflexión", "idea propia que se piensa a partir de lo que se leyó, marcada como mía"), ("Ley Indígena", "ley chilena número 19.253, de 1993, que reconoce a los pueblos indígenas"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen"), ("situación actual", "cómo vive hoy una comunidad")],
    worked=[
        W("Armar una respuesta", TCA + " Arma una respuesta atribuida de cinco partes sobre los cerros.", ["Dato: doña Rosa cuenta que en 1930 un loteo dividió los cerros que eran de todos.", "Consecuencia: en 1980 muchos jóvenes se fueron a la ciudad a buscar trabajo.", "Reflexión: yo pienso que dividir los cerros cambió cómo vivía la comunidad.", "Límite y pregunta: no sé por qué se dividieron; preguntaré al educador tradicional."], "Respuesta con dato atribuido, consecuencia, «yo pienso que», límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «Los loteos destruyeron a todos los pueblos indígenas». ¿Qué le falta a la respuesta?", ["No dice de qué fuente viene el dato.", "Generaliza a todos los pueblos.", "No tiene límite ni pregunta."], "Le falta atribuir la fuente, no generalizar y agregar límite y pregunta."),
    ],
    mistakes=[
        M("Generalizar a todos los pueblos con un solo testimonio.", "Un testimonio no representa a todos los pueblos.", "Escribe «según doña Rosa, en Cerro Azul…»."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Rosa? A) «Todos saben que…» B) «Doña Rosa cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: el territorio. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, proceso y consecuencia, reflexión, límite y pregunta."),
        ex("Tema: el territorio. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Cuál es el número de la Ley Indígena chilena?", "19.253", "Es el número de esa ley, dictada en 1993."),
        ex("Verdadero o falso: la Ley Indígena dice por sí sola qué significó para cada pueblo.", "Falso", "Eso lo cuentan las fuentes de cada pueblo."),
        ex("Tema: el territorio. ¿Para qué sirve la pregunta final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de don Patricio: «Los botes perdieron parte de la playa donde se varaban». Completa la atribución: «Don Patricio cuenta que los botes…»", "Perdieron parte de la playa donde se varaban", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Rosa cuenta que en 2005 inscribieron una parte de los cerros b) yo pienso que eso les dio más seguridad.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        arith("La Ley Indígena se dictó en 1993. ¿Cuántos años pasaron hasta 2005, cuando Cerro Azul (inventada) inscribió parte de sus cerros?", "2005-1993", "Se restan los años."),
    ],
    Z=[
        ex("Tema: el territorio. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque conoce el territorio y puede corregir errores B) porque es una tarea de decoración", "A", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones sobre Cerro Azul. 1) «Doña Rosa cuenta que en 1930 se dividieron los cerros; yo pienso que eso cambió cómo vivía la comunidad». 2) «La empresa de los pinos tuvo la culpa de todos los problemas». ¿Cuál está bien construida?", "La primera", "La segunda culpa sin que la fuente lo diga."),
        ex("Un compañero agrega a su trabajo una fiesta que, según él, «seguro hacen en Caleta Brisa». El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre cómo el puerto cambió la vida de Caleta Brisa. ¿Qué empieza mejor? A) «Todos los pueblos piensan que los puertos…» B) «Don Patricio cuenta que en 1970…»", "B", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida.", "Dato de la fuente, proceso y consecuencia, reflexión, límite y pregunta", "Están en la explicación."),
        ex("Tema: el territorio. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: el territorio. ¿Qué haces al terminar? A) guardarlo sin mostrarlo B) mostrarlo a la comunidad o al educador para que lo revise", "B", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de don Patricio: «Hoy muchos de nosotros pescamos en botes más chicos porque la playa de varado es más pequeña. Los jóvenes trabajan en el puerto y nos ayudan los fines de semana. Hay lugares de pesca que no mostramos.» Escribe una respuesta de cinco partes sobre cómo el proceso del puerto afecta hoy a Caleta Brisa: 1) dato de don Patricio, 2) consecuencia actual, 3) tu reflexión con «yo pienso que», 4) un límite y 5) una pregunta para el educador tradicional.",
           "1) Don Patricio cuenta que la playa de varado es hoy más pequeña. 2) Por eso pescan en botes más chicos y los jóvenes trabajan en el puerto. 3) Yo pienso que el puerto cambió la forma de trabajar de las familias. 4) No sé cómo se decidió el tamaño de la playa. 5) Pregunta: ¿cómo han cuidado su territorio las comunidades cuando llegan cambios grandes?",
           ["atribuye cada dato", "relaciona proceso y situación actual", "incluye límite y pregunta"], ["texto de cinco partes"], ["generalizar a todos los pueblos", "no marcar la opinión propia"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu respuesta con el testimonio de doña Rosa y los cerros de Cerro Azul.",
)

# ------------------------------------------------------------------ OA 08
FVM = ("Ficha situada (inventada). Comunidad: Valle Manso (no es un pueblo real). Territorio: un valle con acequias, chacras y un camino hacia el pueblo. "
       "Fuente y responsable: doña Inés, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Inés autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan las reuniones que la comunidad hace en privado.")
TEX = ("Texto escolar inventado (no es de ningún libro real): «En 1900 llegaron colonos al valle y comenzó el progreso. Antes, el valle estaba deshabitado.»")
MVM = ("Memoria oral inventada de doña Inés, de Valle Manso: «Mi abuela contaba que, antes de 1900, ya vivían familias en el valle y regaban sus chacras con acequias. "
       "Cuando llegaron los colonos, nos quitaron parte de los pastos. Mi familia nunca dejó de vivir aquí.»")

L(
    OA8, 1, materials=MAT,
    use="Aprenderé a situar una memoria histórica indígena: quién la cuenta, de qué comunidad es y qué tipo de fuente es. Sirve para estudiar el pasado desde la mirada de un pueblo sin mezclarla con otras.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada comunidad cuenta su pasado a su manera."],
    explain=[
        "La memoria histórica es lo que un pueblo recuerda y transmite sobre su pasado. Se conserva en relatos orales que pasan de generación en generación, y también en escritos, objetos y lugares. Es una visión del pasado: la mirada de quienes lo vivieron o lo recibieron de sus mayores.",
        "La historia nacional es el relato del pasado del país que se enseña en los textos escolares. Suele contar los hechos desde algunas voces y dejar otras de lado. La memoria de los pueblos indígenas puede aportar voces y hechos que ese relato no incluye, y por eso ayuda a hacerse preguntas sobre la historia nacional.",
        "Para estudiar una memoria hay que situarla: ¿quién la cuenta?, ¿de qué comunidad es?, ¿de qué época habla?, ¿dio permiso?, ¿qué no se cuenta? Una memoria oral vale tanto como un texto escrito, pero es la mirada de una comunidad concreta y no la de todos los pueblos.",
    ],
    vocab=[("memoria histórica", "lo que un pueblo recuerda y transmite sobre su pasado"), ("historia oral", "relato del pasado que se transmite hablando, de generación en generación"), ("historia nacional", "relato del pasado del país que se enseña en los textos escolares"), ("época", "período de tiempo, como un año o una década"), ("fuente histórica", "persona, texto u objeto que informa sobre el pasado")],
    worked=[
        W("Situar una memoria", FVM + " " + MVM + " ¿Quién cuenta, de qué comunidad es y qué tipo de fuente es?", ["Cuenta doña Inés.", "La comunidad es Valle Manso.", "Es memoria oral: la recibió de su abuela, hablando."], "La cuenta doña Inés, de Valle Manso, como memoria oral."),
        W("Distinguir dos fuentes", TEX + " ¿Qué tipo de fuente es y qué puede faltar en ella?", ["Es un texto escolar escrito.", "Dice que el valle estaba deshabitado antes de 1900.", "No incluye la voz de las familias que, según doña Inés, ya vivían allí."], "Es un texto escrito; puede faltarle la voz de la comunidad."),
    ],
    mistakes=[
        M("Pensar que la memoria oral vale menos que un texto escrito.", "La oralidad es una forma válida de conservar el pasado.", "Trata ambas con seriedad y atribuye cada fuente."),
        M("Contar la memoria de Valle Manso como si fuera la de todos los pueblos.", "Cada pueblo tiene su propia memoria.", "Escribe «según doña Inés, en Valle Manso…»."),
    ],
    R=[
        ex("Según la ficha de Valle Manso, ¿quién es la fuente: doña Inés o don Patricio?", "Doña Inés", "La ficha la nombra como fuente."),
        ex("Un relato del pasado que se cuenta hablando de generación en generación, ¿es oral o escrito?", "Oral", "La oralidad transmite relatos hablando."),
        ex("El texto escolar inventado, ¿es una fuente oral o una fuente escrita?", "Escrita", "Está escrito en un texto."),
    ],
    C=[
        ex("Verdadero o falso: una memoria oral vale menos que un texto escrito.", "Falso", "Ambas son formas válidas de conservar el pasado."),
        ex("En Lengua y Cultura, ¿qué es la memoria histórica de un pueblo? A) lo que ese pueblo recuerda y transmite sobre su pasado B) una fecha del calendario escolar", "A", "Es su forma de recordar y contar el pasado."),
        ex("Verdadero o falso: la memoria de una comunidad se puede aplicar tal cual a todos los pueblos.", "Falso", "Cada pueblo tiene su propia memoria."),
    ],
    A=[
        ex("Doña Inés cuenta que, antes de 1900, ya vivían familias en el valle. El texto escolar dice que antes de 1900 estaba deshabitado. ¿En qué se contradicen? A) en el color de las chacras B) en si había familias viviendo antes de 1900", "B", "Una dice que sí había familias y el otro que no."),
        ex("Una ficha dice: «Fuente: doña Inés. Época: antes de 1900. Permiso: sí». ¿Qué dato falta para situar la memoria? A) el color del papel B) la comunidad", "B", "Falta decir de qué comunidad es el relato."),
        ex("Clasifica en MEMORIA ORAL o TEXTO ESCOLAR: a) «Mi abuela contaba que ya vivían familias» b) «El valle estaba deshabitado».", "a memoria oral, b texto escolar", "La primera se transmitió hablando; la segunda está escrita en el texto."),
    ],
    Z=[
        ex("Lucía dice: «Como el texto escolar dice que el valle estaba deshabitado, doña Inés se equivoca». ¿Qué error comete?", "Da por verdadera una sola fuente sin contrastar", "Una memoria y un texto deben contrastarse, no descartarse."),
        ex("Un compañero afirma: «La memoria de Valle Manso es la memoria del pueblo que trabaja mi escuela». ¿Es válido sin consultar? A) No: hay que consultar al educador tradicional B) Sí, siempre", "A", "Solo el educador o la comunidad dicen cuál es la memoria del pueblo que corresponde."),
    ],
    D=[
        arith("Doña Inés cuenta que los colonos llegaron en 1900. ¿Cuántos años pasaron hasta 1975, cuando (en esta historia inventada) se abrió una escuela en el valle?", "1975-1900", "Se restan los años."),
        ex("Tema: la memoria histórica. Una ficha no dice quién cuenta ni de qué época habla. ¿Qué falta para usarla? A) la fuente y la época B) más colores", "A", "Son datos para situar una memoria."),
    ],
    context=[ex("Tu curso lee el texto escolar inventado y la memoria de doña Inés. Una compañera quiere escribir «los indígenas dicen que…». ¿Qué le dices? A) que nombre la comunidad y la fuente de cada dato B) que mezcle todo", "A", "Cada dato se atribuye a su comunidad y fuente.")],
    selfcheck=[
        ex("Nombra dos datos para situar una memoria.", "Dos entre: quién cuenta, comunidad, época, permiso", "Permiten saber de quién es el relato."),
        ex("Tema: la memoria histórica. Verdadero o falso: la oralidad es una forma válida de conservar la historia.", "Verdadero", "Los relatos de generación en generación guardan el pasado."),
        ex("¿Qué haces si no sabes cuál es la memoria del pueblo que corresponde? A) la invento B) pregunto al educador tradicional", "B", "Él o ella es la fuente."),
    ],
    task=T("Lee esta memoria inventada de don Mateo, de Lago Espejo: «Mi tío contaba que sus abuelos ya pescaban en el lago antes de que se hiciera el camino. Hay historias del lago que solo se cuentan en la comunidad.» Haz una ficha con: comunidad, fuente, tipo de fuente (oral o escrita), época y un límite. Después escribe una frase con «Yo pienso que…» sobre qué aporta una memoria oral a la historia de un lugar.",
           "Comunidad: Lago Espejo. Fuente: don Mateo, que recibió el relato de su tío. Tipo: memoria oral. Época: antes de que se hiciera el camino. Límite: no se cuentan las historias del lago que reserva la comunidad. Yo pienso que una memoria oral aporta cómo vivían las familias antes del camino.",
           ["completa la ficha con datos del relato", "distingue fuente oral y escrita", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["agregar datos que el relato no dice", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea del relato está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Subraya en la ficha de Valle Manso la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué la memoria de un pueblo puede aportar algo que el texto escolar inventado no dice.",
)

L(
    OA8, 2, materials=MAT,
    use="Aprenderé a leer una memoria histórica indígena con límites declarados: qué dice la fuente, qué interpreto yo y qué no se cuenta. Sirve para valorar la memoria sin inventar ni exagerar.",
    prior=["Sé situar una memoria histórica con su ficha.", "Sé que la memoria oral y el texto escrito son fuentes distintas."],
    explain=[
        "Una memoria histórica es una visión del pasado. Para valorarla primero hay que leerla bien. Separamos tres cosas: lo que la fuente dice con sus palabras, lo que yo interpreto y lo que no se cuenta. Si mezclamos las tres, ya no sabemos qué recordó la comunidad y qué agregamos nosotros.",
        "Cuando una memoria y un texto escolar cuentan el mismo hecho de manera distinta, no decidimos de inmediato cuál es «la verdadera». Anotamos qué dice cada uno, quién lo dice y qué datos aporta. Valorar la memoria es reconocer que tiene algo que decir, no asegurar que ella sola tiene toda la razón.",
        "También hay cosas que una comunidad resguarda: relatos que solo se cuentan dentro de ella. Respetar ese límite es parte de valorar su memoria. Cerramos el trabajo con una frase que declara hasta dónde llega lo que afirmamos y, si queremos saber más sobre una comunidad real, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("memoria histórica", "lo que un pueblo recuerda y transmite sobre su pasado"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("contrastar", "comparar dos fuentes para ver en qué coinciden y en qué difieren"), ("resguardar", "cuidar algo y no mostrarlo a todos"), ("valorar", "reconocer que algo tiene importancia y algo que aportar")],
    worked=[
        W("Separar tres cosas", MVM + " Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: antes de 1900 ya vivían familias en el valle y regaban con acequias.", "Interpreto: yo pienso que las familias conocían bien el valle.", "No se cuenta: cuántas familias eran ni cuáles pastos perdieron."], "Dice: había familias y acequias antes de 1900. Interpreto: conocían bien el valle. No se cuenta: cuántas familias eran y cuáles pastos perdieron."),
        W("Contrastar sin descartar", TEX + " Si lo comparas con la memoria de doña Inés, ¿qué haces?", ["Anoto lo que dice cada fuente.", "Veo que se contradicen sobre si el valle estaba habitado.", "No descarto a ninguna: busco una tercera fuente y pregunto al educador tradicional."], "Contrasto las dos fuentes y busco una tercera, sin descartar a ninguna."),
    ],
    mistakes=[
        M("Decir que la memoria oral es «la verdad» y el texto escolar, «mentira».", "Valorar una memoria no es descartar toda otra fuente sin contrastar.", "Anota qué dice cada fuente y busca una tercera."),
        M("Rellenar con ideas lo que la comunidad no contó.", "Lo resguardado se respeta; inventarlo puede ser falso e irrespetuoso.", "Escribe «la fuente no lo dice»."),
    ],
    R=[
        ex("Según doña Inés, ¿con qué regaban sus chacras las familias antes de 1900: con acequias o con camiones?", "Con acequias", "La memoria lo dice así."),
        ex("Una interpretación, ¿es mía o de la comunidad?", "Mía", "Interpretar es dar una idea propia."),
        ex("Si la fuente no dice cuántas familias vivían en el valle, ¿qué escribes? A) la fuente no lo dice B) eran diez", "A", "No se inventan datos."),
    ],
    C=[
        ex("Verdadero o falso: valorar una memoria es reconocer que tiene algo que aportar.", "Verdadero", "No significa asegurar que ella sola tiene la razón."),
        ex("Dos fuentes cuentan lo mismo de manera distinta. ¿Qué haces primero? A) elijo la que me gusta más B) anoto qué dice cada una y quién lo dice", "B", "Primero se registra y luego se contrasta."),
        ex("Verdadero o falso: respetar lo que una comunidad resguarda es parte de valorar su memoria.", "Verdadero", "Cuidar lo reservado muestra respeto."),
    ],
    A=[
        ex("Doña Inés dice: «Cuando llegaron los colonos, nos quitaron parte de los pastos». Clasifica en DICE LA FUENTE o INTERPRETO: a) nos quitaron parte de los pastos b) los colonos eran personas egoístas.", "a dice la fuente, b interpreto", "La segunda es un juicio de quien lee, no un dato."),
        ex("Doña Inés dice: «Mi familia nunca dejó de vivir aquí». ¿Qué aporta esa frase a la historia del valle? A) que el valle estuvo vacío B) que hubo familias que permanecieron allí", "B", "Es lo que la memoria cuenta."),
        ex("Un niño escribe: «Doña Inés cuenta que los colonos fueron malos». ¿Qué dato no está en la memoria?", "Que los colonos fueron malos", "La memoria dice que nos quitaron parte de los pastos, no que fueran malos."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «El valle era perfecto antes de 1900». ¿Qué debería hacer con esa frase?", "Marcarla como su opinión o quitarla", "No está en la memoria, así que es opinión."),
        ex("Tema: la memoria histórica. ¿Por qué conviene escribir los límites al final de un trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases sobre la misma memoria. 1) «Doña Inés dice que antes de 1900 ya vivían familias en el valle». 2) «Doña Inés dice que el texto escolar miente». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que la memoria no contiene."),
        ex("La ficha de Valle Manso dice que no se cuentan las reuniones privadas. Un compañero quiere describirlas en su trabajo. ¿Qué haces? A) lo dejo imaginar cómo son B) le pido que respete el límite de la ficha", "B", "El límite se respeta."),
    ],
    context=[ex("En una feria escolar, un grupo quiere un cartel con la frase «Doña Inés demostró que el texto escolar está equivocado». ¿Qué cambio respeta mejor la lectura con límites? A) dejarla igual B) «Doña Inés recuerda algo distinto al texto escolar: que ya vivían familias en el valle»", "B", "La frase A atribuye el dato sin afirmar más de lo que dijo.")],
    selfcheck=[
        ex("Nombra las tres cosas que separo al leer una memoria histórica.", "Lo que dice la fuente, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: la memoria histórica. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("¿Qué haces cuando dos fuentes se contradicen? Escribe una acción.", "Anoto lo que dice cada una y busco otra fuente", "Así se contrasta sin descartar."),
    ],
    task=T("Lee esta memoria inventada de doña Inés: «Mi abuela me contó que las familias se juntaban a limpiar las acequias antes de sembrar. Hubo años en que perdimos pastos, pero seguimos sembrando. De las reuniones de la comunidad no hablamos con visitas.» Haz tres columnas: «La fuente dice», «Yo interpreto» y «No se cuenta». Pon al menos dos datos en cada una. Cierra con una frase de límites.",
           "La fuente dice: las familias limpiaban las acequias juntas; perdieron pastos pero siguieron sembrando. Yo interpreto: yo pienso que trabajar juntos las ayudó a resistir. No se cuenta: qué se habla en las reuniones. Límite: no sé en qué años pasó cada cosa.",
           ["separa tres columnas", "usa datos de la memoria", "marca sus ideas como interpretación"], ["tabla de tres columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar lo que se reserva"],
           "Pedir que indique en qué línea de la memoria está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en la memoria de doña Inés.",
    extend="Explica por qué contrastar una memoria con un texto escolar no significa descartar ninguna de las dos.",
)

L(
    OA8, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre la memoria de un pueblo y la historia nacional: qué voces aporta, qué preguntas permite hacer y cómo comparar sin jerarquizar.",
    prior=["Sé leer una memoria con límites.", "Sé que la memoria oral y el texto escolar son fuentes distintas."],
    explain=[
        "Problematizar la historia nacional es hacerle preguntas: ¿quién la cuenta?, ¿qué voces incluye?, ¿cuáles faltan? No es burlarse de ella ni decir que todo está mal. Es mirarla con atención y buscar si hay otras miradas que ayuden a entender mejor lo que pasó.",
        "La memoria de un pueblo indígena es una de esas miradas. Puede aportar hechos que el texto no menciona, como que ya había familias en un valle antes de que llegaran otros, y puede mostrar cómo vivió un proceso quien lo recibió. Así se complementa la historia nacional: no se reemplaza, se hace más completa.",
        "Para relacionar dos fuentes usamos una tabla con los mismos criterios: qué hecho cuenta cada una, qué voz tiene, qué aporta y qué no dice. No ordenamos las fuentes de «mejor» a «peor». Y si dos comunidades cuentan procesos parecidos, lo anotamos como semejanza, sin decir que todos los pueblos recuerdan lo mismo.",
    ],
    vocab=[("problematizar", "hacer preguntas a un relato para ver qué voces incluye y cuáles faltan"), ("voz", "persona o grupo que cuenta algo"), ("complementar", "agregar algo que ayuda a completar una idea"), ("semejanza", "algo parecido entre dos fuentes"), ("jerarquizar", "decir que una fuente es mejor que otra")],
    worked=[
        W("Hacer una pregunta al texto", TEX + " Escribe una pregunta que problematice el texto.", ["El texto dice que el valle estaba deshabitado.", "No cuenta de qué voces viene esa idea.", "Pregunta: ¿qué dicen las familias que vivían allí antes de 1900?"], "Pregunta posible: ¿qué dicen las familias que vivían en el valle antes de 1900?"),
        W("Complementar sin reemplazar", MVM + " ¿Qué aporta esta memoria al texto escolar inventado?", ["Aporta que ya vivían familias y regaban con acequias.", "Aporta que los colonos les quitaron parte de los pastos.", "No elimina el dato de que en 1900 llegaron colonos: lo completa."], "Aporta voces y hechos que el texto no tiene; complementa, no reemplaza."),
    ],
    mistakes=[
        M("Pensar que problematizar es decir que la historia nacional es falsa.", "Problematizar es preguntar y completar con otras miradas.", "Pregunta qué voces faltan y qué aporta cada fuente."),
        M("Concluir que todos los pueblos recuerdan lo mismo porque dos memorias se parecen.", "Dos memorias no representan a todos los pueblos.", "Escribe «en estas dos memorias»."),
    ],
    R=[
        ex("¿Qué dato aporta la memoria de doña Inés que el texto escolar no menciona? A) que en 1900 llegaron colonos B) que ya vivían familias en el valle antes de 1900", "B", "El texto sí menciona a los colonos; lo que falta es la presencia de las familias."),
        ex("Problematizar la historia nacional, ¿es hacerle preguntas o burlarse de ella?", "Hacerle preguntas", "Es mirarla con atención."),
        ex("En esta clase comparamos el texto escolar con una memoria oral. ¿Cuál de las dos cuenta doña Inés?", "La memoria oral", "Doña Inés transmite lo que recibió de su abuela."),
    ],
    C=[
        ex("Verdadero o falso: una memoria indígena puede complementar la historia nacional.", "Verdadero", "Puede aportar voces y hechos que faltan."),
        ex("¿Cuál es una buena pregunta para problematizar un texto? A) ¿qué voces faltan en este relato? B) ¿qué color tiene la portada?", "A", "Pregunta por las voces del relato."),
        ex("Verdadero o falso: complementar una fuente es lo mismo que reemplazarla.", "Falso", "Complementar agrega; reemplazar elimina."),
    ],
    A=[
        ex("Criterio: «qué voz cuenta». Texto escolar inventado: una voz externa al valle. Memoria de doña Inés: una vecina del valle. ¿Qué diferencia hay? A) las dos cuentan desde dentro B) una cuenta desde afuera y otra desde dentro de la comunidad", "B", "Las voces son distintas."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) las dos fuentes mencionan la llegada de colonos b) solo una dice que ya había familias en el valle.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Doña Inés dice: «Mi familia nunca dejó de vivir aquí». Escribe una pregunta que esa frase permite hacerle al texto escolar.", "¿Por qué el texto dice que el valle estaba deshabitado?", "La pregunta contrasta la memoria con el texto."),
    ],
    Z=[
        ex("Ana dice: «La memoria de doña Inés es mejor que el texto escolar porque es más antigua». ¿Qué falla en su comparación?", "Jerarquiza las fuentes sin un criterio común", "Comparar no es ordenar de mejor a peor."),
        ex("Un compañero escribe: «Como Valle Manso y Lago Espejo recuerdan procesos parecidos, todos los pueblos los recuerdan igual». ¿Qué debería escribir? A) «en todos los pueblos» B) «en estas dos memorias»", "B", "Dos memorias no representan a todos los pueblos."),
    ],
    D=[
        ex("Dos conclusiones. 1) «La memoria de Valle Manso agrega voces que el texto escolar no tiene». 2) «El texto escolar no sirve para nada». ¿Cuál está bien formulada?", "La primera", "La segunda descarta una fuente sin razón."),
        ex("Una compañera quiere usar la memoria de doña Inés para decir qué pasó en toda la región. ¿Qué parte de su afirmación no es válida? A) la parte que extiende un caso a toda la región B) la parte que cita a doña Inés", "A", "Un testimonio no alcanza para hablar de toda una región."),
    ],
    context=[ex("En una clase de Historia, la profesora pide completar la historia de una localidad. Una compañera propone sumar la memoria oral de una comunidad indígena, con permiso. ¿Qué aporta esa decisión? A) otra voz que puede completar la historia B) menos información", "A", "Una nueva voz complementa lo que ya se sabe.")],
    selfcheck=[
        ex("Escribe una pregunta que sirva para problematizar un texto escolar.", "Por ejemplo: ¿qué voces faltan en este relato?", "Debe preguntar por voces o por lo que falta."),
        ex("Verdadero o falso: problematizar la historia nacional es decir que todo en ella es falso.", "Falso", "Es preguntar y completar con otras miradas."),
        ex("Nombra un criterio para comparar una memoria y un texto escolar.", "Por ejemplo: qué voz cuenta", "Debe ser un punto igual para ambas fuentes."),
    ],
    task=T("Compara estas dos fuentes inventadas. Texto escolar: «En 1900 llegaron colonos al valle y comenzó el progreso». Memoria de doña Inés: «Antes de 1900 ya vivían familias en el valle; con los colonos perdimos parte de los pastos». Haz una tabla con tres criterios: «qué hecho cuenta», «qué voz tiene» y «qué aporta». Escribe una semejanza, una diferencia y una pregunta que problematice el texto escolar.",
           "Hecho: ambos mencionan la llegada de colonos. Voz: el texto, una voz externa; la memoria, una vecina del valle. Aporta: el texto marca la llegada; la memoria cuenta que ya había familias y que se perdieron pastos. Semejanza: ambos mencionan a los colonos. Diferencia: solo la memoria dice que ya vivían familias. Pregunta: ¿qué voces faltan en el texto?",
           ["usa los mismos criterios para ambas fuentes", "distingue semejanza y diferencia", "formula una pregunta problematizadora"], ["tabla de tres criterios", "semejanza, diferencia y pregunta"], ["decir que una fuente es falsa", "generalizar a todos los pueblos"],
           "Pedir que señale en cada fuente la frase que respalda su tabla; valorar que no descarte ninguna fuente."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un criterio nuevo (por ejemplo, «qué no dice la fuente») y explica por qué ayuda a problematizar.",
)

L(
    OA8, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore la memoria histórica de un pueblo y que ayude a problematizar la historia nacional, con fuente, reflexión, límite y pregunta.",
    prior=["Sé leer una memoria con límites.", "Sé contrastar una memoria con un texto escolar sin jerarquizar."],
    explain=[
        "Una respuesta atribuida que valora la memoria histórica tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Inés cuenta que…». Segundo, lo que dice el texto escolar sobre el mismo hecho. Tercero, tu reflexión sobre lo que aporta la memoria, marcada con «yo pienso que». Cuarto, un límite. Quinto, una pregunta para el educador o la educadora tradicional.",
        "Valorar la memoria histórica es reconocer que un pueblo es portador de una visión del pasado que puede completar la historia nacional. Es parte de nuestra convivencia aprender a escuchar esas voces. No significa decir que la memoria no puede equivocarse ni que el texto escolar no sirve: toda fuente se contrasta con otras.",
        "Una buena respuesta no se burla de ninguna fuente, no culpa a personas concretas y no inventa lo que la comunidad calló. Se queda en lo que sabemos y deja una pregunta para seguir aprendiendo con quienes conocen su historia. Al final, la devolvemos a la comunidad o al educador para que la revise.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("valorar", "reconocer que algo tiene importancia y algo que aportar"), ("portador de memoria", "persona o pueblo que guarda y transmite un recuerdo del pasado"), ("contrastar", "comparar dos fuentes para ver en qué coinciden y en qué difieren"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TEX + " " + MVM + " Arma una respuesta atribuida de cinco partes.", ["Dato: doña Inés cuenta que antes de 1900 ya vivían familias en el valle.", "El texto escolar inventado dice que el valle estaba deshabitado.", "Reflexión: yo pienso que la memoria de doña Inés agrega una voz que el texto no tiene.", "Límite y pregunta: no sé cuántas familias eran; preguntaré al educador tradicional."], "Respuesta con dato atribuido, texto escolar, «yo pienso que», límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «Los textos escolares siempre mienten sobre los pueblos indígenas». ¿Qué le falta a la respuesta?", ["No dice de qué fuente viene el dato.", "Generaliza con «siempre».", "No tiene límite ni pregunta."], "Le falta atribuir, no generalizar y agregar límite y pregunta."),
    ],
    mistakes=[
        M("Decir que una fuente es «la verdad» y la otra, «mentira».", "Valorar una memoria no es descartar sin contrastar.", "Atribuye cada dato y contrasta con otra fuente."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Inés? A) «Todos saben que…» B) «Doña Inés cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: la memoria histórica. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, texto escolar, reflexión, límite y pregunta."),
        ex("Verdadero o falso: mi reflexión es una idea mía y no de la memoria.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué significa valorar la memoria histórica de un pueblo? A) reconocer que tiene una visión del pasado que puede completar la historia nacional B) aceptar todo sin revisar", "A", "Valorar no es aceptar sin contrastar."),
        ex("Verdadero o falso: valorar la memoria de un pueblo significa decir que el texto escolar no sirve.", "Falso", "Toda fuente se contrasta con otras."),
        ex("Tema: la memoria histórica. ¿Para qué sirve la pregunta final? A) para terminar rápido B) para consultar al educador tradicional lo que no sé", "B", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Memoria de doña Inés: «Cuando llegaron los colonos, nos quitaron parte de los pastos». Completa la atribución: «Doña Inés cuenta que, cuando llegaron los colonos, …»", "Les quitaron parte de los pastos", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Inés cuenta que su familia nunca dejó de vivir en el valle b) yo pienso que eso muestra que la comunidad resistió.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        arith("El texto escolar inventado dice que los colonos llegaron en 1900. ¿Cuántos años pasaron hasta 1990, cuando (en esta historia inventada) las familias volvieron a sembrar chacras abandonadas?", "1990-1900", "Se restan los años."),
    ],
    Z=[
        ex("Tema: la memoria histórica. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque es una tarea de decoración B) porque conoce la historia de su pueblo y puede corregir errores", "B", "Quien conoce su historia puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Inés cuenta que su familia nunca dejó el valle; yo pienso que su memoria ayuda a preguntar qué voces faltan en el texto». 2) «Doña Inés demuestra que toda la historia nacional es falsa». ¿Cuál está bien construida?", "La primera", "La segunda exagera y no se queda en la fuente."),
        ex("Un compañero agrega a su respuesta un hecho que, según él, «seguro pasó» en Valle Manso. La memoria no lo menciona. ¿Qué debe hacer?", "Quitarlo porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre el aporte de la memoria de doña Inés a la historia del valle. ¿Qué empieza mejor? A) «Doña Inés cuenta que…» B) «Todos los pueblos indígenas dicen que…»", "A", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre memoria histórica.", "Dato de la fuente, texto escolar, reflexión, límite y pregunta", "Están en la explicación."),
        ex("Tema: la memoria histórica. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: la memoria histórica. ¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) guardarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa estas dos fuentes inventadas. Texto escolar: «En 1900 llegaron colonos al valle y comenzó el progreso». Memoria de doña Inés: «Mi abuela me contó que las familias ya cuidaban las acequias antes de 1900. Cuando llegaron los colonos perdimos parte de los pastos, pero seguimos sembrando.» Escribe una respuesta de cinco partes sobre lo que aporta la memoria de la comunidad a la historia del valle: 1) dato de doña Inés, 2) lo que dice el texto escolar, 3) tu reflexión con «yo pienso que», 4) un límite y 5) una pregunta para el educador tradicional.",
           "1) Doña Inés cuenta que las familias ya cuidaban las acequias antes de 1900. 2) El texto escolar dice que en 1900 llegaron colonos y comenzó el progreso. 3) Yo pienso que la memoria de la comunidad agrega una voz que ayuda a preguntar qué se cuenta del valle y qué no. 4) No sé cuántos pastos se perdieron. 5) Pregunta: ¿cómo cuenta mi pueblo lo que pasó cuando llegaron otros al territorio?",
           ["atribuye cada dato", "contrasta con el texto escolar sin descartarlo", "incluye límite y pregunta"], ["texto de cinco partes"], ["decir que una fuente es falsa", "no marcar la opinión propia"],
           "Pedir que señale la línea de la fuente que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu respuesta cambiando la fuente por don Mateo, de Lago Espejo, y su memoria sobre el lago.",
)

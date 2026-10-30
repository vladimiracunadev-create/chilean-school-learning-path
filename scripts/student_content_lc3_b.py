"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 16 (creación con sonoridad y visualidad, en relación con la naturaleza y los otros) y OA LF01
(comprensión de textos orales en lengua indígena).

Criterio de autoría: todas las fichas, relatos, personajes y creaciones de práctica son inventados, están en
castellano y se declaran como tales; no pertenecen a ningún pueblo. No se asocia ningún sonido, símbolo, patrón,
instrumento ni visión del mundo con un pueblo concreto: las cualidades que se estudian (fuerte, suave, curvo,
repetido) son generales y las creaciones salen del entorno propio del estudiante. No se incluye ningún texto
real en lengua indígena; la forma tradicional de crear, escuchar y contar la enseñan el educador/a
tradicional y la comunidad, y cada tarea abierta lo remite a ellos.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA16, LF1 = "LC03 OA 16", "LC03 OA LF01"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
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


# =================================================================== OA 16 · creación con sonoridad y visualidad
L(
    OA16, 1,
    materials="Lápiz, hoja y colores. Las fichas están escritas en este cuaderno y son inventadas para practicar; no son de ningún pueblo.",
    use="Aprenderé a preguntar de dónde viene una creación y qué cuidados pide. Sirve para respetar lo que pertenece a una persona o a una comunidad.",
    prior=["Sé que los pueblos originarios tienen su propia cultura y sus propios saberes.", "Sé que una fuente es la persona o el material de donde viene un dato."],
    explain=[
        "Una creación es algo nuevo que una persona hace: un dibujo, un sonido, un cartel o una canción corta. Toda creación tiene una procedencia, que es de dónde viene. También tiene una autoría, que es quién la hizo.",
        "Hay cosas que una comunidad cuida de manera especial. Eso se llama resguardo. Pueden ser símbolos, sonidos o saberes. La comunidad decide cómo, cuándo y quién puede usarlos. Yo no sé cuáles son hasta que pregunto, así que no los copio ni los uso de adorno.",
        "Para trabajar con cuidado hago una ficha de procedencia con cuatro datos: qué es, quién lo creó, si hay permiso y qué cuidado pide. Si falta un dato, no sigo: pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("creación", "algo nuevo que una persona hace"), ("procedencia", "de dónde viene algo"), ("autoría", "quién hizo una creación"), ("resguardo", "cuidado especial que una comunidad da a algo suyo"), ("permiso", "aviso de que sí puedo usar algo")],
    worked=[
        W("Leer una ficha completa", "Ficha inventada. Qué es: un dibujo de olas. Quién lo creó: Inés, de 3.º. Permiso para mostrarlo: sí. Cuidado: ninguno, es un dibujo propio. ¿Cuál es la procedencia del dibujo?", ["Busco el dato de quién lo creó.", "La ficha dice: Inés, de 3.º.", "Es un dibujo propio, no viene de otra comunidad."], "Es un dibujo propio de Inés, de 3.º"),
        W("Qué hago si falta un dato", "Tomás vio un diseño en un papel viejo. No sabe quién lo hizo ni si se puede copiar. ¿Qué debe hacer antes de copiarlo?", ["Veo que faltan la autoría y el permiso.", "Sin esos datos no puedo copiar.", "Pregunto al educador tradicional o a la comunidad."], "Preguntar de dónde viene y no copiarlo hasta tener respuesta"),
    ],
    mistakes=[
        M("Copiar un dibujo porque se ve bonito.", "No sé quién lo hizo ni si la comunidad deja copiarlo.", "Primero pregunto la procedencia y si hay permiso."),
        M("Pensar que si algo está a la vista, es libre para usarlo.", "Verlo no es lo mismo que tener permiso.", "Pido permiso y anoto quién lo creó."),
    ],
    R=[
        ex("Elige la creación: A) una nube del cielo B) un dibujo que hice de una nube.", "B", "Una creación la hace una persona; la nube existe sola."),
        ex("Ficha: «Dibujo hecho por Inés, de 3.º». ¿Quién lo hizo?", "Inés", "El dato de autoría dice quién lo creó."),
        ex("Para usar una creación de otra persona, ¿pido permiso o la copio sin avisar?", "pido permiso", "El permiso muestra respeto por su autoría."),
    ],
    C=[
        ex("Verdadero o falso: si una cosa se ve bonita, ya puedo copiarla.", "Falso", "Que se vea bonita no me da permiso."),
        ex("Ficha: «Golpes suaves en una mesa. Lo creó Mateo, de 3.º. Permiso: sí». ¿Qué dato dice que puedo usarlo?", "Permiso: sí", "La línea de permiso es la que autoriza el uso."),
        ex("¿Qué es un resguardo: A) algo que una comunidad cuida y cuyo uso decide B) algo que se bota?", "A", "Resguardo es cuidado especial de la comunidad."),
    ],
    A=[
        arith("Una ficha de procedencia tiene 4 datos. La ficha de Rosa solo tiene escritos 2. ¿Cuántos datos faltan?", "4 - 2", "Faltan los datos que no están escritos."),
        ex("Tomás encontró un diseño sin nombre de autor. ¿Qué dato necesita saber: A) quién lo creó B) cuántas hojas tiene?", "A", "Sin la autoría no sé de dónde viene."),
        ex("Ordena los pasos: A) pregunto si hay permiso B) veo la creación C) la uso solo si me dicen que puedo. Escribe las letras.", "B, A, C", "Primero veo, luego pregunto y al final uso."),
    ],
    Z=[
        ex("Ana dice: «Como no veo el nombre del autor, puedo usar el dibujo como si fuera mío». ¿Tiene razón? Responde Sí o No.", "No", "Que falte el nombre no es un permiso."),
        ex("Hay dos creaciones. 1) Un dibujo de Inés con permiso escrito. 2) Un símbolo en un papel sin autor ni permiso. ¿Cuál puedes poner en el cartel del curso sin dudar?", "1", "La 1 tiene autoría y permiso; la 2 no."),
    ],
    D=[
        arith("Un curso tiene 5 creaciones. Tres tienen la ficha completa. ¿Cuántas fichas faltan por completar?", "5 - 3", "Faltan las que no están completas."),
        ex("Mateo copió un símbolo de un papel y lo puso de adorno en un afiche, sin preguntar. ¿Qué se saltó: preguntar la procedencia o dibujar con lápiz?", "preguntar la procedencia", "Debió saber de dónde viene antes de copiar."),
    ],
    context=[ex("En tu sala hay un cartel viejo con un dibujo sin firma. Un compañero quiere copiarlo para la fiesta del curso. ¿Qué le dices: «Preguntemos de dónde viene» o «Cópialo igual»?", "«Preguntemos de dónde viene»", "Sin procedencia ni permiso no se copia.")],
    selfcheck=[
        ex("¿Cómo se llama el dato que dice de dónde viene una creación?", "procedencia", "Procedencia significa de dónde viene."),
        ex("¿Qué dato anoto para saber quién hizo una creación?", "la autoría", "La autoría dice quién la creó."),
        ex("Si no sé si puedo copiar un símbolo, ¿qué hago?", "pregunto al educador tradicional o a la comunidad", "Ellos pueden decir si hay resguardo."),
    ],
    task=T(
        "Haz una ficha de procedencia de un dibujo tuyo de las olas del mar. Escribe cuatro datos: qué es, quién lo creó (tú), si das permiso para mostrarlo (sí o no, según tu decisión) y qué cuidado pide. Después escribe una pregunta para el educador tradicional sobre un símbolo que no sepas si se puede copiar.",
        "Qué es: dibujo de olas. Quién lo creó: yo. Permiso: sí, para el curso. Cuidado: ninguno, es propio. Pregunta: ¿hay símbolos que no se deben copiar?",
        ["completa los cuatro datos de la ficha", "indica su propia autoría", "escribe una pregunta al educador/a tradicional"],
        ["ficha escrita en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["dejar datos en blanco", "copiar un símbolo de otra persona en vez de dibujar uno propio"],
        "Valora que reconoció procedencia y permiso; si copió un símbolo ajeno, pídele que dibuje solo líneas propias y pregunte a quien enseña.",
    ),
    reinforce="Mira un dibujo tuyo y di en voz alta sus cuatro datos: qué es, quién lo creó, si hay permiso y qué cuidado pide.",
    extend="Explica a una persona de tu casa por qué no basta con que un dibujo se vea bonito para copiarlo.",
)

L(
    OA16, 2,
    materials="Lápiz, hoja y un lugar tranquilo de tu casa o de la escuela para escuchar. Los datos de práctica están escritos aquí y son inventados.",
    use="Aprenderé a notar cualidades de los sonidos y de las formas del entorno, como fuerte o suave, curvo o recto. Sirve para crear con ideas propias sin copiar símbolos de otros.",
    prior=["Sé que toda creación tiene procedencia y autoría.", "Sé que no copio símbolos sin preguntar."],
    explain=[
        "Un sonido tiene cualidades. Puede ser fuerte o suave, rápido o lento, largo o corto. La lluvia fina suena suave y con muchos golpecitos cortos. Un portazo suena fuerte y corto.",
        "Una forma que veo también tiene cualidades. Una línea puede ser recta, curva u ondulada. Puede repetirse muchas veces o aparecer una sola vez. Las olas del mar, por ejemplo, se ven como líneas curvas que se repiten.",
        "Explorar es mirar y escuchar con calma y anotar lo que noto. Anoto cualidades, no copio símbolos. Un símbolo puede tener un significado que no conozco o ser un resguardo de una comunidad. Mis líneas y mis sonidos pueden ser propios. Cada pueblo originario tiene además sonidos y formas propios; esos los enseñan su educador o educadora tradicional y su comunidad, y aquí no los reemplazo.",
    ],
    vocab=[("cualidad", "cómo es algo: fuerte, suave, curvo, recto"), ("explorar", "mirar y escuchar con calma para descubrir"), ("rápido", "que va con poco tiempo entre un golpe y otro"), ("ondulada", "línea que sube y baja como una ola"), ("símbolo", "dibujo o sonido que representa una idea")],
    worked=[
        W("Cualidades de un sonido", "Ficha: la lluvia fina hace muchos golpecitos cortos y suaves sobre el techo. ¿Qué cualidades tiene ese sonido?", ["Leo la ficha: golpecitos cortos.", "También dice que son suaves.", "Hay muchos, uno tras otro."], "Corto, suave y repetido"),
        W("De la cualidad a mi línea", "Ficha: el viento en las hojas hace un sonido suave y largo que sube y baja. ¿Qué línea mía puede mostrar eso sin copiar un símbolo?", ["Busco una línea que sea larga y que suba y baje.", "Una línea ondulada larga sirve.", "La dibujo con mi mano, no la copio de otro lado."], "Una línea ondulada y larga hecha por mí"),
    ],
    mistakes=[
        M("Copiar un símbolo que vi para mostrar un sonido.", "Puede tener un significado o un resguardo que no conozco.", "Muestro la cualidad con mis propias líneas."),
        M("Decir «suena bonito» y nada más.", "No describe cómo es el sonido.", "Digo si es fuerte o suave, rápido o lento, largo o corto."),
    ],
    R=[
        ex("La lluvia fina suena suave. ¿«Suave» es una cualidad del sonido o un animal?", "una cualidad del sonido", "Suave dice cómo suena."),
        ex("Un portazo suena fuerte y corto. ¿Cuál de las dos palabras dice cuánto dura?", "corto", "Corto dice la duración; fuerte dice el volumen."),
        ex("Una línea que sube y baja como una ola se llama: A) recta B) ondulada.", "B", "Ondulada sube y baja."),
    ],
    C=[
        ex("Ficha: «Una gota cae de la llave cada vez que cuento hasta 5». ¿El sonido es rápido o lento?", "lento", "Pasa mucho tiempo entre una gota y la siguiente."),
        ex("Verdadero o falso: para mostrar un sonido suave, debo copiar un símbolo de otra cultura.", "Falso", "Puedo usar líneas y sonidos propios."),
        ex("Ficha: «Las olas se ven como líneas curvas que se repiten». ¿Qué dos cualidades tiene esa forma?", "curva y repetida", "La ficha dice curvas y que se repiten."),
    ],
    A=[
        ex("Ficha: «El viento en las hojas hace un sonido largo y suave». ¿Qué línea elegirías para dibujarlo: A) una línea larga y suave B) un punto fuerte?", "A", "La línea larga y suave muestra las mismas cualidades."),
        arith("En un minuto de escucha, Sofía anotó 7 golpecitos de lluvia en el techo y 5 pasos en el patio. ¿Cuántos sonidos anotó en total?", "7 + 5", "Sumo los golpecitos y los pasos."),
        ex("Une cada sonido con su cualidad. 1) un portazo 2) un susurro. Cualidades: fuerte, suave. Escribe las dos cualidades en orden.", "fuerte, suave", "Un portazo suena fuerte y un susurro suena suave."),
    ],
    Z=[
        ex("Luis dice: «Voy a dibujar el viento con un símbolo que vi en un papel». ¿Qué le falta saber antes?", "de dónde viene el símbolo", "Debe conocer su procedencia y si hay permiso."),
        ex("Dos niñas describen la lluvia. Rita: «Es bonita». Lola: «Son golpecitos suaves, cortos y rápidos». ¿Quién describió mejor las cualidades?", "Lola", "Lola dice cómo es el sonido."),
    ],
    D=[
        ex("Un sonido es fuerte, largo y se repite 3 veces. Otro es suave, corto y se repite 3 veces. ¿En qué cualidad se parecen?", "se repiten 3 veces", "Las otras cualidades son distintas."),
        arith("Anotaste 4 sonidos fuertes y 6 sonidos suaves del patio. ¿Cuántos sonidos suaves hay más que fuertes?", "6 - 4", "Resto los fuertes de los suaves."),
    ],
    context=[ex("Estás en tu patio y suena el viento. Quieres dibujar lo que oyes. ¿Qué haces primero: anoto sus cualidades o copio un símbolo de un cuaderno viejo?", "anoto sus cualidades", "Primero escucho y describo con mis palabras.")],
    selfcheck=[
        ex("Nombra una cualidad de un sonido.", "fuerte, suave, rápido, lento, largo o corto", "Cualquiera de esas palabras dice cómo es un sonido."),
        ex("¿Qué hago con las cualidades que noto: las anoto o las copio de otra persona?", "las anoto", "Las observo yo y las escribo."),
        ex("¿Puedo usar mis propias líneas para mostrar un sonido?", "Sí", "Mis líneas son una creación propia."),
    ],
    task=T(
        "Escucha tu entorno durante dos minutos: puede ser la lluvia, el viento, el agua de la llave o tus propios pasos. Anota en dos columnas: «Lo que oí» y «Sus cualidades» (fuerte o suave, rápido o lento, largo o corto). Después dibuja con líneas propias una de las cualidades. No copies ningún símbolo que no hayas inventado tú.",
        "Lo que oí: agua de la llave. Cualidades: suave, lento, gota corta. Dibujo: puntos separados con una línea corta debajo de cada uno.",
        ["anota al menos un sonido con dos cualidades", "las cualidades son observables", "su dibujo usa líneas propias", "no copia símbolos"],
        ["tabla con dos columnas", "dibujo de las líneas"],
        ["decir solo «suena bonito»", "copiar un símbolo ajeno"],
        "Reconoce que describió cualidades con sus palabras; si copió un símbolo, invítalo a inventar sus propias líneas.",
    ),
    reinforce="Cierra los ojos un minuto y di en voz alta tres cualidades de un sonido que oigas.",
    extend="Escucha dos sonidos distintos de tu casa y di en qué cualidad se parecen y en cuál se diferencian.",
)

L(
    OA16, 3,
    materials="Lápiz, hoja y colores. Para el sonido, tus palmas o golpecitos suaves con un lápiz sobre una hoja doblada. Los datos de práctica son inventados.",
    use="Aprenderé a crear una pieza breve de sonido y dibujo a partir de mi lugar. Sirve para expresar lo que observo de la naturaleza y compartirlo con otros.",
    prior=["Sé nombrar cualidades de sonidos y formas.", "Sé que no copio símbolos sin permiso."],
    explain=[
        "Crear una respuesta propia es hacer algo nuevo desde lo que yo observé. Es situada cuando sale de mi lugar: mi patio, mi plaza o mi ventana. No tomo la creación de otro lugar ni de otra persona para decir que es mía.",
        "Sigo cuatro pasos. Uno: elijo un elemento de la naturaleza que pueda ver o escuchar cerca, como la lluvia, el viento o un árbol. Dos: anoto tres cualidades. Tres: hago un sonido corto con mis palmas y un dibujo con esas cualidades. Cuatro: pienso con quién lo comparto.",
        "Una creación puede relacionarse con la naturaleza porque nace de lo que observo en ella. También se relaciona con los otros cuando la comparto, escucho sus ideas y cuido los permisos. Compartir no significa publicar: primero lo muestro en mi curso o en mi casa.",
    ],
    vocab=[("situada", "hecha desde mi lugar y lo que observé en él"), ("elemento", "parte de la naturaleza, como el viento o un árbol"), ("pieza", "creación corta y terminada"), ("compartir", "mostrar mi trabajo a otros con cuidado"), ("relación", "unión entre dos cosas o personas")],
    worked=[
        W("Armar el plan de una pieza", "Rosa eligió la lluvia. Anotó tres cualidades: suave, corta y repetida. ¿Qué sonido con las palmas puede hacer?", ["Busco un sonido suave: palmas muy despacio.", "Busco uno corto y repetido: golpecitos breves, uno tras otro.", "Lo ensayo tres veces."], "Palmadas suaves, cortas y repetidas"),
        W("Qué parte es situada", "Pedro dice: «Mi dibujo muestra el viento que mueve el árbol de mi patio». ¿Qué lo hace situado?", ["Veo de dónde sale: del árbol de su patio.", "Pedro lo observó él mismo.", "No lo tomó de otro lugar."], "Sale de lo que Pedro observó en su patio"),
    ],
    mistakes=[
        M("Hacer un dibujo con un patrón que vi en un libro y decir que es mío.", "La idea no salió de lo que yo observé.", "Dibujo lo que veo y escucho en mi lugar."),
        M("Publicar mi pieza en internet de inmediato.", "Primero debo pedir permiso a un adulto y cuidar mis datos.", "La muestro en mi curso o en mi casa."),
    ],
    R=[
        ex("Elige un elemento de la naturaleza: A) el viento B) una silla.", "A", "El viento es naturaleza; la silla es un objeto."),
        ex("Una pieza situada sale de: A) mi lugar y lo que observé B) un dibujo de otro lugar.", "A", "Situada quiere decir desde mi lugar."),
        ex("¿Con las palmas puedo hacer un sonido suave o solo fuerte?", "suave", "Con las palmas puedo golpear despacio o fuerte."),
    ],
    C=[
        ex("Verdadero o falso: compartir mi pieza es lo mismo que publicarla en internet.", "Falso", "Compartir puede ser mostrarla en el curso o en mi casa."),
        ex("Plan de Ana: elemento: lluvia; cualidades: suave, corta, repetida. ¿Qué elemento eligió?", "la lluvia", "El plan lo dice al comienzo."),
        ex("¿Cuántas cualidades anota el plan de la clase: 2 o 3?", "3", "La clase pide tres cualidades."),
    ],
    A=[
        ex("Plan: elemento: viento; cualidades: largo, suave, sube y baja. ¿Qué sonido con tu voz sirve: A) un «uuu» largo y suave que sube y baja B) un grito corto?", "A", "Muestra largo, suave y que sube y baja."),
        arith("Tu pieza dura 3 golpecitos de palma, luego una pausa y otra vez 3 golpecitos. ¿Cuántos golpecitos hay en total?", "3 + 3", "Sumo los dos grupos de golpecitos."),
        ex("Plan: elemento: lluvia; cualidades: suave y repetida. ¿Qué dibujo sirve: A) un círculo grande y fuerte B) muchas rayitas finas, todas iguales?", "B", "Las rayitas finas se repiten y son suaves."),
    ],
    Z=[
        ex("Pedro dice: «Mi pieza es situada porque usé el patrón de otra cultura». ¿Tiene razón? Responde Sí o No.", "No", "Situada es desde mi lugar y mi observación."),
        ex("Una niña quiere mostrar su pieza. ¿Qué es mejor primero: mostrarla a su curso o subirla a una red sin permiso?", "mostrarla a su curso", "Compartir con cuidado y con un adulto cerca."),
    ],
    D=[
        ex("Elena tiene tres pasos escritos al revés: C) comparto con mi curso A) anoto tres cualidades B) elijo un elemento. Ordénalos.", "B, A, C", "Elijo, anoto cualidades y recién después comparto."),
        arith("En tu dibujo hay 4 líneas curvas y cada una se repite 3 veces. ¿Cuántas líneas curvas dibujaste?", "4 * 3", "Cuatro líneas por tres repeticiones."),
    ],
    context=[ex("Mañana tu curso muestra sus piezas. Tu pieza usa el sonido de la lluvia que oíste en tu casa. ¿Qué dices al comenzar: «Esto salió de la lluvia de mi casa» o «Esto lo copié de un libro»?", "«Esto salió de la lluvia de mi casa»", "Explico que la pieza nació de mi observación.")],
    selfcheck=[
        ex("¿De dónde sale una respuesta situada?", "de mi lugar", "Se hace desde lo que observo cerca."),
        ex("¿Cuántos pasos tiene la clase para crear la pieza?", "4", "Elegir, anotar, hacer y compartir son cuatro."),
        ex("¿Dónde muestro primero mi pieza?", "en mi curso o en mi casa", "Primero la comparto con cuidado."),
    ],
    task=T(
        "Crea una pieza breve. Paso 1: elige un elemento de la naturaleza que veas o escuches cerca. Paso 2: anota tres cualidades. Paso 3: haz con las palmas un sonido corto que muestre esas cualidades y dibuja una forma con líneas propias. Paso 4: escribe con quién la compartirás. No copies símbolos ni sonidos de otras personas.",
        "Elemento: viento en el patio. Cualidades: largo, suave, sube y baja. Sonido: palmas lentas y suaves. Dibujo: línea ondulada larga. La compartiré con mi curso.",
        ["elige un elemento de su entorno", "anota tres cualidades", "el sonido y el dibujo muestran esas cualidades", "no copia símbolos"],
        ["hoja con plan, dibujo y registro del sonido", "demostración breve ante el curso o la familia"],
        ["copiar un patrón ajeno", "publicar la pieza sin permiso"],
        "Valora que la pieza salió de su observación; si copió un símbolo, pídele que invente sus propias líneas.",
    ),
    reinforce="Haz un sonido con tus palmas que sea suave y lento y otro que sea fuerte y rápido. Dile a alguien cuál es cuál.",
    extend="Cambia tu pieza: elige otro elemento de la naturaleza y cuenta qué cualidades cambian.",
)

L(
    OA16, 4,
    materials="Tu pieza de la clase anterior, lápiz y hoja. Las frases modelo están escritas aquí.",
    use="Aprenderé a explicar por qué tomé mis decisiones, cómo mi creación se relaciona con la naturaleza y con otros, y dónde están mis límites. Sirve para presentar mi trabajo con honestidad.",
    prior=["Sé hacer una pieza breve desde mi lugar.", "Sé que algunas cosas las enseña el educador tradicional."],
    explain=[
        "Explicar mi creación es contar lo que hice y por qué. Uso frases cortas: «Elegí… porque…». Así otras personas entienden mis decisiones y no tienen que adivinar.",
        "También explico mis relaciones. Con la naturaleza: «Mi pieza nació de…». Con los otros: «La compartí con… y escuché…». Una relación es la unión entre dos cosas, o entre personas.",
        "Digo mis límites. Un límite es lo que no hice o no sé. Puedo decir: «No copié símbolos de otras personas» o «No sé qué significa esto, se lo pregunto a la educadora tradicional». Decir un límite no es un error: es respeto y honestidad.",
    ],
    vocab=[("explicar", "decir lo que hice y por qué"), ("decisión", "elección que hice yo"), ("límite", "lo que no hice o no sé"), ("honestidad", "decir la verdad sobre mi trabajo"), ("relación", "unión entre dos cosas o personas")],
    worked=[
        W("Una explicación completa", "Explicación de Rosa: «Elegí la lluvia porque la oí ayer. Mi pieza nació de ese sonido. La compartí con mi curso. No copié símbolos de otras personas». ¿Cuántas partes tiene: decisión, relación con la naturaleza, relación con otros y límite?", ["Decisión: elegí la lluvia.", "Naturaleza: nació de ese sonido. Otros: la compartió con su curso.", "Límite: no copió símbolos."], "Tiene las 4 partes"),
        W("Falta un límite", "Explicación de Mateo: «Elegí el viento porque lo oí. Mi pieza nació de ese sonido. La compartí con mi hermana». ¿Qué parte falta?", ["Veo decisión: elegí el viento.", "Veo naturaleza y otros: nació del sonido y la compartió.", "No dice qué no hizo o qué no sabe."], "Falta el límite"),
    ],
    mistakes=[
        M("Decir «lo hice porque sí».", "Nadie entiende mi decisión.", "Uso «Elegí… porque…» y doy una razón."),
        M("Guardar silencio sobre algo que no sé.", "Parece que sé más de lo que sé.", "Digo mi límite y a quién preguntaré."),
    ],
    R=[
        ex("Completa: «Elegí el viento ____ lo oí ayer». Elige: porque o pero.", "porque", "«Porque» da la razón de la decisión."),
        ex("Un límite es: A) lo que no hice o no sé B) lo que hice mejor.", "A", "Límite es lo que no hice o no sé."),
        ex("«La compartí con mi curso». ¿Esta frase habla de la naturaleza o de otros?", "otros", "Habla de con quién la compartió."),
    ],
    C=[
        ex("Frase: «No copié símbolos de otras personas». ¿Es una decisión, una relación o un límite?", "un límite", "Dice lo que no hizo."),
        ex("Frase: «Mi pieza nació de la lluvia de mi patio». ¿Se relaciona con la naturaleza o con otros?", "con la naturaleza", "Dice que nació de la lluvia."),
        ex("Verdadero o falso: decir un límite es un error.", "Falso", "Decir un límite es honesto y respetuoso."),
    ],
    A=[
        arith("Una explicación completa tiene 4 partes. La de Mateo tiene 3. ¿Cuántas partes le faltan?", "4 - 3", "Resto las partes que ya tiene."),
        ex("Elige la mejor explicación: A) «Elegí la lluvia porque la oí; la compartí con mi curso; no copié símbolos.» B) «Está bien así.»", "A", "A da razones, relaciones y un límite."),
        ex("Completa con un límite: «No sé qué significa este dibujo, se lo ____ a la educadora tradicional». Elige: pregunto o invento.", "pregunto", "Si no sé, pregunto."),
    ],
    Z=[
        ex("Luis dice: «Si digo que no sé algo, mi trabajo vale menos». ¿Tiene razón? Responde Sí o No.", "No", "Decir lo que no sé muestra honestidad."),
        ex("Una niña dice: «Mi pieza es igual a la de una cultura que vi». ¿Qué pregunta debe responder primero: de dónde viene o cuánto mide?", "de dónde viene", "Debe saber la procedencia y si hay resguardo."),
    ],
    D=[
        ex("Ordena las frases de una explicación: C) No copié símbolos. A) Elegí el viento porque lo oí. B) La compartí con mi curso. Escribe las letras en el orden decisión, otros, límite.", "A, B, C", "A es la decisión, B es relación con otros y C es el límite."),
        arith("Tienes una explicación de 4 frases y cada frase tiene 6 palabras. ¿Cuántas palabras tiene en total?", "4 * 6", "Cuatro frases por seis palabras."),
    ],
    context=[ex("Un compañero te pregunta de dónde sacaste tu dibujo. Tú lo hiciste mirando el árbol de tu patio. ¿Qué respondes: «Lo hice mirando el árbol de mi patio» o «No sé»?", "«Lo hice mirando el árbol de mi patio»", "Explico mi procedencia con honestidad.")],
    selfcheck=[
        ex("¿Qué palabra uso para dar una razón: porque o aunque?", "porque", "«Porque» da la razón."),
        ex("¿Cómo se llama lo que no hice o no sé?", "límite", "El límite es lo que no hice o no sé."),
        ex("¿Con quién puedo consultar lo que no sé de una cultura?", "el educador tradicional o la comunidad", "Ellos pueden enseñarlo."),
    ],
    task=T(
        "Usa tu pieza de la clase 3 o esta pieza inventada: elemento: viento; cualidades: largo, suave; sonido: palmas lentas; dibujo: línea ondulada. Escribe cuatro frases: 1) «Elegí… porque…». 2) «Mi pieza nació de…». 3) «La compartí con…». 4) un límite: «No copié… / No sé… y lo preguntaré a…». Léelas en voz alta a alguien.",
        "Elegí el viento porque lo oí en el patio. Mi pieza nació del viento en las hojas. La compartí con mi curso. No sé qué significa un símbolo de un libro viejo y lo preguntaré a la educadora tradicional.",
        ["escribe las cuatro frases", "da una razón con «porque»", "nombra con quién la comparte", "dice un límite honesto"],
        ["cuatro frases escritas", "lectura en voz alta"],
        ["no dar razones", "no decir ningún límite"],
        "Reconoce la honestidad de su explicación; si no dijo un límite, pregúntale qué no sabe y a quién se lo preguntaría.",
    ),
    reinforce="Cuéntale a alguien en una sola frase por qué elegiste el elemento de tu pieza.",
    extend="Escribe un límite más sobre tu trabajo y a qué persona le consultarías.",
)

# =================================================================== LF01 · comprensión de textos orales en lengua indígena
L(
    LF1, 1,
    materials="Lápiz y hoja. Las fichas son inventadas para practicar y están en castellano; no hay ningún relato real de un pueblo. El educador o la educadora tradicional es quien comparte los relatos de su comunidad.",
    use="Aprenderé a preguntar quién cuenta, de qué pueblo viene lo que se cuenta y en qué momento se cuenta. Sirve para escuchar textos orales en lengua indígena con respeto.",
    prior=["Sé que hay pueblos originarios con sus propias lenguas.", "Sé que una fuente es la persona de donde viene un dato."],
    explain=[
        "Un texto oral es algo que se dice en voz alta y se recibe escuchando. Puede ser un saludo, una conversación breve o un relato. Muchas lenguas indígenas se han conservado porque las personas las cuentan y las recuerdan de viva voz.",
        "Antes de escuchar, situamos el texto. Situar es ubicar tres cosas. La voz: quién lo cuenta. El pueblo: de qué pueblo es lo que se cuenta, según lo diga la persona. El contexto: cuándo, dónde y para qué se cuenta. También pregunto si hay permiso para escuchar y para hablar de lo que escuché.",
        "Un relato de un pueblo no es de todos los pueblos. Tampoco es un material sin dueño. Si no sé de qué pueblo es, no lo adivino: lo anoto en la ficha como «lo dirá la persona que cuenta» y pregunto.",
    ],
    vocab=[("texto oral", "algo que se dice en voz alta"), ("voz", "la persona que cuenta o habla"), ("contexto", "cuándo, dónde y para qué se cuenta algo"), ("situar", "ubicar voz, pueblo y contexto antes de escuchar"), ("relato", "historia que se cuenta")],
    worked=[
        W("Leer una ficha situada", "Ficha inventada. Voz: Elena, educadora tradicional de la escuela. Pueblo: lo dirá ella. Dónde y cuándo: en la sala, a la mañana. Permiso para escuchar: sí. ¿Quién es la voz?", ["Busco la palabra «Voz» en la ficha.", "Dice: Elena, educadora tradicional.", "Ella es quien cuenta."], "Elena, educadora tradicional de la escuela"),
        W("Lo que no se debe adivinar", "En la ficha de Luis, en «Pueblo» no hay nada escrito. Luis quiere escribir el nombre de un pueblo que cree conocer. ¿Qué hace?", ["Veo que el dato no está.", "Un nombre adivinado puede estar equivocado.", "Escribo «lo dirá la persona que cuenta» y pregunto."], "Anota que lo dirá la persona que cuenta y pregunta"),
    ],
    mistakes=[
        M("Escribir el pueblo de un relato sin que nadie lo haya dicho.", "Puedo atribuir el relato a un pueblo equivocado.", "Espero a que la voz lo diga o lo pregunto."),
        M("Pensar que un relato es de todos y se puede contar sin pedir permiso.", "Un relato tiene una voz y una comunidad que lo cuidan.", "Pregunto si puedo hablar de lo que escuché."),
    ],
    R=[
        ex("Ficha: «Voz: Elena, educadora tradicional». ¿Quién cuenta?", "Elena", "La voz es la persona que cuenta."),
        ex("Situar un texto es ubicar: A) voz, pueblo y contexto B) solo los colores.", "A", "Situar es ubicar voz, pueblo y contexto."),
        ex("Antes de escuchar, ¿pregunto si hay permiso o no pregunto nada?", "pregunto si hay permiso", "El permiso es parte de situar."),
    ],
    C=[
        ex("Verdadero o falso: un relato de un pueblo es lo mismo que un relato de todos los pueblos.", "Falso", "Cada relato tiene su propio pueblo y voz."),
        ex("Ficha: «Dónde y cuándo: en la sala, a la mañana». ¿Esa línea habla de voz o de contexto?", "de contexto", "Dice dónde y cuándo se cuenta."),
        ex("Ficha: «Pueblo: lo dirá la persona que cuenta». ¿Quién dirá de qué pueblo es?", "la persona que cuenta", "La ficha deja el dato a quien cuenta."),
    ],
    A=[
        arith("Una ficha situada tiene 4 datos: voz, pueblo, contexto y permiso. La de Ana tiene escritos 3. ¿Cuántos faltan?", "4 - 3", "Resto los datos escritos de los cuatro."),
        ex("Ficha: «Voz: don Carlos, narrador de la comunidad. Pueblo: lo dirá él. Permiso para escuchar: sí». ¿Qué dato falta para estar completa: A) contexto B) un dibujo?", "A", "Faltan dónde y cuándo se cuenta."),
        ex("Une cada dato con su pregunta. 1) voz 2) contexto. Preguntas: A) ¿quién cuenta? B) ¿cuándo y dónde se cuenta? Escribe las letras en orden.", "A, B", "La voz responde quién cuenta y el contexto cuándo y dónde."),
    ],
    Z=[
        ex("Tomás dice: «Si no sé el pueblo, lo escribo igual con el que me suena». ¿Tiene razón? Responde Sí o No.", "No", "Adivinar puede atribuir el relato al pueblo equivocado."),
        ex("Rosa quiere contar en su casa lo que escuchó hoy. ¿Qué debe hacer antes: preguntar si puede hacerlo o contarlo de una vez?", "preguntar si puede hacerlo", "La persona que cuenta cuida lo que comparte."),
    ],
    D=[
        ex("Ordena los pasos antes de escuchar: C) escucho con atención A) leo la ficha situada B) pregunto lo que falte. Escribe las letras.", "A, B, C", "Leo, pregunto lo que falta y después escucho."),
        ex("Dos fichas: 1) Voz: Elena; Pueblo: lo dirá ella; Permiso: sí. 2) Voz: sin nombre; Pueblo: sin dato; Permiso: sin dato. ¿Cuál está en mejores condiciones de usarse?", "1", "La ficha 1 tiene voz y permiso; la 2 no tiene datos."),
    ],
    context=[ex("Hoy viene a tu sala una persona a contar un relato de su comunidad. Un compañero pregunta: «¿Lo grabo con mi teléfono?» ¿Qué respondes: «Primero preguntemos si hay permiso» o «Claro, grábalo»?", "«Primero preguntemos si hay permiso»", "Grabar la voz de alguien requiere permiso.")],
    selfcheck=[
        ex("¿Cuáles son las tres cosas que situamos antes de escuchar?", "voz, pueblo y contexto", "Son los tres datos de la ficha situada."),
        ex("Si no sé de qué pueblo es un relato, ¿qué hago?", "lo pregunto", "No adivino; pregunto a la voz o al educador."),
        ex("¿Puedo contar a otros lo que escuché sin preguntar?", "No", "Primero pido permiso a quien lo contó."),
    ],
    task=T(
        "Completa esta ficha situada para una visita inventada: Voz: ____. Pueblo: ____. Dónde y cuándo: ____. Permiso para escuchar: ____. Permiso para hablar de lo escuchado: ____. Usa estos datos de práctica: la voz es Elena, educadora tradicional de tu escuela; ella dirá el pueblo; viene a la sala hoy a la mañana; ella dice que sí puedes escuchar y que preguntarás antes de hablar de lo escuchado. Después escribe una pregunta que le harías a Elena.",
        "Voz: Elena, educadora tradicional. Pueblo: lo dirá ella. Dónde y cuándo: en la sala, hoy a la mañana. Permiso para escuchar: sí. Permiso para hablar de lo escuchado: lo preguntaré. Pregunta: ¿puedo contar a mi familia lo que escuché?",
        ["completa los cinco datos con los de práctica", "no inventa un pueblo", "escribe una pregunta para quien enseña"],
        ["ficha escrita", "pregunta escrita o dicha en voz alta"],
        ["escribir un pueblo que nadie dijo", "dejar el permiso en blanco"],
        "Valora que situó voz, pueblo y contexto; si adivinó el pueblo, ayúdalo a escribir que lo dirá la persona que cuenta.",
    ),
    reinforce="Con ayuda de alguien, lee la ficha de Elena y señala con el dedo dónde dice la voz y dónde dice el contexto.",
    extend="Escribe dos preguntas más que harías a una persona que viene a contar un relato antes de escucharla.",
)

L(
    LF1, 2,
    materials="Lápiz y hoja. Un adulto lee en voz alta el relato inventado de esta clase, que está escrito aquí en castellano. Es solo para practicar la escucha y no es de ningún pueblo.",
    use="Aprenderé a escuchar un relato la primera vez solo para disfrutarlo. Sirve para prestar atención a la voz y a las emociones antes de analizar.",
    prior=["Sé situar voz, pueblo y contexto.", "Sé que para hablar de lo escuchado pido permiso."],
    explain=[
        "La primera vez que escucho un relato, solo disfruto. No tomo apuntes ni hago preguntas. Pongo atención a la voz: si es suave o fuerte, rápida o lenta, y cómo se cuentan las pausas.",
        "Aunque no entienda todas las palabras de una lengua nueva, puedo disfrutar. La voz, el ritmo y los gestos de quien cuenta también comunican. Escuchar sin entender todo no es un error: es el comienzo de aprender.",
        "Al terminar, espero unos segundos en silencio. Después digo qué sentí con una palabra, como alegría, calma, sorpresa o curiosidad. Sentir lo que sentí está bien, y no tiene una respuesta correcta única. Solo en una segunda escucha buscaré los detalles.",
    ],
    vocab=[("disfrutar", "gozar de lo que escucho sin apuro"), ("pausa", "momento de silencio mientras se cuenta"), ("ritmo", "qué tan rápido o lento va la voz"), ("emoción", "lo que siento, como alegría o calma"), ("atención", "mirar y escuchar con todo el cuidado")],
    worked=[
        W("Escuchar la primera vez", "El adulto lee en voz baja y lenta: «Una gota de lluvia quería llegar al mar. Bajó por el techo, por la calle y por el río». ¿Qué hago la primera vez: tomo apuntes o escucho y disfruto?", ["Recuerdo que la primera vez solo disfruto.", "Pongo atención a la voz baja y lenta.", "Al final digo qué sentí."], "Escucho y disfruto"),
        W("Nombrar la emoción", "Después de escuchar, Rosa siente calma. ¿Cuál es una frase sencilla para decirlo?", ["Pienso en lo que sentí.", "La palabra es calma.", "Digo: «Sentí calma»."], "«Sentí calma»"),
    ],
    mistakes=[
        M("Tomar apuntes de todo en la primera escucha.", "Me pierdo la voz y lo que siento.", "La primera vez solo escucho; los detalles vienen después."),
        M("Pensar que si no entiendo todas las palabras, no sirve escuchar.", "La voz, el ritmo y los gestos también dicen cosas.", "Escucho con atención y disfruto lo que sí entiendo."),
    ],
    R=[
        ex("La primera vez que escucho un relato, ¿disfruto o escribo todo?", "disfruto", "La primera escucha es para disfrutar."),
        ex("Un momento de silencio mientras alguien cuenta se llama: A) pausa B) ritmo.", "A", "La pausa es el silencio breve."),
        ex("Si siento alegría después de escuchar, ¿eso es una emoción o un animal?", "una emoción", "Alegría es algo que siento."),
    ],
    C=[
        ex("Verdadero o falso: si no entiendo todas las palabras de una lengua, no puedo disfrutar de la voz.", "Falso", "Puedo disfrutar de la voz, el ritmo y los gestos."),
        ex("El adulto lee: «La gota bajó por el techo, por la calle y por el río». ¿Hacia dónde quería ir la gota, según el relato de práctica?", "al mar", "El relato dice que quería llegar al mar."),
        ex("La voz va despacio y baja. ¿Qué cualidad tiene el ritmo: lento o rápido?", "lento", "Despacio quiere decir lento."),
    ],
    A=[
        ex("Después de escuchar, ¿qué me conviene decir: A) «Sentí calma» B) «No sentí nada y por eso tengo la respuesta incorrecta»?", "A", "Digo lo que sentí; no hay respuesta única."),
        arith("En el relato de práctica, el adulto hizo 3 pausas en cada una de las 2 partes. ¿Cuántas pausas hizo?", "3 * 2", "Tres pausas por dos partes."),
        ex("Ordena: B) digo una palabra sobre lo que sentí A) escucho sin interrumpir C) espero unos segundos en silencio. Escribe las letras.", "A, C, B", "Escucho, espero en silencio y después digo lo que sentí."),
    ],
    Z=[
        ex("Tomás interrumpe el relato para preguntar el significado de cada palabra. ¿Qué le conviene hacer la primera vez: seguir escuchando o interrumpir de nuevo?", "seguir escuchando", "La primera vez es para disfrutar; las preguntas vienen después."),
        ex("Dos niñas dicen cómo se sintieron: una calma y otra curiosidad. ¿Cuál de las dos está equivocada?", "ninguna", "Cada persona puede sentir distinto."),
    ],
    D=[
        ex("El adulto cuenta un relato dos veces. ¿Para qué es la primera escucha y para qué la segunda? Elige: A) disfrutar y luego buscar detalles B) buscar detalles y luego disfrutar.", "A", "Primero disfruto y recién después busco detalles."),
        arith("Escuchaste un relato de 4 minutos y otro de 3 minutos. ¿Cuántos minutos escuchaste en total?", "4 + 3", "Sumo los dos relatos."),
    ],
    context=[ex("Una visita cuenta un relato en tu sala. Tú no entiendes algunas palabras y te da vergüenza. ¿Qué haces: sigo escuchando con atención o me tapo los oídos?", "sigo escuchando con atención", "Puedo disfrutar de la voz y entender lo que pueda.")],
    selfcheck=[
        ex("¿Qué hago la primera vez que escucho un relato?", "disfruto", "La primera escucha es para disfrutar."),
        ex("¿Cómo se llama lo que siento, como calma o alegría?", "emoción", "Esa palabra nombra lo que siento."),
        ex("¿Puedo disfrutar de una voz aunque no entienda todas las palabras?", "Sí", "La voz y el ritmo también comunican."),
    ],
    task=T(
        "Pídele a una persona de tu casa que lea en voz alta este relato inventado, despacio: «Una gota quería llegar al mar. Bajó por el techo. Bajó por la calle. Bajó por el río. Al final vio el mar y se quedó quieta». Escucha solo para disfrutar. Después escribe una palabra para lo que sentiste y una cualidad de la voz (suave o fuerte, rápida o lenta).",
        "Sentí calma. La voz era suave y lenta.",
        ["escucha una vez sin interrumpir", "nombra una emoción propia", "describe una cualidad de la voz"],
        ["dos palabras escritas en el cuaderno", "conversación breve"],
        ["interrumpir para pedir significados", "decir que debe sentir algo en particular"],
        "Acepta cualquier emoción honesta; si interrumpió, invítalo a esperar al final y a decir lo que sintió.",
    ),
    reinforce="Escucha con los ojos cerrados una canción tranquila de tu casa y di una palabra sobre lo que sentiste.",
    extend="Cuéntale a alguien qué sentiste con el relato y por qué crees que lo sentiste.",
)

L(
    LF1, 3,
    materials="Lápiz y hoja. Un adulto lee en voz alta el relato inventado de esta clase, que está escrito aquí. Es un cuento de práctica y no pertenece a ningún pueblo.",
    use="Aprenderé a reconstruir el orden de un relato y a ver qué cosas lo unen. Sirve para comprender un texto oral a la segunda escucha.",
    prior=["Sé escuchar un relato para disfrutarlo.", "Sé nombrar lo que siento al escucharlo."],
    explain=[
        "Reconstruir la secuencia es decir qué pasó primero, qué pasó después y qué pasó al final. Uso palabras como primero, luego, después y al final. Así puedo contar el relato con mis palabras.",
        "También busco relaciones. Una relación une dos cosas: quién hizo algo, qué pasó por eso y con quién estaba. La palabra «porque» me ayuda a relacionar una causa con lo que pasó.",
        "En la segunda escucha puedo tomar apuntes cortos. Escribo palabras clave, no frases largas. Si no estoy seguro de algo, pido que repitan esa parte. Pedir que repitan no es un error.",
    ],
    vocab=[("secuencia", "el orden en que pasan las cosas"), ("causa", "la razón por la que algo pasa"), ("palabra clave", "palabra importante para recordar"), ("personaje", "quien hace algo en un relato"), ("reconstruir", "volver a armar el orden de un relato")],
    worked=[
        W("Ordenar un relato", "Relato inventado: Rita encontró un cerro seco. Luego llevó agua. Después las plantas crecieron. Al final hubo flores. ¿Qué pasó primero?", ["Busco la palabra «encontró».", "Antes de llevar agua, Rita encontró el cerro seco.", "Es el primer hecho."], "Rita encontró un cerro seco"),
        W("Buscar una causa", "En el relato anterior, ¿por qué crecieron las plantas?", ["Busco qué hizo Rita antes de que crecieran.", "Llevó agua.", "Lo uno con «porque»: crecieron porque Rita llevó agua."], "Porque Rita llevó agua"),
    ],
    mistakes=[
        M("Contar el final primero.", "Cambio el orden y no se entiende lo que pasó.", "Uso primero, luego, después y al final."),
        M("Escribir frases muy largas mientras escucho.", "Me pierdo lo que sigue.", "Escribo solo palabras clave."),
    ],
    R=[
        ex("Relato: Rita encontró un cerro seco. Luego llevó agua. ¿Qué hizo Rita primero?", "encontró un cerro seco", "El relato dice «luego» después de ese hecho."),
        ex("¿Qué palabra marca el último hecho: al final o primero?", "al final", "«Al final» cierra el relato."),
        ex("Una palabra importante para recordar de un relato se llama palabra: A) clave B) larga.", "A", "Palabra clave es la importante."),
    ],
    C=[
        ex("Relato: Rita encontró un cerro seco. Luego llevó agua. Después las plantas crecieron. Al final hubo flores. ¿Qué pasó después de que Rita llevó agua?", "las plantas crecieron", "Después de llevar agua vino el crecimiento."),
        ex("Verdadero o falso: en la segunda escucha escribo frases largas de todo lo que oigo.", "Falso", "Escribo solo palabras clave."),
        ex("Completa: «Las plantas crecieron ____ Rita llevó agua». Elige: porque o pero.", "porque", "«Porque» une la causa con lo que pasó."),
    ],
    A=[
        ex("Ordena los hechos con números del 1 al 4. A) Hubo flores B) Rita encontró un cerro seco C) Las plantas crecieron D) Rita llevó agua. Escribe las letras en orden.", "B, D, C, A", "Encontró, llevó agua, crecieron y hubo flores."),
        arith("En el relato, Rita llevó 3 baldes de agua en la mañana y 2 baldes en la tarde. ¿Cuántos baldes llevó en total?", "3 + 2", "Sumo los baldes de la mañana y la tarde."),
        ex("Una palabra clave del relato de Rita es: A) agua B) la.", "A", "Agua es importante para entender el relato."),
    ],
    Z=[
        ex("Luis dice: «Las flores aparecieron primero». ¿Tiene razón? Responde Sí o No.", "No", "Las flores aparecieron al final."),
        ex("Mateo dice: «Rita llevó agua porque el cerro estaba seco». ¿Esa frase relaciona causa y hecho? Responde Sí o No.", "Sí", "Une el cerro seco con llevar agua."),
    ],
    D=[
        ex("Relato de Rita. Completa: «El cerro estaba seco, entonces Rita ____». Elige: A) llevó agua B) se fue a dormir.", "A", "El relato dice que llevó agua."),
        arith("Rita dio 4 pasos para subir el cerro, 4 pasos más para regar y 2 pasos para bajar. ¿Cuántos pasos dio?", "4 + 4 + 2", "Sumo todos sus pasos."),
    ],
    context=[ex("Tu hermano menor no entendió el relato de Rita. Le dices: «Primero ____». ¿Con qué parte comienzas: Rita encontró el cerro seco o hubo flores?", "Rita encontró el cerro seco", "Un relato se cuenta desde el comienzo.")],
    selfcheck=[
        ex("¿Qué palabra me ayuda a unir una causa con lo que pasó: porque o ayer?", "porque", "«Porque» une causa y hecho."),
        ex("¿Cómo se llama el orden en que pasan las cosas?", "secuencia", "Es la secuencia del relato."),
        ex("Si no estoy seguro de una parte, ¿pido que repitan o me quedo callado?", "pido que repitan", "Preguntar ayuda a comprender."),
    ],
    task=T(
        "Pide a un adulto que lea este relato inventado dos veces: «Pedro vio que el patio estaba lleno de hojas. Tomó una escoba pequeña. Barrió las hojas en un montón. Después las puso en un rincón de las plantas. Al final el patio quedó limpio». En la segunda escucha anota tres palabras clave. Luego cuenta el relato con tus palabras con «primero», «luego» y «al final» y di una causa con «porque».",
        "Palabras clave: hojas, escoba, limpio. Primero Pedro vio las hojas. Luego las barrió. Al final el patio quedó limpio. El patio quedó limpio porque Pedro barrió.",
        ["anota tres palabras clave", "respeta el orden de los hechos", "usa «porque» para una causa"],
        ["palabras clave escritas", "relato contado en voz alta"],
        ["cambiar el orden", "agregar hechos que no estaban en el relato"],
        "Revisa que el orden coincida con el relato; si agregó hechos, pídele que vuelva a escuchar y cuente solo lo que dice el texto.",
    ),
    reinforce="Cuenta el relato de Rita con las palabras «primero», «luego» y «al final», sin cambiar el orden.",
    extend="Inventa un relato breve de tres hechos con una causa y pídele a alguien que lo cuente de vuelta en orden.",
)

L(
    LF1, 4,
    materials="Lápiz y hoja. Las opciones están escritas aquí. Los personajes y los relatos son inventados para practicar.",
    use="Aprenderé a relacionar un relato con lo que sé sin tener que contar cosas privadas. Sirve para sentirme seguro y respetar la privacidad de todos.",
    prior=["Sé reconstruir la secuencia de un relato.", "Sé que algunas cosas las cuida la comunidad."],
    explain=[
        "Cuando escucho un relato puedo relacionarlo con lo que ya sé. Lo conecto con algo que aprendí, algo que vi, algo que sentí o con un personaje inventado. Así lo entiendo mejor y lo recuerdo más.",
        "Nadie está obligado a contar cosas personales o de su familia. Puedo elegir una opción ficticia: «Pienso en un niño llamado Pablo que…». Eso me protege y me permite participar igual. Una pregunta que obliga a contar algo privado no está bien hecha.",
        "También cuido a los otros. No pido a una compañera que cuente algo de su familia ni digo de qué pueblo es. Nadie debe demostrar su identidad ni hablar una lengua para participar. Escuchamos lo que cada persona quiere compartir.",
    ],
    vocab=[("conectar", "unir lo que escucho con algo que ya sé"), ("privado", "que es personal y no se obliga a contar"), ("ficticio", "inventado, que no pasó de verdad"), ("opción", "una de varias maneras de hacer algo"), ("identidad", "lo que cada persona es y siente de sí misma")],
    worked=[
        W("Elegir una forma de conectar", "Relato inventado: una niña riega un cerro seco. Opciones: A) cuento algo privado de mi familia B) pienso en un cerro que vi C) invento un niño llamado Pablo que riega su patio. ¿Cuáles opciones no obligan a contar algo privado?", ["La A pide algo privado.", "La B usa algo que vi.", "La C usa un personaje inventado."], "B y C"),
        W("Detectar una pregunta que obliga", "Una compañera pregunta: «Cuéntanos qué problemas tiene tu familia». ¿Está bien hecha esa pregunta?", ["Veo que pide algo privado.", "Obliga a contar de la familia.", "No está bien hecha."], "No, obliga a contar algo privado"),
    ],
    mistakes=[
        M("Pedir a un compañero que cuente cosas de su familia.", "Puede ser privado y no quiere contarlo.", "Ofrezco opciones, incluso un personaje inventado."),
        M("Preguntar a alguien de qué pueblo es o si habla la lengua.", "Nadie tiene que demostrar su identidad.", "Pregunto qué le gustó del relato."),
    ],
    R=[
        ex("Conectar un relato es: A) unirlo con algo que ya sé B) olvidarlo.", "A", "Conectar es relacionar con lo que ya sé."),
        ex("«Pienso en un niño llamado Pablo» ¿es una opción ficticia o real?", "ficticia", "Pablo es un personaje inventado."),
        ex("¿Puedo participar sin contar nada privado de mi familia?", "Sí", "Puedo usar opciones que no son privadas."),
    ],
    C=[
        ex("Verdadero o falso: todos deben contar algo de su casa para participar.", "Falso", "Nadie está obligado a contar cosas privadas."),
        ex("Relato inventado: una niña riega un cerro seco. Opción: «Pienso en el pasto seco que vi en una plaza». ¿Esa opción usa algo que vi o algo que inventé?", "algo que vi", "Dice que lo vio en una plaza."),
        ex("Una pregunta como «¿De qué pueblo eres?» a una compañera, ¿está bien hecha? Responde Sí o No.", "No", "Nadie debe demostrar su identidad para participar."),
    ],
    A=[
        ex("Elige la pregunta mejor hecha para el relato: A) «¿Qué te gustó del relato?» B) «Cuéntanos qué problemas tiene tu familia.»", "A", "A no obliga a contar nada privado."),
        arith("Tu curso tiene 24 niños. Si 9 prefirieron conectar con algo que vieron, ¿cuántos eligieron otra opción?", "24 - 9", "Resto los 9 del total."),
        ex("¿Cuál es una opción ficticia: A) una niña inventada llamada Rosa que riega su patio B) la compañera que se sienta a tu lado?", "A", "Una niña inventada es ficticia; la compañera es una persona real."),
    ],
    Z=[
        ex("Luis dice: «Si no cuento algo de mi familia, no puedo participar». ¿Tiene razón? Responde Sí o No.", "No", "Puede participar con otras opciones."),
        ex("Una niña no habla la lengua del relato. Un compañero dice: «Entonces no sabe nada». ¿Qué le respondes: «Cada persona puede escuchar y aprender» o «Tienes razón»?", "«Cada persona puede escuchar y aprender»", "Nadie se mide por hablar o no una lengua."),
    ],
    D=[
        ex("Ordena de lo más privado a lo menos privado: A) cuento un secreto de mi familia B) pienso en un personaje inventado C) cuento algo que vi en la plaza. Escribe las letras.", "A, C, B", "El secreto es lo más privado y el personaje inventado lo menos."),
        arith("Tienes 3 opciones de conexión para cada uno de 4 relatos. ¿Cuántas opciones hay en total?", "3 * 4", "Tres opciones por cuatro relatos."),
    ],
    context=[ex("Después de un relato, tu profesora pide: «Cuenten con qué lo relacionan, o inventen un personaje». ¿Qué haces: invento un niño llamado Pablo que pasa algo parecido o cuento algo muy privado?", "invento un niño llamado Pablo", "La opción ficticia me protege y me deja participar.")],
    selfcheck=[
        ex("¿Qué es una opción ficticia?", "algo inventado", "Ficticio quiere decir inventado."),
        ex("¿Estoy obligado a contar cosas privadas de mi familia?", "No", "Puedo elegir otra forma de conectar."),
        ex("¿Puedo preguntar a una compañera de qué pueblo es?", "No", "Nadie debe demostrar su identidad."),
    ],
    task=T(
        "Relato inventado: «Una niña llamada Rita riega un cerro seco hasta que crecen flores». Elige UNA forma de conectarlo y escribe dos frases: A) con algo que aprendí, B) con algo que vi en un parque o plaza, C) con un personaje inventado. No cuentes nada privado de tu familia. Después escribe una pregunta amable que no obligue a nadie a contar algo personal.",
        "Opción C: Pienso en un niño llamado Pablo que riega su patio. Se parece a Rita porque cuida un lugar seco. Pregunta: ¿qué parte del relato les gustó más?",
        ["elige una forma de conectar", "no cuenta nada privado", "escribe una pregunta que no obliga"],
        ["dos frases escritas", "pregunta escrita o dicha en voz alta"],
        ["contar cosas privadas de su familia", "preguntar la identidad de otra persona"],
        "Valora que conectó cuidando la privacidad; si contó algo privado, recuérdale que puede usar un personaje inventado.",
    ),
    reinforce="Escribe una frase con un personaje inventado que se parezca a Rita y di en qué se parecen.",
    extend="Inventa otra pregunta amable para hacer después de un relato, sin obligar a nadie a contar nada personal.",
)

L(
    LF1, 5,
    materials="Lápiz, hoja y colores. Las frases modelo están en este cuaderno. La devolución de práctica es para un educador inventado y también puede dirigirse al educador o educadora real de tu escuela.",
    use="Aprenderé a devolver lo que entendí a quien me contó un relato. Sirve para agradecer, comprobar si entendí bien y respetar a quien comparte su saber.",
    prior=["Sé situar voz, pueblo y contexto.", "Sé reconstruir la secuencia de un relato."],
    explain=[
        "Devolver es volver hacia quien me contó el relato y decirle lo que entendí. Lo hago con mis palabras, y no con las suyas. Así la persona puede decirme si entendí bien.",
        "Una devolución respetuosa tiene cuatro partes. Gracias: agradezco. Lo que entendí: cuento la secuencia con mis palabras. Mi duda: digo qué no entendí. Pregunta de cierre: pregunto si puedo compartirlo y con quién. Cada lengua indígena tiene su manera de agradecer; la enseña el educador o la educadora tradicional y la uso solo con su guía.",
        "Una devolución no cambia el relato ni agrega cosas que no estaban. Tampoco lo comparto fuera sin permiso. Si me dicen que algo no se puede contar, lo respeto sin discutir.",
    ],
    vocab=[("devolver", "volver a quien me contó y decirle lo que entendí"), ("agradecer", "decir gracias a quien me enseñó"), ("duda", "algo que no entendí del todo"), ("compartir", "contar a otros con permiso"), ("respetar", "cuidar lo que otra persona decidió")],
    worked=[
        W("Armar una devolución", "Relato de práctica: Rita encontró un cerro seco, llevó agua y al final hubo flores. Armo la devolución. ¿Qué frase es «lo que entendí»?", ["Gracias es la primera parte.", "Lo que entendí es contar la secuencia con mis palabras.", "Escribo: «Entendí que Rita llevó agua y al final hubo flores»."], "«Entendí que Rita llevó agua y al final hubo flores»"),
        W("Qué hago si me dicen que no", "Después de una devolución, la educadora dice: «Esta parte no se puede contar fuera de la sala». ¿Qué hago?", ["Escucho sin discutir.", "No cuento esa parte fuera de la sala.", "Le agradezco que me lo haya dicho."], "Lo respeto y no lo cuento fuera de la sala"),
    ],
    mistakes=[
        M("Agregar partes que yo inventé a lo que entendí.", "Cambia lo que la persona contó.", "Cuento solo lo que escuché, con mis palabras."),
        M("Contar el relato en otro lugar sin preguntar.", "La persona decide qué se comparte.", "Pregunto si puedo compartirlo y con quién."),
    ],
    R=[
        ex("Devolver es decirle a la persona que me contó: A) lo que entendí B) lo que inventé.", "A", "Devolver es decir lo que entendí."),
        ex("La primera parte de una devolución es: A) agradecer B) pedir que me cuenten otro relato.", "A", "La primera parte de la devolución agradece."),
        ex("Si me dicen que algo no se puede contar fuera, ¿lo cuento igual o lo respeto?", "lo respeto", "La persona decide qué se comparte."),
    ],
    C=[
        ex("Verdadero o falso: una devolución debe usar las mismas palabras exactas del relato.", "Falso", "Se hace con mis propias palabras."),
        ex("Frase: «Entendí que Rita llevó agua». ¿Es el agradecimiento, lo que entendí o una duda?", "lo que entendí", "Cuenta lo que comprendió del relato."),
        ex("Frase: «No entendí por qué Rita usó un balde». ¿Es una duda o una pregunta de cierre?", "una duda", "Dice qué no comprendió."),
    ],
    A=[
        arith("Una devolución tiene 4 partes. Ya escribiste 3. ¿Cuántas faltan?", "4 - 3", "Resto las partes escritas de las cuatro."),
        ex("Ordena las partes: C) mi duda A) gracias B) lo que entendí D) pregunta de cierre. Escribe las letras del orden de la clase.", "A, B, C, D", "El orden es gracias, lo que entendí, mi duda y pregunta de cierre."),
        ex("Elige la pregunta de cierre correcta: A) «¿Puedo compartirlo con mi familia?» B) «Voy a contarlo en internet.»", "A", "A pide permiso; B lo decide sin preguntar."),
    ],
    Z=[
        ex("Tomás dice: «Para devolver, mejor agrego un final más lindo». ¿Está bien? Responde Sí o No.", "No", "No se cambia lo que la persona contó."),
        ex("Una niña dice: «Entendí que Rita llevó flores». El relato dice que Rita llevó agua y hubo flores al final. ¿Qué debe corregir?", "que llevó agua", "Debe decir lo que realmente pasó."),
    ],
    D=[
        ex("¿Qué es mejor para cerrar una devolución: A) «¿Puedo compartirlo, y con quién?» B) «Ya está.»", "A", "Pido permiso y cuido lo compartido."),
        arith("Escribiste una devolución con 4 frases y cada frase tiene 5 palabras. ¿Cuántas palabras escribiste?", "4 * 5", "Cuatro frases por cinco palabras."),
    ],
    context=[ex("Una persona de tu comunidad contó un relato a tu curso. Al irse, ¿qué es mejor: decirle «gracias, esto fue lo que entendí» o irte sin decir nada?", "decirle «gracias, esto fue lo que entendí»", "Agradecer y devolver respeta a quien compartió.")],
    selfcheck=[
        ex("Para agradecer en una lengua indígena, ¿quién me enseña cómo hacerlo: el educador tradicional o lo adivino yo?", "el educador tradicional", "Cada lengua se aprende de quien la enseña, no se adivina."),
        ex("¿Cuántas partes tiene una devolución respetuosa?", "4", "Son cuatro partes."),
        ex("¿Puedo cambiar el relato al devolverlo?", "No", "Devuelvo lo que escuché, sin cambios."),
    ],
    task=T(
        "Usa este relato inventado: «Rita encontró un cerro seco. Llevó agua con un balde. Después crecieron flores». Escribe una devolución de cuatro partes para una persona de tu comunidad o para un educador inventado: 1) gracias, 2) lo que entendí, 3) mi duda, 4) mi pregunta de cierre sobre si puedes compartirlo y con quién. Si puedes, léela en voz alta.",
        "Gracias por contarnos el relato. Entendí que Rita llevó agua al cerro seco y después crecieron flores. No entendí por qué eligió un balde. ¿Puedo compartirlo con mi familia?",
        ["incluye las cuatro partes", "cuenta con sus palabras sin cambiar el relato", "pregunta si puede compartirlo"],
        ["devolución escrita", "lectura en voz alta"],
        ["agregar hechos inventados", "olvidar el permiso"],
        "Valora que devolvió con respeto; si agregó hechos, pídele que vuelva al relato y conserve solo lo escuchado.",
    ),
    reinforce="Dile a alguien «gracias» y una frase corta con lo que entendiste de un relato de práctica.",
    extend="Escribe una segunda devolución para otro relato corto que conozcas, siguiendo las cuatro partes.",
)

"""Student material for 1.º básico Música, OA 01 (cualidades y elementos) y OA 02 (sensaciones y emociones)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA1, OA2 = "MU01 OA 01", "MU01 OA 02"

TA, TT, SIL = "TA", "ti-ti", "SIL"
LEY = "TA = 1 sonido en 1 pulso; ti-ti = 2 sonidos rápidos en 1 pulso; SIL = 1 pulso de silencio"


def P(*tokens: str) -> str:
    """Rhythm written with symbols, e.g. TA – ti-ti – TA – SIL."""
    return " – ".join(tokens)


def sounds(*tokens: str) -> int:
    return sum({TA: 1, TT: 2, SIL: 0}[t] for t in tokens)


# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Lápiz, una olla o un tarro con una cuchara, dos objetos que suenen distinto (por ejemplo una cuchara de metal y una de madera) y tus palmas. Todos los sonidos que se usan en los ejercicios están descritos por escrito.",
    use="Aprenderé a escuchar cuatro cualidades del sonido: altura, timbre, intensidad y duración. Sirve para describir lo que oigo con palabras exactas y para elegir sonidos cuando hago música.",
    prior=["Sé escuchar en silencio unos segundos.", "Sé golpear un objeto con suavidad y con fuerza."],
    explain=[
        "Todo sonido tiene cuatro cualidades. La altura dice si el sonido es agudo (fino, como un pajarito) o grave (hondo, como un trueno lejano). La intensidad dice si es fuerte o suave. La duración dice si es largo o corto. El timbre dice quién suena: una cuchara, una voz o una campana.",
        "Las cualidades son independientes. Un sonido puede ser agudo y suave a la vez, como un silbido bajito. También puede ser grave y fuerte, como un tambor grande golpeado con ganas. Por eso agudo no significa fuerte, ni grave significa suave. Cada cualidad se pregunta por separado.",
        "Para describir un sonido, hazte cuatro preguntas: ¿es agudo o grave?, ¿es fuerte o suave?, ¿es largo o corto?, ¿qué objeto o voz lo produce? Escucha dos veces. La primera para sentirlo y la segunda para responder con una pista que realmente oíste.",
    ],
    vocab=[("agudo", "sonido fino, de tono alto"), ("grave", "sonido hondo, de tono bajo"), ("intensidad", "qué tan fuerte o suave suena"), ("duración", "cuánto tiempo suena: largo o corto"), ("timbre", "el color del sonido; lo que dice quién suena")],
    worked=[
        {"title": "Describir un cascabel", "problem": "Un cascabel pequeño suena fino, flojito y se apaga rápido. Descríbelo con las cuatro cualidades.", "steps": ["Altura: suena fino, así que es agudo.", "Intensidad: suena flojito, así que es suave.", "Duración: se apaga rápido, así que es corto.", "Timbre: lo produce un cascabel de metal."], "answer": "Agudo, suave, corto; timbre de cascabel"},
        {"title": "Separar agudo de fuerte", "problem": "Una niña dice: «el silbido de mi papá es agudo, entonces es fuerte». ¿Tiene razón?", "steps": ["Agudo habla de la altura; fuerte habla de la intensidad.", "Un silbido puede ser agudo y a la vez muy suave, si se silba bajito.", "Son dos preguntas distintas."], "answer": "No necesariamente: agudo y fuerte son cualidades distintas"},
    ],
    mistakes=[
        {"wrong": "Decir que todo sonido agudo es fuerte.", "why": "Se mezclan la altura y la intensidad, que son dos cualidades distintas.", "fix": "Pregunta primero «¿fino u hondo?» y después «¿fuerte o suave?»."},
        {"wrong": "Decir «el sonido es largo» cuando el golpe es fuerte pero se apaga enseguida.", "why": "Se confunde la duración con la intensidad.", "fix": "Cuenta cuánto tiempo se oye el sonido, no qué tan fuerte parte."},
    ],
    tiers={
        "recovery": [
            ex("Un silbato suena muy fino, como un pajarito. ¿Es agudo o grave?", "Agudo", "Un sonido fino y alto de tono es agudo."),
            ex("Un tambor grande suena hondo, como un trueno lejano. ¿Es agudo o grave?", "Grave", "Un sonido hondo y bajo de tono es grave."),
            ex("Dices «hola» casi sin voz, como un secreto. ¿La intensidad es fuerte o suave?", "Suave", "Un secreto se dice con poca fuerza, es decir, suave."),
        ],
        "understand": [
            ex("Golpeas una olla despacito y luego con mucha fuerza. ¿Qué cualidad cambió?", "La intensidad", "Cambió qué tan fuerte suena, y eso es la intensidad."),
            ex("Una guitarra y un piano tocan la misma nota. ¿Qué cualidad te ayuda a saber cuál es cuál?", "El timbre", "El timbre es el color del sonido y dice quién suena."),
            ex("¿Qué cualidad dice si un sonido dura poco o dura mucho?", "La duración", "Largo y corto hablan de cuánto tiempo suena."),
        ],
        "apply": [
            ex("Ordena de más grave a más agudo: chillido de un pajarito, trueno lejano, voz de un niño.", "Trueno lejano, voz de un niño, chillido de un pajarito", "El trueno es muy hondo, la voz es media y el pajarito es muy fino."),
            ex("Clasifica en largo o corto: (a) un aplauso que dura un instante; (b) una campana que se va apagando muy despacio.", "(a) corto; (b) largo", "El aplauso se acaba enseguida y la campana sigue sonando."),
            ex("Describe con las cuatro cualidades este sonido: un pajarito canta muy suavemente por mucho rato.", "Agudo, suave, largo; timbre de pajarito", "Canta fino, con poca fuerza y por mucho tiempo."),
        ],
        "reason": [
            ex("Beto dice: «el silbato es agudo, por eso es fuerte». ¿Por qué se equivoca?", "Porque agudo es la altura y fuerte es la intensidad; un silbato agudo puede sonar suave", "Son dos cualidades distintas que no dependen una de otra."),
            ex("¿Puede un sonido ser grave y suave a la vez? Da un ejemplo.", "Sí, por ejemplo un tambor grande golpeado muy despacito", "Un tambor grande es grave y un golpe despacito es suave."),
        ],
        "challenge": [
            ex("Tienes un cascabel y un tambor. Quieres un sonido agudo, corto y fuerte. ¿Qué objeto eliges y cómo lo tocas?", "El cascabel, sacudido con fuerza y parado enseguida con la mano", "El cascabel es agudo; fuerte se logra sacudiéndolo con fuerza y corto, deteniéndolo."),
            ex("Con una sola olla y una cuchara, ¿qué dos cualidades puedes cambiar sin cambiar de objeto?", "La intensidad y la duración", "Puedes golpear fuerte o suave, y dejar sonar o apagar con la mano."),
        ],
    },
    context=[ex("En la cocina suenan dos cosas. Sonido A: una tetera pita fino durante mucho rato. Sonido B: se cierra la puerta del refrigerador con un golpe hondo y breve. Describe la altura y la duración de A y de B.", "A: agudo y largo; B: grave y corto", "El pito fino es agudo y dura; el golpe hondo es grave y se acaba rápido.")],
    selfcheck=[ex("¿Qué cualidad cambia cuando pasas de un susurro a un grito?", "La intensidad", "Pasas de suave a fuerte."), ex("Un trueno lejano, ¿es agudo o grave?", "Grave", "El trueno suena hondo."), ex("Nombra las cuatro cualidades del sonido.", "Altura, timbre, intensidad y duración", "Son las cuatro preguntas para describir cualquier sonido.")],
    open_task=task(
        f"Con tus palmas toca cuatro veces seguidas este patrón: {P(TA, TT, TA, SIL)} ({LEY}). Primero tócalo fuerte y después suave, manteniendo el mismo pulso. Escribe o dibuja qué cualidad cambió y qué se mantuvo igual.",
        "Toqué el patrón dos veces fuerte y dos veces suave. Cambió la intensidad: fuerte y suave. Se mantuvo el pulso y el orden de los sonidos.",
        ["toca el patrón completo con el silencio en su lugar", "cambia solo la intensidad", "nombra la cualidad que cambió y la que se mantuvo"],
        ["interpretación con palmas", "dibujo o frase escrita", "explicación oral"],
        ["acelerar cuando toca fuerte", "decir que cambió el ritmo en vez de la intensidad"],
        "Reconoce el pulso estable y pregunta qué pista audible le mostró el cambio; si dice «me gustó», pídele que diga si sonó fuerte o suave.",
    ),
    reinforce="Elige tres objetos de tu casa. Golpéalos suavemente y di de cada uno si suena agudo o grave.",
    extend="Busca un sonido que sea agudo y largo, y otro que sea grave y corto. Explica por qué cada uno cumple.",
)

register(
    OA1, 2,
    materials=f"Lápiz, tus palmas y los pasos de tus pies. Leyenda de símbolos: {LEY}. Los patrones están escritos en cada ejercicio.",
    use="Aprenderé a distinguir pulso, acento y patrón. Sirve para marchar, bailar o tocar junto a otras personas sin perderme.",
    prior=["Sé qué es un latido.", "Sé caminar al mismo paso varias veces seguidas."],
    explain=[
        "El pulso es el latido de la música. Es parejo, como los pasos al caminar o los latidos del corazón. Suena siempre igual: 1, 2, 3, 4. No cambia aunque la melodía cambie.",
        f"El acento es un pulso que se marca más fuerte. Si cuentas 1, 2, 3, 4 y el 1 va más fuerte, ese es el acento. El patrón es una secuencia de sonidos que se repite sobre el pulso. Por ejemplo: {P(TA, TA, TT, SIL)}. TA dura un pulso; ti-ti son dos sonidos rápidos en un solo pulso; SIL es un pulso en silencio.",
        "Ojo: pulso y ritmo no son lo mismo. El pulso se mantiene parejo. El ritmo es lo que suena encima del pulso y puede tener sonidos rápidos, lentos y silencios. Camina el pulso con los pies y toca el patrón con las palmas para sentir la diferencia.",
    ],
    vocab=[("pulso", "latido parejo de la música"), ("acento", "pulso que se marca más fuerte"), ("patrón", "secuencia de sonidos que se repite"), ("ritmo", "lo que suena sobre el pulso"), ("silencio", "pulso en que no suena nada")],
    worked=[
        {"title": "Contar los pulsos de un patrón", "problem": f"¿Cuántos pulsos tiene {P(TA, TT, TA, SIL)}?", "steps": ["Cada símbolo ocupa un pulso: TA, ti-ti, TA y SIL.", "Cuento: uno, dos, tres, cuatro.", "El silencio también cuenta como pulso."], "answer": "4 pulsos"},
        {"title": "Encontrar el acento", "problem": "Cuento 1, 2, 3, 4, 1, 2, 3, 4 y marco más fuerte el primero de cada grupo. ¿En qué números va el acento?", "steps": ["Miro dónde se repite el golpe más fuerte.", "Cada grupo parte en 1.", "El acento cae en cada 1."], "answer": "En el número 1 de cada grupo"},
    ],
    mistakes=[
        {"wrong": "Decir que ti-ti son dos pulsos.", "why": "Se cuentan los sonidos y no los latidos.", "fix": "ti-ti son dos sonidos rápidos dentro de un solo pulso."},
        {"wrong": "Saltarse el silencio al contar los pulsos.", "why": "Se piensa que si no suena nada no cuenta.", "fix": "El silencio ocupa un pulso; cuéntalo en voz baja."},
    ],
    tiers={
        "recovery": [
            ex("Caminas al mismo paso: paso, paso, paso, paso. ¿Eso es el pulso o el acento?", "El pulso", "Los pasos parejos son el latido de la música."),
            ex(f"En el patrón {P(TA, TA, SIL, TA)}, ¿cuántos pulsos hay?", "4", "Cada símbolo ocupa un pulso: TA, TA, SIL y TA."),
            ex("Cuentas 1, 2, 3, 4 y el 1 lo dices más fuerte. ¿Cómo se llama ese pulso fuerte?", "Acento", "El pulso que se marca más fuerte es el acento."),
        ],
        "understand": [
            ex("¿Cuántos sonidos tiene un ti-ti?", "2", "Son dos sonidos rápidos."),
            ex("¿Cuántos pulsos ocupa un ti-ti?", "1", "Los dos sonidos caben en un solo pulso."),
            ex("Cambia la melodía, pero los pasos siguen parejos. ¿Cambió el pulso?", "No", "El pulso es el latido parejo y se mantiene."),
        ],
        "apply": [
            ex(f"Cuenta los sonidos del patrón {P(TA, TT, TT, SIL)}. ¿Cuántos sonidos se oyen?", str(sounds(TA, TT, TT, SIL)), "TA suena 1 vez, cada ti-ti suena 2 veces y SIL no suena: 1 + 2 + 2 = 5."),
            ex(f"Escribe el patrón en que suena TA, silencio, ti-ti y TA, en ese orden.", P(TA, SIL, TT, TA), "Se escribe cada símbolo en orden, uno por pulso."),
            ex("Pon un acento en el 1 y cuenta dos grupos de cuatro pulsos. Escribe los números y marca el acento con mayúscula.", "UNO 2 3 4 UNO 2 3 4", "El acento cae al inicio de cada grupo de cuatro."),
        ],
        "reason": [
            ex(f"Un niño dice que {P(TA, TT, TA, SIL)} tiene 5 pulsos porque ve 5 sonidos. ¿Qué confundió?", "Confundió sonidos con pulsos; tiene 4 pulsos", "ti-ti son dos sonidos pero solo un pulso, y el silencio también cuenta."),
            ex("Dos amigos tocan patrones distintos con el mismo paso parejo de sus pies. ¿Qué es igual en los dos: el pulso o el ritmo?", "El pulso", "Los pasos parejos son el pulso; los patrones son distintos."),
        ],
        "challenge": [
            ex(f"Toca con las palmas {P(TA, TA, TT, SIL)} y compara con {P(TA, TT, TT, SIL)}. ¿En qué pulso cambia el patrón?", "En el segundo pulso: TA pasa a ti-ti", "Los dos son iguales salvo el segundo símbolo."),
            ex(f"Quieres un patrón de 4 pulsos con exactamente 3 sonidos. Escribe uno usando TA, ti-ti y SIL.", "TA – ti-ti – SIL – SIL (u otro con 3 sonidos y 4 pulsos)", "TA da 1 y ti-ti da 2: 1 + 2 = 3 sonidos, con dos silencios que completan cuatro pulsos."),
        ],
    },
    context=[ex("En la marcha de un desfile escolar, el tambor toca golpes parejos y la gente camina al mismo ritmo de esos golpes. ¿Qué elemento de la música siguen los pasos?", "El pulso", "Los pasos parejos siguen el latido parejo del tambor.")],
    selfcheck=[ex("¿Cuántos pulsos tiene SIL?", "1", "El silencio ocupa un pulso."), ex(f"¿Cuántos sonidos tiene {P(TA, TA, SIL, SIL)}?", "2", "Solo suenan los dos TA."), ex("¿Qué se repite en un patrón?", "Una secuencia de sonidos", "Un patrón es una secuencia que vuelve a sonar.")],
    open_task=task(
        f"Camina en tu lugar con pulso parejo y toca con las palmas el patrón {P(TA, TA, TT, SIL)} cuatro veces. Luego marca el acento diciendo el primer pulso más fuerte. Cuenta en voz alta y escribe cuántos pulsos y cuántos sonidos tiene el patrón.",
        "Caminé al mismo paso y toqué cuatro veces el patrón. Tiene 4 pulsos y 4 sonidos: TA, TA y dos del ti-ti. El acento fue el primer TA.",
        ["mantiene el pulso parejo con los pies", "toca el patrón con el silencio al final", "escribe 4 pulsos y 4 sonidos"],
        ["interpretación", "conteo escrito", "explicación oral del acento"],
        ["no contar el silencio como pulso", "acelerar en el ti-ti"],
        "Reconoce el pulso estable y pide que muestre con el dedo dónde está el silencio; si cuenta 5 pulsos, repite despacio con una palabra por pulso.",
    ),
    reinforce="Camina 16 pasos parejos y aplaude solo en cada cuarto paso.",
    extend="Prueba un acento cada 3 pasos en lugar de cada 4 y cuenta cómo se siente distinto.",
)

register(
    OA1, 3,
    materials="Lápiz, colores y tarjetas de papel con las letras A y B. La audición está descrita por escrito; un adulto la puede leer y mostrar con objetos de la casa.",
    use="Aprenderé a reconocer secciones que regresan en una música: lo que se repite y lo que contrasta. Sirve para entender cómo está armada una pieza.",
    prior=["Sé distinguir fuerte de suave.", "Sé nombrar sonidos rápidos y lentos."],
    explain=[
        "Una música se arma por partes llamadas secciones. Si una sección vuelve a sonar igual, hay repetición. Si llega una sección distinta, hay contraste. Les ponemos letras para anotarlas: A es la primera sección y B es una sección diferente.",
        "Un orden muy común es A – B – A. Suena la sección A, luego aparece B con otro carácter y al final regresa A. Al volver A sentimos que la música cierra el camino. Si hay dos secciones distintas y no vuelve ninguna, podría ser A – B.",
        "Para encontrar las secciones, escucha un cambio claro: más rápido o más lento, más fuerte o más suave, otro instrumento, otra altura. Cuando oigas el cambio, pon una letra nueva. Cuando oigas que algo ya conocido regresa, repite la letra.",
    ],
    vocab=[("sección", "parte de una música"), ("repetición", "cuando una parte vuelve a sonar igual"), ("contraste", "cuando una parte es distinta de la anterior"), ("A y B", "letras para anotar secciones distintas"), ("regresar", "volver a sonar")],
    worked=[
        {"title": "Una pieza con regreso", "problem": "Un adulto toca así: un tambor grave y lento (4 golpes); luego sonajas agudas y rápidas (8 sacudidas); luego otra vez el tambor grave y lento (4 golpes). ¿Cómo se anotan las secciones?", "steps": ["La primera sección es tambor grave y lento: A.", "Las sonajas agudas y rápidas son distintas: B.", "El tambor grave y lento regresa: A."], "answer": "A – B – A"},
        {"title": "Contar repeticiones", "problem": "Una pieza tiene el orden A – A – B – A. ¿Cuántas veces suena A?", "steps": ["Miro cada letra del orden.", "Hay una A al inicio, otra A en segundo lugar y otra al final.", "Cuento: 3."], "answer": "3 veces"},
    ],
    mistakes=[
        {"wrong": "Poner una letra nueva cada vez que algo suena, aunque sea igual.", "why": "No se compara con lo que ya sonó antes.", "fix": "Si lo que regresa es igual, repite la misma letra."},
        {"wrong": "Decir que hay contraste cuando solo se repite el mismo patrón.", "why": "Se confunde repetir con cambiar.", "fix": "Contraste significa que hay algo distinto; repetición, que vuelve igual."},
    ],
    tiers={
        "recovery": [
            ex("Una parte vuelve a sonar exactamente igual. ¿Es repetición o contraste?", "Repetición", "Repetir es volver a sonar igual."),
            ex("Llega una parte lenta y suave después de una parte rápida y fuerte. ¿Es repetición o contraste?", "Contraste", "La parte nueva es distinta de la anterior."),
            ex("En A – B – A, ¿cuál sección regresa?", "A", "La A suena al inicio y al final."),
        ],
        "understand": [
            ex("¿Para qué sirven las letras A y B al escuchar música?", "Para anotar las secciones", "Cada letra marca una parte distinta de la pieza."),
            ex("Si dos secciones suenan casi igual, ¿llevan la misma letra o distinta?", "La misma letra", "Lo que suena igual se anota igual."),
            ex("¿Qué puedes notar para encontrar un cambio de sección?", "Un cambio en rapidez, fuerza, altura o instrumento", "Esas pistas se oyen cuando empieza una parte distinta."),
        ],
        "apply": [
            ex("Un adulto toca: palmadas fuertes (A), luego golpecitos suaves en la mesa (B), luego otra vez palmadas fuertes. Escribe el orden de secciones.", "A – B – A", "Las palmadas regresan, así que se repite la A."),
            ex("Una pieza tiene el orden A – B – A – B. ¿Cuántas secciones distintas hay y cuántas veces suena B?", "2 secciones distintas; B suena 2 veces", "Solo se usan A y B, y B aparece dos veces."),
            ex("Pinta con dos colores la forma A – A – B: un color para A y otro para B. ¿Cuántos cuadros llevan el color de A?", "2", "La A aparece dos veces antes de la B."),
        ],
        "reason": [
            ex("Pía dice que en A – B – A la tercera parte debe ser una sección nueva. ¿Por qué no?", "Porque la tercera parte es A, que regresa", "Se usa la misma letra cuando la música vuelve."),
            ex("En la pieza A – B – C, ¿hay alguna sección que regrese?", "No", "Las tres letras son distintas y ninguna se repite."),
        ],
        "challenge": [
            ex("Inventa una forma de 4 secciones con solo dos letras en que A regrese al final. Escríbela.", "A – B – B – A (u otra que parta y termine en A)", "Debe usar A y B y terminar con la A que regresa."),
            ex("Escucha esto: tambor fuerte, tambor fuerte, sonajas suaves, tambor fuerte. Escribe las secciones y di cuántos contrastes hay.", "A – A – B – A; hay 2 cambios de A a B o de B a A", "Cambia de tambor a sonajas y luego vuelve al tambor."),
        ],
    },
    context=[ex("En una fiesta de curso suena una música con tres partes: primero un coro de niños cantando (A), luego solo palmas (B) y por último otra vez el coro (A). ¿Cómo describirías la forma?", "A – B – A", "El coro vuelve al final, así que la forma regresa a A.")],
    selfcheck=[ex("¿Cómo se llama cuando una parte vuelve a sonar igual?", "Repetición", "Volver igual es repetir."), ex("En A – B – A, ¿cuántas veces suena A?", "2", "Suena al inicio y al final."), ex("¿Qué es el contraste?", "Una parte distinta de la anterior", "Contrastar es cambiar.")],
    open_task=task(
        "Usa un objeto que suene (una cuchara y un tarro) y tus palmas. Toca esta forma: A = cuatro golpes fuertes en el tarro; B = cuatro palmadas suaves. Hazlo en el orden A – B – A. Escribe qué cambió entre A y B y qué regresó.",
        "Toqué 4 golpes fuertes en el tarro, 4 palmadas suaves y de nuevo 4 golpes fuertes en el tarro. Cambió el instrumento y la fuerza. Regresó A.",
        ["toca las tres secciones en orden", "marca claramente la diferencia entre A y B", "explica qué regresó"],
        ["interpretación", "forma escrita A – B – A", "explicación breve"],
        ["tocar la B igual que la A", "olvidar que A debe regresar"],
        "Reconoce que A regresa y pide una pista audible del cambio; si no hay contraste, que cambie fuerza o instrumento en B.",
    ),
    reinforce="Haz una forma A – B con una parte de aplausos y otra de golpes en la mesa. Díselo a alguien y pídele que adivine el orden.",
    extend="Agrega una C distinta y prueba el orden A – B – A – C. Explica qué regresó y qué fue nuevo.",
)

register(
    OA1, 4,
    materials=f"Papel, lápiz y colores. Leyenda para esta clase: {LEY}. Dibujos: ● = TA (un sonido); ○○ = ti-ti (dos sonidos pequeños); □ = SIL (silencio).",
    use="Aprenderé a escribir lo que escucho con símbolos que yo pueda explicar. Sirve para recordar un ritmo y para que otra persona lo toque.",
    prior=["Sé tocar un patrón corto con las palmas.", "Sé diferenciar sonido de silencio."],
    explain=[
        "Una partitura es un dibujo que guarda una música. La partitura tradicional usa notas en un pentagrama, pero también podemos inventar símbolos propios. Esa es una partitura no convencional y sirve si explicas qué significa cada símbolo.",
        f"En este cuaderno usaremos tres símbolos. El círculo lleno ● es un TA: un sonido en un pulso. Los dos círculos vacíos ○○ son un ti-ti: dos sonidos rápidos en un pulso. El cuadrado vacío □ es un silencio. Así {P(TA, TT, TA, SIL)} se dibuja ● ○○ ● □.",
        "También podemos dibujar fuerza y duración. Un círculo grande puede significar fuerte y uno pequeño, suave. Una línea larga puede mostrar un sonido largo. Lo importante es escribir una llave: la lista que dice qué significa cada símbolo, para que cualquiera pueda leerla.",
    ],
    vocab=[("partitura", "dibujo que guarda una música"), ("símbolo", "dibujo que representa un sonido"), ("llave", "lista que explica qué significa cada símbolo"), ("no convencional", "inventada y explicada por uno mismo"), ("leer", "tocar lo que dice el dibujo")],
    worked=[
        {"title": "De palabras a dibujo", "problem": f"Dibuja el patrón {P(TA, TT, TA, SIL)} con los símbolos de la clase.", "steps": ["TA es ●.", "ti-ti es ○○.", "SIL es □.", "Pongo uno por pulso, de izquierda a derecha."], "answer": "● ○○ ● □"},
        {"title": "De dibujo a sonido", "problem": "Lee este dibujo: ○○ ● □ ●", "steps": ["○○ es ti-ti: dos sonidos rápidos.", "● es TA.", "□ es silencio.", "● es TA otra vez."], "answer": f"{P(TT, TA, SIL, TA)}"},
    ],
    mistakes=[
        {"wrong": "Dibujar un símbolo para el silencio, pero ponerlo en el lugar equivocado.", "why": "No se sigue el orden de izquierda a derecha.", "fix": "Lee con el dedo, un símbolo por pulso, y comprueba tocando."},
        {"wrong": "Usar símbolos sin llave.", "why": "Se piensa que todos entienden el dibujo.", "fix": "Escribe al lado qué significa cada símbolo antes de compartir."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué sonido representa el símbolo ●?", "TA, un sonido en un pulso", "Es el círculo lleno de la llave de esta clase."),
            ex("¿Qué representa el símbolo □?", "Un silencio", "El cuadrado vacío significa que no suena nada."),
            ex("¿Qué representa ○○?", "ti-ti, dos sonidos rápidos en un pulso", "Dos círculos pequeños son dos sonidos en un solo pulso."),
        ],
        "understand": [
            ex("¿Para qué sirve la llave de una partitura?", "Para explicar qué significa cada símbolo", "Sin llave otra persona no puede leer el dibujo."),
            ex("¿En qué dirección se lee una partitura de ritmo?", "De izquierda a derecha", "Es el orden en que suenan los pulsos."),
            ex("Una partitura no convencional, ¿necesita notas de pentagrama?", "No", "Se puede usar cualquier símbolo si se explica."),
        ],
        "apply": [
            ex(f"Dibuja con los símbolos el patrón {P(TA, TA, TT, SIL)}.", "● ● ○○ □", "TA es ●, ti-ti es ○○ y SIL es □, uno por pulso."),
            ex("Lee y escribe con palabras este dibujo: □ ○○ ● ●", P(SIL, TT, TA, TA), "Se traduce cada símbolo en orden."),
            ex("Cuenta los sonidos que se oyen en este dibujo: ● ○○ □ ○○", "5", "● suena 1, cada ○○ suena 2 y □ no suena: 1 + 2 + 2 = 5."),
        ],
        "reason": [
            ex("Mateo dibujó ● ● ● y dice que es TA – ti-ti – TA. ¿Qué le falta?", "Dibujar ○○ en el segundo pulso", "El ti-ti son dos sonidos, y su dibujo muestra tres TA."),
            ex("Dos niños dibujan el mismo patrón con símbolos distintos y ambos escriben su llave. ¿Pueden estar bien los dos?", "Sí", "Una partitura no convencional vale si se explica con una llave."),
        ],
        "challenge": [
            ex("Quieres mostrar fuerte con un círculo grande y suave con uno pequeño. Escribe una llave de tres símbolos: fuerte, suave y silencio.", "Círculo grande = fuerte; círculo pequeño = suave; cuadrado = silencio (u otra llave clara)", "Una llave clara asigna un significado distinto a cada símbolo."),
            ex(f"Escribe un patrón de 4 pulsos con símbolos, que tenga exactamente 4 sonidos y un silencio.", "● ○○ □ ● es un ejemplo: 1 + 2 + 0 + 1 = 4 sonidos y un silencio", "Debe sumar 4 sonidos y tener un □."),
        ],
    },
    context=[ex("Tu hermana quiere tocar el patrón que tú inventaste, pero no estás en casa. Le dejas esta nota: ● ○○ ● □. ¿Qué más debes escribir para que pueda tocarlo bien?", "La llave que explica los símbolos y el orden en que se leen", "Sin llave ella no sabría qué sonido es cada dibujo.")],
    selfcheck=[ex("¿Qué símbolo de la clase se usa para el silencio?", "El cuadrado □", "Fue la regla de la llave."), ex(f"Dibuja {P(TA, SIL)}.", "● □", "TA es ● y SIL es □."), ex("¿Qué es una llave?", "Una lista que explica los símbolos", "Dice qué significa cada dibujo.")],
    open_task=task(
        f"Crea tu propia partitura de 4 pulsos con ●, ○○ y □. Puedes copiar este ejemplo y cambiarle un símbolo: ● ○○ ● □. Escribe tu llave, toca el patrón con las palmas y pídele a alguien que lo lea y lo toque.",
        "Mi partitura fue ● ● ○○ □. Mi llave: ● = un sonido, ○○ = dos sonidos rápidos, □ = silencio. Mi mamá la leyó y tocó igual que yo.",
        ["dibuja 4 pulsos con al menos dos símbolos distintos", "escribe una llave", "otra persona puede tocarlo con ayuda de la llave"],
        ["partitura dibujada", "llave escrita", "interpretación"],
        ["no incluir el silencio en la llave", "mezclar el orden al tocar"],
        "Reconoce la claridad de la llave y pide que toque mientras señala cada símbolo; si el lector se equivoca, mejoren juntos la llave.",
    ),
    reinforce="Dibuja con ● el pulso de 8 pasos y marca con un círculo más grande el acento de cada grupo de 4.",
    extend="Inventa un símbolo para un sonido largo y úsalo en una partitura de 4 pulsos con su llave.",
)

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Un espacio libre para moverte con seguridad, un pañuelo o una hoja de papel y música descrita aquí por escrito. Un adulto puede leer las descripciones en voz alta y mostrar sonidos con objetos de la casa.",
    use="Aprenderé a mostrar con movimiento un cambio que oigo en la música. Sirve para sentir la música con el cuerpo y para contar qué escuché.",
    prior=["Sé moverme en un espacio sin chocar con nada.", "Sé distinguir sonidos fuertes y suaves."],
    explain=[
        "Escuchar con el cuerpo es mover las manos, los brazos o los pies según lo que oyes. Si la música es lenta, tus movimientos pueden ser lentos y largos. Si la música es rápida, pueden ser pequeños y veloces. Si es fuerte, usas más espacio. Si es suave, te mueves con cuidado.",
        "Nadie tiene que moverse igual que otra persona. Lo importante es que tu movimiento cambie cuando cambia el sonido. Esa es tu pista: oí que algo cambió y mi cuerpo lo mostró. Puedes usar un pañuelo, una hoja o solo tus manos.",
        "Antes de moverte, mira tu espacio. Quédate en tu lugar si hay cosas cerca. Mueve los brazos suave para no golpearte. Cuando termine la música, quédate quieto como una estatua. El silencio también se puede mostrar con el cuerpo.",
    ],
    vocab=[("movimiento", "forma de mover el cuerpo"), ("lento", "que va despacio"), ("rápido", "que va veloz"), ("espacio", "lugar libre para moverme"), ("cambio", "cuando algo pasa a ser distinto")],
    worked=[
        {"title": "Mostrar lento y rápido", "problem": "La música suena lenta y grave por un rato y luego rápida y aguda. ¿Cómo muestras el cambio con tus brazos?", "steps": ["En la parte lenta y grave hago movimientos largos y despacio, como un elefante.", "Cuando cambia a rápida y aguda hago movimientos pequeños y veloces, como un ratón.", "El cambio de mi cuerpo muestra el cambio del sonido."], "answer": "Brazos largos y lentos, luego pequeños y veloces"},
        {"title": "Mostrar fuerte y suave", "problem": "Un tambor suena suave y luego muy fuerte. ¿Cómo muestras la diferencia sin hacer ruido?", "steps": ["En lo suave me muevo chiquito, con las manos cerca del cuerpo.", "Cuando suena fuerte abro los brazos grandes pero sin golpear nada.", "Mi cuerpo se agranda cuando el sonido crece."], "answer": "Movimiento chico y luego grande"},
    ],
    mistakes=[
        {"wrong": "Moverme igual todo el tiempo aunque la música cambie.", "why": "No estoy escuchando el cambio.", "fix": "Elige un momento exacto en que la música cambia y cambia tu movimiento allí."},
        {"wrong": "Moverme tan fuerte que choco con cosas.", "why": "Confundo música fuerte con movimientos bruscos.", "fix": "Usa más espacio con los brazos, pero con control y cuidado."},
    ],
    tiers={
        "recovery": [
            ex("La música suena muy despacio. ¿Tu movimiento será lento o veloz?", "Lento", "El movimiento sigue a la música: despacio con música lenta."),
            ex("La música suena rápida. ¿Cómo son tus pasos pequeños?", "Rápidos", "Música rápida se muestra con movimientos veloces."),
            ex("La música termina en silencio. ¿Qué haces con tu cuerpo?", "Quedarme quieto", "El silencio se muestra sin moverse."),
        ],
        "understand": [
            ex("¿Qué debe cambiar en tu cuerpo cuando cambia la música?", "Mi movimiento", "El movimiento muestra que oí el cambio."),
            ex("¿Por qué miras tu espacio antes de moverte?", "Para no chocar con nada", "Moverse seguro es parte de la actividad."),
            ex("¿Todos deben moverse exactamente igual?", "No", "Cada cuerpo puede mostrar el cambio a su manera."),
        ],
        "apply": [
            ex("Un adulto toca golpes suaves en la mesa y luego golpes fuertes. Elige un movimiento para cada parte y escríbelos.", "Suave: movimiento chico; fuerte: movimiento grande", "El tamaño del movimiento sigue la fuerza del sonido."),
            ex("Suena una melodía que sube de grave a agudo. ¿Hacia dónde mueves tus manos para mostrarlo?", "De abajo hacia arriba", "Lo agudo se muestra arriba y lo grave abajo."),
            ex("Suena una nota larga, larga, larga. ¿Cómo mueves un pañuelo?", "Despacio, haciendo una línea larga en el aire", "Una nota larga se muestra con un movimiento continuo."),
        ],
        "reason": [
            ex("Sofía se movió igual en la parte lenta y en la parte rápida. ¿Cómo sabemos que no mostró el cambio?", "Porque su movimiento no cambió cuando cambió la música", "El movimiento debe cambiar junto con el sonido."),
            ex("Dos niños muestran la misma música moviéndose distinto, pero ambos cambian cuando cambia el sonido. ¿Están bien?", "Sí", "Lo importante es mostrar el cambio, no copiar al otro."),
        ],
        "challenge": [
            ex("Una música tiene tres partes: lenta y suave, rápida y fuerte, y otra vez lenta y suave. Describe un movimiento para cada parte.", "Parte 1: movimiento largo y chico; parte 2: movimiento veloz y grande; parte 3: como la 1", "La tercera parte regresa, así que el cuerpo también regresa."),
            ex("Cuando la música se detiene de pronto, ¿qué señal oyes y qué haces?", "Oigo silencio y me quedo quieto", "El silencio es el cambio que se muestra deteniéndose."),
        ],
    },
    context=[ex("En la clase de música la profesora hace sonar un cascabel suave y luego un tambor fuerte. Tú tienes poco espacio entre tu silla y la mesa. ¿Cómo muestras el cambio con seguridad?", "Con movimientos de brazos chicos y luego más grandes, sin salir de mi lugar", "Se puede mostrar el cambio usando el tamaño del movimiento sin chocar.")],
    selfcheck=[ex("Si la música es rápida, ¿cómo te mueves?", "Rápido y con movimientos pequeños", "El cuerpo sigue la velocidad que oye."), ex("¿Cuándo cambias tu movimiento?", "Cuando cambia la música", "El cambio del sonido es la pista."), ex("¿Qué haces cuando termina la música?", "Quedarme quieto", "El silencio se muestra sin moverse.")],
    open_task=task(
        "Un adulto toca con una cuchara y un tarro esta música: 4 golpes suaves y lentos, luego 8 golpes rápidos y fuertes, luego 4 golpes suaves y lentos. Muévete con un pañuelo o con tus manos mostrando cada parte. Cuenta en qué momento cambiaste y qué pista oíste.",
        "Cuando los golpes eran suaves y lentos moví el pañuelo despacio. Cuando se hicieron rápidos y fuertes lo moví grande y veloz. Cambié al golpe número cinco porque oí que sonaba más fuerte.",
        ["cambia el movimiento cuando cambia el sonido", "usa un espacio seguro", "nombra la pista que oyó"],
        ["movimiento observado", "frase oral o escrita", "dibujo del recorrido"],
        ["moverse igual todo el tiempo", "moverse brusco y chocar"],
        "Reconoce el momento exacto del cambio y pregunta qué oyó; si no hay cambio de movimiento, repite la música más despacio.",
    ),
    reinforce="Mueve solo las manos para mostrar un sonido suave y uno fuerte, sentado en una silla.",
    extend="Cuenta cómo cambiaría tu movimiento si el tambor sonara grave en vez de agudo.",
)

register(
    OA2, 2,
    materials="Lápiz y una hoja. Las palabras para describir están escritas en esta clase. Un adulto lee las descripciones de audición en voz alta.",
    use="Aprenderé a decir qué sensación me deja un sonido y qué pista sonora la causa. Sirve para hablar de la música con palabras más exactas que «me gusta».",
    prior=["Sé decir si algo me gusta o no.", "Sé nombrar sonidos fuertes, suaves, rápidos y lentos."],
    explain=[
        "Una música puede dejarnos una sensación: tranquila, alegre, misteriosa, traviesa o fuerte. Esa sensación aparece porque algo suena de cierta manera. Eso que suena es la pista sonora: por ejemplo, «suena lento y suave».",
        "Para hablar de lo que sentimos usamos una frase de dos partes: «Me parece ___ porque suena ___». En la primera parte va la sensación y en la segunda, la pista sonora. Ejemplo: «Me parece tranquila porque suena lenta y suave».",
        "Decir «me gusta» o «no me gusta» no alcanza, porque no cuenta qué se oyó. Las palabras de sensación también ayudan: tranquilo, alegre, travieso, misterioso, grande, pequeño, asustado, feliz. Puedes elegir otra palabra si la explicas con una pista.",
    ],
    vocab=[("sensación", "lo que siento al oír algo"), ("pista sonora", "lo que se oye y explica mi sensación"), ("tranquilo", "que da calma"), ("misterioso", "que da curiosidad o un poco de miedo"), ("travieso", "que parece jugar o saltar")],
    worked=[
        {"title": "Completar la frase de dos partes", "problem": "Un adulto toca un cascabel agudo muy rápido y suave. Completa: «Me parece ___ porque suena ___».", "steps": ["Pienso qué sensación me deja: algo ligero y juguetón.", "Busco la pista: agudo, rápido y suave.", "Armo la frase uniendo las dos partes."], "answer": "Me parece travieso porque suena agudo, rápido y suave"},
        {"title": "Distinguir gusto de descripción", "problem": "Mario dice «me gusta» sobre una música lenta y grave. ¿Qué le falta?", "steps": ["«Me gusta» dice su opinión, pero no lo que oyó.", "Falta una sensación y una pista sonora.", "Puede decir: me parece tranquila porque suena lenta y grave."], "answer": "Le falta la pista sonora"},
    ],
    mistakes=[
        {"wrong": "Decir solo «me gusta».", "why": "Se da una opinión sin describir lo que se oyó.", "fix": "Agrega «porque suena…» y una pista audible."},
        {"wrong": "Decir una sensación sin explicar qué sonido la provoca.", "why": "Falta la pista sonora.", "fix": "Después de la sensación escribe cómo suena: lento, fuerte, agudo, suave."},
    ],
    tiers={
        "recovery": [
            ex("Una música suena lenta y suave. ¿Qué sensación puede dar: tranquila o asustada?", "Tranquila", "Lento y suave suele dar calma."),
            ex("Una música suena rápida y saltarina. ¿Qué palabra le queda: travieso o dormido?", "Travieso", "Lo rápido y saltarín parece juguetón."),
            ex("Pista sonora, ¿es lo que siento o lo que oigo?", "Lo que oigo", "La pista sonora es lo que suena, no lo que siento."),
        ],
        "understand": [
            ex("¿Cómo se completa la frase «Me parece ___ porque suena ___»? Di qué va en cada espacio.", "Una sensación y una pista sonora", "Primero lo que siento, luego lo que oigo."),
            ex("¿Por qué «me gusta» no alcanza para describir una música?", "Porque no dice qué se oyó", "Una descripción necesita una pista audible."),
            ex("¿Pueden dos personas sentir cosas distintas con la misma música si cada una explica con una pista?", "Sí", "La sensación es personal si se apoya en algo que suena."),
        ],
        "apply": [
            ex("Un tambor grave suena muy fuerte y despacio. Completa la frase con una sensación.", "Me parece grande o fuerte porque suena grave, fuerte y despacio (o una sensación parecida bien explicada)", "La frase une la sensación con las pistas graves, fuertes y lentas."),
            ex("Una flauta toca notas agudas y suaves, muy largas. Completa la frase.", "Me parece tranquila o misteriosa porque suena aguda, suave y larga", "Agudo, suave y largo se oye calmado o de misterio."),
            ex("Elige dos palabras del banco (tranquilo, alegre, travieso, misterioso) para una música rápida y fuerte y escribe una pista.", "Alegre o travieso, porque suena rápida y fuerte", "Rápido y fuerte da energía y juego."),
        ],
        "reason": [
            ex("Ana dice «esta música es alegre» y no dice nada más. ¿Qué le puedes preguntar?", "¿Qué oíste que te hace pensar que es alegre?", "Se pide la pista sonora."),
            ex("Beto dice «me parece misteriosa porque suena lenta y muy suave». ¿Dio una pista sonora?", "Sí", "Lenta y muy suave son cosas que se oyen."),
        ],
        "challenge": [
            ex("Una música cambia de lenta y suave a rápida y fuerte. Escribe dos frases, una por cada parte.", "Parte 1: me parece tranquila porque suena lenta y suave. Parte 2: me parece alegre o energética porque suena rápida y fuerte", "Cada parte tiene su sensación con su pista."),
            ex("Escribe tres palabras de sensación distintas que no sean tranquilo ni alegre.", "Por ejemplo: travieso, misterioso, asustado", "Cualquier sensación válida del banco o similar sirve."),
        ],
    },
    context=[ex("Cuando duermes a tu peluche, tarareas una melodía lenta, suave y larga. ¿Qué sensación das y qué pista sonora usas?", "Tranquilidad; lenta, suave y larga", "Esas pistas hacen que la música calme.")],
    selfcheck=[ex("¿Qué palabra de sensación combina con música lenta y suave?", "Tranquila", "Lo suave y lento calma."), ex("¿Qué es una pista sonora?", "Lo que se oye y explica mi sensación", "Es una característica del sonido."), ex("Completa: Me parece ___ porque suena ___. ¿Qué va primero?", "La sensación", "La frase parte con lo que siento.")],
    open_task=task(
        "Un adulto toca tres sonidos: (1) una cuchara en un vaso de vidrio, suave y fino; (2) una olla golpeada fuerte y grave; (3) las palmas muy rápidas. Para cada uno escribe o di una frase con la forma «Me parece ___ porque suena ___».",
        "(1) Me parece delicado porque suena suave y fino. (2) Me parece grande porque suena fuerte y grave. (3) Me parece travieso porque suena rápido.",
        ["escribe una frase para cada sonido", "usa una sensación y una pista sonora", "la pista es algo que se oye"],
        ["tres frases", "dibujo de cada sonido", "explicación oral"],
        ["decir solo me gusta", "dar una sensación sin pista sonora"],
        "Reconoce la sensación elegida y pide la pista; si solo dice «me gusta», ayúdalo con la pregunta «¿cómo sonaba?».",
    ),
    reinforce="Elige un sonido de tu casa y di una frase «Me parece ___ porque suena ___» para ese sonido.",
    extend="Compara dos sonidos usando la palabra «en cambio» y una pista distinta para cada uno.",
)

register(
    OA2, 3,
    materials="Papel, lápiz y colores. Las ideas de música están descritas por escrito. Un adulto puede leerlas o producirlas con objetos de la casa.",
    use="Aprenderé a traducir lo que oigo a un dibujo o a otro sonido. Sirve para expresar mis ideas sobre la música con otros medios, no solo con palabras.",
    prior=["Sé hacer líneas y puntos en un papel.", "Sé decir si un sonido es fuerte o suave."],
    explain=[
        "Podemos responder a la música dibujando. Una línea ondulada suave puede mostrar un sonido suave y largo. Puntos pequeños y juntos pueden mostrar sonidos cortos y rápidos. Un zigzag grande y fuerte puede mostrar un sonido fuerte y agitado.",
        "También podemos responder con otro sonido. Si oigo un tambor lento, puedo contestar con palmas lentas. Si oigo un cascabel rápido, puedo contestar con golpecitos rápidos en la mesa. Traducir es cambiar de medio, pero mantener la idea.",
        "Cuando termines, cuenta qué quisiste mostrar: «Dibujé una línea ondulada porque el sonido era suave y largo». Cualquier dibujo es válido si puedes explicar la pista sonora. Los colores también pueden ayudar, como azul para sonidos suaves y rojo para fuertes.",
    ],
    vocab=[("línea ondulada", "línea con curvas suaves, como olas"), ("zigzag", "línea con picos"), ("puntos", "marcas pequeñas, una por sonido corto"), ("traducir", "mostrar la misma idea con otro medio"), ("medio", "forma de expresar: palabras, dibujo, movimiento o sonido")],
    worked=[
        {"title": "De sonido a dibujo", "problem": "Suena una nota larga y suave. ¿Cómo la dibujas?", "steps": ["Larga: dibujo una línea que se alarga.", "Suave: la hago delgada y con curvas.", "Resultado: una línea ondulada larga y delgada."], "answer": "Línea ondulada larga y delgada"},
        {"title": "De dibujo a sonido", "problem": "Ves una fila de seis puntos pequeños. ¿Qué sonido muestran?", "steps": ["Los puntos son marcas cortas.", "Hay seis, así que son seis sonidos.", "Los toco con la yema de los dedos sobre la mesa, cortos y suaves."], "answer": "Seis golpecitos cortos y suaves"},
    ],
    mistakes=[
        {"wrong": "Dibujar algo que no tiene relación con lo que se oyó.", "why": "Se pierde la pista sonora.", "fix": "Antes de dibujar di cómo sonaba y usa líneas que lo muestren."},
        {"wrong": "No explicar el dibujo.", "why": "Otra persona no puede saber la idea.", "fix": "Escribe una frase que diga qué quisiste mostrar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué línea muestra mejor un sonido suave y largo: ondulada o picuda?", "Ondulada", "Las curvas suaves van con lo suave y largo."),
            ex("¿Qué dibujo muestra sonidos cortos: puntos o una línea larga?", "Puntos", "Los puntos son marcas cortas."),
            ex("¿Qué zigzag muestra un sonido fuerte: uno grande o uno chiquito?", "Uno grande", "Un trazo grande muestra más fuerza."),
        ],
        "understand": [
            ex("¿Qué significa traducir una música a un dibujo?", "Mostrar la misma idea con otro medio", "Se conserva lo que se oyó."),
            ex("¿Para qué escribes una frase junto a tu dibujo?", "Para explicar qué sonido mostré", "Así otros entienden tu idea."),
            ex("¿Se puede responder a un tambor lento con palmas lentas?", "Sí", "Es traducir un sonido a otro sonido."),
        ],
        "apply": [
            ex("Suenan cinco golpes cortos. ¿Cuántos puntos dibujas?", "5", "Un punto por cada sonido corto."),
            ex("Suena una nota que sube de grave a aguda. ¿Cómo es tu línea: sube o baja?", "Sube", "Agudo se dibuja arriba."),
            ex("Suena un cascabel muy rápido y suave. ¿Qué dibujas: puntos pequeños juntos o una línea gruesa?", "Puntos pequeños juntos", "Rápido y suave se muestra con marcas chicas y cercanas."),
        ],
        "reason": [
            ex("Diego dibujó una línea recta y dice que muestra un sonido que sube y baja. ¿Qué cambiarías?", "Haría una línea que suba y baje", "El dibujo debe mostrar el movimiento del sonido."),
            ex("Dos niñas dibujan el mismo sonido de dos formas distintas y explican bien. ¿Está mal una de las dos?", "No", "Ambos dibujos pueden mostrar la misma pista."),
        ],
        "challenge": [
            ex("Dibuja en palabras una música con tres partes: suave y larga, corta y rápida, otra vez suave y larga. Describe tu dibujo.", "Línea ondulada, luego puntos, luego otra línea ondulada", "La primera parte regresa al final."),
            ex("Traduce a sonido de palmas este dibujo: ● ● ○○ □. Escribe cómo suenan las palmas.", "TA, TA, ti-ti, silencio", "Cada símbolo se traduce en el sonido que representa."),
        ],
    },
    context=[ex("Quieres dibujar para tu abuela la música de un arrullo: sube un poco, baja un poco, siempre suave y larga. ¿Qué línea haces?", "Una línea ondulada suave que sube y baja", "Una curva suave muestra un arrullo.")],
    selfcheck=[ex("¿Qué línea va con un sonido suave y largo?", "Una línea ondulada larga", "Las curvas largas muestran suavidad."), ex("¿Cuántos puntos para cuatro golpes cortos?", "4", "Un punto por golpe."), ex("¿Cómo muestras un sonido agudo en un dibujo?", "Arriba en la hoja", "Lo agudo se pone alto.")],
    open_task=task(
        "Un adulto toca esta música: tres golpes suaves y largos en un tarro, luego cinco golpecitos rápidos y fuertes en la mesa. Dibuja una línea para cada parte: elige línea ondulada, puntos o zigzag. Escribe una frase que explique cada dibujo.",
        "Para los tres golpes suaves y largos hice tres ondas delgadas azules. Para los cinco golpecitos rápidos y fuertes hice cinco puntos grandes rojos. Elegí ondas porque duraban y eran suaves.",
        ["hay un dibujo para cada parte", "el dibujo se relaciona con lo que se oyó", "escribe o dice una frase de explicación"],
        ["dibujo", "frase", "explicación oral"],
        ["dibujos sin relación con el sonido", "no explicar los dibujos"],
        "Reconoce la relación entre sonido y trazo y pregunta por qué eligió ese tipo de línea; si el dibujo no coincide, que vuelva a escuchar una parte.",
    ),
    reinforce="Dibuja cuatro sonidos cortos como puntos y un sonido largo como una línea.",
    extend="Elige una música de tu casa y dibuja su forma completa con líneas y colores. Explica los colores.",
)

register(
    OA2, 4,
    materials="Lápiz y una hoja. La audición y las respuestas de dos niños están escritas en esta clase.",
    use="Aprenderé a comparar respuestas distintas a una misma música y a respetarlas. Sirve para entender que una música puede sugerir ideas diferentes.",
    prior=["Sé decir una sensación con una pista sonora.", "Sé escuchar a otra persona sin interrumpir."],
    explain=[
        "Una misma música puede sugerir ideas distintas a diferentes personas. Para unos puede parecer una tormenta; para otros, un tambor que camina. No hay una única respuesta correcta sobre lo que una música significa.",
        "Una respuesta es buena cuando se apoya en una pista sonora. Si alguien dice «es una tormenta porque suena fuerte y grave, y los golpes son largos», dio una razón que se oye. Si dice «es una tormenta» y no puede decir por qué, falta la pista.",
        "Para conversar con respeto, escucha primero, pregunta por la pista y di qué ideas se parecen o se diferencian. Una buena frase es «Yo oí otra cosa porque…». No se corrige a la otra persona por sentir distinto.",
    ],
    vocab=[("interpretación", "lo que cada persona entiende de una música"), ("distinto", "que no es igual"), ("respetar", "escuchar y aceptar sin burlarse"), ("razón", "la pista que explica mi idea"), ("comparar", "decir en qué se parecen y en qué se diferencian dos cosas")],
    worked=[
        {"title": "Dos respuestas distintas", "problem": "Una música suena lenta, grave y fuerte. Lucía dice: «Parece un oso caminando porque es grave y lenta». Tomás dice: «Parece un trueno porque es grave y fuerte». ¿Están bien los dos?", "steps": ["Lucía usa las pistas grave y lenta.", "Tomás usa las pistas grave y fuerte.", "Cada uno apoya su idea con algo que se oye."], "answer": "Sí, ambos están bien porque cada uno da una pista sonora"},
        {"title": "Una respuesta sin pista", "problem": "Una niña dice: «Es triste» y no sabe por qué. ¿Qué le puedes preguntar?", "steps": ["Quiero conocer la pista sonora.", "Le pregunto qué oyó.", "Puede decir que era lenta y suave."], "answer": "¿Qué oíste que te hace pensar que es triste?"},
    ],
    mistakes=[
        {"wrong": "Decir «tu respuesta está mal» a otra persona porque sintió algo distinto.", "why": "Se cree que hay una sola emoción correcta.", "fix": "Pregunta por la pista sonora y cuenta tu propia idea."},
        {"wrong": "Cambiar mi idea solo porque otro dijo algo distinto.", "why": "Pensé que debía coincidir con los demás.", "fix": "Mantén tu idea si tienes una pista que la apoya."},
    ],
    tiers={
        "recovery": [
            ex("Ana oye una música y dice «parece una fiesta». Tú oyes la misma música y dices «parece un paseo tranquilo». ¿Puede ser que ambas ideas sean posibles?", "Sí", "Cada persona puede sentir distinto."),
            ex("¿Qué debe tener una buena respuesta sobre una música?", "Una pista sonora", "La pista muestra lo que se oyó."),
            ex("¿Está bien burlarse de la idea de otro?", "No", "Hay que respetar las ideas distintas."),
        ],
        "understand": [
            ex("¿Por qué una música puede sugerir ideas distintas?", "Porque cada persona oye y siente a su manera", "Las experiencias son diferentes."),
            ex("¿Qué frase puedes usar para hablar con respeto de una idea distinta?", "Yo oí otra cosa porque…", "Muestra tu idea sin corregir al otro."),
            ex("Una música tiene una sola respuesta correcta, ¿verdadero o falso?", "Falso", "Hay varias respuestas válidas si se explican."),
        ],
        "apply": [
            ex("Dos niños oyen una música rápida y aguda. Uno dice «parece un pájaro» y otro «parece lluvia». ¿Qué pista sonora podrían compartir?", "Es rápida y aguda", "Ambos pueden basarse en lo rápido y agudo."),
            ex("Escribe una pregunta respetuosa para alguien que dijo «es un monstruo».", "¿Qué oíste que te hizo pensar en un monstruo?", "La pregunta busca la pista sin juzgar."),
            ex("Completa: Yo oí otra cosa porque la música sonaba ___. Usa la pista «lenta».", "Yo oí otra cosa porque la música sonaba lenta", "La frase incluye la pista que cada uno usa."),
        ],
        "reason": [
            ex("Pablo dice: «Mi hermana cree que la música es feliz, pero está equivocada». ¿Qué le dirías?", "Que no hay una sola respuesta correcta y que le pregunte por su pista sonora", "Una idea distinta puede estar bien apoyada."),
            ex("Si dos niños dicen lo mismo, ¿tienen que tener las mismas razones?", "No", "Pueden coincidir en la idea con pistas diferentes."),
        ],
        "challenge": [
            ex("Lee las dos respuestas. Niña 1: «Es alegre porque va rápido». Niña 2: «Es nerviosa porque va rápido». ¿En qué se parecen y en qué se diferencian?", "Se parecen en la pista (rápido); se diferencian en la sensación", "Las dos usan la misma pista pero sienten algo distinto."),
            ex("Inventa tu propia frase para una música lenta y suave que otra persona llamó «aburrida». Usa una pista.", "A mí me parece calmada porque suena lenta y suave", "La frase respeta la idea del otro y da tu razón."),
        ],
    },
    context=[ex("En un recreo escuchan una música de flauta. Un niño dice que es un día de sol, otra niña que es un viento fresco. ¿Cómo pueden conversar sin discutir?", "Preguntando qué oyó cada uno y diciendo yo oí otra cosa porque…", "Compartir las pistas permite respetar ambas ideas.")],
    selfcheck=[ex("¿Hay una única emoción correcta para una música?", "No", "Las personas pueden sentir distinto."), ex("¿Qué hay que dar para que una idea sea buena?", "Una pista sonora", "Eso muestra lo que se oyó."), ex("¿Cómo respondes si otra persona siente distinto a ti?", "Escucho y cuento mi idea con respeto", "Se aceptan ideas distintas.")],
    open_task=task(
        "Lee esta escena y completa lo que falta. Un adulto toca: golpes lentos, graves y suaves en un tarro. Valentina dice: «Parece un oso durmiendo». Joaquín dice: «Parece un tren lejano». (1) Escribe la pista sonora que podrían compartir los dos. (2) Escribe una frase tuya: «A mí me parece ___ porque suena ___». (3) Escribe una pregunta respetuosa para Joaquín.",
        "(1) Suena lento, grave y suave. (2) A mí me parece un barco porque suena lento y grave. (3) ¿Qué oíste que te hizo pensar en un tren?",
        ["identifica una pista sonora compartida", "da su propia idea con pista", "formula una pregunta respetuosa"],
        ["tres respuestas escritas o dichas", "explicación oral"],
        ["decir que una respuesta es incorrecta", "dar una idea sin pista"],
        "Reconoce la pista identificada y la pregunta respetuosa; si juzga la idea de otro, que reformule con «yo oí otra cosa porque…».",
    ),
    reinforce="Pregunta a alguien qué le parece un sonido de la casa y escucha su razón sin corregirlo.",
    extend="Escribe dos ideas distintas para una misma música y una pista que apoye cada una.",
)

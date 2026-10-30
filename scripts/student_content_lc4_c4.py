"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS04 (escritura inicial de algunas palabras culturalmente significativas) y OA LS05 (presencia de la lengua indígena
en expresiones artísticas: textiles, musicales y literarias, con creaciones digitales de sensibilización).

Criterio de autoría: todas las fichas, bancos de palabras, obras, escuelas y personas son inventados solo para practicar
y están rotulados como tales; las canciones, poemas y textiles de práctica son originales de este cuaderno y no
reproducen ninguna obra real ni sus diseños. Las únicas expresiones en lengua indígena son saludos y palabras muy
atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke) y el nombre de la lengua mapuche en dos
escrituras usadas (mapuzugun, mapudungun). No se inventa gramática, pronunciación ni significado de símbolos de textiles
o de música. Los recursos digitales se describen sin marcas ni enlaces y siempre con un adulto. Cada tarea abierta
remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS4, LS5 = "LC04 OA LS04", "LC04 OA LS05"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_SAL = "Ficha: «mari mari» es un saludo y «chaltumay» quiere decir «gracias», ambas en mapuzugun."
FICHA_PAL = "Ficha de palabras en mapuzugun (de práctica): «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es la casa mapuche, «mapu» es tierra, «ñuke» es madre."


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


BANCO = "Banco de palabras autorizado (inventado para practicar): la educadora tradicional de la Escuela Ejemplo autoriza «ko» (agua), «antü» (sol), «kuyen» (luna), «ruka» (casa mapuche) y «mapu» (tierra), todas en mapuzugun. Contexto de uso: rótulos y frases cortas de la sala."

# =================================================================== LS04 clase 1 · observar modelo y procedencia
L(
    LS4, 1,
    materials="Lápiz y hoja. El banco de palabras está escrito aquí; es inventado para practicar y no pertenece a ninguna escuela real.",
    use="Aprenderé a observar un banco de palabras con su significado y su contexto de uso antes de escribir, y a anotar su procedencia. Sirve para escribir palabras significativas con respeto y sin errores.",
    prior=["Sé copiar una palabra letra por letra desde un modelo.", "Sé que la fuente y el permiso se anotan en una ficha."],
    explain=[
        "Un banco de palabras es una lista de palabras que una fuente autoriza usar. Cada palabra viene con su significado, que dice qué quiere decir, y su contexto de uso, que dice dónde se usa: en un rótulo, en una frase o en un afiche. El banco es mi modelo: de ahí copio, y no de mi memoria.",
        "Antes de escribir observo el banco con cuatro preguntas. ¿Cuál es la palabra y cómo se escribe, letra por letra? ¿Qué significa? ¿Dónde se puede usar? ¿Quién la autorizó? Presto atención a las letras especiales, como la ü de «antü» y la ñ de «ñuke», porque cambiar una letra cambia la palabra escrita.",
        "La procedencia del banco se anota siempre al lado: quién enseñó las palabras y dónde se autorizó usarlas. Una palabra que no está en el banco no la uso, aunque la haya visto en otro lugar. Si necesito otra palabra, se la pido a la educadora o al educador tradicional y espero su respuesta.",
    ],
    vocab=[("banco de palabras", "lista de palabras que una fuente autoriza usar"), ("significado", "lo que quiere decir una palabra"), ("contexto de uso", "dónde se usa una palabra"), ("grafía", "forma de escribir una palabra con letras"), ("autorizar", "dar permiso para usar algo")],
    worked=[
        W("Leer el banco", BANCO + " ¿Qué significa «kuyen» y dónde se puede usar?", ["Busco «kuyen» en el banco.", "Dice: luna.", "El contexto es rótulos y frases cortas de la sala."], "luna; en rótulos y frases cortas de la sala"),
        W("Detectar una palabra no autorizada", BANCO + " Un niño quiere escribir «ñuke» en un rótulo. ¿Está en el banco?", ["Reviso las cinco palabras del banco: ko, antü, kuyen, ruka y mapu.", "«Ñuke» no está.", "Debe pedir permiso a la educadora."], "no está; pide permiso a la educadora"),
    ],
    mistakes=[
        M("Escribir una palabra de memoria sin mirar el banco.", "Puedo cambiar una letra sin darme cuenta.", "Copio desde el banco, letra por letra."),
        M("Usar una palabra que no está en el banco porque la vi en un cartel.", "No tiene la autorización de mi fuente.", "Pido permiso a la educadora tradicional."),
    ],
    R=[
        ex(BANCO + " ¿Cuántas palabras autoriza el banco?", "5", "Son ko, antü, kuyen, ruka y mapu."),
        ex(BANCO + " ¿Qué significa «mapu»?", "tierra", "El banco lo dice."),
        ex("Un banco de palabras, ¿es una lista de palabras autorizadas o una lista de palabras inventadas?", "una lista de palabras autorizadas", "Una fuente las autoriza."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir una palabra que no está en el banco si la vi en un cartel.", "Falso", "Debo pedir permiso."),
        ex(BANCO + " El contexto de uso, ¿dice dónde se usan las palabras o quién las escribió?", "dónde se usan las palabras", "Contexto de uso es el lugar o la situación."),
        ex("Letras especiales del banco: ü de «antü». ¿Se puede cambiar por u? Sí o No.", "No", "Cambia la palabra escrita."),
    ],
    A=[
        ex(BANCO + " ¿Qué palabra del banco tiene la letra ü?", "antü", "Solo «antü» tiene ü en el banco."),
        ex(BANCO + " Dibujo: la casa mapuche. ¿Qué palabra del banco rotula ese dibujo?", "ruka", "Es la que significa casa mapuche."),
        ex("Un niño copió «kuyen» y escribió «kuyén». ¿Qué agregó que el banco no tiene?", "una tilde", "El banco escribe «kuyen» sin tilde."),
    ],
    Z=[
        ex("Una niña dice: «Si me acuerdo de la palabra, no necesito mirar el banco». ¿Tiene razón? Sí o No.", "No", "Puede cambiar una letra sin darse cuenta."),
        ex("Dos formas de preparar un rótulo: A) copiar del banco y anotar la fuente. B) escribir de memoria y anotar la fuente al final. ¿Cuál es más segura?", "A", "Copiar del banco evita errores."),
    ],
    D=[
        ex("Ordena para observar un modelo: A) leo dónde se usa. B) leo la palabra y su significado. C) anoto quién la autorizó. Escribe las letras.", "B, A, C", "Palabra y significado, uso y fuente."),
        arith("El banco tiene 5 palabras y tu curso ya escribió 3 en los rótulos. ¿Cuántas faltan por usar?", "5-3", "Se restan las palabras ya escritas."),
    ],
    context=[ex("Un compañero te pide una palabra para el rótulo de la mesa de la sala y la que quiere no está en el banco. ¿Le dices «Pidamos permiso a la educadora» o «Escríbela igual»?", "«Pidamos permiso a la educadora»", "Solo se usan palabras autorizadas.")],
    selfcheck=[
        ex("¿De dónde copio una palabra: del banco o de mi memoria?", "del banco", "El banco es el modelo."),
        ex("¿Qué dato anoto siempre junto al banco: la fuente o el color?", "la fuente", "La procedencia se anota."),
        ex("¿Puedo cambiar una letra especial como la ü? Sí o No.", "No", "Cambiaría la palabra."),
    ],
    task=T(
        "Lee este banco de palabras inventado para practicar. " + BANCO + " En tu cuaderno haz una tabla de cuatro columnas: palabra, significado, dónde se usa y fuente. Copia cinco palabras con mucho cuidado, letra por letra. Después escribe una palabra que quieras pedir a la educadora tradicional y que no está en el banco. Termina con una pregunta para el educador o la educadora tradicional.",
        "ko, agua, rótulos de la sala, educadora tradicional de la Escuela Ejemplo. antü, sol, rótulos de la sala, educadora tradicional. Quiero pedir: palabra para «cerro». Pregunta: ¿cómo se escribe el nombre del cerro?",
        ["copia las palabras sin cambiar letras", "anota significado, uso y fuente", "nombra una palabra que pedirá", "formula una pregunta para el educador/a tradicional"],
        ["tabla con cinco palabras", "pregunta escrita o dicha en voz alta"],
        ["cambiar la ü o la ñ", "usar palabras fuera del banco"],
        "Compara cada palabra con el banco letra por letra; si usó una palabra que no está en el banco, pide cambiarla por una pregunta.",
    ),
    reinforce="Copia «ko», «antü» y «kuyen» una vez más y revisa letra por letra con el banco.",
    extend="Escribe una oración con una palabra del banco y anota debajo de dónde la copiaste.",
)

# =================================================================== LS04 clase 2 · escribir para nombrar
L(
    LS4, 2,
    materials="Lápiz, hoja y colores. El banco y las situaciones están escritos aquí; son inventados para practicar.",
    use="Aprenderé a escribir una palabra del banco para nombrar lo que dibujo o lo que veo en mi sala, en un rótulo con su significado y su fuente. Sirve para etiquetar con respeto.",
    prior=["Sé observar un banco de palabras con significado y fuente.", "Sé copiar letra por letra."],
    explain=[
        "Nombrar es poner a una cosa la palabra que le corresponde, para que otros sepan cómo se llama. Escribo para nombrar cuando hago un rótulo: pongo la palabra del banco junto al dibujo y escribo su significado entre paréntesis. Si la palabra es «ko» y dibujo agua, el rótulo dice «ko (agua)».",
        "Para nombrar bien elijo la palabra por su significado, no porque me guste cómo suena. Si el dibujo es del sol, busco en el banco la palabra cuyo significado sea sol, que es «antü». Después copio la palabra letra por letra, escribo el significado y anoto la fuente al pie. Un rótulo completo tiene palabra, significado y fuente.",
        "Si quiero nombrar algo que el banco no tiene, no invento una palabra. Escribo el nombre en castellano y anoto la pregunta para la educadora tradicional. Así mi trabajo es correcto y respeta a quienes cuidan la lengua. Además, cada rótulo se revisa con el banco antes de pegarlo.",
    ],
    vocab=[("nombrar", "poner a una cosa la palabra que le corresponde"), ("rótulo", "palabra escrita junto a un dibujo u objeto"), ("fuente", "persona que enseñó la palabra"), ("significado", "lo que quiere decir la palabra"), ("revisar", "leer de nuevo y comparar con el modelo")],
    worked=[
        W("Elegir la palabra por su significado", BANCO + " Dibujo: la luna. ¿Cuál es el rótulo?", ["Busco la palabra cuyo significado sea luna.", "El banco dice: «kuyen».", "Escribo la palabra y el significado."], "kuyen (luna)"),
        W("Rótulo completo", BANCO + " Dibujo: la tierra de una plaza. Fuente: educadora de la Escuela Ejemplo. Escribe el rótulo con sus tres partes.", ["La palabra del banco para tierra es «mapu».", "Agrego el significado entre paréntesis.", "Agrego la fuente."], "mapu (tierra), fuente: educadora de la Escuela Ejemplo"),
    ],
    mistakes=[
        M("Rotular el dibujo de una casa con «ko» porque suena bonito.", "«Ko» es agua; la casa mapuche es «ruka».", "Elijo la palabra por su significado."),
        M("Inventar una palabra para algo que el banco no trae.", "Estaría inventando lengua.", "Escribo el nombre en castellano y pregunto a la educadora."),
    ],
    R=[
        ex(BANCO + " ¿Cuál es la palabra del banco para «sol»?", "antü", "El banco lo dice."),
        ex("Un rótulo completo tiene palabra, significado y fuente. ¿Cuántas partes son?", "3", "Se cuentan tres partes."),
        ex("Para nombrar, ¿elijo la palabra por su significado o por cómo suena?", "por su significado", "El significado decide."),
    ],
    C=[
        ex(BANCO + " Dibujo: una casa mapuche. ¿Con qué palabra la nombras: «ruka» o «ko»?", "ruka", "«Ruka» es la casa mapuche."),
        ex("Verdadero o falso: si el banco no tiene la palabra que necesito, puedo inventarla.", "Falso", "Se pregunta a la educadora."),
        ex("Rótulo: «kuyen (luna)». ¿Qué parte falta para que sea completo?", "la fuente", "Faltan quién enseñó la palabra."),
    ],
    A=[
        ex(BANCO + " Tres dibujos: 1) el agua de un vaso, 2) el sol, 3) la luna. Escribe los rótulos en orden, solo con las palabras.", "ko, antü, kuyen", "Cada palabra sale del banco por su significado."),
        ex("Un niño rotuló el dibujo del sol como «kuyen (sol)». ¿Qué está mal: la palabra o el significado entre paréntesis?", "la palabra", "«Kuyen» es luna; para sol corresponde «antü»."),
        ex("Dibujo: un cerro. El banco no tiene palabra para cerro. ¿Qué haces: A) escribes «cerro» en castellano y preguntas a la educadora. B) inventas una palabra?", "A", "No se inventan palabras."),
    ],
    Z=[
        ex("Una niña dice: «Escribí «mapu (agua)» porque me gustó». ¿Su rótulo es correcto? Sí o No.", "No", "«Mapu» es tierra, no agua."),
        ex("Un rótulo dice «ruka» sin significado ni fuente. Opciones: A) está completo porque trae la palabra. B) le faltan significado y fuente. ¿Cuál es cierta?", "B", "Un rótulo completo tiene tres partes."),
    ],
    D=[
        ex(BANCO + " Cuatro dibujos: sol, agua, casa mapuche y tierra. ¿Cuántos se pueden rotular con una palabra del banco?", "4", "Las cuatro tienen palabra en el banco."),
        ex("Ordena para nombrar: A) copio la palabra letra por letra. B) busco la palabra por su significado. C) anoto la fuente. Escribe las letras en orden.", "B, A, C", "Primero elijo, luego copio y al final anoto la fuente."),
    ],
    context=[ex("Quieres rotular la puerta de la sala de práctica con la palabra para casa mapuche. ¿Escribes «ruka (casa mapuche)» con la fuente o inventas una palabra para sala?", "«ruka (casa mapuche)» con la fuente", "Solo se usa lo que el banco trae.")],
    selfcheck=[
        ex("¿Qué es nombrar?", "poner a una cosa la palabra que le corresponde", "Es dar el nombre."),
        ex("¿Dónde busco la palabra para mi rótulo: en el banco o en mi imaginación?", "en el banco", "El banco la autoriza."),
        ex("¿Cuántas partes tiene un rótulo completo?", "3", "Palabra, significado y fuente."),
    ],
    task=T(
        "Lee el banco inventado para practicar. " + BANCO + " En tu cuaderno dibuja tres cosas del banco y rotula cada una con palabra, significado y fuente (educadora de la Escuela Ejemplo). Después escribe una cosa que dibujaste y no tiene palabra en el banco, con su nombre en castellano. Termina con una pregunta para el educador o la educadora tradicional.",
        "antü (sol), fuente: educadora de la Escuela Ejemplo. ko (agua), fuente: educadora. ruka (casa mapuche), fuente: educadora. Sin palabra: cerro. Pregunta: ¿cómo se dice cerro?",
        ["rotula tres dibujos con tres partes", "copia las palabras sin cambiar letras", "nombra algo sin palabra en el banco", "formula una pregunta para el educador/a tradicional"],
        ["tres dibujos rotulados", "pregunta escrita o dicha en voz alta"],
        ["rotular con una palabra que no corresponde", "inventar una palabra"],
        "Compara cada rótulo con el banco; si inventó una palabra, pídele que la cambie por una pregunta a la educadora tradicional.",
    ),
    reinforce="Escribe tres rótulos con las palabras del banco y revisa su significado.",
    extend="Rotula cinco objetos de tu sala en castellano y escribe una pregunta para el educador tradicional sobre cuáles tienen nombre en la lengua.",
)

# =================================================================== LS04 clase 3 · escribir para caracterizar
L(
    LS4, 3,
    materials="Lápiz y hoja. El banco y los adjetivos están escritos aquí; son de práctica.",
    use="Aprenderé a escribir para caracterizar: decir cómo es algo usando una oración en castellano que lleva una palabra del banco. Sirve para describir con respeto sin inventar frases en la lengua.",
    prior=["Sé nombrar con una palabra del banco.", "Sé que una oración empieza con mayúscula y termina con punto."],
    explain=[
        "Caracterizar es decir cómo es algo: sus rasgos o cualidades. Para caracterizar uso adjetivos, que son palabras que dicen cómo es lo que nombro, como «clara», «cálido», «brillante», «grande». En «El sol (antü) es cálido», «cálido» caracteriza al sol, y «antü» es la palabra del banco.",
        "Una oración para caracterizar tiene tres partes: lo que describo, la palabra «es» o «está» y el adjetivo. Por ejemplo: «La luna (kuyen) es brillante.» Pongo la palabra del banco entre paréntesis junto a lo que describo. Reviso que concuerde: si es femenino, «clara»; si es masculino, «claro».",
        "Caracterizo lo que observo con mis sentidos y lo que sé por el banco, no lo que supongo. No digo cosas sobre ceremonias ni sobre significados espirituales de las palabras: eso lo explican el educador o la educadora tradicional. Mis oraciones son simples, con mayúscula y punto, y las reviso con el banco.",
    ],
    vocab=[("caracterizar", "decir cómo es algo"), ("adjetivo", "palabra que dice cómo es lo que se nombra"), ("rasgo", "característica de algo"), ("concordar", "que el adjetivo coincida en género con lo que describe"), ("observar", "mirar con atención")],
    worked=[
        W("Armar una oración para caracterizar", BANCO + " Describe el agua con el adjetivo «clara» usando la palabra «ko».", ["Elijo lo que describo: el agua.", "Escribo «El agua (ko)» y «es clara».", "Agrego mayúscula y punto."], "El agua (ko) es clara."),
        W("Elegir el adjetivo que concuerda", "Describes la luna (kuyen), que es femenina. ¿Qué adjetivo concuerda: «redonda» o «redondo»?", ["La luna es una palabra femenina.", "El adjetivo debe terminar igual: redonda.", "«Redondo» es masculino."], "redonda"),
    ],
    mistakes=[
        M("Caracterizar con una frase en la lengua indígena inventada.", "No sé cómo se dice y estaría inventando.", "Escribo la oración en castellano con la palabra del banco entre paréntesis."),
        M("Decir cómo es algo sin haberlo observado.", "Puedo escribir algo que no es cierto.", "Describo lo que veo o lo que dice el banco."),
    ],
    R=[
        ex("Un adjetivo, ¿dice cómo es lo que nombro o a qué hora ocurre?", "dice cómo es lo que nombro", "Eso hace un adjetivo."),
        ex("En «El sol (antü) es cálido», ¿qué adjetivo caracteriza al sol?", "cálido", "Dice cómo es el sol."),
        ex("En «El sol (antü) es cálido», ¿qué palabra viene del banco?", "antü", "Está entre paréntesis."),
    ],
    C=[
        ex("Verdadero o falso: caracterizar es decir cómo es algo.", "Verdadero", "Es describir sus rasgos."),
        ex("¿Qué oración caracteriza a la luna? A) «La luna (kuyen) es brillante.» B) «Mañana vamos al museo.»", "A", "La A dice cómo es la luna."),
        ex("Una oración para caracterizar debe terminar con punto. ¿Sí o No?", "Sí", "Toda oración termina con punto."),
    ],
    A=[
        ex("Ordena para formar una oración: clara, el, es, agua, (ko). Agrega mayúscula y punto.", "El agua (ko) es clara.", "Primero lo que describo, luego «es» y el adjetivo."),
        ex("Completa con el adjetivo que concuerda con la tierra (femenino): «La tierra (mapu) está ____». Elige entre húmeda y húmedo.", "húmeda", "«Tierra» es femenino."),
        ex("Completa con la palabra del banco: «El ____ es cálido». Elige entre antü y ko.", "antü", "El sol es cálido; «antü» es sol."),
    ],
    Z=[
        ex("Una niña escribe: «La ruka es roja», pero nunca ha visto una ruka de ese color. ¿Puede afirmarlo? Sí o No.", "No", "Debe describir solo lo que observa o sabe."),
        ex("Dos oraciones: A) «El agua (ko) es transparente.» B) «El agua (ko) es mágica para todos los pueblos.» ¿Cuál es adecuada para caracterizar?", "A", "La B afirma algo que no se sabe y generaliza."),
    ],
    D=[
        ex("Oración: «El sol (antü) es cálido y la luna (kuyen) es brillante.» ¿Cuántas palabras del banco usa?", "2", "Usa antü y kuyen."),
        ex("Ordena los pasos: A) agrego el adjetivo. B) elijo lo que describo. C) pongo la palabra del banco entre paréntesis. D) reviso mayúscula y punto. Escribe las letras.", "B, C, A, D", "Elijo, nombro, caracterizo y reviso."),
    ],
    context=[ex("En un cartel de la sala quieres escribir cómo es el agua que se toma en el recreo. ¿Escribes «El agua (ko) es fresca.» o inventas una frase en la lengua?", "«El agua (ko) es fresca.»", "Se describe en castellano con la palabra del banco.")],
    selfcheck=[
        ex("¿Qué palabra dice cómo es algo: el adjetivo o el verbo?", "el adjetivo", "El adjetivo describe."),
        ex("¿Describo lo que observo o lo que supongo?", "lo que observo", "Lo supuesto puede ser falso."),
        ex("¿Dónde pongo la palabra del banco en mi oración: entre paréntesis o inventando una frase?", "entre paréntesis", "No se inventan frases."),
    ],
    task=T(
        "Escribe tres oraciones para caracterizar usando el banco inventado. " + BANCO + " Elige tres palabras del banco (por ejemplo el agua, el sol y la luna), pon cada una entre paréntesis y agrega un adjetivo que describa lo que observas. Revisa mayúscula, punto y la palabra escrita igual que en el banco. Termina con una pregunta para el educador o la educadora tradicional sobre algo que no sabes describir.",
        "El agua (ko) es clara. El sol (antü) es cálido. La luna (kuyen) es brillante. Pregunta: ¿cómo se dice «clara» en la lengua?",
        ["escribe tres oraciones", "usa una palabra del banco en cada una", "agrega un adjetivo que concuerda", "formula una pregunta para el educador/a tradicional"],
        ["tres oraciones escritas", "pregunta escrita o dicha en voz alta"],
        ["inventar frases en la lengua", "olvidar mayúscula o punto"],
        "Revisa adjetivo, mayúscula, punto y la palabra del banco; si inventó una frase en la lengua, pide cambiarla por una pregunta.",
    ),
    reinforce="Escribe dos adjetivos para el sol y dos para la luna, en castellano.",
    extend="Escribe una oración con dos palabras del banco y dos adjetivos.",
)

# =================================================================== LS04 clase 4 · revisar sin jerarquizar variantes
CARTEL_N = "Cartel Norte (inventado): la educadora tradicional de la Escuela Ejemplo Norte escribe el nombre de la lengua mapuche como «mapuzugun»."
CARTEL_S = "Cartel Sur (inventado): el educador tradicional de la Escuela Ejemplo Sur escribe el nombre de la lengua mapuche como «mapudungun»."

L(
    LS4, 4,
    materials="Lápiz y un lápiz de otro color. Los carteles y las listas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a revisar mi escritura con el banco y a respetar que una palabra puede escribirse de más de una forma, sin decir que una variante es mejor que otra. Sirve para escribir con cuidado y sin jerarquizar.",
    prior=["Sé escribir para nombrar y para caracterizar.", "Sé qué es una variante."],
    explain=[
        "Revisar es comparar lo que escribí con el banco y corregir lo que no coincide. Reviso la palabra, letra por letra; el significado entre paréntesis; la mayúscula y el punto de la oración; y la fuente. Marco con otro color lo que cambio y no borro todo, para ver lo que corregí.",
        "A veces dos fuentes escriben la misma palabra de forma distinta. Por ejemplo, el nombre de la lengua mapuche se ve «mapuzugun» y «mapudungun». Cada una es una variante: una escritura válida de una comunidad o institución. Jerarquizar es decir que una variante es mejor, más correcta o más importante que otra, y no debo hacerlo.",
        "Cuando mi banco trae una escritura, uso esa. Si veo otra variante, no la llamo «error»: anoto de dónde viene y pregunto al educador tradicional por qué existe y cuál usar en mi trabajo. Y no mezclo variantes en un mismo texto, porque el lector se confunde. Un trabajo respetuoso usa una forma y reconoce que existen otras.",
    ],
    vocab=[("variante", "otra escritura válida de la misma palabra"), ("jerarquizar", "decir que una variante es mejor que otra"), ("corregir", "cambiar lo que no coincide con el modelo"), ("mezclar", "usar dos escrituras distintas en un mismo texto"), ("coincidir", "ser igual en todo")],
    worked=[
        W("Comparar con el banco", BANCO + " Escrito de un niño: «El sol (antu) es cálido.» ¿Qué corriges?", ["Comparo la palabra con el banco.", "El banco escribe «antü», con ü.", "Corrijo «antu» por «antü»."], "antu por antü"),
        W("No jerarquizar", CARTEL_N + " " + CARTEL_S + " Un niño dice: «El Norte está correcto y el Sur está mal». ¿Qué respondes?", ["Cada cartel tiene su fuente.", "Son dos variantes.", "Ninguno está mal."], "ninguno está mal: son dos variantes con fuente"),
    ],
    mistakes=[
        M("Llamar «error» a una variante porque no es la de mi banco.", "Es una escritura válida de otra fuente.", "Anoto la variante con su fuente y pregunto al educador tradicional."),
        M("Usar dos escrituras de la misma palabra en un mismo texto.", "El texto queda confuso.", "Elijo la del banco de mi escuela."),
    ],
    R=[
        ex(CARTEL_N + " ¿Cómo escribe esta escuela el nombre de la lengua?", "mapuzugun", "El cartel Norte lo dice."),
        ex(CARTEL_S + " ¿Cómo escribe esta escuela el nombre de la lengua?", "mapudungun", "El cartel Sur lo dice."),
        ex("Revisar, ¿es comparar con el banco o escribir de memoria?", "comparar con el banco", "Revisar es comparar."),
    ],
    C=[
        ex("Verdadero o falso: jerarquizar variantes es decir que una es mejor que otra.", "Verdadero", "Eso es jerarquizar."),
        ex("Dos escrituras de una palabra, cada una con su fuente, ¿son variantes o errores?", "variantes", "Cada una es válida."),
        ex(BANCO + " ¿Cómo escribe el banco la palabra para sol?", "antü", "El banco usa esa escritura."),
    ],
    A=[
        ex(BANCO + " Escrito: «El agua (ko) es clara». ¿Qué le falta a la oración para estar revisada?", "el punto final", "Debe terminar con punto."),
        ex(BANCO + " Escrito: «La luna (kuyen) es brillante.» ¿Hay algo que corregir? Sí o No.", "No", "Coincide con el banco y está bien escrita."),
        ex("Un niño usa «mapuzugun» en la primera línea y «mapudungun» en la tercera del mismo texto. ¿Qué problema tiene?", "mezcla dos variantes", "Debe usar una sola."),
    ],
    Z=[
        ex("Una niña dice: «El nombre de mi banco es el único correcto». ¿Qué falta: reconocer que existen otras variantes o escribir más fuerte?", "reconocer que existen otras variantes", "Respetar las variantes evita jerarquizar."),
        ex("Un cartel de otra escuela escribe la palabra distinta a tu banco. Opciones: A) tacharlo. B) anotar su fuente y preguntar al educador tradicional. ¿Cuál haces?", "B", "No se corrige a otra comunidad."),
    ],
    D=[
        ex(BANCO + " Escrito: «el sol (antu) es cálido». Cuenta los errores: mayúscula, ü y punto. ¿Cuántos son?", "3", "Falta la mayúscula, falta la ü y falta el punto."),
        ex("Ordena la revisión: A) pregunto lo que no puedo resolver. B) comparo cada palabra con el banco. C) marco lo que no coincide. D) anoto la fuente. Escribe las letras.", "B, C, A, D", "Comparo, marco, pregunto y anoto."),
    ],
    context=[ex("Tu amigo muestra un cartel de otra escuela con «mapudungun» y dice «Está mal porque en mi banco dice «mapuzugun»». ¿Qué respondes: «Son dos variantes; anotemos las dos» o «Tienes razón»?", "«Son dos variantes; anotemos las dos»", "No se jerarquiza.")],
    selfcheck=[
        ex("¿Qué comparo para revisar: mi texto con el banco o con otro texto mío?", "mi texto con el banco", "El banco es el modelo."),
        ex("¿Debo decir que una variante es mejor? Sí o No.", "No", "Eso es jerarquizar."),
        ex("¿Uso dos variantes de la misma palabra en un texto? Sí o No.", "No", "Debo elegir una sola."),
    ],
    task=T(
        "Revisa este escrito inventado para practicar: «el sol (antu) es cálido y la luna (kuyen) es brillante». " + BANCO + " " + CARTEL_N + " " + CARTEL_S + " En tu cuaderno haz una tabla de dos columnas: error y corrección. Después escribe una frase que explique por qué no tachas ni jerarquizas las variantes de los carteles. Termina con una pregunta para el educador o la educadora tradicional.",
        "Error: falta la mayúscula, corrijo «El». Error: «antu» sin ü, corrijo «antü». Error: falta el punto final. No tacho los carteles porque cada uno tiene su fuente. Pregunta: ¿cuál variante usa nuestra escuela?",
        ["encuentra mayúscula, ü y punto", "corrige solo lo que no coincide", "no jerarquiza las variantes", "formula una pregunta para el educador/a tradicional"],
        ["tabla de errores y correcciones", "frase y pregunta escritas"],
        ["corregir palabras que sí coinciden con el banco", "tachar una variante"],
        "Comprueba que corrija solo lo que no coincide con el banco; si tachó una variante, conversa por qué ambas tienen fuente.",
    ),
    reinforce="Escribe tres oraciones del banco y revisa cada una con un lápiz de otro color.",
    extend="Explica a una persona de tu casa qué es una variante y por qué no hay que decir que una es mejor que otra.",
)

# =================================================================== LS05 clase 1 · definir propósito de sensibilización
OBRAS = "Obras de práctica (inventadas): A) un cojín bordado por el taller de la Escuela Ejemplo con la palabra «ko». B) una canción del curso, «Canción del río», con la palabra «antü». C) un poema breve del curso, «Mañana de sol», con la palabra «kuyen»."

L(
    LS5, 1,
    materials="Lápiz y hoja. Las obras están escritas aquí; son inventadas para practicar. No reproducen textiles, canciones ni poemas reales.",
    use="Aprenderé a reconocer que la lengua indígena está presente en expresiones artísticas (textiles, música y literatura), a valorar por qué importa para la identidad de un pueblo y a decidir el propósito de un recurso digital de sensibilización. Sirve para dar a conocer sin apropiarme.",
    prior=["Sé que las palabras de la lengua las enseña el educador o la educadora tradicional.", "Sé que un recurso tiene propósito y límites."],
    explain=[
        "Las expresiones artísticas son formas de comunicar ideas y sentimientos con arte. Los textiles son telas tejidas o bordadas, la música son canciones y sonidos, y la literatura son poemas, cuentos y relatos escritos. En muchos pueblos originarios la lengua está presente en estas expresiones: en el nombre de una canción, en una palabra bordada o en un poema.",
        "La lengua es parte de la identidad de un pueblo: de cómo se reconocen y cómo se transmiten sus saberes. Cuando una lengua aparece en el arte, muestra que está viva. Por eso la valoro. Pero valorar no es copiar: no tomo diseños, canciones ni versos de una comunidad para usarlos como míos. Las obras que usamos en esta clase son inventadas para practicar.",
        "Un recurso digital de sensibilización es un trabajo pequeño, como un afiche o una presentación, que busca que otros conozcan y respeten una expresión cultural. Su propósito debe responder: ¿qué quiero que la audiencia comprenda o valore? Un buen propósito es «dar a conocer con respeto». Uno malo es «mostrar que yo sé más» o «copiar un diseño porque es bonito».",
    ],
    vocab=[("expresión artística", "forma de comunicar ideas y sentimientos con arte"), ("textil", "tela tejida o bordada"), ("identidad", "lo que hace que un pueblo se reconozca y se sienta parte de él"), ("sensibilizar", "ayudar a que otros conozcan y valoren algo"), ("audiencia", "personas que verán el recurso")],
    worked=[
        W("Reconocer la lengua en una obra", OBRAS + " ¿En cuál obra aparece la palabra «ko» (agua)?", ["Reviso cada obra.", "La obra A es un cojín bordado con «ko».", "Es la A."], "A"),
        W("Elegir un propósito", "Propósitos: 1) dar a conocer con respeto las obras del curso que llevan palabras de la lengua. 2) copiar el diseño de un textil tradicional para decorar. ¿Cuál es un propósito de sensibilización?", ["Sensibilizar es ayudar a que otros conozcan y valoren.", "El 1 lo hace con respeto.", "El 2 copia un diseño."], "1"),
    ],
    mistakes=[
        M("Copiar el diseño de un textil tradicional para que mi afiche se vea más cultural.", "Puede tener un significado que cuida una familia o un pueblo.", "Dibujo algo propio y pregunto al educador tradicional qué puedo mostrar."),
        M("Pensar que valorar la lengua es repetir versos de canciones de una comunidad.", "Esos versos pertenecen a su autoría.", "Valoro escuchando y dando a conocer con permiso y crédito."),
    ],
    R=[
        ex(OBRAS + " ¿En qué obra aparece «antü»?", "en la B", "La canción lo lleva."),
        ex("Un textil, ¿es una tela tejida o bordada o una canción?", "una tela tejida o bordada", "Textil se refiere a las telas."),
        ex("La identidad de un pueblo, ¿es lo que hace que se reconozca como pueblo o un tipo de música?", "lo que hace que se reconozca como pueblo", "Esa es la idea."),
    ],
    C=[
        ex(OBRAS + " ¿Qué obra es literatura: la A, la B o la C?", "la C", "Es el poema breve."),
        ex("Verdadero o falso: valorar la lengua en el arte significa copiar diseños y canciones de otros.", "Falso", "Valorar es dar a conocer con respeto."),
        ex("Un propósito de sensibilización busca A) que otros conozcan y valoren con respeto. B) mostrar que yo sé más. ¿Cuál es?", "A", "Sensibilizar es ayudar a valorar."),
    ],
    A=[
        ex(OBRAS + " ¿Cuántas obras llevan una palabra del mapuzugun?", "3", "Las tres llevan una."),
        ex(OBRAS + " " + FICHA_PAL + " Une cada obra con la palabra y su significado: A, B y C. Escribe los significados en orden.", "agua, sol, luna", "«Ko» es agua, «antü» es sol y «kuyen» es luna."),
        ex("Un curso quiere dar a conocer las tres obras del curso en un afiche. ¿Cuál es el mejor propósito: «que las familias conozcan y valoren las obras del curso con sus palabras» o «que nadie más hable de la lengua»?", "«que las familias conozcan y valoren las obras del curso con sus palabras»", "Es un propósito de sensibilización."),
    ],
    Z=[
        ex("Una niña dice: «Para mostrar la lengua en el arte, voy a copiar un bordado tradicional de un libro». ¿Es respetuoso? Sí o No.", "No", "Puede tener un significado que no corresponde copiar."),
        ex("Dos afiches: A) obras del curso con sus palabras, sin copiar diseños. B) un diseño tradicional copiado de un libro. ¿Cuál sensibiliza con respeto?", "A", "El B se apropia de un diseño."),
    ],
    D=[
        ex("Ordena para definir un propósito: A) pienso quién lo verá. B) empiezo a hacer el recurso. C) escribo qué quiero que valoren. Escribe las letras.", "A, C, B", "Primero la audiencia, luego el propósito y recién después empiezo."),
        arith("Un curso hizo 3 obras (cojín, canción y poema) y quiere mostrar cada una en una lámina con 2 palabras. ¿Cuántas palabras necesita en total?", "3*2", "Se multiplican las láminas por las palabras de cada una."),
    ],
    context=[ex("Quieres hacer una presentación para el día de la lengua con las obras del curso. ¿El propósito es «dar a conocer con respeto» o «copiar el diseño de un textil de un museo»?", "«dar a conocer con respeto»", "Sensibilizar no es copiar.")],
    selfcheck=[
        ex("¿Cuántas expresiones artísticas nombra la clase: textiles, música y literatura?", "3", "Se cuentan tres."),
        ex("¿Valorar la lengua en el arte es copiar o dar a conocer con respeto?", "dar a conocer con respeto", "No se copia."),
        ex("¿La audiencia de un recurso son las personas que lo verán? Sí o No.", "Sí", "Son quienes lo verán."),
    ],
    task=T(
        "Lee estas obras inventadas para practicar. " + OBRAS + " " + FICHA_PAL + " En tu cuaderno escribe: 1) en qué obra aparece cada palabra y qué significa según la ficha, 2) por qué es importante para la identidad de un pueblo que su lengua aparezca en el arte (en dos oraciones, sin hablar por ningún pueblo), 3) el propósito de un afiche pequeño para dar a conocer una de las obras. Termina con una pregunta para el educador o la educadora tradicional.",
        "Cojín: ko, agua. Canción: antü, sol. Poema: kuyen, luna. Es importante porque muestra que la lengua está viva. Propósito: que las familias conozcan y valoren el poema del curso. Pregunta: ¿cómo aparece la lengua en el arte de su pueblo?",
        ["relaciona cada obra con su palabra y su significado", "explica la importancia de la lengua para la identidad sin hablar por un pueblo", "escribe un propósito de sensibilización", "formula una pregunta para el educador/a tradicional"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["copiar diseños", "hablar en nombre de un pueblo"],
        "Comprueba que el propósito sea sensibilizar y no copiar; si propuso copiar, conversa por qué se pregunta al educador tradicional.",
    ),
    reinforce="Escribe una expresión artística de cada tipo (textil, música, literatura) que conozcas en general, sin copiar ninguna.",
    extend="Explica a una persona de tu casa qué es sensibilizar con un ejemplo de tu curso.",
)

# =================================================================== LS05 clase 2 · examinar autoría y permiso
FICHA_OBRA = "Ficha de obra A (inventada): Obra: cojín «Agua del patio». Autoría: el taller del curso de la Escuela Ejemplo. Palabra en lengua indígena: «ko» (agua), enseñada por la educadora tradicional de la escuela. Permiso para mostrarla: sí, dentro de la escuela. Permiso para copiar el diseño: no."

L(
    LS5, 2,
    materials="Lápiz y hoja. Las fichas están escritas aquí; son inventadas para practicar.",
    use="Aprenderé a examinar la autoría (quién hizo una obra) y el permiso (para qué se puede usar) antes de usar una obra o una palabra. Sirve para respetar el trabajo de otros y la voz de las comunidades.",
    prior=["Sé reconocer la lengua indígena en una obra.", "Sé que no se copian diseños ni canciones de una comunidad."],
    explain=[
        "La autoría es saber quién creó una obra: una persona, una familia, un taller o una comunidad. Quien crea una obra decide cómo se muestra y se usa. Por eso, antes de usarla pregunto: ¿quién la hizo?, ¿quién enseñó las palabras?, ¿para qué hay permiso? Esos datos están en una ficha de obra.",
        "El permiso tiene límites. Puede decir «se puede mostrar en la escuela» pero «no se puede copiar el diseño». Eso quiere decir que puedo mirar la obra y hablar de ella con crédito, pero no puedo dibujarla de nuevo ni usarla en otros lugares. También puede decir «no se indica», y entonces no la uso.",
        "Cuando una obra tiene un diseño, una canción o un poema de una comunidad, las palabras en lengua indígena que contiene no son un adorno: son parte de su identidad. Por eso nunca las quito, las cambio o las uso para algo distinto de lo que dice el permiso. Y en un recurso mío siempre escribo la autoría de cada obra que muestro.",
    ],
    vocab=[("autoría", "quién creó una obra"), ("permiso", "el sí de quien la creó para usarla de cierta manera"), ("crédito", "decir quién hizo o enseñó algo"), ("copiar", "hacer igual lo que otro creó"), ("ficha de obra", "papel con los datos de una obra")],
    worked=[
        W("Leer la ficha de obra", FICHA_OBRA + " ¿Quién creó el cojín?", ["Busco la línea «Autoría».", "Dice: el taller del curso de la Escuela Ejemplo.", "Ellos lo crearon."], "el taller del curso de la Escuela Ejemplo"),
        W("Aplicar el permiso", FICHA_OBRA + " Un niño quiere dibujar el diseño del cojín en su afiche. ¿Puede?", ["Reviso el permiso para copiar el diseño.", "Dice: no.", "No puede; puede mostrar la obra y nombrar su autoría."], "No"),
    ],
    mistakes=[
        M("Mostrar una obra sin decir quién la hizo.", "Se queda sin crédito quien la creó.", "Escribo la autoría junto a la obra."),
        M("Entender que el permiso de mostrar incluye el permiso de copiar.", "Son permisos distintos.", "Leo cada línea del permiso."),
    ],
    R=[
        ex(FICHA_OBRA + " ¿Qué palabra en lengua indígena lleva el cojín?", "ko", "La ficha la nombra."),
        ex(FICHA_OBRA + " ¿Quién enseñó la palabra?", "la educadora tradicional de la escuela", "La ficha lo dice."),
        ex("La autoría de una obra, ¿dice quién la creó o dónde se guarda?", "quién la creó", "Autoría es creación."),
    ],
    C=[
        ex(FICHA_OBRA + " ¿Se puede mostrar el cojín dentro de la escuela? Sí o No.", "Sí", "La ficha da ese permiso."),
        ex(FICHA_OBRA + " ¿Se puede copiar el diseño del cojín? Sí o No.", "No", "La ficha dice que no."),
        ex("Verdadero o falso: si puedo mostrar una obra, puedo también copiar su diseño.", "Falso", "Son permisos distintos."),
    ],
    A=[
        ex("Dos fichas: A trae autoría, fuente de la palabra y permisos. B dice «no se indica» en autoría y permiso. ¿Cuál obra puedes mostrar con respeto?", "A", "La B no tiene datos."),
        ex(FICHA_OBRA + " Escribe el crédito para mostrar el cojín: ¿«Cojín del taller del curso de la Escuela Ejemplo» o «Cojín de internet»?", "«Cojín del taller del curso de la Escuela Ejemplo»", "El crédito nombra a quien lo creó."),
        ex("Una ficha dice: «Permiso: se puede mostrar en la reunión de familias; no se puede publicar». ¿Se puede subir la obra a un sitio abierto de internet? Sí o No.", "No", "No se puede publicar."),
    ],
    Z=[
        ex("Un niño dice: «Si la obra es bonita, no necesito preguntar quién la hizo». ¿Tiene razón? Sí o No.", "No", "La autoría se debe reconocer siempre."),
        ex("Dos afiches: A) muestra el cojín con su autoría y sin copiar su diseño. B) copia el diseño y no dice quién lo hizo. ¿Cuál respeta la ficha?", "A", "La B copia y no da crédito."),
    ],
    D=[
        ex("Ordena para examinar una obra: A) leo el permiso de uso. B) leo la autoría. C) leo quién enseñó la palabra. Escribe las letras en el orden de la ficha A.", "B, C, A", "Autoría, palabra y permiso."),
        arith("Un curso tiene 4 obras y solo 3 tienen la autoría escrita. ¿Cuántas obras no deben mostrarse todavía?", "4-3", "Se restan las obras con autoría de las del curso."),
    ],
    context=[ex("Tu curso encuentra un poema bonito en una hoja sin nombre de autor. ¿Lo muestras en el recurso o pides saber quién lo creó?", "pides saber quién lo creó", "Sin autoría no se muestra.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es la autoría?", "quién creó la obra", "Es el creador de la obra."),
        ex("Si no se indica el permiso, ¿uso la obra o pregunto?", "pregunto", "Sin permiso no se usa."),
        ex("¿Debo escribir el crédito de cada obra que muestro? Sí o No.", "Sí", "El crédito reconoce la autoría."),
    ],
    task=T(
        "Lee esta ficha inventada para practicar. " + FICHA_OBRA + " En tu cuaderno escribe: 1) quién creó la obra, 2) quién enseñó la palabra, 3) qué se puede hacer con la obra y qué no, 4) el crédito que pondrías junto a la obra. Termina con una pregunta para el educador o la educadora tradicional sobre cómo dar crédito a una obra de una comunidad.",
        "Creó la obra el taller del curso. La palabra «ko» la enseñó la educadora tradicional. Se puede mostrar dentro de la escuela; no se puede copiar el diseño. Crédito: «Cojín del taller del curso de la Escuela Ejemplo; palabra enseñada por la educadora tradicional». Pregunta: ¿cómo damos crédito a una obra de la comunidad?",
        ["nombra autoría y fuente de la palabra", "distingue mostrar de copiar", "escribe un crédito completo", "formula una pregunta para el educador/a tradicional"],
        ["cuatro respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["copiar el diseño", "olvidar el crédito"],
        "Comprueba que distingue mostrar de copiar y que el crédito nombra a todos; si propuso copiar el diseño, vuelve a leer con él la línea del permiso.",
    ),
    reinforce="Con la ficha A, señala la línea de la autoría, la de la fuente de la palabra y la del permiso.",
    extend="Escribe una ficha de obra de cinco líneas para un dibujo tuyo, con crédito y permiso.",
)

# =================================================================== LS05 clase 3 · seleccionar palabras contextualizadas
CONTEXTOS = "Contextos de práctica: 1) un afiche que da la bienvenida a una visita. 2) una tarjeta que agradece a la educadora. 3) un rótulo para el rincón de las plantas (agua y tierra). 4) un calendario del mes que nombra la luna."

L(
    LS5, 3,
    materials="Lápiz y hoja. La lista y los contextos están escritos aquí; son inventados para practicar.",
    use="Aprenderé a elegir, de una lista autorizada, la palabra que corresponde a un contexto, explicando por qué sirve y qué significa. Sirve para que cada palabra aparezca donde tiene sentido y no solo como adorno.",
    prior=["Sé examinar la autoría y el permiso de una obra.", "Sé que una palabra se elige por su significado."],
    explain=[
        "Una palabra contextualizada es una palabra que aparece en el lugar donde tiene sentido, con su significado a la vista. Por ejemplo, el saludo «mari mari» tiene sentido en una bienvenida; «chaltumay» tiene sentido en una tarjeta de agradecimiento. Poner «ko» en una bienvenida no tendría sentido porque ko es agua.",
        "Para seleccionar hago tres pasos. Primero leo el contexto y decido qué quiero comunicar: saludar, agradecer, nombrar agua o tierra, nombrar la luna. Segundo busco en la lista autorizada una palabra cuyo significado coincida. Tercero escribo la palabra con su significado entre paréntesis y la razón de mi elección.",
        "Una palabra autorizada no se usa en cualquier lugar. Si ningún contexto necesita una palabra, la dejo fuera. Y si necesito una que no está en la lista, no la invento ni la saco de otro cartel: pido permiso al educador tradicional. Contextualizar es respetar la palabra: que esté donde corresponde y con su sentido claro.",
    ],
    vocab=[("contexto", "lugar o situación donde se usa algo"), ("contextualizada", "puesta donde tiene sentido y con su significado claro"), ("seleccionar", "elegir algunas cosas de un grupo"), ("adorno", "algo que solo decora y no tiene sentido"), ("razón", "motivo de una elección")],
    worked=[
        W("Elegir para un contexto", BANCO + " " + FICHA_SAL + " " + CONTEXTOS + " ¿Qué palabra eliges para el contexto 2?", ["El contexto 2 agradece a la educadora.", "Busco la palabra que significa gracias.", "La ficha de saludos la trae: «chaltumay»."], "chaltumay"),
        W("Dejar una palabra fuera", FICHA_SAL + " " + BANCO + " Un curso tiene la palabra «ruka» pero ningún contexto de su afiche habla de casas. ¿Qué hace?", ["Reviso los contextos.", "Ninguno necesita «ruka».", "La deja fuera."], "la deja fuera"),
    ],
    mistakes=[
        M("Poner una palabra solo porque se ve bonita.", "Una palabra sin sentido en ese lugar es un adorno.", "Elijo la palabra por su significado y el contexto."),
        M("Poner «kuyen» en una bienvenida.", "«Kuyen» es luna, no un saludo.", "Para saludar uso la palabra autorizada que saluda."),
    ],
    R=[
        ex(FICHA_SAL + " ¿Qué palabra de la ficha sirve para saludar?", "mari mari", "La ficha dice que es un saludo."),
        ex(FICHA_SAL + " ¿Qué palabra de la ficha sirve para agradecer?", "chaltumay", "Esa palabra significa gracias."),
        ex("Una palabra contextualizada, ¿está donde tiene sentido o está solo como adorno?", "donde tiene sentido", "Contextualizada significa eso."),
    ],
    C=[
        ex(FICHA_SAL + " " + CONTEXTOS + " ¿Qué palabra eliges para el contexto 1?", "mari mari", "El contexto 1 da la bienvenida."),
        ex("Verdadero o falso: puedo poner «ko» en una bienvenida porque es una palabra bonita.", "Falso", "«Ko» es agua y no tiene sentido ahí."),
        ex(BANCO + " ¿Qué palabra sirve para el contexto 4, el calendario que nombra la luna?", "kuyen", "Es la luna según el banco."),
    ],
    A=[
        ex(BANCO + " " + CONTEXTOS + " Para el contexto 3, el rincón de las plantas que nombra agua y tierra, ¿qué dos palabras eliges?", "ko y mapu", "Ko es agua y mapu es tierra."),
        ex(FICHA_SAL + " " + BANCO + " Une cada contexto con una palabra: 1) bienvenida, 2) agradecimiento, 3) rincón de la luna. Escribe las palabras en orden.", "mari mari, chaltumay, kuyen", "Cada palabra corresponde a su significado."),
        ex(BANCO + " Para un rótulo de la maqueta de una casa mapuche hecha por el curso, ¿qué palabra eliges: «ruka» o «antü»?", "ruka", "«Ruka» es la casa mapuche."),
    ],
    Z=[
        ex("Una niña dice: «Pondré las cinco palabras autorizadas en una sola tarjeta de agradecimiento». ¿Es buena idea si solo una sirve a ese contexto? Sí o No.", "No", "Las demás serían adornos."),
        ex("Dos formas de elegir: A) elijo la palabra por su significado y el contexto. B) elijo la que se ve más misteriosa. ¿Cuál es respetuosa?", "A", "La B convierte la palabra en adorno."),
    ],
    D=[
        ex(FICHA_SAL + " " + BANCO + " Un curso hace una tarjeta de agradecimiento con un dibujo del sol. ¿Qué dos palabras de las fichas pueden ir con sentido: chaltumay y antü, o mari mari y kuyen?", "chaltumay y antü", "Agradecer y nombrar el sol."),
        ex("Ordena los pasos para seleccionar: A) escribo la razón de mi elección. B) decido qué quiero comunicar. C) busco la palabra cuyo significado coincide. Escribe las letras.", "B, C, A", "Decido, busco y explico."),
    ],
    context=[ex("Preparan un afiche para recibir a una visita y alguien propone poner «kuyen» porque suena lindo. ¿Respondes «Mejor «mari mari», que saluda» o «Sí, ponlo»?", "«Mejor «mari mari», que saluda»", "La palabra se elige por su significado.")],
    selfcheck=[
        ex("¿Cómo elijo una palabra: por su significado o por cómo suena?", "por su significado", "El significado decide."),
        ex("Si ningún contexto necesita una palabra, ¿la dejo fuera?", "Sí", "No se usa como adorno."),
        ex("Si necesito una palabra que no está en la lista, ¿la invento o pido permiso?", "pido permiso", "Se pregunta al educador tradicional."),
    ],
    task=T(
        "Lee los contextos y las fichas inventados para practicar. " + CONTEXTOS + " " + FICHA_SAL + " " + BANCO + " En tu cuaderno haz una tabla de tres columnas: contexto, palabra elegida y razón. Completa los cuatro contextos. Después escribe una palabra de las fichas que dejarías fuera de todo y por qué. Termina con una pregunta para el educador o la educadora tradicional.",
        "1 bienvenida: mari mari, porque saluda. 2 agradecimiento: chaltumay, porque significa gracias. 3 rincón de plantas: ko y mapu, agua y tierra. 4 calendario: kuyen, luna. Dejaría fuera ruka porque ningún contexto habla de casas. Pregunta: ¿qué palabra puede ir en un rincón de las plantas?",
        ["completa los cuatro contextos", "elige por significado", "explica por qué deja una palabra fuera", "formula una pregunta para el educador/a tradicional"],
        ["tabla de tres columnas", "pregunta escrita o dicha en voz alta"],
        ["elegir por cómo suena", "usar palabras fuera de las fichas"],
        "Revisa que cada elección tenga razón por significado; si usó una palabra fuera de las fichas, pide cambiarla por una pregunta.",
    ),
    reinforce="Escribe un contexto de tu escuela para cada palabra: mari mari, chaltumay, ko, antü y kuyen.",
    extend="Explica por qué una palabra no debe usarse como adorno.",
)

# =================================================================== LS05 clase 4 · crear sin apropiarse
CANCION = "Canción de práctica «Canción del río» (inventada, original de este cuaderno): «Corre el ko, corre claro; brilla el antü sobre el agua.»"

L(
    LS5, 4,
    materials="Lápiz, hoja y colores. Los textos están escritos aquí; son originales de este cuaderno. Si usas un dispositivo, hazlo con una persona adulta.",
    use="Aprenderé a crear una pieza propia (un poema, un dibujo o una canción corta) que incluya palabras autorizadas sin apropiarme de obras, voces ni diseños de otros. Sirve para crear con libertad y respeto.",
    prior=["Sé examinar autoría y permiso.", "Sé seleccionar palabras para un contexto."],
    explain=[
        "Crear sin apropiarme es hacer algo nuevo, mío, que dialoga con una cultura sin tomar lo de otros. Puedo inspirarme en la naturaleza, en mis sentimientos o en lo que aprendí en clases. No copio un poema, una canción o un diseño de otra persona o comunidad, ni cambio algunas palabras para hacerlo pasar por mío.",
        "Mi creación puede incluir palabras autorizadas, como «ko» o «antü», dentro de versos o frases en castellano. Por ejemplo, la canción de práctica dice: «Corre el ko, corre claro; brilla el antü sobre el agua.» La escribí yo, es original y las palabras vienen del banco. Eso es crear sin apropiarse.",
        "También cuido tres cosas. Primero, no uso la voz ni la imagen de nadie sin permiso. Segundo, no invento ritos ni significados sagrados para mi obra. Tercero, escribo el crédito: «Creado por el curso, con palabras enseñadas por la educadora tradicional». Si me inspiré en algo de una comunidad, lo digo y pregunto si puedo hacerlo.",
    ],
    vocab=[("crear", "hacer algo nuevo y propio"), ("inspirarse", "tomar una idea de algo y hacer algo distinto"), ("apropiarse", "tomar como propio lo de otros"), ("original", "hecho por mí, no copiado"), ("crédito", "decir quién creó o enseñó algo")],
    worked=[
        W("Reconocer una creación propia", CANCION + " ¿Qué palabras del banco usa la canción?", ["Leo la canción.", "Aparecen «ko» y «antü».", "Las dos están en el banco."], "ko y antü"),
        W("Distinguir crear y apropiarse", "Un niño cambia dos palabras de un poema que leyó y dice que lo escribió él. ¿Está creando o apropiándose?", ["Partió de un poema de otra persona.", "Solo cambió dos palabras.", "Lo presenta como suyo."], "se apropia"),
    ],
    mistakes=[
        M("Cambiar algunas palabras de una canción de otro y presentarla como mía.", "Sigue siendo la obra de otra persona.", "Escribo mis propios versos y cito la fuente de mi inspiración."),
        M("Inventar un significado sagrado para una palabra en mi obra.", "Estaría inventando un rito o un significado que no me corresponde.", "Uso la palabra con el significado de la ficha."),
    ],
    R=[
        ex(CANCION + " ¿Qué dos palabras del banco aparecen?", "ko y antü", "Se leen en la canción."),
        ex("Una obra original, ¿la hice yo o la copié?", "la hice yo", "Original es propia."),
        ex("Inspirarse, ¿es tomar una idea y hacer algo distinto o copiar tal cual?", "tomar una idea y hacer algo distinto", "No es copiar."),
    ],
    C=[
        ex("Verdadero o falso: cambiar dos palabras de una canción ajena la convierte en mía.", "Falso", "Sigue siendo de otra persona."),
        ex(CANCION + " ¿La canción de práctica es una canción real de una comunidad? Sí o No.", "No", "Es original de este cuaderno."),
        ex("Un crédito dice: «Creado por el curso, con palabras enseñadas por la educadora tradicional». ¿Nombra a quién creó y a quién enseñó? Sí o No.", "Sí", "Menciona al curso y a la educadora."),
    ],
    A=[
        ex("Tres acciones: 1) escribir mis versos con palabras del banco. 2) copiar los versos de un cantor y firmarlos. 3) usar la voz de una visita sin preguntar. ¿Cuál es crear sin apropiarse? Escribe el número.", "1", "Es la única con versos propios."),
        ex(CANCION + " Si cambias «ko» por «kuyen», ¿cambia lo que dice la canción: del agua a la luna? Sí o No.", "Sí", "«Ko» es agua y «kuyen» es luna."),
        ex(BANCO + " Completa un verso original: «Brilla la luna (____) en la noche». Elige entre kuyen y ko.", "kuyen", "La luna brilla en la noche."),
    ],
    Z=[
        ex("Una niña dice: «Si la canción es bonita y de una comunidad, puedo usarla en mi obra sin decir de quién es». ¿Tiene razón? Sí o No.", "No", "Debe pedir permiso y dar crédito."),
        ex("Dos formas de inspirarme: A) miro el agua del río y escribo versos propios. B) copio el diseño de un textil de un libro. ¿Cuál no es apropiarse?", "A", "La B copia un diseño ajeno."),
    ],
    D=[
        ex("Ordena para crear sin apropiarse: A) escribo el crédito. B) escribo mis propios versos con palabras del banco. C) me inspiro en lo que observo. Escribe las letras.", "C, B, A", "Observo, creo y doy crédito."),
        arith("Un poema de práctica tiene 4 versos y solo 3 llevan una palabra del banco. ¿Cuántos versos no la llevan?", "4-3", "Se restan los versos con palabra del total."),
    ],
    context=[ex("Para el día de la lengua quieres mostrar una canción con la voz de una visita que grabó una compañera sin avisarle. ¿Pides permiso a la visita o la usas igual?", "pides permiso a la visita", "La voz de una persona requiere su permiso.")],
    selfcheck=[
        ex("¿Qué es una obra original?", "una obra hecha por mí", "Original es propia."),
        ex("¿Puedo usar versos de una comunidad como míos? Sí o No.", "No", "Sería apropiarme de otra obra."),
        ex("¿Qué escribo al final de mi creación para reconocer a quienes ayudaron?", "el crédito", "Reconoce a la autora y a la fuente."),
    ],
    task=T(
        "Crea una pieza original de dos versos (o un dibujo con un rótulo) en tu cuaderno que use una o dos palabras de este banco inventado. " + BANCO + " Inspírate en lo que observas, como el agua o la luna. No copies versos ni diseños de otras personas. Debajo escribe el crédito: «Creado por [tu nombre de pila]; palabras enseñadas por la educadora tradicional». Termina con una pregunta para el educador o la educadora tradicional.",
        "Brilla la luna (kuyen) en la noche, y el agua (ko) la guarda. Crédito: creado por Ana; palabras enseñadas por la educadora tradicional. Pregunta: ¿cómo se cuida una palabra que se usa en el arte?",
        ["crea versos o dibujo originales", "usa solo palabras del banco", "escribe el crédito", "formula una pregunta para el educador/a tradicional"],
        ["pieza original y crédito escritos", "pregunta escrita o dicha en voz alta"],
        ["copiar versos o diseños", "olvidar el crédito"],
        "Comprueba que sea original y use solo el banco; si copió algo, conversa por qué se pide inspiración y no copia.",
    ),
    reinforce="Escribe un verso nuevo con la palabra «antü» y revisa que no se parezca a ningún verso que hayas leído.",
    extend="Haz un dibujo propio de un río con un rótulo «ko (agua)» y el crédito del curso.",
)

# =================================================================== LS05 clase 5 · revisar atribución y audiencia
FICHA_REC = "Ficha del recurso (inventada): Recurso: afiche «Palabras del agua». Creado por: el curso. Palabras enseñadas por: la educadora tradicional de la Escuela Ejemplo. Audiencia autorizada: las familias en la reunión de la sala. Dónde se guarda: en la sala."

L(
    LS5, 5,
    materials="Lápiz y hoja. La ficha y los casos están escritos aquí; son inventados para practicar.",
    use="Aprenderé a revisar la atribución (a quién se da crédito) y la audiencia (quiénes lo verán) de un recurso antes de mostrarlo. Sirve para cuidar a las personas que enseñaron y a quienes lo verán.",
    prior=["Sé crear sin apropiarme.", "Sé examinar autoría y permiso."],
    explain=[
        "Atribuir es escribir quién creó el recurso y quién enseñó las palabras. Revisar la atribución es comprobar que están todos los nombres que corresponden y que dicen lo correcto. Un recurso bien atribuido tiene al menos dos datos: quién lo creó y quién enseñó las palabras de la lengua.",
        "La audiencia son las personas que verán el recurso. La ficha dice qué audiencia está autorizada. Si dice «las familias en la reunión de la sala», no lo muestro a otros cursos ni lo subo a internet. Si queda alguna duda sobre quiénes pueden verlo, pregunto al educador tradicional antes de mostrarlo.",
        "Antes de mostrar hago una revisión de cinco puntos: atribución completa, palabras iguales a la ficha, sin datos personales, audiencia autorizada y lugar de guardado. También pienso si el recurso sensibiliza, es decir, si ayuda a otros a conocer y valorar la lengua con respeto. Si algo falla, lo corrijo antes de mostrarlo.",
    ],
    vocab=[("atribución", "escribir a quién se da crédito"), ("audiencia", "personas que verán un recurso"), ("autorizada", "con permiso para estar o ver"), ("revisión", "comprobación antes de mostrar"), ("sensibilizar", "ayudar a otros a conocer y valorar algo")],
    worked=[
        W("Revisar la atribución", FICHA_REC + " ¿Quién enseñó las palabras?", ["Busco la línea «Palabras enseñadas por».", "Dice: la educadora tradicional de la Escuela Ejemplo.", "Ella las enseñó."], "la educadora tradicional de la Escuela Ejemplo"),
        W("Respetar la audiencia", FICHA_REC + " Un niño quiere mostrar el afiche a otro curso. ¿Puede?", ["Reviso la audiencia autorizada.", "Solo las familias en la reunión de la sala.", "No puede mostrarlo a otro curso sin permiso."], "No"),
    ],
    mistakes=[
        M("Mostrar el recurso a una audiencia mayor porque «es solo un rato».", "El permiso señala quiénes pueden verlo.", "Pido permiso para ampliar la audiencia."),
        M("Poner solo «Creado por el curso» sin nombrar a quien enseñó las palabras.", "Falta el crédito de la fuente de la lengua.", "Agrego «palabras enseñadas por la educadora tradicional»."),
    ],
    R=[
        ex(FICHA_REC + " ¿Quién creó el afiche?", "el curso", "La ficha lo dice."),
        ex(FICHA_REC + " ¿Dónde se guarda el afiche?", "en la sala", "La ficha lo dice."),
        ex("La audiencia de un recurso, ¿son las personas que lo verán o el lugar donde se guarda?", "las personas que lo verán", "Audiencia es quienes ven."),
    ],
    C=[
        ex(FICHA_REC + " ¿La audiencia autorizada incluye a todo el colegio? Sí o No.", "No", "Son solo las familias en la reunión de la sala."),
        ex("Verdadero o falso: puedo subir un recurso a un sitio abierto si la ficha dice «audiencia: familias en la reunión».", "Falso", "El permiso limita la audiencia."),
        ex("Una atribución completa nombra a quien creó el recurso y a quien enseñó las palabras. ¿Cuántos datos son?", "2", "Son dos datos."),
    ],
    A=[
        ex("Cinco puntos de revisión: atribución, palabras iguales a la ficha, sin datos personales, audiencia, guardado. Un recurso cumple tres. ¿Cuántos puntos faltan por cumplir?", "2", "5 − 3 = 2."),
        ex("Atribución A: «Creado por el curso». Atribución B: «Creado por el curso; palabras enseñadas por la educadora tradicional». ¿Cuál está completa?", "B", "Nombra a quien creó y a quien enseñó."),
        ex(FICHA_REC + " Un familiar quiere compartir una foto del afiche en una red social. ¿Qué responde mejor el curso: A) «Mejor no; la audiencia es la reunión de la sala». B) «Claro»?", "A", "Se respeta la audiencia autorizada."),
    ],
    Z=[
        ex("Una niña dice: «Si el afiche sensibiliza, no importa quiénes lo vean». ¿Tiene razón? Sí o No.", "No", "La audiencia autorizada se respeta siempre."),
        ex("Dos revisiones: A) solo reviso que se vea bonito. B) reviso atribución, palabras, datos personales, audiencia y guardado. ¿Cuál es completa?", "B", "La A deja puntos sin revisar."),
    ],
    D=[
        ex("Ordena la revisión antes de mostrar: A) reviso la audiencia autorizada. B) reviso la atribución. C) reviso que las palabras sean iguales a la ficha. Escribe las letras en el orden de la ficha del recurso (creador y fuente, palabras, audiencia).", "B, C, A", "Atribución, palabras y audiencia."),
        arith("Se esperaban 20 personas de las familias en la reunión, pero llegaron 26. ¿Cuántas personas más de las previstas llegaron?", "26-20", "Se restan las previstas de las que llegaron."),
    ],
    context=[ex("Terminas el afiche y alguien pregunta si pueden colgarlo en el pasillo de toda la escuela. La ficha dice que es solo para las familias en la reunión. ¿Respondes «Preguntemos a la educadora si se puede ampliar» o «Sí, cuélguenlo»?", "«Preguntemos a la educadora si se puede ampliar»", "La audiencia la define el permiso.")],
    selfcheck=[
        ex("¿Qué es atribuir?", "escribir a quién se da crédito", "Es dar crédito."),
        ex("¿Muestro el recurso a una audiencia mayor sin preguntar? Sí o No.", "No", "Se pide permiso."),
        ex("¿Cuántos puntos se revisan antes de mostrar: atribución, palabras, datos, audiencia y guardado?", "5", "Se cuentan cinco puntos."),
    ],
    task=T(
        "Revisa este recurso inventado para practicar. " + FICHA_REC + " Imagina que el curso quiere agregar al afiche las palabras «ko» y «antü», con su significado, y un dibujo propio. " + BANCO + " En tu cuaderno haz una lista de revisión con cinco puntos (atribución, palabras iguales a la ficha, sin datos personales, audiencia, guardado) y escribe cómo se cumple cada uno. Termina con una pregunta para el educador o la educadora tradicional.",
        "Atribución: creado por el curso; palabras enseñadas por la educadora tradicional. Palabras: ko (agua), antü (sol), iguales al banco. Sin datos personales: solo «el curso». Audiencia: familias en la reunión. Guardado: en la sala. Pregunta: ¿podemos mostrar el afiche en otra reunión?",
        ["completa los cinco puntos", "nombra a quien creó y a quien enseñó", "respeta la audiencia autorizada", "formula una pregunta para el educador/a tradicional"],
        ["lista de revisión de cinco puntos", "pregunta escrita o dicha en voz alta"],
        ["ampliar la audiencia", "olvidar a la fuente de las palabras"],
        "Comprueba los cinco puntos; si amplió la audiencia, repasen qué dice la ficha y por qué se pregunta antes.",
    ),
    reinforce="Escribe en una tarjeta los cinco puntos de revisión antes de mostrar un recurso.",
    extend="Explica a una persona de tu casa por qué es importante nombrar a quien enseñó las palabras.",
)

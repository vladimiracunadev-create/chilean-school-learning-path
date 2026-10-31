"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 10 (textos no literarios que contextualizan) y OA 12 (escritura creativa).

Todos los pasajes literarios, entrevistas, tablas, borradores y comentarios son originales e inventados («de ejemplo»);
cada ejercicio trae escritos los textos y datos que necesita.
Nota: los títulos de las clases del repositorio son específicos del eje; este cuaderno los sigue.
"""
from __future__ import annotations

import re

from student_lessons import arith, ex, register

def E(q, a, why, calc=None):
    """Ejercicio cerrado; en las preguntas de tres opciones (a), (b), (c) reparte la correcta entre las tres posiciones."""
    import zlib
    m = list(re.finditer(r"\(([abc])\) ", q))
    if len(m) == 3 and [x.group(1) for x in m] == ["a", "b", "c"] and a.strip() in ("(a)", "(b)", "(c)"):
        stem = q[:m[0].start()]
        raw = [q[m[0].end():m[1].start()], q[m[1].end():m[2].start()], q[m[2].end():]]
        tail = ""
        last = raw[2].rstrip()
        if last.endswith(("?", ".")) and not (last.startswith(("¿", "¡")) and last.endswith("?") and last.count("?") == last.count("¿")):
            tail = last[-1]
            last = last[:-1]
        raw = [raw[0].strip(), raw[1].strip(), last.strip()]
        opts = []
        for o in raw:
            if o.endswith(".") or (o.endswith("?") and not o.startswith("¿")):
                o = o[:-1]
            opts.append(o.strip())
        if all(opts):
            correct = "abc".index(a.strip()[1])
            want = zlib.crc32((stem + "|".join(sorted(opts))).encode("utf-8")) % 3
            order = list(range(3))
            order.remove(correct)
            order.insert(want, correct)
            new = [opts[i] for i in order]
            mapping = {"abc"[old]: "abc"[pos] for pos, old in enumerate(order)}
            q = stem + " ".join(f"({'abc'[i]}) {t}" for i, t in enumerate(new)) + tail
            a = f"({'abc'[want]})"
            why = re.sub(r"\(([abc])\)", lambda x: f"({mapping[x.group(1)]})", why)
    return ex(q, a, why, calc)


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


OA10 = "LE07 OA 10"
OA12 = "LE07 OA 12"

PAS = "«Cada jueves, Ema empujaba la puerta de la biblioteca de la junta de vecinos y buscaba el estante de los libros sin tapa. —No todos pueden comprar libros —decía doña Rita—, pero todos pueden pedirlos prestados.»"
FA = "Fuente A (entrevista de ejemplo, 14 de marzo de 2024, a Rita Campos, voluntaria): «Atendemos martes y jueves de 16:00 a 19:00. Los libros llegan por donaciones y el préstamo es gratuito por 15 días.»"
FB = "Fuente B (tabla de ejemplo, préstamos por año): 2021, 310; 2022, 420; 2023, 505; 2024, 560."
FC = "Fuente C (entrada sin autor ni fecha): «Las bibliotecas comunitarias son lugares donde se presta de todo y siempre son mejores que las públicas.»"

# ================================================================== OA10 · clase 1
L(OA10, 1,
  "Este cuaderno y un lápiz. El pasaje literario y las fuentes están escritos en los ejercicios.",
  "Aprenderé a detectar qué necesito saber para entender mejor una obra literaria y a formular preguntas de contexto.",
  ["Sé leer un fragmento literario y explicar de qué trata.", "Sé que hay textos no literarios, como artículos, entrevistas y tablas."],
  ["Contextualizar una obra es reunir información de fuera de ella (el lugar, la época, las costumbres, el oficio, el autor, ciertos conceptos) para comprender mejor lo que dice. Un texto literario a veces da por sabido algo que no todos conocemos. Por ejemplo, si un cuento transcurre en una caleta de pescadores y no sabemos qué es una caleta, entenderemos solo en parte.",
   "El primer paso es leer el pasaje y marcar lo que no entendemos o lo que el texto supone que sabemos. El segundo paso es convertir cada duda en una pregunta de contexto: ¿dónde ocurre?, ¿cuándo?, ¿qué es esto?, ¿cómo funciona este lugar? Una pregunta de contexto se responde con información externa. En cambio, una pregunta de interpretación (por ejemplo, ¿por qué Ema se emociona?) se responde con el propio texto.",
   "El tercer paso es elegir palabras clave y el tipo de texto no literario que puede ayudar: un artículo informativo para explicar un concepto, una entrevista para saber cómo funciona algo, una tabla para ver cifras, un mapa para ubicar un lugar. Contextualizar no reemplaza la lectura: complementa lo que ya entendimos del texto literario."],
  [("contextualizar", "reunir información externa para comprender mejor una obra"), ("antecedente", "información previa que ayuda a entender algo"), ("pregunta de contexto", "pregunta que se responde con información externa a la obra"), ("palabra clave", "palabra con la que busco información sobre un tema"), ("texto no literario", "texto informativo, como un artículo, una entrevista o una tabla")],
  [("Formular preguntas de contexto", f"Pasaje de ejemplo: {PAS} Si no sabes cómo funciona una biblioteca de junta de vecinos, ¿qué preguntas de contexto formulas?",
    ["Marco lo que el texto supone que sé: «biblioteca de la junta de vecinos» y «pedirlos prestados».", "Convierto la duda en preguntas: ¿quién atiende? ¿cuánto tiempo se prestan los libros?", "Elijo palabras clave: biblioteca comunitaria, préstamo, voluntarios."], "¿Quién atiende y cómo funciona el préstamo en una biblioteca comunitaria? Palabras clave: biblioteca comunitaria, préstamo"),
   ("Contexto o interpretación", "En el mismo pasaje: (1) ¿por qué doña Rita dice que todos pueden pedir libros prestados? (2) ¿qué horario suele tener una biblioteca comunitaria? Clasifica cada pregunta.",
    ["La 1 pide una razón que se discute con el propio texto: es de interpretación.", "La 2 pide un dato externo que no está en el pasaje: es de contexto."], "La 1 es de interpretación; la 2 es de contexto")],
  [("Buscar información sin saber qué preguntas se tienen.", "Se reúnen datos que no ayudan a entender el pasaje.", "Primero formula preguntas de contexto y después busca."),
   ("Pensar que contextualizar es resumir la obra.", "El contexto agrega información externa, no repite lo que dice el texto.", "Pregúntate qué necesito saber que el texto no explica.")],
  ([E("¿Qué significa contextualizar una obra?", "Reunir información externa para comprenderla mejor", "El contexto viene de fuera de la obra y aclara su sentido."),
    E(f"Pasaje: {PAS} ¿Qué lugar aparece: una biblioteca o un estadio?", "Una biblioteca", "El texto dice «biblioteca de la junta de vecinos»."),
    E("«¿Cuántos días suele durar un préstamo en una biblioteca comunitaria?» ¿Es pregunta de contexto o de interpretación?", "De contexto", "Pide un dato externo que no está en la obra.")],
   [E(f"Pasaje: {PAS} ¿Qué frase supone que el lector sabe cómo funciona un préstamo?", "«Pedirlos prestados»", "Da por sabido el funcionamiento de pedir libros sin comprarlos."),
    E("¿Qué tipo de texto no literario te ayudaría a saber cómo funciona una biblioteca comunitaria: una entrevista a quien la atiende o un poema sobre libros?", "Una entrevista a quien la atiende", "Entrega información directa de quien conoce el funcionamiento."),
    E("«¿Por qué Ema se alegra al ver los estantes?» ¿Se responde con información externa o con el texto literario?", "Con el texto literario", "Es una pregunta de interpretación.")],
   [E("Un cuento transcurre en una caleta de pescadores y menciona «salir con la marea». ¿Cuál es una buena palabra clave para buscar contexto? (a) pesca artesanal (b) cumpleaños (c) videojuegos", "(a)", "Se relaciona con el oficio y el lugar del cuento."),
    E("Un cuento dice: «La campana de la escuela rural sonó dos veces y los niños cruzaron el cerro». ¿Cuál es una pregunta de contexto? (a) ¿Cómo son las escuelas rurales y por qué algunos niños cruzan cerros para llegar? (b) ¿Qué sentirán los niños al oír la campana? (c) ¿Cuántas veces sonó la campana?", "(a)", "Pide información externa; (c) se responde en el texto y (b) es interpretación."),
    E("Ordena los pasos de contextualizar: a) elegir palabras clave y un texto no literario, b) marcar lo que no entiendo, c) formular preguntas de contexto. Escribe las letras en orden.", "b, c, a", "Primero se detectan las dudas, luego se preguntan y después se busca.")],
   [E("Ignacio dice: «Para entender la obra solo necesito saber más de la obra, no de afuera». ¿Es correcto?", "No; el contexto aporta información externa que aclara el texto", "Contextualizar significa buscar fuera de la obra."),
    E("¿Por qué conviene formular preguntas antes de buscar información?", "Para saber qué datos sirven y no perderse", "Las preguntas orientan la búsqueda.")],
   [E("Pasaje de ejemplo: «El minero apagó su lámpara cuando sonó el silbato de las seis». ¿Cuál de estas dos preguntas es de contexto: «¿cómo es el trabajo en una mina?» o «¿qué siente el minero?»?", "«¿Cómo es el trabajo en una mina?»", "La primera pide información externa; la segunda se interpreta desde el texto."),
    arith("Tienes 3 dudas de contexto y para cada una anotas 2 palabras clave. ¿Cuántas palabras clave anotas en total?", "3*2", "Se multiplica el número de dudas por las palabras de cada una.", " palabras clave")]),
  [E(f"Vas a leer un cuento que empieza así: {PAS} Quieres entender mejor el lugar. Escribe una palabra clave para buscar.", "Biblioteca comunitaria", "Resume el tipo de lugar y sirve para buscar su funcionamiento.")],
  [E("¿Una pregunta de contexto se responde con información externa o interna?", "Externa", "Viene de fuera de la obra."),
   E("Nombra un tipo de texto no literario que sirva para contextualizar.", "Un artículo, una entrevista, una tabla o un mapa", "Son textos informativos."),
   E("¿Qué se hace primero: buscar o formular preguntas?", "Formular preguntas", "Las preguntas dirigen la búsqueda.")],
  ("Lee este pasaje de ejemplo: «Mateo guardó la red, saludó al viejo bote y esperó a que el pregonero anunciara el precio del día en la caleta». Marca tres palabras o expresiones que necesites aclarar, formula una pregunta de contexto para cada una y escribe dos palabras clave para buscar.",
   "Aclaro: «red», «caleta», «precio del día». Preguntas: ¿cómo se usa una red de pesca?, ¿qué es una caleta y quién trabaja allí?, ¿cómo se fija el precio del pescado? Palabras clave: pesca artesanal, caleta.",
   ["marca tres expresiones del pasaje", "formula tres preguntas de contexto", "propone dos palabras clave"], ["lista escrita en el cuaderno"],
   ["formular preguntas de interpretación en vez de contexto", "marcar expresiones que sí se entienden"], "Comparte tus preguntas con alguien y pídele que diga cuál lo ayudaría más a entender."),
  "Elige un cuento corto de tu casa y anota dos cosas que el texto supone que sabes.",
  "Escribe un pasaje de tres líneas ambientado en un lugar que conozcas y anota qué contexto necesitaría un lector de otro país.")

# ================================================================== OA10 · clase 2
L(OA10, 2,
  "Este cuaderno y un lápiz. Las tres fuentes están escritas en los ejercicios.",
  "Aprenderé a elegir, entre varias fuentes, la información pertinente para responder una pregunta de contexto y a registrarla.",
  ["Sé formular preguntas de contexto.", "Sé qué es una palabra clave."],
  ["No toda la información sobre un tema sirve para nuestra pregunta. La información pertinente es la que responde directamente la pregunta de contexto que formulamos. Si preguntamos por el horario de una biblioteca comunitaria, un dato sobre el precio de los libros nuevos no es pertinente, aunque hable de libros.",
   "También conviene evaluar la fuente: ¿quién la produjo?, ¿cuándo?, ¿sabe del tema? Una entrevista fechada a una voluntaria es una fuente con autor y fecha. Una tabla de cifras entrega datos numéricos. Una entrada sin autor ni fecha pide más cuidado, porque no sabemos quién lo dice ni si está actualizada, y puede mezclar hechos con opiniones.",
   "Para guardar lo encontrado usamos una ficha con cinco partes: pregunta, palabras clave, hallazgo (la información que sirve), categoría (si es dato, definición o testimonio) y referencia (de dónde sale: tipo de texto, autor y fecha). Con esta ficha podremos citar con orden y volver a revisar."],
  [("información pertinente", "la que responde directamente a la pregunta"), ("fuente", "texto o persona de donde sale la información"), ("hallazgo", "información útil encontrada en una fuente"), ("referencia", "datos que indican de dónde viene una información"), ("ficha", "registro ordenado de lo encontrado")],
  [("Seleccionar lo pertinente", f"Pregunta: ¿cuánto tiempo se puede tener un libro prestado? {FA} ¿Qué parte es pertinente?",
    ["La pregunta pide la duración del préstamo.", "La fuente A dice: «el préstamo es gratuito por 15 días».", "El horario y las donaciones no responden esa pregunta."], "El préstamo es por 15 días"),
   ("Llenar una ficha", f"Con la fuente A: {FA} Completa una ficha de la pregunta ¿cuándo atienden?",
    ["Pregunta: ¿cuándo atiende la biblioteca?", "Hallazgo: martes y jueves de 16:00 a 19:00. Categoría: dato de horario.", "Referencia: entrevista a Rita Campos, voluntaria, 14 de marzo de 2024."], "Hallazgo: martes y jueves de 16:00 a 19:00; referencia: entrevista a Rita Campos, 14/3/2024")],
  [("Copiar toda la fuente en la ficha.", "Se mezclan datos que no responden la pregunta.", "Anota solo el hallazgo pertinente."),
   ("Anotar un dato sin su referencia.", "Después no sabrás de dónde viene ni si es confiable.", "Escribe tipo de texto, autor y fecha.")],
  ([E(f"Pregunta: ¿cuántos días dura el préstamo? {FA} ¿Cuál es el hallazgo pertinente?", "15 días", "La fuente lo dice en la parte del préstamo."),
    E("¿Qué parte de la ficha dice de dónde viene un dato?", "La referencia", "Indica la fuente, el autor y la fecha."),
    E("Una información que no responde a tu pregunta, ¿es pertinente?", "No", "Pertinente es lo que responde directamente.")],
   [E(f"{FB} ¿Qué pregunta se puede responder con esta fuente: cuántos préstamos hubo en 2022 o qué horario tiene la biblioteca?", "Cuántos préstamos hubo en 2022", "La tabla solo entrega préstamos por año."),
    E(f"{FC} ¿Por qué esta fuente exige más cuidado que la entrevista?", "Porque no tiene autor ni fecha y mezcla opinión", "No se sabe quién lo dice ni si es actual."),
    E("¿Una entrevista a una voluntaria con fecha es una fuente con autor o sin autor?", "Con autor", "Sabemos quién habla y cuándo.")],
   [arith("Según la fuente B de ejemplo (2021: 310 préstamos y 2022: 420), ¿cuántos préstamos más hubo en 2022 que en 2021?", "420-310", "Se resta el valor inicial al final.", " préstamos"),
    E(f"Pregunta: ¿por qué se llama biblioteca comunitaria? Lee: {FA} ¿La fuente A responde directamente esa pregunta?", "No; habla de horario y préstamos, no del nombre", "No es pertinente para el origen del nombre."),
    E(f"Con {FB} completa el hallazgo para la pregunta ¿cuántos préstamos hubo en 2024? Escribe el dato.", "560 préstamos", "Es la cifra de 2024 de la tabla.")],
   [E(f"{FC} Un compañero anota «Las bibliotecas comunitarias siempre son mejores que las públicas» como hallazgo. ¿Es buena decisión?", "No; es una opinión sin fuente verificable", "Una ficha necesita hechos con referencia."),
    E(f"Pregunta: ¿cuántos préstamos hubo en 2023? {FB} Un estudiante anota «aumentan cada año» como hallazgo. ¿Responde la pregunta?", "No; la cifra pedida es 505", "Responde otra cosa; la pregunta pide un número.")],
   [arith("Con la fuente B de ejemplo (2023: 505 préstamos y 2024: 560), ¿cuántos préstamos más hubo en 2024 que en 2023?", "560-505", "Se resta la cifra anterior a la más reciente.", " préstamos"),
    E(f"Tienes tres fuentes: {FA} {FB} {FC} Para saber el horario de atención, ¿cuál usarías y por qué?", "La fuente A, porque es una entrevista con autor y fecha que da el horario", "Es la única que informa horario con una fuente identificable.")]),
  [E(f"Tu curso quiere organizar un préstamo de libros y necesita saber cuánto tiempo se presta cada uno. {FA} ¿Qué dato y qué referencia anotas?", "Dato: 15 días; referencia: entrevista a Rita Campos, 14 de marzo de 2024", "El dato responde la pregunta y la referencia dice de dónde sale.")],
  [E("Nombra una parte de la ficha.", "Pregunta, palabras clave, hallazgo, categoría o referencia", "Son las cinco partes de la ficha de la clase."),
   E("¿Qué es un hallazgo?", "La información útil que se encuentra en una fuente", "Es lo que responde la pregunta."),
   E("¿Qué debe tener una fuente confiable: autor y fecha o un título largo?", "Autor y fecha", "Permiten saber quién habla y si está actualizada.")],
  ("Con las fuentes de esta clase, llena una ficha para la pregunta: ¿se puede decir que en esta biblioteca el uso aumentó cada año? Usa la tabla: " + FB + " Anota pregunta, hallazgo, categoría y referencia, e indica si usarías la entrada sin autor.",
   "Pregunta: ¿aumentó el uso cada año? Hallazgo: 310, 420, 505 y 560 préstamos; sube en cada año. Categoría: dato numérico. Referencia: tabla de ejemplo de préstamos por año. No usaría la entrada sin autor porque no tiene fuente.",
   ["formula la pregunta", "usa solo datos de la tabla", "completa la referencia"], ["ficha de cinco partes"],
   ["no escribir referencia", "usar la entrada sin autor como evidencia"], "Revisa tu ficha con alguien y pregúntale si podría encontrar la fuente solo con tu referencia."),
  "Escribe una pregunta de contexto y una fuente que podría responderla.",
  "Inventa una ficha de cinco partes para otra pregunta sobre bibliotecas.")

# ================================================================== OA10 · clase 3
L(OA10, 3,
  "Este cuaderno y un lápiz. El pasaje y las fuentes están escritos en los ejercicios.",
  "Aprenderé a relacionar la información de textos no literarios con un pasaje literario para comprender mejor sus detalles.",
  ["Sé seleccionar información pertinente.", "Sé llenar una ficha de lectura."],
  ["Relacionar significa conectar un dato del texto no literario con una frase del pasaje literario y explicar cómo cambia o profundiza nuestra comprensión. Por ejemplo, si el pasaje dice que doña Rita «presta libros» y la entrevista aclara que el préstamo es gratuito por 15 días, entendemos mejor por qué ella dice que «todos pueden pedirlos prestados».",
   "Una buena relación tiene tres partes: la cita del pasaje, el dato del texto no literario y la explicación que une ambos. La explicación responde: ¿qué entiendo ahora que antes no entendía? Es importante que el dato sea pertinente y que no usemos el contexto para inventar sucesos que la obra no cuenta.",
   "También sirve para ver detalles nuevos: palabras que parecían simples, lugares, costumbres o motivos de los personajes. Pero el contexto es un apoyo: el sentido final de la obra se construye con lo que dice el texto literario, y ese sentido puede ser distinto para cada lector si lo justifica con el texto."],
  [("relacionar", "conectar un dato externo con una frase de la obra y explicar la unión"), ("cita", "frase de la obra copiada entre comillas"), ("explicación", "razonamiento que une la cita con el dato"), ("detalle", "elemento pequeño de un texto que aporta sentido"), ("comprensión enriquecida", "entender más gracias al contexto")],
  [("Relacionar cita y dato", f"Pasaje: {PAS} {FA} Relaciona la frase «todos pueden pedirlos prestados» con la entrevista.",
    ["Cita: «todos pueden pedirlos prestados».", "Dato: el préstamo es gratuito por 15 días.", "Explicación: al ser gratis, cualquier vecino puede leer sin comprar; eso aclara el sentido de la frase de doña Rita."], "Al ser gratuito el préstamo, de verdad todos pueden pedir libros"),
   ("Evitar inventar", f"Un estudiante escribe: «El pasaje cuenta que Ema devolvió sus libros tarde y pagó multa». {PAS} ¿Es una buena relación?",
    ["Busca en el pasaje si aparece una multa: no aparece.", "La fuente A dice que el préstamo es gratuito, no menciona multas.", "Está inventando un hecho que no está en ninguno de los textos."], "No; inventa un hecho que ninguno de los textos dice")],
  [("Poner el dato sin explicar qué aporta.", "El lector no ve la conexión con la obra.", "Agrega una explicación: ahora entiendo que…"),
   ("Usar el contexto para cambiar los hechos de la obra.", "El contexto aclara; no reemplaza lo que cuenta el texto.", "Mantén los hechos de la obra y agrega solo lo que ilumina.")],
  ([E("Una relación bien hecha tiene cita, dato y… ¿qué tercera parte?", "Una explicación", "La explicación une la cita con el dato."),
    E(f"Pasaje: {PAS} ¿Qué dice doña Rita que todos pueden hacer?", "Pedir libros prestados", "Lo dice la última frase del pasaje."),
    E(f"{FA} ¿Cuántos días dura el préstamo?", "15 días", "Lo afirma la entrevista.")],
   [E(f"Pasaje: {PAS} {FA} ¿Qué detalle del pasaje explica la frase «libros sin tapa» si sabemos que los libros llegan por donaciones?", "Que muchos libros vienen donados y pueden estar gastados", "Las donaciones suelen incluir libros usados."),
    E("¿Para qué sirve explicar la conexión entre cita y dato?", "Para mostrar qué se entiende mejor gracias al contexto", "Sin explicación solo hay dos datos sueltos."),
    E("¿Puedes cambiar un hecho de la obra usando el contexto?", "No", "El contexto aclara, no reemplaza el texto.")],
   [E(f"{PAS} {FA} Elige la mejor relación: (a) «Doña Rita habla de préstamos y la entrevista dice que son gratuitos por 15 días: por eso todos pueden leer sin comprar.» (b) «El pasaje y la entrevista hablan de libros, así que no hace falta explicar la conexión.» (c) «Doña Rita habla de préstamos y la entrevista dice que los libros llegan por donaciones: por eso Ema paga por cada libro.»", "(a)", "Cita ambos textos y explica la conexión."),
    E(f"{PAS} {FA} Según la fuente A, la biblioteca atiende martes y jueves. El pasaje dice «Cada jueves». ¿Qué dato de la fuente aclara el detalle del pasaje?", "Que atiende los jueves", "Explica por qué Ema va ese día."),
    arith("La biblioteca atiende de 16:00 a 19:00. ¿Cuántas horas atiende cada día?", "19-16", "Se resta la hora de apertura a la de cierre.", " horas")],
   [E("Un estudiante escribe: «Ema es pobre porque va a la biblioteca». ¿Se apoya en el pasaje o en la entrevista?", "En ninguno; es una suposición", "Ninguno de los textos dice eso."),
    E(f"{PAS} Lee {FA} ¿Qué te permite pensar sobre la frase «no todos pueden comprar libros»? (a) Que la biblioteca ofrece una opción gratuita. (b) Que los libros son malos. (c) Que doña Rita cobra.", "(a)", "El préstamo gratuito responde a esa necesidad.")],
   [E(f"{PAS} {FB} ¿Cuál relación entre «Cada jueves» y la tabla no inventa hechos? (a) Los 560 préstamos de 2024 muestran que la biblioteca se usa mucho, lo que hace creíble que Ema vaya con frecuencia. (b) Ema pidió prestados 560 libros en 2024. (c) Ema fue la persona que más pidió libros.", "(a)", "Solo (a) se apoya en la tabla y en el pasaje sin atribuir cifras a Ema."),
    E(f"{PAS} {FC} ¿Se puede usar la fuente C para explicar el pasaje con confianza?", "No; no tiene autor ni fecha y mezcla opinión", "Es una fuente débil.")]),
  [E(f"En tu biblioteca de aula dicen: «Se presta por 15 días». Vas a escribir sobre este pasaje: {PAS} ¿Qué relación puedes escribir con ese dato?", "Que los préstamos gratuitos permiten que todos lean", "Conecta el dato con la frase de doña Rita.")],
  [E("¿Qué tres partes tiene una buena relación?", "Cita, dato y explicación", "Son los tres elementos de la clase."),
   E("¿El contexto puede reemplazar lo que cuenta la obra?", "No", "Solo la aclara."),
   E("¿Se puede inventar un hecho para explicar el pasaje?", "No", "Debe apoyarse en los textos.")],
  ("Escribe una relación de tres a cuatro líneas entre esta cita y el dato: Pasaje de ejemplo: «El pregonero anunció que la pesca de la mañana había sido buena». Dato de ejemplo: en las caletas los pescadores artesanales salen de madrugada y venden su pesca al regresar. Incluye cita, dato y explicación.",
   "Cita: «el pregonero anunció que la pesca de la mañana había sido buena». Dato: los pescadores salen de madrugada y venden al regresar. Explicación: por eso el anuncio ocurre en la mañana, cuando llega la pesca, y se entiende que la caleta es un lugar de venta.",
   ["incluye la cita", "usa el dato dado", "explica qué se entiende mejor"], ["párrafo de tres a cuatro líneas"],
   ["no explicar la conexión", "inventar hechos del cuento"], "Pide a alguien que lea solo la cita y el dato, y que diga si tu explicación los une."),
  "Elige un cuento corto y anota una frase que se entienda mejor con un dato de contexto.",
  "Inventa un dato de contexto y escribe una relación con un pasaje de ejemplo.")

# ================================================================== OA10 · clase 4
L(OA10, 4,
  "Este cuaderno y un lápiz. El pasaje y las fuentes están escritos en los ejercicios.",
  "Aprenderé a reconocer los límites de la contextualización: lo que el contexto puede aclarar y lo que no puede decidir.",
  ["Sé relacionar un dato externo con un pasaje.", "Sé que una fuente puede ser débil si no tiene autor ni fecha."],
  ["El contexto ayuda, pero tiene límites. Primero, no explica todo: un dato histórico o social no dice qué sintió un personaje ni qué quiso decir el autor. Segundo, no es una regla que obligue a una sola interpretación: personas distintas pueden leer la obra de modos diferentes si los justifican con el texto. Tercero, puede estar incompleto o desactualizado.",
   "También hay límites en las fuentes. Una fuente sin autor ni fecha no permite saber si es confiable. Una cifra de ejemplo no sirve para afirmar algo sobre todos los lugares. Una entrevista a una sola persona muestra un punto de vista, no la opinión de todos. Por eso conviene contrastar: buscar una segunda fuente y ver si coinciden.",
   "Reconocer los límites no es desanimarse; es ser un lector honesto. Una buena frase de límite dice: «Este dato aclara…, pero no permite afirmar…». Con esa frase evitas exagerar lo que el contexto puede probar."],
  [("límite", "aquello que una información no puede probar o explicar"), ("contrastar", "comparar dos o más fuentes para ver si coinciden"), ("punto de vista", "manera particular de ver un asunto"), ("desactualizado", "que ya no corresponde a la situación actual"), ("generalizar", "extender lo que vale para un caso a todos los casos")],
  [("Poner un límite", f"{PAS} {FB} Alguien concluye: «Como los préstamos subieron, Ema es feliz». ¿Qué límite hay?",
    ["La tabla muestra préstamos por año.", "No dice nada de lo que siente Ema.", "El dato aclara el uso de la biblioteca, pero no permite afirmar los sentimientos de un personaje."], "El dato no permite afirmar lo que siente Ema"),
   ("Contrastar fuentes", f"{FA} y {FC} ¿Se puede aceptar la afirmación «siempre son mejores que las públicas»?",
    ["La entrevista (A) habla de horario y préstamos, no compara con otras.", "La entrada (C) no tiene autor ni fecha.", "Ninguna fuente sólida respalda esa comparación: se necesita otra fuente."], "No; falta una fuente confiable que lo respalde")],
  [("Usar un dato para afirmar lo que siente un personaje.", "El dato describe una situación externa, no un sentimiento.", "Apoya los sentimientos en el texto literario."),
   ("Generalizar con una sola entrevista.", "Una persona muestra solo su punto de vista.", "Busca otra fuente y compara.")],
  ([E("¿Qué es un límite de la contextualización?", "Lo que una información no puede explicar o probar", "Marca hasta dónde sirve el dato."),
    E("¿Una sola entrevista muestra el punto de vista de una persona o de todos?", "De una persona", "No representa a todos."),
    E("En Lenguaje: ¿Qué significa contrastar fuentes?", "Compararlas para ver si coinciden", "Sirve para confiar más en un dato.")],
   [E(f"{FB} ¿Esta tabla permite afirmar por qué subieron los préstamos?", "No; solo muestra cuántos hubo", "Las cifras no dan razones."),
    E(f"{FA} ¿La entrevista permite afirmar que todas las bibliotecas comunitarias del país atienden martes y jueves?", "No; habla de una sola biblioteca", "No se puede generalizar."),
    E("Una información de hace 30 años sobre un oficio, ¿puede estar desactualizada?", "Sí", "Los oficios y costumbres cambian.")],
   [E(f"{FC} ¿Qué dos datos faltan para confiar en esta entrada?", "El autor y la fecha", "Sin ellos no se sabe quién lo dice ni si es actual."),
    E(f"{PAS} {FA} Elige la frase con un buen límite: (a) «El dato aclara el préstamo, pero no dice qué siente Ema.» (b) «El dato demuestra que Ema es feliz.» (c) «El dato prueba que doña Rita es la dueña.»", "(a)", "Marca lo que el dato aclara y lo que no."),
    arith(f"{FB} Del 2021 al 2024 los préstamos pasaron de 310 a 560. ¿Cuántos préstamos más hubo en 2024 que en 2021?", "560-310", "Se resta la cifra inicial a la final.", " préstamos")],
   [E("Dos lectoras interpretan de forma distinta el mismo pasaje y ambas citan el texto. ¿Es posible que ambas lecturas sean válidas?", "Sí, si cada una la justifica con el texto", "El contexto no impone una única lectura."),
    E(f"{FA} {FC} La fuente A dice que los libros llegan por donaciones; la C dice que se presta «de todo». ¿Coinciden?", "No; la C dice más de lo que la A confirma", "Una habla de libros donados y la otra afirma «todo».")],
   [E(f"{PAS} {FB} Un estudiante afirma: «El pasaje comprueba que en 2024 se prestaron 560 libros». ¿Es correcto?", "No; el pasaje es literario y no entrega cifras", "La cifra viene de la tabla, no del pasaje."),
    E("Dato de ejemplo: «En 2022 hubo 420 préstamos». ¿Qué frase de límite es correcta? (a) Aclara cuántos préstamos hubo, pero no permite afirmar por qué se pidieron. (b) Prueba que todos los vecinos leen. (c) Explica lo que siente cada lector.", "(a)", "Marca lo que el dato aclara y lo que no puede probar.")]),
  [E("Tu compañera leyó una sola entrevista y dice: «Todos los vecinos piensan igual de la biblioteca». ¿Qué límite le señalas?", "Una entrevista muestra el punto de vista de una persona", "No se puede generalizar desde un solo testimonio.")],
  [E("¿Qué se debe hacer con una fuente sin autor ni fecha?", "Usarla con cuidado o buscar otra", "No se sabe quién la escribió ni si está actualizada."),
   E("¿Un dato externo dice cómo se siente un personaje?", "No", "Ese sentido se apoya en el texto literario."),
   E("Escribe el inicio de una frase de límite.", "Este dato aclara…, pero no permite afirmar…", "Es la fórmula de la clase.")],
  ("Con este pasaje y este dato de ejemplo, escribe dos frases de límite. Pasaje: «Don Aurelio cerró el kiosco y miró el reloj del frontis». Dato: en muchos barrios los kioscos de diarios abren temprano y cierran en la tarde.",
   "Este dato aclara que el kiosco suele cerrar en la tarde, pero no permite afirmar por qué don Aurelio miró el reloj. Tampoco permite asegurar que todos los kioscos cierran a la misma hora.",
   ["incluye lo que el dato aclara", "señala lo que no permite afirmar", "evita generalizar"], ["dos frases escritas"],
   ["usar el dato para explicar un sentimiento", "generalizar a todos los kioscos"], "Lee tus frases a otra persona y comprueba que el límite sea claro."),
  "Anota un dato que hayas oído y que no sirve para afirmar algo sobre todo un grupo.",
  "Inventa una fuente débil y una fuerte sobre un mismo tema y explica la diferencia.")

# ================================================================== OA10 · clase 5
L(OA10, 5,
  "Este cuaderno y un lápiz. El pasaje y las fuentes están escritos en los ejercicios.",
  "Aprenderé a comunicar una comprensión enriquecida: un párrafo que explique un pasaje literario con apoyo de contexto, cita, dato, límite y referencia.",
  ["Sé seleccionar y relacionar información.", "Sé reconocer límites de las fuentes."],
  ["Comunicar una comprensión enriquecida es explicar a otra persona qué entendiste del pasaje y cómo el contexto te ayudó. Un párrafo claro sigue este orden: (1) tu idea sobre el pasaje, (2) la cita que la respalda, (3) el dato de contexto con su referencia, (4) la explicación de la conexión y (5) un límite o una pregunta que queda abierta.",
   "La referencia es el dato que dice de dónde sacaste la información. En un párrafo breve se puede escribir entre paréntesis: (entrevista a Rita Campos, 2024) o (tabla de préstamos de ejemplo). Citar bien muestra respeto por quien aportó la información y permite que otra persona la revise. Si copias palabras, usa comillas.",
   "Un buen párrafo no es una lista de datos: tiene un hilo. Usa conectores como «por eso», «esto aclara» y «sin embargo» para unir las partes. Revisa al final que cada dato sirva a tu idea y que no hayas inventado hechos."],
  [("comprensión enriquecida", "mayor entendimiento de la obra gracias al contexto"), ("referencia", "indicación de la fuente entre paréntesis"), ("conector", "palabra que une ideas, como por eso o sin embargo"), ("idea central", "lo principal que quieres comunicar"), ("párrafo", "conjunto de oraciones que desarrolla una idea")],
  [("Armar un párrafo", f"Pasaje: {PAS} {FA} Escribe un párrafo con idea, cita, dato con referencia, explicación y límite.",
    ["Idea: la biblioteca permite leer a quienes no pueden comprar.", "Cita: «todos pueden pedirlos prestados» y dato: préstamo gratuito por 15 días (entrevista a Rita Campos, 2024).", "Explicación y límite: por eso la frase tiene sentido, pero la entrevista no cuenta qué siente Ema."], "Párrafo con idea, cita, dato con referencia, explicación y límite"),
   ("Revisar un párrafo", "Párrafo de ejemplo: «La biblioteca es lo mejor del mundo y todos los libros son hermosos. Los préstamos son de 15 días.» ¿Qué le falta?",
    ["No cita el pasaje.", "El dato de 15 días no tiene referencia.", "Falta explicar la conexión y marcar un límite."], "Faltan cita, referencia, explicación y límite")],
  [("Escribir una lista de datos sin conectarlos.", "El lector no ve cómo ayudan a entender el pasaje.", "Une cada dato con la cita usando una explicación."),
   ("Olvidar la referencia.", "No se sabe de dónde viene el dato.", "Escribe la fuente entre paréntesis.")],
  ([E("En un párrafo de comprensión enriquecida, ¿qué dato indica de dónde viene la información?", "La referencia", "Señala la fuente."),
    E("¿Qué conector expresa consecuencia: «por eso» o «sin embargo»?", "Por eso", "«Sin embargo» marca un contraste; «por eso» muestra un resultado."),
    E("Si copias palabras de una fuente, ¿qué usas?", "Comillas", "Marcan que son palabras de otra persona.")],
   [E("¿Cuál es el orden del párrafo de la clase? (a) Idea, cita, dato con referencia, explicación y límite. (b) Límite, dato, cita, idea y referencia. (c) Dato, límite, idea.", "(a)", "Ese es el orden que se estudió."),
    E(f"{FA} ¿Cuál es una buena referencia para el dato del préstamo?", "Entrevista a Rita Campos, 14 de marzo de 2024", "Indica tipo de texto, autora y fecha."),
    E("¿Para qué sirve el límite al final del párrafo?", "Para no exagerar lo que el contexto puede probar", "Es una muestra de honestidad intelectual.")],
   [E(f"{PAS} ¿Cuál cita sirve para respaldar la idea «la biblioteca ayuda a quienes no pueden comprar libros»?", "«No todos pueden comprar libros, pero todos pueden pedirlos prestados»", "Es la frase que dice eso."),
    E(f"{FB} ¿Qué referencia pondrías para la cifra de 505 préstamos en 2023?", "Tabla de ejemplo de préstamos por año", "Indica el tipo de fuente."),
    E("Une las ideas con un conector de consecuencia: «El préstamo es gratuito; ___ todos pueden leer». ¿Cuál completa mejor: por eso, aunque o además?", "Por eso", "Es el conector que expresa consecuencia.")],
   [E("Una estudiante copió una frase de la entrevista sin comillas ni referencia. ¿Qué le falta?", "Comillas y referencia", "Debe mostrar que son palabras ajenas."),
    E("¿Por qué un párrafo no debe ser solo una lista de datos?", "Porque debe tener un hilo que los conecte con la idea", "Las explicaciones unen los datos.")],
   [E(f"{PAS} {FA} ¿Qué oración une la cita con el horario y trae referencia? (a) Ema va «cada jueves»; es coherente con que la biblioteca atienda martes y jueves (entrevista a Rita Campos, 2024). (b) Ema va cada jueves porque le gusta. (c) La biblioteca atiende siempre.", "(a)", "Une cita y dato e incluye la referencia.", ),
    E("Un párrafo tiene 5 partes: idea, cita, dato, explicación y límite. Un estudiante escribió idea, cita y dato. ¿Cuántas partes le faltan?", "2", "Faltan la explicación y el límite.")]),
  [E(f"Debes presentar en una frase y con referencia lo que aprendiste. {PAS} {FA} Escribe la referencia en el formato de la clase.", "(entrevista a Rita Campos, 14 de marzo de 2024)", "Indica tipo de fuente, autora y fecha.")],
  [E("¿Qué cinco partes tiene un buen párrafo de comprensión enriquecida? Nombra dos.", "Idea, cita, dato con referencia, explicación o límite", "Son las partes de la clase."),
   E("¿Para qué sirve citar bien?", "Para que otra persona pueda revisar la fuente", "Muestra de dónde sale la información."),
   E("¿Se puede inventar un hecho para completar un párrafo?", "No", "Solo se usan hechos de los textos.")],
  ("Escribe un párrafo de cinco a siete líneas sobre este pasaje de ejemplo: «Cada sábado, Gaspar ordenaba los libros del carrito de la plaza antes de que llegaran los niños». Usa este dato de ejemplo: los carritos de libros de plaza suelen funcionar los fines de semana y prestan libros a quienes pasan. Incluye idea, cita, dato con referencia, explicación y un límite.",
   "Gaspar cumple un rol de cuidado de la lectura. Dice que «cada sábado ordenaba los libros del carrito». Según el dato de ejemplo, estos carritos funcionan los fines de semana (dato de ejemplo sobre carritos de plaza); por eso se entiende por qué lo hace el sábado. Sin embargo, el dato no explica por qué Gaspar asume esa tarea.",
   ["tiene idea y cita", "usa el dato con referencia", "incluye explicación y límite"], ["párrafo escrito en el cuaderno"],
   ["no marcar el límite", "inventar hechos sobre Gaspar"], "Pide a alguien que subraye la cita, el dato y el límite en tu párrafo."),
  "Escribe una referencia para una información que hayas leído esta semana.",
  "Reescribe tu párrafo para un lector de 8 años: ¿qué datos de contexto agregarías?")

# ================================================================== OA12 · clase 1
L(OA12, 1,
  "Este cuaderno y un lápiz. Todos los textos y las opciones están en los ejercicios.",
  "Aprenderé a elegir con intención el tema, el género y el destinatario de un texto creativo.",
  ["Sé que existen cuentos, poemas, cartas, diarios y crónicas.", "Sé que un texto se escribe para alguien."],
  ["Escribir creativamente es tomar decisiones. Las tres primeras son el tema (de qué voy a escribir), el género (la forma del texto: cuento, crónica, diario de vida, carta, poema) y el destinatario (a quién le escribo). Cambiar una decisión cambia las otras. El mismo tema, por ejemplo una bicicleta que se perdió, puede ser un poema nostálgico, una crónica con humor o una carta a quien la encontró.",
   "El género se reconoce por sus rasgos. El cuento narra una historia inventada con personajes y problema. La crónica relata un hecho real o verosímil con la mirada y la voz de quien lo cuenta. El diario de vida registra fechas y emociones en primera persona. La carta se dirige a alguien con saludo y despedida. El poema usa versos, imágenes y ritmo para expresar una emoción.",
   "El destinatario determina el tono y el vocabulario. A una persona querida le escribimos con confianza; a una autoridad, con respeto y claridad. Antes de empezar, conviene responder tres preguntas: ¿sobre qué quiero escribir?, ¿qué forma lo cuenta mejor?, ¿quién lo va a leer? Escribir sobre algo que te importa hace que tu texto sea más auténtico."],
  [("tema", "asunto del que trata un texto"), ("género", "forma de un texto, como cuento, carta o poema"), ("destinatario", "persona o grupo a quien se escribe"), ("crónica", "texto que relata un hecho con la mirada de quien lo cuenta"), ("tono", "actitud con que se escribe, como cariñoso o formal")],
  [("Elegir un género", "Quieres contar la emoción de ver partir un tren y mostrarla con imágenes y pocas palabras. ¿Qué género te conviene: cuento, poema o carta?",
    ["Quieres expresar una emoción con imágenes.", "El poema usa versos e imágenes.", "El cuento narra una historia y la carta se dirige a alguien."], "Un poema"),
   ("Identificar destinatario y tono", "«Querida Fran: ayer vi tu bicicleta roja en la feria y me acordé de tus carreras por el pasaje. ¡Te extraño! Un abrazo, Nico.» ¿Qué género es, quién es el destinatario y qué tono tiene?",
    ["Tiene saludo («Querida Fran») y despedida («Un abrazo»): es una carta.", "Se dirige a Fran.", "Usa expresiones cariñosas: tono afectuoso."], "Carta; destinatario: Fran; tono afectuoso")],
  [("Elegir el género sin pensar en el destinatario.", "Una carta o un poema pueden no ser adecuados para quien va a leerlos.", "Primero piensa quién lo leerá."),
   ("Creer que el tema determina un solo género.", "Un mismo tema se puede escribir como poema, cuento o carta.", "Prueba el género que mejor expresa lo que quieres.")],
  ([E("«Martes 3. Hoy me puse muy nervioso antes de la prueba de ciencias.» ¿Qué género es?", "Diario de vida", "Tiene fecha y emociones en primera persona."),
    E("«Estimada directora: le escribo para pedir un nuevo balón para el taller de fútbol.» ¿Quién es el destinatario?", "La directora", "El saludo la nombra."),
    E("¿Qué género usa versos e imágenes para expresar una emoción?", "El poema", "Esa es su característica.")],
   [E("Quieres contar a tu curso, con humor, lo que pasó cuando el bus 304 llegó 12 minutos tarde y todos lo aplaudieron. ¿Qué género te sirve: crónica o carta formal?", "Crónica", "Relata un hecho cotidiano con la voz de quien lo cuenta."),
    E("¿Cambia el tono si escribes a tu abuela o al director de un diario?", "Sí", "El destinatario cambia el tono y el vocabulario."),
    E("Una historia inventada con un personaje y un problema, ¿es un cuento o un diario?", "Un cuento", "Narra un suceso inventado.")],
   [E("Combina decisiones: tema «mi mascota se perdió», destinatario «quien la encuentre». ¿Qué género es mejor: carta o poema de amor?", "Carta", "Va dirigida a una persona concreta."),
    arith("Tienes 3 temas y 4 géneros posibles. ¿Cuántas combinaciones de tema y género puedes probar?", "3*4", "Cada tema se combina con cada género.", " combinaciones"),
    E("Un texto dice: «El bus 304 llegó con doce minutos de atraso. Al abrirse la puerta, toda la parada aplaudió con ironía». ¿Qué género parece y por qué?", "Crónica; relata un hecho cotidiano con una mirada irónica", "Cuenta un suceso con la voz de quien lo vio.")],
   [E("Valentina quiere contarle a su hermano menor que la escuela no da miedo. ¿Qué tono conviene: tranquilizador o burlón?", "Tranquilizador", "El destinatario necesita calma."),
    E("Un estudiante dice: «Mi tema no sirve para poema porque es real». ¿Tiene razón?", "No; un poema puede partir de algo real", "Los poemas expresan emociones sobre hechos reales.")],
   [E("Eliges escribir sobre tu primer día en un colegio nuevo. Destinatario: tu yo del futuro. ¿Qué género encaja mejor: diario de vida o noticia?", "Diario de vida", "Registra emociones personales en primera persona."),
    E("Dos versiones del mismo tema (la lluvia): una dice «Querida lluvia, ven a visitarnos» y otra «La lluvia cae sobre los techos». ¿En cuál se ve un destinatario?", "En la primera", "La nombra con «Querida» y le habla.")]),
  [E("Tu curso hará un diario mural con textos creativos para estudiantes de 5.º básico. Quieres un texto breve y divertido sobre el recreo. ¿Qué género y qué tono eliges: crónica con humor o carta de reclamo?", "Crónica con humor", "Es breve, divertida y apropiada para esa audiencia.")],
  [E("¿Qué es el destinatario?", "Persona o grupo a quien se escribe", "Es quien lee tu texto."),
   E("¿Qué género se dirige a alguien con saludo y despedida?", "La carta", "Esa es su estructura."),
   E("¿Un tema puede escribirse en distintos géneros?", "Sí", "Cambia la forma, no el tema.")],
  ("Elige uno de estos tres temas: A) la primera vez que probé un sabor nuevo, B) el día que se cortó la luz, C) un lugar donde me siento tranquilo. Elige un género (cuento, crónica, diario, carta o poema) y un destinatario. Anota tus tres decisiones y escribe cuatro líneas de inicio.",
   "Tema B. Género: crónica. Destinatario: mis compañeros de curso. Inicio: «Cuando la luz se cortó, la sala quedó en silencio por tres segundos exactos. Luego alguien empezó a cantar…».",
   ["anota tema, género y destinatario", "el inicio es coherente con ellos", "usa un tono adecuado"], ["texto escrito en el cuaderno"],
   ["no pensar en el destinatario", "cambiar de género a mitad del texto"], "Muestra tus tres decisiones a alguien y pídele que diga si el inicio las respeta."),
  "Escribe dos temas que te importen y dos posibles destinatarios.",
  "Escribe el mismo tema como poema y como carta; compara el tono.")

# ================================================================== OA12 · clase 2
L(OA12, 2,
  "Este cuaderno y un lápiz. Todos los textos están en los ejercicios.",
  "Aprenderé a probar distintas voces y formas para un mismo texto creativo y a elegir la que mejor sirve a mi intención.",
  ["Sé elegir tema, género y destinatario.", "Sé que hay narradores en primera y tercera persona."],
  ["La voz es la manera en que habla un texto: quién cuenta y con qué tono. Puede ser una narradora en primera persona («yo corrí hacia la puerta»), un narrador en tercera persona («ella corrió hacia la puerta»), o incluso un objeto que habla. La voz en primera persona da cercanía; la de tercera permite contar lo que ven varias personas.",
   "La forma es cómo se organiza el texto: en prosa (párrafos), en verso (líneas y estrofas), en diálogo, en carta. Cambiar de forma cambia lo que se siente al leer. Un recuerdo en versos cortos suena distinto que en párrafos largos. Probar dos o tres formas antes de decidir ayuda a descubrir la más adecuada.",
   "Para cambiar la voz hay que cuidar los verbos y los pronombres: «Me asusté» pasa a «Se asustó». Mantén la misma voz durante todo el texto; mezclarla sin intención confunde. También elige un tono (humorístico, nostálgico, tenso) y mantenlo. Una buena voz suena como alguien que existe, no como una lista de hechos."],
  [("voz", "manera en que habla un texto: quién cuenta y con qué tono"), ("primera persona", "voz que cuenta con «yo» o «nosotros»"), ("tercera persona", "voz que cuenta con «él», «ella» o «ellos»"), ("verso", "línea de un poema"), ("prosa", "forma de escribir en párrafos")],
  [("Cambiar de voz", "Cambia a tercera persona: «Me asusté cuando sonó el timbre y corrí a esconderme.»",
    ["Cambio el sujeto: yo → ella.", "Cambio los verbos: me asusté → se asustó; corrí → corrió.", "Cambio el pronombre pegado al verbo: esconderme → esconderse."], "«Ella se asustó cuando sonó el timbre y corrió a esconderse»"),
   ("Probar una forma", "La idea: «la plaza vacía en invierno». ¿Cómo suena en prosa y en verso?",
    ["Prosa: «En invierno la plaza queda vacía y las bancas se llenan de hojas.»", "Verso: «Plaza vacía, / bancas con hojas. / Invierno.»", "El verso es más breve y marca pausas; la prosa explica más."], "El verso condensa; la prosa explica con más detalle")],
  [("Cambiar de voz a mitad del texto sin intención.", "El lector no sabe quién cuenta.", "Elige una voz y mantenla."),
   ("Cambiar «yo» por «él» sin cambiar los verbos.", "Quedan oraciones como «él me asusté».", "Cambia pronombres y verbos juntos.")],
  ([E("«Yo guardé la llave en el bolsillo.» ¿Está en primera o en tercera persona?", "Primera persona", "El sujeto es «yo»."),
    E("«Ella guardó la llave en el bolsillo.» ¿Está en primera o en tercera persona?", "Tercera persona", "El sujeto es «ella»."),
    E("Un texto escrito en líneas cortas con pausas, ¿es prosa o verso?", "Verso", "El verso se organiza en líneas.")],
   [E("¿Qué verbo cambia al pasar «Corrí al paradero» a tercera persona (ella)?", "Corrí pasa a corrió", "El verbo debe concordar con el nuevo sujeto."),
    E("¿Qué voz da más cercanía al lector: primera o tercera persona?", "Primera persona", "El «yo» cuenta desde dentro."),
    E("Un gato cuenta su día: «Me estiré en la ventana y vigilé el patio». ¿Qué voz tiene?", "Primera persona de un animal", "El gato habla con «me» y vigilé.")],
   [E("Cambia a primera persona (yo): «Él abrió la puerta y miró el pasillo vacío».", "Yo abrí la puerta y miré el pasillo vacío", "Cambian sujeto y verbos."),
    E("Cambia a tercera persona (ellos): «Nosotros cantamos en el patio».", "Ellos cantaron en el patio", "Cambian el sujeto y el verbo."),
    E("¿Qué tono tiene «Ay, mi abuela, cuánto extraño sus tardes de pan caliente»: nostálgico o tenso?", "Nostálgico", "Evoca con cariño algo pasado.")],
   [E("Un texto empieza «Camilo caminaba por la calle» y luego dice «me pareció que alguien me miraba». ¿Qué problema tiene la voz?", "Cambia de tercera a primera persona sin intención", "Mezcla dos voces."),
    E("¿Por qué conviene probar dos formas antes de decidir?", "Porque cada forma produce un efecto distinto", "Ayuda a elegir la que mejor sirve.")],
   [E("¿Cuál dice en dos versos cortos la idea «la lluvia golpea el techo de zinc» sin nombrar la lluvia? (a) Golpes de agua / sobre el zinc (b) La lluvia golpea el techo de zinc (c) Hoy llovió mucho en Santiago", "(a)", "Condensa la idea en dos versos con imagen y sin nombrar la lluvia."),
    E("Un texto dice: «Me levanté temprano y preparé mi mochila. Luego se puso los zapatos, abrió la puerta y salió corriendo». ¿Qué problema de voz hay?", "Pasa de primera a tercera persona sin intención y no se sabe quién cuenta", "La primera oración usa «me levanté» y la segunda «se puso», como si hablara otra persona.")]),
  [E("Quieres escribir un recuerdo de la feria para tus compañeros y que sientan que estuvieron ahí. ¿Qué voz eliges: primera persona o tercera?", "Primera persona", "Da cercanía y emoción personal.")],
  [E("¿Qué es la voz de un texto?", "La manera en que habla: quién cuenta y con qué tono", "Define cómo se siente el texto."),
   E("¿Se debe mezclar la voz sin intención?", "No", "Confunde al lector."),
   E("¿Qué es el verso?", "Una línea de un poema", "El poema se organiza en versos.")],
  ("Escribe esta idea en tres versiones: «el último día de clases». Versión 1: primera persona en prosa (dos líneas). Versión 2: tercera persona en prosa (dos líneas). Versión 3: un poema de tres versos. Después escribe cuál elegirías y por qué.",
   "1) Yo guardé mis cuadernos y sentí un nudo en la garganta. 2) Ella guardó sus cuadernos y miró el patio por última vez. 3) Cuadernos cerrados, / el patio sin timbre, / verano. Elijo la 1 porque se siente más cercana.",
   ["tres versiones distintas", "mantiene la voz en cada una", "elige y justifica"], ["tres versiones y una justificación"],
   ["mezclar voces", "cambiar solo el pronombre y no el verbo"], "Lee las tres versiones a alguien y pregúntale cuál le gustó más."),
  "Escribe una oración en primera persona y reescríbela en tercera.",
  "Escribe un texto de cuatro líneas desde la voz de un objeto de tu sala.")

# ================================================================== OA12 · clase 3
L(OA12, 3,
  "Este cuaderno y un lápiz. Todos los textos están en los ejercicios.",
  "Aprenderé a desarrollar el núcleo de un texto creativo con escenas, imágenes sensoriales y detalles que muestren en lugar de decir.",
  ["Sé elegir una voz y una forma.", "Sé que los sentidos son vista, oído, olfato, gusto y tacto."],
  ["El núcleo significativo de un texto es la idea o la emoción que lo sostiene, por ejemplo «el miedo a decepcionar» o «la alegría de un reencuentro». Para desarrollarlo no basta nombrarlo: hay que mostrarlo con una escena (un momento concreto con lugar, acción y personajes) y con detalles específicos. «Estaba nervioso» dice; «me sudaban las manos y no encontraba mi lápiz» muestra.",
   "Una imagen es una expresión que hace ver, oír, oler, probar o tocar. «El pan olía a mantequilla» es una imagen del olfato; «la corteza crujía» es una imagen del oído. Las imágenes sensoriales ayudan a que el lector viva la escena. También sirven las comparaciones («la sala parecía un acuario») cuando son claras y nuevas.",
   "Para decidir qué detalles usar, pregúntate: ¿este detalle ayuda a mostrar la emoción central? Si no la apoya, quítalo. Un buen detalle es concreto (el número, el color, el objeto exacto) y tiene función. Revisa tu borrador marcando las frases que solo dicen la emoción y reescríbelas con una acción o un sentido."],
  [("núcleo", "idea o emoción central de un texto"), ("escena", "momento concreto con lugar, acción y personajes"), ("imagen sensorial", "expresión que apela a un sentido"), ("detalle", "elemento concreto que aporta sentido"), ("mostrar", "expresar una emoción con acciones y detalles en vez de nombrarla")],
  [("Mostrar en vez de decir", "Reescribe «Tenía mucho frío» mostrándolo con una acción y un sentido.",
    ["Pienso en el cuerpo: tiritar, los dientes, las manos.", "Elijo un sentido: el tacto.", "Escribo: «Me castañeteaban los dientes y no sentía los dedos»."], "«Me castañeteaban los dientes y no sentía los dedos»"),
   ("Escoger detalles útiles", "El núcleo es «la alegría de volver a casa». ¿Cuál detalle lo apoya mejor: (a) «el bus tenía asientos verdes» o (b) «sentí el olor a pan en la escalera y subí de dos en dos»?",
    ["Pregunto qué detalle muestra alegría.", "El olor a pan y subir de dos en dos transmiten ganas de llegar.", "Los asientos verdes no tienen relación con la emoción."], "El detalle del pan y de subir de dos en dos")],
  [("Nombrar la emoción en lugar de mostrarla.", "El lector sabe lo que sientes, pero no lo vive.", "Usa una acción, una imagen y un detalle."),
   ("Agregar detalles que no sirven al núcleo.", "Distraen y alargan el texto.", "Pregunta si cada detalle apoya la idea central.")],
  ([E("«Estaba nervioso.» ¿Esa frase muestra o dice la emoción?", "La dice", "Nombra la emoción sin escena."),
    E("«Me sudaban las manos y se me caía el lápiz.» ¿Esa frase muestra o dice?", "La muestra", "Usa acciones concretas."),
    E("¿Qué sentido evoca «olía a pan recién horneado»?", "El olfato", "Habla de un olor.")],
   [E("¿Qué sentido evoca «la corteza crujía»?", "El oído", "Se refiere a un sonido."),
    E("¿Qué es el núcleo de un texto?", "Su idea o emoción central", "Todo el texto debe apoyarla."),
    E("«La sala parecía un acuario» ¿es una comparación o una enumeración?", "Una comparación", "Relaciona la sala con un acuario usando «parecía».")],
   [E("Núcleo: «el miedo antes de hablar en público». ¿Cuál detalle lo muestra? (a) «El micrófono estaba sobre la mesa.» (b) «Se me secó la boca y las hojas temblaban en mis manos.» (c) «Había diez sillas.»", "(b)", "Muestra miedo con el cuerpo."),
    E("¿Cuál muestra el cansancio sin nombrarlo? (a) Arrastraba los pies y los párpados me pesaban. (b) Estaba muy cansado. (c) Me sentía agotado.", "(a)", "Usa acciones del cuerpo en vez de nombrar la emoción."),
    E("Nombra el sentido de «el helado me dejó los dedos pegajosos y fríos».", "El tacto", "Describe lo que se siente en los dedos.")],
   [E("Una estudiante escribe «Fue un día muy triste» y no agrega nada más. ¿Qué le recomiendas?", "Mostrar la tristeza con una escena, acciones y detalles", "Una escena hace vivir la emoción."),
    E("En un texto sobre una despedida, aparece «Los autos de la calle eran azules». ¿Ayuda al núcleo?", "No, salvo que se relacione con la despedida", "Un detalle sin función distrae.")],
   [E("Núcleo: «la alegría del reencuentro». Elige la escena más adecuada: (a) «Abrí la puerta, salté sobre mi hermana y no la solté hasta que se rió». (b) «Esperé en la parada». (c) «Compré un pan».", "(a)", "Muestra alegría con acciones."),
    arith("Un borrador tiene 12 frases y 7 solo nombran la emoción. ¿Cuántas frases ya muestran la emoción?", "12-7", "Se resta al total las que solo la nombran.", " frases")]),
  [E("Tienes que escribir para el diario mural una escena sobre «el primer día de clases». El núcleo es la ansiedad. Escribe una frase que la muestre con un sentido.", "Por ejemplo: Se me aflojaron las rodillas al oír el timbre", "Muestra ansiedad con el cuerpo.")],
  [E("¿Qué es mostrar en vez de decir?", "Expresar una emoción con acciones y detalles", "El lector la vive."),
   E("¿Qué es una imagen sensorial?", "Una expresión que apela a un sentido", "Hace ver, oír, oler, probar o tocar."),
   E("¿Un detalle debe apoyar el núcleo?", "Sí", "Si no lo apoya, se quita.")],
  ("Escribe una escena de cinco a seis líneas con el núcleo «la sorpresa de encontrar algo perdido». Debe incluir al menos dos imágenes de sentidos distintos, una acción concreta y ningún uso de la palabra «sorpresa».",
   "Metí la mano en el bolsillo de la mochila y toqué algo frío y metálico. Saqué la llave, la que buscaba hacía tres días. Me temblaron los dedos y solté una risa que resonó en toda la sala.",
   ["tiene un núcleo claro", "incluye dos sentidos distintos", "muestra la emoción con acciones"], ["escena escrita"],
   ["nombrar la emoción", "agregar detalles sin función"], "Lee tu escena a alguien y pregúntale qué emoción sintió."),
  "Escribe una frase que muestre alegría sin nombrarla.",
  "Escribe la misma escena con un olor y con un sonido, y compara.")

# ================================================================== OA12 · clase 4
BORR = "Borrador de ejemplo: «Era un sábado. Fui a la feria con mi tía. Había mucha gente. Compré una sandía enorme. La sandía estaba rica. Después volvimos a casa.»"
L(OA12, 4,
  "Este cuaderno y un lápiz. El borrador y los comentarios están en los ejercicios.",
  "Aprenderé a compartir un borrador, recibir comentarios útiles y decidir qué cambios hacer, explicando mi decisión de autor.",
  ["Sé desarrollar un núcleo con escenas y detalles.", "Sé que un borrador se puede mejorar."],
  ["Compartir un borrador sirve para ver cómo lo recibe un lector. Antes de compartir, decide qué quieres saber: ¿se entiende?, ¿qué imagen quedó?, ¿qué parte aburre? Quien comenta debe ser específico y respetuoso. Un comentario útil dice qué parte, qué efecto produjo y qué se podría probar: «En la línea tres no entendí quién habla; quizá puedes nombrar al personaje».",
   "Un comentario poco útil es vago («está bien», «no me gustó») o está dirigido a la persona («escribes mal»). Como autor, tú decides qué cambios aceptar. Revisa cada comentario con tres preguntas: ¿afecta mi núcleo?, ¿ayuda al lector que quiero?, ¿vale la pena el cambio? Puedes aceptar, rechazar o transformar un comentario, pero conviene anotar la razón.",
   "Una decisión de autor es una elección explicada: «Mantengo el final abierto porque quiero que el lector imagine». Registrar las decisiones te ayuda a revisar con criterio y a aprender de cada borrador. Cuando recibas un comentario, agradécelo, pregúntale al lector qué sintió y no te defiendas de inmediato."],
  [("borrador", "versión de trabajo de un texto, que todavía se puede cambiar"), ("comentario útil", "observación específica, respetuosa y con una sugerencia"), ("decisión de autor", "elección sobre el texto explicada con una razón"), ("sugerencia", "propuesta para mejorar algo"), ("lector", "persona que recibe y comenta el texto")],
  [("Evaluar comentarios", f"{BORR} Comentario 1: «No me gustó.» Comentario 2: «Las oraciones son muy cortas y todas empiezan igual; prueba juntar dos.» ¿Cuál es más útil?",
    ["El comentario 1 es vago: no dice qué parte ni por qué.", "El comentario 2 señala el problema y sugiere una solución.", "Por eso el 2 sirve para mejorar el borrador."], "El comentario 2"),
   ("Decidir y justificar", f"{BORR} Un lector sugiere: «Cuenta cómo olía la feria». Tu núcleo es «la alegría de comprar algo grande». ¿Qué decides?",
    ["Pregunto si el cambio apoya el núcleo.", "Un olor de la feria puede mostrar alegría y ambiente.", "Decido agregar una imagen del olfato y lo anoto con una razón."], "Aceptar: agregar el olor porque muestra el ambiente y apoya la alegría")],
  [("Defenderse de inmediato ante un comentario.", "Se pierde la oportunidad de saber cómo lo vio el lector.", "Primero escucha y pregunta; luego decide."),
   ("Aceptar todos los comentarios sin pensar.", "El texto deja de ser tuyo y pierde su núcleo.", "Decide con tres preguntas y anota la razón.")],
  ([E("¿Es útil un comentario como «me aburrió»?", "No; es vago y no dice qué parte", "No orienta cómo mejorar."),
    E("¿Quién decide qué cambios hacer en un texto: el autor o el lector?", "El autor", "Los comentarios se analizan, pero la decisión es del autor."),
    E("Un comentario útil, ¿es específico o general?", "Específico", "Señala qué parte y propone algo.")],
   [E(f"{BORR} ¿Qué dos oraciones del borrador repiten una misma idea de la sandía?", "«Compré una sandía enorme» y «La sandía estaba rica»", "Repiten sandía sin aportar algo distinto."),
    E("¿Cuál es la mejor respuesta a un comentario? (a) «Gracias, ¿qué parte te llamó más la atención?» (b) «Tú no entiendes de poemas.» (c) «Ya no importa.»", "(a)", "Escucha y pide más información."),
    E("¿Qué debe acompañar a una decisión de autor?", "Una razón", "Explica por qué se mantiene o se cambia algo.")],
   [E(f"{BORR} Mejora la segunda parte uniendo dos oraciones: «Fui a la feria con mi tía. Había mucha gente.»", "Fui a la feria con mi tía, donde había mucha gente", "Combina dos oraciones cortas en una."),
    E("Un lector dice: «En la línea tres no sé quién habla». ¿Qué cambio propondrías?", "Nombrar al personaje", "Aclara la voz."),
    arith("Recibiste 8 comentarios: 3 vagos y el resto específicos. ¿Cuántos comentarios específicos recibiste?", "8-3", "Se resta al total los vagos.", " comentarios")],
   [E("Un compañero te dice «tu texto es lo peor». ¿Qué tipo de comentario es y qué haces?", "Es un comentario dirigido a la persona; pides que diga qué parte y por qué", "Pedir precisión convierte la crítica en útil."),
    E("Cuatro lectores piden que cambies tu final, pero tu núcleo requiere ese final. ¿Qué decides y cómo lo explicas?", "Mantengo el final y explico que apoya el núcleo", "La decisión se justifica con el núcleo.")],
   [E(f"{BORR} Un lector dice: «Falta una imagen de la sandía». ¿Cuál frase agrega una imagen sensorial? (a) La sandía pesaba tanto que me dolieron los brazos y olía a verano. (b) La sandía era una fruta. (c) Compré una sandía.", "(a)", "Agrega tacto y olfato."),
    E("Sugieren borrar la última línea y quieres mantenerla. ¿Qué decisión de autor está bien escrita? (a) Mantengo la última línea porque cierra el texto con la emoción central. (b) La mantengo porque sí. (c) La mantengo porque nadie opinó.", "(a)", "Una decisión de autor siempre va con una razón relacionada con el texto.")]),
  [E(f"Tu curso intercambia borradores. Recibes el comentario: «En tu texto no sé dónde estás». ¿Qué respuesta pide más información? (a) ¿Qué esperabas ver para saber dónde estoy? (b) Qué lata. (c) No importa dónde.", "(a)", "Convierte el comentario en una pista útil.")],
  [E("¿Qué hace específico a un comentario?", "Señala una parte y propone algo", "Orienta al autor."),
   E("¿Se debe aceptar todo comentario?", "No", "El autor decide con razón."),
   E("¿Qué se hace con los comentarios vagos?", "Se pide al lector que sea más preciso", "Así pueden ayudar.")],
  ("Intercambia con alguien un texto breve tuyo (o usa este borrador de ejemplo: «Hoy llovió. Salí con paraguas. Me mojé igual. Llegué a casa y tomé té.»). Escribe tres comentarios útiles para ese borrador, cada uno con parte, efecto y sugerencia, y una decisión de autor justificada.",
   "Comentario 1: las oraciones son muy cortas; prueba unir «Salí con paraguas» y «me mojé igual». Comentario 2: falta una imagen de la lluvia; agrega un sonido. Comentario 3: el té sorprende; desarrolla ese final. Decisión: mantengo el final breve porque quiero cerrar con calma.",
   ["tres comentarios específicos", "cada uno con sugerencia", "una decisión justificada"], ["comentarios y decisión en el cuaderno"],
   ["comentarios vagos", "no justificar la decisión"], "Pide a quien comentó que diga cuál comentario fue el más útil."),
  "Escribe un comentario específico para una oración tuya.",
  "Escribe qué te dirías a ti mismo sobre tu último texto, con parte, efecto y sugerencia.")

# ================================================================== OA12 · clase 5
L(OA12, 5,
  "Este cuaderno y un lápiz. Todos los textos están en los ejercicios.",
  "Aprenderé a editar una versión de mi texto creativo para que circule: ortografía, puntuación, concordancia y claridad.",
  ["Sé revisar un borrador con comentarios.", "Sé usar punto, coma y tildes en oraciones simples."],
  ["Editar es la última revisión antes de compartir un texto. Ya no cambias las ideas grandes: cuidas los detalles que facilitan la lectura. Revisa en este orden: (1) que el texto diga lo que quieres, (2) que las oraciones estén completas, (3) la concordancia entre sujeto y verbo y entre sustantivo y adjetivo, (4) los tiempos verbales, (5) la puntuación y (6) la ortografía, incluidas las tildes.",
   "Algunos errores frecuentes: cambiar de tiempo verbal sin razón («ayer salgo»), olvidar la concordancia («los niños jugó»), repetir una palabra muchas veces o escribir una oración demasiado larga sin puntuar. La coma separa elementos de una enumeración y encierra aclaraciones; el punto cierra una idea completa; las comillas o rayas marcan lo que dicen los personajes.",
   "Una buena estrategia es leer el texto en voz alta, lento, y marcar donde te trabas. Luego pide a otra persona que lo lea y señale lo que no entiende. Cuando termines, comprueba que el título, el nombre del autor y la fecha estén y que el formato sea legible. Un texto bien editado respeta a quien lo lee."],
  [("editar", "revisar un texto para corregir detalles antes de compartirlo"), ("concordancia", "acuerdo de número y persona entre palabras"), ("tiempo verbal", "momento en que ocurre la acción"), ("puntuación", "signos como punto, coma y comillas"), ("versión final", "texto listo para circular")],
  [("Corregir concordancia y tiempo", "Edita: «Ayer los niños juega en el patio y mañana cantó una canción».",
    ["Concordancia: los niños juegan.", "Tiempo: «ayer» pide pasado: jugaron.", "«Mañana» pide futuro: cantarán."], "«Ayer los niños jugaron en el patio y mañana cantarán una canción»"),
   ("Puntuar una enumeración", "Edita: «Compré pan queso aceitunas y un jugo para el paseo».",
    ["Separo los elementos de la lista con comas.", "Antes de la y final no se pone coma.", "Cierro con punto."], "«Compré pan, queso, aceitunas y un jugo para el paseo.»")],
  [("Corregir solo la ortografía y dejar errores de concordancia.", "El texto sigue confuso aunque tenga bien las tildes.", "Sigue la lista de seis pasos."),
   ("Cambiar el sentido del texto al editar.", "La edición cuida detalles, no cambia las ideas.", "Si quieres cambiar ideas, vuelve a revisar el borrador.")],
  ([E("«Los gatos duerme en el techo.» ¿Cuál es la forma correcta del verbo?", "Duermen", "El sujeto «los gatos» es plural."),
    E("Edita: «Ayer comimos pan mañana comeremos arroz» agregando la coma o el punto que falta. ¿Dónde va?", "Después de «pan»", "Separa dos acciones distintas."),
    E("¿En qué orden se revisa primero: el sentido del texto o la ortografía?", "El sentido del texto", "Se parte por lo grande.")],
   [E("En la oración «La niña alta y simpático llegó», ¿qué palabra no concuerda?", "Simpático", "Debe ser simpática para concordar con «la niña»."),
    E("«Mañana fui al parque.» ¿Qué error de tiempo verbal tiene?", "Usa pasado con «mañana»", "«Mañana» pide futuro."),
    E("¿Para qué sirve leer el texto en voz alta al editar?", "Para detectar dónde te trabas", "La lectura revela errores.")],
   [E("Edita la oración: «Mis amigos y yo juega fútbol los sábado». Escribe la versión correcta.", "Mis amigos y yo jugamos fútbol los sábados", "Corrige verbo y plural."),
    E("Pon las comas: «En la mochila llevo cuadernos lápices una regla y una manzana».", "En la mochila llevo cuadernos, lápices, una regla y una manzana", "Separa los elementos de la lista."),
    E("¿Qué palabra se repite en «La puerta era vieja. La puerta crujía. La puerta se abrió»?", "Puerta", "Se repite tres veces.")],
   [E("Una estudiante dice: «Edité mi texto y ahora tiene otro final». ¿Eso es edición o es un cambio de las ideas grandes?", "Un cambio de las ideas grandes", "Editar cuida detalles y no cambia las ideas grandes."),
    E("Un texto de 20 oraciones tiene 5 errores de concordancia. ¿Cuántas oraciones quedan sin ese error si hay un error por oración?", "15", "Se resta cinco de veinte.")],
   [E("Edita este párrafo: «Ayer el equipo ganaron el partido, los hinchas gritó de alegría y Tomás festejan con su familia». Escribe la versión correcta.", "Ayer el equipo ganó el partido, los hinchas gritaron de alegría y Tomás festejó con su familia", "Concuerdan sujeto y verbo en pasado."),
    E("¿Qué cuatro elementos conviene revisar antes de compartir tu texto final?", "Título, nombre del autor, fecha y formato legible", "Son datos básicos para circular.")]),
  [E("Tu texto saldrá en el diario mural. Dice: «Los estudiantes pintaron el mural y nos gusto mucho». ¿Cuál es la edición correcta?", "Los estudiantes pintaron el mural y nos gustó mucho", "Se corrige la tilde de gustó.")],
  [E("¿Qué es editar?", "Revisar un texto para corregir detalles antes de compartirlo", "Es la última revisión."),
   E("¿Qué es la concordancia?", "El acuerdo de número y persona entre palabras", "Hace que las oraciones suenen bien."),
   E("¿Qué estrategia de lectura te ayuda a notar dónde te trabas al editar tu texto?", "Leerlo en voz alta", "Al oírlo se notan los errores y las frases confusas.")],
  ("Edita este texto de ejemplo y escribe la versión final: «Ayer mi hermanos y yo fue a la playa. Llevamos pelota toalla y un jugo. El mar estaba frío pero igual nos bañaron. Mañana volvimos otra vez». Debes corregir concordancia, tiempos verbales y puntuación, y no cambiar el sentido.",
   "Ayer mis hermanos y yo fuimos a la playa. Llevamos pelota, toalla y un jugo. El mar estaba frío, pero igual nos bañamos. Mañana volveremos otra vez.",
   ["corrige la concordancia", "corrige los tiempos verbales", "agrega las comas necesarias"], ["texto corregido en el cuaderno"],
   ["cambiar el sentido", "dejar errores sin corregir"], "Léelo en voz alta y verifica que no te trabes."),
  "Elige una oración tuya y revisa su concordancia.",
  "Escribe un texto de cuatro líneas con tres errores a propósito y pide a otra persona que los encuentre.")

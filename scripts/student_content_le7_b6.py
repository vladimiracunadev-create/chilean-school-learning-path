"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 15 (proceso de escritura situado).

Todos los textos, mensajes, borradores y listas de ideas son originales e inventados;
cada ejercicio trae escritos los textos y datos que necesita.
Nota: los títulos de las clases del repositorio son específicos del eje; este cuaderno los sigue.
El uso del procesador de textos se trabaja con instrucciones generales (no depende de un programa en particular);
queda como vacío la práctica real con un programa concreto.
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


OA = "LE07 OA 15"

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. Los mensajes y las situaciones están escritos en los ejercicios.",
  "Aprenderé a analizar el contexto, el género y el destinatario de un texto y a adecuar el registro: vocabulario, persona gramatical y estructura.",
  ["Sé que hay textos para distintas audiencias.", "Sé qué es un destinatario."],
  ["Todo texto se escribe en un contexto: quién escribe, a quién, para qué y en qué situación. Estos datos determinan el género (carta, correo, afiche, mensaje de chat, informe) y el registro, es decir, la manera de usar el lenguaje. El registro formal se usa con autoridades o en situaciones oficiales: trata de «usted», evita abreviaturas y expresiones coloquiales. El registro informal se usa entre amigos: trata de «tú», admite expresiones del habla cotidiana y de las redes sociales.",
   "Para adecuar el registro cuida tres aspectos. El vocabulario: términos técnicos cuando el tema lo exige (por ejemplo, «margen» o «interlineado» en un documento), frases hechas con cuidado («estar en las nubes») y evitar palabras propias del chat o del habla coloquial («al tiro», «po») en textos formales. La persona gramatical: primera persona (yo, nosotros), segunda (tú, usted) o tercera (él, ellos, o forma impersonal). Y la estructura del texto: saludo, cuerpo y despedida en una carta; título y párrafos en un informe.",
   "Antes de escribir, responde cuatro preguntas: ¿quién soy?, ¿quién es mi destinatario?, ¿qué quiero lograr?, ¿qué género y registro corresponden? El mismo contenido cambia según la situación: pedir un balón a un amigo y pedirlo a la directora son dos textos distintos aunque el pedido sea el mismo."],
  [("contexto", "situación en que se escribe: quién, a quién, para qué"), ("registro", "manera de usar el lenguaje según la situación"), ("formal", "registro respetuoso y cuidado, propio de situaciones oficiales"), ("informal", "registro cercano y espontáneo, propio de amigos"), ("persona gramatical", "quién habla o de quién se habla: yo, tú, él, nosotros...")],
  [("Adecuar el registro", "Mensaje informal: «Oye, ¿me pasas el afiche al tiro? Es urgente, po». Reescríbelo para pedírselo a la profesora jefe.",
    ["Cambio el trato de «tú» a «usted».", "Quito «al tiro» y «po».", "Agrego saludo y despedida."], "«Estimada profesora: le solicito, por favor, el afiche del taller. Es urgente. Muchas gracias.»"),
   ("Reconocer el contexto", "Un correo comienza «Estimado señor alcalde: me dirijo a usted para solicitar el arreglo de la cancha». ¿Quién es el destinatario y qué registro usa?",
    ["El saludo dice «señor alcalde»: destinatario, el alcalde.", "Usa «usted» y fórmulas respetuosas.", "Es un registro formal."], "Destinatario: el alcalde; registro formal")],
  [("Usar el mismo registro para todo.", "Una expresión de chat puede sonar irrespetuosa ante una autoridad.", "Adecúa el registro al destinatario."),
   ("Mezclar «tú» y «usted» en un mismo texto.", "Confunde al lector y cambia el trato.", "Elige un trato y mantenlo.")],
  ([E("«Estimada directora: le solicito autorización.» ¿Usa registro formal o informal?", "Formal", "Trata de usted y usa un saludo respetuoso."),
    E("«Oye, ¿vamos al tiro?» ¿Usa registro formal o informal?", "Informal", "Es una expresión del habla cotidiana."),
    E("¿Qué trato se usa en una carta formal: tú o usted?", "Usted", "Es la forma respetuosa.")],
   [E("Un mensaje para un amigo dice «Jaja, ¿cachai la tarea?». Si se lo envías a la profesora, ¿qué debes cambiar?", "Las expresiones del habla coloquial y el trato", "No son adecuadas para ese destinatario."),
    E("«Margen» e «interlineado», en un trabajo escrito, ¿son términos técnicos o frases hechas?", "Términos técnicos", "Son palabras específicas de la edición de documentos."),
    E("«Estar en las nubes» ¿es una frase hecha o un término técnico?", "Una frase hecha", "Es una expresión fija que significa estar distraído.")],
   [E("Elige la versión adecuada para pedir un permiso al director: (a) «Director, déjenos salir al tiro, po». (b) «Estimado director: solicitamos su autorización para salir a la actividad». (c) «Ey, dime que sí».", "(b)", "Usa un registro formal y respetuoso."),
    E("Cambia a primera persona plural: «Preparé el afiche».", "Preparamos el afiche", "El verbo cambia de yo a nosotros."),
    E("Un informe escolar sobre el reciclaje usa «se recolectaron 40 kilos» en vez de «recolectamos 40 kilos». ¿Qué persona gramatical usa: impersonal o primera persona?", "Impersonal", "Con «se» no se nombra a quien actúa.")],
   [E("Una estudiante escribe a un diario local: «Hola, wena, quiero reclamar xq no hay luz». ¿Cuántos problemas de registro tiene? Cuenta saludo informal, abreviatura y expresión coloquial.", "3", "Son «hola», «xq» y «wena»."),
    E("Escribes un mensaje de chat al curso para avisar una reunión y otro a la directora para lo mismo. ¿Cuál debe ser más formal?", "El de la directora", "El destinatario es una autoridad.")],
   [E("Un texto comienza «Querida abuela, te quiero contar…». ¿Qué género y qué registro es el más probable?", "Carta personal y registro informal afectuoso", "Usa trato cercano y vocativo cariñoso."),
    E("¿Qué despedida es adecuada en una carta formal a la directora: «Atentamente» o «Chao po»?", "Atentamente", "Es una fórmula respetuosa de cierre.")]),
  [E("Debes escribir el aviso de una feria de ciencias para estudiantes de 5.º, 6.º, 7.º y 8.º. ¿Qué registro es más adecuado: formal respetuoso o muy informal con jerga del chat?", "Formal respetuoso o neutro y claro", "Debe ser entendido por todos y ser adecuado al colegio.")],
  [E("¿Qué determina el registro de un texto?", "El contexto y el destinatario", "Define el trato y el vocabulario."),
   E("¿Se pueden mezclar «tú» y «usted» en un mismo texto?", "No", "Confunde el trato."),
   E("¿Qué es el registro?", "La manera de usar el lenguaje según la situación", "Cambia con el destinatario.")],
  ("Escribe el mismo pedido («quiero que me presten el gimnasio el viernes para ensayar») de dos maneras: un mensaje para un amigo del curso y un correo para el encargado del gimnasio. Subraya tres diferencias de vocabulario, persona gramatical y estructura.",
   "Amigo: «Oye, ¿me prestas el gimnasio el viernes pa ensayar?» Encargado: «Estimado señor: le solicito el uso del gimnasio el viernes para ensayar. Muchas gracias. Atentamente, Camila». Diferencias: trato tú/usted, vocabulario coloquial/formal, saludo y despedida.",
   ["dos versiones coherentes con cada destinatario", "tres diferencias marcadas", "estructura con saludo y despedida en la formal"], ["dos textos y una lista de diferencias"],
   ["mezclar registros", "no marcar diferencias"], "Lee ambos mensajes a alguien y pídele que adivine quién es el destinatario de cada uno."),
  "Escribe dos formas de saludar: una formal y una informal.",
  "Convierte un mensaje de chat tuyo en un correo formal.")

# ================================================================== clase 2
IDEAS = "Lluvia de ideas de ejemplo para un afiche del taller de reciclaje: fecha del taller; botellas plásticas; un chiste sobre el tarro de basura; cómo separar el papel; dónde queda la sala; mi cumpleaños; qué se puede hacer con cartón; hora de inicio; cuántas personas pueden asistir."
L(OA, 2,
  "Este cuaderno y un lápiz. Las listas de ideas y los esquemas están escritos en los ejercicios.",
  "Aprenderé a recopilar información e ideas, a agruparlas y a organizarlas en un esquema antes de escribir.",
  ["Sé analizar el contexto y el destinatario.", "Sé qué es una idea principal."],
  ["Escribir bien comienza antes de escribir. Primero se recopilan ideas y datos: una lluvia de ideas (anotar todo lo que se te ocurra sin juzgar), conversar con personas, leer fuentes y observar. Luego se clasifican: unas ideas sirven para el propósito y el destinatario; otras no, y se descartan. Por último se agrupan por tema y se ordenan.",
   "Para organizar puedes usar un mapa de ideas (un centro con ramas) o un esquema con numeración: 1. Presentación; 2. Desarrollo (con subpuntos); 3. Cierre. Cada grupo de ideas se convierte en un párrafo o en una sección. Un buen esquema responde: ¿qué va primero, qué después y qué al final? ¿Qué información falta?",
   "La información debe ser pertinente: se relaciona con el propósito. Si estás escribiendo un afiche para un taller, importan la fecha, la hora y el lugar; un chiste personal o tu cumpleaños no ayudan. Organizar antes de escribir ahorra tiempo en la revisión, porque evita desórdenes y repeticiones."],
  [("lluvia de ideas", "anotar sin juzgar todas las ideas que se te ocurran"), ("pertinente", "que se relaciona con el propósito del texto"), ("agrupar", "reunir ideas que tratan de lo mismo"), ("esquema", "plan ordenado de las partes de un texto"), ("mapa de ideas", "dibujo con una idea central y ramas")],
  [("Clasificar ideas", f"{IDEAS} ¿Qué ideas descartarías para un afiche informativo?",
    ["El propósito es informar sobre el taller.", "El chiste y mi cumpleaños no aportan información del taller.", "Las demás ideas sirven a la audiencia."], "El chiste sobre el tarro de basura y mi cumpleaños"),
   ("Agrupar", f"{IDEAS} Agrupa las ideas pertinentes en dos grupos: ¿cuándo y dónde? y ¿qué se hará?",
    ["Cuándo y dónde: fecha, hora, sala.", "Qué se hará: botellas plásticas, cómo separar el papel, qué hacer con cartón.", "Cupos: se puede añadir a «cuándo y dónde» o a un tercer grupo."], "Cuándo y dónde: fecha, hora y sala; qué se hará: botellas, papel, cartón (y cupos aparte)")],
  [("Escribir sin reunir ideas.", "Se pierden datos importantes y se repite.", "Anota primero todo y luego clasifica."),
   ("Incluir todas las ideas por ser tuyas.", "Algunas no sirven al propósito.", "Descarta lo que no sea pertinente.")],
  ([E(f"{IDEAS} ¿Qué idea es dato de lugar?", "Dónde queda la sala", "Responde a la pregunta dónde."),
    E(f"{IDEAS} ¿Es pertinente «mi cumpleaños» para un afiche del taller?", "No", "No se relaciona con el propósito."),
    E("¿Qué es una lluvia de ideas?", "Anotar sin juzgar todas las ideas que se te ocurran", "Es el primer paso de recopilar.")],
   [E(f"{IDEAS} ¿Cuántas ideas hay en total en la lluvia de ideas?", "9", "Se cuentan las separadas por punto y coma: son nueve."),
    E("Un esquema tiene tres partes. ¿Cuáles son?", "Presentación, desarrollo y cierre", "Es la estructura básica."),
    E("Un mapa de ideas tiene una idea central y... ¿qué más?", "Ramas con ideas relacionadas", "Muestra cómo se conectan.")],
   [arith(f"{IDEAS} Se descartan 2 ideas por no ser pertinentes. ¿Cuántas ideas quedan?", "9-2", "Se restan las descartadas del total de 9.", " ideas"),
    E("Ordena un esquema para una carta: a) petición, b) saludo, c) problema, d) despedida. Escribe las letras en orden.", "b, c, a, d", "Va del saludo a la despedida."),
    E("Agrupa: «botellas», «papel», «cartón». ¿Qué título les pondrías?", "Materiales para reciclar", "Son materiales con ese fin.")],
   [E("Dos estudiantes escriben sobre el mismo taller. Uno solo anotó 2 ideas y el otro 9. ¿Quién tiene más material para elegir?", "El de 9 ideas", "Con más ideas puede clasificar y elegir mejor."),
    E("Un estudiante comienza a escribir sin esquema y mezcla horarios con chistes. ¿Qué le hubiera ayudado?", "Clasificar y ordenar las ideas antes de escribir", "Un esquema evita el desorden.")],
   [E("Esquema: 1. Presentación del taller; 2. Qué se hará (botellas, papel, cartón); 3. Datos prácticos (fecha, hora, sala); 4. Cierre. ¿Qué información falta para la audiencia? (a) Cómo inscribirse. (b) Una anécdota personal del autor. (c) Un chiste sobre el taller.", "(a)", "Es información práctica que la audiencia necesita."),
    arith("Un esquema tiene 4 secciones y cada una agrupa 3 ideas. ¿Cuántas ideas organiza?", "4*3", "Se multiplica el número de secciones por las ideas de cada una.", " ideas")]),
  [E("Debes escribir un correo para pedir dos sillas para la biblioteca. Anotaste: motivo, cantidad, para qué fecha, y un comentario sobre el clima. ¿Cuál descartas?", "El comentario sobre el clima", "No es pertinente al pedido.")],
  [E("¿Qué se hace después de la lluvia de ideas?", "Clasificar y agrupar las ideas", "Se separan lo pertinente y lo que no."),
   E("¿Qué responde un esquema?", "Qué va primero, qué después y qué al final", "Ordena el texto."),
   E("¿Puedes descartar ideas?", "Sí, las que no son pertinentes", "No todo sirve al propósito.")],
  ("Con esta lluvia de ideas de ejemplo para un correo que invita a un campeonato: nombre del campeonato; mi mascota; fecha; reglas básicas; lugar; el color de las camisetas; cómo inscribirse; qué premio hay; una anécdota del año pasado. Descarta dos, agrupa el resto en tres grupos con título y arma el esquema del correo.",
   "Descarto: mi mascota y la anécdota del año pasado. Grupos: Qué es (nombre, reglas, premio); Cuándo y dónde (fecha, lugar); Cómo participar (inscripción, color de camiseta). Esquema: 1. Presentación; 2. Qué es; 3. Cuándo y dónde; 4. Cómo participar; 5. Cierre.",
   ["descarta ideas no pertinentes", "agrupa con títulos", "esquema ordenado"], ["lista, grupos y esquema"],
   ["no descartar nada", "grupos sin título"], "Pide a alguien que busque qué información falta en tu esquema."),
  "Haz una lista de siete ideas sobre tu fin de semana y agrúpalas.",
  "Arma un mapa de ideas con una idea central y cuatro ramas.")

# ================================================================== clase 3
L(OA, 3,
  "Este cuaderno y un lápiz. Los borradores y textos están escritos en los ejercicios.",
  "Aprenderé a escribir un borrador completo con inicio, desarrollo y cierre a partir de un esquema.",
  ["Sé organizar ideas en un esquema.", "Sé adecuar el registro al destinatario."],
  ["Un borrador es una primera versión completa del texto. No es la versión final: sirve para poner las ideas por escrito y revisarlas después. Para escribirlo, sigue el esquema y convierte cada punto en uno o más párrafos. Escribe con fluidez, sin detenerte a corregir cada tilde; si dudas de una palabra, subráyala y sigue.",
   "Todo borrador completo tiene tres partes. El inicio presenta el asunto y capta la atención del lector. El desarrollo explica o argumenta con datos, ejemplos y razones, un párrafo por idea. El cierre resume o pide algo. Cada párrafo comienza con una oración que anuncia su idea y continúa con detalles. Los conectores (primero, además, por eso, finalmente) ayudan a unir las partes.",
   "Escribir un borrador completo significa que no deja puntos del esquema sin desarrollar. Si te falta un dato, anota una marca entre corchetes, como [buscar fecha], para completarlo después. Termina el borrador antes de revisarlo: corregir mientras escribes puede cortar el hilo de tus ideas."],
  [("borrador", "primera versión completa de un texto"), ("párrafo", "conjunto de oraciones sobre una idea"), ("oración temática", "oración que anuncia la idea de un párrafo"), ("marca de pendiente", "nota entre corchetes que recuerda completar un dato"), ("fluidez", "escritura continua sin detenerse a corregir")],
  [("Del esquema al párrafo", "Punto del esquema: «Cuándo y dónde: sábado 14, 10:00, sala de artes». Escribe un párrafo de tres oraciones.",
    ["Oración temática: anuncia el tema.", "Detalles: fecha, hora y lugar.", "Cierre breve con una invitación."], "«El taller tendrá lugar el sábado 14. Comenzará a las 10:00 en la sala de artes. Los esperamos puntuales.»"),
   ("Usar una marca de pendiente", "Escribes un borrador y no recuerdas el costo de la entrada. ¿Qué haces?",
    ["No detengo la escritura.", "Anoto una marca: [buscar costo].", "Después la completo al revisar."], "Anotar [buscar costo] y seguir escribiendo")],
  [("Corregir cada palabra mientras escribes el borrador.", "Se corta la fluidez y se olvidan ideas.", "Escribe primero y corrige después."),
   ("Dejar partes del esquema sin desarrollar.", "El texto queda incompleto.", "Convierte cada punto en un párrafo.")],
  ([E("En Lenguaje: ¿Qué es un borrador?", "La primera versión completa de un texto", "Se revisa después."),
    E("¿Cuál es la parte que presenta el asunto: inicio, desarrollo o cierre?", "El inicio", "Introduce el tema."),
    E("¿Qué oración anuncia la idea de un párrafo?", "La oración temática", "Abre el párrafo.")],
   [E("Un borrador debe tener tres partes. ¿Cuáles son?", "Inicio, desarrollo y cierre", "Es la estructura básica."),
    E("Esquema con 5 puntos. Tu borrador tiene párrafos para 3. ¿Cuántos puntos quedan sin desarrollar?", "2", "Se restan los desarrollados del total."),
    E("¿Qué conector sirve para el final de un texto: finalmente o primero?", "Finalmente", "Marca el cierre.")],
   [E("Elige la oración temática del párrafo sobre el horario: (a) «El taller tendrá dos horarios para que todos puedan asistir.» (b) «Hoy hace sol.» (c) «Pedro llevó pan.»", "(a)", "Anuncia la idea del párrafo."),
    E("Borrador: «Queremos invitarlos al taller. Será el sábado. Habrá materiales». ¿Qué le conviene agregar para completarlo? (a) Un cierre que invite y agradezca. (b) Otra fecha distinta. (c) Un chiste sobre el clima.", "(a)", "No termina con una despedida ni una invitación final."),
    arith("Un borrador tiene 1 párrafo de inicio, 3 de desarrollo y 1 de cierre. ¿Cuántos párrafos tiene en total?", "1+3+1", "Se suman los párrafos de cada parte.", " párrafos")],
   [E("Un estudiante escribe su borrador deteniéndose 10 minutos en una sola tilde. ¿Qué consecuencia tiene?", "Pierde el hilo de las ideas", "La fluidez ayuda a terminar."),
    E("Un párrafo habla de la fecha, del clima y de las ganas del autor. ¿Qué problema tiene?", "Mezcla varias ideas", "Un párrafo debe tratar una idea.")],
   [E("Ordena las partes de un borrador de invitación: a) cierre con invitación, b) saludo y asunto, c) datos de fecha y lugar, d) qué se hará. Escribe las letras en orden.", "b, d, c, a", "Va de la presentación a la despedida."),
    E("En un borrador falta la hora y escribiste [buscar hora]. ¿Qué haces antes de entregarlo?", "Buscar el dato y reemplazar la marca", "La marca solo es un recordatorio.")]),
  [E("Debes escribir una invitación de tres párrafos para una exposición de dibujos. Tu esquema: 1. Presentación; 2. Lugar y hora; 3. Cierre. ¿Cuántos párrafos tendrá tu borrador?", "3", "Uno por punto del esquema.")],
  [E("¿Qué se hace con una duda ortográfica mientras escribes el borrador?", "Se subraya y se sigue escribiendo", "Se corrige después."),
   E("¿Un borrador es la versión final?", "No", "Se revisa y se edita."),
   E("¿Qué parte cierra el texto?", "El cierre", "Resume o pide algo.")],
  ("Con este esquema escribe un borrador completo de una invitación (tres párrafos): 1. Presentación: feria del libro del curso. 2. Datos: viernes 20, 15:00, patio central; habrá cuentos y libros usados. 3. Cierre: invitar y agradecer. Usa al menos dos conectores y una marca de pendiente si falta un dato.",
   "Queremos invitarlos a la feria del libro de nuestro curso. Primero habrá cuentos y, además, se podrán intercambiar libros usados. Será el viernes 20 a las 15:00 en el patio central. [buscar costo de entrada]. Finalmente, los esperamos para compartir. Gracias.",
   ["tres partes completas", "usa conectores", "sigue el esquema"], ["borrador de tres párrafos"],
   ["omitir el cierre", "corregir mientras escribe y no terminar"], "Lee tu borrador en voz alta y marca dónde necesitas más información."),
  "Convierte una idea de tu esquema en un párrafo de tres oraciones.",
  "Escribe el borrador de un correo a un compañero para invitarlo a estudiar.")

# ================================================================== clase 4
BORR = "Borrador de ejemplo: «Queremos pedir que el colegio abra la biblioteca en la tarde. Hoy cierra a las 13:00 y 120 estudiantes se quedan sin leer. Mi perro se llama Bruno. Además, a las 15:00 hay talleres sin libros. Por eso solicitamos abrirla de 14:00 a 17:00. Mañana llueve.»"
L(OA, 4,
  "Este cuaderno y un lápiz. El borrador de ejemplo está escrito en los ejercicios.",
  "Aprenderé a revisar un borrador para comprobar que la información sea pertinente y que las ideas avancen en un orden claro (progresión).",
  ["Sé escribir un borrador completo.", "Sé qué es una idea principal."],
  ["Revisar es releer el borrador con ojos de lector para mejorarlo. La primera revisión mira el contenido: ¿cada idea es pertinente al propósito y al destinatario? ¿falta información importante? ¿hay datos repetidos? Para decidir, haz tres marcas: tachar lo que no aporta, subrayar lo que falta completar y numerar el orden correcto de las ideas.",
   "La progresión es el avance de las ideas: cada oración agrega algo nuevo y se conecta con la anterior. Hay problemas de progresión cuando el texto da saltos, se repite sin aportar o salta de un tema a otro sin conexión. Una buena progresión suele seguir un orden: causa a efecto, problema a solución, general a particular o cronológico.",
   "Para revisar con método, lee en voz alta y pregúntate después de cada oración: ¿qué dice de nuevo?, ¿con qué se conecta?, ¿es necesaria? Pide también a otra persona que lea y diga qué entendió. Si no entiende lo que querías, el problema no está en el lector sino en el texto."],
  [("pertinencia", "relación de una idea con el propósito y el destinatario"), ("progresión", "avance ordenado de las ideas de un texto"), ("repetición innecesaria", "idea dicha de nuevo sin aportar"), ("salto", "paso brusco de una idea a otra sin conexión"), ("revisión de contenido", "relectura para mejorar las ideas antes de corregir la forma")],
  [("Quitar lo que no aporta", f"{BORR} ¿Qué oraciones no son pertinentes?",
    ["El propósito es pedir que se abra la biblioteca en la tarde.", "«Mi perro se llama Bruno» no aporta.", "«Mañana llueve» no aporta."], "«Mi perro se llama Bruno» y «Mañana llueve»"),
   ("Revisar la progresión", f"{BORR} Ordena las ideas pertinentes: (a) petición, (b) problema con dato, (c) motivo adicional.",
    ["El problema va primero: cierra a las 13:00 y 120 estudiantes se quedan sin leer.", "Luego el motivo adicional: hay talleres sin libros.", "Al final, la petición: abrirla de 14:00 a 17:00."], "b, c, a")],
  [("Dejar información que no aporta por temor a quitar.", "El texto pierde foco.", "Si no sirve al propósito, se tacha."),
   ("Revisar solo la ortografía.", "No se mejoran las ideas.", "Revisa primero el contenido.")],
  ([E(f"{BORR} ¿Qué pide el borrador?", "Que se abra la biblioteca en la tarde", "Lo dice en la primera oración."),
    E("¿Qué es la progresión de un texto?", "El avance ordenado de sus ideas", "Cada idea aporta algo nuevo."),
    E("¿Una oración que repite lo dicho sin aportar es necesaria?", "No", "Es una repetición innecesaria.")],
   [E(f"{BORR} ¿Qué dato muestra el problema?", "120 estudiantes se quedan sin leer porque cierra a las 13:00", "Es el dato que justifica el pedido."),
    E("Un lector dice «no sé por qué se pide esto». ¿Qué falta?", "Una razón o dato que justifique", "Hay un problema de contenido."),
    E("Tachar, subrayar y numerar son marcas de... ¿revisión de contenido o de ortografía?", "Revisión de contenido", "Ayudan a decidir qué mantener y qué ordenar.")],
   [arith(f"{BORR} La biblioteca abriría de 14:00 a 17:00. ¿Cuántas horas estaría abierta en la tarde?", "17-14", "Se resta la hora de apertura a la de cierre.", " horas"),
    E("Texto: «Pido pintar el mural. Por eso hay que comprar pintura. Pido pintar el mural. El mural es importante». ¿Qué problema de progresión tiene?", "Repite la misma idea", "No avanza ni aporta datos nuevos."),
    E("Ordena: a) Por eso pido un techo, b) La cancha se moja cuando llueve, c) Hoy 40 estudiantes no pueden jugar. Escribe las letras en orden.", "b, c, a", "Del problema a la petición.")],
   [E(f"{BORR} Un estudiante propone dejar «Mi perro se llama Bruno» porque es simpático. ¿Es correcto?", "No; no aporta al propósito", "La simpatía no justifica incluirlo."),
    E("Un borrador salta de la biblioteca al casino sin conectar. ¿Qué problema es?", "Un salto en la progresión", "Falta conexión entre ideas.")],
   [E("Falta información en: «Pido que se arregle el baño». ¿Qué dato faltaría para el destinatario? (a) Cuál baño y qué falla tiene (b) Una anécdota sobre el último recreo (c) Un comentario sobre el clima", "(a)", "Sin eso no puede actuar."),
    arith("Un borrador tiene 10 oraciones: 2 no pertinentes y 1 repetida. ¿Cuántas oraciones útiles quedan?", "10-2-1", "Se restan las no pertinentes y las repetidas.", " oraciones")]),
  [E("Revisas tu invitación a una feria y descubres una oración sobre tu videojuego favorito. ¿Qué haces?", "La tacho porque no es pertinente", "No aporta a la invitación.")],
  [E("¿Qué mira la primera revisión: el contenido o la ortografía?", "El contenido", "Se ordenan las ideas antes de corregir la forma."),
   E("¿Qué es un salto en la progresión?", "Un paso brusco de una idea a otra sin conexión", "Dificulta la comprensión."),
   E("¿Quién puede ayudarte a ver lo que no funciona?", "Un lector que dice qué entendió", "Ve el texto desde afuera.")],
  ("Revisa este borrador de ejemplo: «Quiero pedir que el patio tenga más bancas. Hoy hay 6 para 300 estudiantes. Mi cuaderno es azul. Por eso muchos se sientan en el suelo. Hoy comí pan. Pido instalar 10 bancas nuevas». Tacha lo que no aporta, ordena las ideas y escribe la versión revisada.",
   "Tacho «Mi cuaderno es azul» y «Hoy comí pan». Versión revisada: Quiero pedir que el patio tenga más bancas. Hoy hay 6 para 300 estudiantes. Por eso muchos se sientan en el suelo. Pido instalar 10 bancas nuevas.",
   ["tacha las oraciones no pertinentes", "mantiene el orden problema, consecuencia, petición", "reescribe sin saltos"], ["versión revisada"],
   ["tachar datos útiles", "mantener oraciones sin aporte"], "Pide a alguien que lea la versión revisada y diga qué se pide."),
  "Lee un texto tuyo y tacha una oración que no aporte.",
  "Escribe un borrador con dos oraciones no pertinentes para que otra persona las encuentre.")

# ================================================================== clase 5
RECURSO = "«Ayer la brigada prepara el afiche. La brigada, que tenían dos borradores, lo mostraron: “Falta la fuente” dijo Inés. Después el equipo había corregido el afiche y mañana lo presentó.»"
L(OA, 5,
  "Este cuaderno y un lápiz. Los textos y las oraciones están escritos en los ejercicios.",
  "Aprenderé a mejorar la cohesión, el vocabulario y la corrección gramatical de un texto: conectores, palabras precisas, concordancia, participios irregulares y pronombres.",
  ["Sé revisar contenido y progresión.", "Sé qué es un verbo y un sustantivo."],
  ["Una vez ordenadas las ideas, se mejora la forma. La cohesión une las oraciones: conectores (además, por eso, sin embargo), pronombres que retoman lo dicho y signos de puntuación. El vocabulario debe ser variado y preciso: en vez de «cosa» o «hacer», usa palabras exactas (documento, preparar, construir). Y se corrigen los errores gramaticales.",
   "Errores frecuentes: de concordancia, que exige que las palabras concuerden en género y número («las casas grandes», no «las casa grande»); de sujeto y verbo («los niños juegan», no «los niños juega»); de artículo y sustantivo («la mesa», no «el mesa»); y de sustantivo y adjetivo («niñas simpáticas»). También se revisan los participios irregulares: hecho, dicho, escrito, visto, puesto, roto, abierto, vuelto, resuelto (no «hacido», «escribido», «rompido», «abrido», «ponido», «vido»). Y los pronombres personales y reflexivos: «me lavé», «te lavaste», «se lavó»; «para mí», «conmigo».",
   "Para corregir, lee oración por oración, identifica el sujeto, comprueba que el verbo concuerde con él y que el tiempo verbal sea coherente con el resto del texto (no «ayer preparo»). Si una oración es confusa, léela en voz alta y reescríbela. Recuerda: corregir no es cambiar tu estilo, sino ayudar a que se entienda."],
  [("cohesión", "unión de las oraciones mediante conectores y referencias"), ("concordancia", "acuerdo de género y número entre palabras"), ("participio irregular", "forma del verbo que no sigue la regla -ado o -ido, como hecho o roto"), ("pronombre reflexivo", "pronombre como me, te o se que indica que la acción recae en quien la realiza"), ("vocabulario preciso", "palabras exactas en vez de palabras vagas")],
  [("Corregir un texto", f"Corrige: {RECURSO}",
    ["«Prepara» (presente) no concuerda con «ayer»: preparó.", "«La brigada… tenían… mostraron»: el sujeto es singular, así que el verbo también (tenía, mostró).", "«Después… había corregido» no calza con «después»: corrigió; y «mañana lo presentó» pide futuro: presentará."], "«Ayer la brigada preparó el afiche. La brigada, que tenía dos borradores, lo mostró: “Falta la fuente”, dijo Inés. Después el equipo corrigió el afiche y mañana lo presentará.»"),
   ("Participios y reflexivos", "Corrige: «Yo ya he escribido la carta y me han rompido el lápiz. Ella se lavé las manos».",
    ["«Escribido» es incorrecto: escrito.", "«Rompido» es incorrecto: roto.", "«Ella se lavé» no concuerda: se lavó."], "«Yo ya he escrito la carta y me han roto el lápiz. Ella se lavó las manos.»")],
  [("Confiar en que un participio regular sirve siempre.", "Hay formas irregulares como hecho o roto.", "Memoriza los participios irregulares frecuentes."),
   ("Cambiar el tiempo verbal sin razón.", "Confunde cuándo ocurre cada acción.", "Mantén la coherencia temporal.")],
  ([E("«Los niños juega en el patio.» ¿Qué palabra corriges y cómo?", "Juega → juegan", "El verbo debe concordar con «los niños»."),
    E("¿Cuál es el participio correcto de «romper»: rompido o roto?", "Roto", "Es participio irregular."),
    E("¿Cuál es el participio correcto de «escribir»: escribido o escrito?", "Escrito", "Es un participio irregular.")],
   [E("«Las casa son grandes.» ¿Qué corriges?", "Las casas", "El sustantivo debe concordar con el artículo en plural."),
    E("Completa «El afiche está ___». Elige el participio correcto: (a) hecho (b) hacido (c) hacedo", "(a)", "Hecho es el participio irregular de hacer."),
    E("«Para mi, fue difícil.» ¿Qué se corrige: la tilde o el verbo?", "La tilde: para mí", "El pronombre personal lleva tilde.")],
   [E("Corrige: «Ayer mi hermana llega tarde y se pone nerviosa».", "Ayer mi hermana llegó tarde y se puso nerviosa", "El pasado concuerda con «ayer»."),
    E("Completa «Ven ___». Elige el pronombre correcto: (a) con mí (b) conmigo (c) con yo", "(b)", "Conmigo es la forma correcta."),
    E("Completa «Las niñas son ___». Elige el adjetivo que concuerda: (a) simpático (b) simpáticas (c) simpática", "(b)", "Concuerda en género y número con «niñas».")],
   [E("«Los profesores revisó los trabajos.» ¿Es un error de sujeto y verbo o de artículo y sustantivo?", "De sujeto y verbo", "Debe ser «revisaron»."),
    E("Cambia la palabra vaga por una precisa en: «Hice una cosa para la feria». ¿Cuál es más precisa? (a) Construí un puesto para la feria. (b) Hice algo. (c) Hubo cosa.", "(a)", "Nombra qué se hizo."),
    E("Un compañero dice «Voy a corregir mi estilo para escribir igual que todos». ¿Corregir es lo mismo que uniformar?", "No", "Corregir ayuda a entender sin quitar la voz propia.")],
   [E("Corrige: «Había abrido la puerta y no la ha vuelto a cerrar». ¿Qué participios cambias?", "Abrido → abierto", "Abierto es el participio correcto."),
    arith("Un texto tiene 12 errores: 5 de concordancia, 3 de participios y el resto de tilde. ¿Cuántos son de tilde?", "12-5-3", "Se restan los otros dos tipos del total.", " errores")]),
  [E("Tu correo al director dice: «Los estudiantes ha hecho una propuesta que fue escribido por nosotros». ¿Cuál es la versión correcta?", "Los estudiantes han hecho una propuesta que fue escrita por nosotros", "Corrige concordancia y participio.")],
  [E("¿Cuál es el participio de «ver»?", "Visto", "Es un participio irregular, no «vido»."),
   E("¿Con qué palabra debe concordar el verbo en número y persona?", "Con el sujeto", "El verbo se ajusta al sujeto de la oración."),
   E("¿Qué participio irregular corresponde a «poner»?", "Puesto", "Es la forma irregular.")],
  ("Corrige este texto de ejemplo: «Ayer mis amigos y yo fue al parque. Las niñas estaba contentos y habían corrido mucho. Yo me lave las manos y he hacido un dibujo». Reescríbelo corregido y subraya cinco cambios.",
   "Ayer mis amigos y yo fuimos al parque. Las niñas estaban contentas y habían corrido mucho. Yo me lavé las manos y he hecho un dibujo. Cambios: fuimos, estaban, contentas, lavé, hecho.",
   ["corrige concordancia", "corrige el participio", "ajusta el pretérito"], ["texto corregido y lista de cambios"],
   ["dejar errores", "cambiar el sentido"], "Léelo en voz alta para comprobar que suene natural."),
  "Escribe tres participios irregulares con una oración cada uno.",
  "Revisa un texto tuyo y busca dos errores de concordancia.")

# ================================================================== clase 6
L(OA, 6,
  "Este cuaderno y un lápiz. Los textos y listas están escritos en los ejercicios.",
  "Aprenderé a editar el formato y la ortografía de un texto y a preparar la versión final, usando de manera eficaz las herramientas del procesador de textos.",
  ["Sé revisar contenido y gramática.", "Sé reconocer palabras agudas, graves y esdrújulas."],
  ["Editar es la última etapa del proceso: cuidar la ortografía y presentar bien el texto. En ortografía repasa las reglas de acentuación. Las palabras agudas (acento en la última sílaba) llevan tilde si terminan en n, s o vocal: canción, café. Las graves (acento en la penúltima) llevan tilde si terminan en consonante que no sea n ni s: árbol, lápiz. Las esdrújulas (acento en la antepenúltima) siempre llevan tilde: música, rápido. También revisa las mayúsculas, la puntuación y los grupos b/v.",
   "El procesador de textos ayuda a presentar el texto. Algunas herramientas útiles son: elegir una letra legible y de tamaño adecuado, ajustar el interlineado, alinear el texto, poner un título destacado, usar sangría o separar los párrafos, activar el corrector ortográfico (ayuda, pero no detecta todos los errores: «sabana» y «sábana» son palabras válidas), usar la vista previa e imprimir o guardar el archivo con un nombre claro.",
   "Antes de entregar la versión final haz una lista: ¿cumple el propósito?, ¿el registro es adecuado?, ¿tiene título y nombre del autor?, ¿corregí tildes, puntuación y mayúsculas?, ¿el formato se ve ordenado?, ¿guardé una copia? Revisa también leyendo el texto de atrás hacia adelante para detectar errores de escritura."],
  [("edición", "última revisión de ortografía y formato"), ("aguda", "palabra con acento en la última sílaba"), ("grave", "palabra con acento en la penúltima sílaba"), ("esdrújula", "palabra con acento en la antepenúltima sílaba"), ("interlineado", "espacio entre líneas de un texto")],
  [("Poner tildes", "¿Llevan tilde «lapiz», «musica» y «cancion»? Explica.",
    ["«Lápiz» es grave y termina en z: lleva tilde.", "«Música» es esdrújula: lleva tilde.", "«Canción» es aguda terminada en n: lleva tilde."], "Sí, las tres: lápiz, música y canción"),
   ("Revisar el formato", "Un texto está en letra tamaño 8, con todas las líneas pegadas y sin título. ¿Qué mejoras haces en el procesador de textos?",
    ["Subo el tamaño de letra a uno legible.", "Ajusto el interlineado para que respire.", "Agrego un título destacado."], "Letra legible, interlineado ajustado y título")],
  [("Confiar solo en el corrector automático.", "No detecta palabras bien escritas pero mal usadas.", "Relee tú mismo el texto."),
   ("Entregar sin guardar una copia.", "Si el archivo falla, pierdes el trabajo.", "Guarda con un nombre claro y haz una copia.")],
  ([E("«Árbol» ¿es aguda, grave o esdrújula y lleva tilde?", "Grave terminada en consonante distinta de n y s; lleva tilde", "El acento está en la penúltima sílaba y termina en l."),
    E("«Café» ¿lleva tilde por ser aguda terminada en vocal?", "Sí", "Las agudas terminadas en vocal llevan tilde."),
    E("«Cancion» o «canción»: ¿cuál es la correcta?", "Canción", "Es aguda terminada en n.")],
   [E("¿Llevan tilde todas las esdrújulas?", "Sí", "Siempre llevan tilde."),
    E("«Lapiz» o «lápiz»: ¿cuál es correcta?", "Lápiz", "Es grave terminada en z."),
    E("«Sabana» y «sábana» son palabras distintas. ¿Puede el corrector detectar cuál debías usar?", "No siempre", "Ambas están bien escritas y dependen del sentido.")],
   [E("Pon las tildes que faltan: «El telefono de Pedro es util». Escribe la oración correcta.", "El teléfono de Pedro es útil", "Teléfono es esdrújula y útil es grave terminada en l: ambas llevan tilde."),
    E("¿Qué herramienta ayuda a que las líneas no estén pegadas: el interlineado o los márgenes?", "El interlineado", "Controla el espacio entre líneas; los márgenes miden los bordes de la hoja."),
    E("Ordena la edición final: a) guardar con un nombre claro, b) corregir tildes, c) revisar el formato. Escribe las letras en el orden más lógico.", "b, c, a", "Se corrige, se arregla el formato y se guarda.")],
   [E("Un corrector no marcó «Ayer mi hermano tubo mucha tarea», aunque querías escribir «tuvo». ¿Qué aprendes?", "Que el corrector no detecta errores de sentido", "Ambas palabras existen."),
    E("Dos estudiantes entregan el mismo texto: uno con letra legible y título; el otro, sin título y con letra de tamaño 7. ¿Cuál transmite mejor cuidado?", "El que tiene letra legible y título", "El formato también comunica.")],
   [E("Pon tildes: «El camion lleva musica y cancion». Escribe la oración correcta.", "El camión lleva música y canción", "Camión y canción son agudas en n; música es esdrújula."),
    arith("Tienes una lista de verificación de 8 puntos y marcaste 6. ¿Cuántos faltan?", "8-6", "Se resta lo cumplido del total.", " puntos")]),
  [E("Vas a entregar un correo a la directora. Tu lista dice: título, tildes, mayúsculas y guardado. Ya revisaste las tildes y el título. ¿Cuántos puntos te faltan por revisar?", "2", "Faltan mayúsculas y guardado.")],
  [E("¿Qué tilde lleva una palabra esdrújula?", "Siempre lleva tilde", "Es la regla general."),
   E("¿El corrector ortográfico revisa todos los errores?", "No", "No detecta errores de sentido."),
   E("¿Qué archivo conviene guardar con un nombre claro?", "La versión final del texto", "Así es fácil encontrarla después.")],
  ("Edita este texto de ejemplo (agrega tildes, mayúsculas y puntuación) y describe cinco decisiones de formato para la versión final: «hoy en la biblioteca hubo una exposicion de dibujos de los alumnos de septimo y asistio la directora»",
   "Hoy, en la biblioteca, hubo una exposición de dibujos de los alumnos de séptimo y asistió la directora. Decisiones de formato: título «Exposición de dibujos», letra tamaño 12, interlineado 1,5, párrafo alineado a la izquierda y guardar con el nombre «exposicion_dibujos_final».",
   ["corrige tildes y mayúsculas", "agrega puntuación", "describe cinco decisiones de formato"], ["texto editado y lista de decisiones"],
   ["no explicar el formato", "dejar tildes sin poner"], "Compara tu versión con la de otra persona y revisa las diferencias."),
  "Escribe tres palabras esdrújulas con su tilde.",
  "Revisa la ortografía de un texto de tu casa y anota tres tildes.")

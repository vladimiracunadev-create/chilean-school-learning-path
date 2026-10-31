"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 09 (análisis crítico de medios).

Todos los textos, titulares, datos, gráficos descritos y mensajes son originales e inventados («de ejemplo»);
cada ejercicio trae escritos los datos que necesita.
Nota: los títulos de las clases del repositorio son específicos del eje (género, hechos y opiniones, propósitos...);
este cuaderno los sigue y reparte entre ellos los contenidos del texto del OA oficial.
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


OA = "LE07 OA 09"

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. Los textos que se analizan están escritos en cada ejercicio.",
  "Aprenderé a reconocer el género de un texto de los medios, quién lo emite (emisor) y a quién se dirige (audiencia).",
  ["Sé distinguir un texto que informa de uno que convence o entretiene.", "Sé qué es un propósito de lectura."],
  ["Los medios de comunicación (diarios, radio, televisión, sitios web y redes sociales) publican textos de distintos géneros. Una noticia cuenta un hecho reciente con datos y fuentes. Un reportaje investiga un tema con más profundidad y varias voces. Una carta al director es un texto en que un lector opina o reclama ante un medio. Un texto publicitario busca que compremos o usemos algo. Una publicación en una red social es un mensaje breve de una persona o institución a sus seguidores.",
   "El emisor es quien produce el mensaje: un periodista, un medio, una empresa, una institución o una persona. La audiencia es el grupo al que el mensaje se dirige. Para reconocerlos, busca firmas, nombres de marcas, el modo de hablar (¿tú, usted, nosotros?) y el lugar donde se publica. Un mismo hecho se escribe distinto para un diario escolar que para un diario de economía.",
   "Reconocer género, emisor y audiencia es el primer paso del análisis crítico. Antes de decidir si un texto es confiable necesitamos saber quién habla, para quién y con qué forma. El género se reconoce por rasgos que están escritos en el texto; la intención, en cambio, solo se infiere con cuidado y apoyándose en pistas."],
  [("género", "tipo de texto de los medios, como noticia, reportaje o carta al director"), ("emisor", "quien produce y publica el mensaje"), ("audiencia", "grupo de personas al que se dirige el mensaje"), ("titular", "título llamativo con que se presenta una noticia"), ("firma", "nombre de quien escribe un texto")],
  [("Reconocer el género", "«Este sábado se inauguró la biblioteca del barrio Las Palmas, que tiene 4.000 libros, informó la directora Carmen Soto.» ¿Qué género es?",
    ["Cuenta un hecho reciente: una inauguración.", "Incluye un dato (4.000 libros) y cita a una fuente (la directora).", "No pide comprar ni opina: informa."], "Es una noticia"),
   ("Emisor y audiencia", "«¡Tus zapatillas Rayo, ahora con 30 % de descuento! Compra en nuestra tienda hasta el domingo.» ¿Quién es el emisor y a quién se dirige?",
    ["Usa exclamaciones y una orden (compra): busca vender.", "Nombra la marca Rayo y habla en nombre de «nuestra tienda»: el emisor es la tienda.", "Dice «tus» y «compra»: se dirige a posibles compradores."], "Texto publicitario; emisor: la tienda; audiencia: posibles compradores")],
  [("Pensar que todo texto con cifras es una noticia.", "Una publicidad también puede traer cifras (como el 30 % de descuento), pero su fin es vender.", "Mira quién emite el texto y qué pide al lector."),
   ("Confundir emisor y audiencia.", "Se piensa en quién lee y no en quién produce el mensaje.", "Pregunta: ¿quién lo dice? (emisor) y ¿para quién lo dice? (audiencia).")],
  ([E("«Señor director: le escribo para pedir que se arregle el alumbrado de la calle Los Olmos. Atentamente, Julia Rojas.» ¿Qué género es: carta al director, noticia o publicidad?", "Carta al director", "Se dirige a un director, hace un pedido y termina con firma de una lectora."),
    E("En la carta «Señor director: le escribo para pedir que se arregle el alumbrado de la calle Los Olmos. Atentamente, Julia Rojas.», ¿quién es el emisor?", "Julia Rojas, la lectora que firma", "Quien firma y escribe el mensaje es su emisora."),
    E("Un diario escribe una nota para quienes lo leen. A ese grupo de lectores, ¿se le llama emisor o audiencia?", "Audiencia", "La audiencia es quien recibe el mensaje.")],
   [E("Publicación: «Ayer terminamos de pintar el mural del patio. ¡Gracias a las 15 personas que ayudaron! Mañana subiremos fotos. Centro de Estudiantes.» ¿Quién es el emisor?", "El Centro de Estudiantes", "El mensaje está firmado por esa organización."),
    E("¿Qué distingue a un reportaje de una noticia breve del día?", "Que investiga un tema con más profundidad y varias voces", "El reportaje amplía y profundiza, mientras la noticia cuenta un hecho puntual."),
    E("Aviso: «Si tienes entre 12 y 14 años, inscríbete en nuestro taller de robótica. Cupos limitados.» ¿A qué audiencia se dirige?", "A personas de 12 a 14 años", "El propio texto indica ese rango de edad.")],
   [E("Clasifica estos tres textos por su género. 1) «Compra tu entrada hoy y vive la mejor función del año.» 2) «Un equipo de cuatro estudiantes ganó la feria de ciencias, informó la profesora Ana Muñoz.» 3) «Señor director: opino que los recreos deberían durar diez minutos más.» Escribe el género de 1, 2 y 3.", "1 publicidad; 2 noticia; 3 carta al director", "1 pide comprar, 2 cuenta un hecho con fuente y 3 opina ante un director."),
    E("Una periodista conversa durante una semana con vendedores de una feria y publica un texto largo con cuatro voces y datos. ¿Qué género es?", "Reportaje", "Investiga un tema con varias voces y mayor extensión."),
    E("El cierre de una piscina municipal se cuenta en dos textos: uno para un diario infantil y otro para un diario de negocios. ¿Qué cambia: el hecho o la audiencia?", "La audiencia; el hecho es el mismo", "Se ajusta el modo de contarlo al público al que se escribe.")],
   [E("Julio lee «Las mejores mochilas del país son las Cumbre. ¡Llévala hoy!» y dice: «Es una noticia porque da una afirmación». ¿Tiene razón?", "No; es publicidad porque nombra una marca y pide comprar", "Una noticia informa un hecho; este texto promueve un producto."),
    E("Publicación firmada por «Municipalidad de Valle Claro»: «Vecinas y vecinos: mañana habrá corte de agua de 9 a 13 horas». ¿Quién es el emisor y quién la audiencia?", "Emisor: la municipalidad; audiencia: vecinas y vecinos", "El emisor es quien firma y la audiencia es a quienes se dirige el saludo.")],
   [E("Una carta al director se publica en el diario. Además del director, ¿quién más puede leerla?", "Los demás lectores del diario", "Al publicarse, la carta llega a toda la audiencia del medio."),
    E("Publicación: «Fotos del paseo al parque: ¡un día increíble! @septimob». Escribe su género y su emisor.", "Publicación en red social; emisor: el curso séptimo B", "Es un mensaje breve de una cuenta de un curso.")]),
  [E("Tu curso quiere pegar en el diario mural un mensaje que invita a limpiar el patio de 11:00 a 12:00. El mensaje es para estudiantes de 5.º a 8.º. ¿Quién es el emisor y quién la audiencia?", "Emisor: tu curso; audiencia: estudiantes de 5.º a 8.º", "Tu curso produce el mensaje y los cursos nombrados lo reciben.")],
  [E("En análisis de medios, ¿qué es la audiencia?", "El grupo al que se dirige el mensaje", "Es quien recibe el texto, no quien lo escribe."),
   E("¿Qué género busca que el lector compre o use algo?", "El texto publicitario", "Su fin es promover un producto o servicio."),
   E("¿Qué dato ayuda más a reconocer al emisor de un texto: la firma o el titular?", "La firma", "La firma o la marca indican quién emite el mensaje; el titular solo anuncia el tema.")],
  ("Analiza uno de estos tres textos. A: «Se abrió la inscripción al campeonato escolar de básquetbol; participan 12 colegios, informó el profesor Iván Peña.» B: «¡Prueba el yogur Lomas con frutas reales! Solo en tu supermercado.» C: «Señor director: la micro 52 pasa cada 40 minutos y los estudiantes llegamos tarde. Rocío Vera.» Escribe su género, su emisor, su audiencia y una pista del texto que lo demuestre.",
   "Texto B: texto publicitario. Emisor: la marca Lomas. Audiencia: personas que compran en supermercados. Pista: «Prueba» es una orden para consumir y nombra el producto.",
   ["indica un género correcto", "nombra emisor y audiencia", "cita una pista escrita en el texto"], ["cuadro con las cuatro respuestas en el cuaderno"],
   ["confundir emisor con audiencia", "dar una pista que no está en el texto"], "Compara tu análisis con el de otra persona y revisa si usaron la misma pista."),
  "Elige un texto breve de una revista, un envase o un afiche de tu casa y anota su género y su audiencia.",
  "Escribe el mismo hecho (por ejemplo, un corte de luz) como noticia para un diario escolar y como mensaje de una empresa eléctrica a sus clientes.")

# ================================================================== clase 2
L(OA, 2,
  "Este cuaderno y un lápiz. Las oraciones que se analizan están escritas en cada ejercicio.",
  "Aprenderé a distinguir los hechos de las opiniones en textos de los medios y a separar ambos cuando vienen mezclados.",
  ["Sé reconocer el género, el emisor y la audiencia de un texto.", "Sé qué es un adjetivo."],
  ["Un hecho es algo que se puede comprobar: una cifra, una fecha, una acción que se puede observar o medir. «El patio mide 20 metros de largo» es un hecho, porque alguien puede tomar una huincha y verificarlo. Una opinión es una valoración personal: dice lo que alguien piensa o siente, como «el patio es horrible». No se mide; se discute.",
   "Las opiniones suelen traer pistas: adjetivos valorativos (mejor, peor, injusto, hermoso), expresiones como «creo que» o «me parece», y palabras como lamentablemente o por suerte. Los hechos traen números, nombres, fechas y lugares. Ojo: una opinión puede apoyarse en un hecho, y un mismo texto puede mezclar ambos. En una oración mixta conviene separar la parte comprobable de la valoración.",
   "Que un experto o una autoridad diga algo no convierte su opinión en hecho. Es un hecho que la persona lo dijo; lo que dijo puede seguir siendo una valoración. Por eso, al leer medios, preguntamos: ¿cómo se podría comprobar esto? Si hay una forma de comprobarlo, es un hecho; si solo se puede compartir o rechazar, es una opinión."],
  [("hecho", "información que se puede comprobar con datos, mediciones u observación"), ("opinión", "valoración personal que no se puede comprobar como un dato"), ("adjetivo valorativo", "palabra que expresa un juicio, como pésimo o hermoso"), ("verificar", "comprobar si algo es verdadero"), ("oración mixta", "oración que combina un hecho y una opinión")],
  [("Separar hecho y opinión", "Un titular dice: «La plaza necesita más sombra» y el texto agrega: «12 de las 20 bancas reciben sol al mediodía; es el peor lugar para esperar». ¿Qué es hecho y qué es opinión?",
    ["«12 de las 20 bancas reciben sol al mediodía»: se puede comprobar contando las bancas a esa hora.", "«Es el peor lugar para esperar»: «peor» es un juicio personal.", "«La plaza necesita más sombra» es una postura que se apoya en el dato."], "Hecho: 12 de 20 bancas reciben sol; opinión: es el peor lugar para esperar"),
   ("Oración mixta", "«Lamentablemente, el nuevo horario de la biblioteca, que cierra a las 18:00, es absurdo.» Sepáralo en hecho y opinión.",
    ["Busca lo comprobable: la biblioteca cierra a las 18:00.", "Busca las valoraciones: «lamentablemente» y «absurdo».", "Escribe cada parte por separado."], "Hecho: la biblioteca cierra a las 18:00; opinión: es lamentable y absurdo")],
  [("Creer que si una oración tiene un número, es un hecho.", "El número puede usarse dentro de una valoración, como en «tres horas de tarea son una crueldad».", "Pregunta qué parte se puede comprobar y qué parte es un juicio."),
   ("Pensar que lo dicho por una autoridad es siempre un hecho.", "Es un hecho que lo dijo, pero lo que opina sigue siendo opinión.", "Separa «dijo que» de lo que afirma y pregunta cómo comprobarlo.")],
  ([E("«El gimnasio tiene 3 camarines.» ¿Es hecho u opinión?", "Hecho", "Se puede comprobar yendo a contarlos."),
    E("«El gimnasio es horrible.» ¿Es hecho u opinión?", "Opinión", "«Horrible» es un juicio personal."),
    E("¿Qué se puede hacer con un hecho que no se puede hacer con una opinión?", "Comprobarlo con datos, mediciones u observación", "Esa es la diferencia central entre ambos.")],
   [E("«Creo que el recreo es muy corto.» ¿Es hecho u opinión y cuál es la marca?", "Opinión; la marca es «creo que»", "La expresión «creo que» muestra una postura personal."),
    E("«El curso 7.º B reunió 48 kilos de papel para reciclar.» ¿Es hecho u opinión?", "Hecho", "Se puede verificar con el pesaje del papel."),
    E("«El alcalde dijo que la obra será estupenda.» ¿Qué parte es opinión?", "«Estupenda»", "Es la valoración; lo comprobable es que él lo dijo.")],
   [E("Lee: 1) «El campeonato comenzó el 12 de mayo.» 2) «Fue el mejor campeonato de la historia.» 3) «Participaron 16 equipos.» 4) «El árbitro estuvo pésimo.» 5) «El equipo ganador anotó 21 goles.» ¿Cuáles oraciones son opiniones?", "La 2 y la 4", "«El mejor» y «pésimo» son valoraciones."),
    E("¿Cuál oración transforma la opinión «La sopa del casino es asquerosa» en un dato verificable? (a) «La sopa es lo peor.» (b) «En el casino se sirvió sopa 3 veces esta semana.» (c) «Nadie quiere sopa.»", "(b)", "Una frecuencia se puede revisar en el menú; las otras dos son juicios."),
    arith("Un reportaje dice: «El 60 % de los 50 encuestados prefiere la ruta norte». ¿Cuántos encuestados la prefieren? (Un 60 % de 50 es 60 por cada 100, aplicado a 50.)", "50*60//100", "Se calcula el 60 % de 50 para convertir el porcentaje en una cantidad comprobable.", " encuestados")],
   [E("«Según el dueño, su pastelería es la más rica de la ciudad, y vendió 300 tortas en diciembre.» ¿Cuál parte se puede comprobar y cuál no?", "Se comprueba «vendió 300 tortas»; no se comprueba «la más rica»", "Las ventas tienen registro; «la más rica» depende del gusto."),
    E("Un compañero dice: «Si un experto da una opinión, ya es un hecho». ¿Es correcto?", "No; sigue siendo una valoración", "Que la diga un experto puede darle fundamento, pero no la convierte en dato.")],
   [E("«Lamentablemente, solo 3 de los 25 computadores funcionan, y eso es una vergüenza.» Escribe solo el hecho.", "Solo 3 de los 25 computadores funcionan", "Es la parte que se comprueba encendiendo los equipos."),
    arith("En un colegio de ejemplo, de 25 computadores funcionan 3. ¿Cuántos no funcionan?", "25-3", "Al total se le restan los que funcionan.", " computadores")]),
  [E("Una carta al director dice: «La biblioteca abre 5 días a la semana y su horario es incómodo». ¿Qué parte puedes verificar con el horario oficial?", "«Abre 5 días a la semana»", "Los días de apertura están en el horario; «incómodo» es una valoración.")],
  [E("En análisis de medios, ¿qué es un hecho?", "Información que se puede comprobar", "Un hecho tiene forma de ser verificado."),
   E("Escribe una palabra que suela marcar una opinión.", "Por ejemplo: peor, mejor, horrible, injusto o lamentablemente", "Son palabras que expresan un juicio personal."),
   E("¿Una oración puede tener un hecho y una opinión a la vez?", "Sí", "Es una oración mixta y conviene separar sus partes.")],
  ("Separa hechos y opiniones en este párrafo de ejemplo: «El torneo de ajedrez del colegio se jugó el jueves en la biblioteca. Participaron 18 estudiantes. Fue una jornada aburridísima, aunque la ganadora, Tamara Ortiz, jugó brillante. El premio fueron dos libros.» Haz dos columnas, una de hechos y otra de opiniones, y explica en una línea cómo comprobarías uno de los hechos.",
   "Hechos: se jugó el jueves en la biblioteca; participaron 18 estudiantes; ganó Tamara Ortiz; el premio fueron dos libros. Opiniones: «aburridísima», «brillante». Comprobaría el número revisando la lista de inscritos.",
   ["separa al menos tres hechos", "identifica las dos valoraciones", "explica una forma de comprobar un hecho"], ["dos columnas en el cuaderno"],
   ["clasificar «ganó Tamara Ortiz» como opinión", "no justificar cómo se comprueba"], "Pide a otra persona que clasifique el mismo párrafo y compara en qué oraciones difieren."),
  "Escribe dos hechos y dos opiniones sobre tu sala de clases.",
  "Elige una opinión de este cuaderno y reescríbela como dato comprobable.")

# ================================================================== clase 3
L(OA, 3,
  "Este cuaderno y un lápiz. Los textos están escritos en cada ejercicio.",
  "Aprenderé a distinguir el propósito explícito (el que el texto declara) del implícito (el que se deduce de pistas) en textos de los medios.",
  ["Sé reconocer género, emisor y audiencia.", "Sé separar hechos de opiniones."],
  ["El propósito explícito es lo que el texto dice abiertamente que quiere: informar un corte de agua, vender un producto, pedir firmas para una petición. Se reconoce en las palabras del texto. El propósito implícito es lo que el texto busca sin decirlo, por ejemplo mostrar una buena imagen de una empresa o crear la sensación de que algo se acaba pronto.",
   "Para inferir un propósito implícito necesitamos pistas observables: qué datos se eligen y cuáles se omiten, qué adjetivos se usan, qué órdenes se dan, qué emociones se provocan y cómo es el titular frente al contenido. Una inferencia es una conclusión apoyada en pistas; no es una adivinanza. Si no hay pistas, no conviene atribuir una intención a nadie.",
   "Los textos suelen tener más de un propósito a la vez. Un aviso puede informar (explícito) y a la vez quedar bien con el público (implícito). Al analizar, escribe primero lo que dice abiertamente el texto, luego tu inferencia y, al final, la pista que la respalda. Así puedes explicar tu lectura y otra persona puede revisarla."],
  [("propósito explícito", "lo que el texto declara abiertamente que busca"), ("propósito implícito", "lo que el texto busca sin decirlo y se deduce de pistas"), ("inferir", "sacar una conclusión a partir de pistas del texto"), ("pista", "palabra, dato o recurso del texto que respalda una conclusión"), ("urgencia", "sensación de que hay que actuar rápido")],
  [("Propósito en una publicidad", "«Con el jugo Sol, tus mañanas son de campeones. Disponible en tu almacén.» ¿Cuál es el propósito explícito y cuál el implícito?",
    ["Explícito: dar a conocer el jugo y dónde comprarlo («Disponible en tu almacén»).", "Implícito: asociar el producto con éxito y energía.", "Pista: la palabra «campeones» no describe el jugo, sino un logro que se asocia a él."], "Explícito: dar a conocer y vender el jugo; implícito: asociarlo con éxito; pista: «campeones»"),
   ("Propósito en una nota", "«La municipalidad invirtió 12 millones de pesos en luminarias nuevas, y por fin los vecinos podrán caminar tranquilos.» ¿Qué propósito implícito se puede inferir?",
    ["Explícito: informar sobre una inversión en luminarias.", "«Por fin» y «tranquilos» valoran la obra.", "Se infiere el propósito de mostrar una gestión positiva, aunque no es seguro: es una inferencia con pistas."], "Mostrar una buena imagen de la gestión municipal; pistas: «por fin» y «tranquilos»")],
  [("Atribuir una intención sin ninguna pista.", "Es una adivinanza y puede ser injusta con quien escribió.", "Cita siempre la palabra o recurso que respalda tu inferencia."),
   ("Creer que solo existe el propósito explícito.", "Muchos textos buscan algo más que lo que declaran.", "Pregúntate qué quedó sin decir y qué emociones busca provocar.")],
  ([E("Un afiche dice: «Dona útiles escolares hasta el viernes». ¿Cuál es su propósito explícito?", "Pedir donaciones de útiles escolares hasta el viernes", "Lo dice directamente con una orden y una fecha."),
    E("El propósito explícito, ¿se dice abiertamente o se deduce?", "Se dice abiertamente", "Esa es su definición."),
    E("Para sostener un propósito implícito, ¿qué necesitas citar?", "Una pista del texto", "La inferencia debe apoyarse en algo escrito.")],
   [E("«Nuestra marca de bicicletas, la preferida de las familias felices.» ¿Qué propósito implícito es probable?", "Asociar la marca con la felicidad familiar para vender", "La expresión «familias felices» no describe la bicicleta, sino una emoción."),
    E("«Fideos Don Ñam: 500 gramos y el sabor de la abuela.» ¿Qué expresión busca generar cariño y confianza?", "«El sabor de la abuela»", "Evoca un recuerdo afectivo, no una característica del producto."),
    E("«Solo 2 de los 10 parques de la comuna tienen juegos infantiles, informó la junta de vecinos, que pide más espacios.» ¿Qué inferencia tiene mejor respaldo? (a) Que la junta quiere más juegos infantiles. (b) Que la comuna tiene solo 2 parques. (c) Que los otros 8 parques están cerrados.", "(a)", "El texto dice que la junta «pide más espacios»; las otras no tienen pistas.")],
   [E("«Firma la petición para que la ciclovía llegue hasta el colegio.» ¿Cuál es el propósito explícito?", "Conseguir firmas para extender la ciclovía", "La orden «firma» lo declara."),
    E("«El celular Orbe se agotó en 2 horas. ¡No te quedes sin el tuyo!» ¿Qué propósito implícito se infiere?", "Crear urgencia para que se compre rápido", "Mostrar que se agotó y pedir actuar ya presiona al lector."),
    E("Un diario titula «¡Escándalo en la plaza!» y la nota cuenta que una banca fue repintada de otro color. ¿Qué propósito implícito se sospecha del titular y qué pista lo muestra?", "Llamar la atención exagerando; la pista es «escándalo», desproporcionado frente al hecho", "El hecho es menor y la palabra es muy fuerte.")],
   [E("Texto 1: «Se reunieron 120 personas en la plaza para pedir más áreas verdes.» Texto 2: «Apenas 120 personas, un puñado de vecinos, se reunieron en la plaza.» ¿Cuál texto minimiza el hecho y con qué pista?", "El texto 2, con «apenas» y «un puñado»", "Esas expresiones hacen parecer pequeño el mismo número."),
    E("Un estudiante afirma: «El propósito implícito de toda carta al director es insultar». ¿Es una inferencia bien respaldada?", "No; generaliza sin pistas del texto", "Cada texto se analiza con sus propias pistas.")],
   [E("«Aunque algunos critican el precio, nuestro gimnasio ofrece máquinas nuevas por solo $25.000 al mes.» ¿Qué propósito implícito tiene la primera parte y qué pista lo muestra?", "Responder las críticas y justificar el precio; pista: «aunque algunos critican»", "El texto se anticipa a una objeción y la contrarresta."),
    E("«Solo hoy: último día para ahorrar. Pocas unidades. ¡Corre!» ¿Cuántas expresiones crean urgencia?", "4", "Son «solo hoy», «último día», «pocas unidades» y «¡corre!».")]),
  [E("Te llega este mensaje: «Si de verdad quieres a tu curso, comparte esto con 10 contactos». ¿Qué propósito implícito se infiere y cuál es la pista?", "Presionar con culpa para que lo difundas; pista: «si de verdad quieres»", "La condición hace sentir que no compartir sería no querer al curso.")],
  [E("¿Qué propósito se deduce de pistas sin que el texto lo declare?", "El implícito", "Se infiere; no se dice abiertamente."),
   E("¿Qué debe acompañar a una inferencia sobre el propósito?", "Una pista del texto", "Sin pista sería una adivinanza."),
   E("«Compra hoy con 20 % de descuento.» ¿Cuál es el propósito explícito?", "Vender un producto con un descuento", "La orden «compra» declara el fin.")],
  ("Analiza este aviso de ejemplo: «¡Gimnasio Fuerza Total! Más de 500 socios ya cambiaron su vida. Inscríbete esta semana y no pagas matrícula. Tu mejor versión te espera.» Escribe el propósito explícito, un propósito implícito y las dos pistas que lo respaldan.",
   "Explícito: conseguir que la gente se inscriba esta semana. Implícito: hacer sentir que unirse mejora la vida y que los demás ya lo hicieron. Pistas: «500 socios ya cambiaron su vida» y «tu mejor versión te espera».",
   ["propósito explícito correcto", "un propósito implícito razonable", "dos pistas citadas del texto"], ["tres líneas escritas en el cuaderno"],
   ["no citar pistas", "confundir lo explícito con lo implícito"], "Pide a otra persona que revise si tus pistas realmente están en el texto."),
  "Busca un aviso breve de tu casa o de la calle y escribe su propósito explícito.",
  "Reescribe el aviso del gimnasio sin ningún recurso de urgencia ni presión.")

# ================================================================== clase 4
L(OA, 4,
  "Este cuaderno y un lápiz. Las imágenes y los gráficos se describen con palabras y números dentro de cada ejercicio.",
  "Aprenderé a leer imágenes, gráficos y tablas junto con el texto y a descubrir cuándo el encuadre o la escala pueden engañar.",
  ["Sé distinguir hechos y opiniones.", "Sé calcular restas y porcentajes sencillos."],
  ["Los textos de los medios son multimodales: combinan palabras con imágenes, gráficos, tablas, mapas o diagramas. Una imagen puede reforzar el texto (lo repite visualmente), ampliarlo (agrega información) o contradecirlo. El encuadre es lo que la imagen muestra y lo que deja fuera; la misma plaza puede verse llena o vacía según desde dónde se tome la foto.",
   "En un gráfico hay que mirar el título (de qué trata), los ejes (qué se mide y en qué unidades) y la escala (desde qué número parte). Si el eje vertical no parte de cero, las barras pueden exagerar una diferencia pequeña. Una tabla ordena datos en filas y columnas; un mapa muestra lugares y una leyenda explica sus símbolos; un diagrama muestra etapas o relaciones.",
   "Para evaluar, compara siempre lo que dice el texto con lo que muestran las imágenes y los datos. Pregunta: ¿qué se ve y qué queda fuera?, ¿la escala es honesta?, ¿los números del gráfico coinciden con lo que afirma el texto? Así evitas aceptar una impresión visual sin revisar la evidencia."],
  [("encuadre", "lo que una imagen incluye y lo que deja fuera"), ("gráfico", "representación visual de datos con título, ejes y escala"), ("escala", "forma en que un eje muestra los valores, indicando desde dónde parte"), ("multimodal", "texto que combina palabras con imágenes, sonidos o gráficos"), ("leyenda", "explicación de los símbolos de un mapa o gráfico")],
  [("Escala que exagera", "Un gráfico muestra los préstamos de libros: enero 80 y febrero 84. El eje vertical parte en 70. La barra de enero mide 10 unidades y la de febrero 14. ¿Qué impresión da y cuál es la diferencia real?",
    ["Con el eje desde 70, la barra de febrero parece 1,4 veces más alta que la de enero.", "La diferencia real: 84 − 80 = 4 libros.", "Cuatro libros sobre 80 es muy poco; el eje truncado exagera el aumento."], "Parece un gran aumento, pero la diferencia real es de solo 4 libros"),
   ("Encuadre de una foto", "Una foto muestra una esquina de la plaza con 9 personas apretadas; fuera del cuadro quedan las demás bancas, vacías. El titular dice: «La plaza, siempre llena». ¿Qué problema hay?",
    ["La foto muestra solo una esquina.", "Lo que queda fuera (bancas vacías) contradice el titular.", "El encuadre genera una impresión que los datos completos no respaldan."], "El encuadre muestra solo lo lleno y deja fuera lo vacío")],
  [("Mirar solo las barras sin revisar el eje.", "Un eje que no parte de cero cambia la proporción entre las barras.", "Lee siempre desde dónde parte la escala."),
   ("Creer que una foto muestra toda la realidad.", "Toda imagen tiene un encuadre que deja cosas fuera.", "Pregunta qué quedó fuera del cuadro.")],
  ([E("En un análisis de medios, ¿qué es el encuadre de una imagen?", "Lo que la imagen muestra y lo que deja fuera", "El cuadro decide qué parte de la realidad se ve."),
    E("En un gráfico, ¿qué parte indica de qué trata?", "El título", "El título anuncia el tema y los datos."),
    E("Una foto de un parque lleno de basura acompaña la frase «El parque está impecable». ¿La imagen refuerza o contradice el texto?", "Contradice el texto", "La foto muestra lo opuesto a lo que se afirma.")],
   [E("Tabla de visitas a la biblioteca: lunes 40, martes 55, miércoles 30, jueves 50. ¿Qué día tuvo más visitas?", "El martes", "55 es el valor más alto de la tabla."),
    arith("Dos barras valen 98 y 100 y el eje parte en 96. La primera mide 2 unidades y la segunda 4. ¿Cuántas veces más alta parece la segunda barra?", "4//2", "Se divide la altura dibujada de la segunda barra entre la de la primera.", " veces"),
    E("La foto de un bus muestra pasajeros de pie en el pasillo, y el texto dice «viaja cómodo y con espacio». ¿La imagen refuerza, amplía o contradice el texto?", "Contradice el texto", "Los pasajeros de pie no muestran comodidad ni espacio.")],
   [arith("De 20 bancas de una plaza, 12 reciben sol al mediodía. ¿Cuántas no reciben sol?", "20-12", "Al total se le restan las que sí reciben sol.", " bancas"),
    arith("En esa misma plaza, 12 de 20 bancas reciben sol. ¿Qué porcentaje de las bancas recibe sol? Responde solo con el número.", "12*100//20", "Se multiplica por 100 la parte y se divide entre el total.", " %"),
    E("Una foto se tomó desde un rincón donde se ve una banca con 5 personas; las otras 19 bancas, fuera del cuadro, están vacías. El titular dice «La plaza, siempre llena». ¿Qué impresión produce el encuadre?", "Que la plaza está llena aunque casi no lo está", "El cuadro excluye las bancas vacías y exagera la ocupación.")],
   [E("Un aviso dice «¡Casi el triple de vecinos!» y muestra barras de 51 y 53 con el eje partiendo en 50. ¿Es una exageración y por qué?", "Sí; el eje parte en 50 y la diferencia real es de solo 2 vecinos", "Las barras miden 1 y 3 unidades, pero los valores casi no cambian."),
    E("Una tabla indica 120 préstamos en 2023 y 150 en 2024. El texto dice «los préstamos se duplicaron». ¿Coincide con la tabla?", "No; pasaron de 120 a 150, no a 240", "Duplicar sería llegar a 240.")],
   [E("Dos gráficos muestran los mismos valores, 50 y 60. El gráfico 1 parte en 0 y el gráfico 2 parte en 40. ¿Cuál exagera la diferencia?", "El gráfico 2", "Con el eje en 40 las barras miden 10 y 20, y parecen el doble."),
    E("Una nota dice «el reciclaje creció» y su gráfico solo muestra 2 meses. ¿Qué haría más confiable el gráfico? (a) Mostrar más meses para ver la tendencia. (b) Usar un color más fuerte. (c) Agrandar el título.", "(a)", "Con más meses se vería si el crecimiento es sostenido.")]),
  [E("Quieres mostrar en tu diario mural que las visitas a la biblioteca subieron de 120 a 126 en un mes. Para ser honesto, ¿desde qué número debe partir el eje de las barras?", "Desde 0", "Solo así la altura de cada barra es proporcional a su valor.")],
  [E("¿Qué debes revisar en el eje de un gráfico antes de comparar barras?", "Desde qué número parte la escala", "Un eje truncado exagera diferencias."),
   E("Una imagen que repite lo que dice el texto, ¿refuerza o contradice?", "Refuerza", "Dice lo mismo con otro lenguaje."),
   E("¿Qué explica los símbolos de un mapa?", "La leyenda", "Indica qué significa cada símbolo.")],
  ("Analiza este caso de ejemplo. Nota: «Los accidentes bajaron en la calle Los Pinos». Tabla: 2023, 25 accidentes; 2024, 24 accidentes. Gráfico: dos barras con el eje partiendo en 22 (la de 2023 mide 3 unidades y la de 2024 mide 2). Foto: una calle vacía de noche. Escribe qué muestra cada recurso, si hay exageración o encuadre engañoso y una conclusión de dos líneas.",
   "La tabla muestra una baja de 1 accidente. El gráfico con eje desde 22 hace que la barra de 2024 parezca un tercio menor. La foto de una calle vacía de noche sugiere tranquilidad, pero no aporta datos. Conclusión: la baja existe, pero es mínima; el gráfico y la foto la hacen parecer mayor.",
   ["lee la tabla y calcula la diferencia", "detecta el eje truncado", "explica el efecto de la foto"], ["texto de cuatro a seis líneas"],
   ["no calcular la diferencia real", "creer que la foto aporta datos"], "Explica tu conclusión a otra persona y pregúntale si el eje cambiaría su impresión."),
  "Mira un gráfico o una foto en un diario de tu casa y anota qué datos entrega y qué deja fuera.",
  "Dibuja dos gráficos con los valores 30 y 36: uno honesto y uno con eje que exagera.")

# ================================================================== clase 5
L(OA, 5,
  "Este cuaderno y un lápiz. Los ejemplos son inventados y se usan solo para analizarlos; no son ideas verdaderas.",
  "Aprenderé a reconocer estereotipos y prejuicios en textos de los medios y a nombrarlos o reformularlos sin repetirlos como verdades.",
  ["Sé distinguir hechos y opiniones.", "Sé reconocer el propósito implícito de un texto."],
  ["Un estereotipo es una idea simplificada y repetida sobre un grupo de personas, por ejemplo «los adolescentes solo piensan en el celular». Un prejuicio es un juicio negativo que se hace sobre una persona o un grupo sin conocerlos. Ambos ignoran que cada persona es distinta y pueden herir o limitar oportunidades.",
   "En los medios los estereotipos aparecen en el texto y en las imágenes. Algunas señales son: palabras como todos, siempre y nunca; adjetivos fijos para un grupo; roles repartidos por sexo o edad (por ejemplo, mostrar solo a mujeres limpiando y solo a hombres en trabajos de fuerza); y casos aislados que se presentan como si valieran para todos. Un solo caso no demuestra nada sobre un grupo completo.",
   "Reconocer un estereotipo no significa repetirlo. Para analizarlo, nómbralo con tus palabras («atribuye un rol por sexo»), pregunta qué evidencia lo respalda y reformula el mensaje sin generalizar. Si un texto te hace sentir mal o te parece que humilla a alguien, puedes comentarlo con tu profesor o con una persona adulta de confianza."],
  [("estereotipo", "idea simplificada y repetida sobre un grupo de personas"), ("prejuicio", "juicio negativo sobre alguien sin conocerlo"), ("generalizar", "atribuir a todo un grupo lo que se vio en pocos casos"), ("rol", "papel o tarea que se espera de alguien"), ("reformular", "decir lo mismo de otro modo, corrigiendo un problema")],
  [("Estereotipo de roles", "Aviso de ejemplo: «Torneo de robótica: las niñas pueden sumarse al equipo de decoración y los niños al de programación». ¿Qué estereotipo hay y cómo se reformula?",
    ["Reparte tareas según el sexo: decoración para niñas, programación para niños.", "No hay evidencia de que eso dependa del sexo.", "Reformulación: «Todas las personas pueden elegir decoración o programación»."], "Asigna roles según el sexo; se corrige abriendo ambas tareas a todos"),
   ("Generalización", "Frase de ejemplo: «Los adultos mayores siempre se quejan de todo». ¿Qué la hace un prejuicio y cómo se corrige?",
    ["Usa «siempre» y «todo»: generaliza.", "Atribuye una mala cualidad a todo un grupo.", "Se corrige con datos concretos: «Esta semana, vecinos mayores presentaron 3 reclamos»."], "Es un prejuicio porque generaliza; se corrige con datos concretos y limitados")],
  [("Pensar que mencionar un estereotipo para criticarlo es repetirlo.", "Se puede nombrar su idea con palabras propias sin copiar el insulto ni darlo por cierto.", "Describe qué asume el texto y por qué no tiene respaldo."),
   ("Creer que un caso demuestra algo sobre todo un grupo.", "Un caso aislado no representa a miles de personas distintas.", "Pregunta cuántos casos hay y quién los mide.")],
  ([E("«Todos los adolescentes viven pegados al celular.» ¿Qué palabra generaliza?", "Todos", "Atribuye lo mismo a todo un grupo."),
    E("«Marta es la capitana del equipo de fútbol del curso.» ¿Es un estereotipo?", "No; describe a una persona concreta", "No generaliza sobre un grupo, es un dato sobre una persona."),
    E("En medios, ¿qué es un prejuicio?", "Un juicio negativo sobre alguien o un grupo sin conocerlo", "Se forma antes de tener evidencia.")],
   [E("Un anuncio muestra solo a mujeres limpiando la casa y solo a hombres arreglando autos. ¿Qué estereotipo refuerza?", "Que la limpieza es tarea de mujeres y la mecánica de hombres", "Reparte tareas según el sexo."),
    E("¿Cuál reformula mejor «Las niñas no son buenas para las matemáticas»? (a) «Cada estudiante puede aprender matemáticas con práctica, sin importar su sexo.» (b) «Las niñas son mejores en lenguaje.» (c) «Los niños sí son buenos para matemáticas.»", "(a)", "Elimina la generalización por sexo sin reemplazarla por otra."),
    E("«Los jóvenes nunca escuchan.» ¿Qué palabra señala la generalización?", "Nunca", "Afirma que ninguno de ellos escucha jamás.")],
   [E("Lee: 1) «Los hinchas del equipo Rojo son violentos.» 2) «Sebastián llegó tarde tres veces esta semana.» 3) «Las mujeres son demasiado emotivas para dirigir.» ¿Cuáles son estereotipos o prejuicios?", "La 1 y la 3", "Generalizan sobre grupos; la 2 es un hecho sobre una persona."),
    E("«Carmen, de 72 años, aprendió a usar videollamadas en 2 semanas.» ¿Este caso apoya o contradice la frase «Los adultos mayores no pueden aprender tecnología»?", "Contradice la frase", "Muestra un caso en que sí aprendió, aunque un caso solo no cambia a un grupo entero."),
    E("«Todos los gamers son aislados, siempre están pegados a la pantalla y nunca estudian.» ¿Cuántas palabras generalizadoras hay?", "3", "Son «todos», «siempre» y «nunca».")],
   [E("Un reportero escribe «Los vecinos de ese barrio son flojos» tras ver dos sitios sin cuidar. ¿Qué error comete?", "Generaliza a todo un grupo a partir de pocos casos", "Dos sitios no representan a toda la población."),
    E("¿Por qué conviene describir un estereotipo con tus palabras en vez de copiarlo con su insulto?", "Porque repetirlo tal cual puede reforzarlo", "Al describirlo lo analizas sin darlo por cierto.")],
   [E("Elige la mejor reformulación de «Los repartidores son todos imprudentes». (a) «Algunos repartidores cometieron infracciones de tránsito.» (b) «Ningún repartidor respeta las normas.» (c) «Los repartidores son lo peor.»", "(a)", "Es limitada y no generaliza."),
    E("Una nota muestra en la foto solo a niños en el laboratorio y solo a niñas en el coro. ¿Qué estereotipo puede reforzar el encuadre?", "Que la ciencia es cosa de niños y el canto de niñas", "La imagen reparte actividades por sexo.")]),
  [E("En tu colegio un afiche dice: «Taller de cocina para las alumnas. Taller de fútbol para los alumnos». ¿Qué cambio propondrías para evitar el estereotipo?", "Invitar a todos los estudiantes a ambos talleres", "Cada persona debe poder elegir sin que el sexo decida.")],
  [E("¿Qué palabras son pistas de una generalización?", "Todos, siempre y nunca", "Aplican lo mismo a todo un grupo."),
   E("¿Un estereotipo describe a una persona concreta o a un grupo?", "A un grupo", "Es una idea simplificada sobre muchas personas."),
   E("¿Qué se hace con un texto que te parece que humilla a alguien?", "Comentarlo con un profesor o una persona adulta de confianza", "No se enfrenta solo y se pide apoyo.")],
  ("Analiza esta noticia de ejemplo: «En la feria vecinal, los hombres se encargaron de montar los toldos y las mujeres de atender a los niños; así ha sido siempre». Escribe qué estereotipo contiene, qué palabra lo delata y cómo lo reformularías.",
   "Asigna tareas según el sexo (fuerza para hombres, cuidado para mujeres). Lo delata «siempre». Reformulación: «Vecinos y vecinas montaron los toldos y cuidaron a los niños según se ofrecieron».",
   ["nombra el estereotipo sin repetir un insulto", "señala una palabra o recurso que lo delata", "propone una reformulación"], ["tres líneas escritas"],
   ["copiar el estereotipo como si fuera verdad", "reformular con otro estereotipo"], "Lee tu reformulación en voz alta y comprueba que no deje ninguna generalización."),
  "Escribe una frase con «todos» o «siempre» sobre un grupo y reescríbela con un dato concreto.",
  "Mira una publicidad de tu casa y anota qué roles muestra para mujeres y para hombres.")

# ================================================================== clase 6
L(OA, 6,
  "Este cuaderno y un lápiz. Los casos son inventados y no mencionan personas reales.",
  "Aprenderé a examinar qué efectos puede tener una información divulgada en las mujeres y los hombres de quienes se habla, y a decidir con responsabilidad si compartirla.",
  ["Sé distinguir hechos y opiniones.", "Sé reconocer estereotipos y prejuicios."],
  ["Cuando un medio o una persona publica información sobre alguien, esa persona aludida puede sufrir efectos: daño a su reputación, pérdida de privacidad, miedo, problemas en el trabajo o el colegio, incluso riesgos de seguridad. Una información falsa o sin verificar puede hacer daño aunque se corrija después. También la audiencia se ve afectada: un mensaje alarmista puede provocar miedo o decisiones apresuradas.",
   "Los efectos pueden ser distintos para mujeres y hombres cuando se activan estereotipos. Por ejemplo, un titular que destaca el sexo de una persona como si explicara un error («mujer al volante causa choque») refuerza un prejuicio. Antes de divulgar, conviene preguntarse tres cosas: ¿está verificado?, ¿es necesario nombrar o mostrar a la persona?, ¿qué podría pasarle si se publica?",
   "Un buen texto informativo cita fuentes, evita datos personales innecesarios (dirección, rostro de menores) y da espacio para responder o rectificar. Si recibes información privada o humillante sobre alguien, no la reenvíes: avisa a una persona adulta de confianza. Compartir también es publicar, y cada reenvío multiplica el efecto."],
  [("persona aludida", "persona de quien habla un texto"), ("reputación", "imagen que los demás tienen de una persona"), ("privacidad", "derecho a proteger los datos y la vida personal"), ("rectificar", "corregir públicamente un error"), ("divulgar", "dar a conocer información a muchas personas")],
  [("Rumor sin verificar", "Una publicación sin pruebas afirma: «Rodrigo Pino, vendedor de la feria, vende productos vencidos». La comparten 120 personas. ¿Qué efectos puede tener?",
    ["Afecta su reputación: los clientes pueden dejar de comprarle.", "Si es falso, el daño es injusto y difícil de reparar.", "Debió verificarse con una fuente y darle espacio para responder."], "Daño a su reputación y a sus ventas; faltó verificar y dar derecho a responder"),
   ("Datos personales", "Una nota publica el nombre, el colegio y la dirección de una joven que ganó un concurso. ¿Qué riesgo hay y cómo se evita?",
    ["Publicar la dirección expone su seguridad y su privacidad.", "El logro puede informarse sin ese dato.", "Basta con su nombre autorizado y el premio obtenido."], "Se evita publicando el logro sin la dirección ni datos innecesarios")],
  [("Pensar que compartir un rumor no es publicarlo.", "Cada reenvío lo difunde a más personas y multiplica el daño.", "Antes de reenviar, verifica y piensa en la persona aludida."),
   ("Creer que una corrección tardía repara todo.", "El primer mensaje llegó a más gente que la corrección.", "Verifica antes de publicar y rectifica con la misma visibilidad.")],
  ([E("¿Quién es la persona aludida en un texto?", "La persona de quien se habla", "Es quien aparece mencionada, aunque no escriba el texto."),
    E("Antes de compartir un rumor, ¿qué conviene hacer?", "Verificar la información", "Un rumor sin comprobar puede ser falso."),
    E("¿Es seguro publicar la dirección de la casa de una persona?", "No; expone su seguridad", "Cualquiera podría ir a ese lugar.")],
   [E("Circula el rumor «Dicen que la profesora Díaz reprobó a todo el curso», sin pruebas. ¿Qué efecto puede tener en ella?", "Daño a su reputación", "La acusan sin comprobación y otras personas la juzgan."),
    E("¿Cuáles son las tres preguntas antes de divulgar? (a) ¿Está verificado?, ¿es necesario nombrar a la persona?, ¿qué podría pasarle? (b) ¿Es divertido?, ¿cuántos likes tendrá?, ¿quién lo vio antes? (c) ¿Es corto?, ¿tiene imagen?, ¿es viral?", "(a)", "Esas preguntas protegen a la persona aludida."),
    E("Una nota cita a su fuente y da espacio a la persona aludida para responder. ¿Qué cualidad tiene?", "Equilibrio e información responsable", "Escucha a las partes y respalda lo que afirma.")],
   [arith("Una persona envía un mensaje falso a 4 contactos y cada uno lo reenvía a 4 personas nuevas (una sola ronda más). ¿Cuántas personas lo recibieron en total, sin contar a quien lo empezó?", "4+4*4", "Se suman los primeros 4 contactos y los 16 de la segunda ronda.", " personas"),
    E("¿Cuál escritura de una noticia sobre una falta escolar protege mejor a un menor de edad? (a) Con el nombre y el curso del estudiante. (b) «Un estudiante recibió una sanción por una falta». (c) Con la foto del estudiante.", "(b)", "Informa el hecho sin exponer a la persona."),
    E("Una nota sobre una vecina dice: «La señora de la casa azul de la esquina de Los Ceibos con Lingue». ¿Qué dato permite ubicarla fácilmente?", "La casa azul en la esquina de Los Ceibos con Lingue", "Describe un lugar tan preciso que identifica a la persona.")],
   [E("Titular 1: «Mujer al volante causa choque». Titular 2: «Conductora chocó por exceso de velocidad, según el parte policial». ¿Cuál puede reforzar un estereotipo sobre las mujeres?", "El titular 1", "Destaca el sexo de la conductora como si fuera la causa."),
    E("¿Una información alarmista puede afectar también a la audiencia, no solo a la persona aludida?", "Sí; puede causar miedo o decisiones apresuradas", "El mensaje cambia lo que sienten y hacen los lectores.")],
   [E("Un diario dijo que el vecino Luis Mena fue detenido, pero era otro Luis. Corrigió tres días después en una nota pequeña. ¿Qué haría mejor la reparación?", "Una rectificación rápida y con igual visibilidad que el error", "El error fue visible; la corrección también debe serlo."),
    E("Te llega por chat un mensaje privado con fotos de una compañera que no las autorizó. ¿Qué haces?", "No lo reenvío y aviso a una persona adulta de confianza", "Reenviarlo agrandaría el daño; un adulto puede protegerla.")]),
  [E("En el chat del curso alguien escribe: «Dicen que Paula copió en la prueba». No hay pruebas. ¿Qué es lo más responsable?", "No repetirlo ni reenviarlo, y avisar a un profesor si sigue circulando", "Un rumor sin pruebas puede dañar a Paula.")],
  [E("¿Qué hace más daño: compartir un rumor o verificarlo antes?", "Compartirlo", "Verificar evita difundir una información falsa."),
   E("¿Qué debes hacer si recibes información privada o humillante sobre alguien?", "No reenviarla y avisar a una persona adulta de confianza", "Así proteges a la persona aludida."),
   E("¿Qué es rectificar?", "Corregir públicamente un error", "Repara una información equivocada.")],
  ("Analiza este caso de ejemplo: un sitio de noticias publica «Joven del barrio Los Aromos, 15 años, acusada de robo en el liceo», con su foto y el nombre completo, sin hablar con ella ni con el liceo. Escribe tres efectos posibles sobre ella, qué pasos no se siguieron y cómo se podría informar mejor.",
   "Efectos: daño a su reputación, miedo y pérdida de privacidad. No se verificó, no se pidió su versión y se expuso a una menor. Mejor: informar el hecho sin nombre ni foto, con fuentes confirmadas.",
   ["tres efectos distintos", "identifica los pasos omitidos", "propone una versión más responsable"], ["texto de cuatro a seis líneas"],
   ["culpar a la persona aludida", "no mencionar la verificación"], "Léelo a otra persona y comprueba si entendió quién sale afectado."),
  "Piensa en un mensaje que hayas visto compartido y anota si estaba verificado.",
  "Escribe tres reglas personales antes de reenviar un mensaje sobre otra persona.")

# ================================================================== clase 7
NOTA = "Titular: «Los préstamos de la biblioteca barrial se disparan». Texto: en 2023 hubo 400 préstamos y en 2024, 440. El encargado, Mario Lira, dice que «es el mejor programa cultural de la comuna». Gráfico: dos barras, de 400 y 440, con el eje vertical partiendo en 380. Foto: cuatro niños sonrientes frente a estantes llenos de libros, tomada el día de la inauguración."
L(OA, 7,
  "Este cuaderno y un lápiz. La nota que se evalúa está escrita completa en los ejercicios.",
  "Aprenderé a elaborar una evaluación fundamentada de un texto de los medios, que reúna género, hechos y opiniones, propósitos, imágenes, estereotipos y efectos.",
  ["Sé analizar género, emisor y audiencia.", "Sé distinguir hechos y opiniones, propósitos, estereotipos y efectos."],
  ["Evaluar un texto de los medios es emitir un juicio sobre él, pero un juicio apoyado en evidencia. Para hacerlo ordenadamente usamos una guía de seis preguntas: 1) ¿qué género, emisor y audiencia tiene?, 2) ¿qué es hecho y qué es opinión?, 3) ¿qué propósito explícito e implícito se infiere?, 4) ¿qué dicen las imágenes y los gráficos, y qué dejan fuera?, 5) ¿hay estereotipos o prejuicios?, 6) ¿qué efectos puede tener en las personas aludidas y en la audiencia?",
   "Una evaluación fundamentada no dice solo «es bueno» o «es malo». Tiene una postura (por ejemplo, «la nota informa datos reales, pero exagera el cambio») y la respalda con al menos dos evidencias citadas del texto, como un número, una palabra o un detalle de la imagen. También reconoce lo que falta para juzgar mejor.",
   "Evita dos errores: aceptar todo sin revisar y rechazar todo sin pruebas. Si un dato está bien presentado, reconócelo. Si algo está exagerado, señala dónde y por qué. Termina con una conclusión que responda a esta pregunta: ¿qué debería tener en cuenta un lector antes de creer este texto?"],
  [("evaluación fundamentada", "juicio sobre un texto apoyado en evidencias citadas"), ("postura", "conclusión principal que sostienes"), ("evidencia", "dato, palabra o detalle del texto que respalda tu juicio"), ("criterio", "pregunta o regla que usas para evaluar"), ("tendencia", "dirección en que cambian los datos a lo largo del tiempo")],
  [("Evaluar el dossier de la plaza", "Dossier de ejemplo: titular «La plaza necesita más sombra»; dato «12 de 20 bancas reciben sol al mediodía»; opinión «es el peor lugar para esperar»; gráfico con escala truncada; foto tomada desde un solo sector. Elabora una evaluación breve.",
    ["Criterio hecho/opinión: 12 de 20 es dato comprobable; «el peor lugar» es opinión.", "Criterio imagen/gráfico: la escala truncada exagera y la foto desde un sector limita lo que se ve.", "Postura con evidencia y lo que falta: el dato respalda la necesidad de sombra, pero faltan datos de otras horas y de todo el espacio."], "La nota tiene un dato válido (12 de 20 bancas), pero la opinión y el gráfico exageran; falta información de otras horas"),
   ("Revisar una evaluación", "Un estudiante escribe: «La nota es mala porque habla de sombra». ¿Es una evaluación fundamentada? Revísala con la guía.",
    ["¿Tiene postura? Sí, pero es vaga.", "¿Cita evidencia del texto? No cita ningún dato ni palabra.", "Se mejora citando 12 de 20, la escala y la opinión."], "No; falta evidencia citada y una conclusión precisa")],
  [("Evaluar solo por si el tema nos gusta.", "El gusto personal no es un criterio y no se puede comprobar.", "Usa los seis criterios de la guía y cita evidencia."),
   ("Dar una conclusión sin cita del texto.", "Sin cita, otra persona no puede comprobar tu juicio.", "Incluye al menos dos evidencias en tu conclusión.")],
  ([E(f"Lee la nota de ejemplo. {NOTA} ¿Cuál es el hecho cuantificable que entrega?", "400 préstamos en 2023 y 440 en 2024", "Son cifras que se pueden verificar en los registros."),
    E(f"Lee la nota de ejemplo. {NOTA} ¿Qué frase es una opinión?", "«Es el mejor programa cultural de la comuna»", "«Mejor» es una valoración del encargado."),
    E(f"Nota de ejemplo: {NOTA} ¿Por qué conviene desconfiar un poco de que el encargado opine sobre su propio programa?", "Porque tiene interés en que se vea bien", "Es una parte interesada, aunque pueda tener razón.")],
   [arith("En la nota de la biblioteca hubo 400 préstamos en 2023 y 440 en 2024. ¿Cuántos préstamos más hubo en 2024?", "440-400", "Se resta la cifra de 2023 a la de 2024.", " préstamos"),
    arith("Con esos mismos datos (400 y 440 préstamos), ¿en qué porcentaje aumentaron los préstamos? Responde solo con el número.", "40*100//400", "Se divide el aumento (40) entre el valor inicial (400) y se multiplica por 100.", " %"),
    E("El gráfico de la nota tiene dos barras de 400 y 440 y el eje parte en 380. ¿Muestra el aumento mayor o igual que el real?", "Mayor que el real", "Las barras miden 20 y 60 unidades y parecen el triple.")],
   [E("En la nota, el titular dice «se disparan». ¿Es una descripción neutral o una valoración exagerada del aumento de 10 %?", "Una valoración exagerada", "«Disparar» sugiere un alza enorme y el aumento es moderado."),
    E("La foto de la nota se tomó el día de la inauguración. ¿Qué límite tiene para evaluar el uso cotidiano de la biblioteca?", "Muestra un solo día especial, no el uso habitual", "El encuadre temporal no representa lo que ocurre cada día."),
    E("¿Cuál es la evaluación mejor fundamentada de la nota? (a) «Los préstamos subieron de 400 a 440, pero el titular y el gráfico exageran un aumento de 10 %.» (b) «Es una mala nota.» (c) «Me gusta la biblioteca.»", "(a)", "Cita datos y señala dónde hay exageración.")],
   [E("Un compañero dice: «La nota miente porque dice que todo es perfecto». ¿Su crítica está bien fundamentada?", "No; los datos 400 y 440 pueden ser reales y la crítica no cita ninguna exageración concreta", "Lo cuestionable son el titular, el gráfico y la opinión; no todo el texto."),
    E("¿Qué información faltaría para saber si el programa es «el mejor» de la comuna?", "Comparar con datos de otros programas", "Sin comparación no se puede afirmar un «mejor».")],
   [E("Una evaluación revisó emisor, hechos y opiniones, propósito, gráfico y efectos. De los seis criterios de la guía, ¿cuál quedó sin revisar?", "Los estereotipos", "La guía incluye estereotipos y prejuicios como criterio 5."),
    E("En una nota, el encargado Mario Lira es citado con su opinión sobre su propio programa. ¿Es una fuente o la audiencia de esa nota?", "Una fuente", "Aporta una opinión y datos al texto; no es quien lo lee.")]),
  [E("Tu curso quiere publicar en el diario mural: «Nuestra campaña recolectó 30 kilos de pilas y fue un éxito total». Solo hay una foto de la mesa de recolección. ¿Qué evidencia agregarías para fundamentar «éxito»?", "El número de participantes o una comparación con la meta", "«Éxito» necesita un dato con qué compararse.")],
  [E("¿Con qué debe estar apoyada una evaluación fundamentada?", "Con evidencias citadas del texto", "La evidencia permite comprobar el juicio."),
   E("¿Cuántas preguntas tiene la guía de evaluación de la clase?", "Seis", "Son género, hechos y opiniones, propósito, imagen y gráfico, estereotipos y efectos."),
   E("¿Qué se escribe al final de una evaluación?", "Una conclusión sobre qué debe tener en cuenta el lector", "Cierra la evaluación con una postura.")],
  ("Evalúa esta nota de ejemplo con la guía de seis preguntas. «Titular: Las clases de natación llenan la piscina. Texto: en marzo se inscribieron 24 estudiantes y en abril 30. La profesora dice que son las mejores clases del colegio. Gráfico: dos barras con el eje partiendo en 20. Foto: un grupo sonriendo, tomada en la primera clase.» Escribe una evaluación de cinco a siete líneas con una postura y al menos dos evidencias.",
   "La nota informa un aumento real, de 24 a 30 inscritos (25 %). Sin embargo, el titular dice «llenan la piscina» sin dato de cupos, el gráfico con eje desde 20 hace que 30 parezca más del doble de 24 y «las mejores clases» es opinión de la profesora. La foto es de la primera clase. Falta saber el cupo total.",
   ["tiene una postura clara", "cita al menos dos evidencias del texto", "señala lo que falta para juzgar mejor"], ["texto de cinco a siete líneas"],
   ["no citar datos", "rechazar toda la nota sin distinguir sus partes"], "Intercambia tu evaluación con otra persona y marca si cita evidencia."),
  "Elige una publicidad de tu casa y responde dos de las seis preguntas de la guía.",
  "Aplica la guía de seis preguntas a un titular y su foto de un diario o sitio de noticias.")

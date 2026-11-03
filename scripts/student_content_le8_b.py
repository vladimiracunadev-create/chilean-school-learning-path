"""Cuaderno del estudiante, 8.º básico Lengua y Literatura, OA 09 (textos argumentativos: columnas, cartas y discursos).

Todos los textos, datos y encuestas son originales e inventados («de ejemplo»); cada ejercicio trae escritos los textos y datos que necesita.
Nota: los títulos de las clases del repositorio ordenan el OA oficial en siete pasos (postura, argumento, hecho y opinión,
evidencia, lenguaje, comparación, evaluación crítica); este cuaderno los sigue y reparte entre ellos los contenidos del OA.
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


OA = "LE08 OA 09"

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. Los textos que se analizan están escritos en cada ejercicio.",
  "Aprenderé a distinguir el tema de un texto argumentativo de la postura que el autor defiende sobre ese tema.",
  ["Sé distinguir un hecho de una opinión.", "Sé reconocer quién escribe un texto y a quién se dirige."],
  ["Un texto argumentativo busca convencer. Puede ser una columna de opinión (un texto firmado en que alguien defiende una idea en un medio), una carta al director (un lector escribe a un diario o revista) o un discurso (un texto pensado para decirse en voz alta ante un público). En los tres casos hay una persona que escribe, un público al que se dirige y un asunto sobre el que quiere influir.",
   "El tema es el asunto del que trata el texto: «los celulares en el recreo». La postura (o tesis) es lo que el autor defiende sobre ese tema: «los celulares deberían permitirse con reglas claras». Un tema puede tener posturas opuestas. La postura se reconoce por marcas como «creo que», «sostengo que», «deberíamos», «es un error», «propongo», o por verbos que piden hacer algo.",
   "Para formular una postura con fidelidad usa la fórmula «El autor sostiene que…» y completa con una oración entera, no con una palabra suelta. Una buena formulación no exagera ni agrega ideas que el autor no dijo. Un dato, como «30 estudiantes llegan atrasados», no es la postura: solo la apoya."],
  [("tema", "asunto del que trata un texto"), ("postura (tesis)", "idea que el autor defiende sobre el tema"), ("columna de opinión", "texto firmado en un medio en que una persona defiende una idea"), ("discurso", "texto preparado para decirse ante un público"), ("marca de postura", "expresión que revela lo que el autor piensa, como «creo que» o «debería»")],
  [("Postura en una columna", "«Los celulares en el patio no son el enemigo. Quien mira un mapa del metro o avisa a su casa que saldrá tarde los usa con sentido. Lo que hay que regular es el abuso, no el aparato. Por eso el colegio debería permitirlos en el recreo, con reglas claras.» ¿Cuál es el tema y cuál la postura?",
    ["El asunto común es el uso de celulares en el recreo: ese es el tema.", "La última oración dice qué defiende el autor: «debería permitirlos en el recreo, con reglas claras».", "Se formula: el autor sostiene que los celulares deben permitirse en el recreo con reglas claras."], "Tema: celulares en el recreo; postura: deben permitirse con reglas claras"),
   ("Postura en un discurso", "«Compañeras y compañeros: hoy no vengo a pedirles un favor, sino un compromiso. Si cada curso adopta un rincón del patio, en un mes tendremos un colegio más limpio. Adoptemos uno.» ¿Cuál es la postura?",
    ["El tema es el cuidado del patio.", "La marca «Adoptemos uno» y la condición «si cada curso adopta» muestran lo que se defiende.", "El autor sostiene que cada curso debe adoptar un rincón del patio."], "Cada curso debe adoptar un rincón del patio para mantenerlo limpio")],
  [("Responder solo con el tema («habla de los celulares»).", "El tema dice de qué trata el texto, pero no qué defiende el autor.", "Completa «El autor sostiene que…» con una oración entera."),
   ("Tomar un dato como si fuera la postura.", "Un dato apoya la postura, pero no dice lo que el autor propone.", "Busca la oración que pide, propone o valora algo.")],
  ([E("En «Los recreos deberían durar veinte minutos», ¿cuál es el tema y cuál la postura?", "Tema: la duración de los recreos; postura: deberían durar veinte minutos", "El tema es el asunto y la postura es lo que se defiende sobre él."),
    E("¿Qué expresión marca una postura? (a) Se inauguró ayer. (b) Sostengo que. (c) Mide tres metros.", "(b)", "«Sostengo que» introduce lo que el autor piensa."),
    E("¿El tema y la postura de un texto son lo mismo?", "No; el tema es el asunto y la postura es lo que el autor defiende sobre él", "Sobre un mismo tema pueden existir posturas opuestas.")],
   [E("«Cada vez más colegios prohíben las mochilas con ruedas. Es un error: ayudan a cargar peso a quienes tienen dolores de espalda, y prohibirlas castiga a quienes más las necesitan.» ¿Cuál es la postura?", "Prohibir las mochilas con ruedas es un error", "La valoración «es un error» muestra lo que defiende el autor."),
    E("El titular de una columna dice «Tareas para el fin de semana: ¿sí o no?». ¿Se conoce ya la postura del autor?", "No; el titular plantea el tema como pregunta y la postura se descubre al leer", "Una pregunta abierta no dice qué defiende quien escribe."),
    E("¿Qué sirve más para detectar la postura? (a) Expresiones como «debería» y «es un error». (b) La fecha de publicación. (c) El número de párrafos.", "(a)", "Las marcas valorativas y de obligación muestran lo que el autor defiende.")],
   [E("Discurso: «Amigas y amigos: el campeonato no se gana solo con goles. Se gana cuando nadie queda afuera. Por eso propongo que cada equipo incluya a una persona que nunca ha jugado.» ¿Cuál es la postura?", "Cada equipo debe incluir a una persona que nunca ha jugado", "«Propongo que» introduce lo que el orador defiende."),
    E("Carta: «Señor director: el paradero frente al liceo no tiene techo. Los días de lluvia, estudiantes esperan mojándose. Pido que se instale un refugio.» ¿Qué expresión muestra la postura?", "«Pido que se instale un refugio»", "Es la oración que dice qué solicita el autor; lo demás la justifica."),
    E("Columna: «Hay quienes dicen que leer en pantalla no es leer. Discrepo: un cuento leído en una tableta sigue siendo un cuento. Importa la comprensión, no el soporte.» ¿Cuál formulación es fiel? (a) El autor habla de pantallas. (b) El autor sostiene que leer en pantalla también es leer, porque lo importante es la comprensión. (c) El autor sostiene que las tabletas son mejores que los libros.", "(b)", "(a) solo da el tema y (c) agrega una idea que el autor no dijo.")],
   [E("Texto: «Los celulares en clase distraen, pero guardados en la mochila no hacen daño. Propongo que se usen solo en la hora de investigación.» Un estudiante resume: «El autor sostiene que los celulares son malos». ¿Es un resumen fiel?", "No; el autor acepta usarlos en la hora de investigación y propone regularlos", "El resumen exagera: el autor no condena el celular, lo limita."),
    E("Texto A: «El uniforme iguala a todos y evita burlas por la ropa. Debe mantenerse.» Texto B: «El uniforme apaga la identidad de cada estudiante. Debe ser optativo.» ¿Qué comparten y en qué se diferencian?", "Comparten el tema (el uniforme escolar) y se diferencian en la postura: mantenerlo u optativo", "Un mismo tema admite posturas distintas.")],
   [E("«No es casual que el bus de las 7:00 vaya lleno y el de las 7:30 vaya vacío: nadie quiere llegar tarde. Un horario más frecuente en la mañana no sería un lujo, sino una necesidad.» ¿Qué oración resume la postura?", "Un horario más frecuente en la mañana es una necesidad", "La última oración dice lo que el autor defiende; las primeras la apoyan."),
    E("Una columna dice: «El 40 % de los 200 estudiantes usa bicicleta. Por eso el colegio debe instalar un bicicletero». ¿La cifra es la postura o un dato que la apoya?", "Es un dato que apoya la postura; la postura es instalar un bicicletero", "La cifra se comprueba y sirve de apoyo; lo que se pide es el bicicletero.")]),
  [E("Tu centro de estudiantes publica: «Los jueves podrían ser días sin fotocopias: bastan los cuadernos». Escribe el tema y la postura.", "Tema: el uso de fotocopias; postura: los jueves deberían ser días sin fotocopias", "El tema es el asunto y la postura la idea que se defiende sobre él.")],
  [E("¿Qué es una columna de opinión?", "Un texto firmado en un medio en que una persona defiende una idea", "Su finalidad es argumentar una postura."),
   E("¿Con qué fórmula conviene formular la postura de un autor?", "«El autor sostiene que…» seguido de una oración completa", "Así se evita responder solo con el tema."),
   E("Un dato como «30 estudiantes llegan atrasados», ¿es la postura o la apoya?", "La apoya", "Un dato respalda la tesis, pero no dice qué se propone.")],
  ("Lee este texto de ejemplo: «Señora directora: en el patio hay un solo basurero para más de 300 estudiantes. Después del recreo, el suelo queda cubierto de envases. No se trata de culpar a nadie: faltan basureros. Solicito que se instalen al menos cuatro más.» Escribe en dos líneas distintas el tema y la postura, y copia dos palabras o expresiones del texto que te ayudaron a reconocer la postura.",
   "Tema: la basura en el patio. Postura: el autor sostiene que el colegio debe instalar al menos cuatro basureros más. Pistas: «Solicito que se instalen» y «faltan basureros».",
   ["separa tema y postura", "formula la postura con una oración completa", "cita dos expresiones del texto"], ["dos líneas y dos citas en el cuaderno"],
   ["responder la postura solo con «la basura»", "citar expresiones que no están en el texto"], "Intercambia tu ficha con otra persona y revisa si la postura que escribió coincide con la tuya."),
  "Lee en voz alta la oración «Los recreos deberían durar veinte minutos» y subraya la expresión que marca la postura.",
  "Escribe dos posturas opuestas sobre el tema «tareas para el fin de semana» y subraya las marcas de postura de cada una.")

# ================================================================== clase 2
L(OA, 2,
  "Este cuaderno y un lápiz. Los textos que se analizan están escritos en cada ejercicio.",
  "Aprenderé a reconstruir un argumento separando la tesis, las razones que la apoyan y las evidencias que sostienen cada razón.",
  ["Sé distinguir tema y postura.", "Sé calcular un porcentaje sencillo."],
  ["Un argumento es la unión de una razón con una evidencia que apoya una tesis. La tesis es lo que el autor defiende. La razón explica por qué la tesis es aceptable: «porque es peligroso». La evidencia es el dato, el ejemplo, el testimonio o la cita de una persona experta que respalda la razón: «tres ciclistas cayeron esta semana».",
   "Reconstruir un argumento es ordenarlo en un esquema: tesis, razón 1 con su evidencia, razón 2 con su evidencia. Los conectores ayudan a encontrar las razones: «porque», «ya que», «pues», «por lo tanto», «en consecuencia». Una afirmación sin razón («Debe cambiarse, es necesario») solo repite la tesis con otras palabras.",
   "Existen distintos tipos de evidencia: datos y cifras, ejemplos concretos, testimonios y opiniones de expertos. Un buen argumento tiene una razón clara y una evidencia que se relaciona con ella. Cuando el esquema queda con casilleros vacíos, el argumento está incompleto y conviene decirlo al evaluarlo."],
  [("argumento", "razón con su evidencia que apoya una tesis"), ("razón", "explicación de por qué la tesis es aceptable"), ("evidencia", "dato, ejemplo o testimonio que respalda una razón"), ("conector causal", "palabra que introduce una causa, como «porque» o «ya que»"), ("testimonio", "relato de alguien que vio o vivió algo")],
  [("Reconstruir un esquema", "«El colegio debería ofrecer más talleres de música. Primero, la música mejora la concentración: en un taller de ejemplo, 18 de 24 estudiantes dijeron que estudiaban con más calma después de ensayar. Segundo, cuesta poco: bastan seis instrumentos prestados por la comunidad.» Reconstruye el argumento.",
    ["Tesis: el colegio debería ofrecer más talleres de música.", "Razón 1: mejora la concentración. Evidencia: 18 de 24 estudiantes estudian con más calma.", "Razón 2: cuesta poco. Evidencia: bastan seis instrumentos prestados."], "Tesis: más talleres de música; razón 1 con 18 de 24; razón 2 con seis instrumentos prestados"),
   ("Argumento en una carta", "«Pido que se repare la ciclovía de la calle Sur porque es peligrosa. En la última semana, tres ciclistas cayeron en los baches, según el relato de los vecinos.» Identifica tesis, razón y evidencia.",
    ["Tesis: se debe reparar la ciclovía.", "La palabra «porque» introduce la razón: es peligrosa.", "Evidencia: tres ciclistas cayeron, según el testimonio de vecinos."], "Tesis: reparar la ciclovía; razón: es peligrosa; evidencia: tres caídas relatadas por vecinos")],
  [("Contar como razón una frase que repite la tesis.", "«Debe cambiarse porque es necesario cambiarlo» no aporta nada nuevo.", "Pregunta: ¿esta frase explica por qué o solo repite lo que se pide?"),
   ("Llamar evidencia a una opinión.", "«Es horrible» es una valoración y no se puede comprobar.", "La evidencia debe ser un dato, un ejemplo o un testimonio identificable.")],
  ([E("En «Hay que usar casco porque protege la cabeza en una caída», ¿cuál es la razón?", "Protege la cabeza en una caída", "La palabra «porque» introduce la razón de la tesis."),
    E("¿Cuál es una evidencia? (a) «Debemos mejorar el patio.» (b) «En una encuesta de ejemplo, 30 de 40 estudiantes pidieron más bancas.» (c) «El patio es feo.»", "(b)", "Solo (b) entrega un dato que puede comprobarse."),
    E("¿Qué palabra introduce una razón? (a) porque (b) aunque (c) mientras", "(a)", "«Porque» es un conector causal.")],
   [E("«Las tareas largas deberían limitarse a 30 minutos, ya que, según una encuesta de ejemplo a 50 estudiantes, 35 dijeron dormir menos de ocho horas cuando tenían tareas extensas.» ¿Cuál es la evidencia?", "Que 35 de 50 estudiantes durmieron menos de ocho horas con tareas extensas", "Es el dato que respalda la razón."),
    arith("En esa misma encuesta de ejemplo, 35 de 50 estudiantes durmieron poco. ¿Qué porcentaje es? Responde solo con el número.", "35*100//50", "Se multiplica por 100 la parte y se divide entre el total.", " %"),
    E("¿En qué se diferencian una razón y una evidencia?", "La razón explica por qué la tesis es aceptable y la evidencia es el dato o ejemplo que la respalda", "La razón es la explicación y la evidencia es la prueba de esa explicación.")],
   [E("Reconstruye: «Propongo cerrar al tránsito la calle del colegio durante la salida. Es una calle estrecha donde los peatones no caben con seguridad: en un conteo de ejemplo pasaron 60 autos en 10 minutos.» Escribe tesis, razón y evidencia.", "Tesis: cerrar la calle durante la salida; razón: los peatones no caben con seguridad; evidencia: 60 autos en 10 minutos", "Cada elemento aparece escrito: la petición, su motivo y el dato."),
    E("¿Cuál oración es la tesis? (a) «En una encuesta de ejemplo, 22 de 30 vecinos usan la plaza.» (b) «La plaza debe tener más luminarias.» (c) «Con luz, los vecinos salen más tranquilos.»", "(b)", "(a) es evidencia y (c) es una razón; la tesis es lo que se pide."),
    E("«Deberían ampliar el horario de la biblioteca. Es un cambio necesario.» ¿Qué le falta a este argumento?", "Una razón y una evidencia", "Dice qué se pide, pero no explica por qué ni da un dato.")],
   [E("Una columna defiende abrir el gimnasio los sábados. Razón 1: «Hoy el gimnasio está vacío sábado y domingo». Razón 2: «A todos nos gustaría». ¿Cuál razón es más sólida y por qué?", "La razón 1, porque se puede comprobar; la 2 generaliza sin evidencia", "«A todos» no tiene respaldo y la ocupación del gimnasio sí puede revisarse."),
    E("Un estudiante escribe: «El mirador debería cerrarse, porque es necesario cerrarlo». ¿Qué falla tiene?", "La razón repite la tesis y no aporta nada nuevo", "No explica por qué debe cerrarse.")],
   [E("«Los patios deberían tener techo. (1) En invierno se suspende el 30 % de los recreos por lluvia, según un registro de ejemplo. (2) Un techo permite jugar con lluvia. (3) Un colegio de ejemplo lo instaló y no suspendió ningún recreo en un mes.» ¿Cuáles oraciones son evidencia y cuál es la razón?", "Evidencia: la 1 y la 3; razón: la 2", "La 1 y la 3 son datos o casos; la 2 explica por qué sirve un techo."),
    E("¿Qué evidencia respalda de forma pertinente la razón «las rampas facilitan el acceso»? (a) 12 estudiantes usan silla de ruedas o bastón y hoy dan una vuelta de 80 metros porque no hay rampa. (b) Una rampa cuesta más que una escalera, según un vecino. (c) El director cree que sería buena idea.", "(a)", "Solo (a) es un dato que se relaciona con el acceso.")]),
  [E("Tu centro de estudiantes escribe: «Pedimos instalar dos bebederos. Hoy hay una sola llave para 300 estudiantes y en verano la fila dura todo el recreo». Identifica tesis, razón y evidencia.", "Tesis: instalar dos bebederos; razón: una sola llave es insuficiente; evidencia: 300 estudiantes y una fila que dura todo el recreo", "La tesis es lo pedido; la razón explica la necesidad y la evidencia da los datos.")],
  [E("¿Qué es una evidencia en un texto argumentativo?", "Un dato, ejemplo o testimonio que respalda una razón", "Sirve para probar la razón, no para repetirla."),
   E("¿Qué conectores ayudan a encontrar las razones?", "Porque, ya que, pues", "Introducen la causa de lo que se afirma."),
   E("Si un esquema tiene tesis pero no tiene evidencia, ¿cómo está el argumento?", "Incompleto", "Falta lo que respalda la razón.")],
  ("Reconstruye el argumento de esta carta de ejemplo: «Señor director: solicito que el municipio instale un cruce peatonal frente a la escuela. Cada mañana cruzan la calle unos 150 estudiantes y no hay semáforo. Además, el año pasado, según el relato de una apoderada, un auto estuvo a punto de atropellar a un niño.» Escribe la tesis, dos razones y la evidencia de cada una.",
   "Tesis: instalar un cruce peatonal frente a la escuela. Razón 1: cruzan muchos estudiantes sin semáforo; evidencia: unos 150 cada mañana. Razón 2: hay riesgo de accidente; evidencia: el relato de una apoderada sobre un auto que casi atropella a un niño.",
   ["identifica la tesis", "separa dos razones", "asocia una evidencia a cada razón"], ["esquema de cuatro casilleros en el cuaderno"],
   ["confundir la razón con la evidencia", "dejar una razón sin evidencia"], "Compara tu esquema con el de otra persona y revisa si ambos separaron razón y evidencia."),
  "Escribe una tesis cualquiera y, debajo, una razón que empiece con «porque».",
  "Toma la tesis «El colegio debería tener un huerto» y escribe dos razones, cada una con una evidencia de ejemplo.")

# ================================================================== clase 3
L(OA, 3,
  "Este cuaderno y un lápiz. Los textos que se analizan están escritos en cada ejercicio.",
  "Aprenderé a distinguir hechos y opiniones en textos argumentativos y a comprobar inferencias que se apoyan en datos del texto.",
  ["Sé reconstruir tesis, razón y evidencia.", "Sé calcular restas y porcentajes sencillos."],
  ["Un hecho es información que se puede comprobar con datos, mediciones u observación: «la biblioteca cierra a las 18:00». Una opinión es una valoración personal que se discute pero no se mide: «el horario es absurdo». En un texto argumentativo ambos aparecen mezclados. El autor suele partir de hechos para sostener una opinión, y a veces presenta una opinión como si fuera un hecho.",
   "Algunas pistas ayudan. Los hechos traen cifras, fechas, nombres y lugares. Las opiniones traen adjetivos valorativos (injusto, mejor, absurdo), expresiones como «a mi juicio» o «me parece» y palabras que expresan obligación o juicio («debería», «lamentablemente»). La pregunta clave es: ¿cómo se podría comprobar esto? Si hay una forma, es un hecho; si no, es una opinión.",
   "Una inferencia es una conclusión que sacamos a partir de pistas del texto. Una inferencia verificable se apoya en datos que están escritos y puede comprobarse con ellos. Por ejemplo, si el texto dice que 12 de 20 bancas reciben sol, se puede inferir que 8 no lo reciben. En cambio, «a nadie le importa el barrio» no se puede comprobar con los datos dados."],
  [("hecho", "información que se puede comprobar"), ("opinión", "valoración personal que no se puede comprobar como un dato"), ("inferencia", "conclusión que se saca a partir de pistas del texto"), ("verificable", "que se puede comprobar con datos o con la observación"), ("valoración", "juicio sobre algo, como bueno, malo o injusto")],
  [("Separar hecho y opinión", "«Lamentablemente, el nuevo horario de la biblioteca, que cierra a las 18:00, es absurdo.» Sepáralo en hecho y opinión.",
    ["Busca lo comprobable: la biblioteca cierra a las 18:00.", "Busca las valoraciones: «lamentablemente» y «absurdo».", "Escribe cada parte por separado."], "Hecho: la biblioteca cierra a las 18:00; opinión: es lamentable y absurdo"),
   ("Inferencia verificable", "Un texto de ejemplo dice: «Se inscribieron 45 estudiantes al taller de teatro y hay 30 cupos». ¿Qué puede inferirse y se puede comprobar con los datos?",
    ["Restamos: 45 − 30 = 15.", "Se infiere que 15 estudiantes quedarían sin cupo si todos asisten.", "Es verificable porque usa solo los datos escritos."], "Quedarían 15 estudiantes sin cupo")],
  [("Creer que una oración con número siempre es un hecho.", "El número puede servir a una valoración, como en «tres horas de tarea son una crueldad».", "Separa la parte comprobable de la valoración."),
   ("Tratar como verdad comprobada una inferencia sin datos.", "«Nadie lee» no se apoya en ninguna cifra del texto.", "Pregunta qué dato del texto respalda la inferencia.")],
  ([E("«El gimnasio tiene tres camarines.» ¿Es hecho u opinión?", "Hecho", "Se puede comprobar yendo a contarlos."),
    E("«El gimnasio es horrible.» ¿Es hecho u opinión?", "Opinión", "«Horrible» es una valoración personal."),
    E("¿Qué pregunta ayuda a decidir si algo es un hecho?", "¿Cómo se podría comprobar?", "Si existe un modo de comprobarlo, es un hecho.")],
   [E("«Creo que el recreo es demasiado corto.» ¿Es hecho u opinión y cuál es la marca?", "Opinión; la marca es «creo que»", "Esa expresión revela una postura personal."),
    E("«El curso reunió 48 kilos de papel para reciclar.» ¿Es hecho u opinión?", "Hecho", "Se puede verificar pesando el papel."),
    E("«El alcalde dijo que la obra será estupenda.» ¿Qué parte es opinión?", "«Estupenda»", "Es la valoración; lo comprobable es que él lo dijo.")],
   [E("Lee: 1) «El campeonato comenzó el 12 de mayo.» 2) «Fue el mejor campeonato de la historia.» 3) «Participaron 16 equipos.» 4) «El árbitro estuvo pésimo.» 5) «El equipo ganador anotó 21 goles.» ¿Cuáles son opiniones?", "La 2 y la 4", "«El mejor» y «pésimo» son valoraciones."),
    E("Quieres transformar la opinión «la sopa del casino es asquerosa» en un dato. ¿Cuál sirve? (a) «La sopa es lo peor.» (b) «En el casino se sirvió sopa tres veces esta semana.» (c) «Nadie quiere sopa.»", "(b)", "Una frecuencia se revisa en el menú; las otras son juicios."),
    arith("Un texto de ejemplo informa que de 25 computadores del laboratorio funcionan 3. ¿Cuántos no funcionan?", "25-3", "Al total se le restan los que funcionan.", " computadores")],
   [E("«Según el dueño, su pastelería es la más rica de la ciudad, y vendió 300 tortas en diciembre.» ¿Qué se puede comprobar y qué no?", "Se comprueba «vendió 300 tortas»; no se comprueba «la más rica»", "Las ventas tienen registro; «la más rica» depende del gusto."),
    E("Un compañero dice: «Si un experto opina, su opinión ya es un hecho». ¿Es correcto?", "No; es un hecho que lo dijo, pero lo que opina sigue siendo una valoración", "El prestigio de quien habla no convierte una valoración en dato.")],
   [E("Un texto de ejemplo dice: «De 120 estudiantes de octavo, 90 usan la biblioteca al menos una vez por semana». Una persona infiere: «Más de la mitad de octavo usa la biblioteca cada semana». ¿La inferencia es verificable?", "Sí; 90 es más de la mitad de 120, que es 60", "Se comprueba comparando 90 con la mitad de 120."),
    E("Con ese mismo texto, otra persona infiere: «A los estudiantes de octavo les encanta leer». ¿Se puede comprobar con los datos?", "No; el dato solo muestra que usan la biblioteca, no que les encante leer", "«Encanta» es una valoración que el dato no demuestra.")]),
  [E("Una carta dice: «El bus pasa cada 40 minutos y eso es una falta de respeto». ¿Cuál parte es un hecho y cuál una opinión?", "Hecho: pasa cada 40 minutos; opinión: es una falta de respeto", "La frecuencia se mide con un reloj; «falta de respeto» es un juicio.")],
  [E("¿Un hecho puede comprobarse?", "Sí", "Esa es su característica central."),
   E("Escribe una expresión que suele marcar una opinión.", "Por ejemplo: «creo que», «a mi juicio», «lamentablemente»", "Expresan un juicio personal."),
   E("¿Una oración puede mezclar un hecho y una opinión?", "Sí; conviene separar ambas partes", "Muchos textos argumentativos las combinan.")],
  ("Separa hechos y opiniones en este párrafo de ejemplo: «El torneo de ajedrez se jugó el jueves en la biblioteca. Participaron 18 estudiantes. Fue una jornada aburridísima, aunque la ganadora, Tamara Ortiz, jugó brillante. El premio fueron dos libros.» Haz dos columnas, hechos y opiniones, y explica cómo comprobarías uno de los hechos.",
   "Hechos: se jugó el jueves en la biblioteca; participaron 18 estudiantes; ganó Tamara Ortiz; el premio fueron dos libros. Opiniones: «aburridísima» y «brillante». Comprobaría la cantidad de participantes revisando la lista de inscritos.",
   ["separa al menos tres hechos", "identifica las dos valoraciones", "explica una forma de comprobar un hecho"], ["dos columnas en el cuaderno"],
   ["clasificar «ganó Tamara Ortiz» como opinión", "no justificar cómo se comprueba"], "Pide a otra persona que clasifique el mismo párrafo y compara en qué oraciones difieren."),
  "Escribe dos hechos y dos opiniones sobre tu sala de clases.",
  "Elige una opinión de esta clase y reescríbela como un dato comprobable.")

# ================================================================== clase 4
L(OA, 4,
  "Este cuaderno y un lápiz. Los textos y los datos de las encuestas son de ejemplo y están escritos en cada ejercicio.",
  "Aprenderé a evaluar si la evidencia de un argumento es confiable (viene de una fuente creíble) y pertinente (se relaciona con la tesis).",
  ["Sé reconstruir tesis, razón y evidencia.", "Sé distinguir hechos y opiniones."],
  ["No toda evidencia vale lo mismo. Una evidencia es confiable cuando se sabe de dónde viene: una fuente identificada, una persona experta en el tema, un dato con fecha y con la forma en que se obtuvo. Es poco confiable cuando es anónima, no tiene fecha, cita «dicen que…» o la entrega alguien que gana si te convence.",
   "Una evidencia es pertinente cuando se relaciona de verdad con la razón que apoya. Si alguien defiende que el pasto sintético mejora el patio y cita el promedio de notas de matemática, el dato no es pertinente. Además conviene revisar si es suficiente: un solo caso, o una encuesta a cuatro personas, no alcanza para hablar de todo un curso. Y si es actual: un dato de hace veinte años puede haber cambiado.",
   "Al evaluar, haz cuatro preguntas: ¿quién lo dice? (fuente), ¿qué tiene que ver con la tesis? (pertinencia), ¿cuántos casos hay? (suficiencia) y ¿de cuándo es? (actualidad). Una evidencia puede ser verdadera y aun así débil, si no se relaciona con la razón o si es muy pequeña."],
  [("fuente", "origen de la información: quién la entrega y cómo la obtuvo"), ("confiable", "que merece confianza porque se sabe de dónde viene"), ("pertinente", "que se relaciona directamente con lo que se quiere probar"), ("muestra", "grupo pequeño de casos que se estudia para hablar de un grupo mayor"), ("suficiente", "que alcanza para sostener la conclusión")],
  [("Evidencia pertinente", "Tesis: «Hay que instalar un techo en el patio». Evidencia A: «En 2 de cada 10 recreos de invierno llueve, según el registro de ejemplo del colegio». Evidencia B: «El colegio tiene 14 salas». ¿Cuál es pertinente?",
    ["La tesis trata de la lluvia en el patio.", "A habla de recreos con lluvia: se relaciona con la razón.", "B es un dato verdadero, pero no tiene que ver con el techo."], "La evidencia A, porque se relaciona con la lluvia en los recreos"),
   ("Suficiencia y fuente", "Una columna dice: «Todos los vecinos están de acuerdo con cerrar la calle, según me contó mi primo». ¿Es confiable y suficiente?",
    ["La fuente es una sola persona y no se la identifica como experta.", "«Todos los vecinos» se apoya en un solo testimonio.", "No es suficiente ni confiable: faltan datos de una consulta más amplia."], "No; es un testimonio único y no sostiene un «todos»")],
  [("Aceptar un dato solo porque es verdadero.", "Puede ser verdadero y no tener relación con la razón.", "Pregunta qué tiene que ver con la tesis."),
   ("Creer que una cifra grande es siempre más confiable.", "Importa de dónde viene y cómo se obtuvo, no solo su tamaño.", "Busca fuente, fecha y forma de obtención.")],
  ([E("Un dato sin fuente ni fecha, ¿es confiable?", "No", "No se sabe quién lo entrega ni de cuándo es."),
    E("¿Qué fuente es más confiable para saber cuántos estudiantes tiene un colegio? (a) Una cadena de mensajes sin firma. (b) El registro de matrícula del colegio. (c) Lo que dice un compañero.", "(b)", "El registro oficial es una fuente identificada."),
    E("¿Qué significa que una evidencia sea pertinente?", "Que se relaciona directamente con lo que se quiere probar", "Debe tener que ver con la razón.")],
   [E("Una carta defiende más tiempo de recreo y cita: «Mi vecina y yo opinamos igual». ¿Es suficiente como evidencia?", "No; son solo dos personas", "Una muestra tan pequeña no sostiene una conclusión general."),
    E("Tesis: «Hay que ampliar la biblioteca». ¿Qué evidencia es pertinente? (a) «Cada semana se piden 200 libros y solo caben 12 personas sentadas.» (b) «El colegio fue fundado hace mucho.» (c) «El patio tiene cuatro árboles.»", "(a)", "Solo (a) se relaciona con la demanda y el espacio de la biblioteca."),
    E("Una encuesta de ejemplo del año 2005 se usa para describir cómo estudian hoy los jóvenes. ¿Qué criterio falla?", "La actualidad", "El dato es antiguo y puede haber cambiado.")],
   [E("Evidencia: «Un médico, que vende suplementos de su marca, afirma que su producto mejora la memoria». ¿Qué duda razonable genera?", "Que gana dinero si te convence, así que su fuente tiene interés propio", "Quien se beneficia con la conclusión es una fuente menos neutral."),
    arith("Tesis: «Los estudiantes de octavo duermen poco». Evidencia: «En una encuesta de ejemplo a 240 de los 300 estudiantes de octavo, 168 dijeron dormir menos de ocho horas». ¿Qué porcentaje de los encuestados duerme menos de ocho horas? Responde solo con el número.", "168*100//240", "Se calcula qué parte del total encuestado representa el grupo.", " %"),
    E("Lee: «Los vecinos del sector norte pidieron más luz: 15 de 20 entrevistados lo solicitaron». ¿Se puede decir que lo piden todos los vecinos de la comuna?", "No; la muestra es de 20 personas de un solo sector", "No representa a toda la comuna.")],
   [E("Dos evidencias para «la plaza necesita más bancas»: A) «El municipio contó 40 personas de pie esperando a las 19:00 durante cinco días». B) «Alguien me dijo que la plaza está vacía». ¿Cuál es más confiable y por qué?", "La A, porque tiene fuente, método y fechas; la B es un comentario sin respaldo", "La A permite comprobar quién contó y cómo lo hizo."),
    E("Una persona dice: «Mi dato es verdadero, por lo tanto sirve para cualquier tesis». ¿Qué le falta revisar?", "Si es pertinente, es decir, si se relaciona con la razón que quiere apoyar", "Un dato verdadero puede no tener relación con la tesis.")],
   [E("Una columna sostiene que «el transporte escolar debe ampliarse» y cita: «el 85 % de los 20 apoderados que esperaban el bus dijo que llegaba atrasado». Escribe una debilidad de la evidencia.", "Es una muestra pequeña y solo de apoderados que esperaban el bus", "Veinte personas en un solo lugar no representan a todos los usuarios."),
    E("Un texto cita «según expertos» sin nombrarlos. ¿Qué cambio lo haría más confiable? (a) Escribir «expertos» en mayúscula. (b) Indicar nombre, cargo y año de quien lo afirma. (c) Repetir la frase al final.", "(b)", "Una fuente identificada puede comprobarse.")]),
  [E("Quieres defender ante tu curso que «el kiosco venda más fruta». ¿Cuál evidencia de ejemplo usarías por ser pertinente? (a) «El 70 % de los 100 encuestados del recreo pidió fruta.» (b) «El kiosco tiene letrero azul.» (c) «El director usa lentes.»", "(a)", "Solo (a) se relaciona con la demanda de fruta.")],
  [E("Nombra dos preguntas para evaluar una evidencia.", "Por ejemplo: ¿quién lo dice? y ¿se relaciona con la tesis?", "Fuente y pertinencia son criterios de evaluación."),
   E("¿Una evidencia verdadera puede ser débil?", "Sí, si no es pertinente o es insuficiente", "Verdadero no significa que sirva para esa tesis."),
   E("¿Qué hace más confiable a un dato?", "Que tenga fuente identificada, fecha y método", "Así puede comprobarse.")],
  ("Evalúa esta evidencia de ejemplo. Tesis: «Hay que prohibir las bolsas plásticas en la feria». Evidencia: «Un vecino me dijo que vio muchas bolsas en la calle. Además, mi tía tiene una tienda con bolsas de papel y le va muy bien». Escribe tres debilidades de la evidencia (fuente, suficiencia o pertinencia) y qué dato nuevo pedirías.",
   "Debilidades: es el testimonio de una sola persona sin cifras; el caso de la tienda de la tía es único y de una persona con interés; no hay dato sobre cuántas bolsas se usan en la feria. Pediría el conteo de bolsas entregadas en un día de feria, con fecha y quién lo midió.",
   ["nombra tres debilidades distintas", "usa los criterios de fuente, suficiencia o pertinencia", "propone un dato nuevo concreto"], ["lista de tres debilidades y un dato nuevo en el cuaderno"],
   ["decir que la evidencia es mala sin explicar por qué", "pedir un dato que no se relaciona con la tesis"], "Lee tus debilidades a otra persona y pídele que diga cuál criterio usaste en cada una."),
  "Anota una evidencia que hayas escuchado esta semana y escribe quién la dijo.",
  "Inventa una evidencia débil y una fuerte para la tesis «hay que ampliar el bicicletero» y explica la diferencia.")

# ================================================================== clase 5
L(OA, 5,
  "Este cuaderno y un lápiz. Las oraciones y los textos que se analizan están escritos en cada ejercicio.",
  "Aprenderé a reconocer cómo el lenguaje busca persuadir, en especial con qué intención el autor usa los modos verbales indicativo, subjuntivo e imperativo.",
  ["Sé reconocer la postura y la evidencia de un texto.", "Sé qué es un verbo y que se conjuga."],
  ["Los verbos se conjugan en modos. El modo indicativo expresa hechos y certezas: «el humedal alberga aves». El modo subjuntivo expresa deseos, dudas y posibilidades: «ojalá cuidemos el humedal», «para que las aves vuelvan». El modo imperativo da órdenes, pedidos o invitaciones: «cuiden el humedal». El autor elige el modo según la intención: afirmar, desear, dudar o exigir.",
   "Otros recursos persuasivos son las preguntas retóricas (que se hacen sin esperar respuesta: «¿Quién quiere un patio sucio?»), los adjetivos valorativos, las repeticiones, el «nosotros» inclusivo que une al autor con el público («debemos cuidar lo nuestro») y las perífrasis de obligación («hay que», «debemos», «tenemos que»). Estos recursos no son buenos ni malos por sí solos: se evalúa si ayudan a argumentar o si reemplazan a las razones.",
   "Evaluar el lenguaje significa preguntarse con qué intención se usa cada recurso. Un imperativo muestra urgencia, un subjuntivo muestra deseo o duda, un indicativo con cifras da seguridad. Si un texto casi no tiene razones y mucho lenguaje que presiona, conviene sospechar que busca convencer por emoción más que por evidencia."],
  [("modo verbal", "forma de conjugar un verbo que muestra la actitud del hablante"), ("indicativo", "modo que presenta hechos o certezas"), ("subjuntivo", "modo que expresa deseo, duda o posibilidad"), ("imperativo", "modo que expresa orden, pedido o invitación"), ("pregunta retórica", "pregunta que se hace sin esperar respuesta, para reforzar una idea")],
  [("Modos y sus intenciones", "Analiza: «Ojalá cuidemos el humedal. Las aves llegan cada primavera. Cuiden el humedal.» ¿Qué modo y qué intención tiene cada oración?",
    ["«Cuidemos» está en subjuntivo y expresa un deseo.", "«Llegan» está en indicativo y presenta un hecho.", "«Cuiden» está en imperativo y pide actuar."], "Subjuntivo: deseo; indicativo: hecho; imperativo: pedido o exigencia"),
   ("Recursos que persuaden", "«¿Quién quiere un patio sucio? Nosotros no. Tenemos que actuar hoy.» Identifica dos recursos persuasivos.",
    ["«¿Quién quiere un patio sucio?» es una pregunta retórica.", "«Nosotros» incluye al autor y al público.", "«Tenemos que» expresa obligación y urgencia."], "Pregunta retórica y nosotros inclusivo; además, expresión de obligación")],
  [("Pensar que el imperativo solo sirve para mandar con enojo.", "También invita o pide con cortesía («acompáñenos»).", "Fíjate en la intención y en el tono del texto."),
   ("Creer que un recurso persuasivo prueba la tesis.", "Una pregunta retórica o una repetición refuerzan la idea, pero no son evidencia.", "Busca siempre si hay razones y datos además del recurso.")],
  ([E("«Cuiden las áreas verdes.» ¿En qué modo está el verbo «cuiden»?", "Imperativo", "Expresa un pedido u orden."),
    E("«Ojalá todos participemos.» ¿Qué expresa el verbo «participemos»? (a) Un hecho comprobado. (b) Un deseo. (c) Una orden.", "(b)", "«Ojalá» pide el subjuntivo, que expresa deseo."),
    E("«El humedal tiene tres lagunas.» ¿Qué modo presenta el verbo «tiene»?", "Indicativo", "Presenta un hecho como cierto.")],
   [E("¿Qué intención tiene el autor al escribir «Es posible que el agua baje este verano»? (a) Afirmar con total certeza. (b) Expresar una posibilidad. (c) Ordenar algo.", "(b)", "«Es posible que» con «baje» (subjuntivo) expresa posibilidad."),
    E("«¿Cuántas veces más vamos a esperar una solución?» ¿Qué recurso es?", "Una pregunta retórica", "No espera una respuesta; refuerza el reclamo."),
    E("«Tenemos que cuidar lo nuestro.» ¿Qué efecto produce «nosotros» incluido en «tenemos»?", "Une al autor con el público y genera una responsabilidad compartida", "El plural inclusivo busca que el lector se sienta parte.")],
   [E("Clasifica el modo de cada verbo marcado: 1) «Firmen la petición.» 2) «Hay 200 firmas.» 3) «Que se escuche nuestra voz.» Escribe el modo de 1, 2 y 3.", "1 imperativo; 2 indicativo; 3 subjuntivo", "1 es un pedido; 2 un hecho; 3 un deseo con «que»."),
    E("Reescribe «Cuiden el humedal» como un deseo usando «ojalá». ¿Cuál es la forma correcta? (a) Ojalá cuidan el humedal. (b) Ojalá cuiden el humedal. (c) Ojalá cuidar el humedal.", "(b)", "Con «ojalá» el verbo va en subjuntivo."),
    E("«Es evidente, clarísimo y absolutamente obvio que hay que cambiarlo.» ¿Qué recurso se repite para presionar al lector?", "Adjetivos y adverbios de énfasis que refuerzan la certeza sin dar datos", "Insistir en lo «obvio» reemplaza a la evidencia.")],
   [E("Un autor escribe diez veces «Exijan, exijan, exijan». Otro escribe «El 70 % de los 100 consultados exige el cambio». ¿Cuál se apoya más en evidencia?", "El segundo", "El primero repite una orden y el segundo entrega un dato."),
    E("Un discurso dice: «Si todos colaboráramos, el patio brillaría». ¿Expresa un hecho o una posibilidad irreal?", "Una posibilidad irreal, expresada con subjuntivo", "«Colaboráramos» presenta lo que no ocurre pero se desea.")],
   [E("Texto: «Compañeros, sé que están cansados. Aun así, firmen hoy. Mañana quizás sea tarde: ojalá lleguemos a tiempo.» Nombra el modo de «firmen» y de «lleguemos» y qué intención tiene cada uno.", "«Firmen»: imperativo, pide actuar; «lleguemos»: subjuntivo, expresa deseo", "El imperativo exige y el subjuntivo expresa un anhelo."),
    E("Un texto contiene 6 imperativos, 2 preguntas retóricas y ninguna cifra ni razón. ¿Qué se puede decir de su fuerza argumentativa?", "Es débil: persuade por presión y emoción, pero no entrega razones ni evidencia", "El lenguaje persuasivo no sustituye a los argumentos.")]),
  [E("Quieres invitar a tu curso a limpiar la plaza el sábado. ¿Qué frase usa el imperativo? (a) Ojalá limpiemos la plaza. (b) Limpien la plaza el sábado. (c) La plaza está sucia.", "(b)", "Solo (b) usa un verbo en imperativo para pedir actuar.")],
  [E("¿Qué modo verbal expresa deseo o duda?", "El subjuntivo", "Se usa en «ojalá» y «es posible que»."),
   E("¿Qué modo verbal presenta hechos como ciertos?", "El indicativo", "Afirma lo que se considera real."),
   E("Escribe una pregunta retórica sobre el cuidado del agua.", "Por ejemplo: «¿Quién quiere quedarse sin agua?»", "Se hace para reforzar la idea, no para recibir respuesta.")],
  ("Analiza este fragmento de discurso de ejemplo: «Amigas y amigos: ¿quién de nosotros quiere un colegio sin áreas verdes? Nadie. El patio tiene hoy 4 árboles y hace cinco años tenía 11. Ojalá recuperemos lo perdido. Planten un árbol cada curso. Hay que actuar hoy.» Anota tres recursos que persuaden, el modo de «recuperemos» y de «planten», y si el texto entrega evidencia.",
   "Recursos: pregunta retórica, «nosotros» inclusivo, expresión de obligación «hay que actuar». «Recuperemos» está en subjuntivo (deseo); «planten» en imperativo (pedido). Entrega evidencia: 4 árboles hoy frente a 11 hace cinco años.",
   ["nombra tres recursos", "reconoce los dos modos", "indica la evidencia de ejemplo"], ["lista de recursos y dos modos en el cuaderno"],
   ["confundir subjuntivo con imperativo", "creer que la pregunta retórica es evidencia"], "Cambia tu lista con otra persona y revisa si coinciden en el modo de los verbos."),
  "Escribe tres oraciones sobre el reciclaje: una con indicativo, una con subjuntivo y una con imperativo.",
  "Reescribe un párrafo de esta clase quitando los recursos de presión y dejando solo razones y datos.")

# ================================================================== clase 6
L(OA, 6,
  "Este cuaderno y un lápiz. Los dos textos de cada ejercicio están escritos completos en el enunciado.",
  "Aprenderé a comparar dos textos que defienden posturas distintas sobre una misma controversia y a describir qué estrategia usa cada uno.",
  ["Sé reconstruir un argumento.", "Sé evaluar la evidencia y reconocer recursos del lenguaje."],
  ["Una controversia es un tema en que hay posturas opuestas. Dos textos pueden estudiar la misma controversia y convencer de maneras distintas. Una estrategia es el camino que elige el autor para convencer: apoyarse en datos, en ejemplos o historias, en la opinión de una autoridad, en una emoción o en una comparación con otro caso.",
   "Al comparar dos textos conviene revisar: la postura de cada uno, las razones, el tipo de evidencia, el tono (técnico, cercano, urgente) y si el autor reconoce la postura contraria. Un contraargumento es una razón que sirve para la postura opuesta; refutar es mostrar por qué esa razón no basta. Un texto sólido suele considerar al menos una objeción y responderla.",
   "Comparar no es decidir cuál «cae mejor». Se trata de describir con claridad: «El texto A usa datos y un tono técnico; el B usa un caso cercano y un tono emotivo». Después puedes evaluar cuál sostiene mejor su postura con las razones y la evidencia que presenta. Tu opinión debe apoyarse en lo que dicen los textos."],
  [("controversia", "tema en que existen posturas opuestas"), ("estrategia argumentativa", "camino que elige el autor para convencer"), ("contraargumento", "razón que apoya la postura contraria"), ("refutar", "mostrar por qué una razón contraria no es suficiente"), ("tono", "actitud que transmite un texto, como técnica, cercana o urgente")],
  [("Comparar estrategias", "Texto A: «El 65 % de los 80 estudiantes consultados llega más de diez minutos tarde por el bus. Se necesita otra ruta.» Texto B: «Cada mañana veo a Pedro correr, con la mochila abierta, detrás del bus que se va. Merece otra ruta». ¿Qué estrategia usa cada uno?",
    ["A presenta un porcentaje de una consulta: estrategia de datos.", "B cuenta un caso concreto con una persona: estrategia de ejemplo y emoción.", "Ambos tienen la misma postura, pero convencen por caminos distintos."], "A usa datos; B usa un caso cercano y emotivo"),
   ("Contraargumento y refutación", "«Algunos dicen que la jornada de lectura quita tiempo a las matemáticas. Pero leer 20 minutos al día mejora la comprensión de los enunciados, así que ayuda a las matemáticas.» Identifica contraargumento y refutación.",
    ["El contraargumento es «quita tiempo a las matemáticas».", "La refutación comienza en «Pero»: leer mejora la comprensión de enunciados.", "El autor considera la objeción y la responde."], "Contraargumento: quita tiempo a matemáticas; refutación: la lectura mejora la comprensión")],
  [("Decir que un texto es mejor solo porque coincide con mi opinión.", "Evaluar es revisar cómo sostiene su postura, no si me gusta.", "Compara razones y evidencias antes de opinar."),
   ("Creer que mencionar la postura contraria debilita un texto.", "Considerar objeciones y responderlas lo fortalece.", "Busca si el autor reconoce y refuta una objeción.")],
  ([E("¿Qué es una controversia?", "Un tema en que hay posturas opuestas", "Los dos textos pueden defender lados distintos."),
    E("¿Qué estrategia usa un texto que apoya su postura con un porcentaje de una encuesta? (a) De datos. (b) De autoridad. (c) De emoción.", "(a)", "El porcentaje es un dato."),
    E("¿Qué se hace al refutar un contraargumento?", "Se muestra por qué esa razón contraria no es suficiente", "Es responder a la objeción.")],
   [E("Texto A: «La uniformidad evita burlas, según el registro de ejemplo de convivencia: bajaron de 12 a 5 los reclamos». Texto B: «Vestir como cada uno quiere es expresar quién eres». ¿Cuál se apoya en datos y cuál en un valor?", "A se apoya en datos; B en un valor (la expresión personal)", "A da cifras de reclamos y B defiende la libertad de expresarse."),
    arith("Un registro de ejemplo muestra que los reclamos por burlas bajaron de 12 a 5. ¿Cuántos reclamos menos hubo?", "12-5", "A la cantidad inicial se le resta la final.", " reclamos"),
    E("Un texto dice «Aunque algunos piensan que el huerto cuesta mucho, bastan semillas donadas». ¿Qué hace el autor? (a) Ignora la objeción. (b) Reconoce una objeción y la responde. (c) Cambia de tema.", "(b)", "«Algunos piensan» presenta la objeción y «bastan semillas donadas» la rebate.")],
   [E("Texto A (técnico): «El consumo de energía del gimnasio bajó 18 % tras cambiar las ampolletas». Texto B (cercano): «Ahora, al entrar al gimnasio, hay una luz más suave y se ahorra». ¿Cuál tono es técnico y cuál cercano?", "A es técnico; B es cercano", "A usa una cifra y B habla de la experiencia al entrar."),
    E("Dos columnas sobre el uso de bicicletas: A dice «mejoran la salud» y B dice «aumentan los accidentes». ¿Qué debes revisar antes de decidir cuál es más sólida?", "La evidencia que cada una presenta", "Cada afirmación debe respaldarse con datos o ejemplos."),
    E("Una columna reconoce: «Es cierto que la ciclovía costó mucho, pero se pagará sola en cinco años por el ahorro en transporte». ¿Cuál es la refutación?", "«Se pagará sola en cinco años por el ahorro en transporte»", "Es la respuesta a la objeción del costo.")],
   [E("Texto A: «Prohibir los celulares evita distracciones». Texto B: «Prohibir los celulares ignora que sirven para aprender». ¿Qué tienen en común y qué los separa?", "Comparten el tema (los celulares en clase); la postura los separa: prohibir o permitir con uso educativo", "Mismo asunto, posturas opuestas."),
    E("Un estudiante compara y escribe: «El texto B es mejor porque me gusta». ¿Qué le falta a su evaluación?", "Fundamentarla con razones y evidencias de los textos", "Una evaluación necesita apoyo en lo que dicen los textos.")],
   [E("Texto A: «Del total de 50 bancas, 20 están rotas, según el registro de ejemplo del municipio». Texto B: «Imagina esperar en una banca rota con tu abuela». ¿Cuál convence más por evidencia y cuál más por emoción?", "A por evidencia; B por emoción", "A entrega un dato verificable y B apela a un sentimiento."),
    E("Dos columnas defienden posturas opuestas, pero ambas citan la misma encuesta de ejemplo: 60 % a favor y 40 % en contra. ¿Cómo es posible que las dos la usen?", "Cada una destaca la parte que favorece su postura", "Un mismo dato puede enfatizarse de modos distintos.")]),
  [E("Dos vecinos opinan sobre cerrar una plaza por las noches. Vecino 1: «Hubo 9 robos en tres meses, según el registro de ejemplo». Vecino 2: «Cerrarla deja a los jóvenes sin espacio». ¿Quién se apoya en un dato y quién en una consecuencia social?", "El vecino 1 en un dato; el vecino 2 en una consecuencia social", "El primero cita robos y el segundo plantea el efecto en los jóvenes.")],
  [E("En Lenguaje: ¿Qué es un contraargumento?", "Una razón que apoya la postura contraria", "Se menciona para luego responder."),
   E("Nombra una estrategia argumentativa.", "Por ejemplo: datos, ejemplos, autoridad o emoción", "Son caminos para convencer."),
   E("¿Qué puedes comparar entre dos textos de una misma controversia?", "Postura, razones, evidencia y tono", "Esos aspectos muestran cómo convence cada uno.")],
  ("Compara estos dos textos de ejemplo sobre la jornada escolar. Texto A: «Extender la jornada en 30 minutos permite incorporar talleres. En un colegio de ejemplo, 70 de 100 estudiantes los valoraron en una encuesta, y las notas de artes subieron.» Texto B: «Los niños necesitan descansar. Mi sobrino llega a casa agotado a las 17:00 y apenas cena. No hagamos más largos los días». Escribe la postura de cada uno, la estrategia, el tono y cuál sostiene mejor su postura y por qué.",
   "A defiende extender la jornada con talleres; usa datos de una encuesta y un tono técnico. B defiende no extenderla; usa un caso cercano y un tono emotivo. A sostiene mejor su postura porque ofrece una cifra verificable, aunque su muestra es pequeña; B solo presenta un caso.",
   ["describe la postura de ambos", "identifica estrategia y tono", "evalúa con una razón apoyada en los textos"], ["cuadro comparativo de cuatro filas en el cuaderno"],
   ["evaluar solo por gusto personal", "no distinguir dato de caso"], "Muestra tu cuadro a otra persona y pídele que señale si tu evaluación se apoya en los textos."),
  "Anota, para el tema «tareas para el fin de semana», una razón a favor y una razón en contra.",
  "Escribe un párrafo que presente una objeción a «el uniforme debe mantenerse» y la refute con una razón.")

# ================================================================== clase 7
L(OA, 7,
  "Este cuaderno y un lápiz. Los textos que se evalúan están escritos en cada ejercicio.",
  "Aprenderé a escribir una evaluación crítica de un texto argumentativo: mi postura frente a lo leído, apoyada en argumentos, y publicada para una audiencia real.",
  ["Sé reconstruir un argumento y evaluar su evidencia.", "Sé reconocer recursos del lenguaje y comparar textos."],
  ["Evaluar críticamente un texto argumentativo significa decir qué tan bien defiende su postura y cuál es mi postura frente a lo leído. Mi postura puede ser de acuerdo, de desacuerdo o de acuerdo en parte. No basta con decir «me gustó»: necesito argumentos que se apoyen en el texto y en información que yo conozca.",
   "Una evaluación escrita tiene tres partes. Primero, resume la postura del autor con una frase fiel. Segundo, evalúa: ¿las razones son claras?, ¿la evidencia es confiable y pertinente?, ¿el lenguaje apoya o reemplaza los argumentos? Tercero, expresa tu postura y la apoya con al menos una razón propia y una evidencia. Usa expresiones como «estoy de acuerdo en parte, porque…» o «discrepo, ya que…».",
   "Una evaluación pública debe ser respetuosa y pensar en su audiencia. Se critican las ideas y los argumentos, no a la persona. Se cita al autor con exactitud y se evita caricaturizar su postura. Antes de publicarla, revisa que cada afirmación tuya tenga una razón y que no hayas atribuido al autor algo que no dijo."],
  [("evaluación crítica", "juicio razonado sobre la calidad de los argumentos de un texto"), ("postura personal", "lo que yo pienso frente a lo que dice el texto"), ("fundamentar", "apoyar una afirmación con razones y evidencias"), ("caricaturizar", "exagerar la postura de otro para que parezca débil"), ("audiencia", "personas a las que se dirige un texto")],
  [("Evaluación bien fundamentada", "Texto leído: «Las clases deberían empezar a las 9:00 porque los jóvenes duermen poco». Evaluación: «El autor sostiene que el inicio de clases debe retrasarse. Su razón es clara, pero no entrega datos sobre cuántos duermen poco. Estoy de acuerdo en parte: en mi curso, 18 de 30 se acuestan después de las 23:00, pero también habría que ver el horario de salida». ¿Qué partes tiene?",
    ["Resume con fidelidad la postura del autor.", "Evalúa: razón clara, falta evidencia.", "Expresa una postura personal con un dato y una condición."], "Resumen fiel, evaluación de la evidencia y postura personal fundamentada"),
   ("Evaluación sin fundamento", "«Ese texto es malo porque el autor es aburrido y no me cae bien.» ¿Qué le falta?",
    ["Ataca a la persona y no al argumento.", "No cita razones ni evidencias del texto.", "Falta resumir la postura y dar una razón propia."], "Le faltan fidelidad al texto, criterios y razones propias")],
  [("Decir «estoy de acuerdo» sin dar una razón.", "Una postura sin razones no es una evaluación crítica.", "Agrega «porque» y una evidencia."),
   ("Criticar a la persona en vez de sus argumentos.", "Eso no evalúa el texto y puede ser injusto.", "Concéntrate en las razones, las evidencias y el lenguaje.")],
  ([E("¿Qué debe tener primero una evaluación crítica? (a) Un resumen fiel de la postura del autor. (b) Mi opinión personal sobre el tema. (c) Una conclusión sobre si el autor tiene razón.", "(a)", "Para evaluar hay que comprender bien lo que el autor sostiene."),
    E("¿Qué expresión introduce una postura de desacuerdo con razón?", "«Discrepo, ya que…»", "Marca la postura y anuncia la razón."),
    E("Mi postura frente a un texto, ¿puede ser de acuerdo en parte?", "Sí", "Se puede coincidir con algunas ideas y no con otras.")],
   [E("Un estudiante escribe: «El autor es tonto». ¿Qué falla tiene la frase?", "Ataca a la persona y no evalúa sus argumentos", "Una crítica debe referirse a las razones y a la evidencia."),
    E("Texto: «Hay que cerrar la calle del colegio porque es peligrosa». Evaluación: «Concuerdo, porque en mi barrio un auto casi atropella a un compañero». ¿Qué se agrega en la evaluación?", "Una razón y un caso propios que apoyan la postura", "El estudiante agrega un caso para respaldar su acuerdo."),
    E("¿Qué parte de la evaluación dice cuán sólido es el argumento? (a) El resumen. (b) La evaluación de razones y evidencia. (c) La despedida.", "(b)", "Es la parte que juzga la calidad del argumento.")],
   [E("Texto: «El huerto escolar mejora la alimentación porque hoy los estudiantes comen poca verdura». Escribe una evaluación de una oración que señale una debilidad.", "Por ejemplo: «La razón es clara, pero no entrega datos sobre cuánta verdura se come»", "La debilidad es la falta de evidencia."),
    E("Ordena las partes de una evaluación: 1) mi postura con una razón, 2) resumen fiel de la postura del autor, 3) valoración de razones y evidencia. ¿Cuál es el orden?", "2, 3, 1", "Primero se resume, luego se evalúa y al final se expone la postura propia."),
    E("¿Cuál es una forma respetuosa de disentir? (a) «Eso es una tontería.» (b) «Discrepo porque el dato citado es de hace veinte años.» (c) «Nadie te cree.»", "(b)", "Critica una evidencia concreta con una razón.")],
   [E("Un texto dice: «Algunos exageran la lluvia, pero yo propongo techar solo el patio». Un comentario lo resume como «El autor odia a los que se quejan de la lluvia». ¿Es un resumen fiel?", "No; caricaturiza al autor, que solo propone techar el patio", "Atribuye una emoción que el texto no muestra."),
    E("Antes de publicar tu evaluación, ¿qué debes revisar? (a) Que cada afirmación mía tenga una razón. (b) Que sea lo más larga posible. (c) Que no cite al autor.", "(a)", "Sin razones no hay evaluación crítica.")],
   [E("Evaluación: «El columnista tiene razón en que el parque necesita luz, pero cita solo a un vecino. Estoy de acuerdo en parte: yo pediría un conteo de personas que lo usan de noche». ¿Cuál es su postura personal y qué propone mejorar?", "Está de acuerdo en parte; propone sumar un conteo de personas que usan el parque de noche", "La postura es de acuerdo parcial y la mejora es un dato más amplio."),
    E("Escribe la oración que resumiría fielmente: «Propongo que los recreos tengan música suave porque 25 de 40 estudiantes dijeron relajarse con ella».", "El autor sostiene que los recreos deberían tener música suave porque a la mayoría de los consultados les ayuda a relajarse", "Resume la tesis y la razón sin exagerar.")]),
  [E("Tu curso publicará en el diario mural una evaluación de la columna «La biblioteca debe abrir los sábados». ¿Cuál oración sirve para empezar? (a) «Esta columna es una pérdida de tiempo.» (b) «El autor sostiene que la biblioteca debe abrir los sábados; evaluaré sus razones.» (c) «Yo no leo columnas.»", "(b)", "Presenta la postura del autor y anuncia la evaluación.")],
  [E("¿Qué es fundamentar una postura?", "Apoyarla con razones y evidencias", "Sin razones, una opinión no está fundamentada."),
   E("¿A quién se critica en una evaluación crítica?", "A los argumentos del texto, no a la persona", "Se analizan ideas y evidencias."),
   E("¿Qué debe hacerse con la audiencia al publicar?", "Escribir pensando en quién leerá y con respeto", "El texto debe ser claro y respetuoso para quien lo lea.")],
  ("Escribe una evaluación crítica de este texto de ejemplo, de 6 a 8 líneas, para publicarla en el diario mural del curso: «Los estudiantes de octavo deberían tener una hora libre semanal para estudiar en la biblioteca. Muchos no tienen un lugar tranquilo en casa. Además, en un curso de ejemplo, 14 de 30 dijeron que estudian mejor en silencio». Incluye el resumen de la postura, la evaluación de razón y evidencia, y tu postura personal con una razón.",
   "El autor sostiene que octavo debería tener una hora libre semanal de estudio en la biblioteca. Su razón (falta de lugar tranquilo) es clara, y la evidencia (14 de 30) es un dato, pero viene de un solo curso. Estoy de acuerdo en parte: creo que sería útil, aunque habría que consultar a más cursos.",
   ["resume con fidelidad la postura", "evalúa razón y evidencia", "expresa una postura personal con una razón"], ["texto de 6 a 8 líneas en el cuaderno"],
   ["atacar a la persona", "no dar razones para la postura propia"], "Pide a otra persona que lea tu texto y marque dónde aparece cada una de las tres partes."),
  "Subraya, en el ejemplo de respuesta de esta clase, la expresión que introduce la postura personal.",
  "Escribe dos evaluaciones del mismo texto, una de acuerdo y otra de desacuerdo, ambas con una razón propia.")

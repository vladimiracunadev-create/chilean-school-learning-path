"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 14 (escritura persuasiva breve).

Todos los textos, cuentos, cartas, datos y conteos son originales e inventados («de ejemplo»);
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


OA = "LE07 OA 14"

CUENTO = "Cuento de ejemplo «La llave del abuelo»: Inés encuentra una llave oxidada en un cajón de su abuelo. Ninguna puerta de la casa se abre con ella. Al final descubre que abre un baúl con cartas que cuentan los viajes del abuelo. En una página dice: «La llave pesaba como un recuerdo»."

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. Los asuntos, textos y audiencias están escritos en los ejercicios.",
  "Aprenderé a definir el asunto de un texto persuasivo, su audiencia y una afirmación clara que quiero defender.",
  ["Sé distinguir hechos de opiniones.", "Sé qué es un texto explicativo."],
  ["Un texto persuasivo busca convencer a una audiencia de aceptar una postura o de actuar. Son ejemplos la carta al director, el editorial y la crítica literaria. Parte con tres decisiones: el asunto (de qué trata: un tema de actualidad, como la sombra en una plaza, o un tema literario, como el mensaje de un cuento), la audiencia (a quién quiero convencer) y la afirmación (lo que sostengo).",
   "La afirmación es una oración que expresa una postura que se puede discutir. «El patio tiene tres árboles» es un hecho; «¿Debe haber más árboles en el patio?» es una pregunta; «El patio necesita más árboles» es una afirmación. Una buena afirmación es clara, tiene un solo foco y puede apoyarse con razones y evidencias. Si es obvia o imposible de discutir, no persuade.",
   "La audiencia define cómo escribes. A una autoridad le hablas con respeto y datos concretos; a tus compañeros, con ejemplos cercanos. Antes de escribir, completa esta frase: «Quiero convencer a ___ de que ___ porque ___». Si no puedes completarla, todavía no tienes una afirmación bien definida."],
  [("texto persuasivo", "texto que busca convencer a la audiencia"), ("asunto", "tema del que trata el texto"), ("afirmación", "postura clara que se puede discutir y defender"), ("audiencia", "persona o grupo al que se quiere convencer"), ("contingente", "relacionado con la actualidad")],
  [("Reconocer una afirmación", "¿Cuál es una afirmación? (1) «La plaza tiene 20 bancas.» (2) «¿Hay sombra en la plaza?» (3) «La plaza necesita más sombra.»",
    ["La 1 es un hecho comprobable.", "La 2 es una pregunta.", "La 3 expresa una postura que se puede discutir y defender."], "La 3"),
   ("Completar la frase", "Quieres convencer a la dirección del colegio de que los recreos duren 5 minutos más porque hay poco tiempo para almorzar y jugar. Completa: «Quiero convencer a ___ de que ___ porque ___».",
    ["Audiencia: la dirección del colegio.", "Afirmación: los recreos deberían durar 5 minutos más.", "Razón: hay poco tiempo para almorzar y jugar."], "Quiero convencer a la dirección de que los recreos deben durar 5 minutos más porque hay poco tiempo para almorzar y jugar")],
  [("Escribir como afirmación un dato.", "Un hecho no se puede defender ni discutir.", "Formula una postura que alguien podría rebatir."),
   ("Usar una afirmación con varios focos.", "El lector no sabe qué debe aceptar.", "Elige una sola idea para defender.")],
  ([E("«Los recreos duran 15 minutos.» ¿Es una afirmación o un hecho?", "Un hecho", "Se puede comprobar con el horario."),
    E("«¿Deberían ser más largos los recreos?» ¿Es una pregunta o una afirmación?", "Una pregunta", "No expresa una postura."),
    E("«Los recreos deberían durar 25 minutos.» ¿Es una afirmación o un hecho?", "Una afirmación", "Expresa una postura que se puede discutir.")],
   [E("¿Qué audiencia tiene una carta al director de un diario local: el director y los lectores, o solo tu familia?", "El director y los lectores", "Se publica en el diario."),
    E("Asunto: «el mensaje de un cuento». ¿Es un asunto contingente o literario?", "Literario", "Trata de una obra."),
    E("¿Cuál es una buena afirmación? (a) El patio tiene un árbol. (b) El patio necesita más árboles para dar sombra. (c) ¿Hay árboles?", "(b)", "Expresa una postura defendible.")],
   [E(f"{CUENTO} ¿Cuál es una afirmación sobre el cuento? (a) El cuento muestra que los objetos guardan recuerdos. (b) Inés tiene una llave. (c) El cuento tiene un baúl.", "(a)", "Es una interpretación que se puede defender con el texto."),
    E("Completa con la frase correcta: «Quiero convencer a ___ de que ___ porque ___». Si la audiencia es la municipalidad y la afirmación es «se reparen las luces de la calle Los Olmos», ¿cuál es una razón adecuada? (a) la calle es oscura de noche y es insegura (b) me gustan las luces (c) hay árboles", "(a)", "Justifica la petición con un problema real."),
    arith("Un editorial tiene 4 párrafos y en cada uno defiende la misma afirmación con 2 razones. ¿Cuántas razones usa en total?", "4*2", "Se multiplica el número de párrafos por las razones de cada uno.", " razones")],
   [E("Un compañero escribe: «El colegio debe cambiar el horario, los baños y el casino». ¿Qué problema tiene su afirmación?", "Tiene varios focos", "Debe elegir una sola idea para defender."),
    E("Dices: «La contaminación es mala». ¿Por qué es débil como afirmación?", "Porque es obvia y nadie la discute", "No persuade al no haber postura que defender.")],
   [E("Escribes una carta al director de un diario para pedir ciclovías seguras. ¿Quién recibe tu carta primero?", "El director del diario", "Es a quien se dirige la carta."),
    E("Elige la afirmación con un solo foco: (a) Debemos reciclar y también pintar los muros. (b) Debemos reciclar papel en cada sala. (c) Hay que reciclar, pintar y plantar.", "(b)", "Defiende una sola idea.")]),
  [E("Quieres pedir en el diario mural que el colegio ponga bebederos de agua en el patio. ¿Cuál es tu mejor afirmación? (a) Hay un patio. (b) El colegio debe instalar bebederos en el patio. (c) ¿Hay agua?", "(b)", "Es una postura clara y defendible.")],
  [E("¿Qué es una afirmación en un texto persuasivo?", "Una postura clara que se puede discutir y defender", "Es lo que se sostiene."),
   E("¿Un hecho comprobable es una afirmación defendible?", "No", "Los hechos no se discuten."),
   E("¿Qué decisión previa determina el tono y los argumentos que usarás?", "La audiencia", "Condiciona tono y argumentos.")],
  ("Elige uno de estos asuntos: A) más tiempo para la lectura en clases, B) arreglar una cancha, C) el mensaje de un cuento que conozcas. Escribe tu audiencia, tu afirmación en una oración y la frase «Quiero convencer a ___ de que ___ porque ___».",
   "Asunto B. Audiencia: la dirección del colegio. Afirmación: la cancha debe repararse antes de las clases de educación física. Quiero convencer a la dirección de que la cancha debe repararse porque tiene hoyos que pueden causar caídas.",
   ["afirmación clara", "audiencia concreta", "razón coherente"], ["tres líneas en el cuaderno"],
   ["escribir un hecho como afirmación", "usar dos focos"], "Pide a alguien que diga si podría estar en desacuerdo con tu afirmación."),
  "Escribe una afirmación sobre tu colegio y una sobre un cuento que hayas leído.",
  "Reescribe un hecho como afirmación defendible.")

# ================================================================== clase 2
L(OA, 2,
  "Este cuaderno y un lápiz. Las razones, datos y el cuento de ejemplo están escritos en los ejercicios.",
  "Aprenderé a seleccionar razones y evidencias pertinentes y suficientes que respalden una afirmación.",
  ["Sé formular una afirmación.", "Sé distinguir un hecho de una opinión."],
  ["Una razón explica por qué la afirmación es aceptable («porque…»). La evidencia es lo que respalda la razón: un dato, un ejemplo, el testimonio de alguien o, en un tema literario, una cita del texto. Por ejemplo: afirmación «La plaza necesita más sombra»; razón «las personas esperan allí al mediodía»; evidencia «12 de 20 bancas reciben sol directo, según un conteo de ejemplo».",
   "Para elegir bien, revisa tres criterios. Pertinencia: la evidencia se relaciona directamente con la razón. Suficiencia: hay evidencia bastante (un solo ejemplo no basta para algo general). Fiabilidad: la fuente es confiable y se puede verificar. Una opinión sin respaldo («es horrible») no es evidencia; tampoco lo es una generalización («todos lo piensan»).",
   "En los temas literarios, la evidencia es una cita breve del texto y la explicación de cómo apoya tu idea. Por ejemplo, para defender que un cuento trata del recuerdo, citas una frase que muestre ese tema y explicas la conexión. Registra cada evidencia con su fuente: así tu lector puede comprobarla."],
  [("razón", "motivo que explica por qué una afirmación es aceptable"), ("evidencia", "dato, ejemplo, testimonio o cita que respalda una razón"), ("pertinencia", "relación directa entre la evidencia y lo que se defiende"), ("suficiencia", "cantidad adecuada de evidencia"), ("generalización", "afirmación sobre todos a partir de pocos casos")],
  [("Razón y evidencia", "Afirmación: «El colegio debe instalar bebederos». Razón: «los estudiantes no tienen cómo tomar agua en el recreo». Evidencia propuesta: «en un conteo de ejemplo, 18 de 25 estudiantes dijeron que no tienen dónde llenar su botella». ¿Es pertinente?",
    ["La evidencia habla de si los estudiantes tienen dónde llenar su botella.", "Se relaciona directamente con la razón.", "Es un dato concreto con proporción (18 de 25)."], "Sí, es pertinente y concreta"),
   ("Evidencia literaria", f"{CUENTO} Afirmación: «El cuento muestra que los objetos guardan recuerdos». Elige la evidencia y explícala.",
    ["Cita: «La llave pesaba como un recuerdo».", "Explicación: compara un objeto con un recuerdo.", "Refuerzo: la llave abre un baúl con cartas de los viajes del abuelo."], "Cita «La llave pesaba como un recuerdo» y el baúl con cartas")],
  [("Usar «todos piensan así» como evidencia.", "Es una generalización sin respaldo.", "Usa un dato o un ejemplo verificable."),
   ("Dar una evidencia que no tiene relación con la razón.", "No apoya lo que se defiende.", "Pregunta si la evidencia habla de lo mismo que la razón.")],
  ([E("«Las bancas dan mucho calor» y «12 de 20 bancas reciben sol al mediodía (conteo de ejemplo)». ¿Cuál es evidencia?", "La segunda", "Es un dato comprobable."),
    E("¿Qué explica por qué la afirmación es aceptable: una razón o un título?", "La razón", "Responde al «porque»."),
    E("«Todos lo piensan.» ¿Es una evidencia sólida?", "No", "Es una generalización sin respaldo.")],
   [E("Afirmación: «Debe haber más basureros». ¿Cuál evidencia es pertinente? (a) En el patio hay 3 basureros para 400 estudiantes. (b) Me gusta el color verde. (c) Hoy hace calor.", "(a)", "Muestra la relación entre cantidad de basureros y estudiantes."),
    E(f"{CUENTO} ¿Qué cita puede servir para sostener que el cuento habla del recuerdo?", "«La llave pesaba como un recuerdo»", "Compara la llave con un recuerdo."),
    E("¿Qué criterio exige que haya suficiente evidencia?", "La suficiencia", "Un solo caso no basta para algo general.")],
   [arith("En un conteo de ejemplo, 18 de 25 estudiantes no tienen dónde llenar su botella. ¿Cuántos sí tienen dónde llenarla?", "25-18", "Se resta del total los que no tienen.", " estudiantes"),
    E("Un compañero afirma «los baños están mal» y da como evidencia «una vez vi una gotera». ¿Es suficiente?", "No; un solo caso no basta para una afirmación general", "Falta evidencia suficiente."),
    E("¿Qué fuente es más confiable para un dato de asistencia: el libro de clases o un rumor de pasillo?", "El libro de clases", "Se puede verificar.")],
   [E("Afirmación: «Debemos reciclar papel». Evidencia: «en el colegio hay 15 salas y en cada una se usan 30 hojas al día». ¿Es pertinente a la razón «se gasta mucho papel»?", "Sí; muestra la cantidad que se usa", "Habla del gasto de papel."),
    E("Un texto dice «El 90 % opina igual» sin indicar a quiénes se preguntó. ¿Qué criterio falla?", "La fiabilidad", "No se puede verificar la fuente.")],
   [arith("Cada sala usa 30 hojas al día y hay 15 salas. ¿Cuántas hojas se usan en un día en total?", "15*30", "Se multiplica el número de salas por las hojas de cada una.", " hojas"),
    E(f"{CUENTO} Un estudiante cita «Inés encuentra una llave» como evidencia de que el cuento habla del recuerdo. ¿Es suficiente?", "No; muestra un hecho, pero no explica la relación con el recuerdo", "Falta una cita o una explicación que conecte.")]),
  [E("Tu curso pide un domo para el recreo. Tienes dos evidencias: (1) «El 70 % de los 40 estudiantes consultados dice que se moja en los recreos de lluvia» y (2) «Mi primo opina que es una buena idea». ¿Cuál usas primero?", "La primera", "Es un dato verificable y pertinente.")],
  [E("¿Cuáles son los tres criterios para elegir evidencia?", "Pertinencia, suficiencia y fiabilidad", "Son los criterios de la clase."),
   E("¿Qué es evidencia en un tema literario?", "Una cita del texto con su explicación", "Permite comprobar la lectura."),
   E("¿Una opinión sin respaldo es evidencia?", "No", "No se puede comprobar.")],
  ("Elige una afirmación: A) «El colegio debe tener más basureros», B) «El cuento «La llave del abuelo» muestra el valor del recuerdo». Escribe dos razones y, para cada una, una evidencia pertinente (puede ser de ejemplo y debe ir rotulada como tal o una cita del cuento). Indica por qué una de tus evidencias es suficiente.",
   "Afirmación A. Razón 1: hay pocos basureros. Evidencia: en un conteo de ejemplo hay 3 basureros para 400 estudiantes. Razón 2: el patio se ensucia. Evidencia: en un conteo de ejemplo se recogieron 25 bolsas de basura en una semana. La segunda es suficiente porque cubre una semana completa.",
   ["dos razones", "evidencias pertinentes", "criterio de suficiencia explicado"], ["lista de razones y evidencias"],
   ["usar generalizaciones", "evidencia sin relación con la razón"], "Pide a alguien que diga si sus dudas desaparecen con tu evidencia."),
  "Escribe una afirmación y una evidencia verificable para ella.",
  "Busca en un texto una cita breve que apoye una idea y explica la conexión.")

# ================================================================== clase 3
L(OA, 3,
  "Este cuaderno y un lápiz. Los planes y textos están escritos en los ejercicios.",
  "Aprenderé a ordenar un recorrido persuasivo: presentación del asunto, afirmación, razones con evidencia y cierre con petición.",
  ["Sé formular afirmaciones y elegir evidencias.", "Sé usar conectores."],
  ["Un texto persuasivo breve sigue un recorrido. Primero presenta el asunto y la afirmación («Escribo para pedir que la plaza tenga más sombra»). Luego desarrolla las razones, cada una con su evidencia, en un orden lógico: de la más fuerte a la más débil, o de la más general a la más concreta. Al final cierra con una síntesis o con una petición clara.",
   "Cada género tiene sus rasgos. La carta al director empieza con «Señor director», se escribe en primera persona, presenta el problema, entrega razones y datos, hace una petición y termina con una despedida y la firma. El editorial es un texto del diario que opina sin firma personal. La crítica literaria evalúa una obra con la afirmación, citas y una conclusión.",
   "Para unir las partes usa conectores: de orden (en primer lugar, además, finalmente), de causa (porque, ya que), de consecuencia (por lo tanto) y de contraste (sin embargo). Un buen recorrido hace que el lector avance sin perderse. Antes de redactar, haz un plan con una línea por párrafo."],
  [("recorrido persuasivo", "orden en que se presentan las partes de un texto que convence"), ("petición", "pedido claro dirigido a la audiencia"), ("editorial", "texto de opinión de un medio"), ("conector de consecuencia", "palabra que muestra el resultado de lo anterior, como por lo tanto"), ("plan", "esquema de las partes antes de escribir")],
  [("Ordenar un plan", "Partes de una carta al director: (a) petición y despedida, (b) saludo y presentación del problema, (c) razón con dato, (d) segunda razón con ejemplo. Ordénalas.",
    ["Una carta parte con el saludo y el problema.", "Luego van las razones con su evidencia.", "Al final, petición y despedida."], "b, c, d, a"),
   ("Elegir conectores", "Une: «Muchos estudiantes llegan mojados. ___ el colegio debería instalar un techo». ¿Qué conector va: por lo tanto, sin embargo o antes?",
    ["La primera oración es una causa.", "La segunda es su consecuencia.", "El conector de consecuencia es «por lo tanto»."], "Por lo tanto")],
  [("Poner la petición al comienzo y luego las razones.", "El lector no sabe por qué debe aceptar el pedido.", "Primero el asunto y las razones; después la petición."),
   ("Escribir una lista de razones sin conectores.", "Se pierde la relación entre ellas.", "Usa conectores de orden y de causa.")],
  ([E("¿Con qué saludo comienza una carta al director?", "Señor director", "Es la fórmula del género."),
    E("¿Qué parte va al final de una carta: la petición o el saludo?", "La petición", "Cierra con lo que se pide."),
    E("El conector «por lo tanto», ¿expresa causa o consecuencia?", "Consecuencia", "Introduce el resultado.")],
   [E("Plan: 1) problema, 2) primera razón con dato, 3) segunda razón con ejemplo, 4) petición. ¿Cuántas razones tiene?", "2", "Son las partes 2 y 3."),
    E("¿Qué conector sirve para añadir una razón más: además o sin embargo?", "Además", "Suma una idea."),
    E("¿Qué es un editorial?", "Un texto de opinión de un medio", "No lleva la voz de una sola persona.")],
   [E("Ordena las partes de una carta: a) petición, b) saludo, c) presentación del problema, d) despedida y firma. Escribe las letras en orden.", "b, c, a, d", "Saludo, problema, petición y despedida."),
    E("Completa con el conector adecuado: «El patio es muy pequeño. ___, los estudiantes deben jugar por turnos». (a) Por lo tanto (b) Aunque (c) Antes", "(a)", "Muestra una consecuencia."),
    arith("Una carta tiene 6 párrafos: uno de saludo y problema, uno de petición, uno de despedida y el resto son de razones. ¿Cuántos párrafos son de razones?", "6-3", "Se restan los tres párrafos que no son de razones.", " párrafos")],
   [E("Orden A: razón más fuerte, razón menos fuerte, petición. Orden B: petición, razón menos fuerte, razón más fuerte. ¿Cuál es el recorrido recomendado en la clase?", "El orden A", "La petición cierra y las razones la apoyan."),
    E("Una carta al director empieza pidiendo «Quiero que arreglen la cancha» sin explicar nada. ¿Qué falta antes?", "Presentar el problema y las razones", "El lector necesita entender por qué.")],
   [E("Plan A: saludo, problema, razón 1, razón 2, petición. Plan B: saludo, razón 1, razón 2, problema. ¿Cuál es incoherente y por qué?", "El B; presenta las razones antes del problema y no tiene petición", "Falta la petición y el orden es ilógico."),
    E("Escribe qué conector elegirías para introducir el contraste: «Algunos dicen que es caro. ___, el costo es menor que el daño». (a) Sin embargo (b) Por eso (c) Además", "(a)", "Contrapone una idea con otra.")]),
  [E("Vas a escribir una carta al director del diario sobre la falta de ciclovías. ¿Cuál es el primer párrafo adecuado? (a) «Señor director: escribo para pedir ciclovías seguras en mi comuna porque hoy los ciclistas comparten la calzada con los autos». (b) «Quiero decirle que me caen mal los autos». (c) «Atentamente, Pedro».", "(a)", "Tiene saludo, asunto y afirmación.")],
  [E("¿Cómo termina una carta al director?", "Con una despedida y la firma", "Es la fórmula del género."),
   E("¿Qué parte lleva datos: las razones o el saludo?", "Las razones", "Allí va la evidencia."),
   E("¿Para qué sirve un plan antes de escribir?", "Para ordenar las partes del texto", "Evita el desorden y los saltos.")],
  ("Con la afirmación «El colegio debe instalar más basureros» arma el plan de una carta al director del colegio: escribe una línea para cada una de estas partes: saludo, presentación del problema, razón 1 con evidencia, razón 2 con evidencia, petición, despedida. Usa tres conectores distintos.",
   "Saludo: Señora directora. Problema: el patio se llena de basura. Razón 1: hay 3 basureros para 400 estudiantes (conteo de ejemplo). Razón 2: además, el viento esparce papeles. Petición: por lo tanto, pido instalar 6 basureros más. Despedida: Atentamente, Camila.",
   ["incluye las seis partes", "orden lógico", "tres conectores distintos"], ["plan de seis líneas"],
   ["petición al comienzo", "olvidar la evidencia"], "Lee tu plan a otra persona y pregúntale si la petición queda justificada."),
  "Ordena las partes de una carta con papelitos recortados.",
  "Escribe un plan para una crítica literaria breve de un cuento conocido.")

# ================================================================== clase 4
CARTA = "Señor director: Quiero reclamar por la falta de sombra en la plaza Los Aromos. Según un conteo de ejemplo, 12 de las 20 bancas reciben sol directo al mediodía. Por eso muchas personas no pueden esperar allí sin quemarse. Además, el municipio gastó mucho en luces, que son una tontería. Pido que se planten cuatro árboles. Atentamente, Luz Ortega."
L(OA, 4,
  "Este cuaderno y un lápiz. La carta y los borradores están escritos en los ejercicios.",
  "Aprenderé a redactar un texto persuasivo manteniendo el foco temático: cada párrafo y cada oración apoyan la afirmación.",
  ["Sé ordenar un recorrido persuasivo.", "Sé elegir evidencia pertinente."],
  ["Mantener el foco es hacer que todo el texto hable de lo mismo: la afirmación. Esto se llama coherencia temática. Cada párrafo desarrolla una razón y cada oración aporta información sobre esa razón. Una digresión es una idea que se aparta del tema. Aunque sea interesante, debilita el texto porque desvía la atención y puede restar credibilidad.",
   "Para redactar con foco, escribe primero la afirmación y tenla a la vista. Después de cada párrafo, pregúntate: ¿esto apoya mi afirmación? Si la respuesta es no, elimínalo o muévelo. También cuida la cohesión: usa conectores y retoma lo ya dicho con pronombres o sinónimos, así el lector percibe un hilo continuo.",
   "El tono forma parte de la coherencia. Si pides algo a una autoridad, evita insultos y exageraciones: un ataque desvía el tema y perjudica tu causa. Es preferible expresar el desacuerdo con claridad y respeto («considero insuficiente…») que con descalificaciones («es una tontería»). Revisa que tu petición final sea concreta y coherente con tus razones."],
  [("coherencia temática", "relación de todas las partes con un mismo tema"), ("digresión", "idea que se aparta del tema central"), ("cohesión", "unión de las oraciones mediante conectores y referencias"), ("tono", "actitud con que se escribe, como respetuoso o agresivo"), ("petición concreta", "pedido claro y realizable")],
  [("Detectar una digresión", f"{CARTA} ¿Qué oración se aparta del tema de la sombra en la plaza?",
    ["La afirmación es la falta de sombra en la plaza.", "La oración «el municipio gastó mucho en luces, que son una tontería» habla de otro tema y descalifica.", "Se debe eliminar o reformular."], "«Además, el municipio gastó mucho en luces, que son una tontería.»"),
   ("Mejorar el tono", "Reformula con respeto: «Es una tontería que no haya árboles».",
    ["Mantengo la idea: faltan árboles.", "Quito la descalificación.", "Expreso la postura con claridad y respeto."], "«Considero necesario que la plaza tenga más árboles»")],
  [("Agregar un reclamo distinto en medio de la carta.", "Desvía al lector y debilita la afirmación.", "Reserva cada carta para un solo asunto."),
   ("Usar insultos para parecer más firme.", "Pierdes credibilidad y el lector se pone a la defensiva.", "Expresa el desacuerdo con respeto.")],
  ([E(f"{CARTA} ¿Cuál es el asunto de la carta?", "La falta de sombra en la plaza", "Lo dice en la presentación."),
    E(f"{CARTA} ¿Qué dato aparece como evidencia?", "12 de las 20 bancas reciben sol directo al mediodía", "Es el conteo de ejemplo."),
    E("¿Qué es una digresión?", "Una idea que se aparta del tema central", "Desvía la atención del lector.")],
   [E(f"{CARTA} ¿Qué petición hace la carta?", "Que se planten cuatro árboles", "Está al final del texto."),
    E("¿El tono «es una tontería» es respetuoso o descalificador?", "Descalificador", "Ataca en vez de argumentar."),
    E("¿Qué conector de la carta introduce una consecuencia?", "Por eso", "Une el dato con el efecto en las personas.")],
   [E(f"{CARTA} Reescribe la oración sobre las luces para que apoye el tema. ¿Cuál sirve? (a) Además, la sombra permitiría que las personas esperen cómodas. (b) Las luces cuestan mucho. (c) Las luces son feas.", "(a)", "Mantiene el foco en la sombra."),
    E("Un párrafo defiende bebederos y de pronto habla de lo caro del casino. ¿Qué haces?", "Eliminar o mover esa idea", "No apoya la afirmación."),
    arith("Una carta tiene 8 oraciones y 2 se apartan del tema. ¿Cuántas oraciones apoyan la afirmación?", "8-2", "Se restan las digresiones del total.", " oraciones")],
   [E(f"{CARTA} Luz piensa que mencionar las luces refuerza su carta porque muestra que el municipio gasta mal. ¿Por qué debilita su argumento?", "Porque desvía del tema de la sombra y suena a ataque", "Se aparta de la afirmación."),
    E("Dos cartas piden lo mismo. La primera usa «por favor» y datos; la segunda dice «ustedes son unos inútiles». ¿Cuál tiene más posibilidades de convencer?", "La primera", "El respeto y los datos apoyan la causa.")],
   [E("Revisa: «El patio es pequeño. Hay 600 estudiantes. Mi perro se llama Bruno. Por eso pido ampliar el patio». ¿Qué oración sobra?", "«Mi perro se llama Bruno»", "No apoya la afirmación."),
    E("Completa con una petición concreta: «Por lo tanto, solicito ___». (a) que se instalen dos techos en el patio (b) que todo cambie (c) que no me molesten", "(a)", "Es realizable y concreta.")]),
  [E("Escribes al director del colegio por la falta de agua en los baños. Tu borrador incluye una queja por el color de las paredes. ¿Qué haces?", "La elimino o hago otra carta", "Mantiene el foco en un solo asunto.")],
  [E("¿Qué es coherencia temática?", "Que todo el texto hable del mismo tema", "Todo apoya la afirmación."),
   E("¿Se debe usar insultos para dar fuerza a una petición?", "No", "Debilitan la credibilidad."),
   E("¿Cómo es una petición concreta?", "Clara y realizable", "Se puede cumplir.")],
  ("Redacta una carta al director (cinco a siete líneas) con este asunto: pedir un techo para el paradero del colegio. Datos de ejemplo: 30 estudiantes esperan allí cada mañana y cuando llueve se mojan. Debe tener saludo, afirmación, una razón con el dato, una segunda razón, petición concreta, tono respetuoso y ninguna digresión.",
   "Señor director: Escribo para pedir que se instale un techo en el paradero del colegio. Cada mañana 30 estudiantes (dato de ejemplo) esperan allí y, cuando llueve, llegan mojados a clases. Además, la ropa mojada incomoda durante la primera clase. Por lo tanto, solicito que se coloque un techo antes del invierno. Atentamente, Julián Reyes.",
   ["mantiene el foco", "usa el dato", "tono respetuoso con petición concreta"], ["carta de cinco a siete líneas"],
   ["agregar otros reclamos", "usar descalificaciones"], "Marca con color cada oración y verifica que todas apoyen la afirmación."),
  "Escribe una oración que apoye la afirmación «los estudiantes necesitan más tiempo de lectura».",
  "Toma una carta tuya y subraya cualquier digresión.")

# ================================================================== clase 5
L(OA, 5,
  "Este cuaderno y un lápiz. Las objeciones y respuestas están escritas en los ejercicios.",
  "Aprenderé a incorporar una objeción pertinente y a responderla con una concesión y una refutación.",
  ["Sé mantener el foco y el tono en un texto persuasivo.", "Sé usar conectores de contraste."],
  ["Una objeción es una razón que alguien podría oponer a nuestra afirmación. Incluirla muestra que conocemos otras miradas y hace nuestro texto más creíble. Una objeción pertinente se relaciona directamente con la afirmación (por ejemplo: «plantar árboles cuesta dinero»); una impertinente la ataca desde otro tema o contra la persona («tú no entiendes de plazas»).",
   "Para responder, usa dos pasos. La concesión reconoce lo que tiene de cierto la objeción: «Es verdad que plantar árboles tiene un costo». La refutación explica por qué, aun así, nuestra postura se mantiene: «Sin embargo, ese costo es menor que el de reparar bancas dañadas por el sol». Conectores útiles: es cierto que, si bien, sin embargo, no obstante, aun así.",
   "Cuidado con las falacias, que son razonamientos engañosos: atacar a la persona en vez de su idea, decir que todos opinan igual, o exagerar la objeción para derrotarla fácilmente. Tu objeción debe ser la más fuerte que pueda hacer alguien razonable. Y tu respuesta debe apoyarse en evidencia, no solo en tu opinión."],
  [("objeción", "razón que se opone a una afirmación"), ("concesión", "reconocimiento de lo que tiene de cierto la objeción"), ("refutación", "respuesta que explica por qué se mantiene la postura"), ("falacia", "razonamiento engañoso"), ("pertinente", "que se relaciona directamente con el tema")],
  [("Concesión y refutación", "Afirmación: «Debemos plantar árboles en la plaza». Objeción: «Cuesta dinero». Responde con concesión y refutación.",
    ["Concesión: es verdad que plantar árboles tiene un costo.", "Refutación: el costo es menor que el de reparar bancas dañadas por el sol.", "Uno con «sin embargo»."], "«Es verdad que plantar árboles tiene un costo; sin embargo, es menor que reparar las bancas dañadas por el sol.»"),
   ("Objeción pertinente", "Afirmación: «Los recreos deben ser más largos». ¿Cuál objeción es pertinente? (1) «Se perdería tiempo de clases.» (2) «Tú eres flojo.»",
    ["La 1 se relaciona con la duración de los recreos.", "La 2 ataca a la persona, no a la idea.", "Solo la 1 es pertinente."], "La 1")],
  [("Responder a la objeción atacando a la persona.", "Es una falacia y no responde al argumento.", "Responde con evidencia a la idea."),
   ("Inventar una objeción tan débil que sea fácil de vencer.", "El lector lo nota y pierde confianza.", "Usa la objeción más razonable.")],
  ([E("¿Qué es una objeción?", "Una razón que se opone a la afirmación", "Muestra otra mirada."),
    E("«Es verdad que…» al comienzo de una oración, ¿introduce una concesión o una refutación?", "Una concesión", "Reconoce lo cierto de la objeción."),
    E("«Sin embargo…» ¿marca un contraste o una causa?", "Un contraste", "Se opone a lo anterior.")],
   [E("Afirmación: «Hay que instalar bebederos». Objeción: «Cuestan dinero». ¿La objeción es pertinente?", "Sí", "Se relaciona con la instalación."),
    E("«Los que piensan eso son tontos.» ¿Es una objeción pertinente o un ataque a la persona?", "Un ataque a la persona", "No discute la idea."),
    E("¿Qué hace la refutación: reconoce o explica por qué se mantiene la postura?", "Explica por qué se mantiene la postura", "Responde con evidencia.")],
   [E("Completa: «Si bien instalar basureros tiene un costo, ___». (a) también ayuda a mantener limpio el patio y evita multas por suciedad (b) es un gasto que no vale la pena (c) los basureros pueden ser de color verde", "(a)", "Responde con un beneficio relacionado."),
    E("Objeción: «Los recreos largos reducen el tiempo de clases». ¿Qué evidencia sirve para refutar? (a) El tiempo total de clases solo baja 5 minutos por día. (b) Los profesores son simpáticos. (c) Nadie lo notaría.", "(a)", "Es un dato pertinente."),
    arith("Los recreos se alargan 5 minutos por día durante 5 días a la semana. ¿Cuántos minutos de clases se pierden en una semana?", "5*5", "Se multiplica la pérdida diaria por los días.", " minutos")],
   [E("Un estudiante responde a la objeción «es caro» diciendo «eso no importa». ¿Qué falta?", "Reconocer lo cierto y dar evidencia", "Falta concesión y refutación."),
    E("«Todos están de acuerdo conmigo, así que no hay objeciones.» ¿Qué tipo de error es?", "Una falacia de generalización", "Afirma que todos piensan igual sin respaldo.")],
   [E("Escribe qué conector usarías para la concesión: «___ la obra cuesta, beneficia a 400 estudiantes». (a) Si bien (b) Porque (c) Antes", "(a)", "Introduce una concesión."),
    E("Una objeción sobre la ciclovía: «ocupa espacio de los autos». Elige la mejor respuesta: (a) Es cierto que quita espacio, pero reduce accidentes con ciclistas. (b) Los autos son malos. (c) Nadie usa autos.", "(a)", "Concede y refuta con una ventaja.")]),
  [E("Tu carta pide más tiempo de lectura. Un compañero objeta: «Hay poco tiempo en el horario». ¿Qué respondes? (a) Es verdad que el horario es acotado, pero 10 minutos diarios caben y mejoran la comprensión. (b) Eres flojo. (c) No importa.", "(a)", "Concede y refuta con datos.")],
  [E("¿Qué dos pasos tiene la respuesta a una objeción?", "Concesión y refutación", "Reconoce y responde."),
   E("¿Qué es una falacia?", "Un razonamiento engañoso", "Parece válido pero no lo es."),
   E("¿La objeción debe ser débil o razonable?", "Razonable", "Así el texto gana credibilidad.")],
  ("Escribe un párrafo de cinco líneas que defienda: «El colegio debe permitir a los estudiantes llenar sus botellas en bebederos». Incluye una objeción pertinente («cuesta instalar los bebederos»), una concesión, una refutación con dato de ejemplo y una petición.",
   "Pido que el colegio instale bebederos para llenar botellas. Es verdad que instalarlos tiene un costo; sin embargo, ahorraría la compra de botellas desechables, que según un conteo de ejemplo suman 50 por semana. Por lo tanto, solicito instalar dos bebederos.",
   ["objeción pertinente", "concesión y refutación", "petición final"], ["párrafo de cinco líneas"],
   ["atacar a la persona", "refutar sin evidencia"], "Pregunta a alguien si la objeción que elegiste le parece razonable."),
  "Escribe una objeción posible a una afirmación tuya.",
  "Escribe dos refutaciones distintas a la misma objeción.")

# ================================================================== clase 6
L(OA, 6,
  "Este cuaderno y un lápiz. Los borradores y el cuento de ejemplo están escritos en los ejercicios.",
  "Aprenderé a revisar un texto persuasivo para comprobar su efecto, su coherencia y su tono, incluyendo una crítica literaria breve.",
  ["Sé redactar con foco, razones y objeciones.", "Sé citar un texto."],
  ["Revisar un texto persuasivo es comprobar si cumple su propósito: convencer a la audiencia. Usa una lista de verificación: (1) ¿la afirmación es clara?, (2) ¿las razones son pertinentes y tienen evidencia?, (3) ¿mantiene el foco?, (4) ¿incluye una objeción respondida?, (5) ¿el tono es respetuoso y apropiado a la audiencia?, (6) ¿hay una petición o cierre claro?",
   "La crítica literaria es un género persuasivo que evalúa una obra. Tiene una afirmación sobre la obra («el cuento muestra el peso de los recuerdos»), razones apoyadas en citas del texto y una conclusión. Por ejemplo: «El cuento muestra que los objetos guardan recuerdos: la llave 'pesaba como un recuerdo' y abre un baúl con cartas». Una buena crítica distingue su opinión de lo que dice la obra y no cuenta todo el final.",
   "El efecto también se comprueba leyendo en voz alta o pidiendo a alguien de la audiencia que lo lea. Pregúntale: ¿qué entendiste que quería?, ¿qué parte te convenció menos? Con esas respuestas, revisa y reescribe. Revisar es una oportunidad de mejorar, no una señal de que el texto salió mal."],
  [("lista de verificación", "conjunto de preguntas para revisar un texto"), ("crítica literaria", "texto que evalúa una obra con razones y citas"), ("efecto", "resultado que el texto produce en el lector"), ("registro formal", "manera cuidada de hablar o escribir ante una autoridad"), ("reescribir", "volver a escribir mejorando el texto")],
  [("Aplicar la lista", "Borrador: «Señor director: la plaza es horrible. Todos lo saben. Arréglenla». Revísalo con la lista.",
    ["Afirmación: poco clara («horrible»).", "Razones y evidencia: no hay datos.", "Tono: descalificador y sin petición concreta."], "Faltan razones con evidencia, tono respetuoso y una petición concreta"),
   ("Crítica literaria", f"{CUENTO} Escribe una afirmación y una evidencia para una crítica.",
    ["Afirmación: el cuento muestra que los objetos guardan recuerdos.", "Evidencia: la frase «La llave pesaba como un recuerdo».", "Apoyo: la llave abre un baúl con cartas de los viajes del abuelo."], "El cuento muestra que los objetos guardan recuerdos: «La llave pesaba como un recuerdo»")],
  [("Revisar solo la ortografía.", "No se evalúa si convence.", "Usa toda la lista de verificación."),
   ("Contar todo el cuento en una crítica.", "Se pierde la postura y se arruina la lectura.", "Cita lo necesario y defiende una afirmación.")],
  ([E("¿Qué es una crítica literaria?", "Un texto que evalúa una obra con razones y citas", "Es un género persuasivo."),
    E("¿Para qué se revisa un texto persuasivo?", "Para comprobar si cumple su propósito de convencer", "Ese es su propósito principal."),
    E("¿Una crítica debe contar todo el final del cuento?", "No", "Debe defender una afirmación sin arruinar la lectura.")],
   [E("Borrador: «Señor director: los baños están muy sucios. Tomen medidas ya». ¿Qué le falta: evidencia o saludo?", "Evidencia", "No hay datos que respalden."),
    E(f"{CUENTO} ¿Cuál afirmación es adecuada para una crítica? (a) El cuento muestra que los objetos guardan recuerdos. (b) El cuento tiene un baúl. (c) Inés es una niña.", "(a)", "Es una interpretación defendible."),
    E("¿Qué tono corresponde a una carta al director: formal y respetuoso o informal con jerga del chat?", "Formal y respetuoso", "Es el adecuado para esa audiencia.")],
   [E("Lista de verificación: 6 preguntas. Tu texto cumple 4. ¿Cuántas debes mejorar?", "2", "Se resta lo cumplido del total."),
    E("Una lectora dice: «Entendí que quieres un techo, pero no sé por qué». ¿Qué debes agregar?", "Razones con evidencia", "Falta justificar la petición."),
    E(f"{CUENTO} Elige la cita que apoya que el cuento trata del recuerdo: (a) «La llave pesaba como un recuerdo». (b) «Inés encuentra una llave». (c) «Nada se abre en la casa».", "(a)", "Relaciona la llave con el recuerdo.")],
   [E("Un estudiante revisa su carta, cambia dos comas y dice que ya está lista. ¿Qué falta?", "Revisar afirmación, razones, foco y tono", "La revisión es más que la ortografía."),
    E("Una crítica dice: «El cuento es malo porque no me gustó». ¿Qué problema tiene?", "Es solo una opinión sin razones ni citas", "No hay evidencia del texto.")],
   [arith("Una crítica tiene 3 razones y cada una usa 1 cita y 1 explicación. ¿Cuántos elementos de apoyo (citas y explicaciones) tiene?", "3*2", "Cada razón suma dos elementos.", " elementos"),
    E("Escribe la mejor revisión de «La plaza es horrible»: (a) «La plaza necesita más sombra: 12 de 20 bancas reciben sol al mediodía (conteo de ejemplo)». (b) «Odio la plaza». (c) «La plaza, plaza».", "(a)", "Es clara, tiene evidencia y tono adecuado.")]),
  [E("Entregas tu carta a un compañero y dice: «Me convenciste, pero el tono del tercer párrafo suena agresivo». ¿Qué haces?", "Reescribo el párrafo con un tono respetuoso", "El efecto mejora con un tono apropiado.")],
  [E("¿Cuántas preguntas tiene la lista de verificación de la clase?", "Seis", "Va de afirmación a petición."),
   E("¿Qué es el efecto de un texto?", "El resultado que produce en el lector", "Se comprueba con otra persona."),
   E("¿La revisión es solo ortografía?", "No", "También evalúa razones, foco y tono.")],
  ("Revisa este borrador de ejemplo con la lista de seis preguntas y escríbelo mejor: «Señor director: la cancha es un desastre. Todos lo saben y nadie hace nada. Arréglenla pronto». Datos de ejemplo: la cancha tiene 4 hoyos y 2 estudiantes se cayeron este mes.",
   "Señor director: Escribo para pedir que se repare la cancha del colegio. Tiene 4 hoyos y este mes 2 estudiantes se cayeron (datos de ejemplo). Es cierto que repararla tiene un costo, pero evitará accidentes. Por lo tanto, solicito que se tapen los hoyos antes del campeonato. Atentamente, Sofía Tapia.",
   ["afirmación clara", "evidencia con los datos", "tono y petición adecuados"], ["borrador mejorado"],
   ["repetir el tono agresivo", "olvidar la petición"], "Lee tu versión final en voz alta y pide a alguien que la califique con la lista."),
  "Aplica la lista de seis preguntas a una carta tuya.",
  "Escribe una crítica de seis líneas de un cuento que conozcas.")

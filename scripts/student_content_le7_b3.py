"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 11 (estrategias de comprensión según el propósito).

Todos los textos, menús, bitácoras y descripciones de imágenes o sonidos son originales e inventados («de ejemplo»);
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


OA = "LE07 OA 11"

MENU = "Menú de ejemplo: 1) «Cómo armar un huerto en macetas» (instructivo, 2 páginas); 2) «La noche del faro apagado» (cuento, 12 páginas); 3) «Los glaciares y el hielo» (artículo informativo, 3 páginas); 4) «Más lectura en el colegio» (carta argumentativa, 1 página); 5) «Versos del cerro» (poema, 1 página); 6) «Ruta en bicicleta por la ciudad» (reportaje con mapa y fotos, 2 páginas)."

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. El menú de textos está escrito en los ejercicios.",
  "Aprenderé a definir para qué voy a leer, a elegir un texto según ese propósito y a anticipar qué podría dificultarme.",
  ["Sé que leo para informarme, entretenerme o aprender a hacer algo.", "Sé reconocer algunos géneros, como cuento, poema o artículo."],
  ["Leer con estrategia comienza antes de la primera línea: decido para qué leo. El propósito de lectura puede ser informarme sobre un tema, aprender un procedimiento (cómo hacer algo), disfrutar de una historia o de la belleza del lenguaje, o preparar una opinión. Según el propósito elijo el texto y la manera de leerlo: un instructivo se lee con atención a cada paso; un poema, saboreando las imágenes.",
   "Luego anticipo dificultades. Al mirar el título, el género, la extensión y la primera página puedo prever problemas frecuentes: palabras desconocidas, referentes que se pierden (no sé a quién o a qué se refiere un pronombre), información que no coincide con lo que yo sé, o recursos que debo relacionar con el texto, como mapas o fotos. Anticipar permite preparar una solución: buscar una palabra, releer, o consultar otra fuente.",
   "Todo esto se puede registrar en una bitácora de cinco partes: propósito, elección, expectativa (qué espero aprender o sentir), dificultad prevista y decisión (cómo voy a enfrentarla). Al final de la lectura vuelvo a la bitácora para comprobar si logré mi propósito y qué estrategia me ayudó."],
  [("propósito de lectura", "razón por la que leo un texto"), ("estrategia", "plan que uso para comprender mejor"), ("anticipar", "prever qué podría pasar antes de leer"), ("expectativa", "lo que espero aprender o sentir"), ("bitácora", "registro ordenado de mi lectura")],
  [("Elegir según el propósito", f"{MENU} Quieres aprender a plantar lechugas en una maceta. ¿Qué texto eliges y por qué?",
    ["Mi propósito es aprender un procedimiento.", "El texto 1 es un instructivo sobre huertos en macetas.", "Los demás son cuento, artículo, carta, poema y reportaje: no explican pasos."], "El texto 1, porque es un instructivo"),
   ("Anticipar una dificultad", "Primera línea del texto 3: «Los glaciares son grandes masas de hielo que se forman por acumulación de nieve durante siglos». Si no conoces «acumulación», ¿qué dificultad anticipas y qué harás?",
    ["Hay una palabra que no conozco: es un problema de vocabulario.", "Puedo deducirla por el contexto: «acumulación de nieve durante siglos» sugiere que se junta mucha nieve.", "Si no basta, la busco en el diccionario."], "Vocabulario desconocido; la deduzco por contexto o la busco en el diccionario")],
  [("Elegir un texto solo por lo corto que es.", "Un texto corto puede no servir para tu propósito.", "Primero define el propósito y luego revisa el menú."),
   ("Empezar a leer sin pensar qué podría costarte.", "Las dificultades te sorprenden y pierdes el hilo.", "Mira el título y la primera página para anticipar.")],
  ([E(f"{MENU} Quieres disfrutar una historia de misterio. ¿Qué número eliges?", "El 2", "Es un cuento y el título sugiere misterio."),
    E("En Lenguaje: ¿Qué es el propósito de lectura?", "La razón por la que leo un texto", "Define qué texto elijo y cómo lo leo."),
    E("Si el propósito es aprender a hacer algo, ¿conviene un instructivo o un poema?", "Un instructivo", "Muestra pasos para hacer algo.")],
   [E(f"{MENU} Quieres informarte sobre cómo se forman los glaciares. ¿Qué número eliges?", "El 3", "Es un artículo informativo sobre glaciares."),
    E("Primera línea de un texto: «El trasbordo de la línea 5 exige validar el pasaje inicial». Si no conoces «validar», ¿qué dificultad anticipas?", "Vocabulario desconocido", "Es una palabra que no se conoce."),
    E("«Espero aprender cuánto hielo hay en un glaciar.» ¿Es una expectativa o una dificultad?", "Una expectativa", "Dice lo que se espera aprender.")],
   [arith("El cuento del menú tiene 12 páginas y lees 4 páginas diarias. ¿Cuántos días necesitas para terminarlo?", "12//4", "Se divide el total de páginas entre las páginas por día.", " días"),
    E(f"{MENU} El texto 6 trae mapa y fotos. ¿Qué dificultad propia de los textos con imágenes puedes anticipar?", "Relacionar el mapa y las fotos con el texto escrito", "Es un texto con imágenes que debe leerse junto con la escritura."),
    E(f"{MENU} Tienes 30 minutos y lees 1 página cada 6 minutos. ¿Cuál alcanzas a leer completo: el cuento de 12 páginas o el artículo de 3 páginas?", "El artículo de 3 páginas", "En 30 minutos lees 5 páginas: el artículo cabe y el cuento no.")],
   [E(f"{MENU} Un compañero quiere aprender a plantar y escoge el texto 5 porque tiene una sola página. ¿Su elección sirve a su propósito?", "No; un poema no enseña a plantar", "No coincide con el propósito de aprender un procedimiento."),
    E(f"{MENU} Quieres preparar tu opinión sobre cuánto debe leerse en clases. ¿Qué texto del menú te sirve más?", "El 4", "Es una carta argumentativa sobre más lectura en el colegio.")],
   [E(f"{MENU} Tienes 20 minutos y quieres disfrutar la belleza del lenguaje en un texto muy breve. ¿Qué número eliges?", "El 5", "Es un poema de una página."),
    arith("Quieres leer todo el menú: 2, 12, 3, 1, 1 y 2 páginas. Lees 3 páginas al día. ¿Cuántos días necesitas?", "(2+12+3+1+1+2)//3", "Se suman las páginas del menú y se divide entre las páginas diarias.", " días")]),
  [E("Vas a leer para preparar una exposición sobre el hielo del mundo. ¿Qué propósito de lectura tienes: informarte o disfrutar un cuento?", "Informarte", "Necesitas datos para exponer.")],
  [E("¿Qué cinco partes tiene la bitácora de la clase? Nombra dos.", "Propósito, elección, expectativa, dificultad o decisión", "Son las partes de la bitácora."),
   E("¿Qué es anticipar una dificultad?", "Prever qué podría costarme antes de leer", "Permite preparar una solución."),
   E("¿Qué se mira para anticipar: título, género y primera página?", "Sí", "Esos datos permiten prever problemas.")],
  ("Con el menú de esta clase, completa una bitácora de cinco partes para este propósito: preparar una opinión sobre la lectura en el colegio. " + MENU + " Anota propósito, elección, expectativa, dificultad prevista y decisión.",
   "Propósito: preparar mi opinión. Elección: texto 4. Expectativa: encontrar argumentos y datos. Dificultad prevista: palabras como «proponemos» o términos técnicos. Decisión: marcar lo que no entienda y buscarlo.",
   ["elige un texto coherente con el propósito", "anticipa una dificultad real", "propone una decisión"], ["bitácora de cinco partes"],
   ["elegir un texto que no sirve al propósito", "no dar una decisión"], "Compara tu bitácora con la de otra persona y revisa si eligieron igual."),
  "Anota el propósito con que leerías hoy un texto de tu casa.",
  "Inventa un menú de tres textos y define un propósito para cada uno.")

# ================================================================== clase 2
ABEJAS = "Las abejas y los frutos. Las abejas visitan las flores para beber néctar. Mientras lo hacen, el polen se pega a su cuerpo y pasa de flor en flor. Gracias a ese traslado, las flores se fecundan y después se forman los frutos. Por eso, si desaparecieran las abejas, habría menos frutos y semillas."
CICLO = "Ciclovía de la avenida Norte. En la mañana, la ciclovía tiene más usuarios que en la tarde: 240 ciclistas entre las 7:00 y las 9:00, frente a 150 entre las 17:00 y las 19:00. En cambio, la cantidad de micros que pasan es parecida en ambos horarios."
L(OA, 2,
  "Este cuaderno y un lápiz. Los textos que se resumen están escritos en los ejercicios.",
  "Aprenderé a resumir un texto conservando las relaciones entre sus ideas (causa, consecuencia, secuencia y contraste).",
  ["Sé encontrar la idea principal de un párrafo.", "Sé qué es un conector."],
  ["Resumir es escribir con pocas palabras lo esencial de un texto. Un buen resumen es más breve que el original, usa tus propias palabras y conserva las ideas principales y las relaciones entre ellas. Si el texto dice que algo ocurre «por eso» o «en cambio», el resumen debe mantener esa causa o ese contraste; si no, cambia el sentido.",
   "Para resumir sigue estos pasos: (1) lee el texto completo; (2) subraya la idea principal de cada párrafo; (3) tacha detalles, ejemplos y repeticiones; (4) une las ideas con conectores como porque, por eso, luego o en cambio; (5) revisa que no agregaste opiniones y que no cambiaste el sentido.",
   "Las relaciones más frecuentes son causa-consecuencia (algo provoca otra cosa), secuencia (pasos u orden en el tiempo), comparación o contraste (semejanzas y diferencias) y problema-solución. Antes de resumir pregúntate cuál relación domina el texto. Un resumen que solo lista datos sueltos no ayuda a comprender: debe mostrar cómo se conectan."],
  [("resumen", "versión breve de un texto con sus ideas principales"), ("idea principal", "lo más importante que dice un párrafo o un texto"), ("detalle", "dato menor que se puede omitir"), ("relación causa-consecuencia", "conexión entre lo que provoca algo y lo que resulta"), ("contraste", "relación que muestra una diferencia")],
  [("Resumir una causa", f"{ABEJAS} Resume el texto conservando la relación causa-consecuencia.",
    ["Idea principal: las abejas trasladan polen mientras buscan néctar.", "Consecuencia: eso permite que se formen frutos.", "Relación final: si desaparecieran, habría menos frutos y semillas."], "Las abejas trasladan polen al buscar néctar y así se forman los frutos; sin ellas habría menos frutos y semillas"),
   ("Resumir un contraste", f"{CICLO} Resume el texto conservando el contraste.",
    ["Idea 1: más ciclistas en la mañana (240) que en la tarde (150).", "Idea 2: las micros se mantienen parecidas.", "Conector: «en cambio» marca el contraste."], "Hay más ciclistas en la mañana que en la tarde, mientras las micros se mantienen parecidas")],
  [("Copiar frases enteras del texto.", "No es resumir sino repetir y no se acorta bien.", "Escribe con tus palabras y quita detalles."),
   ("Quitar los conectores y dejar datos sueltos.", "Se pierde la relación entre las ideas.", "Conserva causa, secuencia o contraste.")],
  ([E(f"{ABEJAS} ¿Cuál es la idea principal del texto?", "Las abejas, al buscar néctar, trasladan polen y permiten que se formen frutos", "Resume la acción y su consecuencia."),
    E(f"{ABEJAS} ¿Qué relación expresa «Por eso»?", "Consecuencia", "Indica lo que resulta de lo anterior."),
    E("Un resumen debe ser más breve que el original. ¿Verdadero o falso?", "Verdadero", "Esa es una condición del resumen.")],
   [E(f"{ABEJAS} ¿Cuál resumen conserva la relación causal? (a) Las abejas llevan polen entre flores y por eso se forman frutos. (b) Las abejas visitan flores. (c) Hay flores y frutos.", "(a)", "Mantiene la causa y la consecuencia."),
    E(f"{CICLO} ¿Qué conector marca el contraste?", "En cambio", "Opone la ciclovía con las micros."),
    E(f"{ABEJAS} Ordena los pasos del texto: a) se forman los frutos, b) el polen se pega a la abeja, c) las abejas visitan las flores, d) el polen pasa de flor en flor. Escribe las letras en orden.", "c, b, d, a", "Es la secuencia que sigue el texto.")],
   [arith(f"{CICLO} ¿Cuántos ciclistas más hubo en la mañana que en la tarde?", "240-150", "Se resta la cantidad de la tarde a la de la mañana.", " ciclistas"),
    E(f"{CICLO} ¿Cuál resumen conserva el contraste? (a) Hay 240 ciclistas. (b) Hay más ciclistas en la mañana que en la tarde, pero las micros se mantienen parecidas. (c) Pasan micros y ciclistas.", "(b)", "Mantiene la diferencia entre ciclistas y micros."),
    E(f"{ABEJAS} Un estudiante resume: «Las abejas visitan flores y por eso desaparecen». ¿Respeta la relación del texto?", "No; el texto no dice que desaparezcan por eso", "Cambia la relación causal.")],
   [E("Un resumen dice: «Las abejas son importantes». ¿Por qué es insuficiente para el texto de las abejas?", "Porque no dice por qué ni cómo conecta las ideas", "Pierde la relación causa-consecuencia."),
    E("Un resumen de 120 palabras para un texto de 80 palabras, ¿es un resumen?", "No; debe ser más breve", "Un resumen se acorta respecto del original.")],
   [arith("Un texto tiene 80 palabras y quieres un resumen de la cuarta parte. ¿Cuántas palabras tendrá?", "80//4", "Se divide el total entre 4.", " palabras"),
    E(f"{ABEJAS} Un resumen dice: «Las abejas se pegan al polen y por eso hay frutos». ¿Qué relación altera?", "La dirección de la causa: es el polen el que se pega a la abeja", "Invierte quién hace qué.")]),
  [E("Para una exposición resumirás el siguiente párrafo: «El río se secó en verano. Por eso los pescadores trasladaron sus botes al lago. En cambio, los agricultores esperaron las lluvias». ¿Qué dos conectores debes conservar?", "Por eso y en cambio", "Marcan consecuencia y contraste.")],
  [E("¿Qué debe conservar un resumen además de las ideas principales?", "Las relaciones entre las ideas", "Evita cambiar el sentido."),
   E("¿Se pueden omitir los detalles en un resumen?", "Sí", "Solo se mantienen las ideas importantes."),
   E("¿Se pueden agregar opiniones propias al resumen?", "No", "El resumen conserva lo que dice el texto.")],
  ("Resume en dos o tres líneas este texto de ejemplo, conservando la causa y el contraste: «Los patios con árboles son más frescos en verano porque la sombra baja la temperatura del suelo. En cambio, los patios de cemento sin sombra se calientan tanto que muchos estudiantes prefieren jugar adentro. Por eso, el colegio plantó seis árboles en el patio central.»",
   "Los patios con árboles son más frescos por la sombra, mientras los de cemento se calientan mucho y los estudiantes los evitan; por eso el colegio plantó seis árboles.",
   ["conserva la causa", "conserva el contraste", "es más breve que el original"], ["resumen de dos o tres líneas"],
   ["copiar frases completas", "perder el conector de contraste"], "Pide a alguien que lea tu resumen y diga si entiende la causa y el contraste."),
  "Resume en una línea un párrafo de un libro de tu casa.",
  "Escribe un resumen de cinco palabras y otro de veinte palabras del mismo texto; compara.")

# ================================================================== clase 3
FARO = "El faro de Punta Gaviota se construyó sobre un acantilado para guiar a los barcos de pesca. Su luz gira cada diez segundos y se ve desde veinte kilómetros de distancia. Hace unos años una tormenta dañó la lámpara y los vecinos juntaron dinero para repararla. Hoy el faro recibe visitas de cursos de varios colegios."
L(OA, 3,
  "Este cuaderno y un lápiz. El texto del faro y los demás están escritos en los ejercicios.",
  "Aprenderé a formular preguntas literales, inferenciales y críticas que me hacen avanzar en la comprensión de un texto.",
  ["Sé resumir un texto.", "Sé la diferencia entre un hecho y una opinión."],
  ["Hacerse preguntas mientras se lee es una estrategia que mantiene activa la atención. Hay tres tipos principales. Las preguntas literales se responden con lo que el texto dice abiertamente (¿cada cuántos segundos gira la luz?). Las preguntas inferenciales piden deducir algo que el texto no dice, usando pistas (¿por qué los vecinos juntaron dinero?). Las preguntas críticas piden evaluar o opinar con fundamentos (¿es justo que los vecinos paguen?).",
   "Una buena pregunta es clara, tiene una respuesta que se puede buscar en el texto o razonar, y nos hace avanzar. Una pregunta que hace avanzar nos lleva a releer, a conectar ideas o a buscar un dato nuevo. Una pregunta cuya respuesta es «sí» o «no» sin razones suele servir menos. Conviene iniciar con palabras como por qué, para qué, cómo, qué pasaría si.",
   "Puedes formular preguntas antes de leer (a partir del título), durante la lectura (cuando algo no se entiende) y después (para evaluar lo aprendido). Escríbelas en el margen y, al terminar, marca cuáles quedaron respondidas y cuáles necesitan otra fuente."],
  [("pregunta literal", "pregunta cuya respuesta está dicha en el texto"), ("pregunta inferencial", "pregunta que se responde deduciendo con pistas"), ("pregunta crítica", "pregunta que pide evaluar con argumentos"), ("inferir", "concluir algo que el texto no dice abiertamente"), ("margen", "espacio blanco al lado del texto donde se anota")],
  [("Clasificar preguntas", f"{FARO} Clasifica: (1) ¿Cada cuántos segundos gira la luz? (2) ¿Por qué los vecinos juntaron dinero para reparar la lámpara?",
    ["La 1 tiene respuesta escrita: diez segundos. Es literal.", "La 2 no está dicha: se deduce que el faro es importante para el pueblo.", "Por eso es inferencial."], "La 1 es literal; la 2 es inferencial"),
   ("Mejorar una pregunta", "Pregunta débil: «¿Es bonito el faro?» ¿Cómo la mejoras para que haga avanzar?",
    ["Es vaga y su respuesta es un simple gusto.", "Puedo pedir razones o conectar con el texto.", "Mejor: «¿Qué detalles del texto muestran que el faro es importante para el pueblo?»"], "«¿Qué detalles del texto muestran la importancia del faro para el pueblo?»")],
  [("Hacer solo preguntas literales.", "Se queda en repetir datos y no se profundiza.", "Agrega al menos una inferencial y una crítica."),
   ("Hacer preguntas que no se pueden responder con el texto ni razonando.", "Detienen la lectura sin aportar.", "Revisa que haya pistas o una fuente donde buscar.")],
  ([E(f"{FARO} ¿A qué distancia se ve la luz?", "Desde veinte kilómetros", "Lo dice el texto: pregunta literal."),
    E("¿Qué tipo de pregunta se responde con lo que el texto dice abiertamente?", "Literal", "Su respuesta está en el texto."),
    E("¿Qué tipo de pregunta pide opinar con fundamentos?", "Crítica", "Evalúa y se justifica.")],
   [E(f"{FARO} «¿Por qué los barcos de pesca necesitan una luz de noche?» ¿Qué tipo de pregunta es?", "Inferencial", "El texto no lo dice, se deduce."),
    E(f"{FARO} «¿Debe el pueblo seguir pagando la reparación del faro?» ¿Qué tipo de pregunta es?", "Crítica", "Pide una evaluación con argumentos."),
    E("¿Qué palabra inicia una buena pregunta inferencial: «por qué» o «cuándo fue»?", "Por qué", "Pide una explicación deducida.")],
   [arith(f"{FARO} Si la luz gira cada diez segundos, ¿cuántas vueltas da en un minuto?", "60//10", "Se divide 60 segundos entre 10.", " vueltas"),
    E(f"{FARO} Escribe cuál es una pregunta inferencial: (a) ¿Qué pasó con la lámpara? (b) ¿Por qué los vecinos decidieron reparar el faro? (c) ¿Cuántos kilómetros alcanza la luz?", "(b)", "Pide deducir un motivo; (a) y (c) están en el texto."),
    E(f"{FARO} Un estudiante pregunta: «¿Es bueno el faro?» ¿Qué le falta para hacer avanzar?", "Pedir razones o apoyarse en el texto", "Es vaga y de gusto.")],
   [E(f"{FARO} Una compañera pregunta: «¿Cuántas personas visitan el faro?». ¿Se responde con el texto?", "No; el texto no entrega ese dato", "Habría que buscarlo en otra fuente."),
    E("¿Por qué una pregunta de «sí o no» sin razones suele servir menos?", "Porque no obliga a explicar ni a releer", "No hace avanzar la comprensión.")],
   [E(f"{FARO} Formula la mejor pregunta crítica: (a) ¿Cuántos años tiene el faro? (b) ¿Es justo que el pueblo pague si el faro también lo visitan otros colegios? (c) ¿Dónde está el faro?", "(b)", "Pide evaluar con argumentos."),
    E("Tienes 9 preguntas anotadas: 5 literales, 3 inferenciales y el resto críticas. ¿Cuántas son críticas?", "1", "Se suman 5 y 3 y se restan de 9.")]),
  [E("Vas a leer un artículo titulado «El agua de nuestro barrio». Antes de leer, ¿cuál es una buena pregunta para hacerte? (a) ¿De dónde viene el agua que llega a las casas? (b) ¿Es importante el agua? (c) ¿Qué es el agua?", "(a)", "Orienta la lectura hacia una respuesta útil.")],
  [E("¿Qué tipo de pregunta se contesta deduciendo con pistas?", "La inferencial", "Usa lo que el texto sugiere."),
   E("¿Dónde conviene anotar tus preguntas mientras lees?", "En el margen", "Así las tienes a mano."),
   E("¿Para qué sirve una pregunta que hace avanzar?", "Para releer, conectar ideas o buscar un dato nuevo", "Impulsa la comprensión.")],
  ("Lee este texto de ejemplo: «Los murales del barrio Norte se pintaron en dos semanas con ayuda de quince vecinos. Cada mural cuenta una historia distinta del barrio. El año pasado el municipio entregó pintura para renovarlos.» Escribe una pregunta literal, una inferencial y una crítica, y responde la literal.",
   "Literal: ¿Cuántos vecinos ayudaron? (quince). Inferencial: ¿Por qué el municipio entregó pintura para renovarlos? Crítica: ¿Debe el municipio pagar siempre la pintura de los murales?",
   ["tres tipos de pregunta", "la literal está respondida con el texto", "la crítica pide argumentos"], ["tres preguntas y una respuesta"],
   ["inventar datos", "clasificar mal los tipos"], "Intercambia preguntas con alguien y comprueba si puede responderlas con el texto."),
  "Anota tres preguntas sobre un texto que leas hoy.",
  "Escribe una pregunta que se pueda responder de dos maneras razonadas y explica por qué.")

# ================================================================== clase 4
L(OA, 4,
  "Este cuaderno y un lápiz. Las imágenes y los sonidos se describen con palabras dentro de cada ejercicio.",
  "Aprenderé a analizar las relaciones que establecen las imágenes o el sonido con el texto escrito en un texto multimodal.",
  ["Sé analizar el encuadre y la escala en un gráfico.", "Sé resumir y formular preguntas."],
  ["Un texto multimodal combina varios modos: escritura, imágenes, sonido, gráficos o diseño. Un afiche suma palabras e ilustración; un video suma imagen, voz, música y subtítulos; un podcast suma voz y sonidos. Comprender estos textos exige leer cada modo y, sobre todo, descubrir qué relación hay entre ellos.",
   "Las relaciones más frecuentes son: repetición (la imagen o el sonido dicen lo mismo que el texto), complemento (agregan información nueva), ejemplificación (muestran un caso concreto), ambientación (crean un clima o una emoción) y contraste (dicen algo distinto o contrario a lo escrito). El contraste puede ser un recurso intencional, como la ironía, o una señal de que algo no coincide.",
   "Para analizar, describe primero lo que ves o escuchas, luego lee el texto escrito y, al final, pregúntate: ¿se refuerzan, se complementan o se contradicen? ¿qué sentimos por la música o el color? ¿qué información solo está en un modo? Así evitas quedarte solo con las palabras o solo con la imagen."],
  [("multimodal", "texto que combina escritura con imagen, sonido u otros modos"), ("complemento", "relación en que un modo agrega información al otro"), ("contraste", "relación en que un modo dice algo distinto o contrario al otro"), ("ambientación", "creación de un clima con color, música o diseño"), ("subtítulo", "texto escrito que acompaña a un video")],
  [("Reforzar o contradecir", "Afiche de ejemplo. Imagen: un niño sostiene un paraguas roto bajo la lluvia. Texto: «La lluvia no fue problema». ¿Qué relación hay?",
    ["La imagen muestra un paraguas roto y lluvia.", "El texto dice que la lluvia no fue problema.", "Se oponen: es un contraste, que puede ser irónico."], "Contraste (posible ironía)"),
   ("Complemento", "Video de ejemplo. Voz: «Hoy visitamos la huerta escolar». Imagen: se ven 8 camas de cultivo con lechugas y tomates. ¿Qué agrega la imagen?",
    ["La voz nombra el lugar.", "La imagen muestra cuántas camas hay y qué se cultiva.", "Agrega información nueva: es un complemento."], "Complemento: muestra 8 camas con lechugas y tomates")],
  [("Leer solo las palabras y mirar la imagen como adorno.", "Pierdes información que solo está en la imagen.", "Describe la imagen y relaciónala con el texto."),
   ("Pensar que imagen y texto siempre dicen lo mismo.", "A veces se complementan o se contradicen.", "Pregunta cuál es la relación entre ambos.")],
  ([E("Un afiche muestra el dibujo de una bicicleta y dice «Bicicleta». ¿La relación es de repetición o de contraste?", "De repetición", "La imagen y el texto dicen lo mismo."),
    E("¿Qué es un texto multimodal?", "Un texto que combina escritura con imagen, sonido u otros modos", "Usa más de un modo de comunicar."),
    E("Un video muestra a un niño sonriendo mientras la voz dice «Me encantó el paseo». ¿Se refuerzan o se contradicen?", "Se refuerzan", "La sonrisa coincide con lo dicho.")],
   [E("Un afiche dice «Cuida el agua» y su imagen muestra una llave que gotea sobre un balde. ¿Cuál es la relación: ejemplificación o contraste?", "Ejemplificación", "La imagen muestra un caso concreto relacionado."),
    E("Un podcast de ejemplo cuenta un robo de bicicletas con música suave y alegre. ¿Qué relación tiene la música con el tema: contraste o repetición?", "Contraste", "El clima alegre no coincide con un hecho negativo."),
    E("Un video sin sonido tiene subtítulos que dicen «Cae la noche» y la imagen muestra el cielo oscuro. ¿Qué relación hay?", "Repetición o refuerzo", "La imagen confirma el texto.")],
   [E("Afiche de ejemplo: texto «Vecinos unidos» sobre una foto en que 20 personas plantan árboles en la plaza. ¿Qué información agrega la imagen y no el texto?", "Que plantan árboles en la plaza y que son unas 20 personas", "Entrega la acción, el lugar y la cantidad."),
    E("Publicidad de ejemplo: la voz dice «Un producto saludable» y la imagen muestra una bolsa de dulces con grasa derretida. ¿Qué problema detectas?", "La imagen contradice la voz", "Hay contraste entre lo que se dice y lo que se ve."),
    arith("Un video tiene 3 minutos de imágenes con voz y 2 minutos solo con música. ¿Cuántos minutos dura en total?", "3+2", "Se suman los dos tramos.", " minutos")],
   [E("Un mapa de ejemplo marca 5 puntos rojos y la leyenda dice «puntos rojos: lugares con contenedores de reciclaje». El texto dice «Hay 4 contenedores». ¿Coincide?", "No; el mapa muestra 5 y el texto dice 4", "Hay una inconsistencia que conviene verificar."),
    E("Un afiche usa solo colores oscuros y tipografía fina para anunciar una fiesta alegre. ¿Qué relación hay entre diseño y mensaje?", "Contraste; el clima visual no coincide con la alegría", "Los colores crean un clima distinto al del texto.")],
   [E("Describe el efecto: la voz dice «El resultado fue muy bueno» mientras se ve una tabla con puntajes bajos. ¿Qué debe hacer el lector?", "Verificar los datos de la tabla antes de aceptar la afirmación", "La imagen contradice el texto."),
    E("Un cartel de ejemplo dice «Silencio» y muestra un dedo sobre los labios. ¿Se complementan o se repiten?", "Se repiten (refuerzo)", "Imagen y texto dicen lo mismo.")]),
  [E("En un afiche de tu colegio dice «Recreos seguros» y muestra un dibujo de niños corriendo cerca de una escalera. ¿Qué pregunta de análisis haces? (a) ¿La imagen apoya o contradice el mensaje? (b) ¿Cuántos colores hay? (c) ¿Quién dibujó?", "(a)", "Relaciona imagen y texto.")],
  [E("¿Qué relación hay cuando imagen y texto se oponen?", "Contraste", "Dicen algo distinto o contrario."),
   E("¿Qué relación hay cuando la imagen agrega un dato nuevo?", "Complemento", "Suma información nueva al texto."),
   E("¿Qué se hace primero al analizar: describir la imagen o juzgarla?", "Describirla", "Primero se observa y luego se interpreta.")],
  ("Analiza este texto multimodal de ejemplo. Afiche: título «Festival de la lectura»; imagen: un banco de plaza vacío con un libro abierto sobre él; texto pequeño: «Sábado 12, 15:00 horas. Entrada liberada». Describe la imagen, di qué relación tiene con el título y qué información está solo en el texto.",
   "La imagen muestra un banco vacío con un libro abierto. Se relaciona con el título porque sugiere lectura al aire libre (refuerzo y ambientación). Solo en el texto aparecen el día, la hora y que la entrada es liberada.",
   ["describe la imagen", "nombra una relación con el título", "indica información exclusiva del texto"], ["tres líneas"],
   ["juzgar sin describir", "ignorar el texto pequeño"], "Muestra tu análisis a otra persona y pregúntale si vio otra relación."),
  "Mira un afiche de la calle y nombra la relación entre su imagen y su texto.",
  "Diseña un afiche con una imagen que contradiga el texto a propósito y explica el efecto.")

# ================================================================== clase 5
L(OA, 5,
  "Este cuaderno y un lápiz. Los textos cortos están en los ejercicios.",
  "Aprenderé a recuperar los referentes perdidos: a qué o a quién se refieren pronombres y otras palabras que reemplazan.",
  ["Sé qué es un pronombre.", "Sé hacer preguntas durante la lectura."],
  ["Un referente es la persona, cosa o idea a la que se refiere una palabra. Los textos no repiten siempre los nombres: usan pronombres (él, ella, lo, les, este), palabras que reemplazan (el animal, esa idea) y silencios (no repiten el verbo ni el sujeto). Si perdemos el referente, no entendemos quién hizo qué.",
   "Para recuperarlo, sigue estos pasos: (1) subraya la palabra que reemplaza; (2) lee hacia atrás hasta encontrar a qué o a quién puede referirse; (3) comprueba género (masculino o femenino) y número (singular o plural); (4) reemplaza la palabra por el posible referente y relee para ver si tiene sentido. Palabras como «esto» y «aquello» suelen referirse a toda una idea anterior. Cuando se nombran dos personas, «este» señala a la más cercana (la última nombrada) y «aquel», a la más lejana.",
   "A veces el referente es ambiguo, es decir, puede ser más de uno. En «Luisa le dijo a Camila que su bicicleta estaba rota», «su» puede ser Luisa o Camila. Cuando escribas, evita esa ambigüedad repitiendo el nombre; cuando leas, avísalo y busca más pistas en el texto."],
  [("referente", "persona, cosa o idea a la que se refiere una palabra"), ("pronombre", "palabra que reemplaza a un sustantivo, como ella o lo"), ("ambiguo", "que se puede entender de más de una manera"), ("elipsis", "omisión de una palabra que se sobreentiende"), ("género y número", "masculino o femenino, singular o plural")],
  [("Recuperar un referente", "«Tomás y Pablo llegaron temprano a la biblioteca. Este último llevaba un mapa del barrio, que dejó sobre la mesa. Luego lo abrió y buscó la plaza.» ¿A quién se refiere «este último» y qué reemplaza «lo»?",
    ["«Este último» señala al segundo nombrado: Pablo.", "«Lo» es masculino y singular: puede ser el mapa.", "Reemplazo: «Luego abrió el mapa y buscó la plaza». Tiene sentido."], "«Este último» es Pablo; «lo» es el mapa"),
   ("Detectar ambigüedad", "«Luisa le dijo a Camila que su bicicleta estaba rota.» ¿De quién es la bicicleta?",
    ["«Su» puede ser de Luisa.", "«Su» puede ser de Camila.", "El texto no da más pistas: es ambiguo."], "No se sabe: el referente es ambiguo")],
  [("Elegir el sustantivo más cercano sin comprobar género y número.", "El más cercano no siempre es el referente.", "Comprueba concordancia y sentido."),
   ("Leer «esto» sin buscar qué idea reemplaza.", "Se pierde la conexión entre las ideas.", "Busca la idea completa anterior.")],
  ([E("«Camila trajo una manzana. La compartió con su amiga.» ¿Qué reemplaza «la»?", "La manzana", "Es femenino singular y se comparte."),
    E("En comprensión lectora, ¿qué es un referente?", "La persona, cosa o idea a la que se refiere una palabra", "Es lo que el pronombre reemplaza."),
    E("«Los niños juegan. Ellos ríen.» ¿A quiénes reemplaza «ellos»?", "A los niños", "Es masculino plural.")],
   [E("«Las ranas viven cerca del agua. Ellas respiran por los pulmones y también por la piel. Esto les permite vivir en dos ambientes.» ¿A qué se refiere «esto»?", "A respirar por los pulmones y por la piel", "Reemplaza una idea completa."),
    E("«Julia compró manzanas y Ana, peras.» ¿Qué verbo se omite en la segunda parte?", "Compró", "Se sobreentiende «Ana compró peras»."),
    E("«La directora saludó a los profesores. Los invitó a pasar.» ¿A quiénes reemplaza «los»?", "A los profesores", "Es masculino plural y recibe la invitación.")],
   [E("«Mariana le pasó el cuaderno a Rosa. Ella lo guardó en la mochila.» ¿Qué reemplaza «lo»?", "El cuaderno", "Es masculino singular y se guarda."),
    E("«Los vecinos plantaron árboles y regaron los nuevos. Eso alegró al barrio.» ¿Qué idea resume «eso»?", "Plantar y regar los árboles", "Es toda la acción anterior."),
    E("«Santiago y Matías estudian juntos. Este corrige los errores de aquel.» ¿Quién corrige: Matías o Santiago?", "Matías", "«Este» señala al más cercano, Matías; «aquel» a Santiago.")],
   [E("«Javier le contó a Tomás que su perro había ladrado toda la noche.» ¿Qué problema de comprensión hay?", "Ambigüedad: «su» puede ser de Javier o de Tomás", "Hay dos referentes posibles."),
    E("¿Cómo se evita la ambigüedad al escribir?", "Repitiendo el nombre o reformulando", "Se aclara quién es el referente.")],
   [E("«El profesor dejó el libro sobre la mesa y la silla. Lo había olvidado en la mañana.» ¿A qué se refiere «lo»?", "Al libro", "Es masculino singular y se puede olvidar."),
    E("«Marta y su hermana Elisa viajaron a Valdivia. Ella nació allí.» ¿Qué pista falta para saber quién nació allí?", "Falta saber a quién se refiere «ella»: Marta o Elisa", "Es un referente ambiguo.")]),
  [E("Un instructivo dice: «Agrega la harina y mézclala con el agua. Déjala reposar». ¿Qué reemplaza «la» en «Déjala reposar»?", "La mezcla de harina y agua", "Es lo que se deja reposar.")],
  [E("¿Qué se comprueba al buscar un referente?", "Género, número y sentido", "El referente debe concordar y tener sentido."),
   E("¿«Esto» suele referirse a un sustantivo o a una idea completa?", "A una idea completa", "Resume lo anterior."),
   E("¿Qué es un referente ambiguo?", "El que se puede entender de más de una manera", "Hay más de un candidato.")],
  ("En este texto de ejemplo hay tres palabras subrayadas: «Dani y su primo Ramón salieron al patio. Este llevaba una pelota nueva, que le prestó la profesora. Luego Dani lo ayudó a inflarla. Eso fue lo que más agradeció el curso.» Escribe a qué se refieren «este», «lo» (en «lo ayudó») y «eso».",
   "«Este» es Ramón. «Lo» es Ramón. «Eso» es que Dani lo ayudó a inflar la pelota.",
   ["identifica a Ramón en «este»", "identifica a Ramón en «lo»", "explica «eso» como una idea"], ["tres respuestas"],
   ["elegir siempre el más cercano", "no explicar «eso» como idea"], "Lee el texto reemplazando cada palabra por su referente y comprueba el sentido."),
  "Busca en una lectura tres pronombres y escribe a qué se refieren.",
  "Escribe un párrafo con un referente ambiguo y luego corrígelo.")

# ================================================================== clase 6
L(OA, 6,
  "Este cuaderno y un lápiz. Los textos están escritos en los ejercicios.",
  "Aprenderé a resolver vocabulario desconocido y a detectar inconsistencias entre la información del texto y lo que ya sé.",
  ["Sé encontrar referentes.", "Sé que hay palabras con prefijos y sufijos."],
  ["Cuando aparece una palabra desconocida, tengo varias estrategias. La primera es el contexto: las oraciones cercanas suelen dar pistas, como un sinónimo, un ejemplo o una explicación. La segunda es la familia de palabras: «inaudible» viene de «audible» (que se puede oír) con el prefijo in-, que niega; por eso significa «que no se puede oír». La tercera es el diccionario, que confirma el significado.",
   "Las inconsistencias son contradicciones. Pueden ser internas, cuando el texto se contradice («la laguna es tan profunda que apenas llega a los tobillos»), o externas, cuando lo que dice el texto no coincide con lo que yo sé («el hielo se hunde porque es más denso que el agua líquida»; en realidad el hielo flota). Ante una inconsistencia no la ignoro: releo, verifico en otra fuente confiable y decido qué información aceptar.",
   "Registrar la solución ayuda a recordarla: anoto la palabra, la pista que usé y el significado. Y cuando dudo de un dato, anoto dónde lo verifiqué. Resolver dificultades no es señal de ser mal lector: es lo que hacen los buenos lectores."],
  [("contexto", "palabras cercanas que dan pistas sobre el significado"), ("prefijo", "parte que se agrega al inicio de una palabra y cambia su sentido"), ("sufijo", "parte que se agrega al final de una palabra"), ("inconsistencia", "contradicción en la información"), ("verificar", "comprobar un dato en otra fuente confiable")],
  [("Deducir por contexto", "«El sendero era escarpado: en varios tramos las pendientes eran muy empinadas y había que trepar.» ¿Qué significa «escarpado»?",
    ["Busco pistas cerca: «pendientes muy empinadas» y «trepar».", "Los dos puntos anuncian una explicación.", "Escarpado significa con subidas muy empinadas."], "Con pendientes muy empinadas y difícil de subir"),
   ("Detectar una inconsistencia", "«Los murciélagos son aves que vuelan de noche.» Tu conocimiento dice que los murciélagos son mamíferos. ¿Qué haces?",
    ["Noto que el texto y mi conocimiento no coinciden.", "No lo acepto ni lo rechazo sin comprobar.", "Verifico en otra fuente confiable, como una enciclopedia."], "Verifico en otra fuente confiable antes de aceptar el dato")],
  [("Saltarse la palabra desconocida sin intentar deducirla.", "Puedes perder una idea clave.", "Prueba contexto, familia de palabras y diccionario."),
   ("Aceptar un dato dudoso solo porque está escrito.", "Un texto puede equivocarse.", "Verifica en otra fuente confiable.")],
  ([E("«La noticia fue efímera: duró solo un día y luego nadie la comentó.» ¿Qué significa «efímera»?", "De corta duración", "La explicación después de los dos puntos lo muestra."),
    E("Aparece una palabra desconocida en medio de una oración. ¿Qué conviene hacer antes de ir al diccionario?", "Leer las palabras cercanas para deducir su significado", "Las palabras cercanas dan pistas."),
    E("Una contradicción dentro del propio texto, ¿es una inconsistencia?", "Sí", "Dos ideas no pueden ser ciertas a la vez.")],
   [E("«Inaudible» viene de in- (no) y «audible». ¿Qué significa?", "Que no se puede oír", "El prefijo in- niega."),
    E("«La biblioteca abre a las 9:00, pero a las 8:00 ya había lectores dentro.» ¿Es una inconsistencia?", "Sí", "Contradice el horario de apertura."),
    E("«Frutería» viene de «fruta» con el sufijo -ería. ¿Qué es una frutería?", "Un lugar donde se venden frutas", "El sufijo -ería suele indicar lugar.")],
   [E("«El hielo se hunde porque es más denso que el agua líquida.» Sabes que el hielo flota. ¿Qué haces?", "Verificar en otra fuente confiable", "Hay una inconsistencia con lo que sabes."),
    E("«Prehistoria» viene de pre- (antes) e historia. ¿Qué significa?", "Tiempo anterior a la historia escrita", "El prefijo pre- indica antes."),
    E("«La laguna es tan profunda que apenas llega a los tobillos.» ¿Qué parte se contradice con «profunda»?", "«Apenas llega a los tobillos»", "Una laguna profunda no llegaría a los tobillos.")],
   [E("«El camino era tortuoso: giraba y se torcía a cada rato.» ¿Qué pista da el significado?", "«Giraba y se torcía a cada rato»", "Explica cómo era el camino."),
    E("Dos fuentes confiables dicen lo mismo y el texto dice otra cosa. ¿Qué dato aceptas?", "El de las dos fuentes confiables", "Hay más respaldo.")],
   [E("«Transatlántico» une trans- (a través de) y «Atlántico». ¿Qué significa?", "Que atraviesa el océano Atlántico", "El prefijo trans- indica a través."),
    E("Anotas 4 palabras desconocidas y resuelves 3. ¿Cuántas faltan por resolver?", "1", "Se resta 3 de 4.")]),
  [E("Lees en un afiche del colegio: «La feria dura tres días, hoy sábado y mañana domingo». ¿Qué inconsistencia detectas?", "Dice tres días y nombra solo dos", "El número no coincide con los días indicados.")],
  [E("¿Qué estrategias hay para una palabra desconocida? Nombra dos.", "Contexto, familia de palabras o diccionario", "Son las estrategias de la clase."),
   E("¿Qué hacemos ante una inconsistencia?", "Releer y verificar en otra fuente", "No se acepta sin comprobar."),
   E("¿Qué es un prefijo?", "Una parte que se agrega al inicio de una palabra", "Cambia su sentido.")],
  ("Resuelve estas tres dificultades de ejemplo y anota cómo lo hiciste. 1) «El orador fue lacónico: respondió solo con tres palabras.» ¿Qué significa «lacónico»? 2) «Incomprensible» ¿qué significa si «comprensible» es «que se entiende»? 3) «El tren sale a las 7:00 y a las 6:30 ya había partido.» ¿Qué inconsistencia hay?",
   "1) Lacónico: que habla con muy pocas palabras; pista: «solo con tres palabras». 2) Incomprensible: que no se puede entender; in- niega. 3) Si sale a las 7:00, no pudo haber partido a las 6:30: se contradice.",
   ["usa el contexto", "usa el prefijo", "explica la contradicción"], ["tres respuestas con su pista"],
   ["no indicar la pista usada", "no justificar la contradicción"], "Explica en voz alta qué pista usaste en cada caso."),
  "Anota tres palabras que no conozcas de un texto y su significado por contexto.",
  "Inventa tres oraciones con una pista de contexto para una palabra poco usual.")

# ================================================================== clase 7
BIT = "Bitácora de ejemplo de Fernanda. Texto: artículo sobre glaciares. Propósito: informarme. Dificultades: (1) la palabra «acumulación»; (2) no sabía a qué se refería «esto» en el párrafo 2; (3) el texto decía que el hielo se hunde en el agua. Estrategias: (1) leyó la oración completa y buscó en el diccionario; (2) resumió el párrafo 1; (3) comparó con una enciclopedia."
L(OA, 7,
  "Este cuaderno y un lápiz. La bitácora de ejemplo está escrita en los ejercicios.",
  "Aprenderé a evaluar qué estrategia funcionó para cada dificultad y a decidir qué haré en la próxima lectura.",
  ["Sé usar estrategias de resumen, preguntas, relación con imágenes, referentes y vocabulario.", "Sé llevar una bitácora."],
  ["Evaluar las estrategias es pensar sobre cómo leí. Una estrategia funcionó si resolvió la dificultad y me acercó a mi propósito. Para evaluarla, relaciono tres datos: la dificultad que tuve, la estrategia que usé y el resultado. Por ejemplo, si no entendí una palabra, usar el contexto o el diccionario es una estrategia adecuada; hacer un resumen no lo es.",
   "Cada dificultad tiene estrategias propias: para vocabulario, contexto, familia de palabras y diccionario; para referentes perdidos, leer hacia atrás y reemplazar; para ideas largas, resumir; para dudas, formular preguntas; para imágenes y sonido, comparar las relaciones; para inconsistencias, verificar en otra fuente. Si una estrategia no resolvió la dificultad, cambio de estrategia, no de propósito.",
   "Al cerrar la bitácora respondo: ¿logré mi propósito?, ¿qué estrategia ayudó más?, ¿cuál no sirvió y por qué?, ¿qué haré distinto la próxima vez? Escribir esa decisión convierte una experiencia de lectura en un aprendizaje que puedo reutilizar."],
  [("evaluar", "juzgar con criterios si algo funcionó"), ("resultado", "lo que ocurrió después de usar una estrategia"), ("criterio", "regla para decidir si algo funcionó"), ("metacognición", "pensar sobre cómo pienso y cómo aprendo"), ("decisión", "acción que elijo para la próxima vez")],
  [("Emparejar dificultad y estrategia", f"{BIT} Evalúa si cada estrategia correspondía a su dificultad.",
    ["(1) Vocabulario: leer la oración y usar diccionario es adecuado.", "(2) Referente perdido: resumir el párrafo 1 no sirve; debió leer hacia atrás para ver a qué idea se refería «esto».", "(3) Inconsistencia: comparar con una enciclopedia es adecuado."], "Las estrategias 1 y 3 correspondían; la 2 no"),
   ("Decidir para la próxima", f"{BIT} La estrategia 2 no resolvió la dificultad. ¿Qué decisión escribirías?",
    ["Reconozco la dificultad: referente perdido.", "Elijo una estrategia adecuada: leer hacia atrás.", "Escribo: «La próxima vez reemplazaré «esto» por la idea anterior y comprobaré el sentido»."], "Usar lectura hacia atrás y reemplazo para recuperar el referente")],
  [("Cambiar de propósito en vez de cambiar de estrategia.", "El propósito sigue siendo el mismo.", "Si algo no funciona, prueba otra estrategia."),
   ("Evaluar solo si el texto fue fácil.", "No dice cuál estrategia ayudó.", "Relaciona dificultad, estrategia y resultado.")],
  ([E(f"{BIT} ¿Cuál fue el propósito de lectura de Fernanda?", "Informarse", "Lo dice la bitácora."),
    E(f"{BIT} ¿Cuántas dificultades anotó?", "3", "Son las numeradas (1), (2) y (3)."),
    E("¿Qué es evaluar una estrategia?", "Juzgar con criterios si resolvió la dificultad", "Se compara la dificultad con el resultado.")],
   [E(f"{BIT} ¿Qué estrategia usó para la palabra «acumulación»?", "Leyó la oración completa y buscó en el diccionario", "Está en la bitácora."),
    E(f"{BIT} ¿La estrategia 2 resolvió la dificultad 2?", "No; resumir el párrafo 1 no recupera el referente de «esto»", "No corresponde a la dificultad."),
    E("Para una dificultad de vocabulario, ¿qué estrategia sirve: el contexto o formular una pregunta crítica?", "El contexto", "Ayuda a deducir el significado.")],
   [arith(f"{BIT} Fernanda tuvo 3 dificultades y resolvió bien 2. ¿Cuántas quedaron sin resolver?", "3-2", "Se resta lo resuelto del total.", " dificultad"),
    E("Texto con un pronombre «ellos» que no entiendes. ¿Qué estrategia eliges: leer hacia atrás o hacer un resumen?", "Leer hacia atrás", "Busca el referente anterior."),
    E("Un gráfico y un texto dicen cosas distintas. ¿Qué estrategia corresponde: comparar la relación entre imagen y texto o buscar prefijos?", "Comparar la relación entre imagen y texto", "Es una dificultad multimodal.")],
   [E("Un lector dice: «Como el texto era difícil, cambié mi propósito y ya no necesité resolver nada». ¿Qué error comete?", "Cambió el propósito en vez de cambiar la estrategia", "Debió buscar otra manera de resolver."),
    E("Una estrategia ayudó mucho una vez. ¿Sirve para todas las dificultades?", "No; cada dificultad pide estrategias propias", "Se debe elegir según el problema.")],
   [E(f"{BIT} Escribe la decisión mejor justificada: (a) «La próxima vez leeré hacia atrás para recuperar el referente de «esto»». (b) «No leeré más artículos». (c) «Leeré más rápido».", "(a)", "Se relaciona con la dificultad no resuelta."),
    arith("En una semana usaste 5 estrategias distintas y 4 funcionaron. ¿Cuántas no funcionaron?", "5-4", "Se resta lo que funcionó del total.", " estrategia")]),
  [E("Terminas un texto sobre el reciclaje. Tu propósito era informarte y logras explicarlo con tus palabras. ¿Lograste tu propósito?", "Sí", "Puedes explicar lo que aprendiste.")],
  [E("¿Qué tres datos se relacionan para evaluar una estrategia?", "La dificultad, la estrategia y el resultado", "Así se juzga si funcionó."),
   E("¿Qué se hace si una estrategia no resolvió la dificultad?", "Se prueba otra estrategia", "El propósito no cambia."),
   E("¿Para qué sirve escribir qué haré distinto la próxima vez?", "Para convertir la lectura en un aprendizaje que puedo reutilizar", "Deja una decisión concreta para la siguiente lectura.")],
  ("Completa una bitácora de cierre para este caso de ejemplo. Lees un reportaje con un mapa y la frase «Esto los preocupó». No entiendes «esto», encuentras la palabra «litoral» y el mapa muestra 3 puertos pero el texto dice 4. Escribe las tres dificultades, una estrategia para cada una, si funcionó (imagina el resultado) y qué harás la próxima vez.",
   "Dificultades: 1) referente de «esto» → leí hacia atrás y lo reemplacé, funcionó; 2) «litoral» → usé el contexto y el diccionario (costa), funcionó; 3) mapa 3 vs texto 4 → verifiqué con otra fuente, funcionó parcialmente. Próxima vez: anotaré cada dificultad con su estrategia desde el inicio.",
   ["tres dificultades distintas", "estrategia adecuada para cada una", "decisión para la próxima vez"], ["bitácora de cierre"],
   ["usar estrategias que no corresponden", "no escribir una decisión"], "Revisa con otra persona si cada estrategia corresponde a su dificultad."),
  "Escribe qué estrategia usas más cuando una palabra no se entiende.",
  "Arma una tabla de tres columnas: dificultad, estrategia y resultado, con tres lecturas distintas.")

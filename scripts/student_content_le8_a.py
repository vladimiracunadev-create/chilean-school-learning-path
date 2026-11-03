"""Cuaderno del estudiante, 8.º básico Lengua y Literatura, OA 01 (trayectoria lectora autónoma).

Los títulos y textos son originales e inventados para este cuaderno; cada ejercicio trae los datos que necesita.
Aquí se definen los ayudantes `L`, `E`, `task`, `arith` que reutilizan los otros módulos le8_*.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "LE08 OA 01"
E = ex


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


def add_text(oa, numbers, label, text):
    """Agrega al final de la explicación el texto de trabajo con sus rótulos, para que cada pregunta pueda resolverse con lo escrito en la clase."""
    from student_lessons import REGISTRY
    for n in numbers:
        REGISTRY[(oa, n)]["explain"][-1] += f" {label} {text}"


MAT = "Este cuaderno, lápiz y los textos escritos en cada ejercicio. No necesitas libros especiales ni internet."

# Catálogo inventado de seis textos que se usa en las clases de OA 01
CAT = ("«Ceniza y brújula» (novela de aventuras, 220 páginas, una expedición polar), "
       "«Cómo se mide un terremoto» (artículo de divulgación, 4 páginas, sismología), "
       "«Cuaderno de la marea» (poemario, 24 páginas, el mar), "
       "«La regla del juego» (comedia teatral, 35 páginas, un club de ajedrez), "
       "«Diario de una bicicleta» (crónica, 18 páginas, la ciudad sobre ruedas) y "
       "«Ruido blanco» (cuento de ciencia ficción, 15 páginas, un pueblo sin sonido)")

# ------------------------------------------------------------------ OA 01 · clase 1
L(OA1, 1,
  MAT,
  "Aprenderé a definir para qué leo (propósito), a reconocer qué hace difícil un texto (desafío) y a elegir una estrategia cuando la comprensión se interrumpe.",
  ["Distingo cuentos, poemas, artículos y obras de teatro.", "Sé que leer sirve para aprender y también para disfrutar."],
  ["Un lector autónomo no lee al azar: decide para qué lee. Ese para qué es el propósito. Puede ser aprender o informarse (por ejemplo, entender cómo se mide un sismo), hacer algo siguiendo pasos (armar un mueble) o recrearse (disfrutar una aventura). El propósito cambia de un día a otro, y un mismo texto puede servir a propósitos distintos.",
   "Todo texto tiene un desafío: algo que lo vuelve exigente para quien lo lee. Puede ser su extensión (220 páginas), el vocabulario técnico (palabras como «sismógrafo»), una estructura con saltos en el tiempo o un mundo imaginado con reglas propias. Reconocer el desafío antes de empezar permite prepararse, y no es un defecto del lector: es información para planificar.",
   "Cuando la comprensión se interrumpe hay estrategias concretas: releer despacio, leer en voz alta, buscar en el propio texto una definición cercana, anotar en una línea lo que pasó en cada párrafo o dejar una pregunta escrita para conversarla después. Autonomía no significa leer sin metas ni sin hablar con nadie: significa decidir con criterio, registrar lo leído y conversar sobre ello."],
  [("propósito", "para qué voy a leer un texto"), ("desafío", "lo que hace exigente a un texto: extensión, vocabulario, estructura o tema"), ("estrategia", "acción concreta para seguir comprendiendo cuando algo se complica"), ("bitácora", "cuaderno donde se anotan las lecturas, las decisiones y las dificultades")],
  [("Propósito y desafío en una anotación", "Anotación de Camila: «Voy a leer “Cómo se mide un terremoto” para una exposición, pero me frena la palabra “epicentro”». ¿Cuál es el propósito y cuál el desafío?",
    ["El propósito responde a para qué lee: para preparar una exposición.", "El desafío es lo que le cuesta: una palabra técnica.", "Escribo ambos por separado."],
    "Propósito: preparar una exposición; desafío: vocabulario técnico («epicentro»)"),
   ("Elegir una estrategia según la dificultad", "Tomás lee «Ruido blanco» y se pierde porque el cuento cuenta primero el final del martes y luego vuelve al lunes. ¿Qué estrategia le sirve más?",
    ["El problema es el orden de los hechos, no una palabra.", "Una estrategia que ordena es anotar en una línea qué ocurre en cada día.", "Así reconstruye la secuencia sin abandonar el cuento."],
    "Anotar en una línea lo que ocurre en cada día para ordenar los hechos")],
  [("Elegir un texto solo porque es el más largo, para parecer buen lector.", "Se confunde cantidad con propósito.", "Primero define para qué lees y después compara los textos con ese propósito."),
   ("Creer que ser autónomo es leer sin metas ni conversar con nadie.", "Se confunde libertad con ausencia de criterio.", "Fija una meta, registra lo que lees y comenta una duda con otra persona.")],
  ([E("Lees las instrucciones para armar una repisa. ¿Tu propósito es hacer algo siguiendo pasos o recrearte con una historia?", "Hacer algo siguiendo pasos", "Un instructivo sirve para ejecutar un procedimiento, no para entretener con una trama."),
    E("En «Cómo se mide un terremoto» aparecen «magnitud», «sismógrafo» y «epicentro». ¿Qué desafío lector presentan esas palabras?", "Vocabulario técnico", "Son términos especializados que quizá el lector no conoce."),
    E("Si no entiendes un párrafo, ¿qué estrategia de esta clase conviene probar primero: releerlo despacio o saltarlo?", "Releerlo despacio", "Releer permite fijarse en lo que se pasó por alto; saltarlo deja el vacío de comprensión.")],
   [E("Clasifica con I (informarse) o R (recrearse): 1) leer un artículo para una prueba de ciencias, 2) leer un poemario solo por el sonido de las palabras, 3) leer una aventura un sábado por la tarde. Escribe las tres letras en orden.", "I, R, R", "El artículo sirve para informarse; el poemario y la aventura se leen por disfrute."),
    E("Una bitácora dice: «Quiero entender cómo se mide un sismo» y «Me cuestan las palabras técnicas». ¿Cuál de las dos frases es el desafío?", "Me cuestan las palabras técnicas", "Describe lo que dificulta la lectura; la otra frase dice para qué se lee."),
    E("Una lectora comenta: «El cuento “Ruido blanco” está en un pueblo imaginario donde nadie oye su voz, y no entiendo las reglas de ese mundo». ¿Qué tipo de desafío describe? A) vocabulario técnico B) comprender un mundo imaginado con reglas propias C) un tema científico demasiado complejo", "B) comprender un mundo imaginado con reglas propias", "El cuento es de ciencia ficción y plantea un mundo inventado; no usa términos técnicos ni explica un tema de ciencia.")],
   [E("«Ceniza y brújula» tiene 220 páginas y tienes 11 días para leerla. Si lees lo mismo cada día, ¿cuántas páginas leerás por día?", "20", "220 dividido en 11 días da 20 páginas diarias.", "220 // 11"),
    E("Tu propósito es informarte para una exposición sobre sismos y solo tienes una tarde. Opciones: «Cómo se mide un terremoto» (4 páginas), «Ceniza y brújula» (220 páginas) o «Cuaderno de la marea» (24 páginas, poemario). ¿Cuál se ajusta mejor?", "«Cómo se mide un terremoto»", "Es un artículo de divulgación sobre el tema y cabe en una tarde."),
    E("Al leer «epicentro» en un artículo, encuentras: «El epicentro es el punto de la superficie justo sobre el lugar donde se origina el sismo». ¿Qué estrategia usaste para entender la palabra: buscar la definición dentro del propio texto o abandonar el artículo?", "Buscar la definición dentro del propio texto", "La frase explica la palabra con sus propios términos.")],
   [E("Rodrigo elige «Ceniza y brújula» «porque quiero vivir una aventura y tengo tres semanas». Sofía lo elige «porque es el más largo». ¿Quién relaciona su elección con un propósito?", "Rodrigo", "Nombra qué busca (aventura) y qué tiempo tiene; la razón de Sofía es solo la extensión."),
    E("Lucía dice: «Soy autónoma: leo lo que quiero sin anotar ni comentar nada». ¿Qué le falta, según la clase, para una lectura autónoma? A) leer más páginas por día B) tener metas, registrar y conversar sobre lo leído C) elegir siempre textos cortos", "B) tener metas, registrar y conversar sobre lo leído", "La autonomía lectora implica decidir con criterio, llevar un registro y compartir lo leído; la cantidad de páginas o la extensión no la definen.")],
   [E("Tienes tres días y 25 minutos diarios para leer «Cómo se mide un terremoto» (4 páginas). Lees 2 páginas cada 5 minutos. ¿Cuántas páginas podrías leer en una sesión de 25 minutos? (Compara con las 4 del artículo.)", "10 páginas; alcanzas a terminarlo en una sola sesión", "En 25 minutos hay 5 bloques de 5 minutos, y cada bloque da 2 páginas; 10 es más que 4.", "25 // 5 * 2"),
    E("«Ruido blanco» tiene 15 páginas. Después de 5 páginas Ana anota: «Los hechos saltan de un día a otro y me pierdo». ¿Qué debería escribir ella en su bitácora como estrategia: hacer una línea de tiempo corta con lo que ocurre cada día o esperar a que el cuento se explique solo?", "Hacer una línea de tiempo corta con lo que ocurre cada día", "Ordenar los hechos ataca el desafío concreto (saltos en el tiempo); esperar no resuelve la confusión.")]),
  [E("Para el trayecto de 40 minutos en bus a casa de tu abuela quieres un texto narrativo que alcances a terminar. Lees 1 página cada 2 minutos. Opciones: «Ruido blanco» (cuento, 15 páginas), «La regla del juego» (comedia, 35 páginas) y «Cuaderno de la marea» (poemario, 24 páginas). ¿Cuál eliges?", "«Ruido blanco»", "15 páginas son 30 minutos y es un cuento; las otras opciones necesitan 70 y 48 minutos, más que el trayecto, y el poemario no es narrativo.")],
  [E("¿Qué palabra nombra «para qué leo»: propósito o desafío?", "Propósito", "El desafío es lo que dificulta el texto."),
   E("¿Cuál es una estrategia de esta clase para cuando la comprensión se interrumpe? A) anotar en una línea lo que pasa en cada párrafo B) leer solo el final C) cambiar de texto sin ninguna razón", "A) anotar en una línea lo que pasa en cada párrafo", "Resumir por párrafo es una estrategia concreta; leer solo el final o abandonar sin razón no ayuda a comprender."),
   E("Una persona lee 20 páginas por día durante 6 días. ¿Cuántas páginas lee en total?", "120", "20 por 6 da 120 páginas.", "20 * 6")],
  ("Tienes estas dos opciones de la lista: «Ruido blanco» (cuento de ciencia ficción, 15 páginas) y «Diario de una bicicleta» (crónica de 18 páginas). Escribe en tu bitácora: 1) tu propósito para esta semana, 2) cuál eliges y qué desafío prevés (vocabulario, estructura, extensión), 3) qué estrategia usarás si te pierdes.",
   "Propósito: recrearme en el fin de semana. Elijo «Ruido blanco» porque es un cuento breve de ciencia ficción. Prevé el desafío de entender las reglas del mundo inventado. Si me pierdo, anotaré en una línea qué ocurre en cada día y conversaré mi duda con alguien de mi casa.",
   ["formula un propósito claro", "nombra un desafío concreto del texto", "propone una estrategia ligada a ese desafío"], ["entrada de bitácora de tres partes"], ["elegir solo por la extensión", "estrategia genérica sin relación con el desafío"], "Subraya tu propósito, tu desafío y tu estrategia; comprueba que la estrategia responda al desafío que anotaste."),
  "Anota en tu cuaderno qué leíste hoy (cualquier cosa) y cuál fue tu propósito.",
  "Escribe tres propósitos distintos que podrías tener esta semana y un desafío que prevés para cada uno.")

# ------------------------------------------------------------------ OA 01 · clase 2
L(OA1, 2,
  MAT,
  "Aprenderé a explorar y comparar opciones de lectura con criterios observables: género, extensión, tema, dificultad y una muestra de las primeras líneas.",
  ["Defino un propósito y reconozco desafíos lectores.", "Sé que portada, índice y primera página dan pistas."],
  ["Explorar es mirar rasgos de un texto sin leerlo entero. Los rasgos observables son el género (cuento, poema, comedia teatral), la extensión (número de páginas), el tema y una muestra: las primeras líneas, que dejan ver el estilo y la dificultad. Un catálogo es una lista de textos entre los cuales elegir, y una buena exploración compara al menos tres opciones.",
   "Comparar significa poner las opciones frente a un mismo criterio. Si el criterio es el tiempo, se divide el número de páginas por las páginas que puedo leer por día. Si es la dificultad, se lee la muestra y se observa si hay vocabulario desconocido o frases muy largas. Si es el tema, se revisa si responde a mi propósito. Un criterio sin evidencia, como «parece bueno», no sirve para comparar.",
   "Una muestra orienta, pero no reemplaza la lectura: un inicio lento puede mejorar, y un inicio atractivo puede decepcionar. Por eso la decisión final combina varios criterios y admite ser revisada. Si una opción no pasa el filtro más importante (por ejemplo, no cabe en el plazo), se descarta con una razón y se mira la siguiente."],
  [("catálogo", "lista de textos entre los que se puede elegir"), ("muestra", "fragmento corto, como las primeras líneas, que permite hacerse una idea del texto"), ("criterio", "rasgo o regla que se usa para comparar opciones"), ("filtro", "condición que una opción debe cumplir para seguir en la lista")],
  [("Comparar con un criterio de tiempo", "Tienes 5 días y puedes leer 12 páginas por día. ¿Cuáles de estas opciones caben: «Diario de una bicicleta» (18 páginas), «La regla del juego» (35 páginas), «Ceniza y brújula» (220 páginas)?",
    ["Calculo las páginas disponibles: 12 por 5 da 60.", "18 es menor que 60 y 35 es menor que 60; 220 no cabe.", "Quedan dos opciones."],
    "Caben «Diario de una bicicleta» y «La regla del juego»"),
   ("Leer una muestra", "Muestra: «La ley de los cuerpos celestes, en su formulación inicial, establece una proporción entre masa y atracción». Un lector con poca experiencia en física, ¿qué dificultad prevé?",
    ["Busco palabras técnicas: «formulación», «proporción», «masa», «atracción».", "La frase es larga y abstracta.", "Prevé dificultad de vocabulario y de frases largas."],
    "Vocabulario técnico y frases largas")],
  [("Decidir solo por el título o la portada.", "Se toma una pista superficial como si fuera evidencia suficiente.", "Compara al menos dos criterios con datos: páginas, género, tema y una muestra."),
   ("Descartar un texto por una sola línea difícil.", "Se toma la muestra como prueba definitiva del texto.", "Usa la muestra como orientación y revisa la decisión con otro criterio.")],
  ([E("Tienes 4 días y lees 10 páginas por día. ¿Cuántas páginas puedes leer en total?", "40", "10 por 4 da 40 páginas.", "10 * 4"),
    E("¿Qué es una muestra de un texto: sus primeras líneas o su precio?", "Sus primeras líneas", "La muestra es un fragmento que permite hacerse una idea del estilo."),
    E("«Cuaderno de la marea» tiene 24 páginas y «Ceniza y brújula» tiene 220. Con un criterio de extensión, ¿cuál es más corto?", "«Cuaderno de la marea»", "24 es menor que 220.")],
   [E("Lees dos muestras. Muestra 1: «El hielo crujió bajo la tienda antes del amanecer». Muestra 2: «Sea F la función de transferencia del sistema lineal invariante». ¿Cuál muestra anuncia una narración?", "La muestra 1", "Tiene un hecho y un escenario; la otra es lenguaje matemático."),
    E("Un compañero afirma: «Elegí “La regla del juego” porque parece buena». ¿Qué le falta a su criterio: evidencia observable o más páginas?", "Evidencia observable", "«Parece buena» no indica género, tema ni extensión."),
    E("«Ruido blanco» tiene 15 páginas y «Diario de una bicicleta» 18. Lees 6 páginas por día. ¿Cuántos días necesitas para terminar «Diario de una bicicleta»? (Si sobran páginas, cuenta un día más.)", "3", "18 dividido en 6 por día da exactamente 3 días.", "18 // 6")],
   [E("Tienes 6 días y lees 25 páginas por día. ¿Cuántas de estas opciones caben en el plazo: «Ceniza y brújula» (220), «La regla del juego» (35), «Diario de una bicicleta» (18), «Ruido blanco» (15)? Escribe el número.", "3", "En 6 días lees 150 páginas; cabe todo menos la novela de 220."),
    E("Filtro: cuento breve de menos de 20 páginas. De la lista de la clase, ¿cuáles lo cumplen: «Ruido blanco» (cuento, 15), «Diario de una bicicleta» (crónica, 18), «Cuaderno de la marea» (poemario, 24)?", "Solo «Ruido blanco»", "La crónica no es cuento y el poemario tiene más de 20 páginas."),
    E("Muestra: «Los acuíferos, cuerpos de roca saturada, se recargan por infiltración». ¿Qué desafío prevé un lector que no conoce esos términos? A) estructura con saltos en el tiempo B) vocabulario técnico C) un mundo imaginado", "B) vocabulario técnico", "Aparecen términos como «acuíferos» e «infiltración», propios de un texto científico.")],
   [E("Dos lectores comparan los mismos textos. Ana usa tres criterios con datos (género, páginas, muestra). Bruno usa «el que tiene mejor portada». ¿Cuál comparación es más sólida?", "La de Ana", "Usa varios criterios observables; la portada es solo una pista superficial."),
    E("«Ceniza y brújula» empieza con una muestra lenta y descriptiva, pero se trata de una aventura que le interesa mucho a Camilo. ¿Debe descartarla solo por esa muestra?", "No", "Una muestra orienta pero no decide; debe revisar con otros criterios, como el tema y el plazo.")],
   [E("Tienes 8 días y lees 15 páginas diarias, pero reservas 2 días sin leer. ¿Cuántas páginas puedes leer en total?", "90", "Quedan 6 días de lectura y 15 por 6 da 90 páginas.", "(8 - 2) * 15"),
    E("Con un total de 90 páginas posibles, ¿cuál de estas opciones elegirías para recrearte con una narración: «Ceniza y brújula» (220), «Ruido blanco» (15) o «La regla del juego» (35, teatro)?", "«Ruido blanco»", "Es narración y cabe; la novela no cabe y la comedia es texto teatral, no narración.")]),
  [E("Debes elegir una lectura para un viaje de 3 días. Lees 20 páginas por día y buscas aprender algo de ciencias. Opciones: «Cómo se mide un terremoto» (artículo, 4 páginas), «Ceniza y brújula» (novela, 220 páginas) y «Ruido blanco» (cuento, 15 páginas). ¿Cuál eliges?", "«Cómo se mide un terremoto»", "Es el único texto informativo de ciencias y cabe holgadamente en 60 páginas.")],
  [E("¿Qué criterio permite comparar si un texto cabe en tu plazo?", "La extensión (número de páginas)", "Dividiendo las páginas por las que lees por día se obtiene el tiempo."),
   E("¿Una muestra reemplaza la lectura completa: sí o no?", "No", "Solo orienta la decisión."),
   E("Si un texto no cumple tu filtro principal, ¿lo descartas con una razón o lo lees igual?", "Lo descartas con una razón", "El filtro existe para ahorrar tiempo y ajustar la elección al propósito.")],
  ("Compara estas tres opciones con tu propósito de leer una narración corta este fin de semana: «Ruido blanco» (cuento de ciencia ficción, 15 páginas; muestra: «Desde el martes, nadie en Villa Alta oía su propia voz»), «Diario de una bicicleta» (crónica, 18 páginas; muestra: «El semáforo se puso en verde y mi rueda trasera chilló») y «La regla del juego» (comedia teatral, 35 páginas; muestra: «ALBERTO. —Las blancas siempre mueven primero, ¿o no?»). Haz una tabla con tres criterios y elige una opción.",
   "Tabla: «Ruido blanco» — cuento, 15 págs., muestra de misterio. «Diario…» — crónica, 18 págs., muestra de acción cotidiana. «La regla…» — teatro, 35 págs., diálogo ágil. Elijo «Ruido blanco» porque es narración, es la más corta y su muestra despierta preguntas.",
   ["compara con al menos tres criterios", "usa la muestra como evidencia", "elige y justifica con datos"], ["tabla comparativa", "frase de decisión"], ["decidir por la portada", "comparar sin dato"], "Revisa que cada celda de tu tabla tenga un dato y que tu elección use al menos dos de ellos."),
  "Mira tres libros o textos que haya en tu casa y compara su primera página.",
  "Escribe una muestra de tres líneas de un texto inventado por ti y pídele a alguien que adivine su género.")

# ------------------------------------------------------------------ OA 01 · clase 3
L(OA1, 3,
  MAT,
  "Aprenderé a justificar una selección de lectura con propósito, dos criterios con evidencia y una estrategia de respaldo, y a distinguir una buena justificación de una débil.",
  ["Comparo textos con criterios observables.", "Conozco estrategias para cuando la comprensión se interrumpe."],
  ["Justificar es explicar con razones y datos por qué se tomó una decisión. Una justificación sólida de lectura tiene cuatro partes: el propósito (para qué leeré), al menos dos criterios (por ejemplo, género y extensión), la evidencia que respalda cada criterio (un dato del texto) y una estrategia por si la comprensión se interrumpe. Decir «porque me gusta» sin datos no permite que otra persona entienda la decisión.",
   "Una forma útil de escribirla es: «Mi propósito es…; elijo… porque (criterio 1) y porque (criterio 2); si me pierdo, voy a…». Cada «porque» debe apoyarse en un dato verificable: «tiene 18 páginas», «es una crónica», «su muestra describe una situación cotidiana». Una opinión sin dato, como «es entretenido», puede acompañar la justificación, pero no la sostiene sola.",
   "Una justificación también puede cambiar. Si tras leer unas páginas descubro que el texto no cumple mi propósito, puedo dejarlo, pero con una razón y no por impulso. Revisar una decisión con evidencia es parte de la autonomía lectora. Un compañero puede discrepar de mi elección: vale conversar, siempre que ambos mostremos datos y no solo preferencias."],
  [("justificar", "explicar con razones y datos por qué se tomó una decisión"), ("evidencia", "dato observable que respalda una afirmación"), ("criterio", "rasgo que se usa para decidir"), ("estrategia de respaldo", "plan alternativo si la lectura se vuelve difícil")],
  [("Distinguir criterio y evidencia", "Justificación: «Elijo “Diario de una bicicleta” porque es una crónica y porque tiene 18 páginas, y mi plazo es de tres días». ¿Cuáles son los dos criterios y cuál es la evidencia del plazo?",
    ["Los criterios están tras «porque»: género y extensión.", "La evidencia del plazo es el dato numérico: 18 páginas en tres días.", "Separo criterio de dato."],
    "Criterios: género (crónica) y extensión; evidencia del plazo: 18 páginas en tres días"),
   ("Mejorar una justificación débil", "Justificación débil: «Elegí “Ruido blanco” porque sí». Reescríbela con propósito y un criterio con dato (cuento de 15 páginas, ciencia ficción).",
    ["Agrego el propósito: recrearme en el fin de semana.", "Agrego un criterio con dato: es un cuento de 15 páginas.", "Uno ambas partes."],
    "«Mi propósito es recrearme el fin de semana; elijo “Ruido blanco” porque es un cuento de ciencia ficción de solo 15 páginas»")],
  [("Dar una justificación con un solo «porque me gusta».", "No se ofrece ningún dato que otra persona pueda comprobar.", "Agrega al menos dos criterios con un dato cada uno."),
   ("Abandonar el texto sin explicar el motivo.", "Se toma una decisión de impulso, sin revisar la justificación inicial.", "Escribe qué parte del propósito no se cumple y qué cambiarás.")],
  ([E("«Elegí el cuento porque sí.» ¿Esta justificación entrega evidencia comprobable: sí o no?", "No", "No cita ningún dato del texto."),
    E("Justificación: «Mi propósito es aprender; elijo el artículo porque trata sismos y tiene 4 páginas». ¿Qué parte de las cuatro enseñadas no aparece?", "La estrategia de respaldo", "Tiene propósito, criterios y evidencia, pero no un plan por si la comprensión se interrumpe."),
    E("«Tiene 18 páginas» es un dato verificable. «Es entretenido» ¿es un dato verificable o una opinión?", "Una opinión", "No se puede comprobar con una cifra o un rasgo visible del texto.")],
   [E("Justificación: «Mi propósito es aprender sobre sismología; elijo el artículo de 4 páginas porque trata el tema y cabe en mi tarde». ¿Cuál es el propósito?", "Aprender sobre sismología", "Lo dice la primera parte de la frase."),
    E("Justificación: «Mi propósito es aprender sobre sismología; elijo el artículo de 4 páginas porque trata el tema y cabe en mi tarde». ¿Qué dato funciona como evidencia de extensión: «trata el tema» o «4 páginas»?", "«4 páginas»", "Es una cifra verificable; el otro dato corresponde al criterio de tema."),
    E("Un compañero dice: «Mi estrategia de respaldo es releer el párrafo y anotar una línea de resumen». ¿Qué parte de la justificación es esa?", "La estrategia de respaldo", "Es el plan para cuando la comprensión se interrumpe.")],
   [E("Lees 7 páginas por día durante 5 días. ¿Cabe «La regla del juego» (35 páginas) en ese plazo?", "Sí, justo: 7 por 5 es 35", "En 5 días lees exactamente 35 páginas, las que tiene el texto.", "7 * 5"),
    E("Dos justificaciones del mismo cuento. Ema: «Es de ciencia ficción, tiene 15 páginas y mi plazo es de tres días». Iván: «Me dijeron que es bueno». ¿Cuál tiene evidencia comprobable?", "La de Ema", "Cita género, extensión y plazo; la de Iván solo transmite una opinión ajena."),
    E("Elena escribe: «Elijo “Ruido blanco” porque es un cuento y tiene 15 páginas; si me pierdo, anotaré una línea por día». ¿Qué parte de las cuatro falta?", "El propósito", "No dice para qué leerá; tiene criterios, evidencia y estrategia.")],
   [E("Gabriel elige la novela «Ceniza y brújula» (220 páginas) para terminarla en 5 días. ¿Su plazo es coherente con la extensión si puede leer 30 páginas por día?", "No: en 5 días lee 150 páginas, menos que las 220 de la novela", "30 por 5 da 150, que no alcanza para 220 páginas.", "5 * 30"),
    E("Juana elige «Cómo se mide un terremoto» para recrearse con una aventura. ¿Su justificación es coherente con su propósito?", "No", "Un artículo de divulgación informa sobre un tema y no ofrece una aventura.")],
   [E("Una justificación dice: «Elijo la crónica de 18 páginas». Otra lectora la completa: «porque lo leo en 3 días a 6 páginas diarias». ¿Se cumple el cálculo? (Compara 3 por 6 con 18.)", "Sí: 3 por 6 es 18", "El producto coincide con las 18 páginas del texto.", "3 * 6"),
    E("Elena abandona «Ruido blanco» tras 4 páginas escribiendo: «Dejo este cuento porque no tiene diálogos y mi propósito era leer un texto con mucha conversación». ¿Su abandono tiene una razón ligada al propósito?", "Sí", "Explica qué parte del propósito no se cumple.")]),
  [E("Debes justificar para el curso tu lectura de «Diario de una bicicleta» (crónica, 18 páginas). Tu propósito es conocer cómo se ve la ciudad desde una bicicleta. Escribe cuántas páginas leerías por día si lo terminas en 3 días.", "6", "18 páginas repartidas en 3 días dan 6 por día.", "18 // 3")],
  [E("¿Qué debe acompañar a un criterio en una justificación: un dato verificable o solo una opinión?", "Un dato verificable", "La evidencia respalda el criterio."),
   E("¿Se puede cambiar la decisión de lectura si el texto no cumple el propósito?", "Sí, con una razón", "Revisar una decisión con evidencia es parte de la autonomía."),
   E("¿Qué frase inicia una justificación según la forma de la clase: «Mi propósito es…» o «Me dijeron que…»?", "«Mi propósito es…»", "Se parte por lo que busco.")],
  ("Elige uno de estos textos y escribe tu justificación completa: «Cuaderno de la marea» (poemario, 24 páginas; muestra: «La espuma dibuja su letra en la arena»), «Ruido blanco» (cuento, 15 páginas) o «Cómo se mide un terremoto» (artículo, 4 páginas). Debe tener propósito, dos criterios con dato, y una estrategia de respaldo.",
   "Mi propósito es disfrutar el sonido de las palabras. Elijo «Cuaderno de la marea» porque es un poemario (género) y porque tiene 24 páginas que puedo leer en 4 días a 6 por día (extensión). Si me pierdo en una imagen, leeré el poema en voz alta y anotaré qué siento.",
   ["incluye propósito", "nombra dos criterios con datos", "incluye estrategia de respaldo"], ["párrafo de justificación"], ["opinión sin dato", "olvidar la estrategia"], "Marca con colores el propósito, cada criterio y la estrategia; si un color falta, agrégalo."),
  "Explícale a alguien de tu casa por qué elegirías un libro en lugar de otro, con dos razones y un dato.",
  "Escribe dos justificaciones distintas para el mismo texto, con dos propósitos diferentes.")

# ------------------------------------------------------------------ OA 01 · clase 4
L(OA1, 4,
  MAT,
  "Aprenderé a planificar una lectura sostenible: calcular ritmo y plazo, reservar tiempo realista y prever cómo seguir si un día falla.",
  ["Justifico mi elección con propósito y criterios.", "Divido páginas por días para calcular un ritmo."],
  ["Una lectura sostenible es la que puedo mantener en el tiempo sin agotarme. Para planificarla se parte por tres datos: cuántas páginas tiene el texto, de cuántos días dispongo y cuántas páginas leo por día. Con ellos se calcula el ritmo: páginas totales divididas por días. Si el ritmo necesario es mayor que el que puedo sostener, hay que ampliar el plazo o escoger otro texto.",
   "Un plan realista deja un margen. Si calculo que necesito 6 días, conviene agendar 7, porque pueden aparecer imprevistos. También conviene fijar un horario, un lugar tranquilo y una unidad concreta, como un capítulo o 10 páginas. Los objetivos vagos («leer más») no funcionan; los medibles («10 páginas cada tarde») permiten comprobar si voy bien.",
   "La planificación incluye prever obstáculos: un día sin tiempo, un capítulo difícil, cansancio. Un plan sostenible tiene una regla de recuperación, por ejemplo «si falto un día, leo la mitad al siguiente» o «si un capítulo me cuesta, lo divido en dos sesiones». Planificar no vuelve rígida la lectura: ayuda a que el placer o el aprendizaje no queden en una intención."],
  [("ritmo", "cantidad de páginas que se leen en un tiempo dado, por ejemplo por día"), ("plazo", "tiempo disponible para terminar algo"), ("margen", "tiempo extra que se reserva para imprevistos"), ("sostenible", "que se puede mantener en el tiempo sin agotarse")],
  [("Calcular el ritmo", "«Ceniza y brújula» tiene 220 páginas y quieres terminarla en 11 días. ¿Cuántas páginas por día necesitas?",
    ["Divido las páginas totales por los días: 220 ÷ 11.", "El resultado es 20.", "Necesito leer 20 páginas diarias."],
    "20 páginas por día"),
   ("Planificar con margen", "Calculas que necesitas 6 días para un texto. Reservas 1 día de margen y lees 18 páginas diarias. ¿Cuántas páginas tiene el texto y cuántos días agendas?",
    ["Si necesito 6 días de lectura a 18 páginas, el texto tiene 6 × 18 = 108 páginas.", "Agrego 1 día de margen: 6 + 1 = 7.", "Agendo 7 días."],
    "108 páginas; 7 días agendados")],
  [("Calcular el plazo sin dejar margen para imprevistos.", "Se supone que ningún día fallará.", "Agrega al menos un día de margen al plazo calculado."),
   ("Fijar la meta «leer harto».", "No es medible, entonces no se puede comprobar el avance.", "Convierte la meta en una unidad concreta, como 10 páginas cada tarde.")],
  ([E("Un texto tiene 60 páginas y lo leerás en 6 días en partes iguales. ¿Cuántas páginas por día?", "10", "60 dividido en 6 da 10.", "60 // 6"),
    E("¿Qué meta es medible: «leer harto» o «leer 10 páginas cada tarde»?", "«leer 10 páginas cada tarde»", "Tiene una cantidad concreta que puede comprobarse."),
    E("Un margen en un plan lector, ¿sirve para imprevistos o para leer más rápido?", "Para imprevistos", "Es tiempo extra que se reserva por si un día falla.")],
   [E("Un texto tiene 96 páginas. Lees 12 por día. ¿Cuántos días necesitas?", "8", "96 dividido en 12 da 8.", "96 // 12"),
    E("Un texto necesita 8 días de lectura y quieres 2 días de margen. ¿Cuántos días agendas?", "10", "8 más 2 da 10.", "8 + 2"),
    E("Una regla de recuperación dice: «si falto un día, leo la mitad al siguiente». ¿Es una regla de recuperación o una meta de ritmo?", "Una regla de recuperación", "Indica qué hacer cuando el plan se interrumpe.")],
   [E("Tienes «Diario de una bicicleta» (18 páginas) y 4 días. ¿Cuál es la menor cantidad de páginas por día, igual todos los días, que te permite terminar en 4 días? (Redondea hacia arriba.)", "5", "18 dividido en 4 da 4 y sobran 2, así que hay que leer 5 páginas por día.", "(18 + 3) // 4"),
    E("«Ceniza y brújula» tiene 220 páginas. Si lees 25 por día, ¿cuántos días completos necesitas? (Redondea hacia arriba.)", "9", "220 dividido en 25 da 8 y sobran 20 páginas, que requieren un día más.", "(220 + 24) // 25"),
    E("Quieres leer 120 páginas en 10 días, pero 2 de esos días no podrás leer. ¿Cuántas páginas debes leer en cada día de lectura?", "15", "Quedan 8 días de lectura y 120 dividido en 8 da 15.", "120 // (10 - 2)")],
   [E("Valentina planea 30 páginas diarias de una novela de 150 páginas, pero admite que solo puede sostener 15 por día. ¿Su plan es sostenible?", "No", "Su plan exige el doble de lo que reconoce poder sostener."),
    E("Diego tiene 80 páginas y 8 días, pero decide leerlas todas en las últimas 2 noches «para no ocupar tiempo». ¿Su plan reparte la lectura de forma sostenible?", "No", "Concentrar todo al final aumenta el cansancio y deja sin margen.")],
   [E("Elena lee 14 páginas por día. ¿Cuántas páginas lee en 5 días de lectura?", "70", "14 por 5 da 70.", "14 * 5"),
    E("Elena lee 14 páginas por día. ¿Cuántos días de lectura bastan para las 35 páginas de «La regla del juego»? (Redondea hacia arriba.)", "3", "35 dividido en 14 da 2 y sobran 7 páginas, así que hace falta un tercer día.", "(35 + 13) // 14")]),
  [E("Debes leer «Cuaderno de la marea» (24 páginas) en el plazo de una semana, pero te queda libre solo 4 de los 7 días. ¿Cuántas páginas leerás por día de lectura?", "6", "24 dividido en 4 días libres da 6 páginas.", "24 // 4")],
  [E("¿Qué tres datos se necesitan para calcular el ritmo?", "Páginas totales, días disponibles y páginas por día", "Con ellos se calcula cuánto leer y si el plan es realista."),
   E("¿Para qué sirve una regla de recuperación en un plan de lectura?", "Para saber qué hacer si un día falla o un capítulo cuesta", "Es el plan alternativo que mantiene la lectura sostenible."),
   E("Si el ritmo necesario es mayor que el que puedo sostener, ¿qué debo hacer: ampliar el plazo o ignorar el ritmo?", "Ampliar el plazo", "Un plan sostenible se ajusta a lo que puedo cumplir.")],
  ("Planifica la lectura de «Ruido blanco» (cuento de 15 páginas) en una semana. Escribe: 1) cuántas páginas leerás por día, 2) en qué horario y lugar, 3) un día de margen, 4) una regla de recuperación.",
   "15 páginas en 5 días: 3 por día; leeré después de la once, en el living. Día 6 de margen y el 7 de descanso. Si falto un día, leeré 6 páginas al siguiente.",
   ["calcula ritmo con operaciones correctas", "incluye margen", "incluye regla de recuperación"], ["plan escrito de cuatro partes"], ["no dejar margen", "meta vaga"], "Comprueba la división: páginas por días debe dar el total del texto."),
  "Calcula cuántas páginas leíste esta semana en total y cuántas por día en promedio.",
  "Diseña un plan para leer una novela de 150 páginas en un mes, con margen y regla de recuperación.")

# ------------------------------------------------------------------ OA 01 · clase 5
L(OA1, 5,
  MAT,
  "Aprenderé a registrar avances y obstáculos en una bitácora, a interpretar los datos y a ajustar mi plan de lectura con una decisión fundada.",
  ["Planifico una lectura con ritmo y margen.", "Reconozco desafíos y estrategias de comprensión."],
  ["La bitácora lectora es un registro breve que permite ver cómo avanza mi lectura. Cada entrada puede incluir la fecha, las páginas leídas, el avance acumulado, un obstáculo (qué me costó) y la estrategia que usé. Registrar no es un trámite: los datos permiten comprobar si mi plan se cumple y descubrir patrones, por ejemplo que me cuesta leer después de las nueve de la noche.",
   "Para interpretar el registro se comparan dos cantidades: lo planificado y lo real. Si planifiqué 10 páginas por día y leí 7, hay una diferencia de 3 páginas. Una diferencia aislada no es grave, pero si se repite muestra que el plan está mal ajustado. Entonces conviene cambiar una variable: el horario, la cantidad diaria o la estrategia. Los obstáculos se clasifican en externos (falta de tiempo, ruido) y del texto (vocabulario, estructura).",
   "Ajustar un plan es una señal de autonomía, no de fracaso. La decisión debe apoyarse en el registro: «En tres días leí menos de lo previsto porque había mucho ruido; cambio mi horario a la mañana». Una conversación breve sobre lo registrado, con un compañero o una persona de la casa, ayuda a ver soluciones que uno solo no veía. Registrar sin ajustar deja la bitácora como un archivo inútil."],
  [("avance acumulado", "total de páginas leídas hasta una fecha"), ("obstáculo", "algo que dificulta cumplir el plan, ya sea externo o del texto"), ("planificado", "lo que se decidió hacer antes de comenzar"), ("ajuste", "cambio que se hace al plan a partir de los datos")],
  [("Calcular el avance acumulado", "Bitácora de Marta: lunes 8 páginas, martes 6, miércoles 0, jueves 10. ¿Cuál es el avance acumulado al jueves?",
    ["Sumo las páginas de todos los días: 8 + 6 + 0 + 10.", "El resultado es 24.", "El avance acumulado es 24 páginas."],
    "24 páginas"),
   ("Interpretar la diferencia", "Marta había planificado 10 páginas por día durante 4 días. ¿Cuántas páginas debía llevar al jueves y qué diferencia hay con lo real (24)?",
    ["Lo planificado es 10 × 4 = 40.", "La diferencia es 40 − 24 = 16 páginas.", "Es una diferencia grande, así que conviene ajustar el plan."],
    "Debía llevar 40; faltan 16 páginas")],
  [("Anotar solo «leí poco» sin cifras ni obstáculo.", "No se puede comparar con el plan ni descubrir patrones.", "Registra la fecha, las páginas y qué obstáculo hubo."),
   ("Mantener el plan sin cambios aunque el registro muestre que no se cumple.", "Se registra por obligación, sin usar los datos.", "Cambia una variable (horario, cantidad o estrategia) y comprueba el resultado.")],
  ([E("Bitácora: lunes 5 páginas, martes 7 páginas. ¿Cuál es el avance acumulado al martes?", "12", "5 más 7 da 12.", "5 + 7"),
    E("Tu plan era 10 páginas y leíste 6. ¿Cuántas páginas faltaron?", "4", "10 menos 6 da 4.", "10 - 6"),
    E("Un obstáculo como «hubo mucho ruido en mi casa», ¿es externo o del texto?", "Externo", "No depende del contenido del texto, sino del entorno.")],
   [E("Bitácora: miércoles 9 páginas, jueves 7, viernes 12. ¿Cuántas páginas leyó en los tres días?", "28", "9 + 7 + 12 da 28.", "9 + 7 + 12"),
    E("Una lectora anota: «El cuento mezcla narraciones de dos épocas y me cuesta seguirlas». ¿Es un obstáculo externo o del texto?", "Del texto", "La dificultad está en la estructura del cuento."),
    E("En una semana planificaste 70 páginas y leíste 52. ¿Cuántas páginas faltaron?", "18", "70 menos 52 da 18.", "70 - 52")],
   [E("Registro de Pablo: planificó 12 páginas diarias por 5 días y leyó 12, 12, 5, 12, 6. ¿Cuántas páginas leyó en total?", "47", "12 + 12 + 5 + 12 + 6 da 47.", "12 + 12 + 5 + 12 + 6"),
    E("Pablo planificó 12 páginas diarias durante 5 días. ¿Cuántas páginas debía leer en total según el plan?", "60", "12 por 5 da 60.", "12 * 5"),
    E("Pablo leyó 12 páginas casi todos los días. El miércoles leyó 5 y anotó «tuve prueba al día siguiente»; el viernes leyó 6 y anotó lo mismo. ¿Qué obstáculo se repite?", "La prueba del día siguiente (externo)", "Aparece en los dos días de lectura baja y es una causa externa al texto.")],
   [E("Ana registra por cuarta semana que lee menos los viernes por cansancio. ¿Qué ajuste se apoya mejor en el registro: mover la lectura de los viernes a otro momento o cambiar de libro?", "Mover la lectura de los viernes a otro momento", "El obstáculo es el cansancio del día y no el texto."),
    E("Si una lectora no ha cumplido su plan durante 5 días y no cambia nada, ¿está usando su bitácora para ajustar el plan?", "No", "Registrar sin ajustar deja la bitácora sin función.")],
   [E("Bitácora de Camilo: día 1: 15 páginas; día 2: 10; día 3: 12; día 4: 13. Su plan era 50 páginas en 4 días. ¿Cumplió el plan?", "Sí: la suma es 50", "15 + 10 + 12 + 13 da 50, igual al plan.", "15 + 10 + 12 + 13"),
    E("Comparando el día 1 (15 páginas) con el día 2 (10), ¿cuántas páginas más leyó el primer día?", "5", "15 menos 10 da 5.", "15 - 10")]),
  [E("Registro de la semana: lunes 6 páginas, martes 8, miércoles 4, jueves 7. El texto tiene 60 páginas. ¿Cuántas páginas faltan al jueves?", "35", "Ha leído 25 páginas y 60 menos 25 da 35.", "60 - (6 + 8 + 4 + 7)")],
  [E("¿Qué se compara para interpretar un registro: lo planificado y lo real o el título y la portada?", "Lo planificado y lo real", "La diferencia entre ambos muestra si el plan funciona."),
   E("Un registro muestra 18 páginas leídas tres días seguidos, con un plan de 25 diarias. ¿Es una diferencia aislada o repetida?", "Repetida", "Se da los tres días y sugiere que el plan está mal ajustado."),
   E("Si el mismo obstáculo se repite tres días, ¿hay que ajustar el plan o ignorarlo?", "Ajustar el plan", "Un obstáculo repetido es un patrón que requiere un cambio.")],
  ("Con esta bitácora de ejemplo: lunes 10 págs. (sin obstáculo); martes 4 págs. (ruido en la casa); miércoles 5 págs. (ruido en la casa); jueves 12 págs. (sin obstáculo). Plan: 40 páginas. Escribe: 1) el avance acumulado y la diferencia con el plan, 2) el patrón que ves, 3) un ajuste con razón.",
   "Avance: 31 páginas; faltan 9. Patrón: los días con ruido leí menos de la mitad. Ajuste: martes y miércoles leeré en la mañana, antes del ruido, y comprobaré en dos días si subo a 10 páginas.",
   ["calcula avance y diferencia", "identifica un patrón con datos", "propone un ajuste ligado al obstáculo"], ["tres frases con cifras"], ["ajustar sin datos", "no clasificar el obstáculo"], "Revisa que tus tres respuestas usen cifras de la bitácora de ejemplo."),
  "Anota hoy cuántas páginas leíste y si algo te lo impidió.",
  "Diseña una bitácora con columnas de fecha, páginas, obstáculo y estrategia, y llénala con datos de ejemplo de una semana.")

# ------------------------------------------------------------------ OA 01 · clase 6
L(OA1, 6,
  MAT,
  "Aprenderé a recomendar un texto desde una experiencia situada: para una persona concreta, con razones basadas en mi lectura, una advertencia honesta y sin contar el final.",
  ["Justifico selecciones con datos.", "Registro avances y obstáculos en mi bitácora."],
  ["Una recomendación situada nace de una experiencia de lectura real y se dirige a una persona y una situación concretas. «Situada» significa que parte de un lugar y un momento: qué leí, cómo lo leí, qué me costó y qué me dio. Es distinta de un elogio general como «léelo, está genial», que no ayuda a decidir a nadie.",
   "Una buena recomendación tiene cinco elementos: título y género del texto; para quién es y para qué propósito sirve; una razón apoyada en la lectura (un dato o un rasgo, no solo una opinión); una advertencia honesta (por ejemplo, que el inicio es lento o que tiene vocabulario técnico); y ningún spoiler, es decir, no revela el desenlace ni un giro importante. Una advertencia no resta valor: le permite a quien lee decidir con información.",
   "Recomendar desde la propia experiencia no obliga a contar la vida personal. Basta hablar de la lectura: «a mí me costó el segundo capítulo, pero me ayudó releerlo en voz alta». También conviene reconocer los límites: ningún texto sirve a todos. Quien recomienda dice para quién sí y para quién no. Así, la bitácora y la conversación sobre lo leído cierran el ciclo de un lector autónomo."],
  [("recomendación", "mensaje que ayuda a otra persona a decidir si leer un texto"), ("experiencia situada", "experiencia concreta de un lector en un momento y lugar, que se usa como base de una opinión"), ("advertencia", "aviso honesto sobre algo que podría dificultar o no gustar"), ("spoiler", "revelación del final o de un giro importante")],
  [("Reconocer los elementos", "Recomendación: «“Diario de una bicicleta” es una crónica de 18 páginas. Es para quien quiere conocer la ciudad desde la calle. Me gustó porque describe sonidos y olores con detalle. Ojo: el inicio es lento». Señala el elemento de advertencia.",
    ["Reviso los cinco elementos: título y género, destinatario, razón, advertencia, sin spoiler.", "La advertencia avisa algo que puede dificultar.", "Es la frase final: el inicio es lento."],
    "«Ojo: el inicio es lento»"),
   ("Detectar un spoiler", "«“Ruido blanco” es genial: al final descubren que el ruido viene de un aparato oculto en la plaza.» ¿Qué error tiene?",
    ["Reviso si dice el desenlace.", "Revela cómo se explica el misterio.", "Es un spoiler."],
    "Revela el final (spoiler)")],
  [("Escribir «léelo, está genial» como única recomendación.", "No indica para quién, por qué ni qué esperar.", "Agrega destinatario, razón con dato y una advertencia."),
   ("Contar el desenlace para convencer.", "Se cree que revelar el giro da más fuerza.", "Despierta curiosidad con el tema o el conflicto, sin decir cómo termina.")],
  ([E("¿Qué es un spoiler?", "Revelar el final o un giro importante", "Arruina la sorpresa de quien aún no lee."),
    E("En una recomendación, «para quien quiere conocer la ciudad desde la calle» ¿indica el destinatario o la advertencia?", "El destinatario", "Dice para quién sirve el texto."),
    E("¿Cuál de estos NO debe aparecer en una recomendación situada: la advertencia honesta, el destinatario o el final de la historia?", "El final de la historia", "Contar el desenlace es un spoiler; los otros dos son elementos de la recomendación.")],
   [E("Recomendación: «“La regla del juego” es una comedia teatral. Sirve para quien busca reírse en grupo. Los diálogos son rápidos, aunque hay que leer con atención las acotaciones». ¿Cuál es la advertencia?", "Hay que leer con atención las acotaciones", "Es un aviso honesto sobre una exigencia del texto."),
    E("«Es genial, léelo ya» ¿es una recomendación situada o un elogio general?", "Un elogio general", "No nombra destinatario, razón ni advertencia."),
    E("Un lector dice: «Me costó el segundo capítulo, pero me ayudó releerlo en voz alta». ¿Aporta una experiencia situada o un spoiler?", "Una experiencia situada", "Cuenta lo que vivió al leer, sin revelar el final.")],
   [E("Escribe solo el destinatario adecuado para esta recomendación: «“Cómo se mide un terremoto” explica la diferencia entre magnitud e intensidad con ejemplos de la vida diaria». Elige entre: alguien que busca aprender sobre sismos o alguien que busca un cuento de misterio.", "Alguien que busca aprender sobre sismos", "El texto es un artículo de divulgación sobre el tema."),
    E("Una lectora quiere recomendar «Ceniza y brújula» (220 páginas) a un compañero que tiene 5 días libres y lee 20 páginas por día. ¿Debe incluir una advertencia sobre la extensión?", "Sí: en 5 días lee 100 páginas, menos que las 220 del texto", "La diferencia justifica avisar que necesitará más tiempo.", "5 * 20"),
    E("¿Cuál de estas frases es una razón basada en un dato de la lectura? A) «es muy bueno» B) «los diálogos usan frases cortas y rápidas» C) «lo leyó mucha gente»", "B) «los diálogos usan frases cortas y rápidas»", "Describe un rasgo observable del texto; las otras frases son juicios generales o popularidad.")],
   [E("Recomendación A: «Léelo, te va a encantar». Recomendación B: «Es un cuento de 15 páginas, para quien disfruta los mundos imaginados; el inicio exige atención». ¿Cuál es más útil para decidir?", "La B", "Entrega género, extensión, destinatario y advertencia."),
    E("Un compañero dice que recomendar «Ruido blanco» a todos es mejor. ¿Por qué esa idea contradice la clase?", "Porque ningún texto sirve a todos y hay que decir para quién sí y para quién no", "Una recomendación situada reconoce límites.")],
   [E("Recomiendas «Ceniza y brújula» (220 páginas) a Lucas, que puede leer 20 páginas diarias durante 11 días. ¿Alcanza el plazo?", "Sí: 20 por 11 es 220", "El producto coincide con las 220 páginas; puedes decirle que le queda sin margen.", "20 * 11"),
    E("Cecilia recomienda un cuento a un niño de 9 años y a un joven de 15. ¿Qué debe cambiar en su mensaje: el título del cuento o el lenguaje y la advertencia?", "El lenguaje y la advertencia", "La recomendación se ajusta a quien la recibe; el título es el mismo.")]),
  [E("Tu primo de 10 años quiere una historia corta con humor y le dura poco la atención. Opciones: «La regla del juego» (comedia teatral, 35 páginas), «Ceniza y brújula» (novela, 220 páginas) y «Cómo se mide un terremoto» (artículo, 4 páginas). ¿Qué texto le recomiendas y por qué?", "«La regla del juego»", "Es una comedia, usa diálogos rápidos y es la más corta entre las que tienen humor.")],
  [E("¿Qué parte de la recomendación avisa algo que podría dificultar la lectura?", "La advertencia", "Es un aviso honesto."),
   E("¿Se puede recomendar sin contar la vida personal?", "Sí", "Basta hablar de la experiencia de lectura."),
   E("¿Quién decide si el texto sirve: quien recomienda o quien lee?", "Quien lee", "La recomendación da información; la decisión final es de quien lee.")],
  ("Escribe una recomendación de cinco líneas de «Ruido blanco» (cuento de ciencia ficción de 15 páginas, sobre un pueblo donde nadie oye su propia voz; el inicio es lento) para una persona de tu curso que busca un texto breve para recrearse. Incluye título y género, destinatario, una razón con dato, una advertencia y ningún spoiler.",
   "«Ruido blanco» es un cuento de ciencia ficción de 15 páginas. Te lo recomiendo si quieres recrearte con algo breve y misterioso. Me atrapó porque cada párrafo muestra un detalle nuevo del pueblo sin sonido. Ojo: el inicio es lento y cuesta ordenar los días. No te cuento el final para que lo descubras tú.",
   ["incluye los cinco elementos", "se dirige a una persona concreta", "no revela el desenlace"], ["recomendación escrita"], ["elogio general", "spoiler"], "Subraya cada elemento y comprueba que ninguno falte; si algo revela el final, bórralo."),
  "Cuéntale a alguien de tu casa una recomendación de lo último que leíste sin decir el final.",
  "Escribe dos recomendaciones distintas del mismo texto para dos personas con intereses diferentes.")

"""Lengua y Literatura EPJA Media N1, módulo 1, OAD-02: analizar un poema a partir del sentido figurado y de los elementos sonoros (ritmo y rima). Todos los poemas y situaciones son inventados y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los poemas, frases y situaciones de este cuaderno son inventados («de ejemplo») y están escritos en cada ejercicio: "
    "no necesitas libros, audio, video ni internet. Si quieres sentir el ritmo, lee los poemas en voz alta o pide a otra persona que los lea. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)
build = make_build(MATERIALS)

O = "EPJA-LELI-NM1-OAD-02"
PRIOR = ["Uso frases como «me muero de risa» sin pensar que no son literales.", "Reconozco cuando un texto está escrito en versos.", "Sé decir qué me hace sentir un poema o una canción."]

FRASES = ("Situaciones de ejemplo (inventadas). 1) Antes de una entrevista de trabajo, Marcela dice: «Tengo mariposas en el estómago». "
          "2) Al ver la cuenta de la luz, Jorge dice: «Se me heló la sangre». "
          "3) El supervisor dice: «El tiempo es oro; entreguemos el pedido hoy». "
          "4) Rosa dice: «Cerrar la ruta fue un balde de agua fría para el negocio». "
          "5) Rosa llenó un balde de agua fría para lavar el piso.")
CALLE = ("Poema (inventado), «Mi calle de noche». Estrofa 1: «La calle es un río oscuro / que baja con sus faroles; / el viento, vecino cansado, / golpea todos los portones». "
         "Estrofa 2: «La luna camina despacio / como una vecina que espera; / yo cruzo la calle en silencio / y llevo la noche a cuestas».")
PARADERO = ("Poema (inventado), «Lluvia en el paradero». Estrofa 1: «La lluvia golpea el paradero / con dedos de plata y cristal; / la gente, bajo un mismo alero, / comparte el frío y el umbral». "
            "Estrofa 2: «El bus es un barco cansado / que tarda en llegar al andén; / los sueños, en fila, mojados, / esperan la orilla también».")
TAMBOR = ("Poema (inventado), «Tambor de lluvia». Estrofa 1: «Gota a gota, gota a gota, / la lluvia toca el tejado; / gota a gota, gota a gota, / me quedo aquí, a tu lado». "
          "Estrofa 2: «Paso a paso, paso a paso, / llega el sueño a la ventana; / paso a paso, paso a paso, / se hace tarde en la mañana».")
TURNO = ("Poema (inventado), «Turno de noche». Estrofa 1: «La bodega es un mar de cajas / que duerme bajo los focos. / Mis manos, dos barcos cansados, / navegan pasillo adentro». "
         "Estrofa 2: «El reloj, vigilante terco, / cuenta despacio las horas. / A las seis, el sol entra por la puerta / y me abraza como a un hijo que vuelve».")
MARTILLO = ("Poema (inventado), «Mi martillo». Estrofa 1: «Mi martillo es un pájaro de hierro / que canta clavos en la tarde. / El polvo es una niebla de aserrín». "
            "Estrofa 2: «Al caer el sol, mis hombros / pesan como dos sacos de cemento / y la casa, por fin, se levanta».")


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(O, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ============================================================ clase 1
K(1, FRASES,
  "Hoy parto de las frases que uso a diario y distingo cuándo hablo en sentido literal y cuándo en sentido figurado.",
  ["Ya usas lenguaje figurado cada día. Cuando alguien dice «tengo mariposas en el estómago», no hay insectos dentro de su cuerpo: quiere decir que está nervioso. Entiendes la frase sin pensarlo porque conoces la costumbre de tu comunidad.",
   "El sentido literal es el significado habitual de las palabras: «un balde de agua fría» es, literalmente, un recipiente con agua. El sentido figurado usa las mismas palabras para decir otra cosa, casi siempre más viva: un «balde de agua fría» es una noticia que apaga el ánimo.",
   "Los poemas usan mucho el sentido figurado porque con pocas palabras logran que sientas algo. Para reconocerlo, pregúntate: ¿esta frase puede ser verdad tal cual? Si no, probablemente es figurada. Después pregúntate qué quiere decir y qué efecto produce en quien la escucha."],
  [("sentido literal", "significado habitual y directo de las palabras"), ("sentido figurado", "uso de palabras con otro significado para decir algo de modo más vivo"), ("expresión", "frase o dicho que se usa para decir algo"), ("efecto", "lo que una frase hace sentir o pensar en quien la lee")],
  [("Literal o figurado", "Frase 5: «Rosa llenó un balde de agua fría para lavar el piso». Frase 4: «Cerrar la ruta fue un balde de agua fría para el negocio».",
    ["En la frase 5 hay un balde y agua de verdad: es literal.", "En la frase 4 no hay balde: la noticia apaga el ánimo.", "Es figurado."], "Frase 5 literal; frase 4 figurada"),
   ("Qué quiere decir", "Frase 2: «Se me heló la sangre». Pregunta: ¿qué significa y qué efecto produce?",
    ["La sangre no se congela de verdad.", "Significa que Jorge sintió mucho susto.", "El efecto es que sentimos su impresión como un frío que recorre el cuerpo."], "Significa asustarse mucho; transmite impresión")],
  [("Entender «mariposas en el estómago» como si hubiera insectos.", "Se lee la frase literalmente.", "Pregunta si podría ser verdad; si no, busca qué quiere decir."),
   ("Explicar solo lo que quiere decir y no el efecto.", "Falta decir qué siente quien lee.", "Agrega qué sensación produce la expresión.")],
  [("abc", "{F} ¿Cuál de las frases está en sentido literal?", "La 5, porque Rosa usa un balde con agua", "La 1, porque hay mariposas", "La 3, porque el tiempo es de oro", "Solo en la frase 5 hay un balde de agua verdadero."),
   ("ab", "{F} ¿Qué quiere decir Marcela con «tengo mariposas en el estómago»?", "Que está nerviosa", "Que se comió algo en mal estado", "La frase es figurada y expresa nerviosismo antes de la entrevista."),
   ("{F} ¿Cuántas de las cinco frases están en sentido literal? Escribe el número.", "1", "Solo la frase 5 describe un hecho tal como suena."),
   ("abc", "En Lengua y Literatura: ¿qué es el sentido figurado?", "Usar palabras con otro significado para decir algo de modo más vivo", "Decir exactamente lo que las palabras dicen", "Escribir con letra más grande", "El sentido figurado cambia el significado habitual de las palabras."),
   ("abc", "{F} ¿Qué quiere decir el supervisor con «el tiempo es oro»?", "Que el tiempo es muy valioso y no hay que perderlo", "Que los relojes son de oro", "Que hay que cobrar por cada minuto", "Se compara el valor del tiempo con el del oro."),
   ("ab", "{F} «Se me heló la sangre» expresa", "un susto fuerte", "una enfermedad", "Jorge se asustó al ver la cuenta; no habla de una enfermedad."),
   ("abc", "Lee: «Don Raúl dijo que su hija es un sol». ¿Qué quiso decir?", "Que su hija es alegre y cálida", "Que su hija es de tamaño enorme", "Que su hija trabaja de día", "Compara a la hija con el sol para destacar su calidez."),
   ("abc", "Lee: «Mañana a las ocho me llegó una lluvia de llamadas». ¿Cuál es el sentido figurado?", "Muchas llamadas llegaron seguidas", "Cayó agua del cielo durante la mañana", "Alguien trajo un paraguas", "Se compara la cantidad de llamadas con una lluvia."),
   ("abc", "Lee: «La gerenta puso el grito en el cielo». ¿Qué expresa?", "Que se enojó mucho", "Que miró hacia arriba", "Que celebró un buen resultado", "La expresión figurada indica enojo, no un gesto literal."),
   ("ab", "{F} ¿Qué efecto produce «balde de agua fría» en quien escucha la noticia del cierre de la ruta?", "Sentimos que la noticia apaga las ganas", "Sentimos que hace calor", "Esa imagen sugiere impresión y desánimo, no temperatura."),
   ("abc", "Un compañero dice que «mariposas en el estómago» es literal porque él las sintió. ¿Qué le respondes?", "Se siente así, pero la frase es figurada: no hay mariposas reales", "Tiene razón, es literal", "Ninguna frase es figurada", "Sentir algo no vuelve literal una expresión: no hay insectos."),
   ("abc", "{F} ¿Por qué la frase 3 sirve en el trabajo?", "Porque con pocas palabras anima a no perder tiempo", "Porque describe un objeto de oro", "Porque no tiene ningún significado", "Una expresión figurada comunica una idea rápida y vivaz."),
   ("ab", "{F} Si Rosa dijera «llené un balde de agua fría» para contar la noticia, ¿se entendería lo mismo?", "No, se entendería literalmente: un balde con agua", "Sí, siempre se entiende igual", "Sin la comparación con la noticia, la frase queda en sentido literal.")],
  ("abc", "En una conversación en tu centro alguien dice «estoy hecho polvo». ¿Cómo lo entiendes?", "Que está muy cansado", "Que se llenó de polvo literalmente", "Que está muy contento", "Es una expresión figurada para decir cansancio."),
  [("En Lengua y Literatura: ¿qué es el sentido literal?", "El significado habitual y directo de las palabras", "Es lo que las palabras dicen sin otro sentido agregado."),
   ("¿Cómo reconoces una expresión figurada?", "Porque no puede ser verdad tal cual", "Si una frase no es literalmente posible, se lee con otro sentido."),
   ("Escribe una expresión figurada que uses a diario.", "Por ejemplo: me muero de hambre", "Es figurada porque nadie muere de verdad por esa razón.")],
  ("Lee las cinco situaciones: {F} Elige tres frases (por ejemplo, la 1, la 2 y la 4). Para cada una escribe: qué quiere decir y qué efecto produce. Después escribe una expresión figurada que se use en tu trabajo o tu barrio, y qué significa.",
   "Frase 1: significa estar nervioso; el efecto es sentir un cosquilleo. Frase 2: significa asustarse; el efecto es una sensación de frío. Frase 4: significa una mala noticia; apaga el ánimo. Mi expresión: «estar a full» significa tener mucho trabajo.",
   ["tres frases con significado y efecto", "una expresión propia explicada", "distingue lo literal de lo figurado"],
   ["una lista de cuatro puntos"],
   ["explicar solo el significado sin el efecto", "tomar como verdad una frase figurada"],
   "Pregunta: «¿Esa frase podría ser verdad tal cual?»."),
  "Anota tres expresiones figuradas que escuches hoy y qué quieren decir.",
  "Escribe dos frases: una literal y una figurada que usen la palabra «mar».")

# ============================================================ clase 2
K(2, CALLE,
  "Hoy conozco las palabras para hablar de un poema: verso, estrofa, comparación, metáfora y personificación.",
  ["Un poema se organiza en versos, que son cada línea, y en estrofas, que son grupos de versos separados por un espacio. Quien habla en el poema se llama hablante lírico: no es siempre el autor, sino la voz que dice lo que siente o ve. Contar versos y estrofas es el primer paso para describir un poema.",
   "Hay tres figuras muy usadas del lenguaje figurado. La comparación une dos cosas con una palabra como «como» o «parece». La metáfora dice que una cosa es otra, sin «como»: «la calle es un río». La personificación da acciones o sentimientos de persona a una cosa: «el viento golpea la puerta».",
   "Cada figura cumple una función: nos hace ver una cosa de otra manera. Si la calle es un río oscuro, la sentimos larga, silenciosa y en movimiento. Por eso, al analizar, no basta nombrar la figura: hay que decir qué sentido y qué efecto tiene."],
  [("verso", "cada línea de un poema"), ("estrofa", "grupo de versos separado de otro por un espacio"), ("hablante lírico", "voz que habla en el poema"), ("metáfora", "figura que dice que una cosa es otra, sin «como»")],
  [("Identificar una metáfora", "Verso: «La calle es un río oscuro». ¿Qué figura es?",
    ["Dice que la calle «es» un río, sin «como».", "Une dos cosas distintas: calle y río.", "Es una metáfora."], "Metáfora: la calle se ve como un río"),
   ("Identificar una comparación", "Versos: «La luna camina despacio / como una vecina que espera».",
    ["Aparece la palabra «como».", "Se une la luna con una vecina.", "Además, la luna «camina»: personificación."], "Comparación, con personificación")],
  [("Llamar comparación a toda figura.", "La comparación necesita una palabra como «como» o «parece».", "Busca la palabra de comparación; si no está, puede ser una metáfora."),
   ("Confundir verso con estrofa.", "El verso es una línea; la estrofa es un grupo de versos.", "Cuenta las líneas para los versos y los bloques para las estrofas.")],
  [("{F} ¿Cuántas estrofas tiene el poema? Escribe el número.", "2", "El poema separa sus versos en dos bloques."),
   ("abc", "{F} ¿Cuántos versos tiene cada estrofa?", "Cuatro", "Tres", "Seis", "Cada estrofa del poema tiene exactamente cuatro líneas."),
   ("ab", "{F} ¿Con qué se compara la calle en el primer verso?", "Con un río oscuro", "Con una luna", "El verso dice «La calle es un río oscuro»."),
   ("abc", "En Lengua y Literatura: ¿qué es una metáfora?", "Decir que una cosa es otra, sin usar «como»", "Contar los versos de un poema", "Repetir un sonido al final de dos versos", "La metáfora identifica dos cosas distintas directamente."),
   ("abc", "{F} ¿Qué figura es «la luna camina despacio como una vecina que espera»?", "Comparación, porque usa «como»", "Metáfora, porque dice que la luna es un río", "Estrofa, porque tiene cuatro versos", "Une dos cosas con la palabra «como»."),
   ("ab", "{F} «El viento, vecino cansado, golpea todos los portones» es", "una personificación, porque el viento actúa como persona", "un verso sin figuras", "Al viento se le dan acciones humanas: golpear y estar cansado."),
   ("abc", "{F} ¿Qué verso es una personificación de la luna?", "«La luna camina despacio»", "«La calle es un río oscuro»", "«Yo cruzo la calle en silencio»", "Caminar es una acción de persona atribuida a la luna."),
   ("abc", "{F} ¿Qué efecto produce llamar «río oscuro» a la calle?", "La imaginamos larga, en movimiento y silenciosa", "Pensamos que tiene agua verdadera", "Sentimos que es una calle ruidosa", "El efecto de la metáfora viene de lo que tienen en común calle y río."),
   ("abc", "{F} ¿Quién habla en el poema cuando dice «yo cruzo la calle en silencio»?", "El hablante lírico", "Una vecina llamada Luna", "Un río", "La voz que dice «yo» es el hablante lírico."),
   ("ab", "{F} Un compañero dice que «llevo la noche a cuestas» es literal. ¿Qué respondes?", "Es figurado: la noche no se puede cargar", "Es literal: se cargan sacos de noche", "Nadie puede cargar la noche; la frase expresa que el hablante siente su peso."),
   ("abc", "{F} ¿Qué dos ideas relaciona la frase «Llevo la noche a cuestas»?", "La noche con una carga pesada", "La noche con una calle ancha", "La noche con un río", "Se dice que la noche se carga como un bulto."),
   ("abc", "{F} ¿Cuál es la diferencia entre la metáfora «la calle es un río» y la comparación «la calle es como un río»?", "La comparación usa la palabra «como»", "La metáfora tiene más versos", "No hay diferencia en ninguna parte", "Solo la comparación incluye una palabra de comparación."),
   ("ab", "{F} Si cambiamos «La calle es un río oscuro» por «La calle es angosta», ¿se mantiene la figura?", "No, ya no hay metáfora: es una descripción literal", "Sí, se mantiene la metáfora", "«Angosta» describe la calle sin compararla con otra cosa.")],
  ("abc", "Un vecino te lee una frase de su cuaderno: «La ciudad despierta y se estira». ¿Qué figura usa?", "Personificación", "Comparación", "Estrofa", "A la ciudad se le dan acciones de persona."),
  [("En Lengua y Literatura: ¿qué es una personificación?", "Dar acciones o sentimientos de persona a una cosa", "El viento «golpea» como lo haría una persona."),
   ("¿Qué diferencia hay entre verso y estrofa?", "El verso es una línea y la estrofa un grupo de versos", "Varios versos juntos forman una estrofa del poema."),
   ("¿Qué debe decir un análisis además de nombrar la figura?", "Qué significa y qué efecto produce", "Con solo nombrar la figura no se explica el poema.")],
  ("Lee el poema: {F} En tu cuaderno haz una tabla con tres columnas: verso, figura y qué efecto produce. Analiza tres versos (por ejemplo, el primero de cada estrofa y uno más). Termina con una oración sobre cómo te hace sentir el poema.",
   "Verso 1: «La calle es un río oscuro», metáfora, la calle se imagina larga y silenciosa. Verso: «El viento, vecino cansado», personificación, el viento parece una persona fatigada. Verso: «La luna camina despacio», personificación. El poema me hace sentir calma.",
   ["tres versos con su figura", "explica el efecto de cada figura", "expresa lo que siente"],
   ["una tabla de tres filas y una oración"],
   ["nombrar la figura sin decir su efecto", "llamar «metáfora» a todo"],
   "Pregunta: «¿Qué cosa se compara con qué otra?»."),
  "Lee el poema en voz alta y marca con lápiz un verso que te gusta.",
  "Escribe una metáfora y una personificación sobre un lugar de tu barrio.")

# ============================================================ clase 3
K(3, PARADERO,
  "Hoy aprendo, paso a paso, a analizar un poema: leerlo, subrayar figuras, decir qué significan y qué efecto producen.",
  ["Analizar un poema es leerlo con atención para explicar cómo logra lo que nos hace sentir. Hay un método de cuatro pasos. Uno: leerlo completo, de preferencia en voz alta. Dos: subrayar las figuras del lenguaje figurado. Tres: decir qué significan en el poema. Cuatro: explicar el efecto que producen.",
   "Una figura puede ser una metáfora, una comparación o una personificación, y puede mezclarse con otra: «el bus es un barco cansado» tiene metáfora, porque dice que el bus es un barco, y personificación, porque lo llama cansado. No se necesita encontrar una sola etiqueta; se necesita explicar el sentido.",
   "El sentido global es la idea que el poema deja en conjunto. En «Lluvia en el paradero» podemos ver a personas que esperan juntas bajo la lluvia, compartiendo el frío y el silencio. Interpretar el poema es unir las figuras con ese sentido global."],
  [("analizar", "mirar las partes de un texto para explicar cómo funciona"), ("sentido global", "idea general que deja el poema en conjunto"), ("paradero", "lugar donde se espera el transporte público"), ("efecto", "sensación o idea que produce una figura en quien lee")],
  [("Los cuatro pasos", "Verso: «con dedos de plata y cristal». Se analiza paso a paso.",
    ["Leo el poema en voz alta.", "Subrayo la figura: la lluvia tiene «dedos» de plata: personificación y metáfora.", "Significa que la lluvia golpea con suavidad y brillo.", "Efecto: imaginamos una lluvia delicada y brillante."], "Personificación; golpe suave y brillante"),
   ("Del detalle al sentido global", "Versos: «la gente, bajo un mismo alero, / comparte el frío y el umbral».",
    ["Observo: personas bajo un mismo alero.", "Entiendo: comparten espacio y frío.", "Sentido global: la espera une a las personas."], "La espera une a quienes la comparten")],
  [("Dar solo el significado literal de cada verso.", "Se pierde cómo el poema construye su sentido.", "Agrega qué figura hay y qué efecto produce."),
   ("Nombrar la figura sin relacionarla con el sentido global.", "El análisis queda como una lista de nombres.", "Cierra con una idea que una las figuras del poema.")],
  [("abc", "{F} ¿Dónde esperan las personas del poema?", "En un paradero, bajo un alero", "En una sala de hospital", "En una feria al aire libre", "El poema dice «paradero» y «alero»."),
   ("ab", "{F} ¿Qué se compara con «un barco cansado»?", "El bus", "La lluvia", "La segunda estrofa dice que el bus es un barco cansado."),
   ("{F} ¿Cuántos versos tiene el poema completo? Escribe el número.", "8", "Cada una de las dos estrofas tiene cuatro versos."),
   ("abc", "En Lengua y Literatura: ¿cuál es el primer paso para analizar un poema?", "Leerlo completo, de preferencia en voz alta", "Escribir la conclusión", "Contar las letras", "Sin leer el poema completo no se pueden ver sus figuras."),
   ("abc", "{F} ¿Qué figura hay en «con dedos de plata y cristal»?", "Personificación con metáfora: la lluvia tiene dedos brillantes", "Comparación, porque usa la palabra «como»", "Estrofa de cuatro versos", "Se dan partes del cuerpo a la lluvia y se la describe con materiales brillantes."),
   ("ab", "{F} «Los sueños, en fila, mojados, / esperan la orilla también» es", "una personificación: los sueños esperan como personas", "una descripción literal", "Los sueños no pueden hacer fila ni esperar de verdad."),
   ("abc", "{F} ¿Qué efecto produce llamar «barco cansado» al bus?", "Sugiere lentitud y esfuerzo para llegar", "Sugiere que el bus es rápido", "Sugiere que viaja sobre el mar", "Los barcos cansados avanzan lento, como el bus que tarda."),
   ("abc", "{F} ¿Qué significa que la gente «comparte el frío y el umbral»?", "Que están juntas en la misma espera y la misma incomodidad", "Que cada persona está en una casa distinta", "Que el frío es una mercancía", "Compartir muestra que la situación las une."),
   ("abc", "{F} ¿Cuál sería el sentido global del poema?", "La espera bajo la lluvia une a las personas", "Un recuerdo de un viaje en barco", "Una crítica a la lluvia", "Todas las figuras muestran una espera compartida."),
   ("ab", "{F} Una estudiante dice que «el bus es un barco» significa que el bus navega por el mar. ¿Tiene razón?", "No, es una metáfora que habla de lentitud y esfuerzo", "Sí, el bus se convierte en barco", "La metáfora no cambia lo que el bus es, solo lo describe de otra manera."),
   ("abc", "{F} ¿Qué pasa si leemos «los sueños, en fila, mojados» solo en sentido literal?", "Se pierde que se habla de la espera y las ganas de llegar", "El verso se entiende mejor", "No cambia nada", "En sentido literal los sueños no pueden mojarse."),
   ("abc", "{F} Una persona resume: «El poema habla de lluvia y de un bus». ¿Qué le falta?", "Explicar las figuras, su efecto y el sentido global", "Agregar más datos de la lluvia", "Escribir en mayúscula", "Un resumen no interpreta; el análisis agrega sentido."),
   ("ab", "{F} Si el poema dijera «la gente espera con paciencia el bus», ¿qué cambia?", "Se pierde la figura y el poema se vuelve más literal", "Se mantiene toda la fuerza del poema", "La frase directa ya no usa una imagen para comunicar la espera.")],
  ("abc", "En una reunión de vecinos te piden explicar por qué un poema te gustó. ¿Qué ayuda más?", "Citar un verso, decir qué figura tiene y qué efecto te produjo", "Decir solo «me gustó mucho»", "Leerlo sin comentarios", "Un análisis combina cita, figura y efecto."),
  [("En Lengua y Literatura: ¿cuántos pasos tiene el método de análisis de hoy?", "Cuatro: leer, subrayar figuras, decir qué significan y explicar el efecto", "Es un método simple y repetible."),
   ("¿Qué es el sentido global de un poema?", "La idea general que deja en conjunto", "Une las figuras en una idea."),
   ("¿Puede un verso tener dos figuras a la vez?", "Sí, por ejemplo metáfora y personificación", "Lo importante es explicar su sentido.")],
  ("Lee el poema: {F} Aplica los cuatro pasos a la estrofa 2: escribe (1) las figuras que encuentras, (2) qué significan, (3) qué efecto producen y (4) el sentido global de esa estrofa en dos oraciones.",
   "Figuras: «el bus es un barco cansado» (metáfora y personificación); «los sueños, en fila, mojados, esperan» (personificación). Significan lentitud y deseo de llegar. Efecto: sentimos paciencia y cansancio. Sentido global: la espera es lenta pero compartida.",
   ["encuentra al menos dos figuras", "explica significado y efecto", "cierra con un sentido global"],
   ["un párrafo de cuatro a seis oraciones"],
   ["solo nombrar figuras", "no escribir el sentido global"],
   "Pregunta: «¿Qué idea une todas las figuras?»."),
  "Subraya con lápiz en el poema todas las palabras que no podrían ser literales.",
  "Escribe una estrofa de cuatro versos con una personificación sobre una espera que hayas vivido.")

# ============================================================ clase 4
K(4, TAMBOR + " " + PARADERO,
  "Hoy practico con apoyo cómo suena un poema: reconozco la rima consonante y asonante y el ritmo que da la repetición.",
  ["Un poema no solo se entiende: también suena. Los elementos sonoros más comunes son la rima y el ritmo. La rima es la coincidencia de sonidos al final de dos versos, a partir de la última vocal que lleva el golpe de voz. Hay dos tipos: consonante y asonante.",
   "En la rima consonante coinciden vocales y consonantes: «camino» y «destino». En la rima asonante coinciden solo las vocales: «puerto» y «cielo». Para reconocerla, di las dos palabras en voz alta y fíjate desde la vocal fuerte hasta el final. Si coincide todo, es consonante; si coinciden solo las vocales, es asonante.",
   "El ritmo es la cadencia que producen las pausas, los golpes de voz y las repeticiones. Una repetición como «gota a gota, gota a gota» crea un ritmo parecido al de la lluvia. Al analizar, relaciona el sonido con el sentido: ¿qué efecto produce ese ritmo en quien escucha?"],
  [("rima", "coincidencia de sonidos al final de dos versos"), ("rima consonante", "coinciden vocales y consonantes desde la última vocal con golpe de voz"), ("rima asonante", "coinciden solo las vocales"), ("ritmo", "cadencia de pausas, golpes de voz y repeticiones")],
  [("Rima consonante", "Palabras: «camino» y «destino».", ["Desde la vocal fuerte: ca-MI-no y des-TI-no.", "Coinciden «ino»: vocales y consonantes."], "Rima consonante"),
   ("Rima asonante", "Palabras: «casa» y «palma».", ["Casa: CA-sa, vocales a-a.", "Palma: PAL-ma, vocales a-a.", "Las consonantes no coinciden."], "Rima asonante")],
  [("Decir que riman las palabras que empiezan igual.", "La rima se mira al final, desde la vocal fuerte.", "Compara el final de las palabras."),
   ("Pensar que repetir una palabra es rima.", "La repetición es otro recurso que da ritmo.", "Distingue palabras iguales de palabras que solo suenan igual al final.")],
  [("abc", "{F} ¿Qué se repite en los versos 1 y 3 de la estrofa 1 de «Tambor de lluvia»?", "«Gota a gota, gota a gota»", "«Paso a paso, paso a paso»", "«Me quedo aquí, a tu lado»", "Los versos 1 y 3 de la estrofa 1 son iguales."),
   ("ab", "{F} ¿Qué palabras riman en consonante en la estrofa 1 de «Tambor de lluvia»?", "tejado y lado", "gota y lluvia", "Las dos palabras terminan en «-ado»."),
   ("{F} ¿Qué palabra rima con «ventana» en la estrofa 2 de «Tambor de lluvia»? Escribe una sola palabra.", "mañana", "Ventana y mañana terminan en «-ana»."),
   ("abc", "En Lengua y Literatura: ¿qué es la rima consonante?", "Coinciden vocales y consonantes desde la última vocal con golpe de voz", "Coinciden solo las vocales", "Se repite una palabra al principio", "En la consonante coincide todo el sonido final."),
   ("abc", "¿Qué par de palabras tiene rima asonante?", "puerto y cielo", "camino y destino", "farol y sol", "Coinciden las vocales e-o pero no las consonantes."),
   ("ab", "¿Qué par tiene rima consonante?", "farol y sol", "casa y palma", "Las dos terminan en «-ol», con las mismas consonantes y vocales."),
   ("abc", "{F} ¿Qué rima hay entre «paradero» y «alero» en «Lluvia en el paradero»?", "Consonante", "Asonante", "No hay rima", "Coinciden las letras desde la «e» fuerte: «-ero»."),
   ("abc", "{F} ¿Qué palabras riman en consonante en la estrofa 2 de «Lluvia en el paradero»?", "andén y también", "cansado y andén", "sueños y orilla", "Los versos 2 y 4 terminan en «-én»."),
   ("abc", "{F} ¿Qué tipo de rima hay entre «cansado» y «mojados»?", "Asonante, porque coinciden las vocales a-o", "Consonante, porque terminan igual", "Ninguna", "Las vocales coinciden pero no las consonantes completas."),
   ("ab", "{F} ¿Qué efecto produce la repetición «gota a gota» en el poema «Tambor de lluvia»?", "Imita el golpe repetido de la lluvia", "Aumenta el número de estrofas", "La repetición crea un ritmo parecido al de las gotas."),
   ("abc", "{F} ¿Qué palabra repetida da el ritmo en los versos 1 y 3 de la estrofa 2 de «Tambor de lluvia»?", "paso", "mañana", "sueño", "Los versos repiten «paso a paso», y esa repetición crea ritmo."),
   ("abc", "Un lector dice que «gota» y «gota» riman. ¿Qué respuesta es mejor?", "Es una repetición, no una rima: la rima exige palabras distintas con sonido parecido", "Sí, riman porque son iguales", "No riman porque están escritas distinto", "Repetir una palabra no es lo mismo que rimar."),
   ("ab", "{F} Si cambiamos «lado» por «camino» en el verso 4 de «Tambor de lluvia», ¿qué pasa con la rima?", "Se pierde la rima con «tejado»", "Se mantiene igual", "«Camino» no termina en «-ado», por eso ya no rima con «tejado».")],
  ("abc", "En un taller de canto del barrio, alguien dice: «Las canciones que riman se aprenden más fácil». ¿Qué elemento sonoro ayuda a recordar?", "La rima y el ritmo", "Solo el título", "El tamaño del papel", "La rima y el ritmo ayudan a memorizar."),
  [("En Lengua y Literatura: ¿qué es la rima asonante?", "Coinciden solo las vocales desde el golpe de voz", "En ella las consonantes finales pueden ser distintas."),
   ("¿Qué recurso da ritmo en «gota a gota, gota a gota»?", "La repetición", "Repetir las mismas palabras da una cadencia al poema."),
   ("¿Cómo reconoces una rima?", "Comparo el final de las palabras desde la vocal fuerte", "Es lo que suena parecido al final.")],
  ("Lee los poemas: {F} Elige la estrofa 1 de «Lluvia en el paradero». Anota qué versos riman, el tipo de rima y qué ritmo percibes al leerla en voz alta. Termina con una oración que relacione el sonido con el sentido.",
   "Riman «paradero» y «alero» (consonante) y «cristal» y «umbral» (consonante). El ritmo es pausado, como la espera. El sonido regular da sensación de calma.",
   ["identifica pares que riman y su tipo", "describe el ritmo al leer", "relaciona sonido y sentido"],
   ["una lista de tres puntos y una oración"],
   ["confundir repetición con rima", "no relacionar el sonido con el sentido"],
   "Pregunta: «¿Esas palabras terminan igual desde la vocal fuerte?»."),
  "Lee en voz alta «Tambor de lluvia» y marca con palmadas el ritmo.",
  "Escribe dos versos que rimen en consonante sobre tu barrio.")

# ============================================================ clase 5
K(5, TURNO,
  "Hoy aplico lo aprendido a un poema sobre el trabajo: analizo sus figuras y el efecto que tiene el poema en quien lo lee.",
  ["Los poemas no hablan solo de paisajes: también cuentan el trabajo, el cansancio y la espera. El poema de hoy muestra un turno de noche en una bodega. Para analizarlo, puedes aplicar todo lo que ya sabes: ver las figuras, ver los sonidos y unirlos en un sentido global.",
   "Un poema puede no tener rima y seguir siendo poema. Cuando los versos no riman se les llama verso libre. En ese caso la fuerza está en las imágenes y en el ritmo de las pausas. Si el poema no rima, no hay que inventar una rima: se analiza lo que sí tiene.",
   "Una buena práctica es redactar un párrafo de análisis con cuatro partes: la figura, la cita del verso, qué significa y qué efecto produce. Si además dices qué sentido global le encuentras, tu análisis es completo. Y recuerda: si el poema te hace pensar en tu propio trabajo, esa conexión también es parte de la lectura."],
  [("verso libre", "verso que no sigue una rima ni un número fijo de sílabas"), ("imagen", "descripción que hace ver o sentir algo en la mente"), ("bodega", "lugar donde se guardan mercaderías"), ("vigilante", "que cuida o vigila")],
  [("Analizar una metáfora", "Verso: «La bodega es un mar de cajas». Se redacta el análisis.",
    ["Figura: metáfora, la bodega «es» un mar.", "Significa que hay muchas cajas, como olas, y que el lugar es grande y quieto.", "Efecto: sentimos la soledad y el tamaño del lugar."], "Metáfora de la bodega como mar"),
   ("Analizar una comparación", "Verso: «y me abraza como a un hijo que vuelve». Se analiza.",
    ["Figura: comparación con «como»; además el sol «abraza»: personificación.", "Significa que la luz de la mañana trae alivio.", "Efecto: sentimos ternura al terminar el turno."], "Comparación; alivio al terminar el turno")],
  [("Buscar rimas que no hay y decir que el poema «no rima, entonces no es poema».", "Un poema puede estar escrito en verso libre.", "Analiza imágenes, ritmo y sentido."),
   ("Analizar solo una figura y olvidar el resto.", "Quedan sin explicar partes del poema.", "Revisa estrofa por estrofa.")],
  [("abc", "{F} ¿Dónde ocurre la escena del poema?", "En una bodega, de noche", "En una cocina, de día", "En un puerto, al mediodía", "El poema dice que la bodega duerme bajo los focos."),
   ("ab", "{F} ¿A qué hora entra el sol por la puerta?", "A las seis", "A las tres", "El verso dice «A las seis, el sol entra por la puerta»."),
   ("{F} ¿Cuántos versos tiene el poema completo? Escribe el número.", "8", "Cada una de las dos estrofas tiene cuatro versos."),
   ("abc", "En Lengua y Literatura: ¿qué es el verso libre?", "Verso que no sigue una rima fija", "Verso que siempre rima en consonante", "Verso que se repite al final de cada estrofa", "El verso libre no obedece una rima fija."),
   ("abc", "{F} ¿Qué figura hay en «mis manos, dos barcos cansados»?", "Metáfora, porque las manos son barcos", "Rima consonante", "Una estrofa", "Dice que las manos son barcos y agrega «cansados»."),
   ("ab", "{F} «El reloj, vigilante terco, / cuenta despacio las horas» es", "una personificación, porque el reloj vigila y cuenta", "una rima asonante", "Al reloj se le dan acciones de persona."),
   ("abc", "{F} ¿Qué significa «mis manos, dos barcos cansados, navegan pasillo adentro»?", "Que el trabajador avanza con esfuerzo por los pasillos", "Que está de vacaciones en el mar", "Que arregla barcos de verdad", "Las manos cansadas se mueven entre estantes como barcos."),
   ("abc", "{F} ¿Qué efecto produce «cuenta despacio las horas»?", "Que el tiempo parece pasar muy lento", "Que el tiempo pasa rápido", "Que las horas se terminan", "La palabra «despacio» da una sensación de lentitud."),
   ("abc", "{F} ¿Qué sentimiento transmite el final del poema?", "Alivio y ternura al terminar el turno", "Rabia contra el jefe", "Miedo a la noche", "El sol que «abraza» es una imagen de consuelo."),
   ("ab", "{F} ¿El poema tiene rima?", "No, está escrito en verso libre", "Sí, rima en consonante", "Ningún par de versos termina con sonido final parecido."),
   ("abc", "{F} Una persona dice: «Si no rima, no es poema». ¿Qué le respondes?", "Hay poemas en verso libre que valen por sus imágenes", "Tiene razón, sin rima no hay poema", "Los poemas deben tener siempre rima", "El poema vale por sus imágenes y sentido, no solo por la rima."),
   ("abc", "{F} ¿Cuál sería el sentido global del poema?", "El cansancio del trabajo nocturno y el alivio de la mañana", "La alegría de las vacaciones", "Una discusión entre compañeros", "Las imágenes muestran cansancio y luego alivio."),
   ("ab", "{F} Si el verso final dijera «y me voy a casa», ¿qué se perdería?", "La imagen del sol que abraza y el efecto de alivio", "Nada, porque era un verso literal", "«Me abraza como a un hijo que vuelve» da ternura; sin esa imagen se pierde.")],
  ("abc", "En tu trabajo, un compañero escribe un poema sobre su turno. ¿Cuál es una forma respetuosa de comentarlo?", "Decir qué imagen te gustó y qué te hizo sentir", "Corregirle cada palabra delante de todos", "Burlarte de su trabajo", "Un comentario respetuoso se apoya en lo que el poema logra."),
  [("En Lengua y Literatura: ¿puede un poema no rimar?", "Sí, el verso libre no sigue rima", "Se analiza por sus imágenes y su ritmo."),
   ("¿Qué cuatro partes tiene un párrafo de análisis del poema?", "Figura, cita, significado y efecto", "Con esas cuatro partes el análisis queda completo."),
   ("¿Qué figura es «el sol me abraza»?", "Personificación", "El sol hace una acción humana.")],
  ("Lee el poema: {F} Escribe un párrafo de análisis de cuatro a seis oraciones: elige dos figuras, cita el verso exacto, di qué significan y qué efecto producen, y termina con el sentido global. Si quieres, conecta el poema con un trabajo que conozcas, sin datos personales.",
   "En «La bodega es un mar de cajas» hay una metáfora que muestra un lugar grande y quieto. En «el sol me abraza como a un hijo que vuelve» hay comparación y personificación; produce ternura. El poema muestra el cansancio de la noche y el alivio de la mañana.",
   ["dos figuras con cita exacta", "significado y efecto explicados", "sentido global claro"],
   ["un párrafo de cuatro a seis oraciones"],
   ["no citar el verso", "decir «no rima, entonces no es poema»"],
   "Pregunta: «¿Qué imagen te hace sentir más el cansancio?»."),
  "Escribe tres versos en verso libre sobre cómo termina tu día.",
  "Cambia una metáfora del poema por otra que tú inventes y di qué efecto cambia.")

# ============================================================ clase 6
K(6, MARTILLO + " Pauta de análisis: 1) nombra la figura; 2) cita el verso exacto; 3) explica el significado; 4) explica el efecto en quien lee. "
      "Párrafo X: «El poema habla de un obrero con un martillo». "
      "Párrafo Y: «En ‘Mi martillo es un pájaro de hierro’ hay una metáfora; muestra que el golpe suena como un canto y que el trabajo tiene belleza». "
      "Párrafo Z: «Hay una comparación en ‘pesan como dos sacos de cemento’; el efecto es que sentimos el cansancio como un peso real».",
  "Hoy reviso lo logrado: evalúo análisis de un poema con una pauta, reconozco qué me falta y decido cómo seguir.",
  ["En esta unidad aprendimos a distinguir el sentido literal del figurado, a reconocer comparaciones, metáforas y personificaciones, y a escuchar la rima y el ritmo. Hoy revisamos cuánto se nota ese aprendizaje en un análisis escrito.",
   "Para evaluar un análisis usamos una pauta con cuatro criterios: nombrar la figura, citar el verso exacto, explicar el significado y explicar el efecto en quien lee. Un párrafo que cumple los cuatro es sólido. Uno que solo describe el tema del poema todavía no analiza.",
   "Evaluar es una herramienta para mejorar. Fíjate primero en lo que está bien, después en lo que falta y finalmente en cómo se arregla. Eso sirve para tus propios escritos y para dar opiniones respetuosas sobre el trabajo de otras personas."],
  [("pauta", "lista de criterios para evaluar un trabajo"), ("criterio", "aspecto que se mira para evaluar"), ("sólido", "bien apoyado y completo"), ("retroalimentación", "comentario que ayuda a mejorar")],
  [("Aplicar la pauta al párrafo X", "Párrafo X: «El poema habla de un obrero con un martillo». ¿Cuántos criterios cumple?",
    ["1) No nombra ninguna figura.", "2) No cita un verso.", "3) y 4) No explica significado ni efecto."], "Cumple 0 criterios: solo describe el tema"),
   ("Aplicar la pauta al párrafo Y", "Párrafo Y: nombra la metáfora, cita «Mi martillo es un pájaro de hierro», explica que el golpe suena como un canto y que el trabajo tiene belleza.",
    ["1) Nombra la figura: sí.", "2) Cita el verso: sí.", "3) Explica el significado: sí.", "4) El efecto: dice que el trabajo tiene belleza, pero no cómo lo siente quien lee: parcial."], "Cumple tres criterios y medio")],
  [("Dar por bueno un análisis largo que no cita el verso.", "La cita es una prueba de lo que se afirma.", "Revisa criterio por criterio."),
   ("Decir «le falta todo» sin señalar qué mejorar.", "No ayuda a la persona a avanzar.", "Nombra qué falta y propón cómo agregarlo.")],
  [("abc", "{F} ¿Qué párrafo solo describe de qué trata el poema?", "El X", "El Y", "El Z", "El X no nombra figuras ni explica efectos."),
   ("ab", "{F} ¿Qué figura nombra el párrafo Z?", "Una comparación", "Una personificación", "El párrafo Z dice «hay una comparación en ‘pesan como dos sacos de cemento’»."),
   ("{F} ¿Cuántos criterios tiene la pauta? Escribe el número.", "4", "La pauta del enunciado enumera cuatro criterios numerados."),
   ("abc", "{F} ¿Qué verso del poema usa la palabra «como» para comparar?", "«pesan como dos sacos de cemento»", "«Mi martillo es un pájaro de hierro»", "«que canta clavos en la tarde»", "La comparación necesita «como»; solo este verso la tiene."),
   ("abc", "{F} ¿Qué figura es «Mi martillo es un pájaro de hierro»?", "Metáfora", "Comparación", "Rima asonante", "Dice que el martillo es un pájaro, sin «como»."),
   ("ab", "{F} «Que canta clavos en la tarde» es", "una personificación: el martillo canta", "una descripción literal", "Un martillo no canta, es una imagen figurada."),
   ("abc", "{F} ¿Qué criterio de la pauta cumple el párrafo Y y no cumple el X?", "Nombrar la figura y citar el verso", "Escribir en tercera persona", "Tener más de una oración", "Y nombra la metáfora y cita el verso exacto."),
   ("abc", "{F} ¿Qué efecto produce la comparación «pesan como dos sacos de cemento»?", "Sentimos el cansancio como un peso real", "Sentimos que los hombros son de cemento duro y fuertes", "Sentimos que el trabajo es liviano", "Los sacos de cemento dan idea de mucho peso."),
   ("abc", "{F} ¿Qué falta al párrafo Y para cumplir el cuarto criterio?", "Decir qué siente quien lee ese verso", "Cambiar el título del poema", "Agregar más versos", "El criterio 4 pide explicar el efecto en quien lee."),
   ("ab", "{F} ¿Cuál es una retroalimentación respetuosa para quien escribió el párrafo X?", "«Nombra una figura y cita un verso para completar tu análisis»", "«Esto no sirve para nada»", "Esa respuesta indica qué agregar sin humillar."),
   ("abc", "{F} ¿Qué parte del poema muestra el resultado del trabajo?", "«y la casa, por fin, se levanta»", "«El polvo es una niebla de aserrín»", "«mis hombros»", "El último verso muestra lo logrado con el esfuerzo."),
   ("abc", "{F} ¿Cuál podría ser el sentido global del poema?", "El trabajo cansa pero construye algo valioso", "Un martillo se rompió", "El polvo es peligroso", "Las imágenes muestran esfuerzo y logro."),
   ("ab", "{F} Si el poema dijera «mi martillo es pesado», ¿qué pasaría con el análisis?", "Se perdería la metáfora y habría que analizar menos imágenes", "Habría una nueva metáfora", "Es una descripción literal, sin imagen figurada.")],
  ("abc", "En tu trabajo te piden dar tu opinión sobre el informe de un colega. ¿Qué estrategia usada hoy puedes aplicar?", "Usar una pauta con criterios y decir qué cumple y qué falta", "Decir solo si te gustó o no", "Corregirlo delante de todos", "Una pauta permite opinar con claridad y respeto."),
  [("En Lengua y Literatura: ¿qué criterios tiene la pauta de análisis de poemas?", "Nombrar la figura, citar el verso, explicar el significado y el efecto", "Son los cuatro criterios de la clase."),
   ("¿Para qué sirve evaluar un análisis?", "Para saber qué mejorar", "La evaluación orienta los siguientes pasos."),
   ("¿Qué hago si mi análisis solo describe el tema?", "Agrego figura, cita, significado y efecto", "Así pasa de resumen a análisis.")],
  ("Aplica la pauta: {F} Reescribe el párrafo X de modo que cumpla los cuatro criterios con la estrofa 2 del poema. Después escribe qué criterio te cuesta más y qué harás para practicarlo.",
   "Reescritura: «En ‘pesan como dos sacos de cemento’ hay una comparación. Significa que el cansancio es muy fuerte. Produce en quien lee la sensación de un peso real». Me cuesta explicar el efecto; practicaré diciendo cómo me siento al leer.",
   ["cumple los cuatro criterios", "la cita es exacta", "reflexiona sobre qué le cuesta"],
   ["un párrafo y una reflexión de dos líneas"],
   ["no citar", "no decir qué efecto produce"],
   "Pregunta: «¿Cómo te hace sentir ese verso?»."),
  "Vuelve a leer el poema en voz alta y di qué verso te impactó más.",
  "Escribe un poema de cuatro versos sobre tu trabajo con una metáfora y una comparación.")

"""Material del estudiante de 5.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (viajes de exploración) y OA 02 (conquista de América y Chile)."""
from __future__ import annotations

from hi5_lib import build

OA1 = "HI05 OA 01"
OA2 = "HI05 OA 02"

# ================================================================ OA 01 · VIAJES DE EXPLORACIÓN
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología y rutas, hecha para este cuaderno). Año 1488: el portugués Bartolomé Dias rodea el extremo sur de África. "
     "Año 1492: Cristóbal Colón, al servicio de la Corona de Castilla, navega hacia el oeste y cruza el océano Atlántico hasta una isla de América. "
     "Año 1498: el portugués Vasco da Gama llega a la India navegando hacia el este, alrededor de África. "
     "Años 1519 a 1522: la expedición de Hernando de Magallanes, que murió en 1521, da la primera vuelta al mundo; cruza el Atlántico, pasa por el estrecho que hoy lleva su nombre, en el extremo sur de América, y cruza el océano Pacífico.")
build(
    OA1, 1, F,
    use="Aprenderé a ubicar en el tiempo y en el mapa los viajes de Colón, Magallanes y otro explorador. Sirve para no mezclar fechas, rutas ni personas.",
    prior=["Sé leer una línea de tiempo y restar años.", "Sé que los océanos Atlántico y Pacífico son enormes.", "Sé ubicar el oeste y el este en un mapa."],
    explain=[
        "A fines del siglo XV y comienzos del XVI, marinos de Portugal y de Castilla (hoy parte de España) hicieron viajes de exploración: expediciones por mares poco conocidos para los europeos. Sus objetivos eran llegar a Asia, comerciar y ganar riquezas y poder para sus reyes.",
        "Para ubicar un viaje preguntamos cuándo y por dónde. Bartolomé Dias rodeó el sur de África en 1488. Colón navegó hacia el oeste en 1492 y llegó a una isla de América, aunque creía estar cerca de Asia. Vasco da Gama llegó a la India en 1498 navegando hacia el este, alrededor de África.",
        "La expedición de Magallanes salió en 1519 con cinco naves. Pasó por un estrecho en el sur de América y cruzó el océano Pacífico. Magallanes murió en 1521, y la nave Victoria, al mando de Juan Sebastián Elcano, terminó la vuelta al mundo en 1522. Con una línea de tiempo y un mapa evitamos confundir los viajes.",
    ],
    vocab=[("expedición", "viaje organizado para explorar un lugar, con un objetivo y un jefe"), ("explorador", "persona que viaja a lugares poco conocidos para su sociedad"), ("ruta", "camino que sigue un viaje"), ("estrecho", "paso angosto de mar entre dos tierras"), ("Corona", "el rey o la reina y su gobierno")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre el viaje de Colón y la llegada de Vasco da Gama a la India?", ["Busco los años: Colón 1492 y Da Gama 1498.", "Resto: 1498 − 1492 = 6."], "6 años"),
        ("Ubicar una ruta", "{F} Un mapa muestra una nave que sale de Europa y llega a la India rodeando África. ¿De quién es la ruta?", ["Veo que la ruta bordea África y llega a la India.", "La ficha dice que Vasco da Gama llegó a la India alrededor de África."], "De Vasco da Gama"),
    ],
    mistakes=[("Decir que Colón llegó a la India en 1492.", "Se confunde su viaje con el de Da Gama.", "Colón llegó a una isla de América en 1492; Da Gama llegó a la India en 1498."),
              ("Pensar que Magallanes terminó la vuelta al mundo.", "Se olvida que murió en 1521.", "La expedición terminó en 1522 con Elcano, después de la muerte de Magallanes.")],
    T=[
        ("{F} ¿En qué año llegó Colón a una isla de América?", "1492", "La ficha dice que en 1492 Colón cruzó el Atlántico."),
        ("=", "{F} Colón llegó a América en 1492 y la expedición de Magallanes salió en 1519. ¿Cuántos años pasaron entre ambos hechos?", "1519-1492", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Hacia qué punto cardinal navegó Colón para cruzar el Atlántico?", "hacia el oeste", "La ficha dice que Colón navegó hacia el oeste."),
        ("{F} ¿Qué ocurrió primero: la llegada de Vasco da Gama a la India o la salida de la expedición de Magallanes?", "la llegada de Da Gama a la India", "Da Gama llegó en 1498 y la expedición de Magallanes salió en 1519."),
        ("{F} ¿Qué dos océanos cruzó la expedición de Magallanes?", "el Atlántico y el Pacífico", "La ficha dice que cruzó el Atlántico y el Pacífico."),
        ("Elige la frase correcta. A) Vasco da Gama llegó a la India navegando hacia el este alrededor de África. B) Vasco da Gama llegó a la India navegando hacia el oeste por el Atlántico.", "A", "Da Gama rodeó África y navegó hacia el este."),
        ("=", "{F} ¿Cuántos años duró la expedición de Magallanes, que salió en 1519 y terminó en 1522?", "1522-1519", "Se resta el año de partida al de regreso.", " años"),
        ("Ordena de más antiguo a más reciente: viaje de Magallanes (salida), viaje de Colón, viaje de Dias, viaje de Da Gama.", "Dias, Colón, Da Gama, Magallanes", "Los años son 1488, 1492, 1498 y 1519."),
        ("Un mapa muestra una ruta que sale de Europa, pasa por el extremo sur de América y cruza el océano Pacífico. ¿De qué expedición es esa ruta?", "de la expedición de Magallanes", "Solo Magallanes pasó por el estrecho del sur de América y cruzó el Pacífico."),
        ("{F} Pedro dice: «Colón llegó a la India en 1492, igual que Da Gama». Corrige su error con datos de la ficha.", "Colón llegó a una isla de América en 1492; Da Gama llegó a la India en 1498 por otra ruta", "Hay diferencias de lugar, de año y de ruta."),
        ("{F} Ana dice: «Magallanes terminó la vuelta al mundo en 1522». ¿Es correcto? Usa un dato.", "No, Magallanes murió en 1521; la terminó la nave Victoria al mando de Elcano", "La muerte de Magallanes es anterior al fin del viaje."),
        ("{F} Clasifica cada dato en «tiempo» o «lugar»: a) 1488; b) extremo sur de América; c) 1522; d) sur de África.", "tiempo: a y c; lugar: b y d", "Los años responden cuándo; los sitios responden dónde."),
        ("{F} El mapa A dibuja la ruta de Colón con una flecha hacia el este desde España. El mapa B la dibuja hacia el oeste. ¿Cuál concuerda con la ficha?", "el mapa B", "La ficha dice que Colón navegó hacia el oeste."),
    ],
    ctx=("Un cartel de museo dice: «Ruta de la expedición de Magallanes, 1519–1522». ¿Qué parte del cartel indica el tiempo y cuál la persona?", "Tiempo: 1519–1522. Persona: Magallanes", "Los años dan el tiempo y el apellido señala a la persona."),
    sc=[("En una línea de tiempo, ¿qué viaje va primero: el de Colón (1492) o el de Da Gama (1498)?", "el de Colón", "1492 es anterior a 1498."),
        ("¿Por qué es útil un mapa de rutas al estudiar los viajes de exploración?", "porque muestra por dónde navegó cada expedición y evita confundirlas", "La ruta es un dato de lugar que distingue a cada viaje."),
        ("{F} ¿En qué año terminó la primera vuelta al mundo?", "1522", "La ficha dice que la expedición de Magallanes terminó en 1522.")],
    op=("Dibuja dos cosas. Primero, una línea de tiempo con los años 1488, 1492, 1498 y 1519, y escribe sobre cada año el nombre del explorador de la ficha. Segundo, un mapa simple con Europa, África, América y Asia como manchas; dibuja con flecha la ruta de Colón y la ruta de Magallanes. {F}",
        "Línea con cuatro años y cuatro nombres en orden. Mapa con una flecha desde Europa hacia el oeste hasta América y otra que pasa por el sur de América hacia el Pacífico.",
        ["años en orden correcto", "cada explorador con su año", "dos rutas dibujadas con su dirección"], ["línea de tiempo", "mapa simple con dos flechas"], ["poner a Colón antes de Dias", "dibujar la ruta de Da Gama hacia el oeste"],
        "Pide que explique en voz alta por qué la flecha de Da Gama no cruza el Atlántico hacia América."),
    reinforce="Di en voz alta cada explorador de la ficha con su año y su dirección: oeste o este.",
    extend="Escribe dos preguntas que no puedas responder con esta ficha sobre cómo era un viaje en esa época.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre los viajes (hechas para este cuaderno, a partir de hechos conocidos). Fuente A: el diario de a bordo de Cristóbal Colón; el original se perdió y se conserva un resumen hecho por el fraile Bartolomé de las Casas. "
     "Fuente B: el relato de Antonio Pigafetta, un italiano que viajó con Magallanes y anotó lo que veía durante el viaje. "
     "Fuente C: una carta que Colón escribió en 1493 para contar su viaje al reino. "
     "Fuente D: un mapa de navegación del siglo XV, dibujado por un cartógrafo, con costas y rumbos.")
build(
    OA1, 2, F,
    use="Aprenderé a preguntar quién hizo una fuente, cuándo y para qué. Sirve para saber cuánto podemos creerle y qué nos cuenta de los viajes.",
    prior=["Sé que una fuente es una pista sobre el pasado.", "Sé ubicar los viajes de Colón y de Magallanes en el tiempo."],
    explain=[
        "Sabemos de los viajes de exploración por fuentes: diarios, cartas, relatos y mapas. Una fuente primaria nace en la época que estudiamos, como una carta de Colón. Una fuente secundaria se escribió después, a partir de otras. Hay que preguntar quién la hizo, cuándo y para qué.",
        "El diario de Colón se perdió, y hoy se conoce por un resumen de otra persona. Por eso hay que leerlo con cuidado. La carta de 1493 la escribió el propio Colón para informar al reino, así que cuenta el viaje desde su punto de vista. Pigafetta estuvo en la expedición de Magallanes y anotó lo que vio, pero también tiene su mirada personal.",
        "Un mapa de navegación muestra cómo se conocía el mundo en su época, con sus aciertos y errores. Ninguna de estas fuentes entrega la voz de los pueblos americanos que vieron llegar las naves. Una fuente sola no cuenta toda la historia; por eso se comparan varias.",
    ],
    vocab=[("fuente primaria", "documento o resto hecho en la misma época que se estudia"), ("fuente secundaria", "texto escrito después, a partir de otras fuentes"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("cartógrafo", "persona que dibuja mapas"), ("diario de a bordo", "cuaderno donde el capitán anota lo que ocurre cada día del viaje")],
    worked=[
        ("Preguntar por la procedencia", "{F} ¿Quién escribió la fuente B y qué tiene de especial?", ["Leo en la ficha que la escribió Antonio Pigafetta.", "La ficha dice que viajó con Magallanes y anotó lo que veía."], "Pigafetta, que estuvo en el viaje y lo anotó"),
        ("Reconocer un límite", "{F} ¿La fuente C nos dice qué pensaban los pueblos de América al ver llegar las naves?", ["La fuente C es una carta escrita por Colón.", "Colón cuenta su propia versión, no la de esos pueblos."], "No; solo muestra la versión de Colón"),
    ],
    mistakes=[("Creer que una carta cuenta todo lo ocurrido exactamente.", "Se olvida que quien escribe cuenta su versión.", "Pregunta quién la escribió y para qué."),
              ("Usar un resumen como si fuera el original.", "No se revisa la procedencia.", "Anota que el diario de Colón se conoce por el resumen de otra persona.")],
    T=[
        ("{F} ¿Quién hizo el resumen del diario de Colón?", "el fraile Bartolomé de las Casas", "La ficha lo dice en la fuente A."),
        ("{F} ¿Qué fuente es un mapa?", "la fuente D", "La fuente D es el mapa de navegación."),
        ("{F} ¿De qué nacionalidad era Pigafetta?", "italiano", "La ficha dice que era italiano."),
        ("{F} ¿Qué fuente permite saber lo que Colón quería contar al reino en 1493?", "la fuente C", "Es la carta que Colón escribió en 1493."),
        ("{F} ¿Pigafetta estuvo en el viaje que cuenta o lo supo por otros?", "estuvo en el viaje", "La ficha dice que viajó con Magallanes."),
        ("{F} ¿Por qué se dice que el diario de Colón (fuente A) no se conoce tal como lo escribió él?", "porque el original se perdió y se conoce un resumen", "La ficha lo indica."),
        ("{F} Quieres saber qué costas se conocían en el siglo XV. ¿Qué fuente usas?", "la fuente D", "El mapa muestra costas y rumbos."),
        ("{F} Quieres conocer lo que un tripulante vio día a día en la expedición de Magallanes. ¿Qué fuente usas?", "la fuente B", "Pigafetta anotó lo que veía durante el viaje."),
        ("{F} Une cada fuente con su autor: 1) fuente B; 2) fuente C. a) Colón; b) Pigafetta.", "1 con b; 2 con a", "B es de Pigafetta y C es de Colón."),
        ("{F} Luis dice: «La carta de Colón cuenta con exactitud todo lo que pasó». ¿Qué pregunta de procedencia le falta responder?", "para qué la escribió: para informar al reino y mostrar su versión del viaje", "El propósito del autor limita lo que la carta puede probar."),
        ("{F} Clara dice: «Pigafetta no sirve porque no era el jefe de la expedición». ¿Es buen argumento?", "No, estuvo en el viaje y vio hechos de cerca, aunque cuente con su propia mirada", "Un testigo presente aporta datos, que se usan con cuidado."),
        ("{F} Elige la pregunta que ninguna de las cuatro fuentes puede responder. A) ¿Qué ruta quería hacer Colón? B) ¿Qué pensaban los habitantes de la isla, desde su propia voz, al ver las naves?", "B", "Ninguna fuente de la ficha entrega la voz de los pueblos americanos."),
        ("{F} Quieres comparar lo que Colón escribió al reino con el relato de un tripulante de otra expedición. ¿Qué dos fuentes enfrentas?", "la fuente C con la fuente B", "C es la carta de Colón al reino y B es el relato de Pigafetta, tripulante de Magallanes."),
    ],
    ctx=("Un museo muestra una copia del mapa D con un cartel: «Dibujado por un cartógrafo del siglo XV». ¿Qué datos de procedencia entrega el cartel?", "Quién lo hizo (un cartógrafo) y cuándo (siglo XV)", "El cartel indica autor y época, partes de la procedencia."),
    sc=[("¿Qué tres preguntas forman la procedencia de una fuente?", "quién la hizo, cuándo y para qué", "Con ellas se evalúa cuánto aporta la fuente."),
        ("{F} ¿Cuál es la diferencia entre el diario de Colón y su carta de 1493 en la ficha?", "el diario se conoce por un resumen; la carta la escribió él mismo", "La ficha explica cómo llegó cada fuente."),
        ("Si una fuente no menciona algo, ¿puedo afirmar que no ocurrió?", "no, solo puedo decir que esa fuente no lo cuenta", "La ausencia en una fuente no prueba que algo no ocurrió.")],
    op=("Haz una tabla con las columnas «fuente», «quién la hizo», «para qué sirve» y «qué no nos dice». Completa una fila para la fuente B y otra para la fuente C. {F}",
        "Fuente B: Pigafetta; para saber lo que vio un tripulante; no dice la versión de los pueblos de América. Fuente C: Colón; para conocer su versión del viaje; no dice lo que vivieron los marineros.",
        ["dos filas completas", "usa datos de la ficha", "señala un límite de cada fuente"], ["tabla de cuatro columnas"], ["decir que una fuente lo explica todo", "confundir al autor de B con el de C"],
        "Pregunta cuál fuente le parece más cercana a un tripulante y por qué."),
    reinforce="Nombra las fuentes A, B, C y D y di quién hizo cada una.",
    extend="Escribe cómo contaría tu último fin de semana una persona que estuvo contigo y cómo lo contaría quien no estuvo.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (causas y efectos, hecha para este cuaderno). En Europa del siglo XV, los productos de Asia, como las especias (pimienta y canela), eran muy apreciados y llegaban caros por rutas largas con muchos intermediarios. "
     "Los reyes de Castilla y de Portugal querían riquezas y poder, y esperaban extender la fe cristiana. "
     "Ya se usaban la brújula, que indica la dirección, el astrolabio, que ayuda a saber la posición, y cartas de navegación. Las carabelas eran naves ligeras y fáciles de maniobrar. "
     "Consecuencia: los europeos llegaron a tierras desconocidas para ellos, donde ya vivían pueblos con culturas propias, y empezó un contacto permanente entre Europa y América.")
build(
    OA1, 3, F,
    use="Aprenderé por qué ocurrieron los viajes de exploración, quiénes los hicieron posibles y qué trajeron. Sirve para explicar un hecho histórico con causas y consecuencias.",
    prior=["Sé que un hecho puede tener varias causas.", "Sé quiénes fueron Colón y Magallanes."],
    explain=[
        "Una causa es una razón que ayuda a que algo ocurra. Una consecuencia es lo que pasa después. Los viajes de exploración tuvieron varias causas a la vez. Una fue económica: Europa quería especias y otros productos de Asia, que llegaban caros por rutas largas.",
        "Otra causa fue política y religiosa: los reyes de Castilla y de Portugal buscaban riquezas y poder, y esperaban extender el cristianismo. Una tercera fue tecnológica. La brújula indicaba la dirección, el astrolabio ayudaba a calcular la posición y las carabelas eran ligeras y fáciles de maniobrar. Sin estos avances, cruzar un océano era mucho más peligroso.",
        "Los actores fueron los reyes que financiaron, los capitanes como Colón y Magallanes y las tripulaciones que navegaron. Una consecuencia fue el contacto permanente entre Europa y América, donde ya vivían pueblos con culturas propias. Ese contacto cambió la vida de ambos lados del océano.",
    ],
    vocab=[("causa", "razón que ayuda a que un hecho ocurra"), ("consecuencia", "lo que ocurre después de un hecho y por culpa de él"), ("especias", "productos como pimienta o canela, muy valorados en Europa"), ("brújula", "instrumento con una aguja que indica la dirección"), ("astrolabio", "instrumento para calcular la posición de la nave mirando el cielo")],
    worked=[
        ("Separar causa y consecuencia", "{F} ¿«Querer especias» es causa o consecuencia de los viajes? ¿Y «contacto permanente con América»?", ["Pienso qué ocurre antes: querer especias empuja a viajar.", "El contacto permanente ocurre después de llegar."], "Querer especias es causa; el contacto permanente es consecuencia"),
        ("Relacionar actor y acción", "{F} ¿Quiénes financiaban las expediciones y qué buscaban?", ["La ficha nombra a los reyes de Castilla y de Portugal.", "Buscaban riquezas, poder y extender la fe cristiana."], "Los reyes; buscaban riquezas, poder y extender el cristianismo"),
    ],
    mistakes=[("Decir que los viajes ocurrieron por una sola causa.", "Se busca una explicación simple.", "Nombra al menos una causa económica, una política o religiosa y una tecnológica."),
              ("Decir que las tierras eran «desconocidas» y estaban vacías.", "Se confunde desconocido para los europeos con deshabitado.", "Recuerda que ya vivían pueblos con culturas propias.")],
    T=[
        ("{F} ¿Qué productos de Asia eran muy apreciados en Europa?", "las especias", "La ficha nombra la pimienta y la canela."),
        ("{F} ¿Qué instrumento indicaba la dirección?", "la brújula", "La ficha dice que la brújula indica la dirección."),
        ("{F} ¿Quiénes querían riquezas y poder: los reyes de Castilla y Portugal o los pueblos de América?", "los reyes de Castilla y de Portugal", "La ficha lo atribuye a los reyes."),
        ("{F} Clasifica: a) querer especias; b) comenzó el contacto permanente entre Europa y América. ¿Cuál es causa y cuál consecuencia?", "a causa; b consecuencia", "Querer especias empuja el viaje y el contacto ocurre después."),
        ("{F} ¿Qué ventaja tenía la carabela según la ficha?", "era ligera y fácil de maniobrar", "La ficha describe así a la carabela."),
        ("{F} ¿Cuál de estas es una causa tecnológica: A) la brújula o B) el deseo de poder del rey?", "A", "La brújula es un instrumento; el deseo de poder es político."),
        ("{F} Un rey quiere una ruta propia a Asia porque las especias llegan caras. ¿Qué causa de la ficha explica su interés?", "las especias llegaban caras por rutas largas con muchos intermediarios", "Es la causa económica de la ficha."),
        ("{F} Un piloto quiere calcular la posición de su nave mirando el cielo. ¿Qué instrumento de la ficha le ayuda?", "el astrolabio", "El astrolabio ayuda a saber la posición."),
        ("{F} Ordena la cadena: a) los europeos llegan a tierras desconocidas para ellos; b) los reyes quieren especias y poder; c) comienza el contacto permanente con América.", "b, a, c", "Primero la causa, luego el viaje y al final la consecuencia."),
        ("{F} Marta dice: «Los viajes ocurrieron solo porque a Colón le gustaba navegar». Nombra dos causas de la ficha que la contradicen.", "las especias caras y el deseo de riqueza y poder de los reyes, además de los avances técnicos", "La ficha muestra causas económicas, políticas y tecnológicas."),
        ("{F} Pablo dice: «Eran tierras sin gente, por eso las llamaban desconocidas». Corrige su error.", "Eran desconocidas para los europeos, pero allí ya vivían pueblos con culturas propias", "La ficha lo dice en la consecuencia."),
        ("{F} Clasifica cada elemento como «tecnológico» o «político y económico»: a) brújula; b) deseo de riquezas del rey; c) carabela.", "tecnológico: a y c; político y económico: b", "Los instrumentos y naves son técnicos; el deseo de riqueza es político y económico."),
        ("{F} Eres consejero de un rey. ¿Qué argumento a favor de pagar un viaje usa una causa de la ficha? A) «Habrá una ruta propia a las especias». B) «El mar se ve muy bonito».", "A", "Responde a la causa económica descrita."),
    ],
    ctx=("Un afiche de museo dice: «Gracias a la carabela y a la brújula, las tripulaciones se atrevieron a cruzar el océano». ¿Qué tipo de causa destaca el afiche?", "una causa tecnológica", "Nombra una nave y un instrumento, que son avances técnicos."),
    sc=[("Nombra una causa económica de los viajes de exploración.", "el deseo de conseguir especias y productos de Asia", "Las especias llegaban caras por rutas largas."),
        ("{F} ¿Cuál fue una consecuencia de los viajes según la ficha?", "el contacto permanente entre Europa y América", "Es la consecuencia que la ficha nombra."),
        ("¿Qué hace un astrolabio?", "ayuda a calcular la posición de la nave mirando el cielo", "Era un instrumento de navegación astronómica.")],
    op=("Dibuja una cadena de cuatro recuadros unidos con flechas: «causas» (escribe dos), «actores» (escribe dos), «viaje» (escribe un explorador y su año) y «consecuencia» (escribe una). Usa solo datos de la ficha. {F}",
        "Causas: especias caras y deseo de poder; actores: reyes y capitanes; viaje: Colón 1492; consecuencia: contacto permanente con América.",
        ["dos causas distintas", "dos actores", "una consecuencia", "orden con flechas"], ["cadena de cuatro recuadros"], ["poner una consecuencia como causa", "no nombrar ningún actor"],
        "Pregunta qué cambiaría si no existiera la brújula."),
    reinforce="Repite la diferencia entre causa y consecuencia con un ejemplo de los viajes.",
    extend="Escribe una causa y una consecuencia de un hecho de tu vida, como aprender a andar en bicicleta.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación, hecha para este cuaderno). Colón: salió de Palos, un puerto de España, en 1492 con tres naves; quería llegar a Asia navegando hacia el oeste; llegó a islas de América y creyó haber llegado cerca de Asia. "
     "Magallanes: salió de Sanlúcar, otro puerto de España, en 1519 con cinco naves; quería llegar a las islas de las Especias navegando hacia el oeste; encontró el estrecho del sur de América, cruzó el Pacífico y murió en 1521; la nave Victoria regresó en 1522. "
     "Vasco da Gama: salió de Lisboa, capital de Portugal, en 1497; quería llegar a la India por mar; navegó hacia el este alrededor de África y llegó a la India en 1498.")
build(
    OA1, 4, F,
    use="Aprenderé a comparar los viajes de Colón, Magallanes y Da Gama y a mirar un mismo viaje desde distintos puntos de vista. Sirve para ver parecidos y diferencias.",
    prior=["Sé las fechas y rutas de cada explorador.", "Sé que una causa explica un hecho."],
    explain=[
        "Comparar es buscar parecidos y diferencias con los mismos criterios. Para los tres viajes usaremos estos criterios: de dónde salió, cuántas naves llevaba, qué objetivo tenía, qué ruta siguió y qué resultado tuvo. Con los mismos criterios la comparación es justa.",
        "Colón y Magallanes tenían algo en común: buscaban una ruta hacia Asia navegando hacia el oeste. Se diferencian en el resultado: Colón llegó a América, y Magallanes pasó por un estrecho y cruzó el Pacífico. Da Gama fue distinto: viajó hacia el este, alrededor de África, y llegó a la India.",
        "También se comparan puntos de vista. Para la Corona y los cronistas europeos, los viajes fueron un «descubrimiento». Para los pueblos que ya vivían en América, fue la llegada de extranjeros a sus tierras. Una misma historia se ve distinta según quién la cuenta. Un historiador cuidadoso incluye varias miradas.",
    ],
    vocab=[("comparar", "buscar parecidos y diferencias con los mismos criterios"), ("criterio", "aspecto que se usa para comparar, como la ruta o el objetivo"), ("perspectiva", "punto de vista desde el que alguien mira un hecho"), ("islas de las Especias", "islas de Asia donde se producían muchas especias"), ("descubrimiento", "palabra con que los europeos nombraron la llegada a tierras nuevas para ellos")],
    worked=[
        ("Comparar con un criterio", "{F} Compara el objetivo de Colón con el de Da Gama.", ["Colón quería llegar a Asia navegando hacia el oeste.", "Da Gama quería llegar a la India por mar, y fue hacia el este."], "Ambos buscaban llegar a Asia, pero por rutas opuestas"),
        ("Cambiar de perspectiva", "{F} Un cronista español escribe: «descubrimos nuevas tierras». ¿Desde qué punto de vista habla y qué deja fuera?", ["Habla como europeo de la Corona.", "Deja fuera que en esas tierras ya vivían pueblos."], "Habla como europeo y olvida a los pueblos que ya vivían allí"),
    ],
    mistakes=[("Decir que los tres hicieron exactamente lo mismo.", "Se mira solo el parecido.", "Compara también las diferencias de ruta y resultado."),
              ("Contar los viajes solo desde un punto de vista.", "Se supone que existe una sola versión.", "Pregunta qué diría quien vivía en las tierras a las que llegaron.")],
    T=[
        ("=", "{F} Colón salió con 3 naves y Magallanes con 5. ¿Cuántas naves más llevó Magallanes?", "5-3", "Se resta el número menor al mayor.", " naves"),
        ("{F} ¿Quién bordeó África navegando hacia el este?", "Vasco da Gama", "La ficha lo dice de Da Gama."),
        ("{F} ¿Quién encontró el estrecho del sur de América?", "Magallanes", "La ficha lo atribuye a su expedición."),
        ("{F} ¿Qué objetivo compartían Colón y Magallanes?", "llegar a Asia navegando hacia el oeste", "Ambos buscaban una ruta hacia Asia por el oeste."),
        ("{F} ¿En qué se diferencia el resultado del viaje de Colón del de Magallanes?", "Colón llegó a América y Magallanes cruzó el Pacífico", "La ficha describe resultados distintos."),
        ("{F} ¿Cuál de los tres navegó hacia el este?", "Vasco da Gama", "Los otros dos fueron hacia el oeste."),
        ("=", "{F} Colón salió en 1492 y Da Gama en 1497. ¿Cuántos años después de Colón salió Da Gama?", "1497-1492", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué nave volvió de la expedición de Magallanes, en 1522?", "la nave Victoria", "La ficha lo indica."),
        ("{F} Elige la comparación correcta. A) Colón y Magallanes salieron de puertos de España y Da Gama de Lisboa. B) Colón y Da Gama salieron de España.", "A", "Palos y Sanlúcar están en España; Lisboa está en Portugal."),
        ("{F} Tomás dice: «Los tres viajes fueron iguales». Da una diferencia de ruta con datos de la ficha.", "Da Gama fue hacia el este y los otros dos hacia el oeste", "La dirección distingue las rutas."),
        ("{F} Un cronista español escribe «descubrimos tierras nuevas». ¿Qué olvida esa frase?", "que en esas tierras ya vivían pueblos con culturas propias", "La frase solo muestra la mirada europea."),
        ("{F} Completa con «parecido» o «diferencia»: a) los tres buscaban llegar a Asia por mar; b) Colón terminó en América y Da Gama en la India.", "a: parecido; b: diferencia", "El objetivo es común; el resultado cambia."),
        ("{F} Quieres comparar dos viajes que tomaron la misma dirección. ¿Cuáles eliges?", "los de Colón y Magallanes", "Ambos navegaron hacia el oeste."),
    ],
    ctx=("En una sala de museo hay dos carteles. El A dice: «1492, descubrimiento de América». El B dice: «1492, llegada de extranjeros a tierras habitadas». ¿Qué muestran los dos carteles juntos?", "dos perspectivas distintas sobre el mismo hecho", "Cada cartel mira el hecho desde un grupo diferente."),
    sc=[("Nombra dos criterios para comparar viajes de exploración.", "por ejemplo la ruta y el objetivo", "Son aspectos que se pueden comparar en cada viaje."),
        ("{F} ¿Quién llegó a la India: Magallanes o Da Gama?", "Da Gama", "La ficha lo dice."),
        ("¿Por qué conviene conocer más de una perspectiva?", "porque una misma historia se ve distinta según quién la cuenta", "Así se evita una mirada incompleta.")],
    op=("Completa una tabla con filas «Colón», «Magallanes» y «Da Gama» y columnas «salida», «objetivo», «ruta» y «resultado». Usa solo la ficha. Después escribe una frase que empiece con «Un parecido es…» y otra con «Una diferencia es…». {F}",
        "Colón: España; llegar a Asia; oeste por el Atlántico; llegó a América. Un parecido es que buscaban Asia. Una diferencia es que Da Gama fue hacia el este.",
        ["tabla de 3 filas y 4 columnas completa", "un parecido", "una diferencia"], ["tabla completa", "dos frases"], ["mezclar los datos de dos exploradores", "comparar sin criterios"],
        "Pregunta qué columna fue más fácil de completar y por qué."),
    reinforce="Compara en voz alta a Colón y Da Gama con tres criterios.",
    extend="Escribe qué podría decir una persona que vivía en la isla a la que llegó Colón, usando solo lo que sabemos con seguridad: que ya vivía allí.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (dificultades a bordo, hecha para este cuaderno). En los viajes largos faltaban frutas y verduras frescas. Muchos marineros enfermaban de escorbuto, que causa debilidad y sangrado de las encías, por falta de vitamina C. "
     "La comida se echaba a perder y el agua se ponía mala. Había tormentas y calmas sin viento, y a veces hambre y sed. La tripulación vivía apretada en naves pequeñas. "
     "Por el miedo y el cansancio, a veces los marineros protestaban o se rebelaban contra el capitán. De la expedición de Magallanes, que partió con cinco naves, volvió una sola.")
build(
    OA1, 5, F,
    use="Aprenderé a defender una idea sobre los viajes de exploración con evidencia. Sirve para opinar con razones y no solo con ganas.",
    prior=["Sé las causas de los viajes.", "Sé que una fuente tiene límites."],
    explain=[
        "Argumentar es defender una idea con razones y pruebas. Un buen argumento tiene tres partes: una afirmación (lo que defiendes), una evidencia (el dato que la apoya) y una conclusión (lo que se entiende al unirlas). La evidencia debe estar en una fuente, no en nuestra imaginación.",
        "Los viajes de exploración fueron muy difíciles para las tripulaciones. Faltaban alimentos frescos y muchos marineros enfermaban de escorbuto. Había tormentas, calmas sin viento, hambre y sed, y los barcos eran pequeños y apretados. A veces la tripulación protestaba contra el capitán. En la expedición de Magallanes, de cinco naves volvió una.",
        "Una buena afirmación dice solo lo que la evidencia permite. Con esa ficha podemos decir que el viaje fue duro, pero no cuántos marineros murieron de escorbuto, porque la ficha no da la cifra. Reconocer lo que no sabemos también es parte de argumentar bien.",
    ],
    vocab=[("argumento", "idea defendida con razones y pruebas"), ("evidencia", "dato de una fuente que apoya una afirmación"), ("afirmación", "idea que alguien defiende"), ("escorbuto", "enfermedad por falta de vitamina C, que da debilidad y sangrado de encías"), ("rebelarse", "protestar o actuar contra la autoridad")],
    worked=[
        ("Armar un argumento", "{F} Afirmación: «La expedición de Magallanes fue muy difícil». ¿Qué evidencia la apoya?", ["Busco un dato de la ficha sobre esa expedición.", "La ficha dice que partió con cinco naves y volvió una."], "Partió con cinco naves y volvió una sola"),
        ("Reconocer un límite", "{F} ¿Se puede afirmar con la ficha cuántos marineros murieron de escorbuto?", ["Busco una cifra en la ficha.", "No hay ninguna cifra de muertos."], "No, la ficha no da esa cifra"),
    ],
    mistakes=[("Defender una idea sin dar evidencia.", "Se cree que basta con opinar.", "Agrega un dato de la fuente después de tu afirmación."),
              ("Afirmar más de lo que dice la fuente.", "Se completa con imaginación.", "Di solo lo que la evidencia permite y señala lo que no se sabe.")],
    T=[
        ("{F} ¿Qué enfermedad sufrían muchos marineros?", "el escorbuto", "La ficha lo nombra."),
        ("{F} ¿Qué alimentos faltaban en los viajes largos?", "frutas y verduras frescas", "La ficha lo indica."),
        ("=", "{F} Partieron 5 naves y volvió 1. ¿Cuántas naves no volvieron?", "5-1", "Se resta las que volvieron a las que partieron.", " naves"),
        ("{F} ¿Qué dato muestra que la comida era un problema?", "la comida se echaba a perder", "Es un dato explícito de la ficha."),
        ("{F} ¿Qué problema del clima nombra la ficha además de las tormentas?", "las calmas sin viento", "La ficha menciona tormentas y calmas."),
        ("{F} ¿Qué problema de convivencia a bordo menciona la ficha?", "los marineros protestaban o se rebelaban contra el capitán", "Se debía al miedo y al cansancio."),
        ("{F} Afirmación: «Había problemas de salud a bordo». ¿Qué evidencia de la ficha la apoya?", "muchos marineros enfermaban de escorbuto", "El escorbuto es una enfermedad que afectaba a la tripulación."),
        ("{F} Afirmación: «La expedición de Magallanes tuvo grandes pérdidas». ¿Qué evidencia usarías?", "de cinco naves volvió una sola", "El dato numérico apoya la pérdida."),
        ("{F} ¿Qué afirmación está apoyada por la ficha? A) «Los viajes largos eran siempre cómodos». B) «Los marineros pasaban hambre y sed a veces».", "B", "La ficha dice que había hambre y sed."),
        ("{F} Lucía dice: «Los marineros se rebelaban porque eran flojos». ¿Qué evidencia de la ficha ayuda a explicarlo de otro modo?", "tenían miedo, cansancio, hambre y sed", "La ficha da razones para su protesta."),
        ("{F} Ordena un argumento: a) evidencia: volvió una de cinco naves; b) conclusión: la expedición fue muy dura; c) afirmación: el viaje de Magallanes fue difícil.", "c, a, b", "Primero se afirma, luego se prueba y se concluye."),
        ("{F} Argumento A: «El viaje fue difícil». Argumento B: «El viaje fue difícil, pues muchos enfermaban de escorbuto y volvió una nave de cinco». ¿Cuál es mejor y por qué?", "B, porque incluye evidencia", "Un argumento necesita datos que lo apoyen."),
        ("{F} Alguien afirma: «Murieron cien marineros de escorbuto». ¿Qué falta para sostenerlo?", "una fuente que dé esa cifra, porque la ficha no la entrega", "No se puede afirmar un número sin evidencia."),
    ],
    ctx=("Un compañero dice en clase: «Navegar en esa época era fácil». Usando la ficha, responde con una evidencia.", "Era difícil: faltaban alimentos frescos, había escorbuto, tormentas, hambre y sed", "Los datos de la ficha contradicen su afirmación."),
    sc=[("¿Cuáles son las tres partes de un buen argumento?", "afirmación, evidencia y conclusión", "Así se ordena una idea defendida con pruebas."),
        ("{F} ¿Cuántas naves volvieron de la expedición de Magallanes?", "una", "La ficha dice que volvió una sola."),
        ("¿Por qué es bueno decir qué no sabemos?", "porque evita afirmar cosas que la fuente no prueba", "Un argumento honesto reconoce sus límites.")],
    op=("Escribe un párrafo de cuatro líneas que defienda esta afirmación: «Los viajes de exploración fueron un gran desafío para las tripulaciones». Usa al menos dos datos de la ficha y termina con una frase que empiece con «Con esta ficha no puedo saber…». {F}",
        "Los viajes fueron un gran desafío. Faltaban frutas frescas y había escorbuto. Además, de cinco naves volvió una. Con esta ficha no puedo saber cuántos marineros murieron.",
        ["afirmación clara", "dos datos de la ficha", "un límite reconocido"], ["párrafo escrito"], ["inventar cifras", "no usar ningún dato"],
        "Pide que subraye en su párrafo la afirmación y las evidencias con dos colores."),
    reinforce="Explica en voz alta una afirmación sobre los viajes y la evidencia que la apoya.",
    extend="Escribe un argumento sobre otra afirmación, por ejemplo: «Las tripulaciones necesitaban a un buen capitán». Indica qué evidencia necesitarías buscar.",
)

# ================================================================ OA 02 · CONQUISTA DE AMÉRICA Y CHILE
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología, hecha para este cuaderno). 1492: Colón llega a América. De 1519 a 1521: Hernán Cortés y sus hombres, con aliados indígenas, conquistan el imperio azteca; la capital, Tenochtitlan, cae en 1521. "
     "1532: Francisco Pizarro captura al inca Atahualpa en Cajamarca y empieza la conquista del imperio inca. 1535: Diego de Almagro parte desde el Cusco hacia Chile; vuelve al Perú sin fundar ciudades. "
     "1540: Pedro de Valdivia sale del Cusco hacia Chile. 12 de febrero de 1541: Valdivia funda Santiago. 1553: Valdivia muere en la batalla de Tucapel.")
build(
    OA2, 1, F,
    use="Aprenderé cuándo y dónde ocurrió la conquista de América y de Chile. Sirve para seguir el orden de los hechos y los lugares.",
    prior=["Sé que Colón llegó a América en 1492.", "Sé leer una línea de tiempo.", "Sé que Chile está en el extremo sur de América."],
    explain=[
        "Después de los viajes de exploración, los españoles iniciaron la conquista: tomaron el control de territorios de América y de sus pueblos. Una conquista es la ocupación de un territorio por la fuerza o con alianzas. En unos pocos años cayeron dos grandes imperios.",
        "Hernán Cortés conquistó el imperio azteca entre 1519 y 1521, con la ayuda de aliados indígenas. Francisco Pizarro empezó en 1532 la conquista del imperio inca, que estaba en los Andes. Desde el Perú, los españoles miraron hacia el sur, hacia Chile.",
        "Diego de Almagro salió del Cusco en 1535, recorrió el norte de Chile y volvió al Perú sin fundar ciudades. Pedro de Valdivia salió en 1540 y fundó Santiago el 12 de febrero de 1541. Valdivia murió en 1553 en la batalla de Tucapel. Ubicar las fechas y los lugares permite entender cómo la conquista avanzó desde el norte hacia el sur de América.",
    ],
    vocab=[("conquista", "ocupación de un territorio y de sus pueblos por un poder extranjero"), ("imperio", "Estado muy grande que gobierna muchos pueblos"), ("conquistador", "jefe español que dirigía una expedición de conquista"), ("capital", "ciudad principal donde está el gobierno"), ("aliado", "persona o pueblo que se une a otro para un fin común")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre la salida de Almagro hacia Chile y la fundación de Santiago?", ["Busco los años: 1535 y 1541.", "Resto: 1541 − 1535 = 6."], "6 años"),
        ("Ubicar un hecho", "{F} ¿Desde qué ciudad partieron Almagro y Valdivia?", ["Leo en la ficha que Almagro parte desde el Cusco.", "Leo también que Valdivia sale del Cusco."], "Del Cusco, en el Perú"),
    ],
    mistakes=[("Decir que Almagro fundó Santiago.", "Se confunde a los dos conquistadores de Chile.", "Almagro volvió sin fundar ciudades; Valdivia fundó Santiago en 1541."),
              ("Pensar que Chile fue conquistado antes que México.", "No se mira el orden de los años.", "Compara: México 1519–1521 y Chile desde 1540.")],
    T=[
        ("{F} ¿En qué año fundó Valdivia la ciudad de Santiago?", "1541", "La ficha dice 12 de febrero de 1541."),
        ("=", "{F} Colón llegó a América en 1492 y Santiago se fundó en 1541. ¿Cuántos años pasaron?", "1541-1492", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Desde qué ciudad partieron Almagro y Valdivia hacia Chile?", "del Cusco", "La ficha nombra al Cusco."),
        ("{F} ¿Qué imperio conquistó Hernán Cortés?", "el imperio azteca", "La ficha lo indica."),
        ("{F} ¿Qué ocurrió en 1532?", "Pizarro capturó al inca Atahualpa en Cajamarca", "La ficha lo dice."),
        ("{F} ¿Quién llegó primero a Chile: Almagro o Valdivia?", "Almagro", "Salió en 1535, antes que Valdivia en 1540."),
        ("=", "{F} Santiago se fundó en 1541 y Valdivia murió en 1553. ¿Cuántos años vivió Valdivia después de fundar la ciudad?", "1553-1541", "Se resta el año de fundación al de la muerte.", " años"),
        ("Ordena de más antiguo a más reciente: fundación de Santiago, captura de Atahualpa, caída de Tenochtitlan, salida de Almagro hacia Chile.", "caída de Tenochtitlan, captura de Atahualpa, salida de Almagro, fundación de Santiago", "Los años son 1521, 1532, 1535 y 1541."),
        ("{F} Un mapa muestra una flecha que baja desde el Cusco hasta el lugar donde se fundó Santiago en 1541. ¿De quién podría ser esa ruta?", "de Pedro de Valdivia", "Valdivia salió del Cusco y fundó Santiago en 1541."),
        ("{F} Rosa dice: «Almagro fundó Santiago en 1541». ¿Qué dato de la ficha la contradice?", "Almagro volvió al Perú sin fundar ciudades y Santiago la fundó Valdivia", "La ficha atribuye la fundación a Valdivia."),
        ("{F} Ana dice: «Chile se conquistó antes que México». Usa años para corregirla.", "México se conquistó entre 1519 y 1521 y la expedición de Valdivia salió en 1540", "Las fechas muestran el orden contrario."),
        ("{F} Clasifica en «tiempo» o «lugar»: a) 1535; b) Cajamarca; c) Cusco; d) 1553.", "tiempo: a y d; lugar: b y c", "Los años responden cuándo; los nombres de ciudades responden dónde."),
        ("{F} ¿Qué conquista de la ficha ocurrió más al sur: la de Cortés, la de Pizarro o la de Valdivia?", "la de Valdivia en Chile", "Chile está mucho más al sur que México y el Perú."),
    ],
    ctx=("Un cartel de museo dice: «Fundación de Santiago, 12 de febrero de 1541». ¿Qué parte indica el lugar y cuál el tiempo?", "Lugar: Santiago. Tiempo: 12 de febrero de 1541", "El nombre de la ciudad es el lugar y la fecha es el tiempo."),
    sc=[("{F} ¿Quién conquistó el imperio inca empezando en 1532?", "Francisco Pizarro", "La ficha dice que capturó a Atahualpa."),
        ("¿Qué es una conquista?", "la ocupación de un territorio y de sus pueblos por un poder extranjero", "Así se define en esta clase."),
        ("{F} ¿Dónde murió Valdivia?", "en la batalla de Tucapel", "La ficha lo indica.")],
    op=("Dibuja una línea de tiempo con los años 1492, 1521, 1532, 1535, 1541 y 1553, y escribe un hecho de la ficha en cada uno. Luego dibuja un mapa simple de América con tres puntos: México, el Cusco y Santiago. Une el Cusco con Santiago con una flecha. {F}",
        "1521: cae Tenochtitlan; 1541: Valdivia funda Santiago. En el mapa, México arriba, el Cusco en medio y Santiago más al sur.",
        ["seis años en orden", "un hecho correcto en cada año", "tres lugares en orden de norte a sur"], ["línea de tiempo", "mapa simple"], ["poner Santiago entre México y el Cusco", "cambiar el orden de los años"],
        "Pide que explique por qué la flecha va hacia el sur."),
    reinforce="Cuenta en voz alta cinco hechos de la ficha en orden, con su año.",
    extend="Calcula cuántos años pasaron entre la caída de Tenochtitlan y la fundación de Santiago.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre la conquista de Chile (hechas para este cuaderno, a partir de hechos conocidos). Fuente A: una carta de Pedro de Valdivia al emperador Carlos V, escrita en los años 1540, donde cuenta lo que hizo y pide más soldados, caballos y ayuda. "
     "Fuente B: el poema La Araucana, escrito en el siglo XVI por Alonso de Ercilla, un soldado español que estuvo en Chile; cuenta la guerra contra los mapuches y admira su valentía. "
     "Fuente C: el libro de actas del cabildo de Santiago, donde los vecinos anotaban sus decisiones desde 1541. "
     "Fuente D: una historia contada de generación en generación por familias mapuche sobre la llegada de los españoles.")
build(
    OA2, 2, F,
    use="Aprenderé a preguntar quién, cuándo y para qué se hizo cada fuente sobre la conquista de Chile. Sirve para entender qué voz escuchamos y cuál falta.",
    prior=["Sé que una fuente es una pista del pasado.", "Sé quiénes eran Valdivia y Almagro."],
    explain=[
        "Para conocer la conquista de Chile usamos varias fuentes. La carta de Valdivia es una fuente primaria escrita por un conquistador. Él quería convencer al emperador de que ayudara, así que muestra sus logros y sus necesidades. Lo que cuenta es su versión.",
        "La Araucana la escribió Alonso de Ercilla, un soldado que estuvo en Chile. Su mirada es la de un español, pero describe con admiración la valentía de los mapuches. Es un poema, así que mezcla hechos con arte y emoción. El libro de actas del cabildo muestra decisiones concretas de los vecinos de Santiago, como repartir terrenos o nombrar autoridades.",
        "Las historias que las familias mapuche cuentan de generación en generación entregan la mirada de quienes vieron llegar a los españoles. Cada fuente da una parte. Si solo usamos las españolas, falta una voz. Una buena historia compara fuentes y dice cuándo una fuente no alcanza.",
    ],
    vocab=[("cabildo", "gobierno de una ciudad colonial, formado por alcaldes y regidores"), ("acta", "texto donde se anotan las decisiones de una reunión"), ("carta", "texto escrito para informar o pedir algo a una persona"), ("tradición oral", "historia que se transmite hablando, de una generación a otra"), ("emperador", "gobernante de un imperio; Carlos V gobernaba España")],
    worked=[
        ("Procedencia de una fuente", "{F} ¿Quién escribió la fuente A y para qué?", ["Leo que la escribió Pedro de Valdivia al emperador Carlos V.", "La ficha dice que cuenta lo que hizo y pide ayuda."], "Valdivia; para informar y pedir ayuda"),
        ("Reconocer una voz ausente", "{F} ¿Qué voz aparece solo en la fuente D?", ["Reviso quién habla en cada fuente.", "En D hablan las familias mapuche; en las otras, personas españolas."], "La voz de familias mapuche"),
    ],
    mistakes=[("Creer que la carta de Valdivia cuenta toda la verdad.", "Se olvida que quería pedir ayuda al emperador.", "Pregunta para qué escribió y qué resalta."),
              ("Dejar fuera las voces indígenas.", "Se usan solo fuentes españolas.", "Incluye la fuente D y di qué aporta.")],
    T=[
        ("{F} ¿Quién escribió La Araucana?", "Alonso de Ercilla", "La ficha lo nombra en la fuente B."),
        ("{F} ¿A quién escribió Valdivia su carta?", "al emperador Carlos V", "La ficha lo indica."),
        ("{F} ¿Qué fuente anotaba las decisiones de los vecinos de Santiago?", "la fuente C", "Es el libro de actas del cabildo."),
        ("{F} ¿Qué pedía Valdivia al emperador en su carta?", "más soldados, caballos y ayuda", "La ficha lo dice."),
        ("{F} ¿Qué fuente es un poema?", "la fuente B", "La Araucana es un poema."),
        ("{F} ¿Qué fuente reúne historias contadas por familias mapuche?", "la fuente D", "Es la historia de generación en generación."),
        ("{F} Quieres saber qué terrenos se repartieron los primeros vecinos de Santiago. ¿Qué fuente buscas?", "la fuente C", "El cabildo anotaba decisiones como esa."),
        ("{F} Quieres conocer cómo vieron los mapuches la llegada de los españoles. ¿Qué fuente usas?", "la fuente D", "Trae la versión de familias mapuche."),
        ("{F} Une cada fuente con quién la hizo: 1) fuente A; 2) fuente B. a) un soldado que escribió un poema; b) un jefe de la conquista que escribió una carta.", "1 con b; 2 con a", "Valdivia dirigió la conquista y escribió una carta; Ercilla fue soldado y escribió un poema."),
        ("{F} Luis dice: «La carta de Valdivia es neutral». ¿Qué dato de la ficha lo contradice?", "pedía ayuda al emperador, así que mostraba sus logros", "Quien pide ayuda resalta lo que le conviene."),
        ("{F} Ana dice: «Como Ercilla admira a los mapuches, su poema es la voz mapuche». ¿Es correcto?", "No, es un soldado español que cuenta con su mirada", "Su admiración no cambia que habla desde la mirada española."),
        ("{F} Elige la pregunta que las fuentes A, B y C no responden bien. A) ¿Qué pedía Valdivia? B) ¿Cómo vivieron los mapuches la llegada de los españoles, según ellos mismos?", "B", "Solo la fuente D recoge esa voz."),
        ("{F} Para comparar la mirada de un conquistador con la de una familia mapuche, ¿qué dos fuentes enfrentas?", "la fuente A con la fuente D", "Una es de Valdivia y la otra de familias mapuche."),
    ],
    ctx=("En un museo, un cartel dice: «Copia del libro de actas del cabildo de Santiago, siglo XVI». ¿Qué te dice el cartel de su procedencia y qué le falta?", "dice qué es y de qué época; falta saber quién lo escribió y para qué", "La procedencia tiene tres preguntas y el cartel responde solo una parte."),
    sc=[("¿Qué tres preguntas hacemos a una fuente?", "quién la hizo, cuándo y para qué", "Con ellas medimos lo que la fuente aporta."),
        ("{F} ¿Qué es el cabildo?", "el gobierno de una ciudad colonial, con alcaldes y regidores", "El libro de actas guarda sus decisiones."),
        ("¿Por qué se comparan varias fuentes?", "porque cada una muestra solo una parte de lo ocurrido", "Así se completa la mirada.")],
    op=("Haz una tabla con las fuentes A y D. En las columnas escribe «quién habla», «para qué», «qué aporta» y «qué no dice». {F}",
        "A: Valdivia; pedir ayuda; sus logros y necesidades; no dice la versión mapuche. D: familias mapuche; transmitir su historia; su mirada de la llegada; no dice los planes de Valdivia.",
        ["dos filas completas", "usa datos de la ficha", "señala un límite de cada fuente"], ["tabla de cuatro columnas"], ["decir que A es neutral", "mezclar los autores"],
        "Pregunta qué otra voz falta y pídele que la nombre sin inventar datos."),
    reinforce="Nombra las cuatro fuentes y di quién habla en cada una.",
    extend="Escribe cómo describirían un partido de fútbol el árbitro, un hincha y un jugador, y por qué sus versiones se parecen y se diferencian.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (actores, hecha para este cuaderno). La Corona española autorizaba las expediciones por medio de un contrato, la capitulación, y recibía una parte de las riquezas, el quinto real, que era la quinta parte. "
     "Los conquistadores, como Valdivia, reunían soldados, caballos y dinero, y esperaban tierras y honores. La Iglesia católica envió frailes y sacerdotes que buscaban convertir a los indígenas al cristianismo. "
     "Las mujeres también participaron: Inés de Suárez viajó con Valdivia a Chile y ayudó en la defensa de Santiago en 1541. Los pueblos indígenas resistieron o se aliaron con los españoles según sus intereses. "
     "Consecuencia: se fundaron ciudades como Santiago (1541), Concepción (1550) y Valdivia (1552), y poco a poco se formó una nueva sociedad con españoles, indígenas y mestizos.")
build(
    OA2, 3, F,
    use="Aprenderé quiénes participaron en la conquista, qué buscaba cada uno y qué resultó. Sirve para explicar la conquista con actores, causas y consecuencias.",
    prior=["Sé que la conquista de Chile partió desde el Perú.", "Sé distinguir causa y consecuencia."],
    explain=[
        "En la conquista participaron varios actores. La Corona española daba permiso para explorar y conquistar y recibía el quinto real, la quinta parte de las riquezas. Los conquistadores reunían soldados, caballos y dinero, y esperaban tierras y honores a cambio.",
        "La Iglesia católica envió frailes y sacerdotes que buscaban convertir a los indígenas al cristianismo. Las mujeres también tuvieron un papel: Inés de Suárez viajó con Valdivia y ayudó en la defensa de Santiago en 1541. Los pueblos indígenas no fueron espectadores: algunos resistieron y otros se aliaron con los españoles según sus intereses.",
        "Una consecuencia importante fue la fundación de ciudades, como Santiago, Concepción y Valdivia, que muestran la voluntad de los españoles de quedarse y expandirse. Con el tiempo se formó una nueva sociedad con españoles, indígenas y mestizos, es decir, hijos de españoles e indígenas.",
    ],
    vocab=[("capitulación", "contrato con que la Corona autorizaba una expedición de conquista"), ("quinto real", "la quinta parte de las riquezas, que correspondía a la Corona"), ("Iglesia católica", "institución religiosa cristiana que envió misioneros a América"), ("mestizo", "hijo o hija de español e indígena"), ("actor histórico", "persona o grupo que participa en un hecho")],
    worked=[
        ("Calcular el quinto real", "{F} Una expedición reúne 100 monedas de oro. ¿Cuántas corresponden al quinto real?", ["El quinto real es la quinta parte.", "Divido: 100 ÷ 5 = 20."], "20 monedas"),
        ("Relacionar actor y acción", "{F} ¿Qué buscaba la Iglesia católica en la conquista?", ["Leo qué dice la ficha de la Iglesia.", "Envió frailes y sacerdotes para convertir a los indígenas."], "Convertir a los indígenas al cristianismo"),
    ],
    mistakes=[("Decir que Valdivia conquistó Chile solo.", "Se olvidan los otros actores.", "Nombra la Corona, la Iglesia, los soldados, las mujeres y los pueblos indígenas."),
              ("Decir que los indígenas no hicieron nada.", "Se supone que solo actuaron los españoles.", "Recuerda que algunos resistieron y otros se aliaron.")],
    T=[
        ("{F} ¿Qué autorizaba las expediciones: la capitulación o el cabildo?", "la capitulación", "La ficha dice que la Corona daba el contrato llamado capitulación."),
        ("{F} ¿Quién viajó con Valdivia y ayudó en la defensa de Santiago?", "Inés de Suárez", "La ficha la nombra."),
        ("=", "{F} Una expedición reúne 200 monedas de plata. ¿Cuántas corresponden al quinto real?", "200//5", "El quinto es la quinta parte, es decir, se divide por cinco.", " monedas"),
        ("{F} ¿Qué esperaban los conquistadores a cambio de su esfuerzo?", "tierras y honores", "La ficha lo dice."),
        ("{F} ¿Qué buscaban los frailes y sacerdotes?", "convertir a los indígenas al cristianismo", "Es el objetivo de la Iglesia en la ficha."),
        ("{F} ¿Cuál fue una consecuencia de la conquista: A) se fundaron ciudades o B) se firmó una capitulación?", "A", "La capitulación fue antes de la expedición; las ciudades vinieron después."),
        ("{F} Une cada actor con su acción: 1) la Corona; 2) los conquistadores. a) reunían soldados y caballos; b) daba permiso y recibía el quinto real.", "1 con b; 2 con a", "La ficha asigna esas acciones."),
        ("{F} ¿Qué ciudad se fundó antes: Concepción (1550) o Valdivia (1552)?", "Concepción", "1550 es anterior a 1552."),
        ("{F} ¿Qué sociedad nueva se formó con el tiempo?", "una con españoles, indígenas y mestizos", "La ficha lo indica."),
        ("{F} Juan dice: «Valdivia conquistó Chile sin ayuda de nadie». Nombra dos actores de la ficha que lo contradicen.", "la Corona y la Iglesia, o Inés de Suárez y los soldados", "La ficha muestra muchos actores."),
        ("{F} Sofía dice: «Los indígenas solo miraban cómo llegaban los españoles». Corrígela con un dato.", "Algunos resistieron y otros se aliaron con los españoles según sus intereses", "Los pueblos indígenas tomaron decisiones."),
        ("{F} Clasifica cada hecho como «causa» o «consecuencia» de la fundación de ciudades: a) los españoles querían quedarse; b) nació una sociedad mestiza.", "a: causa; b: consecuencia", "El deseo de quedarse impulsa fundar ciudades y la mezcla ocurre después."),
        ("{F} Un conquistador dice: «Si hallo oro, daré a la Corona el quinto». Si halla 150 monedas, ¿cuántas entrega y cuántas se queda?", "entrega 30 y se queda 120", "El quinto de 150 es 30 y quedan 150 − 30 = 120."),
    ],
    ctx=("Un cartel de museo muestra un grabado con un fraile, un soldado, una mujer y un cacique frente a una nueva ciudad. ¿Qué actores de la ficha representa, uno por figura?", "la Iglesia, los conquistadores, las mujeres como Inés de Suárez y los pueblos indígenas", "Cada figura corresponde a un actor de la ficha."),
    sc=[("¿Qué es el quinto real?", "la quinta parte de las riquezas, que correspondía a la Corona", "Así lo define la ficha."),
        ("{F} ¿Qué ciudades fundaron los españoles según la ficha?", "Santiago, Concepción y Valdivia", "La ficha nombra esas tres."),
        ("¿Qué es un mestizo?", "un hijo o hija de español e indígena", "Es el significado del término.")],
    op=("Haz un esquema con el título «Conquista de Chile». Dibuja cuatro recuadros: «Corona», «Conquistadores», «Iglesia» y «Pueblos indígenas». En cada uno escribe qué hacía o buscaba, según la ficha. Abajo, un quinto recuadro: «Consecuencia». {F}",
        "Corona: autorizaba y recibía el quinto real. Conquistadores: reunían soldados y buscaban tierras. Iglesia: convertir. Pueblos indígenas: resistieron o se aliaron. Consecuencia: ciudades y nueva sociedad.",
        ["cuatro actores", "una acción por actor", "una consecuencia"], ["esquema de cinco recuadros"], ["no incluir a los pueblos indígenas", "poner la consecuencia como acción de un actor"],
        "Pregunta qué actor te parece que decidió más y pídele una razón con un dato."),
    reinforce="Nombra cuatro actores de la conquista y lo que buscaba cada uno.",
    extend="Calcula el quinto real de 350 monedas y explica cómo lo hiciste.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación, hecha para este cuaderno). Diego de Almagro, entre 1535 y 1537: salió del Cusco con soldados, cruzó la cordillera con grandes dificultades, recorrió parte de Chile, no encontró las riquezas que esperaba y volvió al Perú sin fundar ciudades. "
     "Pedro de Valdivia, entre 1540 y 1553: salió del Cusco, llegó al valle del Mapocho, fundó Santiago en 1541, y después otras ciudades; repartió tierras a sus soldados y se quedó a vivir en Chile. "
     "Un cronista español escribió que la ciudad se fundaba «para servir a Dios y al rey». Para los pueblos indígenas que vivían en la zona, la fundación de una ciudad significaba la llegada de extranjeros que ocupaban sus tierras.")
build(
    OA2, 4, F,
    use="Aprenderé a comparar las expediciones de Almagro y de Valdivia y a mirar la fundación de una ciudad desde dos perspectivas. Sirve para entender por qué una expedición dejó huella y otra no.",
    prior=["Sé quiénes eran Almagro y Valdivia.", "Sé comparar con criterios."],
    explain=[
        "Almagro y Valdivia salieron del Cusco hacia Chile, pero sus resultados fueron muy distintos. Compararemos con estos criterios: cuándo viajaron, qué esperaban, qué hicieron y qué dejaron. Almagro recorrió parte del territorio, no halló las riquezas que esperaba y volvió al Perú sin fundar ciudades.",
        "Valdivia llegó al valle del Mapocho, fundó Santiago en 1541 y después otras ciudades. Repartió tierras a sus soldados y se quedó. Fundar una ciudad era una forma de ocupar el territorio de manera permanente. Por eso su expedición tuvo efectos más duraderos que la de Almagro.",
        "Una misma fundación se ve distinto según quién la mire. Un cronista español la describía como un servicio a Dios y al rey. Para los pueblos indígenas del lugar, significaba la llegada de extranjeros que ocupaban sus tierras. Cuando comparamos perspectivas, entendemos mejor el hecho.",
    ],
    vocab=[("perspectiva", "punto de vista de un grupo sobre un hecho"), ("cronista", "persona que escribe sobre los hechos de su tiempo"), ("fundar", "crear una ciudad con autoridades y terrenos repartidos"), ("repartir tierras", "dar terrenos a los soldados o vecinos como premio"), ("duradero", "que permanece mucho tiempo")],
    worked=[
        ("Comparar dos expediciones", "{F} ¿En qué se diferencian los resultados de Almagro y de Valdivia?", ["Almagro volvió al Perú sin fundar ciudades.", "Valdivia fundó Santiago y se quedó."], "Almagro no dejó ciudades; Valdivia sí"),
        ("Comparar perspectivas", "{F} ¿Qué significaba fundar una ciudad para el cronista español y para los pueblos indígenas?", ["Para el cronista era servir a Dios y al rey.", "Para los pueblos indígenas era la llegada de extranjeros que ocupaban sus tierras."], "Para el cronista, un servicio; para los indígenas, ocupación de sus tierras"),
    ],
    mistakes=[("Decir que Almagro y Valdivia hicieron lo mismo.", "Se mira solo que salieron del Cusco.", "Compara resultados: uno fundó ciudades y el otro no."),
              ("Aceptar solo la mirada del cronista.", "Se piensa que hay una versión oficial.", "Agrega qué significaba para los pueblos indígenas.")],
    T=[
        ("{F} ¿Quién fundó Santiago: Almagro o Valdivia?", "Valdivia", "La ficha lo atribuye a Valdivia."),
        ("{F} ¿Quién volvió al Perú sin fundar ciudades?", "Almagro", "Lo dice la ficha."),
        ("{F} ¿Desde qué ciudad salieron ambos conquistadores?", "desde el Cusco", "Ambos partieron de allí."),
        ("{F} ¿Qué repartió Valdivia a sus soldados?", "tierras", "La ficha lo indica."),
        ("{F} ¿Qué parecido tienen las dos expediciones?", "las dos salieron del Cusco hacia Chile", "Es el dato común."),
        ("{F} ¿Qué esperaba encontrar Almagro y no halló?", "riquezas", "La ficha dice que no encontró las riquezas que esperaba."),
        ("=", "{F} Almagro salió en 1535 y Valdivia en 1540. ¿Cuántos años después salió Valdivia?", "1540-1535", "Se resta el año menor al mayor.", " años"),
        ("{F} Elige la comparación correcta. A) Valdivia se quedó a vivir en Chile y Almagro volvió al Perú. B) Almagro se quedó en Chile y Valdivia volvió al Perú.", "A", "La ficha dice que Valdivia se quedó."),
        ("{F} ¿Qué cronista escribió «para servir a Dios y al rey» y qué punto de vista tenía?", "un cronista español; el de los españoles", "Es la mirada de quien fundaba la ciudad."),
        ("{F} Pablo dice: «Almagro y Valdivia tuvieron el mismo resultado». Da dos diferencias.", "Valdivia fundó ciudades y se quedó; Almagro volvió sin fundar ciudades", "Son resultados distintos."),
        ("{F} Explica por qué la expedición de Valdivia dejó más huella que la de Almagro.", "porque fundó ciudades y se quedó, ocupando el territorio de manera permanente", "Fundar y quedarse deja efectos duraderos."),
        ("{F} Clasifica cada frase como mirada del «cronista español» o de los «pueblos indígenas»: a) llegaron extranjeros que ocupaban nuestras tierras; b) se fundó la ciudad para servir a Dios y al rey.", "a: pueblos indígenas; b: cronista español", "Cada frase refleja la ficha."),
        ("{F} Un compañero dice que el cronista y los pueblos indígenas dicen lo mismo. ¿Qué dato de la ficha lo contradice?", "para uno era servir a Dios y al rey y para los otros era ocupación de sus tierras", "Las dos perspectivas son distintas."),
    ],
    ctx=("En una exposición hay dos carteles sobre 1541. El A dice: «Se fundó una ciudad». El B dice: «Llegaron extranjeros a ocupar un valle». ¿Qué perspectiva muestra cada uno?", "A, la mirada de los fundadores; B, la mirada de quienes ya vivían allí", "Cada cartel adopta el punto de vista de un grupo."),
    sc=[("{F} ¿Quién se quedó a vivir en Chile: Almagro o Valdivia?", "Valdivia", "La ficha lo dice."),
        ("¿Para qué sirve comparar perspectivas?", "para entender un hecho desde más de un punto de vista", "Un hecho puede significar cosas distintas para cada grupo."),
        ("{F} ¿Cuál era la mirada del cronista español sobre la fundación de la ciudad?", "que se fundaba para servir a Dios y al rey", "Esa frase resume su mirada.")],
    op=("Completa una tabla comparando a Almagro y Valdivia con los criterios «viaje», «qué esperaban», «qué hicieron» y «qué dejaron». Luego escribe dos frases: «Para un cronista español, fundar una ciudad era…» y «Para los pueblos indígenas del lugar, era…». {F}",
        "Almagro: 1535; riquezas; recorrió el territorio; nada permanente. Valdivia: 1540; tierras y honores; fundó ciudades; una ciudad que sigue hasta hoy.",
        ["tabla completa", "dos expediciones comparadas", "dos perspectivas"], ["tabla", "dos frases"], ["mezclar los datos de los dos conquistadores", "dar solo la perspectiva española"],
        "Pregunta cuál criterio explica mejor la diferencia entre ambos."),
    reinforce="Compara en voz alta a Almagro y Valdivia usando tres criterios.",
    extend="Escribe una pregunta que le harías a un historiador para conocer mejor la perspectiva de los pueblos indígenas.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (argumento, hecha para este cuaderno). Afirmación: «Fundar ciudades muestra que los españoles querían quedarse y expandirse en Chile». Datos: "
     "1) Valdivia fundó Santiago en 1541 y luego Concepción en 1550 y Valdivia en 1552. 2) En cada ciudad se formó un cabildo, con alcaldes y regidores, para gobernarla. "
     "3) Se repartieron solares y tierras a los vecinos. 4) Almagro, que no fundó ciudades, volvió al Perú. 5) Los conquistadores pedían a la Corona más soldados y colonos para seguir avanzando.")
build(
    OA2, 5, F,
    use="Aprenderé a defender, con datos, que fundar ciudades expresó la voluntad de los españoles de quedarse y expandirse. Sirve para argumentar con evidencia.",
    prior=["Sé qué es una afirmación, una evidencia y una conclusión.", "Sé quiénes fueron Almagro y Valdivia."],
    explain=[
        "Un argumento histórico une una afirmación con evidencia. La afirmación de hoy es: fundar ciudades muestra que los españoles querían quedarse y expandirse en Chile. Para defenderla necesitamos datos, no solo opiniones.",
        "Primera evidencia: Valdivia fundó varias ciudades, Santiago en 1541, Concepción en 1550 y Valdivia en 1552. Segunda: en cada ciudad se formó un cabildo con alcaldes y regidores, es decir, un gobierno propio. Tercera: se repartieron solares y tierras a los vecinos, que se instalaban a vivir. Cuarta: Almagro, que no fundó ciudades, volvió al Perú.",
        "Estos datos permiten concluir que fundar ciudades era una forma de quedarse y de avanzar hacia nuevos territorios. Pero la ficha no dice qué pensaban los pueblos que ya vivían allí. Un buen argumento reconoce lo que sus fuentes no muestran y no afirma más de lo que prueban.",
    ],
    vocab=[("evidencia", "dato de una fuente que apoya una idea"), ("expandirse", "extender el dominio a nuevos territorios"), ("solar", "terreno en una ciudad donde se construye una casa"), ("colono", "persona que viaja a vivir a un territorio nuevo"), ("regidor", "miembro del cabildo que ayudaba a gobernar la ciudad")],
    worked=[
        ("Elegir evidencia", "{F} ¿Qué dato apoya que los españoles querían quedarse?", ["Busco un dato sobre permanecer en el lugar.", "Se repartieron solares y tierras a los vecinos."], "El reparto de solares y tierras a los vecinos"),
        ("Reconocer un límite", "{F} ¿La ficha permite saber qué pensaban los pueblos indígenas de las ciudades?", ["Reviso si hay datos de sus ideas.", "Todos los datos son sobre los españoles."], "No, esa voz no aparece en la ficha"),
    ],
    mistakes=[("Defender la afirmación solo con «porque sí».", "Se confunde opinar con argumentar.", "Agrega al menos dos datos de la ficha."),
              ("Dar por probado lo que piensan los indígenas.", "Se completa la fuente con imaginación.", "Di que la ficha no muestra esa voz.")],
    T=[
        ("{F} ¿En qué año fundó Valdivia la ciudad de Concepción?", "1550", "La ficha lo indica."),
        ("{F} ¿Qué se formó en cada ciudad para gobernarla?", "un cabildo", "El dato 2 lo indica."),
        ("{F} ¿Qué se repartió a los vecinos?", "solares y tierras", "El dato 3 lo dice."),
        ("=", "{F} Entre la fundación de Santiago (1541) y la de Valdivia (1552), ¿cuántos años pasaron?", "1552-1541", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué pedían los conquistadores a la Corona para avanzar?", "más soldados y colonos", "El dato 5 lo dice."),
        ("{F} ¿Quién volvió al Perú sin fundar ciudades?", "Almagro", "El dato 4 lo dice."),
        ("{F} ¿Qué dato apoya que los españoles querían gobernar las ciudades por sí mismos: el dato 2 o el dato 4?", "el dato 2", "El cabildo era un gobierno propio de la ciudad."),
        ("{F} ¿Qué dato apoya la idea de expandirse a nuevos territorios?", "los conquistadores pedían más soldados y colonos para seguir avanzando", "Pedir más gente es preparar nuevos avances."),
        ("{F} Ordena el argumento: a) conclusión: fundar ciudades era una forma de quedarse y avanzar; b) afirmación: fundar ciudades muestra voluntad de quedarse; c) evidencia: se repartieron solares y tierras.", "b, c, a", "Se afirma, se prueba y se concluye."),
        ("{F} Elena dice: «Si Almagro no fundó ciudades, es prueba de que a los españoles no les interesaba Chile». ¿Qué dato lo contradice?", "Valdivia fundó varias ciudades", "Un caso no representa a todos los españoles."),
        ("{F} Mateo dice: «Los pueblos indígenas estaban felices con las ciudades». ¿Qué problema tiene su frase con esta ficha?", "la ficha no dice nada de lo que pensaban los pueblos indígenas", "No se puede afirmar lo que la fuente no muestra."),
        ("{F} Argumento A: «Querían quedarse». Argumento B: «Querían quedarse, pues repartieron solares y formaron cabildos». ¿Cuál es mejor y por qué?", "B, porque usa evidencia", "Aporta datos de la ficha."),
        ("{F} ¿Qué evidencia nueva ayudaría a saber cómo vivieron los pueblos indígenas la fundación de ciudades?", "una fuente escrita o contada por ellos", "Hace falta su propia voz."),
    ],
    ctx=("En una charla escolar, una compañera afirma: «Los españoles no pensaban quedarse en Chile». Usa dos datos de la ficha para responderle.", "Fundaron varias ciudades, formaron cabildos y repartieron solares y tierras", "Esos datos muestran que se instalaban de manera permanente."),
    sc=[("¿Qué tres partes tiene un argumento?", "afirmación, evidencia y conclusión", "Así se ordena la defensa de una idea."),
        ("{F} ¿Cuántas ciudades nombra el dato 1?", "tres", "Nombra Santiago, Concepción y Valdivia."),
        ("¿Por qué conviene decir lo que una ficha no muestra?", "porque evita afirmar más de lo que prueba", "Es parte de argumentar con honestidad.")],
    op=("Escribe un párrafo de cuatro líneas que defienda la afirmación de la ficha. Debe tener la afirmación, dos datos de la ficha y una conclusión, y terminar con una frase que empiece con «La ficha no muestra…». {F}",
        "Fundar ciudades muestra la voluntad de quedarse. Se fundaron Santiago, Concepción y Valdivia, y se repartieron solares. Por eso la conquista buscaba permanecer. La ficha no muestra la opinión de los pueblos indígenas.",
        ["afirmación clara", "dos datos de la ficha", "conclusión", "un límite reconocido"], ["párrafo escrito"], ["inventar datos", "no reconocer ningún límite"],
        "Pide que subraye con colores la afirmación, la evidencia y la conclusión."),
    reinforce="Explica en voz alta dos datos que prueban que los españoles querían quedarse en Chile.",
    extend="Escribe otra afirmación sobre la conquista de Chile y anota qué datos necesitarías buscar para defenderla.",
)

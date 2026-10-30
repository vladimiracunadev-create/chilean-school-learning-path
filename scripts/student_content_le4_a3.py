"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación, OA 03 (repertorio literario amplio).

Todos los textos son originales y breves (cuento folclórico, cuento de autor, fábula, leyenda y poema escritos
para este cuaderno); cada ejercicio trae el texto que necesita. Los textos reales de la tradición los aporta el docente.
"""
from __future__ import annotations

from student_content_le4_a import E, L
from student_lessons import arith

OA3 = "LE04 OA 03"

FOLK = ("Había una vez tres hermanos que vivían al pie de un cerro. El mayor salió a buscar fortuna y en el camino encontró a un anciano. "
        "El anciano le pidió pan, pero el mayor se lo negó. Al día siguiente salió el hermano del medio y también negó el pan. "
        "Por último salió el menor, que partió su pan en dos y compartió con el anciano. El anciano le regaló una flauta que hacía bailar a quien la oyera. "
        "Y colorín colorado, este cuento se ha acabado.")

# ------------------------------------------------------------------ OA 03
L(OA3, 1,
  "Este cuaderno, lápiz y el cuento escrito en esta clase. Este cuento es original de este cuaderno: el docente puede aportar un cuento folclórico real de la tradición.",
  "Aprenderé a reconocer las características de un cuento folclórico y por qué esos cuentos se han contado por mucho tiempo.",
  ["Leo cuentos y reconozco personajes y hechos.", "Sé que un cuento tiene inicio, desarrollo y final."],
  ["Un cuento folclórico es un cuento que pasa de boca en boca durante muchos años. No se sabe quién lo inventó: el autor es anónimo. Cada persona que lo cuenta puede cambiar algunas cosas, por eso existen versiones distintas del mismo cuento. Esa forma de transmitir historias se llama tradición oral.",
   "Estos cuentos suelen tener fórmulas de inicio y de cierre, como «Había una vez» o «Colorín colorado, este cuento se ha acabado». También repiten hechos, a menudo tres veces: tres hermanos, tres pruebas, tres deseos. Muchas veces enseñan valores, como compartir o ser honesto.",
   "Los cuentos folclóricos guardan la memoria cultural de un pueblo: cómo vivía, qué valoraba y qué temía. Al leerlos aumentas tu conocimiento del mundo y tu imaginación. En esta clase leerás un cuento original escrito con las características del género; el docente puede entregarte uno real de tu región."],
  [("género", "tipo de texto literario, como cuento, fábula o poema"), ("tradición oral", "historias que se cuentan de boca en boca"), ("anónimo", "sin autor conocido"), ("versión", "forma distinta de contar el mismo cuento")],
  [("Reconocer la fórmula de inicio", "Lee el cuento: «" + FOLK + "» ¿Con qué fórmula de inicio empieza?", ["Busco las primeras palabras del cuento.", "Veo «Había una vez».", "Es una fórmula típica de los cuentos folclóricos."], "«Había una vez»"),
   ("Detectar la repetición", "En el cuento, el mayor niega el pan, el del medio también y el menor lo comparte. ¿Cuántos hermanos hacen la misma acción y cuál cambia?", ["Cuento a los hermanos que niegan el pan: dos.", "El tercero hace algo distinto: comparte.", "La repetición prepara el cambio final."], "Dos niegan el pan y el menor lo comparte")],
  [("Pensar que el cuento folclórico tiene un autor famoso.", "Se confunde con un cuento de autor.", "Recuerda que es anónimo y pasa por tradición oral."), ("Creer que hay una sola versión correcta.", "Se piensa en el texto como algo fijo.", "Cada narrador puede cambiar detalles sin perder la historia.")],
  ([E("Un cuento folclórico, ¿tiene un autor conocido o es anónimo?", "Es anónimo", "Pasó de boca en boca y no se sabe quién lo inventó."),
    E("¿Cómo se llama contar historias de boca en boca?", "Tradición oral", "Es la forma en que se transmiten los cuentos folclóricos."),
    E("En el cuento de los tres hermanos, ¿cuántos hermanos hay?", "3", "El texto dice «tres hermanos».")],
   [E("¿Qué fórmula de cierre usa el cuento: «Colorín colorado, este cuento se ha acabado» o «Fin de la historia»?", "«Colorín colorado, este cuento se ha acabado»", "Así termina el texto."),
    E("¿Quién compartió su pan con el anciano?", "El hermano menor", "El texto dice que el menor partió su pan en dos."),
    E("¿Qué regaló el anciano al hermano menor?", "Una flauta", "El texto dice que le regaló una flauta que hacía bailar a quien la oyera.")],
   [E("¿Qué valor muestra el hermano menor: compartir o presumir?", "Compartir", "Partió su pan en dos para dárselo al anciano."),
    E("Dos personas cuentan el mismo cuento, pero una dice que eran tres hermanas. ¿Cómo se llama a cada forma de contarlo?", "Versión", "Cada forma distinta de contar el mismo cuento es una versión."),
    arith("Son 3 hermanos y 2 negaron el pan. ¿Cuántos lo compartieron?", "3-2", "Se restan los que negaron el pan del total de hermanos.")],
   [E("¿Por qué crees que el cuento repite tres veces la visita al anciano? (a) Para preparar el contraste con el hermano menor. (b) Porque no tenía más ideas.", "(a)", "Dos hermanos repiten la misma acción y el tercero hace algo distinto: compartir."),
    E("¿Qué sentido tiene que la flauta se la dé el anciano al hermano que compartió?", "Premiar la generosidad", "El texto muestra que compartir tiene una recompensa.")],
   [E("¿Cuántos hermanos del cuento actúan con generosidad con el anciano?", "1", "Solo el menor comparte su pan."),
    E("Otra persona cuenta el mismo cuento, pero cambia la flauta por una guitarra. ¿Sigue siendo el mismo cuento folclórico?", "Sí", "Los cuentos tradicionales cambian detalles al contarse y siguen siendo el mismo cuento.")]),
  [E("En una reunión, una persona mayor cuenta un cuento que aprendió de otras personas de su barrio, y no recuerda quién lo inventó. ¿Qué característica de los cuentos folclóricos muestra esta situación?", "El autor es anónimo", "No se conoce quién lo creó y se transmite por tradición oral.")],
  [E("¿Con qué fórmula suele empezar un cuento folclórico?", "«Había una vez»", "Es la fórmula de inicio más conocida."),
   E("¿Qué hecho se repite tres veces en el cuento de los hermanos?", "La visita al anciano", "Cada hermano se encuentra con el anciano."),
   E("¿Qué guardan los cuentos folclóricos de un pueblo?", "Su memoria cultural", "Muestran lo que valoraba y cómo vivía.")],
  ("Lee este cuento original y completa: «" + FOLK + "» 1) Copia la fórmula de inicio y la de cierre. 2) Escribe qué repite el cuento. 3) Escribe qué valor muestra y por qué. 4) Anota qué cambiarías si lo contaras en otra versión.", "Inicio: «Había una vez». Cierre: «Colorín colorado, este cuento se ha acabado». Se repite la visita al anciano tres veces. Muestra el valor de compartir porque el menor es premiado. En mi versión, la flauta sería un silbato.", ["identifica fórmula de inicio y de cierre", "señala la repetición", "explica un valor con una prueba del texto", "propone un cambio de versión"], ["respuestas escritas a las cuatro preguntas"], ["confundir con cuento de autor", "no apoyar el valor en el texto"], "Cuéntale el cuento a otra persona con tu versión y pregúntale qué cambió."),
  "Pide a una persona mayor de tu casa que te cuente un cuento que le contaron y anota cómo empieza y cómo termina.",
  "Escribe tu propia versión del cuento cambiando el lugar y el objeto mágico, y conserva la repetición de tres hechos.")

L(OA3, 2,
  "Este cuaderno, lápiz y los textos escritos en cada ejercicio (originales de este cuaderno).",
  "Aprenderé a reconocer cómo un autor decide contar un cuento: con qué narrador, qué título y qué orden, y diferenciar cuento, novela e historieta.",
  ["Reconozco las características del cuento folclórico.", "Sé quién narra en una historia."],
  ["Un cuento de autor es un cuento que escribe una persona conocida. Esa persona decide muchas cosas: el título, los personajes, el lugar y quién cuenta la historia. A diferencia de un cuento folclórico, tiene una única versión escrita por su autor.",
   "El narrador es la voz que cuenta la historia. Si dice «yo» y participa en los hechos, es un narrador en primera persona: «Miré el reloj». Si cuenta desde afuera, con «él» o «ella», es un narrador en tercera persona: «Camilo miró el reloj». Cambiar de narrador cambia lo que sabemos: en primera persona conocemos lo que el narrador siente.",
   "Una novela es un relato largo, dividido en capítulos. Una historieta cuenta con dibujos en cuadros llamados viñetas y con globos de diálogo. El cuento, en cambio, es breve y se lee de una vez. Todos son parte de un repertorio amplio de lectura: mientras más géneros conoces, más aprendes del mundo."],
  [("cuento de autor", "cuento escrito por una persona conocida"), ("narrador", "voz que cuenta la historia"), ("viñeta", "cuadro de una historieta, con dibujo y a veces texto"), ("novela", "relato largo dividido en capítulos")],
  [("Identificar el narrador", "Texto: «Miré el reloj. Faltaban dos minutos para el timbre y no encontraba mi cuaderno.» ¿Quién narra?", ["Busco palabras como «yo», «mi» o verbos en primera persona.", "Veo «miré» y «mi cuaderno».", "El narrador participa en los hechos."], "Un narrador en primera persona"),
   ("Cambiar el narrador", "Pasa a tercera persona: «Miré el reloj». Con el personaje Camilo.", ["Cambio «yo» por «Camilo».", "Cambio el verbo a tercera persona: «miró».", "Escribo la oración nueva."], "«Camilo miró el reloj.»")],
  [("Creer que el narrador es siempre el autor.", "Se confunde a quien escribe con quien cuenta.", "El autor inventa un narrador, que puede ser un personaje."), ("Decir que una historieta no es literatura.", "Se piensa que solo valen los textos sin dibujos.", "La historieta cuenta con viñetas y también forma parte del repertorio.")],
  ([E("Un cuento de autor, ¿es anónimo o lo escribe una persona conocida?", "Lo escribe una persona conocida", "Tiene un autor que firma el texto."),
    E("¿Cómo se llama la voz que cuenta la historia?", "Narrador", "El narrador es quien relata los hechos."),
    E("En «Miré el reloj», ¿el narrador habla en primera o en tercera persona?", "En primera persona", "Dice «yo» al narrar: miré.")],
   [E("En «Camilo miró el reloj», ¿el narrador habla en primera o en tercera persona?", "En tercera persona", "Cuenta desde afuera, sobre Camilo."),
    E("¿Cómo se llama cada cuadro de una historieta?", "Viñeta", "Cada cuadro con dibujo es una viñeta."),
    E("¿Qué texto es más largo y está dividido en capítulos: un cuento o una novela?", "Una novela", "La novela es un relato largo con capítulos.")],
   [E("Pasa a primera persona: «Luisa abrió la puerta y vio una caja.»", "Abrí la puerta y vi una caja.", "Se reemplaza a Luisa por el «yo» y los verbos van en primera persona."),
    E("Una historieta tiene 3 viñetas por tira y 4 tiras en una página. ¿Cuántas viñetas hay en la página?", "12", "Se multiplican 3 viñetas por 4 tiras.", "3*4"),
    E("En una historieta, ¿cómo se muestra lo que dice un personaje: con un globo de diálogo o con un capítulo?", "Con un globo de diálogo", "El globo encierra lo que dice el personaje.")],
   [E("Un narrador en primera persona dice: «Tenía miedo.» ¿Qué nos cuenta ese narrador sobre sí mismo?", "Lo que siente", "En primera persona el narrador cuenta lo que siente."),
    E("Un cuento de autor se publica con el mismo texto en todas las ediciones. Un cuento folclórico cambia cuando se cuenta. ¿Cuál tiene versiones distintas?", "El folclórico", "Los cuentos de tradición oral tienen varias versiones.")],
   [E("Texto: «Yo guardé la llave y Marta la buscó toda la tarde.» ¿Qué marca que el narrador participa en la historia?", "«Yo guardé»", "El «yo» muestra primera persona."),
    E("Un título como «La caja que hablaba» fue elegido por el autor. ¿Esa decisión es del autor o de la tradición oral?", "Del autor", "En un cuento de autor, el título lo decide quien lo escribe.")]),
  [E("Quieres contar a tu curso lo que te pasó con tu mascota perdida, usando «yo». ¿Qué narrador usas?", "Primera persona", "Contar con «yo» es narrar en primera persona.")],
  [E("¿Cómo se llama el relato largo con capítulos?", "Novela", "La novela es larga y se divide en capítulos."),
   E("¿Qué lleva una historieta: viñetas o capítulos?", "Viñetas", "Las viñetas son sus cuadros."),
   E("¿Quién decide el título de un cuento de autor?", "El autor", "Lo decide quien lo escribe.")],
  ("Lee: «Faltaban dos minutos para el timbre y Camilo no encontraba su cuaderno. Revisó la mochila, el banco y el estuche.» 1) Escribe quién narra. 2) Reescríbelo en primera persona. 3) Dibuja dos viñetas con un globo cada una que cuenten lo mismo.", "1) Narrador en tercera persona. 2) Faltaban dos minutos para el timbre y yo no encontraba mi cuaderno. Revisé la mochila, el banco y el estuche. 3) Viñeta 1: niño con la mochila abierta, globo «¿Dónde está?». Viñeta 2: niño levantando el estuche, globo «¡Aquí estaba!».", ["identifica el narrador", "cambia correctamente a primera persona", "dibuja viñetas coherentes con globos"], ["texto reescrito", "dos viñetas dibujadas"], ["cambiar solo algunos verbos", "globos que no corresponden"], "Lee ambos textos a otra persona y pregúntale qué cambió al saber lo que Camilo piensa."),
  "Escoge un cuento de autor de tu biblioteca y anota quién narra y el título.",
  "Escribe un párrafo de cuatro oraciones narrado en primera persona y luego reescríbelo en tercera.")

FAB = ("Durante todo el verano, una ardilla presumida se reía todos los días de un pájaro carpintero. «Qué tonto eres —le decía—, golpeando la corteza sin parar. Yo mejor juego entre las ramas.» "
       "El pájaro seguía su trabajo y guardaba semillas en el hueco del tronco. Cuando llegó el invierno, la ardilla no encontró nada que comer. "
       "El pájaro carpintero le ofreció un puñado de semillas y le dijo: «Mañana empieza a juntar las tuyas».")

L(OA3, 3,
  "Este cuaderno, lápiz y la fábula escrita en esta clase (original de este cuaderno).",
  "Aprenderé a leer una fábula, fijarme en lo que hacen los personajes y explicar qué enseña la historia usando datos del texto, sin repetir una moraleja de memoria.",
  ["Reconozco personajes y acciones.", "Sé qué es un cuento y qué es un narrador."],
  ["Una fábula es un relato breve en que los personajes son animales, plantas o cosas que actúan como personas. Esto se llama personificación. Casi siempre hay un problema pequeño y una enseñanza que se desprende de lo que ocurre.",
   "La enseñanza de una fábula se llama moraleja. A veces está escrita al final, pero otras veces el lector debe descubrirla. Para no repetirla de memoria, fíjate en tres cosas: qué quiere cada personaje, qué hace y qué le pasa por eso. La enseñanza debe apoyarse en esas acciones.",
   "Un mismo relato puede enseñar más de una cosa. Por ejemplo, una fábula puede mostrar que conviene prepararse a tiempo y también que ayudar sin reproches es generoso. Lo importante es que cada idea tenga prueba en el texto. Así la fábula te hace pensar, no solo memorizar una frase."],
  [("fábula", "relato breve con personajes animales que actúan como personas y dejan una enseñanza"), ("personificación", "dar rasgos humanos a un animal o cosa"), ("moraleja", "enseñanza de una fábula"), ("conflicto", "problema que enfrentan los personajes")],
  [("Qué quiere y qué hace", "Lee la fábula: «" + FAB + "» ¿Qué hace la ardilla durante el verano y qué hace el pájaro carpintero?", ["La ardilla se ríe del pájaro y juega.", "El pájaro golpea la corteza y guarda semillas.", "Comparo ambas acciones."], "La ardilla juega y se burla; el pájaro trabaja y guarda semillas"),
   ("Apoyar la enseñanza en el texto", "Una lectora dice: «La fábula enseña que hay que prepararse a tiempo». ¿Qué parte del texto la apoya?", ["Busco qué pasa en el invierno.", "La ardilla no encontró qué comer.", "El pájaro, que guardó semillas, sí tenía."], "En invierno la ardilla no tenía comida y el pájaro sí")],
  [("Escribir la moraleja sin explicar qué pasó en el texto.", "Se repite de memoria sin apoyo.", "Explica con las acciones de los personajes."), ("Pensar que solo existe una enseñanza posible.", "Se cree que la fábula es una regla fija.", "Acepta otras ideas si tienen prueba en el texto.")],
  ([E("En una fábula, ¿los personajes suelen ser animales que actúan como personas o personas reales?", "Animales que actúan como personas", "Eso es la personificación."),
    E("¿Cómo se llama la enseñanza de una fábula?", "Moraleja", "Moraleja es la enseñanza que deja el relato."),
    E("En la fábula, ¿quién se reía del pájaro carpintero?", "La ardilla", "El texto dice que la ardilla presumida se reía de él.")],
   [E("¿Qué hacía el pájaro mientras la ardilla se reía?", "Seguía trabajando y guardaba semillas", "El texto dice que seguía su trabajo y guardaba semillas."),
    E("¿Qué pasó cuando llegó el invierno?", "La ardilla no encontró comida", "El texto dice que no encontró nada que comer."),
    E("¿Qué le ofreció el pájaro a la ardilla?", "Un puñado de semillas", "Se lo ofreció y le dio un consejo.")],
   [E("¿Qué le aconsejó el pájaro a la ardilla al final?", "Que empezara a juntar sus semillas al día siguiente", "El pájaro dijo: «Mañana empieza a juntar las tuyas»."),
    E("¿Qué rasgo humano se da a los animales de la fábula: hablar o volar?", "Hablar", "Los animales conversan como personas."),
    E("¿Cuál es el conflicto de la ardilla: no tiene comida en invierno o no sabe trepar?", "No tiene comida en invierno", "El problema aparece cuando llega el invierno.")],
   [E("Un lector dice: «Enseña que ayudar es bueno» y otro: «Enseña que hay que prepararse a tiempo». ¿Ambas ideas pueden tener respaldo en el texto?", "Sí", "El pájaro se preparó y también ayudó a la ardilla."),
    E("¿Qué acción del pájaro apoya la idea «ayudar sin reproches»?", "Le ofreció semillas", "Ofreció semillas a quien se había burlado de él.")],
   [E("Si el pájaro hubiera dicho «Te lo mereces» y no le hubiera dado semillas, ¿habría cambiado lo que enseña la fábula?", "Sí", "Ya no mostraría generosidad, solo la consecuencia de no prepararse."),
    E("¿Qué título da más pistas del conflicto de la fábula: «La ardilla y el invierno» o «Un día de verano»?", "«La ardilla y el invierno»", "Ese título apunta al problema de la ardilla con la estación.")]),
  [E("Un compañero te dice: «La fábula de la ardilla enseña lo mismo que “No dejes para mañana lo que puedes hacer hoy”». ¿Qué acción de la ardilla en el texto apoya esa idea?", "Que no juntó comida en el verano", "No haber juntado comida a tiempo la dejó sin alimento en el invierno.")],
  [E("¿Cómo se llama dar rasgos humanos a un animal?", "Personificación", "Es la personificación."),
   E("¿Dónde busco la prueba de una enseñanza: en las acciones del texto o en el título solamente?", "En las acciones del texto", "Las acciones muestran qué pasa y por qué."),
   E("¿Puede una fábula tener más de una enseñanza?", "Sí, si cada una tiene prueba en el texto", "Una misma historia puede mostrar varias ideas.")],
  ("Lee esta fábula original: «" + FAB + "» 1) Anota qué quiere y qué hace cada personaje. 2) Escribe una enseñanza con tus palabras. 3) Copia una acción del texto que la apoye. 4) Escribe una segunda enseñanza posible, también con prueba del texto.", "1) La ardilla quiere divertirse y se burla; el pájaro trabaja y guarda semillas. 2) Conviene prepararse a tiempo. 3) «La ardilla no encontró nada que comer.» 4) Ayudar aunque se hayan burlado de uno: el pájaro le ofreció semillas.", ["describe lo que quiere y hace cada personaje", "formula una enseñanza propia", "la apoya en el texto", "da una segunda lectura con prueba"], ["cuatro respuestas escritas"], ["repetir un refrán sin pruebas", "una sola enseñanza sin respaldo"], "Compara tu enseñanza con la de otra persona y busquen juntas la frase del texto que sirva de prueba."),
  "Cuenta una fábula que conozcas y explica qué acciones muestran su enseñanza.",
  "Escribe una fábula de 5 oraciones con dos animales y un problema, y pide a otra persona que descubra la enseñanza.")

LEY = ("En el valle de los Sauces, cuentan los abuelos que el cerro Pequeño no siempre fue pequeño. Dicen que antes llegaba hasta las nubes y que daba sombra a todo el valle. "
       "Un invierno, el río se secó y los vecinos pidieron ayuda al cerro. El cerro se inclinó, dejó caer un trozo de su cumbre y de ahí nació la vertiente que hoy alimenta el pueblo. "
       "Por eso, cuando alguien sube al cerro, deja una piedra en el camino, para agradecer el agua.")

L(OA3, 4,
  "Este cuaderno, lápiz y la leyenda escrita en esta clase (original e inventada para este cuaderno; no es una leyenda de ningún pueblo real).",
  "Aprenderé a reconocer una leyenda, qué la diferencia de un mito y por qué está unida a un lugar.",
  ["Reconozco narrador, personajes y ambiente.", "Distingo cuento folclórico y cuento de autor."],
  ["Una leyenda es un relato que nace en un lugar y explica algo de él: por qué un cerro tiene cierta forma, de dónde salió una vertiente o por qué un pueblo tiene un nombre. Mezcla hechos posibles con elementos fantásticos y se transmite oralmente. Por eso está ligada a un territorio.",
   "Un mito es distinto: cuenta cómo se originó el mundo o explica fuerzas de la naturaleza con dioses o seres sobrenaturales. Las leyendas hablan de lugares, personas o hechos particulares; los mitos, del origen y sentido del mundo. Muchas veces los pueblos usan ambos para explicar su territorio.",
   "Para leer una leyenda, busca tres cosas: el lugar que nombra, el hecho fantástico y lo que explica. La leyenda de este cuaderno es inventada para practicar. Las leyendas reales de tu comunidad o de los pueblos originarios pertenecen a quienes las cuentan: lo mejor es conocerlas por personas de ese pueblo o por libros que ellas mismas publican, y tratarlas con respeto."],
  [("leyenda", "relato tradicional que explica algo de un lugar o un hecho, con elementos fantásticos"), ("mito", "relato sobre el origen del mundo o fuerzas de la naturaleza"), ("territorio", "lugar donde vive una comunidad"), ("vertiente", "agua que brota de la tierra")],
  [("Ubicar el lugar", "Lee la leyenda: «" + LEY + "» ¿Qué lugar nombra?", ["Busco nombres de lugares.", "Veo «valle de los Sauces» y «cerro Pequeño».", "Son los lugares unidos a la leyenda."], "El valle de los Sauces y el cerro Pequeño"),
   ("Qué explica", "¿Qué explica la leyenda del cerro?", ["Busco qué cuenta que ocurrió.", "El cerro dejó caer un trozo y nació la vertiente.", "Explica de dónde salió el agua del pueblo."], "De dónde salió la vertiente que alimenta el pueblo")],
  [("Pensar que una leyenda es un cuento cualquiera, sin vínculo con un lugar.", "Se mira solo la historia.", "Fíjate en qué lugar nombra y qué explica de él."), ("Confundir leyenda y mito.", "Ambos tienen elementos fantásticos.", "La leyenda explica un lugar o hecho particular; el mito, el origen del mundo.")],
  ([E("Una leyenda, ¿explica algo de un lugar o es siempre un chiste?", "Explica algo de un lugar", "Está unida a un territorio."),
    E("¿Qué mezcla una leyenda: hechos posibles y elementos fantásticos o solo datos científicos?", "Hechos posibles y elementos fantásticos", "Mezcla ambos tipos de elementos."),
    E("¿Cómo se llama el relato que explica el origen del mundo?", "Mito", "Los mitos hablan del origen del mundo.")],
   [E("En la leyenda, ¿cómo era el cerro antes: pequeño o muy alto?", "Muy alto", "El texto dice que llegaba hasta las nubes."),
    E("¿Qué se secó un invierno?", "El río", "El texto dice que el río se secó."),
    E("¿Qué dejó caer el cerro?", "Un trozo de su cumbre", "De ese trozo nació la vertiente.")],
   [E("¿Qué hacen las personas al subir al cerro, según la leyenda?", "Dejan una piedra en el camino", "Así agradecen el agua."),
    E("¿Qué hecho de la leyenda es fantástico: que el cerro se inclinara o que el río se secara en invierno?", "Que el cerro se inclinara", "Un cerro no se inclina de verdad; un río puede secarse."),
    E("¿Por qué la leyenda está ligada a un territorio?", "Porque explica algo del valle y del cerro", "Habla de un cerro y de una vertiente concretos.")],
   [E("Si el relato contara cómo un ser gigante formó las montañas y los mares al comienzo del mundo, ¿sería más bien leyenda o mito?", "Mito", "Habla del origen del mundo."),
    E("¿La leyenda del cerro Pequeño es una leyenda de un pueblo real o un ejemplo inventado para practicar?", "Un ejemplo inventado", "Así lo indica este cuaderno.")],
   [E("La leyenda dice «Dicen que antes llegaba hasta las nubes». ¿Qué indica la palabra «dicen» sobre la forma en que se transmite la leyenda?", "Que se transmite oralmente", "«Dicen» muestra que pasa de boca en boca."),
    E("Si se cambiara el valle de los Sauces por otro valle cualquiera, ¿la leyenda seguiría unida al mismo territorio?", "No", "La leyenda explica un lugar concreto; si cambia el lugar, cambia su vínculo.")]),
  [E("Imagina que en una comunidad hay un cerro con una historia que cuentan los mayores. ¿Esa historia que explica algo del lugar es más bien una leyenda o un mito?", "Una leyenda", "Explica un lugar particular de la comunidad.")],
  [E("¿Con qué lugar está unida una leyenda?", "Con un territorio", "Explica algo de él."),
   E("Para conocer una leyenda real de un pueblo originario, ¿qué conviene: preguntar a personas de ese pueblo o inventarla?", "Preguntar a personas de ese pueblo", "Son sus relatos y deben conocerse con respeto."),
   E("¿Qué es una vertiente?", "Agua que brota de la tierra", "Así se define en esta clase.")],
  ("Lee esta leyenda original e inventada: «" + LEY + "» 1) Escribe el lugar que nombra. 2) Anota el hecho fantástico. 3) Anota lo que explica. 4) Escribe en dos oraciones cómo contarías una leyenda inventada sobre una laguna o un árbol de tu barrio.", "1) El valle de los Sauces y el cerro Pequeño. 2) El cerro se inclina y deja caer un trozo de su cumbre. 3) De dónde salió la vertiente. 4) Cuentan que la laguna Brillante se formó cuando una nube lloró de alegría. Por eso su agua siempre está tranquila.", ["identifica el lugar", "señala el hecho fantástico", "dice lo que explica", "inventa una leyenda breve ligada a un lugar"], ["cuatro respuestas escritas"], ["no relacionar con un lugar", "confundir con un cuento sin territorio"], "Pregunta a una persona de tu comunidad si conoce una historia sobre un lugar cercano y compárala con tu leyenda inventada."),
  "Pregunta a una persona mayor por una historia sobre un lugar cercano y anota qué lugar nombra y qué explica.",
  "Escribe una leyenda de cinco oraciones sobre una piedra, un árbol o una laguna que invente tu familia, y anota que es inventada.")

POEMA3 = ("La luna sube despacio / y se asoma por el cerro. / Es una moneda blanca / que ha perdido a su dueño. // "
          "El río le canta bajito, / las piedras bostezan, quietas, / y la noche, con su manto, / guarda a todos en silencio.")

L(OA3, 5,
  "Este cuaderno, lápiz y el poema escrito en esta clase (original de este cuaderno).",
  "Aprenderé a reconocer versos y estrofas de un poema y a explicar una imagen verbal que el poema crea.",
  ["Reconozco el cuento y la fábula.", "Sé leer en voz alta con pausas."],
  ["Un poema es un texto literario escrito en versos. Un verso es cada línea del poema. Varios versos juntos forman una estrofa, que se separa de la siguiente por un espacio. Muchos poemas no cuentan una historia con inicio, desarrollo y final: expresan lo que una voz siente o ve.",
   "En los poemas aparecen imágenes verbales: palabras que crean una imagen en la mente. En el poema de esta clase, el verso «Es una moneda blanca» habla de la luna: la compara con una moneda y hace que la veas redonda y brillante. Los poemas pueden rimar o no. Leerlos en voz alta ayuda a escuchar el ritmo.",
   "Para comprender un poema, lee dos veces. La primera vez, solo escúchalo. La segunda, fíjate en las imágenes y pregúntate qué te hacen ver, oír o sentir. Los poemas forman parte del repertorio literario junto con cuentos, fábulas, leyendas y otros textos."],
  [("poema", "texto literario escrito en versos"), ("verso", "cada línea de un poema"), ("estrofa", "grupo de versos separado por un espacio"), ("imagen verbal", "palabras que hacen ver, oír o sentir algo en la mente")],
  [("Contar versos y estrofas", "Un poema tiene dos grupos de cuatro líneas cada uno. ¿Cuántos versos y cuántas estrofas tiene?", ["Cada grupo de líneas es una estrofa: hay 2.", "Cada línea es un verso: 4 + 4.", "Sumo los versos: 8."], "8 versos y 2 estrofas"),
   ("Explicar una imagen", "Lee el poema: «" + POEMA3 + "» (// separa estrofas). En él, «una moneda blanca» describe la luna. ¿Qué te hace ver?", ["La moneda es redonda y brillante.", "La luna llena también lo es.", "Esa palabra crea la imagen de la luna."], "Una luna redonda y brillante como una moneda")],
  [("Contar los versos por oraciones y no por líneas.", "Se confunde verso con oración.", "Cuenta una línea escrita como un verso."), ("Buscar una historia con inicio y final.", "Se espera que sea un cuento.", "Un poema expresa lo que ve o siente una voz.")],
  ([E("En un poema, ¿cada línea se llama verso o capítulo?", "Verso", "Cada línea de un poema es un verso."),
    E("¿Cómo se llama el grupo de versos separado por un espacio?", "Estrofa", "Una estrofa agrupa varios versos."),
    E("En el verso «La luna sube despacio», ¿cuántas palabras hay?", "4", "Las palabras son La, luna, sube y despacio.")],
   [E("Lee: «La luna sube despacio / y se asoma por el cerro. / Es una moneda blanca / que ha perdido a su dueño.» ¿Cuántos versos tiene esta estrofa?", "4", "Hay cuatro líneas separadas por barras."),
    E("En el poema completo, ¿cuántas estrofas hay?", "2", "El texto tiene una estrofa antes de // y otra después."),
    E("¿Con qué objeto se compara la luna?", "Con una moneda blanca", "El tercer verso dice «Es una moneda blanca».")],
   [E("Segunda estrofa: «El río le canta bajito, / las piedras bostezan, quietas, / y la noche, con su manto, / guarda a todos en silencio.» ¿Qué hacen las piedras?", "Bostezan, quietas", "Lo dice el segundo verso de esa estrofa."),
    E("¿Qué hace la noche con su manto?", "Guarda a todos en silencio", "Lo dice el cuarto verso."),
    arith("El poema tiene 2 estrofas de 4 versos cada una. ¿Cuántos versos tiene en total?", "4+4", "Se suman los versos de las dos estrofas.")],
   [E("«El río le canta bajito» ¿Qué sentido nos hace imaginar este verso: vista u oído?", "Oído", "Cantar bajito hace imaginar un sonido suave."),
    E("¿Qué sensación crea «las piedras bostezan, quietas»: calma o prisa?", "Calma", "Bostezar y estar quietas transmiten tranquilidad.")],
   [E("Un lector dice que la luna del poema está triste porque «ha perdido a su dueño». Otro dice que la luna está tranquila porque todo está en silencio. ¿Qué verso apoya la idea de que la noche es tranquila?", "«guarda a todos en silencio»", "El silencio y el cuidado dan calma."),
    E("Si el poema se lee en voz alta, ¿el verso 5 es «El río le canta bajito» o «y se asoma por el cerro»?", "«El río le canta bajito»", "El quinto verso es el primero de la segunda estrofa.")]),
  [E("Quieres escribir un poema de dos estrofas con tres versos cada una. ¿Cuántos versos necesitas?", "6", "Son dos estrofas de tres versos.", "3+3")],
  [E("¿Cómo se llama cada línea de un poema?", "Verso", "Cada línea es un verso."),
   E("¿Cómo se llama un grupo de versos?", "Estrofa", "Varios versos juntos forman una estrofa."),
   E("¿Qué crea una imagen verbal?", "Palabras que hacen ver o sentir algo", "Las palabras hacen que se forme una imagen en la mente.")],
  ("Lee en voz alta este poema original: «" + POEMA3 + "» (las barras / separan versos y // separa estrofas). 1) Escribe cuántos versos y cuántas estrofas tiene. 2) Copia la imagen verbal que más te gustó. 3) Explica en una oración qué te hace ver, oír o sentir.", "1) 8 versos y 2 estrofas. 2) «Es una moneda blanca». 3) Me hace ver una luna redonda y brillante en el cielo.", ["cuenta bien versos y estrofas", "copia una imagen del poema", "explica lo que le hace ver, oír o sentir"], ["respuestas escritas"], ["confundir verso con oración", "elegir una frase sin explicar"], "Lee el poema a otra persona y pregúntale qué imagen le llegó más."),
  "Busca un poema de un libro y anota cuántos versos y estrofas tiene.",
  "Escribe un poema de dos estrofas de tres versos con una imagen que compare algo de tu casa con otro objeto.")

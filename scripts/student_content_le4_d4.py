"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 27 (exposición oral coherente y articulada)."""
from __future__ import annotations

from student_content_le4_d import E, reg
from student_lessons import arith

OA27 = "LE04 OA 27"

# ================================================================ OA 27 · clase 1
reg(
    OA27, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que haga de audiencia.",
    "Aprenderé a decidir sobre qué voy a exponer, cuál es mi idea central y para quién la preparo. Sirve para que mi exposición tenga un rumbo claro y que mi audiencia me entienda.",
    ["Sé conversar sobre un tema con ideas y razones.", "Sé que una idea es una oración que dice algo sobre un tema."],
    [
        "Una exposición oral es cuando una persona explica un tema a un grupo, hablando de manera ordenada. Antes de empezar, conviene aclarar tres cosas. Primero, el tema, que es de lo que voy a hablar, por ejemplo «el reciclaje de papel». Segundo, la idea central, que es lo más importante que quiero que mi audiencia entienda, escrita como una oración: «Reciclar papel en la sala reduce la basura y es fácil de hacer». Tercero, la audiencia, que son las personas que me escucharán.",
        "El tema es corto: una palabra o una frase. La idea central es una oración completa que dice algo sobre el tema. Si no puedo decir mi idea central en una sola oración, todavía no está clara. Conocer a la audiencia ayuda a elegir las palabras y los ejemplos: no hablamos igual a niños de primero básico que a adultos de la familia.",
        "También pensamos en el propósito, que es para qué hablo: informar, explicar cómo se hace algo o convencer. El propósito y la audiencia ayudan a decidir qué ideas incluir y cuáles dejar fuera para no cansar a quienes escuchan.",
    ],
    [("exposición oral", "explicación de un tema que una persona hace a un grupo"), ("tema", "asunto del que voy a hablar"), ("idea central", "lo más importante que quiero que la audiencia entienda"), ("audiencia", "personas que escuchan la exposición"), ("propósito", "para qué hablo: informar, explicar o convencer")],
    [
        ("Del tema a la idea central", "Tema: «el huerto escolar». ¿Cuál es una idea central: a) «El huerto escolar» b) «Un huerto escolar enseña a cuidar plantas y da verduras frescas»?", ["Busco la oración completa que dice algo del tema.", "La a es solo el tema.", "La b es una oración con una idea."], "b."),
        ("Pensar en la audiencia", "Expondrás cómo cuidar un huerto a niños de primero básico. ¿Qué conviene: a) palabras sencillas y ejemplos cercanos b) palabras técnicas y datos difíciles?", ["Pienso en quién escucha.", "Niños de primero necesitan palabras que conozcan.", "Eso es la a."], "a."),
    ],
    [("Confundir el tema con la idea central.", "Se cree que decir «el reciclaje» ya dice lo importante.", "Escribe una oración: «Reciclar papel reduce la basura»."), ("Preparar la exposición sin pensar en quién escucha.", "Se cree que sirve para todos igual.", "Pregunta: ¿quién escuchará y qué necesita saber?")],
    [
        E("Una exposición oral, ¿explica un tema a un grupo?", "Sí", "Esa es su finalidad."),
        E("¿Cuál es el tema: «el reciclaje de papel» o «Reciclar papel reduce la basura»?", "El reciclaje de papel", "El tema es corto; la segunda es una idea."),
        E("¿Quiénes forman la audiencia?", "Las personas que escuchan", "Reciben la exposición."),
    ],
    [
        E("¿La idea central se escribe como una palabra suelta o como una oración?", "Como una oración", "Debe decir algo sobre el tema."),
        E("Quieres explicar cómo plantar una semilla. ¿Cuál es tu propósito: informar o explicar cómo se hace?", "Explicar cómo se hace", "Muestras pasos para plantar."),
        E("¿Por qué conviene conocer a la audiencia?", "Para elegir palabras y ejemplos que entiendan", "Así se adapta lo que se dice."),
    ],
    [
        E("Escribe en una oración la idea central del tema «los libros de la biblioteca de aula», eligiendo la mejor: a) «Los libros de la biblioteca de aula nos ayudan a leer más y hay que cuidarlos» b) «Libros»", "a", "La a es oración con idea."),
        E("Tema: «el cuidado de las mascotas». Audiencia: apoderados. Propósito: convencer. ¿Qué idea central sirve: a) «Cuidar a una mascota requiere tiempo, agua y cariño todos los días» b) «Mascotas»?", "a", "Es oración y sirve al propósito."),
        E("Tienes dos temas posibles: «mi juego favorito» y «el universo completo». Para una exposición de cinco minutos, ¿cuál es más manejable?", "Mi juego favorito", "El otro es demasiado amplio."),
    ],
    [
        E("Dos compañeros preparan una exposición sobre el reciclaje. Uno piensa en niños de primero y el otro en profesores. ¿Cuál debe usar más ejemplos cercanos y palabras simples?", "El de niños de primero", "Su audiencia conoce menos palabras."),
        E("Si no puedo decir mi idea central en una sola oración, ¿está ya clara?", "No", "La idea central debe poder decirse en una oración."),
    ],
    [
        E("Plan A: «Voy a hablar de muchas cosas del mundo». Plan B: «Voy a explicar cómo regar un huerto en tres pasos». ¿Cuál tiene una idea central más clara?", "El plan B", "Dice qué y cuántos pasos."),
        arith("Tienes cinco minutos para exponer y planeas tres ideas de igual duración. ¿Cuántos segundos dura cada una si repartes 300 segundos entre las tres?", "300//3", "Se reparten los 300 segundos entre tres ideas.", " segundos"),
    ],
    [E("Debes exponer en tu curso sobre el cuidado del patio. Propones esta idea central: «Cuidar el patio es tarea de todos y empieza por no dejar basura». ¿Cumple con ser una oración que dice algo del tema?", "Sí", "Es una oración con una idea clara.")],
    [
        E("¿La idea central es lo más importante que quiero comunicar?", "Sí", "Guía toda la exposición."),
        E("¿El tema es una oración completa?", "No", "Es una palabra o frase breve."),
        E("¿La audiencia influye en las palabras que elijo?", "Sí", "Debo usar términos que entiendan."),
    ],
    ("Prepara el inicio de tu exposición. Elige uno de estos temas: a) «mi deporte o juego favorito», b) «cómo cuidar un lugar común de mi casa o de mi curso». Escribe: 1) el tema, 2) la idea central en una oración, 3) la audiencia (por ejemplo, tu curso o una persona de tu casa), 4) el propósito (informar, explicar cómo se hace o convencer). Léelo a una persona de tu casa y pregúntale si entiende cuál es tu idea central.",
     "1) Tema: cómo cuidar el patio. 2) Idea central: Cuidar el patio es tarea de todos y empieza por no dejar basura. 3) Audiencia: mi curso. 4) Propósito: convencer.",
     ["el tema es una frase breve", "la idea central es una oración clara", "nombra la audiencia", "dice el propósito"], ["hoja con los cuatro puntos y comentario de la persona"], ["confundir tema con idea central", "una idea central muy amplia"],
     "Si tu idea central no cabe en una oración, recórtala a lo más importante."),
    "Escribe tres temas y, para cada uno, una idea central.",
    "Escribe la misma idea central para dos audiencias distintas y explica qué cambiarías.",
)

# ================================================================ OA 27 · clase 2
reg(
    OA27, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: seis papelitos para ordenar frases.",
    "Aprenderé a organizar mi exposición en introducción, desarrollo y cierre, ordenando las ideas con conectores. Sirve para que la audiencia siga lo que digo sin perderse.",
    ["Sé decir una idea central en una oración.", "Sé usar primero, luego y finalmente."],
    [
        "Una exposición bien organizada tiene tres partes. La introducción abre el tema: saluda, dice de qué se hablará, presenta la idea central y avisa qué ideas vendrán. El desarrollo explica cada idea, una por una, con detalles y ejemplos. El cierre repasa lo más importante, repite la idea central con otras palabras y agradece.",
        "Para que el orden se note usamos conectores: «primero», «luego», «además», «por último», «en resumen». Cada idea del desarrollo debería ocupar su propio momento, sin mezclar. Si anunciamos tres ideas en la introducción, el desarrollo debe tener esas tres, y en ese orden.",
        "Veamos un ejemplo de introducción: «Hola, soy Ema. Hoy les explicaré cómo cuidar un huerto escolar. Hablaré de tres cosas: el agua, el sol y la tierra». Ahí está el saludo, el tema, la idea y el aviso. El desarrollo seguirá con el agua, luego el sol y después la tierra.",
    ],
    [("introducción", "parte inicial que presenta el tema y la idea central"), ("desarrollo", "parte central que explica las ideas una por una"), ("cierre", "parte final que repasa y termina"), ("conector", "palabra que ordena o une ideas, como «luego»"), ("anunciar", "decir con anticipación lo que se va a explicar")],
    [
        ("Reconocer las partes", "Frases: 1) «Hola, soy Ema; hoy explicaré cómo cuidar un huerto». 2) «Primero, el agua: se riega temprano». 3) «En resumen, un huerto necesita agua, sol y tierra». ¿Cuál es el cierre?", ["Busco la frase que repasa lo importante.", "La 1 presenta el tema.", "La 3 resume."], "La 3."),
        ("Seguir el orden anunciado", "Ema anunció: «Hablaré del agua, el sol y la tierra». ¿Qué debe explicar después de hablar del agua: a) el sol b) el cierre?", ["Sigo el orden anunciado.", "Después del agua viene el sol.", "El cierre va al final."], "a."),
    ],
    [("Empezar a hablar sin decir de qué se hablará.", "Se salta la introducción.", "Saluda, di el tema y la idea central, y avisa qué ideas vendrán."), ("Terminar con «eso es todo» sin repasar nada.", "Se cree que el cierre no importa.", "Repasa la idea central y las ideas principales, y agradece.")],
    [
        E("¿Cuántas partes tiene una exposición organizada?", "Tres", "Introducción, desarrollo y cierre."),
        E("¿En qué parte se explican las ideas una por una?", "En el desarrollo", "Allí se detalla cada idea."),
        E("¿Qué parte repasa lo más importante?", "El cierre", "Resume y termina."),
    ],
    [
        E("¿Qué conectores sirven para ordenar ideas: «primero», «luego» y «por último» o «pero», «ni» y «aunque»?", "Primero, luego y por último", "Indican el orden de las ideas."),
        E("Si anuncias tres ideas, ¿cuántas debe tener el desarrollo?", "Tres", "Debe cumplir lo anunciado."),
        E("En «Hola, soy Ema. Hoy explicaré cómo cuidar un huerto», ¿qué parte de la introducción es «Hola, soy Ema»?", "El saludo y la presentación", "La persona saluda y dice quién es."),
    ],
    [
        E("Ordena las partes de una exposición: a) cierre, b) desarrollo, c) introducción. Escribe las letras.", "c, b, a", "Primero se presenta, luego se explica y al final se cierra."),
        E("Frases del desarrollo: 1) Por último, la tierra. 2) Primero, el agua. 3) Luego, el sol. ¿En qué orden se dicen?", "2, 3, 1", "Siguen primero, luego, por último."),
        E("Elige la mejor introducción: a) «Hola, hoy explicaré cómo cuidar un huerto. Hablaré del agua, el sol y la tierra» b) «Eh... bueno... voy a empezar»", "a", "La a dice el tema y las ideas."),
    ],
    [
        E("Ema anunció tres ideas pero explicó solo dos. ¿Qué problema tiene su exposición?", "Faltó cumplir lo que anunció", "Dejó una idea sin explicar."),
        E("Luis termina con: «Y eso». ¿Qué le falta a su cierre: a) repasar la idea central y agradecer b) un saludo?", "a", "El cierre repasa y agradece."),
    ],
    [
        E("Una exposición dice: «Hoy les hablaré de las normas del patio. Veremos tres: no empujar, cuidar los juegos y botar la basura». En el desarrollo, el orden correcto de las normas es: a) botar la basura, cuidar los juegos, no empujar; b) no empujar, cuidar los juegos, botar la basura.", "b", "Sigue el orden anunciado."),
        E("En esa misma introducción, ¿cuántas normas se anuncian?", "Tres", "Se nombran no empujar, cuidar los juegos y botar la basura."),
    ],
    [E("Estás preparando una exposición con cuatro ideas. En la introducción anuncias solo tres. ¿Qué debes hacer: a) anunciar las cuatro ideas b) explicar cuatro ideas aunque no las anuncies?", "a", "La introducción debe avisar todas las ideas.")],
    [
        E("¿La introducción presenta el tema y la idea central?", "Sí", "Orienta a la audiencia."),
        E("¿El cierre debe repasar lo más importante?", "Sí", "Ayuda a recordar."),
        E("¿Los conectores ayudan a seguir el orden?", "Sí", "Muestran qué viene después."),
    ],
    ("Organiza una exposición breve. Tema: «cómo cuidar un lugar de mi casa». Escribe: 1) una introducción de tres o cuatro frases con saludo, tema, idea central y aviso de tus ideas, 2) el desarrollo con tres ideas ordenadas con «primero», «luego» y «por último», una frase cada una, 3) un cierre con repaso y agradecimiento. Léela en voz alta a una persona de tu casa.",
     "Introducción: Hola, soy Leo. Hoy explicaré cómo cuidar mi pieza. Hablaré de tres cosas: la cama, el escritorio y el piso. Desarrollo: Primero, la cama se arregla cada mañana. Luego, el escritorio se ordena después de estudiar. Por último, el piso se mantiene despejado. Cierre: En resumen, ordenar mi pieza me ayuda a vivir mejor. Gracias por escuchar.",
     ["tiene introducción, desarrollo y cierre", "usa conectores de orden", "cumple lo que anuncia", "se entiende al leerla"], ["texto escrito y lectura en voz alta"], ["olvidar el cierre", "anunciar ideas que no se explican"],
     "Si algo se perdió, revisa que cada idea anunciada tenga su explicación."),
    "Ordena las frases de una exposición que te muestre una persona de tu casa.",
    "Cambia el orden de las ideas del desarrollo y explica por qué el nuevo orden es mejor o peor.",
)

# ================================================================ OA 27 · clase 3
reg(
    OA27, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: un objeto cotidiano seguro (como una taza de plástico) para describir.",
    "Aprenderé a incluir descripciones y ejemplos que ilustren mis ideas. Sirve para que la audiencia imagine lo que explico y comprenda mejor.",
    ["Sé organizar una exposición en introducción, desarrollo y cierre.", "Sé usar adjetivos para decir cómo es algo."],
    [
        "Cuando exponemos, no basta con decir una idea: conviene ilustrarla. Una descripción dice cómo es algo con detalles que se pueden ver, oír, tocar u oler. Por ejemplo, en lugar de «Mi mochila es buena» podemos decir «Mi mochila es azul, tiene dos bolsillos grandes y un cierre resistente». Los detalles ayudan a que la audiencia se imagine lo que contamos.",
        "Un ejemplo es un caso concreto que muestra una idea. Lo introducimos con «por ejemplo», «como cuando» o «un caso es…». Si decimos «Reciclar ayuda a reducir la basura», un ejemplo sería: «Por ejemplo, si cada día usamos el reverso de las hojas, gastamos menos papel».",
        "Descripciones y ejemplos deben apoyar la idea. Si agregamos un detalle que no tiene relación, distraemos. También cuidamos no alargarnos: uno o dos buenos detalles por idea bastan. Un ejemplo bien elegido hace que la idea se recuerde.",
    ],
    [("descripción", "explicación de cómo es algo, con detalles"), ("detalle", "dato pequeño que hace más precisa una idea"), ("ejemplo", "caso concreto que muestra una idea"), ("ilustrar", "hacer más claro algo con detalles o ejemplos"), ("pertinente", "que tiene relación con lo que se explica")],
    [
        ("Descripción con detalles", "¿Qué frase describe mejor: a) «Mi mochila es buena» b) «Mi mochila es azul, tiene dos bolsillos grandes y un cierre resistente»?", ["Busco la frase con detalles que se pueden imaginar.", "La a no dice cómo es.", "La b da color, tamaño y partes."], "b."),
        ("Ejemplo pertinente", "Idea: «Reciclar ayuda a reducir la basura». ¿Qué ejemplo sirve: a) «Por ejemplo, si usamos el reverso de las hojas, gastamos menos papel» b) «Por ejemplo, mi gato duerme mucho»?", ["Busco el ejemplo relacionado con reciclar.", "La a muestra cómo se gasta menos papel.", "La b no tiene relación."], "a."),
    ],
    [("Decir ideas sin ningún detalle ni ejemplo.", "Se piensa que la idea es clara por sí sola.", "Agrega un detalle o un ejemplo para cada idea."), ("Agregar un ejemplo que no tiene relación con la idea.", "Se elige un ejemplo cualquiera para llenar tiempo.", "Revisa que el ejemplo muestre la idea.")],
    [
        E("¿Qué hace una descripción: dice cómo es algo o cuenta cuánto cuesta?", "Dice cómo es algo", "Da detalles de sus características."),
        E("¿Qué palabras introducen un ejemplo: «por ejemplo» o «sin embargo»?", "Por ejemplo", "Anuncia un caso concreto."),
        E("¿Un ejemplo es un caso concreto?", "Sí", "Muestra la idea con algo real."),
    ],
    [
        E("¿Para qué sirven los detalles en una exposición?", "Para que la audiencia imagine lo que explico", "Hacen más clara la idea."),
        E("Idea: «Un huerto necesita agua». ¿Cuál es un ejemplo: a) «Por ejemplo, una lechuga sin riego se arruga» b) «Los huertos son lindos»?", "a", "La a muestra un caso concreto."),
        E("¿Qué significa que un ejemplo sea pertinente?", "Que tiene relación con la idea", "Apoya lo que explico."),
    ],
    [
        E("Describe mejor este objeto: una taza de plástico verde, mediana y con un asa. ¿Qué frase sirve: a) «Es una taza» b) «Es una taza de plástico verde, mediana y con un asa»?", "b", "La b agrega color, tamaño y partes."),
        E("Idea: «Ordenar la mochila ayuda a no perder útiles». ¿Qué ejemplo sirve: a) «Por ejemplo, si el estuche siempre va en el bolsillo, lo encuentro rápido» b) «Por ejemplo, el recreo es largo»?", "a", "La a muestra cómo el orden ayuda."),
        E("Una frase dice: «Mi perro es tranquilo y duerme junto a mi cama». ¿Cuántos detalles da sobre el perro?", "Dos", "Es tranquilo y duerme junto a la cama."),
    ],
    [
        E("Ema dice: «Las plantas necesitan sol. Por ejemplo, mi lápiz es rojo». ¿Qué falla en su ejemplo?", "No tiene relación con la idea", "No muestra por qué las plantas necesitan sol."),
        E("Luis tiene dos ejemplos: 1) «Las plantas sin sol quedan débiles y pálidas». 2) «El sol sale por la mañana». ¿Cuál ilustra mejor que las plantas necesitan sol?", "El 1", "Muestra qué les pasa sin sol."),
    ],
    [
        E("Una exposición dice: «El patio es un lugar para jugar. Tiene un piso de cemento con dibujos de colores, dos arcos de fútbol y una banca larga». ¿Cuántas cosas describe en el patio?", "Tres", "Piso con dibujos, arcos y banca."),
        E("Con los detalles anteriores, ¿qué agrega la frase «con dibujos de colores»: una descripción o un ejemplo?", "Una descripción", "Dice cómo es el piso."),
    ],
    [E("Debes explicar que «Compartir los juguetes enseña a convivir». ¿Qué ejemplo elegirías: a) «Por ejemplo, cuando dos amigos alternan el uso de un balón, nadie se siente excluido» b) «Por ejemplo, el balón es redondo»?", "a", "La a muestra convivir al compartir.")],
    [
        E("¿Una descripción da detalles?", "Sí", "Dice cómo es algo."),
        E("¿Un ejemplo debe tener relación con la idea?", "Sí", "Si no, distrae."),
        E("¿Es mejor alargarse mucho con detalles?", "No", "Uno o dos buenos detalles bastan."),
    ],
    ("Ilustra una idea con descripción y ejemplo. Elige la idea: a) «Ordenar mi mochila me ayuda a encontrar mis útiles» o b) «Cuidar un objeto lo hace durar más». Escribe: 1) la idea, 2) una descripción de un objeto relacionado (con al menos tres detalles), 3) un ejemplo que comience con «por ejemplo». Léelo en voz alta a una persona de tu casa y pregunta si se imagina lo que describes.",
     "Idea: Ordenar mi mochila me ayuda a encontrar mis útiles. Descripción: Mi mochila es azul, tiene dos bolsillos grandes y uno chico en el frente. Por ejemplo, el estuche siempre va en el bolsillo chico y lo encuentro en un segundo.",
     ["la descripción tiene al menos tres detalles", "el ejemplo es pertinente", "usa «por ejemplo»", "se entiende al decirlo"], ["texto escrito y lectura en voz alta"], ["ejemplo sin relación", "descripción con pocos detalles"],
     "Si no se imagina el objeto, agrega color, tamaño o partes."),
    "Describe con tres detalles un objeto cotidiano de tu casa.",
    "Escribe dos ejemplos distintos para una misma idea y di cuál ilustra mejor.",
)

# ================================================================ OA 27 · clase 4
reg(
    OA27, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer en voz alta las frases.",
    "Aprenderé a aclarar a qué o a quién me refiero y a usar palabras más precisas. Sirve para que mi audiencia no se pierda con palabras como «eso», «ahí» o «cosa».",
    ["Sé organizar una exposición.", "Sé que los pronombres, como «él» o «ellos», reemplazan nombres."],
    [
        "Para no repetir tanto, usamos pronombres, que son palabras como «él», «ellos», «lo» o «eso» que reemplazan a un nombre. También usamos adverbios, que son palabras como «ahí», «ayer» o «así» que indican lugar, tiempo o modo. El referente es la persona, cosa o lugar a la que una palabra se refiere. Por ejemplo, en «Ana y Luis pintaron el mural. Ellos lo terminaron ayer», «ellos» se refiere a Ana y Luis, y «lo» al mural.",
        "En una exposición, la audiencia no puede volver atrás como cuando lee. Por eso, si un pronombre o un adverbio puede confundir, conviene reemplazarlo por una construcción que diga o describa el referente. En vez de «Ellos lo guardan ahí», podemos decir «Los niños guardan los materiales en la caja azul». Así la idea queda clara.",
        "Lo mismo ocurre con palabras comodín, como «cosa», «eso», «bueno», «ahí» y «así». Sirven para hablar rápido, pero dicen poco. Un vocabulario variado usa palabras precisas: en vez de «cosa para cortar», decimos «tijeras»; en vez de «es bueno», decimos «es útil» o «es seguro».",
    ],
    [("pronombre", "palabra que reemplaza a un nombre, como «ellos» o «lo»"), ("adverbio", "palabra que indica lugar, tiempo o modo, como «ahí», «ayer» o «así»"), ("referente", "persona, cosa o lugar a la que se refiere una palabra"), ("palabra comodín", "palabra vaga como «cosa» o «bueno» que dice poco"), ("vocabulario preciso", "palabras exactas que dicen justo lo que queremos")],
    [
        ("Encontrar el referente", "«Ana y Luis pintaron el mural. Ellos lo terminaron ayer». ¿A qué se refiere «lo»?", ["Busco qué cosa terminaron.", "Pintaron el mural.", "«Lo» se refiere al mural."], "Al mural."),
        ("Reemplazar con precisión", "«Ellos lo guardan ahí». Se habla de los niños, los materiales y la caja azul. ¿Qué oración deja claro el referente: a) «Los niños guardan los materiales en la caja azul» b) «Ellos guardan eso allá»?", ["Veo cuál nombra a quiénes, qué y dónde.", "La a lo dice todo.", "La b sigue vaga."], "a."),
    ],
    [("Usar «eso», «cosa» o «ahí» cuando la audiencia no sabe a qué se refiere.", "Hablando rápido se olvida que el otro no lo ve en tu mente.", "Di el nombre o describe: «las tijeras», «la caja azul»."), ("Repetir siempre la misma palabra, como «bueno».", "Es la palabra que primero viene a la mente.", "Busca una palabra más precisa: «útil», «seguro», «divertido».")],
    [
        E("En «Ana y Luis pintaron el mural. Ellos lo terminaron ayer», ¿a quiénes se refiere «ellos»?", "A Ana y Luis", "Son quienes pintaron."),
        E("¿«Ayer» indica lugar o tiempo?", "Tiempo", "Dice cuándo ocurrió."),
        E("¿«Ahí» indica lugar o modo?", "Lugar", "Señala dónde ocurre algo."),
    ],
    [
        E("¿Por qué conviene reemplazar «eso» por el nombre de lo que mencionamos?", "Para que la audiencia sepa a qué nos referimos", "Quienes escuchan no pueden volver atrás."),
        E("¿Qué es el referente de una palabra?", "La persona, cosa o lugar a la que se refiere", "Es lo que la palabra representa."),
        E("«Cosa para cortar papel». ¿Qué palabra precisa la reemplaza: tijeras o cosa?", "Tijeras", "Nombra el objeto exacto."),
    ],
    [
        E("«La profesora entregó los cuadernos a los niños. Ellos los guardaron en las mochilas». ¿A qué se refiere «los» en «los guardaron»?", "A los cuadernos", "Es lo que guardaron."),
        E("Reemplaza con precisión «Es bueno»: la frase es «Ordenar la sala es bueno porque evita accidentes». ¿Qué palabra precisa sirve más: a) seguro b) cosa?", "a", "«Seguro» dice por qué es bueno."),
        E("¿Qué oración deja claro quién trajo el mural: a) «Ellos lo trajeron» b) «Beto y Carla trajeron el mural»?", "b", "La b nombra a quiénes y qué."),
    ],
    [
        E("En «Eso es bueno porque ahí pintan una cosa grande», las palabras comodín son: cosa, eso, bueno, ahí y así. ¿Cuántas aparecen en la frase?", "Cuatro", "Aparecen eso, bueno, ahí y cosa."),
        E("Reescribe con más precisión «Ahí guardo eso» sabiendo que guardas los lápices en el estuche. ¿Qué opción es mejor: a) «En el estuche guardo los lápices» b) «Ahí guardo las cosas»?", "a", "Nombra el lugar y el objeto."),
    ],
    [
        E("Un expositor dice: «Los niños sembraron las semillas. Ellos las regaron todos los días». ¿A qué se refiere «las»?", "A las semillas", "Es lo que regaron."),
        E("En esa oración, ¿conviene reemplazar «ellos» por «los niños» si la audiencia no los vio antes?", "Sí", "Así queda claro quién regó."),
    ],
    [E("Estás explicando cómo funciona la biblioteca de aula y escribes: «Ahí ponen las cosas que traen». ¿Cuál reescritura es mejor: a) «En el estante de la sala se ponen los libros que traen los niños» b) «Allá se ponen eso»?", "a", "Nombra el lugar y los objetos.")],
    [
        E("Un pronombre reemplaza a un nombre. ¿Verdadero o falso?", "Verdadero", "Es su función."),
        E("¿Es mejor usar «cosa» o una palabra precisa cuando existe?", "Una palabra precisa", "Dice justo lo que queremos."),
        E("¿La audiencia puede volver atrás para releer lo que dices?", "No", "Por eso hay que ser claro al hablar."),
    ],
    ("Mejora una explicación. Lee este texto: «Ayer ellos hicieron eso ahí. Fue bueno porque la cosa quedó así». Imagina que se refiere a que Ana y Luis pintaron un mural en la entrada de la escuela, y quedó brillante y ordenado. Reescríbelo en dos o tres oraciones sin usar «ellos», «eso», «ahí», «cosa», «bueno» ni «así», dejando claro quiénes, qué, dónde y cómo. Léelo en voz alta a una persona de tu casa.",
     "Ayer Ana y Luis pintaron un mural en la entrada de la escuela. El mural quedó brillante y ordenado. Fue un trabajo útil porque la entrada se ve más acogedora.",
     ["nombra a quiénes", "nombra qué hicieron", "dice dónde y cómo", "no usa palabras comodín"], ["texto reescrito, escrito u oral"], ["dejar «ellos» sin aclarar", "cambiar los hechos"],
     "Si queda alguna palabra vaga, pregúntate: ¿puedo decir exactamente quién, qué o dónde?"),
    "Cambia tres palabras comodín de una conversación de tu casa por palabras precisas.",
    "Escribe un párrafo de tres oraciones sobre tu curso y marca cada pronombre con su referente.",
)

# ================================================================ OA 27 · clase 5
reg(
    OA27, 5,
    "Este cuaderno, lápiz y una hoja grande o dos hojas pegadas. Una persona de tu casa que mire y comente. Usa solo materiales seguros.",
    "Aprenderé a ensayar mi exposición cuidando la voz, la postura y los gestos, y a preparar un apoyo visual claro. Sirve para que la audiencia me oiga, me entienda y recuerde mi idea central.",
    ["Sé organizar una exposición con ejemplos.", "Sé aclarar a qué me refiero."],
    [
        "Al exponer, el cuerpo y la voz comunican tanto como las palabras. La voz debe tener un volumen que se oiga hasta el fondo, un ritmo ni muy rápido ni muy lento y pausas cortas entre ideas. La postura es firme y relajada: pies apoyados, espalda recta y manos visibles. Miramos a la audiencia, repartiendo la mirada entre las personas. Los gestos acompañan lo que decimos, como señalar un dibujo, pero no distraen.",
        "El material de apoyo, como un afiche, un papelógrafo, un objeto seguro o una presentación, debe ser pertinente: sirve solo si ayuda a entender la idea. Un buen apoyo tiene pocas palabras clave, letras grandes que se lean desde el fondo, y una imagen relacionada. No lo usamos para leerlo entero: lo miramos poco y nos dirigimos a la audiencia.",
        "Ensayar es practicar en voz alta, ojalá frente a alguien, y cronometrar el tiempo. Después de ensayar, pedimos una opinión: ¿se oyó bien?, ¿se entendió la idea central?, ¿ayudó el apoyo visual? Con esas respuestas corregimos antes de exponer.",
    ],
    [("volumen", "qué tan fuerte suena la voz"), ("postura", "forma de colocar el cuerpo al hablar"), ("gesto", "movimiento de manos o cara que acompaña lo que decimos"), ("material de apoyo", "afiche, objeto o imagen que ayuda a explicar"), ("palabra clave", "palabra importante que recuerda una idea")],
    [
        ("Elegir un buen apoyo", "Vas a explicar tres pasos para plantar una semilla. ¿Qué afiche es mejor: a) un dibujo de cada paso con una palabra clave grande b) un párrafo largo con letra muy pequeña?", ["Pienso en qué se lee desde el fondo.", "La a usa dibujos y pocas palabras.", "La b no se lee a distancia."], "a."),
        ("Mejorar la postura y la mirada", "Tomás expone mirando el suelo y con las manos en los bolsillos. ¿Qué cambio ayuda más: a) mirar a la audiencia y dejar las manos visibles b) hablar más rápido?", ["Veo qué hace Tomás que no ayuda.", "No mira a la audiencia.", "La a corrige mirada y manos."], "a."),
    ],
    [("Leer el afiche completo dándole la espalda a la audiencia.", "Se usa el apoyo como guion.", "Usa palabras clave y mira a la audiencia."), ("Poner mucho texto en letra pequeña en el afiche.", "Se quiere decir todo en el material.", "Usa pocas palabras grandes y una imagen.")],
    [
        E("¿Hacia dónde conviene mirar mientras exponemos: a la audiencia o al suelo?", "A la audiencia", "La mirada conecta con quienes escuchan."),
        E("¿El volumen debe permitir que se oiga hasta el fondo?", "Sí", "Si no, parte de la audiencia no escucha."),
        E("En Lenguaje: ¿Qué es una palabra clave?", "Una palabra importante que recuerda una idea", "Sirve para guiar al expositor."),
    ],
    [
        E("¿Para qué sirve un material de apoyo pertinente?", "Para ayudar a entender la idea", "No es solo decoración."),
        E("¿Qué es mejor en un afiche: tres palabras grandes o diez líneas pequeñas?", "Tres palabras grandes", "Se leen desde el fondo."),
        E("¿Qué hacemos después de ensayar: pedir una opinión o no hacer nada?", "Pedir una opinión", "Permite corregir antes de exponer."),
    ],
    [
        arith("Tu afiche tendrá tres ideas con dos palabras clave cada una. ¿Cuántas palabras clave tiene en total?", "3*2", "Se multiplica el número de ideas por las palabras de cada una.", " palabras"),
        arith("Tu exposición dura 4 minutos y ensayas 3 veces completa. ¿Cuántos minutos hablas en total en los ensayos?", "4*3", "Se repite la duración de la exposición en cada ensayo.", " minutos"),
        E("Quieres señalar una parte de tu dibujo mientras hablas. ¿Qué gesto ayuda: a) señalar con la mano y volver a mirar a la audiencia b) tapar el dibujo con el cuerpo?", "a", "El gesto acompaña lo que dices sin ocultarlo."),
    ],
    [
        E("Sofía lee todo el texto de su afiche con voz bajita, mirando solo el afiche. Desde el fondo no se le oye. ¿Qué cambio es más urgente: a) subir el volumen b) cambiar el color del lápiz?", "a", "Sin volumen suficiente no se entiende la idea."),
        E("Mateo dice: «Mi afiche es un dibujo de los tres pasos con una palabra grande en cada uno». ¿Cumple lo que se espera de un buen apoyo?", "Sí", "Tiene pocas palabras clave y una imagen."),
    ],
    [
        E("Explicas cómo cuidar un libro. ¿Qué material de apoyo es más pertinente: a) un dibujo de un libro con una cubierta de plástico y la palabra «Forrar» b) la foto de una montaña?", "a", "La a tiene relación con cuidar un libro."),
        E("Tu afiche estará pegado a dos metros de la audiencia. ¿Qué letra sirve más: a) grande, que se lea desde el fondo b) muy pequeña?", "a", "Debe leerse a distancia."),
    ],
    [E("Tu compañera ensaya y dice: «Me pidieron que hablara más fuerte porque desde el fondo no se oía». ¿Qué debe mejorar: la voz o el color del afiche?", "La voz", "El problema fue el volumen.")],
    [
        E("¿Los gestos deben distraer?", "No", "Deben acompañar lo que decimos."),
        E("¿Ensayar en voz alta ayuda a mejorar?", "Sí", "Permite corregir y cronometrar."),
        E("¿El material de apoyo se usa para leerlo completo?", "No", "Sirve como ayuda, no como guion."),
    ],
    ("Ensaya tu exposición con apoyo visual. Usa el tema «cómo cuidar un libro» con estas tres ideas: forrar la tapa, no doblar las hojas y guardarlo en un lugar seco. Haz un afiche con una hoja grande: una palabra clave grande y un dibujo para cada idea. Ensaya en voz alta con una persona de tu casa, cuidando volumen, mirada y postura. Pídele que anote qué estuvo bien y qué mejorar, y escríbelo.",
     "Afiche: Forrar (dibujo de un libro con cubierta), No doblar (dibujo de una página doblada con una cruz), Seco (dibujo de un estante). Comentario recibido: se oyó bien; mejorar mirar más a la audiencia.",
     ["el afiche tiene pocas palabras clave grandes", "el apoyo es pertinente", "cuida voz, mirada y postura", "registra una opinión con algo bueno y algo por mejorar"], ["afiche y nota con la opinión recibida"], ["afiche con mucho texto", "leer sin mirar a la audiencia"],
     "Si el afiche tiene mucho texto, deja solo la palabra clave y agrega un dibujo."),
    "Ensaya una vez más, esta vez con un cronómetro, y anota cuántos minutos duró.",
    "Prepara otro afiche para la misma exposición con una idea más y ajusta la duración.",
)

# ================================================================ OA 27 · clase 6
reg(
    OA27, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que lea el texto de la exposición.",
    "Aprenderé a revisar una exposición con una pauta, a reconocer qué hace bien y a decidir mis próximos pasos. Sirve para mejorar mis exposiciones con criterios claros.",
    ["Sé organizar mi exposición, usar ejemplos, aclarar referentes y ensayar voz y apoyo.", "Sé dar y recibir una opinión con respeto."],
    [
        "Una pauta es una lista de criterios para revisar un trabajo. Para una exposición podemos usar cinco: 1) tiene introducción con tema e idea central, 2) el desarrollo explica las ideas en orden, 3) incluye ejemplos y descripciones, 4) aclara a qué se refiere, sin palabras vagas, y 5) el cierre repasa y agradece. Para la presentación sumamos voz clara, mirada a la audiencia y apoyo visual pertinente.",
        "Con una pauta buscamos hallazgos, que son lo que descubrimos al revisar: qué cumple y qué no. Escribimos un hallazgo con evidencia, por ejemplo: «Cumple el criterio 3, porque dice: por ejemplo, ayer Pía casi se cae». Un hallazgo sin evidencia no sirve para mejorar.",
        "Después decidimos los próximos pasos: acciones concretas para corregir lo que falló, como «agregar un ejemplo a la segunda idea» o «cambiar eso por el nombre del objeto». Así una exposición revisada se vuelve una exposición mejor.",
    ],
    [("pauta", "lista de criterios para revisar un trabajo"), ("criterio", "característica que se espera que cumpla un trabajo"), ("hallazgo", "lo que descubrimos al revisar algo, con evidencia"), ("evidencia", "frase o dato que muestra que algo se cumple"), ("próximo paso", "acción concreta para mejorar")],
    [
        ("Aplicar un criterio", "Exposición de Tomás: «Hola, soy Tomás. Hoy les explicaré por qué es útil ordenar la sala. Hablaré de dos ideas: encontrar las cosas rápido y estar más seguros. Primero, cuando el estuche está en su caja, lo encuentro en un segundo. Segundo, cuando la sala está ordenada, nadie se tropieza con las mochilas; por ejemplo, ayer Pía casi se cae. En resumen, ordenar la sala nos ahorra tiempo y nos cuida. Gracias por escuchar». ¿Cuántas oraciones forman la introducción?", ["Cuento las oraciones desde el saludo hasta el aviso de las dos ideas.", "La 1 saluda, la 2 dice el tema y la 3 anuncia las ideas.", "Son tres."], "Tres oraciones."),
        ("Escribir un hallazgo con evidencia", "En la exposición de Tomás, ¿qué evidencia muestra que incluye un ejemplo?", ["Busco una frase con «por ejemplo».", "Dice: «por ejemplo, ayer Pía casi se cae».", "Eso es un caso concreto."], "La frase «por ejemplo, ayer Pía casi se cae»."),
    ],
    [("Decir que algo «está bien» o «está mal» sin mostrar evidencia.", "Se opina rápido sin mirar el texto.", "Cita la frase que muestra que cumple o no el criterio."), ("Proponer un próximo paso demasiado general, como «mejorar todo».", "No se decide qué hacer.", "Escribe una acción concreta, como «agregar un ejemplo a la idea 1».")],
    [
        E("¿Qué es una pauta?", "Una lista de criterios para revisar un trabajo", "Sirve para evaluar con claridad."),
        E("En la exposición de Tomás, ¿cuántas ideas anuncia en la introducción?", "Dos", "Encontrar las cosas rápido y estar más seguros."),
        E("¿Qué hace Tomás en el cierre: repasar y agradecer o presentar una nueva idea?", "Repasar y agradecer", "Dice: «En resumen…» y «Gracias por escuchar»."),
    ],
    [
        E("¿Qué es un hallazgo?", "Lo que descubrimos al revisar algo, con evidencia", "Dice qué se cumple o no."),
        E("¿Por qué un hallazgo necesita evidencia?", "Para mostrar de dónde sale la conclusión", "Sin evidencia es solo una opinión."),
        E("¿Qué palabra de Tomás conecta la primera idea del desarrollo: «Primero», «Ayer» o «Gracias»?", "Primero", "Ordena la primera idea."),
    ],
    [
        E("En la exposición de Tomás, ¿qué idea explica la frase «nadie se tropieza con las mochilas»: encontrar las cosas rápido o estar más seguros?", "Estar más seguros", "Habla de evitar tropiezos y accidentes."),
        E("¿Cuál es un próximo paso concreto: a) «agregar un detalle que describa la caja del estuche» b) «hacerlo todo mejor»?", "a", "La a dice qué hacer exactamente."),
        E("Tomás dice «lo encuentro en un segundo». ¿Esa expresión indica tiempo o lugar?", "Tiempo", "Dice qué tan rápido encuentra el estuche."),
    ],
    [
        E("Un compañero evalúa: «Cumple el criterio de ejemplos». Otro evalúa: «Cumple el criterio de ejemplos, porque dice: por ejemplo, ayer Pía casi se cae». ¿Cuál evaluación tiene evidencia?", "La segunda", "Cita la frase."),
        E("En la exposición de Tomás, la palabra «cosas» aparece en «encontrar las cosas rápido». ¿Qué criterio cuestiona: la presencia de ejemplos o las palabras vagas?", "Las palabras vagas", "«Cosas» es una palabra comodín."),
    ],
    [
        E("Corrige «encontrar las cosas rápido»: ¿qué cambio da más precisión: a) «encontrar mis útiles rápido» b) «encontrar eso rápido»?", "a", "Nombra lo que se encuentra."),
        E("Tomás solo dio un ejemplo para la segunda idea y ninguno para la primera. ¿Qué próximo paso concreto le conviene?", "Agregar un ejemplo a la primera idea", "Falta el ejemplo de la idea 1."),
    ],
    [E("Después de revisar tu exposición descubres que la introducción no anuncia las ideas y que usaste «eso» tres veces. ¿Cuántos próximos pasos necesitas como mínimo: uno por problema?", "Dos", "Uno para la introducción y otro para reemplazar «eso».")],
    [
        E("Una pauta ayuda a revisar con criterios claros. ¿Verdadero o falso?", "Verdadero", "Evita revisar solo por impresión."),
        E("¿Un próximo paso debe ser concreto?", "Sí", "Así se puede cumplir."),
        E("¿Conviene mostrar evidencia al evaluar?", "Sí", "Sostiene lo que decimos."),
    ],
    ("Revisa tu exposición con una pauta. Usa la exposición escrita en la clase 2 o 5, o la de Tomás de esta clase. Escribe cinco hallazgos, uno por criterio: introducción con tema e idea central, desarrollo ordenado, ejemplos y descripciones, referentes claros, y cierre. Para cada uno escribe «cumple» o «no cumple» con una evidencia. Luego escribe dos próximos pasos concretos para mejorar y léelos a una persona de tu casa.",
     "Introducción: cumple, porque dice «Hoy les explicaré por qué es útil ordenar la sala». Ejemplos: cumple, porque dice «por ejemplo, ayer Pía casi se cae». Referentes: no cumple del todo, porque dice «las cosas». Próximos pasos: cambiar «las cosas» por «mis útiles» y agregar un ejemplo a la primera idea.",
     ["revisa los cinco criterios", "cada hallazgo tiene evidencia", "propone dos próximos pasos concretos"], ["pauta completada y lectura en voz alta"], ["decir «cumple» sin evidencia", "próximos pasos demasiado generales"],
     "Si no tienes evidencia, vuelve al texto y copia la frase que muestra el criterio."),
    "Revisa una exposición de la clase 2 con solo dos criterios y anota un hallazgo con evidencia.",
    "Prepara una pauta propia de seis criterios para revisar exposiciones del curso.",
)

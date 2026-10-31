"""Cuaderno del estudiante, 5.º básico Lenguaje y Comunicación: OA 28 (exposición oral clara y fundamentada)."""
from __future__ import annotations

from student_content_le5_d import E, reg
from student_lessons import arith

OA28 = "LE05 OA 28"

# ================================================================ OA 28 · clase 1
reg(
    OA28, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa como audiencia para practicar en voz alta.",
    "Aprenderé a reconocer qué es una exposición oral, para qué se hace y cómo se organiza en introducción, desarrollo y cierre. Sirve para presentar con claridad un tema que me interesa ante mi curso.",
    ["Sé presentarme y hablar con respeto.", "Sé que una idea se apoya con razones."],
    [
        "Una exposición oral es una presentación en que una persona habla ante una audiencia, que es el grupo que escucha, sobre un tema que preparó. Su propósito más común es informar: explicar algo para que los demás lo comprendan. El desafío es hablar de forma clara y ordenada, para que la audiencia no se pierda.",
        "Para ordenar las ideas, una exposición tiene tres partes. La introducción saluda, presenta el tema y dice qué se va a explicar. El desarrollo es la parte central: expone las ideas con ejemplos y datos. El cierre resume lo más importante, agradece y puede invitar a hacer preguntas.",
        "Para prepararla conviene seguir un camino: elegir el tema y pensar en la audiencia, juntar datos y ejemplos, organizar las ideas en las tres partes y, por último, ensayar en voz alta. Si la audiencia son niños más pequeños, usamos palabras más simples; si es la directora, un registro más formal.",
    ],
    [("exposición oral", "presentación hablada de un tema preparado"), ("audiencia", "grupo de personas que escucha"), ("introducción", "parte inicial que saluda y presenta el tema"), ("desarrollo", "parte central con ideas, ejemplos y datos"), ("cierre", "parte final que resume y se despide")],
    [
        ("Reconocer las partes", "Texto «El ajedrez»: «Buenos días, compañeros. Hoy les voy a hablar del ajedrez, un juego que practico hace dos años. Les explicaré cómo es el tablero. El tablero tiene 64 casillas, 8 filas y 8 columnas. Cada jugador empieza con 16 piezas. En resumen, el ajedrez se juega en un tablero de 64 casillas. Gracias por escucharme». ¿En qué parte está «Hoy les voy a hablar del ajedrez»?", ["Esa frase saluda y anuncia el tema.", "Ocurre al comienzo.", "Anunciar el tema es propio de la introducción."], "En la introducción."),
        ("Reconocer el propósito", "En «El ajedrez», el expositor explica cómo es el tablero y cuántas piezas hay. ¿Cuál es su propósito: informar o convencer de comprar un tablero?", ["Veo qué hace: explica datos del juego.", "No pide comprar nada.", "Entonces busca que los demás comprendan."], "Informar."),
    ],
    [("Empezar a hablar sin saludar ni decir el tema.", "Se cree que la audiencia ya sabe de qué se hablará.", "Saluda y anuncia el tema y lo que explicarás."), ("Terminar con «bueno, eso es todo» sin resumir.", "Se piensa que el cierre solo sirve para parar.", "Resume lo central en una o dos frases y agradece.")],
    [
        E("Según el texto «El ajedrez», ¿cuántas casillas tiene el tablero?", "64", "El texto lo dice en el desarrollo."),
        E("En el texto, ¿quién es la audiencia: los compañeros o la directora?", "Los compañeros", "Comienza con «Buenos días, compañeros»."),
        E("¿Qué frase del texto es el agradecimiento final?", "Gracias por escucharme", "Cierra la exposición."),
    ],
    [
        E("¿Cuáles son las tres partes de una exposición: a) introducción, desarrollo y cierre b) saludo, chiste y despedida?", "a", "Así se organiza una exposición."),
        E("«Gracias por escucharme», ¿se dice en la introducción o en el cierre?", "En el cierre", "Es parte de la despedida."),
        E("La frase «En resumen, el ajedrez se juega en un tablero de 64 casillas» repite lo central. ¿Con qué parte se relaciona: el desarrollo o el cierre?", "El cierre", "Resumir es una función del cierre."),
    ],
    [
        arith("El tablero tiene 8 filas y cada fila tiene 8 casillas. ¿Cuántas casillas hay en total?", "8*8", "Se multiplica el número de filas por las casillas de cada fila.", " casillas"),
        arith("Cada jugador empieza con 16 piezas y juegan dos personas. ¿Cuántas piezas hay al comenzar sobre el tablero?", "16+16", "Se suman las piezas de ambos jugadores.", " piezas"),
        E("Ordena estas frases como una exposición. a) El alfil solo se mueve en diagonal. b) Hoy les hablaré del ajedrez. c) En resumen, cada pieza tiene su movimiento. Escribe las letras.", "b, a, c", "Primero se anuncia el tema, luego se explica y al final se resume."),
    ],
    [
        E("Un compañero entra directo a hablar de las piezas sin saludar ni decir el tema. ¿Qué parte de la exposición le falta?", "La introducción", "No saludó ni anunció de qué hablaría."),
        E("Dos niños exponen sobre el ajedrez. Ema dice «el ajedrez es lindo». Iván dice «el tablero tiene 64 casillas». ¿Quién entrega información que se puede comprobar?", "Iván", "Su dato se puede comprobar; el de Ema es una opinión."),
    ],
    [
        arith("Una exposición dura 180 segundos. La introducción usa 30 segundos y el cierre otros 30. ¿Cuántos segundos quedan para el desarrollo?", "180-30-30", "Se restan los tiempos de introducción y cierre al total.", " segundos"),
        E("Si tu audiencia son niños de primero básico, ¿qué conviene: a) usar palabras difíciles para sonar serio b) usar palabras simples y ejemplos cercanos?", "b", "La exposición debe adaptarse a la audiencia."),
    ],
    [E("Tu profesora te pide exponer sobre un pasatiempo. Ordena cómo prepararte. a) ensayar en voz alta b) elegir el tema y pensar en la audiencia c) organizar introducción, desarrollo y cierre d) juntar datos y ejemplos. Escribe las letras.", "b, d, c, a", "No se puede organizar sin datos ni ensayar sin organizar.")],
    [
        E("¿Una exposición oral informa o solo adivina?", "Informa", "Su propósito es explicar un tema."),
        E("¿Cuál es la parte central de la exposición: el desarrollo o el cierre?", "El desarrollo", "Allí van las ideas con ejemplos y datos."),
        E("¿Hay que adaptar la exposición a la audiencia? Responde sí o no.", "Sí", "El vocabulario y el registro cambian según quién escucha."),
    ],
    ("Elige uno de estos temas: «un juego que me gusta», «un animal que conozco» o «un lugar de mi barrio». Escribe un plan en tres líneas: 1) Introducción: tu saludo y la frase que anuncia el tema. 2) Desarrollo: dos datos o ejemplos que explicarías. 3) Cierre: tu frase de resumen y agradecimiento. Léelo en voz alta a una persona de tu casa y pregúntale de qué trataba la exposición.",
     "Tema: un juego que me gusta. 1) «Buenos días, hoy les hablaré de la rayuela». 2) «Se dibuja con tiza en el suelo; se salta en un pie». 3) «En resumen, la rayuela es un juego de saltos. Gracias por escucharme».",
     ["tiene las tres partes", "el tema se anuncia con claridad", "incluye al menos dos datos o ejemplos"], ["plan de tres líneas escrito", "lectura en voz alta"], ["no anunciar el tema", "cerrar sin resumir"],
     "Si la persona no entendió el tema, revisa si tu introducción lo dice de forma directa."),
    "Escribe otra introducción para el mismo tema, esta vez dirigida a niños de primero básico.",
    "Observa una presentación o noticia y anota en qué momento aparecen la introducción, el desarrollo y el cierre.",
)

# ================================================================ OA 28 · clase 2
reg(
    OA28, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer en voz alta el texto modelo.",
    "Aprenderé a presentar mis ideas de manera coherente y cohesiva, es decir, ordenadas y unidas con conectores. Sirve para que mi exposición se entienda de principio a fin.",
    ["Sé que una exposición tiene introducción, desarrollo y cierre.", "Sé usar «porque» para dar una razón."],
    [
        "Una exposición es coherente cuando todas sus ideas se relacionan con el tema y siguen un orden lógico. Si hablo de reciclaje y, de pronto, cuento qué hago los sábados, rompo la coherencia. Es mejor dejar fuera lo que no aporta y poner las ideas en una secuencia que la audiencia pueda seguir.",
        "Una exposición es cohesiva cuando sus partes están bien unidas. Para unirlas usamos conectores, que son palabras o frases que enlazan ideas. Algunos marcan orden («primero», «luego», «finalmente»), otros agregan («además»), dan un ejemplo («por ejemplo»), muestran una consecuencia («por eso») o cierran («en resumen»). También ayudan las palabras que reemplazan a otras para no repetirlas, como «ellas» o «allí».",
        "Modelo: «Hoy les hablaré de cómo mi curso recicla papel. Primero, cada estudiante separa las hojas usadas en una caja azul. Además, el viernes la caja se pesa. Por ejemplo, la semana pasada juntamos 9 kilos. Por eso, ahora no botamos papel al basurero común. En resumen, separar papel es fácil y evita desperdiciarlo». Observa cómo cada conector dice qué hace la frase que sigue.",
    ],
    [("coherencia", "relación lógica y ordenada entre las ideas"), ("cohesión", "unión de las partes del texto con conectores"), ("conector", "palabra que enlaza ideas, como «además»"), ("secuencia", "orden en que van las ideas"), ("consecuencia", "lo que resulta de algo")],
    [
        ("Ubicar un conector", "Texto modelo «Reciclar papel»: «Hoy les hablaré de cómo mi curso recicla papel. Primero, cada estudiante separa las hojas usadas en una caja azul. Además, el viernes la caja se pesa. Por ejemplo, la semana pasada juntamos 9 kilos. Por eso, ahora no botamos papel al basurero común. En resumen, separar papel es fácil y evita desperdiciarlo». ¿Qué conector introduce un ejemplo?", ["Busco la frase que presenta un caso concreto.", "Es la que habla de los 9 kilos.", "Comienza con «Por ejemplo»."], "«Por ejemplo»."),
        ("Detectar lo que rompe la coherencia", "En una exposición sobre reciclaje de papel, un niño agrega: «Mi amigo juega fútbol los sábados». ¿Esa frase es coherente con el tema?", ["Comparo con el tema: el reciclaje de papel.", "El fútbol del primo no se relaciona.", "Rompe la coherencia."], "No, porque no se relaciona con el reciclaje."),
    ],
    [("Poner datos sueltos sin conectores.", "Se cree que basta con listar las ideas.", "Une las ideas con «además», «por eso», «por ejemplo»."), ("Usar el mismo conector («y») en todas las oraciones.", "Es una forma muy familiar de hablar.", "Varía: «luego», «sin embargo», «en cambio»…")],
    [
        E("Según el texto, ¿dónde separa el papel cada estudiante?", "En una caja azul", "Está en la segunda oración del texto."),
        E("¿Qué conector del texto marca el cierre?", "En resumen", "Introduce la idea final."),
        E("¿Cuántos kilos juntó el curso la semana pasada, según el texto?", "9 kilos", "Está en el ejemplo."),
    ],
    [
        E("En «Por eso, ahora no botamos papel al basurero común», ¿qué indica «Por eso»: a) una consecuencia b) un ejemplo?", "a", "Muestra el resultado de lo anterior."),
        E("¿Cuál frase rompe la coherencia en una exposición sobre reciclaje de papel: a) «El viernes la caja se pesa.» b) «A mí me gusta cocinar.»", "b", "No se relaciona con el tema."),
        E("En «Las hojas usadas se separan. Ellas van a una caja azul», ¿qué palabra reemplaza a «las hojas usadas»?", "Ellas", "Evita repetir la expresión."),
    ],
    [
        E("Completa con un conector: «Separamos el papel. ______, lo pesamos cada viernes.» Opciones: además / en resumen.", "Además", "Agrega otra acción a la anterior."),
        E("Ordena para formar un párrafo coherente. a) Luego, la llevamos al punto de reciclaje. b) Primero, juntamos papel en una caja. c) Finalmente, anotamos cuántos kilos entregamos. Escribe las letras.", "b, a, c", "Los conectores primero, luego y finalmente marcan el orden."),
        arith("Cada semana el curso junta 9 kilos de papel. ¿Cuántos kilos junta en 4 semanas si mantiene ese ritmo?", "9*4", "Se repite la misma cantidad cuatro veces.", " kilos"),
    ],
    [
        E("Versión A: «Reciclamos. Es bueno. Hay cajas. Pesamos.» Versión B: «Reciclamos porque es bueno; por eso hay cajas y, además, pesamos cada viernes.» ¿Cuál es más cohesiva y por qué?", "La B, porque une las ideas con conectores", "La A son frases sueltas."),
        E("Un expositor usa «y» en todas las oraciones: «Separamos y pesamos y llevamos y anotamos». ¿Qué conviene hacer: a) variar los conectores como «luego» y «finalmente» b) repetir más «y»?", "a", "Variar mejora la cohesión."),
    ],
    [
        E("En una exposición sobre bicicletas, ordena las ideas para que sean coherentes. a) Por ejemplo, el casco protege la cabeza. b) Hoy hablaré de la seguridad al andar en bicicleta. c) Por eso, siempre hay que usarlo. Escribe las letras.", "b, a, c", "Se presenta el tema, se da el ejemplo y se concluye con la consecuencia."),
        E("Tres ideas: 1) el casco se abrocha, 2) el casco debe quedar firme, 3) el cine abrió una película. ¿Cuál no es coherente con una exposición sobre usar casco?", "La 3", "No se relaciona con el casco."),
    ],
    [E("Para exponer sobre el cuidado de las plantas del patio, un compañero escribe: «Las plantas necesitan agua. ______, se riegan cada día». ¿Qué conector indica una consecuencia: a) Por eso b) Sin embargo?", "a", "«Por eso» muestra que el riego es el resultado de que necesiten agua.")],
    [
        E("¿Para qué sirven los conectores: para unir ideas o para llenar espacio?", "Para unir ideas", "Enlazan las partes del texto."),
        E("Una exposición coherente, ¿incluye ideas que no se relacionan con el tema? Responde sí o no.", "No", "Todo debe relacionarse con el tema."),
        E("¿«Por ejemplo» introduce una consecuencia o un caso concreto?", "Un caso concreto", "Muestra una idea con un ejemplo."),
    ],
    ("Usa estos tres datos para escribir un párrafo de exposición sobre «Cuidar el agua en casa»: 1) cerrar la llave al lavarse los dientes, 2) usar un balde para regar, 3) avisar si hay una llave que gotea. Escribe cuatro oraciones ordenadas y úsalas con al menos tres conectores distintos: por ejemplo, primero, además, por eso, finalmente o en resumen. Léelo en voz alta.",
     "«Hoy les hablaré de cómo cuidar el agua en casa. Primero, conviene cerrar la llave al lavarse los dientes. Además, se puede usar un balde para regar. Finalmente, hay que avisar si una llave gotea; por eso, el agua no se desperdicia».",
     ["usa los tres datos", "ordena las ideas con una secuencia", "emplea al menos tres conectores distintos"], ["párrafo escrito de cuatro oraciones"], ["repetir siempre «y»", "incluir ideas que no se relacionan con el tema"],
     "Si el texto suena entrecortado, revisa si cada oración tiene un conector que la una con la anterior."),
    "Subraya los conectores del texto «Reciclar papel» y escribe qué indica cada uno.",
    "Elige un párrafo de un libro o texto de la escuela y marca los conectores que encuentres.",
)

# ================================================================ OA 28 · clase 3
reg(
    OA28, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para comentar tus ejemplos.",
    "Aprenderé a fundamentar mis planteamientos con ejemplos y datos, y a usar un vocabulario preciso en lugar de palabras vagas como «cosa». Sirve para que mi exposición sea creíble y clara.",
    ["Sé que una exposición tiene tres partes.", "Sé distinguir un dato de una opinión."],
    [
        "Un planteamiento es una idea que defendemos en una exposición, como «la forma más común de llegar al colegio es caminar». Para fundamentarlo, es decir, respaldarlo, necesitamos datos y ejemplos. Un dato es información que se puede comprobar, como una cifra. Un ejemplo es un caso concreto que muestra la idea.",
        "Hay que elegir bien los datos. Un dato pertinente es el que apoya de verdad el planteamiento. Si digo «la forma más común es caminar», el dato pertinente es cuántos caminan comparados con los demás. Un dato que no se relaciona, como el color de las mochilas, no sirve. Además, antes de afirmar algo hay que comprobar que el dato lo permite: 10 de 24 no es «la mayoría», pero sí es «el grupo más grande».",
        "También cuidamos el vocabulario preciso, que es usar la palabra exacta. En lugar de decir «la cosa del colegio», decimos «el casillero» o «la biblioteca». En lugar de «un montón», podemos decir la cifra: «24 estudiantes». Las palabras exactas ayudan a que la audiencia entienda sin adivinar.",
    ],
    [("planteamiento", "idea que se defiende en la exposición"), ("fundamentar", "respaldar una idea con datos y ejemplos"), ("pertinente", "que se relaciona y sirve para el tema"), ("vocabulario preciso", "palabras exactas en lugar de palabras vagas"), ("mayoría", "más de la mitad del total")],
    [
        ("Elegir el dato que respalda", "Encuesta: se preguntó a 24 estudiantes de 5.º B cómo llegan al colegio. 10 caminan, 8 van en bus, 4 en auto y 2 en bicicleta. Planteamiento: «Caminar es la forma más común de llegar». ¿Qué dato lo respalda?", ["Busco la cifra que compara las formas.", "10 caminan y es la cifra más alta.", "Eso apoya el planteamiento."], "10 estudiantes caminan, más que en cualquier otra forma."),
        ("Comprobar una afirmación", "Con los mismos datos, ¿es verdad que «la mayoría va en bus»?", ["Mayoría es más de la mitad: más de 12 de 24.", "En bus van 8.", "8 no supera 12."], "No, porque 8 no es más de la mitad de 24."),
    ],
    [("Afirmar algo sin ningún dato que lo respalde.", "Se piensa que decirlo con seguridad basta.", "Agrega una cifra o un ejemplo que se pueda comprobar."), ("Exagerar: decir «todos» cuando son pocos.", "Se cree que suena más fuerte.", "Revisa el dato y usa la palabra exacta: «10 de 24».")],
    [
        E("Según la encuesta, ¿cuántos estudiantes van en bicicleta?", "2", "El dato está en la encuesta."),
        E("¿Cuántos estudiantes se preguntó en total?", "24", "Lo dice la primera oración."),
        E("¿Cuál es un dato: a) «Caminar es sano» b) «10 estudiantes caminan»?", "b", "Una cifra se puede comprobar."),
    ],
    [
        E("¿Qué dato respalda «Pocos estudiantes llegan en bicicleta»: a) 2 van en bicicleta b) 10 caminan?", "a", "Muestra que son pocos."),
        E("¿Cuál palabra es más precisa: a) «cosa» b) «casillero»?", "b", "Nombra exactamente el objeto."),
        E("Un dato pertinente es el que: a) apoya el planteamiento b) llama la atención aunque no se relacione?", "a", "Debe servir para respaldar la idea."),
    ],
    [
        arith("En la encuesta, 10 estudiantes caminan y 8 van en bus. ¿Cuántos usan una de esas dos formas?", "10+8", "Se suman ambos grupos.", " estudiantes"),
        arith("De los 24 estudiantes, 10 caminan. ¿Cuántos llegan de otra forma?", "24-10", "Se restan los que caminan al total.", " estudiantes"),
        E("Reemplaza la palabra vaga: «Nos reunimos en la cosa del patio». ¿Cuál es más precisa: a) «en el escenario del patio» b) «en eso del patio»?", "a", "Nombra el lugar con exactitud."),
    ],
    [
        E("Nico dice: «Casi todo el curso va en auto». Con los datos de la encuesta, ¿es correcto? Responde sí o no.", "No", "Solo 4 de 24 van en auto."),
        E("Para defender «Caminar es lo más frecuente», ¿qué ejemplo sería pertinente: a) «Camino 10 minutos hasta el colegio» b) «Tengo una mochila azul»?", "a", "Es un caso de llegar caminando."),
    ],
    [
        E("Con los datos de la encuesta, ¿qué afirmación se puede respaldar: a) «Más estudiantes caminan que van en bus.» b) «La mitad va en auto.»", "a", "Hay 10 que caminan y 8 en bus; en auto son 4 de 24, menos de la mitad."),
        E("Un expositor dice «un montón de estudiantes caminan». ¿Cómo lo diría con vocabulario preciso: a) «Diez de veinticuatro estudiantes caminan» b) «Muchos caminan harto»?", "a", "Da la cifra exacta."),
    ],
    [E("Quieres exponer que «Los estudiantes de 5.º B prefieren el patio a la biblioteca en el recreo». Tienes dos datos: 15 eligieron el patio y 9 eligieron la biblioteca. ¿Qué dato usas primero para respaldar tu idea?", "Que 15 eligieron el patio", "Es la cifra mayor y apoya la preferencia.")],
    [
        E("Un dato se puede comprobar. Responde sí o no.", "Sí", "Por eso respalda una idea."),
        E("¿Qué es mejor para fundamentar: un ejemplo con cifra o la frase «porque sí»?", "Un ejemplo con cifra", "Entrega una razón comprobable."),
        E("¿«Mayoría» significa más de la mitad? Responde sí o no.", "Sí", "Es más de la mitad del total."),
    ],
    ("Usa estos datos de una encuesta a 20 estudiantes sobre su materia favorita: Educación Física 9, Artes 6, Matemática 3, Lenguaje 2. Escribe un planteamiento (una idea que se pueda respaldar con estos datos) y dos datos o ejemplos que lo fundamenten. Luego escribe una frase del planteamiento usando una palabra precisa en lugar de «cosa» o «un montón». Practícalo en voz alta.",
     "Planteamiento: «La materia más elegida es Educación Física». Datos: 9 de 20 la eligieron, más que las otras tres. Dato 2: Artes quedó segunda con 6 votos, 3 menos. Frase: «Nueve de veinte estudiantes eligieron Educación Física».",
     ["el planteamiento se puede comprobar con los datos", "usa al menos dos datos o ejemplos", "emplea una palabra o cifra precisa"], ["planteamiento escrito", "dos datos o ejemplos", "frase con vocabulario preciso"], ["afirmar más de lo que dicen los datos", "usar palabras vagas"],
     "Si tu planteamiento no se puede respaldar, revisa los números: ¿qué sí permiten afirmar?"),
    "Cambia dos palabras vagas de una oración tuya por palabras exactas.",
    "Busca en un libro o diario una cifra y úsala para fundamentar una idea propia en una oración.",
)

# ================================================================ OA 28 · clase 4
reg(
    OA28, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar las versiones.",
    "Aprenderé a comparar oraciones y a elegir las que usan registro formal, construcciones variadas y verbos bien conjugados. Sirve para que mi exposición suene clara, variada y cuidada.",
    ["Sé que el registro formal se usa en una exposición.", "Sé unir ideas con conectores."],
    [
        "En una exposición usamos un registro formal, que es una manera de hablar cuidada y respetuosa. Evitamos expresiones muy familiares como «o sea», «po» o «cachai». Hablamos con oraciones completas, sin cortar las frases y sin repetir el «y» una y otra vez.",
        "Para variar las construcciones, reemplazamos oraciones cortas y parecidas por otras que unen las ideas. En lugar de «Hay basura. Contamina. Hay que limpiar», podemos decir «Como hay basura que contamina, hay que limpiar». También podemos cambiar el orden: «Después de ensayar tres veces, expuse con seguridad». Así el texto es más fluido.",
        "Los verbos deben estar bien conjugados. Algunos errores frecuentes: «habían muchas personas» (correcto: «había muchas personas», porque «haber» no varía cuando indica existencia), «hubieron» (correcto: «hubo»), «andé» (correcto: «anduve»), «dijistes» (correcto: «dijiste») y «yo sabo» (correcto: «yo sé»). Revisar la conjugación antes de exponer evita estos tropiezos.",
    ],
    [("registro formal", "manera de hablar cuidada y respetuosa"), ("construcción sintáctica", "forma de armar una oración"), ("conjugar", "dar al verbo su forma según persona y tiempo"), ("muletilla", "palabra repetida sin necesidad, como «o sea»"), ("fluido", "que se escucha seguido y natural")],
    [
        ("Corregir un verbo", "Un expositor dice: «En la sala habían muchas sillas». ¿Cómo se corrige?", ["El verbo «haber» indica que existen sillas.", "En ese uso no cambia con el plural.", "Se dice «había»."], "«En la sala había muchas sillas.»"),
        ("Unir oraciones", "Tres oraciones: «Hay basura. Contamina. Hay que limpiar». ¿Cómo las unes en una sola?", ["Busco la causa y la consecuencia.", "La basura contamina y por eso hay que limpiar.", "Uso «como» para unir."], "«Como hay basura que contamina, hay que limpiar.»"),
    ],
    [("Llenar la exposición de «o sea», «po» y «cachai».", "Son muletillas del habla familiar.", "Haz una pausa en vez de usarlas."), ("Decir «hubieron» o «habían» cuando indica existencia.", "Se confunde con el plural.", "Usa «hubo» y «había» en singular.")],
    [
        E("¿Cuál es correcta: a) «Hubo dos exposiciones.» b) «Hubieron dos exposiciones.»", "a", "«Hubo» no cambia al indicar existencia."),
        E("Corrige: «Ayer andé por el parque». ¿Qué forma es correcta?", "Anduve", "Es la forma del verbo andar en pasado."),
        E("¿«Po» es una expresión del registro formal o del familiar?", "Del familiar", "Es una expresión de la conversación entre cercanos."),
    ],
    [
        E("¿Cuál oración es de registro formal: a) «O sea, el tema es importante, po.» b) «El tema es importante porque afecta a todos.»", "b", "Evita muletillas y es completa."),
        E("¿Cuál está bien conjugada: a) «Tú dijistes la verdad.» b) «Tú dijiste la verdad.»", "b", "La forma correcta es «dijiste»."),
        E("¿Cuál opción cambia el orden para variar: a) «Después de ensayar tres veces, expuse con seguridad.» b) «Ensayé. Expuse. Fue bien.»", "a", "Une las ideas y cambia el orden."),
    ],
    [
        E("Une en una oración: «Ensayé. Mejoré. Hablé con calma». ¿Cuál es mejor: a) «Como ensayé, mejoré y hablé con calma.» b) «Ensayé, mejoré, hablé.»", "a", "Une las ideas de manera fluida."),
        E("Corrige el verbo: «Yo sabo la respuesta». ¿Cómo se dice?", "Yo sé la respuesta", "La primera persona de «saber» es «sé»."),
        E("Ordena para formar una oración con cambio de orden: a) hablé con claridad b) Después de practicar c) frente al curso. Escribe las letras.", "b, a, c", "Se ordena: Después de practicar, hablé con claridad frente al curso."),
    ],
    [
        E("Una expositora dice: «Habían doce estudiantes y hubieron preguntas». ¿Cuál es la corrección completa: a) «Había doce estudiantes y hubo preguntas.» b) «Habían doce estudiantes y hubo preguntas.»", "a", "Ambos verbos se usan en singular."),
        E("Comparando «Hay agua. Se desperdicia. Hay que cuidarla» con «Como el agua se desperdicia, hay que cuidarla», ¿cuál usa una construcción más variada y por qué?", "La segunda, porque une las ideas", "La primera son tres oraciones cortas y parecidas."),
    ],
    [
        E("Tres versiones sobre el reciclaje: A) «Reciclar es bueno, po, o sea, ayuda.» B) «Reciclar es bueno porque ayuda a cuidar el ambiente.» C) «Reciclar bueno ayuda.» ¿Cuál es la mejor para una exposición y por qué?", "La B, porque es completa y formal", "La A tiene muletillas y la C es incompleta."),
        E("Corrige todos los errores: «Cuando fuimos al museo, habían muchos niños y yo andé con mi curso». ¿Qué versión es correcta: a) «Cuando fuimos al museo, había muchos niños y yo anduve con mi curso.» b) «Cuando fuimos al museo, habían muchos niños y yo anduve con mi curso.»", "a", "Se corrigen «había» y «anduve»."),
    ],
    [E("Debes exponer ante la directora. Elige la frase de apertura más adecuada: a) «Hola, o sea, hoy voy a hablar de, bueno, del reciclaje.» b) «Buenos días, directora y compañeros. Hoy expondré sobre el reciclaje en nuestro colegio.»", "b", "Saluda, nombra al público y usa un registro cuidado.")],
    [
        E("¿«Hubo» o «hubieron» se usa para indicar existencia en singular?", "Hubo", "No cambia aunque el sustantivo esté en plural."),
        E("Una muletilla se repite sin necesidad. Responde sí o no.", "Sí", "Por eso conviene evitarla."),
        E("¿Unir oraciones cortas con «porque» o «como» las hace más fluidas? Responde sí o no.", "Sí", "Relaciona las ideas."),
    ],
    ("Corrige este texto para una exposición: «Hoy voy a hablar de, o sea, los gatos, po. Habían muchos gatos en mi barrio. Yo andé mirándolos. Son tranquilos. Duermen mucho. Me gustan.» Reescríbelo en registro formal: sin muletillas, con verbos bien conjugados y uniendo al menos dos pares de oraciones. Léelo en voz alta.",
     "«Hoy hablaré de los gatos. En mi barrio había muchos gatos y anduve mirándolos. Como son tranquilos y duermen mucho, me gustan».",
     ["quita las muletillas", "corrige «habían» y «andé»", "une al menos dos pares de oraciones"], ["texto reescrito"], ["dejar muletillas", "olvidar corregir los verbos"],
     "Si algo suena familiar, pregúntate si lo diría ante la directora."),
    "Escribe tres oraciones cortas y únelas en una sola con un conector.",
    "Escucha una exposición o noticia y anota una muletilla que se repita.",
)

# ================================================================ OA 28 · clase 5
reg(
    OA28, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: un papelógrafo casero (una hoja grande) y una persona de tu casa para practicar.",
    "Aprenderé a cuidar la voz, las pausas, los gestos, la postura y el material de apoyo (papelógrafo, presentación, objetos) para que mi exposición se escuche y se vea bien. Sirve para ser claro ante la audiencia.",
    ["Sé que una exposición tiene tres partes.", "Sé usar un registro formal."],
    [
        "Además de lo que decimos, importa cómo lo decimos. Pronunciar claramente significa decir cada palabra completa. El volumen debe ser audible, es decir, que se oiga desde el último puesto sin gritar. La entonación es la subida y bajada de la voz; evita que hablemos como robots. Las pausas son breves silencios que marcan el cambio de idea, y el énfasis es decir con más fuerza la palabra clave.",
        "El cuerpo también comunica. La postura debe ser derecha y relajada, de frente a la audiencia. Los gestos acompañan las palabras: mostrar un número con los dedos, señalar un dibujo. Hay que mirar a distintas personas del público y evitar gestos que distraigan, como jugar con el lápiz o taparse la cara.",
        "El material de apoyo ayuda a que se comprenda mejor. Puede ser un papelógrafo, una presentación de diapositivas u objetos. Para que sea efectivo debe ser legible desde lejos, con letra grande y pocas palabras. No es una hoja para leer en voz alta: es un apoyo para recordar y mostrar. Una imagen o un objeto bien elegido vale más que un párrafo completo.",
    ],
    [("volumen audible", "que se escucha desde el último puesto"), ("entonación", "subida y bajada de la voz al hablar"), ("pausa", "breve silencio que separa ideas"), ("énfasis", "mayor fuerza en una palabra clave"), ("material de apoyo", "recurso visual que ayuda a explicar")],
    [
        ("Elegir material efectivo", "Para exponer sobre el ajedrez tienes dos láminas. A: «Ajedrez: tablero de 64 casillas», con un dibujo grande del tablero. B: un párrafo de diez líneas copiado del libro. ¿Cuál es más efectiva?", ["Veo cuál se lee desde lejos.", "A tiene pocas palabras y una imagen.", "B obliga a leer mucho."], "La A."),
        ("Usar pausas", "En «Primero, / separamos el papel; / después, / lo pesamos», las barras marcan pausas. ¿Qué ayudan a hacer?", ["Observo dónde están: después de cada idea.", "Separan los momentos de la explicación.", "Ayudan a que la audiencia siga el orden."], "Marcar el cambio de idea y facilitar que se entienda."),
    ],
    [("Leer la lámina completa en voz alta dando la espalda al público.", "Se piensa que el material debe contener todo el discurso.", "Usa pocas palabras, mira al público y explica con tus palabras."), ("Hablar en voz muy baja y rápido por nervios.", "Se quiere terminar pronto.", "Respira, haz pausas y sube un poco el volumen.")],
    [
        E("Si no se te oye desde el último puesto, ¿qué debes mejorar: el volumen o el color de la lámina?", "El volumen", "El volumen debe ser audible."),
        E("¿Qué hacen las pausas: marcan el cambio de idea o hacen más largo el recreo?", "Marcan el cambio de idea", "Ayudan a seguir la exposición."),
        E("¿Dónde debes mirar mientras expones: a distintas personas de la audiencia o solo el suelo?", "A distintas personas de la audiencia", "La mirada conecta con el público."),
    ],
    [
        E("¿Qué es el énfasis: a) decir con más fuerza la palabra clave b) hablar siempre igual?", "a", "Destaca lo más importante."),
        E("Un papelógrafo efectivo tiene: a) letra grande y pocas palabras b) letra chica y mucho texto?", "a", "Debe leerse desde lejos."),
        E("¿Qué gesto acompaña bien una palabra: mostrar con los dedos «tres» al decir «tres pasos» o taparse la cara?", "Mostrar con los dedos «tres» al decir «tres pasos»", "El gesto refuerza lo que se dice."),
    ],
    [
        E("Una lámina tiene el título «Reciclar papel: caja azul, pesaje semanal». ¿Cuántas palabras tiene?", "6", "Son: reciclar, papel, caja, azul, pesaje y semanal."),
        E("Tu lámina tiene 40 palabras con letra chica. ¿Cuál es el mejor arreglo: a) dejar cinco palabras con letra grande y un dibujo b) leerla más rápido?", "a", "Pocas palabras y letra grande se leen desde lejos."),
        E("¿Qué conviene hacer con las manos al exponer: a) jugar con el lápiz b) usarlas para señalar el dibujo?", "b", "Los gestos deben apoyar lo que se dice."),
    ],
    [
        E("Un compañero lee de corrido su lámina, de espaldas al curso. ¿Qué dos aspectos fallan: a) postura y contacto visual b) solo el título?", "a", "Debe estar de frente y mirar al público."),
        E("Dos exposiciones: la primera habla muy bajo y la segunda sube y baja la voz y hace pausas. ¿Cuál usa mejor entonación y pausas?", "La segunda", "Varía la voz y marca las ideas."),
    ],
    [
        E("Para exponer sobre la bicicleta, ¿qué objeto es un buen material de apoyo seguro y sencillo: a) un casco de ciclista para mostrar cómo se ajusta b) una herramienta cortante?", "a", "Es seguro y ayuda a explicar."),
        E("Tienes un papelógrafo con el título y un dibujo grande. Notas que desde atrás no se ve. ¿Qué haces: a) agrandas la letra y la imagen b) hablas más rápido?", "a", "Se arregla lo que impide que se lea."),
    ],
    [E("Vas a exponer ante tu curso con una lámina que dice «Cuidar el agua». Ordena lo que haces. a) hablar con volumen audible b) revisar que la letra se vea desde atrás c) ensayar con pausas y énfasis. Escribe las letras.", "b, c, a", "Primero se prepara el material, luego se ensaya y después se expone con la voz adecuada.")],
    [
        E("¿Un buen material de apoyo tiene pocas palabras o un párrafo largo?", "Pocas palabras", "Debe leerse rápido y desde lejos."),
        E("La postura recomendada, ¿es de frente a la audiencia?", "Sí", "Así te escuchan y te ven mejor."),
        E("¿El volumen debe ser tan alto que parezca un grito? Responde sí o no.", "No", "Debe ser audible, no gritado."),
    ],
    ("Prepara el material de apoyo para exponer sobre «Mi juego favorito» con una hoja grande o dibujada en tu cuaderno: un título de máximo cinco palabras y un dibujo claro. Luego escribe tres frases para ensayar y marca con una barra / dónde harás pausas y subraya la palabra clave de cada frase. Ensaya ante una persona de tu casa y pídele que diga si te oyó y te vio bien.",
     "Título: «Rayuela: juego de saltos». Frase: «Primero, / se dibuja con tiza en el suelo; / luego, / se salta en un pie». Palabras clave: «saltos», «tiza», «salta».",
     ["título de máximo cinco palabras", "pausas y palabras clave marcadas", "la persona pudo oír y ver bien"], ["material elaborado", "frases ensayadas con marcas"], ["escribir demasiado texto", "ensayar sin marcar pausas"],
     "Si te cuesta oír tus pausas, haz una más larga después de cada idea."),
    "Dibuja una lámina para exponer sobre un tema de tu elección con título corto e imagen.",
    "Mira a alguien que hable en público (presentación, noticias) y anota dos recursos de voz o gestos que use.",
)

# ================================================================ OA 28 · clase 6
reg(
    OA28, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para dar retroalimentación sobre tu versión mejorada.",
    "Aprenderé a revisar una exposición con una pauta, dar y recibir retroalimentación y mejorar mi versión. Sirve para que mi próxima presentación sea más clara y fundamentada.",
    ["Sé las partes de una exposición.", "Sé usar conectores, datos y ejemplos.", "Sé cuidar voz, gestos y material."],
    [
        "Revisar una exposición es compararla con una pauta de criterios. Una pauta puede tener estas preguntas: ¿tiene introducción, desarrollo y cierre?, ¿las ideas están ordenadas y unidas?, ¿hay datos o ejemplos?, ¿el vocabulario es preciso y el registro formal?, ¿los verbos están bien conjugados? y ¿se cuidan la voz, los gestos y el material? Cada respuesta se apoya en lo que se dijo.",
        "La retroalimentación debe ser específica, amable y útil. Primero se dice un logro, luego algo que mejorar y se propone un cambio. Por ejemplo: «Tu saludo fue claro. Podrías agregar un dato después de decir que las plantas necesitan luz». Un comentario como «estuvo mal» no ayuda porque no dice qué cambiar.",
        "Para mejorar, tomamos un criterio y reescribimos o ensayamos una parte. Después comparamos las dos versiones. Mejorar un texto es una decisión: elegimos qué cambiar y por qué. Una segunda versión no siempre queda perfecta, pero debe ser mejor que la primera en el criterio revisado.",
    ],
    [("pauta", "lista de criterios para evaluar"), ("retroalimentación", "comentario que ayuda a mejorar"), ("logro", "algo que salió bien"), ("versión", "forma en que se presenta un texto"), ("criterio", "aspecto que se mira al revisar")],
    [
        ("Revisar con la pauta", "Exposición de Raúl: «Hola. Yo voy a hablar de las plantas. Las plantas son importantes. Las plantas necesitan agua. Las plantas necesitan luz. Bueno, eso es todo». ¿Qué criterio de la pauta no cumple en el cierre?", ["Miro la última frase.", "Dice «Bueno, eso es todo».", "No resume ni agradece."], "No resume lo principal ni agradece."),
        ("Dar retroalimentación", "¿Qué comentario ayuda a Raúl: a) «Estuvo mal.» b) «Tu tema se entiende. Agrega un ejemplo de cuánta agua necesita una planta y une las frases con conectores.»?", ["Busco el que dice un logro, algo que mejorar y un cambio.", "La b nombra el logro y propone mejoras.", "La a no dice qué cambiar."], "La b."),
    ],
    [("Dar retroalimentación diciendo solo «me gustó» o «no me gustó».", "No se piensa en cómo ayudar.", "Di un logro, algo que mejorar y un cambio posible."), ("Cambiar todo en la segunda versión.", "Se quiere arreglar demasiado a la vez.", "Elige un criterio y mejora esa parte primero.")],
    [
        E("En la exposición de Raúl, ¿cuántas veces aparece la expresión «las plantas»? Cuenta también la de la oración que anuncia el tema.", "Cuatro", "Aparece en «Yo voy a hablar de las plantas» y al comienzo de las otras tres oraciones."),
        E("¿Qué le falta al texto de Raúl en el desarrollo: ejemplos y datos o saludo?", "Ejemplos y datos", "Solo dice ideas generales."),
        E("¿Raúl anuncia el tema en la introducción? Responde sí o no.", "Sí", "Dice «Yo voy a hablar de las plantas»."),
    ],
    [
        E("¿Qué criterio de la pauta se ve afectado por repetir «Las plantas» al inicio de cada oración: la cohesión o el volumen?", "La cohesión", "Faltan conectores y reemplazos que unan las ideas."),
        E("La retroalimentación útil incluye: a) un logro, algo que mejorar y un cambio b) solo una crítica?", "a", "Así ayuda a mejorar sin desanimar."),
        E("¿Qué dato ayudaría a fundamentar «Las plantas necesitan agua»: a) «Una planta sin agua se seca» b) «Hoy es martes»?", "a", "Explica por qué el agua es necesaria."),
    ],
    [
        E("Mejora la primera oración de Raúl con un conector: «Las plantas necesitan agua. ______, necesitan luz.» Opciones: Además / En resumen.", "Además", "Agrega otra necesidad."),
        E("Ordena un cierre mejorado. a) Gracias por escucharme. b) En resumen, las plantas necesitan agua y luz para vivir. Escribe las letras.", "b, a", "Primero resume y luego agradece."),
        E("¿Cuál introducción es mejor para Raúl: a) «Hola. Plantas.» b) «Buenos días, compañeros. Hoy les explicaré qué necesitan las plantas para vivir.»", "b", "Saluda, nombra a la audiencia y anuncia el tema."),
    ],
    [
        E("Dos compañeros comentan la exposición de Raúl. Uno dice: «Tu tema fue claro. Agrega un ejemplo». Otro dice: «No me gustó». ¿Cuál comentario sirve para mejorar y por qué?", "El primero, porque dice un logro y un cambio", "El segundo no señala qué cambiar."),
        E("Raúl cambia solo el cierre y mejora esa parte. ¿Mejoró la exposición completa o solo el criterio revisado?", "Solo el criterio revisado", "Faltan los otros criterios por mejorar."),
    ],
    [
        E("Versión mejorada de Raúl: «Buenos días, compañeros. Hoy les explicaré qué necesitan las plantas. Primero, necesitan agua; por ejemplo, una planta sin agua se seca. Además, necesitan luz. En resumen, el agua y la luz las mantienen vivas. Gracias». ¿Cuántos conectores distintos tiene el texto?", "Cuatro", "Se cuentan primero, por ejemplo, además y en resumen."),
        E("En la versión mejorada, ¿qué frase funciona como resumen del cierre?", "«En resumen, el agua y la luz las mantienen vivas»", "Repite lo central antes de agradecer."),
    ],
    [E("Escuchas una exposición y notas que el expositor habla muy rápido, sin pausas. Redacta la mejor retroalimentación: a) «Tu tema es interesante. Haz pausas entre ideas para que podamos seguirte.» b) «Hablas mal.»", "a", "Dice un logro, un problema y un cambio.")],
    [
        E("¿La retroalimentación debe decir qué cambiar? Responde sí o no.", "Sí", "Debe ser específica y útil."),
        E("¿La pauta se compara con lo que se dijo en la exposición? Responde sí o no.", "Sí", "Cada criterio se apoya en evidencia."),
        E("¿Conviene mejorar un criterio a la vez o intentar cambiar todo?", "Un criterio a la vez", "Es más fácil comprobar el avance."),
    ],
    ("Lee esta exposición: «Hola. Hoy hablaré del reciclaje. El reciclaje sirve. Hay cajas. Gracias». Revísala con la pauta (introducción, desarrollo, cierre, datos y ejemplos, conectores, registro) y haz tres cosas: 1) escribe dos criterios que cumple y dos que no, con la frase que lo muestra; 2) redacta una retroalimentación amable con un logro, algo que mejorar y un cambio; 3) escribe una segunda versión mejorada de dos o tres oraciones, con un dato o ejemplo y un conector.",
     "1) Cumple: anuncia el tema (dice «Hoy hablaré del reciclaje») y cierra con «Gracias». No cumple: faltan datos y ejemplos; las oraciones son cortas sin conectores. 2) «Anunciaste claramente el tema. Agrega un ejemplo de qué se recicla y une las frases con ‘además’». 3) «Hoy hablaré del reciclaje. Por ejemplo, el papel se separa en una caja azul y, además, se pesa cada viernes».",
     ["revisa con criterios y evidencia", "la retroalimentación tiene logro, mejora y cambio", "la segunda versión corrige al menos un criterio"], ["revisión escrita", "retroalimentación", "versión mejorada"], ["revisar sin citar frases", "retroalimentación solo crítica"],
     "Si tu segunda versión se parece a la primera, elige un criterio y cámbialo de forma visible."),
    "Elige una exposición que hayas hecho antes y revisa con la pauta dos criterios.",
    "Pide a una persona de tu casa que escuche tu exposición y te diga un logro y una mejora; anota cómo la aplicarás.",
)

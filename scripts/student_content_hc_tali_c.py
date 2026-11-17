"""Taller de literatura (electivo 3.º y 4.º medio HC): OAC-05 (trayectorias de lectura y criterios de selección, clases 1 a 4) y OAC-06 (producir reflexiones sobre sí mismos y el mundo a partir de las lecturas, clases 1 a 6)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todas las obras, fichas, pasajes y casos de los ejercicios son inventados para este cuaderno (no son libros reales) y están escritos completos en el enunciado: no necesitas libros ni internet. "
             "Para armar tu trayectoria real de lectura usarás los libros que te recomienden tu docente, tu biblioteca o tu familia; este cuaderno no los reproduce. "
             "En las reflexiones sobre ti mismo o sobre el mundo, comparte solo lo que quieras compartir y no cuentes cosas íntimas de otras personas. Si una lectura o un recuerdo te angustia, habla con una persona adulta de confianza, como tu docente o alguien de tu casa.")
build = make_build(MATERIALS)

O5 = "LL-TALI-3y4-OAC-05"
O6 = "LL-TALI-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (obras inventadas para este ejercicio; no son libros reales). A) «La casa del mar quieto», novela sobre una familia que espera noticias de un viaje. B) «Cartas desde el sur», poemas escritos como cartas de alguien que viaja. "
     "C) «El guardián de los relojes», cuentos fantásticos sobre el tiempo. D) «Mapas de papel», crónicas sobre barrios de una ciudad. E) «Voces del cerro», cuentos sobre vecinos de un cerro. F) «Despedidas», microrrelatos sobre personas que se van. "
     "Lectora de ejemplo: Camila, a quien le interesan los viajes y las despedidas.")
build(
    O5, 1, F,
    use="Aprenderé qué es una trayectoria de lectura y cómo se arma con un hilo: un tema, un género, un autor o autora, una época o una pregunta. Sirve para leer con dirección propia y no solo por lo que me toque.",
    prior=["Sé qué es un género literario.", "Sé qué es un tema.", "Sé que leer puede hacerse por interés propio."],
    explain=[
        "Una trayectoria de lectura es un recorrido de obras elegidas por una persona, con un orden y una razón. No es una lista al azar ni el plan lector obligatorio: surge de los intereses, gustos e inquietudes de quien lee. Lo que une las obras es un hilo, es decir, un rasgo que se repite o que se explora de una obra a otra.",
        "Un hilo puede ser un tema (el viaje, la espera, la ciudad), un género (cuentos fantásticos, poesía), un autor o autora, una época, un lugar o una pregunta («¿qué hace que alguien se quede o se vaya?»). El hilo tema suele ser el más flexible porque permite pasar de una novela a un poema o a una crónica. Con un buen hilo, cada obra nueva dialoga con las anteriores.",
        "Armar una trayectoria exige tres decisiones: elegir el hilo, elegir las obras que lo recorren y justificar cada elección. La justificación responde: ¿por qué esta obra, y por qué después de esta otra? Si no hay hilo, la lista se queda en una suma de lecturas sueltas. Tu trayectoria puede cambiar durante el camino: es normal descubrir una obra que abre otro hilo.",
    ],
    vocab=[("trayectoria de lectura", "recorrido de obras elegidas por una persona, con orden y razones"), ("hilo", "rasgo que une las obras de una trayectoria: tema, género, autor, época o pregunta"), ("corpus", "conjunto de obras que se leen o se estudian"), ("criterio de selección", "razón con que se elige o se descarta una obra"), ("inquietud", "pregunta o interés que mueve a leer")],
    worked=[
        ("Elegir obras para un hilo", "El hilo de Camila es «viajes y despedidas». ¿Qué obras de la ficha lo recorren?",
         ["A trata de una familia que espera noticias de un viaje.", "B está escrita como cartas de alguien que viaja.", "F trata de personas que se van.", "C, D y E no tratan de viaje ni de despedidas."],
         "A, B y F"),
        ("Distinguir lista y trayectoria", "Un estudiante dice: «mi trayectoria es leer lo que me caiga en las manos». ¿Es una trayectoria?",
         ["Una trayectoria requiere un hilo y razones.", "Leer al azar no tiene un hilo que una las obras.", "Es una lista de lecturas, no una trayectoria."],
         "No: falta un hilo y razones"),
    ],
    mistakes=[("Confundir trayectoria con el plan lector que entrega el colegio.", "La trayectoria surge de intereses propios, aunque puede incluir lecturas del plan.", "Parte de tu inquietud y elige obras que la exploren."),
              ("Armar una lista de obras sin explicar qué las une.", "Sin hilo y razones no hay trayectoria, solo una suma de lecturas.", "Escribe en una frase el hilo y justifica cada obra.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una trayectoria de lectura?", "Un recorrido de obras elegidas por una persona, con un orden y razones", "La lista de libros que ordena la biblioteca", "Un libro muy extenso", "La trayectoria surge de intereses propios y tiene un hilo que une las obras."),
        ("{F} ¿Cuántas obras inventadas hay en la ficha?", "6", "Las obras son A, B, C, D, E y F: seis."),
        ("{F} ¿Qué obra tiene forma de cartas?", "B", "«Cartas desde el sur» está escrita como cartas de alguien que viaja."),
        ("abc", "{F} ¿Cuál es el hilo de Camila?", "Los viajes y las despedidas", "El género de la novela", "Los barrios de una ciudad", "La ficha dice que le interesan los viajes y las despedidas."),
        ("abc", "{F} ¿Qué obra encaja con el hilo de Camila y es un microrrelato?", "F, «Despedidas»", "D, «Mapas de papel»", "C, «El guardián de los relojes»", "F es de microrrelatos sobre personas que se van, que es el hilo de Camila."),
        ("ab", "{F} ¿La obra E, «Voces del cerro», encaja con el hilo de Camila?", "No: trata de vecinos de un cerro, sin viajes ni despedidas", "Sí: todas las obras de la ficha encajan", "Según la ficha, E trata de vecinos, no de viaje ni despedida."),
        ("abc", "{F} Un estudiante cambia el hilo de Camila por «el tiempo». ¿Qué obra encajaría?", "C, porque trata del tiempo", "D, porque trata de barrios", "B, porque son poemas", "C es de cuentos sobre el tiempo, que sería el nuevo hilo."),
        ("abc", "{F} Camila quiere pasar del tema viajes al género poesía. ¿Qué obra le sirve de puente?", "B, porque es poesía y también trata de viaje", "D, porque es crónica", "E, porque son cuentos", "B reúne el tema viaje y el género poesía."),
        ("ab", "{F} Un amigo dice que la trayectoria de Camila podría incluir C porque «el tiempo también pasa en los viajes». ¿Es una razón válida?", "Es una razón posible si la explica y la relaciona con el hilo", "No, porque nunca se puede cambiar el hilo", "Una trayectoria admite obras que dialoguen con el hilo si se justifican."),
        ("abc", "{F} Elige la justificación más completa para incluir A en la trayectoria de Camila.", "«Incluyo A porque trata de una familia que espera noticias de un viaje, así que explora la espera que suele seguir a una despedida»", "«Incluyo A porque es una novela»", "«Incluyo A porque estaba en la lista»", "Solo la primera relaciona la obra con el hilo y explica qué aporta."),
        ("abc", "{F} Camila ya leyó B y F. ¿Qué obra puede leer después para sumar un género distinto con el mismo hilo?", "A, porque es una novela sobre un viaje", "E, porque suma el género cuento", "D, porque suma el género crónica", "A suma el género novela sin salir del hilo; E y D suman géneros, pero no tratan de viajes ni de despedidas."),
        ("abc", "{F} Una estudiante dice: «mi hilo será leer libros gruesos». ¿Qué problema tiene?", "Se basa en la forma del libro y no en una inquietud de lectura", "Es un hilo demasiado interesante", "No tiene ningún problema", "Un buen hilo responde a una inquietud, no solo al tamaño del libro."),
        ("{F} Completa con una letra de la ficha: la obra de crónicas sobre barrios es la ____.", "D", "«Mapas de papel» es la obra de crónicas de barrios."),
    ],
    ctx=("abc", "Contexto: tu biblioteca te permite pedir prestadas dos obras de la lista de la ficha {F}, y quieres armar una mini trayectoria con el hilo «la vida en un barrio». ¿Qué dos eliges?", "D y E, porque muestran barrios y vecinos", "A y B, porque son las primeras de la lista", "C y F, porque son las más distintas entre sí", "Las obras elegidas deben unirse por el hilo del barrio; D trata de barrios y E de vecinos de un cerro."),
    sc=[
        ("En Taller de literatura: ¿qué es un hilo en una trayectoria de lectura?", "Un rasgo que une las obras: tema, género, autor, época o pregunta", "El hilo da unidad al recorrido y orienta la elección de obras."),
        ("ab", "Una trayectoria de lectura se arma desde:", "Los intereses e inquietudes de quien lee", "Un plan que no admite cambios", "Surge de lo que le importa a quien lee y puede cambiar."),
        ("ab", "Una lista de lecturas sin razones es:", "Una suma de lecturas sueltas", "Una trayectoria completa", "Sin hilo ni razones, no hay trayectoria."),
    ],
    op=("Con las seis obras inventadas de la ficha {F}: (1) elige un hilo propio (puede ser distinto al de Camila); (2) escoge tres obras que lo recorran y ordénalas; (3) escribe una razón de una oración para cada una.",
        "(1) Hilo: lugares y personas que los habitan. (2) E, D, A. (3) E, porque cuenta a vecinos de un cerro; D, porque muestra barrios de una ciudad; A, porque muestra una casa y su familia.",
        ["hilo claro", "tres obras de la ficha ordenadas", "razón por obra", "razones relacionadas con el hilo"],
        ["hilo, tres obras y tres razones"],
        ["elegir obras sin relación con el hilo", "razones como «porque sí»", "repetir una obra"],
        "Pregunta: «¿qué cuarta obra inventarías para tu hilo y qué tendría?»."),
    reinforce="Escribe dos hilos distintos que se podrían armar con las seis obras de la ficha y las obras que usarías en cada uno.",
    extend="Explica en qué se diferencia una trayectoria de lectura del plan lector de un curso, y cómo se pueden complementar.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (criterios de ejemplo de un lector). K1) Me interesa el tema del mar. K2) Quiero un libro que me desafíe un poco más que el anterior. K3) Quiero variar de género. K4) Me lo recomendó alguien que conoce mis gustos. K5) Tengo catorce días para leerlo. "
     "Obra candidata (inventada): «La casa del mar quieto», novela de 240 páginas.")
build(
    O5, 2, F,
    use="Aprenderé a explicitar los criterios con que elijo mis lecturas: interés, desafío, variedad, recomendaciones y tiempo. Sirve para justificar mi trayectoria y compartirla con claridad.",
    prior=["Sé qué es una trayectoria de lectura y un hilo.", "Sé calcular páginas por día.", "Sé que elegir exige razones."],
    explain=[
        "Un criterio de selección es una razón con la que decides elegir o descartar una obra. Todos tenemos criterios, pero muchas veces no los decimos: «me llamó la atención la portada». Explicitar un criterio es nombrarlo con claridad: «elijo esta novela porque su tema, el mar, me interesa». Ponerlo en palabras permite comprobar si es una buena razón y compartirlo con otras personas.",
        "Algunos criterios frecuentes son: el interés por un tema o género; el desafío, es decir, que la obra exija un poco más que la anterior; la variedad, para no leer siempre lo mismo; la recomendación de alguien de confianza; y las condiciones prácticas, como el tiempo y la extensión. Un buen conjunto de criterios no se contradice: no puedes elegir un libro «corto y fácil» y a la vez uno que «exija mucho».",
        "Los criterios sirven para planificar. Si una obra tiene 240 páginas y dispones de 14 días, calculas cuántas páginas debes leer por día: más de 17. Si vas a leer solo 15 páginas diarias, sabrás que en 14 días leerás 210 páginas y no alcanzarás. También puedes elegir otra obra o ampliar el plazo. Elegir con criterio no es renunciar al gusto: es sumar razones al gusto.",
    ],
    vocab=[("criterio de selección", "razón con la que se elige o se descarta una obra"), ("explicitar", "decir con claridad algo que estaba implícito"), ("desafío", "dificultad que invita a crecer como lector"), ("variedad", "diferencia de géneros, temas o autores entre las obras"), ("recomendación", "sugerencia de una persona sobre una obra")],
    worked=[
        ("Aplicar un criterio de tiempo", "Tienes catorce días y la obra tiene 240 páginas. Lees 20 páginas por día. ¿Alcanza?",
         ["En catorce días lees 20 por 14, es decir, 280 páginas.", "280 es mayor que 240."],
         "Sí, alcanza"),
        ("Explicitar un criterio", "Eliges una novela porque «me da curiosidad». ¿Cómo lo explicitas mejor?",
         ["Identifica qué te da curiosidad: el tema del mar.", "Conviértelo en criterio: elijo por el tema que me interesa.", "Escribe: elijo esta novela porque su tema, el mar, me interesa."],
         "Elijo esta novela porque su tema, el mar, me interesa"),
    ],
    mistakes=[("Elegir una obra «porque sí» y no poder explicar la razón.", "Sin criterio explícito no se puede compartir ni revisar la elección.", "Escribe una frase con «porque» que diga el criterio."),
              ("Usar criterios que se contradicen, como «corta» y «que me desafíe mucho» a la vez.", "Los criterios deben poder cumplirse juntos para guiar una elección.", "Revisa que tus criterios no se opongan y prioriza uno si lo hacen.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es un criterio de selección de una obra?", "Una razón con la que elijo o descarto una lectura", "El precio del libro", "El número de capítulos", "El criterio es la razón que justifica la elección de una obra."),
        ("{F} ¿Cuántos criterios de ejemplo tiene la ficha?", "5", "La ficha enumera K1, K2, K3, K4 y K5: cinco."),
        ("{F} ¿Cuántas páginas tiene «La casa del mar quieto»?", "240", "La ficha dice que la novela tiene 240 páginas."),
        ("abc", "{F} ¿Qué criterio cumple «La casa del mar quieto» si el lector se interesa por el mar?", "K1", "K3", "K5", "K1 se refiere al interés por el tema del mar."),
        ("abc", "{F} Un lector ya leyó solo poesía en el último mes. ¿Qué criterio justificaría elegir la novela?", "K3, variar de género", "K1, porque la poesía no tiene mar", "K5, porque la novela es breve", "La novela es un género distinto de la poesía, así que cumple con la variedad."),
        ("=", "{F} Si lees 16 páginas por día durante catorce días, ¿cuántas páginas lees?", "16*14", "Se multiplica el ritmo diario por los días disponibles.", " páginas"),
        ("=", "{F} Con 224 páginas leídas en catorce días, ¿cuántas páginas de la novela quedan sin leer?", "240-224", "Se resta lo leído al total de páginas.", " páginas"),
        ("abc", "{F} ¿Qué decisión es coherente con el criterio K5 si lees 16 páginas por día?", "Ampliar el plazo o elegir una obra más breve", "Ignorar el plazo", "Leer solo el comienzo y decir que terminaste", "Si no alcanza, hay que ajustar el plazo o la obra."),
        ("=", "{F} Si quieres terminar la novela exactamente en doce días, leyendo lo mismo cada día, ¿cuántas páginas debes leer por día?", "240//12", "Se reparte el total de páginas entre los días.", " páginas"),
        ("ab", "{F} Un lector dice: «quiero variar de género, pero leer solo cuentos como siempre». ¿Qué problema tiene?", "Sus criterios se contradicen, porque variar de género se opone a leer siempre el mismo", "Ninguno, porque se puede cumplir todo", "No se puede variar de género y leer solo cuentos como siempre, así que los criterios chocan."),
        ("abc", "{F} Una amiga te recomienda la novela porque conoce tus gustos. ¿Qué criterio es?", "K4, la recomendación", "K2, el desafío", "K5, el tiempo", "La recomendación de alguien que conoce tus gustos es un criterio válido."),
        ("abc", "{F} Elige el conjunto de criterios más coherente para tu próxima lectura.", "Tema que me interesa, un poco más difícil que la anterior y que quepa en dos semanas", "Que sea muy corto, muy difícil y muy distinto", "Que sea el más grueso de la biblioteca", "Los tres criterios del primer conjunto se pueden cumplir a la vez."),
        ("abc", "{F} Dos lectores leen la misma novela con criterios distintos: uno por el tema del mar, el otro por el desafío. ¿Qué pasa?", "Pueden elegir la misma obra por razones distintas", "Es imposible que coincidan", "Uno de los dos está equivocado", "Una obra puede cumplir varios criterios."),
    ],
    ctx=("abc", "Contexto: en la biblioteca de tu liceo debes decidir entre dos obras para las vacaciones de invierno, de 14 días, y solo puedes llevar una. Una tiene 230 páginas y la otra 300. Lees 18 páginas por día. ¿Qué criterio práctico decide?", "El tiempo: en 14 días lees 252 páginas, así que la de 230 alcanza y la de 300 no", "La portada más llamativa", "La que tenga más personajes", "18 por 14 es 252: la obra de 230 páginas cabe en el plazo y la de 300 no."),
    sc=[
        ("En Taller de literatura: ¿qué significa explicitar un criterio?", "Decir con claridad la razón de una elección", "Explicitar es poner en palabras algo que antes era implícito."),
        ("ab", "Los criterios de una lectura deben:", "Poder cumplirse a la vez", "Contradecirse entre sí", "Criterios que se oponen impiden decidir."),
        ("ab", "El tiempo disponible es un criterio:", "Práctico que influye en qué obra se elige", "Que no importa al elegir", "La extensión y el plazo condicionan la lectura."),
    ],
    op=("Con la ficha {F} como modelo, escribe tus propios criterios de selección para tu próxima lectura: (1) tres criterios distintos, que no se contradigan; (2) una obra real o inventada que los cumpla, nombrada por ti; (3) un cálculo de cuántas páginas leerías por día si la obra tuviera 180 páginas y tienes 12 días.",
        "(1) Me interesa el misterio; quiero algo un poco más largo que lo último que leí; quiero variar de género. (2) «El guardián de los relojes» (inventado). (3) 180 dividido en 12 es 15 páginas por día.",
        ["tres criterios distintos y coherentes", "obra que los cumple", "cálculo correcto de páginas por día", "criterios explicitados con claridad"],
        ["tres respuestas numeradas"],
        ["criterios que se contradicen", "no explicar por qué la obra los cumple", "cálculo incorrecto"],
        "Pregunta: «¿qué criterio cambiarías si tuvieras la mitad del tiempo?»."),
    reinforce="Escribe tres criterios de selección de lectura que no usaste en esta clase y una obra que los cumpliría.",
    extend="Explica por qué explicitar los criterios con que eliges lecturas ayuda a descubrir qué tipo de lector eres.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (trayectoria de ejemplo, de un lector inventado). Diego declara su hilo: «leer sobre lugares y las personas que los habitan». Sus cinco obras, en orden, con la razón que dio. "
     "1) «Voces del cerro» (cuentos de barrio): porque cuenta vecinos de un cerro. 2) «Mapas de papel» (crónicas): porque muestra barrios y ciudad. 3) «La casa del mar quieto» (novela): porque presenta una casa y una familia. "
     "4) «El guardián de los relojes» (cuentos fantásticos sobre el tiempo): porque me la prestaron. 5) «Cartas desde el sur» (poemas de viaje): porque habla de lugares recorridos. Todas las obras son inventadas.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una trayectoria de lectura según su coherencia, variedad y progresión, y a detectar eslabones débiles. Sirve para revisar y mejorar la trayectoria que armé.",
    prior=["Sé qué es un hilo.", "Sé explicitar criterios de selección.", "Sé distinguir un género de otro."],
    explain=[
        "Analizar una trayectoria es evaluarla con criterios, igual que se evalúa un texto. Tres criterios sirven de base. La coherencia: ¿todas las obras se relacionan con el hilo declarado? La variedad: ¿hay géneros, voces o épocas distintas, o es siempre lo mismo? La progresión: ¿hay un orden con sentido, por ejemplo de lo más cercano a lo más desafiante, o de lo general a lo particular?",
        "La coherencia se comprueba obra por obra. Para cada una pregunta: ¿cómo se relaciona con el hilo?, ¿qué aporta? Si la única razón es «me la prestaron» o «estaba a mano», es un eslabón débil: la obra puede ser buena, pero no pertenece a esa trayectoria. Se puede reemplazar o mover a otra trayectoria. Dejarla no es un error mientras se reconozca que es una excepción.",
        "La variedad se cuenta: ¿cuántos géneros distintos hay entre las obras? Una trayectoria de cinco obras con solo cuentos tiene poca variedad. La progresión se explica: ¿por qué esta obra después de esta otra? A veces se pasa de un texto breve a uno largo, o de lo más conocido a lo más lejano. Analizar la trayectoria termina con una decisión: conservarla, ajustarla o dividirla en dos.",
    ],
    vocab=[("coherencia", "relación de cada obra con el hilo declarado"), ("variedad", "diferencia de géneros, voces o épocas entre las obras"), ("progresión", "orden con sentido entre las obras"), ("eslabón débil", "obra cuya razón no se relaciona con el hilo"), ("ajustar", "cambiar o reordenar obras para mejorar la trayectoria")],
    worked=[
        ("Comprobar la coherencia", "¿Qué obra de Diego es un eslabón débil?",
         ["Revisa cada razón frente al hilo: lugares y personas que los habitan.", "Las obras 1, 2, 3 y 5 tienen razones que se relacionan con lugares.", "La obra 4 solo tiene la razón «me la prestaron»."],
         "La obra 4"),
        ("Contar la variedad", "¿Cuántos géneros distintos hay en la trayectoria?",
         ["Obra 1 y 4: cuento.", "Obra 2: crónica.", "Obra 3: novela.", "Obra 5: poesía.", "Géneros distintos: cuento, crónica, novela y poesía."],
         "4 géneros distintos"),
    ],
    mistakes=[("Dejar una obra que no calza con el hilo por no querer reordenar la lista.", "Una obra sin relación con el hilo debilita la coherencia de la trayectoria.", "Reemplázala, muévela a otra trayectoria o declara que es una excepción."),
              ("Medir la variedad solo por la cantidad de libros.", "La variedad se refiere a géneros, voces o épocas, no al número de obras.", "Cuenta cuántos géneros o voces distintas hay entre las obras.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué mide la coherencia de una trayectoria de lectura?", "Si cada obra se relaciona con el hilo", "Cuántos libros se leyeron", "Qué tan nuevos son los libros", "La coherencia revisa la relación de cada obra con el hilo declarado."),
        ("{F} ¿Cuántas obras tiene la trayectoria de Diego?", "5", "La ficha enumera cinco obras numeradas del 1 al 5."),
        ("{F} ¿Cuál es el hilo de Diego?", "Leer sobre lugares y las personas que los habitan", "Es el hilo que Diego declara al comienzo de la ficha."),
        ("abc", "{F} ¿Qué obra de Diego se justifica porque habla de lugares recorridos?", "La obra 5, «Cartas desde el sur»", "La obra 4, «El guardián de los relojes»", "La obra 1, «Voces del cerro»", "Esa es la razón que Diego dio para la obra 5."),
        ("abc", "{F} Si Diego reemplaza la obra 5 por otro libro de cuentos, ¿cuántos géneros distintos quedan en su trayectoria?", "3", "4", "5", "Quedarían cuentos, crónica y novela: tres géneros."),
        ("ab", "{F} ¿Qué obras de Diego son del mismo género?", "La 1 y la 4, que son cuentos", "La 2 y la 5, que son crónicas", "Las obras 1 y 4 están descritas como cuentos."),
        ("abc", "{F} Diego quiere reemplazar la obra 4 por una que sea coherente con su hilo. ¿Cuál sirve?", "«Voces de la costa», un libro inventado de relatos sobre un pueblo de pescadores", "Otro libro de cuentos sobre el tiempo", "Un libro cualquiera que le presten", "El primer libro trata de un lugar y sus habitantes, que es el hilo."),
        ("abc", "{F} ¿Qué mejora de progresión se puede proponer?", "Empezar por textos breves de barrio y terminar con la novela, más extensa", "Mezclar el orden al azar", "Ordenarlos por el color de la portada", "Un orden con sentido va de lo breve a lo extenso, por ejemplo."),
        ("abc", "{F} Si Diego decide mantener la obra 4 como excepción, ¿qué debe hacer?", "Declarar que no responde al hilo y explicar por qué la lee", "Fingir que sí responde al hilo", "Borrar las demás obras", "Reconocer la excepción mantiene la honestidad de la trayectoria."),
        ("ab", "{F} Una compañera dice que las obras 2 y 3 de Diego no son coherentes con su hilo porque son de géneros distintos. ¿Es correcto?", "No: sus razones (barrios y ciudad; una casa y una familia) se relacionan con el hilo, y los géneros miden la variedad", "Sí: obras de géneros distintos no pueden tener el mismo hilo", "La coherencia se mide por la relación con el hilo; que sean de géneros distintos aporta variedad, no incoherencia."),
        ("abc", "{F} ¿Qué decisión tomarías con la trayectoria de Diego?", "Ajustarla reemplazando la obra 4 o declarándola excepción", "Borrarla entera", "Dejarla igual sin pensar", "El análisis muestra un solo eslabón débil, que se puede ajustar."),
        ("abc", "{F} Diego quiere dividir su trayectoria en dos: una de lugares y otra del tiempo. ¿Qué obra iría en la segunda?", "La obra 4", "La obra 2", "La obra 5", "La obra 4 trata del tiempo, un hilo diferente."),
        ("abc", "{F} Una trayectoria de cinco obras que son todas cuentos de miedo. ¿Qué rasgo tiene?", "Mucha coherencia y poca variedad", "Mucha variedad y poca coherencia", "Ninguna coherencia", "Todas se unen en torno a un género único, pero no varían."),
    ],
    ctx=("abc", "Contexto: tu docente te pide que muestres la trayectoria de la ficha {F} a un curso menor y justifiques por qué es una buena trayectoria. ¿Cuál es el argumento mejor?", "«Tiene un hilo claro, cuatro géneros distintos y solo una obra que es excepción»", "«Es buena porque son cinco libros»", "«Es buena porque a mí me gusta»", "El primer argumento evalúa coherencia, variedad y excepción con criterios; los otros no."),
    sc=[
        ("En Taller de literatura: ¿qué es un eslabón débil de una trayectoria?", "Una obra cuya razón no se relaciona con el hilo", "El eslabón débil no se vincula con el hilo declarado."),
        ("ab", "La variedad se mide por:", "Los géneros, voces o épocas distintas", "El número de páginas", "La variedad es diversidad entre obras."),
        ("ab", "La progresión de una trayectoria:", "Explica por qué se leen las obras en ese orden", "No importa para nada", "El orden con sentido es una parte del análisis."),
    ],
    op=("Con la trayectoria de la ficha {F}: (1) evalúa la coherencia, la variedad y la progresión en una oración cada una; (2) propone un cambio concreto, con una obra que inventes para reemplazar la obra 4; (3) explica por qué tu cambio mejora la trayectoria.",
        "(1) Coherencia: alta, salvo la obra 4. Variedad: cuatro géneros distintos. Progresión: va de lo breve a lo extenso y termina en poesía. (2) Reemplazo la obra 4 por «Voces de la costa», relatos sobre un pueblo de pescadores. (3) Mejora la coherencia porque trata de un lugar y sus habitantes.",
        ["tres evaluaciones con criterio", "obra de reemplazo coherente", "justificación del cambio", "coherencia con el hilo"],
        ["tres respuestas numeradas"],
        ["evaluar sin criterio", "proponer una obra que tampoco calza", "no explicar el cambio"],
        "Pregunta: «¿qué ocurriría con la variedad si reemplazas la obra 4 por otro libro de cuentos?»."),
    reinforce="Evalúa con coherencia, variedad y progresión una trayectoria de tres obras de tu elección, inventadas por ti.",
    extend="Explica por qué una trayectoria con una obra que es excepción puede seguir siendo coherente si se reconoce.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (dos trayectorias de ejemplo, de lectoras inventadas). Lucía: hilo «las personas que se van y las que se quedan»; obras: 1) «Despedidas», microrrelatos; 2) «Cartas desde el sur», poemas; 3) «La casa del mar quieto», novela. "
     "Mateo: hilo «lugares con misterio»; obras: 1) «Voces del cerro», cuentos; 2) «Mapas de papel», crónicas; 3) «El guardián de los relojes», cuentos fantásticos. Todas las obras son inventadas. En la sesión de taller, cada persona tiene 3 minutos para presentar su trayectoria.")
build(
    O5, 4, F,
    use="Aprenderé a presentar mi trayectoria de lectura a mis pares, con hilo, criterios y razones, y a escuchar otras trayectorias para comparar y recomendar. Sirve para compartir lecturas y enriquecer las propias.",
    prior=["Sé armar una trayectoria con hilo.", "Sé explicitar criterios.", "Sé analizar coherencia y variedad."],
    explain=[
        "Compartir una trayectoria significa presentarla a otras personas para conversar. Una buena presentación tiene cuatro partes: el hilo en una frase; las obras en orden; los criterios con que fueron elegidas, con una razón para cada una; y un balance de lo que se descubrió. Se puede cerrar con una recomendación: una obra de la trayectoria que quieres que otros lean y por qué.",
        "Escuchar las trayectorias de otros también tiene reglas. Primero se identifica el hilo de la otra persona; después, qué criterios usó; y finalmente se comparan con los propios. Comparar no es juzgar quién lee mejor: es descubrir semejanzas (¿hay una obra que ambos leyeron?), diferencias (¿qué criterios distintos usaron?) y posibilidades (¿qué obra del otro podría sumar a mi trayectoria?).",
        "Una recomendación útil explica para quién es la obra y por qué. Sirve decir «te la recomiendo si te interesa el tema de la espera, porque la novela la muestra desde una familia». No sirve decir «léela, es buenísima». Y se respeta que a otra persona no le guste lo mismo: el gusto es personal. El tiempo de presentación también se planifica: si cada persona tiene 3 minutos, un grupo de cuatro necesita 12.",
    ],
    vocab=[("presentar", "exponer a otras personas el hilo, las obras y las razones"), ("balance", "reflexión final sobre lo que se descubrió al leer"), ("recomendación", "sugerencia razonada de una obra para alguien"), ("comparar", "buscar semejanzas y diferencias entre dos trayectorias"), ("semejanza", "rasgo que dos trayectorias comparten")],
    worked=[
        ("Armar una presentación", "Lucía presenta su trayectoria en 3 minutos. ¿Qué partes incluye?",
         ["El hilo: las personas que se van y las que se quedan.", "Las obras en orden, con una razón para cada una.", "Un balance y una recomendación."],
         "Hilo, obras con razones, balance y recomendación"),
        ("Comparar dos trayectorias", "¿Qué semejanza y qué diferencia hay entre Lucía y Mateo?",
         ["Semejanza: ambos leen tres obras y ambos incluyen narrativa breve (los microrrelatos de Lucía y los cuentos de Mateo).", "Diferencia: el hilo de Lucía son los vínculos entre personas; el de Mateo, los lugares con misterio."],
         "Misma cantidad de obras y narrativa breve, pero hilos distintos"),
    ],
    mistakes=[("Presentar la trayectoria como una lista de títulos sin hilo ni razones.", "Quien escucha no entiende qué une las obras ni por qué se eligieron.", "Empieza por el hilo y da una razón por obra."),
              ("Recomendar una obra con «es buenísima» y nada más.", "Sin razones ni destinatario, la recomendación no orienta.", "Di para quién es y qué aporta la obra.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué contiene una buena presentación de trayectoria?", "El hilo, las obras con sus razones, un balance y una recomendación", "Solo una lista de títulos", "Solo la opinión de otra persona", "Una presentación completa muestra el hilo, las razones y lo aprendido."),
        ("{F} ¿Cuál es el hilo de Lucía?", "Las personas que se van y las que se quedan", "La ficha declara ese hilo para Lucía."),
        ("{F} ¿Cuál es el hilo de Mateo?", "Lugares con misterio", "La ficha declara ese hilo para Mateo."),
        ("abc", "{F} ¿Qué obra aparece en la trayectoria de Mateo y no en la de Lucía?", "«Mapas de papel»", "«Despedidas»", "«La casa del mar quieto»", "«Mapas de papel» solo está en la trayectoria de Mateo."),
        ("abc", "{F} ¿Qué obra aparece en la trayectoria de Lucía y no en la de Mateo?", "«Cartas desde el sur»", "«El guardián de los relojes»", "«Voces del cerro»", "«Cartas desde el sur» está solo en la lista de Lucía."),
        ("=", "{F} Cada persona tiene 3 minutos y el grupo tiene seis personas. ¿Cuántos minutos necesita el grupo?", "3*6", "Se multiplica el tiempo individual por el número de personas.", " minutos"),
        ("=", "{F} La sesión dura 20 minutos y se presentan cuatro personas con el mismo tiempo cada una. ¿Cuántos minutos corresponde a cada una?", "20//4", "Se reparte el tiempo total entre las personas.", " minutos"),
        ("abc", "{F} ¿Cuál es una recomendación bien formulada de «Despedidas» para un compañero que busca lecturas breves sobre personas que se van?", "«Te la recomiendo si buscas lecturas breves sobre personas que se van, porque son microrrelatos sobre despedidas»", "«Léela porque sí»", "«Es la mejor de todas»", "La primera dice para quién es y qué aporta."),
        ("abc", "{F} Lucía quiere decidir si una obra de Mateo sirve a su trayectoria. ¿Qué conviene revisar?", "Si se relaciona con su hilo, las personas que se van y las que se quedan, y explicar cómo", "Si el título es más corto que los de su lista", "Si Mateo la leyó antes que ella", "Una obra se suma a una trayectoria cuando se relaciona con su hilo y se puede explicar esa relación."),
        ("ab", "{F} Lucía dice que la trayectoria de Mateo «no vale porque no es como la mía». ¿Qué respondes?", "Que cada trayectoria responde a un hilo propio y se compara sin jerarquías", "Que tiene razón", "Comparar sirve para descubrir semejanzas y diferencias, no para decidir cuál vale más."),
        ("abc", "{F} Mateo presenta su balance: «descubrí que me interesan los espacios pequeños». ¿Qué parte de la presentación es?", "El balance", "El hilo", "La recomendación", "El balance cuenta lo que se descubrió al leer."),
        ("abc", "{F} ¿Qué pregunta ayuda a conversar sobre la trayectoria de Lucía?", "«¿Por qué pusiste primero los microrrelatos?»", "«¿Por qué lees tan poco?»", "«¿Para qué sirve leer?»", "La pregunta se refiere a una decisión concreta de la trayectoria."),
        ("abc", "{F} Si a un compañero no le gusta una obra recomendada, ¿qué corresponde?", "Respetar su gusto y preguntar qué le interesaría más", "Insistir hasta que le guste", "Burlarse de su gusto", "El gusto es personal y se respeta."),
    ],
    ctx=("abc", "Contexto: tu curso hará una «feria de trayectorias» en que cada persona se sienta con otra a conversar en parejas, durante diez minutos. Te toca con alguien con la trayectoria de Mateo, de la ficha {F}. ¿Cómo preparas el diálogo?", "Escucho su hilo, comparo con el mío y le recomiendo una obra de mi lista con una razón", "Le digo que mi trayectoria es mejor", "Leo mi lista de títulos sin dar razones", "El diálogo parte de escuchar, compara y recomienda con razones."),
    sc=[
        ("En Taller de literatura: ¿qué es un balance de trayectoria?", "Una reflexión final sobre lo que se descubrió al leer", "El balance resume los aprendizajes de lector que dejó el recorrido."),
        ("ab", "Una recomendación útil dice:", "Para quién es la obra y por qué", "Solo que es buenísima", "Con destinatario y razón se orienta la lectura de otro."),
        ("ab", "Comparar trayectorias sirve para:", "Descubrir semejanzas, diferencias y posibilidades", "Decidir quién lee mejor", "Comparar es enriquecer la propia lectura, no competir."),
    ],
    op=("Con tu hilo propio (puedes retomar el de la clase 1) y tres obras de la lista de la ficha {F} o inventadas por ti: escribe el guion de tu presentación de 3 minutos con (1) el hilo en una frase; (2) las tres obras con una razón cada una; (3) un balance de una oración; (4) una recomendación con destinatario y razón.",
        "(1) Mi hilo es cómo la gente se despide. (2) «Despedidas», porque muestra despedidas breves; «Cartas desde el sur», porque las despedidas se escriben; «La casa del mar quieto», porque muestra a quienes se quedan. (3) Descubrí que me interesa lo que queda después. (4) Recomiendo «Cartas desde el sur» a quien le guste la poesía narrativa, porque cuenta un viaje en forma de cartas.",
        ["hilo claro", "tres obras con razones", "balance de una oración", "recomendación con destinatario y razón", "presentación que cabe en tres minutos"],
        ["guion de cuatro partes"],
        ["lista de títulos sin razones", "recomendación sin destinatario", "balance que repite el hilo"],
        "Pregunta: «¿qué pregunta te haría alguien curioso y qué le responderías?»."),
    reinforce="Escribe una recomendación de una obra inventada para una persona que ama el misterio, con la razón.",
    extend="Explica cómo escuchar la trayectoria de otra persona puede cambiar tus propios criterios de selección.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (pasaje original de ejemplo). «En la estación vacía, un hombre ensayaba en voz baja cómo decir adiós. Cuando el tren llegó, ya no necesitó ninguna frase.» "
     "Productos posibles de reflexión. P) ensayo personal; Q) crónica de un hecho vivido; R) carta a alguien; S) poema; T) fotografía con un texto breve.")
build(
    O6, 1, F,
    use="Aprenderé a elegir un género para producir una reflexión propia, a partir de lo leído: ensayo personal, crónica, carta, poema o producción visual con texto. Sirve para comunicar lo que pienso sobre mí y sobre el mundo.",
    prior=["Sé qué es una interpretación.", "Conozco varios géneros literarios.", "Sé que escribir tiene un propósito."],
    explain=[
        "Una reflexión es un pensamiento que parte de una lectura o experiencia y se pregunta por su sentido. Reflexionar sobre sí mismo es preguntarse qué pienso, siento o hago ante algo; reflexionar sobre el mundo es preguntarse por las personas, la sociedad o la condición humana. En este taller, esas reflexiones surgen de las obras leídas, de tu trayectoria de lectura y de los criterios con que elegiste leer.",
        "Se puede producir una reflexión en varios géneros. El ensayo personal expone una idea propia con argumentos y ejemplos, en primera persona. La crónica narra un hecho vivido y reflexiona a partir de él. La carta se dirige a alguien concreto. El poema condensa una experiencia en imágenes. Una fotografía con un texto breve combina imagen y palabra. Cada género permite decir algo distinto y exige decisiones de forma distintas.",
        "Para elegir, pregunta qué quieres decir, a quién y con qué materia cuentas. Si quieres argumentar una idea, el ensayo es el más adecuado. Si tienes un hecho vivido que te hizo pensar, la crónica. Si hay una persona a quien le quieres decir algo, la carta. Si lo que tienes es una sensación o una imagen, el poema o la fotografía comentada. Una reflexión sin género claro termina siendo un conjunto de frases sueltas.",
    ],
    vocab=[("reflexión", "pensamiento que parte de una lectura o experiencia y se pregunta por su sentido"), ("ensayo personal", "texto que expone una idea propia con argumentos y ejemplos"), ("crónica", "texto que narra un hecho vivido y reflexiona a partir de él"), ("carta", "texto dirigido a una persona concreta"), ("materia", "lo que tienes para escribir: un hecho, una sensación o una idea")],
    worked=[
        ("Elegir un género por la materia", "Después de leer el pasaje de la estación, recuerdas una despedida real que viviste y quieres contarla pensando en lo que te enseñó. ¿Qué género eliges?",
         ["Tu materia es un hecho vivido.", "Quieres narrarlo y reflexionar.", "El género que narra un hecho vivido y reflexiona es la crónica."],
         "Crónica"),
        ("Elegir un género por el destinatario", "Quieres decirle a una amiga, que se fue a vivir lejos, lo que te hizo pensar el pasaje. ¿Qué género eliges?",
         ["Tu audiencia es una persona concreta.", "Quieres hablarle directamente.", "El género dirigido a alguien concreto es la carta."],
         "Carta"),
    ],
    mistakes=[("Elegir el género sin saber qué se quiere reflexionar.", "El género debe servir a lo que se quiere decir y a quién.", "Escribe primero la pregunta o idea que quieres explorar y luego el género."),
              ("Creer que una reflexión es solo contar la experiencia propia.", "La reflexión añade una pregunta o una idea sobre el sentido de lo vivido o leído.", "Después de contar, pregúntate qué significa eso y qué piensas de ello.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una reflexión?", "Un pensamiento que parte de una lectura o experiencia y se pregunta por su sentido", "Un resumen de una obra", "Una lista de opiniones", "La reflexión se pregunta por el sentido de lo leído o vivido."),
        ("{F} ¿Dónde ocurre la escena del pasaje?", "En una estación", "El pasaje comienza en una estación vacía."),
        ("{F} ¿Qué ensayaba el hombre?", "Cómo decir adiós", "El pasaje dice que ensayaba en voz baja cómo decir adiós."),
        ("abc", "{F} ¿Qué producto conviene para exponer una idea propia con argumentos y ejemplos?", "P, el ensayo personal", "S, el poema", "T, la fotografía con texto", "El ensayo personal está hecho para argumentar una idea propia."),
        ("abc", "{F} Viviste una mudanza que te hizo pensar en lo que dejamos atrás y quieres contarla con escenas y luego reflexionar. ¿Qué producto conviene?", "Q, la crónica", "R, la carta", "S, el poema", "La crónica narra un hecho vivido y piensa a partir de él."),
        ("abc", "{F} Quieres escribirle a un profesor o profesora que te acompañó en el colegio lo que te hizo pensar el pasaje. ¿Qué producto conviene?", "R, la carta", "P, el ensayo", "T, la fotografía", "La carta tiene un destinatario determinado."),
        ("ab", "{F} Una estudiante tiene solo una sensación y una imagen: el eco de una voz en un andén. ¿Qué producto conviene?", "S, el poema", "P, el ensayo con argumentos", "Una sensación y una imagen se condensan bien en un poema; el ensayo exige argumentos que ella aún no tiene."),
        ("abc", "{F} Un estudiante quiere mostrar una fotografía de un andén y escribir una frase que invite a pensar. ¿Qué producto es?", "T, la fotografía con un texto breve", "P, el ensayo personal", "R, la carta", "Combina imagen y palabra, que es el producto T."),
        ("abc", "{F} ¿Cuál es una pregunta de reflexión que surge del pasaje?", "¿Por qué a veces las palabras ensayadas dejan de hacer falta cuando llega el momento?", "¿De qué color era el tren?", "¿Cuántas personas había en la estación?", "La primera pregunta busca el sentido del pasaje; las otras piden datos que el texto no da."),
        ("abc", "{F} Una estudiante escribe: «el pasaje me recordó una despedida real; la cuento». ¿Qué le falta para que sea una reflexión?", "Preguntarse qué significa esa despedida y qué piensa de ella", "Más datos del tren", "Cambiar la despedida por otra", "La reflexión necesita pensar el sentido de lo contado."),
        ("abc", "{F} Se quiere escribir sobre las despedidas en general, con ejemplos de la lectura. ¿Qué producto conviene?", "El ensayo personal", "La carta a un amigo", "El poema de una sola imagen", "Un tema general con ejemplos se trabaja mejor en un ensayo."),
        ("abc", "{F} Una reflexión sobre sí mismo, a partir del pasaje, empieza con: «Me di cuenta de que yo también ensayo lo que voy a decir». ¿Qué voz usa?", "Primera persona", "Tercera persona", "Segunda persona", "Usa «yo» y «me», propios de la primera persona."),
        ("abc", "{F} Elige el plan más claro para una reflexión.", "Idea o pregunta, género elegido por la materia, audiencia y un pasaje de la lectura", "Un conjunto de frases sueltas sin orden", "Copiar el pasaje sin comentar", "El primer plan articula lo que se piensa con el género y el apoyo en la lectura."),
    ],
    ctx=("abc", "Contexto: tu curso organiza una «semana de las reflexiones» y debes presentar la tuya a partir del pasaje de la ficha {F} en una sola hoja pegada en el pasillo. ¿Qué producto conviene?", "T, una fotografía con un texto breve que invita a pensar", "Un ensayo de seis hojas", "Una carta privada guardada en tu mochila", "Una hoja visible en un pasillo pide un producto breve y llamativo."),
    sc=[
        ("En Taller de literatura: ¿qué distingue a una crónica de un ensayo personal?", "La crónica narra un hecho vivido; el ensayo argumenta una idea", "Cada género tiene su forma: narración de un hecho o argumentación de una idea."),
        ("ab", "Una reflexión debe incluir:", "Una pregunta o idea sobre el sentido de lo leído o vivido", "Solo una lista de datos", "La reflexión piensa el sentido, no solo describe."),
        ("ab", "El género de una reflexión se elige según:", "Qué quiero decir, a quién y con qué materia", "El azar", "La elección responde a un propósito y a una materia."),
    ],
    op=("Con el pasaje de la ficha {F}: (1) escribe una pregunta de reflexión que te deje el pasaje; (2) elige uno de los productos P, Q, R, S o T; (3) explica por qué ese género sirve a tu pregunta; (4) escribe las dos primeras oraciones de tu producto.",
        "(1) ¿Por qué a veces lo que preparamos para decir se vuelve innecesario cuando llega el momento? (2) P, ensayo personal. (3) Porque quiero argumentar una idea con ejemplos de la lectura y de mi vida. (4) «A veces ensayamos una frase durante días y luego no la decimos. El hombre del pasaje ensayaba un adiós que el tren hizo innecesario.»",
        ["pregunta de reflexión propia", "género elegido entre P, Q, R, S y T", "justificación coherente", "dos oraciones iniciales"],
        ["cuatro respuestas numeradas"],
        ["pregunta que pide datos y no reflexión", "justificar el género por moda", "oraciones sin voz propia"],
        "Pregunta: «¿cómo cambiaría tu reflexión si la escribieras como carta?»."),
    reinforce="Escribe tres preguntas de reflexión distintas que te deje el pasaje de la estación.",
    extend="Explica por qué una misma reflexión puede comunicarse de forma muy distinta en un ensayo y en un poema.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (pasaje original de ejemplo). «Todos los días, Rita guardaba en un frasco una cosa que ya no necesitaba: un botón, un papel, una palabra escrita en una servilleta. El frasco se llenó. Rita no supo qué hacer con él.» "
     "Formulaciones de ejemplo. T1) «Las cosas que guardamos.» T2) «¿Qué le pasa a un recuerdo cuando intentamos conservarlo en un objeto?» T3) «Guardar cosas inútiles es una manera de no aceptar que algo terminó.»")
build(
    O6, 2, F,
    use="Aprenderé a pasar de un pasaje leído a una pregunta de reflexión sobre mí y sobre el mundo, distinguiendo tema, pregunta y tesis. Sirve para tener un punto de partida claro antes de escribir.",
    prior=["Sé distinguir tema y tesis.", "Sé formular una pregunta de escritura.", "Sé citar un pasaje."],
    explain=[
        "Toda reflexión parte de un pasaje o experiencia que deja algo pendiente: una extrañeza, una duda, un parecido con la propia vida. Ese algo pendiente puede escribirse de tres modos. El tema nombra de qué trata («los objetos»). La pregunta de reflexión abre una duda sobre el sentido («¿qué hacemos con lo que no queremos soltar?»). La tesis es una respuesta que se propone («guardar es una forma de aplazar una despedida»).",
        "En la práctica se avanza en ese orden: del tema a la pregunta y de la pregunta a la tesis. Una buena pregunta de reflexión no se responde con sí o no ni con un dato; admite varias respuestas razonables y obliga a pensar. «¿Cuántos objetos guardó Rita?» es una pregunta de datos; «¿qué guarda Rita realmente cuando guarda un botón?» es de reflexión. La pregunta se vuelve más fértil si conecta el pasaje con la vida humana en general.",
        "La tesis es provisoria: es la respuesta que hoy te parece más razonable y que podrías matizar al escribir. Debe apoyarse en el pasaje y en algo de tu experiencia o de tu observación del mundo. Si la tesis solo repite lo que dice el pasaje, no reflexiona; si no se relaciona con él, deja de ser una reflexión sobre lo leído. La reflexión crece cuando el pasaje y tu mirada se encuentran.",
    ],
    vocab=[("tema", "idea general de la que trata un texto"), ("pregunta de reflexión", "pregunta que abre una duda sobre el sentido y admite varias respuestas"), ("tesis", "respuesta que se propone y se defiende"), ("provisoria", "que puede cambiar al seguir pensando"), ("fértil", "que da lugar a muchas ideas")],
    worked=[
        ("Del tema a la pregunta", "El tema de la ficha es «los objetos». ¿Cómo llegas a una pregunta de reflexión?",
         ["Pregúntate qué hace Rita con los objetos: guarda lo que no necesita.", "Convierte esa acción en duda sobre el sentido: ¿por qué guardamos lo que no necesitamos?", "La pregunta admite varias respuestas."],
         "¿Por qué guardamos lo que ya no necesitamos?"),
        ("De la pregunta a la tesis", "Tu pregunta es «¿qué hacemos con lo que no queremos soltar?». ¿Cómo propones una tesis?",
         ["Piensa en la acción de Rita: guarda un objeto cada día.", "Propón una respuesta razonable: guardar es aplazar una despedida.", "Verifica que se apoya en el pasaje: el frasco se llena y Rita no sabe qué hacer."],
         "Guardar es una forma de aplazar una despedida"),
    ],
    mistakes=[("Plantear una pregunta que se responde con un dato: «¿cuántos objetos guardó Rita?».", "No abre una duda sobre el sentido ni obliga a pensar.", "Reformula: «¿qué guarda Rita realmente cuando guarda un botón?»."),
              ("Dejar una tesis que no se relaciona con el pasaje.", "Entonces la reflexión no surge de lo leído.", "Conecta la tesis con una acción o frase concreta del pasaje.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una pregunta de reflexión?", "Una pregunta que abre una duda sobre el sentido y admite varias respuestas", "Una pregunta que se responde con un dato", "Una pregunta que se responde con sí o no", "La pregunta de reflexión invita a pensar, no a buscar un dato."),
        ("{F} ¿Qué guardaba Rita en el frasco todos los días?", "Una cosa que ya no necesitaba", "El pasaje dice que cada día guardaba algo que ya no necesitaba."),
        ("{F} ¿Cuál de las formulaciones T1, T2 o T3 es solo un tema?", "T1", "«Los objetos» nombra de qué trata sin preguntar ni afirmar."),
        ("{F} ¿Cuál es una pregunta de reflexión?", "T2", "T2 abre una duda sobre el sentido de guardar y soltar."),
        ("{F} ¿Cuál es una tesis?", "T3", "T3 afirma una respuesta que se puede defender."),
        ("abc", "{F} ¿Qué pasaje del texto apoya la tesis T3?", "«El frasco se llenó. Rita no supo qué hacer con él»", "«un botón, un papel»", "«Todos los días»", "Que el frasco se llene y Rita no sepa qué hacer sugiere que no puede soltar lo guardado."),
        ("abc", "{F} ¿Cuál es una pregunta de datos, no de reflexión?", "¿Cuántas cosas distintas se nombran como ejemplo de lo que guardaba?", "¿Por qué guardamos lo que no necesitamos?", "¿Qué dice un frasco lleno sobre quien lo llena?", "La primera se responde contando; las otras abren una duda sobre el sentido."),
        ("ab", "{F} Un estudiante propone la tesis «Rita guardaba cosas en un frasco». ¿Qué problema tiene?", "Solo repite lo que dice el pasaje y no reflexiona", "Es demasiado original", "Una tesis debe ir más allá del pasaje; esta solo lo resume."),
        ("abc", "{F} ¿Cuál es una mejor pregunta de reflexión?", "¿Qué guardamos realmente cuando guardamos algo que ya no usamos?", "¿De qué color era el frasco?", "¿Rita tenía un frasco?", "Es la única que lleva a pensar en el sentido y se puede conectar con la vida humana."),
        ("abc", "{F} Una estudiante propone la tesis «los frascos son de vidrio». ¿Qué problema tiene?", "No se relaciona con el sentido del pasaje ni abre una reflexión", "Es muy extensa", "Tiene demasiados adjetivos", "Es un dato sin conexión con el sentido del pasaje."),
        ("abc", "{F} Una tesis provisoria significa que:", "Puede cambiar o matizarse mientras sigues pensando", "No hay que defenderla", "No se puede escribir", "La tesis es la mejor respuesta de hoy, que se ajusta al seguir pensando."),
        ("abc", "{F} Se quiere conectar la pregunta con la vida de quien escribe sin exponer datos íntimos de otros. ¿Qué enfoque conviene?", "Usar un ejemplo propio y general, sin nombrar a otras personas", "Contar un secreto de una amiga con su nombre", "Usar datos personales de un vecino", "Se puede reflexionar desde la experiencia propia cuidando la privacidad ajena."),
        ("abc", "{F} Cuando ya tienes el tema y la pregunta de reflexión, ¿qué sigue?", "Proponer una tesis provisoria", "Escribir la conclusión sin pensar", "Volver a elegir el tema", "Primero se pregunta y luego se propone una respuesta provisoria."),
    ],
    ctx=("abc", "Contexto: para el diario mural debes escribir una frase que invite a leer tu reflexión sobre el pasaje de {F}. ¿Cuál sirve mejor?", "«¿Qué guardamos cuando guardamos lo que ya no necesitamos?»", "«Texto sobre un frasco»", "«Reflexión número tres»", "La pregunta despierta curiosidad y anticipa el tema; los otros títulos no."),
    sc=[
        ("En Taller de literatura: ¿qué diferencia hay entre tema y pregunta de reflexión?", "El tema nombra de qué trata; la pregunta abre una duda sobre el sentido", "El tema es general; la pregunta indaga en el sentido."),
        ("ab", "Una tesis de reflexión debe:", "Apoyarse en el pasaje y en la mirada propia", "Ser un dato sin relación con el pasaje", "Reflexionar es conectar lo leído con lo que uno piensa."),
        ("ab", "Una tesis provisoria:", "Puede matizarse al escribir", "No puede cambiar nunca", "Pensar mientras se escribe permite ajustarla."),
    ],
    op=("Con el pasaje de la ficha {F} o con otro breve que tú escribas: (1) anota el tema; (2) escribe una pregunta de reflexión; (3) propone una tesis provisoria; (4) cita una frase del pasaje que la apoye.",
        "(1) Los objetos que guardamos. (2) ¿Por qué cuesta tanto soltar objetos sin uso? (3) Cuesta porque los objetos guardan una parte de quienes fuimos. (4) «El frasco se llenó. Rita no supo qué hacer con él».",
        ["tema claro", "pregunta de reflexión que admite varias respuestas", "tesis provisoria que responde la pregunta", "cita que apoya la tesis"],
        ["cuatro respuestas numeradas"],
        ["pregunta de datos", "tesis que repite el pasaje", "cita que no apoya la tesis"],
        "Pregunta: «¿qué argumento contrario podría plantear alguien a tu tesis?»."),
    reinforce="Convierte estos temas en preguntas de reflexión: «la espera», «los recuerdos», «los apodos».",
    extend="Explica por qué una pregunta de reflexión fértil suele servir para muchos pasajes y no solo para uno.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (modelos de ejemplo, escritos por estudiantes inventados). Pasaje de base: «Todos los días, Rita guardaba en un frasco una cosa que ya no necesitaba. El frasco se llenó. Rita no supo qué hacer con él.» "
     "M1) «Yo también guardo entradas de cine y nunca las miro. Me gusta guardar.» M2) «En el pasaje, Rita guarda cosas que no necesita y el frasco se llena; eso muestra que no puede soltar.» "
     "M3) «El frasco que se llena sin que Rita sepa qué hacer me recuerda mi caja de entradas de cine: guardo cada una sin saber si es para recordar o para no soltar. Quizás Rita y yo guardamos para aplazar el fin de algo.» "
     "M4) «Mi vecino Jorge guarda diarios viejos porque su familia está pasando por un problema grave.»")
build(
    O6, 3, F,
    use="Aprenderé a sostener una reflexión con evidencia de la obra y con experiencia propia, sin perder el texto ni exponer a otras personas. Sirve para conectar mis lecturas con mi vida y con el mundo de forma respetuosa.",
    prior=["Sé formular una pregunta y una tesis de reflexión.", "Sé citar y comentar un pasaje.", "Sé que debo cuidar la privacidad de las personas."],
    explain=[
        "Una reflexión sólida combina tres fuentes: lo que dice el texto, lo que tú piensas o has vivido y lo que observas del mundo. Si solo hay texto, queda en comentario literario; si solo hay experiencia propia, la lectura desaparece. La buena reflexión va y viene entre ambos: cita un pasaje, lo relaciona con una experiencia y saca una idea sobre las personas o la vida.",
        "Para equilibrar, usa la secuencia texto, yo y mundo. Primero, qué dice el pasaje (texto). Segundo, en qué se parece o se diferencia de tu experiencia (yo). Tercero, qué idea más general sugiere sobre las personas o la sociedad (mundo). En el modelo M3, el frasco de Rita (texto) se conecta con la caja de entradas de la autora (yo) y con la idea de que guardar puede aplazar un final (mundo).",
        "Al hablar de ti, comparte solo lo que quieras. Al hablar de otras personas, no uses nombres ni expongas asuntos íntimos o de salud sin su permiso: M4 cuenta un problema de otra persona, y eso no corresponde. Es mejor usar ejemplos generales o propios. Si una lectura te recuerda algo doloroso o te preocupa por alguien, cuéntaselo a una persona adulta de confianza; una reflexión escrita no reemplaza esa conversación.",
    ],
    vocab=[("texto, yo y mundo", "tres fuentes de la reflexión: lo que dice la obra, la experiencia propia y la idea general"), ("experiencia propia", "algo que quien escribe ha vivido o pensado"), ("idea general", "afirmación sobre las personas o la vida que va más allá de un caso"), ("privacidad", "derecho a no exponer asuntos personales"), ("ejemplo general", "ejemplo que no identifica a ninguna persona real")],
    worked=[
        ("Distinguir el equilibrio", "M2 solo habla del pasaje y M1 solo habla de la autora. ¿Cuál equilibra texto, yo y mundo?",
         ["M2 tiene texto pero no experiencia ni idea general.", "M1 tiene experiencia pero no texto.", "M3 combina el frasco (texto), la caja de entradas (yo) y la idea de aplazar el fin (mundo)."],
         "M3"),
        ("Cuidar la privacidad", "M4 cuenta un problema de Jorge. ¿Qué cambias?",
         ["M4 nombra a una persona real y expone una situación íntima.", "Se reemplaza por un ejemplo general: «hay personas que guardan cosas viejas cuando atraviesan momentos difíciles».", "Si algo preocupa por alguien cercano, se habla con una persona adulta de confianza."],
         "Un ejemplo general, sin nombre ni asunto íntimo"),
    ],
    mistakes=[("Contar una experiencia propia larga y olvidar el pasaje que la provocó.", "La reflexión deja de ser una respuesta a la lectura.", "Vuelve al texto con una cita que conecte con tu experiencia."),
              ("Usar el nombre y los problemas de una persona real como ejemplo.", "Expone a esa persona sin su permiso.", "Usa un ejemplo general o propio, sin nombres.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué tres fuentes combina una reflexión sólida?", "El texto, la experiencia propia y la idea general sobre el mundo", "Solo la opinión de otras personas", "Solo datos de internet", "La reflexión sólida va y viene entre lo leído, lo vivido y lo general."),
        ("{F} ¿Qué objeto guarda la autora en M3?", "Entradas de cine", "M3 y M1 hablan de entradas de cine."),
        ("{F} ¿Qué modelo, M1, M2 o M3, plantea una duda abierta con la palabra «quizás»?", "M3", "Solo M3 termina con un «quizás» que deja abierta una idea sobre por qué guardamos."),
        ("abc", "{F} ¿Qué le falta a M1?", "Un pasaje del texto y una idea general", "Más entradas de cine", "Un título más largo", "M1 es solo experiencia propia, sin texto ni idea general."),
        ("abc", "{F} ¿Qué le falta a M2?", "Experiencia propia y una idea general sobre las personas", "Una cita más larga del pasaje", "Un cambio de narrador", "M2 solo comenta el texto, sin conexión con el yo ni el mundo."),
        ("abc", "{F} Otro modelo dice: «Rita llena un frasco (1); yo llené un cuaderno de recortes (2); quizás muchas personas guardamos para sentir que el tiempo pasa más despacio (3)». ¿Qué parte es la experiencia propia?", "(2), «yo llené un cuaderno de recortes»", "(1), «Rita llena un frasco»", "(3), «quizás muchas personas guardamos…»", "La parte (2) cuenta algo que le pasó a quien escribe; (1) es el texto y (3) la idea general."),
        ("abc", "{F} ¿Por qué M4 no corresponde en una reflexión?", "Nombra a una persona real y expone un asunto íntimo suyo", "Porque habla de diarios", "Porque es muy corto", "Las reflexiones no deben exponer a terceros sin su permiso."),
        ("abc", "{F} ¿Cómo reescribirías M4 respetando la privacidad?", "«Hay personas que guardan cosas viejas cuando atraviesan momentos difíciles»", "«Mi vecino Jorge está muy mal»", "«Jorge debería hablar de eso con todo el curso»", "El ejemplo general no identifica a nadie."),
        ("abc", "{F} Si una lectura te recuerda algo muy doloroso, ¿qué es lo más adecuado?", "Contarlo a una persona adulta de confianza, además de escribir lo que quieras compartir", "Guardarlo en secreto y no hablar con nadie", "Contarlo en redes sociales con detalles", "Una persona adulta de confianza puede acompañarte; la escritura no reemplaza esa ayuda."),
        ("abc", "{F} Una compañera te cuenta un problema familiar suyo y te dice que lo uses como ejemplo. ¿Qué corresponde?", "Usar un ejemplo general y sugerirle que, si le preocupa, lo converse con una persona adulta de confianza", "Contarlo con su nombre", "Publicarlo en el mural", "Es más prudente usar un ejemplo general y cuidar la privacidad."),
        ("abc", "{F} Se quiere mejorar M2 sumando experiencia propia. ¿Cuál es una buena adición?", "«En mi caso, guardo mensajes antiguos y no sé si es para recordar o para no soltar»", "«Rita guarda cosas»", "«Los frascos son de vidrio»", "La primera añade una experiencia propia que dialoga con el pasaje."),
        ("abc", "{F} ¿Qué orden sigue la secuencia texto, yo y mundo?", "Pasaje, experiencia propia, idea general", "Idea general, experiencia propia, pasaje", "Experiencia propia, idea general, pasaje", "La secuencia va del pasaje a la experiencia y de allí a una idea general."),
        ("{F} Completa con una palabra de M3: la autora guarda cada entrada sin saber si es para recordar o para no ____.", "soltar", "M3 dice que no sabe si guarda para recordar o para no soltar."),
    ],
    ctx=("abc", "Contexto: tu docente publicará reflexiones anónimas del curso en un libro de la clase. ¿Qué cuidado básico debes tener al escribir sobre tu experiencia con la ficha {F}?", "No nombrar a personas reales y compartir solo lo que quieras que se publique", "Nombrar a todas las personas para que se sepa quiénes son", "Incluir datos personales de tu familia", "Una publicación pide cuidar la privacidad propia y ajena."),
    sc=[
        ("En Taller de literatura: ¿qué significa la secuencia texto, yo y mundo?", "Pasaje, experiencia propia e idea general", "La reflexión conecta lo leído, lo vivido y lo general."),
        ("ab", "Al hablar de otras personas en una reflexión:", "No expongo sus asuntos íntimos ni uso sus nombres", "Cuento todo lo que sé de ellas", "La privacidad de otras personas se cuida siempre al escribir."),
        ("ab", "Si una lectura me remueve algo doloroso, es adecuado:", "Hablar con una persona adulta de confianza", "Guardarlo para siempre sin contárselo a nadie", "Pedir ayuda a una persona adulta es una decisión de cuidado."),
    ],
    op=("Con el pasaje de la ficha {F} o con otro tuyo: escribe una reflexión de cinco oraciones con esta secuencia: (1) qué dice el pasaje (con una cita breve); (2) una experiencia propia, sin nombres de otras personas; (3) una idea general sobre las personas; (4) una pregunta que quede abierta; (5) una frase de cierre.",
        "(1) El pasaje dice «El frasco se llenó. Rita no supo qué hacer con él». (2) A mí me pasa con las fotos del celular: las guardo y nunca las miro. (3) Quizás guardamos para sentir que lo vivido no se acaba. (4) ¿Cuántas cosas guardamos para no despedirnos? (5) Quizás soltar es también una forma de recordar.",
        ["cita breve del pasaje", "experiencia propia sin nombres de terceros", "idea general", "pregunta abierta", "cierre"],
        ["cinco oraciones numeradas"],
        ["olvidar el pasaje", "nombrar a una persona real", "idea general que no se relaciona con lo anterior"],
        "Pregunta: «¿qué parte de tu reflexión te costó más escribir y por qué?»."),
    reinforce="Escribe una oración de texto, una de yo y una de mundo para reflexionar sobre el pasaje del frasco, sin repetir los modelos.",
    extend="Explica por qué una reflexión que mezcla texto, yo y mundo es más convincente que una que solo cuenta la experiencia propia.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (dos reflexiones de ejemplo, de estudiantes inventados). Pasaje de base: «Todos los días, Rita guardaba en un frasco una cosa que ya no necesitaba. El frasco se llenó. Rita no supo qué hacer con él.» "
     "R1) «Todos los jóvenes guardan cosas porque no saben soltar.» "
     "R2) «Algunas personas guardan objetos para recordar y otras para no enfrentar una despedida; el pasaje de Rita permite pensar en las dos posibilidades, aunque no dice cuál es la suya.»")
build(
    O6, 4, F,
    use="Aprenderé a contrastar reflexiones: reconocer generalizaciones apresuradas, matices y contraargumentos, y a afinar mi propia postura. Sirve para que mis reflexiones sean justas con las personas y con el texto.",
    prior=["Sé conectar texto, yo y mundo.", "Sé qué es una tesis.", "Sé qué es una interpretación plausible."],
    explain=[
        "Dos reflexiones sobre el mismo pasaje pueden ser muy distintas, y comparar permite ver cuál es más sólida. Un criterio útil es el alcance: ¿cuánto afirma? Una generalización apresurada afirma sobre «todos» o «nadie» sin evidencia suficiente: «todos los jóvenes guardan cosas porque no saben soltar». Es débil porque basta un caso contrario para refutarla y porque simplifica a las personas.",
        "El matiz es el recurso contrario. Matizar es reconocer que algo ocurre a veces, a algunas personas o por varias razones. Se expresa con palabras como «algunas», «a veces», «puede ser», «en ciertos casos». R2 matiza: dice que algunas personas guardan para recordar y otras para evitar una despedida, y reconoce que el pasaje no define cuál es el caso de Rita. Matizar no es dudar de todo: es ajustar lo que se afirma a lo que se puede respaldar.",
        "Un contraargumento es una razón que va en contra de tu tesis. Considerar uno fortalece una reflexión: lo planteas, lo respondes y muestras que tu postura resiste. Por ejemplo: «alguien podría decir que guardar es solo comodidad; sin embargo, el pasaje muestra que Rita no sabe qué hacer con el frasco lleno». Al contrastar reflexiones, no se busca ganar, sino afinar la propia postura con lo que se aprende de las otras.",
    ],
    vocab=[("generalización apresurada", "afirmación sobre «todos» o «nadie» sin evidencia suficiente"), ("matiz", "ajuste que reconoce excepciones o varias posibilidades"), ("contraargumento", "razón que va en contra de la propia tesis"), ("alcance", "cuánto afirma una tesis"), ("refutar", "mostrar con una razón que una afirmación es falsa o insuficiente")],
    worked=[
        ("Reconocer una generalización", "R1 dice «todos los jóvenes guardan cosas porque no saben soltar». ¿Qué problema tiene?",
         ["Afirma sobre «todos» los jóvenes.", "No tiene evidencia que respalde ese alcance.", "Un solo joven que no guarde cosas la refuta. Es una generalización apresurada."],
         "Generaliza sobre todos sin evidencia"),
        ("Plantear un contraargumento", "Tu tesis es «guardar es aplazar una despedida». ¿Cómo planteas un contraargumento?",
         ["Piensa en una razón contraria: guardar puede ser simple comodidad.", "Formula: «alguien podría decir que guardar es solo comodidad».", "Responde con el pasaje: Rita no sabe qué hacer con el frasco lleno."],
         "Se plantea la razón contraria y se responde con el pasaje"),
    ],
    mistakes=[("Matizar tanto que no se afirma nada: «tal vez, a veces, quizás, no sé».", "El matiz ajusta la afirmación; no la elimina.", "Afirma algo concreto y señala sus límites."),
              ("Ignorar los contraargumentos para no debilitar la tesis.", "Ignorarlos hace la reflexión frágil ante la primera objeción.", "Plantea el contraargumento más fuerte y responde con evidencia.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una generalización apresurada?", "Una afirmación sobre «todos» o «nadie» sin evidencia suficiente", "Una afirmación con mucho matiz", "Una pregunta de reflexión", "Generaliza sin respaldo y se refuta con un solo caso."),
        ("{F} ¿Cuál reflexión, R1 o R2, contiene la palabra «Todos»?", "R1", "R1 comienza con «Todos los jóvenes»."),
        ("{F} ¿Cuántas posibilidades distintas para guardar menciona R2?", "2", "R2 menciona guardar para recordar y guardar para no enfrentar una despedida: dos."),
        ("abc", "{F} Una estudiante escribe: «A veces se guarda por costumbre y otras veces por no querer despedirse». ¿Qué recurso usa para ajustar lo que afirma?", "Matiz, con «a veces… otras veces»", "Generalización apresurada", "Contraargumento", "«A veces» y «otras veces» limitan el alcance de lo que afirma."),
        ("abc", "{F} ¿Qué reflexión es más fácil de refutar con un solo caso?", "R1", "R2", "Ninguna", "Afirma sobre todos los jóvenes; un solo caso contrario la refuta."),
        ("ab", "{F} R2 dice que el pasaje no define cuál es la razón de Rita. ¿Es una debilidad?", "No: es un matiz que reconoce lo que el texto no dice", "Sí: toda reflexión debe afirmar con seguridad total", "Reconocer los límites del texto es parte de una reflexión honesta."),
        ("abc", "{F} ¿Cuál es un matiz apropiado para corregir R1?", "«Algunas personas jóvenes guardan cosas porque les cuesta soltar»", "«Todos los jóvenes son iguales»", "«Nadie guarda cosas»", "Cambia «todos» por «algunas», lo que ajusta el alcance."),
        ("abc", "{F} ¿Cuál es un contraargumento a la tesis «guardar es una forma de recordar»?", "Alguien podría decir que se guarda por simple costumbre, sin pensar en recordar", "Guardar es una forma de recordar", "Rita guarda cosas", "Una razón que va en contra de la tesis es un contraargumento."),
        ("abc", "{F} Después de plantear un contraargumento a tu tesis, ¿qué conviene hacer?", "Responderlo con evidencia, por ejemplo con un pasaje del texto", "Dejarlo sin respuesta para no debilitar la tesis", "Cambiar de tesis sin pensarlo", "Un contraargumento fortalece la reflexión cuando se responde con evidencia."),
        ("ab", "{F} Una compañera dice que R1 es verdadera «porque yo conozco a dos jóvenes que guardan cosas». ¿Es suficiente?", "No: dos casos no prueban algo sobre todos los jóvenes", "Sí: con dos casos basta para generalizar", "Una cantidad pequeña de casos no respalda una afirmación sobre todos."),
        ("abc", "{F} Se quiere mejorar R2 con un contraargumento. ¿Cuál agregarías?", "«Alguien podría pensar que Rita guarda por costumbre; sin embargo, el pasaje dice que el frasco se llenó y no supo qué hacer»", "«Rita es mala persona»", "«El frasco es de vidrio»", "Plantea una objeción y la responde con el texto."),
        ("abc", "{F} ¿Qué actitud tiene quien contrasta reflexiones para afinar la suya?", "Busca qué puede aprender de la otra reflexión", "Busca vencer al otro", "Evita leer otras reflexiones", "Contrastar es afinar la propia postura, no ganar."),
        ("abc", "{F} Un compañero responde a tu reflexión diciendo que eres «inmaduro». ¿Qué corresponde?", "Pedir que discuta tu argumento y no a la persona, y avisar a tu docente si persiste", "Responder con otro insulto", "Callarte para siempre", "La crítica debe dirigirse al argumento; el insulto se aborda con tu docente."),
    ],
    ctx=("abc", "Contexto: tu curso escribirá reflexiones sobre {F} para un panel de discusión. Quien modera pide que cada una plantee un contraargumento. ¿Cuál es la mejor estrategia?", "Elegir la objeción más fuerte y responderla con el pasaje", "Elegir una objeción muy débil para ganar fácil", "No incluir objeciones", "Una objeción fuerte, respondida con evidencia, fortalece la reflexión."),
    sc=[
        ("En Taller de literatura: ¿qué es un contraargumento?", "Una razón que va en contra de la propia tesis", "El contraargumento pone a prueba la tesis."),
        ("ab", "Matizar significa:", "Ajustar lo que se afirma a lo que se puede respaldar", "No afirmar nada", "El matiz limita el alcance con precisión."),
        ("ab", "«Todos los jóvenes…» es:", "Una generalización que requiere evidencia", "Un matiz", "Hablar de todos exige una evidencia que normalmente no se tiene."),
    ],
    op=("Con las reflexiones R1 y R2 de la ficha {F}: (1) explica en una oración por qué R2 es más sólida que R1; (2) reescribe R1 con un matiz; (3) escribe un contraargumento a la tesis de R2 y una respuesta apoyada en el pasaje.",
        "(1) R2 limita su alcance y reconoce lo que el texto no dice; R1 generaliza sobre todos. (2) A veces los jóvenes guardan cosas porque les cuesta soltar. (3) Contraargumento: alguien podría decir que Rita guarda por simple costumbre; respuesta: el pasaje dice que no supo qué hacer con el frasco lleno, lo que sugiere que no es solo costumbre.",
        ["comparación con criterio de alcance", "matiz que cambia el alcance", "contraargumento verosímil", "respuesta apoyada en el pasaje"],
        ["tres respuestas numeradas"],
        ["decir que R2 es mejor sin razón", "matiz que elimina la afirmación", "responder al contraargumento sin pasaje"],
        "Pregunta: «¿qué pasaría con tu reflexión si cambias ‘algunas’ por ‘todas’?»."),
    reinforce="Reescribe con un matiz esta generalización: «Nadie lee poesía hoy».",
    extend="Explica por qué considerar un contraargumento fuerte puede hacer más convincente una reflexión propia.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (plan de ejemplo). Reflexión: «guardar puede ser una forma de aplazar una despedida», a partir del pasaje del frasco de Rita (inventado). Tres audiencias posibles. A) El curso, en una lectura en voz alta de 5 minutos. "
     "B) La comunidad escolar, en un mural de 200 palabras. C) Una persona de tu casa, en una carta. Ritmo de lectura en voz alta de ejemplo: 100 palabras por minuto. Estructura de ejemplo: apertura, desarrollo con texto, yo y mundo, contraargumento y cierre.")
build(
    O6, 5, F,
    use="Aprenderé a planificar la comunicación de una reflexión a una audiencia: qué compartir, con qué tono, en qué formato y con qué estructura. Sirve para producir reflexiones claras y cuidadosas con las personas.",
    prior=["Sé conectar texto, yo y mundo.", "Sé plantear un contraargumento.", "Sé calcular duraciones."],
    explain=[
        "Planificar una reflexión es decidir antes de escribir. Primero, la audiencia: no se escribe igual para el curso, para la comunidad escolar o para una persona cercana. La audiencia define el tono (más formal o más íntimo), la cantidad de contexto (presentar el pasaje o no) y lo que conviene compartir. Una carta a alguien de tu casa admite confidencias que un mural público no debería incluir.",
        "Segundo, el formato y el tiempo. Una lectura en voz alta de cinco minutos, a un ritmo de 100 palabras por minuto, permite unas 500 palabras. Un mural de 200 palabras exige síntesis. Una carta puede ser más libre. Calcular la extensión evita textos que no caben en el tiempo o en el espacio. Tercero, la estructura: apertura con la pregunta, desarrollo (texto, yo y mundo), contraargumento y cierre.",
        "Cuarto, el cuidado. Una reflexión pública debe respetar la privacidad propia y ajena: no incluyas datos personales que no quieras que todos lean ni asuntos íntimos de otras personas. Si el tema te remueve emociones fuertes, puedes escribirlo para ti y conversarlo con una persona adulta de confianza, sin necesidad de publicarlo. Decidir qué se comparte es parte de la reflexión.",
    ],
    vocab=[("audiencia", "personas a quienes se dirige el texto"), ("tono", "actitud de la voz del texto: formal, cercano, íntimo"), ("formato", "forma de presentar el texto: lectura, mural, carta"), ("estructura", "organización de las partes del texto"), ("síntesis", "expresión breve de lo esencial")],
    worked=[
        ("Calcular la extensión", "Una lectura de 5 minutos a 100 palabras por minuto. ¿Cuántas palabras caben?",
         ["Se multiplica la duración por el ritmo.", "5 por 100 es 500."],
         "500 palabras"),
        ("Elegir qué compartir", "Quieres incluir en un mural público un conflicto familiar. ¿Qué decides?",
         ["El mural lo ve toda la comunidad.", "Un conflicto familiar es un asunto íntimo.", "Decides no incluirlo y usar un ejemplo general, y lo conversas con una persona de confianza si te preocupa."],
         "No incluirlo en el mural"),
    ],
    mistakes=[("Escribir el mismo texto para cualquier audiencia.", "La audiencia cambia el tono, el contexto y lo que conviene compartir.", "Define la audiencia antes de escribir y ajusta el texto."),
              ("Compartir en un espacio público datos íntimos propios o de otras personas.", "Un texto público lo ve cualquiera y no se puede retirar de la memoria de quien lo leyó.", "Decide qué compartir y usa ejemplos generales.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué define el tono de una reflexión?", "La audiencia y el propósito", "El tamaño de la letra", "El color de la hoja", "El tono se ajusta a quién lee y a lo que se quiere lograr."),
        ("{F} ¿Cuántas audiencias se proponen en la ficha?", "3", "La ficha propone A, B y C: tres audiencias."),
        ("=", "{F} Un texto tiene 400 palabras y se lee al ritmo de la ficha. ¿Cuántos minutos dura la lectura?", "400//100", "Se divide el número de palabras entre el ritmo de lectura.", " minutos"),
        ("=", "{F} El mural permite 200 palabras y tu borrador tiene 260. ¿Cuántas palabras debes cortar?", "260-200", "Se resta al borrador la extensión permitida.", " palabras"),
        ("abc", "{F} ¿Cuál audiencia permite más intimidad?", "C, una persona de tu casa", "B, la comunidad escolar", "A, el curso completo", "Una carta personal es un espacio más privado que un mural o una lectura en el curso."),
        ("abc", "{F} ¿Qué audiencia exige más síntesis?", "B, el mural de 200 palabras", "A, la lectura de 5 minutos", "C, la carta", "El mural tiene el menor espacio, así que obliga a sintetizar."),
        ("ab", "{F} Para la lectura en voz alta (A), ¿qué conviene hacer?", "Ensayarla y medir el tiempo", "Leerla sin haberla leído antes", "Un ensayo permite ajustar ritmo y duración antes de presentar."),
        ("=", "{F} Una lectura de 3 minutos con el ritmo de la ficha, ¿cuántas palabras permite?", "3*100", "Se multiplica la duración por el ritmo de lectura.", " palabras"),
        ("abc", "{F} ¿Dónde se ubica el contraargumento en la estructura de ejemplo?", "Después del desarrollo con texto, yo y mundo, y antes del cierre", "Antes de la apertura", "Después del cierre", "La estructura de la ficha pone el contraargumento entre el desarrollo y el cierre."),
        ("abc", "{F} En el mural, ¿qué sería mejor omitir?", "El nombre de una persona real con su problema personal", "La pregunta de reflexión", "La cita del pasaje", "Los asuntos íntimos de otras personas no deben publicarse."),
        ("abc", "{F} Una estudiante quiere escribir una reflexión muy íntima sobre una pérdida personal. ¿Qué opción es adecuada?", "Escribirla para sí y conversarla con una persona adulta de confianza, y compartir solo si desea", "Publicarla en el mural sin pensarlo", "Obligar a los demás a leerla", "Decidir qué compartir y buscar apoyo en una persona adulta es lo más cuidadoso."),
        ("abc", "{F} ¿Qué cambia al pasar de la audiencia A a la C?", "El tono se vuelve más personal y se necesita menos presentación del pasaje", "El pasaje desaparece", "Nada cambia", "En una carta a alguien cercano el tono es íntimo y el contexto puede ser menor."),
        ("abc", "{F} Elige el plan más completo para la audiencia A.", "Pregunta, pasaje, experiencia propia sin datos íntimos, contraargumento, cierre y ensayo con cronómetro", "Solo una cita larga", "Un texto sin tiempo definido", "El primer plan cubre estructura, cuidado y tiempo."),
    ],
    ctx=("abc", "Contexto: el liceo te pide una versión de tu reflexión sobre {F} para el mural de la comunidad, con un máximo de 200 palabras, y para una lectura en voz alta de 2 minutos. ¿Qué decisión es razonable?", "Escribir dos versiones: una breve de 200 palabras o menos y otra de unas 200 palabras para leer en 2 minutos", "Pegar la misma versión de 600 palabras en ambos", "No presentar nada", "Dos minutos a 100 palabras por minuto son 200 palabras; ambas versiones caben en 200."),
    sc=[
        ("En Taller de literatura: ¿qué define el formato de una reflexión?", "El espacio, el tiempo y la audiencia", "El formato se ajusta a dónde y cómo se comparte."),
        ("ab", "Antes de publicar una reflexión conviene:", "Decidir qué se comparte y cuidar la privacidad", "Publicarlo todo", "Compartir no obliga a contarlo todo."),
        ("ab", "Si el tema me remueve emociones fuertes puedo:", "Escribirlo para mí y hablar con una persona adulta de confianza", "Obligarme a publicarlo", "El cuidado propio es parte de la reflexión."),
    ],
    op=("Elige una audiencia de la ficha {F} (A, B o C) y escribe tu plan: (1) la audiencia y el tono; (2) la extensión máxima calculada, con la cuenta; (3) las cinco partes de la estructura con una idea para cada una; (4) una cosa que decides no compartir y por qué.",
        "(1) Mural de la comunidad; tono cercano pero respetuoso. (2) 200 palabras. (3) Apertura: ¿por qué guardamos lo que no usamos? Desarrollo con texto: el frasco de Rita. Yo y mundo: guardo mensajes antiguos; muchos lo hacen. Contraargumento: puede ser comodidad. Cierre: soltar también es recordar. (4) No comparto el nombre de quien me regaló esos mensajes, porque es un asunto de otra persona.",
        ["audiencia y tono", "extensión calculada", "cinco partes con ideas", "decisión de qué no compartir con razón"],
        ["plan de cuatro partes"],
        ["extensión sin cálculo", "estructura incompleta", "compartir datos íntimos de terceros"],
        "Pregunta: «¿cómo cambiaría tu plan si la audiencia fuera la carta C?»."),
    reinforce="Calcula cuántas palabras caben en una lectura de 4 minutos con el ritmo de la ficha y escribe qué recortarías de un borrador de 500.",
    extend="Explica por qué la misma reflexión puede necesitar tres versiones distintas según la audiencia.",
)

# ============================================================ OAC-06, clase 6
F = ("Ficha 6 (borrador y pauta de ejemplo). Borrador: «Yo creo que el texto de Rita habla de guardar cosas y yo tambien guardo cosas y creo que todos guardamos cosas porque es normal.» "
     "Pauta. a) Cita o menciona un pasaje del texto; b) incluye una experiencia propia sin nombres de terceros; c) no generaliza sobre todos; d) tiene una pregunta o idea de reflexión; e) sin faltas de ortografía. Límite de extensión: 150 palabras.")
build(
    O6, 6, F,
    use="Aprenderé a producir, revisar y editar una reflexión completa, usando una pauta, una revisión global y local y una edición final. Sirve para entregar una producción cuidada sobre mí, el mundo y mis lecturas.",
    prior=["Sé planificar una reflexión para una audiencia.", "Sé revisar globalmente y localmente.", "Sé usar una pauta y una bitácora."],
    explain=[
        "Producir una reflexión es un proceso de varias pasadas. Primero se escribe un borrador sin detenerse a corregir. Después se revisa con la pauta: se lee el texto y se comprueba cada criterio. Se empieza por lo global (¿hay pregunta o idea?, ¿hay pasaje?, ¿hay experiencia propia?, ¿se generaliza?) y luego por lo local (frases, repeticiones, ortografía). Por último viene la edición final: ajustar la extensión, el título y la presentación.",
        "El borrador de la ficha muestra problemas típicos. No cita ni menciona un pasaje concreto; la experiencia propia es vaga; generaliza con «todos guardamos cosas»; repite «guardar cosas» tres veces; y le falta una tilde en «tambien». Al revisar con la pauta, se detecta qué criterios no cumple y se decide qué cambiar. La bitácora de cambios registra qué se corrigió y con qué criterio.",
        "Antes de entregar, haz una lectura final en voz alta o a una persona de confianza, comprueba la extensión y verifica que no incluyes datos que no quieres compartir. También puedes dejar una nota: qué cambió desde el borrador, qué aprendiste de tu lectura y qué pregunta te quedó abierta. Una producción terminada no es una que no se puede mejorar, sino una que cumple su propósito y su pauta.",
    ],
    vocab=[("borrador", "primera versión de un texto, que se puede mejorar"), ("pauta", "lista de criterios con que se revisa un texto"), ("edición final", "ajuste último de extensión, título y presentación"), ("bitácora de cambios", "registro de qué se cambió, por qué y con qué criterio"), ("lectura final", "relectura previa a la entrega")],
    worked=[
        ("Revisar con la pauta", "¿Qué criterios de la pauta incumple el borrador?",
         ["a) No cita ninguna frase ni imagen del pasaje: solo dice que «habla de guardar cosas». Incumple.", "b) La experiencia propia es vaga («yo también guardo cosas») y no la desarrolla.", "c) Dice «todos guardamos»: generaliza.", "d) No plantea una pregunta; solo afirma que guardar es «normal».", "e) Escribe «tambien» sin tilde."],
         "a), c) y e) se incumplen; b) y d) quedan débiles"),
        ("Reescribir una oración", "Reescribe «creo que todos guardamos cosas porque es normal».",
         ["Elimina «todos»: se limita el alcance.", "Sustituye «es normal» por una razón concreta.", "Queda: «Creo que algunas personas guardan cosas para no despedirse».", "La nueva frase cumple el criterio c)."],
         "Algunas personas guardan cosas para no despedirse"),
    ],
    mistakes=[("Revisar solo la ortografía y entregar.", "El texto puede tener ortografía correcta y no cumplir el resto de la pauta.", "Revisa primero lo global y deja la ortografía para el final."),
              ("Entregar un borrador con la sensación de que «ya está bien».", "Sin comparar con la pauta no se sabe si cumple los criterios.", "Aplica cada criterio de la pauta y registra los cambios.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué orden sigue la revisión de una reflexión?", "Primero lo global y después lo local", "Primero la ortografía y después lo global", "Solo lo local", "Lo global puede cambiar lo que se conserva; lo local se pule al final."),
        ("{F} ¿Cuántas palabras tiene como máximo la reflexión según la pauta?", "150", "La ficha fija 150 palabras como límite de extensión."),
        ("{F} ¿Cuántos criterios tiene la pauta?", "5", "La pauta enumera a, b, c, d y e: cinco criterios."),
        ("abc", "{F} ¿Qué criterio incumple la frase «creo que todos guardamos cosas»?", "c), no generalizar sobre todos", "a), citar un pasaje", "e), ortografía", "Dice «todos», lo que generaliza sin evidencia suficiente."),
        ("abc", "{F} ¿Qué palabra del borrador necesita tilde?", "tambien", "guardar", "texto", "Esa palabra lleva tilde y debe escribirse «también»."),
        ("abc", "{F} ¿Qué criterio incumple el borrador al no citar ninguna frase ni imagen concreta del pasaje?", "a), citar o mencionar un pasaje", "b), experiencia propia", "d), pregunta", "No se refiere a ningún pasaje concreto."),
        ("=", "{F} El borrador mejorado tiene 190 palabras y el límite es 150. ¿Cuántas palabras debes cortar?", "190-150", "Se resta al borrador la extensión permitida.", " palabras"),
        ("=", "{F} Después de cortar 45 palabras de un borrador de 190, ¿cuántas palabras tiene?", "190-45", "Se resta lo cortado a la extensión inicial.", " palabras"),
        ("abc", "{F} Elige una reescritura que cumple a) y c).", "«En el pasaje, Rita llena un frasco y no sabe qué hacer; algunas personas guardan para no despedirse»", "«Todos guardamos cosas»", "«Rita guarda cosas, y yo también»", "Menciona el pasaje y limita el alcance con «algunas personas»."),
        ("abc", "{F} Una estudiante agrega una experiencia propia con el nombre y la enfermedad de su abuela. ¿Qué corresponde según la pauta?", "Quitar el nombre y los datos de salud, y usar un ejemplo general o propio", "Dejarlo porque da emoción", "Agregar más datos", "El criterio b) pide una experiencia propia sin nombres de terceros."),
        ("ab", "{F} ¿Para qué sirve la bitácora de cambios?", "Para registrar qué se cambió, por qué y con qué criterio", "Para esconder el borrador", "La bitácora muestra la mejora y permite explicar las decisiones."),
        ("abc", "{F} Antes de entregar, ¿qué haces?", "Releer en voz alta, comprobar la extensión y verificar qué estás compartiendo", "Entregar sin revisar", "Agregar más ideas sin límite", "La lectura final detecta fallas y confirma que cumples la pauta."),
        ("abc", "{F} Una compañera dice que su reflexión está «terminada» porque no tiene faltas de ortografía. ¿Qué respondes?", "Que también debe cumplir los demás criterios de la pauta", "Que tiene razón", "Que debe borrarla", "La ortografía es solo uno de cinco criterios."),
    ],
    ctx=("abc", "Contexto: en la sesión final del taller cada persona entrega su reflexión con el borrador, la pauta marcada y la bitácora. Para el borrador de la ficha {F}, ¿qué entrega demuestra mejor el proceso?", "Borrador, versión final, la pauta con cada criterio comprobado y una bitácora de cambios", "Solo la versión final", "Solo una lista de ideas", "El proceso se demuestra mostrando versiones, criterios y decisiones."),
    sc=[
        ("En Taller de literatura: ¿qué es la edición final de una reflexión?", "El ajuste último de extensión, título y presentación", "Es la última pasada antes de entregar."),
        ("ab", "Una producción está lista cuando:", "Cumple la pauta y su propósito", "Nunca se puede mejorar", "El criterio de cierre es la pauta, no la perfección."),
        ("ab", "Antes de compartir una reflexión debo comprobar:", "Qué datos propios y ajenos incluyo", "Solo el color de la hoja", "La privacidad es parte de la revisión."),
    ],
    op=("Con el borrador de la ficha {F}: (1) revisa cada criterio a) a e) y escribe sí o no con una razón; (2) escribe una versión final de máximo 150 palabras que cumpla la pauta, usando el pasaje del frasco de Rita; (3) cuenta tus palabras y anota tres cambios en una bitácora.",
        "(1) a) no; b) débil; c) no; d) no; e) no. (2) «Al leer que Rita llena un frasco con lo que no necesita y no sabe qué hacer, pensé en mi galería de fotos, que nunca miro. ¿Qué guardamos cuando guardamos? Quizás algunas personas guardan para no despedirse. Soltar, tal vez, también sea una forma de recordar.» (3) Cuento 46 palabras. Bitácora: citar el pasaje (criterio a); cambiar «todos» por «algunas personas» (criterio c); agregar pregunta (criterio d).",
        ["revisión de los cinco criterios con razón", "versión final de máximo 150 palabras", "conteo de palabras", "bitácora de tres cambios", "cumple la pauta"],
        ["revisión, versión final y bitácora"],
        ["revisar sin razón", "pasar de 150 palabras", "no usar el pasaje"],
        "Pregunta: «¿qué criterio de la pauta te costó más cumplir y cómo lo lograste?»."),
    reinforce="Escribe una pauta de cuatro criterios para revisar una reflexión tuya sobre una lectura distinta.",
    extend="Explica por qué revisar con una pauta escrita y llevar una bitácora hace más seria una producción creativa.",
)

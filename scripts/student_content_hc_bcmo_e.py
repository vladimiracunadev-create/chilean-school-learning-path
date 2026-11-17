"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-05 (relación entre estructura y función de proteínas, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así, con unidades arbitrarias) y están escritos completos en el enunciado: no necesitas laboratorio, microscopio ni internet. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos: los resultados que se analizan se entregan ya escritos. Los esquemas se dibujan a mano con lápiz y papel. "
             "Los números de ejemplo sirven para razonar, no para medir procesos reales.")
build = make_build(MATERIALS)

O5 = "CN-BCMO-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (proteína de ejemplo, inventada). Proteína PX: cadena de aminoácidos en este orden: Ala, Lys, Glu, Leu, Gly, Ser. "
     "Niveles de estructura: primaria, la secuencia de aminoácidos; secundaria, plegamientos locales regulares como la hélice y la lámina; terciaria, la forma tridimensional de toda la cadena; cuaternaria, la unión de varias cadenas. "
     "Dato de ejemplo: si en PX se cambia Glu por otro aminoácido, la proteína ya no se pliega bien y pierde su función.")
build(
    O5, 1, F,
    use="Aprenderé cómo la secuencia de aminoácidos determina la forma de una proteína y cómo la forma determina su función. Sirve para explicar por qué un pequeño cambio puede alterar el funcionamiento de una proteína.",
    prior=["Sé que las proteínas son cadenas de aminoácidos.", "Sé traducir un mensajero a aminoácidos.", "Sé qué es una enzima."],
    explain=[
        "Una proteína es una cadena de aminoácidos que se pliega en una forma tridimensional precisa. La estructura primaria es la secuencia de aminoácidos, determinada por el gen. La secundaria son plegamientos locales regulares, como la hélice y la lámina. La terciaria es el plegamiento de toda la cadena, que da la forma final. La cuaternaria aparece cuando varias cadenas se unen para formar una proteína completa, como ocurre en la hemoglobina.",
        "La forma depende de la secuencia, porque los aminoácidos tienen propiedades distintas (algunos se atraen entre sí, otros rechazan el agua) y esas propiedades guían el plegamiento. La función depende de la forma: una enzima necesita una cavidad con la forma justa para su sustrato, y una proteína de transporte necesita un hueco por donde pase una sustancia. Si cambia la forma, cambia la función.",
        "La desnaturalización es la pérdida de la forma de una proteína por condiciones como una temperatura muy alta o un pH extremo. Como la forma se pierde, también se pierde la función, aunque la secuencia de aminoácidos siga igual. Un cambio de un solo aminoácido puede alterar la forma, pero no siempre: depende de cuál es el aminoácido y de dónde está en la cadena.",
    ],
    vocab=[("estructura primaria", "secuencia de aminoácidos"), ("estructura terciaria", "forma tridimensional de toda la cadena"), ("estructura cuaternaria", "unión de varias cadenas en una proteína"), ("desnaturalización", "pérdida de la forma de una proteína por calor o pH extremo"), ("plegamiento", "proceso por el que la cadena adquiere su forma")],
    worked=[
        ("Identificar el nivel", "La secuencia Ala, Lys, Glu, Leu, Gly, Ser de PX, ¿qué nivel de estructura es?",
         ["Una lista ordenada de aminoácidos es la secuencia.", "La secuencia es la estructura primaria."],
         "Estructura primaria"),
        ("Posibles secuencias", "¿Cuántas cadenas distintas de 2 aminoácidos se pueden formar con 20 tipos de aminoácidos?",
         ["En la primera posición hay 20 opciones.", "En la segunda también hay 20.", "20 × 20 = 400."],
         "400"),
    ],
    mistakes=[("Decir que la desnaturalización rompe la secuencia de aminoácidos.", "Cambia la forma, no la secuencia primaria.", "Escribe «pierde su forma, aunque la secuencia sigue igual»."),
              ("Creer que cualquier cambio de aminoácido destruye la proteína.", "Depende del aminoácido y de su posición; algunos cambios son casi neutros.", "Analiza si el cambio altera la forma.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es la estructura primaria de una proteína?", "La secuencia de aminoácidos", "La forma tridimensional", "La unión de varias cadenas", "La estructura primaria es el orden de los aminoácidos."),
        ("{F} ¿Cuántos aminoácidos tiene la proteína PX?", "6", "La ficha enumera seis aminoácidos en la cadena."),
        ("{F} ¿Qué aminoácido ocupa la tercera posición de PX?", "Glu", "En orden: Ala, Lys, Glu, así que el tercero es Glu."),
        ("abc", "{F} ¿Qué nivel describe la forma tridimensional de toda la cadena?", "El terciario", "El primario", "El cuaternario", "La estructura terciaria es la forma global de la cadena."),
        ("ab", "{F} ¿De qué depende la forma de una proteína?", "De la secuencia de aminoácidos", "Del tamaño de la célula", "Las propiedades de los aminoácidos guían el plegamiento."),
        ("{F} ¿Cómo se llama la pérdida de forma por calor o pH extremo?", "Desnaturalización", "La desnaturalización es la pérdida de la forma de la proteína."),
        ("=", "¿Cuántas cadenas distintas de 3 aminoácidos se pueden formar con 20 tipos de aminoácidos?", "20*20*20", "En cada una de las tres posiciones hay 20 opciones, así que se multiplican.", " cadenas"),
        ("=", "Una proteína de ejemplo tiene 150 aminoácidos. ¿Cuántas bases tiene la parte del mensajero que la codifica, sin contar la parada?", "150*3", "Cada aminoácido corresponde a un codón de tres bases.", " bases"),
        ("abc", "{F} Se cambia Glu por otro aminoácido y la proteína ya no funciona. ¿Qué explicación es más razonable?", "El cambio alteró el plegamiento y por tanto la forma", "La proteína dejó de tener aminoácidos", "El cambio borró el gen", "Si cambia el plegamiento, cambia la forma y, con ella, la función."),
        ("abc", "{F} Se calienta una proteína de ejemplo y pierde la función. ¿Qué cambió?", "Su forma, aunque la secuencia sigue igual", "Su secuencia de aminoácidos", "Su gen", "La desnaturalización cambia la forma, no la secuencia."),
        ("ab", "Una compañera dice: «cualquier cambio de un aminoácido destruye la proteína». ¿Qué corriges?", "Depende de cuál aminoácido y de dónde esté", "Tiene razón en todo", "Algunos cambios son casi neutros y otros alteran la forma."),
        ("abc", "{F} Si PX se une a otra cadena igual para formar una proteína de dos cadenas, ¿qué nivel de estructura aparece?", "La estructura cuaternaria", "La estructura primaria", "La estructura secundaria", "La unión de varias cadenas es el nivel cuaternario."),
        ("abc", "Dos proteínas de ejemplo tienen la misma secuencia, pero una está desnaturalizada. ¿Cuál no funciona?", "La desnaturalizada, porque perdió su forma", "La otra, porque tiene la misma secuencia", "Ninguna, porque la secuencia es igual", "La función depende de la forma; la secuencia sola no basta."),
    ],
    ctx=("abc", "Contexto: en tu liceo una compañera pregunta por qué un alimento rico en proteínas cambia de aspecto al calentarse. Con lo visto, ¿cómo lo explicas en una frase?", "Las proteínas se desnaturalizan con el calor: cambian de forma", "Los aminoácidos desaparecen", "El calor produce nuevas proteínas", "El calor desnaturaliza las proteínas, cambiando su forma."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la desnaturalización?", "La pérdida de la forma de una proteína por calor o pH extremo", "La proteína pierde su forma y su función."),
        ("ab", "La función de una proteína depende de:", "Su forma", "Su color", "La forma determina qué puede hacer."),
        ("ab", "La estructura primaria es:", "La secuencia de aminoácidos", "La unión de cadenas", "Primaria significa el orden de los aminoácidos en la cadena."),
    ],
    op=("Con la proteína PX de la ficha {F}: (1) escribe qué nivel de estructura es cada una de estas ideas: la secuencia, la forma de toda la cadena y la unión de dos cadenas; (2) explica con tus palabras cómo un cambio de un aminoácido podría alterar la función; (3) escribe una condición que desnaturaliza una proteína y qué ocurre con la función.",
        "(1) Primaria, terciaria y cuaternaria. (2) El cambio puede alterar el plegamiento y así la forma, y con ella lo que la proteína puede hacer. (3) El calor excesivo: la proteína pierde su forma y su función.",
        ["tres niveles correctamente asociados", "explicación de la relación secuencia, forma y función", "condición de desnaturalización con consecuencia"],
        ["tres respuestas numeradas"],
        ["decir que la desnaturalización rompe la secuencia", "no mencionar la forma", "asociar mal los niveles"],
        "Pregunta: «¿qué cambio de aminoácido sería menos probable que altere la forma?»."),
    reinforce="Dibuja un esquema de cuatro cajas con los cuatro niveles de estructura y una frase corta para cada uno.",
    extend="Explica por qué dos proteínas con funciones distintas deben tener formas distintas, usando un ejemplo inventado.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (datos de ejemplo; unidades arbitrarias de velocidad de reacción). Una enzima actúa sobre su sustrato en su sitio activo y forma un producto. "
     "Velocidad según la temperatura: 10 °C: 20; 20 °C: 40; 30 °C: 70; 40 °C: 100; 50 °C: 30; 60 °C: 0. "
     "Velocidad según el pH: pH 4: 10; pH 6: 50; pH 7: 100; pH 8: 60; pH 10: 5. "
     "Velocidad según la cantidad de sustrato (con la misma cantidad de enzima): 1: 10; 2: 20; 4: 40; 8: 70; 16: 90; 32: 95.")
build(
    O5, 2, F,
    use="Aprenderé cómo funciona una enzima, por qué es específica y cómo la temperatura, el pH y la cantidad de sustrato cambian su actividad. Sirve para interpretar gráficos y tablas de actividad enzimática.",
    prior=["Sé que las enzimas son proteínas.", "Sé que la forma de una proteína determina su función.", "Sé leer una tabla de datos."],
    explain=[
        "Una enzima acelera una reacción química sin consumirse. El sustrato es la molécula sobre la que actúa, y el producto, la molécula que resulta. La enzima tiene una región llamada sitio activo, con una forma y una química que encajan con su sustrato. Por eso cada enzima es específica: solo actúa sobre sustratos que calzan en su sitio activo.",
        "Las enzimas aceleran reacciones porque disminuyen la energía de activación, la energía que hay que dar para que la reacción parta. La actividad depende de las condiciones. Con la temperatura, la velocidad aumenta hasta un óptimo y luego cae porque la enzima se desnaturaliza. El pH también tiene un óptimo. Con más sustrato, la velocidad sube y luego se estabiliza porque todas las enzimas están ocupadas.",
        "Un inhibidor es una molécula que reduce la actividad de una enzima, por ejemplo ocupando su sitio activo. Muchos medicamentos actúan así, aunque su uso lo decide un profesional. En los datos de ejemplo se debe identificar la variable que cambia, la que se mide y lo que se mantiene constante, y no concluir más allá de lo que muestran los números.",
    ],
    vocab=[("sustrato", "molécula sobre la que actúa una enzima"), ("sitio activo", "región de la enzima donde se une el sustrato"), ("energía de activación", "energía necesaria para que una reacción comience"), ("óptimo", "condición en la que la actividad es máxima"), ("inhibidor", "molécula que reduce la actividad de una enzima")],
    worked=[
        ("Hallar el óptimo", "Con los datos de temperatura, ¿cuál es la temperatura óptima?",
         ["La velocidad máxima es 100.", "Ocurre a 40 °C."],
         "40 °C"),
        ("Interpretar la caída", "¿Por qué la velocidad baja a 30 unidades a los 50 °C, si a 40 °C era 100?",
         ["Una temperatura alta desnaturaliza la enzima.", "Al perder la forma, el sitio activo ya no encaja con el sustrato."],
         "La enzima se desnaturaliza y pierde actividad"),
    ],
    mistakes=[("Pensar que la enzima se gasta en la reacción.", "La enzima no se consume: queda libre para actuar de nuevo.", "Escribe «acelera sin consumirse»."),
              ("Creer que más temperatura siempre acelera la enzima.", "Pasado el óptimo, la enzima se desnaturaliza y su actividad cae.", "Describe el aumento hasta el óptimo y la caída posterior.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es el sitio activo de una enzima?", "La región donde se une el sustrato", "El gen que la fabrica", "El producto de la reacción", "El sitio activo es donde el sustrato encaja y reacciona."),
        ("{F} ¿Cuál es la velocidad a 20 °C?", "40", "La ficha indica 40 unidades a 20 °C."),
        ("{F} ¿A qué pH la velocidad es máxima?", "7", "Con pH 7 la velocidad es 100, el valor más alto de la tabla."),
        ("abc", "{F} ¿Qué ocurre con la velocidad al pasar de 40 °C a 60 °C?", "Disminuye hasta 0", "Aumenta", "Se mantiene en 100", "La velocidad cae de 100 a 0, porque la enzima se desnaturaliza."),
        ("ab", "{F} ¿Por qué una enzima es específica?", "Porque su sitio activo solo encaja con ciertos sustratos", "Porque se gasta en la reacción", "La forma del sitio activo determina qué sustrato puede unirse."),
        ("{F} ¿Con qué cantidad de sustrato la velocidad es 70?", "8", "La tabla asigna 70 a la cantidad de sustrato 8."),
        ("=", "{F} ¿Cuántas unidades más de velocidad hay a 40 °C que a 10 °C?", "100-20", "Se resta la velocidad a 10 °C de la velocidad a 40 °C.", " unidades"),
        ("=", "{F} ¿Cuántas veces mayor es la velocidad a pH 7 que a pH 4?", "100/10", "Se divide la velocidad a pH 7 por la velocidad a pH 4.", " veces"),
        ("abc", "{F} Pasando de 16 a 32 de sustrato, la velocidad sube solo de 90 a 95. ¿Qué indica?", "Que casi todas las enzimas ya están ocupadas", "Que la enzima se desnaturalizó", "Que el sustrato no sirve", "Con mucho sustrato casi todas las enzimas ya están ocupadas, y la velocidad se estabiliza."),
        ("abc", "{F} Una enzima de ejemplo se usa a 55 °C. ¿Qué esperas, comparando con la tabla?", "Una actividad muy baja por desnaturalización parcial", "La actividad máxima", "Una actividad igual a la de 20 °C", "A 50 °C la velocidad ya es 30 y a 60 °C es 0, así que a 55 °C es baja."),
        ("ab", "Una compañera dice: «mientras más calor, mejor trabaja siempre la enzima». ¿Qué corriges?", "Hay un óptimo y luego la enzima se desnaturaliza", "Tiene razón: sube siempre", "La tabla muestra que a 50 °C ya cae la actividad."),
        ("abc", "{F} Un inhibidor ocupa el sitio activo de la enzima de ejemplo. ¿Qué esperas?", "Que la velocidad baje, porque el sustrato no puede unirse", "Que la velocidad suba", "Que el inhibidor no tenga efecto", "Un inhibidor que ocupa el sitio activo impide la unión del sustrato."),
        ("abc", "{F} Para estudiar el efecto del pH, ¿qué variables deben mantenerse constantes?", "La temperatura y la cantidad de enzima y de sustrato", "El pH", "Ninguna", "Para atribuir el efecto al pH, lo demás debe permanecer igual."),
    ],
    ctx=("abc", "Contexto: para un afiche del liceo sobre alimentos debes explicar por qué algunas enzimas de los alimentos dejan de actuar al calentarlos. ¿Qué mensaje eliges?", "El calor desnaturaliza las enzimas, que pierden su forma y dejan de actuar", "El calor crea más enzimas", "Las enzimas se gastan al calentarlas", "La desnaturalización explica la pérdida de actividad."),
    sc=[
        ("En Biología celular y molecular: ¿qué es el sustrato?", "La molécula sobre la que actúa una enzima", "El sustrato se une al sitio activo."),
        ("ab", "La energía de activación es la energía:", "Necesaria para que la reacción comience", "Que sobra al final", "Las enzimas disminuyen esa energía y por eso aceleran la reacción."),
        ("ab", "Una enzima:", "No se consume en la reacción", "Se gasta en cada reacción", "Una enzima queda libre y se reutiliza en nuevas reacciones."),
    ],
    op=("Con las tres tablas de la ficha {F}: (1) escribe la temperatura óptima y el pH óptimo; (2) explica con una frase por qué la velocidad con mucho sustrato deja de aumentar; (3) predice la velocidad a 70 °C y justifica con la tabla.",
        "(1) 40 °C y pH 7. (2) Porque todas las enzimas ya están ocupadas y no puede aumentar. (3) Cercana a 0, porque a 60 °C ya es 0 y la enzima está desnaturalizada.",
        ["óptimos correctos", "explicación de la saturación", "predicción coherente con la tabla"],
        ["tres respuestas numeradas"],
        ["leer mal la tabla", "no mencionar que todas las enzimas están ocupadas", "predecir un aumento a 70 °C"],
        "Pregunta: «¿qué otro dato necesitarías para predecir con más seguridad?»."),
    reinforce="Dibuja una enzima, su sustrato y el producto en tres pasos y rotula el sitio activo.",
    extend="Explica por qué dos enzimas distintas pueden tener óptimos de pH muy diferentes, sin que una sea mejor que la otra.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (modelo y datos de ejemplo de proteínas de membrana). Canal iónico: proteína que forma un poro y cambia de forma (abierto o cerrado) según una señal; deja pasar un tipo de ion a favor de su concentración, sin gastar ATP. "
     "Bomba de sodio y potasio: proteína que, en cada ciclo, saca 3 iones de sodio, mete 2 iones de potasio y gasta 1 ATP; trabaja en contra de la concentración de ambos. "
     "Datos de ejemplo: concentración del ion X: afuera 10, adentro 2 (unidades arbitrarias).")
build(
    O5, 3, F,
    use="Aprenderé cómo la estructura de las proteínas de membrana, sus cambios de forma, permiten el paso de iones: canales y bombas. Sirve para explicar cómo la célula mantiene concentraciones distintas a cada lado de la membrana.",
    prior=["Conozco la membrana celular.", "Sé qué es el transporte pasivo y el activo.", "Sé que la forma de una proteína determina su función."],
    explain=[
        "Los iones, como el sodio y el potasio, tienen carga y no atraviesan la bicapa de lípidos. Cruzan por proteínas de membrana. Los canales iónicos son proteínas que forman un poro con la forma y la carga adecuadas para un ion; pueden abrirse o cerrarse por un cambio de forma cuando reciben una señal, como una molécula que se une o un cambio de voltaje. A través de un canal abierto, el ion se mueve a favor de su concentración, sin gastar ATP.",
        "Las bombas son proteínas que mueven iones en contra de su concentración. La bomba de sodio y potasio cambia de forma en cada ciclo: se une a 3 iones de sodio, gasta un ATP y cambia de forma para soltarlos afuera; luego se une a 2 de potasio y cambia de forma para soltarlos adentro. Es un ejemplo claro de que un cambio de forma, impulsado por energía, realiza un trabajo.",
        "Estas proteínas mantienen la diferencia de concentración de iones entre el interior y el exterior de la célula. Esa diferencia es la base de la señal nerviosa y de muchas otras funciones. Cuando un canal se abre, los iones entran o salen y cambian la carga eléctrica de la membrana. Así la estructura de una proteína explica una función celular completa.",
    ],
    vocab=[("canal iónico", "proteína que forma un poro por donde pasa un tipo de ion a favor de su concentración"), ("bomba", "proteína que mueve iones en contra de su concentración gastando ATP"), ("cambio conformacional", "cambio de forma de una proteína"), ("gradiente de concentración", "diferencia de concentración a ambos lados de la membrana"), ("ion", "partícula con carga eléctrica")],
    worked=[
        ("Dirección por un canal abierto", "El ion X tiene concentración 10 afuera y 2 adentro, y su canal se abre. ¿Hacia dónde se mueve?",
         ["Un canal permite el paso a favor de la concentración.", "Hay más afuera que adentro."],
         "Hacia adentro"),
        ("Contar ciclos de la bomba", "En 5 ciclos de la bomba de sodio y potasio, ¿cuántos iones de sodio salen?",
         ["Cada ciclo saca 3 iones de sodio.", "5 × 3 = 15."],
         "15 iones de sodio"),
    ],
    mistakes=[("Decir que el canal «empuja» los iones gastando ATP.", "Un canal solo abre un camino; el ion se mueve a favor de su concentración sin gasto de ATP.", "Reserva el gasto de ATP para las bombas."),
              ("Creer que las bombas igualan las concentraciones.", "Las bombas mantienen la diferencia, moviendo iones en contra de su concentración.", "Describe a la bomba como mantenedora del gradiente.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un canal iónico?", "Una proteína que forma un poro por donde pasa un ion a favor de su concentración", "Un organelo que gasta ATP", "Un lípido de la membrana", "Un canal es una proteína con poro que permite el paso pasivo de un ion."),
        ("{F} ¿Cuántos iones de sodio saca la bomba en un ciclo?", "3", "La ficha indica que saca 3 iones de sodio por ciclo."),
        ("{F} ¿Cuántos ATP gasta la bomba por ciclo?", "1", "La bomba gasta un ATP en cada ciclo."),
        ("abc", "{F} ¿Qué permite que un canal pase de cerrado a abierto?", "Un cambio de forma de la proteína", "Un cambio en la secuencia del gen", "La entrada de ADN", "El canal cambia de forma ante una señal y se abre."),
        ("ab", "{F} ¿Un canal abierto gasta ATP?", "No: el ion se mueve a favor de su concentración", "Sí: siempre gasta ATP", "El paso por canal es pasivo, sin gasto de ATP."),
        ("{F} ¿Cuántos iones de potasio mete la bomba en un ciclo?", "2", "La ficha indica que mete 2 iones de potasio por ciclo."),
        ("=", "{F} En 10 ciclos, ¿cuántos iones de sodio salen?", "3*10", "Cada ciclo saca 3 iones de sodio, así que se multiplica por el número de ciclos.", " iones"),
        ("=", "{F} En 15 ciclos, ¿cuántos iones de potasio entran?", "2*15", "Cada ciclo mete 2 iones de potasio, así que se multiplica por el número de ciclos.", " iones"),
        ("=", "{F} En 8 ciclos, ¿cuántos iones salen de sodio menos los que entran de potasio?", "3*8-2*8", "Cada ciclo saca 3 y mete 2, así que la diferencia total es la resta de ambos totales.", " iones"),
        ("abc", "{F} Si el canal del ion X se abre y no hay bombas, ¿qué pasará con las concentraciones con el tiempo?", "Tenderán a igualarse", "La diferencia aumentará", "No cambiarán nunca", "Sin bombas, el flujo a favor de la concentración reduce la diferencia."),
        ("abc", "{F} Una célula de ejemplo pierde ATP y su bomba se detiene. ¿Qué pasará con la diferencia de concentración a largo plazo?", "Disminuirá", "Aumentará", "Se mantendrá igual", "Sin ATP la bomba no mantiene la diferencia y los canales la deshacen."),
        ("ab", "Un compañero dice: «el canal gasta ATP para mover el ion». ¿Qué corriges?", "El canal es pasivo: el ion se mueve a favor de su concentración sin ATP", "Tiene razón: todo el transporte gasta ATP", "El gasto de ATP es de las bombas, no de los canales."),
        ("abc", "{F} ¿Por qué un cambio de forma de la bomba es esencial?", "Porque le permite pasar de unirse al ion a soltarlo del otro lado", "Porque la hace desaparecer", "Porque cambia el ADN", "Cada cambio de forma traslada los iones de un lado de la membrana al otro."),
    ],
    ctx=("abc", "Contexto: una compañera pregunta por qué las células necesitan ATP aunque los canales no lo usen. ¿Qué respondes?", "Porque las bombas lo gastan para mantener la diferencia de concentración que luego usan los canales", "Porque los canales usan mucho ATP", "No lo necesitan", "El ATP mantiene el gradiente que hace funcionar a los canales."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un cambio conformacional?", "Un cambio de forma de una proteína", "Es el cambio de forma que permite abrir un canal o mover un ion."),
        ("ab", "Una bomba mueve iones:", "En contra de su concentración", "A favor de su concentración", "Por eso la bomba necesita gastar ATP para funcionar."),
        ("ab", "Un canal abierto permite:", "Paso pasivo de un ion", "Paso con gasto de ATP", "El canal solo abre el camino."),
    ],
    op=("Con la ficha {F}: (1) dibuja la membrana con un canal abierto para el ion X y una bomba, y rotula flechas con la dirección de cada ion; (2) calcula cuántos iones de sodio salen y cuánto ATP se gasta en 12 ciclos; (3) explica con una frase por qué sin ATP se pierde el gradiente.",
        "(1) Flecha del ion X hacia adentro por el canal; flechas de sodio hacia afuera y de potasio hacia adentro por la bomba. (2) 36 iones de sodio y 12 ATP. (3) Porque sin ATP la bomba no mantiene la diferencia y los canales la deshacen.",
        ["esquema con direcciones correctas", "cálculos correctos", "explicación del papel del ATP"],
        ["un esquema, dos cálculos y una frase"],
        ["invertir la dirección del sodio", "decir que el canal gasta ATP", "calcular mal los totales"],
        "Pregunta: «¿qué pasaría si el canal se quedara siempre cerrado?»."),
    reinforce="Haz una tabla comparando canal y bomba: dirección, uso de ATP y cambio de forma.",
    extend="Explica cómo la diferencia de concentración de iones entre el interior y el exterior de una célula puede usarse como una forma de energía almacenada.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (modelo y datos de ejemplo de proteínas motoras). Las fibras de un músculo contienen filamentos de actina y filamentos de miosina. La cabeza de miosina se une a la actina, cambia de forma y tira de ella; luego el ATP hace que la cabeza se suelte y vuelva a su forma inicial, listo para repetir. "
     "El calcio permite que la miosina acceda a la actina. Los filamentos se deslizan entre sí y el sarcómero, la unidad de contracción, se acorta; los filamentos no cambian de largo. "
     "Datos de ejemplo: largo del sarcómero relajado: 20 unidades; contraído: 16 unidades. Otra proteína motora, la kinesina, avanza por microtúbulos llevando vesículas dentro de la célula.")
build(
    O5, 4, F,
    use="Aprenderé cómo los cambios de forma de las proteínas motoras producen movimiento: la contracción del músculo y el transporte dentro de la célula. Sirve para analizar con datos cómo la estructura de una proteína se relaciona con el movimiento.",
    prior=["Conozco el citoesqueleto.", "Sé qué es el ATP.", "Sé que las proteínas cambian de forma."],
    explain=[
        "Las proteínas motoras convierten la energía del ATP en movimiento. En el músculo, la actina y la miosina forman filamentos. La cabeza de la miosina tiene una forma que le permite unirse a la actina. Al unirse, cambia de forma y tira del filamento de actina; luego el ATP la suelta y la cabeza recupera su forma inicial. Repetido muchas veces por muchas cabezas, el filamento se desliza.",
        "El sarcómero es la unidad de contracción. Cuando se contrae, los filamentos de actina y de miosina se deslizan entre sí y el sarcómero se acorta, pero los filamentos mantienen su largo. El calcio es una señal: cuando aumenta, permite que la miosina acceda a la actina y comience la contracción; cuando baja, el músculo se relaja. Sin ATP, la miosina no se suelta de la actina.",
        "Otras proteínas motoras funcionan con el mismo principio de cambiar de forma usando ATP. La kinesina avanza por los microtúbulos transportando vesículas, y la dineína mueve cilios y flagelos. La motilidad de la célula, que es su capacidad de moverse o de mover sus partes, depende de estos cambios de forma de las proteínas y de la red del citoesqueleto.",
    ],
    vocab=[("miosina", "proteína motora que tira de la actina"), ("actina", "proteína que forma filamentos del citoesqueleto y del músculo"), ("sarcómero", "unidad de contracción del músculo"), ("proteína motora", "proteína que usa ATP para generar movimiento"), ("motilidad", "capacidad de moverse o de mover partes de la célula")],
    worked=[
        ("Calcular el acortamiento", "El sarcómero pasa de 20 a 16 unidades. ¿Cuánto se acorta?",
         ["Se resta el largo contraído del relajado.", "20 − 16 = 4."],
         "4 unidades"),
        ("Qué cambia y qué no", "Al contraerse, ¿cambia el largo de los filamentos de actina?",
         ["Los filamentos se deslizan entre sí.", "No cambian de largo; lo que se acorta es el sarcómero."],
         "No cambia"),
    ],
    mistakes=[("Decir que los filamentos se acortan al contraerse el músculo.", "Los filamentos se deslizan y mantienen su largo; se acorta el sarcómero.", "Escribe «se deslizan»."),
              ("Creer que el ATP solo sirve para unir la miosina a la actina.", "El ATP hace que la miosina se suelte y recupere su forma.", "Describe el ciclo: unión, cambio de forma, soltura con ATP.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es una proteína motora?", "Una proteína que usa ATP para generar movimiento", "Un organelo que fabrica ADN", "Un lípido de la membrana", "Las proteínas motoras usan ATP y cambian de forma para mover."),
        ("{F} ¿Cuál es el largo del sarcómero relajado?", "20 unidades", "La ficha indica 20 unidades en el estado relajado."),
        ("{F} ¿Qué proteína del músculo cambia de forma y tira de la actina?", "La miosina", "La cabeza de miosina cambia de forma y tira del filamento de actina."),
        ("abc", "{F} ¿Qué hace el ATP en el ciclo de la miosina?", "Hace que la cabeza se suelte de la actina y recupere su forma", "Fabrica nuevas moléculas de actina", "Copia el ADN", "El ATP suelta la miosina de la actina y la devuelve a su forma."),
        ("ab", "{F} Al contraerse el músculo, ¿qué se acorta?", "El sarcómero", "Los filamentos de actina", "Los filamentos mantienen su largo y se deslizan entre sí."),
        ("{F} ¿Qué proteína motora lleva vesículas por los microtúbulos?", "La kinesina", "La ficha menciona la kinesina como transportadora por microtúbulos."),
        ("=", "Un sarcómero de otra fibra de ejemplo mide 24 unidades relajado y 19 contraído. ¿Cuánto se acorta?", "24-19", "Se resta el largo contraído del largo relajado.", " unidades"),
        ("=", "Una fibra de ejemplo tiene 100 sarcómeros en fila, cada uno de 20 unidades relajado. ¿Cuántas unidades mide la fibra relajada?", "100*20", "Se multiplica el número de sarcómeros por el largo de cada uno.", " unidades"),
        ("=", "{F} La misma fibra de 100 sarcómeros se contrae y cada sarcómero mide 16. ¿Cuántas unidades se acorta la fibra?", "100*20-100*16", "Se resta el largo contraído total del largo relajado total.", " unidades"),
        ("abc", "{F} Si baja el calcio en una fibra de ejemplo, ¿qué esperas?", "Que la miosina no pueda acceder a la actina y el músculo se relaje", "Que se contraiga más", "Que se divida", "El calcio permite la unión de miosina y actina; sin él, no hay contracción."),
        ("abc", "{F} Una enfermedad de ejemplo impide que la miosina se suelte de la actina. ¿Qué proceso falla?", "El ciclo de unión y soltura, necesario para que el músculo se relaje", "La síntesis de ADN", "La digestión celular", "Sin soltura, la miosina queda unida y el ciclo no continúa."),
        ("ab", "Un compañero dice: «el calcio entrega la energía que mueve a la miosina». ¿Qué corriges?", "El calcio es una señal que permite el acceso; la energía viene del ATP", "Tiene razón: el calcio es la fuente de energía", "El calcio habilita la unión de miosina y actina, y el ATP aporta la energía del ciclo."),
        ("abc", "{F} ¿Qué tienen en común la miosina y la kinesina?", "Ambas cambian de forma usando ATP para producir movimiento", "Ambas son lípidos", "Ambas copian el ADN", "Son proteínas motoras que usan ATP."),
    ],
    ctx=("abc", "Contexto: en una clase de educación física del liceo, una estudiante pregunta qué pasa dentro del músculo cuando se contrae. ¿Qué respuesta, en una frase, es correcta?", "Los filamentos de actina y miosina se deslizan entre sí gracias a los cambios de forma de la miosina con ATP", "Los filamentos se acortan solos", "El músculo se contrae sin ninguna proteína", "La contracción se explica por el deslizamiento impulsado por la miosina."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un sarcómero?", "La unidad de contracción del músculo", "El sarcómero se acorta cuando los filamentos se deslizan."),
        ("ab", "El calcio en el músculo:", "Permite que la miosina acceda a la actina", "Fabrica ATP", "El calcio actúa como señal de contracción."),
        ("ab", "La kinesina transporta:", "Vesículas por los microtúbulos", "ADN por la membrana", "Es una proteína motora del transporte interno."),
    ],
    op=("Con el modelo de la ficha {F}: (1) escribe en orden los cuatro pasos del ciclo de la cabeza de miosina; (2) calcula cuánto se acorta una fibra de 50 sarcómeros si cada uno pasa de 20 a 16; (3) explica con una frase por qué el ATP es necesario tanto para contraerse como para relajarse.",
        "(1) Se une a la actina, cambia de forma, tira del filamento y el ATP la suelta. (2) 50 × 4 = 200 unidades. (3) Porque el ATP suelta la miosina; sin ATP queda unida y el músculo no puede relajarse.",
        ["cuatro pasos en orden", "cálculo correcto del acortamiento", "explicación del papel del ATP"],
        ["una lista, un cálculo y una frase"],
        ["omitir la soltura por ATP", "calcular mal el acortamiento", "decir que los filamentos se acortan"],
        "Pregunta: «¿qué pasaría con el ciclo si no hubiera calcio?»."),
    reinforce="Dibuja tres cuadros del ciclo de la miosina: unida, tirando y soltándose, y rotula el rol del ATP.",
    extend="Explica por qué el principio de cambiar de forma usando ATP sirve tanto para contraer un músculo como para transportar vesículas dentro de una célula.",
)

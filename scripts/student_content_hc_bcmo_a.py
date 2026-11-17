"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-01 (desarrollo histórico e interdisciplinar del conocimiento, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, microscopio ni internet. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos: los resultados que se analizan se entregan ya escritos. Si quieres ver células reales, pide a tu docente una demostración con muestras preparadas, bajo su supervisión. "
             "Las fechas se dan solo cuando son bien conocidas; en los demás casos se habla de siglos o épocas. Si dudas de un dato, contrástalo con tu docente.")
build = make_build(MATERIALS)

O1 = "CN-BCMO-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (resumen de ejemplo de hitos históricos). Registro 1: en el siglo XVII, un investigador observó con un microscopio simple una lámina muy delgada de corcho y dibujó pequeñas cavidades que llamó «celdillas». "
     "Registro 2: en el mismo siglo, otro investigador, con lentes muy bien pulidos, vio seres diminutos en una gota de agua de estanque. "
     "Registro 3: a mediados del siglo XIX se formuló que todos los seres vivos están formados por células y que toda célula proviene de otra célula. "
     "Registro 4: en el siglo XX, el microscopio electrónico permitió ver estructuras internas de la célula, los organelos.")
build(
    O1, 1, F,
    use="Aprenderé a delimitar una pregunta histórica sobre cómo surgió la idea de célula y a ver cómo los instrumentos de la física cambiaron lo que se podía preguntar. Sirve para entender que el conocimiento biológico se construye con evidencia, paso a paso.",
    prior=["Sé que los seres vivos están formados por células.", "Distingo una observación de una explicación.", "Sé leer una lista de hechos ordenados en el tiempo."],
    explain=[
        "La biología celular y molecular estudia la célula y las moléculas que la forman. Su historia empieza con un instrumento: el microscopio. Como el ojo no ve lo muy pequeño, los lentes de la óptica, rama de la física, abrieron un mundo nuevo. Cada vez que el instrumento mejoró, aparecieron estructuras que antes no se podían ver y, con ellas, preguntas nuevas.",
        "Una observación es lo que se ve con un instrumento y se registra. Una teoría es una explicación amplia, apoyada en muchas observaciones, que se puede poner a prueba. La teoría celular dice dos cosas: los seres vivos están formados por células, y toda célula proviene de otra célula. No salió de una sola observación, sino de muchas hechas por distintas personas durante mucho tiempo.",
        "Para investigar la historia, primero se delimita el sistema, es decir, la parte de la realidad que se estudia, y la pregunta. Por ejemplo, «¿cómo cambió lo que se podía ver de la célula al mejorar los instrumentos?». Una pregunta bien delimitada se puede responder con registros concretos, no con todo el pasado de la ciencia.",
    ],
    vocab=[("microscopio", "instrumento con lentes que agranda lo muy pequeño"), ("teoría celular", "explicación según la cual los seres vivos están hechos de células y toda célula viene de otra"), ("observación", "lo que se ve y se registra con un instrumento"), ("sistema", "parte de la realidad que se delimita para estudiarla"), ("organelo", "estructura con función propia dentro de la célula")],
    worked=[
        ("Observación o teoría", "El Registro 1 dice que se dibujaron celdillas en el corcho. ¿Es una observación o una teoría?",
         ["Pregunta: ¿describe lo visto con un instrumento o generaliza a todos los seres vivos?", "Describe una lámina concreta de corcho y lo dibujado.", "No generaliza a todos los seres vivos."],
         "Es una observación"),
        ("Delimitar una pregunta", "Quieres investigar la historia del microscopio en la biología. ¿Qué pregunta está mejor delimitada: «¿qué pasó en la ciencia?» o «¿qué estructuras permitió ver el microscopio electrónico que el óptico no mostraba?»",
         ["La primera abarca toda la ciencia y no se puede responder con pocos registros.", "La segunda nombra dos instrumentos y un resultado comparable.", "Se puede responder con el Registro 4 y los registros más antiguos."],
         "La segunda pregunta"),
    ],
    mistakes=[("Creer que la teoría celular la formuló una sola persona en un día.", "Se construyó con observaciones de muchas personas y épocas, y se fue corrigiendo.", "Habla de un proceso colectivo: observaciones, generalización y revisión."),
              ("Mezclar observación y teoría: «el corcho tiene celdillas, así que todo ser vivo tiene células».", "Una sola lámina no basta para generalizar a todos los seres vivos.", "Separa lo visto (observación) de lo que se concluye con muchas observaciones (teoría).")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué dice la teoría celular?", "Los seres vivos están formados por células y toda célula proviene de otra célula", "Solo los animales están formados por células", "Las células se forman solas a partir de materia sin vida", "La teoría celular tiene dos ideas: los seres vivos están hechos de células y toda célula viene de otra."),
        ("{F} ¿Qué registro (1, 2, 3 o 4) describe la formulación de la teoría celular?", "Registro 3", "El Registro 3 habla de una generalización a todos los seres vivos y del origen de toda célula."),
        ("{F} ¿Qué registro (1, 2, 3 o 4) menciona el instrumento que permitió ver los organelos?", "Registro 4", "Los organelos se vieron gracias al microscopio electrónico, mencionado en el Registro 4."),
        ("abc", "{F} ¿Por qué el Registro 1 es una observación y el Registro 3 una teoría?", "El 1 describe lo visto con un instrumento; el 3 generaliza a todos los seres vivos", "El 1 es falso y el 3 es verdadero", "El 1 es más reciente que el 3", "La observación registra lo visto; la teoría generaliza apoyándose en muchas observaciones."),
        ("ab", "{F} El microscopio nace de la óptica, rama de la física. ¿Cómo influyó en la biología según los registros?", "Cada mejora del instrumento permitió ver estructuras nuevas y plantear nuevas preguntas", "El instrumento no cambió las preguntas, solo las respuestas", "Los registros muestran que al mejorar el instrumento se vieron cosas nuevas, lo que abrió preguntas nuevas."),
        ("{F} ¿Qué registro (1, 2, 3 o 4) describe la observación de seres vivos completos en una gota de agua?", "Registro 2", "Los seres diminutos de la gota de estanque se mencionan en el Registro 2."),
        ("abc", "Una estudiante observa en una lámina de ejemplo muchas unidades pequeñas y separadas en una hoja. ¿Qué afirmación de la teoría celular apoya esa observación?", "Que los seres vivos están formados por células", "Que toda célula proviene de otra célula", "Que el microscopio electrónico siempre es necesario", "Ver células en una hoja apoya que los seres vivos tienen células; el origen de toda célula necesita otro tipo de evidencia."),
        ("=", "Un microscopio de ejemplo tiene un ocular de 10 aumentos y un objetivo de 40 aumentos, y el aumento total es el producto de ambos. ¿Cuántos aumentos totales tiene?", "10*40", "El aumento total es el producto de los aumentos del ocular y del objetivo.", " aumentos"),
        ("abc", "Un grupo quiere ver células de una lámina de hoja con el instrumento más sencillo que sirva. ¿Cuál elige?", "Un microscopio óptico", "Un microscopio electrónico, porque es el único que ve células", "Ningún instrumento: las células se ven a simple vista", "Las células se ven con el microscopio óptico; el electrónico se usa para estructuras internas más pequeñas."),
        ("abc", "{F} Alguien afirma: «el Registro 2 demuestra que toda célula proviene de otra». ¿Qué respondes?", "No: el Registro 2 solo describe seres diminutos observados; esa afirmación general está en el Registro 3", "Sí: el Registro 2 ya contiene toda la teoría", "Sí, porque el Registro 2 es más antiguo", "Observar seres diminutos no prueba de dónde proviene toda célula."),
        ("ab", "{F} ¿Qué pregunta se puede responder comparando los registros 1 y 4?", "¿Cómo cambió lo que se ve de la célula al mejorar los instrumentos?", "¿Quién fue la primera persona en usar un microscopio?", "Los registros 1 y 4 muestran qué se veía con instrumentos distintos, así que permiten esa comparación."),
        ("abc", "Para la pregunta «¿tienen células las hojas?», ¿cuál es un sistema bien delimitado?", "Una lámina muy delgada de hoja observada con un microscopio óptico", "Todos los seres vivos de la Tierra", "La historia completa de todos los instrumentos científicos", "Un sistema delimitado es una parte acotada y observable, como una lámina de hoja."),
        ("{F} Ordena por antigüedad, del más antiguo al más reciente, los registros 1, 3 y 4. Escribe los números separados por comas.", "1, 3, 4", "El Registro 1 es del siglo XVII, el 3 de mediados del XIX y el 4 del XX."),
    ],
    ctx=("abc", "Contexto: en la feria científica de tu liceo debes explicar en un cartel por qué el microscopio fue clave para la biología. ¿Qué mensaje central eliges?", "Al mejorar los instrumentos se vieron estructuras nuevas y la idea de célula se fue construyendo con muchas observaciones", "Una persona descubrió la célula sola y de una vez", "El microscopio es importante solo porque agranda cosas", "El mensaje correcto muestra la relación entre instrumento, observación y construcción colectiva de la teoría."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un organelo?", "Una estructura con función propia dentro de la célula", "El organelo es una parte de la célula con una función definida."),
        ("ab", "La teoría celular se apoya en:", "Muchas observaciones hechas por distintas personas", "Una sola observación de corcho", "Una teoría amplia necesita muchas observaciones y no una sola lámina."),
        ("ab", "Una pregunta bien delimitada:", "Se puede responder con registros concretos", "Abarca todo el pasado de la ciencia", "Delimitar significa acotar para poder responder con evidencia concreta."),
    ],
    op=("Con los registros de la ficha {F} haz lo siguiente: (1) escribe una pregunta histórica bien delimitada; (2) elige dos registros que sirvan de evidencia; (3) explica en dos oraciones qué respuesta provisoria darías y qué otro registro necesitarías para estar más seguro.",
        "(1) ¿Cómo cambió lo que se veía de la célula entre el siglo XVII y el XX? (2) Registros 1 y 4. (3) En el XVII se veían cavidades y seres diminutos; en el XX, organelos. Me faltaría un registro intermedio sobre mejoras de los lentes.",
        ["pregunta con sistema acotado", "dos registros elegidos con su número", "respuesta provisoria distinta de copiar el registro", "indica qué evidencia falta"],
        ["tres respuestas numeradas"],
        ["hacer una pregunta demasiado amplia", "citar un registro que no sirve a la pregunta", "no reconocer ninguna limitación"],
        "Pregunta: «¿qué registro te haría cambiar tu respuesta provisoria?»."),
    reinforce="Escribe tres frases: una observación, una teoría y una pregunta de investigación sobre las células, y rotula cada una.",
    extend="Explica por qué la mejora de un instrumento físico puede crear nuevas preguntas en la biología, usando un ejemplo de la ficha.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (datos de ejemplo inspirados en un experimento histórico). Se tienen dos tipos de bacterias: el tipo L, que forma colonias lisas, y el tipo R, que forma colonias rugosas. "
     "Al agregar al tipo R una sustancia extraída del tipo L, algunas bacterias R pasan a formar colonias lisas y esa característica se hereda a sus descendientes. "
     "Tabla de ejemplo (la sustancia extraída se trata antes con una enzima, que es una proteína que degrada un componente): enzima que degrada proteínas: la transformación ocurre; enzima que degrada ARN: la transformación ocurre; enzima que degrada ADN: la transformación no ocurre. "
     "Dato adicional de ejemplo: imágenes de difracción de rayos X de fibras de ADN muestran un patrón regular y repetitivo.")
build(
    O1, 2, F,
    use="Aprenderé cómo la química y la física permitieron identificar el ADN como material hereditario y descubrir su estructura. Sirve para ver cómo se evalúan fuentes y variables en un experimento histórico.",
    prior=["Sé que los rasgos se heredan.", "Sé qué es una enzima en términos generales.", "Sé leer una tabla de resultados."],
    explain=[
        "Durante mucho tiempo se discutió qué molécula guardaba la herencia: algunos pensaban en las proteínas, que son muy variadas, y otros en el ADN. Experimentos con bacterias mostraron que una sustancia podía transmitir una característica de una bacteria a otra. La pregunta fue: ¿qué componente de esa sustancia hace el trabajo? Para responder, se fueron destruyendo componentes uno por uno con enzimas específicas, y se miró si la transformación seguía ocurriendo.",
        "Esa lógica es la de controlar variables: se cambia una cosa a la vez y se observa el efecto. Si al destruir proteínas la transformación ocurre igual, las proteínas no eran necesarias. Si al destruir ADN la transformación desaparece, el ADN sí era necesario. Aquí la química aportó enzimas y métodos para separar componentes, y la física aportó la difracción de rayos X, que dio imágenes de la estructura regular del ADN.",
        "Con esas imágenes y con una regla química, que en el ADN la cantidad de adenina (A) es igual a la de timina (T) y la de guanina (G) igual a la de citosina (C), James Watson y Francis Crick propusieron en 1953 el modelo de doble hélice. Fue un trabajo colectivo que reunió datos de varios equipos, entre ellos las imágenes de rayos X obtenidas por Rosalind Franklin y Maurice Wilkins.",
    ],
    vocab=[("ADN", "molécula que guarda la información hereditaria"), ("enzima", "proteína que acelera una reacción química"), ("variable", "cantidad o condición que se puede cambiar o medir"), ("difracción de rayos X", "técnica de la física que da imágenes de la estructura regular de una molécula"), ("doble hélice", "forma de dos cadenas enrolladas del ADN")],
    worked=[
        ("Leer la tabla de enzimas", "Con los datos de la ficha, ¿qué componente de la sustancia no puede ser el responsable de la transformación: las proteínas o el ADN?",
         ["Se destruyen las proteínas y la transformación ocurre igual.", "Si fuera necesario, al destruirlo desaparecería la transformación.", "Eso ocurre al destruir ADN, no al destruir proteínas."],
         "Las proteínas no son necesarias; el ADN sí"),
        ("Completar proporciones de bases", "Una muestra de ADN de ejemplo tiene 22 % de adenina. ¿Qué porcentaje de guanina tiene?",
         ["Si A es 22 %, T también es 22 %: A y T suman 44 %.", "Quedan 100 − 44 = 56 % para G y C, que son iguales.", "G = 56 ÷ 2 = 28 %."],
         "28 %"),
    ],
    mistakes=[("Concluir que «las proteínas no existen en la sustancia» porque su destrucción no impidió la transformación.", "El resultado solo muestra que no eran necesarias para esa transformación.", "Escribe: «no eran necesarias para la transformación», no «no existían»."),
              ("Atribuir la doble hélice a una sola persona.", "El modelo usó datos de varios equipos: rayos X, proporciones químicas y construcción de modelos.", "Habla de un trabajo colectivo y nombra los aportes.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es el ADN?", "La molécula que guarda la información hereditaria de la célula", "Una proteína que acelera reacciones", "Un lípido que forma la membrana", "El ADN es el material de la herencia, no una enzima ni un lípido de la membrana."),
        ("{F} En la tabla de ejemplo, ¿con qué tipo de enzima (que degrada proteínas, ARN o ADN) la transformación no ocurre?", "Con la enzima que degrada ADN", "La tabla indica que al degradar el ADN la transformación no ocurre."),
        ("{F} ¿Qué tipo de colonias forman las bacterias R que se han transformado?", "Colonias lisas", "La transformación hace que las bacterias R pasen a formar colonias lisas, como las del tipo L."),
        ("abc", "{F} ¿Qué se concluye de la tabla de ejemplo?", "El ADN es necesario para la transformación", "Las proteínas son lo único necesario", "El ARN es lo único necesario", "Solo al destruir el ADN desaparece la transformación, por lo que el ADN es necesario."),
        ("ab", "{F} ¿Por qué se trató la sustancia con tres enzimas distintas y no con una sola?", "Para comprobar cuál componente era necesario, quitando uno a la vez", "Para aumentar la cantidad de sustancia", "Cada enzima quita un componente distinto, así se ve cuál es necesario."),
        ("{F} En el ADN de ejemplo, ¿qué relación hay entre la cantidad de adenina (A) y la de timina (T)?", "Son iguales", "En el ADN la cantidad de A es igual a la de T, lo que se usó para el modelo."),
        ("=", "Una muestra de ADN de ejemplo tiene 30 % de adenina. Como A es igual a T y G es igual a C, ¿qué porcentaje de guanina tiene?", "(100-30-30)/2", "Primero se restan A y T del total y lo que queda se reparte entre G y C.", " %"),
        ("=", "Otra muestra de ADN de ejemplo tiene 18 % de citosina. ¿Qué porcentaje de timina tiene?", "(100-18-18)/2", "Como C es igual a G, se restan ambas del total y el resto se reparte entre A y T, que son iguales.", " %"),
        ("abc", "Otro estudio de ejemplo repite el experimento: la transformación ocurre aunque se destruyan las proteínas, pero no si se destruye el ADN. ¿Qué hace este resultado?", "Refuerza la conclusión de que el ADN es necesario", "La contradice, porque las proteínas deberían ser necesarias", "No tiene relación con la conclusión", "Un resultado repetido por otros apoya la conclusión; no la contradice."),
        ("abc", "Un estudiante dice: «el experimento prueba que las proteínas no existen en la sustancia». ¿Qué falla en su razonamiento?", "Solo muestra que las proteínas no eran necesarias para la transformación, no que no existan", "Nada: está bien concluido", "Las proteínas sí son necesarias", "Destruir una molécula sin afectar el resultado indica que no es necesaria, no que esté ausente."),
        ("ab", "¿Qué aportó la química a este descubrimiento?", "Enzimas y métodos para separar y degradar componentes por separado", "El microscopio óptico con lentes más potentes", "La química permitió aislar y quitar componentes de la sustancia, que es lo que mostró cuál era necesario."),
        ("abc", "{F} El patrón regular y repetitivo en las imágenes de rayos X de fibras de ADN, ¿qué sugiere?", "Que el ADN tiene una estructura ordenada y repetitiva, compatible con una hélice", "Que el ADN es una proteína", "Que el ADN no tiene ninguna estructura", "Un patrón regular de difracción indica una estructura ordenada, base del modelo de hélice."),
        ("=", "Una muestra de ADN de ejemplo tiene 24 % de guanina. Como G es igual a C, ¿cuánto suman juntas la adenina y la timina?", "100-24-24", "Se resta del total lo que ocupan G y C; el resto es la suma de A y T.", " %"),
    ],
    ctx=("abc", "Contexto: tu curso prepara un mural sobre «cómo se supo que el ADN guarda la herencia». Debes elegir el título que mejor refleje la historia. ¿Cuál escoges?", "Muchas pruebas y varios equipos mostraron que el ADN es el material de la herencia", "Una persona descubrió el ADN en un día", "Las proteínas fueron siempre el material hereditario", "El título correcto muestra un proceso colectivo apoyado en evidencia química y física."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una enzima?", "Una proteína que acelera una reacción química", "Las enzimas son proteínas que aceleran reacciones, y algunas degradan componentes específicos."),
        ("ab", "Cambiar una sola condición a la vez permite:", "Saber cuál condición produce el efecto", "Obtener siempre el resultado esperado", "Controlar variables sirve para atribuir el efecto a una causa concreta."),
        ("ab", "El modelo de doble hélice fue un trabajo:", "Colectivo, con datos de varios equipos", "De una sola persona sin datos previos", "El modelo usó imágenes de rayos X y reglas químicas obtenidas por varios equipos."),
    ],
    op=("Con los datos de la ficha {F}: (1) escribe la pregunta que el experimento quiso responder; (2) explica en dos oraciones qué variable se cambió, qué se midió y qué resultado fue decisivo; (3) escribe una limitación del experimento (algo que no permite concluir).",
        "(1) ¿Qué componente de la sustancia hace que las bacterias R se transformen? (2) Se cambió la enzima aplicada y se midió si había transformación; fue decisivo que sin ADN no hubiera transformación. (3) No permite saber cómo el ADN guarda la información, solo que es necesario.",
        ["pregunta clara", "variable cambiada y variable medida", "resultado decisivo identificado", "limitación bien formulada"],
        ["tres respuestas numeradas"],
        ["confundir variable cambiada con variable medida", "concluir más de lo que muestran los datos", "no declarar ninguna limitación"],
        "Pregunta: «¿qué dato nuevo agregarías para reforzar la conclusión?»."),
    reinforce="Escribe en una tabla las tres enzimas, su resultado y qué indica cada resultado sobre el componente que degradan.",
    extend="Explica por qué se necesitaron datos de química, de física y de matemática (proporciones) para proponer el modelo de doble hélice.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (datos de ejemplo). Cultivo de bacterias de ejemplo en un medio con alimento suficiente: hora 0: 100 células; hora 1: 200; hora 2: 400; hora 3: 800. "
     "Recuento de ejemplo de células en tres campos de un microscopio: 12, 15 y 18. "
     "Dato de ejemplo: una imagen de 40 mm de largo de una célula, hecha con 400 aumentos; 1 mm equivale a 1.000 micrómetros (µm).")
build(
    O1, 3, F,
    use="Aprenderé cómo la matemática y otras disciplinas ayudan a construir modelos en biología celular: tablas, promedios, escalas y tasas. Sirve para interpretar datos de forma ordenada y reconocer los límites de un modelo.",
    prior=["Sé calcular promedios y multiplicar.", "Sé leer tablas de datos.", "Conozco unidades de longitud como milímetro."],
    explain=[
        "Un modelo es una representación simplificada de un fenómeno que permite explicar y predecir. En biología celular hay modelos matemáticos (una tabla o regla de crecimiento), modelos físicos (una maqueta) y modelos conceptuales (un diagrama). Todos dejan cosas fuera, por eso siempre hay que preguntar qué supone el modelo y hasta dónde sirve.",
        "La matemática ayuda de varias formas. El promedio resume varios recuentos en un valor, por ejemplo el número de células en varios campos del microscopio. La escala permite pasar del tamaño de la imagen al tamaño real: tamaño real = tamaño de la imagen ÷ aumentos. Una regla de crecimiento, como «se duplica cada hora», permite predecir cuántas células habrá más tarde, mientras el alimento alcance.",
        "La química aporta la composición de las moléculas, la física aporta la óptica, los rayos X y las cargas eléctricas de las membranas, y la informática analiza grandes cantidades de datos. Ningún modelo reemplaza a la evidencia: se contrasta con datos nuevos y se corrige si falla.",
    ],
    vocab=[("modelo", "representación simplificada que explica y predice un fenómeno"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("aumento", "cuántas veces se agranda una imagen respecto del tamaño real"), ("micrómetro (µm)", "milésima parte de un milímetro"), ("supuesto", "condición que un modelo da por cierta para funcionar")],
    worked=[
        ("Predecir con una regla", "Con la regla «se duplica cada hora» y 100 células al inicio, ¿cuántas habrá a las 2 horas?",
         ["En la hora 1: 100 × 2 = 200.", "En la hora 2: 200 × 2 = 400."],
         "400 células"),
        ("Pasar de la imagen al tamaño real", "Una imagen de 20 mm hecha con 100 aumentos, ¿qué tamaño real representa en micrómetros?",
         ["Tamaño real = 20 ÷ 100 = 0,2 mm, pero conviene evitar decimales: 20 mm son 20.000 µm.", "20.000 µm ÷ 100 = 200 µm."],
         "200 µm"),
    ],
    mistakes=[("Predecir sin considerar los supuestos: «habrá siempre el doble cada hora».", "La regla vale mientras haya alimento y espacio; el modelo supone condiciones constantes.", "Declara el supuesto antes de predecir."),
              ("Dividir por los aumentos sin pasar antes a micrómetros y dejar la unidad mezclada.", "Si se mezclan milímetros y micrómetros se obtienen valores incomparables.", "Convierte primero a la unidad que usarás y luego divide.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un modelo?", "Una representación simplificada que explica y predice un fenómeno", "Una copia exacta de la realidad", "Un resultado final que no se puede corregir", "Un modelo simplifica, por eso deja cosas fuera y puede ajustarse con nuevos datos."),
        ("{F} ¿Cuántas células hay en la hora 3 del cultivo de ejemplo?", "800", "La tabla de la ficha indica 800 células en la hora 3."),
        ("=", "{F} ¿Cuál es el promedio de los tres recuentos de células por campo?", "(12+15+18)/3", "El promedio suma los tres valores y divide por la cantidad de campos.", " células"),
        ("abc", "{F} ¿Qué regla describe el crecimiento de la tabla de ejemplo?", "Se duplica cada hora", "Aumenta 100 células cada hora", "Se mantiene constante", "De 100 a 200 y a 400 y a 800, cada valor es el doble del anterior."),
        ("ab", "{F} El cultivo de ejemplo crece con alimento suficiente. ¿Qué supuesto da por cierto la regla de duplicación?", "Que sigue habiendo alimento y espacio", "Que las células no necesitan alimento", "La duplicación solo se mantiene mientras los recursos alcanzan."),
        ("=", "{F} Si se mantuviera la duplicación, ¿cuántas células habría a la hora 5?", "100*2*2*2*2*2", "Se multiplica por 2 una vez por cada hora transcurrida desde las 100 células iniciales.", " células"),
        ("=", "{F} ¿Qué tamaño real, en micrómetros, tiene la célula de la imagen? Pasa primero los 40 mm a micrómetros.", "40*1000/400", "Los 40 mm son 40.000 µm y el tamaño real se obtiene dividiendo por los aumentos.", " µm"),
        ("=", "Una célula de ejemplo mide 50 µm de largo en la realidad. ¿Cuántos milímetros mide su imagen hecha con 200 aumentos? Recuerda que 1 mm son 1.000 µm.", "50*200/1000", "La imagen mide el tamaño real por los aumentos (10.000 µm); luego se pasa a milímetros dividiendo por 1.000.", " mm"),
        ("abc", "{F} Un estudiante predice que a la hora 10 habrá más de cien mil células (100 × 2 diez veces). ¿Qué advertencia hace falta?", "La predicción supone que el alimento y el espacio no se agotan", "No se puede predecir nada con una tabla", "La predicción es falsa porque 100 es un número pequeño", "Una predicción con un modelo debe declarar sus supuestos y su alcance."),
        ("abc", "{F} Una compañera dice que el promedio de 12, 15 y 18 prueba que todas las muestras del mundo tendrán 15 células por campo. ¿Qué falla?", "Tres campos de ejemplo no representan todas las muestras", "El promedio está mal calculado", "Los promedios no sirven en biología", "Un promedio de pocos datos describe esas muestras, no todas las posibles."),
        ("ab", "¿Qué aporta la física a la biología celular, según lo visto?", "La óptica de los microscopios y la difracción de rayos X", "Las proporciones entre las bases A, T, G y C", "La óptica y los rayos X son técnicas de la física que permiten ver estructuras que el ojo no alcanza."),
        ("abc", "{F} Se observa que a la hora 4 hay 1.500 células en vez de las 1.600 que predice la regla. ¿Qué conclusión es más razonable?", "El modelo predice bien pero hay una diferencia que se debe investigar, por ejemplo por menos alimento", "El modelo es totalmente falso", "Los datos no valen nada", "Una diferencia pequeña invita a revisar los supuestos antes de descartar el modelo."),
        ("{F} ¿Cuántas células más hay en la hora 3 que en la hora 1?", "600", "En la hora 3 hay 800 y en la hora 1 hay 200, y la diferencia es 600."),
    ],
    ctx=("abc", "Contexto: en una exposición debes explicar a tu curso cómo se usa la matemática en biología celular. ¿Qué ejemplo escoges?", "Calcular el tamaño real de una célula a partir de una imagen con aumentos conocidos", "Dibujar una célula con colores", "Memorizar los nombres de los organelos", "El cálculo de escala usa matemática para obtener un dato biológico real."),
    sc=[
        ("En Biología celular y molecular: ¿qué es el aumento de una imagen?", "Cuántas veces se agranda la imagen respecto del tamaño real", "El aumento compara el tamaño de la imagen con el real."),
        ("ab", "El promedio de varios recuentos sirve para:", "Resumir los datos en un solo valor", "Reemplazar todos los datos por uno solo sin pérdida", "Resume, pero pierde información sobre la variación entre campos."),
        ("ab", "Un modelo debe declarar:", "Sus supuestos y su alcance", "Que es perfecto", "Declarar supuestos y alcance permite saber cuándo sirve y cuándo no."),
    ],
    op=("Con los datos de la ficha {F}: (1) escribe una regla para el crecimiento del cultivo de ejemplo; (2) usa la regla para predecir las células en la hora 4; (3) escribe dos supuestos del modelo y una situación real en la que la predicción fallaría.",
        "(1) Cada hora el número de células se duplica. (2) 800 × 2 = 1.600 células. (3) Supuestos: hay alimento y espacio suficientes, y todas las células se dividen. Fallaría si el alimento se agota o hay un cambio de temperatura que frene la división.",
        ["regla coherente con la tabla", "predicción calculada correctamente", "dos supuestos distintos", "situación en que la predicción falla"],
        ["tres respuestas numeradas"],
        ["no usar la tabla", "calcular mal la predicción", "declarar supuestos que no afectan al modelo"],
        "Pregunta: «¿cuándo dejaría de servir tu regla?»."),
    reinforce="Calcula el promedio de los recuentos 8, 10 y 12 y explica qué información pierde ese promedio.",
    extend="Explica cómo la química, la física y la matemática contribuyen de forma distinta a un mismo modelo celular.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (tres fuentes de ejemplo, escritas para este cuaderno sobre un hallazgo ficticio). Fuente 1: página de un cuaderno de laboratorio, escrita el mismo día de la observación: «Hoy, con la lente nueva, vi estructuras redondas en la lámina; dibujé tres y anoté su tamaño aproximado». "
     "Fuente 2: artículo de divulgación escrito cien años después: «El investigador X descubrió la célula él solo, de un día para otro». "
     "Fuente 3: revisión escrita por especialistas, que cita seis equipos que aportaron observaciones en distintos años y concluye que el hallazgo fue gradual.")
build(
    O1, 4, F,
    use="Aprenderé a evaluar fuentes sobre la historia de la biología celular: cuáles son primarias y secundarias, cuáles son más confiables y por qué la ciencia es un trabajo colectivo. Sirve para no repetir mitos como el del «descubridor solitario».",
    prior=["Sé distinguir un hecho de una opinión.", "Sé que una fuente tiene autor y fecha.", "Conozco la teoría celular."],
    explain=[
        "Una fuente primaria es un registro hecho por quien vivió o hizo la observación, como un cuaderno de laboratorio. Una fuente secundaria interpreta o resume fuentes anteriores, como un artículo de divulgación o una revisión. Ninguna es mejor por sí sola: la primaria da el dato original, y la secundaria ayuda a verlo en conjunto, pero puede simplificar o deformar.",
        "Para evaluar una fuente se preguntan cuatro cosas: quién la escribió y cuándo, con qué datos se apoya, si cita otras fuentes y si exagera. Frases como «descubrió él solo» o «de un día para otro» son señales de alerta, porque la historia de la ciencia suele ser gradual y colectiva. Las revisiones que citan varios equipos y señalan sus limitaciones merecen más confianza.",
        "Contrastar fuentes significa compararlas: si una primaria muestra una observación y una secundaria afirma algo mucho mayor, hay que desconfiar de la secundaria. Además, no todos los aportes recibieron el mismo reconocimiento: a veces el trabajo de ciertos equipos, entre ellos el de mujeres científicas, quedó menos visible. Por eso conviene buscar quién hizo cada parte.",
    ],
    vocab=[("fuente primaria", "registro hecho por quien realizó la observación"), ("fuente secundaria", "texto que interpreta o resume otras fuentes"), ("sesgo", "inclinación que deforma la información"), ("contrastar", "comparar fuentes para ver si coinciden"), ("revisión", "texto que reúne y evalúa muchos estudios")],
    worked=[
        ("Clasificar fuentes", "En la ficha, ¿la Fuente 1 es primaria o secundaria?",
         ["Se pregunta si fue escrita por quien observó y el mismo día.", "El texto dice «hoy vi» y «dibujé tres»: es el propio registro."],
         "Es primaria"),
        ("Detectar una exageración", "La Fuente 2 dice «descubrió la célula él solo, de un día para otro». ¿Qué conviene hacer?",
         ["Se contrasta con la Fuente 3, que cita seis equipos y habla de un hallazgo gradual.", "La Fuente 1 solo muestra tres estructuras dibujadas, no toda la teoría."],
         "Desconfiar de la frase y apoyarse en la Fuente 3 y la Fuente 1"),
    ],
    mistakes=[("Creer que una fuente primaria siempre es más correcta que una secundaria.", "La primaria aporta el dato original, pero puede ser parcial; la secundaria puede reunir muchos datos.", "Usa ambas y contrástalas."),
              ("Aceptar un artículo porque suena seguro y usa frases fuertes como «sin duda».", "La seguridad del tono no es evidencia; hay que mirar los datos y las fuentes que cita.", "Pregunta qué datos sostienen la frase.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es una fuente primaria?", "Un registro hecho por quien realizó la observación", "Un resumen de lo que otros escribieron", "Una opinión sin autor", "La fuente primaria nace de quien observó, como un cuaderno de laboratorio."),
        ("{F} ¿Cuál de las fuentes (1, 2 o 3) es un cuaderno de laboratorio del mismo día de la observación?", "Fuente 1", "La Fuente 1 es un registro escrito el mismo día por quien observó."),
        ("{F} ¿Cuántos equipos cita la Fuente 3?", "6", "La Fuente 3 dice que cita seis equipos que aportaron en distintos años."),
        ("abc", "{F} ¿Por qué la Fuente 3 merece más confianza que la 2 para hablar del hallazgo completo?", "Cita varios equipos y reconoce que fue gradual", "Porque está escrita con palabras más difíciles", "Porque es más corta", "Una revisión que cita fuentes y reconoce el proceso gradual se apoya en más evidencia."),
        ("abc", "{F} ¿Qué frase de la Fuente 2 es una señal de alerta?", "«Descubrió la célula él solo, de un día para otro»", "«El investigador X»", "«Escrito cien años después»", "Lo absoluto de «él solo» y «de un día para otro» sugiere una simplificación."),
        ("ab", "{F} La Fuente 1 dice que se dibujaron tres estructuras redondas. ¿Qué permite concluir?", "Que se observaron estructuras redondas en esa lámina", "Que se descubrió toda la teoría celular", "Una fuente primaria prueba lo observado ese día, no una teoría completa."),
        ("abc", "{F} Si quieres saber qué se observó realmente un día concreto, ¿qué fuente conviene mirar primero?", "La Fuente 1, porque es el registro original", "La Fuente 2, porque es la más reciente", "La Fuente 3 reemplaza a las demás", "Para el dato original se acude primero a la fuente primaria."),
        ("abc", "{F} Una compañera dice: «la Fuente 1 no sirve porque solo habla de tres estructuras». ¿Cuál es la mejor respuesta?", "Sirve como dato original, aunque sola no basta para una conclusión general", "No sirve y debe descartarse", "Sirve y por eso la Fuente 2 es verdadera", "Una fuente primaria aporta datos concretos pero necesita otras fuentes para generalizar."),
        ("ab", "Una revisión de ejemplo señala que dos equipos no fueron mencionados en artículos antiguos aunque aportaron datos. ¿Qué conviene hacer al estudiar la historia?", "Buscar quién hizo cada aporte y no quedarse con una sola versión", "Ignorar a esos equipos porque no salían en los artículos", "La historia se reconstruye con varias fuentes, incluso las que muestran aportes menos visibles."),
        ("abc", "{F} Alguien dice que, como la Fuente 2 es de divulgación, no puede usarse jamás. ¿Qué corriges?", "Puede usarse, pero sus afirmaciones deben contrastarse con otras fuentes", "Tiene razón: ninguna divulgación sirve", "Debe preferirse siempre sobre las revisiones", "Una fuente de divulgación puede orientar, siempre que se verifique con fuentes más sólidas."),
        ("abc", "{F} ¿Cuál es el mejor plan para reconstruir cómo se descubrió el hallazgo?", "Contrastar la Fuente 1 con la 3 y tratar la 2 como una versión simplificada", "Usar solo la Fuente 2 por ser la más fácil de leer", "Usar solo la Fuente 1 sin ninguna otra", "La reconstrucción más sólida combina el dato original con una revisión y corrige simplificaciones."),
        ("{F} ¿Qué dato de la Fuente 3 contradice la idea del «descubridor solitario»?", "Que cita seis equipos en distintos años", "Seis equipos en distintos años muestran un trabajo colectivo y gradual."),
        ("abc", "Dos fuentes de ejemplo sobre el mismo hallazgo se contradicen en una fecha. ¿Qué haces primero?", "Buscar una tercera fuente confiable para contrastar", "Elegir la que te guste más", "Promediar las dos fechas", "Ante dos fuentes en conflicto se busca una tercera que ayude a decidir."),
    ],
    ctx=("abc", "Contexto: tu docente te pide escribir una breve cápsula para el diario mural sobre «quién descubrió la célula». ¿Cómo la planteas?", "Explico que fue un proceso gradual con varios aportes y cito dos fuentes distintas", "Escribo que lo hizo una sola persona porque es más fácil de leer", "Copio el primer artículo que encuentro", "La cápsula fiel a la evidencia muestra el proceso y se apoya en fuentes contrastadas."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una fuente secundaria?", "Un texto que interpreta o resume otras fuentes", "La fuente secundaria se apoya en registros anteriores y los explica."),
        ("ab", "Contrastar fuentes significa:", "Compararlas para ver si coinciden", "Elegir la más reciente sin comparar", "Contrastar es comparar para detectar acuerdos y diferencias."),
        ("ab", "Una frase como «descubrió él solo» suele ser:", "Una señal de posible simplificación", "Una prueba de que es verdad", "La ciencia suele ser colectiva, por eso la frase merece verificarse."),
    ],
    op=("Con las tres fuentes de la ficha {F}: (1) clasifica cada una como primaria o secundaria; (2) escribe qué te hace confiar más o menos en cada una; (3) redacta en dos oraciones tu versión de la historia del hallazgo, usando al menos dos fuentes.",
        "(1) Fuente 1 primaria; fuentes 2 y 3 secundarias. (2) Confío en la 1 como dato original; desconfío de la 2 por exagerar; confío en la 3 porque cita equipos y habla de un proceso gradual. (3) Según las fuentes 1 y 3, el hallazgo fue gradual: hubo una observación original de estructuras redondas y varios equipos aportaron después.",
        ["clasificación correcta de las tres fuentes", "criterio de confianza por fuente", "versión propia que no copia una sola fuente", "usa al menos dos fuentes"],
        ["tres respuestas numeradas"],
        ["clasificar mal las fuentes", "dar confianza por el tono y no por los datos", "copiar la frase de la Fuente 2"],
        "Pregunta: «¿qué otra fuente buscarías para comprobar tu versión?»."),
    reinforce="Escribe una lista con dos preguntas que harías a cualquier fuente histórica antes de confiar en ella.",
    extend="Explica por qué contar la historia como obra de una sola persona puede ocultar aportes y qué efecto tiene eso en cómo se ve la ciencia.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (dos explicaciones y datos de ejemplo, inspirados en un experimento histórico). Explicación 1: los microorganismos aparecen en un caldo nutritivo porque se forman solos a partir de materia sin vida. "
     "Explicación 2: los microorganismos del caldo provienen de otros microorganismos que llegan desde el aire. "
     "Datos de ejemplo: Recipiente 1, caldo hervido y con la boca abierta: el caldo se pone turbio en 2 días. Recipiente 2, caldo hervido, con un cuello largo y curvo que atrapa las partículas del aire: sigue transparente durante 30 días. "
     "Recipiente 3, igual al 2, pero se inclina hasta que el caldo toca la parte curva del cuello: el caldo se pone turbio en 2 días.")
build(
    O1, 5, F,
    use="Aprenderé a comparar explicaciones rivales con la evidencia y a ver cómo la discusión llevó a la idea de que toda célula proviene de otra célula. Sirve para reconocer que en ciencia una explicación se acepta o se descarta según los datos.",
    prior=["Conozco la teoría celular.", "Sé qué es una variable.", "Sé leer una tabla de resultados."],
    explain=[
        "Durante siglos hubo dos explicaciones sobre el origen de los seres diminutos. La generación espontánea decía que podían formarse solos desde materia sin vida. La otra decía que provenían de otros seres vivos que llegaban, por ejemplo, con el aire. Ninguna se resolvió por discusión: se resolvió con experimentos que ponían a prueba predicciones distintas de cada una.",
        "Una predicción es lo que debería ocurrir si una explicación es cierta. Si la generación espontánea fuera cierta, el caldo hervido se pondría turbio incluso sin contacto con el aire. Si los microorganismos vienen del aire, entonces impedir ese contacto evitaría la turbidez. Un buen experimento cambia una sola condición, mantiene las demás iguales y registra el resultado.",
        "Cuando los datos favorecen una explicación, la ciencia la acepta de manera provisoria. Los resultados del recipiente de cuello curvo apoyaron la idea de que los microorganismos provienen de otros, y eso encaja con la teoría celular: toda célula proviene de otra célula. Aun así, el conocimiento sigue abierto: la pregunta del origen de la primera célula es otro problema, que se investiga hoy.",
    ],
    vocab=[("generación espontánea", "idea antigua de que los seres vivos pueden formarse solos desde materia sin vida"), ("predicción", "lo que debería ocurrir si una explicación es cierta"), ("turbidez", "aspecto no transparente de un líquido por la presencia de partículas o microorganismos"), ("explicación rival", "explicación alternativa que compite con otra"), ("provisorio", "aceptado por ahora, mientras no aparezcan datos que lo contradigan")],
    worked=[
        ("Hacer una predicción", "Si los microorganismos vinieran del aire, ¿qué debería pasar en el Recipiente 2, que atrapa partículas del aire?",
         ["Se parte de la explicación 2: los microorganismos llegan con el aire.", "El Recipiente 2 impide que las partículas lleguen al caldo.", "Entonces el caldo debería quedar transparente."],
         "Debería quedar transparente"),
        ("Interpretar el Recipiente 3", "El Recipiente 3 se pone turbio al inclinar el cuello. ¿Qué indica?",
         ["Al inclinar, el caldo toca las partículas atrapadas en la curva.", "El caldo no era incapaz de enturbiarse: sí podía, si recibía partículas.", "Eso respalda que lo que enturbia viene de afuera."],
         "Respalda la explicación 2"),
    ],
    mistakes=[("Decir que los datos «demuestran para siempre» una explicación.", "Los datos la apoyan, pero la ciencia la mantiene mientras no aparezca evidencia contraria.", "Usa «apoyan» o «son consistentes con» y no «demuestran para siempre»."),
              ("Olvidar el control: concluir con el Recipiente 2 sin mirar el 1 y el 3.", "Sin comparar, no se sabe si el cuello curvo fue la causa del resultado.", "Compara todas las condiciones antes de concluir.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué decía la idea de generación espontánea?", "Que los seres vivos pueden formarse solos desde materia sin vida", "Que todo ser vivo viene de otro ser vivo", "Que las células no existen", "La generación espontánea afirmaba que los seres vivos aparecen desde materia sin vida."),
        ("{F} ¿Qué pasa con el caldo del Recipiente 1 en 2 días?", "Se pone turbio", "Los datos de la ficha indican que el Recipiente 1 se enturbia en 2 días."),
        ("{F} ¿Durante cuántos días el Recipiente 2 permanece transparente?", "30", "La ficha señala que el Recipiente 2 queda transparente durante 30 días."),
        ("abc", "{F} Si la generación espontánea fuera cierta, ¿qué debería pasar en el Recipiente 2?", "Debería ponerse turbio igual, porque no depende del aire", "Debería seguir transparente", "Debería secarse", "La generación espontánea predice turbidez aunque no entren partículas del aire."),
        ("ab", "{F} El Recipiente 2 permaneció transparente. ¿Qué explicación apoya?", "La explicación 2, que los microorganismos vienen del aire", "La explicación 1, la generación espontánea", "Al impedir la llegada de partículas del aire el caldo no se enturbió, lo que favorece la explicación 2."),
        ("ab", "{F} ¿Qué diferencia hay entre los recipientes 1 y 2 según la ficha?", "El tipo de cuello: abierto en el 1 y largo y curvo en el 2", "El tipo de caldo: distinto en cada uno", "La ficha dice que ambos tienen caldo hervido; cambia la forma del cuello."),
        ("abc", "{F} Si el Recipiente 3 se inclina y el caldo se enturbia, ¿qué se descarta?", "Que el caldo del Recipiente 2 fuera incapaz de enturbiarse por algún defecto", "Que existan partículas atrapadas en el cuello", "Que el Recipiente 1 se enturbie", "El Recipiente 3 muestra que el mismo caldo sí podía enturbiarse al recibir partículas."),
        ("abc", "{F} Otro grupo de ejemplo repite el Recipiente 2 en cinco recipientes iguales y los cinco permanecen transparentes. ¿Qué efecto tiene?", "Aumenta la confianza en el resultado", "Anula el resultado", "No tiene efecto sobre la confianza", "Repetir con resultados iguales vuelve más confiable la conclusión."),
        ("abc", "{F} Una estudiante dice: «los datos demuestran para siempre que nunca hubo generación espontánea». ¿Qué corriges?", "Los datos son muy fuertes en este caso, pero la ciencia mantiene sus conclusiones de forma provisoria", "Tiene razón y es lo único posible", "Los datos no dicen nada", "En ciencia se aceptan explicaciones apoyadas por evidencia mientras no aparezca evidencia contraria."),
        ("ab", "{F} Un compañero ignora el Recipiente 1 y usa solo el 2 para concluir. ¿Qué pierde?", "La comparación con una condición en la que el caldo sí se enturbia", "Nada, porque el Recipiente 2 basta", "Sin el 1 no se sabe si el caldo era capaz de enturbiarse en condiciones normales."),
        ("abc", "{F} ¿Cuál es la condición que cambia entre los recipientes 2 y 3?", "Se inclina el recipiente y el caldo toca la curva del cuello", "El tipo de caldo", "El tiempo de observación", "El Recipiente 3 es igual al 2, pero se inclina para que el caldo toque las partículas."),
        ("abc", "¿Cómo se relaciona este resultado con la teoría celular?", "Es consistente con que toda célula proviene de otra célula", "Contradice la teoría celular", "No tiene relación alguna", "Que los microorganismos vengan de otros microorganismos coincide con que toda célula viene de otra."),
        ("ab", "¿Qué quedó sin responder con este experimento?", "Cómo apareció la primera célula en la historia de la vida", "Si el caldo hervido se enturbia", "Que el caldo se enturbie ya se observó; el origen de la primera célula requiere otras investigaciones."),
    ],
    ctx=("abc", "Contexto: en una charla del liceo alguien dice que «los gusanos aparecen solos en la basura». Con lo aprendido, ¿cómo respondes con respeto y con evidencia?", "Explico que se pone a prueba con una predicción y con condiciones controladas, como en el experimento de los recipientes", "Digo que es verdad porque lo dice mucha gente", "Digo que es falso sin dar ninguna razón", "Una respuesta con evidencia propone una prueba controlada, no se basa en la opinión de la mayoría."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una predicción?", "Lo que debería ocurrir si una explicación es cierta", "Predecir es deducir un resultado que se podrá comprobar."),
        ("ab", "Repetir un experimento con los mismos resultados:", "Aumenta la confianza en la conclusión", "La disminuye", "Resultados repetidos por distintos intentos hacen más confiable la conclusión."),
        ("ab", "Una conclusión científica bien apoyada es:", "Provisoria, hasta que aparezcan datos contrarios", "Imposible de revisar nunca", "La ciencia revisa sus conclusiones cuando aparece nueva evidencia."),
    ],
    op=("Con la ficha {F}: (1) escribe una predicción de cada explicación para el Recipiente 2; (2) indica qué datos apoyan una de ellas; (3) escribe qué evidencia nueva podría hacerte cambiar de conclusión.",
        "(1) Explicación 1: el caldo se pondría turbio igual; explicación 2: quedaría transparente. (2) El Recipiente 2 quedó transparente 30 días y el 3 se enturbió al inclinar, lo que apoya la explicación 2. (3) Si un recipiente sin ninguna entrada de partículas se enturbiara repetidamente, revisaría mi conclusión.",
        ["una predicción por cada explicación", "dato concreto citado", "conclusión provisoria", "evidencia que haría cambiar de opinión"],
        ["tres respuestas numeradas"],
        ["dar la misma predicción para las dos explicaciones", "no citar datos", "presentar la conclusión como definitiva"],
        "Pregunta: «¿qué resultado habría apoyado a la otra explicación?»."),
    reinforce="Escribe en una tabla las dos explicaciones, la predicción de cada una para el Recipiente 2 y cuál fue el resultado.",
    extend="Explica por qué un experimento con un control (el Recipiente 1) es más convincente que uno que solo muestra el resultado esperado.",
)

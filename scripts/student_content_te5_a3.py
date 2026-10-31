"""Cuaderno del estudiante, 5.º básico Tecnología: OA 04 (probar y evaluar la calidad de trabajos), clases 1 a 5, y OA 05 (presentaciones y hojas de cálculo), clases 1 a 5.

Las pruebas usan objetos seguros (fichas, papel, cartón, tapas); nada de fuego, vidrio ni herramientas con filo.
Las pantallas se describen con texto y son ejemplos ficticios; no se nombra ninguna marca. Todas las clases de software tienen alternativa en papel.
Simplificación declarada: el manejo de un programa real de presentación o de hoja de cálculo NO se verifica aquí (cada programa se ve distinto);
solo se enseñan los conceptos (celdas con nombre, sumas simples, elección del tipo de gráfico) y la lectura de resultados. No se enseñan fórmulas
distintas de la suma ni formato condicional. Los datos de las tablas son ficticios y sin datos personales.
"""
from __future__ import annotations

from student_content_te5_a import reg
from student_lessons import arith

OA4 = "TE05 OA 04"
OA5 = "TE05 OA 05"

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja y lápiz. Los resultados de las pruebas están escritos en este cuaderno.",
    use="Aprenderé a evaluar si un trabajo funciona usando criterios de funcionamiento y una prueba justa. Sirve para juzgar un trabajo propio o ajeno con datos y no con simpatía.",
    prior=["Sé escribir criterios con números.", "Sé hacer tres pruebas y anotarlas.", "Sé que una prueba debe repetirse en las mismas condiciones."],
    explain=[
        "Evaluar la calidad es revisar qué tan bien cumple un trabajo lo que se pidió. Se puede evaluar un trabajo propio, de otra persona o de un equipo. Para hacerlo se usan criterios, que son condiciones comprobables. En esta clase estudiamos los criterios de funcionamiento, que preguntan si el objeto logra hacer lo que debía.",
        "Un criterio de funcionamiento se expresa con una acción y un número. «La tapa se abre y se cierra 20 veces sin romperse» o «el colgador aguanta 400 gramos durante 1 minuto». Una prueba justa se hace con las mismas condiciones para todos los trabajos: mismo peso, mismo tiempo, misma persona midiendo y los datos anotados.",
        "El resultado se registra en una tabla y se compara con el criterio. Si el criterio dice 20 veces y el trabajo resistió 20, cumple. Si resistió 14, no cumple, y la tabla muestra cuánto falta. No se mezcla gusto con funcionamiento: un trabajo bonito puede no funcionar. El objetivo de la prueba no es castigar, es descubrir cómo mejorar.",
    ],
    vocab=[("calidad", "qué tan bien cumple un trabajo lo que se pidió"), ("criterio de funcionamiento", "condición sobre lo que el objeto debe lograr hacer"), ("prueba justa", "prueba hecha con las mismas condiciones para todos"), ("registro", "tabla donde se anotan los datos"), ("cumple", "alcanza o supera lo que pide el criterio")],
    worked=[
        ("Comparar con el criterio", "Criterio: la tapa se abre y se cierra 20 veces sin romperse. La caja de Ema resistió 20 veces y la de Teo resistió 14. ¿Quién cumple?", ["Ema llegó a 20, que es lo pedido.", "Teo llegó a 14 y le faltan 6."], "Cumple Ema; Teo no cumple"),
        ("Revisar si la prueba es justa", "Un colgador se probó con 400 g, otro con 300 g. ¿Es una prueba justa?", ["Se usaron pesos distintos.", "Para comparar, el peso debe ser igual en los dos."], "No es justa porque los pesos son distintos"),
    ],
    mistakes=[
        ("Decir «funciona» porque se ve bien.", "La apariencia no prueba el funcionamiento.", "Haz la prueba con el número del criterio."),
        ("Probar un trabajo con 400 g y otro con 300 g.", "No se pueden comparar.", "Usa el mismo peso, tiempo y persona midiendo."),
    ],
    R=[
        ("Criterio: «aguanta 400 gramos». Un colgador aguanta 400 gramos. ¿Cumple?", "Sí", "Alcanza lo que pide el criterio."),
        ("Una prueba justa, ¿usa las mismas condiciones o condiciones distintas para todos?", "Las mismas condiciones", "Así se pueden comparar."),
        ("¿Dónde se anotan los datos de la prueba?", "En un registro o tabla", "La tabla ordena los datos."),
    ],
    C=[
        ("¿Por qué no se mezcla el gusto con el funcionamiento?", "Porque un trabajo bonito puede no funcionar", "El funcionamiento se comprueba con datos."),
        ("Criterio: 20 aperturas. Un trabajo logra 14. ¿Cuánto le falta?", "6 aperturas", "20 menos 14 es 6."),
        ("¿Cuál es un criterio de funcionamiento? A «Es hermoso», B «Se abre y cierra 20 veces».", "B", "Solo B habla de lo que el objeto logra hacer."),
    ],
    A=[
        arith("Un colgador debe aguantar 400 g y aguantó 350 g. ¿Cuántos gramos le faltan?", "400-350", "Se resta lo que aguantó de lo pedido."),
        arith("El criterio pide 20 aperturas. Una tapa resistió 12 aperturas en la primera prueba, 15 en la segunda y 18 en la tercera. ¿Cuántas aperturas le faltaron en la tercera para llegar a 20?", "20-18", "Se resta lo que resistió de lo que pide el criterio."),
        ("Dos cajas se prueban: una con 10 fichas y otra con 12 fichas. ¿Qué debe cambiar para que la prueba sea justa?", "Usar el mismo número de fichas", "Las condiciones deben ser iguales."),
    ],
    Z=[
        ("Dos estudiantes dicen que su caja es mejor. Uno muestra una tabla con 3 pruebas y el otro dice «a mí me gusta más». ¿Cuál evaluación es más confiable y por qué?", "La de la tabla, porque tiene datos", "Los datos de las pruebas se pueden comprobar."),
        ("Un trabajo cumple el criterio de funcionamiento pero se rompe al guardarlo. ¿Qué indica el resultado?", "Que falta revisar la resistencia", "Aunque cumpla una prueba, debe resistir su uso."),
    ],
    D=[
        arith("Un grupo midió 18, 20 y 22 aperturas en tres pruebas. ¿Cuántas aperturas más tuvo la tercera que la primera?", "22-18", "Se resta la primera de la tercera."),
        ("Criterio: «aguanta 400 g en las tres pruebas». Resultados: 400 g, 400 g y 300 g. ¿Cumple?", "No", "En la tercera prueba aguantó menos que lo pedido."),
    ],
    ctx=("Pruebas una caja de cartón con tapa. Criterio: se abre y cierra 20 veces sin romperse. Resultados de tres pruebas: 20, 20 y 17. Escribe si cumple, cuánto faltó en la prueba que falló y una idea de mejora para la tapa.", "No cumple porque en la tercera prueba logró 17. Le faltaron 3 aperturas. Idea: reforzar la bisagra de cartón con cinta", "Decide con datos y propone una mejora."),
    sc=[
        ("¿Con qué se compara el resultado de la prueba?", "Con el criterio", "Así se sabe si cumple."),
        ("¿Cómo debe ser una prueba entre dos trabajos?", "Con las mismas condiciones", "Así es justa."),
        ("¿Para qué sirve evaluar?", "Para descubrir cómo mejorar", "No es para castigar."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: un colgador de cordel y cartón con criterio «aguanta 400 g durante 1 minuto» y resultados 400 g, 400 g y 300 g. Trabajo 2: una caja de cartón con criterio «se abre y cierra 20 veces» y resultados 20, 19 y 20. Haz la tabla, di si cumple, cuánto falta y una idea de mejora.",
        "Trabajo 2: prueba 1: 20 cumple; prueba 2: 19 falta 1; prueba 3: 20 cumple. No cumple en total. Idea: reforzar la bisagra.",
        ["tabla con los resultados", "compara con el criterio", "dice cuánto falta", "propone una idea de mejora"],
        ["tabla con decisión y mejora"],
        ["decidir sin comparar con el criterio", "mezclar gusto con funcionamiento"],
        "Pregunta: «¿qué número del criterio comparaste con qué número de la prueba?». Si no los compara, pídele hacerlo.",
    ),
    reinforce="Escribe un criterio de funcionamiento con número para un objeto de tu casa.",
    extend="Explica con un ejemplo por qué una prueba debe ser justa para comparar dos trabajos.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja, lápiz y regla. Las medidas están escritas en este cuaderno.",
    use="Aprenderé a evaluar criterios técnicos: medidas, uniones y terminaciones. Sirve para saber si un trabajo está bien hecho aunque funcione.",
    prior=["Sé medir con regla y comprobar tolerancia.", "Sé que hay uniones permanentes y temporales.", "Sé evaluar con criterios de funcionamiento."],
    explain=[
        "Los criterios técnicos revisan cómo está hecho el trabajo. Preguntan si las medidas son correctas, si las uniones están firmes y si los cortes y la terminación están bien hechos. Un trabajo puede funcionar y aun así estar mal hecho, por ejemplo, con las piezas desparejas, y eso se nota con el uso o con el tiempo.",
        "Un criterio técnico de medida se acompaña de una tolerancia, que es la diferencia aceptada. «La pieza mide 20 cm, con tolerancia de 1 cm» significa que sirven las piezas de 19, 20 y 21 cm. Una pieza de 22 cm queda fuera. Se mide con regla en tres puntos para comprobar que no sea mayor en un extremo.",
        "Las uniones se revisan con una prueba suave: se tira o empuja con cuidado y se mira si algo se despega. Los cortes se revisan mirando que la línea sea recta y sin bordes desiguales. La terminación se revisa mirando que no haya pegamento a la vista ni bordes rotos. Cada punto se anota con una marca en una lista de cotejo.",
    ],
    vocab=[("criterio técnico", "condición sobre cómo está hecho el trabajo"), ("tolerancia", "diferencia aceptada respecto de la medida"), ("lista de cotejo", "lista de criterios con una marca de cumple o no cumple"), ("terminación", "aspecto final de bordes y uniones"), ("firmeza", "qué tan bien sujeta una unión")],
    worked=[
        ("Revisar una medida con tolerancia", "Una pieza debe medir 20 cm, con tolerancia de 1 cm. Se midieron tres piezas: 19, 22 y 20 cm. ¿Cuáles sirven?", ["Valen las medidas de 19 a 21 cm.", "19 y 20 están dentro; 22 está fuera."], "Sirven las de 19 y 20 cm"),
        ("Completar la lista de cotejo", "Una caja tiene medidas correctas, una unión que se despega con un tirón suave y cortes rectos. ¿Qué criterios cumple?", ["Medidas: cumple.", "Unión: no cumple.", "Cortes: cumple."], "Cumple medidas y cortes; no cumple uniones"),
    ],
    mistakes=[
        ("Medir la pieza en un solo punto.", "Puede ser desigual en otros puntos.", "Mide en tres puntos."),
        ("Probar una unión con un tirón fuerte.", "Puedes dañar el trabajo.", "Haz una prueba suave y con el mismo esfuerzo para todos."),
    ],
    R=[
        ("Una pieza debe medir 20 cm con tolerancia de 1 cm. ¿Sirve una de 21 cm?", "Sí", "21 está dentro del rango de 19 a 21."),
        ("¿Una lista de cotejo marca cumple o no cumple?", "Cumple o no cumple", "Esa es su función."),
        ("¿Qué se mira en la terminación: los bordes o el color de la pared?", "Los bordes", "Es parte del aspecto final."),
    ],
    C=[
        ("¿Por qué se mide una pieza en tres puntos?", "Para saber si es pareja", "Un extremo podría ser más ancho."),
        ("Un trabajo funciona pero sus cortes están torcidos. ¿Cumple el criterio técnico de cortes?", "No", "Los cortes deben ser rectos."),
        ("¿Cuál es un criterio técnico? A «La unión no se despega con un tirón suave», B «Me gusta el color».", "A", "A se puede comprobar y habla de cómo está hecho."),
    ],
    A=[
        arith("Una pieza debe medir 25 cm con tolerancia de 2 cm. ¿Cuál es la medida mayor que se acepta?", "25+2", "Se suma la tolerancia a la medida."),
        arith("Una pieza debe medir 25 cm con tolerancia de 2 cm. ¿Cuál es la medida menor que se acepta?", "25-2", "Se resta la tolerancia de la medida."),
        ("Medidas de tres piezas: 24, 26 y 29. Deben medir 25 con tolerancia de 2 cm. ¿Cuántas sirven?", "2", "Sirven 24 y 26; 29 queda fuera."),
    ],
    Z=[
        ("Dos cajas: una tiene medidas exactas pero la tapa se despega, y la otra tiene la tapa firme y una medida fuera de tolerancia. ¿Cuál cumple más criterios técnicos, o empatan?", "Empatan: cada una cumple uno y falla uno", "Cada una falla un criterio."),
        ("Un compañero dice: «Funciona, así que no importa si los cortes están torcidos». ¿Qué respondes?", "Que la calidad técnica también se evalúa", "Los criterios técnicos revisan cómo está hecho el trabajo."),
    ],
    D=[
        arith("Una lista de cotejo tiene 8 criterios y un trabajo cumple 6. ¿Cuántos no cumple?", "8-6", "Se resta lo que cumple del total."),
        ("Piezas medidas: 24, 25, 25 y 26 cm. Deben medir 25 con tolerancia de 1 cm. ¿Cuántas están dentro?", "4", "Todas están entre 24 y 26."),
    ],
    ctx=("Evalúas una caja de cartón con una lista de cotejo. Medida: 20 cm con tolerancia 1 cm (la caja mide 22 cm). Uniones: no se despegan. Cortes: rectos. Escribe qué criterios cumple, cuál no y qué mejorarías.", "Cumple uniones y cortes. No cumple la medida porque 22 cm pasa de 21. Mejoraría cortando de nuevo esa pieza", "Aplica la tolerancia y completa la lista."),
    sc=[
        ("¿Qué es la tolerancia?", "La diferencia aceptada respecto de la medida", "Dice cuánto se puede alejar la pieza."),
        ("¿Cómo se prueba una unión?", "Con una prueba suave", "Así no se daña el trabajo."),
        ("¿Qué se anota en la lista de cotejo?", "Cumple o no cumple por criterio", "Ordena la evaluación."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: una caja con pared de 15 cm (tolerancia 1 cm), medida 17 cm, unión firme y corte recto. Trabajo 2: un estante con tablero de 30 cm (tolerancia 2 cm), medida 29 cm, unión que se despega y corte recto. Completa la lista de cotejo con tres criterios y escribe qué mejorarías.",
        "Trabajo 2: medida: cumple (29 dentro de 28 a 32). Unión: no cumple. Corte: cumple. Mejoraría la unión con pestañas.",
        ["aplica la tolerancia", "marca cumple o no cumple por criterio", "no mezcla gusto", "propone una mejora"],
        ["lista de cotejo completada con mejora"],
        ["no aplicar la tolerancia", "marcar sin comprobar"],
        "Pregunta: «¿entre qué medidas se acepta?». Si no responde, pídele calcular el rango.",
    ),
    reinforce="Mide tres lápices y di si miden lo mismo con una tolerancia de 1 cm.",
    extend="Escribe tres criterios técnicos para evaluar una caja de cartón.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a evaluar criterios medioambientales y de seguridad. Sirve para cuidar el planeta y a las personas que usarán el trabajo.",
    prior=["Sé reducir, reutilizar y reciclar.", "Sé aplicar medidas de seguridad al trabajar.", "Sé hacer una lista de cotejo."],
    explain=[
        "Los criterios medioambientales revisan qué efecto tiene el trabajo en la naturaleza. Se puede contar cuántas piezas son reutilizadas, cuántos gramos de desperdicio quedaron y si los residuos se pueden reciclar. Un buen trabajo usa materiales reutilizados, genera poco desperdicio y dura mucho. Todo esto se puede medir o contar.",
        "Los criterios de seguridad revisan si el trabajo puede dañar a quien lo usa. Se revisa que no tenga bordes que corten, puntas que pinchen, piezas pequeñas que se puedan tragar si lo usan niños pequeños, ni material tóxico. También se revisa que el objeto sea estable y no se caiga sobre alguien. Se prueba con cuidado, nunca con riesgo.",
        "La seguridad es prioritaria: un trabajo que no es seguro no cumple, aunque funcione y sea bonito. Si un criterio de seguridad falla, se corrige primero. Los criterios medioambientales se pueden mejorar de a poco: reutilizar una pieza más, reducir el desperdicio o usar un material reciclado. Se anota el dato antes y después.",
    ],
    vocab=[("criterio medioambiental", "condición sobre el efecto en la naturaleza"), ("desperdicio", "material que sobra y se bota"), ("pieza pequeña", "pieza que un niño pequeño podría tragar"), ("estable", "que no se cae ni se vuelca con facilidad"), ("residuo", "lo que queda después de usar algo")],
    worked=[
        ("Contar piezas reutilizadas", "Un trabajo tiene 8 piezas y 6 son reutilizadas. ¿Cuántas piezas no lo son?", ["Total: 8. Reutilizadas: 6.", "Se resta 8 − 6."], "2 piezas"),
        ("Priorizar la seguridad", "Un trabajo usa mucho material reutilizado, pero tiene un borde de lata que corta. ¿Qué se corrige primero?", ["El borde que corta pone en riesgo a quien lo use.", "La seguridad va antes que lo ambiental."], "El borde que corta, es decir, la seguridad"),
    ],
    mistakes=[
        ("Aceptar un trabajo con un borde que corta porque usa material reciclado.", "La seguridad es prioritaria.", "Corrige primero lo que puede dañar a las personas."),
        ("Decir «es ecológico» sin dato.", "No se puede comprobar.", "Cuenta piezas reutilizadas o gramos de desperdicio."),
    ],
    R=[
        ("Un trabajo con un borde que corta, ¿es seguro?", "No", "Puede dañar a quien lo use."),
        ("Usar una caja que ya existía en vez de comprar una nueva, ¿es reutilizar o reciclar?", "Reutilizar", "Se usa otra vez sin transformarla."),
        ("¿Qué criterio va primero cuando falla: la seguridad o el color?", "La seguridad", "La seguridad es prioritaria."),
    ],
    C=[
        ("¿Por qué un criterio medioambiental conviene medirlo con un número?", "Para poder comprobar el efecto", "Con un número se compara antes y después."),
        ("¿Por qué una pieza muy pequeña puede ser un riesgo en un juguete?", "Porque un niño pequeño podría tragarla", "Es un riesgo de atragantamiento."),
        ("Un objeto que se vuelca fácil sobre una mesa, ¿cumple estabilidad?", "No", "Se cae con facilidad."),
    ],
    A=[
        arith("Un trabajo tiene 10 piezas y 7 son reutilizadas. ¿Cuántas no lo son?", "10-7", "Se resta lo reutilizado del total."),
        arith("Antes de la mejora quedaron 120 g de desperdicio; después, 85 g. ¿Cuántos gramos menos de desperdicio hay?", "120-85", "Se resta el desperdicio de después del de antes."),
        ("Un trabajo está terminado y tiene una punta de cartón que pincha. ¿Qué haces?", "La redondeo o la tapo con cinta", "La punta es un riesgo."),
    ],
    Z=[
        ("Dos trabajos: A usa 9 de 10 piezas reutilizadas pero se vuelca; B usa 5 de 10 y es estable. ¿Cuál tiene un problema de seguridad?", "A", "Se vuelca y puede caer sobre alguien."),
        ("Un grupo dice: «Nuestro trabajo es ecológico» sin dar datos. ¿Qué datos pedirías?", "Cuántas piezas son reutilizadas y cuánto desperdicio quedó", "Son datos medibles."),
    ],
    D=[
        arith("Cada una de 6 cajas usa 3 piezas reutilizadas. ¿Cuántas piezas reutilizadas hay en total?", "6*3", "Se multiplican las cajas por las piezas de cada una."),
        ("Se reduce el desperdicio de 90 g a 60 g. ¿Es una mejora medioambiental?", "Sí", "Hay menos desperdicio que antes."),
    ],
    ctx=("Evalúas un portalápices de cartón con 8 piezas, 6 reutilizadas, 40 g de desperdicio y una punta que pincha. Escribe un criterio medioambiental con dato, un criterio de seguridad y qué corriges primero.", "Ambiental: 6 de 8 piezas son reutilizadas. Seguridad: no tiene puntas que pinchen. Corrijo primero la punta", "Dato ambiental, criterio de seguridad y prioridad."),
    sc=[
        ("¿Qué va primero cuando falla: seguridad o decoración?", "Seguridad", "La seguridad es prioritaria."),
        ("¿Cómo se mide un criterio ambiental?", "Contando piezas reutilizadas o gramos de desperdicio", "Son datos numéricos."),
        ("¿Un objeto estable se vuelca fácil?", "No", "Estable significa que no se vuelca fácil."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: una caja con 9 piezas, 7 reutilizadas, 30 g de desperdicio y un borde de cartón doblado sin filo. Trabajo 2: un colgador con 6 piezas, 2 reutilizadas, 80 g de desperdicio y una punta que pincha. Escribe un criterio ambiental con dato, un criterio de seguridad, qué cumple y qué corriges primero.",
        "Trabajo 2: ambiental: 2 de 6 reutilizadas, mejora. Seguridad: no hay puntas que pinchen; falla. Corrijo la punta primero.",
        ["criterio ambiental con dato", "criterio de seguridad", "dice qué cumple", "corrige primero la seguridad"],
        ["tabla con criterios, resultados y prioridad"],
        ["dar prioridad a lo ambiental sobre lo seguro", "no dar datos"],
        "Pregunta: «¿qué podría dañar a quien lo use?». Si no lo revisó, pídele mirar bordes y puntas.",
    ),
    reinforce="Revisa un objeto de tu casa y di si tiene bordes o puntas que podrían herir.",
    extend="Escribe cómo bajarías el desperdicio de un trabajo en 20 gramos.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja, lápiz y lápices de colores. Los casos están escritos en este cuaderno.",
    use="Aprenderé a evaluar criterios estéticos con rasgos que se pueden observar. Sirve para opinar sobre la apariencia de un trabajo sin depender del gusto.",
    prior=["Sé que un criterio se puede comprobar.", "Sé evaluar funcionamiento y seguridad.", "Sé usar listas de cotejo."],
    explain=[
        "Los criterios estéticos revisan la apariencia del trabajo. Aunque cada persona tiene gustos distintos, se pueden definir rasgos que se observan: que los bordes sean parejos, que las partes iguales tengan el mismo tamaño, que no haya manchas ni pegamento a la vista, que los colores se combinen con un propósito y que el diseño esté ordenado.",
        "Un criterio estético comprobable se puede responder mirando. «Las dos paredes iguales miden lo mismo» se comprueba con una regla. «No hay manchas de pegamento a la vista» se comprueba mirando. «Me gusta» no es un criterio estético, porque no explica nada. Un criterio dice qué se debe ver en el trabajo.",
        "La apariencia es importante, pero no tiene prioridad sobre la seguridad ni sobre el funcionamiento. Primero se revisa que sea seguro y funcione, y después que se vea cuidado. Al evaluar, se habla del trabajo y no de la persona: «el borde derecho quedó desparejo» y no «eres descuidado». Así la crítica ayuda a mejorar.",
    ],
    vocab=[("estética", "apariencia de un trabajo"), ("simetría", "partes iguales a ambos lados de una línea"), ("borde parejo", "borde sin ondas ni salientes"), ("combinación de colores", "colores que se usan juntos con un propósito"), ("orden", "partes bien ubicadas y limpias")],
    worked=[
        ("Convertir una opinión en criterio", "Un compañero escribe «el estuche es feo». Reescríbelo como criterio observable.", ["«Feo» no dice qué mirar.", "Miro rasgos: bordes, manchas, tamaño de las partes."], "Los bordes son parejos y no hay manchas de pegamento"),
        ("Evaluar simetría", "Un cartel tiene dos alas iguales. La izquierda mide 15 cm y la derecha 13 cm. ¿Cumple el criterio «las dos alas miden lo mismo»?", ["Comparo 15 y 13.", "No son iguales."], "No cumple; le faltan 2 cm a la derecha"),
    ],
    mistakes=[
        ("Evaluar con «me gusta» o «no me gusta».", "No dice qué mejorar.", "Describe un rasgo que se ve: bordes, manchas, tamaño."),
        ("Decirle a una persona «eres descuidada» al evaluar su trabajo.", "Se critica a la persona y no al trabajo.", "Di «el borde derecho quedó desparejo»."),
    ],
    R=[
        ("«El borde es parejo» ¿es un criterio observable?", "Sí", "Se puede comprobar mirando."),
        ("¿Es «me gusta» un criterio estético?", "No", "No dice qué se debe ver."),
        ("Dos partes iguales a ambos lados de una línea, ¿es simetría?", "Sí", "Eso es la simetría."),
    ],
    C=[
        ("¿Por qué la estética no tiene prioridad sobre la seguridad?", "Porque un trabajo inseguro puede dañar a alguien", "La seguridad va primero."),
        ("«Los colores se combinan con un propósito» ¿qué rasgo evalúa?", "La combinación de colores", "Habla del uso de los colores."),
        ("¿Es mejor decir «el borde derecho quedó desparejo» o «eres descuidado»?", "El borde derecho quedó desparejo", "Habla del trabajo, no de la persona."),
    ],
    A=[
        arith("Una pared mide 18 cm y la pared igual mide 15 cm. ¿Cuántos centímetros de diferencia hay?", "18-15", "Se resta la menor de la mayor."),
        arith("Un cartel tiene 6 bordes y 5 están parejos. ¿Cuántos bordes no están parejos?", "6-5", "Se resta lo parejo del total."),
        ("Reescribe como criterio observable «el trabajo se ve lindo». Elige: A «Las partes iguales miden lo mismo y no hay manchas», B «Se ve lindo».", "A", "A dice qué se debe ver."),
    ],
    Z=[
        ("Dos estudiantes evalúan un cartel. Uno dice «está bien». Otra dice «los bordes están parejos y hay una mancha en la esquina». ¿Quién da información que ayuda a mejorar?", "La segunda", "Dice qué rasgo corregir."),
        ("Un trabajo es muy bonito pero se vuelca fácil. ¿Qué criterio debe corregirse primero?", "La estabilidad", "El funcionamiento y la seguridad van antes que la estética."),
    ],
    D=[
        arith("Una lista estética tiene 5 criterios y un trabajo cumple 3. ¿Cuántos no cumple?", "5-3", "Se restan los cumplidos del total."),
        ("Un grupo cambia el color de su trabajo cuando la seguridad aún falla. ¿Es buena decisión?", "No", "La seguridad va primero."),
    ],
    ctx=("Evalúas un estuche de cartón. Rasgos: un borde está ondulado, hay una mancha de pegamento visible, los colores combinan y las dos tapas miden lo mismo. Escribe cuántos criterios cumple de los cuatro y dos ideas de mejora.", "Cumple 2 de 4 (colores y tapas iguales). Mejoras: igualar el borde ondulado y limpiar la mancha de pegamento", "Cuenta lo cumplido y propone mejoras."),
    sc=[
        ("¿Un criterio estético se puede observar?", "Sí", "Se comprueba mirando."),
        ("¿De quién se habla al evaluar: del trabajo o de la persona?", "Del trabajo", "La crítica ayuda a mejorar."),
        ("¿Qué va antes: estética o seguridad?", "Seguridad", "La seguridad es prioritaria."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un cartel con borde ondulado, color claro y dos partes de 12 cm y 10 cm que deberían ser iguales. Caso 2: una caja con manchas de pegamento, bordes parejos y colores que combinan. Escribe cuatro criterios estéticos observables y marca cuáles cumple.",
        "Caso 2: bordes parejos: cumple. Sin manchas de pegamento: no cumple. Colores que combinan: cumple. Partes iguales: no se pueden evaluar.",
        ["cuatro criterios observables", "marca cumple o no cumple", "habla del trabajo y no de la persona", "no usa solo «me gusta»"],
        ["lista de cotejo estética"],
        ["opinar solo por gusto", "criticar a la persona"],
        "Pregunta: «¿qué se ve en el trabajo que te hace decir eso?». Si no tiene un rasgo, pídele describirlo.",
    ),
    reinforce="Mira un objeto de tu casa y describe tres rasgos que se ven en él.",
    extend="Escribe una crítica amable de un trabajo con un rasgo que se ve y una sugerencia.",
)

# ------------------------------------------------------------------ OA 04, clase 5
reg(
    OA4, 5,
    materials="Hoja y lápiz. Los casos y las rúbricas están escritos en este cuaderno.",
    use="Aprenderé a dialogar sobre los resultados de una evaluación y a proponer ideas de mejora, en forma individual o en equipo. Sirve para aprender de las pruebas y mejorar el trabajo.",
    prior=["Sé evaluar con criterios de funcionamiento, técnicos, ambientales, estéticos y de seguridad.", "Sé que se critica el trabajo y no a la persona.", "Sé sumar puntajes."],
    explain=[
        "Evaluar un trabajo termina en una conversación. Dialogar sobre los resultados es contar qué se observó, con datos, y escuchar a la otra persona. Una retroalimentación útil tiene tres partes: lo logrado con evidencia («sostuvo 400 g»), lo que falta según un criterio («la unión se despegó») y una idea de mejora («agregar una pestaña»).",
        "Se puede evaluar un trabajo individual o de un equipo. En equipo, cada persona tiene un rol: quien prueba, quien anota los datos, quien mide y quien explica. Todos opinan y se llega a una decisión con los datos. Cuando el equipo evalúa el trabajo de otro, usa la misma rúbrica para ser justo.",
        "Una rúbrica da un puntaje a cada criterio: por ejemplo 1 es insuficiente, 2 es en desarrollo, 3 es logrado y 4 es destacado. Se suman los puntos y se interpreta el total. Pero el total no reemplaza la conversación: dos trabajos con igual total pueden necesitar mejoras distintas. La conversación decide qué cambiar primero, empezando por la seguridad.",
    ],
    vocab=[("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("rúbrica", "tabla con criterios y puntajes"), ("rol", "tarea que tiene cada integrante del equipo"), ("evidencia", "datos que apoyan una opinión"), ("idea de mejora", "propuesta concreta de cambio")],
    worked=[
        ("Dar retroalimentación", "El colgador de Ana aguantó 400 g en dos pruebas y se despegó en la tercera. Escribe lo logrado, lo que falta y una idea.", ["Lo logrado: aguantó 400 g en dos pruebas.", "Lo que falta: se despegó en la tercera.", "Idea: agregar una pestaña al pegar."], "Aguantó 400 g dos veces; falta firmeza en la unión; agregar una pestaña"),
        ("Sumar una rúbrica", "Funcionamiento 3, técnico 2, seguridad 4, estético 3. ¿Cuánto suma?", ["Los puntajes son 3, 2, 4 y 3.", "Se suman los cuatro puntajes."], "12"),
    ],
    mistakes=[
        ("Decir solo «está bien» o «está mal».", "No ayuda a mejorar.", "Da un dato, un criterio y una idea."),
        ("Elegir la mejora mirando solo el puntaje total.", "Puntajes iguales pueden esconder fallas distintas.", "Conversa sobre qué criterio falló y empieza por la seguridad."),
    ],
    R=[
        ("¿Cuántas partes tiene una retroalimentación útil?", "Tres", "Lo logrado, lo que falta y una idea."),
        ("Un puntaje 4 en la rúbrica de esta clase, ¿significa destacado o insuficiente?", "Destacado", "En esa escala 4 es el mayor."),
        ("Quien prueba, quien anota los datos y quien explica en un equipo, ¿son roles o puntajes?", "Roles", "Cada integrante tiene una tarea."),
    ],
    C=[
        ("¿Por qué conviene usar la misma rúbrica al evaluar a distintos equipos?", "Para ser justos", "Todos se evalúan con los mismos criterios."),
        ("«Está bien» ¿es una retroalimentación útil?", "No", "No da datos ni ideas."),
        ("Dos trabajos suman 10 puntos. ¿Pueden necesitar mejoras distintas?", "Sí", "Los puntajes pueden venir de criterios distintos."),
    ],
    A=[
        arith("Una rúbrica tiene funcionamiento 3, técnico 4, seguridad 4 y estético 2. ¿Cuántos puntos suma?", "3+4+4+2", "Se suman los cuatro puntajes."),
        arith("El máximo de la rúbrica es 16 puntos. Un trabajo tiene 13. ¿Cuántos puntos le faltan?", "16-13", "Se resta lo obtenido del máximo."),
        ("Elige la mejor retroalimentación. A «Hiciste un buen trabajo», B «Tu caja resistió 20 aperturas; la tapa tiene una esquina rota; puedes reforzarla con cinta».", "B", "B tiene dato, criterio e idea."),
    ],
    Z=[
        ("Dos trabajos suman 12. En uno falla la seguridad y en el otro falla lo estético. ¿Cuál se corrige primero?", "El de seguridad", "La seguridad va primero."),
        ("En un equipo, una persona opina sin mirar los datos y el resto no la escucha. ¿Qué regla de la conversación falta?", "Escuchar y usar los datos", "Las decisiones se basan en datos y respeto."),
    ],
    D=[
        arith("En una rúbrica con máximo de 16 puntos, el trabajo A suma 12 y el trabajo B suma 9. ¿Cuántos puntos más tiene A que B?", "12-9", "Se resta el total de B del total de A."),
        ("Un grupo dice: «Nuestro puntaje es alto, no hay nada que mejorar». ¿Qué respondes?", "Siempre se puede mejorar el criterio con menor puntaje", "Aun con total alto, un criterio puede tener un puntaje bajo."),
    ],
    ctx=("Evaluaste la caja de otro equipo. Datos: resistió 20 aperturas (logrado), la unión de una esquina se despegó (falta) y está limpia y ordenada. Escribe una retroalimentación de tres partes y la idea más importante.", "Lo logrado: resistió 20 aperturas y está ordenada. Falta: se despegó una esquina. Idea: reforzar esa unión con una pestaña", "Tres partes y una idea concreta."),
    sc=[
        ("¿Cuáles son las tres partes de la retroalimentación?", "Lo logrado, lo que falta y una idea de mejora", "Así ayuda a mejorar."),
        ("¿Se critica el trabajo o la persona?", "El trabajo", "La crítica debe ayudar."),
        ("¿Qué se corrige primero?", "Lo que afecta la seguridad", "Es lo más importante."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: una caja con 20 aperturas logradas, una esquina despegada y una mancha de pegamento. Caso 2: un colgador que aguantó 400 g, tiene bordes parejos y una punta que pincha. Escribe la retroalimentación de tres partes con datos y define qué se mejora primero.",
        "Caso 2: logrado: aguantó 400 g y bordes parejos. Falta: una punta pincha. Idea: redondearla. Primero: la punta.",
        ["lo logrado con dato", "lo que falta con criterio", "una idea de mejora", "ordena la mejora desde la seguridad"],
        ["retroalimentación de tres partes con prioridad"],
        ["comentarios sin datos", "criticar a la persona"],
        "Pregunta: «¿qué dato muestra lo que dices?». Si no hay, pídele volver al resultado.",
    ),
    reinforce="Cuéntale a una persona de tu casa lo que lograste en un trabajo y qué mejorarías, con un dato.",
    extend="Escribe tres reglas para una conversación respetuosa sobre el trabajo de un equipo.",
)

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja y lápiz. Los casos y los datos están escritos en este cuaderno. Si tienes computador, un programa de presentaciones; si no, usa hojas de papel como diapositivas.",
    use="Aprenderé a planificar la comunicación de una investigación: para qué, para quién y qué mostrar en cada diapositiva. Sirve para que otras personas entiendan lo que descubriste.",
    prior=["Sé que una presentación tiene diapositivas.", "Sé buscar información y anotar la fuente.", "Sé ordenar ideas."],
    explain=[
        "Comunicar una investigación es mostrar a otras personas lo que descubriste. Antes de abrir un programa, planifica. Responde tres preguntas: ¿para qué comunico?, que es el propósito, por ejemplo informar o convencer; ¿para quién?, que es la audiencia; y ¿qué es lo más importante que debe quedar claro?, que es el mensaje central.",
        "Después se hace el guion, que es la lista de diapositivas con una idea cada una. Un guion típico tiene: portada con título y autoría, pregunta de investigación, tres ideas principales, conclusión y fuentes. Cada diapositiva expresa una sola idea; si tienes dos, haz dos diapositivas. Así la audiencia no se pierde y tú sabes qué decir.",
        "El software de presentación permite mostrar textos, imágenes y diagramas en diapositivas. Pero un programa no reemplaza el pensamiento: si no sabes tu mensaje, el programa no lo inventa. La alternativa en papel sirve igual: una hoja es una diapositiva. Se puede presentar con pocas palabras y explicar lo demás hablando.",
    ],
    vocab=[("propósito", "para qué se comunica"), ("audiencia", "personas que recibirán el mensaje"), ("mensaje central", "idea más importante que debe quedar clara"), ("guion", "lista de diapositivas con su idea"), ("diapositiva", "página de una presentación")],
    worked=[
        ("Planificar con tres preguntas", "Investigaste cuánta agua gasta tu curso en un día y la contarás al curso para que la cuide. Escribe propósito, audiencia y mensaje.", ["Propósito: convencer de cuidar el agua.", "Audiencia: el curso.", "Mensaje central: el curso gasta mucha agua y puede ahorrar."], "Convencer al curso de cuidar el agua"),
        ("Dividir una idea doble", "Una diapositiva dice «Qué es el agua potable y cómo se contamina». ¿Qué haces?", ["Hay dos ideas en una diapositiva.", "Las separo en dos."], "Hacer dos diapositivas, una por idea"),
    ],
    mistakes=[
        ("Abrir el programa y poner todo en una diapositiva.", "La audiencia se pierde.", "Haz primero un guion con una idea por diapositiva."),
        ("Pensar que el programa elige el mensaje.", "El mensaje lo decide quien investigó.", "Escribe tu mensaje central antes de armar."),
    ],
    R=[
        ("¿Qué es la audiencia de una presentación?", "Las personas que reciben el mensaje", "Son quienes miran y escuchan."),
        ("¿Cuántas ideas lleva una diapositiva?", "Una", "Así la audiencia no se pierde."),
        ("¿Qué es el guion de una presentación?", "La lista de diapositivas con una idea cada una", "Ordena lo que se mostrará."),
    ],
    C=[
        ("Quieres que tu curso cuide la electricidad. ¿Cuál es tu propósito: informar o convencer?", "Convencer", "Quieres que cambien una conducta."),
        ("¿Por qué conviene hacer el guion antes de abrir el programa?", "Para saber qué mostrar en cada diapositiva", "El guion ordena las ideas."),
        ("¿Qué diapositivas debería tener un guion típico además de las tres ideas principales?", "Portada, pregunta, conclusión y fuentes", "Son las partes del guion de la clase."),
    ],
    A=[
        ("Elige el mensaje central. A «Hay muchos datos», B «El curso gasta 120 litros por día y puede ahorrar 40».", "B", "B es una idea clara y comprobable."),
        arith("Un guion tiene portada, pregunta, 3 ideas, conclusión y fuentes. ¿Cuántas diapositivas son?", "1+1+3+1+1", "Se suman las diapositivas de cada parte."),
        ("La audiencia son niños de 1.º básico. ¿Conviene mucho texto o pocas palabras e imágenes?", "Pocas palabras e imágenes", "Los más pequeños se pierden con mucho texto."),
    ],
    Z=[
        ("Dos presentaciones: una pone toda la investigación en 1 diapositiva; la otra usa 7 con una idea cada una. ¿Cuál comunica mejor y por qué?", "La de 7, porque cada idea queda clara", "Una idea por diapositiva ayuda a la audiencia."),
        ("Quieres informar a los apoderados, no convencerlos. ¿Qué cambia en tu propósito?", "Solo presentas los datos sin pedir un cambio", "Informar es mostrar datos."),
    ],
    D=[
        arith("Cada diapositiva dura 2 minutos. Tienes 14 minutos para presentar. ¿Cuántas diapositivas caben?", "14//2", "Se divide el tiempo entre lo que dura cada una."),
        arith("Tu guion tiene 8 diapositivas y quitas 2. ¿Cuántas quedan?", "8-2", "Se restan las que quitas."),
    ],
    ctx=("Investigaste cuántos minutos usa tu curso las pantallas en el recreo. Datos: 3 de 10 estudiantes las usan más de 15 minutos. Escribe propósito, audiencia, mensaje central y el título de la portada.", "Propósito: informar. Audiencia: el curso. Mensaje: 3 de 10 estudiantes usan pantallas más de 15 minutos en el recreo. Portada: Pantallas en el recreo", "Tres preguntas respondidas y un título."),
    sc=[
        ("¿Qué tres preguntas se responden al planificar?", "Para qué, para quién y qué mensaje", "Son propósito, audiencia y mensaje."),
        ("¿Una hoja de papel puede ser una diapositiva?", "Sí", "Una hoja sirve igual."),
        ("¿Qué va en la última diapositiva además de la conclusión?", "Las fuentes", "Se reconoce de dónde viene la información."),
   ],
    open_task=(
        "Escoge un tema. Tema 1: cuántas botellas plásticas junta tu curso en una semana (datos: lunes 12, martes 9, miércoles 15, jueves 8, viernes 11). Tema 2: cuántos libros leyó el curso en un mes (datos: semana 1: 14, semana 2: 18, semana 3: 11, semana 4: 17). Escribe propósito, audiencia, mensaje central y el guion de al menos 6 diapositivas.",
        "Tema 1: propósito: informar; audiencia: el curso; mensaje: se juntan 55 botellas por semana. Guion: portada, pregunta, datos por día, día con más botellas, conclusión, fuentes.",
        ["responde propósito, audiencia y mensaje", "guion con una idea por diapositiva", "incluye portada, conclusión y fuentes", "el mensaje es comprobable"],
        ["planificación y guion"],
        ["más de una idea por diapositiva", "olvidar las fuentes"],
        "Pregunta: «¿qué idea tiene cada diapositiva?». Si tiene dos, pídele separarla.",
    ),
    reinforce="Elige un tema que conozcas y di en una frase tu mensaje central.",
    extend="Explica cómo cambia tu guion si tu audiencia son niños de 1.º básico o personas adultas.",
)

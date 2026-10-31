"""Cuaderno del estudiante, 7.º básico Tecnología: OA 03 (evaluación técnica de soluciones implementadas), clases 1 a 5.

Seguridad: las pruebas usan papel, cartón, monedas, libros livianos y cordel; nada de cargas que puedan caer sobre los pies ni objetos pesados.
Cifras enteras. Los casos y los datos son inventados para practicar y no nombran marcas ni personas reales.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te7_a import reg
from student_lessons import arith

OA3 = "TE07 OA 03"

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir los criterios propios, que dependen de lo que prefiere una persona, de los criterios técnicos, que se pueden medir. Sirve para evaluar una solución con argumentos y no solo con gustos.",
    prior=["Sé que un criterio es una condición comprobable.", "Sé medir en centímetros y gramos.", "Sé que una solución implementada es una solución ya construida."],
    explain=[
        "Evaluar una solución es juzgar qué tan bien responde a la necesidad. Para eso se usan dos tipos de criterios. Los criterios propios dependen de lo que valoran las personas que la usan, como la comodidad, el gusto o la facilidad de entenderla. Los criterios técnicos se pueden medir o contar, como el peso, la resistencia, la durabilidad, el costo, el tiempo de armado o la seguridad.",
        "Los dos tipos sirven, pero cumplen funciones distintas. Los criterios técnicos entregan evidencia que cualquiera puede repetir y comprobar. Los criterios propios muestran si la solución es adecuada para sus usuarios, pero cada persona los entiende un poco distinto. Un buen informe usa ambos y no los mezcla: separa «mide 28 cm» de «me gustó».",
        "Un criterio propio se puede transformar en uno técnico preguntando «¿cómo lo comprobaría?». «Es cómodo de sostener» puede convertirse en «se sostiene con una sola mano durante 1 minuto sin soltarse». Así se evalúa con datos, y no solo con opiniones. Evaluar es juzgar la solución, nunca a las personas que la hicieron.",
    ],
    vocab=[("criterio propio", "condición que depende de lo que valora una persona"), ("criterio técnico", "condición que se puede medir o contar"), ("solución implementada", "solución ya construida y en uso"), ("evidencia", "datos que apoyan una evaluación"), ("evaluar", "juzgar qué tan bien una solución responde a la necesidad")],
    worked=[
        ("Clasificar criterios", "Se evalúa un organizador de escritorio. ¿Cuáles son técnicos y cuáles propios? (1) Resiste 2 kilos. (2) Su color me gusta. (3) Se arma en 15 minutos. (4) Se siente agradable al tocarlo.", ["El 1 se mide con pesas y el 3 se mide con un reloj: son técnicos.", "El 2 y el 4 dependen de la preferencia de cada persona: son propios."], "Técnicos: 1 y 3. Propios: 2 y 4"),
        ("Convertir un criterio propio en técnico", "El criterio propio «es fácil de abrir» se quiere transformar en uno técnico para una caja. ¿Cómo queda?", ["Pregunto cómo lo comprobaría: se puede contar el tiempo o los intentos.", "Lo escribo con un número: «una persona lo abre con una mano en menos de 5 segundos»."], "«Una persona lo abre con una mano en menos de 5 segundos»"),
    ],
    mistakes=[
        ("Evaluar una solución diciendo solo «me gustó» o «no me gustó».", "Es una opinión que otras personas no pueden comprobar.", "Agrega un criterio técnico con un número que respalde tu opinión."),
        ("Pensar que los criterios propios no sirven.", "Sirven para saber si la solución es adecuada para sus usuarios.", "Usa criterios propios y técnicos, y no los mezcles."),
    ],
    R=[
        ("«Pesa 300 g», ¿es un criterio propio o técnico?", "Técnico", "El peso se mide con una balanza."),
        ("«Me parece lindo», ¿es un criterio propio o técnico?", "Propio", "Depende del gusto de cada persona."),
        ("«Resiste 20 aperturas sin romperse», ¿es técnico o propio?", "Técnico", "Se comprueba contando las aperturas."),
    ],
    C=[
        ("¿Cuál criterio se puede comprobar con números? A «se arma en menos de 10 minutos», B «se ve moderno».", "A", "A se mide con un reloj; B depende del gusto."),
        ("Una compañera dice: «Mi evaluación es técnica porque yo lo sé». ¿Tiene razón?", "No", "Un criterio técnico se debe poder medir y repetir, no depender de quien opina."),
        ("¿Por qué conviene usar criterios propios y técnicos? A porque los técnicos dan evidencia y los propios muestran si sirve a sus usuarios, B porque los propios son más exactos que los técnicos.", "A", "Cada tipo aporta algo distinto a la evaluación."),
    ],
    A=[
        ("Clasifica con T (técnico) o P (propio), en orden: (1) soporta 4 libros, (2) me da confianza, (3) cuesta $2.000, (4) me parece cómodo.", "1 T, 2 P, 3 T, 4 P", "Soportar libros y costar $2.000 se miden; la confianza y la comodidad dependen de la persona."),
        arith("Una caja debe pesar como máximo 500 g. La caja pesa 380 g. ¿Cuántos gramos le sobran al límite?", "500-380", "Se resta el peso de la caja del máximo.", " g"),
        ("Un criterio dice: «el asa se siente cómoda». ¿Cuál lo convierte en técnico? A «una persona lleva la caja 100 pasos sin soltarla», B «es linda y suave».", "A", "A se puede contar y repetir."),
    ],
    Z=[
        ("Dani dice: «Mi puente es el mejor porque es más lindo». Elena dice: «El mío es mejor porque sostiene 600 g y el tuyo 400 g». ¿Quién usa un criterio técnico?", "Elena", "Compara con un dato medido."),
        ("Una solución cumple 3 criterios técnicos, pero a sus usuarios no les resulta cómoda. ¿Qué indica eso?", "Que debe mejorarse en un criterio propio", "Los criterios propios también cuentan para decidir."),
    ],
    D=[
        arith("Se evalúan 8 criterios: 5 técnicos y el resto propios. ¿Cuántos criterios propios hay?", "8-5", "Se resta la cantidad de técnicos del total.", " criterios"),
        ("Tres soportes con los mismos tres criterios técnicos: peso máximo de 300 g, ancho máximo de 20 cm y costo máximo de $1.500. Soporte 1: 280 g, 22 cm, $1.200. Soporte 2: 290 g, 19 cm, $1.500. Soporte 3: 310 g, 18 cm, $1.000. ¿Cuál cumple los tres?", "El soporte 2", "El 1 pasa el ancho y el 3 pasa el peso."),
    ],
    ctx=("Un curso hizo un cartel de cartón de 40 cm por 30 cm para la puerta de la sala. Escribe un criterio técnico y un criterio propio para evaluarlo, y transforma el propio en uno técnico.", "Técnico: se lee a 3 metros de distancia. Propio: me parece atractivo. Transformado: al menos 8 de 10 compañeros nombran el tema del cartel después de mirarlo 5 segundos", "Se separan medidas de preferencias y se transforma una preferencia en un número."),
    sc=[
        ("¿Qué es un criterio técnico?", "Una condición que se puede medir o contar", "Se comprueba con datos."),
        ("¿Qué es un criterio propio?", "Una condición que depende de lo que valora una persona", "Cambia según quién evalúa."),
        ("¿Se evalúa la solución o a las personas que la hicieron?", "La solución", "La crítica es al diseño, no a las personas."),
    ],
    open_task=(
        "Escoge una solución. Solución 1: un portavasos de cartón de 10 cm de diámetro y 3 cm de alto. Solución 2: una funda de cartón para un lápiz grueso. Solución 3: un separador de libros hecho de cartón. Escribe tres criterios técnicos con números, dos criterios propios y convierte uno de los propios en técnico.",
        "Solución 1: técnicos: soporta un vaso de 200 g; mide 10 cm; cuesta menos de $500. Propios: me parece cómodo; me gusta el color. Convertido: 8 de 10 personas lo sostienen con una mano durante 1 minuto sin soltarlo",
        ["tres criterios técnicos con números", "dos criterios propios", "convierte uno propio en técnico", "no mezcla opiniones con medidas"],
        ["hoja con criterios clasificados"],
        ["escribir criterios técnicos sin número", "mezclar gustos con medidas"],
        "Pregunta: «¿cómo medirías este criterio?». Si no puede responder, es propio.",
    ),
    reinforce="Elige un objeto de tu casa y escribe un criterio técnico y uno propio para evaluarlo.",
    extend="Explica por qué dos personas pueden estar de acuerdo en los criterios técnicos y distintas en los propios.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Hoja, lápiz y las tablas escritas en este cuaderno.",
    use="Aprenderé a comparar soluciones con una matriz de evaluación, dándole más peso a los criterios más importantes. Sirve para decidir cuál solución es mejor con una regla clara.",
    prior=["Sé separar criterios propios y técnicos.", "Sé multiplicar y sumar.", "Sé leer una tabla."],
    explain=[
        "Una matriz de evaluación es una tabla con las soluciones en las columnas y los criterios en las filas. En cada casilla se anota un puntaje del 1 al 5: 1 es muy bajo y 5 es muy alto. Se evalúa cada solución con la misma regla, para que la comparación sea justa.",
        "No todos los criterios importan igual. Por eso se asigna a cada uno un peso, que es un número que indica cuánto vale. Por ejemplo, la seguridad puede pesar 3, el costo 2 y el color 1. Para obtener el puntaje de un criterio se multiplica el puntaje por el peso. Después se suman todos los resultados para obtener el total de cada solución.",
        "La solución con el total más alto es la mejor según esa matriz. Pero los puntajes dependen de los pesos: si cambian los pesos, el resultado puede cambiar. Por eso, antes de evaluar se acuerdan los pesos con el grupo y se anota por qué. Si hay empate, se desempata con el criterio de mayor peso.",
    ],
    vocab=[("matriz de evaluación", "tabla que compara soluciones con puntajes por criterio"), ("puntaje", "número del 1 al 5 que se asigna a un criterio"), ("peso", "número que indica cuánto importa un criterio"), ("total", "suma de todos los puntajes ponderados"), ("desempate", "forma de decidir cuando hay igual total")],
    worked=[
        ("Calcular un total ponderado", "Solución A: seguridad 4 (peso 3), costo 2 (peso 2), color 5 (peso 1). ¿Cuál es el total?", ["Seguridad: 4 × 3 = 12. Costo: 2 × 2 = 4. Color: 5 × 1 = 5.", "Sumo: 12 + 4 + 5."], "21 puntos"),
        ("Comparar dos soluciones", "Solución B: seguridad 3 (peso 3), costo 5 (peso 2), color 4 (peso 1). Compara con A, que tiene 21. ¿Cuál gana?", ["Seguridad: 9. Costo: 10. Color: 4. Total: 9 + 10 + 4 = 23.", "23 es mayor que 21."], "Gana B con 23 puntos contra 21"),
    ],
    mistakes=[
        ("Sumar los puntajes sin multiplicar por el peso.", "Se trata un criterio poco importante igual que uno muy importante.", "Multiplica cada puntaje por su peso y recién suma."),
        ("Cambiar los pesos después de ver cuál solución ganó.", "Se manipula el resultado para que gane la preferida.", "Acuerda los pesos antes de evaluar y anótalos."),
    ],
    R=[
        ("En la matriz, ¿qué indica el peso de un criterio?", "Cuánto importa ese criterio", "Más peso, más importancia."),
        ("Un puntaje de 5, ¿es muy alto o muy bajo?", "Muy alto", "La escala va de 1 (muy bajo) a 5 (muy alto)."),
        ("Para el total ponderado, ¿se multiplica o se divide el puntaje por el peso?", "Se multiplica", "Puntaje por peso."),
    ],
    C=[
        ("Si la seguridad pesa 3 y el color pesa 1, ¿cuál influye más en el total?", "La seguridad", "Su peso es mayor."),
        ("¿Qué debe hacerse con los pesos antes de evaluar? A acordarlos y anotarlos, B decidirlos después de ver los resultados.", "A", "Así la comparación es justa."),
        ("Dos soluciones tienen el mismo total. ¿Cómo desempatas? A usando el puntaje del criterio de mayor peso, B lanzando una moneda.", "A", "El desempate usa el criterio que más importa."),
    ],
    A=[
        arith("Una solución saca 3 en seguridad (peso 3), 4 en costo (peso 2) y 5 en tamaño (peso 1). ¿Cuál es su total?", "3*3+4*2+5*1", "Cada puntaje se multiplica por su peso y se suman los resultados.", " puntos"),
        arith("Otra solución saca 5 en resistencia (peso 4), 2 en ligereza (peso 2) y 3 en tamaño (peso 1). ¿Cuál es su total?", "5*4+2*2+3*1", "Se multiplica y se suma.", " puntos"),
        arith("Una matriz tiene 4 soluciones y 5 criterios. ¿Cuántos puntajes se deben anotar en total?", "4*5", "Cada solución recibe un puntaje en cada criterio.", " puntajes"),
    ],
    Z=[
        ("Solución X: seguridad 5, costo 2. Solución Y: seguridad 3, costo 5. Pesos: seguridad 3, costo 1. ¿Cuál gana?", "X", "X suma 17 (15 + 2) e Y suma 14 (9 + 5)."),
        ("Mateo dice: «Si cambio el peso del color de 1 a 5, mi solución gana». ¿Es correcto cambiar los pesos después de evaluar?", "No", "Los pesos se acuerdan antes para que la evaluación sea justa."),
    ],
    D=[
        arith("Un grupo evalúa 3 soluciones con los pesos seguridad 3, costo 2 y estética 1. La solución P saca 5, 3 y 2; la solución Q saca 4, 4 y 5. ¿Cuántos puntos más tiene Q que P?", "(4*3+4*2+5*1)-(5*3+3*2+2*1)", "P suma 23 y Q suma 25.", " puntos"),
        ("Pesos: seguridad 2 y costo 1. La solución M saca seguridad 5 y costo 2; la solución N saca seguridad 4 y costo 4. Si hay empate, gana la que saca más en el criterio de mayor peso. ¿Cuál gana?", "M", "Ambas suman 12 (10 + 2 y 8 + 4) y M saca más en seguridad, el criterio de mayor peso."),
    ],
    ctx=("Un grupo evalúa dos portalápices con los pesos resistencia 3, costo 2 y apariencia 1. El portalápices de Ana saca 4, 3 y 2; el de Bea saca 5, 2 y 1. Calcula el total de cada uno y di cuál gana.", "Ana: 12 + 6 + 2 = 20. Bea: 15 + 4 + 1 = 20. Hay empate; se desempata por resistencia, y gana Bea", "Se multiplican los puntajes por sus pesos y, con empate, se usa el criterio más pesado."),
    sc=[
        ("¿Qué es una matriz de evaluación?", "Una tabla que compara soluciones por criterios", "Reúne puntajes de cada solución."),
        ("¿Cómo se obtiene el total ponderado?", "Multiplicando cada puntaje por su peso y sumando", "Así cada criterio vale según su peso."),
        ("¿Cuándo se acuerdan los pesos?", "Antes de evaluar", "Así no se manipula el resultado."),
    ],
    open_task=(
        "Escoge una comparación. Comparación 1: dos estantes de cartón. Estante A: resistencia 4, costo 3, tamaño 5. Estante B: resistencia 5, costo 2, tamaño 3. Pesos: resistencia 3, costo 2, tamaño 1. Comparación 2: dos carteles. Cartel P: legibilidad 5, costo 2, durabilidad 3. Cartel Q: legibilidad 3, costo 5, durabilidad 4. Pesos: legibilidad 3, costo 1, durabilidad 2. Calcula los totales, decide cuál gana y explica por qué los pesos son razonables.",
        "Comparación 1: A: 12 + 6 + 5 = 23. B: 15 + 4 + 3 = 22. Gana A. Los pesos son razonables porque un estante debe resistir primero y el tamaño importa menos",
        ["multiplica cada puntaje por su peso", "suma bien los totales", "decide con los números", "justifica los pesos"],
        ["hoja con la matriz y los cálculos"],
        ["sumar sin ponderar", "cambiar los pesos después de evaluar"],
        "Pregunta: «¿por qué elegiste este peso?». Si no da razón, pídele relacionarlo con la necesidad.",
    ),
    reinforce="Elige dos objetos de tu casa y compáralos con tres criterios y puntajes del 1 al 5.",
    extend="Explica qué pasaría con el ganador si el criterio más importante bajara de peso 3 a peso 1.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja, lápiz y los datos escritos en este cuaderno. Si quieres practicar, un puente de papel y monedas de $10.",
    use="Aprenderé a medir criterios técnicos con pruebas repetidas, a calcular el promedio, el rango y el porcentaje de éxito, y a decidir si una solución es confiable. Sirve para evaluar con datos y no con impresiones.",
    prior=["Sé calcular un promedio.", "Sé que una prueba justa cambia una sola variable.", "Sé comparar un resultado con un criterio."],
    explain=[
        "Un criterio técnico se mide con una prueba que se repite varias veces. La resistencia se puede medir con cuánto peso aguanta una estructura; la durabilidad, con cuántas veces se usa antes de fallar; la estabilidad, con cuántas veces se mantiene en pie al moverse. Se hacen al menos tres pruebas. Antes de probar se escribe cómo se medirá y qué resultado cuenta como éxito.",
        "Con los datos se calcula el promedio, que es la suma de los resultados dividida entre la cantidad de pruebas. También se calcula el rango, que es la diferencia entre el dato mayor y el menor. Un rango pequeño indica que la solución se comporta de manera parecida cada vez. Un rango grande indica poca confiabilidad: a veces funciona y a veces no.",
        "El porcentaje de éxito dice en cuántas pruebas la solución cumplió el criterio: si cumple en 8 de 10 pruebas, el éxito es 80 %. Si el criterio exige cumplir siempre, 8 de 10 no es suficiente. Una solución confiable cumple el criterio en todas o casi todas las pruebas y mantiene un rango pequeño.",
    ],
    vocab=[("promedio", "suma de los datos dividida entre la cantidad de datos"), ("rango", "diferencia entre el dato mayor y el menor"), ("confiabilidad", "capacidad de funcionar parecido cada vez"), ("porcentaje de éxito", "pruebas cumplidas de cada 100"), ("durabilidad", "tiempo o número de usos antes de fallar")],
    worked=[
        ("Calcular promedio y rango", "Una repisa de cartón sostuvo en 3 pruebas 400 g, 500 g y 450 g. Calcula el promedio y el rango.", ["Promedio: (400 + 500 + 450) ÷ 3 = 1.350 ÷ 3 = 450 g.", "Rango: el mayor menos el menor, 500 − 400 = 100 g."], "Promedio 450 g y rango 100 g"),
        ("Calcular el porcentaje de éxito", "Un cierre se abrió y cerró correctamente en 18 de 20 pruebas. ¿Cuál es el porcentaje de éxito?", ["Divido 18 entre 20 y multiplico por 100.", "18 de 20 es lo mismo que 90 de 100."], "90 %"),
    ],
    mistakes=[
        ("Decir «funciona bien» porque lo probé una sola vez.", "Un resultado puede ser una casualidad.", "Repite la prueba varias veces y mira el rango."),
        ("Usar solo el promedio y olvidar el rango.", "Dos soluciones pueden tener el mismo promedio y comportarse muy distinto.", "Calcula también el rango para saber si es confiable."),
    ],
    R=[
        ("El rango, ¿es la diferencia entre el dato mayor y el menor o la suma de todos?", "La diferencia entre el dato mayor y el menor", "Es la definición del rango."),
        ("Una solución que cumple en 10 de 10 pruebas, ¿es poco confiable o muy confiable?", "Muy confiable", "Cumple en todas."),
        ("¿Qué se mide con el número de aperturas antes de que algo se rompa: la resistencia o la durabilidad?", "La durabilidad", "Cuenta cuántos usos aguanta."),
    ],
    C=[
        ("Dos soluciones tienen promedio 400 g. La primera tiene rango 20 g y la segunda rango 300 g. ¿Cuál es más confiable?", "La primera", "Un rango pequeño indica que siempre se comporta parecido."),
        ("¿Por qué conviene escribir cómo se medirá antes de probar? A para que la prueba sea justa y repetible, B para que la prueba dure más.", "A", "Así cualquiera repite la misma prueba."),
        ("Un criterio exige «sostiene 300 g siempre». La solución sostiene 300 g en 7 de 10 pruebas. ¿Cumple?", "No", "No cumple en todas las pruebas."),
    ],
    A=[
        arith("Cuatro pruebas de durabilidad: 40, 50, 60 y 50 aperturas antes de fallar. ¿Cuál es el promedio?", "(40+50+60+50)//4", "Se suman los datos y se divide entre 4.", " aperturas"),
        arith("En tres pruebas el soporte aguantó 210 g, 180 g y 240 g. ¿Cuál es el rango?", "240-180", "Se resta el menor del mayor.", " g"),
        arith("Un cordel resistió 15 de 20 tirones. ¿Qué porcentaje de éxito tiene?", "15*100//20", "Se calcula pruebas cumplidas por 100 entre el total.", " %"),
    ],
    Z=[
        ("Solución 1: 100 g, 100 g y 100 g. Solución 2: 20 g, 100 g y 180 g. Las dos tienen promedio 100 g. ¿Cuál es más confiable y por qué?", "La solución 1, porque su rango es 0", "Se comporta igual cada vez; la 2 varía mucho."),
        ("Ana dice: «Mi puente cumple porque en una prueba aguantó 500 g». ¿Qué le responderías?", "Que repita la prueba al menos 3 veces", "Una prueba no basta para evaluar."),
    ],
    D=[
        arith("Seis pruebas de un portalápices al volcarse: aguantó 12, 14, 12, 15, 12 y 13 lápices. ¿Cuál es el promedio?", "(12+14+12+15+12+13)//6", "Se suman y se divide entre 6.", " lápices"),
        ("Criterio: promedio de al menos 24 aperturas y rango de 6 o menos. Cierre X: 22, 25 y 28. Cierre Y: 18, 20 y 22. Cierre Z: 15, 30 y 25. ¿Cuál cumple los dos?", "El cierre X", "X tiene promedio 25 y rango 6; Y tiene promedio 20 y Z tiene rango 15."),
    ],
    ctx=("Pruebas una puerta de cartón con bisagra de cinta: se abre y cierra sin romperse 40, 44 y 42 veces en tres ensayos. Calcula el promedio y el rango, y di si es confiable.", "Promedio: 42 veces. Rango: 4 veces. Es confiable porque los resultados son parecidos", "Se calcula (40 + 44 + 42) ÷ 3 y 44 − 40."),
    sc=[
        ("¿Qué indica un rango pequeño?", "Que la solución se comporta parecido cada vez", "Los datos están cerca."),
        ("¿Cuántas pruebas se necesitan como mínimo para evaluar?", "Tres", "Con tres datos se calcula un promedio."),
        ("¿Qué porcentaje es 9 pruebas cumplidas de 10?", "90 %", "9 de 10 es 90 de 100."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: un cierre de cartón se abrió y cerró bien 26, 30 y 28 veces en tres ensayos. Registro 2: una estructura de papel sostuvo 250 g, 300 g, 200 g y 250 g en cuatro ensayos. Calcula el promedio, el rango, el porcentaje de éxito si el criterio es «cumplir al menos 25 veces» (para el registro 1) o «sostener al menos 220 g» (para el registro 2), y escribe una conclusión.",
        "Registro 1: promedio 28, rango 4, cumple en 3 de 3 (100 %). Conclusión: es confiable porque cumple siempre y el rango es pequeño",
        ["calcula bien promedio y rango", "calcula el porcentaje de éxito", "conclusión con datos", "habla de confiabilidad"],
        ["hoja con cálculos y conclusión"],
        ["usar solo el promedio", "olvidar el porcentaje de éxito"],
        "Pregunta: «¿cuánto varían tus datos?». Si no calcula el rango, pídele hacerlo.",
    ),
    reinforce="Haz un puente con una hoja doblada entre dos libros, prueba 5 veces cuántas monedas de $10 sostiene y calcula el promedio y el rango.",
    extend="Explica por qué una solución con promedio alto pero rango grande puede no ser la mejor.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a evaluar la seguridad, el mantenimiento y el costo de una solución, y a decidir entre repararla o reemplazarla. Sirve para elegir soluciones que duren y no hagan daño.",
    prior=["Sé dividir.", "Sé que una solución tiene un costo.", "Sé que una reparación devuelve la función a un objeto."],
    explain=[
        "Además de medir si una solución funciona, hay que evaluar si es segura y si se puede mantener. La seguridad revisa que no tenga bordes que corten ni piezas que se suelten, y que no se vuelque. Para el uso por niñas y niños pequeños se revisa además que no tenga piezas pequeñas que se puedan tragar. El mantenimiento son las acciones simples para que siga funcionando: limpiar, apretar, cambiar una pieza.",
        "El costo no es solo lo que se paga al comienzo. Un cálculo útil es el costo por uso o por mes: el costo total dividido entre la cantidad de usos o de meses que dura. Si una reparación de $3.000 permite usar un objeto 12 meses, cuesta $250 por mes. Si uno nuevo de $9.000 dura 24 meses, cuesta $375 por mes. En este caso conviene reparar.",
        "La decisión de reparar o reemplazar también considera el ambiente. Reparar evita botar el objeto y gasta menos material. Pero si la reparación no es segura, o si el objeto dañado puede lastimar, conviene reemplazarlo. Evaluar bien es mirar la seguridad, el costo por uso y el efecto ambiental.",
    ],
    vocab=[("mantenimiento", "acciones simples para que algo siga funcionando"), ("costo por uso", "costo total dividido entre el número de usos"), ("seguridad", "ausencia de riesgo de daño al usar algo"), ("reemplazar", "cambiar un objeto dañado por otro nuevo"), ("vida útil", "tiempo durante el cual un objeto sirve")],
    worked=[
        ("Calcular el costo por mes", "Reparar una silla cuesta $3.000 y la deja servir 12 meses. Una silla nueva cuesta $9.000 y sirve 24 meses. ¿Cuál cuesta menos por mes?", ["Reparada: 3.000 ÷ 12 = 250 por mes.", "Nueva: 9.000 ÷ 24 = 375 por mes."], "La reparación cuesta menos por mes: $250 contra $375"),
        ("Evaluar la seguridad", "Un organizador de cartón tiene una esquina con una tira metálica suelta que sobresale. ¿Qué decides?", ["La tira puede cortar o pinchar.", "No se usa hasta que se retire o se reemplace por una pieza segura."], "Se debe corregir la tira antes de usarlo, por seguridad"),
    ],
    mistakes=[
        ("Elegir siempre lo más barato al comprar.", "Lo barato puede durar poco y salir más caro por uso.", "Calcula el costo por uso o por mes."),
        ("Reparar un objeto que ya no es seguro.", "Una reparación que no elimina el riesgo sigue siendo peligrosa.", "Si el riesgo no desaparece, reemplázalo."),
    ],
    R=[
        ("El mantenimiento, ¿son acciones simples para que algo siga funcionando o la compra de uno nuevo?", "Acciones simples para que siga funcionando", "Es la definición de la clase."),
        ("Un borde que corta, ¿es un problema de seguridad o de estética?", "De seguridad", "Puede causar un daño."),
        ("Un objeto sirve 24 meses antes de fallar. ¿Cuál es su vida útil?", "24 meses", "La vida útil es el tiempo durante el cual sirve."),
    ],
    C=[
        ("¿Qué indica el costo por mes? A cuánto cuesta mantener el objeto cada mes de uso, B cuánto costó el objeto nuevo.", "A", "Es el costo total dividido entre los meses de uso."),
        ("¿Cuándo conviene reemplazar un objeto en vez de repararlo?", "Cuando la reparación no elimina el riesgo", "La seguridad pesa más que el ahorro."),
        ("Reparar un objeto en vez de botarlo, ¿gasta más o menos material?", "Menos", "Se conserva el objeto original."),
    ],
    A=[
        arith("Una reparación cuesta $4.000 y permite usar el objeto 16 meses. ¿Cuánto cuesta por mes?", "4000//16", "Se divide el costo entre los meses.", " pesos"),
        arith("Un objeto nuevo cuesta $10.000 y dura 20 meses. ¿Cuánto cuesta por mes?", "10000//20", "Se divide el costo entre los meses.", " pesos"),
        ("Opción 1: reparar por $2.000 y usar 10 meses. Opción 2: reemplazar por $3.000 y usar 10 meses. ¿Cuál cuesta menos por mes?", "La opción 1", "Cuesta $200 por mes; la otra, $300."),
    ],
    Z=[
        ("Reparar una bicicleta de un niño cuesta $5.000 y dura 10 meses; la reparación deja un tornillo que sobresale y puede lastimar. Reemplazarla cuesta $20.000 y dura 40 meses. Los costos por mes son $500 y $500. ¿Qué eliges y por qué?", "Reemplazarla, porque la reparación no es segura", "Empatan en costo por mes, y el riesgo decide."),
        ("Mateo dice: «Lo barato siempre es mejor». ¿Qué le responderías?", "Que debe calcular el costo por uso", "Lo barato puede durar poco."),
    ],
    D=[
        arith("Un objeto se reparó dos veces: la primera costó $1.500 y la segunda $2.500. Entre ambas lo usaste 20 meses. ¿Cuánto costó por mes?", "(1500+2500)//20", "Se suma el gasto y se divide entre los meses.", " pesos"),
        ("Un objeto cuesta $6.000 y dura 12 meses. Otro cuesta $8.000 y dura 20 meses. Si ambos son seguros, ¿cuál conviene por costo mensual?", "El de $8.000", "Cuesta $400 por mes contra $500 del otro."),
    ],
    ctx=("En tu casa, una silla pequeña tiene una pata floja. Arreglarla con un tornillo nuevo costaría $1.200 y la dejaría servir 12 meses. Una silla nueva costaría $6.000 y duraría 30 meses. Calcula el costo por mes de cada opción y di cuál elegirías si el arreglo es seguro.", "Arreglo: $100 por mes. Silla nueva: $200 por mes. Conviene arreglar si es seguro", "Se calcula 1.200 ÷ 12 = 100 y 6.000 ÷ 30 = 200."),
    sc=[
        ("¿Cómo se calcula el costo por mes?", "Costo total dividido entre los meses de uso", "Compara opciones distintas."),
        ("¿Qué pasa si una reparación deja un riesgo?", "Conviene reemplazar", "La seguridad es lo primero."),
        ("¿Reparar suele gastar más o menos material que reemplazar?", "Menos", "No se compra un objeto completo."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: una mochila con un cierre roto; repararla cuesta $2.000 y dura 10 meses; una nueva cuesta $12.000 y dura 24 meses. Caso 2: un organizador de cartón que se dobló; repararlo cuesta $1.000 y dura 5 meses; hacer uno nuevo cuesta $4.000 y dura 16 meses. Calcula el costo por mes de cada opción, di cuál conviene un riesgo de seguridad que revisarías y una frase sobre el efecto ambiental de tu decisión.",
        "Caso 1: reparar cuesta $200 por mes; la nueva $500 por mes. Conviene reparar. Riesgo: que el cierre roto deje un borde que raspe, se revisa antes. Ambiente: reparar evita botar la mochila",
        ["calcula el costo por mes de las dos opciones", "decide con los números", "nombra un riesgo de seguridad", "considera el efecto ambiental"],
        ["hoja con cálculos y decisión"],
        ["elegir solo por el precio inicial", "olvidar la seguridad"],
        "Pregunta: «¿cuánto cuesta por mes cada opción?». Si no calcula, pídele dividir.",
    ),
    reinforce="Elige un objeto de tu casa, anota cuánto costó y cuántos meses lo usas, y calcula el costo por mes.",
    extend="Explica un ejemplo en que reparar sería peor que reemplazar, aunque cueste menos.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja, lápiz y los informes escritos en este cuaderno.",
    use="Aprenderé a escribir una conclusión de evaluación con hechos y no con opiniones, a separar lo que cumple de lo que no, y a recomendar mejoras. Sirve para comunicar una evaluación honesta y útil.",
    prior=["Sé usar criterios propios y técnicos.", "Sé calcular promedio, rango y porcentaje.", "Sé que se evalúa la solución y no a las personas."],
    explain=[
        "Una evaluación termina con una conclusión. Primero se distingue un hecho, que se puede comprobar («sostuvo 450 g»), de una opinión, que depende de la persona («es muy buena»). La conclusión se apoya en hechos. Después se revisa criterio por criterio si la solución cumple, cumple a medias o no cumple.",
        "Una buena conclusión tiene cuatro partes: qué se evaluó, qué criterios cumple (con su dato), qué criterios no cumple (con su dato) y qué mejora se recomienda. La recomendación cambia una sola cosa a la vez, por ejemplo «reforzar la base con una segunda capa de cartón». Así se podrá probar si la mejora funcionó.",
        "Al comunicar la evaluación a otras personas, habla de la solución con respeto: «el soporte se vuelca con 4 libros» y no «tu soporte es malo». Reconoce lo que funciona y explica lo que se puede mejorar. Si usas datos de otras personas, anota de dónde vienen. Una evaluación honesta incluye también los resultados que no salieron bien.",
    ],
    vocab=[("hecho", "afirmación que se puede comprobar"), ("opinión", "afirmación que depende de lo que piensa una persona"), ("conclusión", "decisión final basada en los datos"), ("recomendación", "mejora que se propone a partir de la evaluación"), ("evaluación honesta", "evaluación que incluye también lo que no salió bien")],
    worked=[
        ("Separar hechos y opiniones", "¿Cuáles son hechos? (1) El puente sostuvo 500 g. (2) El puente es feo. (3) El puente se armó en 20 minutos. (4) El puente es el mejor del curso.", ["Un hecho se puede comprobar con una medida o un conteo.", "El 1 y el 3 se comprueban; el 2 y el 4 dependen de la opinión."], "Hechos: 1 y 3. Opiniones: 2 y 4"),
        ("Armar una conclusión", "El soporte de cartón sostuvo 5, 5 y 3 lápices; el criterio pide 5 en cada prueba. Cuesta $800 (límite $1.000). Escribe una conclusión.", ["Cumple el costo (800 es menor que 1.000). No cumple la resistencia, porque en una prueba sostuvo 3.", "Recomiendo reforzar la base con una segunda capa y volver a probar."], "Cumple el costo y no cumple la resistencia (3 lápices en una prueba); se recomienda reforzar la base"),
    ],
    mistakes=[
        ("Escribir «el diseño es malo» sin datos.", "Es una opinión que no ayuda a mejorar.", "Escribe qué criterio no cumple y con qué dato."),
        ("Recomendar cambiar tres cosas a la vez.", "Después no se sabrá cuál cambio produjo la mejora.", "Recomienda un solo cambio y vuelve a probar."),
    ],
    R=[
        ("«Sostuvo 450 g», ¿es un hecho o una opinión?", "Un hecho", "Se puede comprobar con una balanza."),
        ("«Es bonito», ¿es un hecho o una opinión?", "Una opinión", "Depende de quien mire."),
        ("¿La recomendación de una evaluación cambia una cosa o muchas a la vez?", "Una cosa", "Así se puede probar si funciona."),
    ],
    C=[
        ("¿Cuál conclusión es mejor? A «Cumple el costo ($800) pero se vuelca con 4 libros», B «No me convence».", "A", "A nombra criterios y datos."),
        ("¿Por qué incluir también lo que no salió bien?", "Para que la evaluación sea honesta y sirva para mejorar", "Ocultar las fallas impide corregirlas."),
        ("Para comentar el diseño de otra persona, ¿qué frase es respetuosa? A «el soporte se vuelca con 4 libros», B «hiciste un soporte inútil».", "A", "A habla del objeto con un dato; B ataca a la persona."),
    ],
    A=[
        arith("Un diseño cumple 4 de 5 criterios. ¿Cuántos criterios no cumple?", "5-4", "Se resta lo cumplido del total.", " criterio"),
        arith("Un diseño cumplió el criterio en 9 de 12 pruebas. ¿Cuántas pruebas no cumplió?", "12-9", "Se resta lo cumplido del total.", " pruebas"),
        ("Ordena las partes de la conclusión: (a) mejora recomendada, (b) qué se evaluó, (c) criterios que no cumple con datos, (d) criterios que cumple con datos. ¿Cuál es el orden?", "b, d, c, a", "Primero lo evaluado, luego lo cumplido, lo no cumplido y la recomendación."),
    ],
    Z=[
        ("Un grupo escribe: «El soporte es muy resistente y lo recomendamos». Otro escribe: «El soporte sostuvo 600 g en 3 de 3 pruebas; cumple el criterio de 500 g». ¿Cuál conclusión es más sólida?", "La del segundo grupo", "Muestra el dato y lo compara con el criterio."),
        ("El soporte falló una vez de tres. Un compañero propone no contarlo para que el resultado se vea mejor. ¿Es correcto?", "No", "Una evaluación honesta incluye todos los resultados."),
    ],
    D=[
        arith("Un informe tiene 12 afirmaciones; 7 son hechos con datos y el resto son opiniones. ¿Cuántas son opiniones?", "12-7", "Se restan los hechos del total.", " opiniones"),
        ("Dos recomendaciones. R1: «reforzar la base con una segunda capa». R2: «cambiar el material, la base y el tamaño». ¿Cuál permite saber qué mejoró?", "R1", "Cambia una sola cosa."),
    ],
    ctx=("Evaluaste un porta-libros de cartón. Sostuvo 6, 6 y 4 libros; el criterio pide 6. Costó $1.200 (el límite era $1.500). Escribe una conclusión con lo que cumple, lo que no, y una recomendación.", "Cumple el costo ($1.200 es menor que $1.500). No cumple la resistencia: en una prueba sostuvo 4 libros. Recomiendo reforzar el fondo con una segunda capa y repetir la prueba", "Se nombran criterios cumplidos y no cumplidos con datos y una sola mejora."),
    sc=[
        ("¿En qué se diferencia un hecho de una opinión?", "El hecho se puede comprobar y la opinión depende de la persona", "Esa diferencia define la conclusión."),
        ("¿Cuántos cambios recomiendas a la vez?", "Uno", "Así se puede probar la mejora."),
        ("¿Se critica la solución o a las personas?", "La solución", "El respeto es parte de evaluar."),
    ],
    open_task=(
        "Escoge un informe. Informe 1: un porta-lápices de cartón de $900 (límite $1.000) que sostuvo 12, 12 y 8 lápices (el criterio pide 12 en cada prueba). Informe 2: un cartel de 40 cm por 30 cm que se lee a 2 metros, pero no a 3 metros (el criterio pide 3 metros), y costó $500 (límite $800). Escribe la conclusión con las cuatro partes, separando hechos de opiniones, y una recomendación con un solo cambio.",
        "Informe 1: evaluado: porta-lápices. Cumple el costo ($900 menor que $1.000). No cumple la resistencia: en una prueba sostuvo 8 lápices. Recomiendo ensanchar la base y repetir las tres pruebas",
        ["cuatro partes de la conclusión", "usa hechos con datos", "recomienda un solo cambio", "lenguaje respetuoso"],
        ["hoja con conclusión redactada"],
        ["usar solo opiniones", "recomendar varios cambios a la vez"],
        "Pregunta: «¿qué dato apoya esta frase?». Si no tiene, pídele reemplazarla por un hecho.",
    ),
    reinforce="Escribe tres hechos y tres opiniones sobre un objeto de tu casa.",
    extend="Explica por qué es útil que una evaluación incluya las pruebas que fallaron.",
)

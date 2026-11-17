"""Gastronomía TP 4.º medio, mención Cocina: OAM-04 (variaciones de recetas y de la forma de servirlas) y OAM-05 (cartas y menús para servicios de consumo frecuente o masivo). Todo en papel, sin recetas ni técnicas paso a paso: datos «de ejemplo»."""
from __future__ import annotations

from tp_gaco_common import build

O4 = "TP-GACO-4-OAM-04"
O5 = "TP-GACO-4-OAM-05"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: la práctica en cocina requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); no te habilita para trabajar."

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (variaciones de una receta, casino de ejemplo, inventado). Receta base: «Guiso de verduras de ejemplo». Variaciones posibles (de ejemplo): versión vegetariana, versión baja en sal, versión con porción pequeña. "
     "Cada variación es una versión nueva con su propia ficha: ingredientes cambiados, costo, alérgenos y porción. Reglas: toda variación la aprueba la jefa de cocina; se registra con número de versión; se evalúa con una prueba sensorial antes de ofrecerla; se rotulan los alérgenos. "
     "Demanda diversa: personas con gustos, costumbres y necesidades alimentarias distintas.")
build(
    O4, 1, F,
    use="Aprenderé a situar las variaciones de recetas: por qué se hacen, quién las aprueba, cómo se registran y qué riesgos tienen.",
    prior=["Conozco la receta estándar y el costeo.", "Conozco los alérgenos y el rótulo.", "Sé contar y multiplicar."],
    explain=[
        "En Gastronomía, una variación es un cambio planificado en una receta o en la forma de servirla, para mejorar su sabor o su textura o para adaptarla a las necesidades de distintas personas. Cuando la clientela es variada, es decir, hay una demanda diversa, se necesitan versiones distintas de un mismo plato, como una versión vegetariana, una baja en sal o una de porción pequeña.",
        "Cada variación es una versión nueva de la receta: tiene su propia ficha con ingredientes, costo, alérgenos y porción. La aprueba la jefa de cocina, se registra con un número de versión y se evalúa con una prueba sensorial, que es la evaluación de aspecto, color, olor, sabor y textura. Nunca se cambia una receta sin registro.",
        "El mayor riesgo es cambiar un ingrediente y no actualizar los alérgenos: una persona alérgica podría consumir algo que no esperaba. Por eso toda variación se rotula. Este cuaderno trabaja en papel y no enseña a elaborar los platos. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("variación", "cambio planificado de una receta o de su forma de servirla"), ("versión", "variante de una receta con su propia ficha y registro"), ("demanda diversa", "clientela con gustos y necesidades distintas"), ("prueba sensorial", "evaluación de aspecto, color, olor, sabor y textura"), ("registro de versiones", "anotación de cada cambio con número, fecha y aprobación")],
    worked=[
        ("Contar versiones", "Una receta de ejemplo tiene la base y 2 variaciones. ¿Cuántas versiones hay en total?", ["Se cuenta la base y las variaciones.", "1 + 2 = 3."], "3 versiones"),
        ("Reconocer una necesidad", "Un cliente de ejemplo pide una opción baja en sal. ¿A qué tipo de variación corresponde?", ["Responde a una necesidad alimentaria.", "Es una versión baja en sal."], "A una versión baja en sal"),
    ],
    mistakes=[("Cambiar un ingrediente y no actualizar los alérgenos.", "Las personas alérgicas pueden consumir algo que creen que no contiene su alérgeno.", "Actualiza la ficha y el rótulo de alérgenos con cada versión."),
              ("Ofrecer una variación sin probarla ni registrarla.", "No se sabe si agrada ni se puede repetir igual.", "Realiza la prueba sensorial y registra la versión con su número.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es una variación de una receta?", "Un cambio planificado en la receta o en la forma de servirla", "Un error de un cocinero al seguir la receta", "El reemplazo definitivo de la receta base sin registro", "La variación es un cambio deliberado, aprobado y registrado."),
        ("abc", "{F} ¿Quién aprueba una variación?", "La jefa de cocina", "Cualquier cocinero", "El proveedor", "La ficha asigna la aprobación a la jefa de cocina."),
        ("abc", "{F} ¿Qué se registra de cada variación?", "Su número de versión y su ficha propia", "Solo el nombre del cocinero", "Solo el precio de venta", "Cada variación es una versión con ficha y número."),
        ("=", "{F} La receta base tiene 3 variaciones. ¿Cuántas versiones hay en total, contando la base?", "1+3", "Se suma la versión base y las variaciones.", " versiones"),
        ("abc", "{F} ¿Qué es la demanda diversa?", "Clientela con gustos y necesidades alimentarias distintas", "Una receta con muchos ingredientes", "Un menú con precios variables", "La ficha la define como personas con necesidades y gustos distintos."),
        ("abc", "{F} ¿Para qué se hace una prueba sensorial antes de ofrecer una variación?", "Para evaluar aspecto, color, olor, sabor y textura de la nueva versión", "Para calcular su precio de venta", "Para registrar al proveedor", "La prueba sensorial evalúa la calidad que perciben los sentidos."),
        ("abc", "{F} Una variación reemplaza un ingrediente por otro que contiene un alérgeno nuevo. ¿Qué corresponde?", "Actualizar la ficha y rotular el alérgeno nuevo", "No informar, porque la receta es la misma", "Informar solo si alguien pregunta", "El cliente debe conocer los alérgenos de la versión que consume."),
        ("=", "Un casino de ejemplo produce 3 versiones de un guiso con 20 porciones cada una. ¿Cuántas porciones son?", "3*20", "Se multiplican las versiones por las porciones de cada una.", " porciones"),
        ("abc", "{F} Un cocinero cree que el guiso quedará más suave con otro ingrediente y lo ofrece de inmediato. ¿Qué corresponde?", "Presentarlo como propuesta, probarlo y registrarlo con aprobación antes de ofrecerlo", "Ofrecerlo y avisar al final del día", "Ofrecerlo solo si nadie reclama", "Un cambio se aprueba y se prueba antes de llegar al cliente."),
        ("abc", "{F} Una versión vegetariana reemplaza la carne por legumbres. ¿Qué debe revisarse?", "Los alérgenos nuevos, el costo y la porción", "Solo el nombre", "Nada, porque es más sana", "Cada versión tiene ficha propia con ingredientes, costo, alérgenos y porción."),
        ("=", "Un casino de ejemplo sirve 200 almuerzos y el 10 % elige la versión vegetariana. ¿Cuántos almuerzos vegetarianos son?", "200*10//100", "Se calcula el 10 % del total de almuerzos.", " almuerzos"),
        ("abc", "{F} Una versión «con porción pequeña» se sirve en un recipiente igual al de la porción normal. ¿Qué problema puede ocurrir?", "Que el cliente piense que recibe menos de lo que paga o que se confunda la versión", "Ninguno, porque el recipiente no importa", "Que la receta base desaparezca", "Servir una porción distinta exige identificarla claramente."),
        ("abc", "{F} Un compañero dice que no hace falta registrar la variación si fue solo un cambio pequeño. ¿Qué respuesta es correcta?", "Todo cambio, incluso pequeño, se registra para repetirlo y controlar alérgenos y costo", "Tiene razón, el registro es solo para cambios grandes", "El registro es opcional si la jefa está presente", "Un cambio sin registro se pierde y puede afectar alérgenos y costos."),
    ],
    ctx=("abc", "{F} Un colegio solicita una opción vegetariana para 20 estudiantes. ¿Qué pasos de gestión corresponde seguir?", "Definir la versión con su ficha, calcular costo y alérgenos, probarla y registrarla antes de ofrecerla", "Servir cualquier plato sin carne y avisar si hay reclamos", "Pedir a los estudiantes que traigan su comida", "Una versión se define, se costea, se prueba y se registra antes de servirse."),
    sc=[
        ("En Gastronomía: ¿quién aprueba una variación?", "La jefa de cocina", "Responde por la calidad y por la información al cliente."),
        ("¿Qué evalúa la prueba sensorial?", "Aspecto, color, olor, sabor y textura", "Son las características que perciben los sentidos."),
        ("¿Qué se actualiza si cambia un ingrediente?", "Los alérgenos y la ficha", "Así la información al cliente sigue siendo verdadera."),
    ],
    op=("Receta base de ejemplo «Arroz con verduras de ejemplo». El casino quiere ofrecer una versión baja en sal y una versión con porción pequeña para estudiantes de básica. "
        "Escribe: (a) qué documentos o datos tendría cada versión, (b) quién las aprueba, (c) qué prueba se haría antes de ofrecerlas, y (d) qué se debe informar sobre alérgenos si en la versión baja en sal se agrega un caldo que contiene apio (alérgeno declarado de ejemplo).",
        "(a) Cada versión tiene su ficha con ingredientes, costo, alérgenos y porción, y un número de versión. (b) La aprueba la jefa de cocina. (c) Una prueba sensorial de aspecto, color, olor, sabor y textura. (d) Se actualiza el rótulo para informar que contiene apio.",
        ["indica ficha, número de versión y datos de cada versión", "nombra a la jefa y la prueba sensorial", "actualiza el rótulo de alérgenos"],
        ["hoja con cuatro respuestas"],
        ["ofrecer las versiones sin aprobación", "olvidar el rótulo de alérgenos", "describir cómo preparar el plato"],
        "Pregunta: «¿qué informa el rótulo si el caldo lleva apio?». Debe responder que contiene apio."),
    reinforce="Inventa una receta base y tres variaciones para una demanda diversa, y escribe qué cambia en cada una.",
    extend="Explica por qué una variación bien registrada permite repetir el resultado en otro turno.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (registro de versiones de ejemplo). Receta «Tortilla de verduras de ejemplo». Versión 1 (base): huevo 600 g, verduras 900 g, harina 100 g, sal 10 g. Versión 2 (baja en sal): igual a la versión 1, pero con sal 6 g. "
     "Versión 3 (sin huevo): el huevo se reemplaza por una mezcla de legumbres de 600 g; elimina el alérgeno huevo y agrega soya (alérgeno declarado de ejemplo). "
     "Prueba sensorial (escala de 1 a 5; 10 personas): versión 1, suma 40; versión 2, suma 40; versión 3, suma 30. Aprueba la jefa de cocina; el encargado de calidad verifica el registro.")
build(
    O4, 2, F,
    use="Aprenderé a leer un registro de versiones y a usar los conceptos de sustitución, versión y prueba sensorial para decidir si una variación se adopta.",
    prior=["Conozco la variación y la versión.", "Sé calcular porcentajes.", "Conozco los alérgenos y la receta estándar."],
    explain=[
        "Un registro de versiones anota cada cambio de una receta: qué ingredientes cambian, en qué cantidad, cómo cambian los alérgenos y quién lo aprobó. Así se sabe qué versión se está ofreciendo y se puede volver a la anterior. La sustitución es reemplazar un ingrediente por otro que cumple una función parecida; después de sustituir se revisan alérgenos, costo y porción.",
        "La prueba sensorial se hace con una escala de 1 a 5 aplicada por varias personas. La suma de los puntajes y el porcentaje respecto del máximo posible permiten comparar versiones. El máximo posible es la cantidad de personas multiplicada por 5. Por ejemplo, con 10 personas el máximo es 50.",
        "Las cantidades de este registro son de ejemplo y solo sirven para calcular y comparar. Aprueba la jefa de cocina y verifica el encargado de calidad que lo servido sea la versión registrada. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("sustitución", "reemplazo de un ingrediente por otro de función parecida"), ("escala de 1 a 5", "puntaje de 1 (muy deficiente) a 5 (muy bueno)"), ("puntaje máximo", "personas por 5"), ("reducción", "disminución de una cantidad respecto de la anterior"), ("encargado de calidad", "persona que verifica que lo servido coincide con la ficha")],
    worked=[
        ("Calcular una reducción", "Una receta de ejemplo tenía 20 g de sal y ahora lleva 15 g. ¿Cuántos gramos se redujo?", ["Se resta la cantidad nueva a la anterior.", "20 − 15 = 5."], "5 g"),
        ("Calcular el máximo de una prueba", "Si 8 personas evalúan con una escala de 1 a 5, ¿cuál es el puntaje máximo posible?", ["Se multiplican las personas por 5.", "8 × 5 = 40."], "40 puntos"),
    ],
    mistakes=[("Reemplazar un ingrediente por otro «equivalente» sin revisar sus alérgenos.", "El nuevo ingrediente puede contener un alérgeno que el anterior no tenía.", "Revisa alérgenos, costo y porción de cada sustitución."),
              ("Comparar dos pruebas con distinto número de personas usando solo la suma.", "La suma depende de cuántas personas evaluaron.", "Compara el porcentaje del máximo posible.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es una sustitución en una receta?", "El reemplazo de un ingrediente por otro de función parecida", "El aumento de la cantidad de todos los ingredientes", "El cambio de nombre del plato", "La sustitución cambia un ingrediente por otro, y exige revisar alérgenos y costo."),
        ("=", "{F} ¿Cuántos gramos se redujo la sal en la versión 2 respecto de la versión 1?", "10-6", "A la sal de la versión 1 se le resta la sal de la versión 2.", " g"),
        ("=", "{F} ¿Qué porcentaje de reducción de sal hay entre la versión 1 y la 2?", "(10-6)*100//10", "Se multiplica la reducción por 100 y se divide por la cantidad original.", " %"),
        ("abc", "{F} ¿Qué alérgeno elimina la versión 3?", "El huevo", "La soya", "La harina", "La ficha dice que la versión 3 elimina el huevo y agrega soya."),
        ("abc", "{F} ¿Qué alérgeno agrega la versión 3?", "La soya", "El huevo", "El gluten", "Según la ficha, la mezcla de legumbres agrega soya como alérgeno declarado."),
        ("=", "{F} ¿Cuál es el puntaje máximo posible de la prueba con 10 personas?", "10*5", "Se multiplican las personas por el puntaje más alto de la escala.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la versión 1?", "40*100//50", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la versión 3?", "30*100//50", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("abc", "{F} ¿Qué versión obtuvo menor puntaje en la prueba sensorial?", "La versión 3", "La versión 1", "La versión 2", "La versión 3 sumó 30, menos que las otras dos."),
        ("abc", "{F} ¿Quién verifica que lo servido corresponda a la versión registrada?", "El encargado de calidad", "El cocinero", "El proveedor", "La ficha asigna esa verificación al encargado de calidad."),
        ("abc", "{F} Un cocinero propone cambiar la versión 2 por una con 4 g de sal sin registrarlo. ¿Qué corresponde?", "Registrar la nueva versión y obtener la aprobación de la jefa", "Cambiarla y avisar después", "Cambiarla solo en el turno de la tarde", "Un cambio de cantidad crea una nueva versión que se aprueba y se registra."),
        ("abc", "{F} Se comparan dos pruebas: en la A, 10 personas dieron suma 40; en la B, 8 personas dieron suma 36. ¿Cuál tiene mejor porcentaje del máximo?", "La B, con 90 %", "La A, con 80 %", "Ambas tienen el mismo porcentaje", "A obtiene 80 % de 50 y B obtiene 90 % de 40; el porcentaje permite comparar."),
        ("=", "{F} La versión 3 usa 600 g de legumbres en lugar de 600 g de huevo. Si se producen 4 veces la receta, ¿cuántos gramos de legumbres se usan?", "600*4", "Se multiplica la cantidad de legumbres de la ficha por el número de veces.", " g"),
    ],
    ctx=("abc", "{F} La jefa debe decidir si adopta la versión 3 para la demanda de clientes alérgicos al huevo. ¿Qué datos de la ficha debe considerar?", "La prueba sensorial, el alérgeno soya que se agrega y el costo, antes de aprobarla y rotularla", "Solo el nombre de la versión", "Solo que elimina el huevo", "Eliminar un alérgeno puede agregar otro, y la aceptación del producto también importa."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el puntaje máximo de una prueba sensorial?", "Personas por 5", "Es el puntaje si todos dan la nota máxima."),
        ("¿Para qué se registra cada versión?", "Para saber qué se ofrece y poder repetirla", "Facilita el control y la trazabilidad."),
        ("¿Qué se revisa tras una sustitución?", "Alérgenos, costo y porción", "Cada cambio afecta esos tres datos."),
    ],
    op=("Registro de ejemplo. Versión 1 de una «Salsa de verduras de ejemplo»: verduras 1.000 g, aceite 50 g, sal 10 g. Versión 2: sal 5 g. Prueba sensorial de 10 personas con escala de 1 a 5: versión 1, suma 42; versión 2, suma 36. Criterio de ejemplo: se adopta si obtiene al menos 80 % del máximo. "
        "Calcula la reducción de sal y su porcentaje, el máximo posible y el porcentaje de cada versión, y decide cuál se adopta y por qué.",
        "Reducción: 10 − 5 = 5 g, es decir, 50 %. Máximo: 10 × 5 = 50. Versión 1: 42 × 100 ÷ 50 = 84 %. Versión 2: 36 × 100 ÷ 50 = 72 %. Se adopta la versión 1, porque cumple al menos 80 %; la 2 no lo alcanza.",
        ["calcula 5 g y 50 %", "calcula el máximo 50 y los porcentajes 84 % y 72 %", "decide con el criterio de 80 %"],
        ["hoja con cálculos y decisión"],
        ["usar solo la suma sin porcentaje", "adoptar la versión de 72 %", "no registrar la decisión"],
        "Pregunta: «¿cuál es el máximo posible?». Si responde 10, repasa personas por 5."),
    reinforce="Inventa un registro de tres versiones de una receta y calcula el porcentaje del máximo de una prueba sensorial.",
    extend="Explica por qué se compara el porcentaje del máximo y no solo la suma cuando evalúan distintos números de personas.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (caso de variación vegetariana, de ejemplo, inventado). Versión base «Guiso de carne de ejemplo», rinde 20 porciones: carne 2.000 g a $6.000 el kilo; verduras 2.000 g a $1.200 el kilo; aceite 100 g a $3.000 el kilo. "
     "Versión vegetariana: legumbres 1.600 g a $2.500 el kilo, en lugar de la carne; verduras 2.400 g; aceite 100 g (agrega soya como alérgeno declarado de ejemplo). "
     "Prueba sensorial de la versión vegetariana: 8 personas, escala de 1 a 5; puntajes 4, 3, 5, 4, 3, 4, 4 y 5. Criterio de ejemplo: se adopta si el promedio es al menos 4 y el costo por porción no supera el de la versión base.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de variación en papel: recalcular costo y alérgenos, evaluar la prueba sensorial y decidir si la versión se adopta.",
    prior=["Conozco el registro de versiones y la prueba sensorial.", "Sé costear una receta.", "Sé calcular promedios con números enteros."],
    explain=[
        "Para analizar una variación se comparan la versión base y la nueva en tres aspectos: el costo por porción, los alérgenos y el resultado de la prueba sensorial. El costo de cada ingrediente se calcula multiplicando los gramos por el precio por kilo y dividiendo por 1.000; la suma es el costo total y, dividida por las porciones, el costo por porción.",
        "El promedio de una prueba sensorial es la suma de los puntajes dividida por el número de personas. Se compara con el criterio de aceptación. Si la variación agrega un alérgeno, se declara en el rótulo y en la carta, y se informa a quienes lo necesiten.",
        "La decisión final es de la jefa de cocina y se registra con su justificación. Una variación puede ser más barata y gustar, y aun así rechazarse si no cumple los criterios acordados. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("promedio", "suma de los puntajes dividida por el número de personas"), ("criterio de aceptación", "condiciones que debe cumplir una versión para adoptarse"), ("costo por porción", "costo total dividido por las porciones"), ("justificación", "razones de una decisión con datos")],
    worked=[
        ("Calcular un promedio", "Cuatro personas dan puntajes de ejemplo 3, 4, 5 y 4. ¿Cuál es el promedio?", ["Se suman: 3 + 4 + 5 + 4 = 16.", "16 ÷ 4 = 4."], "4"),
        ("Comparar costos", "La versión A de ejemplo cuesta $400 por porción y la B cuesta $350. ¿Cuál es más barata?", ["Se comparan los dos costos.", "350 es menor que 400."], "La B"),
    ],
    mistakes=[("Decidir por el costo sin considerar la prueba sensorial.", "Una versión barata que no gusta no se vende.", "Considera costo, alérgenos y aceptación."),
              ("Calcular el promedio dividiendo por el máximo posible en vez de por las personas.", "El resultado es incorrecto.", "Divide la suma por el número de personas.")],
    T=[
        ("=", "{F} ¿Cuánto cuesta la carne de la versión base?", "2000*6000//1000", "Se multiplican los gramos por el precio por kilo y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan las verduras de la versión base?", "2000*1200//1000", "Se multiplican los gramos por el precio por kilo y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la versión base (carne, verduras y aceite)?", "2000*6000//1000+2000*1200//1000+100*3000//1000", "Se suman los costos de los tres ingredientes.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por porción de la versión base?", "14700//20", "Se divide el costo total por las porciones.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la versión vegetariana?", "1600*2500//1000+2400*1200//1000+100*3000//1000", "Se suman los costos de legumbres, verduras y aceite.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por porción de la versión vegetariana?", "7180//20", "Se divide el costo total por las porciones.", " pesos"),
        ("=", "{F} ¿Cuántos pesos menos cuesta cada porción de la versión vegetariana respecto de la base?", "735-359", "Al costo de la versión base se le resta el de la vegetariana.", " pesos"),
        ("=", "{F} ¿Cuál es la suma de los puntajes de la prueba sensorial de la versión vegetariana?", "4+3+5+4+3+4+4+5", "Se suman los ocho puntajes.", " puntos"),
        ("=", "{F} ¿Cuál es el promedio de la prueba sensorial de la versión vegetariana?", "32//8", "Se divide la suma de los puntajes por el número de personas.", ""),
        ("abc", "{F} Con el criterio de la ficha, ¿se adopta la versión vegetariana?", "Sí: el promedio es 4 y su costo por porción es menor que el de la base", "No: el costo es mayor que el de la base", "No: el promedio es menor que 4", "Cumple las dos condiciones del criterio."),
        ("abc", "{F} ¿Qué debe hacerse con el alérgeno que agrega la versión vegetariana?", "Declararlo en el rótulo y en la carta", "No informarlo, porque la versión es más sana", "Informarlo solo a quien pregunte", "El alérgeno nuevo debe informarse siempre."),
        ("abc", "{F} Un compañero dice que la versión vegetariana debe ofrecerse porque cuesta menos, sin importar la prueba. ¿Qué respuesta es correcta?", "La decisión considera costo, alérgenos y aceptación juntos", "Tiene razón, el costo es lo único que importa", "Solo importa que sea vegetariana", "El criterio exige cumplir varias condiciones y no una sola."),
        ("=", "{F} Si se producen 3 veces la receta vegetariana, ¿cuántos gramos de legumbres se necesitan?", "1600*3", "Se multiplica la cantidad de legumbres por 3.", " g"),
    ],
    ctx=("abc", "{F} La jefa duda porque la versión vegetariana usa soya como alérgeno declarado y un cliente alérgico a la soya quiere una opción. ¿Qué debe hacer?", "Informar con claridad el alérgeno, no ofrecerle esa versión y buscar otra opción sin soya", "Ofrecerle la versión de todas formas", "Ocultar la soya para no asustarlo", "La información veraz permite al cliente evitar el alérgeno."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el promedio de una prueba sensorial?", "Suma de puntajes dividida por el número de personas", "Resume los puntajes en un solo valor."),
        ("¿Qué se compara en el análisis de una variación?", "Costo, alérgenos y aceptación sensorial", "Los tres aspectos influyen en la decisión."),
        ("¿Quién decide si una versión se adopta?", "La jefa de cocina", "Responde por la calidad y por la información."),
    ],
    op=("Caso de ejemplo. Versión base «Cazuela de ave de ejemplo», 10 porciones, costo por porción de $900. Versión «con porción pequeña»: la misma preparación se reparte en 20 porciones más pequeñas, con el mismo costo total. Prueba sensorial de 5 personas con puntajes 5, 4, 4, 3 y 4. Criterio: se adopta si el promedio es al menos 4. "
        "Calcula el costo total, el costo por porción pequeña, el promedio y decide si se adopta.",
        "Costo total: 900 × 10 = 9.000. Costo por porción pequeña: 9.000 ÷ 20 = 450. Promedio: (5 + 4 + 4 + 3 + 4) ÷ 5 = 20 ÷ 5 = 4. Cumple el criterio de al menos 4, por lo que se adopta.",
        ["calcula 9.000 y 450", "calcula el promedio 4", "decide con el criterio"],
        ["hoja con cálculos y decisión"],
        ["dividir el promedio por 4", "usar 10 porciones en vez de 20", "no justificar"],
        "Pregunta: «¿cuántos puntos suman los cinco puntajes?». Debe responder 20."),
    reinforce="Inventa una versión base y una variación con costos y una prueba de 6 personas, y decide con un criterio.",
    extend="Explica por qué una versión más barata puede rechazarse si la gente no la acepta.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (comparación de dos variaciones, de ejemplo, inventada). Una cocina prueba dos variaciones, A y B, de una salsa de verduras con 10 personas, escala de 1 a 5. Variación A: suma 38; costo por porción $320. Variación B: suma 44; costo por porción $380. "
     "Criterio de ejemplo: se adopta si obtiene al menos 80 % del puntaje máximo y su costo por porción no supera $400; si más de una cumple, se elige la de mayor porcentaje. Demanda diversa: el 30 % de los clientes pide una opción baja en sal.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: comparar variaciones con porcentajes y costos, y decidir cuál se adopta.",
    prior=["Sé calcular porcentajes del máximo.", "Conozco el costo por porción.", "Conozco el registro de versiones."],
    explain=[
        "Para elegir entre dos variaciones se aplica un criterio con condiciones medibles. En la prueba sensorial, el porcentaje del máximo se calcula con la suma de puntajes multiplicada por 100 y dividida por el máximo posible, que es el número de personas por 5. Además se comparan los costos con un límite.",
        "Si más de una variación cumple el criterio, se elige la que obtiene el mayor porcentaje. Si ninguna lo cumple, se mejora la receta o se mantiene la versión base. La decisión se registra con sus datos y la jefa de cocina la aprueba.",
        "Una demanda diversa se atiende ofreciendo versiones; por ejemplo, el porcentaje de clientes que pide una opción baja en sal indica cuántas porciones preparar. Todo es un ejercicio en papel con datos de ejemplo." + LIM,
    ],
    vocab=[("porcentaje del máximo", "suma de puntajes por 100, dividida por el máximo posible"), ("límite de costo", "valor máximo permitido de costo por porción"), ("condición", "requisito que debe cumplirse para adoptar una versión"), ("trazabilidad", "posibilidad de seguir el historial de una versión")],
    worked=[
        ("Calcular el porcentaje del máximo", "En una prueba de 5 personas (máximo 25), una variación suma 20. ¿Qué porcentaje del máximo obtiene?", ["Se multiplica la suma por 100 y se divide por 25.", "20 × 100 ÷ 25 = 80."], "80 %"),
        ("Aplicar un límite", "Una variación cuesta $350 por porción y el límite es $300. ¿Cumple?", ["Se compara el costo con el límite.", "350 es mayor que 300."], "No cumple"),
    ],
    mistakes=[("Elegir la variación más barata sin revisar la prueba sensorial.", "Puede no cumplir el porcentaje mínimo de aceptación.", "Aplica todas las condiciones del criterio."),
              ("Cambiar el criterio después de ver los resultados.", "Se pierde objetividad y confianza.", "Define el criterio antes de la prueba y aplícalo igual a todas.")],
    T=[
        ("=", "{F} ¿Cuál es el puntaje máximo posible en la prueba?", "10*5", "Se multiplican las personas por el puntaje más alto.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la variación A?", "38*100//50", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la variación B?", "44*100//50", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("abc", "{F} ¿Qué variación cumple la condición de al menos 80 % del máximo?", "Solo la B", "Solo la A", "Ambas", "A obtiene 76 % y B obtiene 88 %."),
        ("abc", "{F} ¿Cumple la variación B el límite de costo?", "Sí, porque $380 no supera $400", "No, porque $380 supera $320", "No, porque $380 es mayor que $300", "El límite de la ficha es $400."),
        ("abc", "{F} ¿Qué variación se adopta con el criterio de la ficha?", "La B, porque cumple las dos condiciones", "La A, porque es más barata", "Ninguna, porque cuestan distinto", "Solo B cumple tanto el porcentaje como el límite."),
        ("=", "{F} ¿Cuántos pesos más cuesta cada porción de B respecto de A?", "380-320", "Al costo de B se le resta el costo de A.", " pesos"),
        ("=", "{F} Si se producen 200 porciones y el 30 % es la versión baja en sal, ¿cuántas porciones son?", "200*30//100", "Se calcula el 30 % del total de porciones.", " porciones"),
        ("=", "{F} ¿Cuánto cuesta producir 200 porciones de la variación B?", "380*200", "Se multiplica el costo por porción por las porciones.", " pesos"),
        ("abc", "{F} Un compañero propone cambiar el criterio a «al menos 70 %» para que la A se adopte. ¿Qué observación corresponde?", "El criterio se define antes de la prueba; cambiarlo después quita objetividad", "Es válido, porque así se aprovecha la A", "Es válido si la jefa no está", "Cambiar el criterio después de ver los resultados vuelve la decisión arbitraria."),
        ("abc", "{F} Si ninguna variación hubiera cumplido el criterio, ¿qué corresponde?", "Mejorar la receta o mantener la versión base", "Adoptar la que más se acerque", "Ofrecer ambas sin registro", "Sin cumplir el criterio, no se adopta una versión."),
        ("=", "{F} Si el costo de B subiera a $410 por porción, ¿cuántos pesos excedería el límite de $400?", "410-400", "Al costo se le resta el límite.", " pesos"),
        ("abc", "{F} Aunque B cumple el criterio, un cliente informa una alergia que puede estar relacionada con un ingrediente nuevo de B. ¿Qué corresponde?", "Revisar los alérgenos declarados de B y ofrecer una opción segura según la ficha", "Servir B igualmente", "Ocultar el ingrediente nuevo", "La información sobre alérgenos prevalece sobre el resultado de la prueba."),
    ],
    ctx=("abc", "{F} La jefa debe registrar la decisión. ¿Qué datos debe incluir?", "Los puntajes, los costos, el criterio aplicado, la versión elegida y su aprobación", "Solo el nombre de la versión elegida", "Solo el costo de la versión elegida", "Un registro completo permite justificar y repetir la decisión."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el porcentaje del máximo?", "Suma por 100, dividida por el máximo posible", "Permite comparar pruebas de distinto tamaño."),
        ("¿Qué se hace si más de una variación cumple el criterio?", "Se elige la de mayor porcentaje", "Es la regla de desempate de la ficha."),
        ("¿Cuándo se define el criterio de aceptación?", "Antes de la prueba", "Así se mantiene la objetividad de la decisión."),
    ],
    op=("Variaciones C y D de una crema de verduras de ejemplo, probadas por 8 personas con escala de 1 a 5. C: suma 30, costo por porción $410. D: suma 34, costo por porción $360. Criterio de ejemplo: al menos 80 % del máximo y costo por porción de hasta $400. "
        "Calcula el máximo y el porcentaje de cada una, di si cumplen el límite de costo, decide cuál se adopta y qué registrarías.",
        "Máximo: 8 × 5 = 40. C: 30 × 100 ÷ 40 = 75 %. D: 34 × 100 ÷ 40 = 85 %. C cuesta $410, que supera $400. D cumple porcentaje y costo, por lo que se adopta. Se registran los puntajes, los costos, el criterio, la versión elegida y la aprobación de la jefa.",
        ["calcula 40, 75 % y 85 %", "compara costos con el límite", "decide y nombra los datos a registrar"],
        ["hoja con cálculos, decisión y registro"],
        ["usar 5 como máximo", "elegir C por la suma", "no registrar la decisión"],
        "Pregunta: «¿cuál es el máximo con 8 personas?». Debe responder 40."),
    reinforce="Inventa dos variaciones con suma y costo y decide cuál se adopta con un criterio escrito antes.",
    extend="Explica por qué definir el criterio antes de la prueba hace más justa la decisión.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (servicios de ejemplo, inventados). Carta: lista de preparaciones disponibles, con sus precios, de la que cada cliente elige. Menú del día: conjunto de preparaciones (entrada, plato de fondo y postre) a un precio fijo. "
     "Los establecimientos de consumo frecuente o masivo, como un casino de empresa, un colegio o un comedor institucional, atienden a muchas personas cada día y usan un ciclo de menús, es decir, un conjunto de menús que se repite cada cierto número de semanas (de ejemplo, 4 semanas). "
     "Factores para elaborar un menú: la estación del año, el tipo de cliente, los requerimientos nutricionales y la disponibilidad de insumos. Norma: rotulado de alérgenos y estándares de higiene (autoridad sanitaria).")
build(
    O5, 1, F,
    use="Aprenderé a situar la elaboración de cartas y menús: qué los distingue, qué es un ciclo de menús y qué factores se consideran en servicios de consumo frecuente o masivo.",
    prior=["Conozco la receta estándar y el costeo.", "Conozco el rotulado de alérgenos.", "Sé multiplicar."],
    explain=[
        "En Gastronomía, una carta es la lista de preparaciones que ofrece un servicio, con sus precios, y cada cliente elige lo que quiere. Un menú del día es un conjunto de preparaciones, por ejemplo entrada, plato de fondo y postre, a un precio fijo. En servicios de consumo frecuente o masivo, como casinos o colegios, es habitual usar menús fijos organizados en un ciclo de menús que se repite cada cierto número de semanas.",
        "Para elaborar un menú se consideran cuatro factores: la estación del año, porque los productos de temporada suelen ser más abundantes y económicos; el tipo de cliente, como estudiantes, trabajadores o pacientes; los requerimientos nutricionales, que orientan sobre una alimentación saludable y sobre los que aconseja la nutricionista (profesional de la nutrición), y la disponibilidad de insumos, es decir, qué se puede conseguir de forma segura y a tiempo.",
        "Todo menú debe rotular los alérgenos y cumplir las normas de higiene que fiscaliza la autoridad sanitaria. Este cuaderno trabaja en papel y no describe cómo elaborar los platos. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("carta", "lista de preparaciones con precios, de la que el cliente elige"), ("menú del día", "conjunto de preparaciones a precio fijo"), ("ciclo de menús", "conjunto de menús que se repite cada cierto número de semanas"), ("producto de temporada", "producto que se cosecha o abunda en cierta estación"), ("requerimiento nutricional", "necesidad de nutrientes de un grupo de personas")],
    worked=[
        ("Distinguir carta y menú", "Un restaurante de ejemplo ofrece entrada, fondo y postre a $5.000 en conjunto. ¿Es carta o menú del día?", ["Es un conjunto a un precio fijo.", "Eso corresponde a un menú del día."], "Un menú del día"),
        ("Contar menús de un ciclo", "Un ciclo de ejemplo tiene 3 semanas de 5 días, con un menú distinto cada día. ¿Cuántos menús tiene el ciclo?", ["Se multiplican las semanas por los días.", "3 × 5 = 15."], "15 menús"),
    ],
    mistakes=[("Elaborar el menú solo con lo que gusta a la jefa de cocina.", "El menú debe responder al tipo de cliente y a sus requerimientos, no a una preferencia personal.", "Considera los cuatro factores: estación, cliente, nutrición e insumos."),
              ("Planificar un plato con un producto que no se puede conseguir con seguridad a tiempo.", "Se rompe el menú el día del servicio.", "Verifica la disponibilidad de insumos antes de fijar el menú.")],
    T=[
        ("abc", "En Gastronomía: ¿qué diferencia hay entre una carta y un menú del día?", "En la carta el cliente elige entre varias preparaciones con precios; el menú del día es un conjunto a precio fijo", "La carta solo tiene postres y el menú del día solo tiene fondos", "Son lo mismo con distinto nombre", "La carta ofrece opciones a elegir; el menú del día agrupa preparaciones a un precio fijo."),
        ("abc", "{F} ¿Qué es un ciclo de menús?", "Un conjunto de menús que se repite cada cierto número de semanas", "La lista de proveedores del casino", "La receta de un plato de fondo", "El ciclo permite variar los menús y organizar las compras."),
        ("abc", "{F} ¿Cuál de estos es un factor para elaborar un menú, según la ficha?", "La disponibilidad de insumos", "La cantidad de mesas del comedor", "El nombre del proveedor", "La ficha enumera estación, tipo de cliente, requerimientos nutricionales y disponibilidad de insumos."),
        ("=", "{F} Un ciclo de 4 semanas de 5 días, con un menú distinto cada día, ¿cuántos menús tiene?", "4*5", "Se multiplican las semanas por los días de cada semana.", " menús"),
        ("abc", "En Gastronomía: ¿qué ventaja suele tener un producto de temporada?", "Suele estar más disponible y ser más económico", "Siempre es más caro", "No requiere medidas de higiene", "En su temporada, la oferta aumenta y el precio suele bajar."),
        ("abc", "{F} Un hospital de ejemplo debe ofrecer menús para personas con distintos requerimientos nutricionales. ¿Con quién conviene diseñarlos?", "Con la nutricionista, que orienta sobre esos requerimientos", "Solo con el proveedor de alimentos", "Con cada paciente por separado, sin registro", "La nutricionista orienta sobre los requerimientos nutricionales."),
        ("=", "Un casino de ejemplo atiende 300 comensales por día durante 5 días a la semana. ¿Cuántos almuerzos sirve en una semana?", "300*5", "Se multiplican los comensales diarios por los días.", " almuerzos"),
        ("abc", "{F} Un menú tiene sopa de zapallo, zapallo en el plato de fondo y budín de zapallo de postre. ¿Qué problema tiene?", "Repite el mismo ingrediente y reduce la variedad", "Es demasiado caro por ser de temporada", "Necesita un ciclo de menús más largo", "Un menú equilibrado varía los ingredientes principales."),
        ("abc", "{F} Un casino quiere ofrecer un producto muy caro y difícil de conseguir todos los días. ¿Qué factor lo limita?", "La disponibilidad de insumos y el costo", "La estación del año solamente", "El color del producto", "La disponibilidad y el costo hacen inviable un producto así en un servicio masivo."),
        ("=", "Una carta de ejemplo tiene 12 preparaciones y el 25 % son vegetarianas. ¿Cuántas preparaciones vegetarianas hay?", "12*25//100", "Se calcula el 25 % del total de preparaciones.", " preparaciones"),
        ("abc", "{F} Un colegio de ejemplo cambia su menú de verano al de invierno. ¿Por qué conviene hacerlo?", "Porque cambia la estación, la oferta de productos y las necesidades de las personas", "Porque la norma lo exige cada mes", "Porque los estudiantes prefieren menús más caros", "La estación del año es uno de los factores que orientan el menú."),
        ("abc", "{F} ¿Qué debe indicar todo menú, además de las preparaciones?", "Los alérgenos de cada preparación", "El nombre del cocinero", "La marca del proveedor", "El rotulado de alérgenos es una obligación de la norma sanitaria."),
        ("abc", "{F} Un casino repite exactamente el mismo menú todos los días porque «es más fácil». ¿Qué observación corresponde?", "Un ciclo de menús aporta variedad y mejor alimentación sin complicar la organización", "Es lo más adecuado, porque se compra siempre igual", "Es obligatorio por norma", "El ciclo de menús permite variar y planificar a la vez."),
    ],
    ctx=("abc", "{F} Un colegio solicita un ciclo de menús para el invierno, con una opción vegetariana diaria. ¿Qué factores debe considerar la jefa de cocina?", "Estación, tipo de cliente, requerimientos nutricionales y disponibilidad de insumos", "Solo el costo", "Solo los gustos de los cocineros", "Los cuatro factores orientan el diseño del ciclo de menús."),
    sc=[
        ("En Gastronomía: ¿qué es un menú del día?", "Un conjunto de preparaciones a precio fijo", "Se distingue de la carta, donde el cliente elige."),
        ("¿Qué es un ciclo de menús?", "Menús que se repiten cada cierto número de semanas", "Permite variar y organizar las compras."),
        ("¿Qué factores se consideran?", "Estación, cliente, nutrición e insumos", "Son los cuatro de la ficha."),
    ],
    op=("Un comedor institucional de ejemplo atiende a 150 trabajadores por día de lunes a viernes, en otoño. Desea diseñar un ciclo de 2 semanas con un menú distinto cada día y una opción vegetariana diaria. "
        "Calcula cuántos menús tiene el ciclo y cuántos almuerzos se sirven por semana, y escribe los cuatro factores que consideraría, con un dato de ejemplo para cada uno.",
        "Menús del ciclo: 2 × 5 = 10. Almuerzos por semana: 150 × 5 = 750. Factores: estación (otoño, usar productos de temporada); tipo de cliente (trabajadores); requerimientos nutricionales (alimentación saludable y opción vegetariana); disponibilidad de insumos (verificar proveedores).",
        ["calcula 10 menús y 750 almuerzos", "nombra los cuatro factores", "da un dato para cada factor"],
        ["hoja con cálculos y cuatro factores"],
        ["multiplicar por 150 en vez de 5", "olvidar un factor", "no considerar la opción vegetariana"],
        "Pregunta: «¿cuántos días tiene el ciclo?». Debe responder 10."),
    reinforce="Escribe un ciclo de tres menús para un colegio inventado, con entrada, fondo y postre.",
    extend="Explica por qué un servicio masivo necesita un ciclo de menús y no uno nuevo cada día.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (menú semanal y documentos de ejemplo). Estructura del menú: entrada, plato de fondo y postre. Equilibrio: variedad de colores y de grupos de alimentos; no repetir el mismo ingrediente principal en un mismo menú ni repetir el mismo plato de fondo en una semana (excepto las legumbres, que pueden aparecer hasta 2 veces). "
     "Ficha de menú: nombre del plato, ingredientes principales, alérgenos, costo por porción y precio. Costo objetivo de ejemplo: 40 % del precio de venta. Roles: la nutricionista revisa el equilibrio; la jefa de cocina diseña; la administradora fija el precio. "
     "Menú del lunes (de ejemplo): ensalada de temporada, guiso de legumbres y fruta de temporada.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario y los documentos de un menú: estructura, equilibrio, ficha de menú, costo objetivo y los roles que lo diseñan y revisan.",
    prior=["Conozco la carta, el menú y el ciclo de menús.", "Sé calcular el precio de venta con el costo objetivo.", "Conozco los factores del menú."],
    explain=[
        "Un menú se organiza en entrada, plato de fondo y postre. El plato de fondo es la preparación principal, que suele llevar una guarnición. Un menú equilibrado combina distintos colores y grupos de alimentos, evita repetir un mismo ingrediente principal en el mismo menú y no repite el mismo plato de fondo en una semana, salvo las legumbres, que pueden aparecer dos veces.",
        "La ficha de menú reúne el nombre de cada plato, sus ingredientes principales, los alérgenos, el costo por porción y el precio. El costo objetivo indica qué parte del precio se destina a ingredientes; con él, el precio de venta se calcula multiplicando el costo por 100 y dividiendo por el porcentaje.",
        "En el diseño participan varios roles: la nutricionista revisa que el menú sea equilibrado, la jefa de cocina lo diseña y comprueba que sea posible producirlo, y la administradora fija el precio. Los datos de esta ficha son de ejemplo. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("plato de fondo", "preparación principal del menú"), ("guarnición", "acompañamiento del plato de fondo"), ("menú equilibrado", "menú con variedad de colores y grupos de alimentos"), ("ficha de menú", "documento con platos, ingredientes, alérgenos, costo y precio"), ("legumbres", "alimentos como porotos, lentejas y garbanzos")],
    worked=[
        ("Calcular el precio de un menú", "Un menú de ejemplo cuesta $1.200 en ingredientes y el costo objetivo es 40 %. ¿Cuál es su precio de venta?", ["Se multiplica el costo por 100 y se divide por el porcentaje.", "1.200 × 100 ÷ 40 = 3.000."], "$3.000"),
        ("Detectar una repetición", "Un menú de ejemplo ofrece sopa de choclo, pastel de choclo y gelatina. ¿Qué ingrediente principal se repite en las dos primeras preparaciones?", ["Se observa el ingrediente principal.", "Se repite el choclo."], "El choclo"),
    ],
    mistakes=[("Fijar el precio del menú sin revisar su costo por porción.", "Puede quedar sin margen o por debajo del costo.", "Calcula el costo y aplica el costo objetivo antes de fijar el precio."),
              ("Diseñar el menú sin consultar a la nutricionista cuando existe.", "Puede no cumplir los requerimientos nutricionales del grupo.", "Haz revisar el equilibrio por la nutricionista.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es el plato de fondo?", "La preparación principal del menú", "El postre del menú", "La bebida que acompaña", "El plato de fondo es la preparación principal, entre la entrada y el postre."),
        ("abc", "{F} ¿Qué incluye el menú del lunes?", "Ensalada de temporada, guiso de legumbres y fruta de temporada", "Sopa de verduras, pollo con arroz y gelatina", "Solo un plato de fondo", "La ficha detalla ese menú de ejemplo."),
        ("abc", "{F} ¿Qué rol revisa que el menú sea equilibrado?", "La nutricionista", "La administradora", "El proveedor", "La ficha asigna la revisión del equilibrio a la nutricionista."),
        ("abc", "{F} ¿Qué rol fija el precio del menú?", "La administradora", "La nutricionista", "La jefa de cocina", "La ficha asigna el precio a la administradora."),
        ("=", "{F} Un menú cuesta $1.550 en ingredientes. Con el costo objetivo de 40 %, ¿cuál es su precio de venta?", "1550*100//40", "Se multiplica el costo por 100 y se divide por el porcentaje objetivo.", " pesos"),
        ("abc", "{F} Según la ficha, ¿cuántas veces puede aparecer el guiso de legumbres en una semana?", "Dos veces", "Ninguna vez", "Cinco veces", "La excepción de las legumbres permite dos apariciones en la semana."),
        ("abc", "{F} Un menú propone arroz de entrada, arroz en el fondo y arroz con leche de postre. ¿Qué principio de equilibrio incumple?", "Repite el mismo ingrediente principal en un mismo menú", "Usa legumbres más de dos veces", "Falta la nutricionista", "El menú repite el arroz en las tres preparaciones."),
        ("abc", "{F} ¿Qué datos incluye la ficha de menú?", "Plato, ingredientes principales, alérgenos, costo por porción y precio", "Solo el nombre del plato", "Solo el costo y el proveedor", "La ficha enumera esos cinco datos."),
        ("=", "{F} Un menú tiene costos por porción de $300, $1.300 y $250. ¿Cuál es su costo total?", "300+1300+250", "Se suman los costos de la entrada, el fondo y el postre.", " pesos"),
        ("=", "{F} Con el costo total anterior y el costo objetivo, ¿cuál es el precio de venta de ese menú?", "1850*100//40", "Se multiplica el costo total por 100 y se divide por el porcentaje objetivo.", " pesos"),
        ("abc", "{F} Una jefa propone repetir el pollo con arroz de fondo tres días en la misma semana para ahorrar. ¿Qué observación corresponde?", "Incumple el equilibrio: solo las legumbres pueden repetirse, y hasta dos veces", "Es válido si el costo baja", "Es válido si la nutricionista no está", "La ficha establece que solo las legumbres pueden repetirse en la semana."),
        ("abc", "Un menú ofrece ensalada de lechuga, tomate y zanahoria, un fondo con arroz blanco y un postre de manzana. ¿Qué característica de equilibrio muestra?", "Variedad de colores y de grupos de alimentos", "Repetición de ingredientes", "Falta de verduras", "Combina verduras, un cereal y una fruta, de distintos colores."),
        ("abc", "{F} El menú nuevo no tiene rotulados los alérgenos. ¿Qué corresponde?", "Completar el rótulo de alérgenos antes de ofrecerlo", "Ofrecerlo igual y rotular después", "Informar solo si alguien pregunta", "Los alérgenos se declaran en la ficha de menú y en el rótulo antes del servicio."),
    ],
    ctx=("abc", "{F} La administradora quiere fijar el precio de un menú sin conocer su costo por porción, «por un precio parecido al de otro casino». ¿Qué debe hacer la jefa?", "Entregar el costo por porción de cada plato para que el precio respete el costo objetivo", "Aceptar el precio parecido", "Subir el costo de los ingredientes", "El precio debe basarse en el costo real y en el costo objetivo."),
    sc=[
        ("En Gastronomía: ¿qué rol revisa el equilibrio nutricional del menú?", "La nutricionista", "Tiene la formación para orientar sobre la nutrición."),
        ("¿Qué legumbres o platos pueden repetirse en la semana?", "Las legumbres, hasta dos veces", "Es la excepción de la ficha."),
        ("¿Qué incluye la ficha de menú?", "Platos, alérgenos, costo y precio", "Reúne todos los datos necesarios para decidir."),
    ],
    op=("Menú de ejemplo del martes: entrada, sopa de verduras ($350); fondo, pollo con arroz ($1.300); postre, gelatina ($250). Costo objetivo: 40 %. "
        "Calcula el costo total y el precio de venta del menú; di si hay algún ingrediente principal repetido y qué rol del menú revisaría el equilibrio de este menú.",
        "Costo total: 350 + 1.300 + 250 = 1.900. Precio de venta: 1.900 × 100 ÷ 40 = 4.750. No hay ingrediente principal repetido: verduras, pollo con arroz y gelatina. El equilibrio lo revisa la nutricionista.",
        ["calcula 1.900 y 4.750", "revisa la repetición de ingredientes", "nombra el rol de la nutricionista"],
        ["hoja con cálculos y respuestas"],
        ["no sumar el postre", "dividir por 100 en vez de 40", "olvidar al rol"],
        "Pregunta: «¿cuánto suma 350 + 1.300 + 250?». Debe responder 1.900."),
    reinforce="Escribe un menú de ejemplo de tres platos, inventa un costo para cada uno y calcula el precio con un costo objetivo.",
    extend="Explica por qué repetir un ingrediente principal en todo el menú reduce la calidad nutricional.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Casino de empresa con 300 almuerzos por día durante 5 días, en verano de ejemplo (ensalada de temporada y fruta de temporada son abundantes y económicas). "
     "Costos por porción (de ejemplo): entradas, ensalada de temporada $300 y sopa de verduras $350; fondos, guiso de legumbres $900, pollo con arroz $1.300, tortilla de verduras con arroz $800 y pasta con salsa de tomate $700; postres, fruta de temporada $350 y gelatina $250. "
     "Reglas: costo máximo por menú de $1.900; el guiso de legumbres se ofrece exactamente 2 días y los otros fondos 1 día cada uno; cada día debe haber una opción vegetariana (guiso de legumbres, tortilla de verduras con arroz o pasta con salsa de tomate).")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de menú en papel: combinar platos, comprobar un límite de costo y revisar las reglas de equilibrio y de opciones especiales.",
    prior=["Conozco la estructura y el equilibrio de un menú.", "Sé sumar costos y comparar con un límite.", "Conozco el costo objetivo."],
    explain=[
        "Armar un menú semanal es combinar entradas, fondos y postres que cumplan reglas: un costo máximo por menú, una distribución de los platos de fondo en la semana y opciones para distintos clientes, como una opción vegetariana. Se empieza fijando los platos de fondo, que son los más costosos, y luego se eligen entradas y postres que permitan respetar el límite de costo.",
        "Para comprobar un menú se suma el costo de sus tres preparaciones y se compara con el límite. Si lo supera, se cambia la entrada o el postre por una opción más económica, o se rediseña el menú. También se verifica que no se repitan ingredientes principales y que cada día cumpla las reglas.",
        "En servicios masivos, la estación ayuda a controlar el costo: los productos de temporada suelen ser más abundantes y económicos. Los costos de esta ficha son de ejemplo y las decisiones finales las toma la jefa de cocina con la administración y la nutricionista." + LIM,
    ],
    vocab=[("límite de costo", "costo máximo permitido por menú"), ("opción vegetariana", "preparación sin carne ni pescado"), ("combinación", "conjunto elegido de entrada, fondo y postre"), ("distribución", "reparto de los platos de fondo en la semana")],
    worked=[
        ("Comprobar un menú", "Un menú de ejemplo tiene entrada de $400, fondo de $1.000 y postre de $300, con límite de $1.800. ¿Lo cumple?", ["Se suman los costos: 400 + 1.000 + 300 = 1.700.", "1.700 es menor que 1.800."], "Sí, cumple"),
        ("Reducir un costo", "Un menú de ejemplo cuesta $2.000 y el límite es $1.800. Si se cambia el postre de $450 por uno de $200, ¿cumple?", ["El ahorro es 450 − 200 = 250.", "2.000 − 250 = 1.750, menor que 1.800."], "Sí, cumple"),
    ],
    mistakes=[("Elegir primero las entradas y los postres y dejar el fondo para el final.", "El fondo es lo más caro; puede quedar sin presupuesto para el límite.", "Fija primero los fondos y luego ajusta entradas y postres."),
              ("Ofrecer la opción vegetariana solo un día porque «hay pocas personas».", "La regla del caso exige una opción vegetariana cada día.", "Verifica las reglas de cada día del menú.")],
    T=[
        ("=", "{F} Un menú con ensalada de temporada, guiso de legumbres y fruta de temporada, ¿cuánto cuesta?", "300+900+350", "Se suman los costos de la entrada, el fondo y el postre.", " pesos"),
        ("abc", "{F} ¿Cumple ese menú el costo máximo por menú?", "Sí, porque 1.550 no supera $1.900", "No, porque supera $1.900", "No, porque la fruta es más cara que la gelatina", "El costo total de 1.550 es menor que el límite."),
        ("=", "{F} Un menú con ensalada de temporada, pollo con arroz y gelatina, ¿cuánto cuesta?", "300+1300+250", "Se suman los costos de la entrada, el fondo y el postre.", " pesos"),
        ("abc", "{F} ¿Cumple ese menú el costo máximo por menú?", "Sí, porque 1.850 no supera $1.900", "No, porque supera $1.900", "No, porque el pollo no es vegetariano", "1.850 está por debajo del límite de 1.900."),
        ("abc", "{F} Con el pollo con arroz y la ensalada de temporada como entrada, ¿qué postre permite cumplir el límite?", "La gelatina, que deja el menú en 1.850", "La fruta de temporada, que deja el menú en 1.950", "Ninguno, porque el pollo es muy caro", "Con la fruta el menú costaría 1.950, que supera el límite."),
        ("abc", "{F} ¿Qué día no tiene que ofrecerse la opción vegetariana?", "Ninguno: debe ofrecerse cada día", "El día del pollo con arroz", "El día de la pasta", "La regla exige una opción vegetariana cada día."),
        ("abc", "{F} El día del pollo con arroz, ¿cómo puede cumplirse la regla de la opción vegetariana?", "Ofreciendo una opción vegetariana adicional, como la tortilla de verduras con arroz", "No es necesario, porque el pollo es el plato del día", "Reemplazando el pollo por pescado", "La regla exige una opción vegetariana adicional, también el día del pollo."),
        ("=", "{F} La semana tiene el guiso 2 días y los otros tres fondos 1 día cada uno. ¿Cuántos días suma la semana?", "2+1+1+1", "Se suman los días de cada plato de fondo.", " días"),
        ("=", "{F} ¿Cuántos almuerzos con guiso de legumbres se sirven en la semana, si cada día de guiso se sirven los 300?", "300*2", "Se multiplican los comensales por los dos días de guiso.", " almuerzos"),
        ("=", "{F} ¿Cuántos almuerzos se sirven en la semana?", "300*5", "Se multiplican los comensales por los cinco días.", " almuerzos"),
        ("abc", "{F} Una compañera propone ofrecer pollo con arroz dos días y no ofrecer la pasta, «para comprar menos variedad». ¿Qué observación corresponde?", "Incumple la regla: los fondos distintos del guiso se ofrecen un día cada uno", "Es válido, porque ahorra", "Es válido si la fruta es abundante", "La regla fija cuántos días se ofrece cada plato de fondo."),
        ("abc", "{F} En invierno ya no hay abundancia de la ensalada de temporada. ¿Qué debe hacerse?", "Revisar la disponibilidad y el costo de las entradas y rediseñar el menú", "Seguir con la misma ensalada sin importar el costo", "Eliminar la entrada sin informar", "Cambiar la estación cambia la disponibilidad y el costo de los productos."),
        ("=", "{F} Si el costo del pollo con arroz subiera a $1.500, ¿cuánto costaría el menú con ensalada, pollo con arroz y gelatina?", "300+1500+250", "Se suman los costos de la entrada, el fondo y el postre con el nuevo valor.", " pesos"),
    ],
    ctx=("abc", "{F} El menú con pollo con arroz subió de costo a $2.050 por un alza de precios. ¿Qué decisión es más razonable?", "Rediseñar el menú de ese día con una entrada o un postre más económicos, o cambiar el fondo, y consultar a la administración", "Mantener el menú y ofrecer menos porciones sin avisar", "Eliminar la opción vegetariana", "Hay que volver al límite de costo sin dañar el equilibrio ni engañar al cliente."),
    sc=[
        ("En Gastronomía: ¿qué se fija primero al armar un menú semanal?", "Los platos de fondo", "Son los más costosos y condicionan lo demás."),
        ("¿Cómo se comprueba el límite de costo de un menú?", "Sumando el costo de sus tres preparaciones", "El total se compara con el límite."),
        ("¿Qué opción debe ofrecerse cada día en el caso?", "Una opción vegetariana", "Es una de las reglas del caso."),
    ],
    op=("Caso de ejemplo. Un colegio pide menús de 3 días con un costo máximo de $1.600 por menú. Costos por porción de ejemplo: entradas, ensalada $250 y sopa $300; fondos, tortilla de verduras con arroz $700, pasta con salsa de tomate $650 y lentejas $800; postres, fruta $300 y gelatina $200. "
        "Arma tres menús (un fondo distinto por día), calcula el costo de cada uno, comprueba el límite y señala cuál es la opción vegetariana de cada día.",
        "Ejemplo: día 1, ensalada $250 + tortilla $700 + fruta $300 = $1.250; día 2, sopa $300 + pasta $650 + gelatina $200 = $1.150; día 3, ensalada $250 + lentejas $800 + fruta $300 = $1.350. Todos son menores que $1.600. Cada fondo del ejemplo es vegetariano, por lo que cada día cumple la regla.",
        ["arma tres menús con fondos distintos", "calcula costos que no superan $1.600", "señala la opción vegetariana de cada día"],
        ["hoja con tres menús y costos"],
        ["repetir el mismo fondo", "superar el límite", "no indicar la opción vegetariana"],
        "Pregunta: «¿cuánto suma tu menú más caro?». Si supera $1.600, cambia el postre o la entrada."),
    reinforce="Arma un menú de un día con entrada, fondo y postre de una lista de seis costos inventados y comprueba un límite.",
    extend="Explica por qué se decide primero el plato de fondo al armar un menú con límite de costo.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (menú semanal costeado, de ejemplo). Platos de fondo y costo por porción: lunes, guiso de legumbres $900; martes, pollo con arroz $1.300; miércoles, pasta con salsa de tomate $700; jueves, guiso de legumbres $900; viernes, tortilla de verduras con arroz $800. "
     "La entrada y el postre cuestan $650 en conjunto cada día. Comensales: 300 por día. Costo objetivo: 40 % del precio de venta. Metas de ejemplo: promedio de costo de los fondos de hasta $1.100 y al menos 2 días de legumbres en la semana.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: costear un menú semanal, calcular precios y verificar si cumple las metas de costo y de alimentación saludable.",
    prior=["Conozco el costo objetivo.", "Sé calcular promedios y totales.", "Conozco la estructura y el equilibrio del menú."],
    explain=[
        "Para costear un menú semanal se suma, para cada día, el costo del plato de fondo y el de la entrada y el postre; ese es el costo por comensal. El precio de venta de cada día se calcula con el costo objetivo: el costo se multiplica por 100 y se divide por el porcentaje. El costo semanal total se obtiene multiplicando la suma de los costos diarios por el número de comensales.",
        "El promedio de costo de los fondos es la suma de los costos dividida por los días. Las metas se verifican comparando: el promedio con su límite y el número de días con legumbres con el mínimo exigido. Si no se cumple una meta, se rediseña el menú.",
        "Los datos son de ejemplo. En la práctica, el menú se revisa con la nutricionista y se ajusta según los precios reales vigentes." + LIM,
    ],
    vocab=[("costo por comensal", "costo en ingredientes del menú de una persona"), ("costo semanal total", "costo por comensal de la semana por el número de comensales"), ("promedio", "suma de valores dividida por la cantidad de valores"), ("meta", "valor o condición que se espera cumplir")],
    worked=[
        ("Calcular el promedio", "Los fondos de ejemplo cuestan $600, $800 y $1.000 en tres días. ¿Cuál es el promedio?", ["Se suman: 600 + 800 + 1.000 = 2.400.", "2.400 ÷ 3 = 800."], "$800"),
        ("Calcular un costo semanal", "Un menú de ejemplo cuesta $1.500 por comensal por día, durante 5 días y para 100 comensales. ¿Cuál es el costo semanal total?", ["1.500 × 5 = 7.500 por comensal.", "7.500 × 100 = 750.000."], "$750.000"),
    ],
    mistakes=[("Calcular el costo semanal sin multiplicar por el número de comensales.", "Se subestima mucho lo que cuesta el servicio.", "Multiplica el costo por comensal por los comensales."),
              ("Calcular el promedio de los fondos dividiendo por 100 o por el total de comensales.", "El promedio se divide por el número de días, no por los comensales.", "Divide la suma de los fondos por 5.")],
    T=[
        ("=", "{F} ¿Cuál es el costo por comensal del menú del lunes?", "900+650", "Se suman el fondo y el costo de entrada y postre.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta del menú del lunes con el costo objetivo?", "1550*100//40", "Se multiplica el costo por 100 y se divide por el porcentaje objetivo.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por comensal del menú del martes?", "1300+650", "Se suman el fondo y el costo de entrada y postre.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta del menú del martes?", "1950*100//40", "Se multiplica el costo por 100 y se divide por el porcentaje objetivo.", " pesos"),
        ("=", "{F} ¿Cuánto suman los costos de los cinco platos de fondo?", "900+1300+700+900+800", "Se suman los cinco costos de los fondos.", " pesos"),
        ("=", "{F} ¿Cuál es el promedio de costo de los fondos?", "4600//5", "Se divide la suma de los fondos por el número de días.", " pesos"),
        ("abc", "{F} ¿Cumple el promedio de fondos la meta de la ficha?", "Sí, porque 920 no supera 1.100", "No, porque 920 supera 900", "No, porque 920 es menor que 1.100", "El promedio queda por debajo del límite de $1.100."),
        ("abc", "{F} ¿Cumple el menú la meta de al menos 2 días de legumbres?", "Sí, porque el guiso de legumbres está el lunes y el jueves", "No, porque solo aparece una vez", "No, porque las legumbres no aparecen", "La ficha tiene guiso de legumbres dos días."),
        ("=", "{F} ¿Cuál es el costo por comensal de toda la semana?", "4600+650*5", "Se suman los fondos de la semana y el costo de entrada y postre de los cinco días.", " pesos"),
        ("=", "{F} ¿Cuál es el costo semanal total para los 300 comensales?", "(4600+650*5)*300", "Se multiplica el costo semanal por comensal por el número de comensales.", " pesos"),
        ("=", "{F} Si el martes el pollo con arroz se reemplazara por un fondo nuevo de $700 (de ejemplo), ¿cuál sería el nuevo promedio de fondos?", "(900+700+700+900+800)//5", "Se recalculan los fondos y se divide por 5.", " pesos"),
        ("abc", "{F} Un compañero dice que el costo semanal se calcula sin multiplicar por los comensales, «porque ya está por persona». ¿Qué corrección corresponde?", "El costo por comensal debe multiplicarse por 300 para conocer el costo del servicio", "Tiene razón, el costo por persona es el costo total", "Debe dividirse por 300", "El servicio atiende a 300 personas, por lo que el costo total es mayor."),
        ("abc", "{F} Si el promedio de fondos superara $1.100, ¿qué corresponde?", "Rediseñar el menú con fondos más económicos o negociar costos", "Ignorar la meta", "Eliminar la entrada y el postre", "Una meta no cumplida obliga a revisar el menú."),
    ],
    ctx=("abc", "{F} La administradora ve que el costo semanal total es alto y propone reducir porciones sin avisar a los comensales. ¿Qué debe responder la jefa?", "Que cambiar la porción afecta la calidad y debe decidirse con la nutricionista y registrarse; mejor revisar fondos y compras", "Que lo haga de inmediato, porque ahorra", "Que reduzca solo la fruta sin informar", "Una reducción oculta de porciones afecta la nutrición y la confianza."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el costo semanal total?", "Costo por comensal de la semana por los comensales", "Muestra el costo real del servicio."),
        ("¿Cómo se calcula el promedio de los fondos?", "Suma de fondos dividida por los días", "Refleja el costo típico de cada día."),
        ("¿Qué se hace si no se cumple una meta?", "Se rediseña el menú", "El menú debe ajustarse para cumplirla."),
    ],
    op=("Menú de ejemplo de 4 días: lunes, lentejas $750; martes, tortilla de verduras con arroz $700; miércoles, pollo con arroz $1.200; jueves, lentejas $750. Entrada y postre: $600 en conjunto cada día. Comensales: 200 por día. Costo objetivo: 40 %. Metas: promedio de fondos de hasta $1.000 y al menos 2 días de legumbres. "
        "Calcula el promedio de fondos, el costo por comensal de la semana, el costo semanal total, el precio de venta del menú del miércoles y di si se cumplen las dos metas.",
        "Fondos: 750 + 700 + 1.200 + 750 = 3.400; promedio: 3.400 ÷ 4 = 850. Costo por comensal: 3.400 + 600 × 4 = 5.800. Costo total: 5.800 × 200 = 1.160.000. Miércoles: 1.200 + 600 = 1.800; precio: 1.800 × 100 ÷ 40 = 4.500. Metas: el promedio 850 no supera 1.000 y hay 2 días de lentejas: ambas se cumplen.",
        ["calcula el promedio 850", "calcula el costo semanal y el total", "calcula 4.500 y verifica las dos metas"],
        ["hoja con cálculos y verificación"],
        ["dividir por 5 en vez de 4", "no multiplicar por 200", "olvidar verificar la meta de legumbres"],
        "Pregunta: «¿cuántos días tiene el menú?». Debe responder 4."),
    reinforce="Inventa un menú de 3 días con costos y calcula promedio de fondos, costo por comensal y precio de un día.",
    extend="Explica por qué una meta de costo debe equilibrarse con una meta de alimentación saludable.",
)

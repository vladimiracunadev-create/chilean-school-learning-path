"""Ambiente y sostenibilidad 3.º y 4.º medio FG: OA 01 clases 4 y 5 (analizar evidencia y comparar soluciones de consumo sostenible). Datos de ejemplo inventados."""
from __future__ import annotations

from fg_cias_common import build

O1 = "FG-CIAS-3y4-OAC-01"

# ============================================================ OA 01, clase 4
F = ("Ficha 4 (datos de ejemplo, en unidades de impacto «u» inventadas) para servir 1.000 vasos de jugo: "
     "Caja de cartón desechable: extracción 20 u, fabricación 30 u, transporte 12 u, fin de vida 8 u. "
     "Botella de vidrio retornable (se lava y se usa muchas veces): extracción 4 u, fabricación 8 u, transporte 25 u, lavado y reposición 11 u, fin de vida 2 u. "
     "Todos los datos provienen de un solo estudio de ejemplo hecho en una sola ciudad.")
build(
    O1, 4, F,
    use="Aprenderé a analizar una tabla de impactos por etapa: encontrar puntos críticos, comparar con la misma función, probar la sensibilidad y declarar incertidumbre.",
    prior=["Sé armar un modelo de ciclo de vida con etapas.", "Sé calcular un porcentaje.", "Sé distinguir asociación de causa."],
    explain=[
        "Analizar evidencia es leer los datos con preguntas: qué etapa pesa más, cómo cambia el total si cambia un dato y qué tan seguros son los números. Una etapa que concentra gran parte del impacto es un punto crítico: ahí conviene actuar primero. Para comparar dos productos los datos deben referirse a la misma unidad funcional; si no, la comparación no es válida. En la ficha ambos productos sirven 1.000 vasos de jugo.",
        "El análisis de sensibilidad cambia un dato para ver si la conclusión se mantiene. Por ejemplo, la botella retornable gana cuando su transporte es corto, pero si la distancia de retorno crece, su transporte sube y la ventaja puede desaparecer. El punto donde dos opciones empatan se llama punto de equilibrio. Saberlo permite decir en qué condiciones cada opción es mejor, en lugar de afirmar que una gana siempre.",
        "Los datos también tienen incertidumbre: un valor puede darse con un rango, como 50 u más o menos 10 u, porque cada medición varía. Además, una asociación entre dos hechos no prueba que uno cause al otro: dos cosas pueden crecer juntas por una tercera causa. Un solo estudio en una sola ciudad no permite generalizar. La conclusión prudente dice qué muestran los datos, bajo qué condiciones y qué falta contrastar.",
    ],
    vocab=[("punto crítico", "etapa que concentra gran parte del impacto"), ("punto de equilibrio", "valor de un dato en que dos opciones tienen el mismo impacto"), ("sensibilidad", "cuánto cambia el resultado cuando cambia un dato"), ("incertidumbre", "grado en que un dato puede variar o no conocerse con exactitud"), ("asociación", "relación entre dos hechos que ocurren juntos, sin que uno cause el otro necesariamente")],
    worked=[
        ("Encontrar el punto crítico", "Un envase de ejemplo suma: extracción 6 u, fabricación 20 u, transporte 4 u, fin de vida 10 u. ¿Cuál es su punto crítico y qué porcentaje del total pesa?", ["El total es 6 + 20 + 4 + 10 = 40 u.", "La etapa mayor es la fabricación, con 20 u.", "20 de 40 es la mitad: 50 %."], "Fabricación, 50 % del total"),
        ("Sensibilidad", "Una opción de ejemplo suma 40 u y otra 45 u. Si la primera sube su transporte en 8 u, ¿cambia cuál es menor?", ["La primera pasaría a 48 u.", "48 u es mayor que 45 u.", "Ahora la menor es la otra opción."], "Sí, la conclusión se invierte"),
    ],
    mistakes=[("Afirmar que una opción «siempre» es mejor sin cambiar ningún dato.", "No se probó la sensibilidad: una distancia mayor o una etapa distinta podrían invertir el resultado.", "Cambia el dato más incierto y busca el punto de equilibrio."),
              ("Concluir que A causa B porque aparecen juntos.", "Dos hechos pueden asociarse por una tercera causa.", "Habla de asociación y pregunta qué otros factores influyen.")],
    T=[
        ('abc', 'En Ambiente y sostenibilidad, ¿qué es un punto crítico en un ciclo de vida?', 'La etapa que concentra gran parte del impacto', 'La etapa que dura más tiempo', 'La etapa que cuesta más dinero', 'El punto crítico se define por el impacto que concentra; la duración o el costo pueden ser otra cosa.'),
        ('abc', '{F} ¿Cuál es el punto crítico de la caja de cartón?', 'La fabricación, con 30 u', 'El transporte, con 12 u', 'El fin de vida, con 8 u', 'La fabricación aporta 30 u, más que cualquier otra etapa de la caja.'),
        ('=', '{F} ¿Cuántas u suma en total la caja de cartón para servir los 1.000 vasos?', '20+30+12+8', 'Se suman las cuatro etapas de la caja.', ' u'),
        ('=', '{F} ¿Cuántas u suma en total la botella retornable?', '4+8+25+11+2', 'Se suman las cinco etapas de la botella, incluyendo lavado y reposición.', ' u'),
        ('=', '{F} ¿Qué porcentaje del total de la botella retornable es el transporte?', '25*100//50', 'El total de la botella es 50 u; se divide el transporte entre el total y se multiplica por 100.', ' %'),
        ('ab', '{F} ¿Por qué se comparan ambas opciones con los datos de 1.000 vasos?', 'Porque así cumplen la misma función y la comparación es justa', 'Porque 1.000 vasos es la cantidad de jugo que cada envase contiene realmente', 'Se comparan por la misma unidad funcional; el número no indica la capacidad de un envase.'),
        ('=', '{F} ¿Cuántas u menos tiene la botella retornable que la caja?', '(20+30+12+8)-(4+8+25+11+2)', 'Se resta el total de la botella al total de la caja.', ' u'),
        ('abc', '{F} Si la distancia de retorno se duplica y el transporte de la botella pasa de 25 u a 50 u, ¿qué ocurre?', 'La botella suma 75 u y queda con más impacto que la caja, que tiene 70 u', 'La botella sigue siendo mejor, porque el vidrio se reutiliza', 'La caja sube a 95 u, porque se comparan por separado', 'Con 50 u de transporte la botella suma 4 + 8 + 50 + 11 + 2 = 75 u, más que 70 u; la ventaja depende de la distancia.'),
        ('=', '{F} Con las otras etapas de la botella iguales (4 u, 8 u, 11 u y 2 u), ¿con cuántas u de transporte la botella empata con las 70 u de la caja?', '70-(4+8+11+2)', 'Al total de la caja se le restan las etapas fijas de la botella; lo que queda es el transporte de empate.', ' u'),
        ('abc', 'En una ciudad de ejemplo, los barrios con más botellas retornables también tienen más árboles. ¿Qué conclusión es prudente?', 'Hay una asociación, pero no prueba que las botellas causen más árboles: pueden influir otros factores', 'Las botellas retornables hacen que crezcan más árboles', 'Los árboles hacen que las personas compren botellas retornables', 'Una asociación no prueba causa; otro factor, como la organización vecinal, podría explicar ambos hechos.'),
        ('abc', '{F} Un estudio de ejemplo da 50 u para la botella con un rango de 40 a 60 u, y 70 u para la caja. ¿Qué implica el rango?', 'Aun en el extremo de 60 u la botella queda bajo la caja, así que la conclusión se mantiene', 'El rango anula el estudio y no permite concluir nada', 'Solo el valor central importa y el rango se puede ignorar', 'El peor caso de la botella (60 u) sigue siendo menor que 70 u; el rango se revisa, no se descarta.'),
        ('abc', '{F} ¿Qué conclusión es la más prudente con estos datos?', 'La botella parece tener menos impacto en este caso; faltan otros estudios y ciudades antes de generalizar', 'La botella retornable es mejor siempre, porque su fabricación tiene menos impacto', 'No se puede concluir nada, porque con un solo estudio ningún dato sirve', 'Un estudio da una pista para un caso; hay que declarar su alcance y no extender a todas las situaciones.'),
        ('abc', '{F} Si la caja mejorara su reciclaje y su fin de vida bajara de 8 u a 4 u, ¿cambiaría la comparación?', 'No: la caja quedaría en 66 u, todavía mayor que las 50 u de la botella', 'Sí: la caja pasaría a tener menos impacto que la botella', 'Sí: ambas opciones quedarían empatadas', 'La caja pasaría de 70 u a 66 u; mientras siga sobre 50 u, la botella conserva su ventaja.'),
    ],
    ctx=('abc', 'Para medir el transporte, un compañero propone seguir en bicicleta a un camión de reparto por la carretera. ¿Qué haces?', 'Le dices que no es seguro, avisas a una persona adulta y propones usar distancias de mapas', 'Aceptas si todos usan casco y van juntos en grupo, con cuidado', 'Aceptas si el camión va despacio y casi no hay tráfico ese día', 'Seguir vehículos en la vía es un riesgo; las distancias se pueden obtener de mapas o de fuentes de datos.'),
    sc=[
        ('En Ambiente y sostenibilidad: ¿qué es un análisis de sensibilidad?', 'Cambiar un dato para ver si la conclusión se mantiene', 'Se prueba cuánto depende la conclusión de un dato incierto.'),
        ('abc', '¿Qué es un punto de equilibrio entre dos opciones?', 'El valor de un dato en que ambas tienen el mismo impacto', 'El momento en que una opción se agota', 'El precio en que ambas cuestan lo mismo', 'En el equilibrio las dos opciones empatan en impacto; sirve para ver en qué condiciones cada una es mejor.'),
        ('abc', 'Dos hechos aparecen juntos en los datos. ¿Qué se puede afirmar con seguridad?', 'Que están asociados, sin concluir todavía una causa', 'Que uno de los dos hechos causa al otro, porque ocurren a la vez', 'Que no tienen ninguna relación, porque no se sabe cuál causa cuál', 'Asociación no es causalidad; para decidir hace falta más evidencia.'),
    ],
    op=("Usa la {F} Escribe un análisis breve: punto crítico de cada opción, diferencia de impacto entre las dos, qué ocurre si el transporte de la botella llega a 50 u y una frase final con una limitación de los datos. Evita la palabra «siempre».",
        "Punto crítico de la caja: fabricación (30 u). De la botella: transporte (25 u). La botella tiene 20 u menos (50 u frente a 70 u). Si el transporte de la botella llega a 50 u, suma 75 u y queda peor que la caja. Limitación: los datos vienen de un solo estudio en una ciudad.",
        ["identifica puntos críticos", "calcula la diferencia", "prueba la sensibilidad", "declara una limitación"], ["dos puntos críticos", "una diferencia calculada", "una frase de limitación"], ["generalizar desde un estudio", "no probar la sensibilidad"],
        "Pregunta qué otro dato cambiarías para ver si la conclusión se mantiene."),
    reinforce="Explica con tus palabras por qué una sola fuente no basta para concluir qué envase es mejor.",
    extend="Inventa una tabla de impactos por etapa para dos productos y encuentra el punto de equilibrio de un dato.",
)

# ============================================================ OA 01, clase 5
F = ("Ficha 5 (caso de ejemplo): un liceo ficticio quiere reducir el impacto de las mochilas escolares. Opciones: "
     "(A) un taller de reparación y reutilización de mochilas; (B) comprar cada año mochilas nuevas de material reciclado; (C) una campaña de «no comprar» sin ningún apoyo. "
     "Matriz con puntajes de 1 (bajo) a 3 (alto) y pesos de cada criterio: impacto ambiental, peso 3; costo bajo, peso 2; viabilidad, peso 2; equidad (que nadie quede fuera), peso 1. "
     "Puntajes de A: impacto 3, costo 3, viabilidad 2, equidad 3. Puntajes de B: impacto 2, costo 1, viabilidad 3, equidad 1. Puntajes de C: impacto 3, costo 3, viabilidad 1, equidad 2. "
     "Datos de ejemplo: reparar una mochila cuesta $2.000 y comprar una nueva cuesta $9.000.")
build(
    O1, 5, F,
    use="Aprenderé a comparar estrategias de consumo sostenible con criterios, a ponderar una matriz y a proponer una medida con indicador de seguimiento.",
    prior=["Sé analizar una tabla de impactos.", "Sé qué es un punto de equilibrio.", "Sé que prevenir y mitigar son distintos."],
    explain=[
        "Las estrategias de consumo sostenible se ordenan con una jerarquía: primero rechazar y reducir lo que no se necesita, luego reutilizar y reparar, y al final reciclar. Esa jerarquía prioriza prevenir sobre mitigar, porque lo que no se compra no se fabrica ni se transporta. Reciclar es útil, pero llega al final del ciclo de vida y tampoco recupera todo el material. Una medida se propone con evidencia, no con intuición.",
        "Para comparar soluciones se usan criterios: cuánto reduce el impacto ambiental, cuánto cuesta, si es viable (si realmente se podrá hacer en ese lugar) y si es equitativa (si beneficia o excluye a algunas personas). Una matriz de decisión asigna un puntaje a cada opción en cada criterio y multiplica por un peso, que dice cuánto importa ese criterio. Se suma y se compara. Los pesos los eligen personas, así que se prueba qué pasa al cambiarlos.",
        "Una buena propuesta incluye un indicador de seguimiento, una medida observable que muestra si la solución funciona, por ejemplo cuántas mochilas se reparan al año. También reconoce sus límites y consulta a quienes serán afectados. Si una opción es débil en un criterio, como la viabilidad, a veces se puede mejorar con acciones concretas. Si una actividad implica herramientas, se hace con supervisión de una persona adulta.",
    ],
    vocab=[("jerarquía de residuos", "orden de prioridad: reducir, reutilizar, reparar y, al final, reciclar"), ("viabilidad", "posibilidad real de llevar a cabo una medida en ese lugar"), ("equidad", "que la medida no excluya ni perjudique a ciertas personas"), ("peso de un criterio", "número que indica cuánto importa ese criterio en la decisión"), ("indicador de seguimiento", "medida observable que muestra si una solución funciona")],
    worked=[
        ("Puntaje de una opción", "Una opción de ejemplo tiene impacto 2, costo 3 y viabilidad 3, con pesos 3, 2 y 2. ¿Cuál es su puntaje?", ["Se multiplica cada puntaje por su peso: 2 × 3 = 6, 3 × 2 = 6 y 3 × 2 = 6.", "Se suman: 6 + 6 + 6."], "18 puntos"),
        ("Elegir un indicador", "Un curso quiere reducir las compras de útiles nuevos mediante un intercambio. ¿Qué indicador de seguimiento sirve?", ["Debe ser observable y relacionado con el objetivo.", "Sirve «cantidad de útiles intercambiados cada mes»; «cuántos afiches se pegaron» mide una actividad, no el resultado."], "Útiles intercambiados cada mes"),
    ],
    mistakes=[("Elegir la opción más barata sin mirar impacto ni equidad.", "Un criterio por sí solo no basta para decidir.", "Compara todos los criterios con una matriz y revisa los pesos."),
              ("Creer que reciclar siempre es la mejor estrategia.", "Reciclar actúa al final y no evita fabricar ni transportar.", "Prioriza reducir y reutilizar; recicla lo que no se puede evitar.")],
    T=[
        ('abc', 'En Ambiente y sostenibilidad, ¿cuál orden de prioridad es el correcto?', 'Reducir y reutilizar antes que reciclar', 'Reciclar antes que reducir', 'Reciclar y luego comprar más para reemplazar', 'La jerarquía prioriza evitar el impacto antes que mitigarlo; reciclar va al final.'),
        ('=', '{F} ¿Cuántos puntos suma la opción A?', '3*3+3*2+2*2+3*1', 'Se multiplica cada puntaje por el peso de su criterio y se suman los resultados.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma la opción B?', '2*3+1*2+3*2+1*1', 'Mismo procedimiento: puntaje por peso y suma de los cuatro criterios.', ' puntos'),
        ('abc', '{F} La opción C suma 19 puntos. ¿Cuál queda en segundo lugar?', 'C, con 19 puntos', 'B, con 15 puntos', 'Empatan A y C', 'A suma 22, C suma 19 y B suma 15; el segundo lugar es C.'),
        ('abc', '{F} ¿Para qué sirve el criterio de equidad?', 'Para ver quién se beneficia y quién queda fuera, como estudiantes sin recursos', 'Para medir cuánto cuesta cada opción y cuánto se ahorraría', 'Para saber cuánto material se recicla al final de cada opción', 'La equidad se refiere a las personas; el costo y el reciclaje son otros criterios.'),
        ('=', '{F} El liceo necesita mochilas para 40 estudiantes. ¿Cuántos pesos se ahorran si se reparan en vez de comprarlas nuevas?', '40*(9000-2000)', 'Se multiplica la diferencia de costo por mochila por el número de estudiantes.', ' pesos'),
        ('abc', '{F} ¿Qué indicador de seguimiento sirve para la opción A?', 'Número de mochilas reparadas y reutilizadas cada año', 'Número de afiches pegados en el liceo', 'Cantidad de comentarios positivos en una red social', 'Un buen indicador mide el resultado; los afiches y los comentarios miden una actividad o una opinión.'),
        ('=', '{F} Si el peso de viabilidad sube de 2 a 5 y los otros pesos no cambian, ¿cuántos puntos suma la opción A?', '3*3+3*2+2*5+3*1', 'Se recalcula la suma con el nuevo peso del tercer criterio.', ' puntos'),
        ('abc', '{F} Con el peso de viabilidad en 5, A suma 28, B suma 24 y C suma 22. ¿Cambia la opción que queda primera?', 'No: A sigue primera con 28 puntos', 'Sí: B pasa a ser la primera', 'Sí: C pasa a ser la primera', 'Los tres totales siguen ordenados igual; la conclusión resiste el cambio de peso.'),
        ('abc', '{F} La opción C tiene viabilidad 1 porque nadie la apoya. ¿Cómo se puede mejorar?', 'Agregar apoyo concreto, como un taller y un punto de intercambio, para subir su viabilidad', 'Subir el puntaje de viabilidad a 3 sin cambiar ninguna acción', 'Eliminar el criterio de viabilidad de la matriz', 'Mejorar la viabilidad exige acciones reales; cambiar el puntaje en el papel o quitar el criterio no cambia la realidad.'),
        ('abc', '{F} ¿Cuál de las opciones es principalmente prevención?', 'A y C, porque evitan comprar mochilas nuevas', 'B, porque usa material reciclado', 'Ninguna: todas son mitigación', 'Reparar o no comprar evita fabricar un producto nuevo; comprar mochilas recicladas cada año sigue generando nuevas.'),
        ('abc', 'Una opción gana por pocos puntos, pero los pesos los eligió un solo grupo. ¿Qué es lo más prudente?', 'Probar otros pesos y consultar a la comunidad, para ver si la conclusión se mantiene', 'Aceptar el resultado, porque los números son objetivos', 'Anular la matriz y decidir por votación rápida sin mirar los datos', 'Los pesos son decisiones humanas; probarlos y consultar da más confianza.'),
        ('abc', '{F} Un informe recomienda la opción A, pero no dice a quién afectará ni cómo se sabrá si funcionó. ¿Qué le falta?', 'Evidencia de equidad (a quién beneficia o excluye) y un indicador de seguimiento con meta', 'Un costo más bajo por mochila, porque el costo es el único criterio que importa', 'Más fotos de mochilas para que el informe se vea mejor', 'Una propuesta necesita saber quién se beneficia y cómo se medirá su resultado.'),
    ],
    ctx=('abc', 'En el taller de reparación, un compañero quiere usar una máquina de coser eléctrica sin que haya una persona adulta presente. ¿Qué haces?', 'Le pides que espere y avisas a la persona adulta a cargo, porque se usa con supervisión', 'Lo dejas, pero le pides que vaya despacio y cuide sus dedos', 'Lo ayudas a enchufarla para que el trabajo avance más rápido', 'Las herramientas con riesgo se usan solo con supervisión adulta; apurar el trabajo no justifica el riesgo.'),
    sc=[
        ('En Ambiente y sostenibilidad: ¿qué es un indicador de seguimiento?', 'Una medida observable que muestra si la solución funciona', 'Un buen indicador mide el resultado de la medida, por ejemplo mochilas reparadas por año.'),
        ('abc', '¿Qué es la viabilidad de una medida?', 'La posibilidad real de llevarla a cabo en ese lugar', 'El costo total de la medida', 'La cantidad de personas que la conocen', 'Una medida viable puede hacerse con los recursos y condiciones disponibles.'),
        ('abc', 'En una matriz de decisión, ¿qué hace el peso de un criterio?', 'Indica cuánto importa ese criterio en la decisión', 'Indica cuántas personas votaron por él', 'Indica cuánto pesa físicamente la opción', 'El peso multiplica el puntaje y hace que un criterio cuente más o menos en el total.'),
    ],
    op=("Usa la {F} Escribe una recomendación en cinco líneas: la opción que eliges y por qué (con sus puntos), un criterio donde es débil y cómo mejorarlo, un indicador de seguimiento con meta y una persona o grupo que consultarías. Cierra con un límite de tu análisis.",
        "Elijo A, el taller de reparación, que suma 22 puntos frente a 19 y 15. Su criterio más débil es la viabilidad (2): se mejora con un horario fijo y una persona adulta a cargo. Indicador: mochilas reparadas por año, con meta de 40. Consultaría a los estudiantes que no pueden comprar una mochila. Límite: los puntajes son de ejemplo y los pesos los elegimos nosotros.",
        ["elige con puntaje", "propone mejorar un criterio débil", "incluye indicador con meta", "consulta a la comunidad"], ["cinco líneas", "indicador con meta", "límite declarado"], ["elegir por un solo criterio", "no proponer seguimiento"],
        "Pregunta qué pasaría con tu recomendación si los pesos de la matriz cambiaran."),
    reinforce="Explica con un ejemplo de tu casa por qué reparar es mejor que reciclar.",
    extend="Propón un indicador de seguimiento para una campaña de intercambio de ropa en tu curso.",
)

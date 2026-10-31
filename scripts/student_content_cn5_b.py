"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 12 (distribución del agua dulce y salada en la Tierra)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12 = "CN05 OA 12"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 12, clase 1
register(
    OA12, 1,
    materials="Papel y lápiz. Si quieres, cien porotos o botones para contar; no son necesarios, los datos están escritos en el cuaderno.",
    use="Aprenderé a distinguir lo que muestran los datos de lo que yo interpreto sobre dónde está el agua de la Tierra. Sirve para no sacar conclusiones apresuradas sobre cuánta agua podemos usar.",
    prior=["Sé que el agua puede estar en estado sólido, líquido y gaseoso.", "Conozco el ciclo del agua: el agua se evapora, forma nubes y vuelve como lluvia."],
    explain=[
        "El agua de la Tierra se guarda en varios lugares: los océanos, los glaciares (grandes masas de hielo), las aguas subterráneas (bajo el suelo), los ríos y lagos, y la atmósfera, donde hay nubes y vapor de agua. El vapor de agua es agua en estado gaseoso que no se ve.",
        "El agua de los océanos es salada: tiene muchas sales disueltas y no sirve para beber ni para regar. El agua dulce tiene muy poca sal. Está en los glaciares, en las aguas subterráneas, en los ríos y en los lagos.",
        "Un modelo ayuda a ver las proporciones. Imagina que toda el agua de la Tierra cabe en 100 vasos. En este modelo, con datos redondeados, 97 vasos son agua salada de los océanos. Además, 2 vasos son hielo de glaciares y 1 vaso es agua subterránea dulce. Ríos, lagos, nubes y vapor juntos no llegan a completar un vaso. Una observación es un dato que leo de la tabla. Una interpretación es la explicación que yo agrego.",
    ],
    vocab=[("agua salada", "agua con muchas sales disueltas, como la de los océanos"), ("agua dulce", "agua con muy poca sal, como la de ríos, lagos y glaciares"), ("glaciar", "gran masa de hielo que se forma en lugares muy fríos"), ("aguas subterráneas", "agua que está bajo la superficie del suelo"), ("vapor de agua", "agua en estado gaseoso; no se ve")],
    worked=[
        {"title": "Cuánta agua dulce hay en el modelo", "problem": "En el modelo de 100 vasos hay 2 vasos de hielo de glaciares y 1 vaso de agua subterránea dulce. ¿Cuántos vasos de agua dulce hay en total, sin contar lo que es menos de un vaso?", "steps": ["Los glaciares son agua dulce: 2 vasos.", "El agua subterránea dulce: 1 vaso.", "Sumo: 2 + 1 = 3."], "answer": "3 vasos de 100"},
        {"title": "Observación o interpretación", "problem": "Dos frases: (A) «En el modelo, los océanos tienen 97 vasos.» (B) «Los océanos nos sirven para tomar agua.» ¿Cuál es observación?", "steps": ["La frase A es un dato que se lee directo de la tabla.", "La frase B agrega una idea que los datos no muestran, porque el agua de los océanos es salada."], "answer": "La frase A es observación; la B es una interpretación que no se apoya en los datos."},
    ],
    mistakes=[
        {"wrong": "Pensar que si hay mucha agua en el planeta, hay mucha agua para beber.", "why": "Se mira el total sin separar agua salada y agua dulce.", "fix": "Separa los datos: casi toda el agua es salada y solo una parte pequeña es dulce."},
        {"wrong": "Escribir una opinión como si fuera un dato de la tabla.", "why": "Se mezcla lo que se observa con lo que se piensa.", "fix": "Pregúntate: ¿esto está escrito en la tabla o lo agregué yo?"},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál de estos lugares guarda agua salada: un océano, un glaciar o un río?", "Un océano", "El agua de los océanos tiene muchas sales; la de glaciares y ríos es dulce."),
            ex("El hielo de un glaciar, ¿está hecho de agua dulce o de agua salada?", "Agua dulce", "Los glaciares son hielo de agua con muy poca sal."),
            ex("El vapor de agua que hay en el aire, ¿está en estado sólido, líquido o gaseoso?", "Gaseoso", "El vapor de agua es agua en estado de gas y no se ve."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es el agua dulce?", "Agua con muy poca sal", "Dulce quiere decir que casi no tiene sales disueltas, aunque no tenga sabor a azúcar."),
            ex("Lee esta frase: «Según el modelo, los océanos tienen 97 vasos de 100». ¿Es una observación o una interpretación?", "Observación", "Es un dato que se lee directamente del modelo."),
            ex("Lee esta frase: «Como hay tanta agua en el planeta, nunca nos faltará agua para beber». ¿Es una observación o una interpretación?", "Interpretación", "Es una idea agregada; los datos no dicen cuánta agua se puede beber."),
        ],
        "apply": [
            arith("Con el modelo de 100 vasos, suma el hielo de glaciares (2 vasos) y el agua subterránea dulce (1 vaso). ¿Cuántos vasos de agua dulce hay en esos dos depósitos?", "2+1", "Se suman los dos depósitos de agua dulce.", " vasos"),
            arith("En el modelo hay 97 vasos de agua salada y 3 vasos de agua dulce. ¿Cuántos vasos más de agua salada que de agua dulce hay?", "97-3", "La diferencia compara los dos volúmenes.", " vasos"),
            ex("Según el modelo, ¿qué guarda más agua: el hielo de los glaciares o los ríos, lagos, nubes y vapor juntos?", "El hielo de los glaciares", "Los glaciares tienen 2 vasos y los otros depósitos juntos tienen menos de 1 vaso."),
        ],
        "reason": [
            ex("Ana dice: «Hay 97 vasos de 100 con agua, así que casi toda el agua sirve para tomar». ¿Qué dato del modelo muestra que se equivoca?", "Los 97 vasos son agua salada de los océanos y el agua dulce son solo 3 vasos", "Casi toda el agua del modelo es salada y no se puede beber."),
            ex("Los glaciares tienen 2 vasos y el agua subterránea dulce tiene 1 vaso. Completa: los glaciares guardan ___ veces el agua de las aguas subterráneas dulces.", "2", "Dos vasos es el doble de un vaso."),
        ],
        "challenge": [
            ex("El modelo de los 100 vasos usa datos redondeados. ¿Cuál es una limitación de ese modelo: (a) muestra que el agua se mueve de un lugar a otro, o (b) usa cifras aproximadas y no muestra el movimiento del agua?", "(b)", "Un modelo de vasos muestra cantidades en un momento y redondea los valores."),
            arith("De los 3 vasos de agua dulce del modelo, 2 son hielo de glaciares. ¿Cuántos vasos de agua dulce no están congelados?", "3-2", "Se resta el hielo del total de agua dulce.", " vaso"),
        ],
    },
    context=[ex("En tu casa alguien dice: «Podemos gastar toda el agua que queramos, porque el mar es enorme». Con lo que aprendiste, ¿qué respuesta con datos le darías?", "El mar es agua salada; el agua dulce es solo cerca de 3 de cada 100 vasos del modelo", "Se usa el dato de proporción para corregir la idea de que sobra agua dulce.")],
    selfcheck=[
        ex("¿Qué agua tiene muchas sales: la del océano o la de un glaciar?", "La del océano", "El agua de mar es salada."),
        ex("En el modelo, ¿cuántos vasos de 100 son agua salada de los océanos?", "97", "Es el dato del modelo de 100 vasos."),
        ex("Una observación, ¿se lee en los datos o la agrego yo?", "Se lee en los datos", "La interpretación es la que agrega la persona."),
    ],
    open_task=task(
        "Copia esta tabla en tu cuaderno: océanos 97 vasos, glaciares 2 vasos, aguas subterráneas dulces 1 vaso, ríos, lagos, nubes y vapor menos de 1 vaso. Escribe tres observaciones que salgan directo de la tabla y una interpretación tuya. Marca con una O las observaciones y con una I la interpretación.",
        "O: los océanos tienen 97 vasos. O: los glaciares tienen el doble que las aguas subterráneas. O: ríos y lagos tienen menos de 1 vaso. I: me parece que cuidar el agua dulce es importante porque es poca.",
        ["tres observaciones que están en la tabla", "una interpretación marcada", "no mezcla una con otra"],
        ["tabla copiada", "frases rotuladas O e I"],
        ["escribir como observación algo que no está en la tabla", "olvidar rotular"],
        "Pregunta cómo supo que cada observación estaba en la tabla.",
    ),
    reinforce="Escribe una frase que sea observación y otra que sea interpretación sobre el agua dulce y el agua salada.",
    extend="Averigua con una persona de tu casa de dónde viene el agua que llega a tu llave y si es agua de río, de lago o subterránea.",
)

# ---------------------------------------------------------------- OA 12, clase 2
register(
    OA12, 2,
    materials="Papel y lápiz. Los datos que necesitas están escritos en el cuaderno.",
    use="Aprenderé a formular preguntas que se pueden comprobar con datos y a hacer predicciones sobre los volúmenes de agua de la Tierra. Sirve para comparar sin adivinar.",
    prior=["Sé que casi toda el agua de la Tierra es salada.", "Sé leer una tabla de datos con vasos como unidad."],
    explain=[
        "Una pregunta comprobable se puede responder con datos o mediciones. «¿Cuántos vasos de 100 son agua dulce?» es comprobable. «¿Qué agua es más bonita?» no lo es, porque depende del gusto de cada persona.",
        "Una predicción es lo que creo que va a pasar o a resultar, apoyado en un dato. Se puede escribir como «Si…, entonces…». Por ejemplo: si los glaciares tienen 2 vasos y las aguas subterráneas dulces tienen 1 vaso, entonces predigo que los glaciares guardan más agua dulce.",
        "Después se compara la predicción con los datos. Si coincide, la predicción se sostiene. Si no coincide, se corrige la predicción, no los datos. En esta clase usas el modelo de 100 vasos: 97 de agua salada, 2 de hielo de glaciares, 1 de agua subterránea dulce, y menos de 1 para ríos, lagos, nubes y vapor.",
    ],
    vocab=[("pregunta comprobable", "pregunta que se responde con datos o mediciones"), ("predicción", "lo que creo que resultará, apoyado en un dato"), ("proporción", "cuántas partes hay de algo en cada 100 partes del total"), ("volumen", "cuánto espacio ocupa el agua"), ("comparar", "mirar dos datos con la misma unidad para ver cuál es mayor")],
    worked=[
        {"title": "Predecir con proporción", "problem": "En 100 vasos de agua del planeta, 3 son de agua dulce. Si el modelo fuera de 200 vasos con las mismas proporciones, ¿cuántos serían de agua dulce?", "steps": ["200 vasos son 2 veces 100 vasos.", "Por cada 100 hay 3 de agua dulce, entonces 2 × 3 = 6."], "answer": "6 vasos"},
        {"title": "Elegir la pregunta comprobable", "problem": "¿Cuál se puede comprobar: «¿Qué océano es más lindo?» o «¿Cuántos vasos de 100 son hielo de glaciares?»?", "steps": ["La primera depende del gusto.", "La segunda se responde con un dato de la tabla: 2 vasos."], "answer": "La segunda, porque se responde con un dato"},
    ],
    mistakes=[
        {"wrong": "Escribir una predicción que no se apoya en ningún dato.", "why": "Se confunde adivinar con predecir.", "fix": "Empieza con «Si…» y nombra el dato en que te apoyas."},
        {"wrong": "Cambiar los datos cuando la predicción falló.", "why": "Se quiere tener razón a toda costa.", "fix": "Si el dato contradice la predicción, corrige la predicción."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál se puede comprobar con datos: «¿Qué océano es más bonito?» o «¿Cuántos vasos de 100 son agua dulce?»?", "¿Cuántos vasos de 100 son agua dulce?", "Se responde con un dato, no con un gusto."),
            ex("Completa: una predicción se apoya en un ___ (dato o gusto).", "dato", "Predecir con evidencia exige un dato como base."),
            ex("En el modelo de 100 vasos hay 97 de agua salada y 3 de agua dulce. ¿Se cumple la predicción «hay más agua salada que dulce»?", "Sí", "97 es mayor que 3."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una predicción?", "Lo que creo que resultará, apoyado en un dato", "Una predicción no es una adivinanza, tiene un dato de apoyo."),
            ex("La pregunta «¿Qué color de agua es más agradable?», ¿es una pregunta comprobable con datos?", "No", "Depende del gusto de la persona."),
            ex("¿Cuál es una buena predicción: (a) «Me gustan los glaciares» o (b) «Si los glaciares tienen 2 vasos y los lagos menos de 1 vaso, entonces los glaciares guardan más agua que los lagos»?", "(b)", "Empieza con «Si…», usa dos datos y se puede comprobar."),
        ],
        "apply": [
            arith("Si toda el agua de la Tierra fuera 200 vasos, con las mismas proporciones del modelo, ¿cuántos vasos serían de agua dulce (3 de cada 100)?", "2*3", "200 es el doble de 100, entonces el agua dulce también se duplica.", " vasos"),
            arith("Y si fueran 300 vasos en total, ¿cuántos serían de agua salada (97 de cada 100)?", "3*97", "300 es tres veces 100, entonces se multiplica 97 por 3.", " vasos"),
            ex("Ordena de mayor a menor volumen estos tres depósitos del modelo: glaciares (2 vasos), océanos (97 vasos), aguas subterráneas dulces (1 vaso).", "Océanos, glaciares, aguas subterráneas dulces", "Se ordenan por el número de vasos: 97, 2 y 1."),
        ],
        "reason": [
            ex("Nico predijo: «los ríos y lagos juntos tienen más agua que los glaciares». Con el modelo, ¿qué dato muestra que su predicción falla?", "Los ríos y lagos son menos de 1 vaso y los glaciares son 2 vasos", "Menos de un vaso es menor que dos vasos."),
            ex("Natalia predijo que las aguas subterráneas dulces tendrían más agua que los glaciares y los datos dicen lo contrario. ¿Qué debe corregir: la predicción o los datos?", "La predicción", "Los datos son la evidencia; la predicción se ajusta."),
        ],
        "challenge": [
            ex("Equipo A dice: «97 vasos de 100 son agua salada». Equipo B dice: «970 mL de 1.000 mL son agua salada». ¿Muestran la misma proporción?", "Sí", "970 de 1.000 es lo mismo que 97 de 100."),
            arith("En un modelo de 1.000 vasos con las mismas proporciones, ¿cuántos vasos serían hielo de glaciares (2 de cada 100)? Hay 10 grupos de 100 vasos.", "10*2", "Cada grupo de 100 vasos tiene 2 de hielo.", " vasos"),
        ],
    },
    context=[ex("Tu curso quiere averiguar si en la Tierra sobra o falta agua dulce. ¿Qué pregunta comprobable puede hacer: (a) «¿Qué agua nos gusta más?» o (b) «¿Cuántos vasos de 100 son agua dulce?»?", "(b)", "Se responde con la tabla del modelo.")],
    selfcheck=[
        ex("Una pregunta comprobable, ¿se responde con datos o con gustos?", "Con datos", "Los datos permiten comprobar."),
        ex("¿Con qué palabras puede empezar una predicción?", "Si", "Se escribe «Si…, entonces…»."),
        ex("Si el dato contradice mi predicción, ¿qué debo cambiar?", "La predicción", "El dato es la evidencia."),
    ],
    open_task=task(
        "Con los datos del modelo (océanos 97 vasos, glaciares 2, aguas subterráneas dulces 1, ríos, lagos, nubes y vapor menos de 1), escribe una pregunta comprobable y una predicción con «Si…, entonces…». Luego revisa en la tabla si tu predicción se cumple y escribe qué dato usaste.",
        "Pregunta: ¿cuál depósito de agua dulce es el mayor? Predicción: si los glaciares tienen 2 vasos y las aguas subterráneas 1 vaso, entonces los glaciares son mayores. Se cumple: 2 es mayor que 1.",
        ["pregunta que se responde con datos", "predicción con «Si…, entonces…»", "comparación con la tabla"],
        ["pregunta escrita", "predicción escrita", "dato usado"],
        ["hacer una pregunta de gusto", "predecir sin citar un dato"],
        "Pregunta qué habría hecho si el dato hubiera contradicho su predicción.",
    ),
    reinforce="Inventa otra predicción con «Si…, entonces…» sobre océanos y glaciares y revísala con la tabla.",
    extend="Averigua con una persona de tu casa si en tu región el agua que usan viene de un río, de un pozo o de otra fuente.",
)

# ---------------------------------------------------------------- OA 12, clase 3
register(
    OA12, 3,
    materials="Una botella de 1 litro y una cuchara sopera si quieres hacer el modelo con ayuda de una persona adulta; si no, trabaja con los datos escritos. Solo agua de la llave.",
    use="Aprenderé a usar un modelo a escala para representar cuánta agua salada y cuánta agua dulce hay en la Tierra. Sirve para imaginar proporciones que son imposibles de ver.",
    prior=["Sé que 1 litro tiene 1.000 mililitros (mL).", "Conozco el modelo de 100 vasos."],
    explain=[
        "Un modelo es una representación simple de algo muy grande o difícil de ver. Para mostrar el agua de la Tierra puedo usar una botella de 1 litro, que son 1.000 mililitros. La botella completa representa toda el agua del planeta.",
        "En este modelo, con datos redondeados, el agua salada de los océanos es 970 mL. El agua dulce es solo 30 mL, más o menos dos cucharadas soperas. De esos 30 mL, 20 mL representan el hielo de los glaciares y 10 mL el agua subterránea dulce. Los ríos, lagos, nubes y vapor serían menos de 1 mL: casi invisibles.",
        "Todo modelo tiene límites. Este muestra cuánta agua hay en cada lugar en un momento, pero no muestra que el agua se mueve con el ciclo del agua, ni cuánta es fácil de usar. Tampoco las cifras son exactas, porque están redondeadas. Por eso un modelo ayuda a explicar, pero no reemplaza la medición.",
    ],
    vocab=[("modelo", "representación simple de algo para poder estudiarlo"), ("escala", "relación entre el tamaño del modelo y la cosa real"), ("mililitro (mL)", "unidad de volumen; 1.000 mL son 1 litro"), ("limitación", "algo que el modelo no puede mostrar"), ("proporción", "parte que representa una cantidad dentro del total")],
    worked=[
        {"title": "Agua dulce en la botella", "problem": "La botella de 1.000 mL representa toda el agua del planeta. El agua salada son 970 mL. ¿Cuántos mL son de agua dulce?", "steps": ["El total es 1.000 mL.", "Resto el agua salada: 1.000 − 970 = 30."], "answer": "30 mL"},
        {"title": "Cucharadas de agua dulce", "problem": "Una cucharada sopera tiene 15 mL. ¿Cuántas cucharadas llenan los 30 mL de agua dulce del modelo?", "steps": ["Divido 30 en grupos de 15.", "30 ÷ 15 = 2."], "answer": "2 cucharadas"},
    ],
    mistakes=[
        {"wrong": "Creer que el modelo muestra el agua exacta de cada lugar.", "why": "Se olvida que las cifras están redondeadas.", "fix": "Un modelo da una idea de las proporciones, no una medición exacta."},
        {"wrong": "Pensar que 30 mL de agua dulce son mucho porque la botella es grande.", "why": "Se compara con el tamaño de la botella y no con el total de 1.000 mL.", "fix": "Compara 30 con 1.000: es una parte muy pequeña."},
    ],
    tiers={
        "recovery": [
            arith("En una botella de 1.000 mL que representa toda el agua de la Tierra, el agua salada son 970 mL. ¿Cuántos mL son de agua dulce?", "1000-970", "Se resta el agua salada del total.", " mL"),
            ex("En este modelo, ¿qué representa la botella completa?", "Toda el agua de la Tierra", "La botella es el total del modelo."),
            arith("Una cucharada sopera tiene 15 mL. ¿Cuántas cucharadas hacen los 30 mL de agua dulce del modelo?", "30//15", "Se reparte 30 mL en cucharadas de 15 mL.", " cucharadas"),
        ],
        "understand": [
            ex("En Ciencias, ¿para qué sirve un modelo?", "Para representar a pequeña escala algo grande o difícil de ver", "El modelo permite imaginar y comparar cantidades."),
            arith("En el modelo de 1 L, 20 mL son hielo de glaciares y el agua dulce total son 30 mL. ¿Cuántos mL de agua dulce no son glaciares?", "30-20", "Se resta el hielo del total de agua dulce.", " mL"),
            ex("El modelo de 100 vasos y el modelo de la botella de 1.000 mL, ¿muestran la misma proporción de agua dulce?", "Sí", "3 de 100 es lo mismo que 30 de 1.000."),
        ],
        "apply": [
            arith("Si usas una garrafa de 10 litros (10.000 mL) para representar toda el agua del planeta, ¿cuántos mL serían agua dulce, a razón de 3 por cada 100? Hay 100 grupos de 100 mL.", "100*3", "Cada grupo de 100 mL aporta 3 mL de agua dulce.", " mL"),
            arith("Con un modelo de 2 litros (2.000 mL), ¿cuántos mL serían agua salada, a razón de 97 por cada 100? Hay 20 grupos de 100 mL.", "20*97", "Cada grupo de 100 mL aporta 97 mL de agua salada.", " mL"),
            ex("En la botella, los ríos, lagos, nubes y vapor serían menos de 1 mL. ¿Se verían como una parte grande o casi invisible de la botella?", "Casi invisible", "Menos de 1 mL entre 1.000 mL es una parte diminuta."),
        ],
        "reason": [
            ex("Pedro dice que la botella prueba que el agua dulce se acabará pronto. ¿Qué limitación del modelo muestra que no puede afirmar eso?", "El modelo muestra cantidades en un momento y no muestra que el agua se mueve y se renueva con el ciclo del agua", "Un modelo estático no puede probar lo que pasará."),
            ex("Dos modelos: A usa una botella de 1.000 mL y B una de 500 mL. En ambos el agua dulce es 3 de cada 100 partes. ¿En cuál hay más mL de agua dulce?", "En la botella de 1.000 mL", "Tiene 30 mL contra 15 mL de la botella de 500 mL."),
        ],
        "challenge": [
            arith("En una botella de 500 mL, ¿cuántos mL de agua salada hay (97 por cada 100)? Hay 5 grupos de 100 mL.", "5*97", "Cada grupo de 100 mL tiene 97 mL de agua salada.", " mL"),
            arith("El modelo de la botella tiene 20 mL de hielo y 10 mL de agua subterránea dulce. ¿Cuántas veces cabe el agua subterránea en el hielo?", "20//10", "20 dividido en grupos de 10 da 2.", " veces"),
        ],
    },
    context=[ex("En una feria de ciencias muestran una botella de 1 litro con solo 30 mL de agua celeste y el resto transparente. ¿Qué representa el agua celeste?", "El agua dulce de la Tierra", "Los 30 mL son el agua dulce dentro del total de 1.000 mL.")],
    selfcheck=[
        ex("¿Cuántos mL de agua dulce hay en el modelo de 1.000 mL?", "30 mL", "1.000 − 970 = 30."),
        ex("¿Cuántos mL tiene 1 litro?", "1.000 mL", "Es la equivalencia entre litro y mililitro."),
        ex("Nombra una limitación del modelo de la botella.", "No muestra el movimiento del agua o usa cifras redondeadas", "Un modelo nunca lo muestra todo."),
    ],
    open_task=task(
        "Con ayuda de una persona de tu casa, usa una botella de 1 litro y una cuchara sopera de 15 mL. Llena la botella con 1 litro de agua. Con la cuchara (más o menos 15 mL) saca 2 cucharadas y échalas en un vaso: ese vaso representa el agua dulce del planeta y lo que queda en la botella, el agua salada. Si no puedes, dibuja una botella y marca con color los 30 mL. Escribe qué parte del dibujo representa el agua dulce y una limitación de tu modelo.",
        "Dibujo de una botella con una franja muy fina de 30 mL. El agua dulce es muy poca. Limitación: no muestra que el agua cambia de lugar con el ciclo del agua.",
        ["la parte dulce es mucho más pequeña que la salada", "explica qué representa cada parte", "nombra una limitación"],
        ["dibujo o fotografía del modelo", "frase de explicación"],
        ["dibujar el agua dulce como la mitad de la botella", "no nombrar limitaciones"],
        "Pregunta por qué la parte dulce se ve tan pequeña y qué dato lo justifica.",
    ),
    reinforce="Explica a alguien de tu casa por qué 30 mL de agua dulce en 1.000 mL son muy pocos.",
    extend="Imagina una botella de 1,5 litros (1.500 mL) que representa toda el agua de la Tierra. Calcula cuántos mL serían de agua dulce, a razón de 3 por cada 100 mL.",
)

# ---------------------------------------------------------------- OA 12, clase 4
register(
    OA12, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a comparar los volúmenes de agua de la Tierra con un criterio común y a concluir por qué el agua dulce es escasa en comparación con el total. Sirve para decidir con datos.",
    prior=["Conozco el modelo de 100 vasos y el de la botella de 1.000 mL.", "Sé que comparar exige usar la misma unidad."],
    explain=[
        "Para comparar volúmenes hay que usar un criterio común: la misma unidad y el mismo total. No se puede comparar mililitros de una botella con vasos de otra sin convertir. Una forma justa es decir cuántas partes hay en cada 100 partes del total.",
        "Con ese criterio, el modelo dice: de cada 100 partes de agua de la Tierra, 97 son agua salada de los océanos, 2 son hielo de glaciares, 1 es agua subterránea dulce y ríos, lagos, nubes y vapor son menos de 1. Así se ve que el agua dulce es escasa en términos relativos: es una parte pequeña del total.",
        "Además, gran parte del agua dulce está congelada en los glaciares. Por eso el agua dulce que es fácil de usar, como la de ríos, lagos y parte de las aguas subterráneas, es todavía menos. «Hay mucha agua en el planeta» y «hay mucha agua dulce fácil de usar» son dos afirmaciones muy distintas.",
    ],
    vocab=[("criterio común", "regla igual para todos los datos que se comparan"), ("escasez relativa", "ser poco comparado con el total"), ("depósito", "lugar donde se guarda agua, como un océano o un glaciar"), ("conclusión", "idea final que se apoya en los datos"), ("accesible", "que se puede alcanzar y usar con facilidad")],
    worked=[
        {"title": "Misma proporción", "problem": "La botella A tiene 500 mL con 15 mL de agua dulce. La botella B tiene 1.000 mL con 30 mL de agua dulce. ¿Cuál tiene más proporción de agua dulce?", "steps": ["En A: 500 mL son 5 grupos de 100 mL, y 15 mL ÷ 5 = 3 mL por cada 100 mL.", "En B: 1.000 mL son 10 grupos, y 30 mL ÷ 10 = 3 mL por cada 100 mL."], "answer": "Ninguna: las dos tienen 3 mL de agua dulce por cada 100 mL"},
        {"title": "Diferencia de volúmenes", "problem": "En el modelo de 100 vasos, ¿cuántos vasos más tienen los océanos (97) que los glaciares (2)?", "steps": ["Los dos datos están en vasos de 100.", "Resto: 97 − 2 = 95."], "answer": "95 vasos"},
    ],
    mistakes=[
        {"wrong": "Comparar 30 mL de una botella con 15 mL de otra y decir que la primera tiene más proporción de agua dulce.", "why": "No se consideró que las botellas tienen distinto tamaño.", "fix": "Compara cuántos mL hay por cada 100 mL de agua."},
        {"wrong": "Concluir que sobra agua porque los océanos son enormes.", "why": "Se olvida que esa agua es salada.", "fix": "Cita el dato: el agua dulce es 3 de cada 100 partes."},
    ],
    tiers={
        "recovery": [
            ex("Para comparar dos volúmenes de agua, ¿se deben usar unidades distintas o la misma unidad?", "La misma unidad", "Sin unidad común la comparación no es justa."),
            ex("¿Qué depósito del modelo tiene más agua: los glaciares (2 vasos) o las aguas subterráneas dulces (1 vaso)?", "Los glaciares", "2 vasos es más que 1 vaso."),
            ex("El agua dulce es 3 de cada 100 partes del agua de la Tierra. ¿Es escasa o abundante en comparación con el agua salada?", "Escasa", "Tres de cien es una parte muy pequeña."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es un criterio común de comparación?", "Usar la misma unidad y el mismo total para todos los datos", "Así los datos se pueden comparar con justicia."),
            ex("Ordena de menor a mayor volumen: aguas subterráneas dulces (1 vaso), glaciares (2 vasos), ríos, lagos, nubes y vapor (menos de 1 vaso).", "Ríos, lagos, nubes y vapor; aguas subterráneas dulces; glaciares", "Se ordenan por el número de vasos: menos de 1, 1 y 2."),
            ex("La escasez relativa del agua dulce, ¿significa que no hay nada de agua dulce o que es poca comparada con el total?", "Que es poca comparada con el total", "Relativa quiere decir en comparación con otra cantidad."),
        ],
        "apply": [
            arith("El equipo A anotó en su botella de 1 L: glaciares 20 mL y aguas subterráneas dulces 10 mL. ¿Cuántos mL de agua dulce suman?", "20+10", "Se suman los dos depósitos de agua dulce.", " mL"),
            arith("En el modelo de 100 vasos, ¿cuántos vasos más tienen los océanos (97) que las aguas subterráneas dulces (1)?", "97-1", "Los dos datos están en vasos del mismo modelo.", " vasos"),
            ex("Botella A: 200 mL con 6 mL de agua dulce. Botella B: 400 mL con 16 mL de agua dulce. ¿Cuál tiene mayor proporción de agua dulce?", "La botella B", "En A hay 3 mL por cada 100 mL (6 ÷ 2) y en B hay 4 mL por cada 100 mL (16 ÷ 4)."),
        ],
        "reason": [
            ex("Julia dice: «mi modelo tiene más agua dulce porque tiene 30 mL y el de Tomás 15 mL». Tomás usó 500 mL en total y Julia 1.000 mL. ¿Es válida su comparación?", "No, porque los totales son distintos; en ambos el agua dulce es 3 de cada 100", "Hay que comparar la proporción, no solo los mL."),
            ex("¿Qué dato usarías para justificar que el agua dulce es escasa: (a) «el planeta tiene mucha agua» o (b) «solo 3 de cada 100 partes son agua dulce»?", "(b)", "La proporción respalda la escasez relativa; la frase (a) no distingue entre agua salada y agua dulce."),
        ],
        "challenge": [
            arith("Un modelo tiene 200 vasos en total, con las mismas proporciones. ¿Cuántos vasos serían hielo de glaciares (2 de cada 100)?", "2*2", "200 son dos grupos de 100 vasos, y cada uno tiene 2 de hielo.", " vasos"),
            ex("¿Qué conclusión se sostiene mejor con los datos: (a) «Los océanos y glaciares guardan casi toda el agua, y el hielo no es fácil de usar, así que el agua dulce accesible es poca» o (b) «Hay agua de sobra para todos»?", "(a)", "Cita datos y reconoce el límite del hielo; la (b) no tiene evidencia."),
        ],
    },
    context=[ex("En un cartel del colegio escriben: «La Tierra es azul, así que hay agua de sobra». Con lo aprendido, ¿qué dato agregarías para corregirlo?", "Solo 3 de cada 100 partes del agua son dulces", "El dato de proporción muestra que el agua dulce es escasa.")],
    selfcheck=[
        ex("¿Qué se necesita para comparar volúmenes con justicia?", "Un criterio común, con la misma unidad", "Sin criterio común la comparación no vale."),
        ex("¿Cuál tiene más agua en el modelo: los océanos o los glaciares?", "Los océanos", "97 vasos es más que 2 vasos."),
        ex("¿El agua dulce es abundante o escasa en relación con el total?", "Escasa", "Es una parte pequeña del total."),
    ],
    open_task=task(
        "Copia la tabla: océanos 97 vasos, glaciares 2 vasos, aguas subterráneas dulces 1 vaso, ríos, lagos, nubes y vapor menos de 1 vaso. Ordénala de mayor a menor y escribe una conclusión de dos frases sobre la escasez de agua dulce. Debe citar al menos dos datos y mencionar una limitación del modelo.",
        "Orden: océanos, glaciares, aguas subterráneas dulces, ríos, lagos, nubes y vapor. Conclusión: el agua dulce son solo 3 de 100 vasos y gran parte es hielo. El modelo usa cifras redondeadas.",
        ["tabla ordenada de mayor a menor", "cita al menos dos datos", "nombra una limitación"],
        ["tabla ordenada", "conclusión escrita"],
        ["ordenar sin fijarse en los vasos", "concluir sin usar datos"],
        "Pregunta qué dato fue el más importante para su conclusión.",
    ),
    reinforce="Escribe una oración que explique por qué «mucha agua» no significa «mucha agua dulce».",
    extend="Averigua en qué parte de Chile hay glaciares y piensa por qué el hielo no es un agua fácil de usar.",
)

"""Cuaderno del estudiante, 2.º medio Tecnología: OA 01 (necesidades que implican reducir efectos perjudiciales del uso de energía y materiales, desde la sustentabilidad), clases 1 a 4.

Seguridad: las tareas son de lectura, cálculo y escritura. Los consumos se leen de boletas, etiquetas y medidores que están a la vista; nunca se abren aparatos, tableros ni instalaciones eléctricas.
Cifras enteras. Las potencias, los consumos, los precios y los residuos son datos de ejemplo para practicar; no nombran marcas ni personas reales.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE2M OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    def conv(i):
        return i if isinstance(i, dict) else ex(*i)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [conv(i) for i in R], "understand": [conv(i) for i in C], "apply": [conv(i) for i in A], "reason": [conv(i) for i in Z], "challenge": [conv(i) for i in D]},
        context=[conv(ctx)], selfcheck=[conv(i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01, clase 1
reg(
    OA1, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus respuestas.",
    use="Aprenderé a distinguir fuentes de energía renovables y no renovables, a reconocer los efectos perjudiciales del uso de energía y de materiales y a explicar qué significa sustentabilidad. Sirve para detectar dónde hay una necesidad que atender.",
    prior=["Sé que una necesidad es algo que falta o que funciona mal.", "Sé calcular un porcentaje sencillo.", "Sé que un material se fabrica y luego se desecha."],
    explain=[
        "La energía puede venir de fuentes renovables, que se reponen en un tiempo corto, como el sol, el viento y el agua en movimiento. También puede venir de fuentes no renovables, que se agotan al usarlas, como el carbón, el petróleo y el gas natural. Los materiales, como el papel, el plástico o los metales, se extraen de la naturaleza, se fabrican, se usan y al final se desechan.",
        "El uso de energía y de materiales tiene efectos perjudiciales: gases que se emiten al quemar combustibles y que aumentan el calentamiento de la atmósfera, residuos que se acumulan, agotamiento de recursos y consumo excesivo de agua. Un efecto perjudicial se detecta cuando se compara lo que se usa con lo que realmente se necesita. Dejar una luz encendida en una sala vacía es un gasto sin beneficio.",
        "La sustentabilidad consiste en satisfacer las necesidades de hoy sin comprometer la posibilidad de que las generaciones futuras satisfagan las suyas. Una necesidad tecnológica sustentable es aquella en que falta una solución para reducir un efecto perjudicial del uso de energía o materiales. Se parte siempre del efecto y de a quiénes afecta, no de un objeto elegido de antemano.",
    ],
    vocab=[("fuente renovable", "fuente de energía que se repone en poco tiempo"), ("fuente no renovable", "fuente de energía que se agota al usarla"), ("efecto perjudicial", "daño o gasto sin beneficio que causa el uso de un recurso"), ("residuo", "material que queda después de usar algo y se desecha"), ("sustentabilidad", "satisfacer necesidades de hoy sin dañar las de generaciones futuras"), ("recurso", "energía o material que se usa para hacer algo")],
    worked=[
        ("Clasificar una fuente", "Clasifica como renovable o no renovable: la energía de un río que mueve una turbina.", ["Pregunto si la fuente se repone en poco tiempo: el agua vuelve a correr con la lluvia y el deshielo.", "Entonces no se agota al usarla."], "Renovable"),
        ("Detectar un efecto perjudicial", "En un taller se imprimen 80 hojas por una sola cara y 30 de ellas se botan sin leerse. ¿Cuál es el efecto perjudicial y qué porcentaje del papel se desperdicia?", ["El efecto es un gasto de material sin beneficio: papel que termina como residuo.", "Se calcula 30 × 100 ÷ 80 = 37,5, es decir, casi 38 de cada 100 hojas."], "Residuo de papel; cerca del 38 % se desperdicia"),
    ],
    mistakes=[
        ("Pensar que una fuente renovable no produce ningún efecto perjudicial.", "Fabricar equipos para captar esa energía también usa materiales y energía, y después se desechan.", "Revisa el efecto en todo el recorrido: fabricación, uso y desecho."),
        ("Empezar diciendo «hay que comprar un aparato» antes de ver el efecto.", "Se elige un objeto sin saber qué daño o gasto se quiere reducir.", "Primero escribe el efecto y a quiénes afecta; la solución viene después."),
    ],
    R=[
        ("¿Cuál es una fuente de energía renovable? A) el petróleo B) el viento", "B", "El viento se repone constantemente; el petróleo se agota al usarlo."),
        ("¿Es renovable o no renovable el gas natural?", "No renovable", "Se agota al quemarlo y no se repone en un tiempo corto."),
        ("Una luz queda encendida toda la noche en una sala vacía. ¿Qué efecto perjudicial hay? A) un gasto de energía sin beneficio B) un exceso de residuos sólidos", "A", "Se consume energía y nadie la aprovecha."),
    ],
    C=[
        ("¿Cuál frase define mejor la sustentabilidad? A) satisfacer necesidades de hoy sin comprometer las de generaciones futuras B) gastar lo menos posible en el presente", "A", "La sustentabilidad mira también el futuro, no solo el ahorro de dinero de hoy."),
        ("Un grupo dice: «El panel solar no tiene ningún efecto perjudicial». ¿Qué se le puede responder? A) fabricarlo usa materiales y energía, y al final se desecha B) la energía del sol se agota con el uso", "A", "Un recurso renovable también tiene efectos en la fabricación y el desecho."),
        ("Una necesidad sustentable, ¿parte de un objeto elegido o de un efecto perjudicial por reducir? A) de un objeto elegido B) de un efecto perjudicial", "B", "Primero se identifica el efecto y a quiénes afecta."),
    ],
    A=[
        arith("En un país de ejemplo, de 200 unidades de energía eléctrica, 120 vienen de fuentes renovables. ¿Qué porcentaje viene de fuentes no renovables?", "(200-120)*100//200", "Se resta lo renovable al total y se pasa a porcentaje.", " %"),
        ("Clasifica cada fuente como renovable (R) o no renovable (N): (1) el sol, (2) el carbón, (3) el agua en movimiento.", "1 R, 2 N, 3 R", "El sol y el agua en movimiento se reponen; el carbón se agota."),
        arith("En un liceo de ejemplo, un curso bota 12 kg de papel a la semana. Si reutilizan la mitad de ese papel, ¿cuántos kg dejan de botar en 4 semanas?", "12*4//2", "Se calcula el total de 4 semanas y se toma la mitad.", " kg"),
    ],
    Z=[
        ("Un colegio quiere cambiar todos los enchufes por otros nuevos, aunque los actuales funcionan bien. ¿Por qué podría aumentar el efecto perjudicial?", "Fabricar los nuevos gasta materiales y energía, y los antiguos se vuelven residuo", "Cambiar algo que funciona crea un gasto y un residuo que antes no existían."),
        ("Un vecino dice: «Si la energía es renovable, puedo gastar toda la que quiera». ¿Es correcto?", "No: igual conviene no gastar sin necesidad", "Aunque se repone, captarla y distribuirla usa materiales y no siempre alcanza para todos."),
    ],
    D=[
        ex("Salas de ejemplo con ahorro posible: sala A gasta 200 Wh al día y podría ahorrar 50; sala B gasta 120 y podría ahorrar 40; sala C gasta 300 y podría ahorrar 60. ¿En cuál es mayor el porcentaje de ahorro posible y de cuánto es?", "En la sala B, 33 %", "A ahorra 25 %, B cerca de 33 % y C 20 %.", calc="40*100//120"),
        arith("Un edificio de ejemplo gasta 480 kWh al mes. Si logra reducir 15 % del consumo, ¿cuántos kWh gastará?", "480-480*15//100", "Se calcula 15 % de 480 y se resta del total.", " kWh"),
    ],
    ctx=ex("Una escuela de ejemplo tiene 25 salas y en 10 de ellas queda la luz encendida después de la jornada. ¿Qué porcentaje de las salas gasta energía sin beneficio?", "40 %", "Se calcula 10 × 100 ÷ 25 = 40.", calc="10*100//25"),
    sc=[
        ("En Tecnología: ¿qué es un efecto perjudicial del uso de un recurso?", "Un daño o gasto sin beneficio que causa su uso", "Es la definición de la clase."),
        ("¿La energía del viento es renovable o no renovable?", "Renovable", "Se repone constantemente."),
        ("¿Desde dónde parte una necesidad sustentable?", "Desde un efecto perjudicial y las personas a las que afecta", "La solución se elige después."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: en un casino escolar se botan cada día unos 30 vasos desechables. Caso 2: en un gimnasio de ejemplo las luces quedan encendidas toda la noche. Caso 3: en un taller se descartan retazos de madera que aún se podrían usar. Escribe: (1) el recurso, (2) el efecto perjudicial, (3) quiénes resultan afectados y (4) una oración que diga por qué esa situación no es sustentable, sin nombrar ningún objeto como solución.",
        "Caso 2: recurso, energía eléctrica; efecto, gasto sin beneficio; afectados, el gimnasio que paga más y quienes dependen de la misma energía; no es sustentable porque se consume un recurso que no se aprovecha",
        ["nombra el recurso", "describe el efecto con claridad", "indica a quiénes afecta", "no nombra la solución"],
        ["hoja con las cuatro respuestas"],
        ["decir «hay que comprar un aparato»", "confundir el recurso con el efecto"],
        "Pregunta: «¿esto dice qué daño o gasto hay o ya dice qué construir?». Si dice qué construir, pídele reescribirlo.",
    ),
    reinforce="Mira tu casa o tu curso y anota dos casos en que se gasta energía o material sin beneficio, con una oración que explique por qué.",
    extend="Explica por qué una fuente renovable puede igualmente tener efectos perjudiciales y cómo lo descubrirías.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los datos escritos en este cuaderno. Todo se resuelve en papel, sin conectar aparatos.",
    use="Aprenderé a calcular cuánta energía gasta un aparato, a convertir entre Wh y kWh, a calcular un costo y a decidir dónde está el mayor consumo. Sirve para demostrar con números que una necesidad existe.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé calcular un porcentaje.", "Sé que un efecto perjudicial puede ser un gasto sin beneficio."],
    explain=[
        "La potencia de un aparato dice cuánta energía usa por cada hora que funciona. Se mide en vatios (W) y viene escrita en su etiqueta. La energía que gasta se calcula así: energía en Wh = potencia en W × horas de uso. Un aparato de 10 W encendido 5 horas gasta 10 × 5 = 50 Wh. Un kilovatio hora (kWh) equivale a 1.000 Wh y es la unidad que aparece en la boleta de la luz.",
        "Con el consumo se calcula el costo: costo = kWh × precio por kWh. En esta clase el precio es un dato de ejemplo. Para detectar dónde hay más gasto se calcula el consumo de cada aparato y se compara. También se calcula qué porcentaje del total representa cada uno, porque así se ve dónde conviene actuar primero.",
        "La medición se hace sin riesgo: se leen la etiqueta del aparato y la boleta o el medidor que estén a la vista, y se anotan las horas de uso. Nunca se abren aparatos, tableros ni enchufes. La boleta muestra el total del hogar o del lugar, no el de cada aparato, así que sola no sirve para culpar a un aparato.",
    ],
    vocab=[("potencia", "energía que un aparato usa por cada hora, en vatios (W)"), ("Wh", "vatio hora: unidad de energía gastada"), ("kWh", "kilovatio hora: 1.000 Wh, unidad de la boleta"), ("consumo", "cantidad de energía que se gasta en un tiempo"), ("precio por kWh", "lo que se paga por cada kWh"), ("etiqueta", "dato impreso en el aparato que indica su potencia")],
    worked=[
        ("Calcular la energía de un aparato", "Un ventilador de ejemplo tiene 30 W y se usa 4 horas al día. ¿Cuántos Wh gasta al día?", ["Uso la fórmula: energía = potencia × horas.", "Calculo 30 × 4 = 120."], "120 Wh"),
        ("Porcentaje del total", "Un hogar de ejemplo gasta 400 Wh al día en total y el computador gasta 240 Wh. ¿Qué porcentaje es?", ["Multiplico 240 por 100: 24.000.", "Divido entre 400: 24.000 ÷ 400 = 60."], "60 %"),
    ],
    mistakes=[
        ("Multiplicar la potencia solo por los días y olvidar las horas.", "La energía depende de la potencia y del tiempo que funciona cada día.", "Escribe primero «W × horas» y luego multiplica por los días."),
        ("Culpar a un aparato porque la boleta subió.", "La boleta suma todo lo que se usa, no dice cuál aparato gastó más.", "Calcula el consumo de cada aparato con su potencia y sus horas."),
    ],
    R=[
        ("¿Qué unidad mide la energía gastada por un aparato en un tiempo? A) Wh B) W", "A", "El vatio hora combina potencia y tiempo; el vatio solo mide la potencia."),
        arith("Un cargador de ejemplo de 5 W está conectado 8 horas. ¿Cuántos Wh gasta?", "5*8", "Energía = potencia × horas.", " Wh"),
        arith("Una boleta de ejemplo indica 3 kWh. ¿A cuántos Wh equivale?", "3*1000", "Un kWh son 1.000 Wh.", " Wh"),
    ],
    C=[
        ("Para saber la potencia de un aparato sin riesgo, ¿qué se hace? A) leer la etiqueta que trae impresa B) abrirlo y mirar sus cables", "A", "La etiqueta entrega el dato sin manipular la electricidad."),
        ("Equipo P: 60 W durante 2 horas. Equipo Q: 20 W durante 5 horas. ¿Cuál gasta más energía? A) el equipo P B) el equipo Q", "A", "P gasta 60 × 2 = 120 Wh y Q gasta 20 × 5 = 100 Wh."),
        ("¿Por qué un aparato de poca potencia puede gastar más que uno de mucha potencia? A) porque puede estar encendido muchas más horas B) porque los vatios no influyen en el consumo", "A", "La energía depende de la potencia y del tiempo de uso."),
    ],
    A=[
        arith("Un curso de ejemplo consume 60 kWh al mes y el precio de ejemplo es $200 por kWh. ¿Cuánto paga?", "60*200", "Costo = kWh × precio por kWh.", " pesos"),
        ("Datos de ejemplo (W, horas al día): ampolleta 15 W, 10 h; ventilador 40 W, 5 h; radio 10 W, 8 h. ¿Cuál gasta más Wh al día?", "El ventilador", "Gasta 200 Wh; la ampolleta 150 Wh y la radio 80 Wh."),
        arith("Un ventilador de ejemplo gasta 200 Wh de un total diario de 500 Wh en una sala. ¿Qué porcentaje del total es?", "200*100//500", "Se multiplica por 100 y se divide entre el total.", " %"),
    ],
    Z=[
        ("Un estudiante dice: «El aparato de 150 W siempre gasta más que uno de 25 W». Compara 150 W durante 1 hora con 25 W durante 8 horas. ¿Es correcta su afirmación?", "No: 25 W × 8 h = 200 Wh es más que 150 W × 1 h = 150 Wh", "El tiempo de uso puede compensar la potencia."),
        ("La boleta de ejemplo de una casa marca 90 kWh en marzo y 120 kWh en abril. Un hermano dice: «Seguro fue el computador». ¿Se puede concluir eso?", "No, la boleta muestra el total de la casa y no el de cada aparato", "Para saber qué aparato gastó más hay que calcular el consumo de cada uno."),
    ],
    D=[
        arith("Un computador de ejemplo de 60 W se usa 6 horas al día. Si baja a 4 horas diarias durante 30 días, ¿cuántos Wh se ahorran?", "60*(6-4)*30", "Se calculan las horas ahorradas por día y se multiplica por la potencia y los días.", " Wh"),
        arith("Un taller de ejemplo gasta al mes: luz 180 kWh, calefacción 420 kWh y equipos 300 kWh. Quiere reducir 10 % de su consumo total. ¿Cuántos kWh debe dejar de gastar?", "(180+420+300)*10//100", "Se suma el total y se calcula el 10 %.", " kWh"),
    ],
    ctx=arith("Una ampolleta de ejemplo de 9 W queda encendida 4 horas diarias durante 30 días. ¿Cuántos Wh gasta al mes?", "9*4*30", "Se multiplican la potencia, las horas por día y los días.", " Wh"),
    sc=[
        ("¿Cuántos Wh son 2 kWh?", "2.000 Wh", "Un kWh son 1.000 Wh.", "2*1000"),
        ("¿Cómo se calcula la energía que gasta un aparato?", "Potencia en W × horas de uso", "Es la fórmula de la clase."),
        ("¿Se pueden abrir los aparatos para saber cuánto consumen?", "No, se lee la etiqueta", "Abrir aparatos o tableros es peligroso."),
    ],
    open_task=(
        "Escoge una tabla de ejemplo. Tabla 1 (W, horas al día): proyector 200 W, 3 h; computador 80 W, 5 h; parlante 20 W, 4 h. Tabla 2 (W, horas al día): estufa de ejemplo 1.000 W, 2 h; luces 100 W, 6 h; cargadores 30 W, 10 h. Calcula los Wh de cada aparato, el total, el porcentaje de cada uno y escribe dónde conviene actuar primero y por qué.",
        "Tabla 1: proyector 600 Wh, computador 400 Wh, parlante 80 Wh, total 1.080 Wh; el proyector es el mayor (cerca del 56 %), conviene actuar ahí primero",
        ["calcula bien energía y total", "calcula porcentajes", "elige dónde actuar con base en los números", "no usa mediciones que requieran abrir aparatos"],
        ["hoja con cálculos y conclusión"],
        ["olvidar las horas", "elegir por la potencia y no por el consumo"],
        "Pregunta: «¿tu elección se basa en la potencia o en los Wh totales?». Debe basarse en los Wh.",
    ),
    reinforce="Lee la etiqueta de dos aparatos de tu casa, anota la potencia, estima las horas diarias y calcula cuál gasta más en un día.",
    extend="Explica por qué dos casas con la misma boleta pueden tener aparatos que gastan de manera muy distinta.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. No se necesitan materiales especiales.",
    use="Aprenderé a recorrer el ciclo de vida de un material, a distinguir reducir, reutilizar y reciclar y a comparar opciones por su costo por uso. Sirve para encontrar en qué etapa conviene reducir el daño.",
    prior=["Sé que un material se extrae, se fabrica, se usa y se desecha.", "Sé calcular porcentajes.", "Sé dividir números enteros."],
    explain=[
        "El ciclo de vida de un material tiene cinco etapas: extracción de la materia prima, fabricación, transporte, uso y fin de vida. En cada etapa se gasta energía y puede haber residuos. Para reducir un efecto perjudicial primero se busca en qué etapa ocurre la mayor parte. A veces el mayor daño no está en el uso, sino en la fabricación o en el desecho.",
        "Las tres R ordenan las acciones. Reducir es usar menos material o energía, y es la primera porque evita el residuo antes de que exista. Reutilizar es volver a usar un objeto sin transformarlo, como llevar el mismo bidón cada día. Reciclar es transformar un residuo en materia prima para fabricar algo nuevo, y requiere separarlo y que exista un sistema que lo recolecte y lo procese.",
        "Un criterio de sustentabilidad convierte estas ideas en algo comparable. Por ejemplo, el costo por uso es el precio dividido entre las veces que se usa un objeto. Un objeto más caro pero muy duradero puede costar menos por uso que uno barato que se desecha enseguida. Un material «reciclable» solo ayuda si de verdad se recicla.",
    ],
    vocab=[("ciclo de vida", "etapas de un material: extracción, fabricación, transporte, uso y fin de vida"), ("reducir", "usar menos material o energía"), ("reutilizar", "volver a usar un objeto sin transformarlo"), ("reciclar", "transformar un residuo en materia prima nueva"), ("materia prima", "material básico que se usa para fabricar algo"), ("costo por uso", "precio dividido entre las veces que se usa")],
    worked=[
        ("Clasificar una acción", "Un taller guarda tornillos en frascos plásticos vacíos que antes tenían otro uso. ¿Qué R es?", ["El frasco se usa de nuevo sin transformarlo.", "No se usa menos material ni se funde para hacer otro."], "Reutilizar"),
        ("Costo por uso", "Una botella reutilizable de ejemplo cuesta $5.000 y se usa 250 veces. Una botella desechable cuesta $60. ¿Cuál cuesta menos por uso?", ["Reutilizable: 5.000 ÷ 250 = 20 pesos por uso.", "Desechable: 60 pesos por uso."], "La reutilizable, con $20 por uso"),
    ],
    mistakes=[
        ("Creer que reciclar es siempre mejor que reducir.", "Reciclar gasta energía y requiere un sistema; reducir evita el residuo desde el inicio.", "Primero reduce, luego reutiliza y recién después recicla."),
        ("Pensar que, si un envase se puede reciclar, no hay problema.", "Solo ayuda si se recolecta y se procesa de verdad.", "Revisa si existe un sistema que lo reciba."),
    ],
    R=[
        ("¿Qué significa reutilizar? A) volver a usar un objeto sin transformarlo B) fundirlo para fabricar otro", "A", "Reutilizar no transforma el objeto; transformarlo es reciclar."),
        ("¿En qué etapa del ciclo de vida se obtiene el material de la naturaleza? A) extracción B) fabricación", "A", "La extracción es sacar la materia prima del ambiente."),
        ("¿Cuál acción es reducir? A) comprar a granel sin envase extra B) llevar botellas plásticas a un punto de reciclaje", "A", "Reducir es usar menos material desde el principio."),
    ],
    C=[
        ("Convertir latas de aluminio usadas en materia prima para fabricar latas nuevas, ¿qué R es?", "Reciclar", "Se transforma el residuo en materia prima nueva."),
        ("¿Por qué reducir es la primera de las tres R? A) porque evita que el residuo exista B) porque transforma el residuo en materia prima nueva", "A", "Lo que no se genera no hay que reutilizar ni reciclar."),
        ("Después de la fabricación, ¿qué etapa sigue en el ciclo de vida de un material? A) el transporte y la distribución B) la extracción", "A", "Después de fabricar se lleva el producto a quien lo usará."),
    ],
    A=[
        arith("Un bidón reutilizable de ejemplo cuesta $6.000 y se usa 300 veces. ¿Cuánto cuesta cada uso?", "6000//300", "Costo por uso = precio ÷ usos.", " pesos"),
        arith("En un curso de ejemplo de 30 estudiantes cada uno bota 2 envases al día. Si 12 estudiantes llevan botella reutilizable y ya no botan envases, ¿cuántos envases se botan al día?", "(30-12)*2", "Quedan 18 estudiantes que botan 2 envases cada uno.", " envases"),
        ("Clasifica cada acción como reducir, reutilizar o reciclar: (1) imprimir por ambos lados, (2) usar frascos vacíos y limpios para guardar tornillos, (3) llevar cartones al contenedor de reciclaje.", "1 reducir, 2 reutilizar, 3 reciclar", "Usar menos papel reduce, volver a usar el frasco reutiliza y procesar el cartón recicla."),
    ],
    Z=[
        ("Un equipo dice: «Este envase es reciclable, así que no hay problema». ¿Qué falta revisar? A) si en su comuna se recolecta y se recicla de verdad B) si tiene el símbolo de reciclaje impreso", "A", "El símbolo no asegura que el envase se procese."),
        ("Bolsa de tela de ejemplo: $2.400 y 120 usos. Bolsa plástica: $30 cada uso. ¿Cuál cuesta menos por uso y por cuántos pesos?", "La de tela, por $10 por uso", "La de tela cuesta 2.400 ÷ 120 = 20 pesos por uso y la plástica 30."),
    ],
    D=[
        arith("Un taller de ejemplo bota 45 kg de material a la semana. Al reutilizar piezas baja 20 % su residuo. ¿Cuántos kg evita en 4 semanas?", "45*20//100*4", "Se calcula el 20 % de 45 y se multiplica por 4 semanas.", " kg"),
        ex("Un objeto de ejemplo tiene estas unidades de impacto, que suman 80: extracción 24, fabricación 36, transporte 8, uso 4 y fin de vida 8. ¿En qué etapa conviene actuar primero y qué porcentaje del total es?", "En la fabricación, 45 %", "Tiene el mayor valor y 36 × 100 ÷ 80 = 45.", calc="36*100//80"),
    ],
    ctx=ex("Un colegio de ejemplo usa 400 hojas al mes y solo escribe por una cara. Si escribe por las dos caras, ¿cuántas hojas necesita?", "200 hojas", "Cada hoja rinde el doble, así que se necesita la mitad: 400 ÷ 2.", calc="400//2"),
    sc=[
        ("En Tecnología: ¿qué es el ciclo de vida de un material?", "Sus etapas: extracción, fabricación, transporte, uso y fin de vida", "Es la definición de la clase."),
        ("¿Qué R se aplica primero?", "Reducir", "Evita el residuo desde el inicio."),
        ("¿Cómo se calcula el costo por uso?", "Precio ÷ veces que se usa", "Mide cuánto cuesta cada vez."),
    ],
    open_task=(
        "Escoge un objeto: Objeto 1: botella de bebida de plástico. Objeto 2: cuaderno universitario. Objeto 3: mochila escolar. Escribe sus cinco etapas del ciclo de vida, señala en cuál crees que hay más impacto y por qué, y propone una acción de reducir, una de reutilizar y una de reciclar, sin nombrar ningún producto comercial.",
        "Cuaderno: extracción de madera, fabricación de papel, transporte, uso en clases y fin de vida; más impacto en la fabricación; reducir: usar ambas caras; reutilizar: pasar hojas libres a otro cuaderno; reciclar: separar el papel al desecharlo",
        ["completa las cinco etapas", "elige una etapa y la justifica", "propone una acción de cada R", "usa términos de la clase"],
        ["hoja con las etapas y las tres acciones"],
        ["omitir una etapa", "confundir reutilizar con reciclar"],
        "Pregunta: «¿esta acción usa el objeto otra vez o lo transforma?». Con eso distingue reutilizar de reciclar.",
    ),
    reinforce="Escoge un envase de tu casa y escribe qué haces con él al terminarlo; clasifica tu acción como reducir, reutilizar, reciclar o desechar.",
    extend="Explica por qué un objeto más caro puede ser más sustentable que uno barato y qué dato necesitarías para comprobarlo.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz y los enunciados escritos en este cuaderno.",
    use="Aprenderé a escribir una necesidad con línea base, meta e indicador, a calcular metas de reducción y a revisar que la medición sea segura. Sirve para dejar la necesidad clara antes de pensar en soluciones.",
    prior=["Sé calcular porcentajes.", "Sé que una necesidad sustentable parte de un efecto perjudicial.", "Sé calcular el consumo en kWh."],
    explain=[
        "Una necesidad bien escrita dice quiénes la tienen, qué efecto perjudicial se quiere reducir, dónde ocurre, desde qué valor se parte, hasta qué valor se quiere llegar y con qué se medirá. Por ejemplo: «El gimnasio necesita reducir su consumo eléctrico de 500 a 450 kWh al mes, medido en la boleta». No nombra ninguna solución: la herramienta se elige después.",
        "La línea base es el valor de partida, medido antes de actuar. La meta es el valor al que se quiere llegar, y se puede escribir como porcentaje de reducción: meta = línea base − línea base × porcentaje ÷ 100. El indicador es la medida que permite comprobar el avance, como los kWh al mes o los kg de residuos por semana. Frases como «gastar menos» no sirven porque no se pueden comprobar.",
        "Toda necesidad tiene restricciones, que son límites que no se pueden pasar: la seguridad de las personas, el presupuesto y los permisos. Reducir el consumo no puede significar apagar luces de emergencia o alarmas. En la medición se piden solo los datos necesarios, sin nombres ni direcciones, y se leen valores que estén a la vista, como boletas, medidores y etiquetas.",
    ],
    vocab=[("línea base", "valor de partida medido antes de actuar"), ("meta", "valor al que se quiere llegar"), ("indicador", "medida que permite comprobar el avance"), ("restricción", "límite que no se puede pasar, como la seguridad o el presupuesto"), ("reducción", "disminución de un valor respecto de la línea base"), ("datos mínimos", "solo los datos que hacen falta para medir")],
    worked=[
        ("Calcular una meta", "Un taller de ejemplo parte con 600 kWh al mes y quiere reducir 15 %. ¿Cuál es la meta?", ["Calculo el 15 % de 600: 600 × 15 ÷ 100 = 90.", "Resto: 600 − 90 = 510."], "510 kWh al mes"),
        ("Revisar un enunciado", "«Los estudiantes necesitan gastar menos energía.» ¿Qué le falta?", ["No dice dónde, ni desde qué valor, ni hasta cuál.", "Tampoco tiene un indicador con el que comprobar el avance."], "Línea base, meta e indicador"),
    ],
    mistakes=[
        ("Escribir la meta como «mucho menos» o «lo más posible».", "No se puede comprobar si se cumplió.", "Escribe un valor o un porcentaje y un plazo."),
        ("Medir el consumo abriendo el tablero eléctrico.", "Es peligroso y no es necesario.", "Lee la boleta, el medidor visible o la etiqueta del aparato."),
    ],
    R=[
        ("¿Cuál enunciado es una necesidad y no una solución? A) instalar paneles en el techo B) el gimnasio necesita reducir su consumo de 500 a 450 kWh al mes", "B", "Dice qué lograr, no qué construir."),
        ("¿Cuál es un indicador medible? A) los kWh al mes de la boleta B) gastar menos", "A", "Los kWh se pueden comprobar con números."),
        ("Antes de cambiar nada, se midieron 80 kg de residuos en una semana. ¿Cómo se llama ese valor?", "Línea base", "Es el valor de partida."),
    ],
    C=[
        ("¿Qué le falta a «Los estudiantes necesitan gastar menos energía»? A) una cifra de partida y una meta con plazo B) el nombre de la herramienta que se usará", "A", "La necesidad no nombra la herramienta; sí necesita línea base y meta."),
        ("¿Cuál es una forma segura de medir el consumo de un curso? A) leer el medidor que está a la vista B) abrir el tablero para ver los cables", "A", "Leer no expone a ningún riesgo eléctrico."),
        ("Una ficha pide nombre y dirección de cada estudiante para registrar el consumo de las salas. ¿Qué conviene hacer? A) registrar solo el consumo por sala B) mantener nombre y dirección para poder comparar", "A", "Se aplica el principio de datos mínimos."),
    ],
    A=[
        arith("Un liceo de ejemplo parte con 840 kWh al mes y quiere reducir 25 %. ¿Cuál es la meta?", "840-840*25//100", "Se calcula el 25 % de 840 y se resta.", " kWh"),
        arith("Una casa de ejemplo bajó su consumo de 360 a 288 kWh. ¿Qué porcentaje redujo?", "(360-288)*100//360", "Se calcula la diferencia, se multiplica por 100 y se divide entre la línea base.", " %"),
        arith("Una escuela de ejemplo bota 90 kg de residuos en la semana 1 y baja 6 kg cada semana. ¿Cuántos kg botará en la semana 5?", "90-6*4", "Hay 4 semanas de baja entre la semana 1 y la 5.", " kg"),
    ],
    Z=[
        arith("Un equipo bajó de 500 a 450 kWh y dice: «Logramos 50 % de reducción». ¿Cuál es el porcentaje real?", "(500-450)*100//500", "El 50 es la diferencia en kWh, no el porcentaje: se divide entre la línea base.", " %"),
        ("Un liceo quiere reducir 20 % su consumo y propone apagar el sistema de alarmas y las luces de emergencia. ¿Debe incluirse esa medida?", "No, porque la seguridad es una restricción", "Reducir consumo no puede poner en riesgo a las personas."),
    ],
    D=[
        arith("La línea base de un edificio de ejemplo es 720 kWh al mes y su meta es bajar 20 % en 4 meses, con la misma baja cada mes. ¿Cuántos kWh debe bajar cada mes?", "720*20//100//4", "Primero se calcula la baja total y luego se reparte en 4 meses.", " kWh"),
        ("Lista de revisión: quiénes, efecto, línea base, meta, indicador y ninguna solución nombrada. Enunciado: «El curso necesita bajar sus residuos de 50 a 40 kg por semana, medidos con el pesaje del lunes, usando contenedores nuevos». ¿Qué criterio incumple?", "No nombrar ninguna solución", "Menciona los contenedores nuevos, que son una solución."),
    ],
    ctx=ex("Un casino escolar de ejemplo bota 60 kg de residuos orgánicos a la semana y quiere llegar a 45. ¿Qué porcentaje de reducción es?", "25 %", "La diferencia es 15 kg y 15 × 100 ÷ 60 = 25.", calc="15*100//60"),
    sc=[
        ("En Tecnología: ¿qué es la línea base?", "El valor de partida medido antes de actuar", "Sirve para saber cuánto se logró."),
        ("En Tecnología: ¿Qué es un indicador?", "Una medida que permite comprobar el avance", "Convierte la meta en algo comparable."),
        ("¿Una necesidad puede nombrar la solución?", "No, la solución se elige después", "Nombrarla limita el diseño."),
    ],
    open_task=(
        "Escoge un caso de ejemplo. Caso 1: un taller gasta 420 kWh al mes y quiere reducir 10 %. Caso 2: un casino bota 75 kg de residuos a la semana y quiere reducir 20 %. Caso 3: un liceo usa 2.000 hojas de papel al mes y quiere reducir 25 %. Escribe la necesidad en una o dos oraciones con quiénes, efecto, línea base, meta numérica, indicador, una restricción y sin nombrar la solución.",
        "Caso 1: «El taller necesita reducir su consumo eléctrico de 420 a 378 kWh al mes, medido en la boleta; sin apagar equipos de seguridad»",
        ["incluye línea base y meta correctas", "indica el indicador", "señala una restricción", "no nombra la solución"],
        ["necesidad redactada con sus cálculos"],
        ["escribir una meta sin cifra", "nombrar la solución en la necesidad"],
        "Pregunta: «¿cómo comprobarías con un número que se logró la meta?». Si no puede, pídele agregar el indicador.",
    ),
    reinforce="Escribe una necesidad sobre el consumo de agua, energía o papel de tu casa o tu curso, con línea base y meta inventadas de ejemplo.",
    extend="Explica por qué una buena necesidad no debe nombrar la solución y cómo cambiaría el diseño si la nombra.",
)

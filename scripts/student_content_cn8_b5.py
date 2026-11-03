"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 15 (elementos químicos frecuentes y soporte de la vida)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA15 = "CN08 OA 15"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 15, clase 1
register(
    OA15, 1,
    materials="Papel y lápiz. Todos los datos están escritos en el cuaderno. Si quieres, puedes pesar una hoja fresca en una balanza de cocina con ayuda de una persona de tu casa.",
    use="Aprenderé cuáles son los cuatro elementos más comunes en los seres vivos (carbono, hidrógeno, oxígeno y nitrógeno) y a formular preguntas investigables sobre ellos. Sirve para entender de qué está hecha la vida.",
    prior=["Sé qué es un elemento y un compuesto.", "Conozco algunos símbolos químicos y fórmulas como H2O y CO2."],
    explain=[
        "Los seres vivos están formados sobre todo por cuatro elementos: carbono (C), hidrógeno (H), oxígeno (O) y nitrógeno (N), que se conocen como CHON. Son frecuentes en la Tierra y forman las moléculas de la vida. El agua tiene H y O. Los glúcidos (azúcares) y los lípidos (grasas) tienen C, H y O. Las proteínas tienen C, H, O y N. Los ácidos nucleicos, como el ADN, también.",
        "Se dice que estos elementos son soporte para la vida porque con ellos se construyen las moléculas que forman las células y que realizan sus funciones. En el cuerpo humano, por masa y de forma aproximada, el oxígeno es cerca del 65 %, el carbono el 18 %, el hidrógeno el 10 % y el nitrógeno el 3 %.",
        "Una pregunta investigable sobre estos elementos debe poder responderse con una medición. «¿Qué porcentaje de la masa de una hoja se pierde al secarla durante cinco días?» es investigable porque se pesa la hoja fresca y la seca. «¿Qué elemento es el más importante?» no lo es, porque «importante» no se mide.",
    ],
    vocab=[("CHON", "sigla de carbono, hidrógeno, oxígeno y nitrógeno"), ("biomolécula", "molécula formada por los seres vivos, como un azúcar o una proteína"), ("proteína", "biomolécula con C, H, O y N que cumple funciones en la célula"), ("porcentaje", "parte de cada 100"), ("elemento frecuente", "elemento que se encuentra en gran cantidad")],
    worked=[
        {"title": "Contar CHON en una fórmula", "problem": "La glicina, una biomolécula, tiene la fórmula C2H5NO2. ¿Qué elementos CHON tiene?", "steps": ["Hay C (carbono), H (hidrógeno), N (nitrógeno) y O (oxígeno) en la fórmula.", "Están los cuatro elementos CHON."], "answer": "Los cuatro: C, H, N y O"},
        {"title": "Porcentaje de agua en una hoja", "problem": "En una medición de ejemplo, una hoja fresca pesa 10 g y seca pesa 3 g. ¿Qué porcentaje de su masa era agua?", "steps": ["Agua perdida = 10 − 3 = 7 g.", "7 de cada 10 g es 70 de cada 100."], "answer": "70 %"},
    ],
    mistakes=[
        {"wrong": "Decir que el oxígeno del cuerpo viene solo del aire que se respira.", "why": "Se piensa en el gas O2 y no en el oxígeno que hay en el agua y en las biomoléculas.", "fix": "El oxígeno del cuerpo está sobre todo en el agua y en otras moléculas."},
        {"wrong": "Creer que, si una hoja se seca, deja de tener H y O.", "why": "Se confunde perder agua con perder todo el hidrógeno y el oxígeno.", "fix": "La hoja seca aún tiene C, H y O en sus glúcidos y otras moléculas."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuáles son los cuatro elementos de la sigla CHON?", "Carbono, hidrógeno, oxígeno y nitrógeno", "Cada letra es el símbolo de un elemento."),
            ex("En el cuerpo humano, por masa, ¿cuál es el elemento más abundante: el carbono o el oxígeno?", "El oxígeno", "El oxígeno es cerca del 65 % y el carbono cerca del 18 %."),
            ex("¿Qué símbolo químico tiene el nitrógeno?", "N", "Es la inicial de su nombre."),
        ],
        "understand": [
            ex("¿Cuál es una pregunta investigable? A) ¿Qué porcentaje de la masa de una hoja se pierde al secarla durante cinco días?; B) ¿Qué elemento es el más importante?", "A)", "Se puede responder pesando la hoja antes y después."),
            ex("El agua es H2O. ¿Qué dos elementos CHON aporta?", "Hidrógeno y oxígeno", "Esos son los elementos de su fórmula."),
            ex("El aire tiene cerca de 78 % de N2. ¿Qué elemento CHON es?", "El nitrógeno", "N2 está formado por dos átomos de nitrógeno."),
        ],
        "apply": [
            arith("Una hoja fresca pesa 20 g y, seca, pesa 6 g (datos de ejemplo). ¿Cuántos gramos de agua perdió?", "20-6", "Se resta la masa seca a la fresca.", " g"),
            arith("Con los mismos datos de ejemplo, la hoja perdió 14 g de 20 g. ¿Qué porcentaje de su masa perdió?", "14*100//20", "Se divide la masa perdida por la masa total y se multiplica por 100.", " %"),
            arith("Una persona de 50 kg tiene aproximadamente 18 % de carbono. ¿Cuántos kilogramos de carbono son?", "50*18//100", "Se calcula el porcentaje de la masa total.", " kg"),
        ],
        "reason": [
            ex("Santiago dice que la hoja seca «ya no tiene hidrógeno ni oxígeno» porque perdió agua. ¿Cómo lo corriges?", "Aún tiene C, H y O en sus glúcidos y otras moléculas", "Perder agua no elimina esos elementos de las biomoléculas."),
            ex("Una persona de 60 kg tiene aproximadamente 65 % de oxígeno. Alguien dice que ese oxígeno es todo gas O2. ¿Qué responderías?", "Que está sobre todo en el agua y en otras moléculas, no como gas O2", "El oxígeno forma parte de H2O y de biomoléculas."),
        ],
        "challenge": [
            arith("Una persona de 60 kg tiene aproximadamente 65 % de oxígeno. ¿Cuántos kilogramos de oxígeno son?", "60*65//100", "Se calcula el porcentaje de la masa total.", " kg"),
            ex("La glucosa es C6H12O6. ¿Cuántos elementos CHON tiene y cuál falta?", "Tres: C, H y O; falta el N", "En la fórmula no aparece el nitrógeno."),
        ],
    },
    context=[ex("Una bolsa de abono para plantas indica que contiene nitrógeno. ¿Qué biomolécula de las plantas necesita ese nitrógeno?", "Las proteínas", "Las proteínas tienen C, H, O y N.")],
    selfcheck=[
        ex("¿Qué biomoléculas tienen nitrógeno: los glúcidos o las proteínas?", "Las proteínas", "Los glúcidos solo tienen C, H y O."),
        ex("¿Qué dos elementos tiene el agua?", "Hidrógeno y oxígeno", "Su fórmula es H2O."),
        ex("¿Qué es una pregunta investigable?", "La que se puede responder con una medición", "Debe tener algo que medir."),
    ],
    open_task=task(
        "Datos de ejemplo: en tres hojas, la masa fresca y la seca fueron: hoja 1, 12 g y 4 g; hoja 2, 15 g y 5 g; hoja 3, 20 g y 6 g. Calcula cuántos gramos de agua perdió cada una y el porcentaje de agua redondeado. Luego formula una pregunta investigable sobre otra parte de la planta, como una raíz o un tallo, indicando qué mides y qué mantienes igual.",
        "Hoja 1: perdió 8 g, 67 %. Hoja 2: perdió 10 g, 67 %. Hoja 3: perdió 14 g, 70 %. Pregunta: ¿Qué porcentaje de su masa pierde un tallo de 20 g al secarse cinco días en el mismo lugar?",
        ["tres cálculos de pérdida", "tres porcentajes", "pregunta con algo que medir y variables iguales"],
        ["tabla de tres filas", "pregunta escrita"],
        ["olvidar restar la masa seca", "pregunta que no se pueda medir"],
        "Pregunta qué elementos CHON seguirá teniendo la hoja seca.",
    ),
    reinforce="Escribe los cuatro elementos CHON con su símbolo y una molécula de la vida donde aparecen.",
    extend="Con una persona de tu casa, busquen en una etiqueta de alimento si menciona proteínas y anoten cuánta cantidad indica.",
)

# ================================================================ OA 15, clase 2
register(
    OA15, 2,
    materials="Papel y lápiz. Las tablas de datos de ejemplo están escritas en el cuaderno.",
    use="Aprenderé a leer tablas de composición del cuerpo humano, de la corteza terrestre y del aire para argumentar con evidencia. Sirve para ver qué elementos son comunes en la Tierra y en los seres vivos.",
    prior=["Sé qué son C, H, O y N.", "Sé calcular un porcentaje."],
    explain=[
        "Los datos siguientes son valores aproximados de referencia. Cuerpo humano, por masa: O 65 %, C 18 %, H 10 %, N 3 %, otros 4 %. Corteza terrestre, por masa: O 46 %, Si 28 %, Al 8 %, Fe 5 %, otros 13 %. Aire seco, por volumen: N2 78 %, O2 21 %, otros 1 %. Los otros incluyen al carbono del CO2, que está en una cantidad pequeña.",
        "Al comparar tablas se buscan patrones. El oxígeno es muy abundante en la corteza y en el cuerpo. El nitrógeno es el gas principal del aire. El carbono es poco abundante en la corteza, pero el cuerpo lo concentra: 18 %. El silicio es el segundo más abundante en la corteza y no es uno de los cuatro principales del cuerpo. Entonces la abundancia en la Tierra no basta para ser soporte de la vida: los seres vivos usan elementos que forman moléculas útiles.",
        "No se pueden sumar sin cuidado porcentajes de tablas distintas, porque unas son por masa y otras por volumen. Y una tabla de promedios no describe a todas las personas ni a todas las rocas.",
    ],
    vocab=[("composición", "qué elementos hay y en qué cantidad"), ("por masa", "porcentaje medido con la masa de cada elemento"), ("por volumen", "porcentaje medido con el espacio que ocupa cada gas"), ("corteza terrestre", "capa sólida más externa de la Tierra"), ("aire seco", "aire sin vapor de agua")],
    worked=[
        {"title": "Sumar los CHON del cuerpo", "problem": "Con los valores aproximados del cuerpo humano, ¿qué porcentaje de la masa forman C, H, O y N juntos?", "steps": ["O + C + H + N = 65 + 18 + 10 + 3.", "La suma es 96."], "answer": "Cerca del 96 %"},
        {"title": "Comparar el silicio", "problem": "El silicio es 28 % de la corteza y no está entre los cuatro principales del cuerpo. ¿Qué conclusión se apoya en el dato?", "steps": ["Un elemento muy abundante en la corteza no siempre es abundante en los seres vivos.", "Los seres vivos usan sobre todo C, H, O y N."], "answer": "La abundancia en la Tierra no basta para ser soporte de la vida"},
    ],
    mistakes=[
        {"wrong": "Sumar el 78 % del aire (por volumen) con el 65 % del cuerpo (por masa).", "why": "Se suman cantidades medidas de modo distinto.", "fix": "Compara cada tabla con sus propias unidades."},
        {"wrong": "Concluir que el carbono es poco importante porque es poco abundante en la corteza.", "why": "Se ignora que el cuerpo lo concentra.", "fix": "Mira también el dato del cuerpo: 18 %."},
    ],
    tiers={
        "recovery": [
            ex("Cuerpo humano, por masa (valores aproximados): O 65 %, C 18 %, H 10 %, N 3 %, otros 4 %. ¿Qué elemento es el más abundante?", "El oxígeno", "Es el mayor porcentaje de la tabla."),
            ex("En la misma composición del cuerpo humano (O 65 %, C 18 %, H 10 %, N 3 %), ¿qué elemento CHON es el menos abundante?", "El nitrógeno", "Con 3 % es el menor de los cuatro."),
            arith("Cuerpo humano, por masa: O 65 %, C 18 %, H 10 %, N 3 %. ¿Qué porcentaje suman los cuatro?", "65+18+10+3", "Se suman los cuatro porcentajes.", " %"),
        ],
        "understand": [
            ex("Corteza terrestre, por masa: O 46 %, Si 28 %, Al 8 %, Fe 5 %, otros 13 %. ¿Cuál de esos cuatro elementos también es uno de los CHON?", "El oxígeno", "Es el único de la lista que está en CHON."),
            arith("Aire seco, por volumen: N2 78 %, O2 21 %, otros 1 %. ¿Qué porcentaje del aire es N2 u O2?", "78+21", "Se suman los dos gases principales.", " %"),
            ex("El silicio es 28 % de la corteza y no es uno de los cuatro principales del cuerpo. ¿Qué indica?", "Que ser abundante en la Tierra no basta para ser soporte de la vida", "Los seres vivos usan sobre todo C, H, O y N."),
        ],
        "apply": [
            arith("Cuerpo humano: O 65 %, C 18 %, H 10 % y N 3 %. ¿Qué porcentaje queda para los otros elementos?", "100-(65+18+10+3)", "Se resta la suma de los cuatro a 100.", " %"),
            arith("El oxígeno es 65 % del cuerpo y 46 % de la corteza. ¿Cuántos puntos porcentuales más hay en el cuerpo?", "65-46", "Se resta el porcentaje menor al mayor.", " puntos"),
            arith("Una persona de 80 kg tiene aproximadamente 10 % de hidrógeno. ¿Cuántos kilogramos de hidrógeno son?", "80*10//100", "Se calcula el 10 % de 80 kg.", " kg"),
        ],
        "reason": [
            ex("Laura dice que, como el silicio es el segundo más abundante en la corteza, debe ser clave para los seres vivos. ¿Qué dato de la tabla del cuerpo la contradice?", "El silicio no está entre los cuatro elementos principales del cuerpo", "Los datos del cuerpo no lo muestran entre los principales."),
            ex("El carbono es menos de 1 % de la corteza y 18 % del cuerpo. ¿Qué conclusión es correcta? A) Los seres vivos concentran carbono más que su entorno; B) El carbono no es importante en los seres vivos", "A)", "El cuerpo tiene mucho más carbono que la corteza."),
        ],
        "challenge": [
            ex("¿Por qué no conviene sumar el 78 % de N2 del aire con el 65 % de oxígeno del cuerpo?", "Porque uno es por volumen y el otro por masa", "Las unidades de medida son distintas."),
            ex("Una persona dice «yo soy 65 % oxígeno, que es un gas». ¿En qué forma está ese oxígeno principalmente?", "En el agua y en otras moléculas, no como gas O2", "El cuerpo contiene mucha agua y biomoléculas con oxígeno."),
        ],
    },
    context=[ex("La tabla del aire dice N2 78 %, O2 21 %. Un estudiante concluye que el aire casi no tiene dióxido de carbono. ¿Qué dato apoya esa conclusión?", "Que todos los otros gases juntos son solo 1 %", "El CO2 está dentro de ese 1 % o menos.")],
    selfcheck=[
        ex("¿Qué elemento es el gas más abundante del aire?", "El nitrógeno", "N2 es el 78 %."),
        ex("¿Los porcentajes de una tabla por masa y otra por volumen se pueden sumar directamente?", "No", "Unos miden masa y otros volumen."),
        ex("¿Qué elemento de los cuatro CHON es también el más abundante en la corteza?", "El oxígeno", "Es 46 % de la corteza."),
    ],
    open_task=task(
        "Con las tres tablas de la explicación (cuerpo, corteza y aire), redacta una conclusión de tres frases que responda: ¿qué elementos CHON son comunes en la Tierra y en los seres vivos? Cita al menos tres datos con su porcentaje, señala un elemento que sea abundante en la Tierra pero no en los seres vivos y escribe una limitación de comparar las tablas.",
        "El oxígeno es 46 % de la corteza y 65 % del cuerpo. El nitrógeno es 78 % del aire y 3 % del cuerpo. El silicio es 28 % de la corteza pero no está entre los principales del cuerpo. Limitación: son valores aproximados y no todas son por masa.",
        ["tres datos con porcentaje", "un elemento abundante solo en la Tierra", "una limitación"],
        ["conclusión de tres frases"],
        ["sumar porcentajes de tablas distintas", "no citar datos"],
        "Pregunta qué dato nuevo ayudaría a comparar mejor los elementos.",
    ),
    reinforce="Escribe una oración que explique por qué la abundancia en la corteza no basta para ser soporte de la vida.",
    extend="Con una persona de tu casa, comenten por qué creen que el cuerpo tiene tanto oxígeno, y escriban lo que respondan.",
)

# ================================================================ OA 15, clase 3
register(
    OA15, 3,
    materials="Papel y lápiz. Las fórmulas están escritas en el cuaderno.",
    use="Aprenderé el modelo de enlaces de C, H, O y N y cómo se arman las moléculas de la vida. Sirve para comprobar si una molécula dibujada es posible y para explicar por qué el carbono es tan especial.",
    prior=["Conozco el enlace covalente.", "Sé contar átomos en una fórmula."],
    explain=[
        "Cada átomo forma un número característico de enlaces covalentes. El hidrógeno forma 1, el oxígeno forma 2, el nitrógeno forma 3 y el carbono forma 4. Con esas reglas se arman moléculas: H2O (O con dos H), NH3 (N con tres H), CH4 (C con cuatro H) y CO2 (O=C=O, donde cada doble línea cuenta como dos enlaces, así que el C tiene 4 en total).",
        "El carbono es especial porque, además de sus cuatro enlaces, puede unirse consigo mismo y formar cadenas largas y anillos. Esto permite una enorme variedad de moléculas. La glucosa, C6H12O6, tiene 6 átomos de C, 12 de H y 6 de O. La glicina, un componente de proteínas, es C2H5NO2.",
        "Un modelo de moléculas debe respetar el número de enlaces de cada átomo. Si un átomo de C aparece con cinco líneas, el modelo está mal. Como todo modelo, simplifica: no muestra la forma real en tres dimensiones.",
    ],
    vocab=[("valencia de enlace", "número de enlaces que forma un átomo"), ("cadena de carbono", "átomos de carbono unidos uno tras otro"), ("anillo", "cadena de átomos que se cierra sobre sí misma"), ("glucosa", "azúcar con fórmula C6H12O6"), ("doble enlace", "unión de dos átomos con dos líneas")],
    worked=[
        {"title": "Comprobar una molécula", "problem": "¿Es posible la molécula CH5?", "steps": ["El carbono forma 4 enlaces.", "CH5 necesitaría 5 H unidos a un C, que son 5 enlaces."], "answer": "No es posible: el carbono forma 4 enlaces"},
        {"title": "Átomos de una molécula", "problem": "¿Cuántos átomos tiene una molécula de glicina, C2H5NO2?", "steps": ["Se suman los subíndices: 2 + 5 + 1 + 2.", "El total es 10."], "answer": "10 átomos"},
    ],
    mistakes=[
        {"wrong": "Dibujar un carbono con cinco líneas.", "why": "No se respeta el número de enlaces del carbono.", "fix": "El carbono forma exactamente cuatro enlaces."},
        {"wrong": "Creer que el modelo muestra la forma real de la molécula.", "why": "Se toma una representación plana como real.", "fix": "El dibujo solo muestra qué átomos están unidos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos enlaces forma un átomo de carbono?", "4", "Es su característica principal."),
            ex("¿Cuántos enlaces forma un átomo de oxígeno?", "2", "Por eso une dos H en el agua."),
            ex("¿Cuántos enlaces forma un átomo de nitrógeno?", "3", "Por eso tiene tres H en NH3."),
        ],
        "understand": [
            ex("¿Por qué el carbono permite tantas moléculas distintas?", "Porque forma 4 enlaces y se une consigo mismo en cadenas y anillos", "Esa versatilidad produce muchísimas moléculas."),
            ex("En el modelo O=C=O, ¿cuántos enlaces (líneas) salen del carbono?", "4", "Cada doble línea cuenta como dos enlaces."),
            ex("¿Qué fórmula tiene una molécula con un átomo de N unido a tres de H?", "NH3", "El nitrógeno forma 3 enlaces."),
        ],
        "apply": [
            arith("La glucosa es C6H12O6. ¿Cuántos átomos tiene una molécula?", "6+12+6", "Se suman los subíndices.", " átomos"),
            arith("¿Cuántos átomos de H hay en 3 moléculas de NH3?", "3*3", "Cada molécula tiene 3 átomos de H.", " átomos"),
            arith("En la cadena C–C–C–C, el carbono del medio está unido a otros dos carbonos. ¿Cuántos H necesita para completar sus cuatro enlaces?", "4-2", "Se resta lo ya enlazado al total de enlaces del carbono.", " H"),
        ],
        "reason": [
            ex("Un estudiante dibuja un carbono con cinco líneas. ¿Qué error cometió?", "El carbono solo forma 4 enlaces", "Cinco líneas no respetan su número de enlaces."),
            ex("Un estudiante dibuja un átomo de hidrógeno con dos líneas de enlace. ¿Es posible según las reglas de la clase? Responde sí o no.", "No", "El hidrógeno forma un solo enlace."),
        ],
        "challenge": [
            arith("El propano tiene 3 carbonos en cadena: los dos extremos con 3 H cada uno y el del medio con 2 H. ¿Cuántos H tiene en total?", "3+2+3", "Se suman los H de los tres carbonos.", " H"),
            ex("Compara CH4 (5 átomos) y C2H6 (8 átomos). ¿Qué muestra sobre las cadenas de carbono?", "Al unir más carbonos se forman moléculas mayores y distintas", "El carbono permite alargar la molécula."),
        ],
    },
    context=[ex("La glucosa es el azúcar que usan las células. ¿Qué elementos CHON tiene?", "C, H y O", "Su fórmula es C6H12O6, sin nitrógeno.")],
    selfcheck=[
        ex("¿Cuántos enlaces forma el hidrógeno?", "1", "Por eso une un solo átomo."),
        ex("¿Qué forma el carbono además de enlaces con otros átomos?", "Cadenas y anillos de carbono", "Se une consigo mismo."),
        ex("¿Un modelo muestra la forma real de la molécula?", "No, simplifica", "Solo muestra qué átomos están unidos."),
    ],
    open_task=task(
        "Dibuja con líneas estas moléculas respetando los enlaces: (a) H2O; (b) NH3; (c) CH4. Cuenta cuántas líneas salen de cada átomo central. Luego comprueba con las reglas de enlaces si es posible una molécula con 1 carbono y 3 hidrógenos y explica en una frase qué le falta.",
        "(a) H–O–H, el O tiene 2 líneas. (b) N con 3 líneas hacia H. (c) C con 4 líneas hacia H. CH3 no es posible como molécula completa: al carbono le falta un enlace.",
        ["tres dibujos correctos", "cuenta de líneas", "CH3 comprobada con la regla"],
        ["dibujos", "frase"],
        ["dibujar cinco líneas en el carbono", "olvidar el átomo central"],
        "Pregunta cuántos H necesitaría un carbono con dos enlaces ya ocupados.",
    ),
    reinforce="Escribe una tabla con átomo y número de enlaces para H, O, N y C.",
    extend="Con una persona de tu casa, construyan una molécula de metano con bolitas de plasticina y palitos de fideos sin cocer, y expliquen la limitación del modelo.",
)

# ================================================================ OA 15, clase 4
register(
    OA15, 4,
    materials="Papel y lápiz. La ecuación y los datos están escritos en el cuaderno.",
    use="Aprenderé a relacionar variables en la fotosíntesis y la respiración celular y a seguir los átomos de C, H y O en ellas. Sirve para explicar cómo los elementos pasan del ambiente a los seres vivos.",
    prior=["Sé balancear una ecuación contando átomos.", "Sé que las plantas hacen fotosíntesis."],
    explain=[
        "En la fotosíntesis, las plantas usan luz para transformar dióxido de carbono (CO2) y agua (H2O) en glucosa (C6H12O6) y oxígeno (O2). La ecuación balanceada es 6 CO2 + 6 H2O → C6H12O6 + 6 O2. A cada lado hay 6 átomos de C, 12 de H y 18 de O: los átomos se conservan, solo se reordenan.",
        "En la respiración celular ocurre el proceso inverso: la glucosa reacciona con oxígeno y libera CO2 y H2O y la energía que usa la célula: C6H12O6 + 6 O2 → 6 CO2 + 6 H2O. Así el carbono pasa del aire a los seres vivos y vuelve al aire.",
        "Una investigación puede relacionar variables. Si una planta acuática recibe más luz, produce más burbujas de oxígeno. Los datos de ejemplo son: lámpara a 10 cm, 24 burbujas por minuto; a 20 cm, 12; a 40 cm, 6. Las burbujas son una evidencia indirecta de la fotosíntesis, y para comparar bien se mantienen iguales la planta, la temperatura del agua y el tiempo.",
    ],
    vocab=[("fotosíntesis", "proceso en que las plantas fabrican glucosa y oxígeno con luz, CO2 y agua"), ("respiración celular", "proceso en que la célula obtiene energía de la glucosa usando oxígeno"), ("reactante", "sustancia que reacciona"), ("producto", "sustancia que se forma"), ("evidencia indirecta", "dato del que se infiere un proceso que no se ve")],
    worked=[
        {"title": "Contar átomos de C en la fotosíntesis", "problem": "¿Cuántos átomos de C hay en 6 CO2 y cuántos en C6H12O6?", "steps": ["6 CO2 tiene 6 × 1 = 6 átomos de C.", "C6H12O6 tiene 6 átomos de C."], "answer": "6 en cada lado: el carbono se conserva"},
        {"title": "Leer una relación en datos", "problem": "Con una lámpara a 10 cm hay 24 burbujas por minuto y a 20 cm hay 12. ¿Qué relación se observa?", "steps": ["Al duplicar la distancia, las burbujas bajan a la mitad.", "A mayor distancia hay menos luz y menos fotosíntesis."], "answer": "A mayor distancia de la lámpara, menos burbujas"},
    ],
    mistakes=[
        {"wrong": "Decir que las plantas no respiran porque hacen fotosíntesis.", "why": "Se confunden los dos procesos.", "fix": "Las plantas hacen fotosíntesis y también respiración celular."},
        {"wrong": "Contar solo los átomos de un producto para comprobar el balance.", "why": "No se suman todos los productos.", "fix": "Se suman los átomos de cada elemento en todos los productos."},
    ],
    tiers={
        "recovery": [
            ex("En la fotosíntesis, ¿qué sustancia se libera al aire?", "Oxígeno (O2)", "Es el gas que se produce junto con la glucosa."),
            ex("¿Qué sustancia aporta hidrógeno para formar la glucosa en la fotosíntesis?", "El agua", "H2O es la fuente de hidrógeno."),
            ex("¿Qué elementos CHON tiene el dióxido de carbono?", "Carbono y oxígeno", "Su fórmula es CO2."),
        ],
        "understand": [
            arith("En 6 CO2 + 6 H2O, ¿cuántos átomos de oxígeno hay en los reactantes?", "6*2+6*1", "Cada CO2 aporta 2 y cada H2O aporta 1.", " átomos"),
            arith("En los productos C6H12O6 + 6 O2, ¿cuántos átomos de oxígeno hay?", "6+6*2", "La glucosa aporta 6 y cada O2 aporta 2.", " átomos"),
            arith("En los reactantes 6 CO2 + 6 H2O, ¿cuántos átomos de hidrógeno hay? Compáralos con los 12 H de la glucosa C6H12O6.", "6*2", "Solo el agua aporta hidrógeno: 6 moléculas con 2 H cada una; coincide con los 12 H de la glucosa, así que el hidrógeno se conserva.", " átomos"),
        ],
        "apply": [
            arith("Con la lámpara a 10 cm hay 24 burbujas por minuto y a 40 cm hay 6. ¿Cuántas más hay a 10 cm que a 40 cm?", "24-6", "Se resta el menor al mayor.", " burbujas"),
            ex("Al alejar la lámpara de la planta, ¿las burbujas por minuto aumentan o disminuyen?", "Disminuyen", "La luz que llega es menor."),
            arith("Si el patrón es que las burbujas bajan a la mitad al duplicar la distancia, ¿cuántas habría a 80 cm si a 40 cm hay 6?", "6//2", "Se divide por 2 al duplicar la distancia.", " burbujas"),
        ],
        "reason": [
            ex("Para comparar justamente las distancias, ¿qué debe mantenerse igual? A) La misma planta, la misma temperatura del agua y el mismo tiempo de conteo; B) Una planta distinta en cada distancia y tiempos distintos", "A)", "Solo cambia la distancia a la lámpara."),
            ex("En la respiración celular C6H12O6 + 6 O2 → 6 CO2 + 6 H2O, ¿cuántas moléculas de O2 se consumen por cada molécula de glucosa?", "6", "El coeficiente delante del O2 es 6."),
        ],
        "challenge": [
            arith("Si una planta usa 12 moléculas de CO2 en la fotosíntesis, ¿cuántas moléculas de glucosa se forman si se necesitan 6 CO2 para cada una?", "12//6", "Se divide el CO2 usado entre 6.", " moléculas"),
            ex("Con esas 12 moléculas de CO2, ¿cuántas moléculas de O2 se liberan si por cada CO2 se libera un O2?", "12", "En la ecuación 6 CO2 producen 6 O2, la misma cantidad."),
        ],
    },
    context=[ex("Un acuario tiene una planta acuática junto a una ventana. ¿Por qué la luz ayuda a los peces?", "Porque la planta hace fotosíntesis y libera oxígeno al agua", "El oxígeno liberado disuelto beneficia la respiración de los peces.")],
    selfcheck=[
        ex("¿Qué se necesita para hacer fotosíntesis además de CO2 y agua?", "Luz", "Es la fuente de energía del proceso."),
        ex("¿Qué proceso libera CO2 y H2O desde la glucosa?", "La respiración celular", "Es el proceso inverso de la fotosíntesis."),
        ex("¿Por qué las burbujas son una evidencia indirecta?", "Porque muestran un efecto de la fotosíntesis sin verla directamente", "Se infiere el proceso desde las burbujas."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo de una planta acuática: lámpara a 10 cm, 30 burbujas por minuto; a 20 cm, 15; a 30 cm, 10; a 60 cm, 5. (1) Ordena los datos en una tabla. (2) Describe en una frase la relación entre distancia y burbujas. (3) Escribe tres variables que mantendrías iguales. (4) Comprueba que 6 CO2 + 6 H2O → C6H12O6 + 6 O2 conserva los átomos de C.",
        "(2) A mayor distancia, menos burbujas. (3) Misma planta, misma temperatura del agua y mismo tiempo de conteo. (4) Hay 6 C en 6 CO2 y 6 C en la glucosa.",
        ["tabla", "relación descrita", "tres variables controladas", "conteo de C"],
        ["tabla y frases", "conteo escrito"],
        ["decir que más distancia da más burbujas", "olvidar variables controladas"],
        "Pregunta qué cambio harías para saber si el tipo de luz afecta las burbujas.",
    ),
    reinforce="Escribe la ecuación de la fotosíntesis con palabras, de reactantes a productos.",
    extend="Con una persona de tu casa, miren una planta de interior y comenten hacia dónde se inclina y por qué creen que lo hace.",
)

# ================================================================ OA 15, clase 5
register(
    OA15, 5,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a explicar con evidencia cómo circulan el carbono y el nitrógeno entre el ambiente y los seres vivos. Sirve para argumentar por qué estos elementos son soporte de la vida y cuáles son los límites de esa afirmación.",
    prior=["Conozco la fotosíntesis y la respiración celular.", "Sé que el aire tiene mucho nitrógeno."],
    explain=[
        "El carbono circula así: las plantas toman CO2 del aire en la fotosíntesis, los animales obtienen carbono al comer plantas o a otros animales, y la respiración y la descomposición devuelven CO2 al aire. El hidrógeno y el oxígeno circulan sobre todo con el agua, que evapora, llueve y las plantas absorben.",
        "El nitrógeno del aire (N2) es muy abundante, pero casi ningún ser vivo puede usarlo directamente. Algunas bacterias del suelo y de las raíces de las leguminosas, como los porotos, lo transforman en compuestos que las plantas absorben. Los animales obtienen nitrógeno al comer, y los descomponedores devuelven compuestos al suelo.",
        "Para argumentar, se usa afirmación, evidencia y razonamiento. Una afirmación como «CHON son soporte para la vida» se apoya en que forman las biomoléculas y el agua. Pero no es toda la historia: otros elementos, como el fósforo de los ácidos nucleicos, también son necesarios. Una buena conclusión dice lo que los datos permiten y reconoce lo que falta.",
    ],
    vocab=[("ciclo del carbono", "recorrido del carbono entre el aire y los seres vivos"), ("fijación de nitrógeno", "transformación del N2 en compuestos que las plantas pueden usar"), ("descomponedor", "ser vivo que degrada restos y devuelve materia al ambiente"), ("leguminosa", "planta como el poroto o la lenteja, con bacterias en sus raíces"), ("afirmación", "conclusión que se quiere defender")],
    worked=[
        {"title": "Por qué las plantas necesitan bacterias", "problem": "El aire tiene 78 % de N2. ¿Por qué las plantas no lo usan directamente?", "steps": ["El N2 es una molécula muy estable y las plantas no pueden usarla así.", "Las bacterias lo transforman en compuestos como los nitratos."], "answer": "Porque necesitan que las bacterias lo transformen en compuestos utilizables"},
        {"title": "Argumentar con evidencia", "problem": "Datos de ejemplo: plantas con bacterias fijadoras crecieron 25 cm y las sin bacterias, 15 cm. ¿Qué conclusión cuidadosa se puede sacar?", "steps": ["La diferencia fue 10 cm a favor de las plantas con bacterias.", "Sugiere que aportan nitrógeno utilizable, aunque habría que repetir la prueba."], "answer": "Las bacterias parecen favorecer el crecimiento, pero hay que repetir la prueba"},
    ],
    mistakes=[
        {"wrong": "Decir que las plantas toman el nitrógeno directamente del aire porque el aire tiene mucho.", "why": "Se confunde abundancia con disponibilidad.", "fix": "Necesitan compuestos de nitrógeno, que producen las bacterias."},
        {"wrong": "Afirmar que CHON es lo único que necesitan los seres vivos.", "why": "Se generaliza de más.", "fix": "También se necesitan otros elementos, como el fósforo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué proceso permite a las plantas incorporar el carbono del aire?", "La fotosíntesis", "Usan CO2 para fabricar glucosa."),
            ex("¿En qué forma está el nitrógeno principalmente en el aire?", "Como N2", "Es el gas más abundante del aire."),
            ex("¿Pueden las plantas usar directamente el N2 del aire?", "No", "Necesitan compuestos de nitrógeno formados por bacterias."),
        ],
        "understand": [
            ex("¿Cómo obtienen los animales el nitrógeno?", "Al comer plantas o a otros animales", "El nitrógeno pasa por la alimentación."),
            ex("¿Qué devuelve CO2 al aire? A) La respiración y la descomposición; B) Solo la fotosíntesis", "A)", "Ambas liberan CO2."),
            ex("¿Por qué se dice que C, H, O y N son soporte de la vida?", "Porque forman el agua y las biomoléculas de las células", "Con ellos se construyen las moléculas que realizan las funciones vitales."),
        ],
        "apply": [
            arith("Un abono tiene 10 % de nitrógeno. ¿Cuántos gramos de nitrógeno hay en 200 g de abono?", "200*10//100", "Se calcula el 10 % de 200 g.", " g"),
            ex("¿Qué elemento diferencia a una proteína de un glúcido?", "El nitrógeno", "La proteína lo tiene y el glúcido no."),
            arith("Plantas con bacterias fijadoras crecieron 30 cm y plantas sin bacterias 18 cm (datos de ejemplo). ¿Cuántos cm más crecieron las primeras?", "30-18", "Se resta el crecimiento menor al mayor.", " cm"),
        ],
        "reason": [
            ex("Un estudiante afirma que, como el aire tiene 78 % de N2, las plantas nunca necesitan agregar nitrógeno al suelo. ¿Qué dato lo corrige?", "Que las plantas no pueden usar el N2 directamente", "La abundancia no es lo mismo que la disponibilidad."),
            ex("¿Cuál es la mejor conclusión? A) Las plantas con bacterias crecieron 12 cm más que las sin ellas, lo que sugiere que las bacterias aportan nitrógeno utilizable, aunque hay que repetir la prueba; B) Las plantas con bacterias crecieron 12 cm más, lo que demuestra que las bacterias hacen crecer a todas las plantas", "A)", "Es una conclusión cuidadosa y con datos."),
        ],
        "challenge": [
            ex("La sigla CHON no incluye al fósforo. ¿Se puede afirmar que solo se necesita CHON para vivir?", "No; el fósforo, por ejemplo, forma parte de los ácidos nucleicos", "CHON es la base, pero hay otros elementos necesarios."),
            arith("Una persona de 50 kg tiene cerca de 96 % de C, H, O y N juntos. ¿Cuántos kilogramos son?", "50*96//100", "Se calcula el porcentaje de su masa.", " kg"),
        ],
    },
    context=[ex("Un agricultor planta porotos después de otro cultivo. ¿Por qué eso puede mejorar el suelo?", "Porque las bacterias de las raíces de los porotos aportan nitrógeno utilizable", "Las leguminosas tienen bacterias que fijan el nitrógeno.")],
    selfcheck=[
        ex("¿Qué parte tiene una argumentación además de la afirmación?", "La evidencia y el razonamiento", "Sin ellas la afirmación no está respaldada."),
        ex("¿Qué elemento falta en la sigla CHON pero es necesario en los ácidos nucleicos?", "El fósforo", "Forma parte del ADN."),
        ex("¿Qué organismos devuelven compuestos al suelo al degradar restos?", "Los descomponedores", "Reciclan la materia."),
    ],
    open_task=task(
        "Escribe una argumentación de tres partes (afirmación, evidencia, razonamiento) sobre esta afirmación: «El nitrógeno es soporte de la vida». Usa estos datos: el aire tiene 78 % de N2, las proteínas tienen nitrógeno y las plantas con bacterias fijadoras crecieron 25 cm frente a 15 cm sin ellas (datos de ejemplo). Añade una limitación y dibuja un esquema de flechas con el ciclo del nitrógeno en cuatro cajas: aire, bacterias, plantas y animales.",
        "Afirmación: el nitrógeno es soporte de la vida. Evidencia: forma las proteínas y las plantas con bacterias crecieron 10 cm más. Razonamiento: las plantas usan compuestos de nitrógeno hechos por bacterias a partir del N2. Limitación: son datos de ejemplo y falta repetir la prueba.",
        ["tres partes", "dos datos citados", "una limitación", "esquema de cuatro cajas"],
        ["texto", "esquema"],
        ["decir que las plantas usan N2 directamente", "no declarar una limitación"],
        "Pregunta qué cambiaría si no hubiera descomponedores.",
    ),
    reinforce="Escribe una oración que explique cómo el carbono pasa del aire a un animal.",
    extend="Con una persona de tu casa, miren un huerto o una maceta y comenten qué cosas de ahí crees que necesitan nitrógeno.",
)

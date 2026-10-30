"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 11 (medir masa, volumen y temperatura) y OA 12 (efectos de las fuerzas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA11, OA12 = "CN04 OA 11", "CN04 OA 12"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 11
register(
    OA11, 1,
    materials="Papel y lápiz. Si hay una balanza de cocina en tu casa, úsala con una persona adulta; si no, trabaja con los datos escritos en el cuaderno.",
    use="Aprenderé a medir la masa de sólidos, líquidos y gases con balanza y unidades. Sirve para comparar cuánta materia tienen las cosas sin adivinar.",
    prior=["Sé que todo lo que nos rodea es materia.", "Sé que la materia puede ser sólida, líquida o gaseosa."],
    explain=[
        "La masa es la cantidad de materia que tiene un objeto. Una piedra, el agua de un vaso y el aire de un globo tienen masa. La masa se mide con una balanza.",
        "Las unidades de masa son el gramo (g) y el kilogramo (kg). Un kilogramo tiene 1.000 gramos. Los objetos livianos se miden en gramos, como una manzana, y los más pesados en kilogramos, como un saco de papas.",
        "Para medir un líquido, lo pongo en un recipiente sobre la balanza. La balanza marca la masa del recipiente más la del líquido. Por eso mido antes el recipiente vacío y resto: masa del líquido = total menos recipiente vacío.",
    ],
    vocab=[("masa", "cantidad de materia que tiene un objeto"), ("balanza", "instrumento que mide la masa"), ("gramo (g)", "unidad de masa para cosas livianas"), ("kilogramo (kg)", "unidad de masa; equivale a 1.000 g"), ("recipiente", "objeto que sirve para guardar un líquido")],
    worked=[
        {"title": "Masa del agua de un jarro", "problem": "Un jarro vacío tiene 200 g. Con agua, la balanza marca 700 g. ¿Qué masa tiene el agua?", "steps": ["La balanza mide el jarro más el agua: 700 g.", "El jarro vacío tiene 200 g.", "Resto: 700 − 200 = 500."], "answer": "500 g"},
        {"title": "De kilogramos a gramos", "problem": "Una bolsa de arroz tiene 2 kg. ¿Cuántos gramos son?", "steps": ["1 kg equivale a 1.000 g.", "Son 2 kilogramos: 2 × 1.000."], "answer": "2.000 g"},
    ],
    mistakes=[
        {"wrong": "Anotar como masa del líquido todo lo que marca la balanza.", "why": "Se olvida que el recipiente también tiene masa.", "fix": "Mide el recipiente vacío y réstalo."},
        {"wrong": "Decir que el aire no tiene masa porque no se ve.", "why": "Lo que no se ve parece que no existe.", "fix": "El aire es materia gaseosa y por eso tiene masa, aunque sea muy poca."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué instrumento se usa para medir la masa de un objeto?", "La balanza", "La balanza es el instrumento de la masa."),
            ex("Mides la masa de una manzana. ¿Usas gramos (g) o mililitros (mL)?", "Gramos (g)", "Los gramos miden masa; los mililitros miden volumen."),
            ex("Completa: 1 kg equivale a ___ gramos.", "1.000", "Un kilogramo tiene mil gramos."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la masa de un objeto?", "La cantidad de materia que tiene", "Masa es cuánta materia hay en el objeto."),
            ex("Pedro dice que el agua no tiene masa porque no se puede agarrar con los dedos. ¿Tiene razón?", "No, el agua es materia y tiene masa", "Toda materia tiene masa, aunque sea líquida."),
            arith("Una bolsa de papas tiene 2 kg. ¿Cuántos gramos son?", "2*1000", "Cada kilogramo tiene 1.000 g.", " g"),
        ],
        "apply": [
            arith("Un jarro vacío tiene 240 g. Con agua, la balanza marca 640 g. ¿Qué masa tiene el agua?", "640-240", "Se resta la masa del jarro vacío.", " g"),
            arith("Cada manzana tiene 150 g. ¿Qué masa tienen 3 manzanas juntas?", "3*150", "Se suman tres masas iguales.", " g"),
            ex("¿Cuál tiene más masa: 2.500 g de harina o 2 kg de harina?", "2.500 g", "2 kg son 2.000 g, que es menos que 2.500 g."),
        ],
        "reason": [
            ex("Lucas dice: «mi mochila tiene 3 litros de masa». ¿Qué error cometió?", "Usó litros, que miden volumen; la masa va en gramos o kilogramos", "El litro es una unidad de volumen."),
            ex("Ana puso un vaso con agua en la balanza y marcó 320 g. Dice que el agua tiene 320 g, pero el vaso vacío tiene 120 g. ¿Cuánta masa tiene el agua?", "200 g", "Hay que restar el vaso: 320 − 120 = 200."),
        ],
        "challenge": [
            arith("Un balón de fútbol desinflado tiene 400 g. Después de inflarlo con una bomba, la balanza marca 410 g. ¿Cuántos gramos de masa tiene el aire que se agregó?", "410-400", "Esta diferencia muestra que el gas también tiene masa.", " g"),
            arith("Para completar 1 kg de harina se juntan dos paquetes de 250 g y uno de 500 g. ¿Cuántos gramos suman?", "250+250+500", "Se suman las tres masas; al llegar a 1.000 g se completa 1 kg.", " g"),
        ],
    },
    context=[arith("En la feria, Camila compra 1 kg de tomates y 750 g de cebollas. ¿Cuántos gramos lleva en total?", "1000+750", "Primero se pasa 1 kg a gramos y luego se suma.", " g")],
    selfcheck=[
        ex("¿Con qué instrumento se mide la masa?", "Con una balanza", "La balanza mide masa."),
        ex("¿Un gas, como el aire, tiene masa?", "Sí", "El gas es materia y toda materia tiene masa."),
        ex("Para medir la masa de un líquido, ¿qué hay que restar?", "La masa del recipiente vacío", "La balanza suma recipiente y líquido."),
    ],
    open_task=task(
        "Con una persona de tu casa, elige tres objetos de la cocina que traen la masa escrita en el envase (por ejemplo, un paquete de fideos o de arroz) y anota las masas. Si no puedes, usa estos datos: fideos 400 g, arroz 1 kg, azúcar 500 g. Ordénalos de menor a mayor masa y escribe cuántos gramos suman los tres.",
        "Fideos 400 g, azúcar 500 g, arroz 1.000 g. Suman 1.900 g.",
        ["usa gramos y kilogramos correctamente", "convierte kg a g antes de comparar", "ordena de menor a mayor"],
        ["tabla con los tres objetos", "orden escrito", "suma de las masas"],
        ["comparar 1 kg con 500 g sin convertir", "usar litros para masa"],
        "Reconoce la conversión bien hecha y pide revisar la suma si hay error.",
    ),
    reinforce="Anota tres cosas de tu casa y escribe si su masa se mediría mejor en gramos o en kilogramos.",
    extend="Averigua qué masa de pan se compra normalmente en una casa en una semana y exprésala en gramos y kilogramos.",
)

register(
    OA11, 2,
    materials="Un jarro o taza graduado con marcas en mL, o los dibujos descritos en el cuaderno. Agua de la llave en recipientes plásticos.",
    use="Aprenderé a medir el volumen de líquidos, de sólidos y de gases con unidades apropiadas. Sirve para saber cuánto espacio ocupa la materia.",
    prior=["Sé que la masa se mide con balanza.", "Sé que la materia puede ser sólida, líquida o gaseosa."],
    explain=[
        "El volumen es el espacio que ocupa la materia. Un líquido se mide con un recipiente graduado, como una probeta o una jarra con marcas. Las unidades son el mililitro (mL) y el litro (L). Un litro tiene 1.000 mililitros.",
        "Para leer el volumen, pongo el recipiente sobre una mesa plana y miro la marca a la altura de mis ojos. La marca que coincide con la superficie del líquido es el volumen. Los gases también ocupan volumen: el aire llena el globo y toma su forma.",
        "Un sólido pequeño que no se disuelve en el agua también tiene volumen. Lo mido con el agua: anoto el nivel antes y después de sumergirlo con cuidado. La diferencia es el volumen del sólido.",
    ],
    vocab=[("volumen", "espacio que ocupa la materia"), ("mililitro (mL)", "unidad de volumen para cantidades pequeñas"), ("litro (L)", "unidad de volumen; equivale a 1.000 mL"), ("probeta", "recipiente alargado con marcas para medir líquidos"), ("sumergir", "meter un objeto dentro del agua")],
    worked=[
        {"title": "Volumen de una piedra", "problem": "Una probeta tiene 100 mL de agua. Al sumergir una piedra, el nivel sube a 130 mL. ¿Qué volumen tiene la piedra?", "steps": ["El nivel antes era 100 mL y después 130 mL.", "Resto: 130 − 100 = 30."], "answer": "30 mL"},
        {"title": "Litros y mililitros", "problem": "Una botella tiene 2 L de agua. ¿Cuántos mL son?", "steps": ["1 L equivale a 1.000 mL.", "Calculo 2 × 1.000."], "answer": "2.000 mL"},
    ],
    mistakes=[
        {"wrong": "Medir el volumen de un líquido con una balanza.", "why": "Se confunden masa y volumen.", "fix": "El volumen se mide con recipiente graduado; la balanza mide masa."},
        {"wrong": "Leer la marca mirando desde arriba.", "why": "La vista inclinada hace que la marca parezca otra.", "fix": "Mira a la altura de la superficie del líquido."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué instrumento mide el volumen de un líquido: la probeta o la balanza?", "La probeta", "La probeta tiene marcas para leer el volumen."),
            ex("¿El volumen se mide en mililitros o en gramos?", "En mililitros", "Los mL miden volumen; los gramos miden masa."),
            ex("Completa: 1 L equivale a ___ mL.", "1.000", "Un litro tiene mil mililitros."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es el volumen?", "El espacio que ocupa la materia", "Volumen es cuánto espacio ocupa algo."),
            ex("Un globo lleno de aire tiene la forma del globo. ¿El aire ocupa espacio?", "Sí", "El gas llena el globo y por eso tiene volumen."),
            arith("Una botella tiene 3 L de bebida. ¿Cuántos mL son?", "3*1000", "Cada litro tiene 1.000 mL.", " mL"),
        ],
        "apply": [
            arith("Una probeta marca 150 mL de agua. Al sumergir una piedra, marca 210 mL. ¿Cuál es el volumen de la piedra?", "210-150", "La piedra desplaza el agua; se resta el nivel inicial.", " mL"),
            arith("Un jarro tiene 250 mL de leche y otro tiene 400 mL de leche. ¿Cuántos mL hay en total?", "250+400", "Se suman los dos volúmenes.", " mL"),
            ex("¿Cuál es mayor: 1.500 mL o 1 L de agua?", "1.500 mL", "1 L son 1.000 mL, que es menos que 1.500 mL."),
        ],
        "reason": [
            ex("Marta lee el nivel del agua mirando desde arriba del vaso. ¿Cómo debe mirar para leer bien?", "A la altura de la superficie del agua", "Así la marca no parece cambiar de lugar."),
            ex("Pedro dice que una piedra no tiene volumen porque es dura. ¿Cómo se lo demuestras con agua?", "Al sumergirla el nivel del agua sube", "El agua sube porque la piedra ocupa espacio."),
        ],
        "challenge": [
            arith("Un vaso medidor tiene 500 mL de agua. Al meter una llave de metal limpia, sube a 505 mL. ¿Cuál es el volumen de la llave?", "505-500", "El aumento del nivel es el volumen del sólido.", " mL"),
            ex("Dos recipientes tienen 300 mL de agua. En uno se sumerge una piedra y el nivel sube a 340 mL; en el otro, una piedra que lo sube a 360 mL. ¿Cuál piedra tiene mayor volumen?", "La que subió a 360 mL", "Subió 60 mL, más que los 40 mL de la otra."),
        ],
    },
    context=[arith("Para una receta se necesitan 1 L de leche. En casa solo hay un jarro de 250 mL. ¿Cuántas veces hay que llenar el jarro?", "1000//250", "Un litro son 1.000 mL y cada jarro trae 250 mL.", " veces")],
    selfcheck=[
        ex("¿Qué mide el volumen?", "El espacio que ocupa la materia", "Volumen es espacio ocupado."),
        ex("¿Cuántos mL tiene 1 L?", "1.000 mL", "Un litro equivale a mil mililitros."),
        ex("¿Qué instrumento mide el volumen de un líquido?", "Una probeta o jarra graduada", "Tiene marcas para leer los mL."),
    ],
    open_task=task(
        "Con ayuda de una persona adulta, llena un jarro con marcas hasta 200 mL de agua, sumerge una piedra pequeña y anota el nuevo nivel. Si no tienes jarro graduado, usa estos datos: antes 200 mL, después 245 mL. Calcula el volumen de la piedra y escribe una frase que explique por qué sube el agua.",
        "245 − 200 = 45 mL. El agua sube porque la piedra ocupa un espacio y el agua se corre hacia arriba.",
        ["resta bien los dos niveles", "usa mL como unidad", "explica la subida con espacio ocupado"],
        ["tabla con nivel antes y después", "cálculo", "frase explicativa"],
        ["usar gramos para el volumen", "olvidar restar el nivel inicial"],
        "Valora la resta y pide que justifique la unidad usada.",
    ),
    reinforce="Mira dos envases de tu casa que tengan el volumen escrito y ordénalos de menor a mayor volumen.",
    extend="Averigua cómo se mide el volumen de una piedra grande que no cabe en un vaso y cuenta tu idea.",
)

register(
    OA11, 3,
    materials="Un termómetro de pared o ambiental si hay uno en casa; si no, los datos escritos. Nunca uses el termómetro con agua que queme ni lo metas en la boca.",
    use="Aprenderé a leer la temperatura en grados Celsius con un termómetro. Sirve para comparar qué tan caliente o frío está algo sin depender de lo que sentimos.",
    prior=["Sé que algo puede estar frío, tibio o caliente.", "Sé comparar números de dos cifras."],
    explain=[
        "La temperatura indica qué tan caliente o frío está algo. Se mide con un termómetro y su unidad es el grado Celsius (°C). Por ejemplo, el agua helada está cerca de 0 °C y el agua de la llave tibia, cerca de 30 °C.",
        "Un termómetro tiene un tubo con un líquido que sube cuando la temperatura aumenta y baja cuando disminuye. Para leer, miro hasta dónde llega el líquido y busco la marca más cercana en la escala. La escala es la fila de números y rayitas.",
        "Nuestras manos no son buenos termómetros: si tengo una mano fría y otra tibia, el mismo objeto me parece distinto. Por eso medimos. Se puede medir la temperatura de sólidos, líquidos y gases, como el aire de una pieza.",
    ],
    vocab=[("temperatura", "medida de qué tan caliente o frío está algo"), ("termómetro", "instrumento que mide la temperatura"), ("grado Celsius (°C)", "unidad de temperatura"), ("escala", "serie de números y marcas de un instrumento"), ("aumentar", "hacerse mayor")],
    worked=[
        {"title": "Leer el termómetro", "problem": "En un termómetro, el líquido llega a la marca 22 °C. ¿Qué temperatura tiene la pieza?", "steps": ["Miro dónde termina el líquido.", "Leo la marca más cercana en la escala."], "answer": "22 °C"},
        {"title": "Comparar dos aguas", "problem": "Un vaso de agua tiene 8 °C y otro tiene 25 °C. ¿Cuál está más caliente y por cuántos grados?", "steps": ["El número mayor indica más calor: 25 °C.", "Resto: 25 − 8 = 17."], "answer": "El de 25 °C, por 17 °C más"},
    ],
    mistakes=[
        {"wrong": "Decir que algo está más caliente porque «se siente» más caliente.", "why": "La mano cambia según cómo venga: fría o tibia.", "fix": "Mide con un termómetro y compara los números."},
        {"wrong": "Medir temperatura en gramos o en mililitros.", "why": "Se confunden las unidades de las tres medidas.", "fix": "Temperatura va en °C, masa en g o kg y volumen en mL o L."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué instrumento mide la temperatura?", "El termómetro", "El termómetro mide qué tan caliente o frío está algo."),
            ex("¿En qué unidad se mide la temperatura: °C o kg?", "°C", "Los grados Celsius miden temperatura."),
            ex("Si el líquido del termómetro sube, ¿la temperatura aumenta o disminuye?", "Aumenta", "Al subir el líquido, hay más calor."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué indica la temperatura de un objeto?", "Qué tan caliente o frío está", "Es una medida de calor o frío."),
            ex("¿Por qué no basta tocar con la mano para comparar temperaturas?", "Porque la mano puede engañarse", "La mano fría o tibia cambia lo que se siente."),
            ex("Un termómetro marca 0 °C en un vaso con hielo y agua. ¿Está caliente o frío?", "Frío", "0 °C es una temperatura baja."),
        ],
        "apply": [
            arith("Un vaso de agua tiene 11 °C y otro tiene 26 °C. ¿Cuántos grados más tiene el segundo?", "26-11", "Se resta el número menor del mayor.", " °C"),
            ex("Tres vasos tienen 30 °C, 12 °C y 21 °C. ¿Cuál está más frío?", "El de 12 °C", "El número menor indica menos calor."),
            arith("La pieza tenía 14 °C y después de un rato subió 6 °C. ¿Cuál es su temperatura ahora?", "14+6", "Si sube, se suma.", " °C"),
        ],
        "reason": [
            ex("Sofía dice que 5 kg es una temperatura baja. ¿Cuál es el error?", "El kilogramo mide masa, no temperatura", "La temperatura se mide en °C."),
            ex("Mateo tiene una mano en agua helada y otra en agua tibia, y después las dos en el mismo vaso. Dice que el vaso tiene dos temperaturas. ¿Qué instrumento resuelve la duda?", "Un termómetro", "El instrumento da un solo valor medido."),
        ],
        "challenge": [
            ex("Una profesora mide el aire de la sala con un termómetro a las 9:00 (16 °C), 12:00 (22 °C) y 15:00 (20 °C). ¿A qué hora hubo más calor?", "A las 12:00", "22 °C es el número mayor de las tres medidas."),
            arith("Entre las 9:00 (16 °C) y las 12:00 (22 °C), ¿cuántos grados subió la temperatura del aire?", "22-16", "Es la diferencia entre las dos lecturas.", " °C"),
        ],
    },
    context=[ex("Antes de bañarse, Pablo mide el agua con un termómetro: marca 38 °C. Su hermana dice que está fría, pero él dice que está tibia. ¿Qué dato pesa más: lo que sienten o lo que marca el termómetro?", "Lo que marca el termómetro", "Es una medida igual para todos, la sensación cambia.")],
    selfcheck=[
        ex("¿En qué unidad se mide la temperatura?", "En grados Celsius", "Su símbolo es °C."),
        ex("¿Un gas, como el aire de la sala, tiene temperatura?", "Sí", "Se puede medir en sólidos, líquidos y gases."),
        ex("Si un termómetro marca 5 °C y otro 18 °C, ¿cuál mide más calor?", "El de 18 °C", "El número mayor indica más calor."),
    ],
    open_task=task(
        "Si tienes un termómetro, mide la temperatura del aire de tu pieza en tres momentos del día. Si no, usa estos datos: mañana 14 °C, mediodía 21 °C, noche 16 °C. Haz una tabla y escribe cuándo hay más calor y cuántos grados más que en la mañana.",
        "Más calor al mediodía: 21 °C, que son 7 °C más que en la mañana.",
        ["lee las tres temperaturas", "compara con la unidad °C", "calcula la diferencia"],
        ["tabla de tres filas", "frase de comparación"],
        ["usar kg o mL", "restar mal los grados"],
        "Reconoce la tabla clara y pide que revise la resta.",
    ),
    reinforce="Anota la temperatura que dice el pronóstico del día y compárala con la de ayer.",
    extend="Averigua por qué el termómetro de vidrio de antes se reemplazó en muchos hogares por termómetros digitales.",
)

register(
    OA11, 4,
    materials="Papel y lápiz. Las tres medidas se hacen con los datos escritos del cuaderno; si tienes una balanza, un jarro con marcas y un termómetro, puedes comprobar con agua tibia.",
    use="Aprenderé a elegir el instrumento y la unidad correctos para cada medida y a explicar mi conclusión con datos. Sirve para no mezclar masa, volumen y temperatura.",
    prior=["Sé medir masa con balanza, volumen con probeta y temperatura con termómetro.", "Sé qué unidad va con cada una."],
    explain=[
        "Masa, volumen y temperatura son tres medidas distintas de la materia. Cada una tiene su pregunta, su instrumento y su unidad. Masa: ¿cuánta materia hay? Balanza, g o kg. Volumen: ¿cuánto espacio ocupa? Probeta o jarra graduada, mL o L. Temperatura: ¿qué tan caliente está? Termómetro, °C.",
        "Cuando investigo, cambio una sola cosa y dejo igual todo lo demás. Si quiero saber si el agua caliente se enfría más rápido en un vaso ancho o angosto, uso la misma cantidad de agua y la misma temperatura al inicio. Así la diferencia viene del vaso.",
        "Una conclusión debe citar los datos. Por ejemplo: «El agua del vaso ancho bajó de 40 °C a 28 °C y la del vaso angosto a 33 °C». Además, digo qué límite tiene mi medición, como que solo medí una vez.",
    ],
    vocab=[("instrumento", "objeto que sirve para medir"), ("unidad", "nombre de la medida, como g, mL o °C"), ("dato", "número medido que anotamos"), ("conclusión", "respuesta que sale de los datos"), ("límite", "algo que puede hacer menos segura mi conclusión")],
    worked=[
        {"title": "Elegir instrumento y unidad", "problem": "Quieres saber cuánto jugo hay en una jarra. ¿Qué instrumento y qué unidad usas?", "steps": ["Pregunto qué medida es: el espacio que ocupa el líquido, o sea volumen.", "Para volumen uso jarra graduada y mL o L."], "answer": "Jarra graduada, en mL o L"},
        {"title": "Concluir con datos", "problem": "Agua A bajó de 60 °C a 45 °C en 10 min. Agua B bajó de 60 °C a 50 °C en 10 min. ¿Cuál se enfrió más?", "steps": ["A bajó 60 − 45 = 15 °C.", "B bajó 60 − 50 = 10 °C.", "15 es mayor que 10."], "answer": "El agua A se enfrió más"},
    ],
    mistakes=[
        {"wrong": "Medir los mililitros de agua con un termómetro.", "why": "Se mezclan instrumento y magnitud.", "fix": "Primero pregunta qué medida es; luego elige el instrumento."},
        {"wrong": "Comparar dos vasos con distintas cantidades de agua y decir que el vaso es la causa.", "why": "Cambiaron dos cosas a la vez.", "fix": "Deja igual la cantidad de agua y cambia solo el vaso."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué instrumento y qué unidad usas para medir masa?", "Balanza, en g o kg", "Masa se mide con balanza."),
            ex("¿Qué medida se hace con una probeta?", "El volumen", "La probeta tiene marcas para leer volumen."),
            ex("¿Qué unidad usa un termómetro?", "°C", "Los grados Celsius miden temperatura."),
        ],
        "understand": [
            ex("Une cada medida con su unidad: masa, volumen y temperatura (g, mL, °C).", "Masa: g; volumen: mL; temperatura: °C", "Cada medida tiene su unidad."),
            ex("¿Cuál pregunta corresponde a la masa: «¿cuánto espacio ocupa?» o «¿cuánta materia hay?»?", "¿Cuánta materia hay?", "Masa es cantidad de materia."),
            ex("¿Por qué un dato debe llevar unidad?", "Porque sin unidad no se sabe qué se midió", "Un número solo no dice si son g, mL o °C."),
        ],
        "apply": [
            ex("Quieres saber qué tan caliente está el agua de una taza. ¿Qué instrumento eliges?", "Un termómetro", "La temperatura se mide con termómetro."),
            ex("Quieres saber cuántos gramos tiene una bolsa de pan. ¿Qué instrumento eliges?", "Una balanza", "Para masa se usa balanza."),
            ex("Quieres saber cuánta agua cabe en un balde. ¿Qué medida haces y con qué unidad?", "Volumen, en litros (L)", "El espacio ocupado por un líquido es volumen; en un balde conviene usar litros."),
        ],
        "reason": [
            arith("El agua de una taza estaba a 50 °C y diez minutos después marcó 38 °C. ¿Cuántos grados bajó su temperatura?", "50-38", "Se resta la temperatura final de la inicial.", " °C"),
            ex("Dos vasos tienen agua a la misma temperatura: un vaso angosto con 100 mL y un vaso ancho con 300 mL. Alguien dice que el vaso angosto se enfría más rápido por ser angosto. ¿Qué se hizo mal en la prueba?", "Los vasos tienen distinta cantidad de agua", "Debe cambiar solo la forma del vaso, no el volumen."),
        ],
        "challenge": [
            ex("Un grupo midió el agua de una taza una sola vez: 40 °C. ¿Cuál es un límite de esta medición?", "Fue una sola medida", "Con una medida no se sabe si el valor es repetible."),
            ex("Un niño anota la masa de su mochila así: «5 L». ¿Qué está mal en su dato?", "La unidad: los litros miden volumen, no masa", "La masa se anota en g o kg."),
        ],
    },
    context=[ex("En una receta se pide medir 500 g de harina, 250 mL de leche y calentar el agua a 40 °C. Si cada medida usa un instrumento, ¿cuántos instrumentos distintos se necesitan?", "Tres", "Se necesita balanza, jarra graduada y termómetro.")],
    selfcheck=[
        ex("¿Qué medida se hace con una balanza?", "La masa", "La balanza mide masa."),
        ex("¿Qué unidad va con el volumen de un líquido?", "mL o L", "El volumen de líquidos va en esas unidades."),
        ex("¿Por qué las conclusiones deben citar datos?", "Porque así se puede comprobar", "Los datos son la evidencia."),
    ],
    open_task=task(
        "Usa este conjunto de datos simulado, no medido: agua en vaso A (200 mL): 60 °C al inicio y 44 °C a los 10 min; agua en vaso B (200 mL, con tapa): 60 °C al inicio y 52 °C a los 10 min. Escribe cuánto bajó cada temperatura, cuál se enfrió más, una causa posible y un límite de esta prueba.",
        "A bajó 16 °C; B bajó 8 °C. El agua del vaso A se enfrió más; una causa posible es que B tenía tapa. Un límite: solo hay una medida a los 10 min.",
        ["calcula las dos bajadas", "compara con los datos", "nombra una causa y un límite"],
        ["resta de cada vaso", "frase de conclusión con datos"],
        ["decir que A bajó 44 °C", "concluir sin citar números"],
        "Valora que cite los números y pide mejorar el límite si es muy general.",
    ),
    reinforce="Escribe tres medidas de la vida diaria y di qué instrumento y qué unidad usarías para cada una.",
    extend="Piensa cómo comprobarías con medidas si una taza con tapa mantiene el agua tibia más tiempo.",
)

# ---------------------------------------------------------------- OA 12
register(
    OA12, 1,
    materials="Una pelota blanda o un calcetín enrollado, una mesa y un libro. Trabaja sobre el suelo despejado y con cuidado de no golpear a nadie.",
    use="Aprenderé qué es una fuerza y cómo puede poner en movimiento o detener un objeto. Sirve para explicar qué pasa cuando empujamos o tiramos de algo.",
    prior=["Sé que algunos objetos se mueven y otros están quietos.", "Sé que empujar y tirar son acciones."],
    explain=[
        "Una fuerza es un empujón o un tirón que se aplica a un objeto. Cuando pateo una pelota, la empujo. Cuando abro un cajón, tiro de él. No vemos la fuerza, pero sí vemos lo que provoca.",
        "Una fuerza puede hacer que un objeto quieto comience a moverse. También puede hacer que un objeto en movimiento se detenga. Si una pelota rueda y la agarro con la mano, mi mano ejerce una fuerza que la frena.",
        "Para que haya un cambio en el movimiento tiene que actuar una fuerza. Un libro sobre la mesa no se mueve solo. Si nadie lo empuja o tira de él, se queda quieto. Las fuerzas pueden ser pequeñas o grandes. Si dos fuerzas iguales empujan un objeto desde lados opuestos, el objeto no se mueve.",
    ],
    vocab=[("fuerza", "empujón o tirón que se aplica a un objeto"), ("empujar", "aplicar una fuerza alejando el objeto de mí"), ("tirar", "aplicar una fuerza acercando el objeto a mí"), ("movimiento", "cambio de lugar de un objeto"), ("detener", "hacer que algo deje de moverse")],
    worked=[
        {"title": "Cajón", "problem": "Abres un cajón. ¿Empujas o tiras, y qué cambia?", "steps": ["Agarro la manilla y lo acerco a mí: es un tirón.", "El cajón estaba quieto y ahora se mueve."], "answer": "Tiras; el cajón pasa de quieto a en movimiento"},
        {"title": "Parar una pelota", "problem": "Una pelota rueda y la pisas con cuidado. ¿Qué cambia?", "steps": ["El pie aplica una fuerza sobre la pelota.", "La pelota estaba en movimiento y queda quieta."], "answer": "La fuerza detuvo la pelota"},
    ],
    mistakes=[
        {"wrong": "Decir que un objeto en movimiento no necesita ninguna fuerza para detenerse.", "why": "Se cree que los objetos se frenan por sí solos.", "fix": "Para detener un objeto actúa una fuerza, por ejemplo la mano o el roce."},
        {"wrong": "Pensar que la fuerza es algo que se ve, como una flecha en el aire.", "why": "Los dibujos usan flechas y parecen reales.", "fix": "La flecha solo representa la fuerza; lo que vemos es su efecto."},
    ],
    tiers={
        "recovery": [
            ex("Empujas una puerta para abrirla. ¿Aplicas un empujón o un tirón?", "Un empujón", "Alejas la puerta de ti."),
            ex("Abres un cajón con la manilla. ¿Aplicas un empujón o un tirón?", "Un tirón", "Acercas el cajón a ti."),
            ex("Completa: a un empujón o un tirón sobre un objeto se le llama ___.", "fuerza", "Esa es la definición de fuerza."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una fuerza?", "Un empujón o un tirón sobre un objeto", "Así se define la fuerza."),
            ex("Un libro está quieto sobre una mesa. ¿Qué hay que hacer para que comience a moverse?", "Aplicarle una fuerza", "Sin fuerza no cambia su movimiento."),
            ex("Una pelota rueda y la agarras con las manos. ¿Qué provocó que se detuviera?", "La fuerza de tus manos", "Las manos aplicaron una fuerza que la frenó."),
        ],
        "apply": [
            ex("Clasifica en empujón o tirón: patear una pelota, abrir un cajón, cerrar una puerta con la mano.", "Patear: empujón; abrir un cajón: tirón; cerrar la puerta: empujón", "Se mira si el objeto se aleja o se acerca de ti."),
            ex("Tomas un carrito de juguete quieto y lo empujas. ¿Qué efecto tuvo la fuerza?", "Lo puso en movimiento", "El carrito pasó de quieto a en movimiento."),
            ex("Una bicicleta va rodando y alguien aprieta los frenos hasta que se detiene. ¿Qué efecto tuvo la fuerza de los frenos?", "Detuvo la bicicleta", "La fuerza frenó el movimiento."),
        ],
        "reason": [
            ex("Un niño dice que el balón se detuvo «solo». ¿Qué le preguntas para encontrar la fuerza?", "Qué cosa tocó o frenó el balón", "Algo, como el pasto o una mano, aplicó una fuerza."),
            ex("Una caja está quieta en el suelo. ¿Se moverá sola si nadie la toca?", "No", "Un objeto quieto necesita una fuerza para moverse."),
        ],
        "challenge": [
            ex("Dos amigos empujan una caja desde lados opuestos con la misma fuerza y la caja no se mueve. ¿Hubo fuerzas aplicadas?", "Sí, pero son iguales y opuestas, y la caja no se mueve", "Las dos fuerzas son iguales y contrarias."),
            ex("Camila dice: «si empujo una pared con todas mis fuerzas y no se mueve, no apliqué ninguna fuerza». ¿Tiene razón?", "No", "Sí aplicó una fuerza, pero no fue suficiente para moverla."),
        ],
    },
    context=[ex("En el patio, Diego patea una pelota que estaba quieta. La pelota rueda y un compañero la detiene con el pie. ¿Cuántas fuerzas distintas aplicaron las personas sobre la pelota?", "Dos", "La patada puso la pelota en movimiento y el pie la detuvo.")],
    selfcheck=[
        ex("¿Qué es una fuerza?", "Un empujón o un tirón", "Esa es la idea central."),
        ex("¿Qué hace falta para que un objeto quieto se mueva?", "Una fuerza", "Sin fuerza queda quieto."),
        ex("Cerrar un cajón con la mano, ¿es empujar o tirar?", "Empujar", "El cajón se aleja de ti."),
    ],
    open_task=task(
        "Con una pelota blanda, haz tres acciones seguras: empujarla suave para que ruede, detenerla con la mano y empujarla otra vez. Si no puedes, usa esta lista: A) empujar un carrito, B) tirar de un cordel atado a una caja, C) frenar con la mano una pelota que rueda hacia ti. Para cada acción anota si es empujón o tirón y qué cambio provoca.",
        "A) empujón: el carrito pasa de quieto a moverse. B) tirón: la caja se acerca. C) empujón: la mano empuja la pelota en contra de su movimiento y la detiene.",
        ["distingue empujón y tirón", "dice si pone en movimiento o detiene", "usa la palabra fuerza"],
        ["tabla de tres acciones", "frase final con el concepto de fuerza"],
        ["decir que no hay fuerza si no hay movimiento", "confundir empujón con tirón"],
        "Valora la tabla y pide corregir cualquier acción mal clasificada.",
    ),
    reinforce="Observa en tu casa cinco acciones de empujar o tirar y anótalas en dos columnas.",
    extend="Busca un ejemplo en que una fuerza detenga algo grande, como un vehículo, y explica qué lo detiene.",
)

register(
    OA12, 2,
    materials="Una esponja, una banda elástica gruesa, plasticina o masa de sal y una regla. No estires la banda hacia la cara de nadie.",
    use="Aprenderé cómo una fuerza puede cambiar la forma de un objeto. Sirve para explicar por qué se doblan, se estiran o se aplastan algunas cosas.",
    prior=["Sé que una fuerza es un empujón o un tirón.", "Sé que las fuerzas pueden mover o detener objetos."],
    explain=[
        "Una fuerza también puede cambiar la forma de un objeto. Si aprieto una esponja, se aplasta. Si estiro una banda elástica, se alarga. Si presiono plasticina, queda con la forma de mis dedos.",
        "Hay objetos elásticos, que vuelven a su forma cuando la fuerza termina, como la esponja, el resorte y la banda elástica. Otros son moldeables o plásticos, y su forma queda cambiada, como la plasticina y la masa. Otros son rígidos y casi no cambian, como una piedra.",
        "El tamaño de la fuerza importa. Con un apretón suave una esponja se aplasta un poco y con uno fuerte se aplasta mucho. Si la fuerza es demasiado grande, algunos objetos se rompen, como una galleta.",
    ],
    vocab=[("elástico", "que vuelve a su forma cuando se deja de aplicar la fuerza"), ("moldeable", "que cambia de forma y la conserva"), ("rígido", "que casi no cambia de forma"), ("aplastar", "presionar hasta dejar algo más plano"), ("estirar", "tirar para hacer algo más largo")],
    worked=[
        {"title": "Esponja y plasticina", "problem": "Aprietas una esponja y una bolita de plasticina y las sueltas. ¿Qué pasa con cada una?", "steps": ["La esponja vuelve a su forma: es elástica.", "La plasticina queda aplastada: es moldeable."], "answer": "Esponja: recupera su forma; plasticina: queda cambiada"},
        {"title": "Banda de largo medido", "problem": "Una banda mide 10 cm. Al estirarla mide 16 cm. ¿Cuánto se alargó?", "steps": ["Largo final menos largo inicial.", "16 − 10 = 6."], "answer": "6 cm"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los objetos vuelven a su forma al soltarlos.", "why": "Se generaliza desde la esponja o el resorte.", "fix": "Los elásticos vuelven; los moldeables quedan cambiados."},
        {"wrong": "Pensar que una fuerza solo mueve cosas y no las deforma.", "why": "Se asocia fuerza únicamente con movimiento.", "fix": "Una fuerza también cambia la forma de un objeto."},
    ],
    tiers={
        "recovery": [
            ex("Aprietas una esponja. ¿Cambia su forma?", "Sí", "La esponja se aplasta con la fuerza."),
            ex("Estiras una banda elástica. ¿Se vuelve más larga o más corta?", "Más larga", "Tirar la alarga."),
            ex("Completa: la plasticina es ___ porque queda con la forma que le damos (elástica o moldeable).", "moldeable", "No vuelve a la forma inicial."),
        ],
        "understand": [
            ex("¿Qué significa que un objeto sea elástico?", "Que vuelve a su forma cuando termina la fuerza", "Esa es la propiedad."),
            ex("¿Cuál queda con otra forma al soltarla: la esponja o la plasticina?", "La plasticina", "La plasticina es moldeable."),
            ex("¿Por qué una piedra casi no cambia de forma al apretarla con la mano?", "Porque es rígida", "Un objeto rígido casi no se deforma."),
        ],
        "apply": [
            arith("Una banda mide 12 cm. Al estirarla mide 20 cm. ¿Cuánto se alargó?", "20-12", "Se resta el largo inicial del final.", " cm"),
            ex("Clasifica en elástico o moldeable: resorte, masa de modelar, esponja.", "Elásticos: resorte y esponja. Moldeable: masa de modelar", "Los elásticos recuperan su forma; la masa no."),
            ex("Aprietas fuerte una galleta y se parte en trozos. ¿Qué efecto tuvo la fuerza?", "La rompió", "Fue demasiado grande para ese objeto."),
        ],
        "reason": [
            ex("Un niño dice: «la banda es elástica porque se alargó». ¿Qué observación falta para saberlo?", "Ver si vuelve a su largo original al soltarla", "Elástico es volver a la forma."),
            ex("Ana aprieta una pelota blanda con poca y con mucha fuerza. ¿En cuál queda más aplastada?", "Con mucha fuerza", "Más fuerza produce un cambio de forma mayor."),
        ],
        "challenge": [
            arith("Una banda mide 10 cm. Con una carga pequeña colgada mide 13 cm y con una carga mayor mide 19 cm. ¿Cuántos cm más se alargó con la carga mayor que con la pequeña?", "19-13", "Se comparan los largos con cada peso.", " cm"),
            ex("Quieres saber si más fuerza aplasta más una esponja. ¿Qué debes cambiar y qué debes dejar igual en la prueba?", "Cambio solo la fuerza; dejo igual la esponja y la forma de apretar", "Una prueba justa cambia una sola cosa."),
        ],
    },
    context=[ex("Marta guarda un resorte de juguete en un cajón. Lo estira con las manos y al soltarlo vuelve a quedar corto. ¿Es un objeto elástico o moldeable?", "Elástico", "Recupera su forma al terminar la fuerza.")],
    selfcheck=[
        ex("¿Una fuerza puede cambiar la forma de un objeto?", "Sí", "Aplastar y estirar cambian la forma."),
        ex("¿La esponja es elástica o moldeable?", "Elástica", "Vuelve a su forma cuando se suelta."),
        ex("Si la fuerza es muy grande, ¿qué puede pasarle a una galleta?", "Se rompe", "Las fuerzas muy grandes pueden romper objetos."),
    ],
    open_task=task(
        "Prueba con una esponja, plasticina y una banda elástica: aprieta o estira y suelta. Si no tienes esos materiales, usa este resultado ya medido: la esponja vuelve a su forma, la plasticina queda aplastada y la banda mide 10 cm, se alarga a 15 cm y al soltarla vuelve a medir 10 cm. Escribe en una tabla qué objeto es elástico y cuál moldeable, y cuánto se alargó la banda.",
        "Esponja: elástica. Plasticina: moldeable. Banda: elástica, se alargó 5 cm.",
        ["clasifica los tres objetos", "calcula el alargamiento", "usa elástico y moldeable bien"],
        ["tabla", "cálculo de la banda"],
        ["decir que la plasticina es elástica", "restar mal los cm"],
        "Reconoce la clasificación correcta y revisa la resta si hace falta.",
    ),
    reinforce="Aprieta o estira tres objetos seguros de tu casa y anota cuál vuelve a su forma y cuál no.",
    extend="Averigua para qué se usa un colchón con resortes y qué efecto de las fuerzas aprovecha.",
)

register(
    OA12, 3,
    materials="Una pelota blanda, un libro y una mesa baja, un cordel. Juega en un lugar despejado, sin vidrios y lejos de otras personas.",
    use="Aprenderé cómo una fuerza cambia la rapidez y la dirección de un objeto en movimiento. Sirve para explicar por qué una pelota llega más lejos o cambia de rumbo.",
    prior=["Sé que una fuerza puede poner en movimiento o detener un objeto.", "Sé que la rapidez dice qué tan rápido se mueve algo."],
    explain=[
        "La rapidez dice qué tan rápido se mueve un objeto. Una fuerza puede aumentarla o disminuirla. Si empujo un carrito con más fuerza, sale más rápido. Si ya va rodando y lo empujo otra vez en el mismo sentido, aumenta su rapidez. Si lo freno, disminuye.",
        "La dirección es hacia dónde va el objeto. Una fuerza puede cambiarla. Si una pelota va hacia adelante y la golpeo por un lado, cambia de rumbo. Por eso un jugador de fútbol puede cambiar el rumbo del balón con un toque.",
        "En resumen, una fuerza puede cambiar la forma, la rapidez y la dirección del movimiento. La fuerza mayor produce un cambio mayor. Para comprobarlo hago una prueba justa: cambio solo la fuerza y dejo igual el objeto, el piso y el largo del recorrido.",
    ],
    vocab=[("rapidez", "qué tan rápido se mueve un objeto"), ("dirección", "hacia dónde se mueve un objeto"), ("aumentar", "hacer más grande"), ("disminuir", "hacer más pequeño"), ("prueba justa", "prueba en que cambia una sola cosa")],
    worked=[
        {"title": "Más fuerza, más rapidez", "problem": "Un carrito recorre 40 cm con un empujón suave y 90 cm con un empujón fuerte. ¿Qué pasó con la rapidez?", "steps": ["Con el empujón fuerte llega más lejos.", "Eso indica mayor rapidez al partir."], "answer": "Con más fuerza, el carrito tuvo más rapidez"},
        {"title": "Cambio de dirección", "problem": "Una pelota va hacia adelante y la golpeas por un lado. ¿Qué cambia?", "steps": ["La fuerza actúa de lado.", "La pelota deja de ir derecho y gira hacia el costado."], "answer": "Cambia la dirección"},
    ],
    mistakes=[
        {"wrong": "Concluir que más fuerza siempre es mejor.", "why": "A veces una fuerza muy grande rompe o desvía el objeto.", "fix": "Elige la fuerza según lo que quieres lograr."},
        {"wrong": "Comparar dos empujones con pelotas distintas y concluir sobre la fuerza.", "why": "Cambiaron dos cosas a la vez.", "fix": "Usa la misma pelota y el mismo piso."},
    ],
    tiers={
        "recovery": [
            ex("Empujas más fuerte un carrito. ¿Su rapidez aumenta o disminuye?", "Aumenta", "Mayor fuerza produce más rapidez."),
            ex("Frenas una bicicleta. ¿Su rapidez aumenta o disminuye?", "Disminuye", "Frenar es reducir la rapidez."),
            ex("Completa: la ___ es hacia dónde se mueve un objeto (rapidez o dirección).", "dirección", "La dirección indica el rumbo."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la rapidez de un objeto?", "Qué tan rápido se mueve", "Rapidez es qué tan rápido va."),
            ex("¿Por qué una pelota cambia de dirección si la golpeas por un lado?", "Porque la fuerza actúa de lado", "La fuerza empuja hacia el costado."),
            ex("Un carrito que recibe un empujón fuerte llega más lejos que con uno suave. ¿Qué cambio de la fuerza explica esto?", "Que su rapidez inicial fue mayor", "A mayor fuerza, mayor rapidez."),
        ],
        "apply": [
            arith("Con un empujón suave, un carrito recorre 45 cm. Con uno fuerte, recorre 120 cm. ¿Cuántos cm más recorrió con el fuerte?", "120-45", "Se compara la distancia recorrida.", " cm"),
            ex("Una pelota rueda hacia adelante y un niño la patea desde un costado. Ahora la pelota sigue otro rumbo. ¿Qué cambió principalmente: la rapidez o la dirección?", "La dirección", "Cambió hacia dónde se mueve."),
            ex("Un patinador va rápido y se agarra de una baranda con las manos hasta casi detenerse. ¿Qué cambio tuvo su movimiento?", "Disminuyó su rapidez", "La fuerza de las manos lo frenó."),
        ],
        "reason": [
            ex("Dos niñas patean la misma pelota: una con poca fuerza y otra con mucha. ¿Qué debe mantenerse igual para que la prueba sea justa?", "La pelota y el lugar", "Solo debe cambiar la fuerza."),
            ex("Un niño dice que la pelota llegó más lejos porque estaba más contento. ¿Qué dato de la prueba sirve de evidencia?", "La distancia recorrida", "La distancia es una medida del efecto de la fuerza."),
        ],
        "challenge": [
            arith("Una pelota recorre 80 cm con un empujón suave, 130 cm con uno mediano y 190 cm con uno fuerte. ¿Cuántos cm más recorre con el fuerte que con el suave?", "190-80", "Se resta la menor distancia de la mayor.", " cm"),
            ex("Predice: si empujas con una fuerza todavía mayor que la del empujón fuerte, ¿qué esperas que pase con la distancia, según los datos de la pregunta anterior (80, 130 y 190 cm)?", "Que será mayor", "Los datos muestran que más fuerza dio más distancia."),
        ],
    },
    context=[ex("En un partido, Joaquín golpea la pelota con fuerza hacia el arco y su compañero la toca de lado con la cabeza para desviarla. ¿Qué efecto tuvo el toque de lado?", "Cambió la dirección de la pelota", "La fuerza lateral cambió su rumbo.")],
    selfcheck=[
        ex("¿Una fuerza puede cambiar la dirección de un objeto?", "Sí", "Un golpe de lado cambia el rumbo."),
        ex("Si aplicas más fuerza, ¿qué pasa con la rapidez?", "Aumenta", "Mayor fuerza, mayor rapidez."),
        ex("En una prueba justa, ¿cuántas cosas cambias?", "Una sola", "Así sabes qué causó el resultado."),
    ],
    open_task=task(
        "Con un carrito, una pelota o un calcetín enrollado, lanza o empuja tres veces: suave, mediano y fuerte, y mide con una regla o con pasos cuánto recorre. Si no puedes, usa estos datos: suave 30 cm, mediano 70 cm, fuerte 120 cm. Haz una tabla y escribe una conclusión con la relación entre fuerza y distancia.",
        "A mayor fuerza, mayor distancia: 30, 70 y 120 cm. Con el empujón fuerte llegó 90 cm más lejos que con el suave.",
        ["tabla con tres fuerzas", "relación fuerza-distancia", "una sola variable cambiada"],
        ["tabla", "conclusión con números"],
        ["comparar cuerpos distintos", "concluir sin citar la distancia"],
        "Reconoce la prueba justa y pide mencionar el límite de medir una sola vez.",
    ),
    reinforce="Haz rodar una pelota de dos modos y anota qué cambió: rapidez o dirección.",
    extend="Averigua por qué en el boliche la bola puede cambiar su dirección al chocar con un pino.",
)

register(
    OA12, 4,
    materials="Una pelota pequeña, una rampa hecha con un libro grande o una tabla apoyada en dos libros, una regla o cinta de medir. Pruebas en piso plano y sin personas cerca.",
    use="Aprenderé a diseñar una investigación simple para probar los efectos de una fuerza y a concluir con datos. Sirve para saber si una explicación es verdadera con evidencia.",
    prior=["Sé que una fuerza cambia forma, rapidez y dirección.", "Sé que una prueba justa cambia solo una cosa."],
    explain=[
        "Una investigación experimental parte con una pregunta que se puede probar. Por ejemplo: ¿una pelota que baja por una rampa más alta llega más lejos? Ahí la altura de la rampa es la variable que cambio, y la distancia recorrida es lo que mido.",
        "Hago una predicción: «si la rampa es más alta, la pelota llegará más lejos». Después pruebo varias veces con cada altura, para ver si el resultado se repite, y anoto los datos con unidad en una tabla. Si los intentos dan números parecidos, el resultado es más confiable que con un solo intento.",
        "La conclusión responde la pregunta con los datos y dice un límite, como que probé solo con una pelota. Una explicación o modelo sirve mientras coincida con las pruebas; si no coincide, la cambio.",
    ],
    vocab=[("variable", "algo que puede cambiar en una prueba"), ("predicción", "lo que creo que pasará antes de probar"), ("intento", "cada vez que repito la prueba"), ("evidencia", "datos que apoyan una conclusión"), ("límite", "algo que hace menos segura la conclusión")],
    worked=[
        {"title": "Intentos parecidos", "problem": "Con la rampa baja una pelota recorre 60 cm, 62 cm y 58 cm. Con la alta recorre 100 cm, 104 cm y 98 cm. ¿Cuántos cm más recorrió en el primer intento con la rampa alta que con la baja?", "steps": ["Los tres intentos de cada rampa son parecidos, así que el resultado es confiable.", "Comparo los primeros intentos: 100 − 60 = 40."], "answer": "40 cm más"},
        {"title": "Elegir la variable", "problem": "Quieres saber si la altura de la rampa afecta la distancia. ¿Qué cambias y qué mantienes igual?", "steps": ["Cambio la altura de la rampa.", "Mantengo igual la pelota, el piso y el punto de partida."], "answer": "Cambio la altura; mantengo pelota, piso y partida"},
    ],
    mistakes=[
        {"wrong": "Sacar una conclusión después de un solo intento.", "why": "Un resultado puede ser casualidad.", "fix": "Repite varias veces y compara si los intentos se parecen."},
        {"wrong": "Escribir una conclusión que no usa los datos.", "why": "Se responde con lo que se esperaba.", "fix": "Cita los números de la tabla en la conclusión."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué se hace primero en una investigación: la pregunta o la conclusión?", "La pregunta", "Antes de probar hay que saber qué se quiere responder."),
            ex("¿Qué es una predicción?", "Lo que creo que pasará antes de probar", "Es una idea anticipada."),
            ex("¿Una prueba justa cambia una sola cosa o varias?", "Una sola", "Así se sabe qué causó el cambio."),
        ],
        "understand": [
            ex("¿Por qué conviene repetir una prueba varias veces?", "Para ver si el resultado se repite", "Un solo intento puede ser casualidad."),
            ex("En una prueba sobre la altura de la rampa, ¿qué variable se mide como resultado?", "La distancia que recorre la pelota", "Es el efecto que depende de la altura."),
            ex("¿Para qué sirve anotar los datos en una tabla?", "Para compararlos y comprobar la conclusión", "La tabla ordena la evidencia."),
        ],
        "apply": [
            arith("Una pelota recorre 90 cm, 96 cm y 84 cm en tres intentos. ¿Cuál es la diferencia entre el mayor y el menor de esos intentos?", "96-84", "Una diferencia pequeña indica que los intentos se parecen.", " cm"),
            arith("En el primer intento con la rampa baja la pelota recorrió 60 cm y con la alta recorrió 105 cm. ¿Cuántos cm más recorrió con la alta?", "105-60", "Se comparan los dos primeros intentos.", " cm"),
            ex("Quieres probar si la superficie del piso cambia la distancia. ¿Qué dejas igual?", "La pelota, la rampa y la altura", "Solo debe cambiar el piso."),
        ],
        "reason": [
            ex("Un grupo dice «la pelota más pesada llegó más lejos» porque usaron una pelota distinta en cada rampa. ¿Por qué esa conclusión no es confiable?", "Porque cambiaron la pelota y la rampa a la vez", "No se sabe cuál variable causó el resultado."),
            ex("Los datos: rampa baja 50 cm, rampa media 80 cm, rampa alta 110 cm. ¿Apoyan la predicción «a mayor altura, mayor distancia»?", "Sí", "La distancia crece al subir la rampa."),
        ],
        "challenge": [
            ex("Los datos de una prueba fueron 60 cm, 62 cm y 118 cm con la misma rampa. ¿Qué haces con el valor 118?", "Reviso si hubo un error y repito esa prueba", "Es muy distinto de los otros y puede ser un error."),
            ex("Escribe un límite posible de una investigación hecha con una sola pelota y un solo tipo de piso.", "Los resultados pueden no servir para otras pelotas u otros pisos", "Se probó en pocos casos."),
        ],
    },
    context=[arith("En una feria de ciencias, un curso mide la distancia de un carrito en cuatro intentos: 40 cm, 44 cm, 36 cm y 40 cm. ¿Cuántos cm más recorrió en el segundo intento que en el tercero?", "44-36", "Se comparan dos intentos con una resta.", " cm")],
    selfcheck=[
        ex("¿Qué dice una predicción?", "Lo que creo que pasará", "Se hace antes de probar."),
        ex("¿Qué debe citar una conclusión?", "Los datos", "Así se apoya en evidencia."),
        ex("Si repites una prueba y los números son parecidos, ¿el resultado es más confiable?", "Sí", "Un resultado que se repite es más seguro."),
    ],
    open_task=task(
        "Con una rampa hecha con un libro grande, haz rodar una pelota tres veces desde una altura baja y tres desde una alta, y mide cuánto avanza. Si no puedes, usa estos datos simulados: altura baja 40, 42 y 38 cm; altura alta 70, 74 y 66 cm. Calcula cuántos cm más recorrió la pelota en el primer intento de la altura alta, escribe tu predicción, tu conclusión con datos y un límite.",
        "En el primer intento, 70 − 40 = 30 cm más con la altura alta. Mi predicción era que más altura daría más distancia. Se cumplió en los tres intentos. Un límite es que usé solo una pelota.",
        ["calcula la diferencia", "compara con datos", "incluye predicción y límite"],
        ["tabla de seis datos", "conclusión escrita"],
        ["usar un solo intento", "no mencionar un límite"],
        "Valora la diferencia calculada y la comparación; pide agregar un límite si falta.",
    ),
    reinforce="Plantea una nueva pregunta que se pueda probar con la pelota y la rampa y escribe tu predicción.",
    extend="Piensa cómo cambiaría tu prueba si usaras una pelota más pesada y qué mantendrías igual.",
)

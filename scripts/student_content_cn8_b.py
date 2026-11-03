"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 11 (calor, temperatura y transferencia térmica)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA11 = "CN08 OA 11"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 11, clase 1
register(
    OA11, 1,
    materials="Papel y lápiz. Todos los datos están escritos en el cuaderno. Si quieres, puedes mirar un vaso con agua tibia en tu casa, sin hervir agua ni usar fuego.",
    use="Aprenderé a distinguir calor de temperatura y a formular preguntas investigables sobre la transferencia térmica. Sirve para planificar una medición con variables claras.",
    prior=["Sé que un modelo de partículas explica cómo se comporta la materia.", "Sé separar lo que observo de lo que interpreto."],
    explain=[
        "La temperatura es una medida de qué tan rápido se mueven, en promedio, las partículas de un cuerpo. Se mide con un termómetro. El calor es la energía térmica que pasa de un cuerpo a mayor temperatura a otro a menor temperatura. Un cuerpo no «guarda calor»: tiene energía térmica y, cuando hay una diferencia de temperatura, esa energía se transfiere. La transferencia continúa hasta el equilibrio térmico, cuando ambos cuerpos llegan a la misma temperatura.",
        "Dos cuerpos pueden tener la misma temperatura y distinta energía térmica total. Un balde con mucha agua tibia tiene más partículas que una taza con agua a la misma temperatura, así que tiene más energía térmica total. Por eso calor y temperatura no son sinónimos.",
        "Una pregunta investigable se puede responder midiendo. Tiene una variable que se cambia a propósito (independiente), una que se mide (dependiente) y varias que se mantienen iguales (controladas). «¿Cuántos grados baja el agua en 20 minutos en un vaso con tapa y en otro sin tapa?» es investigable. «¿Cuál vaso es más lindo?» no lo es.",
    ],
    vocab=[("temperatura", "medida de la rapidez promedio de las partículas de un cuerpo"), ("calor", "energía térmica que pasa de un cuerpo más caliente a uno más frío"), ("equilibrio térmico", "situación en que dos cuerpos en contacto tienen la misma temperatura"), ("variable independiente", "la que el investigador cambia a propósito"), ("variable dependiente", "la que se mide para ver el efecto"), ("variable controlada", "la que se mantiene igual en todas las pruebas")],
    worked=[
        {"title": "Convertir una duda en pregunta investigable", "problem": "Una estudiante quiere saber «cuál es el mejor vaso para que el té no se enfríe». Reescribe la duda como pregunta investigable.", "steps": ["Elige qué cambiar: el material del vaso (plumavit o metal). Elige qué medir: la temperatura del té cada 10 minutos.", "Fija lo que debe quedar igual: cantidad de té, temperatura inicial, tapa y lugar."], "answer": "¿Cuántos °C baja en 30 minutos el té de un vaso de plumavit y el de un vaso de metal, con igual cantidad, igual tapa y igual temperatura inicial?"},
        {"title": "Sentido de la transferencia", "problem": "Una cuchara a 70 °C se mete en agua a 25 °C. ¿Hacia dónde pasa el calor y qué ocurre con las temperaturas?", "steps": ["El calor pasa del cuerpo de mayor temperatura al de menor temperatura: de la cuchara al agua.", "La temperatura de la cuchara baja y la del agua sube hasta que se igualan."], "answer": "Del cuerpo más caliente (cuchara) al más frío (agua), hasta el equilibrio térmico"},
    ],
    mistakes=[
        {"wrong": "Decir que el hielo le «pasa frío» a la bebida.", "why": "Se imagina que el frío es algo que se transfiere.", "fix": "Lo que se transfiere es calor, de la bebida más caliente hacia el hielo."},
        {"wrong": "Pensar que, si dos cuerpos tienen la misma temperatura, tienen la misma energía térmica.", "why": "Se ignora la cantidad de partículas.", "fix": "La energía térmica total depende de la temperatura y de la cantidad de materia."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es el calor: A) una sustancia que se guarda dentro de los cuerpos o B) una transferencia de energía entre cuerpos con distinta temperatura?", "B)", "El calor es energía en tránsito, no una sustancia almacenada."),
            ex("Una taza a 70 °C toca un vaso a 20 °C. ¿En qué sentido pasa el calor?", "De la taza al vaso", "El calor va desde el cuerpo de mayor temperatura al de menor temperatura."),
            ex("A nivel de partículas, ¿qué indica la temperatura de un cuerpo?", "Qué tan rápido se mueven en promedio sus partículas", "La temperatura mide la rapidez promedio de las partículas."),
        ],
        "understand": [
            ex("¿Qué enunciado distingue bien calor y temperatura? A) El calor es lo que mide el termómetro; B) La temperatura mide la rapidez promedio de las partículas y el calor es energía que pasa entre cuerpos; C) Son dos nombres de lo mismo", "B)", "El termómetro mide temperatura, y el calor es el proceso de transferencia."),
            ex("¿Qué es el equilibrio térmico entre dos cuerpos en contacto?", "Cuando llegan a la misma temperatura", "Sin diferencia de temperatura ya no hay transferencia neta de calor."),
            ex("Quieres comparar cómo el material del vaso (plumavit o metal) afecta el enfriamiento del agua. ¿Qué debe mantenerse igual en los dos vasos? A) La cantidad de agua inicial; B) El material de cada vaso", "A)", "La cantidad de agua es una variable controlada; el material es la que se cambia."),
        ],
        "apply": [
            arith("El agua de un vaso baja de 64 °C a 41 °C en 20 minutos. ¿Cuántos °C bajó?", "64-41", "Se resta la temperatura final a la inicial.", " °C"),
            ex("¿Cuál es una pregunta investigable? A) ¿Cuántos °C baja en 15 minutos una botella con agua tibia envuelta en lana frente a otra envuelta en papel?; B) ¿Qué abrigo es mejor para todos?", "A)", "Tiene una variable que se cambia, otra que se mide y un tiempo fijo."),
            ex("La sala marca 22 °C y la mesa de madera, que está ahí desde anoche, también marca 22 °C. ¿Hay transferencia neta de calor entre la sala y la mesa?", "No, porque están a la misma temperatura", "Sin diferencia de temperatura no hay transferencia neta de calor."),
        ],
        "reason": [
            ex("Vaso 1: 100 mL de agua a 50 °C. Vaso 2: 400 mL de agua a 50 °C. Julia dice que tienen la misma energía térmica porque tienen la misma temperatura. ¿Es correcto?", "No; el vaso 2 tiene cuatro veces más agua, por lo que tiene más energía térmica total", "La energía térmica total depende también de la cantidad de partículas."),
            ex("Un compañero dice que al poner hielo en una bebida «entra frío» a la bebida. Reescribe la frase usando la idea de transferencia de calor.", "El calor pasa de la bebida, que está más caliente, al hielo", "Lo que se transfiere es calor, siempre desde lo más caliente."),
        ],
        "challenge": [
            ex("Datos de ejemplo (temperatura del agua en °C): minuto 0 con tapa 60 y sin tapa 60; minuto 30 con tapa 41 y sin tapa 31. ¿Qué vaso perdió más grados en 30 minutos y cuántos más que el otro?", "El vaso sin tapa; bajó 10 °C más", "Sin tapa bajó 29 °C y con tapa 19 °C; la diferencia es 10 °C.", calc="(60-31)-(60-41)"),
            ex("Quieres saber si el color del vaso (negro o blanco) cambia cuánto se calienta 200 mL de agua al sol en 30 minutos. ¿Qué plan es correcto? A) Cambiar el color, medir la temperatura del agua y mantener igual la cantidad de agua, el tiempo y el lugar; B) Cambiar la cantidad de agua, medir el color y mantener igual la temperatura; C) Cambiar el lugar, medir el tiempo y mantener igual el color", "A)", "Se cambia una sola variable (el color) y se mide el efecto en la temperatura."),
        ],
    },
    context=[ex("En una feria de ciencias, un grupo afirma que una bufanda «da calor» a una botella con agua tibia. ¿Qué compararían para ver si la bufanda frena la pérdida de calor?", "La temperatura del agua de una botella con bufanda y de otra sin bufanda, medida a intervalos iguales", "La bufanda no produce calor; se comprueba si disminuye la pérdida con una comparación.")],
    selfcheck=[
        ex("¿Hacia dónde pasa el calor entre dos cuerpos con distinta temperatura?", "Del más caliente al más frío", "La diferencia de temperatura determina el sentido de la transferencia."),
        ex("¿Qué instrumento mide la temperatura?", "El termómetro", "El termómetro entrega el valor de la temperatura, no del calor."),
        ex("En una investigación, ¿cómo se llama la variable que se mide para ver el efecto?", "Variable dependiente", "Depende de lo que se cambió en el experimento."),
    ],
    open_task=task(
        "Tienes estas dudas: (1) «¿Qué vaso conserva mejor el calor?» (2) «¿Por qué el invierno es feo?» (3) «¿Una botella con agua a 50 °C se enfría más rápido con tapa o sin tapa?». Elige la que se puede investigar y escribe: qué cambiarías, qué medirías (con su unidad) y tres variables que mantendrías iguales. Después reescribe la duda (1) como pregunta investigable.",
        "Elijo la (3). Cambio: con tapa o sin tapa. Mido: temperatura del agua en °C cada 10 minutos. Igual: cantidad de agua, temperatura inicial y lugar. La (1) queda: ¿Cuántos °C baja en 30 minutos el agua en un vaso de plumavit y en uno de metal, con igual cantidad y temperatura inicial?",
        ["elige la duda investigable", "nombra variable independiente y dependiente con unidad", "tres variables controladas", "reescribe la duda (1) con variables"],
        ["texto con las tres partes", "pregunta reescrita"],
        ["no incluir unidad de medida", "cambiar dos variables a la vez"],
        "Pregunta qué cambiaría en la pregunta si el termómetro solo se puede leer cada 15 minutos.",
    ),
    reinforce="Escribe dos frases cortas: una que use la palabra «temperatura» y otra que use la palabra «calor», cada una con su significado correcto.",
    extend="Con una persona de tu casa, anota en qué sentido pasa el calor cuando apoyas la mano en un vaso con agua tibia. Usa la frase «pasa de … a …».",
)

# ================================================================ OA 11, clase 2
register(
    OA11, 2,
    materials="Papel y lápiz. Las tablas y las fórmulas están escritas en el cuaderno.",
    use="Aprenderé a leer termómetros y tablas de temperatura y a convertir entre las escalas Celsius, Kelvin y Fahrenheit. Sirve para comparar mediciones hechas con instrumentos distintos.",
    prior=["Sé que la temperatura mide la rapidez promedio de las partículas.", "Sé leer una tabla de datos."],
    explain=[
        "Un termómetro de líquido funciona por dilatación: al aumentar la temperatura, las partículas del líquido se mueven más rápido, ocupan más espacio y el líquido sube por el tubo. Hay tres escalas. En la escala Celsius (°C), el agua se congela a 0 °C y hierve a 100 °C al nivel del mar. En la escala Kelvin (K), esos puntos son 273 K y 373 K, y el 0 K es la temperatura más baja posible. En la escala Fahrenheit (°F), son 32 °F y 212 °F.",
        "Para convertir: K = °C + 273. °F = °C × 9 ÷ 5 + 32. °C = (°F − 32) × 5 ÷ 9. Un intervalo de 1 °C es igual a un intervalo de 1 K, por eso una subida de 10 °C es también una subida de 10 K. En Fahrenheit, el grado es más pequeño.",
        "Para examinar una tabla de tiempo y temperatura, busca cuánto cambió la temperatura en cada intervalo. Un cuerpo caliente se enfría rápido al principio y cada vez más lento, porque la diferencia con el ambiente se va haciendo menor y pasa menos calor por minuto.",
    ],
    vocab=[("dilatación", "aumento de volumen de un cuerpo cuando sube su temperatura"), ("escala Celsius", "escala con 0 °C en el congelamiento del agua y 100 °C en su ebullición"), ("kelvin", "unidad de la escala que parte en el 0 absoluto, igual a −273 °C"), ("grado Fahrenheit", "unidad de una escala en que el agua se congela a 32 °F"), ("intervalo", "diferencia entre dos valores medidos")],
    worked=[
        {"title": "De Celsius a Kelvin", "problem": "Una muestra está a 25 °C. ¿Cuántos kelvin son?", "steps": ["Se usa K = °C + 273.", "25 + 273 = 298."], "answer": "298 K"},
        {"title": "De Celsius a Fahrenheit", "problem": "Un horno de secado de ejemplo está a 50 °C. ¿Cuántos °F son?", "steps": ["Se usa °F = °C × 9 ÷ 5 + 32.", "50 × 9 = 450; 450 ÷ 5 = 90; 90 + 32 = 122."], "answer": "122 °F"},
    ],
    mistakes=[
        {"wrong": "Convertir de °C a K restando 273.", "why": "Se invierte la operación.", "fix": "A los °C se les suma 273 para obtener K."},
        {"wrong": "Decir que 86 °F es lo mismo que 86 °C.", "why": "Se ignora que las escalas parten de puntos distintos y sus grados tienen otro tamaño.", "fix": "Siempre convierte con la fórmula antes de comparar."},
    ],
    tiers={
        "recovery": [
            arith("Un termómetro marca 30 °C. ¿Cuántos kelvin son?", "30+273", "Se suma 273 a la temperatura en °C.", " K"),
            ex("¿A cuántos kelvin hierve el agua al nivel del mar?", "373 K", "100 °C más 273 da 373 K."),
            ex("¿Cuántos °F marca un termómetro Fahrenheit cuando el agua se congela?", "32 °F", "El punto de congelamiento del agua en esa escala es 32 °F."),
        ],
        "understand": [
            ex("¿Por qué sube el líquido de un termómetro al calentarse? A) Porque el líquido se dilata al moverse más rápido sus partículas; B) Porque el calor es un líquido que entra por el tubo; C) Porque el vidrio se achica", "A)", "Con más temperatura, las partículas se agitan, ocupan más espacio y el líquido sube."),
            ex("¿Qué escala tiene su cero en la temperatura más baja posible?", "Kelvin", "El 0 K equivale a −273 °C."),
            ex("La temperatura de una muestra sube 10 °C. ¿Cuántos kelvin sube?", "10 K", "Un intervalo de 1 °C es igual a un intervalo de 1 K."),
        ],
        "apply": [
            arith("Una muestra está a 80 °C. ¿Cuántos kelvin son?", "80+273", "Se suma 273 a los °C.", " K"),
            arith("Un termómetro marca 40 °C. ¿Cuántos °F son?", "40*9//5+32", "Se multiplica por 9, se divide por 5 y se suma 32.", " °F"),
            ex("Una muestra está a 300 K. ¿Cuántos °C son?", "27 °C", "Se resta 273 a los kelvin.", calc="300-273"),
        ],
        "reason": [
            ex("Tabla de ejemplo del agua de una taza que se enfría en una sala (minuto: °C): 0: 90; 5: 70; 10: 58; 15: 50; 20: 45. ¿En qué intervalo de 5 minutos bajó más la temperatura y cuántos °C?", "Entre el minuto 0 y el 5; bajó 20 °C", "La diferencia es 90 menos 70, la mayor de la tabla.", calc="90-70"),
            ex("En la misma tabla, el agua se enfría cada vez más lento. ¿Por qué? A) Porque al acercarse a la temperatura de la sala hay menos diferencia y pasa menos calor por minuto; B) Porque el agua se queda sin calor; C) Porque el termómetro se descompone", "A)", "El calor pasa por la diferencia de temperatura, que se reduce con el tiempo."),
        ],
        "challenge": [
            ex("En una playa extranjera un termómetro Fahrenheit marca 86 °F. Un compañero dice que son 86 K. ¿Cuántos °C son realmente?", "30 °C; las escalas parten de puntos distintos", "(86 − 32) × 5 ÷ 9 = 30; no se pueden leer como si fueran iguales.", calc="(86-32)*5//9"),
            ex("Mateo midió el agua de un baño con dos termómetros: uno marca 35 °C y el otro 95 °F. ¿Coinciden?", "Sí, 35 °C equivalen a 95 °F", "35 × 9 ÷ 5 + 32 = 95, así que las lecturas coinciden.", calc="35*9//5+32"),
        ],
    },
    context=[ex("El pronóstico de una ciudad extranjera indica 68 °F para el mediodía. ¿Cuántos °C son?", "20 °C", "(68 − 32) × 5 ÷ 9 = 20.", calc="(68-32)*5//9")],
    selfcheck=[
        ex("¿Cuánto es 0 K en grados Celsius?", "-273 °C", "El cero absoluto está 273 grados bajo el cero Celsius.", calc="0-273"),
        ex("¿Qué fenómeno del líquido permite que funcione un termómetro?", "La dilatación", "El líquido ocupa más volumen al subir la temperatura."),
        ex("¿Qué operación se hace con 273 para pasar de °C a K?", "Sumarlo", "K es igual a °C más 273."),
    ],
    open_task=task(
        "Una persona midió la temperatura del agua mientras se enfriaba en una sala y anotó estos datos de ejemplo (minuto: °C): 0: 80; 10: 56; 20: 44; 30: 38; 40: 35. (1) Convierte a K la primera y la última medición. (2) Calcula cuántos °C bajó en cada intervalo de 10 minutos. (3) Escribe en una frase por qué la baja se hace más lenta.",
        "(1) 353 K y 308 K. (2) Bajó 24, 12, 6 y 3 °C. (3) Se enfría más lento porque cada vez hay menos diferencia de temperatura con la sala.",
        ["dos conversiones correctas", "cuatro diferencias", "explicación con diferencia de temperatura"],
        ["tabla de intervalos", "frase de explicación"],
        ["restar 273 en vez de sumar", "decir que el agua «pierde ganas» de enfriarse"],
        "Pregunta cuántos °F marcaría la primera medición y cómo lo calculó.",
    ),
    reinforce="Escribe los tres puntos de congelamiento del agua en °C, K y °F.",
    extend="Con una persona de tu casa, busca un termómetro (de clima o de cuerpo) y anota qué escala usa y cuál sería la lectura en K.",
)

# ================================================================ OA 11, clase 3
register(
    OA11, 3,
    materials="Papel y lápiz. Los casos están escritos en el cuaderno.",
    use="Aprenderé el modelo de partículas de la conducción, la convección y la radiación, y cómo lo usan los objetos que protegen del calor o del frío. Sirve para explicar por qué un material abriga o enfría.",
    prior=["Sé qué es el calor y qué es la temperatura.", "Sé que las partículas de un gas y un líquido se mueven más que las de un sólido."],
    explain=[
        "Hay tres formas de propagación del calor. En la conducción, el calor pasa por choques entre partículas vecinas, sobre todo en sólidos. Los metales conducen muy bien; la madera, el plumavit y el aire quieto conducen mal y se llaman aislantes. En la convección, el calor viaja con el movimiento de un fluido (líquido o gas): el fluido caliente se dilata, queda menos denso y sube, mientras el frío baja, y se forman corrientes. En la radiación, la energía viaja como ondas, incluso por el vacío; así llega el calor del Sol.",
        "El calor produce efectos: cambio de temperatura, dilatación (los cuerpos aumentan de tamaño, lo que los deforma si están sujetos) y cambio de estado. Los objetos tecnológicos usan estas ideas. Una chaqueta de plumas atrapa aire que conduce mal. Un termo tiene doble pared con vacío entre ellas, que frena la conducción y la convección, y una cara plateada que refleja la radiación. Un traje de bombero lleva una capa reflectante.",
        "Para explicar con el modelo, nombra la forma de propagación y di qué hacen las partículas. Un objeto que protege no crea calor ni frío: frena la transferencia de calor.",
    ],
    vocab=[("conducción", "paso de calor por choques entre partículas vecinas"), ("convección", "paso de calor con el movimiento de un líquido o un gas"), ("radiación", "paso de energía por ondas, incluso en el vacío"), ("aislante térmico", "material que conduce mal el calor"), ("conductor térmico", "material que conduce bien el calor")],
    worked=[
        {"title": "El mango de una sartén", "problem": "Una sartén de metal se calienta en la cocina y, después de un rato, el mango también está caliente. ¿Qué forma de propagación actúa?", "steps": ["El calor pasa por el metal sólido, sin que el material se mueva.", "Las partículas chocan con sus vecinas y se pasan la energía."], "answer": "Conducción"},
        {"title": "El Sol y la Tierra", "problem": "¿Por qué el calor del Sol no puede llegar a la Tierra por conducción ni por convección?", "steps": ["Entre el Sol y la Tierra hay casi vacío, sin partículas que choquen ni fluido que se mueva.", "La energía viaja como ondas, que sí atraviesan el vacío."], "answer": "Por radiación"},
    ],
    mistakes=[
        {"wrong": "Decir que una frazada «da calor».", "why": "Se piensa que el objeto crea calor.", "fix": "La frazada frena la pérdida de calor de tu cuerpo al atrapar aire."},
        {"wrong": "Creer que el aire caliente baja y el frío sube.", "why": "Se olvida que el aire caliente es menos denso.", "fix": "El aire caliente sube y el frío baja, y eso forma la convección."},
    ],
    tiers={
        "recovery": [
            ex("Un extremo de una barra de cobre se calienta y, a los pocos minutos, el otro extremo también. ¿Qué forma de propagación ocurre?", "Conducción", "El calor pasa por choques entre partículas de un sólido."),
            ex("El aire caliente sube sobre un calefactor y el aire frío baja. ¿Qué forma de propagación es?", "Convección", "Es movimiento de un fluido que transporta el calor."),
            ex("¿Qué forma de propagación no necesita ningún material para ocurrir?", "La radiación", "Las ondas viajan incluso por el vacío."),
        ],
        "understand": [
            ex("¿Por qué no hay convección en un trozo de metal sólido? A) Porque sus partículas no pueden desplazarse como en un fluido; B) Porque el metal no conduce el calor; C) Porque el metal no tiene temperatura", "A)", "La convección necesita que el material fluya."),
            ex("¿Por qué abriga una chaqueta de plumas? A) Porque las plumas generan calor; B) Porque el aire atrapado entre ellas conduce mal el calor y frena la pérdida; C) Porque las plumas reflejan el frío", "B)", "El aire quieto es aislante, y frena la transferencia desde el cuerpo."),
            ex("En un termo, el vacío entre las paredes frena la conducción y la convección. ¿Por qué?", "Porque sin partículas no hay choques ni fluido que se mueva", "Ambas formas de propagación necesitan materia."),
        ],
        "apply": [
            ex("Dos tubos idénticos, uno de metal y otro de plástico, tienen un extremo a 70 °C. A los 5 minutos, el otro extremo marca 55 °C en el metal y 28 °C en el plástico. ¿Qué tubo conduce mejor y cuántos °C más marca?", "El de metal; marca 27 °C más", "El otro extremo se calentó más en el metal, y 55 menos 28 son 27.", calc="55-28"),
            ex("¿Qué material conviene para el mango de una olla? A) Cobre, que conduce muy bien el calor; B) Madera, que conduce mal el calor", "B)", "Un mango aislante evita que el calor llegue a la mano."),
            ex("Un calefactor calienta una pieza. ¿Dónde conviene ponerlo para calentar mejor el aire de la pieza por convección? A) Cerca del suelo; B) Cerca del techo", "A)", "El aire caliente sube y deja espacio al aire frío, que baja y se calienta."),
        ],
        "reason": [
            ex("Un compañero dice que las frazadas «dan calor». Explica con la idea de transferencia qué hacen realmente.", "Frenan la pérdida de calor del cuerpo porque atrapan aire que conduce mal", "Un aislante reduce la transferencia, no produce calor."),
            ex("Las casas de zonas frías llevan lana mineral o plumavit en el techo. ¿Qué logran? A) Frenar la conducción del calor hacia el exterior; B) Producir calor dentro de la casa", "A)", "Los aislantes reducen el paso de calor por conducción."),
        ],
        "challenge": [
            ex("Relaciona cada parte de un termo con lo que frena: (1) vacío entre paredes; (2) cara interior plateada. Elige entre «conducción y convección» y «radiación».", "(1) conducción y convección; (2) radiación", "El vacío no tiene partículas y la cara plateada refleja las ondas."),
            ex("El traje de un bombero lleva una capa externa reflectante. ¿Qué forma de propagación frena principalmente esa capa?", "La radiación", "Una capa que refleja devuelve las ondas del fuego en lugar de absorberlas."),
        ],
    },
    context=[ex("En una mañana helada, un pájaro esponja sus plumas. ¿Cómo ayuda eso a perder menos calor?", "Atrapa más aire entre las plumas, que conduce mal el calor", "El aire quieto actúa como aislante, igual que en una chaqueta.")],
    selfcheck=[
        ex("¿Cuál forma de propagación explica que el agua de una olla se caliente por completo cuando el fuego está abajo?", "La convección", "El agua caliente sube y la fría baja, y se mueve todo el líquido."),
        ex("¿Qué es un aislante térmico?", "Un material que conduce mal el calor", "Frena la transferencia de calor."),
        ex("¿Qué efecto del calor hace que un riel de tren aumente su largo en verano?", "La dilatación", "El sólido aumenta de tamaño cuando sube su temperatura."),
    ],
    open_task=task(
        "Una cocina tiene: (1) una cuchara de metal en una olla con sopa tibia; (2) vapor que sube de la olla; (3) una persona sentada al sol que siente calor en la cara. Para cada caso, escribe qué forma de propagación predomina (conducción, convección o radiación) y qué hacen las partículas o las ondas. Después propone un objeto de tu casa que proteja del frío y explica qué transferencia frena.",
        "(1) Conducción: las partículas de la cuchara chocan y pasan la energía por el metal. (2) Convección: el vapor caliente sube y arrastra energía. (3) Radiación: el Sol emite ondas que llegan a la cara. Objeto: una frazada, que atrapa aire y frena la conducción.",
        ["tres casos clasificados", "una explicación con partículas u ondas por caso", "un objeto con su transferencia frenada"],
        ["tabla de tres filas", "frase final del objeto"],
        ["decir que el objeto «da calor»", "usar solo la palabra «calor» sin nombrar la forma"],
        "Pregunta qué cambiaría en el caso 1 si la cuchara fuera de madera.",
    ),
    reinforce="Escribe un ejemplo de tu casa para cada forma de propagación: conducción, convección y radiación.",
    extend="Con una persona de tu casa, busca dos objetos que sean aislantes y dos que sean conductores del calor. Anota de qué material están hechos.",
)

# ================================================================ OA 11, clase 4
register(
    OA11, 4,
    materials="Papel y lápiz. Las fórmulas y los datos están escritos en el cuaderno.",
    use="Aprenderé a calcular el calor cedido y absorbido con Q = m × c × ΔT. Sirve para predecir cuánto cambia la temperatura de un cuerpo y la temperatura final de una mezcla.",
    prior=["Sé que el calor pasa del cuerpo más caliente al más frío.", "Sé usar las escalas de temperatura."],
    explain=[
        "La cantidad de calor Q que absorbe o cede un cuerpo depende de tres cosas: su masa (m), de qué sustancia es y cuánto cambia su temperatura (ΔT). La fórmula es Q = m × c × ΔT. La masa se mide en gramos, ΔT en °C y Q en calorías (cal). La letra c es el calor específico: las calorías necesarias para subir 1 °C la temperatura de 1 g de la sustancia. Para el agua, c vale 1 cal/(g·°C).",
        "ΔT es la temperatura final menos la inicial. Si el cuerpo se calienta, ΔT y Q son positivos: absorbe calor. Si se enfría, son negativos: cede calor. Si dos cuerpos se mezclan en un recipiente aislado, el calor que cede el más caliente es igual al que absorbe el más frío, porque la energía no desaparece.",
        "Cuando se mezclan masas iguales de la misma sustancia, la temperatura final es el promedio de las dos temperaturas. Si las masas son distintas, hay que igualar el calor cedido con el absorbido o usar el promedio ponderado por la masa: (m1 × T1 + m2 × T2) ÷ (m1 + m2), donde T1 y T2 son las temperaturas iniciales de cada masa.",
    ],
    vocab=[("caloría (cal)", "unidad de calor; calienta 1 g de agua en 1 °C"), ("calor específico (c)", "calor para subir 1 °C la temperatura de 1 g de una sustancia"), ("ΔT", "cambio de temperatura: temperatura final menos inicial"), ("sistema aislado", "recipiente en que no entra ni sale calor")],
    worked=[
        {"title": "Calor para calentar agua", "problem": "¿Cuántas calorías absorbe una masa de 200 g de agua al pasar de 20 °C a 50 °C?", "steps": ["ΔT = 50 − 20 = 30 °C.", "Q = 200 × 1 × 30 = 6.000 cal."], "answer": "6.000 cal"},
        {"title": "Mezcla de masas iguales", "problem": "En un recipiente aislado se mezclan 150 g de agua a 70 °C con 150 g de agua a 30 °C. ¿Cuál es la temperatura final?", "steps": ["Las masas y la sustancia son iguales: la temperatura final es el promedio.", "(70 + 30) ÷ 2 = 50 °C. Comprobación: el agua caliente cede 150 × 20 = 3.000 cal y la fría absorbe 150 × 20 = 3.000 cal."], "answer": "50 °C"},
    ],
    mistakes=[
        {"wrong": "Calcular ΔT como temperatura inicial menos final.", "why": "Se cambia el orden de la resta.", "fix": "ΔT es la temperatura final menos la inicial."},
        {"wrong": "Usar solo la masa y olvidar el calor específico.", "why": "Se piensa que todas las sustancias absorben igual.", "fix": "Cada sustancia tiene su propio c, que debe multiplicarse."},
    ],
    tiers={
        "recovery": [
            arith("¿Cuántas calorías necesita una masa de 100 g de agua para subir 10 °C?", "100*1*10", "Q = m × c × ΔT con c igual a 1 para el agua.", " cal"),
            ex("En un cálculo de calor, el resultado de Q es negativo. ¿Qué indica?", "Que el cuerpo cede calor", "Q negativo corresponde a un enfriamiento."),
            arith("Un cuerpo pasa de 15 °C a 40 °C. ¿Cuál es su ΔT?", "40-15", "Se resta la temperatura inicial a la final.", " °C"),
        ],
        "understand": [
            ex("Si se duplica la masa de agua y el ΔT es el mismo, ¿qué pasa con Q? A) Se duplica; B) Se mantiene; C) Se reduce a la mitad", "A)", "Q es proporcional a la masa en Q = m × c × ΔT."),
            ex("La sustancia Z tiene c = 2 cal/(g·°C), valor de ejemplo, y el agua 1. Con la misma masa y el mismo ΔT, ¿cuál necesita más calor?", "La sustancia Z", "Un c mayor significa más calor por cada grado."),
            ex("En un recipiente aislado, ¿por qué el calor cedido por el cuerpo caliente es igual al absorbido por el frío?", "Porque la energía no desaparece, solo pasa de un cuerpo a otro", "Si no entra ni sale calor, lo que uno pierde lo gana el otro."),
        ],
        "apply": [
            arith("Una masa de 250 g de agua sube de 18 °C a 38 °C. ¿Cuántas calorías absorbe?", "250*1*(38-18)", "Se multiplica la masa por c y por ΔT.", " cal"),
            arith("Una masa de 150 g de agua recibe 3.000 cal. ¿Cuántos °C sube su temperatura?", "3000//(150*1)", "Se divide Q por m × c.", " °C"),
            arith("Una masa de 50 g de la sustancia Z (c = 2 cal/(g·°C), valor de ejemplo) sube 12 °C. ¿Cuántas calorías absorbe?", "50*2*12", "Q = m × c × ΔT con c igual a 2.", " cal"),
        ],
        "reason": [
            arith("Se mezclan 200 g de agua a 60 °C con 200 g de agua a 20 °C en un recipiente aislado. ¿Cuál es la temperatura final en °C?", "(60+20)//2", "Con masas iguales de agua, la temperatura final es el promedio.", " °C"),
            ex("Ana calienta 100 g de agua y Beto 100 g de la sustancia Z (c = 2, valor de ejemplo). Los dos suben de 20 °C a 40 °C. ¿Quién recibe más calor y cuántas calorías más?", "Beto; 2.000 cal más", "Ana recibe 2.000 cal y Beto 4.000 cal.", calc="100*2*20-100*1*20"),
        ],
        "challenge": [
            arith("Se mezclan 100 g de agua a 80 °C con 300 g de agua a 20 °C en un recipiente aislado. ¿Cuál es la temperatura final en °C?", "(100*80+300*20)//400", "Se pondera por la masa y se divide por la masa total; el calor cedido es 4.500 cal y el absorbido también.", " °C"),
            arith("Un cuerpo de agua de 200 g cede 4.000 cal. ¿Cuántos °C baja su temperatura?", "4000//(200*1)", "Se divide el calor entre la masa y el calor específico.", " °C"),
        ],
    },
    context=[ex("Un calefón calienta 10 litros de agua (unos 10.000 g) de 15 °C a 40 °C para una ducha. ¿Cuántas calorías absorbe el agua?", "250.000 cal", "ΔT = 25 °C, y 10.000 × 1 × 25 = 250.000.", calc="10000*1*25")],
    selfcheck=[
        ex("¿Cuál es el calor específico del agua?", "1 cal/(g·°C)", "Es el valor de referencia para el agua."),
        ex("En Q = m × c × ΔT, ¿cuánto vale Q si ΔT es 0?", "0", "Sin cambio de temperatura no hay calor absorbido ni cedido con esta fórmula."),
        ex("¿En qué unidad se expresa Q en esta clase?", "Calorías (cal)", "Es la unidad del calor usada con gramos y °C."),
    ],
    open_task=task(
        "Una botella con 500 g de agua a 20 °C se deja al sol y llega a 32 °C. En otra botella, 500 g de la sustancia Z (c = 2 cal/(g·°C), valor de ejemplo) comienza a 20 °C y recibe el mismo calor. Calcula: (1) las calorías que absorbió el agua; (2) cuántos °C subió la temperatura de la sustancia Z con ese mismo calor. Escribe cada paso con su fórmula y una frase que explique por qué subió menos.",
        "(1) ΔT = 12 °C; Q = 500 × 1 × 12 = 6.000 cal. (2) ΔT = 6.000 ÷ (500 × 2) = 6 °C. Subió menos porque su c es mayor: necesita más calor por cada grado.",
        ["Q calculado con fórmula", "ΔT de Z calculado", "explicación con calor específico"],
        ["dos cálculos escritos con pasos", "frase de explicación"],
        ["invertir la resta de ΔT", "olvidar multiplicar por c"],
        "Pregunta cuánto calor haría falta para que Z subiera los mismos 12 °C que el agua.",
    ),
    reinforce="Escribe la fórmula de Q con sus tres variables y la unidad de cada una.",
    extend="Con una persona de tu casa, estima cuántos gramos de agua caben en una taza y calcula las calorías que necesita esa agua para subir 20 °C.",
)

# ================================================================ OA 11, clase 5
register(
    OA11, 5,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a explicar patrones térmicos con evidencia y a usar el modelo de partículas para argumentar. Sirve para defender una conclusión sobre aislantes, cambios de estado y calentamiento de materiales.",
    prior=["Sé las formas de propagación del calor.", "Sé calcular calor con Q = m × c × ΔT."],
    explain=[
        "Para explicar un patrón térmico se usa una estructura de tres partes: afirmación (lo que concluyes), evidencia (los datos que la apoyan) y razonamiento (el mecanismo con partículas que une los dos). Por ejemplo, el metal se siente más frío que la madera a la misma temperatura porque conduce mejor el calor y se lo quita más rápido a tu mano.",
        "Durante un cambio de estado, como la fusión del hielo, la temperatura se mantiene mientras hay mezcla de hielo y agua. El calor que se recibe se usa para separar partículas, no para moverlas más rápido. Cuando todo el hielo se fundió, el agua vuelve a subir su temperatura.",
        "Un material con mayor calor específico, como el agua, se calienta y enfría más lento. Por eso el mar se calienta más despacio que la arena. Una conclusión debe declarar su límite: una sola medición o un solo material no permiten generalizar.",
    ],
    vocab=[("afirmación", "conclusión que se quiere defender"), ("evidencia", "datos medidos que apoyan la afirmación"), ("razonamiento", "explicación con el modelo que conecta los datos con la afirmación"), ("cambio de estado", "paso entre sólido, líquido y gas, como la fusión"), ("fusión", "paso de sólido a líquido")],
    worked=[
        {"title": "Metal y madera", "problem": "Una baranda de metal y una de madera están a 10 °C. La de metal se siente más fría. ¿Cómo lo explicas?", "steps": ["Afirmación: el metal se siente más frío aunque ambas están a 10 °C. Evidencia: tu mano está a más temperatura que las dos.", "Razonamiento: el metal conduce mejor y se lleva el calor de tu mano más rápido."], "answer": "El metal es mejor conductor y quita calor a la mano más rápido"},
        {"title": "Temperatura constante en el hielo", "problem": "Un termómetro marca 0 °C durante varios minutos en una mezcla de hielo y agua que recibe calor. ¿Qué indica?", "steps": ["La temperatura no sube aunque entra calor.", "Ese calor se usa para fundir el hielo, separando partículas."], "answer": "Que el calor se usa en el cambio de estado"},
    ],
    mistakes=[
        {"wrong": "Concluir que el material con la temperatura más baja al tocarlo está realmente más frío.", "why": "Se confunde sensación con temperatura.", "fix": "Mide con termómetro: la sensación depende de qué tan rápido el material conduce el calor."},
        {"wrong": "Afirmar que, durante la fusión, la temperatura sigue subiendo.", "why": "Se piensa que todo calor aumenta la temperatura.", "fix": "Durante el cambio de estado la temperatura se mantiene y el calor separa partículas."},
    ],
    tiers={
        "recovery": [
            ex("Durante la fusión de un hielo, ¿qué pasa con la temperatura de la mezcla de hielo y agua?", "Se mantiene constante", "El calor se usa en separar partículas."),
            ex("Una mesa de metal y una de madera están a 12 °C. ¿Por qué la de metal se siente más fría?", "Porque conduce mejor el calor y se lo quita más rápido a la mano", "La sensación depende de la rapidez de conducción."),
            ex("Una botella con agua se calienta más lento que un tarro con aceite de la misma masa. ¿Qué propiedad del agua lo explica?", "Su mayor calor específico", "Necesita más calor para subir cada grado."),
        ],
        "understand": [
            ex("Durante la ebullición del agua, el calor recibido se usa en: A) Subir la temperatura sin límite; B) Separar las partículas del líquido para que pasen a gas; C) Enfriar el recipiente", "B)", "Por eso la temperatura se mantiene durante el cambio de estado."),
            ex("Un termómetro marca 0 °C seis minutos mientras un hielo recibe calor. ¿Qué conclusión prudente se puede sacar? A) El hielo no recibe calor; B) El calor recibido se usa en cambiar de estado; C) El termómetro falló", "B)", "La temperatura constante con entrada de calor indica cambio de estado."),
            ex("Un grupo midió una sola vez la temperatura de cada vaso. ¿Qué limitación tiene su conclusión?", "Una sola medición no permite saber si la diferencia es casual", "Repetir mediciones da más confianza."),
        ],
        "apply": [
            ex("Datos de ejemplo (minuto: °C) del calentamiento de hielo con una fuente de calor constante: 0: −10; 2: 0; 34: 0; 36: 5. ¿Cuántos minutos se mantuvo la temperatura en 0 °C mientras el hielo se fundía?", "32 minutos", "La temperatura quedó en 0 °C desde el minuto 2 hasta el 34, porque el calor se usó en fundir el hielo.", calc="34-2"),
            ex("Un recipiente con agua se calienta desde abajo. ¿Qué agua sube: la más caliente o la más fría?", "La más caliente", "El agua caliente es menos densa y sube por convección."),
            arith("Una masa de 100 g de agua a 25 °C recibe 6.000 cal sin cambio de estado ni pérdidas. ¿Cuál es su temperatura final en °C?", "25+6000//(100*1)", "ΔT = Q ÷ (m × c) y se suma a la temperatura inicial.", " °C"),
        ],
        "reason": [
            ex("Carla afirma que la lana aísla mejor que el papel de aluminio. Datos de ejemplo tras 30 minutos, con agua inicial a 60 °C: con lana, 47 °C; con aluminio, 38 °C; sin envolver, 33 °C. ¿Cuántos °C más conservó la lana que el aluminio?", "9 °C más", "47 menos 38 es 9, y eso apoya su afirmación.", calc="47-38"),
            ex("En los mismos datos, ¿qué explica que la botella con lana quede a 47 °C y la descubierta a 33 °C? A) La lana atrapa aire que conduce mal y frena la pérdida de calor; B) La lana produce calor; C) La lana refleja el frío", "A)", "El aire atrapado es aislante y reduce la transferencia."),
        ],
        "challenge": [
            ex("Una mesa de piedra y una de plástico pasaron la noche en una pieza a 12 °C. Si la piedra conduce mejor el calor, ¿cuál se sentirá más fría al tocarla y qué marcaría un termómetro sobre cada una?", "La de piedra; ambas marcan 12 °C", "La sensación depende de la conducción, no de la temperatura, que es la misma."),
            ex("Una mezcla de hielo y agua en equilibrio marca 273 K. ¿Cuántos °C son?", "0 °C", "273 menos 273 es 0, el punto de fusión del hielo.", calc="273-273"),
        ],
    },
    context=[ex("Una olla de sopa a 95 °C con tapa se enfría más lento que sin tapa. ¿Qué frena la tapa?", "La salida de aire caliente por convección", "La tapa impide que el aire caliente se lleve la energía hacia arriba.")],
    selfcheck=[
        ex("En la estructura afirmación-evidencia-razonamiento, ¿qué parte corresponde a los datos medidos?", "La evidencia", "Los datos apoyan la afirmación."),
        ex("¿Qué se mantiene constante mientras ocurre un cambio de estado?", "La temperatura", "El calor se usa en separar partículas."),
        ex("Un material con mayor calor específico, ¿se calienta más rápido o más lento?", "Más lento", "Necesita más calor por cada grado."),
    ],
    open_task=task(
        "Una familia de ejemplo compara dos termos: A y B. Los dos tienen 300 g de agua a 80 °C. A las 3 horas, el termo A marca 62 °C y el termo B 41 °C. El termo A tiene vacío entre las paredes y el B no. Escribe una explicación con afirmación, evidencia y razonamiento (con conducción, convección o radiación). Añade una limitación de este estudio.",
        "Afirmación: el termo A conserva mejor el calor. Evidencia: bajó 18 °C y el B bajó 39 °C. Razonamiento: el vacío no tiene partículas, así que frena la conducción y la convección. Limitación: solo se probó un termo de cada tipo y no sabemos la temperatura de la sala.",
        ["afirmación clara", "dos datos como evidencia", "razonamiento con partículas", "una limitación"],
        ["texto de tres partes", "limitación declarada"],
        ["no usar datos numéricos", "decir que el vacío «guarda» el calor"],
        "Pregunta qué otro dato necesitarías para generalizar a todos los termos.",
    ),
    reinforce="Escribe una explicación de dos oraciones de por qué el mar se calienta más lento que la arena, usando «calor específico».",
    extend="Con una persona de tu casa, busca tres objetos que sirvan para frenar el calor o el frío y escribe qué transferencia frena cada uno.",
)

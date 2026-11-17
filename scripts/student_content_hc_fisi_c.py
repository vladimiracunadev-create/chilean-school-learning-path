"""Física (electivo HC, 3.º y 4.º medio): OAC-05 (física aplicada a sistemas naturales: fluidos, electromagnetismo y termodinámica), clases 1 a 6,
y OAC-06 (integración con otras ciencias y valoración ética, social y ambiental), clases 1 a 4.
Todo en papel: sin laboratorio, sin electricidad de red ni fuentes de calor. Los datos son de ejemplo y están escritos en cada ficha."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel; calculadora simple opcional. No se necesita laboratorio, instrumentos, fuentes de calor ni electricidad de red: "
             "todos los datos son de ejemplo (inventados o redondeados para practicar) y están escritos en la ficha. Las constantes que aparecen "
             "(g ≈ 10 m/s², densidad del agua dulce 1000 kg/m³, calor específico del agua de unos 4200 J/(kg·°C)) son valores aproximados y se rotulan como tales. "
             "Los casos se resuelven por cálculo: no se calienta nada ni se conecta ningún aparato.")
build = make_build(MATERIALS)

O5 = "CN-FISI-3y4-OAC-05"
O6 = "CN-FISI-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (de ejemplo; g ≈ 10 m/s²). Densidad del agua dulce: 1000 kg/m³; del agua de mar, de ejemplo: 1030 kg/m³. Presión atmosférica: unos 100.000 Pa (pascal, 1 Pa = 1 N/m²). "
     "Presión del agua a profundidad h: P agua = ρ × g × h. Presión total: P = P atmosférica + ρ × g × h. Fuerza sobre una superficie: F = P × A.")
build(
    O5, 1, F,
    use="Aprenderé a delimitar un problema de presión en océanos y lagos, a calcular cómo aumenta la presión con la profundidad y a reconocer las variables que importan.",
    prior=["Sé qué es la densidad.", "Sé que la gravedad atrae los cuerpos hacia la Tierra.", "Sé multiplicar y dividir con números grandes."],
    explain=[
        "La mecánica de fluidos estudia líquidos y gases. En un fluido en reposo, como el agua de un lago, la presión es la fuerza que ejerce el fluido por cada metro cuadrado, y se mide en pascales (Pa). La presión aumenta con la profundidad porque hay más agua encima: P agua = ρ × g × h, donde ρ es la densidad, g ≈ 10 m/s² y h la profundidad. La presión no depende de la forma del recipiente ni de su ancho.",
        "A la presión del agua se suma la de la atmósfera, que actúa sobre la superficie: P total = P atmosférica + ρ × g × h. En agua dulce, cada 10 m de profundidad suman 1000 × 10 × 10 = 100.000 Pa, es decir, otra atmósfera. Por eso a 10 m la presión total es el doble que en la superficie. La fuerza sobre una superficie se calcula como F = P × A, y explica por qué submarinos e instrumentos del fondo del mar necesitan paredes muy resistentes.",
        "Delimitar el problema significa decidir qué sistema se estudia (una columna de agua de un lago, el océano frente a la costa), qué variables se miden (profundidad, densidad, presión) y qué supuestos se aceptan (agua en reposo, densidad constante, g constante). El agua de mar es algo más densa que la dulce por la sal, así que la presión crece un poco más rápido con la profundidad.",
    ],
    vocab=[("presión", "fuerza por unidad de área, en pascales (Pa)"), ("pascal (Pa)", "unidad de presión: 1 N por m²"), ("densidad (ρ)", "masa por unidad de volumen, en kg/m³"), ("profundidad (h)", "distancia vertical bajo la superficie"), ("presión atmosférica", "presión del aire sobre la superficie, unos 100.000 Pa"), ("fluido en reposo", "líquido o gas sin movimiento neto")],
    worked=[
        ("Presión del agua", "¿Qué presión ejerce el agua dulce a 15 m de profundidad (sin contar la atmósfera)?", ["Aplica P = ρ × g × h con ρ = 1000 y g = 10.", "1000 × 10 × 15 = 150.000."], "150.000 Pa"),
        ("Presión total", "¿Cuál es la presión total a 30 m de profundidad en agua dulce?", ["Presión del agua: 1000 × 10 × 30 = 300.000 Pa.", "Suma la atmosférica: 100.000 + 300.000."], "400.000 Pa"),
    ],
    mistakes=[("Olvidar sumar la presión atmosférica en la presión total.", "Se calcula solo la del agua.", "Pregunta si el enunciado pide la presión del agua o la total."),
              ("Creer que la presión depende del ancho del recipiente.", "Se confunde la presión con el peso total del agua.", "Recuerda que depende de la profundidad y de la densidad.")],
    T=[
        ("abc", "¿Qué ocurre con la presión de un fluido en reposo al aumentar la profundidad?", "Aumenta", "Disminuye", "No cambia", "Hay más fluido encima y su peso aumenta la presión."),
        ("abc", "La unidad de presión en el Sistema Internacional es", "el pascal (Pa)", "el newton (N)", "el kilogramo (kg)", "El pascal es un newton por metro cuadrado."),
        ("ab", "A una profundidad dada, la presión del agua de un lago depende de la profundidad y de", "la densidad del agua", "el ancho del lago", "La fórmula incluye ρ y h, pero no el ancho del lago."),
        ("=", "{F} Calcula ρ × g × h para agua dulce a 5 m de profundidad.", "1000*10*5", "Se multiplican densidad, gravedad y profundidad.", " Pa"),
        ("=", "{F} ¿Qué presión total hay a 25 m de profundidad en agua dulce?", "100000+1000*10*25", "A la presión atmosférica se suma la del agua.", " Pa"),
        ("abc", "{F} ¿Por qué la presión total a 10 m en agua dulce es el doble que en la superficie?", "Porque el agua aporta otros 100.000 Pa, igual que la atmósfera", "Porque g se duplica", "Porque la densidad se duplica", "A 10 m el agua aporta 100.000 Pa, que se suman a los 100.000 Pa de la atmósfera."),
        ("=", "{F} ¿Qué presión total hay a 100 m de profundidad en el mar (ρ = 1030 kg/m³)?", "100000+1030*10*100", "Se suma la presión del agua de mar a la atmosférica.", " Pa"),
        ("=", "Una ventana de observación de un acuario ficticio mide 2 m² y soporta una presión de agua de 30.000 Pa. ¿Qué fuerza ejerce el agua sobre ella?", "30000*2", "La fuerza es la presión por el área.", " N"),
        ("=", "Un lago ficticio tiene 20 m de profundidad. ¿Qué presión ejerce el agua en el fondo, sin contar la atmósfera?", "1000*10*20", "Se aplica P = ρ × g × h con h = 20 m.", " Pa"),
        ("abc", "Dos recipientes de formas distintas contienen agua dulce hasta 3 m de altura. ¿Cómo se comparan las presiones en el fondo?", "Son iguales, porque dependen de la altura y no de la forma", "Es mayor en el más ancho", "Es mayor en el más angosto", "La presión sólo depende de la densidad, de g y de la altura de agua."),
        ("abc", "¿Por qué los instrumentos del fondo del mar deben tener paredes muy resistentes?", "Porque la presión aumenta con la profundidad y la fuerza sobre sus paredes es muy grande", "Porque el agua del fondo es más fría", "Porque la gravedad cambia con la profundidad", "La fuerza es presión por área, y a gran profundidad la presión es enorme."),
        ("abc", "Un estudiante dice: «a 20 m de profundidad en el mar la presión es 20 veces la de la superficie». ¿Qué falla?", "Que el agua se suma a la atmosférica: a 20 m la presión total es solo unas 3 veces la de la superficie", "Nada, es exacto", "Que en el mar no hay presión", "A 20 m el agua aporta unos 206.000 Pa que se suman a los 100.000 Pa de la atmósfera."),
        ("=", "{F} ¿A qué profundidad en agua dulce la presión del agua (sin atmósfera) es 300.000 Pa? (h = P ÷ (ρ × g))", "300000//(1000*10)", "Se despeja la profundidad dividiendo la presión por ρ × g.", " m"),
    ],
    ctx=("abc", "Una investigadora ficticia delimita su pregunta sobre un lago: «¿cómo cambia la presión con la profundidad?». ¿Qué debe medir, además de la profundidad?", "La densidad del agua y la presión a cada profundidad", "El color del agua", "La edad del lago", "La presión depende de la densidad y se contrasta con mediciones a cada profundidad."),
    sc=[
        ("En Física de fluidos: ¿qué fórmula da la presión del agua a una profundidad h?", "P = ρ × g × h", "Relaciona la presión con la densidad, la gravedad y la profundidad."),
        ("¿Cuántos Pa aporta cada 10 m de agua dulce?", "100.000 Pa", "Se calcula 1000 × 10 × 10."),
        ("¿La presión del agua depende de la forma del recipiente?", "No", "Solo depende de la profundidad, la densidad y g."),
    ],
    op=("Elige un sitio. Sitio 1: un lago ficticio de 40 m de profundidad. Sitio 2: una bahía ficticia de 60 m de profundidad con agua de mar (ρ = 1030 kg/m³). Calcula la presión del agua y la presión total en el fondo, escribe el supuesto principal del cálculo y explica en una frase qué pasaría con la fuerza sobre una ventana de 1 m² en el fondo.",
        "Sitio 1: presión del agua = 1000 × 10 × 40 = 400.000 Pa; total = 500.000 Pa. Supuesto: agua en reposo y densidad constante. Sobre una ventana de 1 m² la fuerza total sería 500.000 N, por lo que debe ser muy resistente.",
        ["calcula presión del agua y total con unidades", "nombra un supuesto del modelo", "relaciona la presión con la fuerza sobre una superficie"],
        ["hoja con los cálculos, el supuesto y la frase final"],
        ["olvidar sumar la atmósfera", "usar el ancho del lago", "olvidar las unidades"],
        "Pregunta: «¿qué presión pide el enunciado: la del agua o la total?»."),
    reinforce="Con la ficha, calcula la presión total en agua dulce a 0 m, 10 m, 20 m y 30 m y dibuja un gráfico.",
    extend="Explica por qué en el mar la presión crece algo más rápido con la profundidad que en un lago.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (de ejemplo; g ≈ 10 m/s²). Densidades en kg/m³: agua dulce 1000; agua de mar 1030; hielo 920; madera ficticia 600. "
     "Empuje sobre un cuerpo sumergido: E = ρ del fluido × g × volumen sumergido. Un cuerpo flota si su densidad es menor que la del fluido; el porcentaje de su volumen que queda sumergido es (ρ del cuerpo ÷ ρ del fluido) × 100. "
     "Lago ficticio con dos capas: superficial, 1000 kg/m³; profunda, 1004 kg/m³.")
build(
    O5, 2, F,
    use="Aprenderé a usar la densidad y el empuje para explicar por qué algo flota o se hunde y por qué los océanos y los lagos se ordenan en capas.",
    prior=["Sé que la presión del agua aumenta con la profundidad.", "Sé calcular volúmenes y porcentajes.", "Sé qué es la densidad."],
    explain=[
        "La densidad es la masa por unidad de volumen: ρ = m ÷ V. Un cuerpo sumergido recibe un empuje hacia arriba igual al peso del fluido que desplaza (principio de Arquímedes): E = ρ del fluido × g × V sumergido. Si el empuje supera al peso, el cuerpo sube; si es menor, se hunde. Un cuerpo flota cuando su densidad es menor que la del fluido, y la parte sumergida es la razón entre ambas densidades.",
        "El hielo flota en agua dulce porque su densidad (920 kg/m³) es menor que la del agua (1000 kg/m³): queda sumergido un 92 % de su volumen. Un barco de acero flota aunque el acero sea más denso que el agua, porque su forma encierra mucho aire y su densidad media es menor que la del agua.",
        "En los océanos y lagos el agua más densa tiende a quedar abajo y la menos densa arriba (estratificación). La densidad del agua de mar aumenta cuando baja la temperatura y cuando aumenta la salinidad (cantidad de sales disueltas). Esa diferencia de densidad estabiliza las capas y dificulta la mezcla entre ellas. Al evaluar una fuente sobre el agua, se revisa si informa las variables de las que depende la densidad.",
    ],
    vocab=[("empuje", "fuerza hacia arriba que ejerce un fluido sobre un cuerpo sumergido"), ("principio de Arquímedes", "el empuje es igual al peso del fluido desplazado"), ("estratificación", "ordenamiento en capas según la densidad"), ("salinidad", "cantidad de sales disueltas en el agua"), ("volumen sumergido", "parte del volumen del cuerpo bajo la superficie del fluido"), ("densidad media", "masa total dividida por volumen total, incluyendo el aire encerrado")],
    worked=[
        ("Empuje", "Un bloque ficticio de 3 m³ queda totalmente sumergido en agua dulce. ¿Qué empuje recibe?", ["E = ρ × g × V = 1000 × 10 × 3.", "Calcula el producto."], "30.000 N"),
        ("Porcentaje sumergido", "Un cuerpo ficticio de 800 kg/m³ flota en agua dulce. ¿Qué porcentaje de su volumen queda sumergido?", ["Razón de densidades: 800 ÷ 1000 = 0,8.", "Pasa a porcentaje: 80 %."], "80 %"),
    ],
    mistakes=[("Creer que todo lo pesado se hunde.", "Se confunde peso con densidad.", "Compara densidades, no pesos."),
              ("Creer que un barco de acero flota porque el acero es menos denso que el agua.", "Se ignora el aire encerrado en el casco.", "Calcula la densidad media del barco completo.")],
    T=[
        ("abc", "Un objeto flota en un fluido si su densidad es", "menor que la del fluido", "mayor que la del fluido", "igual a su masa", "El empuje supera al peso cuando el cuerpo es menos denso que el fluido."),
        ("abc", "La densidad se calcula como", "masa ÷ volumen", "volumen ÷ masa", "masa × volumen", "Es la masa por unidad de volumen."),
        ("ab", "En un océano estratificado, la capa más densa se ubica", "abajo", "arriba", "El agua más densa se hunde y queda debajo de la menos densa."),
        ("=", "{F} Un bloque de 2 m³ queda totalmente sumergido en agua dulce. ¿Qué empuje recibe?", "1000*10*2", "El empuje es la densidad del fluido por g por el volumen.", " N"),
        ("abc", "{F} ¿Por qué el hielo flota en agua dulce?", "Porque su densidad (920) es menor que la del agua (1000)", "Porque está más frío que el agua", "Porque siempre pesa menos que el agua", "Un cuerpo menos denso que el fluido flota."),
        ("abc", "Una masa de agua de mar es más densa cuando tiene", "menor temperatura y mayor salinidad", "mayor temperatura y menor salinidad", "menor presión y menor salinidad", "El enfriamiento y las sales aumentan la densidad."),
        ("=", "{F} Un cuerpo ficticio de 600 kg/m³ flota en agua dulce. ¿Qué porcentaje de su volumen queda sumergido?", "600*100//1000", "Es la razón entre la densidad del cuerpo y la del fluido, por 100.", " %"),
        ("=", "{F} Un cuerpo ficticio flota en agua dulce y queda sumergido el 75 % de su volumen. ¿Cuál es su densidad?", "1000*75//100", "La razón de densidades es 0,75, así que la densidad del cuerpo es el 75 % de la del agua.", " kg/m³"),
        ("=", "Un objeto ficticio de 3.000 kg ocupa 2 m³. ¿Cuál es su densidad?", "3000//2", "La densidad es la masa dividida por el volumen.", " kg/m³"),
        ("abc", "Un objeto de 1.500 kg/m³ se coloca en agua dulce. ¿Qué ocurre?", "Se hunde, porque su densidad es mayor que 1.000 kg/m³", "Flota, porque pesa mucho", "Queda a media altura", "Una densidad mayor que la del fluido hace que se hunda."),
        ("abc", "{F} Si el viento mezcla la superficie del lago ficticio, ¿qué se opone a que el agua profunda suba?", "La diferencia de densidad, que mantiene el agua más densa abajo", "El color del agua", "La profundidad del lago por sí sola", "El agua profunda es más densa y tiende a permanecer abajo."),
        ("abc", "La tabla X de un grupo ficticio entrega la densidad del agua de mar sin indicar temperatura ni salinidad. La tabla Y indica ambas. ¿Cuál es mejor fuente para explicar la estratificación y por qué?", "La tabla Y, porque informa las variables de las que depende la densidad", "La tabla X, porque tiene menos datos", "Ninguna de las dos", "Sin temperatura ni salinidad no se puede explicar de qué depende la densidad."),
        ("abc", "Un estudiante dice: «un barco de acero flota porque el acero es menos denso que el agua». ¿Qué falla?", "El acero es más denso; flota porque su forma encierra mucho aire y su densidad media es menor", "Nada, es exacto", "El acero es un gas", "La densidad que importa es la del casco completo con el aire."),
    ],
    ctx=("=", "Un bloque de hielo ficticio de 1.000 m³ flota en un lago de agua dulce. ¿Cuántos m³ de hielo quedan sumergidos? (el 92 % del volumen)", "1000*92//100", "Se calcula el 92 % del volumen total.", " m³"),
    sc=[
        ("En Física de fluidos: ¿cuándo flota un cuerpo?", "Cuando su densidad es menor que la del fluido", "El empuje supera a su peso y por eso el cuerpo sube."),
        ("¿Qué dos variables aumentan la densidad del agua de mar?", "Menor temperatura y mayor salinidad", "El frío y las sales hacen el agua más densa."),
        ("¿Dónde queda el agua más densa en un lago estratificado?", "Abajo", "La más densa se hunde bajo la menos densa."),
    ],
    op=("Elige un caso. Caso 1: un trozo de hielo ficticio de 500 m³ flotando en agua dulce. Caso 2: un bloque ficticio de madera de 600 kg/m³ y 10 m³ flotando en agua dulce. Calcula el volumen sumergido, el empuje cuando flota (igual al peso del fluido desplazado) y explica en dos líneas por qué flota.",
        "Caso 1: el 92 % de 500 m³ es 460 m³ sumergidos. El empuje es 1000 × 10 × 460 = 4.600.000 N. Flota porque su densidad (920) es menor que la del agua (1000).",
        ["calcula el volumen sumergido con la razón de densidades", "calcula el empuje con unidades", "explica por qué flota"],
        ["hoja con el cálculo y la explicación"],
        ["usar el volumen total como sumergido", "confundir peso con densidad", "olvidar las unidades"],
        "Pregunta: «¿cuál es mayor, la densidad del cuerpo o la del fluido?»."),
    reinforce="Con la ficha, calcula qué porcentaje de un bloque de madera de 600 kg/m³ queda sumergido en agua dulce.",
    extend="Explica por qué, al enfriarse y volverse más densa, el agua superficial de un lago puede hundirse.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (de ejemplo, valores redondeados). Calor específico en J/(kg·°C): agua 4200; arena, de ejemplo, 800. Energía para cambiar la temperatura: Q = m × c × ΔT, con Q en joules (J), m en kg y ΔT en °C. "
     "Transferencias de calor: conducción (contacto), convección (movimiento de fluido) y radiación (ondas electromagnéticas).")
build(
    O5, 3, F,
    use="Aprenderé a usar la termodinámica para explicar cómo el océano y la atmósfera almacenan y mueven la energía, y a calcular la energía que intercambian.",
    prior=["Sé la diferencia entre calor y temperatura.", "Sé que el aire caliente asciende.", "Sé multiplicar tres números."],
    explain=[
        "El calor es energía que se transfiere entre cuerpos por una diferencia de temperatura. Se transfiere por conducción (contacto directo), por convección (el fluido caliente sube y el frío baja) y por radiación (ondas electromagnéticas, como la luz del Sol). La energía necesaria para cambiar la temperatura de una masa m en ΔT es Q = m × c × ΔT, donde c es el calor específico: la energía necesaria para subir 1 °C a 1 kg de la sustancia.",
        "El agua tiene un calor específico muy alto: 4200 J/(kg·°C) frente a unos 800 de la arena. Por eso el agua se calienta y enfría lentamente y el océano almacena mucha energía con cambios de temperatura pequeños. Esto modera el clima de las zonas costeras: tienen menos diferencia entre día y noche y entre verano e invierno que las zonas del interior.",
        "La convección explica la brisa marina. De día la tierra se calienta más rápido que el mar; el aire sobre la tierra se calienta, se vuelve menos denso y sube, y el aire más frío del mar lo reemplaza: la brisa va del mar a la tierra. De noche la tierra se enfría más y la brisa va de la tierra al mar. En la atmósfera el aire que sube se expande y se enfría, lo que ayuda a explicar la formación de nubes.",
    ],
    vocab=[("calor", "energía transferida por diferencia de temperatura"), ("calor específico (c)", "energía para subir 1 °C a 1 kg de una sustancia"), ("conducción", "transferencia de calor por contacto"), ("convección", "transferencia por movimiento del fluido"), ("radiación", "transferencia por ondas electromagnéticas"), ("brisa marina", "viento que va del mar a la tierra durante el día")],
    worked=[
        ("Energía para calentar", "¿Cuánta energía hace falta para calentar 3 kg de agua en 4 °C?", ["Q = m × c × ΔT = 3 × 4200 × 4.", "Calcula el producto."], "50.400 J"),
        ("Brisa de día", "En una costa ficticia, a mediodía la arena está más caliente que el mar. ¿Hacia dónde va la brisa?", ["El aire sobre la arena se calienta, se hace menos denso y sube.", "El aire más frío del mar ocupa su lugar."], "Del mar hacia la tierra"),
    ],
    mistakes=[("Confundir calor con temperatura.", "Se piensa que ambos miden lo mismo.", "Recuerda: la temperatura es un nivel y el calor es energía transferida."),
              ("Creer que masas iguales suben igual la temperatura con la misma energía.", "Se olvida que el calor específico es distinto en cada material.", "Usa Q = m × c × ΔT con el c correspondiente.")],
    T=[
        ("abc", "El calor es", "energía que se transfiere por una diferencia de temperatura", "la temperatura de un cuerpo", "una sustancia que fluye", "El calor es energía en tránsito, no un nivel de temperatura."),
        ("abc", "El aire caliente asciende porque", "es menos denso que el aire frío que lo rodea", "es más pesado que el aire frío", "tiene más masa que el aire frío", "Un fluido menos denso flota sobre uno más denso."),
        ("ab", "Un material con calor específico alto, al recibir la misma energía, sube su temperatura", "menos", "más", "Necesita más energía por cada °C."),
        ("=", "{F} ¿Cuánta energía hace falta para calentar 2 kg de agua en 5 °C?", "2*4200*5", "Se multiplica masa, calor específico y variación de temperatura.", " J"),
        ("abc", "{F} Con la misma energía y la misma masa, ¿qué se calienta más, el agua o la arena?", "La arena", "El agua", "Se calientan igual", "La arena tiene un calor específico menor y sube más su temperatura."),
        ("abc", "¿Por qué el océano modera las temperaturas de las zonas costeras?", "Porque el agua tiene un calor específico alto y almacena mucha energía con poco cambio de temperatura", "Porque el agua es azul", "Porque el océano no recibe energía", "Por su capacidad de almacenar energía, el mar cambia lentamente de temperatura."),
        ("=", "{F} ¿Cuánta energía hace falta para calentar 3 kg de arena en 10 °C?", "3*800*10", "Se aplica Q = m × c × ΔT con el calor específico de la arena.", " J"),
        ("=", "Una masa de 5 kg de agua se enfría de 20 °C a 16 °C. ¿Cuánta energía libera?", "5*4200*(20-16)", "La variación de temperatura es 4 °C y se aplica la fórmula.", " J"),
        ("=", "{F} Si 4 kg de arena reciben 32.000 J, ¿cuántos °C sube su temperatura? (ΔT = Q ÷ (m × c))", "32000//(4*800)", "Se despeja la variación de temperatura de la fórmula.", " °C"),
        ("abc", "En una playa, de día la arena está más caliente que el mar. ¿Qué brisa se produce?", "Del mar hacia la tierra, porque el aire caliente sobre la tierra sube y el aire más frío del mar lo reemplaza", "De la tierra hacia el mar", "No se produce ninguna brisa", "La convección mueve aire frío hacia el lugar donde el aire caliente sube."),
        ("abc", "De noche, la arena se enfría más rápido que el mar. ¿Qué brisa se produce?", "De la tierra hacia el mar", "Del mar hacia la tierra", "No se produce ninguna brisa", "Ahora el aire más caliente está sobre el mar y sube, y el de la tierra lo reemplaza."),
        ("abc", "Un estudiante afirma: «con la misma energía, 1 kg de agua y 1 kg de arena suben igual la temperatura porque tienen la misma masa». ¿Qué falla?", "No considera el calor específico: el agua necesita mucha más energía por cada °C", "Nada, las masas iguales suben igual", "El agua no tiene calor específico", "La energía necesaria depende de la masa y del material."),
        ("=", "{F} ¿Cuántos J más necesita 1 kg de agua que 1 kg de arena para subir 1 °C?", "4200-800", "Se resta el calor específico de la arena del calor específico del agua.", " J"),
    ],
    ctx=("abc", "Una ciudad costera ficticia tiene veranos suaves y otra ciudad del interior, a la misma latitud, veranos extremos. ¿Qué propiedad física ayuda a explicarlo?", "El alto calor específico del agua, que modera la temperatura cerca del mar", "La forma de las nubes", "La edad de las ciudades", "El mar almacena mucha energía con poco cambio de temperatura y suaviza el clima cercano."),
    sc=[
        ("En Física: ¿qué mide el calor específico?", "La energía para subir 1 °C a 1 kg de una sustancia", "Es una propiedad de cada material."),
        ("¿Cuál es el sentido de la brisa marina de día?", "Del mar hacia la tierra", "El aire sobre la tierra caliente sube y el del mar lo reemplaza."),
        ("¿Qué energía requieren 2 kg de agua para subir 1 °C?", "8.400 J", "Se calcula 2 × 4200 × 1."),
    ],
    op=("Elige un caso. Caso 1: una bahía ficticia con 1.000 kg de agua que se calientan 2 °C en una jornada. Caso 2: una playa ficticia con 500 kg de arena que se calientan 10 °C. Calcula la energía necesaria con los calores específicos de la ficha y escribe dos líneas que expliquen cómo esto influye en la brisa de la costa.",
        "Caso 2: Q = 500 × 800 × 10 = 4.000.000 J. La arena se calienta rápido, calienta el aire encima y este sube; el aire frío del mar lo reemplaza, por lo que de día hay brisa del mar a la tierra.",
        ["usa Q = m × c × ΔT con unidades", "compara el comportamiento del agua y la arena", "explica el sentido de la brisa"],
        ["hoja con el cálculo y la explicación"],
        ["mezclar masas o calores específicos", "invertir el sentido de la brisa", "olvidar las unidades"],
        "Pregunta: «¿quién se calienta más rápido y qué le pasa al aire encima?»."),
    reinforce="Calcula la energía que necesitan 10 kg de agua para subir 2 °C.",
    extend="Explica por qué la temperatura de los desiertos cambia mucho entre el día y la noche, en comparación con la costa.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (de ejemplo, valores redondeados). Rapideces de ondas sísmicas en la corteza: onda P, 6 km/s; onda S, 3 km/s. Una estación registra la llegada de la onda P y, Δt segundos después, la de la onda S. "
     "Con estos valores, la distancia al epicentro es d = Δt × 6 km (se deduce de d = 6 × t y d = 3 × (t + Δt)). Capas de la Tierra: corteza, manto, núcleo externo (líquido) y núcleo interno (sólido).")
build(
    O5, 4, F,
    use="Aprenderé a analizar evidencia indirecta del interior de la Tierra (ondas sísmicas y campo magnético) y a calcular la distancia a un terremoto.",
    prior=["Sé qué es una onda y su rapidez.", "Sé que la Tierra tiene capas.", "Sé calcular distancia como rapidez por tiempo."],
    explain=[
        "El interior de la Tierra no se puede observar directamente, por eso se estudia con evidencia indirecta. Cuando ocurre un terremoto se generan ondas sísmicas. Las ondas P (de compresión) viajan por sólidos y líquidos; las ondas S (de corte) viajan solo por sólidos y son más lentas. En una estación, la onda P llega primero y la S después; la diferencia de tiempo Δt permite calcular la distancia al epicentro.",
        "Con tres o más estaciones se ubica el epicentro, porque cada distancia define una circunferencia y las circunferencias se cruzan en un punto. Las ondas S no atraviesan el núcleo externo, lo que dejó una «sombra» de ondas S al otro lado del planeta y mostró que esa capa es líquida. El núcleo interno, en cambio, es sólido.",
        "El electromagnetismo aporta otra evidencia: la Tierra tiene un campo magnético que orienta la brújula. Se atribuye al movimiento del hierro líquido eléctricamente conductor del núcleo externo (geodinamo). Ese campo desvía gran parte de las partículas cargadas del viento solar y protege la atmósfera; algunas partículas guiadas hacia los polos producen auroras. Estas conclusiones son indirectas: no hay fotos del núcleo.",
    ],
    vocab=[("onda P", "onda sísmica de compresión, la más rápida, viaja por sólidos y líquidos"), ("onda S", "onda sísmica de corte, más lenta, solo viaja por sólidos"), ("epicentro", "punto de la superficie sobre el origen de un terremoto"), ("sismógrafo", "instrumento que registra ondas sísmicas"), ("campo magnético", "región donde actúan fuerzas magnéticas"), ("geodinamo", "proceso que genera el campo magnético terrestre")],
    worked=[
        ("Distancia al epicentro", "En una estación, la onda S llega 15 s después de la P. Con los valores de la ficha, ¿a qué distancia está el epicentro?", ["Aplica d = Δt × 6.", "15 × 6 = 90."], "90 km"),
        ("Inferir una capa", "Las ondas S no atraviesan cierta capa interior. ¿Qué se infiere?", ["Las ondas S solo viajan por sólidos.", "Si no la atraviesan, la capa no es sólida."], "La capa es líquida"),
    ],
    mistakes=[("Creer que el interior de la Tierra se conoce por fotografías o perforaciones hasta el núcleo.", "Se confunde evidencia directa con indirecta.", "Recuerda que la mayor parte se infiere con ondas sísmicas y el campo magnético."),
              ("Creer que la onda S llega antes que la P.", "Se confunde cuál es más rápida.", "La P es más rápida y llega primero.")],
    T=[
        ("abc", "¿Qué onda sísmica no atraviesa los líquidos?", "La onda S", "La onda P", "Ambas la atraviesan", "Las ondas S son de corte y los líquidos no las transmiten."),
        ("abc", "¿Qué indica que las ondas S no atraviesen el núcleo externo?", "Que el núcleo externo está en estado líquido", "Que es muy delgado", "Que está muy frío", "Como las S solo viajan por sólidos, esa capa no es sólida."),
        ("ab", "Se atribuye el campo magnético de la Tierra al movimiento de", "hierro líquido en el núcleo externo", "rocas sólidas de la corteza", "El hierro líquido conductor en movimiento genera el campo."),
        ("=", "{F} La onda S llega 20 s después de la P. ¿A qué distancia está el epicentro?", "20*6", "Con los valores de la ficha, d = Δt × 6.", " km"),
        ("abc", "{F} ¿Por qué la onda S llega después de la P?", "Porque su rapidez es menor", "Porque recorre un camino más largo", "Porque se produce después del terremoto", "Ambas salen del mismo lugar, pero la S va a 3 km/s y la P a 6 km/s."),
        ("abc", "¿Cómo protege el campo magnético terrestre a los seres vivos?", "Desvía gran parte de las partículas cargadas que vienen del Sol", "Absorbe todo el calor solar", "Produce el oxígeno del aire", "Las partículas cargadas del viento solar son desviadas por el campo."),
        ("=", "{F} La onda S llega 35 s después de la P. ¿A qué distancia está el epicentro?", "35*6", "Se multiplica la diferencia de tiempo por 6 km/s.", " km"),
        ("=", "{F} Una estación está a 300 km del epicentro. ¿Cuántos segundos después de la P llega la S?", "300//6", "Se despeja Δt dividiendo la distancia por 6.", " s"),
        ("=", "Una onda P viaja a 6 km/s durante 30 s. ¿Qué distancia recorre?", "6*30", "La distancia es la rapidez por el tiempo.", " km"),
        ("abc", "En el lado opuesto de la Tierra a un terremoto no llegan ondas S. ¿Qué conclusión sostiene?", "Que hay una capa líquida en el interior que las ondas S no atraviesan", "Que los sismógrafos fallan", "Que no hubo terremoto", "La ausencia de ondas S del otro lado indica un interior líquido."),
        ("abc", "Un sismógrafo registra P y S con 40 s de diferencia y otro con 10 s. ¿Cuál está más lejos del epicentro?", "El de 40 s", "El de 10 s", "Ambos igual", "Una mayor diferencia de tiempo corresponde a una mayor distancia."),
        ("abc", "Dos estaciones miden diferencias S−P de 20 s y 30 s. ¿Qué permite estimar el epicentro con más confianza?", "Usar tres o más estaciones, porque con tres distancias se ubica un punto", "Usar solo la estación más cercana", "Promediar las dos diferencias", "Cada distancia define una circunferencia y tres se cruzan en un punto."),
        ("abc", "Un periodista escribe: «ya se tomaron fotos del núcleo de la Tierra». ¿Qué corrige una lectura crítica?", "Que el interior se conoce de forma indirecta, con ondas sísmicas y campo magnético, no con fotos", "Que sí se tomaron fotos", "Que el núcleo no existe", "El núcleo está a miles de kilómetros bajo la superficie y no se puede fotografiar."),
    ],
    ctx=("=", "Una estación ficticia registra una diferencia S−P de 25 s. ¿A qué distancia está el epicentro, en km?", "25*6", "Se usa d = Δt × 6 con los valores de la ficha.", " km"),
    sc=[
        ("En Física de la Tierra: ¿qué onda sísmica llega primero a una estación?", "La onda P", "Es más rápida que la onda S."),
        ("¿Qué evidencia indica que el núcleo externo es líquido?", "Que las ondas S no lo atraviesan", "Las ondas S no viajan por líquidos."),
        ("¿Cuántos km está el epicentro si S−P es 10 s (valores de la ficha)?", "60 km", "Se calcula la distancia como 10 × 6 km."),
    ],
    op=("Elige un caso ficticio. Caso 1: tres estaciones registran diferencias S−P de 10 s, 20 s y 30 s. Caso 2: dos estaciones registran 15 s y 45 s. Calcula las distancias al epicentro con los valores de la ficha, explica por qué se necesitan tres estaciones para ubicar un punto y escribe dos evidencias indirectas del interior de la Tierra.",
        "Caso 1: las distancias son 60, 120 y 180 km. Con tres circunferencias de esos radios alrededor de las estaciones se ubica el epicentro, porque se cruzan en un punto. Evidencias: la sombra de ondas S y el campo magnético.",
        ["calcula las distancias con unidades", "explica el uso de tres estaciones", "nombra dos evidencias indirectas"],
        ["hoja con las distancias, un esquema de tres circunferencias y dos evidencias"],
        ["usar la onda S como la primera", "no usar tres estaciones", "afirmar que se vio el núcleo"],
        "Pregunta: «¿qué onda llega primero y por qué?»."),
    reinforce="Con la ficha, calcula la distancia al epicentro para diferencias S−P de 5 s, 15 s y 40 s.",
    extend="Explica por qué la evidencia indirecta puede ser tan convincente como la observación directa si se usan métodos independientes.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (de ejemplo; g ≈ 10 m/s², ρ del agua 1000 kg/m³). Caudal Q = A × v (m³/s), con A el área de la sección en m² y v la rapidez del agua en m/s. "
     "Potencia hidráulica ideal P = ρ × g × Q × H (W), con H la altura de caída en m. Opción 1: Q = 2 m³/s y H = 5 m. Opción 2: Q = 1 m³/s y H = 12 m. "
     "Eficiencia de ejemplo: 50 %. Porosidad: porcentaje del volumen de un suelo que son huecos.")
build(
    O5, 5, F,
    use="Aprenderé a comparar soluciones que usan el agua de ríos y suelos: caudal, potencia hidráulica e infiltración, con criterios técnicos y ambientales.",
    prior=["Sé calcular áreas y volúmenes.", "Sé qué es la potencia.", "Sé usar porcentajes."],
    explain=[
        "El caudal es el volumen de agua que pasa por una sección cada segundo: Q = A × v. Si un canal se angosta y el caudal se mantiene, la rapidez aumenta (ecuación de continuidad). Un río con sección de 5 m² y rapidez de 2 m/s tiene un caudal de 10 m³/s. El caudal se mide en m³/s.",
        "El agua que cae desde una altura H puede mover una turbina. La potencia hidráulica ideal es P = ρ × g × Q × H. Con Q = 2 m³/s y H = 5 m resulta 1000 × 10 × 2 × 5 = 100.000 W. La potencia útil es menor, porque la eficiencia (fracción de la potencia ideal que se aprovecha) no es 100 %. Dos diseños pueden dar potencias parecidas con combinaciones distintas de caudal y altura.",
        "En los suelos el agua se infiltra por los huecos. La porosidad indica qué fracción del volumen son huecos. Los suelos arenosos dejan pasar el agua rápido y retienen poca; los arcillosos la dejan pasar lento y retienen más. Al comparar soluciones se usan varios criterios: potencia útil, costo, efecto sobre el río y las personas aguas abajo (caudal ecológico) y adecuación al suelo. Un buen análisis explicita qué criterio pesa más.",
    ],
    vocab=[("caudal", "volumen de agua por segundo, Q = A × v"), ("ecuación de continuidad", "si la sección se reduce, la rapidez aumenta con caudal constante"), ("potencia hidráulica", "potencia de una caída de agua, P = ρ × g × Q × H"), ("eficiencia", "fracción de la potencia ideal que se aprovecha"), ("porosidad", "porcentaje del volumen de suelo que son huecos"), ("caudal ecológico", "caudal mínimo que necesita un río para mantener su ecosistema")],
    worked=[
        ("Caudal", "Un canal ficticio tiene 3 m² de sección y el agua avanza a 4 m/s. ¿Cuál es el caudal?", ["Q = A × v.", "3 × 4 = 12."], "12 m³/s"),
        ("Potencia ideal", "Una caída ficticia tiene Q = 3 m³/s y H = 4 m. ¿Cuál es la potencia ideal?", ["P = 1000 × 10 × 3 × 4.", "Calcula el producto."], "120.000 W"),
    ],
    mistakes=[("Elegir la opción con más potencia sin considerar el efecto sobre el río.", "Se usa un solo criterio.", "Agrega criterios ambientales y sociales."),
              ("Usar la potencia ideal como si fuera la útil.", "Se ignora la eficiencia.", "Multiplica la potencia ideal por la eficiencia.")],
    T=[
        ("abc", "El caudal de un río es", "el volumen de agua que pasa por una sección cada segundo", "la altura del río", "la rapidez del viento", "Se mide en m³/s y mide cuánta agua pasa por segundo."),
        ("abc", "Según la continuidad, si un canal se angosta y el caudal se mantiene, la rapidez del agua", "aumenta", "disminuye", "no cambia", "Con Q = A × v constante, si A disminuye, v aumenta."),
        ("ab", "Comparado con un suelo arcilloso, un suelo arenoso suele", "dejar infiltrar el agua más rápido", "retener el agua por más tiempo", "Los huecos grandes de la arena dejan pasar el agua rápido."),
        ("=", "{F} Un canal de 2 m de ancho y 1 m de profundidad lleva agua a 3 m/s. ¿Cuál es su caudal?", "2*1*3", "La sección es ancho por profundidad y el caudal es sección por rapidez.", " m³/s"),
        ("=", "{F} Con el caudal de la opción 1, ¿cuál sería la potencia ideal si la altura de caída fuera 8 m?", "1000*10*2*8", "Se aplica P = ρ × g × Q × H con Q = 2 m³/s y H = 8 m.", " W"),
        ("abc", "{F} ¿Qué representa H en la fórmula de potencia hidráulica?", "La altura de caída del agua", "La hora del día", "La humedad del suelo", "La energía del agua depende de la altura desde la que cae."),
        ("=", "{F} Un río tiene una sección de 7 m² y una rapidez de 2 m/s. ¿Cuál es su caudal?", "7*2", "El caudal es sección por rapidez.", " m³/s"),
        ("=", "{F} ¿Cuál es la potencia ideal de la opción 2?", "1000*10*1*12", "Se aplica la fórmula con Q = 1 m³/s y H = 12 m.", " W"),
        ("=", "{F} Con la eficiencia de ejemplo, ¿cuánta potencia útil entrega la opción 1, que tiene 100.000 W de potencia ideal?", "100000*50//100", "Se toma el 50 % de la potencia ideal.", " W"),
        ("abc", "{F} Con la eficiencia de 50 % en ambas, ¿qué opción entrega más potencia útil y cuánto más?", "La opción 2, 10.000 W más", "La opción 1, 10.000 W más", "Entregan lo mismo", "La opción 1 da 50.000 W y la opción 2 da 60.000 W."),
        ("abc", "Un agricultor debe regar un terreno de suelo arenoso. ¿Qué conviene?", "Riegos más frecuentes y de menor cantidad, porque el agua se infiltra rápido y se pierde hacia abajo", "Un riego muy largo una vez por semana", "No regar", "El suelo arenoso retiene poca agua, así que se riega en dosis pequeñas y frecuentes."),
        ("abc", "{F} Una comunidad compara la opción 1 (caudal alto) y la opción 2 (caudal bajo, mucha altura). ¿Qué criterio, además de la potencia, es importante?", "El efecto sobre el caudal ecológico del río y quienes lo usan aguas abajo", "El color de la turbina", "El nombre del proyecto", "Desviar un caudal grande puede dejar sin agua al ecosistema."),
        ("=", "Un suelo ficticio tiene 40 % de porosidad. ¿Cuántos m³ de huecos hay en 50 m³ de ese suelo?", "50*40//100", "Se calcula el 40 % del volumen total.", " m³"),
    ],
    ctx=("abc", "Una comunidad ficticia compara las dos opciones de la ficha con eficiencia del 50 %. ¿Qué debe presentar para decidir con evidencia?", "Potencia útil de cada opción, costos y efectos sobre el río", "Solo la potencia ideal", "Solo el nombre de los proyectos", "Una decisión con evidencia compara varios criterios con datos."),
    sc=[
        ("En Física de fluidos: ¿cómo se calcula el caudal?", "Sección por rapidez: Q = A × v", "Mide el volumen que pasa por segundo."),
        ("¿La potencia útil es igual a la ideal?", "No", "La eficiencia es menor que 100 %."),
        ("¿Qué suelo retiene más agua, el arenoso o el arcilloso?", "El arcilloso", "Deja pasar el agua más lento."),
    ],
    op=("Elige un problema. Problema 1: un canal ficticio de 4 m² de sección con agua a 2 m/s y una caída de 6 m. Problema 2: un canal ficticio de 3 m² de sección con agua a 1 m/s y una caída de 20 m. Calcula el caudal y la potencia ideal, la potencia útil con eficiencia de 50 %, y escribe dos criterios (uno técnico y uno ambiental) para comparar con otra opción.",
        "Problema 1: Q = 4 × 2 = 8 m³/s; P ideal = 1000 × 10 × 8 × 6 = 480.000 W; potencia útil = 240.000 W. Criterios: potencia útil (técnico) y caudal ecológico del río (ambiental).",
        ["calcula caudal y potencias con unidades", "aplica la eficiencia", "propone un criterio técnico y uno ambiental"],
        ["hoja con los cálculos y los criterios"],
        ["usar la potencia ideal como útil", "olvidar el efecto ambiental", "olvidar unidades"],
        "Pregunta: «¿qué pasa con el río si se desvía todo el caudal?»."),
    reinforce="Con la ficha, calcula el caudal de un río de 6 m² de sección y 2 m/s.",
    extend="Explica cómo la porosidad y el tipo de suelo influyen en cuánta agua llega a los acuíferos.",
)

# ============================================================ OAC-05, clase 6
F = ("Ficha 6 (de ejemplo, datos inventados). Informe ficticio sobre un fiordo: profundidad medida 120 m ± 6 m; presión del agua en el fondo estimada con P = ρ × g × h, con ρ = 1000 kg/m³ y g = 10 m/s² para simplificar. "
     "Error relativo = (error ÷ valor medido) × 100. Preguntas posibles: ¿cómo aumenta la presión con la profundidad?, ¿por qué se estratifica el agua?, ¿cómo se mueve el calor entre capas?, ¿por qué una brújula apunta al norte?")
build(
    O5, 6, F,
    use="Aprenderé a comunicar los límites de un análisis físico de un sistema natural y a tomar una decisión que declare supuestos, incertidumbre y alcance.",
    prior=["Sé calcular presión con ρ × g × h.", "Sé qué es una incertidumbre ± .", "Sé que cada rama de la física tiene su campo."],
    explain=[
        "Un análisis físico de un sistema natural parte de una pregunta, un sistema y un modelo, usa datos con su incertidumbre y declara sus límites. Si la profundidad medida es 120 m ± 6 m, el valor probablemente está entre 114 y 126 m. El error relativo, (error ÷ valor) × 100, indica qué tan importante es el error: por ejemplo, una medición de 50 m ± 5 m tiene un error relativo de 5 ÷ 50 × 100 = 10 %. Con el rango de profundidad se calculan valores mínimo y máximo de la presión.",
        "Cada rama de la física responde preguntas distintas. La mecánica de fluidos explica cómo aumenta la presión con la profundidad y por qué algo flota. La termodinámica explica cómo se almacena y mueve el calor. El electromagnetismo explica la brújula y el campo magnético terrestre. Muchas preguntas reales combinan varias ramas, y por eso se debe declarar cuáles se usan.",
        "Todo modelo tiene límites. P = ρ × g × h supone agua en reposo, densidad constante y g constante; en la realidad hay corrientes, cambios de temperatura y salinidad. Comunicar con honestidad significa no dar un valor exacto cuando hay rango, decir qué se simplificó y decidir con un margen de seguridad. Una buena decisión reconoce que un modelo simple puede ser suficiente para una pregunta y no para otra.",
    ],
    vocab=[("incertidumbre", "margen en que puede estar un valor"), ("error relativo", "error dividido por el valor medido, en porcentaje"), ("supuesto", "condición que se acepta para simplificar un modelo"), ("rango de validez", "condiciones en que el modelo funciona bien"), ("margen de seguridad", "holgura que se agrega para cubrir lo desfavorable"), ("mecánica de fluidos", "rama de la física que estudia líquidos y gases")],
    worked=[
        ("Error relativo", "Una medición ficticia es 80 m ± 4 m. ¿Cuál es el error relativo?", ["Divide el error entre el valor: 4 ÷ 80 = 0,05.", "Pasa a porcentaje."], "5 %"),
        ("Elegir la rama", "¿Qué rama de la física responde mejor «¿por qué se hunde una piedra en el agua?»?", ["La pregunta trata de flotar o hundirse según la densidad.", "Eso corresponde a la mecánica de fluidos."], "La mecánica de fluidos"),
    ],
    mistakes=[("Entregar un valor exacto cuando hay incertidumbre.", "Se oculta el margen de error.", "Escribe el rango o el ± en el resultado."),
              ("Usar un modelo sin declarar sus supuestos.", "Se cree que el cálculo es la realidad.", "Anota qué se simplificó y cuándo deja de valer.")],
    T=[
        ("abc", "¿Qué significa 120 m ± 6 m?", "Que el valor probablemente está entre 114 y 126 m", "Que el valor es exactamente 120 m", "Que el valor está entre 100 y 140 m", "El ± indica el margen alrededor del valor central."),
        ("abc", "El error relativo se calcula como", "error ÷ valor medido × 100", "valor medido ÷ error", "error × valor medido", "Compara el tamaño del error con el valor medido."),
        ("ab", "Un informe honesto sobre un modelo físico de la naturaleza debe declarar", "sus supuestos y límites", "solo sus resultados", "Sin los supuestos no se puede juzgar cuándo vale el resultado."),
        ("=", "{F} ¿Cuál es el error relativo de la profundidad medida, en %?", "6*100//120", "Se divide el error por el valor y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué supuestos hace el modelo P = ρ × g × h para el agua del fiordo?", "Que el agua está en reposo y su densidad es constante", "Que el agua se mueve rápido", "Que no hay gravedad", "Esos supuestos simplifican el cálculo y deben declararse."),
        ("abc", "¿Qué rama de la física responde mejor a «¿por qué una brújula apunta al norte?»?", "El electromagnetismo", "La termodinámica", "La mecánica de fluidos", "La brújula responde al campo magnético terrestre."),
        ("=", "{F} Con el valor mínimo de profundidad, ¿cuál es la presión del agua en el fondo?", "1000*10*114", "Se aplica P = ρ × g × h con h = 114 m.", " Pa"),
        ("=", "{F} Con el valor máximo de profundidad, ¿cuál es la presión del agua en el fondo?", "1000*10*126", "Se aplica P = ρ × g × h con h = 126 m.", " Pa"),
        ("=", "{F} ¿Cuántos Pa de diferencia hay entre la presión máxima y la mínima?", "1260000-1140000", "Se resta la presión mínima de la máxima.", " Pa"),
        ("abc", "{F} Un titular dice: «la presión en el fondo del fiordo es exactamente 1.200.000 Pa». ¿Qué falla?", "Da un valor exacto sin rango ni supuestos, aunque la profundidad tiene ±6 m", "Nada, es correcto", "Que usa pascales", "La incertidumbre de la profundidad se traspasa a la presión."),
        ("abc", "Una persona dice: «como el modelo es una simplificación, no vale nada». ¿Qué respuesta es adecuada?", "Un modelo es útil dentro de su rango de validez; hay que declarar sus límites y decidir si basta para la pregunta", "Tiene razón: los modelos nunca sirven", "Los modelos son exactos y no tienen límites", "Un modelo simple puede ser suficiente para ciertas preguntas."),
        ("abc", "{F} Una comunidad quiere instalar un sensor a 130 m de profundidad en el fiordo. ¿Qué decisión apoya la evidencia?", "No instalar a 130 m, porque el fondo máximo probable es 126 m, y revisar la medición", "Instalar a 130 m de todas formas", "Instalar a 120 m exactos", "El sensor quedaría bajo el fondo según el rango de la medición."),
        ("=", "Si una profundidad fuera 150 m ± 6 m, ¿cuál sería su error relativo?", "6*100//150", "Se divide el error por el valor y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Al cerrar su informe, una estudiante debe ordenar los pasos. ¿Qué orden es el adecuado?", "Pregunta y sistema, modelo y datos con incertidumbre, límites, decisión", "Decisión, datos, pregunta", "Datos, decisión, sin límites", "Primero se delimita, luego se calcula con incertidumbre, se declaran límites y recién se decide."),
    sc=[
        ("En Física de sistemas naturales: ¿cómo se calcula el error relativo?", "Error dividido por el valor medido, por 100", "Indica qué tan grande es el error respecto del valor."),
        ("¿Qué rama explica cómo se almacena el calor en el océano?", "La termodinámica", "Estudia el intercambio y almacenamiento de energía térmica."),
        ("¿Se puede dar un valor exacto si la medición tiene ±?", "No", "Hay que informar el rango junto con el valor."),
    ],
    op=("Elige un caso. Caso 1: un lago ficticio de 100 m ± 5 m de profundidad. Caso 2: una bahía ficticia de 200 m ± 10 m. Calcula el error relativo y la presión mínima y máxima del agua en el fondo (ρ = 1000, g = 10) y escribe tres frases: una con el resultado y su rango, una con los supuestos del modelo y una con la decisión que tomarías (por ejemplo, para instalar un instrumento) con su margen de seguridad.",
        "Caso 1: error relativo = 5 ÷ 100 × 100 = 5 %. Presión entre 1000 × 10 × 95 = 950.000 Pa y 1000 × 10 × 105 = 1.050.000 Pa. Supuestos: agua en reposo y densidad constante. Decisión: elegir un instrumento resistente a más de 1.050.000 Pa.",
        ["calcula error relativo y rango de presión", "declara supuestos", "toma una decisión con margen de seguridad"],
        ["hoja con cálculos y las tres frases"],
        ["dar un valor exacto", "no declarar supuestos", "decidir sin margen"],
        "Pregunta: «¿qué cambiaría tu decisión si la profundidad real fuera la máxima?»."),
    reinforce="Con la ficha, calcula el error relativo si la medición fuera 60 m ± 3 m.",
    extend="Explica cuándo un modelo simple de un sistema natural puede ser suficiente y cuándo hay que usar uno más completo.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (de ejemplo, datos inventados). Escuela rural ficticia «Los Aromos»: una sala de 20 m² de piso, con 4 ventanas de 2 m² cada una y un techo de 20 m². "
     "Gasto de calefacción de ejemplo: 300 kWh al mes. Medida de ejemplo (aislar el techo): reduce el gasto en un 20 %. Cada kWh de leña emite, en este ejemplo, 400 g de CO2. "
     "Actores: estudiantes, docentes, familias, municipio y vecinos del bosque cercano.")
build(
    O6, 1, F,
    use="Aprenderé a delimitar un problema real que necesita varias ciencias y a incluir desde el inicio las dimensiones ética, social y ambiental.",
    prior=["Sé que la física estudia la energía y el calor.", "Sé qué es una fuente de energía.", "Sé qué significa que algo afecte a otras personas."],
    explain=[
        "Los problemas actuales, como calefaccionar una escuela rural, no se resuelven con una sola ciencia. La física aporta cómo se transfiere el calor y cuánta energía se necesita; la química, qué ocurre al quemar leña y qué materiales aíslan; la biología y la salud, cómo afecta el humo a las personas y al bosque; las ciencias sociales y la economía, quién puede pagar y cómo se decide. Integrar significa usar cada conocimiento para la parte del problema que le corresponde.",
        "Delimitar el problema con varias ciencias exige nombrar el sistema (la sala y su entorno), las variables (energía, emisiones, costos, salud) y los actores afectados. Una pregunta bien delimitada se puede responder con datos, por ejemplo: «¿cuántos kWh por mes se ahorrarían aislando el techo de una sala de 20 m²?». Una pregunta como «¿es buena la calefacción?» es una opinión y no sirve como punto de partida.",
        "La dimensión ética pregunta quién gana, quién asume los riesgos y quién decide. Algunos criterios son: justicia (que los costos y beneficios se repartan de forma equitativa), participación (que las personas afectadas sean escuchadas), precaución (actuar con prudencia ante riesgos graves aunque falte certeza total) y transparencia (explicar los datos y criterios). Las implicancias ambientales incluyen emisiones, uso de recursos y efectos sobre ecosistemas cercanos.",
    ],
    vocab=[("integración", "uso conjunto de varias ciencias para un mismo problema"), ("actor", "persona o grupo afectado por una decisión o que participa en ella"), ("justicia", "reparto equitativo de beneficios y costos"), ("participación", "derecho de las personas afectadas a ser escuchadas"), ("precaución", "actuar con prudencia ante un riesgo grave aunque falte certeza"), ("transparencia", "explicar datos y criterios usados")],
    worked=[
        ("Repartir preguntas", "Para el problema de una piscina ficticia: ¿qué ciencia responde mejor «¿cuánta energía se pierde por evaporación?»?", ["La pregunta trata de energía y calor.", "Eso corresponde a la física."], "La física"),
        ("Delimitar", "Convierte «¿Es buena una caldera nueva?» en una pregunta investigable para un gimnasio ficticio.", ["Nombra una variable con unidad: kWh por mes.", "Agrega el sistema y el cambio: el gimnasio, antes y después de cambiar la caldera."], "«¿Cuántos kWh por mes ahorra el gimnasio con la caldera nueva?»"),
    ],
    mistakes=[("Delimitar el problema usando solo la ciencia que se domina.", "Se ignoran otras dimensiones del problema.", "Pregunta qué otras ciencias y qué actores faltan."),
              ("Dejar la ética para el final, como adorno.", "Se la trata como opinión y no como criterio de análisis.", "Incluye quién gana, quién arriesga y quién decide desde el inicio.")],
    T=[
        ("abc", "{F} ¿Qué pregunta corresponde principalmente a la física?", "¿Cuánta energía se pierde por las paredes y ventanas de la sala?", "¿Qué enfermedades respiratorias produce el humo?", "¿Qué familias pueden pagar el cambio?", "Calcular pérdidas de energía es un problema de transferencia de calor."),
        ("abc", "¿Qué pregunta corresponde principalmente a la biología y la salud?", "¿Cómo afecta el humo de la combustión a la salud respiratoria de los estudiantes?", "¿Cuántos kWh se pierden por el techo?", "¿Cuánto cuesta la aislación?", "Los efectos del humo en el cuerpo pertenecen a la biología y a la salud."),
        ("ab", "Un problema complejo como reducir el gasto de calefacción de una escuela se aborda mejor", "integrando varias disciplinas y consultando a las personas afectadas", "usando solo la disciplina que domina el equipo", "Cada disciplina aporta una parte distinta del problema."),
        ("abc", "¿Quiénes son actores afectados por una decisión sobre la calefacción de la escuela?", "Estudiantes, docentes, familias, municipio y vecinos cercanos", "Solo los docentes", "Solo quienes pagan la cuenta", "Una decisión pública afecta a todos los actores que usan o rodean la escuela."),
        ("abc", "{F} ¿Cuál es una pregunta bien delimitada?", "¿Cuántos kWh por mes se podrían ahorrar en la sala de 20 m² aislando el techo?", "¿Es buena la calefacción?", "¿Qué pasará con el mundo?", "Tiene variable con unidad, sistema y medida; las otras son opiniones o demasiado amplias."),
        ("abc", "En una evaluación ética, una pregunta clave es", "¿quién gana, quién asume los riesgos y quién decide?", "¿cuál tecnología es más moderna?", "¿cuál es más barata para quien decide?", "Esas preguntas revelan el reparto de beneficios, riesgos y poder."),
        ("=", "{F} ¿Cuántos m² de ventanas tiene la sala?", "4*2", "Se multiplica el número de ventanas por su área.", " m²"),
        ("=", "{F} ¿Cuántos kWh por mes se ahorrarían si el gasto de 300 kWh baja 20 %?", "300*20//100", "Se calcula el 20 % del gasto mensual.", " kWh"),
        ("=", "{F} ¿Cuántos g de CO2 por mes se evitan al ahorrar 60 kWh?", "60*400", "Se multiplica la energía ahorrada por la emisión de cada kWh.", " g"),
        ("abc", "Una propuesta mide solo el ahorro de energía y no pregunta a las familias. ¿Qué dimensión falta?", "La social y ética: quiénes son afectados y cómo participan", "La matemática", "Ninguna, porque el ahorro lo dice todo", "Una decisión pública también debe considerar la participación y el reparto de costos."),
        ("abc", "El municipio propone talar el bosque cercano para tener leña barata. ¿Qué disciplina aporta una advertencia clave?", "La ecología, sobre el efecto en el ecosistema y el suelo", "La música", "Ninguna, porque es solo una decisión económica", "Talar el bosque afecta la biodiversidad, el suelo y el agua."),
        ("abc", "El grupo 1 delimita el problema solo por el costo. El grupo 2 lo hace por costo, salud del aire interior y participación de las familias. ¿Cuál delimitación es más completa?", "La del grupo 2, porque integra dimensiones técnica, ambiental y social", "La del grupo 1, porque es más simple", "Ninguna, porque no hay delimitación posible", "El problema real tiene varias dimensiones y conviene nombrarlas."),
        ("abc", "Un integrante dice: «la ética es opinión y no importa en un problema de física». ¿Qué falla?", "Las decisiones sobre tecnologías afectan a personas y ambientes y requieren criterios éticos explícitos", "Nada: la ética nunca interviene", "La física no se puede aplicar a la escuela", "Aplicar la física tiene consecuencias que se evalúan con criterios éticos."),
    ],
    ctx=("abc", "Una escuela ficticia piensa instalar un panel solar. ¿Qué disciplinas deberían participar en el análisis?", "Física (energía), tecnología (instalación), economía (costos), ciencias ambientales (impacto) y la comunidad escolar", "Solo la física", "Solo la economía", "Un buen análisis integra el aporte técnico con los efectos económicos, ambientales y sociales."),
    sc=[
        ("En Física aplicada: ¿para qué sirve integrar varias ciencias en un problema?", "Para usar cada conocimiento en la parte del problema que le corresponde", "Ningún conocimiento solo cubre todas las dimensiones."),
        ("¿Qué pregunta ética resume quién se beneficia y quién se perjudica?", "¿Quién gana y quién asume los riesgos?", "Revela cómo se reparten los efectos de una decisión."),
        ("¿Cuántos kWh son el 10 % de 300 kWh?", "30 kWh", "Se calcula 300 × 10 ÷ 100."),
    ],
    op=("Elige un problema. Problema 1: un liceo ficticio quiere reemplazar sus ampolletas por otras que gastan menos energía. Problema 2: un pueblo ficticio quiere calentar agua para el comedor escolar con energía solar. Escribe una pregunta investigable, las ciencias que participan y qué aporta cada una, los actores afectados y una pregunta ética que deban responder antes de decidir.",
        "Problema 2: pregunta: ¿cuántos kWh por mes ahorra el comedor al calentar agua con energía solar? Ciencias: física (energía y calor), química (materiales), ciencias ambientales (emisiones), economía (costos). Actores: estudiantes, cocineras, familias y municipio. Pregunta ética: ¿quién paga y quién se beneficia?",
        ["formula una pregunta con variable, unidad y sistema", "asigna aportes a al menos tres ciencias", "nombra actores y una pregunta ética"],
        ["hoja con las cuatro partes completas"],
        ["usar una pregunta de opinión", "nombrar una sola ciencia", "omitir los actores afectados"],
        "Pregunta: «¿quién podría quedar fuera de la decisión que propones?»."),
    reinforce="Con la ficha, calcula cuántos kWh se ahorran en un año (12 meses) con la medida de ejemplo.",
    extend="Explica por qué dos grupos con la misma información física pueden llegar a decisiones distintas y cómo se resolvería ese desacuerdo.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (de ejemplo, datos inventados). Panel fotovoltaico ficticio de 5 kW de potencia en condiciones ideales. Horas de sol equivalentes por día: 5 h. Consumo de la escuela: 30 kWh por día. "
     "Fuente X: folleto comercial sin método ni datos. Fuente Y: informe independiente con mediciones de un año en la zona. Emisión de la red eléctrica de ejemplo: 400 g de CO2 por kWh.")
build(
    O6, 2, F,
    use="Aprenderé a evaluar fuentes y variables en un problema de energía que une física, ciencias ambientales y economía, y a calcular producción y emisiones evitadas.",
    prior=["Sé que energía = potencia × tiempo.", "Sé qué es una fuente confiable.", "Sé calcular porcentajes."],
    explain=[
        "Un panel fotovoltaico transforma luz en electricidad. Su potencia (en kW) indica cuánto entrega en condiciones ideales; la energía producida en un día es potencia × horas de sol equivalentes. Con 5 kW y 5 horas, produce 5 × 5 = 25 kWh. Las horas de sol equivalentes dependen de la latitud, la estación del año y la nubosidad, que es una variable del clima y de la atmósfera, por lo que integra la física con las ciencias de la Tierra.",
        "Para comparar con el consumo, se calcula qué porcentaje de la energía diaria cubre la producción: (25 ÷ 30) × 100, algo más de 83 %. Si esa energía reemplaza electricidad de la red, se evitan emisiones: 25 kWh × 400 g de CO2 por kWh = 10.000 g, es decir, 10 kg de CO2 al día. Estos números son estimaciones de ejemplo, y el resultado real depende de las condiciones.",
        "Para evaluar una fuente se revisa quién la produce, con qué método, durante cuánto tiempo y si tiene conflicto de intereses. Un folleto comercial que promete «producción constante de 5 kW» confunde potencia ideal con producción real. Un informe independiente de un año incluye estaciones con distinta luz y nubosidad, por lo que es mejor evidencia que una medición de un solo día soleado.",
    ],
    vocab=[("kWh", "kilovatio-hora: energía de 1 kW durante 1 hora"), ("potencia", "energía por unidad de tiempo, en kW"), ("horas de sol equivalentes", "horas con la luz máxima que dan la misma energía que el día real"), ("nubosidad", "fracción del cielo cubierta de nubes"), ("conflicto de intereses", "situación en que quien informa se beneficia de cierta conclusión"), ("fuente independiente", "fuente sin interés económico en el resultado")],
    worked=[
        ("Energía diaria", "Un panel ficticio de 3 kW tiene 6 horas de sol equivalentes. ¿Cuántos kWh produce en un día?", ["Energía = potencia × horas.", "3 × 6 = 18."], "18 kWh"),
        ("Evaluar una fuente", "Un folleto ficticio afirma que el panel «ahorra el 100 % de la cuenta». No explica método. ¿Qué haces?", ["Pregunta por el método, los datos y el interés de quien informa.", "Busca un informe independiente con mediciones en la zona."], "No lo uso como evidencia hasta contrastarlo con una fuente independiente"),
    ],
    mistakes=[("Creer que la potencia del panel es la producción diaria constante.", "Se confunde potencia ideal con energía real.", "Multiplica la potencia por las horas de sol equivalentes."),
              ("Aceptar un folleto comercial como evidencia suficiente.", "No se considera el interés de quien informa.", "Contrasta con una fuente independiente y con medición propia.")],
    T=[
        ("abc", "¿Qué mide el kWh?", "Energía", "Potencia", "Tiempo", "Un kWh es la energía de 1 kW durante 1 hora."),
        ("abc", "La energía producida por un panel en un día se calcula como", "potencia × horas de sol equivalentes", "potencia ÷ horas de sol equivalentes", "horas de sol equivalentes ÷ potencia", "La energía es la potencia por el tiempo."),
        ("ab", "Un día muy nublado hace que las horas de sol equivalentes sean", "menores", "mayores", "Las nubes bloquean parte de la luz y reducen la energía."),
        ("=", "{F} Un día nublado solo hay 2 horas de sol equivalentes. ¿Cuántos kWh produce el panel ese día?", "5*2", "Se multiplica la potencia por las horas de sol equivalentes de ese día.", " kWh"),
        ("abc", "{F} ¿Qué fuente es más confiable para estimar la producción real?", "La fuente Y, porque mide un año en la zona y es independiente", "La fuente X, porque es la más breve", "Ambas por igual, porque hablan del panel", "Un informe independiente con mediciones de un año reduce el sesgo."),
        ("abc", "¿Qué variable de la atmósfera afecta la producción de un panel?", "La nubosidad, que bloquea parte de la luz", "El color de la casa", "El nombre del instalador", "La luz que llega al panel depende de las nubes."),
        ("=", "{F} En un día de 5 horas de sol equivalentes, ¿cuántos kWh del consumo diario de la escuela quedan sin cubrir por el panel?", "30-5*5", "Se resta la producción del consumo diario.", " kWh"),
        ("=", "{F} Si la producción de 25 kWh por día reemplaza energía de la red, ¿cuántos kg de CO2 se evitan en 10 días? (1 kg = 1000 g)", "10*25*400//1000", "Se multiplica la energía de los 10 días por la emisión de cada kWh y se pasa a kg.", " kg"),
        ("=", "En un mes de 30 días con 4 horas de sol equivalentes por día, ¿cuántos kWh produce un panel de 5 kW?", "5*4*30", "Se multiplica potencia, horas diarias y días.", " kWh"),
        ("abc", "Un folleto dice que el panel «producirá siempre 5 kW». ¿Qué falla?", "Confunde la potencia en condiciones ideales con la producción real, que depende de las horas de sol", "Nada, es correcto", "Los kW no se aplican a paneles", "La producción real varía con la luz, la hora y la nubosidad."),
        ("abc", "El informe Y mide durante un año completo. ¿Por qué es relevante la duración?", "Porque incluye estaciones con distinta luz y nubosidad", "Porque un año suma más kWh", "Porque los paneles solo funcionan un año", "La variación entre estaciones del año queda representada en los datos."),
        ("=", "El invierno tiene 3 horas de sol equivalentes y el verano 7. ¿Cuántos kWh más produce el panel de 5 kW un día de verano que uno de invierno?", "5*7-5*3", "Se calcula la producción de cada estación y se resta.", " kWh"),
        ("abc", "Una persona propone comprobar el folleto con una sola medición en un día soleado. ¿Qué problema tiene?", "Un día no representa el año y sesgaría la estimación al alza", "Ninguno, un día basta", "El Sol solo sale en verano", "Una medición única de un día extremo no refleja la variación anual."),
    ],
    ctx=("abc", "Para decidir el tamaño de un panel para la escuela, ¿qué datos debe reunir primero la comunidad?", "El consumo diario de energía de la escuela y las horas de sol de la zona", "El color del techo", "La edad del alcalde", "Sin consumo ni horas de sol no se puede dimensionar el panel."),
    sc=[
        ("En Física aplicada: ¿cómo se calcula la energía diaria de un panel?", "Potencia por horas de sol equivalentes", "Es la fórmula básica de energía."),
        ("¿Un folleto comercial es suficiente como evidencia?", "No", "Hay que contrastarlo con una fuente independiente."),
        ("¿Cuántos kWh produce un panel de 2 kW con 4 horas de sol equivalentes?", "8 kWh", "Se calcula la energía como 2 kW por 4 horas."),
    ],
    op=("Elige un caso. Caso 1: una posta rural ficticia con consumo de 20 kWh por día, y un panel de 4 kW con 5 horas de sol equivalentes. Caso 2: un jardín infantil ficticio con consumo de 12 kWh por día y un panel de 3 kW con 4 horas de sol. Calcula la producción, el porcentaje del consumo que cubre y los kg de CO2 que evita por día (400 g por kWh); después evalúa con tres preguntas una fuente que promete «cubrir el 100 % del consumo todo el año».",
        "Caso 1: producción = 4 × 5 = 20 kWh, que cubre el 100 % en un día soleado; evita 20 × 400 ÷ 1000 = 8 kg de CO2. La fuente que promete 100 % todo el año: ¿qué método usó?, ¿midió el invierno?, ¿quién la financió?",
        ["calcula producción, porcentaje y CO2 con unidades", "formula tres preguntas para evaluar la fuente", "distingue día soleado y año completo"],
        ["hoja con cálculos y las tres preguntas"],
        ["confundir potencia con energía", "aceptar la promesa sin preguntas", "olvidar las unidades"],
        "Pregunta: «¿qué dato te permitiría comprobar que funciona en invierno?»."),
    reinforce="Con la ficha, calcula cuántos kWh produce el panel en 10 días con 5 horas de sol equivalentes.",
    extend="Explica por qué el almacenamiento (baterías) es un tema físico, químico y ambiental al mismo tiempo.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (de ejemplo, datos inventados). Potencia perdida por un muro: P = U × A × ΔT, con P en W, U (transmitancia) en W/(m²·°C), A el área del muro en m² y ΔT la diferencia entre la temperatura interior y la exterior, en °C. "
     "Un U menor significa mejor aislación. Muro sin aislar: U = 2. Muro con aislación: U = 0,5. Área: 20 m². Temperatura interior de ejemplo: 16 °C; exterior: 6 °C (ΔT = 10 °C). Energía en kWh = potencia en W × horas ÷ 1000.")
build(
    O6, 3, F,
    use="Aprenderé a construir un modelo simple que une física (pérdidas de calor), ambiente y economía para comparar una solución de aislación térmica.",
    prior=["Sé que el calor pasa de lo caliente a lo frío.", "Sé que energía = potencia × tiempo.", "Sé qué es un modelo simplificado."],
    explain=[
        "Un muro pierde calor hacia el exterior por conducción. Un modelo simple dice que la potencia perdida es P = U × A × ΔT: crece con el área del muro, con la diferencia de temperatura y con la transmitancia U, que es mayor cuando el material aísla peor. Con U = 1, A = 50 m² y ΔT = 10 °C, el muro pierde 1 × 50 × 10 = 500 W. Con una aislación que baja U a 0,2, pierde 100 W: una quinta parte.",
        "La energía perdida en un tiempo t es potencia × tiempo. Si se pierden 500 W durante 4 horas, son 2000 Wh, es decir, 2 kWh. Ahorrar calefacción reduce el consumo de combustible o de electricidad y, con ello, las emisiones. Para evaluar la medida se compara el costo inicial con el ahorro acumulado en el tiempo y con el beneficio ambiental y de confort.",
        "El modelo integra, pero también simplifica. Considera solo la conducción por el muro y deja fuera filtraciones de aire por rendijas, pérdidas por ventanas y techo, y la humedad. Además, desde la salud y la química del aire, aislar sin ventilación segura puede acumular humedad y gases interiores, especialmente si hay combustión. Un buen análisis declara estos límites y busca soluciones que combinen aislación y ventilación adecuada.",
    ],
    vocab=[("transmitancia (U)", "medida de cuánto calor pasa por m² y por °C, menor es mejor aislación"), ("aislación térmica", "material o diseño que reduce el paso de calor"), ("ΔT", "diferencia de temperatura entre dos lugares"), ("filtración", "paso de aire por rendijas"), ("ventilación", "renovación del aire interior"), ("costo-beneficio", "comparación entre lo que se gasta y lo que se gana")],
    worked=[
        ("Potencia perdida", "Un muro ficticio de 10 m² tiene U = 2 y ΔT = 5 °C. ¿Qué potencia pierde?", ["P = U × A × ΔT = 2 × 10 × 5.", "Calcula el producto."], "100 W"),
        ("Energía perdida", "Ese muro pierde 100 W durante 12 horas. ¿Cuántos kWh son?", ["Energía en Wh = 100 × 12 = 1200.", "Pasa a kWh dividiendo por 1000: 1,2."], "1,2 kWh"),
    ],
    mistakes=[("Creer que un U mayor aísla mejor.", "Se invierte el significado de U.", "Recuerda: más U, más calor que pasa."),
              ("Olvidar pasar de Wh a kWh.", "Se usa 1000 W como 1 W.", "Divide por 1000.")],
    T=[
        ("abc", "En P = U × A × ΔT, un valor de U menor significa que el muro", "aísla mejor", "aísla peor", "no pierde calor nunca", "Menor U implica menos calor que pasa por cada m² y cada °C."),
        ("abc", "La pérdida de calor por un muro aumenta cuando", "aumenta la diferencia de temperatura entre interior y exterior", "disminuye el área del muro", "disminuye el valor de U", "La potencia perdida P es proporcional a la diferencia ΔT."),
        ("ab", "Si un muro pierde 300 W durante 5 horas, la energía perdida es", "1,5 kWh", "15 kWh", "Se calcula 300 × 5 = 1500 Wh, que son 1,5 kWh."),
        ("=", "{F} ¿Cuántos W pierde el muro sin aislar?", "2*20*10", "Se aplica P = U × A × ΔT con U = 2.", " W"),
        ("=", "{F} ¿Cuántos W pierde el muro con aislación (U = 0,5, es decir, la mitad de 1)?", "20*10//2", "Con U = 0,5, la potencia es 0,5 × 20 × 10.", " W"),
        ("abc", "{F} ¿Cuánto reduce las pérdidas la aislación?", "Las reduce a la cuarta parte: 100 W en vez de 400 W", "Las reduce a la mitad", "No las reduce", "Pasa de 400 W a 100 W, una cuarta parte."),
        ("=", "{F} ¿Cuántos kWh pierde el muro sin aislar en 5 horas?", "400*5//1000", "Se multiplica los 400 W por las horas y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuántos kWh se ahorran en 10 horas con la aislación?", "(400-100)*10//1000", "Se ahorran 300 W durante 10 horas y se pasa a kWh.", " kWh"),
        ("=", "Un muro de 30 m² con U = 2 y ΔT = 10 °C. ¿Cuántos W pierde?", "2*30*10", "Se aplica P = U × A × ΔT.", " W"),
        ("abc", "La aislación cuesta al inicio, pero ahorra combustible cada día. Para evaluarla se compara", "el costo inicial con el ahorro acumulado en el tiempo y el beneficio ambiental", "solo el costo inicial", "solo el color del material", "Una evaluación costo-beneficio mira el tiempo y los efectos."),
        ("abc", "Si se aísla mejor pero se cierra del todo la ventilación en una sala donde hay combustión, ¿qué riesgo aparece desde la salud y la química del aire?", "Acumulación de humedad y de gases interiores, por lo que debe mantenerse una ventilación segura", "Ninguno", "Que la sala se enfríe más", "La ventilación renueva el aire y evita acumular gases y humedad."),
        ("abc", "El modelo P = U × A × ΔT considera la conducción por un muro. ¿Qué pérdida deja fuera?", "Las filtraciones de aire por rendijas y las pérdidas por ventanas y techo", "Ninguna", "La gravedad", "El modelo es una simplificación de una parte del problema."),
        ("=", "En una noche más fría con ΔT = 20 °C, el muro sin aislar de la ficha (U = 2, A = 20) pierde ¿cuántos W?", "2*20*20", "Se aplica la fórmula con la nueva diferencia de temperatura.", " W"),
    ],
    ctx=("abc", "Una escuela ficticia puede aislar el techo (ahorro de 3 kWh por día) o cambiar la caldera (ahorro de 2 kWh por día, pero con menos humo). ¿Qué información falta para decidir con criterio integrado?", "Costos, impactos en la salud, emisiones y la opinión de la comunidad", "Solo el ahorro de energía", "El color de cada opción", "La decisión integra energía, salud, ambiente, costos y participación."),
    sc=[
        ("En Física aplicada: ¿qué significa un valor bajo de U?", "Que el muro aísla bien", "Pasa poco calor por m² y por °C."),
        ("¿Cuántos kWh son 3000 Wh?", "3 kWh", "Para pasar de Wh a kWh se divide por 1000."),
        ("¿Aislar sin ventilar puede traer riesgos?", "Sí", "Puede acumularse humedad y gases interiores."),
    ],
    op=("Elige un caso. Caso 1: un muro de 15 m² con U = 2 y ΔT = 10 °C, aislado a U = 0,5. Caso 2: un muro de 25 m² con U = 2 y ΔT = 8 °C, aislado a U = 0,5. Calcula la potencia perdida antes y después, el ahorro en kWh durante 10 horas y escribe dos límites del modelo y una condición de seguridad (ventilación) para aislar bien.",
        "Caso 1: antes: 2 × 15 × 10 = 300 W; después: 0,5 × 15 × 10 = 75 W; ahorro: 225 W × 10 h = 2.250 Wh = 2,25 kWh. Límites: no considera filtraciones ni ventanas. Condición: mantener ventilación segura.",
        ["calcula potencia antes y después con unidades", "calcula el ahorro en kWh", "declara límites y una condición de seguridad"],
        ["hoja con los cálculos y las dos frases"],
        ["confundir U con mejor aislación", "olvidar pasar a kWh", "omitir la ventilación"],
        "Pregunta: «¿qué pérdidas no incluye tu cálculo?»."),
    reinforce="Con la ficha, calcula la potencia perdida si ΔT fuera 5 °C, sin y con aislación.",
    extend="Explica por qué ahorrar energía en calefacción puede ser, a la vez, un beneficio ambiental, económico y de salud.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (de ejemplo, puntajes inventados de 1 a 5, donde 5 es lo mejor). Tres propuestas para la escuela ficticia, evaluadas en cuatro criterios, en este orden: ahorro de energía, costo, salud del aire interior y aceptación de la comunidad. "
     "Propuesta 1 (aislar el techo): 4, 3, 4, 5. Propuesta 2 (panel solar): 3, 2, 5, 4. Propuesta 3 (cambiar la caldera): 3, 4, 2, 3. Un criterio con peso 2 cuenta doble.")
build(
    O6, 4, F,
    use="Aprenderé a analizar evidencia y valores en una decisión con implicancias éticas, sociales y ambientales, usando una matriz de criterios y reconociendo sus límites.",
    prior=["Sé sumar y comparar puntajes.", "Sé que los criterios pueden tener distinta importancia.", "Sé qué es la transparencia."],
    explain=[
        "Una matriz de decisión ordena las opciones en filas y los criterios en columnas. Cada celda lleva un puntaje y la suma permite comparar. Para comparar se suman los puntajes de cada fila. Por ejemplo, una opción ficticia con puntajes 2, 5, 3 y 3 suma 13. Si un criterio es más importante se le da peso 2, es decir, su puntaje cuenta doble: si el segundo criterio pesa doble, esa opción suma 2 + 2 × 5 + 3 + 3 = 18.",
        "La matriz ayuda a pensar, pero tiene límites: los puntajes son estimaciones y pueden ser subjetivos. Por eso se declara quién los asignó y con qué evidencia, y se prueba si el resultado cambia al variar los pesos (análisis de sensibilidad). Un criterio como la aceptación de la comunidad no es un detalle: si las personas afectadas rechazan una opción, la decisión no será legítima ni estable.",
        "En la dimensión ética se aplican la justicia (¿quién gana y quién carga con los costos?), la participación (¿quiénes fueron escuchados?), la precaución (actuar con prudencia ante riesgos graves) y la transparencia (explicar datos, criterios y límites, también los de la opción preferida). Una buena decisión muestra la tabla, los supuestos, cómo se escucharon las opiniones y qué se hará si los resultados no son los esperados.",
    ],
    vocab=[("matriz de decisión", "tabla que compara opciones según criterios"), ("peso", "importancia relativa de un criterio, que multiplica su puntaje"), ("análisis de sensibilidad", "prueba de cuánto cambia el resultado al variar los pesos o puntajes"), ("subjetivo", "que depende de la valoración de quien evalúa"), ("legitimidad", "aceptación de una decisión por quienes la reciben"), ("principio de precaución", "actuar con prudencia ante un riesgo grave aunque falte certeza")],
    worked=[
        ("Sumar puntajes", "Una opción ficticia tiene puntajes 5, 2, 3 y 4 en cuatro criterios. ¿Cuánto suma?", ["Suma todos los puntajes.", "5 + 2 + 3 + 4 = 14."], "14 puntos"),
        ("Dar peso doble", "En esa opción, el segundo criterio (puntaje 2) pasa a contar doble. ¿Cuánto suma ahora?", ["El 2 cuenta doble: 2 × 2 = 4.", "Suma: 5 + 4 + 3 + 4."], "16 puntos"),
    ],
    mistakes=[("Creer que la suma de puntajes es una verdad objetiva.", "Se ignora que los puntajes y los pesos son valoraciones.", "Declara quién puntuó, con qué evidencia, y prueba otros pesos."),
              ("Ignorar el rechazo de la comunidad si la opción suma más puntos.", "Se trata la participación como adorno.", "Considera la aceptación como parte del problema.")],
    T=[
        ("abc", "El principio de precaución dice que ante un riesgo posible y grave", "conviene tomar medidas prudentes aunque falte certeza total", "se debe esperar a tener certeza absoluta", "se debe ignorar el riesgo", "Ante daños graves, esperar certeza total puede ser demasiado tarde."),
        ("abc", "Una decisión justa se pregunta", "¿quiénes se benefician y quiénes cargan con los costos?", "¿cuál es la más rápida de ejecutar?", "¿cuál es la más barata para quien decide?", "La justicia mira cómo se reparten beneficios y costos."),
        ("ab", "Transparencia significa", "explicar los datos y criterios usados para decidir", "ocultar los criterios para evitar discusiones", "Permite que otras personas revisen y cuestionen la decisión."),
        ("=", "{F} ¿Cuánto suma la propuesta 1 con puntajes simples?", "4+3+4+5", "Se suman los cuatro puntajes de la propuesta.", " puntos"),
        ("=", "{F} ¿Cuánto suma la propuesta 2 con puntajes simples?", "3+2+5+4", "Se suman los cuatro puntajes de la propuesta.", " puntos"),
        ("=", "{F} ¿Cuánto suma la propuesta 3 con puntajes simples?", "3+4+2+3", "Se suman los cuatro puntajes de la propuesta.", " puntos"),
        ("=", "{F} Si el ahorro de energía cuenta doble, ¿cuánto suma la propuesta 1?", "2*4+3+4+5", "El primer puntaje se multiplica por 2 y los demás se suman.", " puntos"),
        ("=", "{F} Si el ahorro de energía cuenta doble, ¿cuánto suma la propuesta 2?", "2*3+2+5+4", "El primer puntaje se multiplica por 2 y los demás se suman.", " puntos"),
        ("=", "{F} Si el ahorro de energía cuenta doble, ¿cuánto suma la propuesta 3?", "2*3+4+2+3", "El primer puntaje se multiplica por 2 y los demás se suman.", " puntos"),
        ("abc", "{F} Con puntajes simples, ¿qué propuesta resulta mejor y por cuánto sobre la segunda?", "La propuesta 1, por 2 puntos", "La propuesta 2, por 2 puntos", "La propuesta 3, por 4 puntos", "Las sumas son 16, 14 y 12; la primera supera a la segunda por 2."),
        ("abc", "Un integrante dice que los puntajes son subjetivos. ¿Qué respuesta es adecuada?", "Es cierto: por eso se declara quién los asignó y con qué evidencia, y se prueba cómo cambia el resultado al variar los pesos", "Entonces la matriz no sirve para nada", "Son exactos y no se discuten", "Reconocer la subjetividad y probar la sensibilidad fortalece la decisión."),
        ("abc", "{F} Los puntajes dan 16, 14 y 12, pero la comunidad rechaza la propuesta 1. ¿Qué debería hacerse?", "Volver a analizar con la comunidad, porque la aceptación y la participación son parte del problema", "Imponer la propuesta 1 porque suma más", "Borrar el criterio de aceptación", "Una decisión rechazada por los afectados no es legítima ni estable."),
        ("abc", "Un informe presenta solo la propuesta preferida y oculta sus riesgos. ¿Qué principio se vulnera?", "La transparencia", "La rapidez", "El ahorro", "Ocultar riesgos impide a otras personas evaluar la decisión."),
    ],
    ctx=("abc", "Una comunidad ficticia debe elegir entre las propuestas de la ficha. ¿Qué debe preparar para que la decisión sea legítima?", "Una tabla con criterios, puntajes, supuestos, límites y cómo se escucharon las opiniones", "Solo el nombre de la propuesta ganadora", "Solo la opinión de quien dirige", "La legitimidad requiere transparencia, participación y límites declarados."),
    sc=[
        ("En Física aplicada: ¿qué es el análisis de sensibilidad?", "Probar cuánto cambia el resultado al variar pesos o puntajes", "Muestra qué tan robusta es una decisión."),
        ("¿Qué pregunta mide la justicia de una decisión?", "¿Quiénes se benefician y quiénes cargan con los costos?", "Se trata del reparto de efectos."),
        ("¿Cuánto suma una opción con puntajes 3, 3, 4 y 5?", "15 puntos", "Se suma 3 + 3 + 4 + 5."),
    ],
    op=("Elige una decisión. Decisión 1: un barrio ficticio debe elegir entre instalar paneles solares en el consultorio o aislar el edificio. Decisión 2: un colegio ficticio debe elegir entre cambiar la caldera o aislar el techo. Construye una matriz con tres criterios (ahorro de energía, impacto ambiental y aceptación de la comunidad), puntajes de ejemplo de 1 a 5, calcula la suma, prueba un peso doble en un criterio, y escribe dos límites de tu matriz y una pregunta ética.",
        "Decisión 2: aislar techo: 4, 4, 5 (suma 13); cambiar caldera: 3, 2, 3 (suma 8). Con peso doble en impacto ambiental: 17 y 10. Límites: los puntajes son de ejemplo y subjetivos; faltan costos. Pregunta ética: ¿quiénes cargan con los costos?",
        ["construye una matriz con puntajes y sumas correctas", "prueba un peso doble", "declara límites y una pregunta ética"],
        ["hoja con la matriz, las sumas, la prueba de peso y los límites"],
        ["no declarar quién puntuó", "ignorar la participación", "tomar la suma como verdad absoluta"],
        "Pregunta: «¿qué pasa con tu decisión si cambias el peso del criterio más importante?»."),
    reinforce="Con la ficha, calcula las sumas si el costo cuenta doble en las tres propuestas.",
    extend="Explica por qué una decisión técnicamente correcta puede fracasar si no se escuchó a las personas afectadas.",
)

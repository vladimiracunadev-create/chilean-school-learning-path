"""Mecánica Automotriz TP (3.º y 4.º medio) módulo B: OAE-04 (motores de gasolina, diésel, gas e híbridos, y sus sistemas de lubricación, refrigeración y control de emisiones) y OAE-05 (sistemas hidráulicos y neumáticos: suspensión, dirección, frenos y transmisión). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meau_common import AVISO, EMER, build

O4 = "TP-MEAU-3y4-OAE-04"
O5 = "TP-MEAU-3y4-OAE-05"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller «Motores Demo» recibe vehículos con cuatro tipos de motor: a gasolina, diésel, a gas e híbrido (un motor de combustión más un motor eléctrico con una batería de alto voltaje). "
     "Su matriz de peligros anota: combustible inflamable, gases de escape, piezas calientes, sistemas a presión, partes giratorias y, en los híbridos, alto voltaje. Vehículos ingresados hoy: 9 a gasolina, 6 diésel, 3 a gas y 2 híbridos.")
build(
    O4, 1, F,
    use="Aprenderé qué tipos de motor existen, qué peligros tiene cada uno en un taller y qué institución fiscaliza combustibles y electricidad.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé sumar y multiplicar números enteros.", "Sé que un vehículo usa un combustible o electricidad."],
    explain=[
        "Un motor de combustión interna transforma la energía química del combustible en movimiento. El motor a gasolina enciende la mezcla con una chispa; el diésel la enciende por el calor de comprimir el aire; el motor a gas usa gas natural o gas licuado como combustible; y el híbrido combina un motor de combustión con un motor eléctrico y una batería de alto voltaje. Todos tienen sistemas de lubricación, refrigeración y control de emisiones.",
        "Los peligros dependen del tipo: el combustible es inflamable y no se acerca a llamas ni chispas; el gas puede acumularse si hay una fuga; los gases de escape contienen monóxido de carbono, que es tóxico; los sistemas a presión y las piezas calientes pueden causar lesiones; y el alto voltaje de un híbrido exige formación y autorización específicas. Por eso cualquier intervención la hace personal autorizado.",
        f"La Superintendencia de Electricidad y Combustibles (SEC) fiscaliza instalaciones de combustibles, gas y electricidad según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("motor de combustión interna", "motor que transforma la energía química del combustible en movimiento"), ("motor diésel", "motor que enciende el combustible por el calor de comprimir el aire"), ("motor híbrido", "combina un motor de combustión y un motor eléctrico con batería"), ("inflamable", "que se enciende con facilidad"), ("alto voltaje", "tensión eléctrica muy superior a la de una batería común de 12 V"), ("SEC", "Superintendencia de Electricidad y Combustibles")],
    worked=[
        ("Tipo de motor", "Un motor de ejemplo enciende la mezcla de aire y combustible con una chispa. ¿Qué tipo de motor es?", ["La chispa es propia del encendido de la gasolina.", "El diésel se enciende por compresión, sin chispa."], "Un motor a gasolina"),
        ("Tipo de control", "Un taller de ejemplo prohíbe llamas abiertas en la zona de combustibles con una regla escrita y una señal. ¿Qué tipo de control es?", ["Una regla y una señal ordenan la conducta.", "Eso es un control administrativo."], "Control administrativo"),
    ],
    mistakes=[("Creer que un híbrido no tiene peligros de combustible porque «tiene batería».", "El híbrido conserva el combustible y suma el alto voltaje.", "Suma los peligros de cada fuente de energía."),
              ("Considerar que una batería de alto voltaje es «igual a una de 12 V».", "El alto voltaje puede ser mortal y exige formación específica.", "La interviene solo personal autorizado y certificado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué hace un motor de combustión interna?", "Transforma la energía química del combustible en movimiento", "Almacena energía eléctrica para el arranque", "Enfría el aire del habitáculo", "El motor convierte el combustible en movimiento; el almacenamiento eléctrico y el aire acondicionado son otros sistemas."),
        ("abc", "En Mecánica Automotriz: ¿en qué se diferencia un motor híbrido de uno a gasolina?", "Combina un motor de combustión con un motor eléctrico y una batería de alto voltaje", "Funciona solo con baterías, sin ningún motor de combustión", "Usa dos tanques de gasolina", "El híbrido suma un motor eléctrico al de combustión."),
        ("abc", "En Mecánica Automotriz: ¿cómo se enciende el combustible en un motor diésel?", "Por el calor de comprimir el aire, sin chispa", "Con una chispa de una bujía", "Con una llama permanente dentro del cilindro", "El diésel se enciende por compresión, no por chispa."),
        ("abc", "{F} ¿Qué peligro de la matriz es propio de los híbridos y exige formación específica?", "El alto voltaje", "Las piezas calientes", "Los gases de escape", "Las piezas calientes y los gases de escape afectan a todos los motores; el alto voltaje es propio del híbrido."),
        ("abc", "{F} ¿Qué peligro previene la regla de no usar llamas ni chispas cerca de los combustibles?", "El incendio por combustible inflamable", "El ruido", "El alto voltaje", "El combustible inflamable se enciende con una llama o una chispa."),
        ("abc", "{F} El taller exige un permiso escrito firmado antes de intervenir un híbrido. ¿Qué tipo de control es?", "Un control administrativo", "Un control de ingeniería", "La eliminación del peligro", "Un permiso es una regla escrita que ordena la conducta; no cambia el equipo ni quita el peligro."),
        ("=", "{F} ¿Cuántos vehículos ingresaron hoy en total?", "9+6+3+2", "Se suman los vehículos de los cuatro tipos de motor.", " vehículos"),
        ("=", "{F} Los vehículos a gas e híbridos requieren personal con formación específica. ¿Cuántos de los ingresados hoy requieren ese personal?", "3+2", "Se suman los vehículos a gas y los híbridos.", " vehículos"),
        ("=", "{F} La revisión documental de cada vehículo diésel toma 3 horas y la de cada híbrido, 5 horas. ¿Cuántas horas suman?", "6*3+2*5", "Se multiplican los vehículos de cada tipo por sus horas y se suman.", " horas"),
        ("abc", "{F} Un compañero dice: «en el híbrido no hay peligro de combustible porque tiene batería». ¿Qué respuesta es correcta?", "Es falso: el híbrido tiene combustible inflamable y además alto voltaje, por lo que suma peligros", "Es cierto, porque la batería reemplaza al combustible", "Es cierto, si el motor eléctrico está apagado", "El híbrido conserva el motor de combustión, por eso conserva sus peligros."),
        ("abc", "Un aprendiz de ejemplo quiere hacer funcionar un motor a gasolina dentro de un taller con la puerta cerrada «solo un momento». ¿Qué corresponde?", "No hacerlo: los gases de escape son tóxicos y esa tarea la decide personal autorizado con ventilación y extracción adecuadas", "Hacerlo, si es solo un momento", "Hacerlo, si usa una mascarilla de papel", "El monóxido de carbono es tóxico aun en poco tiempo y una mascarilla de papel no lo detiene."),
        ("=", "{F} El taller tiene 3 puestos de trabajo y cada uno atiende 1 vehículo por turno. Si hay 2 turnos, ¿cuántos de los vehículos ingresados hoy quedan para otro día?", "(9+6+3+2)-3*2", "Se restan los vehículos atendidos en los dos turnos al total ingresado.", " vehículos"),
        ("abc", "En una visita a un taller de ejemplo se siente olor a combustible y alguien ve una llama pequeña. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apagar la llama con lo que haya a mano", "Abrir todas las puertas y esperar sin avisar", "Acercarse a un conato de incendio sin formación puede sumar otro accidente; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "Una persona te pide en un taller de ejemplo que le «revises rápido» la batería de su vehículo híbrido porque «es solo una batería». ¿Qué respondes?", "Que la batería de alto voltaje solo la interviene personal con formación y autorización específicas, y que se avisa a un adulto responsable del taller", "Que es igual a una batería común de 12 V", "Que sí, si apaga el motor", "El alto voltaje exige formación específica; apagar el motor no lo elimina."),
    sc=[
        ("En Mecánica Automotriz: ¿qué gas tóxico contienen los gases de escape?", "El monóxido de carbono", "No se ve ni se huele y es tóxico."),
        ("¿Qué institución fiscaliza instalaciones de combustibles, gas y electricidad?", "La SEC", "Esa superintendencia fiscaliza esos sectores según la norma vigente."),
        ("¿Cómo se enciende el combustible de un motor diésel?", "Por el calor de la compresión del aire", "El diésel no usa chispa para encender."),
    ],
    op=("El taller de ejemplo recibe un vehículo a gas y un vehículo híbrido. Escribe (a) un peligro propio de cada uno, (b) un control de ingeniería y un control administrativo para cualquiera de ellos, (c) por qué el EPP no basta, (d) quién interviene estos vehículos. No describas cómo se interviene ninguno.",
        "(a) Gas: acumulación de gas si hay una fuga; híbrido: alto voltaje. (b) Ingeniería: ventilación o detección de gas en la zona; administrativo: permiso escrito y señal de que solo personal autorizado interviene. (c) El EPP es la última barrera y no reemplaza la formación ni quita el peligro. (d) Personal con formación y autorización específicas, con la norma vigente.",
        ["nombra un peligro propio de cada vehículo", "propone un control de ingeniería y uno administrativo", "explica por qué el EPP no basta", "indica quién interviene"],
        ["hoja con las cuatro respuestas"],
        ["decir que el híbrido no tiene combustible", "proponer solo el EPP", "describir cómo se interviene el vehículo"],
        "Pregunta: «¿qué fuente de energía tiene cada vehículo?». Si no responde, pídele que relea los peligros de cada tipo de motor."),
    reinforce="Escribe los cuatro tipos de motor de la clase y, junto a cada uno, un peligro propio de su energía.",
    extend="Explica con un ejemplo por qué un taller necesita reglas distintas para vehículos a gas y para híbridos.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo, inventada). Motor M-4 del «Modelo Demo 8»: 4 cilindros; volumen de cada cilindro (cilindrada unitaria), 450 cm³; volumen de la cámara de combustión de cada cilindro, 50 cm³; ciclo de cuatro tiempos; 2 válvulas por cilindro; capacidad de aceite, 4 L.")
build(
    O4, 2, F,
    use="Aprenderé los cuatro tiempos del motor, sus partes principales, qué hacen la lubricación y la refrigeración y cómo se calculan la cilindrada y la relación de compresión.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es un volumen.", "Sé que un motor tiene cilindros y pistones."],
    explain=[
        "En un motor de cuatro tiempos cada cilindro repite cuatro etapas en orden: admisión (entra aire o mezcla), compresión (el pistón sube y comprime), expansión (la combustión empuja el pistón hacia abajo y entrega energía) y escape (salen los gases quemados). El pistón, la biela y el cigüeñal convierten el movimiento de subida y bajada en giro. El bloque contiene los cilindros y la culata aloja las válvulas de admisión y escape.",
        "El sistema de lubricación reduce el roce entre piezas con una película de aceite que impulsa una bomba y limpia un filtro. El sistema de refrigeración retira calor con líquido, radiador, bomba y termostato. La cilindrada total es el número de cilindros por la cilindrada unitaria. La relación de compresión es la cilindrada unitaria más el volumen de la cámara, dividido por el volumen de la cámara.",
        f"Esta clase explica partes y cálculos en papel; abrir o reparar un motor es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("cuatro tiempos", "admisión, compresión, expansión y escape"), ("cilindrada unitaria", "volumen de un cilindro"), ("cámara de combustión", "volumen que queda sobre el pistón cuando está arriba"), ("relación de compresión", "volumen total del cilindro dividido por el volumen de la cámara"), ("lubricación", "reducción del roce con una película de aceite"), ("refrigeración", "retiro del calor del motor con líquido")],
    worked=[
        ("Cilindrada total", "Un motor de ejemplo tiene 6 cilindros de 300 cm³ cada uno. ¿Cuál es su cilindrada total?", ["Se multiplican los cilindros por la cilindrada unitaria.", "6 por 300 son 1.800."], "1.800 cm³"),
        ("Relación de compresión", "Un cilindro de ejemplo tiene cilindrada unitaria 350 cm³ y cámara de 50 cm³. ¿Cuál es su relación de compresión?", ["Se suman 350 y 50 y da 400.", "400 dividido por 50 es 8."], "8 a 1"),
    ],
    mistakes=[("Confundir la cilindrada de un cilindro con la cilindrada total del motor.", "La total multiplica por el número de cilindros.", "Pregunta si el dato es de un cilindro o de todos."),
              ("Creer que el aceite y el líquido refrigerante cumplen la misma función.", "El aceite reduce el roce y el líquido retira el calor: son sistemas distintos.", "Asocia cada sistema con su función.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cuáles son los cuatro tiempos de un motor, en orden?", "Admisión, compresión, expansión y escape", "Compresión, admisión, escape y expansión", "Admisión, escape, compresión y expansión", "Primero entra la mezcla, luego se comprime, se quema y se expulsa."),
        ("abc", "En Mecánica Automotriz: ¿qué función cumple el sistema de lubricación del motor?", "Reducir el roce entre piezas en movimiento con una película de aceite", "Mantener la temperatura con líquido refrigerante", "Dosificar el combustible que entra al cilindro", "La lubricación usa aceite para reducir el roce; la temperatura la controla la refrigeración."),
        ("abc", "En Mecánica Automotriz: ¿qué función cumple el sistema de refrigeración del motor?", "Retirar calor para mantener el motor en su temperatura de funcionamiento", "Reducir el roce con una película de aceite", "Mejorar la mezcla de aire y combustible", "La refrigeración retira el calor; la lubricación y la mezcla son otras funciones."),
        ("abc", "{F} ¿Qué mide la cilindrada unitaria de la ficha?", "El volumen de cada cilindro", "El volumen total del motor", "El volumen del líquido refrigerante", "La cilindrada unitaria es el volumen de un solo cilindro."),
        ("abc", "{F} ¿Qué ocurre en el tiempo de expansión?", "La combustión empuja al pistón hacia abajo y entrega energía", "El pistón sube y comprime la mezcla", "Los gases quemados salen por la válvula de escape", "La expansión es el tiempo en que se obtiene la energía; subir comprime y los gases salen en el escape."),
        ("abc", "{F} ¿Qué piezas convierten el movimiento de subida y bajada del pistón en giro?", "La biela y el cigüeñal", "La culata y el termostato", "El filtro de aceite y la bomba de agua", "El pistón empuja la biela y esta hace girar el cigüeñal."),
        ("=", "{F} ¿Cuántos cm³ tiene la cilindrada total del motor M-4?", "4*450", "Se multiplican los cilindros por la cilindrada unitaria.", " cm³"),
        ("=", "{F} ¿Cuál es la relación de compresión del motor M-4? Responde el número que va antes de «a 1».", "(450+50)//50", "Se suman cilindrada unitaria y cámara, y se divide entre la cámara.", " a 1"),
        ("=", "{F} ¿Cuántas válvulas tiene el motor M-4 en total?", "4*2", "Se multiplican los cilindros por las válvulas de cada uno.", " válvulas"),
        ("abc", "{F} Un compañero dice: «la cilindrada total de M-4 es 450 cm³, porque es el valor de la ficha». ¿Qué respuesta es correcta?", "Es falso: 450 cm³ es de cada cilindro y el total multiplica por los 4 cilindros", "Es cierto, porque la ficha da un solo volumen", "Es falso: el total es la suma de la cilindrada unitaria y la cámara", "La cilindrada unitaria es de un cilindro; el total depende del número de cilindros."),
        ("abc", "Un aprendiz dice que «el aceite y el líquido refrigerante hacen lo mismo». ¿Qué respuesta es correcta?", "Es falso: el aceite reduce el roce y el líquido retira el calor, en sistemas distintos", "Es cierto, son el mismo líquido con dos nombres", "Es falso: el aceite refrigera todo el motor y el líquido es opcional", "Cada sistema cumple una función propia y ninguno reemplaza al otro."),
        ("abc", "{F} Si se reduce la cámara de combustión de 50 a 25 cm³ con la misma cilindrada unitaria, ¿qué ocurre con la relación de compresión?", "Aumenta, porque el volumen total se divide entre una cámara menor", "Disminuye, porque la cámara es más pequeña", "No cambia, porque la cilindrada unitaria es la misma", "Al dividir entre un número menor el resultado crece."),
        ("=", "Un motor de ejemplo de 6 cilindros tiene una cilindrada total de 3.000 cm³ y una cámara de 50 cm³ por cilindro. ¿Cuál es su relación de compresión? Responde el número que va antes de «a 1».", "(3000//6+50)//50", "Se obtiene la cilindrada unitaria, se suma la cámara y se divide entre la cámara.", " a 1"),
    ],
    ctx=("abc", "Una persona lee en una ficha «1.600 cm³, 4 cilindros» y te pregunta cuánto mide cada cilindro. ¿Qué respondes?", "400 cm³, porque 1.600 dividido entre 4 es 400", "1.600 cm³ cada uno", "6.400 cm³ cada uno", "La cilindrada total se reparte en partes iguales entre los cilindros."),
    sc=[
        ("En Mecánica Automotriz: ¿qué tiempo del motor entrega la energía?", "La expansión", "La combustión empuja el pistón durante la expansión."),
        ("¿Cómo se calcula la cilindrada total?", "Multiplicando los cilindros por la cilindrada unitaria", "Cada cilindro aporta el mismo volumen."),
        ("¿Qué sistema retira calor del motor?", "La refrigeración", "Su líquido, radiador y bomba retiran el calor."),
    ],
    op=("Ficha de ejemplo: motor N-6 con 6 cilindros de 600 cm³ cada uno y cámara de 60 cm³ por cilindro. Escribe (a) la cilindrada total, (b) la relación de compresión, (c) los cuatro tiempos en orden, (d) qué sistema retira el calor del motor.",
        "(a) 6 × 600 = 3.600 cm³. (b) (600 + 60) ÷ 60 = 11, es decir 11 a 1. (c) Admisión, compresión, expansión y escape. (d) El sistema de refrigeración.",
        ["calcula la cilindrada total", "calcula la relación de compresión", "ordena los cuatro tiempos", "nombra el sistema"],
        ["hoja con las cuatro respuestas"],
        ["confundir cilindrada unitaria y total", "olvidar sumar la cámara", "desordenar los tiempos"],
        "Pregunta: «¿el dato de 600 cm³ es de un cilindro o de todos?». Si duda, pídele que relea la definición de cilindrada unitaria."),
    reinforce="Inventa un motor con número de cilindros, cilindrada unitaria y cámara, y calcula la cilindrada total y la relación de compresión.",
    extend="Explica con un ejemplo qué pasaría con el roce de las piezas si faltara la película de aceite.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Vehículo «Modelo Demo 8» con motor M-4. Quejas escritas: (1) «sale humo azulado por el escape y hay que agregar aceite seguido»; (2) «el indicador de temperatura sube y el ventilador no se activa»; (3) «el motor tironea al acelerar». "
     "Tabla de orientación del manual de ejemplo (síntoma y sistema candidato): humo azulado y consumo de aceite, lubricación y sellado del cilindro; indicador de temperatura alto, refrigeración; tirones al acelerar, alimentación de combustible o encendido. "
     "Nota: la tabla orienta y la causa se confirma con inspección y datos. Registro de personal autorizado para la queja 2: nivel de líquido refrigerante, 3 L (mínimo de ejemplo: 5 L); el ventilador recibe energía pero no gira.")
build(
    O4, 3, F,
    use="Aprenderé a relacionar quejas con sistemas del motor usando una tabla de orientación, a combinar hallazgos de un registro y a escribir un informe prudente.",
    prior=["Sé qué es un síntoma y un sistema candidato.", "Sé restar números enteros.", "Sé que la lubricación y la refrigeración son sistemas del motor."],
    explain=[
        "Una tabla de orientación del manual relaciona un síntoma con uno o más sistemas candidatos, que luego se verifican con inspección y datos; no confirma la pieza dañada. Un mismo vehículo puede tener varias quejas distintas, cada una con su sistema candidato, y un registro puede traer varios hallazgos que no se explican entre sí: dos hallazgos distintos pueden requerir dos verificaciones.",
        "El sobrecalentamiento es una temperatura de funcionamiento por sobre la prevista y puede dañar gravemente el motor. Un sistema de refrigeración caliente está a presión: el líquido caliente puede causar quemaduras graves, por lo que solo personal autorizado interviene. El informe debe decir qué se observó, qué sistema orienta y qué falta verificar, sin afirmar una pieza dañada.",
        f"Esta clase interpreta informes escritos; no se interviene ningún motor. {EMER} {AVISO}",
    ],
    vocab=[("tabla de orientación", "tabla que relaciona síntomas con sistemas candidatos"), ("hallazgo", "dato observado en un registro de inspección"), ("sobrecalentamiento", "temperatura de funcionamiento por sobre la prevista"), ("sellado del cilindro", "hermeticidad del cilindro que evita fugas de aceite y de gases"), ("alimentación de combustible", "sistema que lleva el combustible al motor")],
    worked=[
        ("Sistema candidato", "Una queja de ejemplo dice: «el motor suelta humo negro y gasta mucho combustible». La tabla del manual de ejemplo asocia humo negro con alimentación de combustible. ¿Qué sistema es candidato?", ["La tabla relaciona el síntoma con un sistema.", "El sistema candidato es la alimentación de combustible."], "Alimentación de combustible"),
        ("Dos hallazgos", "Un registro de ejemplo anota una tensión de batería baja y luces del tablero débiles. ¿Qué sistema comprometen los dos?", ["Ambos hallazgos se refieren a la energía eléctrica.", "El sistema que la reparte es el sistema eléctrico."], "El sistema eléctrico"),
    ],
    mistakes=[("Tomar la tabla de orientación como si confirmara la pieza dañada.", "La tabla orienta hacia un sistema; la causa se confirma con inspección.", "Escribe «sistema candidato» y la verificación que falta."),
              ("Creer que un solo hallazgo explica todos los síntomas del vehículo.", "Cada queja puede tener una causa distinta.", "Relaciona cada queja con sus propios datos.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿para qué sirve una tabla de orientación del manual?", "Para relacionar un síntoma con sistemas candidatos que luego se verifican", "Para confirmar la pieza dañada sin inspección", "Para calcular el costo de la reparación", "La tabla orienta; la confirmación la dan la inspección y los datos."),
        ("abc", "En Mecánica Automotriz: ¿qué es el sobrecalentamiento de un motor?", "Una temperatura de funcionamiento por sobre la prevista, que puede dañar el motor", "Un calentamiento rápido al encender, que es normal", "Una temperatura exterior alta", "El sobrecalentamiento es una temperatura del motor sobre la prevista, no el clima ni el calentamiento normal."),
        ("abc", "En Mecánica Automotriz: ¿por qué solo personal autorizado interviene un sistema de refrigeración caliente?", "Porque está a presión y el líquido caliente puede causar quemaduras graves", "Porque el líquido se pierde por evaporación", "Porque se contamina el aire del taller", "La presión y la temperatura son el peligro; la evaporación o el aire no son la razón."),
        ("abc", "{F} ¿Qué sistema candidato indica la tabla para la queja 1?", "Lubricación y sellado del cilindro", "Refrigeración", "Alimentación de combustible o encendido", "La tabla asocia humo azulado y consumo de aceite con la lubricación y el sellado."),
        ("abc", "{F} ¿Qué hallazgo del registro apunta al sistema de refrigeración?", "El nivel de líquido refrigerante bajo el mínimo", "El humo azulado del escape", "Los tirones al acelerar", "El registro de la queja 2 trae un nivel de líquido refrigerante bajo."),
        ("abc", "{F} ¿Qué advierte la nota de la tabla de orientación?", "Que la tabla orienta y la causa se confirma con inspección y datos", "Que la tabla identifica la pieza exacta", "Que la tabla solo sirve para vehículos nuevos", "La nota recuerda que la tabla no confirma la causa."),
        ("=", "{F} El vehículo recibe 1 L de aceite cada 1.500 km. ¿Cuántos L de aceite agrega en 6.000 km?", "(6000//1500)*1", "Se divide el recorrido entre los km de cada reposición y se multiplica por el litro.", " L"),
        ("=", "{F} El indicador de temperatura sube a 112 °C y el máximo normal de ejemplo es 100 °C. ¿Cuántos °C sobre el máximo está?", "112-100", "Se resta el máximo normal a la lectura del indicador.", " °C"),
        ("=", "{F} ¿Cuántos L faltan para llegar al mínimo de líquido refrigerante?", "5-3", "Se resta el nivel registrado al mínimo.", " L"),
        ("abc", "{F} Un compañero dice: «como el nivel de refrigerante está bajo, queda explicado que el ventilador no gire». ¿Qué respuesta es correcta?", "Es falso: son dos hallazgos distintos y el nivel bajo no explica por sí solo que el ventilador reciba energía y no gire", "Es cierto, porque sin refrigerante ningún ventilador gira", "Es cierto, porque ambos son del sistema de lubricación", "El registro muestra dos hallazgos distintos, y cada uno necesita su verificación."),
        ("abc", "Un aprendiz propone rellenar de inmediato un sistema de refrigeración recién apagado y caliente. ¿Qué corresponde?", "No intervenir: el sistema caliente está a presión y la tarea la decide personal autorizado", "Hacerlo, si usa guantes", "Hacerlo, si espera solo un minuto", "El sistema caliente a presión puede proyectar líquido; unos guantes o un minuto no lo evitan."),
        ("=", "{F} Verificar cada queja toma 2 horas de personal autorizado a $13.000 la hora, y por agrupar las tres quejas en una visita se descuentan $10.000. ¿Cuántos pesos cuesta verificar las 3 quejas?", "3*2*13000-10000", "Se multiplican las quejas, las horas y la tarifa, y se resta el descuento.", " pesos"),
        ("abc", "{F} ¿Qué informe es el más adecuado para la queja 2?", "Indicador alto, nivel de refrigerante bajo el mínimo y ventilador que no gira: orienta al sistema de refrigeración y se deriva a verificación autorizada", "El motor tiene la culata dañada y debe cambiarse", "El motor está bien y el indicador de temperatura falló", "El informe cita los hallazgos, orienta al sistema y no afirma una pieza dañada."),
    ],
    ctx=("abc", "Una persona propietaria te pregunta en un taller de ejemplo si puede seguir usando su vehículo con el indicador de temperatura alto «hasta llegar a casa». ¿Qué respondes?", "Que no conviene: un motor sobrecalentado puede dañarse gravemente y conviene avisar al taller para que personal autorizado lo evalúe", "Que sí, porque el motor siempre aguanta", "Que sí, si sube la calefacción al máximo", "Un motor sobrecalentado puede sufrir daños graves; la calefacción no lo soluciona."),
    sc=[
        ("En Mecánica Automotriz: ¿qué relaciona una tabla de orientación?", "Síntomas con sistemas candidatos", "Sirve para orientar la verificación posterior."),
        ("¿Por qué no se abre un sistema de refrigeración caliente?", "Porque está a presión y puede quemar", "El líquido caliente a presión puede causar quemaduras graves."),
        ("¿Un hallazgo puede explicar todas las quejas de un vehículo?", "No necesariamente", "Cada queja puede tener una causa distinta."),
    ],
    op=("Ficha de ejemplo: queja escrita: «se enciende la luz de aviso de presión de aceite al ralentí». Tabla del manual de ejemplo: luz de presión de aceite, lubricación. Registro de personal autorizado: nivel de aceite 2 L (mínimo de ejemplo: 3 L). Escribe (a) el sistema candidato, (b) el hallazgo que lo apoya, (c) cuántos L faltan para el mínimo, (d) qué no puedes concluir todavía y quién verifica.",
        "(a) La lubricación. (b) El nivel de aceite bajo el mínimo. (c) 3 − 2 = 1 L. (d) No se puede afirmar qué pieza falla ni por qué bajó el nivel; la verificación la hace personal autorizado.",
        ["nombra el sistema candidato", "cita el hallazgo", "calcula lo que falta", "indica el límite de la conclusión y quién verifica"],
        ["hoja con las cuatro respuestas"],
        ["afirmar una pieza dañada", "no citar el hallazgo", "calcular mal lo que falta"],
        "Pregunta: «¿qué dice la tabla y qué dice el registro?». Si no responde, pídele que relea la nota sobre la tabla de orientación."),
    reinforce="Inventa tres quejas de un vehículo y asocia a cada una un sistema candidato.",
    extend="Explica con un ejemplo por qué dos hallazgos del mismo vehículo pueden tener causas distintas.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado; lo tomó personal autorizado). Motor de 4 cilindros del «Modelo Demo 9». Presión de compresión por cilindro, en kPa (valores de ejemplo): cilindro 1, 1.050; cilindro 2, 1.040; cilindro 3, 800; cilindro 4, 1.060. "
     "Especificación de ejemplo: mínimo de 950 kPa por cilindro y diferencia máxima de 100 kPa entre el mayor y el menor valor. Consumo de combustible de ejemplo: 8 L cada 100 km; recorrido semanal, 400 km; precio de ejemplo: $1.200 el litro.")
build(
    O4, 4, F,
    use="Aprenderé a comparar un registro de compresión con su especificación, a calcular consumo y costo de combustible y a conocer qué hace el catalizador.",
    prior=["Sé comparar y restar números enteros.", "Sé qué es una especificación.", "Sé que un motor tiene varios cilindros."],
    explain=[
        "La presión de compresión mide qué tan bien sella cada cilindro. La especificación suele pedir un mínimo para cada cilindro y una diferencia máxima entre el mayor y el menor valor. Un valor muy bajo en un solo cilindro apunta a un problema localizado en ese cilindro, y debe verificarse. Un promedio no reemplaza a la especificación, porque puede ocultar a un cilindro que no cumple.",
        "El consumo de combustible se expresa en litros cada 100 km; el consumo de un recorrido es el recorrido dividido por 100 y multiplicado por el consumo. El costo es el volumen por el precio del litro. El catalizador es una pieza del sistema de escape que reduce gases contaminantes mediante reacciones químicas, y forma parte del control de emisiones junto con sensores como el de oxígeno.",
        f"Los registros los toma personal autorizado y esta clase solo los lee. {EMER} {AVISO}",
    ],
    vocab=[("presión de compresión", "presión que alcanza un cilindro al comprimir la mezcla, y refleja su sellado"), ("diferencia máxima", "mayor valor menos menor valor permitido"), ("consumo", "litros de combustible cada 100 km"), ("catalizador", "pieza del escape que reduce gases contaminantes"), ("kPa", "kilopascal, unidad de presión")],
    worked=[
        ("Diferencia entre cilindros", "Un registro de ejemplo da 900, 920, 880 y 930 kPa, con diferencia máxima de 80 kPa. ¿Cumple ese criterio?", ["La diferencia es el mayor menos el menor: 930 menos 880 son 50.", "50 no supera 80."], "Sí, cumple"),
        ("Consumo de un recorrido", "Un vehículo de ejemplo consume 6 L cada 100 km y recorre 500 km. ¿Cuántos L consume?", ["500 km son 5 tramos de 100 km.", "5 por 6 son 30."], "30 L"),
    ],
    mistakes=[("Aprobar el motor porque el promedio supera el mínimo.", "Un promedio oculta al cilindro que no cumple.", "Compara cada cilindro con el mínimo y calcula la diferencia entre el mayor y el menor."),
              ("Leer «8 L cada 100 km» como «100 L cada 8 km».", "El consumo es litros por tramo de 100 km.", "Lee primero los litros y después los 100 km.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué indica un valor de compresión mucho más bajo en un solo cilindro?", "Un problema localizado en ese cilindro, que debe verificarse", "Que el motor está bien porque los otros cilindros están altos", "Que falta combustible en todo el vehículo", "Un valor aislado bajo apunta al sellado de ese cilindro, no a todo el motor."),
        ("abc", "En Mecánica Automotriz: ¿qué hace el catalizador en el sistema de escape?", "Reduce gases contaminantes del escape mediante reacciones químicas", "Aumenta la potencia del motor", "Enfría el aceite del motor", "El catalizador pertenece al control de emisiones y trata los gases del escape."),
        ("abc", "En Mecánica Automotriz: ¿cómo se expresa el consumo de combustible de un vehículo?", "En litros cada 100 km", "En kilómetros por hora", "En grados Celsius por litro", "El consumo relaciona litros con distancia recorrida."),
        ("abc", "{F} ¿Qué cilindro tiene el valor de compresión más bajo?", "El cilindro 3", "El cilindro 1", "El cilindro 4", "800 kPa del cilindro 3 es el valor más bajo del registro."),
        ("abc", "{F} Además del mínimo por cilindro, ¿qué otro criterio trae la especificación?", "Que la diferencia entre el mayor y el menor valor no pase de 100 kPa", "Que todos los cilindros tengan exactamente el mismo valor", "Que el promedio supere 1.000 kPa", "La especificación fija una diferencia máxima entre cilindros, no igualdad exacta."),
        ("abc", "{F} ¿Qué significa un consumo de 8 L cada 100 km?", "Que recorre 100 km por cada 8 L de combustible", "Que gasta 100 L cada 8 km", "Que gasta 8 L por hora", "El consumo mide litros por cada 100 km recorridos."),
        ("=", "{F} ¿Cuántos kPa de diferencia hay entre el mayor y el menor valor del registro?", "1060-800", "Se resta el menor valor al mayor.", " kPa"),
        ("=", "{F} ¿Cuántos L de combustible consume el vehículo en una semana?", "(400//100)*8", "Se divide el recorrido entre 100 y se multiplica por el consumo.", " L"),
        ("=", "{F} ¿Cuántos pesos gasta en combustible en una semana?", "(400//100)*8*1200", "Se calculan los litros y se multiplican por el precio del litro.", " pesos"),
        ("abc", "{F} ¿Qué conclusión corresponde para el registro de compresión?", "El cilindro 3 queda bajo el mínimo de 950 kPa y la diferencia supera 100 kPa: no conforme, se deriva a personal autorizado", "Todo cumple porque tres cilindros están sobre 950 kPa", "El motor completo está dañado y debe cambiarse", "Basta un cilindro bajo el mínimo para no conformar, pero el registro no prueba que todo el motor esté dañado."),
        ("abc", "{F} Un compañero dice: «como el promedio de los cuatro valores supera 950 kPa, el motor cumple». ¿Qué respuesta es correcta?", "No corresponde: la especificación exige cada cilindro sobre el mínimo y limita la diferencia; el promedio oculta al cilindro 3", "Corresponde, porque el promedio resume el estado del motor", "Corresponde, si el cilindro 3 no es el primero del registro", "Un promedio no reemplaza el criterio por cilindro de la especificación."),
        ("=", "{F} Una mejora de mantenimiento baja el consumo a 7 L cada 100 km. ¿Cuántos pesos se ahorran en 4 semanas con el mismo recorrido y precio?", "(8-7)*(400//100)*4*1200", "Se calcula el ahorro semanal de litros, se multiplica por 4 semanas y por el precio.", " pesos"),
        ("abc", "{F} Tras una verificación autorizada, el cilindro 3 mide 1.000 kPa y los otros cilindros no cambian. ¿Cumple el registro?", "Sí: todos superan 950 kPa y la diferencia entre 1.060 y 1.000 es 60, bajo el máximo de 100", "No, porque el cilindro 3 sigue siendo el más bajo", "No, porque 1.000 es menor que 1.060", "Cumple el mínimo en cada cilindro y la diferencia es de 60 kPa."),
    ],
    ctx=("abc", "Una persona que vende vehículos de ejemplo te pide quitar del informe el valor bajo del cilindro 3 antes de mostrarlo a una persona compradora. ¿Qué respondes?", "Que el informe debe reflejar los valores medidos y no se modifica, porque ocultar un dato afecta la seguridad y la confianza", "Que sí, porque es información del vendedor", "Que sí, si baja el precio", "Un informe técnico no se edita para favorecer una venta."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula la diferencia entre cilindros?", "Restando el menor valor al mayor", "La especificación fija un máximo para esa diferencia entre cilindros."),
        ("¿Cuántos L consume en 300 km un vehículo de 6 L cada 100 km?", "18 L", "300 km son 3 tramos de 100 km, y 3 por 6 son 18."),
        ("¿Qué reduce el catalizador?", "Los gases contaminantes del escape", "Es parte del control de emisiones."),
    ],
    op=("Ficha de ejemplo: motor de 4 cilindros con presiones de compresión de 920, 930, 900 y 780 kPa. Especificación de ejemplo: mínimo de 850 kPa por cilindro y diferencia máxima de 100 kPa. Consumo: 9 L cada 100 km; recorrido semanal, 300 km; precio de ejemplo: $1.100 el litro. Escribe (a) qué cilindro no cumple el mínimo, (b) la diferencia entre el mayor y el menor valor y si cumple el criterio, (c) si el registro cumple en general, (d) los litros y los pesos de combustible de una semana.",
        "(a) El cuarto, con 780 kPa. (b) 930 − 780 = 150 kPa, que supera los 100 kPa: no cumple. (c) No cumple, porque falla el mínimo y la diferencia. (d) (300 ÷ 100) × 9 = 27 L; 27 × 1.100 = 29.700 pesos.",
        ["identifica el cilindro bajo el mínimo", "calcula y evalúa la diferencia", "concluye sobre el registro", "calcula litros y costo"],
        ["hoja con las cuatro respuestas"],
        ["aprobar por el promedio", "calcular mal la diferencia", "confundir litros con pesos"],
        "Pregunta: «¿qué cilindro está más lejos de los demás?». Si duda, pídele que relea cómo se evalúa un registro de compresión."),
    reinforce="Inventa un registro de cuatro cilindros con una especificación de mínimo y diferencia máxima, y decide si cumple.",
    extend="Explica con un ejemplo por qué un solo cilindro bajo mínimo no se puede compensar con otros cilindros altos.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (alternativas y pruebas finales de ejemplo, inventadas). Un motor con baja compresión en un cilindro admite dos alternativas. Alternativa A: reacondicionar el motor con personal autorizado; repuestos $180.000, mano de obra 12 horas, garantía 6 meses. "
     "Alternativa B: reemplazar el motor por uno reacondicionado; motor $520.000, mano de obra 8 horas, garantía 12 meses. Tarifa: $13.000 por hora. Pruebas finales exigidas por el manual de ejemplo: presión de aceite entre 150 y 300 kPa; temperatura entre 80 y 100 °C; CO no mayor que 2 unidades. "
     "Resultados registrados: presión de aceite, 220 kPa; temperatura, 96 °C; CO, 3 unidades.")
build(
    O4, 5, F,
    use="Aprenderé a comparar dos alternativas de trabajo en un motor por costo, garantía y cumplimiento, y a verificar la calidad con pruebas finales registradas y residuos bien gestionados.",
    prior=["Sé calcular costo con horas y tarifa.", "Sé dividir números enteros.", "Sé comparar un resultado con un rango."],
    explain=[
        "Un motor reacondicionado es un motor usado cuyas partes fueron reparadas o reemplazadas para dejarlo dentro de especificación. Para comparar alternativas se calcula el costo total (repuestos más horas por tarifa), se calcula el costo por mes de garantía y se miran el cumplimiento de la especificación y la seguridad. La decisión final es de la persona propietaria, con la información del taller.",
        "La prueba final de funcionamiento es una verificación, registrada por escrito, de que las magnitudes quedaron dentro de la especificación antes de entregar; la realiza personal autorizado. Si una prueba no cumple, el vehículo no se entrega y se informa a la jefatura. Los registros no se modifican para cumplir un plazo. Las piezas retiradas y el aceite usado son residuos que se clasifican y se entregan a un gestor autorizado, según la norma vigente.",
        f"Esta clase compara cifras y registros; el trabajo en el motor lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("motor reacondicionado", "motor usado cuyas partes se repararon o reemplazaron"), ("prueba final", "verificación registrada de que las magnitudes cumplen antes de entregar"), ("costo por mes de garantía", "costo total dividido por los meses de garantía"), ("residuo", "pieza o fluido retirado que debe gestionarse"), ("registro", "documento que deja constancia de lo medido y lo hecho")],
    worked=[
        ("Costo total", "Una alternativa de ejemplo cuesta $100.000 en repuestos y 5 horas a $12.000 la hora. ¿Cuál es su costo total?", ["La mano de obra son 5 por 12.000, es decir 60.000.", "Se suman 100.000 y 60.000."], "$160.000"),
        ("Verificar contra el rango", "Una prueba final de ejemplo pide de 80 a 100 °C y el resultado es 82 °C. ¿Cumple?", ["82 está entre 80 y 100.", "Un valor dentro del rango cumple."], "Sí, cumple"),
    ],
    mistakes=[("Entregar el vehículo con una prueba final fuera de rango porque «las otras salieron bien».", "Basta una prueba que no cumple para no entregar.", "Informa a la jefatura y deriva a personal autorizado."),
              ("Modificar un resultado del registro para cumplir el plazo.", "Falsear un registro es una falta grave y oculta un riesgo.", "Anota el valor real y deriva el caso.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es una prueba final de funcionamiento?", "Una verificación registrada por escrito de que las magnitudes quedaron dentro de la especificación antes de entregar", "Una prueba en la que la persona propietaria recibe el vehículo para ver si falla", "Una revisión que hace la persona compradora al recibir el vehículo", "La prueba final es una verificación del taller, registrada antes de la entrega."),
        ("abc", "En Mecánica Automotriz: ¿qué es un motor reacondicionado?", "Un motor usado cuyas partes fueron reparadas o reemplazadas para dejarlo dentro de especificación", "Un motor nuevo de fábrica sin uso", "Un motor usado que solo fue lavado", "El reacondicionamiento repara o reemplaza partes; lavar no basta."),
        ("abc", "En Mecánica Automotriz: ¿qué se hace con las piezas y el aceite que se retiran en un trabajo de motor?", "Se clasifican y se entregan a un gestor autorizado cuando son residuos, según la norma vigente", "Se botan con la basura común del taller", "Se guardan sin registro en cualquier rincón", "Los residuos del taller requieren clasificación y un gestor autorizado."),
        ("abc", "{F} ¿Qué prueba final no cumple lo exigido?", "La del CO", "La de presión de aceite", "La de temperatura", "El CO es 3 y el máximo es 2; la presión y la temperatura están dentro de sus rangos."),
        ("abc", "{F} ¿Se puede entregar el vehículo con esos resultados?", "No, porque una prueba final no cumple y se informa a la jefatura", "Sí, porque dos de tres pruebas cumplen", "Sí, porque el CO es la prueba menos importante", "Basta una prueba que no cumple para impedir la entrega."),
        ("abc", "{F} ¿Qué alternativa exige menos horas de mano de obra?", "La alternativa B", "La alternativa A", "Ambas exigen las mismas horas", "B usa 8 horas y A usa 12."),
        ("=", "{F} ¿Cuántos pesos cuesta en total la alternativa A?", "180000+12*13000", "Se suman los repuestos con las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta en total la alternativa B?", "520000+8*13000", "Se suma el motor con las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta por mes de garantía la alternativa A?", "(180000+12*13000)//6", "Se divide el costo total de A entre sus 6 meses de garantía.", " pesos"),
        ("abc", "{F} ¿Qué alternativa tiene menor costo por mes de garantía y cuánto?", "La B, con 52.000 pesos por mes frente a 56.000 de la A", "La A, porque su costo total es menor", "Ambas cuestan lo mismo por mes", "A cuesta 336.000 entre 6 meses y B cuesta 624.000 entre 12 meses."),
        ("abc", "Tras una nueva medición de personal autorizado, el CO del vehículo de la ficha da 2 unidades. ¿Qué corresponde?", "Cumple el límite, porque un valor igual al límite cumple, y las tres pruebas quedan conformes", "No cumple, porque debe ser menor que 2", "Cumple solo si el motor es nuevo", "El límite se incluye en lo conforme, sin importar si el motor es nuevo o reacondicionado."),
        ("=", "{F} El taller descuenta $24.000 de la mano de obra de B y se paga en 4 cuotas iguales. ¿Cuántos pesos es cada cuota?", "(520000+8*13000-24000)//4", "Se calcula el total con el descuento y se divide entre 4.", " pesos"),
        ("abc", "{F} ¿Qué informe de pruebas finales corresponde?", "Presión de aceite 220 kPa y temperatura 96 °C conformes; CO 3 sobre el límite de 2, no conforme; no se entrega y se deriva a personal autorizado", "Todas las pruebas conformes", "No conforme, sin indicar los valores", "El informe cita cada resultado con su límite y la decisión de no entregar."),
    ],
    ctx=("abc", "Quien dirige un taller de ejemplo quiere entregar hoy el vehículo con CO 3 y «ajustar el registro» para que diga 2. ¿Qué corresponde?", "No modificar el registro: se informa el valor real y se deriva a personal autorizado, porque falsear un registro es una falta grave", "Ajustar el registro para cumplir el plazo", "Anotar 2 pero avisar solo a la persona propietaria", "Un registro refleja el valor medido; cambiarlo oculta un riesgo."),
    sc=[
        ("En Mecánica Automotriz: ¿cuántas pruebas finales deben cumplir para entregar?", "Todas", "Una sola prueba fuera de rango impide la entrega."),
        ("¿Cómo se calcula el costo por mes de garantía?", "Dividiendo el costo total entre los meses de garantía", "Permite comparar alternativas con plazos distintos."),
        ("¿A quién se entregan los residuos del taller?", "A un gestor autorizado", "La norma vigente exige gestionarlos con quien está autorizado."),
    ],
    op=("Ficha de ejemplo: alternativa X: repuestos $90.000, 6 horas y garantía de 3 meses. Alternativa Y: repuestos $180.000, 4 horas y garantía de 12 meses. Tarifa: $15.000 por hora. Prueba final de ejemplo: presión de aceite entre 150 y 300 kPa; resultado, 140 kPa. Escribe (a) el costo total de cada alternativa, (b) el costo por mes de garantía de cada una, (c) si la prueba final cumple, (d) qué haces si no cumple.",
        "(a) X: 90.000 + 6 × 15.000 = 180.000; Y: 180.000 + 4 × 15.000 = 240.000. (b) X: 180.000 ÷ 3 = 60.000; Y: 240.000 ÷ 12 = 20.000. (c) No cumple, porque 140 está bajo el mínimo de 150. (d) No se entrega el vehículo, se informa a la jefatura y se deriva a personal autorizado, sin modificar el registro.",
        ["calcula los costos totales", "calcula el costo por mes", "evalúa la prueba final", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["elegir solo por el costo total", "aprobar la prueba fuera de rango", "modificar el registro"],
        "Pregunta: «¿140 está dentro del rango de 150 a 300?». Si duda, pídele que relea cómo se evalúa un rango."),
    reinforce="Inventa dos alternativas con repuestos, horas y garantía, y calcula cuál tiene menor costo por mes.",
    extend="Explica con un ejemplo por qué una prueba final que no cumple debe detener la entrega.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller «Chasis Demo» trabaja con suspensión, dirección, frenos y transmisión. Su matriz de peligros anota: vehículo elevado, fluido hidráulico a presión, aire comprimido, resortes comprimidos, piezas pesadas de transmisión y fluidos calientes. "
     "Cada día se atienden 10 vehículos; 4 de ellos tienen trabajos en frenos o en dirección.")
build(
    O5, 1, F,
    use="Aprenderé qué son los sistemas hidráulicos y neumáticos del vehículo, por qué la suspensión, la dirección y los frenos son sistemas de seguridad y qué peligros tienen en un taller.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé sumar y multiplicar números enteros.", "Sé que un vehículo tiene frenos y dirección."],
    explain=[
        "Un sistema hidráulico transmite fuerza con un líquido y un sistema neumático la transmite con aire comprimido. En los vehículos se usan en la suspensión (amortiguadores y resortes), en la dirección asistida, en los frenos (de líquido en los livianos y, a menudo, de aire en los pesados) y en la transmisión de potencia, manual con embrague o automática con un circuito de fluido.",
        "La dirección y los frenos son sistemas de seguridad: una falla puede causar un accidente. Por eso se exigen repuestos con la referencia correcta, verificación registrada y control de calidad antes de entregar. Los peligros del taller incluyen el fluido hidráulico a presión, que puede salir proyectado y lesionar, el aire comprimido, que puede proyectar objetos, y los resortes comprimidos, que almacenan energía y pueden liberarla de golpe.",
        f"Estos trabajos los hace personal autorizado, con norma vigente, y la revisión técnica periódica también verifica estos sistemas. {EMER} {AVISO}",
    ],
    vocab=[("sistema hidráulico", "transmite fuerza con un líquido"), ("sistema neumático", "transmite fuerza con aire comprimido"), ("suspensión", "conjunto de resortes y amortiguadores que une las ruedas al vehículo"), ("dirección asistida", "dirección con ayuda de un circuito de fluido"), ("sistema de seguridad", "sistema cuya falla puede causar un accidente"), ("energía almacenada", "energía que puede liberarse de golpe, como la de un resorte comprimido")],
    worked=[
        ("Hidráulico o neumático", "Un camión de ejemplo acciona un freno con aire comprimido. ¿El sistema es hidráulico o neumático?", ["El fluido que transmite la fuerza es aire comprimido.", "Un sistema con aire comprimido es neumático."], "Neumático"),
        ("Peligro y riesgo", "Un taller de ejemplo tiene un charco de fluido hidráulico en el piso de un pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el charco de fluido en el piso.", "El riesgo es que alguien resbale y se lesione."], "Peligro: el charco de fluido; riesgo: que alguien resbale y se lesione"),
    ],
    mistakes=[("Pensar que el fluido del freno es inofensivo si salpica.", "A presión puede proyectarse, lesionar y dañar el sistema.", "Solo personal autorizado interviene un circuito con fluido."),
              ("Creer que un resorte comprimido «ya está quieto».", "Almacena energía y puede liberarla de golpe.", "Lo trata solo personal autorizado, con la norma vigente.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué diferencia hay entre un sistema hidráulico y uno neumático?", "El hidráulico transmite fuerza con un líquido y el neumático con aire comprimido", "El hidráulico usa electricidad y el neumático usa gas combustible", "El hidráulico es siempre más grande que el neumático", "La diferencia está en el fluido que transmite la fuerza."),
        ("abc", "En Mecánica Automotriz: ¿por qué se llaman sistemas de seguridad la dirección y los frenos?", "Porque una falla puede causar un accidente", "Porque están dentro de una caja cerrada", "Porque se instalan solo en vehículos nuevos", "Su importancia nace de las consecuencias de una falla."),
        ("abc", "En Mecánica Automotriz: ¿qué es la energía almacenada en un resorte comprimido?", "Energía que puede liberarse de golpe y lesionar", "Energía eléctrica de la batería", "Calor que se pierde por el escape", "Un resorte comprimido guarda energía mecánica que puede soltarse de golpe."),
        ("abc", "{F} ¿Qué puede ocurrir con el fluido hidráulico a presión según la matriz?", "Salir proyectado y lesionar", "Producir solo ruido", "Quedarse sin repuestos", "El fluido a presión puede proyectarse; el ruido y los repuestos son otros asuntos."),
        ("abc", "{F} El taller exige que ningún vehículo con trabajo en frenos o dirección se entregue sin verificación registrada. ¿Qué tipo de control es?", "Un control administrativo", "Un control de ingeniería", "El equipo de protección personal", "Es una regla escrita que ordena la conducta."),
        ("abc", "{F} ¿A qué sistema se asocian los resortes comprimidos de la matriz?", "A la suspensión", "A la transmisión", "A la dirección asistida", "Los resortes forman parte de la suspensión."),
        ("=", "{F} ¿Cuántos vehículos del día no tienen trabajos en frenos ni en dirección?", "10-4", "Se restan los vehículos con frenos o dirección al total del día.", " vehículos"),
        ("=", "{F} Cada vehículo con trabajo en frenos o dirección requiere 2 horas de verificación registrada. ¿Cuántas horas suman al día?", "4*2", "Se multiplican los vehículos por las horas de verificación.", " horas"),
        ("=", "{F} Si el taller trabaja 5 días a la semana con la misma carga, ¿cuántos vehículos con trabajo en frenos o dirección atiende en la semana?", "4*5", "Se multiplican los vehículos del día por los días de la semana.", " vehículos"),
        ("abc", "{F} Un aprendiz dice: «el fluido del freno es solo un líquido; si me salpica no pasa nada». ¿Qué respuesta es correcta?", "Es falso: un fluido a presión puede proyectarse y lesionar, y solo personal autorizado interviene", "Es cierto, porque los fluidos hidráulicos son inofensivos", "Es cierto, si usa guantes", "El fluido a presión es un peligro y los guantes no autorizan a nadie."),
        ("abc", "El jefe de un taller de ejemplo pide entregar hoy un vehículo con trabajo en dirección sin la verificación registrada porque la persona propietaria espera. ¿Qué corresponde?", "Completar y registrar la verificación antes de entregar, porque es un sistema de seguridad", "Entregarlo y verificar mañana", "Entregarlo si el técnico dice que se ve bien", "En sistemas de seguridad la verificación se hace antes de la entrega."),
        ("=", "{F} El peligro del fluido a presión tiene probabilidad 3 y gravedad 5; el de los resortes comprimidos, probabilidad 2 y gravedad 4. ¿Cuántos puntos más tiene el primero?", "3*5-2*4", "Se calculan los dos puntajes como probabilidad por gravedad y se restan.", " puntos"),
        ("abc", "En una visita a un taller de ejemplo, una manguera de aire comprimido se rompe y se mueve violentamente. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sujetar la manguera", "Acercarte a cerrar tú mismo la válvula", "Acercarse a una manguera descontrolada puede causar un golpe grave."),
    ],
    ctx=("abc", "Un amigo te pide que le ayudes a «arreglar los frenos» de su vehículo en el patio de su casa. ¿Qué respondes?", "Que los frenos son un sistema de seguridad que interviene personal autorizado en un taller, con norma vigente, y que lo acompañas a consultar", "Que sí, si tienen las herramientas", "Que sí, si lo hacen despacio y con ayuda de un video", "Un sistema de seguridad no se interviene sin formación ni autorización."),
    sc=[
        ("En Mecánica Automotriz: ¿con qué transmite fuerza un sistema neumático?", "Con aire comprimido", "Neumático viene del aire a presión."),
        ("¿Qué sistemas del vehículo son de seguridad?", "La dirección y los frenos, entre otros", "Una falla en ellos puede causar un accidente."),
        ("¿Quién interviene un circuito con fluido a presión?", "Personal autorizado", "El fluido a presión puede proyectarse y lesionar."),
    ],
    op=("El taller de ejemplo anota dos peligros: un resorte de suspensión comprimido y una línea de fluido hidráulico a presión con una fuga. Escribe (a) el peligro y el riesgo de cada uno, (b) un control administrativo, (c) por qué un trabajo de frenos exige verificación registrada, (d) quién realiza estos trabajos. No describas cómo se hacen.",
        "(a) Resorte: peligro, la energía almacenada; riesgo, que se libere y golpee a alguien. Línea de fluido: peligro, el fluido a presión; riesgo, que salga proyectado y lesione. (b) Una regla escrita y una señal de que solo personal autorizado interviene. (c) Porque los frenos son un sistema de seguridad y una falla puede causar un accidente. (d) Personal autorizado, con la norma vigente.",
        ["distingue peligro y riesgo", "propone un control administrativo", "explica por qué se verifica y registra", "indica quién interviene"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al resorte", "proponer solo el EPP", "describir cómo se trabaja el sistema"],
        "Pregunta: «¿qué puede pasar si ese sistema falla?». Si no responde, pídele que relea qué es un sistema de seguridad."),
    reinforce="Escribe tres componentes de un vehículo y marca si su sistema es hidráulico, neumático o ninguno de los dos.",
    extend="Explica con un ejemplo por qué la energía almacenada es un peligro aunque no haya movimiento visible.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (esquema hidráulico de ejemplo, descrito por escrito, inventado). Circuito de accionamiento: un depósito de fluido, una bomba, una válvula y dos cilindros. Pistón de entrada: área de 4 cm². Pistón de salida: área de 20 cm². "
     "Fuerza aplicada al pistón de entrada: 100 N (valor de ejemplo). Presión = fuerza ÷ área, en N/cm².")
build(
    O5, 2, F,
    use="Aprenderé a calcular presión, a explicar cómo un circuito hidráulico multiplica la fuerza y por qué un líquido y el aire se comportan distinto.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es una fuerza.", "Sé qué es un área."],
    explain=[
        "La presión es la fuerza repartida en un área: presión = fuerza ÷ área. En un fluido encerrado, la presión se transmite igual en todo el fluido. Un líquido casi no se comprime, por eso un circuito hidráulico transmite la fuerza de inmediato; el aire sí se comprime, por eso un sistema neumático responde de forma más elástica y, si entra aire a un circuito de líquido, el accionamiento se siente esponjoso.",
        "Si la presión es igual y el pistón de salida tiene mayor área, la fuerza de salida es mayor: fuerza de salida = presión × área de salida. Pero el pistón de salida recorre menos distancia, en la misma proporción: el circuito multiplica la fuerza, no crea energía. Los componentes básicos son el depósito (guarda el fluido), la bomba (genera el flujo con presión), la válvula (permite o corta el paso) y el cilindro (convierte la presión en movimiento).",
        f"Esta clase calcula en papel; no enseña a intervenir circuitos. {EMER} {AVISO}",
    ],
    vocab=[("presión", "fuerza dividida por el área sobre la que actúa"), ("N", "newton, unidad de fuerza"), ("depósito", "componente que guarda el fluido"), ("bomba", "componente que genera el flujo con presión"), ("válvula", "componente que permite o corta el paso del fluido"), ("cilindro", "componente que convierte presión en movimiento")],
    worked=[
        ("Presión", "Una fuerza de ejemplo de 60 N actúa sobre un pistón de 3 cm². ¿Cuál es la presión?", ["La presión es la fuerza dividida por el área.", "60 entre 3 son 20."], "20 N/cm²"),
        ("Fuerza de salida", "En un circuito de ejemplo la presión es 10 N/cm² y el pistón de salida tiene 8 cm². ¿Qué fuerza entrega?", ["La fuerza es la presión por el área.", "10 por 8 son 80."], "80 N"),
    ],
    mistakes=[("Pensar que el circuito hidráulico crea energía porque la fuerza de salida es mayor.", "El pistón de salida recorre menos distancia en la misma proporción.", "Recuerda que se multiplica la fuerza, no la energía."),
              ("Calcular la presión multiplicando fuerza por área.", "La presión es fuerza dividida por área.", "Divide la fuerza entre el área.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula la presión?", "Dividiendo la fuerza entre el área", "Multiplicando la fuerza por el área", "Restando el área a la fuerza", "La presión es la fuerza repartida en un área."),
        ("abc", "En Mecánica Automotriz: ¿por qué un sistema hidráulico responde de inmediato y uno neumático se siente más elástico?", "Porque el líquido casi no se comprime y el aire sí", "Porque el líquido es más liviano que el aire", "Porque el aire siempre está más caliente", "La compresibilidad del aire explica la respuesta más elástica."),
        ("abc", "En Mecánica Automotriz: ¿qué hace una bomba en un circuito hidráulico?", "Impulsa el fluido y genera el flujo con presión", "Guarda el fluido de reserva", "Mide la temperatura del fluido", "La bomba genera el flujo; el depósito guarda la reserva."),
        ("abc", "{F} ¿Qué componente del circuito guarda el fluido de reserva?", "El depósito", "La bomba", "La válvula", "El depósito almacena el fluido; la bomba lo impulsa y la válvula regula el paso."),
        ("abc", "{F} ¿Qué pistón tiene el área mayor?", "El de salida", "El de entrada", "Tienen la misma área", "El de salida mide 20 cm² y el de entrada 4 cm²."),
        ("abc", "{F} Según el principio explicado, ¿qué ocurre con la presión de un fluido encerrado?", "Se transmite por igual en todo el fluido", "Es mayor cerca de la bomba y menor en el pistón de salida", "Desaparece al llegar a la válvula", "Esa es la propiedad que permite multiplicar la fuerza con áreas distintas."),
        ("=", "{F} ¿Cuántos N/cm² de presión genera la fuerza de entrada?", "100//4", "Se divide la fuerza entre el área del pistón de entrada.", " N/cm²"),
        ("=", "{F} ¿Cuántos N de fuerza entrega el pistón de salida?", "(100//4)*20", "Se multiplica la presión por el área del pistón de salida.", " N"),
        ("=", "{F} ¿Cuántas veces mayor es el área del pistón de salida que la del pistón de entrada?", "20//4", "Se divide el área de salida entre el área de entrada.", " veces"),
        ("abc", "{F} Un compañero dice: «el pistón de salida entrega más fuerza, así que el sistema crea energía». ¿Qué respuesta es correcta?", "Es falso: la fuerza aumenta pero el recorrido del pistón de salida disminuye en la misma proporción, y no se crea energía", "Es cierto: el sistema multiplica también la energía", "Es falso: la fuerza de salida es igual a la de entrada", "El circuito intercambia fuerza por recorrido y no genera energía."),
        ("abc", "Si entra aire a un circuito diseñado para líquido, el accionamiento se siente esponjoso. ¿Por qué?", "Porque el aire se comprime y absorbe parte del movimiento en vez de transmitir la fuerza", "Porque el aire pesa más que el líquido", "Porque el aire aumenta la presión del circuito", "El aire es compresible, por eso el movimiento se pierde en comprimirlo."),
        ("=", "Un circuito de ejemplo tiene un pistón de entrada de 5 cm² que recibe 150 N y un pistón de salida de 25 cm². ¿Cuántos N entrega el pistón de salida?", "(150//5)*25", "Se calcula la presión y se multiplica por el área de salida.", " N"),
        ("=", "{F} Si la fuerza de entrada sube a 140 N con las mismas áreas, ¿cuántos N más que antes entrega el pistón de salida?", "(140//4)*20-(100//4)*20", "Se calcula la fuerza de salida con 140 N y con 100 N, y se restan.", " N"),
    ],
    ctx=("abc", "Una persona te muestra una ficha de ejemplo con «fuerza 200 N, área 10 cm²» y te pregunta cuál es la presión. ¿Qué respondes?", "20 N/cm², porque 200 dividido entre 10 es 20", "2.000 N/cm²", "190 N/cm²", "La presión se obtiene dividiendo la fuerza entre el área."),
    sc=[
        ("En Mecánica Automotriz: ¿qué se multiplica en un circuito hidráulico con áreas distintas?", "La fuerza", "La energía no se crea; se multiplica la fuerza a costa del recorrido."),
        ("¿Qué componente permite o corta el paso del fluido?", "La válvula", "Su función es regular el paso del fluido."),
        ("¿Qué pasa si entra aire a un circuito de líquido?", "El accionamiento se siente esponjoso", "El aire se comprime y absorbe movimiento."),
    ],
    op=("Ficha de ejemplo: un circuito tiene un pistón de entrada de 2 cm² que recibe 40 N y un pistón de salida de 12 cm². Escribe (a) la presión, (b) la fuerza que entrega el pistón de salida, (c) cuántas veces mayor es el área de salida, (d) por qué el circuito no crea energía.",
        "(a) 40 ÷ 2 = 20 N/cm². (b) 20 × 12 = 240 N. (c) 12 ÷ 2 = 6 veces. (d) Porque el pistón de salida recorre 6 veces menos distancia: se multiplica la fuerza, no la energía.",
        ["calcula la presión", "calcula la fuerza de salida", "calcula la razón de áreas", "explica por qué no se crea energía"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar en lugar de dividir", "olvidar la unidad", "decir que se crea energía"],
        "Pregunta: «¿divido o multiplico la fuerza por el área para la presión?». Si duda, pídele que relea la definición de presión."),
    reinforce="Inventa un circuito con dos pistones y calcula la presión y la fuerza de salida.",
    extend="Explica con un ejemplo por qué el pistón de salida con más fuerza recorre menos distancia.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Vehículo liviano «Modelo Demo 10». Quejas: (1) «el volante se siente muy pesado al girar»; (2) «el pedal del freno se hunde más de lo normal y se siente esponjoso»; (3) «golpeteo al pasar por baches». "
     "Tabla de orientación del manual de ejemplo: volante pesado, dirección asistida (nivel de fluido, bomba); pedal esponjoso, circuito de frenos (aire o fluido insuficiente, fuga); golpeteo en baches, suspensión (amortiguadores, bujes). "
     "Registro de personal autorizado: queja 1, nivel de fluido de dirección 1 L (mínimo de ejemplo: 2 L); queja 2, espesor de pastillas 6 mm (mínimo de ejemplo: 3 mm) y nivel de fluido de frenos bajo el mínimo; queja 3, amortiguador delantero izquierdo con fuga visible de aceite.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso con quejas de suspensión, dirección y frenos, a priorizar por seguridad y a redactar un informe prudente que no oculte fugas.",
    prior=["Sé usar una tabla de orientación.", "Sé comparar un dato con un mínimo.", "Sé qué es un sistema de seguridad."],
    explain=[
        "Cuando un vehículo llega con varias quejas, cada una se relaciona con su sistema candidato usando la tabla de orientación y después se mira el registro de datos. Se prioriza lo que afecta a la seguridad, como los frenos y la dirección. Un amortiguador es un componente de la suspensión que controla el rebote de los resortes usando un fluido; una fuga visible en él apunta a la suspensión.",
        "En un sistema cerrado de fluido, un nivel bajo suele indicar una fuga u otra causa, no solo «falta de fluido». Reponer fluido sin investigar oculta la fuga y deja un sistema de seguridad sin verificar. Un dato que cumple, como el espesor de las pastillas, no descarta otra falla en el mismo sistema. Ante duda en frenos o dirección, el vehículo no se entrega hasta que lo verifique personal autorizado.",
        f"Esta clase interpreta informes escritos; no enseña a intervenir frenos ni dirección. {EMER} {AVISO}",
    ],
    vocab=[("amortiguador", "componente de la suspensión que controla el rebote de los resortes"), ("pastilla de freno", "pieza que roza para frenar y se desgasta"), ("espesor mínimo", "grosor por debajo del cual la pieza se informa para reemplazo"), ("fuga", "salida de fluido de un sistema cerrado"), ("prioridad de seguridad", "orden que atiende primero lo que puede causar un accidente")],
    worked=[
        ("Prioridad de seguridad", "Un vehículo de ejemplo llega con dos quejas: una luz interior que parpadea y una pérdida de fluido en la dirección. ¿Cuál se atiende primero?", ["La dirección es un sistema de seguridad.", "Una falla en la dirección puede causar un accidente."], "La pérdida de fluido en la dirección"),
        ("Comparar con el mínimo", "El espesor mínimo de un disco de freno de ejemplo es 20 mm y se registra 19 mm. ¿Cuántos mm faltan y cumple?", ["Se resta el registro al mínimo: 20 menos 19 es 1.", "Está bajo el mínimo: no cumple."], "Faltan 1 mm; no cumple"),
    ],
    mistakes=[("Reponer fluido en un sistema cerrado y dar el problema por resuelto.", "El nivel bajo puede indicar una fuga que sigue ahí.", "Informa el nivel bajo y deja que personal autorizado busque la causa."),
              ("Descartar un problema del sistema porque un dato cumple.", "Un dato conforme no cubre las otras posibles fallas.", "Evalúa cada hallazgo por separado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿por qué un nivel de fluido bajo en un sistema cerrado debe investigarse?", "Porque puede indicar una fuga u otra causa que reponer fluido no corrige", "Porque el fluido siempre se evapora", "Porque el nivel bajo es normal en vehículos antiguos", "En un sistema cerrado el fluido no debería perderse sin una causa."),
        ("abc", "En Mecánica Automotriz: ¿qué se prioriza cuando un vehículo llega con quejas de distintos sistemas?", "Los sistemas de seguridad, como frenos y dirección", "Los trabajos de menor costo", "Los trabajos que toman menos horas", "La seguridad va primero; el costo y la duración no definen la prioridad."),
        ("abc", "En Mecánica Automotriz: ¿qué es un amortiguador?", "Un componente de la suspensión que controla el rebote de los resortes con un fluido", "Un componente del freno que detiene el vehículo", "Una pieza que dosifica el combustible", "El amortiguador pertenece a la suspensión."),
        ("abc", "{F} ¿Qué sistema orienta la queja 1 según la tabla del manual?", "La dirección asistida", "El circuito de frenos", "La suspensión", "La tabla asocia el volante pesado con la dirección asistida."),
        ("abc", "{F} ¿Qué dato del registro de la queja 3 apunta a la suspensión?", "La fuga visible de aceite en el amortiguador delantero izquierdo", "El nivel de fluido de la dirección", "El espesor de las pastillas", "El amortiguador es un componente de la suspensión."),
        ("abc", "{F} ¿Qué hallazgo de la queja 2 cumple su mínimo?", "El espesor de las pastillas, 6 mm contra 3 mm", "El nivel de fluido de frenos", "Ninguno de los dos", "6 mm supera el mínimo de 3 mm; el fluido está bajo el mínimo."),
        ("=", "{F} ¿Cuántos L faltan en el fluido de dirección para llegar al mínimo?", "2-1", "Se resta el nivel registrado al mínimo.", " L"),
        ("=", "{F} ¿Cuántos mm sobre el mínimo está el espesor de las pastillas?", "6-3", "Se resta el mínimo al espesor registrado.", " mm"),
        ("=", "{F} Verificar cada queja toma 2 horas a $13.000 la hora. ¿Cuántos pesos cuesta verificar las tres quejas?", "3*2*13000", "Se multiplican las quejas, las horas de cada una y la tarifa.", " pesos"),
        ("abc", "{F} Un compañero dice: «las pastillas están bien, así que el pedal esponjoso no es problema». ¿Qué respuesta es correcta?", "Es falso: el espesor cumple, pero el nivel bajo de fluido de frenos y el pedal esponjoso exigen verificación por tratarse de un sistema de seguridad", "Es cierto, porque el pedal depende solo de las pastillas", "Es cierto, porque un nivel bajo de fluido es normal", "Un dato conforme no descarta otra falla en el mismo sistema."),
        ("abc", "Un técnico propone reponer fluido de frenos y entregar el vehículo sin buscar la causa. ¿Qué observación es correcta?", "No corresponde: reponer sin investigar oculta una posible fuga y deja un sistema de seguridad sin verificar", "Corresponde, porque el nivel es lo único que importa", "Corresponde, si la persona propietaria está de acuerdo", "Un nivel bajo señala una posible fuga que reponer no corrige."),
        ("=", "{F} Si el espesor de las pastillas baja 1 mm cada 10.000 km, ¿cuántos km faltan para llegar al mínimo?", "(6-3)*10000", "Se calculan los mm que faltan y se multiplican por los km de cada mm.", " km"),
        ("abc", "{F} ¿Qué informe corresponde para la queja 2?", "Pedal esponjoso con nivel de fluido de frenos bajo el mínimo y pastillas conformes: no se entrega el vehículo y se deriva a verificación autorizada", "Pastillas conformes: el vehículo se entrega", "Falla del cilindro maestro, que debe cambiarse", "El informe cita los hallazgos, no afirma una pieza y detiene la entrega de un sistema de seguridad."),
    ],
    ctx=("abc", "Una persona propietaria te cuenta que le repone fluido de frenos a su vehículo cada mes «y listo». ¿Qué respondes?", "Que perder fluido en un sistema cerrado indica una posible fuga y debe evaluarlo personal autorizado en un taller", "Que está bien, así se mantiene el nivel", "Que es normal que los frenos gasten fluido cada mes", "Un sistema cerrado no debería perder fluido sin una causa."),
    sc=[
        ("En Mecánica Automotriz: ¿qué sistemas se priorizan en un taller?", "Los de seguridad, como frenos y dirección", "Su falla puede causar un accidente."),
        ("¿Qué indica un nivel bajo de fluido en un sistema cerrado?", "Una posible fuga", "El fluido no se consume en un circuito cerrado."),
        ("¿Un dato que cumple descarta otras fallas del sistema?", "No", "Cada hallazgo se evalúa por separado."),
    ],
    op=("Ficha de ejemplo: queja escrita: «ruido metálico al girar el volante». Tabla del manual de ejemplo: ruido al girar el volante, dirección (rótulas, fluido de dirección). Registro de personal autorizado: nivel de fluido de dirección, 3 L (rango de ejemplo: 2 a 3 L); juego de una rótula, 4 mm (máximo de ejemplo: 2 mm). Escribe (a) el sistema candidato, (b) qué hallazgo cumple y cuál no, (c) cuánto se aparta el que no cumple, (d) una conclusión prudente.",
        "(a) La dirección. (b) El nivel de fluido cumple (3 L está en el rango); el juego de la rótula no cumple. (c) 4 − 2 = 2 mm sobre el máximo. (d) La rótula queda fuera de especificación y, por ser un sistema de seguridad, el vehículo no se entrega hasta que personal autorizado lo verifique.",
        ["nombra el sistema", "clasifica cada hallazgo", "calcula la diferencia", "redacta una conclusión prudente"],
        ["hoja con las cuatro respuestas"],
        ["afirmar que el fluido es la causa", "calcular mal la diferencia", "entregar el vehículo"],
        "Pregunta: «¿cada hallazgo cumple su propio límite?». Si duda, pídele que relea cómo se evalúa cada hallazgo."),
    reinforce="Inventa dos quejas de un vehículo y decide cuál se atiende primero y por qué.",
    extend="Explica con un ejemplo por qué un nivel de fluido bajo puede ser el síntoma y no la causa.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (caja de cambios de ejemplo, inventada, descrita por escrito). Caja manual de 3 marchas. En cada marcha un engranaje motriz, en el eje de entrada, mueve un engranaje conducido, en el eje de salida. "
     "Marcha 1: motriz de 15 dientes, conducido de 45 dientes. Marcha 2: motriz de 20 dientes, conducido de 40 dientes. Marcha 3: motriz de 30 dientes, conducido de 30 dientes. El eje de entrada gira a 3.000 revoluciones por minuto (rpm) y entrega un par de 50 N·m (valores de ejemplo).")
build(
    O5, 4, F,
    use="Aprenderé a calcular la relación de transmisión de un par de engranajes, las rpm y el par de salida, y qué hace el embrague y el fluido de una transmisión automática.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es un engranaje.", "Sé que una caja de cambios tiene marchas."],
    explain=[
        "La relación de transmisión de un par de engranajes es el número de dientes del conducido dividido por el número de dientes del motriz. Las rpm de salida son las rpm de entrada divididas por la relación, y el par de salida ideal es el par de entrada multiplicado por la relación. Si la relación es mayor que 1, el eje de salida gira más lento y entrega más par; si el conducido tiene la mitad de dientes que el motriz, la salida gira al doble de rpm y entrega la mitad del par.",
        "Estos cálculos son ideales: en una caja real hay pérdidas de par por roce y otras causas. En una caja manual, el embrague acopla y desacopla la potencia entre el motor y la caja. La transmisión automática usa un convertidor de par y un circuito hidráulico de fluido: el fluido lubrica, retira calor y transmite la presión que acciona los cambios. Las unidades son rpm para el giro y newton metro (N·m) para el par.",
        f"Esta clase calcula en papel; abrir o reparar una caja es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("relación de transmisión", "dientes del conducido divididos por dientes del motriz"), ("rpm", "revoluciones por minuto, medida del giro"), ("par", "capacidad de girar, en newton metro (N·m)"), ("embrague", "componente que acopla y desacopla el motor y la caja manual"), ("convertidor de par", "componente de la caja automática que transmite la potencia con fluido")],
    worked=[
        ("Relación de transmisión", "Un engranaje motriz de 10 dientes mueve a uno conducido de 30 dientes. ¿Cuál es la relación?", ["Se divide los dientes del conducido entre los del motriz.", "30 entre 10 son 3."], "Relación 3"),
        ("rpm de salida", "Un eje de entrada gira a 2.400 rpm y la relación es 4. ¿Cuántas rpm tiene el eje de salida?", ["Las rpm de salida son las de entrada divididas por la relación.", "2.400 entre 4 son 600."], "600 rpm"),
    ],
    mistakes=[("Dividir los dientes del motriz entre los del conducido para la relación.", "La relación es conducido entre motriz.", "Pon arriba el conducido y abajo el motriz."),
              ("Creer que una marcha que gira más rápido también entrega más par.", "Giro y par cambian en sentido contrario.", "A más giro de salida, menos par.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula la relación de transmisión de un par de engranajes?", "Dividiendo los dientes del conducido entre los del motriz", "Sumando los dientes de ambos engranajes", "Dividiendo los dientes del motriz entre los del conducido", "La relación es conducido dividido por motriz."),
        ("abc", "En Mecánica Automotriz: ¿qué ocurre con el giro y el par de salida cuando la relación es mayor que 1?", "El giro de salida baja y el par de salida sube", "El giro de salida sube y el par baja", "Ambos bajan", "Con relación mayor que 1 la salida gira más lento y entrega más par."),
        ("abc", "En Mecánica Automotriz: ¿qué función cumple el embrague en una caja manual?", "Acoplar y desacoplar la potencia entre el motor y la caja", "Almacenar el fluido de la transmisión", "Enfriar el aceite de la caja", "El embrague conecta o separa el motor de la caja."),
        ("abc", "{F} ¿En qué marcha el engranaje conducido tiene el doble de dientes que el motriz?", "En la marcha 2", "En la marcha 1", "En la marcha 3", "Marcha 2: 40 es el doble de 20; marcha 1: 45 es el triple de 15; marcha 3: son iguales."),
        ("abc", "{F} ¿Qué marcha entrega el mayor par de salida?", "La marcha 1", "La marcha 2", "La marcha 3", "La marcha 1 tiene la mayor relación, 3, y por eso el mayor par."),
        ("abc", "{F} ¿Qué diferencia tiene una caja real con el cálculo ideal?", "Pierde parte del par por roce y otras causas", "Pierde todo el giro del eje de entrada", "No pierde nada, porque los cálculos ideales son exactos", "El cálculo ideal no considera pérdidas, que existen en una caja real."),
        ("=", "{F} ¿Cuál es la relación de transmisión de la marcha 1?", "45//15", "Se dividen los dientes del conducido entre los del motriz.", ""),
        ("=", "{F} ¿Cuántas rpm tiene el eje de salida en la marcha 2?", "3000//(40//20)", "Se divide la entrada entre la relación de la marcha 2.", " rpm"),
        ("=", "{F} ¿Cuántos N·m de par ideal entrega la marcha 1?", "50*(45//15)", "Se multiplica el par de entrada por la relación.", " N·m"),
        ("abc", "{F} Un compañero dice: «la marcha 3 entrega más par que la marcha 1 porque el eje gira más rápido». ¿Qué respuesta es correcta?", "Es falso: la marcha 3 gira más rápido pero entrega menos par, 50 N·m contra 150 N·m", "Es cierto: a mayor giro siempre hay mayor par", "Es falso: las dos entregan el mismo par", "El giro y el par cambian en sentido contrario."),
        ("abc", "Una persona dice que el fluido de una transmisión automática «solo sirve para lubricar». ¿Qué respuesta es correcta?", "Es incompleto: además de lubricar, transmite la presión que acciona los cambios y ayuda a retirar calor", "Es correcto: el fluido solo lubrica", "Es falso: el fluido solo sirve para accionar los cambios", "El fluido cumple varias funciones en la transmisión automática."),
        ("=", "Una marcha de ejemplo tiene un motriz de 12 dientes y un conducido de 48 dientes. El eje de entrada gira a 2.400 rpm. ¿Cuántas rpm tiene el eje de salida?", "2400//(48//12)", "Se calcula la relación y se divide la entrada entre ella.", " rpm"),
        ("abc", "{F} Se agrega una marcha 4 con motriz de 40 dientes y conducido de 20 dientes. ¿Qué entrega esa marcha con la misma entrada?", "6.000 rpm de salida y 25 N·m de par ideal", "1.500 rpm de salida y 100 N·m de par ideal", "3.000 rpm de salida y 50 N·m de par ideal", "El conducido tiene la mitad de dientes: la salida gira al doble y entrega la mitad del par."),
    ],
    ctx=("abc", "Una persona te pregunta por qué una caja de cambios necesita varias marchas. ¿Qué respondes?", "Porque cada relación cambia el giro y el par de salida, y así el motor puede trabajar útilmente en distintas condiciones", "Porque cada marcha tiene un motor distinto", "Porque así el vehículo gasta menos fluido", "Las marchas ofrecen relaciones distintas entre giro y par."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calculan las rpm de salida?", "Dividiendo las rpm de entrada entre la relación", "Una relación mayor reduce el giro."),
        ("¿Cómo se calcula el par ideal de salida?", "Multiplicando el par de entrada por la relación", "Una relación mayor aumenta el par."),
        ("¿Qué hace el embrague?", "Acopla y desacopla el motor y la caja", "Así se separa o une la potencia."),
    ],
    op=("Ficha de ejemplo: una caja tiene la marcha A con motriz de 10 dientes y conducido de 40, y la marcha B con motriz de 20 dientes y conducido de 40. El eje de entrada gira a 2.000 rpm y entrega 30 N·m. Escribe (a) la relación de cada marcha, (b) las rpm de salida de cada una, (c) el par ideal de cada una, (d) qué pierde una caja real respecto de estos cálculos.",
        "(a) A: 40 ÷ 10 = 4; B: 40 ÷ 20 = 2. (b) A: 2.000 ÷ 4 = 500 rpm; B: 2.000 ÷ 2 = 1.000 rpm. (c) A: 30 × 4 = 120 N·m; B: 30 × 2 = 60 N·m. (d) Parte del par, por roce y otras pérdidas.",
        ["calcula las relaciones", "calcula las rpm de salida", "calcula el par ideal", "menciona las pérdidas"],
        ["hoja con las cuatro respuestas"],
        ["invertir la división de la relación", "multiplicar las rpm por la relación", "olvidar las pérdidas"],
        "Pregunta: «¿qué engranaje va arriba en la división?». Si duda, pídele que relea cómo se calcula la relación."),
    reinforce="Inventa una marcha con los dientes de dos engranajes, las rpm de entrada y el par de entrada, y calcula las rpm y el par de salida.",
    extend="Explica con un ejemplo por qué una marcha con más par gira más lento.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (alternativas y control de seguridad de ejemplo, inventados). Un vehículo liviano con una fuga en la dirección asistida admite dos alternativas. Alternativa A: reemplazar solo el componente con fuga; repuesto $60.000, mano de obra 3 horas, garantía 6 meses. "
     "Alternativa B: reemplazar el conjunto de dirección; repuesto $150.000, mano de obra 5 horas, garantía 12 meses. Tarifa: $12.000 por hora. Control de seguridad de ejemplo (todo debe cumplir): 1, repuesto con la referencia del manual; 2, nivel de fluido entre 2 y 3 L; 3, sin fugas visibles; 4, verificación registrada por personal autorizado; 5, firma de control de calidad. "
     "Estado: puntos 1, 2, 3 y 4 cumplidos; el 5, pendiente.")
build(
    O5, 5, F,
    use="Aprenderé a comparar alternativas de reparación de un sistema de seguridad por costo y garantía, y a verificar la calidad con un control de seguridad completo, la referencia del repuesto y la gestión de residuos.",
    prior=["Sé calcular costo con horas y tarifa.", "Sé calcular costo por mes de garantía.", "Sé qué es un sistema de seguridad."],
    explain=[
        "En un sistema de seguridad el repuesto debe tener la referencia exacta que indica el manual: uno «parecido» puede no resistir las presiones y las condiciones del sistema. Para comparar alternativas se calcula el costo total (repuesto más horas por tarifa) y el costo por mes de garantía, y además se consideran la recomendación técnica del fabricante y la necesidad real del vehículo. Una garantía más larga no decide por sí sola.",
        "El control de seguridad verifica por escrito cada punto: referencia del repuesto, niveles dentro del rango, ausencia de fugas, verificación registrada y firma de control de calidad, que es una verificación independiente. Si un punto está pendiente, el vehículo no se entrega, aunque la persona propietaria tenga apuro o ofrezca firmar que se hace responsable. El fluido usado y las piezas retiradas son residuos que se clasifican y se entregan a un gestor autorizado, con registro.",
        f"Esta clase compara cifras y documentos; los trabajos reales los hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("referencia del repuesto", "código exacto que identifica la pieza correcta en el manual"), ("control de seguridad", "lista de puntos que deben cumplirse antes de entregar"), ("control de calidad", "verificación independiente y registrada"), ("gestor autorizado", "empresa autorizada para retirar y tratar residuos"), ("costo por mes de garantía", "costo total dividido por los meses de garantía")],
    worked=[
        ("Costo por mes de garantía", "Una alternativa de ejemplo cuesta $120.000 en total y tiene 8 meses de garantía. ¿Cuánto cuesta por mes?", ["Se divide el costo total entre los meses.", "120.000 entre 8 son 15.000."], "$15.000 por mes"),
        ("Nivel dentro del rango", "El rango de ejemplo de un nivel es de 5 a 6 L y el registro dice 6 L. ¿Cumple?", ["El límite superior se incluye en lo conforme.", "6 está dentro del rango."], "Sí, cumple"),
    ],
    mistakes=[("Usar un repuesto «parecido» porque es más barato.", "En un sistema de seguridad la referencia exacta importa.", "Usa la referencia del manual y registra su trazabilidad."),
              ("Mezclar el fluido usado con el aceite del motor «para ahorrar espacio».", "Mezclar residuos dificulta su gestión y puede aumentar el riesgo.", "Clasifica cada residuo y entrégalo a un gestor autorizado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿por qué en un sistema de seguridad se usa un repuesto con la referencia exacta del manual?", "Porque uno «parecido» puede no resistir las presiones y condiciones del sistema", "Porque la referencia hace más barato el repuesto", "Porque la referencia solo importa para la garantía", "La referencia garantiza que la pieza corresponde al diseño del sistema."),
        ("abc", "En Mecánica Automotriz: ¿qué es el control de calidad en un trabajo sobre un sistema de seguridad?", "Una verificación independiente y registrada de que el trabajo cumple lo exigido", "Una nueva ronda del mismo técnico sin registrar", "Una encuesta de satisfacción a la persona propietaria", "El control de calidad lo hace otra persona y deja constancia escrita."),
        ("abc", "En Mecánica Automotriz: ¿qué se hace con el fluido usado y las piezas retiradas?", "Se clasifican y se entregan a un gestor autorizado, con registro", "Se mezclan con el aceite del motor para ahorrar espacio", "Se vierten en el desagüe del taller", "Los residuos requieren clasificación y un gestor autorizado; mezclarlos o verterlos es una mala práctica."),
        ("abc", "{F} ¿Se puede entregar el vehículo con ese estado del control?", "No, porque el punto 5 está pendiente", "Sí, porque cuatro de cinco puntos están cumplidos", "Sí, si la persona propietaria firma que se hace responsable", "Todos los puntos deben cumplirse y una firma de responsabilidad no reemplaza la verificación."),
        ("abc", "{F} ¿Por qué se exige la firma de control de calidad del punto 5?", "Para que una segunda persona verifique el sistema de seguridad antes de entregarlo", "Para que el taller cobre una tarifa adicional", "Para que la persona propietaria apruebe el precio", "La firma deja constancia de una verificación independiente."),
        ("abc", "{F} ¿Qué rango de nivel de fluido exige el punto 2?", "Entre 2 y 3 L", "Menos de 2 L", "Más de 3 L", "El control pide un nivel dentro del rango de 2 a 3 L."),
        ("=", "{F} ¿Cuántos pesos cuesta en total la alternativa A?", "60000+3*12000", "Se suma el repuesto con las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta en total la alternativa B?", "150000+5*12000", "Se suma el repuesto con las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta por mes de garantía la alternativa A?", "(60000+3*12000)//6", "Se divide el costo total de A entre sus 6 meses.", " pesos"),
        ("abc", "{F} ¿Qué alternativa tiene menor costo por mes de garantía?", "La A, con 16.000 pesos por mes frente a 17.500 de la B", "La B, porque su garantía es más larga", "Ambas cuestan lo mismo por mes", "A cuesta 96.000 entre 6 meses y B cuesta 210.000 entre 12 meses."),
        ("abc", "{F} Un compañero dice: «elijo B porque tiene garantía más larga». ¿Qué observación es correcta?", "La garantía es solo un criterio: también cuentan el costo por mes, la necesidad real del vehículo y la recomendación técnica", "Es correcto: la garantía más larga siempre decide", "Es incorrecto: la garantía no importa", "Una decisión técnica combina varios criterios."),
        ("=", "{F} Por un convenio, el taller rebaja la tarifa de B a $9.000 la hora. ¿Cuántos pesos cuesta ahora B por mes de garantía?", "(150000+5*9000)//12", "Se recalcula el costo total de B y se divide entre 12.", " pesos"),
        ("abc", "{F} ¿Qué informe de cierre corresponde?", "Control de seguridad con cuatro puntos cumplidos y el punto 5 pendiente: no se entrega hasta completar la firma de control de calidad", "Control completado: se entrega el vehículo", "Cuatro de cinco puntos cumplidos: se entrega con aviso a la persona propietaria", "El informe indica el estado real y detiene la entrega mientras falte un punto."),
    ],
    ctx=("abc", "La persona propietaria te pide el vehículo ya, con el control de calidad pendiente, y ofrece firmar que se hace responsable. ¿Qué respondes?", "Que no corresponde: la verificación protege a todas las personas y no se reemplaza por una firma de responsabilidad", "Que sí, si firma una declaración", "Que sí, solo si es un cliente antiguo", "En un sistema de seguridad, un punto pendiente impide la entrega."),
    sc=[
        ("En Mecánica Automotriz: ¿qué debe tener un repuesto de un sistema de seguridad?", "La referencia exacta del manual", "Una pieza parecida puede no resistir las condiciones del sistema."),
        ("¿Cuándo se entrega un vehículo con control de seguridad?", "Cuando todos los puntos están cumplidos", "Un punto pendiente detiene la entrega."),
        ("¿A quién se entrega el fluido usado?", "A un gestor autorizado", "Es un residuo que requiere gestión autorizada."),
    ],
    op=("Ficha de ejemplo: alternativa X: reemplazar un componente, repuesto $80.000, 2 horas y garantía de 4 meses. Alternativa Y: reemplazar el conjunto, repuesto $140.000, 4 horas y garantía de 12 meses. Tarifa: $10.000 por hora. Control de ejemplo: nivel de fluido entre 4 y 5 L; resultado registrado, 3 L. Escribe (a) el costo total de cada alternativa, (b) el costo por mes de garantía de cada una, (c) si el nivel cumple, (d) qué haces si no cumple.",
        "(a) X: 80.000 + 2 × 10.000 = 100.000; Y: 140.000 + 4 × 10.000 = 180.000. (b) X: 100.000 ÷ 4 = 25.000; Y: 180.000 ÷ 12 = 15.000. (c) No cumple, porque 3 L está bajo el mínimo de 4 L. (d) No se entrega el vehículo, se informa a la jefatura, se deriva a verificación autorizada y no se modifica el registro.",
        ["calcula los costos totales", "calcula el costo por mes", "evalúa el nivel", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["elegir solo por el costo total", "aprobar el nivel fuera de rango", "entregar el vehículo"],
        "Pregunta: «¿3 L está dentro del rango de 4 a 5 L?». Si duda, pídele que relea cómo se evalúa un rango."),
    reinforce="Inventa dos alternativas con repuesto, horas y garantía, y calcula cuál tiene menor costo por mes.",
    extend="Explica con un ejemplo por qué una garantía firmada por la persona propietaria no reemplaza un control de seguridad.",
)

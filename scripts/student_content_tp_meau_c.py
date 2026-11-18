"""Mecánica Automotriz TP (3.º y 4.º medio) módulo C: OAE-06 (sistemas eléctricos y electrónicos: carga, arranque, encendido, alumbrado y cierre centralizado), OAE-07 (sistemas de seguridad y confortabilidad) y OAE-08 (residuos y desechos del mantenimiento). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meau_common import AVISO, EMER, build

O6 = "TP-MEAU-3y4-OAE-06"
O7 = "TP-MEAU-3y4-OAE-07"
O8 = "TP-MEAU-3y4-OAE-08"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller «Electro Auto Demo» trabaja con los sistemas de carga, arranque, encendido, alumbrado y señalización, y cierre centralizado. "
     "Su matriz de peligros anota: batería de 12 V, cortocircuito en cables, gases de la batería, chispas, componentes sensibles a descargas estáticas y, en vehículos eléctricos e híbridos, alto voltaje. Dotación del turno: 12 personas; el taller tiene 4 puestos.")
build(
    O6, 1, F,
    use="Aprenderé qué sistemas eléctricos tiene un vehículo, qué peligros tiene trabajar con ellos y por qué solo personal autorizado interviene los circuitos.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé multiplicar y dividir números enteros.", "Sé que un vehículo tiene batería y luces."],
    explain=[
        "El sistema eléctrico de un vehículo reúne la batería, que almacena energía; el sistema de carga, con el alternador, que genera energía con el motor funcionando y recarga la batería; el sistema de arranque, que hace girar el motor al partir; el sistema de encendido, que produce la chispa en un motor a gasolina; el alumbrado y la señalización, y el cierre centralizado, que bloquea y desbloquea todas las puertas con una sola orden.",
        "Los peligros son un cortocircuito, que es un paso de mucha corriente por un camino no previsto y calienta cables hasta causar quemaduras o incendio; los gases de la batería, que pueden ser inflamables y no se acercan a llamas ni chispas; el ácido de la batería, que quema; las descargas estáticas, que dañan módulos electrónicos; y el alto voltaje de los vehículos eléctricos e híbridos, que puede ser mortal y exige formación y autorización específicas.",
        f"La Superintendencia de Electricidad y Combustibles (SEC) fiscaliza instalaciones eléctricas según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("batería", "componente que almacena energía eléctrica"), ("alternador", "componente que genera energía con el motor funcionando"), ("cortocircuito", "paso de mucha corriente por un camino no previsto"), ("cierre centralizado", "sistema que bloquea y desbloquea todas las puertas con una orden"), ("descarga estática", "chispa de electricidad acumulada que daña componentes electrónicos"), ("alto voltaje", "tensión mucho mayor que la de una batería común")],
    worked=[
        ("Peligro y riesgo", "Un cable de ejemplo con el aislante roto roza una pieza metálica. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cable con el aislante roto.", "El riesgo es un cortocircuito que caliente el cable y cause un incendio."], "Peligro: el cable con aislante roto; riesgo: cortocircuito, calor o incendio"),
        ("Nivel de control", "Un taller de ejemplo entrega a cada persona gafas de seguridad para protegerse de las chispas. ¿En qué nivel de la jerarquía de controles está esa medida?", ["Unas gafas protegen solo a quien las usa y no quitan el peligro.", "Eso es equipo de protección personal, el último nivel."], "En el EPP, el último nivel"),
    ],
    mistakes=[("Creer que una batería de 12 V es inofensiva por ser de baja tensión.", "Un cortocircuito puede calentar cables y la batería libera gases y ácido.", "Trata toda batería como un peligro y deja la intervención a personal autorizado."),
              ("Pensar que un vehículo híbrido es «igual» a uno común en lo eléctrico.", "Su alto voltaje exige formación específica.", "Solo personal con autorización específica interviene el alto voltaje.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es un cortocircuito?", "Un paso de mucha corriente por un camino no previsto, que calienta los cables", "Un apagado normal del circuito con un interruptor", "Una caída de tensión por no usar el vehículo", "El cortocircuito es un camino no previsto con mucha corriente; apagar con un interruptor es normal."),
        ("abc", "En Mecánica Automotriz: ¿qué función cumple la batería del vehículo?", "Almacenar energía eléctrica y entregarla, por ejemplo al arrancar", "Generar energía mientras el motor funciona", "Enfriar los cables del circuito", "La batería almacena energía; quien genera con el motor funcionando es el alternador."),
        ("abc", "En Mecánica Automotriz: ¿qué función cumple el alternador?", "Generar energía eléctrica con el motor funcionando y recargar la batería", "Hacer girar el motor para arrancarlo", "Producir la chispa de las bujías", "El alternador genera y recarga; el arranque y la chispa son de otros sistemas."),
        ("abc", "{F} ¿Qué peligro de la matriz puede causar un incendio por calentamiento de cables?", "El cortocircuito en cables", "Los componentes sensibles a descargas estáticas", "El alto voltaje de un híbrido", "El cortocircuito calienta los cables; las descargas estáticas dañan módulos."),
        ("ab", "{F} ¿Qué regla corresponde a los gases de la batería?", "No acercar llamas ni chispas, porque pueden ser inflamables", "Guardar las baterías en un recinto cerrado sin ventilación", "Los gases inflamables se alejan de chispas y llamas; encerrarlos aumenta el peligro."),
        ("abc", "{F} ¿Qué peligro exige formación y autorización específicas en vehículos eléctricos e híbridos?", "El alto voltaje", "La batería de 12 V", "Los componentes sensibles a descargas estáticas", "El alto voltaje puede ser mortal; la batería de 12 V y las descargas estáticas son otros peligros."),
        ("=", "{F} ¿Cuántas personas hay por puesto de trabajo, repartidas en partes iguales?", "12//4", "Se divide la dotación entre el número de puestos.", " personas"),
        ("=", "{F} El peligro de cortocircuito tiene probabilidad 3 y gravedad 5; el de descarga estática, probabilidad 4 y gravedad 2. ¿Cuántos puntos más tiene el cortocircuito?", "3*5-4*2", "Se calculan los dos puntajes como probabilidad por gravedad y se restan.", " puntos"),
        ("=", "{F} El taller capacita a cada persona 1 hora cada 3 meses en riesgo eléctrico. ¿Cuántas horas de capacitación suma la dotación en 12 meses?", "12*(12//3)*1", "Se calculan las capacitaciones del año por persona y se multiplican por la dotación.", " horas"),
        ("abc", "{F} Un aprendiz dice: «la batería de 12 V es inofensiva porque es de baja tensión». ¿Qué respuesta es correcta?", "Es falso: aun con 12 V un cortocircuito puede calentar cables y causar incendio, y la batería libera gases y ácido", "Es cierto, porque 12 V no puede causar ningún daño", "Es cierto, si no se toca con las dos manos", "El peligro de la batería viene del cortocircuito, los gases y el ácido, no solo de la tensión."),
        ("abc", "El jefe de un taller de ejemplo pide a un aprendiz que «cambie rápido» un componente de alto voltaje de un híbrido porque «es igual a uno común». ¿Qué corresponde?", "Negarse y avisar a un adulto responsable, porque el alto voltaje exige formación y autorización específicas", "Hacerlo con guantes comunes", "Hacerlo si el vehículo está apagado", "Apagar el vehículo o usar guantes comunes no reemplaza la formación específica."),
        ("=", "{F} Cada hora de capacitación cuesta $4.000 por persona. ¿Cuántos pesos cuesta la capacitación de un año de toda la dotación?", "12*(12//3)*1*4000", "Se calculan las horas del año y se multiplican por el costo de cada hora.", " pesos"),
        ("abc", "En una visita a un taller de ejemplo, una persona recibe una descarga eléctrica y queda inmóvil junto a un equipo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Tomarla del brazo para apartarla", "Tocar el equipo para apagarlo", "Tocar a la persona o al equipo puede hacerte parte del circuito; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "Un conocido te ofrece «un trabajito»: instalar luces extra en su vehículo con cables «que sobran». ¿Qué respondes?", "Que las modificaciones eléctricas deben respetar el manual y la norma vigente, con cables y fusibles adecuados, y las hace personal autorizado", "Que sí, si los cables son gruesos", "Que sí, si no se nota", "Las modificaciones eléctricas se hacen con componentes adecuados y personal autorizado."),
    sc=[
        ("En Mecánica Automotriz: ¿qué sistema genera energía con el motor funcionando?", "El sistema de carga, con el alternador", "El alternador genera energía y recarga la batería."),
        ("¿Qué institución fiscaliza instalaciones eléctricas?", "La SEC", "Esa superintendencia fiscaliza electricidad según la norma vigente."),
        ("¿Qué peligro exige formación específica en un híbrido?", "El alto voltaje", "Puede ser mortal y no se maneja sin autorización."),
    ],
    op=("El taller de ejemplo anota dos situaciones: una batería de 12 V sobre un carro con un borne sin cubierta, y cables sueltos dentro de un tablero de fusibles abierto. Escribe (a) el peligro y el riesgo de cada una, (b) un control de ingeniería, (c) un control administrativo, (d) quién interviene un circuito y por qué el EPP no basta. No describas cómo se interviene.",
        "(a) Batería: peligro, el borne sin cubierta; riesgo, un cortocircuito con chispa o quemadura. Tablero: peligro, los cables sueltos; riesgo, un cortocircuito que caliente los cables e incendie. (b) Una caja o tapa fija que cierre el tablero. (c) Una regla y una señal de que solo personal autorizado interviene los circuitos. (d) Personal autorizado; el EPP es la última barrera y no quita el peligro.",
        ["distingue peligro y riesgo", "propone un control de ingeniería", "propone un control administrativo", "explica por qué el EPP no basta y quién interviene"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a los cables sueltos", "proponer solo el EPP", "describir cómo se interviene el circuito"],
        "Pregunta: «¿qué medida impediría el contacto o el cortocircuito?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe los cinco sistemas eléctricos de la clase y una función de cada uno.",
    extend="Explica con un ejemplo por qué el alto voltaje de un híbrido exige reglas distintas a las de una batería de 12 V.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (datos eléctricos de ejemplo, inventados). Sistema de 12 V. Un faro de 60 W. Dos luces de posición de 6 W cada una. Un ventilador cuyo motor tiene una resistencia de 4 Ω. Fusibles disponibles: 5 A, 10 A, 15 A y 20 A. "
     "Relaciones de ejemplo: tensión (V) = corriente (A) × resistencia (Ω); potencia (W) = tensión (V) × corriente (A).")
build(
    O6, 2, F,
    use="Aprenderé a relacionar tensión, corriente, resistencia y potencia, a calcular la corriente de un circuito y a elegir el fusible adecuado, y qué hace cada sistema eléctrico del vehículo.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es una batería y un fusible.", "Sé leer un diagrama simple."],
    explain=[
        "La tensión se mide en volts (V), la corriente en amperes (A), la resistencia en ohms (Ω) y la potencia en watts (W). La corriente de un componente es la tensión dividida por su resistencia, y también la potencia dividida por la tensión. Cuando varias cargas se conectan directamente a la alimentación, sus corrientes se suman. Todos estos cálculos son en papel y con valores de ejemplo.",
        "El fusible adecuado es el menor valor disponible que supera la corriente normal del circuito, salvo que el manual indique otro. Un fusible igual a la corriente normal se abriría sin falla real; uno mucho mayor deja sin protección al cable y oculta la causa de un exceso de corriente. El sistema de carga recarga la batería, el de arranque hace girar el motor, el de encendido produce la chispa en un motor a gasolina, el alumbrado ilumina y señala, y el cierre centralizado bloquea las puertas con un módulo y actuadores.",
        f"Esta clase calcula en papel; intervenir un circuito real es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("tensión (V)", "volts, empuje que mueve la corriente"), ("corriente (A)", "amperes, cantidad de carga que circula"), ("resistencia (Ω)", "ohms, oposición al paso de la corriente"), ("potencia (W)", "watts, tensión por corriente"), ("sistema de encendido", "produce la chispa que enciende la mezcla en un motor a gasolina"), ("actuador", "componente que realiza un movimiento al recibir una orden")],
    worked=[
        ("Corriente por resistencia", "Un componente de ejemplo de 6 Ω se conecta a 12 V. ¿Cuántos A circulan?", ["La corriente es la tensión dividida por la resistencia.", "12 entre 6 son 2."], "2 A"),
        ("Elegir un fusible", "La corriente normal de un circuito de ejemplo es 7 A y hay fusibles de 5 A, 10 A y 15 A. ¿Cuál es el adecuado?", ["Debe superar los 7 A.", "El menor que los supera es el de 10 A."], "El fusible de 10 A"),
    ],
    mistakes=[("Elegir un fusible igual a la corriente normal.", "Se abriría sin una falla real porque no deja margen.", "Elige el menor valor que supera la corriente normal."),
              ("Subir el fusible para que «ya no se abra».", "Un fusible mayor deja sin protección al cable y oculta la causa.", "Si se abre seguido, informa a personal autorizado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula la corriente de un componente a partir de la tensión y su resistencia?", "Dividiendo la tensión entre la resistencia", "Multiplicando la tensión por la resistencia", "Restando la resistencia a la tensión", "La corriente es la tensión dividida por la resistencia."),
        ("abc", "En Mecánica Automotriz: ¿qué sistema produce la chispa que enciende la mezcla en un motor a gasolina?", "El sistema de encendido", "El sistema de carga", "El sistema de arranque", "El encendido produce la chispa; la carga recarga la batería y el arranque hace girar el motor."),
        ("abc", "En Mecánica Automotriz: ¿qué hace el cierre centralizado?", "Bloquea y desbloquea todas las puertas con una sola orden", "Enciende las luces interiores al abrir una puerta", "Aumenta la presión de los neumáticos", "El cierre centralizado actúa sobre las cerraduras; encender luces interiores es otra función."),
        ("abc", "{F} ¿Qué relación de la ficha permite calcular potencia?", "Potencia = tensión × corriente", "Potencia = tensión ÷ corriente", "Potencia = corriente ÷ resistencia", "La ficha define potencia como tensión por corriente."),
        ("=", "{F} ¿Cuántos W consume el motor del ventilador con 12 V, con la corriente que circula por él?", "12*(12//4)", "Primero se calcula la corriente con la resistencia y después se multiplica por la tensión.", " W"),
        ("abc", "{F} ¿Qué unidad mide la resistencia en la ficha?", "El ohm (Ω)", "El watt (W)", "El ampere (A)", "El ohm es la unidad de resistencia; el watt mide potencia y el ampere corriente."),
        ("=", "{F} ¿Cuántos A consume el faro?", "60//12", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "{F} ¿Cuántos A pasan por el motor del ventilador con 12 V?", "12//4", "La corriente es la tensión dividida por la resistencia.", " A"),
        ("=", "{F} ¿Cuántos A consumen en total el faro y las dos luces de posición, conectados directamente a la alimentación?", "(60+6+6)//12", "Se suman las potencias y se divide entre la tensión.", " A"),
        ("abc", "{F} El faro consume 5 A normales. ¿Cuál es el menor fusible de la ficha que supera esa corriente?", "El de 10 A", "El de 5 A, porque coincide con la corriente normal", "El de 20 A, porque deja más margen", "Un fusible igual a la corriente normal no deja margen y uno de 20 A protege mal."),
        ("abc", "Un compañero dice: «si el fusible se abre seguido, pongo uno de 20 A y se arregla». ¿Qué respuesta es correcta?", "Es falso: un fusible mayor deja sin protección al cable y oculta la causa; se informa a personal autorizado", "Es cierto: un fusible mayor siempre es más seguro", "Es cierto, si el cable es nuevo", "El fusible protege al cable y se abre por una causa que debe investigarse."),
        ("=", "{F} Se agrega un segundo faro de 60 W conectado directamente a la alimentación. ¿Cuántos A normales pasan en total por el fusible común de ambos faros?", "(60+60)//12", "Se suman las potencias de los dos faros y se divide entre la tensión.", " A"),
        ("abc", "{F} Con ese segundo faro, ¿qué fusible de la ficha es el adecuado para el circuito común?", "El de 15 A, el menor que supera 10 A", "El de 10 A, porque coincide con la corriente normal", "El de 20 A, el mayor disponible", "Los dos faros consumen 10 A y el menor fusible que supera esa corriente es el de 15 A."),
    ],
    ctx=("abc", "Una persona te cuenta que su vehículo con luces extra se descarga rápido. ¿Cómo lo explicas en papel?", "Cada luz extra suma corriente y potencia consumidas, por eso la carga total debe calcularse y respetar la capacidad del sistema", "Las luces extra generan energía para la batería", "La batería se desgasta solo con el tiempo, no por el consumo", "Cada carga agregada aumenta la corriente que debe entregar el sistema."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula la corriente de una lámpara de ejemplo?", "Dividiendo su potencia entre la tensión", "Potencia, tensión y corriente se relacionan en P = V × I."),
        ("¿Qué fusible se elige?", "El menor que supera la corriente normal", "Así deja margen y sigue protegiendo el cable."),
        ("¿Qué se hace si el fusible se abre seguido?", "Se informa a personal autorizado", "Se abre por una causa que debe investigarse."),
    ],
    op=("Ficha de ejemplo: sistema de 12 V; una luz de freno de 24 W; un ventilador con resistencia de 3 Ω; fusibles disponibles de 5 A, 10 A y 15 A. Escribe (a) la corriente de la luz, (b) la corriente del ventilador, (c) la corriente total si ambos están conectados directamente a la alimentación, (d) el fusible adecuado.",
        "(a) 24 ÷ 12 = 2 A. (b) 12 ÷ 3 = 4 A. (c) 2 + 4 = 6 A. (d) El de 10 A, el menor que supera 6 A.",
        ["calcula la corriente de la luz", "calcula la corriente del ventilador", "suma las corrientes", "elige el fusible"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "elegir un fusible igual a la corriente", "no sumar las corrientes"],
        "Pregunta: «¿qué dato uso para cada componente, potencia o resistencia?». Si duda, pídele que relea las dos formas de calcular la corriente."),
    reinforce="Inventa un circuito con dos cargas de potencia conocida a 12 V y calcula la corriente total y el fusible adecuado.",
    extend="Explica con un ejemplo por qué un fusible mayor no «arregla» un circuito.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado; los datos los registró personal autorizado). Vehículo «Modelo Demo 11». Queja escrita: «la luz de aviso de batería se enciende con el motor en marcha y, después de unos días, el vehículo no arranca». "
     "Especificaciones de ejemplo: tensión de la batería en reposo, mínimo 12 V; tensión con el motor en marcha (carga), de 13 a 15 V; corriente de carga, mínimo 20 A. Registro: tensión en reposo, 12 V; tensión con el motor en marcha, 12 V; corriente de carga, 0 A.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de carga y arranque: distinguir la causa de la consecuencia, comparar las lecturas con las especificaciones y escribir una conclusión prudente.",
    prior=["Sé qué es una especificación.", "Sé comparar números enteros con un rango.", "Sé qué hacen la batería y el alternador."],
    explain=[
        "Con el motor en marcha, el alternador debe entregar una tensión más alta que la de reposo, dentro de un rango, y una corriente de carga sobre un mínimo. Si la tensión en marcha es igual a la de reposo y la corriente de carga está bajo el mínimo, el sistema de carga no está entregando lo previsto. La luz de aviso de batería suele relacionarse con una carga fuera de lo esperado.",
        "Una batería descargada puede ser una consecuencia: si no se recarga, termina sin energía para arrancar. Cambiar solo la batería sin verificar el sistema de carga deja la falla de fondo y la batería nueva también se descargará. Cargar una batería es una tarea de personal autorizado y no corrige la causa. Un dato que cumple, como la tensión en reposo, no descarta otra falla.",
        f"Esta clase interpreta registros escritos; no enseña a medir ni a intervenir. {EMER} {AVISO}",
    ],
    vocab=[("sistema de carga", "alternador y componentes que recargan la batería"), ("consecuencia", "efecto que aparece por otra falla de fondo"), ("tensión de carga", "tensión con el motor en marcha, más alta que en reposo"), ("corriente de carga", "corriente que el alternador entrega a la batería"), ("capacidad en Ah", "amperes-hora que una batería puede entregar")],
    worked=[
        ("Hay carga o no", "Un registro de ejemplo da 12 V en reposo y 13 V en marcha, con un rango de 13 a 15 V. ¿Hay carga dentro de lo esperado?", ["13 V es el límite inferior del rango y los límites se incluyen.", "La tensión en marcha es más alta que en reposo."], "Sí, la carga cumple"),
        ("Causa y consecuencia", "Un vehículo de ejemplo no arranca porque su batería está descargada, y el alternador no está cargando. ¿Qué es la consecuencia?", ["El alternador sin cargar es la falla de fondo.", "La batería descargada es lo que resulta de esa falla."], "La batería descargada"),
    ],
    mistakes=[("Culpar a la batería de todo porque «no arranca».", "La batería puede estar descargada como consecuencia de otra falla.", "Compara también la carga con el motor en marcha."),
              ("Cambiar solo la batería y entregar el vehículo.", "Si el sistema de carga falla, la batería nueva también se descargará.", "Verifica la causa de fondo antes de reemplazar.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se reconoce en un registro que el sistema de carga entrega lo previsto?", "La tensión con el motor en marcha queda dentro del rango de carga y por sobre la de reposo", "La tensión con el motor en marcha es igual a la de reposo", "La tensión baja a cero con el motor en marcha", "Un sistema que carga eleva la tensión por sobre la de reposo y dentro de su rango."),
        ("abc", "En Mecánica Automotriz: ¿qué es una consecuencia en una falla?", "Un efecto que aparece por otra falla de fondo, como una batería descargada por falta de carga", "La causa original de la falla", "Un dato que no se debe registrar", "La consecuencia es lo que resulta de la falla de fondo."),
        ("abc", "En Mecánica Automotriz: ¿qué indica una corriente de carga bajo el mínimo especificado?", "Que el sistema de carga no entrega la corriente prevista y debe verificarse", "Que la batería está perfecta", "Que el motor de arranque funciona mejor", "Una corriente de carga bajo el mínimo es un hallazgo del sistema de carga."),
        ("abc", "{F} ¿Qué lectura de la ficha cumple su especificación?", "La tensión en reposo, 12 V", "La tensión con el motor en marcha, 12 V", "La corriente de carga, 0 A", "12 V en reposo iguala el mínimo; 12 V en marcha queda bajo 13 V y 0 A queda bajo 20 A."),
        ("abc", "{F} ¿Qué sistema queda como candidato principal?", "El sistema de carga", "El sistema de encendido", "El cierre centralizado", "Las lecturas con el motor en marcha apuntan a que no se recarga la batería."),
        ("abc", "{F} ¿Qué relación hay entre la luz de aviso de batería y el registro?", "La luz coincide con una carga fuera del rango esperado", "La luz indica que la batería está cargada al máximo", "No hay ninguna relación", "El registro muestra carga insuficiente, que es lo que suele avisar esa luz."),
        ("=", "{F} ¿Cuántos V faltan, con el motor en marcha, para llegar al mínimo del rango de carga?", "13-12", "Se resta la lectura al mínimo del rango.", " V"),
        ("=", "{F} ¿Cuántos A le faltan a la corriente de carga para llegar al mínimo?", "20-0", "Se resta la lectura al mínimo.", " A"),
        ("=", "Otro vehículo de ejemplo mide 16 V con el motor en marcha y el máximo del rango de carga es 15 V. ¿Cuántos V supera el máximo?", "16-15", "Se resta el máximo a la lectura.", " V"),
        ("abc", "{F} Un compañero dice: «la batería está mala porque el vehículo no arranca». ¿Qué respuesta es correcta?", "Es una conclusión apresurada: la batería en reposo cumple y el registro apunta a que no se recarga, así que puede estar descargada como consecuencia", "Es correcta, porque la batería es siempre la causa", "Es incorrecta, porque la batería no influye en el arranque", "La batería puede estar descargada por falta de carga; el dato en reposo no la acusa."),
        ("abc", "Un técnico cambia solo la batería y entrega el vehículo sin verificar el sistema de carga. ¿Qué problema tiene?", "Si el sistema de carga falla, la batería nueva también se descargará y la falla de fondo sigue", "Ninguno, porque una batería nueva resuelve todo", "Que la batería nueva no sirve para ese vehículo", "Sin verificar la causa de fondo la falla se repite."),
        ("=", "Una batería de ejemplo tiene 60 Ah de capacidad y una carga consume 5 A de forma continua. ¿Cuántas horas teóricas podría alimentar esa carga la batería? (capacidad ÷ consumo)", "60//5", "Se divide la capacidad entre el consumo.", " horas"),
        ("abc", "{F} Tras una verificación de personal autorizado, un nuevo registro con el motor en marcha da 14 V y 25 A. ¿Qué informe corresponde?", "El sistema de carga cumple: 14 V está en el rango de 13 a 15 V y 25 A supera el mínimo de 20 A", "No cumple, porque 14 V es mayor que la tensión en reposo", "No cumple, porque 25 A es mayor que 20 A", "Ambos valores están conformes con la especificación."),
    ],
    ctx=("abc", "Una persona propietaria te pide que «dejes la batería cargando toda la noche» como solución. ¿Qué respondes?", "Que cargarla no corrige la causa si el sistema de carga falla, y que la evaluación y la carga las hace personal autorizado", "Que sí, porque siempre resuelve el problema", "Que sí, si el garaje está cerrado", "Una carga solo repone energía; si la falla de fondo sigue, el problema vuelve."),
    sc=[
        ("En Mecánica Automotriz: ¿qué se compara con el motor en marcha?", "La tensión y la corriente de carga con sus rangos", "Así se sabe si el alternador entrega lo previsto."),
        ("¿Una batería descargada siempre es la causa?", "No, puede ser una consecuencia", "Puede descargarse por falta de carga."),
        ("¿Qué se hace antes de cambiar una batería?", "Se verifica el sistema de carga", "Si falla, la batería nueva también se descargará."),
    ],
    op=("Ficha de ejemplo: queja escrita: «el motor arranca lento por las mañanas». Especificaciones: tensión en reposo, mínimo 12 V; tensión durante el arranque, mínimo 10 V; tensión con el motor en marcha, de 13 a 15 V. Registro: reposo, 12 V; durante el arranque, 7 V; con el motor en marcha, 14 V. Escribe (a) qué lecturas cumplen, (b) cuál no cumple y cuánto se aparta, (c) qué sistema queda como candidato y cuál se ve conforme, (d) una conclusión prudente.",
        "(a) La de reposo y la de marcha. (b) La de arranque: 7 V, 3 V bajo el mínimo de 10 V. (c) Candidato: el suministro de energía durante el arranque (batería, conexiones o motor de arranque); el sistema de carga se ve conforme. (d) El dato señala el suministro de energía del arranque, pero no una pieza; la verificación la hace personal autorizado.",
        ["clasifica las lecturas", "calcula la diferencia", "distingue sistema candidato y sistema conforme", "redacta una conclusión prudente"],
        ["hoja con las cuatro respuestas"],
        ["decir que el alternador está mal", "afirmar una pieza dañada", "calcular mal la diferencia"],
        "Pregunta: «¿qué lectura es la única fuera de especificación?». Si duda, pídele que compare cada lectura con su propio mínimo."),
    reinforce="Inventa tres lecturas con sus especificaciones y marca cuáles cumplen.",
    extend="Explica con un ejemplo por qué una falla de carga puede aparecer primero como un problema de arranque.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (tabla de repuestos y cargas de ejemplo, inventada). Alumbrado y cierre centralizado, sistema de 12 V. Circuito de alumbrado trasero: 2 luces de freno de 24 W cada una y 2 luces de posición de 6 W cada una, conectadas directamente a la alimentación y protegidas por un fusible común de 10 A. "
     "Cierre centralizado: 4 actuadores de 24 W cada uno, protegidos por un fusible de 15 A. Repuestos de ejemplo: L-24, lámpara de 24 W; L-60, lámpara de 60 W; L-24-X, lámpara de 24 W con otra base. La ficha del vehículo exige la referencia L-24.")
build(
    O6, 4, F,
    use="Aprenderé a calcular la carga de un circuito, a medir el margen del fusible y a elegir el repuesto por su referencia exacta, sin cambiar la potencia por conveniencia.",
    prior=["Sé calcular la corriente con potencia y tensión.", "Sé elegir un fusible adecuado.", "Sé que una referencia identifica un repuesto."],
    explain=[
        "La carga de un circuito se calcula sumando las potencias de sus componentes, en watts, y dividiendo entre la tensión; el resultado es la corriente normal, en amperes. El margen del fusible es el valor del fusible menos la corriente normal. Un repuesto debe tener la referencia que exige el fabricante: una lámpara de mayor potencia aumenta el consumo y el calor del cableado aunque el fusible no se abra, y una de base distinta puede no calzar ni hacer buen contacto.",
        "El alumbrado y la señalización son parte de la seguridad: una luz de freno fundida o un aviso desactivado se repara en su causa, no se oculta, porque la revisión técnica y la seguridad vial dependen de ellos. Toda modificación de un circuito se registra y respeta el manual. Las pruebas finales las hace personal autorizado.",
        f"Esta clase calcula y compara repuestos en papel; no enseña a reemplazar componentes. {EMER} {AVISO}",
    ],
    vocab=[("carga del circuito", "suma de las potencias de sus componentes"), ("margen del fusible", "valor del fusible menos la corriente normal"), ("referencia", "código que identifica el repuesto correcto"), ("base de la lámpara", "parte que calza y conecta la lámpara al portalámparas"), ("modificación", "cambio de un circuito respecto de su diseño")],
    worked=[
        ("Corriente de un circuito", "Un circuito de ejemplo tiene 3 luces de 12 W cada una conectadas directamente a 12 V. ¿Cuántos A normales pasan?", ["La potencia total es 3 por 12, es decir 36 W.", "36 entre 12 son 3."], "3 A"),
        ("Margen del fusible", "Un circuito de ejemplo tiene una corriente normal de 6 A y un fusible de 10 A. ¿Cuál es el margen?", ["El margen es el valor del fusible menos la corriente normal.", "10 menos 6 son 4."], "4 A"),
    ],
    mistakes=[("Usar una lámpara de mayor potencia «para que alumbre más».", "Aumenta el consumo y el calor del cableado aunque el fusible no se abra.", "Usa la referencia que exige el fabricante."),
              ("Usar un repuesto que «casi calza» con la misma potencia.", "Una base distinta puede no calzar ni hacer buen contacto.", "Pide la referencia correcta o consulta el manual.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿por qué se reemplaza una lámpara por otra con la referencia exacta que exige el fabricante?", "Porque una de mayor potencia aumenta el consumo y el calor del cableado, y una base distinta puede no calzar", "Porque la referencia solo cambia el color de la luz", "Porque la potencia no afecta al circuito", "La referencia garantiza potencia y base compatibles con el circuito."),
        ("abc", "En Mecánica Automotriz: ¿qué es el margen de un fusible?", "La diferencia entre el valor del fusible y la corriente normal del circuito", "El precio del fusible", "La duración del fusible en meses", "El margen mide cuánta corriente sobra antes de que el fusible se abra."),
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula la corriente total de varias cargas conectadas directamente a la alimentación?", "Sumando las potencias y dividiendo entre la tensión", "Multiplicando las potencias entre sí", "Dividiendo la tensión entre el número de cargas", "La corriente total sale de la potencia total dividida por la tensión."),
        ("abc", "{F} ¿Qué repuesto corresponde al vehículo según la ficha?", "L-24", "L-24-X", "L-60", "La ficha exige la referencia L-24; L-24-X tiene otra base y L-60 otra potencia."),
        ("abc", "{F} ¿Qué cargas forman el circuito de alumbrado trasero?", "Dos luces de freno de 24 W y dos luces de posición de 6 W", "Cuatro actuadores de 24 W", "Una lámpara de 60 W", "El alumbrado trasero reúne luces de freno y de posición; los actuadores son del cierre centralizado."),
        ("abc", "{F} ¿Qué decisión depende del cálculo de la carga y no del precio de los repuestos?", "Si el fusible del circuito sigue siendo adecuado", "Cuál repuesto se compra primero", "Cuántas horas trabaja el taller por la tarde", "El cálculo de carga permite decidir si el fusible protege bien el circuito."),
        ("=", "{F} ¿Cuántos W suma el circuito de alumbrado trasero?", "2*24+2*6", "Se suman las potencias de las dos luces de freno y de las dos de posición.", " W"),
        ("=", "{F} ¿Cuántos A normales pasan por el fusible del alumbrado trasero?", "(2*24+2*6)//12", "Se divide la potencia total entre la tensión.", " A"),
        ("=", "{F} Si los cuatro actuadores del cierre centralizado funcionan a la vez, ¿cuántos A de margen tiene su fusible de 15 A?", "15-(4*24)//12", "Se calcula la corriente de los actuadores y se resta al valor del fusible.", " A"),
        ("abc", "{F} Un compañero propone usar la lámpara L-60 en lugar de una luz de freno de 24 W «para que alumbre más». ¿Qué respuesta es correcta?", "No corresponde: se usa la referencia del fabricante, porque una lámpara de mayor potencia aumenta el consumo y el calor del cableado aunque el fusible no se abra", "Corresponde, porque más potencia siempre es mejor", "Corresponde, mientras el fusible no se abra", "Que el fusible no se abra no significa que el cableado esté a salvo."),
        ("abc", "{F} El taller no tiene L-24 y propone usar L-24-X porque «tiene la misma potencia». ¿Qué corresponde?", "Pedir la referencia correcta o consultar el manual, porque una base distinta puede no calzar ni contactar bien", "Usar L-24-X, porque la potencia es lo único que importa", "Forzar L-24-X para que calce", "La referencia incluye la base; forzar una pieza puede dañar el portalámparas."),
        ("=", "{F} Se agrega al alumbrado trasero una tercera luz de 24 W conectada directamente. ¿Cuántos A normales pasan ahora?", "(2*24+2*6+24)//12", "Se suma la nueva potencia a la anterior y se divide entre la tensión.", " A"),
        ("abc", "{F} Con esa tercera luz, el margen del fusible de 10 A es de 3 A. ¿Qué conclusión corresponde?", "El fusible sigue siendo adecuado, pero la modificación se registra y debe respetar el manual", "No hay que registrar nada porque el fusible no se abre", "El margen es negativo y el fusible se abrirá siempre", "Un margen de 3 A es positivo; igual toda modificación se registra y sigue el manual."),
    ],
    ctx=("abc", "Una persona propietaria quiere desactivar el aviso de una luz fundida «porque molesta». ¿Qué respondes?", "Que el aviso protege la seguridad y la revisión técnica verifica el alumbrado, por lo que se repara la causa y no se desactiva el aviso", "Que sí, si hay otra luz que alumbre", "Que sí, si el vehículo pasa la revisión técnica", "Desactivar un aviso oculta una falla que afecta la seguridad."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula la corriente normal de un circuito?", "Con la potencia total dividida por la tensión", "Cada carga aporta su potencia al total."),
        ("¿Qué repuesto se usa?", "El de la referencia exacta que exige el fabricante", "La potencia y la base deben coincidir."),
        ("¿Qué se hace con una modificación de un circuito?", "Se registra y respeta el manual", "Así queda trazabilidad y se respeta la seguridad."),
    ],
    op=("Ficha de ejemplo: alumbrado delantero de 12 V con 2 luces de 60 W y 2 luces de 6 W conectadas directamente, protegidas por un fusible de 15 A. La ficha del vehículo exige la referencia H-60; en la bodega hay H-60, H-55 y H-60-B. Escribe (a) la potencia total, (b) la corriente normal, (c) el margen del fusible, (d) qué referencia usas y por qué.",
        "(a) 2 × 60 + 2 × 6 = 132 W. (b) 132 ÷ 12 = 11 A. (c) 15 − 11 = 4 A. (d) H-60, porque es la referencia exacta que exige la ficha; H-55 cambia la potencia y H-60-B es otra referencia.",
        ["calcula la potencia total", "calcula la corriente", "calcula el margen", "elige la referencia y justifica"],
        ["hoja con las cuatro respuestas"],
        ["no sumar todas las cargas", "elegir una referencia parecida", "olvidar la unidad"],
        "Pregunta: «¿qué referencia pide exactamente la ficha?». Si duda, pídele que relea la regla de la referencia."),
    reinforce="Inventa un circuito con tres cargas de potencia conocida y calcula su corriente y el margen de un fusible.",
    extend="Explica con un ejemplo por qué la misma potencia no basta para decir que dos lámparas son equivalentes.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller «Confort y Seguridad Demo» atiende cinturones de seguridad, airbag, alarmas, aire acondicionado y equipos de audio. "
     "Su matriz de peligros anota: airbag con componentes pirotécnicos, cinturones con pretensor pirotécnico, refrigerante del aire acondicionado a presión, cargas eléctricas adicionales (audio y alarma) y cableado oculto. "
     "Tareas del día: 14, de ellas 3 de cinturones, 2 de airbag, 4 de alarma, 3 de aire acondicionado y 2 de audio.")
build(
    O7, 1, F,
    use="Aprenderé qué sistemas de seguridad y de confort tiene un vehículo, qué peligros tiene cada uno en un taller y por qué algunos no se manipulan sin autorización.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé sumar y multiplicar números enteros.", "Sé que un vehículo tiene cinturones y aire acondicionado."],
    explain=[
        "Los sistemas de seguridad pasiva reducen lesiones en un choque: el cinturón sujeta a la persona al asiento y el airbag es una bolsa que se infla en un choque y complementa al cinturón, no lo reemplaza. Los sistemas de confort, como el aire acondicionado, el audio y la alarma, hacen más cómodo o más seguro el uso. Todos se documentan en el manual del fabricante.",
        "El airbag y el pretensor del cinturón tienen componentes pirotécnicos, es decir cargas que se activan de golpe y pueden lesionar gravemente si se activan por error; solo los manipula personal autorizado, siguiendo las indicaciones del fabricante y la norma vigente. El aire acondicionado usa un refrigerante a presión, que puede causar quemaduras por frío y dañar el ambiente si se libera. Los accesorios eléctricos suman carga al circuito y pueden causar un incendio si no se calculan.",
        f"La norma vigente exige que los accesorios no alteren los sistemas de seguridad del vehículo. {EMER} {AVISO}",
    ],
    vocab=[("cinturón de seguridad", "correa que sujeta a la persona al asiento"), ("airbag", "bolsa que se infla en un choque y complementa al cinturón"), ("pirotécnico", "con una carga que se activa de golpe"), ("refrigerante", "fluido a presión del aire acondicionado"), ("sistema de confort", "sistema que mejora la comodidad, como el aire acondicionado"), ("alarma", "sistema que advierte una apertura o un golpe no autorizados")],
    worked=[
        ("Cuántas tareas", "Un día de ejemplo tiene 4 tareas de alarma y 5 de audio, de un total de 20. ¿Cuántas no son de alarma ni de audio?", ["Se suman las tareas de alarma y de audio: 9.", "20 menos 9 son 11."], "11 tareas"),
        ("Seguridad o confort", "Un taller de ejemplo atiende un cinturón de seguridad y un equipo de audio. ¿Cuál es un sistema de seguridad pasiva y cuál uno de confort?", ["El cinturón sujeta a la persona y reduce lesiones en un choque.", "El audio solo hace más cómodo el uso del vehículo."], "El cinturón es de seguridad pasiva; el audio es de confort"),
    ],
    mistakes=[("Creer que el airbag reemplaza al cinturón.", "El airbag complementa al cinturón, que sigue siendo la sujeción principal.", "Usa siempre el cinturón: el airbag solo lo complementa."),
              ("Pensar que un componente pirotécnico «no se activa solo».", "Puede activarse por error y lesionar gravemente.", "Solo personal autorizado, con las indicaciones del fabricante, lo manipula.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué función cumple el cinturón de seguridad?", "Sujetar a la persona al asiento para reducir lesiones en un choque o frenado brusco", "Evitar que el vehículo se mueva", "Reemplazar al airbag", "El cinturón retiene a la persona; no detiene el vehículo ni sustituye al airbag."),
        ("abc", "En Mecánica Automotriz: ¿cuál es la relación entre el airbag y el cinturón?", "El airbag complementa al cinturón y no lo reemplaza", "El airbag reemplaza al cinturón", "Funcionan solo uno u otro, nunca juntos", "Ambos trabajan juntos y el cinturón sigue siendo la sujeción principal."),
        ("abc", "En Mecánica Automotriz: ¿por qué un airbag se considera peligroso de manipular?", "Porque tiene componentes pirotécnicos que pueden activarse y lesionar gravemente", "Porque es muy caro de reponer", "Porque pesa demasiado para levantarlo", "Su peligro está en la carga pirotécnica, no en su precio ni en su peso."),
        ("abc", "{F} ¿Qué peligro de la matriz se relaciona con los pretensores de los cinturones?", "Los componentes pirotécnicos", "El refrigerante a presión", "Las cargas eléctricas adicionales", "El pretensor tiene una carga pirotécnica que tensa el cinturón en un choque."),
        ("abc", "{F} ¿Qué sistema de la matriz tiene refrigerante a presión?", "El aire acondicionado", "La alarma", "El audio", "El refrigerante es el fluido del aire acondicionado."),
        ("abc", "{F} El taller exige instalar accesorios eléctricos solo según el manual y con el fusible adecuado. ¿Qué peligro previene?", "La sobrecarga eléctrica y el incendio", "Las quemaduras por frío", "La activación accidental del airbag", "Un accesorio mal calculado puede sobrecargar el circuito y calentarlo."),
        ("=", "{F} ¿Cuántas tareas de seguridad pasiva, de cinturones y airbag, tiene el día?", "3+2", "Se suman las tareas de cinturones y de airbag.", " tareas"),
        ("=", "{F} Cada tarea de cinturones o airbag exige 2 horas de personal autorizado. ¿Cuántas horas suman?", "(3+2)*2", "Se suman las tareas y se multiplican por las horas de cada una.", " horas"),
        ("=", "{F} ¿Cuántas tareas del día no son de aire acondicionado?", "14-3", "Se resta al total las tareas de aire acondicionado.", " tareas"),
        ("abc", "{F} Un compañero dice: «con airbag no se necesita cinturón». ¿Qué respuesta es correcta?", "Es falso: el airbag complementa al cinturón, que sigue siendo la sujeción principal", "Es cierto: el airbag protege por sí solo", "Es cierto, si el vehículo es nuevo", "El airbag está diseñado para trabajar junto con el cinturón."),
        ("abc", "Un aprendiz de ejemplo quiere liberar el gas del aire acondicionado a la atmósfera «porque no se ve». ¿Qué corresponde?", "No: el refrigerante daña el ambiente y es peligroso, y solo personal capacitado con equipo y norma vigente lo recupera", "Sí, si es poca cantidad", "Sí, siempre que lo haga al aire libre", "Que no se vea no significa que no contamine; su manejo exige formación y equipo."),
        ("=", "{F} El taller cobra $9.000 por hora de mano de obra. ¿Cuántos pesos suma la mano de obra de las tareas de cinturones y airbag, con 2 horas cada una?", "(3+2)*2*9000", "Se calculan las horas totales y se multiplican por la tarifa.", " pesos"),
        ("abc", "En una visita a un taller de ejemplo, un módulo de airbag se activa de golpe cerca de una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a revisar si la persona está herida sin avisar", "Recoger la pieza para guardarla", "Acercarse sin avisar puede sumar otra lesión; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "Una persona propietaria te propone «sacar el airbag» del volante para instalar un volante deportivo. ¿Qué respondes?", "Que modificar el airbag altera un sistema de seguridad y no se hace sin respaldo del fabricante y la norma vigente; se consulta a un taller autorizado", "Que sí, si el volante nuevo se ve bien", "Que sí, si deja el cinturón puesto", "El airbag es un sistema de seguridad y no se retira por estética."),
    sc=[
        ("En Mecánica Automotriz: ¿qué significa pirotécnico en un airbag?", "Que tiene una carga que se activa de golpe", "Por eso solo personal autorizado lo manipula."),
        ("¿Qué sistema de confort usa refrigerante a presión?", "El aire acondicionado", "El refrigerante circula a presión en su circuito."),
        ("¿Quién manipula airbag y pretensores?", "Personal autorizado, con indicaciones del fabricante", "Una activación por error puede lesionar gravemente."),
    ],
    op=("El taller de ejemplo recibe dos pedidos: revisar un airbag y recuperar el refrigerante de un aire acondicionado. Escribe (a) el peligro de cada pedido, (b) un control administrativo, (c) un control de ingeniería para uno de ellos, (d) quién hace estas tareas y por qué el EPP no basta. No describas cómo se hacen.",
        "(a) Airbag: la carga pirotécnica que puede activarse; aire acondicionado: el refrigerante a presión. (b) Una regla escrita y una señal de que solo personal autorizado manipula estos sistemas. (c) Un equipo cerrado de recuperación de refrigerante, para no liberarlo. (d) Personal autorizado y capacitado, con norma vigente; el EPP no quita el peligro.",
        ["identifica un peligro por pedido", "propone un control administrativo", "propone un control de ingeniería", "indica quién hace la tarea y por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["decir que cualquiera puede manipularlo", "proponer solo el EPP", "describir cómo se hace la tarea"],
        "Pregunta: «¿qué puede pasar si ese sistema se activa o se libera por error?». Si no responde, pídele que relea los peligros de la clase."),
    reinforce="Escribe tres sistemas de seguridad o confort de la clase y el peligro de cada uno.",
    extend="Explica con un ejemplo por qué un sistema de seguridad no se modifica por estética.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Manual del fabricante de ejemplo: equipo de audio AUD-2, 120 W a 12 V, con un fusible dedicado de 15 A; alarma ALM-1, con un consumo continuo de 2 A. "
     "Pauta de ejemplo: filtro de cabina del aire acondicionado, cada 15.000 km o 12 meses; cinturón de seguridad, se reemplaza después de un impacto fuerte, según el manual. "
     "Ficha de instalación de ejemplo: anota la fecha, el vehículo, el accesorio con su referencia, quién lo instaló y la garantía, que es de 12 meses.")
build(
    O7, 2, F,
    use="Aprenderé cómo funciona el aire acondicionado, qué documentos respaldan la instalación de accesorios y cómo calcular la carga eléctrica de un audio y una alarma.",
    prior=["Sé calcular la corriente con potencia y tensión.", "Sé qué es un fusible.", "Sé qué es una referencia."],
    explain=[
        "El aire acondicionado mueve calor con un refrigerante que circula en un circuito cerrado. El compresor comprime el refrigerante; el condensador libera su calor al exterior; una válvula lo expande; y el evaporador absorbe calor del aire del habitáculo al evaporarse el refrigerante. Una alarma tiene sensores, un módulo y una sirena; un equipo de audio es una carga eléctrica que se calcula como cualquier otra.",
        "La instalación de accesorios se respalda con documentos: el manual del fabricante fija el fusible y la carga; la ficha de instalación anota fecha, vehículo, accesorio y su referencia, quién lo instaló y la garantía; y la pauta de mantenimiento fija los reemplazos. Sin ficha no hay trazabilidad ni garantía. Los componentes de seguridad, como los cinturones, se reemplazan según las indicaciones del fabricante, por ejemplo después de un impacto fuerte.",
        f"Esta clase lee documentos y calcula en papel; las instalaciones reales las hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("compresor", "componente que comprime el refrigerante"), ("condensador", "componente que libera el calor del refrigerante al exterior"), ("evaporador", "componente que absorbe calor del aire del habitáculo"), ("ficha de instalación", "documento que anota fecha, accesorio, quién lo instaló y garantía"), ("fusible dedicado", "fusible exclusivo para un accesorio"), ("filtro de cabina", "filtro del aire que entra al habitáculo")],
    worked=[
        ("Corriente de un accesorio", "Un equipo de ejemplo de 96 W funciona a 12 V. ¿Cuántos A consume?", ["La corriente es la potencia dividida por la tensión.", "96 entre 12 son 8."], "8 A"),
        ("Qué documento", "Se quiere saber quién instaló un accesorio de ejemplo, cuándo y con qué garantía. ¿Qué documento se consulta?", ["Ese documento anota fecha, accesorio, quién instaló y garantía.", "Es la ficha de instalación."], "La ficha de instalación"),
    ],
    mistakes=[("Instalar un accesorio sin anotar su referencia ni la fecha.", "Se pierde la trazabilidad y la garantía queda sin respaldo.", "Completa la ficha de instalación con todos sus datos."),
              ("Elegir un fusible igual al consumo del accesorio.", "No deja margen y se abriría sin falla real.", "Usa el fusible que fija el manual del fabricante.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué función cumple el compresor del aire acondicionado?", "Comprimir el refrigerante para hacerlo circular por el circuito", "Enfriar el aire del habitáculo directamente con agua", "Almacenar energía eléctrica", "El compresor mueve y comprime el refrigerante; no usa agua ni almacena energía."),
        ("abc", "En Mecánica Automotriz: ¿qué hace el evaporador del aire acondicionado?", "Absorbe calor del aire del habitáculo al evaporarse el refrigerante", "Libera calor al exterior", "Comprime el refrigerante", "El evaporador enfría el habitáculo; el condensador libera calor y el compresor comprime."),
        ("abc", "En Mecánica Automotriz: ¿qué anota una ficha de instalación de un accesorio?", "El vehículo, el accesorio con su referencia, la fecha, quién lo instaló y la garantía", "Solo el precio del accesorio", "Solo el nombre de la persona propietaria", "La ficha de instalación respalda el trabajo con todos esos datos."),
        ("abc", "{F} ¿Qué fusible exige el manual para el equipo de audio?", "Un fusible dedicado de 15 A", "Uno de 5 A compartido con otros accesorios", "Ninguno, porque el audio no necesita fusible", "El manual fija un fusible dedicado de 15 A."),
        ("abc", "{F} ¿Qué documento de la ficha fija el fusible del audio?", "El manual del fabricante", "La ficha de instalación", "La pauta de mantenimiento", "El manual del fabricante fija fusible y carga; la ficha de instalación solo registra lo hecho."),
        ("abc", "{F} ¿Cuándo se reemplaza un cinturón según la pauta de la ficha?", "Después de un impacto fuerte, según el manual", "Cada 15.000 km", "Nunca, porque dura toda la vida del vehículo", "Un cinturón puede quedar dañado tras un impacto fuerte aunque no se vea."),
        ("=", "{F} ¿Cuántos A consume el equipo de audio?", "120//12", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "{F} ¿Cuántos A de margen tiene el fusible dedicado del audio?", "15-120//12", "Se calcula la corriente del audio y se resta al valor del fusible.", " A"),
        ("=", "{F} El filtro de cabina se reemplazó a los 40.000 km. ¿A qué kilometraje vence por kilometraje?", "40000+15000", "Se suma el intervalo al kilometraje del último reemplazo.", " km"),
        ("abc", "{F} Un compañero dice: «el audio consume 10 A, así que basta un fusible de 10 A». ¿Qué respuesta es correcta?", "Es falso: un fusible igual a la corriente normal no deja margen y el manual fija uno dedicado de 15 A", "Es cierto: coincide con el consumo", "Es falso: conviene uno de 40 A para mayor seguridad", "El fusible debe dejar margen sin perder su función de protección."),
        ("abc", "Un técnico instala un accesorio sin anotar la referencia ni la fecha. ¿Qué problema tiene?", "Pierde la trazabilidad y la garantía queda sin respaldo", "Ninguno, si el accesorio funciona", "Que el accesorio se desactiva solo", "Sin ficha no se puede demostrar qué se instaló, cuándo ni con qué garantía."),
        ("=", "{F} Se agrega la alarma al mismo circuito del audio. ¿Cuántos A de margen quedan respecto del fusible de 15 A?", "15-(120//12)-2", "Se restan al fusible las corrientes del audio y de la alarma.", " A"),
        ("abc", "{F} ¿Qué anotación de instalación es correcta?", "Fecha, vehículo, referencias ALM-1 y AUD-2, fusible dedicado de 15 A para el audio, técnico y garantía de 12 meses", "Audio instalado, funciona bien", "Alarma y audio sin referencias, para ahorrar tiempo", "La ficha completa permite trazabilidad y garantía."),
    ],
    ctx=("abc", "Una persona propietaria te pide una instalación «sin ficha, para que salga más barata». ¿Qué respondes?", "Que la ficha y la garantía respaldan el trabajo y a ambas partes, y por eso se anotan", "Que sí, si paga al contado", "Que se anota en una libreta personal", "La ficha de instalación es el respaldo de la garantía."),
    sc=[
        ("En Mecánica Automotriz: ¿qué componente del aire acondicionado absorbe calor del habitáculo?", "El evaporador", "Al evaporarse, el refrigerante absorbe calor."),
        ("¿Quién fija el fusible de un accesorio?", "El manual del fabricante", "El fabricante conoce la carga y el circuito."),
        ("¿Qué respalda la garantía de una instalación?", "La ficha de instalación", "Sin ella no hay trazabilidad ni garantía."),
    ],
    op=("Ficha de ejemplo: manual del fabricante: parlantes PAR-1, 72 W a 12 V, con un fusible dedicado de 15 A. Pauta: filtro de cabina cada 20.000 km o 12 meses; el último reemplazo fue a los 31.000 km. Escribe (a) la corriente de los parlantes, (b) el margen del fusible, (c) el kilometraje en que vence el filtro de cabina, (d) qué datos anotas en la ficha de instalación.",
        "(a) 72 ÷ 12 = 6 A. (b) 15 − 6 = 9 A. (c) 31.000 + 20.000 = 51.000 km. (d) La fecha, el vehículo, el accesorio con su referencia, quién lo instaló y la garantía.",
        ["calcula la corriente", "calcula el margen", "calcula el vencimiento", "completa los datos de la ficha"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "no restar la corriente al fusible", "olvidar la referencia en la ficha"],
        "Pregunta: «¿potencia entre tensión o tensión entre potencia?». Si duda, pídele que relea cómo se calcula la corriente."),
    reinforce="Inventa un accesorio con su potencia y fusible, y calcula su corriente y su margen.",
    extend="Explica con un ejemplo por qué el refrigerante no se libera a la atmósfera.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (solicitudes de ejemplo, inventadas). Cuatro solicitudes de personas propietarias en un taller. S1: instalar un equipo de audio de 180 W a 12 V. S2: instalar una luz auxiliar de 36 W. S3: desactivar la luz de aviso del airbag, que está encendida. S4: reemplazar un cinturón con el tejido deshilachado. "
     "Reglas de ejemplo del taller: las solicitudes que alteran sistemas de seguridad se rechazan o se derivan al servicio autorizado del fabricante; los accesorios eléctricos se aceptan con carga calculada y fusible dedicado según el manual; los cinturones se reemplazan con la referencia del fabricante y personal autorizado.")
build(
    O7, 3, F,
    use="Aprenderé a evaluar solicitudes de clientes en papel: aceptar, aceptar con condiciones, derivar o rechazar, según si alteran un sistema de seguridad y según su carga eléctrica.",
    prior=["Sé calcular la corriente de un accesorio.", "Sé qué es un sistema de seguridad.", "Sé qué es una ficha de instalación."],
    explain=[
        "Evaluar una solicitud es decidir con criterios escritos. Primero se pregunta si altera un sistema de seguridad: si lo altera, se rechaza o se deriva al servicio autorizado del fabricante, sin importar quién la pida. Si es un accesorio eléctrico, se calcula la carga y se verifica el fusible dedicado del manual. Si es un reemplazo de un componente de seguridad, se usa la referencia del fabricante y personal autorizado.",
        "Una luz de aviso de airbag encendida indica que el sistema detectó una falla y debe evaluarlo personal autorizado; desactivarla o taparla oculta el riesgo. Un cinturón con el tejido dañado puede fallar en un impacto y no se repara con costuras ni parches: se reemplaza. Toda solicitud y su decisión se registran, con la explicación entregada a la persona propietaria.",
        f"Esta clase evalúa solicitudes escritas; no se interviene ningún sistema real. {EMER} {AVISO}",
    ],
    vocab=[("solicitud", "pedido de una persona propietaria al taller"), ("derivar", "enviar una tarea a quien está autorizado para hacerla"), ("servicio autorizado", "taller reconocido por el fabricante"), ("aceptar con condiciones", "aceptar si se cumplen requisitos técnicos"), ("registro de decisión", "anotación de qué se decidió y por qué")],
    worked=[
        ("Aceptar con condiciones", "Una solicitud de ejemplo pide instalar un cargador de teléfono de 24 W para el vehículo. El manual exige carga calculada y fusible dedicado. ¿Cómo se decide?", ["Es un accesorio eléctrico, no altera un sistema de seguridad.", "Se acepta con carga calculada y fusible dedicado."], "Se acepta con condiciones"),
        ("Derivar", "Una persona de ejemplo pide quitar el aviso de una falla del sistema de frenos. ¿Cómo se decide?", ["Ese aviso es parte de un sistema de seguridad.", "Desactivarlo altera el sistema: se deriva o se rechaza."], "Se rechaza o se deriva al servicio autorizado"),
    ],
    mistakes=[("Aceptar una solicitud que altera un sistema de seguridad porque la persona es cliente frecuente.", "La decisión no depende de quién pide.", "Aplica la regla escrita a todas las solicitudes."),
              ("Reparar un cinturón dañado con una costura.", "Un cinturón dañado puede fallar en un impacto y debe reemplazarse.", "Se reemplaza con la referencia del fabricante y personal autorizado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué hace un taller ante una solicitud que altera un sistema de seguridad?", "La rechaza o la deriva al servicio autorizado del fabricante", "La acepta si la persona propietaria firma", "La acepta si el costo es bajo", "Un sistema de seguridad no se altera ni con firma ni por precio."),
        ("abc", "En Mecánica Automotriz: ¿qué indica una luz de aviso de airbag encendida?", "Que el sistema detectó una falla y debe ser evaluado por personal autorizado", "Que el airbag está listo y no necesita revisión", "Que la luz está fundida y se puede apagar", "La luz de aviso señala una posible falla del sistema."),
        ("abc", "En Mecánica Automotriz: ¿qué condiciones debe cumplir un accesorio eléctrico que se instala?", "Carga calculada, fusible dedicado según el manual y registro de la instalación", "Solo que encienda al conectarlo", "Solo que sea de una marca conocida", "Un accesorio se acepta con cálculo, protección y registro."),
        ("abc", "{F} ¿Qué solicitud se rechaza o se deriva al servicio autorizado del fabricante?", "S3, desactivar el aviso del airbag", "S2, instalar una luz auxiliar", "S1, instalar el equipo de audio", "Desactivar el aviso altera un sistema de seguridad; las otras son accesorios eléctricos."),
        ("abc", "{F} ¿Cómo se atiende S4, el cinturón deshilachado?", "Se reemplaza con la referencia del fabricante y personal autorizado", "Se repara cosiendo el tejido", "Se deja como está si todavía se abrocha", "Un cinturón dañado puede fallar; la regla pide reemplazo con la referencia del fabricante."),
        ("abc", "{F} ¿Qué dato falta para decidir sobre S1?", "La carga eléctrica total y el fusible dedicado que fija el manual", "El color del equipo de audio", "La marca del vehículo", "S1 es un accesorio eléctrico y se decide con carga y fusible."),
        ("=", "{F} ¿Cuántos A consume el equipo de audio de S1?", "180//12", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "{F} El manual de ejemplo fija un fusible dedicado de 25 A para ese audio. ¿Cuántos A de margen tiene?", "25-180//12", "Se calcula la corriente y se resta al valor del fusible.", " A"),
        ("=", "{F} Cada solicitud requiere 1 hora de revisión documental a $9.000 la hora. ¿Cuántos pesos suman las 4 solicitudes?", "4*1*9000", "Se multiplican las solicitudes, las horas y la tarifa.", " pesos"),
        ("abc", "{F} Una persona dice: «la luz de airbag es un aviso molesto, con un poco de cinta se tapa». ¿Qué respuesta es correcta?", "Es falso: la luz señala una posible falla del sistema de seguridad y tapar el aviso oculta el riesgo", "Es cierto, porque el airbag funciona igual", "Es cierto, si el cinturón está puesto", "Tapar el aviso no corrige la falla y deja el riesgo sin evaluar."),
        ("abc", "Un taller de ejemplo acepta S3 «por ser un cliente frecuente». ¿Qué observación es correcta?", "No corresponde: desactivar un aviso de seguridad altera el sistema y no depende del tipo de cliente", "Corresponde, porque los clientes frecuentes tienen excepciones", "Corresponde si el cliente firma una declaración", "La regla se aplica a todas las solicitudes por igual."),
        ("=", "{F} Si S1 se aprueba y se agrega la luz auxiliar de S2 en el mismo circuito, ¿cuántos A normales pasan?", "(180+36)//12", "Se suman las potencias y se divide entre la tensión.", " A"),
        ("abc", "{F} ¿Qué respuesta corresponde a la persona de S3?", "Explicar que el aviso indica una posible falla del sistema de seguridad, que no se desactiva y que se deriva al servicio autorizado, registrando la solicitud", "Aceptar y apagar la luz", "Rechazar sin explicar ni registrar", "La respuesta explica, deriva y deja registro."),
    ],
    ctx=("abc", "Una persona propietaria te muestra un cinturón deshilachado y dice que «todavía sirve». ¿Qué respondes?", "Que un cinturón dañado puede fallar en un impacto y debe reemplazarlo personal autorizado con la referencia correcta", "Que sí sirve mientras se abroche", "Que se refuerza con una costura", "Un cinturón con el tejido dañado pierde resistencia aunque aún se abroche."),
    sc=[
        ("En Mecánica Automotriz: ¿qué se hace con una solicitud que altera un sistema de seguridad?", "Se rechaza o se deriva al servicio autorizado", "La decisión no depende de quién la pide."),
        ("¿Qué se calcula antes de aceptar un accesorio eléctrico?", "La carga y el fusible dedicado", "Así se evita una sobrecarga del circuito."),
        ("¿Qué se registra de cada solicitud?", "La decisión y su explicación", "El registro da trazabilidad a cada decisión tomada."),
    ],
    op=("Ficha de ejemplo: S1: instalar parlantes de 96 W a 12 V, con fusible dedicado de 15 A según el manual. S2: «quitar» el airbag del volante. S3: reemplazar un cinturón dañado. Escribe (a) la decisión para cada solicitud: aceptar con condiciones, derivar, rechazar o reemplazar con la referencia, (b) la corriente de S1 y su margen de fusible, (c) qué explicas a la persona de S2, (d) qué se registra.",
        "(a) S1: se acepta con condiciones; S2: se rechaza o se deriva al servicio autorizado; S3: se reemplaza con la referencia del fabricante por personal autorizado. (b) 96 ÷ 12 = 8 A; margen 15 − 8 = 7 A. (c) Que quitar el airbag altera un sistema de seguridad y no se hace. (d) La solicitud, la decisión, su explicación y, para S1 y S3, los datos de la instalación.",
        ["decide cada solicitud", "calcula la corriente y el margen", "explica el rechazo", "indica qué se registra"],
        ["hoja con las cuatro respuestas"],
        ["aceptar la modificación del airbag", "calcular mal el margen", "no registrar la decisión"],
        "Pregunta: «¿esta solicitud altera un sistema de seguridad?». Si duda, pídele que relea la regla del taller de la ficha."),
    reinforce="Inventa tres solicitudes de una persona propietaria y decide cuál se acepta, cuál se deriva y cuál se rechaza.",
    extend="Explica con un ejemplo por qué una norma de seguridad vale para todos los clientes por igual.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (propuestas de instalación de ejemplo, inventadas). Dos propuestas para un mismo vehículo, con un circuito dedicado de 12 V y fusible de 15 A. "
     "Propuesta P: audio de 96 W y alarma de 24 W; materiales $135.000; mano de obra 3 horas; garantía 6 meses. Propuesta Q: audio de 144 W y alarma de 24 W; materiales $220.000; mano de obra 4 horas; garantía 12 meses. Tarifa: $11.000 por hora. "
     "Condición de ejemplo del manual: la corriente normal del circuito no debe superar el 80 % del valor del fusible.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar una condición técnica del manual a dos propuestas de instalación y a comparar costos solo entre las propuestas que cumplen.",
    prior=["Sé calcular la corriente de un accesorio.", "Sé calcular costo con horas y tarifa.", "Sé calcular un porcentaje exacto."],
    explain=[
        "Una condición del manual puede limitar la carga de un circuito, por ejemplo a un porcentaje del valor del fusible. El 80 % de un valor se calcula multiplicando por 80 y dividiendo entre 100. La corriente normal del circuito, en amperes, es la suma de las potencias dividida por la tensión. Si la corriente supera el límite de la condición, la propuesta no cumple, aunque quede bajo el valor del fusible.",
        "Primero se verifica el cumplimiento técnico y de seguridad; solo entre las propuestas que cumplen se comparan costo total y costo por mes de garantía. Una propuesta más barata por mes no se elige si no cumple la condición. Si el fusible se aumenta para que una propuesta «quepa», el cableado queda sin protección. Las instalaciones las hace personal autorizado y se anotan en una ficha de instalación.",
        f"Esta clase aplica reglas y calcula en papel; no enseña a instalar. {EMER} {AVISO}",
    ],
    vocab=[("condición del manual", "requisito técnico que fija el fabricante"), ("porcentaje", "parte de cada cien"), ("cumplimiento técnico", "que una propuesta respete las condiciones del manual"), ("costo por mes de garantía", "costo total dividido por los meses de garantía"), ("propuesta", "oferta de trabajo con materiales, horas y garantía")],
    worked=[
        ("Calcular el 80 %", "Un fusible de ejemplo es de 10 A y la condición pide a lo más el 80 % de su valor. ¿Cuántos A permite?", ["Se multiplica 10 por 80 y se divide entre 100.", "10 por 80 son 800 y entre 100 son 8."], "8 A"),
        ("Corriente de un circuito", "Dos equipos de ejemplo de 48 W y 36 W se conectan directamente a 12 V. ¿Cuántos A normales pasan?", ["Se suman las potencias: 84 W.", "84 entre 12 son 7."], "7 A"),
    ],
    mistakes=[("Elegir la propuesta de menor costo por mes sin revisar la condición del manual.", "Una propuesta que no cumple no se compara por precio.", "Verifica primero el cumplimiento técnico."),
              ("Pedir un fusible mayor para que la propuesta «quepa».", "El cableado queda sin protección adecuada.", "Reduce la carga o consulta al fabricante con personal autorizado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué significa que la carga no supere el 80 % del fusible?", "Que la corriente normal debe ser a lo más el 80 % del valor del fusible", "Que el fusible debe costar el 80 % del precio del equipo", "Que el equipo debe funcionar el 80 % del tiempo", "El 80 % se aplica al valor del fusible como límite de corriente normal."),
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula el 80 % de un valor?", "Multiplicando por 80 y dividiendo entre 100", "Restándole 80", "Dividiéndolo entre 80", "El porcentaje se calcula como el valor por 80 dividido entre 100."),
        ("abc", "En Mecánica Automotriz: ¿qué se verifica primero al comparar propuestas de instalación?", "Que cumplan las condiciones técnicas y de seguridad del manual", "Cuál tiene el menor costo por mes", "Cuál tiene la garantía más larga", "Solo se comparan por costo las propuestas que cumplen la condición técnica."),
        ("abc", "{F} ¿Qué condición del manual deben cumplir ambas propuestas?", "Una corriente normal de a lo más el 80 % del fusible de 15 A", "Una garantía de al menos 12 meses", "Un costo de materiales menor que $200.000", "La condición del manual limita la corriente normal del circuito."),
        ("abc", "{F} ¿En qué unidad se compara la carga del circuito con el fusible?", "En amperes (A)", "En watts (W)", "En volts (V)", "El fusible se mide en amperes y la carga se convierte a corriente."),
        ("abc", "{F} ¿Qué decisión depende del cálculo de la carga y no del precio?", "Si la propuesta cumple la condición de seguridad", "Qué propuesta usa menos horas", "Qué propuesta tiene materiales más baratos", "La carga define el cumplimiento; el precio solo se compara después."),
        ("=", "{F} ¿Cuántos A normales tiene la propuesta P?", "(96+24)//12", "Se suman las potencias y se divide entre la tensión.", " A"),
        ("=", "{F} ¿Cuántos pesos cuesta en total la propuesta P, entre materiales y mano de obra?", "135000+3*11000", "Se suman los materiales con las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta por mes de garantía la propuesta P?", "(135000+3*11000)//6", "Se divide el costo total de P entre sus 6 meses de garantía.", " pesos"),
        ("abc", "{F} ¿Cumple la propuesta Q la condición del manual?", "No: sus 168 W suman 14 A, sobre los 12 A permitidos", "Sí: 14 A no supera el fusible de 15 A", "Sí: tiene la garantía más larga", "El límite es el 80 % de 15 A, es decir 12 A, y 14 A lo supera aunque el fusible no se abra."),
        ("abc", "{F} Un compañero dice: «Q es mejor porque cuesta menos por mes de garantía». ¿Qué respuesta es correcta?", "No corresponde: Q no cumple la condición de seguridad y por eso no se compara por costo", "Corresponde: el menor costo por mes siempre decide", "Corresponde si la persona propietaria lo prefiere", "Una propuesta que no cumple la condición técnica queda fuera de la comparación."),
        ("=", "{F} Si en Q se baja el audio a 120 W y la alarma sigue en 24 W, ¿cuántos A normales tendría?", "(120+24)//12", "Se suman las nuevas potencias y se divide entre la tensión.", " A"),
        ("abc", "{F} ¿Qué recomendación corresponde con los datos de la ficha?", "Proponer P, que cumple la condición de 12 A; Q solo sería comparable si se reduce su carga a 12 A o menos", "Proponer Q por su menor costo por mes", "Proponer ambas sin aclarar la condición", "Entre propuestas, primero cuenta el cumplimiento técnico."),
    ],
    ctx=("abc", "Una persona propietaria te pide la propuesta Q «aunque sea con un fusible más grande para que no se corte». ¿Qué respondes?", "Que subir el fusible deja sin protección al cableado; hay que reducir la carga o consultar el manual con personal autorizado", "Que sí, un fusible mayor es más seguro", "Que sí, si el equipo es caro", "Un fusible mayor deja de proteger el cable."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula el 80 % de 20 A?", "Multiplicando por 80 y dividiendo entre 100, es decir 16 A", "20 por 80 es 1.600 y entre 100 es 16."),
        ("¿Qué se verifica antes de comparar costos?", "El cumplimiento de la condición técnica", "Una propuesta que no cumple queda fuera."),
        ("¿Qué se anota de una instalación?", "Una ficha de instalación con sus datos", "Así queda trazabilidad y el trabajo tiene garantía."),
    ],
    op=("Ficha de ejemplo: circuito de 12 V con fusible de 20 A; condición del manual: carga normal a lo más el 80 % del fusible. Propuesta R: audio de 120 W y alarma de 24 W; materiales $90.000, mano de obra 2 horas, garantía de 5 meses. Propuesta S: audio de 192 W y alarma de 24 W. Tarifa: $10.000 por hora. Escribe (a) el límite de corriente de la condición, (b) la corriente de R y de S, (c) cuál cumple, (d) el costo por mes de garantía de la que cumple.",
        "(a) 20 × 80 ÷ 100 = 16 A. (b) R: (120 + 24) ÷ 12 = 12 A; S: (192 + 24) ÷ 12 = 18 A. (c) R cumple porque 12 A no supera 16 A; S no cumple. (d) R: 90.000 + 2 × 10.000 = 110.000; 110.000 ÷ 5 = 22.000 pesos por mes.",
        ["calcula el límite", "calcula las corrientes", "decide cuál cumple", "calcula el costo por mes"],
        ["hoja con las cuatro respuestas"],
        ["decir que S cumple porque no supera el fusible", "olvidar la mano de obra", "dividir mal"],
        "Pregunta: «¿el límite es el fusible o el 80 % del fusible?». Si duda, pídele que relea la condición del manual."),
    reinforce="Inventa un fusible, una condición del 80 % y dos propuestas, y decide cuál cumple.",
    extend="Explica con un ejemplo por qué una propuesta barata que no cumple no se debe elegir.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (inventario mensual de residuos de ejemplo, inventado) del «Taller Verde Demo». Aceite usado, 120 L; líquido refrigerante usado, 40 L; filtros de aceite usados, 30 unidades; baterías de plomo-ácido fuera de uso, 6 unidades; neumáticos fuera de uso, 20 unidades; "
     "trapos con aceite, 15 kg; envases vacíos de aceite, 25 unidades; chatarra metálica, 80 kg. El taller tiene un contenedor de aceite usado de 200 L de capacidad.")
build(
    O8, 1, F,
    use="Aprenderé qué residuos genera el mantenimiento de vehículos, cuáles son peligrosos, cómo se ordena su manejo y por qué se entregan a un gestor autorizado.",
    prior=["Sé sumar, restar y multiplicar números enteros.", "Sé qué es un peligro y un riesgo.", "Sé que algunos productos contaminan el agua y el suelo."],
    explain=[
        "Un residuo es un material que se desecha. Un residuo peligroso es el que, por sus propiedades, puede dañar la salud o el ambiente, por ejemplo por ser tóxico, inflamable o corrosivo. En el mantenimiento de vehículos suelen ser peligrosos el aceite usado, las baterías de plomo-ácido, los filtros y trapos con aceite y los líquidos refrigerantes usados; los neumáticos y la chatarra son, en general, no peligrosos, pero tienen una gestión específica. La clasificación exacta la fija la norma vigente.",
        "La jerarquía de manejo ordena las acciones de lo preferible a lo menos preferible: prevenir, reducir, reutilizar, reciclar, valorizar y, al final, eliminar. Los residuos se separan, se rotulan, se guardan en contenedores cerrados y se entregan a un gestor autorizado, una empresa autorizada para retirarlos, transportarlos y tratarlos, con un documento de entrega. Nunca se vierten en desagües ni en el suelo. Un derrame puede causar resbalones, incendio y contaminación.",
        f"La autoridad sanitaria y la ambiental fiscalizan el manejo de residuos según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("residuo", "material que se desecha"), ("residuo peligroso", "residuo que puede dañar la salud o el ambiente"), ("gestor autorizado", "empresa autorizada para retirar, transportar y tratar residuos"), ("jerarquía de manejo", "orden: prevenir, reducir, reutilizar, reciclar, valorizar y eliminar"), ("rótulo", "etiqueta que indica el contenido de un contenedor"), ("derrame", "salida de un líquido fuera de su contenedor")],
    worked=[
        ("Clasificar", "Un taller de ejemplo tiene líquido de frenos usado. Por ser un fluido usado que contamina el agua, ¿cómo se clasifica en general?", ["Un fluido usado que contamina el agua y daña el ambiente es peligroso.", "Se separa, se rotula y se entrega a un gestor autorizado."], "Residuo peligroso"),
        ("Jerarquía", "Un taller de ejemplo puede reutilizar un envase limpio o eliminarlo. Según la jerarquía de manejo, ¿qué es preferible?", ["Reutilizar va antes que eliminar en la jerarquía.", "Eliminar es la última opción."], "Reutilizarlo"),
    ],
    mistakes=[("Pensar que un residuo líquido se puede verter en el desagüe «porque se diluye».", "Contamina el agua y el suelo y es una infracción a la norma.", "Se guarda en un contenedor cerrado y se entrega a un gestor autorizado."),
              ("Mezclar todos los residuos en un solo contenedor para ahorrar espacio.", "La mezcla puede aumentar el peligro y complica el tratamiento.", "Cada tipo de residuo se separa y se rotula.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es un residuo peligroso?", "Un residuo que por sus propiedades puede dañar la salud o el ambiente, como el aceite usado", "Un residuo que pesa mucho", "Un residuo que se puede vender", "El peligro depende de sus propiedades, no de su peso ni de su valor."),
        ("abc", "En Mecánica Automotriz: ¿cuál es el orden de la jerarquía de manejo de residuos, de lo preferible a lo menos preferible?", "Prevenir, reducir, reutilizar, reciclar, valorizar y eliminar", "Eliminar, reciclar, reutilizar y prevenir", "Reciclar, eliminar, prevenir, reutilizar y reducir", "La jerarquía parte por evitar generar residuos y termina en eliminar."),
        ("abc", "En Mecánica Automotriz: ¿qué es un gestor autorizado de residuos?", "Una empresa autorizada para retirar, transportar y tratar residuos", "Cualquier persona que acepte llevarse los residuos", "El taller que generó los residuos", "El gestor debe tener autorización; no basta con que alguien los retire."),
        ("abc", "{F} ¿Cuál de estos residuos del inventario se registra en litros?", "El aceite usado", "Los neumáticos fuera de uso", "La chatarra metálica", "El aceite es un líquido; los neumáticos se cuentan en unidades y la chatarra en kilos."),
        ("abc", "{F} ¿Qué riesgo especial tienen las baterías de plomo-ácido fuera de uso?", "Contienen plomo y ácido, que contaminan y pueden causar quemaduras", "Se incendian solas cuando están frías", "No tienen ningún riesgo si ya no funcionan", "Aunque no funcionen, conservan plomo y ácido."),
        ("abc", "{F} ¿Cuál de estos residuos se considera, en general, no peligroso aunque requiere una gestión específica?", "Los neumáticos fuera de uso", "El aceite usado", "Las baterías de plomo-ácido", "El aceite y las baterías son peligrosos; los neumáticos tienen gestión específica."),
        ("=", "{F} ¿Cuántos L de fluidos usados, entre aceite y líquido refrigerante, hay en el inventario?", "120+40", "Se suman los litros de aceite usado y de líquido refrigerante.", " L"),
        ("=", "{F} ¿Cuántos L le faltan al contenedor de aceite usado para llenarse?", "200-120", "Se resta el aceite almacenado a la capacidad del contenedor.", " L"),
        ("=", "{F} Si el taller genera 120 L de aceite usado cada mes, ¿cuántos L genera en un año de 12 meses?", "120*12", "Se multiplica el aceite del mes por los 12 meses.", " L"),
        ("abc", "{F} Un compañero propone mezclar el aceite usado con el líquido refrigerante usado «para llenar un solo contenedor». ¿Qué respuesta es correcta?", "No corresponde: los residuos se separan y se rotulan, porque mezclarlos puede aumentar el peligro y complica su tratamiento", "Corresponde, porque así se ocupa menos espacio", "Corresponde, si el contenedor tiene tapa", "La mezcla de residuos distintos no es una práctica segura ni ordenada."),
        ("abc", "En una visita a un taller de ejemplo, un charco de aceite se extiende hacia un desagüe. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Lavarlo con agua para que baje por el desagüe", "Cubrirlo con aserrín y botarlo con la basura común", "Un derrame se informa a quienes pueden actuar y no se lava ni se bota como basura común."),
        ("=", "{F} El contenedor de aceite usado se retira cuando llega a 180 L, con una generación de 120 L al mes. ¿Cuántos retiros hay en 12 meses?", "(12*120)//180","Se calculan los litros del año y se dividen entre la capacidad de cada retiro.", " retiros"),
        ("abc", "¿Cuál es el rótulo más completo, de ejemplo, para un contenedor de aceite usado?", "«Aceite usado, residuo peligroso, taller y fecha de inicio de acumulación»", "«Líquido»", "«Basura del taller»", "Un buen rótulo dice qué contiene, qué peligro tiene y desde cuándo se acumula."),
    ],
    ctx=("abc", "Un vecino de ejemplo te pide el aceite usado del taller «para pintar su cerca de madera». ¿Qué respondes?", "Que el aceite usado es un residuo peligroso que solo se entrega a un gestor autorizado, no a particulares para usos informales", "Que sí, porque así se reutiliza", "Que sí, si lleva su propio envase", "Un uso informal del aceite usado contamina y puede causar un accidente."),
    sc=[
        ("En Mecánica Automotriz: ¿a quién se entregan los residuos peligrosos del taller?", "A un gestor autorizado", "Solo una empresa autorizada puede retirarlos y tratarlos."),
        ("¿Qué es lo primero en la jerarquía de manejo?", "Prevenir la generación de residuos", "Lo mejor es no generar el residuo."),
        ("¿Dónde nunca se vierte un residuo líquido?", "En desagües ni en el suelo", "Contamina el agua y el suelo."),
    ],
    op=("Ficha de ejemplo: inventario de un taller: aceite usado, 90 L; baterías de plomo-ácido, 4 unidades; filtros usados, 20 unidades; solvente usado, 10 L; neumáticos fuera de uso, 12 unidades. Escribe (a) cuáles son peligrosos y cuál no lo es en general, (b) cuántos L de líquidos usados hay, (c) un rótulo para el aceite usado, (d) a quién se entregan y qué nunca se hace con los líquidos.",
        "(a) Peligrosos: aceite, baterías, filtros con aceite y solvente; no peligrosos en general: los neumáticos, que requieren gestión específica. (b) 90 + 10 = 100 L. (c) «Aceite usado, residuo peligroso, taller y fecha de inicio de acumulación». (d) Se entregan a un gestor autorizado; nunca se vierten en desagües ni en el suelo.",
        ["clasifica los residuos", "suma los litros", "redacta un rótulo", "indica el destino y lo que nunca se hace"],
        ["hoja con las cuatro respuestas"],
        ["clasificar los neumáticos como peligrosos", "olvidar el solvente al sumar", "proponer verter un líquido en el desagüe"],
        "Pregunta: «¿este residuo puede dañar la salud o el ambiente?». Si duda, pídele que relea la definición de residuo peligroso."),
    reinforce="Escribe cuatro residuos de un taller de vehículos y marca cuáles son peligrosos.",
    extend="Explica con un ejemplo por qué prevenir un residuo es mejor que reciclarlo.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados) del «Taller Verde Demo». Hoja de datos de seguridad (HDS) del «Aceite de motor Demo»: peligros, irritación de la piel y contaminante del agua; manejo, guardar en envase cerrado y rotulado, lejos de llamas; eliminación, entregar a un gestor autorizado. "
     "Registro mensual de aceite usado entregado al gestor: semana 1, 40 L; semana 2, 60 L; semana 3, 20 L; semana 4, 30 L. El inventario del mes indica que se generaron 160 L. Documento de entrega de ejemplo: anota fecha, tipo y cantidad del residuo, gestor y firmas.")
build(
    O8, 2, F,
    use="Aprenderé qué documentos respaldan el manejo de residuos: la hoja de datos de seguridad, las etiquetas, el rótulo del contenedor y el registro y documento de entrega.",
    prior=["Sé sumar y restar números enteros.", "Sé qué es un residuo peligroso.", "Sé qué es un gestor autorizado."],
    explain=[
        "La hoja de datos de seguridad (HDS) es un documento del proveedor que describe los peligros de un producto y las medidas generales de manejo y de eliminación. La etiqueta del envase trae el nombre del producto, pictogramas y advertencias; un pictograma de peligro es un símbolo que indica el tipo de peligro, como inflamable, corrosivo, tóxico o dañino para el ambiente. El rótulo del contenedor de un residuo indica su contenido y desde cuándo se acumula.",
        "El registro mensual anota cuánto residuo se generó y cuánto se entregó, y el documento de entrega deja constancia de la fecha, el tipo y la cantidad de residuo, el gestor y las firmas. Con estos documentos se demuestra la trazabilidad del residuo: de dónde sale, adónde va y quién lo recibe. Un registro con huecos no demuestra nada. Las HDS deben estar accesibles y el personal debe saber consultarlas antes de usar o desechar un producto.",
        f"Esta clase lee y completa documentos en papel; el manejo real lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("hoja de datos de seguridad (HDS)", "documento del proveedor con los peligros y el manejo de un producto"), ("pictograma", "símbolo que indica un tipo de peligro"), ("etiqueta", "información impresa en el envase de un producto"), ("rótulo de residuo", "etiqueta del contenedor con su contenido y fecha"), ("trazabilidad", "poder seguir el origen, el destino y el receptor de un residuo"), ("documento de entrega", "constancia de que un residuo se entregó a un gestor")],
    worked=[
        ("Qué documento", "Se quiere saber qué peligros tiene un producto y cómo desecharlo. ¿Qué documento se consulta primero?", ["Ese documento lo entrega el proveedor del producto.", "Es la hoja de datos de seguridad."], "La hoja de datos de seguridad (HDS)"),
        ("Sumar entregas", "Un registro de ejemplo anota entregas de 25 L y 35 L de un residuo. ¿Cuántos L suma?", ["Se suman las dos entregas.", "25 más 35 son 60."], "60 L"),
    ],
    mistakes=[("Dejar sin anotar una entrega porque «ya se sabe cuánto fue».", "Un registro con huecos no demuestra la trazabilidad del residuo.", "Anota cada entrega con su fecha, tipo y cantidad."),
              ("Archivar las HDS donde nadie las consulta.", "Deben estar accesibles antes de usar o desechar un producto.", "Déjalas a mano y capacita al personal para leerlas.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es una hoja de datos de seguridad (HDS)?", "Un documento del proveedor que describe los peligros de un producto y las medidas generales de manejo", "Una factura de compra del producto", "Un plano del taller", "La HDS informa peligros y manejo del producto; la factura y el plano son otros documentos."),
        ("abc", "En Mecánica Automotriz: ¿qué indica un pictograma de peligro en una etiqueta?", "El tipo de peligro del producto, con un símbolo", "El precio del producto", "La fecha de fabricación", "El pictograma es un símbolo de advertencia."),
        ("abc", "En Mecánica Automotriz: ¿qué debe registrar un documento de entrega de residuos?", "La fecha, el tipo y la cantidad del residuo, el gestor y las firmas", "Solo el nombre del taller", "El color de los contenedores", "Con esos datos se demuestra a quién se entregó, qué y cuánto."),
        ("abc", "{F} ¿Qué peligros indica la HDS de ejemplo?", "Irritación de la piel y contaminación del agua", "Explosión al contacto con agua", "Ningún peligro", "La HDS de la ficha nombra la irritación de la piel y el daño al agua."),
        ("abc", "{F} ¿Qué dice la HDS de ejemplo sobre la eliminación?", "Entregarlo a un gestor autorizado", "Verterlo en el desagüe diluido", "Quemarlo en el patio", "La HDS indica la entrega a un gestor autorizado."),
        ("abc", "{F} ¿Quién retira los residuos según el documento de entrega?", "El gestor autorizado", "El mismo taller", "Cualquier persona que pase", "El documento de entrega registra al gestor que recibe el residuo."),
        ("=", "{F} ¿Cuántos L de aceite usado se entregaron en las cuatro semanas?", "40+60+20+30", "Se suman las entregas de las cuatro semanas.", " L"),
        ("=", "{F} ¿Cuántos L más se entregaron en la semana 2 que en la semana 3?", "60-20", "Se resta la entrega de la semana 3 a la de la semana 2.", " L"),
        ("=", "{F} Se generaron 160 L en el mes. ¿Cuántos L quedan sin entregar?", "160-(40+60+20+30)", "Se restan los litros entregados a los generados.", " L"),
        ("abc", "{F} Un compañero dice: «si falta una semana en el registro no importa, se entrega todo igual». ¿Qué respuesta es correcta?", "Es falso: el registro debe reflejar cada entrega para demostrar la trazabilidad del residuo", "Es cierto, porque lo importante es el último retiro", "Es cierto, si el gestor es conocido", "Un registro con huecos no demuestra qué pasó con el residuo."),
        ("abc", "Un contenedor de residuo llega al patio del taller sin rótulo. ¿Qué corresponde?", "No manipularlo ni mezclarlo y avisar al encargado, para que se identifique su contenido y se rotule", "Dejarlo sin rótulo, porque ya se sabe qué lleva", "Mezclarlo con el contenedor más cercano", "Sin rótulo no hay trazabilidad, y adivinar el contenido o mezclarlo puede ser peligroso."),
        ("=", "{F} El gestor cobra $150 por litro retirado. ¿Cuántos pesos cuesta el retiro de lo entregado en el mes?", "(40+60+20+30)*150", "Se suman los litros entregados y se multiplican por el costo por litro.", " pesos"),
        ("abc", "{F} ¿Qué anotación del documento de entrega corresponde a la semana 4?", "Semana 4: aceite usado, 30 L, entregado al gestor autorizado, con fecha y firmas", "Aceite, algunos litros, entregado a un vecino", "Residuos varios, sin cantidad", "La anotación completa tiene tipo, cantidad, destino, fecha y firmas."),
    ],
    ctx=("abc", "Una persona del taller te dice que «las HDS están en una carpeta que nadie lee». ¿Qué propones?", "Dejarlas accesibles y capacitar al personal para consultarlas antes de usar o desechar un producto", "Archivarlas en una bodega cerrada", "Imprimir solo las HDS de los productos más baratos", "Una HDS solo sirve si el personal puede y sabe consultarla."),
    sc=[
        ("En Mecánica Automotriz: ¿qué muestra la trazabilidad de un residuo?", "De dónde sale, adónde va y quién lo recibe", "Se logra con registro y documento de entrega."),
        ("¿Qué indica un pictograma?", "El tipo de peligro de un producto", "Es un símbolo que advierte un tipo de peligro."),
        ("¿Qué debe llevar el rótulo de un contenedor de residuo?", "Su contenido y desde cuándo se acumula", "Así se sabe qué hay y cuánto tiempo lleva."),
    ],
    op=("Ficha de ejemplo: HDS del «Refrigerante Demo»: peligros, irritación de los ojos y contaminante del agua; eliminación, entregar a un gestor autorizado. Registro: entregas de refrigerante usado de 20 L en la semana 1 y de 30 L en la semana 3; se generaron 70 L en el mes. Escribe (a) los peligros de la HDS, (b) el destino de la eliminación, (c) cuántos L se entregaron y cuántos quedan sin entregar, (d) qué documento deja constancia de cada entrega.",
        "(a) Irritación de los ojos y contaminación del agua. (b) Entregar a un gestor autorizado. (c) 20 + 30 = 50 L entregados; 70 − 50 = 20 L sin entregar. (d) El documento de entrega, con fecha, tipo y cantidad, gestor y firmas.",
        ["lee los peligros en la HDS", "indica el destino", "calcula lo entregado y lo pendiente", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["olvidar una entrega al sumar", "decir que se vierte en un desagüe", "no nombrar el documento de entrega"],
        "Pregunta: «¿de dónde saco los peligros y el destino?». Si duda, pídele que relea lo que dice la HDS de la ficha."),
    reinforce="Inventa un registro de cuatro entregas de un residuo y suma lo entregado.",
    extend="Explica con un ejemplo por qué un registro incompleto puede ser un problema aunque el residuo sí se haya entregado.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (observaciones de una visita de ejemplo, inventadas) al «Taller Verde Demo». (1) El aceite usado se guarda en un tambor de 200 L sin tapa y sin rótulo; contiene 135 L. (2) El aceite y el solvente usados están mezclados en un mismo envase. "
     "(3) Seis baterías fuera de uso están apiladas sobre el piso de tierra. (4) Los trapos con aceite están en un contenedor con tapa y rótulo y se entregan al gestor. (5) Los neumáticos fuera de uso se entregan a un gestor autorizado, con documento. "
     "Criterios de ejemplo: separar los residuos; contenedor cerrado y rotulado; piso impermeable; entrega a gestor autorizado con documento.")
build(
    O8, 3, F,
    use="Aprenderé a evaluar en papel las prácticas de manejo de residuos de un taller, a compararlas con criterios y a redactar un informe de observaciones con acciones sugeridas.",
    prior=["Sé qué es un residuo peligroso.", "Sé qué documentos respaldan un residuo.", "Sé calcular con números enteros."],
    explain=[
        "Un informe de observación de una visita anota el hecho observado, el criterio con que se compara, el riesgo que implica y una acción sugerida. Los criterios de ejemplo de esta clase son: separar los residuos, guardarlos en contenedores cerrados y rotulados, sobre piso impermeable, y entregarlos a un gestor autorizado con documento. Una práctica que cumple se anota como tal; una que no cumple se informa al encargado, sin corregirla por cuenta propia.",
        "Los residuos líquidos se guardan en contenedores cerrados y rotulados porque un tambor abierto puede derramarse, evaporar sustancias o mezclarse con otros residuos. Las baterías sobre tierra pueden contaminar el suelo con plomo y ácido. Mezclar residuos distintos aumenta el peligro y complica el tratamiento. Los incumplimientos se registran con plazos y responsables, porque sin registro no hay seguimiento.",
        f"Esta clase evalúa informes escritos; la corrección real la hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("observación", "hecho que se ve en una visita"), ("criterio", "regla con que se compara lo observado"), ("incumplimiento", "práctica que no cumple un criterio"), ("acción sugerida", "medida que se propone al encargado"), ("contención ante derrames", "recipiente o bandeja que retiene un líquido que se derrama")],
    worked=[
        ("Observación contra criterio", "Una visita de ejemplo observa un envase de pintura usada con tapa pero sin rótulo. El criterio dice «contenedor cerrado y rotulado». ¿Cumple?", ["El criterio pide un contenedor cerrado y también rotulado.", "Al envase le falta el rótulo."], "No cumple"),
        ("Una buena práctica", "Una visita de ejemplo observa que un residuo se entrega a un gestor autorizado con documento. ¿Cumple el criterio de entrega?", ["El criterio pide gestor autorizado y documento.", "Ambos se observan."], "Sí, cumple"),
    ],
    mistakes=[("Corregir una práctica por cuenta propia durante la visita.", "Puede ser peligroso y no deja registro del hecho.", "Se informa al encargado con el hecho, el criterio y el riesgo."),
              ("Anotar solo una opinión como «está mal».", "Un informe necesita hecho, criterio, riesgo y acción sugerida.", "Escribe los cuatro elementos.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo debe almacenarse, en general, un residuo líquido peligroso?", "En un contenedor cerrado, rotulado y con contención ante derrames", "En cualquier envase abierto para que se evapore", "Al aire libre sobre tierra", "Un contenedor cerrado y rotulado evita derrames, mezclas y emanaciones."),
        ("abc", "En Mecánica Automotriz: ¿por qué no se mezclan residuos distintos?", "Porque la mezcla puede aumentar el peligro y complica su tratamiento", "Porque así se ocupa más espacio", "Porque el gestor cobra menos", "Mezclar residuos distintos puede volverlos más peligrosos y más difíciles de tratar."),
        ("abc", "En Mecánica Automotriz: ¿qué elementos debe tener un informe de observación de una visita?", "El hecho observado, el criterio, el riesgo y una acción sugerida", "Solo la opinión de quien visita", "Solo la lista de personas del taller", "Con esos cuatro elementos el informe permite decidir."),
        ("abc", "{F} ¿Qué observación cumple el criterio de entrega a un gestor autorizado con documento?", "La observación 5", "La observación 1", "La observación 3", "Los neumáticos se entregan a un gestor autorizado con documento."),
        ("abc", "{F} ¿Qué criterio incumple la observación 2?", "Separar los residuos", "Entregar con documento", "Tener piso impermeable", "El aceite y el solvente están mezclados en un mismo envase."),
        ("abc", "{F} ¿Qué riesgo principal tiene la observación 3?", "Contaminación del suelo con plomo y ácido de las baterías", "Ruido excesivo", "Pérdida de documentos", "Las baterías sobre tierra pueden filtrar sus contenidos al suelo."),
        ("=", "{F} De las 5 observaciones, 2 cumplen los criterios. ¿Cuántas no los cumplen?", "5-2", "Se resta al total las observaciones que cumplen.", " observaciones"),
        ("=", "{F} ¿Cuántos L de espacio libre quedan en el tambor de aceite usado de la observación 1?", "200-135", "Se resta el aceite que contiene a la capacidad del tambor.", " L"),
        ("=", "{F} Las 6 baterías de la observación 3 se reparten en 2 contenedores con la misma cantidad. ¿Cuántas baterías van en cada contenedor?", "6//2", "Se divide el total de baterías entre los 2 contenedores.", " baterías"),
        ("abc", "{F} Un compañero dice: «como los neumáticos van al gestor, el taller ya cumple todo». ¿Qué respuesta es correcta?", "Es falso: la observación 5 cumple, pero las observaciones 1, 2 y 3 incumplen y deben corregirse", "Es cierto: un buen manejo compensa los demás", "Es cierto, porque los neumáticos son lo más importante", "Un cumplimiento no compensa otros incumplimientos."),
        ("abc", "El jefe de un taller dice que corregirá lo observado «cuando haya tiempo», sin dejar registro. ¿Qué corresponde?", "Anotar plazos y responsables por escrito, porque sin registro no hay seguimiento", "Confiar en que se hará", "Esperar a la próxima fiscalización", "El registro de plazos y responsables permite verificar que se corrija."),
        ("=", "{F} Corregir cada incumplimiento requiere 4 horas a $8.000 la hora. ¿Cuántos pesos cuesta corregir los incumplimientos observados?", "3*4*8000", "Hay 3 incumplimientos: se multiplican por las horas y la tarifa.", " pesos"),
        ("abc", "{F} ¿Qué acción sugerida es la más adecuada para la observación 2?", "Informar al encargado para que los residuos se separen, se rotulen y se entreguen al gestor autorizado según su tipo", "Dejar la mezcla y rotularla como «aceite»", "Entregar la mezcla a quien la quiera", "La acción sugerida respeta separación, rótulo y gestor autorizado."),
    ],
    ctx=("abc", "Una persona del taller te pide que quemes los trapos con aceite en el patio para deshacerte de ellos. ¿Qué respondes?", "Que no: quemar residuos es peligroso y contamina, y se entregan a un gestor autorizado", "Que sí, si es poca cantidad", "Que sí, si hay viento", "Quemar residuos genera humo tóxico y riesgo de incendio."),
    sc=[
        ("En Mecánica Automotriz: ¿qué se compara en un informe de observación?", "El hecho observado con un criterio", "El criterio permite decidir si cumple."),
        ("¿Qué se hace con un incumplimiento visto en la visita?", "Se informa al encargado, sin corregirlo por cuenta propia", "Se registra y se asignan plazo y responsable."),
        ("¿Por qué no se apilan baterías sobre tierra?", "Porque pueden contaminar el suelo", "Contienen plomo y ácido que contaminan el suelo."),
    ],
    op=("Ficha de ejemplo: observaciones de otro taller. (1) El solvente usado está en un envase abierto de 20 L que contiene 12 L. (2) El aceite usado se entrega a un gestor autorizado con documento. (3) Los filtros usados están en una caja de cartón sin rótulo, sobre el piso. Criterios: contenedor cerrado y rotulado; entrega a gestor con documento. Escribe (a) cuáles cumplen y cuáles no, (b) cuántos L de espacio libre tiene el envase de la observación 1, (c) el riesgo de la observación 3, (d) una acción sugerida para la observación 1.",
        "(a) La 2 cumple; la 1 y la 3 no cumplen. (b) 20 − 12 = 8 L. (c) Que los filtros con aceite contaminen el piso y el suelo y que se pierda su trazabilidad. (d) Informar al encargado para que el solvente quede en un contenedor cerrado y rotulado y se entregue a un gestor autorizado.",
        ["clasifica las observaciones", "calcula el espacio libre", "explica el riesgo", "propone una acción sugerida sin corregir por cuenta propia"],
        ["hoja con las cuatro respuestas"],
        ["decir que la 3 cumple", "calcular mal el espacio libre", "proponer corregirlo uno mismo"],
        "Pregunta: «¿cuál es el criterio que se compara con cada observación?». Si duda, pídele que relea los criterios de la ficha."),
    reinforce="Escribe tres observaciones inventadas de un taller y marca cuáles cumplen y cuáles no.",
    extend="Explica con un ejemplo por qué un informe necesita criterio y riesgo y no solo una opinión.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (plan de residuos de ejemplo, inventado) del «Taller Verde Demo». Genera por semana: aceite usado, 25 L; líquido refrigerante usado, 10 L; filtros de aceite usados, 6 unidades; baterías fuera de uso, 1 unidad. "
     "Contenedor de aceite usado, 200 L; contenedor de refrigerante usado, 40 L. El gestor autorizado retira cuando un contenedor se llena o cada 8 semanas como máximo, lo que ocurra primero. Costo de ejemplo de cada retiro: $40.000. Un año de trabajo del taller tiene 48 semanas.")
build(
    O8, 4, F,
    use="Aprenderé a planificar los retiros de residuos con números: en cuántas semanas se llena un contenedor, cuántos retiros hay al año y cuánto se ahorra al coordinarlos.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es un gestor autorizado.", "Sé calcular un costo anual."],
    explain=[
        "Para planificar se calcula primero en cuántas semanas se llena un contenedor, dividiendo su capacidad entre los litros que se generan por semana. El gestor retira cuando el contenedor se llena o cuando se cumple el plazo máximo, lo que ocurra primero. El número de retiros al año es el número de semanas del año dividido por las semanas entre retiros, y el costo es ese número por el costo de cada retiro.",
        "Coordinar los retiros de distintos residuos en una sola visita reduce viajes y costos, siempre que ningún contenedor se llene antes del retiro. Reducir es generar menos residuo desde el origen. No se retrasan los retiros ni se excede la capacidad de un contenedor para ahorrar dinero: un contenedor desbordado es un derrame y una infracción. Los residuos que esperan se guardan cerrados, rotulados y bajo techo.",
        f"Esta clase planifica con números; el manejo real lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("capacidad", "volumen máximo que cabe en un contenedor"), ("retiro", "visita del gestor para llevarse los residuos"), ("reducir", "generar menos residuo desde el origen"), ("coordinar", "juntar en una sola visita lo que se puede retirar junto"), ("plazo máximo", "tiempo máximo que puede esperar un residuo")],
    worked=[
        ("Tiempo de llenado", "Un contenedor de ejemplo de 120 L recibe 15 L por semana. ¿En cuántas semanas se llena?", ["Se divide la capacidad entre los litros por semana.", "120 entre 15 son 8."], "En 8 semanas"),
        ("Retiros al año", "Un taller de ejemplo tiene un retiro cada 6 semanas y trabaja 48 semanas al año. ¿Cuántos retiros hay?", ["Se divide el año entre las semanas de cada retiro.", "48 entre 6 son 8."], "8 retiros"),
    ],
    mistakes=[("Dejar que un contenedor se llene por encima de su capacidad para ahorrar un retiro.", "Un contenedor desbordado es un derrame y una infracción.", "El retiro se programa antes de que se llene."),
              ("Mezclar residuos para coordinar mejor los retiros.", "Coordinar es juntar retiros, no mezclar residuos.", "Cada residuo mantiene su contenedor y su rótulo.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula en cuántas semanas se llena un contenedor?", "Dividiendo su capacidad entre los litros que se generan por semana", "Multiplicando su capacidad por los litros semanales", "Restando los litros semanales a la capacidad", "El tiempo de llenado es la capacidad dividida por la generación semanal."),
        ("abc", "En Mecánica Automotriz: ¿por qué conviene coordinar los retiros de distintos residuos con el mismo gestor?", "Porque reduce los viajes y su costo, sin dejar que ningún contenedor se llene", "Porque así se pueden mezclar los residuos", "Porque el gestor retira sin documento", "Coordinar ahorra viajes; no cambia las reglas de separación ni de documento."),
        ("abc", "En Mecánica Automotriz: ¿qué significa «reducir» en la jerarquía de manejo de residuos?", "Generar menos residuo desde el origen", "Comprimir el residuo para que ocupe menos", "Mezclarlo con otro para usar un solo contenedor", "Reducir actúa sobre la generación y no sobre el volumen del residuo ya generado."),
        ("abc", "{F} ¿Qué datos de la ficha permiten saber cada cuánto se llena el contenedor de aceite?", "La capacidad del contenedor y los litros generados por semana", "Las baterías por semana", "El costo de cada retiro", "El llenado depende de capacidad y generación."),
        ("abc", "{F} ¿Qué contenedor se llena antes?", "El de refrigerante", "El de aceite", "Ninguno, porque se retiran siempre cada 8 semanas", "El de refrigerante se llena en 4 semanas y el de aceite en 8."),
        ("abc", "{F} ¿Qué condición fija el gestor para retirar?", "Cuando un contenedor se llena o cada 8 semanas como máximo, lo que ocurra primero", "Solo cuando el taller lo pide", "Solo cada 8 semanas exactas", "La regla toma el primer plazo o llenado que ocurra."),
        ("=", "{F} ¿En cuántas semanas se llena el contenedor de aceite usado?", "200//25", "Se divide la capacidad entre los litros generados por semana.", " semanas"),
        ("=", "{F} ¿En cuántas semanas se llena el contenedor de refrigerante usado?", "40//10", "Se divide la capacidad entre los litros generados por semana.", " semanas"),
        ("=", "{F} ¿Cuántos filtros de aceite usados genera el taller en 12 semanas?", "6*12", "Se multiplican los filtros semanales por las semanas.", " filtros"),
        ("abc", "{F} Con retiros separados por contenedor en un año de 48 semanas, ¿cuántos retiros necesita el taller?", "6 de aceite y 12 de refrigerante, es decir 18 retiros", "12 de aceite y 6 de refrigerante, es decir 18 retiros", "6 retiros en total, porque el aceite es lo principal", "El aceite se retira cada 8 semanas y el refrigerante cada 4."),
        ("abc", "{F} Con retiros conjuntos cada 4 semanas, ¿hay riesgo de que el contenedor de aceite se llene antes?", "No: en 4 semanas el aceite llega a 100 L, bajo sus 200 L", "Sí, porque el aceite se llena en 4 semanas", "Sí, porque los retiros conjuntos no se permiten", "100 L son la mitad de la capacidad del contenedor de aceite."),
        ("=", "{F} ¿Cuántos pesos se ahorran en 48 semanas con retiros conjuntos cada 4 semanas, frente a los retiros separados?", "(6+12)*40000-12*40000", "Se resta el costo de los retiros conjuntos al de los separados.", " pesos"),
        ("abc", "{F} ¿Qué decisión de plan es más adecuada?", "Coordinar retiros conjuntos cada 4 semanas, registrar cada entrega y revisar que ningún contenedor supere su capacidad", "Retirar solo cuando el gestor pase por el sector", "Dejar que el contenedor de aceite pase su capacidad para ahorrar un retiro", "El plan coordina, registra y respeta la capacidad."),
    ],
    ctx=("abc", "Una persona propone guardar los filtros usados en el patio hasta «juntar muchos». ¿Qué respondes?", "Que se guardan en contenedores cerrados y rotulados, bajo techo, con un plazo máximo acordado con el gestor, y se registran", "Que sí, mientras no huelan", "Que sí, apilados sobre la tierra", "Los filtros con aceite contaminan y deben guardarse en contenedores adecuados."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula cuántos retiros hay al año?", "Dividiendo las semanas del año entre las semanas de cada retiro", "Muestra cuántas veces cabe el intervalo en el año."),
        ("¿Qué ocurre si un contenedor se llena sobre su capacidad?", "Hay riesgo de derrame y una infracción", "Un contenedor desbordado no cumple la norma."),
        ("¿Qué ahorra coordinar retiros?", "Viajes y costo, sin mezclar residuos", "Se juntan las visitas del gestor."),
    ],
    op=("Ficha de ejemplo: un taller genera por semana 30 L de aceite usado, con un contenedor de 240 L, y 8 L de refrigerante usado, con un contenedor de 40 L. Cada retiro cuesta $30.000 y el año tiene 40 semanas de trabajo. Escribe (a) en cuántas semanas se llena cada contenedor, (b) cuántos retiros y cuántos pesos cuestan con retiros separados, (c) cuántos retiros y cuántos pesos cuestan con retiros conjuntos cada 5 semanas, (d) cuánto se ahorra y qué se verifica del contenedor de aceite.",
        "(a) Aceite: 240 ÷ 30 = 8 semanas; refrigerante: 40 ÷ 8 = 5 semanas. (b) 40 ÷ 8 = 5 retiros de aceite y 40 ÷ 5 = 8 de refrigerante: 13 retiros, 390.000 pesos. (c) 40 ÷ 5 = 8 retiros: 240.000 pesos. (d) Se ahorran 150.000 pesos; se verifica que en 5 semanas el aceite llegue a 150 L, bajo sus 240 L.",
        ["calcula los tiempos de llenado", "calcula retiros y costo separados", "calcula retiros y costo conjuntos", "calcula el ahorro y verifica la capacidad"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar los retiros del aceite", "no verificar la capacidad"],
        "Pregunta: «¿cuántas veces cabe el plazo en el año?». Si duda, pídele que relea cómo se calculan los retiros al año."),
    reinforce="Inventa un contenedor, una generación semanal y calcula en cuántas semanas se llena y cuántos retiros hay en 48 semanas.",
    extend="Explica con un ejemplo por qué ahorrar un retiro no justifica llenar un contenedor sobre su capacidad.",
)

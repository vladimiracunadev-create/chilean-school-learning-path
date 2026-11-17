"""Electricidad TP 3.º y 4.º medio: OAE-04 (calefacción y fuerza motriz de hasta 5 kW: documentos y cálculos), OAE-05 (cubicación) y OAE-06 (mantenimiento: planificación, documentos y prevención). Solo conceptos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_elec_common import AVISO, EMER, build

O4 = "TP-ELEC-3y4-OAE-04"
O5 = "TP-ELEC-3y4-OAE-05"
O6 = "TP-ELEC-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). «Taller Cobre» (ficticio) tiene una estufa eléctrica de 2000 W, una bomba de agua con motor de 750 W y un ventilador de 250 W. "
     "El OA nombra instalaciones de calefacción y fuerza motriz de hasta 5 kW de potencia total instalada, sin alimentadores. Tensión de ejemplo: 220 V. "
     "Riesgos anotados: quemadura, incendio por sobrecalentamiento y partes en movimiento.")
build(
    O4, 1, F,
    use="Aprenderé qué son la calefacción eléctrica y la fuerza motriz, qué límite de potencia nombra el objetivo y qué riesgos tienen, sin intervenir ningún equipo.",
    prior=["Sé qué es la potencia en vatios.", "Sé pasar de W a kW.", "Sé que los documentos de un proyecto deben coincidir."],
    explain=[
        "La calefacción eléctrica convierte energía eléctrica en calor: una estufa tiene una resistencia que se calienta. La fuerza motriz usa motores eléctricos para producir movimiento, como el de una bomba o un ventilador: el motor convierte energía eléctrica en movimiento. El objetivo de aprendizaje habla de instalaciones de baja tensión con hasta 5 kW de potencia total instalada y sin alimentadores. La potencia total instalada es la suma de las potencias de todos los equipos conectados; 1 kW son 1000 W.",
        "Estos equipos tienen riesgos propios, además de la descarga eléctrica: la quemadura por superficies calientes, el incendio por sobrecalentamiento si hay materiales combustibles cerca, y el atrapamiento por partes en movimiento. La prevención es el conjunto de medidas para evitar el daño antes de que ocurra. Un equipo con energía o con partes en movimiento solo lo interviene personal autorizado, con la norma vigente de la SEC; el estudiante no se acerca a esas partes.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("calefacción eléctrica", "uso de la energía eléctrica para producir calor"), ("fuerza motriz", "uso de motores eléctricos para producir movimiento"), ("motor", "equipo que convierte energía eléctrica en movimiento"), ("potencia total instalada", "suma de las potencias de todos los equipos conectados"), ("prevención", "medidas para evitar el daño antes de que ocurra"), ("atrapamiento", "riesgo de que una parte del cuerpo quede atrapada por una pieza en movimiento")],
    worked=[
        ("Potencia total", "Un taller de ejemplo tiene dos estufas de 1500 W y un ventilador de 200 W. ¿Cuál es su potencia total instalada?", ["Se suman las potencias de todos los equipos.", "1500 más 1500 más 200 son 3200."], "3200 W"),
        ("Identificar un riesgo", "Una cinta transportadora de ejemplo gira con un motor eléctrico. ¿Qué riesgo propio tiene además de la descarga?", ["Tiene piezas que se mueven.", "Una prenda o un cabello podría quedar atrapado."], "El atrapamiento por partes en movimiento"),
    ],
    mistakes=[("Pensar que un equipo que solo da calor no tiene riesgo eléctrico.", "Sigue siendo un artefacto conectado a la energía.", "Considera descarga, quemadura e incendio."),
              ("Acercarse a revisar una bomba que está funcionando.", "Las partes en movimiento y la energía pueden causar lesiones graves.", "Avisa a un adulto responsable y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la fuerza motriz?", "El uso de motores eléctricos para producir movimiento, como en una bomba", "El uso de la energía eléctrica solo para producir calor", "El uso de la energía eléctrica solo para alumbrar", "La fuerza motriz es el movimiento producido por motores; el calor y la luz son otros usos."),
        ("abc", "En Electricidad: ¿qué hace un artefacto de calefacción eléctrica?", "Convierte energía eléctrica en calor", "Convierte calor en energía eléctrica", "Convierte energía eléctrica en movimiento", "La estufa transforma energía eléctrica en calor, no al revés ni en movimiento."),
        ("=", "Un taller de ejemplo tiene dos calefactores de 1500 W. ¿Cuántos kW suman entre los dos?", "(2*1500)//1000", "Se suman las potencias y se pasan a kW dividiendo por 1000.", " kW"),
        ("=", "{F} ¿Cuántos vatios de potencia total instalada suman los tres equipos de la ficha?", "2000+750+250", "Se suman las potencias de la estufa, la bomba y el ventilador.", " W"),
        ("=", "{F} ¿Cuántos kW de margen quedan respecto del límite del OA?", "(5000-(2000+750+250))//1000", "Al límite de 5000 W se le resta la potencia instalada y se pasa a kW.", " kW"),
        ("abc", "{F} ¿Qué riesgo propio corresponde a la bomba y al ventilador, y cuál a la estufa?", "Partes en movimiento para la bomba y el ventilador; quemadura e incendio para la estufa", "Quemadura para la bomba y el ventilador; partes en movimiento para la estufa", "Solo descarga eléctrica para los tres, sin otros riesgos", "Los motores tienen piezas que se mueven y la estufa tiene superficies calientes."),
        ("=", "{F} El taller agrega un segundo ventilador igual de 250 W. ¿Cuántos vatios de potencia total instalada tendrá?", "2000+750+250+250", "Se suma el nuevo ventilador a la potencia total anterior.", " W"),
        ("=", "{F} La estufa funciona 5 horas. ¿Cuántos kWh consume?", "2000*5//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("abc", "{F} Un trabajador cree que la bomba, por ser pequeña, puede revisarse mientras funciona. ¿Qué corresponde?", "No acercarse a las partes en movimiento ni intervenir un equipo con energía; lo hace personal autorizado", "Revisarla con cuidado si se ponen guantes", "Revisarla si la estufa del taller está apagada", "Los guantes o apagar otro equipo no eliminan el riesgo de la bomba en funcionamiento."),
        ("abc", "{F} Un compañero dice que, como la estufa solo da calor, no hay riesgo eléctrico. ¿Qué respuesta es correcta?", "La estufa también es un artefacto eléctrico: tiene riesgo de descarga, además de quemadura e incendio", "Tiene razón: el calor no es un riesgo eléctrico", "Tiene razón: el riesgo eléctrico es solo de los motores", "Todo artefacto conectado a la energía puede causar descarga."),
        ("ab", "{F} Un cliente quiere sumar un horno de 4000 W al taller. ¿Qué corresponde?", "Reconocer que la potencia total subiría a 7 kW y superaría los 5 kW del OA, e informar al proyectista", "Instalarlo igual porque es un solo equipo más", "Con 3 kW instalados y 4 kW más se llega a 7 kW; ya no es el tipo de proyecto que nombra el OA."),
        ("=", "{F} Si los tres equipos funcionaran a la vez durante 2 horas, ¿cuántos kWh consumirían en total?", "(2000+750+250)*2//1000", "Se suman las potencias, se multiplican por las horas y se pasa a kWh.", " kWh"),
        ("abc", "Ante un principio de incendio en una estufa eléctrica, ¿qué indican las reglas generales?", "Avisar a un adulto responsable y a emergencias, cortar el suministro solo si se está autorizado y no tocar a nadie que siga en contacto con la energía", "Apagar el fuego con agua sin cortar la energía", "Esperar a que se apague sola antes de avisar", "El agua con energía conectada es peligrosa y esperar retrasa la ayuda."),
    ],
    ctx=("abc", "{F} Una empresa de ejemplo propone que los estudiantes en práctica «ayuden» a destapar el motor de la bomba mientras funciona porque «es rápido». ¿Qué corresponde?", "Rechazarlo: el estudiante no interviene equipos con energía ni partes en movimiento; lo hace personal autorizado", "Aceptarlo si el estudiante usa lentes", "Aceptarlo si la práctica es de corta duración", "La rapidez o un elemento de protección aislado no reemplazan la autorización ni la norma vigente."),
    sc=[
        ("En Electricidad: ¿qué es la potencia total instalada?", "La suma de las potencias de todos los equipos conectados", "La suma incluye todos los equipos, no solo el mayor."),
        ("¿Qué riesgo propio tienen los motores además de la descarga?", "El atrapamiento por partes en movimiento", "Las piezas que giran pueden atrapar ropa o cabello."),
        ("¿Quién interviene un equipo con energía?", "Personal autorizado, con norma vigente (SEC) y protección", "Este cuaderno no habilita para intervenir equipos."),
    ],
    op=("Taller de ejemplo «Fragua Sur» (ficticio): una estufa de 1500 W, dos motores de 600 W cada uno y un ventilador de 300 W. Escribe (a) la potencia total instalada en vatios, (b) cuántos vatios faltan para llegar a 5 kW, (c) el riesgo propio de los motores y el de la estufa, (d) qué haces si un compañero se acerca a un motor en marcha para «arreglarlo».",
        "(a) 1500+600+600+300 son 3000 W. (b) 5000 menos 3000: faltan 2000 W. (c) Los motores: atrapamiento por partes en movimiento; la estufa: quemadura e incendio. (d) No lo toco, aviso a un adulto responsable y dejo la tarea a personal autorizado; si hay una descarga no toco a la persona en contacto con la energía y llamo a emergencias.",
        ["suma bien las potencias", "calcula bien la diferencia con el límite", "distingue los riesgos propios", "actúa con las reglas generales de seguridad"],
        ["hoja con las cuatro respuestas"],
        ["olvidar un equipo en la suma", "decir que la estufa no tiene riesgo", "proponer intervenir"],
        "Pregunta: «¿por qué no te acercas al motor en marcha?». Si no responde, pídele que relea los riesgos de los motores."),
    reinforce="Inventa un taller con tres equipos (uno de calor y dos con motor) y calcula su potencia total y cuánto falta para 5 kW.",
    extend="Explica con un ejemplo por qué la prevención es mejor que reaccionar después de un accidente.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (placas de características de ejemplo, inventadas). Motor de la bomba del «Taller Cobre»: potencia 1100 W; tensión 220 V; corriente nominal 5 A; velocidad 1500 vueltas por minuto; "
     "alimentación monofásica. Estufa: potencia 2000 W; tensión 220 V; alimentación monofásica.")
build(
    O4, 2, F,
    use="Aprenderé a leer la placa de características de un equipo y a distinguir alimentación monofásica y trifásica, siempre en papel.",
    prior=["Sé que P = V × I.", "Sé calcular horas y kWh.", "Sé que un documento debe coincidir con el equipo."],
    explain=[
        "La placa de características es una etiqueta del fabricante que trae los datos del equipo: potencia, tensión, corriente nominal, velocidad y tipo de alimentación. La corriente nominal es la que el equipo consume cuando funciona en sus condiciones normales. La velocidad de un motor se da en vueltas por minuto. La alimentación monofásica usa una fase y un neutro, y es la habitual en casas y locales pequeños. La alimentación trifásica usa tres fases y se emplea en equipos de más potencia. El tipo de alimentación y la tensión de la placa deben coincidir con los del lugar.",
        "Para comprobar si los datos de la placa son coherentes se usa P = V × I: la potencia dividida por la tensión debe dar la corriente nominal. Si un dato no coincide con la alimentación disponible, no se adapta por cuenta propia: se informa al proyectista. La placa se copia a un registro sin cambiar ningún valor.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("placa de características", "etiqueta del fabricante con los datos del equipo"), ("corriente nominal", "corriente que consume el equipo en sus condiciones normales de funcionamiento"), ("vueltas por minuto", "unidad con que se expresa la velocidad de giro de un motor"), ("monofásica", "alimentación con una fase y un neutro"), ("trifásica", "alimentación con tres fases, usada en equipos de más potencia"), ("fase", "conductor activo de la alimentación, por donde llega la energía al equipo"), ("neutro", "conductor de retorno de la alimentación")],
    worked=[
        ("Comprobar la placa", "La placa de un motor de ejemplo dice 660 W, 220 V y corriente nominal 3 A. ¿Es coherente?", ["660 dividido por 220 son 3.", "Coincide con la corriente de la placa."], "Sí, es coherente"),
        ("Vueltas en un tiempo", "Un motor de ejemplo gira a 900 vueltas por minuto. ¿Cuántas vueltas da en 5 minutos?", ["Se multiplica la velocidad por los minutos.", "900 por 5 son 4500."], "4.500 vueltas"),
    ],
    mistakes=[("Corregir un dato de la placa porque «parece un error».", "La placa es el dato del fabricante; cambiarlo falsea el registro.", "Anota lo que dice y consulta al proyectista."),
              ("Suponer que un motor trifásico funciona con una alimentación monofásica.", "El tipo de alimentación de la placa debe coincidir con el del lugar.", "Informa la diferencia al proyectista.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la placa de características de un equipo?", "Una etiqueta del fabricante con los datos del equipo, como potencia y tensión", "El plano del taller con las medidas del equipo", "La factura de compra del equipo", "La placa trae los datos técnicos del equipo; el plano y la factura son otros documentos."),
        ("abc", "En Electricidad: ¿qué es la corriente nominal de un equipo?", "La corriente que consume en sus condiciones normales de funcionamiento", "La corriente máxima que el equipo puede soportar sin ningún riesgo", "La corriente que tiene el equipo cuando está desconectado", "La nominal es la del funcionamiento normal; no es un límite de seguridad ni la del equipo desconectado."),
        ("abc", "¿Qué diferencia hay entre alimentación monofásica y trifásica?", "La monofásica usa una fase y un neutro; la trifásica usa tres fases", "La monofásica tiene mayor tensión que la trifásica", "La trifásica se usa solo en casas", "Se distinguen por el número de fases; no por la tensión ni por el lugar de uso."),
        ("=", "{F} ¿Cuántas vueltas da el motor de la bomba en 10 minutos?", "1500*10", "Se multiplica la velocidad por los minutos.", " vueltas"),
        ("abc", "{F} ¿Es coherente la corriente nominal de la placa del motor con su potencia y su tensión?", "Sí: 1100 W divididos por 220 V son 5 A", "No: debería ser 1100 A", "No: la corriente no se relaciona con la potencia", "I = P ÷ V y 1100 dividido por 220 da 5."),
        ("abc", "{F} Un técnico necesita la corriente nominal del motor. ¿Dónde la encuentra?", "En la placa de características del motor", "En el rótulo del plano", "En la leyenda del diagrama", "La corriente nominal es un dato del fabricante, escrito en la placa."),
        ("=", "{F} Tres motores iguales al de la placa funcionan a la vez a 220 V. ¿Cuántos amperios suman?", "3*5", "Cada motor usa 5 A y se multiplica por la cantidad.", " A"),
        ("=", "{F} ¿Cuántos kWh consume el motor funcionando 10 horas?", "1100*10//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("abc", "{F} Una bomba de repuesto de ejemplo trae una placa que dice 110 V, pero el taller tiene 220 V. ¿Qué corresponde?", "No usarla sin autorización: la tensión de la placa no coincide con la del taller; se consulta al proyectista", "Usarla, porque la bomba se adapta sola", "Usarla si funciona poco tiempo", "La tensión de la placa debe coincidir con la del lugar; no se supone que el equipo se adapte."),
        ("abc", "Un motor de ejemplo trae en su placa «trifásico», y el local solo tiene alimentación monofásica. ¿Qué corresponde?", "Informar al proyectista que el motor no coincide con la alimentación disponible", "Conectarlo de todos modos, porque el motor se ajusta solo", "Pedir a un compañero que lo pruebe con cuidado", "Un equipo que no coincide con la alimentación no se adapta por cuenta propia."),
        ("ab", "{F} El cliente dice que su local trabaja a 380 V (de ejemplo) pero la placa del motor dice 220 V. ¿Qué corresponde?", "Informar la diferencia: el motor no coincide con la tensión de ese local", "Conectarlo igual, porque un motor aguanta más tensión", "Una tensión distinta a la de la placa puede dañar el equipo o causar un accidente; se informa."),
        ("=", "Un equipo monofásico de ejemplo de 1320 W funciona a 220 V. ¿Cuántos amperios usa?", "1320//220", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "{F} El OA limita la potencia total a 5 kW. ¿Cuántos motores como el de la placa (1100 W) caben sin pasar de ese límite?", "5000//1100", "El límite en vatios se divide por la potencia de cada motor y se toma la parte entera.", " motores"),
    ],
    ctx=("abc", "{F} Una técnica de ejemplo anota en el registro «bomba, 1100 W». ¿Qué le falta para que el registro sirva?", "La tensión, la corriente nominal, el tipo de alimentación, la fecha y quién anotó", "El color de la bomba", "El nombre del cliente únicamente", "Un registro útil copia los datos de la placa y deja constancia de quién y cuándo."),
    sc=[
        ("En Electricidad: ¿qué indica la corriente nominal?", "La corriente del equipo en sus condiciones normales", "No es un límite de seguridad."),
        ("¿Qué se hace si el tipo de alimentación de la placa no coincide con el del lugar?", "Se informa al proyectista", "No se adapta el equipo por cuenta propia."),
        ("¿Cómo se comprueba la corriente nominal con la placa?", "Dividiendo la potencia por la tensión", "Se aplica I = P ÷ V a la potencia y a la tensión."),
    ],
    op=("Placa de ejemplo de un motor de extracción: potencia 880 W, tensión 220 V, corriente nominal 4 A, velocidad 1200 vueltas por minuto, alimentación monofásica. Escribe (a) si la corriente nominal es coherente con la potencia y la tensión, (b) cuántas vueltas da en 15 minutos, (c) cuántos amperios usan 3 motores iguales a la vez, (d) qué haces si el local tiene alimentación trifásica y la placa dice monofásica.",
        "(a) 880 dividido por 220 son 4 A: es coherente. (b) 1200 por 15 son 18.000 vueltas. (c) 3 por 4 son 12 A. (d) Informo al proyectista la diferencia y no adapto el equipo por mi cuenta.",
        ["comprueba la coherencia con P = V × I", "calcula las vueltas", "calcula la corriente total", "informa la diferencia sin adaptar"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar en vez de dividir", "olvidar los 15 minutos", "proponer conectar igual"],
        "Pregunta: «¿qué datos de la placa copiarías al registro?». Si no responde, pídele que relea qué trae la placa."),
    reinforce="Inventa la placa de un motor con potencia, tensión, corriente nominal y velocidad coherentes entre sí, y compruébala con P = V × I.",
    extend="Explica con un ejemplo por qué es riesgoso conectar un equipo con una tensión distinta de la de su placa.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (cuadro de cargas de ejemplo, inventado). Taller «Hilo Norte», tensión de ejemplo 220 V. Estufa E1: 1540 W. Motor M1: 1100 W. Motor M2: 660 W. Ventilador V1: 220 W. "
     "Límite del OA: 5 kW de potencia total instalada. El tablero de ejemplo tiene un límite de corriente de 15 A (valor de ejemplo, no real) para los equipos que funcionan a la vez.")
build(
    O4, 3, F,
    use="Aprenderé a distinguir potencia instalada y potencia simultánea, a calcular la corriente de los equipos que funcionan a la vez y a compararla con un límite de planilla.",
    prior=["Sé que I = P ÷ V.", "Sé calcular la potencia total instalada.", "Sé comparar un valor con un límite."],
    explain=[
        "La potencia instalada es la suma de las potencias de todos los equipos del taller, funcionen o no al mismo tiempo. La potencia simultánea es la suma de las potencias de los equipos que funcionan a la vez. El límite del OA se refiere a la potencia total instalada, pero la corriente que debe soportar el tablero depende de lo que funciona al mismo tiempo. Por eso hay que revisar los dos criterios: cumplir uno no asegura cumplir el otro.",
        "Para revisar un escenario de uso se suman las potencias de los equipos que funcionan juntos, se divide por la tensión para obtener la corriente y se compara con el límite de corriente de la planilla. Si se pasa, el escenario se informa al proyectista, que decide cómo rediseñar el reparto de cargas. Las reglas de uso quedan escritas en el proyecto; quien opera los equipos no las cambia por su cuenta.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("potencia instalada", "suma de las potencias de todos los equipos, funcionen o no a la vez"), ("potencia simultánea", "suma de las potencias de los equipos que funcionan a la vez"), ("escenario de uso", "combinación de equipos que se supone funcionando al mismo tiempo"), ("límite de corriente", "corriente máxima que fija el proyecto para el tablero o el circuito")],
    worked=[
        ("Potencia simultánea", "Un taller de ejemplo tiene equipos de 800 W, 600 W y 400 W; solo los dos primeros funcionan a la vez. ¿Cuál es la potencia simultánea?", ["Solo se suman los equipos que funcionan juntos.", "800 más 600 son 1400."], "1400 W"),
        ("Corriente de un escenario", "Dos equipos de ejemplo suman 1320 W a 220 V. ¿Cuántos amperios usan?", ["La corriente es la potencia dividida por la tensión.", "1320 dividido por 220 son 6."], "6 A"),
    ],
    mistakes=[("Revisar solo el límite de potencia del OA y no la corriente del tablero.", "Cumplir un criterio no asegura cumplir el otro.", "Revisa potencia instalada y corriente simultánea."),
              ("Cambiar por cuenta propia qué equipos funcionan juntos para «arreglar» el cálculo.", "Las reglas de uso las define el proyecto.", "Informa el resultado al proyectista.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la potencia simultánea?", "La suma de las potencias de los equipos que funcionan a la vez", "La potencia del equipo más grande", "La suma de las potencias de todos los equipos del taller, aunque no funcionen juntos", "La simultánea considera solo lo que funciona al mismo tiempo; la suma de todos es la instalada."),
        ("=", "Dos equipos de ejemplo de 700 W y 500 W funcionan a la vez. ¿Cuántos vatios de potencia simultánea hay?", "700+500", "Se suman las potencias de los equipos que funcionan juntos.", " W"),
        ("abc", "En Electricidad: ¿para qué sirve calcular la corriente de los equipos que funcionan a la vez?", "Para compararla con el límite del circuito o del tablero y detectar sobrecargas en el papel", "Para decidir qué proveedor vende los equipos", "Para saber cuántas horas puede funcionar cada equipo al día", "La corriente simultánea se compara con el límite de corriente; no decide proveedores ni horas."),
        ("=", "{F} ¿Cuál es la potencia total instalada del taller?", "1540+1100+660+220", "Se suman las potencias de los cuatro equipos.", " W"),
        ("=", "{F} ¿Cuántos amperios usa el escenario con E1, M1 y V1 funcionando a la vez?", "(1540+1100+220)//220", "Se suman las tres potencias y se divide por la tensión.", " A"),
        ("abc", "{F} ¿Cumple la potencia total instalada con el límite de 5 kW del OA?", "Sí: la potencia instalada es menor que 5000 W", "No: la potencia instalada supera 5 kW", "No se puede saber sin medir los equipos funcionando", "La suma es 3520 W, menor que 5000 W; se calcula en el papel."),
        ("=", "{F} ¿Cuántos amperios usa el escenario con M1, M2 y V1 funcionando a la vez?", "(1100+660+220)//220", "Se suman las tres potencias y se divide por la tensión.", " A"),
        ("=", "{F} ¿Cuántos amperios usarían los cuatro equipos funcionando a la vez?", "(1540+1100+660+220)//220", "Se suma toda la potencia y se divide por la tensión.", " A"),
        ("abc", "{F} Con los cuatro equipos a la vez y el límite de 15 A, ¿qué ocurre?", "Se supera el límite en 1 A; el uso simultáneo debe revisarse con el proyectista", "Se cumple, porque 16 A está cerca de 15 A", "Se cumple, porque la potencia total es menor que 5 kW", "Los cuatro equipos usan 16 A, más que 15 A; el límite de potencia del OA es otro criterio."),
        ("abc", "{F} E1, M1 y M2 funcionan a la vez. ¿Qué resultado da frente al límite de 15 A?", "Usan 15 A: llegan al límite sin superarlo", "Usan 15 A: superan el límite", "Usan 14 A: quedan bajo el límite", "Suman 3300 W, que a 220 V son 15 A, igual al límite."),
        ("ab", "{F} Un compañero dice que, como la potencia total está bajo 5 kW, no hace falta calcular la corriente. ¿Qué corresponde?", "Calcularla igual: cumplir el límite de potencia del OA no asegura cumplir el límite de corriente del tablero", "No hace falta: si cumple el límite del OA, todo está bien", "Son dos criterios distintos y deben revisarse los dos."),
        ("=", "{F} En un mes de ejemplo los cuatro equipos funcionan juntos 25 horas. ¿Cuántos kWh consumen en esas horas?", "3520*25//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("abc", "{F} El dueño quiere agregar un quinto equipo de 1100 W. ¿Qué ocurre?", "La potencia total sería 4620 W y cumpliría el OA, pero la corriente simultánea subiría a 21 A y superaría los 15 A de ejemplo", "No hay problema: 4620 W es menor que 5 kW", "Se supera el límite de 5 kW del OA", "Con 1100 W más, la potencia sigue bajo 5 kW pero la corriente de uso simultáneo pasa el límite del tablero."),
    ],
    ctx=("abc", "{F} Un operador de ejemplo dice: «yo enciendo todo a la vez, total el taller cumple los 5 kW». ¿Qué corresponde responder?", "Que el escenario de los cuatro equipos juntos supera el límite de corriente del tablero y debe informarse al proyectista", "Que no hay problema, porque cumple los 5 kW", "Que lo haga solo cuando el jefe no esté", "Cumplir la potencia del OA no basta: la corriente simultánea tiene su propio límite."),
    sc=[
        ("En Electricidad: ¿qué se suma para obtener la potencia simultánea?", "Las potencias de los equipos que funcionan a la vez", "Los que no funcionan juntos no entran en esa suma."),
        ("¿Cómo se pasa de potencia a corriente?", "Dividiendo la potencia por la tensión", "Se aplica I = P ÷ V a la potencia y a la tensión."),
        ("¿Cuántos criterios hay que revisar: potencia instalada y corriente simultánea?", "Los dos", "Cumplir uno no asegura cumplir el otro."),
    ],
    op=("Cuadro de ejemplo del taller «Bruma»: tensión 220 V; estufa 1320 W; motor 880 W; ventilador 220 W; límite de corriente del tablero de ejemplo: 10 A. Escenario 1: estufa y ventilador a la vez. Escenario 2: los tres a la vez. Escribe (a) la potencia total instalada, (b) la corriente de cada escenario, (c) cuál cumple el límite de 10 A, (d) qué haces con el escenario que no cumple.",
        "(a) 1320+880+220 son 2420 W. (b) Escenario 1: 1540 dividido por 220 son 7 A; escenario 2: 2420 dividido por 220 son 11 A. (c) El escenario 1 cumple; el 2 supera el límite en 1 A. (d) Informo al proyectista; no cambio por mi cuenta cómo se usan los equipos.",
        ["suma bien la potencia instalada", "calcula las dos corrientes", "compara con el límite", "informa en lugar de cambiar por su cuenta"],
        ["hoja con la tabla de cálculos"],
        ["sumar solo dos equipos en el escenario 2", "decir que el escenario 2 cumple", "decidir un rediseño"],
        "Pregunta: «¿por qué el escenario 2 es un problema aunque la potencia sea baja?». Si no responde, pídele que relea los dos criterios."),
    reinforce="Inventa un taller con cuatro equipos y dos escenarios de uso; calcula la corriente de cada escenario con un límite que fijes tú.",
    extend="Explica con un ejemplo por qué el uso simultáneo de equipos puede ser riesgoso aunque cada equipo esté dentro de su límite.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (alternativas de ejemplo, inventadas). Una bomba de un taller debe entregar 720 W de potencia útil y funciona 6 horas al día durante 25 días al mes. "
     "Motor X: rendimiento 80 %, precio $60.000. Motor Y: rendimiento 90 %, precio $90.000. Energía de ejemplo: $150 por kWh. "
     "Rendimiento = potencia útil ÷ potencia consumida × 100, de modo que potencia consumida = potencia útil × 100 ÷ rendimiento.")
build(
    O4, 4, F,
    use="Aprenderé qué es el rendimiento de un motor y a comparar el consumo y el costo de dos alternativas con datos de ejemplo.",
    prior=["Sé calcular energía en kWh.", "Sé calcular porcentajes sencillos.", "Sé comparar costos de compra y de uso."],
    explain=[
        "Un motor no convierte toda la energía eléctrica que consume en trabajo útil: una parte se pierde, sobre todo como calor. El rendimiento mide qué parte es útil: potencia útil ÷ potencia consumida × 100, en porcentaje. Un motor de rendimiento 80 % que debe entregar 720 W útiles consume 720 × 100 ÷ 80 = 900 W. Un motor de mayor rendimiento consume menos para hacer el mismo trabajo.",
        "Para comparar dos motores se calcula la potencia consumida de cada uno, la energía mensual (potencia por horas, en kWh), el costo de la energía y el costo de compra. El mejor no es siempre el más barato de comprar: depende del tiempo de uso. Los datos de rendimiento deben venir de la placa o de la ficha del fabricante y se registran con su fuente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("potencia útil", "parte de la potencia que se convierte en trabajo, como el movimiento de una bomba"), ("potencia consumida", "potencia eléctrica que toma el motor de la red"), ("rendimiento", "potencia útil ÷ potencia consumida × 100, en porcentaje"), ("pérdidas", "parte de la energía que no se convierte en trabajo útil, sobre todo calor")],
    worked=[
        ("Calcular el rendimiento", "Un motor de ejemplo consume 1000 W y entrega 700 W útiles. ¿Qué rendimiento tiene?", ["Rendimiento = útil ÷ consumida × 100.", "700 por 100 dividido por 1000 son 70."], "70 %"),
        ("Calcular lo consumido", "Un motor de ejemplo de rendimiento 90 % debe entregar 450 W útiles. ¿Cuántos vatios consume?", ["Consumida = útil × 100 ÷ rendimiento.", "450 por 100 dividido por 90 son 500."], "500 W"),
    ],
    mistakes=[("Elegir el motor de menor precio sin calcular su consumo.", "Un menor rendimiento significa más energía pagada cada mes.", "Compara compra y energía durante el período de uso."),
              ("Suponer que un rendimiento mayor significa más potencia útil.", "El rendimiento mide la proporción aprovechada, no la potencia entregada.", "Calcula la potencia consumida para cada motor.")],
    T=[
        ("abc", "En Electricidad: ¿qué es el rendimiento de un motor?", "La relación entre la potencia útil que entrega y la potencia que consume, en porcentaje", "La velocidad con que gira, en vueltas por minuto", "El tiempo que dura sin fallar", "El rendimiento compara lo útil con lo consumido; la velocidad y la duración son otros datos."),
        ("=", "Un motor de ejemplo consume 500 W y entrega 400 W útiles. ¿Qué rendimiento tiene, en porcentaje?", "400*100//500", "El rendimiento es la potencia útil por 100 dividida por la consumida.", " %"),
        ("abc", "En Electricidad: ¿qué ocurre con la parte de la potencia consumida que no se convierte en trabajo útil?", "Se pierde, en gran parte como calor", "Se guarda en el motor para el día siguiente", "Se convierte en tensión adicional", "Las pérdidas de un motor se disipan, sobre todo como calor."),
        ("=", "{F} ¿Cuántas horas funciona la bomba al mes?", "6*25", "Se multiplican las horas diarias por los días del mes.", " horas"),
        ("=", "{F} ¿Cuántos vatios consume el motor X para entregar la potencia útil pedida?", "720*100//80", "Consumida = útil × 100 ÷ rendimiento.", " W"),
        ("=", "{F} ¿Cuántos vatios consume el motor Y?", "720*100//90", "Consumida = útil × 100 ÷ rendimiento.", " W"),
        ("=", "{F} ¿Cuántos kWh consume el motor X en un mes?", "900*150//1000", "Se multiplica la potencia consumida por las horas del mes y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuánto cuesta al mes la energía del motor Y?", "800*150//1000*150", "Se calculan los kWh del mes y se multiplican por el precio de cada kWh.", " pesos"),
        ("=", "{F} ¿Cuántos pesos al mes ahorra Y respecto de X solo en energía?", "(900-800)*150//1000*150", "Se calcula la diferencia de kWh y se multiplica por el precio.", " pesos"),
        ("abc", "{F} Un compañero dice que X conviene porque cuesta $30.000 menos. ¿Qué respuesta es correcta?", "Falta calcular el ahorro de energía de Y en el período de uso y compararlo con la diferencia de compra", "Tiene razón: el precio de compra es el único criterio", "Tiene razón porque Y consume más que X", "Y consume menos que X; hay que comparar su ahorro acumulado con la diferencia de compra."),
        ("ab", "{F} Si la bomba funcionara solo 2 horas al mes, ¿seguiría conviniendo Y por ahorro de energía?", "No necesariamente: con tan pocas horas el ahorro no alcanza a cubrir los $30.000 de diferencia", "Sí: siempre conviene el motor de mayor rendimiento", "El ahorro depende de las horas de uso; con muy poco uso la diferencia de compra no se recupera."),
        ("=", "{F} En 24 meses, ¿cuántos pesos de energía ahorra Y respecto de X?", "24*(900-800)*150//1000*150", "Se multiplica el ahorro mensual por los 24 meses.", " pesos"),
        ("abc", "{F} Antes de decidir, se verifica la calidad de los datos. ¿Qué verificación es útil?", "Que el rendimiento y la potencia útil vengan de la placa o de la ficha del fabricante y se registren con su fuente", "Que el precio sea un número redondo", "Que el motor sea el más pesado", "Un cálculo es confiable si sus datos tienen origen conocido y registrado."),
    ],
    ctx=("abc", "{F} El jefe del taller de ejemplo quiere comprar el motor X «para no gastar de más ahora». ¿Qué le explica la técnica?", "Que Y cuesta $30.000 más pero ahorra energía cada mes, y que la decisión se registra con el cálculo", "Que X es ilegal", "Que Y ahorra solo si funciona las 24 horas del día", "Con la ficha, Y ahorra energía mensual y en 24 meses recupera la diferencia."),
    sc=[
        ("En Electricidad: ¿cómo se calcula la potencia consumida de un motor?", "Potencia útil × 100 ÷ rendimiento", "Con menor rendimiento se consume más para el mismo trabajo."),
        ("En electricidad: ¿cuántos kWh son 3000 Wh?", "3 kWh", "Cada 1000 Wh forman 1 kWh, así que se divide por 1000."),
        ("¿Qué se compara además del precio de compra?", "El costo de la energía durante el período de uso", "El motor barato puede costar más en total."),
    ],
    op=("Datos de ejemplo: un ventilador debe entregar 600 W útiles y funciona 5 horas al día durante 20 días al mes. Motor P: rendimiento 75 %, precio $40.000. Motor Q: rendimiento 80 %, precio $55.000. Energía a $140 por kWh. Escribe (a) los vatios que consume cada motor, (b) los kWh mensuales de cada uno, (c) el costo mensual de energía de cada uno, (d) si en 12 meses el ahorro supera la diferencia de compra.",
        "(a) P: 600 por 100 dividido por 75 son 800 W; Q: 600 por 100 dividido por 80 son 750 W. (b) Son 100 horas al mes: P 80 kWh; Q 75 kWh. (c) P: 80 por 140 son 11.200 pesos; Q: 75 por 140 son 10.500 pesos. (d) El ahorro mensual es 700 pesos; en 12 meses son 8.400 pesos, menos que la diferencia de compra de 15.000: no conviene Q solo por ahorro en 12 meses.",
        ["calcula bien los vatios consumidos", "calcula bien los kWh", "calcula bien los costos", "compara el ahorro con la inversión"],
        ["hoja con la tabla de cálculos y la conclusión"],
        ["usar el rendimiento al revés", "olvidar las horas", "decidir solo por el precio"],
        "Pregunta: «¿en cuántos años recuperarías la diferencia de compra?». Si no responde, pídele que relea cómo se compara el período de uso."),
    reinforce="Inventa dos motores con distinto rendimiento y calcula cuántos vatios consume cada uno para entregar la misma potencia útil.",
    extend="Explica con un ejemplo por qué un motor de mayor rendimiento puede no convenir si se usa muy pocas horas.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (informe de calidad de ejemplo, inventado). Proyecto «Taller Arce»: potencia instalada declarada en la memoria de cálculo: 3520 W; suma real según el cuadro de cargas: 3620 W; límite del OA: 5 kW. "
     "La estufa figura con 1500 W en el plano y con 1540 W en el cuadro de cargas. Presupuesto: materiales $350.000; mano de obra 40 horas a $4.500 la hora; gastos generales de ejemplo: 10 % sobre materiales y mano de obra.")
build(
    O4, 5, F,
    use="Aprenderé a verificar la coherencia de un proyecto de calefacción y fuerza motriz, a registrar no conformidades y a calcular un presupuesto de ejemplo.",
    prior=["Sé comparar documentos de un proyecto.", "Sé calcular potencia total y porcentajes sencillos.", "Sé qué es un hallazgo."],
    explain=[
        "Verificar la calidad de un proyecto es comprobar que cumple los requisitos y que los documentos son coherentes entre sí. Una no conformidad es un punto que no cumple un requisito del proyecto o de la norma vigente, y se registra. Una acción correctiva es una medida para corregir el problema y evitar que se repita. La decisión de qué documento se corrige la toma el proyectista o el supervisor, no quien detectó la diferencia. Después de corregir, se verifica que la corrección sea correcta y se deja registro del cierre.",
        "El presupuesto suma los materiales, la mano de obra (horas por valor de la hora) y los gastos generales, que se estiman como porcentaje de lo anterior. Los precios y porcentajes de esta ficha son de ejemplo. Un presupuesto debe reflejar el costo real: no se ocultan costos para que el total parezca menor.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("no conformidad", "punto que no cumple un requisito del proyecto o de la norma vigente"), ("acción correctiva", "medida para corregir un problema detectado y evitar que se repita"), ("verificar", "comprobar que algo cumple lo exigido"), ("gastos generales", "costos del trabajo que no son un material ni una hora de mano de obra, estimados como porcentaje"), ("cierre", "registro de que la corrección se hizo y se comprobó")],
    worked=[
        ("Detectar una no conformidad", "La memoria de un proyecto de ejemplo dice 2000 W y el cuadro suma 2100 W. ¿Qué se registra?", ["Los dos documentos no coinciden.", "Hay una diferencia de 100 W que se registra como no conformidad."], "Una no conformidad: 2000 W en la memoria y 2100 W en el cuadro"),
        ("Gastos generales", "Un subtotal de ejemplo es de $200.000 y los gastos generales son el 10 %. ¿Cuánto son los gastos generales?", ["El 10 % de 200.000 es 20.000.", "Se suma al subtotal si se quiere el total."], "$20.000"),
    ],
    mistakes=[("Elegir por cuenta propia el valor «más seguro» cuando dos documentos difieren y seguir sin registrar.", "No se sabe cuál documento es el correcto y se pierde la trazabilidad.", "Registra la no conformidad y espera la decisión del proyectista."),
              ("Dar por cerrada una no conformidad apenas se corrige el documento.", "Falta comprobar que la corrección es correcta.", "Verifica la corrección y deja el registro de cierre.")],
    T=[
        ("abc", "En Electricidad: ¿qué es una no conformidad en un control de calidad?", "Un punto que no cumple un requisito del proyecto o de la norma vigente", "Un cambio aprobado al proyecto", "Una firma de recepción del cliente", "La no conformidad es un incumplimiento detectado; los cambios aprobados y la recepción son otros actos."),
        ("abc", "En Electricidad: ¿qué es una acción correctiva?", "Una medida para corregir un problema detectado y evitar que se repita", "Un descuento al cliente por el atraso", "Una copia del plano para el archivo", "La acción correctiva ataca la causa del problema; el descuento y el archivo son otros asuntos."),
        ("=", "Un presupuesto de ejemplo tiene 30 horas de mano de obra a $4.000 la hora. ¿Cuánto cuesta la mano de obra?", "30*4000", "Se multiplican las horas por el valor de cada hora.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la mano de obra del proyecto?", "40*4500", "Se multiplican las horas por el valor de cada hora.", " pesos"),
        ("=", "{F} ¿Cuántos vatios de diferencia hay entre la potencia de la memoria y la suma del cuadro de cargas?", "3620-3520", "Se resta la potencia de la memoria a la del cuadro.", " W"),
        ("abc", "{F} ¿Qué hallazgo es una incoherencia entre documentos?", "La memoria declara 3520 W y el cuadro de cargas suma 3620 W", "El límite del OA es de 5 kW", "El presupuesto incluye mano de obra", "Una incoherencia es cuando dos documentos dan datos distintos para lo mismo."),
        ("=", "{F} Los gastos generales son el 10 % de materiales más mano de obra. ¿Cuántos pesos son?", "(350000+40*4500)*10//100", "Se suma el subtotal y se calcula el 10 %.", " pesos"),
        ("=", "{F} ¿Cuál es el total del presupuesto con gastos generales?", "(350000+40*4500)*110//100", "El subtotal más el 10 % equivale a multiplicar por 110 y dividir por 100.", " pesos"),
        ("abc", "{F} ¿Quién decide si se corrige la memoria o el cuadro de cargas?", "El proyectista o el supervisor", "Quien detectó la diferencia, porque la conoce mejor", "El cliente, porque paga el proyecto", "La decisión corresponde a quien diseña o supervisa."),
        ("abc", "{F} Un compañero propone «usar el mayor valor, por seguridad, y seguir sin registrar nada». ¿Qué respuesta es correcta?", "Registrar la no conformidad y que el proyectista determine el valor correcto y recalcule", "Usar el mayor y no registrar nada", "Usar el menor, porque cumple el OA", "Sin registro no hay trazabilidad, y ninguno de los dos valores está confirmado."),
        ("ab", "{F} Una vez corregida la memoria, ¿se da la no conformidad por cerrada de inmediato?", "No: se verifica que la corrección sea correcta y se deja registro del cierre", "Sí: ya se corrigió el documento", "Cerrar exige comprobar la corrección; de lo contrario puede repetirse el error."),
        ("=", "{F} Si el cuadro es el correcto, ¿cuántos vatios de margen quedan respecto del límite de 5 kW?", "5000-3620", "Al límite se le resta la potencia total del cuadro.", " W"),
        ("abc", "{F} Además, la estufa figura con 1500 W en el plano y con 1540 W en el cuadro. ¿Cuántas incoherencias de potencia hay ahora en la ficha?", "Dos: memoria contra cuadro y plano contra cuadro", "Una: solo la de la memoria", "Tres: memoria, plano y presupuesto", "Hay dos pares de documentos que difieren; el presupuesto no declara potencias."),
    ],
    ctx=("abc", "{F} El jefe del proyecto de ejemplo pide aprobar el informe «porque la diferencia es de solo 100 W». ¿Qué corresponde?", "No aprobarlo hasta que el proyectista resuelva y se registre la no conformidad", "Aprobarlo si la diferencia no supera el 5 %", "Aprobarlo y corregirlo después de la ejecución", "Una incoherencia, aunque sea pequeña, se resuelve antes de aprobar."),
    sc=[
        ("En Electricidad: ¿qué hace quien detecta una diferencia entre dos documentos?", "La registra y la informa al proyectista", "No decide qué documento se corrige."),
        ("¿Qué incluye el presupuesto de un proyecto?", "Materiales, mano de obra y gastos generales", "Los tres rubros forman el costo total."),
        ("¿Cuándo se cierra una no conformidad?", "Después de verificar la corrección y registrar el cierre", "Corregir no basta: hay que comprobarlo."),
    ],
    op=("Informe de ejemplo del proyecto «Panel Lago»: memoria: 2640 W; cuadro de cargas: 2860 W; límite del OA: 5 kW; materiales $200.000; mano de obra 30 horas a $5.000 la hora; gastos generales de ejemplo: 10 %. Escribe (a) la diferencia entre memoria y cuadro, (b) cómo registrarías la no conformidad y a quién la informarías, (c) el costo de la mano de obra, (d) el total del presupuesto con gastos generales, (e) los vatios de margen respecto de 5 kW si el cuadro es el correcto.",
        "(a) 2860 menos 2640 son 220 W. (b) Registro que la memoria dice 2640 W y el cuadro 2860 W, con fecha y mi nombre, y lo informo al proyectista o supervisor. (c) 30 por 5.000 son 150.000 pesos. (d) 200.000 + 150.000 = 350.000; con 10 %: 385.000 pesos. (e) 5000 menos 2860: 2140 W.",
        ["calcula la diferencia", "registra e informa correctamente", "calcula la mano de obra", "calcula el total del presupuesto", "calcula el margen"],
        ["hoja con los cálculos y el registro"],
        ["decidir el valor correcto por su cuenta", "olvidar los gastos generales", "restar mal el margen"],
        "Pregunta: «¿quién decide cuál valor es el correcto?». Si no responde, pídele que relea quién decide qué documento se corrige."),
    reinforce="Escribe una no conformidad de ejemplo con tres datos: qué documentos difieren, qué dice cada uno y quién la detectó.",
    extend="Explica con un ejemplo por qué es útil registrar el cierre de una no conformidad.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). «Kiosco Pino» (ficticio). Plano: 9 puntos de luz, 6 tomacorrientes, 2 interruptores y 1 tablero. "
     "Especificaciones: los tomacorrientes se compran en cajas de 4 unidades. Presupuesto de ejemplo: cada punto de luz cuesta $3.500, cada tomacorriente $2.000 y cada interruptor $1.500.")
build(
    O5, 1, F,
    use="Aprenderé qué es cubicar, qué documentos se usan para hacerlo y por qué una cubicación mal hecha es un problema de costo y de seguridad.",
    prior=["Sé leer un plano y una lista de materiales.", "Sé sumar, multiplicar y dividir.", "Sé redondear hacia arriba."],
    explain=[
        "Cubicar es calcular las cantidades de materiales, insumos y mano de obra que necesita un proyecto, a partir de los planos y las especificaciones. Un material es lo que queda incorporado a la instalación, como un tomacorriente. Un insumo es un elemento que se consume al trabajar y también se cuenta, como etiquetas o abrazaderas. La mano de obra es el trabajo humano, medido en horas. El resultado se ordena en una planilla de cubicación, y con ella se arma el presupuesto.",
        "Muchos materiales se venden en presentaciones fijas, como cajas de 4 unidades. Entonces se compra un número entero de presentaciones, redondeando hacia arriba, y pueden sobrar unidades que se registran. Cubicar mal tiene dos riesgos: si faltan materiales, aparece la tentación de improvisar con piezas inadecuadas, lo que es un riesgo de seguridad; si sobran muchos, se paga de más. Si el plano y la especificación no coinciden, se informa al proyectista antes de comprar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular las cantidades de materiales, insumos y mano de obra de un proyecto"), ("material", "elemento que queda incorporado a la instalación"), ("insumo", "elemento que se consume al trabajar y se cuenta, como etiquetas o abrazaderas"), ("planilla de cubicación", "tabla con las cantidades calculadas de cada material e insumo"), ("presentación", "cantidad fija en que un proveedor vende un material, como una caja de 4 unidades")],
    worked=[
        ("Contar elementos", "Un plano de ejemplo dibuja 7 puntos de luz y 5 tomacorrientes. ¿Cuántos elementos hay en total?", ["Se suman los puntos de luz y los tomacorrientes.", "7 más 5 son 12."], "12 elementos"),
        ("Cajas necesarias", "Se necesitan 10 piezas y se venden en cajas de 6. ¿Cuántas cajas hay que comprar?", ["Con 1 caja hay 6, no alcanza; con 2 cajas hay 12.", "Se redondea hacia arriba."], "2 cajas"),
    ],
    mistakes=[("Comprar menos de lo cubicado «por si no se usa todo».", "Los faltantes empujan a improvisar con piezas inadecuadas.", "Compra lo cubicado y registra los sobrantes."),
              ("Redondear hacia abajo al calcular cajas.", "Las cantidades quedarían cortas.", "Redondea siempre hacia arriba a presentaciones completas.")],
    T=[
        ("abc", "En Electricidad: ¿qué es cubicar?", "Calcular las cantidades de materiales, insumos y mano de obra que necesita un proyecto", "Dibujar el proyecto en tres dimensiones", "Pagar los materiales en cuotas", "Cubicar es calcular cantidades; no es dibujar ni pagar."),
        ("abc", "En Electricidad: ¿qué es un insumo?", "Un elemento que se consume al trabajar y que también se cuenta, como las etiquetas", "Una herramienta que se guarda y se reutiliza siempre", "Un documento del proyecto", "El insumo se consume; la herramienta se reutiliza y el documento no es un elemento físico."),
        ("=", "Un proyecto de ejemplo tiene 7 puntos de luz y 5 tomacorrientes. ¿Cuántos puntos hay en total?", "7+5", "Se suman los puntos de luz y los tomacorrientes.", " puntos"),
        ("=", "{F} ¿Cuántas unidades hay en el plano entre luces, tomacorrientes e interruptores, sin contar el tablero?", "9+6+2", "Se suman las tres cantidades del plano.", " unidades"),
        ("=", "{F} ¿Cuántas cajas de tomacorrientes se necesitan para cubrir los 6 del plano?", "(6+4-1)//4", "Se divide por 4 redondeando hacia arriba, porque solo se venden cajas completas.", " cajas"),
        ("=", "{F} Si se compran las cajas necesarias, ¿cuántos tomacorrientes sobran?", "2*4-6", "Se resta lo necesario a lo que traen las cajas compradas.", " tomacorrientes"),
        ("=", "{F} ¿Cuánto cuestan en total los puntos de luz?", "9*3500", "Se multiplica el precio de un punto de luz por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los 6 tomacorrientes y los 2 interruptores?", "6*2000+2*1500", "Se suman el costo de los tomacorrientes y el de los interruptores.", " pesos"),
        ("abc", "{F} Un comprador sugiere comprar «un poco menos, por si no se usan todos». ¿Qué corresponde?", "No: comprar menos de lo cubicado deja faltantes que empujan a improvisar con piezas inadecuadas", "Sí: lo que falte se improvisa", "Sí: el plano siempre trae de más", "Un faltante puede llevar a usar piezas inadecuadas, lo que es un riesgo."),
        ("abc", "{F} El plano dibuja 9 puntos de luz y la planilla del comprador dice 10. ¿Qué corresponde?", "Informar la diferencia al proyectista o al supervisor antes de comprar", "Comprar 10, porque es más seguro", "Comprar 9, porque el plano siempre manda", "Una diferencia entre documentos se informa antes de comprar."),
        ("ab", "{F} Un compañero dice que, si sobran 2 tomacorrientes, el error de compra no importa. ¿Qué corresponde?", "Registrar el sobrante: pagar de más es un costo y cada compra debe coincidir con la cubicación", "No importa: lo que sobra se usa en otros proyectos", "Un sobrante sin registrar oculta una diferencia con la cubicación y un gasto innecesario."),
        ("=", "{F} Si el proyecto cambia a 12 luces y 8 tomacorrientes, ¿cuánto cuestan en total luces y tomacorrientes?", "12*3500+8*2000", "Se suman el costo de las luces y el de los tomacorrientes.", " pesos"),
        ("abc", "{F} Con 8 tomacorrientes, ¿cuántas cajas se necesitan y cuántos sobran?", "2 cajas y no sobra ninguno", "3 cajas y sobran 4", "2 cajas y sobran 4", "Dos cajas de 4 traen justo 8 tomacorrientes."),
    ],
    ctx=("abc", "{F} Un instalador de ejemplo dice que «en obra se ve cuánto se necesita» y que no es necesario cubicar. ¿Qué corresponde?", "Explicar que cubicar antes permite comprar lo correcto, presupuestar y evitar improvisaciones riesgosas", "Aceptar, porque en obra se arregla todo", "Cubicar solo si el cliente lo pide", "Cubicar antes ordena la compra y el costo, y evita improvisar con piezas inadecuadas."),
    sc=[
        ("En Electricidad: ¿qué se hace cuando un material se vende en cajas?", "Se compra un número entero de cajas, redondeando hacia arriba", "No se pueden comprar cajas incompletas."),
        ("¿Qué riesgo trae un faltante de materiales?", "La tentación de improvisar con piezas inadecuadas", "Improvisar puede dejar la instalación insegura."),
        ("¿Qué es la mano de obra?", "El trabajo humano necesario, medido en horas", "Se cuenta en horas y se multiplica por el valor de la hora."),
    ],
    op=("Plano de ejemplo del proyecto «Peluquería Mar» (ficticio): 11 puntos de luz, 7 tomacorrientes y 2 interruptores. Los tomacorrientes se venden en cajas de 4. Precios de ejemplo: punto de luz $3.000; caja de tomacorrientes $7.000; interruptor $1.500. Escribe (a) cuántas cajas de tomacorrientes se necesitan, (b) cuántos tomacorrientes sobran, (c) el costo total de luces, cajas e interruptores, (d) qué haces si la planilla del comprador dice 12 puntos de luz.",
        "(a) 7 dividido por 4, redondeado hacia arriba: 2 cajas. (b) 8 menos 7: sobra 1. (c) 11 por 3.000 son 33.000; 2 cajas son 14.000; 2 interruptores son 3.000: total 50.000 pesos. (d) Informo la diferencia al proyectista o supervisor antes de comprar.",
        ["calcula las cajas con redondeo hacia arriba", "calcula el sobrante", "calcula bien el costo total", "informa la diferencia antes de comprar"],
        ["hoja con la tabla de cálculos y las respuestas"],
        ["redondear hacia abajo", "olvidar los interruptores", "comprar sin informar"],
        "Pregunta: «¿por qué compras 2 cajas y no 1,75?». Si no responde, pídele que relea cómo se venden los materiales."),
    reinforce="Inventa un proyecto con cuatro elementos, cuenta cuántos hay de cada uno y calcula cuántas cajas de 5 unidades necesitarías para cada uno.",
    extend="Explica con un ejemplo por qué un faltante de materiales puede ser un riesgo de seguridad y no solo un problema de plazo.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (planilla de cubicación de ejemplo, inventada). Conductor tipo «T» de ejemplo (sin sección ni marca). Plano a escala 1:100. Recorrido dibujado: 4 tramos que miden 5 cm, 8 cm, 12 cm y 15 cm en el plano. "
     "Merma de ejemplo: 10 % sobre el total de metros. El conductor se vende en rollos de 25 m.")
build(
    O5, 2, F,
    use="Aprenderé a pasar medidas del plano a metros reales, a sumar la merma y a calcular cuántas presentaciones hay que comprar.",
    prior=["Sé aplicar una escala.", "Sé qué es una presentación.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "Para cubicar el largo de un recorrido se mide en el plano cada tramo, se suman los centímetros y se multiplican por el número de la escala: a escala 1:100, 1 cm del plano son 100 cm reales, es decir, 1 m. Entonces 40 cm de plano son 40 m reales. A ese total se le suma la merma: material adicional que se prevé porque parte se pierde, se recorta o no se puede usar. La merma se expresa como porcentaje del total.",
        "Con los metros ya con merma se calcula cuántas presentaciones comprar: si el conductor se vende en rollos de 25 m, se divide y se redondea hacia arriba. Lo que sobra de los rollos se registra. Los valores de esta ficha (escala, merma y rollo) son de ejemplo; los reales los fija el proyecto y la norma vigente. No se indica ningún tipo de conductor real.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("merma", "material adicional que se prevé porque parte se pierde o no se puede usar"), ("tramo", "parte de un recorrido dibujado en el plano"), ("rollo", "presentación en que se vende un conductor, con un largo fijo"), ("escala 1:100", "razón en que 1 cm del plano son 100 cm reales")],
    worked=[
        ("Del plano a metros", "A escala 1:100, un recorrido suma 28 cm en el plano. ¿Cuántos metros reales son?", ["Cada centímetro del plano es 1 metro real.", "28 cm de plano son 28 m."], "28 m"),
        ("Con merma", "Un recorrido de ejemplo suma 30 m y la merma es del 10 %. ¿Cuántos metros se cubican?", ["El 10 % de 30 es 3.", "30 más 3 son 33."], "33 m"),
    ],
    mistakes=[("Aplicar la merma solo al tramo más largo.", "La merma es un porcentaje del total.", "Calcula la merma sobre la suma de todos los tramos."),
              ("Comprar justo los metros calculados cuando el material se vende en rollos completos.", "No se pueden comprar fracciones de rollo.", "Divide y redondea hacia arriba.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la merma en una cubicación?", "Material adicional que se prevé porque parte se pierde o no se puede usar", "Material que se devuelve al proveedor", "Un descuento por compra grande", "La merma se suma a lo calculado; no es una devolución ni un descuento."),
        ("=", "Un recorrido dibujado mide 35 cm en un plano a escala 1:100. ¿Cuántos metros reales son?", "35*100//100", "Se multiplica por la escala y se pasa de centímetros a metros.", " m"),
        ("abc", "En Electricidad: ¿qué significa la presentación de un material, como un rollo o una caja?", "La cantidad fija en que lo vende el proveedor", "El precio por unidad", "La calidad del material", "La presentación es la cantidad fija de venta; el precio y la calidad son otros datos."),
        ("=", "{F} ¿Cuántos centímetros suman los cuatro tramos en el plano?", "5+8+12+15", "Se suman las medidas de los cuatro tramos.", " cm"),
        ("=", "{F} ¿Cuántos metros reales suman los cuatro tramos?", "(5+8+12+15)*100//100", "Se multiplica por la escala y se pasa a metros.", " m"),
        ("=", "{F} ¿Cuántos metros de merma se prevén?", "40*10//100", "La merma es el 10 % de los metros del recorrido.", " m"),
        ("=", "{F} ¿Cuántos metros hay que cubicar en total, con merma?", "40+40*10//100", "Se suman los metros del recorrido y la merma.", " m"),
        ("=", "{F} ¿Cuántos rollos de 25 m hay que comprar?", "(44+24)//25", "Se divide por 25 redondeando hacia arriba.", " rollos"),
        ("=", "{F} ¿Cuántos metros sobran de los rollos comprados?", "2*25-44", "Se resta lo cubicado a lo que traen los rollos.", " m"),
        ("abc", "{F} La tienda vende solo rollos completos. Un compañero propone comprar 44 m cortando un rollo. ¿Qué corresponde?", "Comprar 2 rollos completos y registrar los 6 m sobrantes", "Comprar 1 rollo y buscar el resto después", "Comprar 2 rollos y anotar 0 m sobrantes", "Si solo hay rollos completos, se compran los necesarios y se registra el sobrante."),
        ("ab", "{F} Un cubicador aplica la merma de 10 % solo al tramo más largo, de 15 m. ¿Qué corresponde?", "Aplicarla sobre el total de 40 m, como dice la planilla", "Mantener su cálculo, porque el tramo más largo es el que más merma tiene", "La planilla fija la merma sobre el total de metros, no sobre un tramo."),
        ("=", "{F} Si el plano estuviera a escala 1:50 y los tramos midieran lo mismo, ¿cuántos metros reales sumarían?", "40*50//100", "Se multiplica por 50 para pasar a centímetros y se divide por 100 para pasar a metros.", " m"),
        ("=", "{F} Si cada rollo cuesta $9.000, ¿cuánto cuesta comprar los rollos necesarios para los 44 m?", "2*9000", "Se multiplica el precio de un rollo por la cantidad de rollos.", " pesos"),
    ],
    ctx=("abc", "{F} El comprador de ejemplo dice: «con 40 m me alcanza, la merma es un invento para cobrar más». ¿Qué corresponde?", "Explicar que la merma prevé recortes y pérdidas, y que sin ella pueden faltar metros", "Aceptar, porque 40 m son los del plano", "Aceptar, y completar con cable de otro proyecto si falta", "Sin merma pueden faltar metros, y completar con material no cubicado es improvisar."),
    sc=[
        ("En Electricidad: ¿cómo se pasa una medida del plano a la real?", "Multiplicándola por el número de la escala", "A escala 1:100, 1 cm del plano son 100 cm reales."),
        ("¿Sobre qué se calcula la merma?", "Sobre el total de metros del recorrido", "La merma es un porcentaje del total."),
        ("¿Cómo se calcula cuántos rollos comprar?", "Dividiendo los metros por el largo del rollo y redondeando hacia arriba", "No se compran fracciones de rollo."),
    ],
    op=("Planilla de ejemplo: plano a escala 1:100; recorrido dibujado con tramos de 6 cm, 9 cm, 15 cm y 10 cm; merma de ejemplo 10 %; rollos de 25 m a $8.000 cada uno. Escribe (a) cuántos metros reales suman los tramos, (b) cuántos metros se cubican con merma, (c) cuántos rollos se compran y cuántos metros sobran, (d) cuánto cuesta la compra.",
        "(a) 6+9+15+10 son 40 cm de plano, que a 1:100 son 40 m. (b) El 10 % de 40 es 4: 44 m. (c) 44 dividido por 25, redondeado hacia arriba, son 2 rollos; sobran 50 menos 44, es decir 6 m. (d) 2 por 8.000 son 16.000 pesos.",
        ["suma bien los tramos y aplica la escala", "calcula la merma", "redondea hacia arriba los rollos", "calcula bien el costo"],
        ["hoja con la tabla de cálculos"],
        ["no aplicar la escala", "olvidar la merma", "redondear hacia abajo"],
        "Pregunta: «¿por qué compras 2 rollos y no 1,76?». Si no responde, pídele que relea cómo se calculan las presentaciones."),
    reinforce="Inventa un recorrido con tres tramos a escala 1:50, calcula los metros reales y la merma de 10 %.",
    extend="Explica con un ejemplo por qué la merma no debe calcularse tramo por tramo si la planilla dice sobre el total.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (proyecto de ejemplo, inventado). «Bodega Álamo»: plano a escala 1:100. Elementos contados en el plano: 14 puntos de luz, 10 tomacorrientes, 3 interruptores. "
     "Recorridos dibujados: 60 cm en total para alumbrado y 40 cm en total para tomacorrientes. Merma de ejemplo: 10 % en los recorridos. "
     "Presentaciones de ejemplo: tomacorrientes e interruptores en cajas de 5 unidades; conductor en rollos de 25 m. Precios de ejemplo: punto de luz $3.000; caja de tomacorrientes $9.000; caja de interruptores $6.000; rollo $9.000.")
build(
    O5, 3, F,
    use="Aprenderé a armar una cubicación completa de un proyecto pequeño, paso a paso en papel, y a detectar incoherencias antes de comprar.",
    prior=["Sé aplicar escala y merma.", "Sé calcular presentaciones completas.", "Sé calcular costos."],
    explain=[
        "Una cubicación completa recorre la planilla en orden: primero se cuentan los elementos del plano, después se miden los recorridos y se les aplica escala y merma, luego se convierten las cantidades en presentaciones completas y por último se calcula el costo. Cada resultado se anota con sus datos de origen: qué plano, qué escala, qué precio. Así otra persona puede revisarla y repetirla.",
        "Si el plano y las especificaciones no coinciden, se informa antes de comprar. Si cambia la escala del plano o una cantidad, la cubicación se rehace completa, porque todos los resultados dependen unos de otros. La planilla de esta ficha es un ejemplo para calcular: no entrega ningún dato de conductor real.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("planilla de cubicación", "tabla con cantidades, presentaciones y costos de cada material"), ("elemento del plano", "símbolo contado en el plano, como un punto de luz"), ("trazabilidad", "posibilidad de saber de dónde salió cada dato y repetir el cálculo"), ("rehacer la cubicación", "volver a calcular todo cuando cambia un dato de origen")],
    worked=[
        ("Costo de una partida", "Un proyecto de ejemplo tiene 8 puntos de luz a $2.500 cada uno. ¿Cuánto cuesta esa partida?", ["Se multiplica el precio por la cantidad.", "8 por 2.500 son 20.000."], "$20.000"),
        ("Rollos de un tramo", "Un recorrido cubicado de 60 m se compra en rollos de 25 m. ¿Cuántos rollos hacen falta?", ["Con 2 rollos hay 50 m, no alcanza.", "Con 3 rollos hay 75 m."], "3 rollos"),
    ],
    mistakes=[("Cambiar la escala del plano y corregir solo los metros de un recorrido.", "Todos los resultados que dependen de la escala cambian.", "Rehace la cubicación completa."),
              ("Anotar cantidades sin decir de qué plano o escala salieron.", "Nadie puede revisar ni repetir el cálculo.", "Anota el origen de cada dato.")],
    T=[
        ("abc", "En Electricidad: ¿qué es una planilla de cubicación?", "Una tabla con las cantidades, las presentaciones y los costos de cada material", "Un dibujo del proyecto a escala", "Un contrato entre el cliente y el instalador", "La planilla ordena cantidades y costos; el dibujo es el plano y el contrato es otro documento."),
        ("abc", "En Electricidad: ¿qué se hace primero al cubicar un proyecto?", "Contar los elementos del plano y revisar las especificaciones", "Comprar los materiales más baratos", "Pedir al cliente que elija las cantidades", "Primero se cuenta y se revisa; la compra viene después de calcular."),
        ("=", "Un plano de ejemplo muestra 11 luces y 9 tomacorrientes. ¿Cuántos elementos son?", "11+9", "Se suman las cantidades de cada elemento.", " elementos"),
        ("=", "{F} ¿Cuántos metros reales suman los recorridos de alumbrado, sin merma?", "60*100//100", "Se multiplica por la escala y se pasa a metros.", " m"),
        ("=", "{F} ¿Cuántos metros se cubican para alumbrado con la merma?", "60+60*10//100", "A los 60 m se les suma el 10 %.", " m"),
        ("=", "{F} ¿Cuántos rollos de 25 m se necesitan para alumbrado?", "(66+24)//25", "Se divide por 25 redondeando hacia arriba.", " rollos"),
        ("=", "{F} ¿Cuántos metros se cubican para tomacorrientes con la merma?", "40+40*10//100", "A los 40 m se les suma el 10 %.", " m"),
        ("=", "{F} ¿Cuántas cajas de tomacorrientes se necesitan para los 10 del plano?", "(10+4)//5", "Se divide por 5 redondeando hacia arriba.", " cajas"),
        ("=", "{F} ¿Cuánto cuesta comprar los puntos de luz?", "14*3000", "Se multiplica el precio de un punto de luz por la cantidad.", " pesos"),
        ("abc", "{F} El cubicador nota que el plano dibuja 3 interruptores y las especificaciones piden 4. ¿Qué corresponde?", "Informar la diferencia antes de comprar y esperar la decisión del proyectista", "Comprar 4, porque es más seguro", "Comprar 3, porque el plano manda", "Una diferencia entre plano y especificaciones se informa antes de comprar."),
        ("ab", "{F} El cubicador propone no incluir la merma «para ahorrar». ¿Qué corresponde?", "Mantenerla: la planilla la exige y sin ella pueden faltar metros", "Quitarla, porque las mermas no existen", "La merma está prevista en la planilla; quitarla deja el proyecto con riesgo de faltantes."),
        ("=", "{F} ¿Cuánto cuesta el proyecto completo con los materiales de la planilla (luces, cajas de tomacorrientes, una caja de interruptores y los rollos de alumbrado y tomacorrientes)?", "14*3000+2*9000+1*6000+5*9000", "Se suman el costo de luces, cajas y rollos de ambos recorridos.", " pesos"),
        ("abc", "{F} El cliente cambia el plano a escala 1:50 y los recorridos dibujados miden lo mismo. ¿Qué ocurre con los metros cubicados?", "Se reducen a la mitad, porque cada centímetro del plano equivale a menos metros reales", "Se duplican", "No cambian, porque la escala no importa", "A escala 1:50, cada centímetro del plano equivale a 50 cm reales, la mitad que antes."),
    ],
    ctx=("abc", "{F} Un instalador de ejemplo recibe la planilla con todos los números, pero sin el plano de origen. ¿Qué corresponde?", "Pedir el plano y la escala usados, porque sin origen no se puede revisar la planilla", "Usar la planilla igual, porque los números parecen correctos", "Rehacer la planilla midiendo con regla otro plano", "Sin el origen de los datos no se puede repetir ni verificar el cálculo."),
    sc=[
        ("En Electricidad: ¿qué orden sigue una cubicación completa?", "Contar elementos, medir recorridos con escala y merma, pasar a presentaciones y calcular costos", "Cada paso usa el resultado del anterior."),
        ("¿Qué pasa si cambia la escala del plano?", "Se rehace toda la cubicación", "Los metros dependen de la escala."),
        ("¿Para qué se anota el origen de cada dato?", "Para que otra persona pueda revisar y repetir el cálculo", "Esa posibilidad de repetir el cálculo se llama trazabilidad."),
    ],
    op=("Proyecto de ejemplo «Sala Cedro»: plano a escala 1:100; 8 puntos de luz y 6 tomacorrientes; recorrido total de alumbrado de 30 cm de plano; merma de ejemplo 10 %; rollos de 25 m a $8.000; punto de luz a $2.800; caja de 4 tomacorrientes a $6.000. Escribe (a) los metros cubicados de alumbrado con merma, (b) los rollos necesarios, (c) las cajas de tomacorrientes, (d) el costo total de luces, rollos y cajas.",
        "(a) 30 cm de plano son 30 m; la merma es 3 m: 33 m. (b) 33 dividido por 25, hacia arriba: 2 rollos. (c) 6 dividido por 4, hacia arriba: 2 cajas. (d) 8 por 2.800 son 22.400; 2 rollos son 16.000; 2 cajas son 12.000: total 50.400 pesos.",
        ["aplica escala y merma", "redondea presentaciones hacia arriba", "calcula el costo", "suma bien el total"],
        ["hoja con la tabla de cálculos"],
        ["olvidar la merma", "redondear hacia abajo", "olvidar una partida"],
        "Pregunta: «¿qué cambiaría si el plano estuviera a 1:50?». Si no responde, pídele que relea qué pasa si cambia la escala."),
    reinforce="Inventa una planilla de cubicación con tres partidas y calcula el costo de cada una y el total.",
    extend="Explica con un ejemplo por qué rehacer toda la cubicación es más seguro que corregir un solo número.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (presupuesto de ejemplo, inventado). Cubicación del proyecto «Bodega Álamo»: materiales $111.000 según la planilla. Mano de obra de ejemplo: 36 horas a $4.500 la hora. "
     "Gastos generales de ejemplo: 10 % sobre materiales, despacho y mano de obra. Dos proveedores de ejemplo: Proveedor 1: materiales $111.000 y despacho $6.000; Proveedor 2: materiales $104.000 y despacho $12.000.")
build(
    O5, 4, F,
    use="Aprenderé a armar un presupuesto con materiales, despacho, mano de obra y gastos generales, y a comparar dos proveedores por su costo total.",
    prior=["Sé calcular cantidades de una cubicación.", "Sé calcular porcentajes sencillos.", "Sé comparar costos."],
    explain=[
        "El presupuesto de un proyecto reúne los materiales, el despacho (el costo de llevarlos), la mano de obra y los gastos generales. La mano de obra se calcula con las horas estimadas por el valor de cada hora. Los gastos generales son costos del trabajo que no son un material ni una hora de mano de obra; se estiman como porcentaje del subtotal. El total es el subtotal más los gastos generales.",
        "Para comparar proveedores no basta mirar el precio de los materiales: se suma el despacho y se compara el costo total. Si la diferencia es pequeña, se consideran otros criterios por escrito, como el plazo de entrega. El presupuesto debe mostrar el costo real: no se ocultan costos para que el total parezca menor, y toda decisión se registra con sus criterios y su autorización.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("presupuesto", "documento que reúne los costos del proyecto"), ("subtotal", "suma de materiales, despacho y mano de obra antes de los gastos generales"), ("gastos generales", "costos del trabajo que no son un material ni una hora de mano de obra, estimados como porcentaje"), ("despacho", "costo de llevar los materiales al lugar"), ("costo total", "subtotal más gastos generales")],
    worked=[
        ("Mano de obra", "Un trabajo de ejemplo requiere 20 horas a $5.000 la hora. ¿Cuánto cuesta la mano de obra?", ["Se multiplican las horas por el valor de la hora.", "20 por 5.000 son 100.000."], "$100.000"),
        ("Total con gastos generales", "Un subtotal de ejemplo es de $300.000 y los gastos generales son 10 %. ¿Cuál es el total?", ["El 10 % de 300.000 es 30.000.", "300.000 más 30.000 son 330.000."], "$330.000"),
    ],
    mistakes=[("Elegir un proveedor solo por el precio de los materiales.", "El despacho también es un costo.", "Compara el costo total con despacho."),
              ("Dejar los gastos generales en cero para que el presupuesto parezca más barato.", "Oculta un costo real.", "Incluye todos los costos del proyecto.")],
    T=[
        ("abc", "En Electricidad: ¿qué incluye un presupuesto de proyecto?", "Materiales, despacho, mano de obra y gastos generales", "Solo los materiales", "Solo la mano de obra y la ganancia", "Un presupuesto completo reúne todos los costos; los materiales solos dejarían fuera la mano de obra."),
        ("=", "Una mano de obra de ejemplo de 20 horas a $5.000 la hora, ¿cuánto cuesta?", "20*5000", "Se multiplican las horas por el valor de cada hora.", " pesos"),
        ("abc", "En Electricidad: ¿qué son los gastos generales de un presupuesto?", "Costos del trabajo que no son un material ni una hora de mano de obra, estimados como porcentaje", "El costo de cada material", "El pago al cliente", "Los gastos generales cubren costos que no se asignan a un material ni a una hora."),
        ("=", "{F} ¿Cuánto cuesta la mano de obra del proyecto?", "36*4500", "Se multiplican las horas por el valor de cada hora.", " pesos"),
        ("=", "{F} ¿Cuál es el subtotal con el Proveedor 1, sumando materiales, despacho y mano de obra?", "111000+6000+36*4500", "Se suman los materiales, el despacho y la mano de obra.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los gastos generales sobre el subtotal del Proveedor 1?", "(111000+6000+36*4500)*10//100", "Se calcula el 10 % del subtotal.", " pesos"),
        ("=", "{F} ¿Cuál es el total del presupuesto con el Proveedor 1?", "(111000+6000+36*4500)*110//100", "El subtotal más el 10 % equivale a multiplicar por 110 y dividir por 100.", " pesos"),
        ("=", "{F} ¿Cuánto suman materiales y despacho del Proveedor 2?", "104000+12000", "Se suman los materiales y el despacho.", " pesos"),
        ("abc", "{F} ¿Qué proveedor conviene solo por materiales más despacho?", "El Proveedor 2, con $116.000, contra $117.000", "El Proveedor 1, porque tiene el despacho más barato", "Ninguno, porque cuestan lo mismo", "El Proveedor 1 suma 117.000 y el Proveedor 2 suma 116.000."),
        ("abc", "{F} Un compañero dice que el Proveedor 2 conviene porque sus materiales son $7.000 más baratos. ¿Qué falta considerar?", "El despacho, que es $6.000 mayor; con él la ventaja baja a $1.000", "Nada: el precio de los materiales es lo único que cuenta", "La mano de obra, que cambia según el proveedor", "El despacho cambia el costo total; la mano de obra es la misma con ambos."),
        ("ab", "{F} El jefe pide bajar los gastos generales a cero «para que el presupuesto se vea barato». ¿Qué corresponde?", "No ocultar costos: el presupuesto debe reflejar el costo real y cualquier cambio de criterio se registra", "Hacerlo: el presupuesto puede mostrar menos de lo que cuesta", "Un presupuesto con costos ocultos engaña al cliente y puede dejar el proyecto sin fondos."),
        ("=", "{F} ¿Cuántos pesos menos cuesta el presupuesto total con el Proveedor 2 que con el 1?", "(111000+6000+36*4500)*110//100-(104000+12000+36*4500)*110//100", "Se restan los dos totales con gastos generales.", " pesos"),
        ("abc", "{F} ¿Qué debe quedar en el registro de la decisión del proveedor?", "El proveedor elegido, los totales comparados, los criterios usados y quién autorizó", "Solo el nombre del proveedor", "Solo el precio de los materiales", "El registro permite que otra persona entienda y revise la decisión."),
    ],
    ctx=("abc", "{F} El Proveedor 2 ofrece rebajar el precio si el pago se hace «hoy mismo, sin papeles». ¿Qué corresponde?", "Pedir la oferta por escrito y someterla a la autorización de quien aprueba el presupuesto", "Aceptar, porque es más barato", "Pagar y registrar la decisión después", "Una oferta sin registro ni autorización no es una base confiable para decidir."),
    sc=[
        ("En Electricidad: ¿qué se suma al subtotal para obtener el total?", "Los gastos generales", "El total es el subtotal más los gastos generales."),
        ("¿Qué se compara entre dos proveedores?", "El costo total, incluido el despacho", "Los materiales solos no muestran el costo real."),
        ("¿Por qué no se ocultan costos en un presupuesto?", "Porque debe reflejar el costo real del proyecto", "Ocultar costos engaña a quien decide."),
    ],
    op=("Datos de ejemplo: materiales $150.000; despacho $10.000; mano de obra 24 horas a $5.000 la hora; gastos generales de ejemplo 10 % sobre el subtotal. Otro proveedor ofrece materiales por $140.000 con despacho de $20.000. Escribe (a) la mano de obra, (b) el subtotal con el primer proveedor, (c) el total con gastos generales, (d) qué proveedor conviene por materiales más despacho y por cuánto.",
        "(a) 24 por 5.000 son 120.000 pesos. (b) 150.000+10.000+120.000 son 280.000 pesos. (c) El 10 % es 28.000: total 308.000 pesos. (d) Primer proveedor: 160.000; segundo: 160.000. Cuestan lo mismo; se decide por otro criterio escrito, como el plazo.",
        ["calcula la mano de obra", "calcula el subtotal", "calcula el total con gastos generales", "compara con despacho y concluye que empatan"],
        ["hoja con la tabla de cálculos y la conclusión"],
        ["comparar solo materiales", "olvidar los gastos generales", "elegir sin registrar un criterio"],
        "Pregunta: «¿qué criterio usarías si los dos proveedores cuestan lo mismo?». Si no responde, pídele que relea qué se hace si la diferencia es pequeña."),
    reinforce="Inventa dos proveedores con materiales y despacho distintos y calcula cuál tiene el menor costo total.",
    extend="Explica con un ejemplo por qué un presupuesto con costos ocultos puede perjudicar al cliente y al instalador.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (pauta de mantenimiento de ejemplo, inventada). El taller ficticio «Metal Sur» tiene una pauta con 3 equipos: ventilador V1 (revisión cada 3 meses), bomba B1 (cada 6 meses) y tablero T1 (cada 12 meses). "
     "Cada revisión la hace personal autorizado: V1 consume 2 horas, B1 consume 3 horas y T1 consume 4 horas. Valor de la hora de ejemplo: $6.000. Año de 12 meses.")
build(
    O6, 1, F,
    use="Aprenderé qué es el mantenimiento, qué tipos hay, cómo se planifica en papel y por qué solo lo realiza personal autorizado.",
    prior=["Sé qué es una pauta o una lista de verificación.", "Sé multiplicar y dividir.", "Sé que un trabajo con energía requiere personal autorizado."],
    explain=[
        "El mantenimiento es el conjunto de acciones planificadas para conservar los equipos eléctricos seguros y en funcionamiento. El mantenimiento preventivo se planifica y se hace antes de que el equipo falle. El mantenimiento correctivo se hace después de una falla, que es un evento en que el equipo deja de funcionar como debe. La pauta de mantenimiento es el documento que dice qué equipo se revisa y cada cuánto tiempo, y se elabora con las recomendaciones del fabricante y la norma vigente.",
        "Los equipos monofásicos y trifásicos, los componentes y los sistemas eléctricos se mantienen siempre con personal autorizado, con permiso de trabajo y con las medidas que fija la empresa y la norma vigente de la SEC. Este cuaderno no enseña cómo se interviene un equipo: enseña a leer una pauta, a planificar el tiempo y el costo en papel, y a reconocer los riesgos (descarga, quemadura, incendio, partes en movimiento). Cada revisión se anota en un registro.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "el que se planifica y se hace antes de que el equipo falle"), ("mantenimiento correctivo", "el que se hace después de una falla"), ("falla", "evento en que un equipo deja de funcionar como debe"), ("pauta de mantenimiento", "documento que dice qué equipo se revisa y cada cuánto tiempo"), ("registro", "anotación de lo que se hizo, cuándo y quién")],
    worked=[
        ("Revisiones al año", "Un equipo de ejemplo se revisa cada 4 meses. ¿Cuántas revisiones tiene en un año de 12 meses?", ["Se divide el año por el intervalo.", "12 dividido por 4 son 3."], "3 revisiones"),
        ("Tipo de mantenimiento", "Una bomba de ejemplo deja de funcionar y se repara. ¿Qué tipo de mantenimiento es?", ["La reparación ocurre después de la falla.", "Eso es mantenimiento correctivo."], "Correctivo"),
    ],
    mistakes=[("Saltarse una revisión porque el equipo «nunca ha fallado».", "El mantenimiento preventivo existe para evitar la falla.", "Cumple la pauta; cambiarla lo decide quien la elaboró."),
              ("Creer que un estudiante puede ayudar a revisar un tablero.", "Intervenir equipos exige personal autorizado.", "Aprende a leer la pauta y deja el trabajo al personal autorizado.")],
    T=[
        ("abc", "En Electricidad: ¿qué es el mantenimiento preventivo?", "El que se planifica y se hace antes de que el equipo falle", "El que se hace después de que el equipo falla", "El que se hace solo cuando el cliente reclama", "Preventivo significa anticiparse a la falla; el que sigue a la falla es el correctivo."),
        ("abc", "En Electricidad: ¿qué es una pauta de mantenimiento?", "El documento que indica qué se revisa en cada equipo y cada cuánto tiempo", "El plano del taller con las cotas", "La factura por el servicio", "La pauta programa las revisiones; el plano y la factura cumplen otras funciones."),
        ("=", "Un equipo de ejemplo se revisa cada 2 meses. ¿Cuántas revisiones tiene en un año de 12 meses?", "12//2", "Se divide el año por el intervalo entre revisiones.", " revisiones"),
        ("=", "{F} ¿Cuántas revisiones tiene V1 en un año?", "12//3", "Se divide el año por el intervalo de 3 meses.", " revisiones"),
        ("=", "{F} ¿Cuántas horas de personal autorizado consume V1 en el año?", "12//3*2", "Se multiplican las revisiones del año por las horas de cada una.", " horas"),
        ("abc", "{F} ¿Qué equipo de la ficha tiene la revisión menos frecuente?", "El tablero T1, cada 12 meses", "El ventilador V1, cada 3 meses", "La bomba B1, cada 6 meses", "Cada 12 meses es el intervalo más largo, es decir, la revisión menos frecuente."),
        ("=", "{F} ¿Cuántas horas suman las revisiones anuales de los tres equipos?", "12//3*2+12//6*3+12//12*4", "Se suman las horas anuales de cada equipo.", " horas"),
        ("=", "{F} ¿Cuánto cuesta ese tiempo de personal al año?", "(12//3*2+12//6*3+12//12*4)*6000", "Se multiplican las horas anuales por el valor de la hora.", " pesos"),
        ("abc", "{F} Un jefe sugiere saltarse la revisión de T1 este año «porque nunca ha fallado». ¿Qué corresponde?", "Cumplir la pauta: el mantenimiento preventivo evita fallas, y cambiarla lo decide quien la elaboró", "Saltarla: si nunca ha fallado, no hace falta", "Hacerla solo si el tablero da señales de falla", "El preventivo se hace precisamente antes de que haya señales."),
        ("abc", "{F} Un estudiante propone revisar el tablero T1 para ayudar. ¿Qué responde un adulto responsable?", "No: intervenir un tablero exige personal autorizado, permiso de trabajo y norma vigente", "Sí, si usa casco", "Sí, si la revisión es corta", "El casco o la corta duración no reemplazan la autorización."),
        ("ab", "{F} La bomba B1 falla antes de su revisión programada. ¿Qué tipo de mantenimiento corresponde?", "Correctivo, porque se hace después de la falla", "Preventivo, porque estaba en la pauta", "Una falla que ya ocurrió se atiende con mantenimiento correctivo."),
        ("=", "{F} Se agrega a la pauta un equipo con revisión cada 4 meses de 2 horas. ¿Cuántas horas anuales suma la pauta ahora?", "12//3*2+12//6*3+12//12*4+12//4*2", "Se suman a las 18 horas anteriores las del equipo nuevo.", " horas"),
        ("abc", "Un trabajador de un taller de ejemplo sufre una quemadura durante una revisión. ¿Qué indican las reglas generales?", "Avisar a un adulto responsable y a emergencias, y no tocar a la persona si sigue en contacto con la energía; el suministro se corta solo si se está autorizado", "Seguir con la revisión para no perder tiempo", "Tratarlo en el taller sin avisar a nadie", "Seguir o callar retrasa la ayuda; las reglas generales piden avisar y no tocar si hay contacto con la energía."),
    ],
    ctx=("abc", "{F} El dueño del taller dice que prefiere esperar a que falle la bomba B1 «para no gastar horas en revisiones». ¿Qué corresponde explicar?", "Que el mantenimiento preventivo cuesta horas planificadas, pero evita fallas y riesgos que salen más caros", "Que esperar la falla siempre sale más barato que revisar", "Que las revisiones no tienen relación con los riesgos", "El preventivo planifica el costo y reduce el riesgo; esperar a la falla puede ser más caro y peligroso."),
    sc=[
        ("En Electricidad: ¿qué es la falla de un equipo?", "Un evento en que el equipo deja de funcionar como debe", "La falla es lo que el mantenimiento preventivo busca evitar."),
        ("¿Quién interviene un equipo eléctrico en un mantenimiento?", "Personal autorizado, con permiso de trabajo y norma vigente", "Este cuaderno no habilita para intervenir equipos."),
        ("¿Qué se anota después de cada revisión?", "Un registro de lo hecho, la fecha y quién lo hizo", "El registro deja constancia y permite revisar el trabajo."),
    ],
    op=("Pauta de ejemplo del taller «Fragua Oeste»: compresor C1 (revisión cada 2 meses, 3 horas); tablero T2 (cada 6 meses, 4 horas); bomba B2 (cada 4 meses, 2 horas). Valor de la hora: $5.000. Año de 12 meses. Escribe (a) cuántas revisiones tiene cada equipo al año, (b) cuántas horas anuales suma la pauta, (c) cuánto cuesta ese tiempo, (d) qué tipo de mantenimiento es una reparación después de que C1 se detiene y quién la realiza.",
        "(a) C1: 6; T2: 2; B2: 3. (b) 6 por 3=18; 2 por 4=8; 3 por 2=6: 32 horas. (c) 32 por 5.000 son 160.000 pesos. (d) Mantenimiento correctivo; lo realiza personal autorizado con permiso de trabajo y norma vigente.",
        ["calcula las revisiones", "suma las horas", "calcula el costo", "clasifica el mantenimiento y nombra quién lo hace"],
        ["hoja con la tabla de cálculos y las respuestas"],
        ["dividir mal el año", "olvidar un equipo", "decir que cualquiera puede repararlo"],
        "Pregunta: «¿qué tipo de mantenimiento evita la falla?». Si no responde, pídele que relea la diferencia entre preventivo y correctivo."),
    reinforce="Inventa una pauta con tres equipos y calcula cuántas revisiones y horas tiene cada uno en un año.",
    extend="Explica con un ejemplo por qué una pauta escrita ayuda a que no se olviden revisiones importantes.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (orden de trabajo de ejemplo, inventada). Orden N.º 15 (de ejemplo) del taller «Metal Sur». Equipo: ventilador V1, alimentación monofásica de 220 V, potencia 250 W. "
     "Tipo de trabajo: mantenimiento preventivo. Responsable autorizado: Técnico R. (ficticio). Permiso de trabajo: pendiente de firma del jefe. "
     "Recomendación del fabricante (de ejemplo): revisar cada 3 meses. Registro de cierre: sin completar.")
build(
    O6, 2, F,
    use="Aprenderé a leer una orden de trabajo, un permiso y las recomendaciones del fabricante, y a distinguir alimentación monofásica y trifásica en papel.",
    prior=["Sé qué es mantenimiento preventivo y correctivo.", "Sé leer una placa de características.", "Sé que un documento debe estar completo antes de actuar."],
    explain=[
        "Una orden de trabajo es el documento que describe y autoriza un trabajo: qué equipo, qué tipo de trabajo, quién es el responsable autorizado y cuándo. El permiso de trabajo es una autorización escrita de la persona responsable para que personal autorizado intervenga un equipo; sin el permiso firmado, el trabajo no comienza. Las recomendaciones del fabricante son las instrucciones de uso y mantención que da quien fabricó el equipo, y no se cambian por costumbre. El registro de cierre se completa al terminar: qué se hizo, quién lo verificó y la fecha.",
        "Los equipos pueden tener alimentación monofásica, con una fase y un neutro, o trifásica, con tres fases. El tipo y la tensión están en la placa y deben coincidir con los del lugar. Si algo no coincide, se informa al responsable; no se adapta el equipo por cuenta propia. La bitácora es el registro cronológico de todos los trabajos de un equipo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("orden de trabajo", "documento que describe y autoriza un trabajo"), ("permiso de trabajo", "autorización escrita de la persona responsable para intervenir un equipo"), ("recomendaciones del fabricante", "instrucciones de uso y mantención dadas por quien fabricó el equipo"), ("registro de cierre", "anotación final de qué se hizo, quién lo verificó y la fecha"), ("bitácora", "registro cronológico de los trabajos de un equipo"), ("fase y neutro", "conductores de la alimentación: la fase lleva la energía al equipo y el neutro es el retorno")],
    worked=[
        ("Revisiones en tres años", "El fabricante recomienda revisar un equipo de ejemplo cada 6 meses. ¿Cuántas revisiones hay en 3 años (36 meses)?", ["Se divide el período por el intervalo.", "36 dividido por 6 son 6."], "6 revisiones"),
        ("Campo faltante", "Una orden de ejemplo tiene equipo, responsable y fecha, pero el permiso está sin firmar. ¿Puede comenzar el trabajo?", ["El permiso firmado es un requisito previo.", "Sin él, no comienza."], "No, falta la firma del permiso"),
    ],
    mistakes=[("Empezar un trabajo mientras «el permiso se firma después».", "El permiso debe estar firmado antes de intervenir.", "Espera la firma y registra la hora."),
              ("Cambiar el intervalo de revisión por costumbre del taller.", "La recomendación del fabricante se respeta o se cambia con quien elaboró la pauta.", "Registra la diferencia y consulta.")],
    T=[
        ("abc", "En Electricidad: ¿qué es una orden de trabajo?", "El documento que describe y autoriza un trabajo", "La placa de características de un equipo", "El plano de la instalación", "La orden de trabajo identifica y autoriza el trabajo; la placa y el plano son otros documentos."),
        ("abc", "En Electricidad: ¿qué es un permiso de trabajo?", "Una autorización escrita de la persona responsable para que personal autorizado intervenga un equipo", "Un plano que muestra por dónde pasan los circuitos", "La etiqueta con los datos del equipo", "El permiso autoriza la intervención; el plano y la etiqueta describen otras cosas."),
        ("abc", "¿Qué diferencia hay entre alimentación monofásica y trifásica?", "La monofásica usa una fase y un neutro; la trifásica usa tres fases", "La monofásica tiene más tensión que la trifásica", "La trifásica se usa solo en casas", "Se distinguen por el número de fases."),
        ("abc", "{F} ¿Qué falta en la orden antes de que el trabajo pueda comenzar?", "La firma del permiso de trabajo", "El registro de cierre, que es lo primero", "El cambio del tipo de trabajo a correctivo", "El permiso firmado es requisito previo; el cierre se completa al terminar."),
        ("abc", "{F} ¿Cuándo se completa el registro de cierre?", "Al terminar el trabajo, con lo que se hizo y quién lo verificó", "Antes de empezar, para ahorrar tiempo", "Solo si hubo un accidente", "El cierre deja constancia de lo realizado, así que se completa al final."),
        ("=", "{F} El fabricante recomienda revisar V1 cada 3 meses. ¿Cuántas revisiones hay en 2 años (24 meses)?", "24//3", "Se divide el período por el intervalo.", " revisiones"),
        ("=", "{F} Cada revisión de V1 consume 2 horas a $6.000 la hora. ¿Cuánto cuestan las revisiones de 12 meses?", "12//3*2*6000", "Se multiplican las revisiones por las horas y por el valor de la hora.", " pesos"),
        ("abc", "{F} El fabricante recomienda revisar cada 3 meses, pero el jefe dice «cada 6, siempre se hizo así». ¿Qué corresponde?", "Registrar la diferencia y consultar con quien elaboró la pauta; la recomendación del fabricante no se cambia por costumbre", "Seguir al jefe, porque la costumbre es más importante", "Seguir al fabricante sin informar a nadie", "Una diferencia se registra y se consulta; no se resuelve por costumbre ni en silencio."),
        ("abc", "{F} Un técnico dice que empezará el trabajo y que el permiso «se firma después». ¿Qué corresponde?", "No empezar: el permiso debe estar firmado antes de intervenir", "Empezar si el trabajo es corto", "Empezar si avisa por mensaje", "La duración o el aviso informal no reemplazan el permiso firmado."),
        ("ab", "La placa de un compresor de ejemplo dice «trifásico», pero el local solo tiene alimentación monofásica. ¿Qué corresponde?", "Informar al responsable: el equipo no coincide con la alimentación del local", "Conectarlo de todos modos, porque el motor se ajusta solo", "Un equipo que no coincide con la alimentación no se adapta por cuenta propia."),
        ("=", "Un compresor monofásico de ejemplo de 1760 W funciona a 220 V. ¿Cuántos amperios usa?", "1760//220", "La corriente es la potencia dividida por la tensión.", " A"),
        ("abc", "{F} Tras el trabajo, el registro de cierre dice solo «listo». ¿Qué le falta?", "Qué se hizo, quién lo verificó y la fecha", "El precio del equipo", "El plano del taller", "El cierre debe dejar constancia de lo hecho, de quién lo verificó y de cuándo."),
        ("=", "{F} Si se agrega una segunda revisión anual de 4 horas a $6.000 la hora, además de las 4 revisiones de V1 de 2 horas, ¿cuántos pesos suman las horas anuales de V1?", "(12//3*2+4)*6000", "Se suman las horas de las revisiones y se multiplican por el valor de la hora.", " pesos"),
    ],
    ctx=("abc", "{F} Un estudiante en práctica ve que la orden tiene el permiso sin firmar y que el técnico ya abrió el equipo. ¿Qué hace?", "Avisa a un adulto responsable y no participa en el trabajo", "Ayuda para terminar más rápido", "Firma él mismo el permiso", "Un trabajo sin permiso firmado es un riesgo; quien no está autorizado avisa y se mantiene al margen."),
    sc=[
        ("En Electricidad: ¿cuándo debe estar firmado el permiso de trabajo?", "Antes de intervenir el equipo", "El permiso es un requisito previo."),
        ("¿Qué se hace si el tipo de alimentación del equipo no coincide con el del local?", "Se informa al responsable", "No se adapta el equipo por cuenta propia."),
        ("¿Qué dice el registro de cierre?", "Qué se hizo, quién lo verificó y la fecha", "Deja constancia por escrito del trabajo realizado y quién lo verificó."),
    ],
    op=("Orden de ejemplo N.º 22 del taller «Fragua Oeste»: equipo: compresor C1, alimentación trifásica (de ejemplo), tipo de trabajo: mantenimiento preventivo, permiso de trabajo firmado, registro de cierre vacío. Recomendación del fabricante: revisar cada 4 meses. Cada revisión consume 3 horas a $5.000 la hora. Escribe (a) cuántas revisiones hay en 12 meses, (b) cuánto cuestan las horas anuales, (c) si el trabajo puede comenzar y por qué, (d) qué debe completarse al terminar.",
        "(a) 12 dividido por 4 son 3 revisiones. (b) 3 por 3 son 9 horas; 9 por 5.000 son 45.000 pesos. (c) Sí, porque el permiso está firmado y lo realiza personal autorizado. (d) El registro de cierre: qué se hizo, quién lo verificó y la fecha.",
        ["calcula las revisiones", "calcula el costo", "justifica con el permiso", "indica el contenido del cierre"],
        ["hoja con las cuatro respuestas"],
        ["no usar el permiso como condición", "olvidar el valor de la hora", "dejar el cierre vacío"],
        "Pregunta: «¿qué falta antes de comenzar si el permiso no estuviera firmado?». Si no responde, pídele que relea qué es un permiso de trabajo."),
    reinforce="Escribe una orden de trabajo de ejemplo con cinco campos (equipo, tipo, responsable, permiso y recomendación) y márcalos como completos o incompletos.",
    extend="Explica con un ejemplo por qué un permiso firmado antes protege a las personas y al equipo.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (solicitud de reemplazo de ejemplo, inventada). Componente a reemplazar: ventilador V1 del taller «Metal Sur». Datos del original: 250 W, 220 V, monofásico, vida útil 20.000 h, caudal de aire 600 (unidad de ejemplo). "
     "Opciones de repuesto (ficticias, sin marca): R1: 250 W, 220 V, monofásico, 25.000 h, caudal 600, $38.000; R2: 250 W, 380 V (de ejemplo), trifásico, 25.000 h, caudal 600, $30.000; "
     "R3: 300 W, 220 V, monofásico, 25.000 h, caudal 650, $35.000; R4: 250 W, 220 V, monofásico, 15.000 h, caudal 600, $28.000. "
     "Criterio de equivalencia de la orden: misma potencia, misma tensión, mismo tipo de alimentación, vida útil igual o mayor y caudal igual o mayor.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel una solicitud de reemplazo, a comprobar la equivalencia técnica de un repuesto y a decidir quién autoriza el cambio.",
    prior=["Sé leer una placa de características.", "Sé qué es una orden de trabajo.", "Sé comparar opciones con requisitos."],
    explain=[
        "Reemplazar un componente en un equipo es una decisión que se toma primero en papel. Un repuesto es técnicamente equivalente cuando cumple los mismos datos que se exigen del original: potencia, tensión, tipo de alimentación y, según la orden, otros como vida útil o caudal. Se compara cada dato del repuesto con la placa del original y con el criterio de la orden, uno por uno. Si falla uno, el repuesto no es equivalente y se descarta, aunque sea más barato o tenga un dato mejor.",
        "Si no hay un repuesto equivalente, no se improvisa: se informa al responsable de la orden, que decide si se cambia el criterio y quién lo autoriza. El reemplazo mismo lo hace personal autorizado con permiso de trabajo y la norma vigente; este cuaderno no enseña cómo. El registro del reemplazo guarda los datos del original, los del repuesto, la comparación y la autorización.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("equivalencia técnica", "cumplir los mismos datos exigidos del componente original"), ("repuesto", "pieza que reemplaza a otra en un equipo"), ("vida útil", "horas de funcionamiento previstas por el fabricante"), ("caudal", "cantidad de aire que mueve un ventilador, medida en una unidad de ejemplo"), ("criterio de equivalencia", "lista de datos que el repuesto debe cumplir")],
    worked=[
        ("Comparar un dato", "El original de ejemplo es de 400 W y un repuesto de ejemplo es de 500 W. ¿Cumple la misma potencia?", ["Se compara con el dato del original.", "500 W es distinto de 400 W."], "No cumple"),
        ("Presupuesto de repuestos", "Un repuesto de ejemplo cuesta $20.000 y se necesitan 3. ¿Cuánto cuestan?", ["Se multiplica el precio por la cantidad.", "20.000 por 3 son 60.000."], "$60.000"),
    ],
    mistakes=[("Aceptar un repuesto con más potencia porque «más es mejor».", "La orden exige la misma potencia.", "Compara cada dato con el criterio, sin suponer mejoras."),
              ("Elegir un repuesto sin dejar registro de la comparación.", "Nadie puede revisar por qué se eligió.", "Anota original, repuesto y comparación.")],
    T=[
        ("abc", "En Electricidad: ¿qué significa que un repuesto sea técnicamente equivalente?", "Que cumple los mismos datos exigidos del componente original, como potencia, tensión y alimentación", "Que tiene el mismo color y tamaño", "Que cuesta lo mismo que el original", "La equivalencia técnica compara datos de funcionamiento; el color, el tamaño o el precio no la aseguran."),
        ("abc", "En Electricidad: ¿qué se compara primero al elegir un repuesto?", "Sus datos con los de la placa del original y con el criterio de la orden", "Su precio con el de los demás repuestos", "Su apariencia con la del original", "Primero se comprueba que cumpla lo exigido; el precio se mira después."),
        ("=", "Un repuesto de ejemplo cuesta $38.000 y se necesitan 3. ¿Cuánto cuestan?", "38000*3", "Se multiplica el precio por la cantidad.", " pesos"),
        ("abc", "{F} ¿Qué opción tiene una potencia distinta de la del original?", "Solo R3, con 300 W", "R2 y R3", "Solo R4", "R3 es la única con 300 W; las demás tienen 250 W."),
        ("abc", "{F} ¿Por qué se descarta R2?", "Su tensión y su tipo de alimentación no coinciden con los del original", "Su vida útil es menor que la del original", "Su caudal es menor que el del original", "R2 es de 380 V y trifásico, y el original es de 220 V y monofásico."),
        ("abc", "{F} ¿Por qué se descarta R4?", "Su vida útil de 15.000 h es menor que las 20.000 h del original", "Su potencia no coincide", "Su alimentación no coincide", "R4 coincide en potencia y alimentación; falla en vida útil."),
        ("abc", "{F} ¿Qué opción cumple todo el criterio de equivalencia?", "R1", "R3", "R4", "Solo R1 cumple potencia, tensión, alimentación, vida útil y caudal."),
        ("=", "{F} ¿Cuánto cuestan 2 repuestos de la opción que cumple?", "2*38000", "Se multiplica el precio de R1 por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuántas horas más de vida útil tiene la opción que cumple respecto del original?", "25000-20000", "Se resta la vida útil del original a la del repuesto.", " horas"),
        ("abc", "{F} Un compañero propone R4 porque «es la más barata y el ventilador casi no se usa». ¿Qué respuesta es correcta?", "R4 incumple el criterio de vida útil; solo quien elabora la orden puede cambiar el criterio", "Es válido: si se usa poco, la vida útil no importa", "Es válido si se anota el ahorro", "El criterio se cumple o no; cambiarlo lo decide quien elabora la orden."),
        ("ab", "{F} R1 no está en bodega y el proveedor ofrece R3 «que es mejor porque tiene más potencia y caudal». ¿Qué corresponde?", "No usarla sin autorización: no cumple la misma potencia; se informa al responsable de la orden", "Usarla: más potencia siempre es mejor", "La orden exige la misma potencia; un cambio de criterio lo autoriza el responsable."),
        ("=", "{F} Si el presupuesto para repuestos es de $120.000 y cada R1 cuesta $38.000, ¿cuántos R1 se pueden comprar como máximo?", "120000//38000", "El presupuesto se divide por el precio y se toma la parte entera.", " repuestos"),
        ("abc", "{F} El registro del reemplazo debe poder demostrar que el repuesto es equivalente. ¿Qué anotar?", "Los datos de la placa del original, los del repuesto, la comparación y quién autorizó", "Solo el nombre del repuesto", "Solo el precio pagado", "Para demostrar la equivalencia hay que dejar los dos grupos de datos y su comparación."),
    ],
    ctx=("abc", "{F} El taller de ejemplo no tiene R1 ni plazo para esperarlo, y alguien propone usar R4 «provisoriamente». ¿Qué corresponde?", "Informar al responsable de la orden, que decide si se acepta un cambio de criterio y quién lo autoriza", "Usar R4 y registrar después", "Usar R3 porque es más potente", "Un cambio de criterio, aunque sea provisorio, lo autoriza el responsable y queda registrado."),
    sc=[
        ("En Electricidad: ¿cuándo se descarta un repuesto?", "Cuando falla en cualquier dato del criterio", "Un solo dato incumplido basta para descartarlo."),
        ("¿Quién decide si se cambia el criterio de equivalencia?", "El responsable de la orden", "Quien compra o instala no cambia el criterio por su cuenta."),
        ("¿Qué datos se comparan con el repuesto?", "Los de la placa del original y los del criterio de la orden", "Así se comprueba la equivalencia técnica."),
    ],
    op=("Original de ejemplo: motor de 550 W, 220 V, monofásico, vida útil 18.000 h. Criterio: misma potencia, tensión y alimentación, y vida útil igual o mayor. Repuestos de ejemplo: S1: 550 W, 220 V, monofásico, 20.000 h, $52.000; S2: 550 W, 220 V, monofásico, 12.000 h, $40.000; S3: 750 W, 220 V, monofásico, 22.000 h, $48.000. Escribe (a) qué repuestos cumplen y por qué los otros no, (b) cuánto cuestan 2 de la opción que cumple, (c) qué anotas en el registro, (d) qué haces si S1 no estuviera disponible.",
        "(a) Cumple solo S1; S2 falla en vida útil (12.000 menor que 18.000) y S3 en potencia (750 W distinta de 550 W). (b) 2 por 52.000 son 104.000 pesos. (c) Datos del original, datos de S1, la comparación y quién autorizó. (d) Informo al responsable de la orden y espero su decisión; no uso S2 ni S3 por mi cuenta.",
        ["compara todos los datos", "calcula bien el costo", "propone un registro completo", "informa en lugar de improvisar"],
        ["hoja con la tabla de comparación y las respuestas"],
        ["elegir S3 por tener más potencia", "elegir S2 por precio", "improvisar sin informar"],
        "Pregunta: «¿por qué S3 no sirve aunque tenga más vida útil?». Si no responde, pídele que relea qué pasa cuando falla un dato."),
    reinforce="Inventa un original con cuatro datos y tres repuestos; indica cuál cumple y por qué los otros no.",
    extend="Explica con un ejemplo por qué un repuesto con mejores datos igual puede no ser equivalente.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (análisis de riesgo de ejemplo, inventado). Tarea planificada en papel: mantenimiento preventivo de una bomba con partes en movimiento y alimentación eléctrica. "
     "Peligros identificados: descarga eléctrica, atrapamiento por partes en movimiento y quemadura por superficie caliente. Controles propuestos: C1: resguardo físico que cubre las partes en movimiento; "
     "C2: casco, guantes aislantes y calzado de seguridad; C3: permiso de trabajo y capacitación del personal; C4: reemplazar la bomba por otra de menor peligro; C5: cartel de advertencia en la zona.")
build(
    O6, 4, F,
    use="Aprenderé la jerarquía de controles, qué son los elementos de protección personal y la señalética, para analizar riesgos de un mantenimiento sin realizar ninguna tarea.",
    prior=["Sé qué riesgos tiene una instalación eléctrica.", "Sé qué es un permiso de trabajo.", "Sé qué es prevención."],
    explain=[
        "La jerarquía de controles ordena las medidas de prevención de la más a la menos efectiva. Primero, eliminar el peligro. Segundo, sustituirlo por uno menor. Tercero, los controles de ingeniería, que son protecciones físicas del equipo, como un resguardo. Cuarto, los controles administrativos, como permisos, capacitación, turnos y señalética. Último, los elementos de protección personal (EPP), como casco, guantes aislantes y calzado de seguridad. El EPP es el último recurso y nunca reemplaza a los controles anteriores.",
        "La señalética usa colores: rojo para prohibición y equipos contra incendio, amarillo para advertencia, azul para obligación (por ejemplo, uso de EPP) y verde para condición segura. En muchas empresas existe además un sistema de bloqueo y etiquetado que impide que un equipo se energice mientras personal autorizado trabaja en él; cómo se aplica lo fija la norma vigente y la empresa, y solo lo aplica personal autorizado. Este cuaderno no enseña ese sistema.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("control de ingeniería", "protección física del equipo, como un resguardo"), ("control administrativo", "medida de organización, como permisos, capacitación o señalética"), ("EPP", "elementos de protección personal; es el último recurso"), ("señalética", "carteles con colores y símbolos que advierten, prohíben u obligan"), ("bloqueo y etiquetado", "sistema de la empresa que impide energizar un equipo mientras se trabaja en él; lo aplica solo personal autorizado")],
    worked=[
        ("Clasificar un control", "Un resguardo físico cubre las partes en movimiento de una máquina de ejemplo. ¿A qué nivel de la jerarquía pertenece?", ["Es una protección física del equipo.", "Eso es un control de ingeniería."], "Control de ingeniería"),
        ("Color de la señal", "Un cartel de ejemplo dice «Uso obligatorio de casco». ¿Qué color corresponde?", ["Es una señal de obligación.", "La obligación usa el azul."], "Azul"),
    ],
    mistakes=[("Creer que el EPP basta y que se pueden omitir los controles anteriores.", "El EPP es el último recurso de la jerarquía.", "Aplica primero los controles más altos y usa el EPP además."),
              ("Creer que leer sobre el bloqueo y etiquetado permite aplicarlo.", "Solo lo aplica personal autorizado, con la norma vigente.", "Reconoce el concepto y deja su aplicación al personal autorizado.")],
    T=[
        ("abc", "En Electricidad: ¿cuál es la idea de la jerarquía de controles?", "Preferir las medidas que eliminan o reducen el peligro en su origen antes que las que solo protegen a la persona", "Usar siempre los elementos de protección personal primero", "Elegir siempre la medida más barata", "La jerarquía ordena de la más a la menos efectiva; el EPP queda al final."),
        ("abc", "En Electricidad: ¿qué color tiene la señal de obligación, como «uso obligatorio de casco»?", "Azul", "Rojo", "Amarillo", "El azul indica obligación; el rojo, prohibición, y el amarillo, advertencia."),
        ("abc", "En Electricidad: ¿qué es un EPP?", "Un elemento de protección personal, que se usa como último recurso además de los controles anteriores", "Un permiso escrito para intervenir un equipo", "Un resguardo que cubre partes en movimiento", "El EPP protege a la persona; el permiso es administrativo y el resguardo es de ingeniería."),
        ("abc", "{F} ¿A qué nivel de la jerarquía pertenece el control C1, el resguardo físico?", "Control de ingeniería", "EPP", "Control administrativo", "Un resguardo es una protección física del equipo."),
        ("abc", "{F} ¿A qué nivel pertenece el control C3, el permiso de trabajo y la capacitación?", "Control administrativo", "Control de ingeniería", "Sustitución", "El permiso y la capacitación son medidas de organización."),
        ("abc", "{F} ¿A qué nivel pertenece C4, reemplazar la bomba por otra de menor peligro?", "Sustitución", "EPP", "Control administrativo", "Cambiar por algo menos peligroso es sustituir."),
        ("abc", "{F} Entre C1 (resguardo físico) y C2 (casco y guantes), ¿cuál es preferible según la jerarquía?", "C1, porque es un control de ingeniería y el EPP es el último recurso", "C2, porque el EPP es el control más efectivo", "Ambos son iguales", "La jerarquía prefiere el resguardo físico al EPP."),
        ("abc", "{F} ¿Qué color debe tener el cartel C5, de advertencia?", "Amarillo", "Verde", "Azul", "El amarillo es el color de las señales de advertencia."),
        ("=", "{F} El taller necesita 1 cartel de advertencia por cada peligro identificado y 2 carteles de obligación de EPP. ¿Cuántos carteles son en total?", "3+2", "Se suman un cartel por cada uno de los 3 peligros y los 2 de obligación.", " carteles"),
        ("abc", "{F} El jefe dice: «con casco y guantes (C2) basta; no hace falta el resguardo». ¿Qué respuesta es correcta?", "No: el EPP es el último recurso; primero se aplican controles más altos como el resguardo", "Sí: el EPP es el control más seguro", "Sí, si los guantes son nuevos", "El EPP no sustituye a los controles de niveles superiores."),
        ("ab", "{F} Un trabajador dice que no necesita permiso de trabajo porque se puso el casco y los guantes. ¿Qué corresponde?", "El permiso es un control administrativo distinto: el EPP no lo reemplaza", "Tiene razón: el EPP reemplaza el permiso", "Cada nivel de la jerarquía cumple una función distinta y ninguno sustituye a otro."),
        ("abc", "El sistema de bloqueo y etiquetado de una empresa de ejemplo impide energizar un equipo durante un trabajo. ¿Quién lo aplica?", "Solo personal autorizado, con la norma vigente y las reglas de la empresa; este cuaderno no enseña cómo", "Cualquier estudiante que haya leído este cuaderno", "El cliente, cuando pide una revisión", "Es una tarea de personal autorizado; leer sobre el concepto no habilita."),
        ("=", "Tres trabajadores de ejemplo necesitan cada uno casco ($8.000), guantes aislantes ($15.000) y calzado ($30.000), todos valores de ejemplo. ¿Cuánto cuesta el EPP del equipo?", "3*(8000+15000+30000)", "Se suma el EPP de un trabajador y se multiplica por 3.", " pesos"),
    ],
    ctx=("abc", "{F} Una empresa de ejemplo compra EPP para todos pero no instala el resguardo ni emite permisos «para ahorrar». ¿Qué observa un revisor?", "Que el EPP no reemplaza los controles superiores y que faltan el resguardo y el permiso", "Que todo está correcto, porque hay EPP", "Que los permisos son opcionales si hay EPP", "El EPP es el último recurso; sin resguardo ni permiso el riesgo sigue sin control."),
    sc=[
        ("En Electricidad: ¿cuál es el último nivel de la jerarquía de controles?", "Los elementos de protección personal", "El EPP es el último recurso."),
        ("¿Qué color tiene la señal de prohibición?", "Rojo", "El rojo indica prohibición y equipos contra incendio."),
        ("¿Quién aplica el bloqueo y etiquetado?", "Solo personal autorizado", "Este cuaderno no habilita para hacerlo."),
    ],
    op=("Análisis de ejemplo de una tarea planificada en papel: revisión de un compresor con peligros de descarga eléctrica, atrapamiento y ruido. Controles propuestos: (1) resguardo que cubre las partes que giran; (2) protectores auditivos y calzado de seguridad; (3) permiso de trabajo y capacitación; (4) cartel de advertencia. Escribe (a) a qué nivel de la jerarquía pertenece cada control, (b) cuál es el más preferible y por qué, (c) qué color tiene el cartel, (d) qué mensaje daría el control (3) a un estudiante que quisiera ayudar.",
        "(a) 1: control de ingeniería; 2: EPP; 3: control administrativo; 4: control administrativo (señalética). (b) El 1, porque protege en el origen y el EPP es el último recurso. (c) Amarillo, por ser una advertencia. (d) Que solo personal autorizado con permiso interviene el equipo; el estudiante no ayuda.",
        ["clasifica los cuatro controles", "elige el más preferible con la razón", "indica el color correcto", "explica el papel del permiso"],
        ["hoja con la tabla y las respuestas"],
        ["decir que el EPP es lo mejor", "confundir permiso con ingeniería", "decir que el estudiante puede ayudar"],
        "Pregunta: «¿por qué el EPP queda al final?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Inventa una tarea con dos peligros y escribe un control para cada nivel de la jerarquía.",
    extend="Explica con un ejemplo por qué un cartel no reemplaza a un resguardo físico.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (decisión de ejemplo, inventada). Bomba B1 del taller «Metal Sur». Opción 1: seguir con mantenimiento correctivo: 5 fallas al año; cada falla cuesta $40.000 en piezas y 4 horas de personal a $6.000 la hora, y deja la bomba 8 horas detenida. "
     "Opción 2: reemplazar la bomba por una nueva de $600.000 con 1 falla al año (mismos costos por falla) y mantenimiento preventivo de 6 horas al año al mismo valor de la hora.")
build(
    O6, 5, F,
    use="Aprenderé a comparar seguir reparando con reemplazar un equipo, a usar indicadores de mantenimiento y a dejar un registro de cierre completo.",
    prior=["Sé qué es una falla y qué es mantenimiento preventivo y correctivo.", "Sé calcular costos anuales.", "Sé qué es un registro."],
    explain=[
        "Un indicador de mantenimiento es un dato que se mide y se registra para evaluar el desempeño: el número de fallas al año, las horas que el equipo queda detenido o el costo anual. Para decidir entre seguir reparando y reemplazar se compara el costo anual de cada opción, se suma la inversión de la compra y se observa en cuántos años el ahorro la recupera. Una opción que parece barata hoy puede costar más cada año.",
        "Cuando el trabajo termina, el registro de cierre debe dejar constancia de qué se reemplazó, los datos del repuesto, quién autorizó y verificó, la fecha y las observaciones. La decisión de reemplazar la toma el responsable del taller con esos datos; el trabajo mismo lo hace personal autorizado con permiso y norma vigente. Los costos de esta ficha son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("indicador", "dato que se mide y se registra para evaluar el desempeño"), ("inversión", "dinero que se paga de una vez para obtener un beneficio después"), ("costo anual", "suma de todos los costos de un equipo en un año"), ("horas detenida", "horas en que el equipo no funciona por una falla"), ("registro de cierre", "constancia final de qué se hizo, con quién lo autorizó y verificó")],
    worked=[
        ("Costo de una falla", "Una falla de ejemplo cuesta $30.000 en piezas y 2 horas de personal a $5.000 la hora. ¿Cuánto cuesta la falla?", ["Las horas de personal cuestan 2 por 5.000, es decir, 10.000.", "30.000 más 10.000 son 40.000."], "$40.000"),
        ("Ahorro acumulado", "Una opción de ejemplo ahorra $200.000 al año. ¿Cuánto ahorra en 3 años?", ["Se multiplica el ahorro anual por los años.", "200.000 por 3 son 600.000."], "$600.000"),
    ],
    mistakes=[("Elegir seguir reparando solo por no pagar la inversión inicial.", "Los costos anuales se acumulan y pueden superar la inversión.", "Compara el costo total en varios años."),
              ("Cerrar la orden con un registro que solo dice «reemplazado».", "No permite revisar el trabajo ni la autorización.", "Anota datos del repuesto, quién autorizó y verificó, y la fecha.")],
    T=[
        ("abc", "En Electricidad: ¿qué es una falla en el contexto del mantenimiento?", "Un evento en que el equipo deja de funcionar como debe", "Una revisión planificada del equipo", "Una orden de trabajo mal escrita", "La falla es el evento de mal funcionamiento; la revisión planificada es preventiva."),
        ("abc", "En Electricidad: ¿qué es un indicador de mantenimiento?", "Un dato que se mide y se registra para evaluar el desempeño, como las fallas al año", "Una luz del tablero que se enciende al fallar", "Un permiso de trabajo firmado", "El indicador es un dato de gestión; no es una luz ni un permiso."),
        ("=", "Una falla de ejemplo cuesta $50.000 y ocurre 4 veces al año. ¿Cuánto cuestan las fallas al año?", "50000*4", "Se multiplica el costo de una falla por las fallas del año.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta una falla, sumando piezas y horas de personal?", "40000+4*6000", "Se suman las piezas y las horas de personal por su valor.", " pesos"),
        ("=", "{F} ¿Cuántas horas queda detenida la bomba al año con la opción 1?", "5*8", "Se multiplican las fallas por las horas detenidas de cada una.", " horas"),
        ("=", "{F} ¿Cuánto cuestan las fallas anuales de la opción 1?", "5*(40000+4*6000)", "Se multiplica el costo de una falla por las 5 fallas del año.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el mantenimiento preventivo anual de la opción 2?", "6*6000", "Se multiplican las horas por el valor de la hora.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta al año la opción 2, sumando su falla y su mantenimiento preventivo?", "(40000+4*6000)+6*6000", "Se suman el costo de la falla y el del mantenimiento preventivo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos al año ahorra la opción 2 respecto de la opción 1?", "5*(40000+4*6000)-((40000+4*6000)+6*6000)", "Se resta el costo anual de la opción 2 al de la opción 1.", " pesos"),
        ("abc", "{F} Después de 3 años, ¿el ahorro acumulado supera el costo de la compra de la bomba nueva?", "Sí: 3 años ahorran 660.000 pesos, más que 600.000", "No: 3 años ahorran 330.000 pesos", "No: el ahorro es solo el costo de las piezas", "El ahorro anual es de 220.000 pesos y en 3 años suma 660.000."),
        ("ab", "{F} El jefe elige la opción 1 porque «no hay que gastar los $600.000 ahora». ¿Qué respuesta es correcta?", "Ahorrar hoy no evita los costos anuales: la opción 1 cuesta 220.000 pesos más cada año y deja más horas detenida", "Tiene razón: no gastar siempre es mejor", "La comparación debe incluir los costos de todos los años, no solo la compra de hoy."),
        ("=", "{F} En 3 años, ¿cuántos pesos menos cuesta la opción 2, contando la compra de la bomba nueva?", "3*5*(40000+4*6000)-(600000+3*((40000+4*6000)+6*6000))", "Se resta el costo total de la opción 2, con la compra, al de la opción 1.", " pesos"),
        ("abc", "{F} Tras reemplazar la bomba, ¿qué debe quedar en el registro de cierre?", "Qué se reemplazó, los datos del repuesto, quién autorizó y verificó, la fecha y las observaciones", "Solo la palabra «listo»", "Solo el precio pagado", "El cierre debe permitir revisar el trabajo y la autorización."),
    ],
    ctx=("abc", "{F} El taller de ejemplo decide reemplazar la bomba y un estudiante en práctica pide «ayudar a retirar la antigua para aprender». ¿Qué corresponde?", "Agradecer, pero explicar que lo hace personal autorizado con permiso y norma vigente; él puede aprender revisando el registro en papel", "Aceptar, porque aprender haciendo es mejor", "Aceptar si usa guantes y casco", "Aprender en papel es el límite de este cuaderno; el trabajo con equipos lo hace personal autorizado."),
    sc=[
        ("En Electricidad: ¿qué se compara para decidir entre reparar y reemplazar?", "El costo anual de cada opción y la inversión de la compra", "Así se ve en cuántos años se recupera la inversión."),
        ("¿Qué es un indicador de mantenimiento?", "Un dato que se mide y se registra para evaluar el desempeño", "Por ejemplo, las fallas al año."),
        ("¿Quién realiza el reemplazo de un componente de un equipo eléctrico?", "Personal autorizado, con permiso de trabajo y norma vigente", "Este cuaderno no habilita para trabajar."),
    ],
    op=("Datos de ejemplo: la bomba B2 del taller «Fragua Oeste» tiene dos opciones. Opción 1: mantener, con 4 fallas al año; cada falla cuesta $30.000 en piezas y 3 horas a $5.000 la hora. Opción 2: reemplazar por una nueva de $400.000 con 1 falla al año (mismo costo por falla) y 4 horas de mantenimiento preventivo al año a $5.000 la hora. Escribe (a) el costo de una falla, (b) el costo anual de cada opción, (c) el ahorro anual de la opción 2, (d) si en 3 años el ahorro supera la compra, (e) qué debe contener el registro de cierre.",
        "(a) 30.000+3 por 5.000 son 45.000 pesos. (b) Opción 1: 4 por 45.000 son 180.000. Opción 2: 45.000 más 4 por 5.000, es decir 20.000: 65.000. (c) 180.000 menos 65.000: 115.000 al año. (d) 3 por 115.000 son 345.000, menos que 400.000: aún no supera la compra. (e) Qué se reemplazó, datos del repuesto, quién autorizó y verificó, fecha y observaciones.",
        ["calcula el costo de una falla", "calcula el costo anual de cada opción", "calcula el ahorro", "compara el ahorro con la inversión", "propone un registro completo"],
        ["hoja con la tabla de cálculos y la conclusión"],
        ["olvidar el mantenimiento preventivo", "creer que 3 años recuperan la compra", "dejar un registro incompleto"],
        "Pregunta: «¿en cuántos años recuperarías la compra?». Si no responde, pídele que relea cómo se compara el ahorro acumulado."),
    reinforce="Inventa dos opciones para un equipo (seguir reparando o reemplazar) y calcula el costo anual de cada una.",
    extend="Explica con un ejemplo por qué un indicador como las horas detenidas ayuda a decidir un reemplazo.",
)

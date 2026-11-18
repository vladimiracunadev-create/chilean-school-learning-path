"""Mecánica Industrial, mención Máquinas-Herramientas, 4.º medio: OAM-04 (CNC y CAM: conceptos, coordenadas, tiempos y verificación, sin programas ejecutables) y OAM-05 (centros de mecanizado: conceptos, hoja de setup y cálculo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_memh_common import AVISO, EMER, build

O4 = "TP-MEMH-4-OAM-04"
O5 = "TP-MEMH-4-OAM-05"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo CNC» tiene un torno y una fresadora de control numérico computarizado (CNC): máquinas que ejecutan movimientos programados, de forma automática y a gran velocidad. "
     "Peligros anotados: movimientos automáticos y rápidos que pueden empezar sin aviso, colisión de la herramienta con la pieza o con la máquina, proyección de virutas y refrigerante, puertas abiertas durante el movimiento, un error en el programa y ruido. "
     "Elementos de seguridad: puertas con enclavamiento (que impiden que la máquina se mueva con la puerta abierta), botón de parada de emergencia y pantalla de simulación. Personas del turno: 6.")
build(
    O4, 1, F,
    use="Aprenderé qué es una máquina CNC, qué riesgos propios tiene frente a una máquina convencional y qué roles intervienen, sin escribir ni ejecutar programas.",
    prior=["Sé qué es una máquina-herramienta convencional.", "Sé qué es un resguardo y una parada de emergencia.", "Sé qué es un peligro y un riesgo."],
    explain=[
        "El control numérico computarizado (CNC) es un sistema que mueve la herramienta y la pieza según un programa, que es una lista de instrucciones codificadas. A diferencia de una máquina convencional, donde una persona gira volantes, la máquina CNC se mueve sola y puede hacerlo rápido y sin aviso. Eso cambia los riesgos: una colisión, que es un choque de la herramienta con la pieza o la máquina, puede ocurrir por un error en el programa y no por un gesto de la persona.",
        "Las puertas con enclavamiento impiden el movimiento con la puerta abierta, y la parada de emergencia detiene la máquina; ambos son controles de ingeniería. La simulación en pantalla permite revisar el programa antes de usarlo. Los roles son el programador, que prepara el programa, el operador autorizado, que supervisa la máquina, y el supervisor, que aprueba. Un programa nuevo no se ejecuta sin que alguien con autorización lo haya verificado.",
        f"Este cuaderno no enseña a programar ni a operar una máquina CNC. {EMER} {AVISO}",
    ],
    vocab=[("CNC", "control numérico computarizado, sistema que mueve la máquina según un programa"), ("programa de partes", "lista de instrucciones codificadas que ejecuta una máquina CNC"), ("colisión", "choque de la herramienta con la pieza o con la máquina"), ("enclavamiento", "dispositivo que impide el movimiento con la puerta abierta"), ("simulación", "revisión del programa en pantalla antes de usarlo"), ("programador", "persona que prepara el programa de una pieza")],
    worked=[
        ("Convencional o CNC", "En una máquina de ejemplo, la persona gira volantes para mover la herramienta. ¿Es convencional o CNC?", ["El movimiento depende de la persona y no de un programa.", "Es una máquina convencional."], "Convencional"),
        ("Clasificar un control", "Una puerta de ejemplo no permite que la máquina se mueva si está abierta. ¿Qué tipo de control es?", ["Es un dispositivo físico que actúa sin depender de la conducta.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que una máquina CNC es más segura porque «trabaja sola».", "Puede moverse rápido y sin aviso, y un error de programa puede provocar una colisión.", "Respeta las puertas, el enclavamiento y las verificaciones previas."),
              ("Pensar que leer sobre CNC habilita para programar u operar.", "Programar y operar exigen instructor autorizado y norma vigente.", "Aprende el concepto y deja la tarea a quien está autorizado.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es el CNC?", "Un sistema que mueve la herramienta y la pieza según un programa", "Un instrumento que mide piezas con precisión", "Un tipo de herramienta de corte", "El CNC controla los movimientos con un programa."),
        ("abc", "En Máquinas-Herramientas: ¿qué es una colisión en una máquina CNC?", "Un choque de la herramienta con la pieza o con la máquina", "Un corte de energía", "Un cambio de turno", "La colisión es un choque inesperado."),
        ("abc", "En Máquinas-Herramientas: ¿qué hace un enclavamiento en la puerta de una máquina CNC?", "Impide que la máquina se mueva con la puerta abierta", "Cuenta las piezas fabricadas", "Enfría la herramienta", "El enclavamiento protege a quien está cerca."),
        ("abc", "{F} ¿Qué diferencia principal en el riesgo hay entre una máquina CNC y una convencional?", "La CNC puede moverse rápido y sin aviso por un programa", "La CNC no tiene partes móviles", "La convencional se mueve sola", "El movimiento programado puede iniciar sin gesto de la persona."),
        ("abc", "{F} ¿Cuál de los peligros de la lista se relaciona con un error en el programa?", "La colisión de la herramienta", "El ruido", "El refrigerante frío", "Un programa mal preparado puede hacer chocar la herramienta."),
        ("abc", "{F} Las puertas con enclavamiento son un control:", "De ingeniería", "Administrativo", "De EPP", "Son un dispositivo físico que actúa por sí mismo."),
        ("=", "{F} El taller tiene 2 máquinas y cada una requiere 1 operador y 1 persona de apoyo. ¿Cuántas personas se necesitan?", "2*(1+1)", "Se suman operador y apoyo y se multiplican por las máquinas.", " personas"),
        ("=", "{F} Cada persona del turno recibe 2 pares de gafas al año. ¿Cuántos pares se necesitan?", "6*2", "Se multiplican las personas por los pares de cada una.", " pares"),
        ("abc", "{F} Un programa nuevo se quiere ejecutar de inmediato «para ahorrar tiempo». ¿Qué respuesta es correcta?", "No corresponde: se simula y lo verifica personal autorizado antes de ejecutarlo", "Corresponde, porque el programador sabe lo que hace", "Corresponde, si la puerta está cerrada", "Un error no detectado puede causar una colisión."),
        ("abc", "{F} Un aprendiz dice: «anulo el enclavamiento de la puerta para ver mejor el corte». ¿Qué respuesta es correcta?", "Es falso: anular una protección expone a proyecciones y movimientos; nunca se anula", "Es cierto, si lo hace por poco tiempo", "Es cierto, si usa gafas", "El enclavamiento es un control de ingeniería que no se anula."),
        ("abc", "En una visita a un taller de ejemplo, una máquina CNC arranca sola y una persona queda atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar tirar de la persona", "Meter la mano para detener la herramienta", "Intervenir sin formación puede causar otro accidente."),
        ("=", "{F} Cada máquina retira 10 kg de virutas por día. ¿Cuántos kg retiran las 2 máquinas en 5 días?", "2*10*5", "Se multiplican las máquinas, los kg por día y los días.", " kg"),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con el refrigerante usado de una máquina CNC?", "Se almacena y gestiona como residuo según la norma vigente", "Se vierte al desagüe", "Se mezcla con aceite nuevo", "El refrigerante usado es un residuo que requiere gestión."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «el colegio tiene un torno CNC, probemos un programa que vi en internet». ¿Qué respondes?", "Que usar una máquina CNC exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, si el programa parece simple", "Que sí, si cerramos la puerta", "Un programa de internet puede causar una colisión y este cuaderno no habilita para operar."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué es un programa de partes?", "Una lista de instrucciones codificadas que ejecuta la máquina CNC", "El programa dirige los movimientos de la máquina."),
        ("En Máquinas-Herramientas: ¿qué permite la simulación?", "Revisar el programa en pantalla antes de usarlo", "La simulación ayuda a detectar errores antes de que causen una colisión."),
        ("En Máquinas-Herramientas: ¿quién prepara el programa de una pieza?", "El programador", "Cada rol tiene una función distinta y definida."),
    ],
    op=("Ficha de ejemplo: un taller tiene un torno CNC con puerta con enclavamiento, parada de emergencia y pantalla de simulación. Peligros: movimientos rápidos sin aviso, colisión por error de programa y proyección de virutas. Escribe (a) qué control evita el movimiento con la puerta abierta, (b) qué herramienta permite revisar el programa antes de usarlo, (c) un control administrativo, (d) quién ejecuta la máquina. No escribas ningún programa.",
        "(a) El enclavamiento de la puerta. (b) La simulación en pantalla. (c) La regla de que ningún programa nuevo se ejecuta sin que personal autorizado lo haya verificado. (d) Un operador autorizado, con instructor y norma vigente.",
        ["nombra el enclavamiento", "nombra la simulación", "propone un control administrativo", "indica quién opera"],
        ["hoja con las cuatro respuestas"],
        ["decir que la máquina es segura porque trabaja sola", "proponer anular el enclavamiento", "escribir un programa"],
        "Pregunta: «¿qué puede pasar si hay un error en el programa?». Si duda, pídele que relea la definición de colisión."),
    reinforce="Escribe tres diferencias entre una máquina convencional y una máquina CNC desde el punto de vista del riesgo.",
    extend="Explica con un ejemplo por qué un enclavamiento no debe anularse aunque estorbe.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (flujo y hoja de setup de ejemplo, inventados). Flujo de trabajo: CAD (el dibujo de la pieza en computador) → CAM (software que genera las trayectorias de la herramienta a partir del dibujo) → programa de partes → post-procesador (adapta el programa a la máquina concreta) → simulación → máquina. "
     "Hoja de setup (preparación) de la pieza «Soporte-01»: material, acero de ejemplo; cero pieza (el punto de origen desde el cual se miden las coordenadas) en la esquina superior izquierda; herramientas: T1 fresa de 16 mm, T2 broca de 8 mm, T3 fresa de 6 mm; sujeción con mordazas; área de trabajo de la máquina: X de 0 a 300 mm, Y de 0 a 200 mm, Z de 0 a 150 mm. "
     "Coordenadas absolutas: se miden siempre desde el cero pieza. Coordenadas incrementales: se miden desde el punto anterior.")
build(
    O4, 2, F,
    use="Aprenderé la diferencia entre CAD y CAM, el flujo hasta la máquina, los documentos de preparación y las coordenadas absolutas e incrementales, sin escribir programas.",
    prior=["Sé qué es un programa de partes.", "Sé leer una tabla.", "Sé restar y sumar enteros."],
    explain=[
        "El CAD es el dibujo de la pieza hecho en el computador. El CAM es el software que, a partir de ese dibujo, genera las trayectorias de la herramienta y un programa de partes. Como cada máquina entiende su propia versión del lenguaje, el post-procesador adapta el programa a la máquina concreta. Antes de usarlo se simula en pantalla para detectar choques y errores. La hoja de setup, o de preparación, anota el material, el cero pieza, las herramientas y la sujeción.",
        "El cero pieza es el punto de origen desde el cual se miden las coordenadas de la pieza. En coordenadas absolutas cada punto se mide siempre desde el cero pieza; en coordenadas incrementales, desde el punto anterior. Las coordenadas no se pueden salir del área de trabajo de la máquina. El programador, el operador y el supervisor verifican cada documento.",
        f"Aquí solo se leen documentos y se calculan coordenadas. {EMER} {AVISO}",
    ],
    vocab=[("CAD", "dibujo de la pieza hecho en computador"), ("CAM", "software que genera las trayectorias de la herramienta a partir del dibujo"), ("post-procesador", "programa que adapta el código a una máquina concreta"), ("hoja de setup", "documento con material, cero pieza, herramientas y sujeción"), ("cero pieza", "punto de origen desde el cual se miden las coordenadas"), ("coordenada absoluta", "medida desde el cero pieza"), ("coordenada incremental", "medida desde el punto anterior")],
    worked=[
        ("CAD o CAM", "Un software de ejemplo toma el dibujo de una pieza y calcula por dónde debe pasar la herramienta. ¿Es CAD o CAM?", ["Genera trayectorias a partir del dibujo.", "Eso es el CAM."], "CAM"),
        ("Pasar a incremental", "Dos puntos de ejemplo tienen coordenada absoluta X de 20 mm y de 55 mm. ¿Cuál es la coordenada incremental del segundo respecto del primero?", ["Se resta el primer valor al segundo.", "55 menos 20 son 35."], "35 mm"),
    ],
    mistakes=[("Confundir CAD con CAM.", "El CAD dibuja; el CAM genera las trayectorias.", "Pregunta si el software dibuja o calcula trayectorias."),
              ("Medir una coordenada absoluta desde el punto anterior.", "Las absolutas se miden desde el cero pieza.", "Identifica siempre el cero pieza antes de leer.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es el CAD?", "El dibujo de la pieza hecho en computador", "El software que genera las trayectorias", "El adaptador del programa a la máquina", "En este caso, El CAD es el dibujo."),
        ("abc", "En Máquinas-Herramientas: ¿qué hace el post-procesador?", "Adapta el programa a la máquina concreta", "Dibuja la pieza", "Mide la pieza terminada", "Cada máquina entiende su versión del lenguaje."),
        ("abc", "En Máquinas-Herramientas: ¿qué es el cero pieza?", "El punto de origen desde el cual se miden las coordenadas", "La pieza que se descarta", "La máquina en reposo", "El cero pieza es el origen del sistema de coordenadas."),
        ("abc", "{F} ¿Qué paso del flujo sigue después del CAM?", "El programa de partes", "El dibujo CAD", "La pieza terminada", "El CAM genera trayectorias y de ellas sale el programa."),
        ("abc", "{F} ¿Qué paso del flujo sirve para detectar choques antes de usar el programa?", "La simulación", "El post-procesador", "El dibujo CAD", "La simulación revisa el programa en pantalla."),
        ("abc", "{F} ¿Qué herramienta de la hoja de setup es la broca?", "T2", "T1", "T3", "T2 es la broca de 8 mm."),
        ("=", "{F} ¿Cuántas herramientas lista la hoja de setup?", "3", "T1, T2 y T3 son las herramientas listadas.", " herramientas"),
        ("=", "{F} Un punto está en X = 120 mm y otro en X = 200 mm (absolutas). ¿Cuánto es la coordenada incremental en X del segundo respecto del primero?", "200-120", "Se resta el primer valor al segundo.", " mm"),
        ("=", "{F} Un punto está en Y = 90 mm (absoluta) y el siguiente se mueve +40 mm en incremental. ¿Cuál es su coordenada absoluta en Y?", "90+40", "Se suma el incremento a la absoluta anterior.", " mm"),
        ("abc", "{F} Un punto programado tiene X = 320 mm. ¿Es posible en esta máquina?", "No, porque el área de trabajo en X llega hasta 300 mm", "Sí, porque 320 es un número normal", "Sí, si se baja la velocidad", "El punto queda fuera del área de trabajo."),
        ("abc", "{F} Un programador dice: «el cero pieza puede cambiar de esquina en cualquier momento sin avisar». ¿Qué respuesta es correcta?", "Es falso: el cero pieza lo define la hoja de setup, y cambiarlo cambia todas las coordenadas", "Es cierto, porque las coordenadas se ajustan solas", "Es cierto, si es más cómodo", "Si cambia el origen, el programa se desplaza y puede chocar."),
        ("=", "{F} El área de trabajo en X mide 300 mm. Una pieza de 180 mm ocupa parte. ¿Cuántos mm de recorrido libre sobran en X?", "300-180", "Se resta el largo de la pieza al recorrido de la máquina.", " mm"),
        ("En una hoja de ejemplo, el cero pieza no está definido. ¿Qué conviene hacer antes de usar el programa?", "Informarlo y pedir que se complete la hoja", "Sin cero pieza las coordenadas no tienen origen y el programa no se puede usar."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «el programa que me pasaron ya está listo, no necesita simulación». ¿Qué propones?", "Simularlo y que lo verifique personal autorizado antes de ejecutarlo", "Ejecutarlo directamente", "Cambiar el cero pieza al azar", "La simulación evita colisiones por errores no detectados."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué genera el CAM?", "Las trayectorias de la herramienta y el programa", "Se calcula a partir del dibujo CAD."),
        ("En Máquinas-Herramientas: ¿desde dónde se miden las coordenadas absolutas?", "Desde el cero pieza", "El cero pieza es el origen común."),
        ("En Máquinas-Herramientas: ¿qué anota la hoja de setup?", "Material, cero pieza, herramientas y sujeción", "Son los datos para preparar la máquina."),
    ],
    op=("Ficha de ejemplo: una máquina con área de trabajo X de 0 a 250 mm y Y de 0 a 150 mm. Puntos absolutos de una pieza: P1 (X 30, Y 20); P2 (X 90, Y 20); P3 (X 90, Y 80); P4 (X 270, Y 80). Escribe (a) el incremento de P1 a P2 en X, (b) el incremento de P2 a P3 en Y, (c) qué punto está fuera del área de trabajo, (d) por qué se simula antes de ejecutar.",
        "(a) 90 − 30 = 60 mm. (b) 80 − 20 = 60 mm. (c) P4, porque X = 270 supera los 250 mm. (d) Para detectar errores y choques en pantalla antes de mover la máquina.",
        ["calcula el incremento en X", "calcula el incremento en Y", "detecta el punto fuera", "explica la simulación"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "no comparar con el área de trabajo", "omitir la simulación"],
        "Pregunta: «¿cuál es el límite de X?». Si duda, pídele que relea el área de trabajo."),
    reinforce="Escribe el flujo desde el dibujo hasta la máquina en cinco pasos con una frase de cada uno.",
    extend="Explica con un ejemplo por qué un punto fuera del área de trabajo hace inválido un programa.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (tabla de puntos de ejemplo, inventada, solo para practicar coordenadas). Área de trabajo de la máquina: X de 0 a 300 mm; Y de 0 a 200 mm. Cero pieza en la esquina inferior izquierda de la pieza, que mide 120 mm en X y 80 mm en Y. "
     "Puntos absolutos (X, Y en mm): A (10, 10); B (110, 10); C (110, 70); D (10, 70); E (60, 40); F (130, 40). Regla de ejemplo del plano: el centro de la herramienta debe quedar a 10 mm o más de cada borde de la pieza. "
     "Recorrido: A → B → C → D → A. Avance de ejemplo: 80 mm por minuto.")
build(
    O4, 3, F,
    use="Aprenderé a analizar en papel una tabla de puntos: convertir absolutas a incrementales, detectar puntos fuera de la pieza o del área, y calcular la longitud y el tiempo de un recorrido.",
    prior=["Sé qué son coordenadas absolutas e incrementales.", "Sé restar y sumar enteros.", "Sé calcular un tiempo de recorrido."],
    explain=[
        "Una tabla de puntos lista las posiciones por donde pasa la herramienta. Se pueden convertir de absolutas a incrementales restando cada punto al anterior, y de incrementales a absolutas sumando. Se comprueba que cada punto esté dentro del área de trabajo de la máquina y dentro de la pieza. La longitud de un recorrido recto horizontal o vertical es la diferencia de coordenadas entre sus extremos.",
        "El tiempo de recorrido es la longitud total dividida por el avance en mm por minuto. Un punto fuera de la pieza o del área es una incoherencia que se registra e informa al programador, y el programa no se ejecuta hasta que se corrija. Todo el análisis es documental.",
        f"No se escribe ni se ejecuta ningún programa. {EMER} {AVISO}",
    ],
    vocab=[("tabla de puntos", "lista de posiciones por donde pasa la herramienta"), ("recorrido", "secuencia de puntos que sigue la herramienta"), ("longitud de un tramo", "distancia entre dos puntos consecutivos en línea recta"), ("punto fuera", "punto que sale de la pieza o del área de trabajo"), ("incoherencia", "dato que contradice a otro o al plano")],
    worked=[
        ("Incremental", "Dos puntos de ejemplo son (20, 30) y (50, 30). ¿Cuánto es el incremento en X y en Y?", ["En X: 50 menos 20 son 30.", "En Y: 30 menos 30 son 0."], "30 mm en X y 0 mm en Y"),
        ("Longitud de un tramo", "Un tramo recto de ejemplo va de X = 10 a X = 85 con Y constante. ¿Cuánto mide?", ["Se resta el inicio al final.", "85 menos 10 son 75."], "75 mm"),
    ],
    mistakes=[("Calcular la longitud de un tramo sumando las coordenadas.", "La longitud es la diferencia entre los extremos.", "Resta la coordenada menor a la mayor."),
              ("Ejecutar un programa con un punto fuera del área.", "Puede provocar una colisión o un error.", "Informa al programador y espera la corrección.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una tabla de puntos?", "Una lista de posiciones por donde pasa la herramienta", "Una lista de herramientas disponibles", "Un plano con tolerancias", "La tabla de puntos lista las posiciones."),
        ("abc", "En Máquinas-Herramientas: ¿cómo se pasa de coordenadas absolutas a incrementales?", "Restando a cada punto el anterior", "Sumando todos los puntos", "Multiplicando por el avance", "El incremento es la diferencia con el punto anterior."),
        ("abc", "En Máquinas-Herramientas: ¿qué es un punto fuera?", "Uno que sale de la pieza o del área de trabajo", "Uno que está en el centro de la pieza", "Uno que se repite", "Un punto fuera es una incoherencia."),
        ("=", "{F} ¿Cuántos mm mide el tramo A → B?", "110-10", "Se resta la coordenada X de A a la de B.", " mm"),
        ("=", "{F} ¿Cuántos mm mide el tramo B → C?", "70-10", "Se resta la coordenada Y de B a la de C.", " mm"),
        ("=", "{F} ¿Cuántos mm mide el recorrido cerrado A → B → C → D → A?", "100+60+100+60", "Se suman los cuatro tramos del rectángulo.", " mm"),
        ("=", "{F} ¿Cuántos minutos tarda ese recorrido a 80 mm por minuto, sumando los 320 mm?", "320//80", "Se divide la longitud entre el avance por minuto.", " minutos"),
        ("abc", "{F} ¿Qué punto de la tabla está fuera de la pieza?", "F (130, 40), porque X supera los 120 mm de la pieza", "E (60, 40), porque está en el centro", "A (10, 10), porque está en la esquina", "La pieza llega hasta X = 120 mm."),
        ("abc", "{F} ¿Todos los puntos están dentro del área de trabajo de la máquina?", "Sí, todos tienen X menor que 300 e Y menor que 200", "No, F supera el área", "No, A está fuera", "Incluso F está dentro del área, aunque fuera de la pieza."),
        ("abc", "{F} Un programador dice: «F está dentro del área de la máquina, así que no hay problema con la pieza». ¿Qué respuesta es correcta?", "Es falso: F está fuera de la pieza, y la herramienta cortaría aire o chocaría con la sujeción", "Es cierto, porque el área es lo único que importa", "Es cierto, si la herramienta es pequeña", "Un punto fuera de la pieza es una incoherencia aunque esté en el área."),
        ("abc", "{F} Un operario sugiere corregir el punto F de memoria y ejecutar. ¿Qué respuesta es correcta?", "No corresponde: lo corrige el programador, se simula y lo verifica personal autorizado", "Corresponde, si lo recuerda bien", "Corresponde, si es el último punto", "Un cambio sin verificación puede causar una colisión."),
        ("=", "{F} Con el borde de la pieza en X = 120 y la regla de 10 mm de distancia mínima al borde para el centro de la herramienta, ¿cuál es el X máximo permitido para ese centro?", "120-10", "Se resta la distancia mínima al borde, según la regla de ejemplo.", " mm"),
        ("Los puntos (0, 0), (50, 0) y (50, 30) forman un recorrido. ¿Cuántos mm suman sus dos tramos?", "80 mm", "El primer tramo mide 50 y el segundo mide 30."),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «ese punto está algo fuera, pero la máquina lo aguanta». ¿Qué propones?", "Registrar la incoherencia y que el programador la corrija antes de ejecutar", "Ejecutar el programa igual", "Mover la pieza a ojo", "Un punto fuera es una incoherencia que no se ejecuta."),
    sc=[
        ("En Máquinas-Herramientas: ¿cómo se obtiene la longitud de un tramo recto horizontal?", "Restando la X inicial a la X final", "La longitud es la diferencia de coordenadas."),
        ("En Máquinas-Herramientas: ¿qué se hace con un punto fuera de la pieza?", "Se informa al programador para que lo corrija", "No se ejecuta un programa con incoherencias."),
        ("En Máquinas-Herramientas: ¿cómo se calcula el tiempo de un recorrido?", "Dividiendo la longitud entre el avance por minuto", "Distancia dividida por velocidad da tiempo."),
    ],
    op=("Ficha de ejemplo: área de trabajo X de 0 a 200 mm, Y de 0 a 150 mm; pieza de 100 mm por 60 mm con cero en la esquina inferior izquierda. Puntos absolutos: P1 (10, 10); P2 (90, 10); P3 (90, 50); P4 (110, 50). Avance de ejemplo 60 mm por minuto. Escribe (a) la longitud del tramo P1 → P2, (b) la longitud de P2 → P3, (c) qué punto está fuera de la pieza, (d) el tiempo de P1 → P2 → P3 en minutos enteros.",
        "(a) 90 − 10 = 80 mm. (b) 50 − 10 = 40 mm. (c) P4, porque X = 110 supera los 100 mm de la pieza. (d) 120 mm ÷ 60 mm por minuto son 2 minutos.",
        ["calcula tramos", "detecta el punto fuera", "calcula el tiempo"],
        ["hoja con las cuatro respuestas"],
        ["sumar coordenadas en vez de restar", "no detectar el punto fuera", "ejecutar con incoherencias"],
        "Pregunta: «¿hasta dónde llega la pieza en X?». Si duda, pídele que relea el enunciado."),
    reinforce="Inventa cuatro puntos absolutos y convierte los tramos a incrementos.",
    extend="Explica con un ejemplo por qué un punto fuera de la pieza es un error aunque esté dentro del área de la máquina.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (tiempo de ciclo CNC de ejemplo, inventado). Pieza «Placa-02» en una fresadora CNC. Recorridos de corte: 1.500 mm en total a 300 mm por minuto. Recorridos rápidos (sin cortar): 9.000 mm a 3.000 mm por minuto. Cambios de herramienta: 3, de 20 segundos cada uno. "
     "Colocar y retirar la pieza: 60 segundos. Lote de 120 piezas. Costo de ejemplo de la máquina: $18.000 la hora. Preparación del lote (setup): 45 minutos. Turno de 480 minutos. Una herramienta de corte alcanza para 400 piezas y cuesta $20.000.")
build(
    O4, 4, F,
    use="Aprenderé a calcular el tiempo de ciclo de una máquina CNC con cortes, rápidos y cambios de herramienta, y el costo y las piezas por turno de un lote, con datos de ejemplo.",
    prior=["Sé calcular un tiempo de recorrido.", "Sé pasar segundos a minutos.", "Sé calcular un costo por minuto."],
    explain=[
        "En una máquina CNC el tiempo de ciclo de una pieza suma varios tiempos: el de corte, que se calcula dividiendo la longitud de corte entre el avance de corte; el de los recorridos rápidos, que se calcula dividiendo su longitud entre la velocidad rápida; el de los cambios de herramienta, y el de colocar y retirar la pieza. Los segundos se pasan a minutos dividiendo por 60.",
        "El tiempo del lote suma el ciclo por las piezas y la preparación. El costo del lote es los minutos totales por el costo por minuto. Las piezas por turno se calculan dividiendo los minutos disponibles, sin la preparación, entre el ciclo. Una herramienta con vida limitada también se cuenta. Los valores son de ejemplo.",
        f"Es un cálculo de papel; no se programa ni se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("tiempo de corte", "longitud de corte dividida por el avance de corte"), ("recorrido rápido", "movimiento de la herramienta sin cortar, a mayor velocidad"), ("tiempo de ciclo", "suma de todos los tiempos para hacer una pieza"), ("setup", "preparación del lote que se hace una vez"), ("vida de la herramienta", "cantidad de piezas que alcanza una herramienta")],
    worked=[
        ("Tiempo de corte", "Un corte de ejemplo de 600 mm a 200 mm por minuto. ¿Cuántos minutos toma?", ["Se divide la longitud entre el avance.", "600 dividido en 200 son 3."], "3 minutos"),
        ("Pasar segundos", "Un cambio de ejemplo toma 90 segundos. ¿Cuántos minutos son?", ["Se divide por 60.", "90 dividido en 60 son 1 minuto y medio."], "1,5 minutos"),
    ],
    mistakes=[("Olvidar los recorridos rápidos al calcular el ciclo.", "También ocupan tiempo de máquina.", "Súmalos al tiempo de corte."),
              ("Mezclar segundos con minutos sin convertir.", "El resultado queda mal.", "Pasa todo a la misma unidad antes de sumar.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es un recorrido rápido?", "Un movimiento de la herramienta sin cortar, a mayor velocidad", "El corte más veloz", "El cambio de herramienta", "En este caso, Se mueve sin retirar material."),
        ("abc", "En Máquinas-Herramientas: ¿qué es el setup?", "La preparación del lote que se hace una vez", "El control final de cada pieza", "La limpieza de la máquina", "El setup se hace antes de producir un lote."),
        ("abc", "En Máquinas-Herramientas: ¿cómo se calcula el tiempo de corte?", "Dividiendo la longitud de corte entre el avance de corte", "Multiplicando la longitud por el avance", "Sumando el avance y la longitud", "Tiempo es distancia dividida por velocidad."),
        ("=", "{F} ¿Cuántos minutos toma el corte, con 1.500 mm a 300 mm por minuto?", "1500//300", "Se divide la longitud entre el avance de corte.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suman los recorridos rápidos, con 9.000 mm a 3.000 mm por minuto?", "9000//3000", "Se divide la longitud entre la velocidad de los recorridos rápidos.", " minutos"),
        ("=", "{F} ¿Cuántos segundos suman los 3 cambios de herramienta?", "3*20", "Se multiplican los cambios por los segundos de cada uno.", " segundos"),
        ("=", "{F} ¿Cuántos segundos suman el corte, los rápidos, los cambios y el colocar y retirar, tomando el corte de 300 s, los rápidos de 180 s, los cambios de 60 s y colocar y retirar de 60 s?", "300+180+60+60", "Se suman los cuatro tiempos en segundos.", " segundos"),
        ("=", "{F} ¿Cuántos minutos es un ciclo de 600 segundos?", "600//60", "Se divide por 60 para pasar de segundos a minutos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos de ciclo hay en 120 piezas de 10 minutos cada una?", "120*10", "Se multiplican las piezas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita el lote con la preparación de 45 minutos, con 1.200 minutos de ciclo?", "1200+45", "Se suman los minutos del ciclo y de la preparación.", " minutos"),
        ("abc", "{F} Un jefe dice: «alcanza con un turno de 480 minutos para el lote de 1.245 minutos». ¿Qué respuesta es correcta?", "Es falso: el lote requiere 1.245 minutos y el turno tiene 480", "Es cierto, porque son pocas piezas", "Es cierto, si se acelera la máquina", "1.245 supera los 480 minutos del turno."),
        ("=", "{F} ¿Cuántas herramientas de corte se usan en el lote de 120 piezas, si cada una alcanza para 400?", "(120+399)//400", "Se divide entre la vida de la herramienta, redondeando hacia arriba.", " herramienta"),
        ("Si el lote de 1.245 minutos cuesta $18.000 por hora, ¿cuánto cuesta el lote?", "$373.500", "1.245 por 18.000 dividido en 60 son 373.500."),
    ],
    ctx=("abc", "El cliente de ejemplo quiere el lote en un turno y el cálculo da 1.245 minutos. ¿Qué propones?", "Informar que se necesitan 2 turnos o más máquinas, con el cálculo a la vista", "Prometer un turno", "Saltarse el control de calidad", "El plazo se basa en el tiempo real calculado."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuánto tarda un corte de 900 mm a 300 mm por minuto?", "3 minutos", "Se divide la longitud entre el avance."),
        ("En Máquinas-Herramientas: ¿cómo se pasan los segundos a minutos?", "Dividiendo por 60", "En este caso, Un minuto tiene 60 segundos."),
        ("En Máquinas-Herramientas: ¿qué se suma al ciclo del lote además del tiempo por pieza?", "La preparación del lote", "El setup se hace una vez por lote."),
    ],
    op=("Ficha de ejemplo: una pieza en una fresadora CNC tiene 1.200 mm de corte a 200 mm por minuto, 600 segundos de rápidos y cambios que suman 60 segundos y 60 segundos de colocar y retirar. Lote de 50 piezas, preparación de 30 minutos y turno de 480 minutos. Escribe (a) los minutos de corte, (b) los minutos de ciclo por pieza, (c) los minutos del lote con la preparación, (d) si cabe en un turno.",
        "(a) 1.200 ÷ 200 = 6 minutos. (b) 6 + 10 (600 s) + 1 (60 s) + 1 (60 s) = 18 minutos. (c) 50 × 18 + 30 = 930 minutos. (d) No, 930 supera 480 y se necesitan 2 turnos.",
        ["calcula el corte", "calcula el ciclo", "calcula el lote", "compara con el turno"],
        ["hoja con las cuatro respuestas"],
        ["no pasar segundos a minutos", "olvidar la preparación", "no comparar con el turno"],
        "Pregunta: «¿todo está en la misma unidad?». Si duda, pídele que pase los segundos a minutos."),
    reinforce="Inventa un corte, unos rápidos y unos cambios y calcula el ciclo en minutos.",
    extend="Explica con un ejemplo por qué los recorridos rápidos no se pueden olvidar en el ciclo.",
)

# ============================================================ OAM-04, clase 5
F = ("Ficha 5 (comparación de dos estrategias de programa, de ejemplo). Misma pieza, dos estrategias. Estrategia E1: 5 herramientas distintas, 5 cambios de herramienta, ciclo de 12 minutos por pieza, calidad de superficie suficiente, simulación hecha. "
     "Estrategia E2: 3 herramientas distintas, 2 cambios de herramienta, ciclo de 15 minutos por pieza, calidad de superficie suficiente, simulación hecha. Condición obligatoria: simulación hecha y calidad de superficie suficiente. Lote de 80 piezas. Costo de la máquina: $18.000 la hora. "
     "Costo de ejemplo de cada herramienta distinta: $9.000 por lote. Lista de verificación: simulación sin errores; cero pieza verificado; primera pieza inspeccionada; instrumento con certificado vigente; registro firmado; residuos gestionados.")
build(
    O4, 5, F,
    use="Aprenderé a comparar dos estrategias de programa con una condición obligatoria, tiempos y costos de ejemplo, y a verificar la calidad con una lista, sin escribir programas.",
    prior=["Sé calcular el tiempo de un lote.", "Sé qué es una condición obligatoria.", "Sé qué es una lista de verificación."],
    explain=[
        "Dos estrategias pueden fabricar la misma pieza con distintas herramientas, cambios y tiempos. Se descartan primero las que no cumplen la condición obligatoria, como tener la simulación hecha y la calidad de superficie suficiente. Entre las que cumplen se compara el costo del lote, que suma el costo de máquina por los minutos totales y el costo de las herramientas distintas usadas.",
        "Después de producir, se verifica la calidad con una lista: simulación sin errores, cero pieza verificado, primera pieza inspeccionada, instrumento calibrado, registro firmado y residuos gestionados. La primera pieza inspeccionada permite detectar problemas antes de seguir con el lote. La lista incompleta no se firma, y las decisiones las toma la jefatura por escrito.",
        f"El análisis es de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("estrategia de programa", "forma de organizar herramientas y trayectorias para fabricar una pieza"), ("condición obligatoria", "requisito que se debe cumplir para considerar la estrategia"), ("primera pieza", "pieza inicial que se inspecciona antes de seguir con el lote"), ("costo del lote", "costo de máquina más costo de herramientas"), ("lista de verificación", "lista de puntos que se comprueban uno a uno")],
    worked=[
        ("Costo de máquina", "Un lote de ejemplo toma 300 minutos en una máquina de $12.000 la hora. ¿Cuánto cuesta la máquina?", ["300 minutos son 5 horas.", "5 por 12.000 son 60.000."], "$60.000"),
        ("Descartar", "Una condición exige simulación hecha y una estrategia de ejemplo no la tiene. ¿Se considera?", ["No cumple la condición obligatoria.", "Se descarta."], "No, se descarta"),
    ],
    mistakes=[("Elegir la estrategia más rápida sin revisar la condición obligatoria.", "Una estrategia sin simulación puede causar una colisión.", "Descarta primero las que no cumplen."),
              ("Saltarse la inspección de la primera pieza.", "Un error se repetiría en todo el lote.", "Inspecciona la primera pieza antes de seguir.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una estrategia de programa?", "Una forma de organizar herramientas y trayectorias para fabricar una pieza", "Una máquina distinta para cada pieza", "Un tipo de plano", "Cada estrategia define herramientas, cambios y trayectorias."),
        ("abc", "En Máquinas-Herramientas: ¿para qué se inspecciona la primera pieza?", "Para detectar un problema antes de seguir con el lote", "Para ahorrar tiempo de control", "Para reemplazar el plano", "Un error se detecta antes de repetirlo muchas veces."),
        ("abc", "En Máquinas-Herramientas: ¿qué ocurre con una estrategia que no cumple la condición obligatoria?", "Se descarta, sin importar su costo", "Se elige si es la más barata", "Se usa solo con supervisión", "La condición obligatoria se aplica antes de comparar costos."),
        ("=", "{F} ¿Cuántos minutos toma el lote de 80 piezas con E1?", "80*12", "Se multiplican las piezas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos toma el lote de 80 piezas con E2?", "80*15", "Se multiplican las piezas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuánto cuesta la máquina para el lote con E1, a $18.000 la hora?", "960*18000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta la máquina para el lote con E2, a $18.000 la hora?", "1200*18000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuestan las herramientas distintas de E1, a $9.000 cada una?", "5*9000", "Se multiplican las herramientas por su costo por lote.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuestan las herramientas distintas de E2, a $9.000 cada una?", "3*9000", "Se multiplican las herramientas por su costo por lote.", " pesos de ejemplo"),
        ("abc", "{F} Con máquina y herramientas, ¿qué estrategia resulta más barata para el lote?", "E1, con $333.000 frente a $387.000 de E2", "E2, porque usa menos herramientas", "Cuestan lo mismo", "E1 ahorra tiempo de máquina y eso compensa sus herramientas."),
        ("abc", "{F} Un jefe dice: «ejecutemos E1 sin inspeccionar la primera pieza para ahorrar». ¿Qué respuesta es correcta?", "No corresponde: la primera pieza se inspecciona para evitar repetir un error en todo el lote", "Corresponde, porque E1 es la más rápida", "Corresponde, si la máquina es nueva", "Un error detectado a tiempo ahorra más que lo que cuesta la inspección."),
        ("abc", "{F} El instrumento de control tiene el certificado vencido. ¿Qué corresponde con la lista de verificación?", "No firmarla hasta que se mida con un instrumento calibrado", "Firmarla porque el resto cumple", "Borrar el punto del instrumento", "Un instrumento vencido deja las mediciones en duda."),
        ("abc", "En Máquinas-Herramientas: ¿qué puede ocurrir si una estrategia más rápida se ejecuta sin simulación?", "Puede producir una colisión que dañe la herramienta, la pieza o la máquina", "Nada, porque el CAM siempre genera programas correctos", "Solo se pierde un poco de tiempo", "Un error no detectado en pantalla se descubre en la máquina, con riesgo de daño y de accidente."),
    ],
    ctx=("abc", "Un programador de ejemplo propone una estrategia más rápida sin simulación porque «la máquina la acepta». ¿Qué propones?", "No usarla hasta que se simule y lo verifique personal autorizado", "Ejecutarla de inmediato", "Quitar la condición de simulación", "La simulación es una condición obligatoria."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué se hace primero al comparar estrategias?", "Descartar las que no cumplen la condición obligatoria", "En este caso, después se comparan los costos."),
        ("En Máquinas-Herramientas: ¿cuánto cuesta una hora de máquina a $18.000 si dura 5 horas?", "$90.000", "Se multiplica el costo por hora por las horas."),
        ("En Máquinas-Herramientas: ¿qué se inspecciona antes de seguir con el lote?", "La primera pieza", "Así se detectan errores a tiempo."),
    ],
    op=("Ficha de ejemplo: dos estrategias para una pieza, ambas con simulación hecha. S1: ciclo de 10 minutos, 4 herramientas a $8.000 cada una por lote. S2: ciclo de 12 minutos, 2 herramientas a $8.000 cada una por lote. Lote de 60 piezas, máquina a $12.000 la hora. Escribe (a) los minutos del lote con cada una, (b) el costo de máquina de cada una, (c) el costo total de cada una, (d) qué compruebas con la lista de verificación al terminar.",
        "(a) S1: 600; S2: 720 minutos. (b) S1: 600 × 12.000 ÷ 60 = 120.000; S2: 720 × 200 = 144.000. (c) S1: 120.000 + 32.000 = 152.000; S2: 144.000 + 16.000 = 160.000 pesos de ejemplo. (d) Simulación sin errores, cero pieza, primera pieza inspeccionada, instrumento calibrado, registro firmado y residuos gestionados.",
        ["calcula los minutos", "calcula el costo de máquina", "calcula el costo total", "nombra la verificación"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las herramientas", "dividir mal por 60", "firmar sin verificar"],
        "Pregunta: «¿cuántos minutos toma el lote con cada estrategia?». Si duda, pídele que multiplique el ciclo por las piezas."),
    reinforce="Inventa dos estrategias con ciclo y herramientas y calcula cuál cuesta menos para un lote.",
    extend="Explica con un ejemplo por qué inspeccionar la primera pieza ahorra costos.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Un centro de mecanizado ficticio es una máquina CNC con un cambiador automático de herramientas: un almacén (magazine) de 20 posiciones donde la máquina toma y cambia herramientas sola. Tiene 3 ejes (X, Y, Z) y un cuarto eje giratorio. "
     "Peligros anotados: cambio automático de herramientas con movimientos de brazos, movimientos simultáneos de varios ejes, refrigerante a presión, piezas pesadas, virutas, colisión, puertas abiertas y ruido. Elementos de seguridad: puertas con enclavamiento, parada de emergencia, protección contra choques y simulación.")
build(
    O5, 1, F,
    use="Aprenderé qué es un centro de mecanizado, en qué se diferencia de otras máquinas CNC, qué peligros tiene y qué roles intervienen, sin programarlo ni operarlo.",
    prior=["Sé qué es una máquina CNC.", "Sé qué es un programa y una simulación.", "Sé qué es un enclavamiento."],
    explain=[
        "Un centro de mecanizado es una máquina CNC que cambia herramientas por sí sola. Tiene un magazine, un almacén con varias posiciones donde se guardan las herramientas, y un cambiador automático que las toma y las coloca en el husillo. Además de los tres ejes lineales X, Y y Z, puede tener ejes giratorios que inclinan o giran la pieza, con lo que trabaja varias caras sin volver a sujetarla.",
        "Esa automatización agrega peligros: el cambiador y los brazos se mueven solos, varios ejes se mueven a la vez y el refrigerante sale a presión. Se controlan con puertas con enclavamiento, parada de emergencia, protección contra choques y simulación del programa. Los roles son el programador, el operador autorizado, el supervisor y el control de calidad. Ningún programa nuevo se ejecuta sin verificación.",
        f"Este cuaderno no enseña a programar ni a operar un centro de mecanizado. {EMER} {AVISO}",
    ],
    vocab=[("centro de mecanizado", "máquina CNC que cambia herramientas por sí sola"), ("magazine", "almacén de herramientas con varias posiciones"), ("cambiador automático", "mecanismo que toma y coloca herramientas en el husillo"), ("eje giratorio", "eje que gira o inclina la pieza"), ("husillo", "eje que hace girar la herramienta"), ("refrigerante a presión", "líquido de enfriamiento que sale con fuerza")],
    worked=[
        ("Función del magazine", "Un almacén de ejemplo guarda 24 herramientas distintas. ¿Cómo se llama y qué función cumple?", ["Se llama magazine.", "Permite que la máquina cambie herramientas sola."], "Magazine; permite cambiar herramientas automáticamente"),
        ("Clasificar un control", "Una puerta de ejemplo no permite el movimiento con la puerta abierta. ¿Qué tipo de control es?", ["Es un dispositivo físico.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Acercar la mano al cambiador automático porque «está parado un momento».", "Puede moverse sin aviso porque es automático.", "No se interviene en una máquina con cambiador; solo personal autorizado."),
              ("Creer que leer sobre el centro de mecanizado habilita para operarlo.", "Su uso exige instructor y norma vigente.", "Aprende el concepto y deja el uso a quien está autorizado.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es un centro de mecanizado?", "Una máquina CNC que cambia herramientas por sí sola", "Una máquina convencional con muchas herramientas", "Una zona de bodega de herramientas", "El cambio automático lo distingue de otras máquinas."),
        ("abc", "En Máquinas-Herramientas: ¿qué es el magazine?", "Un almacén de herramientas con varias posiciones", "Un tipo de plano", "La puerta de la máquina", "El magazine guarda las herramientas listas."),
        ("abc", "En Máquinas-Herramientas: ¿qué permite un eje giratorio?", "Girar o inclinar la pieza para trabajar varias caras", "Cambiar de herramienta", "Medir la pieza", "El eje giratorio amplía las caras que se pueden trabajar."),
        ("abc", "{F} ¿Cuántas herramientas puede guardar el magazine de la ficha?", "20", "3", "4", "En este caso, El magazine tiene 20 posiciones."),
        ("abc", "{F} ¿Qué peligro de la lista se debe al cambio automático de herramientas?", "Los movimientos de brazos del cambiador", "El ruido de la oficina", "El color del refrigerante", "En este caso, El cambiador se mueve solo."),
        ("abc", "{F} La protección contra choques de la máquina es un control:", "De ingeniería", "Administrativo", "De EPP", "En este caso, Es un dispositivo físico."),
        ("=", "{F} La máquina tiene 3 ejes lineales y un eje giratorio. ¿Cuántos ejes tiene en total?", "3+1", "Se suman los ejes lineales y el giratorio.", " ejes"),
        ("=", "{F} El taller tiene 4 centros como el de la ficha y 2 personas por centro en el turno. ¿Cuántas personas se necesitan?", "4*2", "Se multiplican los centros por las personas de cada uno.", " personas"),
        ("abc", "{F} Un operario dice: «meto la mano al magazine mientras está parado; no se mueve». ¿Qué respuesta es correcta?", "Es falso: el cambiador puede moverse sin aviso y solo personal autorizado interviene", "Es cierto, porque está parado", "Es cierto, si lleva guantes", "Una máquina automática puede reiniciar un movimiento."),
        ("abc", "{F} Un estudiante dice: «sé cómo funciona el centro de mecanizado, puedo ponerlo en marcha». ¿Qué respuesta es correcta?", "Es falso: ponerlo en marcha exige instructor autorizado y norma vigente", "Es cierto, si entiende el manual", "Es cierto, si lo hace con un compañero", "Entender el concepto no autoriza a operar."),
        ("abc", "En una visita a un taller de ejemplo, el brazo del cambiador automático golpea a una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Detener el brazo con tus manos", "Mover a la persona rápidamente", "Intervenir sin formación puede causar otro accidente."),
        ("=", "{F} Si cada centro genera 12 kg de virutas por día, ¿cuántos kg generan los 4 centros en 5 días?", "4*12*5", "Se multiplican centros, kg por día y días.", " kg"),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con el refrigerante usado de un centro de mecanizado?", "Se almacena y gestiona como residuo según la norma vigente", "Se vierte al desagüe", "Se rellena con agua y se reutiliza siempre", "Es un residuo que requiere gestión."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «hay un centro de mecanizado en el liceo, intentemos encenderlo cuando no haya nadie». ¿Qué respondes?", "Que no, porque usarlo exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, si solo lo encendemos", "Que sí, con gafas puestas", "Este cuaderno no habilita para operar máquinas."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué hace el cambiador automático?", "Toma y coloca herramientas en el husillo", "Cambia herramientas sin intervención de la persona."),
        ("En Máquinas-Herramientas: ¿qué es un eje giratorio?", "Un eje que gira o inclina la pieza", "Amplía las caras que se pueden trabajar."),
        ("En Máquinas-Herramientas: ¿quién puede operar un centro de mecanizado?", "Personal autorizado con instructor y norma vigente", "En este caso, El uso exige autorización."),
    ],
    op=("Ficha de ejemplo: un centro de mecanizado ficticio con magazine de 16 posiciones, 3 ejes lineales y 1 giratorio, puertas con enclavamiento y parada de emergencia. Peligros: cambiador automático, varios ejes a la vez y refrigerante a presión. Escribe (a) qué es el magazine, (b) cuántos ejes tiene, (c) un control de ingeniería, (d) quién lo opera. No describas cómo se opera.",
        "(a) Un almacén de herramientas con varias posiciones. (b) 3 + 1 = 4 ejes. (c) Las puertas con enclavamiento. (d) Personal autorizado con instructor y norma vigente.",
        ["define el magazine", "cuenta los ejes", "propone un control de ingeniería", "indica quién opera"],
        ["hoja con las cuatro respuestas"],
        ["confundir el magazine con la puerta", "contar mal los ejes", "describir cómo se opera"],
        "Pregunta: «¿cuántos ejes lineales y cuántos giratorios hay?». Si duda, pídele que relea el enunciado."),
    reinforce="Escribe tres diferencias entre un centro de mecanizado y una fresadora convencional.",
    extend="Explica con un ejemplo por qué una máquina automática puede reiniciar un movimiento sin aviso.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (lista de herramientas y correctores de ejemplo, inventada). Centro de mecanizado con magazine de 20 posiciones. Lista de la pieza «Carcasa-03»: T1 fresa de 20 mm, largo 100 mm; T2 fresa de 10 mm, largo 90 mm; T3 broca de 6 mm, largo 80 mm; T4 broca de 12 mm, largo 85 mm; T5 macho de roscar M8 (herramienta que hace rosca), largo 75 mm. "
     "Corrector de herramienta: valor que informa a la máquina el largo real de cada herramienta, medido fuera de la máquina. Recorrido máximo de Z: 150 mm. Cero pieza en la cara superior de la pieza, de 60 mm de espesor. Pieza sujeta en una morsa (dispositivo de sujeción).")
build(
    O5, 2, F,
    use="Aprenderé a leer una lista de herramientas, a entender qué es un corrector y qué restricciones físicas tiene el magazine, sin programar ni preparar la máquina.",
    prior=["Sé qué es el magazine.", "Sé qué es el cero pieza.", "Sé restar y comparar números."],
    explain=[
        "La lista de herramientas de una pieza anota el número de cada herramienta, su tipo, su diámetro y su largo. El número, como T1, T2 o T3, identifica la posición de la herramienta en el magazine. El corrector es un valor que informa a la máquina el largo real de cada herramienta, medido fuera de la máquina por personal autorizado; si el corrector no corresponde, la herramienta puede chocar o cortar mal.",
        "El magazine tiene un número de posiciones, y la lista no puede tener más herramientas que ellas. Las herramientas deben caber en el recorrido de la máquina: el largo de la herramienta más la profundidad de trabajo debe ser compatible con el recorrido en Z y con la altura de la pieza y de la sujeción. La sujeción es el dispositivo que mantiene firme la pieza.",
        f"Aquí solo se leen documentos y se hacen comprobaciones de papel. {EMER} {AVISO}",
    ],
    vocab=[("número de herramienta (T)", "identificador de la posición de una herramienta en el magazine"), ("corrector de herramienta", "valor que informa a la máquina el largo real de una herramienta"), ("macho de roscar", "herramienta que hace una rosca en un agujero"), ("sujeción", "dispositivo que mantiene firme la pieza"), ("recorrido en Z", "distancia máxima que puede subir y bajar el eje vertical")],
    worked=[
        ("Contar herramientas", "Una lista de ejemplo tiene herramientas T1 a T7. ¿Cuántas herramientas hay?", ["Se cuentan de la 1 a la 7.", "Son 7 herramientas."], "7 herramientas"),
        ("Capacidad del magazine", "Un magazine de ejemplo tiene 12 posiciones y una lista pide 14 herramientas. ¿Cabe?", ["14 es mayor que 12.", "No caben todas."], "No cabe"),
    ],
    mistakes=[("Usar un corrector de memoria.", "Un corrector equivocado puede hacer chocar la herramienta.", "El corrector lo mide y registra personal autorizado."),
              ("Olvidar la sujeción al revisar si la herramienta cabe.", "La sujeción también ocupa espacio y puede chocar.", "Considera pieza y sujeción al revisar el recorrido.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es un corrector de herramienta?", "Un valor que informa a la máquina el largo real de la herramienta", "Un instrumento que corrige errores de dibujo", "Un tipo de broca", "El corrector permite que la máquina conozca el largo."),
        ("abc", "En Máquinas-Herramientas: ¿qué identifica el número T1 o T2?", "La posición de la herramienta en el magazine", "El precio de la herramienta", "El diámetro de la herramienta", "En este caso, El número ubica la herramienta."),
        ("abc", "En Máquinas-Herramientas: ¿qué es un macho de roscar?", "Una herramienta que hace una rosca en un agujero", "Una herramienta que pule una superficie", "Un instrumento de medición", "El macho de roscar hace roscas."),
        ("=", "{F} ¿Cuántas herramientas lista la pieza?", "5", "T1, T2, T3, T4 y T5 son las cinco herramientas de la lista.", " herramientas"),
        ("=", "{F} ¿Cuántas posiciones libres quedan en el magazine después de cargar las herramientas de la lista?", "20-5", "Se resta el número de herramientas a las posiciones del magazine.", " posiciones"),
        ("abc", "{F} ¿Qué herramienta de la lista es la más larga?", "T1, de 100 mm", "T3, de 80 mm", "T5, de 75 mm", "T1 mide 100 mm, el mayor largo de la lista."),
        ("=", "{F} ¿Cuántos mm más larga es la herramienta T1 que la T5?", "100-75", "Se resta el largo de T5 al de T1.", " mm"),
        ("=", "{F} Si la herramienta más larga baja hasta el fondo del trabajo, ¿cuántos mm sobran en Z, restando su largo al recorrido máximo?", "150-100", "Se resta el largo al recorrido máximo.", " mm"),
        ("abc", "{F} ¿Qué corrector de la lista corresponde a la broca de 6 mm?", "El de T3, de largo 80 mm", "El de T1, de largo 100 mm", "El de T5, de largo 75 mm", "T3 es la broca de 6 mm."),
        ("abc", "{F} Un programador dice: «el corrector de T3 lo escribo de memoria, es 82 mm». ¿Qué respuesta es correcta?", "No corresponde: el corrector se mide fuera de la máquina por personal autorizado, y la lista dice 80 mm", "Corresponde, si recuerda el valor", "Corresponde, si la diferencia es pequeña", "Un corrector erróneo puede causar una colisión."),
        ("abc", "{F} Se agregan a la lista 18 herramientas más. ¿Qué observación es correcta?", "No caben: el magazine tiene 20 posiciones y ya hay 5 usadas", "Caben todas porque el magazine es grande", "Caben si se retira la puerta", "5 más 18 son 23 y el magazine tiene 20 posiciones."),
        ("=", "{F} Para fabricar 15 carcasas, ¿cuántas veces se usa la broca T3 si hace 4 agujeros por carcasa?", "15*4", "Se multiplican las carcasas por los agujeros de cada una.", " agujeros"),
        ("Una herramienta de ejemplo de 120 mm de largo debe trabajar en una máquina cuyo recorrido en Z es de 100 mm. ¿Es posible?", "No", "El largo de la herramienta supera el recorrido disponible en Z."),
    ],
    ctx=("abc", "El operador de ejemplo dice: «no medí el largo de T4, pero seguro es el de la lista». ¿Qué propones?", "Que el largo se mida y registre como corrector antes de usar la herramienta", "Aceptar el valor de la lista sin medir", "Ejecutar el programa para comprobar", "Un corrector equivocado puede causar una colisión."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué indica T3?", "La posición o número de la herramienta", "Es un identificador en el magazine."),
        ("En Máquinas-Herramientas: ¿cuántas herramientas caben en un magazine de 20 posiciones?", "Hasta 20", "El número de posiciones es el límite."),
        ("En Máquinas-Herramientas: ¿quién mide los correctores?", "Personal autorizado", "En este caso, exige instrumentos y formación."),
    ],
    op=("Ficha de ejemplo: magazine de 12 posiciones. Lista de una pieza: T1 fresa de 16 mm, largo 95 mm; T2 broca de 8 mm, largo 80 mm; T3 macho de roscar M6, largo 70 mm. Recorrido máximo de Z: 120 mm. Escribe (a) cuántas herramientas lista la pieza, (b) cuántas posiciones libres quedan, (c) cuántos mm sobran en Z con la herramienta más larga, (d) quién mide los correctores.",
        "(a) 3. (b) 12 − 3 = 9 posiciones. (c) 120 − 95 = 25 mm. (d) Personal autorizado, fuera de la máquina.",
        ["cuenta las herramientas", "calcula las posiciones libres", "calcula el margen en Z", "indica quién mide"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "ignorar el recorrido", "decir que el corrector se anota de memoria"],
        "Pregunta: «¿cuántas herramientas hay y cuántas posiciones?». Si duda, pídele que relea el enunciado."),
    reinforce="Inventa una lista de cuatro herramientas con su largo y calcula los mm que sobran en un recorrido dado.",
    extend="Explica con un ejemplo por qué el corrector no se anota de memoria.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (hoja de setup de ejemplo con errores, inventada). Centro de mecanizado con magazine de 8 posiciones y recorrido en Z de 150 mm. Pieza «Bloque-04». Lista de herramientas: T1 a T9 (nueve herramientas) con largos entre 70 y 160 mm; la T7 mide 160 mm. "
     "Cero pieza anotado: «a definir». Sujeción: morsa con la pieza de 50 mm de altura sobre la mesa; la altura de la morsa es 40 mm. Tiempo de ciclo anotado: 15 minutos, suma de operaciones: 4, 5, 3 y 6 minutos. Simulación: «pendiente». Revisión de la hoja: A; del plano: B.")
build(
    O5, 3, F,
    use="Aprenderé a revisar en papel una hoja de setup, detectando faltantes, incoherencias de capacidad, sumas erróneas y revisiones distintas, y a informar sin corregir por cuenta propia.",
    prior=["Sé leer una hoja de setup.", "Sé qué es el magazine y el corrector.", "Sé sumar tiempos."],
    explain=[
        "Al revisar una hoja de setup se comprueba que cada dato exista y sea coherente: que haya un cero pieza definido, que el número de herramientas no supere las posiciones del magazine, que cada herramienta quepa en el recorrido en Z junto con la pieza y la sujeción, que la suma de tiempos sea correcta, que la simulación esté hecha y que la revisión de la hoja sea la del plano.",
        "Una hoja con puntos pendientes o con incoherencias no se usa. Quien la revisa registra cada hallazgo con el dato y el motivo, y lo informa a quien emitió la hoja. No se corrige por cuenta propia ni se ejecuta un programa con una simulación pendiente. La revisión es solo documental.",
        f"No se prepara ni se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("hallazgo", "dato incoherente o faltante detectado en la revisión"), ("pendiente", "punto de la hoja que aún no se ha completado"), ("capacidad del magazine", "número de herramientas que puede guardar"), ("altura útil de Z", "recorrido en Z menos la altura de pieza y sujeción"), ("revisión de la hoja", "versión del documento que debe coincidir con la del plano")],
    worked=[
        ("Capacidad", "Una hoja de ejemplo lista 10 herramientas y el magazine tiene 8 posiciones. ¿Qué incoherencia hay?", ["Hay más herramientas que posiciones.", "No caben todas."], "Sobran 2 herramientas"),
        ("Altura útil", "Un recorrido de Z de ejemplo es de 200 mm y la pieza con la sujeción miden 120 mm de altura. ¿Cuánto queda?", ["Se resta la altura al recorrido.", "200 menos 120 son 80."], "80 mm"),
    ],
    mistakes=[("Usar una hoja con la simulación pendiente porque «el programa es simple».", "Un error no detectado puede causar una colisión.", "Espera la simulación y la verificación."),
              ("Completar el cero pieza por cuenta propia.", "Lo define quien emitió la hoja con el plano.", "Registra el pendiente e infórmalo.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es un pendiente en una hoja de setup?", "Un punto de la hoja que aún no se completó", "Una herramienta ya usada", "Un tiempo muy largo", "Un pendiente impide usar la hoja."),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con una hoja de setup con hallazgos?", "Se registran e informan a quien la emitió", "Se corrigen con lápiz y se usa", "Se archivan sin informar", "Quien emitió la hoja la corrige."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la altura útil de Z?", "El recorrido en Z menos la altura de la pieza y la sujeción", "La altura de la máquina", "La altura de la herramienta más larga", "Es el espacio que queda para la herramienta."),
        ("=", "{F} ¿Cuántas herramientas sobran respecto de las posiciones del magazine?", "9-8", "Se resta la capacidad del magazine a la cantidad de herramientas.", " herramienta"),
        ("abc", "{F} ¿Qué incoherencia hay en el cero pieza?", "Está anotado como «a definir»", "Está en la cara superior", "Está en el centro", "Un cero pieza sin definir impide usar la hoja."),
        ("abc", "{F} ¿Qué estado tiene la simulación de la hoja?", "Pendiente", "Hecha", "Sin errores", "La ficha anota la simulación como pendiente."),
        ("=", "{F} ¿Cuántos minutos suman realmente las cuatro operaciones?", "4+5+3+6", "Se suman los tiempos de las cuatro operaciones.", " minutos"),
        ("abc", "{F} ¿Es correcto el ciclo de 15 minutos anotado en la hoja?", "No, porque las operaciones suman 18", "Sí, porque 15 es la suma", "Sí, porque incluye un descanso", "4 más 5 más 3 más 6 son 18."),
        ("=", "{F} ¿Cuánto mide la altura de la pieza más la de la morsa, en mm?", "50+40", "Se suman la altura de la pieza y la de la morsa.", " mm"),
        ("=", "{F} ¿Cuánto queda de altura útil en Z, restando al recorrido la pieza y la morsa?", "150-90", "Se resta la altura total al recorrido en Z.", " mm"),
        ("abc", "{F} ¿Cabe la herramienta T7 de 160 mm en el recorrido de Z de 150 mm?", "No, porque 160 supera el recorrido de 150", "Sí, porque 160 es un largo normal", "Sí, si se baja la mesa", "En este caso, El largo supera el recorrido."),
        ("abc", "{F} Un operario dice: «usemos la hoja revisión A, aunque el plano sea B; son casi iguales». ¿Qué respuesta es correcta?", "No corresponde: se pide la hoja en revisión B antes de trabajar", "Corresponde, porque son casi iguales", "Corresponde, si lo anota", "Una revisión distinta puede tener datos desactualizados."),
        ("En una hoja de ejemplo, el magazine tiene 10 posiciones y la lista pide 10 herramientas. ¿Qué observación corresponde?", "Caben justo, sin posiciones libres de repuesto", "Con 10 posiciones y 10 herramientas no queda ninguna libre."),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «la simulación aún no se hizo, pero ejecutemos el programa y vemos». ¿Qué propones?", "Esperar la simulación y la verificación antes de ejecutar", "Ejecutarlo para comprobar", "Anotar que la simulación se hizo", "Ejecutar sin simulación puede causar una colisión."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué no puede superar la cantidad de herramientas de una lista?", "Las posiciones del magazine", "En este caso, cada herramienta ocupa una posición."),
        ("En Máquinas-Herramientas: ¿quién corrige una hoja de setup con errores?", "Quien la emitió", "Los cambios se hacen en una nueva revisión."),
        ("En Máquinas-Herramientas: ¿qué debe estar hecho antes de ejecutar un programa?", "La simulación y su verificación", "En este caso, así se evitan colisiones."),
    ],
    op=("Ficha de ejemplo: hoja de setup para un centro con magazine de 6 posiciones y recorrido en Z de 120 mm. Lista de herramientas: 7. Pieza y morsa suman 70 mm de altura. La herramienta más larga mide 55 mm. Cero pieza definido. Simulación: pendiente. Operaciones de 3, 5 y 4 minutos; total anotado: 10 minutos. Escribe (a) cuántas herramientas sobran, (b) la suma real de las operaciones, (c) la altura útil en Z y si cabe la herramienta, (d) qué haces con la simulación pendiente.",
        "(a) 7 − 6 = 1 herramienta. (b) 3 + 5 + 4 = 12 minutos. (c) 120 − 70 = 50 mm; la herramienta de 55 mm no cabe. (d) No se ejecuta el programa: se espera la simulación y la verificación, y se informa a quien emitió la hoja.",
        ["calcula las herramientas que sobran", "suma las operaciones", "calcula la altura útil", "decide sobre la simulación"],
        ["hoja con las cuatro respuestas"],
        ["no contar las herramientas", "olvidar la sujeción", "ejecutar sin simulación"],
        "Pregunta: «¿cuántas posiciones hay y cuántas herramientas se piden?». Si duda, pídele que compare ambos números."),
    reinforce="Escribe cuatro puntos que revisarías en una hoja de setup antes de aceptarla.",
    extend="Explica con un ejemplo por qué la sujeción debe considerarse al revisar el recorrido en Z.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cálculo de producción en un centro de mecanizado, de ejemplo). Pieza «Carcasa-05». Ciclo por pieza: corte, 8 minutos; cambios de herramienta, 4 cambios de 15 segundos; colocar y retirar, 2 minutos; control, 1 minuto. "
     "Lote de 200 piezas. Preparación (setup) del lote: 90 minutos. Costo de ejemplo del centro: $24.000 la hora. Un turno tiene 480 minutos y se trabajan 2 turnos al día. Salen defectuosas 8 piezas. Precio de venta de ejemplo: $9.000 por pieza buena. Las herramientas del lote cuestan $60.000 en total.")
build(
    O5, 4, F,
    use="Aprenderé a calcular el ciclo de un centro de mecanizado, el tiempo y el costo de un lote, los días de producción y el margen, con datos de ejemplo.",
    prior=["Sé calcular un tiempo de ciclo.", "Sé pasar segundos a minutos.", "Sé calcular un costo por minuto."],
    explain=[
        "El ciclo por pieza en un centro de mecanizado suma el corte, los cambios de herramienta, el tiempo de colocar y retirar la pieza y el control. Los cambios de herramienta se pasan de segundos a minutos dividiendo por 60. El tiempo del lote suma el ciclo por las piezas y la preparación. El costo del lote suma el costo de máquina, los minutos por el costo por minuto, y las herramientas.",
        "Los días de producción se calculan dividiendo los minutos del lote entre los minutos disponibles por día y se redondean hacia arriba. El margen es lo que se obtiene al vender las piezas buenas menos el costo del lote. Los defectuosos se restan de las piezas del lote. Todos los valores son de ejemplo.",
        f"No se programa ni se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("ciclo por pieza", "suma de los tiempos para hacer una pieza"), ("minutos del lote", "ciclo por piezas más la preparación"), ("costo del lote", "costo de máquina más costo de herramientas"), ("margen", "ventas de las piezas buenas menos el costo del lote"), ("días de producción", "minutos del lote divididos por los minutos disponibles por día")],
    worked=[
        ("Ciclo", "Una pieza de ejemplo toma 5 minutos de corte, 1 de cambios y 2 de colocar y retirar. ¿Cuánto es el ciclo?", ["Se suman los tres tiempos.", "5 más 1 más 2 son 8."], "8 minutos"),
        ("Margen", "Un lote de ejemplo vende 50 piezas buenas a $1.000 y cuesta $30.000. ¿Cuánto es el margen?", ["Las ventas son 50 por 1.000, es decir 50.000.", "50.000 menos 30.000 son 20.000."], "$20.000"),
    ],
    mistakes=[("Olvidar la preparación del lote.", "Se hace una vez por lote y suma tiempo.", "Suma la preparación a los minutos del lote."),
              ("Vender todas las piezas, incluidas las defectuosas.", "Solo las piezas buenas se venden.", "Resta los defectuosos antes de calcular las ventas.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es el margen de un lote?", "Las ventas de las piezas buenas menos el costo del lote", "El costo de las herramientas", "El número de piezas del lote", "En este caso, El margen mide la ganancia."),
        ("abc", "En Máquinas-Herramientas: ¿cómo se pasan los segundos de los cambios de herramienta a minutos?", "Dividiendo por 60", "Multiplicando por 60", "Sumando 60", "En este caso, Un minuto tiene 60 segundos."),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con la preparación del lote?", "Se suma una vez a los minutos del lote", "Se multiplica por las piezas", "Se ignora", "La preparación se hace una vez por lote."),
        ("=", "{F} ¿Cuántos segundos suman los 4 cambios de herramienta?", "4*15", "Se multiplican los cambios por los segundos de cada uno.", " segundos"),
        ("=", "{F} ¿Cuántos minutos son esos segundos?", "60//60", "Se dividen los segundos entre 60 para pasarlos a minutos.", " minuto"),
        ("=", "{F} ¿Cuál es el ciclo por pieza con 8 minutos de corte, 1 de cambios, 2 de colocar y 1 de control?", "8+1+2+1", "Se suman los cuatro tiempos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita el lote de 200 piezas con un ciclo de 12 minutos y la preparación de 90?", "200*12+90", "Se multiplica el ciclo por las piezas y se suma la preparación.", " minutos"),
        ("=", "{F} ¿Cuántos minutos disponibles hay por día con 2 turnos de 480 minutos?", "2*480", "Se multiplican los turnos por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos días se necesitan para 2.490 minutos, con 960 por día? Redondea hacia arriba.", "(2490+959)//960", "Se divide entre los minutos por día redondeando hacia arriba.", " días"),
        ("=", "{F} ¿Cuántas piezas buenas hay en el lote?", "200-8", "Se restan los defectuosos al lote.", " piezas"),
        ("=", "{F} ¿Cuánto cuesta el centro en el lote de 2.490 minutos, a $24.000 la hora?", "2490*24000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe dice: «vendemos las 200 piezas, sin descontar defectuosos». ¿Qué respuesta es correcta?", "Es falso: solo se venden las piezas buenas", "Es cierto, porque se produjeron 200", "Es cierto, si el cliente no revisa", "Las piezas defectuosas no cumplen el plano."),
        ("Si las ventas son $1.728.000 y el costo del lote es $996.000 más $60.000 de herramientas, ¿cuánto es el margen?", "$672.000", "En este caso, 1.728.000 menos 1.056.000 son 672.000."),
    ],
    ctx=("abc", "El cliente de ejemplo pide el lote en un día y el cálculo da 3 días. ¿Qué propones?", "Informar el plazo real y ofrecer alternativas, como más turnos o más máquinas", "Prometer un día", "Omitir el control de calidad", "El plazo se basa en los minutos reales."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuántos segundos son 2 minutos?", "120", "Se multiplican los minutos por 60."),
        ("En Máquinas-Herramientas: ¿cómo se redondean los días de producción?", "Hacia arriba", "En este caso, Un resto exige otro día."),
        ("En Máquinas-Herramientas: ¿qué se resta al lote para obtener las piezas buenas?", "Los defectuosos", "En este caso, los defectuosos no se venden."),
    ],
    op=("Ficha de ejemplo: lote de 100 piezas en un centro: corte, 6 minutos; cambios, 4 cambios de 15 segundos; colocar y retirar, 2 minutos; control, 1 minuto; preparación, 60 minutos; 2 turnos de 480 minutos al día; 4 piezas defectuosas. Escribe (a) el ciclo por pieza, (b) los minutos del lote, (c) los días de producción, (d) cuántas piezas buenas hay.",
        "(a) 6 + 1 (60 s) + 2 + 1 = 10 minutos. (b) 100 × 10 + 60 = 1.060 minutos. (c) 960 minutos por día: 1.060 ÷ 960 da 2 días redondeando hacia arriba. (d) 100 − 4 = 96 piezas buenas.",
        ["calcula el ciclo", "calcula los minutos del lote", "calcula los días", "calcula las piezas buenas"],
        ["hoja con las cuatro respuestas"],
        ["no pasar segundos a minutos", "olvidar la preparación", "redondear hacia abajo"],
        "Pregunta: «¿incluiste la preparación?». Si duda, pídele que relea cómo se calcula el lote."),
    reinforce="Inventa un ciclo de cuatro tiempos y calcula los minutos de un lote de 50 piezas con una preparación de 30 minutos.",
    extend="Explica con un ejemplo por qué el margen debe calcularse solo con piezas buenas.",
)

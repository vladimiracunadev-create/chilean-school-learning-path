"""Electricidad TP 3.º y 4.º medio: OAE-07 (sistemas de control, fuerza y protecciones: lectura y criterio en papel) y OAE-08 (programas y parámetros: gestión del cambio en papel). Solo conceptos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_elec_common import AVISO, EMER, build

O7 = "TP-ELEC-3y4-OAE-07"
O8 = "TP-ELEC-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (máquina de ejemplo, inventada). Cinta transportadora de práctica «CT-1» de un taller ficticio: un motor de 1100 W a 220 V mueve la cinta. El mando tiene un pulsador de marcha, un pulsador de parada y una parada de emergencia; "
     "existe además una protección contra sobrecarga del motor. El mantenimiento de la máquina genera residuos: aceite usado y componentes eléctricos desechados.")
build(
    O7, 1, F,
    use="Aprenderé qué es un sistema de control, qué diferencia hay entre fuerza y mando, qué son las protecciones y cómo se relacionan con el medio ambiente, solo en papel.",
    prior=["Sé que P = V × I.", "Sé qué es una falla y qué es una sobrecarga.", "Sé que las máquinas con energía las interviene personal autorizado."],
    explain=[
        "Un sistema de control es el conjunto de componentes que ordenan cuándo y cómo funciona una máquina. Tiene dos partes. El circuito de fuerza lleva la energía al motor. El circuito de mando lleva las señales que ordenan el funcionamiento: pulsadores, protecciones y bobinas, con poca potencia. Las protecciones son dispositivos que cortan o limitan la energía para cuidar a las personas y al equipo; por ejemplo, la protección contra sobrecarga actúa cuando la corriente supera lo permitido. La parada de emergencia es un pulsador que una persona acciona para detener la máquina rápidamente ante un peligro.",
        "Las protecciones nunca se anulan ni se reemplazan unas por otras, porque cada una cumple una función distinta. Además, la norma vigente exige cuidar el medio ambiente: los residuos de una máquina, como el aceite usado o los componentes desechados, se gestionan por separado y no se botan con la basura común. Los requisitos del proyecto y las especificaciones del fabricante dicen qué se necesita. Ejecutar o intervenir un sistema de control es tarea de personal autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("sistema de control", "conjunto de componentes que ordenan cuándo y cómo funciona una máquina"), ("circuito de fuerza", "el que lleva la energía al motor"), ("circuito de mando", "el que lleva las señales que ordenan el funcionamiento, con poca potencia"), ("protección", "dispositivo que corta o limita la energía para cuidar a las personas y al equipo"), ("parada de emergencia", "pulsador que una persona acciona para detener la máquina rápidamente"), ("residuo", "material desechado que se gestiona según la norma vigente")],
    worked=[
        ("Fuerza o mando", "En una máquina de ejemplo, el cable que lleva energía al motor, ¿es de fuerza o de mando?", ["El que lleva energía al motor es el de fuerza.", "El de mando lleva solo las señales de control."], "Es de fuerza"),
        ("Corriente del motor", "Un motor de ejemplo de 880 W funciona a 220 V. ¿Cuántos amperios usa?", ["La corriente es la potencia dividida por la tensión.", "880 dividido por 220 son 4."], "4 A"),
    ],
    mistakes=[("Anular la parada de emergencia «porque molesta en las pruebas».", "Sin ella no hay forma de detener la máquina ante un peligro.", "Informa al responsable para revisar el diseño; las protecciones no se anulan."),
              ("Botar el aceite usado con la basura común.", "Es un residuo que la norma vigente manda gestionar aparte.", "Registra el residuo y entrégalo a gestión autorizada.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un sistema de control de una máquina?", "El conjunto de componentes que ordenan cuándo y cómo funciona la máquina", "La carcasa metálica que cubre la máquina", "El plano de la fábrica donde está instalada", "El sistema de control ordena el funcionamiento; la carcasa y el plano son otras cosas."),
        ("abc", "En Electricidad: ¿cuál es la diferencia entre circuito de fuerza y circuito de mando?", "El de fuerza lleva la energía al motor; el de mando lleva las señales que ordenan su funcionamiento", "El de fuerza lleva las señales; el de mando lleva la energía al motor", "No hay diferencia: son dos nombres del mismo circuito", "La fuerza mueve la energía grande y el mando lleva señales de control."),
        ("abc", "En Electricidad: ¿para qué sirve una protección contra sobrecarga?", "Para cortar o limitar la energía cuando la corriente supera lo permitido", "Para aumentar la velocidad del motor", "Para registrar las horas de uso de la máquina", "La protección actúa ante exceso de corriente para cuidar el equipo y a las personas."),
        ("abc", "{F} ¿Qué componente del mando permite que una persona detenga la máquina rápidamente ante un peligro?", "La parada de emergencia", "El pulsador de marcha", "La protección contra sobrecarga", "La parada de emergencia la acciona una persona; la protección actúa por sí sola ante un exceso de corriente."),
        ("=", "{F} ¿Cuántos kWh consume el motor de CT-1 si funciona 10 horas?", "1100*10//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuántos amperios usa el motor de CT-1 a 220 V?", "1100//220", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "{F} Un taller de ejemplo tiene 3 máquinas iguales a CT-1 funcionando a la vez. ¿Cuántos amperios suman?", "3*1100//220", "Se multiplica la potencia por 3 y se divide por la tensión.", " A"),
        ("abc", "{F} ¿Qué corresponde con el aceite usado del mantenimiento?", "Gestionarlo como residuo según la norma vigente de control del medio ambiente, no como basura común", "Echarlo por el desagüe del taller", "Guardarlo sin rotular en cualquier rincón", "Un residuo se registra, se rotula y se entrega a gestión autorizada."),
        ("abc", "{F} Un técnico dice que, como hay protección contra sobrecarga, la parada de emergencia sobra. ¿Qué corresponde?", "No: cumplen funciones distintas; la protección actúa ante sobrecarga y la parada la acciona una persona", "Sí: una protección reemplaza a la parada", "Sí, si la máquina es pequeña", "Cada protección cubre una situación distinta y ninguna reemplaza a otra."),
        ("abc", "{F} Un compañero propone anular temporalmente la parada de emergencia «porque molesta en las pruebas». ¿Qué corresponde?", "No: las protecciones no se anulan; si molesta, se informa al responsable para revisar el diseño", "Sí, si la prueba es corta", "Sí, si avisa a todos los presentes", "Una protección anulada deja de proteger justo cuando puede ser necesaria."),
        ("ab", "{F} Un estudiante cree que, por leer esta clase, puede revisar el mando de CT-1. ¿Qué corresponde?", "No: intervenir sistemas de control exige personal autorizado y norma vigente", "Sí: ya conoce los componentes", "Conocer los componentes en papel no habilita para intervenir una máquina."),
        ("=", "{F} Si CT-1 funciona 8 horas al día durante 25 días, ¿cuántos kWh consume en el mes?", "1100*8*25//1000", "Se multiplica la potencia por las horas del mes y se pasa a kWh.", " kWh"),
        ("abc", "Una operaria de ejemplo recibe una descarga al tocar la carcasa de una máquina y queda en contacto con la energía. ¿Qué indican las reglas generales?", "No tocarla, cortar el suministro solo si se está autorizado, avisar a un adulto responsable y a emergencias", "Jalarla de la ropa para separarla de inmediato", "Esperar a ver si se suelta sola antes de avisar", "Tocarla puede transmitir la descarga a quien ayuda; se avisa y se corta el suministro solo si se está autorizado."),
    ],
    ctx=("abc", "{F} Un cliente de ejemplo pide quitar el pulsador de parada de emergencia de CT-1 «porque se activa sin querer». ¿Qué corresponde?", "Explicar que la parada es una protección que no se quita y proponer al proyectista revisar su ubicación", "Quitarlo para que el cliente quede conforme", "Taparlo con cinta para que no se active", "La parada de emergencia no se elimina ni se inutiliza; se estudia otra ubicación con el proyectista."),
    sc=[
        ("En Electricidad: ¿qué lleva el circuito de fuerza?", "La energía que alimenta al motor", "El mando lleva solo señales de control."),
        ("¿Se pueden anular las protecciones para facilitar una prueba?", "No, nunca se anulan", "Sin protecciones desaparece el cuidado de las personas y del equipo."),
        ("¿Cómo se manejan los residuos de una máquina?", "Se gestionan aparte según la norma vigente", "No se botan con la basura común."),
    ],
    op=("Máquina de ejemplo «Prensa P-3» (ficticia): motor de 880 W a 220 V; mando con pulsador de marcha, parada y parada de emergencia; protección contra sobrecarga; el mantenimiento genera aceite usado. Escribe (a) cuántos amperios usa el motor, (b) cuántos kWh consume en 25 horas, (c) qué función tiene la parada de emergencia, (d) qué haces con el aceite usado, (e) quién interviene el mando.",
        "(a) 880 dividido por 220 son 4 A. (b) 880 por 25 son 22.000 Wh, es decir, 22 kWh. (c) Permite que una persona detenga la máquina rápidamente ante un peligro. (d) Lo gestiono como residuo según la norma vigente, no como basura común. (e) Personal autorizado, con norma vigente (SEC).",
        ["calcula la corriente", "calcula la energía", "explica la parada de emergencia", "gestiona el residuo", "nombra quién interviene"],
        ["hoja con las cinco respuestas"],
        ["dividir mal", "decir que la parada se puede quitar", "botar el aceite"],
        "Pregunta: «¿por qué no se quita la parada de emergencia?». Si no responde, pídele que relea qué son las protecciones."),
    reinforce="Escribe tres componentes de un sistema de control y di si pertenecen al circuito de fuerza o al de mando.",
    extend="Explica con un ejemplo por qué las protecciones no se reemplazan unas por otras.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (esquema de mando descrito por escrito, de ejemplo, inventado). Leyenda: M1 = motor de la cinta; S1 = pulsador de marcha (contacto normalmente abierto, NA); S2 = pulsador de parada (contacto normalmente cerrado, NC); "
     "S3 = parada de emergencia (NC); F1 = protección contra sobrecarga (NC mientras no se activa); K1 = contactor, un interruptor que se cierra cuando se energiza su bobina y alimenta a M1. "
     "Regla de mando: la bobina de K1 se energiza solo si se cumple a la vez: (S1 presionado O K1 ya cerrado, que actúa como memoria) Y S2 sin presionar Y S3 sin accionar Y F1 sin activar. M1 funciona mientras K1 está cerrado.")
build(
    O7, 2, F,
    use="Aprenderé a leer la lógica de un esquema de mando descrito por escrito: contactos NA y NC, contactor, memoria y condiciones Y/O.",
    prior=["Sé qué es un circuito de mando.", "Sé qué hace una protección.", "Sé leer una leyenda."],
    explain=[
        "Un contacto normalmente abierto (NA) solo conduce mientras se acciona; un contacto normalmente cerrado (NC) conduce siempre, salvo mientras se acciona. El contactor es un interruptor que se cierra cuando se energiza su bobina y permite que la energía llegue al motor. La memoria es un contacto del propio contactor que mantiene la orden de marcha después de soltar el pulsador. En la lógica, «Y» significa que deben cumplirse todas las condiciones a la vez; «O» significa que basta con una.",
        "Las paradas se hacen con contactos NC: si la vía se corta por una falla, la bobina se desenergiza y la máquina se detiene; es una falla segura. Un arranque inesperado es un peligro: por eso, si la energía vuelve después de una detención, la máquina no debe arrancar sola. Esta clase solo lee la lógica del esquema; no explica cómo se conecta ni se pone en marcha una máquina.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("contacto NA", "contacto normalmente abierto: solo conduce mientras se acciona"), ("contacto NC", "contacto normalmente cerrado: conduce salvo mientras se acciona"), ("contactor", "interruptor que se cierra cuando se energiza su bobina"), ("memoria", "contacto del contactor que mantiene la orden de marcha"), ("falla segura", "falla que deja la máquina detenida y no en marcha")],
    worked=[
        ("Leer un contacto", "Un pulsador de ejemplo es NA y nadie lo presiona. ¿Conduce?", ["Un NA solo conduce mientras se acciona.", "Sin accionar, no conduce."], "No conduce"),
        ("Condición Y", "Una luz de ejemplo se enciende si el interruptor A está cerrado Y el interruptor B está cerrado. A está cerrado y B está abierto. ¿Se enciende?", ["Con «Y» deben cumplirse las dos condiciones.", "B está abierto, así que no se cumple."], "No se enciende"),
    ],
    mistakes=[("Pensar que un pulsador de parada debe ser NA.", "Con NA, una falla en la vía dejaría la máquina sin posibilidad de detenerse.", "Las paradas usan contactos NC."),
              ("Creer que la memoria mantiene la marcha aunque se accione la parada.", "La parada corta la vía de la bobina y se pierde la memoria.", "Lee la regla completa: todas las condiciones Y.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un contacto normalmente abierto (NA)?", "Un contacto que solo conduce mientras se acciona", "Un contacto que conduce siempre, salvo cuando se acciona", "Un contacto que nunca conduce", "El NA está abierto en reposo y conduce solo al accionarse."),
        ("abc", "En Electricidad: ¿qué es un contactor?", "Un interruptor que se cierra por una bobina de mando y permite que la energía llegue al motor", "Un resistor que limita la corriente del motor", "Un instrumento que mide la corriente", "El contactor conmuta la energía del motor según la orden de su bobina."),
        ("abc", "En Electricidad: ¿qué significa que una regla de mando use la condición «Y»?", "Que deben cumplirse todas las condiciones a la vez", "Que basta con cumplir una de ellas", "Que ninguna condición importa", "Con «Y» se exigen todas las condiciones; con «O» basta una."),
        ("abc", "{F} M1 está detenido y K1 abierto. Alguien presiona S1 y no se acciona nada más. ¿Qué ocurre?", "La bobina de K1 se energiza, K1 se cierra y M1 funciona", "Nada, porque falta presionar S2", "M1 queda detenido porque S3 está sin accionar", "Con S1 presionado y S2, S3 y F1 en reposo se cumplen todas las condiciones."),
        ("abc", "{F} M1 funciona con K1 cerrado y alguien presiona S2. ¿Qué ocurre?", "Se corta la vía de la bobina, K1 se abre y M1 se detiene", "M1 sigue funcionando por la memoria", "M1 se detiene solo mientras S2 está presionado y arranca sola al soltarlo", "S2 es NC: al accionarlo deja de conducir y la condición Y falla."),
        ("abc", "{F} M1 funciona y se acciona S3. ¿Qué ocurre?", "M1 se detiene, porque S3 interrumpe la vía de la bobina", "M1 sigue funcionando, porque S3 no afecta a K1", "M1 se detiene solo si además se presiona S2", "S3 es NC y forma parte de la condición Y de la bobina."),
        ("abc", "{F} Con M1 en marcha, F1 se activa por una sobrecarga. ¿Qué ocurre?", "K1 se abre y M1 se detiene", "M1 sigue funcionando hasta que alguien lo detenga", "S1 se presiona solo", "F1 es NC y al activarse corta la vía de la bobina."),
        ("abc", "{F} Con K1 abierto y todo lo demás en reposo, nadie presiona S1. ¿Funciona M1?", "No: falta S1 presionado o la memoria de K1", "Sí: las demás condiciones están cumplidas", "Sí: S2 y S3 mantienen la marcha", "Sin S1 ni memoria no se cumple el «O» de la primera condición."),
        ("abc", "{F} Un compañero dice que S2 debería ser NA «para que presionar active la parada». ¿Qué corresponde?", "Las paradas son NC para que una falla en la vía también detenga la máquina; es una falla segura", "El tipo de contacto no cambia lo que ocurre ante una falla", "Con S2 NA, la máquina se detendría siempre ante una falla", "Con un contacto NC, una vía cortada detiene la máquina; con NA no."),
        ("ab", "{F} Un técnico deja S1 trabado en posición presionada. Se presiona S2 y luego se suelta. ¿Qué ocurre?", "M1 vuelve a arrancar al soltar S2, lo que es un peligro y se informa al responsable", "M1 queda detenido para siempre después de S2", "Con S1 trabado, al soltar S2 se vuelve a cumplir la condición y la máquina arranca sola."),
        ("abc", "{F} F1 se activa y luego se desactiva sola, con K1 ya abierto y S1 sin presionar. ¿M1 vuelve a funcionar?", "No: K1 se abrió y sin S1 ni memoria no hay vía; así se evita un arranque inesperado", "Sí: K1 recuerda que estaba en marcha", "Sí, porque F1 es NC", "La memoria se pierde cuando K1 se abre; hace falta una nueva orden con S1."),
        ("=", "{F} Cuatro máquinas como M1, de 1100 W cada una, funcionan a la vez en un tablero de ejemplo a 220 V. ¿Cuántos amperios usan?", "4*1100//220", "Se multiplica la potencia por 4 y se divide por la tensión.", " A"),
        ("abc", "{F} Si F1, S2 y S3 están en reposo y S1 está presionado, ¿cuántas condiciones de la regla se cumplen?", "Las cuatro: S1 presionado, S2 sin presionar, S3 sin accionar y F1 sin activar", "Solo tres, porque S1 no cuenta", "Solo una, porque basta S1", "Las cuatro condiciones se cumplen y la bobina se energiza."),
    ],
    ctx=("abc", "{F} Un técnico de ejemplo dice: «cambié S2 por un contacto NA porque el NC me daba problemas». ¿Qué corresponde?", "Informar al responsable: una parada NA ya no es falla segura y debe revisarse antes de usar la máquina", "Aceptar, porque la máquina arranca igual", "Aceptar si lo anota en un registro", "Cambiar el tipo de contacto altera la seguridad del mando y lo decide el proyectista."),
    sc=[
        ("En Electricidad: ¿qué es un contacto normalmente cerrado (NC)?", "Uno que conduce salvo mientras se acciona", "Por eso las paradas usan contactos NC."),
        ("¿Qué significa «Y» en una regla de mando?", "Que deben cumplirse todas las condiciones", "Basta una condición incumplida para que la regla falle."),
        ("¿Qué es una falla segura?", "Una falla que deja la máquina detenida", "No deja la máquina en marcha."),
    ],
    op=("Esquema de ejemplo de una bomba: B1 = motor; PM = pulsador de marcha (NA); PP = pulsador de parada (NC); PE = parada de emergencia (NC); KB = contactor con memoria. Regla: la bobina de KB se energiza si (PM presionado O KB cerrado) Y PP sin presionar Y PE sin accionar. Escribe qué ocurre en cada caso: (a) KB abierto y se presiona PM, (b) B1 funciona y se presiona PP, (c) B1 funciona y se acciona PE, (d) KB abierto, nadie presiona PM y PP y PE en reposo, (e) por qué PP es NC.",
        "(a) La bobina se energiza, KB se cierra y B1 funciona. (b) Se corta la vía, KB se abre y B1 se detiene. (c) Igual: B1 se detiene. (d) B1 no funciona: falta PM o la memoria. (e) Porque, con un NC, si la vía se corta por una falla, la máquina se detiene; es una falla segura.",
        ["lee bien la condición Y", "interpreta los contactos NC", "reconoce la memoria", "explica la falla segura"],
        ["hoja con las cinco respuestas"],
        ["creer que la memoria ignora la parada", "decir que PP debe ser NA", "olvidar la condición O"],
        "Pregunta: «¿qué pasa si PE se acciona con B1 en marcha?». Si no responde, pídele que relea la regla con las condiciones Y."),
    reinforce="Escribe una regla de mando de una luz con dos interruptores usando las palabras «Y» y «O», y di en qué casos se enciende.",
    extend="Explica con un ejemplo por qué un arranque inesperado después de volver la energía es peligroso.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (revisión de proyecto de ejemplo, inventada). Máquina «Mezcladora M-2» (ficticia). Placa del motor: 1100 W, 220 V, corriente nominal 5 A, monofásico. "
     "Especificaciones del fabricante (de ejemplo): protección contra sobrecarga con ajuste mayor que la corriente nominal y menor que el límite del circuito; parada de emergencia visible; tablero rotulado. "
     "Proyecto: límite del circuito de ejemplo 8 A; ajuste propuesto de la protección 6 A; no incluye parada de emergencia; el tablero no está rotulado. "
     "La máquina usa aceite lubricante y el proyecto no dice qué se hace con el aceite usado.")
build(
    O7, 3, F,
    use="Aprenderé a revisar en papel un proyecto de control contra las especificaciones del fabricante y a anotar lo que cumple y lo que no.",
    prior=["Sé leer una placa de características.", "Sé qué son las protecciones.", "Sé comparar requisitos con datos."],
    explain=[
        "Las especificaciones del fabricante son las condiciones que exige quien fabricó la máquina para usarla de forma segura y correcta. Una lista de requisitos pone en una tabla cada exigencia y, al lado, lo que trae el proyecto: cumple o no cumple. Para revisar la protección contra sobrecarga se compara su ajuste con la corriente nominal del motor y con el límite del circuito: debe quedar por encima de la primera y por debajo del segundo. Los valores de esta ficha son de ejemplo.",
        "Lo que no cumple se anota como no conformidad y se informa al proyectista; el revisor no corrige el proyecto por su cuenta. La norma vigente de control del medio ambiente también se revisa: si la máquina genera residuos, el proyecto debe decir cómo se gestionan. El informe final deja claro qué cumple, qué no, qué datos se usaron y a quién se informó.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("especificaciones del fabricante", "condiciones que exige el fabricante para usar la máquina de forma segura y correcta"), ("lista de requisitos", "tabla que compara cada exigencia con lo que trae el proyecto"), ("no conformidad", "punto que no cumple un requisito"), ("ajuste de la protección", "valor de corriente al que actúa la protección")],
    worked=[
        ("Revisar un ajuste", "Un motor de ejemplo tiene corriente nominal 4 A y el circuito un límite de 7 A. Una protección se ajusta en 5 A. ¿Cumple?", ["Debe ser mayor que 4 A y menor que 7 A.", "5 está entre 4 y 7."], "Cumple"),
        ("Corriente de la placa", "La placa de un motor de ejemplo dice 660 W y 220 V. ¿Cuál es su corriente nominal?", ["La corriente es la potencia dividida por la tensión.", "660 dividido por 220 son 3."], "3 A"),
    ],
    mistakes=[("Corregir el proyecto «a ojo» para que cumpla.", "El revisor informa; el proyectista corrige.", "Anota la no conformidad e informa."),
              ("Olvidar los residuos al revisar un proyecto eléctrico.", "La norma vigente de control del medio ambiente también aplica.", "Incluye una fila de residuos en la lista de requisitos.")],
    T=[
        ("abc", "En Electricidad: ¿qué son las especificaciones del fabricante?", "Las condiciones que exige el fabricante para usar la máquina de forma segura y correcta", "Las preferencias del cliente sobre el aspecto de la máquina", "Las medidas del taller donde se instala", "Las especificaciones del fabricante fijan exigencias de uso; no son preferencias ni medidas del taller."),
        ("abc", "En Electricidad: ¿para qué sirve una lista de requisitos?", "Para comparar cada exigencia con lo que trae el proyecto y marcar si cumple", "Para calcular el precio del proyecto", "Para dibujar el esquema de mando", "La lista contrasta exigencias y diseño; el precio y el dibujo son otros documentos."),
        ("=", "Un motor de ejemplo de 660 W funciona a 220 V. ¿Cuántos amperios usa?", "660//220", "La corriente es la potencia dividida por la tensión.", " A"),
        ("abc", "{F} ¿Es coherente la corriente nominal de la placa con su potencia y su tensión?", "Sí: 1100 W divididos por 220 V son 5 A", "No: debería ser 1100 A", "No: la corriente nominal no depende de la potencia", "I = P ÷ V y 1100 dividido por 220 da 5."),
        ("abc", "{F} Sin contar el aceite, ¿cuántos requisitos del fabricante incumple el proyecto?", "Dos: la parada de emergencia y el rotulado", "Uno: solo la parada de emergencia", "Tres: la protección, la parada y el rotulado", "El ajuste de la protección sí cumple; fallan parada y rotulado."),
        ("abc", "{F} ¿Cumple el ajuste de 6 A la exigencia sobre la protección contra sobrecarga?", "Sí: 6 A es mayor que la corriente nominal de 5 A y menor que el límite de 8 A", "No: debe ser exactamente 5 A", "No: debe ser mayor que 8 A", "El ajuste debe quedar entre la corriente nominal y el límite del circuito."),
        ("=", "{F} ¿Cuántos amperios de margen hay entre la corriente nominal y el límite del circuito?", "8-5", "Al límite del circuito se le resta la corriente nominal.", " A"),
        ("=", "{F} La mezcladora trabaja 6 horas al día durante 20 días. ¿Cuántos kWh consume el motor en el mes?", "1100*6*20//1000", "Se multiplica la potencia por las horas del mes y se pasa a kWh.", " kWh"),
        ("abc", "{F} ¿Qué corresponde con el aceite usado, que el proyecto no menciona?", "Pedir que el proyecto incluya cómo se gestiona como residuo según la norma vigente de control del medio ambiente", "Nada: el aceite no es parte del proyecto eléctrico", "Botarlo con la basura del taller", "Un residuo de la máquina debe tener una gestión definida desde el proyecto."),
        ("abc", "{F} Un compañero dice que se puede omitir la parada de emergencia porque «la mezcladora es pequeña». ¿Qué respuesta es correcta?", "No: es un requisito del fabricante; se informa para que el proyectista la incorpore", "Sí: las máquinas pequeñas no la necesitan", "Sí, si se coloca un cartel de advertencia", "Un requisito del fabricante no se omite por el tamaño ni se reemplaza por un cartel."),
        ("ab", "{F} El proyectista propone ajustar la protección en 9 A «para que no se active tanto». ¿Qué corresponde?", "No: 9 A supera el límite del circuito de 8 A; el ajuste debe quedar por debajo y lo decide el proyectista", "Sí: ajustar más alto evita molestias", "Un ajuste sobre el límite del circuito deja de proteger; no se hace por comodidad."),
        ("abc", "{F} Dos mezcladoras iguales funcionan a la vez en el mismo circuito de 8 A. ¿Qué resultado da?", "Usan 10 A y superan el límite del circuito de 8 A", "Usan 5 A y cumplen", "Usan 10 A y cumplen", "Dos motores de 5 A suman 10 A, más que 8 A."),
        ("abc", "{F} ¿Qué debe contener el informe de revisión del proyecto?", "Los requisitos, qué cumple y qué no, los datos usados y a quién se informa", "Solo la palabra «aprobado»", "Solo el nombre de quien revisó", "El informe debe permitir que otra persona repita y entienda la revisión."),
    ],
    ctx=("abc", "{F} El cliente pide aprobar el proyecto de M-2 de inmediato «porque la protección ya está bien ajustada». ¿Qué corresponde?", "Explicar que aún faltan la parada de emergencia, el rotulado y la gestión del aceite, y registrar las no conformidades", "Aprobar, porque la protección es lo más importante", "Aprobar y corregir lo demás después", "Un proyecto con requisitos incumplidos no se aprueba, aunque otra parte esté bien."),
    sc=[
        ("En Electricidad: ¿entre qué valores debe quedar el ajuste de la protección?", "Sobre la corriente nominal y bajo el límite del circuito", "Así protege sin activarse por el uso normal."),
        ("¿Qué hace el revisor con un requisito incumplido?", "Lo anota como no conformidad e informa al proyectista", "El revisor no corrige el proyecto por su cuenta."),
        ("¿Qué debe decir el proyecto sobre los residuos de la máquina?", "Cómo se gestionan según la norma vigente", "Los residuos también son parte del proyecto."),
    ],
    op=("Ficha de ejemplo «Taladro T-4» (ficticio): motor de 880 W a 220 V; límite del circuito 7 A; ajuste propuesto de la protección: 8 A; el proyecto incluye parada de emergencia pero no rotula el tablero; usa refrigerante que se desecha. Escribe (a) la corriente nominal del motor, (b) si el ajuste de 8 A cumple y por qué, (c) qué requisitos faltan, (d) qué haces con lo que no cumple.",
        "(a) 880 dividido por 220 son 4 A. (b) No cumple: 8 A supera el límite del circuito de 7 A. (c) Falta rotular el tablero y definir la gestión del refrigerante desechado. (d) Lo anoto como no conformidad e informo al proyectista, que corrige.",
        ["calcula la corriente nominal", "compara el ajuste con el límite", "lista los requisitos faltantes", "informa en lugar de corregir"],
        ["hoja con las cuatro respuestas"],
        ["decir que 8 A cumple", "olvidar el refrigerante", "corregir sin informar"],
        "Pregunta: «¿entre qué valores debía quedar el ajuste?». Si no responde, pídele que relea cómo se revisa la protección."),
    reinforce="Inventa una lista de requisitos con cuatro filas para una máquina y marca cuáles cumple un proyecto imaginario.",
    extend="Explica con un ejemplo por qué una protección ajustada sobre el límite del circuito deja de cumplir su función.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (alternativas de control de ejemplo, ficticias). Una máquina necesita al menos 6 entradas (pulsadores y sensores) y 3 salidas (contactores y una señal luminosa). Requisitos del proyecto: consumo de mando de 20 W como máximo y presupuesto de $220.000 como máximo. "
     "Alternativa 1: lógica con contactores y relés auxiliares: 6 entradas, 3 salidas, 30 W, $120.000. Alternativa 2: controlador programable de ejemplo: 8 entradas, 4 salidas, 15 W, $210.000. "
     "Alternativa 3: controlador programable pequeño: 4 entradas, 2 salidas, 10 W, $150.000. El mando funciona 600 horas al mes. Energía de ejemplo: $150 por kWh.")
build(
    O7, 4, F,
    use="Aprenderé a elegir entre alternativas de control con criterios técnicos, de energía y de medio ambiente, y a dejar la decisión registrada.",
    prior=["Sé comparar requisitos con opciones.", "Sé calcular energía en kWh.", "Sé qué es un residuo."],
    explain=[
        "Un controlador programable es un equipo electrónico que ejecuta la lógica de control según un programa. Cambiar la lógica por programa permite modificarla sin reemplazar piezas del mando, pero cada cambio debe ser autorizado y registrado. Para elegir una alternativa se comparan sus datos con los requisitos del proyecto: entradas, salidas, consumo y presupuesto. La que falla en cualquier requisito se descarta; entre las que cumplen todo se compara el costo total, que incluye la energía durante el uso.",
        "El medio ambiente también cuenta: los equipos electrónicos desechados son residuos que la norma vigente manda entregar a una gestión autorizada, no botar con la basura común. Las cifras de esta ficha son de ejemplo. La decisión se registra con los datos comparados, los criterios y quién autorizó.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("controlador programable", "equipo electrónico que ejecuta la lógica de control según un programa"), ("entrada", "señal que recibe el controlador, como un pulsador o un sensor"), ("salida", "señal que entrega el controlador, como la orden a un contactor"), ("residuo electrónico", "equipo electrónico desechado, que se entrega a gestión autorizada")],
    worked=[
        ("Revisar un requisito", "Un proyecto de ejemplo exige al menos 5 entradas. Una alternativa tiene 4. ¿Cumple?", ["Debe tener 5 o más.", "4 es menos que 5."], "No cumple"),
        ("Energía del mando", "Un mando de ejemplo de 20 W funciona 500 horas. ¿Cuántos kWh consume?", ["20 por 500 son 10.000 Wh.", "10.000 dividido por 1000 son 10."], "10 kWh"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar todos los requisitos.", "Puede incumplir entradas, salidas o consumo.", "Descarta primero lo que falla."),
              ("Botar un controlador desechado con la basura común.", "Es un residuo electrónico que la norma vigente manda gestionar aparte.", "Entrégalo a una gestión autorizada y regístralo.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un controlador programable?", "Un equipo electrónico que ejecuta la lógica de control según un programa", "Un motor que se programa para girar", "Un plano que se imprime con la lógica de la máquina", "El controlador programable ejecuta la lógica de control; no es motor ni plano."),
        ("abc", "En Electricidad: ¿qué ventaja tiene cambiar la lógica de control por programa?", "Se puede modificar sin reemplazar piezas del mando, pero el cambio debe ser autorizado y registrado", "No requiere ninguna autorización", "Elimina la necesidad de protecciones", "Programar permite cambios rápidos, que igual deben ser autorizados y registrados."),
        ("=", "Un mando de ejemplo de 40 W funciona 250 horas al mes. ¿Cuántos kWh consume?", "40*250//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("abc", "{F} ¿Qué alternativa incumple el requisito de entradas?", "La alternativa 3, con 4 entradas", "La alternativa 1, con 6 entradas", "La alternativa 2, con 8 entradas", "El proyecto pide al menos 6 y la alternativa 3 solo tiene 4."),
        ("abc", "{F} ¿Por qué se descarta la alternativa 1?", "Su consumo de 30 W supera el máximo de 20 W", "Tiene menos entradas que las pedidas", "Su precio supera los $220.000", "La alternativa 1 cumple entradas, salidas y precio; falla en el consumo."),
        ("abc", "{F} ¿Qué alternativa cumple todos los requisitos?", "La alternativa 2", "La alternativa 1", "La alternativa 3", "Solo la 2 cumple entradas, salidas, consumo y precio."),
        ("=", "{F} ¿Cuántos kWh consume al mes la alternativa 2?", "15*600//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuántos kWh consume la alternativa 1 en el mismo mes?", "30*600//1000", "Se multiplica la potencia por las horas y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuántos pesos al mes cuesta la energía de la alternativa 2?", "15*600//1000*150", "Se calculan los kWh y se multiplican por el precio de cada kWh.", " pesos"),
        ("abc", "{F} Un compañero dice que la alternativa 1 conviene porque es la más barata. ¿Qué respuesta es correcta?", "Incumple el consumo máximo; el precio solo se compara entre las alternativas que cumplen todo", "Tiene razón: el precio es el único criterio", "Tiene razón porque consume menos que la 2", "Un requisito incumplido descarta la alternativa, y la 1 consume más, no menos."),
        ("ab", "{F} La alternativa 2 permite cambiar la lógica por programa. ¿Quién puede hacerlo?", "Solo personal autorizado, con una solicitud aprobada y registro del cambio", "Cualquier operador que conozca la clave", "Un cambio de lógica afecta la seguridad de la máquina y exige autorización y registro."),
        ("=", "{F} Si el controlador se reemplaza cada 5 años y el taller tiene 4 máquinas con uno cada una, ¿cuántos controladores desechará en 10 años?", "4*10//5", "Se calculan los reemplazos por máquina en 10 años y se multiplican por 4.", " controladores"),
        ("abc", "{F} ¿Qué se hace con los controladores desechados?", "Se entregan a una gestión autorizada de residuos electrónicos, según la norma vigente de control del medio ambiente", "Se botan con la basura común", "Se guardan indefinidamente en cualquier lugar", "Los residuos electrónicos tienen gestión definida por la norma vigente."),
    ],
    ctx=("abc", "{F} El proveedor de ejemplo ofrece una alternativa 4 con 8 entradas, 4 salidas, 25 W y $140.000. El jefe pide aceptarla por ser barata. ¿Qué corresponde?", "Descartarla porque su consumo de 25 W supera el máximo de 20 W, salvo que quien autoriza el proyecto cambie el requisito", "Aceptarla porque es la más barata", "Aceptarla porque tiene más entradas", "Un requisito incumplido descarta la opción; solo quien autoriza el proyecto puede modificarlo."),
    sc=[
        ("En Electricidad: ¿qué se descarta primero al comparar alternativas?", "Las que incumplen algún requisito", "El precio se compara después entre las que cumplen todo."),
        ("¿Quién autoriza un cambio de programa?", "Personal autorizado, con solicitud aprobada", "Todo cambio queda registrado por escrito para poder revisarlo."),
        ("¿Qué se hace con un equipo electrónico desechado?", "Se entrega a una gestión autorizada de residuos", "No se bota con la basura común."),
    ],
    op=("Requisitos de ejemplo: al menos 4 entradas y 2 salidas; consumo máximo 12 W; presupuesto máximo $100.000. Alternativas: A: 4 entradas, 2 salidas, 10 W, $90.000; B: 6 entradas, 3 salidas, 14 W, $80.000; C: 4 entradas, 2 salidas, 8 W, $95.000. El mando funciona 500 horas al mes; energía a $140 por kWh. Escribe (a) qué alternativas cumplen, (b) cuál eliges y por qué, (c) los kWh y pesos mensuales de energía de la elegida, (d) qué haces con el equipo cuando se deseche.",
        "(a) Cumplen A y C; B falla en consumo (14 W mayor que 12 W). (b) A, porque cumple todo y cuesta menos que C. (c) 10 por 500 son 5000 Wh, es decir, 5 kWh; 5 por 140 son 700 pesos. (d) Lo entrego a una gestión autorizada de residuos electrónicos y lo registro.",
        ["descarta con la razón", "elige la más barata entre las que cumplen", "calcula la energía y el costo", "gestiona el residuo"],
        ["hoja con la tabla de comparación y los cálculos"],
        ["elegir B por precio", "olvidar las horas", "botar el equipo"],
        "Pregunta: «¿por qué B no se elige aunque sea la más barata?». Si no responde, pídele que relea qué se descarta primero."),
    reinforce="Inventa un requisito con tres condiciones y tres alternativas; indica cuál cumple y por qué.",
    extend="Explica con un ejemplo por qué el consumo de energía durante el uso puede pesar más que una pequeña diferencia de precio.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (planta de ejemplo, inventada). «Planta Agua Clara» (ficticia): una bomba llena un estanque y es controlada por un equipo de control. Parámetros actuales del equipo: nivel de arranque 30 %; nivel de parada 80 %; "
     "tiempo máximo de funcionamiento continuo 20 minutos. Documentos: manual del equipo, tabla de parámetros y bitácora de cambios. "
     "Riesgo anotado: un cambio incorrecto puede hacer arrancar la bomba mientras una persona trabaja cerca, o dejarla funcionando sin control.")
build(
    O8, 1, F,
    use="Aprenderé qué son un programa y un parámetro, por qué cambiarlos tiene riesgos y quién los autoriza, siempre en papel y sin tocar ningún equipo.",
    prior=["Sé qué es un sistema de control.", "Sé qué es una protección.", "Sé que los cambios se registran y se autorizan."],
    explain=[
        "Un programa es el conjunto de instrucciones que un equipo de control ejecuta para controlar un proceso. Un parámetro es un valor ajustable que define cómo se comporta el equipo, como un nivel, un tiempo o una velocidad. Los requerimientos operacionales son lo que necesita el proceso o la planta: qué debe hacer el equipo, cuándo y con qué límites. Modificar un programa o un parámetro cambia el comportamiento real de una máquina, por eso es una tarea de personal autorizado, con la norma vigente de la SEC y la aprobación de la persona responsable de la planta.",
        "Un cambio mal hecho puede hacer arrancar una máquina cuando una persona trabaja cerca, anular una protección o dejar el proceso sin control. Por eso todo cambio sigue un orden de gestión en papel: una solicitud escrita con el motivo, la revisión contra los límites del fabricante, la aprobación del responsable, un respaldo del programa anterior y un registro en la bitácora. Las claves de acceso son personales y no se comparten. Este cuaderno no enseña a modificar equipos.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("programa", "conjunto de instrucciones que un equipo de control ejecuta"), ("parámetro", "valor ajustable que define cómo se comporta el equipo"), ("requerimiento operacional", "lo que necesita el proceso o la planta del equipo de control"), ("solicitud de cambio", "documento escrito que pide un cambio y explica el motivo"), ("respaldo", "copia del programa anterior que se guarda antes de un cambio"), ("bitácora de cambios", "registro cronológico de los cambios hechos a un equipo")],
    worked=[
        ("Parámetro o programa", "En un equipo de ejemplo, «tiempo de espera: 10 s», ¿es un parámetro o un programa?", ["Es un valor ajustable.", "Un programa es un conjunto de instrucciones."], "Es un parámetro"),
        ("Contar un rango", "Un parámetro de ejemplo va de un nivel de arranque de 20 % a uno de parada de 70 %. ¿Cuántos puntos porcentuales hay entre ambos?", ["Se resta el nivel menor al mayor.", "70 menos 20 son 50."], "50 puntos porcentuales"),
    ],
    mistakes=[("Cambiar un parámetro «solo un poco» sin solicitud ni registro.", "Un valor distinto puede cambiar la seguridad del proceso.", "Todo cambio lleva solicitud, aprobación y registro."),
              ("Compartir la clave de acceso con un compañero para ahorrar tiempo.", "Deja de saberse quién hizo cada cambio.", "Las claves son personales.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un parámetro de un equipo de control?", "Un valor ajustable que define cómo se comporta el equipo, como un nivel o un tiempo", "Una pieza física del equipo", "Un cable que lo conecta a la red", "El parámetro es un valor de ajuste; no es una pieza ni un cable."),
        ("abc", "En Electricidad: ¿qué es un programa en un equipo de control?", "Un conjunto de instrucciones que el equipo ejecuta para controlar un proceso", "El manual de usuario del equipo", "La placa de características", "El programa son las instrucciones que se ejecutan; el manual y la placa son documentos."),
        ("abc", "En Electricidad: ¿para qué sirve el respaldo antes de un cambio?", "Para guardar una copia del programa anterior y poder volver atrás", "Para aumentar la velocidad del equipo", "Para borrar la bitácora", "El respaldo conserva el estado anterior para poder restituirlo."),
        ("=", "{F} ¿Cuántos puntos porcentuales hay entre el nivel de arranque y el nivel de parada?", "80-30", "Se resta el nivel de arranque al de parada.", " puntos"),
        ("abc", "{F} ¿Qué riesgo tiene cambiar un parámetro sin autorización en esa planta?", "Que la bomba arranque mientras una persona trabaja cerca o quede funcionando sin control", "Que la bomba funcione igual que antes en todos los casos", "Que solo cambie el nombre del parámetro en el manual", "La ficha anota esos riesgos; el cambio altera el comportamiento real."),
        ("=", "{F} ¿Cuántos ciclos de funcionamiento continuo de 20 minutos caben en 2 horas?", "120//20", "Se pasan 2 horas a 120 minutos y se divide por 20.", " ciclos"),
        ("=", "{F} Si el tiempo máximo de funcionamiento continuo pasara de 20 a 25 minutos, ¿cuántos minutos más funcionaría la bomba seguidos?", "25-20", "Se resta el tiempo actual al nuevo.", " minutos"),
        ("abc", "{F} Un operador quiere cambiar el nivel de arranque a 50 % «porque la bomba parte tarde». ¿Qué corresponde?", "Presentar una solicitud escrita con el motivo, para que el responsable la revise y la apruebe", "Cambiarlo él mismo y avisar después", "Pedirle la clave a un compañero para hacerlo más rápido", "Un cambio se pide por escrito, se revisa y se aprueba antes de hacerse."),
        ("abc", "{F} Un compañero dice que no hace falta respaldo porque «es un cambio pequeño». ¿Qué respuesta es correcta?", "El respaldo se hace siempre, porque permite volver al estado anterior si el cambio falla", "Tiene razón: los cambios pequeños no necesitan respaldo", "El respaldo solo se hace si el equipo es nuevo", "Un cambio pequeño también puede fallar; el respaldo permite revertirlo."),
        ("ab", "Un estudiante ha leído esta clase y quiere modificar los parámetros de una bomba real. ¿Qué corresponde?", "No hacerlo: esa tarea la realiza personal autorizado, con aprobación y norma vigente", "Hacerlo con cuidado, porque ya conoce el concepto", "Conocer el concepto en papel no habilita para modificar equipos reales."),
        ("=", "{F} Una planta de ejemplo tiene 6 equipos como el de la ficha y cada uno registra 3 cambios al año. ¿Cuántos registros de cambio hay en 2 años?", "6*3*2", "Se multiplican los equipos por los cambios anuales y por los años.", " registros"),
        ("abc", "{F} ¿Qué debe contener un registro de la bitácora de cambios?", "Qué se cambió, el valor anterior y el nuevo, el motivo, quién lo autorizó y la fecha", "Solo la fecha", "Solo el nombre de quien tecleó el valor", "El registro debe permitir reconstruir qué pasó y quién lo autorizó."),
        ("abc", "{F} Una persona queda sin conocimiento tras tocar un tablero de la planta y sigue en contacto con la energía. ¿Qué indican las reglas generales?", "No tocarla, cortar el suministro solo si se está autorizado, avisar a un adulto responsable y a emergencias", "Tirar de ella para separarla de inmediato", "Esperar a ver si despierta antes de avisar", "Tocarla puede transmitir la descarga; se avisa y se corta el suministro solo si se está autorizado."),
    ],
    ctx=("abc", "{F} Un proveedor de ejemplo ofrece cambiar los parámetros «por teléfono, sin papeles» para ahorrar tiempo. ¿Qué corresponde?", "Pedir la solicitud por escrito y la aprobación del responsable antes de cualquier cambio", "Aceptar, porque el proveedor conoce el equipo", "Aceptar si el proveedor da su nombre", "Un cambio sin solicitud, aprobación ni registro no se puede revisar ni revertir."),
    sc=[
        ("En Electricidad: ¿qué es un parámetro?", "Un valor ajustable que define cómo se comporta el equipo", "Un parámetro es un ajuste, no una pieza del equipo."),
        ("¿Qué se guarda antes de un cambio de programa?", "Un respaldo del programa anterior", "Así se puede volver al estado anterior."),
        ("¿Se comparte la clave de acceso a un equipo?", "No, las claves son personales", "Compartirla impide saber quién hizo cada cambio."),
    ],
    op=("Planta de ejemplo «Aguas Sur» (ficticia): una bomba con equipo de control; parámetros actuales: nivel de arranque 25 %, nivel de parada 85 %, tiempo máximo continuo 15 minutos. Un operador pide cambiar el nivel de arranque a 40 %. Escribe (a) cuántos puntos porcentuales hay entre arranque y parada ahora y con el cambio pedido, (b) qué documentos se necesitan antes de hacer el cambio, (c) quién lo realiza y quién lo aprueba, (d) un riesgo de cambiarlo sin autorización.",
        "(a) Ahora: 85 menos 25 son 60 puntos. Con el cambio: 85 menos 40 son 45 puntos. (b) Solicitud escrita con el motivo, respaldo del programa y registro en la bitácora. (c) Lo realiza personal autorizado y lo aprueba el responsable de la planta. (d) Que la bomba arranque cuando una persona trabaja cerca o quede sin control.",
        ["calcula bien las diferencias", "nombra los documentos", "distingue quién realiza y quién aprueba", "reconoce un riesgo real"],
        ["hoja con las cuatro respuestas"],
        ["restar mal", "decir que el operador puede cambiarlo solo", "olvidar el respaldo"],
        "Pregunta: «¿qué pasa si no hay respaldo?». Si no responde, pídele que relea para qué sirve el respaldo."),
    reinforce="Escribe una solicitud de cambio de ejemplo con tres datos: qué se pide cambiar, el motivo y quién debe aprobar.",
    extend="Explica con un ejemplo por qué es importante saber quién hizo cada cambio en un equipo de control.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (tabla de parámetros de ejemplo, inventada). Equipo de control de la «Planta Agua Clara». P1, nivel de arranque: actual 30 %, mínimo 10 %, máximo 50 %, de fábrica 25 %. "
     "P2, nivel de parada: actual 80 %, mínimo 60 %, máximo 95 %, de fábrica 85 %. P3, tiempo máximo continuo: actual 20 min, mínimo 5 min, máximo 30 min, de fábrica 15 min. "
     "P4, retardo de arranque: actual 10 s, mínimo 0 s, máximo 60 s, de fábrica 5 s. Regla de coherencia del fabricante: el nivel de arranque debe ser menor que el nivel de parada.")
build(
    O8, 2, F,
    use="Aprenderé a leer una tabla de parámetros, sus rangos, unidades y valores de fábrica, y a revisar si un valor pedido es coherente, todo en papel.",
    prior=["Sé qué es un parámetro.", "Sé convertir minutos y segundos.", "Sé comparar un valor con un rango."],
    explain=[
        "Una tabla de parámetros dice, para cada parámetro, su valor actual, su mínimo, su máximo, su unidad y su valor de fábrica, que es el que trae el equipo desde el origen. El rango es el conjunto de valores permitidos, desde el mínimo hasta el máximo; un valor fuera del rango no se acepta. Las unidades importan: 1 minuto son 60 segundos y 1 hora son 60 minutos, y un valor en la unidad equivocada puede quedar fuera de rango sin que nadie lo note.",
        "La coherencia entre parámetros también se revisa: por ejemplo, el nivel de arranque debe ser menor que el de parada, o el equipo no funcionaría como debe. Antes de pedir un cambio se verifica el rango, la unidad y la coherencia en el papel. Quien solicita no cambia nada: lo hace personal autorizado con aprobación, respaldo y registro.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("rango", "valores permitidos de un parámetro, desde el mínimo hasta el máximo"), ("valor de fábrica", "valor con que el equipo viene desde el origen"), ("unidad", "forma de medir un parámetro, como %, minutos o segundos"), ("coherencia", "que los valores de varios parámetros no se contradigan entre sí"), ("fuera de rango", "valor menor que el mínimo o mayor que el máximo permitido")],
    worked=[
        ("Revisar un rango", "Un parámetro de ejemplo tiene mínimo 10 y máximo 40. ¿Es aceptable el valor 35?", ["Se compara con el mínimo y el máximo.", "35 está entre 10 y 40."], "Sí, está dentro del rango"),
        ("Cambiar de unidad", "Un tiempo de ejemplo se pide como 2 minutos y el parámetro está en segundos. ¿Cuántos segundos son?", ["1 minuto son 60 segundos.", "2 por 60 son 120."], "120 s"),
    ],
    mistakes=[("Ingresar 2 en un parámetro de segundos creyendo que son 2 minutos.", "El valor queda mal por una diferencia de unidad.", "Convierte siempre a la unidad del parámetro."),
              ("Revisar cada parámetro por separado y no su coherencia.", "Dos valores válidos pueden contradecirse entre sí.", "Compara también los parámetros entre sí.")],
    T=[
        ("abc", "En Electricidad: ¿qué es el valor de fábrica de un parámetro?", "El valor con que el equipo viene desde el origen", "El valor máximo que acepta el parámetro", "El último valor que cambió el operador", "El valor de fábrica es el de origen; el máximo y el último cambio son otros datos."),
        ("abc", "En Electricidad: ¿qué es el rango de un parámetro?", "Los valores permitidos, desde el mínimo hasta el máximo", "El valor que tiene hoy el parámetro", "El nombre del parámetro", "El rango limita los valores aceptables; el valor actual es solo uno de ellos."),
        ("=", "Un tiempo de ejemplo es de 3 minutos. ¿Cuántos segundos son?", "3*60", "Cada minuto tiene 60 segundos.", " s"),
        ("abc", "{F} ¿Está 45 % dentro del rango del parámetro P1?", "Sí: está entre 10 % y 50 %", "No: supera el valor actual de 30 %", "No: es menor que el valor de fábrica", "El rango es de 10 % a 50 %, y 45 % queda dentro."),
        ("abc", "{F} ¿Está 70 % dentro del rango del parámetro P1?", "No: supera el máximo de 50 %", "Sí: es menor que el nivel de parada", "Sí: es mayor que el valor de fábrica", "El máximo de P1 es 50 %; 70 % está fuera de rango."),
        ("=", "{F} P3 se pide como 0,5 horas. ¿Cuántos minutos son?", "60//2", "Media hora son 30 minutos.", " minutos"),
        ("abc", "{F} Se pide P3 = 0,5 horas, que son 30 minutos. ¿Es un valor aceptable para P3?", "Sí: son 30 minutos y el máximo de P3 es 30 minutos", "No: supera el máximo de 30 minutos", "No: es menor que el mínimo de 5 minutos", "30 minutos igualan el máximo, que es un valor permitido."),
        ("=", "{F} P4 se pide como 2 minutos. ¿Cuántos segundos son?", "2*60", "Cada minuto tiene 60 segundos.", " s"),
        ("abc", "{F} ¿Es aceptable el valor de P4 de 2 minutos?", "No: son 120 s y el máximo es 60 s", "Sí: 2 es menor que 60", "Sí: 2 minutos es el valor de fábrica", "Al pasar a segundos son 120, mayor que el máximo de 60 s."),
        ("abc", "{F} Se pide P1 = 45 % y P2 = 40 %. ¿Se cumple la regla de coherencia?", "No: P2 = 40 % está fuera de rango y además no queda mayor que P1", "Sí: ambos valores son menores que 50 %", "Sí: P1 es mayor que P2", "P2 debe estar entre 60 % y 95 % y mayor que P1; 40 % no cumple."),
        ("ab", "{F} Un operador dice que escribirá 2 en P4 «porque 2 es menor que 60». Quiere decir 2 minutos. ¿Qué corresponde?", "Aclarar que 2 minutos son 120 s y que supera el máximo; el valor se revisa en la unidad del parámetro", "Escribir 2: el equipo entiende minutos", "Un valor se revisa siempre en la unidad del parámetro, no en la que uno imagina."),
        ("=", "{F} ¿Cuántos puntos porcentuales hay entre el máximo y el mínimo de P2?", "95-60", "Se resta el mínimo al máximo.", " puntos"),
        ("abc", "{F} ¿Qué debe hacer quien solicita cambiar un parámetro al valor de fábrica?", "Presentar la solicitud y esperar la aprobación y el trabajo de personal autorizado", "Reponer el valor de fábrica él mismo si es el original", "Pedir a un compañero que lo cambie sin registro", "Aunque el valor sea el de fábrica, el cambio sigue el mismo orden de gestión."),
    ],
    ctx=("abc", "{F} Un técnico de ejemplo pide volver P3 a 40 minutos «porque así funcionaba la bomba antigua». ¿Qué corresponde?", "Rechazar el valor: supera el máximo de 30 minutos de la tabla; si hay una necesidad real, se consulta al fabricante y al responsable", "Aceptarlo, porque la bomba antigua lo usaba", "Aceptarlo si lo anota en la bitácora", "Un valor fuera de rango no se acepta, aunque tenga historia; se consulta a quien corresponde."),
    sc=[
        ("En Electricidad: ¿cuántos segundos tiene un minuto?", "60 segundos", "Un minuto equivale a 60 segundos."),
        ("¿Qué se revisa antes de pedir un valor nuevo?", "Su rango, su unidad y su coherencia con otros parámetros", "Un valor fuera de rango no se acepta."),
        ("¿Qué es el valor de fábrica?", "El valor con que el equipo viene desde el origen", "No es el máximo ni el último cambio."),
    ],
    op=("Tabla de ejemplo de un equipo de «Aguas Sur»: Q1, nivel de arranque: actual 25 %, rango 10 % a 40 %; Q2, nivel de parada: actual 85 %, rango 60 % a 95 %; Q3, tiempo máximo continuo: actual 15 min, rango 5 a 25 min; Q4, retardo: actual 5 s, rango 0 a 30 s. Regla de coherencia: arranque menor que parada. Se solicita: Q1 = 45 %, Q2 = 90 %, Q3 = 0,25 horas y Q4 = 1 minuto. Escribe (a) cuáles valores están dentro de su rango, (b) los segundos y los minutos de las conversiones, (c) si se cumple la regla de coherencia con los valores aceptables, (d) qué haces con los fuera de rango.",
        "(a) Q2 = 90 % está en rango; Q3 = 0,25 horas son 15 minutos, en rango; Q1 = 45 % supera el máximo de 40 %; Q4 = 1 minuto son 60 s y supera el máximo de 30 s. (b) 0,25 horas son 15 min; 1 minuto son 60 s. (c) Con Q1 actual 25 % y Q2 = 90 %, 25 es menor que 90: se cumple. (d) Los informo al responsable como fuera de rango y no los acepto.",
        ["revisa cada rango", "convierte las unidades", "revisa la coherencia", "informa en lugar de aceptar"],
        ["hoja con la tabla de revisión y las respuestas"],
        ["no convertir unidades", "aceptar valores fuera de rango", "olvidar la coherencia"],
        "Pregunta: «¿por qué 1 minuto no sirve para Q4?». Si no responde, pídele que relea cómo se cambian las unidades."),
    reinforce="Inventa una tabla con tres parámetros (con mínimo, máximo y unidad) y revisa tres valores pedidos.",
    extend="Explica con un ejemplo por qué una diferencia de unidad puede pasar inadvertida en un parámetro.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (solicitud de cambio de ejemplo, inventada). Solicitante: Operador A. (ficticio). Cambios pedidos al equipo de la «Planta Agua Clara»: P1 de 30 % a 55 %; P2 de 80 % a 90 %; P3 de 20 min a 25 min; P4 de 10 s a 1 min 30 s. "
     "Rangos de la tabla: P1 10 % a 50 %; P2 60 % a 95 %; P3 5 a 30 min; P4 0 a 60 s. La solicitud no tiene firma del jefe de planta ni motivo escrito, y no hay respaldo del programa actual.")
build(
    O8, 3, F,
    use="Aprenderé a evaluar en papel una solicitud de cambio de parámetros: rangos, unidades, documentos y aprobación.",
    prior=["Sé leer una tabla de parámetros.", "Sé convertir minutos y segundos.", "Sé qué es un respaldo y una bitácora."],
    explain=[
        "Evaluar una solicitud de cambio es revisar, uno por uno, cada valor pedido: si está dentro del rango, si está en la unidad correcta y si es coherente con los demás. Además se revisan los documentos de la solicitud: motivo escrito, firma del responsable, respaldo del programa actual y espacio en la bitácora. Si falta alguno, la solicitud no puede avanzar aunque los valores estén bien.",
        "El resultado de la evaluación se escribe como una lista: valores aceptables, valores fuera de rango y documentos faltantes. La lista se entrega al responsable de la planta, que decide. La modificación misma, si se aprueba, la hace personal autorizado con la norma vigente de la SEC; quien evalúa no toca el equipo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("solicitud de cambio", "documento que pide un cambio, con motivo y aprobación"), ("evaluar", "revisar si cada parte de la solicitud cumple lo exigido"), ("documento faltante", "documento exigido que no está en la solicitud"), ("responsable de la planta", "persona que decide si se aprueba un cambio")],
    worked=[
        ("Evaluar un valor", "Un parámetro de ejemplo tiene rango de 5 a 30 y se pide 35. ¿Qué se concluye?", ["35 supera el máximo de 30.", "El valor está fuera de rango."], "Fuera de rango"),
        ("Documentos faltantes", "Una solicitud de ejemplo tiene motivo y firma, pero no respaldo. ¿Puede avanzar?", ["El respaldo es un documento exigido.", "Sin él, no avanza."], "No, falta el respaldo"),
    ],
    mistakes=[("Aceptar los valores buenos y aprobar la solicitud aunque falten documentos.", "Sin firma ni respaldo no hay aprobación ni forma de volver atrás.", "Devuelve la solicitud con la lista de faltantes."),
              ("Corregir tú mismo un valor pedido para que entre en rango.", "Cambias lo que pidió el solicitante sin su acuerdo ni el del responsable.", "Informa el valor fuera de rango y espera la nueva solicitud.")],
    T=[
        ("abc", "En Electricidad: ¿qué es evaluar una solicitud de cambio de parámetros?", "Revisar cada valor pedido y los documentos de la solicitud", "Hacer el cambio en el equipo", "Cambiar los valores para que queden en rango", "Evaluar es revisar; el cambio lo hace personal autorizado después de la aprobación."),
        ("abc", "En Electricidad: ¿qué hace el responsable de la planta con la evaluación?", "Decide si se aprueba la solicitud", "Ejecuta el cambio él mismo en el equipo", "Descarta la solicitud sin leerla", "El responsable decide con la evaluación a la vista."),
        ("=", "Un tiempo de ejemplo se pide como 1 minuto 30 segundos. ¿Cuántos segundos son en total?", "60+30", "Se suman los segundos del minuto y los 30 adicionales.", " s"),
        ("abc", "{F} ¿Está P1 = 55 % dentro del rango?", "No: supera el máximo de 50 %", "Sí: es mayor que el valor actual", "Sí: es menor que 60 %", "El máximo de P1 es 50 % y 55 % lo supera."),
        ("abc", "{F} ¿Está P2 = 90 % dentro del rango?", "Sí: está entre 60 % y 95 %", "No: supera el máximo", "No: es menor que el mínimo", "El rango de P2 va de 60 % a 95 % y 90 % queda dentro."),
        ("=", "{F} P4 se pide como 1 minuto 30 segundos. ¿Cuántos segundos son?", "60+30", "Se suman los segundos del minuto y los 30 adicionales.", " s"),
        ("abc", "{F} ¿Está P4 = 90 s dentro del rango?", "No: supera el máximo de 60 s", "Sí: 90 es mayor que el mínimo de 0", "Sí: es mayor que el valor actual", "El máximo de P4 es 60 s y 90 s lo supera."),
        ("abc", "{F} ¿Cuántos de los cuatro valores pedidos están dentro de su rango?", "Dos: P2 y P3", "Uno: solo P2", "Tres: P1, P2 y P3", "P2 = 90 % y P3 = 25 min están en rango; P1 y P4 no."),
        ("abc", "{F} ¿Qué documentos faltan en la solicitud?", "El motivo escrito, la firma del jefe de planta y el respaldo del programa actual", "Solo la firma del jefe de planta", "El plano de la planta", "La ficha anota esos tres faltantes."),
        ("abc", "{F} El operador dice que, como dos valores están bien, se pueden hacer esos dos cambios ya. ¿Qué corresponde?", "No: la solicitud completa debe cumplir los documentos y ser aprobada antes de cambiar algo", "Sí: lo que está en rango se puede cambiar de inmediato", "Sí, si avisa al jefe después", "Sin firma, motivo y respaldo no hay cambio, aunque algunos valores sean válidos."),
        ("ab", "{F} Un revisor escribe 50 % en lugar de 55 % para P1 «para ayudar a que entre en rango». ¿Qué corresponde?", "No: no se cambian los valores del solicitante; se informa que 55 % está fuera de rango", "Sí: así la solicitud queda correcta", "El revisor evalúa y devuelve; el solicitante decide si presenta un nuevo valor."),
        ("=", "{F} Si P3 pasa de 20 a 25 minutos, ¿cuántos minutos queda por debajo del máximo de 30?", "30-25", "Se resta el nuevo valor al máximo del rango.", " minutos"),
        ("abc", "{F} ¿Qué respuesta final debe recibir el solicitante?", "Una lista con los valores fuera de rango (P1 y P4) y los documentos faltantes, para presentar una solicitud corregida", "Un «aprobado» parcial para P2 y P3", "Un «rechazado» sin explicación", "La respuesta debe ser clara y permitir corregir la solicitud."),
    ],
    ctx=("abc", "{F} El jefe de planta de ejemplo pide aprobar la solicitud «porque el operador tiene mucha experiencia». ¿Qué corresponde?", "Recordar que los valores fuera de rango y los documentos faltantes impiden aprobarla, sin importar la experiencia", "Aprobarla, porque el jefe decide", "Aprobarla y corregir los valores después", "La experiencia no reemplaza el rango del fabricante ni los documentos exigidos."),
    sc=[
        ("En Electricidad: ¿qué se revisa en una solicitud de cambio?", "Los valores pedidos y los documentos que la acompañan", "Valores y documentos deben estar en orden para aprobar."),
        ("¿Qué se hace con un valor fuera de rango?", "Se informa y no se acepta", "El revisor no lo corrige por su cuenta."),
        ("¿Quién hace el cambio si se aprueba?", "Personal autorizado, con norma vigente", "Quien evalúa no toca el equipo."),
    ],
    op=("Solicitud de ejemplo para el equipo de «Aguas Sur»: R1 (arranque) de 25 % a 35 %, rango 10 % a 40 %; R2 (parada) de 85 % a 98 %, rango 60 % a 95 %; R3 (tiempo continuo) de 15 min a 0,5 horas, rango 5 a 25 min; R4 (retardo) de 5 s a 20 s, rango 0 a 30 s. La solicitud tiene motivo y firma, pero no respaldo. Escribe (a) cuáles valores están en rango, (b) la conversión de R3, (c) qué documento falta, (d) qué respuesta das al solicitante.",
        "(a) R1 = 35 % y R4 = 20 s están en rango; R2 = 98 % supera 95 %; R3 supera el máximo. (b) 0,5 horas son 30 minutos, mayor que el máximo de 25 minutos. (c) Falta el respaldo del programa actual. (d) Una lista con R2 y R3 fuera de rango y el respaldo faltante, para presentar una solicitud corregida.",
        ["revisa cada valor", "convierte la unidad", "identifica el documento faltante", "redacta la respuesta"],
        ["hoja con la evaluación y la respuesta"],
        ["no convertir R3", "aprobar con faltantes", "corregir los valores"],
        "Pregunta: «¿puedes aprobar R1 y R4 solos?». Si no responde, pídele que relea qué se revisa en una solicitud."),
    reinforce="Escribe una lista de revisión de cinco puntos para evaluar una solicitud de cambio de parámetros.",
    extend="Explica con un ejemplo por qué una experiencia larga no reemplaza el rango que fija el fabricante.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (regla de control de ejemplo, inventada). Una bomba llena un estanque. Regla actual: la bomba arranca cuando el nivel baja de 30 % y se detiene cuando sube a 80 %. "
     "Con la bomba funcionando, el nivel sube 5 puntos porcentuales por minuto (neto); con la bomba detenida, el consumo hace bajar el nivel 1 punto porcentual por minuto. "
     "Criterio de ejemplo para proteger la bomba: no más de 30 arranques por día. Un día tiene 1440 minutos.")
build(
    O8, 4, F,
    use="Aprenderé a analizar en papel una regla de control y el efecto de cambiar sus parámetros, para decidir si el cambio propuesto es aceptable.",
    prior=["Sé leer una tabla de parámetros.", "Sé calcular tiempos con una razón de cambio.", "Sé qué es una solicitud de cambio."],
    explain=[
        "Una regla de control describe cuándo el equipo actúa: por ejemplo, arrancar al bajar de un nivel y detenerse al subir a otro. Para analizar una regla en papel se calcula cuánto dura cada fase: el tiempo de funcionamiento es la diferencia de nivel dividida por lo que sube por minuto, y el tiempo detenido es la diferencia de nivel dividida por lo que baja por minuto. La suma de ambos es un ciclo. Los arranques por día son los minutos del día divididos por la duración del ciclo.",
        "Arrancar y detenerse muchas veces desgasta y recalienta el equipo, por eso el fabricante o el proyecto fijan un máximo de arranques por día. Si un cambio propuesto hace pasar ese máximo, no se aprueba. El análisis en papel ayuda a decidir, pero el cambio real solo lo hace personal autorizado, con solicitud, respaldo, registro y la norma vigente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("regla de control", "descripción de cuándo y bajo qué condiciones actúa el equipo"), ("ciclo", "una fase de funcionamiento más una fase detenida"), ("arranque", "momento en que el equipo pasa de detenido a funcionando"), ("razón de cambio", "cuánto sube o baja una magnitud por unidad de tiempo")],
    worked=[
        ("Tiempo de una fase", "En una regla de ejemplo el nivel debe subir 40 puntos y sube 4 puntos por minuto. ¿Cuántos minutos dura?", ["Se divide la diferencia por lo que sube por minuto.", "40 dividido por 4 son 10."], "10 minutos"),
        ("Arranques por día", "Un ciclo de ejemplo dura 120 minutos. ¿Cuántos arranques hay en un día de 1440 minutos?", ["Se divide el día por la duración del ciclo.", "1440 dividido por 120 son 12."], "12 arranques"),
    ],
    mistakes=[("Subir el nivel de arranque sin calcular cuántos arranques por día produce.", "Un ciclo más corto produce muchos más arranques.", "Calcula el ciclo y los arranques antes de pedir el cambio."),
              ("Suponer que «más tiempo funcionando» siempre es mejor.", "Hay un máximo de tiempo continuo en la tabla.", "Compara el tiempo con el máximo de la tabla.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un ciclo en una regla de control de una bomba?", "Una fase de funcionamiento más una fase detenida", "Solo el tiempo en que la bomba funciona", "El cambio de un parámetro en la bitácora", "El ciclo suma la fase en marcha y la fase detenida."),
        ("abc", "En Electricidad: ¿por qué se limita el número de arranques por día de una bomba?", "Porque arrancar muchas veces desgasta y recalienta el equipo", "Porque la bomba gasta menos si arranca menos veces siempre", "Porque la bomba no puede funcionar más de una hora por día", "El desgaste y el calentamiento por arranques repetidos justifican el máximo."),
        ("=", "En una regla de ejemplo el nivel debe subir 60 puntos y sube 3 puntos por minuto. ¿Cuántos minutos dura la fase?", "60//3", "Se divide la diferencia de nivel por lo que sube cada minuto.", " minutos"),
        ("=", "{F} ¿Cuántos minutos funciona la bomba en cada fase de llenado, de 30 % a 80 %?", "(80-30)//5", "Se divide la diferencia de nivel por lo que sube cada minuto.", " minutos"),
        ("=", "{F} ¿Cuántos minutos queda detenida la bomba mientras el nivel baja de 80 % a 30 %?", "(80-30)//1", "Se divide la diferencia de nivel por lo que baja cada minuto.", " minutos"),
        ("=", "{F} ¿Cuántos minutos dura un ciclo completo con la regla actual?", "(80-30)//5+(80-30)//1", "Se suman la fase de llenado y la fase detenida.", " minutos"),
        ("=", "{F} ¿Cuántos arranques por día produce la regla actual?", "1440//((80-30)//5+(80-30)//1)", "Se divide el día por la duración del ciclo.", " arranques"),
        ("abc", "{F} ¿Cumple la regla actual el criterio de no más de 30 arranques por día?", "Sí: produce 24 arranques, menos que 30", "No: produce 48 arranques", "No: el criterio exige más de 30 arranques", "Con ciclos de 60 minutos hay 24 arranques por día, bajo el máximo."),
        ("=", "{F} Un operador propone arrancar a 70 % en lugar de 30 %. ¿Cuántos minutos dura la fase de llenado de 70 % a 80 %?", "(80-70)//5", "Se divide la diferencia de nivel por lo que sube cada minuto.", " minutos"),
        ("=", "{F} Con el arranque a 70 %, ¿cuántos minutos dura el ciclo completo (llenado más fase detenida de 80 % a 70 %)?", "(80-70)//5+(80-70)//1", "Se suman la fase de llenado y la fase detenida.", " minutos"),
        ("abc", "{F} Con el arranque a 70 %, ¿cuántos arranques por día habría y qué se concluye?", "120 arranques; supera el máximo de 30 y el cambio no se aprueba", "12 arranques; cumple el máximo", "48 arranques; cumple el máximo de 50", "Un ciclo de 12 minutos da 120 arranques por día, muy por encima de 30."),
        ("ab", "{F} Un compañero dice que arrancar a 70 % es mejor porque «la bomba funciona menos minutos cada vez». ¿Qué corresponde?", "Mostrar que produce 120 arranques por día, muy por encima del máximo", "Aceptarlo: funcionar menos minutos siempre cuida la bomba", "Menos minutos por fase no compensa el aumento de arranques que desgasta el equipo."),
        ("=", "{F} Si el operador propusiera arrancar a 10 %, ¿cuántos minutos duraría el ciclo (llenado de 10 % a 80 % más fase detenida)?", "(80-10)//5+(80-10)//1", "Se suman la fase de llenado y la fase detenida.", " minutos"),
    ],
    ctx=("abc", "{F} El jefe de planta de ejemplo pregunta si puede aprobar el cambio a 70 %. ¿Qué respuesta del analista es correcta?", "No: el análisis en papel muestra 120 arranques por día, sobre el máximo de 30; se recomienda mantener la regla o estudiar otra", "Sí: la bomba trabaja menos tiempo por fase", "Sí: el criterio de 30 arranques es solo una sugerencia", "El criterio de arranques por día es un límite del proyecto; el cambio propuesto lo supera por mucho."),
    sc=[
        ("En Electricidad: ¿cómo se calcula la duración de una fase de llenado?", "Dividiendo la diferencia de nivel por lo que sube por minuto", "Así se obtiene el tiempo en minutos."),
        ("¿Cómo se calculan los arranques por día?", "Dividiendo los minutos del día por la duración del ciclo", "Cada ciclo completo implica un arranque de la bomba."),
        ("¿Quién hace un cambio aprobado de parámetros?", "Personal autorizado, con respaldo, registro y norma vigente", "El análisis en papel no habilita para modificar equipos."),
    ],
    op=("Regla de ejemplo de otro estanque: la bomba arranca al bajar de 40 % y se detiene al subir a 90 %; con la bomba funcionando el nivel sube 5 puntos por minuto y con la bomba detenida baja 2 puntos por minuto; máximo de 30 arranques por día; un día tiene 1440 minutos. Se propone arrancar al bajar de 80 %. Escribe (a) la duración de un ciclo con la regla actual, (b) los arranques por día actuales, (c) la duración del ciclo con la propuesta, (d) los arranques por día con la propuesta y si se aprueba.",
        "(a) Llenado: 50 dividido por 5 son 10 minutos; detenida: 50 dividido por 2 son 25 minutos; ciclo de 35 minutos. (b) 1440 dividido por 35 son 41 arranques (parte entera), sobre el máximo de 30. (c) Con arranque a 80 %: llenado 10 dividido por 5 son 2 minutos; detenida 10 dividido por 2 son 5 minutos; ciclo de 7 minutos. (d) 1440 dividido por 7 son 205 arranques: no se aprueba. La regla actual tampoco cumple el máximo.",
        ["calcula las fases", "calcula el ciclo", "calcula los arranques", "concluye con el criterio"],
        ["hoja con la tabla de cálculos y la conclusión"],
        ["dividir mal el día", "no comparar con el máximo", "aprobar un cambio que empeora"],
        "Pregunta: «¿qué ocurre con los arranques si el ciclo es más corto?». Si no responde, pídele que relea cómo se calculan los arranques por día."),
    reinforce="Inventa una regla de control con dos niveles y dos razones de cambio, y calcula la duración de un ciclo.",
    extend="Explica con un ejemplo por qué un cambio que parece mejorar un dato puede empeorar otro.",
)

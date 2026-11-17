"""Electrónica TP 3.º y 4.º medio: OAE-07 (modificar programas y parámetros en control de procesos: solo conceptos, lectura de programas en seudocódigo y control de cambios en papel). Todo con datos de ejemplo."""
from __future__ import annotations

from tp_eltr_common import AVISO, EMER, build

O7 = "TP-ELTR-3y4-OAE-07"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (proceso de ejemplo, inventado). Una planta ficticia de agua tiene un estanque de 1000 litros y una bomba que lo llena, controlada por un controlador programable (equipo que ejecuta un programa para controlar un proceso). "
     "Un sensor entrega el nivel del estanque de 0 % a 100 %. Programa vigente: la bomba parte si el nivel baja de 20 % y se detiene al superar 80 %. La planta pide modificar el programa para que la bomba parta bajo 30 %. "
     "Documentos: solicitud de cambio, programa vigente, procedimiento de la planta y norma eléctrica vigente (SEC).")
build(
    O7, 1, F,
    use="Aprenderé qué es modificar un programa o un parámetro en el control de un proceso, qué riesgos tiene y por qué solo lo hace personal autorizado con respaldo y norma vigente.",
    prior=["Sé qué es un sensor y un actuador.", "Sé qué es una regla si-entonces.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El control de procesos es el uso de sensores, controladores y actuadores para mantener una magnitud, como el nivel de un estanque o una temperatura, dentro de lo deseado. El controlador programable es el equipo que ejecuta un programa: lee las entradas, aplica las reglas y ordena las salidas. Se modifica un programa o un parámetro cuando cambia un requerimiento operacional, es decir, una necesidad del proceso o de la planta.",
        "Un cambio mal hecho puede hacer que una bomba funcione sin agua, que un estanque se desborde o que una máquina se mueva cuando hay personas cerca. Por eso, antes de cambiar nada se guarda un respaldo: una copia del programa y de los parámetros, para poder volver atrás. El cambio lo hace personal autorizado, con permiso de la planta, cumpliendo la norma eléctrica vigente (SEC) y el procedimiento de la planta.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("control de procesos", "uso de sensores, controladores y actuadores para mantener una magnitud dentro de lo deseado"), ("controlador programable", "equipo que ejecuta un programa para controlar un proceso a partir de entradas y salidas"), ("requerimiento operacional", "necesidad del proceso o de la planta que justifica un cambio"), ("respaldo", "copia del programa y los parámetros guardada antes de cambiarlos"), ("modo automático", "modo en que el controlador decide por sí solo según el programa")],
    worked=[
        ("Elegir el documento", "Un técnico de ejemplo quiere saber cómo está programado hoy el sistema. ¿Qué documento consulta?", ["Se necesita el programa que está en uso.", "Ese documento es el programa vigente."], "El programa vigente"),
        ("Volumen entre dos niveles", "Un estanque de ejemplo de 500 litros cambia de 10 % a 60 %. ¿Cuántos litros entran?", ["La diferencia es 60 menos 10, es decir, 50 puntos porcentuales.", "El 50 % de 500 son 250."], "250 litros"),
    ],
    mistakes=[("Cambiar un parámetro directamente en el controlador en funcionamiento, sin respaldo ni permiso.", "Si algo falla, no se puede volver atrás y el cambio no tiene autorización.", "Guarda el respaldo y exige permiso, norma vigente y personal autorizado."),
              ("Pensar que un cambio pequeño no necesita registro.", "Aun un cambio pequeño puede cambiar el comportamiento del proceso.", "Registra todo cambio, sin importar su tamaño.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un controlador programable?", "Un equipo que ejecuta un programa para controlar un proceso a partir de sus entradas y salidas", "Un sensor que mide el nivel de un estanque", "Un cable que une la bomba con la fuente", "El controlador ejecuta el programa; el sensor solo mide y el cable solo une."),
        ("abc", "En Electrónica: ¿qué es un requerimiento operacional?", "Una necesidad del proceso o de la planta que justifica cambiar un programa o un parámetro", "Un permiso para entrar a la planta", "El precio del controlador programable", "El requerimiento operacional es la razón de negocio o de proceso para hacer un cambio."),
        ("abc", "En Electrónica: ¿qué es el respaldo de un programa?", "Una copia del programa y sus parámetros, guardada para poder volver atrás", "Un segundo controlador conectado a la red", "Un manual impreso del fabricante", "El respaldo conserva la configuración anterior antes de modificarla."),
        ("abc", "{F} ¿Qué documento de la ficha dice cómo está programado el sistema hoy?", "El programa vigente", "La solicitud de cambio", "La norma eléctrica vigente", "El programa vigente describe lo que el controlador ejecuta ahora."),
        ("abc", "{F} ¿Qué cambio se pide en la ficha?", "Que la bomba parta cuando el nivel baje de 30 % y no de 20 %", "Que la bomba se detenga al superar 20 %", "Que el estanque tenga 3000 litros", "La solicitud modifica el nivel de partida, que hoy es 20 %."),
        ("abc", "{F} ¿Qué riesgo puede tener un cambio mal hecho en este sistema?", "Que la bomba funcione sin agua o que el estanque se desborde", "Que cambie la tensión de la red eléctrica de la planta", "Ninguno, porque son valores pequeños", "Un nivel mal programado puede hacer trabajar la bomba en vacío o rebasar el estanque."),
        ("=", "{F} ¿Cuántos litros hay entre los niveles de 20 % y 80 % del estanque?", "1000*(80-20)//100", "Se toma el porcentaje de diferencia sobre los 1000 litros.", " litros"),
        ("=", "{F} Con el cambio pedido, la bomba parte bajo 30 % y se detiene sobre 80 %. ¿Cuántos litros hay entre esos dos niveles?", "1000*(80-30)//100", "Se toma el porcentaje de diferencia sobre los 1000 litros.", " litros"),
        ("abc", "{F} ¿Quién debe hacer el cambio en el controlador de la planta?", "Personal autorizado, con permiso de la planta, respaldo y norma vigente", "Cualquier estudiante que conozca el programa", "Un operador de turno, sin respaldo ni permiso", "Es una tarea de riesgo reservada a personal autorizado."),
        ("ab", "Una estudiante terminó este cuaderno y quiere modificar el programa del controlador de una planta real. ¿Qué corresponde?", "No hacerlo: exige personal autorizado, permiso, respaldo y norma vigente, y el cuaderno no habilita", "Hacerlo con cuidado, porque ya entiende qué es un parámetro", "Modificar un controlador real puede producir daños y accidentes; entender conceptos no habilita."),
        ("abc", "{F} Un compañero propone hacer el cambio directamente en el controlador, sin respaldo. ¿Qué problema tiene?", "Si algo falla no se podrá volver a la configuración anterior", "Ninguno, porque el cambio es pequeño", "El estanque se llenará más rápido", "Sin respaldo no hay forma de recuperar la configuración que funcionaba."),
        ("=", "{F} La bomba de ejemplo llena 100 litros por minuto. ¿Cuántos minutos tarda en subir el nivel de 20 % a 80 %?", "1000*(80-20)//100//100", "Se calculan los litros entre los dos niveles y se dividen por el caudal.", " minutos"),
        ("abc", "En el tablero de control de una planta se ven chispas y se siente olor a quemado. ¿Qué corresponde de forma general?", "Alejarse, avisar al responsable de la planta y a emergencias, y cortar el suministro solo si se está autorizado", "Acercarse a mirar de qué tablero se trata", "Echarle agua para enfriarlo", "El humo o las chispas en un tablero son riesgo eléctrico; se aleja a las personas y se avisa."),
    ],
    ctx=("abc", "El jefe de turno de una planta de ejemplo dice: «cambia tú el programa ahora, es solo un número y hay apuro». Como estudiante, ¿qué respondes?", "Que el cambio lo hace personal autorizado con respaldo y registro, aun con apuro", "Que lo harás rápido para ganar tiempo", "Que lo harás sin respaldo porque es solo un número", "El apuro no elimina los requisitos de seguridad ni el control de cambios."),
    sc=[
        ("En Electrónica: ¿qué hace un controlador programable?", "Ejecuta un programa que lee entradas y ordena salidas", "Es el equipo que aplica las reglas del proceso."),
        ("¿Qué se guarda antes de modificar un programa?", "Un respaldo del programa y sus parámetros", "Permite volver atrás si el cambio falla."),
        ("¿Quién modifica el programa de una planta real?", "Personal autorizado, con norma vigente (SEC)", "Este cuaderno no habilita para trabajar."),
    ],
    op=("Ficha de ejemplo: un estanque de 2000 litros se llena con una bomba controlada por un controlador programable. Programa vigente: la bomba parte bajo 25 % y se detiene sobre 75 %. La planta pide que parta bajo 35 %. Escribe (a) cuántos litros hay entre 25 % y 75 %, (b) cuántos litros habrá entre 35 % y 75 % con el cambio, (c) qué guardarías antes del cambio, (d) quién haría el cambio.",
        "(a) 2000 por 50 ÷ 100 son 1000 litros. (b) 2000 por 40 ÷ 100 son 800 litros. (c) Un respaldo del programa y de los parámetros. (d) Personal autorizado con permiso de la planta y norma vigente.",
        ["calcula bien los litros de cada caso", "nombra el respaldo", "dice quién hace el cambio"],
        ["hoja con los cálculos y las respuestas"],
        ["no usar los 2000 litros del estanque", "olvidar el respaldo", "decir que él haría el cambio"],
        "Pregunta: «¿qué pasaría si el cambio sale mal y no hay respaldo?». Si no responde, pídele que relea la parte del respaldo."),
    reinforce="Escribe tres riesgos de un cambio mal hecho en un sistema de bomba y estanque, y una forma conceptual de reducir cada uno.",
    extend="Explica con un ejemplo por qué el apuro es un factor de riesgo al modificar un programa.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (tabla de parámetros de ejemplo, inventada) de la bomba del estanque. P1, nivel de partida: 20 % (rango admitido: 10 % a 40 %); P2, nivel de parada: 80 % (rango: 60 % a 95 %); "
     "P3, retardo de partida: 5 s (rango: 0 s a 30 s); P4, nivel de alarma por nivel alto: 90 % (rango: 85 % a 100 %). Estanque de 1000 litros. La variable de proceso es el nivel del estanque.")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario del control de procesos: variable de proceso, consigna, parámetro, alarma y límite, y a leer una tabla de parámetros con sus rangos.",
    prior=["Sé qué es un parámetro y un rango.", "Sé qué es un sensor.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La variable de proceso es la magnitud que se mide y se controla, como el nivel de un estanque o la temperatura de una sala. La consigna, también llamada valor deseado, es el valor al que se quiere llevar la variable. Un parámetro es un valor ajustable del programa, como el nivel de partida de una bomba o un tiempo de espera. Cada parámetro tiene un rango admitido: fuera de él, el equipo o el proceso pueden fallar.",
        "Una alarma es un aviso que se activa cuando la variable sale de los límites permitidos. El retardo es un tiempo de espera antes de ejecutar una acción. La tabla de parámetros lista cada parámetro con su valor actual y su rango. Antes de proponer un cambio se comprueba que el valor nuevo esté dentro del rango y que tenga sentido con los demás parámetros: por ejemplo, la alarma de nivel alto no debe estar por debajo del nivel de parada.",
        f"Los parámetros de este cuaderno son solo de ejemplo. {AVISO}",
    ],
    vocab=[("variable de proceso", "magnitud que se mide y se controla, como el nivel de un estanque"), ("consigna", "valor deseado al que se quiere llevar la variable"), ("parámetro", "valor ajustable del programa"), ("alarma", "aviso que se activa cuando la variable sale de los límites permitidos"), ("retardo", "tiempo de espera antes de ejecutar una acción"), ("rango admitido", "intervalo de valores que se puede ajustar de un parámetro")],
    worked=[
        ("Reconocer la variable", "Una sala de ejemplo se mantiene a 22 °C con un termostato. ¿Cuál es la variable de proceso y cuál la consigna?", ["Se mide la temperatura de la sala.", "El valor deseado es 22 °C."], "Variable: la temperatura; consigna: 22 °C"),
        ("Comprobar un rango", "Un parámetro de ejemplo admite de 10 % a 40 %. ¿Se puede ajustar a 35 %?", ["35 es mayor que 10 y menor que 40.", "Está dentro del rango."], "Sí, está dentro del rango"),
    ],
    mistakes=[("Fijar una alarma de nivel alto por debajo del nivel de parada normal.", "La alarma sonaría durante el funcionamiento normal.", "Comprueba que la alarma esté por encima del nivel de parada."),
              ("Usar el mismo valor para el nivel de partida y el de parada.", "El equipo se encendería y apagaría sin parar.", "Deja una diferencia suficiente entre ambos niveles.")],
    T=[
        ("abc", "En Electrónica: ¿qué es la variable de proceso?", "La magnitud que se mide y se controla, como el nivel de un estanque", "El valor del precio de la energía", "El nombre del programa del controlador", "La variable de proceso es lo que el sistema mide y trata de mantener."),
        ("abc", "En Electrónica: ¿qué es la consigna?", "El valor deseado al que se quiere llevar la variable", "El valor máximo que el sensor puede medir", "El nombre del operador de turno", "La consigna es el objetivo que el controlador persigue."),
        ("abc", "En Electrónica: ¿qué es una alarma en un sistema de control?", "Un aviso que se activa cuando la variable sale de los límites permitidos", "El apagado manual de la bomba", "Una copia del programa", "La alarma advierte que la variable se salió de lo normal."),
        ("abc", "{F} ¿Cuál es la variable de proceso en la ficha?", "El nivel del estanque", "El retardo de partida", "El rango de P1", "El sistema mide y controla el nivel del estanque."),
        ("abc", "{F} ¿Qué significa P3, el retardo de partida de 5 s?", "Un tiempo de espera de 5 segundos antes de que parta la bomba", "El nivel en que la bomba para", "La cantidad de agua que bombea por minuto", "El retardo es una espera antes de ejecutar una acción."),
        ("=", "{F} ¿Cuántos puntos porcentuales hay entre el nivel de parada y el de alarma?", "90-80", "Se resta el nivel de parada al nivel de alarma.", " puntos"),
        ("abc", "{F} Se propone ajustar P1 a 35 %. ¿Está dentro del rango admitido?", "Sí, porque 35 % está entre 10 % y 40 %", "No, porque es mayor que el valor actual", "No, porque el rango solo admite 20 %", "El rango admitido de P1 va de 10 % a 40 %."),
        ("abc", "{F} Se propone ajustar P2 a 98 %. ¿Está dentro del rango admitido?", "No, porque supera el máximo de 95 %", "Sí, porque 98 % es menor que 100 %", "Sí, porque P2 no tiene rango", "El rango de P2 llega hasta 95 %."),
        ("=", "{F} ¿Cuántos litros hay en el estanque cuando el nivel llega a la alarma de 90 %?", "1000*90//100", "Se toma el 90 % de los 1000 litros.", " litros"),
        ("abc", "{F} Si, ignorando su rango, P4 se fijara en 70 %, ¿qué problema habría?", "La alarma sonaría en el funcionamiento normal, porque la bomba para recién a los 80 %", "La bomba no arrancaría nunca", "El estanque se vaciaría", "Una alarma por debajo del nivel de parada se activaría siempre que se llene normalmente."),
        ("abc", "{F} Un técnico dice que P1 y P2 «son lo mismo». ¿Qué diferencia hay?", "P1 fija cuándo parte la bomba y P2 cuándo se detiene", "P1 es el retardo y P2 la alarma", "No hay ninguna diferencia, solo cambia el nombre", "El nivel de partida y el de parada tienen funciones distintas en el ciclo de llenado."),
        ("=", "Un registro de ejemplo muestra los niveles 25 %, 30 %, 38 % y 46 % en cuatro lecturas seguidas del estanque de 1000 litros. ¿Cuántos litros entraron entre la primera y la última lectura?", "1000*(46-25)//100", "Se resta el primer nivel al último y se toma ese porcentaje de los 1000 litros.", " litros"),
        ("abc", "{F} ¿Por qué cada parámetro tiene un rango admitido?", "Para evitar valores que dañen el equipo o pongan en riesgo el proceso", "Para que el programa tenga más líneas", "Porque el rango reemplaza al programa", "Los límites impiden configuraciones peligrosas o dañinas."),
    ],
    ctx=("abc", "Un operador de ejemplo dice: «sube la alarma al 100 % para que no suene tanto». El rango de P4 es de 85 % a 100 % y el estanque se desborda poco después de 100 %. ¿Qué respondes?", "Que 100 % está dentro del rango pero deja sin margen ante el desborde, por lo que debe evaluarlo quien autoriza el cambio", "Que se hace de inmediato, porque está dentro del rango", "Que se quita la alarma por completo", "Estar dentro del rango no basta: el cambio reduce el margen de seguridad y requiere evaluación."),
    sc=[
        ("En Electrónica: ¿qué es un parámetro?", "Un valor ajustable del programa", "Por ejemplo, un nivel de partida o un retardo."),
        ("¿Qué indica el rango admitido de un parámetro?", "Entre qué valores se puede ajustar", "Fuera del rango el equipo puede fallar."),
        ("¿Dónde debe estar la alarma de nivel alto respecto de la parada?", "Por encima del nivel de parada", "Así no suena en funcionamiento normal."),
    ],
    op=("Ficha de ejemplo: horno eléctrico de laboratorio (ficticio). Parámetros: T1, temperatura de encendido, 150 °C (rango 100 a 250); T2, temperatura de apagado, 180 °C (rango 150 a 300); T3, alarma de temperatura alta, 200 °C (rango 190 a 320). Escribe (a) cuál es la variable de proceso, (b) si T1 = 120 °C está en rango, (c) qué problema daría T3 = 170 °C, (d) cuántos grados hay entre T2 y T3.",
        "(a) La temperatura del horno. (b) Sí, 120 °C está entre 100 °C y 250 °C. (c) T3 = 170 °C está fuera del rango (190 a 320) y además quedaría bajo la temperatura de apagado de 180 °C, por lo que la alarma sonaría en el funcionamiento normal. (d) 200 menos 180 son 20 grados.",
        ["identifica la variable de proceso", "comprueba el rango", "explica el problema de la alarma", "calcula bien la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["no comprobar el rango", "poner la alarma bajo el apagado", "restar al revés"],
        "Pregunta: «¿qué margen de seguridad deja la alarma de T3 = 200 °C?». Si no responde, pídele que relea cómo se relaciona la alarma con el nivel de parada."),
    reinforce="Escribe una tabla de cuatro parámetros de un sistema de ejemplo con su valor actual y su rango admitido.",
    extend="Explica con un ejemplo por qué dos parámetros pueden estar en rango por separado y aun así ser incompatibles entre sí.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (programa de ejemplo en seudocódigo, inventado). Regla 1: si NIVEL < 20, entonces BOMBA = 1. Regla 2: si NIVEL > 80, entonces BOMBA = 0. "
     "Regla 3: si NIVEL está entre 20 y 80, incluidos ambos, BOMBA mantiene el valor que tenía. Al inicio, BOMBA = 0. NIVEL es el nivel del estanque en porcentaje; BOMBA vale 1 si está encendida y 0 si está apagada.")
build(
    O7, 3, F,
    use="Aprenderé a leer un programa de control escrito en seudocódigo, a seguirlo lectura por lectura y a prever qué haría un cambio propuesto, siempre en papel.",
    prior=["Sé qué es una regla si-entonces.", "Sé comparar valores con menor y mayor que.", "Sé qué es un parámetro."],
    explain=[
        "El seudocódigo es la descripción de un programa en lenguaje cotidiano y ordenado, sin la sintaxis de un lenguaje real. Sirve para razonar el programa antes de modificarlo. Una variable de salida es un valor que el programa entrega al actuador, como BOMBA. Seguir un programa «a mano» es tomar cada lectura en orden, revisar las reglas y anotar el valor de las salidas.",
        "Cuando ninguna regla cambia una salida, esta mantiene su valor anterior: es la memoria del programa. Una condición como «NIVEL < 20» se cumple solo con valores menores que 20; el valor 20 exacto no la cumple. Si dos reglas pueden contradecirse con una misma lectura, el programa tiene un error y no debe aprobarse.",
        f"Todo se practica con valores de ejemplo y en papel; las modificaciones en equipos reales las hace personal autorizado. {AVISO}",
    ],
    vocab=[("seudocódigo", "descripción de un programa en lenguaje cotidiano y ordenado"), ("variable de salida", "valor que el programa entrega a un actuador"), ("mantener el valor", "seguir como estaba hasta que una regla lo cambie"), ("condición", "comparación que puede cumplirse o no"), ("contradicción", "dos reglas que ordenan cosas opuestas ante una misma lectura")],
    worked=[
        ("Seguir una lectura", "Programa de ejemplo: si T < 5, entonces ALARMA = 1; si T > 10, entonces ALARMA = 0; entre 5 y 10, mantiene. ALARMA era 0 y T marca 3. ¿Cuánto vale ALARMA?", ["3 es menor que 5.", "Se cumple la primera regla."], "ALARMA = 1"),
        ("Valor que se mantiene", "Con el mismo programa, ALARMA vale 1 y T marca 7. ¿Cuánto vale ALARMA?", ["7 está entre 5 y 10.", "Ninguna regla la cambia, así que mantiene su valor."], "ALARMA = 1"),
    ],
    mistakes=[("Pensar que NIVEL = 20 cumple la condición NIVEL < 20.", "20 no es menor que 20.", "Lee el signo de la condición con exactitud."),
              ("Olvidar el valor anterior cuando ninguna regla actúa.", "La salida mantiene el valor que tenía.", "Anota siempre el valor de la salida tras cada lectura.")],
    T=[
        ("abc", "En Electrónica: ¿qué es el seudocódigo?", "La descripción de un programa en lenguaje cotidiano y ordenado", "Un lenguaje que solo entiende el controlador", "El esquema eléctrico de una bomba", "El seudocódigo describe la lógica sin la sintaxis de un lenguaje real."),
        ("abc", "En Electrónica: ¿qué significa que la salida «mantiene su valor»?", "Que sigue como estaba hasta que una regla la cambie", "Que vuelve a cero en cada lectura", "Que se apaga por seguridad", "Sin una regla que actúe, la salida conserva su valor previo."),
        ("abc", "En Electrónica: ¿qué es una variable de salida?", "El valor que el programa entrega a un actuador, como BOMBA", "La lectura que entrega el sensor", "El tiempo que dura el programa", "La salida es lo que el programa ordena al actuador."),
        ("abc", "{F} NIVEL = 15 y BOMBA = 0. ¿Cuánto vale BOMBA después de la lectura?", "1, porque 15 es menor que 20", "0, porque la bomba estaba apagada", "No cambia nunca", "La Regla 1 se cumple con 15 y ordena encender la bomba."),
        ("abc", "{F} NIVEL = 50 y BOMBA = 1, que venía llenando. ¿Cuánto vale BOMBA?", "1, porque 50 está entre 20 y 80 y mantiene su valor", "0, porque 50 es la mitad del estanque", "0, porque ya está lleno", "Entre 20 y 80 la Regla 3 mantiene el valor anterior."),
        ("abc", "{F} NIVEL = 85 y BOMBA = 1. ¿Cuánto vale BOMBA?", "0, porque 85 es mayor que 80", "1, porque venía encendida", "1, porque 85 está cerca de 80", "La Regla 2 apaga la bomba cuando el nivel supera 80."),
        ("abc", "{F} NIVEL = 20 exacto y BOMBA = 0. ¿Cuánto vale BOMBA?", "0, porque 20 no es menor que 20 y se mantiene", "1, porque 20 cumple la Regla 1", "No se puede saber con ese valor", "La Regla 1 exige menor que 20; con 20 exacto rige la Regla 3."),
        ("abc", "{F} NIVEL = 80 exacto y BOMBA = 1. ¿Cuánto vale BOMBA?", "1, porque 80 no es mayor que 80 y se mantiene", "0, porque 80 cumple la Regla 2", "0, porque 80 es el máximo", "La Regla 2 exige mayor que 80; con 80 exacto rige la Regla 3."),
        ("abc", "{F} BOMBA = 0 al inicio y las lecturas llegan en este orden: 50, 30, 15, 40. ¿Cuánto vale BOMBA tras la última?", "1, porque se encendió con 15 y 40 mantiene el valor", "0, porque 40 está entre 20 y 80", "Con esos datos no se puede saber", "15 enciende la bomba y 40 no cambia nada, así que queda en 1."),
        ("abc", "{F} Se cambia la Regla 1 a «si NIVEL < 30». Con BOMBA = 0 y una lectura de 25, ¿qué cambia respecto del programa original?", "Ahora la bomba se enciende; antes se mantenía en 0", "Nada cambia, porque 25 sigue entre 20 y 80", "La bomba se apaga", "Con el nuevo valor, 25 es menor que 30 y cumple la Regla 1."),
        ("abc", "{F} Por un error se escribe la Regla 2 como «si NIVEL > 8». ¿Qué problema crea?", "Las Reglas 1 y 2 se contradicen con lecturas entre 9 y 19", "Ninguno, porque 8 es menor que 20", "La bomba nunca se apaga", "Una lectura de 15 cumple «menor que 20» y «mayor que 8» a la vez, con órdenes opuestas."),
        ("=", "{F} El estanque es de 1000 litros y la bomba llena 130 litros por minuto. ¿Cuántos minutos tarda en subir el nivel de 15 % a 80 %?", "1000*(80-15)//100//130", "Se calculan los litros entre los niveles y se dividen por el caudal.", " minutos"),
        ("abc", "{F} Las lecturas son 50, 30, 15, 40, 70, 85 y 60, con BOMBA = 0 al inicio. ¿En cuántas de esas lecturas queda la bomba encendida?", "En 3 lecturas: 15, 40 y 70", "En 7 lecturas, todas", "En 1 lectura, la de 15", "La bomba se enciende con 15, se mantiene con 40 y 70, y se apaga con 85."),
    ],
    ctx=("abc", "Un técnico autorizado de ejemplo recibe una solicitud para cambiar «NIVEL < 20» por «NIVEL < 30». Antes de aplicar, ¿qué hace en papel?", "Sigue lecturas de prueba por las reglas para ver qué cambia con 25, 30 y 35", "Aplica el cambio y espera a ver qué pasa", "Cambia todos los números del programa por si acaso", "Probar en papel anticipa el comportamiento sin riesgo antes de tocar el controlador."),
    sc=[
        ("En Electrónica: ¿cuándo se cumple «NIVEL < 20»?", "Solo con valores menores que 20", "El 20 exacto no cumple esa condición."),
        ("¿Qué pasa con una salida cuando ninguna regla actúa?", "Mantiene su valor anterior", "Esa es la memoria del programa."),
        ("¿Qué indica una contradicción entre dos reglas?", "Que el programa tiene un error y no debe aprobarse", "Con una misma lectura darían órdenes opuestas."),
    ],
    op=("Ficha de ejemplo: ventilador de un invernadero (ficticio). Regla 1: si T > 28, entonces VENT = 1. Regla 2: si T < 24, entonces VENT = 0. Regla 3: si T está entre 24 y 28, incluidos, VENT mantiene su valor. Al inicio VENT = 0. Lecturas en orden: 22, 26, 30, 27, 23. Escribe (a) el valor de VENT tras cada lectura, (b) cuántas veces cambia VENT de valor, (c) qué problema crearía cambiar la Regla 2 a «si T < 30».",
        "(a) 22: 0; 26: 0; 30: 1; 27: 1; 23: 0. (b) Cambia 2 veces: de 0 a 1 con 30 y de 1 a 0 con 23. (c) Las Reglas 1 y 2 se contradirían con T = 29, que es mayor que 28 y menor que 30 a la vez, y darían órdenes opuestas.",
        ["sigue bien las cinco lecturas", "cuenta bien los cambios", "detecta la contradicción"],
        ["hoja con la tabla de lecturas y las respuestas"],
        ["olvidar que mantiene su valor", "tratar el límite exacto como si cumpliera", "no ver la contradicción"],
        "Pregunta: «¿qué ocurriría con T = 28 exacto?». Si no responde, pídele que relea cuándo se cumple una condición «mayor que»."),
    reinforce="Inventa un programa de tres reglas para una luz con sensor de luz y sigue en papel cinco lecturas.",
    extend="Explica con un ejemplo por qué probar un cambio en papel ayuda a detectar errores antes de aplicarlo.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (solicitud de cambio de ejemplo, inventada). Solicitud S-12: cambiar P1, el nivel de partida de la bomba, de 20 % a 30 %, para dejar más reserva de agua; rango admitido de P1: 10 % a 40 %. "
     "Regla del programa tras el cambio: la bomba parte cuando NIVEL < P1. Evaluación de riesgo anotada: si P1 sube, la bomba arranca más veces por día. Plan de prueba de ejemplo: simular lecturas de 35, 28 y 31 con BOMBA = 0. "
     "Requisitos de la planta para cualquier cambio: respaldo previo, aprobación del supervisor, personal autorizado, registro del cambio y plan de vuelta atrás.")
build(
    O7, 4, F,
    use="Aprenderé a evaluar en papel una solicitud de cambio de un programa o parámetro: validar el rango, anticipar efectos, planear pruebas y revisar el control de cambios.",
    prior=["Sé qué es un parámetro y su rango.", "Sé seguir un programa en seudocódigo.", "Sé qué es un respaldo."],
    explain=[
        "Un control de cambios es el proceso por el cual cada cambio se solicita, se evalúa, se aprueba, se prueba y se registra. La solicitud de cambio dice qué se quiere cambiar, por qué, en qué rango se mueve y qué riesgos tiene. La evaluación comprueba que el valor nuevo esté dentro del rango y revisa los efectos en otras partes del proceso, como un mayor desgaste si el equipo arranca más veces.",
        "El plan de prueba define casos con lecturas y resultados esperados. Si el resultado obtenido no coincide con el esperado, el cambio no se aprueba y se vuelve a la configuración anterior mediante el plan de vuelta atrás, que es el plan escrito para restablecer el respaldo. Un cambio sin respaldo, sin aprobación o fuera de rango no se hace. El registro final guarda el valor anterior, el nuevo, la fecha, el motivo y quién lo aprobó.",
        f"Estas decisiones las toma el personal autorizado de la planta con la norma vigente. {AVISO}",
    ],
    vocab=[("control de cambios", "proceso de solicitar, evaluar, aprobar, probar y registrar cada cambio"), ("solicitud de cambio", "documento que pide un cambio con su motivo, rango y riesgos"), ("plan de prueba", "casos con lecturas y resultados esperados para verificar el cambio"), ("plan de vuelta atrás", "plan escrito para restablecer el respaldo si el cambio falla"), ("aprobación", "autorización escrita del supervisor para aplicar el cambio")],
    worked=[
        ("Validar el rango", "Un parámetro de ejemplo admite de 10 a 40. La solicitud pide 45. ¿Qué corresponde?", ["45 es mayor que 40.", "Está fuera del rango."], "Devolver la solicitud, porque el valor está fuera del rango"),
        ("Una prueba en papel", "Con la regla «la bomba parte si NIVEL < 25» y BOMBA = 0, ¿qué se espera con una lectura de 24?", ["24 es menor que 25.", "Se cumple la condición."], "BOMBA = 1"),
    ],
    mistakes=[("Aprobar un cambio solo porque está dentro del rango, sin evaluar sus efectos.", "Un valor en rango puede aumentar el desgaste o el riesgo.", "Evalúa el efecto en el proceso y anótalo en la solicitud."),
              ("Dar por buena una prueba cuando el resultado obtenido difiere del esperado.", "Una diferencia indica un error del cambio o del plan.", "Registra la no conformidad y vuelve a la configuración anterior.")],
    T=[
        ("abc", "En Electrónica: ¿qué es una solicitud de cambio?", "Un documento que pide un cambio con su motivo, rango y riesgos", "Un permiso para entrar a la planta", "Una copia del programa", "La solicitud de cambio describe qué se cambia y por qué."),
        ("abc", "En Electrónica: ¿qué es un plan de vuelta atrás?", "El plan escrito para restablecer la configuración respaldada si el cambio falla", "Un cartel que avisa del cambio", "Una nueva solicitud de cambio", "Si el cambio falla, el plan permite volver a la configuración que funcionaba."),
        ("abc", "En Electrónica: ¿qué es el control de cambios?", "El proceso de solicitar, evaluar, aprobar, probar y registrar cada cambio", "Un cambio de turno entre operadores", "Una lista de precios de repuestos", "El control de cambios ordena y deja trazabilidad de cada modificación."),
        ("abc", "{F} ¿Está P1 = 30 % dentro del rango admitido?", "Sí, porque 30 % está entre 10 % y 40 %", "No, porque es mayor que 20 %", "No, porque el rango empieza en 30 %", "El rango de P1 va de 10 % a 40 %."),
        ("=", "{F} ¿Cuántos puntos porcentuales sube P1 con el cambio?", "30-20", "Se resta el valor anterior al valor nuevo.", " puntos"),
        ("abc", "{F} ¿Qué consecuencia anota la evaluación de riesgo de la solicitud?", "La bomba arrancará más veces por día", "El estanque tendrá menos reserva de agua", "La bomba no arrancará nunca", "Al subir el nivel de partida la bomba parte más seguido."),
        ("abc", "{F} Con el cambio, la bomba parte cuando NIVEL < P1. Con BOMBA = 0 y una lectura de 28, ¿qué se espera?", "BOMBA = 1, porque 28 es menor que 30", "BOMBA = 0, porque 28 es menor que 35", "BOMBA = 0, porque 28 no es menor que 20", "Con P1 = 30, una lectura de 28 cumple la condición de partida."),
        ("abc", "{F} Con el cambio, BOMBA = 0 y una lectura de 31. ¿Qué se espera?", "BOMBA = 0, porque 31 no es menor que 30", "BOMBA = 1, porque 31 está cerca de 30", "BOMBA = 1, porque 31 es mayor que 20", "La condición exige menor que 30, y 31 no la cumple."),
        ("abc", "{F} Una solicitud S-13 pide P1 = 45 %. ¿Qué corresponde?", "Devolverla, porque 45 % está fuera del rango admitido de 10 % a 40 %", "Aprobarla, porque 45 % es un valor redondo", "Aprobarla si el supervisor está apurado", "Un valor fuera del rango no se aprueba."),
        ("abc", "{F} Una solicitud S-14 cumple el rango, pero no menciona el respaldo previo. ¿Qué corresponde?", "No aprobarla hasta que incluya el respaldo previo", "Aprobarla, porque cumple el rango", "Aprobarla y hacer el respaldo después", "El respaldo previo es un requisito de la planta para cualquier cambio."),
        ("abc", "{F} En la prueba con lectura 28 se esperaba BOMBA = 1, pero el resultado obtenido fue 0. ¿Qué corresponde?", "Registrar una no conformidad, volver a la configuración anterior y revisar el cambio", "Aprobar el cambio, porque las otras pruebas salieron bien", "Cambiar el resultado esperado a 0", "Una prueba fallida impide aprobar; el resultado esperado no se modifica para ajustarse."),
        ("=", "{F} Con P1 = 30 la bomba arranca 6 veces por día, en lugar de 4 veces con P1 = 20. ¿Cuántos arranques más hay en 30 días?", "(6-4)*30", "Se multiplica por 30 días la diferencia de arranques diarios.", " arranques"),
        ("abc", "{F} ¿Qué debe guardar el registro final del cambio?", "Valor anterior, valor nuevo, fecha, motivo y quién aprobó", "Solo el valor nuevo", "Solo el nombre de quien lo ejecutó", "El registro completo permite auditar el cambio y volver atrás."),
    ],
    ctx=("abc", "El jefe de turno de una planta de ejemplo dice: «aplica el cambio ahora y firmamos los papeles mañana». ¿Qué corresponde?", "Seguir el control de cambios completo antes de aplicar, aun con apuro", "Aplicarlo ahora y firmar después", "Aplicarlo ahora sin respaldo para ganar tiempo", "El respaldo, la aprobación y el plan de prueba se completan antes del cambio."),
    sc=[
        ("En Electrónica: ¿qué pasos tiene el control de cambios?", "Solicitar, evaluar, aprobar, probar y registrar", "Cada paso deja trazabilidad del cambio."),
        ("¿Qué se hace si una prueba falla?", "Se registra la no conformidad y se vuelve a la configuración anterior", "Una prueba fallida impide aprobar el cambio."),
        ("¿Basta con estar dentro del rango para aprobar un cambio?", "No, también se evalúan los efectos y se cumplen los requisitos", "Un valor en rango puede aumentar el desgaste o el riesgo."),
    ],
    op=("Ficha de ejemplo: solicitud S-20 para cambiar P2, el nivel de parada de una bomba, de 80 % a 90 %, para almacenar más agua. Rango admitido de P2: 60 % a 95 %. La alarma de nivel alto está en 92 %. La bomba se detiene cuando NIVEL > P2. Requisitos de la planta: respaldo, aprobación, personal autorizado, registro y plan de vuelta atrás. Escribe (a) si P2 = 90 % está en rango, (b) qué efecto tiene sobre el margen hasta la alarma, (c) qué espera la bomba con una lectura de 91 y BOMBA = 1, (d) qué datos anotarías en el registro final.",
        "(a) Sí, 90 % está entre 60 % y 95 %. (b) El margen hasta la alarma baja de 12 puntos (92 − 80) a 2 puntos (92 − 90), por lo que hay que evaluar el riesgo. (c) BOMBA = 0, porque 91 es mayor que 90. (d) Valor anterior, valor nuevo, fecha, motivo y quién aprobó.",
        ["comprueba el rango", "evalúa el efecto en el margen", "aplica la regla a la lectura", "lista datos del registro"],
        ["hoja con las cuatro respuestas"],
        ["aprobar solo por el rango", "calcular mal el margen", "olvidar el respaldo y la aprobación"],
        "Pregunta: «¿qué pasaría si falla la prueba?». Si no responde, pídele que relea el plan de vuelta atrás."),
    reinforce="Redacta una solicitud de cambio de ejemplo de tres líneas para un parámetro de un sistema de bomba, con motivo, rango y riesgo.",
    extend="Explica con un ejemplo por qué el control de cambios protege a las personas y a la planta.",
)

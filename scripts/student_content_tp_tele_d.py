"""Telecomunicaciones TP 3.º y 4.º medio: OAE-09 (fallas en circuitos de corriente continua: solo conceptos, lectura de valores y razonamiento en papel) y OAE-10 (determinar equipos y sistemas para una conectividad según los requerimientos)."""
from __future__ import annotations

from tp_tele_common import AVISO, build

O9 = "TP-TELE-3y4-OAE-09"
O10 = "TP-TELE-3y4-OAE-10"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (sitio de ejemplo, inventado). Una caseta de equipos del «Sitio Cerro Alto» (ficticio) funciona con corriente continua de 24 V (valor de ejemplo). Elementos: un rectificador (convierte la corriente alterna de la red en corriente continua), "
     "un banco de 2 baterías de 12 V conectadas en serie (sus voltajes se suman), un fusible de protección y un equipo de transmisión que consume 10 A (amperios, de ejemplo). "
     "Advertencia del sitio: solo personal autorizado interviene los tableros y las baterías.")
build(
    O9, 1, F,
    use="Aprenderé qué es la corriente continua, dónde aparece en telecomunicaciones, qué normas y riesgos hay y por qué solo personal autorizado interviene.",
    prior=["Sé qué es una batería.", "Sé qué es un riesgo eléctrico.", "Sé sumar y multiplicar."],
    explain=[
        "La corriente eléctrica es el movimiento de cargas por un circuito. En la corriente continua (CC) las cargas se mueven siempre en el mismo sentido, como la que entrega una batería; en la corriente alterna (CA) cambia de sentido muchas veces por segundo, como la de la red de un edificio. Muchos equipos de telecomunicaciones funcionan con corriente continua, alimentados por un rectificador, que convierte CA en CC, y respaldados por baterías.",
        "Un circuito tiene una fuente (que da la energía), una carga (el equipo que la consume), conductores (cables) y protecciones, como el fusible, que se corta si la corriente es excesiva. Dos baterías conectadas en serie suman sus voltajes: 12 V más 12 V dan 24 V. La tensión se mide en voltios (V), la corriente en amperios (A) y la resistencia en ohmios (Ω).",
        f"Que la tensión sea baja no significa que no haya riesgo: una batería puede entregar mucha corriente en un cortocircuito y causar calor intenso, quemaduras o incendio. Las instalaciones se rigen por la norma vigente, que fiscaliza, por ejemplo, la SEC. {AVISO} Aquí solo se razonan valores escritos.",
    ],
    vocab=[("corriente continua (CC)", "corriente cuyas cargas se mueven siempre en el mismo sentido"), ("corriente alterna (CA)", "corriente que cambia de sentido muchas veces por segundo"), ("rectificador", "equipo que convierte corriente alterna en continua"), ("fusible", "protección que se corta si la corriente es excesiva"), ("serie", "conexión en cadena donde los voltajes se suman"), ("cortocircuito", "unión directa que permite una corriente muy alta")],
    worked=[
        ("Baterías en serie", "Tres baterías de ejemplo de 12 V se conectan en serie. ¿Cuál es la tensión total?", ["En serie se suman los voltajes.", "12 más 12 más 12."], "36 V"),
        ("Para qué sirve el fusible", "Una corriente excesiva circula por un circuito de ejemplo. ¿Qué hace el fusible?", ["El fusible es una protección.", "Se corta y detiene la corriente."], "Se corta y protege el circuito"),
    ],
    mistakes=[("Pensar que una batería de baja tensión no puede causar daño.", "Un cortocircuito en una batería puede producir calor intenso y quemaduras.", "Trata toda fuente de energía con respeto y deja la intervención a personal autorizado."),
              ("Confundir corriente continua con corriente alterna.", "La continua va siempre en un sentido; la alterna cambia de sentido.", "Recuerda: batería, continua; red del edificio, alterna.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la corriente continua?", "Corriente cuyas cargas se mueven siempre en el mismo sentido", "Corriente que cambia de sentido muchas veces por segundo", "Corriente que no se mide", "La continua mantiene el mismo sentido, como la de una batería."),
        ("abc", "En Telecomunicaciones: ¿qué hace un rectificador?", "Convierte corriente alterna en continua", "Convierte voz en datos", "Mide la longitud de un cable", "El rectificador pasa de alterna a continua."),
        ("abc", "¿Qué protege un fusible?", "Corta el circuito si la corriente es excesiva", "Aumenta la tensión", "Guarda energía como una batería", "El fusible se corta ante una corriente excesiva."),
        ("=", "{F} ¿Cuál es la tensión total del banco de 2 baterías de 12 V en serie, en voltios?", "12+12", "En serie se suman los voltajes de las baterías.", " V"),
        ("abc", "{F} ¿Qué elemento de la caseta convierte la corriente de la red en continua?", "El rectificador", "El fusible", "El equipo de transmisión", "Según la ficha, el rectificador hace esa conversión."),
        ("abc", "{F} ¿Qué elemento es la carga del circuito?", "El equipo de transmisión", "El rectificador", "El fusible", "La carga es lo que consume la energía, aquí el equipo de transmisión."),
        ("=", "Cuatro baterías de ejemplo de 6 V se conectan en serie. ¿Cuál es la tensión total, en voltios?", "4*6", "En serie se suman los voltajes de las cuatro baterías.", " V"),
        ("abc", "{F} Un técnico novato propone abrir el banco de baterías «porque es solo 24 V». ¿Qué corresponde?", "No hacerlo: lo interviene solo personal autorizado, aunque la tensión sea baja", "Hacerlo con cuidado y sin avisar", "Pedir ayuda a un amigo", "Una batería puede causar daño aun con tensión baja."),
        ("abc", "¿Qué riesgo principal tiene un cortocircuito en una batería?", "Calor intenso, quemaduras o incendio", "Que baje el volumen de la voz", "Que cambie el nombre de la red", "La corriente muy alta calienta los conductores."),
        ("=", "Un equipo de ejemplo de 24 V consume 5 A. Si hay 3 equipos iguales en el mismo sitio, ¿cuántos amperios consumen entre todos?", "3*5", "Se multiplica el consumo de un equipo por la cantidad de equipos.", " A"),
        ("abc", "El encargado del sitio de ejemplo dice: «la tensión es baja, que el pasante cambie solo el fusible». ¿Qué corresponde responder?", "Que esa tarea la hace personal autorizado con norma vigente", "Que lo cambie rápido", "Que lo cambie de noche", "Las tareas en tableros energizados son para personal autorizado."),
        ("abc", "{F} ¿Qué mide el amperio?", "La corriente", "La resistencia", "La tensión", "El amperio es la unidad de corriente; el ohmio mide resistencia y el voltio tensión."),
        ("abc", "{F} Una compañera dice que el equipo de la caseta usa corriente alterna porque está enchufado a un rectificador. ¿Cuál es la aclaración correcta?", "El rectificador convierte la alterna de la red y el equipo usa corriente continua", "El equipo usa siempre alterna", "El rectificador no hace nada", "El equipo se alimenta con la corriente continua que sale del rectificador."),
    ],
    ctx=("abc", "Un joven de ejemplo ve en un video cómo alguien conecta cables a una batería grande y quiere imitarlo en la caseta de su barrio. ¿Qué corresponde?", "No hacerlo: se aprende con un instructor autorizado y la norma vigente", "Hacerlo con guantes de tela", "Hacerlo cuando no haya nadie", "Imitar videos con energía es peligroso; se aprende con instructor autorizado."),
    sc=[
        ("En Telecomunicaciones: ¿qué convierte un rectificador?", "La corriente alterna en continua", "Alimenta los equipos de corriente continua."),
        ("¿Qué pasa con la tensión de dos baterías en serie?", "Se suman", "12 V más 12 V dan 24 V."),
        ("¿Quién interviene tableros y baterías?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
    ],
    op=("Una radio de ejemplo tiene 3 baterías de 12 V en serie, un fusible y un equipo que consume 4 A. Dibuja o escribe el circuito con fuente, fusible y carga, calcula la tensión total y los amperios que consumen 2 equipos iguales, y explica en dos líneas por qué no intervendrías tú el banco de baterías.",
        "Circuito: fuente (baterías) → fusible → carga. Tensión: 12 más 12 más 12 son 36 V. Dos equipos: 2 por 4 son 8 A. No lo intervendría porque aunque la tensión sea baja, un cortocircuito puede producir calor y quemaduras; lo hace personal autorizado con norma vigente.",
        ["dibuja el circuito con sus tres partes", "calcula la tensión y los amperios", "explica el límite de seguridad"],
        ["hoja con el dibujo, los cálculos y la explicación"],
        ["restar los voltajes en serie", "decir que él mismo lo intervendría", "olvidar el fusible"],
        "Pregunta: «¿qué pasa con los voltajes al conectar baterías en serie?». Si no responde, pídele que sume 12 más 12."),
    reinforce="Calcula la tensión de 5 baterías de 6 V en serie.",
    extend="Explica con un ejemplo inventado por qué un fusible protege un circuito.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (datos y símbolos de ejemplo, inventados). Ley de Ohm: tensión = corriente × resistencia (V = I × R). Potencia: P = V × I (vatios, W). Símbolos de ejemplo en un esquema: batería (dos rayas), resistencia (rectángulo), fusible (rectángulo con línea), "
     "interruptor (línea abierta) y tierra (tres rayas decrecientes). Un circuito de ejemplo tiene una fuente de 12 V y una carga de 6 Ω. Documentos: esquema eléctrico, hoja de datos del fabricante y registro de medidas. Roles: técnico, supervisor y encargado de seguridad.")
build(
    O9, 2, F,
    use="Aprenderé la ley de Ohm, la potencia, los símbolos de un circuito de corriente continua y los documentos y roles del trabajo.",
    prior=["Sé qué son tensión, corriente y resistencia.", "Sé multiplicar y dividir.", "Sé leer un esquema simple."],
    explain=[
        "La ley de Ohm relaciona tensión, corriente y resistencia: la tensión (V) es igual a la corriente (I) multiplicada por la resistencia (R). Si se conocen dos valores, se calcula el tercero: I = V ÷ R y R = V ÷ I. Con 12 V y 6 Ω, la corriente es 12 ÷ 6 = 2 A. A mayor resistencia, menor corriente para la misma tensión.",
        "La potencia dice cuánta energía por segundo consume un equipo: P = V × I, en vatios (W). Con 12 V y 2 A, la potencia es 24 W. En un esquema, los símbolos representan cada elemento: batería, resistencia, fusible, interruptor y tierra. En un circuito en serie los elementos van en una sola cadena y por todos pasa la misma corriente; en paralelo van en ramas y cada rama recibe la misma tensión.",
        f"Los documentos son: el esquema eléctrico (cómo se conecta todo), la hoja de datos del fabricante (valores máximos y mínimos) y el registro de medidas (lecturas con fecha y quién midió). El técnico ejecuta lo autorizado, el supervisor revisa y el encargado de seguridad verifica las condiciones. {AVISO}",
    ],
    vocab=[("ley de Ohm", "V = I × R: tensión es corriente por resistencia"), ("potencia", "energía por segundo que consume un equipo, en vatios (W)"), ("serie", "elementos en una sola cadena, con la misma corriente"), ("paralelo", "elementos en ramas, con la misma tensión en cada una"), ("hoja de datos", "documento del fabricante con los valores del equipo"), ("registro de medidas", "lecturas con fecha, valor y quién midió")],
    worked=[
        ("Calcular la corriente", "Un circuito de ejemplo tiene 24 V y una carga de 8 Ω. ¿Qué corriente circula?", ["I es la tensión dividida por la resistencia.", "24 entre 8."], "3 A"),
        ("Calcular la potencia", "Un equipo de ejemplo funciona con 12 V y 3 A. ¿Qué potencia consume?", ["P es tensión por corriente.", "12 por 3."], "36 W"),
    ],
    mistakes=[("Multiplicar la tensión por la resistencia para obtener la corriente.", "La corriente es la tensión dividida por la resistencia.", "Escribe I = V ÷ R antes de reemplazar los números."),
              ("Creer que en un circuito en serie cada elemento tiene corriente distinta.", "En serie la corriente es la misma en todos.", "Recuerda: serie, misma corriente; paralelo, misma tensión.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué dice la ley de Ohm?", "Que la tensión es la corriente por la resistencia", "Que la corriente es la tensión por la resistencia", "Que la resistencia es la tensión más la corriente", "V = I × R relaciona las tres magnitudes."),
        ("abc", "En Telecomunicaciones: ¿qué mide la potencia?", "La energía por segundo que consume un equipo", "La longitud de un cable", "El número de baterías", "La potencia se mide en vatios."),
        ("abc", "¿Qué se mantiene igual en todos los elementos de un circuito en serie?", "La corriente", "La tensión", "La resistencia", "En serie pasa la misma corriente por todos."),
        ("=", "{F} ¿Qué corriente circula por la carga de 6 Ω con 12 V?", "12//6", "La corriente es la tensión dividida por la resistencia.", " A"),
        ("=", "{F} ¿Qué potencia consume la carga si circula la corriente del ejercicio anterior, de 2 A, con 12 V?", "12*2", "La potencia es la tensión por la corriente.", " W"),
        ("abc", "{F} ¿Qué símbolo representa el interruptor?", "Una línea abierta", "Un rectángulo", "Tres rayas decrecientes", "La ficha dice que el interruptor es una línea abierta."),
        ("=", "Un circuito de ejemplo tiene 36 V y una carga de 12 Ω. ¿Qué corriente circula?", "36//12", "Se divide la tensión por la resistencia.", " A"),
        ("=", "Un equipo de ejemplo tiene una potencia de 60 W y funciona con 12 V. ¿Qué corriente consume?", "60//12", "La corriente es la potencia dividida por la tensión.", " A"),
        ("abc", "{F} Si la carga fuera de 12 Ω en vez de 6 Ω, con los mismos 12 V, ¿qué pasa con la corriente?", "Baja a la mitad", "Se duplica", "Queda igual", "A mayor resistencia, menor corriente; de 2 A bajaría a 1 A."),
        ("abc", "{F} ¿Qué documento del fabricante dice la tensión máxima que soporta un equipo?", "La hoja de datos", "El registro de medidas", "El esquema eléctrico", "La hoja de datos trae los valores máximos y mínimos."),
        ("=", "Una carga de ejemplo consume 2 A con 48 V (valores de ejemplo). ¿Cuántos vatios consume?", "48*2", "La potencia es la tensión por la corriente.", " W"),
        ("abc", "Una compañera calcula la corriente de 24 V y 8 Ω como 24 por 8 igual a 192 A. ¿Cuál es su error?", "Multiplicó en vez de dividir", "Sumó las unidades", "Olvidó el fusible", "La corriente es la tensión dividida por la resistencia, es decir, 3 A."),
        ("abc", "El registro de medidas de ejemplo no tiene la fecha de una lectura. ¿Qué problema crea?", "No se sabe cuándo se midió", "No se sabe quién fabricó el equipo", "No cambia nada", "Sin fecha, la lectura pierde valor como evidencia."),
    ],
    ctx=("abc", "Un equipo de ejemplo necesita 5 A y el fusible disponible es de 3 A. ¿Qué concluye el técnico en papel?", "Que ese fusible se cortaría con el funcionamiento normal y que se necesita uno mayor, según la hoja de datos", "Que el fusible sirve porque 3 es menor que 5", "Que se puede reemplazar por un alambre", "El fusible debe soportar la corriente normal; la elección la define la hoja de datos."),
    sc=[
        ("En Telecomunicaciones: ¿cómo se calcula la corriente con la ley de Ohm?", "Dividiendo la tensión por la resistencia", "La ley de Ohm da la corriente como I = V ÷ R, tensión sobre resistencia."),
        ("¿Cómo se calcula la potencia de un equipo de telecomunicaciones alimentado en corriente continua?", "Multiplicando tensión por corriente", "La potencia se calcula como P = V × I, tensión por corriente."),
        ("¿Qué se mantiene igual en un circuito en paralelo?", "La tensión", "Cada rama recibe la misma tensión."),
    ],
    op=("Un equipo de ejemplo funciona con 24 V y tiene una resistencia de 12 Ω. Calcula (a) la corriente, (b) la potencia, (c) la corriente si la resistencia fuera 24 Ω y qué ocurre con ella, y (d) qué documento del fabricante consultarías para saber el máximo permitido.",
        "(a) 24 entre 12 son 2 A. (b) 24 por 2 son 48 W. (c) 24 entre 24 es 1 A; la corriente baja a la mitad. (d) La hoja de datos.",
        ["aplica la ley de Ohm", "calcula la potencia", "compara y nombra el documento"],
        ["hoja con los cuatro resultados"],
        ["multiplicar en vez de dividir", "confundir potencia con corriente", "no nombrar el documento"],
        "Pregunta: «¿qué dos valores divides para obtener la corriente?». Si no responde, pídele que escriba I = V ÷ R."),
    reinforce="Calcula la corriente de un circuito de 12 V con una carga de 4 Ω.",
    extend="Explica con un ejemplo inventado qué le pasa a la corriente si se duplica la resistencia con la misma tensión.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (lecturas de ejemplo, inventadas; las toma personal autorizado). Circuito en serie de ejemplo: fuente de 12 V → fusible → interruptor → carga de 6 Ω → de vuelta a la fuente. "
     "Caso A (funciona): tensión en la carga 12 V; corriente 2 A. Caso B (no funciona): tensión en la carga 0 V; la tensión entre los dos extremos del fusible es 12 V; corriente 0 A. "
     "Caso C (no funciona): tensión en la carga 0 V; la tensión entre los dos extremos del fusible es 0 V; el interruptor está abierto y la tensión entre sus dos extremos es 12 V. "
     "Regla: si hay un corte en un circuito en serie, no circula corriente y toda la tensión de la fuente aparece entre los extremos del elemento cortado.")
build(
    O9, 3, F,
    use="Aprenderé a interpretar en papel lecturas de un circuito de corriente continua para encontrar el elemento con falla, sin hacer mediciones.",
    prior=["Sé la ley de Ohm y el circuito en serie.", "Sé qué es un circuito abierto.", "Sé qué hace un fusible."],
    explain=[
        "Una falla común es el circuito abierto: un corte en el camino de la corriente, por ejemplo un fusible quemado, un interruptor abierto o un cable roto. En un circuito en serie, si hay un corte, la corriente es cero en todo el circuito. Y la tensión de la fuente aparece completa entre los dos extremos del elemento cortado, porque ahí está la interrupción.",
        "Otra falla es el cortocircuito, una unión de baja resistencia que deja pasar una corriente muy alta. El fusible está para cortarse en ese caso. Interpretar lecturas consiste en preguntarse: ¿hay tensión en la carga?, ¿hay corriente?, ¿entre qué extremos aparece toda la tensión? Con esas respuestas se descubre qué elemento tiene la falla.",
        f"Estas lecturas las entrega el enunciado: tomar mediciones en un circuito con energía es tarea de personal autorizado, con instrumentos calibrados y la norma vigente. Corregir la falla (cambiar un fusible, reparar un cable) también lo hace personal autorizado. {AVISO} Aquí solo se identifica el elemento con falla y se registra.",
    ],
    vocab=[("circuito abierto", "camino cortado por donde no circula corriente"), ("elemento cortado", "parte del circuito que interrumpe el paso de la corriente"), ("lectura", "valor entregado por un instrumento"), ("falla", "defecto que impide el funcionamiento esperado"), ("diagnóstico", "conclusión sobre cuál es la falla y dónde está")],
    worked=[
        ("Fusible quemado", "Lecturas de ejemplo: 0 V en la carga, 0 A y 12 V entre los dos extremos del fusible. ¿Qué elemento está cortado?", ["Toda la tensión aparece entre los extremos del fusible.", "Entonces el fusible está cortado."], "El fusible"),
        ("Descartar", "Si el circuito de ejemplo funciona con 12 V en la carga y 2 A, ¿hay falla?", ["Hay tensión y corriente en la carga.", "El circuito funciona."], "No hay falla"),
    ],
    mistakes=[("Culpar a la carga porque no funciona, sin mirar el resto del circuito.", "La carga puede estar bien y faltarle alimentación por un corte antes de ella.", "Mira entre qué extremos aparece la tensión completa."),
              ("Cambiar un fusible quemado por uno de mayor valor «para que no se corte más».", "El fusible protege los cables; uno mayor deja de proteger.", "Informa y usa solo el valor indicado en la hoja de datos, por personal autorizado.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un circuito abierto?", "Un camino cortado por donde no circula corriente", "Un circuito con corriente muy alta", "Un circuito sin fuente", "En un circuito abierto la corriente es cero."),
        ("abc", "En un circuito en serie con un corte, ¿qué corriente circula?", "Cero", "La máxima", "La mitad", "Sin camino cerrado no hay corriente."),
        ("abc", "¿Dónde aparece toda la tensión de la fuente si hay un elemento cortado en serie?", "Entre los extremos del elemento cortado", "En la carga", "En la fuente solamente", "El corte concentra la tensión de la fuente."),
        ("abc", "{F} En el caso B, ¿qué elemento está cortado?", "El fusible", "El interruptor", "La carga", "Toda la tensión de 12 V aparece entre los extremos del fusible."),
        ("abc", "{F} En el caso C, ¿qué elemento causa la falla?", "El interruptor, que está abierto", "El fusible", "La fuente", "Hay 12 V entre los extremos del interruptor abierto."),
        ("abc", "{F} ¿Funciona el circuito del caso A?", "Sí, porque hay 12 V en la carga y 2 A", "No, porque la corriente es 2 A", "No, porque hay un fusible", "Con tensión y corriente en la carga, el circuito funciona."),
        ("=", "{F} En el caso A, ¿cuántos vatios consume la carga, con 12 V y 2 A?", "12*2", "La potencia es la tensión por la corriente.", " W"),
        ("abc", "{F} En el caso B, ¿qué debe hacer una persona sin autorización al ver el fusible quemado?", "Informar a personal autorizado para su cambio", "Cambiarlo con cualquier alambre", "Cambiarlo por uno de mayor valor", "Corregir fallas con energía es tarea de personal autorizado."),
        ("abc", "{F} En el caso C, el fusible tiene 0 V entre sus extremos. ¿Qué indica?", "Que el fusible está sano y deja pasar la corriente", "Que el fusible está cortado", "Que la fuente está apagada", "Con 0 V entre sus extremos no hay corte en el fusible."),
        ("=", "{F} ¿Cuántos casos de la ficha tienen falla de corte (B y C)?", "1+1", "Los casos B y C tienen elementos cortados.", " casos"),
        ("abc", "Lecturas de ejemplo: 0 V en la carga, 0 A y 0 V entre los extremos de todos los elementos, incluida la fuente. ¿Qué falla se sospecha?", "Que la fuente no entrega tensión", "Que el fusible está cortado", "Que la carga es de 6 Ω", "Si no hay tensión en ningún punto, el problema está en la fuente."),
        ("abc", "{F} Un técnico novato propone puentear el interruptor con un cable para «arreglar» el caso C. ¿Qué corresponde?", "No hacerlo: la reparación la hace personal autorizado", "Hacerlo, si usa guantes", "Hacerlo, pero sin avisar", "Alterar protecciones y circuitos energizados es tarea de personal autorizado."),
        ("abc", "{F} ¿Qué debe quedar escrito tras interpretar las lecturas?", "El diagnóstico, las lecturas y quién informó", "Solo el nombre del cliente", "Solo la fecha", "El registro escrito respalda el diagnóstico y permite verificarlo después."),
    ],
    ctx=("abc", "Una radio comunitaria de ejemplo pregunta por qué su equipo se apagó. La lectura entre los extremos del fusible es de 24 V y en la carga hay 0 V. ¿Qué diagnóstico hace el técnico en papel?", "El fusible está cortado y debe informarse a personal autorizado", "La carga está mala y hay que tirarla", "Hay que quitar el fusible para que funcione", "Toda la tensión entre los extremos del fusible indica un fusible cortado."),
    sc=[
        ("En Telecomunicaciones: ¿qué corriente circula en un circuito en serie con un corte?", "Cero", "Sin camino cerrado no hay corriente."),
        ("¿Dónde aparece la tensión completa de la fuente?", "Entre los extremos del elemento cortado", "Ese elemento interrumpe el circuito y concentra la tensión de la fuente."),
        ("¿Quién corrige las fallas con energía?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
    ],
    op=("Lecturas de ejemplo de un circuito en serie de 24 V (fuente, fusible, cable, carga): corriente 0 A; tensión en la carga 0 V; tensión entre los extremos del fusible 0 V; tensión entre los extremos del cable 24 V. Escribe (a) qué elemento está cortado y por qué, (b) qué valor tendría la corriente si el cable estuviera sano y la carga fuera de 12 Ω y (c) quién corrige la falla.",
        "(a) El cable está cortado, porque toda la tensión de 24 V aparece entre sus extremos. (b) Con el cable sano, la corriente sería 24 entre 12, es decir, 2 A. (c) Personal autorizado, con norma vigente.",
        ["identifica el elemento cortado con la regla", "calcula la corriente con la ley de Ohm", "dice quién corrige"],
        ["hoja con la lectura interpretada y los cálculos"],
        ["culpar a la carga", "olvidar la regla de los extremos", "proponer reparar sin autorización"],
        "Pregunta: «¿entre qué extremos aparece toda la tensión?». Si no responde, pídele que lea las lecturas una por una."),
    reinforce="Interpreta estas lecturas de ejemplo: 0 A, 12 V entre los extremos de un interruptor. ¿Qué elemento está abierto?",
    extend="Explica con un ejemplo inventado por qué un fusible quemado indica que hay que buscar la causa antes de cambiarlo.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (criterio técnico con datos de ejemplo, inventados). Equipo de transmisión del «Sitio Loma Verde» (ficticio) en corriente continua: 24 V; consumo normal 10 A. El cable soporta como máximo 30 A (hoja de datos de ejemplo). "
     "Fusibles disponibles en papel: 5 A, 15 A y 40 A. Banco de baterías de 200 Ah (amperios-hora) a 24 V. Regla de ejemplo: el fusible debe estar sobre la corriente normal y bajo el máximo del cable. "
     "Falla observada (lecturas de ejemplo): 24 V a la entrada del equipo; en un tramo del cable se miden 20 V al final; el cable tiene 0,4 Ω de resistencia total (de ejemplo) con una corriente de 10 A circulando.")
build(
    O9, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: elegir un fusible, estimar la autonomía de las baterías y calcular la caída de tensión en un cable.",
    prior=["Sé la ley de Ohm y la potencia.", "Sé qué es un fusible.", "Sé dividir y multiplicar."],
    explain=[
        "El fusible se elige entre dos límites: debe ser mayor que la corriente normal del equipo (si no, se cortaría en el funcionamiento normal) y menor que la corriente máxima que soporta el cable (si no, no protegería al cable). Con consumo normal de 10 A y cable de 30 A como máximo, sirve un fusible entre 10 A y 30 A. En la práctica el valor lo define el proyecto y la hoja de datos.",
        "La autonomía de un banco de baterías se estima dividiendo su capacidad (en amperios-hora, Ah) por la corriente que consume el equipo. Con 200 Ah y 10 A, la autonomía ideal es 20 horas. En la realidad es menor, por el envejecimiento y la temperatura, por lo que se deja un margen. La caída de tensión en un cable se calcula con la ley de Ohm: V = I × R. Con 10 A y 0,4 Ω, la caída es 4 V.",
        f"La decisión se escribe con los números y se entrega a la jefatura. Cambiar fusibles, medir en un sitio energizado o intervenir baterías lo hace personal autorizado. {AVISO}",
    ],
    vocab=[("corriente normal", "corriente que el equipo consume al funcionar bien"), ("corriente máxima del cable", "mayor corriente que el cable soporta sin dañarse"), ("capacidad (Ah)", "carga que una batería puede entregar, en amperios-hora"), ("autonomía", "tiempo que el banco de baterías mantiene el equipo"), ("caída de tensión", "pérdida de tensión en un cable al circular corriente")],
    worked=[
        ("Elegir el fusible", "Un equipo de ejemplo consume 8 A y el cable soporta 20 A. Hay fusibles de 5 A, 10 A y 40 A. ¿Cuál sirve?", ["Debe estar sobre 8 A y bajo 20 A.", "El de 10 A cumple."], "El de 10 A"),
        ("Autonomía", "Un banco de ejemplo de 100 Ah alimenta un equipo de 5 A. ¿Cuántas horas de autonomía ideal tiene?", ["Se divide la capacidad por la corriente.", "100 entre 5."], "20 horas"),
    ],
    mistakes=[("Elegir el fusible más grande «para estar seguros».", "Uno mayor que el máximo del cable no lo protege.", "Elige un fusible entre la corriente normal y el máximo del cable."),
              ("Creer que la autonomía ideal es la real.", "La capacidad real baja con el uso y la temperatura.", "Deja un margen y no prometas la cifra ideal.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿entre qué dos límites se elige un fusible?", "Sobre la corriente normal y bajo el máximo del cable", "Bajo la corriente normal", "Sobre el máximo del cable", "El fusible debe permitir el uso normal y proteger al cable."),
        ("abc", "En Telecomunicaciones: ¿qué es la autonomía de un banco de baterías?", "El tiempo que mantiene funcionando el equipo", "El número de baterías", "La tensión del equipo", "La autonomía se estima dividiendo la capacidad por la corriente."),
        ("abc", "¿Qué unidad mide la capacidad de una batería?", "Amperios-hora (Ah)", "Ohmios", "Voltios", "La capacidad se mide en amperios-hora."),
        ("abc", "{F} ¿Qué fusible cumple la regla de la ficha?", "El de 15 A", "El de 5 A", "El de 40 A", "15 A es mayor que 10 A y menor que 30 A."),
        ("abc", "{F} ¿Por qué no sirve el fusible de 5 A?", "Se cortaría con el funcionamiento normal de 10 A", "No protege al cable", "Consume mucha energía", "El consumo normal, 10 A, supera los 5 A del fusible."),
        ("abc", "{F} ¿Por qué no sirve el fusible de 40 A?", "Es mayor que los 30 A que soporta el cable y no lo protege", "Se corta con 10 A", "Cambia la tensión", "Con 40 A el cable podría dañarse antes de que el fusible se corte."),
        ("=", "{F} ¿Cuántas horas de autonomía ideal da el banco de 200 Ah con el consumo normal de 10 A?", "200//10", "Se divide la capacidad por la corriente.", " horas"),
        ("=", "{F} ¿Cuál es la caída de tensión en el cable, en voltios, con 10 A y 0,4 Ω?", "10*4//10", "Se aplica V = I × R: 10 por 0,4 es 4.", " V"),
        ("abc", "{F} Si entran 24 V al cable y la caída es 4 V, ¿cuánta tensión llega al final?", "20 V", "28 V", "24 V", "Se resta la caída: 24 menos 4 da 20 V, lo que coincide con la lectura."),
        ("=", "{F} Si la autonomía real fuera la mitad de la ideal, ¿cuántas horas serían?", "200//10//2", "La autonomía ideal son 20 horas; la mitad son 10.", " horas"),
        ("=", "Un equipo de ejemplo consume 4 A en un banco de 120 Ah. ¿Cuántas horas de autonomía ideal da?", "120//4", "Se divide la capacidad por la corriente.", " horas"),
        ("abc", "{F} Un colega propone reemplazar el fusible por un alambre grueso «porque aguanta más». ¿Qué corresponde?", "No hacerlo: el fusible debe ser el indicado y el cambio lo hace personal autorizado", "Hacerlo, es lo mismo", "Hacerlo y no avisar", "Un alambre no protege y eliminar protecciones crea riesgo de incendio."),
        ("abc", "{F} El cliente de ejemplo pide prometer 20 horas de autonomía por escrito. ¿Qué responde el técnico?", "Que 20 horas es la cifra ideal y que la real será menor, con un margen indicado", "Que promete 20 horas exactas", "Que promete 40 horas", "Las cifras ideales no se prometen como reales."),
    ],
    ctx=("abc", "La dueña de un sitio de ejemplo quiere ahorrar y propone usar un cable más delgado. La caída de tensión ya llega a 4 V de los 24 V. ¿Qué advierte el técnico?", "Que un cable más delgado tiene más resistencia y aumentaría la caída de tensión, y que decide el proyecto", "Que el cable delgado es mejor", "Que no hay caída de tensión", "Más resistencia significa más caída con la misma corriente."),
    sc=[
        ("En Telecomunicaciones: ¿cómo se calcula la autonomía ideal?", "Dividiendo la capacidad en Ah por la corriente en A", "100 Ah entre 5 A dan 20 horas."),
        ("¿Cómo se calcula la caída de tensión en un cable?", "Multiplicando corriente por resistencia", "Se aplica V = I × R."),
        ("¿Quién cambia fusibles en un sitio energizado?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
    ],
    op=("Un equipo de ejemplo en un sitio rural consume 6 A a 24 V; el cable soporta 20 A; hay fusibles de 5 A, 10 A y 30 A; el banco es de 120 Ah; la resistencia total del cable es 0,5 Ω. Elige el fusible y justifica, calcula la autonomía ideal, estima la caída de tensión (6 por 0,5) y escribe una frase prudente sobre la autonomía.",
        "Fusible de 10 A, porque es mayor que 6 A y menor que 20 A. Autonomía ideal: 120 entre 6 son 20 horas. Caída de tensión: 6 por 0,5 son 3 V. Frase: la autonomía real será menor que 20 horas por el envejecimiento y la temperatura, por lo que se deja un margen.",
        ["elige el fusible entre los dos límites", "calcula la autonomía y la caída", "escribe una frase prudente"],
        ["hoja con la elección, los cálculos y la frase"],
        ["elegir el fusible más grande", "prometer la autonomía ideal", "olvidar justificar"],
        "Pregunta: «¿por qué no el fusible de 30 A?». Si no responde, pídele que lo compare con el máximo del cable."),
    reinforce="Elige un fusible entre 3 A, 8 A y 25 A para un equipo de 5 A en un cable de 15 A.",
    extend="Explica con un ejemplo inventado por qué una batería nunca entrega en la práctica su capacidad ideal.",
)

# ============================================================ OAE-10, clase 1
F = ("Ficha 5 (solicitud de ejemplo, inventada). La «Clínica Dental Sonrisa» (ficticia) pide ayuda: 12 puestos de trabajo con computador, 1 recepción con telefonía, videollamadas con pacientes, wifi para la sala de espera y cámaras de seguridad en la entrada. "
     "Dice el dueño: «no podemos quedarnos sin internet en horario de atención» y «quiero lo mejor que exista». Presupuesto de ejemplo: $1.500.000 en total, a cobrar una sola vez. Datos de pacientes se guardan en un computador (datos personales).")
build(
    O10, 1, F,
    use="Aprenderé a entender la necesidad de un cliente, a distinguir lo que necesita de lo que desea y a cuidar la ética y la privacidad al proponer equipos.",
    prior=["Sé qué es una red LAN y una red inalámbrica.", "Sé qué es un dato personal.", "Sé qué es un presupuesto."],
    explain=[
        "Determinar los equipos de una red empieza por entender al cliente, no por elegir equipos. El levantamiento de requerimientos es la lista de lo que el cliente necesita y las condiciones del lugar. Un requerimiento funcional dice qué debe hacer el sistema (por ejemplo, permitir videollamadas); uno no funcional dice cómo debe comportarse (por ejemplo, estar disponible en horario de atención). También se anota el presupuesto y los plazos.",
        "Se distingue lo que el cliente necesita de lo que desea. «Lo mejor que exista» no es un requerimiento: se traduce en números, como usuarios, velocidad y disponibilidad. Proponer equipos de más para vender más no es honesto; proponer equipos de menos para ganar el contrato tampoco. La propuesta debe ser verdadera, justificada y ajustada al presupuesto.",
        "También hay cuidados éticos. Las cámaras y los computadores de una clínica manejan datos personales, que se protegen según la norma vigente: acceso restringido, respaldos y aviso a las personas cuando corresponde. Esta clase es de papel con datos inventados; la instalación de equipos la realiza personal autorizado. " + AVISO,
    ],
    vocab=[("levantamiento de requerimientos", "lista de lo que el cliente necesita y de las condiciones del lugar"), ("requerimiento funcional", "lo que el sistema debe hacer"), ("requerimiento no funcional", "cómo debe comportarse el sistema, como su disponibilidad"), ("presupuesto", "monto máximo que el cliente puede gastar"), ("propuesta técnica", "documento con los equipos recomendados y sus razones")],
    worked=[
        ("Clasificar un requerimiento", "El cliente de ejemplo dice: «el sistema debe permitir videollamadas». ¿Es funcional o no funcional?", ["Dice qué debe hacer el sistema.", "Es un requerimiento funcional."], "Funcional"),
        ("Traducir un deseo", "El cliente de ejemplo dice: «quiero internet rápido». ¿Qué debe hacer el técnico?", ["Un deseo vago no sirve para calcular.", "Debe traducirlo en números, como Mbps y usuarios."], "Preguntar y traducirlo en números"),
    ],
    mistakes=[("Elegir equipos antes de entender lo que el cliente necesita.", "Se puede proponer algo caro o insuficiente.", "Primero haz el levantamiento de requerimientos."),
              ("Proponer equipos de más para que la venta sea mayor.", "No es honesto y el cliente paga por algo que no necesita.", "Propone lo que se justifica con los números.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un requerimiento funcional?", "Lo que el sistema debe hacer", "Cómo se llama el equipo", "El precio del contrato", "El requerimiento funcional describe una función del sistema."),
        ("abc", "En Telecomunicaciones: ¿qué es un requerimiento no funcional?", "Cómo debe comportarse el sistema, como su disponibilidad", "Una función como hacer llamadas", "El color de los equipos", "Estar disponible en horario de atención es una condición de comportamiento."),
        ("abc", "¿Qué documento reúne los equipos recomendados y sus razones?", "La propuesta técnica", "El plano de evacuación", "La bitácora de mantenimiento", "La propuesta técnica justifica las recomendaciones."),
        ("=", "{F} ¿Cuántos puestos de trabajo y recepción hay en total (12 puestos más 1 recepción)?", "12+1", "Se suman los puestos y la recepción.", " puestos"),
        ("abc", "{F} ¿Qué frase del cliente es un requerimiento no funcional?", "No podemos quedarnos sin internet en horario de atención", "Hacemos videollamadas", "Tenemos 12 computadores", "Estar disponible en horario de atención describe cómo debe funcionar el sistema."),
        ("abc", "{F} ¿Qué frase del cliente es un deseo que hay que traducir en números?", "Quiero lo mejor que exista", "Tengo 12 puestos de trabajo", "El presupuesto es $1.500.000", "«Lo mejor que exista» no se puede calcular sin números."),
        ("abc", "{F} Un vendedor de ejemplo propone tres veces más equipos de los necesarios para ganar más dinero. ¿Qué problema ético hay?", "Se le hace pagar al cliente por algo que no necesita", "Se baja el presupuesto", "Se mejora la propuesta", "Una propuesta debe ser honesta y justificada."),
        ("abc", "{F} ¿Qué dato de la clínica exige especial cuidado según la norma vigente?", "Los datos personales de los pacientes", "El número de computadores", "El color de las paredes", "Los datos de pacientes son personales y se protegen."),
        ("=", "{F} Si ya se gastaron $400.000 de un presupuesto de $1.500.000, ¿cuánto queda disponible?", "1500000-400000", "Se resta lo gastado al presupuesto.", ""),
        ("abc", "El técnico de ejemplo ve en el computador del dueño la lista de pacientes. ¿Qué corresponde?", "Limitarse al trabajo pedido y no copiar ni comentar los datos", "Copiarla para sus pruebas", "Comentarla con sus amigos", "Los datos personales no se usan fuera del fin autorizado."),
        ("=", "Un cliente de ejemplo tiene 3 sucursales con 8 puestos cada una. ¿Cuántos puestos hay en total?", "3*8", "Se multiplican las sucursales por los puestos de cada una.", " puestos"),
        ("abc", "{F} El dueño pide instalar las cámaras en el baño de pacientes «por seguridad». ¿Qué corresponde responder?", "Que no corresponde por la privacidad de las personas y que se proponen alternativas", "Que se instalan sin avisar", "Que se instalan en secreto", "La privacidad de las personas se respeta y las alternativas se proponen."),
        ("abc", "{F} El dueño del negocio de ejemplo pide subir un cable por el techo, a gran altura, para ahorrar. ¿Qué corresponde?", "Dejar el trabajo en altura a personal autorizado y norma vigente", "Subir con una escalera prestada", "Pedirle a un familiar", "El trabajo en altura es de personal autorizado."),
    ],
    ctx=("abc", "La clínica de ejemplo pide una propuesta, pero no dice cuántos usuarios usarán el wifi de la sala de espera. ¿Qué hace el técnico?", "Pregunta por el número de usuarios y lo anota en el levantamiento", "Inventa una cifra grande", "Pone el wifi más caro", "Se pregunta para tener datos reales."),
    sc=[
        ("En Telecomunicaciones: ¿qué se hace antes de elegir equipos?", "El levantamiento de requerimientos", "Primero se entiende la necesidad del cliente y después se eligen equipos."),
        ("¿Por qué «lo mejor que exista» no sirve como requerimiento?", "Porque no se puede calcular sin números", "Hay que traducirlo en usuarios, velocidad y disponibilidad."),
        ("¿Qué datos de la clínica son personales?", "Los de los pacientes", "Se protegen según la norma vigente."),
    ],
    op=("Un taller de ejemplo dice: «necesitamos internet para 10 computadores, una impresora en red, videollamadas con clientes y que no se caiga en el horario de 9 a 18 horas». Clasifica en funcionales y no funcionales sus necesidades, escribe dos preguntas que harías para completar el levantamiento y un cuidado de privacidad.",
        "Funcionales: internet para 10 computadores, impresora en red, videollamadas. No funcional: disponibilidad en el horario de 9 a 18 horas. Preguntas: cuántas videollamadas a la vez y cuál es el presupuesto. Cuidado: proteger los datos personales de los clientes con acceso restringido y respaldo.",
        ["clasifica los requerimientos", "formula dos preguntas útiles", "nombra un cuidado de privacidad"],
        ["hoja con la clasificación, las preguntas y el cuidado"],
        ["confundir funcional con no funcional", "no preguntar", "olvidar los datos personales"],
        "Pregunta: «¿qué debe hacer el sistema y cómo debe comportarse?». Si no responde, pídele que separe las frases en dos columnas."),
    reinforce="Escribe dos requerimientos funcionales y uno no funcional para una biblioteca de ejemplo.",
    extend="Explica con un ejemplo inventado por qué proponer de menos o de más es una falta de honestidad con el cliente.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 6 (glosario y documentos de ejemplo, inventados). Equipos de ejemplo: router (conecta con internet), switch (reparte la red local; con PoE alimenta teléfonos y cámaras por el cable), punto de acceso (wifi), cortafuegos (filtra el tráfico) y UPS (respaldo de energía por unos minutos). "
     "Medidas: ancho de banda en Mbps; disponibilidad en porcentaje del tiempo; latencia en milisegundos. Documentos: levantamiento de requerimientos, propuesta técnica, cotización y diagrama de la red. "
     "Roles: ejecutivo comercial, ingeniero de preventa, técnico y cliente.")
build(
    O10, 2, F,
    use="Aprenderé el vocabulario para dimensionar una red (ancho de banda, disponibilidad, redundancia, escalabilidad) y los documentos y roles de una propuesta.",
    prior=["Sé qué hace un router, un switch y un punto de acceso.", "Sé calcular porcentajes sencillos.", "Sé qué es un requerimiento."],
    explain=[
        "El ancho de banda es la cantidad de datos por segundo que puede llevar un enlace y se mide en megabits por segundo (Mbps). La disponibilidad es el porcentaje del tiempo en que el servicio funciona: una disponibilidad de 99 % significa que en cada 1.000 horas habrá 10 horas sin servicio. La latencia es la demora de los datos, en milisegundos. La redundancia es tener un equipo o enlace de respaldo para que el servicio siga si algo falla. La escalabilidad es la capacidad de crecer sin cambiar todo.",
        "Los equipos tienen funciones distintas: el router conecta con internet, el switch reparte la red local, el punto de acceso da wifi, el cortafuegos filtra el tráfico peligroso y la UPS da energía de respaldo por unos minutos para apagar bien o mantener el servicio. El PoE (energía por el cable de red) permite alimentar teléfonos y cámaras sin enchufe cercano.",
        "Los documentos son el levantamiento de requerimientos, la propuesta técnica (qué equipos y por qué), la cotización (el precio) y el diagrama de la red. El ejecutivo comercial atiende al cliente, el ingeniero de preventa diseña la solución, el técnico instala lo autorizado y el cliente aprueba. Las instalaciones las realiza personal autorizado. " + AVISO,
    ],
    vocab=[("ancho de banda", "datos por segundo que puede llevar un enlace, en Mbps"), ("disponibilidad", "porcentaje del tiempo en que el servicio funciona"), ("redundancia", "equipo o enlace de respaldo para que el servicio siga si algo falla"), ("escalabilidad", "capacidad de crecer sin cambiar todo"), ("UPS", "equipo que da energía de respaldo por unos minutos"), ("cotización", "documento con el precio de la propuesta")],
    worked=[
        ("Horas sin servicio", "Una disponibilidad de 99 % significa que en 1.000 horas hay 10 horas sin servicio. Con 99,9 % hay 1 hora sin servicio en 1.000. ¿Cuántas horas sin servicio hay en 2.000 horas con 99 %?", ["En 1.000 horas hay 10 horas.", "En 2.000 horas el doble: 20."], "20 horas"),
        ("Para qué sirve una UPS", "Se corta la energía de un edificio de ejemplo. ¿Para qué sirve la UPS?", ["Da energía de respaldo por unos minutos.", "Permite mantener el servicio o apagar los equipos sin dañarlos."], "Para dar energía de respaldo por unos minutos"),
    ],
    mistakes=[("Creer que 99 % de disponibilidad es «casi perfecto» para cualquier cliente.", "En 1.000 horas hay 10 horas sin servicio, que para una clínica puede ser demasiado.", "Traduce el porcentaje a horas y pregunta si el cliente lo tolera."),
              ("Pensar que la UPS da energía por horas.", "La UPS da respaldo por unos minutos, no por horas.", "Para más tiempo se necesita otro sistema de respaldo, según el proyecto.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la redundancia?", "Tener un equipo o enlace de respaldo para seguir si algo falla", "Tener más equipos de los necesarios por tener", "Cambiar de proveedor cada año", "La redundancia mantiene el servicio ante una falla."),
        ("abc", "En Telecomunicaciones: ¿qué es la escalabilidad?", "La capacidad de crecer sin cambiar todo", "La velocidad del router", "El precio por mes", "Escalable es lo que puede ampliarse sin rehacerse."),
        ("abc", "¿Qué documento tiene el precio de la propuesta?", "La cotización", "El diagrama de la red", "El levantamiento de requerimientos", "La cotización es el documento que indica el precio de la propuesta."),
        ("abc", "{F} ¿Qué equipo filtra el tráfico peligroso de la red?", "El cortafuegos", "El switch", "La UPS", "El cortafuegos filtra el tráfico que entra y sale de la red."),
        ("abc", "{F} ¿Qué característica permite alimentar una cámara por el mismo cable de red?", "PoE", "UPS", "Latencia", "PoE entrega energía por el cable de red."),
        ("=", "En 1.000 horas, una disponibilidad de 99 % deja 10 horas sin servicio. ¿Cuántas horas sin servicio hay en 3.000 horas con 99 %?", "3*10", "Cada 1.000 horas hay 10 sin servicio; se multiplica por 3.", " horas"),
        ("=", "En 1.000 horas, una disponibilidad de 99,9 % deja 1 hora sin servicio. ¿Cuántas horas sin servicio hay en 5.000 horas con 99,9 %?", "5*1", "Cada 1.000 horas hay 1 hora sin servicio.", " horas"),
        ("abc", "Un cliente de ejemplo no tolera más de 2 horas sin servicio cada 1.000 horas. ¿Le sirve una disponibilidad de 99 %?", "No, porque deja 10 horas sin servicio", "Sí, porque 99 es casi 100", "Sí, porque 10 es menor que 2", "10 horas superan el máximo tolerado de 2."),
        ("abc", "{F} ¿Qué rol diseña la solución técnica?", "El ingeniero de preventa", "El cliente", "El ejecutivo comercial al firmar", "El ingeniero de preventa diseña la solución."),
        ("=", "Un enlace de ejemplo ofrece 100 Mbps y se reparten en partes iguales entre 20 puestos. ¿Cuántos Mbps tiene cada puesto?", "100//20", "Se divide el ancho de banda entre los puestos.", " Mbps"),
        ("abc", "{F} Un cliente quiere que su red no se caiga si falla el router principal. ¿Qué concepto debe incluir la propuesta?", "Redundancia", "Escalabilidad", "Latencia", "Un router de respaldo es redundancia."),
        ("abc", "{F} La UPS de ejemplo da 10 minutos de respaldo. El corte de energía dura 2 horas. ¿Qué concluye el técnico?", "Que la UPS sola no alcanza para toda la duración y se informa al cliente", "Que la UPS alcanza porque 10 es mayor que 2", "Que no se necesita UPS", "10 minutos no cubren 2 horas."),
        ("abc", "El ejecutivo comercial de ejemplo promete 100 % de disponibilidad sin consultar al técnico. ¿Qué problema hay?", "Hace una promesa que no puede garantizar", "Mejora la propuesta", "No hay problema", "Ninguna red puede prometer disponibilidad total."),
    ],
    ctx=("abc", "Un cliente de ejemplo con dos locales pregunta qué es mejor: una UPS o un segundo enlace de internet. ¿Qué responde el técnico?", "Que cubren problemas distintos: la UPS la falta de energía y el segundo enlace la falla de internet", "Que son iguales", "Que ninguno sirve", "La UPS respalda la energía y la redundancia de enlace respalda internet."),
    sc=[
        ("En Telecomunicaciones: ¿qué mide el ancho de banda?", "Los datos por segundo que lleva un enlace", "El ancho de banda se mide en megabits por segundo, Mbps."),
        ("¿Qué hace la UPS?", "Da energía de respaldo por unos minutos", "La UPS da respaldo por unos minutos y no dura horas."),
        ("¿Quién diseña la solución?", "El ingeniero de preventa", "El técnico instala solo lo autorizado en la propuesta."),
    ],
    op=("Una escuela de ejemplo pide una propuesta con disponibilidad de al menos 99,9 % y respaldo de energía. Escribe (a) cuántas horas sin servicio permite 99,9 % en 1.000 horas, (b) qué equipos incluirías para el respaldo de energía y de enlace y (c) qué documento llevaría el precio.",
        "(a) 1 hora sin servicio en cada 1.000 horas. (b) UPS para la energía y un segundo enlace de internet como redundancia. (c) La cotización.",
        ["interpreta el porcentaje en horas", "propone equipos de respaldo", "nombra el documento del precio"],
        ["hoja con las tres respuestas"],
        ["no traducir el porcentaje a horas", "decir que la UPS da horas", "confundir la cotización con el diagrama"],
        "Pregunta: «¿cuántas horas sin servicio son 0,1 % de 1.000?». Si no responde, pídele que recuerde la equivalencia de la ficha."),
    reinforce="Explica con tus palabras la diferencia entre redundancia y escalabilidad.",
    extend="Explica con un ejemplo inventado por qué dos locales pueden necesitar disponibilidades distintas.",
)



# ============================================================ OAE-10, clase 3
F = ("Ficha 7 (caso de ejemplo, inventado). La «Constructora Aguas Claras» (ficticia) tiene una oficina con 40 usuarios. Datos de ejemplo: cada usuario activo usa en promedio 2 Mbps; en la hora de mayor uso, solo el 50 % de los usuarios está activo a la vez; "
     "además habrá 8 videollamadas simultáneas de 3 Mbps cada una; los enlaces de internet se ofrecen de 50, 100 y 200 Mbps; regla de ejemplo: el tráfico esperado no debe superar el 70 % del enlace. "
     "La oficina tendrá 40 computadores, 5 impresoras en red y 6 teléfonos IP. Switches de ejemplo: 24 y 48 puertos.")
build(
    O10, 3, F,
    use="Aprenderé a analizar en papel los requerimientos de una oficina y a calcular el ancho de banda y los puertos que necesita.",
    prior=["Sé qué es el ancho de banda y los Mbps.", "Sé calcular un porcentaje simple.", "Sé qué es un switch."],
    explain=[
        "Para saber qué enlace de internet necesita una oficina se calcula el tráfico que se espera en la hora de mayor uso. Primero, los usuarios activos a la vez: el total de usuarios por el porcentaje que está activo. Luego, el consumo de esos usuarios: usuarios activos por lo que usa cada uno. A ese tráfico se suman las videollamadas simultáneas (cantidad por los Mbps de cada una).",
        "Con el total se elige el enlace de menor tamaño que lo cubra respetando la regla del proyecto, que aquí pide no superar el 70 % del enlace para dejar reserva. Para el switch se cuentan los puertos: un puerto por computador, impresora o teléfono IP conectado por cable. Si el total supera los puertos de un switch, se usa uno mayor o se suman varios.",
        "El análisis termina con una conclusión escrita con los números, que se entrega a la jefatura o al cliente. Las cifras de uso real dependen de la organización; aquí son solo de ejemplo. La instalación de los equipos la hace personal autorizado. " + AVISO,
    ],
    vocab=[("usuarios activos", "usuarios que usan la red a la vez en la hora de mayor uso"), ("tráfico esperado", "datos por segundo que se espera que use la oficina"), ("puerto", "entrada de un switch para conectar un equipo"), ("reserva", "parte de la capacidad que se deja libre para crecer")],
    worked=[
        ("Usuarios activos", "Una oficina de ejemplo tiene 60 usuarios y el 50 % está activo a la vez. ¿Cuántos usuarios están activos?", ["El 50 % es la mitad.", "60 entre 2."], "30 usuarios"),
        ("Videollamadas", "En una oficina de ejemplo hay 5 videollamadas simultáneas de 2 Mbps cada una. ¿Cuántos Mbps suman?", ["Se multiplica la cantidad por lo que usa cada una.", "5 por 2."], "10 Mbps"),
    ],
    mistakes=[("Calcular con todos los usuarios activos a la vez cuando el cliente dice que solo la mitad lo está.", "Se sobredimensiona la solución y se cobra de más.", "Usa el porcentaje de actividad que informa el cliente."),
              ("Olvidar contar los puertos de las impresoras y los teléfonos.", "Se queda corto el switch.", "Cuenta todos los equipos que se conectan por cable.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué son los usuarios activos?", "Los usuarios que usan la red a la vez en la hora de mayor uso", "Todos los usuarios de la oficina", "Los usuarios que están de vacaciones", "El tráfico se calcula con quienes están activos a la vez."),
        ("abc", "En Telecomunicaciones: ¿qué es un puerto de un switch?", "La entrada para conectar un equipo", "La velocidad del enlace", "La contraseña del switch", "Cada puerto conecta un equipo por cable."),
        ("abc", "¿Cómo se calcula el tráfico de los usuarios activos?", "Usuarios activos por el consumo de cada uno", "Usuarios totales más impresoras", "Número de switches por 2", "Se multiplica la cantidad de activos por lo que usa cada uno."),
        ("=", "{F} ¿Cuántos usuarios están activos a la vez (50 % de 40)?", "40//2", "El 50 % es la mitad de los usuarios.", " usuarios"),
        ("=", "{F} ¿Cuántos Mbps consumen esos usuarios activos, a 2 Mbps cada uno?", "20*2", "Se multiplican los usuarios activos por lo que usa cada uno.", " Mbps"),
        ("=", "{F} ¿Cuántos Mbps suman las 8 videollamadas de 3 Mbps?", "8*3", "Se multiplican las videollamadas por lo que usa cada una.", " Mbps"),
        ("=", "{F} ¿Cuántos Mbps necesita la oficina en total en la hora de mayor uso?", "20*2+8*3", "Se suma el tráfico de los usuarios activos y el de las videollamadas.", " Mbps"),
        ("abc", "{F} Con 64 Mbps esperados y la regla del 70 %, ¿cuál es el enlace de menor tamaño que sirve?", "100 Mbps", "50 Mbps", "200 Mbps", "El de 50 Mbps no alcanza y el de 100 Mbps permite hasta 70 Mbps."),
        ("=", "{F} ¿Cuántos puertos por cable necesita la oficina para computadores, impresoras y teléfonos IP?", "40+5+6", "Se suma un puerto por cada equipo conectado.", " puertos"),
        ("abc", "{F} ¿Basta un switch de 48 puertos para esos equipos?", "No, porque se necesitan 51 puertos", "Sí, porque 48 es mayor que 40", "Sí, porque las impresoras no usan puerto", "Con 51 equipos por cable se superan los 48 puertos."),
        ("=", "{F} Si se usan dos switches de 48 puertos, ¿cuántos puertos quedan libres tras conectar los 51 equipos?", "2*48-51", "Se restan los equipos conectados a los puertos totales.", " puertos"),
        ("abc", "{F} Un colega calcula con los 40 usuarios activos (40 por 2 más 24 de videollamadas, 104 Mbps) y recomienda 200 Mbps. ¿Cuál es el error?", "Usó a todos los usuarios como activos, aunque solo lo está el 50 %", "Olvidó las videollamadas", "Usó la regla del 70 %", "El cliente informó que solo la mitad de los usuarios está activa a la vez."),
        ("abc", "{F} Con 64 Mbps y un enlace de 100 Mbps, ¿se cumple la regla del 70 %?", "Sí, porque 64 es menor que 70", "No, porque 64 es mayor que 50", "No, porque faltan las impresoras", "El 70 % de 100 es 70 y 64 no lo supera."),
    ],
    ctx=("abc", "El dueño de la constructora de ejemplo dice: «pongamos 200 Mbps por si acaso». ¿Qué responde el técnico?", "Que con 64 Mbps esperados un enlace de 100 Mbps cumple la regla y que 200 solo se justifica si se espera crecer", "Que no se puede calcular", "Que 200 siempre es lo mejor", "La recomendación se apoya en los números y el dueño decide."),
    sc=[
        ("En Telecomunicaciones: ¿qué son los usuarios activos?", "Quienes usan la red a la vez en la hora de mayor uso", "Con ellos se calcula el tráfico esperado."),
        ("¿Qué se suma al tráfico de los usuarios?", "Las videollamadas simultáneas", "Cantidad de videollamadas por los Mbps de cada una."),
        ("¿Cuántos puertos necesita una oficina con 20 computadores y 2 impresoras?", "22 puertos", "Se suma un puerto por cada equipo conectado por cable."),
    ],
    op=("Una oficina de ejemplo tiene 30 usuarios, de los cuales el 40 % está activo a la vez, usando 3 Mbps cada uno; habrá 5 videollamadas simultáneas de 4 Mbps; hay 30 computadores, 3 impresoras y 4 teléfonos IP. Los enlaces son de 50, 100 y 200 Mbps y la regla pide no superar el 70 % del enlace. Calcula (a) el tráfico total, (b) el enlace que elegirías, (c) los puertos necesarios y si basta un switch de 48 puertos.",
        "(a) 40 % de 30 son 12 usuarios activos; 12 por 3 son 36 Mbps; 5 por 4 son 20 Mbps; el total es 56 Mbps. (b) El de 100 Mbps, porque 56 es menor que 70. (c) 30 más 3 más 4 son 37 puertos; basta un switch de 48 y quedan 11 libres.",
        ["calcula usuarios activos y tráfico total", "elige el enlace con la regla", "cuenta los puertos y concluye"],
        ["hoja con los cálculos y la conclusión"],
        ["usar todos los usuarios como activos", "olvidar las videollamadas", "no contar las impresoras ni los teléfonos"],
        "Pregunta: «¿cuántos usuarios están activos a la vez?». Si no responde, pídele que calcule el 40 % de 30."),
    reinforce="Calcula el tráfico de 10 usuarios activos de 2 Mbps y 2 videollamadas de 3 Mbps.",
    extend="Explica con un ejemplo inventado por qué se deja una reserva en el enlace de internet.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 8 (criterio técnico con datos de ejemplo, inventados). El «Taller Los Andes» (ficticio) necesita conectividad. Requisitos del cliente: tráfico esperado 64 Mbps; no más de 2 horas sin servicio cada 1.000 horas; costo mensual máximo $90.000; "
     "posible crecimiento: el tráfico podría subir un 25 %. Opciones de ejemplo: Opción 1: enlace de 100 Mbps, $60.000 al mes, disponibilidad 99 % (10 horas sin servicio cada 1.000). "
     "Opción 2: enlace de 100 Mbps con un enlace de respaldo, $85.000 al mes, disponibilidad 99,9 % (1 hora sin servicio cada 1.000). Opción 3: enlace de 300 Mbps, $110.000 al mes, disponibilidad 99 %. UPS de ejemplo: $120.000, un solo pago.")
build(
    O10, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: comparar opciones con los requisitos del cliente y justificar la elección.",
    prior=["Sé calcular el tráfico esperado y la disponibilidad.", "Sé comparar valores con un máximo o un mínimo.", "Sé multiplicar costos mensuales por 12."],
    explain=[
        "Elegir entre opciones es comparar cada una con los requisitos del cliente. Se arma una tabla con una fila por requisito y una columna por opción, y se marca si cumple. Un requisito obligatorio (como el tráfico, la disponibilidad o el presupuesto máximo) descarta la opción que no lo cumple. Entre las que quedan, se prefiere la que cumple con holgura y se explica por qué.",
        "Se revisan además la escalabilidad y los costos totales. Si el tráfico puede crecer un 25 %, se calcula el nuevo valor (25 % de 64 es 16, y el tráfico pasa a 80 Mbps) y se verifica que la opción lo soporte. El costo anual es el costo mensual por 12, más los pagos únicos, como una UPS. La decisión final la toma el cliente, con una propuesta honesta y escrita.",
        "La propuesta indica qué se recomienda, qué se descartó y por qué, con los números a la vista. Las cifras son de ejemplo y no representan precios reales de ningún proveedor. La instalación la hace personal autorizado. " + AVISO,
    ],
    vocab=[("requisito obligatorio", "condición que una opción debe cumplir sí o sí"), ("descartar", "dejar fuera una opción que no cumple un requisito obligatorio"), ("holgura", "diferencia a favor entre lo que ofrece una opción y lo que se pide"), ("costo anual", "costo mensual por 12 más los pagos únicos"), ("crecimiento", "aumento esperado del tráfico en el futuro")],
    worked=[
        ("Descartar por costo", "El presupuesto máximo de ejemplo es $50.000 al mes y una opción cuesta $70.000. ¿Se descarta?", ["Se compara 70.000 con el máximo 50.000.", "70.000 es mayor que 50.000."], "Sí, se descarta por costo"),
        ("Costo anual", "Una opción de ejemplo cuesta $20.000 al mes. ¿Cuánto cuesta al año?", ["Se multiplica por 12 meses.", "20.000 por 12."], "$240.000"),
    ],
    mistakes=[("Elegir la opción más barata aunque no cumpla la disponibilidad pedida.", "Un requisito obligatorio descarta la opción sin importar el precio.", "Primero descarta las que no cumplen y luego compara costos."),
              ("Olvidar sumar los pagos únicos al costo del primer año.", "Se subestima lo que el cliente pagará.", "Suma el costo mensual por 12 más los pagos únicos.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un requisito obligatorio?", "Una condición que la opción debe cumplir sí o sí", "Una condición opcional", "Una idea del vendedor", "Si no se cumple, la opción se descarta."),
        ("abc", "En Telecomunicaciones: ¿qué significa descartar una opción?", "Dejarla fuera porque no cumple un requisito obligatorio", "Elegirla como la mejor", "Compararla de nuevo sin cambios", "Descartar es excluir la opción que no cumple."),
        ("abc", "¿Cómo se calcula el costo anual de una opción con pago mensual y un pago único?", "Costo mensual por 12 más el pago único", "Costo mensual más el pago único", "Costo mensual por 2", "Se anualiza el pago mensual y se suma lo único."),
        ("abc", "{F} ¿Qué opción no cumple el máximo de 2 horas sin servicio cada 1.000 horas?", "La opción 1, con 10 horas", "La opción 2, con 1 hora", "Ninguna", "Con disponibilidad de 99 % hay 10 horas sin servicio, más de 2."),
        ("abc", "{F} ¿Qué opción se descarta por superar el presupuesto de $90.000?", "La opción 3, de $110.000", "La opción 1, de $60.000", "La opción 2, de $85.000", "Los $110.000 superan el máximo mensual de $90.000 del presupuesto."),
        ("abc", "{F} ¿Qué opción cumple todos los requisitos obligatorios?", "La opción 2", "La opción 1", "La opción 3", "La opción 2 cumple tráfico, disponibilidad y presupuesto."),
        ("=", "{F} ¿Cuántos Mbps más se esperan si el tráfico sube un 25 % sobre 64 Mbps?", "64//4", "El 25 % es la cuarta parte de 64.", " Mbps"),
        ("=", "{F} ¿Cuál sería el tráfico total tras ese crecimiento, en Mbps?", "64+64//4", "Se suma el aumento al tráfico actual.", " Mbps"),
        ("abc", "{F} Con ese tráfico de 80 Mbps, ¿la opción 2 de 100 Mbps lo soporta?", "Sí, porque 80 es menor que 100", "No, porque 80 es mayor que 64", "No, porque la disponibilidad es 99,9 %", "100 Mbps cubren los 80 Mbps de la proyección."),
        ("=", "{F} ¿Cuánto cuesta al año la opción 2, en pesos?", "85000*12", "Se multiplica el costo mensual por 12.", ""),
        ("=", "{F} ¿Cuánto cuesta el primer año de la opción 2 si se agrega la UPS, en pesos?", "85000*12+120000", "Se suman el costo anual y el pago único de la UPS.", ""),
        ("abc", "{F} El vendedor de ejemplo oculta que la opción 2 tiene un costo único de instalación no informado. ¿Qué principio se rompe?", "La propuesta debe ser honesta y mostrar todos los costos", "El enlace debe ser mayor", "La opción 3 debe ser la elegida", "Ocultar costos engaña al cliente y rompe la honestidad de la propuesta."),
        ("abc", "{F} Un colega propone elegir la opción 1 «porque es la más barata». ¿Qué le responde el análisis?", "Que no cumple la disponibilidad pedida, por lo que queda descartada", "Que sí, que siempre se elige la más barata", "Que el costo no importa", "Un requisito obligatorio descarta la opción sin importar el precio."),
    ],
    ctx=("abc", "El dueño del taller de ejemplo pregunta si puede ahorrar quitando el enlace de respaldo de la opción 2. ¿Qué responde el técnico?", "Que se quedaría en la opción 1, que no cumple las horas máximas sin servicio, y que la decisión es suya", "Que sí, sin ningún efecto", "Que mejor elija la opción 3", "Quitar el respaldo cambia la disponibilidad; el dueño decide con la información."),
    sc=[
        ("En Telecomunicaciones: ¿qué se hace con una opción que no cumple un requisito obligatorio?", "Se descarta", "Aunque sea barata, no sirve para el cliente."),
        ("¿Cómo se calcula el costo anual de $10.000 al mes?", "$120.000", "Se multiplica el costo mensual por 12."),
        ("¿Quién toma la decisión final?", "El cliente, con una propuesta honesta", "El técnico entrega el análisis y el cliente decide."),
    ],
    op=("Una librería de ejemplo pide conectividad con estas condiciones: tráfico esperado 40 Mbps; máximo 3 horas sin servicio cada 1.000 horas; presupuesto máximo $50.000 al mes. Opciones: A, 50 Mbps, $35.000, 10 horas sin servicio; B, 50 Mbps con respaldo, $48.000, 1 hora sin servicio; C, 200 Mbps, $80.000, 1 hora sin servicio. Haz la tabla de cumplimiento, indica cuál recomendarías, calcula su costo anual y di si soporta un crecimiento del 25 % del tráfico (10 Mbps más).",
        "A no cumple las horas (10 mayor que 3). C supera el presupuesto ($80.000 mayor que $50.000). B cumple tráfico (50 mayor que 40), horas (1 menor que 3) y presupuesto ($48.000 menor que $50.000): se recomienda B. Costo anual: 48.000 por 12 son $576.000. Con 25 %, el tráfico sube 10 Mbps y llega a 50 Mbps, justo al límite del enlace: soporta, pero sin holgura.",
        ["arma la tabla de cumplimiento", "recomienda y calcula el costo anual", "evalúa el crecimiento con honestidad"],
        ["tabla con tres opciones y la recomendación"],
        ["elegir la más barata", "no revisar las horas sin servicio", "no mencionar la falta de holgura"],
        "Pregunta: «¿qué requisito descarta a la opción A y cuál a la C?». Si no responde, pídele que revise la tabla columna por columna."),
    reinforce="Haz una tabla de dos opciones de ejemplo y marca cuál cumple un presupuesto máximo de $40.000.",
    extend="Explica con un ejemplo inventado por qué una propuesta debe mostrar todos los costos, incluidos los pagos únicos.",
)

"""Conectividad y Redes TP 3.º y 4.º medio: OAE-04 (pruebas de conexión y señal), OAE-05 (seguridad informática en una LAN) y OAE-06 (recuperación de fallas y respaldos). Datos, direcciones y resultados inventados; sin equipos ni software."""
from __future__ import annotations

from tp_core_common import build

O4 = "TP-CORE-3y4-OAE-04"
O5 = "TP-CORE-3y4-OAE-05"
O6 = "TP-CORE-3y4-OAE-06"
AVISO = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (plan de pruebas de ejemplo, inventado) para la red de «Clínica Veterinaria Pellín». Pruebas previstas: de conexión (¿el equipo logra comunicarse?), de señal (¿qué calidad tiene la conexión?) y de rendimiento (velocidad, demora y pérdida). "
     "Puntos a probar: 5; cada punto tarda 12 minutos en probarse y entre punto y punto hay una pausa de 10 minutos (4 pausas). Instrumentos de ejemplo: probador de cableado, certificador de cable y medidor de potencia de fibra. "
     "Roles: técnico, jefa de proyecto, personal de la clínica. Las pruebas se hacen con aviso y autorización, porque pueden interrumpir el servicio.")
build(
    O4, 1, F,
    use="Aprenderé para qué sirven las pruebas de conexión y señal, quién participa, qué documentos dejan y qué riesgos tienen.",
    prior=["Sé qué es una red LAN y qué es un punto de red.", "Conozco los modelos OSI y TCP/IP.", "Sé sumar y multiplicar."],
    explain=[
        "Las pruebas de una red comprueban que lo instalado funciona y cumple lo pedido. La prueba de conexión revisa si un equipo logra comunicarse con otro. La prueba de señal mide la calidad de esa conexión, por ejemplo qué tan fuerte llega la señal. La prueba de rendimiento mide qué tan bien trabaja la red: velocidad, demora y pérdida de datos. Se usan instrumentos de medición y de certificación, y los resultados se comparan con las especificaciones técnicas.",
        "Todo se hace con un plan: qué se prueba, con qué instrumento, en qué horario y quién autoriza. Se avisa al personal porque una prueba puede interrumpir el servicio. Los resultados se anotan en un registro que sirve de evidencia. Al medir una red se revisa el estado de la conexión y no el contenido de lo que las personas envían: la privacidad se respeta siempre.",
        "Los riesgos más comunes son interrumpir la atención sin avisar, probar redes sin autorización, no registrar resultados y abrir equipos en funcionamiento. La luz de la fibra puede dañar los ojos y los equipos tienen electricidad, por lo que esas tareas son de personal autorizado." + AVISO,
    ],
    vocab=[("prueba de conexión", "comprobar si un equipo logra comunicarse con otro"), ("prueba de señal", "medir la calidad de la conexión"), ("rendimiento", "qué tan bien trabaja la red en velocidad, demora y pérdida"), ("certificación", "medición con instrumento que compara el enlace con la especificación"), ("registro de pruebas", "documento donde se anotan los resultados"), ("privacidad", "derecho a que no se revise lo que las personas envían")],
    worked=[
        ("Tiempo de pruebas", "Un plan de ejemplo prueba 3 puntos de 10 minutos cada uno. ¿Cuántos minutos tarda sin contar pausas?", ["Se multiplican los puntos por los minutos de cada uno.", "3 × 10 = 30."], "30 minutos"),
        ("Qué prueba usar", "Quieres saber si dos computadores de ejemplo pueden comunicarse entre sí. ¿Qué prueba corresponde?", ["La pregunta es si logran comunicarse.", "Eso lo responde la prueba de conexión."], "Prueba de conexión"),
    ],
    mistakes=[("Probar la red en plena atención al público sin avisar.", "La prueba puede cortar el servicio y perjudicar a las personas.", "Coordina un horario, avisa y obtén autorización."),
              ("Decir «ya probé, funciona» sin dejar registro.", "Sin evidencia nadie puede revisar ni repetir la comprobación.", "Anota punto, fecha, instrumento, resultado y responsable.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una prueba de conexión?", "Comprobar si un equipo logra comunicarse con otro", "Medir cuánto cuesta el cable", "Cambiar la clave de la red", "La prueba de conexión responde si hay comunicación entre dos equipos."),
        ("abc", "¿Para qué se registran los resultados de las pruebas?", "Para dejar evidencia que otra persona pueda revisar", "Para que el cable dure más", "Para que la red sea más rápida", "El registro es la evidencia de lo que se midió y de cómo se hizo."),
        ("abc", "¿Qué se hace antes de probar una red que está en servicio?", "Avisar y obtener autorización, y coordinar el horario", "Cortar la red sin avisar", "Probar solo de noche, sin permiso", "Las pruebas pueden interrumpir el servicio, por eso se avisan y se autorizan."),
        ("=", "{F} ¿Cuántos minutos duran las pruebas de los 5 puntos, sin contar las pausas?", "5*12", "Se multiplican los puntos por los minutos de cada uno.", " minutos"),
        ("abc", "{F} ¿Cuál prueba mide velocidad, demora y pérdida?", "La prueba de rendimiento", "La prueba de conexión", "La prueba de rotulado", "El rendimiento es lo que describe la velocidad, la demora y la pérdida."),
        ("abc", "{F} ¿Qué prueba responde si el equipo logra comunicarse?", "La prueba de conexión", "La prueba de rendimiento", "La certificación de fibra", "Comunicarse o no es la pregunta de la prueba de conexión."),
        ("=", "{F} Contando las 4 pausas de 10 minutos, ¿cuántos minutos dura en total la jornada de pruebas?", "5*12+4*10", "Se suman los minutos de prueba y los de pausa.", " minutos"),
        ("abc", "{F} El técnico quiere probar justo en la hora de mayor atención a los clientes. ¿Qué corresponde?", "Coordinar un horario con aviso para no interrumpir el servicio", "Probar igual y sin avisar", "Cortar la red a todos para que sea más rápido", "La atención se protege coordinando horario y avisando antes."),
        ("abc", "{F} Durante una prueba el técnico ve un mensaje personal en la pantalla de una persona. ¿Qué corresponde?", "No leerlo ni copiarlo: la prueba mide la red, no el contenido de las personas", "Leerlo para entender la falla", "Compartirlo con la jefa", "La privacidad exige no revisar lo que las personas envían."),
        ("abc", "Un técnico de ejemplo dice «ya probé todo, funciona», pero no anotó nada. ¿Qué falla en su trabajo?", "Falta evidencia: sin registro otra persona no puede verificar el resultado", "Falta cambiar el color del cable", "Falta apagar los equipos", "Sin registro no hay respaldo documental de la prueba."),
        ("abc", "Durante una prueba un compañero quiere abrir un equipo de red encendido «para ver por dentro». ¿Qué corresponde?", "No hacerlo: abrir equipos es tarea de personal autorizado y puede ser peligroso", "Abrirlo si usa guantes", "Abrirlo si nadie está mirando", "Los equipos tienen electricidad y partes sensibles: solo los abre quien está autorizado."),
        ("=", "{F} Si fueran 8 puntos con las mismas pausas entre cada uno (7 pausas), ¿cuántos minutos duraría la jornada?", "8*12+7*10", "Se suman los minutos de 8 pruebas y los de 7 pausas.", " minutos"),
        ("abc", "{F} ¿Qué debe contener el informe final de las pruebas?", "Los puntos probados, los resultados, el instrumento usado y el responsable", "Solo la opinión del técnico", "Los mensajes que vio en las pantallas", "El informe se apoya en datos verificables y deja constancia de quién midió."),
    ],
    ctx=("abc", "La dueña de la clínica pide que pruebes la red «ahora mismo», en plena atención. Tú sabes que la prueba corta el servicio unos minutos. ¿Qué haces?", "Le explico el efecto, propongo un horario con aviso y registro la autorización", "Pruebo igual sin decir nada", "Me niego sin explicar", "Se informa del efecto y se acuerda un horario; así se protege el servicio y se deja constancia."),
    sc=[
        ("En Conectividad y Redes: ¿qué mide la prueba de rendimiento?", "Velocidad, demora y pérdida de datos", "Describe qué tan bien trabaja la red en uso."),
        ("¿Qué haces con los mensajes de las personas durante una prueba?", "No los reviso: respeto la privacidad", "La prueba mide la red, no el contenido de las personas."),
        ("¿Qué debe llevar el registro de una prueba?", "Punto, fecha, instrumento, resultado y responsable", "Con esos datos la prueba se puede revisar."),
    ],
    op=("Un gimnasio de ejemplo necesita probar 6 puntos de red; cada prueba tarda 15 minutos y entre un punto y otro hay una pausa de 5 minutos. Calcula cuánto dura la jornada, escribe a quién avisarías y qué regla de privacidad respetarías, y arma una fila de registro para el primer punto con los campos de la ficha.",
        "Pruebas: 6 × 15 = 90 minutos. Pausas: 5 × 5 = 25 minutos. Total: 115 minutos. Avisaría a la administradora y al personal del gimnasio. Regla: no reviso el contenido de lo que envían las personas. Registro del punto 1: punto P-01; fecha de ejemplo; instrumento de ejemplo; resultado pendiente; responsable: yo.",
        ["calcula bien la jornada con pausas", "nombra a quién avisa y una regla de privacidad", "arma un registro con los campos pedidos"],
        ["hoja con el cálculo, el aviso y la fila de registro"],
        ["olvidar las pausas (5 y no 6)", "no mencionar la privacidad", "dejar el registro sin responsable"],
        "Pregunta: «¿cuántas pausas hay con 6 puntos?». Si responde 6, pídele que dibuje los puntos y cuente los espacios entre ellos."),
    reinforce="Inventa un plan de pruebas de tres puntos con tiempo por punto y una pausa entre ellos, y calcula la duración total.",
    extend="Explica por qué una prueba bien registrada ayuda a otra persona del equipo que no estuvo presente.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (glosario y umbrales de ejemplo). Umbrales de ejemplo del proyecto: demora (latencia) máxima de 20 ms; pérdida de paquetes máxima de 1 %; rendimiento mínimo de 90 Mbps en un enlace de 100 Mbps. "
     "Mbps = megabits por segundo; ms = milésimas de segundo; 1 byte = 8 bits (por eso 1 MB, megabyte, son 8 Mb, megabits). Ping: prueba que envía mensajes cortos y mide cuánto tardan en volver y si vuelven. "
     "Instrumentos: el probador de cableado revisa que los hilos estén bien conectados; el certificador mide longitud, atenuación y otras magnitudes y emite «pasa» o «falla»; el medidor de potencia óptica mide la luz que llega por una fibra.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de las mediciones de una red (latencia, pérdida, Mbps), los instrumentos y los documentos donde se registran.",
    prior=["Sé qué son las pruebas de conexión, señal y rendimiento.", "Sé calcular porcentajes sencillos.", "Sé qué es un enlace."],
    explain=[
        "Las pruebas de rendimiento usan unidades precisas. La latencia es la demora en milisegundos (ms) que tarda un mensaje en ir y volver. El ancho de banda es la capacidad de un enlace, medida en megabits por segundo (Mbps). El rendimiento real es lo que realmente se logra, que casi siempre es menor que la capacidad. La pérdida de paquetes es el porcentaje de mensajes que no llegan.",
        "La prueba más conocida es el ping: envía mensajes cortos a otro equipo y mide si vuelven y cuánto tardan. Sirve para comprobar conexión y demora, pero no mide la calidad del cable. Eso lo hacen los instrumentos: el probador de cableado revisa que los hilos estén bien conectados; el certificador mide longitud y atenuación y entrega un informe de pasa o falla; el medidor de potencia óptica mide la luz en una fibra.",
        "Cada resultado se compara con un umbral, que es el valor límite fijado por las especificaciones técnicas. El registro de pruebas anota el punto, el instrumento, el resultado y si pasa o falla. Un instrumento solo da un dato; la decisión la toma la persona con ese dato y la especificación." + AVISO,
    ],
    vocab=[("latencia", "demora que tarda un mensaje en ir y volver, en milisegundos"), ("ancho de banda", "capacidad de un enlace, medida en Mbps"), ("Mbps", "megabits por segundo"), ("pérdida de paquetes", "porcentaje de mensajes que no llegan"), ("ping", "prueba que mide si un mensaje vuelve y cuánto tarda"), ("umbral", "valor límite que fija la especificación"), ("certificador", "instrumento que mide un enlace y emite pasa o falla")],
    worked=[
        ("Pasar de MB a Mb", "¿Cuántos megabits son 20 megabytes?", ["1 byte son 8 bits, así que 1 MB son 8 Mb.", "20 × 8 = 160."], "160 Mb"),
        ("Porcentaje de pérdida", "En una prueba de ejemplo se envían 100 paquetes y vuelven 97. ¿Qué porcentaje se perdió?", ["Se perdieron 100 − 97 = 3 paquetes.", "3 de 100 son 3 %."], "3 %"),
    ],
    mistakes=[("Creer que si el ping responde, el cable está certificado.", "El ping muestra que hay comunicación, pero no mide longitud ni atenuación.", "Para certificar un enlace se usa un certificador y se archiva su informe."),
              ("Confundir Mb con MB al calcular tiempos.", "El megabyte tiene 8 veces más datos que el megabit.", "Convierte a las mismas unidades antes de dividir.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué mide la latencia?", "La demora que tarda un mensaje en ir y volver", "La cantidad de cables de un rack", "La longitud del cable", "La latencia se mide en milisegundos y expresa la demora."),
        ("abc", "En Conectividad y Redes: ¿qué significa Mbps?", "Megabits por segundo", "Metros por segundo", "Megabytes por semana", "Mbps es la unidad de capacidad de un enlace: megabits por segundo."),
        ("abc", "¿Qué es la pérdida de paquetes?", "El porcentaje de mensajes que no llegan a su destino", "El cable que se corta durante la obra", "La cantidad de equipos apagados", "Se expresa como porcentaje de lo enviado que no llegó."),
        ("abc", "{F} ¿Qué instrumento mide longitud y atenuación de un enlace de cobre y emite pasa o falla?", "El certificador", "El ping", "El medidor de potencia óptica", "El certificador es el instrumento de certificación; el ping es una prueba de mensajes."),
        ("abc", "{F} ¿Qué se puede saber con un ping?", "Si los mensajes vuelven y cuánto tardan", "La longitud exacta del cable", "El tipo de fibra instalada", "El ping mide conexión y demora, no la calidad física del cable."),
        ("=", "{F} ¿Cuántos megabits son 50 megabytes?", "50*8", "Cada megabyte equivale a 8 megabits.", " Mb"),
        ("=", "{F} A 100 Mbps, ¿cuántos segundos tardaría teóricamente en pasar un archivo de 50 MB (400 Mb)?", "400//100", "Se divide el tamaño en megabits por la capacidad en Mbps.", " segundos"),
        ("abc", "{F} Un punto mide 35 ms de demora. ¿Cumple el umbral?", "No: supera los 20 ms", "Sí, porque 35 es más que 20", "Sí, porque los milisegundos son pequeños", "El umbral es 20 ms como máximo y 35 lo supera."),
        ("=", "{F} Se enviaron 200 paquetes y volvieron 198. ¿Qué porcentaje se perdió?", "(200-198)*100//200", "Se calcula la parte perdida respecto del total enviado.", " %"),
        ("abc", "{F} Un enlace de 100 Mbps mide 60 Mbps de rendimiento real. ¿Cumple el umbral?", "No: debe medir al menos 90 Mbps", "Sí, porque 60 es menor que 100", "Sí, porque el enlace es de 100 Mbps", "El umbral exige un mínimo de 90 Mbps y 60 no lo alcanza."),
        ("abc", "Un técnico dice: «si el ping responde, el cable está certificado». ¿Qué falta en su razonamiento?", "El ping no mide longitud ni atenuación; para certificar se necesita un certificador", "Nada, porque el ping lo mide todo", "Falta cambiar el cable", "El ping muestra comunicación, no cumplimiento de la especificación."),
        ("abc", "{F} Resultados de un punto de ejemplo: demora 15 ms, pérdida 2 %, rendimiento 95 Mbps. ¿Qué umbral falla?", "Solo la pérdida de paquetes", "Solo la demora", "Solo el rendimiento", "La pérdida de 2 % supera el 1 % permitido; 15 ms y 95 Mbps cumplen."),
        ("=", "{F} Un ping de ejemplo devolvió tiempos de 12, 14, 11, 15 y 18 ms. ¿Cuál es el promedio?", "(12+14+11+15+18)//5", "Se suman los tiempos y se divide por la cantidad de mensajes.", " ms"),
    ],
    ctx=("abc", "Un cliente de ejemplo se queja de que «internet está lento». Tú mides 18 ms de demora, 0 % de pérdida y 93 Mbps de rendimiento en un enlace de 100 Mbps. ¿Qué concluyes?", "Los tres valores cumplen los umbrales: la lentitud debe buscarse en otra parte, por ejemplo en el servicio al que accede", "La red está mal porque no llega a 100 Mbps", "El cable está roto", "Los valores cumplen los umbrales; se amplía el análisis sin culpar a la red de entrada."),
    sc=[
        ("En Conectividad y Redes: ¿cuántos megabits tiene un megabyte?", "8", "Un byte equivale a 8 bits."),
        ("En una prueba de red: ¿qué es un umbral?", "El valor límite fijado por la especificación técnica", "Cada resultado se compara con el umbral para decidir si pasa."),
        ("¿Qué instrumento certifica un enlace de cobre?", "El certificador", "Mide longitud y atenuación y emite pasa o falla."),
    ],
    op=("Un taller de ejemplo recibe estos resultados de un punto: demora 22 ms, pérdida 0,5 % (equivale a 1 paquete perdido de cada 200), rendimiento 92 Mbps en un enlace de 100 Mbps. Usa los umbrales de la ficha 2 para decir qué mediciones cumplen y cuáles no, y calcula en segundos cuánto tardaría teóricamente en pasar un archivo de 25 MB a 100 Mbps.",
        "Demora: 22 ms supera 20 ms, no cumple. Pérdida: 0,5 % es menor que 1 %, cumple. Rendimiento: 92 Mbps es mayor que 90 Mbps, cumple. Archivo: 25 × 8 = 200 Mb; 200 ÷ 100 = 2 segundos.",
        ["compara cada valor con su umbral", "convierte MB a Mb y calcula el tiempo", "concluye cuál falla"],
        ["tabla de tres filas con medición, umbral y resultado, más el cálculo del tiempo"],
        ["dividir sin convertir MB a Mb", "decir que la demora cumple", "confundir el umbral de pérdida con el de demora"],
        "Pregunta: «¿por qué conviertes 25 MB a megabits?». Si no puede decirlo, repasa 1 byte = 8 bits."),
    reinforce="Convierte tres tamaños de archivo inventados de MB a Mb y calcula cuánto tardan a 100 Mbps.",
    extend="Explica por qué el rendimiento real casi nunca es igual a la capacidad del enlace.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (informe de pruebas de ejemplo, inventado) de 6 puntos de la «Biblioteca Municipal de Ejemplo». Límites del proyecto: longitud máxima 90 m; mapa de cableado OK; demora máxima 20 ms; pérdida máxima 1 %. "
     "P-01: mapa OK, 40 m, 8 ms, 0 %. P-02: mapa OK, 92 m, 10 ms, 0 %. P-03: mapa FALLA, 55 m, 12 ms, 0 %. P-04: mapa OK, 70 m, 25 ms, 0 %. P-05: mapa OK, 85 m, 9 ms, 3 %. P-06: mapa OK, 60 m, 14 ms, 1 %. Un punto «pasa» si cumple los cuatro límites.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un informe de pruebas: decidir qué puntos pasan, por qué falla cada uno y qué hacer sin alterar los resultados.",
    prior=["Conozco los umbrales de demora, pérdida y longitud.", "Sé qué es un certificador.", "Sé calcular promedios exactos."],
    explain=[
        "Un informe de pruebas se lee punto por punto. Para cada punto se comparan los resultados con los límites del proyecto. Un punto pasa solo si cumple todos los límites; si incumple uno, falla, aunque los demás estén bien. El mapa de cableado revisa que los hilos estén conectados en el orden correcto y sin cortes ni cruces; si falla, el punto no sirve hasta corregirlo.",
        "Al analizar, se anota cuál límite incumple cada punto y qué acción corresponde: revisar la conexión, revisar el recorrido si la longitud supera el límite, o estudiar la causa de la demora o la pérdida. Después de corregir, el punto se vuelve a probar y se registra la nueva medición. Los resultados originales no se borran ni se cambian.",
        "Alterar un resultado para que el punto «pase» es una falta grave de ética profesional: el informe pierde valor y las personas podrían trabajar con una red que no cumple. Si un dato no se pudo medir, se declara como pendiente. Los datos de esta clase son de ejemplo." + AVISO,
    ],
    vocab=[("mapa de cableado", "revisión de que los hilos están bien conectados"), ("pasa / falla", "resultado de comparar el punto con todos los límites"), ("causa probable", "explicación más razonable de una falla según los datos"), ("nueva prueba", "medición repetida después de corregir"), ("pendiente", "dato que aún no se mide")],
    worked=[
        ("Pasa o falla", "Un punto de ejemplo mide 60 m, 15 ms y 0 % de pérdida, con mapa OK. Los límites son 90 m, 20 ms y 1 %. ¿Pasa?", ["60 m cumple 90 m, 15 ms cumple 20 ms y 0 % cumple 1 %.", "Además el mapa está OK: cumple los cuatro límites."], "Sí, pasa"),
        ("Qué hacer con una falla", "Un punto falla porque su mapa de cableado es FALLA. ¿Qué corresponde?", ["Se registra la falla sin cambiar el resultado.", "Se corrige la conexión por personal autorizado y se vuelve a probar."], "Corregir y probar de nuevo, sin alterar el registro"),
    ],
    mistakes=[("Cambiar un resultado de «falla» a «pasa» porque la diferencia es pequeña.", "Alterar un dato rompe la confianza del informe y puede dejar una red defectuosa.", "Registra el valor real y propone una corrección."),
              ("Entregar el informe como si estuviera completo cuando falta medir un punto.", "Se oculta información y las decisiones se apoyan en datos incompletos.", "Marca el punto como pendiente y declara la falta.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué revisa el mapa de cableado?", "Que los hilos estén conectados en el orden correcto y sin cortes ni cruces", "Cuánto cuesta el cable", "El nombre del cliente", "El mapa de cableado verifica la correcta conexión de cada hilo."),
        ("abc", "¿Qué es un umbral o límite del proyecto?", "El valor que fija hasta dónde una medición se considera aceptable", "El color del cable", "El nombre del instrumento", "Cada medición se compara con el límite para decidir si cumple."),
        ("abc", "¿Qué significa que un punto «pasa» la certificación?", "Que sus mediciones cumplen todos los límites del proyecto", "Que el cable es nuevo", "Que se probó una sola vez", "Pasa solo si cumple todos los límites, no solo algunos."),
        ("abc", "{F} ¿Qué puntos pasan los cuatro límites?", "P-01 y P-06", "P-01 y P-02", "P-04 y P-05", "P-02, P-03, P-04 y P-05 incumplen un límite; P-01 y P-06 cumplen todos."),
        ("abc", "{F} ¿Por qué falla P-02?", "Porque mide 92 m y el límite es 90 m", "Porque su demora es alta", "Porque su mapa de cableado falla", "Según la ficha, P-02 tiene buen mapa y buena demora, pero supera la longitud permitida."),
        ("abc", "{F} ¿Qué límite incumple P-04?", "La demora: 25 ms supera 20 ms", "La longitud", "La pérdida", "P-04 tiene longitud y pérdida correctas, pero su demora es mayor que el máximo."),
        ("=", "{F} ¿Cuántos puntos fallan al menos un límite?", "6-2", "A los seis puntos se les restan los dos que pasan.", " puntos"),
        ("=", "{F} ¿Cuál es el promedio de longitud de los seis puntos?", "(40+92+55+70+85+60)//6", "Se suman los seis largos y se divide por seis.", " metros"),
        ("abc", "{F} P-06 tiene pérdida de 1 % y el límite es 1 % como máximo. ¿Qué corresponde?", "Cumple ese límite, porque el límite es un máximo y 1 % no lo supera", "No cumple, porque 1 % es igual al límite", "No se puede decidir nunca", "Un límite máximo permite el valor igual al límite."),
        ("abc", "{F} El técnico quiere anotar «pasa» en P-05 «porque 3 % es poco». ¿Qué corresponde?", "No alterar el resultado: se registra la falla y se propone una corrección", "Anotar «pasa» para entregar a tiempo", "Borrar la fila de P-05", "Los resultados reales no se cambian; la falla se registra y se corrige."),
        ("abc", "{F} Si la medición de P-03 mostró un mapa FALLA, ¿qué corresponde después de corregir?", "Probarlo de nuevo y registrar la nueva medición sin borrar la anterior", "Dar el punto por aprobado sin probar", "Cambiar la fila anterior por la nueva", "Corregir exige repetir la prueba y dejar el historial."),
        ("abc", "{F} ¿Cuál es la conclusión correcta del informe?", "Solo 2 de 6 puntos pasan; los otros cuatro requieren corrección y nueva prueba", "Todos pasan porque la mayoría tiene buen mapa", "Ninguno pasa", "Hay dos puntos que cumplen todo y cuatro que incumplen algún límite."),
        ("=", "{F} Si se corrigen P-02 y P-03 y ambos pasan en la nueva prueba, ¿cuántos puntos pasan en total?", "2+2", "A los dos puntos que ya pasan se suman los dos corregidos.", " puntos"),
    ],
    ctx=("abc", "La jefa necesita el informe hoy, pero todavía no se mide el punto P-07. ¿Qué haces?", "Entrego el informe marcando P-07 como pendiente, sin inventar el resultado", "Anoto un resultado parecido al de los otros puntos", "Retraso todo el informe sin avisar", "Un dato no medido se declara pendiente; inventarlo es una falta de ética."),
    sc=[
        ("En Conectividad y Redes: ¿cuándo pasa un punto?", "Cuando cumple todos los límites del proyecto", "Si incumple uno solo, el punto falla."),
        ("¿Qué haces con un resultado que falla?", "Lo registro tal cual y propongo una corrección", "No se altera el dato; se corrige y se vuelve a probar."),
        ("¿Qué haces con un punto que aún no se midió?", "Lo marco como pendiente", "Declarar lo que falta mantiene la confianza en el informe."),
    ],
    op=("Un colegio de ejemplo recibe estos resultados (límites: 90 m, 20 ms, 1 %, mapa OK). A-1: OK, 50 m, 10 ms, 0 %. A-2: OK, 88 m, 21 ms, 0 %. A-3: FALLA, 30 m, 5 ms, 0 %. A-4: OK, 75 m, 18 ms, 2 %. Indica qué puntos pasan, por qué falla cada uno de los demás y cuál es la acción recomendada, sin cambiar ningún resultado.",
        "Pasa solo A-1. A-2 falla por demora (21 ms supera 20 ms). A-3 falla por mapa de cableado. A-4 falla por pérdida (2 % supera 1 %). Acción: registrar las fallas tal cual, corregir las causas con personal autorizado y probar de nuevo, dejando el historial.",
        ["identifica qué puntos pasan", "explica el límite incumplido de cada falla", "propone acciones sin alterar resultados"],
        ["tabla de cuatro filas con resultado, causa y acción"],
        ["considerar que A-2 pasa porque está cerca del límite", "cambiar un resultado", "olvidar el mapa de A-3"],
        "Pregunta: «¿por qué A-2 falla si está tan cerca?». Si duda, recuérdale que el límite es 20 ms y 21 ms lo supera."),
    reinforce="Con una tabla inventada de tres puntos, marca cuáles pasan y cuáles fallan con los mismos límites.",
    extend="Explica por qué un registro con resultados reales, aunque sean malos, es más valioso que uno 'bonito'.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (caso de lentitud, de ejemplo). Una oficina tiene 25 computadores que se conectan por un switch al servidor de archivos mediante un único enlace de 100 Mbps. "
     "En hora punta todos usan el servidor a la vez y el enlace se reparte en partes iguales. Opciones: A) cambiar el enlace del servidor a 1.000 Mbps, costo de ejemplo $90.000; B) pedir a los usuarios que no usen el servidor entre las 10:00 y las 11:00, sin costo; "
     "C) comprar un servidor más potente, costo de ejemplo $800.000, que mantiene el enlace de 100 Mbps. Meta del proyecto: al menos 20 Mbps por computador en hora punta.")
build(
    O4, 4, F,
    use="Aprenderé a encontrar un cuello de botella con mediciones y a recomendar una mejora de rendimiento con datos, costo y límites.",
    prior=["Sé qué es el ancho de banda y los Mbps.", "Sé convertir MB a Mb.", "Sé dividir y comparar."],
    explain=[
        "Optimizar el rendimiento de una red es mejorar su desempeño para que cumpla una meta, por ejemplo una velocidad mínima por equipo. Primero se busca el cuello de botella, que es el punto de menor capacidad por el que pasa todo el tráfico: la red completa rinde como su tramo más lento. Mejorar otra parte no ayuda si el cuello de botella sigue igual.",
        "Cuando varios equipos comparten un enlace, la capacidad por equipo es aproximadamente la capacidad del enlace dividida en partes iguales entre los equipos que lo usan a la vez. Con esos datos se compara cada opción con la meta y se consideran el costo y los efectos. Una medida que no cambia el cuello de botella puede aliviar un momento, pero no asegura la meta.",
        "Una recomendación técnica muestra el cálculo, compara con la meta y declara su límite: los valores son de ejemplo, se confirman con mediciones reales antes y después del cambio, y la decisión final la toma la persona responsable del presupuesto y de la norma vigente.",
    ],
    vocab=[("cuello de botella", "tramo de menor capacidad por el que pasa todo el tráfico"), ("optimizar", "mejorar el desempeño para cumplir una meta"), ("hora punta", "momento de mayor uso de la red"), ("meta", "valor mínimo de rendimiento que se quiere lograr"), ("reparto en partes iguales", "dividir la capacidad entre los equipos que usan el enlace")],
    worked=[
        ("Capacidad por equipo", "Un enlace de ejemplo de 60 Mbps lo usan 10 equipos a la vez en partes iguales. ¿Cuántos Mbps tiene cada uno?", ["Se divide la capacidad entre los equipos.", "60 ÷ 10 = 6."], "6 Mbps por equipo"),
        ("Identificar el cuello de botella", "Un servidor de ejemplo tiene conexión de 100 Mbps, pero el enlace entre switches es de 10 Mbps. ¿Dónde está el cuello de botella?", ["Todo el tráfico entre switches pasa por el enlace de 10 Mbps.", "Es el tramo de menor capacidad."], "En el enlace de 10 Mbps"),
    ],
    mistakes=[("Comprar un servidor más potente cuando el problema es el enlace.", "El cuello de botella sigue igual y se gasta dinero sin lograr la meta.", "Mide primero y mejora el tramo de menor capacidad."),
              ("Medir una sola vez a una hora tranquila.", "La lentitud aparece en la hora punta; una medición fuera de ella engaña.", "Mide en hora punta y repite en varios días.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un cuello de botella?", "El tramo de menor capacidad por el que pasa todo el tráfico", "El cable más caro de la red", "El equipo más moderno", "Un cuello de botella limita a toda la red según su capacidad."),
        ("abc", "En Conectividad y Redes: ¿qué significa optimizar el rendimiento?", "Mejorar el desempeño para cumplir una meta medible", "Cambiar todos los equipos aunque no haga falta", "Apagar la red en hora punta", "Optimizar tiene un fin: lograr un desempeño medido frente a una meta."),
        ("abc", "¿Qué es el ancho de banda de un enlace?", "La capacidad máxima de datos por segundo que puede transportar", "El largo del cable", "El número de puertos del switch", "El ancho de banda indica cuánto cabe por segundo en el enlace."),
        ("=", "{F} Con el enlace actual de 100 Mbps y 25 computadores a la vez, ¿cuántos Mbps tiene cada uno?", "100//25", "Se divide la capacidad del enlace entre los computadores.", " Mbps"),
        ("abc", "{F} ¿Se cumple hoy la meta de 20 Mbps por computador?", "No: cada uno tiene 4 Mbps", "Sí: 100 Mbps alcanza", "Sí: son 20 Mbps cada uno", "Con 25 computadores a la vez, cada uno recibe solo 4 Mbps y la meta es 20."),
        ("=", "{F} Con la opción A (enlace de 1.000 Mbps), ¿cuántos Mbps tiene cada computador?", "1000//25", "Se divide el nuevo enlace entre los 25 computadores.", " Mbps"),
        ("abc", "{F} ¿Qué opción cumple la meta y cuánto cuesta?", "La opción A, con $90.000", "La opción B, con $0", "La opción C, con $800.000", "Solo A aumenta la capacidad del enlace, que es el cuello de botella."),
        ("=", "{F} Con la opción A, ¿cuántos Mbps por computador sobran sobre la meta?", "1000//25-20", "Se resta la meta a la capacidad por computador.", " Mbps"),
        ("=", "{F} Con la opción A (40 Mbps por computador), ¿cuántos segundos tarda un computador en descargar un archivo de 100 MB?", "100*8//40", "Se convierten 100 MB a megabits y se dividen por la velocidad.", " segundos"),
        ("abc", "{F} Un jefe propone C porque «más potente es mejor». ¿Qué respondes?", "El cuello de botella es el enlace de 100 Mbps y C no lo cambia, por lo que no se logra la meta", "Tiene razón, un servidor potente soluciona todo", "C es mejor porque cuesta más", "Un servidor más potente no aumenta la capacidad del enlace compartido."),
        ("abc", "{F} La opción B no cuesta nada. ¿Por qué no basta?", "No aumenta la capacidad del enlace y no asegura la meta en hora punta", "Porque la norma la prohíbe", "Porque hace más lenta la red", "Pedir menos uso alivia un momento, pero la capacidad por equipo sigue igual."),
        ("=", "{F} Con un enlace de 1.000 Mbps, ¿cuántos computadores podrían usar el servidor a la vez manteniendo 20 Mbps cada uno?", "1000//20", "Se divide la capacidad por la meta de cada computador.", " computadores"),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación de elegir A?", "Los valores son de ejemplo y se confirman con mediciones reales antes y después del cambio", "Ninguno, porque el cálculo es perfecto", "Que no hace falta medir de nuevo", "Un cálculo en papel debe confirmarse con mediciones reales."),
    ],
    ctx=("abc", "La jefa dice: «los usuarios se quejan, compremos lo más caro». Tú mediste que el enlace del servidor está al máximo en hora punta. ¿Qué respondes?", "Que la medición muestra un cuello de botella en el enlace y que conviene mejorarlo antes de comprar otra cosa", "Que comprar lo más caro siempre sirve", "Que no se puede hacer nada", "La decisión se apoya en la medición del cuello de botella, no en el precio."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula la capacidad por equipo en un enlace compartido?", "Capacidad del enlace dividida entre los equipos que lo usan a la vez", "El reparto en partes iguales es una estimación sencilla."),
        ("¿Por qué medir en hora punta?", "Porque ahí aparece la lentitud real", "Una medición en hora tranquila puede ocultar el problema."),
        ("¿Qué es un cuello de botella?", "El tramo de menor capacidad por el que pasa todo el tráfico", "Limita el rendimiento de toda la red."),
    ],
    op=("Un colegio de ejemplo tiene 30 computadores que comparten un enlace de 150 Mbps al servidor. La meta es 10 Mbps por computador en hora punta. Opción 1: subir el enlace a 600 Mbps, costo de ejemplo $120.000. Opción 2: cambiar el servidor por uno más potente, $500.000, con el mismo enlace. Calcula los Mbps por computador de hoy y con cada opción, indica cuál cumple la meta y escribe una recomendación con un límite.",
        "Hoy: 150 ÷ 30 = 5 Mbps, no cumple. Opción 1: 600 ÷ 30 = 20 Mbps, cumple. Opción 2: sigue en 5 Mbps, no cumple. Recomiendo la opción 1 por $120.000. Límite: los valores son de ejemplo y se confirman con mediciones reales antes y después.",
        ["calcula la capacidad por computador", "compara con la meta", "recomienda con datos y límite"],
        ["hoja con cálculos, tabla y recomendación"],
        ["elegir la opción 2 por ser más cara", "dividir mal el enlace", "no declarar límite"],
        "Pregunta: «¿qué tramo limita la red?». Si no responde 'el enlace', pídele que explique el cuello de botella."),
    reinforce="Calcula cuántos Mbps tiene cada computador si 12 comparten un enlace de 96 Mbps.",
    extend="Explica por qué mejorar el tramo equivocado puede no cambiar el rendimiento.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 5 (colegio de ejemplo, inventado). «Colegio Costanera»: 40 computadores en una LAN y un servidor de notas. Incidentes observados en el año (de ejemplo): 10 correos de engaño (phishing), 5 programas dañinos detectados, 3 intentos de acceso adivinando claves y 2 pérdidas de datos por error; en total 20. "
     "Principios de la seguridad: confidencialidad (solo ve quien corresponde), integridad (los datos no se alteran sin autorización) y disponibilidad (los datos y servicios están cuando se necesitan). Roles: encargada de seguridad, técnico, usuarios. "
     "Riesgo de ejemplo = probabilidad (1 a 3) × impacto (1 a 3).")
build(
    O5, 1, F,
    use="Aprenderé qué amenazas tiene una red LAN, qué principios la protegen, quién tiene qué rol y qué límites éticos y legales hay.",
    prior=["Sé qué es una red LAN.", "Sé qué son los datos personales.", "Sé multiplicar y calcular porcentajes sencillos."],
    explain=[
        "La seguridad informática protege la información y los servicios de una red. Una amenaza es algo que puede causar daño, como un correo de engaño (phishing) que pide la clave, un programa dañino o alguien que adivina contraseñas. Una vulnerabilidad es una debilidad, como una clave débil o un equipo sin actualizar. El riesgo combina cuán probable es el daño y cuánto impacto tendría.",
        "Los tres principios son la confidencialidad, la integridad y la disponibilidad. Cada incidente afecta a alguno de ellos. Para proteger se combinan medidas: contraseñas largas y distintas, actualizaciones, antivirus, copias de respaldo, permisos mínimos y filtrado de tráfico. Nadie debe compartir su clave ni escribirla a la vista; ante un correo sospechoso se avisa a la encargada de seguridad sin abrir enlaces ni archivos.",
        "Las redes y los datos pertenecen a personas e instituciones. Según la ley vigente de protección de datos personales y la ley vigente sobre delitos informáticos, entrar o probar técnicas en una red ajena sin autorización puede ser delito. Por eso las pruebas de seguridad se hacen solo con autorización escrita de quien es responsable. Aquí se aprende a proteger, no a vulnerar.",
    ],
    vocab=[("amenaza", "algo que puede causar daño a la información o a la red"), ("vulnerabilidad", "debilidad que una amenaza podría aprovechar"), ("riesgo", "combinación de probabilidad e impacto de un daño"), ("phishing", "correo o mensaje de engaño que busca obtener datos"), ("confidencialidad", "que solo vea la información quien corresponde"), ("integridad", "que los datos no se alteren sin autorización"), ("disponibilidad", "que los datos y servicios estén cuando se necesitan")],
    worked=[
        ("Calcular un riesgo", "Una amenaza de ejemplo tiene probabilidad 2 e impacto 3. ¿Cuál es su riesgo?", ["Riesgo = probabilidad × impacto.", "2 × 3 = 6."], "Riesgo 6"),
        ("Principio afectado", "Una persona de ejemplo ve las notas de un curso que no le corresponde. ¿Qué principio se afecta?", ["Alguien vio información sin permiso.", "Eso afecta la confidencialidad."], "La confidencialidad"),
    ],
    mistakes=[("Pensar que «no tengo nada importante» en el computador.", "Hay datos personales de otras personas, como notas, que deben protegerse.", "Protege todo equipo como si guardara datos de terceros."),
              ("Probar si se puede entrar a la red del colegio «para ayudar», sin avisar.", "Probar sin autorización puede ser delito y producir daños.", "Ofrece tu ayuda a la encargada y haz pruebas solo con autorización escrita.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el phishing?", "Un mensaje de engaño que busca que entregues datos o claves", "Una copia de seguridad", "Un cable de red falso", "El phishing engaña a la persona para obtener información."),
        ("abc", "En Conectividad y Redes: ¿qué es una vulnerabilidad?", "Una debilidad que una amenaza podría aprovechar", "Una copia de seguridad", "Un permiso de acceso", "Una vulnerabilidad es una debilidad, por ejemplo una clave débil."),
        ("abc", "¿Qué protege la confidencialidad?", "Que solo vea la información quien corresponde", "Que los datos estén siempre disponibles", "Que el equipo sea rápido", "La confidencialidad limita el acceso a las personas autorizadas."),
        ("=", "{F} ¿Cuántos incidentes hubo en el año sumando los cuatro tipos de la ficha?", "10+5+3+2", "Se suman los incidentes de cada tipo.", " incidentes"),
        ("abc", "{F} Un correo falso que pide la clave de un docente ataca principalmente uno de los tres principios. ¿Cuál?", "La confidencialidad", "La integridad", "La disponibilidad", "El objetivo es que alguien no autorizado conozca la clave."),
        ("abc", "{F} Una persona cambia notas en el servidor sin autorización. ¿Qué principio se afecta?", "La integridad", "La confidencialidad", "La disponibilidad", "Se alteran los datos sin permiso, y eso afecta la integridad."),
        ("=", "{F} ¿Qué porcentaje de los 20 incidentes fueron correos de engaño?", "10*100//20", "Se calcula la parte de correos de engaño respecto del total.", " %"),
        ("=", "{F} El phishing tiene probabilidad 3 e impacto 2. ¿Cuál es su riesgo?", "3*2", "El riesgo es probabilidad por impacto.", ""),
        ("abc", "{F} Una persona usa la misma clave en todos sus servicios. ¿Cuál es el riesgo?", "Si se filtra una clave, quedan expuestos todos los servicios", "Se olvida la clave con más facilidad", "El servidor se vuelve más lento", "Repetir claves hace que una sola filtración abra muchas puertas."),
        ("abc", "{F} Un docente dice: «en mi computador no hay nada importante». ¿Qué respondes?", "Hay notas y datos personales de estudiantes que deben protegerse", "Tiene razón, no necesita protección", "Solo importa lo que hay en el servidor", "Los datos de estudiantes son personales y requieren protección."),
        ("abc", "Un estudiante propone «probar» si puede entrar al servidor del colegio sin avisar, «para ayudar». ¿Qué corresponde?", "No hacerlo; ofrecer ayuda a la encargada para pruebas autorizadas", "Hacerlo si no cambia nada", "Hacerlo a escondidas por la noche", "Entrar sin autorización puede ser delito aunque la intención sea buena."),
        ("abc", "{F} Llega un correo urgente que dice «tu cuenta se cierra, entra a este enlace y escribe tu clave». ¿Qué haces?", "No abro el enlace, no respondo y aviso a la encargada de seguridad", "Entro rápido para no perder la cuenta", "Reenvío el correo a todos mis compañeros", "El apuro y el enlace son señales de engaño; se avisa a quien corresponde."),
        ("abc", "{F} En una lista de riesgos, los errores humanos tienen probabilidad 3 e impacto 1; el phishing, 3 y 2; los programas dañinos, 2 y 3. ¿Cuál tiene el valor más bajo?", "Los errores humanos, con 3", "El phishing, con 6", "Los programas dañinos, con 6", "Los errores humanos tienen 3×1 = 3, menor que 6 y 6."),
    ],
    ctx=("abc", "Una compañera te cuenta que escribió su clave en un correo que parecía del colegio. ¿Qué le aconsejas?", "Avisar de inmediato a la encargada de seguridad y a una persona adulta, y cambiar su clave siguiendo las indicaciones", "Esperar a ver si pasa algo", "Pedirle que no cuente nada", "Avisar rápido reduce el daño; ocultarlo lo aumenta."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula un riesgo de ejemplo?", "Probabilidad por impacto", "Combina cuán probable es el daño y cuánto impacto tendría."),
        ("¿Qué haces ante un correo sospechoso?", "No abro enlaces ni archivos y aviso a la encargada de seguridad", "Evita entregar datos y permite que se revise el engaño."),
        ("¿Cuándo se hacen pruebas de seguridad?", "Solo con autorización escrita de quien es responsable de la red", "Probar sin autorización puede ser delito."),
    ],
    op=("Una biblioteca de ejemplo registró este año: 6 correos de engaño, 2 programas dañinos, 1 intento de acceso con claves adivinadas y 1 pérdida de datos por error. Calcula el total de incidentes y el porcentaje de correos de engaño, indica qué principio afecta el correo de engaño, y escribe dos reglas simples de buenas prácticas para el personal.",
        "Total: 6 + 2 + 1 + 1 = 10. Correos de engaño: 6 de 10, es decir 60 %. Afecta la confidencialidad. Reglas: usar contraseñas largas y distintas; no abrir enlaces ni archivos de correos sospechosos y avisar a la encargada.",
        ["calcula total y porcentaje", "relaciona con el principio correcto", "escribe dos buenas prácticas útiles"],
        ["hoja con cálculos, principio y dos reglas"],
        ["calcular el porcentaje sobre el dato equivocado", "confundir integridad con confidencialidad", "proponer una práctica que vulnere a otros"],
        "Pregunta: «¿por qué el correo de engaño afecta la confidencialidad?». Si no responde, repasa la definición del principio."),
    reinforce="Escribe tres buenas prácticas de contraseñas que explicarías a un familiar.",
    extend="Explica por qué pedir autorización escrita protege tanto a la institución como a la persona que hace las pruebas.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 6 (glosario y redes de ejemplo). Firewall: equipo o programa que filtra el tráfico según reglas. Filtrado de tráfico: permitir o bloquear comunicaciones según origen, destino y servicio. "
     "ACL (lista de control de acceso): lista ordenada de reglas «permitir» o «bloquear»; se leen de arriba hacia abajo, se aplica la primera que coincide y, si ninguna coincide, se bloquea. "
     "Segmentación: dividir la red en partes para limitar el daño. Mínimo privilegio: cada persona recibe solo los permisos que necesita. Autenticación de dos pasos: pedir una prueba adicional además de la clave. Registro (log): anotación automática de eventos. "
     "Redes de ejemplo: administración 192.168.10.0/24, estudiantes 192.168.30.0/24 (una red /24 admite 254 equipos) y servidor de notas 192.168.10.5.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario de los métodos de seguridad (firewall, ACL, segmentación, mínimo privilegio) y los documentos y roles que los acompañan.",
    prior=["Conozco las amenazas y los tres principios.", "Sé leer direcciones y máscaras.", "Sé que las pruebas de seguridad requieren autorización."],
    explain=[
        "Los métodos de seguridad actúan en capas, para que si una falla otra proteja. El filtrado de tráfico decide qué comunicaciones pasan: un firewall lo aplica según reglas que miran el origen, el destino y el servicio. Una lista de control de acceso (ACL) es una lista ordenada de esas reglas. Se lee de arriba hacia abajo; la primera regla que coincide decide, y si ninguna coincide, el tráfico se bloquea.",
        "La segmentación divide la red en partes, como la red de administración y la de estudiantes, para que un problema en una no pase a la otra. El principio de mínimo privilegio entrega a cada persona solo los permisos que necesita. La autenticación de dos pasos pide una prueba adicional a la clave. El registro (log) anota eventos para detectar y revisar problemas. Se suman las actualizaciones, el antivirus y las copias de respaldo.",
        "Los documentos de esta área son la política de seguridad (reglas de la institución), la tabla de reglas del firewall o de la ACL, y el registro de incidentes. Cada cambio de reglas lo aprueba la encargada de seguridad y se anota para poder revisarlo. Sin autorización, nadie cambia reglas de una red ajena.",
    ],
    vocab=[("firewall", "equipo o programa que filtra el tráfico según reglas"), ("ACL", "lista ordenada de reglas permitir o bloquear"), ("segmentación", "dividir la red en partes para limitar el daño"), ("mínimo privilegio", "dar solo los permisos necesarios"), ("autenticación de dos pasos", "pedir una prueba adicional además de la clave"), ("registro (log)", "anotación automática de eventos"), ("política de seguridad", "reglas de seguridad de una institución")],
    worked=[
        ("Orden de una ACL", "Una ACL de ejemplo tiene primero «permitir todo» y después «bloquear estudiantes». ¿Qué efecto tiene?", ["La regla de permitir todo coincide primero con cualquier tráfico.", "La regla de bloquear queda sin efecto."], "Se permite todo y el bloqueo no se aplica"),
        ("Mínimo privilegio", "Un docente solo debe ver las notas de su curso. ¿Qué permiso conviene darle?", ["Debe tener lo necesario para su trabajo y nada más.", "Se le da permiso de ver las notas de su curso."], "Ver solo las notas de su curso"),
    ],
    mistakes=[("Poner una regla de «permitir todo» al comienzo de la ACL.", "Como la primera coincidencia decide, anula las reglas de abajo.", "Ordena de lo más específico a lo más general y termina con el bloqueo."),
              ("Dar permisos de administrador a todo el personal «para ahorrar solicitudes».", "Un error o ataque tendría el máximo alcance.", "Aplica mínimo privilegio y revisa los permisos con regularidad.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un firewall?", "Un equipo o programa que filtra el tráfico según reglas", "Un cable que une dos redes", "Un programa para escribir documentos", "El firewall permite o bloquea comunicaciones según sus reglas."),
        ("abc", "En Conectividad y Redes: ¿qué es una ACL?", "Una lista ordenada de reglas de permitir o bloquear tráfico", "Una lista de contraseñas", "Un tipo de cable", "La ACL se compone de reglas leídas en orden."),
        ("abc", "¿Qué significa el principio de mínimo privilegio?", "Dar solo los permisos que cada persona necesita", "Dar permisos de administrador a todos", "No dar ninguna cuenta a nadie", "El mínimo privilegio limita el daño que puede causar una cuenta."),
        ("abc", "{F} ¿Cómo se lee una ACL?", "De arriba hacia abajo, y se aplica la primera regla que coincide", "De abajo hacia arriba", "Se aplican todas las reglas a la vez", "El orden importa porque la primera coincidencia decide."),
        ("abc", "{F} ¿Qué pasa con un tráfico que no coincide con ninguna regla?", "Se bloquea", "Se permite", "Se guarda para decidir después", "La ficha dice que si ninguna regla coincide el tráfico se bloquea."),
        ("abc", "{F} ¿Para qué sirve segmentar la red?", "Para limitar el daño si una parte tiene un problema", "Para que los equipos funcionen sin energía", "Para borrar el registro de eventos", "Dividir la red evita que un problema se extienda a todo."),
        ("=", "{F} La red de estudiantes admite 254 equipos y ya hay 40 computadores. ¿Cuántas direcciones quedan libres?", "254-40", "A las direcciones que admite la red se les restan las usadas.", " direcciones"),
        ("abc", "{F} Bajo el principio de mínimo privilegio, ¿quién debería poder editar las notas?", "Solo el personal autorizado de administración", "Todos los estudiantes", "Cualquier persona de la red", "Editar notas es una función restringida al personal que la necesita."),
        ("abc", "{F} Un profesor necesita ver las notas de su curso. ¿Qué permiso es adecuado?", "Ver solo las notas de su curso", "Administrar todo el servidor", "Ver y editar todas las notas del colegio", "Solo ver su curso es lo necesario para su trabajo."),
        ("abc", "{F} ¿Para qué sirve el registro (log) del servidor de notas?", "Para detectar y revisar eventos como accesos o cambios", "Para que el servidor sea más rápido", "Para borrar archivos viejos", "El registro deja evidencia que ayuda a investigar problemas."),
        ("abc", "{F} Una técnica pone «permitir todo» como primera regla de la ACL. ¿Qué efecto tiene?", "Anula las reglas de abajo que bloquean, porque la primera que coincide se aplica", "Hace más segura la red", "No cambia nada", "La primera regla coincide con todo y las siguientes no se evalúan."),
        ("abc", "{F} Una ACL tiene al final «permitir cualquiera hacia el servidor» y arriba «bloquear estudiantes hacia el servidor». ¿Se bloquea a los estudiantes?", "Sí: la regla de bloqueo aparece antes y coincide primero", "No: la regla de permitir anula la anterior", "Depende del color del servidor", "Las reglas se leen en orden y la primera coincidencia se aplica."),
        ("abc", "{F} ¿Qué enfoque protege mejor el servidor de notas?", "Combinar segmentación, reglas de acceso, claves fuertes y actualizaciones", "Confiar solo en una regla de firewall", "Confiar en que nadie intentará entrar", "Varias medidas en capas protegen aunque una falle."),
    ],
    ctx=("abc", "El director pide dar acceso total al servidor a todos los docentes «para no tener problemas». ¿Qué respondes?", "Que conviene dar a cada docente solo lo que necesita y registrar los accesos, por mínimo privilegio", "Que se hará sin revisar nada", "Que se dará acceso total y se quitarán las claves", "Dar solo lo necesario reduce el daño y deja registro."),
    sc=[
        ("En Conectividad y Redes: ¿qué ocurre si ninguna regla de la ACL coincide?", "Se bloquea el tráfico", "Esa es la regla final de la ficha."),
        ("¿Para qué sirve la segmentación?", "Para que un problema en una parte no pase a las otras", "Divide la red y limita el alcance del daño."),
        ("¿Qué es el mínimo privilegio?", "Dar solo los permisos necesarios", "Cada cuenta tiene un alcance acotado al trabajo de la persona."),
    ],
    op=("Un taller de ejemplo tiene tres tipos de usuarios: personal administrativo (puede ver y editar notas), docentes (pueden ver solo las notas de su curso) y estudiantes (no ven notas). Define el permiso de cada grupo, indica en qué orden pondrías tres reglas de una ACL (bloquear estudiantes hacia el servidor, permitir al personal administrativo hacia el servidor, bloquear todo lo demás) y explica por qué.",
        "Permisos: administrativo ve y edita; docentes ven solo su curso; estudiantes ninguno. Orden: 1) bloquear estudiantes hacia el servidor; 2) permitir al personal administrativo hacia el servidor; 3) bloquear todo lo demás. Se pone lo específico primero porque la primera regla que coincide decide, y el bloqueo final deja a la red cerrada por defecto.",
        ["asigna permisos mínimos", "ordena las reglas de lo específico a lo general", "justifica con la lectura de arriba hacia abajo"],
        ["tabla de permisos y lista numerada de reglas con la razón"],
        ["poner el bloqueo final al principio", "dar permisos de edición a docentes", "no justificar el orden"],
        "Pregunta: «¿qué pasaría si el bloqueo de todo lo demás fuera primero?». Si no lo sabe, pídele que simule un paquete con las reglas en ese orden."),
    reinforce="Escribe tres permisos mínimos para tres personas distintas de una oficina inventada.",
    extend="Explica por qué la segmentación y el mínimo privilegio se complementan.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 7 (ACL de ejemplo, inventada; se lee de arriba hacia abajo, se aplica la primera regla que coincide y, si ninguna coincide, se bloquea). "
     "Regla 1: PERMITIR origen 192.168.10.0/24 hacia 192.168.20.5, servicio web seguro (puerto 443). Regla 2: BLOQUEAR origen 192.168.30.0/24 hacia cualquier destino y servicio. "
     "Regla 3: PERMITIR cualquier origen hacia 192.168.20.5, servicio web (puerto 80). Regla final implícita: BLOQUEAR todo lo demás. «192.168.10.0/24» significa todas las direcciones que empiezan con 192.168.10. "
     "Paquetes de ejemplo: A) de 192.168.10.7 a 192.168.20.5, puerto 443; B) de 192.168.30.9 a 192.168.20.5, puerto 443; C) de 192.168.10.7 a 192.168.20.5, puerto 80; D) de 192.168.30.9 a 192.168.20.5, puerto 80; E) de 192.168.10.7 a 192.168.20.9, puerto 443.")
build(
    O5, 3, F,
    use="Aprenderé a evaluar paquetes de ejemplo contra una ACL, a ver cómo el orden cambia el resultado y a registrar la decisión.",
    prior=["Sé leer una ACL de arriba hacia abajo.", "Sé qué es una dirección IP y una red /24.", "Sé que cada cambio de reglas se aprueba y se registra."],
    explain=[
        "Evaluar un paquete contra una ACL es un proceso ordenado. Se toma el paquete, se mira su origen, su destino y su servicio (el puerto), y se compara con la regla 1. Si coincide en los tres datos, se aplica esa regla y se termina. Si no coincide, se pasa a la regla 2, y así hasta el final. Si ninguna regla coincide, el paquete se bloquea.",
        "El puerto es el número que identifica el servicio al que va el tráfico: en esta ficha el 443 es web segura y el 80 es web. Una dirección como 192.168.10.0/24 representa a todas las direcciones que empiezan con 192.168.10. El orden de las reglas es parte del diseño: si se cambia, un mismo paquete puede recibir un resultado distinto.",
        "En la práctica, toda ACL se prueba primero en papel, luego en un ambiente autorizado y con copia de la configuración, y nunca en una red en uso sin aviso. Cada cambio se registra con su fecha, quién lo aprobó y por qué. Los datos de esta clase son de ejemplo.",
    ],
    vocab=[("puerto (servicio)", "número que identifica el servicio al que va el tráfico"), ("origen", "dirección desde donde sale el tráfico"), ("destino", "dirección hacia donde va el tráfico"), ("regla implícita", "regla final no escrita que bloquea lo que no coincide"), ("coincidir", "cumplir origen, destino y servicio de una regla"), ("ventana de mantenimiento", "horario acordado para cambios en una red en uso")],
    worked=[
        ("Aplicar la primera regla", "Una ACL de ejemplo tiene: 1) PERMITIR de 10.0.0.0/24 a 10.1.1.5 por el puerto 443; 2) BLOQUEAR lo demás. Llega un paquete de 10.0.0.9 a 10.1.1.5, puerto 443. ¿Qué pasa?", ["Coincide con la regla 1 en origen, destino y puerto.", "Se aplica la regla 1 y se termina."], "Se permite"),
        ("Sin coincidencia", "En la misma ACL llega un paquete de 10.0.0.9 a 10.1.1.5 por el puerto 22. ¿Qué pasa?", ["No coincide con la regla 1 porque el puerto es distinto.", "Pasa a la regla 2, que bloquea lo demás."], "Se bloquea"),
    ],
    mistakes=[("Revisar solo el origen y olvidar el puerto.", "Una regla coincide únicamente si coinciden origen, destino y servicio.", "Compara los tres datos en cada regla."),
              ("Probar una ACL nueva directamente en la red en uso.", "Un error puede cortar el servicio o dejar la red abierta.", "Prueba en papel y en un ambiente autorizado, con copia de la configuración y ventana de mantenimiento.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué identifica el puerto de un servicio?", "El servicio al que va el tráfico", "El nombre de la persona usuaria", "El color del cable", "Cada servicio usa un número de puerto, como 443 para web segura en esta ficha."),
        ("abc", "En Conectividad y Redes: ¿qué significa 192.168.10.0/24?", "Todas las direcciones que empiezan con 192.168.10", "Solo la dirección 192.168.10.0", "Un cable de 24 metros", "El /24 indica que los tres primeros números identifican la red."),
        ("abc", "¿Qué es la regla implícita final de una ACL en esta ficha?", "Una regla no escrita que bloquea lo que no coincide con ninguna", "Una regla que permite todo", "Una regla que borra los registros", "Si ninguna regla coincide, el tráfico se bloquea."),
        ("abc", "{F} ¿Qué ocurre con el paquete A?", "Se permite por la regla 1", "Se bloquea por la regla 2", "Se bloquea por la regla implícita", "A viene de la red 192.168.10, va al servidor 192.168.20.5 por el puerto 443 y coincide con la regla 1."),
        ("abc", "{F} ¿Qué ocurre con el paquete B?", "Se bloquea por la regla 2", "Se permite por la regla 1", "Se permite por la regla 3", "B viene de la red 192.168.30; no coincide con la regla 1 y la regla 2 lo bloquea."),
        ("abc", "{F} ¿Qué ocurre con el paquete C?", "Se permite por la regla 3", "Se permite por la regla 1", "Se bloquea por la regla 2", "C no coincide con la regla 1 por el puerto, ni con la 2 por el origen; la regla 3 lo permite."),
        ("abc", "{F} ¿Por qué se bloquea el paquete D si la regla 3 permite la web a cualquier origen?", "Porque la regla 2 aparece antes y coincide primero", "Porque la regla 3 no existe", "Porque el puerto 80 está prohibido", "El orden importa: la regla 2 coincide primero con el origen 192.168.30."),
        ("abc", "{F} ¿Qué ocurre con el paquete E?", "Se bloquea por la regla implícita final", "Se permite por la regla 1", "Se permite por la regla 3", "Su destino es .9 y no .5, por lo que no coincide con las reglas 1 ni 3."),
        ("abc", "{F} De los cinco paquetes, ¿cuántos se permiten?", "2: A y C", "3: A, C y D", "1: solo A", "Se permiten A (regla 1) y C (regla 3); B, D y E se bloquean."),
        ("abc", "{F} Si se intercambiaran las reglas 2 y 3, ¿qué pasaría con el paquete D?", "Se permitiría, porque la regla 3 coincidiría primero", "Se bloquearía igual", "Se perdería sin registro", "Con la regla 3 antes, el puerto 80 hacia 192.168.20.5 se permite sin llegar a la regla 2."),
        ("abc", "{F} Alguien propone eliminar la regla 2 «porque molesta». ¿Qué efecto tendría sobre los cinco paquetes?", "Solo cambia D, que pasaría a permitirse por la regla 3", "Cambian todos los paquetes", "No cambia ninguno", "B seguiría bloqueado por la regla implícita, porque la regla 3 solo permite el puerto 80; solo D usa el puerto 80 desde esa red."),
        ("abc", "{F} Un informe dice que la regla 3 es poco segura. ¿Qué razón se puede dar?", "Permite web al servidor desde cualquier origen, y el mínimo privilegio sugiere limitar los orígenes", "Porque usa el puerto 80, que no existe", "Porque está después de la regla 1", "El permiso amplio a cualquier origen se revisa con el principio de mínimo privilegio."),
        ("abc", "{F} ¿Qué orden de reglas es más seguro?", "Bloqueos y permisos específicos primero y un bloqueo general al final", "Un «permitir todo» al comienzo", "Reglas sin ningún orden", "Lo específico antes de lo general y la red cerrada por defecto da más control."),
    ],
    ctx=("abc", "La encargada te pide probar una nueva ACL en la red del colegio en pleno horario de clases. ¿Qué haces?", "Propongo probarla primero en papel y en un ambiente autorizado, con copia de la configuración y una ventana de mantenimiento", "La pruebo ahora, sin copia", "La pruebo y no registro nada", "Un cambio en una red en uso se planifica, se respalda y se registra."),
    sc=[
        ("En Conectividad y Redes: ¿cuándo coincide un paquete con una regla?", "Cuando coinciden origen, destino y servicio", "Los tres datos deben coincidir para aplicar la regla."),
        ("¿Por qué importa el orden de las reglas?", "Porque se aplica la primera que coincide", "Cambiar el orden puede cambiar el resultado del mismo paquete."),
        ("¿Qué se registra al cambiar una ACL?", "Fecha, quién aprobó y el motivo", "El registro permite revisar y volver atrás."),
    ],
    op=("Una ACL de ejemplo dice: 1) PERMITIR de 172.16.5.0/24 a 172.16.9.2, puerto 443; 2) BLOQUEAR de 172.16.7.0/24 a cualquier destino; 3) PERMITIR de cualquier origen a 172.16.9.2, puerto 80; 4) BLOQUEAR lo demás (implícita). Evalúa estos paquetes: P1) de 172.16.5.4 a 172.16.9.2, puerto 443; P2) de 172.16.7.8 a 172.16.9.2, puerto 80; P3) de 172.16.5.4 a 172.16.9.2, puerto 80; P4) de 172.16.5.4 a 172.16.9.3, puerto 443. Indica la regla aplicada a cada uno.",
        "P1: se permite (regla 1). P2: se bloquea (regla 2, aunque la 3 lo permitiría). P3: se permite (regla 3). P4: se bloquea (implícita: el destino .3 no coincide con las reglas 1 ni 3). Se permiten 2 de los 4.",
        ["evalúa los cuatro paquetes con la regla correcta", "explica la importancia del orden con P2", "usa la regla implícita en P4"],
        ["tabla de cuatro filas con paquete, regla y resultado"],
        ["olvidar que la primera coincidencia decide", "no mirar el puerto", "no aplicar la regla final"],
        "Pregunta: «¿por qué P2 se bloquea si la regla 3 permite su puerto?». Si no sabe, pídele que recorra las reglas en orden."),
    reinforce="Escribe una ACL de tres reglas para una red de ejemplo y evalúa dos paquetes.",
    extend="Explica por qué cerrar la red por defecto es más seguro que abrirla por defecto.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 8 (matriz de riesgos de ejemplo). Riesgo = probabilidad (1 a 3) × impacto (1 a 3). R1 phishing a docentes: probabilidad 3, impacto 3. R2 programa dañino por memorias USB: probabilidad 2, impacto 2. "
     "R3 claves débiles en el servidor de notas: probabilidad 3, impacto 2. R4 pérdida de datos por error: probabilidad 1, impacto 3. Medidas (costos de ejemplo): M1 capacitación contra el phishing y doble verificación, $150.000, reduce R1 y R3; "
     "M2 bloquear el uso de USB desconocidas y revisarlas, $60.000, reduce R2; M3 respaldos fuera de línea, $200.000, reduce R4. Presupuesto: $250.000. Criterio: tratar primero los riesgos más altos que quepan en el presupuesto.")
build(
    O5, 4, F,
    use="Aprenderé a priorizar riesgos de una red LAN con una matriz, elegir medidas con presupuesto y recomendar con datos y límites.",
    prior=["Sé qué es un riesgo y cómo se calcula.", "Conozco medidas como filtrado, ACL y mínimo privilegio.", "Sé sumar y comparar costos."],
    explain=[
        "Priorizar riesgos permite usar bien los recursos. Se calcula el riesgo de cada amenaza (probabilidad por impacto) y se ordenan de mayor a menor. Una medida de mitigación es una acción que reduce la probabilidad o el impacto de un riesgo. No hay medidas perfectas: cada una tiene costo y no cubre todo.",
        "Con un presupuesto limitado se elige la combinación de medidas que reduzca los riesgos más altos y que quepa en el presupuesto. Una medida que reduce dos riesgos altos suele ser mejor que otra que reduce uno bajo. Un riesgo bajo no se ignora: se registra y se revisa en el siguiente período. La defensa en profundidad significa combinar varias medidas, porque ninguna es suficiente por sí sola.",
        "La recomendación incluye el cálculo, la comparación con el presupuesto y los límites. Aquí las probabilidades y los costos son de ejemplo y deben reevaluarse con datos reales y con la política de seguridad de la institución. Las pruebas técnicas siempre requieren autorización.",
    ],
    vocab=[("matriz de riesgos", "tabla que ordena riesgos por probabilidad e impacto"), ("mitigación", "acción que reduce un riesgo"), ("presupuesto", "dinero disponible para las medidas"), ("defensa en profundidad", "combinar varias medidas de protección"), ("riesgo residual", "riesgo que queda después de aplicar medidas")],
    worked=[
        ("Ordenar riesgos", "Tres riesgos de ejemplo valen 6, 3 y 9. ¿En qué orden se tratan primero?", ["Se ordenan de mayor a menor.", "9, luego 6 y por último 3."], "9, 6 y 3"),
        ("Cabe en el presupuesto", "Dos medidas de ejemplo cuestan $80.000 y $50.000, y el presupuesto es $120.000. ¿Caben juntas?", ["Se suman: 80.000 + 50.000 = 130.000.", "130.000 es mayor que 120.000."], "No caben juntas"),
    ],
    mistakes=[("Gastar todo el presupuesto en la medida más cara «por si acaso».", "Puede dejar sin tratar los riesgos más altos.", "Calcula el riesgo y elige las medidas que reducen los más altos dentro del presupuesto."),
              ("Ignorar un riesgo porque su valor es bajo.", "Un riesgo bajo puede cambiar con el tiempo.", "Regístralo y revísalo en el siguiente período.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una matriz de riesgos?", "Una tabla que ordena los riesgos por probabilidad e impacto", "Una lista de contraseñas", "Un plano de cableado", "La matriz ayuda a decidir qué riesgo tratar primero."),
        ("abc", "En Conectividad y Redes: ¿qué es una medida de mitigación?", "Una acción que reduce la probabilidad o el impacto de un riesgo", "Un equipo nuevo siempre", "Un permiso para entrar a la red", "Mitigar significa reducir la probabilidad o el impacto de un riesgo."),
        ("abc", "¿Qué es la defensa en profundidad?", "Combinar varias medidas de protección", "Confiar en una sola medida muy fuerte", "Esconder la red", "Si una medida falla, las otras siguen protegiendo."),
        ("=", "{F} ¿Cuál es el riesgo R3 (claves débiles en el servidor de notas)?", "3*2", "El riesgo es la probabilidad por el impacto.", ""),
        ("abc", "{F} ¿Qué riesgo es el más alto?", "R1, phishing, con 9", "R2, programa dañino, con 4", "R4, pérdida de datos, con 3", "R1 tiene 3×3 = 9, mayor que R3 (6), R2 (4) y R4 (3)."),
        ("=", "{F} ¿Cuánto suman los valores de los cuatro riesgos?", "3*3+2*2+3*2+1*3", "Se calcula cada riesgo y se suman.", ""),
        ("=", "{F} ¿Cuántos pesos cuestan juntas M1 y M2?", "150000+60000", "Se suman los costos de las dos medidas.", " pesos"),
        ("=", "{F} Si se aplican M1 y M2, ¿cuántos pesos sobran del presupuesto?", "250000-150000-60000", "Al presupuesto se le restan las dos medidas.", " pesos"),
        ("abc", "{F} ¿Qué combinación cubre los tres riesgos más altos y cabe en el presupuesto?", "M1 y M2", "M1 y M3", "M2 y M3", "M1 y M2 cuestan $210.000, caben en $250.000 y reducen R1, R3 y R2; las otras combinaciones superan el presupuesto."),
        ("abc", "{F} Un jefe quiere gastar todo en M3 «por si acaso». ¿Qué respondes con el criterio de la ficha?", "M3 reduce el riesgo más bajo; conviene tratar primero los más altos que quepan en el presupuesto", "Tiene razón: M3 es la más cara", "M3 reduce todos los riesgos", "El criterio prioriza los riesgos más altos y R4 tiene el valor más bajo."),
        ("abc", "{F} R4 es el riesgo más bajo. ¿Se ignora?", "No: se registra y se revisa en el siguiente período", "Sí, para siempre", "Sí, porque no tiene medidas", "Un riesgo bajo puede cambiar con el tiempo."),
        ("abc", "{F} ¿Qué datos debe incluir la recomendación?", "Los riesgos calculados, las medidas elegidas, su costo y el presupuesto", "Solo la opinión del técnico", "Las claves de los usuarios", "Con esos datos otra persona puede revisar la decisión."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Las probabilidades y costos son de ejemplo y deben reevaluarse con datos reales y la política de seguridad", "Ninguno, porque los números son exactos", "Que no hace falta revisar la política de seguridad", "Los valores de la ficha son estimaciones de ejemplo."),
    ],
    ctx=("abc", "Después de aplicar M1 y M2, la encargada pregunta si ya «estamos 100 % seguros». ¿Qué respondes?", "Que quedan riesgos residuales, que se registran y se revisan, porque ninguna medida protege del todo", "Que sí, completamente", "Que ya no hace falta mirar la matriz", "Siempre queda un riesgo residual que se vigila."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se ordenan los riesgos?", "De mayor a menor valor", "Así se tratan primero los más altos."),
        ("¿Qué criterio se usa con un presupuesto limitado?", "Tratar los riesgos más altos que quepan", "Se busca la mayor reducción de riesgo con el dinero disponible."),
        ("¿Qué es el riesgo residual?", "El riesgo que queda después de aplicar medidas", "Ninguna medida elimina todo el riesgo."),
    ],
    op=("Una escuela de ejemplo tiene cuatro riesgos: A) correos de engaño (probabilidad 3, impacto 2); B) claves compartidas (2, 3); C) equipos sin actualizar (3, 3); D) corte de energía (1, 2). Medidas: M1 actualizaciones automáticas, $70.000, reduce C; M2 capacitación en claves y correos, $90.000, reduce A y B; M3 respaldo de energía, $130.000, reduce D. Presupuesto $170.000. Calcula los riesgos, ordénalos y elige medidas dentro del presupuesto con una frase de límite.",
        "Riesgos: A = 6, B = 6, C = 9, D = 2. Orden: C, A y B (empatan), D. M1 + M2 = $160.000, caben en $170.000 y cubren C, A y B. M3 no cabe junto con ellas. Recomiendo M1 y M2; D queda residual y se revisa después. Límite: los valores son de ejemplo y se confirman con datos reales.",
        ["calcula y ordena los riesgos", "elige medidas que caben en el presupuesto", "declara el riesgo residual y un límite"],
        ["tabla de cuatro filas con riesgo y valor, y la lista de medidas con costo"],
        ["elegir M3 por ser la más cara", "olvidar sumar M1 y M2", "no declarar límites"],
        "Pregunta: «¿por qué M3 no entra en tu recomendación?». Si no puede responder, pídele que sume M1 + M2 + M3."),
    reinforce="Elige tres riesgos de tu entorno digital, califícalos de 1 a 3 y calcula su valor.",
    extend="Explica por qué una medida que cubre dos riesgos altos suele convenir más que una que cubre uno bajo.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 9 (servidor de ejemplo, inventado). «SRV-ARCHIVOS» de la oficina «Contadores del Sur» guarda 150 GB de archivos de clientes (datos personales). Hoy se hace una copia cada 24 horas a un disco que está en la misma sala. "
     "Fallas de ejemplo: disco dañado, borrado por error, programa que cifra los archivos y pide un pago (ransomware), corte de energía e incendio de la sala. Roles: administradora de sistemas, responsable de datos, usuarios. "
     "La copia completa se hace a 50 GB por hora.")
build(
    O6, 1, F,
    use="Aprenderé por qué se hacen copias de respaldo, qué fallas existen, quién participa y cuáles son los riesgos de la recuperación (solo conceptos).",
    prior=["Sé qué es un servidor.", "Sé qué son los datos personales.", "Sé dividir y multiplicar."],
    explain=[
        "Un servidor concentra archivos y servicios de muchas personas. Puede fallar por un disco dañado, un borrado por error, un programa dañino que cifra los archivos (ransomware), un corte de energía o un siniestro como un incendio. Un respaldo es una copia de los datos para poder recuperarlos, y restaurar es volver a poner esos datos en el servidor. La integridad es que los datos recuperados sean iguales a los originales; la disponibilidad es que estén cuando se necesitan.",
        "Un respaldo útil se piensa con cuidado: no sirve si está en el mismo lugar del servidor y se pierde en el mismo incendio, ni si nunca se probó restaurar. Como contiene datos personales, la copia tiene acceso restringido y, cuando corresponde, cifrado, según la ley vigente de protección de datos personales. Nadie se lleva copias a su casa por su cuenta.",
        "Ante un ransomware no se negocia ni se paga por cuenta propia: se avisa de inmediato a la responsable y a la autoridad competente, y se recupera desde una copia limpia con ayuda autorizada. Esta clase solo enseña conceptos y razonamiento; no te habilita para intervenir servidores reales.",
    ],
    vocab=[("respaldo", "copia de los datos para poder recuperarlos"), ("restaurar", "volver a poner los datos copiados en el servidor"), ("integridad", "que los datos recuperados sean iguales a los originales"), ("disponibilidad", "que los datos estén cuando se necesitan"), ("ransomware", "programa dañino que cifra archivos y pide un pago"), ("siniestro", "evento como un incendio que destruye equipos")],
    worked=[
        ("Tiempo de un respaldo", "Un respaldo de ejemplo de 120 GB se hace a 40 GB por hora. ¿Cuántas horas tarda?", ["Se divide el tamaño por la velocidad.", "120 ÷ 40 = 3."], "3 horas"),
        ("Dónde guardar la copia", "Un servidor de ejemplo guarda su copia en un disco de la misma sala. ¿Qué riesgo tiene?", ["Un incendio o un robo afectaría a ambos.", "Se perdería el original y la copia."], "Perder servidor y copia en el mismo siniestro"),
    ],
    mistakes=[("Guardar el respaldo junto al servidor.", "Un incendio, robo o inundación destruiría ambos.", "Guarda al menos una copia en otro lugar, con acceso restringido."),
              ("Llevarse un disco de respaldo a la casa «para estar seguro».", "Contiene datos personales de clientes y queda fuera de los controles.", "Las copias se guardan solo en lugares autorizados y protegidos.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un respaldo?", "Una copia de los datos para poder recuperarlos", "Un cable de repuesto del servidor", "Una clave de acceso", "El respaldo existe para recuperar datos si algo falla."),
        ("abc", "En Conectividad y Redes: ¿qué significa restaurar?", "Volver a poner los datos copiados en el servidor", "Borrar los archivos viejos", "Apagar el servidor", "Restaurar es recuperar los datos desde la copia."),
        ("abc", "¿Qué significa integridad de los datos?", "Que los datos recuperados sean iguales a los originales", "Que los datos sean muy pocos", "Que cualquiera pueda editarlos", "La integridad asegura que los datos no cambien o se dañen."),
        ("abc", "{F} Con una copia cada 24 horas, ¿cuántos datos podrían perderse como máximo?", "Hasta 24 horas de trabajo", "Solo los de un minuto", "Ninguno", "Lo creado desde la última copia no está respaldado."),
        ("abc", "{F} ¿Qué riesgo tiene guardar la copia en la misma sala del servidor?", "Un incendio destruiría el servidor y la copia", "Que la copia sea más rápida", "Que el servidor ocupe menos espacio", "Un siniestro en la sala afecta a ambos."),
        ("abc", "{F} ¿Por qué los respaldos tienen acceso restringido?", "Porque contienen datos personales de clientes", "Porque pesan mucho", "Porque son más lentos", "Las copias guardan los mismos datos personales que el servidor."),
        ("=", "{F} ¿Cuántas horas tarda la copia completa de 150 GB?", "150//50", "Se divide el tamaño de la copia por la velocidad.", " horas"),
        ("=", "{F} Si se guardara una copia completa diaria durante 7 días, ¿cuántos GB se necesitarían?", "150*7", "Se multiplica el tamaño de cada copia por los días guardados.", " GB"),
        ("abc", "{F} El servidor aparece con archivos cifrados y un mensaje que pide un pago. ¿Qué corresponde?", "Avisar de inmediato a la responsable, no pagar por cuenta propia y recuperar desde una copia limpia con ayuda autorizada", "Pagar rápido para no perder tiempo", "Apagar la copia de respaldo", "Se informa y se recupera con ayuda autorizada; pagar no asegura nada."),
        ("abc", "{F} Una usuaria borró una carpeta por error. ¿Qué dato necesita la administradora para recuperarla?", "Cuándo se borró, para elegir la última copia anterior a ese momento", "El color de la carpeta", "La clave personal de la usuaria", "Restaurar requiere elegir una copia previa al borrado."),
        ("abc", "El administrador de ejemplo dice: «hago respaldos todos los días, pero nunca probé restaurar». ¿Qué falla en su trabajo?", "No hay certeza de que la copia sirva para recuperar los datos", "Los respaldos son demasiado seguros", "No usa suficientes cables", "Una copia que nunca se restauró puede estar dañada sin que nadie lo sepa."),
        ("=", "{F} La última copia fue a las 02:00 y el disco falló a las 18:00 del mismo día. ¿Cuántas horas de trabajo se pierden?", "18-2", "Se restan las horas entre la última copia y la falla.", " horas"),
        ("abc", "{F} ¿Qué mejora más la protección frente a un incendio de la sala?", "Una copia guardada en otro lugar", "Otra copia en el mismo escritorio", "Un disco más rápido", "Solo una copia fuera del lugar sobrevive a un siniestro de la sala."),
    ],
    ctx=("abc", "Un técnico de ejemplo se lleva a su casa un disco con el respaldo de los clientes «para tenerlo a mano». ¿Qué corresponde?", "Devolverlo y avisar: contiene datos personales y debe guardarse en un lugar autorizado y protegido", "Dejarlo porque es de confianza", "Copiarlo a su computador personal", "Los datos personales se protegen con controles; nadie decide llevarlos por su cuenta."),
    sc=[
        ("En Conectividad y Redes: ¿qué es restaurar?", "Recuperar los datos desde una copia", "Es el paso que usa el respaldo cuando algo falla."),
        ("¿Por qué una copia no debe estar solo en la misma sala?", "Porque un siniestro podría destruir ambos", "Se necesita al menos una copia fuera del lugar."),
        ("¿Qué haces ante un ransomware?", "Aviso de inmediato a la responsable y no pago por cuenta propia", "La recuperación se hace con ayuda autorizada."),
    ],
    op=("Una veterinaria de ejemplo guarda 80 GB de fichas de clientes en un servidor y hace una copia cada 24 horas en el mismo mueble. La copia se hace a 40 GB por hora. Calcula cuántas horas tarda, di qué riesgo tiene guardarla ahí, y propone dos mejoras de ejemplo (una de lugar y una de control de datos personales).",
        "Tiempo: 80 ÷ 40 = 2 horas. Riesgo: un incendio o robo destruiría el servidor y la copia. Mejoras: guardar una copia en otro lugar; restringir el acceso a la copia y cifrarla cuando corresponda, porque contiene datos personales.",
        ["calcula el tiempo", "señala el riesgo del mismo lugar", "propone mejoras de lugar y de privacidad"],
        ["hoja con cálculo, riesgo y dos mejoras"],
        ["dividir al revés", "no mencionar la privacidad", "proponer llevar la copia a la casa"],
        "Pregunta: «¿qué se pierde si se incendia el mueble?». Si no responde, dibuja el servidor y la copia en el mismo cuadro."),
    reinforce="Anota tres cosas de tu vida digital que respaldarías y dónde guardarías las copias.",
    extend="Explica por qué una copia que nunca se probó no se puede considerar segura.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 10 (glosario de ejemplo). Respaldo completo: copia de todos los archivos. Respaldo incremental: copia solo lo que cambió desde el último respaldo, sea completo o incremental. "
     "Respaldo diferencial: copia lo que cambió desde el último respaldo completo. Regla 3-2-1: 3 copias de los datos en total (contando el original), en 2 tipos de medios distintos y con 1 copia fuera del lugar. "
     "RPO: máxima cantidad de datos, medida en tiempo, que se acepta perder. RTO: tiempo máximo aceptado para volver a operar. Huella (suma de comprobación): valor calculado a partir de un archivo; si el archivo cambia, el valor cambia. "
     "Documentos: plan de respaldo, bitácora de respaldos y plan de recuperación.")
build(
    O6, 2, F,
    use="Aprenderé los tipos de respaldo, la regla 3-2-1, el RPO y el RTO, la comprobación de integridad y los documentos del respaldo.",
    prior=["Sé qué es un respaldo y qué es restaurar.", "Sé qué es la integridad.", "Sé restar y dividir."],
    explain=[
        "Hay tres tipos de respaldo. El completo copia todo. El incremental copia solo lo que cambió desde el último respaldo, por eso es pequeño pero para restaurar se necesita el completo y todos los incrementales siguientes. El diferencial copia lo que cambió desde el último completo, por lo que crece cada día pero para restaurar bastan el completo y el último diferencial.",
        "La regla 3-2-1 propone tener 3 copias de los datos en total, contando el original, en 2 tipos de medios distintos y 1 de ellas fuera del lugar. Dos metas guían el plan: el RPO, que es cuántos datos se acepta perder (medido en tiempo, por ejemplo 24 horas), y el RTO, que es cuánto tiempo se acepta tardar en volver a operar. De ellos depende cada cuánto se respalda y con qué medios.",
        "Para comprobar la integridad se calcula una huella del archivo original y de la copia; si coinciden, la copia es igual al original. Los documentos que acompañan son el plan de respaldo (qué, cuándo, dónde y quién), la bitácora (registro de cada respaldo) y el plan de recuperación (cómo y en qué orden se recupera).",
    ],
    vocab=[("respaldo incremental", "copia de lo que cambió desde el último respaldo"), ("respaldo diferencial", "copia de lo que cambió desde el último respaldo completo"), ("regla 3-2-1", "3 copias, 2 medios distintos, 1 fuera del lugar"), ("RPO", "máximo de datos, en tiempo, que se acepta perder"), ("RTO", "tiempo máximo aceptado para volver a operar"), ("huella", "valor calculado de un archivo que cambia si el archivo cambia"), ("bitácora", "registro de cada respaldo hecho")],
    worked=[
        ("Crecimiento del diferencial", "Después de un completo, el lunes cambian 10 GB y el martes 6 GB más. ¿Cuánto pesa el diferencial del martes?", ["El diferencial copia todo lo cambiado desde el completo.", "10 + 6 = 16."], "16 GB"),
        ("Respaldos por día", "Si el RPO de ejemplo es 8 horas, ¿cuántos respaldos hay que hacer en 24 horas?", ["Se divide el día por el RPO.", "24 ÷ 8 = 3."], "3 respaldos"),
    ],
    mistakes=[("Creer que 3-2-1 son tres copias aparte del original.", "La regla cuenta el original como una de las 3 copias.", "Cuenta original, copia 2 y copia 3."),
              ("Usar la huella para comprobar un archivo sin tener la huella original.", "Sin referencia no hay con qué comparar.", "Calcula y guarda la huella cuando el archivo está sano.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es la regla 3-2-1?", "3 copias de los datos, en 2 medios distintos y 1 fuera del lugar", "3 servidores, 2 cables y 1 router", "3 respaldos al día, 2 por semana y 1 por mes", "La regla 3-2-1 busca resistir fallas combinando copias, medios y lugares."),
        ("abc", "En Conectividad y Redes: ¿qué es el RPO?", "El máximo de datos, medido en tiempo, que se acepta perder", "El tiempo para volver a operar", "El precio del respaldo", "El RPO define la antigüedad máxima aceptable del último respaldo."),
        ("abc", "¿Qué es un respaldo incremental?", "La copia de lo que cambió desde el último respaldo", "La copia de todos los archivos", "La copia de los archivos más grandes", "El incremental copia solo los cambios desde el último respaldo."),
        ("abc", "{F} ¿Cuántas copias exige la regla 3-2-1, contando el original?", "3", "2", "1", "La ficha dice 3 copias en total, contando el original."),
        ("abc", "{F} ¿Qué mide el RTO?", "El tiempo máximo aceptado para volver a operar", "Los datos que se pueden perder", "El tamaño del disco", "El RTO es un tiempo de recuperación."),
        ("abc", "{F} ¿Qué copia es la diferencial?", "La que guarda lo cambiado desde el último respaldo completo", "La que guarda lo cambiado desde el respaldo anterior, sea cual sea", "La que guarda todos los archivos", "El diferencial acumula los cambios desde el último completo."),
        ("=", "{F} Tras el completo, el lunes cambian 10 GB y el martes 6 GB más. ¿Cuánto pesa el diferencial del martes?", "10+6", "El diferencial acumula todo lo cambiado desde el completo.", " GB"),
        ("abc", "{F} Con el mismo ejemplo, ¿cuál pesa más el martes, el incremental o el diferencial?", "El diferencial, con 16 GB, frente a 6 GB del incremental", "El incremental, con 16 GB", "Pesan lo mismo", "El incremental copia solo los 6 GB del martes y el diferencial acumula 10 + 6."),
        ("abc", "{F} Original en el servidor (disco), una copia en un disco externo en la misma sala y una copia en cinta guardada en otro edificio. ¿Cumple la regla 3-2-1?", "Sí: 3 copias, 2 tipos de medio y 1 fuera del lugar", "No: faltan copias", "No: todas están en el mismo lugar", "Hay tres copias, dos medios (disco y cinta) y una copia en otro edificio."),
        ("abc", "{F} Original en el servidor y dos copias en discos externos de la misma sala. ¿Cumple la regla 3-2-1?", "No: hay un solo tipo de medio y ninguna copia fuera del lugar", "Sí: hay tres copias", "Sí: hay dos discos", "Cumple las 3 copias, pero no los 2 medios ni la copia fuera del lugar."),
        ("abc", "{F} La huella del archivo original es A9F3 y la de la copia es A9F3. ¿Qué indica?", "Que la copia es igual al original", "Que el archivo cambió", "Que la copia se dañó", "Huellas iguales indican que el contenido no cambió."),
        ("abc", "{F} La huella del original es A9F3 y la de la copia es 7C21. ¿Qué indica?", "Que la copia no es igual al original: cambió o se dañó, y no debe usarse sin revisar", "Que la copia es mejor", "Que la huella no sirve", "Una huella distinta indica que el contenido cambió."),
        ("=", "{F} Para que el RPO sea de 6 horas, ¿cuántos respaldos hay que hacer en un día de 24 horas?", "24//6", "Se divide el día por el tiempo máximo aceptado de pérdida.", " respaldos"),
    ],
    ctx=("abc", "El RTO acordado es de 4 horas, pero en una prueba la restauración demoró 6 horas. ¿Qué concluyes?", "No cumple el RTO; hay que cambiar el plan, por ejemplo con otro esquema o más velocidad", "Cumple, porque se restauró", "El RTO no importa", "Si el tiempo real supera el RTO, el plan no cumple lo acordado."),
    sc=[
        ("En Conectividad y Redes: ¿qué es el RTO?", "El tiempo máximo aceptado para volver a operar", "Se compara con el tiempo real de restauración."),
        ("¿Para qué sirve la huella de un archivo?", "Para comprobar que la copia es igual al original", "Si el archivo cambia, la huella cambia."),
        ("¿Qué documentos acompañan al respaldo?", "Plan de respaldo, bitácora y plan de recuperación", "Registran qué se hace, qué se hizo y cómo se recupera."),
    ],
    op=("Una radio comunitaria de ejemplo tiene el original de sus archivos en un computador, una copia en un disco externo del mismo escritorio y no tiene más copias. Evalúa si cumple la regla 3-2-1, propone un cambio para cumplirla, escribe el RPO para respaldar cada 12 horas y calcula cuántos respaldos hay al día.",
        "No cumple: hay 2 copias (original y disco), un solo medio y ninguna copia fuera del lugar. Cambio: agregar una copia en otro tipo de medio guardada en otro lugar autorizado. Respaldar cada 12 horas da RPO de 12 horas y 24 ÷ 12 = 2 respaldos al día.",
        ["evalúa la regla 3-2-1 con las tres condiciones", "propone un cambio coherente", "calcula RPO y respaldos por día"],
        ["hoja con la evaluación, el cambio y el cálculo"],
        ["contar mal las copias", "proponer otra copia en el mismo escritorio", "confundir RPO con RTO"],
        "Pregunta: «¿qué condición de 3-2-1 incumple?». Si dice una sola, pídele que revise copias, medios y lugar."),
    reinforce="Aplica la regla 3-2-1 a tus fotos de ejemplo y escribe dónde estaría cada copia.",
    extend="Explica por qué un esquema incremental puede ser más rápido de respaldar pero más lento de restaurar.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 11 (semana de respaldos de ejemplo). Domingo: respaldo completo de 200 GB. Cambios de cada día (datos nuevos o modificados): lunes 12 GB, martes 8 GB, miércoles 15 GB, jueves 10 GB, viernes 9 GB y sábado 6 GB. "
     "Esquema incremental: cada día se copia solo el cambio del día. Esquema diferencial: cada día se copia todo lo cambiado desde el domingo (acumulado: lunes 12, martes 20, miércoles 35, jueves 45, viernes 54 y sábado 60 GB). "
     "Velocidad de restauración de ejemplo: 35 GB por hora.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de respaldos: espacio por semana, cadena de restauración y qué pasa si una copia se daña (solo cálculos en papel).",
    prior=["Conozco los respaldos completo, incremental y diferencial.", "Sé qué es el RTO.", "Sé sumar y dividir."],
    explain=[
        "Para analizar un esquema de respaldo se calculan el espacio que ocupa y lo que hace falta para restaurar. En el esquema incremental se necesita la cadena completa: el respaldo completo más todos los incrementales hasta el día que se quiere recuperar. Si una pieza de la cadena se daña, los días siguientes no se pueden recuperar. En el diferencial solo hacen falta el completo y el último diferencial del día elegido.",
        "El espacio semanal del incremental es menor, porque cada día copia solo el cambio del día. El del diferencial es mayor, porque copia cada vez todo lo acumulado. El tiempo de restauración se calcula dividiendo los GB necesarios por la velocidad. La retención es el tiempo que se guardan las copias, y define el espacio total que se necesita.",
        "Todo plan declara qué día se puede recuperar, con cuántas piezas y en cuánto tiempo, y se prueba con restauraciones de ensayo en un ambiente autorizado. Los cálculos de esta clase son de ejemplo y no reemplazan una prueba real.",
    ],
    vocab=[("cadena de respaldos", "el completo más los incrementales necesarios para restaurar"), ("retención", "tiempo durante el cual se guardan las copias"), ("restauración de ensayo", "prueba de recuperar datos sin afectar el servicio"), ("pieza", "cada respaldo de una cadena"), ("espacio semanal", "GB que ocupan los respaldos de una semana")],
    worked=[
        ("Espacio incremental", "Un completo de 100 GB y dos incrementales de 5 y 7 GB. ¿Cuántos GB ocupan en total?", ["Se suman el completo y los incrementales.", "100 + 5 + 7 = 112."], "112 GB"),
        ("Tiempo de restauración", "Hay que restaurar 140 GB a 35 GB por hora. ¿Cuántas horas tarda?", ["Se divide el tamaño por la velocidad.", "140 ÷ 35 = 4."], "4 horas"),
    ],
    mistakes=[("Pensar que con el incremental del jueves se recupera todo.", "El incremental solo guarda el cambio de ese día; hace falta toda la cadena.", "Reúne el completo y todos los incrementales hasta el día elegido."),
              ("Calcular el espacio de un diferencial sumando solo el último día.", "Cada diferencial guarda todo lo acumulado desde el completo y se conserva cada día, así que ocupa espacio todos los días.", "Suma el completo y todos los diferenciales de la semana.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es la cadena de respaldos?", "El completo más los incrementales necesarios para restaurar un día", "Un cable largo que une servidores", "Una lista de claves", "Sin todas las piezas de la cadena no se puede recuperar el día elegido."),
        ("abc", "En Conectividad y Redes: ¿qué es la retención?", "El tiempo durante el cual se guardan las copias", "La velocidad de copia", "El tamaño del disco", "La retención define cuánto historial se conserva."),
        ("abc", "¿Qué es una restauración de ensayo?", "Una prueba de recuperar datos sin afectar el servicio, en un ambiente autorizado", "Borrar el servidor para ver si funciona", "Pagar por una copia nueva", "El ensayo comprueba que la copia sirve sin arriesgar el servicio."),
        ("=", "{F} ¿Cuántos GB ocupan los respaldos de la semana con el esquema incremental?", "200+12+8+15+10+9+6", "Se suman el completo y los seis incrementales.", " GB"),
        ("=", "{F} ¿Cuántos GB ocupan los respaldos de la semana con el esquema diferencial?", "200+12+20+35+45+54+60", "Se suman el completo y los seis diferenciales acumulados.", " GB"),
        ("abc", "{F} ¿Qué esquema ocupa menos espacio durante la semana?", "El incremental", "El diferencial", "Ocupan lo mismo", "260 GB del incremental son menos que 426 GB del diferencial."),
        ("=", "{F} Para restaurar hasta el jueves con el esquema incremental, ¿cuántos GB se necesitan (completo y cuatro incrementales)?", "200+12+8+15+10", "Se suman el completo del domingo y los incrementales de lunes a jueves.", " GB"),
        ("=", "{F} ¿Cuántas horas tarda esa restauración hasta el jueves?", "(200+12+8+15+10)//35", "Se dividen los GB de la cadena por la velocidad de restauración.", " horas"),
        ("abc", "{F} Con el esquema diferencial, ¿qué piezas se necesitan para restaurar el jueves?", "El completo del domingo y el diferencial del jueves", "El completo y los cuatro diferenciales", "Solo el diferencial del jueves", "El diferencial del jueves ya acumula todos los cambios desde el domingo."),
        ("abc", "{F} Si el incremental del martes está dañado, ¿qué pasa con la restauración hasta el jueves?", "No se puede recuperar completa: la cadena está rota", "Se recupera igual con el incremental del jueves", "Se recupera más rápido", "Las piezas siguientes dependen de la del martes."),
        ("abc", "{F} Si el diferencial del miércoles está dañado, ¿se puede restaurar hasta el jueves?", "Sí, con el completo del domingo y el diferencial del jueves", "No, porque el jueves depende del miércoles", "Solo si se repite el completo", "Cada diferencial depende del completo, no del diferencial anterior."),
        ("=", "{F} Si se guardan 4 semanas del esquema incremental, ¿cuántos GB se necesitan?", "4*(200+12+8+15+10+9+6)", "Se multiplica el espacio de una semana por las semanas guardadas.", " GB"),
        ("abc", "{F} El disco de respaldo es de 1.000 GB. ¿Alcanza para 4 semanas con el esquema incremental?", "No: faltan 40 GB", "Sí, sobran 40 GB", "Sí, queda justo", "Las 4 semanas necesitan 1.040 GB y el disco tiene 1.000 GB."),
    ],
    ctx=("abc", "Una oficina de ejemplo prefiere restaurar con pocas piezas y no le preocupa el espacio. ¿Qué esquema conviene considerar?", "El diferencial, porque solo necesita el completo y el último diferencial", "El incremental, porque ocupa menos", "Ninguno: no se puede restaurar", "El diferencial reduce las piezas de la restauración a costa de más espacio."),
    sc=[
        ("En Conectividad y Redes: ¿cuántas piezas necesita restaurar con diferencial?", "Dos: el completo y el último diferencial", "El diferencial acumula todos los cambios desde el completo."),
        ("¿Qué pasa si se daña una pieza de la cadena incremental?", "Los días siguientes no se pueden recuperar", "Cada incremental depende de todos los anteriores de la cadena."),
        ("¿Cómo se calcula el tiempo de restauración?", "GB necesarios divididos por la velocidad", "Es una estimación sencilla que se confirma con ensayos."),
    ],
    op=("Un servidor de ejemplo hace un completo el domingo de 100 GB. Cambios de cada día: lunes 5 GB, martes 4 GB, miércoles 6 GB. Calcula cuántos GB ocupan los tres primeros días con incremental y con diferencial (diferencial acumulado: lunes 5, martes 9, miércoles 15), cuántos GB hay que restaurar para volver al miércoles con cada esquema y qué pasaría si se daña el incremental del lunes.",
        "Incremental: 100 + 5 + 4 + 6 = 115 GB. Diferencial: 100 + 5 + 9 + 15 = 129 GB. Para volver al miércoles: incremental, 100 + 5 + 4 + 6 = 115 GB; diferencial, 100 + 15 = 115 GB. Si se daña el incremental del lunes, se rompe la cadena y no se recupera completo el martes ni el miércoles.",
        ["calcula el espacio de ambos esquemas", "calcula los GB para restaurar", "explica el efecto de una pieza dañada"],
        ["tabla con ambos esquemas y una frase sobre la cadena rota"],
        ["sumar solo el último día", "creer que el incremental del miércoles basta", "no explicar la cadena rota"],
        "Pregunta: «¿por qué la restauración es igual en ambos esquemas?». Si duda, pídele que liste las piezas de cada uno."),
    reinforce="Con un completo de 50 GB y cambios de 2, 3 y 4 GB, calcula el espacio incremental de tres días.",
    extend="Explica por qué conviene probar la restauración antes de necesitarla.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 12 (decisión de respaldo de ejemplo). Servidor de 200 GB que cambia 10 GB al día. Meta del proyecto: RPO de 24 horas y RTO de 8 horas. Velocidad de restauración de ejemplo: 52 GB por hora. "
     "Opción A: respaldo completo todos los días a un disco en la misma sala. Opción B: respaldo completo el domingo e incrementales diarios (de lunes a sábado), con una copia semanal guardada en otro edificio. "
     "Capacidad del disco de respaldo: 2.000 GB. Retención: 4 semanas.")
build(
    O6, 4, F,
    use="Aprenderé a elegir y justificar un esquema de respaldo con datos de espacio, RPO y RTO, y a decir qué falta para darlo por bueno (solo cálculos en papel).",
    prior=["Conozco los tipos de respaldo y la regla 3-2-1.", "Sé qué son el RPO y el RTO.", "Sé multiplicar, sumar y dividir."],
    explain=[
        "Elegir un esquema de respaldo es una decisión con criterios medibles: el espacio necesario para la retención debe caber en el disco, el RPO debe cumplirse con la frecuencia de respaldo, el RTO debe cumplirse con el tiempo real de restauración y debe haber al menos una copia fuera del lugar. Una opción que incumple un criterio indispensable se descarta, aunque sea más simple.",
        "El cálculo se hace en tres pasos: espacio semanal (completo más cambios), espacio de la retención (semanal por las semanas guardadas) y tiempo de restauración del peor caso (completo más todos los incrementales, dividido por la velocidad). Con eso se compara cada opción con las metas del proyecto.",
        "Un buen plan nunca se da por bueno solo por el cálculo: se completa con una prueba de restauración y una comprobación de integridad con huellas, hechas en un ambiente autorizado, y con el control de acceso a las copias porque contienen datos personales. La recomendación declara que los datos son de ejemplo.",
    ],
    vocab=[("peor caso", "situación que requiere más piezas o tiempo para restaurar"), ("criterio indispensable", "condición que una opción debe cumplir sí o sí"), ("prueba de restauración", "ensayo de recuperar datos para comprobar que la copia sirve"), ("comprobación de integridad", "verificar con huellas que la copia es igual al original"), ("plan de recuperación", "documento que dice cómo y en qué orden se recupera")],
    worked=[
        ("Espacio de una semana", "Un completo de 100 GB y seis incrementales de 5 GB cada uno. ¿Cuántos GB ocupa la semana?", ["Seis incrementales: 6 × 5 = 30.", "100 + 30 = 130."], "130 GB"),
        ("Peor caso", "Con 130 GB en la cadena y una velocidad de 26 GB por hora, ¿cuánto tarda el peor caso?", ["Se divide el tamaño de la cadena por la velocidad.", "130 ÷ 26 = 5."], "5 horas"),
    ],
    mistakes=[("Dar por buena una opción solo con el cálculo.", "Un cálculo no prueba que la copia se pueda restaurar.", "Haz una restauración de ensayo y verifica la integridad antes de confiar."),
              ("Elegir la opción más simple aunque no cabe en el disco.", "Un criterio indispensable incumplido descarta la opción.", "Descarta primero lo que no cumple y compara después.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una prueba de restauración?", "Un ensayo de recuperar datos para comprobar que la copia sirve", "Borrar el servidor para empezar de nuevo", "Cambiar el disco de respaldo", "La prueba de restauración demuestra que la copia es utilizable."),
        ("abc", "En Conectividad y Redes: ¿qué es un plan de recuperación?", "Un documento que dice cómo y en qué orden se recuperan los datos y servicios", "Una lista de precios", "Un tipo de cable", "El plan ordena la recuperación y asigna responsables."),
        ("abc", "¿Por qué se pide al menos una copia fuera del lugar?", "Para que un siniestro en la sala no destruya todas las copias", "Para que el respaldo sea más rápido", "Para ahorrar espacio", "Una copia en otro lugar sobrevive a un incendio o robo en la sala."),
        ("=", "{F} ¿Cuántos GB ocuparía la opción A en una semana (copia completa diaria durante 7 días)?", "200*7", "Se multiplica el tamaño de la copia por los 7 días.", " GB"),
        ("=", "{F} ¿Cuántos GB ocuparía la opción A en 4 semanas?", "200*7*4", "Se multiplica el espacio semanal por las 4 semanas de retención.", " GB"),
        ("abc", "{F} ¿Cabe la opción A en el disco de 2.000 GB?", "No: necesita 5.600 GB", "Sí: sobran 600 GB", "Sí: queda justo", "Las 4 semanas de la opción A superan por mucho la capacidad del disco."),
        ("=", "{F} ¿Cuántos GB ocupa una semana de la opción B (completo más seis incrementales de 10 GB)?", "200+6*10", "Se suman el completo y los seis incrementales.", " GB"),
        ("=", "{F} ¿Cuántos GB ocupa la opción B durante las 4 semanas?", "4*(200+6*10)", "Se multiplica el espacio de una semana por las 4 semanas.", " GB"),
        ("=", "{F} En el peor caso de la opción B (completo y seis incrementales), ¿cuántas horas tarda la restauración?", "(200+6*10)//52", "Se divide el tamaño de la cadena por la velocidad de restauración.", " horas"),
        ("abc", "{F} ¿Cumple la opción B el RTO de 8 horas?", "Sí: el peor caso tarda 5 horas", "No: tarda 13 horas", "No se puede saber nunca", "5 horas es menor que las 8 horas aceptadas."),
        ("abc", "{F} Un jefe quiere la opción A «porque restaurar es más simple». ¿Qué respondes?", "A no cabe en el disco y no tiene copia fuera del lugar; B cumple capacidad, RPO y RTO", "Tiene razón: la simplicidad es lo único importante", "A es mejor porque usa más espacio", "A incumple criterios indispensables; la simplicidad no los reemplaza."),
        ("abc", "{F} ¿Cumple B el RPO de 24 horas?", "Sí: se respalda cada día", "No: respalda cada semana", "No se puede saber nunca", "Con respaldos diarios se pierden como máximo 24 horas de datos."),
        ("abc", "{F} ¿Qué falta para dar por buena la opción B, además del cálculo?", "Una prueba de restauración, la comprobación de integridad y control de acceso a las copias", "Nada: el cálculo basta", "Cambiar el nombre del plan", "Los datos son una estimación y deben comprobarse en una prueba real."),
    ],
    ctx=("abc", "El cliente pregunta: «¿cómo sé que mi respaldo realmente sirve?». ¿Qué respondes?", "Que se hacen restauraciones de ensayo periódicas y se compara la huella de la copia con la del original", "Que si el programa no dio error, sirve", "Que basta con mirar el tamaño de la copia", "Solo restaurar y comparar demuestra que la copia es utilizable."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula el espacio de la retención?", "Espacio de una semana por las semanas guardadas", "La retención multiplica el espacio de cada período."),
        ("¿Qué criterio descarta una opción aunque sea simple?", "Un criterio indispensable incumplido, como no caber en el disco", "El criterio indispensable se cumple sí o sí."),
        ("¿Qué se hace antes de confiar en un respaldo?", "Una restauración de ensayo y una comprobación de integridad", "El cálculo no prueba que la copia se pueda usar."),
    ],
    op=("Un servidor de ejemplo tiene 100 GB y cambia 5 GB al día. Meta: RPO de 24 horas y RTO de 4 horas; velocidad de restauración de 26 GB por hora; disco de respaldo de 700 GB; retención de 4 semanas. Opción 1: completo diario en el mismo mueble. Opción 2: completo el domingo, incrementales diarios y una copia semanal en otro edificio. Calcula el espacio de ambas opciones, el peor caso de la opción 2 y recomienda con un límite.",
        "Opción 1: 100 × 7 × 4 = 2.800 GB, no cabe en 700 GB y no tiene copia fuera del lugar. Opción 2: semana 100 + 6 × 5 = 130 GB; 4 semanas = 520 GB, caben. Peor caso: 130 ÷ 26 = 5 horas, que supera el RTO de 4 horas. La opción 2 cumple espacio y RPO pero no el RTO de ejemplo: habría que subir la velocidad o usar diferencial. Límite: valores de ejemplo, falta la prueba de restauración.",
        ["calcula el espacio de ambas opciones", "calcula el peor caso y lo compara con el RTO", "concluye con honestidad y declara el límite"],
        ["hoja con cálculos, comparación y recomendación"],
        ["decir que cumple el RTO sin comparar 5 con 4", "olvidar la retención", "no declarar el límite"],
        "Pregunta: «¿cumple el RTO?». Si responde sí, pídele que compare 5 horas con 4 horas."),
    reinforce="Calcula el espacio de 3 semanas de un esquema con un completo de 60 GB y seis incrementales de 4 GB.",
    extend="Explica por qué es importante que el plan de recuperación indique quién hace cada paso.",
)

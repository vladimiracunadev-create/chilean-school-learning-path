"""Telecomunicaciones TP 3.º y 4.º medio: OAE-04 (medidas y pruebas de conexión y continuidad: lectura de resultados en papel) y OAE-05 (red de telefonía tradicional o IP: conceptos, capacidades y planes en papel)."""
from __future__ import annotations

from tp_tele_common import AVISO, build

O4 = "TP-TELE-3y4-OAE-04"
O5 = "TP-TELE-3y4-OAE-05"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (orden de pruebas de ejemplo, inventada). La empresa ficticia «Enlaces Pehuén» recibe la orden OT-204: certificar 6 enlaces de cable de red de una oficina. Pruebas pedidas: mapa de cableado, longitud, "
     "atenuación y continuidad. Instrumentos de ejemplo: probador de cables (muestra «pasa» o «falla») y certificador (entrega un informe por enlace). Referencia de ejemplo: el tramo fijo de un enlace de cobre no debe superar 90 metros (verifica la norma del proyecto). "
     "Advertencia de la orden: las pruebas se hacen sobre cables sin energía de red; todo trabajo con energía eléctrica lo hace personal autorizado.")
build(
    O4, 1, F,
    use="Aprenderé por qué se miden las conexiones y la continuidad de una señal, qué instrumentos se usan y qué riesgos y normas hay que respetar.",
    prior=["Sé qué es un enlace de red y un esquema.", "Sé leer una tabla con pasa o falla.", "Sé qué es un riesgo eléctrico."],
    explain=[
        "Medir es comprobar con un instrumento si una conexión cumple lo que pide el proyecto. La prueba de continuidad comprueba que el camino de la señal esté sin cortes, de un extremo al otro del cable. La prueba de conexión, que se llama mapa de cableado, revisa que cada hilo llegue al punto correcto. La certificación es el conjunto de pruebas que confirma que el enlace cumple las exigencias de la norma vigente, y deja un informe como evidencia.",
        "Cada instrumento mide algo distinto. El probador de cables dice si hay continuidad y si los hilos están bien conectados. El certificador mide además la longitud y la atenuación (cuánto se debilita la señal en el cable). En fibra óptica, un medidor de potencia óptica mide cuánta luz llega al otro extremo. Todo instrumento debe estar calibrado, es decir, contrastado con una referencia para que sus lecturas sean confiables.",
        f"Una lectura sin registro no sirve: se anotan fecha, enlace, resultado e instrumento. Medir en circuitos con energía eléctrica es riesgoso y solo lo hace personal autorizado. {AVISO} Aquí solo se leen resultados escritos.",
    ],
    vocab=[("continuidad", "camino de la señal sin cortes de un extremo al otro"), ("certificación", "conjunto de pruebas que confirma que un enlace cumple la norma"), ("atenuación", "cuánto se debilita la señal en el cable"), ("probador de cables", "instrumento que indica si hay continuidad y si los hilos están bien conectados"), ("calibración", "contraste de un instrumento con una referencia para que mida bien"), ("informe de certificación", "documento con los resultados de las pruebas de un enlace")],
    worked=[
        ("Elegir el instrumento", "Un técnico de ejemplo quiere saber si un cable tiene un corte en el camino de la señal. ¿Qué prueba hace?", ["Un corte es una falta de continuidad.", "La prueba de continuidad lo detecta."], "La prueba de continuidad"),
        ("Cumplir el largo", "El largo de un enlace de ejemplo es 82 metros y el máximo del proyecto es 90 metros. ¿Cumple?", ["Se compara 82 con el máximo de 90.", "82 es menor que 90."], "Sí, cumple"),
    ],
    mistakes=[("Usar un instrumento sin saber si está calibrado, «porque siempre funcionó».", "Un instrumento descalibrado puede dar lecturas erróneas sin avisar.", "Verifica la calibración vigente antes de medir."),
              ("Anotar el resultado de memoria al final del día.", "Se olvidan lecturas o se confunden los enlaces.", "Registra cada lectura en el momento con fecha y enlace.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué comprueba la prueba de continuidad?", "Que el camino de la señal no tenga cortes", "Que el cable sea de un color determinado", "Que el cliente pagó el trabajo", "La continuidad verifica que la señal pueda recorrer el cable sin cortes."),
        ("abc", "En Telecomunicaciones: ¿qué es la atenuación?", "Cuánto se debilita la señal en el cable", "Cuánto aumenta la señal en un amplificador", "El nombre del instrumento", "La atenuación es la pérdida de señal en el cable."),
        ("abc", "¿Para qué sirve calibrar un instrumento?", "Para que sus lecturas sean confiables", "Para que pese menos", "Para que mida más rápido", "La calibración compara el instrumento con una referencia."),
        ("=", "{F} ¿Cuántas pruebas distintas pide la orden por cada enlace?", "1+1+1+1", "La orden nombra mapa de cableado, longitud, atenuación y continuidad.", " pruebas"),
        ("abc", "{F} ¿Qué instrumento entrega un informe por enlace con longitud y atenuación?", "El certificador", "El probador de cables solo con pasa o falla", "La cinta de medir", "La ficha dice que el certificador entrega un informe por enlace."),
        ("abc", "{F} Un enlace mide 94 metros. ¿Qué corresponde según la referencia de la ficha?", "No cumple el máximo de 90 metros", "Cumple porque 94 es mayor que 90", "Cumple porque el probador lo dijo", "94 supera el máximo de ejemplo de 90."),
        ("=", "{F} Si cada uno de los 6 enlaces requiere 4 pruebas, ¿cuántas pruebas se registran en total?", "6*4", "Se multiplican los enlaces por las pruebas de cada uno.", " pruebas"),
        ("abc", "{F} Un colaborador propone medir directamente en un tablero con energía eléctrica «para adelantar». ¿Qué corresponde?", "Dejar esa medida a personal autorizado con norma vigente", "Hacerlo con cuidado y sin avisar", "Pedirle al cliente que lo haga", "Medir con energía es riesgoso y lo hace personal autorizado."),
        ("abc", "El probador de ejemplo muestra «falla» y el técnico anota «pasa» para no atrasar la entrega. ¿Qué principio se rompe?", "Los registros deben reflejar fielmente la lectura", "El cable debe ser más largo", "El informe debe ser más corto", "Alterar un resultado es una falta grave a la honestidad del registro."),
        ("=", "El tramo de un enlace de ejemplo mide 56 metros y el máximo es 90 metros. ¿Cuántos metros de margen hay?", "90-56", "Se resta el largo medido al máximo permitido.", " metros"),
        ("abc", "Un instrumento tiene la etiqueta de calibración vencida hace un año. ¿Qué corresponde?", "No usarlo hasta que lo calibren", "Usarlo igual y avisar después", "Anotar una fecha nueva en la etiqueta", "Un instrumento sin calibración vigente no da lecturas confiables."),
        ("abc", "{F} ¿Qué dato mínimo debe llevar el registro de una lectura?", "Fecha, enlace, resultado e instrumento", "Solo el resultado", "Solo la fecha", "Con esos cuatro datos otra persona puede verificar la lectura."),
        ("abc", "{F} Una orden de trabajo pide medir los 6 enlaces, pero el técnico solo tiene tiempo para 4. ¿Qué corresponde?", "Informar a la jefatura y registrar cuáles quedaron pendientes", "Anotar «pasa» en los 2 restantes", "No entregar ningún informe", "No se inventan resultados; se informa lo pendiente."),
    ],
    ctx=("abc", "El cliente de ejemplo dice: «no me hagan el informe de certificación, me fío de ustedes». ¿Qué responde la empresa?", "Que el informe es la evidencia de que los enlaces cumplen y se entrega igualmente", "Que no es necesario si el cliente confía", "Que se entrega solo si el cliente paga más", "El informe respalda el trabajo ante cualquier revisión."),
    sc=[
        ("En Telecomunicaciones: ¿para qué sirve el probador de cables?", "Para ver si hay continuidad y si los hilos están bien conectados", "El probador muestra pasa o falla para cada enlace."),
        ("¿Qué se registra con cada lectura?", "Fecha, enlace, resultado e instrumento", "Con esos datos otra persona puede verificar la medida después."),
        ("¿Quién mide en circuitos con energía?", "Personal autorizado con norma vigente", "El cuaderno no habilita para medir con energía."),
    ],
    op=("Una escuela de ejemplo pide certificar 5 enlaces. Lecturas de ejemplo: enlace 1, 70 m, pasa; enlace 2, 91 m, falla por largo; enlace 3, 40 m, pasa; enlace 4, 88 m, pasa; enlace 5, 60 m, falla por continuidad. El máximo de ejemplo es 90 m. Escribe (a) cuántos enlaces cumplen, (b) por qué falla cada uno que no cumple y (c) qué dato mínimo anotarías de cada lectura.",
        "(a) Cumplen 3 enlaces (1, 3 y 4). (b) El 2 falla porque 91 m supera 90 m; el 5 falla porque no tiene continuidad. (c) Fecha, enlace, resultado e instrumento.",
        ["cuenta los enlaces que cumplen", "explica cada falla", "nombra los datos del registro"],
        ["tabla con los 5 enlaces y su resultado"],
        ["contar mal los que pasan", "decir que el 91 m cumple", "no anotar el instrumento"],
        "Pregunta: «¿qué enlaces fallan y por qué?». Si no responde, pídele que compare cada largo con el máximo."),
    reinforce="Escribe tres datos que debe llevar el registro de una lectura de un enlace.",
    extend="Explica con un ejemplo inventado por qué un informe de certificación protege tanto a la empresa como al cliente.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (lecturas de ejemplo, inventadas). Mapa de cableado de un enlace de 8 hilos agrupados en 4 pares: par 1 OK; par 2 OK; par 3 «abierto» (un hilo con corte); par 4 «cruzado» (dos hilos intercambiados). "
     "Resistencia de continuidad medida en un hilo: 2 ohmios (Ω); criterio de ejemplo del proyecto: se acepta hasta 5 Ω. Documentos: protocolo de pruebas, informe de certificación, etiqueta del enlace y registro de calibración. "
     "Roles: técnico de pruebas, supervisor y cliente.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de las pruebas (continuidad, resistencia, mapa de cableado), los tipos de falla y los documentos y roles de una certificación.",
    prior=["Sé qué es la continuidad y la atenuación.", "Sé leer una tabla de resultados.", "Sé qué es un par de hilos."],
    explain=[
        "La resistencia eléctrica dice cuánto se opone un hilo al paso de la corriente y se mide en ohmios (Ω). Un hilo sano tiene una resistencia baja; un corte tiene resistencia muy alta (circuito abierto). Un hilo tocando a otro por error produce un cortocircuito (resistencia casi nula entre dos puntos que no deben unirse). El mapa de cableado muestra si cada hilo llega al punto correcto.",
        "Las fallas típicas de conexión son: abierto (un hilo cortado), cortocircuito (dos hilos unidos), cruzado o invertido (dos hilos en posiciones cambiadas) y par dividido (hilos de pares distintos mal emparejados). Cada falla se anota con el par afectado. Las lecturas se comparan con el criterio del proyecto: si cumplen, el resultado es «pasa»; si no, «falla».",
        f"Los documentos de una certificación son: el protocolo de pruebas (qué se mide y con qué criterio), el informe de certificación (los resultados), la etiqueta que identifica cada enlace y el registro de calibración del instrumento. El técnico de pruebas mide, el supervisor revisa y el cliente recibe el informe. {AVISO}",
    ],
    vocab=[("resistencia", "oposición de un hilo al paso de la corriente, en ohmios (Ω)"), ("circuito abierto", "camino cortado, sin paso de señal"), ("cortocircuito", "unión no deseada entre dos puntos"), ("mapa de cableado", "prueba que muestra a dónde llega cada hilo"), ("cruzado", "dos hilos en posiciones cambiadas"), ("protocolo de pruebas", "documento que dice qué se mide y con qué criterio")],
    worked=[
        ("Aceptar una resistencia", "El criterio de ejemplo acepta hasta 6 Ω y un hilo mide 4 Ω. ¿Pasa?", ["Se compara 4 con el máximo de 6.", "4 es menor que 6."], "Sí, pasa"),
        ("Nombrar la falla", "El mapa de ejemplo muestra que dos hilos de un par están en posiciones cambiadas. ¿Qué falla es?", ["Los hilos están intercambiados.", "Eso se llama cruzado o invertido."], "Cruzado (invertido)"),
    ],
    mistakes=[("Creer que un hilo cortado da una resistencia baja.", "Un corte impide el paso: la resistencia es muy alta (circuito abierto).", "Recuerda: corte, resistencia muy alta; unión no deseada, resistencia casi nula."),
              ("Informar «falla» sin decir en qué par ni qué tipo de falla.", "Sin ese dato nadie sabe qué corregir.", "Anota el par y el tipo de falla en el informe.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un circuito abierto?", "Un camino cortado, sin paso de señal", "Una unión no deseada entre dos hilos", "Un hilo muy grueso", "En un circuito abierto la señal no puede pasar."),
        ("abc", "En Telecomunicaciones: ¿qué es un cortocircuito?", "Una unión no deseada entre dos puntos", "Un hilo cortado", "Un equipo apagado", "El cortocircuito une dos puntos que no deben unirse."),
        ("abc", "¿En qué unidad se mide la resistencia?", "Ohmios (Ω)", "Metros", "Decibeles", "La resistencia se mide en ohmios."),
        ("abc", "{F} ¿Qué falla tiene el par 3?", "Abierto", "Cruzado", "Cortocircuito", "La ficha dice que el par 3 tiene un hilo con corte."),
        ("abc", "{F} ¿Qué falla tiene el par 4?", "Cruzado", "Abierto", "Par dividido", "La ficha dice que el par 4 tiene dos hilos intercambiados."),
        ("=", "{F} ¿Cuántos pares de los cuatro están sin falla?", "4-1-1", "Se restan los pares con falla a los cuatro del enlace.", " pares"),
        ("abc", "{F} El hilo medido da 2 Ω y el criterio acepta hasta 5 Ω. ¿Qué resultado corresponde?", "Pasa", "Falla", "Se repite sin medir", "2 es menor que el máximo aceptado de 5."),
        ("=", "{F} El criterio acepta hasta 5 Ω. Un segundo hilo mide 8 Ω. ¿Cuántos ohmios se pasa del máximo?", "8-5", "Se resta el máximo aceptado a la lectura.", " Ω"),
        ("abc", "¿Qué documento dice qué se mide y con qué criterio?", "El protocolo de pruebas", "La etiqueta del enlace", "El registro de calibración", "El protocolo define las pruebas y sus criterios."),
        ("abc", "{F} ¿Qué resultado total corresponde al enlace con el par 3 abierto y el par 4 cruzado?", "Falla", "Pasa", "Pasa con observaciones", "Un enlace con fallas de conexión no cumple."),
        ("abc", "Un técnico ve un resultado «abierto» y escribe en el informe solo «falla». ¿Qué falta?", "El par afectado y el tipo de falla", "El nombre del cliente", "El precio del cable", "Sin el detalle no se sabe qué corregir."),
        ("abc", "El técnico de pruebas quiere aprobar su propio informe. ¿Qué rol corresponde que lo revise?", "El supervisor", "El mismo técnico", "El cliente sin leerlo", "Nadie aprueba su propio trabajo; lo revisa otra persona."),
        ("=", "Un enlace de ejemplo tiene 8 hilos y se midió la resistencia de cada uno. Si solo 1 hilo falló, ¿cuántos hilos pasaron?", "8-1", "Se resta el hilo con falla a los ocho del enlace.", " hilos"),
    ],
    ctx=("abc", "El cliente de ejemplo pregunta por qué falló su enlace. El informe dice «par 3: abierto». ¿Qué puede explicar el técnico?", "Que uno de los hilos del par 3 está cortado y no deja pasar la señal", "Que el enlace sobra y no sirve", "Que el cliente debe repetir la prueba", "El informe indica el par y el tipo de falla."),
    sc=[
        ("En Telecomunicaciones: ¿qué es un circuito abierto?", "Un camino cortado que no deja pasar la señal", "El corte da resistencia muy alta."),
        ("¿Qué falla es un hilo con un corte?", "Abierto", "Con el corte, la señal no puede pasar por ese hilo."),
        ("¿Quién revisa el informe de pruebas?", "El supervisor", "No se aprueba el propio trabajo."),
    ],
    op=("Lecturas de ejemplo de un enlace de 4 pares: par 1 OK; par 2 cortocircuito; par 3 OK; par 4 abierto. Resistencia de un hilo: 9 Ω; criterio de ejemplo: hasta 5 Ω. Escribe (a) el resultado total del enlace, (b) qué dos fallas aparecen y en qué par, (c) si la resistencia de 9 Ω cumple y (d) quién revisa el informe.",
        "(a) Falla. (b) Cortocircuito en el par 2 y abierto en el par 4. (c) No cumple, porque 9 es mayor que 5. (d) El supervisor.",
        ["indica el resultado total", "nombra las dos fallas con su par", "compara la resistencia y nombra al revisor"],
        ["hoja con las cuatro respuestas"],
        ["decir que pasa con dos fallas", "confundir abierto con cortocircuito", "olvidar al supervisor"],
        "Pregunta: «¿qué diferencia hay entre un corte y una unión no deseada?». Si no sabe, pídele que dibuje un hilo cortado."),
    reinforce="Escribe una lectura de ejemplo para un enlace con un par cruzado y otra para un enlace sin fallas.",
    extend="Explica con un ejemplo inventado por qué el informe debe indicar el par que falla y no solo «falla».",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (informe de ejemplo, inventado). Informe de certificación de la «Oficina Techo Azul» (ficticia): "
     "enlace E1, largo 45 m, atenuación 10 dB, mapa OK. Enlace E2, largo 92 m, atenuación 18 dB, mapa OK. Enlace E3, largo 60 m, atenuación 14 dB, mapa «par 2 abierto». "
     "Enlace E4, largo 85 m, atenuación 17 dB, mapa OK. Criterios de ejemplo: largo máximo 90 m; atenuación máxima 20 dB; mapa debe estar OK.")
build(
    O4, 3, F,
    use="Aprenderé a analizar en papel un informe de pruebas y a decidir qué enlaces pasan, cuáles fallan y por qué.",
    prior=["Sé qué son largo, atenuación y mapa de cableado.", "Sé comparar un valor con un máximo.", "Sé leer una tabla de resultados."],
    explain=[
        "Analizar un informe de pruebas es comparar cada lectura con su criterio. Cada enlace debe cumplir todos los criterios a la vez: si falla en uno, el enlace falla, aunque los demás estén bien. Para analizar con orden se hace una tabla con una fila por enlace y una columna por criterio, y se marca cumple o no cumple en cada casilla.",
        "Al comparar se mira el sentido de cada criterio. Un máximo se cumple si la lectura es menor o igual que él (largo, atenuación). El mapa de cableado se cumple solo si está OK. Después se anotan las causas probables de cada falla: un largo excesivo sugiere que el recorrido real es mayor al previsto; un par abierto sugiere un hilo cortado o mal conectado.",
        "El análisis termina con una conclusión: cuántos enlaces pasan, cuáles fallan y qué se recomienda (por ejemplo, volver a revisar o rehacer el enlace, trabajo que haría personal autorizado). No se cambia ninguna lectura para que el informe se vea mejor; los resultados reales se entregan a la jefatura.",
    ],
    vocab=[("criterio", "valor o condición que la lectura debe cumplir"), ("cumple", "la lectura está dentro del criterio"), ("causa probable", "explicación más posible de una falla"), ("conclusión", "resumen final con los resultados y las recomendaciones")],
    worked=[
        ("Revisar un enlace", "Un enlace de ejemplo mide 80 m y tiene atenuación de 22 dB. Los criterios son 90 m y 20 dB como máximo. ¿Pasa?", ["El largo cumple: 80 es menor que 90.", "La atenuación no cumple: 22 es mayor que 20."], "Falla por atenuación"),
        ("Contar enlaces", "En una prueba de ejemplo de 5 enlaces, 3 pasaron. ¿Cuántos fallaron?", ["Se resta lo que pasó al total.", "5 menos 3."], "2 enlaces"),
    ],
    mistakes=[("Decir que un enlace pasa porque cumple el largo, sin mirar los otros criterios.", "Un enlace debe cumplir todos los criterios a la vez.", "Marca cada criterio en la tabla antes de concluir."),
              ("Cambiar una lectura a mano para que el informe quede limpio.", "Un informe alterado deja de ser evidencia y es una falta grave.", "Entrega las lecturas reales y explica las fallas.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿cuándo pasa un enlace?", "Cuando cumple todos los criterios a la vez", "Cuando cumple el largo", "Cuando el cliente lo pide", "Un enlace pasa solo si cumple todos los criterios."),
        ("abc", "¿Un valor de 18 dB cumple un máximo de 20 dB?", "Sí, porque 18 es menor que 20", "No, porque 18 está muy cerca de 20", "No, porque un máximo solo se cumple con valores iguales a 20", "Un máximo se cumple si la lectura es menor o igual."),
        ("abc", "{F} ¿Qué enlace falla por largo?", "E2", "E1", "E4", "E2 mide 92 m, más que el máximo de 90 m."),
        ("abc", "{F} ¿Qué enlace falla por el mapa de cableado?", "E3", "E1", "E2", "E3 tiene un par abierto; su mapa no está OK."),
        ("=", "{F} ¿Cuántos enlaces de los cuatro pasan todos los criterios?", "4-1-1", "Fallan E2 por largo y E3 por mapa; pasan los otros.", " enlaces"),
        ("abc", "{F} ¿Pasa el enlace E4?", "Sí, cumple largo, atenuación y mapa", "No, porque está cerca del máximo", "No, porque su atenuación es 17 dB", "E4 cumple los tres criterios: 85 m, 17 dB y mapa OK."),
        ("=", "{F} ¿Cuántos metros le faltan a E4 para llegar al largo máximo?", "90-85", "Se resta el largo del enlace al máximo.", " metros"),
        ("abc", "{F} ¿Cuál es la causa probable de la falla de E3?", "Un hilo cortado o mal conectado en el par 2", "Un cable demasiado largo", "Un instrumento sin pilas", "Un par abierto sugiere un hilo cortado o mal conectado."),
        ("abc", "{F} ¿Qué recomendación corresponde para E2, de 92 m?", "Informar a la jefatura para revisar el recorrido o rehacer el enlace por personal autorizado", "Cambiar el largo a 90 m en el informe", "Dejarlo así porque son solo 2 metros más", "No se alteran las lecturas; se informa y se propone."),
        ("=", "{F} ¿Cuántos dB de margen tiene E1 respecto del máximo de atenuación?", "20-10", "Se resta la atenuación medida al máximo permitido.", " dB"),
        ("abc", "{F} El cliente pide cambiar en el informe el largo de E2 de 92 m a 90 m para recibir el trabajo. ¿Qué corresponde?", "Negarse con respeto y entregar la lectura real", "Cambiar el dato si el cliente paga", "Cambiarlo y avisar después", "Un informe alterado deja de ser evidencia."),
        ("abc", "Un enlace de ejemplo tiene largo 88 m, atenuación 21 dB y mapa OK, con criterios 90 m y 20 dB. ¿Qué resultado corresponde?", "Falla por atenuación", "Pasa porque el largo cumple", "Pasa porque el mapa está OK", "Aunque cumple dos criterios, la atenuación supera el máximo."),
        ("abc", "{F} Una persona resume: «3 de los 4 enlaces están bien». ¿Cuál es el error?", "Solo 2 enlaces pasan todos los criterios, no 3", "Sí es correcto", "Pasan los 4 enlaces", "Pasan E1 y E4; E2 y E3 fallan."),
    ],
    ctx=("abc", "La jefatura de ejemplo pregunta si puede entregar el informe de E1 a E4 al cliente tal cual. ¿Qué respondes?", "Sí, si incluye las lecturas reales, las 2 fallas, sus causas y la recomendación", "No, hay que ocultar las fallas", "Sí, pero quitando E2 y E3", "El informe veraz incluye también las fallas."),
    sc=[
        ("En Telecomunicaciones: ¿qué se compara en un informe de pruebas?", "Cada lectura con su criterio", "Así se decide si pasa o falla."),
        ("¿Se puede cambiar una lectura para que quede bien?", "No", "Un informe alterado no es evidencia."),
        ("Si un enlace falla en un criterio, ¿pasa?", "No", "Un enlace debe cumplir todos los criterios a la vez."),
    ],
    op=("Informe de ejemplo: enlace A, 70 m, 12 dB, mapa OK; enlace B, 95 m, 15 dB, mapa OK; enlace C, 50 m, 22 dB, mapa OK; enlace D, 60 m, 16 dB, mapa «par 1 cruzado». Criterios: 90 m, 20 dB y mapa OK. Haz una tabla con cumple o no cumple por criterio, indica cuántos enlaces pasan y escribe una recomendación breve.",
        "A pasa; B falla por largo (95 m); C falla por atenuación (22 dB); D falla por mapa (par 1 cruzado). Pasa 1 enlace de 4. Recomendación: informar a la jefatura las tres fallas con sus causas y proponer que personal autorizado revise o rehaga B, C y D.",
        ["marca cada criterio por enlace", "cuenta los enlaces que pasan", "recomienda sin alterar datos"],
        ["tabla de 4 filas y la recomendación"],
        ["pasar un enlace que falla un criterio", "alterar lecturas", "no indicar la causa"],
        "Pregunta: «¿qué criterio no cumple cada enlace que falla?». Si no responde, pídele que revise la tabla columna por columna."),
    reinforce="Haz una tabla de ejemplo con tres enlaces y marca cuál pasa y cuál falla según un largo máximo de 90 m.",
    extend="Explica con un ejemplo inventado qué haría la jefatura si un cliente le pide quitar una falla del informe.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (presupuesto de pérdidas de fibra de ejemplo, inventado). Enlace de fibra óptica entre dos edificios de la «Cooperativa Vista Sur» (ficticia): largo 2 kilómetros; atenuación de la fibra 3 dB por kilómetro (valor de ejemplo); "
     "2 conectores de 1 dB cada uno y 1 empalme de 1 dB (valores de ejemplo). Pérdida máxima aceptada por el proyecto: 11 dB. Medición de ejemplo con el medidor de potencia óptica: pérdida total 9 dB.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular el presupuesto de pérdida de un enlace de fibra y compararlo con la medición.",
    prior=["Sé qué es la atenuación en dB.", "Sé sumar pérdidas y comparar con un máximo.", "Sé qué es una certificación."],
    explain=[
        "Un enlace de fibra óptica lleva la señal como luz por un hilo de vidrio muy delgado. Tiene tres fuentes de pérdida: la fibra misma (se multiplica su atenuación por kilómetro por los kilómetros del enlace), cada conector y cada empalme (unión permanente de dos fibras). La pérdida total esperada es la suma de las tres, y se llama presupuesto de pérdida.",
        "Después de medir con el medidor de potencia óptica, se compara la pérdida medida con la esperada y con el máximo del proyecto. Si la medida es menor o igual que el máximo, el enlace pasa. Si la medida es mucho mayor que la esperada, aunque pase, conviene sospechar un conector sucio o un empalme malo y avisar. Una medida menor que la esperada también debe revisarse: puede indicar un error de la medición.",
        f"El resultado se anota en el informe de certificación con la lectura real. Manipular fibra y medir enlaces en terreno exige instructor y norma; la luz de algunos equipos puede dañar los ojos y nunca se mira directamente un extremo de fibra. {AVISO}",
    ],
    vocab=[("fibra óptica", "hilo de vidrio muy delgado por donde viaja la señal como luz"), ("empalme", "unión permanente de dos fibras"), ("conector", "pieza que permite unir y separar una fibra de un equipo"), ("presupuesto de pérdida", "suma de las pérdidas esperadas de un enlace"), ("medidor de potencia óptica", "instrumento que mide cuánta luz llega por la fibra")],
    worked=[
        ("Pérdida de la fibra", "Una fibra de ejemplo de 3 km pierde 2 dB por km. ¿Cuánto pierde la fibra en total?", ["Se multiplica la pérdida por kilómetro por los kilómetros.", "2 por 3."], "6 dB"),
        ("Pasa o falla", "La pérdida medida de ejemplo es 8 dB y el máximo es 10 dB. ¿Pasa?", ["Se compara 8 con el máximo 10.", "8 es menor que 10."], "Sí, pasa"),
    ],
    mistakes=[("Olvidar los conectores y empalmes al calcular la pérdida esperada.", "También restan señal y pueden pasar el máximo.", "Suma fibra, conectores y empalmes."),
              ("Mirar de frente el extremo de una fibra «para ver si hay luz».", "La luz de algunos equipos puede dañar los ojos.", "Nunca mires un extremo de fibra; usa el medidor.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un empalme?", "La unión permanente de dos fibras", "El conector que se enchufa a un equipo", "El hilo de cobre del cable", "El empalme une dos fibras de forma permanente."),
        ("abc", "En Telecomunicaciones: ¿qué mide el medidor de potencia óptica?", "Cuánta luz llega por la fibra", "La temperatura del cable", "La cantidad de usuarios", "Mide la potencia de la luz que llega."),
        ("abc", "¿Qué fuentes de pérdida tiene un enlace de fibra?", "La fibra, los conectores y los empalmes", "Solo la fibra", "Solo los conectores", "La pérdida total suma las tres fuentes."),
        ("=", "{F} ¿Cuántos dB pierde la fibra de 2 km a 3 dB por km?", "2*3", "Se multiplican los kilómetros por la pérdida por kilómetro.", " dB"),
        ("=", "{F} ¿Cuántos dB pierden en total los 2 conectores?", "2*1", "Cada conector pierde 1 dB y son 2.", " dB"),
        ("=", "{F} ¿Cuál es la pérdida total esperada del enlace, en dB?", "2*3+2*1+1", "Se suman la pérdida de fibra, la de los conectores y la del empalme.", " dB"),
        ("abc", "{F} La pérdida esperada es 9 dB y el máximo es 11 dB. ¿Pasa el presupuesto?", "Sí, porque 9 es menor que 11", "No, porque 9 es mayor que 2", "No, porque hay un empalme", "9 está por debajo del máximo aceptado."),
        ("=", "{F} ¿Cuántos dB de margen hay entre la pérdida medida de 9 dB y el máximo?", "11-9", "Se resta la pérdida medida al máximo.", " dB"),
        ("abc", "{F} La medición da 14 dB. ¿Qué corresponde?", "Falla y conviene sospechar un conector sucio o un empalme malo", "Pasa, porque supera la pérdida esperada de 9 dB", "Se corrige restando 3 dB al valor", "14 supera el máximo de 11, por lo que falla."),
        ("abc", "{F} Un técnico de ejemplo mira el extremo de la fibra con la cara muy cerca «para ver si pasa luz». ¿Qué corresponde?", "No hacerlo: puede dañar la vista; se usa el instrumento", "Seguir mirando con más cuidado", "Pedir a un compañero que mire", "La luz de algunos equipos puede dañar los ojos."),
        ("=", "Otro enlace de ejemplo tiene 4 km de fibra a 2 dB por km, 2 conectores de 1 dB y 2 empalmes de 1 dB. ¿Cuántos dB pierde en total?", "4*2+2*1+2*1", "Se suman fibra, conectores y empalmes.", " dB"),
        ("abc", "{F} La medición real de un enlace es 5 dB, menor que los 9 dB esperados. ¿Qué corresponde?", "Revisar si hubo un error de medición antes de aceptar", "Aceptar sin más, porque es mejor", "Sumar 4 dB al informe", "Una medida mucho menor que la esperada también debe revisarse."),
        ("abc", "El cliente de ejemplo pide que el informe diga 9 dB aunque la lectura real fue 12 dB (máximo 11). ¿Qué corresponde?", "Entregar la lectura real e indicar que falla", "Escribir 9 dB", "Escribir 11 dB", "El informe refleja la lectura real."),
    ],
    ctx=("abc", "Una cooperativa de ejemplo pregunta si su enlace de fibra pasa con una pérdida medida de 10 dB y un máximo de 11 dB. ¿Qué respondes?", "Que pasa con 1 dB de margen y que se anotan los valores reales en el informe", "Que falla porque 10 es mayor que 1", "Que no se puede decidir", "10 es menor que 11, por lo que pasa con poco margen."),
    sc=[
        ("En Telecomunicaciones: ¿qué se suma para el presupuesto de pérdida?", "La fibra, los conectores y los empalmes", "Son las fuentes de pérdida del enlace."),
        ("¿Cuántos dB pierde una fibra de 3 km a 2 dB por km?", "6 dB", "Se multiplican los kilómetros por los dB por kilómetro: 3 por 2 son 6."),
        ("¿Se mira el extremo de una fibra con luz?", "No", "La luz del equipo puede dañar los ojos de quien mira."),
    ],
    op=("Un enlace de fibra de ejemplo mide 3 km; la fibra pierde 2 dB por km; tiene 2 conectores de 1 dB y 2 empalmes de 1 dB cada uno. El máximo del proyecto es 12 dB y la medición real es 11 dB. Calcula (a) la pérdida esperada, (b) si la medición pasa, (c) el margen y (d) un cuidado de seguridad con la fibra.",
        "(a) Fibra 3 por 2 son 6 dB; conectores 2 dB; empalmes 2 dB; total 10 dB. (b) Pasa, porque 11 es menor que 12. (c) El margen es 12 menos 11, es decir, 1 dB. (d) No mirar nunca el extremo de una fibra con luz.",
        ["calcula la pérdida esperada", "compara con el máximo y calcula el margen", "nombra un cuidado de seguridad"],
        ["hoja con los cálculos y el cuidado"],
        ["olvidar conectores o empalmes", "restar mal el margen", "no nombrar el cuidado"],
        "Pregunta: «¿qué tres pérdidas sumaste?». Si no responde, pídele que las nombre una por una."),
    reinforce="Calcula la pérdida de una fibra de 5 km a 2 dB por km con 2 conectores de 1 dB.",
    extend="Explica con un ejemplo inventado por qué una medida mucho mayor que la esperada obliga a revisar conectores y empalmes.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (dos informes de ejemplo, inventados). Mismo enlace de la «Oficina Los Alerces» (ficticia) medido por dos técnicos distintos con instrumentos distintos. "
     "Técnico 1 (certificador calibrado, calibración vigente): largo 84 m, atenuación 19 dB. Técnico 2 (probador simple, sin registro de calibración): largo 84 m, atenuación 15 dB. "
     "Criterios de ejemplo: largo máximo 90 m; atenuación máxima 20 dB. Para aceptar un enlace con margen pequeño, el proyecto pide al menos 2 dB de margen de ejemplo en atenuación.")
build(
    O4, 5, F,
    use="Aprenderé a comparar resultados de dos mediciones, a elegir la más confiable y a verificar la calidad antes de entregar.",
    prior=["Sé qué es la calibración y la atenuación.", "Sé calcular un margen.", "Sé que un informe debe ser veraz."],
    explain=[
        "Cuando dos mediciones del mismo enlace dan resultados distintos, no se promedian ni se elige la que conviene. Se compara la confiabilidad de cada una: ¿el instrumento estaba calibrado?, ¿quién midió y cuándo?, ¿la prueba fue la que pide el protocolo? Se confía más en la medición con instrumento calibrado y con registro completo.",
        "Para verificar la calidad se calcula el margen respecto del criterio. Un margen grande da confianza; uno pequeño aconseja repetir la medición. Repetir la prueba con el mismo instrumento y comprobar que da lo mismo se llama repetibilidad. Si los resultados cambian mucho, hay un problema del instrumento, del conector o del procedimiento, y se informa antes de entregar.",
        "La decisión final se anota con el motivo: qué medición se aceptó, por qué y con qué margen. Si hay duda, se vuelve a medir con un instrumento calibrado. Estas decisiones son de papel y datos de ejemplo; hacer las mediciones en terreno exige personal autorizado y norma vigente. " + AVISO,
    ],
    vocab=[("confiabilidad", "grado en que se puede confiar en una medición"), ("repetibilidad", "capacidad de obtener el mismo resultado al repetir la medición"), ("margen pequeño", "diferencia pequeña entre la lectura y el límite"), ("verificar", "comprobar con evidencia que un resultado es correcto")],
    worked=[
        ("Elegir la medición", "Dos mediciones de ejemplo de un mismo enlace difieren. Una usó un instrumento calibrado y la otra no. ¿En cuál se confía más?", ["La calibración vigente da confiabilidad.", "Se confía en la del instrumento calibrado."], "En la del instrumento calibrado"),
        ("Calcular el margen", "La atenuación medida de ejemplo es 17 dB y el máximo es 20 dB. ¿Cuál es el margen?", ["Se resta lo medido al máximo.", "20 menos 17."], "3 dB"),
    ],
    mistakes=[("Promediar dos mediciones distintas «para quedar en el medio».", "Un promedio mezcla una medida confiable con una dudosa.", "Elige la medición con instrumento calibrado y registro completo, o repite."),
              ("Aceptar el enlace porque una medición dio mejor resultado, sin revisar el instrumento.", "El resultado más cómodo no es necesariamente el verdadero.", "Revisa la calibración y repite si hay duda.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la repetibilidad?", "Obtener el mismo resultado al repetir la medición", "Medir con un instrumento distinto cada vez", "Escribir el informe dos veces", "La repetibilidad mide si la prueba da lo mismo al repetirla."),
        ("abc", "Dos mediciones del mismo enlace difieren. ¿Qué se hace primero?", "Comparar la confiabilidad de cada una", "Elegir la que da mejor resultado", "Sacar el promedio", "Se revisa la calibración y el procedimiento de cada medición."),
        ("abc", "¿En qué medición se confía más?", "La de un instrumento calibrado y con registro completo", "La que tiene el número más bajo", "La que se hizo más rápido", "La calibración y el registro dan confiabilidad."),
        ("abc", "{F} ¿Qué medición de la ficha es más confiable?", "La del técnico 1, con certificador calibrado", "La del técnico 2, por ser menor", "Ambas por igual", "El técnico 1 usó un instrumento con calibración vigente."),
        ("=", "{F} ¿Cuántos dB de margen tiene la medición del técnico 1 respecto del máximo?", "20-19", "Se resta la atenuación medida al máximo.", " dB"),
        ("abc", "{F} El proyecto pide al menos 2 dB de margen. ¿Cumple la medición del técnico 1?", "No, porque su margen es 1 dB", "Sí, porque 19 es menor que 20", "Sí, porque el largo cumple", "El margen de 1 dB es menor que los 2 dB pedidos."),
        ("=", "{F} ¿Cuántos dB de diferencia hay entre las dos mediciones de atenuación?", "19-15", "Se resta la medida menor a la mayor.", " dB"),
        ("abc", "{F} ¿Qué corresponde hacer ante esa diferencia?", "Repetir la medición con un instrumento calibrado y revisar los conectores", "Quedarse con el promedio", "Aceptar la menor", "Una diferencia grande exige repetir con un instrumento confiable."),
        ("abc", "{F} Un colega dice: «sacamos el promedio y listo». ¿Qué problema tiene?", "Mezcla una medida confiable con una dudosa", "Es difícil de calcular", "Siempre da un número entero", "El promedio oculta cuál medición es válida."),
        ("=", "{F} Si se repite con el certificador y da 18 dB, ¿cuál es el nuevo margen respecto de 20 dB?", "20-18", "Se resta la nueva medida al máximo.", " dB"),
        ("abc", "{F} Con 18 dB y margen de 2 dB, ¿cumple el criterio del proyecto?", "Sí, porque el margen es de 2 dB como mínimo", "No, porque 2 dB es poco", "No, porque 18 es mayor que 2", "El margen de 2 dB iguala lo pedido por el proyecto."),
        ("abc", "El cliente de ejemplo pide usar la medición del probador simple porque es la que «pasa con holgura». ¿Qué corresponde?", "Explicar que se usa la medición del instrumento calibrado y respaldada por registro", "Aceptar su pedido", "Borrar la otra medición", "Se elige la medición con mayor confiabilidad."),
        ("abc", "Tras repetir tres veces con el mismo certificador, los resultados son 18, 18 y 19 dB. ¿Qué indica esto?", "Buena repetibilidad con una variación pequeña", "Que el instrumento está malo", "Que el enlace tiene fallas de mapa", "Las lecturas casi iguales indican repetibilidad."),
    ],
    ctx=("abc", "Una empresa de ejemplo entrega un enlace con margen de 1 dB cuando el proyecto pide 2 dB, y dice «es casi lo mismo». ¿Qué corresponde?", "Informar que no cumple el margen pedido y proponer revisar conectores o rehacer el tramo con personal autorizado", "Entregarlo sin avisar", "Cambiar la medición por la del probador simple", "El criterio del proyecto manda; no se entrega algo que no cumple."),
    sc=[
        ("En Telecomunicaciones: ¿qué es verificar un resultado?", "Comprobarlo con evidencia", "Se revisa instrumento, registro y margen."),
        ("Con dos mediciones distintas, ¿qué se hace?", "Se compara su confiabilidad y se repite si hay duda", "No se promedian ni se elige la más cómoda."),
        ("¿Cuándo conviene repetir la medición?", "Cuando el margen es pequeño o hay diferencias", "Repetir permite confirmar si el resultado es confiable."),
    ],
    op=("Un mismo enlace de ejemplo se midió dos veces: medición A con certificador calibrado, largo 80 m y atenuación 18 dB; medición B con probador simple sin calibración, largo 80 m y atenuación 12 dB. Criterios de ejemplo: 90 m, 20 dB y un margen de 2 dB. Decide qué medición aceptas, calcula el margen de ella, di si cumple y qué harías con la diferencia.",
        "Se acepta la medición A porque usó un instrumento calibrado. Su margen es 20 menos 18, es decir, 2 dB, y cumple justo el margen pedido. La diferencia con B (6 dB) se informa y se repite la medición con el certificador y se revisan los conectores para confirmar.",
        ["elige la medición confiable con motivo", "calcula el margen y lo compara con 2 dB", "propone repetir y revisar"],
        ["hoja con la decisión, el cálculo y la propuesta"],
        ["promediar las mediciones", "elegir la más baja", "no calcular el margen"],
        "Pregunta: «¿por qué no aceptas la medición B?». Si no responde, pídele que lea la calibración de cada instrumento."),
    reinforce="Escribe dos preguntas que harías para saber si una medición es confiable.",
    extend="Explica con un ejemplo inventado cuándo conviene repetir una medición aunque el enlace haya pasado.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 6 (organización de ejemplo, inventada). El «Hotel Costa Brava» (ficticio) quiere renovar su telefonía: 30 anexos (teléfonos internos de las habitaciones y oficinas), una recepción y una central telefónica que conecta con 6 líneas troncales (líneas hacia la red telefónica pública). "
     "Dos opciones en papel: telefonía tradicional (cable de voz propio) o telefonía IP (voz sobre la red de datos). Aviso del proyecto: las llamadas de emergencia deben poder salir siempre, y no se graban llamadas sin informar y sin la norma vigente.")
build(
    O5, 1, F,
    use="Aprenderé qué es una red de telefonía (tradicional o IP) de una organización, qué normas, riesgos y cuidados de privacidad hay que considerar.",
    prior=["Sé qué es una red LAN y un cable de red.", "Sé qué es un dato personal.", "Sé multiplicar y comparar números."],
    explain=[
        "Una red de telefonía de una organización conecta teléfonos internos y los comunica con la red telefónica pública. El corazón es la central telefónica (PBX), que conmuta las llamadas. Cada teléfono interno tiene un anexo, un número corto. La central se conecta hacia afuera por líneas troncales: cada troncal permite una llamada externa a la vez.",
        "En la telefonía tradicional, la voz viaja por cables propios de voz. En la telefonía IP, la voz se convierte en datos y viaja por la red de datos de la organización, con un protocolo como SIP. La telefonía IP aprovecha el cableado de red, pero depende de que la red de datos esté bien. Las dos pueden convivir en una misma organización.",
        f"Hay cuidados de seguridad y privacidad: las llamadas de emergencia deben poder salir siempre, y grabar o escuchar llamadas ajenas está restringido por la norma vigente, por lo que solo se hace con aviso y autorización. Los teléfonos IP suelen recibir energía por el cable de red, y las instalaciones con energía o en altura las hace personal autorizado. {AVISO}",
    ],
    vocab=[("central telefónica (PBX)", "equipo que conmuta las llamadas de una organización"), ("anexo", "número corto de un teléfono interno"), ("troncal", "línea que conecta la central con la red telefónica pública; permite una llamada externa a la vez"), ("telefonía IP", "telefonía donde la voz viaja como datos por la red"), ("SIP", "protocolo que establece las llamadas de voz sobre IP"), ("conmutar", "conectar entre sí a quien llama y a quien contesta")],
    worked=[
        ("Tipo de línea", "En una oficina de ejemplo hay 20 teléfonos internos con número de 3 cifras y 4 líneas hacia la red pública. ¿Cuántos anexos y cuántas troncales hay?", ["Los teléfonos internos tienen anexos.", "Las líneas hacia la red pública son troncales."], "20 anexos y 4 troncales"),
        ("Llamadas externas a la vez", "Una central de ejemplo tiene 3 troncales. ¿Cuántas llamadas externas puede haber a la vez?", ["Cada troncal permite una llamada externa.", "Con 3 troncales hay 3 llamadas."], "3 llamadas"),
    ],
    mistakes=[("Creer que la telefonía IP no necesita una buena red de datos.", "Si la red falla, también fallan las llamadas.", "Revisa la red de datos antes de proponer telefonía IP."),
              ("Grabar llamadas del personal sin avisar «por seguridad».", "La norma vigente restringe grabar o escuchar llamadas ajenas sin aviso y autorización.", "Informa y obtén autorización antes de grabar.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un anexo?", "El número corto de un teléfono interno", "La línea hacia la red pública", "El equipo que conmuta llamadas", "Un anexo identifica un teléfono dentro de la organización."),
        ("abc", "En Telecomunicaciones: ¿qué es una troncal?", "Una línea que conecta la central con la red telefónica pública", "Un número interno corto", "Un teléfono de recepción", "La troncal da salida a llamadas externas."),
        ("abc", "¿Cómo viaja la voz en la telefonía IP?", "Como datos por la red", "Solo por cables de voz propios", "Por el aire sin equipos", "La telefonía IP convierte la voz en datos."),
        ("abc", "{F} En el Hotel Costa Brava, ¿qué equipo conmuta las llamadas?", "La central telefónica", "El anexo de recepción", "La troncal", "La central telefónica conmuta las llamadas."),
        ("=", "{F} ¿Cuántas llamadas externas pueden estar al mismo tiempo?", "6", "Cada una de las 6 troncales permite una llamada externa.", " llamadas"),
        ("=", "{F} Si 4 de los 30 anexos son de oficinas y el resto de habitaciones, ¿cuántos anexos son de habitaciones?", "30-4", "Se restan los de oficinas al total de anexos.", " anexos"),
        ("abc", "{F} Un integrante del equipo propone grabar todas las llamadas de recepción para controlar al personal, sin avisar. ¿Qué corresponde?", "No hacerlo sin aviso ni autorización, según la norma vigente", "Hacerlo en secreto", "Grabar solo las de los clientes", "La grabación de llamadas está restringida y exige aviso y autorización."),
        ("abc", "{F} Una llamada de emergencia no sale por falta de troncales. ¿Qué principio del proyecto se rompe?", "Las llamadas de emergencia deben poder salir siempre", "Los anexos deben ser de dos cifras", "Todos los teléfonos deben ser IP", "El proyecto exige que las llamadas de emergencia puedan salir siempre."),
        ("abc", "Un hotel de ejemplo quiere pasar a telefonía IP. ¿Qué debe revisar antes?", "Que su red de datos soporte el tráfico de voz", "Que los colores de los teléfonos coincidan", "Que haya más anexos que troncales", "Si la red de datos falla, también fallan las llamadas."),
        ("=", "Un hotel de ejemplo tiene 18 habitaciones por piso y 5 pisos. Si cada habitación tiene un anexo, ¿cuántos anexos de habitaciones son?", "18*5", "Se multiplican las habitaciones por piso por los pisos.", " anexos"),
        ("abc", "Un técnico de ejemplo ve en el panel de la central los números marcados por un empleado. ¿Qué corresponde?", "Usar esa información solo para el trabajo autorizado y no comentarla", "Comentarla con sus compañeros", "Anotarla para curiosear después", "Los datos de llamadas son personales y se usan solo para el fin autorizado."),
        ("abc", "{F} El proyecto de telefonía IP incluye subir a un techo a instalar un cable por una canaleta alta. ¿Qué corresponde a un estudiante?", "Dejarlo a personal autorizado con norma vigente y protección", "Subir con una escalera prestada", "Pedirle a un amigo que suba", "El trabajo en altura exige personal autorizado."),
        ("abc", "{F} ¿Pueden convivir telefonía tradicional e IP en un mismo hotel?", "Sí, pueden convivir durante una transición", "No, es imposible", "Solo si se cambia toda la red de datos primero", "Muchas organizaciones mantienen ambas durante el cambio."),
    ],
    ctx=("abc", "La gerente de un hotel de ejemplo pide saber si 6 troncales bastan para 30 anexos. ¿Qué respondes?", "Que depende de cuántas llamadas externas simultáneas se esperan; con 6 troncales solo hay 6 a la vez", "Que sí, porque 6 troncales alcanzan para cualquier número de anexos", "Que no, porque cada anexo necesita su troncal", "Las troncales limitan las llamadas externas a la vez, no el número de anexos."),
    sc=[
        ("En Telecomunicaciones: ¿cuántas llamadas externas permite cada troncal?", "Una a la vez", "Por eso el número de troncales limita las llamadas externas simultáneas."),
        ("¿Se pueden grabar llamadas sin avisar?", "No", "La norma vigente exige aviso y autorización."),
        ("¿Quién trabaja en altura o con energía?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
    ],
    op=("Un colegio de ejemplo tiene 25 anexos (aulas y oficinas) y contrata 4 troncales. Escribe (a) cuántas llamadas externas puede haber a la vez, (b) una ventaja y un riesgo de pasar a telefonía IP y (c) una regla de privacidad para las llamadas del personal.",
        "(a) 4 llamadas a la vez. (b) Ventaja: aprovecha el cableado de red; riesgo: depende de que la red de datos funcione bien. (c) No grabar ni escuchar llamadas sin aviso y autorización, según la norma vigente.",
        ["calcula las llamadas simultáneas", "nombra una ventaja y un riesgo", "plantea una regla de privacidad"],
        ["hoja con las tres respuestas"],
        ["confundir anexos con troncales", "decir que la IP no depende de la red", "proponer grabar sin avisar"],
        "Pregunta: «¿cuántas llamadas externas simultáneas hay con 4 troncales?». Si no responde, pídele que dibuje 4 líneas hacia la red pública."),
    reinforce="Escribe la diferencia entre anexo y troncal con un ejemplo inventado.",
    extend="Explica con un ejemplo inventado por qué una caída de la red de datos afecta más a la telefonía IP que a la tradicional.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 7 (datos de ejemplo, inventados). Telefonía IP de la «Empresa Aurora» (ficticia). Datos de ejemplo: cada llamada usa 100 kbps (kilobits por segundo) del enlace; 1 Mbps (megabit por segundo) son 1.000 kbps; "
     "la voz necesita poca demora (latencia) y poca variación en esa demora (jitter); los teléfonos IP se identifican por su anexo y reciben energía por el cable de red (PoE). "
     "Documentos: plan de numeración, diagrama de la red de voz, inventario de teléfonos y política de uso. Roles: administrador de telefonía, técnico de soporte y usuario.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario de la telefonía IP (códec, latencia, jitter, VLAN de voz, PoE), los documentos y los roles del equipo.",
    prior=["Sé qué es un anexo, una troncal y una central.", "Sé qué es una red LAN.", "Sé multiplicar."],
    explain=[
        "En telefonía IP, la voz se convierte en datos con un códec, que es el método que comprime y reconstruye la voz. Cada llamada usa un ancho de banda, medido en kilobits por segundo (kbps). La calidad depende de la latencia (la demora de la voz en llegar), del jitter (la variación de esa demora) y de la pérdida de paquetes (datos de voz que no llegan). Si hay demasiada demora o pérdida, la voz se corta o suena entrecortada.",
        "Para cuidar la calidad se separa el tráfico de voz en una red virtual propia (VLAN de voz) y se le da prioridad sobre el resto del tráfico (QoS, calidad de servicio). Los teléfonos IP pueden recibir energía por el mismo cable de red (PoE), por lo que no necesitan un enchufe aparte. El plan de numeración define qué anexos se asignan a cada área.",
        "Los documentos del trabajo son el plan de numeración, el diagrama de la red de voz, el inventario de teléfonos y la política de uso. El administrador de telefonía configura la central, el técnico de soporte atiende las fallas y el usuario cumple la política. Todo cambio queda en el registro. " + AVISO,
    ],
    vocab=[("códec", "método que comprime y reconstruye la voz digital"), ("kbps", "kilobits por segundo: medida de ancho de banda"), ("latencia", "demora de la voz en llegar"), ("jitter", "variación de la demora entre paquetes"), ("VLAN de voz", "red virtual propia para el tráfico de voz"), ("QoS", "calidad de servicio: dar prioridad al tráfico de voz"), ("PoE", "energía por el mismo cable de red")],
    worked=[
        ("Ancho de banda de llamadas", "En un enlace de ejemplo, cada llamada usa 100 kbps y hay 5 llamadas a la vez. ¿Cuántos kbps se usan?", ["Se multiplica lo que usa una llamada por las llamadas.", "100 por 5."], "500 kbps"),
        ("Qué mide el jitter", "En una llamada de ejemplo, la demora de la voz varía mucho entre un paquete y otro. ¿Qué medida describe eso?", ["La demora se llama latencia.", "La variación de la demora es el jitter."], "El jitter"),
    ],
    mistakes=[("Confundir latencia con jitter.", "La latencia es la demora; el jitter es la variación de esa demora.", "Pregunta: ¿es cuánto tarda o cuánto varía?"),
              ("Mezclar el tráfico de voz con la descarga de archivos grandes sin prioridad.", "La voz se entrecorta si espera en la fila de datos.", "Usa una VLAN de voz y QoS.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la latencia?", "La demora de la voz en llegar", "La variación de esa demora", "El nombre del códec", "La latencia mide cuánto tarda la voz; el jitter mide su variación."),
        ("abc", "En Telecomunicaciones: ¿para qué sirve una VLAN de voz?", "Para separar el tráfico de voz en una red virtual propia", "Para grabar las llamadas", "Para aumentar el número de anexos", "La VLAN aísla y ordena el tráfico de voz."),
        ("abc", "¿Qué hace el PoE?", "Entrega energía a un teléfono por el cable de red", "Comprime la voz", "Traduce nombres a direcciones", "PoE alimenta el equipo por el mismo cable de red."),
        ("=", "{F} Si hay 8 llamadas a la vez, ¿cuántos kbps de ancho de banda usan?", "8*100", "Se multiplican las llamadas por lo que usa cada una.", " kbps"),
        ("=", "{F} ¿Cuántos kbps son 2 Mbps?", "2*1000", "1 Mbps son 1.000 kbps.", " kbps"),
        ("=", "{F} Un enlace de 2 Mbps (2.000 kbps) está disponible solo para voz. ¿Cuántas llamadas simultáneas caben, a 100 kbps cada una?", "2000//100", "Se divide el ancho de banda por lo que usa cada llamada.", " llamadas"),
        ("abc", "{F} ¿Qué documento define qué anexos se asignan a cada área?", "El plan de numeración", "El inventario de teléfonos", "La política de uso", "El plan de numeración reparte los anexos."),
        ("abc", "{F} Un usuario se queja de que la voz de su teléfono se entrecorta cuando alguien descarga un archivo muy grande. ¿Qué mejora se propone?", "Dar prioridad a la voz con QoS y una VLAN de voz", "Cambiar el color del teléfono", "Quitar el anexo", "La prioridad evita que la voz espere tras los datos."),
        ("abc", "{F} Un teléfono IP de ejemplo no tiene enchufe cerca. ¿Qué característica permite alimentarlo por el cable de red?", "PoE", "SIP", "Jitter", "PoE entrega energía por el cable de red."),
        ("abc", "Una llamada de ejemplo llega con 400 milisegundos (milésimas de segundo) de demora y se corta. ¿Qué medida es la que está mal?", "La latencia", "El anexo", "La política de uso", "Una demora grande es latencia alta."),
        ("=", "En una oficina de ejemplo caben 20 llamadas en el ancho de banda de voz y ya hay 12. ¿Cuántas llamadas más caben?", "20-12", "Se restan las llamadas en curso a las que caben.", " llamadas"),
        ("abc", "El técnico de soporte de ejemplo recibe un teléfono nuevo y copia el anexo de otro empleado, porque «son de la misma área». ¿Qué problema crea?", "Dos teléfonos con el mismo anexo, y las llamadas se confunden", "Ninguno, porque dos teléfonos pueden compartir anexo sin problema", "Se baja la latencia", "Cada anexo debe ser único dentro de la organización."),
        ("abc", "{F} Una usuaria usa el teléfono de la empresa para asuntos personales, contra la política de uso. ¿Quién fija esas reglas?", "La organización, en la política de uso", "El técnico de soporte a su gusto", "El proveedor de internet", "La política de uso es un documento de la organización."),
    ],
    ctx=("abc", "El administrador de telefonía de ejemplo ve que 30 llamadas a la vez usarían 3.000 kbps, pero la VLAN de voz solo tiene 2.000 kbps. ¿Qué concluye?", "Que no caben todas y debe ampliar el ancho de banda o limitar las llamadas", "Que sí caben porque 30 es menor que 2.000", "Que el PoE lo resuelve", "3.000 kbps superan los 2.000 kbps disponibles."),
    sc=[
        ("En Telecomunicaciones: ¿qué mide la latencia?", "La demora de la voz en llegar", "El jitter mide la variación de esa demora entre paquetes."),
        ("¿Cuántos kbps son 1 Mbps?", "1.000 kbps", "Mega es mil veces kilo, por eso 1 Mbps son 1.000 kbps."),
        ("¿Para qué se usa QoS?", "Para dar prioridad al tráfico de voz", "La voz no debe esperar tras los datos."),
    ],
    op=("Una clínica de ejemplo planea telefonía IP con 15 llamadas simultáneas máximas a 100 kbps cada una y un enlace de voz de 2 Mbps. Calcula (a) los kbps que usarían las 15 llamadas, (b) si caben en 2 Mbps, (c) cuántas llamadas más podrían agregarse y (d) una medida para cuidar la calidad de la voz.",
        "(a) 15 por 100 son 1.500 kbps. (b) Caben, porque 2 Mbps son 2.000 kbps. (c) Quedan 500 kbps, es decir, 5 llamadas más. (d) Una VLAN de voz con QoS para dar prioridad a la voz.",
        ["calcula los kbps de las llamadas", "compara con los 2 Mbps convertidos", "propone una medida de calidad"],
        ["hoja con los cálculos y la medida"],
        ["no convertir Mbps a kbps", "sumar en vez de multiplicar", "olvidar la prioridad de la voz"],
        "Pregunta: «¿cuántos kbps son 2 Mbps?». Si no responde, pídele que recuerde la equivalencia de la ficha."),
    reinforce="Calcula los kbps que usan 6 llamadas simultáneas de 100 kbps cada una.",
    extend="Explica con un ejemplo inventado qué le pasa a una llamada si no hay prioridad para la voz.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 8 (caso de ejemplo, inventado). La «Distribuidora Norte Sur» (ficticia) tiene 4 áreas con anexos: Ventas 101 a 108; Bodega 109 a 112; Administración 113 a 118; Gerencia 119 y 120. "
     "Tabla de teléfonos entregada por el cliente: teléfono 1 anexo 105; teléfono 2 anexo 105; teléfono 3 anexo 130; teléfono 4 anexo 118; teléfono 5 anexo 112. "
     "Enlace de voz de 1 Mbps (1.000 kbps), 100 kbps por llamada. Troncales contratadas: 4. Hora de mayor uso de ejemplo: 7 llamadas externas a la vez.")
build(
    O5, 3, F,
    use="Aprenderé a analizar en papel el plan de numeración y la capacidad de una red de telefonía y a detectar errores.",
    prior=["Sé qué es un anexo y una troncal.", "Sé calcular kbps por llamada.", "Sé comparar cantidades con un límite."],
    explain=[
        "Analizar una red de telefonía en papel es contrastar tres cosas: el plan de numeración, la capacidad de las troncales y el ancho de banda. En el plan de numeración, cada anexo debe ser único y pertenecer al rango de su área. Un anexo repetido o fuera de rango es un error de configuración.",
        "La capacidad de las troncales se compara con las llamadas externas simultáneas que se esperan en la hora de mayor uso. Si se esperan más llamadas que troncales, algunas personas recibirán señal de ocupado. El ancho de banda se compara así: llamadas a la vez por lo que usa cada llamada, contra el ancho de banda del enlace de voz.",
        "El análisis termina en una lista de hallazgos con su corrección propuesta, que se informa al administrador de telefonía. No se modifica la configuración de una central real sin autorización. Este caso es de papel con datos inventados. " + AVISO,
    ],
    vocab=[("rango de numeración", "grupo de anexos asignado a un área"), ("hora de mayor uso", "momento con más llamadas simultáneas"), ("señal de ocupado", "aviso de que no hay troncales libres"), ("hallazgo", "error o riesgo encontrado al revisar")],
    worked=[
        ("Anexo fuera de rango", "El área de ejemplo Ventas tiene los anexos 201 a 205. Un teléfono de Ventas tiene el anexo 210. ¿Qué error hay?", ["Se compara 210 con el rango 201 a 205.", "210 no está en el rango."], "El anexo está fuera del rango del área"),
        ("Troncales insuficientes", "Una empresa de ejemplo tiene 3 troncales y espera 5 llamadas externas a la vez. ¿Cuántas personas recibirán señal de ocupado?", ["Se restan las troncales a las llamadas esperadas.", "5 menos 3."], "2 llamadas sin troncal"),
    ],
    mistakes=[("Revisar los anexos uno por uno sin comparar con el rango del área.", "Un anexo puede ser único y aun así estar en el área equivocada.", "Compara cada anexo con su rango."),
              ("Aprobar la capacidad mirando solo el promedio del día.", "Los problemas aparecen en la hora de mayor uso.", "Calcula con la hora de mayor uso.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la hora de mayor uso?", "El momento con más llamadas simultáneas", "La hora en que se apaga la central", "La hora de entrada del personal", "La capacidad se diseña para el momento de mayor uso."),
        ("abc", "¿Qué pasa si hay más llamadas externas simultáneas que troncales?", "Algunas personas reciben señal de ocupado", "Se cae toda la red", "Se duplican los anexos", "Sin troncales libres, la llamada no sale."),
        ("abc", "¿Qué error es tener dos teléfonos con el mismo anexo?", "Un anexo repetido", "Un anexo fuera de rango", "Una troncal de más", "Cada anexo debe ser único dentro de la organización."),
        ("abc", "{F} ¿Qué teléfonos de la tabla comparten anexo?", "Teléfono 1 y teléfono 2", "Teléfono 3 y teléfono 4", "Teléfono 4 y teléfono 5", "Ambos teléfonos tienen asignado el mismo anexo, 105, y eso es un error."),
        ("abc", "{F} El teléfono 3 tiene el anexo 130. ¿Qué error hay?", "Está fuera de todos los rangos del plan", "Es un anexo repetido", "Es un anexo de Gerencia", "130 es mayor que 120, el último anexo del plan."),
        ("abc", "{F} El teléfono 5 tiene el anexo 112. ¿A qué área corresponde?", "Bodega", "Ventas", "Gerencia", "112 está en el rango de Bodega, de 109 a 112."),
        ("=", "{F} ¿Cuántos anexos tiene el área de Ventas, de 101 a 108, ambos incluidos?", "108-101+1", "Se resta el inicio al final y se suma 1 porque se incluyen ambos.", " anexos"),
        ("=", "{F} ¿Cuántas llamadas externas se quedarán sin troncal en la hora de mayor uso?", "7-4", "Se restan las troncales a las llamadas esperadas.", " llamadas"),
        ("=", "{F} ¿Cuántos kbps usarían las 7 llamadas a la vez?", "7*100", "Se multiplican las llamadas por lo que usa cada una.", " kbps"),
        ("abc", "{F} ¿Cabe el tráfico de 7 llamadas en el enlace de 1 Mbps?", "Sí, porque 700 kbps es menor que 1.000 kbps", "No, porque 700 es mayor que 1", "No, porque hay solo 4 troncales", "700 kbps es menor que los 1.000 kbps del enlace."),
        ("abc", "{F} ¿Cuántas troncales harían falta para esa hora de mayor uso?", "7", "4", "11", "Con 7 llamadas externas a la vez hacen falta 7 troncales."),
        ("abc", "{F} Una persona propone cambiar de inmediato en la central real el anexo 130 por el 121. ¿Qué corresponde?", "Informar al administrador de telefonía y esperar autorización", "Hacer el cambio sin avisar", "Borrar el teléfono 3", "Los cambios en una central real los autoriza el administrador."),
        ("abc", "{F} Dos hallazgos del plan son el anexo repetido y el anexo fuera de rango. ¿Cuántos teléfonos de la tabla tienen alguno de esos errores?", "3", "2", "5", "Los teléfonos 1 y 2 repiten el anexo y el 3 está fuera de rango."),
    ],
    ctx=("abc", "El gerente de ejemplo dice: «hay 4 troncales, es lo que hemos pagado, no hace falta más». Pero en la hora de mayor uso se esperan 7 llamadas. ¿Qué respondes?", "Que 3 llamadas quedarán sin troncal y que propones ampliar o aceptar ese riesgo por escrito", "Que todo está bien", "Que hay que cambiar los teléfonos", "7 llamadas superan las 4 troncales; la decisión se registra."),
    sc=[
        ("En Telecomunicaciones: ¿qué debe cumplir un anexo?", "Ser único y estar en el rango de su área", "Así no se confunden las llamadas."),
        ("¿Con qué hora se diseña la capacidad?", "Con la hora de mayor uso", "Es cuando hay más llamadas a la vez."),
        ("¿Quién autoriza cambios en la central?", "El administrador de telefonía", "Los cambios en la central no se hacen sin autorización."),
    ],
    op=("Plan de ejemplo de un taller: Mecánica anexos 21 a 25; Oficina anexos 26 a 28. Tabla: teléfono A anexo 22; teléfono B anexo 22; teléfono C anexo 27; teléfono D anexo 31. Hay 2 troncales y se esperan 3 llamadas externas a la vez, a 100 kbps cada una, en un enlace de 500 kbps. Escribe los hallazgos y una corrección propuesta.",
        "Hallazgos: 1) A y B repiten el anexo 22. 2) D tiene el anexo 31, fuera del plan. 3) Con 2 troncales y 3 llamadas, 1 queda sin troncal. 4) 3 llamadas usan 300 kbps y caben en 500 kbps. Propuesta: cambiar el anexo de B o A a uno libre del rango, asignar a D un anexo del plan y ampliar a 3 troncales, todo con autorización.",
        ["detecta anexos repetidos y fuera de rango", "compara troncales y ancho de banda", "propone correcciones con autorización"],
        ["lista de hallazgos con correcciones"],
        ["no ver el anexo repetido", "no calcular el ancho de banda", "corregir sin autorización"],
        "Pregunta: «¿qué anexos están repetidos y cuáles fuera de rango?». Si no responde, pídele que compare con el plan."),
    reinforce="Revisa en papel una lista de cuatro anexos de ejemplo y marca cuál está repetido.",
    extend="Explica con un ejemplo inventado por qué la hora de mayor uso importa más que el promedio del día.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 9 (criterio técnico con datos de ejemplo, inventados). La «Municipalidad de Ejemplo» (ficticia) renueva su telefonía. Datos de ejemplo: 60 anexos; se espera que, en la hora de mayor uso, el 20 % de los anexos hable con el exterior a la vez; "
     "cada llamada usa 100 kbps; la VLAN de voz tiene 2 Mbps (2.000 kbps); cada troncal permite 1 llamada externa; las troncales se contratan de a 2. Regla de ejemplo del proyecto: dejar al menos un 20 % de ancho de banda libre.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular las troncales y el ancho de banda de voz y comprobar el margen.",
    prior=["Sé qué es una troncal y un kbps.", "Sé calcular un porcentaje simple.", "Sé convertir Mbps a kbps."],
    explain=[
        "El criterio técnico para dimensionar una red de telefonía parte de las llamadas externas esperadas en la hora de mayor uso. Una forma simple es usar un porcentaje de los anexos que hablan con el exterior a la vez (aquí, 20 % de ejemplo). Con eso se calculan las troncales: una por llamada, redondeando hacia arriba cuando el proveedor las vende de a más de una.",
        "Después se calcula el ancho de banda de voz: llamadas simultáneas por lo que usa cada llamada. Se compara con el enlace de voz y se verifica el margen de reserva que pide el proyecto, como dejar libre al menos un 20 %. Si el cálculo supera lo disponible, se propone ampliar el enlace o reducir las llamadas simultáneas.",
        "La conclusión se escribe con los números y se entrega a la jefatura. Los valores reales de tráfico y de contratos dependen del proveedor y de la norma vigente; aquí se usan solo cifras de ejemplo. Instalar equipos y cableado en una organización exige personal autorizado. " + AVISO,
    ],
    vocab=[("dimensionar", "calcular cuánta capacidad hace falta"), ("llamadas simultáneas", "llamadas que ocurren a la vez"), ("redondear hacia arriba", "subir a la cantidad entera siguiente cuando no alcanza"), ("reserva", "parte de la capacidad que se deja libre")],
    worked=[
        ("Porcentaje de anexos", "Una oficina de ejemplo tiene 50 anexos y se espera que el 10 % hable con el exterior a la vez. ¿Cuántas llamadas externas simultáneas se esperan?", ["El 10 % de 50 es 50 dividido por 10.", "50 entre 10 son 5."], "5 llamadas"),
        ("Troncales de a 2", "Se necesitan 5 troncales y se venden de a 2. ¿Cuántas se contratan?", ["Con 2 troncales por paquete, 5 no se completa: dos paquetes dan 4 y tres paquetes dan 6.", "Se redondea hacia arriba: 6."], "6 troncales"),
    ],
    mistakes=[("Contratar justo las troncales calculadas, aunque el proveedor las venda de a 2 y falte una.", "Si falta una, algunas llamadas no saldrán.", "Redondea hacia arriba al paquete siguiente."),
              ("Usar todo el ancho de banda de voz sin dejar reserva.", "Un pequeño aumento de llamadas lo satura.", "Deja la reserva que pide el proyecto.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué significa dimensionar una red de telefonía?", "Calcular cuánta capacidad hace falta", "Pintar los cables", "Cambiar de proveedor", "Dimensionar es calcular las troncales y el ancho de banda necesarios."),
        ("abc", "Si se necesitan 5 troncales y se venden de a 2, ¿cuántas se contratan?", "6", "5", "4", "Con 4 faltaría una; se redondea hacia arriba a 6."),
        ("abc", "¿Por qué se deja una reserva de ancho de banda?", "Para soportar más llamadas sin saturar el enlace", "Para que el teléfono pese menos", "Para reducir los anexos", "La reserva absorbe aumentos de uso."),
        ("=", "{F} ¿Cuántas llamadas externas simultáneas se esperan (20 % de 60 anexos)?", "60//5", "El 20 % es la quinta parte, es decir, 60 dividido por 5.", " llamadas"),
        ("=", "{F} Con esas llamadas, ¿cuántas troncales se contratan si se venden de a 2 y se redondea hacia arriba?", "(12+1)//2*2", "Se necesitan 12 troncales y 12 ya es múltiplo de 2, por lo que no hay que subir.", " troncales"),
        ("=", "{F} ¿Cuántos kbps usarían las 12 llamadas simultáneas?", "12*100", "Se multiplican las llamadas por lo que usa cada una.", " kbps"),
        ("=", "{F} El proyecto pide dejar libre un 20 % de los 2.000 kbps. ¿Cuántos kbps deben quedar libres?", "2000//5", "El 20 % es la quinta parte de 2.000.", " kbps"),
        ("=", "{F} ¿Cuántos kbps se pueden usar como máximo para voz, sin tocar la reserva?", "2000-2000//5", "Se restan los kbps de reserva a los 2.000 kbps.", " kbps"),
        ("abc", "{F} Las 12 llamadas usan 1.200 kbps. ¿Cumplen el límite de uso máximo de 1.600 kbps?", "Sí, porque 1.200 es menor que 1.600", "No, porque 1.200 es mayor que 100", "No, porque hay 12 troncales", "1.200 kbps está por debajo del máximo de 1.600 kbps."),
        ("=", "{F} Si se agregan 30 anexos más y el 20 % habla a la vez, ¿cuántas llamadas simultáneas más se esperan?", "30//5", "El 20 % de 30 es 30 dividido por 5.", " llamadas"),
        ("abc", "{F} Con esas 6 llamadas más hay 18 llamadas simultáneas en total y usan 1.800 kbps. ¿Cumple el límite de 1.600 kbps?", "No, porque 1.800 supera los 1.600 kbps", "Sí, porque 1.800 es menor que 2.000", "Sí, porque hay reserva", "Aunque quepa en 2.000, invade la reserva exigida."),
        ("abc", "{F} Para ese caso de 18 llamadas, ¿qué propone el técnico?", "Ampliar el ancho de banda de voz o limitar las llamadas, según decida la jefatura", "Quitar la regla de reserva", "Borrar 30 anexos", "Se propone una solución respetando el criterio del proyecto."),
        ("abc", "Una persona calcula 20 % de 60 anexos como 20 llamadas. ¿Cuál es su error?", "Usó 20 como si fuera el resultado en vez de calcular el 20 % de 60", "Olvidó la troncal", "Confundió kbps con Mbps", "El 20 % de 60 es 12, no 20."),
    ],
    ctx=("abc", "La directora de ejemplo quiere contratar menos troncales para ahorrar y propone que «con 8 alcanza». El cálculo da 12. ¿Qué respondes?", "Que con 8 algunas llamadas no saldrán en la hora de mayor uso y que la decisión debe quedar por escrito", "Que 8 es más que 12", "Que se cambie el cálculo a 8", "8 troncales dejan 4 llamadas sin salida; el riesgo se informa."),
    sc=[
        ("En Telecomunicaciones: ¿qué es la reserva de ancho de banda?", "La parte de capacidad que se deja libre", "La reserva evita saturar el enlace si aumentan las llamadas."),
        ("¿Cuántos kbps usan 10 llamadas de 100 kbps?", "1.000 kbps", "Se multiplican las llamadas por lo que usa cada una: 10 por 100 son 1.000."),
        ("¿Qué se hace si el cálculo supera el enlace?", "Se propone ampliar el enlace o limitar las llamadas", "La jefatura decide con los números."),
    ],
    op=("Un colegio de ejemplo tiene 40 anexos. Se espera que el 25 % hable con el exterior a la vez. Cada llamada usa 100 kbps y la VLAN de voz tiene 1,5 Mbps, es decir, 1.500 kbps; el proyecto pide dejar libre al menos 20 %. Calcula (a) las llamadas simultáneas, (b) los kbps que usan, (c) el máximo utilizable sin tocar la reserva y (d) si cumple.",
        "(a) 25 % de 40 son 10 llamadas. (b) 10 por 100 son 1.000 kbps. (c) La reserva es 300 kbps, así que se pueden usar hasta 1.200 kbps. (d) Cumple, porque 1.000 es menor que 1.200.",
        ["calcula las llamadas con el porcentaje", "calcula kbps, reserva y máximo", "concluye si cumple"],
        ["hoja con los cuatro cálculos"],
        ["calcular mal el porcentaje", "olvidar la reserva", "mezclar Mbps con kbps"],
        "Pregunta: «¿cuánto es el 20 % de 1.500?». Si no responde, pídele que divida 1.500 por 5."),
    reinforce="Calcula las llamadas simultáneas si el 10 % de 80 anexos habla a la vez.",
    extend="Explica con un ejemplo inventado por qué se redondea hacia arriba al contratar troncales.",
)

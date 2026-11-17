"""Conectividad y Redes TP 3.º y 4.º medio: OAE-01 (leer proyectos de redes LAN, TCP/IP y OSI), OAE-02 (sistemas operativos en una LAN) y OAE-03 (cableado estructurado, solo conceptos). Redes, direcciones e importes inventados; sin equipos ni software."""
from __future__ import annotations

from tp_core_common import build

O1 = "TP-CORE-3y4-OAE-01"
O2 = "TP-CORE-3y4-OAE-02"
O3 = "TP-CORE-3y4-OAE-03"
AVISO = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). «Oficina Contable Mirador»: un piso con 12 puestos de trabajo, 1 impresora de red, 1 punto de acceso Wi-Fi y 1 rack (gabinete de equipos) en una sala técnica. "
     "Cada puesto lleva 2 puntos de red; la impresora y el punto de acceso usan 1 punto cada uno. Documentos del proyecto: plano de planta, diagrama de la red, listado de equipos y memoria técnica. "
     "Roles: jefa de proyecto, técnico en conectividad, cliente.")
build(
    O1, 1, F,
    use="Aprenderé qué es una red LAN, qué documentos tiene un proyecto de conectividad, quién participa y qué riesgos hay al leerlo y compartirlo.",
    prior=["Sé sumar, restar y multiplicar cifras.", "Sé leer una tabla simple.", "Sé que los computadores se conectan entre sí."],
    explain=[
        "Una red de área local (LAN) conecta computadores, impresoras y otros equipos dentro de un espacio limitado, como una oficina o un liceo. Un proyecto de conectividad y redes se comunica con documentos: el plano de planta muestra dónde está cada punto de red, y el diagrama de la red muestra cómo se conectan los equipos entre sí. Leer bien estos documentos es la primera tarea de un técnico.",
        "Trabajar con redes tiene normas y riesgos. La norma vigente y las especificaciones del proyecto mandan sobre la costumbre. Los riesgos más comunes son leer mal un plano y pedir materiales de menos, compartir un diagrama con quien no debe verlo porque muestra cómo está protegida la red, y cambiar un documento sin dejar registro. También importa la ergonomía: se trabaja con buena postura y pausas.",
        "El técnico no decide solo: responde a la jefa de proyecto, respeta lo que pidió el cliente y registra lo que hace." + AVISO,
    ],
    vocab=[("LAN", "red de área local; conecta equipos en un espacio limitado"), ("plano de planta", "dibujo que muestra la ubicación física de puntos y equipos"), ("diagrama de la red", "dibujo que muestra cómo se conectan los equipos"), ("rack", "gabinete donde se instalan los equipos de red"), ("punto de red", "toma donde se conecta un equipo a la red"), ("memoria técnica", "documento que explica lo que se diseñó y por qué"), ("confidencialidad", "reservar la información para quien corresponde")],
    worked=[
        ("Contar puntos de red", "Un proyecto de ejemplo tiene 5 puestos con 2 puntos cada uno y 1 impresora con 1 punto. ¿Cuántos puntos de red hay?", ["Puestos: 5 × 2 = 10 puntos.", "Se suma la impresora: 10 + 1 = 11."], "11 puntos de red"),
        ("Elegir el documento", "Quieres saber en qué muro va un punto de red. ¿Consultas el plano de planta o el diagrama de la red?", ["La ubicación física está en el plano de planta.", "El diagrama muestra conexiones entre equipos, no su lugar en el edificio."], "El plano de planta"),
    ],
    mistakes=[("Enviar el diagrama completo de la red de un cliente a un amigo «para mostrar lo que hice».", "El diagrama revela cómo está organizada y protegida la red del cliente: es información confidencial.", "Pide autorización a la jefa de proyecto y comparte solo una versión sin datos sensibles."),
              ("Cambiar una medida del plano con corrector sin avisar.", "Un documento alterado sin registro deja de ser confiable para todo el equipo.", "Avisa, propone el cambio y deja constancia de quién lo aprobó.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una LAN?", "Una red que conecta equipos dentro de un espacio limitado, como una oficina", "Una red que une países con cables submarinos", "Un programa para dibujar planos", "LAN significa red de área local: cubre un espacio pequeño como una oficina o un liceo."),
        ("abc", "¿Qué muestra un plano de planta?", "Dónde está ubicado físicamente cada punto de red y cada equipo", "Qué clave usa cada persona", "Cuánto cuesta cada equipo", "El plano de planta ubica las cosas en el edificio; no guarda claves ni precios."),
        ("abc", "¿Qué muestra un diagrama de la red?", "Cómo se conectan entre sí los equipos", "En qué muro está cada punto", "Cuánto mide cada habitación", "El diagrama dibuja las conexiones lógicas entre equipos y no las medidas del edificio."),
        ("abc", "{F} ¿Quién coordina el proyecto y responde ante el cliente?", "La jefa de proyecto", "El técnico por su cuenta", "El punto de acceso Wi-Fi", "Según la ficha, la jefa de proyecto coordina; el técnico ejecuta y registra lo que hace."),
        ("abc", "{F} ¿Qué documento detalla qué equipos hay y cuántos?", "El listado de equipos", "El diagrama de la red", "El plano de planta", "El listado de equipos enumera los equipos; el diagrama y el plano muestran conexiones y ubicación."),
        ("=", "{F} ¿Cuántos puntos de red tiene el proyecto en total?", "12*2+1+1", "Se multiplican los puestos por 2 y se suman la impresora y el punto de acceso.", " puntos"),
        ("=", "{F} Se compran 30 cables de red, uno por punto. ¿Cuántos cables sobran?", "30-(12*2+1+1)", "A los cables comprados se les resta la cantidad de puntos del proyecto.", " cables"),
        ("=", "{F} El cliente agrega 5 puestos de trabajo con 2 puntos cada uno. ¿Cuántos puntos de red habrá ahora?", "(12+5)*2+1+1", "Con 17 puestos se multiplica por 2 y se suman los 2 puntos de impresora y acceso.", " puntos"),
        ("abc", "{F} Un técnico cuenta 20 puntos en vez de 26. ¿Qué riesgo produce ese error?", "Se comprarían materiales de menos y el trabajo se atrasaría", "Se perdería la clave del punto de acceso", "El plano de planta cambiaría de color", "Contar de menos deja puntos sin cable ni material y obliga a rehacer pedidos."),
        ("abc", "Una compañera quiere subir a una red social una foto del diagrama de una oficina real, con los nombres de los equipos. ¿Qué principio rompe?", "La confidencialidad de la información del cliente", "La ergonomía del puesto de trabajo", "La escala del plano de planta", "El diagrama muestra la estructura de la red y debe reservarse para quien corresponde."),
        ("abc", "Un técnico de ejemplo cambia una medida del plano sin avisar y sin dejar registro. ¿Qué práctica profesional incumple?", "Registrar y avisar cada cambio a los documentos del proyecto", "Usar siempre lápiz grafito", "Archivar el plano en el rack", "Los cambios sin registro hacen que el equipo trabaje con datos distintos."),
        ("abc", "{F} Un compañero dice: «el diagrama sirve para medir cuántos metros de cable hay que comprar». ¿Qué respondes?", "El diagrama muestra conexiones; las ubicaciones y distancias se leen en el plano de planta", "Tiene razón: el diagrama siempre trae medidas reales", "Ningún documento sirve para medir distancias", "Las distancias se estiman con el plano de planta; el diagrama dibuja conexiones, no medidas."),
        ("=", "{F} Se estiman 20 metros de cable por cada punto de red. ¿Cuántos metros de cable se necesitan en total?", "(12*2+1+1)*20", "Se multiplica el total de puntos por los metros estimados de cada uno.", " metros"),
    ],
    ctx=("abc", "Un amigo, dueño de otro negocio, te pide por mensaje el diagrama de la red de tu cliente «para copiar la idea». ¿Qué corresponde?", "Responder que debes pedir autorización a la jefa de proyecto y no compartir datos del cliente", "Enviarlo, porque es solo un dibujo", "Enviarlo borrando solo tu nombre", "El diagrama pertenece al cliente y al proyecto: se comparte solo con autorización."),
    sc=[
        ("En Conectividad y Redes: ¿qué es un punto de red?", "La toma donde se conecta un equipo a la red", "Cada puesto se conecta a la red por medio de uno o más puntos."),
        ("¿Qué documento usas para saber dónde va cada punto?", "El plano de planta", "Ese plano ubica físicamente los puntos y equipos del proyecto."),
        ("¿Qué haces antes de compartir un diagrama de red?", "Pido autorización a la jefa de proyecto", "El diagrama es información confidencial del cliente y no se difunde libremente."),
    ],
    op=("Una veterinaria de ejemplo tiene 4 puestos de atención con 2 puntos de red cada uno, 1 impresora de etiquetas con 1 punto y 1 punto de acceso Wi-Fi con 1 punto. Calcula cuántos puntos de red hay, indica qué documento usarías para saber en qué muro va cada uno y escribe una regla de confidencialidad para tu trabajo.",
        "Puntos: 4 × 2 = 8; más 1 de impresora y 1 de acceso = 10 puntos. Para ubicarlos usaría el plano de planta. Regla: no comparto diagramas ni nombres de equipos del cliente sin autorización de la jefa de proyecto.",
        ["calcula bien los puntos de red", "elige el documento correcto", "escribe una regla de confidencialidad clara"],
        ["hoja con el cálculo, el documento elegido y la regla"],
        ["olvidar la impresora o el punto de acceso", "usar el diagrama para ubicar muros", "no mencionar la autorización"],
        "Pregunta: «¿cómo sabes que contaste todos los puntos?». Si solo repite el número, pídele que muestre la suma por tipo de equipo."),
    reinforce="Dibuja el plano simple de una sala con 3 puestos de computador y marca con una cruz cada punto de red (2 por puesto).",
    extend="Explica con un ejemplo inventado por qué un plano de planta y un diagrama de la red se complementan.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (modelos de capas, de ejemplo). Modelo OSI: 7 aplicación, 6 presentación, 5 sesión, 4 transporte, 3 red, 2 enlace de datos, 1 física. "
     "Modelo TCP/IP de 4 capas: aplicación, transporte, internet, acceso a la red. Correspondencia: la aplicación de TCP/IP equivale a las capas 7, 6 y 5 de OSI; transporte a la 4; internet a la 3; acceso a la red a la 2 y la 1. "
     "Unidades de datos: segmento (transporte), paquete (red), trama (enlace) y bits (física). El switch trabaja sobre todo en la capa 2 y el router en la capa 3.")
build(
    O1, 2, F,
    use="Aprenderé los modelos OSI y TCP/IP, qué hace cada capa y quiénes usan estos modelos al leer un proyecto de red.",
    prior=["Sé qué es una red LAN.", "Sé que un diagrama muestra conexiones.", "Sé que cada equipo tiene una dirección."],
    explain=[
        "Un modelo de capas divide la comunicación entre equipos en funciones separadas. Así, cuando algo falla, se puede ubicar en qué capa está el problema. El modelo OSI tiene 7 capas: física, enlace de datos, red, transporte, sesión, presentación y aplicación. El modelo TCP/IP, que es el que usa internet, se explica aquí con 4 capas: acceso a la red, internet, transporte y aplicación.",
        "Cada capa se apoya en la de abajo. La física mueve bits por cable o por aire. La de enlace organiza los datos en tramas entre equipos vecinos, y el switch trabaja sobre todo ahí. La de red usa direcciones IP y envía paquetes entre redes; ahí trabaja el router. La de transporte entrega segmentos entre programas, y la de aplicación es la que ve el usuario, por ejemplo al navegar o enviar correo.",
        "Los modelos son una guía para leer diagramas y proyectos, para conversar con otras personas del equipo con las mismas palabras y para ordenar un diagnóstico. No son una norma que diga cómo instalar: eso lo fijan las especificaciones técnicas y la norma vigente.",
    ],
    vocab=[("modelo OSI", "modelo de 7 capas que describe la comunicación entre equipos"), ("modelo TCP/IP", "modelo de 4 capas usado por internet"), ("capa", "función de la comunicación que se apoya en la capa de abajo"), ("trama", "unidad de datos de la capa de enlace"), ("paquete", "unidad de datos de la capa de red"), ("segmento", "unidad de datos de la capa de transporte"), ("switch", "equipo que conecta equipos de una LAN usando la capa 2")],
    worked=[
        ("Ubicar una falla", "Un cable de red está cortado y no pasa ninguna señal. ¿En qué capa del modelo TCP/IP se ubica el problema?", ["El cable mueve bits, es decir, es la capa física (OSI 1).", "En TCP/IP, la capa física forma parte del acceso a la red."], "Acceso a la red"),
        ("Equivalencia de capas", "¿A qué capa de TCP/IP equivale la capa 3 (red) de OSI?", ["La capa 3 trabaja con direcciones IP y paquetes.", "En TCP/IP esa función está en la capa internet."], "Internet"),
    ],
    mistakes=[("Decir que el switch y el router hacen lo mismo porque «los dos tienen cables conectados».", "El switch trabaja con tramas dentro de una LAN (capa 2) y el router con paquetes entre redes (capa 3).", "Pregunta si el equipo mueve tramas dentro de la LAN o paquetes con dirección IP entre redes."),
              ("Buscar una «capa de presentación» en TCP/IP de 4 capas.", "Ese nombre es de OSI; en TCP/IP esa función está dentro de la capa de aplicación.", "Usa la tabla de correspondencia antes de nombrar una capa.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿cuántas capas tiene el modelo OSI?", "7", "4", "6", "El modelo OSI tiene siete capas, desde la física hasta la aplicación."),
        ("abc", "En Conectividad y Redes: ¿cuántas capas tiene el modelo TCP/IP que usamos en este cuaderno?", "4", "7", "3", "Este cuaderno explica TCP/IP con cuatro capas: acceso a la red, internet, transporte y aplicación."),
        ("abc", "¿Para qué sirve un modelo de capas en el trabajo de redes?", "Para dividir la comunicación en funciones y ubicar en qué parte falla algo", "Para fijar el precio de los equipos", "Para escribir las claves de los usuarios", "Separar funciones permite ubicar el problema en una capa y hablar con palabras comunes."),
        ("abc", "{F} ¿Qué capa OSI es el transporte?", "La capa 4", "La capa 3", "La capa 2", "Según la ficha, el transporte es la capa 4; la 3 es red y la 2 es enlace de datos."),
        ("abc", "{F} ¿A qué capas de OSI equivale la capa aplicación de TCP/IP?", "A las capas 7, 6 y 5", "A las capas 4 y 3", "A las capas 2 y 1", "La aplicación de TCP/IP reúne aplicación, presentación y sesión de OSI."),
        ("abc", "{F} ¿Qué unidad de datos se llama paquete?", "La de la capa de red", "La de la capa de enlace", "La de la capa de transporte", "El paquete es la unidad de la capa de red; la trama es del enlace y el segmento del transporte."),
        ("=", "{F} Un técnico de ejemplo revisó las capas OSI 1, 2 y 3 de un problema. ¿Cuántas capas OSI le faltan por revisar?", "7-3", "El modelo tiene siete capas y ya revisó tres.", " capas"),
        ("abc", "{F} Un cable suelto impide que los bits viajen. ¿En qué capa de TCP/IP se ubica la falla?", "En el acceso a la red", "En la aplicación", "En internet", "Los bits por cable pertenecen a la física, que dentro de TCP/IP forma parte del acceso a la red."),
        ("abc", "{F} Un equipo tiene mal escrita su dirección IP. ¿En qué capa OSI se ubica el problema?", "En la capa 3, red", "En la capa 2, enlace de datos", "En la capa 4, transporte", "La dirección IP pertenece a la capa de red, que es la 3 de OSI."),
        ("abc", "{F} Un compañero afirma que el switch y el router hacen lo mismo. ¿Qué corrección corresponde?", "El switch trabaja sobre todo en la capa 2 con tramas y el router en la capa 3 con paquetes", "Tiene razón: ambos trabajan en la capa 3", "Ambos trabajan solo en la capa 1", "La ficha ubica el switch en la capa 2 y el router en la 3."),
        ("abc", "Un informe de ejemplo dice: «la falla está en la capa de presentación de TCP/IP». ¿Qué error tiene?", "TCP/IP de 4 capas no tiene capa de presentación; ese nombre es de OSI", "Ninguno, porque TCP/IP tiene 7 capas", "Debió decir capa de red de OSI, que es la 2", "La capa de presentación pertenece al modelo OSI y TCP/IP la incluye en la aplicación."),
        ("abc", "{F} Se comprobaron el cable, la dirección IP y la entrega entre programas, pero el navegador muestra un error de la página web. ¿Qué capa de TCP/IP falta revisar?", "La aplicación", "El acceso a la red", "Internet", "Ya se revisaron las capas de abajo; lo que ve el usuario en el navegador es la aplicación."),
        ("ab", "{F} ¿Cuál es el orden de las capas TCP/IP de arriba hacia abajo?", "Aplicación, transporte, internet, acceso a la red", "Acceso a la red, internet, transporte, aplicación", "La capa más cercana al usuario es la aplicación y la más cercana al cable es el acceso a la red."),
    ],
    ctx=("abc", "En una oficina de ejemplo ninguna persona puede abrir páginas ni imprimir, y las luces de los puertos del switch están apagadas. La jefa te pide por dónde empezar. ¿Qué respondes?", "Empezar por lo físico: revisar la alimentación del switch y los cables, y luego subir de capa", "Empezar por reinstalar el navegador en todos los computadores", "Empezar por cambiar todas las direcciones IP", "Si las luces del switch están apagadas, la falla está abajo; se ordena el diagnóstico desde la capa física."),
    sc=[
        ("En Conectividad y Redes: ¿en qué capa trabaja un switch?", "Sobre todo en la capa 2, enlace de datos", "El switch conecta equipos de una misma LAN usando tramas."),
        ("¿Qué capa de OSI usa direcciones IP?", "La capa 3, red", "La dirección IP identifica equipos entre redes y pertenece a la capa de red."),
        ("¿Para qué sirve ubicar la capa de una falla?", "Para ordenar el diagnóstico y avisar al equipo con palabras comunes", "Cada capa tiene funciones distintas y eso reduce el tiempo de búsqueda."),
    ],
    op=("Una escuela de ejemplo registra seis síntomas: (a) un cable de red está cortado; (b) dos computadores tienen la misma dirección IP; (c) una página web de la intranet muestra un error de contenido; (d) un servicio no recibe datos porque su entrada de transporte está cerrada; (e) la tarjeta de red de un equipo está desactivada; (f) el router envía los paquetes hacia una red equivocada. Ubica cada síntoma en una capa de TCP/IP.",
        "(a) acceso a la red; (b) internet; (c) aplicación; (d) transporte; (e) acceso a la red; (f) internet. Justificación breve: la capa se elige según qué dato o función falla (bits, direcciones IP, paquetes entre redes, entrega a programas o lo que ve el usuario).",
        ["ubica bien al menos cinco síntomas", "justifica con la función de la capa", "usa los nombres de capas de TCP/IP"],
        ["tabla de seis filas con síntoma, capa y razón"],
        ["usar nombres de capas de OSI en TCP/IP", "confundir direcciones IP con cables", "no justificar"],
        "Pregunta: «¿qué función falla en (b)?». Si responde 'el cable', repasa que una dirección IP repetida es de la capa de internet."),
    reinforce="Dibuja las cuatro capas de TCP/IP una sobre otra y escribe al lado un ejemplo de falla para cada una.",
    extend="Explica por qué se suele empezar el diagnóstico desde la capa más baja y subir.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (diagrama de ejemplo, inventado, con direcciones privadas). PC-1 (192.168.10.11) y PC-2 (192.168.10.12) están en los puertos 1 y 2 del Switch-A; la impresora IMP-1 (192.168.10.20) está en el puerto 3; "
     "el puerto 24 del Switch-A va al Router-R1 (192.168.10.1), que sale a internet. El Switch-A tiene 24 puertos. Máscara de la red: 255.255.255.0 (una red así admite 254 equipos).")
build(
    O1, 3, F,
    use="Aprenderé a leer un diagrama de una red LAN: equipos, puertos, direcciones y camino de un mensaje, y a detectar errores simples.",
    prior=["Conozco las capas de los modelos OSI y TCP/IP.", "Sé qué es una red LAN.", "Sé restar y comparar números."],
    explain=[
        "Un diagrama de una red LAN se lee de manera ordenada: primero los equipos (computadores, impresoras, switch, router), luego los enlaces entre ellos y los puertos usados, y por último las direcciones. Cada equipo tiene una dirección IP, que es un número que lo identifica dentro de la red. Los equipos de una misma red comparten las primeras partes de la dirección.",
        "El switch conecta equipos de la misma LAN, y cada cable llega a un puerto. El router conecta la LAN con otras redes, como internet; su dirección dentro de la LAN es la puerta de enlace. La máscara de red indica qué parte de la dirección identifica la red. Con la máscara 255.255.255.0, dos equipos están en la misma red si sus tres primeros números son iguales.",
        "Al leer, se buscan inconsistencias: una dirección repetida entre dos equipos produce un conflicto, un equipo dibujado en un puerto que no existe indica un error del diagrama, y un equipo con tres primeros números distintos está en otra red. Los datos del diagrama son de ejemplo; en un proyecto real se contrastan con el plano, la memoria técnica y la norma vigente.",
    ],
    vocab=[("dirección IP", "número que identifica a un equipo dentro de una red"), ("puerto", "conexión física del switch donde se enchufa un cable"), ("router", "equipo que conecta la LAN con otras redes"), ("puerta de enlace", "dirección del router dentro de la LAN"), ("máscara de red", "número que indica qué parte de la dirección identifica la red"), ("conflicto de direcciones", "dos equipos con la misma dirección IP")],
    worked=[
        ("Misma red o no", "Con máscara 255.255.255.0, ¿están en la misma red 192.168.50.7 y 192.168.50.90 (direcciones de ejemplo)?", ["Los tres primeros números son 192.168.50 en ambas.", "Con esa máscara, eso significa que comparten la red."], "Sí, están en la misma red"),
        ("Puertos libres", "Un switch de ejemplo tiene 16 puertos y 5 están ocupados. ¿Cuántos puertos libres tiene?", ["Se restan los puertos ocupados de los totales.", "16 − 5 = 11."], "11 puertos libres"),
    ],
    mistakes=[("Asignar la misma dirección IP a dos equipos «porque son del mismo tipo».", "Cada equipo necesita una dirección propia dentro de su red; si se repite, se produce un conflicto.", "Compara las direcciones del diagrama y marca cualquier repetición."),
              ("Cambiar el cable de puerto en el equipo real para que calce con una anotación.", "Lo que debe corregirse primero es el documento y la causa de la diferencia, con aviso a la jefatura.", "Anota la diferencia y consulta antes de tocar nada.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una dirección IP?", "Un número que identifica a un equipo dentro de una red", "El nombre comercial del cable", "El permiso para entrar a la sala técnica", "La dirección IP identifica a cada equipo para que los datos lleguen al destino correcto."),
        ("abc", "En Conectividad y Redes: ¿qué hace un router?", "Conecta redes distintas, por ejemplo la LAN con internet", "Reparte la energía eléctrica a los computadores", "Guarda las copias de respaldo", "El router une redes y por eso la LAN sale a internet a través de él."),
        ("abc", "¿Qué es un puerto de un switch?", "Cada conexión física donde se enchufa un cable de red", "Una dirección de internet", "Un tipo de contraseña", "Los puertos son las entradas físicas del switch a las que llegan los cables."),
        ("=", "{F} ¿Cuántos puertos libres tiene el Switch-A? Cuenta los puertos ocupados por PC-1, PC-2, IMP-1 y el router.", "24-4", "A los 24 puertos se les restan los 4 ocupados.", " puertos"),
        ("abc", "{F} ¿Qué equipo tiene la dirección 192.168.10.20?", "La impresora IMP-1", "El PC-2", "El Router-R1", "La ficha asigna .20 a la impresora; PC-2 es .12 y el router es .1."),
        ("abc", "{F} ¿Cuál es la salida de la LAN hacia internet?", "El Router-R1, con la dirección 192.168.10.1", "El Switch-A, en el puerto 1", "El PC-1, con la dirección 192.168.10.11", "El router une la LAN con internet; el switch solo conecta equipos de la LAN."),
        ("abc", "{F} Se configura un PC-3 con la dirección 192.168.10.12. ¿Qué problema produce?", "Una dirección repetida con PC-2, que causa conflicto", "Ninguno, porque son equipos distintos", "El switch se queda sin puertos", "PC-2 ya usa esa dirección: dos equipos con la misma IP generan conflicto."),
        ("=", "{F} Se conectan 6 computadores y 1 punto de acceso Wi-Fi nuevos al Switch-A, uno por puerto. ¿Cuántos puertos quedarán libres?", "24-4-6-1", "A los puertos libres se les restan los 7 equipos nuevos.", " puertos"),
        ("abc", "{F} ¿Cuál de estas direcciones pertenece a la misma red que PC-1?", "192.168.10.45", "192.168.20.45", "10.0.0.45", "Con la máscara 255.255.255.0 deben coincidir los tres primeros números: 192.168.10."),
        ("abc", "{F} PC-1 se comunica con PC-2, pero ninguno llega a internet. ¿Qué elemento conviene revisar primero?", "El Router-R1 y sus enlaces al switch y a internet", "La impresora IMP-1", "El puerto 2 del Switch-A", "Si PC-1 y PC-2 se ven entre sí, el switch funciona; la salida a internet depende del router."),
        ("abc", "{F} Una técnica anota que la impresora está en el puerto 4, pero la ficha dice puerto 3. ¿Qué corresponde?", "Marcar la diferencia y consultar antes de corregir cualquier cosa", "Corregir el diagrama sin avisar", "Cambiar el cable de puerto para que coincida con su anotación", "Una diferencia entre el documento y la realidad se registra y se consulta."),
        ("=", "{F} Con la máscara indicada, la red admite 254 equipos. Ya se usan las 4 direcciones .11, .12, .20 y .1. ¿Cuántas direcciones quedan libres?", "254-4", "A las direcciones que admite la red se les restan las que ya están en uso.", " direcciones"),
        ("ab", "{F} ¿Cuál es el camino correcto de un mensaje desde PC-1 hacia internet?", "PC-1, Switch-A, Router-R1, internet", "PC-1, Router-R1, Switch-A, internet", "En el diagrama, PC-1 se conecta al switch y el switch al router, que sale a internet."),
    ],
    ctx=("abc", "La impresora IMP-1 dejó de imprimir, pero los demás equipos funcionan. Según el diagrama, ¿qué compruebas primero?", "El cable de la impresora y el puerto 3 del Switch-A", "La configuración del Router-R1 completo", "La dirección del PC-2", "Como los demás equipos funcionan, el problema está cerca de la impresora y de su puerto."),
    sc=[
        ("En Conectividad y Redes: ¿qué provoca una dirección IP repetida?", "Un conflicto de direcciones entre dos equipos", "Los datos no saben a qué equipo llegar y ambos pueden quedar sin red."),
        ("¿Cómo sabes que dos equipos están en la misma red con máscara 255.255.255.0?", "Si sus tres primeros números son iguales", "La máscara indica que esos tres números identifican a la red."),
        ("¿Qué haces si el diagrama no coincide con lo que ves en la sala?", "Lo anoto y consulto antes de corregir", "No se debe cambiar nada sin autorización y sin dejar constancia."),
    ],
    op=("Un taller de ejemplo tiene este diagrama: Switch-T de 8 puertos; PC-A (192.168.5.10) en el puerto 1; PC-B (192.168.5.11) en el puerto 2; PC-C (192.168.5.11) en el puerto 3; impresora (192.168.5.30) en el puerto 4; Router-T (192.168.5.1) en el puerto 8. Máscara 255.255.255.0. Escribe cuántos puertos libres hay, detecta la inconsistencia, el camino de un mensaje de PC-A a internet y una acción para corregir el diagrama.",
        "Puertos ocupados: 5 de 8; libres: 3. Inconsistencia: PC-B y PC-C tienen la misma dirección 192.168.5.11 (conflicto). Camino: PC-A, Switch-T, Router-T, internet. Acción: consultar a la jefatura y asignar a uno de los dos una dirección libre de la red, dejando constancia en el diagrama.",
        ["cuenta bien los puertos libres", "detecta la dirección repetida", "describe el camino y propone una corrección con constancia"],
        ["hoja con el conteo, la inconsistencia, el camino y la acción"],
        ["no ver la dirección repetida", "invertir el camino", "corregir sin consultar ni dejar constancia"],
        "Pregunta: «¿qué dos equipos entran en conflicto y por qué?». Si no puede decirlo, pídele que subraye las direcciones del diagrama."),
    reinforce="Dibuja una red con un switch, tres computadores y un router; asígnales direcciones de una misma red y rotula cada puerto.",
    extend="Explica por qué dos equipos con tres primeros números distintos necesitan un router para comunicarse.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (propuestas de ejemplo para una oficina con 20 puntos de red). Propuesta A: 1 switch de 24 puertos, $180.000 (de ejemplo). Propuesta B: 1 switch de 16 puertos, $110.000 (de ejemplo). "
     "Propuesta C: 2 switches de 24 puertos cada uno, $360.000 (de ejemplo). Criterios del proyecto: cubrir los 20 puntos y dejar una reserva de al menos 5 puertos para crecer.")
build(
    O1, 4, F,
    use="Aprenderé a comparar propuestas de un proyecto de red con criterios técnicos y datos, y a escribir una recomendación con sus límites.",
    prior=["Sé leer un diagrama de red.", "Sé calcular puertos libres.", "Sé comparar cifras y precios."],
    explain=[
        "Un criterio técnico es una regla verificable que se usa para decidir entre opciones. En un proyecto de red puede ser que el switch cubra todos los puntos y deje una reserva para crecer. La reserva es capacidad extra prevista para no rehacer el proyecto cuando se agreguen equipos. Una especificación técnica es la descripción de lo que el equipo o el proyecto debe cumplir.",
        "Para decidir se hacen tres cosas: se calculan los datos que pide cada criterio (por ejemplo, puertos necesarios = puntos + reserva), se compara cada propuesta con ese valor y se descartan las que no cumplen. Entre las que cumplen, se considera el costo. El precio más bajo no decide por sí solo: una propuesta barata que no cumple el criterio no sirve.",
        "Una recomendación técnica se escribe con los datos que la respaldan y con sus límites: aquí los precios y la reserva son de ejemplo, y en un proyecto real también intervienen la norma vigente, la revisión de la jefa de proyecto y el presupuesto del cliente. Una recomendación sin datos es solo una opinión.",
    ],
    vocab=[("criterio técnico", "regla verificable para decidir entre opciones"), ("reserva", "capacidad extra prevista para crecer"), ("especificación técnica", "descripción de lo que debe cumplir un equipo o proyecto"), ("propuesta", "opción de solución con equipos y costo"), ("recomendación", "decisión escrita con los datos que la respaldan"), ("límite", "aquello que la recomendación no puede asegurar")],
    worked=[
        ("Puertos necesarios", "Una sala de ejemplo tiene 12 puntos y se exige una reserva de 4 puertos. ¿Cuántos puertos necesita el switch?", ["Puertos necesarios = puntos + reserva.", "12 + 4 = 16."], "16 puertos"),
        ("Descartar por el criterio", "Un switch de 16 puertos cuesta menos que uno de 24, pero el proyecto necesita 20. ¿Se puede elegir el de 16?", ["16 es menor que 20: no cubre los puntos.", "El criterio no se cumple, aunque el precio sea menor."], "No: no cumple el criterio"),
    ],
    mistakes=[("Elegir siempre la opción más barata.", "Una opción barata que no cumple el criterio obliga a rehacer o ampliar el trabajo.", "Primero descarta las que no cumplen; luego compara el costo de las que sí."),
              ("Recomendar sin mostrar los datos.", "Sin datos nadie puede verificar la recomendación.", "Escribe los cálculos, el criterio y los límites junto a la decisión.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es la reserva en un proyecto de red?", "Capacidad extra prevista para crecer sin rehacer el proyecto", "Un equipo guardado que nunca se usa", "El dinero que se devuelve al cliente", "La reserva deja espacio para agregar equipos sin cambiar el diseño."),
        ("abc", "¿Qué es un criterio técnico?", "Una regla verificable que se usa para decidir entre opciones", "Una opinión personal sin datos", "El precio más bajo de todas las ofertas", "Un criterio permite decidir con datos y que otra persona repita la comprobación."),
        ("abc", "¿Qué es una especificación técnica?", "Una descripción de lo que el equipo o el proyecto debe cumplir", "Una lista de contraseñas del cliente", "Un permiso para entrar al edificio", "La especificación fija las condiciones que debe cumplir lo que se instala o se compra."),
        ("=", "{F} ¿Cuántos puertos necesita el switch según los criterios (20 puntos más la reserva mínima)?", "20+5", "Se suman los puntos y la reserva mínima exigida.", " puertos"),
        ("abc", "{F} ¿Qué propuesta no alcanza ni siquiera a cubrir los 20 puntos?", "La propuesta B", "La propuesta A", "La propuesta C", "B tiene 16 puertos, que son menos que los 20 puntos."),
        ("=", "{F} ¿Cuántos puertos tiene en total la propuesta C?", "2*24", "Son dos switches de 24 puertos cada uno.", " puertos"),
        ("abc", "{F} ¿Qué propuesta cumple todos los criterios?", "La propuesta C", "La propuesta A", "La propuesta B", "Se necesitan 25 puertos; A tiene 24 y B tiene 16; C tiene 48."),
        ("=", "{F} ¿Cuántos pesos más cuesta la propuesta C que la propuesta A?", "360000-180000", "Se resta el precio de A al precio de C.", " pesos"),
        ("=", "{F} Si se usara la propuesta C y se conectaran los 20 puntos, ¿cuántos puertos quedarían libres?", "48-20", "A los 48 puertos se les restan los 20 usados.", " puertos"),
        ("abc", "{F} El cliente dice: «tomen la B, es la más barata». ¿Qué respuesta técnica corresponde?", "La B tiene 16 puertos y se necesitan 25, por lo que no cumple el criterio aunque cueste menos", "Tiene razón: el precio decide siempre", "Mejor la C, porque tiene más puertos que la A, sin mirar criterios", "El criterio de puertos se verifica antes que el precio; B no cubre ni los puntos."),
        ("abc", "{F} Si el cliente aceptara una reserva de solo 4 puertos, ¿qué cambiaría?", "La propuesta A también cumpliría, porque 24 puertos alcanzan para 20 puntos más 4", "Ninguna propuesta cambiaría", "La propuesta B pasaría a cumplir", "Con 24 necesarios, A queda justa; B sigue con 16, que no alcanza."),
        ("abc", "{F} Un técnico escribe solo «recomiendo la C». ¿Qué le falta para que sea una recomendación técnica?", "Los datos que la respaldan: puertos necesarios, puertos de cada propuesta y el criterio usado", "Un adjetivo más positivo", "El nombre de la marca del switch", "Una recomendación técnica muestra cálculos y criterio para que otra persona pueda verificar."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los precios y la reserva son de ejemplo y un proyecto real requiere norma vigente y revisión de la jefa de proyecto", "Ninguno, porque los números son exactos", "Que el switch elegido es el mejor del mundo", "Los datos de la ficha son de ejemplo; en la realidad se contrastan con la norma y con la jefatura."),
    ],
    ctx=("abc", "La jefa de proyecto te pide una recomendación hoy para una bodega de ejemplo que necesita 10 puntos de red y una reserva de 4. Hay un switch de 16 puertos y otro de 8 puertos. ¿Qué recomiendas?", "El de 16 puertos, porque se necesitan 14 y el de 8 no alcanza", "El de 8 puertos, porque es más barato", "Ninguno: no se puede decidir sin saber la marca", "Se necesitan 10 más 4 puertos, es decir 14; solo el de 16 cumple."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calculan los puertos necesarios?", "Puntos de red más reserva", "La reserva se suma a los puntos para dejar espacio de crecimiento."),
        ("¿Por qué no basta con elegir lo más barato?", "Porque debe cumplir primero los criterios técnicos", "Una opción que no cumple obliga a rehacer o ampliar el trabajo."),
        ("¿Qué debe llevar una recomendación técnica?", "Datos, criterio usado y límites", "Con eso otra persona puede comprobarla y entender qué no asegura."),
    ],
    op=("Un consultorio de ejemplo necesita 30 puntos de red con una reserva mínima de 6 puertos. Opción 1: 1 switch de 48 puertos, $300.000 (de ejemplo). Opción 2: 1 switch de 24 puertos, $170.000 (de ejemplo). Opción 3: 2 switches de 24 puertos, $340.000 (de ejemplo). Calcula los puertos necesarios, descarta lo que no cumple, recomienda una opción con sus datos y escribe un límite.",
        "Puertos necesarios: 30 + 6 = 36. La opción 2 tiene 24 y no cumple. La opción 1 tiene 48 y cumple; la opción 3 tiene 48 y también cumple pero cuesta más. Recomiendo la opción 1 ($300.000 frente a $340.000). Límite: los precios son de ejemplo y el proyecto real requiere la revisión de la jefa de proyecto y la norma vigente.",
        ["calcula los puertos necesarios", "descarta con el criterio y compara el costo", "escribe una recomendación con datos y un límite"],
        ["hoja con cálculos, tabla comparativa y recomendación"],
        ["elegir por precio sin verificar", "olvidar la reserva", "no declarar límites"],
        "Pregunta: «¿por qué descartaste la opción 2?». Si no cita los números, pídele que escriba 24 frente a 36."),
    reinforce="Calcula los puertos que necesitaría un laboratorio de 18 puntos con una reserva de 6 puertos.",
    extend="Explica por qué conviene dejar una reserva en un switch aunque hoy no se use.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (laboratorio de ejemplo, inventado). «Liceo Los Alerces»: laboratorio con 10 computadores que se incorporarán a la red LAN. Requisitos mínimos del sistema operativo de ejemplo «SO-Demo»: 4 GB de memoria RAM y 64 GB de espacio libre en disco. "
     "Los computadores guardan trabajos de estudiantes, con nombres (datos personales). Roles: la encargada de informática del liceo autoriza; el técnico configura. Estándar de seguridad del liceo (de ejemplo): cuenta de administrador solo para el técnico, contraseñas con frase larga, actualizaciones al día y respaldo antes de reinstalar.")
build(
    O2, 1, F,
    use="Aprenderé qué es un sistema operativo, por qué se instala y configura con autorización, y qué riesgos y estándares hay que respetar.",
    prior=["Sé qué es una red LAN.", "Sé qué es un computador personal.", "Sé comparar números en GB."],
    explain=[
        "Un sistema operativo es el programa base que administra el computador y permite usar otros programas. Instalarlo es dejarlo funcionando en el equipo; configurarlo es ajustar cuentas, nombre del equipo, red y seguridad para que el equipo se pueda incorporar a la red LAN y cumpla los estándares de calidad y seguridad de la institución.",
        "Esta tarea se hace con autorización de quien es responsable de los equipos y respetando la licencia, que es el permiso legal de uso de un programa. Antes de reinstalar se hace una copia de respaldo, porque instalar puede borrar los archivos. Los equipos suelen guardar datos personales, que se protegen según la ley de protección de datos personales vigente y las reglas del establecimiento.",
        "Los riesgos más comunes son perder datos, usar programas sin licencia, dejar cuentas de administrador con claves débiles y trabajar en equipos ajenos sin permiso. También importa la ergonomía: se trabaja con pausas y buena postura. Esta clase no te enseña a instalar en equipos reales; enseña a decidir con orden y a registrar lo que se hace.",
    ],
    vocab=[("sistema operativo", "programa base que administra el computador"), ("licencia", "permiso legal de uso de un programa"), ("respaldo", "copia de archivos para poder recuperarlos"), ("cuenta de administrador", "cuenta que puede cambiar la configuración del equipo"), ("datos personales", "información que identifica a una persona"), ("estándar de seguridad", "reglas mínimas que debe cumplir un equipo")],
    worked=[
        ("Comprobar un requisito", "Un equipo de ejemplo tiene 8 GB de RAM y el sistema pide 4 GB como mínimo. ¿Cumple el requisito de RAM?", ["Se compara 8 con el mínimo de 4.", "8 es mayor que 4."], "Sí, cumple"),
        ("Qué hacer antes de reinstalar", "Un equipo de ejemplo tiene tareas de estudiantes y se quiere reinstalar el sistema. ¿Qué se hace primero?", ["La reinstalación puede borrar archivos.", "Primero se pide autorización y se hace una copia de respaldo."], "Autorización y respaldo"),
    ],
    mistakes=[("Reinstalar el sistema para «dejarlo limpio» sin respaldar los trabajos.", "Los archivos de las personas pueden perderse y no siempre se recuperan.", "Haz y comprueba el respaldo antes de reinstalar y registra la fecha."),
              ("Usar el programa pagado sin licencia «solo esta vez».", "Usar software sin licencia incumple el permiso de uso y expone al liceo a problemas legales.", "Explica que se necesita licencia o propone una alternativa autorizada.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un sistema operativo?", "El programa base que administra el computador y permite usar otros programas", "Un cable que une el computador a la red", "Una copia de seguridad de los archivos", "El sistema operativo coordina el equipo y es la base sobre la que corren los demás programas."),
        ("abc", "En Conectividad y Redes: ¿qué es una licencia de software?", "El permiso legal para usar un programa", "La clave del punto de acceso", "El número de serie del cable", "La licencia fija bajo qué condiciones se puede usar un programa."),
        ("abc", "¿Qué se hace antes de reinstalar el sistema de un equipo que guarda trabajos de estudiantes?", "Pedir autorización y hacer una copia de respaldo", "Formatear de inmediato para ganar tiempo", "Borrar los archivos para liberar espacio", "Reinstalar puede borrar archivos, por eso se respalda y se pide autorización."),
        ("abc", "{F} ¿Quién autoriza el trabajo sobre los equipos del laboratorio?", "La encargada de informática del liceo", "Cualquier estudiante del curso", "El primer técnico que llegue", "La ficha asigna la autorización a la encargada de informática."),
        ("abc", "{F} ¿Qué dato personal puede haber en los equipos del laboratorio?", "Trabajos con los nombres de las y los estudiantes", "Ninguno, porque los computadores son del liceo", "Solo la clave del administrador", "Los trabajos con nombres identifican a personas y deben protegerse."),
        ("abc", "{F} ¿Qué contraseña sigue mejor el estándar del liceo?", "Una frase larga de varias palabras sin relación, fácil de recordar para ti", "El número 1234", "El nombre del liceo", "Una frase larga resiste mejor los intentos de adivinar que un número corto o un nombre conocido."),
        ("=", "{F} Un equipo de ejemplo tiene 250 GB de disco y 150 GB ocupados. ¿Cuántos GB de espacio libre le sobran después de reservar los 64 GB mínimos del SO-Demo?", "250-150-64", "Al disco se le restan el espacio ocupado y el mínimo exigido.", " GB"),
        ("abc", "{F} Un equipo tiene 2 GB de RAM. ¿Cumple el requisito del sistema?", "No: se necesitan al menos 4 GB", "Sí, porque el disco es grande", "Depende del color del gabinete", "El requisito de RAM no se reemplaza con disco: 2 GB es menos que 4 GB."),
        ("=", "{F} Se estiman 45 minutos de configuración por equipo en los 10 computadores. ¿Cuántos minutos son en total?", "10*45", "Se multiplican los equipos por los minutos de cada uno.", " minutos"),
        ("abc", "{F} Una docente pide instalar un programa pagado sin licencia «solo esta vez». ¿Qué corresponde?", "Explicar que requiere licencia y derivar la compra o buscar una alternativa autorizada", "Instalarlo igual y no decir nada", "Instalarlo y anotarlo con otro nombre", "El software sin licencia incumple el permiso de uso y el técnico debe derivar la solución."),
        ("abc", "{F} El técnico deja la clave del administrador escrita en un papel pegado al computador. ¿Qué buena práctica incumple?", "Proteger las credenciales y limitar el uso de la cuenta de administrador", "Mantener las actualizaciones al día", "Hacer el respaldo antes de reinstalar", "Una clave a la vista permite que cualquiera la use; el estándar la limita al técnico."),
        ("abc", "{F} Una estudiante pide acceder a los archivos de otra porque «perdió su tarea». ¿Qué corresponde?", "Avisar a la encargada o a la docente responsable, que decide con autorización", "Darle los archivos porque son del mismo curso", "Entrar con la cuenta del técnico sin avisar", "Los trabajos de otra persona son datos personales; solo se entregan con autorización."),
        ("=", "{F} Los 10 equipos tienen 20 GB de trabajos cada uno y se respaldan en un disco externo de 500 GB. ¿Cuántos GB quedan libres en el disco externo?", "500-10*20", "Se resta del disco externo el total de los trabajos respaldados.", " GB"),
    ],
    ctx=("abc", "La encargada te pide dejar un equipo listo para mañana, pero ese equipo tiene trabajos de estudiantes que no están respaldados. ¿Qué haces?", "Hago y compruebo un respaldo con su autorización antes de cambiar nada y lo registro", "Reinstalo igual: los trabajos son antiguos", "Borro lo que no reconozco para ganar espacio", "El equipo guarda datos de personas: se respalda con autorización antes de intervenirlo."),
    sc=[
        ("En Conectividad y Redes: ¿qué se hace antes de reinstalar un sistema operativo?", "Pedir autorización y hacer un respaldo", "Reinstalar puede borrar archivos que no siempre se recuperan."),
        ("¿Para qué sirve una licencia?", "Para tener el permiso legal de usar el programa", "Sin licencia se incumplen las condiciones de uso del programa."),
        ("¿Quién debe usar la cuenta de administrador?", "Solo el técnico autorizado", "Esa cuenta puede cambiar todo el equipo y por eso se limita."),
    ],
    op=("Un colegio de ejemplo tiene 6 equipos para incorporar a su LAN. Requisitos del sistema de ejemplo: 4 GB de RAM y 40 GB de disco libre. Equipos: E1 (8 GB, 100 GB libres), E2 (2 GB, 200 GB libres), E3 (4 GB, 30 GB libres), E4 (4 GB, 40 GB libres), E5 (16 GB, 300 GB libres), E6 (4 GB, 80 GB libres). Indica cuáles cumplen, qué harías antes de cualquier cambio y una regla de contraseñas para el técnico.",
        "Cumplen E1, E4, E5 y E6. E2 falla por RAM y E3 por disco. Antes de cambiar nada: pedir autorización, respaldar los archivos y registrar el estado. Regla: contraseña con frase larga, distinta para cada cuenta, y cuenta de administrador solo para el técnico.",
        ["clasifica bien los seis equipos", "incluye autorización y respaldo", "propone una regla de contraseñas razonable"],
        ["tabla de seis filas con equipo, RAM, disco y conclusión, más la regla"],
        ["no ver que E4 cumple justo el mínimo", "olvidar el respaldo", "proponer una contraseña corta"],
        "Pregunta: «¿por qué E4 sí cumple?». Si dice que no, recuérdale que el requisito es un mínimo y que 40 GB lo cumple."),
    reinforce="Anota los requisitos de RAM y disco que pedirías para un programa de ejemplo y compara con un computador inventado.",
    extend="Explica por qué la cuenta de trabajo de las y los estudiantes no debería ser administradora.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (ficha de configuración de ejemplo del equipo LAB-03; el estándar del liceo pide cuenta de trabajo estándar, actualizaciones automáticas activadas y antivirus activo). "
     "Datos: usuario de trabajo «alumnos», cuenta estándar; cuenta de administrador solo del técnico; disco de 250 GB con 2 particiones, sistema de 100 GB y datos de 150 GB; actualizaciones automáticas activadas; antivirus activo; "
     "dirección de red asignada automáticamente por DHCP (servicio que entrega direcciones a los equipos).")
build(
    O2, 2, F,
    use="Aprenderé los conceptos básicos de la instalación y configuración de un sistema operativo (cuentas, particiones, controladores, actualizaciones) y los documentos que dejan constancia.",
    prior=["Sé qué es un sistema operativo.", "Sé qué es una red LAN.", "Sé que hay estándares de seguridad."],
    explain=[
        "Un disco se puede dividir en particiones, que son espacios separados que el sistema usa como si fueran discos distintos. Separar el sistema de los datos ayuda a ordenar y a reinstalar el sistema sin tocar los datos, aunque los datos igual se respaldan. Los controladores (drivers) son programas que permiten al sistema operativo usar un dispositivo, como la tarjeta de red o la impresora.",
        "Las cuentas se separan por función. La cuenta de administrador puede cambiar la configuración de todo el equipo y la usa solo el técnico. La cuenta estándar sirve para el trabajo diario y no puede cambiar la configuración del sistema, lo que reduce el daño de un error o de un programa malicioso. Las actualizaciones corrigen fallas y problemas de seguridad; el antivirus ayuda a detectar programas dañinos.",
        "Todo lo que se configura se registra en una ficha de configuración: nombre del equipo, cuentas, particiones, actualizaciones y dirección de red. Al terminar se firma un acta de entrega con el estado del equipo y quién lo recibe. Esos documentos permiten revisar el trabajo y repetirlo. La política de seguridad de la institución fija el estándar que se debe cumplir.",
    ],
    vocab=[("partición", "división de un disco que se usa como espacio separado"), ("controlador", "programa que permite usar un dispositivo"), ("cuenta estándar", "cuenta de trabajo diario sin permiso para cambiar el sistema"), ("actualización", "cambio que corrige fallas o problemas de seguridad"), ("ficha de configuración", "documento con los datos configurados en un equipo"), ("acta de entrega", "documento que deja constancia de lo entregado y su estado"), ("DHCP", "servicio que entrega direcciones a los equipos de una red")],
    worked=[
        ("Espacio sin asignar", "Un disco de ejemplo de 200 GB tiene una partición de sistema de 80 GB y una de datos de 100 GB. ¿Cuántos GB quedan sin asignar?", ["Se suman las particiones: 80 + 100 = 180.", "200 − 180 = 20."], "20 GB"),
        ("Elegir la cuenta", "Una estudiante necesita escribir un informe en un equipo. ¿Qué cuenta debe usar, estándar o de administrador?", ["Escribir un informe es trabajo diario.", "La cuenta de administrador se reserva para el técnico."], "La cuenta estándar"),
    ],
    mistakes=[("Dar a la cuenta de trabajo permisos de administrador para «evitar pedir permisos».", "Cualquier error o programa dañino podría cambiar la configuración de todo el equipo.", "Mantén la cuenta de trabajo como estándar y deja los cambios al técnico."),
              ("Configurar el equipo sin dejar ficha.", "Nadie sabrá qué se cambió ni cómo repetirlo o revisarlo.", "Completa la ficha de configuración y el acta antes de entregar el equipo.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una partición de disco?", "Una división del disco que se usa como espacio separado", "Un programa dañino", "Una copia de seguridad en la nube", "Una partición separa espacios dentro de un mismo disco físico."),
        ("abc", "¿Qué es un controlador (driver)?", "Un programa que permite al sistema operativo usar un dispositivo", "La persona que dirige el laboratorio", "Un cable que une dos computadores", "El controlador traduce entre el sistema operativo y el dispositivo, como una tarjeta de red."),
        ("abc", "¿Qué diferencia hay entre una cuenta estándar y una de administrador?", "La estándar sirve para el trabajo diario y la de administrador puede cambiar la configuración del equipo", "La estándar es más rápida y la de administrador es más lenta", "No hay ninguna diferencia", "Las cuentas se separan por función para limitar el daño de un error."),
        ("abc", "{F} ¿Qué cuenta usan las y los estudiantes en LAB-03?", "La cuenta estándar «alumnos»", "La cuenta de administrador", "Ninguna cuenta", "La ficha asigna a «alumnos» una cuenta estándar."),
        ("=", "{F} Si la partición de datos fuera de 100 GB en vez de 150 GB, ¿cuántos GB del disco quedarían sin asignar?", "250-100-100", "Al disco se le restan las dos particiones.", " GB"),
        ("abc", "{F} ¿Qué documento deja constancia de lo configurado en el equipo?", "La ficha de configuración", "El plano de planta", "La boleta de compra", "La ficha registra nombre, cuentas, particiones y red del equipo."),
        ("=", "{F} En la partición de sistema se usan 40 GB para el sistema y 25 GB para programas. ¿Cuántos GB quedan libres en esa partición?", "100-40-25", "A la partición se le restan el sistema y los programas.", " GB"),
        ("abc", "{F} ¿Qué ventaja tiene separar sistema y datos en dos particiones?", "Si hay que reinstalar el sistema, los datos están en otra partición, aunque igual se respaldan", "Los datos ya no necesitan respaldo", "El equipo no necesita actualizaciones", "La separación ordena y facilita la reinstalación, pero no reemplaza el respaldo."),
        ("abc", "{F} ¿Para qué sirve el acta de entrega?", "Para dejar constancia de lo entregado, su estado y quién lo recibe", "Para cambiar las claves de los usuarios", "Para instalar nuevos programas", "El acta es un documento de respaldo del trabajo realizado."),
        ("abc", "{F} Un técnico pone la cuenta «alumnos» como administradora «para no pedir permisos». ¿Qué riesgo crea?", "Un error o un programa dañino podría cambiar la configuración de todo el equipo", "Ninguno, porque es solo un nombre", "El disco se llenaría más rápido", "Los permisos amplios en la cuenta de uso diario amplían el daño posible."),
        ("abc", "{F} El técnico asigna a mano una dirección fija a LAB-03, pero la ficha dice DHCP. ¿Qué conviene?", "Anotar el cambio en la ficha y consultar, porque puede chocar con otra dirección", "No decir nada, porque el equipo funciona", "Borrar la ficha para que no haya diferencias", "Un cambio que contradice la ficha se registra y se consulta para evitar conflictos."),
        ("abc", "{F} La ficha del equipo LAB-07 de ejemplo dice: usuario de trabajo, cuenta de administrador; actualizaciones, desactivadas; antivirus, activo. ¿Cuántas desviaciones tiene respecto del estándar?", "Dos: la cuenta de trabajo y las actualizaciones", "Una", "Tres", "El estándar pide cuenta estándar, actualizaciones activadas y antivirus activo; solo el antivirus coincide."),
        ("=", "{F} El liceo tiene 10 equipos y 7 ya tienen su ficha completa. ¿Cuántas fichas faltan por completar?", "10-7", "A los equipos totales se les restan los que ya tienen ficha.", " fichas"),
    ],
    ctx=("abc", "Al entregar un equipo la encargada dice: «anótalo en tu cabeza, no hace falta ficha». ¿Qué respondes?", "Que la ficha y el acta dejan constancia y permiten revisar y repetir el trabajo", "Que no se necesita ficha si el equipo enciende", "Que la ficha es solo para equipos nuevos", "Sin ficha no hay respaldo documental de lo configurado."),
    sc=[
        ("En Conectividad y Redes: ¿para qué sirven las actualizaciones?", "Para corregir fallas y problemas de seguridad", "Un equipo sin actualizar queda expuesto a fallas conocidas."),
        ("¿Quién usa la cuenta de administrador?", "Solo el técnico autorizado", "Esa cuenta puede cambiar la configuración de todo el equipo."),
        ("¿Qué datos lleva una ficha de configuración?", "Nombre del equipo, cuentas, particiones, actualizaciones y red", "Con esos datos otra persona puede revisar o repetir el trabajo."),
    ],
    op=("Completa en papel la ficha de configuración del equipo LAB-05 de ejemplo con estos datos: disco de 500 GB con partición de sistema de 120 GB y de datos de 300 GB; cuenta de trabajo estándar «alumnos»; administrador solo del técnico; actualizaciones activadas; antivirus activo; red por DHCP. Calcula los GB sin asignar y señala si cumple el estándar del liceo.",
        "Ficha: LAB-05; cuenta de trabajo «alumnos» (estándar); administrador del técnico; particiones 120 GB y 300 GB; sin asignar 500 − 420 = 80 GB; actualizaciones activadas; antivirus activo; red por DHCP. Cumple el estándar porque las tres reglas se cumplen.",
        ["completa todos los campos de la ficha", "calcula los GB sin asignar", "concluye si cumple el estándar con razones"],
        ["ficha en papel con cada campo y la conclusión"],
        ["sumar mal las particiones", "poner la cuenta de trabajo como administradora", "olvidar firmar o registrar"],
        "Pregunta: «¿qué regla del estándar revisaste primero?». Si no cita ninguna, pídele que subraye las tres reglas."),
    reinforce="Dibuja un disco como una barra dividida en sistema, datos y espacio sin asignar con medidas inventadas.",
    extend="Explica por qué una buena ficha de configuración ayuda a otra persona del equipo.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (casos de ejemplo). Requisitos del SO-Demo: RAM 4 GB como mínimo y disco libre 64 GB como mínimo. Equipos: EQ-1 con RAM 8 GB y disco libre 120 GB; EQ-2 con RAM 2 GB y disco libre 200 GB; "
     "EQ-3 con RAM 4 GB y disco libre 50 GB; EQ-4 con RAM 4 GB y disco libre 64 GB. Red LAN de ejemplo: 192.168.30.0 con máscara 255.255.255.0; la puerta de enlace es 192.168.30.1; el servicio DHCP entrega direcciones del .100 al .150, ambos incluidos.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso: decidir qué equipos cumplen los requisitos y cómo se incorporan a una LAN con direcciones del servicio DHCP.",
    prior=["Sé qué es un sistema operativo y sus requisitos.", "Sé qué es una dirección IP y una máscara.", "Sé restar y contar rangos."],
    explain=[
        "Para decidir si un equipo puede recibir un sistema operativo se compara cada requisito con los datos del equipo. Un requisito mínimo se cumple si el equipo tiene ese valor o más. Si falla uno solo, el equipo no cumple, aunque los demás datos sobren: más disco no reemplaza la falta de memoria RAM.",
        "Para incorporar un equipo a una LAN hay que dar a cada equipo una dirección IP de esa red, con la misma máscara. Puede ser fija, escrita a mano por el técnico (dirección estática), o automática, entregada por el servicio DHCP desde un rango. La puerta de enlace es la dirección del router, por donde el equipo sale a otras redes. Un equipo con una dirección de otra red no se comunica bien con la LAN.",
        "Un buen análisis de un caso lista los datos, compara con cada requisito, concluye con una frase y nombra el riesgo que queda. También deja constancia: qué equipos no cumplen y qué se propone, como ampliar memoria o dejarlos fuera hasta tener autorización. Los datos son de ejemplo y la decisión final la toma la persona responsable.",
    ],
    vocab=[("requisito mínimo", "valor que el equipo debe tener o superar"), ("dirección estática", "dirección fija escrita a mano en el equipo"), ("rango DHCP", "conjunto de direcciones que el servicio puede entregar"), ("puerta de enlace", "dirección del router por la que el equipo sale a otras redes"), ("holgura", "margen que sobra sobre el mínimo")],
    worked=[
        ("Rango de direcciones", "Un DHCP de ejemplo entrega del .10 al .30, ambos incluidos. ¿Cuántas direcciones entrega?", ["Se restan los extremos: 30 − 10 = 20.", "Como ambos extremos cuentan, se suma 1: 21."], "21 direcciones"),
        ("Cumplir todos los requisitos", "Un equipo de ejemplo tiene RAM 4 GB y disco libre 30 GB, y el sistema pide 4 GB y 64 GB. ¿Cumple?", ["La RAM cumple (4 es igual al mínimo).", "El disco no cumple (30 es menor que 64): falla un requisito."], "No cumple"),
    ],
    mistakes=[("Decir que un equipo cumple porque tiene «mucho disco» aunque le falte RAM.", "Cada requisito se verifica por separado; un valor alto no compensa otro insuficiente.", "Compara requisito por requisito y anota cuál falla."),
              ("Dejar que un equipo use una dirección de otra red en la LAN.", "Con otros tres primeros números, el equipo no está en la misma red y no se comunica bien.", "Verifica que la dirección esté en la red y en el rango previstos.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el servicio DHCP?", "Un servicio que entrega direcciones a los equipos de una red de forma automática", "Un programa que borra archivos viejos", "Un tipo de cable de red", "DHCP asigna direcciones automáticamente desde un rango definido."),
        ("abc", "En Conectividad y Redes: ¿qué es la puerta de enlace?", "La dirección del router por la que un equipo sale a otras redes", "El nombre del switch", "El puerto donde se conecta la impresora", "La puerta de enlace es la salida de la LAN, normalmente la dirección del router."),
        ("abc", "¿Qué es una dirección estática?", "Una dirección fija escrita a mano en el equipo", "Una dirección que cambia cada hora", "Una dirección que no pertenece a ninguna red", "Estática significa que no la entrega el DHCP, sino que la fija el técnico."),
        ("abc", "{F} ¿Qué equipos cumplen los dos requisitos?", "EQ-1 y EQ-4", "EQ-1 y EQ-2", "EQ-3 y EQ-4", "EQ-2 falla por RAM y EQ-3 por disco; EQ-1 y EQ-4 cumplen ambos."),
        ("abc", "{F} ¿Por qué EQ-3 no cumple?", "Tiene 50 GB de disco libre y se necesitan al menos 64", "Tiene poca RAM", "No tiene dirección IP", "Su RAM está en el mínimo, pero el disco libre es menor que 64 GB."),
        ("=", "{F} ¿Cuántas direcciones puede entregar el DHCP, contando el .100 y el .150?", "150-100+1", "Se restan los extremos y se suma 1 porque ambos se incluyen.", " direcciones"),
        ("=", "{F} Se conectan 20 equipos a la LAN y todos piden dirección. ¿Cuántas direcciones del rango quedan libres?", "51-20", "A las 51 direcciones del rango se les restan las 20 usadas.", " direcciones"),
        ("abc", "{F} Un equipo recibe la dirección 192.168.30.120. ¿Está dentro del rango del DHCP?", "Sí, porque 120 está entre 100 y 150", "No, porque termina en 0", "No, porque la puerta de enlace es .1", "El rango va del .100 al .150, y 120 queda dentro."),
        ("abc", "{F} Un equipo aparece con la dirección 192.168.40.120. ¿Qué indica?", "Que está en otra red y no corresponde a esta LAN", "Que está correcto", "Que es la puerta de enlace", "Los tres primeros números 192.168.40 no coinciden con 192.168.30 de la LAN."),
        ("abc", "{F} EQ-2 tiene solo 2 GB de RAM. Un compañero dice: «agrego más disco y cumple». ¿Qué respondes?", "El requisito que falla es la RAM y más disco no la reemplaza", "Tiene razón, el disco compensa", "Basta con instalar un antivirus", "Cada requisito se cumple por separado; el disco no suple la memoria."),
        ("abc", "{F} EQ-4 tiene exactamente 64 GB libres y 4 GB de RAM. ¿Cumple?", "Sí, porque el requisito es un mínimo y lo iguala", "No, porque debe tener más del mínimo", "Solo cumple si tiene 8 GB de RAM", "Un requisito mínimo se cumple al igualarlo, aunque no quede holgura."),
        ("abc", "{F} ¿Qué riesgo práctico tiene EQ-4 aunque cumpla los mínimos?", "Casi no tiene holgura y puede quedarse corto al actualizar o guardar archivos", "No podrá conectarse a ninguna LAN", "Perderá su dirección IP para siempre", "Estar justo en el mínimo deja poco margen para crecer."),
        ("=", "{F} Las direcciones .100 a .109 (10 direcciones) se reservan para impresoras fijas. ¿Cuántas del rango quedan para el DHCP?", "51-10", "A las 51 direcciones del rango se les restan las 10 reservadas.", " direcciones"),
    ],
    ctx=("abc", "Una estudiante pide conectar a la LAN del liceo su computador personal, que tiene sus fotos y documentos. ¿Qué corresponde?", "Consultar a la persona autorizada y respetar la política de uso y la privacidad de sus datos", "Conectarlo y revisar todos sus archivos para ver que esté limpio", "Pedirle su clave personal para configurarlo", "Un equipo personal tiene datos privados; se conecta solo con autorización y sin acceder a lo que no corresponde."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se cuenta un rango del .20 al .30, ambos incluidos?", "Son 11 direcciones", "Se restan los extremos y se suma 1 porque ambos se incluyen."),
        ("¿Qué pasa si un equipo tiene una dirección de otra red?", "No se comunica bien con la LAN", "Los tres primeros números deben coincidir con los de la red."),
        ("¿Basta con que sobre disco si falta RAM?", "No, cada requisito se cumple por separado", "Un valor alto no compensa otro insuficiente."),
    ],
    op=("Un taller de ejemplo tiene el sistema «SO-Demo» (4 GB de RAM, 64 GB de disco libre) y la LAN 192.168.60.0 con máscara 255.255.255.0, puerta de enlace .1 y DHCP del .50 al .90 (ambos incluidos). Equipos: T1 (4 GB, 80 GB libres), T2 (8 GB, 40 GB libres), T3 (6 GB, 100 GB libres). Indica qué equipos cumplen, cuántas direcciones entrega el DHCP, y cuántas quedan si ya hay 15 equipos conectados.",
        "T1 y T3 cumplen; T2 falla por disco (40 es menor que 64). Direcciones: 90 − 50 + 1 = 41. Si hay 15 conectados, quedan 41 − 15 = 26.",
        ["clasifica bien los tres equipos", "calcula el rango con ambos extremos incluidos", "calcula las direcciones libres"],
        ["hoja con tabla de equipos, cálculos y conclusión"],
        ["restar sin sumar 1", "decir que T2 cumple por su RAM", "mezclar la puerta de enlace con el rango DHCP"],
        "Pregunta: «¿por qué sumas 1 al calcular el rango?». Si no sabe, pídele que cuente a mano del .50 al .55."),
    reinforce="Cuenta cuántas direcciones hay del .10 al .25, ambos incluidos, y escribe cómo lo calculaste.",
    extend="Explica una ventaja y un riesgo de usar direcciones estáticas en lugar de DHCP.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (opciones de ejemplo para el equipo de una oficina). Equipo disponible: RAM 8 GB y disco libre 100 GB. Opción 1, «SO-A»: pide RAM 2 GB y disco 20 GB; su fabricante ya no entrega actualizaciones de seguridad; licencia gratuita. "
     "Opción 2, «SO-B»: pide RAM 4 GB y disco 40 GB; recibe actualizaciones de seguridad; la licencia ya está comprada. Criterios de la oficina: cumplir los requisitos del equipo, tener actualizaciones de seguridad vigentes y contar con licencia.")
build(
    O2, 4, F,
    use="Aprenderé a elegir y justificar un sistema operativo con criterios técnicos y de seguridad, y a ordenar las etapas de una configuración responsable.",
    prior=["Sé comparar requisitos mínimos.", "Sé qué son actualizaciones y licencias.", "Sé qué es un respaldo."],
    explain=[
        "Elegir un sistema operativo es una decisión técnica con criterios: que el equipo cumpla los requisitos mínimos, que el sistema reciba actualizaciones de seguridad vigentes, que haya licencia y que sirva para lo que necesita la persona usuaria. Un parche es una actualización que corrige un problema de seguridad; un sistema sin parches queda expuesto a fallas ya conocidas.",
        "La decisión se compara contra cada criterio con datos. Se descartan las opciones que no cumplen un criterio indispensable, aunque tengan otras ventajas, como ser gratuitas. Luego se dejan registrados el criterio, los datos y la persona que autorizó, para que la decisión se pueda revisar.",
        "El trabajo siguiente se hace en un orden responsable: autorización y respaldo, instalación por parte de quien corresponde, actualizaciones, cuentas con permisos mínimos, antivirus y registro en la ficha. Cada etapa deja evidencia y mantiene los estándares de calidad y de seguridad. La recomendación declara su límite: los datos son de ejemplo y decide la persona responsable.",
    ],
    vocab=[("parche", "actualización que corrige un problema de seguridad"), ("criterio indispensable", "condición que una opción debe cumplir sí o sí"), ("permisos mínimos", "dar solo los permisos que cada persona necesita"), ("evidencia", "registro que prueba lo que se hizo"), ("expuesto", "con riesgo por no tener protección actual")],
    worked=[
        ("Descartar por seguridad", "Un sistema de ejemplo es gratuito, pero ya no recibe parches de seguridad. La oficina exige actualizaciones vigentes. ¿Se elige?", ["El criterio de actualizaciones es indispensable.", "No lo cumple, aunque sea gratuito."], "No se elige"),
        ("Total de descarga", "Una actualización de ejemplo pesa 500 MB y hay 4 equipos. ¿Cuántos MB se descargan si cada equipo la descarga por separado?", ["Se multiplica por el número de equipos.", "4 × 500 = 2.000."], "2.000 MB"),
    ],
    mistakes=[("Elegir un sistema solo porque es gratuito.", "Un sistema sin parches de seguridad expone al equipo aunque no cueste dinero.", "Revisa primero los criterios indispensables y luego el costo."),
              ("Dar permisos de administrador a todas las cuentas «para que funcione todo».", "Amplía el daño de cualquier error o programa dañino.", "Entrega permisos mínimos según el trabajo de cada persona.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un parche de seguridad?", "Una actualización que corrige un problema de seguridad", "Un cable de repuesto", "Una copia de los archivos", "Un parche corrige fallas que podrían aprovecharse contra el equipo."),
        ("abc", "¿Por qué importa que el sistema reciba actualizaciones de seguridad vigentes?", "Porque sin ellas el equipo queda expuesto a fallas ya conocidas", "Porque hacen más bonito el escritorio", "Porque permiten usar más cables", "Las actualizaciones cierran fallas conocidas y reducen el riesgo."),
        ("abc", "¿Qué significa dar permisos mínimos?", "Dar solo los permisos que cada persona necesita para su trabajo", "No dar ninguna cuenta a nadie", "Dar permisos de administrador a todos", "Los permisos mínimos limitan el daño que puede causar un error."),
        ("abc", "{F} ¿Qué opción cumple los tres criterios de la oficina?", "SO-B", "SO-A", "Ninguna de las dos", "SO-A no tiene actualizaciones vigentes; SO-B cumple requisitos, actualizaciones y licencia."),
        ("=", "{F} Si se instalaran los programas del SO-B, que piden 40 GB, ¿cuántos GB de disco libre le quedan al equipo?", "100-40", "Al disco libre se le resta el espacio que pide el sistema.", " GB"),
        ("abc", "{F} ¿Por qué se descarta SO-A?", "Porque ya no recibe actualizaciones de seguridad", "Porque exige demasiada RAM", "Porque no tiene licencia", "El criterio indispensable de actualizaciones no se cumple en SO-A."),
        ("=", "{F} El equipo tiene 8 GB de RAM y el SO-B pide 4 GB. ¿Cuántos GB de RAM sobran?", "8-4", "A la memoria del equipo se le resta lo que exige el sistema.", " GB"),
        ("=", "{F} La oficina tiene 30 equipos y una actualización de 500 MB que cada equipo descarga por separado. ¿Cuántos MB se descargan en total?", "30*500", "Se multiplica el tamaño de la actualización por el número de equipos.", " MB"),
        ("abc", "{F} Si la oficina no actualiza nunca el SO-B, ¿qué ocurre con el tiempo?", "Queda expuesto a fallas de seguridad que ya fueron corregidas por parches", "Se vuelve más rápido", "Pierde su licencia automáticamente", "Sin actualizaciones, las fallas corregidas siguen abiertas en ese equipo."),
        ("abc", "{F} Una docente propone usar SO-A «porque es gratis». ¿Qué respuesta técnica corresponde?", "Es gratuito, pero no recibe actualizaciones de seguridad y no cumple un criterio indispensable", "Tiene razón, el costo es lo único importante", "SO-A es mejor porque pide menos RAM", "El costo no reemplaza la seguridad; el criterio de actualizaciones es indispensable."),
        ("abc", "{F} ¿Qué evidencia conviene dejar de la decisión?", "El criterio usado, los datos de cada opción y quién autorizó", "Solo la opinión de una persona", "Nada, porque ya se instaló", "La evidencia permite revisar y repetir la decisión."),
        ("ab", "¿Cuál es el orden más responsable de las etapas?", "Autorización y respaldo, instalación, actualizaciones, cuentas con permisos mínimos y registro en la ficha", "Instalación, registro, respaldo, autorización y actualizaciones", "Primero se protege lo que ya existe y se autoriza; el registro cierra el trabajo."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los datos son de ejemplo y la decisión final la toma la persona responsable con la norma vigente", "Ninguno, porque el sistema elegido es perfecto", "Que el sistema elegido no necesita revisión", "Toda recomendación indica qué parte de la decisión no depende de ella."),
    ],
    ctx=("abc", "Un cliente de ejemplo te pide instalar SO-A en 5 equipos «porque nos sale gratis». Sabes que ya no recibe parches. ¿Qué haces?", "Explico el riesgo con los datos, recomiendo SO-B y dejo registrada su decisión", "Lo instalo sin decir nada", "Lo instalo y desactivo las actualizaciones", "El técnico informa el riesgo con datos y respeta que decida la persona responsable."),
    sc=[
        ("En Conectividad y Redes: ¿qué es un criterio indispensable?", "Una condición que la opción debe cumplir sí o sí", "Si no se cumple, la opción se descarta aunque tenga otras ventajas."),
        ("¿Qué se hace primero en el orden responsable de la configuración?", "Pedir autorización y hacer un respaldo", "Todo cambio parte por proteger lo que ya existe y contar con permiso."),
        ("¿Para qué sirve el registro final en la ficha?", "Para dejar constancia que permita revisar y repetir el trabajo", "Sin registro nadie sabe qué se cambió."),
    ],
    op=("Una bodega de ejemplo debe elegir entre «SO-X» (pide RAM 8 GB y disco 50 GB; sin parches de seguridad vigentes; licencia gratuita) y «SO-Y» (pide RAM 4 GB y disco 30 GB; con parches vigentes; licencia comprada). El equipo tiene RAM 8 GB y disco libre 60 GB. Aplica los criterios de la ficha 8, calcula el disco que sobra con la opción elegida y escribe una recomendación de tres líneas con un límite.",
        "SO-X cumple requisitos, pero no tiene parches vigentes: se descarta. SO-Y cumple requisitos, tiene parches y licencia. Disco que sobra con SO-Y: 60 − 30 = 30 GB. Recomendación: SO-Y, con respaldo previo, cuentas con permisos mínimos y registro en la ficha. Límite: los datos son de ejemplo y decide la persona responsable.",
        ["aplica los tres criterios", "calcula el disco que sobra", "recomienda con datos y declara un límite"],
        ["hoja con tabla de criterios, cálculo y recomendación"],
        ["elegir por ser gratuito", "olvidar el respaldo", "no declarar el límite"],
        "Pregunta: «¿qué criterio descartó a SO-X?». Si responde 'el precio', pídele que lea de nuevo la condición de actualizaciones."),
    reinforce="Lista tres criterios que usarías para elegir un sistema operativo para el computador de tu casa.",
    extend="Explica por qué dejar registrada la decisión también protege a la persona que la tomó.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 9 (edificio de ejemplo, inventado). «Centro Comunitario Las Lengas»: 2 pisos y una sala técnica en el primer piso. Subsistemas del cableado estructurado: cableado troncal o vertical (une la sala técnica con el rack del segundo piso), "
     "cableado horizontal (une el rack de cada piso con cada punto de red) y área de trabajo (el puesto con su punto). Roles: instalador autorizado, supervisor, inspector. Riesgos conocidos: trabajo en altura, cercanía de electricidad, luz de fibra óptica que no se ve, polvo y mala postura. Piso 1: 18 puntos; piso 2: 14 puntos.")
build(
    O3, 1, F,
    use="Aprenderé qué es un cableado estructurado, cuáles son sus partes, quiénes participan y qué riesgos tiene el trabajo en terreno (solo conceptos).",
    prior=["Sé qué es una red LAN.", "Sé leer un plano y un diagrama.", "Sé sumar y multiplicar."],
    explain=[
        "El cableado estructurado es un sistema ordenado y normalizado de cables, conectores y canalizaciones que da servicio de red a un edificio. Se divide en partes: el cableado troncal une las salas de equipos entre pisos o edificios, el cableado horizontal une el rack de cada piso con cada punto de red, y el área de trabajo es el puesto con su punto. Puede usar cable de cobre y fibra óptica, que lleva luz por un hilo de vidrio.",
        "Todo se rige por las especificaciones técnicas del proyecto y por la norma vigente. El trabajo en terreno tiene riesgos serios: trabajo en altura, cercanía de electricidad, polvo, esfuerzo físico y mala postura. La luz de la fibra óptica no se ve y puede dañar los ojos, por eso nunca se mira dentro de una fibra o conector. Estos trabajos los hacen solo personas formadas y autorizadas, con supervisión y elementos de protección.",
        "En este cuaderno solo aprendes los conceptos y a leer los documentos del cableado; no hay instrucciones para instalar." + AVISO,
    ],
    vocab=[("cableado estructurado", "sistema ordenado y normalizado de cables, conectores y canalizaciones"), ("cableado horizontal", "tramo entre el rack de un piso y cada punto de red"), ("cableado troncal", "tramo que une salas de equipos entre pisos o edificios"), ("área de trabajo", "puesto donde está el punto de red"), ("fibra óptica", "cable que lleva señales como luz por un hilo de vidrio"), ("supervisor", "persona que dirige y revisa el trabajo"), ("inspector", "persona que verifica que lo hecho cumple el proyecto y la norma")],
    worked=[
        ("Puntos horizontales", "Un edificio de ejemplo tiene 10 puntos en el piso 1 y 6 en el piso 2. ¿Cuántos puntos tiene el cableado horizontal?", ["Cada punto de cada piso es parte del cableado horizontal.", "10 + 6 = 16."], "16 puntos"),
        ("Ubicar la parte", "¿Qué parte del cableado une el rack del piso 1 con el del piso 2?", ["Une dos pisos, es decir, es vertical.", "Esa parte se llama cableado troncal."], "El cableado troncal"),
    ],
    mistakes=[("Ayudar a pasar cables por el cielo falso en altura «porque se ve fácil».", "El trabajo en altura tiene riesgo de caída y solo lo hace personal formado y autorizado.", "No participes; pide instrucción y deja el trabajo a quien corresponde."),
              ("Mirar el extremo de una fibra óptica para ver si «tiene luz».", "La luz no es visible y puede dañar los ojos sin que lo notes.", "Nunca mires dentro de una fibra o conector; quien mide usa instrumentos y protección.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el cableado estructurado?", "Un sistema ordenado y normalizado de cables, conectores y canalizaciones que da servicio de red a un edificio", "Un solo cable largo que une todos los computadores", "Un programa para configurar redes", "El cableado estructurado se organiza en partes y se rige por normas."),
        ("abc", "En Conectividad y Redes: ¿qué une el cableado horizontal?", "El rack de un piso con cada punto de red", "Un edificio con otro", "El computador con su impresora a través del aire", "El tramo horizontal llega desde el rack del piso hasta cada punto de red."),
        ("abc", "¿Por qué nunca se mira dentro de una fibra óptica?", "Porque la luz no se ve y puede dañar los ojos", "Porque se ensucia con la mirada", "Porque la fibra apaga el computador", "La luz de la fibra es invisible y puede lesionar la vista sin que se note."),
        ("abc", "{F} ¿Qué une el cableado troncal en este edificio?", "La sala técnica con el rack del segundo piso", "Cada puesto con su punto", "La impresora con el computador", "Según la ficha, el troncal une la sala técnica con el rack del segundo piso."),
        ("abc", "{F} ¿Quién verifica que lo instalado cumple el proyecto y la norma?", "El inspector", "El cliente de otro edificio", "Cualquier visitante", "El inspector es quien revisa el cumplimiento."),
        ("abc", "{F} ¿Cuál de estos riesgos es propio de trabajar con fibra óptica?", "La luz invisible que puede dañar los ojos", "El exceso de memoria RAM", "La cantidad de contraseñas", "La luz que viaja por la fibra no se ve, por eso es un riesgo para la vista."),
        ("=", "{F} ¿Cuántos puntos de red tiene el cableado horizontal del edificio?", "18+14", "Se suman los puntos de los dos pisos.", " puntos"),
        ("=", "{F} Cada punto lleva un conector en el puesto y otro en el panel del rack. ¿Cuántos conectores hay en total?", "(18+14)*2", "Se multiplica el total de puntos por los dos conectores de cada uno.", " conectores"),
        ("abc", "{F} Una persona sin formación quiere ayudar a pasar cables por el cielo falso. ¿Qué corresponde?", "No participar: ese trabajo exige personal autorizado, norma vigente y protección", "Participar si trabaja rápido", "Participar si no hay supervisor", "El trabajo en altura es de personal formado; querer ayudar no reemplaza la autorización."),
        ("abc", "El supervisor de ejemplo ordena tender cable cerca de un tablero eléctrico «rápido y sin avisar». ¿Qué corresponde?", "Detenerse y exigir instrucción: el trabajo cerca de electricidad requiere personal autorizado y norma vigente", "Obedecer porque lo manda el supervisor", "Desconectar el tablero por cuenta propia", "El riesgo eléctrico exige personal habilitado; la urgencia no justifica saltarse la norma."),
        ("abc", "Una estudiante en práctica ve el conector abierto de una fibra y quiere mirar para ver si «hay luz». ¿Qué corresponde?", "No mirar y avisar al instructor, que usa los instrumentos y la protección adecuados", "Mirar solo un segundo", "Mirar con una lupa para ver mejor", "Ningún tiempo ni lupa hace seguro mirar una fibra: el daño ocurre sin dolor."),
        ("abc", "{F} Una técnica pasa horas inclinada sobre un rack sin descansar. ¿Qué principio ergonómico se incumple?", "Mantener buena postura y hacer pausas", "Usar siempre el mismo color de cable", "Archivar el plano en una carpeta", "La ergonomía exige posturas adecuadas y pausas para cuidar el cuerpo."),
        ("abc", "¿Por qué este cuaderno no te habilita para trabajar en cableado?", "Porque el aprendizaje en papel no reemplaza la formación práctica supervisada ni la norma vigente", "Porque el cableado es demasiado simple", "Porque la norma no existe", "El oficio exige formación presencial, instructor autorizado y protección."),
    ],
    ctx=("abc", "En tu práctica de ejemplo, un compañero te dice que subas a una escalera a tender cable porque «faltan manos». No tienes formación ni autorización. ¿Qué haces?", "Me niego, aviso al instructor y sigo con tareas que sí me corresponden, como leer y rotular en papel", "Subo, pero con cuidado", "Subo si él sostiene la escalera", "El trabajo en altura exige personas formadas y autorizadas; avisar es la conducta correcta."),
    sc=[
        ("En Conectividad y Redes: ¿qué une el cableado troncal?", "Salas de equipos de distintos pisos o edificios", "El troncal es el tramo que conecta entre sí los racks principales."),
        ("¿Por qué no se mira dentro de una fibra?", "La luz no se ve y puede dañar los ojos", "El daño puede ocurrir sin que la persona lo note."),
        ("¿Quién puede hacer trabajos en altura o cerca de electricidad?", "Solo personal formado y autorizado, con norma vigente y protección", "Los riesgos de esos trabajos exigen formación y supervisión."),
    ],
    op=("Un colegio de ejemplo tiene 3 pisos con estas cantidades de puntos de red: piso 1, 20; piso 2, 24; piso 3, 16. Calcula el total de puntos del cableado horizontal y el total de conectores si cada punto lleva dos. Luego escribe cuál es el cableado troncal en un edificio de tres pisos y una regla de seguridad que se aplica a quien trabaja en terreno.",
        "Puntos: 20 + 24 + 16 = 60. Conectores: 60 × 2 = 120. El troncal une la sala técnica con los racks de cada piso. Regla: el trabajo en altura o cerca de electricidad lo hace solo personal formado y autorizado, con norma vigente y protección; yo no lo hago sin instructor.",
        ["calcula puntos y conectores", "nombra el tramo troncal", "escribe una regla de seguridad correcta"],
        ["hoja con cálculos, definición y regla"],
        ["usar la suma como si fuera el troncal", "olvidar duplicar los conectores", "proponer hacer el trabajo sin instructor"],
        "Pregunta: «¿qué diferencia hay entre troncal y horizontal?». Si no distingue, pídele que dibuje un edificio de tres pisos y marque ambos tramos."),
    reinforce="Dibuja un edificio de dos pisos con una sala técnica, un rack por piso, el tramo troncal y tres puntos por piso.",
    extend="Explica por qué la formación y la supervisión son parte de la seguridad en el trabajo de cableado.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 10 (glosario y documentos de ejemplo). Medios: cable de par trenzado UTP (cobre) de categoría 5e o 6; fibra óptica multimodo (distancias cortas dentro de un edificio) y monomodo (distancias largas). "
     "Elementos: panel de parcheo, cordón de parcheo, rack, canalización (ducto o bandeja por donde van los cables) y toma. Límite de ejemplo para el cableado horizontal de cobre: el cable permanente llega hasta 90 m y, con los cordones, el canal completo llega hasta 100 m. "
     "Documentos: especificaciones técnicas, planilla de puntos, plano de cableado e informe de certificación. Rotulado de ejemplo: P2-A07 significa piso 2, panel A, puerto 07.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario del cableado estructurado (medios, elementos, rotulado) y los documentos con que se lee y se verifica (solo conceptos).",
    prior=["Sé qué es el cableado horizontal y el troncal.", "Sé leer un plano.", "Sé que los riesgos del terreno exigen personal autorizado."],
    explain=[
        "El cableado estructurado usa distintos medios. El cable UTP de par trenzado es de cobre y se clasifica en categorías, como la 5e y la 6, según el desempeño que se espera. La fibra óptica lleva luz por un hilo de vidrio: la multimodo sirve para distancias cortas dentro de un edificio y la monomodo para distancias largas. Cada medio tiene límites de distancia que fijan las especificaciones técnicas.",
        "Los elementos se nombran con precisión: el rack es el gabinete; el panel de parcheo agrupa los extremos de los cables permanentes; el cordón de parcheo es el cable corto que une el panel con un equipo; la canalización es el ducto o bandeja por donde van los cables. El rotulado identifica cada punto con un código único, por ejemplo P2-A07, para que cualquiera lo encuentre en los documentos.",
        "Los documentos clave son las especificaciones técnicas (qué debe cumplirse), la planilla de puntos (lista de cada punto con su destino y largo), el plano de cableado (dónde va cada tramo) y el informe de certificación (resultado de la medición con instrumento, hecho por personal autorizado)." + AVISO,
    ],
    vocab=[("UTP", "cable de cobre de pares trenzados sin blindaje"), ("categoría", "clasificación del cable según su desempeño, como 5e o 6"), ("panel de parcheo", "panel donde terminan los cables permanentes"), ("cordón de parcheo", "cable corto que une el panel con un equipo"), ("canalización", "ducto o bandeja por donde pasan los cables"), ("rotulado", "identificación de cada punto con un código"), ("informe de certificación", "resultado de medir un enlace con instrumento")],
    worked=[
        ("Leer un rotulado", "En el código P1-B12 de ejemplo, ¿qué significa cada parte?", ["P1 es el piso 1.", "B es el panel B y 12 es el puerto 12."], "Piso 1, panel B, puerto 12"),
        ("Largo permanente", "Un canal de ejemplo de cobre puede llegar hasta 100 m y los cordones suman 10 m. ¿Cuántos metros puede medir el cable permanente?", ["Al canal se le resta lo que ocupan los cordones.", "100 − 10 = 90."], "90 m"),
    ],
    mistakes=[("Rotular los cables con apodos distintos según cada persona.", "Si cada persona usa su apodo, nadie puede encontrar el punto en la documentación.", "Usa el esquema de rotulado del proyecto, igual en planos, planilla y panel."),
              ("Confiar en que un enlace «funciona» sin informe de certificación.", "Que funcione hoy no prueba que cumple los límites de la especificación técnica.", "Exige el informe de certificación, hecho por personal autorizado, y archívalo.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un panel de parcheo?", "Un panel donde terminan los cables permanentes y se conectan los cordones", "Un programa para dibujar planos", "Una caja de herramientas", "El panel de parcheo agrupa los extremos de los cables permanentes."),
        ("abc", "En Conectividad y Redes: ¿qué es un cable UTP?", "Un cable de cobre de pares trenzados", "Un cable de fibra óptica de luz", "Un cable de electricidad de red", "UTP es de cobre con pares trenzados, usado para datos."),
        ("abc", "¿Qué es un informe de certificación?", "El resultado de medir un enlace con un instrumento, hecho por personal autorizado", "Un permiso para entrar a la obra", "Una lista de precios", "El informe documenta las mediciones del enlace frente a la especificación."),
        ("abc", "{F} ¿Qué indica el código P2-A07?", "Piso 2, panel A, puerto 07", "Piso 7, panel A, puerto 2", "Persona 2, área 07", "El rotulado de la ficha se lee piso, panel y puerto."),
        ("abc", "{F} ¿Qué documento lista cada punto con su destino y largo?", "La planilla de puntos", "El informe de certificación", "El plano de planta del terreno", "La planilla de puntos enumera cada punto; el informe registra mediciones."),
        ("abc", "{F} ¿Cuál es el límite de ejemplo del cable permanente horizontal de cobre?", "90 m", "100 m", "250 m", "Los 100 m son del canal completo con cordones; el permanente llega hasta 90 m."),
        ("=", "{F} Los cordones de un canal suman 10 m. ¿Cuántos metros puede medir como máximo el cable permanente?", "100-10", "Al canal de 100 m se le resta lo que ocupan los cordones.", " metros"),
        ("abc", "{F} ¿Qué código corresponde al puerto 12 del panel B del piso 1?", "P1-B12", "P1-A12", "P2-B12", "El código se arma con piso 1, panel B y puerto 12."),
        ("=", "{F} Una planilla tiene 4 paneles de 24 puertos cada uno. ¿Cuántos puertos hay en total?", "4*24", "Se multiplica la cantidad de paneles por los puertos de cada uno.", " puertos"),
        ("abc", "{F} Un punto de cobre tiene un cable permanente de 95 m. ¿Qué conclusión corresponde?", "Supera el límite de 90 m y hay que revisar el recorrido o el diseño", "Cumple porque es menor que 100 m", "Cumple porque el cable es nuevo", "El límite del permanente es 90 m; los 100 m son del canal completo."),
        ("abc", "Dos técnicos rotulan los mismos cables con códigos distintos en el plano y en el panel. ¿Qué problema produce?", "Nadie puede relacionar el punto del panel con el de los documentos", "El cable pierde su categoría", "El rack cambia de tamaño", "El rotulado debe ser único y coincidir en todos los documentos."),
        ("abc", "{F} ¿Cuándo conviene la fibra óptica en vez del cobre?", "Cuando las distancias son largas o superan el límite del cobre", "Cuando el enlace mide menos de 5 m", "Cuando no hay planilla de puntos", "El cobre tiene límite de distancia y la fibra sirve para distancias largas."),
        ("abc", "{F} Un instalador entrega un enlace sin informe de certificación porque «funciona». ¿Qué corresponde?", "Exigir el informe de certificación, hecho por personal autorizado, antes de aceptarlo", "Aceptarlo, porque funciona hoy", "Pedir solo que lo rotulen de nuevo", "Que funcione no prueba que cumple las especificaciones; la certificación lo verifica."),
    ],
    ctx=("abc", "El cliente pregunta cómo sabrá que los 40 puntos instalados cumplen lo pedido. ¿Qué respondes?", "Con el informe de certificación de cada punto, comparado con las especificaciones técnicas", "Con mi palabra de que se ven bien", "Probando solo 2 puntos al azar y mostrando una foto", "La verificación se apoya en mediciones documentadas, no en la apariencia."),
    sc=[
        ("En Conectividad y Redes: ¿qué es un cordón de parcheo?", "El cable corto que une el panel con un equipo", "Se usa en los extremos del canal y se suma a la distancia total."),
        ("¿Para qué sirve el rotulado?", "Para identificar cada punto con un código único en el panel y en los documentos", "Un código común permite encontrar y revisar cualquier punto."),
        ("¿Qué medio se usa para distancias largas?", "La fibra óptica monomodo", "La monomodo sirve para distancias largas; la multimodo, para distancias cortas."),
    ],
    op=("Una escuela de ejemplo tiene un panel B en el piso 2 con puertos del 01 al 24. Se te entregan estos cables de ejemplo: puerto 05 hacia la sala de computación (largo 62 m), puerto 11 hacia la biblioteca (largo 94 m), puerto 19 hacia la dirección (largo 48 m). Rotula cada punto con el esquema de la ficha 10, indica cuál supera el límite de 90 m y qué documento archivarías.",
        "Rótulos: P2-B05, P2-B11 y P2-B19. Supera el límite P2-B11 (94 m es mayor que 90 m); hay que revisar el recorrido o el diseño. Archivaría la planilla de puntos y el informe de certificación de cada punto, hecho por personal autorizado.",
        ["rotula bien los tres puntos", "detecta el que supera el límite", "nombra un documento de respaldo"],
        ["tabla de tres filas con código, largo y conclusión"],
        ["invertir piso y panel", "usar 100 m como límite del permanente", "no mencionar el informe"],
        "Pregunta: «¿por qué 94 m no cumple si el canal llega a 100 m?». Si no sabe, repasa la diferencia entre permanente y canal."),
    reinforce="Inventa cinco códigos de rotulado para el piso 1 de un edificio con el esquema de la ficha.",
    extend="Explica por qué se usan cordones cortos y no cables permanentes largos para conectar los equipos.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 11 (planilla de puntos de ejemplo, medidas tomadas de un plano de ejemplo). Límite del cable permanente: 90 m. Puntos: P1-A01 = 35 m; P1-A02 = 58 m; P1-A03 = 91 m; P1-A04 = 72 m; P2-A01 = 88 m; P2-A02 = 96 m. "
     "Se agrega una reserva de 10 % de cable para curvas y sobrantes. El rollo disponible tiene 500 m.")
build(
    O3, 3, F,
    use="Aprenderé a analizar una planilla de puntos: calcular el cable necesario, detectar puntos fuera del límite y decidir qué corregir (solo en papel).",
    prior=["Conozco el límite del cable permanente.", "Sé leer el rotulado.", "Sé calcular un 10 % de una cifra redonda."],
    explain=[
        "Una planilla de puntos lista cada punto de red con su código y el largo estimado desde el panel. Con ella se calcula el cable necesario: se suman los largos y se agrega una reserva para curvas y sobrantes, por ejemplo el 10 %. El total se compara con el rollo disponible, y si no alcanza, se pide más antes de empezar.",
        "También se compara cada largo con el límite del cable permanente. Un punto que supera el límite no cumple la especificación aunque funcione. Las salidas razonables son revisar el recorrido, cambiar la ubicación del rack o del punto, o usar otro medio, siempre con aprobación de la jefa de proyecto y dejando constancia en los documentos. No se corta ni se mide en el sitio sin autorización.",
        "Un punto con poco margen, como 88 m frente a 90 m, cumple pero merece revisión, porque el recorrido real puede ser más largo que el del plano. Todo cálculo se redacta con sus datos y su límite: las medidas son de ejemplo, y las reales las toma personal autorizado." + AVISO,
    ],
    vocab=[("planilla de puntos", "lista de cada punto con su código, destino y largo"), ("reserva de cable", "porcentaje extra de cable para curvas y sobrantes"), ("margen", "diferencia entre el valor y el límite"), ("rollo", "cable enrollado que se entrega en cantidad fija"), ("recorrido", "camino por donde pasa el cable"), ("enlace permanente", "tramo fijo entre el panel y la toma, sin los cordones")],
    worked=[
        ("Total con reserva", "Dos puntos de ejemplo miden 50 m y 70 m y se agrega una reserva de 10 %. ¿Cuántos metros de cable se necesitan?", ["Suma: 50 + 70 = 120.", "Reserva: 10 % de 120 es 12; total 120 + 12 = 132."], "132 m"),
        ("Revisar el margen", "Un punto de ejemplo mide 89 m y el límite es 90 m. ¿Cumple y qué precaución conviene?", ["89 es menor que 90: cumple.", "El margen es 1 m, por lo que conviene verificar el recorrido real."], "Cumple con poco margen; revisar el recorrido"),
    ],
    mistakes=[("Comprar el cable sumando los largos sin reserva.", "Las curvas, los sobrantes y los errores de medida consumen cable.", "Agrega la reserva definida por el proyecto antes de comparar con el rollo."),
              ("Cortar los cables para que «calcen» con el límite sin avisar.", "No se alteran los recorridos ni los largos sin aprobación; podrían quedar fuera de la especificación.", "Informa a la jefa de proyecto y deja constancia de la solución aprobada.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una reserva de cable?", "Un porcentaje extra de cable previsto para curvas y sobrantes", "Un cable guardado que nunca se usa", "El cable que se devuelve al proveedor", "La reserva cubre lo que las curvas y las medidas imperfectas consumen."),
        ("abc", "En Conectividad y Redes: ¿qué es el margen de un punto?", "La diferencia entre su largo y el límite permitido", "La suma de todos los largos", "El código del punto", "El margen indica cuánto falta para llegar al límite."),
        ("abc", "¿Qué es un enlace permanente?", "El tramo fijo entre el panel y la toma, sin los cordones", "El cordón que va de la toma al computador", "Un cable que se cambia todos los días", "El permanente es el tramo instalado de forma fija; los cordones se suman al canal."),
        ("abc", "{F} ¿Qué puntos superan el límite del cable permanente?", "P1-A03 y P2-A02", "Solo P2-A02", "P1-A03 y P2-A01", "91 m y 96 m superan 90 m; 88 m cumple."),
        ("=", "{F} ¿Cuántos metros de cable suman los seis puntos?", "35+58+91+72+88+96", "Se suman los seis largos de la planilla.", " metros"),
        ("abc", "{F} ¿Qué punto tiene el recorrido más corto?", "P1-A01", "P1-A02", "P2-A01", "Con 35 m, P1-A01 es el más corto."),
        ("=", "{F} ¿Cuántos metros son la reserva del 10 % sobre el total de la planilla?", "(35+58+91+72+88+96)*10//100", "Se calcula el 10 % del total de metros.", " metros"),
        ("=", "{F} ¿Cuántos metros de cable se necesitan en total, con la reserva incluida?", "(35+58+91+72+88+96)+(35+58+91+72+88+96)*10//100", "Al total se le suma el 10 % de reserva.", " metros"),
        ("=", "{F} ¿Cuántos metros del rollo de 500 m sobran después de cubrir el total con reserva?", "500-((35+58+91+72+88+96)+(35+58+91+72+88+96)*10//100)", "Al rollo se le resta el cable necesario con reserva.", " metros"),
        ("abc", "{F} Para los dos puntos que superan 90 m, ¿qué decisión es razonable?", "Revisar el recorrido o la ubicación del punto o del rack, con aprobación y constancia", "Instalarlos igual porque funcionan", "Cortar los cables a 90 m sin mirar el plano", "Un punto fuera del límite se corrige en el diseño, con aprobación y registro."),
        ("abc", "{F} El punto P2-A01 mide 88 m. ¿Qué corresponde?", "Cumple por 2 m, pero conviene revisar el recorrido real porque el margen es pequeño", "No cumple", "Cumple y no requiere ninguna precaución", "Un margen pequeño exige verificar que el recorrido real no sea mayor al del plano."),
        ("=", "{F} Tras rediseñar, P1-A03 pasa a medir 60 m y P2-A02 pasa a medir 70 m. ¿Cuántos metros suman ahora los seis puntos?", "35+58+60+72+88+70", "Se reemplazan los largos corregidos y se suma de nuevo.", " metros"),
        ("abc", "{F} Un informe de ejemplo dice «P2-A02: longitud 96 m, resultado: falla». ¿Qué relación tiene con la planilla?", "Confirma que supera 90 m; hay que corregir el diseño y volver a certificar", "Muestra que el cable es de mala calidad", "No tiene relación con la planilla", "El resultado coincide con el largo de la planilla, que excede el límite."),
    ],
    ctx=("abc", "La planilla suma 484 m con reserva, pero el instalador dice haber usado 560 m y pide que se le pague todo. ¿Qué corresponde?", "Pedir el respaldo de la diferencia y consultar al supervisor antes de aceptar el cobro", "Aprobar el pago porque confías", "Rechazar el pago sin mirar nada", "Una diferencia grande se verifica con evidencia antes de aprobar un pago."),
    sc=[
        ("En Conectividad y Redes: ¿para qué se agrega una reserva de cable?", "Para cubrir curvas, sobrantes y pequeñas diferencias de medida", "Sin reserva el cable puede faltar a mitad del trabajo."),
        ("¿Qué haces con un punto que supera el límite del permanente?", "Reviso el diseño y propongo una solución con aprobación y constancia", "El punto fuera del límite no cumple la especificación."),
        ("¿Cuál es el riesgo de un margen muy pequeño?", "Que el recorrido real sea más largo y el punto quede fuera del límite", "El plano es una estimación; el recorrido real puede ser distinto."),
    ],
    op=("Una biblioteca de ejemplo tiene cuatro puntos: P1-A01 = 40 m; P1-A02 = 85 m; P1-A03 = 93 m; P1-A04 = 62 m. Límite del permanente: 90 m. Reserva de 10 %. Rollo de 300 m. Calcula el total con reserva, cuántos metros sobran del rollo, cuáles puntos superan el límite y qué propondrías para ellos.",
        "Suma: 40 + 85 + 93 + 62 = 280; reserva: 28 m (10 % de 280); total 308 m, que supera el rollo de 300 m: faltan 8 m. Supera el límite P1-A03 (93 m). Propuesta: revisar el recorrido o la ubicación del rack con aprobación de la jefa de proyecto y pedir más cable.",
        ["suma y aplica la reserva", "compara con el rollo y concluye", "detecta el punto fuera de límite y propone una solución con constancia"],
        ["hoja con cálculos, conclusión y propuesta"],
        ["olvidar la reserva", "no comparar con el rollo", "proponer cortar o alterar el recorrido sin aprobación"],
        "Pregunta: «¿alcanza el rollo?». Si responde sí sin calcular, pídele que sume la reserva."),
    reinforce="Con cinco largos inventados menores de 90 m, calcula el total con una reserva de 10 %.",
    extend="Explica por qué un punto que 'funciona' puede igualmente no cumplir la especificación.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 12 (enlace entre dos edificios de ejemplo). Distancia entre los racks: 2.000 m. Opción A: cable de cobre UTP (el canal llega hasta 100 m). "
     "Opción B: fibra multimodo; pérdida de ejemplo de 4 dB por kilómetro y 1 dB por conector, con 2 conectores en el enlace; la pérdida máxima que acepta el equipo es 6 dB. "
     "Opción C: fibra monomodo; pérdida de ejemplo de 1 dB por kilómetro y 1 dB por conector, con 2 conectores; la pérdida máxima que acepta el equipo es 10 dB.")
build(
    O3, 4, F,
    use="Aprenderé a elegir el medio de un enlace con datos de distancia y pérdida de señal, y a escribir una recomendación con sus límites (solo en papel).",
    prior=["Conozco cobre y fibra óptica.", "Sé el límite de distancia del cobre.", "Sé multiplicar y comparar cifras."],
    explain=[
        "La atenuación es la pérdida de potencia de la señal en su trayecto y se mide en decibeles (dB). Cuanto más largo es el enlace y más conectores tiene, más pérdida acumula. Cada equipo acepta una pérdida máxima: si la pérdida total del enlace es menor o igual que ese valor, el enlace puede funcionar; si es mayor, no.",
        "Para decidir entre medios se calcula con datos: primero se descartan los que no llegan por distancia, como el cobre más allá de 100 m. Luego, para la fibra, la pérdida total es la pérdida por kilómetro multiplicada por los kilómetros del enlace, más la de los conectores. Se compara con el máximo del equipo y se elige la opción que cumple, considerando el costo.",
        "Una recomendación se escribe con sus datos y con sus límites: aquí los valores son de ejemplo y la decisión real depende de las especificaciones técnicas, la norma vigente y la certificación con instrumentos, hecha por personal autorizado." + AVISO,
    ],
    vocab=[("atenuación", "pérdida de potencia de la señal en el trayecto"), ("decibel (dB)", "unidad con que se mide la pérdida o ganancia de señal"), ("pérdida máxima", "valor máximo de pérdida que acepta el equipo"), ("multimodo", "fibra para distancias cortas"), ("monomodo", "fibra para distancias largas")],
    worked=[
        ("Pérdida total de una fibra", "Un enlace de ejemplo mide 3 km, la fibra pierde 2 dB por km y hay 2 conectores de 1 dB. ¿Cuál es la pérdida total?", ["Fibra: 3 × 2 = 6 dB.", "Conectores: 2 × 1 = 2 dB; total 6 + 2 = 8 dB."], "8 dB"),
        ("Cumplir el máximo", "El equipo del ejemplo acepta hasta 10 dB y la pérdida total es 8 dB. ¿Cumple?", ["Se compara 8 con el máximo de 10.", "8 es menor que 10."], "Sí, cumple"),
    ],
    mistakes=[("Olvidar la pérdida de los conectores al calcular el enlace.", "Los conectores también restan potencia y pueden dejar el enlace fuera del máximo.", "Suma siempre fibra y conectores."),
              ("Elegir por precio sin comprobar la pérdida.", "Una opción barata que supera el máximo no funcionará bien.", "Comprueba primero el criterio técnico y luego compara el costo.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es la atenuación?", "La pérdida de potencia de la señal en su trayecto", "El aumento de velocidad del cable", "La cantidad de puertos del switch", "La atenuación mide cuánto se debilita la señal al viajar."),
        ("abc", "¿En qué unidad se mide la pérdida de señal?", "En decibeles (dB)", "En voltios", "En litros", "Los decibeles se usan para expresar pérdida o ganancia de señal."),
        ("abc", "¿Qué es la pérdida máxima de un equipo?", "El mayor valor de pérdida que el equipo acepta para funcionar", "El precio más alto del equipo", "El número de conectores", "Si la pérdida del enlace supera ese valor, la señal llega demasiado débil."),
        ("abc", "{F} ¿Por qué se descarta la opción A?", "Porque el cobre llega hasta 100 m y el enlace mide 2.000 m", "Porque el cobre no se puede rotular", "Porque el cobre pesa mucho", "La distancia del enlace supera el límite del canal de cobre."),
        ("=", "{F} ¿Cuántos dB pierde en total la opción B (fibra por kilómetro y conectores)?", "2*4+2*1", "Se suman la pérdida de la fibra en 2 km y la de los dos conectores.", " dB"),
        ("=", "{F} ¿Cuántos dB pierde en total la opción C?", "2*1+2*1", "Se suman la pérdida de la fibra en 2 km y la de los dos conectores.", " dB"),
        ("abc", "{F} ¿Qué opción cumple el máximo del equipo?", "La opción C", "La opción A", "La opción B", "B pierde 10 dB y su máximo es 6; C pierde 4 dB y su máximo es 10."),
        ("=", "{F} ¿Cuántos dB de margen le quedan a la opción C respecto de su máximo?", "10-(2*1+2*1)", "Al máximo del equipo se le resta la pérdida total.", " dB"),
        ("=", "{F} Si a la opción C se le agregaran 2 conectores más (4 en total), ¿cuál sería la pérdida total?", "2*1+4*1", "Se suma la pérdida de la fibra y la de los cuatro conectores.", " dB"),
        ("abc", "{F} Un técnico dice: «la B cuesta menos, la recomiendo igual». ¿Qué responde un criterio técnico?", "La B pierde 10 dB y el equipo acepta 6: no cumple, por barata que sea", "Tiene razón, el costo manda", "La B es mejor porque es multimodo", "El criterio de pérdida es indispensable y se verifica antes del costo."),
        ("abc", "{F} ¿Qué debe hacerse antes de dar por bueno el enlace elegido?", "Certificarlo con instrumentos, por personal autorizado, y archivar el informe", "Mirar dentro de la fibra para ver la luz", "Aceptarlo por el cálculo del ejemplo", "El cálculo es una estimación; la certificación comprueba el enlace real."),
        ("=", "{F} Si el enlace de la opción C midiera 5.000 m (5 km) con 2 conectores, ¿cuántos dB perdería?", "5*1+2*1", "Se suma la pérdida de 5 km de fibra y la de los dos conectores.", " dB"),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los valores son de ejemplo y la decisión real depende de las especificaciones técnicas, la norma vigente y la certificación", "Ninguno, porque el cálculo es exacto", "Que el cliente no debe revisar la propuesta", "Los datos de la ficha son de ejemplo; la realidad se verifica con norma y medición."),
    ],
    ctx=("abc", "Un cliente de ejemplo quiere unir dos bodegas separadas por 150 m con cable de cobre «porque es lo que ya tenemos». El límite del cobre es 100 m. ¿Qué respondes?", "Que 150 m supera el límite del cobre y que conviene evaluar fibra óptica, con la especificación y un profesional autorizado", "Que se pueden unir con cobre y probar si funciona", "Que da lo mismo la distancia", "Una distancia mayor al límite no se resuelve probando: se cambia de medio o se rediseña."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula la pérdida total de un enlace de fibra?", "Pérdida por kilómetro por los kilómetros, más la de los conectores", "Se suman las pérdidas de la fibra y de los conectores."),
        ("¿Cuándo se acepta un enlace de fibra?", "Cuando su pérdida total es menor o igual que la máxima del equipo", "Si la pérdida supera el máximo, la señal llega muy débil."),
        ("¿Quién certifica el enlace real?", "Personal autorizado con instrumentos", "El instrumento mide el enlace real y el informe se archiva."),
    ],
    op=("Dos edificios de ejemplo están a 3.000 m. Fibra multimodo: 3 dB por km, 1 dB por conector, 2 conectores, máximo del equipo 8 dB. Fibra monomodo: 1 dB por km, 1 dB por conector, 2 conectores, máximo del equipo 10 dB. Calcula la pérdida de cada opción, indica cuál cumple, y escribe dos líneas de recomendación con un límite.",
        "Multimodo: 3 × 3 + 2 × 1 = 11 dB, mayor que 8: no cumple. Monomodo: 3 × 1 + 2 × 1 = 5 dB, menor que 10: cumple, con 5 dB de margen. Recomendación: monomodo, con certificación por personal autorizado. Límite: los valores son de ejemplo y no habilitan para instalar.",
        ["calcula la pérdida de cada opción", "compara con el máximo y elige", "escribe recomendación y límite"],
        ["hoja con cálculos y recomendación"],
        ["olvidar los conectores", "comparar con el máximo de la otra opción", "no declarar límite"],
        "Pregunta: «¿qué máximo comparas con cada opción?». Si los mezcla, pídele que anote el máximo al lado de cada cálculo."),
    reinforce="Calcula la pérdida de un enlace de 1 km con 1 dB por km y 2 conectores de 1 dB.",
    extend="Explica por qué el cálculo en papel no reemplaza la medición con instrumentos.",
)

"""Programación TP 3.º y 4.º medio: OAE-07 (soporte técnico a usuarios, local o remoto) y OAE-08 (instalar y actualizar hardware y software). Casos de papel con datos inventados; no se hace ningún trabajo práctico sobre equipos."""
from __future__ import annotations

from tp_prog_common import build

O7 = "TP-PROG-3y4-OAE-07"
O8 = "TP-PROG-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 25 (ticket de ejemplo, inventado). Ticket TK-01 de la «Oficina Contable Sur» (nombre de ejemplo): usuaria Clara (nombre de ejemplo), problema «no puedo abrir mi planilla», prioridad media, estado «abierto». "
     "Atención posible: local (el técnico va al puesto de trabajo) o remota (el técnico se conecta al equipo a través de la red, solo con permiso de la usuaria). Reglas de la oficina de ejemplo: el técnico nunca pide la contraseña de la usuaria; "
     "toda conexión remota se registra en el ticket.")
build(
    O7, 1, F,
    use="Aprenderé en qué consiste el soporte técnico, cómo se atiende de forma local o remota y qué cuidados de privacidad y seguridad exige.",
    prior=["Sé qué es un computador y un programa.", "Sé qué es un dato personal.", "Sé qué es un respaldo."],
    explain=[
        "El soporte técnico es la ayuda que se da a las personas para que puedan usar bien sus computadores y programas. Se atiende por una mesa de ayuda: un punto donde las usuarias piden ayuda y el pedido se anota en un ticket, un registro con número, usuaria, descripción del problema, prioridad y estado. El soporte puede ser local, en el puesto de la persona, o remoto, conectándose al equipo a través de la red.",
        "En el soporte remoto la usuaria da su permiso para que el técnico vea o controle su pantalla, y puede terminar la conexión cuando quiera. Mientras tanto el técnico ve información privada, como correos o documentos, por eso solo mira lo necesario para resolver el problema y no copia ni guarda nada. Todo se registra en el ticket: qué se hizo, cuándo y con qué permiso.",
        "La seguridad es una regla central: el técnico nunca pide ni anota la contraseña de la usuaria; si hace falta acceder, usa su propia cuenta con permiso o ayuda a la usuaria a cambiar la suya. Hay personas que se hacen pasar por soporte para engañar y obtener claves (ingeniería social): se desconfía de un llamado inesperado que pide contraseñas y se verifica con la jefatura.",
    ],
    vocab=[("soporte técnico", "ayuda a las personas para usar bien sus equipos y programas"), ("mesa de ayuda", "punto donde se piden y registran las ayudas"), ("ticket", "registro de un pedido de ayuda con su estado"), ("soporte remoto", "ayuda a través de la red sobre el equipo de la usuaria"), ("consentimiento", "permiso que da la persona"), ("ingeniería social", "engaño a una persona para obtener datos o claves")],
    worked=[
        ("Local o remoto", "El técnico de ejemplo se sienta frente al computador de la usuaria para revisar la impresora. ¿El soporte es local o remoto?", ["El técnico está en el puesto de la usuaria.", "Es soporte local."], "Local"),
        ("Pedido sospechoso", "Una llamada de ejemplo dice ser «del soporte» y pide la contraseña a una usuaria. ¿Qué corresponde?", ["Ningún técnico real pide la contraseña.", "Se corta y se avisa a la jefatura."], "No entregarla y avisar a la jefatura"),
    ],
    mistakes=[("Pedir la contraseña de la usuaria «para entrar más rápido» a arreglar el problema.", "Quien conoce la contraseña puede actuar como la usuaria y se rompe la confianza.", "Usa tu propia cuenta autorizada o ayuda a la usuaria a cambiar la suya."),
              ("Conectarse a un equipo remotamente sin avisar a la usuaria.", "Se invade su privacidad y puede ser una falta grave.", "Pide permiso y registra la conexión en el ticket.")],
    T=[
        ("abc", "En Programación: ¿qué es un ticket de soporte?", "Un registro de un pedido de ayuda con su estado", "Una entrada para un evento", "Una copia de los datos de la usuaria", "El ticket ordena y deja constancia del pedido."),
        ("abc", "En Programación: ¿qué es el soporte remoto?", "Ayuda a través de la red sobre el equipo de la usuaria, con su permiso", "Ayuda sentado frente al equipo", "Ayuda sin que la usuaria lo sepa", "El soporte remoto se hace a distancia y con consentimiento."),
        ("abc", "¿Qué debe hacer el técnico antes de conectarse al equipo de una usuaria?", "Pedir su permiso y registrarlo en el ticket", "Conectarse sin avisar para ahorrar tiempo", "Pedir su contraseña por mensaje", "El consentimiento es obligatorio y queda registrado."),
        ("abc", "{F} ¿Cuál es el estado del ticket TK-01?", "abierto", "cerrado", "en espera de la jefatura", "El ticket está abierto: aún no se resuelve."),
        ("abc", "{F} Clara dice: «mi contraseña es esta, entra tú». ¿Qué responde el técnico según las reglas de la oficina?", "Que no la necesita y que usará su propia cuenta autorizada", "La anota para volver a usarla", "La comparte con sus colegas", "El técnico nunca recibe la contraseña de la usuaria."),
        ("abc", "{F} ¿Qué debe quedar anotado si el técnico se conecta de forma remota?", "La conexión, el permiso y lo que se hizo", "Solo el nombre del técnico", "La contraseña de la usuaria", "Todo se registra en el ticket."),
        ("=", "{F} El técnico resuelve 5 tickets por la mañana y 4 por la tarde. ¿Cuántos tickets resolvió en el día?", "5+4", "Se suman los tickets de ambos turnos.", " tickets"),
        ("abc", "Una persona llama diciendo ser «del soporte del banco» y pide a Clara que le diga su clave para «evitar un bloqueo». ¿Qué tipo de engaño es?", "Ingeniería social", "Mantención preventiva", "Respaldo", "El engaño busca obtener una clave haciéndose pasar por soporte."),
        ("abc", "{F} Mientras ayuda a Clara, el técnico ve en pantalla un documento con datos de clientes. ¿Qué corresponde?", "Mirar solo lo necesario, no copiar nada y respetar la confidencialidad", "Copiar el documento por si sirve", "Comentarlo con sus amigos", "Se respeta la privacidad de lo que se ve en pantalla."),
        ("abc", "{F} El técnico no puede solucionar el problema por teléfono. ¿Qué opción es válida?", "Pasar a soporte local o escalar el ticket, y registrarlo", "Cerrar el ticket como resuelto", "Pedir la contraseña por mensaje", "Si el remoto no basta, se atiende en el lugar o se escala."),
        ("=", "En un día de ejemplo la mesa de ayuda recibió 20 tickets: 12 locales y el resto remotos. ¿Cuántos fueron remotos?", "20-12", "Se resta lo local al total.", " tickets"),
        ("abc", "El técnico comparte en un grupo de mensajería una captura del correo de una usuaria «para pedir ayuda». ¿Qué falló?", "Compartió información privada sin permiso", "Atendió muy rápido", "Cerró el ticket antes de tiempo", "La captura expone datos de la usuaria."),
        ("ab", "{F} Clara pide terminar la conexión remota a mitad del trabajo. ¿Qué hace el técnico?", "Termina la conexión y lo anota en el ticket", "Continúa para no dejar el trabajo a medias", "La usuaria puede terminar la conexión cuando quiera y el técnico lo respeta."),
    ],
    ctx=("abc", "Un jefe de ejemplo pide al técnico mirar los correos de una trabajadora «por curiosidad», durante una atención remota. ¿Qué hace el técnico?", "Se niega: solo accede a lo necesario para el soporte y lo informa", "Acepta porque el jefe manda", "Copia los correos en un pendrive", "El soporte se limita a su fin y respeta la privacidad."),
    sc=[
        ("En Programación: ¿qué se anota en un ticket?", "Usuaria, problema, prioridad y estado", "Es el registro del pedido de ayuda."),
        ("¿El técnico pide la contraseña de la usuaria?", "No, nunca", "El técnico usa su propia cuenta autorizada."),
        ("¿Qué se hace antes de una conexión remota?", "Se pide permiso a la usuaria", "El consentimiento de la usuaria es obligatorio."),
    ],
    op=("En una clínica dental de ejemplo, la recepcionista Ana (nombre de ejemplo) pide ayuda porque no puede imprimir las citas. Escribe el ticket (número, usuaria, problema, prioridad, estado), indica si lo atenderías local o remoto y qué le dirías para pedir su permiso, y qué harías si Ana te ofrece su contraseña.",
        "Ticket TK-02, usuaria Ana, problema «no imprime las citas», prioridad media, estado abierto. Atención local o remota con su permiso: «¿Me autoriza a conectarme a su equipo? Puede terminar la conexión cuando quiera». Si ofrece su contraseña, le diría que no la necesito, que no se la debe dar a nadie y usaría mi cuenta autorizada.",
        ["escribe el ticket con sus cinco elementos", "pide permiso y menciona el registro", "rechaza la contraseña con una razón"],
        ["hoja con el ticket y la frase de permiso"],
        ["conectarse sin permiso", "anotar la contraseña", "no registrar la atención"],
        "Pregunta: «¿por qué no puedes aceptar su contraseña aunque ella la ofrezca?». Si no responde, pídele que piense qué pasaría si se filtra."),
    reinforce="Escribe tres datos que un ticket de soporte debe tener y uno que nunca debe tener.",
    extend="Explica con un ejemplo inventado cómo reconocerías un llamado falso de soporte.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 26 (documentos y niveles de ejemplo, inventados). Mesa de ayuda del «Colegio Los Alerces» (nombre de ejemplo). Nivel 1 (N1): recibe, registra y resuelve problemas simples con la base de conocimiento. "
     "Nivel 2 (N2): resuelve problemas técnicos más complejos. Nivel 3 (N3): especialistas o proveedor, para fallas de fondo. Escalar es pasar un ticket al nivel siguiente. "
     "Acuerdo de nivel de servicio (SLA) de ejemplo: respuesta inicial en 2 horas y solución en 8 horas para prioridad alta; respuesta en 4 horas y solución en 24 horas para prioridad media. "
     "Base de conocimiento (artículos de solución escritos): artículo A-01 «reiniciar la sesión de la impresora», artículo A-02 «recuperar acceso a una cuenta con el procedimiento oficial».")
build(
    O7, 2, F,
    use="Aprenderé los conceptos y documentos del soporte (niveles, escalamiento, SLA y base de conocimiento) y los roles de la mesa de ayuda.",
    prior=["Sé qué es un ticket y qué es soporte remoto.", "Sé que no se pide la contraseña.", "Sé comparar horas."],
    explain=[
        "La mesa de ayuda se organiza en niveles. El nivel 1 recibe y registra el pedido y resuelve lo simple, apoyándose en la base de conocimiento: artículos escritos con soluciones ya probadas. El nivel 2 atiende problemas técnicos más complejos y el nivel 3 reúne a especialistas o al proveedor del sistema. Escalar significa pasar el ticket al nivel siguiente, con todo lo ya probado anotado para no repetir pasos.",
        "El acuerdo de nivel de servicio (SLA) fija los tiempos máximos de respuesta y de solución según la prioridad. Sirve para saber si el servicio cumple lo prometido y para ordenar el trabajo: un ticket de prioridad alta se atiende antes. Los valores del SLA de esta ficha son de ejemplo; en una organización real los fija el acuerdo vigente.",
        "Los documentos de la mesa de ayuda son el ticket, la base de conocimiento, el SLA y el informe de cierre, donde la usuaria confirma que el problema se resolvió. Los roles son la analista de mesa de ayuda (N1), el técnico de soporte (N2), el especialista (N3) y la jefatura de TI. Quien resuelve explica a la usuaria lo que hizo con palabras claras, sin tecnicismos innecesarios.",
    ],
    vocab=[("nivel de soporte", "grupo que atiende según la complejidad del problema"), ("escalar", "pasar el ticket al nivel siguiente"), ("base de conocimiento", "conjunto de artículos con soluciones ya probadas"), ("SLA", "acuerdo con los tiempos máximos de respuesta y solución"), ("informe de cierre", "documento en que la usuaria confirma la solución"), ("tiempo de respuesta", "tiempo hasta la primera atención")],
    worked=[
        ("Elegir el nivel", "Una usuaria de ejemplo olvidó cómo reiniciar la sesión de la impresora y existe un artículo para eso. ¿Qué nivel lo resuelve?", ["Es un problema simple con solución escrita.", "Lo resuelve el nivel 1."], "Nivel 1"),
        ("Revisar el SLA", "Un ticket de prioridad alta se abrió a las 9:00 y recibió respuesta a las 10:30. Con el SLA de la ficha (2 horas), ¿se cumplió la respuesta?", ["De 9:00 a 10:30 pasaron 1 hora y 30 minutos.", "1 h 30 min es menos de 2 horas."], "Sí, se cumplió"),
    ],
    mistakes=[("Escalar un ticket sin anotar lo que ya se probó.", "El siguiente nivel repite pasos y se pierde tiempo.", "Anota lo realizado antes de escalar."),
              ("Cerrar un ticket cuando el técnico cree que quedó resuelto, sin que la usuaria lo confirme.", "El problema puede seguir y la usuaria queda sin ayuda.", "Pide su confirmación en el informe de cierre.")],
    T=[
        ("abc", "En Programación: ¿qué es escalar un ticket?", "Pasarlo al nivel siguiente de soporte", "Cerrarlo sin resolverlo", "Borrar el ticket", "Escalar significa derivar a quien puede resolverlo."),
        ("abc", "En Programación: ¿para qué sirve la base de conocimiento?", "Para encontrar soluciones ya probadas", "Para guardar contraseñas", "Para medir la velocidad de la red", "Reúne artículos con soluciones ya probadas."),
        ("abc", "En Programación: ¿qué fija un SLA?", "Los tiempos máximos de respuesta y de solución", "La contraseña de cada usuaria", "El precio de los equipos", "Define el servicio que se promete a las usuarias."),
        ("abc", "{F} ¿Qué nivel atiende primero un pedido de reiniciar la sesión de la impresora?", "Nivel 1", "Nivel 2", "Nivel 3", "Es un problema simple con artículo en la base de conocimiento."),
        ("abc", "{F} Una falla de fondo que solo puede resolver el proveedor, ¿a qué nivel llega?", "Nivel 3", "Nivel 1", "Nivel 2", "El nivel 3 reúne a especialistas o al proveedor."),
        ("=", "{F} Para prioridad alta, ¿cuántas horas máximas se dan en total para la solución?", "8", "Es el tiempo de solución que fija el SLA de la ficha.", " horas"),
        ("=", "{F} Un ticket de prioridad media se abre a las 9 y se resuelve 20 horas después. ¿Cuántas horas sobran respecto del SLA de solución?", "24-20", "Se resta el tiempo usado al tiempo máximo de 24 horas.", " horas"),
        ("abc", "{F} Un ticket de prioridad alta se resuelve en 10 horas. ¿Se cumplió la solución según el SLA?", "No, el máximo era de 8 horas", "Sí, porque 10 es mayor que 8", "Sí, porque la respuesta fue rápida", "El tiempo de solución superó el máximo permitido."),
        ("abc", "{F} Una usuaria dice que olvidó su clave. ¿Qué corresponde según el artículo A-02?", "Seguir el procedimiento oficial de recuperación sin que el técnico conozca la nueva clave", "Pedirle la clave antigua por mensaje", "Que el técnico invente una clave y la anote", "La recuperación oficial evita que el técnico conozca claves."),
        ("abc", "El técnico de N1 escala un ticket a N2 con el mensaje «no sirve» y nada más. ¿Qué falta?", "Los pasos ya probados y el resultado de cada uno", "El nombre completo de la usuaria y su teléfono personal", "La contraseña de la usuaria", "El siguiente nivel necesita saber qué ya se intentó."),
        ("=", "En un mes de ejemplo se resolvieron 50 tickets: 30 en N1, 15 en N2 y el resto en N3. ¿Cuántos se resolvieron en N3?", "50-30-15", "Se restan los de N1 y N2 al total.", " tickets"),
        ("abc", "{F} El técnico quiere cerrar un ticket que parece resuelto, pero la usuaria no ha respondido. ¿Qué conviene?", "Pedir su confirmación antes de cerrar", "Cerrarlo igual", "Dejarlo abierto sin avisarle", "El cierre se confirma con la usuaria."),
        ("ab", "{F} ¿Qué rol define las prioridades y aprueba los cambios en los procedimientos?", "La jefatura de TI", "La usuaria que reporta", "Las prioridades y los cambios de procedimiento los aprueba la jefatura de TI."),
    ],
    ctx=("abc", "Una usuaria de ejemplo está molesta porque su ticket lleva dos días sin respuesta. ¿Qué hace la analista de N1?", "Revisa el SLA, pide disculpas con claridad, informa el estado y escala si hace falta", "Le dice que espere sin explicar", "Cierra el ticket para que no aparezca atrasado", "Se informa con honestidad y se actúa según el SLA."),
    sc=[
        ("En Programación: ¿qué nivel resuelve los problemas simples?", "El nivel 1", "Se apoya en la base de conocimiento."),
        ("¿Qué se anota antes de escalar?", "Los pasos ya probados", "Así el siguiente nivel no repite pasos."),
        ("¿Cuándo se cierra un ticket?", "Cuando la usuaria confirma la solución", "El cierre se respalda con su confirmación."),
    ],
    op=("Con el SLA de la ficha (alta: respuesta 2 h y solución 8 h; media: respuesta 4 h y solución 24 h) revisa estos tickets de ejemplo: T1 alta, respondido a las 1 h 30 min y resuelto a las 9 h; T2 media, respondido a las 3 h y resuelto a las 20 h; T3 alta, respondido a las 3 h y resuelto a las 6 h. Indica cuáles cumplen respuesta y solución y qué harías con los que no cumplen.",
        "T1: respuesta cumple (1 h 30 min < 2 h), solución no cumple (9 h > 8 h). T2: ambas cumplen (3 h < 4 h y 20 h < 24 h). T3: respuesta no cumple (3 h > 2 h), solución cumple (6 h < 8 h). En T1 y T3 analizaría la causa del atraso, lo anotaría y lo informaría a la jefatura de TI.",
        ["compara cada tiempo con el SLA correcto", "clasifica bien los tres tickets", "propone una acción de mejora con registro"],
        ["tabla de tres tickets con respuesta, solución y conclusión"],
        ["usar el SLA de otra prioridad", "confundir respuesta con solución", "no proponer acción"],
        "Pregunta: «¿qué diferencia hay entre tiempo de respuesta y de solución?». Si no responde, pídele que lo explique con T3."),
    reinforce="Escribe un artículo de dos líneas para la base de conocimiento sobre cómo reiniciar un programa que no responde.",
    extend="Explica con un ejemplo inventado por qué anotar lo ya probado antes de escalar ahorra tiempo.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 27 (caso de ejemplo, inventado). Ticket TK-07 de «Estudio Jurídico Las Palmas» (nombre de ejemplo): la usuaria Rosa dice «no puedo imprimir». Información reunida: (1) otras personas sí imprimen en la misma impresora; "
     "(2) el computador de Rosa muestra «sin conexión a la red»; (3) el cable de red de Rosa está conectado al computador y al enchufe de pared; (4) el computador de Rosa funciona bien con otros programas; "
     "(5) la impresora tiene papel y tinta. Árbol de decisión de ejemplo: si la impresora funciona para otros, el problema está en el equipo de la usuaria o en su conexión; si el equipo no tiene red, se revisa la conexión.")
build(
    O7, 3, F,
    use="Aprenderé a diagnosticar un problema en papel, descartando causas con evidencia, y a comunicar la solución a la usuaria.",
    prior=["Sé qué es un ticket y los niveles de soporte.", "Sé leer una lista de datos.", "Sé explicar con palabras claras."],
    explain=[
        "Diagnosticar es encontrar la causa de un problema con método. Se reúne información (qué pasó, desde cuándo, qué cambió), se plantean causas posibles y se descartan una a una con evidencia, empezando por las más simples y probables. Cada prueba debe ser reversible y no poner en riesgo los datos de la usuaria. No se cambia más de una cosa a la vez, para saber qué resolvió el problema.",
        "Un árbol de decisión ayuda a ordenar el razonamiento: cada pregunta tiene respuestas que llevan a la siguiente. Por ejemplo, si otras personas sí imprimen, la impresora no es la causa; si el equipo de la usuaria muestra «sin conexión», se revisa la red. La evidencia sale de lo que se observa o se mide, no de suposiciones. Si un dato falta, se pregunta a la usuaria con respeto.",
        "Al terminar, el técnico comunica con palabras claras qué falló, qué hizo y qué debe hacer la usuaria para evitarlo, y lo anota en el ticket. Si el problema supera su nivel, escala con la información reunida. Si requiere abrir o cambiar algo físico del equipo, lo hace solo personal autorizado, con el equipo apagado y desconectado, según las normas de seguridad de la organización.",
    ],
    vocab=[("diagnóstico", "encontrar la causa de un problema con método"), ("evidencia", "dato observado o medido que respalda una conclusión"), ("descartar", "eliminar una causa porque la evidencia no la respalda"), ("causa probable", "explicación más posible según la evidencia"), ("árbol de decisión", "esquema de preguntas que lleva a una conclusión")],
    worked=[
        ("Descartar con evidencia", "En un caso de ejemplo, el computador no enciende pero las luces de la sala sí funcionan. ¿Se descarta que se haya cortado la luz de la sala?", ["Las luces funcionan: hay electricidad en la sala.", "Esa causa se descarta."], "Sí, se descarta el corte de luz"),
        ("Un cambio a la vez", "El técnico de ejemplo cambia el cable y reinicia el equipo a la vez. El problema se resuelve. ¿Qué se pierde?", ["No se sabe cuál de los dos cambios lo resolvió.", "Conviene cambiar una sola cosa por vez."], "No se sabe cuál cambio resolvió el problema"),
    ],
    mistakes=[("Suponer que la impresora está mala sin revisar si otras personas imprimen.", "Se pierde tiempo cambiando algo que funciona.", "Reúne evidencia antes de culpar a una pieza."),
              ("Explicar la solución con palabras técnicas que la usuaria no entiende.", "La usuaria no aprende a evitar el problema y puede sentirse incómoda.", "Explica con palabras claras y ejemplos.")],
    T=[
        ("abc", "En Programación: ¿qué es la evidencia en un diagnóstico?", "Un dato observado o medido que respalda una conclusión", "Una opinión sin dato", "La contraseña de la usuaria", "La evidencia sale de lo que se observa o se mide."),
        ("abc", "En Programación: ¿qué significa descartar una causa?", "Eliminarla porque la evidencia no la respalda", "Escribirla en el ticket", "Repetirla varias veces", "Descartar una causa se hace con evidencia observada."),
        ("abc", "¿Por qué se cambia una sola cosa a la vez al probar?", "Para saber qué resolvió el problema", "Para gastar más tiempo", "Para no escribir el ticket", "Si se cambian dos cosas, no se sabe cuál fue la solución."),
        ("abc", "{F} Dato (1): otras personas sí imprimen. ¿Qué causa se descarta?", "Que la impresora esté dañada", "Que el computador de Rosa esté bien", "Que Rosa no haya reportado", "Si otras personas imprimen, la impresora funciona."),
        ("abc", "{F} Dato (5): la impresora tiene papel y tinta. ¿Qué causa se descarta?", "La falta de papel o de tinta", "Un problema de red de Rosa", "Un problema del computador de Rosa", "El dato muestra que sí hay papel y tinta."),
        ("abc", "{F} Datos (2) y (3): el equipo de Rosa dice «sin conexión a la red» aunque el cable está conectado. ¿Qué conviene revisar después?", "La configuración de red del equipo y el enchufe de pared", "El papel de la impresora", "El color de la tinta", "El cable parece bien conectado, pero el equipo no tiene red."),
        ("abc", "{F} Dato (4): el computador funciona bien con otros programas. ¿Qué causa se descarta?", "Una falla general del computador", "Un problema de red", "Una desconexión del cable", "Si otros programas funcionan, el equipo en general está bien."),
        ("abc", "{F} Según el árbol de decisión, ¿dónde está probablemente el problema?", "En la conexión de red del equipo de Rosa", "En la impresora", "En el papel", "Otras personas imprimen y el equipo de Rosa no tiene red."),
        ("=", "{F} El técnico dedica 6 minutos a revisar cada una de las cinco informaciones reunidas. ¿Cuántos minutos son en total?", "6*5", "Se multiplican los minutos por la cantidad de informaciones.", " minutos"),
        ("abc", "{F} El técnico prueba el enchufe de pared con otro equipo de ejemplo y funciona. ¿Qué concluye?", "El enchufe de pared está bien y se revisa la configuración del equipo de Rosa", "El enchufe está malo", "La impresora está mala", "Si otro equipo se conecta en el mismo enchufe, el enchufe funciona."),
        ("abc", "Para revisar un equipo por dentro, un técnico de ejemplo quiere abrirlo mientras está encendido. ¿Qué corresponde?", "No: lo hace solo personal autorizado, con el equipo apagado y desconectado", "Sí, porque así ve mejor", "Sí, si usa una herramienta pequeña", "Abrir un equipo exige personal autorizado, equipo apagado y desconectado."),
        ("=", "Rosa pierde 15 minutos de trabajo cada vez que falla la red, y hoy falló 3 veces. ¿Cuántos minutos perdió?", "15*3", "Se multiplican los minutos por las veces.", " minutos"),
        ("ab", "{F} Rosa pregunta por qué falló la red. ¿Qué explicación es mejor?", "«El equipo no encontraba la red; ya lo configuramos de nuevo»", "«Un problema de capa de enlace con el DHCP»", "Una explicación con palabras claras ayuda a la usuaria a entender y evitar el problema."),
    ],
    ctx=("abc", "Una usuaria de ejemplo se frustra y dice: «ustedes no sirven». ¿Cuál es la respuesta profesional del técnico?", "Escucha, reconoce el problema, explica los pasos y mantiene un trato respetuoso", "Discute con ella", "Cierra el ticket sin hablar", "La comunicación respetuosa es parte del soporte."),
    sc=[
        ("En Programación: ¿qué se hace primero al diagnosticar?", "Reunir información y descartar las causas simples con evidencia", "Así se avanza de lo simple a lo complejo."),
        ("¿Cuántas cosas se cambian a la vez en una prueba?", "Una sola", "Así se sabe qué resolvió el problema."),
        ("¿Cómo se explica la solución a la usuaria?", "Con palabras claras", "La usuaria debe entender qué pasó."),
    ],
    op=("Ticket de ejemplo: un profesor del taller dice «no puedo entrar al programa de notas». Datos: (1) otros profesores sí entran; (2) su cuenta aparece como bloqueada por intentos fallidos; (3) su computador abre otros programas sin problema; (4) la red funciona. Descarta causas con evidencia, indica la causa probable, qué harías sin pedirle su contraseña y cómo se lo explicarías en dos líneas.",
        "Se descarta falla general del programa (1), del computador (3) y de la red (4). Causa probable: cuenta bloqueada por intentos fallidos (2). Sin pedir su contraseña, seguiría el procedimiento oficial de desbloqueo y recuperación para que él defina una nueva. Explicación: «Su cuenta se bloqueó por intentos fallidos; ya la desbloqueamos y usted elige una clave nueva».",
        ["descarta causas con evidencia", "identifica la causa probable y una acción sin pedir clave", "explica con palabras claras"],
        ["hoja con el razonamiento y las dos líneas de explicación"],
        ["culpar al programa sin evidencia", "pedir la contraseña", "explicar con tecnicismos"],
        "Pregunta: «¿qué dato te permite descartar una falla general del programa?». Si no responde, pídele que relea el dato (1)."),
    reinforce="Escribe tres datos que descartarían que un televisor de ejemplo no enciende por falta de luz en la casa.",
    extend="Explica con un ejemplo inventado por qué una suposición sin evidencia puede alargar la solución de un problema.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 28 (datos de ejemplo, inventados) de la mesa de ayuda del «Instituto Los Notros». Tickets pendientes: T1 (impacto 3, urgencia 3, afecta a toda la secretaría); T2 (impacto 1, urgencia 2, un cambio de fondo de pantalla); "
     "T3 (impacto 2, urgencia 3, un profesor sin acceso antes de una clase). Prioridad = impacto × urgencia (1 a 3). Cumplimiento del SLA de ejemplo en el mes: de 40 tickets, 34 se resolvieron dentro del plazo. "
     "Encuesta de satisfacción de ejemplo: de 20 usuarias que respondieron, 17 dijeron estar conformes. Mensaje sospechoso de ejemplo: «Soporte TI: envíe su contraseña para evitar el cierre de su cuenta».")
build(
    O7, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: priorizar tickets, medir el cumplimiento del servicio y responder con seguridad a pedidos riesgosos.",
    prior=["Sé qué es un SLA y qué es un ticket.", "Sé calcular porcentajes simples.", "Sé qué es la ingeniería social."],
    explain=[
        "El criterio técnico del soporte combina prioridad, medición y seguridad. La prioridad de un ticket se calcula como impacto por urgencia; los tickets se atienden de mayor a menor prioridad, y si dos empatan se desempata con un criterio escrito, como el riesgo para la seguridad de los datos o la cantidad de personas afectadas.",
        "Para saber si el servicio es bueno se miden indicadores. El porcentaje de cumplimiento del SLA es los tickets resueltos dentro del plazo dividido por el total, por cien. La satisfacción es el porcentaje de usuarias conformes entre las que respondieron. Se interpretan con prudencia: una encuesta con pocas respuestas muestra una pista, no una verdad definitiva.",
        "Un mensaje que pide enviar la contraseña es una señal de engaño (phishing, un mensaje falso que busca claves). Nunca se responde con datos: se reporta a la jefatura de TI y se avisa a las demás personas. El técnico deja constancia de cada decisión y no comparte datos personales de las usuarias en los informes.",
    ],
    vocab=[("prioridad", "impacto por urgencia"), ("indicador", "cifra que mide si el servicio mejora"), ("cumplimiento del SLA", "porcentaje de tickets resueltos dentro del plazo"), ("satisfacción", "porcentaje de usuarias conformes entre las que respondieron"), ("phishing", "mensaje falso que busca obtener claves o datos")],
    worked=[
        ("Calcular el cumplimiento", "En un mes de ejemplo, de 50 tickets se resolvieron 45 dentro del plazo. ¿Cuál es el cumplimiento del SLA?", ["45 ÷ 50 = 0,9.", "0,9 × 100 = 90."], "90 %"),
        ("Reconocer phishing", "Un correo de ejemplo dice: «haga clic y escriba su clave para no perder su cuenta». ¿Qué se hace?", ["Pide una clave por un enlace: es una señal de engaño.", "Se reporta a la jefatura de TI y no se hace clic."], "Reportarlo y no hacer clic"),
    ],
    mistakes=[("Atender primero el ticket de la persona más insistente sin calcular la prioridad.", "El ticket más urgente para la organización puede quedar esperando.", "Calcula impacto por urgencia y desempata con un criterio escrito."),
              ("Responder el mensaje sospechoso «para comprobar si era real».", "Se confirma que la cuenta existe y se puede perder información.", "No respondas; repórtalo a la jefatura de TI.")],
    T=[
        ("abc", "En Programación: ¿qué es el phishing?", "Un mensaje falso que busca obtener claves o datos", "Una copia de seguridad", "Un nivel de soporte", "Se hace pasar por una entidad confiable para engañar."),
        ("abc", "¿Cómo se calcula la prioridad de un ticket?", "Impacto × urgencia", "Impacto + días", "Urgencia − impacto", "La ficha define la prioridad con ese producto."),
        ("=", "{F} ¿Cuál es la prioridad de T1?", "3*3", "Se multiplica impacto por urgencia.", ""),
        ("=", "{F} ¿Cuál es la prioridad de T3?", "2*3", "Se multiplica impacto por urgencia.", ""),
        ("abc", "{F} ¿Qué ticket se atiende último?", "T2", "T1", "T3", "T2 tiene prioridad 2 y es la más baja."),
        ("abc", "{F} ¿Cuál es el orden de atención de mayor a menor prioridad?", "T1, T3, T2", "T3, T1, T2", "T2, T3, T1", "Las prioridades son 9, 6 y 2."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento del SLA tuvo la mesa de ayuda en el mes?", "34*100//40", "Se divide los tickets en plazo por el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos tickets del mes se resolvieron fuera del plazo?", "40-34", "Se resta lo cumplido al total.", " tickets"),
        ("=", "{F} ¿Qué porcentaje de las usuarias que respondieron la encuesta está conforme?", "17*100//20", "Se divide las conformes por las que respondieron y se multiplica por 100.", " %"),
        ("abc", "{F} Un jefe dice: «con 85 % de conformes el servicio es perfecto». ¿Cuál es una conclusión prudente?", "Es una buena señal, pero respondieron pocas personas y hay que seguir midiendo", "Es una prueba definitiva de perfección", "No dice nada del servicio", "Una encuesta de pocas respuestas es una pista, no una conclusión definitiva."),
        ("abc", "{F} ¿Qué debe hacer la usuaria que recibe el mensaje «Soporte TI: envíe su contraseña…»?", "No responder y avisar a la jefatura de TI", "Enviar la clave rápidamente", "Reenviar el mensaje a sus amistades", "Ningún soporte real pide la contraseña por mensaje."),
        ("abc", "El técnico quiere subir el cumplimiento del SLA y propone cerrar tickets sin que la usuaria confirme. ¿Qué problema tiene?", "El indicador mejora pero el servicio no, y se pierde la confianza", "Ninguno, es válido", "Que habrá menos tickets", "Un indicador no puede manipularse; debe reflejar el servicio real."),
        ("abc", "{F} El informe mensual incluye el nombre completo de cada usuaria que se quejó. ¿Qué corresponde?", "Presentar los datos agregados sin nombres", "Publicar los nombres", "Enviar los nombres a todo el instituto", "Los informes protegen los datos personales."),
    ],
    ctx=("abc", "Un directivo de ejemplo pide pasar primero el ticket de su hijo, que es un cambio de fondo de pantalla, antes que el de la secretaría. ¿Qué responde la jefatura de TI?", "Aplica el criterio de prioridad escrito y explica la razón con respeto", "Acepta para evitar problemas", "Cierra ambos tickets", "La prioridad se aplica con un criterio común."),
    sc=[
        ("En Programación: ¿cómo se calcula el cumplimiento del SLA?", "Tickets en plazo dividido por el total, por cien", "El resultado se expresa como un porcentaje."),
        ("¿Qué haces con un mensaje que pide tu contraseña?", "No respondo y lo reporto a la jefatura de TI", "Es una señal clara de engaño."),
        ("¿Cómo se desempata entre dos tickets de igual prioridad?", "Con un criterio escrito", "Así la decisión es justa y comprobable."),
    ],
    op=("Un colegio de ejemplo tiene tickets pendientes: A (impacto 2, urgencia 2), B (impacto 3, urgencia 2), C (impacto 1, urgencia 3). Calcula la prioridad y el orden de atención. En el mes se resolvieron 27 de 30 tickets dentro del plazo: calcula el cumplimiento. Además llegó el mensaje «Soporte: envíe su contraseña ahora». Escribe qué harías y una conclusión prudente con un límite.",
        "Prioridades: A = 4, B = 6, C = 3; orden B, A, C. Cumplimiento: 27 ÷ 30 × 100 = 90 %. Sobre el mensaje: no respondería, lo reportaría a la jefatura de TI y avisaría al resto de las usuarias. Conclusión: el 90 % es una buena señal; el límite es que un solo mes no muestra una tendencia.",
        ["calcula las prioridades y el orden", "calcula el porcentaje de cumplimiento", "responde con seguridad al mensaje sospechoso y declara un límite"],
        ["hoja con la tabla de prioridades, el porcentaje y la respuesta al mensaje"],
        ["sumar en vez de multiplicar", "responder el mensaje", "no declarar un límite"],
        "Pregunta: «¿qué ticket va primero y por qué?». Si no responde, pídele que lea de nuevo las prioridades."),
    reinforce="Inventa tres tickets con impacto y urgencia y calcula su prioridad.",
    extend="Explica con un ejemplo inventado por qué un indicador bueno no siempre significa que todas las usuarias están conformes.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 29 (caso de ejemplo, inventado). La «Clínica Veterinaria Pelusa» (nombre de ejemplo) tiene 5 computadores antiguos y quiere mejorar su rendimiento. Hardware es la parte física (procesador, memoria, almacenamiento); software es la parte lógica (programas y sistema operativo). "
     "Datos de ejemplo del equipo 1: memoria 4 GB, almacenamiento 250 GB con 240 GB usados, programa de gestión de pacientes que se pone lento. Reglas de la clínica de ejemplo: toda instalación o actualización la hace solo personal autorizado, con respaldo previo, equipo apagado y desconectado si se toca el hardware, y se anota en la bitácora.")
build(
    O8, 1, F,
    use="Aprenderé qué es instalar y actualizar hardware y software, para qué se hace y qué cuidados de seguridad y de registro se exigen.",
    prior=["Sé qué es un computador y un programa.", "Sé qué es un respaldo.", "Sé qué es una bitácora."],
    explain=[
        "Un computador tiene hardware, la parte física, y software, la parte lógica. Entre el hardware están el procesador (que hace los cálculos), la memoria RAM (donde trabaja el equipo mientras está en uso) y el almacenamiento (donde se guardan programas y archivos). El software incluye el sistema operativo y los programas. Instalar es dejar algo funcionando por primera vez; actualizar es cambiarlo por una versión más nueva o mejorarlo.",
        "Se actualiza para mejorar el rendimiento (que el equipo trabaje más rápido) o para corregir errores típicos, como fallas ya conocidas o agujeros de seguridad. Antes de actualizar se revisa la compatibilidad: que la pieza o la versión nueva funcione con el resto del equipo. Un cambio mal elegido puede dejar el equipo igual de lento o inutilizable.",
        "Hay normas de seguridad. Lo que implica abrir o tocar el interior de un equipo lo hace solo personal autorizado y capacitado, con el equipo apagado y desconectado, siguiendo las instrucciones del fabricante y la norma vigente de la organización. Los datos se respaldan antes de cualquier cambio. Los equipos en desuso y las piezas retiradas se tratan como residuos electrónicos según la norma vigente. Este cuaderno es solo conceptual y no te habilita para intervenir equipos.",
    ],
    vocab=[("hardware", "parte física de un computador"), ("software", "parte lógica: sistema operativo y programas"), ("memoria RAM", "espacio de trabajo del equipo mientras está en uso"), ("almacenamiento", "espacio donde se guardan programas y archivos"), ("actualizar", "cambiar a una versión más nueva o mejorar"), ("compatibilidad", "que una pieza o versión funcione con el resto del equipo"), ("residuo electrónico", "equipo o pieza en desuso que se maneja según la norma")],
    worked=[
        ("Hardware o software", "En un caso de ejemplo se cambia la memoria RAM de un equipo y se instala una versión nueva de un programa de facturas. ¿Cuál es hardware y cuál es software?", ["La memoria es una pieza física.", "El programa de facturas es lógico."], "La memoria es hardware; el programa es software"),
        ("Espacio libre", "Un equipo de ejemplo tiene almacenamiento de 500 GB con 460 GB usados. ¿Cuánto espacio libre queda?", ["Libre = total menos usado.", "500 − 460."], "40 GB"),
    ],
    mistakes=[("Abrir un equipo encendido «solo para mirar».", "Es un riesgo para la persona y para el equipo.", "El interior lo revisa solo personal autorizado, con el equipo apagado y desconectado."),
              ("Actualizar un programa en horario de trabajo sin respaldo.", "Si falla, las usuarias quedan sin servicio y se pueden perder datos.", "Haz el respaldo y planifica la actualización fuera del horario de trabajo.")],
    T=[
        ("abc", "En Programación: ¿qué es el hardware?", "La parte física de un computador", "Los programas instalados", "Los archivos del usuario", "El hardware se puede tocar; el software no."),
        ("abc", "En Programación: ¿qué es la memoria RAM?", "El espacio de trabajo del equipo mientras está en uso", "El lugar donde se guardan los archivos para siempre", "El programa de gestión", "La RAM se usa mientras el equipo está encendido."),
        ("abc", "En Programación: ¿qué es la compatibilidad?", "Que una pieza o versión funcione con el resto del equipo", "Que la pieza sea la más cara", "Que el equipo sea nuevo", "Sin compatibilidad, el cambio puede no funcionar."),
        ("=", "{F} ¿Cuántos GB libres tiene el almacenamiento del equipo 1?", "250-240", "Se resta lo usado al total.", " GB"),
        ("abc", "{F} El programa de gestión se pone lento y el almacenamiento está casi lleno. ¿Qué dato de la ficha es una pista de la causa?", "Quedan solo 10 GB libres de 250 GB", "El equipo tiene 5 computadores", "El programa es de pacientes", "Poco espacio libre puede ralentizar el equipo."),
        ("abc", "{F} ¿Qué regla de la clínica se aplica antes de actualizar un programa?", "Hacer un respaldo previo", "Instalar sin avisar", "Quitar la bitácora", "La regla de la ficha pide respaldo previo."),
        ("abc", "{F} Una auxiliar quiere abrir el computador para limpiarlo. ¿Qué corresponde según las reglas?", "Avisar al personal autorizado, que lo hace con el equipo apagado y desconectado", "Abrirlo ella con el equipo encendido", "Prestarlo a un amigo", "Solo el personal autorizado interviene el hardware."),
        ("abc", "¿Qué motivo justifica actualizar un programa?", "Corregir errores conocidos o agujeros de seguridad", "Cambiar el color del escritorio por gusto", "Que se vea moderno", "Las actualizaciones corrigen errores y mejoran la seguridad."),
        ("=", "{F} Si la clínica compra una memoria adicional de 4 GB para cada uno de los 5 computadores, ¿cuántos GB compra en total?", "5*4", "Se multiplican los equipos por los GB de cada uno.", " GB"),
        ("abc", "Un equipo de ejemplo fue reemplazado y el técnico lo arroja a la basura común. ¿Qué corresponde?", "Manejarlo como residuo electrónico según la norma vigente", "Tirarlo, no pasa nada", "Dejarlo en la calle", "Los equipos en desuso se manejan según la norma de residuos electrónicos."),
        ("abc", "{F} El técnico actualiza el equipo 1 y no anota nada. Dos semanas después aparece una falla. ¿Qué dificultad aparece?", "No hay registro de qué cambió ni quién lo hizo", "Hay demasiado espacio libre", "La falla desaparece sola", "La bitácora permite ubicar el cambio que originó la falla."),
        ("=", "{F} Si se libera la mitad de los 240 GB usados del equipo 1, ¿cuántos GB quedarían libres?", "10+240//2", "Libres originales más los liberados.", " GB"),
        ("ab", "{F} Un técnico de ejemplo compra una memoria sin revisar si es compatible con el equipo. ¿Qué puede ocurrir?", "Que no funcione y se pierda dinero y tiempo", "Nada, toda memoria sirve en todos los equipos", "Sin compatibilidad una pieza puede no funcionar con el equipo."),
    ],
    ctx=("abc", "El dueño de una clínica de ejemplo pide a su sobrino, que «sabe de computadores», abrir el equipo y cambiar piezas el viernes por la tarde. ¿Qué recomienda la persona encargada de TI?", "Que lo haga personal autorizado, con respaldo y registro", "Que lo haga el sobrino sin respaldo", "Que se deje así para siempre", "Las intervenciones físicas las hace personal autorizado y con respaldo."),
    sc=[
        ("En Programación: ¿qué diferencia hay entre hardware y software?", "El hardware es físico y el software es lógico", "Uno se toca; el otro son programas."),
        ("¿Qué se hace antes de actualizar?", "Respaldo, revisión de compatibilidad y autorización", "Así se evitan pérdidas de datos."),
        ("¿Quién interviene el interior de un equipo?", "Personal autorizado, con el equipo apagado y desconectado", "Es una regla de seguridad de la organización."),
    ],
    op=("Una escuela de ejemplo tiene un equipo con 4 GB de memoria y 100 GB de almacenamiento con 95 GB usados; los profesores dicen que «va lento». Lista tres causas posibles que revisarías, qué dos datos pedirías antes de decidir, qué regla de seguridad aplicarías si hay que tocar el hardware y qué dejarías anotado en la bitácora. Esto es solo conceptual.",
        "Causas posibles: poco espacio libre (5 GB), poca memoria RAM para los programas que usa y un programa que consume demasiados recursos. Pediría los programas que más se usan y los requisitos del programa. Si hay que tocar el hardware, lo haría personal autorizado, con respaldo y el equipo apagado y desconectado. En la bitácora: qué se revisó o cambió, quién y cuándo.",
        ["nombra tres causas posibles con los datos de la ficha", "pide información antes de decidir", "aplica seguridad, respaldo y registro"],
        ["hoja con las tres causas, dos preguntas y las reglas"],
        ["abrir el equipo sin autorización", "decidir sin datos", "no hacer respaldo ni registro"],
        "Pregunta: «¿qué dato te dice que el almacenamiento está casi lleno?». Si no responde, pídele que haga la resta."),
    reinforce="Escribe en una tabla tres ejemplos de hardware y tres de software que conozcas.",
    extend="Explica con un ejemplo inventado por qué una actualización de software puede ser más importante que cambiar una pieza.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 30 (documentos de ejemplo, inventados). Inventario de equipos de la «Biblioteca Municipal Los Arrayanes» (nombre de ejemplo): equipo INV-01, memoria 4 GB, almacenamiento 250 GB, sistema operativo versión 10; equipo INV-02, memoria 8 GB, almacenamiento 500 GB, versión 11. "
     "Documentos: inventario (lista de equipos y sus características), orden de trabajo (pedido de instalar o actualizar con responsable y fecha), plan de actualización, acta de entrega y bitácora. "
     "Conceptos: controlador (driver, programa que permite al sistema usar una pieza), firmware (programa interno de una pieza), parche (corrección de un error o de seguridad) y versión.")
build(
    O8, 2, F,
    use="Aprenderé los conceptos de la actualización de equipos (controlador, firmware, parche y versión), los documentos y los roles.",
    prior=["Sé qué es hardware, software y compatibilidad.", "Sé qué es una bitácora.", "Sé qué es una versión."],
    explain=[
        "Para mantener los equipos actualizados se usan algunos conceptos. Un controlador (driver) es un programa que permite que el sistema operativo use una pieza, como una impresora. El firmware es el programa interno de una pieza. Un parche es una corrección que el fabricante publica para arreglar un error o un problema de seguridad. La versión es el número que identifica el estado de un programa; una versión nueva suele traer mejoras y correcciones.",
        "El trabajo se apoya en documentos. El inventario lista cada equipo y sus características, para saber qué hay y qué falta. La orden de trabajo pide una instalación o actualización con responsable y fecha. El plan de actualización define el orden, el horario y el plan de reversa, y el acta de entrega deja constancia de que el equipo quedó funcionando y fue recibido por la usuaria o la jefatura.",
        "Los roles se reparten: la usuaria o jefatura pide y autoriza, el técnico ejecuta, quien administra el inventario lo mantiene al día y la jefatura de TI aprueba el plan. Las actualizaciones se descargan solo del sitio oficial del fabricante o desde el canal que indique la organización, para evitar programas falsos que traen amenazas. No se actualiza un equipo en uso sin avisar.",
    ],
    vocab=[("controlador (driver)", "programa que permite al sistema usar una pieza"), ("firmware", "programa interno de una pieza"), ("parche", "corrección de un error o de seguridad"), ("inventario", "lista de equipos y sus características"), ("orden de trabajo", "pedido de instalar o actualizar con responsable y fecha"), ("acta de entrega", "documento que deja constancia de que el equipo quedó funcionando")],
    worked=[
        ("Leer el inventario", "Inventario de ejemplo: equipo A, 8 GB de memoria; equipo B, 4 GB. El programa nuevo pide 6 GB. ¿Qué equipo cumple?", ["Se compara cada memoria con 6 GB.", "8 es mayor o igual que 6; 4 no."], "El equipo A"),
        ("Elegir el documento", "El técnico necesita dejar constancia de que el computador quedó funcionando y la usuaria lo recibió. ¿Qué documento usa?", ["Es un documento de cierre y recepción.", "Es el acta de entrega."], "El acta de entrega"),
    ],
    mistakes=[("Descargar un controlador desde un sitio cualquiera porque «salió primero en la búsqueda».", "Puede ser un programa falso con amenazas.", "Usa solo el sitio oficial del fabricante o el canal de la organización."),
              ("Dar por cerrada una actualización sin acta de entrega ni bitácora.", "No hay constancia de lo hecho ni de quién lo recibió.", "Completa los documentos al terminar.")],
    T=[
        ("abc", "En Programación: ¿qué es un controlador (driver)?", "Un programa que permite al sistema usar una pieza", "La pieza física del computador", "Una clave de acceso", "El controlador conecta el sistema operativo con la pieza."),
        ("abc", "En Programación: ¿qué es un parche?", "Una corrección de un error o de seguridad", "Una pieza nueva de hardware", "Un respaldo", "El fabricante publica parches para arreglar problemas."),
        ("abc", "¿Para qué sirve el inventario de equipos?", "Para saber qué equipos hay y cómo son", "Para guardar contraseñas", "Para medir la velocidad de internet", "Lista los equipos y sus características."),
        ("abc", "{F} ¿Qué equipo del inventario tiene más memoria?", "INV-02", "INV-01", "Ambos tienen igual", "INV-02 tiene 8 GB y INV-01 tiene 4 GB."),
        ("=", "{F} ¿Cuántos GB de memoria suman los dos equipos?", "4+8", "Se suma la memoria de INV-01 y de INV-02.", " GB"),
        ("abc", "{F} Un programa nuevo pide 6 GB de memoria. ¿Qué equipo cumple ese requisito?", "INV-02", "INV-01", "Ambos", "Solo INV-02 tiene 6 GB o más."),
        ("abc", "{F} ¿Qué documento define el orden, el horario y el plan de reversa de una actualización?", "El plan de actualización", "El acta de entrega", "El inventario", "El plan organiza cómo se hará la actualización."),
        ("abc", "{F} ¿Qué documento deja constancia de que el equipo quedó funcionando y fue recibido?", "El acta de entrega", "La orden de trabajo", "El inventario", "El acta se firma al terminar."),
        ("abc", "{F} Una orden de trabajo pide actualizar INV-01 a la versión 11 del sistema operativo. ¿Qué debe revisarse antes?", "Que el equipo cumpla los requisitos de la versión 11 y hacer un respaldo", "Que el equipo tenga un fondo de pantalla bonito", "Que la usuaria no se entere", "Se revisa compatibilidad y se respalda."),
        ("=", "Un técnico de ejemplo actualiza 3 equipos por hora. ¿Cuántos equipos actualiza en 4 horas?", "3*4", "Se multiplican los equipos por hora por las horas.", " equipos"),
        ("abc", "Un correo dice: «descargue este parche urgente desde este enlace». ¿Qué corresponde?", "Verificar en el sitio oficial del fabricante o con la jefatura de TI", "Descargarlo de inmediato", "Reenviarlo a todos", "Los parches se obtienen de canales oficiales."),
        ("abc", "{F} El técnico actualiza INV-02 en plena atención al público sin avisar. ¿Cuál es el problema?", "Interrumpe el servicio sin avisar ni planificar", "Es la mejor hora para actualizar", "No hay problema", "Las actualizaciones se planifican y se avisa a las usuarias."),
        ("ab", "{F} ¿Quién aprueba el plan de actualización?", "La jefatura de TI", "La usuaria sola sin nadie más", "El plan lo aprueba la jefatura de TI, que responde por el servicio."),
    ],
    ctx=("abc", "El técnico de una biblioteca de ejemplo ve que el inventario no coincide con los equipos que hay en las salas. ¿Qué hace?", "Actualiza el inventario y deja constancia de las diferencias en la bitácora", "No toca nada y lo ignora", "Borra los equipos que no encuentra", "Un inventario al día evita errores y compras innecesarias."),
    sc=[
        ("En Programación: ¿qué es un parche?", "Una corrección de un error o de seguridad", "Se obtiene solo del canal oficial."),
        ("¿Qué documento pide la actualización con responsable y fecha?", "La orden de trabajo", "Deja claro quién lo hace y cuándo."),
        ("¿De dónde se descarga una actualización?", "Del sitio oficial del fabricante o del canal indicado", "Así se evitan programas falsos con amenazas."),
    ],
    op=("Inventario de ejemplo de un jardín infantil: equipo 1 (memoria 2 GB, versión 10), equipo 2 (memoria 8 GB, versión 10), equipo 3 (memoria 4 GB, versión 11). Un programa nuevo pide 4 GB de memoria y la versión 10 o superior. Indica qué equipos cumplen, qué documentos usarías para planificar y cerrar la actualización, y cómo asegurarías que el parche es auténtico.",
        "Cumplen los equipos 2 y 3 (memoria suficiente y versión 10 o mayor); el equipo 1 no cumple por memoria. Usaría el plan de actualización y la orden de trabajo para planificar y el acta de entrega y la bitácora para cerrar. El parche se obtiene del sitio oficial del fabricante o del canal de la organización.",
        ["compara cada equipo con ambos requisitos", "nombra documentos de inicio y de cierre", "indica la fuente oficial del parche"],
        ["tabla con los tres equipos y el cumplimiento"],
        ["mirar solo la memoria", "olvidar el acta de entrega", "descargar de cualquier sitio"],
        "Pregunta: «¿por qué el equipo 1 no cumple?». Si no responde, pídele que revise cada requisito."),
    reinforce="Escribe tres columnas de un inventario de equipos y llénalas con dos equipos de ejemplo.",
    extend="Explica con un ejemplo inventado por qué un inventario desactualizado puede causar compras innecesarias.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 31 (caso de ejemplo, inventado). Informe de síntomas de tres equipos de la «Oficina de Turismo Los Volcanes» (nombre de ejemplo). "
     "Equipo X: «se pone muy lento cuando abro varios programas a la vez»; memoria 4 GB, 60 % de la memoria en uso al abrir un solo programa. "
     "Equipo Y: «no me deja guardar más archivos»; almacenamiento de 120 GB con 118 GB usados. "
     "Equipo Z: «la impresora nueva no funciona»; el sistema no tiene el controlador de esa impresora. "
     "Opciones de mejora: (1) aumentar la memoria RAM; (2) liberar espacio o ampliar el almacenamiento; (3) instalar el controlador del fabricante.")
build(
    O8, 3, F,
    use="Aprenderé a relacionar un síntoma con la mejora adecuada de hardware o software y a justificarla con datos de un caso en papel.",
    prior=["Sé qué son memoria RAM, almacenamiento y controlador.", "Sé calcular porcentajes simples.", "Sé qué es la compatibilidad."],
    explain=[
        "Elegir una actualización es relacionar el síntoma con su causa más probable, usando datos. Un equipo que se pone lento cuando se abren varios programas a la vez suele tener poca memoria RAM: no alcanza el espacio de trabajo y el equipo se arrastra. Un equipo que no deja guardar archivos tiene el almacenamiento casi lleno. Una pieza nueva que no funciona suele necesitar su controlador.",
        "El análisis se hace con números: el porcentaje de memoria usada es la memoria en uso dividida por la memoria total, por cien, y el espacio libre es el total menos el usado. También se piensa en el costo y en el riesgo de cada opción, y se elige la que resuelve la causa con el menor cambio. Antes de cualquier cambio se hace un respaldo y se anota en la bitácora.",
        "No toda lentitud se arregla con hardware: a veces basta liberar espacio, cerrar programas innecesarios o actualizar un programa. Por eso se prueban primero las opciones más simples y reversibles. Y no se instala ningún software sin licencia o de origen dudoso para «ahorrar», porque compromete la seguridad de la organización.",
    ],
    vocab=[("síntoma", "señal que muestra que algo falla"), ("causa probable", "explicación más posible según los datos"), ("porcentaje de uso", "parte usada dividida por el total, por cien"), ("reversible", "que se puede deshacer"), ("liberar espacio", "borrar o mover archivos que ya no se necesitan, con respaldo")],
    worked=[
        ("Relacionar síntoma y mejora", "Un equipo de ejemplo se pone lento al abrir muchos programas y tiene poca memoria RAM. ¿Qué mejora corresponde?", ["El síntoma coincide con poca memoria.", "La mejora es aumentar la memoria RAM."], "Aumentar la memoria RAM"),
        ("Calcular el porcentaje", "Un equipo de ejemplo usa 3 GB de 4 GB de memoria. ¿Qué porcentaje usa?", ["3 ÷ 4 = 0,75.", "0,75 × 100."], "75 %"),
    ],
    mistakes=[("Comprar piezas nuevas sin revisar primero qué consume la memoria o el espacio.", "Se gasta dinero y el problema puede ser un programa o archivos innecesarios.", "Prueba primero las opciones simples y reversibles."),
              ("Borrar archivos del equipo para liberar espacio sin respaldo ni permiso.", "Se pueden perder datos de trabajo.", "Respalda y consulta antes de borrar.")],
    T=[
        ("abc", "En Programación: ¿qué es un síntoma?", "Una señal que muestra que algo falla", "La causa exacta del problema", "Una pieza de hardware", "El síntoma es lo que se ve; la causa se investiga."),
        ("abc", "En Programación: ¿qué significa que una mejora sea reversible?", "Que se puede deshacer", "Que cuesta mucho", "Que no necesita respaldo", "Las opciones reversibles reducen el riesgo."),
        ("abc", "{F} Equipo X, lento al abrir varios programas a la vez: ¿cuál es la opción más probable?", "(1) aumentar la memoria RAM", "(2) liberar espacio", "(3) instalar un controlador", "Poca memoria produce lentitud con varios programas abiertos."),
        ("abc", "{F} Equipo Y, no deja guardar archivos: ¿qué opción corresponde?", "(2) liberar espacio o ampliar el almacenamiento", "(1) aumentar la memoria RAM", "(3) instalar un controlador", "El almacenamiento de ese equipo está casi lleno."),
        ("abc", "{F} Equipo Z, la impresora nueva no funciona: ¿qué opción corresponde?", "(3) instalar el controlador del fabricante", "(1) aumentar la memoria RAM", "(2) ampliar el almacenamiento", "El sistema no tiene el controlador de la impresora."),
        ("=", "{F} ¿Cuántos GB libres tiene el equipo Y?", "120-118", "Se resta lo usado al total.", " GB"),
        ("=", "Un equipo de ejemplo tiene 8 GB de memoria y usa el 50 % al abrir un programa. ¿Cuántos GB de memoria usa?", "8*50//100", "El 50 % de 8 GB es la mitad.", " GB"),
        ("abc", "{F} Tras aumentar la memoria del equipo X a 8 GB, el mismo programa sigue usando 2,4 GB. ¿Qué porcentaje de la memoria usa ahora?", "30 %", "60 %", "2,4 %", "2,4 ÷ 8 = 0,3, es decir 30 %."),
        ("abc", "{F} Antes de liberar espacio en el equipo Y, ¿qué conviene hacer?", "Respaldar y consultar a la usuaria qué archivos puede borrar", "Borrar archivos al azar", "Formatear el disco sin avisar", "Se evita perder datos de trabajo."),
        ("abc", "{F} La jefa dice: «compremos RAM para el equipo Y». ¿Cuál es el argumento correcto?", "No resuelve el problema: el síntoma indica falta de almacenamiento", "Sí, toda lentitud se arregla con RAM", "Sí, porque es barato", "La causa no es la memoria sino el espacio."),
        ("=", "{F} Una memoria adicional de ejemplo cuesta $25.000 y hay que equipar 2 equipos. ¿Cuántos pesos cuestan las dos?", "25000*2", "Se multiplica el costo de una por la cantidad.", " pesos"),
        ("abc", "Para ahorrar, el encargado propone instalar un programa de oficina sin licencia en los tres equipos. ¿Qué corresponde?", "No hacerlo: compromete la seguridad y no cumple la licencia", "Hacerlo si nadie se entera", "Pedirle a un amigo que lo instale", "El software sin licencia es un riesgo legal y de seguridad."),
        ("ab", "{F} Se comprueba que el controlador oficial de la impresora existe para la versión del sistema. ¿Es una evidencia a favor de instalarlo?", "Sí, confirma compatibilidad", "No, no tiene relación", "Si el controlador oficial es compatible, instalarlo es una opción segura."),
    ],
    ctx=("abc", "La oficina de ejemplo tiene poco presupuesto. El técnico debe elegir entre comprar memoria para el equipo X o liberar espacio en el equipo Y. ¿Cómo se decide de forma responsable?", "Resolver primero la causa de cada síntoma con evidencia y priorizar por el impacto en el trabajo", "Comprar lo más caro", "Elegir al azar", "Se decide con evidencia, costo e impacto."),
    sc=[
        ("En Programación: ¿qué síntoma sugiere poca memoria RAM?", "Lentitud al abrir varios programas a la vez", "El equipo no tiene espacio de trabajo suficiente."),
        ("¿Qué síntoma indica poco almacenamiento?", "No deja guardar más archivos", "El espacio libre es muy pequeño."),
        ("¿Qué se prueba primero?", "Las opciones simples y reversibles", "Esas opciones reducen costo y riesgo."),
    ],
    op=("Informe de ejemplo: Equipo P: «tarda mucho en abrir el programa de notas y la memoria de 4 GB está al 90 % de uso»; Equipo Q: «el disco de 200 GB tiene 195 GB usados»; Equipo R: «el escáner nuevo no es reconocido». Elige para cada equipo una mejora entre aumentar RAM, liberar o ampliar almacenamiento e instalar el controlador, justifica con el dato y escribe qué harías antes de cambiar nada.",
        "P: aumentar la memoria RAM (90 % de 4 GB en uso). Q: liberar espacio o ampliar el almacenamiento (quedan 5 GB libres de 200 GB). R: instalar el controlador oficial del escáner. Antes de cambiar, haría respaldo, pediría autorización y lo anotaría en la bitácora; las intervenciones de hardware las hace personal autorizado.",
        ["relaciona cada síntoma con la mejora correcta", "justifica con un dato de la ficha", "incluye respaldo, autorización y registro"],
        ["tabla con equipo, mejora y dato que la respalda"],
        ["recomendar RAM para todos", "no citar el dato", "olvidar el respaldo"],
        "Pregunta: «¿qué dato justifica tu elección para el equipo Q?». Si no responde, pídele que calcule el espacio libre."),
    reinforce="Escribe un síntoma y la mejora que corresponde para un equipo de ejemplo con poco almacenamiento.",
    extend="Explica con un ejemplo inventado por qué a veces conviene optimizar el software antes de comprar hardware.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 32 (plan de ejemplo, inventado) de la «Municipalidad de Ejemplo» (nombre inventado). Se deben actualizar 8 equipos. Cada actualización de software toma 30 minutos por equipo y se hace de a un equipo a la vez, "
     "en una ventana de 5 horas fuera del horario de atención. Presupuesto de ejemplo: $200.000. Costos de ejemplo: memoria adicional $30.000 por equipo; disco más grande $45.000 por equipo. "
     "Prioridades: primero las actualizaciones de seguridad, luego el rendimiento. Reglas: respaldo previo, plan de reversa, acta de entrega y bitácora.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: planificar una ventana de actualización, calcular costos y priorizar por seguridad.",
    prior=["Sé qué es un plan de actualización y una ventana.", "Sé calcular tiempos y costos.", "Sé qué es una actualización de seguridad."],
    explain=[
        "Un plan de actualización masivo se apoya en cálculos. El tiempo total es el tiempo por equipo multiplicado por la cantidad de equipos; si supera la ventana disponible, se divide el trabajo en más de una ventana. El costo total es el valor de cada pieza multiplicado por la cantidad de equipos y debe caber en el presupuesto; si no cabe, se prioriza.",
        "El criterio de prioridad es técnico y de seguridad: primero se corrigen los agujeros de seguridad, porque exponen los datos de las personas, y luego el rendimiento. Se actualiza primero un grupo pequeño de prueba (un piloto) y, si funciona, el resto. Siempre hay respaldo previo, plan de reversa para volver atrás y bitácora de cada equipo.",
        "Los equipos se entregan con acta, y la usuaria confirma que su trabajo funciona. Los datos personales que contienen los equipos no se copian ni se ven más de lo necesario. Si algo no cabe en el tiempo o el presupuesto, el técnico informa la situación y propone alternativas, sin recortar el respaldo ni las pruebas.",
    ],
    vocab=[("piloto", "grupo pequeño de equipos para probar antes de actualizar el resto"), ("ventana de actualización", "horario acordado para actualizar con menos interrupciones"), ("presupuesto", "monto máximo disponible"), ("plan de reversa", "pasos para volver atrás si algo falla"), ("prioridad de seguridad", "corregir primero lo que expone datos")],
    worked=[
        ("Tiempo total", "Una oficina de ejemplo actualiza 6 equipos a 20 minutos cada uno. ¿Cuántos minutos son en total?", ["Se multiplica el tiempo por la cantidad de equipos.", "20 por 6."], "120 minutos"),
        ("Cabe en el presupuesto", "Presupuesto de ejemplo $100.000. Cada pieza cuesta $30.000 y se necesitan 4. ¿Cabe?", ["Costo total: 30.000 por 4 = 120.000.", "120.000 es mayor que 100.000."], "No cabe"),
    ],
    mistakes=[("Actualizar los 8 equipos a la vez sin probar antes en un grupo piloto.", "Si falla, todos los equipos quedan afectados.", "Prueba primero en un piloto de uno o dos equipos."),
              ("Recortar el respaldo para que el trabajo quepa en la ventana.", "Si algo falla se pierden datos.", "Informa que no cabe y pide otra ventana.")],
    T=[
        ("abc", "En Programación: ¿qué es un piloto en una actualización masiva?", "Un grupo pequeño de equipos para probar antes de actualizar el resto", "El jefe de la actualización", "Un programa de dibujo", "Probar en un piloto reduce el riesgo de falla."),
        ("abc", "En Programación: ¿qué se prioriza primero en un plan de actualización?", "Las actualizaciones de seguridad", "Los fondos de pantalla", "Las mejoras estéticas", "La seguridad protege los datos de las personas."),
        ("=", "{F} ¿Cuántos minutos toma actualizar los 8 equipos?", "30*8", "Se multiplican los minutos por equipo por la cantidad de equipos.", " minutos"),
        ("=", "{F} ¿Cuántas horas son esos minutos?", "30*8//60", "Se divide el total de minutos por 60.", " horas"),
        ("abc", "{F} ¿Cabe el trabajo en la ventana de 5 horas?", "Sí, porque 4 horas es menos que 5", "No, porque 4 horas es más que 5", "No se puede saber", "Las 4 horas calculadas caben en las 5 horas de la ventana."),
        ("=", "{F} ¿Cuánto cuesta dar memoria adicional a los 8 equipos?", "30000*8", "Se multiplica el costo por equipo por la cantidad de equipos.", " pesos"),
        ("abc", "{F} ¿Cabe la memoria para los 8 equipos en el presupuesto de $200.000?", "No: cuesta $240.000", "Sí: cuesta $160.000", "Sí: cuesta $200.000", "30.000 por 8 es 240.000, mayor que el presupuesto."),
        ("=", "{F} ¿Para cuántos equipos alcanza el presupuesto si se compra solo memoria?", "200000//30000", "Se divide el presupuesto por el costo de cada pieza y se toma la parte entera.", " equipos"),
        ("abc", "{F} Con el presupuesto, ¿qué decisión es más prudente?", "Equipar primero los equipos con peor rendimiento y registrar los pendientes", "Comprar piezas no compatibles", "Pedir un préstamo sin avisar", "Se prioriza con el presupuesto y se documenta lo pendiente."),
        ("=", "{F} Se actualizan 2 equipos como piloto y 6 el resto. Si cada uno toma 30 minutos, ¿cuántos minutos toma el piloto?", "30*2", "Se multiplican los minutos por los equipos del piloto.", " minutos"),
        ("abc", "{F} El piloto falla en un equipo. ¿Qué corresponde?", "Aplicar el plan de reversa, anotarlo y revisar la causa antes de seguir", "Seguir con los otros 6 de todos modos", "Borrar la bitácora", "No se avanza hasta entender la falla."),
        ("abc", "El técnico propone usar parches «piratas» de un sitio desconocido para acelerar. ¿Qué responde la jefatura?", "No: solo parches oficiales del fabricante", "Sí, si funcionan en el piloto", "Sí, para ahorrar tiempo", "Un parche de origen dudoso puede traer amenazas."),
        ("ab", "{F} Un funcionario pide copiar a su pendrive los archivos del equipo «para estar seguro». ¿Qué corresponde?", "Seguir el respaldo oficial de la organización", "Dejar que cada persona copie como quiera", "El respaldo se hace por el canal oficial para proteger los datos."),
    ],
    ctx=("abc", "Faltando una hora para el cierre de la ventana, quedan 2 equipos sin actualizar y sin respaldo. ¿Qué hace el técnico?", "Informa, deja esos equipos para otra ventana y anota el motivo", "Los actualiza sin respaldo", "Alarga la ventana sin avisar", "Se informa y se reprograma, sin recortar el respaldo."),
    sc=[
        ("En Programación: ¿cómo se calcula el tiempo total de una actualización masiva?", "Tiempo por equipo por cantidad de equipos", "El resultado se compara con la ventana disponible."),
        ("¿Qué se actualiza primero?", "Lo que corrige problemas de seguridad", "Esto protege los datos de las personas."),
        ("¿Qué se hace si el piloto falla?", "Aplicar el plan de reversa y revisar la causa", "No se sigue hasta entender la falla."),
    ],
    op=("Una escuela de ejemplo debe actualizar 10 equipos: 20 minutos cada uno, ventana de 4 horas. Hay $90.000 y la memoria cuesta $25.000 por equipo. Calcula si caben en la ventana, para cuántos equipos alcanza el presupuesto de memoria y propone un orden de trabajo con piloto, respaldo y registro.",
        "Tiempo: 20 × 10 = 200 minutos (3 h 20 min), cabe en 4 horas. Presupuesto: 90.000 ÷ 25.000 = 3 equipos. Orden: respaldo, piloto en 1 o 2 equipos, plan de reversa, resto de equipos, acta de entrega y bitácora; las actualizaciones de seguridad primero.",
        ["calcula tiempo y presupuesto", "decide con piloto, respaldo y prioridad de seguridad", "incluye acta y bitácora"],
        ["hoja con los cálculos y el orden de trabajo"],
        ["no convertir minutos a horas", "olvidar el piloto", "recortar el respaldo"],
        "Pregunta: «¿cómo sabes que caben en la ventana?». Si no responde, pídele que compare 200 minutos con 240."),
    reinforce="Calcula cuánto tarda actualizar 12 equipos si cada uno toma 15 minutos.",
    extend="Explica con un ejemplo inventado por qué se prefiere un piloto antes de actualizar todos los equipos.",
)

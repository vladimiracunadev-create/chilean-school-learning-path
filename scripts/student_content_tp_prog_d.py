"""Programación TP 3.º y 4.º medio: OAE-09 (instalar y configurar sistemas operativos e integrarlos a una red LAN) y OAE-10 (instalar software de productividad y utilitarios). Casos de papel con datos inventados; no se hace ningún trabajo práctico sobre equipos."""
from __future__ import annotations

from tp_prog_common import build

O9 = "TP-PROG-3y4-OAE-09"
O10 = "TP-PROG-3y4-OAE-10"

# ============================================================ OAE-09, clase 1
F = ("Ficha 33 (caso de ejemplo, inventado). El «Liceo Los Coigües» (nombre de ejemplo) prepara 10 computadores para su sala de computación y los incorporará a una red LAN (red de área local: conecta equipos cercanos, como los de una sala o un edificio). "
     "Estándar de seguridad de ejemplo de la organización: cuentas individuales (no compartidas); contraseña de al menos 12 caracteres con mayúscula, minúscula y número; actualizaciones automáticas activadas; antivirus activo; "
     "cuenta de administrador usada solo para tareas de instalación. Todo cambio se autoriza por escrito, se respalda y se anota en la bitácora.")
build(
    O9, 1, F,
    use="Aprenderé qué es un sistema operativo, qué es una red LAN y qué estándares de calidad y seguridad se exigen al configurar un equipo.",
    prior=["Sé qué es hardware y software.", "Sé qué es una cuenta de usuario.", "Sé qué es una bitácora."],
    explain=[
        "El sistema operativo es el software principal de un computador: administra el hardware, ejecuta los programas y entrega la forma de usar el equipo. Una red LAN es la red que conecta computadores cercanos entre sí y con recursos compartidos, como una impresora o un servidor, de modo que puedan compartir archivos y servicios. Instalar y configurar un equipo para la red significa dejarlo funcionando, con su identidad en la red y las medidas de seguridad de la organización.",
        "La organización fija estándares: reglas iguales para todos los equipos. Un estándar de calidad busca que todos queden con la misma configuración, para que sea más fácil mantenerlos y encontrar fallas. Un estándar de seguridad protege a las personas y a los datos con medidas como cuentas individuales, contraseñas fuertes, actualizaciones automáticas y antivirus. Los valores de la ficha son de ejemplo; los reales los fija la política de cada organización.",
        "Los riesgos más frecuentes son usar cuentas compartidas, dejar contraseñas simples o escritas en un papel pegado al monitor, no actualizar el sistema y usar la cuenta de administrador para todo. En este cuaderno jamás se escriben contraseñas reales: se trabaja con ejemplos inventados. Esto es solo conceptual y no te habilita para instalar ni configurar equipos de una organización.",
    ],
    vocab=[("sistema operativo", "software principal que administra el hardware y ejecuta los programas"), ("red LAN", "red que conecta computadores cercanos"), ("estándar", "regla común que se aplica a todos los equipos"), ("cuenta individual", "cuenta que usa solo una persona"), ("administrador", "cuenta con permisos para cambiar la configuración"), ("actualización automática", "instalación de correcciones sin que la persona deba pedirla")],
    worked=[
        ("Cuenta individual", "Tres estudiantes de ejemplo comparten la misma cuenta del computador. ¿Qué estándar se incumple y por qué importa?", ["Las cuentas deben ser individuales.", "Con una cuenta compartida no se sabe quién hizo cada cambio."], "Cuentas individuales; sin ellas no hay trazabilidad"),
        ("Aplicar la regla de la contraseña", "Contraseña de ejemplo inventada: «Sol1». ¿Cumple el estándar de al menos 12 caracteres?", ["«Sol1» tiene 4 caracteres.", "4 es menor que 12."], "No cumple"),
    ],
    mistakes=[("Usar la cuenta de administrador para el trabajo diario porque «así no pide permisos».", "Un error o un programa dañino tendría permisos para dañar todo el equipo.", "Usa una cuenta estándar y el administrador solo para tareas de instalación."),
              ("Anotar la contraseña en un papel pegado al monitor.", "Cualquier persona que pase puede verla.", "Memorízala o usa el método de gestión que indique la organización.")],
    T=[
        ("abc", "En Programación: ¿qué es un sistema operativo?", "El software principal que administra el hardware y ejecuta los programas", "Una pieza física del computador", "Una red de computadores", "El sistema operativo es la base sobre la que funcionan los programas."),
        ("abc", "En Programación: ¿qué es una red LAN?", "Una red que conecta computadores cercanos", "Un tipo de contraseña", "Un programa de dibujo", "LAN significa red de área local."),
        ("abc", "En Programación: ¿para qué sirve un estándar de configuración?", "Para que todos los equipos queden iguales y sean más fáciles de mantener", "Para que cada equipo sea distinto", "Para evitar usar contraseñas", "Un estándar uniforme facilita el mantenimiento y la seguridad."),
        ("abc", "{F} ¿Cuál de estas contraseñas de ejemplo inventadas cumple el largo mínimo del estándar?", "Roble-Azul-2041", "Mesa7!", "laguna1234", "«Roble-Azul-2041» tiene 15 caracteres; las otras tienen menos de 12."),
        ("abc", "{F} ¿Qué incumple una sala donde todos los estudiantes usan la misma cuenta?", "El estándar de cuentas individuales", "El estándar de antivirus", "El largo de la contraseña", "Sin cuentas individuales no se sabe quién hizo cada cambio."),
        ("abc", "{F} ¿Para qué debe usarse la cuenta de administrador, según el estándar?", "Solo para tareas de instalación", "Para el trabajo diario", "Para navegar por internet", "Usar permisos mínimos reduce el daño de un error."),
        ("=", "{F} Si cada uno de los 10 computadores necesita su propio nombre en la red, ¿cuántos nombres distintos se necesitan?", "10", "Cada equipo debe tener un nombre único.", " nombres"),
        ("abc", "{F} Un estudiante quiere usar en el computador del liceo la misma contraseña que ya usa en su correo personal. ¿Qué corresponde?", "No reutilizar contraseñas de otros servicios y crear una nueva", "Usarla porque ya la recuerda", "Compartirla con un amigo", "Reutilizar contraseñas aumenta el riesgo si una se filtra."),
        ("=", "{F} Una sala tiene 10 computadores y 3 aún no tienen antivirus activo. ¿Cuántos sí cumplen ese estándar?", "10-3", "Se restan los que no cumplen al total.", " computadores"),
        ("abc", "{F} Un técnico de ejemplo desactiva las actualizaciones automáticas para que «no molesten». ¿Qué riesgo crea?", "Quedan sin corregir fallas de seguridad conocidas", "El equipo se vuelve más seguro", "El equipo usa menos memoria", "Sin actualizaciones se acumulan fallas conocidas."),
        ("abc", "El técnico configura un equipo sin pedir autorización ni anotar en la bitácora. ¿Qué principio se rompe?", "Todo cambio se autoriza, se respalda y se registra", "Cada equipo debe tener un fondo distinto", "Debe haber una cuenta compartida", "El registro permite revisar lo hecho."),
        ("=", "En una sala de ejemplo hay 10 computadores y 2 impresoras de red, y los computadores se reparten por igual entre las impresoras. ¿Cuántos computadores usan cada impresora?", "10//2", "Se reparten los computadores entre las impresoras.", " computadores"),
        ("ab", "{F} Un estudiante ofrece su contraseña real para que el técnico «pruebe el equipo». ¿Qué responde el técnico?", "Que no la necesita y que probará con una cuenta de ejemplo", "Que la anote en la bitácora", "El técnico nunca recibe contraseñas reales y prueba con cuentas de ejemplo."),
    ],
    ctx=("abc", "La directora de un liceo de ejemplo pide que todos los equipos usen la misma contraseña «para que sea más fácil». ¿Qué propone el técnico?", "Mantener cuentas individuales con contraseñas propias y explicar el riesgo", "Aceptar sin decir nada", "Quitar las contraseñas", "El técnico informa el riesgo y propone una solución segura."),
    sc=[
        ("En Programación: ¿qué es una red LAN?", "Una red que conecta computadores cercanos", "Permite compartir archivos y recursos entre los equipos."),
        ("¿Cuántos caracteres mínimos pide el estándar de la ficha para la contraseña?", "12", "Es el largo mínimo que fija el ejemplo."),
        ("¿Para qué se usa la cuenta de administrador?", "Solo para tareas de instalación", "Usar permisos mínimos reduce el riesgo de daño."),
    ],
    op=("Un centro comunitario de ejemplo prepara 6 computadores con el estándar de la ficha. Escribe una lista de cinco medidas de seguridad que verificarías en cada equipo, indica cuál de estas contraseñas de ejemplo inventadas cumple («Cerro8», «Cobre-Rojo-3019», «azul12345678») y por qué, y qué harías si alguien te ofrece su contraseña real. Esto es solo conceptual.",
        "Medidas: cuentas individuales, contraseña de al menos 12 caracteres con mayúscula, minúscula y número, actualizaciones automáticas, antivirus activo y administrador solo para instalación. Cumple «Cobre-Rojo-3019»: tiene 15 caracteres con mayúscula, minúsculas y números; «Cerro8» es corta y «azul12345678» no tiene mayúscula. Si ofrecen su contraseña real, no la recibiría ni la anotaría.",
        ["nombra cinco medidas del estándar", "evalúa las tres contraseñas con el estándar", "rechaza la contraseña real"],
        ["hoja con las cinco medidas y la evaluación"],
        ["aceptar una contraseña corta", "ignorar la mayúscula", "recibir una contraseña real"],
        "Pregunta: «¿qué regla incumple azul12345678?». Si no responde, pídele que revise cada requisito del estándar."),
    reinforce="Inventa una contraseña de ejemplo que cumpla el estándar y otra que no, y explica la diferencia.",
    extend="Explica con un ejemplo inventado por qué las cuentas compartidas dificultan encontrar quién cometió un error.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 34 (plan de direccionamiento de ejemplo, inventado) de la sala de computación del liceo. Red: 192.168.10.0. Máscara de red: 255.255.255.0. Puerta de enlace (el equipo que conecta la sala con el exterior): 192.168.10.1. "
     "Servidor de la sala: 192.168.10.10 (dirección fija). Impresora de la red: 192.168.10.20 (dirección fija). Rango entregado automáticamente por DHCP a los computadores: de 192.168.10.50 a 192.168.10.200. "
     "Documentos: plan de direccionamiento, estándar de configuración, inventario y acta de entrega. Roles: administrador de la red, técnico de instalación, usuario y jefatura de TI.")
build(
    O9, 2, F,
    use="Aprenderé los conceptos de direccionamiento de una red LAN (dirección IP, máscara, puerta de enlace y DHCP), los documentos y los roles.",
    prior=["Sé qué es una red LAN.", "Sé qué es un estándar.", "Sé restar y sumar números."],
    explain=[
        "Cada equipo de una red LAN tiene una dirección IP, un número que lo identifica en la red, escrito con cuatro números separados por puntos (como 192.168.10.50). La máscara de red indica qué parte de la dirección corresponde a la red: con la máscara 255.255.255.0 los tres primeros números identifican la red y el último identifica al equipo. Dos equipos hablan directamente solo si sus tres primeros números coinciden con esa máscara.",
        "La puerta de enlace es el equipo (generalmente un router) que conecta la red local con el exterior, y se anota en cada computador. La dirección puede ser fija, anotada a mano para equipos que no deben cambiar, como un servidor o una impresora, o entregada automáticamente por DHCP, un servicio que reparte direcciones libres a los equipos que se conectan. Dos equipos no pueden tener la misma dirección: se produce un conflicto.",
        "El plan de direccionamiento es el documento que lista las direcciones fijas, el rango de DHCP, la máscara y la puerta de enlace. Con el estándar de configuración, el inventario y el acta de entrega permiten que otra persona comprenda y revise la red. Los datos de esta ficha son de ejemplo. Quien configura no cambia direcciones por su cuenta: lo autoriza el administrador de la red.",
    ],
    vocab=[("dirección IP", "número que identifica un equipo en la red"), ("máscara de red", "indica qué parte de la dirección identifica la red"), ("puerta de enlace", "equipo que conecta la red local con el exterior"), ("DHCP", "servicio que reparte direcciones automáticamente"), ("dirección fija", "dirección anotada a mano que no cambia"), ("conflicto de direcciones", "dos equipos con la misma dirección")],
    worked=[
        ("Misma red", "Con máscara 255.255.255.0, ¿están en la misma red 192.168.10.5 y 192.168.10.70?", ["Se comparan los tres primeros números: 192.168.10 en ambas.", "Coinciden."], "Sí, están en la misma red"),
        ("Distinta red", "Con máscara 255.255.255.0, ¿está 192.168.20.5 en la red 192.168.10.0?", ["Los tres primeros números son 192.168.20.", "No coinciden con 192.168.10."], "No, está en otra red"),
    ],
    mistakes=[("Asignar la misma dirección fija a dos equipos «porque son iguales».", "Dos equipos con la misma dirección producen un conflicto y ninguno funciona bien.", "Cada equipo tiene una dirección única; anótala en el plan."),
              ("Escribir una dirección fuera del rango de la red en un equipo de la sala.", "Ese equipo no podrá hablar con los demás.", "Usa direcciones de la red de la ficha, con los tres primeros números coincidentes.")],
    T=[
        ("abc", "En Programación: ¿qué es una dirección IP?", "Un número que identifica un equipo en la red", "La contraseña del equipo", "El nombre del usuario", "La dirección IP permite ubicar cada equipo."),
        ("abc", "En Programación: ¿qué hace el servicio DHCP?", "Reparte direcciones automáticamente a los equipos", "Cifra los archivos", "Instala programas", "DHCP asigna direcciones libres a los equipos que se conectan."),
        ("abc", "En Programación: ¿qué es la puerta de enlace?", "El equipo que conecta la red local con el exterior", "El cable que va a la pared", "La impresora de la red", "Permite salir de la red local."),
        ("abc", "{F} ¿Cuál es la dirección fija de la impresora de la ficha?", "192.168.10.20", "192.168.10.10", "192.168.10.1", "La impresora tiene la dirección .20."),
        ("abc", "{F} ¿Qué dirección tiene el servidor?", "192.168.10.10", "192.168.10.20", "192.168.10.50", "El servidor tiene dirección fija .10."),
        ("abc", "{F} Con la máscara de la ficha, ¿qué equipo está en la misma red que 192.168.10.60?", "192.168.10.150", "192.168.20.60", "10.0.0.60", "Los tres primeros números 192.168.10 coinciden."),
        ("=", "{F} ¿Cuántas direcciones distintas reparte DHCP en el rango de la ficha (de .50 a .200 inclusive)?", "200-50+1", "Se cuentan los extremos: 200 − 50 más 1.", " direcciones"),
        ("abc", "{F} Un computador recibe por DHCP la dirección 192.168.10.30. ¿Qué ocurre?", "Está fuera del rango de DHCP de la ficha y hay que revisar la configuración", "Es perfectamente normal", "Es la dirección del servidor", "El rango de DHCP va de .50 a .200."),
        ("abc", "{F} Se asigna a un computador la dirección 192.168.10.20. ¿Qué problema aparece?", "Conflicto con la impresora que ya tiene esa dirección", "Ninguno", "No hay problema, es una dirección libre", "Dos equipos no pueden compartir dirección."),
        ("=", "{F} Hay 30 computadores en la sala y DHCP reparte 151 direcciones. ¿Cuántas direcciones quedan libres?", "151-30", "Se restan los equipos al total de direcciones.", " direcciones"),
        ("abc", "{F} ¿Qué documento muestra las direcciones fijas, el rango de DHCP y la puerta de enlace?", "El plan de direccionamiento", "El acta de entrega", "La bitácora de respaldos", "El plan de direccionamiento reúne esos datos."),
        ("abc", "Un técnico cambia direcciones de la red sin avisar al administrador de la red. ¿Qué problema puede ocurrir?", "Se pueden producir conflictos y fallas que nadie sabe explicar", "Se acelera la red", "Aumenta el número de usuarios", "Los cambios deben autorizarse y registrarse."),
        ("ab", "{F} ¿Está 192.168.10.1, la puerta de enlace, dentro del rango de DHCP?", "No, porque .1 es menor que .50", "Sí, porque es la primera dirección", "El rango de DHCP empieza en .50, así que .1 no se reparte."),
    ],
    ctx=("abc", "Dos computadores de la sala dejan de conectarse el mismo día. Al revisar se encuentra que ambos tienen la dirección 192.168.10.75. ¿Qué hace el técnico?", "Informa al administrador de la red, corrige una dirección y lo anota en la bitácora", "Cambia todas las direcciones de la sala", "Apaga la red entera sin avisar", "Se corrige solo lo necesario y se deja registro."),
    sc=[
        ("En Programación: ¿qué identifica a un equipo en la red?", "Su dirección IP", "La dirección de cada equipo debe ser única."),
        ("¿Cuándo dos direcciones están en la misma red con máscara 255.255.255.0?", "Cuando coinciden sus tres primeros números", "Entre equipos de la misma red solo cambia el último número."),
        ("¿Qué equipos reciben dirección fija?", "Los que no deben cambiar, como servidor e impresora", "Así se encuentran siempre en la misma dirección."),
    ],
    op=("Un centro de ejemplo usa la red 192.168.30.0, máscara 255.255.255.0, puerta de enlace 192.168.30.1, impresora fija 192.168.30.20 y DHCP de .100 a .150. Indica: cuántas direcciones reparte DHCP, si 192.168.30.120 es válido para un computador, si 192.168.40.120 está en la misma red y qué problema habría si un computador recibiera .20.",
        "DHCP reparte 150 − 100 + 1 = 51 direcciones. 192.168.30.120 es válido (está en el rango de DHCP). 192.168.40.120 no está en la misma red (cambia el tercer número). Si un computador recibiera .20 habría un conflicto con la impresora.",
        ["cuenta bien las direcciones del rango", "distingue misma red y otra red", "identifica el conflicto de direcciones"],
        ["hoja con los cuatro resultados"],
        ["olvidar sumar 1 al contar el rango", "confundir el tercer número", "no reconocer el conflicto"],
        "Pregunta: «¿cuántas direcciones hay entre .100 y .150 inclusive?». Si no responde, pídele que cuente con los extremos."),
    reinforce="Escribe tres direcciones válidas y una inválida para la red 192.168.10.0 con máscara 255.255.255.0.",
    extend="Explica con un ejemplo inventado por qué se anotan en un documento las direcciones fijas.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 35 (caso de ejemplo, inventado). Tabla de configuración de cinco computadores de la sala del liceo. Red: 192.168.10.0, máscara 255.255.255.0, puerta de enlace 192.168.10.1. "
     "PC1: IP 192.168.10.51, puerta 192.168.10.1. PC2: IP 192.168.10.52, puerta 192.168.10.1. PC3: IP 192.168.10.52, puerta 192.168.10.1. PC4: IP 192.168.20.53, puerta 192.168.10.1. PC5: IP 192.168.10.54, puerta 192.168.10.9. "
     "Síntomas: PC2 y PC3 «a veces pierden la conexión»; PC4 «no ve a los demás equipos»; PC5 «no sale a internet».")
build(
    O9, 3, F,
    use="Aprenderé a revisar en papel la configuración de varios equipos, detectar errores y proponer una corrección sin riesgo.",
    prior=["Sé qué son dirección IP, máscara y puerta de enlace.", "Sé qué es un conflicto de direcciones.", "Sé comparar valores."],
    explain=[
        "Revisar una configuración es comparar cada equipo con el plan. Para cada uno se verifica que su dirección esté en la red correcta (tres primeros números iguales), que no se repita con otro equipo y que su puerta de enlace sea la del plan. Se anota una tabla de resultados y se identifica el tipo de error.",
        "Los errores típicos tienen síntomas conocidos. Dos equipos con la misma dirección producen un conflicto y pérdidas de conexión intermitentes. Un equipo con una dirección de otra red no ve a los de la red principal. Un equipo con una puerta de enlace incorrecta puede hablar con los de su red pero no puede salir al exterior. Con la evidencia del síntoma se hace una hipótesis y se comprueba con el plan.",
        "La corrección es mínima y registrada: se cambia solo lo necesario, con autorización del administrador de la red, y se anota el antes y el después en la bitácora. No se prueba con contraseñas reales ni se comparte información de otros usuarios mientras se revisa. Si el cambio afecta a muchos equipos, se hace en una ventana acordada.",
    ],
    vocab=[("configuración", "valores que definen cómo funciona un equipo en la red"), ("hipótesis", "explicación posible que se comprueba con datos"), ("conexión intermitente", "conexión que se pierde y vuelve a veces"), ("antes y después", "registro del valor anterior y del nuevo")],
    worked=[
        ("Detectar un conflicto", "En una tabla de ejemplo, el equipo A tiene 192.168.10.40 y el equipo B también. ¿Qué ocurre?", ["Dos equipos comparten la misma dirección.", "Hay un conflicto de direcciones."], "Conflicto de direcciones"),
        ("Puerta incorrecta", "Un equipo de ejemplo tiene puerta 192.168.10.9 y el plan dice 192.168.10.1. ¿Qué puede hacer y qué no?", ["Puede comunicarse con su red local.", "No puede salir al exterior por la puerta equivocada."], "Ve a su red, pero no sale a internet"),
    ],
    mistakes=[("Cambiar la dirección de los cinco equipos para «empezar de nuevo».", "Se pierde la configuración correcta de los que estaban bien.", "Cambia solo los equipos con error y anota el antes y el después."),
              ("Asumir que el problema es del cable sin revisar la configuración.", "Se pierde tiempo cambiando algo que funciona.", "Compara primero cada equipo con el plan.")],
    T=[
        ("abc", "En Programación: ¿qué es un conflicto de direcciones?", "Dos equipos con la misma dirección IP", "Dos usuarios con el mismo nombre", "Dos programas iguales", "Cada equipo debe tener una dirección única."),
        ("abc", "En Programación: ¿qué es una hipótesis en un diagnóstico?", "Una explicación posible que se comprueba con datos", "Un hecho ya comprobado", "Una contraseña", "Se comprueba con la evidencia del plan."),
        ("abc", "{F} ¿Qué equipos tienen un conflicto de direcciones?", "PC2 y PC3", "PC1 y PC2", "PC4 y PC5", "PC2 y PC3 tienen la misma dirección 192.168.10.52."),
        ("abc", "{F} ¿Qué equipo está en una red distinta de la principal?", "PC4", "PC1", "PC5", "PC4 tiene 192.168.20.53 y la red principal es 192.168.10."),
        ("abc", "{F} ¿Qué equipo tiene una puerta de enlace distinta de la del plan?", "PC5", "PC3", "PC2", "PC5 tiene 192.168.10.9 en lugar de 192.168.10.1."),
        ("abc", "{F} El síntoma de PC5 es «no sale a internet». ¿Cuál es la causa más probable?", "La puerta de enlace incorrecta", "El conflicto de direcciones", "La dirección de otra red", "Con puerta equivocada no puede salir al exterior."),
        ("abc", "{F} El síntoma de PC4 es «no ve a los demás equipos». ¿Cuál es la causa más probable?", "Su dirección es de otra red (192.168.20.x)", "La puerta de enlace incorrecta", "El conflicto de direcciones", "Está en otra red y no ve a los demás."),
        ("=", "{F} De los cinco computadores, ¿cuántos tienen la configuración sin errores?", "1", "Solo PC1 tiene red, dirección única y puerta correctas.", " computador"),
        ("abc", "{F} ¿Cuál es una corrección mínima para PC4?", "Asignarle una dirección libre de la red 192.168.10.x, dentro del rango del plan y con autorización", "Cambiar todas las direcciones", "Reemplazar el cable", "Se corrige solo lo necesario y se registra."),
        ("abc", "{F} Para PC3, ¿qué dirección sería adecuada, según el rango de DHCP .50 a .200 y las direcciones usadas?", "192.168.10.55", "192.168.10.52", "192.168.20.52", "Está en la red, en el rango y no se repite."),
        ("=", "{F} Si cada corrección toma 10 minutos y hay que corregir 3 equipos (uno de los dos con conflicto, PC4 y PC5), ¿cuántos minutos toman las 3 correcciones?", "10*3", "Se multiplican los minutos por las correcciones necesarias.", " minutos"),
        ("abc", "El técnico, para comprobar, pide a una usuaria su contraseña real. ¿Qué corresponde?", "No pedirla y usar una cuenta de ejemplo o la suya autorizada", "Pedirla igual", "Anotarla en el plan", "Las contraseñas reales no se piden."),
        ("ab", "{F} Después de corregir, el técnico anota «cambios hechos». ¿Es suficiente?", "No: falta el antes y el después de cada equipo y la autorización", "Sí, basta con eso", "La bitácora debe mostrar qué cambió, el valor anterior y el nuevo, y quién autorizó."),
    ],
    ctx=("abc", "Una usuaria de ejemplo dice que su computador pierde la conexión «cada diez minutos». El técnico sospecha un conflicto de direcciones. ¿Cómo lo comprueba en papel?", "Compara su dirección con las demás de la tabla y con el plan", "Cambia el computador sin revisar", "Pide su contraseña", "Una comparación con el plan confirma o descarta la hipótesis."),
    sc=[
        ("En Programación: ¿qué síntoma produce un conflicto de direcciones?", "Pérdidas intermitentes de conexión", "Los equipos se pelean por la misma dirección."),
        ("¿Qué síntoma produce una puerta de enlace incorrecta?", "El equipo no sale al exterior", "Aún se comunica con su red local."),
        ("¿Qué se anota en el registro al corregir un error de un programa?", "El valor anterior, el nuevo y quién autorizó", "Así se puede revisar y volver atrás."),
    ],
    op=("Red de ejemplo: 192.168.10.0, máscara 255.255.255.0, puerta 192.168.10.1. Tabla: A (192.168.10.60, puerta .1), B (192.168.10.61, puerta .1), C (192.168.10.61, puerta .1), D (192.168.15.62, puerta .1), E (192.168.10.63, puerta .7). Encuentra los errores, indica el síntoma de cada uno y qué corregirías con registro.",
        "B y C tienen la misma dirección (.61): conflicto y pérdidas de conexión. D está en la red 192.168.15 y no ve a los demás. E tiene puerta .7 y no sale a internet. A está bien. Corregiría una dirección de B o C, cambiaría D a la red 192.168.10 y E a la puerta .1, con autorización y anotando el antes y el después.",
        ["detecta los tres tipos de error", "asocia cada error con su síntoma", "propone correcciones con registro"],
        ["hoja con la tabla de errores y las correcciones"],
        ["no ver el conflicto", "confundir la causa de cada síntoma", "no registrar el antes y el después"],
        "Pregunta: «¿qué síntoma esperarías de D?». Si no responde, pídele que compare su tercer número con la red."),
    reinforce="Escribe una tabla con tres equipos de ejemplo y marca cuál tiene la dirección de otra red.",
    extend="Explica con un ejemplo inventado cómo distinguirías un problema de dirección de uno de puerta de enlace.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 36 (checklist de ejemplo, inventado) para aceptar un equipo en la red del liceo. Verificar: (1) cuenta de usuario individual; (2) contraseña de al menos 12 caracteres con mayúscula, minúscula y número; (3) actualizaciones automáticas activadas; "
     "(4) antivirus activo; (5) nombre de equipo único y según el plan; (6) dirección dentro del plan; (7) cuenta de administrador usada solo para instalación. Resultado de cuatro equipos de ejemplo: "
     "E1 cumple (1) a (7); E2 cumple todo menos (4); E3 cumple todo menos (2) y (3); E4 cumple (1) a (6) pero usa la cuenta de administrador para el trabajo diario. Regla: un equipo se acepta en la red solo si cumple los 7 puntos.")
build(
    O9, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo para aceptar o rechazar un equipo en la red y justificar la decisión con evidencia.",
    prior=["Sé los estándares de seguridad y calidad de un equipo.", "Sé contar y calcular porcentajes simples.", "Sé qué es una bitácora."],
    explain=[
        "Un criterio de aceptación es una regla que dice cuándo un equipo puede entrar a la red. Se verifica con una lista de comprobación: cada punto se marca como cumple o no cumple. Si falta un punto obligatorio, el equipo no se acepta hasta corregirlo. Así la decisión es objetiva y comparable entre equipos.",
        "Se miden también indicadores sencillos, como el porcentaje de equipos que cumplen todo (equipos conformes dividido por el total, por cien). Un indicador ayuda a decidir qué corregir primero, pero no reemplaza la revisión de cada equipo. Los puntos de seguridad pesan más: un equipo sin antivirus o con contraseña débil es un riesgo para toda la red.",
        "La decisión se escribe con la evidencia usada y se informa a quien corresponde. Los datos personales de las usuarias que aparezcan en un equipo no se copian ni se comentan. Las contraseñas no se muestran en los informes y, en este cuaderno, siempre son ejemplos inventados. Si un equipo no cumple, se informa qué falta y se agenda su corrección.",
    ],
    vocab=[("criterio de aceptación", "regla que dice cuándo un equipo entra a la red"), ("lista de comprobación", "lista de puntos que se marcan como cumple o no cumple"), ("equipo conforme", "equipo que cumple todos los puntos"), ("punto obligatorio", "punto que debe cumplirse sí o sí"), ("agendar una corrección", "fijar fecha y responsable para corregir")],
    worked=[
        ("Aplicar la regla", "Un equipo de ejemplo cumple 6 de los 7 puntos. ¿Se acepta en la red con la regla de la ficha?", ["La regla pide cumplir los 7 puntos.", "Falta uno."], "No, hasta corregir el punto pendiente"),
        ("Porcentaje de conformes", "De 8 equipos de ejemplo, 6 cumplen todo. ¿Qué porcentaje es conforme?", ["6 ÷ 8 = 0,75.", "0,75 × 100."], "75 %"),
    ],
    mistakes=[("Aceptar un equipo que cumple 6 de 7 puntos «porque casi cumple».", "Un solo punto de seguridad pendiente puede abrir un riesgo para toda la red.", "Aplica la regla sin excepciones y agenda la corrección."),
              ("Marcar «cumple» sin haber revisado el punto.", "La decisión se apoya en un dato falso.", "Revisa cada punto con evidencia antes de marcar.")],
    T=[
        ("abc", "En Programación: ¿qué es un criterio de aceptación?", "Una regla que dice cuándo un equipo puede entrar a la red", "Un tipo de cable", "Un programa de oficina", "Permite decidir de forma objetiva y comparable."),
        ("abc", "En Programación: ¿qué es un equipo conforme?", "Un equipo que cumple todos los puntos de la lista", "Un equipo que cumple la mitad de los puntos", "Un equipo nuevo", "Conforme significa que el equipo cumple todos los puntos."),
        ("abc", "{F} ¿Se acepta E1 en la red?", "Sí, cumple los siete puntos", "No, falta el antivirus", "No, usa administrador", "E1 cumple los puntos (1) a (7) de la lista."),
        ("abc", "{F} ¿Se acepta E2 en la red?", "No, porque falta el antivirus", "Sí, cumple casi todo", "Sí, si la usuaria lo pide", "La regla exige los siete puntos y falta el (4)."),
        ("abc", "{F} ¿Qué puntos incumple E3?", "(2) contraseña y (3) actualizaciones", "(4) antivirus", "(7) administrador", "E3 cumple todo menos (2) y (3)."),
        ("=", "{F} ¿Cuántos puntos incumple E3?", "2", "Incumple los puntos (2) y (3).", " puntos"),
        ("abc", "{F} ¿Qué incumple E4?", "El punto (7), cuenta de administrador usada para el trabajo diario", "El punto (4), antivirus", "El punto (1), cuentas individuales", "E4 cumple (1) a (6) y falla (7)."),
        ("=", "{F} ¿Qué porcentaje de los cuatro equipos es conforme?", "1*100//4", "Solo E1 cumple todo y se divide por el total.", " %"),
        ("abc", "{F} ¿Qué equipo incumple más puntos de la lista?", "E3, que incumple dos puntos", "E2, que incumple dos puntos", "E4, que incumple dos puntos", "E3 incumple (2) y (3); E2 y E4 incumplen uno solo."),
        ("abc", "{F} Para corregir E2 hay que...", "Activar el antivirus y volver a comprobar los siete puntos", "Aceptarlo y avisar después", "Cambiar el nombre del equipo", "Se corrige el punto pendiente y se revisa de nuevo."),
        ("abc", "El técnico marca «cumple» el punto (4) en E2 sin abrir el panel del antivirus. ¿Qué principio se rompe?", "Decidir con evidencia revisada", "Usar cuentas individuales", "Tener un nombre único", "Una decisión sin evidencia no es confiable."),
        ("=", "El colegio de ejemplo tiene 40 equipos y 34 conformes. ¿Qué porcentaje no es conforme (aproximado, hacia abajo)?", "6*100//40", "Se calcula el porcentaje de los 6 equipos que no cumplen.", " %"),
        ("ab", "{F} La jefa pide aceptar E2 «solo por esta vez» en la red mientras se compra el antivirus. ¿Qué corresponde?", "Dejar constancia del riesgo y decidir con la jefatura de TI, sin ocultarlo", "Aceptarlo sin anotar nada", "Un permiso excepcional lo decide la jefatura de TI con el riesgo registrado, no se oculta."),
    ],
    ctx=("abc", "Un profesor de ejemplo lleva su computador personal y pide conectarlo a la red del liceo. Falta revisar su antivirus y no tiene cuenta individual. ¿Qué responde el técnico?", "Que primero debe cumplir el estándar; si no, no se conecta", "Lo conecta para no molestar", "Le pide su contraseña personal", "El mismo criterio se aplica a todos los equipos."),
    sc=[
        ("En Programación: ¿cuándo se acepta un equipo en la red?", "Cuando cumple todos los puntos de la lista", "La regla no tiene excepciones por conveniencia."),
        ("¿Cómo se calcula el porcentaje de equipos conformes?", "Equipos conformes dividido por el total, por cien", "Es un indicador simple para decidir qué corregir."),
        ("¿Qué se hace con un equipo que no cumple?", "Se informa qué falta y se agenda su corrección", "El equipo no se acepta hasta corregir lo pendiente."),
    ],
    op=("Un centro de ejemplo revisó 5 equipos con la lista de la ficha: F1 cumple todo; F2 incumple (3); F3 incumple (1) y (2); F4 cumple todo; F5 incumple (7). Indica cuáles se aceptan, cuál incumple más puntos, qué porcentaje es conforme y qué le dirías a la persona que usa F3, sin pedir su contraseña real.",
        "Se aceptan F1 y F4. Incumple más puntos F3 (dos, entre ellos la contraseña). Conformes: 2 ÷ 5 × 100 = 40 %. A la persona de F3 le diría que debe usar una cuenta individual y crear una contraseña que cumpla el estándar, y que el técnico no necesita conocerla.",
        ["decide la aceptación con la regla", "calcula el porcentaje", "comunica sin pedir contraseñas"],
        ["hoja con la decisión por equipo, el porcentaje y el mensaje"],
        ["aceptar un equipo con un punto pendiente", "calcular mal el porcentaje", "pedir la contraseña"],
        "Pregunta: «¿por qué F1 y F4 sí y los demás no?». Si no responde, pídele que relea la regla."),
    reinforce="Haz una lista de comprobación de cuatro puntos para aceptar un teléfono de ejemplo en una red.",
    extend="Explica con un ejemplo inventado por qué una sola excepción puede debilitar la seguridad de toda una red.",
)

# ============================================================ OAE-10, clase 1
F = ("Ficha 37 (caso de ejemplo, inventado). La «Oficina Contable Los Cipreses» (nombre de ejemplo) tiene 3 computadores nuevos y las usuarias piden: escribir cartas (Marta), hacer planillas de cálculo (Pablo) y leer documentos PDF y comprimir archivos (Ana). "
     "Tipos de software: de productividad (para tareas de oficina, como un procesador de textos o una planilla) y utilitario (herramienta de apoyo, como un compresor de archivos, un lector de PDF o un antivirus). "
     "Licencias: comercial (se paga), libre o de código abierto (se puede usar según su licencia) y de prueba (gratis por un tiempo limitado).")
build(
    O10, 1, F,
    use="Aprenderé qué es el software de productividad y los utilitarios, qué tipos de licencia existen y qué cuidados exige instalar programas en un equipo ajeno.",
    prior=["Sé qué es un programa y un sistema operativo.", "Sé qué es una licencia.", "Sé qué es una cuenta de administrador."],
    explain=[
        "El software de productividad sirve para el trabajo de oficina: procesador de textos para escribir documentos, planilla de cálculo para ordenar y calcular datos, y presentaciones para exponer. Los programas utilitarios son herramientas de apoyo: compresor de archivos (junta archivos en uno más liviano), lector de PDF (abre documentos con formato fijo) y antivirus (protege contra programas dañinos). Se instalan según las necesidades de cada persona.",
        "Antes de instalar se escuchan los requerimientos del usuario: qué tareas hace, qué programas necesita y qué formatos usa. Cada programa tiene una licencia: la comercial se paga, la libre o de código abierto se usa según sus condiciones y la de prueba dura un tiempo. Usar un programa comercial sin pagar su licencia (software pirata) es ilegal y riesgoso, porque suele traer programas dañinos.",
        "Se instala solo desde el sitio oficial del proveedor o el canal que fije la organización, con la cuenta de administrador usada solo para eso y con autorización. Se anota en el inventario qué se instaló, en qué equipo y con qué licencia. Los datos de las usuarias se protegen: el técnico no abre sus archivos personales mientras instala.",
    ],
    vocab=[("software de productividad", "programas para tareas de oficina"), ("programa utilitario", "herramienta de apoyo, como un compresor o un antivirus"), ("licencia libre", "licencia que permite usar el programa según sus condiciones"), ("licencia de prueba", "licencia gratuita por tiempo limitado"), ("software pirata", "programa usado sin pagar su licencia"), ("inventario de software", "lista de programas instalados y su licencia")],
    worked=[
        ("Clasificar programas", "Un procesador de textos y un compresor de archivos. ¿Cuál es de productividad y cuál utilitario?", ["El procesador sirve para escribir documentos.", "El compresor es una herramienta de apoyo."], "Procesador: productividad; compresor: utilitario"),
        ("Tipo de licencia", "Un programa de ejemplo funciona gratis por 30 días y luego pide pago. ¿Qué licencia es?", ["Es gratis por un tiempo limitado.", "Es licencia de prueba."], "De prueba"),
    ],
    mistakes=[("Instalar un programa comercial descargado de un sitio que ofrece «versiones gratis».", "Suele ser software pirata y puede traer programas dañinos.", "Instala desde el sitio oficial con licencia."),
              ("Instalar todos los programas posibles «por si acaso».", "Ocupan espacio, abren riesgos de seguridad y pueden no tener licencia.", "Instala solo lo que cada persona necesita.")],
    T=[
        ("abc", "En Programación: ¿qué es un programa utilitario?", "Una herramienta de apoyo, como un compresor o un antivirus", "Un programa para escribir cartas", "Una pieza de hardware", "Los utilitarios apoyan el trabajo con el equipo."),
        ("abc", "En Programación: ¿qué es el software pirata?", "Un programa usado sin pagar su licencia", "Un programa libre y gratuito", "Un antivirus", "Usarlo es ilegal y además riesgoso."),
        ("abc", "¿Qué tipo de licencia es gratuita por un tiempo limitado?", "La licencia de prueba", "La licencia comercial", "La licencia pirata", "Después del plazo se debe pagar o desinstalar."),
        ("abc", "{F} ¿Qué programa de productividad necesita Marta?", "Un procesador de textos", "Un compresor de archivos", "Un antivirus", "Marta escribe cartas y necesita un procesador."),
        ("abc", "{F} ¿Qué programa de productividad necesita Pablo?", "Una planilla de cálculo", "Un lector de PDF", "Un compresor de archivos", "Pablo hace planillas y necesita una planilla de cálculo."),
        ("abc", "{F} ¿Qué dos utilitarios necesita Ana?", "Un lector de PDF y un compresor de archivos", "Un procesador de textos y una planilla", "Un antivirus y una planilla", "Ana lee PDF y comprime archivos."),
        ("=", "{F} ¿Cuántos tipos de licencia se explican en la ficha?", "3", "Son comercial, libre y de prueba.", " tipos"),
        ("abc", "{F} Un técnico encuentra la planilla de cálculo «gratis» en un sitio desconocido. ¿Qué corresponde?", "Instalar solo la versión del sitio oficial o la que indique la organización", "Descargarla igual", "Reenviar el enlace a Pablo", "Un sitio desconocido puede ofrecer software pirata."),
        ("abc", "{F} ¿Con qué cuenta se instala el programa?", "Con la de administrador, solo para esa tarea", "Con la de Marta usando su contraseña", "Con una cuenta compartida", "El administrador se usa solo para instalar."),
        ("=", "{F} Si cada programa se instala en los equipos que lo necesitan y hay 3 usuarias con 1 equipo cada una, ¿cuántos equipos hay que preparar?", "3*1", "Se multiplican las usuarias por los equipos de cada una.", " equipos"),
        ("abc", "Mientras instala, el técnico ve en el escritorio de Ana archivos personales con fotos. ¿Qué corresponde?", "No abrirlos y seguir con su trabajo", "Abrirlos por curiosidad", "Copiarlos a su pendrive", "El técnico respeta la privacidad de las usuarias."),
        ("abc", "El técnico instala los programas y no anota nada en el inventario. Un año después no se sabe qué licencias hay. ¿Qué faltó?", "El inventario de software", "Más programas", "Una cuenta compartida", "El inventario permite controlar las licencias."),
        ("ab", "{F} Ana pide además un programa para editar videos que no usa en su trabajo. ¿Qué corresponde?", "Preguntar para qué lo necesita y consultar a la jefatura", "Instalarlo sin preguntar", "Se instala solo lo que el trabajo requiere y lo autoriza la jefatura."),
    ],
    ctx=("abc", "El jefe de la oficina de ejemplo dice: «instalemos una copia de la planilla que tiene un amigo, es gratis». ¿Qué responde el técnico?", "Explica el riesgo legal y de seguridad y propone una licencia legítima o un programa libre", "Acepta sin decir nada", "Instala y oculta el origen", "Se informa el riesgo y se propone una alternativa legítima."),
    sc=[
        ("En Programación: ¿qué hace un compresor de archivos?", "Junta archivos en uno más liviano", "Es un programa utilitario de apoyo."),
        ("¿De dónde se instala un programa?", "Del sitio oficial o del canal de la organización", "Así se evitan programas falsos con amenazas."),
        ("¿Qué se anota después de instalar?", "El programa, el equipo y la licencia en el inventario", "Permite controlar las licencias de cada programa."),
    ],
    op=("Una peluquería de ejemplo tiene 2 computadores. Necesitan: llevar la agenda en una planilla, escribir avisos, abrir PDF de proveedores y proteger los equipos. Clasifica cada necesidad como productividad o utilitario, indica qué licencia revisarías y escribe tres cuidados al instalar (origen, cuenta y registro).",
        "Planilla y avisos son de productividad; abrir PDF (lector) y proteger los equipos (antivirus) son utilitarios. Revisaría si cada programa es comercial, libre o de prueba. Cuidados: instalar desde el sitio oficial, usar la cuenta de administrador solo para instalar y anotar el programa, el equipo y la licencia en el inventario.",
        ["clasifica las cuatro necesidades", "menciona la revisión de licencia", "nombra origen, cuenta y registro"],
        ["tabla de necesidades con su tipo y tres cuidados"],
        ["confundir productividad con utilitario", "ignorar la licencia", "no anotar en el inventario"],
        "Pregunta: «¿qué diferencia hay entre un programa de productividad y un utilitario?». Si no responde, pídele que ponga un ejemplo."),
    reinforce="Escribe tres programas de productividad y tres utilitarios que reconozcas.",
    extend="Explica con un ejemplo inventado por qué el software pirata puede salir más caro que una licencia.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 38 (documentos de ejemplo, inventados). Para instalar programas en la «Consultora Aguas Claras» (nombre de ejemplo) se usan estos documentos: solicitud de software (quién lo pide, para qué y con qué justificación); inventario de software (programa, versión, licencia, equipo, fecha); "
     "política de uso aceptable (qué se puede y qué no se puede hacer con los equipos); acuerdo de licencia (condiciones del proveedor); acta de entrega. Inventario de ejemplo: procesador de textos, versión 5.1, 6 licencias compradas, 6 instalaciones; "
     "planilla, versión 3.2, 4 licencias compradas, 5 instalaciones. Verificación de integridad: el proveedor publica una huella (código corto que identifica el archivo) del instalador, y el técnico compara la huella del archivo descargado.")
build(
    O10, 2, F,
    use="Aprenderé los conceptos y documentos para instalar programas (licencias, inventario, huella de verificación) y los roles de quienes participan.",
    prior=["Sé qué son software de productividad y utilitario.", "Sé los tipos de licencia.", "Sé comparar cantidades."],
    explain=[
        "Instalar programas de forma ordenada exige documentos. La solicitud de software dice quién lo pide y para qué. El inventario de software lista cada programa con su versión, su licencia, el equipo y la fecha, y permite comprobar que las instalaciones no superen las licencias compradas. La política de uso aceptable fija qué se puede hacer con los equipos de la organización. El acuerdo de licencia detalla las condiciones del proveedor.",
        "Al descargar un instalador conviene comprobar su integridad: el proveedor publica una huella, un código corto que identifica el archivo exacto. El técnico calcula la huella del archivo descargado y la compara con la publicada; si coinciden, el archivo no fue alterado, y si no coinciden, no se instala. Esto protege contra archivos modificados. Los códigos de esta ficha son ejemplos inventados.",
        "Los roles se reparten: la usuaria o jefatura solicita, la jefatura de TI aprueba, el técnico instala y registra, y el administrador de licencias controla que no haya más instalaciones que licencias. Nadie instala un programa solo porque «lo necesita ahora»: se sigue el proceso para proteger la seguridad y la legalidad.",
    ],
    vocab=[("solicitud de software", "pedido formal de un programa, con su justificación"), ("política de uso aceptable", "reglas de lo que se puede hacer con los equipos"), ("huella de verificación", "código corto que identifica un archivo exacto"), ("integridad", "que el archivo no fue alterado"), ("administrador de licencias", "persona que controla que no haya más instalaciones que licencias"), ("exceso de instalaciones", "más instalaciones que licencias compradas")],
    worked=[
        ("Revisar licencias", "Inventario de ejemplo: un programa tiene 5 licencias y 7 instalaciones. ¿Qué ocurre?", ["Hay más instalaciones que licencias.", "7 menos 5 son 2 instalaciones sin licencia."], "Hay 2 instalaciones en exceso"),
        ("Comparar huellas", "Huella publicada de ejemplo: «A7F3». Huella del archivo descargado: «A7F9». ¿Se instala?", ["Las huellas no coinciden.", "El archivo puede haber sido alterado."], "No, no se instala"),
    ],
    mistakes=[("Instalar un programa desde un archivo sin comparar su huella con la publicada.", "El archivo podría estar alterado y traer programas dañinos.", "Compara las huellas; si no coinciden, no lo instales."),
              ("Aprobar tú mismo tu propia solicitud de software.", "Se pierde el control y la revisión de otra persona.", "La solicitud la aprueba la jefatura de TI.")],
    T=[
        ("abc", "En Programación: ¿qué es la huella de verificación de un archivo?", "Un código corto que identifica el archivo exacto", "La contraseña del programa", "El nombre del proveedor", "Si el archivo cambia, la huella cambia."),
        ("abc", "En Programación: ¿para qué sirve el inventario de software?", "Para controlar qué programas hay y con qué licencia", "Para guardar contraseñas", "Para medir la velocidad del equipo", "Permite comprobar que no haya más instalaciones que licencias."),
        ("abc", "¿Qué dice la política de uso aceptable?", "Qué se puede y qué no se puede hacer con los equipos", "Cuánto cuestan las licencias", "Qué versión tiene cada programa", "Fija las reglas de uso de los equipos."),
        ("=", "{F} ¿Cuántas instalaciones de la planilla exceden sus licencias?", "5-4", "Se restan las licencias a las instalaciones.", " instalación"),
        ("abc", "{F} ¿Qué programa del inventario cumple sus licencias?", "El procesador de textos", "La planilla", "Ninguno", "El procesador tiene 6 licencias y 6 instalaciones."),
        ("abc", "{F} Huella publicada «B21C» y huella calculada «B21C». ¿Qué corresponde?", "Instalar, porque coinciden", "No instalar, porque coinciden", "Pedir la contraseña al proveedor", "Si las huellas coinciden, el archivo es íntegro."),
        ("abc", "{F} Huella publicada «B21C» y huella calculada «B21D». ¿Qué corresponde?", "No instalar y descargar de nuevo desde el sitio oficial", "Instalar igual", "Ignorar la diferencia", "Una diferencia indica que el archivo pudo ser alterado."),
        ("abc", "{F} ¿Qué rol aprueba una solicitud de software?", "La jefatura de TI", "La misma persona que la solicitó", "Un proveedor desconocido", "Otra persona distinta revisa y autoriza."),
        ("=", "{F} Si se compran 2 licencias más de la planilla, ¿cuántas licencias tendrá en total?", "4+2", "Se suman las licencias compradas.", " licencias"),
        ("abc", "{F} Con esas 2 licencias más, ¿cumplirá la planilla sus licencias?", "Sí, 6 licencias para 5 instalaciones", "No, seguirá en exceso", "No se puede saber", "6 licencias alcanzan para 5 instalaciones."),
        ("abc", "Una usuaria instala por su cuenta un programa de música en el equipo de la oficina. ¿Qué documento se incumple?", "La política de uso aceptable", "El acta de entrega", "El inventario de hardware", "La política dice qué programas se pueden instalar."),
        ("abc", "La solicitud de software de ejemplo dice solo «necesito algo para trabajar mejor». ¿Qué le falta?", "Qué programa es y para qué tarea lo necesita", "El nombre completo de su familia", "Su contraseña", "Una solicitud debe tener programa y justificación."),
        ("ab", "{F} La técnica descubre un programa instalado que no figura en el inventario. ¿Qué hace?", "Lo informa y actualiza el inventario con autorización", "Lo borra sin avisar", "Un programa desconocido se informa a la jefatura de TI y se regulariza con registro."),
    ],
    ctx=("abc", "El administrador de licencias de una consultora de ejemplo detecta más instalaciones que licencias. ¿Qué propone?", "Regularizar: comprar licencias o desinstalar los excesos, con respaldo y registro", "Ocultar la diferencia", "Seguir igual", "Se regulariza de forma legal y con registro."),
    sc=[
        ("En Programación: ¿cuándo se instala un archivo según su huella?", "Cuando coincide con la huella publicada", "Si no coincide, puede estar alterado."),
        ("¿Quién aprueba una solicitud de software?", "La jefatura de TI", "Otra persona distinta de quien la pide."),
        ("¿Qué compara el inventario de software?", "Instalaciones contra licencias", "No debe haber más instalaciones que licencias."),
    ],
    op=("Inventario de ejemplo de una escuela: lector de PDF, 10 licencias, 10 instalaciones; editor de imágenes, 3 licencias, 5 instalaciones. Huella publicada del instalador del lector «C5D1» y huella calculada «C5D1»; del editor, publicada «E9A0» y calculada «E9A8». Indica qué programa cumple las licencias, cuántas instalaciones sobran, qué instalador puedes instalar y qué documentos usarías para regularizar.",
        "El lector cumple (10 y 10). El editor tiene 2 instalaciones en exceso (5 − 3). El instalador del lector se puede instalar porque las huellas coinciden; el del editor no coincide y no se instala. Para regularizar usaría la solicitud de software y el inventario, y registraría en el acta y la bitácora.",
        ["calcula el exceso de instalaciones", "decide con las huellas", "nombra documentos de regularización"],
        ["hoja con los cálculos, las decisiones y los documentos"],
        ["restar al revés", "instalar con huella distinta", "no nombrar documentos"],
        "Pregunta: «¿qué haces con el instalador que no coincide?». Si no responde, pídele que relea la regla de integridad."),
    reinforce="Haz un inventario con tres programas inventados, sus licencias e instalaciones, y marca el exceso.",
    extend="Explica con un ejemplo inventado por qué una huella distinta puede ser señal de un archivo alterado.",
)

# ============================================================ OAE-10, clase 3
F = ("Ficha 39 (caso de ejemplo, inventado). Requerimientos de tres personas de la «Notaría de ejemplo Los Maitenes» y programas candidatos (datos de ejemplo). Lucía: redactar escritos y cartas. Mario: hacer una planilla de pagos con cálculos. Elsa: abrir PDF y comprimir archivos para enviar por correo. "
     "Candidatos: Programa 1, suite de oficina comercial (procesador, planilla y presentaciones), $15.000 al mes por usuario. Programa 2, suite de oficina libre (procesador, planilla y presentaciones), $0. "
     "Programa 3, lector de PDF libre, $0. Programa 4, compresor de archivos libre, $0. Presupuesto mensual de ejemplo: $40.000. Condición: todos los programas deben ser de licencia legítima.")
build(
    O10, 3, F,
    use="Aprenderé a analizar en papel qué programas cubren los requerimientos de cada usuaria, comparando costos y licencias.",
    prior=["Sé qué son software de productividad y utilitarios.", "Sé qué es una licencia legítima.", "Sé calcular costos mensuales."],
    explain=[
        "Elegir software es hacer corresponder cada requerimiento con un programa. Se escribe una tabla con las personas, lo que necesitan y qué candidatos lo cubren. Un requerimiento se cubre solo si el programa realmente realiza esa tarea. Un solo programa puede cubrir varios requerimientos, como una suite de oficina que incluye procesador de textos y planilla.",
        "Se comparan los costos y se verifica que la licencia sea legítima. Una licencia comercial se paga, y una licencia libre se usa según sus condiciones sin pagar. El costo total mensual es el costo por usuario por la cantidad de usuarios. Se prefiere la opción que cubre todos los requerimientos, cabe en el presupuesto y se puede mantener de forma legal. Si hay empate, se desempata con el soporte disponible y la capacitación necesaria.",
        "La decisión se escribe con evidencia (qué requerimiento cubre cada programa y cuánto cuesta) y se revisa si cambia una condición, como el presupuesto o el número de usuarios. La decisión final es de la jefatura. Si hay datos personales en los documentos de las usuarias, el programa se configura para cuidarlos y no se envían por canales abiertos.",
    ],
    vocab=[("cubrir un requerimiento", "que el programa realice la tarea que se necesita"), ("suite de oficina", "conjunto de programas de oficina: textos, planilla y presentaciones"), ("licencia legítima", "licencia obtenida de forma legal"), ("costo total mensual", "costo por usuario por la cantidad de usuarios"), ("capacitación", "enseñanza para usar un programa")],
    worked=[
        ("Costo mensual", "Una suite comercial de ejemplo cuesta $10.000 al mes por usuario y la usarán 3 personas. ¿Cuánto cuesta al mes?", ["Se multiplica el costo por usuario por la cantidad de usuarios.", "10.000 por 3."], "$30.000"),
        ("Cubrir requerimientos", "Una persona necesita escribir y hacer planillas. La suite de ejemplo incluye procesador y planilla. ¿Cubre ambos?", ["Procesador cubre escribir.", "Planilla cubre las planillas."], "Sí, cubre ambos requerimientos"),
    ],
    mistakes=[("Elegir el programa más caro creyendo que es el mejor.", "Un precio alto no garantiza que cubra mejor el requerimiento.", "Compara qué tareas cubre y cuánto cuesta."),
              ("Elegir un programa «gratis» de un sitio desconocido por ahorrar.", "Puede ser software pirata o traer programas dañinos.", "Elige licencias legítimas: comerciales o libres de fuente oficial.")],
    T=[
        ("abc", "En Programación: ¿qué es una suite de oficina?", "Un conjunto de programas de oficina como textos y planilla", "Un solo compresor de archivos", "Un tipo de licencia pirata", "Una suite agrupa varios programas de productividad."),
        ("abc", "En Programación: ¿qué es una licencia legítima?", "Una licencia obtenida de forma legal", "Una copia sin pagar", "Un archivo comprimido", "La legitimidad evita problemas legales y de seguridad."),
        ("abc", "{F} ¿Qué programa cubre el requerimiento de Lucía?", "Programa 1 o Programa 2, porque incluyen procesador de textos", "Solo Programa 3", "Solo Programa 4", "Lucía redacta, y ambas suites incluyen procesador."),
        ("abc", "{F} ¿Qué programa cubre el requerimiento de Mario?", "Programa 1 o Programa 2, porque incluyen planilla", "Programa 3", "Programa 4", "Mario necesita una planilla con cálculos."),
        ("abc", "{F} ¿Qué dos programas cubren los requerimientos de Elsa?", "Programa 3 y Programa 4", "Programa 1 y Programa 2", "Programa 2 y Programa 3 solamente", "Elsa abre PDF con el lector y comprime con el compresor."),
        ("=", "{F} Si las tres personas usan la suite comercial (Programa 1), ¿cuánto cuesta al mes?", "15000*3", "Se multiplica el costo por usuario por las tres personas.", " pesos"),
        ("abc", "{F} ¿Cabe esa opción en el presupuesto mensual?", "No, cuesta $45.000 y el presupuesto es $40.000", "Sí, cuesta menos de $40.000", "Sí, justo cuesta $40.000", "45.000 supera el presupuesto de 40.000."),
        ("=", "{F} Si Lucía y Mario usan el Programa 1 y Elsa usa solo los programas 3 y 4, ¿cuánto cuesta al mes?", "15000*2", "Solo Lucía y Mario pagan licencia comercial; los otros son libres.", " pesos"),
        ("abc", "{F} ¿Cabe esa opción en el presupuesto?", "Sí, cuesta $30.000", "No, cuesta más de $40.000", "No, cuesta $45.000", "30.000 es menor que el presupuesto de 40.000."),
        ("=", "{F} Si todos usan el Programa 2 (suite libre) y los programas 3 y 4, ¿cuánto cuesta al mes?", "0", "Los programas de la opción son libres y su costo es cero.", " pesos"),
        ("abc", "{F} Elsa dice: «instalemos otro lector de PDF que me pasó una amiga en un pendrive». ¿Qué corresponde?", "No instalarlo; usar el Programa 3 oficial, autorizado por la organización", "Instalarlo porque es gratis", "Compartirlo con todos", "Un archivo de origen desconocido es un riesgo de seguridad."),
        ("abc", "{F} Si el presupuesto bajara a $20.000, ¿qué opción de las analizadas cumpliría todo?", "Programa 2 (suite libre) con los programas 3 y 4", "Programa 1 para las tres", "Ninguna opción cumple", "Cuesta $0 y cubre todos los requerimientos."),
        ("ab", "{F} Mario pide una función que ninguno de los programas candidatos incluye. ¿Qué corresponde?", "Informar a la jefatura y evaluar otras opciones", "Instalar un programa sin licencia", "Si ningún candidato cubre la función, se informa y se evalúa otro programa legítimo."),
    ],
    ctx=("abc", "La jefa de la notaría de ejemplo pregunta: «¿Por qué no usamos solo el más barato?». El técnico responde...", "Que el más barato debe cubrir todos los requerimientos y tener licencia legítima", "Que el más caro es siempre mejor", "Que la licencia no importa", "El criterio es cubrir requerimientos de forma legal y dentro del presupuesto."),
    sc=[
        ("En Programación: ¿cómo se calcula el costo mensual de una suite comercial?", "Costo por usuario por cantidad de usuarios", "El costo se compara con el presupuesto disponible."),
        ("¿Qué debe tener un programa para aceptarse?", "Cubrir el requerimiento y tener licencia legítima", "Ambas condiciones son obligatorias para aceptar un programa."),
        ("¿Quién decide la compra?", "La jefatura", "El técnico entrega el análisis, pero decide la jefatura."),
    ],
    op=("Un taller de ejemplo tiene tres usuarias: Sofía (cartas), Raúl (planilla) y Clara (comprimir archivos y abrir PDF). Candidatos: Programa A, suite comercial $12.000 al mes por usuario; Programa B, suite libre $0; Programa C, lector de PDF libre $0; Programa D, compresor libre $0. Presupuesto $30.000. Escribe una tabla de requerimientos y programas, calcula el costo de dos opciones y elige una justificándola.",
        "Sofía y Raúl se cubren con la suite A o B; Clara con C y D. Opción 1: A para Sofía y Raúl (24.000) más C y D (0) = 24.000, cabe. Opción 2: B para Sofía y Raúl más C y D = 0, cabe. Elijo la opción 2 si cubre lo necesario, porque cuesta $0 y tiene licencia libre legítima; si necesitaran una función exclusiva de A, la opción 1 también cabe.",
        ["relaciona cada usuaria con su programa", "calcula el costo de dos opciones", "justifica la elección con costo y licencia"],
        ["tabla de requerimientos y programas con los dos costos"],
        ["asignar el compresor a Sofía", "calcular mal el costo", "elegir sin justificar"],
        "Pregunta: «¿qué dato respalda tu elección?». Si no responde, pídele que muestre los costos de las dos opciones."),
    reinforce="Escribe tres necesidades de una tienda de ejemplo y el programa que cubriría cada una.",
    extend="Explica con un ejemplo inventado cómo cambiaría tu elección si el presupuesto se redujera a la mitad.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 40 (decisiones de ejemplo, inventadas) de la «Oficina Contable Los Cipreses». Solicitudes recibidas: (S1) una usuaria pide instalar un editor de imágenes comercial descargado de un sitio que dice «versión gratis completa»; "
     "(S2) una usuaria pide un compresor libre del sitio oficial, con huella publicada «F302» y huella del archivo descargado «F302»; (S3) una usuaria pide una suite de oficina comercial con 4 licencias compradas y 3 instalaciones actuales. "
     "Costo anual de ejemplo: suite comercial $10.000 al mes por usuario, con 4 usuarios. Capacitación de ejemplo: 2 sesiones de 1 hora por usuario. Regla: instalar solo con licencia legítima, fuente oficial, huella coincidente, autorización y registro.")
build(
    O10, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo para aprobar o rechazar solicitudes de instalación y calcular costos con seguridad.",
    prior=["Sé qué es una licencia legítima, la huella de verificación y el inventario.", "Sé calcular costos mensuales y anuales.", "Sé qué es una solicitud de software."],
    explain=[
        "El criterio técnico para instalar software combina cuatro condiciones: licencia legítima, fuente oficial, integridad comprobada (huella coincidente) y autorización con registro. Si falta alguna, la solicitud se rechaza o se devuelve para corregirla. Una solicitud que parece conveniente, pero no cumple estas condiciones, se rechaza explicando el riesgo y ofreciendo una alternativa legítima.",
        "Los cálculos de apoyo son simples. El costo anual es el costo mensual por la cantidad de usuarios por 12 meses. El número de licencias disponibles es las compradas menos las instaladas. El tiempo de capacitación es las sesiones por usuario por la cantidad de usuarios. Estos números permiten planificar, aunque la decisión también considera la seguridad y las necesidades del trabajo.",
        "Después de instalar, se entrega un acta, se capacita a las personas para usar el programa con seguridad (no abrir archivos desconocidos, no compartir licencias, guardar sus trabajos) y se registra todo en el inventario. Si el programa se desinstala, se respaldan antes los archivos que dependan de él. Los datos personales de las usuarias no se copian.",
    ],
    vocab=[("fuente oficial", "sitio o canal autorizado por el proveedor"), ("licencia disponible", "licencia comprada que aún no se usa"), ("costo anual", "costo mensual por usuarios por 12 meses"), ("rechazar una solicitud", "no aprobarla explicando el motivo"), ("alternativa legítima", "opción legal y segura que cubre la misma necesidad")],
    worked=[
        ("Licencias disponibles", "Un programa de ejemplo tiene 6 licencias compradas y 4 instalaciones. ¿Cuántas licencias quedan disponibles?", ["Disponibles = compradas menos instaladas.", "6 − 4."], "2"),
        ("Rechazar con alternativa", "Una usuaria pide un programa comercial «crackeado» (sin pagar licencia). ¿Qué hace el técnico?", ["No cumple la regla de licencia legítima.", "Lo rechaza y ofrece una alternativa legal."], "Rechaza y propone una alternativa legítima"),
    ],
    mistakes=[("Aprobar una solicitud porque «el programa es muy bueno» sin revisar la fuente ni la licencia.", "La calidad del programa no compensa el riesgo de que sea pirata o esté alterado.", "Revisa las cuatro condiciones antes de aprobar."),
              ("Desinstalar un programa sin respaldar los archivos que dependen de él.", "Se pueden perder trabajos que solo ese programa abre.", "Respalda antes de desinstalar.")],
    T=[
        ("abc", "En Programación: ¿qué es una fuente oficial de un programa?", "El sitio o canal autorizado por el proveedor", "Cualquier sitio que lo ofrece gratis", "Un mensaje de una amiga", "La fuente oficial reduce el riesgo de archivos alterados."),
        ("abc", "En Programación: ¿qué es una alternativa legítima?", "Una opción legal y segura que cubre la misma necesidad", "Una copia sin licencia más barata", "Un programa de origen dudoso", "Se ofrece al rechazar una solicitud riesgosa."),
        ("abc", "{F} ¿Qué corresponde con la solicitud S1?", "Rechazarla y ofrecer una alternativa legítima", "Aprobarla porque dice «gratis»", "Instalarla y anotarla después", "Una versión «gratis completa» de un sitio no oficial suele ser pirata."),
        ("abc", "{F} ¿Qué corresponde con la solicitud S2?", "Aprobarla: fuente oficial, huellas coincidentes, con autorización y registro", "Rechazarla por ser libre", "Rechazarla porque la huella coincide", "Cumple las condiciones de la regla."),
        ("=", "{F} Para la solicitud S3, ¿cuántas licencias disponibles quedan?", "4-3", "Se restan las instalaciones a las licencias compradas.", " licencia"),
        ("abc", "{F} ¿Se puede aprobar S3 si cumple las demás condiciones de la regla (fuente oficial, huella coincidente, autorización y registro)?", "Sí, hay una licencia disponible", "No, las licencias se agotaron", "No, el programa es comercial", "Hay 4 compradas y 3 instaladas; queda una."),
        ("=", "{F} ¿Cuánto cuesta al año la suite comercial para los 4 usuarios?", "10000*4*12", "Se multiplica el costo mensual por usuario, los usuarios y 12 meses.", " pesos"),
        ("=", "{F} ¿Cuántas horas de capacitación se necesitan en total para los 4 usuarios?", "2*1*4", "Son 2 sesiones de 1 hora por usuario, por 4 usuarios.", " horas"),
        ("abc", "{F} El técnico quiere calcular la huella de S2 y recibe «F30Z». ¿Qué debe hacer?", "No instalar y descargar de nuevo desde la fuente oficial", "Instalar igual", "Ignorar la diferencia", "No coincide con la huella publicada «F302»."),
        ("abc", "{F} Antes de desinstalar un programa que ya no se usa, ¿qué conviene hacer?", "Respaldar los archivos que dependen de él", "Borrar el respaldo", "Pedir la contraseña de la usuaria", "Así se evita perder trabajos de las usuarias."),
        ("=", "Una oficina de ejemplo tiene 25 solicitudes de software al año y rechaza 4 por no cumplir la regla. ¿Cuántas aprueba?", "25-4", "Se restan las rechazadas al total.", " solicitudes"),
        ("abc", "La usuaria de S1 dice que el sitio tiene muchas reseñas positivas. ¿Qué responde el técnico?", "Que las reseñas no reemplazan la licencia legítima ni la fuente oficial", "Que entonces se instala", "Que la reseña vale más que la regla", "La regla se basa en la legitimidad y la integridad."),
        ("ab", "{F} Se capacita a las usuarias para no compartir su licencia con nadie. ¿Por qué?", "Porque compartirla incumple las condiciones de la licencia y expone la cuenta", "Porque cuesta más", "Una licencia suele ser personal o limitada y compartirla incumple el acuerdo."),
    ],
    ctx=("abc", "El dueño de la oficina de ejemplo presiona para instalar rápido el editor de S1 porque «el cliente lo exige hoy». ¿Qué hace la jefatura de TI?", "Mantiene la regla, explica el riesgo y propone una alternativa legítima rápida", "Instala el editor sin revisar", "Oculta el origen del programa", "La regla no se salta por presión; se busca una alternativa."),
    sc=[
        ("En Programación: ¿cuáles son las condiciones para instalar un programa?", "Licencia legítima, fuente oficial, huella coincidente, autorización y registro", "Si falta una, se rechaza o se corrige."),
        ("¿Cómo se calculan las licencias disponibles?", "Compradas menos instaladas", "Se revisa en el inventario de software."),
        ("¿Qué se hace antes de desinstalar?", "Respaldar los archivos que dependen del programa", "Así se evita perder trabajos de las usuarias."),
    ],
    op=("Una escuela de ejemplo recibe tres solicitudes: (S1) un reproductor de video descargado de un enlace enviado por un mensaje, sin huella; (S2) un lector de PDF libre del sitio oficial, huella publicada «A10B» y calculada «A10B»; (S3) una suite comercial, con 5 licencias compradas y 5 instaladas. Decide cada una con la regla de la ficha y calcula el costo anual de 3 licencias nuevas de la suite a $9.000 al mes por usuario.",
        "S1: se rechaza (fuente no oficial y sin huella) y se ofrece una alternativa legítima. S2: se aprueba (fuente oficial, huellas coinciden) con autorización y registro. S3: no se aprueba hasta comprar más licencias (5 − 5 = 0 disponibles). Costo anual de 3 licencias: 9.000 × 3 × 12 = 324.000 pesos.",
        ["decide cada solicitud con la regla", "calcula las licencias disponibles y el costo anual", "ofrece una alternativa legítima"],
        ["tabla de tres solicitudes con su decisión y el cálculo"],
        ["aprobar S1", "no calcular los 12 meses", "ignorar que no hay licencias disponibles"],
        "Pregunta: «¿qué falta en la solicitud S1?». Si no responde, pídele que revise fuente, huella y licencia."),
    reinforce="Escribe cuatro condiciones que debe cumplir un programa para instalarse en una oficina de ejemplo.",
    extend="Explica con un ejemplo inventado por qué una presión por rapidez no justifica saltarse la regla de licencia.",
)

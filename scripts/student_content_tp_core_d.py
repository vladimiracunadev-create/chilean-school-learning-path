"""Conectividad y Redes TP 3.º y 4.º medio: OAE-10 (mantener actualizado el software de productividad y utilitarios) y OAE-11 (armar y configurar un equipo personal, solo conceptos). Equipos, versiones y precios inventados; sin software ni equipos reales."""
from __future__ import annotations

from tp_core_common import build

O10 = "TP-CORE-3y4-OAE-10"
O11 = "TP-CORE-3y4-OAE-11"
AVISO = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-10, clase 1
F = ("Ficha 1 (oficina de ejemplo, inventada). «Estudio Rayén» tiene 15 computadores con programas de productividad (procesador de textos, planilla de cálculo, presentaciones), un lector de documentos PDF, un compresor de archivos y un antivirus. "
     "Hay 15 licencias de ofimática compradas y 17 instalaciones de ese programa (algunos equipos lo tienen instalado dos veces), es decir, 2 instalaciones de más. De los 15 computadores, 12 tienen versiones antiguas. Roles: personas usuarias y administradora de informática. "
     "Reglas (de ejemplo): instalar solo desde la fuente oficial, hacer un respaldo antes de actualizar y registrar los cambios.")
build(
    O10, 1, F,
    use="Aprenderé por qué se mantienen actualizados el software de productividad y los programas utilitarios, quién decide, qué riesgos hay y qué reglas se siguen.",
    prior=["Sé usar un procesador de textos y una planilla.", "Sé qué es una licencia.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El software de productividad son los programas con que se trabaja: procesador de textos, planilla de cálculo, presentaciones. Los programas utilitarios ayudan al equipo: antivirus, lector de PDF, compresor de archivos. Mantenerlos actualizados significa instalar las versiones nuevas que corrigen fallas y problemas de seguridad, o que agregan funciones que las personas necesitan.",
        "Actualizar no es solo instalar lo más nuevo. Se hace según los requerimientos de las personas usuarias, con una licencia vigente, desde la fuente oficial del programa y después de respaldar la información. Se registra qué se cambió y cuándo. Usar programas sin licencia o desde sitios desconocidos pone en riesgo los datos y vulnera los derechos de autor.",
        "Los riesgos son instalar programas dañinos, perder datos por una actualización fallida, tener versiones incompatibles que no abren los archivos y descuidar la ergonomía durante el trabajo. En esta clase solo se aprenden conceptos y razonamiento; los equipos reales se actualizan con la autorización de la administradora de informática.",
    ],
    vocab=[("software de productividad", "programas para trabajar con documentos, planillas y presentaciones"), ("programa utilitario", "programa de apoyo al equipo, como un antivirus"), ("actualización", "instalación de una versión nueva de un programa"), ("fuente oficial", "sitio o medio autorizado por el fabricante del programa"), ("licencia", "permiso legal de uso de un programa"), ("respaldo", "copia de la información antes de un cambio")],
    worked=[
        ("Porcentaje desactualizado", "En una oficina de ejemplo, 6 de 20 equipos tienen versión antigua. ¿Qué porcentaje es?", ["Se divide 6 entre 20 y se multiplica por 100.", "6 × 100 ÷ 20 = 30."], "30 %"),
        ("Qué hacer antes de actualizar", "Una persona usuaria tiene archivos importantes en su equipo y se va a actualizar la ofimática. ¿Qué se hace antes?", ["La actualización puede fallar y afectar archivos.", "Se hace un respaldo y se pide autorización."], "Respaldo y autorización"),
    ],
    mistakes=[("Descargar el instalador desde un sitio desconocido porque «aparece primero en el buscador».", "Puede contener programas dañinos o ser una versión falsa.", "Usa solo la fuente oficial o el servidor de la institución."),
              ("Actualizar sin respaldar.", "Si algo falla pueden perderse archivos.", "Respalda y registra antes de actualizar.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el software de productividad?", "Programas para trabajar con documentos, planillas y presentaciones", "Piezas físicas del computador", "Cables y conectores", "El software de productividad es el que usan las personas para su trabajo diario."),
        ("abc", "En Conectividad y Redes: ¿qué es un programa utilitario?", "Un programa de apoyo al equipo, como un antivirus", "Un programa solo para juegos", "Un cable de red", "Los utilitarios ayudan al funcionamiento y la seguridad del equipo."),
        ("abc", "¿Por qué se mantienen actualizados los programas?", "Para corregir fallas y problemas de seguridad y atender los requerimientos de las personas", "Para que el computador cambie de color", "Para gastar más internet", "Las actualizaciones corrigen errores y agregan lo que se necesita."),
        ("=", "{F} ¿Qué porcentaje de los 15 computadores tiene versiones antiguas?", "12*100//15", "Se calcula la parte de equipos antiguos respecto del total.", " %"),
        ("=", "{F} ¿Cuántos computadores están al día?", "15-12", "Al total se le restan los equipos con versión antigua.", " equipos"),
        ("abc", "{F} ¿De dónde se debe descargar un instalador según las reglas del estudio?", "De la fuente oficial", "Del primer sitio que aparezca en el buscador", "De un enlace recibido por un mensaje desconocido", "La regla indica instalar solo desde la fuente oficial."),
        ("=", "{F} Hay 17 instalaciones y 15 licencias de ofimática. ¿Cuántas instalaciones exceden las licencias?", "17-15", "A las instalaciones se les restan las licencias compradas.", " instalaciones"),
        ("abc", "{F} ¿Por qué se hace un respaldo antes de actualizar?", "Porque si la actualización falla podrían perderse archivos", "Porque la actualización es más rápida", "Porque así no se necesita licencia", "El respaldo protege la información ante un fallo."),
        ("abc", "{F} Una persona usuaria dice: «con un instalador de un sitio desconocido ahorro tiempo». ¿Qué respondes?", "Puede traer programas dañinos; se usa la fuente oficial", "Tiene razón, es más rápido", "Basta con borrar el instalador después", "Un instalador desconocido es un riesgo para los datos del estudio."),
        ("abc", "{F} Se descubre una instalación sin licencia. ¿Qué corresponde?", "Avisar a la administradora para regularizar la licencia o retirar el programa", "Ocultarlo para que nadie lo vea", "Instalarlo en más equipos", "Usar software sin licencia vulnera los derechos de autor."),
        ("abc", "Una administradora instala un programa copiado «porque es igual al original». ¿Qué principio se vulnera?", "Los derechos de autor y las reglas de licencia", "La ergonomía", "El cableado horizontal", "Usar copias sin permiso vulnera los derechos del autor."),
        ("=", "{F} Si se actualizan 4 equipos por semana, ¿cuántas semanas se necesitan para los 12 equipos antiguos?", "12//4", "Se divide el total de equipos antiguos por los de cada semana.", " semanas"),
        ("abc", "{F} Una persona usuaria trabaja sin pausas mientras espera una actualización larga. ¿Qué recomendación aplica?", "Aprovechar la espera para una pausa y cuidar la postura", "Seguir trabajando sin moverse", "Apagar el equipo en medio de la actualización", "La espera puede usarse para descansar sin interrumpir la actualización."),
    ],
    ctx=("abc", "Una usuaria te pide instalar un programa que descargó de un sitio desconocido para «comprimir archivos más rápido». ¿Qué respondes?", "Que no se instala desde fuentes desconocidas y que la administradora puede indicar el compresor autorizado", "Que lo instalas de inmediato", "Que lo instalas en todos los equipos", "Se usa la herramienta autorizada y se evita el riesgo de programas dañinos."),
    sc=[
        ("En Conectividad y Redes: ¿qué se hace antes de actualizar un equipo?", "Respaldar y obtener autorización", "La actualización puede fallar y afectar archivos."),
        ("¿De dónde se descarga un instalador?", "De la fuente oficial o del servidor de la institución", "Así se evita software dañino o falso."),
        ("¿Qué se registra al actualizar?", "Qué se cambió, cuándo y quién", "Sirve para revisar y volver atrás si algo falla."),
    ],
    op=("Una veterinaria de ejemplo tiene 20 computadores; 8 tienen el antivirus desactualizado y 18 instalaciones de ofimática para 16 licencias. Calcula el porcentaje de equipos con antivirus antiguo, cuántas instalaciones exceden las licencias y escribe tres reglas para mantener el software al día.",
        "Porcentaje: 8 × 100 ÷ 20 = 40 %. Exceso: 18 − 16 = 2 instalaciones. Reglas: instalar solo desde la fuente oficial; respaldar antes de actualizar; registrar los cambios y las licencias.",
        ["calcula el porcentaje y el exceso", "escribe tres reglas útiles", "incluye licencia y respaldo"],
        ["hoja con cálculos y tres reglas"],
        ["calcular el porcentaje sobre el dato equivocado", "proponer un sitio desconocido", "olvidar el respaldo"],
        "Pregunta: «¿por qué respaldas?». Si no puede responder, repasa qué pasa si una actualización falla."),
    reinforce="Lista cinco programas de tu entorno y anota si son de productividad o utilitarios.",
    extend="Explica por qué las licencias protegen tanto a quien crea el programa como a quien lo usa.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 2 (glosario e inventario de ejemplo). Versión: número que identifica una edición de un programa; se comparan de izquierda a derecha, así que 4.1 es mayor que 4.0 y 6.9 es menor que 7.0. "
     "Actualización menor (parche): corrige fallas o problemas de seguridad. Actualización mayor: agrega funciones o cambia la forma de usar el programa. Licencia: permiso de uso. Inventario de software: lista de programas instalados con su versión y su licencia. "
     "Compatibilidad de archivos: poder abrir un archivo creado con otra versión. Huella del instalador: valor que permite verificar que el archivo no fue alterado. Ventana de mantenimiento: horario acordado para actualizar. Reversión: volver a la versión anterior si algo falla. "
     "Inventario de ejemplo de la ofimática: E1, versión 4.2, licencia vigente; E2, versión 4.0, licencia vigente; E3, versión 4.2, sin licencia; E4, versión 3.9, licencia vigente.")
build(
    O10, 2, F,
    use="Aprenderé el vocabulario del mantenimiento del software (versión, parche, inventario, compatibilidad, reversión) y los documentos que se usan.",
    prior=["Sé por qué se actualizan los programas.", "Sé qué es una licencia.", "Sé comparar números de versión."],
    explain=[
        "Cada programa tiene una versión que lo identifica. Las versiones se comparan de izquierda a derecha: 4.1 es más nueva que 4.0, y 7.0 es más nueva que 6.9. Una actualización menor, o parche, corrige fallas o problemas de seguridad y suele instalarse pronto. Una actualización mayor agrega funciones o cambia la forma de usar el programa, y requiere más cuidado porque puede cambiar menús o formatos de archivo.",
        "El inventario de software es la lista de programas instalados, con su versión y su licencia, equipo por equipo. Permite ver qué está desactualizado y qué no tiene licencia. La compatibilidad de archivos es poder abrir un archivo creado con otra versión; si no se cuida, una persona puede quedar sin acceso a sus documentos. La huella del instalador permite comprobar que el archivo descargado no fue alterado.",
        "Las actualizaciones se hacen en una ventana de mantenimiento acordada con las personas usuarias, con respaldo previo y con la posibilidad de volver a la versión anterior (reversión) si algo falla. Todo se anota en un registro de cambios.",
    ],
    vocab=[("versión", "número que identifica una edición de un programa"), ("parche", "actualización menor que corrige fallas o seguridad"), ("actualización mayor", "actualización que agrega funciones o cambia el uso"), ("inventario de software", "lista de programas con versión y licencia por equipo"), ("compatibilidad de archivos", "poder abrir archivos creados con otra versión"), ("reversión", "volver a la versión anterior si algo falla"), ("ventana de mantenimiento", "horario acordado para actualizar")],
    worked=[
        ("Comparar versiones", "¿Cuál es más nueva: la versión 3.9 o la 4.0?", ["Se compara de izquierda a derecha.", "3 es menor que 4, así que 4.0 es más nueva."], "La versión 4.0"),
        ("Equipo sin licencia", "En un inventario de ejemplo un equipo tiene la versión 5.0 y no tiene licencia. ¿Qué corresponde?", ["Usar el programa sin licencia vulnera los derechos de autor.", "Se avisa a la administradora para regularizar o retirar el programa."], "Avisar para regularizar o retirar"),
    ],
    mistakes=[("Creer que 4.10 es menor que 4.9 porque 10 «parece» menor que 9.", "Las partes de la versión se comparan como números enteros: 10 es mayor que 9.", "Compara parte por parte de izquierda a derecha, como números."),
              ("Instalar una actualización mayor sin probar la compatibilidad de los archivos.", "Puede que algunos archivos importantes no abran.", "Prueba primero con copias en un equipo de prueba.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una versión de un programa?", "El número que identifica una edición del programa", "El precio del programa", "El nombre del dueño del programa", "La versión permite saber qué edición está instalada."),
        ("abc", "En Conectividad y Redes: ¿qué es la reversión?", "Volver a la versión anterior si algo falla", "Instalar tres veces el mismo programa", "Borrar el inventario", "La reversión es el plan B ante una actualización fallida."),
        ("abc", "¿Qué es un inventario de software?", "La lista de programas instalados con su versión y licencia", "La lista de claves del personal", "La lista de cables del rack", "El inventario permite ver qué falta actualizar o licenciar."),
        ("abc", "{F} ¿Qué equipos del inventario tienen la versión más reciente (4.2)?", "E1 y E3", "E1 y E2", "E2 y E4", "E1 y E3 tienen 4.2; E2 tiene 4.0 y E4 tiene 3.9."),
        ("abc", "{F} ¿Qué equipo no tiene licencia?", "E3", "E1", "E4", "El inventario indica «sin licencia» para E3."),
        ("abc", "{F} ¿Qué equipo tiene la versión más antigua?", "E4, con 3.9", "E2, con 4.0", "E1, con 4.2", "3.9 es menor que 4.0 y que 4.2."),
        ("abc", "{F} Si la versión mínima aceptada es 4.0, ¿qué equipos del inventario NO cumplen?", "Solo E4", "E2 y E4", "E1 y E3", "3.9 es menor que 4.0; las demás versiones son iguales o mayores."),
        ("abc", "{F} Una actualización corrige una falla grave de seguridad sin cambiar nada visible. ¿Qué tipo es?", "Una actualización menor o parche", "Una actualización mayor", "Una licencia nueva", "Corregir fallas sin cambiar el uso es lo propio de un parche."),
        ("abc", "{F} E3 no tiene licencia. ¿Qué corresponde?", "Avisar a la administradora para regularizar la licencia o retirar el programa", "Usarlo igual porque es la versión más nueva", "Copiarlo a los demás equipos", "La versión nueva no reemplaza la licencia."),
        ("abc", "{F} Un usuario dice: «mi versión es la más nueva, así que no necesito licencia». ¿Qué respondes?", "La licencia es un permiso de uso y no depende de la versión", "Tiene razón", "La licencia solo sirve para versiones antiguas", "Tener la versión más nueva no da permiso de uso por sí solo."),
        ("abc", "{F} La huella publicada del instalador coincide con la del archivo descargado. ¿Qué indica?", "Que el archivo no fue alterado", "Que el programa es gratuito", "Que no hace falta licencia", "Huellas iguales indican que el contenido es el mismo."),
        ("abc", "{F} Una actualización mayor cambia el formato de archivos. ¿Qué conviene hacer antes de instalarla en todos los equipos?", "Probarla con copias de los archivos en un equipo de prueba y respaldar", "Instalarla en todos sin avisar", "Borrar los archivos antiguos", "La prueba previa detecta problemas de compatibilidad sin riesgo."),
        ("=", "{F} Una actualización tarda 20 minutos por equipo y hay que actualizar 3 equipos. ¿Cuántos minutos son en total?", "20*3", "Se multiplican los minutos de cada equipo por la cantidad de equipos.", " minutos"),
    ],
    ctx=("abc", "El equipo de contabilidad de ejemplo usa plantillas creadas hace años. Hay una actualización mayor de la ofimática. ¿Qué haces?", "Probarla antes con las plantillas en un equipo de prueba y respaldarlas", "Instalarla en todos los equipos de inmediato", "Prohibir las plantillas", "La compatibilidad con el trabajo real de las personas es un requerimiento."),
    sc=[
        ("En Conectividad y Redes: ¿qué es un parche?", "Una actualización menor que corrige fallas o seguridad", "Suele instalarse pronto y con poco riesgo."),
        ("¿Qué indica el inventario?", "Programas, versión y licencia de cada equipo", "Permite detectar lo desactualizado y lo sin licencia."),
        ("¿Qué es la reversión?", "Volver a la versión anterior si algo falla", "Reduce el riesgo de una actualización."),
    ],
    op=("Inventario de ejemplo del antivirus: E1, versión 7.2, con licencia; E2, versión 6.9, con licencia; E3, versión 7.0, sin licencia; E4, versión 7.1, con licencia. Versión mínima aceptada: 7.0. Indica qué equipos cumplen la versión, qué equipo tiene un problema de licencia, cuántos equipos necesitan actualización y cuántos minutos tomaría si cada actualización tarda 15 minutos.",
        "Cumplen la versión: E1, E3 y E4 (7.2, 7.0 y 7.1). E2 (6.9) no cumple. Problema de licencia: E3. Necesitan actualización: 1 equipo (E2) y 15 minutos. E3 debe regularizar la licencia con la administradora.",
        ["compara las versiones con el mínimo", "detecta el equipo sin licencia", "calcula el tiempo"],
        ["tabla con cada equipo y su estado, más el cálculo"],
        ["decir que 6.9 cumple", "ignorar la licencia de E3", "multiplicar mal los minutos"],
        "Pregunta: «¿por qué 7.0 cumple el mínimo de 7.0?». Si dice que no, recuérdale que el mínimo se cumple al igualarlo."),
    reinforce="Escribe un inventario de ejemplo de tres programas para un equipo, con versión y licencia.",
    extend="Explica por qué una huella del instalador ayuda a evitar programas falsos.",
)

# ============================================================ OAE-10, clase 3
F = ("Ficha 3 (inventario de ejemplo de 6 equipos). Versiones mínimas del estudio: ofimática 4.1; antivirus 7.0; lector PDF 2.5. Las versiones se comparan de izquierda a derecha (4.1 es mayor que 4.0; 6.9 es menor que 7.0). "
     "E1: ofimática 4.2, antivirus 7.1, PDF 2.6. E2: 4.0, 7.1, 2.6. E3: 4.2, 6.9, 2.6. E4: 4.1, 7.0, 2.4. E5: 3.9, 6.5, 2.1. E6: 4.2, 7.2, 2.6. Cada actualización tarda 20 minutos por programa.")
build(
    O10, 3, F,
    use="Aprenderé a analizar un inventario: qué equipos cumplen las versiones mínimas, qué programas hay que actualizar y en qué orden (solo en papel).",
    prior=["Sé comparar versiones.", "Sé qué es un inventario.", "Sé sumar y multiplicar."],
    explain=[
        "Para analizar un inventario se compara, programa por programa y equipo por equipo, la versión instalada con la versión mínima del estudio. Un equipo cumple si todos sus programas igualan o superan el mínimo. Cada programa que no cumple es una actualización pendiente. El total de actualizaciones pendientes y el tiempo por actualización permiten estimar el trabajo.",
        "Las actualizaciones no tienen todas la misma urgencia. Primero se atienden las de seguridad, como el antivirus, porque protegen a todo el equipo. Después se atienden las de productividad y las utilitarias, según las necesidades de las personas y la compatibilidad con sus archivos. Todo se hace con autorización, respaldo y registro.",
        "El resultado del análisis es una lista priorizada con equipos, programas pendientes y tiempo estimado, y una nota de límites: los datos son de ejemplo y se confirman en cada equipo real.",
    ],
    vocab=[("versión mínima", "la menor versión aceptada por el estudio"), ("actualización pendiente", "programa cuya versión es menor que la mínima"), ("prioridad", "orden de urgencia de las tareas"), ("lista priorizada", "lista ordenada por urgencia"), ("estimar", "calcular de manera aproximada")],
    worked=[
        ("Equipo que cumple", "Un equipo de ejemplo tiene ofimática 4.2, antivirus 7.1 y PDF 2.6. Mínimos: 4.1, 7.0 y 2.5. ¿Cumple?", ["4.2 ≥ 4.1, 7.1 ≥ 7.0 y 2.6 ≥ 2.5.", "Cumple los tres programas."], "Sí, cumple"),
        ("Tiempo estimado", "Un equipo necesita 2 actualizaciones de 15 minutos cada una. ¿Cuántos minutos son?", ["Se multiplica por la cantidad de actualizaciones.", "2 × 15 = 30."], "30 minutos"),
    ],
    mistakes=[("Atender primero los cambios de apariencia y dejar para después el antivirus.", "El antivirus protege a todo el equipo; es de mayor urgencia.", "Prioriza seguridad y luego el resto."),
              ("Dar por cumplido un equipo porque dos de sus tres programas están al día.", "Un equipo cumple solo si todos sus programas cumplen.", "Revisa los tres programas de cada equipo.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una versión mínima?", "La menor versión aceptada por el estudio", "La versión más cara", "La versión más antigua del mercado", "Una versión mínima fija el piso que deben cumplir los equipos."),
        ("abc", "En Conectividad y Redes: ¿qué es una actualización pendiente?", "Un programa cuya versión es menor que la mínima", "Un programa recién instalado", "Una licencia vencida", "Pendiente quiere decir que aún falta actualizarlo."),
        ("abc", "¿Qué es una lista priorizada?", "Una lista ordenada por urgencia", "Una lista ordenada alfabéticamente", "Una lista sin orden", "Priorizar es ordenar las tareas por urgencia."),
        ("abc", "{F} ¿Qué equipos cumplen los tres mínimos?", "E1 y E6", "E1 y E2", "E4 y E6", "E2 falla en ofimática, E3 en antivirus, E4 en PDF y E5 en los tres."),
        ("abc", "{F} ¿Por qué falla E2?", "Su ofimática 4.0 es menor que la mínima 4.1", "Su antivirus es antiguo", "Su PDF es antiguo", "E2 cumple antivirus y PDF, pero no la ofimática."),
        ("abc", "{F} ¿Por qué falla E3?", "Su antivirus 6.9 es menor que la mínima 7.0", "Su ofimática es antigua", "No tiene licencia", "E3 cumple ofimática y PDF; el antivirus 6.9 es menor que 7.0."),
        ("=", "{F} ¿Cuántas actualizaciones pendientes hay en total (E2: 1, E3: 1, E4: 1, E5: 3)?", "1+1+1+3", "Se suman las actualizaciones pendientes de cada equipo.", " actualizaciones"),
        ("=", "{F} ¿Cuántos minutos tomarían todas las actualizaciones pendientes?", "(1+1+1+3)*20", "Se multiplican las actualizaciones por los minutos de cada una.", " minutos"),
        ("abc", "{F} ¿Qué actualización tiene prioridad en E5?", "El antivirus, por seguridad", "El lector PDF, porque pesa menos", "La ofimática, por apariencia", "El antivirus protege todo el equipo y es la prioridad de seguridad."),
        ("=", "{F} Los equipos que no cumplen son E2, E3, E4 y E5. ¿Cuántos equipos cumplen respecto del total de 6?", "6-4", "Al total se le restan los equipos que no cumplen.", " equipos"),
        ("abc", "{F} Una persona propone dar por cumplido a E4 «porque dos de tres programas cumplen». ¿Qué respondes?", "Un equipo cumple solo si todos sus programas cumplen; a E4 le falta el PDF", "Tiene razón: dos de tres alcanza", "E4 cumple porque su ofimática es 4.1", "El estudio exige que cada programa iguale el mínimo."),
        ("=", "{F} Se actualizan primero los antivirus de E3 y de E5, es decir 2 actualizaciones. ¿Cuántos minutos toman?", "2*20", "Se multiplican las dos actualizaciones por los minutos de cada una.", " minutos"),
        ("abc", "{F} ¿Qué límite debe declarar el análisis?", "Los datos son de ejemplo y se confirman en cada equipo real, con autorización y respaldo", "Ninguno, porque los números son exactos", "Que no hace falta registrar", "El análisis en papel se verifica en la realidad antes de actuar."),
    ],
    ctx=("abc", "La jefa te pregunta: «¿qué equipo está peor?». Con la ficha, ¿qué respondes?", "E5, porque incumple los tres mínimos, y propongo empezar por su antivirus", "E1, porque tiene todo al día", "No se puede saber nunca", "E5 incumple ofimática, antivirus y PDF; la seguridad va primero."),
    sc=[
        ("En Conectividad y Redes: ¿cuándo cumple un equipo?", "Cuando todos sus programas igualan o superan el mínimo", "Un solo programa que falle basta para incumplir."),
        ("¿Qué actualización se atiende primero?", "La de seguridad, como el antivirus", "El antivirus protege a todo el equipo y es prioridad de seguridad."),
        ("¿Qué se hace con los datos de ejemplo antes de actuar?", "Se confirman en cada equipo real, con autorización y respaldo", "El análisis en papel no reemplaza la verificación."),
    ],
    op=("Inventario de ejemplo con mínimos ofimática 4.1 y antivirus 7.0: A1 (4.1; 7.0), A2 (4.0; 7.2), A3 (4.2; 6.8), A4 (3.8; 6.5). Indica qué equipos cumplen, cuántas actualizaciones pendientes hay, cuántos minutos toma si cada una tarda 20 minutos y qué actualización haces primero.",
        "Cumple A1. A2 falla en ofimática; A3 falla en antivirus; A4 falla en ambos. Pendientes: 1 + 1 + 2 = 4 actualizaciones; 4 × 20 = 80 minutos. Primero los antivirus de A3 y A4, por seguridad.",
        ["identifica los equipos que cumplen", "cuenta las actualizaciones y el tiempo", "prioriza la seguridad"],
        ["tabla con equipo, estado, pendientes y orden"],
        ["decir que A2 cumple", "contar mal las actualizaciones", "no priorizar la seguridad"],
        "Pregunta: «¿cuántas actualizaciones necesita A4?». Si responde una, pídele que revise los dos programas."),
    reinforce="Con tres equipos inventados, anota las versiones y marca cuáles cumplen un mínimo que tú definas.",
    extend="Explica por qué se confirma en cada equipo real un análisis hecho con datos en papel.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 4 (decisión de ejemplo). Hay 3 actualizaciones pendientes en los 15 equipos: U1, parche de seguridad del antivirus, que corrige una falla grave (15 minutos por equipo); U2, actualización mayor de la ofimática, que cambia menús y el formato de archivos y podría no abrir las plantillas de contabilidad (40 minutos por equipo); "
     "U3, actualización menor del lector PDF (10 minutos por equipo). Trabajan 3 técnicos a la vez y los 15 equipos se reparten en partes iguales. Ventana de mantenimiento: 150 minutos. Requerimiento de usuarios: contabilidad necesita sus plantillas funcionando. "
     "Criterio: primero seguridad; después lo que quepa en la ventana sin poner en riesgo el trabajo.")
build(
    O10, 4, F,
    use="Aprenderé a decidir qué actualizar y cuándo, equilibrando seguridad, requerimientos de las personas usuarias y tiempo disponible.",
    prior=["Sé la diferencia entre parche y actualización mayor.", "Sé qué es una ventana de mantenimiento.", "Sé multiplicar y dividir."],
    explain=[
        "Decidir qué actualizar y cuándo es un problema de criterio. El primer criterio es la seguridad: un parche que corrige una falla grave se instala pronto. El segundo es el requerimiento de las personas usuarias: si una actualización puede dejarlas sin trabajar, se prueba antes. El tercero es el tiempo: las actualizaciones deben caber en la ventana de mantenimiento.",
        "El tiempo se calcula repartiendo los equipos entre los técnicos: equipos por técnico por minutos de cada actualización. Si algo no cabe, se deja para otra ventana. Una actualización mayor se prueba antes en un equipo de prueba con los archivos reales, para detectar problemas de compatibilidad sin afectar el trabajo; recién entonces se programa.",
        "La recomendación incluye los cálculos, el orden propuesto, el plan de reversión y los límites. Los datos son de ejemplo y las decisiones reales las toma la administradora de informática con las personas usuarias.",
    ],
    vocab=[("equipo de prueba", "equipo donde se prueba una actualización antes de instalarla en todos"), ("criterio de seguridad", "la seguridad se atiende primero"), ("plan de reversión", "pasos acordados para volver a la versión anterior"), ("equipos por técnico", "reparto de los equipos entre las personas que trabajan"), ("riesgo de interrupción", "posibilidad de dejar a las personas sin poder trabajar")],
    worked=[
        ("Equipos por técnico", "Hay 12 equipos y 3 técnicos que se reparten el trabajo en partes iguales. ¿Cuántos equipos atiende cada uno?", ["Se divide el total de equipos por los técnicos.", "12 ÷ 3 = 4."], "4 equipos"),
        ("Cabe en la ventana", "Cada técnico atiende 4 equipos y cada actualización tarda 20 minutos. La ventana es de 90 minutos. ¿Cabe?", ["Tiempo por técnico: 4 × 20 = 80 minutos.", "80 es menor que 90."], "Sí, cabe"),
    ],
    mistakes=[("Instalar una actualización mayor en todos los equipos sin probarla con los archivos reales.", "Si las plantillas no abren, se detiene el trabajo de contabilidad.", "Pruébala primero en un equipo de prueba y respalda."),
              ("Ignorar el parche de seguridad porque «el equipo anda bien».", "Una falla grave sin corregir expone los datos aunque el equipo parezca funcionar.", "Aplica primero los parches de seguridad.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un equipo de prueba?", "Un equipo donde se prueba una actualización antes de instalarla en todos", "Un equipo que ya no funciona", "El equipo de la jefa", "La prueba previa reduce el riesgo para los demás."),
        ("abc", "En Conectividad y Redes: ¿qué es un plan de reversión?", "Los pasos acordados para volver a la versión anterior si algo falla", "Una lista de precios", "Una nueva licencia", "La reversión prepara una salida ante un fallo."),
        ("abc", "¿Qué criterio va primero al decidir actualizaciones?", "La seguridad", "La apariencia", "El gusto de cada usuario", "Una falla de seguridad grave expone a todos los equipos."),
        ("=", "{F} ¿Cuántos equipos atiende cada técnico?", "15//3", "Se divide el total de equipos por los técnicos.", " equipos"),
        ("=", "{F} ¿Cuántos minutos necesita cada técnico para U1?", "(15//3)*15", "Se multiplican sus equipos por los minutos de la actualización.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita cada técnico para U2?", "(15//3)*40", "Se multiplican sus equipos por los minutos de la actualización mayor.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita cada técnico para U1 y U3 juntas?", "(15//3)*(15+10)", "Se suman los minutos de las dos actualizaciones y se multiplican por los equipos.", " minutos"),
        ("abc", "{F} ¿Caben U1 y U3 en la ventana de 150 minutos?", "Sí: necesitan 125 minutos", "No: necesitan 200 minutos", "No: necesitan 150 minutos exactos", "125 minutos es menor que la ventana de 150."),
        ("=", "{F} ¿Cuántos minutos sobran de la ventana después de U1 y U3?", "150-(15//3)*(15+10)", "A la ventana se le restan los minutos de las dos actualizaciones.", " minutos"),
        ("abc", "{F} ¿Por qué no se instala U2 en esta ventana?", "Necesita 200 minutos, más que los 150 disponibles, y puede dejar sin plantillas a contabilidad", "Porque U2 es un parche", "Porque no hay técnicos", "No cabe en la ventana y tiene riesgo de interrupción para el trabajo."),
        ("abc", "{F} La jefa pide «actualizar todo ahora». ¿Qué respondes con los datos?", "Que U1 y U3 caben y se hacen ahora, y que U2 se prueba antes porque podría afectar las plantillas", "Que se hace todo aunque falle", "Que no se hace nada nunca", "Se actúa según el criterio: seguridad, ventana y requerimientos."),
        ("abc", "{F} ¿Qué se hace antes de programar U2?", "Probarla con las plantillas reales en un equipo de prueba, con respaldo", "Instalarla en todos los equipos", "Borrar las plantillas", "La prueba previa detecta problemas de compatibilidad sin riesgo."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los datos son de ejemplo y decide la administradora de informática con las personas usuarias", "Ninguno, porque los números son exactos", "Que no hace falta plan de reversión", "Las decisiones reales dependen de las personas responsables y de la situación real."),
    ],
    ctx=("abc", "Después de instalar U1 y U3, un técnico quiere dejar los equipos sin registrar «para ganar tiempo». ¿Qué respondes?", "Que se registran las versiones y la fecha, porque permite revisar y volver atrás", "Que no se registra nada", "Que se registra solo si algo falla", "El registro es parte del trabajo y permite revisar los cambios."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula el tiempo por técnico?", "Equipos por técnico multiplicado por los minutos de cada actualización", "Se compara con la ventana de mantenimiento."),
        ("¿Qué se prueba antes de una actualización mayor?", "La compatibilidad con los archivos reales de las personas", "Así se evita dejar a alguien sin trabajar."),
        ("¿Qué actualización de software se atiende primero en el inventario?", "Los parches de seguridad", "Reducen el riesgo para todos los equipos."),
    ],
    op=("Un estudio de ejemplo tiene 12 equipos y 2 técnicos que los reparten en partes iguales. Pendientes: V1, parche del antivirus (10 minutos por equipo); V2, actualización mayor de la planilla que podría cambiar un formato (30 minutos por equipo); V3, utilidad de compresión (5 minutos por equipo). Ventana: 100 minutos. Calcula el tiempo por técnico de V1 y V3 juntas y de V2, decide qué hacer en la ventana y qué dejar para después, con un límite.",
        "Cada técnico atiende 6 equipos. V1 y V3: 6 × (10 + 5) = 90 minutos, caben en 100. V2: 6 × 30 = 180 minutos, no cabe y podría afectar un formato. En la ventana se hacen V1 y V3; V2 se prueba antes en un equipo de prueba y se programa en otra ventana. Límite: datos de ejemplo.",
        ["calcula equipos y tiempos por técnico", "decide qué cabe", "propone probar la actualización mayor"],
        ["hoja con cálculos, decisión y límite"],
        ["olvidar dividir entre dos técnicos", "instalar V2 sin probar", "no declarar límite"],
        "Pregunta: «¿por qué V2 se deja para después?». Si solo dice 'por el tiempo', pídele que agregue el riesgo del formato."),
    reinforce="Con 10 equipos y 2 técnicos, calcula cuántos minutos necesita cada uno si cada actualización tarda 12 minutos.",
    extend="Explica por qué un parche de seguridad pesa más que una mejora de apariencia al priorizar.",
)

# ============================================================ OAE-11, clase 1
F = ("Ficha 5 (taller de ejemplo, inventado). El «Taller de Informática del Liceo Los Cóndores» arma y configura equipos para el laboratorio con ayuda de un manual de instalación escrito por el fabricante de las piezas. "
     "Riesgos: electricidad (equipos conectados y fuente de poder), descarga de electricidad estática que daña piezas, bordes cortantes, peso, polvo y mala postura. Roles: instructor o instructora, estudiante en práctica y jefa de laboratorio. "
     "Elementos de protección y herramientas (nombres genéricos): pulsera antiestática, destornilladores adecuados, mesa ordenada y bien iluminada. Se siguen el manual, la norma vigente y las instrucciones del instructor. Armar un equipo toma 90 minutos de ejemplo con instructor.")
build(
    O11, 1, F,
    use="Aprenderé qué significa armar y configurar un equipo, qué documentos y roles intervienen y qué riesgos y normas de seguridad existen (solo conceptos).",
    prior=["Conozco las partes de un computador.", "Sé qué es un manual de instalación.", "Sé multiplicar y dividir."],
    explain=[
        "Armar un equipo personal es reunir sus piezas (placa madre, procesador, memoria, almacenamiento, fuente de poder y gabinete) y dejarlas funcionando juntas. Configurarlo es dejar listo el sistema, las cuentas, las actualizaciones y las medidas de seguridad. Se apoya siempre en el manual de instalación del fabricante de las piezas, que es el documento de referencia, y en las normas de seguridad.",
        "Hay riesgos reales: electricidad, descarga de electricidad estática que daña las piezas, bordes cortantes, peso, polvo y mala postura. Por eso se trabaja con instructor, con elementos de protección y herramientas adecuadas, en una mesa ordenada, y nunca con el equipo conectado mientras está abierto. Además se cuida la ergonomía: se hacen pausas y se cambia de postura.",
        "En este cuaderno aprendes solo los conceptos y la lectura de documentos, y no se describe ningún procedimiento." + AVISO,
    ],
    vocab=[("manual de instalación", "documento del fabricante con las instrucciones de las piezas"), ("descarga electrostática", "descarga de electricidad estática que puede dañar piezas"), ("elemento de protección", "equipo que reduce un riesgo, como una pulsera antiestática"), ("instructor", "persona autorizada que supervisa y enseña"), ("norma de seguridad", "regla que debe cumplirse para evitar accidentes")],
    worked=[
        ("Tiempo para varios equipos", "Armar un equipo de ejemplo toma 60 minutos y hay 5 equipos. ¿Cuántos minutos son?", ["Se multiplican los equipos por los minutos de cada uno.", "5 × 60 = 300."], "300 minutos"),
        ("Qué documento mandar", "El manual del fabricante dice una cosa y un compañero dice que «siempre se hace de otra forma». ¿A quién se sigue?", ["El manual y la norma son la referencia.", "Se consulta al instructor ante la duda."], "Al manual, y se consulta al instructor"),
    ],
    mistakes=[("Probar el equipo con la tapa abierta y conectado «solo un momento».", "Hay riesgo eléctrico y de daño a las piezas.", "No lo hagas sin instructor y sin la norma vigente."),
              ("Trabajar sin protección contra la electricidad estática porque «nunca ha pasado nada».", "La descarga puede dañar piezas sin que se note.", "Usa los elementos de protección indicados por el instructor.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el manual de instalación?", "El documento del fabricante con las instrucciones de las piezas", "Una lista de precios", "Un permiso para entrar al taller", "El manual es la referencia técnica de cómo trabajar con las piezas."),
        ("abc", "En Conectividad y Redes: ¿qué es la descarga electrostática?", "Una descarga de electricidad estática que puede dañar las piezas", "Una descarga de datos desde internet", "Un tipo de virus", "La electricidad estática puede dañar componentes sensibles."),
        ("abc", "¿Quién supervisa y autoriza el trabajo con equipos en el taller?", "El instructor o la instructora", "Cualquier compañero", "La persona que llegue primero", "El taller de ejemplo trabaja con instructor autorizado."),
        ("abc", "{F} ¿Qué documento es la referencia técnica para armar el equipo?", "El manual de instalación del fabricante", "Un mensaje de un compañero", "El horario del taller", "La ficha indica que se sigue el manual del fabricante."),
        ("abc", "{F} ¿Cuál es un riesgo de trabajar con un equipo abierto y conectado?", "La electricidad", "El exceso de memoria", "El cifrado de la red", "Un equipo conectado tiene electricidad y solo personal autorizado lo abre."),
        ("=", "{F} Armar un equipo toma 90 minutos. ¿Cuántos minutos se necesitan para 10 equipos?", "10*90", "Se multiplican los equipos por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántas horas son 900 minutos?", "900//60", "Se divide el total de minutos por 60.", " horas"),
        ("=", "{F} En una jornada de 360 minutos, ¿cuántos equipos de 90 minutos caben?", "360//90", "Se divide la jornada por el tiempo de cada equipo.", " equipos"),
        ("abc", "{F} Un estudiante en práctica quiere trabajar sin pulsera antiestática porque «nunca pasa nada». ¿Qué corresponde?", "Usar los elementos de protección indicados por el instructor", "Trabajar sin protección", "Trabajar solo si nadie lo mira", "La descarga puede dañar piezas aunque no se vea."),
        ("abc", "{F} El manual y un compañero dicen cosas distintas. ¿Qué corresponde?", "Seguir el manual y consultar al instructor", "Seguir al compañero porque lleva más tiempo", "Seguir la costumbre del taller", "El manual y la norma son la referencia; la duda se consulta."),
        ("abc", "{F} El instructor no ha llegado y un compañero propone conectar el equipo abierto «para probar». ¿Qué respondes?", "No: se espera al instructor, porque hay riesgo eléctrico", "Sí, si lo conecta rápido", "Sí, si usa guantes", "Sin instructor y con norma vigente no se prueba un equipo abierto."),
        ("abc", "{F} Una estudiante pasa cuatro horas inclinada sobre la mesa sin descanso. ¿Qué se descuida?", "La ergonomía: la postura y las pausas", "El cifrado de la red", "La licencia del sistema", "La postura mantenida sin pausas daña el cuerpo."),
        ("abc", "¿Por qué este cuaderno no te habilita para armar equipos?", "Porque el aprendizaje en papel no reemplaza la formación práctica con instructor ni la norma vigente", "Porque armar equipos es muy fácil", "Porque no existen manuales", "El oficio exige práctica supervisada y elementos de protección."),
    ],
    ctx=("abc", "Un compañero de ejemplo te propone abrir la fuente de poder de un equipo viejo «para ver qué tiene». ¿Qué respondes?", "Que no se abre: es peligrosa aunque esté apagada y esa tarea exige personal autorizado", "Que sí, con un destornillador", "Que sí, si nadie lo ve", "La fuente de poder puede almacenar energía peligrosa; solo personal autorizado interviene."),
    sc=[
        ("En Conectividad y Redes: ¿qué documento se sigue para armar un equipo?", "El manual de instalación del fabricante", "Es la referencia técnica de las piezas."),
        ("¿Quién supervisa el trabajo con equipos?", "El instructor autorizado", "El trabajo con riesgos exige supervisión."),
        ("¿Por qué se usan elementos de protección?", "Porque reducen riesgos como la electricidad estática", "Protegen a las personas y a las piezas."),
    ],
    op=("Un taller de ejemplo debe armar 8 equipos de 75 minutos cada uno, en jornadas de 300 minutos. Calcula cuántos minutos son en total, cuántos equipos caben por jornada, cuántas jornadas se necesitan, y escribe tres normas de seguridad conceptuales (sin pasos de armado).",
        "Total: 8 × 75 = 600 minutos. Por jornada caben 300 ÷ 75 = 4 equipos. Jornadas: 8 ÷ 4 = 2. Normas: trabajar con instructor; usar elementos de protección; no abrir ni conectar equipos sin autorización.",
        ["calcula minutos, equipos por jornada y jornadas", "escribe tres normas coherentes", "no describe procedimientos de armado"],
        ["hoja con cálculos y tres normas"],
        ["dividir al revés", "describir pasos de armado", "no mencionar al instructor"],
        "Pregunta: «¿cuántas jornadas?». Si responde 8, pídele que use equipos por jornada."),
    reinforce="Lista cinco elementos de seguridad de un taller y explica con una frase para qué sirve cada uno.",
    extend="Explica por qué seguir el manual del fabricante es parte del trabajo seguro.",
)

# ============================================================ OAE-11, clase 2
F = ("Ficha 6 (piezas y documentos de ejemplo). Piezas: placa madre (conecta todo; define qué procesador y qué memoria admite), procesador, memoria RAM, almacenamiento, fuente de poder (se mide en watts) y gabinete. "
     "Compatibilidad: el procesador debe calzar en el socket de la placa; la memoria debe ser del tipo que admite la placa; el tamaño (factor de forma) de la placa debe caber en el gabinete. "
     "Documentos: manual de instalación, lista de componentes, lista de verificación y acta de entrega. Ejemplo: la placa PM-1 admite procesadores de socket S1, memoria tipo M1 y tiene tamaño «medio»; el gabinete GA-1 admite placas de tamaño «medio» o «pequeño»; el gabinete GA-2 admite solo «pequeño».")
build(
    O11, 2, F,
    use="Aprenderé las piezas de un equipo, cómo se comprueba su compatibilidad y qué documentos acompañan el armado (solo lectura de documentos).",
    prior=["Conozco las partes del computador.", "Sé leer una ficha técnica.", "Sé que el armado se hace con instructor."],
    explain=[
        "Cada pieza de un computador cumple una función: la placa madre conecta todo; el procesador ejecuta instrucciones; la memoria RAM guarda lo que se está usando; el almacenamiento guarda los archivos; la fuente de poder entrega energía y se mide en watts; el gabinete aloja las piezas. Para que funcionen juntas deben ser compatibles.",
        "La compatibilidad se revisa antes de comprar o armar. El procesador debe calzar en el socket de la placa, que es el zócalo donde va. La memoria debe ser del tipo que admite la placa. El tamaño de la placa, llamado factor de forma, debe caber en el gabinete. Estos datos están en el manual de instalación y en la lista de componentes del equipo.",
        "Los documentos son: el manual de instalación (referencia técnica), la lista de componentes (qué piezas lleva el equipo), la lista de verificación (puntos que se comprueban y marcan) y el acta de entrega (constancia de lo entregado y de su estado). Aquí solo se lee y se interpreta; armar un equipo exige instructor autorizado." + AVISO,
    ],
    vocab=[("socket", "zócalo de la placa donde se instala el procesador"), ("factor de forma", "tamaño de la placa madre"), ("lista de componentes", "lista de las piezas que lleva un equipo"), ("lista de verificación", "lista de puntos que se comprueban y marcan"), ("acta de entrega", "constancia de lo entregado y su estado"), ("compatibilidad", "que las piezas funcionen juntas")],
    worked=[
        ("Compatibilidad de procesador", "Una placa de ejemplo tiene socket S1. ¿Es compatible un procesador de socket S2?", ["El procesador debe calzar en el socket de la placa.", "S2 es distinto de S1."], "No es compatible"),
        ("Memoria total", "Una placa de ejemplo lleva 2 módulos de 4 GB. ¿Cuántos GB de RAM tiene?", ["Se multiplican los módulos por su capacidad.", "2 × 4 = 8."], "8 GB"),
    ],
    mistakes=[("Elegir un procesador solo por su precio sin mirar el socket.", "Si el socket no coincide, no se puede usar en esa placa.", "Revisa en el manual el socket que admite la placa."),
              ("Dar por revisado el equipo sin completar la lista de verificación.", "Pueden quedar puntos sin comprobar.", "Completa y firma la lista de verificación con el instructor.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el socket de una placa madre?", "El zócalo donde se instala el procesador", "La toma de energía de la pared", "El cable de red", "El socket define con qué procesadores es compatible la placa."),
        ("abc", "En Conectividad y Redes: ¿qué es el factor de forma de una placa?", "Su tamaño, que debe caber en el gabinete", "Su precio", "Su color", "El factor de forma indica el tamaño de la placa."),
        ("abc", "¿Qué es una lista de verificación?", "Una lista de puntos que se comprueban y marcan", "Una lista de claves", "Una lista de precios", "La lista de verificación ayuda a no olvidar ninguna comprobación."),
        ("abc", "{F} ¿Qué procesador es compatible con la placa PM-1: P-A de socket S1 o P-B de socket S2?", "P-A, de socket S1", "P-B, de socket S2", "Ambos", "La placa PM-1 admite procesadores de socket S1."),
        ("abc", "{F} ¿Cabe la placa PM-1 en el gabinete GA-1?", "Sí: GA-1 admite placas de tamaño medio", "No: GA-1 solo admite placas grandes", "Solo si se corta el gabinete", "PM-1 es de tamaño medio y GA-1 admite medio o pequeño."),
        ("abc", "{F} ¿Qué documento deja constancia de lo entregado y de su estado?", "El acta de entrega", "El manual de instalación", "La lista de componentes", "El acta firma el estado del equipo al entregarlo."),
        ("=", "{F} Un equipo lleva 2 módulos de memoria tipo M1 de 8 GB cada uno. ¿Cuántos GB de RAM tiene?", "2*8", "Se multiplican los módulos por su capacidad.", " GB"),
        ("abc", "{F} Se ofrece un módulo de memoria tipo M2 para la placa PM-1. ¿Sirve?", "No: la placa admite tipo M1", "Sí, porque tiene más capacidad", "Sí, porque todos los módulos son iguales", "El tipo de memoria debe coincidir con el que admite la placa."),
        ("abc", "{F} ¿Cabe la placa PM-1 en el gabinete GA-2?", "No: GA-2 admite solo placas pequeñas", "Sí, porque es un gabinete", "Sí, si se aprieta", "PM-1 es de tamaño medio y GA-2 solo acepta pequeño."),
        ("abc", "{F} Un compañero compra un procesador solo por su precio sin mirar el socket. ¿Qué respondes?", "Que debe calzar en el socket de la placa, porque si no, no sirve", "Que está bien, todos calzan", "Que el color decide", "El socket es un requisito indispensable de compatibilidad."),
        ("abc", "{F} Un estudiante da por revisado el equipo sin completar la lista de verificación. ¿Qué riesgo hay?", "Pueden quedar puntos sin comprobar", "Ninguno", "Que la lista pierda el color", "La lista existe para no olvidar ninguna comprobación."),
        ("=", "{F} Una lista de verificación tiene 12 puntos y se han comprobado 9. ¿Cuántos faltan?", "12-9", "Al total de puntos se le restan los comprobados.", " puntos"),
        ("abc", "{F} ¿Qué debe llevar el acta de entrega de un equipo?", "Qué se entrega, su estado, la fecha y quién lo recibe", "Solo el nombre del técnico", "Las claves de las personas", "Con esos datos queda constancia revisable."),
    ],
    ctx=("abc", "Un jefe de ejemplo pide comprar piezas «de las más baratas» para 10 equipos sin mirar el manual. ¿Qué respondes?", "Que primero se revisa la compatibilidad en el manual y la lista de componentes, para que las piezas funcionen juntas", "Que se compra lo más barato aunque no sirva", "Que no se compra nada nunca", "La compatibilidad es indispensable; el precio se compara entre piezas compatibles."),
    sc=[
        ("En Conectividad y Redes: ¿qué debe coincidir entre procesador y placa?", "El socket", "El procesador debe calzar en el zócalo de la placa."),
        ("¿Qué es el factor de forma?", "El tamaño de la placa, que debe caber en el gabinete", "Define el tipo de gabinete compatible."),
        ("¿Para qué sirve el acta de entrega?", "Para dejar constancia de lo entregado y su estado", "Es un documento de respaldo del trabajo."),
    ],
    op=("Ficha de ejemplo: placa PM-5 con socket S3, memoria tipo M2, tamaño «pequeño». Piezas disponibles: procesador P-1 (socket S3), procesador P-2 (socket S1), memoria M2 de 4 GB, memoria M1 de 8 GB, gabinete GA-3 (admite solo «medio»), gabinete GA-4 (admite «pequeño»). Elige qué piezas son compatibles con PM-5, indica qué gabinete sirve y calcula cuántos GB de RAM habría con 2 módulos compatibles.",
        "Compatibles: procesador P-1 (S3) y memoria M2 de 4 GB; el gabinete GA-4 (admite pequeño). RAM: 2 × 4 = 8 GB. Se descartan P-2 (socket S1), la memoria M1 y el gabinete GA-3.",
        ["elige solo piezas compatibles", "indica el gabinete correcto", "calcula la RAM"],
        ["tabla con pieza, compatible sí o no y razón"],
        ["elegir P-2 por barato", "elegir el gabinete GA-3", "mezclar tipos de memoria"],
        "Pregunta: «¿qué dato de PM-5 usaste para el gabinete?». Si no lo sabe, pídele que lea el tamaño de la placa."),
    reinforce="Elige una placa inventada con socket, tipo de memoria y tamaño, y arma una lista de piezas compatibles.",
    extend="Explica por qué el acta de entrega protege tanto a quien arma como a quien recibe el equipo.",
)

# ============================================================ OAE-11, clase 3
F = ("Ficha 7 (caso de ejemplo). Se arma un equipo con: placa PM-1 (socket S1, memoria tipo M1, tamaño medio); procesador P-A (socket S1, consumo 65 W) o P-B (socket S2, consumo 95 W); 2 módulos de memoria M1 de 8 GB (10 W en total); disco (10 W); tarjeta de red y ventilación (25 W); tarjeta de video (100 W). "
     "Fuentes disponibles: F-1 de 200 W, F-2 de 350 W y F-3 de 550 W. Regla de ejemplo: la potencia de la fuente debe ser al menos un 20 % mayor que la suma de los consumos.")
build(
    O11, 3, F,
    use="Aprenderé a analizar un caso de armado en papel: elegir piezas compatibles y calcular la fuente de poder con un margen de seguridad.",
    prior=["Sé qué es la compatibilidad.", "Sé qué es un watt.", "Sé calcular un porcentaje de una cifra redonda."],
    explain=[
        "Para analizar un armado en papel se revisan dos cosas. Primero, la compatibilidad de las piezas con la placa: socket, tipo de memoria y tamaño. Segundo, la potencia de la fuente: se suman los consumos de todas las piezas, medidos en watts (W), y se agrega un margen de seguridad, por ejemplo el 20 %, para que la fuente no trabaje al límite.",
        "La fuente se elige entre las disponibles como la más pequeña que cumple la regla. Una fuente menor que la necesaria no entrega energía suficiente; una mucho mayor puede cumplir, pero es una decisión de costo y no de compatibilidad. Todo cálculo se escribe con sus datos y con el límite: los consumos son de ejemplo y los reales están en el manual de cada pieza.",
        "Las decisiones de armado y de conexión las toma y ejecuta personal autorizado con instructor y norma vigente." + AVISO,
    ],
    vocab=[("watt (W)", "unidad de potencia y de consumo"), ("consumo", "potencia que usa una pieza"), ("margen de seguridad", "porcentaje extra para no trabajar al límite"), ("potencia de la fuente", "potencia máxima que entrega la fuente"), ("compatible", "que funciona con las demás piezas")],
    worked=[
        ("Suma de consumos", "Tres piezas de ejemplo consumen 40 W, 30 W y 50 W. ¿Cuánto suman?", ["Se suman los consumos.", "40 + 30 + 50 = 120."], "120 W"),
        ("Aplicar el margen", "La suma de consumos es 100 W y se pide un margen del 20 %. ¿Qué potencia mínima debe tener la fuente?", ["El 20 % de 100 es 20.", "100 + 20 = 120."], "120 W"),
    ],
    mistakes=[("Elegir la fuente sin sumar los consumos de todas las piezas.", "Puede quedar corta y el equipo no funcionar bien.", "Suma todos los consumos antes de comparar."),
              ("Olvidar el margen de seguridad.", "Una fuente al límite trabaja forzada y dura menos.", "Agrega el margen que pide la regla.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el consumo de una pieza?", "La potencia que usa, medida en watts", "Su precio", "Su tamaño", "El consumo se mide en watts y se suma para elegir la fuente."),
        ("abc", "En Conectividad y Redes: ¿para qué sirve el margen de seguridad en la fuente?", "Para que no trabaje al límite", "Para pagar menos", "Para cambiar el socket", "El margen evita que la fuente trabaje forzada."),
        ("abc", "¿Qué significa que una pieza sea compatible?", "Que funciona con las demás piezas del equipo", "Que es la más barata", "Que es la más nueva", "La compatibilidad se verifica en el manual de la pieza."),
        ("abc", "{F} ¿Qué procesador conviene usar con la placa PM-1?", "P-A, de socket S1", "P-B, de socket S2", "Cualquiera", "La placa PM-1 admite solamente procesadores con socket S1."),
        ("=", "{F} ¿Cuántos watts suman los consumos del equipo con P-A?", "65+10+10+25+100", "Se suman procesador, memoria, disco, red y ventilación, y video.", " W"),
        ("=", "{F} ¿Cuál es la potencia mínima de la fuente con el margen del 20 %?", "(65+10+10+25+100)*120//100", "Se multiplica la suma por 120 % y se divide por 100.", " W"),
        ("abc", "{F} ¿Cuál es la fuente más pequeña que cumple la regla?", "F-2, de 350 W", "F-1, de 200 W", "F-3, de 550 W", "F-1 no alcanza los 252 W; F-2 sí y es la más pequeña que cumple."),
        ("=", "{F} ¿Cuántos watts de margen real le quedan a F-2 sobre la suma de consumos?", "350-(65+10+10+25+100)", "A la potencia de la fuente se le resta la suma de los consumos.", " W"),
        ("abc", "{F} ¿Por qué no sirve F-1?", "Porque 200 W es menos que el mínimo de 252 W", "Porque es demasiado grande", "Porque es de otro socket", "F-1 no cubre ni la suma de consumos con margen."),
        ("abc", "{F} Una persona dice: «usemos F-3 por si acaso». ¿Qué respondes?", "F-3 cumple, pero F-2 ya cumple la regla; elegir F-3 es una decisión de costo y no de compatibilidad", "F-3 no cumple la regla", "F-3 es más pequeña que F-2", "Cumplir la regla es lo técnico; pagar más es una decisión aparte."),
        ("abc", "{F} Alguien propone el procesador P-B «porque consume más y es más potente». ¿Qué respondes?", "No calza en el socket de la placa PM-1; la compatibilidad es indispensable", "Es mejor, aunque no calce", "Se puede forzar para que calce", "Las piezas incompatibles no se fuerzan."),
        ("=", "{F} Si se agrega un segundo disco de 10 W, ¿cuál sería la nueva potencia mínima de la fuente con el margen del 20 %?", "(65+10+10+25+100+10)*120//100", "Se agrega el consumo del segundo disco a la suma y se aplica el margen.", " W"),
        ("abc", "{F} Con el segundo disco, ¿sigue cumpliendo F-2?", "Sí: 350 W es mayor que 264 W", "No: 264 W es mayor que 350 W", "No se puede saber", "La nueva potencia mínima es 264 W, menor que los 350 W de F-2."),
    ],
    ctx=("abc", "Faltan solo 10 minutos para el cierre del taller y un compañero propone conectar el equipo armado a la corriente «para ver si enciende». El instructor no está. ¿Qué haces?", "Me niego y aviso al instructor, porque conectar un equipo exige autorización y supervisión", "Lo conecto yo, es rápido", "Lo conecto con el gabinete abierto", "Las pruebas con electricidad requieren instructor y norma vigente."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula la potencia mínima de la fuente?", "Suma de consumos más el margen de seguridad", "El margen evita que la fuente trabaje al límite."),
        ("¿Qué fuente se elige entre varias que cumplen?", "La más pequeña que cumple la regla", "Elegir otra es una decisión de costo."),
        ("¿Qué se hace con una pieza incompatible?", "Se descarta, no se fuerza", "La compatibilidad es un criterio indispensable para elegir las piezas."),
    ],
    op=("Equipo de ejemplo: procesador 95 W, memoria 10 W, disco 10 W, red y ventilación 25 W. Fuentes: G-1 de 150 W, G-2 de 250 W, G-3 de 400 W. Regla: la fuente debe superar en al menos 20 % la suma de consumos. Calcula la suma, la potencia mínima y qué fuente elegir, y escribe una norma de seguridad (conceptual) para el trabajo en el taller.",
        "Suma: 95 + 10 + 10 + 25 = 140 W. Mínimo: 140 × 120 ÷ 100 = 168 W. G-1 no alcanza; G-2 de 250 W cumple y es la más pequeña. Norma: no conectar ni abrir equipos sin instructor y sin norma vigente.",
        ["suma los consumos", "calcula el mínimo con margen", "elige la fuente más pequeña que cumple"],
        ["hoja con cálculo y elección, más la norma de seguridad"],
        ["no aplicar el margen", "elegir G-3 sin razón", "describir pasos de conexión"],
        "Pregunta: «¿por qué no G-1?». Si no responde, pídele que compare 150 con 168."),
    reinforce="Con cuatro consumos inventados, calcula la suma y la potencia mínima con un margen del 20 %.",
    extend="Explica por qué una fuente mucho mayor que la necesaria es una decisión de costo y no de compatibilidad.",
)

# ============================================================ OAE-11, clase 4
F = ("Ficha 8 (decisión de ejemplo). El laboratorio necesita 6 equipos para edición de documentos y navegación, con al menos 8 GB de RAM y un disco de 256 GB, con un presupuesto total de $2.400.000. "
     "Configuración A: RAM 8 GB, disco 256 GB, $380.000 por equipo. Configuración B: RAM 16 GB, disco 512 GB, $470.000 por equipo. Configuración C: RAM 4 GB, disco 128 GB, $250.000 por equipo. "
     "Criterios: cumplir los requisitos mínimos y caber en el presupuesto. Después del armado, personal autorizado configura cuentas, actualizaciones y antivirus, y se entrega el equipo con acta. Todos los precios son de ejemplo.")
build(
    O11, 4, F,
    use="Aprenderé a decidir una configuración de equipo con requisitos y presupuesto, y a escribir una recomendación con límites (solo cálculos en papel).",
    prior=["Sé comparar requisitos mínimos.", "Sé calcular costos totales.", "Sé que el armado lo hace personal autorizado."],
    explain=[
        "Decidir la configuración de un equipo parte de los requerimientos de quien lo usará: cuánta memoria y cuánto almacenamiento necesita para su trabajo. Cada configuración se compara con esos requisitos y se descartan las que no los cumplen, aunque sean baratas. Luego se calcula el costo total (precio por equipo por cantidad de equipos) y se compara con el presupuesto.",
        "Una configuración mejor que lo necesario puede salir de presupuesto, y una más barata puede dejar al equipo corto desde el primer día. La decisión final equilibra requisitos, presupuesto y vida útil, y deja constancia de los datos usados. Después del armado se configuran las cuentas, las actualizaciones y el antivirus y se entrega con un acta, siempre por personal autorizado.",
        "La recomendación se escribe con sus cálculos y sus límites: los precios son de ejemplo, las piezas se verifican en el manual y no se describe aquí ningún procedimiento." + AVISO,
    ],
    vocab=[("requisito mínimo", "valor que la configuración debe igualar o superar"), ("costo total", "precio por equipo multiplicado por la cantidad"), ("presupuesto", "dinero disponible para la compra"), ("vida útil", "tiempo durante el cual el equipo sirve bien"), ("configuración inicial", "ajustes de cuentas, actualizaciones y seguridad antes de entregar")],
    worked=[
        ("Costo total", "Una configuración de ejemplo cuesta $300.000 por equipo y se necesitan 4. ¿Cuál es el costo total?", ["Se multiplica el precio por la cantidad.", "300.000 × 4 = 1.200.000."], "$1.200.000"),
        ("Descartar por requisitos", "Una configuración de ejemplo tiene 4 GB de RAM y se exigen 8 GB. ¿Se acepta?", ["4 es menor que 8.", "No cumple el requisito mínimo."], "No se acepta"),
    ],
    mistakes=[("Elegir la configuración más barata aunque no cumpla los requisitos.", "El equipo quedaría corto desde el primer día.", "Descarta primero lo que no cumple y compara después."),
              ("Entregar el equipo sin acta ni configuración inicial.", "Nadie sabe en qué estado se entregó.", "Completa la configuración inicial y firma el acta.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un requisito mínimo?", "Un valor que la configuración debe igualar o superar", "El precio más bajo", "El nombre de la marca", "Si no se cumple el mínimo, la configuración se descarta."),
        ("abc", "En Conectividad y Redes: ¿qué es la configuración inicial?", "Los ajustes de cuentas, actualizaciones y seguridad antes de entregar el equipo", "El armado de las piezas", "La compra de las piezas", "La configuración inicial deja el equipo listo y seguro."),
        ("abc", "¿Qué es el acta de entrega?", "La constancia de lo entregado y de su estado", "La factura de compra", "El manual de instalación", "El acta es el documento de respaldo del trabajo."),
        ("abc", "{F} ¿Qué configuración no cumple los requisitos mínimos?", "La configuración C", "La configuración A", "La configuración B", "C tiene 4 GB de RAM y 128 GB de disco, menos de lo exigido."),
        ("=", "{F} ¿Cuántos pesos cuesta la configuración A en los 6 equipos?", "6*380000", "Se multiplica el precio por equipo por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la configuración B en los 6 equipos?", "6*470000", "Se multiplica el precio por equipo por la cantidad.", " pesos"),
        ("abc", "{F} ¿Qué configuración cumple los requisitos y cabe en el presupuesto?", "La configuración A", "La configuración B", "La configuración C", "B supera el presupuesto y C no cumple los requisitos; A cumple ambos."),
        ("=", "{F} ¿Cuántos pesos sobran del presupuesto con la configuración A?", "2400000-6*380000", "Al presupuesto se le resta el costo total de A.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta por equipo la configuración B que la A?", "470000-380000", "Se resta el precio de A al de B.", " pesos"),
        ("abc", "{F} Un jefe propone la C «porque es la más barata». ¿Qué respondes?", "C no cumple los requisitos mínimos de RAM ni de disco, así que se descarta", "Tiene razón, el precio manda", "C es mejor porque ocupa menos espacio", "Los requisitos mínimos se verifican antes que el precio."),
        ("abc", "{F} ¿Por qué no se elige la B, que es técnicamente mejor?", "Porque con 6 equipos cuesta más que el presupuesto total", "Porque no cumple el requisito de RAM", "Porque es de otro tipo de memoria", "Cuesta 2.820.000, más que los 2.400.000 disponibles."),
        ("abc", "{F} ¿Qué debe hacerse después del armado, antes de entregar el equipo?", "Configuración inicial por personal autorizado y acta de entrega", "Nada, se entrega tal cual", "Borrar el manual", "Sin configuración ni acta, el estado del equipo no queda registrado."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los precios son de ejemplo, las piezas se verifican en el manual y el armado lo hace personal autorizado", "Ninguno, porque los números son exactos", "Que no hace falta acta", "Los datos de la ficha son de ejemplo y el trabajo real exige autorización."),
    ],
    ctx=("abc", "El laboratorio de ejemplo recibe equipos armados y un técnico los entrega sin acta «porque son del mismo curso». ¿Qué respondes?", "Que el acta deja constancia del estado y de quién recibe, y se hace siempre", "Que no hace falta si hay confianza", "Que se hace solo si algo falla", "El acta protege a todas las personas ante cualquier problema posterior."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula el costo total?", "Precio por equipo multiplicado por la cantidad", "Ese total luego se compara con el presupuesto disponible."),
        ("¿Qué configuración se descarta primero?", "La que no cumple los requisitos mínimos", "El precio se compara solo entre las que cumplen."),
        ("¿Qué se entrega junto al equipo?", "El acta de entrega", "Deja constancia del estado y de quién lo recibe."),
    ],
    op=("Un taller de ejemplo necesita 5 equipos con al menos 8 GB de RAM y 500 GB de disco, con un presupuesto de $2.000.000. Opción X: 8 GB, 500 GB, $360.000 por equipo. Opción Y: 16 GB, 1.000 GB, $480.000 por equipo. Opción Z: 8 GB, 250 GB, $300.000 por equipo. Descarta las que no cumplen, calcula el costo total de las que cumplen, recomienda una y escribe un límite.",
        "Z se descarta (250 GB es menos de 500 GB). X cumple: 5 × 360.000 = 1.800.000, cabe. Y cumple requisitos: 5 × 480.000 = 2.400.000, supera el presupuesto. Recomiendo X; sobran 200.000. Límite: precios de ejemplo y el armado lo hace personal autorizado con instructor y norma vigente.",
        ["descarta con los requisitos", "calcula costos y los compara con el presupuesto", "recomienda y declara un límite"],
        ["tabla de tres filas con criterios, costos y recomendación"],
        ["elegir Z por barata", "no multiplicar por 5", "no declarar límites"],
        "Pregunta: «¿qué opción se descarta primero y por qué?». Si no cita el disco, pídele que compare cada opción con los requisitos."),
    reinforce="Haz una tabla de dos configuraciones inventadas con RAM, disco y precio, y marca cuál cumple un requisito que tú elijas.",
    extend="Explica por qué cumplir los requisitos es más importante que elegir la opción más barata.",
)

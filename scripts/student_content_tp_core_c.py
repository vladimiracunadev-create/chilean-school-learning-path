"""Conectividad y Redes TP 3.º y 4.º medio: OAE-07 (redes inalámbricas), OAE-08 (servicios de intranet e internet) y OAE-09 (mantenimiento y actualización de hardware, solo conceptos). Datos y redes inventados; sin equipos ni software."""
from __future__ import annotations

from tp_core_common import build

O7 = "TP-CORE-3y4-OAE-07"
O8 = "TP-CORE-3y4-OAE-08"
O9 = "TP-CORE-3y4-OAE-09"
AVISO = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). «Biblioteca Los Pinos»: sala de lectura de 20 m por 10 m, con hasta 60 personas conectadas a la vez y 2 puntos de acceso Wi-Fi en el techo, cada uno con capacidad de ejemplo para 40 dispositivos. "
     "Redes previstas: «Personal» (con clave) y «Visitas» (separada de la del personal). Roles: técnico, administradora de la biblioteca, usuarios. Documentos: plano de cobertura, hoja de configuración y registro de pruebas.")
build(
    O7, 1, F,
    use="Aprenderé qué es una red inalámbrica, qué documentos y roles tiene su proyecto y qué riesgos de seguridad, privacidad y trabajo en terreno hay (solo conceptos).",
    prior=["Sé qué es una red LAN.", "Sé qué es un punto de acceso.", "Sé multiplicar y comparar."],
    explain=[
        "Una red inalámbrica local, o WLAN, conecta dispositivos mediante ondas de radio, sin cable entre el equipo y la red. Se conoce como Wi-Fi y sigue la familia de estándares IEEE 802.11. El punto de acceso es el equipo que conecta los dispositivos inalámbricos con la red cableada, y cada uno atiende hasta un número limitado de dispositivos a la vez.",
        "Como las ondas atraviesan paredes, cualquier persona cercana podría intentar conectarse. Por eso se usa cifrado (por ejemplo WPA2 o WPA3), claves fuertes y una red de visitas separada de la del personal. Se respeta la privacidad: el técnico mide cobertura y calidad, y no revisa el contenido que las personas envían. La autoridad de telecomunicaciones fija reglas sobre el uso de las frecuencias y la potencia: se cumple la norma vigente.",
        "Instalar puntos de acceso implica trabajo en altura, alimentación eléctrica y cableado, por lo que lo hace personal autorizado." + AVISO,
    ],
    vocab=[("red inalámbrica (WLAN)", "red que conecta dispositivos por ondas de radio"), ("Wi-Fi", "nombre común de las redes del estándar IEEE 802.11"), ("punto de acceso", "equipo que conecta dispositivos inalámbricos con la red cableada"), ("cifrado", "protección que vuelve ilegibles los datos para quien no los debe ver"), ("red de visitas", "red separada para invitados"), ("plano de cobertura", "plano que muestra la intensidad de señal en cada zona")],
    worked=[
        ("Capacidad de los puntos de acceso", "Un local de ejemplo tiene 3 puntos de acceso de 30 dispositivos cada uno. ¿Cuál es su capacidad total?", ["Se multiplican los puntos por su capacidad.", "3 × 30 = 90."], "90 dispositivos"),
        ("Red de visitas", "¿Por qué una biblioteca de ejemplo separa la red de visitas de la del personal?", ["Las visitas son personas externas y no deben llegar a los recursos internos.", "Separar limita el acceso a los datos del personal."], "Para proteger los datos del personal"),
    ],
    mistakes=[("Dejar la red del personal sin clave «para que sea más fácil».", "Cualquier persona cercana podría conectarse y ver recursos internos.", "Usa cifrado y una clave fuerte, y deja a las visitas en otra red."),
              ("Revisar los sitios que visitan las personas «para entender la carga».", "Eso invade la privacidad; la medición debe ser de la red, no del contenido.", "Usa solo estadísticas generales y con autorización.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es un punto de acceso?", "Un equipo que conecta dispositivos inalámbricos con la red cableada", "Un cable que une dos switches", "Un programa para dibujar planos", "El punto de acceso es el puente entre el aire y la red cableada."),
        ("abc", "¿Por qué se separa la red de visitas de la del personal?", "Para limitar el acceso de personas externas a los recursos del personal", "Para que la señal llegue más lejos", "Para que haya más puntos de acceso", "La separación protege los datos y los equipos internos."),
        ("abc", "¿Cómo transmite una red inalámbrica?", "Mediante ondas de radio", "Mediante cables de cobre", "Mediante luz por un hilo de vidrio", "La red inalámbrica no necesita cable entre el equipo y el punto de acceso."),
        ("=", "{F} ¿Cuál es la capacidad total de los 2 puntos de acceso en dispositivos?", "2*40", "Se multiplican los puntos de acceso por su capacidad.", " dispositivos"),
        ("abc", "{F} Si cada persona usa un dispositivo, ¿alcanza la capacidad para 60 personas?", "Sí: 80 dispositivos alcanzan para 60", "No: faltan 20 dispositivos", "No se puede saber", "La capacidad total es 80 y el uso es 60."),
        ("abc", "{F} ¿Quién autoriza la instalación en la biblioteca?", "La administradora de la biblioteca", "Cualquier visitante", "El primer usuario que se conecte", "La ficha asigna la responsabilidad del proyecto a la administradora."),
        ("=", "{F} Si cada una de las 60 personas usa 2 dispositivos, ¿cuántos dispositivos hay en total?", "60*2", "Se multiplica el número de personas por los dispositivos de cada una.", " dispositivos"),
        ("abc", "{F} Con 2 dispositivos por persona, ¿qué ocurre con la capacidad?", "No alcanza: hay 120 dispositivos y la capacidad es 80", "Alcanza con 40 sobrantes", "Alcanza justo", "120 es mayor que 80, por lo que hay que ampliar la capacidad."),
        ("=", "{F} Con 2 dispositivos por persona, ¿cuántos dispositivos exceden la capacidad?", "60*2-2*40", "Se resta la capacidad total a los dispositivos presentes.", " dispositivos"),
        ("abc", "{F} Alguien propone dejar la red «Personal» sin clave para que sea más fácil. ¿Qué respondes?", "Que debe tener cifrado y clave fuerte, porque cualquier persona cercana podría conectarse", "Que sin clave es más segura", "Que la clave solo sirve para las visitas", "Una red abierta no protege los recursos del personal."),
        ("abc", "{F} Un técnico quiere revisar los sitios que visitan las personas «para entender la carga». ¿Qué corresponde?", "No revisar el contenido: usar solo estadísticas generales de la red, con autorización", "Revisarlos sin avisar", "Revisarlos y anotarlos en una lista", "La privacidad exige medir la red sin mirar lo que hacen las personas."),
        ("abc", "{F} Una visita pide la clave de la red «Personal». ¿Qué corresponde?", "Indicarle la red «Visitas» y no compartir la clave del personal", "Darle la clave del personal", "Anotar la clave en un papel visible", "Compartir la clave del personal expone recursos internos."),
        ("abc", "Un compañero propone subir al techo a instalar un punto de acceso, aunque no es personal autorizado. ¿Qué corresponde?", "No hacerlo: el trabajo en altura y con electricidad lo hace personal autorizado", "Hacerlo con cuidado", "Hacerlo si hay una escalera firme", "Ese trabajo exige formación, protección y norma vigente."),
    ],
    ctx=("abc", "Una usuaria de la biblioteca de ejemplo se queja de que la señal es débil y pide que subas la potencia al máximo. ¿Qué respondes?", "Que primero se mide la señal y que la potencia está limitada por la norma vigente y por la interferencia que causaría", "Que lo harás de inmediato", "Que no se puede hacer nada nunca", "La decisión se basa en mediciones y en las reglas de uso de frecuencias."),
    sc=[
        ("En Conectividad y Redes: ¿para qué se usa una red de visitas separada?", "Para que las visitas no accedan a los recursos del personal", "La separación limita el acceso y el daño posible."),
        ("¿Qué no hace el técnico al medir la red?", "Revisar el contenido que envían las personas", "El técnico respeta la privacidad de las personas durante la medición."),
        ("¿Quién instala puntos de acceso en altura?", "Personal autorizado", "Hay riesgo de caídas y de electricidad."),
    ],
    op=("Un club de ejemplo tiene 45 personas y 3 dispositivos por persona en su peor momento. Tiene 4 puntos de acceso de 40 dispositivos cada uno. Calcula si alcanza la capacidad, escribe dos reglas de seguridad para la red del personal y una regla de privacidad para el técnico.",
        "Dispositivos: 45 × 3 = 135. Capacidad: 4 × 40 = 160, que alcanza para 135. Reglas de seguridad: cifrado con clave fuerte; red de visitas separada. Privacidad: el técnico no revisa el contenido que envían las personas.",
        ["calcula dispositivos y capacidad", "escribe dos reglas de seguridad adecuadas", "incluye una regla de privacidad"],
        ["hoja con cálculos y tres reglas"],
        ["olvidar multiplicar por 3", "proponer una red sin clave", "no mencionar privacidad"],
        "Pregunta: «¿por qué se suman las capacidades?». Si no responde, pídele que dibuje los cuatro puntos y escriba 40 en cada uno."),
    reinforce="Dibuja el plano de una sala con dos puntos de acceso y escribe cuántos dispositivos atiende cada uno según una capacidad inventada.",
    extend="Explica por qué la autorización escrita es importante antes de medir una red inalámbrica ajena.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (glosario y valores de ejemplo). SSID: nombre visible de la red inalámbrica. Banda de 2,4 GHz: más alcance, menos velocidad y más interferencia; en ella los canales 1, 6 y 11 no se solapan entre sí. "
     "Banda de 5 GHz: menos alcance, más velocidad y menos interferencia. Cifrado: WPA2 o WPA3 protege los datos; una red abierta no cifra. Intensidad de señal en dBm: son números negativos y mientras más cerca de 0, más fuerte. "
     "Valores de ejemplo: mejor que −65 dBm, buena; entre −65 y −75 dBm, aceptable; peor que −75 dBm, mala.")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario de las redes inalámbricas (SSID, bandas, canales, cifrado, dBm) y los documentos del proyecto.",
    prior=["Sé qué es una red inalámbrica.", "Sé qué es un punto de acceso.", "Sé comparar números negativos."],
    explain=[
        "Una red inalámbrica tiene un nombre visible, el SSID, y trabaja en bandas de frecuencia. La banda de 2,4 GHz llega más lejos y atraviesa mejor las paredes, pero es más lenta y tiene más interferencia. La de 5 GHz es más rápida y con menos interferencia, pero llega menos lejos. Dentro de cada banda hay canales: en 2,4 GHz los canales 1, 6 y 11 no se solapan, así que puntos de acceso vecinos deben usar canales distintos de ese grupo.",
        "La intensidad de la señal se mide en dBm. Son números negativos: −50 dBm es más fuerte que −70 dBm, porque está más cerca de cero. Con los valores de ejemplo, una señal mejor que −65 es buena y peor que −75 es mala. El cifrado WPA2 o WPA3 protege lo que viaja por el aire; ocultar el nombre de la red no protege los datos ni reemplaza al cifrado.",
        "El proyecto se apoya en documentos: el plano de cobertura (señal en cada zona), la hoja de configuración (SSID, banda, canal, tipo de cifrado y responsable; sin escribir las claves) y el registro de pruebas. Las claves nunca se anotan en documentos que circulen." + AVISO,
    ],
    vocab=[("SSID", "nombre visible de una red inalámbrica"), ("banda", "rango de frecuencias que usa la red, como 2,4 GHz o 5 GHz"), ("canal", "subdivisión de una banda"), ("dBm", "unidad de intensidad de señal; números negativos"), ("WPA2 / WPA3", "formas de cifrar una red inalámbrica"), ("hoja de configuración", "documento con los ajustes de cada equipo, sin claves"), ("interferencia", "señales que se molestan entre sí")],
    worked=[
        ("Comparar señales", "¿Cuál señal es más fuerte: −50 dBm o −70 dBm?", ["Los dBm son negativos; mientras más cerca de 0, más fuerte.", "−50 está más cerca de 0 que −70."], "−50 dBm"),
        ("Elegir la banda", "Un punto de acceso debe cubrir una bodega lejana con paredes gruesas. ¿Qué banda conviene?", ["Las paredes debilitan la señal.", "La banda de 2,4 GHz tiene más alcance."], "2,4 GHz"),
    ],
    mistakes=[("Pensar que −80 dBm es mejor que −50 dBm porque 80 es mayor que 50.", "Con números negativos, el valor más cercano a cero es el más fuerte.", "Compara con el signo: −50 es mayor que −80."),
              ("Creer que ocultar el SSID protege los datos.", "Ocultar el nombre no cifra la información ni evita que otros detecten la red.", "Usa cifrado y una clave fuerte.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el SSID?", "El nombre visible de una red inalámbrica", "La clave de la red", "La dirección del router", "El SSID es el nombre que ves al buscar redes."),
        ("abc", "¿Qué banda tiene más alcance?", "La de 2,4 GHz", "La de 5 GHz", "Ninguna", "La banda de 2,4 GHz llega más lejos, aunque es más lenta."),
        ("abc", "¿Qué canales de 2,4 GHz no se solapan entre sí?", "1, 6 y 11", "1, 2 y 3", "4, 5 y 6", "Los canales 1, 6 y 11 están separados lo suficiente para no molestarse."),
        ("abc", "{F} ¿Cuál señal es más fuerte?", "−55 dBm", "−72 dBm", "Son iguales", "−55 está más cerca de 0 que −72."),
        ("abc", "{F} Una señal de −70 dBm, ¿cómo se clasifica con los valores de ejemplo?", "Aceptable", "Buena", "Mala", "Está entre −65 y −75 dBm, que es el rango aceptable."),
        ("abc", "{F} ¿Qué hace el cifrado WPA3?", "Protege los datos que viajan por el aire", "Aumenta la velocidad", "Oculta el nombre de la red", "El cifrado vuelve ilegible el contenido para quien no tiene la clave."),
        ("abc", "{F} Dos puntos de acceso vecinos están en los canales 1 y 3 de 2,4 GHz. ¿Qué problema puede ocurrir?", "Interferencia, porque el canal 3 se solapa con el 1", "Ninguno, porque son distintos", "Se apagan los dos", "Solo 1, 6 y 11 no se solapan; el 3 invade al 1."),
        ("abc", "{F} Para una sala de reuniones a 5 m del punto de acceso con pocas paredes, ¿qué banda conviene si se busca velocidad?", "La de 5 GHz", "La de 2,4 GHz", "Ninguna", "A corta distancia la banda de 5 GHz da más velocidad y menos interferencia."),
        ("=", "{F} La diferencia entre −60 dBm y −72 dBm (restando los valores sin signo) es de cuántos dB?", "72-60", "Se resta el valor más grande al más pequeño sin signo.", " dB"),
        ("abc", "{F} Un informe dice: «−80 dBm, señal excelente, porque 80 es un número grande». ¿Cuál es el error?", "Con números negativos, −80 está lejos de 0: es una señal mala", "Ninguno, el informe está bien", "La señal excelente es −100 dBm", "Mientras más cerca de 0, más fuerte; −80 es peor que −75."),
        ("abc", "{F} Un técnico afirma: «ocultando el SSID la red queda protegida». ¿Qué respondes?", "Ocultar el nombre no cifra los datos; hace falta WPA2 o WPA3 y una clave fuerte", "Tiene razón: si no se ve, no se puede usar", "La protección depende solo de la banda", "El nombre oculto igual se puede detectar y no protege el contenido."),
        ("abc", "{F} Tres puntos de acceso vecinos usan canales 1, 6 y 6 de 2,4 GHz. ¿Qué cambio conviene?", "Cambiar el tercero al canal 11", "Cambiar el primero al 2", "No cambiar nada", "Con canales 1, 6 y 11 ninguno se solapa."),
        ("abc", "{F} ¿Qué NO debe anotarse en la hoja de configuración que circula?", "La clave de la red", "El SSID", "La banda y el canal", "La clave es una credencial y no se escribe en documentos que circulan."),
    ],
    ctx=("abc", "Un cliente de ejemplo se queja de lentitud. Mides −85 dBm en su escritorio, lejos del punto de acceso. ¿Cuál es la causa más razonable que mencionas?", "Una señal mala por distancia u obstáculos: conviene revisar la ubicación del punto de acceso o agregar otro, con aprobación", "Que el cable de su computador está cortado", "Que la red está hackeada", "−85 dBm es peor que −75, es decir, señal mala; se propone revisar la cobertura."),
    sc=[
        ("En Conectividad y Redes: ¿cuál señal es más fuerte, −45 o −75 dBm?", "−45 dBm", "Con números negativos, el valor más cercano a cero es el más fuerte."),
        ("¿Qué canales de 2,4 GHz no se solapan?", "El 1, el 6 y el 11", "Evitan interferencia entre puntos de acceso vecinos."),
        ("¿Qué no se escribe en la hoja de configuración que circula?", "La clave de la red", "Las claves se guardan de forma segura."),
    ],
    op=("Un taller de ejemplo tiene tres puntos de acceso vecinos en 2,4 GHz. Se mide la señal en su escritorio más lejano: −58, −71 y −79 dBm. Propón un canal para cada punto de acceso para evitar interferencias, clasifica las tres señales con los valores de la ficha 2 y escribe qué dato de la hoja de configuración no incluirías.",
        "Canales: 1, 6 y 11. Señales: −58 buena; −71 aceptable; −79 mala. No incluiría la clave de la red en la hoja que circula.",
        ["propone canales 1, 6 y 11", "clasifica bien las tres señales", "indica que la clave no se escribe"],
        ["tabla con punto, canal, señal y clasificación"],
        ["usar canales 1, 2 y 3", "pensar que −79 es mejor que −58", "escribir la clave en la hoja"],
        "Pregunta: «¿por qué elegiste esos canales?». Si no sabe, repasa que 1, 6 y 11 no se solapan."),
    reinforce="Ordena de más fuerte a más débil estas señales de ejemplo: −82, −49, −66, −71.",
    extend="Explica por qué una banda más rápida no siempre es la mejor opción para cubrir una zona grande.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (caso de cobertura de ejemplo). Tres salas en fila, cada una de 10 m de largo (S1, S2, S3), con un punto de acceso en el centro de cada una (AP-1, AP-2, AP-3) en la banda de 2,4 GHz. Capacidad de ejemplo de cada punto: 40 dispositivos. "
     "Usuarios (un dispositivo cada uno): S1, 25; S2, 45; S3, 20. Mediciones de ejemplo: S1 centro −40 dBm; S1 esquina −58 dBm; S2 esquina −72 dBm; S3 esquina −79 dBm. Meta: señal mejor o igual que −75 dBm en toda la sala. "
     "Valores de ejemplo: mejor que −65 dBm, buena; entre −65 y −75, aceptable; peor que −75, mala.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un caso de cobertura y capacidad: qué zonas cumplen la meta, dónde hay sobrecarga y qué canales evitan interferencia.",
    prior=["Sé comparar señales en dBm.", "Sé qué canales no se solapan.", "Sé sumar y restar."],
    explain=[
        "Analizar una red inalámbrica en un caso tiene dos preguntas: ¿llega buena señal a todas las zonas? y ¿alcanzan los puntos de acceso para los usuarios? La primera se responde comparando las mediciones de señal con la meta del proyecto. La segunda se responde comparando los usuarios de cada zona con la capacidad del punto de acceso que la atiende.",
        "También hay que cuidar la interferencia entre puntos de acceso vecinos: en 2,4 GHz se asignan canales 1, 6 y 11 sin repetir en los vecinos. Subir la potencia de todos los puntos al máximo no es una solución: aumenta la interferencia y puede incumplir la norma vigente sobre potencia. Las soluciones se proponen con base en mediciones: mover un punto de acceso, agregar otro o repartir la carga entre bandas.",
        "Todo se escribe como recomendación con sus datos y su aprobación. Las mediciones de este caso son de ejemplo, y las reales las toma personal autorizado." + AVISO,
    ],
    vocab=[("zona sin cobertura", "lugar donde la señal es peor que la meta"), ("sobrecarga", "más usuarios que la capacidad del punto de acceso"), ("repartir la carga", "distribuir usuarios entre puntos de acceso o bandas"), ("asignación de canales", "elegir canales distintos para puntos vecinos"), ("potencia máxima", "límite de potencia que fija la norma")],
    worked=[
        ("Cumplir la meta", "La meta es −75 dBm o mejor. Una esquina de ejemplo mide −68 dBm. ¿Cumple?", ["−68 está más cerca de 0 que −75.", "Por lo tanto es mejor que la meta."], "Sí, cumple"),
        ("Sobrecarga", "Un punto de acceso de ejemplo atiende 50 usuarios y su capacidad es 40. ¿Cuántos usuarios exceden la capacidad?", ["Se restan la capacidad a los usuarios.", "50 − 40 = 10."], "10 usuarios"),
    ],
    mistakes=[("Subir la potencia de todos los puntos de acceso al máximo para «arreglar todo».", "Aumenta la interferencia entre vecinos y puede incumplir la norma vigente.", "Ajusta según mediciones y asigna canales distintos."),
              ("Resolver la sobrecarga sin medir cuántos usuarios hay en cada sala.", "Sin datos puede ampliarse donde no hace falta.", "Compara usuarios y capacidad sala por sala.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una zona sin cobertura?", "Un lugar donde la señal es peor que la meta del proyecto", "Un lugar donde no hay personas", "Un lugar con muchos cables", "La zona sin cobertura se define con la meta de señal del proyecto."),
        ("abc", "En Conectividad y Redes: ¿qué es la interferencia?", "Señales que se molestan entre sí y empeoran la conexión", "Un cable cortado", "Un virus", "La interferencia aparece cuando dos señales usan canales que se solapan."),
        ("abc", "¿Qué muestra un plano de cobertura?", "La intensidad de señal en cada zona", "La cantidad de cables del rack", "El costo de los equipos", "Sirve para decidir si hace falta mover o agregar puntos de acceso."),
        ("abc", "{F} ¿Qué mediciones cumplen la meta de −75 dBm o mejor?", "S1 centro, S1 esquina y S2 esquina", "Solo S1 centro", "S2 y S3 esquinas", "−79 de S3 es peor que −75; las otras tres cumplen."),
        ("abc", "{F} ¿Qué sala supera la capacidad de su punto de acceso?", "S2, con 45 usuarios", "S1, con 25 usuarios", "S3, con 20 usuarios", "Solo S2 supera los 40 dispositivos."),
        ("=", "{F} ¿Cuántos usuarios hay en total en las tres salas?", "25+45+20", "Se suman los usuarios de las tres salas.", " usuarios"),
        ("=", "{F} ¿Cuántos usuarios exceden la capacidad del AP-2?", "45-40", "A los usuarios de S2 se les resta la capacidad del punto de acceso.", " usuarios"),
        ("abc", "{F} Los puntos de acceso AP-1, AP-2 y AP-3 usan los canales 1, 6 y 11. ¿Se solapan?", "No: son canales que no se solapan", "Sí, porque son tres puntos de acceso", "Sí, porque están en la misma banda", "Los canales 1, 6 y 11 no se solapan, aun estando en la misma banda."),
        ("abc", "{F} Si AP-2 y AP-3 usaran ambos el canal 6, ¿qué ocurriría?", "Habría interferencia entre ellos, que son vecinos", "Aumentaría la capacidad", "No ocurriría nada", "Puntos vecinos en el mismo canal se molestan entre sí."),
        ("abc", "{F} En S3 la esquina mide −79 dBm. ¿Qué corresponde?", "Es una señal mala bajo la meta: se propone revisar la ubicación o agregar cobertura, con aprobación", "Es excelente", "Se sube la potencia al máximo de todos los puntos", "−79 dBm es peor que −75; se propone una solución con base en mediciones."),
        ("abc", "{F} Un técnico sube la potencia al máximo de todos los puntos para «arreglar todo». ¿Qué riesgo tiene?", "Más interferencia entre vecinos y posible incumplimiento de la norma sobre potencia", "Ninguno", "La red se vuelve más lenta solo para las visitas", "Más potencia no siempre mejora; puede empeorar la interferencia y salir de la norma."),
        ("abc", "{F} ¿Qué medida atiende la sobrecarga de S2 sin tocar S1 y S3?", "Agregar un segundo punto de acceso en S2 o repartir la carga, con aprobación", "Subir la potencia en S1", "Quitar a 5 usuarios de S3", "La sobrecarga está solo en S2, que es donde se actúa."),
        ("=", "{F} Con un segundo punto de acceso en S2, la capacidad de esa sala sería de 80. ¿Cuántos dispositivos más podrían conectarse?", "80-45", "A la nueva capacidad se le restan los 45 usuarios de S2.", " dispositivos"),
    ],
    ctx=("abc", "Un usuario de S3 se queja de que se corta la conexión. Tú mediste −79 dBm en su esquina. ¿Qué respondes?", "Que la señal está bajo la meta y que propondrás mover o agregar un punto de acceso, con aprobación", "Que es culpa de su celular", "Que subirás la potencia de toda la red al máximo", "Con la medición se propone una mejora, no una solución al azar."),
    sc=[
        ("En Conectividad y Redes: ¿cuándo hay sobrecarga?", "Cuando los usuarios superan la capacidad del punto de acceso", "La sobrecarga se calcula comparando usuarios y capacidad."),
        ("¿Por qué no subir la potencia al máximo en todos los puntos?", "Puede aumentar la interferencia y salirse de la norma", "Las soluciones se basan en mediciones."),
        ("¿Qué canales se asignan a puntos vecinos en 2,4 GHz?", "Los canales 1, 6 y 11 sin repetirlos", "Con esos canales los puntos de acceso vecinos no se molestan entre sí."),
    ],
    op=("Una escuela de ejemplo tiene tres salas en fila. Mediciones en las esquinas más lejanas: sala A, −62 dBm; sala B, −77 dBm; sala C, −70 dBm. Usuarios: A, 30; B, 38; C, 55. Cada punto de acceso admite 40 dispositivos y la meta es −75 dBm o mejor. Indica qué zonas cumplen la señal, qué sala está sobrecargada y qué asignación de canales propones para 2,4 GHz.",
        "Señal: A cumple; B (−77) no cumple; C cumple. Sobrecarga: C tiene 55 usuarios, 15 por encima de 40. Canales: A en 1, B en 6 y C en 11. Propuestas: revisar la cobertura de B y agregar capacidad en C, con aprobación y mediciones reales.",
        ["compara señales con la meta", "detecta la sobrecarga de C", "asigna canales 1, 6 y 11"],
        ["tabla con sala, señal, usuarios y observaciones"],
        ["decir que B cumple", "olvidar la sobrecarga", "repetir canales vecinos"],
        "Pregunta: «¿qué sala tiene mala señal y cuál sobrecarga?». Si las mezcla, pídele que las anote en columnas separadas."),
    reinforce="Con una sala de 35 usuarios y un punto de acceso de 30, calcula cuántos usuarios sobran.",
    extend="Explica por qué medir antes de proponer una mejora evita gastar en el lugar equivocado.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (propuestas de ejemplo para un colegio). Se necesita cubrir 3 salas con 90 dispositivos en total y proteger los datos del personal. Propuesta A: 2 puntos de acceso de 40 dispositivos, red abierta sin clave, $120.000. "
     "Propuesta B: 3 puntos de acceso de 40 dispositivos, red del personal con WPA3 y red de visitas separada, $210.000. Propuesta C: 3 puntos de acceso de 40 dispositivos, una sola red con WPA3 para todos, $200.000. "
     "Criterios del proyecto: capacidad suficiente para 90 dispositivos, cifrado en la red del personal y red de visitas separada. Todos los precios son de ejemplo.")
build(
    O7, 4, F,
    use="Aprenderé a comparar propuestas de red inalámbrica con criterios de capacidad y seguridad, y a escribir una recomendación con límites.",
    prior=["Sé calcular capacidad y sobrecarga.", "Sé qué son el cifrado y la red de visitas.", "Sé comparar costos."],
    explain=[
        "Elegir una solución inalámbrica es una decisión con criterios: que la capacidad alcance para los dispositivos, que la red del personal esté cifrada, que las visitas estén separadas, y que se cumpla la norma vigente. Se calcula cada criterio por propuesta, se descartan las que incumplen alguno indispensable y, entre las que cumplen, se compara el costo.",
        "Una red abierta sin clave deja que cualquier persona cercana se conecte y vea recursos internos; por eso incumple el criterio de cifrado. Una sola red para todos, aunque esté cifrada, mezcla visitas y personal: si la clave se comparte con visitas, todos quedan en la misma red. La separación es una medida adicional que limita el daño.",
        "La recomendación incluye los cálculos, la propuesta elegida y los límites: precios y capacidades son de ejemplo, y en un proyecto real se mide la cobertura en el sitio, se cumple la norma vigente y se pide autorización. Este cuaderno no te habilita para instalar." + AVISO,
    ],
    vocab=[("criterio indispensable", "condición que la propuesta debe cumplir sí o sí"), ("capacidad", "dispositivos que puede atender un punto de acceso"), ("separación de redes", "visitas y personal en redes distintas"), ("recomendación", "decisión escrita con los datos que la respaldan"), ("límite", "aquello que la recomendación no puede asegurar")],
    worked=[
        ("Capacidad suficiente", "Una propuesta de ejemplo tiene 2 puntos de acceso de 40 dispositivos para 100 dispositivos. ¿Alcanza?", ["Capacidad: 2 × 40 = 80.", "80 es menor que 100."], "No alcanza"),
        ("Descartar por seguridad", "Una propuesta de ejemplo deja la red del personal abierta. El criterio exige cifrado. ¿Se acepta?", ["La red abierta no cifra.", "Incumple un criterio indispensable."], "No se acepta"),
    ],
    mistakes=[("Elegir la propuesta más barata aunque deje la red del personal abierta.", "Incumple un criterio indispensable de seguridad.", "Primero cumple los criterios y luego compara el costo."),
              ("Dar por buena la capacidad sin sumar los dispositivos de todas las salas.", "La suma de dispositivos es el dato base del cálculo.", "Suma todos los dispositivos antes de comparar.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es la capacidad de un punto de acceso?", "El número de dispositivos que puede atender", "El largo de su cable", "El precio del equipo", "La capacidad indica cuántos dispositivos atiende a la vez."),
        ("abc", "En Conectividad y Redes: ¿por qué una red abierta no cumple el criterio de cifrado?", "Porque no protege los datos que viajan por el aire", "Porque tiene demasiados puntos de acceso", "Porque usa canales 1, 6 y 11", "Una red abierta no cifra y cualquiera cercano puede conectarse."),
        ("abc", "¿Qué es un criterio indispensable?", "Una condición que la propuesta debe cumplir sí o sí", "Una opinión del instalador", "El precio más bajo", "Si no se cumple, la propuesta se descarta aunque tenga otras ventajas."),
        ("=", "{F} ¿Cuántos dispositivos soporta en total la propuesta A?", "2*40", "Son 2 puntos de acceso de 40 dispositivos.", " dispositivos"),
        ("=", "{F} ¿Cuántos dispositivos soporta en total la propuesta B?", "3*40", "Son 3 puntos de acceso de 40 dispositivos.", " dispositivos"),
        ("abc", "{F} ¿Qué propuesta no alcanza en capacidad para 90 dispositivos?", "La propuesta A", "La propuesta B", "La propuesta C", "A soporta 80 dispositivos, menos de 90."),
        ("abc", "{F} ¿Qué propuesta cumple capacidad, cifrado y red de visitas separada?", "La propuesta B", "La propuesta A", "La propuesta C", "C tiene una sola red para todos y A está abierta y sin capacidad suficiente."),
        ("=", "{F} ¿Cuántos pesos más cuesta la propuesta B que la propuesta C?", "210000-200000", "Se resta el precio de C al de B.", " pesos"),
        ("=", "{F} ¿Cuántos dispositivos de capacidad sobran en la propuesta B para 90 dispositivos?", "3*40-90", "A la capacidad se le restan los 90 dispositivos.", " dispositivos"),
        ("abc", "{F} Alguien dice: «elijamos la A, es la más barata». ¿Qué respondes?", "A no tiene capacidad ni cifrado, así que no cumple criterios indispensables", "Tiene razón: el costo manda", "A es mejor porque es abierta", "Los criterios indispensables se verifican antes que el costo."),
        ("abc", "{F} ¿Por qué C no cumple todos los criterios aunque cifre y tenga capacidad?", "Porque no separa la red de visitas de la del personal", "Porque no tiene puntos de acceso", "Porque cuesta más", "El criterio de separación de redes no se cumple en C."),
        ("abc", "{F} ¿Qué datos debe tener la recomendación para ser técnica?", "Capacidades, cifrado, separación de redes, costo y el criterio usado", "Solo la opinión del instalador", "El nombre del colegio", "Con esos datos otra persona puede comprobar la decisión."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los precios y capacidades son de ejemplo; en la realidad se mide la cobertura, se cumple la norma vigente y se pide autorización", "Ninguno, los números son exactos", "Que el cifrado no hace falta", "Los datos de la ficha son de ejemplo y no reemplazan una medición en el lugar."),
    ],
    ctx=("abc", "El director de ejemplo te pide poner la misma clave para personal y visitas «para no complicarse». ¿Qué respondes?", "Que conviene separar las redes porque las visitas no deben acceder a los recursos internos", "Que está bien, la clave no importa", "Que mejor no ponga ninguna clave", "La separación de redes limita el acceso de personas externas."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula la capacidad total?", "Puntos de acceso por capacidad de cada uno", "Es una estimación sencilla que se compara con los dispositivos."),
        ("¿Qué hace que una propuesta se descarte?", "Incumplir un criterio indispensable", "Una propuesta barata igualmente se descarta si incumple un criterio indispensable."),
        ("¿Para qué se separa la red de visitas?", "Para limitar el acceso a los recursos internos", "Las visitas son personas externas y no deben llegar a los recursos internos."),
    ],
    op=("Un taller de ejemplo debe cubrir 100 dispositivos y proteger la red del personal. Opción 1: 2 puntos de acceso de 50 dispositivos, una sola red con WPA3, $180.000. Opción 2: 3 puntos de acceso de 40 dispositivos, red del personal con WPA3 y visitas aparte, $250.000. Opción 3: 3 puntos de acceso de 40 dispositivos, red abierta, $190.000. Calcula la capacidad de cada opción, descarta las que no cumplen y recomienda con un límite.",
        "Capacidades: opción 1, 100; opción 2, 120; opción 3, 120. La opción 1 cumple capacidad y cifrado, pero no separa visitas. La opción 3 no tiene cifrado. La opción 2 cumple todo. Recomiendo la opción 2 por $250.000. Límite: precios de ejemplo y falta medir la cobertura en el lugar.",
        ["calcula la capacidad", "descarta con criterios", "recomienda con datos y límite"],
        ["tabla comparativa con criterios y recomendación"],
        ["elegir la más barata", "olvidar la separación de redes", "no declarar límites"],
        "Pregunta: «¿qué criterio incumple la opción 1?». Si no responde, pídele que compare cada opción con los tres criterios."),
    reinforce="Escribe tres criterios que usarías para elegir la red inalámbrica de una escuela.",
    extend="Explica por qué la separación de redes y el cifrado se complementan.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (oficina de ejemplo, inventada). «Taller Los Boldos» usa una intranet (sitio interno con documentos y formularios, accesible solo desde la red de la oficina), correo electrónico, un navegador para internet y una carpeta compartida en un servidor. "
     "Reglas de uso aceptable (de ejemplo): usar los servicios para el trabajo, no descargar programas de fuentes no confiables, no compartir claves y no reenviar datos de clientes sin autorización. Roles: persona usuaria y administradora de informática. "
     "Plan de pausas de ejemplo: en una jornada de 8 horas (480 minutos), 5 pausas de 10 minutos para descansar la vista y el cuerpo.")
build(
    O8, 1, F,
    use="Aprenderé qué son los servicios de intranet e internet, qué reglas de uso responsable existen y qué riesgos hay al usarlos.",
    prior=["Sé navegar por internet.", "Sé qué es un correo electrónico.", "Sé multiplicar y restar."],
    explain=[
        "Una intranet es una red o sitio interno de una institución: solo puede usarse desde su red o con una conexión autorizada. Internet es la red mundial a la que se conecta casi cualquier persona. Los servicios más usados son el correo electrónico, la navegación por páginas web, las carpetas compartidas y las videollamadas. Las herramientas de software, como el navegador o el programa de correo, permiten usarlos.",
        "Usar bien estos servicios es parte del trabajo. La política de uso aceptable de la institución fija reglas: usar los servicios para el trabajo, no descargar programas de fuentes no confiables, no compartir claves y cuidar los datos personales y de clientes. También se respetan los derechos de autor: no se usan películas, música ni programas copiados sin permiso. La ley vigente de protección de datos personales y las normas de la institución mandan.",
        "Los riesgos son los correos de engaño (phishing), los programas dañinos, la filtración de datos y la mala postura frente a la pantalla. Por eso se hacen pausas: descansar la vista y el cuerpo es parte de la ergonomía. Esta clase es conceptual y todos los nombres son inventados.",
    ],
    vocab=[("intranet", "sitio o red interna de una institución"), ("internet", "red mundial de redes"), ("política de uso aceptable", "reglas de la institución para usar sus servicios"), ("phishing", "mensaje de engaño que busca datos o claves"), ("derechos de autor", "derechos de quien creó una obra"), ("ergonomía", "cuidar la postura y el descanso al trabajar")],
    worked=[
        ("Minutos de pausa", "Un plan de ejemplo tiene 4 pausas de 15 minutos. ¿Cuántos minutos de pausa son?", ["Se multiplican las pausas por los minutos de cada una.", "4 × 15 = 60."], "60 minutos"),
        ("Quién accede a la intranet", "Una intranet de ejemplo es de una oficina. ¿Puede acceder cualquier persona de internet?", ["La intranet es interna.", "Solo se accede desde la red de la oficina o con conexión autorizada."], "No"),
    ],
    mistakes=[("Reenviar la lista de clientes a un correo personal para trabajar en casa.", "Son datos de clientes y salen del control de la institución.", "Pide autorización y usa un medio autorizado."),
              ("Usar la misma clave para el correo del trabajo y para un sitio de juegos.", "Si el sitio de juegos se filtra, el correo del trabajo queda expuesto.", "Usa claves distintas y largas para cada servicio.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una intranet?", "Un sitio o red interna de una institución", "La red mundial de redes", "Un virus", "La intranet es de uso interno, no abierta a todo internet."),
        ("abc", "En Conectividad y Redes: ¿qué es la política de uso aceptable?", "Las reglas de la institución para usar sus servicios", "Una lista de precios de internet", "Un tipo de cable", "Fija qué se puede y qué no se puede hacer con los servicios."),
        ("abc", "¿Qué es el phishing?", "Un mensaje de engaño para obtener datos o claves", "Un respaldo de archivos", "Una actualización", "El phishing busca engañar a la persona usuaria."),
        ("abc", "{F} ¿Quién puede acceder a la intranet del taller?", "Quienes estén en la red de la oficina o tengan conexión autorizada", "Cualquier persona de internet", "Solo los clientes externos", "La ficha dice que es accesible solo desde la red de la oficina."),
        ("=", "{F} ¿Cuántos minutos de pausa tiene el plan en la jornada?", "5*10", "Se multiplican las pausas por los minutos de cada una.", " minutos"),
        ("abc", "{F} ¿Por qué no se descargan programas de fuentes no confiables?", "Porque pueden traer programas dañinos", "Porque pesan mucho", "Porque son más lentos", "Una fuente no confiable puede entregar un programa con virus."),
        ("=", "{F} Si la jornada dura 480 minutos y 50 son de pausa, ¿cuántos minutos de trabajo hay?", "480-5*10", "A la jornada se le restan los minutos de pausa.", " minutos"),
        ("abc", "{F} Una persona recibe un correo inesperado que dice «factura urgente» con un adjunto. ¿Qué hace?", "No lo abre y avisa a la administradora de informática", "Lo abre rápido para saber qué es", "Lo reenvía a todos sus compañeros", "Un adjunto inesperado con apuro es señal de engaño."),
        ("abc", "{F} Una persona quiere reenviar la lista de clientes a su correo personal. ¿Corresponde?", "No sin autorización, porque son datos de clientes", "Sí, porque es su trabajo", "Sí, si borra el correo después", "Los datos de clientes no salen sin autorización."),
        ("abc", "{F} Un compañero usa la misma clave para el correo del taller y para un sitio de juegos. ¿Cuál es el riesgo?", "Si se filtra la clave del sitio de juegos, el correo del taller queda expuesto", "Ninguno, porque son sitios distintos", "Se gasta más internet", "Repetir claves hace que una filtración abra varios servicios."),
        ("abc", "Una persona descarga una película copiada en el computador de la oficina. ¿Qué principio se rompe?", "Los derechos de autor y la política de uso aceptable", "La ergonomía", "La puerta de enlace", "Usar obras sin permiso vulnera los derechos de autor y las reglas de la institución."),
        ("=", "{F} Una persona de ejemplo trabaja 6 horas con pausas de 10 minutos cada hora completa de trabajo (6 pausas). ¿Cuántos minutos de pausa acumula?", "6*10", "Se multiplican las pausas por los minutos de cada una.", " minutos"),
        ("abc", "{F} Una persona trabaja ocho horas sin ninguna pausa frente a la pantalla. ¿Qué principio se descuida?", "La ergonomía: la postura y el descanso", "La licencia de software", "El cifrado de la red", "Las pausas cuidan la vista y el cuerpo."),
    ],
    ctx=("abc", "Una compañera de ejemplo recibe un mensaje que dice «tu cuenta del taller se bloqueará: confirma tu clave en este enlace». ¿Qué le aconsejas?", "No abrir el enlace y avisar a la administradora de informática", "Confirmar la clave de inmediato", "Pedirle a otra persona que la confirme", "Un mensaje urgente con enlace que pide la clave es un engaño habitual."),
    sc=[
        ("En Conectividad y Redes: ¿qué diferencia hay entre intranet e internet?", "La intranet es interna de una institución y internet es la red mundial", "La diferencia principal está en quién puede acceder a cada una de las redes."),
        ("¿Qué haces con un adjunto inesperado?", "No lo abro y aviso a la administradora de informática", "Puede ser un engaño o un programa dañino."),
        ("¿Para qué sirven las pausas al usar pantallas?", "Para descansar la vista y el cuerpo", "Las pausas forman parte de la ergonomía y cuidan la vista y el cuerpo."),
    ],
    op=("Una escuela de ejemplo define una política de uso: (1) usar los servicios para el trabajo; (2) no compartir claves; (3) no descargar programas de fuentes no confiables; (4) hacer pausas. Escribe un caso de ejemplo en que alguien incumpla cada regla (cuatro casos cortos, sin datos reales) y qué acción corresponde en cada uno.",
        "(1) Alguien usa el computador para juegos en horario de trabajo: se le recuerda la regla. (2) Una persona le presta su clave a un compañero: se cambia la clave y se avisa a la administradora. (3) Descargan un programa desconocido: se desinstala con la administradora. (4) Trabajan toda la tarde sin pausas: se organiza un plan de pausas.",
        ["escribe cuatro casos distintos y coherentes", "relaciona cada caso con su regla", "propone una acción adecuada"],
        ["tabla de cuatro filas con regla, caso y acción"],
        ["usar datos reales de personas", "no relacionar con la regla", "acciones que invaden la privacidad"],
        "Pregunta: «¿qué regla incumple cada caso?». Si mezcla dos, pídele que escriba la regla al lado de cada caso."),
    reinforce="Escribe tres reglas de uso responsable de internet que seguirías en tu casa.",
    extend="Explica por qué el uso responsable de los servicios protege a la institución y a cada persona.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (glosario y ejemplos). URL de ejemplo: https://intranet.taller-ejemplo/documentos. Intranet: sitio interno de una institución. Navegador: programa para abrir páginas web. "
     "DNS: servicio que traduce nombres (como intranet.taller-ejemplo) a direcciones IP. HTTPS: conexión web cifrada, que muestra un candado en el navegador; el candado no garantiza que el sitio sea confiable, solo que la conexión está cifrada. "
     "VPN: conexión protegida a la red de la institución desde fuera. Nube: almacenamiento de archivos en servidores de un proveedor. Adjunto: archivo enviado con un correo. Caché: copia temporal guardada para que algo cargue más rápido. "
     "Límite de ejemplo del correo: 25 MB por mensaje.")
build(
    O8, 2, F,
    use="Aprenderé el vocabulario de los servicios de intranet e internet (URL, DNS, HTTPS, VPN, nube) y las herramientas con que se usan.",
    prior=["Sé qué es una intranet.", "Sé qué es una dirección IP.", "Sé qué es un correo."],
    explain=[
        "Para abrir un sitio, el navegador usa una URL, que es su dirección escrita en palabras. El servicio DNS traduce el nombre del servidor a una dirección IP, como una guía telefónica. Si la dirección comienza con HTTPS, la conexión entre el navegador y el servidor va cifrada y aparece un candado. El candado dice que la conexión está protegida, no que el sitio sea honesto: hay que fijarse también en el nombre del servidor.",
        "Para trabajar desde fuera de la oficina se usa una VPN, que crea una conexión protegida con la red de la institución. La nube es almacenamiento en servidores de un proveedor, y solo se usa el servicio que la institución autoriza. Un adjunto es un archivo enviado con el correo; los correos tienen un límite de tamaño, por eso para archivos grandes conviene compartir un enlace a una carpeta.",
        "La caché guarda copias temporales para que las páginas carguen más rápido, y comprimir archivos reduce su tamaño. Usar bien estas herramientas ahorra capacidad de la red. Cada institución define qué herramientas autoriza; los nombres de esta ficha son de ejemplo.",
    ],
    vocab=[("URL", "dirección de una página escrita en palabras"), ("DNS", "servicio que traduce nombres a direcciones IP"), ("HTTPS", "conexión web cifrada, con candado"), ("VPN", "conexión protegida a la red de la institución desde fuera"), ("nube", "almacenamiento en servidores de un proveedor"), ("adjunto", "archivo enviado con un correo"), ("caché", "copia temporal guardada para cargar más rápido")],
    worked=[
        ("Adjunto o enlace", "Quieres enviar un archivo de 60 MB y el correo admite 25 MB por mensaje. ¿Qué haces?", ["60 MB supera el límite de 25 MB.", "Compartes un enlace a una carpeta autorizada en vez de adjuntar el archivo."], "Compartir un enlace"),
        ("Qué muestra el candado", "Un sitio de ejemplo muestra el candado de HTTPS. ¿Qué significa?", ["El candado indica conexión cifrada.", "No garantiza que el sitio sea confiable."], "Conexión cifrada, no sitio confiable"),
    ],
    mistakes=[("Creer que si hay candado el sitio es seguro y honesto.", "El candado solo indica que la conexión está cifrada.", "Verifica además el nombre del servidor y la fuente."),
              ("Enviar un archivo muy grande como adjunto a muchas personas.", "Ocupa mucho espacio y puede superar el límite del correo.", "Comparte un enlace a una carpeta autorizada.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿para qué sirve el DNS?", "Para traducir nombres de servidores a direcciones IP", "Para cifrar los correos", "Para borrar archivos", "El DNS convierte un nombre en la dirección IP que usan los equipos."),
        ("abc", "En Conectividad y Redes: ¿qué indica el candado de HTTPS?", "Que la conexión está cifrada", "Que el sitio es honesto", "Que no hay virus", "El candado solo habla de la conexión."),
        ("abc", "¿Para qué se usa una VPN?", "Para conectarse de forma protegida a la red de la institución desde fuera", "Para subir la velocidad", "Para ocultar el nombre de la red", "Una VPN crea un túnel protegido hacia la red interna."),
        ("abc", "{F} ¿Qué parte de la URL es el nombre del servidor?", "intranet.taller-ejemplo", "documentos", "https", "El nombre del servidor va después de https:// y antes de la primera barra."),
        ("abc", "{F} ¿Qué servicio traduce intranet.taller-ejemplo a una dirección IP?", "El DNS", "La VPN", "El adjunto", "Traducir nombres a direcciones es la función del DNS."),
        ("abc", "{F} Una persona quiere trabajar desde su casa con los documentos de la intranet. ¿Qué herramienta usa?", "Una VPN autorizada", "Un adjunto", "La caché", "La VPN permite llegar a la red interna de forma protegida."),
        ("=", "{F} Un adjunto de 20 MB se envía a 15 personas. ¿Cuántos MB se envían en total?", "20*15", "Se multiplica el tamaño del adjunto por la cantidad de destinatarios.", " MB"),
        ("=", "{F} Si en vez se sube el archivo una vez a una carpeta compartida y se envía el enlace, ¿cuántos MB menos se mueven por la red que con los 15 adjuntos?", "20*15-20", "Se resta lo que se sube una sola vez a lo que se enviaría 15 veces.", " MB"),
        ("abc", "{F} Un archivo de 40 MB se quiere enviar como adjunto. ¿Qué pasa con el límite del correo?", "Lo supera, porque 40 MB es mayor que 25 MB", "Cabe, porque 40 es menor que 25", "No hay límite", "El límite de ejemplo es 25 MB por mensaje."),
        ("abc", "{F} Se comparan dos URL: https://intranet.taller-ejemplo/documentos y http://taller-ejemplo.verifica-clave/documentos. ¿Cuál es sospechosa?", "La segunda: tiene otro nombre de servidor y no usa conexión cifrada", "La primera, porque tiene candado", "Ninguna, porque son iguales", "El nombre del servidor de la segunda es distinto y no usa HTTPS."),
        ("abc", "Un compañero dice que, si un sitio tiene candado, se puede entregar cualquier dato sin problemas. ¿Qué respondes?", "El candado solo indica conexión cifrada; hay que confiar también en el nombre y en la fuente", "Tiene razón, el candado lo garantiza todo", "El candado significa que el sitio no puede ser falso", "Un sitio falso también puede usar HTTPS."),
        ("abc", "{F} ¿Para qué sirve la caché del navegador?", "Para guardar copias temporales que hacen cargar las páginas más rápido", "Para cifrar la contraseña", "Para borrar el historial automáticamente", "La caché evita pedir de nuevo lo que ya se descargó."),
        ("abc", "{F} Una persona quiere guardar archivos de la oficina en un servicio de nube gratuito que ella eligió. ¿Qué corresponde?", "Usar solo el servicio de nube que la institución autoriza", "Usar cualquiera, porque es gratis", "Compartir la clave con sus compañeros", "Los datos de la institución se guardan en servicios autorizados."),
    ],
    ctx=("abc", "Estás en tu casa y necesitas abrir un documento de la intranet. ¿Qué haces?", "Uso la VPN autorizada por la institución", "Pido la clave de un compañero y entro desde su cuenta", "Copio el documento en un servicio gratuito de internet", "La VPN permite acceder de forma protegida y con tu propia cuenta."),
    sc=[
        ("En Conectividad y Redes: ¿qué significa HTTPS?", "Conexión web cifrada", "El cifrado protege lo que viaja entre el navegador y el servidor."),
        ("¿Qué hace el DNS?", "Traduce nombres a direcciones IP", "Así el navegador sabe a qué servidor ir."),
        ("¿Qué haces con un archivo que supera el límite del correo?", "Comparto un enlace a una carpeta autorizada", "Así se evitan adjuntos pesados y repetidos que gastan capacidad de red."),
    ],
    op=("Una oficina de ejemplo debe compartir un informe de 50 MB con 12 personas. El correo admite 25 MB por mensaje. Escribe dos formas de hacerlo con las herramientas de la ficha 2, calcula cuántos MB se enviarían si se mandara como adjunto a las 12 personas (aunque no se pueda) y cuántos si se sube una vez y se comparte un enlace. Indica cuál usarías y por qué.",
        "Formas: compartir un enlace a una carpeta autorizada de la intranet, o comprimir y dividir el archivo (menos recomendado). Adjunto a 12: 50 × 12 = 600 MB. Subida única: 50 MB. Usaría el enlace, porque supera el límite del correo y mueve 550 MB menos.",
        ["propone dos formas válidas", "calcula 600 y 50 MB", "elige y justifica"],
        ["hoja con las dos formas, el cálculo y la elección"],
        ["proponer un servicio gratuito no autorizado", "multiplicar mal", "no considerar el límite del correo"],
        "Pregunta: «¿por qué no adjuntar?». Si no menciona el límite, pídele que compare 50 MB con 25 MB."),
    reinforce="Anota tres ejemplos de URL inventadas y marca cuáles son HTTPS.",
    extend="Explica por qué usar solo servicios autorizados protege los datos de la institución.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (caso de eficiencia de ejemplo). En «Taller Los Boldos» 20 personas comparten una conexión a internet de 100 Mbps. Casos: (a) enviar un informe de 30 MB a 10 personas como adjunto, con límite de 25 MB por mensaje; "
     "(b) descargar una actualización de 600 MB en cada uno de los 20 computadores; (c) una videollamada de 2 Mbps por persona con 10 personas conectadas. Herramientas disponibles: carpeta compartida de la intranet; compresor de archivos (reduce el informe a 20 MB); "
     "servidor interno de actualizaciones (descarga una vez desde internet y luego reparte por la red local). 1 MB son 8 Mb (megabits).")
build(
    O8, 3, F,
    use="Aprenderé a analizar un caso y elegir herramientas de intranet e internet que ahorren capacidad de red y cumplan las reglas.",
    prior=["Sé convertir MB a Mb.", "Sé qué es una carpeta compartida.", "Sé calcular tiempos de descarga."],
    explain=[
        "Un servicio se usa de manera eficiente cuando logra su objetivo con el menor gasto de capacidad de red y de tiempo. Para analizar un caso se calculan los datos que se mueven por la conexión: tamaño del archivo por cantidad de veces que se envía o descarga. Con ese dato se compara con la capacidad disponible y se evalúan alternativas.",
        "Algunas herramientas ayudan a ahorrar: comprimir un archivo reduce su tamaño; una carpeta compartida permite enviar un enlace en vez de muchas copias; un servidor interno de actualizaciones descarga una vez desde internet y reparte por la red local. El tiempo de descarga se calcula convirtiendo los MB a megabits y dividiendo por los Mbps de la conexión.",
        "En cada decisión se respetan las reglas: se usan solo herramientas autorizadas y se cuida la confidencialidad. Los datos de la ficha son de ejemplo.",
    ],
    vocab=[("eficiente", "que logra el objetivo con el menor gasto posible"), ("compresión", "reducir el tamaño de un archivo"), ("servidor de actualizaciones", "servidor interno que descarga una vez y reparte a la red local"), ("capacidad de la conexión", "Mbps disponibles para todos"), ("tiempo de descarga", "tamaño en megabits dividido por la velocidad en Mbps")],
    worked=[
        ("Tiempo de descarga", "Un archivo de 50 MB se descarga a 100 Mbps. ¿Cuántos segundos tarda?", ["50 MB son 50 × 8 = 400 Mb.", "400 ÷ 100 = 4 segundos."], "4 segundos"),
        ("Ahorro con una descarga única", "Una actualización de 100 MB la necesitan 5 equipos. ¿Cuántos MB se ahorran si se descarga una sola vez y se reparte por la red local?", ["Sin servidor: 100 × 5 = 500 MB.", "Con servidor: 100 MB; ahorro 400 MB."], "400 MB"),
    ],
    mistakes=[("Enviar un informe pesado como adjunto a todas las personas.", "Ocupa espacio repetido y puede superar el límite del correo.", "Comprime y comparte un enlace a una carpeta autorizada."),
              ("Descargar 20 veces la misma actualización desde internet.", "Satura la conexión y tarda mucho.", "Usa un servidor interno que descargue una vez y reparta.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es comprimir un archivo?", "Reducir su tamaño", "Cifrarlo con una clave", "Borrarlo", "La compresión reduce el espacio y el tiempo de envío."),
        ("abc", "En Conectividad y Redes: ¿para qué sirve un servidor interno de actualizaciones?", "Para descargar una vez desde internet y repartir por la red local", "Para cifrar los correos", "Para aumentar la velocidad del cable", "Evita que cada equipo descargue lo mismo desde internet."),
        ("abc", "¿Qué significa usar un servicio de forma eficiente?", "Lograr el objetivo con el menor gasto de capacidad y tiempo", "Usar siempre la herramienta más cara", "Enviar cuantas copias se pueda", "La eficiencia relaciona el resultado con el gasto."),
        ("abc", "{F} ¿Cumple el caso (a) el límite del correo si se envía el informe de 30 MB?", "No: 30 MB supera el límite de 25 MB", "Sí: 30 MB es menor que 25 MB", "Depende de la velocidad de internet", "El límite de ejemplo es 25 MB por mensaje."),
        ("abc", "{F} Si se comprime el informe a 20 MB, ¿cumple el límite del correo?", "Sí: 20 MB es menor que 25 MB", "No: sigue siendo de 30 MB", "No: el límite es 10 MB", "Tras comprimir queda por debajo del límite."),
        ("=", "{F} Con el informe comprimido a 20 MB, ¿cuántos MB se envían si se manda como adjunto a las 10 personas?", "20*10", "Se multiplica el tamaño del adjunto por los destinatarios.", " MB"),
        ("=", "{F} Si en vez se sube el informe una vez a la carpeta compartida (20 MB), ¿cuántos MB menos se mueven?", "20*10-20", "Se resta lo que se sube una vez a lo que se enviaría diez veces.", " MB"),
        ("=", "{F} ¿Cuántos MB se descargarían desde internet si cada uno de los 20 computadores baja la actualización de 600 MB?", "600*20", "Se multiplica la actualización por los equipos.", " MB"),
        ("=", "{F} Con el servidor interno de actualizaciones, ¿cuántos MB menos se descargan desde internet?", "600*20-600", "Se resta lo que se descarga una sola vez a lo que se descargaría 20 veces.", " MB"),
        ("=", "{F} ¿Cuántos segundos tarda una descarga de 600 MB a 100 Mbps?", "600*8//100", "Se convierte a megabits y se divide por la velocidad.", " segundos"),
        ("=", "{F} La videollamada usa 2 Mbps por persona y hay 10 personas. ¿Cuántos Mbps usa en total?", "2*10", "Se multiplica lo que usa cada persona por el número de personas.", " Mbps"),
        ("abc", "{F} ¿Qué parte de la conexión de 100 Mbps usa la videollamada de 20 Mbps?", "Una quinta parte", "La mitad", "Toda la conexión", "20 Mbps es la quinta parte de 100 Mbps."),
        ("abc", "{F} Un compañero sugiere subir el informe a un servicio gratuito de internet que él eligió para evitar la intranet. ¿Qué corresponde?", "Usar la carpeta compartida de la intranet, que es la herramienta autorizada", "Subirlo igual porque es más rápido", "Enviar la clave a todos", "Los datos de la institución no se suben a servicios no autorizados."),
    ],
    ctx=("abc", "A las 10:00 se actualizan los 20 equipos al mismo tiempo y la videollamada se corta. ¿Qué propones?", "Programar la actualización fuera de horario y usar el servidor interno de actualizaciones", "Cancelar las videollamadas para siempre", "Descargar más veces para asegurar", "Repartir la carga en el tiempo y descargar una vez reduce la saturación."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calcula el tiempo de descarga?", "Megabits del archivo divididos por los Mbps de la conexión", "Primero se convierten los MB a megabits."),
        ("¿Para qué sirve comprimir un archivo antes de enviarlo?", "Para reducir su tamaño y gastar menos capacidad", "Puede permitir que cumpla el límite del correo."),
        ("¿Qué ventaja tiene el servidor interno de actualizaciones?", "Descarga una vez desde internet y reparte por la red local", "Así se ahorra capacidad de la conexión a internet de toda la oficina."),
    ],
    op=("Una oficina de ejemplo con 15 computadores comparte una conexión de 100 Mbps. Quiere (a) enviar un archivo de 50 MB a 8 personas y (b) actualizar un programa de 200 MB en los 15 equipos. El correo admite 25 MB por mensaje. Propón cómo hacer (a) y (b) de forma eficiente, y calcula los MB movidos desde internet en (b) con y sin servidor interno.",
        "(a) Subir el archivo a una carpeta compartida autorizada y enviar el enlace, porque 50 MB supera 25 MB. (b) Sin servidor: 200 × 15 = 3.000 MB. Con servidor interno: 200 MB. Ahorro: 2.800 MB.",
        ["propone una solución válida para (a)", "calcula con y sin servidor", "usa herramientas autorizadas"],
        ["hoja con las dos soluciones y los cálculos"],
        ["adjuntar los 50 MB", "descargar 15 veces", "usar un servicio no autorizado"],
        "Pregunta: «¿cuántas veces se descarga de internet con el servidor?». Si responde 15, repasa cómo reparte el servidor."),
    reinforce="Calcula los segundos que tarda en descargarse un archivo de 25 MB a 100 Mbps.",
    extend="Explica por qué programar tareas pesadas fuera de horario también es una buena práctica.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (decisión de ejemplo). Hay que compartir un archivo de 40 MB con datos de clientes entre 12 compañeros y 3 clientes externos. Opción A: adjuntarlo en el correo a las 15 personas (límite de 25 MB por mensaje). "
     "Opción B: ponerlo en la carpeta compartida de la intranet (acceso solo interno). Opción C: subirlo a un servicio gratuito de un proveedor desconocido con un enlace público. "
     "Opción D: usar el servicio de almacenamiento autorizado por la institución, con enlace privado y acceso individual por clave. Criterios: respetar el límite técnico, proteger la confidencialidad, llegar a los clientes externos con control de acceso y no sobrecargar la red.")
build(
    O8, 4, F,
    use="Aprenderé a elegir un servicio de intranet o internet con criterios técnicos, de seguridad y de eficiencia, y a justificar la decisión.",
    prior=["Conozco intranet, nube y VPN.", "Sé calcular cuántos MB se mueven.", "Conozco la política de uso aceptable."],
    explain=[
        "Elegir cómo compartir información es una decisión con criterios: límite técnico del medio, confidencialidad, quién necesita acceso (internos y externos), control de acceso y carga sobre la red. Se evalúa cada opción con cada criterio y se descartan las que incumplen alguno indispensable.",
        "Un enlace público de un proveedor desconocido no controla quién accede ni qué se hace con los datos: no cumple la confidencialidad. Una carpeta interna protege, pero no llega a personas externas sin una conexión autorizada. Un servicio autorizado por la institución, con enlace privado y acceso individual, cumple los criterios y deja registro de quién accedió.",
        "La decisión se escribe con los cálculos, el criterio, quién la autorizó y el límite: los datos son de ejemplo y la política de la institución y la ley vigente de protección de datos personales mandan en un caso real.",
    ],
    vocab=[("control de acceso", "decidir quién puede entrar y qué puede hacer"), ("enlace público", "enlace que cualquiera con la dirección puede abrir"), ("enlace privado", "enlace que exige identificarse"), ("servicio autorizado", "servicio aprobado por la institución"), ("trazabilidad", "poder ver quién accedió y cuándo")],
    worked=[
        ("Evaluar por un criterio", "Una opción de ejemplo usa un enlace público de un proveedor desconocido para datos de clientes. ¿Cumple la confidencialidad?", ["Cualquiera con el enlace puede abrirlo.", "Con un enlace público no hay control sobre quién abre el archivo."], "No cumple"),
        ("Datos movidos", "Un archivo de 40 MB se adjunta a 15 personas. ¿Cuántos MB se envían?", ["Se multiplica por los destinatarios.", "40 × 15 = 600."], "600 MB"),
    ],
    mistakes=[("Elegir la opción más rápida de hacer aunque exponga datos de clientes.", "La confidencialidad es un criterio indispensable.", "Descarta lo que incumple y elige entre lo que cumple."),
              ("No dejar registro de quién autorizó el servicio usado.", "Si hay un problema nadie puede revisar la decisión.", "Anota el criterio, la opción y quién autorizó.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el control de acceso?", "Decidir quién puede entrar a un recurso y qué puede hacer", "Cambiar el color de la página", "Borrar el historial", "El control de acceso limita el recurso a las personas autorizadas."),
        ("abc", "En Conectividad y Redes: ¿qué es un enlace público?", "Un enlace que cualquiera con la dirección puede abrir", "Un enlace que exige identificarse", "Un enlace roto", "Un enlace público no controla quién entra."),
        ("abc", "¿Qué es la trazabilidad?", "Poder ver quién accedió a un recurso y cuándo", "Ocultar el nombre del archivo", "Comprimir el archivo", "La trazabilidad deja evidencia para revisar la decisión."),
        ("abc", "{F} ¿Por qué la opción A no cumple el límite técnico?", "Porque 40 MB supera los 25 MB del correo", "Porque es muy lenta", "Porque no tiene clave", "El archivo es más grande que el límite del correo."),
        ("=", "{F} ¿Cuántos MB se enviarían con la opción A si se pudiera adjuntar a las 15 personas?", "40*15", "Se multiplica el archivo por el número de destinatarios.", " MB"),
        ("abc", "{F} ¿Qué falla de la opción B respecto de los clientes externos?", "Su acceso es solo interno y no llega a los clientes sin una conexión autorizada", "Pesa demasiado", "Cuesta demasiado", "La carpeta interna no está pensada para personas externas."),
        ("abc", "{F} ¿Qué criterio incumple la opción C?", "La confidencialidad: el enlace es público y el proveedor es desconocido", "El límite técnico del correo", "El número de personas", "No hay control de acceso ni garantías sobre los datos."),
        ("abc", "{F} ¿Qué opción cumple todos los criterios?", "La opción D", "La opción A", "La opción C", "D respeta el límite, controla el acceso y está autorizada."),
        ("=", "{F} Con la opción D se sube el archivo una sola vez. ¿Cuántos MB menos se mueven que con los 15 adjuntos de la opción A?", "40*15-40", "Se resta lo que se sube una vez a lo que se enviaría quince veces.", " MB"),
        ("=", "{F} ¿Cuántas personas tendrán acceso individual con la opción D (12 compañeros y 3 clientes)?", "12+3", "Se suman las personas internas y las externas.", " personas"),
        ("abc", "{F} Un compañero dice: «usemos C, es lo más rápido». ¿Qué respondes?", "C incumple la confidencialidad de datos de clientes, por lo que no se puede usar", "Tiene razón, la rapidez manda", "C es mejor porque es gratis", "La confidencialidad es un criterio indispensable."),
        ("abc", "{F} ¿Qué debe quedar escrito de la decisión?", "El criterio, la opción elegida, quién autorizó y el límite de los datos", "Solo la opción elegida", "Las claves de los clientes", "Una decisión bien registrada puede ser revisada por otra persona."),
        ("abc", "{F} ¿Qué límite debe declarar quien recomienda D?", "Los datos son de ejemplo y manda la política de la institución y la ley vigente de datos personales", "Ninguno, porque D es perfecta", "Que no hace falta consultar a nadie", "Un caso real exige la política vigente y la norma sobre datos personales."),
    ],
    ctx=("abc", "Un cliente externo de ejemplo pide que le envíes el archivo por una aplicación de mensajería personal porque «es más cómodo». ¿Qué respondes?", "Que se usará el servicio autorizado de la institución con acceso individual, para proteger sus datos", "Que sí, lo envías de inmediato", "Que se lo dejas en un lugar público", "Se usa el canal autorizado, y eso protege también al cliente."),
    sc=[
        ("En Conectividad y Redes: ¿qué opción se descarta primero?", "La que incumple un criterio indispensable", "Los criterios indispensables se verifican antes que la comodidad."),
        ("¿Por qué no usar un enlace público para datos de clientes?", "Porque cualquiera con el enlace podría abrirlo", "Con un enlace público no hay control sobre quién abre el archivo."),
        ("¿Qué se anota de la decisión?", "Criterio, opción, quién autorizó y límite", "Así se puede revisar la decisión."),
    ],
    op=("Una oficina de ejemplo debe compartir un contrato de 30 MB con 6 personas internas y 2 externas. Opciones: (A) correo con adjunto (límite 25 MB); (B) carpeta interna (solo para personas de la red); (C) servicio gratuito de proveedor desconocido con enlace público; (D) servicio autorizado con acceso individual. Evalúa cada opción con los criterios de la ficha 4, calcula los MB movidos si se usa A (aunque no cumpla) y D, y recomienda.",
        "A: supera el límite de 25 MB (30 × 8 = 240 MB si se enviara a 8). B: no llega a las 2 personas externas. C: enlace público, incumple confidencialidad. D: cumple los cuatro criterios; mueve 30 MB. Ahorro frente a A: 240 − 30 = 210 MB. Recomiendo D.",
        ["evalúa las cuatro opciones con criterios", "calcula los MB de A y D", "recomienda D con una razón"],
        ["tabla de cuatro filas y cálculo"],
        ["elegir C por comodidad", "olvidar a las personas externas", "no calcular los MB"],
        "Pregunta: «¿qué criterio incumple cada opción descartada?». Si no puede, pídele que complete una tabla de criterios."),
    reinforce="Escribe una regla para decidir cómo compartir un archivo con datos personales.",
    extend="Explica por qué la comodidad no debe decidir cómo se comparten datos de clientes.",
)

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (cooperativa de ejemplo, inventada). «Cooperativa Lo Verde»: 24 computadores en 3 salas (8 por sala). Mantenimiento preventivo: se hace antes de que haya fallas, según un cronograma. Mantenimiento correctivo: se hace después de una falla. "
     "Roles: técnico, jefa de informática y persona usuaria. Riesgos del trabajo con equipos: electricidad, descarga de electricidad estática que daña piezas, polvo, peso, bordes cortantes y mala postura. Las fichas técnicas del equipo y el cronograma mandan sobre la costumbre. "
     "Cada mantenimiento preventivo dura 45 minutos por equipo.")
build(
    O9, 1, F,
    use="Aprenderé qué es el mantenimiento de hardware, qué tipos hay, quién participa y qué riesgos y normas existen (solo conceptos).",
    prior=["Conozco las partes de un computador.", "Sé multiplicar y dividir.", "Sé que algunas tareas exigen personal autorizado."],
    explain=[
        "Mantener el hardware es cuidar las piezas físicas de los equipos para que funcionen bien. El mantenimiento preventivo se hace antes de que haya fallas, siguiendo un cronograma: limpieza, revisión y actualización. El mantenimiento correctivo se hace después de una falla. Se sigue la especificación técnica del equipo, que indica qué piezas y repuestos son compatibles.",
        "Los equipos tienen riesgos: electricidad, descarga de electricidad estática que puede dañar las piezas, polvo, peso, bordes cortantes y mala postura. Por eso las tareas con equipos abiertos son del personal autorizado y se hacen con las normas vigentes y elementos de protección. Antes de intervenir un equipo se pide autorización y se respalda la información, porque contiene datos de personas.",
        "Al terminar la vida útil de un equipo no se botan sus piezas a la basura común: los residuos electrónicos se entregan a gestores autorizados, y los discos se borran de forma segura para proteger los datos personales." + AVISO,
    ],
    vocab=[("mantenimiento preventivo", "el que se hace antes de que haya fallas"), ("mantenimiento correctivo", "el que se hace después de una falla"), ("cronograma", "calendario de trabajos con fechas y responsables"), ("descarga electrostática", "descarga de electricidad estática que puede dañar piezas"), ("residuo electrónico", "equipo o pieza electrónica desechada"), ("ficha técnica", "documento con las especificaciones del equipo")],
    worked=[
        ("Clasificar el mantenimiento", "Un técnico limpia por calendario los equipos de una sala que funcionan bien. ¿Es preventivo o correctivo?", ["No hay una falla.", "Se hace por calendario: es preventivo."], "Preventivo"),
        ("Tiempo de una sala", "Una sala de ejemplo tiene 6 equipos y cada mantenimiento dura 30 minutos. ¿Cuántos minutos necesita la sala?", ["Se multiplican los equipos por los minutos de cada uno.", "6 × 30 = 180."], "180 minutos"),
    ],
    mistakes=[("Abrir un equipo encendido «solo para mirar».", "Hay riesgo eléctrico y de dañar piezas; es tarea de personal autorizado.", "No lo hagas; pide al instructor o a la jefatura."),
              ("Desechar un disco sin borrar sus datos.", "Podrían recuperarse datos personales.", "Sigue la política de borrado seguro y entrega los residuos a gestores autorizados.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es el mantenimiento preventivo?", "El que se hace antes de que haya fallas, según un cronograma", "El que se hace después de una falla", "El que se hace sin cronograma", "Preventivo significa anticiparse a la falla."),
        ("abc", "En Conectividad y Redes: ¿qué es el mantenimiento correctivo?", "El que se hace después de una falla", "El que se hace según un calendario sin que haya fallas", "El que reemplaza todos los equipos", "Correctivo corrige una falla que ya ocurrió."),
        ("abc", "¿Qué es un cronograma?", "Un calendario de trabajos con fechas y responsables", "Una lista de claves", "Un tipo de repuesto", "El cronograma ordena cuándo y quién hace cada trabajo."),
        ("=", "{F} ¿Cuántos computadores hay en las 3 salas?", "8*3", "Se multiplican las salas por los equipos de cada una.", " computadores"),
        ("abc", "{F} La limpieza programada de las salas, cuando los equipos funcionan bien, ¿qué mantenimiento es?", "Preventivo", "Correctivo", "Ninguno", "No hay falla y se hace por calendario: es preventivo."),
        ("abc", "{F} Se reemplaza la pieza de un equipo después de que falló. ¿Qué mantenimiento es?", "Correctivo", "Preventivo", "Ninguno", "Se actúa después de la falla."),
        ("=", "{F} ¿Cuántos días tarda el mantenimiento si se hacen 4 equipos por día en los 24 equipos?", "24//4", "Se divide el total de equipos por los equipos de cada día.", " días"),
        ("abc", "{F} Antes de intervenir un equipo que guarda archivos de personas, ¿qué corresponde?", "Pedir autorización y hacer un respaldo", "Abrirlo de inmediato", "Borrar los archivos", "Los archivos de personas se protegen antes de cualquier intervención."),
        ("abc", "{F} Un técnico quiere abrir un equipo con la fuente conectada «rápido, solo para mirar». ¿Qué corresponde?", "No hacerlo: es riesgoso y es tarea de personal autorizado, con la norma vigente", "Hacerlo si usa guantes", "Hacerlo si nadie lo ve", "Un equipo conectado tiene electricidad y solo lo abre personal autorizado."),
        ("abc", "Una cooperativa de ejemplo quiere botar los equipos viejos a la basura común. ¿Qué corresponde?", "Entregarlos a un gestor autorizado de residuos electrónicos, borrando antes los datos de los discos", "Botarlos a la basura común", "Regalarlos con los datos dentro", "Los residuos electrónicos y los datos personales requieren manejo especial."),
        ("=", "{F} Una sala tiene 8 equipos y cada mantenimiento preventivo dura 45 minutos. ¿Cuántos minutos necesita la sala?", "8*45", "Se multiplican los equipos por los minutos de cada uno.", " minutos"),
        ("=", "{F} En una sala de 8 equipos se hacen 2 pausas de 10 minutos durante el trabajo. ¿Cuántos minutos dura en total el trabajo de la sala, contando mantenimiento y pausas?", "8*45+2*10", "Se suman los minutos de mantenimiento y los de pausa.", " minutos"),
        ("abc", "{F} Un técnico pasa horas agachado frente a los equipos sin cambiar de postura. ¿Qué se descuida?", "La ergonomía: buena postura y pausas", "El cifrado de la red", "La licencia del sistema", "La mala postura continua daña el cuerpo y se previene con pausas."),
    ],
    ctx=("abc", "Una usuaria te pide que arregles su computador, que falla, y que lo hagas «ya, sin guardar nada». El equipo tiene archivos de clientes. ¿Qué respondes?", "Que primero se necesita autorización de la jefa y un respaldo, porque hay datos de clientes", "Que lo harás sin avisar", "Que lo formatearás ahora", "Antes de intervenir se protegen los datos y se obtiene autorización."),
    sc=[
        ("En Conectividad y Redes: ¿qué diferencia hay entre preventivo y correctivo?", "El preventivo se hace antes de una falla y el correctivo después", "El tipo depende del momento en que se interviene."),
        ("¿Qué se hace con los residuos electrónicos?", "Se entregan a gestores autorizados", "No se botan a la basura común."),
        ("¿Quién abre equipos conectados?", "Solo personal autorizado, con norma vigente", "Hay riesgo eléctrico y de dañar piezas."),
    ],
    op=("Un liceo de ejemplo tiene 30 computadores en 5 salas de 6 equipos. Cada mantenimiento preventivo dura 40 minutos. Calcula cuántos minutos necesita una sala, cuántos días tardan si se hacen 6 equipos por día, y escribe tres reglas de seguridad y privacidad para el técnico.",
        "Una sala: 6 × 40 = 240 minutos. Días: 30 ÷ 6 = 5 días. Reglas: no abrir equipos conectados; pedir autorización y respaldar antes de intervenir; entregar residuos electrónicos a un gestor autorizado y borrar los discos con la política de la institución.",
        ["calcula minutos y días", "escribe tres reglas coherentes", "incluye privacidad y seguridad"],
        ["hoja con los cálculos y las tres reglas"],
        ["dividir mal", "proponer abrir equipos conectados", "no mencionar el respaldo"],
        "Pregunta: «¿por qué se respalda antes?». Si no puede responder, recuérdale que los equipos guardan datos de personas."),
    reinforce="Haz una lista de cinco cosas que aparecerían en un cronograma de mantenimiento preventivo (por ejemplo, revisar la hoja de vida), sin describir cómo abrir ni desarmar equipos.",
    extend="Explica por qué el mantenimiento preventivo suele costar menos que esperar a que todo falle.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo del equipo PC-07). Procesador: tipo S1 (de ejemplo); placa madre: admite memoria tipo M1, tiene 2 ranuras y un máximo de 16 GB en total; memoria instalada: 2 módulos tipo M1 de 2 GB cada uno; "
     "almacenamiento: disco de 500 GB; fuente de poder: 300 W; años de uso: 4 (de ejemplo). Documentos: ficha técnica (especificaciones), hoja de vida del equipo (historial de intervenciones), orden de trabajo (qué hacer, quién y cuándo) y cronograma.")
build(
    O9, 2, F,
    use="Aprenderé las partes principales de un computador, la compatibilidad de piezas y los documentos del mantenimiento (solo conceptos).",
    prior=["Sé qué es mantenimiento preventivo y correctivo.", "Sé qué es la RAM y el disco.", "Sé sumar y comparar."],
    explain=[
        "Un computador tiene piezas con funciones distintas. El procesador ejecuta las instrucciones. La memoria RAM guarda lo que se está usando ahora. El almacenamiento (disco) guarda los archivos aunque el equipo se apague. La placa madre conecta todas las piezas y define con qué piezas es compatible. La fuente de poder entrega la energía y se mide en watts (W). Además hay ventilación y una tarjeta de red.",
        "Cualquier actualización debe ser compatible con la placa: el tipo de memoria que admite, el número de ranuras y la capacidad máxima. Esos datos están en la ficha técnica, que es el documento de referencia. La hoja de vida registra cada intervención, y la orden de trabajo indica qué hacer, quién lo hace y cuándo. El cronograma ordena las órdenes en el tiempo.",
        "Los registros permiten saber la edad, el historial y las piezas de cada equipo, y decidir si conviene actualizar o reemplazar. Aquí aprendes a leer los documentos; abrir equipos y cambiar piezas es tarea de personal autorizado." + AVISO,
    ],
    vocab=[("procesador", "pieza que ejecuta las instrucciones"), ("memoria RAM", "memoria que guarda lo que se está usando"), ("almacenamiento", "disco donde se guardan los archivos"), ("placa madre", "pieza que conecta todas las demás"), ("fuente de poder", "pieza que entrega energía, medida en watts"), ("hoja de vida", "registro del historial de intervenciones de un equipo"), ("orden de trabajo", "documento que dice qué hacer, quién y cuándo")],
    worked=[
        ("Margen de memoria", "Una placa de ejemplo admite hasta 16 GB y tiene instalados 4 GB. ¿Cuántos GB más admite en total?", ["Se resta lo instalado al máximo.", "16 − 4 = 12."], "12 GB"),
        ("Compatibilidad", "La placa de ejemplo usa memoria tipo M1. Se ofrece un módulo tipo M2. ¿Es compatible?", ["La placa solo admite el tipo M1.", "M2 es de otro tipo."], "No es compatible"),
    ],
    mistakes=[("Comprar memoria sin revisar la ficha técnica porque «todas son iguales».", "Si el tipo no es el que admite la placa, no sirve.", "Lee primero el tipo, las ranuras y el máximo en la ficha."),
              ("No anotar en la hoja de vida una pieza reemplazada.", "Después nadie sabrá qué se cambió ni cuándo.", "Registra cada intervención con fecha y responsable.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿para qué sirve la memoria RAM?", "Para guardar lo que se está usando en este momento", "Para guardar archivos para siempre", "Para entregar energía al equipo", "La RAM es memoria de trabajo y se vacía al apagar."),
        ("abc", "En Conectividad y Redes: ¿qué hace la placa madre?", "Conecta todas las piezas y define con cuáles es compatible", "Entrega la energía", "Ejecuta las instrucciones", "La placa madre es el soporte y el enlace de las demás piezas."),
        ("abc", "¿Qué es la hoja de vida de un equipo?", "El registro del historial de intervenciones del equipo", "La lista de claves del equipo", "El manual de usuario", "La hoja de vida permite saber qué se hizo y cuándo."),
        ("abc", "{F} ¿Qué tipo de memoria admite la placa de PC-07?", "Tipo M1", "Tipo M2", "Cualquier tipo", "La ficha dice que la placa admite memoria tipo M1."),
        ("=", "{F} ¿Cuántos GB de memoria tiene instalada PC-07?", "2*2", "Son dos módulos de 2 GB.", " GB"),
        ("abc", "{F} ¿Qué documento da las especificaciones del equipo?", "La ficha técnica", "La orden de trabajo", "La hoja de vida", "La ficha técnica contiene tipo de memoria, ranuras y máximo."),
        ("=", "{F} ¿Cuántos GB de memoria más admite la placa, sobre lo instalado?", "16-4", "Al máximo de 16 GB se le restan los 4 GB instalados.", " GB"),
        ("abc", "{F} Se ofrece un módulo tipo M2 de 8 GB para PC-07. ¿Sirve?", "No: la placa admite tipo M1", "Sí: tiene mayor capacidad", "Sí: solo importa la capacidad", "El tipo de memoria debe coincidir con el que admite la placa."),
        ("abc", "{F} ¿Qué falta resolver para instalar más memoria si las 2 ranuras ya están ocupadas?", "Reemplazar los módulos instalados por otros de mayor capacidad del mismo tipo", "Instalar un módulo en una ranura inexistente", "Subir la potencia de la fuente", "Con las ranuras ocupadas, solo se puede cambiar lo instalado."),
        ("abc", "{F} Un técnico compra memoria sin revisar la ficha técnica porque «todas son iguales». ¿Qué respondes?", "No son iguales: el tipo debe coincidir con el que admite la placa", "Tiene razón, todas sirven", "Solo importa el color", "La compatibilidad se verifica en la ficha técnica."),
        ("abc", "{F} Se reemplazó un módulo de memoria y no se anotó nada. ¿Qué problema produce?", "Nadie sabrá qué se cambió ni cuándo", "El equipo queda más rápido", "La fuente se apaga", "La hoja de vida debe registrar cada intervención."),
        ("=", "{F} Si se reemplazaran los 2 módulos por dos de 8 GB del tipo M1, ¿cuántos GB tendría PC-07?", "2*8", "Se multiplican los módulos nuevos por su capacidad.", " GB"),
        ("abc", "{F} Con los dos módulos de 8 GB, ¿cumple el máximo de la placa?", "Sí: 16 GB igualan el máximo admitido", "No: supera el máximo", "No se puede saber", "El máximo es 16 GB y 2 × 8 son 16."),
    ],
    ctx=("abc", "Un jefe de ejemplo pide comprar 10 módulos de memoria «los más baratos que haya» para los equipos de la ficha. ¿Qué respondes?", "Que primero se revisa la ficha técnica para comprar el tipo compatible y la capacidad adecuada", "Que se compra cualquier cosa", "Que no se compra nada nunca", "El criterio es la compatibilidad, no solo el precio."),
    sc=[
        ("En Conectividad y Redes: ¿dónde se revisa la compatibilidad de una pieza?", "En la ficha técnica del equipo", "Allí están el tipo, las ranuras y el máximo."),
        ("¿Qué registra la hoja de vida?", "Las intervenciones hechas al equipo", "Es la memoria del historial del equipo."),
        ("¿Qué es una orden de trabajo?", "Un documento que dice qué hacer, quién y cuándo", "Sirve para ordenar y registrar el trabajo."),
    ],
    op=("Ficha técnica de ejemplo del equipo PC-12: placa que admite memoria tipo M1, 4 ranuras, máximo 32 GB; instalados 2 módulos de 4 GB tipo M1; disco de 250 GB; fuente de 350 W. Un jefe pide subir la memoria a 16 GB. Calcula cuántos GB faltan, cuántos módulos de 4 GB tipo M1 hay que agregar si hay ranuras libres, y qué documento usarías y qué registrarías después.",
        "Instalados: 8 GB. Faltan: 16 − 8 = 8 GB, es decir, 2 módulos de 4 GB (4 ranuras menos 2 ocupadas dejan 2 libres, justo las que hacen falta). Documento: ficha técnica para verificar el tipo y el máximo. Registraría la intervención en la hoja de vida (fecha, pieza y responsable). El trabajo lo hace personal autorizado.",
        ["calcula la memoria que falta", "verifica compatibilidad con la ficha", "registra la intervención"],
        ["hoja con el cálculo, el documento y el registro"],
        ["olvidar las ranuras libres", "comprar el tipo incorrecto", "no registrar"],
        "Pregunta: «¿cuántas ranuras libres hay?». Si no sabe, pídele que reste 2 de 4."),
    reinforce="Anota cinco piezas de un computador y la función de cada una.",
    extend="Explica por qué la hoja de vida ayuda a decidir si conviene reemplazar un equipo.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (cronograma de ejemplo). La cooperativa tiene 24 computadores en 3 salas de 8. Se intervienen 4 equipos por jornada, de lunes a viernes, sin trabajar fines de semana. Cada equipo requiere 45 minutos de mantenimiento preventivo "
     "más 15 minutos de registro. Se hace una pausa de 10 minutos entre el segundo y el tercer equipo de cada jornada. El trabajo parte el miércoles.")
build(
    O9, 3, F,
    use="Aprenderé a analizar un cronograma de mantenimiento: cuántas jornadas se necesitan, cuánto dura cada una y cuándo termina (solo cálculos en papel).",
    prior=["Sé qué es un cronograma.", "Sé dividir y multiplicar.", "Sé contar días hábiles."],
    explain=[
        "Un cronograma de mantenimiento reparte el trabajo en el tiempo. Se calcula cuántos equipos se hacen por jornada, cuántas jornadas se necesitan para todos y cuánto dura cada jornada. El tiempo de una jornada suma el mantenimiento y el registro de cada equipo más las pausas. Después se cuentan solo los días hábiles, porque no se trabaja fines de semana.",
        "Un buen cronograma deja holgura para imprevistos, como una falla que obliga a un mantenimiento correctivo, y respeta las pausas, que forman parte de la ergonomía. También coordina con las personas usuarias, para no dejarlas sin equipo cuando lo necesitan. Todo se registra en la orden de trabajo y en la hoja de vida de cada equipo.",
        "Los cálculos de esta clase son de ejemplo. Las tareas con equipos las realiza personal autorizado y este cuaderno no te habilita para trabajar." + AVISO,
    ],
    vocab=[("jornada", "día de trabajo"), ("día hábil", "día en que se trabaja, de lunes a viernes"), ("holgura", "tiempo extra para imprevistos"), ("hito", "fecha importante del cronograma"), ("registro", "anotación de lo hecho")],
    worked=[
        ("Jornadas necesarias", "Hay 18 equipos y se hacen 6 por jornada. ¿Cuántas jornadas se necesitan?", ["Se divide el total de equipos por los de cada jornada.", "18 ÷ 6 = 3."], "3 jornadas"),
        ("Minutos de una jornada", "Se hacen 2 equipos por jornada, con 30 minutos de trabajo y 10 de registro cada uno. ¿Cuántos minutos dura la jornada?", ["Cada equipo: 30 + 10 = 40.", "Dos equipos: 2 × 40 = 80."], "80 minutos"),
    ],
    mistakes=[("Contar los sábados y domingos como días de trabajo.", "El cronograma dice que solo se trabaja de lunes a viernes.", "Cuenta solo días hábiles."),
              ("Dejar el cronograma sin holgura.", "Una falla inesperada atrasa todo.", "Agrega un margen para imprevistos.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es una holgura en un cronograma?", "Tiempo extra para imprevistos", "Un trabajo extra", "Un día de descanso del cliente", "La holgura evita que un imprevisto atrase todo."),
        ("abc", "En Conectividad y Redes: ¿qué es un día hábil?", "Un día en que se trabaja, de lunes a viernes en este caso", "Cualquier día del año", "Solo el sábado", "El cronograma de la ficha excluye los fines de semana."),
        ("abc", "¿Qué es un hito del cronograma?", "Una fecha importante del trabajo", "Una pieza del computador", "Una clave de acceso", "Un hito marca un punto clave del plan."),
        ("=", "{F} ¿Cuántas jornadas se necesitan para los 24 equipos?", "24//4", "Se divide el total de equipos por los de cada jornada.", " jornadas"),
        ("=", "{F} ¿Cuántos minutos de trabajo y registro hay por equipo?", "45+15", "Se suman los minutos de mantenimiento y de registro.", " minutos"),
        ("=", "{F} ¿Cuántos minutos dura una jornada, con 4 equipos y la pausa de 10 minutos?", "4*(45+15)+10", "Se suman los equipos con su registro y la pausa.", " minutos"),
        ("abc", "{F} Si el trabajo parte el miércoles, ¿cuándo termina la sexta jornada?", "El miércoles de la semana siguiente", "El lunes de la semana siguiente", "El viernes de la misma semana", "Miércoles, jueves, viernes, lunes, martes y miércoles son las seis jornadas."),
        ("=", "{F} ¿Cuántos minutos de trabajo suman las 6 jornadas completas?", "6*(4*(45+15)+10)", "Se multiplican las jornadas por los minutos de cada una.", " minutos"),
        ("=", "{F} Si se pasa a 6 equipos por jornada, ¿cuántas jornadas se necesitan?", "24//6", "Se divide el total de equipos por los nuevos equipos por jornada.", " jornadas"),
        ("abc", "{F} Un lunes hay feriado y no se trabaja. ¿Qué efecto tiene en el cronograma?", "Se desplaza el trabajo un día hábil más tarde", "Se adelanta el término", "No cambia nada", "Perder un día hábil atrasa el término un día hábil."),
        ("abc", "{F} Un técnico propone eliminar la pausa para ganar tiempo. ¿Qué respondes?", "La pausa forma parte de la ergonomía y debe mantenerse", "Tiene razón, las pausas no sirven", "Mejor eliminar el registro", "Las pausas cuidan el cuerpo y la atención."),
        ("abc", "{F} Un equipo falla un martes y necesita un mantenimiento correctivo imprevisto. ¿Qué ayuda a absorberlo?", "Una holgura prevista en el cronograma", "Eliminar las pausas", "Cancelar el registro", "La holgura permite resolver imprevistos sin atrasar todo."),
        ("=", "{F} Una sala tiene 8 equipos y se hacen 4 por jornada. ¿Cuántas jornadas necesita?", "8//4", "Se divide el total de equipos de la sala por los de cada jornada.", " jornadas"),
    ],
    ctx=("abc", "La jefa dice: «terminen antes, sáltense el registro». ¿Qué respondes?", "Que el registro es parte del trabajo y permite revisarlo, y que si hay urgencia se ajusta el cronograma", "Que lo harás sin registrar nada", "Que los equipos se registran después de un mes", "El registro deja evidencia; si falta tiempo, se ajusta el plan, no el registro."),
    sc=[
        ("En Conectividad y Redes: ¿cómo se calculan las jornadas?", "Total de equipos dividido por los equipos de cada jornada", "Ese cálculo es la base para armar el cronograma de trabajo completo."),
        ("¿Por qué agregar holgura?", "Para absorber imprevistos", "Un cronograma sin margen se atrasa con cualquier falla."),
        ("¿Qué días se cuentan?", "Solo los días hábiles", "No se trabaja fines de semana en este cronograma."),
    ],
    op=("Una bodega de ejemplo tiene 18 computadores. Se hacen 3 equipos por jornada, de lunes a viernes; cada equipo requiere 50 minutos de mantenimiento y 10 de registro. El trabajo parte el jueves. Calcula las jornadas, los minutos de cada una (sin pausas) y el día en que termina, y propón una holgura.",
        "Jornadas: 18 ÷ 3 = 6. Minutos por jornada: 3 × (50 + 10) = 180. Jueves, viernes, lunes, martes, miércoles y jueves: termina el jueves de la semana siguiente. Holgura propuesta: un día hábil extra para imprevistos.",
        ["calcula jornadas y minutos", "cuenta solo los días hábiles", "propone una holgura"],
        ["hoja con los cálculos, el calendario y la holgura"],
        ["contar el fin de semana", "olvidar el registro", "no dejar holgura"],
        "Pregunta: «¿en qué día termina la sexta jornada?». Si no lo sabe, pídele que escriba los días uno por uno."),
    reinforce="Arma un cronograma de ejemplo para 10 equipos, con 2 por jornada, y calcula cuántas jornadas necesitas.",
    extend="Explica por qué un cronograma realista incluye pausas y holgura.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (decisión de actualización de ejemplo). La cooperativa necesita al menos 8 GB de memoria RAM en cada uno de sus 24 equipos. Cada equipo tiene 4 GB (2 módulos tipo M1 de 2 GB), 2 ranuras ocupadas, máximo 16 GB y admite solo memoria tipo M1. "
     "Opción A: reemplazar los 2 módulos por 2 módulos tipo M1 de 8 GB, $30.000 cada módulo. Opción B: agregar un módulo tipo M2 de 8 GB, $28.000. Opción C: reemplazar todo el equipo, $350.000 cada uno. Presupuesto: $1.500.000. Todos los precios son de ejemplo.")
build(
    O9, 4, F,
    use="Aprenderé a decidir una actualización de hardware con criterios de compatibilidad, requerimientos y costo, y a justificarla (solo cálculos en papel).",
    prior=["Sé leer una ficha técnica.", "Sé calcular costos totales.", "Sé qué es la compatibilidad."],
    explain=[
        "Decidir una actualización de hardware exige tres pasos. Primero se verifica la compatibilidad con la ficha técnica: tipo de pieza, ranuras libres y máximo admitido. Segundo, se comprueba que la opción cumple el requerimiento (por ejemplo, la memoria mínima que necesita el trabajo). Tercero, se calcula el costo total y se compara con el presupuesto.",
        "Una opción incompatible se descarta aunque sea barata, porque no se podrá instalar. Entre las que cumplen, se elige por costo y por vida útil. Reemplazar todo el equipo puede ser mejor cuando el equipo es muy antiguo, pero cuesta más. Si se retira una pieza o un equipo, se entrega como residuo electrónico a un gestor autorizado y se protege la información.",
        "La recomendación se escribe con los cálculos y los límites: precios y requisitos son de ejemplo y las intervenciones las realiza personal autorizado. Este cuaderno no te habilita para trabajar." + AVISO,
    ],
    vocab=[("requerimiento", "necesidad que la solución debe cumplir"), ("compatibilidad", "que una pieza funcione con las demás"), ("vida útil", "tiempo durante el cual un equipo sirve bien"), ("costo total", "costo de una opción multiplicado por la cantidad"), ("gestor autorizado", "empresa autorizada para recibir residuos")],
    worked=[
        ("Costo total", "Una opción de ejemplo cuesta $40.000 por equipo y hay 10 equipos. ¿Cuál es el costo total?", ["Se multiplica el costo por la cantidad.", "40.000 × 10 = 400.000."], "$400.000"),
        ("Descartar por incompatible", "Un módulo de ejemplo es de un tipo que la placa no admite. ¿Se acepta?", ["La compatibilidad es un criterio indispensable y esta pieza no lo cumple.", "No se podrá instalar."], "No se acepta"),
    ],
    mistakes=[("Elegir la opción más barata aunque sea incompatible.", "No funcionará y el gasto se pierde.", "Verifica primero la compatibilidad con la ficha técnica."),
              ("Botar la pieza reemplazada a la basura común.", "Es un residuo electrónico y puede contener datos.", "Entrégala a un gestor autorizado y borra los datos antes.")],
    T=[
        ("abc", "En Conectividad y Redes: ¿qué es la compatibilidad de una pieza?", "Que la pieza funcione con las demás piezas del equipo", "Que la pieza sea barata", "Que la pieza sea nueva", "Una pieza compatible cumple el tipo y las especificaciones de la placa."),
        ("abc", "En Conectividad y Redes: ¿qué es el costo total de una opción?", "El costo por equipo multiplicado por la cantidad de equipos", "El costo de un solo módulo", "El precio más bajo", "Para compararlo con el presupuesto se multiplica por la cantidad."),
        ("abc", "¿Qué es un requerimiento?", "Una necesidad que la solución debe cumplir", "Un permiso del vecino", "Un tipo de cable", "El requerimiento orienta qué opción sirve."),
        ("abc", "{F} ¿Por qué se descarta la opción B?", "Porque el módulo es tipo M2 y los equipos solo admiten tipo M1", "Porque es muy cara", "Porque la RAM no sirve", "La compatibilidad es un criterio indispensable y esta pieza no lo cumple."),
        ("=", "{F} Con la opción A, ¿cuántos GB de memoria quedan en cada equipo?", "2*8", "Se multiplican los 2 módulos por 8 GB.", " GB"),
        ("abc", "{F} ¿Cumple la opción A el requerimiento de 8 GB y el máximo de 16 GB?", "Sí: tiene 16 GB, que es mayor que 8 y no excede el máximo", "No: 16 GB supera el máximo", "No: 16 GB es menos de 8", "16 GB cumple el mínimo de 8 GB y es igual al máximo admitido."),
        ("=", "{F} ¿Cuántos pesos cuesta la opción A en cada equipo (2 módulos)?", "2*30000", "Se multiplican los 2 módulos por su precio.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la opción A en los 24 equipos?", "24*2*30000", "Se multiplica el costo de cada equipo por 24 equipos.", " pesos"),
        ("abc", "{F} ¿Cabe la opción A en el presupuesto de $1.500.000?", "Sí: cuesta $1.440.000", "No: cuesta $2.000.000", "No: cuesta $1.600.000", "Los 24 equipos cuestan 24 × 60.000 = 1.440.000, menos de 1.500.000."),
        ("=", "{F} ¿Cuántos pesos sobran del presupuesto con la opción A?", "1500000-24*2*30000", "Al presupuesto se le resta el costo total de la opción A.", " pesos"),
        ("=", "{F} ¿Cuántos pesos costaría la opción C en los 24 equipos?", "24*350000", "Se multiplica el precio por equipo por 24.", " pesos"),
        ("abc", "{F} Un jefe propone la opción C «porque es nueva». ¿Qué respondes con los datos?", "C cuesta $8.400.000 y supera el presupuesto; A cumple el requerimiento y cabe", "Tiene razón, C es siempre mejor", "C es más barata", "C supera por mucho el presupuesto y el requerimiento se cumple con A."),
        ("abc", "{F} ¿Qué límite debe declarar la recomendación?", "Los precios son de ejemplo, falta verificar en la realidad cada equipo y las intervenciones las hace personal autorizado", "Ninguno, los números son exactos", "Que no se necesita ficha técnica", "La ficha es de ejemplo y no reemplaza la verificación real."),
    ],
    ctx=("abc", "Al reemplazar los módulos, sobran 48 módulos de 2 GB. Un técnico quiere llevárselos a su casa. ¿Qué corresponde?", "Entregarlos según la política de la cooperativa, como residuo electrónico a un gestor autorizado, o reutilizarlos si la jefa lo autoriza", "Llevárselos sin avisar", "Botarlos a la basura común", "Las piezas retiradas tienen valor y deben gestionarse con autorización."),
    sc=[
        ("En Conectividad y Redes: ¿qué se verifica primero al elegir una pieza?", "La compatibilidad con la ficha técnica", "Una pieza incompatible no se puede instalar."),
        ("¿Cómo se compara una opción con el presupuesto?", "Multiplicando el costo por la cantidad y comparando", "El costo total se compara con lo disponible."),
        ("¿Qué se hace con una pieza retirada?", "Se entrega a un gestor autorizado o se reutiliza con autorización", "Una pieza retirada es un residuo electrónico y requiere manejo autorizado."),
    ],
    op=("Una radio de ejemplo necesita 8 GB de RAM en 10 equipos que hoy tienen 4 GB (2 módulos tipo M1 de 2 GB, ranuras ocupadas, máximo 16 GB). Opción 1: 2 módulos tipo M1 de 4 GB por equipo, $20.000 cada módulo. Opción 2: 1 módulo tipo M3 de 4 GB por equipo, $15.000 (la placa no lo admite). Opción 3: equipo nuevo, $300.000. Presupuesto: $500.000. Evalúa cada opción y recomienda con un límite.",
        "Opción 1: 2 × 4 = 8 GB, cumple y es compatible; costo 10 × 2 × 20.000 = 400.000, cabe. Opción 2: incompatible, se descarta. Opción 3: 10 × 300.000 = 3.000.000, supera el presupuesto. Recomiendo la opción 1. Límite: precios de ejemplo y la intervención la realiza personal autorizado.",
        ["verifica compatibilidad", "calcula costos y los compara con el presupuesto", "recomienda y declara un límite"],
        ["tabla de tres opciones con criterios y costos"],
        ["elegir la 2 por barata", "olvidar multiplicar por 10", "no declarar el límite"],
        "Pregunta: «¿qué opción se descarta primero y por qué?». Si no responde, pídele que lea la compatibilidad."),
    reinforce="Compara tres piezas inventadas de un computador según compatibilidad y precio.",
    extend="Explica por qué retirar una pieza con datos exige un cuidado especial.",
)

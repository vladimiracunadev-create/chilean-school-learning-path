"""Explotación Minera TP 3.º y 4.º medio: OAE-04 (perforación y tronadura: solo conceptos, documentos y cálculos de planilla; sin procedimientos ni manejo de explosivos), OAE-05 (marco legal minero) y OAE-06 (muestreo: conceptos, rotulado y cálculos de planilla). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_exmi_common import AVISO, EMER, build

O4 = "TP-EXMI-3y4-OAE-04"
O5 = "TP-EXMI-3y4-OAE-05"
O6 = "TP-EXMI-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 15 (caso de ejemplo, inventado). La faena ficticia «Mina Demo Cerro Pelado» explota cobre a cielo abierto por bancos (escalones del rajo). En su matriz de peligros de la perforación y la tronadura se anotan: polvo (probabilidad 5 y gravedad 3), vibración y caída de rocas (probabilidad 3 y gravedad 4), proyección de fragmentos de roca (probabilidad 2 y gravedad 5) y ruido (probabilidad 4 y gravedad 2). "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. Personal de ejemplo en el sector: 6 personas en perforación, 4 en seguridad y control de accesos y 3 en topografía. Toda tronadura tiene una zona de exclusión y una señal de aviso, y la dirige un responsable autorizado.")
build(
    O4, 1, F,
    use="Aprenderé qué son la perforación y la tronadura, por qué son de las tareas más riesgosas de una faena y por qué solo personal formado y autorizado por la empresa y la autoridad minera puede realizarlas.",
    prior=["Sé qué es un peligro y qué es un riesgo.", "Sé qué es una zona de exclusión.", "Sé calcular un puntaje multiplicando dos números."],
    explain=[
        "La perforación es hacer hoyos en la roca, llamados pozos, y la tronadura es el uso controlado de explosivos para fragmentar la roca. Ambas se hacen según diagramas e instrucciones técnicas y forman parte del proceso que prepara la roca para sacar el mineral. Son tareas de alto riesgo: hay polvo, ruido, vibración, riesgo de caída de rocas y de proyección de fragmentos, y los explosivos están controlados por la autoridad minera y la norma vigente.",
        "Por eso solo realiza estas tareas personal formado y autorizado, bajo la dirección de un responsable también autorizado. Toda tronadura tiene una zona de exclusión, que es un área de acceso prohibido, y una señal de aviso; nadie entra mientras la zona esté activa. Un peligro de gravedad máxima, como la proyección de fragmentos, se controla manteniendo a las personas fuera del área aunque su puntaje no sea el mayor. En la matriz de ejemplo, el puntaje de riesgo es probabilidad por gravedad y se atiende primero el mayor.",
        f"Este cuaderno no enseña a perforar, cargar ni tronar: solo vocabulario, lectura de documentos y reglas generales. Si ves algo parecido a un explosivo, no lo toques. {EMER} {AVISO}",
    ],
    vocab=[("perforación", "hacer hoyos, llamados pozos, en la roca"), ("tronadura", "uso controlado de explosivos para fragmentar la roca"), ("pozo", "hoyo hecho en la roca por la perforación"), ("banco", "escalón de una mina a cielo abierto"), ("zona de exclusión", "área donde nadie entra durante una tronadura"), ("señal de aviso", "alarma o aviso que anuncia una tronadura"), ("responsable autorizado", "persona formada y autorizada que dirige la tarea")],
    worked=[
        ("Puntaje de riesgo", "En la matriz de ejemplo de un taller de herramientas, el ruido de un martillo tiene probabilidad 3 y gravedad 2. ¿Qué puntaje de riesgo resulta?", ["Se multiplica la probabilidad por la gravedad.", "3 por 2 son 6."], "6 puntos"),
        ("Peligro y riesgo", "En el borde de un banco de ejemplo no hay barrera. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el borde sin barrera, porque puede causar una caída.", "El riesgo es que una persona o un vehículo caiga al nivel de abajo."], "Peligro: el borde sin barrera; riesgo: que alguien o algo caiga"),
    ],
    mistakes=[("Creer que quien entiende cómo se organiza una tronadura ya puede participar en ella.", "Solo personal formado y autorizado por la empresa y la autoridad minera participa.", "Usa este cuaderno para entender y deja la tarea a personal autorizado."),
              ("Creer que un explosivo abandonado se puede recoger si se tiene cuidado.", "Un objeto que parece explosivo no se toca ni se mueve.", "No te acerques, avisa a un adulto responsable y a emergencias.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es la perforación de rocas?", "Hacer hoyos, llamados pozos, en la roca", "Mover las rocas con una pala", "Mezclar la roca con agua", "La perforación abre pozos; mover rocas con pala es otra tarea."),
        ("abc", "En Explotación Minera: ¿qué es la tronadura?", "El uso controlado de explosivos para fragmentar la roca", "El transporte del mineral en camiones", "El análisis del mineral en un laboratorio", "La tronadura fragmenta la roca; el transporte es otra etapa."),
        ("abc", "En Explotación Minera: ¿por qué hay una zona de exclusión durante una tronadura?", "Para que nadie esté en el área de riesgo mientras la tronadura está activa", "Para marcar dónde se guarda el mineral", "Para señalar el lugar donde se estaciona", "La zona de exclusión mantiene a las personas fuera del riesgo."),
        ("=", "{F} ¿Cuántas personas hay en total en el sector de la ficha?", "6+4+3", "Se suman las personas de perforación, seguridad y topografía.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «proyección de fragmentos de roca»?", "Que un fragmento golpee a una persona o a un equipo", "Que la roca quede muy fina", "Que la perforación se atrase", "El riesgo es el daño posible, no una consecuencia de la producción."),
        ("abc", "{F} ¿Quién dirige la tronadura según la ficha?", "Un responsable autorizado", "Cualquier persona del sector", "El personal de topografía", "La ficha dice que la dirige un responsable autorizado."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el polvo?", "5*3", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la proyección de fragmentos de roca?", "2*5", "Se multiplican la probabilidad y la gravedad de ese peligro.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál de los cuatro peligros debe atenderse primero?", "El polvo, porque tiene el mayor puntaje (15)", "La proyección de fragmentos, porque es la más grave (5)", "El ruido, porque se escucha todo el día", "Se atiende primero el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Un joven en práctica dice: «entiendo cómo se hace una tronadura, así que puedo ayudar a organizarla». ¿Qué es correcto?", "Entenderlo no lo habilita: solo personal formado y autorizado participa", "Puede ayudar si lleva casco y lentes", "Puede ayudar si lo supervisa un compañero", "Los elementos de protección no reemplazan la formación ni la autorización."),
        ("abc", "{F} ¿Por qué, aunque la proyección de fragmentos tenga un puntaje menor que el polvo, se controla con una zona de exclusión?", "Porque su gravedad es máxima y la forma de evitar el daño es mantener a las personas fuera del área", "Porque, al tener menor puntaje, no necesita ningún control", "Porque la zona de exclusión solo sirve para reducir el polvo", "Un daño muy grave se controla manteniendo a las personas lejos, aunque su puntaje no sea el mayor."),
        ("=", "{F} Para un simulacro de evacuación, el personal de perforación y el de seguridad se reparten en vehículos de 5 personas cada uno. ¿Cuántos vehículos se necesitan?", "(6+4)//5", "Se suman las personas de las dos áreas y se divide entre las personas de cada vehículo.", " vehículos"),
        ("abc", "Durante una visita de ejemplo, ves en el suelo un objeto que parece un cartucho explosivo. ¿Qué corresponde según las reglas generales?", "No tocarlo ni acercarte, avisar a un adulto responsable y a emergencias", "Recogerlo con cuidado para entregarlo", "Moverlo a un lugar más seguro", "Un objeto que parece explosivo no se toca ni se mueve."),
    ],
    ctx=("abc", "Un contratista de ejemplo te dice: «Ven al banco, te muestro cómo se hace una tronadura, la zona de exclusión es solo una formalidad». ¿Qué respondes?", "Que no: la zona de exclusión es obligatoria y solo personal autorizado participa, y que consultarás a un adulto responsable", "Que sí, si te quedas lejos", "Que sí, si no hay nadie más", "Una zona de exclusión es una barrera de seguridad, no una formalidad."),
    sc=[
        ("En Explotación Minera: ¿qué es un pozo?", "Un hoyo hecho en la roca por la perforación", "El pozo es el resultado de perforar."),
        ("En Explotación Minera: ¿quién dirige una tronadura?", "Un responsable autorizado", "Solo personal formado y autorizado realiza estas tareas."),
        ("¿Qué haces si encuentras algo que parece un explosivo?", "No lo tocas, no te acercas y avisas a un adulto responsable y a emergencias", "Nadie sin autorización maneja ni mueve explosivos."),
    ],
    op=("La faena ficticia «Mina Demo Cerro Claro» tiene un banco donde se perfora y se tronará mañana. Escribe (a) un peligro de la perforación y su riesgo asociado, (b) para qué sirve la zona de exclusión, (c) quiénes pueden participar en una tronadura, (d) qué haces si ves un objeto que parece un explosivo en el camino.",
        "(a) Peligro: el polvo; riesgo: que las personas lo respiren y se dañen los pulmones. (b) Para que nadie esté en el área de riesgo mientras la tronadura está activa. (c) Solo personal formado y autorizado por la empresa y la autoridad minera, bajo un responsable autorizado. (d) No lo toco ni me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "explica la zona de exclusión", "nombra quién puede participar", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que cualquier persona puede participar", "recoger o mover el objeto"],
        "Pregunta: «¿qué haces si ves algo que parece un explosivo?». Si no responde, pídele que relea el tercer párrafo de la explicación."),
    reinforce="Inventa una matriz de tres peligros de un banco con probabilidad y gravedad, calcula los puntajes y ordénalos.",
    extend="Explica con un ejemplo por qué una persona puede entender la tronadura y aun así no estar autorizada.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 16 (documentos de ejemplo, inventados). Diagrama de perforación de un banco de la faena ficticia «Mina Demo Piedra Azul»: 4 filas de pozos, con 6 pozos por fila. Espaciamiento (distancia entre pozos de una misma fila): 4 m. Burden (distancia entre una fila y la siguiente): 3 m. Profundidad de cada pozo: 10 m. Diámetro: 100 mm. "
     "Documentos: diagrama de perforación, programa de tronadura (que prepara y firma el responsable autorizado), registro de perforación y aviso de tronadura. Roles: el perforista maneja el equipo de perforación (solo personal formado y autorizado); el topógrafo marca en el terreno la ubicación de los pozos; el responsable autorizado dirige la tronadura; el supervisor organiza el sector; el prevencionista vela por la seguridad.")
build(
    O4, 2, F,
    use="Aprenderé a leer un diagrama de perforación, a conocer los documentos de una tronadura y a distinguir el rol de cada persona.",
    prior=["Sé qué es la perforación y qué es la tronadura.", "Sé multiplicar números enteros.", "Sé qué es una zona de exclusión."],
    explain=[
        "Un diagrama de perforación, también llamado malla, muestra dónde se harán los pozos: se organiza en filas. El espaciamiento es la distancia entre los pozos de una misma fila; el burden, o piedra, es la distancia entre una fila y la siguiente; la profundidad es el largo de cada pozo y el diámetro es su ancho. Con estos datos de planilla se calculan cuántos pozos hay y cuántos metros de perforación se necesitan.",
        "Los documentos de una tronadura son: el diagrama de perforación, el programa de tronadura, que prepara y firma el responsable autorizado; el registro de perforación, donde se anota lo realmente perforado; y el aviso de tronadura, que informa a las personas del sector. Sin documentos firmados y vigentes no se inicia ninguna etapa.",
        f"Los roles no se intercambian: el topógrafo marca, el perforista perfora, el responsable autorizado dirige la tronadura y el supervisor organiza. Este cuaderno no enseña a hacer ninguna de esas tareas. {EMER} {AVISO}",
    ],
    vocab=[("malla de perforación", "diagrama que muestra dónde se harán los pozos, ordenados en filas"), ("espaciamiento", "distancia entre pozos de una misma fila"), ("burden", "distancia entre una fila de pozos y la siguiente; también se llama piedra"), ("profundidad", "largo de cada pozo"), ("diámetro", "ancho de un pozo"), ("programa de tronadura", "documento que prepara y firma el responsable autorizado"), ("registro de perforación", "documento donde se anota lo realmente perforado")],
    worked=[
        ("Pozos de una malla", "Una malla de ejemplo tiene 3 filas de 8 pozos cada una. ¿Cuántos pozos tiene?", ["Se multiplican las filas por los pozos de cada fila.", "3 por 8 son 24 pozos."], "24 pozos"),
        ("Metros de perforación", "Una malla de ejemplo tiene 20 pozos de 8 m de profundidad cada uno. ¿Cuántos metros se deben perforar?", ["Se multiplican los pozos por la profundidad de cada uno.", "20 por 8 son 160 m."], "160 metros"),
    ],
    mistakes=[("Confundir espaciamiento y burden.", "El espaciamiento es entre pozos de la misma fila; el burden es entre filas.", "Pregúntate: ¿la distancia es a lo largo de una fila o de una fila a otra?"),
              ("Creer que un documento sin firma del responsable autorizado se puede usar «porque ya está listo».", "Sin documentos firmados y vigentes no se inicia ninguna etapa.", "Pide el documento firmado o avisa a la jefatura.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el espaciamiento de una malla de perforación?", "La distancia entre pozos de una misma fila", "La distancia entre una fila y la siguiente", "La profundidad de cada pozo", "El espaciamiento se mide a lo largo de una fila."),
        ("abc", "En Explotación Minera: ¿qué es el burden de una malla de perforación?", "La distancia entre una fila de pozos y la siguiente", "La distancia entre pozos de una misma fila", "El diámetro de cada pozo", "El burden separa las filas entre sí."),
        ("abc", "En Explotación Minera: ¿qué documento prepara y firma el responsable autorizado antes de una tronadura?", "El programa de tronadura", "El registro de perforación", "El diagrama de topografía", "El programa lo prepara y lo firma el responsable autorizado."),
        ("=", "{F} ¿Cuántos pozos tiene la malla?", "4*6", "Se multiplican las filas por los pozos de cada fila.", " pozos"),
        ("=", "{F} ¿Cuántos metros de perforación se necesitan en total?", "4*6*10", "Se multiplican los pozos de la malla por la profundidad de cada uno.", " m"),
        ("abc", "{F} ¿Qué rol marca en el terreno la ubicación de los pozos?", "El topógrafo", "El perforista", "El supervisor", "El topógrafo ubica los puntos; el perforista no decide dónde van."),
        ("=", "{F} ¿Cuántos metros de largo ocupa una fila de 6 pozos, medidos desde el primero hasta el último?", "(6-1)*4", "Entre 6 pozos hay 5 espacios de 4 m cada uno.", " m"),
        ("=", "{F} ¿Cuántos metros de ancho ocupa la malla, medidos desde la primera fila hasta la última?", "(4-1)*3", "Entre 4 filas hay 3 espacios de 3 m cada uno.", " m"),
        ("abc", "{F} ¿Qué documento registra lo que realmente se perforó?", "El registro de perforación", "El aviso de tronadura", "El diagrama de perforación", "El diagrama dice lo planificado; el registro, lo realizado."),
        ("abc", "{F} Un supervisor dice que la tronadura puede comenzar aunque el programa no esté firmado porque «ya está todo listo». ¿Qué corresponde?", "No iniciar y avisar a la jefatura: sin documentos firmados no se inicia ninguna etapa", "Iniciar si los pozos ya están perforados", "Iniciar si el responsable avisa por radio", "Los documentos firmados son condición para iniciar."),
        ("abc", "{F} ¿Por qué el perforista no decide por su cuenta cambiar la profundidad de los pozos?", "Porque la profundidad está fijada en el diagrama y cualquier cambio lo decide el responsable autorizado", "Porque la profundidad es siempre la misma en todas las minas", "Porque el perforista solo trabaja de día", "Los cambios deben pasar por el responsable y quedar documentados."),
        ("=", "{F} Si la malla tuviera 5 filas con los mismos 6 pozos por fila y 10 m de profundidad, ¿cuántos metros de perforación serían?", "5*6*10", "Se multiplican filas, pozos por fila y profundidad.", " m"),
        ("abc", "Una persona te cuenta que, en un banco de ejemplo, se escuchó una alarma y hay una persona dentro de la zona de exclusión. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a sacarla antes de que termine la alarma", "Esperar a que termine la alarma para avisar", "Entrar a una zona de exclusión activa es extremadamente peligroso."),
    ],
    ctx=("abc", "Una compañera de práctica ve en el diagrama de ejemplo que el espaciamiento es de 3 m y el burden es de 2 m, y dice que «da lo mismo cuál es cuál». ¿Qué respondes?", "Que no da lo mismo: el espaciamiento es entre pozos de una fila y el burden es entre filas", "Que da lo mismo, porque ambos son distancias", "Que el burden es la profundidad", "Cada término mide una distancia distinta en la malla."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el número de pozos de una malla?", "Filas por pozos de cada fila", "Se multiplica el número de filas por los pozos de cada una."),
        ("En Explotación Minera: ¿quién marca la ubicación de los pozos en el terreno?", "El topógrafo", "El topógrafo traslada el diagrama al terreno."),
        ("¿Qué se necesita para iniciar una etapa de una tronadura?", "Documentos firmados y vigentes", "Sin documentos firmados no se inicia ninguna etapa."),
    ],
    op=("Diagrama ficticio de la faena «Mina Demo Cerro Claro»: 3 filas de 5 pozos, espaciamiento de 4 m, burden de 3 m y profundidad de 12 m. Escribe (a) cuántos pozos hay, (b) cuántos metros de perforación se necesitan, (c) qué documento usarías para anotar lo realmente perforado, (d) qué haces si el programa de tronadura no está firmado.",
        "(a) 3 × 5 = 15 pozos. (b) 15 × 12 = 180 m. (c) El registro de perforación. (d) Aviso a la jefatura y no se inicia ninguna etapa hasta que esté firmado.",
        ["calcula los pozos", "calcula los metros", "elige el documento", "aplica la regla de documentos firmados"],
        ["hoja con las cuatro respuestas"],
        ["confundir filas con pozos", "olvidar la profundidad", "iniciar sin documentos firmados"],
        "Pregunta: «¿qué dos números multiplicas para los pozos?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Dibuja una malla de 3 filas de 4 pozos, rotula el espaciamiento y el burden con valores inventados y calcula los pozos.",
    extend="Explica con un ejemplo por qué el registro de perforación puede ser distinto del diagrama.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 17 (caso de ejemplo, inventado). Registro de perforación de un banco de la faena ficticia «Mina Demo Lomas Bajas». Diagrama: 10 pozos con profundidad planificada de 12 m y tolerancia de 1 m en más o en menos (valor de ejemplo). Profundidades realmente perforadas (m): P1 = 12; P2 = 12; P3 = 11; P4 = 12; P5 = 9; P6 = 12; P7 = 12; P8 = 14; P9 = 12; P10 = 12. "
     "Regla de ejemplo: un pozo fuera de tolerancia se informa de inmediato al responsable autorizado, quien decide qué hacer; nadie corrige un pozo por su cuenta. Además, el aviso de tronadura de ese banco está sin la firma del responsable autorizado.")
build(
    O4, 3, F,
    use="Aprenderé a analizar en papel un registro de perforación frente al diagrama: detectar desviaciones, calcular porcentajes, decidir a quién se informa y reconocer un documento incompleto.",
    prior=["Sé qué es la profundidad de un pozo.", "Sé qué es una tolerancia.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "Un registro de perforación se compara con el diagrama pozo por pozo. La diferencia entre lo planificado y lo realizado se llama desviación. Una tolerancia indica cuánta desviación se acepta: si la profundidad planificada es 12 m con tolerancia de 1 m, se acepta de 11 a 13 m, incluidos los extremos. Un pozo fuera de ese rango se informa de inmediato al responsable autorizado.",
        "El porcentaje de pozos dentro de tolerancia es los pozos dentro por 100 divididos entre los pozos totales. Un documento incompleto, como un aviso de tronadura sin firma del responsable autorizado, es una no conformidad: se informa y no se continúa hasta que se corrija.",
        f"Nadie corrige un pozo, ni completa una firma, por su cuenta. Este análisis es solo de papel y no habilita para trabajar en una perforación real. {EMER} {AVISO}",
    ],
    vocab=[("desviación", "diferencia entre lo planificado y lo realizado"), ("tolerancia", "desviación que se acepta"), ("fuera de tolerancia", "valor que queda fuera del rango aceptado"), ("no conformidad", "hallazgo que no cumple lo exigido y se registra e informa"), ("pozo dentro de tolerancia", "pozo cuya profundidad queda dentro del rango aceptado")],
    worked=[
        ("Rango de tolerancia", "Un pozo de ejemplo debía tener 8 m con tolerancia de 1 m. ¿Cuál es el rango aceptado?", ["El mínimo es 8 menos 1, es decir, 7 m.", "El máximo es 8 más 1, es decir, 9 m."], "De 7 a 9 m"),
        ("Clasificar un pozo", "Con ese rango, un pozo de ejemplo de 9 m, ¿está dentro de tolerancia?", ["El máximo aceptado es 9 m, y los extremos se aceptan.", "9 m está dentro del rango."], "Sí, está dentro"),
    ],
    mistakes=[("Creer que un pozo de 11 m está fuera de tolerancia por no medir 12 m.", "La tolerancia acepta de 11 a 13 m.", "Calcula primero el rango aceptado."),
              ("Completar la firma que falta en el aviso de tronadura para no atrasar el trabajo.", "Solo el responsable autorizado firma; falsear una firma es una falta grave.", "Informa que falta la firma y no se continúa.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una desviación en un registro de perforación?", "La diferencia entre lo planificado y lo realizado", "La cantidad de pozos que se perforó", "El nombre del equipo que perforó", "La desviación compara lo planificado con lo hecho."),
        ("abc", "En Explotación Minera: ¿qué significa que un pozo esté fuera de tolerancia?", "Que su profundidad queda fuera del rango aceptado", "Que se perforó en el lugar correcto", "Que el pozo es más ancho que el diagrama", "Fuera de tolerancia significa fuera del rango de profundidad aceptado."),
        ("abc", "En Explotación Minera: ¿qué es una no conformidad?", "Un hallazgo que no cumple lo exigido y que se registra e informa", "Un permiso que se aprueba", "Un pozo perforado en el tiempo previsto", "Una no conformidad es un incumplimiento registrado."),
        ("=", "{F} ¿Cuántos metros de profundidad mínima acepta la tolerancia?", "12-1", "Se resta la tolerancia a la profundidad planificada.", " m"),
        ("=", "{F} ¿Cuántos metros de profundidad máxima acepta la tolerancia?", "12+1", "Se suma la tolerancia a la profundidad planificada.", " m"),
        ("abc", "{F} ¿El pozo P3, de 11 m, está dentro de tolerancia?", "Sí, porque 11 m es el mínimo aceptado", "No, porque mide menos de 12 m", "No, porque está en el borde", "Los extremos del rango se aceptan."),
        ("abc", "{F} ¿Qué pozos están fuera de tolerancia?", "P5 y P8", "P3 y P5", "P3 y P8", "P5 tiene 9 m y P8 tiene 14 m; ambos quedan fuera del rango de 11 a 13 m."),
        ("=", "{F} ¿Cuántos metros por debajo de lo planificado quedó el pozo P5?", "12-9", "Se resta lo realizado a lo planificado.", " m"),
        ("=", "{F} ¿Qué porcentaje de los pozos quedó dentro de tolerancia?", "8*100//10", "Se multiplican por 100 los pozos dentro y se divide entre los totales.", " %"),
        ("abc", "{F} ¿A quién se informa el pozo P8 y cuándo?", "Al responsable autorizado, de inmediato", "Al topógrafo, al final del mes", "A nadie, porque el pozo es más profundo", "La regla indica informar de inmediato al responsable autorizado."),
        ("abc", "{F} Un asistente propone anotar 12 m en el registro para P5 «para que cuadre con el diagrama». ¿Qué corresponde?", "No hacerlo: se registra el valor real de 9 m y se informa el pozo", "Hacerlo si el pozo se ve bien", "Hacerlo si lo aprueba un compañero", "Un registro debe reflejar lo realmente perforado."),
        ("abc", "{F} ¿Qué corresponde con el aviso de tronadura sin firma del responsable autorizado?", "Informarlo como no conformidad y no continuar hasta que se firme", "Firmarlo con el nombre del jefe de turno", "Usarlo igual porque el responsable ya sabe", "Falsear una firma es una falta grave; sin firma no se continúa."),
        ("abc", "Una persona te cuenta que, en un banco de ejemplo, un camión se acercó a la zona de exclusión durante una alarma de tronadura. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para hacerle señas al conductor", "Esperar a que pase la alarma para informar", "Acercarse a una zona de exclusión activa es muy peligroso."),
    ],
    ctx=("abc", "Un asistente de ejemplo ve que el pozo P5 quedó en 9 m y dice: «lo completo con un metro más de perforación mañana y no aviso». ¿Qué respondes?", "Que no: se informa de inmediato al responsable autorizado, que decide qué hacer", "Que sí, porque así se corrige rápido", "Que sí, si lo hace a primera hora", "Nadie corrige un pozo por su cuenta; se informa y decide el responsable."),
    sc=[
        ("En Explotación Minera: ¿qué rango acepta una profundidad de 15 m con tolerancia de 2 m?", "De 13 a 17 m", "Se resta y se suma la tolerancia a la profundidad planificada."),
        ("¿Cómo se calcula el porcentaje de pozos dentro de tolerancia?", "Pozos dentro por 100, divididos entre los totales", "El porcentaje compara los pozos dentro con el total."),
        ("¿Qué se hace con un documento sin la firma exigida?", "Se informa como no conformidad y no se continúa", "Nadie completa ni falsea una firma ajena en un documento."),
    ],
    op=("Registro ficticio de la faena «Mina Demo Cerro Claro»: 8 pozos con profundidad planificada de 10 m y tolerancia de 1 m. Profundidades realizadas (m): 10; 11; 10; 8; 10; 9; 12; 10. Escribe (a) el rango aceptado, (b) cuáles pozos quedan fuera de tolerancia, (c) el porcentaje de pozos dentro de tolerancia, (d) qué haces con los pozos fuera de tolerancia.",
        "(a) De 9 a 11 m. (b) El de 8 m y el de 12 m. (c) 6 × 100 ÷ 8 = 75 %. (d) Se registran con su valor real y se informan de inmediato al responsable autorizado; nadie los corrige por su cuenta.",
        ["calcula el rango aceptado", "identifica los pozos fuera de tolerancia", "calcula el porcentaje", "describe el procedimiento de informe"],
        ["hoja con las cuatro respuestas"],
        ["rechazar un pozo en el límite", "dividir entre 6 en vez de entre 8", "corregir un pozo por su cuenta"],
        "Pregunta: «¿el pozo de 9 m se acepta?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un registro de 6 pozos de 8 m con tolerancia de 1 m, dos de ellos fuera de rango, y calcula el porcentaje dentro.",
    extend="Explica con un ejemplo por qué un registro debe mostrar lo realizado y no solo lo planificado.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 18 (planilla de ejemplo, inventada). Malla de perforación de un banco de la faena ficticia «Mina Demo Río Hondo»: 5 filas de 8 pozos, espaciamiento de 4 m, burden de 3 m, profundidad de 12 m y altura del banco de 10 m. Volumen de roca asignado a cada pozo = burden × espaciamiento × altura del banco. "
     "Rendimiento de ejemplo de un equipo de perforación: 24 metros por hora. Se asignan 2 equipos. Precio de ejemplo de la perforación: $9.000 por metro perforado. Turno de ejemplo: 10 horas.")
build(
    O4, 4, F,
    use="Aprenderé a calcular en una planilla los pozos, los metros, el volumen de roca, el tiempo y el costo de una perforación a partir de un diagrama, sin hacer ninguna operación de terreno.",
    prior=["Sé qué es una malla de perforación.", "Sé multiplicar y dividir números enteros.", "Sé calcular un volumen de una caja."],
    explain=[
        "Con la malla se calculan cuatro cosas en papel. Los pozos son las filas por los pozos de cada fila. Los metros de perforación son los pozos por la profundidad. El volumen de roca asignado a cada pozo es el burden por el espaciamiento por la altura del banco, y el volumen total es ese valor por los pozos. El tiempo es los metros divididos entre el rendimiento de todos los equipos juntos.",
        "El costo es los metros multiplicados por el precio por metro. En una planilla se escribe cada cálculo en una fila, con su unidad, y se revisa que los números tengan sentido: si el tiempo da muchísimo más que un turno, hay que revisar el cálculo o planificar más turnos. Los valores de esta planilla son de ejemplo; los reales los fija el proyecto.",
        f"Estos cálculos son de oficina: no incluyen ninguna decisión de terreno ni cantidad de explosivos. {EMER} {AVISO}",
    ],
    vocab=[("volumen de roca por pozo", "volumen asignado a cada pozo: burden por espaciamiento por altura del banco"), ("altura del banco", "alto del escalón que se perfora"), ("rendimiento", "metros que perfora un equipo en una hora"), ("planilla de costos", "tabla con cantidades, precios y totales"), ("turno", "período de trabajo de un grupo de personas")],
    worked=[
        ("Volumen por pozo", "En una malla de ejemplo el burden es 2 m, el espaciamiento es 5 m y el banco tiene 8 m de alto. ¿Qué volumen de roca corresponde a cada pozo?", ["Se multiplican burden, espaciamiento y altura.", "2 por 5 son 10, y 10 por 8 son 80 m³."], "80 m³"),
        ("Tiempo de perforación", "Una malla de ejemplo necesita 300 m de perforación y se usan 3 equipos de 20 m por hora cada uno. ¿Cuántas horas tarda?", ["Entre los 3 equipos perforan 60 m por hora.", "300 dividido entre 60 son 5 horas."], "5 horas"),
    ],
    mistakes=[("Dividir los metros entre el rendimiento de un solo equipo cuando trabajan varios.", "El rendimiento total es el de un equipo por la cantidad de equipos.", "Multiplica primero el rendimiento por los equipos."),
              ("Calcular el volumen por pozo con la profundidad del pozo en lugar de la altura del banco.", "La regla de la planilla usa la altura del banco.", "Lee qué dato pide la fórmula de la ficha.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el rendimiento de un equipo de perforación?", "Los metros que perfora en una hora", "El precio que cobra por cada pozo", "El diámetro de los pozos que hace", "El rendimiento mide metros por hora."),
        ("abc", "En Explotación Minera: ¿qué dato se usa en la planilla para calcular el volumen de roca de cada pozo?", "Burden, espaciamiento y altura del banco", "Solo la profundidad del pozo", "Solo el diámetro del pozo", "La fórmula de la planilla combina las tres distancias indicadas."),
        ("abc", "En Explotación Minera: ¿qué es una planilla de costos?", "Una tabla con cantidades, precios y totales", "Un plano de la mina", "Una lista de las personas del turno", "La planilla de costos organiza cantidades y precios."),
        ("=", "{F} ¿Cuántos pozos tiene la malla?", "5*8", "Se multiplican las filas por los pozos de cada fila.", " pozos"),
        ("=", "{F} ¿Cuántos metros de perforación necesita la malla?", "5*8*12", "Se multiplican los pozos por la profundidad de cada uno.", " m"),
        ("=", "{F} ¿Qué volumen de roca corresponde a cada pozo?", "3*4*10", "Se multiplican burden, espaciamiento y altura del banco.", " m³"),
        ("=", "{F} ¿Qué volumen total de roca corresponde a la malla?", "5*8*3*4*10", "Se multiplica el volumen por pozo por la cantidad de pozos.", " m³"),
        ("=", "{F} ¿Cuántos metros por hora perforan juntos los 2 equipos?", "24*2", "Se multiplica el rendimiento de un equipo por la cantidad de equipos.", " m/h"),
        ("=", "{F} ¿Cuántas horas tarda la perforación de toda la malla con los 2 equipos?", "5*8*12//(24*2)", "Se dividen los metros entre el rendimiento de los dos equipos.", " horas"),
        ("abc", "{F} ¿Se alcanza a perforar la malla en un solo turno de 10 horas?", "Sí, porque tarda 10 horas y el turno dura 10", "No, porque tarda más de 10 horas", "No, porque hay solo 2 equipos", "La perforación completa tarda exactamente 10 horas, lo que cabe en el turno."),
        ("=", "{F} ¿Cuánto cuesta la perforación de la malla completa?", "5*8*12*9000", "Se multiplican los metros por el precio por metro.", " pesos"),
        ("abc", "{F} Un asistente dice que con 4 equipos la malla tardaría 20 horas porque «más equipos, más tiempo». ¿Qué respondes?", "Que con 4 equipos tardaría 5 horas, porque más equipos reducen el tiempo", "Que tiene razón, porque hay más cosas que coordinar", "Que tardaría lo mismo, porque la malla no cambia", "A más equipos, mayor rendimiento total y menor tiempo para los mismos metros."),
        ("abc", "Una persona te cuenta que, mientras se perfora un banco de ejemplo, se acerca un grupo de visitantes sin autorización a mirar. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acompañar a los visitantes para que vean mejor", "Dejar que miren si usan casco", "La zona de perforación solo la ocupa personal autorizado."),
    ],
    ctx=("abc", "Un jefe de turno de ejemplo calcula el tiempo de perforar 600 m con 2 equipos de 30 m por hora y escribe «600 ÷ 30 = 20 horas». ¿Qué respondes?", "Que los dos equipos rinden 60 m por hora juntos, así que son 600 ÷ 60 = 10 horas", "Que está correcto, porque 600 dividido entre 30 son 20", "Que son 40 horas, porque hay que multiplicar el tiempo por los 2 equipos", "Con varios equipos se usa el rendimiento total, no el de uno solo."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el tiempo de perforación?", "Metros divididos entre el rendimiento total de los equipos", "El rendimiento total es el de un equipo por la cantidad de equipos."),
        ("¿Cómo se calcula el volumen de roca por pozo en la planilla de ejemplo?", "Burden por espaciamiento por altura del banco", "Es una multiplicación de tres distancias."),
        ("¿Cómo se calcula el costo de la perforación?", "Metros por el precio por metro", "El costo multiplica la cantidad por el precio unitario."),
    ],
    op=("Planilla ficticia de la faena «Mina Demo Cerro Claro»: malla de 4 filas de 6 pozos, burden de 3 m, espaciamiento de 4 m, profundidad de 10 m, altura del banco de 9 m. Rendimiento de ejemplo: 20 m por hora por equipo, con 2 equipos. Precio de ejemplo: $8.000 por metro. Escribe (a) pozos y metros de perforación, (b) volumen total de roca de la malla, (c) horas de perforación, (d) costo de la perforación.",
        "(a) 4 × 6 = 24 pozos y 24 × 10 = 240 m. (b) 3 × 4 × 9 = 108 m³ por pozo, y 24 × 108 = 2.592 m³. (c) 240 ÷ (20 × 2) = 6 horas. (d) 240 × 8.000 = $1.920.000.",
        ["calcula pozos y metros", "calcula el volumen", "calcula las horas con los dos equipos", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["usar el rendimiento de un solo equipo", "usar la profundidad en vez de la altura del banco", "olvidar multiplicar por los pozos"],
        "Pregunta: «¿entre qué número dividiste los metros y por qué?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una malla de 3 filas de 5 pozos, define burden, espaciamiento y altura, y calcula el volumen total.",
    extend="Explica con un ejemplo por qué una planilla de oficina no reemplaza las decisiones del responsable autorizado.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 19 (caso de ejemplo, inventado). La empresa ficticia «Minera Demo Altiplano» tiene una planta de beneficio con 120 personas. En un año la autoridad minera hizo 4 inspecciones de seguridad (dato de ejemplo): en 3 no hubo observaciones y en 1 se anotaron 2 observaciones, que la empresa corrigió. "
     "En el programa anual de prevención de ejemplo, 96 de las 120 personas completaron la capacitación. Normas que aplican a la empresa, de mayor a menor jerarquía: la Constitución, las leyes, los reglamentos y los procedimientos internos de la empresa. Peligros anotados: polvo, ruido, tránsito de vehículos y falta de señales.")
build(
    O5, 1, F,
    use="Aprenderé qué es el marco legal minero, quién fiscaliza su cumplimiento, cómo se ordenan las normas y por qué su incumplimiento es un riesgo para las personas y para la empresa.",
    prior=["Sé qué es una norma.", "Sé calcular un porcentaje sencillo.", "Sé qué es un peligro y un riesgo."],
    explain=[
        "El marco legal minero es el conjunto de normas que regulan la actividad minera: la propiedad minera, la seguridad de las personas, la prevención de riesgos y el cuidado del medio ambiente. Las normas se ordenan por jerarquía: la Constitución, las leyes, los reglamentos y, por debajo, los procedimientos internos de cada empresa. Si un procedimiento interno contradice una ley, prevalece la ley. Fiscalizar es revisar que las normas se cumplan, y la autoridad minera fiscaliza la seguridad de las faenas, mientras que otras autoridades fiscalizan el medio ambiente y el trabajo.",
        "Cumplir la norma protege a las personas y evita sanciones, que son medidas que se aplican cuando alguien incumple, como una multa o la paralización de una faena. Una inspección es una visita de revisión y puede terminar sin observaciones o con observaciones que la empresa debe corregir. En este cuaderno las cifras de inspecciones y de capacitación son de ejemplo.",
        f"Nadie debe saltarse una norma para producir más rápido ni esperar a que lo fiscalicen para cumplirla. Este cuaderno no entrega asesoría legal: ante una duda, se consulta a un adulto responsable o a la autoridad competente. {EMER} {AVISO}",
    ],
    vocab=[("marco legal minero", "conjunto de normas que regulan la actividad minera"), ("jerarquía de normas", "orden de las normas: Constitución, leyes, reglamentos y procedimientos internos"), ("fiscalizar", "revisar que las normas se cumplan"), ("inspección", "visita de revisión de una autoridad"), ("sanción", "medida que se aplica cuando alguien incumple una norma"), ("autoridad minera", "institución del Estado que fiscaliza la seguridad de las faenas")],
    worked=[
        ("Porcentaje de capacitación", "En otra empresa de ejemplo, 45 de 50 personas completaron una capacitación. ¿Qué porcentaje es?", ["Se multiplican por 100 las personas capacitadas y se divide entre el total.", "45 por 100 dividido entre 50 son 90."], "90 %"),
        ("Jerarquía de normas", "El procedimiento interno de una empresa de ejemplo dice que se puede trabajar sin protección en un lugar donde un reglamento la exige. ¿Cuál prevalece?", ["El procedimiento interno está por debajo del reglamento.", "Prevalece el reglamento."], "El reglamento"),
    ],
    mistakes=[("Creer que un procedimiento interno de la empresa puede estar por encima de una ley.", "La jerarquía pone la ley sobre los procedimientos internos.", "Si hay contradicción, se cumple la norma de mayor jerarquía y se informa."),
              ("Creer que se cumple la norma solo cuando hay una inspección.", "La norma se cumple siempre, no solo cuando se fiscaliza.", "Cumple las reglas todos los días, haya o no haya inspección.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el marco legal minero?", "El conjunto de normas que regulan la actividad minera", "El conjunto de máquinas que usa una faena", "La lista de las personas que trabajan en la mina", "El marco legal reúne las normas, no los equipos ni las personas."),
        ("abc", "En Explotación Minera: ¿qué significa fiscalizar?", "Revisar que las normas se cumplan", "Producir más mineral por turno", "Entregar equipos de protección", "Fiscalizar es comprobar el cumplimiento de las normas."),
        ("abc", "En Explotación Minera: ¿qué es una sanción?", "Una medida que se aplica cuando alguien incumple una norma", "Un permiso para trabajar en una zona", "Un premio por cumplir las metas de producción", "La sanción responde a un incumplimiento."),
        ("=", "{F} Si corregir cada observación toma 3 días, ¿cuántos días de corrección necesita la empresa en total?", "2*3", "Se multiplican las observaciones anotadas por los días de cada corrección.", " días"),
        ("abc", "{F} ¿Cuál es el orden de las normas, de mayor a menor jerarquía?", "Constitución, leyes, reglamentos y procedimientos internos", "Procedimientos internos, reglamentos, leyes y Constitución", "Leyes, Constitución, procedimientos internos y reglamentos", "La jerarquía va de lo más general a lo más particular."),
        ("abc", "{F} ¿Qué autoridad fiscalizó la seguridad de la planta según la ficha?", "La autoridad minera", "La empresa por su cuenta", "Una persona del turno", "La ficha dice que la autoridad minera hizo las inspecciones de seguridad."),
        ("=", "{F} ¿Qué porcentaje de las inspecciones del año no tuvo observaciones?", "3*100//4", "Se multiplican por 100 las inspecciones sin observaciones y se divide entre el total.", " %"),
        ("=", "{F} ¿Qué porcentaje de las 120 personas completó la capacitación?", "96*100//120", "Se multiplican por 100 las personas capacitadas y se divide entre el total.", " %"),
        ("=", "{F} ¿Cuántas personas faltan por capacitar?", "120-96", "Se resta las personas capacitadas al total.", " personas"),
        ("abc", "{F} ¿Cuál de las normas de la ficha tiene la menor jerarquía?", "Los procedimientos internos de la empresa", "Los reglamentos", "Las leyes", "Los procedimientos internos están por debajo de reglamentos, leyes y Constitución."),
        ("abc", "{F} ¿Por qué no basta con cumplir la norma solo cuando llega la inspección?", "Porque la norma protege a las personas todos los días, no solo cuando se fiscaliza", "Porque las inspecciones son todos los días", "Porque las sanciones solo se aplican a los trabajadores", "La norma existe para prevenir daños siempre."),
        ("=", "{F} La empresa se propone capacitar a las personas que faltan en grupos de 6. ¿Cuántos grupos necesita?", "(120-96)//6", "Se divide el número de personas por capacitar entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, ves que una pared del almacén se está viniendo abajo y que hay personas adentro. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a sacar a las personas", "Fotografiar el daño para el informe", "Entrar a una estructura que cede sin formación pone en riesgo a otras personas."),
    ],
    ctx=("abc", "Un compañero de práctica te dice: «da lo mismo que falte una señal en el patio, el inspector pasa una vez al año». ¿Qué respondes?", "Que la norma se cumple todos los días porque protege a las personas, y que se debe informar la señal que falta", "Que tiene razón, porque la inspección es lo único que importa", "Que no importa si nadie se queja", "El cumplimiento de la norma no depende de que llegue una inspección."),
    sc=[
        ("En Explotación Minera: ¿qué es el marco legal minero?", "El conjunto de normas que regulan la actividad minera", "Incluye propiedad minera, seguridad, prevención y medio ambiente."),
        ("¿Qué norma prevalece si un procedimiento interno contradice una ley?", "La ley", "La ley tiene mayor jerarquía que un procedimiento interno."),
        ("¿Cómo se calcula el porcentaje de personas capacitadas?", "Capacitadas por 100, divididas entre el total", "El porcentaje compara las personas capacitadas con el total de la dotación."),
    ],
    op=("La empresa ficticia «Minera Demo Cerro Claro» tuvo 5 inspecciones de seguridad en un año: 4 sin observaciones y 1 con 3 observaciones. De sus 80 personas, 60 completaron la capacitación anual. Escribe (a) el porcentaje de inspecciones sin observaciones, (b) el porcentaje de personas capacitadas, (c) qué debe hacer la empresa con las observaciones, (d) por qué se debe cumplir la norma aunque no haya inspección.",
        "(a) 4 × 100 ÷ 5 = 80 %. (b) 60 × 100 ÷ 80 = 75 %. (c) Corregirlas y dejar constancia. (d) Porque la norma protege a las personas todos los días, no solo cuando hay una fiscalización.",
        ["calcula el porcentaje de inspecciones", "calcula el porcentaje de capacitación", "describe qué hacer con las observaciones", "justifica el cumplimiento permanente"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre 4 en vez de entre 5", "creer que la norma solo importa en las inspecciones", "no mencionar la corrección de las observaciones"],
        "Pregunta: «¿entre qué número dividiste en cada porcentaje?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una empresa con 6 inspecciones y 100 personas, y calcula el porcentaje de inspecciones sin observaciones y de personas capacitadas.",
    extend="Explica con un ejemplo qué puede pasar si una empresa solo cumple la norma cuando la fiscalizan.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 20 (documentos y roles de ejemplo, inventados). Faena ficticia «Mina Demo Piedra Azul». Documentos: título de concesión minera (derecho a explorar o explotar un mineral dentro de un área, distinto de ser dueño del terreno superficial); reglamento interno de la empresa; plan de emergencia; programa de prevención; registro de capacitación; informe de accidente; resolución ambiental (documento de la autoridad ambiental que aprueba un proyecto con condiciones). "
     "Una patente minera es un pago anual para mantener una concesión. Responsabilidad individual: la de cada trabajador (cumplir normas, usar sus elementos de protección, informar peligros). Responsabilidad colectiva: la de los grupos, como el comité paritario de higiene y seguridad, formado por representantes de los trabajadores y de la empresa. "
     "Responsabilidad empresarial: la de la empresa (dar condiciones seguras, capacitar, mantener los planes y cumplir las condiciones ambientales).")
build(
    O5, 2, F,
    use="Aprenderé los documentos básicos del marco legal minero y los tres tipos de responsabilidad: individual, colectiva y empresarial.",
    prior=["Sé qué es el marco legal minero.", "Sé qué es una norma.", "Sé qué es un registro."],
    explain=[
        "La concesión minera es un derecho para explorar o explotar un mineral dentro de un área, otorgado según el Código de Minería; no es lo mismo que ser dueño del terreno de la superficie. Para mantenerla se paga una patente anual. Quien explota sin tener la concesión incumple la norma. Esto se llama propiedad minera y es uno de los contenidos del marco legal.",
        "Hay tres tipos de responsabilidad. La individual es la de cada trabajador: cumplir las normas, usar sus elementos de protección e informar los peligros. La colectiva es la de los grupos, como el comité paritario de higiene y seguridad, que reúne a representantes de los trabajadores y de la empresa para vigilar la prevención. La empresarial es la de la empresa: dar condiciones seguras, capacitar, mantener los planes de emergencia y cumplir las condiciones ambientales.",
        f"Los documentos dejan constancia: el plan de emergencia dice qué hacer en una emergencia, el registro de capacitación muestra quién se capacitó, el informe de accidente describe lo ocurrido y la resolución ambiental fija condiciones para proteger el entorno. {EMER} {AVISO}",
    ],
    vocab=[("concesión minera", "derecho para explorar o explotar un mineral dentro de un área"), ("patente minera", "pago anual para mantener una concesión"), ("responsabilidad individual", "la de cada trabajador"), ("responsabilidad colectiva", "la de los grupos, como el comité paritario"), ("responsabilidad empresarial", "la de la empresa"), ("comité paritario", "grupo de representantes de los trabajadores y de la empresa que vigila la prevención"), ("resolución ambiental", "documento de la autoridad ambiental que aprueba un proyecto con condiciones")],
    worked=[
        ("Clasificar una responsabilidad", "En una faena de ejemplo, un trabajador ve un cable pelado y no avisa. ¿De qué tipo es la responsabilidad que se incumplió?", ["Informar los peligros es un deber de cada trabajador.", "Es una responsabilidad individual."], "Individual"),
        ("Patente anual", "Una concesión de ejemplo de 40 hectáreas paga una patente de $3.000 por hectárea al año (valor de ejemplo). ¿Cuánto es?", ["Se multiplican las hectáreas por el valor de cada una.", "40 por 3.000 son 120.000."], "$120.000 al año"),
    ],
    mistakes=[("Creer que la concesión minera hace dueño del terreno de la superficie.", "La concesión da derecho sobre el mineral, no sobre el terreno superficial.", "Distingue siempre el derecho minero del terreno de la superficie."),
              ("Creer que la seguridad es responsabilidad solo de la empresa.", "También hay responsabilidad individual y colectiva.", "Cada nivel cumple su parte: trabajador, grupo y empresa.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una concesión minera?", "Un derecho para explorar o explotar un mineral dentro de un área", "La propiedad del terreno de la superficie", "Un permiso para entrar a la faena", "La concesión da derecho sobre el mineral, no sobre el terreno superficial."),
        ("abc", "En Explotación Minera: ¿qué es la responsabilidad individual?", "La de cada trabajador, como usar sus elementos de protección", "La de la empresa de capacitar al personal", "La de un comité que vigila la prevención", "La responsabilidad individual es la de cada persona."),
        ("abc", "En Explotación Minera: ¿qué es un comité paritario?", "Un grupo de representantes de los trabajadores y de la empresa que vigila la prevención", "Un grupo de directivos que fija los precios", "Un grupo de inspectores de la autoridad minera", "El comité paritario reúne a ambas partes."),
        ("=", "{F} Una concesión de 50 hectáreas paga una patente de $2.000 por hectárea al año. ¿Cuánto paga en total?", "50*2000", "Se multiplican las hectáreas por el valor de cada una.", " pesos"),
        ("abc", "{F} ¿Qué documento muestra quién ha completado una capacitación?", "El registro de capacitación", "El plan de emergencia", "El título de concesión", "El registro deja constancia de quién se capacitó."),
        ("abc", "{F} ¿Qué documento describe lo ocurrido después de un accidente?", "El informe de accidente", "La resolución ambiental", "La patente minera", "El informe de accidente relata los hechos."),
        ("abc", "{F} Un trabajador no usa su casco en una zona donde es obligatorio. ¿Qué responsabilidad incumple?", "La individual", "La empresarial", "La colectiva", "Usar sus elementos de protección es un deber personal."),
        ("abc", "{F} La empresa no capacitó a sus 10 trabajadores nuevos. ¿Qué responsabilidad incumple?", "La empresarial", "La individual", "La colectiva", "Capacitar es un deber de la empresa."),
        ("abc", "{F} El comité paritario no investiga un incidente que debía revisar. ¿Qué responsabilidad incumple?", "La colectiva", "La individual", "La empresarial", "El comité es un grupo que vigila la prevención."),
        ("abc", "{F} ¿Por qué la concesión no autoriza a hacer cualquier cosa en el terreno de la superficie?", "Porque da derecho sobre el mineral y no sobre el terreno, que tiene sus propias normas y dueños", "Porque la concesión solo vale de noche", "Porque la concesión se vence cada semana", "El terreno de la superficie se rige por otras normas."),
        ("abc", "{F} Una empresa dice que, como tiene la resolución ambiental, ya no necesita cumplir sus condiciones. ¿Qué es correcto?", "Debe cumplir las condiciones de la resolución durante toda la operación", "No necesita cumplirlas, porque ya fue aprobada", "Solo debe cumplirlas cuando hay inspección", "La aprobación del proyecto trae condiciones que deben cumplirse siempre."),
        ("=", "{F} Si la concesión de 50 hectáreas se ampliara a 70 hectáreas con la misma patente de $2.000 por hectárea, ¿cuántos pesos más pagaría al año?", "(70-50)*2000", "Se multiplican las hectáreas agregadas por el valor de cada una.", " pesos"),
        ("abc", "Un compañero te cuenta que en una faena de ejemplo hubo un derrumbe con personas atrapadas. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a ayudar a rescatarlas", "Esperar el informe de accidente antes de avisar", "El rescate lo hacen equipos formados; lo tuyo es avisar."),
    ],
    ctx=("abc", "Una persona te dice: «Tengo una concesión minera, así que puedo cerrar el camino que pasa por mi terreno y nadie me dice nada». ¿Qué respondes?", "Que la concesión es sobre el mineral y que el uso del terreno y de los caminos se rige por otras normas, así que debe consultarse a la autoridad competente", "Que sí, porque la concesión hace dueño de todo", "Que sí, mientras pague la patente", "La concesión minera no da dominio sobre el terreno superficial."),
    sc=[
        ("En Explotación Minera: ¿qué es una patente minera?", "Un pago anual para mantener una concesión", "Mantener la concesión implica pagar la patente cada año."),
        ("En Explotación Minera: ¿qué es la responsabilidad empresarial?", "La de la empresa de dar condiciones seguras y capacitar", "La empresa responde por las condiciones de trabajo."),
        ("¿Qué documento dice qué hacer en una emergencia?", "El plan de emergencia", "Es el documento de referencia ante una emergencia."),
    ],
    op=("Situaciones ficticias de la «Minera Demo Cerro Claro»: (1) un trabajador no informa que una baranda está suelta; (2) la empresa no mantiene actualizado su plan de emergencia; (3) el comité paritario no revisa los registros del mes. Escribe (a) qué tipo de responsabilidad se incumple en cada situación, (b) qué documento de los nombrados en la explicación debería actualizarse en el caso (2), (c) qué haría una persona que ve la baranda suelta, (d) por qué la concesión no autoriza a incumplir estas normas.",
        "(a) 1 es individual, 2 es empresarial, 3 es colectiva. (b) El plan de emergencia. (c) Avisar a un responsable para que se corrija. (d) Porque la concesión da derecho sobre el mineral, no exime de cumplir las normas de seguridad y de medio ambiente.",
        ["clasifica las tres responsabilidades", "relaciona el caso 2 con su documento", "propone qué hacer ante un peligro", "explica el alcance de la concesión"],
        ["hoja con las cuatro respuestas"],
        ["confundir la responsabilidad colectiva con la individual", "creer que la concesión exime de cumplir normas", "no avisar del peligro"],
        "Pregunta: «¿quién incumple en cada caso: una persona, un grupo o la empresa?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa tres situaciones de una faena y clasifica cada una según el tipo de responsabilidad.",
    extend="Explica con un ejemplo por qué la seguridad exige las tres responsabilidades a la vez.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 21 (caso de ejemplo, inventado). Informe interno de una revisión en la planta de la empresa ficticia «Minera Demo Lomas Bajas». Situaciones: S1, un operador entra a una zona señalizada sin su casco. S2, la empresa no entregó la capacitación anual a 10 personas nuevas. S3, el comité paritario no revisó un incidente del mes. "
     "S4, un trabajador vio un cable de energía pelado y lo comentó a un compañero, pero no avisó a su jefatura. S5, la planta vertió agua sin cumplir una condición de su resolución ambiental de ejemplo. S6, una persona externa empezó a extraer mineral en un área sin tener título de concesión. "
     "Plan de acción de ejemplo: cada situación se asigna a una responsabilidad (individual, colectiva, empresarial) o a propiedad minera, y se anota qué se debe hacer.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso en papel: asignar cada situación a su tipo de responsabilidad, decidir qué se debe hacer y contar y calcular porcentajes con los datos del caso.",
    prior=["Sé qué son las responsabilidades individual, colectiva y empresarial.", "Sé qué es la concesión minera.", "Sé calcular un porcentaje."],
    explain=[
        "Para analizar un caso se lee cada situación y se pregunta quién tenía el deber: una persona (individual), un grupo (colectiva) o la empresa (empresarial). Si la situación trata de explotar mineral sin título, no es un tema de seguridad sino de propiedad minera. Cada incumplimiento se informa a quien corresponde y se corrige.",
        "Una situación puede combinar dos responsabilidades: por ejemplo, si un trabajador no usa su casco porque la empresa no se lo entregó, la responsabilidad es de la empresa que no lo dio y también de quien lo sabía y no avisó. Para contar, se agrupan las situaciones por tipo y se calcula el porcentaje que representa cada grupo.",
        f"Este es un análisis de papel: las sanciones y las decisiones legales las determinan las autoridades competentes, no un cuaderno. {EMER} {AVISO}",
    ],
    vocab=[("incumplimiento", "hecho de no cumplir una norma o un deber"), ("deber", "obligación que tiene una persona, un grupo o una empresa"), ("explotar sin título", "extraer mineral sin tener la concesión"), ("plan de acción", "lista de lo que se debe corregir y por quién"), ("informar", "avisar a quien corresponde")],
    worked=[
        ("Clasificar una situación", "En una faena de ejemplo, la empresa no entrega mascarillas a quienes trabajan con polvo. ¿De qué tipo es la responsabilidad incumplida?", ["Dar elementos de protección es un deber de la empresa.", "Es una responsabilidad empresarial."], "Empresarial"),
        ("Porcentaje de un grupo", "De 8 situaciones de ejemplo, 2 son de responsabilidad individual. ¿Qué porcentaje es?", ["Se multiplican por 100 las situaciones individuales y se divide entre el total.", "2 por 100 dividido entre 8 son 25."], "25 %"),
    ],
    mistakes=[("Asignar todas las situaciones a la empresa porque «ella es la responsable de todo».", "También hay deberes de cada persona y de los grupos.", "Pregunta quién tenía el deber en cada situación."),
              ("Creer que quien vio un peligro y se lo contó solo a un compañero ya cumplió.", "Hay que avisar a la jefatura o al responsable.", "Informa a quien puede corregir el peligro.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un incumplimiento?", "No cumplir una norma o un deber", "Cumplir una norma con retraso", "Cambiar de turno sin avisar", "Incumplir es no hacer lo que la norma o el deber exigen."),
        ("abc", "En Explotación Minera: ¿qué es explotar sin título?", "Extraer mineral sin tener la concesión", "Extraer mineral con una patente impaga hace una semana", "Extraer mineral en turno de noche", "Explotar sin título es no tener el derecho minero."),
        ("abc", "En Explotación Minera: ¿qué es un plan de acción?", "Una lista de lo que se debe corregir y quién lo hace", "Un permiso para volver a producir", "Una multa de la autoridad", "El plan de acción ordena las correcciones."),
        ("abc", "{F} ¿De qué tipo es la responsabilidad en S1, el operador sin casco?", "Individual", "Empresarial", "Colectiva", "Usar sus elementos de protección es un deber personal."),
        ("abc", "{F} ¿De qué tipo es la responsabilidad en S2, la capacitación no entregada?", "Empresarial", "Individual", "Colectiva", "Capacitar es un deber de la empresa."),
        ("abc", "{F} ¿De qué tipo es la responsabilidad en S3, el incidente sin revisar?", "Colectiva, porque es un deber del comité paritario", "Individual, porque la revisión es de una sola persona", "Empresarial, porque solo la empresa puede revisar", "El comité paritario es un grupo que vigila la prevención."),
        ("abc", "{F} ¿A qué contenido pertenece la situación S6?", "A la propiedad minera, porque extraer mineral exige título de concesión", "A la responsabilidad individual, porque lo hace una persona", "A la responsabilidad colectiva, porque hay un grupo", "Explotar sin título es un tema de propiedad minera."),
        ("abc", "{F} En S4, ¿qué debió hacer el trabajador?", "Avisar a su jefatura o al responsable de inmediato, sin tocar el cable", "Comentarlo solo con su compañero", "Esperar a ver si el cable se arregla solo", "Informar a quien puede corregir el peligro es su deber individual."),
        ("=", "{F} Cada situación suma puntos de alerta: 3 las empresariales y 1 las individuales (valores de ejemplo). ¿Cuántos puntos suman S1, S2, S4 y S5 juntas?", "1+3+1+3", "S1 y S4 son individuales y S2 y S5 son empresariales.", " puntos"),
        ("=", "{F} ¿Qué porcentaje de las 6 situaciones es de responsabilidad individual o colectiva (S1, S3 y S4)?", "3*100//6", "Se multiplican por 100 esas tres situaciones y se divide entre el total.", " %"),
        ("abc", "{F} Para S5, ¿quién debe corregir el incumplimiento ambiental y cuándo?", "La empresa, tan pronto como lo detecta, informando a quien corresponde", "El trabajador de turno, cuando termine su jornada", "La autoridad, sin que la empresa haga nada", "El cumplimiento de la resolución ambiental es un deber de la empresa."),
        ("abc", "{F} Un jefe propone no informar S2 «porque son personas nuevas y todavía no se lastiman». ¿Qué corresponde?", "Informarlo y capacitar a las 10 personas, porque es un deber de la empresa", "No informarlo hasta que ocurra un accidente", "Capacitarlas solo si se quejan", "El deber de capacitar existe antes de que haya un accidente."),
        ("abc", "Durante una visita de ejemplo, ves a un compañero que cae a una fosa con maquinaria en movimiento. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sacarlo de la fosa", "Anotar el incumplimiento antes de avisar", "Acercarte a una máquina en movimiento puede causar otro accidente."),
    ],
    ctx=("abc", "En una charla de ejemplo, un participante dice: «si algo sale mal, la culpa siempre es del trabajador que lo hizo». ¿Qué respondes?", "Que la responsabilidad puede ser de la persona, del grupo o de la empresa, según quién tenía el deber en cada caso", "Que tiene razón, porque el trabajador está en el lugar", "Que la culpa es siempre de la empresa", "El marco legal reparte deberes entre las personas, los grupos y la empresa."),
    sc=[
        ("En Explotación Minera: ¿qué pregunta ayuda a clasificar una situación?", "¿Quién tenía el deber: una persona, un grupo o la empresa?", "El deber determina el tipo de responsabilidad."),
        ("¿A qué contenido pertenece extraer mineral sin concesión?", "A la propiedad minera", "El derecho de extraer mineral lo da la concesión."),
        ("¿Qué debe hacer quien ve un cable pelado?", "Avisar a la jefatura sin tocarlo", "Informar a quien puede corregir el peligro es un deber."),
    ],
    op=("Informe ficticio de la «Minera Demo Cerro Claro»: S1, un conductor no respeta una señal de velocidad; S2, la empresa no revisa el plan de emergencia hace dos años; S3, el comité paritario no se reúne en el mes; S4, un trabajador ve una fuga de aceite y no avisa. Escribe (a) el tipo de responsabilidad de cada situación, (b) qué porcentaje de las 4 situaciones es individual, (c) qué se debe hacer con S2, (d) qué hace una persona que ve la fuga de aceite.",
        "(a) S1 individual, S2 empresarial, S3 colectiva y S4 individual. (b) 2 × 100 ÷ 4 = 50 %. (c) Informarlo y actualizar el plan de emergencia. (d) Avisar a la jefatura para que se corrija, sin intentar repararla.",
        ["clasifica cada situación", "calcula el porcentaje", "propone una acción para S2", "describe qué hacer ante un peligro"],
        ["hoja con las cuatro respuestas"],
        ["culpar siempre a la empresa", "dividir entre un número distinto de 4", "no informar el peligro"],
        "Pregunta: «¿quién tenía el deber en S3?». Si no responde, pídele que relea la definición de responsabilidad colectiva."),
    reinforce="Inventa cuatro situaciones de una faena y clasifícalas según el tipo de responsabilidad.",
    extend="Explica con un ejemplo cómo una misma situación puede involucrar dos responsabilidades.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 22 (planilla de ejemplo, inventada). Datos de un año de la planta de la empresa ficticia «Minera Demo Altiplano». Horas trabajadas por todo el personal: 500.000. Accidentes con tiempo perdido (accidentes tras los cuales la persona debió faltar al trabajo): 2. "
     "Fórmula de ejemplo de la tasa de frecuencia: accidentes con tiempo perdido × 1.000.000 ÷ horas trabajadas. Meta de la empresa (de ejemplo): una tasa de frecuencia menor o igual a 5. "
     "Capacitación: 96 de 120 personas capacitadas; meta de ejemplo: al menos 90 %. Inspecciones de seguridad internas: 12 programadas en el año y 9 realizadas. Cumplimiento ambiental: 8 condiciones de la resolución ambiental y 7 cumplidas.")
build(
    O5, 4, F,
    use="Aprenderé a calcular en una planilla algunos indicadores de seguridad y de cumplimiento (tasa de frecuencia, porcentajes de capacitación, de inspecciones y ambiental) y a compararlos con metas.",
    prior=["Sé calcular porcentajes.", "Sé qué es una meta.", "Sé qué es el marco legal minero."],
    explain=[
        "Un indicador es un número que resume qué tan bien se cumple algo. La tasa de frecuencia de accidentes compara los accidentes con tiempo perdido con las horas trabajadas, multiplicados por 1.000.000 para obtener un número fácil de comparar. Mientras menor sea, mejor, porque indica menos accidentes por cada millón de horas trabajadas. La fórmula y las metas de este cuaderno son de ejemplo.",
        "Un indicador de cumplimiento es un porcentaje: lo realizado por 100, dividido entre lo programado o exigido. Se compara con una meta: si la supera o la iguala, cumple; si queda debajo, no cumple y se informa para corregir. Los indicadores no reemplazan la prevención: detrás de cada accidente hay una persona, y un buen indicador no autoriza a descuidar la seguridad.",
        f"Las cifras reales las fija la norma vigente y las calcula personal de prevención con registros verificados. No se debe alterar ningún dato para llegar a la meta. {EMER} {AVISO}",
    ],
    vocab=[("indicador", "número que resume qué tan bien se cumple algo"), ("tasa de frecuencia", "accidentes con tiempo perdido por millón de horas trabajadas"), ("meta", "valor que se quiere alcanzar o no superar"), ("accidente con tiempo perdido", "accidente tras el cual la persona debe faltar al trabajo"), ("programado", "lo que estaba planificado hacer")],
    worked=[
        ("Tasa de frecuencia", "En una empresa de ejemplo hubo 3 accidentes con tiempo perdido en 600.000 horas trabajadas. ¿Cuál es la tasa de frecuencia?", ["Se multiplican los accidentes por 1.000.000.", "3.000.000 dividido entre 600.000 son 5."], "5"),
        ("Comparar con la meta", "Una empresa de ejemplo tiene una meta de capacitar al 80 % y capacitó a 36 de 40 personas. ¿Cumple?", ["36 por 100 dividido entre 40 son 90 %.", "90 % es mayor que la meta de 80 %."], "Sí, cumple"),
    ],
    mistakes=[("Calcular la tasa de frecuencia dividiendo los accidentes entre las horas, sin multiplicar por 1.000.000.", "El factor 1.000.000 permite comparar empresas de distinto tamaño.", "Aplica la fórmula completa."),
              ("Cambiar un dato de accidentes para no superar la meta.", "Alterar un registro es una falta grave y oculta un problema real.", "Registra el valor real e informa.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un indicador?", "Un número que resume qué tan bien se cumple algo", "Una señal luminosa de una máquina", "Un permiso de la autoridad", "Un indicador resume un nivel de cumplimiento."),
        ("abc", "En Explotación Minera: ¿qué mide la tasa de frecuencia de accidentes de la planilla de ejemplo?", "Los accidentes con tiempo perdido por cada millón de horas trabajadas", "Los días que dura cada accidente", "El costo de cada accidente", "La tasa de frecuencia compara accidentes con horas trabajadas."),
        ("abc", "En Explotación Minera: ¿qué significa cumplir una meta de ejemplo de «al menos 90 %»?", "Alcanzar o superar el 90 %", "Quedar exactamente en 90 %", "No superar el 90 %", "«Al menos» significa igual o mayor."),
        ("=", "{F} ¿Cuál es la tasa de frecuencia de la planta?", "2*1000000//500000", "Se multiplican los accidentes por 1.000.000 y se divide entre las horas trabajadas.", ""),
        ("abc", "{F} ¿Cumple la planta la meta de tasa de frecuencia (menor o igual a 5)?", "Sí, porque su tasa es 4", "No, porque su tasa no es exactamente 5", "No, porque tuvo accidentes", "La tasa es menor que la meta."),
        ("=", "{F} ¿Qué porcentaje de las personas está capacitado?", "96*100//120", "Se multiplican por 100 las personas capacitadas y se divide entre el total.", " %"),
        ("abc", "{F} ¿Cumple la planta la meta de capacitación de al menos 90 %?", "No, porque llegó al 80 %", "Sí, porque capacitó a 96 personas", "Sí, porque 80 es cercano a 90", "El 80 % queda debajo de la meta del 90 %."),
        ("=", "{F} ¿Cuántas personas más debería haber capacitado para llegar al 90 % de las 120?", "120*90//100-96", "Se calcula el 90 % de 120 y se resta lo ya capacitado.", " personas"),
        ("=", "{F} ¿Qué porcentaje de las inspecciones programadas se realizó?", "9*100//12", "Se multiplican por 100 las inspecciones realizadas y se divide entre las programadas.", " %"),
        ("=", "{F} ¿Cuántas condiciones de la resolución ambiental quedaron sin cumplir?", "8-7", "Se resta las cumplidas a las exigidas.", " condición"),
        ("abc", "{F} ¿Qué corresponde hacer con la condición ambiental no cumplida?", "Informarla y corregirla, dejando constancia", "Ocultarla hasta que la fiscalicen", "Esperar al próximo año para corregirla", "Un incumplimiento se informa y se corrige."),
        ("abc", "{F} Un encargado propone anotar 1 accidente en lugar de 2 para bajar la tasa. ¿Qué corresponde?", "Rechazarlo: se registra el valor real, porque alterar el dato es una falta grave", "Aceptarlo si el accidente fue leve", "Aceptarlo si la meta está cerca", "Un registro debe reflejar la realidad."),
        ("abc", "Una persona te cuenta que, en una planta de ejemplo, una cinta se atascó y un trabajador quedó con la mano atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar mover la cinta con las manos", "Anotar el accidente antes de avisar", "Acercarse a una máquina atascada puede provocar otro daño."),
    ],
    ctx=("abc", "Un jefe de ejemplo dice: «tuvimos tasa 4, menor que la meta de 5, así que podemos relajar la prevención». ¿Qué respondes?", "Que el indicador no autoriza a descuidar la seguridad, porque cada accidente involucra a una persona", "Que tiene razón, porque la meta ya se cumplió", "Que la meta debería ser 10 para tener más margen", "Un buen indicador no reemplaza la prevención continua."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula la tasa de frecuencia de la planilla de ejemplo?", "Accidentes por 1.000.000, divididos entre las horas trabajadas", "Compara accidentes con las horas trabajadas."),
        ("¿Cómo se calcula el porcentaje de cumplimiento de capacitación?", "Personas capacitadas por 100, divididas entre el total", "Compara las personas capacitadas con la dotación completa."),
        ("¿Qué se hace con un indicador que no cumple la meta?", "Se informa y se corrige", "El incumplimiento se informa para tomar medidas."),
    ],
    op=("Planilla ficticia de la «Minera Demo Cerro Claro»: horas trabajadas 500.000; accidentes con tiempo perdido 1; meta de tasa de frecuencia menor o igual a 4; personas capacitadas 45 de 50, con meta de al menos 85 %; inspecciones realizadas 9 de 10. Escribe (a) la tasa de frecuencia y si cumple la meta, (b) el porcentaje de capacitación y si cumple, (c) el porcentaje de inspecciones realizadas, (d) qué haces si el encargado propone alterar un dato para cumplir la meta.",
        "(a) 1 × 1.000.000 ÷ 500.000 = 2; cumple la meta de 4. (b) 45 × 100 ÷ 50 = 90 %; cumple la meta de 85 %. (c) 9 × 100 ÷ 10 = 90 %. (d) Rechazarlo y avisar: el registro debe decir el valor real.",
        ["calcula la tasa de frecuencia", "calcula la capacitación y compara", "calcula el porcentaje de inspecciones", "rechaza alterar datos"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el 1.000.000", "confundir «al menos» con «a lo más»", "alterar un dato"],
        "Pregunta: «¿el 90 % cumple una meta de al menos 85 %?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una planilla con 800.000 horas y 4 accidentes con tiempo perdido, y calcula la tasa de frecuencia.",
    extend="Explica con un ejemplo por qué no se debe alterar un dato para cumplir una meta.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 23 (caso de ejemplo, inventado). La faena ficticia «Mina Demo Cerro Pelado» produce concentrado de cobre. Su plan de muestreo de ejemplo define tres puntos: A, en la frente de la mina (roca recién extraída); B, a la salida del chancado (mineral chancado); y C, en la planta (concentrado). "
     "Matriz de peligros del muestreo: polvo (probabilidad 5 y gravedad 3), tránsito de camiones y cargadores (probabilidad 3 y gravedad 4), partes en movimiento de equipos (probabilidad 2 y gravedad 5) y caída de altura en plataformas (probabilidad 2 y gravedad 4). "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. Personal de ejemplo: 5 personas de muestreo, 3 de laboratorio y 2 de geología.")
build(
    O6, 1, F,
    use="Aprenderé qué es el muestreo de mineral, para qué sirve un plan de muestreo, qué peligros tiene el trabajo en cada punto y por qué solo personal autorizado toma muestras en equipos o zonas de riesgo.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé calcular un puntaje multiplicando dos números.", "Sé leer una tabla sencilla."],
    explain=[
        "Un muestreo es el proceso de tomar una porción pequeña de un material para conocer cómo es el total. Una muestra es esa porción; es representativa si refleja a todo el material. El plan de muestreo es el documento que define en qué puntos, con qué frecuencia y de qué tipo se toman las muestras. Los puntos están repartidos en el proceso productivo: la mina, el chancado (donde se rompe la roca) y la planta, que entrega el concentrado (un producto con más metal que la roca original). Rotular es escribir en cada muestra los datos que permiten identificarla.",
        "Los peligros del muestreo son el polvo, el tránsito de vehículos, las partes en movimiento de los equipos y la caída desde plataformas. En la matriz de ejemplo, el puntaje es probabilidad por gravedad y se atiende primero el mayor. Tomar muestras junto a equipos en movimiento, en altura o en zonas restringidas es una tarea de riesgo que solo hace personal formado y autorizado, con el permiso y los medios que la empresa defina.",
        f"Este cuaderno no enseña a tomar muestras en terreno. La autoridad minera y la norma vigente fijan las condiciones de seguridad. {EMER} {AVISO}",
    ],
    vocab=[("muestreo", "proceso de tomar una porción pequeña de un material para conocer el total"), ("muestra", "porción pequeña de un material"), ("muestra representativa", "muestra que refleja a todo el material"), ("plan de muestreo", "documento que define puntos, frecuencia y tipo de las muestras"), ("punto de muestreo", "lugar del proceso donde se toma la muestra"), ("rotular", "escribir en una muestra los datos que permiten identificarla")],
    worked=[
        ("Puntaje de riesgo", "En la matriz de ejemplo de un laboratorio, el ruido de un equipo de molienda tiene probabilidad 4 y gravedad 2. ¿Qué puntaje resulta?", ["Se multiplica la probabilidad por la gravedad.", "4 por 2 son 8."], "8 puntos"),
        ("Peligro y riesgo", "En un punto de muestreo de ejemplo hay una plataforma sin baranda. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la plataforma sin baranda.", "El riesgo es que una persona caiga de altura."], "Peligro: la plataforma sin baranda; riesgo: caída de altura"),
    ],
    mistakes=[("Creer que tomar una muestra es una tarea sencilla que cualquiera puede hacer en cualquier punto.", "Algunos puntos tienen equipos en movimiento, polvo o altura y exigen personal autorizado.", "Aprende el concepto aquí y deja la toma en terreno a personal autorizado."),
              ("Creer que una muestra tomada en el lugar más cómodo es igual de buena.", "Una muestra debe tomarse en el punto definido por el plan para que sea representativa.", "Respeta el punto y la frecuencia del plan.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un muestreo?", "El proceso de tomar una porción pequeña de un material para conocer cómo es el total", "El proceso de transportar el mineral desde la mina hasta la planta", "El proceso de pesar los camiones que salen de la faena", "El muestreo busca conocer el total a partir de una porción."),
        ("abc", "En Explotación Minera: ¿qué es una muestra representativa?", "Una muestra que refleja a todo el material", "Una muestra del mineral más valioso", "La muestra más grande que se pueda tomar", "Representativa significa que refleja el total, no que sea la más grande."),
        ("abc", "En Explotación Minera: ¿qué define un plan de muestreo?", "Los puntos, la frecuencia y el tipo de las muestras", "El precio del mineral", "El horario de los turnos de la faena", "El plan fija dónde, cuándo y qué muestras se toman."),
        ("=", "{F} ¿Cuántas personas hay en total en el equipo de la ficha?", "5+3+2", "Se suman las personas de muestreo, laboratorio y geología.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «partes en movimiento de equipos» en un punto de muestreo?", "Que una persona sufra un atrapamiento o un golpe grave", "Que el equipo se desgaste", "Que la muestra salga mal rotulada", "El riesgo es el daño a las personas, no un problema del equipo ni de la muestra."),
        ("abc", "{F} ¿Dónde se toma la muestra del punto B?", "A la salida del chancado, del mineral chancado", "En la frente de la mina, de la roca recién extraída", "En la planta, del concentrado", "El plan ubica el punto B a la salida del chancado."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el polvo?", "5*3", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el tránsito de camiones y cargadores?", "3*4", "Se multiplican la probabilidad y la gravedad de ese peligro.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál de los cuatro peligros debe atenderse primero?", "El polvo, porque tiene el mayor puntaje (15)", "Las partes en movimiento, porque su gravedad es la más alta (5)", "La caída de altura, porque ocurre en plataformas", "Se atiende primero el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Un joven en práctica dice: «sé cómo se toma una muestra, así que puedo hacerlo en la correa del chancado mientras funciona». ¿Qué es correcto?", "No: ese punto tiene equipos en movimiento y solo personal autorizado, con permiso y medios de la empresa, toma muestras", "Sí, si va con casco y guantes", "Sí, si lo hace rápido", "Los elementos de protección no reemplazan la autorización ni los medios de la empresa."),
        ("abc", "{F} ¿Por qué se debe tomar la muestra en el punto que fija el plan y no en el lugar más cómodo?", "Porque solo así la muestra representa al material del proceso", "Porque los puntos del plan son siempre los más cercanos", "Porque el laboratorio solo acepta muestras de esos puntos", "Cambiar el punto cambia lo que la muestra representa."),
        ("=", "{F} Para una capacitación, el equipo completo se reparte en grupos de 5 personas. ¿Cuántos grupos se forman?", "(5+3+2)//5", "Se suman las personas del equipo y se divide entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, ves que una persona que tomaba una muestra cae desde una plataforma y no se mueve. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Subir a la plataforma a ayudarla", "Tomar la muestra para que no se pierda", "Moverla o acercarte sin formación puede agravar el daño."),
    ],
    ctx=("abc", "Un compañero de práctica te dice: «ayúdame a sacar una muestra de la correa del chancado, solo hay que meter un balde un segundo». ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado, permiso y los medios de la empresa, y que consultarás a un adulto responsable", "Que sí, si es solo un segundo", "Que sí, si usas guantes gruesos", "Meter la mano o un balde en un equipo en movimiento es muy peligroso."),
    sc=[
        ("En Explotación Minera: ¿qué es una muestra representativa?", "Una muestra que refleja a todo el material", "Representar al total es el objetivo del muestreo."),
        ("En Explotación Minera: ¿para qué se rotula una muestra?", "Para poder identificarla con sus datos", "Sin rotulado la muestra pierde su valor."),
        ("¿Cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("La faena ficticia «Mina Demo Cerro Claro» tiene un plan de muestreo con un punto en la frente de la mina y otro en la entrada de la planta, junto a una cinta transportadora en movimiento. Escribe (a) un peligro del segundo punto y su riesgo asociado, (b) por qué la muestra debe tomarse en el punto del plan, (c) quién puede tomar muestras en un punto con equipos en movimiento, (d) qué haces si ves a alguien atrapado en la cinta.",
        "(a) Peligro: las partes en movimiento de la cinta; riesgo: que una persona sufra un atrapamiento. (b) Para que la muestra represente al material del proceso. (c) Personal formado y autorizado, con permiso y los medios que la empresa defina. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "justifica el punto del plan", "nombra quién puede tomar muestras", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que cualquier persona puede tomar la muestra", "acercarse a la cinta"],
        "Pregunta: «¿qué pasa con la muestra si cambias el punto?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un plan de muestreo con tres puntos de una faena y escribe un peligro y su riesgo para cada uno.",
    extend="Explica con un ejemplo por qué una muestra mal tomada puede llevar a una decisión equivocada.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 24 (documentos y datos de ejemplo, inventados). Plan de muestreo de la faena ficticia «Mina Demo Piedra Azul»: punto A, frente de la mina, una muestra por turno; punto B, salida del chancado, una muestra cada 2 horas; punto C, planta (concentrado), una muestra cada 4 horas. "
     "Rotulado exigido: código (punto-fecha-turno), fecha, hora, punto y responsable. Una roca ígnea se forma al enfriarse el magma o la lava; una sedimentaria, por acumulación de sedimentos; una metamórfica, por transformación de otra roca con presión y calor. "
     "Un mineral es una sustancia natural de composición química definida; la mena es el mineral que se explota por su metal, como la calcopirita para el cobre; la ganga es el material sin valor que la acompaña, como el cuarzo. La ley de un mineral es el contenido de metal, en porcentaje. Roles: el muestrero toma las muestras; el geólogo define el plan; el laboratorista analiza; el supervisor organiza.")
build(
    O6, 2, F,
    use="Aprenderé vocabulario de rocas y minerales, el contenido de un plan de muestreo, cómo se rotula una muestra y qué rol tiene cada persona.",
    prior=["Sé qué es un muestreo y un plan de muestreo.", "Sé leer una tabla sencilla.", "Sé dividir números enteros."],
    explain=[
        "Las rocas se clasifican por su origen: las ígneas se forman al enfriarse el magma o la lava, las sedimentarias por acumulación de sedimentos y las metamórficas cuando otra roca cambia por presión y calor. Un mineral es una sustancia natural de composición química definida; la mena es el mineral que se explota por su metal, como la calcopirita para el cobre, y la ganga es el material sin valor que la acompaña, como el cuarzo. La ley es el contenido de metal en porcentaje.",
        "El plan de muestreo dice en qué punto, con qué frecuencia y de qué material se toma cada muestra. Cada muestra se rotula con su código, fecha, hora, punto y responsable; el código identifica punto, fecha y turno. Una muestra sin rotular completa pierde su valor, porque nadie puede saber de dónde viene.",
        f"Cada rol tiene su límite: el muestrero toma las muestras según el plan, el geólogo define el plan, el laboratorista analiza y el supervisor organiza. Nadie cambia el plan por su cuenta. {EMER} {AVISO}",
    ],
    vocab=[("roca ígnea", "roca que se forma al enfriarse el magma o la lava"), ("roca sedimentaria", "roca que se forma por acumulación de sedimentos"), ("roca metamórfica", "roca que cambia por presión y calor"), ("mineral", "sustancia natural de composición química definida"), ("mena", "mineral que se explota por su metal"), ("ganga", "material sin valor que acompaña a la mena"), ("ley", "contenido de metal en un mineral, en porcentaje")],
    worked=[
        ("Clasificar una roca", "Una roca de ejemplo se formó al enfriarse lava de un volcán. ¿Es ígnea, sedimentaria o metamórfica?", ["Se formó al enfriarse la lava.", "Las rocas que se forman así son ígneas."], "Ígnea"),
        ("Muestras por día", "Un punto de ejemplo toma una muestra cada 3 horas durante 24 horas. ¿Cuántas muestras son?", ["Se divide el tiempo entre el intervalo.", "24 dividido entre 3 son 8 muestras."], "8 muestras"),
    ],
    mistakes=[("Confundir mena y ganga porque ambas están en la misma roca.", "La mena se explota por su metal y la ganga no tiene valor.", "Pregúntate si el mineral se explota por su metal."),
              ("Dejar sin rotular una muestra porque «se sabe de dónde viene».", "Sin rotulado nadie más puede saber su origen.", "Rotula cada muestra con los cinco datos exigidos.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una roca ígnea?", "Una roca que se forma al enfriarse el magma o la lava", "Una roca que se forma por acumulación de sedimentos", "Una roca que cambió por presión y calor", "Las ígneas se forman por enfriamiento de material fundido."),
        ("abc", "En Explotación Minera: ¿qué es la mena?", "El mineral que se explota por su metal", "El material sin valor que acompaña al mineral", "La roca donde se hace el muestreo", "La mena es lo que se explota; lo que no tiene valor es la ganga."),
        ("abc", "En Explotación Minera: ¿qué es la ley de un mineral?", "El contenido de metal, en porcentaje", "La norma que regula la explotación", "El peso total de la muestra", "La ley es la proporción de metal en el mineral."),
        ("=", "{F} ¿Cuántas muestras por día se toman en el punto B?", "24//2", "Se divide el tiempo del día entre el intervalo entre muestras.", " muestras"),
        ("=", "{F} ¿Cuántas muestras por día se toman en el punto C?", "24//4", "Se divide el tiempo del día entre el intervalo entre muestras.", " muestras"),
        ("abc", "{F} ¿Cuál de estos materiales es mena de cobre según la ficha?", "La calcopirita", "El cuarzo", "La ganga", "La ficha indica la calcopirita como mena y el cuarzo como ganga."),
        ("abc", "{F} Una roca se forma cuando otra roca cambia por presión y calor. ¿De qué tipo es?", "Metamórfica", "Ígnea", "Sedimentaria", "El cambio por presión y calor define a las metamórficas."),
        ("abc", "{F} ¿Qué datos exige la ficha para rotular cada muestra?", "Código, fecha, hora, punto y responsable", "Solo el nombre del muestrero", "El precio y el peso", "El rotulado exigido por el plan incluye cinco datos."),
        ("abc", "{F} Un código dice «B-0412-T2». ¿Qué información entrega, según la ficha?", "Punto B, fecha 0412 y turno 2", "Punto B, hora 04:12 y 2 muestras", "Punto B, 412 gramos y turno 2", "El código sigue la forma punto, fecha y turno."),
        ("abc", "{F} ¿Quién define el plan de muestreo?", "El geólogo", "El muestrero", "El laboratorista", "El geólogo define el plan y el muestrero lo aplica."),
        ("abc", "{F} Un muestrero propone tomar la muestra del punto A en la bodega porque «queda más cerca». ¿Qué corresponde?", "No hacerlo: la muestra debe tomarse en el punto que fija el plan para ser representativa", "Hacerlo si el material es parecido", "Hacerlo si ahorra tiempo", "Cambiar el punto cambia lo que la muestra representa."),
        ("=", "{F} En 5 días completos, ¿cuántas muestras se toman en total entre los puntos B y C?", "5*(24//2+24//4)", "Se calculan las muestras por día de B y C y se multiplican por 5 días.", " muestras"),
        ("abc", "Una persona te cuenta que, en un punto de muestreo de ejemplo, el material se desplomó sobre un muestrero que quedó atrapado. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Excavar tú para liberarlo", "Esperar a que termine el turno para avisar", "Un desplome puede repetirse; lo correcto es avisar y no acercarse."),
    ],
    ctx=("abc", "Un asistente de ejemplo encuentra una bolsa de muestra sin código, sin fecha y sin punto, y dice: «la mando igual al laboratorio, seguro es del turno de hoy». ¿Qué respondes?", "Que no se puede enviar sin rotular, porque nadie sabría de dónde viene, y que debe avisar al supervisor", "Que sí, porque se nota que es del turno", "Que sí, y que el laboratorista adivine el punto", "Una muestra sin rotulado completo pierde su valor."),
    sc=[
        ("En Explotación Minera: ¿qué es la ganga?", "El material sin valor que acompaña a la mena", "La ganga no se explota por su metal."),
        ("En Explotación Minera: ¿qué datos lleva el rotulado de una muestra?", "Código, fecha, hora, punto y responsable", "Son los datos que permiten identificar la muestra."),
        ("En Explotación Minera: ¿qué rol define el plan de muestreo?", "El geólogo", "El muestrero solo aplica el plan definido."),
    ],
    op=("Plan ficticio de la faena «Mina Demo Cerro Claro»: punto 1, salida del chancado, una muestra cada 4 horas; punto 2, planta, una muestra cada 8 horas. Se rotula con código (punto-fecha-turno), fecha, hora, punto y responsable. Escribe (a) cuántas muestras por día se toman en cada punto, (b) un ejemplo de código para el punto 2 del turno 1 de una fecha inventada, (c) qué datos faltan en una bolsa que dice código 2-0611-T1, fecha 0611, punto 2, sin hora y sin responsable, (d) quién define el plan y quién lo aplica.",
        "(a) Punto 1: 24 ÷ 4 = 6 muestras; punto 2: 24 ÷ 8 = 3 muestras. (b) 2-0611-T1. (c) Faltan la hora y el responsable. (d) El geólogo define el plan y el muestrero lo aplica.",
        ["calcula las muestras por día", "arma un código con la forma exigida", "detecta los datos faltantes", "asigna los roles"],
        ["hoja con las cuatro respuestas"],
        ["confundir punto con fecha en el código", "olvidar la hora o el responsable", "creer que el muestrero define el plan"],
        "Pregunta: «¿qué cinco datos pide el rotulado?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa tres códigos de muestras con la forma punto-fecha-turno y explica qué dice cada uno.",
    extend="Explica con un ejemplo por qué una muestra sin rotular completa no sirve aunque el material sea bueno.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 25 (caso de ejemplo, inventado). Planilla de recepción de muestras en el laboratorio de la faena ficticia «Mina Demo Lomas Bajas». El plan tiene solo los puntos A, B y C. Cada muestra debe traer código, fecha, hora, punto y responsable, y el código debe coincidir con la fecha y el punto. "
     "M1: código A-0310-T1, fecha 0310, hora 08:00, punto A, responsable R. Soto. M2: código B-0310-T1, fecha 0310, sin hora, punto B, responsable M. Rojas. M3: código C-0310-T1, fecha 0310, hora 12:00, punto C, sin responsable. "
     "M4: código A-0311-T2, fecha 0310, hora 16:00, punto A, responsable R. Soto. M5: código B-0311-T2, fecha 0311, hora 18:00, punto B, responsable M. Rojas. M6: código D-0311-T2, fecha 0311, hora 20:00, punto D, responsable L. Pino. "
     "M7: código A-0312-T1, fecha 0312, hora 06:30, punto A, responsable R. Soto. M8: código C-0311-T2, fecha 0311, hora 23:30, punto C, responsable M. Rojas. Regla de ejemplo: una muestra con rotulado incompleto o incoherente no se analiza hasta que su responsable lo aclare; el laboratorista no completa ni corrige los datos.")
build(
    O6, 3, F,
    use="Aprenderé a revisar en papel una planilla de recepción de muestras: detectar rotulados incompletos o incoherentes, calcular porcentajes y decidir qué se hace con cada muestra.",
    prior=["Sé qué datos lleva el rotulado.", "Sé qué es un plan de muestreo.", "Sé calcular un porcentaje."],
    explain=[
        "Al recibir muestras, el laboratorio revisa cada rotulado. Una muestra está incompleta si le falta uno de los cinco datos, e incoherente si los datos se contradicen, por ejemplo si el código dice una fecha y la columna fecha dice otra, o si el punto no existe en el plan. Una muestra incompleta o incoherente no se analiza porque su resultado no se podría atribuir con seguridad a un lugar y un momento.",
        "La regla es devolverla al responsable de la muestra para que lo aclare; nadie completa ni corrige los datos de otra persona, y nunca se adivina. El porcentaje de muestras aceptables es las aceptables por 100 divididas entre el total recibido, y un porcentaje bajo es una señal de que hay que reforzar el rotulado.",
        f"Este análisis es de papel: la toma de muestras y el análisis real corresponden a personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("rotulado incompleto", "muestra a la que le falta uno de los datos exigidos"), ("rotulado incoherente", "muestra cuyos datos se contradicen entre sí o con el plan"), ("muestra aceptable", "muestra con rotulado completo y coherente"), ("devolver una muestra", "enviarla al responsable para que aclare el rotulado")],
    worked=[
        ("Detectar una incoherencia", "Una muestra de ejemplo tiene código C-0512-T1 pero la columna fecha dice 0513. ¿Está bien rotulada?", ["El código indica fecha 0512 y la columna indica 0513.", "Los datos se contradicen: es incoherente."], "No: es incoherente"),
        ("Porcentaje de aceptables", "De 10 muestras de ejemplo, 7 son aceptables. ¿Qué porcentaje es?", ["Se multiplican por 100 las aceptables y se divide entre el total.", "7 por 100 dividido entre 10 son 70."], "70 %"),
    ],
    mistakes=[("Completar tú la hora que falta porque «era más o menos a esa hora».", "Adivinar un dato falsea el registro.", "Devuelve la muestra al responsable para que lo aclare."),
              ("Aceptar una muestra de un punto que no está en el plan porque «el mineral parece igual».", "Un punto que no está en el plan no se puede interpretar.", "Se devuelve y se informa al supervisor.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un rotulado incompleto?", "Una muestra a la que le falta uno de los datos exigidos", "Una muestra con demasiados datos", "Una muestra de un punto lejano", "Incompleto significa que falta algún dato."),
        ("abc", "En Explotación Minera: ¿qué es un rotulado incoherente?", "Uno cuyos datos se contradicen entre sí o con el plan", "Uno que tiene todos los datos", "Uno escrito a mano", "Incoherente significa que los datos no concuerdan."),
        ("abc", "En Explotación Minera: ¿qué se hace con una muestra con rotulado incompleto?", "Se devuelve a su responsable y no se analiza hasta que lo aclare", "Se analiza igual y se anota el dato probable", "Se descarta sin avisar a nadie", "Un dato adivinado falsea el registro."),
        ("abc", "{F} ¿Qué dato falta en la muestra M2?", "La hora", "El responsable", "El punto", "M2 tiene código, fecha, punto y responsable, pero no hora."),
        ("abc", "{F} ¿Qué dato falta en la muestra M3?", "El responsable", "La hora", "La fecha", "M3 tiene código, fecha, hora y punto, pero no responsable."),
        ("abc", "{F} ¿Cuál es la incoherencia de la muestra M4?", "El código indica fecha 0311 y la columna fecha dice 0310", "La hora no corresponde al turno", "El punto A no existe en el plan", "Código y fecha deben coincidir; en M4 no coinciden."),
        ("abc", "{F} ¿Cuál es el problema de la muestra M6?", "El punto D no existe en el plan", "Le falta la hora", "No tiene responsable", "El plan solo tiene los puntos A, B y C."),
        ("=", "{F} ¿Cuántas de las ocho muestras están completas y coherentes (M1, M5, M7 y M8)?", "8-4", "Se restan al total las cuatro muestras con problemas (M2, M3, M4 y M6).", " muestras"),
        ("=", "{F} ¿Qué porcentaje de las muestras recibidas es aceptable?", "4*100//8", "Se multiplican por 100 las aceptables y se divide entre el total.", " %"),
        ("abc", "{F} Un laboratorista propone anotar la hora de M2 como «aprox. 10:00» para poder analizarla. ¿Qué corresponde?", "No hacerlo: se devuelve la muestra a su responsable para que aclare la hora", "Hacerlo si la hora es razonable", "Hacerlo si el supervisor lo comenta por pasillo", "Adivinar un dato falsea el registro."),
        ("abc", "{F} ¿Qué se informa respecto de la muestra M6?", "Que corresponde a un punto que no está en el plan, para que el supervisor aclare con su responsable", "Que se analizará como si fuera del punto C", "Que se descartará sin avisar", "Una muestra de un punto fuera del plan debe aclararse con quien la tomó."),
        ("=", "{F} Si las 4 muestras con problemas se aclaran y se aceptan, ¿cuántas muestras aceptables habría en total?", "4+4", "Se suman las muestras ya aceptables y las que se aclararían.", " muestras"),
        ("abc", "Una persona te cuenta que, en un punto de muestreo de ejemplo, un equipo se prendió fuego y hay trabajadores cerca. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apagar el fuego con lo que haya", "Esperar a ver si se apaga solo", "Un incendio exige personal formado; lo tuyo es avisar."),
    ],
    ctx=("abc", "Una compañera de laboratorio de ejemplo ve una muestra sin responsable y dice: «yo sé de quién es, le pongo su nombre y la mandamos a analizar». ¿Qué respondes?", "Que no: la muestra se devuelve al responsable para que lo aclare, porque nadie completa datos de otra persona", "Que sí, porque se nota que es suya", "Que sí, si se anota después", "Completar datos ajenos es una falta en el registro."),
    sc=[
        ("En Explotación Minera: ¿cuándo es incoherente el rotulado de una muestra?", "Cuando sus datos se contradicen entre sí o con el plan", "Por ejemplo, un código con una fecha distinta de la columna fecha."),
        ("¿Qué se hace con una muestra incompleta o incoherente?", "Se devuelve al responsable para que la aclare", "Nadie completa ni corrige datos de otra persona."),
        ("¿Cómo se calcula el porcentaje de muestras aceptables?", "Aceptables por 100, divididas entre el total", "El porcentaje compara las aceptables con las recibidas."),
    ],
    op=("Planilla ficticia de la «Mina Demo Cerro Claro»: el plan tiene los puntos 1 y 2. M1: código 1-0705-T1, fecha 0705, hora 09:00, punto 1, responsable P. Díaz. M2: código 2-0705-T1, fecha 0705, hora 13:00, punto 2, sin responsable. M3: código 1-0706-T2, fecha 0705, hora 17:00, punto 1, responsable P. Díaz. M4: código 3-0706-T2, fecha 0706, hora 19:00, punto 3, responsable A. Vera. Escribe (a) qué problema tiene cada muestra, (b) qué porcentaje de las 4 es aceptable, (c) qué se hace con cada muestra con problema, (d) qué no puede hacer el laboratorista.",
        "(a) M1 está bien; M2 no tiene responsable; M3 tiene fecha del código distinta de la columna; M4 es de un punto que no está en el plan. (b) 1 × 100 ÷ 4 = 25 %. (c) Se devuelven a sus responsables para que lo aclaren y no se analizan. (d) No puede completar ni corregir los datos ni adivinarlos.",
        ["detecta los problemas", "calcula el porcentaje", "describe qué hacer con las muestras con problemas", "aplica la regla de no corregir datos ajenos"],
        ["hoja con las cuatro respuestas"],
        ["aceptar una muestra incoherente", "dividir entre un número distinto de 4", "corregir datos ajenos"],
        "Pregunta: «¿qué dato contradice a qué dato en M3?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una planilla de 5 muestras con una incompleta y una incoherente, y calcula el porcentaje aceptable.",
    extend="Explica con un ejemplo cómo una muestra mal rotulada puede llevar a una decisión equivocada en la faena.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 26 (planilla de ejemplo, inventada). Lotes de mineral de la faena ficticia «Mina Demo Río Hondo» con la ley de cobre de ejemplo obtenida de sus muestras. Lote 1: 200 toneladas con ley de 1 %. Lote 2: 100 toneladas con ley de 4 %. "
     "Fórmula de ejemplo: cobre fino (en toneladas) = toneladas del lote × ley ÷ 100. La ley promedio de varios lotes es el cobre fino total por 100 dividido entre las toneladas totales. "
     "Muestreo: una muestra cada 2 horas durante las 24 horas del día; cada muestra pesa 2 kg; el análisis cuesta $5.000 por muestra (valor de ejemplo). Mes de ejemplo: 30 días.")
build(
    O6, 4, F,
    use="Aprenderé a calcular en una planilla el cobre fino de un lote, la ley promedio de varios lotes, las muestras por día y por mes, su peso y su costo de análisis.",
    prior=["Sé qué es la ley de un mineral.", "Sé calcular un porcentaje.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La ley es el porcentaje de metal que contiene el mineral. El cobre fino de un lote es la cantidad de cobre que realmente contiene: toneladas del lote multiplicadas por la ley y divididas entre 100. Si un lote de 100 toneladas tiene una ley de 2 %, contiene 2 toneladas de cobre fino. Los lotes con distinta ley no se promedian simplemente: la ley promedio se calcula sumando el cobre fino de todos los lotes, multiplicando por 100 y dividiendo entre las toneladas totales.",
        "El muestreo se planifica con frecuencia: si se toma una muestra cada 2 horas, en un día de 24 horas son 12 muestras. Multiplicando por el peso de cada muestra se obtiene el peso total, y multiplicando por el precio del análisis se obtiene el costo. Estos valores son de ejemplo; los reales los define el plan y la norma vigente.",
        f"Estos cálculos son de planilla: ningún número de este cuaderno reemplaza un análisis de laboratorio real. {EMER} {AVISO}",
    ],
    vocab=[("cobre fino", "cantidad real de cobre que contiene un lote"), ("ley promedio", "ley de varios lotes juntos: cobre fino total por 100, dividido entre las toneladas totales"), ("lote", "cantidad de mineral que se trata como una unidad"), ("frecuencia de muestreo", "cada cuánto tiempo se toma una muestra"), ("tonelada", "unidad de peso que equivale a 1.000 kg")],
    worked=[
        ("Cobre fino de un lote", "Un lote de ejemplo de 500 toneladas tiene una ley de 3 %. ¿Cuántas toneladas de cobre fino contiene?", ["Se multiplican las toneladas por la ley y se divide entre 100.", "500 por 3 son 1.500, y 1.500 dividido entre 100 son 15."], "15 toneladas"),
        ("Ley promedio", "Dos lotes de ejemplo: 200 t con 2 % y 100 t con 5 %. ¿Cuál es la ley promedio?", ["El cobre fino es 4 más 5, es decir, 9 t.", "9 por 100 dividido entre 300 son 3 %."], "3 %"),
    ],
    mistakes=[("Promediar las leyes sin considerar las toneladas de cada lote.", "Un lote grande pesa más en el promedio que uno pequeño.", "Calcula el cobre fino de cada lote y divide el total entre las toneladas totales."),
              ("Olvidar dividir entre 100 al calcular el cobre fino.", "La ley está en porcentaje.", "Multiplica por la ley y divide entre 100.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el cobre fino de un lote?", "La cantidad real de cobre que contiene el lote", "El peso total del lote", "El precio del cobre en el mercado", "El cobre fino es el cobre contenido, no el peso del lote."),
        ("abc", "En Explotación Minera: ¿cómo se calcula el cobre fino de un lote?", "Toneladas por ley, divididas entre 100", "Toneladas más ley", "Ley dividida entre las toneladas", "La ley es un porcentaje, por eso se divide entre 100."),
        ("abc", "En Explotación Minera: ¿qué es la frecuencia de muestreo?", "Cada cuánto tiempo se toma una muestra", "El peso de cada muestra", "El número de laboratorios que analizan", "La frecuencia indica el intervalo entre muestras."),
        ("=", "{F} ¿Cuántas toneladas de cobre fino tiene el lote 1?", "200*1//100", "Se multiplican las toneladas por la ley y se divide entre 100.", " t"),
        ("=", "{F} ¿Cuántas toneladas de cobre fino tiene el lote 2?", "100*4//100", "Se multiplican las toneladas por la ley y se divide entre 100.", " t"),
        ("=", "{F} ¿Cuántas toneladas de cobre fino tienen los dos lotes juntos?", "200*1//100+100*4//100", "Se suma el cobre fino de cada lote.", " t"),
        ("=", "{F} ¿Cuántas toneladas de mineral hay en total entre los dos lotes?", "200+100", "Se suman las toneladas de cada lote.", " t"),
        ("=", "{F} ¿Cuál es la ley promedio de los dos lotes, en porcentaje?", "(200*1//100+100*4//100)*100//(200+100)", "Se divide el cobre fino total por 100 entre las toneladas totales.", " %"),
        ("abc", "{F} Un asistente dice que la ley promedio es 2,5 % porque «(1 + 4) ÷ 2». ¿Qué respondes?", "Que el promedio debe considerar las toneladas: el lote 1 es el doble de grande, por eso la ley promedio es 2 %", "Que está correcto, porque se promedian las dos leyes", "Que es 5 % porque se suman las leyes", "Un lote más grande pesa más en el promedio."),
        ("=", "{F} ¿Cuántas muestras se toman por día?", "24//2", "Se divide el tiempo del día entre el intervalo de muestreo.", " muestras"),
        ("=", "{F} ¿Cuántos kilogramos de muestra se toman en un día?", "24//2*2", "Se multiplican las muestras del día por el peso de cada una.", " kg"),
        ("=", "{F} ¿Cuántos pesos cuesta el análisis de todas las muestras del mes de 30 días?", "24//2*30*5000", "Se multiplican las muestras por día, los días y el precio de cada análisis.", " pesos"),
        ("abc", "Una persona te cuenta que, en un acopio de ejemplo, un camión retrocedió y dejó a un muestrero atrapado contra un montón. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a mover el camión", "Tomar una muestra del montón para el informe", "Acercarse a un vehículo en movimiento puede provocar otro accidente."),
    ],
    ctx=("abc", "Un jefe de ejemplo promedia dos lotes, uno de 800 t con 1 % y otro de 200 t con 6 %, y anuncia «ley promedio 3,5 %». ¿Qué respondes?", "Que debe ponderar por toneladas: el cobre fino es 8 más 12, es decir, 20 t, y la ley promedio es 20 × 100 ÷ 1.000 = 2 %", "Que está correcto, porque (1 + 6) ÷ 2 son 3,5", "Que es 6 % porque domina el lote de mayor ley", "Se pondera por toneladas porque un lote grande influye más."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula la ley promedio de varios lotes?", "Cobre fino total por 100, dividido entre las toneladas totales", "Se considera cuánto pesa cada lote."),
        ("¿Cuántas toneladas de cobre fino tiene un lote de 100 t con 1 % de ley?", "1 tonelada", "100 por 1 dividido entre 100 es 1."),
        ("¿Cuántas muestras por día se toman si se toma una cada 3 horas?", "8 muestras", "Se divide el tiempo del día entre el intervalo de muestreo."),
    ],
    op=("Planilla ficticia de la faena «Mina Demo Cerro Claro»: lote A de 300 toneladas con ley de 2 %, lote B de 100 toneladas con ley de 6 % y una muestra cada 4 horas, de 3 kg cada una, con análisis de $6.000 por muestra durante 30 días. Escribe (a) el cobre fino de cada lote, (b) la ley promedio de los dos lotes, (c) las muestras por día y por mes, (d) el costo mensual del análisis.",
        "(a) A: 300 × 2 ÷ 100 = 6 t; B: 100 × 6 ÷ 100 = 6 t. (b) (6 + 6) × 100 ÷ 400 = 3 %. (c) 24 ÷ 4 = 6 muestras por día y 6 × 30 = 180 por mes. (d) 180 × 6.000 = $1.080.000.",
        ["calcula el cobre fino", "calcula la ley promedio ponderada", "calcula las muestras", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["promediar las leyes sin ponderar", "olvidar dividir entre 100", "no multiplicar por los 30 días"],
        "Pregunta: «¿cuánto pesa cada lote en el promedio?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa dos lotes con toneladas y leyes distintas y calcula su ley promedio ponderada.",
    extend="Explica con un ejemplo por qué promediar solo las leyes puede dar una cifra engañosa.",
)

"""Química Industrial, mención Planta Química (4.º medio TP): OAM-01 (equipos de producción: solo lectura de documentos, monitoreo en papel y cálculos de balance), OAM-02 (muestras de productos intermedios o finales) y OAM-03 (verificar equipos y pérdidas operacionales). Todo en papel, con datos de ejemplo; no enseña a operar, ajustar, mantener ni calibrar equipos."""
from __future__ import annotations

from tp_qupl_common import AVISO, EMER, build, em

O1 = "TP-QUPL-4-OAM-01"
O2 = "TP-QUPL-4-OAM-02"
O3 = "TP-QUPL-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La planta ficticia «Química Demo Valle Claro» produce el «Producto Z de ejemplo». Orden de producción OP-310: lote Z-310, cantidad objetivo de 2.000 kg en 4 turnos de igual producción. "
     "Parámetros del reactor R-1 con límites de ejemplo: temperatura de 40 a 80 °C; presión de 100 a 200 kPa; caudal de alimentación de 50 a 70 L/min. Lecturas de las 08:00: temperatura 60 °C, presión 150 kPa y caudal 60 L/min. "
     "Peligros anotados: superficies calientes, partes en movimiento y presión en tuberías. Matriz de ejemplo: puntaje = probabilidad × gravedad. Superficies calientes: probabilidad 3 y gravedad 3. Partes en movimiento: probabilidad 2 y gravedad 5. Presión en tuberías: probabilidad 2 y gravedad 4. "
     "Roles de ejemplo: el operador autorizado opera según la instrucción; el jefe de turno autoriza y recibe los avisos; el supervisor aprueba cambios; el prevencionista revisa la seguridad.")
build(
    O1, 1, F,
    use="Aprenderé qué es una planta química, qué es una instrucción de producción y por qué se monitorean los instrumentos, y entenderé que operar y ajustar equipos lo hace solo personal formado y autorizado: este cuaderno no enseña a operarlos.",
    prior=["Sé qué es una variable, un límite y un indicador.", "Sé calcular el puntaje de riesgo.", "Sé dividir y restar números enteros."],
    explain=[
        "En Química Industrial, una planta química es una instalación donde se transforman materias primas en productos mediante equipos como reactores, bombas y tanques. La instrucción de producción es el documento que indica qué producir, cuánto, con qué parámetros y en qué orden. Monitorear es observar los instrumentos de medición y registrar sus lecturas para comprobar que los parámetros, como temperatura, presión y caudal, estén dentro de sus límites.",
        "Cuando una lectura se acerca a un límite o a una alarma, el operador autorizado lo informa al jefe de turno y actúa solo según la instrucción de producción y su autorización. Ajustar un parámetro de un equipo no es una decisión personal: se hace según el procedimiento, con formación y con aviso. Los peligros se priorizan con la matriz de ejemplo: probabilidad por gravedad.",
        f"Este cuaderno solo lee documentos y calcula en papel. Operar o ajustar equipos de planta exige instructor autorizado, formación y elementos de protección. {EMER} {AVISO}",
    ],
    vocab=[("planta química", "instalación donde se transforman materias primas en productos con equipos"), ("instrucción de producción", "documento que indica qué producir, cuánto y con qué parámetros"), ("monitorear", "observar los instrumentos y registrar las lecturas"), ("parámetro", "variable del proceso con un valor y un límite, como la temperatura"), ("operador autorizado", "persona formada y autorizada para operar los equipos"), ("jefe de turno", "persona que autoriza y recibe los avisos durante el turno")],
    worked=[
        ("Producción por turno", "Una orden de ejemplo pide 900 kg en 3 turnos de igual producción. ¿Cuántos kg corresponden a cada turno?", ["Se divide la cantidad entre los turnos.", "900 entre 3 son 300."], "300 kg por turno"),
        ("Margen al límite", "Una presión de ejemplo marca 120 kPa y el límite máximo es 160 kPa. ¿Cuánto falta para el límite?", ["Se resta la lectura al límite máximo.", "160 menos 120 son 40."], "40 kPa"),
    ],
    mistakes=[("Creer que quien conoce los parámetros de la instrucción puede ajustar el equipo.", "Ajustar exige formación, autorización y aviso al jefe de turno.", "Usa la instrucción para entender el proceso y pide autorización para operar."),
              ("Anotar solo las lecturas «normales» y omitir las que se acercan al límite.", "Las lecturas cercanas al límite son las más importantes para prevenir problemas.", "Registra todas las lecturas y avisa las que se acercan al límite.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una instrucción de producción?", "Un documento que indica qué producir, cuánto y con qué parámetros", "Una factura de las materias primas", "Un plano del terreno de la planta", "La instrucción guía la producción con valores definidos."),
        ("abc", "En Química Industrial: ¿qué significa monitorear un proceso?", "Observar los instrumentos y registrar las lecturas", "Cambiar los parámetros cada hora", "Apagar los equipos para revisarlos", "Monitorear consiste en observar los instrumentos y registrar."),
        ("abc", "En Química Industrial: ¿quién opera los equipos de una planta?", "El operador autorizado, con formación", "Cualquier persona que haya leído la instrucción", "El cliente que visita la planta", "Operar equipos exige formación y autorización del personal."),
        ("=", "{F} ¿Cuántos kg debe producir cada turno para cumplir la orden OP-310?", "2000//4", "Se divide la cantidad objetivo entre los 4 turnos.", " kg"),
        ("=", "{F} ¿Cuántos °C faltan para que la temperatura de las 08:00 llegue al límite máximo?", "80-60", "Se resta la lectura al límite máximo.", " °C"),
        ("=", "{F} ¿Cuántos kPa faltan para el límite máximo de presión de las 08:00?", "200-150", "Se resta la lectura al límite máximo.", " kPa"),
        ("abc", "{F} ¿Está el caudal de las 08:00 dentro del límite?", "Sí, porque 60 está entre 50 y 70", "No, porque 60 es menor que 70", "No, porque 60 es mayor que 50", "Estar dentro del límite exige estar entre el mínimo y el máximo."),
        ("abc", "{F} Según la matriz, ¿qué peligro tiene el mayor puntaje de riesgo?", "Partes en movimiento, con 10 puntos", "Superficies calientes, con 9 puntos", "Presión en tuberías, con 8 puntos", "Se comparan probabilidad por gravedad de cada peligro."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la presión en tuberías?", "2*4", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("=", "{F} Con el caudal de las 08:00, ¿cuántos litros ingresan al reactor en 60 minutos?", "60*60", "Se multiplica el caudal por los minutos.", " L"),
        ("abc", "{F} La temperatura de R-1 sube cerca de 75 °C. Un estudiante propone «bajar un poco la válvula» para ayudar. ¿Qué corresponde?", "No hacerlo: informar al jefe de turno, porque el ajuste lo hace solo el operador autorizado", "Hacerlo, si la válvula está a mano", "Hacerlo, si solo mueve un poco", "Ajustar equipos exige formación, autorización y aviso."),
        ("abc", "{F} ¿A quién informa el operador autorizado cuando una lectura se acerca a un límite?", "Al jefe de turno", "Al cliente", "Al proveedor", "Según los roles, el jefe de turno recibe los avisos."),
        em("Lees la orden de producción de ejemplo en la sala de control cuando alguien avisa que el reactor R-1 vibra de forma anormal y que sale vapor de una brida.", 0),
    ],
    ctx=("abc", "Un compañero de ejemplo te dice: «Entra a la sala de control y sube la temperatura de R-1 a 70 °C, que ya viste la instrucción». No tienes autorización. ¿Qué respondes?", "Que no, porque operar y ajustar equipos exige formación y autorización, y que avisarás a un adulto responsable", "Que sí, si el límite es 80 °C", "Que sí, si lo anotas después", "Leer la instrucción no habilita para ajustar un equipo."),
    sc=[
        ("En Química Industrial: ¿qué es un parámetro del proceso?", "Una variable con un valor y un límite, como la temperatura", "Los parámetros se miden y se mantienen dentro de límites."),
        ("En Química Industrial: ¿qué se hace cuando una lectura se acerca al límite?", "Se informa al jefe de turno", "El aviso permite que se tome una decisión autorizada."),
        ("¿Quién ajusta los parámetros de un equipo de planta?", "El operador autorizado según la instrucción", "El ajuste exige formación y autorización."),
    ],
    op=("Orden ficticia de «Química Demo Costa Norte»: producir 1.200 kg del «Producto Y de ejemplo» en 3 turnos iguales; temperatura de 30 a 70 °C (lectura de las 08:00: 50 °C); presión de 80 a 120 kPa (lectura: 110 kPa). Peligro: superficie caliente, probabilidad 3 y gravedad 4. Escribe (a) los kg por turno, (b) los márgenes de temperatura y de presión al límite máximo, (c) el puntaje del peligro, (d) qué debe hacer un estudiante si la presión sube cerca del límite.",
        "(a) 1.200 entre 3 son 400 kg. (b) Temperatura: 20 °C; presión: 10 kPa. (c) 3 por 4 son 12 puntos. (d) No acercarse ni ajustar nada, avisar al jefe de turno o a un adulto responsable.",
        ["calcula los kg por turno", "calcula los márgenes", "calcula el puntaje", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["no dividir entre los turnos", "restar mal el margen", "ajustar sin autorización"],
        "Pregunta: «¿quién puede ajustar y a quién se informa?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una orden de producción con cantidad, turnos y un parámetro con límites, y calcula producción por turno y margen al límite.",
    extend="Explica con un ejemplo por qué un operador informa al jefe de turno antes de ajustar un parámetro.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Diagrama de bloques de la planta ficticia «Química Demo Valle Claro»: recepción de materias primas → tanque T-1 → reactor R-1 → separador S-1 → envasado. "
     "Instrumentos de ejemplo: TI-101 (indicador de temperatura de R-1), PI-102 (indicador de presión de R-1), FI-103 (indicador de caudal de entrada a R-1) y LI-104 (indicador de nivel de T-1). "
     "Convención de ejemplo: la primera letra indica la variable (T temperatura, P presión, F caudal, L nivel) y la segunda letra I indica «indicador». Consigna (valor deseado) de la temperatura de R-1: 60 °C; alarma alta: 75 °C; límite máximo: 80 °C. "
     "Lecturas actuales: TI-101: 64 °C; PI-102: 150 kPa; FI-103: 55 L/min; LI-104: 70 %. Entrega de turno: documento en que el turno saliente informa al entrante el estado de los equipos y las novedades.")
build(
    O1, 2, F,
    use="Aprenderé a leer un diagrama de bloques y los nombres de los instrumentos, y qué son la consigna, la alarma, la bitácora y la entrega de turno, como documentos de la operación de una planta.",
    prior=["Sé qué es un parámetro y un límite.", "Sé qué es un registro.", "Sé restar números enteros."],
    explain=[
        "En Química Industrial, un diagrama de bloques muestra con cajas y flechas las etapas del proceso en orden. Los instrumentos tienen un código, llamado tag, que dice qué miden: en la convención de ejemplo, TI-101 es un indicador de temperatura. La consigna es el valor deseado de un parámetro; la alarma avisa que una lectura se acerca a un límite, y el límite es el valor máximo o mínimo aceptable.",
        "La bitácora de turno es el registro de lo ocurrido: lecturas, novedades y avisos. La entrega de turno es el documento y la conversación en que el turno saliente informa al entrante el estado de los equipos y lo pendiente, para que no se pierda ninguna novedad. La desviación es la diferencia entre la lectura y la consigna.",
        f"Esta clase es de lectura de documentos en papel; operar y ajustar equipos corresponde a personal formado. {EMER} {AVISO}",
    ],
    vocab=[("diagrama de bloques", "dibujo con cajas y flechas que muestra las etapas del proceso"), ("tag de instrumento", "código que indica qué mide el instrumento"), ("consigna", "valor deseado de un parámetro"), ("alarma", "aviso de que una lectura se acerca a un límite"), ("bitácora de turno", "registro de lecturas, novedades y avisos del turno"), ("entrega de turno", "informe del turno saliente al entrante sobre el estado de los equipos"), ("desviación", "diferencia entre la lectura y la consigna")],
    worked=[
        ("Leer un tag", "En la convención de ejemplo, ¿qué mide el instrumento PI-205?", ["La primera letra P indica presión.", "La segunda letra I indica que es un indicador."], "Un indicador de presión"),
        ("Desviación", "La consigna de una temperatura de ejemplo es 50 °C y la lectura es 54 °C. ¿Cuál es la desviación?", ["Se resta la consigna a la lectura.", "54 menos 50 son 4."], "4 °C"),
    ],
    mistakes=[("Leer el tag FI-103 como «indicador de nivel».", "La primera letra F indica caudal; el nivel es la letra L.", "Lee la primera letra como la variable y la segunda como el tipo de instrumento."),
              ("Hacer la entrega de turno solo de palabra, sin registro.", "Lo que no se escribe se olvida y las novedades se pierden.", "Escribe las novedades en la bitácora y úsala en la entrega de turno.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la consigna de un parámetro?", "El valor deseado del parámetro", "El límite máximo permitido", "La alarma más alta", "La consigna es el valor al que se quiere mantener el parámetro."),
        ("abc", "En Química Industrial: ¿para qué sirve la entrega de turno?", "Para que el turno entrante conozca el estado de los equipos y las novedades", "Para cambiar los límites del proceso", "Para reemplazar la bitácora", "La entrega evita que se pierdan novedades entre turnos."),
        ("abc", "En Química Industrial: ¿qué es un diagrama de bloques?", "Un dibujo con cajas y flechas que muestra las etapas del proceso", "Una lista de personas del turno", "Una factura de insumos", "El diagrama de bloques muestra el orden de las etapas."),
        ("abc", "{F} ¿Qué mide el instrumento FI-103?", "El caudal de entrada a R-1", "El nivel de T-1", "La presión de R-1", "La primera letra F de la convención indica caudal."),
        ("abc", "{F} ¿Qué mide LI-104?", "El nivel de T-1", "La temperatura de R-1", "El caudal de entrada", "La primera letra L de la convención indica nivel."),
        ("=", "{F} ¿Cuál es la desviación de la temperatura respecto de la consigna?", "64-60", "Se resta la consigna a la lectura de TI-101.", " °C"),
        ("=", "{F} ¿Cuántos °C faltan para que la lectura llegue a la alarma alta?", "75-64", "Se resta la lectura a la alarma alta.", " °C"),
        ("=", "{F} ¿Cuántos °C hay entre la alarma alta y el límite máximo?", "80-75", "Se resta la alarma alta al límite máximo.", " °C"),
        ("=", "{F} Con el caudal de FI-103, ¿cuántos litros ingresan a R-1 en 20 minutos?", "55*20", "Se multiplica el caudal por los minutos.", " L"),
        ("abc", "{F} ¿Qué etapa del diagrama viene justo después del reactor R-1?", "El separador S-1", "El tanque T-1", "El envasado", "El diagrama ordena: R-1 y luego S-1."),
        ("abc", "{F} Un turno saliente dice «todo normal» sin escribir que la temperatura estaba subiendo. ¿Qué corresponde?", "Escribir la novedad en la bitácora y comentarla en la entrega de turno", "Dejarlo así, porque no pasó nada", "Esperar a que suene la alarma", "Las tendencias deben quedar registradas y entregarse al turno siguiente."),
        ("abc", "{F} ¿La lectura de 64 °C activó ya la alarma alta de 75 °C?", "No, porque 64 es menor que 75", "Sí, porque 64 es mayor que 60", "Sí, porque 64 es mayor que 40", "La alarma se activa al llegar a 75 °C."),
        em("Lees un diagrama de bloques en la sala de control cuando alguien avisa que el separador S-1 hace un ruido muy fuerte y que se escapa vapor.", 1),
    ],
    ctx=("abc", "Una compañera de ejemplo te dice: «Como el diagrama muestra la válvula del tanque T-1, ve y ábrela, que ya sabes dónde está». No tienes autorización. ¿Qué respondes?", "Que no, porque operar válvulas exige formación y autorización, y que avisarás al jefe de turno", "Que sí, porque el diagrama la muestra", "Que sí, si la abres poco", "Un diagrama no habilita para operar válvulas."),
    sc=[
        ("En Química Industrial: ¿qué indica la letra T en la convención de ejemplo?", "Temperatura", "La primera letra indica la variable que se mide."),
        ("En Química Industrial: ¿qué es la desviación de un parámetro?", "La diferencia entre la lectura y la consigna", "Muestra cuánto se aleja el valor del deseado."),
        ("¿Qué documento resume las novedades del turno?", "La bitácora de turno", "Ahí se registran lecturas, novedades y avisos."),
    ],
    op=("Documento ficticio de «Química Demo Costa Norte»: diagrama de bloques: tanque T-2 → reactor R-2 → envasado; instrumentos: TI-201, PI-202 y LI-203; consigna de temperatura de R-2: 50 °C, alarma alta 65 °C, límite máximo 70 °C; lectura de TI-201: 56 °C. Escribe (a) qué mide cada instrumento, (b) la desviación de la temperatura, (c) cuántos °C faltan para la alarma alta, (d) qué debe decir la entrega de turno si la temperatura viene subiendo.",
        "(a) TI-201 mide temperatura, PI-202 presión y LI-203 nivel. (b) 56 menos 50 son 6 °C. (c) 65 menos 56 son 9 °C. (d) Que la temperatura viene subiendo, con las lecturas y la hora, para que el turno entrante la vigile.",
        ["interpreta los tags", "calcula la desviación", "calcula el margen a la alarma", "describe la entrega de turno"],
        ["hoja con las cuatro respuestas"],
        ["confundir las letras de los tags", "restar al revés", "hacer una entrega sin datos"],
        "Pregunta: «¿qué indica la primera letra del tag?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Dibuja un diagrama de bloques de tres etapas y escribe tres tags de instrumentos con la convención de la clase.",
    extend="Explica con un ejemplo por qué la entrega de turno debe quedar escrita.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Hoja de turno del reactor R-1 de la planta ficticia «Química Demo Valle Claro». Temperatura de R-1 cada hora, en °C: 08:00 = 60; 09:00 = 61; 10:00 = 63; 11:00 = 66; 12:00 = 71; 13:00 = 78. "
     "Consigna: 60 °C. Alarma alta: 75 °C. Límite máximo: 80 °C. Reglas de ejemplo: ante una lectura sobre la alarma alta, el operador autorizado informa de inmediato al jefe de turno y actúa solo según la instrucción de producción y su autorización. "
     "Un estudiante en práctica puede observar y leer la hoja, pero no operar ni ajustar equipos.")
build(
    O1, 3, F,
    use="Aprenderé a analizar una hoja de turno: calcular desviaciones y tendencias, reconocer cuándo una lectura supera una alarma y distinguir quién informa y quién actúa.",
    prior=["Sé qué es una consigna, una alarma y una desviación.", "Sé calcular diferencias entre lecturas.", "Sé qué es un aviso al jefe de turno."],
    explain=[
        "En Química Industrial, analizar una hoja de turno es calcular la desviación de cada lectura respecto de la consigna y observar cómo cambia de una hora a otra. Si las diferencias entre lecturas consecutivas crecen, la variable se acelera hacia el límite, y eso es una señal de alerta incluso antes de llegar a la alarma. Cuando una lectura supera la alarma alta, el aviso al jefe de turno es inmediato.",
        "Quien monitorea informa; quien está autorizado actúa según la instrucción de producción. Un estudiante en práctica no opera ni ajusta: observa, lee y avisa. Todo lo que ocurre se anota en la bitácora con hora, valor y persona que informa. Las decisiones del proceso las toma el personal autorizado con el jefe de turno.",
        f"El caso es de papel; no se opera ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("diferencia entre lecturas consecutivas", "cambio de una lectura a la siguiente"), ("alerta temprana", "señal de que una variable va hacia un límite antes de llegar a él"), ("alarma alta", "aviso de que la lectura llegó al valor de alerta"), ("estudiante en práctica", "persona en formación que observa y lee, sin operar ni ajustar"), ("aviso inmediato", "información al jefe de turno sin esperar al fin del turno")],
    worked=[
        ("Tendencia", "Una temperatura de ejemplo va 50, 51, 53, 56 °C. ¿Cómo cambian las diferencias?", ["Las diferencias son 1, 2 y 3.", "Crecen: la temperatura se acelera."], "Se acelera"),
        ("Alarma", "Con alarma alta de 70 °C, una lectura de 72 °C, ¿qué corresponde?", ["72 supera la alarma de 70.", "Se informa de inmediato al jefe de turno."], "Informar de inmediato al jefe de turno"),
    ],
    mistakes=[("Esperar a que la lectura llegue al límite máximo para avisar.", "La alarma y la tendencia son las señales para avisar antes de llegar al límite.", "Avisa cuando se supera la alarma o cuando la tendencia se acelera."),
              ("Creer que un estudiante en práctica puede actuar «solo un poco» sobre el equipo.", "Ningún estudiante opera ni ajusta equipos de planta.", "Observa, registra y avisa al jefe de turno.")],
    T=[
        ("abc", "En Química Industrial: ¿qué indica que las diferencias entre lecturas crecen?", "Que la variable se acelera hacia un límite", "Que el instrumento está calibrado", "Que la consigna cambió", "Diferencias crecientes entre lecturas muestran que el cambio se acelera."),
        ("abc", "En Química Industrial: ¿qué hace un estudiante en práctica ante una alarma?", "Observa, registra y avisa al jefe de turno", "Ajusta el equipo para bajar la lectura", "Apaga el equipo", "El estudiante no opera ni ajusta."),
        ("abc", "En Química Industrial: ¿qué se anota en la bitácora ante un aviso?", "Hora, valor y persona que informa", "Solo el valor", "Solo la hora", "Un aviso se registra con todos sus datos."),
        ("=", "{F} ¿Cuál es la desviación de la lectura de las 13:00 respecto de la consigna?", "78-60", "Se resta la consigna a la lectura.", " °C"),
        ("=", "{F} ¿Cuánto subió la temperatura entre las 12:00 y las 13:00?", "78-71", "Se resta la lectura de las 12:00 a la de las 13:00.", " °C"),
        ("=", "{F} ¿Cuánto subió la temperatura entre las 09:00 y las 12:00?", "71-61", "Se resta la lectura de las 09:00 a la de las 12:00.", " °C"),
        ("abc", "{F} ¿A qué hora se superó por primera vez la alarma alta de 75 °C?", "A las 13:00, con 78 °C", "A las 12:00, con 71 °C", "A las 11:00, con 66 °C", "Solo la lectura de 78 °C supera 75 °C."),
        ("=", "{F} ¿Cuántos °C faltan para el límite máximo desde la lectura de las 13:00?", "80-78", "Se resta la lectura al límite máximo.", " °C"),
        ("abc", "{F} ¿Cómo cambian las diferencias de una hora a la siguiente?", "Aumentan: 1, 2, 3, 5 y 7 °C", "Se mantienen en 1 °C", "Disminuyen cada hora", "Cada subida es mayor que la anterior."),
        ("abc", "{F} A las 13:00 un estudiante en práctica ve 78 °C. ¿Qué corresponde?", "Informar de inmediato al jefe de turno y no tocar nada", "Esperar a las 14:00 para ver si baja", "Ajustar la válvula para bajar la temperatura", "Sobre la alarma el aviso es inmediato."),
        ("abc", "{F} Un operador dice: «si la lectura todavía no llega a 80, no hace falta avisar». ¿Es correcto?", "No: se debe avisar al superar la alarma de 75 °C, antes del límite", "Sí, porque 80 es el único límite", "Sí, si la lectura sube despacio", "La alarma existe para avisar antes del límite."),
        ("=", "{F} ¿Cuántos °C subió la temperatura entre las 11:00 y las 13:00?", "78-66", "Se resta la lectura de las 11:00 a la de las 13:00.", " °C"),
        em("Analizas la hoja de turno de ejemplo cuando alguien avisa que se escucha un golpe seco en el reactor R-1 y que sale vapor por una junta.", 2),
    ],
    ctx=("abc", "Un jefe de turno de ejemplo te dice: «Anota que a las 13:00 hubo 73 °C, así no activamos el protocolo». ¿Qué respondes?", "Que no: se anota la lectura real de 78 °C y se informa a quien corresponde", "Que sí, si el límite no se ha superado", "Que sí, si lo anotas con lápiz", "Cambiar un dato oculta una alarma y pone en riesgo a las personas."),
    sc=[
        ("En Química Industrial: ¿qué se calcula para ver la tendencia?", "La diferencia entre lecturas consecutivas", "Las diferencias muestran si el cambio se acelera."),
        ("¿Qué se hace al superar la alarma alta?", "Se informa de inmediato al jefe de turno", "El aviso permite una decisión autorizada a tiempo."),
        ("En Química Industrial: ¿puede un estudiante en práctica ajustar un equipo?", "No, solo observa, registra y avisa", "Ajustar un equipo exige formación y autorización del personal."),
    ],
    op=("Hoja ficticia de «Química Demo Costa Norte»: temperatura de un reactor cada hora: 40; 41; 43; 46; 50; consigna 40 °C; alarma alta 52 °C; límite máximo 60 °C. Escribe (a) la desviación de la última lectura, (b) las diferencias entre lecturas consecutivas y qué muestran, (c) si se superó la alarma, (d) qué debe hacer un estudiante en práctica si la lectura sigue subiendo.",
        "(a) 50 menos 40 son 10 °C. (b) 1, 2, 3 y 4 °C: la temperatura se acelera. (c) No se superó: 50 es menor que 52. (d) Informar al jefe de turno y no tocar nada.",
        ["calcula la desviación", "calcula las diferencias", "compara con la alarma", "indica la conducta del estudiante"],
        ["hoja con las cuatro respuestas"],
        ["no ver la aceleración", "avisar solo en el límite", "ajustar por cuenta propia"],
        "Pregunta: «¿qué cambia más rápido, la temperatura o la consigna?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una hoja de turno de cinco lecturas con consigna y alarma, y señala cuándo avisarías.",
    extend="Explica con un ejemplo por qué la tendencia es una señal útil aunque la alarma no haya sonado.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Balance del lote Z-310 de la planta ficticia «Química Demo Valle Claro». Entradas: materia A, 1.200 kg a $500 por kg; materia B, 800 kg a $300 por kg. "
     "Salidas: producto Z, 1.700 kg; residuos registrados, 180 kg; pérdidas, 120 kg. Meta de rendimiento de ejemplo: 88 %. Fórmulas de ejemplo: balance de masa: masa que entra = masa que sale; rendimiento (%) = producto × 100 ÷ masa de entradas. "
     "Costo medio de las entradas: el costo total de las materias dividido entre los kg de entrada.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un balance de masa y un rendimiento con datos de ejemplo, comparar con una meta y calcular el costo de las materias primas y de las pérdidas, con números enteros.",
    prior=["Sé calcular porcentajes.", "Sé qué es un lote.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "En Química Industrial, el balance de masa dice que la masa que entra a un proceso debe ser igual a la masa que sale, contando el producto, los residuos y las pérdidas. Si no cierra, hay un error de medición o una pérdida no registrada. El rendimiento es el porcentaje de la masa de entrada que se transforma en producto: producto por 100 dividido entre la masa de entradas.",
        "Una meta de rendimiento fija el porcentaje que se quiere lograr; para saber cuántos kg faltan, se calcula el producto que exige la meta y se resta el producto obtenido. El costo de las materias primas se calcula multiplicando los kg de cada una por su precio por kg; el costo medio de las entradas es el costo total dividido entre los kg que entraron. Con él se estima el valor de lo perdido.",
        f"Los cálculos son de planilla y sirven para el informe al especialista; no se opera ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("balance de masa", "comparación entre la masa que entra y la que sale"), ("rendimiento", "porcentaje de la masa de entrada que se convierte en producto"), ("residuo", "material que sale del proceso y no es producto"), ("pérdida", "masa que no se logra recuperar ni registrar como producto o residuo"), ("meta de rendimiento", "porcentaje de rendimiento que se quiere lograr"), ("costo medio de las entradas", "costo total de las materias dividido entre los kg que entraron")],
    worked=[
        ("Rendimiento", "Un lote de ejemplo recibe 500 kg y produce 400 kg. ¿Cuál es el rendimiento?", ["Se multiplica 400 por 100 y se divide entre 500.", "40.000 entre 500 son 80."], "80 %"),
        ("Cerrar el balance", "Un lote de ejemplo: entran 1.000 kg y salen 820 kg de producto y 150 kg de residuos. ¿Cuántos kg de pérdidas faltan para cerrar el balance?", ["Salen 820 más 150, es decir, 970 kg.", "1.000 menos 970 son 30."], "30 kg"),
    ],
    mistakes=[("Calcular el rendimiento dividiendo el producto entre los residuos.", "El rendimiento se compara con la masa que entró, no con los residuos.", "Divide el producto entre la masa de entradas."),
              ("Ignorar un balance que no cierra porque «se parece».", "Una diferencia significa pérdida o error de medición y debe informarse.", "Calcula la diferencia y avísala al especialista.")],
    T=[
        ("abc", "En Química Industrial: ¿qué dice el balance de masa?", "Que la masa que entra debe ser igual a la que sale", "Que siempre sale más de lo que entra", "Que solo se pesa el producto", "El balance compara entradas y salidas."),
        ("abc", "En Química Industrial: ¿qué es el rendimiento de un lote?", "El porcentaje de la masa de entrada que se convierte en producto", "El tiempo que tarda el lote", "El precio del producto", "Mide cuánto de lo que entra termina como producto."),
        ("abc", "En Química Industrial: ¿qué significa que un balance no cierre?", "Que hay una pérdida no registrada o un error de medición", "Que el producto es de mala calidad", "Que el lote es más grande", "Las masas de entrada y salida deben coincidir."),
        ("=", "{F} ¿Cuántos kg entraron en total al lote Z-310?", "1200+800", "Se suman las materias A y B.", " kg"),
        ("=", "{F} ¿Cuántos kg salieron en total del lote?", "1700+180+120", "Se suman producto, residuos y pérdidas.", " kg"),
        ("abc", "{F} ¿Cierra el balance de masa del lote?", "Sí, porque entran 2.000 kg y salen 2.000 kg", "No, porque entran más de lo que sale", "No, porque salen más de lo que entra", "Las dos sumas son iguales, así que el balance cierra."),
        ("=", "{F} ¿Cuál es el rendimiento del lote?", "1700*100//2000", "Se multiplica el producto por 100 y se divide entre la masa de entradas.", " %"),
        ("=", "{F} ¿Cuántos kg de producto exigía la meta del 88 %?", "2000*88//100", "Se calcula el 88 % de los 2.000 kg de entradas.", " kg"),
        ("=", "{F} ¿Cuántos kg de producto faltaron para llegar a la meta?", "2000*88//100-1700", "Se resta el producto obtenido al que exigía la meta.", " kg"),
        ("=", "{F} ¿Cuál es el costo de las materias primas del lote?", "1200*500+800*300", "Se multiplican los kg de cada materia por su precio y se suman.", " pesos"),
        ("=", "{F} ¿Cuál es el costo medio por kg de entrada?", "840000//2000", "Se divide el costo total entre los kg que entraron.", " pesos"),
        ("=", "{F} ¿Cuánto vale la pérdida de 120 kg al costo medio de las entradas?", "120*420", "Se multiplican los kg perdidos por el costo medio por kg.", " pesos"),
        em("Haces cálculos de balance en la oficina de la planta cuando alguien avisa que se rompió una tubería y que se derrama un líquido caliente cerca del reactor.", 3),
    ],
    ctx=("abc", "Un jefe de ejemplo dice: «Anota 1.760 kg de producto para llegar a la meta; ya sabemos que casi se logró». ¿Qué respondes?", "Que no: se anota el producto realmente obtenido, 1.700 kg, y se informa la diferencia con la meta", "Que sí, si el balance cierra", "Que sí, si lo corrige el turno siguiente", "Un registro falso impide detectar y corregir las causas de la brecha."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula el rendimiento?", "Producto por 100 entre la masa de entradas", "Se compara el producto con lo que entró."),
        ("En Química Industrial: ¿qué se suma en las salidas del balance?", "Producto, residuos y pérdidas", "Todo lo que sale del proceso debe contarse."),
        ("¿Cómo se calcula el costo de las materias primas de un lote?", "Kg de cada materia por su precio, y se suman", "Cada materia aporta su costo al total."),
    ],
    op=("Balance ficticio de «Química Demo Costa Norte»: entradas, 600 kg de materia M a $400 por kg y 400 kg de materia N a $250 por kg; salidas, producto 850 kg, residuos 100 kg y pérdidas 50 kg; meta de rendimiento 90 %. Escribe (a) si cierra el balance, (b) el rendimiento, (c) cuántos kg faltaron para la meta, (d) el costo total de las materias.",
        "(a) Entran 1.000 y salen 1.000: cierra. (b) 850 por 100 entre 1.000 son 85 %. (c) La meta exige 900 kg y faltaron 50 kg. (d) 240.000 más 100.000 son 340.000 pesos.",
        ["verifica el balance", "calcula el rendimiento", "calcula lo que faltó", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar un componente de las salidas", "no multiplicar por el precio"],
        "Pregunta: «¿cuánto entra y cuánto sale?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un lote con dos materias de entrada y tres salidas, y calcula el balance y el rendimiento.",
    extend="Explica con un ejemplo por qué un balance de masa que no cierra debe informarse.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Dos lotes de la planta ficticia «Química Demo Valle Claro». Lote Z-310: entradas 2.000 kg; producto 1.700 kg; energía 300 kWh (de ejemplo); 12 lecturas de temperatura, ninguna fuera de límite. "
     "Lote Z-311: entradas 2.000 kg; producto 1.800 kg; energía 400 kWh; 12 lecturas de temperatura, 3 fuera de límite. Condición obligatoria de ejemplo: el lote debe mantener sus parámetros dentro de los límites. "
     "Lista de control de la hoja de turno, 5 puntos: (1) lecturas con unidad; (2) hora de cada lectura; (3) firma del operador; (4) avisos anotados; (5) sin borrones. Se revisaron 10 hojas: 8 cumplen los 5 puntos y 2 no.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos lotes con rendimiento, consumo de energía y cumplimiento de límites, a reconocer lo que no se puede concluir y a verificar la calidad de las hojas de turno con una lista de control.",
    prior=["Sé calcular el rendimiento.", "Sé qué es una condición obligatoria.", "Sé calcular porcentajes."],
    explain=[
        "En Química Industrial, al comparar dos lotes se miran varios criterios a la vez: el rendimiento, el consumo de energía y el cumplimiento de los límites. Un lote con mejor rendimiento no es necesariamente mejor si tuvo lecturas fuera de límite, porque eso puede haber puesto en riesgo a las personas o a los equipos. El cumplimiento de los límites es una condición obligatoria: lo que no la cumple se informa al especialista y no se toma como ejemplo.",
        "Con los datos de dos lotes no se puede concluir por qué uno rindió más; esa interpretación la hace el especialista con más información. Verificar la calidad de las hojas de turno es revisarlas con una lista de control: cada punto se marca como cumple o no cumple. El porcentaje de hojas conformes es las hojas que cumplen los cinco puntos entre las revisadas, por 100.",
        f"Todo es análisis en papel; no se opera ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("cumplimiento de límites", "mantener los parámetros dentro de sus valores aceptables"), ("consumo de energía", "energía usada por el proceso, aquí en kWh de ejemplo"), ("conclusión limitada", "afirmación que solo se apoya en los datos disponibles"), ("hoja de turno conforme", "hoja que cumple los cinco puntos de la lista de control")],
    worked=[
        ("Comparar rendimientos", "El lote P de ejemplo rinde 80 % y el lote Q, 90 %, pero Q tuvo lecturas fuera de límite. ¿Se puede decir que Q trabajó mejor?", ["Q rinde más, pero incumple una condición obligatoria.", "No se puede concluir que haya trabajado mejor; se informa al especialista."], "No se puede concluir"),
        ("Porcentaje de lecturas fuera", "En un lote de ejemplo, 2 de 10 lecturas estuvieron fuera de límite. ¿Qué porcentaje es?", ["Se divide 2 entre 10 y se multiplica por 100.", "2 por 100 son 200, y 200 entre 10 son 20."], "20 %"),
    ],
    mistakes=[("Concluir que el lote de mayor rendimiento es el mejor sin mirar los límites.", "Un lote que sale de los límites puede ser riesgoso aunque rinda más.", "Revisa primero la condición obligatoria y luego compara rendimientos."),
              ("Dar por conforme una hoja de turno sin firma.", "La firma identifica a quien se hace responsable de las lecturas.", "Marca «no cumple» si falta cualquiera de los cinco puntos.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una condición obligatoria al comparar lotes?", "Un requisito que debe cumplirse, como mantener los parámetros dentro de los límites", "Un criterio que se mira solo si sobra tiempo", "El lote que produjo más", "Si no se cumple, el lote no se toma como ejemplo."),
        ("abc", "En Química Industrial: ¿qué es una conclusión limitada?", "Una afirmación que solo se apoya en los datos disponibles", "Una conclusión que no se escribe", "Una opinión sobre el operador", "No se afirma más de lo que muestran los datos."),
        ("abc", "En Química Industrial: ¿para qué sirve la lista de control de la hoja de turno?", "Para revisar punto por punto si la hoja está bien hecha", "Para calcular el rendimiento del lote", "Para elegir qué lote producir", "La lista ordena la revisión de calidad."),
        ("=", "{F} ¿Cuál es el rendimiento del lote Z-310?", "1700*100//2000", "Se multiplica el producto por 100 y se divide entre las entradas.", " %"),
        ("=", "{F} ¿Cuál es el rendimiento del lote Z-311?", "1800*100//2000", "Se multiplica el producto por 100 y se divide entre las entradas.", " %"),
        ("=", "{F} ¿Cuántos kWh más consumió el lote Z-311 que el Z-310?", "400-300", "Se resta el consumo de Z-310 al de Z-311.", " kWh"),
        ("=", "{F} ¿Qué porcentaje de las lecturas de temperatura del lote Z-311 estuvo fuera de límite?", "3*100//12", "Se divide las lecturas fuera de límite entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Se puede concluir que el lote Z-311 trabajó mejor porque rindió más?", "No, porque tuvo lecturas fuera de límite y consumió más energía; lo evalúa el especialista", "Sí, porque 90 % es mayor que 85 %", "Sí, porque consumió más energía", "El rendimiento no basta si se incumple la condición obligatoria."),
        ("abc", "{F} ¿Qué lote cumple la condición obligatoria?", "El Z-310, porque no tuvo lecturas fuera de límite", "El Z-311, porque rindió más", "Ambos, porque tienen 12 lecturas", "Solo el Z-310 mantuvo sus parámetros dentro de límites."),
        ("=", "{F} ¿Qué porcentaje de las 10 hojas de turno revisadas cumple los 5 puntos?", "8*100//10", "Se dividen las hojas conformes entre las revisadas y se multiplica por 100.", " %"),
        ("abc", "{F} Una hoja de turno no tiene la firma del operador. ¿Qué corresponde?", "Marcarla como no conforme e informar para corregirla con respaldo", "Aceptarla porque tiene todas las lecturas", "Firmarla otra persona", "La firma identifica al responsable de las lecturas."),
        ("=", "{F} Si se corrigen las 2 hojas no conformes con respaldo, ¿cuántas de las 10 cumplirán los 5 puntos?", "8+2", "Se suman las conformes y las corregidas.", " hojas"),
        em("Comparas dos lotes de ejemplo en la oficina cuando alguien avisa que un equipo de la sala se está recalentando y que sale humo con mal olor.", 4),
    ],
    ctx=("abc", "Un supervisor de ejemplo dice: «Copiemos la forma de trabajar del lote Z-311, que rinde más». ¿Qué respondes?", "Que primero debe revisarse por qué hubo lecturas fuera de límite, y que lo decide el especialista", "Que sí, porque rinde más", "Que sí, si se consume menos energía", "Un lote que sale de los límites no es un buen modelo sin revisión."),
    sc=[
        ("En Química Industrial: ¿qué se revisa primero al comparar lotes?", "Que cumplan la condición obligatoria de los límites", "Sin eso, el rendimiento no basta."),
        ("En Química Industrial: ¿cómo se calcula el porcentaje de hojas conformes?", "Hojas conformes entre revisadas, por 100", "Es un indicador de la calidad del registro."),
        ("¿Qué se hace con una hoja de turno sin firma?", "Se informa y se corrige con respaldo", "La firma no se agrega por suposición."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: lote K-1, entradas 1.000 kg, producto 800 kg, 0 lecturas fuera de límite de 10; lote K-2, entradas 1.000 kg, producto 900 kg, 2 lecturas fuera de límite de 10. De 5 hojas de turno, 4 son conformes. Escribe (a) el rendimiento de cada lote, (b) qué lote cumple la condición obligatoria, (c) el porcentaje de lecturas fuera de límite de K-2, (d) por qué no se concluye que K-2 sea mejor.",
        "(a) K-1: 80 %; K-2: 90 %. (b) K-1. (c) 2 por 100 entre 10 son 20 %. (d) Porque K-2 tuvo lecturas fuera de límite y la causa la evalúa el especialista.",
        ["calcula los rendimientos", "identifica el lote que cumple", "calcula el porcentaje fuera de límite", "justifica no concluir"],
        ["hoja con las cuatro respuestas"],
        ["elegir por rendimiento", "olvidar la condición obligatoria", "afirmar sin datos"],
        "Pregunta: «¿qué lote mantuvo sus parámetros dentro de los límites?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Compara dos lotes inventados con rendimiento, energía y lecturas fuera de límite, y escribe una conclusión limitada.",
    extend="Explica con un ejemplo por qué un buen rendimiento no basta para considerar bueno un lote.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Plan de muestreo de proceso de la planta ficticia «Química Demo Valle Claro» para el «Producto Z de ejemplo»: PM-1 (salida del reactor R-1, producto intermedio), una muestra cada 2 horas; PM-2 (salida del separador S-1, producto intermedio), una muestra cada 4 horas; "
     "PM-3 (envasado, producto final), una muestra por lote. Los turnos son de 8 horas. Peligros anotados: producto caliente, superficie caliente y presión en la válvula del punto de muestreo. Matriz de ejemplo: puntaje = probabilidad × gravedad. "
     "Producto caliente: probabilidad 3 y gravedad 4. Superficie caliente: probabilidad 3 y gravedad 3. Presión en la válvula: probabilidad 2 y gravedad 4.")
build(
    O2, 1, F,
    use="Aprenderé qué son las muestras de productos intermedios y finales, qué es un punto de muestreo y una frecuencia, qué peligros tiene el muestreo en planta y por qué solo personal formado toma muestras.",
    prior=["Sé qué es una muestra y un rótulo.", "Sé calcular el puntaje de riesgo.", "Sé dividir números enteros."],
    explain=[
        "En Química Industrial, un producto intermedio es el que está en una etapa del proceso y aún no es el producto terminado; el producto final es el que sale terminado y se envasa. Las muestras de proceso se toman en puntos de muestreo, que son lugares designados del equipo o de la línea, con una frecuencia fijada en el plan, para comprobar que la calidad está dentro de lo esperado. Cada muestra se rotula con su código, el punto, el lote, la fecha y la hora.",
        "Los equipos auxiliares y utensilios con que se toma una muestra deben estar limpios, identificados y ser apropiados para el producto, según el procedimiento aprobado. El muestreo en planta tiene peligros, como producto caliente y presión en la válvula; el puntaje de riesgo de la matriz de ejemplo se calcula como probabilidad por gravedad.",
        f"Tomar muestras de proceso exige formación, autorización y elementos de protección; este cuaderno no enseña a tomarlas. {EMER} {AVISO}",
    ],
    vocab=[("producto intermedio", "producto de una etapa del proceso que aún no está terminado"), ("producto final", "producto terminado que se envasa"), ("punto de muestreo", "lugar designado del equipo o de la línea para tomar una muestra"), ("frecuencia de muestreo", "cada cuánto tiempo se toma una muestra"), ("utensilio apropiado", "elemento limpio, identificado y adecuado al producto según el procedimiento"), ("puntaje de riesgo", "probabilidad multiplicada por gravedad")],
    worked=[
        ("Muestras por turno", "Un punto de muestreo de ejemplo toma una muestra cada 4 horas en un turno de 8 horas. ¿Cuántas muestras son?", ["Se divide la duración del turno entre la frecuencia.", "8 entre 4 son 2."], "2 muestras"),
        ("Puntaje de riesgo", "Un peligro de ejemplo, un piso mojado junto al punto de muestreo, tiene probabilidad 4 y gravedad 2. ¿Qué puntaje tiene?", ["Se multiplica la probabilidad por la gravedad.", "4 por 2 son 8."], "8 puntos"),
    ],
    mistakes=[("Creer que quien conoce el plan de muestreo puede tomar las muestras.", "El muestreo en planta exige formación, autorización y elementos de protección.", "Usa el plan para entender el trabajo y pide autorización para hacerlo."),
              ("Usar cualquier envase a mano para guardar una muestra.", "El envase debe ser apropiado e identificado según el procedimiento.", "Usa solo los utensilios que indica el procedimiento.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un producto intermedio?", "Un producto de una etapa del proceso que aún no está terminado", "El producto terminado y envasado", "El envase vacío", "El intermedio está entre la materia prima y el producto final."),
        ("abc", "En Química Industrial: ¿qué es un punto de muestreo?", "Un lugar designado del equipo o de la línea para tomar una muestra", "La hora en que termina el turno", "El nombre del laboratorio", "El punto de muestreo está definido en el plan."),
        ("abc", "En Química Industrial: ¿qué es la frecuencia de muestreo?", "Cada cuánto tiempo se toma una muestra", "Cuántos gramos tiene la muestra", "Quién firma la muestra", "La frecuencia fija el intervalo entre muestras."),
        ("=", "{F} ¿Cuántas muestras se toman en PM-1 en un turno de 8 horas?", "8//2", "Se divide la duración del turno entre la frecuencia de 2 horas.", " muestras"),
        ("=", "{F} ¿Cuántas muestras se toman en PM-2 en un turno de 8 horas?", "8//4", "Se divide la duración del turno entre la frecuencia de 4 horas.", " muestras"),
        ("=", "{F} ¿Cuántas muestras de proceso se toman en total en PM-1 y PM-2 en un turno?", "8//2+8//4", "Se suman las muestras de los dos puntos.", " muestras"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el producto caliente?", "3*4", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} Según la matriz, ¿qué peligro tiene el mayor puntaje de riesgo?", "El producto caliente, con 12 puntos", "La superficie caliente, con 9 puntos", "La presión en la válvula, con 8 puntos", "Se compara probabilidad por gravedad de cada peligro."),
        ("abc", "{F} ¿Qué punto del plan toma muestras del producto final?", "PM-3, en el envasado", "PM-1, en el reactor", "PM-2, en el separador", "El plan indica que PM-3 toma el producto final."),
        ("abc", "{F} Una estudiante en práctica propone tomar una muestra en PM-1 «para ayudar». ¿Qué corresponde?", "No hacerlo: solo personal formado y autorizado toma muestras de proceso", "Hacerlo con guantes", "Hacerlo si el producto se ve frío", "Tomar muestras exige formación, autorización y protección."),
        ("abc", "{F} Un operario quiere guardar una muestra de PM-2 en una botella cualquiera que encontró. ¿Qué corresponde?", "Rechazarlo: debe usarse el utensilio apropiado e identificado que indica el procedimiento", "Aceptarlo si la botella está limpia", "Aceptarlo si se rotula después", "El envase debe ser apropiado e identificado según el procedimiento."),
        ("=", "{F} En 3 turnos de 8 horas, ¿cuántas muestras se toman en PM-1?", "3*(8//2)", "Se multiplica las muestras de un turno por los turnos.", " muestras"),
        em("Lees el plan de muestreo de ejemplo en la sala de control cuando alguien avisa que de la válvula de un punto de muestreo sale vapor a presión y que se siente olor fuerte.", 0),
    ],
    ctx=("abc", "Un compañero de ejemplo te dice: «Ve a PM-2 y toma la muestra de las 12:00, que yo estoy ocupado». No tienes autorización. ¿Qué respondes?", "Que no, porque tomar muestras de proceso exige formación y autorización, y que avisarás al jefe de turno", "Que sí, si usas guantes", "Que sí, si es solo una muestra pequeña", "Un plan escrito no habilita para tomar muestras."),
    sc=[
        ("En Química Industrial: ¿qué es el producto final?", "El producto terminado que se envasa", "Sale del proceso listo para entregarse."),
        ("En Química Industrial: ¿cómo se calculan las muestras de un turno?", "Duración del turno dividida entre la frecuencia", "Así se obtiene cuántas veces se toma la muestra."),
        ("¿Quién toma las muestras de proceso?", "Personal formado y autorizado", "Leer el plan no basta para tomarlas."),
    ],
    op=("Plan ficticio de «Química Demo Costa Norte»: PM-A, salida del reactor, una muestra cada 3 horas; PM-B, envasado, una muestra por lote; turnos de 9 horas; peligro: producto caliente (probabilidad 4, gravedad 3). Escribe (a) cuántas muestras se toman en PM-A por turno, (b) el puntaje del peligro, (c) qué punto toma muestras del producto final, (d) por qué leer este plan no te habilita para tomar muestras.",
        "(a) 9 entre 3 son 3 muestras. (b) 4 por 3 son 12 puntos. (c) PM-B, en el envasado. (d) Porque tomar muestras exige formación, autorización y elementos de protección.",
        ["calcula las muestras por turno", "calcula el puntaje", "identifica el punto del producto final", "aclara que leer no habilita"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "confundir los puntos", "creer que el plan autoriza"],
        "Pregunta: «¿qué se divide entre qué?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un plan con dos puntos de muestreo, sus frecuencias y la duración del turno, y calcula las muestras por turno.",
    extend="Explica con un ejemplo por qué las muestras de proceso se toman con una frecuencia fija.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Rótulo de una muestra de planta de «Química Demo Valle Claro»: código PM2-Z310-0830; producto: intermedio del Producto Z; punto: PM-2; lote: Z-310; fecha y hora: 14 de mayo de ejemplo, 08:30; temperatura registrada del producto: 55 °C (de ejemplo); responsable: operador de turno; destino: laboratorio. "
     "Registro de muestras del turno: 8 muestras tomadas, de las cuales 6 tienen el rótulo completo y 2 tienen algún dato faltante. Plazo máximo de entrega al laboratorio: 45 minutos (de ejemplo). La muestra del rótulo se tomó a las 08:30 y se entregó a las 09:10. "
     "La muestra retenida es una porción guardada del producto final de cada lote.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos y documentos del rotulado de muestras de planta: rótulo, registro de muestras, plazo de entrega, cadena de custodia, muestra retenida y los roles de cada persona.",
    prior=["Sé qué es un punto de muestreo.", "Sé calcular porcentajes.", "Sé calcular diferencias de horas."],
    explain=[
        "En Química Industrial, el rótulo de una muestra de planta lleva el código, el producto, el punto de muestreo, el lote, la fecha y la hora, la temperatura registrada, el responsable y el destino. Con esos datos se puede seguir la muestra hasta el laboratorio, que es la trazabilidad. El registro de muestras del turno es la lista de todas las muestras tomadas, con su rótulo y su entrega.",
        "La cadena de custodia anota quién tuvo la muestra en cada momento, con hora y firma. Hay un plazo máximo de entrega al laboratorio, porque una muestra que espera demasiado puede cambiar. La muestra retenida es una porción del producto final de cada lote que se guarda por si hay reclamos. Cada rol tiene su tarea: el operador autorizado toma y rotula, el laboratorio recibe y analiza, y el supervisor revisa los registros.",
        f"Esta clase trabaja con documentos de ejemplo en papel. {EMER} {AVISO}",
    ],
    vocab=[("rótulo de muestra de planta", "etiqueta con código, producto, punto, lote, fecha y hora, temperatura, responsable y destino"), ("registro de muestras del turno", "lista de las muestras tomadas en el turno con su rótulo y su entrega"), ("plazo máximo de entrega", "tiempo máximo para llevar la muestra al laboratorio"), ("cadena de custodia", "registro de quién tuvo la muestra en cada momento"), ("muestra retenida", "porción del producto final de un lote que se guarda por si hay reclamos")],
    worked=[
        ("Tiempo de entrega", "Una muestra de ejemplo se tomó a las 14:00 y se entregó a las 14:35, con plazo máximo de 40 minutos. ¿Cumple?", ["Pasaron 35 minutos.", "35 es menor que 40, así que cumple."], "Sí, cumple"),
        ("Porcentaje de rótulos completos", "En un turno de ejemplo, 9 de 12 muestras tienen el rótulo completo. ¿Qué porcentaje es?", ["Se divide 9 entre 12 y se multiplica por 100.", "9 por 100 son 900, y 900 entre 12 son 75."], "75 %"),
    ],
    mistakes=[("Entregar una muestra sin hora de entrega ni firma.", "Se rompe la cadena de custodia y no se puede comprobar el plazo.", "Anota hora y firma en cada entrega."),
              ("Rotular una muestra con el lote anterior «porque es el mismo producto».", "Cada lote debe identificarse con su propio código para la trazabilidad.", "Escribe el lote que corresponde a la muestra.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la muestra retenida?", "Una porción del producto final de un lote que se guarda por si hay reclamos", "La primera muestra del turno", "Una muestra sin rótulo", "La retenida respalda la calidad de cada lote."),
        ("abc", "En Química Industrial: ¿para qué existe un plazo máximo de entrega?", "Porque una muestra que espera demasiado puede cambiar", "Para que el turno termine antes", "Para reducir el costo del análisis", "El plazo protege la integridad de la muestra."),
        ("abc", "En Química Industrial: ¿qué es la cadena de custodia?", "El registro de quién tuvo la muestra en cada momento", "La lista de los lotes del año", "El orden de los puntos de muestreo", "Documenta el recorrido de la muestra."),
        ("=", "{F} ¿Cuántos minutos pasaron entre la toma y la entrega de la muestra del rótulo?", "(9*60+10)-(8*60+30)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Se cumplió el plazo máximo de entrega de 45 minutos?", "Sí, porque pasaron 40 minutos", "No, porque pasaron más de 45 minutos", "No, porque la entrega fue en la mañana", "40 minutos es menor que 45."),
        ("=", "{F} ¿Cuántas muestras del registro tienen algún dato faltante?", "8-6", "Se resta las completas al total.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de las muestras del turno tiene el rótulo completo?", "6*100//8", "Se divide las completas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué dato del rótulo identifica de qué lote es la muestra?", "Z-310", "PM-2", "55 °C", "El lote está en el rótulo como Z-310."),
        ("abc", "{F} ¿Qué dato permite saber en qué lugar del proceso se tomó la muestra?", "El punto PM-2", "El código del responsable", "La fecha", "El punto de muestreo identifica el lugar."),
        ("abc", "{F} Una muestra llegó al laboratorio con el lote Z-301 en el rótulo, pero se tomó del lote Z-310. ¿Qué corresponde?", "Informar al supervisor y corregir con traza, sin cambiarlo por cuenta propia", "Cambiar el rótulo apenas se detecta", "Dejarlo porque es casi igual", "Un cambio sin registro rompe la trazabilidad."),
        ("abc", "{F} El laboratorio recibe la muestra sin firma de entrega. ¿Qué ocurre con la cadena de custodia?", "Queda rota y debe informarse al supervisor", "No pasa nada, porque la hora está anotada", "Se firma por la persona que no estaba", "La cadena exige firma en cada traspaso."),
        ("=", "{F} Si el plazo máximo de entrega fuera de 60 minutos, ¿cuántos minutos de margen habría con la entrega de 40 minutos?", "60-40", "Se resta el tiempo usado al plazo máximo.", " minutos"),
        em("Revisas un registro de muestras de ejemplo en la sala de control cuando alguien avisa que se rompió un envase de muestras en el pasillo y que hay olor irritante.", 1),
    ],
    ctx=("abc", "Un operador de ejemplo te dice: «Anota que entregué la muestra a las 08:50, aunque llegó a las 09:30; así cumple el plazo». ¿Qué respondes?", "Que no: se anota la hora real y se informa el atraso al supervisor", "Que sí, si la muestra se ve bien", "Que sí, pero solo esta vez", "Un registro falso rompe la cadena de custodia."),
    sc=[
        ("En Química Industrial: ¿qué datos lleva el rótulo de una muestra de planta?", "Código, producto, punto, lote, fecha y hora, temperatura, responsable y destino", "Permite seguir la muestra hasta el laboratorio."),
        ("En Química Industrial: ¿para qué se guarda la muestra retenida?", "Para respaldar la calidad del lote si hay reclamos", "Se guarda una porción de cada lote."),
        ("¿Qué se hace si el rótulo tiene un dato equivocado?", "Se informa y se corrige con traza", "No se cambia por cuenta propia."),
    ],
    op=("Registro ficticio de «Química Demo Costa Norte»: 5 muestras de proceso, una con la hora ilegible, otra sin firma de entrega; la muestra M-3 se tomó a las 10:00 y se entregó a las 10:50 con plazo máximo de 45 minutos. Escribe (a) cuántas muestras tienen rótulo completo y qué porcentaje es, (b) si M-3 cumple el plazo y cuántos minutos pasaron, (c) qué problema tiene la muestra sin firma, (d) por qué se guarda una muestra retenida.",
        "(a) 3 de 5 muestras: 60 %. (b) Pasaron 50 minutos, más de 45: no cumple. (c) Se rompe la cadena de custodia. (d) Para respaldar la calidad del lote si hay reclamos.",
        ["calcula el porcentaje", "evalúa el plazo", "detecta la falla de custodia", "explica la muestra retenida"],
        ["hoja con las cuatro respuestas"],
        ["restar mal las horas", "no ver la firma faltante", "no explicar la retenida"],
        "Pregunta: «¿entre qué horas se mide el plazo?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe un rótulo de ejemplo de una muestra de planta con los ocho datos y calcula el tiempo de entrega.",
    extend="Explica con un ejemplo por qué una muestra que espera demasiado puede dar un resultado distinto al real.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Lista de muestras de un turno en «Química Demo Valle Claro». Cada muestra debe tener código correcto, lote correcto (Z-310), temperatura registrada, firma y entrega dentro de 45 minutos. "
     "1) PM1-Z310-0800, 08:00, completa, entregada 08:30. 2) PM1-Z310-1000, 10:00, completa, entregada 10:20. 3) PM2-Z310-1030, 10:30, sin temperatura registrada, entregada 11:00. "
     "4) PM1-Z310-1200, rótulo con el lote Z-301 por error, entregada 12:25. 5) PM2-Z310-1430, completa, entregada 15:30. 6) PM3-Z310-1600, completa, entregada 16:20.")
build(
    O2, 3, F,
    use="Aprenderé a analizar una lista de muestras de un turno: detectar datos faltantes, lotes equivocados y plazos excedidos, decidir qué problema pesa más e informar sin corregir de memoria.",
    prior=["Sé qué lleva el rótulo de una muestra de planta.", "Sé calcular diferencias de horas.", "Sé calcular porcentajes."],
    explain=[
        "En Química Industrial, revisar la lista de muestras de un turno es comparar cada una con los requisitos: código correcto, lote correcto, temperatura registrada, firma y entrega dentro del plazo. Una muestra que incumple un requisito es una no conformidad y no se usa para decidir sobre el producto hasta que se resuelva, porque sus resultados podrían ser engañosos.",
        "No todos los problemas pesan igual: un lote equivocado hace que el resultado se asigne al lote que no corresponde y puede llevar a aprobar o rechazar un producto por error. Un plazo excedido puede alterar la muestra, y una temperatura faltante dificulta interpretar el resultado. Todos se informan al supervisor y se resuelven con respaldo, sin corregir ni inventar datos.",
        f"El caso se resuelve en papel; no se toman muestras. {EMER} {AVISO}",
    ],
    vocab=[("lote equivocado", "rótulo con un lote distinto al de la muestra"), ("plazo excedido", "entrega que tarda más que el máximo permitido"), ("dato faltante", "requisito del rótulo que no está escrito"), ("no conformidad", "incumplimiento de un requisito del rótulo o del registro"), ("muestra no confiable", "muestra con un problema que impide usar su resultado")],
    worked=[
        ("Revisar un plazo", "Una muestra de ejemplo se tomó a las 09:00 y se entregó a las 09:50, con plazo máximo de 45 minutos. ¿Cumple?", ["Pasaron 50 minutos.", "50 es mayor que 45: no cumple."], "No cumple"),
        ("Comparar gravedad", "Una muestra de ejemplo tiene el lote equivocado y otra no tiene temperatura. ¿Cuál puede llevar a una decisión equivocada sobre el lote?", ["Con el lote equivocado el resultado se asigna a otro lote.", "La temperatura faltante dificulta interpretar, pero no cambia el lote."], "La del lote equivocado"),
    ],
    mistakes=[("Corregir el lote del rótulo por cuenta propia apenas se detecta el error.", "Un cambio sin registro rompe la trazabilidad.", "Informa al supervisor y corrige con traza y respaldo."),
              ("Usar una muestra entregada fuera de plazo porque «se ve igual».", "El tiempo puede alterar la muestra aunque se vea igual.", "Informa el atraso y espera la decisión del responsable.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un lote equivocado en un rótulo?", "Un rótulo con un lote distinto al de la muestra", "Un lote más grande de lo previsto", "Una muestra sin firma", "El lote equivocado impide la trazabilidad."),
        ("abc", "En Química Industrial: ¿qué se hace con una muestra no confiable?", "Se informa y no se usa su resultado hasta resolverlo", "Se usa igual para ahorrar tiempo", "Se descarta sin avisar", "El resultado de una muestra no confiable puede engañar."),
        ("abc", "En Química Industrial: ¿se corrige un rótulo de memoria?", "No, se informa y se corrige con traza y respaldo", "Sí, si el error es evidente", "Sí, si lo hace el operador", "Los datos no se inventan ni se cambian sin registro."),
        ("=", "{F} ¿Cuántos minutos tardó la entrega de la muestra 5?", "(15*60+30)-(14*60+30)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Qué muestra incumple el plazo de 45 minutos?", "La muestra 5", "La muestra 2", "La muestra 6", "Pasaron 60 minutos entre la toma y la entrega."),
        ("abc", "{F} ¿Qué problema tiene la muestra 3?", "No tiene temperatura registrada", "Tiene el lote equivocado", "Excedió el plazo", "La lista dice que no tiene temperatura."),
        ("abc", "{F} ¿Qué problema tiene la muestra 4?", "Tiene el lote Z-301 por error", "No tiene firma", "Se entregó a tiempo, pero no tiene hora", "El rótulo dice Z-301 y debería decir Z-310."),
        ("=", "{F} ¿Cuántas muestras de la lista tienen algún problema?", "3", "Tienen problema las muestras 3, 4 y 5.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de la lista está completo?", "3*100//6", "Se divide las completas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué problema puede llevar a decidir sobre el lote equivocado?", "El rótulo con el lote Z-301 de la muestra 4", "La temperatura faltante de la muestra 3", "El plazo de la muestra 5", "Con el lote equivocado el resultado se asigna al lote que no corresponde."),
        ("abc", "{F} Un operador propone cambiar el lote de la muestra 4 a Z-310 con su lapicero «para arreglarlo ya». ¿Qué corresponde?", "Informar al supervisor y corregir con traza y respaldo", "Hacerlo, porque el error es evidente", "Hacerlo si lo hace otra persona", "Un cambio sin registro rompe la trazabilidad."),
        ("abc", "{F} ¿Qué corresponde con la muestra 5, entregada fuera de plazo?", "Informar el atraso y esperar la decisión del responsable", "Usar su resultado si se ve normal", "Anotar que se entregó dentro del plazo", "El atraso puede alterar la muestra."),
        em("Revisas la lista de muestras en la oficina cuando alguien avisa que se rompió un tambor de muestras en la bodega y que se escapa un olor muy fuerte.", 2),
    ],
    ctx=("abc", "Una supervisora de ejemplo te dice: «Marca las 6 muestras como completas para cerrar el informe del turno». ¿Qué respondes?", "Que no: se informan las 3 no conformidades y esas muestras no se usan hasta resolverlas", "Que sí, si se corrigen mañana", "Que sí, si el cliente no se entera", "El informe debe reflejar lo real."),
    sc=[
        ("En Química Industrial: ¿qué problema del rótulo es más grave, un lote equivocado o una temperatura faltante?", "El lote equivocado", "El resultado se asignaría al lote que no corresponde."),
        ("En Química Industrial: ¿qué se hace con una muestra fuera de plazo?", "Se informa y espera la decisión del responsable", "El atraso puede alterar la muestra."),
        ("¿Se inventan los datos faltantes de un rótulo?", "No, se informa y se resuelve con respaldo", "Un dato inventado rompe la trazabilidad."),
    ],
    op=("Lista ficticia de «Química Demo Costa Norte»: 1) completa, entregada a los 30 minutos; 2) sin firma de entrega; 3) con el lote K-12 en lugar de K-21, entregada a los 20 minutos; 4) completa, entregada a los 50 minutos; plazo máximo de 45 minutos. Escribe (a) cuántas muestras tienen problemas, (b) cuáles son los problemas, (c) cuál es el más grave y por qué, (d) qué haces con las muestras involucradas.",
        "(a) Tres: la 2, la 3 y la 4. (b) Falta de firma, lote equivocado y plazo excedido. (c) El lote equivocado, porque el resultado se asignaría al lote que no corresponde. (d) Informar al supervisor y no usar sus resultados hasta resolverlos.",
        ["cuenta las muestras con problemas", "nombra los problemas", "identifica el más grave", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["no contar la excedida", "corregir por suposición", "usar los resultados sin resolver"],
        "Pregunta: «¿qué decisión podría tomarse por error?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una lista de cinco muestras con dos errores y descríbelos.",
    extend="Explica con un ejemplo por qué un lote equivocado puede cambiar la decisión sobre un producto.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada) de «Química Demo Valle Claro». Plan de muestreo: 3 turnos por día; en cada turno de 8 horas se toma una muestra cada 2 horas en PM-1 y una cada 4 horas en PM-2; en PM-3 se toma 1 muestra por día (un lote por día). "
     "Cada muestra es de 250 mL (de ejemplo). Todas las muestras se retienen 30 días. Un estante de retención admite 90 muestras. Costo de analizar una muestra: $8.000 (de ejemplo).")
build(
    O2, 4, F,
    use="Aprenderé a aplicar el plan de muestreo con datos de ejemplo: calcular muestras por día, volumen, estantes de retención y costo de análisis, con números enteros y redondeo hacia arriba cuando corresponda.",
    prior=["Sé calcular muestras por turno.", "Sé multiplicar y dividir números enteros.", "Sé redondear hacia arriba."],
    explain=[
        "En Química Industrial, los cálculos de un plan de muestreo ordenan el trabajo y el costo. Las muestras por turno son la duración del turno dividida entre la frecuencia de cada punto; las muestras por día son las de un turno por el número de turnos, más las muestras por lote. El volumen total se calcula multiplicando el número de muestras por el volumen de cada una.",
        "Las muestras retenidas se guardan durante un plazo; para saber cuántas hay guardadas se multiplica la cantidad diaria por los días del plazo. Los estantes necesarios se obtienen dividiendo las muestras entre las que admite cada estante y redondeando hacia arriba, porque una muestra más ya ocupa un estante nuevo. El costo de análisis es el número de muestras por el costo de cada una.",
        f"Los cálculos son de planilla; tomar y guardar muestras lo hace personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("muestras por día", "muestras de un turno por los turnos, más las de cada lote"), ("volumen total", "muestras por el volumen de cada una"), ("muestras retenidas", "muestras que se guardan durante un plazo"), ("estante de retención", "estante con capacidad limitada para guardar muestras retenidas"), ("redondear hacia arriba", "subir al entero siguiente cuando sobra una parte")],
    worked=[
        ("Muestras por día", "Un punto de ejemplo toma 3 muestras por turno y hay 2 turnos al día, más 1 muestra por lote. ¿Cuántas muestras son por día?", ["Se multiplican las muestras por turno por los turnos: 3 por 2 son 6.", "Se suma 1 por el lote: 7."], "7 muestras"),
        ("Estantes necesarios", "Un laboratorio de ejemplo guarda 150 muestras y cada estante admite 60. ¿Cuántos estantes necesita? Redondea hacia arriba.", ["150 entre 60 es 2 y sobran 30.", "Las 30 muestras sobrantes ocupan un estante más: 3."], "3 estantes"),
    ],
    mistakes=[("Olvidar la muestra por lote al calcular las muestras del día.", "El plan incluye una muestra por lote además de las muestras de proceso.", "Suma las muestras por lote a las de los turnos."),
              ("Redondear hacia abajo los estantes.", "Una muestra sobrante igual necesita un estante.", "Si sobra, sube al entero siguiente.")],
    T=[
        ("abc", "En Química Industrial: ¿qué se calcula para las muestras por día?", "Las muestras de un turno por los turnos, más las de cada lote", "Solo las muestras de un turno", "Solo las muestras por lote", "El plan incluye las muestras de proceso y las de lote."),
        ("abc", "En Química Industrial: ¿cómo se calcula el volumen total de las muestras?", "Muestras por volumen de cada una", "Muestras entre volumen de cada una", "Volumen de una muestra menos las muestras", "El volumen total es el producto de ambos."),
        ("abc", "En Química Industrial: ¿para qué se redondea hacia arriba al calcular estantes?", "Porque una muestra sobrante igual necesita un estante", "Porque así se compra más de lo necesario", "Porque los estantes son siempre de 90", "El resto de muestras ocupa un estante nuevo."),
        ("=", "{F} ¿Cuántas muestras se toman por turno en PM-1 y PM-2 juntos?", "8//2+8//4", "Se suman las muestras de ambos puntos en un turno de 8 horas.", " muestras"),
        ("=", "{F} ¿Cuántas muestras se toman por día en total, contando la de PM-3?", "(8//2+8//4)*3+1", "Se multiplican las muestras de un turno por 3 turnos y se suma la muestra por lote.", " muestras"),
        ("=", "{F} ¿Cuántos mL suman las muestras de un día?", "19*250", "Se multiplica el número de muestras por el volumen de cada una.", " mL"),
        ("=", "{F} ¿Cuántas muestras retenidas hay guardadas después de 30 días?", "19*30", "Se multiplican las muestras diarias por los días del plazo.", " muestras"),
        ("=", "{F} ¿Cuántos estantes de retención se necesitan para 570 muestras? Redondea hacia arriba.", "(570+89)//90", "Se divide entre 90 y se redondea hacia arriba porque sobran muestras.", " estantes"),
        ("=", "{F} ¿Cuánto cuesta analizar las muestras de un día?", "19*8000", "Se multiplica el número de muestras por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta analizar solo las muestras de PM-1 de un turno?", "(8//2)*8000", "Se multiplican las muestras del turno por el costo de cada una.", " pesos"),
        ("abc", "{F} Un jefe propone no retener las muestras de PM-2 «para ahorrar estantes». ¿Qué corresponde?", "Mantener la retención según el plan, y consultar al responsable si falta espacio", "Aceptarlo porque son intermedios", "Aceptarlo si se avisa por mensaje", "El plan fija la retención de todas las muestras."),
        ("=", "{F} Si PM-2 pasara a tomar una muestra cada 2 horas, ¿cuántas muestras tomaría por turno?", "8//2", "Se divide la duración del turno entre la nueva frecuencia.", " muestras"),
        em("Haces cálculos del plan de muestreo en la oficina cuando alguien avisa que un estante de retención se cayó y que hay frascos rotos con olor irritante.", 3),
    ],
    ctx=("abc", "Una compañera de ejemplo dice: «Tomemos solo la mitad de las muestras para bajar los costos». ¿Qué respondes?", "Que la frecuencia la fija el plan aprobado y se consulta al responsable antes de cambiarla", "Que sí, porque ahorra dinero", "Que sí, si nadie se entera", "Cambiar la frecuencia sin autorización reduce el control de calidad."),
    sc=[
        ("En Química Industrial: ¿cómo se calculan las muestras retenidas?", "Muestras diarias por días del plazo", "Se acumulan durante todo el plazo."),
        ("En Química Industrial: ¿qué se hace si sobran muestras al calcular estantes?", "Se redondea hacia arriba", "La sobrante igual necesita un estante."),
        ("¿Cómo se calcula el costo de análisis?", "Muestras por el costo de cada una", "Cada muestra tiene su costo de análisis y se suman."),
    ],
    op=("Plan ficticio de «Química Demo Costa Norte»: 2 turnos por día de 8 horas; PM-A, una muestra cada 4 horas; PM-B, 1 muestra por día; muestras de 200 mL; retención de 20 días; estantes de 30 muestras; análisis a $5.000. Escribe (a) cuántas muestras se toman por día, (b) cuántos mL suman, (c) cuántos estantes se necesitan para la retención, (d) cuánto cuesta analizar las muestras de un día.",
        "(a) PM-A: 8 entre 4 son 2 por turno y 4 por día; con PM-B son 5 muestras. (b) 5 por 200 son 1.000 mL. (c) 5 por 20 son 100 muestras; 100 entre 30 son 3 y sobra, así que 4 estantes. (d) 5 por 5.000 son 25.000 pesos.",
        ["calcula las muestras por día", "calcula el volumen", "calcula los estantes", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la muestra por lote", "no redondear hacia arriba", "no multiplicar por los turnos"],
        "Pregunta: «¿cuántas muestras salen de PM-A por día?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un plan con dos puntos de muestreo y calcula muestras por día, volumen y estantes.",
    extend="Explica con un ejemplo por qué una frecuencia de muestreo no debe cambiarse sin autorización.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Ronda de verificación de la planta ficticia «Química Demo Valle Claro» con equipos: bomba P-1, intercambiador E-1, reactor R-1 y compresor C-1. "
     "Señales anotadas: ruido anormal en la bomba P-1; una mancha húmeda en el piso bajo una brida del reactor R-1 (posible fuga); la temperatura del intercambiador E-1, 5 °C sobre lo normal. "
     "Matriz de ejemplo: puntaje = probabilidad × gravedad. Ruido anormal: probabilidad 3 y gravedad 3. Posible fuga: probabilidad 3 y gravedad 5. Temperatura sobre lo normal: probabilidad 2 y gravedad 3. "
     "Estimación de ejemplo de la posible fuga: 10 kg de producto por hora durante 8 horas; costo medio de $420 por kg.")
build(
    O3, 1, F,
    use="Aprenderé qué significa verificar el funcionamiento de equipos con una ronda, qué son las pérdidas operacionales y qué se informa, y entenderé que mantener, calibrar o reparar lo hace solo personal formado y autorizado.",
    prior=["Sé qué es un peligro, un riesgo y una lista de verificación.", "Sé calcular el puntaje de riesgo.", "Sé multiplicar números enteros."],
    explain=[
        "En Química Industrial, verificar el funcionamiento de un equipo es observarlo con una lista de verificación para detectar señales de que algo falla: ruidos o vibraciones anormales, temperaturas distintas de lo normal, manchas o goteras, alarmas. Una pérdida operacional es producto, energía o tiempo que se pierde por una falla o por un mal funcionamiento, como una fuga que desperdicia producto o una parada que detiene la producción.",
        "Lo que se observa se informa con un aviso de falla, un documento que indica el equipo, lo observado, la hora y quién informa, para que mantención actúe. El mantenimiento básico, como limpiezas externas, revisiones visuales o lubricaciones simples indicadas en el plan, lo realiza personal formado y autorizado con el procedimiento; la calibración la hace un técnico autorizado. Aquí no se enseña ninguna de esas tareas.",
        f"Ante una posible fuga, una mancha desconocida o un olor extraño, no se acerca nadie sin formación: se aleja y avisa. {EMER} {AVISO}",
    ],
    vocab=[("verificar el funcionamiento", "observar un equipo con una lista para detectar señales de falla"), ("pérdida operacional", "producto, energía o tiempo que se pierde por una falla"), ("aviso de falla", "documento que informa el equipo, lo observado, la hora y quién informa"), ("mantenimiento básico", "tareas simples del plan que hace personal formado y autorizado"), ("calibración", "comparación de un instrumento con un patrón, a cargo de un técnico autorizado"), ("posible fuga", "señal de que un equipo podría estar perdiendo producto")],
    worked=[
        ("Pérdida de producto", "Una posible fuga de ejemplo pierde 5 kg por hora durante 6 horas. ¿Cuántos kg se pierden?", ["Se multiplican los kg por hora por las horas.", "5 por 6 son 30."], "30 kg"),
        ("Costo de la pérdida", "Con un costo de ejemplo de $300 por kg, ¿cuánto valen esos 30 kg?", ["Se multiplican los kg por el costo por kg.", "30 por 300 son 9.000."], "$9.000"),
    ],
    mistakes=[("Acercarse a mirar de cerca una mancha húmeda bajo una brida «para saber qué es».", "Puede ser una fuga de una sustancia peligrosa y acercarse sin formación es riesgoso.", "Mantén la distancia, avisa al jefe de turno y a emergencias, y anota lo que viste desde lejos."),
              ("Intentar apretar o reparar una brida que gotea.", "Intervenir un equipo es tarea del personal autorizado.", "Informa con un aviso de falla y no toques el equipo.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una pérdida operacional?", "Producto, energía o tiempo que se pierde por una falla o mal funcionamiento", "El sueldo de un operador", "El valor del equipo nuevo", "La pérdida operacional es lo que se pierde por operar mal o con fallas."),
        ("abc", "En Química Industrial: ¿qué es un aviso de falla?", "Un documento que informa el equipo, lo observado, la hora y quién informa", "Una orden para apagar la planta", "Un manual del fabricante", "El aviso informa a mantención para que actúe."),
        ("abc", "En Química Industrial: ¿quién calibra los instrumentos de la planta?", "Un técnico autorizado", "El operador que los lee", "Un estudiante en práctica", "La calibración es tarea del técnico autorizado."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la posible fuga?", "3*5", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} Según la matriz, ¿qué señal se atiende primero?", "La posible fuga, con 15 puntos", "El ruido anormal, con 9 puntos", "La temperatura sobre lo normal, con 6 puntos", "Se prioriza siempre el hallazgo de mayor puntaje."),
        ("=", "{F} ¿Cuántos kg de producto se perderían por la posible fuga en 8 horas?", "10*8", "Se multiplican los kg por hora por las horas.", " kg"),
        ("=", "{F} ¿Cuánto valen esos kg de producto al costo medio?", "10*8*420", "Se multiplican los kg perdidos por el costo por kg.", " pesos"),
        ("abc", "{F} Quien hace la ronda ve la mancha bajo la brida del reactor R-1. ¿Qué corresponde?", "No acercarse a la zona de riesgo, anotar lo observado desde lejos y avisar al jefe de turno y a emergencias", "Acercarse a oler la mancha", "Limpiar la mancha con lo que tenga a mano", "Una posible fuga no se atiende sin formación."),
        ("abc", "{F} ¿Qué se anota en el aviso de falla por el ruido de la bomba P-1?", "El equipo, el ruido observado, la hora y quién informa", "Solo el nombre de la bomba", "La opinión del operador sobre el fabricante", "El aviso debe llevar los cuatro datos."),
        ("abc", "{F} Un compañero propone «apretar la brida» del reactor para detener la mancha. ¿Qué corresponde?", "Rechazarlo: intervenir el equipo es tarea del personal autorizado", "Aceptarlo si lleva guantes", "Aceptarlo si el reactor está en marcha", "Ajustar o reparar un equipo exige formación y autorización."),
        ("=", "{F} Si la temperatura normal de E-1 es 50 °C, ¿qué lectura tiene ahora?", "50+5", "Se suma la diferencia a la temperatura normal.", " °C"),
        ("abc", "{F} ¿Por qué se verifican los equipos con una lista?", "Para no olvidar señales de falla y poder compararlas entre rondas", "Para reemplazar el mantenimiento", "Para evitar escribir avisos", "La lista ordena la observación y evita olvidos."),
        em("Haces una ronda de verificación de ejemplo cuando ves que de la brida del reactor R-1 sale un chorro de vapor y se siente un olor fuerte.", 4),
    ],
    ctx=("abc", "Un técnico de ejemplo te pide sostener una llave mientras él aprieta la brida del reactor R-1 que gotea. No tienes formación. ¿Qué respondes?", "Que no, porque participar en una reparación exige formación y autorización, y que avisarás a un adulto responsable", "Que sí, si solo sostienes la llave", "Que sí, si el reactor está apagado", "Estar cerca de una brida con fuga es riesgoso sin formación."),
    sc=[
        ("En Química Industrial: ¿qué es verificar el funcionamiento de un equipo?", "Observarlo con una lista para detectar señales de falla", "Se observa sin intervenir el equipo."),
        ("En Química Industrial: ¿qué se hace al ver una mancha bajo una brida?", "No acercarse y avisar al jefe de turno y a emergencias", "Puede ser una fuga y no se atiende sin formación."),
        ("¿Cómo se calcula el valor de una pérdida de producto?", "Kg perdidos por el costo por kg", "Se multiplica la cantidad por su precio."),
    ],
    op=("Ronda ficticia de «Química Demo Costa Norte»: bomba P-2 con vibración anormal (probabilidad 3, gravedad 3), válvula con goteo (probabilidad 4, gravedad 4) y un manómetro con lectura distinta de la normal (probabilidad 2, gravedad 2). El goteo pierde 4 kg por hora durante 5 horas; costo medio de $200 por kg. Escribe (a) los puntajes y cuál se atiende primero, (b) cuántos kg se pierden por el goteo, (c) cuánto valen, (d) qué debe hacer quien hace la ronda ante el goteo.",
        "(a) Vibración: 9; goteo: 16; manómetro: 4; se atiende primero el goteo. (b) 4 por 5 son 20 kg. (c) 20 por 200 son 4.000 pesos. (d) No acercarse a la zona de riesgo, anotar lo observado desde lejos y avisar al jefe de turno y a emergencias.",
        ["calcula los puntajes y prioriza", "calcula la pérdida", "calcula el valor", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar probabilidad por gravedad", "acercarse al goteo", "intervenir el equipo"],
        "Pregunta: «¿quién repara la válvula y qué debe hacer quien la observa?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una ronda con tres señales de falla, calcula sus puntajes y escribe un aviso de falla.",
    extend="Explica con un ejemplo por qué una pequeña fuga también es una pérdida operacional.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Registro mensual del compresor C-1 de la planta ficticia «Química Demo Valle Claro»: horas programadas de operación del mes, 500. Parada programada (mantención preventiva): 10 horas. "
     "Paradas no programadas (por fallas): 5 horas, 6 horas y 4 horas. Costo de ejemplo de una hora de parada no programada: $20.000 de producción perdida. "
     "Orden de trabajo de mantención (OT): documento que autoriza y registra un trabajo de mantención, con prioridad y plazo. Disponibilidad (%) = horas operadas × 100 ÷ horas programadas. "
     "Bloqueo y etiquetado: medida de seguridad que impide que un equipo se encienda mientras se interviene; solo la aplican personas autorizadas.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos y documentos del seguimiento de equipos: paradas programadas y no programadas, disponibilidad, orden de trabajo, aviso de falla y bloqueo y etiquetado, y a calcular con números enteros.",
    prior=["Sé qué es una pérdida operacional.", "Sé calcular porcentajes.", "Sé sumar y restar números enteros."],
    explain=[
        "En Química Industrial, una parada programada es la que se planifica, como una mantención preventiva; una parada no programada ocurre por una falla y es una pérdida operacional. Las horas operadas son las horas programadas menos las horas de parada. La disponibilidad es el porcentaje de las horas programadas en que el equipo estuvo operando: horas operadas por 100 entre horas programadas.",
        "La orden de trabajo de mantención, u OT, autoriza y registra un trabajo con su prioridad y plazo; se genera a partir de un aviso de falla o del plan preventivo. El bloqueo y etiquetado es una medida de seguridad que impide que un equipo se encienda mientras se interviene; este cuaderno solo lo nombra, y únicamente lo aplican personas formadas y autorizadas.",
        f"Aquí se leen y calculan registros en papel; intervenir equipos es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("parada programada", "parada planificada, como una mantención preventiva"), ("parada no programada", "parada por una falla, que es una pérdida operacional"), ("horas operadas", "horas programadas menos las horas de parada"), ("disponibilidad", "horas operadas por 100 entre horas programadas"), ("orden de trabajo (OT)", "documento que autoriza y registra un trabajo de mantención"), ("bloqueo y etiquetado", "medida que impide que un equipo se encienda mientras se interviene, aplicada solo por personas autorizadas")],
    worked=[
        ("Horas operadas", "Un equipo de ejemplo tiene 200 horas programadas, 8 de parada programada y 12 de paradas no programadas. ¿Cuántas horas operó?", ["Las paradas suman 8 más 12, es decir, 20 horas.", "200 menos 20 son 180."], "180 horas"),
        ("Disponibilidad", "Otro equipo de ejemplo con 200 horas programadas operó 180 horas. ¿Cuál es su disponibilidad?", ["Se multiplica 180 por 100 y se divide entre 200.", "18.000 entre 200 son 90."], "90 %"),
    ],
    mistakes=[("Contar solo las paradas no programadas al calcular las horas operadas.", "También las paradas programadas restan horas de operación.", "Resta todas las paradas a las horas programadas."),
              ("Creer que quien conoce el bloqueo y etiquetado puede aplicarlo.", "Solo lo aplican personas formadas y autorizadas.", "Informa y deja que el personal autorizado lo aplique.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una parada no programada?", "Una parada por una falla, que es una pérdida operacional", "Una parada planificada para mantención", "El fin del turno", "No estaba planificada y detiene la producción."),
        ("abc", "En Química Industrial: ¿qué es una orden de trabajo de mantención?", "Un documento que autoriza y registra un trabajo de mantención", "Un plano del equipo", "Una factura del fabricante", "La OT registra qué se hace, cuándo y con qué prioridad."),
        ("abc", "En Química Industrial: ¿para qué sirve el bloqueo y etiquetado?", "Para impedir que un equipo se encienda mientras se interviene", "Para aumentar la producción", "Para calibrar los instrumentos", "Es una medida de seguridad aplicada por personal autorizado."),
        ("=", "{F} ¿Cuántas horas de paradas no programadas tuvo el compresor?", "5+6+4", "Se suman las horas de cada parada por falla.", " horas"),
        ("=", "{F} ¿Cuántas horas de parada, programadas y no programadas, tuvo en total?", "10+5+6+4", "Se suman las paradas programadas y las no programadas.", " horas"),
        ("=", "{F} ¿Cuántas horas operó el compresor?", "500-10-5-6-4", "Se restan todas las paradas a las horas programadas.", " horas"),
        ("=", "{F} ¿Cuál fue la disponibilidad del compresor?", "475*100//500", "Se multiplica las horas operadas por 100 y se divide entre las programadas.", " %"),
        ("=", "{F} ¿Cuánto costó la producción perdida por las paradas no programadas?", "15*20000", "Se multiplican las horas no programadas por el costo de cada hora.", " pesos"),
        ("abc", "{F} ¿Qué tipo de parada fue la mantención preventiva de 10 horas?", "Una parada programada", "Una parada no programada", "Una orden de trabajo", "Estaba planificada en el plan de mantención."),
        ("abc", "{F} ¿Qué documento autoriza y registra un trabajo de mantención, según la ficha?", "La orden de trabajo (OT)", "El aviso de falla", "La hoja de datos de seguridad", "La ficha define la OT con ese propósito."),
        ("abc", "{F} Un operador propone aplicar él mismo el bloqueo y etiquetado «para trabajar tranquilo» en el compresor. ¿Qué corresponde?", "Rechazarlo: solo lo aplican personas formadas y autorizadas", "Aceptarlo si lo hace con cuidado", "Aceptarlo si el equipo está apagado", "El bloqueo y etiquetado exige formación y autorización."),
        ("=", "{F} Si las paradas no programadas hubieran sido solo 5 horas, ¿cuántas horas habría operado?", "500-10-5", "Se restan la parada programada y las 5 horas no programadas.", " horas"),
        em("Lees el registro del compresor de ejemplo en la oficina cuando alguien avisa que el compresor C-1 echa chispas y que se oye un golpe fuerte con olor a quemado.", 5),
    ],
    ctx=("abc", "Un supervisor de ejemplo te dice: «No anotes la parada de 6 horas como falla; anótala como programada». ¿Qué respondes?", "Que no: se anota como no programada porque fue una falla", "Que sí, si mejora la disponibilidad", "Que sí, si se anota con lápiz", "Cambiar el tipo de parada oculta pérdidas y vuelve falso el registro."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula la disponibilidad?", "Horas operadas por 100 entre horas programadas", "Es el porcentaje del tiempo en que operó el equipo."),
        ("En Química Industrial: ¿qué diferencia hay entre parada programada y no programada?", "La programada se planifica y la no programada ocurre por una falla", "La no programada es una pérdida operacional."),
        ("En Química Industrial: ¿quién aplica el bloqueo y etiquetado en una planta?", "Personas formadas y autorizadas", "Es una medida de seguridad con riesgo."),
    ],
    op=("Registro ficticio de «Química Demo Costa Norte»: equipo con 400 horas programadas, 10 horas de mantención preventiva y paradas por fallas de 10 y 20 horas; costo de $15.000 por hora de parada no programada. Escribe (a) cuántas horas operó, (b) la disponibilidad, (c) el costo de las paradas no programadas, (d) por qué una parada por falla es una pérdida operacional.",
        "(a) 400 menos 10, 10 y 20 son 360 horas. (b) 360 por 100 entre 400 son 90 %. (c) 30 por 15.000 son 450.000 pesos. (d) Porque detiene la producción y se pierden producto, tiempo y dinero.",
        ["calcula las horas operadas", "expresa la disponibilidad", "calcula el costo", "explica la pérdida operacional"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la parada programada", "dividir al revés", "no multiplicar por el costo"],
        "Pregunta: «¿qué paradas restan horas de operación?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un registro mensual de un equipo con horas programadas, paradas y costos, y calcula la disponibilidad.",
    extend="Explica con un ejemplo por qué una parada programada suele ser mejor que una no programada.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Registro de 3 días de la planta ficticia «Química Demo Valle Claro» (kg por día). Día 1: entradas 5.000; producto 4.700; residuos registrados 150. Día 2: entradas 5.000; producto 4.800; residuos registrados 150. "
     "Día 3: entradas 4.000; producto 3.760; residuos registrados 120. Diferencia no explicada = entradas − producto − residuos registrados. Regla de aviso de ejemplo: se informa si la diferencia es mayor que el 2 % de las entradas. Costo medio de ejemplo: $400 por kg. "
     "Causas posibles (solo como lista general para el especialista): fugas, errores de pesaje, producto retenido en equipos o errores de registro.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un registro diario de balance para detectar posibles pérdidas operacionales: calcular la diferencia no explicada, compararla con una regla de aviso, valorizarla e informar al especialista.",
    prior=["Sé qué es el balance de masa.", "Sé calcular porcentajes.", "Sé qué es una pérdida operacional."],
    explain=[
        "En Química Industrial, la diferencia no explicada de un día es lo que entró menos el producto y los residuos registrados. Si es cero, el balance cierra; si es positiva, hay masa que no se sabe a dónde fue, y puede ser una pérdida operacional. El porcentaje de la diferencia se calcula con el valor de entrada: diferencia por 100 entre entradas. La regla de aviso fija desde qué porcentaje se informa.",
        "La diferencia se puede valorizar multiplicando los kg por el costo medio. Las causas posibles, como fugas, errores de pesaje, producto retenido en equipos o errores de registro, las investiga el personal autorizado y el especialista; quien registra no inspecciona equipos por cuenta propia ni se acerca a posibles fugas. Informa los datos y espera instrucciones.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("diferencia no explicada", "entradas menos producto y residuos registrados"), ("regla de aviso", "porcentaje desde el cual se informa al especialista"), ("valorizar una pérdida", "calcular cuánto cuesta multiplicando los kg por el costo por kg"), ("causa posible", "explicación que debe investigar el personal autorizado"), ("balance que cierra", "balance en que la diferencia no explicada es cero")],
    worked=[
        ("Diferencia no explicada", "Un día de ejemplo entran 1.000 kg y salen 900 kg de producto y 60 kg de residuos. ¿Cuál es la diferencia no explicada?", ["Salen 900 más 60, es decir, 960 kg.", "1.000 menos 960 son 40."], "40 kg"),
        ("Aplicar la regla", "Con una regla de aviso del 3 %, ¿se informa esa diferencia de 40 kg sobre 1.000 kg?", ["40 por 100 entre 1.000 son 4 %.", "4 % es mayor que 3 %, así que se informa."], "Sí, se informa"),
    ],
    mistakes=[("Ignorar una diferencia pequeña porque «es poco».", "Pequeñas diferencias repetidas suman pérdidas grandes y pueden indicar una fuga.", "Aplica la regla de aviso y registra todas las diferencias."),
              ("Acercarse a revisar los equipos para encontrar la causa de la diferencia.", "Investigar equipos es tarea del personal autorizado.", "Informa los datos y espera instrucciones.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la diferencia no explicada de un día?", "Lo que entró menos el producto y los residuos registrados", "El producto menos los residuos", "El costo de las materias", "Es la masa que no se sabe a dónde fue."),
        ("abc", "En Química Industrial: ¿qué es una regla de aviso?", "El porcentaje desde el cual se informa al especialista", "La cantidad de turnos del día", "El costo de cada kg", "Fija desde qué valor hay que informar al especialista."),
        ("abc", "En Química Industrial: ¿quién investiga las causas de una pérdida?", "El personal autorizado y el especialista", "Cualquier persona que pase por la planta", "El cliente", "La investigación exige formación y autorización."),
        ("=", "{F} ¿Cuál es la diferencia no explicada del día 1?", "5000-4700-150", "Se restan el producto y los residuos a las entradas.", " kg"),
        ("=", "{F} ¿Cuál es la diferencia no explicada del día 2?", "5000-4800-150", "Se restan el producto y los residuos a las entradas.", " kg"),
        ("=", "{F} ¿Cuál es la diferencia no explicada del día 3?", "4000-3760-120", "Se restan el producto y los residuos a las entradas.", " kg"),
        ("=", "{F} ¿Qué porcentaje de las entradas es la diferencia del día 1?", "150*100//5000", "Se divide la diferencia entre las entradas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de las entradas es la diferencia del día 2?", "50*100//5000", "Se divide la diferencia entre las entradas y se multiplica por 100.", " %"),
        ("abc", "{F} Con la regla de aviso del 2 %, ¿qué días se informan?", "Los días 1 y 3, con 3 %", "Solo el día 2", "Ninguno, porque son pocos kg", "Los días 1 y 3 superan el 2 %."),
        ("=", "{F} ¿Cuánto vale la diferencia no explicada del día 1 al costo medio?", "150*400", "Se multiplican los kg por el costo por kg.", " pesos"),
        ("abc", "{F} Un auxiliar dice: «el día 2 tuvo 50 kg de diferencia, no hay que anotarlo». ¿Qué corresponde?", "Anotarlo igual, aunque no supere la regla de aviso", "No anotarlo, porque es poco", "Anotarlo solo si hay una fuga", "Todas las diferencias se registran, aunque sean pequeñas."),
        ("abc", "{F} Un operario propone revisar de cerca las bridas del reactor para encontrar la causa. ¿Qué corresponde?", "Rechazarlo: informar los datos y dejar la investigación al personal autorizado", "Aceptarlo si lleva guantes", "Aceptarlo si el equipo está detenido", "Investigar equipos sin formación puede ser peligroso."),
        em("Analizas el registro de balance de ejemplo cuando alguien avisa que hay un charco con olor fuerte junto al reactor y que se siente irritación en los ojos.", 0),
    ],
    ctx=("abc", "Una jefatura de ejemplo dice: «Anota que el día 1 el producto fue 4.850 kg, así cierra el balance». ¿Qué respondes?", "Que no: se anota el producto realmente obtenido, 4.700 kg, y se informa la diferencia", "Que sí, si el balance cierra con ese dato", "Que sí, si se corrige después", "Un dato inventado oculta una pérdida."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula la diferencia no explicada?", "Entradas menos producto y menos residuos", "La diferencia muestra lo que no cierra del balance."),
        ("En Química Industrial: ¿cómo se valoriza una pérdida?", "Kg perdidos por el costo por kg", "El resultado indica cuánto se perdió en dinero."),
        ("¿Se anotan las diferencias pequeñas?", "Sí, todas se anotan", "Muchas diferencias pequeñas pueden indicar un problema."),
    ],
    op=("Registro ficticio de «Química Demo Costa Norte»: día A: entradas 2.000 kg, producto 1.880 kg, residuos 60 kg; día B: entradas 2.000 kg, producto 1.900 kg, residuos 80 kg; regla de aviso del 2 %; costo de $300 por kg. Escribe (a) la diferencia no explicada de cada día, (b) qué días se informan, (c) el valor de la diferencia mayor, (d) quién investiga la causa.",
        "(a) Día A: 60 kg; día B: 20 kg. (b) El día A, porque 60 por 100 entre 2.000 son 3 %, mayor que 2 %; el día B tiene 1 % y no se informa, pero igual se anota. (c) 60 por 300 son 18.000 pesos. (d) El personal autorizado y el especialista.",
        ["calcula las diferencias", "aplica la regla de aviso", "valoriza la mayor", "nombra a quien investiga"],
        ["hoja con las cuatro respuestas"],
        ["restar solo uno de los componentes", "no anotar las diferencias pequeñas", "investigar por cuenta propia"],
        "Pregunta: «¿cuántos kg salen en total cada día?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un registro de dos días con entradas y salidas y calcula la diferencia no explicada de cada uno.",
    extend="Explica con un ejemplo por qué pequeñas diferencias repetidas pueden indicar una fuga.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada) de «Química Demo Valle Claro». Órdenes de trabajo abiertas: OT-1, posible fuga en una brida, probabilidad 3 y gravedad 5; OT-2, ruido anormal en una bomba, probabilidad 3 y gravedad 3; OT-3, sensor de presión con lectura de 104 kPa frente a un patrón de 100 kPa, probabilidad 2 y gravedad 3; "
     "OT-4, limpieza externa de un filtro, probabilidad 4 y gravedad 1. Regla de plazos de ejemplo: puntaje de 12 o más, plazo de 1 día; de 8 a 11, 3 días; menos de 8, 7 días. Tolerancia del sensor de ejemplo: ±3 % del patrón. "
     "La posible fuga pierde 12 kg por hora (de ejemplo); costo medio de $400 por kg.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar criterios de seguimiento con datos de ejemplo: priorizar órdenes de trabajo, calcular el error relativo de un instrumento y valorizar una pérdida mientras no se atiende, y a informar sin intervenir equipos.",
    prior=["Sé calcular el puntaje de riesgo y el error relativo.", "Sé qué es una orden de trabajo.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "En Química Industrial, las órdenes de trabajo de mantención se priorizan con el puntaje de riesgo: probabilidad por gravedad. A mayor puntaje, menor plazo para atenderla. La regla de plazos de ejemplo fija 1 día para 12 puntos o más, 3 días para 8 a 11 y 7 días para menos de 8. Quien da seguimiento informa las prioridades; la atención de cada orden la hace personal autorizado.",
        "El error relativo de un instrumento es el error absoluto por 100 entre el valor del patrón; si supera la tolerancia, el instrumento queda fuera de servicio hasta que un técnico autorizado lo calibre. Mientras una fuga no se atiende, se sigue perdiendo producto: la pérdida se calcula multiplicando los kg por hora por las horas y por el costo por kg.",
        f"Todo es cálculo de planilla; no se interviene ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("prioridad de una OT", "orden de atención según su puntaje de riesgo"), ("plazo de atención", "tiempo máximo para atender una orden de trabajo"), ("error relativo", "error absoluto por 100 entre el valor del patrón"), ("tolerancia", "error máximo aceptable de un instrumento"), ("pérdida mientras no se atiende", "producto que se sigue perdiendo hasta que se repara el equipo")],
    worked=[
        ("Plazo según puntaje", "Con la regla de la clase, una OT de ejemplo tiene 9 puntos. ¿Qué plazo corresponde?", ["De 8 a 11 puntos el plazo es de 3 días.", "9 está en ese tramo."], "3 días"),
        ("Pérdida acumulada", "Una fuga de ejemplo pierde 5 kg por hora y no se atiende durante 10 horas. ¿Cuántos kg se pierden?", ["Se multiplican los kg por hora por las horas.", "5 por 10 son 50."], "50 kg"),
    ],
    mistakes=[("Atender primero la orden más fácil en vez de la de mayor puntaje.", "La prioridad la fija el riesgo, no la facilidad.", "Ordena por puntaje y atiende de mayor a menor."),
              ("Seguir usando un sensor fuera de tolerancia «porque se ve normal».", "Sin tolerancia cumplida, la lectura no es confiable.", "Déjalo fuera de servicio y avisa al técnico.")],
    T=[
        ("abc", "En Química Industrial: ¿cómo se priorizan las órdenes de trabajo?", "Por su puntaje de riesgo, de mayor a menor", "Por el orden de llegada", "Por la facilidad de arreglo", "La prioridad se decide según el riesgo de cada orden."),
        ("abc", "En Química Industrial: ¿qué se hace con un instrumento que supera su tolerancia?", "Se deja fuera de servicio hasta que un técnico lo calibre", "Se sigue usando con cuidado", "Se ajusta sin avisar", "Fuera de tolerancia no es confiable."),
        ("abc", "En Química Industrial: ¿qué es el error relativo?", "El error absoluto por 100 entre el valor del patrón", "La diferencia entre dos patrones", "El costo de la calibración", "Expresa el error como porcentaje del patrón."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene OT-1?", "3*5", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene OT-2?", "3*3", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} ¿Qué plazo corresponde a OT-1 según la regla?", "1 día", "3 días", "7 días", "Con 15 puntos corresponde el plazo más corto."),
        ("abc", "{F} ¿Qué plazo corresponde a OT-2, con 9 puntos?", "3 días", "1 día", "7 días", "De 8 a 11 puntos son 3 días."),
        ("=", "{F} ¿Cuál es el error relativo del sensor de presión de OT-3?", "(104-100)*100//100", "Se divide el error absoluto entre el patrón y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cumple el sensor de OT-3 la tolerancia de ±3 %?", "No, porque su error relativo de 4 % supera el 3 %", "Sí, porque 104 es cercano a 100", "Sí, porque el error es de solo 4 kPa", "El 4 % está fuera de la tolerancia del 3 %."),
        ("=", "{F} ¿Cuántos kg se perderían por la fuga de OT-1 si no se atiende durante las 24 horas de un día?", "12*24", "Se multiplican los kg por hora por las horas.", " kg"),
        ("=", "{F} ¿Cuánto valdría esa pérdida de un día al costo medio?", "12*24*400", "Se multiplican los kg perdidos por el costo por kg.", " pesos"),
        ("abc", "{F} ¿Cuál es el orden de atención de las cuatro órdenes?", "OT-1, OT-2, OT-3 y OT-4", "OT-4, OT-3, OT-2 y OT-1", "OT-2, OT-1, OT-4 y OT-3", "Los puntajes son 15, 9, 6 y 4, de mayor a menor."),
        em("Das seguimiento a las órdenes de trabajo cuando alguien avisa que la brida de OT-1 empezó a lanzar un chorro de líquido y que hay un olor fuerte en la sala.", 1),
    ],
    ctx=("abc", "Un jefe de ejemplo propone atender primero OT-4, la limpieza del filtro, «porque es rápida», y dejar la fuga para después. ¿Qué respondes?", "Que debe atenderse primero la fuga de OT-1, porque tiene el mayor puntaje y el plazo más corto", "Que sí, porque OT-4 es más fácil", "Que sí, si el filtro está sucio", "La prioridad la fija el riesgo."),
    sc=[
        ("En Química Industrial: ¿qué plazo corresponde a 15 puntos con la regla de la clase?", "1 día", "A mayor puntaje de riesgo, menor es el plazo."),
        ("En Química Industrial: ¿cómo se calcula el error relativo?", "Error absoluto por 100 entre el patrón", "Se expresa como porcentaje del patrón."),
        ("¿Cómo se calcula la pérdida de una fuga no atendida?", "Kg por hora por horas, y por costo por kg", "Cada hora sin atender se sigue perdiendo producto."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte»: OT-A, fuga en una válvula (probabilidad 4, gravedad 4); OT-B, vibración en un motor (probabilidad 2, gravedad 4); OT-C, manómetro con lectura de 52 kPa frente a un patrón de 50 kPa, tolerancia de ±3 %; la fuga pierde 6 kg por hora y cuesta $300 por kg. Con la regla de plazos de la clase, escribe (a) los puntajes y el plazo de OT-A y OT-B, (b) el error relativo de OT-C y si cumple, (c) cuántos kg y cuánto dinero pierde la fuga en 12 horas, (d) qué debe hacer quien ve la fuga.",
        "(a) OT-A: 16 puntos, plazo de 1 día; OT-B: 8 puntos, plazo de 3 días. (b) 2 por 100 entre 50 son 4 %: no cumple. (c) 6 por 12 son 72 kg; 72 por 300 son 21.600 pesos. (d) No acercarse a la zona de riesgo y avisar al jefe de turno y a emergencias.",
        ["calcula puntajes y plazos", "calcula el error relativo", "calcula la pérdida", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["no usar la regla de plazos", "dividir entre la lectura", "acercarse a la fuga"],
        "Pregunta: «¿respecto de qué valor se divide el error?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa cuatro órdenes de trabajo con probabilidad y gravedad, calcula los puntajes y ordénalas.",
    extend="Explica con un ejemplo por qué el plazo de una OT depende de su puntaje de riesgo.",
)

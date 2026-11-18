"""Mecánica de Mantenimiento de Aeronaves TP (3.º y 4.º medio) módulo C: OAE-06 (inspección visual e instrumentos en sistemas eléctricos y electrónicos, lectura de diagramas e informe oportuno) y OAE-07 (registrar e informar el mantenimiento). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meae_common import AVISO, EMER, build

O6 = "TP-MEAE-3y4-OAE-06"
O7 = "TP-MEAE-3y4-OAE-07"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (matriz de peligros de ejemplo, inventada). El «Hangar Demo de Aviónica» anota: una batería conectada a un tablero, cables con la aislación deteriorada a la vista, una unidad electrónica sensible a la electricidad estática fuera de su envase, "
     "una aeronave con energía eléctrica externa conectada, un recipiente de solvente abierto cerca de un tablero y ruido intenso. Dotación del turno: 12 personas; el hangar tiene 3 puestos de trabajo.")
build(
    O6, 1, F,
    use="Aprenderé qué son los sistemas eléctricos y electrónicos de una aeronave, qué peligros tienen y qué reglas generales los controlan.",
    prior=["Sé leer una matriz de peligros.", "Sé multiplicar y dividir enteros.", "Sé que el trabajo sigue manuales del fabricante."],
    explain=[
        "Los sistemas eléctricos de una aeronave generan, almacenan y distribuyen la electricidad que alimenta los equipos. Los sistemas electrónicos, también llamados aviónica, incluyen los instrumentos, las comunicaciones y la navegación. Su mantenimiento comprende la inspección visual de lo que se ve, la lectura de diagramas del manual, el uso de instrumentos de medición y el informe oportuno de las fallas y discrepancias, según el manual de mantenimiento de la aeronave.",
        "La electricidad puede causar descargas, quemaduras e incendios. Una batería puede dar energía aunque el resto del sistema esté apagado, y algunos componentes guardan carga. Las unidades electrónicas son sensibles a la electricidad estática, que puede dañarlas sin que se note. Un permiso de trabajo, un bloqueo y etiquetado y la regla de que solo personal autorizado interviene son controles administrativos; el EPP es la última barrera.",
        f"Este cuaderno solo estudia los conceptos y no te enseña a intervenir sistemas eléctricos. {EMER} {AVISO}",
    ],
    vocab=[("sistema eléctrico", "conjunto que genera, almacena y distribuye electricidad"), ("aviónica", "sistemas electrónicos de una aeronave: instrumentos, comunicaciones y navegación"), ("electricidad estática", "carga eléctrica acumulada que puede dañar piezas electrónicas"), ("aislación", "cubierta que evita el contacto con un conductor eléctrico"), ("energía externa", "alimentación eléctrica que viene de un equipo fuera de la aeronave"), ("discrepancia", "diferencia entre lo observado y lo que el manual permite")],
    worked=[
        ("Peligro y riesgo", "En un taller de ejemplo hay una herramienta metálica apoyada sobre una batería. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la herramienta metálica sobre la batería.", "El riesgo son chispas o una quemadura."], "Peligro: la herramienta metálica sobre la batería; riesgo: chispas o una quemadura"),
        ("Tipo de control", "Un hangar de ejemplo permite abrir un tablero solo a personas con una autorización escrita. ¿Qué tipo de control es?", ["Una autorización ordena quién puede actuar.", "Es un control administrativo."], "Control administrativo"),
    ],
    mistakes=[("Creer que un sistema apagado no tiene energía.", "Una batería o un componente con carga puede dar energía.", "Trata todo sistema como si tuviera energía hasta que personal autorizado confirme lo contrario."),
              ("Pensar que con guantes se puede tocar un cable.", "El EPP es la última barrera y no habilita para intervenir.", "Solo personal autorizado interviene, con el sistema controlado.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la aviónica?", "Los sistemas electrónicos de una aeronave, como instrumentos, comunicaciones y navegación", "El conjunto de ruedas y frenos de la aeronave", "El combustible que usa el motor", "La aviónica agrupa los sistemas electrónicos."),
        ("abc", "En Mantenimiento de Aeronaves: ¿por qué un sistema eléctrico apagado puede ser peligroso?", "Porque una batería o un componente con carga puede seguir dando energía", "Porque un sistema apagado siempre está conectado a energía externa", "Porque apagado significa que el sistema está en mantenimiento", "Apagado no significa sin energía, pues puede haber carga almacenada."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué daño puede causar la electricidad estática?", "Dañar unidades electrónicas sensibles sin que se note", "Descargar por completo la batería de la aeronave", "Cortar la energía externa del hangar", "La carga estática puede dañar componentes electrónicos sensibles."),
        ("abc", "{F} ¿Qué peligro de la matriz puede causar una descarga eléctrica por contacto?", "Los cables con la aislación deteriorada a la vista", "El ruido intenso", "La unidad electrónica fuera de su envase", "Sin aislación, un conductor energizado puede descargar al contacto."),
        ("abc", "{F} ¿Qué peligro de la matriz puede dañar un componente sin riesgo directo para la persona?", "La unidad electrónica sensible a la estática fuera de su envase", "La batería conectada a un tablero", "El solvente abierto cerca del tablero", "La estática daña la electrónica; los otros peligros pueden lesionar a la persona."),
        ("abc", "{F} Un permiso de trabajo y un bloqueo con etiqueta para el tablero son:", "Controles administrativos", "Controles de ingeniería", "El equipo de protección personal", "Son reglas de trabajo que ordenan la conducta de las personas."),
        ("=", "{F} El hangar asigna 1 persona a cargo de seguridad por cada 4 personas del turno. ¿Cuántas personas se necesitan?", "12//4", "Se divide la dotación entre las personas que cubre cada responsable.", " personas"),
        ("=", "{F} Cada uno de los 3 puestos debe tener 2 etiquetas de bloqueo y el hangar guarda 5 de repuesto. ¿Cuántas etiquetas necesita?", "3*2+5", "Se multiplican los puestos por las etiquetas de cada uno y se suma el repuesto.", " etiquetas"),
        ("=", "Un peligro de ejemplo tiene probabilidad 4 y gravedad 4. Con un control, la probabilidad baja a 1. ¿Cuántos puntos baja el puntaje (probabilidad por gravedad)?", "4*4-1*4", "Se calcula el puntaje antes y después, y se restan.", " puntos"),
        ("abc", "{F} Una persona en práctica dice: «con guantes puestos puedo tocar los cables de la aislación dañada». ¿Qué respuesta es correcta?", "Es falso: el EPP no habilita para intervenir y la tarea es de personal autorizado", "Es cierto, porque los guantes aíslan de todo", "Es cierto, si hay una persona cerca", "El EPP es la última barrera y no reemplaza la autorización."),
        ("abc", "En una visita a un hangar de ejemplo, ves chispas y humo saliendo de un tablero. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a desconectar el tablero", "Echarle agua al tablero", "Acercarse a una descarga o un incendio puede causar otro accidente."),
        ("=", "{F} El peligro de la batería conectada tiene probabilidad 3 y gravedad 5; el del solvente abierto tiene probabilidad 2 y gravedad 4. ¿Cuántos puntos más de puntaje (probabilidad por gravedad) tiene el primero?", "3*5-2*4", "Se calculan los dos puntajes y se restan.", " puntos"),
        ("abc", "{F} Un compañero dice: «el riesgo de la aislación dañada es bajo porque la aeronave está en tierra». ¿Qué observación es correcta?", "Estar en tierra no quita la energía: el riesgo depende de si hay tensión y de la gravedad", "Tiene razón, porque en tierra no hay electricidad", "Tiene razón, porque la aislación no importa", "La energía externa o una batería puede energizar el sistema en tierra."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «toca ese cable y dime si está caliente, yo te cuido». ¿Qué respondes?", "Que no, porque tocar cables exige instructor autorizado y norma vigente, y que avisarás a un adulto responsable", "Que sí, porque ella te cuida", "Que sí, si usas guantes", "Tocar un cable puede causar una descarga; es tarea de personal autorizado."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es la aislación de un cable?", "La cubierta que evita el contacto con el conductor", "Protege de tocar un conductor energizado."),
        ("¿Quién interviene los sistemas eléctricos de una aeronave?", "Personal capacitado y autorizado", "Esa tarea exige autorización y capacitación."),
        ("En Mantenimiento de Aeronaves: ¿qué lugar ocupa el EPP en la jerarquía de controles?", "La última barrera", "El EPP no quita el peligro."),
    ],
    op=("Un hangar de ejemplo anota dos situaciones: (1) una persona en práctica ve cables con la aislación dañada junto a un tablero con energía externa conectada; (2) una unidad electrónica sensible está fuera de su envase sobre una mesa. Escribe (a) el peligro y el riesgo de cada una, (b) un control administrativo, (c) la conducta de la persona en práctica ante la situación 1, (d) por qué el EPP no basta. No describas cómo se interviene.",
        "(a) 1: peligro, cables sin aislación con energía; riesgo, descarga o incendio. 2: peligro, la estática; riesgo, dañar la unidad sin notarlo. (b) Un permiso de trabajo con bloqueo y etiquetado. (c) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. (d) El EPP es la última barrera y no quita el peligro.",
        ["distingue peligro y riesgo", "propone un control administrativo", "responde con conducta de emergencia", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["proponer tocar los cables", "proponer solo el EPP", "describir cómo se interviene"],
        "Pregunta: «¿quién puede actuar y qué debo hacer yo?». Si duda, pídele que relea la conducta de emergencia."),
    reinforce="Escribe tres peligros de los sistemas eléctricos y su riesgo, con una frase para cada uno.",
    extend="Explica con un ejemplo por qué «apagado» no significa «sin energía».",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (diagrama de ejemplo, inventado). Diagrama eléctrico de ejemplo en serie: [Batería B] → [Fusible U] → [Interruptor S] → [Lámpara L] → [Retorno R], que vuelve a B. Leyenda: B batería, U fusible, S interruptor, L lámpara, R retorno. "
     "Instrumento de ejemplo: un multímetro mide tensión en volts (V), corriente en amperes (A) y resistencia en ohms (Ω). Valores de ejemplo: la batería entrega 24 V.")
build(
    O6, 2, F,
    use="Aprenderé qué se mira en una inspección visual, qué miden los instrumentos y cómo se lee un diagrama eléctrico sencillo.",
    prior=["Sé leer un esquema con flechas.", "Sé qué es una leyenda.", "Sé que informar con datos es parte del trabajo."],
    explain=[
        "La inspección visual busca, con la vista y sin tocar, señales de problema: aislación dañada o quemada, decoloración por calor, corrosión en conectores, conectores o abrazaderas flojos, cables rozados y suciedad o humedad. Lo que se ve se compara con el manual y se registra. Una discrepancia es una diferencia con lo permitido, y una falla es el mal funcionamiento de un componente.",
        "Los instrumentos miden magnitudes: la tensión, en volts (V), es la fuerza que empuja la corriente; la corriente, en amperes (A), es cuánta electricidad circula; la resistencia, en ohms (Ω), es la dificultad que opone un componente. Un diagrama eléctrico usa símbolos con una leyenda: batería, fusible, interruptor, lámpara y retorno. En un circuito en serie la corriente pasa por todos los componentes uno tras otro: si uno se abre, el resto no recibe corriente.",
        f"Usar un instrumento en un sistema real exige formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("inspección visual", "revisión con la vista, sin tocar, de señales de problema"), ("tensión (V)", "fuerza que empuja la corriente, medida en volts"), ("corriente (A)", "cantidad de electricidad que circula, medida en amperes"), ("resistencia (Ω)", "dificultad que opone un componente, medida en ohms"), ("fusible", "componente que se abre para proteger un circuito de un exceso de corriente"), ("circuito en serie", "circuito donde la corriente pasa por todos los componentes uno tras otro"), ("falla", "mal funcionamiento de un componente")],
    worked=[
        ("Magnitud", "Un instrumento de ejemplo mide la cantidad de electricidad que circula. ¿Qué magnitud mide y en qué unidad?", ["La cantidad que circula es la corriente.", "Se mide en amperes."], "Corriente, en amperes (A)"),
        ("Circuito en serie", "En un circuito en serie de ejemplo con tres componentes P, Q y R, se abre Q. ¿Qué pasa con R?", ["En serie la corriente pasa por todos.", "Si Q se abre, R deja de recibir corriente."], "R deja de recibir corriente"),
    ],
    mistakes=[("Confundir tensión con corriente.", "La tensión empuja; la corriente es lo que circula.", "Recuerda que volts miden tensión y amperes miden corriente."),
              ("Tocar para «revisar» una señal de calentamiento.", "La inspección visual se hace sin tocar y con el sistema controlado.", "Mira, registra e informa; no toques.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué busca una inspección visual?", "Señales de problema que se ven, sin tocar, como aislación dañada o conectores flojos", "Solo el funcionamiento de los instrumentos al encender el sistema", "La resistencia de cada componente con un multímetro", "La inspección visual detecta lo que se ve."),
        ("abc", "En Mantenimiento de Aeronaves: ¿en qué unidad se mide la resistencia?", "En ohms (Ω)", "En volts (V)", "En amperes (A)", "La resistencia se mide en ohms."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué hace un fusible?", "Se abre para proteger el circuito de un exceso de corriente", "Aumenta la tensión de la batería", "Enciende la lámpara", "El fusible es una protección que se abre."),
        ("abc", "{F} ¿Qué componente está justo después del fusible U en el diagrama?", "El interruptor S", "La lámpara L", "La batería B", "El orden es B, U, S, L y R."),
        ("abc", "{F} ¿Qué símbolo de la leyenda representa a la lámpara?", "L", "S", "U", "La leyenda indica que L es la lámpara."),
        ("abc", "{F} ¿Qué mide un multímetro en volts?", "La tensión", "La corriente", "La resistencia", "La unidad volt corresponde a la magnitud llamada tensión."),
        ("=", "{F} Cada uno de los 5 símbolos del diagrama lleva 2 anotaciones en una planilla de ejemplo. ¿Cuántas anotaciones hay?", "5*2", "Se multiplican los símbolos por las anotaciones de cada uno.", " anotaciones"),
        ("=", "En un diagrama de ejemplo en serie hay 6 componentes y se revisa cada uno 3 veces en papel. ¿Cuántas revisiones suman?", "6*3", "Se multiplican los componentes por las revisiones de cada uno.", " revisiones"),
        ("=", "{F} El rango esperado de la batería de la ficha va desde 1 V bajo sus 24 V hasta 1 V sobre ellos. ¿Cuántos volts es el máximo del rango?", "24+1", "Se suma 1 V a la tensión de 24 V.", " V"),
        ("abc", "{F} Una persona dice: «si el fusible U se abre, la lámpara L sigue encendida porque está lejos». ¿Qué observación es correcta?", "Es falsa: en serie, si U se abre, L deja de recibir corriente", "Es correcta, porque L está lejos del fusible", "Es correcta, porque la batería la alimenta de otra forma", "En un circuito en serie, un componente abierto corta la corriente al resto."),
        ("abc", "{F} Una persona en práctica ve un cable con la cubierta quemada y propone tocarlo para ver si está caliente. ¿Qué corresponde?", "No tocarlo: registrar lo observado e informar a personal autorizado", "Tocarlo con un dedo, solo un momento", "Cortar la zona quemada", "La inspección visual es sin tocar y el informe va a personal autorizado."),
        ("abc", "Una persona anota «cable raro cerca del tablero». ¿Qué problema tiene esa anotación?", "Es vaga: no dice qué se vio, dónde ni qué señal tenía", "Ninguno, porque basta con avisar", "Que es muy larga", "Una anotación útil describe lo observado y su ubicación."),
        ("=", "{F} Un diagrama de ejemplo parecido tiene 8 símbolos y el de la ficha tiene 5. ¿Cuántos símbolos más tiene?", "8-5", "Se resta el total de la ficha al del otro diagrama.", " símbolos"),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona te dice: «toca el conector, si está caliente es que hay problema». ¿Qué respondes?", "Que la inspección visual es sin tocar, que informarás lo que ves y que consultarás a un adulto responsable", "Que sí, porque es rápido", "Que sí, si usas guantes", "Tocar un conector energizado puede causar una descarga."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué miden los amperes?", "La corriente", "Los amperes miden cuánta electricidad circula."),
        ("¿Qué pasa en un circuito en serie si un componente se abre?", "El resto deja de recibir corriente", "La corriente pasa por todos uno tras otro."),
        ("¿Cómo se hace una inspección visual?", "Mirando, sin tocar, y registrando lo observado", "Es una revisión con la vista."),
    ],
    op=("Diagrama de ejemplo en serie: [Batería B] → [Fusible F1] → [Interruptor S1] → [Equipo E1] → [Retorno R1]. Leyenda: B batería, F1 fusible, S1 interruptor, E1 equipo, R1 retorno. Escribe (a) cuántos componentes hay, (b) qué componentes están antes de E1, (c) qué pasa con E1 si F1 se abre, (d) qué anotas si ves una aislación quemada, sin tocarla.",
        "(a) 5 componentes. (b) B, F1 y S1. (c) E1 deja de recibir corriente, porque es un circuito en serie. (d) Qué vi, dónde, y la señal observada («aislación quemada, cerca del equipo E1»), y lo informo a personal autorizado.",
        ["cuenta los componentes", "identifica los anteriores", "explica el efecto en serie", "anota con datos sin tocar"],
        ["hoja con las cuatro respuestas"],
        ["contar mal", "decir que E1 sigue recibiendo corriente", "proponer tocar la aislación"],
        "Pregunta: «¿qué hay antes de E1 en la línea?». Si duda, pídele que relea el circuito en serie."),
    reinforce="Dibuja un circuito en serie de cuatro componentes con leyenda y escribe qué ocurre si se abre el segundo.",
    extend="Explica con un ejemplo por qué una anotación vaga no sirve para informar.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (planilla de lecturas de ejemplo, inventada). Circuito de ejemplo en serie con puntos de lectura: P1 (salida de la batería), P2 (después del fusible), P3 (después del interruptor), P4 (después de la lámpara). "
     "Rango esperado de tensión en cada punto: de 23 a 25 V (valores de ejemplo). Lecturas registradas por una persona autorizada: P1: 24 V; P2: 24 V; P3: 12 V; P4: 0 V. Candidatos de ejemplo entre P2 y P3: solo el interruptor.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel una planilla de lecturas: ver dónde cambia el valor, listar candidatos y escribir un informe sin afirmar una causa.",
    prior=["Sé leer un circuito en serie.", "Sé comparar un valor con un rango.", "Sé distinguir síntoma, candidato y causa."],
    explain=[
        "Una planilla de lecturas anota la tensión en varios puntos de un circuito. Cada lectura se compara con el rango esperado del manual. En un circuito en serie, el valor normal se mantiene hasta el punto donde algo cambia. El primer punto con una lectura fuera de rango muestra que el cambio ocurrió antes de ese punto y después del punto anterior bueno. Los componentes que están entre esos dos puntos son los candidatos a causa.",
        "Un candidato no es una causa confirmada. La causa se establece con pruebas y verificación de personal autorizado. En el informe se escribe: la lectura, el rango, el punto anterior bueno, el primer punto malo, los candidatos y lo que no se sabe. No se afirma «el interruptor está malo», sino «el interruptor es un candidato». Quien analiza la planilla no mide ni repara: informa.",
        f"El análisis es solo en papel. {EMER} {AVISO}",
    ],
    vocab=[("planilla de lecturas", "tabla con los valores medidos en distintos puntos"), ("rango esperado", "intervalo de valores normales según el manual"), ("punto de lectura", "lugar del circuito donde se anota un valor"), ("candidato a causa", "componente que podría explicar el síntoma y aún no está confirmado"), ("causa confirmada", "causa establecida con pruebas autorizadas")],
    worked=[
        ("Primer punto fuera de rango", "Lecturas de ejemplo con rango de 10 a 12 V: Q1 11 V, Q2 11 V, Q3 5 V, Q4 0 V. ¿Cuál es el primer punto fuera de rango?", ["Q1 y Q2 están dentro.", "Q3 es el primer fuera de rango."], "Q3"),
        ("Candidatos", "Con las lecturas anteriores, ¿dónde están los candidatos?", ["El último punto bueno es Q2 y el primero malo es Q3.", "Están los componentes entre Q2 y Q3."], "Los componentes entre Q2 y Q3"),
    ],
    mistakes=[("Escribir «el interruptor está malo» sin pruebas autorizadas.", "Un candidato no es una causa confirmada.", "Escribe «el interruptor es un candidato»."),
              ("Mirar solo el último punto con 0 V.", "El cambio pudo ocurrir antes; el primer punto fuera de rango es lo que ubica el cambio.", "Busca el primer punto fuera de rango.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un rango esperado?", "El intervalo de valores normales según el manual", "El valor más alto que se ha medido alguna vez", "El promedio de dos lecturas cualquiera", "El manual fija el intervalo normal de cada lectura."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué ubica el primer punto con una lectura fuera de rango?", "Que el cambio ocurrió entre el último punto bueno y ese punto", "Que todos los componentes están dañados", "Que el instrumento está malo siempre", "El cambio está entre el punto anterior bueno y el primer punto malo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un candidato a causa?", "Un componente que podría explicar el síntoma y aún no está confirmado", "La causa ya comprobada", "El instrumento que midió", "Candidato significa posible, pero todavía no confirmado por pruebas."),
        ("abc", "{F} ¿Cuál es el primer punto con una lectura fuera de rango?", "P3, con 12 V", "P4, con 0 V", "P2, con 24 V", "El rango es 23 a 25 V; P3 es el primero fuera."),
        ("abc", "{F} ¿Qué punto es el último bueno antes del cambio?", "P2", "P1", "P4", "P2 tiene 24 V, dentro del rango, justo antes de P3."),
        ("abc", "{F} ¿Dónde están los candidatos a causa según el análisis?", "Entre P2 y P3", "Entre P3 y P4", "Antes de P1", "El cambio ocurre entre el último punto bueno y el primero malo."),
        ("=", "{F} ¿Cuántos volts se perdieron entre P2 y P3?", "24-12", "Se resta la lectura de P3 a la de P2.", " V"),
        ("=", "{F} ¿Cuántos volts por debajo del mínimo del rango está P3?", "23-12", "Se resta la lectura de P3 al mínimo del rango.", " V"),
        ("=", "{F} Si cada punto se anota con 3 datos en la planilla de ejemplo, ¿cuántos datos hay en total en los 4 puntos?", "4*3", "Se multiplican los puntos por los datos de cada uno.", " datos"),
        ("abc", "{F} Un compañero dice: «el interruptor está malo». ¿Qué observación es correcta?", "Es un candidato, no una causa confirmada, y la confirma personal autorizado", "Es correcto, porque es el único componente entre P2 y P3", "Es correcto, porque P4 marca 0 V", "Un candidato no es una causa confirmada."),
        ("abc", "{F} Una persona en práctica propone «abrir el interruptor para mirarlo». ¿Qué corresponde?", "No hacerlo: informar los datos al personal autorizado", "Hacerlo, porque es el candidato", "Hacerlo, si lo hace con guantes", "Analizar la planilla no autoriza a intervenir."),
        ("=", "{F} ¿Cuántos volts hay entre la lectura más alta y la más baja de la planilla?", "24-0", "Se resta la lectura menor a la mayor.", " V"),
        ("abc", "{F} ¿Qué frase es correcta en el informe?", "«P2 con 24 V (dentro del rango) y P3 con 12 V (fuera); candidato entre ellos: el interruptor; causa no confirmada»", "«El interruptor está malo y hay que cambiarlo»", "«Hay problemas en el circuito»", "El informe da datos y candidatos y no afirma una causa."),
    ],
    ctx=("abc", "Una persona de práctica te muestra una planilla con una lectura de 0 V y dice «es el último componente, seguro». ¿Qué respondes?", "Que primero se busca el primer punto fuera de rango y que el candidato no es una causa confirmada", "Que sí, porque 0 V siempre marca el último componente", "Que cambie la lectura por 24 V", "El primer punto fuera de rango ubica el cambio."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿dónde están los candidatos a causa en un circuito en serie?", "Entre el último punto bueno y el primer punto malo", "El cambio ocurre en ese tramo."),
        ("¿Quién confirma una causa?", "Personal autorizado con pruebas", "El análisis en papel solo orienta."),
        ("¿Una lectura dentro del rango es un problema?", "No, cumple lo esperado", "La lectura está dentro del intervalo normal del manual."),
    ],
    op=("Planilla de ejemplo: rango de 11 a 13 V. Lecturas en serie: Z1 12 V; Z2 13 V; Z3 9 V; Z4 9 V; Z5 0 V. Escribe (a) el primer punto fuera de rango, (b) el último punto bueno, (c) dónde están los candidatos, (d) una frase de informe que no afirme la causa y a quién se informa.",
        "(a) Z3, con 9 V. (b) Z2, con 13 V, que es el máximo del rango y cumple. (c) Entre Z2 y Z3. (d) «Z2 con 13 V (dentro) y Z3 con 9 V (fuera); candidatos entre Z2 y Z3; causa no confirmada»; se informa al personal autorizado.",
        ["identifica el primer punto fuera de rango", "identifica el último bueno", "ubica los candidatos", "no afirma la causa e informa"],
        ["hoja con las cuatro respuestas"],
        ["tomar Z5 como el primero fuera", "afirmar una causa", "proponer intervenir"],
        "Pregunta: «¿cuál es la primera lectura fuera del rango?». Si duda, pídele que relea cómo se ubican los candidatos."),
    reinforce="Inventa una planilla de cuatro lecturas con un rango y marca el primer punto fuera de rango y los candidatos.",
    extend="Explica por qué no basta mirar solo la lectura más baja de la planilla.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (cálculos de ejemplo, inventados). Fórmula de ejemplo: tensión = corriente × resistencia (V = I × R). Un circuito de ejemplo tiene una tensión de 24 V y una resistencia esperada de 8 Ω, con un rango aceptable de 7 a 9 Ω. "
     "Lectura registrada de resistencia por una persona autorizada: 12 Ω. Potencia de ejemplo: potencia = tensión × corriente (P = V × I), en watts (W).")
build(
    O6, 4, F,
    use="Aprenderé a aplicar la relación entre tensión, corriente y resistencia a números enteros de ejemplo y a comparar una lectura con un rango sin intervenir ningún circuito.",
    prior=["Sé multiplicar y dividir enteros exactos.", "Sé comparar con un rango.", "Sé qué miden volts, amperes y ohms."],
    explain=[
        "La relación entre tensión, corriente y resistencia es V = I × R: la tensión en volts es igual a la corriente en amperes por la resistencia en ohms. De ahí se obtienen otras dos formas: la corriente es la tensión dividida entre la resistencia (I = V / R) y la resistencia es la tensión dividida entre la corriente (R = V / I). Por ejemplo, con 30 V y 6 Ω la corriente es 30 dividido en 6, es decir, 5 A.",
        "La potencia eléctrica P, en watts (W), es la tensión por la corriente: P = V × I. Con 30 V y 5 A, la potencia es 150 W. Un valor medido que sale de su rango esperado es una discrepancia y se informa. En los cálculos de este cuaderno solo se usan números enteros exactos y valores de ejemplo; los reales los fija el fabricante.",
        f"Estos cálculos se hacen en papel y no habilitan para medir ni intervenir un circuito. {EMER} {AVISO}",
    ],
    vocab=[("V = I × R", "relación entre tensión, corriente y resistencia"), ("potencia (W)", "tensión por corriente, medida en watts"), ("rango aceptable", "intervalo de valores que el manual permite"), ("lectura", "valor medido y anotado"), ("discrepancia", "diferencia entre lo medido y lo permitido")],
    worked=[
        ("Corriente", "Un circuito de ejemplo tiene 12 V y 4 Ω. ¿Cuánta corriente circula?", ["I es la tensión dividida entre la resistencia.", "12 dividido en 4 son 3 A."], "3 A"),
        ("Potencia", "Un equipo de ejemplo funciona con 28 V y 5 A. ¿Cuánta potencia usa?", ["La potencia es tensión por corriente.", "28 por 5 son 140 W."], "140 W"),
    ],
    mistakes=[("Dividir al revés: resistencia entre tensión.", "La corriente es la tensión dividida entre la resistencia.", "Escribe la fórmula antes de reemplazar los números."),
              ("Usar la lectura sin compararla con el rango.", "La lectura solo se evalúa contra el rango del manual.", "Compara siempre con el mínimo y el máximo.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué relación liga tensión, corriente y resistencia?", "V = I × R", "V = I + R", "V = R / I", "La tensión es la corriente por la resistencia."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula la potencia eléctrica?", "Tensión por corriente", "Tensión dividida entre resistencia", "Corriente más resistencia", "P = V × I, en watts."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué se hace con un valor medido fuera del rango aceptable?", "Se registra como discrepancia y se informa", "Se cambia por un valor que esté dentro del rango", "Se ignora si es pequeño", "Una discrepancia se informa con sus datos."),
        ("abc", "{F} ¿Qué resistencia esperada tiene el circuito?", "8 Ω", "24 Ω", "12 Ω", "La ficha indica una resistencia esperada de 8 Ω."),
        ("abc", "{F} ¿Está la lectura de 12 Ω dentro del rango aceptable?", "No, porque supera el máximo de 9 Ω", "Sí, porque 12 es mayor que 8", "Sí, porque está cerca de 9", "El rango es 7 a 9 Ω y 12 lo supera."),
        ("abc", "{F} ¿Qué fórmula da la corriente en este circuito?", "I = V / R", "I = V × R", "I = R / V", "De V = I × R se obtiene I = V / R."),
        ("=", "{F} ¿Cuántos amperes circulan con la resistencia esperada de 8 Ω?", "24//8", "Se divide la tensión entre la resistencia.", " A"),
        ("=", "{F} ¿Cuántos watts de potencia hay con 24 V y la corriente esperada de 3 A?", "24*3", "Se multiplica la tensión por la corriente.", " W"),
        ("=", "{F} Si la resistencia fuera la leída de 12 Ω con los mismos 24 V, ¿cuántos amperes circularían?", "24//12", "Se divide la tensión entre la resistencia leída.", " A"),
        ("abc", "{F} Una persona dice: «12 Ω está cerca de 9 Ω, así que lo anoto como dentro del rango». ¿Qué observación es correcta?", "Es falsa: 12 supera el máximo, y debe registrarse como discrepancia", "Es correcta, porque 12 está cerca de 9", "Es correcta, porque la resistencia no se compara", "Un valor fuera del rango es una discrepancia aunque esté cerca."),
        ("abc", "{F} Una persona en práctica propone «cambiar el componente que da 12 Ω». ¿Qué corresponde?", "No hacerlo: informar la lectura y el rango al personal autorizado", "Cambiarlo, porque está fuera del rango", "Cambiarlo, si tiene una pieza de repuesto", "Informar es lo que corresponde; la decisión es de personal autorizado."),
        ("=", "Un circuito de ejemplo tiene 3 A y 6 Ω. ¿Cuántos volts hay?", "3*6", "Se multiplica la corriente por la resistencia.", " V"),
        ("=", "Un circuito de ejemplo tiene 42 V y 6 A. ¿Cuántos ohms tiene?", "42//6", "Se divide la tensión entre la corriente.", " Ω"),
    ],
    ctx=("abc", "Una compañera te muestra un cálculo de ejemplo en que escribe 24 V ÷ 8 Ω = 192 A. ¿Qué haces?", "Le explicas que la división da 3 A y que multiplicó en vez de dividir", "Lo dejas, porque ya lo calculó", "Cambias el 24 por 192", "La corriente es la tensión dividida entre la resistencia."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿cómo se calcula la corriente?", "Tensión dividida entre resistencia", "De V = I × R se despeja I."),
        ("¿Cuánto es 10 V ÷ 5 Ω?", "2 A", "Diez dividido en cinco son dos."),
        ("En Mantenimiento de Aeronaves: ¿en qué unidad se mide la potencia eléctrica?", "En watts (W)", "La potencia se mide en watts."),
    ],
    op=("Datos de ejemplo: un circuito tiene 20 V, resistencia esperada 5 Ω y rango aceptable de 4 a 6 Ω. La lectura registrada es 8 Ω. Escribe (a) la corriente esperada, (b) la potencia esperada, (c) si la lectura está dentro del rango y por qué, (d) qué haces con la lectura y a quién informas.",
        "(a) 20 / 5 = 4 A. (b) 20 × 4 = 80 W. (c) No: 8 supera el máximo de 6 Ω. (d) La registro como discrepancia, con la lectura y el rango, y la informo a personal autorizado; no intervengo.",
        ["calcula la corriente", "calcula la potencia", "compara con el rango", "informa sin intervenir"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "decir que está dentro del rango", "proponer cambiar el componente"],
        "Pregunta: «¿qué fórmula usas para la corriente?». Si duda, pídele que relea V = I × R."),
    reinforce="Inventa un circuito con 18 V y 3 Ω y calcula la corriente y la potencia.",
    extend="Explica con un ejemplo por qué comparar con un rango es indispensable antes de concluir.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (dos informes de discrepancia de ejemplo, inventados). Informe A: «hay algo raro con un cable». Informe B: «Hallazgo en inspección visual del día de ejemplo, turno de la mañana. Ubicación: tablero del puesto 2, cable identificado C-14 (de ejemplo). "
     "Señal: aislación decolorada por calor, de unos 3 cm. Lectura de la persona autorizada: 0 V en el punto posterior, rango esperado 23 a 25 V. Sin intervención. Informado al personal certificado a las 10:00; firma del técnico». Lista de datos de un buen informe de ejemplo: qué, dónde, cuándo, cómo se detectó, lectura con su rango y a quién se informó (6 datos).")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos informes de discrepancia, a decidir cuál sirve y a informar a tiempo y a quien corresponde.",
    prior=["Sé qué es una discrepancia.", "Sé calcular porcentajes sencillos.", "Sé que un informe debe tener datos."],
    explain=[
        "Informar oportunamente significa avisar a tiempo y a la persona correcta. Un buen informe de discrepancia responde seis preguntas: qué se vio, dónde, cuándo, cómo se detectó, qué lectura se obtuvo con su rango y a quién se informó. Si el informe es vago, quien lo recibe no puede decidir ni reconstruir lo ocurrido. No se escribe una causa que no se comprobó, y no se esconde nada para que el trabajo salga más rápido.",
        "El plazo depende de la gravedad: algo que puede afectar la seguridad se avisa de inmediato al personal certificado o al responsable del turno, y lo demás se informa dentro del turno, según la regla de la organización. Un informe se puede comparar con otro contando cuántos de los seis datos tiene cada uno.",
        f"Informar no significa reparar. {EMER} {AVISO}",
    ],
    vocab=[("informar oportunamente", "avisar a tiempo y a la persona correcta"), ("hallazgo", "lo que se observa en una inspección"), ("dato del informe", "cada una de las seis respuestas de un buen informe"), ("responsable del turno", "persona a cargo del trabajo de un turno"), ("causa no comprobada", "explicación que no se debe escribir como si fuera un hecho")],
    worked=[
        ("Contar datos", "Un informe de ejemplo dice: qué se vio, dónde y cuándo. ¿Cuántos de los seis datos tiene?", ["Cuenta qué, dónde y cuándo.", "Son tres datos."], "3 de 6"),
        ("A quién informar", "Una persona de ejemplo ve una señal de calor en un cable que podría afectar la seguridad. ¿Cuándo avisa?", ["Si afecta la seguridad, se avisa de inmediato.", "Al personal certificado o al responsable del turno."], "De inmediato, al personal certificado o al responsable del turno"),
    ],
    mistakes=[("Informar solo «algo raro» sin datos.", "Sin datos nadie puede decidir ni verificar.", "Responde las seis preguntas."),
              ("Informar una causa que nadie comprobó.", "Una causa no comprobada confunde la decisión.", "Escribe lo observado y deja la causa para personal autorizado.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa informar oportunamente?", "Avisar a tiempo y a la persona correcta", "Avisar cuando termina el mes", "Avisar solo si alguien pregunta", "Oportuno es a tiempo y a quien corresponde."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué debe incluir un buen informe de discrepancia?", "Qué, dónde, cuándo, cómo se detectó, lectura con su rango y a quién se informó", "Solo la opinión de la persona", "Solo la hora", "Estos datos permiten decidir y reconstruir lo ocurrido."),
        ("abc", "En Mantenimiento de Aeronaves: ¿a quién se avisa de inmediato algo que puede afectar la seguridad?", "Al personal certificado o al responsable del turno", "A nadie, hasta terminar la jornada", "Solo a un compañero", "Un riesgo para la seguridad no espera al final del turno."),
        ("abc", "{F} ¿Cuál de los dos informes sirve mejor para decidir?", "El informe B, porque trae ubicación, señal, lectura con su rango y a quién se informó", "El informe A, porque es más corto", "Los dos sirven igual", "El informe B responde las preguntas necesarias."),
        ("abc", "{F} ¿Qué le falta al informe A?", "Dónde, cuándo, cómo se detectó, lectura y a quién se informó", "Nada, está completo", "Solo la hora", "Solo dice que hay algo raro con un cable."),
        ("abc", "{F} ¿Qué dato del informe B muestra que no hubo intervención?", "La frase «Sin intervención»", "El número del cable", "La hora del informe", "Esa frase declara que solo se observó e informó."),
        ("=", "{F} El informe B tiene los 6 datos de la lista y el informe A tiene 1. ¿Cuántos datos más tiene B que A?", "6-1", "Se resta lo que tiene A a lo que tiene B.", " datos"),
        ("=", "Una organización de ejemplo recibe 5 informes y revisa cada uno con los 6 datos de la lista. ¿Cuántas comprobaciones hace?", "5*6", "Se multiplican los informes por los datos de cada uno.", " comprobaciones"),
        ("=", "{F} La persona vio el hallazgo a las 9:30 y lo informó a las 10:00. ¿Cuántos minutos pasaron?", "10*60-(9*60+30)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("abc", "{F} Una persona dice: «en el informe A pongo que el cable está quemado por sobrecarga». ¿Qué observación es correcta?", "Es una causa no comprobada: se debe escribir lo observado y dejar la causa a personal autorizado", "Es correcto, porque explica el problema", "Es correcto, si suena técnico", "Una causa no comprobada puede confundir la decisión."),
        ("abc", "{F} Una persona en práctica ve el cable decolorado y dice: «lo reemplazo yo y así no hay informe». ¿Qué corresponde?", "No: informar el hallazgo, porque ocultarlo y repararlo sin autorización falsea el registro", "Hacerlo, para ahorrar papeleo", "Hacerlo, si el cable es barato", "No informar un hallazgo es una falta grave de honestidad."),
        ("=", "Un informe de ejemplo tiene 4 de los 6 datos. ¿Cuántos datos faltan?", "6-4", "Se resta lo presente al total.", " datos"),
        ("abc", "Un hallazgo menor sin efecto en la seguridad se detecta a media mañana. ¿Cuándo corresponde informarlo según la regla de ejemplo?", "Dentro del turno, al responsable", "Nunca, porque es menor", "El mes siguiente", "Lo menor igual se informa, dentro del turno."),
    ],
    ctx=("abc", "Una persona a cargo de un hangar de ejemplo te dice: «no informes ese cable decolorado, retrasa la salida». ¿Qué respondes?", "Que lo informarás igual al personal certificado y que consultarás a un adulto responsable", "Que sí, para no retrasar", "Que lo anotarás solo si lo pregunta alguien", "Ocultar un hallazgo es una falta grave."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿cuántos datos tiene un buen informe de discrepancia en esta clase?", "Seis", "Qué, dónde, cuándo, cómo, lectura y a quién."),
        ("¿Se escribe en el informe una causa que no se comprobó?", "No", "Se escribe solo lo observado y se deja la causa."),
        ("¿Informar significa reparar?", "No", "Informar y reparar son tareas distintas."),
    ],
    op=("Caso de ejemplo: una persona ve que el conector de un equipo del puesto 3 tiene corrosión visible. Lectura de ejemplo: 5 V en el punto posterior, rango esperado de 10 a 12 V. No intervino. Escribe (a) un informe breve con los seis datos (inventa la hora y el identificador), (b) cuántos datos tiene, (c) a quién informas y por qué, (d) por qué no escribes la causa de la corrosión.",
        "(a) «Qué: corrosión visible en el conector. Dónde: puesto 3, equipo de ejemplo E-7. Cuándo: 11:15. Cómo: inspección visual y lectura. Lectura: 5 V, rango 10 a 12 V. Informado al responsable del turno.» (b) Seis datos. (c) Al personal certificado o al responsable del turno, que decide. (d) La causa no se comprobó; informo lo observado.",
        ["escribe los seis datos", "cuenta los datos", "elige a quién informar", "no afirma una causa"],
        ["hoja con las cuatro respuestas"],
        ["informe vago", "afirmar una causa", "proponer reparar"],
        "Pregunta: «¿respondiste qué, dónde, cuándo, cómo, lectura y a quién?». Si duda, pídele que relea la lista."),
    reinforce="Reescribe el informe «algo raro con un cable» con los seis datos, inventando los que falten.",
    extend="Explica por qué ocultar un hallazgo es una falta grave de honestidad.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 6 (hoja de registro del día de ejemplo, inventada). Registro de la «Organización Demo de Mantenimiento»: el día se anotaron 10 trabajos. De ellos, 7 tienen fecha, referencia al manual, firma de quien ejecutó y firma de la revisión independiente; 2 no tienen la firma de la revisión independiente (pero tienen todo lo demás); 1 tiene ambas firmas pero no tiene fecha. "
     "Dotación del turno: 15 personas.")
build(
    O7, 1, F,
    use="Aprenderé por qué se registran las acciones de mantenimiento, qué exige la normativa aeronáutica vigente en general y qué reglas básicas tiene un buen registro.",
    prior=["Sé leer un registro sencillo.", "Sé calcular un porcentaje exacto.", "Sé que las firmas dan constancia."],
    explain=[
        "El mantenimiento de una aeronave se registra por exigencia de la normativa aeronáutica vigente. El registro permite a cualquier persona saber qué se hizo, quién lo hizo, cuándo y con qué referencia del manual. Esta propiedad se llama trazabilidad. Con registros incompletos o falsos una aeronave podría volar con un defecto sin que nadie lo sepa. Por eso falsear un registro es una falta grave, y la liberación a servicio la firma solo personal certificado.",
        "Un buen registro es legible, con fecha, con referencia al manual vigente, con la firma de quien ejecutó y con la revisión independiente cuando corresponde. No tiene espacios en blanco. Si hay un error, no se borra: se tacha con una línea, se escribe lo correcto, y se fecha y firma la corrección. Informar es avisar a las personas correctas lo ocurrido, con datos y a tiempo.",
        f"En este cuaderno solo estudias las reglas generales. {EMER} {AVISO}",
    ],
    vocab=[("registro de mantenimiento", "documento donde se anotan los trabajos hechos"), ("trazabilidad", "posibilidad de reconstruir qué se hizo, quién y cuándo"), ("normativa aeronáutica", "reglas de la autoridad aeronáutica sobre el mantenimiento"), ("corrección de un registro", "error tachado con una línea, con el valor correcto, fecha y firma"), ("revisión independiente", "verificación de una persona distinta de quien ejecutó")],
    worked=[
        ("Corregir un error", "En un registro de ejemplo se anotó «4» y debía decir «5». ¿Cómo se corrige?", ["No se borra: se tacha con una línea.", "Se escribe 5, y se fecha y firma la corrección."], "Se tacha con una línea, se escribe 5, y se fecha y firma"),
        ("Trazabilidad", "Un registro de ejemplo no dice quién hizo el trabajo. ¿Qué propiedad falla?", ["Sin autor no se puede reconstruir quién lo hizo.", "Falla la trazabilidad."], "La trazabilidad"),
    ],
    mistakes=[("Borrar un dato mal anotado con corrector.", "El borrado oculta lo que decía antes y deja dudas.", "Tacha con una línea y firma la corrección."),
              ("Dejar casillas en blanco «para completar después».", "Un espacio en blanco permite agregar datos sin respaldo.", "Completa todo o tacha la casilla con una nota.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la trazabilidad?", "La posibilidad de reconstruir qué se hizo, quién y cuándo", "La rapidez con que se termina un trabajo", "El número de piezas del hangar", "Con trazabilidad se verifica el trabajo después."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se corrige un error en un registro?", "Se tacha con una línea, se escribe lo correcto y se fecha y firma", "Se borra con corrector y se escribe encima", "Se cubre con una hoja nueva pegada encima", "La corrección debe dejar visible el dato anterior."),
        ("abc", "En Mantenimiento de Aeronaves: ¿por qué es grave falsear un registro?", "Porque una aeronave podría volar con un defecto que nadie conoce", "Porque retrasa la entrega del informe al turno siguiente", "Porque cambia el precio de la aeronave", "Un registro falso puede esconder un defecto que afecta la seguridad."),
        ("abc", "{F} ¿Cuántos trabajos del día tienen la revisión independiente firmada?", "8 trabajos: los 7 completos y el que solo no tiene fecha", "7 trabajos, solo los completos", "10 trabajos, todos", "Siete completos más el que solo falla en la fecha; los otros dos no tienen esa firma."),
        ("abc", "{F} ¿Qué trabajos están incompletos?", "Los 2 sin revisión independiente y el 1 sin fecha", "Solo el que no tiene fecha", "Ninguno", "Faltan requisitos en tres de los diez trabajos."),
        ("abc", "{F} ¿Qué dato falta en el trabajo sin fecha para que cumpla el registro?", "La fecha, que da el cuándo", "El nombre del fabricante de la aeronave", "La hora de término del turno", "La fecha indica cuándo se hizo el trabajo."),
        ("=", "{F} ¿Cuántos trabajos están incompletos?", "10-7", "Se resta lo completo al total de trabajos.", " trabajos"),
        ("=", "{F} ¿Qué porcentaje de los trabajos del día está completo?", "7*100//10", "Se multiplica lo completo por 100 y se divide entre el total.", " %"),
        ("=", "{F} Cada persona del turno firma en promedio 2 registros en una semana de ejemplo. ¿Cuántas firmas son?", "15*2", "Se multiplican las personas por las firmas de cada una.", " firmas"),
        ("abc", "{F} Una persona dice: «los dos trabajos sin revisión independiente quedan igual de válidos». ¿Qué observación es correcta?", "Es falsa: sin esa firma falta la verificación y el registro está incompleto", "Es correcta, porque la firma de quien ejecutó basta", "Es correcta, si pasó poco tiempo", "La revisión independiente es una verificación requerida."),
        ("abc", "{F} Una persona en práctica dice: «completo yo la firma independiente de los dos trabajos». ¿Qué corresponde?", "No: esa firma es de otra persona que comprobó el trabajo", "Hacerlo, para cerrar los registros", "Hacerlo, si firma con otro color", "Firmar sin comprobar falsea el registro."),
        ("=", "Un registro de ejemplo tiene 25 trabajos y 5 están incompletos. ¿Cuántos están completos?", "25-5", "Se resta lo incompleto al total.", " trabajos"),
        ("abc", "Un técnico de ejemplo anota «bien» como único dato del trabajo. ¿Qué problema tiene el registro?", "No dice qué se hizo, con qué referencia ni cuándo", "Ninguno, porque es corto", "Que no incluye el precio del trabajo", "Un registro necesita datos que se puedan verificar."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «anota que lo hicimos ayer, aunque fue hoy, así cuadra con la planilla». ¿Qué respondes?", "Que no, porque anotar una fecha falsa falsea el registro, y que consultarás a un adulto responsable", "Que sí, porque nadie lo notará", "Que sí, si es solo un día", "Una fecha falsa rompe la trazabilidad."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es un registro de mantenimiento?", "El documento donde se anotan los trabajos hechos", "Deja constancia por escrito de los trabajos que se hicieron."),
        ("¿Se borra un dato mal anotado?", "No, se tacha con una línea y se firma la corrección", "El dato anterior debe seguir visible."),
        ("¿Quién firma la liberación a servicio?", "Personal certificado", "Solo personal certificado puede firmar esa liberación."),
    ],
    op=("Hoja de ejemplo: de 12 trabajos del día, 9 están completos, 2 no tienen fecha y 1 no tiene firma de quien ejecutó. Escribe (a) cuántos están incompletos, (b) qué porcentaje está completo, (c) cómo corriges en tu propio registro una fecha anotada «12» que debía decir «21», (d) por qué no inventas la fecha que falta.",
        "(a) 12 - 9 = 3 incompletos. (b) 9 × 100 / 12 = 75 %. (c) Tachar el 12 con una línea, escribir 21, fechar y firmar la corrección; no borrar. (d) Una fecha inventada falsea el registro; informo que falta el dato.",
        ["calcula los incompletos", "calcula el porcentaje", "describe la corrección", "no inventa datos"],
        ["hoja con las cuatro respuestas"],
        ["borrar el error", "inventar la fecha", "calcular mal el porcentaje"],
        "Pregunta: «¿qué requisitos faltan?». Si duda, pídele que relea qué tiene un buen registro."),
    reinforce="Escribe cinco características de un buen registro de mantenimiento.",
    extend="Explica con un ejemplo cómo un registro incompleto puede esconder un defecto.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 7 (registro de componentes con vida límite de ejemplo, inventado). Componente K1: vida límite 3.000 horas de vuelo (HV); acumula 2.750 HV. Componente K2: vida límite 1.200 ciclos; acumula 1.200 ciclos. "
     "Componente K3: vida límite 5.000 HV; acumula 1.500 HV. Documentos del hangar de ejemplo: libro de la aeronave, orden de trabajo, tarjeta de tarea, registro de componentes y certificado de liberación a servicio.")
build(
    O7, 2, F,
    use="Aprenderé los documentos del registro de mantenimiento, qué rol firma cada uno y cómo se calcula la vida restante de un componente.",
    prior=["Sé restar números enteros.", "Sé qué es un registro.", "Sé qué es una orden de trabajo."],
    explain=[
        "El libro de la aeronave registra su historia: horas de vuelo, ciclos y trabajos. La orden de trabajo pide un trabajo y la tarjeta de tarea baja una tarea del manual con espacios para anotar. El registro de componentes anota cada componente con su número de parte, su número de serie, sus horas o ciclos acumulados y, si corresponde, su vida límite: el máximo de horas o ciclos que el fabricante permite antes de retirarlo. El certificado de liberación a servicio declara que el trabajo cumple lo exigido y lo firma personal certificado.",
        "La vida restante de un componente es su vida límite menos lo acumulado. Si es cero o negativa, el componente llegó a su límite y se informa a personal certificado, que decide con la norma vigente. Los registros se guardan por el tiempo que fija la normativa aeronáutica vigente. Cada documento tiene su autor: quien ejecuta firma la tarea, quien inspecciona firma la revisión independiente y personal certificado firma la liberación.",
        f"Los valores de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("libro de la aeronave", "registro de la historia de la aeronave: horas, ciclos y trabajos"), ("registro de componentes", "documento con la historia y los acumulados de cada componente"), ("vida límite", "máximo de horas o ciclos permitido antes de retirar un componente"), ("vida restante", "vida límite menos lo acumulado"), ("certificado de liberación a servicio", "documento que declara el trabajo cumplido y firma personal certificado")],
    worked=[
        ("Vida restante", "Un componente de ejemplo tiene vida límite de 800 HV y acumula 620 HV. ¿Cuánta vida le queda?", ["Se resta lo acumulado a la vida límite.", "800 menos 620 son 180."], "180 HV"),
        ("Documento", "¿Qué documento declara que un trabajo cumple lo exigido y permite volver al servicio?", ["Es el certificado de liberación a servicio.", "Lo firma personal certificado."], "El certificado de liberación a servicio"),
    ],
    mistakes=[("Confundir la vida límite con lo acumulado.", "La vida límite es el máximo permitido; lo acumulado es lo usado.", "Calcula la vida restante restando."),
              ("Creer que la orden de trabajo libera la aeronave.", "La orden de trabajo pide el trabajo; la liberación es otro documento firmado por personal certificado.", "Distingue qué documento hace cada cosa.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la vida límite de un componente?", "El máximo de horas o ciclos permitido antes de retirarlo", "Las horas que ya acumuló", "El precio del componente", "La vida límite es un tope fijado por el fabricante."),
        ("abc", "En Mantenimiento de Aeronaves: ¿quién firma el certificado de liberación a servicio?", "Personal certificado", "Quien ejecutó la tarea", "La persona propietaria", "Esa firma declara el trabajo cumplido y es de personal certificado."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula la vida restante?", "Vida límite menos lo acumulado", "Lo acumulado más la vida límite", "Vida límite dividida entre dos", "Resta lo usado al máximo permitido."),
        ("abc", "{F} ¿Qué documento guarda la historia de horas y ciclos de la aeronave?", "El libro de la aeronave", "La tarjeta de tarea", "El certificado de liberación", "El libro anota horas, ciclos y trabajos."),
        ("abc", "{F} ¿Cuál componente llegó a su vida límite?", "K2, con 1.200 ciclos de 1.200", "K1, con 2.750 HV", "K3, con 1.500 HV", "Solo K2 iguala su vida límite."),
        ("abc", "{F} ¿Qué documento baja una tarea del manual con espacios para anotar y firmar?", "La tarjeta de tarea", "El registro de componentes", "El libro de la aeronave", "La tarjeta organiza la ejecución y la firma."),
        ("=", "{F} ¿Cuántas HV de vida le quedan a K1?", "3000-2750", "Se resta lo acumulado a la vida límite.", " HV"),
        ("=", "{F} ¿Cuántas HV de vida le quedan a K3?", "5000-1500", "Se resta lo acumulado a la vida límite.", " HV"),
        ("=", "{F} ¿Cuántos ciclos de vida le quedan a K2?", "1200-1200", "Se resta lo acumulado a la vida límite.", " ciclos"),
        ("abc", "{F} Una persona dice: «K2 aún puede usarse porque no pasó su límite». ¿Qué observación es correcta?", "Es falsa: llegó a su límite y debe informarse a personal certificado", "Es correcta, porque no lo superó", "Es correcta, si lo usa pocas veces más", "Llegar al límite equivale a agotar la vida del componente."),
        ("abc", "{F} Una persona en práctica propone anotar 1.100 ciclos en K2 «para que le quede vida». ¿Qué corresponde?", "No: anotar un valor falso falsea el registro; se anota el real e informa", "Hacerlo, para evitar un cambio caro", "Hacerlo, si nadie lo revisa", "Un valor falso puede esconder un componente agotado."),
        ("=", "{F} Si K1 vuela 100 HV más, ¿cuántas HV acumulará?", "2750+100", "Se suma el nuevo uso a lo acumulado.", " HV"),
        ("abc", "{F} Si K1 vuela 300 HV más, ¿pasará su vida límite?", "Sí: acumulará 3.050 HV, más que las 3.000 de su límite", "No: 3.050 es menor que 3.000", "No, porque los límites no se superan", "2.750 más 300 son 3.050, que supera 3.000."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «el componente K2 está justo en su límite, anota que le quedan 100 ciclos para seguir». ¿Qué respondes?", "Que no, porque anotar un valor falso falsea el registro, y que informarás a un adulto responsable", "Que sí, porque solo es un componente", "Que sí, si firma el técnico", "El registro debe reflejar los valores reales."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué anota el libro de la aeronave?", "Sus horas, ciclos y trabajos", "Es la historia de la aeronave."),
        ("¿Qué pasa cuando la vida restante es cero?", "Se informa a personal certificado", "El componente llegó a su límite."),
        ("¿Quién firma la revisión independiente?", "Una persona distinta de quien ejecutó", "La independencia permite detectar errores que el autor no ve."),
    ],
    op=("Registro de ejemplo: componente M1: vida límite 2.500 HV, acumula 2.380 HV. Componente M2: vida límite 900 ciclos, acumula 650 ciclos. Escribe (a) la vida restante de cada uno, (b) cuántas HV le quedarían a M1 si vuela 100 HV más, (c) qué documento firma personal certificado, (d) qué haces si un componente llegó al límite.",
        "(a) M1: 2.500 - 2.380 = 120 HV; M2: 900 - 650 = 250 ciclos. (b) 120 - 100 = 20 HV. (c) El certificado de liberación a servicio. (d) Lo informo a personal certificado, que decide con la norma vigente.",
        ["calcula la vida restante", "calcula la vida tras más uso", "nombra el documento", "informa el límite alcanzado"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "afirmar un valor falso", "decir que decide el técnico"],
        "Pregunta: «¿cuánto queda de cada uno?». Si duda, pídele que relea cómo se calcula la vida restante."),
    reinforce="Escribe los cinco documentos del registro de mantenimiento y quién firma cada uno.",
    extend="Explica por qué un componente con vida límite debe registrarse con valores reales.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 8 (cuatro líneas del libro de la aeronave de ejemplo, inventadas). Línea 1: fecha 10, horas de la aeronave 1.200, trabajo «tarea 07», referencia al manual y firma del técnico y de la revisión independiente. "
     "Línea 2: fecha 11, horas 1.205, trabajo «tarea 12», sin referencia al manual, firma del técnico y de la revisión. Línea 3: fecha 12, horas 1.198, trabajo «tarea 15», con referencia y ambas firmas. "
     "Línea 4: sin fecha, horas 1.210, trabajo «tarea 18», con referencia y ambas firmas. Las horas de una aeronave solo pueden subir o mantenerse entre líneas sucesivas.")
build(
    O7, 3, F,
    use="Aprenderé a revisar un registro en papel, a detectar errores y omisiones y a escribir un informe de hallazgos sin falsear nada.",
    prior=["Sé qué lleva un buen registro.", "Sé comparar números.", "Sé qué es una corrección válida."],
    explain=[
        "Revisar un registro es comprobar, línea por línea, que tenga fecha, referencia al manual, firma de quien ejecutó, revisión independiente y datos coherentes. Un dato incoherente es el que no puede ser cierto: por ejemplo, las horas de una aeronave no pueden bajar entre dos líneas sucesivas. Una omisión es un dato que falta, como una fecha o una referencia.",
        "Cuando se detecta un error, no se borra ni se completa con un dato inventado: se informa al responsable del registro, que lo corrige con las reglas de corrección y deja constancia. En el informe de hallazgos se escribe la línea, el tipo de problema (omisión o incoherencia) y lo que se sabe. Quien revisa no decide si se libera la aeronave: eso lo hace personal certificado.",
        f"La revisión es solo en papel. {EMER} {AVISO}",
    ],
    vocab=[("omisión", "dato que falta en un registro"), ("incoherencia", "dato que no puede ser cierto junto con otros"), ("referencia al manual", "indicación del documento y la revisión vigente usados en el trabajo"), ("hallazgo de revisión", "problema detectado al revisar un registro"), ("responsable del registro", "persona que debe corregirlo y dejar constancia")],
    worked=[
        ("Incoherencia", "En un libro de ejemplo, la línea 1 marca 800 horas y la línea 2, 790. ¿Qué problema hay?", ["Las horas no pueden bajar.", "Es una incoherencia."], "Una incoherencia: las horas bajaron"),
        ("Omisión", "Una línea de ejemplo no trae la firma de quien ejecutó. ¿Qué problema hay?", ["Falta un dato requerido.", "Es una omisión."], "Una omisión"),
    ],
    mistakes=[("Completar una fecha que falta con la que parece lógica.", "Un dato inventado falsea el registro.", "Informa que falta y deja que el responsable lo corrija con respaldo."),
              ("Revisar solo la primera línea y dar por bueno el resto.", "Los errores pueden estar en cualquier línea.", "Revisa línea por línea con la misma lista.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una omisión en un registro?", "Un dato que falta", "Un dato que está mal escrito", "Un dato que se anotó dos veces", "La omisión es lo que no se anotó."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una incoherencia en un registro?", "Un dato que no puede ser cierto junto con otros", "Un dato que falta", "Una letra poco legible", "La incoherencia es una contradicción entre datos."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué se hace al detectar un error en un registro ajeno?", "Se informa al responsable del registro", "Se borra y se escribe lo que parece correcto", "Se ignora para no causar problemas", "La corrección la hace el responsable con las reglas y deja constancia."),
        ("abc", "{F} ¿Qué problema tiene la línea 2?", "Una omisión: falta la referencia al manual", "Una incoherencia en las horas", "Ninguno", "La línea 2 no trae referencia al manual."),
        ("abc", "{F} ¿Qué problema tiene la línea 3?", "Una incoherencia: las horas bajaron de 1.205 a 1.198", "Una omisión de fecha", "Ninguno", "Las horas de una aeronave no pueden bajar."),
        ("abc", "{F} ¿Qué problema tiene la línea 4?", "Una omisión: no tiene fecha", "Una incoherencia en las horas", "Ninguno", "La línea 4 no tiene fecha."),
        ("=", "{F} Si cada línea con problema ocupa 2 renglones en el informe de hallazgos y solo la línea 1 está sin problemas, ¿cuántos renglones ocupa el informe?", "(4-1)*2", "Se restan las líneas sin problema y se multiplica por los renglones.", " renglones"),
        ("=", "{F} ¿Cuántas horas bajó la aeronave entre la línea 2 y la línea 3?", "1205-1198", "Se resta la lectura de la línea 3 a la de la línea 2.", " horas"),
        ("=", "{F} ¿Cuántas horas subió la aeronave entre la línea 1 y la línea 4?", "1210-1200", "Se resta la lectura de la línea 1 a la de la línea 4.", " horas"),
        ("abc", "{F} Una persona dice: «a la línea 4 le pongo la fecha 13, que es la que sigue». ¿Qué observación es correcta?", "Es falsa: un dato inventado falsea el registro; se informa la omisión", "Es correcta, porque la fecha sigue el orden", "Es correcta, si lo anota con lápiz", "Un dato sin respaldo no se agrega."),
        ("abc", "{F} ¿Qué línea está sin problemas?", "La línea 1", "La línea 2", "La línea 3", "La línea 1 tiene todos sus datos y es coherente."),
        ("=", "{F} Si cada línea se revisa con 5 requisitos, ¿cuántos requisitos se comprueban en las 4 líneas?", "4*5", "Se multiplican las líneas por los requisitos de cada una.", " requisitos"),
        ("abc", "{F} ¿Qué frase es correcta en el informe de hallazgos?", "«Línea 3: incoherencia, las horas bajan de 1.205 a 1.198; se informa al responsable»", "«La línea 3 está mal escrita, la corrijo yo»", "«Todo bien, solo hay detalles»", "El informe nombra la línea, el problema y el dato, sin corregir por su cuenta."),
    ],
    ctx=("abc", "Una compañera te dice: «borra el 1.198 y pon 1.208, para que cuadre». ¿Qué respondes?", "Que no, porque se informa al responsable, que corrige con las reglas y deja constancia", "Que sí, porque así cuadra", "Que sí, si lo haces con otra tinta", "Un cambio sin respaldo falsea el registro."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿pueden bajar las horas de una aeronave entre líneas sucesivas?", "No", "Las horas solo suben o se mantienen."),
        ("¿Se completa un dato que falta con uno inventado?", "No, se informa", "Un dato inventado falsea el registro."),
        ("¿Quién corrige un registro?", "El responsable del registro, con las reglas de corrección", "Debe dejar constancia con fecha y firma."),
    ],
    op=("Libro de ejemplo, tres líneas: L1: fecha 20, horas 600, tarea 03, con referencia y ambas firmas. L2: fecha 21, horas 596, tarea 04, con referencia y ambas firmas. L3: fecha 22, horas 604, tarea 05, sin firma de la revisión independiente. Escribe (a) qué problema tiene L2 y cuántas horas bajó, (b) qué problema tiene L3, (c) cuántas líneas tienen problemas, (d) qué haces con los errores, sin corregirlos tú.",
        "(a) Incoherencia: las horas bajaron 600 - 596 = 4. (b) Omisión: falta la firma de la revisión independiente. (c) Dos líneas, L2 y L3. (d) Informo línea, tipo de problema y dato al responsable del registro, que corrige con las reglas y deja constancia.",
        ["detecta la incoherencia y calcula", "detecta la omisión", "cuenta las líneas", "informa sin corregir"],
        ["hoja con las cuatro respuestas"],
        ["confundir omisión e incoherencia", "calcular mal", "corregir por su cuenta"],
        "Pregunta: «¿falta un dato o los datos se contradicen?». Si duda, pídele que relea las definiciones."),
    reinforce="Inventa un libro de cuatro líneas con una omisión y una incoherencia, y escribe el informe.",
    extend="Explica por qué se informa al responsable en vez de corregir el registro de otra persona.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 9 (informe de entrega de turno de ejemplo, inventado). Turno de la mañana de la «Organización Demo de Mantenimiento»: 12 tareas planificadas; 9 terminadas con su registro completo; 2 en proceso; 1 pendiente por falta de una pieza de ejemplo. "
     "Horas de trabajo anotadas: 6 personas, 8 horas cada una. Una tarea tiene vencimiento a las 1.500 HV y la aeronave acumula 1.460 HV. El responsable de turno es personal certificado de ejemplo.")
build(
    O7, 4, F,
    use="Aprenderé a escribir un informe de entrega de turno en papel, con cálculos exactos de avance y de horas, y a informar pendientes sin ocultar nada.",
    prior=["Sé calcular porcentajes exactos.", "Sé multiplicar y restar enteros.", "Sé qué es un pendiente."],
    explain=[
        "Un informe de entrega de turno comunica al turno siguiente el estado del trabajo. Debe decir cuántas tareas se planificaron, cuántas están terminadas con su registro completo, cuántas están en proceso y cuántas pendientes, con el motivo. Informa también las horas de trabajo y los vencimientos cercanos. Es una forma de informar oportunamente: lo que el turno siguiente no sabe, no lo puede cuidar.",
        "Las horas de trabajo son el número de personas por las horas de cada una. El avance se calcula como tareas terminadas por 100 dividido entre las tareas planificadas. Los pendientes se escriben con su motivo y su responsable, sin cerrarlos con una firma que no corresponde. El informe no decide la liberación de la aeronave: eso lo hace personal certificado.",
        f"Estos cálculos son de ejemplo y se hacen en papel. {EMER} {AVISO}",
    ],
    vocab=[("entrega de turno", "informe que pasa el estado del trabajo al turno siguiente"), ("avance", "porcentaje de tareas terminadas sobre las planificadas"), ("horas de trabajo", "personas por las horas de cada una"), ("tarea en proceso", "tarea iniciada y aún sin terminar"), ("vencimiento cercano", "tarea cuyo límite está próximo")],
    worked=[
        ("Avance", "En un turno de ejemplo se planificaron 8 tareas y se terminaron 6. ¿Cuál es el avance?", ["Se multiplica 6 por 100 y se divide entre 8.", "600 dividido en 8 es 75."], "75 %"),
        ("Horas de trabajo", "Un turno de ejemplo tiene 4 personas que trabajan 6 horas cada una. ¿Cuántas horas de trabajo hay?", ["Se multiplican las personas por las horas.", "4 por 6 son 24."], "24 horas"),
    ],
    mistakes=[("Contar una tarea en proceso como terminada.", "Terminada significa con su registro completo y verificado.", "Cuenta como terminadas solo las cerradas."),
              ("Omitir un pendiente para que el informe se vea mejor.", "El turno siguiente no podrá cuidar lo que no sabe.", "Informa todos los pendientes con su motivo.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿para qué sirve un informe de entrega de turno?", "Para que el turno siguiente conozca el estado del trabajo", "Para calcular el costo total de la aeronave", "Para reemplazar la liberación a servicio", "Lo que el turno siguiente no sabe, no lo puede cuidar."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula el avance de un turno?", "Tareas terminadas por 100 dividido entre las planificadas", "Tareas pendientes más terminadas", "Horas trabajadas por personas", "El avance compara lo terminado con lo planificado."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué debe llevar un pendiente en el informe?", "Su motivo y su responsable", "Solo la palabra «pendiente»", "Una firma que lo cierre", "El motivo y el responsable permiten seguirlo."),
        ("abc", "{F} ¿Cuántas tareas están terminadas con su registro completo?", "9", "12", "11", "La ficha indica 9 terminadas con registro completo."),
        ("abc", "{F} ¿Qué motivo tiene el pendiente?", "La falta de una pieza de ejemplo", "Un descuido de la persona", "Que la tarea no estaba planificada", "La ficha dice que falta una pieza."),
        ("abc", "{F} ¿Qué tarea tiene un vencimiento cercano?", "La que vence a las 1.500 HV, porque la aeronave acumula 1.460 HV", "Ninguna, porque 1.500 es lejano", "La que ya terminó", "Faltan pocas horas para el vencimiento."),
        ("=", "{F} ¿Qué porcentaje de avance tiene el turno?", "9*100//12", "Se multiplican las terminadas por 100 y se divide entre las planificadas.", " %"),
        ("=", "{F} ¿Cuántas horas de trabajo anotó el turno?", "6*8", "Se multiplican las personas por las horas de cada una.", " horas"),
        ("=", "{F} ¿Cuántas HV faltan para el vencimiento de la tarea?", "1500-1460", "Se resta lo acumulado al vencimiento.", " HV"),
        ("abc", "{F} Una persona dice: «las 2 tareas en proceso las anoto como terminadas, así el avance es 11 de 12». ¿Qué observación es correcta?", "Es falsa: en proceso no es terminada, y anotarlo así falsea el informe", "Es correcta, porque ya casi están", "Es correcta, si las termina el turno siguiente", "Solo cuentan como terminadas las cerradas con su registro."),
        ("abc", "{F} Una persona en práctica propone no informar el pendiente de la pieza «para no preocupar». ¿Qué corresponde?", "Informarlo con su motivo, porque el turno siguiente necesita saberlo", "No informarlo, para ahorrar tiempo", "Informarlo solo si lo preguntan", "Un pendiente oculto no puede cuidarse."),
        ("=", "{F} ¿Cuántas tareas quedan sin terminar?", "12-9", "Se resta lo terminado al total planificado.", " tareas"),
        ("abc", "{F} ¿Quién decide si la aeronave se libera a servicio con tareas sin terminar?", "El personal certificado, según la norma vigente", "El técnico que escribe el informe", "Quien tenga más años de experiencia", "La liberación es siempre de personal certificado."),
    ],
    ctx=("abc", "Al terminar el turno, una persona te dice: «anota el pendiente como terminado, mañana lo hacemos». ¿Qué respondes?", "Que no, porque anotarlo terminado falsea el registro, y que lo informarás como pendiente", "Que sí, porque mañana lo harán", "Que sí, si es una tarea corta", "Un pendiente se informa como tal."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿cuenta una tarea en proceso como terminada?", "No", "Solo cuenta lo terminado con su registro completo."),
        ("¿Cómo se calculan las horas de trabajo?", "Personas por las horas de cada una", "Se multiplican las personas por las horas."),
        ("¿Quién decide liberar la aeronave?", "Personal certificado", "El informe de turno no decide eso."),
    ],
    op=("Informe de ejemplo: turno de la tarde con 10 tareas planificadas, 7 terminadas con registro completo, 2 en proceso y 1 pendiente por falta de un documento. Trabajaron 5 personas, 6 horas cada una. Una tarea vence a las 900 HV y la aeronave acumula 875 HV. Escribe (a) el avance en porcentaje, (b) las horas de trabajo, (c) cuántas HV faltan para el vencimiento, (d) cómo informas el pendiente y a quién.",
        "(a) 7 × 100 / 10 = 70 %. (b) 5 × 6 = 30 horas. (c) 900 - 875 = 25 HV. (d) Escribo el pendiente con su motivo (falta un documento) y su responsable, y lo informo al responsable del turno y al turno siguiente; la liberación la decide personal certificado.",
        ["calcula el avance", "calcula las horas", "calcula lo que falta", "informa el pendiente con motivo"],
        ["hoja con las cuatro respuestas"],
        ["contar en proceso como terminado", "calcular mal las horas", "ocultar el pendiente"],
        "Pregunta: «¿qué estado tiene cada tarea?». Si duda, pídele que relea cómo se calcula el avance."),
    reinforce="Escribe un informe de entrega de turno de seis líneas con datos inventados y calcula su avance.",
    extend="Explica por qué ocultar un pendiente puede afectar la seguridad del turno siguiente.",
)

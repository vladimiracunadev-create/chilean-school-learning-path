"""Administración 3.º medio TP: OAE-03 (seguimiento e informes de un programa operativo) y OAE-04 (atención de clientes internos y externos). Empresas, personas y cifras inventadas; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, bitácoras, correos y diálogos están escritos en cada ejercicio: las empresas y las personas son inventadas y las cifras son «de ejemplo», "
             "así que no necesitas programas, teléfono ni internet. No uses datos personales ni documentos reales de clientes o trabajadores. "
             "Este cuaderno enseña técnicas y cálculos básicos en papel; los derechos de las personas consumidoras y las obligaciones de la empresa se consultan en la norma vigente y con tu docente de la especialidad. "
             "Cuida tu postura al escribir y descansa la vista y la voz con pausas cortas.")

build = make_build(MATERIALS)

O3 = "TP-ADMI-3-OAE-03"
O4 = "TP-ADMI-3-OAE-04"

# ============================================================ OAE-03, clase 1
F = ("Ficha 11 (caso de ejemplo, inventado). «Servicios Maitén Ltda.» tiene un programa de 6 semanas para digitar 600 facturas. Al terminar la semana 3 se hace el seguimiento. "
     "La bitácora (registro diario de lo hecho) muestra 270 facturas digitadas; el programa esperaba 300 a esa fecha. La jefa del área, Daniela, pide un informe de avance para el viernes.")
build(
    O3, 1, F,
    use="Aprenderé qué es el seguimiento de un programa operativo, por qué se basa en evidencias y qué cuidados éticos exige al informar.",
    prior=["Sé qué es un programa operativo y sus elementos.", "Sé calcular diferencias y porcentajes simples.", "Sé qué es una meta."],
    explain=[
        "Hacer seguimiento a un programa operativo es comparar lo programado con lo realmente hecho, para saber si se avanza como se esperaba y qué corregir. Se basa en evidencias: registros fechados, planillas, documentos y observaciones anotadas por el responsable. Una impresión o un recuerdo no son evidencia, porque nadie puede revisarlos.",
        "El seguimiento debe considerar todos los elementos del programa: las personas (sus horas), los insumos, el equipamiento, la distribución temporal y los resultados esperados. Una técnica común es la bitácora, el registro diario de lo hecho. Con ella se calcula el avance y se compara con lo esperado a esa fecha. Los resultados se escriben en un informe de avance dirigido a la jefatura.",
        "El informe debe ser fiel: usa las cifras reales, indica la fuente y declara los datos provisionales. Maquillar una cifra para evitar un llamado de atención es una falta ética que además lleva a malas decisiones. Los datos personales de las trabajadoras y los trabajadores, como el motivo de una ausencia, se mantienen reservados.",
    ],
    vocab=[("seguimiento", "comparar lo programado con lo realizado"), ("evidencia", "registro que prueba un hecho o una cifra"), ("bitácora", "registro diario de lo que se hizo"), ("avance", "parte del trabajo ya realizada"), ("informe de avance", "documento que resume el seguimiento para la jefatura"), ("dato provisional", "cifra aún por confirmar")],
    worked=[
        ("Comparar", "Un taller ficticio esperaba 50 piezas a la semana 2 y la bitácora muestra 45. ¿Cuál es la diferencia y qué porcentaje de lo esperado se logró?", ["Diferencia = 50 − 45 = 5.", "Porcentaje = 45 × 100 ÷ 50 = 90."], "Faltan 5 piezas; se logró el 90 %"),
        ("Evidencia", "Un supervisor ficticio dice «creo que vamos bien». ¿Es evidencia?", ["Una opinión sin registro no se puede revisar.", "La evidencia sería la planilla fechada con las cantidades."], "No es evidencia"),
    ],
    mistakes=[("Informar «vamos bien» sin cifras.", "Sin cifras, la jefatura no puede decidir ni comprobar.", "Escribe lo programado, lo realizado, la diferencia y la fuente."),
              ("Cambiar una cifra para evitar reclamos.", "Es una falta ética y engaña a la jefatura.", "Informa la cifra real y explica las causas del atraso.")],
    T=[
        ("abc", "En Administración: ¿qué es hacer seguimiento a un programa operativo?", "Comparar lo programado con lo realizado usando evidencias", "Escribir el programa por primera vez", "Cambiar las metas cuando hay atrasos", "El seguimiento mide el avance real frente a lo programado; no crea ni cambia las metas."),
        ("abc", "{F} ¿Qué es la bitácora?", "El registro diario de lo hecho", "La lista de precios de la empresa", "El plan para varios años", "La bitácora anota cada día lo realizado, y sirve de base del seguimiento."),
        ("abc", "¿Cuál de estas es una evidencia válida?", "Una planilla fechada con las cantidades anotadas por el responsable", "Un comentario sin registro de un compañero", "Una cifra recordada de memoria", "Solo un registro fechado puede revisarse y respaldar la cifra."),
        ("=", "{F} ¿Cuántas facturas faltaban por digitar para llegar a lo esperado a la semana 3?", "300-270", "Diferencia = esperado − realizado.", " facturas"),
        ("=", "{F} ¿Qué porcentaje de lo esperado a la semana 3 se logró?", "270*100//300", "Porcentaje = realizado × 100 ÷ esperado.", " %"),
        ("=", "{F} ¿Qué porcentaje del total del programa (600 facturas) está hecho?", "270*100//600", "Porcentaje del total = realizado × 100 ÷ total.", " %"),
        ("=", "{F} ¿Cuántas facturas faltan para completar las 600 del programa?", "600-270", "Faltante = total − realizado.", " facturas"),
        ("abc", "{F} Con el 90 % de lo esperado a la semana 3, ¿qué conclusión es adecuada?", "Hay un atraso de 10 % respecto de lo esperado: se informa y se buscan las causas", "El programa ya terminó", "No hay atraso, porque 90 es un número alto", "El 90 % indica que falta un 10 % de lo esperado a esa fecha."),
        ("abc", "Daniela pide el informe y a un digitador se le olvidó anotar un día en la bitácora. ¿Qué hace quien elabora el informe?", "Consulta al digitador y marca el dato como provisional mientras tanto", "Inventa la cifra más probable", "Deja el día en blanco sin avisar", "Un dato faltante se consulta y se declara provisional; no se inventa ni se esconde."),
        ("abc", "Un compañero propone informar 300 facturas aunque la bitácora dice 270 «para que no haya reto». ¿Qué corresponde?", "Rechazarlo e informar la cifra real con sus causas", "Aceptarlo si Daniela no revisa", "Aceptarlo si nadie sale perjudicado", "Informar una cifra falsa es una falta ética aunque no se note."),
        ("abc", "Un informe sobre atrasos nombra el motivo médico de la ausencia de una persona. ¿Qué corresponde?", "Indicar solo «ausencia» y mantener reservado el motivo personal", "Dejar el motivo para que se entienda mejor", "Agregar el diagnóstico completo para que la jefatura decida", "Los datos personales son reservados; basta informar el efecto en el programa."),
        ("abc", "¿Qué elementos del programa debe considerar el seguimiento?", "Personas, insumos, equipamiento, tiempo y resultados", "Solo el tiempo", "Solo los resultados", "El seguimiento mira todos los elementos del programa, no uno solo."),
        ("abc", "{F} ¿A quién se dirige el informe de avance que pide Daniela?", "A la jefatura que decide con esa información", "A cualquier persona fuera de la empresa", "Solo al digitador que cometió el atraso", "El informe de avance informa a quien toma decisiones sobre el programa."),
    ],
    ctx=("abc", "Daniela recibe un informe que dice «270, 300, 90 %» sin explicar qué significa cada número. ¿Qué le falta?", "Indicar qué es realizado, qué es esperado, el porcentaje y la fuente", "Más colores en las letras", "Un título más largo", "Un informe necesita que cada cifra se identifique y tenga su fuente."),
    sc=[
        ("En Administración: ¿por qué el seguimiento usa evidencias?", "Porque las cifras deben poder comprobarse", "Solo lo registrado puede revisarse y respaldarse."),
        ("¿Qué haces si un dato del informe está sin confirmar?", "Lo declaro como provisional", "Un dato dudoso se declara y se confirma después."),
        ("¿Qué datos del informe se mantienen reservados?", "Los datos personales de las personas", "El motivo de una ausencia es un dato personal."),
    ],
    op=("Con la Ficha 11, escribe un informe de avance de cinco líneas para Daniela: período, cifra realizada, cifra esperada, diferencia y porcentaje, y una frase con la fuente de las cifras. Termina con un dato que declararías provisional si no estuviera confirmado.\n{F}",
        "Período: semanas 1 a 3. Realizadas: 270 facturas. Esperadas: 300. Diferencia: 30 facturas, 90 % de lo esperado. Fuente: bitácora diaria del área. Dato provisional: lo digitado el último día, hasta confirmar con el responsable.",
        ["usa las cifras de la ficha", "calcula diferencia y porcentaje", "nombra la fuente", "declara un dato provisional"],
        ["informe de cinco líneas con cifras y fuente"],
        ["cifras sin fuente", "ocultar el atraso", "incluir datos personales"],
        "Comprueba cada cifra con la ficha. Si no hay fuente, pide que la agregue."),
    reinforce="Anota cinco días de bitácora de un trabajo ficticio con cantidad hecha y suma lo realizado en la semana.",
    extend="Explica con un ejemplo inventado cómo una cifra falsa puede llevar a una mala decisión de la jefatura.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 12 (formatos de ejemplo, inventados) de «Servicios Maitén Ltda.». Formato A, bitácora: fecha, actividad, cantidad hecha, responsable, observación. Formato B, lista de cotejo: actividad, ¿cumplida? (sí o no), evidencia. "
     "Formato C, informe de avance: período, resumen, cifras, desviaciones, causas, propuestas y firma de quien lo elabora. Formato D, semáforo con criterio de ejemplo de la empresa: verde si el avance es 100 % o más de lo esperado; "
     "amarillo si está entre 80 % y 99 %; rojo si está bajo 80 %.")
build(
    O3, 2, F,
    use="Aprenderé los documentos del seguimiento (bitácora, lista de cotejo, informe y semáforo) y los roles de quienes registran, revisan e informan.",
    prior=["Sé qué es el seguimiento y qué es una evidencia.", "Sé calcular porcentajes simples.", "Sé qué es una desviación."],
    explain=[
        "El seguimiento usa documentos con función propia. La bitácora registra día a día lo realizado. La lista de cotejo marca si cada actividad se cumplió y cuál es su evidencia. El informe de avance resume el período para la jefatura con cifras, desviaciones, causas y propuestas. El semáforo clasifica el avance con colores según un criterio fijado por la empresa; en este cuaderno el criterio es de ejemplo.",
        "Una desviación es la diferencia entre lo programado y lo realizado. Puede ser un atraso (se hizo menos) o un adelanto (se hizo más). Una causa es el hecho que explica la desviación, por ejemplo la falta de un insumo. Una propuesta es la medida que se sugiere para corregir; la decide la jefatura.",
        "Los roles se distinguen: el responsable de cada actividad anota en la bitácora; quien hace el seguimiento revisa, calcula y arma el informe; la jefatura analiza y decide. Quien informa no culpa a personas sin evidencia: se describen hechos y efectos sobre el programa, no juicios sobre alguien.",
    ],
    vocab=[("desviación", "diferencia entre lo programado y lo realizado"), ("atraso", "se hizo menos de lo programado"), ("adelanto", "se hizo más de lo programado"), ("causa", "hecho que explica una desviación"), ("lista de cotejo", "pauta que marca si cada actividad se cumplió"), ("semáforo", "clasificación del avance por colores")],
    worked=[
        ("Elegir el color", "Con el criterio del semáforo, una actividad de ejemplo logró el 85 % de lo esperado. ¿Qué color corresponde?", ["85 está entre 80 y 99.", "Ese tramo es amarillo."], "Amarillo"),
        ("Distinguir atraso de adelanto", "Se esperaba hacer 40 y se hicieron 46. ¿Es atraso o adelanto?", ["46 es mayor que 40.", "Se hizo más de lo programado."], "Adelanto de 6"),
    ],
    mistakes=[("Escribir en el informe «culpa de Pedro» sin evidencia.", "Atribuir culpas sin pruebas daña a la persona y no explica la causa.", "Describe el hecho registrado y su efecto en el programa."),
              ("Confundir la causa con la desviación.", "La desviación es la diferencia; la causa es lo que la explica.", "Escribe primero la cifra de la desviación y después su causa.")],
    T=[
        ("abc", "En Administración: ¿qué es una desviación?", "La diferencia entre lo programado y lo realizado", "Un cambio de domicilio de la empresa", "El nombre de una actividad", "La desviación mide cuánto se aparta lo real de lo programado."),
        ("abc", "{F} ¿Qué formato marca si cada actividad se cumplió y su evidencia?", "La lista de cotejo (Formato B)", "La bitácora (Formato A)", "El semáforo (Formato D)", "El Formato B pregunta si la actividad fue cumplida y cuál es su evidencia."),
        ("abc", "{F} ¿Qué color del semáforo corresponde a un avance de 100 %?", "Verde", "Amarillo", "Rojo", "El criterio de ejemplo asigna verde a 100 % o más."),
        ("abc", "{F} ¿Qué color corresponde a un avance de 72 %?", "Rojo", "Amarillo", "Verde", "72 % está bajo 80 %, que es el límite del rojo en el criterio de ejemplo."),
        ("abc", "¿Qué es una causa en el informe de avance?", "El hecho que explica la desviación", "La cifra de la desviación", "La firma de quien informa", "La causa explica por qué hay desviación, y la cifra la mide."),
        ("abc", "¿Quién decide la medida correctiva que propone el informe?", "La jefatura", "El responsable de la bitácora solo", "Ninguna persona", "El informe propone y la jefatura decide."),
        ("=", "Se esperaba hacer 80 revisiones y se hicieron 68. ¿Qué porcentaje de lo esperado se logró?", "68*100//80", "Porcentaje = realizado × 100 ÷ esperado.", " %"),
        ("abc", "{F} Una actividad de ejemplo logró el 85 % de lo esperado. ¿Qué color del semáforo corresponde?", "Amarillo", "Verde", "Rojo", "85 % está entre 80 % y 99 %, tramo amarillo del criterio de ejemplo."),
        ("=", "Se esperaban 120 consultas atendidas y se atendieron 90. ¿Qué porcentaje de lo esperado se logró?", "90*100//120", "Porcentaje = realizado × 100 ÷ esperado.", " %"),
        ("abc", "{F} Con 75 % de avance, ¿qué color y qué acción se esperan según el criterio?", "Rojo: se informa y se propone una medida correctiva", "Verde: no se hace nada", "Amarillo: se omite en el informe", "Bajo 80 % es rojo; el informe lo muestra con su causa y su propuesta."),
        ("abc", "Un informe dice: «El atraso fue por la inutilidad de Rocío». ¿Qué corrección corresponde?", "Describir el hecho registrado, como «faltaron 12 horas de digitación», sin juicios sobre la persona", "Dejarlo igual, porque es honesto", "Agregar el apellido completo para identificarla", "El informe describe hechos y efectos; los juicios sobre personas no son evidencia."),
        ("abc", "El responsable anota en la bitácora «se hizo mucho». ¿Qué mejora el registro?", "Anotar la cantidad exacta y la fecha", "Anotar la opinión de otro compañero", "Dejarlo en blanco", "Una bitácora útil registra cantidades y fechas verificables."),
        ("abc", "{F} Quien hace el seguimiento nota que dos cifras de la bitácora y del informe no coinciden. ¿Qué hace?", "Revisa los registros y corrige con evidencia antes de entregar", "Usa la cifra más alta", "Entrega ambas sin explicarlo", "Las cifras deben coincidir; se revisa la causa con los registros."),
    ],
    ctx=("abc", "La jefa quiere ver de un vistazo qué actividades van bien y cuáles no. ¿Qué formato de la ficha le muestra eso?", "El semáforo", "La bitácora", "La firma del informe", "El semáforo resume con colores el estado de cada actividad."),
    sc=[
        ("En Administración: ¿qué diferencia hay entre atraso y adelanto?", "Atraso es hacer menos de lo programado; adelanto, hacer más", "La desviación puede ir en cualquiera de los dos sentidos."),
        ("¿Qué contiene el informe de avance?", "Período, resumen, cifras, desviaciones, causas, propuestas y firma", "Cada parte ayuda a decidir a la jefatura."),
        ("¿Por qué no se culpa a personas sin evidencia?", "Porque no se puede comprobar y daña a la persona", "El informe describe solo hechos registrados y no juicios personales."),
    ],
    op=("Con la Ficha 12, arma un informe de avance de ejemplo con estos datos inventados: esperadas 200 consultas, atendidas 150 (causa: faltó un equipo 2 días). Incluye cifras, porcentaje, color del semáforo, causa descrita sin culpas y una propuesta.\n{F}",
        "Período: semana 2. Esperadas: 200 consultas; atendidas: 150; desviación: 50 (75 %). Semáforo: rojo. Causa: un equipo no estuvo disponible 2 días, según la bitácora. Propuesta: reservar un equipo de respaldo, sujeto a la decisión de la jefatura.",
        ["calcula el porcentaje", "asigna el color del criterio", "describe la causa sin culpas", "propone una medida"],
        ["informe de ejemplo de seis líneas"],
        ["culpar a una persona", "no indicar la fuente", "no asignar color"],
        "Verifica el porcentaje y el color. Si hay juicio sobre una persona, pide reescribirlo como hecho registrado."),
    reinforce="Dibuja un semáforo de tres colores con los criterios de la ficha y clasifica cinco porcentajes que inventes.",
    extend="Explica con un ejemplo inventado por qué dos informes con el mismo color pueden requerir medidas distintas.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 13 (tabla de seguimiento de ejemplo, inventada), cierre de la semana 4 de «Servicios Maitén Ltda.». Actividad A, orden del archivo: programado 40 horas, realizado 40. "
     "Actividad B, atención de consultas: programado 120 consultas, realizado 96. Actividad C, digitación de facturas: programado 400 facturas, realizado 300. "
     "Observaciones de la bitácora: el computador 1 estuvo fuera de uso 2 días; faltó papel una tarde; una persona estuvo ausente 5 días por permiso. Criterio del semáforo de ejemplo: verde 100 % o más; amarillo 80 % a 99 %; rojo bajo 80 %.")
build(
    O3, 3, F,
    use="Aprenderé a analizar una tabla de seguimiento en papel: calcular desviaciones, asignar colores y relacionar cada atraso con su causa y con el elemento del programa.",
    prior=["Sé calcular porcentajes de avance.", "Sé el criterio del semáforo.", "Sé qué elementos tiene un programa."],
    explain=[
        "Analizar una tabla de seguimiento tiene cuatro pasos. Primero se calcula, para cada actividad, la desviación y el porcentaje de avance. Segundo se asigna el color del semáforo con el criterio acordado. Tercero se busca la causa de cada desviación en la bitácora y en otras evidencias. Cuarto se identifica qué elemento del programa fue afectado: personas, insumos, equipamiento, tiempo o resultados.",
        "Una causa solo se acepta si tiene evidencia. Por ejemplo, «el computador 1 estuvo fuera de uso 2 días» está en la bitácora, y afecta al equipamiento. «Faltó papel una tarde» afecta a los insumos, y la ausencia de una persona afecta a los recursos humanos. No toda desviación tiene una sola causa: varias pueden sumarse.",
        "Después del análisis se priorizan las actividades. Se atiende primero la que está en rojo y la que más afecta la meta del programa. Las propuestas son concretas y se presentan a la jefatura con el efecto que se espera.",
    ],
    vocab=[("desviación", "diferencia entre lo programado y lo realizado"), ("porcentaje de avance", "realizado × 100 ÷ programado"), ("causa", "hecho que explica una desviación"), ("elemento afectado", "parte del programa que sufre el problema"), ("prioridad", "lo que se atiende primero"), ("propuesta", "medida sugerida a la jefatura")],
    worked=[
        ("Calcular y colorear", "Una actividad de ejemplo programó 50 y realizó 45. ¿Qué porcentaje es y qué color tiene según el criterio?", ["45 × 100 ÷ 50 = 90.", "90 % está entre 80 % y 99 %."], "90 %, amarillo"),
        ("Elemento afectado", "Se anotó en una bitácora de ejemplo que se acabó el tóner de una impresora. ¿Qué elemento del programa se afecta?", ["El tóner se consume al trabajar.", "Es un insumo."], "Insumos"),
    ],
    mistakes=[("Explicar el atraso con una causa que no está en ninguna evidencia.", "No se puede comprobar y puede ocultar la causa real.", "Busca la causa en la bitácora u otro registro."),
              ("Atender primero la actividad que tiene menos desviación.", "Se gasta tiempo en lo menos urgente.", "Prioriza lo que está en rojo y más afecta la meta.")],
    T=[
        ("abc", "En Administración: ¿cómo se calcula el porcentaje de avance de una actividad?", "Realizado por 100 dividido por programado", "Programado por 100 dividido por realizado", "Realizado menos programado", "El avance compara lo realizado con lo programado y se expresa sobre 100."),
        ("=", "{F} ¿Qué porcentaje de avance tiene la actividad A?", "40*100//40", "Avance = realizado × 100 ÷ programado.", " %"),
        ("=", "{F} ¿Qué porcentaje de avance tiene la actividad B?", "96*100//120", "Avance = realizado × 100 ÷ programado.", " %"),
        ("=", "{F} ¿Qué porcentaje de avance tiene la actividad C?", "300*100//400", "Avance = realizado × 100 ÷ programado.", " %"),
        ("abc", "{F} ¿Qué color del semáforo corresponde a la actividad B?", "Amarillo", "Verde", "Rojo", "El avance de B es 80 %, que está en el tramo amarillo (80 % a 99 %)."),
        ("abc", "{F} ¿Qué color corresponde a la actividad C?", "Rojo", "Amarillo", "Verde", "El avance de C es 75 %, bajo el 80 % del criterio."),
        ("=", "{F} ¿Cuántas facturas faltan a la actividad C respecto de lo programado?", "400-300", "Desviación = programado − realizado.", " facturas"),
        ("abc", "{F} El computador 1 estuvo fuera de uso 2 días. ¿Qué elemento del programa afecta?", "El equipamiento", "Los insumos", "Los resultados esperados", "Un computador es un equipo, y su falla afecta al equipamiento."),
        ("abc", "{F} Faltó papel una tarde. ¿Qué elemento afecta?", "Los insumos", "El equipamiento", "La distribución temporal", "El papel se consume al trabajar, por lo tanto es un insumo."),
        ("abc", "{F} Una persona estuvo ausente 5 días por permiso. ¿Qué elemento afecta y cómo debe informarse?", "Los recursos humanos; se informa «ausencia de 5 días» sin detallar el motivo personal", "Los insumos; se informa el motivo completo", "El equipamiento; se omite del informe", "La ausencia reduce las horas de personas, y el motivo es un dato personal reservado."),
        ("abc", "{F} ¿Qué actividad conviene atender primero?", "La C, porque está en rojo y es la que más se aparta de lo programado", "La A, porque ya está completa", "La B, porque es la segunda de la lista", "Se prioriza lo que está en rojo y más afecta la meta."),
        ("abc", "{F} Un compañero dice que el atraso de C se debe «a que la gente es floja». ¿Qué respondes?", "Que la causa debe estar respaldada en la bitácora y describir hechos, no juicios", "Que es una explicación válida", "Que se escriba en el informe en mayúsculas", "Sin evidencia, una frase así no es una causa aceptable."),
        ("abc", "{F} Si el computador 1 se repara y no se ausenta nadie, ¿qué parte del atraso de C podría recuperarse?", "La causada por la falla del equipo y por las horas perdidas, que se podrían reponer en las semanas siguientes", "Ninguna, porque los atrasos nunca se recuperan", "Toda, aunque falte el papel", "Si se eliminan las causas, las semanas siguientes pueden reponer horas; no hay garantías."),
    ],
    ctx=("abc", "Daniela pregunta cuál es el problema más grave de la tabla. ¿Qué responde un buen informe?", "La actividad C: 75 % de avance, rojo, con causas de equipamiento y de personas registradas", "Que todas las actividades están igual", "Que no hay problemas porque la A está completa", "Un buen informe prioriza lo más grave con cifras y causas respaldadas."),
    sc=[
        ("En Administración: ¿cuál es el primer paso del análisis de la tabla?", "Calcular la desviación y el porcentaje", "Antes de buscar causas se miden las desviaciones."),
        ("¿Qué elementos del programa pueden verse afectados?", "Personas, insumos, equipamiento, tiempo y resultados", "El análisis relaciona cada causa con un elemento."),
        ("¿Qué se atiende primero?", "Lo que está en rojo y más afecta la meta", "La prioridad ordena qué medida se atiende primero."),
    ],
    op=("Con la Ficha 13, escribe un análisis de seis líneas: porcentaje y color de cada actividad, causa y elemento afectado de la actividad en rojo, y una propuesta para recuperar el atraso, con el supuesto que declararías.\n{F}",
        "A: 100 %, verde. B: 80 %, amarillo. C: 75 %, rojo. En C, la causa es la falla del computador 1 (2 días), el faltante de papel y la ausencia de una persona; afecta equipamiento, insumos y recursos humanos. Propuesta: reservar un equipo y papel de respaldo y reprogramar horas de la semana 5. Supuesto: no habrá nuevas ausencias.",
        ["calcula los tres porcentajes", "asigna los colores", "relaciona causas con elementos", "propone una medida con supuesto"],
        ["análisis de seis líneas"],
        ["culpar a personas", "colores equivocados", "propuestas sin supuesto"],
        "Verifica porcentajes y colores. Si la propuesta es vaga, pide que diga qué se hará y cuándo."),
    reinforce="Toma una tabla de tres actividades que inventes y calcula porcentajes y colores.",
    extend="Explica con un ejemplo inventado cómo cambiaría la prioridad si la actividad A estuviera en rojo.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 14 (datos de ejemplo, inventados). Programa de «Servicios Maitén Ltda.» de 6 semanas para digitar 600 facturas. Al cierre de la semana 4 se llevan 300 facturas digitadas (ritmo real de 75 facturas por semana). "
     "Equipo: 3 personas, cada una disponible 40 horas semanales; el rendimiento de ejemplo es de 5 facturas por hora y persona. Semanas restantes: 2. La jefatura pide una proyección y una medida correctiva con base en evidencias.")
build(
    O3, 4, F,
    use="Aprenderé a proyectar el cierre de un programa con el ritmo real, a calcular qué se necesita para cumplirlo y a redactar un informe breve con evidencias.",
    prior=["Sé calcular el avance y la desviación.", "Sé usar el semáforo.", "Sé calcular capacidad en horas."],
    explain=[
        "Con el seguimiento se puede proyectar cómo terminará el programa. Si se mantiene el ritmo real, la proyección es: realizado hasta hoy + ritmo semanal × semanas restantes. Se compara con el total esperado para saber si se cumplirá. Es una estimación y se declara como tal, porque el ritmo puede cambiar.",
        "Si la proyección no alcanza, se calcula qué se necesita: el ritmo requerido es lo que falta dividido por las semanas restantes. Se compara con la capacidad del equipo (personas × horas × rendimiento) para saber si el equipo puede lograrlo o si hace falta una medida correctiva, por ejemplo más horas o más personas, que decide la jefatura.",
        "El informe breve debe tener: situación actual con cifras, proyección con su supuesto, ritmo requerido, capacidad disponible, propuesta y fuente de los datos. Cada cifra debe poder rastrearse a la bitácora o a la ficha de seguimiento.",
    ],
    vocab=[("proyección", "estimación de cómo terminará el programa"), ("ritmo real", "cantidad hecha por semana hasta hoy"), ("ritmo requerido", "cantidad por semana que se necesita para cumplir"), ("capacidad", "trabajo máximo que puede hacer el equipo"), ("medida correctiva", "acción para recuperar un atraso"), ("supuesto", "condición que se declara al proyectar")],
    worked=[
        ("Proyectar", "Un equipo de ejemplo lleva 120 piezas en 3 semanas (ritmo de 40 por semana) y le quedan 2 semanas. ¿Cuántas piezas tendrá si mantiene el ritmo?", ["Se agregan 40 × 2 = 80.", "120 + 80 = 200."], "200 piezas"),
        ("Ritmo requerido", "Para cerrar el programa anterior se necesitan 260 piezas. ¿Qué ritmo semanal se requiere en las 2 semanas restantes?", ["Faltan 260 − 120 = 140.", "140 ÷ 2 = 70 por semana."], "70 piezas por semana"),
    ],
    mistakes=[("Presentar la proyección como un hecho seguro.", "Es una estimación que depende de que el ritmo se mantenga.", "Declara el supuesto con que proyectas."),
              ("Pedir más personas sin comparar el ritmo requerido con la capacidad.", "Se puede gastar recursos sin necesidad o quedarse corto.", "Calcula la capacidad y compárala con lo que se requiere.")],
    T=[
        ("abc", "En Administración: ¿qué es una proyección en un programa?", "Una estimación de cómo terminará el programa si algo se mantiene", "Un hecho que ya ocurrió", "Un cambio de la meta fijada", "La proyección estima el cierre con un supuesto declarado."),
        ("=", "{F} ¿Cuántas facturas tendrá digitadas al cierre si mantiene el ritmo de 75 por semana durante las 2 semanas restantes?", "300+75*2", "Proyección = realizado + ritmo × semanas restantes.", " facturas"),
        ("=", "{F} ¿Cuántas facturas faltan para completar las 600?", "600-300", "Faltante = total − realizado.", " facturas"),
        ("=", "{F} ¿Cuántas facturas por semana se requieren en las 2 semanas restantes?", "(600-300)//2", "Ritmo requerido = faltante ÷ semanas restantes.", " facturas por semana"),
        ("=", "{F} ¿Cuántas facturas digita una persona en un día de 8 horas, con el rendimiento de ejemplo de 5 por hora?", "8*5", "Facturas del día = horas × facturas por hora.", " facturas"),
        ("=", "{F} ¿Cuántas facturas puede digitar el equipo en una semana a plena capacidad (3 personas × 40 horas × 5 por hora)?", "3*40*5", "Capacidad semanal = personas × horas × rendimiento.", " facturas"),
        ("abc", "{F} ¿Puede el equipo cumplir el ritmo requerido de 150 por semana?", "Sí, porque su capacidad de 600 por semana es mayor", "No, porque el ritmo requerido es mayor que su capacidad", "No se puede saber sin conocer el salario", "La capacidad semanal supera el ritmo requerido, por eso es posible si se dedican las horas."),
        ("=", "{F} Si cada persona dedicara solo 10 horas semanales a esta tarea, ¿cuántas facturas digitaría el equipo por semana?", "3*10*5", "Con menos horas se rehace el cálculo de capacidad.", " facturas"),
        ("abc", "{F} Con solo 10 horas semanales por persona, ¿alcanza para el ritmo requerido de 150?", "Sí, porque 150 es igual al ritmo requerido", "No, porque 150 es mayor a lo que producen", "No, porque 10 horas es poco tiempo", "3 × 10 × 5 = 150, igual al ritmo que se requiere."),
        ("abc", "{F} ¿Cuál es el supuesto de la proyección con el ritmo de 75 por semana?", "Que el ritmo real se mantendrá igual las 2 semanas restantes", "Que la meta del programa cambiará a 450", "Que las facturas se digitan solas", "La proyección con ritmo real supone que el ritmo no cambiará."),
        ("abc", "La proyección da 450 y la meta es 600. ¿Qué debe decir el informe?", "Que al ritmo actual no se cumple la meta y se propone una medida correctiva", "Que la meta se cumple igual", "Que se corrige la meta a 450 sin consultar", "Si la proyección no alcanza, se informa y se propone una medida; la meta no se cambia por cuenta propia."),
        ("abc", "Un asistente propone mostrar solo la cifra de 600 «porque es la meta» y omitir la proyección. ¿Qué corresponde?", "Presentar la proyección real con su supuesto", "Omitir la proyección para no preocupar", "Presentar una proyección inventada más alta", "La jefatura necesita la información real para decidir."),
        ("abc", "¿Qué debe tener cada cifra del informe de seguimiento?", "Un respaldo que se pueda rastrear a la bitácora o ficha", "Un adjetivo que la describa", "El nombre de quien la inventó", "Cada cifra se rastrea a su fuente para poder comprobarla."),
    ],
    ctx=("abc", "Daniela lee la proyección de 450 facturas y pregunta qué hacer. ¿Qué propuesta es adecuada y respaldada?", "Pedir más horas por persona, porque el ritmo requerido (150) cabe en la capacidad del equipo", "Cambiar la meta a 450 sin decirle a nadie", "Despedir a la persona más lenta sin revisar", "La medida se apoya en la capacidad calculada y la decide la jefatura."),
    sc=[
        ("En Administración: ¿cómo se calcula el ritmo requerido?", "Lo que falta dividido por las semanas restantes", "Muestra cuánto debe hacerse por semana para cumplir."),
        ("¿Qué se compara con el ritmo requerido?", "La capacidad del equipo", "Así se ve si la meta es alcanzable."),
        ("¿Qué se declara siempre al proyectar?", "El supuesto", "Una proyección depende de que se mantenga algo."),
    ],
    op=("Con la Ficha 14, escribe un informe breve para Daniela con: facturas digitadas, proyección al cierre, faltante, ritmo requerido, capacidad semanal, una propuesta y el supuesto de tu proyección.\n{F}",
        "Digitadas: 300. Proyección al ritmo actual: 450. Faltan 300. Ritmo requerido: 150 por semana. Capacidad semanal: 600. Propuesta: aumentar las horas dedicadas por persona hasta alcanzar 150 por semana, sujeto a la decisión de la jefatura. Supuesto: no habrá nuevas ausencias ni fallas.",
        ["calcula proyección y ritmo requerido", "compara con la capacidad", "propone una medida", "declara el supuesto"],
        ["informe breve de siete líneas"],
        ["presentar la proyección como seguro", "no comparar con la capacidad", "cambiar la meta"],
        "Rehace las cuentas con la ficha. Si falta el supuesto, pídelo."),
    reinforce="Proyecta en papel el cierre de un programa ficticio de 100 piezas con 40 hechas en 2 de 5 semanas.",
    extend="Explica con un ejemplo inventado por qué una proyección puede cambiar si baja el ritmo.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 15 (caso de ejemplo, inventado). «Muebles Roble Ltda.» atiende a clientes externos (compradores y proveedores) y a clientes internos (otras áreas de la misma empresa). "
     "Situación 1: una compradora llama por teléfono y pregunta por el estado de su pedido. Situación 2: el encargado de bodega envía un correo a ventas para pedir una orden de despacho. "
     "Situación 3: un comprador reclama en el mostrador porque una pata de su silla llegó rota.")
build(
    O4, 1, F,
    use="Aprenderé quiénes son los clientes internos y externos, qué canales se usan para atenderlos y qué cuidados éticos y de privacidad exige la atención.",
    prior=["Sé redactar mensajes breves.", "Sé escuchar a otra persona sin interrumpir.", "Sé que los datos personales son reservados."],
    explain=[
        "Un cliente externo es una persona o empresa de fuera que compra o provee, como un comprador o un proveedor. Un cliente interno es otra persona o área de la misma empresa que necesita nuestro trabajo para hacer el suyo, como la bodega que espera una orden de ventas. Los dos se atienden con respeto, rapidez y claridad. Atender significa entender la necesidad o la demanda de la persona y dar una respuesta útil.",
        "La atención puede ser presencial (en persona) o a distancia, por teléfono, correo electrónico u otro medio escrito. Cada canal tiene cuidados propios: en persona se cuida el saludo y la postura; por teléfono, el tono de voz y la claridad; por correo, la redacción y que el asunto sea claro. El fax casi no se usa hoy, pero aparece en el objetivo oficial como ejemplo de medio.",
        "Hay cuidados éticos y legales. Se piden solo los datos necesarios y no se entregan datos de un cliente a otra persona. No se promete lo que no se puede cumplir. Los derechos de las personas consumidoras y los plazos de respuesta se consultan en la norma vigente y en las políticas de la empresa. Si una situación te supera, la derivas a tu jefatura.",
    ],
    vocab=[("cliente externo", "persona o empresa de fuera que compra o provee"), ("cliente interno", "persona o área de la misma empresa que necesita tu trabajo"), ("demanda", "lo que la persona pide o reclama"), ("canal", "medio por el que se atiende: en persona, teléfono, correo"), ("datos personales", "información que identifica a una persona y es reservada"), ("derivar", "pasar un caso a quien puede resolverlo")],
    worked=[
        ("Clasificar al cliente", "En una oficina ficticia, el área de contabilidad pide a recepción las fotocopias de un contrato. ¿Es cliente interno o externo?", ["Contabilidad es parte de la misma empresa.", "Por eso es cliente interno."], "Cliente interno"),
        ("Canal", "Un proveedor ficticio envía una consulta escrita por correo. ¿Es atención presencial o a distancia?", ["No está en la oficina.", "El correo es un medio a distancia."], "A distancia"),
    ],
    mistakes=[("Atender con prisa al cliente interno porque «no compra».", "El trabajo de otras áreas depende de tu respuesta, y una demora afecta al cliente externo.", "Atiende al cliente interno con el mismo respeto y claridad."),
              ("Dar por teléfono datos de un cliente a quien dice ser su familiar.", "Los datos personales son reservados y no se sabe quién llama.", "No entregues datos personales a terceros; consulta a la jefatura.")],
    T=[
        ("abc", "En Administración: ¿quién es un cliente interno?", "Otra área de la misma empresa que necesita tu trabajo", "Un comprador que viene de otra ciudad", "Un proveedor extranjero", "El cliente interno pertenece a la propia empresa; los otros son externos."),
        ("abc", "{F} En la situación 1, ¿qué canal de atención se usa?", "Teléfono, a distancia", "Presencial en el mostrador", "Correo electrónico", "La compradora llama por teléfono, que es un canal a distancia."),
        ("abc", "{F} ¿Quién es el cliente interno en la situación 2?", "El encargado de bodega, que necesita una orden de ventas", "La compradora que llama por teléfono", "El comprador que reclama en el mostrador", "El encargado de bodega trabaja en la misma empresa y pide un servicio a ventas."),
        ("abc", "{F} En la situación 3, ¿qué demanda presenta el cliente?", "Un reclamo por una pieza llegada rota", "Una consulta por un pedido", "Una solicitud interna de despacho", "El comprador reclama porque la pata de su silla llegó rota."),
        ("abc", "¿Qué significa atender al cliente?", "Entender su necesidad o demanda y dar una respuesta útil", "Terminar la conversación lo antes posible", "Convencerlo de no reclamar", "Atender es entender y responder; no es apurar ni evitar reclamos."),
        ("abc", "{F} ¿Qué dato necesita una persona de ventas para ubicar el pedido de la situación 1 sin pedir información innecesaria?", "El número de pedido o el nombre de quien compró", "La clave del correo personal de la compradora", "Los datos de su familia", "Se piden solo los datos necesarios para encontrar el pedido."),
        ("=", "En un día de ejemplo se atendieron 18 clientes externos y 7 clientes internos. ¿Cuántas personas se atendieron en total?", "18+7", "Se suman los dos tipos de clientes.", " personas"),
        ("=", "De 25 solicitudes de ejemplo de un día, 15 vinieron por teléfono y 4 por correo; el resto fue presencial. ¿Cuántas fueron presenciales?", "25-15-4", "Se restan las solicitudes a distancia del total.", " solicitudes"),
        ("abc", "Alguien que dice ser el hermano de un cliente llama y pide su dirección. ¿Qué corresponde?", "No entregarla y ofrecer que el cliente se comunique con la empresa", "Entregarla si parece amable", "Entregarla si sabe el nombre del cliente", "Los datos personales no se entregan a terceros; el titular puede pedirlos él mismo."),
        ("abc", "Un cliente interno pide un informe con urgencia. ¿Qué respuesta es adecuada?", "Preguntar el plazo, confirmar cuándo se entregará y cumplirlo", "Decir que espere sin dar plazo", "Ignorar el pedido porque no es un cliente externo", "Un cliente interno también merece una respuesta con plazo claro."),
        ("abc", "Una cliente pide un descuento que la empresa no autoriza. ¿Qué corresponde?", "Explicar lo que sí se puede ofrecer y derivar a la jefatura si insiste", "Prometerlo para evitar problemas", "Ofrecer uno distinto sin consultar", "No se promete lo que no se puede cumplir; se informa y se deriva."),
        ("abc", "Un reclamo presencial se vuelve tenso. ¿Qué es lo más adecuado?", "Mantener un tono calmado, escuchar y derivar a la jefatura si se necesita", "Gritar para que el cliente se calme", "Cerrar la ventanilla sin decir nada", "La calma y la derivación evitan que el conflicto crezca."),
        ("abc", "{F} Un cliente grita en el mostrador. ¿Cuál es una conducta profesional?", "Escuchar el reclamo completo y repetir lo que entendiste antes de proponer una solución", "Responder gritando", "Pedirle que se vaya", "Repetir lo entendido confirma el reclamo y baja la tensión."),
    ],
    ctx=("abc", "En «Muebles Roble» llega un correo de un proveedor y una llamada de un comprador al mismo tiempo. ¿Qué es lo más adecuado?", "Atender la llamada y avisar que se responderá el correo el mismo día, anotando ambos", "Ignorar la llamada para leer el correo", "Cortar la llamada para responder el correo", "Se atiende lo urgente y se registra lo pendiente con un plazo."),
    sc=[
        ("En Administración: ¿qué diferencia hay entre cliente interno y externo?", "El interno es de la misma empresa; el externo es de fuera", "Ambos tipos de cliente merecen buena atención y respeto."),
        ("¿Qué canales de atención hay?", "Presencial y a distancia, como teléfono y correo", "Cada canal de atención tiene cuidados propios que se deben conocer."),
        ("¿Qué haces con los datos personales de un cliente?", "Los mantengo reservados y no los entrego a terceros", "Son datos protegidos que solo se usan para atender."),
    ],
    op=("Con la Ficha 15, escribe una tabla con las tres situaciones y estas columnas: tipo de cliente, canal, demanda, y un cuidado que tendrías (ético o de privacidad) en cada una.\n{F}",
        "Situación 1: cliente externo; teléfono; consulta de estado de pedido; verificar solo datos necesarios. Situación 2: cliente interno; correo; orden de despacho; confirmar plazo. Situación 3: cliente externo; presencial; reclamo por pieza rota; escuchar y derivar si se necesita.",
        ["clasifica bien el tipo de cliente", "identifica el canal", "nombra la demanda", "nombra un cuidado"],
        ["tabla de tres filas y cuatro columnas"],
        ["confundir interno y externo", "pedir datos innecesarios", "prometer algo sin autorización"],
        "Verifica cada fila con la ficha. Si el cuidado es vago, pide un ejemplo concreto."),
    reinforce="Escribe tres ejemplos de clientes internos de un colegio ficticio y qué necesita cada uno.",
    extend="Explica con un ejemplo inventado cómo una mala atención a un cliente interno puede llegar a un cliente externo.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 16 (técnicas y formatos de ejemplo, inventados) de «Muebles Roble Ltda.». Técnicas orales: saludar y presentarse; escucha activa (no interrumpir, repetir lo entendido); preguntar para precisar; lenguaje claro y amable; confirmar el acuerdo. "
     "Técnicas escritas para correo: asunto claro, saludo, mensaje breve y ordenado, cierre cordial, nombre y cargo de quien escribe. Formatos: registro de atención (fecha, cliente, canal, demanda, respuesta, estado) y hoja de reclamo (fecha, hecho, solicitud, quién resuelve). "
     "Roles: ejecutivo(a) de atención, que atiende y registra; jefatura, a quien se deriva lo que supera su autorización.")
build(
    O4, 2, F,
    use="Aprenderé las técnicas de comunicación oral y escrita para atender, y los formatos y roles que ordenan la atención al cliente.",
    prior=["Sé quién es un cliente interno y uno externo.", "Sé qué canales existen.", "Sé que los datos personales se protegen."],
    explain=[
        "Las relaciones públicas son el conjunto de acciones que cuidan la imagen y la relación de la empresa con sus clientes. En la atención, eso se traduce en técnicas de comunicación. En la comunicación oral: saludar y presentarse, escuchar con atención sin interrumpir, repetir lo entendido, preguntar para precisar y usar un lenguaje claro y amable. Al terminar se confirma el acuerdo: qué se hará y cuándo.",
        "En la comunicación escrita, como un correo electrónico, se usa un asunto claro, un saludo, un mensaje breve y ordenado, un cierre cordial y la firma con nombre y cargo. Se evita escribir todo en mayúsculas, que se lee como un grito, y se revisa la ortografía antes de enviar. El tono es respetuoso aunque el mensaje recibido sea molesto.",
        "La atención se ordena con formatos: el registro de atención guarda fecha, cliente, canal, demanda, respuesta y estado; la hoja de reclamo recoge el hecho y la solicitud del cliente. El ejecutivo atiende y registra; la jefatura resuelve lo que supera su autorización. El registro contiene solo los datos necesarios y se guarda con reserva.",
    ],
    vocab=[("escucha activa", "escuchar sin interrumpir y repetir lo entendido"), ("asunto", "título breve de un correo"), ("registro de atención", "formato que guarda cada atención"), ("hoja de reclamo", "formato que recoge un reclamo"), ("relaciones públicas", "acciones que cuidan la relación con los clientes"), ("cierre cordial", "despedida amable de un mensaje")],
    worked=[
        ("Escucha activa", "Un cliente ficticio dice: «El sofá llegó con una mancha». Un ejecutivo responde: «Entiendo que el sofá llegó manchado. ¿Puede indicarme su número de pedido?». ¿Qué técnica usó?", ["Repitió lo entendido.", "Luego hizo una pregunta para precisar."], "Escucha activa y pregunta para precisar"),
        ("Asunto claro", "¿Cuál es mejor asunto para pedir una orden de despacho: «Hola» o «Solicitud de orden de despacho, pedido 482»?", ["El asunto debe decir de qué trata el correo.", "El segundo da el tema y el número."], "«Solicitud de orden de despacho, pedido 482»"),
    ],
    mistakes=[("Escribir un correo sin asunto o en mayúsculas.", "Es difícil de ubicar y se lee como un grito.", "Pon un asunto claro y usa mayúsculas solo donde corresponde."),
              ("Interrumpir al cliente para dar la solución.", "Puede resolverse otro problema que no era el real.", "Escucha completo, repite lo entendido y luego responde.")],
    T=[
        ("abc", "En Administración: ¿qué es la escucha activa?", "Escuchar sin interrumpir y repetir lo entendido", "Responder lo más rápido posible", "Tomar notas sin mirar a la persona", "La escucha activa confirma que se entendió lo que la persona dijo."),
        ("abc", "{F} ¿Qué técnica escrita corresponde a poner «Solicitud de despacho, pedido 482» en un correo?", "Un asunto claro", "Un cierre cordial", "Un saludo", "El asunto dice de qué trata el correo."),
        ("abc", "{F} ¿Qué datos guarda el registro de atención de la ficha?", "Fecha, cliente, canal, demanda, respuesta y estado", "Solo el nombre del cliente", "La clave del correo del cliente", "El formato de la ficha incluye esas seis columnas."),
        ("abc", "{F} ¿Quién resuelve un reclamo que supera la autorización del ejecutivo?", "La jefatura", "El propio cliente", "Otro cliente", "El ejecutivo deriva a la jefatura lo que supera su autorización."),
        ("abc", "¿Por qué se evita escribir todo en mayúsculas en un correo?", "Porque se lee como un grito y es poco cordial", "Porque no se entiende el contenido", "Porque la empresa lo prohíbe por el costo", "Las mayúsculas sostenidas se interpretan como un tono agresivo."),
        ("abc", "¿Qué se hace al terminar una atención oral?", "Confirmar qué se acordó y cuándo", "Cortar sin despedirse", "Pedir al cliente que repita todo el reclamo", "Confirmar el acuerdo evita malos entendidos."),
        ("=", "En un registro de ejemplo hay 40 atenciones; 28 están en estado «resuelto». ¿Cuántas están sin resolver?", "40-28", "Sin resolver = total − resueltas.", " atenciones"),
        ("=", "De 50 correos de ejemplo recibidos en una semana, 45 fueron respondidos el mismo día. ¿Qué porcentaje fue respondido el mismo día?", "45*100//50", "Porcentaje = respondidos × 100 ÷ recibidos.", " %"),
        ("abc", "{F} Un cliente dice por teléfono: «Mi pedido no llegó». ¿Cuál es la mejor respuesta del ejecutivo?", "«Entiendo que su pedido no llegó. ¿Me indica su número de pedido para revisarlo?»", "«Seguro se perdió, qué pena»", "«Llame mañana»", "Repite lo entendido y pregunta un dato necesario para actuar."),
        ("abc", "Un correo termina con «Saludos» sin nombre ni cargo. ¿Qué falta?", "La firma con nombre y cargo de quien escribe", "Un chiste", "Una foto de la persona", "La firma identifica a quien escribe y su rol."),
        ("abc", "{F} Una hoja de reclamo solo dice «el cliente estaba molesto». ¿Qué le falta?", "El hecho y la solicitud concretos del cliente", "El tono de voz del ejecutivo", "Una calificación de la personalidad del cliente", "La hoja de reclamo debe recoger hechos y solicitud, no opiniones."),
        ("abc", "El ejecutivo anota en el registro el número de teléfono personal de su cliente en una libreta personal. ¿Qué falla?", "Mal uso de datos personales: deben guardarse solo en el registro de la empresa", "Nada, porque la libreta es suya", "Falta escribir la fecha del cumpleaños", "Los datos de clientes pertenecen al registro de la empresa y se guardan con reserva."),
        ("abc", "{F} Un cliente interno pide una información por correo que otra persona debe autorizar. ¿Qué hace el ejecutivo?", "Informa que consultará a la persona autorizada y da un plazo", "La entrega sin autorización", "Rechaza el pedido sin explicación", "Sin autorización no se entrega, pero se orienta y se da un plazo."),
    ],
    ctx=("abc", "Una ejecutiva recibe un correo molesto de un proveedor. ¿Qué tono usa en la respuesta?", "Respetuoso y claro, resumiendo lo que entendió y lo que hará", "Molesto, para igualar el tono", "Sin saludo, para ahorrar tiempo", "El tono se mantiene respetuoso aunque el mensaje recibido sea duro."),
    sc=[
        ("En Administración: ¿qué incluye un buen correo?", "Asunto claro, saludo, mensaje breve, cierre y firma", "Esos elementos lo hacen claro y cordial."),
        ("¿Para qué sirve el registro de atención?", "Para guardar cada atención y su estado", "Permite hacer seguimiento y evita olvidar solicitudes pendientes."),
        ("¿Qué se hace con un reclamo que supera tu autorización?", "Se deriva a la jefatura", "El ejecutivo no resuelve lo que no le corresponde."),
    ],
    op=("Con la Ficha 16, redacta un correo de cinco líneas al cliente interno de bodega, respondiendo: «Necesito la orden de despacho del pedido 482». Debe tener asunto, saludo, mensaje breve, cierre y firma con nombre y cargo inventados, y una frase con el plazo.\n{F}",
        "Asunto: Orden de despacho, pedido 482. Hola, Jorge: te envío la orden de despacho del pedido 482 antes de las 16:00 de hoy. Si falta algún dato, avísame. Saludos, Camila Rojas, ejecutiva de ventas.",
        ["asunto claro", "mensaje breve y ordenado", "plazo concreto", "cierre y firma"],
        ["correo de cinco líneas"],
        ["sin asunto", "mensaje confuso", "mayúsculas sostenidas"],
        "Revisa cada elemento. Si falta el plazo, pide que lo agregue."),
    reinforce="Escribe en papel el diálogo de una atención telefónica de cinco líneas aplicando saludo, escucha activa y cierre.",
    extend="Explica con un ejemplo inventado por qué repetir lo entendido ayuda a evitar errores.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 17 (conversación de ejemplo, inventada) en «Muebles Roble Ltda.». Cliente: «Hola, compré un escritorio hace una semana y las instrucciones no vienen. Estoy muy molesto». "
     "Ejecutivo: «Mmm, eso no es conmigo, llame a bodega». Cliente: «Ya llamé y nadie contesta». Ejecutivo: «Entonces no sé, llame más tarde». Cliente: «¡Quiero hablar con alguien que me ayude!». "
     "Ejecutivo: «Pues espere». Datos que el ejecutivo tenía a mano: el registro de atención muestra el pedido 530, un escritorio, entregado el lunes; la jefatura, Sra. Pérez, está disponible; "
     "la política de ejemplo de la empresa es enviar el manual de armado por correo al cliente en el mismo día.")
build(
    O4, 3, F,
    use="Aprenderé a analizar una atención ya hecha, identificar lo que falló y proponer una mejor respuesta basada en técnicas y en la política de la empresa.",
    prior=["Conozco las técnicas orales y escritas de atención.", "Sé qué es derivar.", "Sé qué datos se piden."],
    explain=[
        "Analizar una atención es revisar una conversación, un correo o un registro para ver qué se hizo bien y qué falló. Se usan preguntas fijas: ¿se saludó y se escuchó?, ¿se entendió la necesidad?, ¿se pidió solo el dato necesario?, ¿se dio una solución o una derivación clara?, ¿se confirmó el acuerdo? y ¿se registró?",
        "En una mala atención suelen aparecer errores como: responder «eso no es conmigo» sin orientar, dejar al cliente esperando sin explicación, no usar los datos que ya están en el registro, o no derivar a quien puede resolver. Una respuesta mejor identifica la necesidad, usa la información disponible, ofrece una solución concreta dentro de la política de la empresa y, si no basta, deriva con un plazo.",
        "La atención se mide por lo que logra el cliente y por el respeto con que se le trata. Analizar el caso no es buscar culpables, sino mejorar el servicio. Los datos del cliente del caso se tratan con reserva incluso cuando se estudian en la capacitación.",
    ],
    vocab=[("orientar", "indicar a la persona qué hacer o a quién dirigirse"), ("política de la empresa", "regla interna de cómo se atiende"), ("derivación", "paso de un caso a quien puede resolverlo"), ("necesidad", "lo que el cliente realmente requiere"), ("acuerdo", "lo que se compromete a hacer y cuándo"), ("mejora", "cambio que hace mejor la atención")],
    worked=[
        ("Detectar el error", "Un ejecutivo ficticio responde «no sé, pregunte en otro lado» a una consulta de despacho. ¿Qué falló?", ["No orienta ni entrega una solución.", "No usa el registro para ayudar."], "No orientó ni buscó la solución"),
        ("Respuesta mejor", "Frente a ese caso, ¿qué respuesta sería mejor?", ["Debe usar el registro, entregar la información o derivar con un plazo.", "«Reviso su pedido ahora y le informo en unos minutos»."], "Revisar el pedido y dar un plazo claro"),
    ],
    mistakes=[("Decir «eso no es conmigo» y nada más.", "El cliente queda sin orientación y se siente ignorado.", "Indica a quién se debe dirigir o encárgate tú de derivarlo."),
              ("Dejar esperando al cliente sin explicar.", "No sabe si lo atenderán ni cuánto tardará.", "Explica el motivo y da un tiempo estimado.")],
    T=[
        ("abc", "En Administración: ¿para qué se analiza una atención ya hecha?", "Para mejorar el servicio, no para buscar culpables", "Para castigar al ejecutivo", "Para esconder errores", "El análisis busca aprender y mejorar la atención."),
        ("abc", "{F} ¿Cuál fue el primer error del ejecutivo en la conversación?", "Decir «eso no es conmigo» sin orientar al cliente", "Saludar con cortesía", "Pedir el número de pedido", "El ejecutivo no orientó y dejó al cliente sin una salida."),
        ("abc", "{F} ¿Qué dato ya disponible en el registro pudo haber usado el ejecutivo?", "El pedido 530, un escritorio entregado el lunes", "El apellido de la jefa", "El teléfono de otra clienta", "El registro mostraba el pedido del cliente y se podía usar de inmediato."),
        ("abc", "{F} ¿Qué dice la política de ejemplo de la empresa que el ejecutivo podía hacer?", "Enviar el manual de armado por correo el mismo día", "Devolver el dinero sin preguntar", "Cambiar el producto en el acto", "La política de ejemplo indica enviar el manual de armado por correo el mismo día."),
        ("abc", "{F} Cuando el cliente dijo «¡Quiero hablar con alguien que me ayude!», ¿qué debió hacer el ejecutivo?", "Derivar a la Sra. Pérez, que estaba disponible, o resolver con la política", "Decirle que esperara sin explicar", "Colgar", "Existía una jefatura disponible y una política para resolver el caso."),
        ("abc", "{F} ¿Qué técnica faltó al inicio de la atención?", "Escucha activa: repetir lo entendido", "Gritar para tomar el control", "Hablar más rápido", "Repetir el problema muestra que se entendió la necesidad."),
        ("=", "En una atención de ejemplo de 12 minutos, el ejecutivo dedicó 5 a escuchar y 4 a buscar el pedido en el registro. ¿Cuántos minutos quedaron para dar la solución?", "12-5-4", "Se restan los minutos de escucha y de búsqueda al total.", " minutos"),
        ("=", "En una semana de ejemplo hubo 60 atenciones y 9 quejas por mala orientación. ¿Cuántas atenciones no tuvieron esa queja?", "60-9", "Sin queja = total − quejas.", " atenciones"),
        ("=", "De esas 60 atenciones de ejemplo, 9 tuvieron queja por mala orientación. ¿Qué porcentaje del total son (aprox. entero)?", "9*100//60", "Porcentaje = quejas × 100 ÷ total.", " %"),
        ("abc", "{F} ¿Cuál de estas respuestas mejora la atención?", "«Entiendo que le faltan las instrucciones del escritorio. Le envío el manual por correo hoy; ¿me confirma su correo?»", "«No sé, llame de nuevo»", "«Es culpa de bodega»", "La respuesta repite lo entendido, ofrece una solución dentro de la política y pide un dato necesario."),
        ("abc", "El ejecutivo, para disculparse, comparte con otro cliente el reclamo completo del primero «como ejemplo». ¿Qué falla?", "Entrega datos de un cliente a otra persona", "Nada, porque ayuda a que otros aprendan", "Falta el nombre del producto", "Los datos del cliente son reservados y no se comparten."),
        ("abc", "{F} El cliente grita. ¿Qué respuesta mantiene la calma?", "«Lamento la molestia. Voy a ver su pedido ahora mismo»", "«No me grite»", "«Eso no es mi problema»", "Reconocer la molestia y actuar baja la tensión."),
        ("abc", "{F} Después de resolver, ¿qué debe hacer el ejecutivo?", "Anotar en el registro lo ocurrido y lo acordado", "Borrar el registro", "Contarlo a otros clientes", "El registro deja constancia de la atención y del acuerdo."),
    ],
    ctx=("abc", "Una ejecutiva de otra sucursal recibe un reclamo similar y no sabe si puede ofrecer un cambio. ¿Qué hace?", "Consulta la política de la empresa y deriva a la jefatura si supera su autorización", "Ofrece lo que se le ocurra", "Le dice al cliente que no hay solución", "Se actúa según la política y se deriva si supera la autorización."),
    sc=[
        ("En Administración: ¿qué se analiza en una atención?", "Escucha, necesidad, dato pedido, solución o derivación, acuerdo y registro", "Esas preguntas fijas ordenan el análisis de cualquier atención."),
        ("¿Qué es orientar?", "Indicar a la persona qué hacer o a quién dirigirse", "Orientar evita que el cliente quede sin salida."),
        ("¿Por qué no se buscan culpables?", "Porque el objetivo es mejorar el servicio", "El análisis de una atención sirve para aprender y mejorar."),
    ],
    op=("Con la Ficha 17, reescribe la conversación completa con una mejor atención de seis líneas, usando saludo, escucha activa, el dato del pedido 530, la política del manual y una derivación a la Sra. Pérez si el cliente no queda conforme.\n{F}",
        "Cliente: no vienen las instrucciones. Ejecutivo: Entiendo que al escritorio le faltan las instrucciones. Veo su pedido 530, entregado el lunes. Le envío el manual de armado por correo hoy; ¿me confirma su correo? Si no queda conforme, le derivo con la Sra. Pérez ahora mismo.",
        ["usa escucha activa", "usa el dato del registro", "aplica la política de ejemplo", "incluye derivación con plazo"],
        ["diálogo de seis líneas"],
        ["repetir los errores", "inventar políticas", "no mencionar datos del registro"],
        "Compara con la ficha. Si el diálogo promete algo que la política no dice, pide corregir."),
    reinforce="Revisa una conversación breve que inventes y marca lo que hizo bien y lo que falló el ejecutivo.",
    extend="Explica con un ejemplo inventado cómo una buena derivación puede mejorar la opinión de un cliente.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 18 (datos de ejemplo, inventados) del área de atención de «Muebles Roble Ltda.» en una semana. Solicitudes recibidas: 80 (teléfono 32, correo 28, presencial 20). Plazo de respuesta de ejemplo según la política: 24 horas. "
     "Solicitudes respondidas dentro del plazo: 64. Reclamos: 10, de los cuales 7 se resolvieron esa semana. Cuatro solicitudes pendientes y su prioridad: A) cliente interno de bodega, despacho que sale hoy, urgente; "
     "B) comprador, cambio de color, no urgente; C) proveedor, consulta de pago, plazo vence mañana; D) comprador, reclamo por pieza rota, entrega comprometida hoy.")
build(
    O4, 4, F,
    use="Aprenderé a medir la atención con datos simples (porcentaje de respuestas en plazo, reclamos resueltos) y a priorizar solicitudes con un criterio claro.",
    prior=["Sé calcular porcentajes.", "Sé usar las técnicas de atención.", "Sé qué es un registro de atención."],
    explain=[
        "La calidad de la atención se mide con datos simples. El porcentaje de respuestas dentro del plazo se calcula como respuestas dentro del plazo × 100 ÷ solicitudes recibidas. El porcentaje de reclamos resueltos se calcula como resueltos × 100 ÷ reclamos recibidos. Estos números ayudan a ver dónde mejorar, pero no reemplazan escuchar cada caso.",
        "Cuando llegan varias solicitudes a la vez, se priorizan con un criterio claro. Un criterio útil combina la urgencia (cuándo vence el plazo o si algo depende de la respuesta) y el impacto (a cuántas personas o procesos afecta). Se atiende primero lo urgente que afecta a más personas o detiene un proceso, y se informa un plazo a quienes deben esperar.",
        "La priorización nunca justifica tratar mal a quien espera. A cada persona se le dice cuándo será atendida. Los datos de la semana se presentan sin nombres de clientes; así se cuida su privacidad.",
    ],
    vocab=[("porcentaje en plazo", "respuestas dentro del plazo × 100 ÷ solicitudes"), ("urgencia", "qué tan pronto vence el plazo o se necesita la respuesta"), ("impacto", "a cuántas personas o procesos afecta"), ("prioridad", "orden en que se atiende"), ("plazo", "tiempo máximo para responder"), ("pendiente", "solicitud sin responder")],
    worked=[
        ("Porcentaje en plazo", "En una semana de ejemplo se recibieron 50 solicitudes y 40 se respondieron en plazo. ¿Qué porcentaje es?", ["40 × 100 ÷ 50 = 80.", "El resultado se expresa en porcentaje."], "80 %"),
        ("Prioridad", "Dos solicitudes ficticias: una detiene la entrega de un camión hoy; otra puede esperar tres días. ¿Cuál se atiende primero?", ["La primera es urgente y detiene un proceso.", "La segunda puede esperar."], "La que detiene la entrega"),
    ],
    mistakes=[("Atender por orden de llegada sin mirar la urgencia.", "Una solicitud que detiene un proceso puede quedar atrás.", "Usa urgencia e impacto para ordenar."),
              ("Priorizar y no avisar a quienes esperan.", "Las personas no saben cuándo serán atendidas.", "Informa un plazo a cada una.")],
    T=[
        ("abc", "En Administración: ¿cómo se calcula el porcentaje de respuestas en plazo?", "Respuestas en plazo por 100 dividido por solicitudes recibidas", "Solicitudes recibidas menos reclamos", "Reclamos por 100 dividido por plazo", "El porcentaje compara las respuestas en plazo con las solicitudes recibidas."),
        ("=", "{F} ¿Cuántas solicitudes llegaron por los tres canales sumados (teléfono, correo y presencial)?", "32+28+20", "Se suman los tres canales.", " solicitudes"),
        ("=", "{F} ¿Qué porcentaje de las 80 solicitudes se respondió dentro del plazo?", "64*100//80", "Porcentaje = respondidas en plazo × 100 ÷ recibidas.", " %"),
        ("=", "{F} ¿Cuántas solicitudes se respondieron fuera del plazo?", "80-64", "Fuera de plazo = recibidas − en plazo.", " solicitudes"),
        ("=", "{F} ¿Qué porcentaje de los 10 reclamos se resolvió esa semana?", "7*100//10", "Porcentaje = resueltos × 100 ÷ reclamos.", " %"),
        ("=", "{F} ¿Cuántos reclamos quedaron sin resolver?", "10-7", "Sin resolver = reclamos − resueltos.", " reclamos"),
        ("abc", "{F} ¿Cuál de las solicitudes pendientes viene de un cliente interno y es urgente?", "La A, el despacho de bodega que sale hoy", "La B, el cambio de color", "La C, la consulta de pago del proveedor", "La A es urgente porque el despacho sale hoy y detiene un proceso."),
        ("abc", "{F} ¿Por qué se atiende la A antes que la B?", "Porque la A es urgente y detiene un despacho, y la B puede esperar", "Porque la A llegó primero a la lista", "Porque la B es de un comprador y no importa", "La urgencia y el impacto de la A superan a los de la B, que no tiene plazo cercano."),
        ("abc", "{F} ¿Cuál es la solicitud no urgente que puede esperar?", "La B, el cambio de color", "La C, que vence mañana", "La D, con entrega comprometida hoy", "La B no tiene plazo cercano ni detiene nada."),
        ("abc", "{F} ¿Qué se hace con la persona de la solicitud B mientras espera?", "Se le informa cuándo será atendida", "Se le ignora", "Se le dice que su pedido no existe", "A cada persona se le dice un plazo, aunque su caso no sea el más urgente."),
        ("abc", "{F} Un informe de la semana muestra los nombres y teléfonos de los 10 reclamantes. ¿Qué corresponde?", "Presentar solo datos agregados, sin nombres", "Publicar la lista en un lugar visible", "Enviarla a todos los clientes", "Los informes muestran números, no datos personales."),
        ("=", "{F} Si la meta de la empresa es 90 % de respuestas en plazo y se logró un 80 %, ¿cuántos puntos porcentuales faltan?", "90-80", "Diferencia entre la meta y el resultado.", " puntos"),
        ("abc", "{F} Con ese resultado, ¿qué propuesta es adecuada?", "Revisar las causas de las respuestas fuera de plazo y ajustar los turnos", "Cambiar la meta a 80 % sin consultar", "Ocultar el dato en el informe", "Un resultado bajo la meta se analiza y se propone una mejora; la meta la fija la jefatura."),
    ],
    ctx=("abc", "Llegan a la vez la solicitud C (plazo vence mañana) y B (no urgente). ¿Cómo las organiza una ejecutiva?", "Atiende C hoy y avisa a B el día en que será atendida", "Atiende B primero porque llegó antes", "Responde ambas sin leerlas", "Se prioriza lo que vence primero y se avisa a quien espera."),
    sc=[
        ("En Administración: ¿qué dos criterios se combinan para priorizar?", "Urgencia e impacto", "Ambos ayudan a decidir el orden."),
        ("¿Qué porcentaje mide la rapidez de la atención?", "Respuestas en plazo", "Se calcula sobre las solicitudes recibidas."),
        ("¿Qué se hace con los nombres al presentar datos?", "Se dejan fuera del informe", "Así se resguarda la privacidad de los clientes atendidos."),
    ],
    op=("Con la Ficha 18, escribe un resumen de la semana para la jefatura: porcentaje de respuestas en plazo, reclamos resueltos, el orden en que atenderías las solicitudes A, B, C y D con una razón para cada una, y una propuesta de mejora.\n{F}",
        "En plazo: 80 % (64 de 80). Reclamos resueltos: 70 % (7 de 10). Orden: A (despacho que sale hoy), D (entrega comprometida hoy), C (vence mañana), B (puede esperar). Propuesta: revisar las causas de las 16 respuestas fuera de plazo y ajustar turnos. Datos sin nombres de clientes.",
        ["calcula los porcentajes", "ordena con urgencia e impacto", "da razón por solicitud", "propone mejora y cuida la privacidad"],
        ["resumen de siete líneas"],
        ["ordenar por llegada", "incluir nombres", "no dar razones"],
        "Comprueba los porcentajes. Si el orden no tiene razones, pide que las agregue."),
    reinforce="Ordena en papel cinco solicitudes ficticias por urgencia e impacto y justifica cada lugar.",
    extend="Explica con un ejemplo inventado un caso en que dos solicitudes urgentes obligan a pedir ayuda a la jefatura.",
)

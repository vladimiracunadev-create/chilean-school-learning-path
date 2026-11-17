"""Telecomunicaciones TP 3.º y 4.º medio: OAE-06 (mantenimiento y reparaciones menores: pautas y registros), OAE-07 (normativa, seguridad y medio ambiente: solo conceptos) y OAE-08 (red inalámbrica: planificación en papel)."""
from __future__ import annotations

from tp_tele_common import AVISO, build

O6 = "TP-TELE-3y4-OAE-06"
O7 = "TP-TELE-3y4-OAE-07"
O8 = "TP-TELE-3y4-OAE-08"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (pauta de mantenimiento de ejemplo, inventada). Equipo de ejemplo «Switch SX» de la empresa ficticia «Servicios Andes». Pauta del fabricante (de ejemplo): cada 3 meses, revisar los registros de eventos y el estado de los indicadores; "
     "cada 6 meses, hacer un respaldo de la configuración; cada 12 meses, revisión de ventilación y limpieza interna por el servicio técnico autorizado. Reglas de la pauta: no abrir el equipo durante la garantía; "
     "cualquier trabajo con el equipo energizado lo hace personal autorizado.")
build(
    O6, 1, F,
    use="Aprenderé los tipos de mantenimiento, por qué se siguen las pautas del fabricante y qué reparaciones menores pueden hacerse y cuáles no.",
    prior=["Sé qué es un registro y una bitácora.", "Sé qué es un riesgo eléctrico.", "Sé contar meses y años."],
    explain=[
        "El mantenimiento es el conjunto de tareas que mantienen un equipo funcionando. El mantenimiento preventivo se hace antes de que ocurra una falla, según un calendario. El mantenimiento correctivo se hace después de una falla, para recuperar el servicio. Hacer preventivo cuesta menos que esperar a que todo falle. La pauta del fabricante es el documento que dice qué revisar, cada cuánto y quién puede hacerlo.",
        "Una reparación menor es un arreglo simple y de bajo riesgo que la pauta permite a quien opera el equipo, como cambiar un accesorio que se enchufa y se retira sin herramientas. Cualquier trabajo que implique abrir el equipo, usar energía eléctrica o subir a una altura no es menor: lo hace personal autorizado. Abrir un equipo en garantía puede hacer perder la garantía.",
        f"Todo mantenimiento se anota en la bitácora: fecha, equipo, tarea, quién y resultado. La herramienta correcta es la que indica el fabricante; no se improvisa con otra. {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "tarea que se hace antes de una falla, según calendario"), ("mantenimiento correctivo", "tarea que se hace después de una falla para recuperar el servicio"), ("pauta del fabricante", "documento que dice qué revisar, cada cuánto y quién lo hace"), ("reparación menor", "arreglo simple y de bajo riesgo que la pauta permite"), ("garantía", "compromiso del fabricante de reparar si el equipo falla en un plazo"), ("bitácora", "registro de las tareas realizadas")],
    worked=[
        ("Tipo de mantenimiento", "Un equipo de ejemplo falla y se repara para volver a usarlo. ¿Qué tipo de mantenimiento es?", ["Se hace después de la falla.", "Eso es mantenimiento correctivo."], "Correctivo"),
        ("Frecuencia", "Una tarea de ejemplo se hace cada 3 meses. ¿Cuántas veces se hace en 12 meses?", ["Se divide el tiempo por el intervalo.", "12 entre 3."], "4 veces"),
    ],
    mistakes=[("Abrir un equipo en garantía «para mirar adentro».", "Puede perderse la garantía y crear riesgos con energía.", "Sigue la pauta y llama al servicio técnico autorizado."),
              ("Usar una herramienta distinta de la que indica la pauta porque «sirve igual».", "Puede dañar el equipo o hacer una mala revisión.", "Usa lo que indica el fabricante.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es el mantenimiento preventivo?", "El que se hace antes de una falla, según calendario", "El que se hace solo después de una falla", "El que reemplaza todo el equipo", "El preventivo se anticipa a la falla."),
        ("abc", "En Telecomunicaciones: ¿qué es una reparación menor?", "Un arreglo simple y de bajo riesgo que la pauta permite", "Cualquier trabajo con energía eléctrica", "Un cambio completo de la red", "La reparación menor es simple y permitida por la pauta."),
        ("abc", "¿Qué dice la pauta del fabricante?", "Qué revisar, cada cuánto y quién puede hacerlo", "Cuánto cuesta el equipo", "Cuántos usuarios tiene la empresa", "La pauta es la guía del fabricante para mantener el equipo."),
        ("=", "{F} Si la revisión de registros se hace cada 3 meses, ¿cuántas veces al año se hace?", "12//3", "Se divide los 12 meses del año por el intervalo de 3.", " veces"),
        ("abc", "{F} ¿Quién hace la revisión de ventilación y limpieza interna, según la pauta?", "El servicio técnico autorizado", "Cualquier funcionario", "El cliente con una aspiradora", "La pauta reserva esa tarea al servicio técnico autorizado."),
        ("abc", "{F} ¿Cada cuánto tiempo se hace el respaldo de configuración?", "Cada 6 meses", "Cada 3 meses", "Cada 12 meses", "La pauta indica respaldo de la configuración cada 6 meses."),
        ("=", "{F} ¿Cuántos respaldos de configuración se hacen en 3 años?", "36//6", "En 3 años hay 36 meses; se divide por el intervalo de 6.", " respaldos"),
        ("abc", "{F} Un funcionario quiere abrir el switch para limpiarlo, aunque está en garantía. ¿Qué corresponde?", "No abrirlo y pedir el servicio técnico autorizado", "Abrirlo con un destornillador", "Usar un aspirador dentro del equipo", "La pauta prohíbe abrir el equipo en garantía."),
        ("abc", "{F} La revisión de registros muestra un error repetido. ¿Qué tipo de mantenimiento se inicia si el equipo falla después?", "Correctivo", "Preventivo", "Ninguno", "Si ya hay falla, se actúa con mantenimiento correctivo."),
        ("abc", "Un técnico en formación anota en la bitácora solo «se revisó». ¿Qué falta?", "Fecha, equipo, tarea, quién y resultado", "El precio del equipo", "El nombre del fabricante", "Una bitácora útil permite saber qué se hizo exactamente."),
        ("=", "Una empresa de ejemplo tiene 5 equipos y cada uno recibe 4 revisiones al año. ¿Cuántas revisiones se hacen al año?", "5*4", "Se multiplican los equipos por las revisiones de cada uno.", " revisiones"),
        ("abc", "Un técnico de ejemplo propone cambiar una pieza de un equipo energizado «rápido y sin apagarlo». ¿Qué corresponde?", "No hacerlo: es trabajo para personal autorizado", "Hacerlo con guantes de tela", "Pedirle a un amigo que lo haga", "Trabajar con energía no es una reparación menor."),
        ("abc", "{F} ¿Qué ventaja tiene seguir el calendario preventivo?", "Reduce las fallas inesperadas y su costo", "Aumenta las fallas", "Elimina la necesidad de bitácora", "El mantenimiento preventivo evita fallas costosas."),
    ],
    ctx=("abc", "Un cliente de ejemplo dice: «no hagan la revisión de 12 meses, el equipo anda bien». ¿Qué responde la empresa?", "Que la pauta del fabricante pide esa revisión aunque funcione y que conviene mantener el calendario", "Que la omiten para ahorrar", "Que cambian la pauta", "El preventivo se hace aunque no haya falla."),
    sc=[
        ("En Telecomunicaciones: ¿cuándo se hace el mantenimiento preventivo?", "Antes de que haya falla, según calendario", "El preventivo se anticipa al problema, antes de que haya falla."),
        ("¿Se puede abrir un equipo en garantía?", "No, se llama al servicio técnico autorizado", "Abrirlo puede hacer perder la garantía."),
        ("¿Qué se anota después de cada tarea?", "Fecha, equipo, tarea, quién y resultado", "Eso queda en la bitácora de mantenimiento."),
    ],
    op=("Una escuela de ejemplo recibe la pauta de un router: revisar los indicadores cada 2 meses; respaldar la configuración cada 6 meses; limpieza interna anual por servicio técnico autorizado. Escribe (a) cuántas revisiones de indicadores y respaldos se hacen en 12 meses, (b) cuál tarea no harías tú y por qué y (c) los cinco datos de una anotación de bitácora.",
        "(a) 6 revisiones de indicadores (12 entre 2) y 2 respaldos (12 entre 6). (b) La limpieza interna, porque implica abrir el equipo y la pauta la reserva al servicio técnico autorizado. (c) Fecha, equipo, tarea, quién y resultado.",
        ["calcula las repeticiones", "reconoce la tarea que no hace y por qué", "nombra los datos de la bitácora"],
        ["hoja con los cálculos y las respuestas"],
        ["abrir el equipo", "confundir los intervalos", "olvidar la bitácora"],
        "Pregunta: «¿cuántas veces cabe el intervalo en un año?». Si no responde, pídele que divida 12 por el intervalo."),
    reinforce="Escribe la pauta de mantenimiento de un equipo inventado con tres tareas y su frecuencia.",
    extend="Explica con un ejemplo inventado por qué el mantenimiento preventivo suele costar menos que esperar la falla.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Hoja de vida» del equipo EX-7 (ejemplo): instalado hace 18 meses; fallas registradas: 3; horas de funcionamiento desde la instalación: 12.000 horas. "
     "Documentos del mantenimiento: manual y pauta del fabricante, hoja de vida del equipo, bitácora, orden de mantenimiento y registro de repuestos. Roles: técnico, supervisor y servicio técnico del fabricante. "
     "Definiciones del taller de ejemplo: MTBF = horas de funcionamiento ÷ número de fallas.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario del mantenimiento (hoja de vida, repuesto, MTBF, disponibilidad), los documentos y los roles.",
    prior=["Sé la diferencia entre mantenimiento preventivo y correctivo.", "Sé dividir.", "Sé qué es una bitácora."],
    explain=[
        "La hoja de vida de un equipo reúne su historia: cuándo se instaló, qué mantenimientos y fallas tuvo y qué repuestos usó. La orden de mantenimiento autoriza una tarea concreta. El repuesto es una pieza de reemplazo; debe ser el que indica el fabricante o uno equivalente aprobado. El registro de repuestos dice cuántos hay en bodega.",
        "Para medir qué tan confiable es un equipo se usa el MTBF (tiempo medio entre fallas): horas de funcionamiento divididas por el número de fallas. Un MTBF alto indica un equipo más confiable. La disponibilidad dice qué parte del tiempo el equipo estuvo en servicio: horas en servicio divididas por horas totales. Se expresa como porcentaje.",
        f"Cada rol tiene límites. El técnico ejecuta lo que permite la pauta, el supervisor revisa y autoriza y el servicio técnico del fabricante hace lo que la pauta le reserva (por ejemplo, abrir el equipo). Nadie cambia una pieza por otra que no esté aprobada. {AVISO}",
    ],
    vocab=[("hoja de vida", "documento con la historia del equipo: instalación, mantenimientos y fallas"), ("orden de mantenimiento", "documento que autoriza una tarea de mantenimiento"), ("repuesto", "pieza de reemplazo aprobada por el fabricante"), ("MTBF", "horas de funcionamiento divididas por el número de fallas"), ("disponibilidad", "parte del tiempo que el equipo está en servicio")],
    worked=[
        ("Calcular el MTBF", "Un equipo de ejemplo funcionó 1.000 horas con 5 fallas. ¿Cuál es el MTBF?", ["Se dividen las horas por las fallas.", "1.000 entre 5."], "200 horas"),
        ("Disponibilidad", "Un equipo de ejemplo estuvo en servicio 90 horas de 100. ¿Qué porcentaje de disponibilidad tiene?", ["Se dividen las horas en servicio por las horas totales.", "90 de 100 es 90 %."], "90 %"),
    ],
    mistakes=[("Poner en un equipo una pieza «parecida» sin que el fabricante la apruebe.", "Puede fallar o dañar el equipo y perder la garantía.", "Usa solo repuestos aprobados."),
              ("Calcular el MTBF dividiendo las fallas por las horas.", "El MTBF son las horas divididas por las fallas.", "Escribe la fórmula antes de reemplazar los números.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la hoja de vida de un equipo?", "El documento con su historia de instalación, mantenimientos y fallas", "La lista de usuarios del equipo", "El manual de uso del cliente", "La hoja de vida reúne la historia técnica del equipo."),
        ("abc", "En Telecomunicaciones: ¿qué es el MTBF?", "Horas de funcionamiento divididas por el número de fallas", "El costo mensual del mantenimiento", "El número de repuestos en bodega", "El MTBF mide el tiempo medio entre fallas."),
        ("abc", "¿Qué documento autoriza una tarea concreta de mantenimiento?", "La orden de mantenimiento", "La hoja de vida", "El registro de repuestos", "La orden de mantenimiento autoriza la tarea."),
        ("=", "{F} ¿Cuál es el MTBF del equipo EX-7, en horas?", "12000//3", "Se dividen las horas de funcionamiento por las fallas.", " horas"),
        ("=", "{F} El equipo EX-7 lleva 18 meses instalado. ¿Cuántos meses faltan para que cumpla 2 años (24 meses)?", "24-18", "Se restan los meses transcurridos a los 24 meses de dos años.", " meses"),
        ("abc", "{F} ¿Qué documento registra los repuestos que hay en bodega?", "El registro de repuestos", "La bitácora de fallas", "La pauta del fabricante", "El registro de repuestos lleva la cantidad de piezas."),
        ("=", "Un equipo de ejemplo funcionó 4.000 horas con 2 fallas. ¿Cuál es su MTBF?", "4000//2", "Se dividen las horas por las fallas.", " horas"),
        ("abc", "Un equipo A tiene MTBF de 800 horas y un equipo B de 1.500 horas. ¿Cuál es más confiable?", "B, porque su MTBF es mayor", "A, porque su MTBF es menor", "Son iguales", "Un MTBF más alto significa más tiempo entre fallas."),
        ("abc", "{F} El técnico encuentra en bodega una pieza parecida pero no aprobada. ¿Qué corresponde?", "No usarla y pedir el repuesto aprobado", "Usarla porque se parece", "Limarla hasta que encaje", "Solo se usan repuestos aprobados por el fabricante."),
        ("=", "En 200 horas totales, un equipo de ejemplo estuvo en servicio 190 horas. ¿Cuál es su disponibilidad, en porcentaje?", "190*100//200", "Se divide las horas en servicio por las totales y se pasa a porcentaje.", " %"),
        ("abc", "{F} ¿Quién hace una tarea que la pauta reserva al servicio técnico del fabricante?", "El servicio técnico del fabricante", "El técnico de la empresa", "El cliente", "La pauta reserva ciertas tareas al servicio técnico del fabricante."),
        ("abc", "Una persona calcula el MTBF de un equipo de 600 horas y 3 fallas como 3 entre 600. ¿Cuál es su error?", "Dividió las fallas por las horas, al revés", "Sumó las fallas", "Olvidó la disponibilidad", "El MTBF son las horas divididas por las fallas, es decir, 200 horas."),
        ("abc", "El supervisor de ejemplo quiere firmar una orden de mantenimiento de una tarea que hizo él mismo. ¿Qué corresponde?", "Que la revise otra persona", "Que se firme igual", "Que no se anote", "Nadie aprueba su propio trabajo; lo revisa otra persona."),
    ],
    ctx=("abc", "Una empresa de ejemplo compara dos routers: el X con MTBF de 1.000 horas y el Y con 3.000 horas, al mismo precio. ¿Qué puede decir el técnico?", "Que el Y falla con menos frecuencia, según el MTBF", "Que el X es mejor porque su MTBF es menor", "Que el MTBF no sirve", "A mayor MTBF, mayor tiempo entre fallas."),
    sc=[
        ("En Telecomunicaciones: ¿cómo se calcula el MTBF?", "Horas de funcionamiento divididas por el número de fallas", "El MTBF mide el tiempo medio entre una falla y la siguiente."),
        ("¿Qué repuestos se usan?", "Los aprobados por el fabricante", "Una pieza parecida puede dañar el equipo."),
        ("¿Qué documento guarda la historia del equipo?", "La hoja de vida", "La hoja de vida reúne instalación, mantenimientos y fallas del equipo."),
    ],
    op=("Un equipo de ejemplo funcionó 6.000 horas, tuvo 4 fallas y estuvo en servicio 5.700 de esas horas. Calcula (a) su MTBF, (b) su disponibilidad en porcentaje, (c) qué documento guardaría el detalle de esas fallas y (d) qué repuestos usarías.",
        "(a) 6.000 entre 4 son 1.500 horas. (b) 5.700 de 6.000 es 95 %. (c) La hoja de vida y la bitácora del equipo. (d) Los repuestos aprobados por el fabricante.",
        ["calcula el MTBF", "calcula el porcentaje", "nombra el documento y el criterio de repuestos"],
        ["hoja con los cálculos y las respuestas"],
        ["dividir al revés", "olvidar pasar a porcentaje", "aceptar repuestos no aprobados"],
        "Pregunta: «¿qué divides por qué en el MTBF?». Si no responde, pídele que escriba la fórmula."),
    reinforce="Calcula el MTBF de un equipo de ejemplo que funcionó 2.400 horas con 3 fallas.",
    extend="Explica con un ejemplo inventado por qué un equipo con alta disponibilidad no siempre tiene un MTBF alto.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (planilla de mantenimiento de ejemplo, inventada). Hoy es el 1 de octubre del año de ejemplo. Equipos de la «Oficina Faro» (ficticia) y su última revisión preventiva: Router R1, última revisión hace 2 meses, intervalo 3 meses; "
     "Switch S1, última revisión hace 5 meses, intervalo 4 meses; Punto de acceso A1, última revisión hace 1 mes, intervalo 6 meses; Central C1, última revisión hace 7 meses, intervalo 6 meses. "
     "Un equipo está «atrasado» si los meses desde la última revisión superan el intervalo.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel una planilla de mantenimiento, detectar atrasos y decidir qué hacer con cada equipo.",
    prior=["Sé qué es el mantenimiento preventivo.", "Sé comparar números.", "Sé qué es una orden de mantenimiento."],
    explain=[
        "Una planilla de mantenimiento lista los equipos, la última revisión y el intervalo que pide la pauta. Para saber si un equipo está al día se comparan los meses transcurridos con el intervalo. Si los meses transcurridos son menores o iguales que el intervalo, el equipo está al día. Si son mayores, está atrasado.",
        "Cuando hay equipos atrasados se ordenan por prioridad: primero los que prestan servicios críticos (como la central telefónica) y los que más se atrasaron. Se genera una orden de mantenimiento para cada uno y se informa a la jefatura. La prioridad se explica por escrito, con los números del caso.",
        "El análisis también revisa cuántos meses faltan para la próxima revisión de los equipos al día, para programar con tiempo. La planilla se entrega a la jefatura con el resultado. Todo es de papel con datos inventados; el mantenimiento en terreno lo realiza personal autorizado. " + AVISO,
    ],
    vocab=[("al día", "equipo cuya última revisión está dentro del intervalo"), ("atrasado", "equipo cuya última revisión superó el intervalo"), ("prioridad", "orden en que se atienden los equipos según su importancia"), ("servicio crítico", "servicio sin el cual la organización no puede operar bien")],
    worked=[
        ("Equipo atrasado", "Un equipo de ejemplo se revisó hace 5 meses y su intervalo es 3 meses. ¿Está atrasado?", ["Se compara 5 con 3.", "5 es mayor que 3."], "Sí, está atrasado por 2 meses"),
        ("Meses para la próxima", "Otro equipo de ejemplo se revisó hace 1 mes y su intervalo es 4. ¿Cuántos meses faltan para su próxima revisión?", ["Se resta el tiempo transcurrido al intervalo.", "4 menos 1."], "3 meses"),
    ],
    mistakes=[("Considerar al día un equipo porque «anda bien», aunque haya superado el intervalo.", "La pauta se mide con el calendario, no solo con el aspecto del equipo.", "Compara los meses con el intervalo."),
              ("Atender primero el equipo más fácil en vez del más importante.", "Un servicio crítico sin mantenimiento puede detener la organización.", "Ordena por prioridad y por atraso.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿cuándo está atrasado un equipo?", "Cuando los meses desde su revisión superan el intervalo", "Cuando es muy antiguo", "Cuando lleva muchos años instalado", "El atraso se mide con el calendario de la pauta."),
        ("abc", "En Telecomunicaciones: ¿qué es un servicio crítico?", "Un servicio sin el cual la organización no puede operar bien", "Un servicio gratuito", "Un servicio que usa poca energía", "La prioridad se da a lo crítico."),
        ("abc", "Un equipo se revisó hace 3 meses y su intervalo es 3 meses. ¿Está atrasado?", "No, está justo al día", "Sí, por 3 meses", "Sí, por 1 mes", "Como 3 no supera a 3, el equipo está justo al día."),
        ("abc", "{F} ¿Está atrasado el router R1?", "No, porque 2 meses no superan los 3", "Sí, porque 2 es menor que 3", "Sí, porque es un router", "2 meses está dentro del intervalo de 3."),
        ("abc", "{F} ¿Cuáles equipos de la planilla están atrasados?", "El switch S1 y la central C1", "El router R1 y el punto de acceso A1", "Solo el router R1", "S1 lleva 5 meses con intervalo 4, y C1 lleva 7 con intervalo 6."),
        ("=", "{F} ¿Cuántos meses de atraso tiene la central C1?", "7-6", "Se resta el intervalo a los meses transcurridos.", " mes"),
        ("=", "{F} ¿Cuántos meses de atraso tiene el switch S1?", "5-4", "Se resta el intervalo a los meses transcurridos.", " mes"),
        ("=", "{F} ¿Cuántos meses faltan para la próxima revisión del punto de acceso A1?", "6-1", "Se resta el tiempo transcurrido al intervalo.", " meses"),
        ("abc", "{F} Si la central telefónica es el servicio más crítico, ¿qué equipo atrasado se atiende primero?", "La central C1, por ser crítica y estar atrasada", "El punto de acceso A1", "El router R1", "La prioridad combina criticidad y atraso."),
        ("abc", "{F} ¿Cuántos equipos de los cuatro están al día?", "2", "1", "3", "R1 y A1 están al día; S1 y C1 están atrasados."),
        ("abc", "{F} El técnico de ejemplo propone no registrar el atraso del switch «para no preocupar». ¿Qué corresponde?", "Registrarlo e informarlo a la jefatura", "Borrar el dato", "Cambiar el intervalo a 5 meses", "Un atraso se informa con transparencia."),
        ("=", "Una planilla de ejemplo lista 10 equipos y 3 están atrasados. ¿Cuántos equipos están al día?", "10-3", "Se restan los atrasados al total.", " equipos"),
        ("abc", "Un jefe de ejemplo dice: «el intervalo de la pauta es solo una sugerencia». ¿Qué responde el técnico?", "Que la pauta del fabricante define el calendario de mantenimiento", "Que es solo una sugerencia", "Que el calendario no importa", "La pauta es la referencia técnica para el mantenimiento."),
    ],
    ctx=("abc", "La jefatura de ejemplo pide saber qué equipos atender primero. Hay una central atrasada 1 mes y un punto de acceso atrasado 3 meses. ¿Qué recomienda el técnico?", "Atender primero la central por ser un servicio crítico y explicarlo por escrito", "Atender primero el punto de acceso por el mayor atraso, sin decir por qué", "No atender ninguno", "La criticidad pesa en la prioridad y se justifica."),
    sc=[
        ("En Telecomunicaciones: ¿cómo se sabe si un equipo está atrasado?", "Comparando los meses desde la última revisión con el intervalo", "Si los meses transcurridos superan el intervalo, está atrasado."),
        ("¿Qué equipo se atiende primero?", "El servicio crítico atrasado", "La prioridad se explica por escrito."),
        ("¿Quién ejecuta el mantenimiento en terreno?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
    ],
    op=("Planilla de ejemplo de un taller (hoy es mes 12): Router: última revisión mes 10, intervalo 3; Switch: mes 7, intervalo 4; Central: mes 5, intervalo 6; Cámara: mes 12, intervalo 6. Calcula los meses transcurridos de cada equipo, indica cuáles están atrasados y en qué orden los atenderías (considera la Central como servicio crítico), con una frase de justificación.",
        "Meses transcurridos: Router 2, Switch 5, Central 7, Cámara 0. Atrasados: Switch (5 mayor que 4, 1 mes) y Central (7 mayor que 6, 1 mes). Orden: primero la Central por ser crítica, luego el Switch. Los otros dos están al día.",
        ["calcula los meses transcurridos", "identifica los atrasados", "ordena con una justificación"],
        ["tabla con los cuatro equipos y la lista de prioridad"],
        ["confundir la fecha de revisión con los meses transcurridos", "no justificar el orden", "marcar equipos al día como atrasados"],
        "Pregunta: «¿cuántos meses pasaron desde la última revisión de cada equipo?». Si no sabe, pídele que reste el mes de revisión a 12."),
    reinforce="Arma una planilla de ejemplo con tres equipos, sus intervalos y las últimas revisiones, y marca cuál está atrasado.",
    extend="Explica con un ejemplo inventado por qué un equipo crítico merece prioridad aunque su atraso sea pequeño.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (decisión de ejemplo, inventada). Un router de la «Panadería Doña Luz» (ficticia) falla. Opciones en papel: (A) reparación menor permitida por la pauta, que cuesta $15.000 de ejemplo y toma 1 día; "
     "(B) servicio técnico autorizado, que cuesta $40.000 de ejemplo y toma 3 días, con garantía de 6 meses para la reparación; (C) comprar un router nuevo por $90.000 de ejemplo, disponible mañana. "
     "Información de ejemplo: el equipo está fuera de garantía; la pauta dice que la reparación menor es el cambio de un accesorio que se enchufa y retira sin abrir el equipo; pérdida por día sin servicio, $20.000 de ejemplo.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo para decidir entre reparar, derivar o reemplazar un equipo.",
    prior=["Sé qué es una reparación menor y una garantía.", "Sé sumar costos.", "Sé comparar alternativas con números."],
    explain=[
        "Decidir entre reparar, derivar al servicio técnico o reemplazar es un problema de criterio técnico. Se comparan las alternativas con tres datos: el costo directo (lo que cuesta la reparación o la compra), el tiempo sin servicio (días por el costo de la pérdida diaria) y el riesgo (si se puede dañar el equipo o a una persona). El costo total de cada opción es el costo directo más la pérdida por los días sin servicio.",
        "La pauta del fabricante manda antes que el costo: si una reparación no es menor según la pauta, no se hace por ahorrar. También se mira la garantía de la reparación: un trabajo con garantía protege si falla otra vez. La decisión la toma la jefatura; el técnico entrega el análisis con los números.",
        f"Una reparación menor es solo la que la pauta describe como tal. Cualquier trabajo con energía, apertura del equipo o altura queda en manos de personal autorizado. {AVISO}",
    ],
    vocab=[("costo directo", "lo que cuesta la reparación o la compra"), ("pérdida por día", "lo que la organización deja de ganar por un día sin servicio"), ("costo total", "costo directo más la pérdida por los días sin servicio"), ("derivar", "enviar una tarea a quien está autorizado a hacerla")],
    worked=[
        ("Costo total", "Una opción de ejemplo cuesta $30.000 y deja 2 días sin servicio, con pérdida de $10.000 por día. ¿Cuál es el costo total?", ["La pérdida son 2 por 10.000, es decir 20.000.", "Se suma el costo directo: 30.000 más 20.000."], "$50.000"),
        ("Qué prima", "Una tarea de ejemplo exige abrir el equipo, pero la pauta no lo permite al usuario. ¿Qué se hace aunque cueste más?", ["La pauta manda antes que el ahorro.", "Se deriva al servicio autorizado."], "Se deriva al servicio técnico autorizado"),
    ],
    mistakes=[("Elegir siempre la opción más barata sin sumar la pérdida por los días sin servicio.", "La opción barata y lenta puede salir más cara.", "Calcula el costo total de cada opción."),
              ("Hacer una reparación que la pauta no permite porque «ahorra dinero».", "Puede dañar el equipo y crear riesgos.", "Respeta la pauta y deriva.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es el costo total de una opción?", "El costo directo más la pérdida por los días sin servicio", "Solo el precio de las piezas", "El precio del equipo nuevo", "El costo total incluye la pérdida por el tiempo sin servicio."),
        ("abc", "En Telecomunicaciones: ¿qué es derivar una tarea?", "Enviarla a quien está autorizado a hacerla", "Cancelarla definitivamente", "Hacerla más rápido", "Derivar es pasar la tarea al servicio autorizado."),
        ("abc", "Si una tarea no es una reparación menor según la pauta, ¿qué se hace?", "Se deriva al servicio técnico autorizado", "Se hace igual con cuidado", "Se espera a que falle más", "La pauta manda sobre el ahorro."),
        ("=", "{F} ¿Cuál es el costo total de la opción A, en pesos?", "15000+1*20000", "Se suma el costo directo y la pérdida de 1 día.", ""),
        ("=", "{F} ¿Cuál es el costo total de la opción B, en pesos?", "40000+3*20000", "Se suma el costo directo y la pérdida de 3 días.", ""),
        ("=", "{F} ¿Cuál es el costo total de la opción C, en pesos? Se compra hoy y queda disponible mañana, es decir, 1 día sin servicio.", "90000+1*20000", "Se suma el costo directo y la pérdida de 1 día.", ""),
        ("abc", "{F} ¿Cuál opción tiene el menor costo total?", "La A", "La B", "La C", "A suma 35.000, B suma 100.000 y C suma 110.000."),
        ("abc", "{F} La opción A solo es válida si la falla es la del accesorio que se enchufa. ¿Qué pasa si el diagnóstico muestra que la falla es interna?", "Deja de ser una reparación menor y se deriva", "Se abre el equipo para reparar", "Se compra otro accesorio igual", "La reparación menor se limita a lo que la pauta describe."),
        ("abc", "{F} ¿Qué ventaja da la opción B?", "Una garantía de 6 meses para la reparación", "Es la más rápida", "Es la más barata", "La opción B incluye garantía de 6 meses."),
        ("=", "{F} Si la falla se repitiera en 2 meses con la opción A, que no tiene garantía, ¿cuánto se pagaría en total por dos reparaciones menores de $15.000?", "2*15000", "Se multiplica el costo directo por el número de reparaciones.", ""),
        ("abc", "{F} Una persona calcula el costo de C como $90.000 e ignora la pérdida por el día sin servicio. ¿Cuál es el error?", "No sumó la pérdida por los días sin servicio", "Olvidó la garantía de A", "Sumó el costo de B", "El costo total incluye la pérdida diaria."),
        ("abc", "El jefe de ejemplo pide abrir el equipo «para ver si se arregla solo». ¿Qué responde el técnico?", "Que abrirlo no es una reparación menor y debe hacerlo el servicio autorizado", "Que lo abre ahora mismo", "Que lo abre y luego informa", "Abrir equipos no es una reparación menor."),
        ("abc", "{F} Si el diagnóstico confirma que es la falla del accesorio, ¿qué opción recomienda el análisis?", "La A, por menor costo total y porque la pauta la permite", "La C, por ser nueva", "La B, por ser más lenta", "La A cumple la pauta y tiene el menor costo total."),
    ],
    ctx=("abc", "La dueña de la panadería de ejemplo pregunta por qué no comprar siempre equipos nuevos. ¿Qué responde el técnico?", "Que depende del costo total, de la pauta y del riesgo, y que la decisión la toma ella con los números", "Que nunca conviene", "Que sí conviene siempre", "La decisión se apoya en los números, no en un hábito."),
    sc=[
        ("En Telecomunicaciones: ¿cómo se calcula el costo total de una opción?", "Costo directo más pérdida por días sin servicio", "Incluye lo que se deja de ganar."),
        ("¿Qué manda antes que el ahorro?", "La pauta del fabricante", "La pauta evita daños al equipo y riesgos para las personas."),
        ("¿Quién decide entre las opciones?", "La jefatura, con el análisis del técnico", "El técnico entrega los números y la jefatura decide."),
    ],
    op=("Un switch de ejemplo de una librería falla. Opción A: reparación menor permitida por la pauta, $10.000 y 1 día; opción B: servicio autorizado, $30.000, 2 días y garantía de 6 meses; opción C: equipo nuevo, $70.000 y 1 día. La pérdida por día sin servicio es $15.000. Calcula el costo total de cada una, indica cuál tiene el menor costo total y qué más considerarías antes de decidir.",
        "A: 10.000 más 15.000 son $25.000. B: 30.000 más 30.000 son $60.000. C: 70.000 más 15.000 son $85.000. El menor costo total es A. Además consideraría que la reparación esté permitida por la pauta, el riesgo y la garantía.",
        ["calcula los tres costos totales", "indica el menor", "menciona pauta, riesgo y garantía"],
        ["tabla con las tres opciones y la conclusión"],
        ["olvidar la pérdida por día", "elegir solo por precio directo", "ignorar la pauta"],
        "Pregunta: «¿cuántos días sin servicio tiene cada opción?». Si no responde, pídele que los anote al lado de cada costo."),
    reinforce="Calcula el costo total de una reparación de $20.000 que deja 2 días sin servicio con pérdida de $5.000 por día.",
    extend="Explica con un ejemplo inventado cuándo una opción más cara sale más conveniente por su garantía.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 5 (visita a un sitio de ejemplo, inventada). Informe de un estudiante en práctica al visitar una sala de equipos y un techo con antenas de la «Cooperativa Radio Sur» (ficticia). Peligros anotados: (1) cables y tableros con energía eléctrica; (2) trabajo en el techo, a gran altura; "
     "(3) antenas que emiten ondas de radio; (4) pisos mojados cerca de equipos; (5) cajas apiladas en un pasillo. Documentos del sitio: reglamento interno de seguridad y plano de evacuación (de ejemplo).")
build(
    O7, 1, F,
    use="Aprenderé la diferencia entre peligro y riesgo, qué normas orientan la seguridad en telecomunicaciones y por qué hay tareas que solo hace personal autorizado.",
    prior=["Sé qué es un riesgo.", "Sé leer un plano simple.", "Sé qué es una norma."],
    explain=[
        "Un peligro es algo que puede causar daño (un cable con energía, una altura). El riesgo es la posibilidad de que ese daño ocurra, y depende de qué tan probable es y de cuán grave sería. Prevenir es reducir la probabilidad o la gravedad antes de que ocurra el daño. En Chile, la prevención de riesgos laborales y la seguridad de las instalaciones se rigen por la norma vigente; por ejemplo, la Superintendencia de Electricidad y Combustibles (SEC) fiscaliza las instalaciones eléctricas y Subtel regula las telecomunicaciones.",
        "En telecomunicaciones los peligros típicos son: la electricidad, el trabajo en altura (techos, torres), las ondas de radio de las antenas (cuyo efecto depende de la potencia y de la distancia), las herramientas, los pisos resbaladizos y el levantamiento de cargas. Cada peligro se reduce con medidas: capacitación, permisos de trabajo, elementos de protección personal y orden.",
        f"Hay tareas que solo hace personal autorizado: las que usan energía de red, las de altura y las que ocurren cerca de antenas. {AVISO} Si una persona ve un peligro, avisa a la jefatura; nunca lo ignora ni lo resuelve por su cuenta.",
    ],
    vocab=[("peligro", "algo que puede causar daño"), ("riesgo", "posibilidad de que un peligro cause daño, según su probabilidad y gravedad"), ("prevención", "medidas para reducir la probabilidad o la gravedad de un daño"), ("elemento de protección personal", "equipo que protege a una persona de un peligro"), ("permiso de trabajo", "autorización escrita para una tarea de riesgo"), ("evacuación", "salida ordenada de las personas en una emergencia")],
    worked=[
        ("Peligro o riesgo", "Un techo de ejemplo está a gran altura y una persona va a subir sin protección. ¿Qué es la altura y qué es la posibilidad de caer?", ["La altura es lo que puede causar daño.", "La posibilidad de caer es el riesgo."], "La altura es el peligro y la posibilidad de caer es el riesgo"),
        ("Cuántos peligros", "Un informe de ejemplo anota 3 peligros eléctricos y 2 de altura. ¿Cuántos peligros hay?", ["Se suman los peligros de ambos tipos.", "3 más 2."], "5 peligros"),
    ],
    mistakes=[("Pensar que el peligro y el riesgo son lo mismo.", "El peligro es la fuente de daño; el riesgo, su posibilidad.", "Nombra primero el peligro y luego pregunta qué tan probable y grave es el daño."),
              ("Ignorar un peligro porque «nunca ha pasado nada».", "Que no haya ocurrido no quiere decir que no pueda ocurrir.", "Avisa a la jefatura de cada peligro que ves.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un peligro?", "Algo que puede causar daño", "La posibilidad de que ocurra el daño", "El permiso para trabajar", "El peligro es la fuente de daño; el riesgo es la posibilidad."),
        ("abc", "En Telecomunicaciones: ¿qué es el riesgo?", "La posibilidad de que un peligro cause daño", "El equipo de protección", "El nombre de una norma", "El riesgo depende de la probabilidad y de la gravedad."),
        ("abc", "¿Qué institución fiscaliza las instalaciones eléctricas en Chile?", "La Superintendencia de Electricidad y Combustibles (SEC)", "El Servicio de Impuestos Internos", "La Dirección del Trabajo", "La SEC fiscaliza las instalaciones eléctricas."),
        ("=", "{F} ¿Cuántos peligros anotó el informe del estudiante?", "1+1+1+1+1", "Se cuenta cada peligro numerado del informe.", " peligros"),
        ("abc", "{F} ¿Qué peligro de la ficha está relacionado con las antenas?", "Las ondas de radio que emiten", "Los pisos mojados", "Las cajas apiladas", "La ficha ubica las ondas de radio en las antenas."),
        ("abc", "{F} ¿Qué peligros de la ficha exigen personal autorizado?", "La energía eléctrica y el trabajo en altura", "Los pisos mojados y las cajas apiladas", "El plano de evacuación", "La electricidad y la altura exigen personal autorizado."),
        ("abc", "{F} Un estudiante en práctica quiere subir al techo porque «es solo mirar». ¿Qué corresponde?", "No subir sin autorización: el trabajo en altura lo hace personal autorizado", "Subir con calzado cómodo", "Subir si hay buen clima", "La altura es un peligro que exige personal autorizado."),
        ("=", "{F} En el pasillo hay 12 cajas apiladas en 3 columnas iguales. ¿Cuántas cajas hay en cada columna?", "12//3", "Se dividen las cajas por las columnas.", " cajas"),
        ("abc", "{F} ¿Qué documento de la ficha dice cómo salir ordenadamente en una emergencia?", "El plano de evacuación", "El reglamento de visitas", "El informe del estudiante", "El plano de evacuación señala las vías de salida."),
        ("abc", "{F} Un colega ve un cable con la cubierta rota y lo comenta con un amigo en vez de avisar a la jefatura. ¿Qué corresponde?", "Avisar de inmediato a la jefatura y no tocarlo", "Taparlo con cinta él mismo", "Esperar a que alguien lo note", "Los peligros se avisan; no se resuelven por cuenta propia."),
        ("abc", "¿De qué depende el efecto de las ondas de una antena en una persona?", "De la potencia y de la distancia", "Del color de la antena", "Del nombre del dueño", "Cuanta más potencia y cercanía, mayor puede ser la exposición."),
        ("abc", "La jefatura dice «esta tarea es rápida, no necesitamos permiso». ¿Qué responde un trabajador responsable?", "Que una tarea de riesgo requiere permiso de trabajo", "Que la hace sin permiso", "Que la hace de noche", "Las tareas de riesgo requieren permiso de trabajo."),
        ("=", "Una sala tiene 4 salidas de emergencia y 2 están bloqueadas con cajas. ¿Cuántas salidas están libres?", "4-2", "Se restan las salidas bloqueadas a las totales.", " salidas"),
    ],
    ctx=("abc", "Un técnico novato de ejemplo ve que un compañero repara un equipo sin apagarlo y sin permiso. ¿Qué corresponde?", "Avisar a la jefatura del peligro y no imitar la práctica", "Imitarlo para ir más rápido", "Ignorarlo para no ser delator", "Las prácticas inseguras se avisan para evitar un daño."),
    sc=[
        ("En Telecomunicaciones: ¿qué diferencia hay entre peligro y riesgo?", "El peligro causa daño; el riesgo es la posibilidad del daño", "El peligro y el riesgo son conceptos distintos, aunque relacionados."),
        ("¿Quién hace las tareas con energía o altura?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
        ("¿Qué se hace al ver un peligro?", "Avisar a la jefatura", "No se ignora ni se resuelve por cuenta propia."),
    ],
    op=("Un taller de ejemplo tiene estos peligros: tablero con energía, una escalera alta, ruido de un generador y un cable cruzando un pasillo. Escribe (a) el riesgo de cada peligro en una frase, (b) cuáles dos exigen personal autorizado y (c) a quién avisarías del cable en el pasillo.",
        "(a) Tablero con energía: descarga eléctrica; escalera alta: caída; ruido: daño al oído; cable en el pasillo: tropiezo. (b) El tablero con energía y la escalera alta. (c) A la jefatura o al encargado de prevención.",
        ["relaciona cada peligro con su riesgo", "identifica los peligros que exigen personal autorizado", "indica a quién avisar"],
        ["hoja con la lista de peligros y riesgos"],
        ["confundir peligro con riesgo", "decir que él mismo haría la tarea", "no avisar"],
        "Pregunta: «¿qué daño puede producir cada peligro?». Si no responde, pídele que lo imagine paso a paso."),
    reinforce="Nombra tres peligros de una sala de equipos de ejemplo y el riesgo de cada uno.",
    extend="Explica con un ejemplo inventado por qué un peligro puede tener bajo riesgo si hay buenas medidas.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 6 (cartilla de seguridad de ejemplo, inventada). Colores de señales de seguridad usados en la «Planta Radio Sur» (ficticia): rojo = prohibición o equipo contra incendios; amarillo = advertencia de peligro; azul = obligación (por ejemplo, usar casco); verde = salida o primeros auxilios. "
     "Elementos de protección personal (EPP) de ejemplo: casco, lentes de seguridad, guantes, calzado de seguridad. Matriz de riesgo de ejemplo: riesgo = probabilidad × gravedad, cada una de 1 (baja) a 3 (alta). Roles: trabajador, supervisor y encargado de prevención de riesgos.")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario de la seguridad (EPP, señalética, matriz de riesgo, permiso de trabajo) y los roles que participan.",
    prior=["Sé la diferencia entre peligro y riesgo.", "Sé multiplicar números pequeños.", "Sé qué es un permiso de trabajo."],
    explain=[
        "Los elementos de protección personal (EPP) son equipos que protegen a la persona de un peligro cuando no se pudo eliminar: el casco protege la cabeza, los lentes los ojos, los guantes las manos y el calzado de seguridad los pies. El EPP no elimina el peligro; es la última barrera. Debe ser adecuado al riesgo, estar en buen estado y usarse siempre en la tarea que lo exige.",
        "La señalética usa colores y formas fijos para comunicar rápido: rojo para prohibir o indicar equipos contra incendios, amarillo para advertir, azul para obligar y verde para salidas y primeros auxilios. La matriz de riesgo califica cada riesgo como probabilidad por gravedad: de 1 a 3 cada una, con resultados de 1 (bajo) a 9 (muy alto). Con ella se decide qué riesgos atender primero.",
        "Los roles son: el trabajador cumple las reglas y avisa los peligros; el supervisor verifica las condiciones y autoriza el permiso de trabajo; el encargado de prevención de riesgos asesora y revisa las medidas. Nadie debe hacer una tarea de riesgo sin estos controles. Ningún cuaderno reemplaza la capacitación de un instructor autorizado. " + AVISO,
    ],
    vocab=[("EPP", "equipo que protege a una persona de un peligro, como casco o guantes"), ("señalética", "señales con colores y formas fijos que comunican seguridad"), ("matriz de riesgo", "tabla que califica el riesgo como probabilidad por gravedad"), ("probabilidad", "qué tan posible es que ocurra el daño"), ("gravedad", "qué tan serio sería el daño"), ("encargado de prevención de riesgos", "persona que asesora y revisa las medidas de seguridad")],
    worked=[
        ("Calcular el riesgo", "Un peligro de ejemplo tiene probabilidad 2 y gravedad 3. ¿Cuál es su riesgo en la matriz?", ["El riesgo es probabilidad por gravedad.", "2 por 3."], "6"),
        ("Leer una señal", "Una señal de ejemplo es azul y muestra un casco. ¿Qué significa?", ["El azul indica obligación.", "El casco es el elemento a usar."], "Es obligatorio usar casco"),
    ],
    mistakes=[("Creer que el EPP elimina el peligro.", "El EPP solo reduce el daño cuando el peligro sigue presente.", "Usa EPP además de las otras medidas, no en vez de ellas."),
              ("Interpretar el color amarillo como «obligación».", "El amarillo advierte un peligro; el azul obliga.", "Aprende los cuatro colores de la cartilla.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿para qué sirve un EPP?", "Para proteger a la persona cuando no se eliminó el peligro", "Para que el peligro desaparezca", "Para reemplazar el permiso de trabajo", "El EPP es la última barrera de protección."),
        ("abc", "En Telecomunicaciones: ¿qué significa una señal amarilla?", "Advertencia de peligro", "Obligación de usar un elemento", "Salida de emergencia", "En la cartilla, el amarillo advierte de un peligro."),
        ("abc", "¿Cómo se calcula el riesgo en la matriz?", "Probabilidad por gravedad", "Probabilidad más gravedad", "Gravedad menos probabilidad", "La matriz multiplica probabilidad y gravedad."),
        ("abc", "{F} ¿Qué color de señal indica una salida de emergencia?", "Verde", "Rojo", "Azul", "Según la cartilla, el verde indica salidas y primeros auxilios."),
        ("abc", "{F} ¿Qué color de señal prohíbe una acción?", "Rojo", "Azul", "Amarillo", "El rojo indica prohibición o equipos contra incendios."),
        ("=", "{F} Un peligro tiene probabilidad 3 y gravedad 3. ¿Cuál es su riesgo?", "3*3", "Se multiplica probabilidad por gravedad.", ""),
        ("=", "{F} Otro peligro tiene probabilidad 1 y gravedad 3. ¿Cuál es su riesgo?", "1*3", "Se multiplica probabilidad por gravedad.", ""),
        ("abc", "{F} ¿Qué peligro se atiende primero: uno de riesgo 9 o uno de riesgo 3?", "El de riesgo 9", "El de riesgo 3", "Ambos igual", "A mayor valor de riesgo, mayor prioridad de atención."),
        ("abc", "{F} ¿Qué EPP protege los ojos?", "Los lentes de seguridad", "El casco", "Los guantes", "Los lentes de seguridad protegen los ojos de golpes y partículas."),
        ("abc", "{F} Una señal azul con casco está en la entrada de una sala. ¿Qué debe hacer quien entra?", "Usar casco", "Evitar entrar", "Salir por otra puerta", "El azul obliga al uso del elemento indicado."),
        ("=", "{F} En una cuadrilla de ejemplo de 8 personas, 5 tienen casco y lentes. ¿Cuántas personas faltan por equipar con ambos?", "8-5", "Se restan los equipados al total.", " personas"),
        ("abc", "{F} ¿Qué rol autoriza el permiso de trabajo?", "El supervisor", "El trabajador de otra empresa", "El visitante", "El supervisor verifica las condiciones y autoriza el permiso."),
        ("abc", "Un trabajador de ejemplo tiene el casco roto, pero dice «solo es una raja». ¿Qué corresponde?", "Cambiarlo, porque un EPP dañado no protege", "Seguir usándolo", "Taparlo con cinta", "El EPP debe estar en buen estado."),
    ],
    ctx=("abc", "En una planta de ejemplo, una señal roja dice «prohibido el paso» frente a una zona con antenas. Un técnico de otra empresa quiere pasar a tomar una foto. ¿Qué corresponde?", "Respetar la señal y pedir autorización al supervisor", "Pasar rápido", "Cubrir la señal", "La señal roja prohíbe; la autorización es del supervisor."),
    sc=[
        ("En Telecomunicaciones: ¿qué significa una señal azul?", "Obligación", "El azul indica algo que se debe usar o hacer."),
        ("¿Cómo se obtiene el riesgo en la matriz?", "Multiplicando probabilidad por gravedad", "Se califica de 1 a 9."),
        ("¿Qué rol autoriza el permiso de trabajo?", "El supervisor", "Verifica que las condiciones sean seguras."),
    ],
    op=("Un taller de ejemplo evalúa tres peligros: A, tablero con energía (probabilidad 2, gravedad 3); B, escalera alta con baranda (probabilidad 2, gravedad 2); C, cable en el pasillo (probabilidad 3, gravedad 1). Calcula el riesgo de cada uno, ordénalos de mayor a menor, nombra un EPP para uno de ellos y qué rol autoriza el trabajo con el tablero.",
        "A: 2 por 3 son 6; B: 2 por 2 son 4; C: 3 por 1 son 3. Orden: A, B, C. EPP: casco para la escalera alta. El tablero con energía no se resuelve con EPP: el trabajo lo autoriza el supervisor y lo hace personal autorizado.",
        ["calcula los tres riesgos", "los ordena de mayor a menor", "nombra un EPP y el rol que autoriza"],
        ["tabla con los tres riesgos y el orden"],
        ["sumar en vez de multiplicar", "ordenar al revés", "dejar el trabajo con energía a cualquier persona"],
        "Pregunta: «¿cuál riesgo atiendes primero?». Si no responde, pídele que mire el valor más alto."),
    reinforce="Calcula el riesgo de un peligro con probabilidad 2 y gravedad 2, y di si es mayor o menor que 5.",
    extend="Explica con un ejemplo inventado por qué el EPP debe ser la última barrera y no la única.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 7 (caso de ejemplo, inventado). La empresa ficticia «Torres y Redes Ltda.» revisa una orden: reemplazar el equipo de una antena de un edificio. Condiciones anotadas: (a) el equipo está en un techo con borde sin baranda; (b) hay un tablero con energía a 2 metros del equipo; "
     "(c) el trabajador asignado tiene el casco del tamaño equivocado y sin lentes de seguridad; (d) no hay permiso de trabajo firmado; (e) el supervisor no está presente; (f) el equipo antiguo incluye una batería que hay que desechar. "
     "Matriz de ejemplo: riesgo = probabilidad × gravedad, de 1 a 3 cada una.")
build(
    O7, 3, F,
    use="Aprenderé a analizar en papel un caso de trabajo, detectar las condiciones inseguras y decidir que la tarea no se hace hasta cumplir las condiciones.",
    prior=["Sé qué son EPP, señalética, matriz de riesgo y permiso de trabajo.", "Sé calcular el riesgo.", "Sé qué hace cada rol."],
    explain=[
        "Analizar un caso de seguridad es comparar las condiciones del trabajo con lo que exigen la norma vigente y la empresa. Para cada condición se pregunta: ¿es un peligro?, ¿cuál es su riesgo?, ¿qué medida falta? Una orden de trabajo con condiciones inseguras no se ejecuta: se detiene hasta que se corrijan, y se informa al supervisor.",
        "Algunas faltas detienen la tarea sin discusión: no tener permiso de trabajo firmado, no contar con el supervisor, no tener el EPP adecuado o trabajar en altura sin las protecciones que exige la norma. Detener un trabajo inseguro no es una falta, es una obligación: es la decisión correcta aunque atrase la entrega. Nadie puede presionar a otra persona a trabajar sin las condiciones de seguridad.",
        f"Además hay una parte ambiental: los equipos y baterías viejos son residuos especiales que no se botan a la basura común; se entregan a un gestor autorizado según la norma vigente. {AVISO}",
    ],
    vocab=[("condición insegura", "situación del lugar o del trabajo que puede causar daño"), ("detener la tarea", "no comenzar o suspender un trabajo hasta corregir las condiciones"), ("gestor autorizado", "empresa autorizada para recibir y tratar ciertos residuos"), ("residuo especial", "desecho que no puede ir a la basura común, como una batería")],
    worked=[
        ("Detener la tarea", "Una orden de ejemplo exige trabajar en un techo sin permiso de trabajo firmado. ¿Se ejecuta?", ["Sin permiso no se trabaja.", "Se detiene y se informa al supervisor."], "No, se detiene hasta tener el permiso"),
        ("Dónde va una batería", "Una batería vieja de ejemplo se desecha. ¿A dónde debe ir?", ["No es basura común: es residuo especial.", "Se entrega a un gestor autorizado."], "A un gestor autorizado"),
    ],
    mistakes=[("Hacer el trabajo «rápido» sin permiso porque el cliente tiene apuro.", "El apuro no cambia el riesgo.", "Detén la tarea y explica que se necesita el permiso."),
              ("Botar una batería a la basura común.", "Contamina y puede ser peligrosa.", "Entrégala a un gestor autorizado.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es una condición insegura?", "Una situación que puede causar daño", "Una herramienta nueva", "Un permiso firmado", "Las condiciones inseguras se corrigen antes de trabajar."),
        ("abc", "En Telecomunicaciones: ¿qué es un gestor autorizado?", "Una empresa autorizada para recibir y tratar ciertos residuos", "Un supervisor de obra", "Un fabricante de equipos", "Los residuos especiales van a un gestor autorizado."),
        ("abc", "¿Qué se hace con una orden con condiciones inseguras?", "Se detiene hasta corregirlas y se informa al supervisor", "Se ejecuta rápido", "Se cancela para siempre", "Detener el trabajo inseguro es una obligación."),
        ("=", "{F} ¿Cuántas condiciones de la orden son inseguras (de la a a la e, sin contar el residuo)?", "1+1+1+1+1", "Se cuentan las cinco condiciones inseguras de la orden.", " condiciones"),
        ("abc", "{F} ¿Qué falta en el EPP del trabajador asignado?", "Casco de talla correcta y lentes de seguridad", "Solo los guantes", "Nada", "La ficha anota casco incorrecto y sin lentes."),
        ("abc", "{F} ¿Qué falta para poder iniciar la tarea, aparte del EPP?", "Permiso de trabajo firmado y supervisor presente", "Un plano más grande", "Más herramientas", "Sin permiso ni supervisor la tarea no puede iniciar."),
        ("abc", "{F} ¿Qué debe hacer la persona asignada ante el borde sin baranda del techo?", "Detener la tarea y avisar al supervisor", "Trabajar con cuidado", "Asomarse para ver", "La falta de protección contra caídas detiene el trabajo."),
        ("=", "{F} Si el riesgo del tablero se califica con probabilidad 2 y gravedad 3, ¿cuál es su valor?", "2*3", "Se multiplica probabilidad por gravedad.", ""),
        ("abc", "{F} El cliente pide terminar hoy y ofrece pagar más si no esperan el permiso. ¿Qué corresponde?", "Negarse y explicar que sin permiso no se trabaja", "Aceptar el pago extra", "Trabajar solo en la mitad del techo", "El dinero no reemplaza las condiciones de seguridad."),
        ("abc", "{F} ¿Qué se hace con la batería del equipo antiguo?", "Se entrega a un gestor autorizado", "Se bota con la basura común", "Se deja en el techo", "Las baterías son residuos especiales y no van a la basura común."),
        ("=", "{F} De las 6 condiciones anotadas (a a la f), la (f) es ambiental y se separa. ¿Cuántas condiciones de seguridad quedan?", "6-1", "Se resta la ambiental al total.", " condiciones"),
        ("abc", "Un compañero presiona: «si no subes, te acusan de flojo». ¿Qué corresponde?", "No subir y avisar al supervisor", "Subir para evitar problemas", "Hacerlo en silencio", "Nadie debe trabajar sin las condiciones seguras."),
        ("abc", "{F} ¿Qué medida de la lista reduciría el riesgo del tablero sin cambiar la tarea?", "Que lo trate personal autorizado y se cumpla el permiso", "Taparlo con un paño", "Acercar más el equipo", "La medida correcta pasa por personal autorizado y permiso."),
    ],
    ctx=("abc", "Una estudiante en práctica de ejemplo recibe la orden de subir al techo con casco roto y sin permiso porque «es un favor». ¿Qué responde?", "Que no sube, que se necesita permiso y el EPP correcto y que avisa al supervisor", "Que sube un momento", "Que sube solo si nadie la ve", "La estudiante no hace tareas de riesgo sin las condiciones."),
    sc=[
        ("En Telecomunicaciones: ¿qué se hace con un trabajo inseguro?", "Se detiene hasta corregir las condiciones", "Es una obligación, no una falta."),
        ("¿A dónde van las baterías viejas?", "A un gestor autorizado", "Las baterías son residuos especiales y no van a la basura común."),
        ("¿Se puede trabajar sin permiso si hay apuro?", "No", "El apuro no cambia el riesgo."),
    ],
    op=("Orden de ejemplo: cambiar un equipo en un entretecho. Condiciones: sin permiso firmado; supervisor ausente; el trabajador tiene el casco pero no tiene guantes; el equipo antiguo incluye una batería; el tablero tiene energía. Escribe (a) cuáles condiciones detienen la tarea, (b) qué harías con la batería y (c) una frase al cliente que pide hacerlo hoy.",
        "(a) Detienen la tarea: no hay permiso, el supervisor está ausente, falta el EPP completo (guantes) y el tablero tiene energía y exige personal autorizado. (b) La batería se entrega a un gestor autorizado. (c) «No podemos comenzar sin permiso y condiciones seguras; reprogramamos para la fecha en que se cumplan.»",
        ["identifica las condiciones que detienen", "dice qué hacer con la batería", "redacta una frase firme y respetuosa"],
        ["hoja con las tres respuestas"],
        ["trabajar con apuro", "botar la batería", "no avisar al supervisor"],
        "Pregunta: «¿qué falta para empezar con seguridad?». Si no responde, pídele que recorra la lista de condiciones una por una."),
    reinforce="Escribe tres condiciones que detendrían un trabajo de ejemplo en un techo.",
    extend="Explica con un ejemplo inventado por qué detener un trabajo inseguro protege también a la empresa.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 8 (plan de medidas de ejemplo, inventado). Peligros de una sala de equipos de ejemplo y medidas propuestas: "
     "(1) tablero con energía → solo personal autorizado, etiqueta de advertencia; (2) escalera alta → permiso de trabajo y supervisor; (3) piso mojado → limpiar y poner señal amarilla; "
     "(4) cables sueltos en el piso → ordenar con canaleta; (5) ruido fuerte → protección auditiva. Jerarquía de controles (de más a menos efectiva): eliminar el peligro; sustituirlo; controles de ingeniería (barreras, canaletas); controles administrativos (permisos, señales, capacitación); EPP. "
     "Residuos de la sala (de ejemplo): 6 baterías, 20 metros de cable viejo, 3 equipos fuera de uso.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: clasificar medidas por la jerarquía de controles y planificar el manejo de residuos.",
    prior=["Sé qué es un EPP y un permiso de trabajo.", "Sé calcular el riesgo.", "Sé qué es un gestor autorizado."],
    explain=[
        "La jerarquía de controles ordena las medidas de más a menos efectiva. Primero eliminar el peligro (retirar lo que causa el daño). Luego sustituir (cambiar por algo menos peligroso). Después los controles de ingeniería, que son barreras físicas como canaletas o protecciones. Más abajo, los controles administrativos: permisos, señales y capacitación. Al final, el EPP. Se prefiere siempre la medida más alta que se pueda aplicar.",
        "Para decidir, se clasifica cada medida del plan en su nivel y se revisa si se pudo elegir una más efectiva. Por ejemplo, ordenar los cables con una canaleta es un control de ingeniería; poner una señal amarilla es administrativo. También se calcula cuánto baja el riesgo: si una medida cambia la probabilidad de 3 a 1, el riesgo baja a la tercera parte.",
        f"La normativa del medio ambiente pide separar los residuos y entregar los especiales (baterías, equipos electrónicos) a un gestor autorizado, según la norma vigente de residuos y responsabilidad extendida del productor. Se lleva un registro de lo que se entrega. {AVISO}",
    ],
    vocab=[("jerarquía de controles", "orden de las medidas de la más efectiva a la menos efectiva"), ("control de ingeniería", "barrera física que reduce el peligro, como una canaleta"), ("control administrativo", "medida de organización, como un permiso, una señal o una capacitación"), ("eliminar", "retirar el peligro por completo"), ("sustituir", "cambiar por algo menos peligroso"), ("registro de residuos", "constancia de lo que se entregó al gestor")],
    worked=[
        ("Clasificar una medida", "Una medida de ejemplo es poner una baranda en un borde. ¿Qué nivel de la jerarquía es?", ["La baranda es una barrera física.", "Eso es un control de ingeniería."], "Control de ingeniería"),
        ("Cuánto baja el riesgo", "Un riesgo de ejemplo tiene probabilidad 3 y gravedad 3. Con una medida la probabilidad baja a 1. ¿Cuál es el nuevo riesgo?", ["El riesgo es probabilidad por gravedad.", "1 por 3."], "3"),
    ],
    mistakes=[("Pensar que dar un casco es mejor que retirar el peligro.", "El EPP es la última medida; eliminar el peligro es la primera.", "Revisa la jerarquía desde arriba."),
              ("No llevar registro de lo entregado al gestor de residuos.", "Sin registro no hay evidencia de que se cumplió la norma.", "Anota qué, cuánto y a quién se entregó.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué medida es la más efectiva de la jerarquía de controles?", "Eliminar el peligro", "Usar EPP", "Poner una señal", "Eliminar quita el peligro del todo."),
        ("abc", "En Telecomunicaciones: ¿qué es un control de ingeniería?", "Una barrera física que reduce el peligro", "Una capacitación", "Un casco", "Las barreras físicas son controles de ingeniería."),
        ("abc", "¿Qué tipo de medida es una capacitación?", "Control administrativo", "Control de ingeniería", "Eliminación del peligro", "La capacitación y los permisos son medidas de organización."),
        ("abc", "{F} ¿En qué nivel está la medida (4) de ordenar los cables con una canaleta?", "Control de ingeniería", "EPP", "Control administrativo", "La canaleta es una barrera física."),
        ("abc", "{F} ¿En qué nivel está la medida (5) de protección auditiva?", "EPP", "Eliminación", "Sustitución", "La protección auditiva es un equipo de protección personal."),
        ("abc", "{F} ¿En qué nivel está la medida (3) de poner una señal amarilla en el piso mojado?", "Control administrativo", "Control de ingeniería", "EPP", "Una señal informa; no es una barrera física."),
        ("abc", "{F} ¿Cuántas de las 5 medidas del plan son controles administrativos?", "3", "2", "5", "Son administrativas las medidas 1, 2 y 3; la 4 es de ingeniería y la 5 es EPP."),
        ("abc", "{F} Para el piso mojado, ¿cuál sería una medida aún más efectiva que la señal?", "Eliminar la causa de la humedad", "Dar zapatos", "Poner otra señal", "Eliminar el peligro es lo más efectivo."),
        ("=", "{F} ¿Cuántos residuos sólidos de la lista (baterías y equipos) deben ir a un gestor autorizado?", "6+3", "Las baterías y los equipos fuera de uso son residuos especiales.", " residuos"),
        ("abc", "{F} Los 20 metros de cable viejo, ¿qué hacer con ellos?", "Entregarlos para su reciclaje a un gestor autorizado, sin botarlos", "Dejarlos en la sala", "Regalarlos a un conocido sin registro", "Los cables y equipos electrónicos van a gestor autorizado."),
        ("=", "{F} Un riesgo de ejemplo tiene probabilidad 3 y gravedad 3 y baja a probabilidad 1 con la canaleta. ¿Cuánto baja el riesgo?", "3*3-1*3", "Se resta el riesgo nuevo al riesgo anterior.", ""),
        ("abc", "{F} Un colega propone dejar el tablero sin etiqueta «porque todos saben». ¿Qué corresponde?", "Mantener la etiqueta de advertencia como medida del plan", "Quitarla", "Taparla con pintura", "La etiqueta es una medida informativa del plan."),
        ("abc", "Un supervisor de ejemplo entrega solo cascos a la cuadrilla y dice «con eso estamos cubiertos». ¿Qué le responderías?", "Que primero hay que revisar si se pueden eliminar o controlar los peligros", "Que está perfecto", "Que no se necesita nada más", "El EPP no reemplaza las otras medidas."),
    ],
    ctx=("abc", "La encargada de una sala de ejemplo pide guardar las 6 baterías viejas en una bodega «hasta que haya espacio». ¿Qué recomienda el técnico?", "Almacenarlas con seguridad un tiempo breve y entregarlas pronto a un gestor autorizado con registro", "Botarlas en el contenedor común", "Dejarlas sin ningún control", "Las baterías son residuos especiales con registro y entrega al gestor."),
    sc=[
        ("En Telecomunicaciones: ¿qué es la jerarquía de controles?", "El orden de las medidas de la más a la menos efectiva", "Se prefiere siempre la más alta."),
        ("¿Dónde queda el EPP en la jerarquía?", "Al final, como última barrera", "El EPP no reemplaza otras medidas más efectivas."),
        ("¿Qué se hace con las baterías viejas?", "Se entregan a un gestor autorizado con registro", "Las baterías son residuos especiales y no van a la basura común."),
    ],
    op=("Un taller de ejemplo tiene estos peligros: (1) cables sueltos; (2) ruido fuerte; (3) borde sin baranda. Medidas propuestas: ordenar con canaleta; protección auditiva; poner una señal de advertencia. Clasifica cada medida en su nivel de la jerarquía (ingeniería, administrativo o EPP), di si propondrías algo más efectivo para el borde y cómo entregarías 4 baterías viejas.",
        "Canaleta: control de ingeniería. Protección auditiva: EPP. Señal de advertencia: control administrativo. Para el borde, algo más efectivo sería una baranda (ingeniería) hecha por personal autorizado. Las 4 baterías se entregan a un gestor autorizado y se anota en el registro de residuos.",
        ["clasifica las tres medidas", "propone una medida más efectiva", "dice cómo entregar las baterías"],
        ["tabla con las tres medidas y su nivel"],
        ["poner el EPP primero", "olvidar el registro de residuos", "decir que las baterías van a la basura común"],
        "Pregunta: «¿qué medida elimina el peligro en vez de solo avisarlo?». Si no responde, pídele que piense en el borde."),
    reinforce="Clasifica tres medidas de ejemplo (un permiso, una baranda y unos guantes) en la jerarquía de controles.",
    extend="Explica con un ejemplo inventado por qué una señal sola no basta frente a un peligro grave.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 9 (oficina de ejemplo, inventada). El «Colegio Los Cipreses» (ficticio) quiere cobertura inalámbrica en un edificio de 2 pisos con 6 salas y un patio techado. Pregunta del director: «¿podemos poner puntos de acceso en el techo exterior para que llegue al patio?». "
     "Datos de ejemplo: red del colegio con alumnos menores de edad; cada sala tiene 30 estudiantes con dispositivos; se usarán 3 puntos de acceso de ejemplo. Aviso del proyecto: el uso del aire (espectro) está regulado por la autoridad.")
build(
    O8, 1, F,
    use="Aprenderé qué es una red inalámbrica, qué normas y riesgos hay que considerar, y por qué las instalaciones en altura exigen personal autorizado.",
    prior=["Sé qué es una red LAN.", "Sé qué es un dato personal.", "Sé qué es un riesgo."],
    explain=[
        "Una red inalámbrica conecta dispositivos sin cables, usando ondas de radio. El equipo que da la conexión se llama punto de acceso. El nombre de la red que ven los dispositivos es el SSID. Las ondas que usa viajan por el aire, que es un recurso compartido y regulado: la autoridad (Subtel, según la norma vigente) fija qué frecuencias y potencias se pueden usar. Por eso no se usan equipos ni potencias fuera de lo permitido.",
        "El aire compartido trae riesgos de privacidad y seguridad. Una red sin clave de acceso o con una clave débil permite que cualquiera la use o vea el tráfico. Por eso se usa cifrado (WPA2 o WPA3) y una contraseña robusta; en estos ejercicios nunca se usan contraseñas reales. En una red con menores de edad se cuidan además los datos personales y los contenidos.",
        f"Instalar puntos de acceso en techos, torres o altura es trabajo para personal autorizado. {AVISO} Aquí solo se planifica en papel.",
    ],
    vocab=[("red inalámbrica", "red que conecta dispositivos con ondas de radio"), ("punto de acceso", "equipo que da la conexión inalámbrica"), ("SSID", "nombre de la red inalámbrica"), ("cifrado", "forma de codificar los datos para que otros no los lean"), ("WPA2 y WPA3", "formas de cifrado para redes inalámbricas"), ("espectro", "conjunto de frecuencias de radio, que es regulado")],
    worked=[
        ("Qué es el SSID", "Un dispositivo de ejemplo muestra la lista «Cipreses» y «Taller». ¿Qué son esos nombres?", ["Son los nombres de las redes disponibles.", "Cada nombre se llama SSID."], "SSID"),
        ("Cuántos dispositivos", "Un punto de acceso de ejemplo atiende 20 dispositivos por sala y hay 5 salas. ¿Cuántos dispositivos son?", ["Se multiplican los dispositivos por las salas.", "20 por 5."], "100 dispositivos"),
    ],
    mistakes=[("Dejar la red inalámbrica sin clave «para que todos entren fácil».", "Cualquiera puede usarla o espiar el tráfico.", "Usa cifrado y una contraseña robusta."),
              ("Subir a un techo a poner un punto de acceso porque «es solo un aparato pequeño».", "El trabajo en altura exige personal autorizado, sin importar el tamaño del equipo.", "Planifica en papel y deja la instalación a quien está autorizado.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un punto de acceso?", "El equipo que da la conexión inalámbrica", "El cable que une dos salas", "La contraseña de la red", "El punto de acceso entrega la conexión inalámbrica."),
        ("abc", "En Telecomunicaciones: ¿qué es el SSID?", "El nombre de la red inalámbrica", "El cable de energía", "La potencia del equipo", "El SSID es el nombre que ven los dispositivos."),
        ("abc", "¿Qué institución regula en Chile el uso del espectro de radio?", "La Subsecretaría de Telecomunicaciones (Subtel)", "El Servicio de Impuestos Internos", "La Dirección del Trabajo", "Subtel regula las telecomunicaciones y el uso del espectro."),
        ("=", "{F} ¿Cuántos estudiantes hay en total en las 6 salas, con 30 por sala?", "6*30", "Se multiplican las salas por los estudiantes por sala.", " estudiantes"),
        ("=", "{F} Si los 3 puntos de acceso se reparten los estudiantes en partes iguales, ¿cuántos estudiantes atiende cada punto?", "6*30//3", "Se divide el total de estudiantes por los puntos de acceso.", " estudiantes"),
        ("abc", "{F} ¿Qué tipo de dato exige especial cuidado en la red del colegio?", "Los datos de los estudiantes menores de edad", "El nombre del edificio", "El color de los puntos de acceso", "Los datos de menores de edad se protegen según la norma vigente."),
        ("abc", "{F} El director pide instalar puntos de acceso en el techo exterior. ¿Qué corresponde responder?", "Que se planifica en papel y que el trabajo en altura lo hace personal autorizado", "Que lo hace un profesor con una escalera", "Que lo hacen los estudiantes", "El trabajo en altura es de personal autorizado."),
        ("abc", "Una red inalámbrica de ejemplo no tiene clave. ¿Qué riesgo tiene?", "Que cualquiera la use o vea el tráfico", "Que sea más lenta por tener clave", "Que gaste menos energía", "Sin cifrado ni clave, la red queda expuesta."),
        ("abc", "{F} ¿Se puede usar un equipo con una potencia mayor a la permitida para lograr más alcance?", "No, la potencia y la frecuencia están reguladas por la autoridad", "Sí, mientras no moleste", "Sí, si el colegio lo decide", "Las potencias permitidas las fija la autoridad."),
        ("=", "Un patio de ejemplo necesita 2 puntos de acceso y cada sala 1. Con 6 salas y 1 patio, ¿cuántos puntos hacen falta?", "6*1+2", "Se suman los puntos de las salas y los del patio.", " puntos"),
        ("abc", "Un profesor de ejemplo quiere usar la contraseña de la red del colegio en su celular personal y compartirla con los estudiantes. ¿Qué corresponde?", "Pedir autorización a quien administra la red", "Compartirla en el patio", "Publicarla en un cartel", "Las claves de la red se comparten con autorización."),
        ("abc", "{F} Un estudiante de ejemplo cree que, como la red es del colegio, nadie puede ver su navegación. ¿Qué es lo correcto?", "Una red mal protegida puede exponer datos, por eso se usa cifrado y buenas prácticas", "Nadie puede ver nada nunca", "Todos ven todo siempre", "Sin buenas prácticas, el tráfico puede quedar expuesto."),
        ("abc", "{F} El administrador del colegio de ejemplo sospecha de un acceso no autorizado a la red. ¿Qué corresponde?", "Informar a la dirección y al responsable de informática", "Ignorarlo", "Apagar la red sin avisar", "Los incidentes se informan a los responsables."),
    ],
    ctx=("abc", "Una apoderada de ejemplo pide la clave de la red del colegio para usarla desde su casa. ¿Qué responde el encargado?", "Que no puede compartirla y que la red es solo para uso del colegio", "Que se la da, porque es amable", "Que la publica en la puerta", "La clave de la red no se entrega sin autorización."),
    sc=[
        ("En Telecomunicaciones: ¿qué es el SSID?", "El nombre de la red inalámbrica", "Es lo que ven los dispositivos."),
        ("¿Quién regula el uso del espectro en Chile?", "Subtel, según la norma vigente", "El aire es un recurso regulado."),
        ("¿Quién instala equipos en altura?", "Personal autorizado", "El cuaderno no habilita para trabajar."),
    ],
    op=("Un consultorio de ejemplo planea una red inalámbrica para la sala de espera. Escribe (a) un nombre de ejemplo para el SSID que no revele datos personales, (b) dos medidas de seguridad para la red y (c) qué responderías si te piden instalar un punto de acceso en un techo alto.",
        "(a) SSID de ejemplo: «Consultorio_Espera». (b) Usar cifrado WPA2 o WPA3 y una contraseña robusta que no se comparta. (c) Que se planifica en papel y que el trabajo en altura lo hace personal autorizado con instructor y norma vigente.",
        ["elige un SSID sin datos personales", "nombra dos medidas de seguridad", "responde con el límite de la altura"],
        ["hoja con las tres respuestas"],
        ["poner datos personales en el SSID", "dejar la red abierta", "aceptar subir al techo"],
        "Pregunta: «¿qué dato personal no pondrías en el nombre de la red?». Si no responde, pídele que piense en nombres de personas."),
    reinforce="Escribe dos nombres de red de ejemplo adecuados para un negocio y uno que no usarías.",
    extend="Explica con un ejemplo inventado por qué una clave débil pone en riesgo a toda la red.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 10 (cartilla de ejemplo, inventada). Bandas de una red inalámbrica: 2,4 GHz (alcanza más lejos, atraviesa mejor las paredes, tiene menos velocidad y más interferencia) y 5 GHz (más velocidad, menos alcance, menos interferencia). "
     "Canales de ejemplo en 2,4 GHz: los canales 1, 6 y 11 no se superponen entre sí. Cifrado: abierta (sin clave, no recomendada), WPA2 y WPA3. "
     "Documentos: estudio de cobertura, plan de canales y ficha de configuración del punto de acceso. Roles: administrador de red, técnico de redes y usuario.")
build(
    O8, 2, F,
    use="Aprenderé el vocabulario de las redes inalámbricas (banda, canal, interferencia, cobertura, roaming) y los documentos y roles del trabajo.",
    prior=["Sé qué es un punto de acceso y un SSID.", "Sé qué son MHz y GHz.", "Sé qué es el cifrado."],
    explain=[
        "Un punto de acceso emite en una banda de frecuencias: 2,4 GHz o 5 GHz. La banda de 2,4 GHz llega más lejos y atraviesa mejor las paredes, pero es más lenta y hay más interferencia. La banda de 5 GHz es más rápida y tiene menos interferencia, pero alcanza menos. Dentro de cada banda hay canales: si dos puntos de acceso cercanos usan el mismo canal, se interfieren. En 2,4 GHz los canales 1, 6 y 11 no se superponen entre sí.",
        "La cobertura es la zona donde la señal llega con calidad suficiente; los muros, los metales y la distancia la reducen. Si una persona se mueve entre dos puntos de acceso, el roaming es el paso automático de uno a otro sin cortarse. La interferencia es la mezcla de señales que perjudica la calidad. El cifrado protege la red: WPA2 y WPA3 son los recomendados; una red abierta no se recomienda.",
        "Los documentos son: el estudio de cobertura (dónde llega la señal), el plan de canales (qué canal usa cada punto) y la ficha de configuración (SSID, cifrado, canal de cada equipo). El administrador de red configura, el técnico de redes ejecuta lo autorizado y el usuario cumple la política de uso. " + AVISO,
    ],
    vocab=[("banda", "grupo de frecuencias que usa la red, como 2,4 GHz o 5 GHz"), ("canal", "división de una banda en la que emite un punto de acceso"), ("interferencia", "mezcla de señales que perjudica la calidad"), ("cobertura", "zona donde la señal llega con calidad suficiente"), ("roaming", "paso automático de un punto de acceso a otro sin cortarse"), ("estudio de cobertura", "documento que muestra dónde llega la señal")],
    worked=[
        ("Elegir la banda", "Una bodega de ejemplo necesita que la señal llegue lejos y atraviese muros. ¿Qué banda conviene?", ["La banda que alcanza más lejos y atraviesa mejor es la de 2,4 GHz.", "Aunque sea más lenta."], "2,4 GHz"),
        ("Canales sin superposición", "Tres puntos de acceso de ejemplo cercanos usarán la banda de 2,4 GHz. ¿Qué canales conviene asignar?", ["Los canales 1, 6 y 11 no se superponen.", "Se asigna uno a cada punto."], "Los canales 1, 6 y 11"),
    ],
    mistakes=[("Poner dos puntos de acceso cercanos en el mismo canal para que «tengan lo mismo».", "Se interfieren y bajan la velocidad.", "Asigna canales distintos y sin superposición."),
              ("Creer que la banda de 5 GHz siempre es mejor.", "Alcanza menos y atraviesa peor los muros.", "Elige según la distancia y los obstáculos.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la interferencia?", "La mezcla de señales que perjudica la calidad", "La clave de la red", "El nombre del punto de acceso", "La interferencia mezcla señales y empeora la comunicación."),
        ("abc", "En Telecomunicaciones: ¿qué es el roaming?", "El paso automático de un punto de acceso a otro sin cortarse", "El cifrado de la red", "La potencia del punto de acceso", "El roaming permite moverse entre puntos de acceso."),
        ("abc", "¿Qué banda tiene más alcance y atraviesa mejor los muros?", "2,4 GHz", "5 GHz", "Ambas por igual", "La banda de 2,4 GHz alcanza más lejos."),
        ("abc", "{F} ¿Qué banda tiene más velocidad y menos interferencia?", "5 GHz", "2,4 GHz", "Ninguna", "Según la cartilla, la banda de 5 GHz es más rápida."),
        ("abc", "{F} Tres puntos de acceso cercanos usan la banda de 2,4 GHz. ¿Qué canales asignar?", "1, 6 y 11", "1, 2 y 3", "6, 7 y 8", "Los canales 1, 6 y 11 no se superponen entre sí."),
        ("abc", "{F} ¿Qué cifrado no se recomienda?", "Abierta, sin clave", "WPA2", "WPA3", "La red abierta no protege el tráfico."),
        ("=", "{F} Si en 2,4 GHz hay 3 canales sin superposición (1, 6 y 11) y se usan 2, ¿cuántos quedan libres?", "3-2", "Se restan los usados a los tres canales.", " canal"),
        ("abc", "{F} ¿Qué documento muestra dónde llega la señal con calidad suficiente?", "El estudio de cobertura", "El plan de canales", "La política de uso", "El estudio de cobertura muestra la zona con señal."),
        ("abc", "{F} Un salón de ejemplo está lejos del punto de acceso y tiene un muro grueso. ¿Qué banda conviene?", "2,4 GHz", "5 GHz", "Ninguna", "La banda de 2,4 GHz atraviesa mejor el muro."),
        ("abc", "Un auditorio de ejemplo está cerca del punto de acceso y necesita mucha velocidad con muchos usuarios. ¿Qué banda conviene?", "5 GHz", "2,4 GHz", "Cualquiera da lo mismo", "5 GHz ofrece más velocidad con menos interferencia."),
        ("=", "Un punto de acceso de ejemplo cubre un radio de 20 metros. ¿Cuántos metros de diámetro cubre?", "20*2", "El diámetro es el doble del radio.", " metros"),
        ("abc", "{F} Dos puntos de acceso vecinos quedaron en el canal 6. ¿Qué corresponde?", "Cambiar uno a un canal sin superposición, como el 1 o el 11", "Dejar ambos igual", "Apagar el router", "Se evita la interferencia con canales distintos."),
        ("abc", "{F} Una usuaria de ejemplo se mueve por el pasillo y su videollamada se corta al cambiar de punto de acceso. ¿Qué función debería mejorarse?", "El roaming", "El SSID", "El cifrado", "El roaming debe permitir un paso sin cortes."),
    ],
    ctx=("abc", "El administrador de ejemplo ve que su red de 2,4 GHz está lenta porque tres vecinos usan el mismo canal. ¿Qué propone?", "Cambiar de canal o usar la banda de 5 GHz donde sea posible", "Subir la potencia más allá de lo permitido", "Quitar la clave", "Cambiar de canal o de banda reduce la interferencia."),
    sc=[
        ("En Telecomunicaciones: ¿qué banda alcanza más lejos?", "2,4 GHz", "La banda de 2,4 GHz atraviesa mejor los muros."),
        ("¿Qué canales de 2,4 GHz no se superponen?", "1, 6 y 11", "Evitan la interferencia entre puntos de acceso."),
        ("¿Qué cifrado es recomendable?", "WPA2 o WPA3", "Una red abierta no protege los datos."),
    ],
    op=("Un hotel de ejemplo tiene tres puntos de acceso en el mismo piso: P1 en el pasillo central, P2 al fondo, P3 en la entrada. Asigna (a) un canal sin superposición a cada punto en 2,4 GHz, (b) una banda para una sala de reuniones cercana a P1 con muchos usuarios y (c) un cifrado, y explica en dos líneas por qué.",
        "(a) P1 canal 1, P2 canal 6, P3 canal 11. (b) 5 GHz, porque ofrece más velocidad y menos interferencia con la sala cerca del punto. (c) WPA2 o WPA3, porque protegen el tráfico.",
        ["asigna tres canales sin superposición", "elige banda con razón", "elige un cifrado recomendado"],
        ["hoja con los tres puntos, la banda y el cifrado"],
        ["repetir canal", "elegir red abierta", "no justificar la banda"],
        "Pregunta: «¿qué canales no se superponen en 2,4 GHz?». Si no responde, pídele que revise la cartilla."),
    reinforce="Escribe una ventaja y una desventaja de la banda de 5 GHz.",
    extend="Explica con un ejemplo inventado por qué dos puntos de acceso en el mismo canal se perjudican.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 11 (caso de ejemplo, inventado). La «Biblioteca Los Boldos» (ficticia) tiene tres puntos de acceso en la banda de 2,4 GHz. Configuración de papel: P1 canal 1, SSID «Biblioteca», cifrado WPA2; P2 canal 3, SSID «Biblioteca», cifrado WPA2; "
     "P3 canal 6, SSID «Biblioteca2», red abierta (sin clave). Contraseña anotada en la ficha: «1234» (de ejemplo, claramente débil). Queja: «la señal se corta en el fondo». Canales sin superposición en 2,4 GHz: 1, 6 y 11.")
build(
    O8, 3, F,
    use="Aprenderé a analizar en papel la configuración de una red inalámbrica, detectar interferencias y fallas de seguridad y proponer correcciones.",
    prior=["Sé las bandas y los canales sin superposición.", "Sé qué es el cifrado.", "Sé qué es un hallazgo."],
    explain=[
        "Revisar una red inalámbrica en papel es comparar la configuración de cada punto con las buenas prácticas. Se miran cuatro cosas: el canal (que no haya superposición con los vecinos), el nombre de la red (SSID), el cifrado (WPA2 o WPA3) y la contraseña (robusta, no del tipo 1234 ni con datos personales).",
        "Un canal que se superpone con otro cercano, como el 3 con el 1 o el 6, produce interferencia. Una red abierta permite que cualquiera la use y vea el tráfico. Una contraseña débil es adivinable. Varios puntos con el mismo SSID y el mismo cifrado permiten el roaming; un SSID distinto con otra configuración obliga a cambiar de red manualmente.",
        "El resultado es una lista de hallazgos con su corrección: qué está mal, por qué y qué cambiar. Los hallazgos se informan al administrador de red y no se corrigen en una red real sin autorización. Este caso es de papel con datos inventados. " + AVISO,
    ],
    vocab=[("superposición", "cuando dos canales se pisan y se interfieren"), ("contraseña robusta", "contraseña larga y difícil de adivinar, sin datos personales"), ("red abierta", "red sin clave ni cifrado"), ("hallazgo", "error o riesgo encontrado al revisar")],
    worked=[
        ("Detectar la superposición", "En 2,4 GHz, un punto usa el canal 2 y su vecino el canal 1. ¿Qué problema hay?", ["Los canales 1 y 2 están muy cerca.", "Se superponen y producen interferencia."], "Superposición de canales"),
        ("Contraseña débil", "Una contraseña de ejemplo es «abc». ¿Cuál es el hallazgo?", ["Es muy corta y fácil de adivinar.", "No es una contraseña robusta."], "Contraseña débil"),
    ],
    mistakes=[("Dejar un punto de acceso en red abierta «solo para visitas» sin separarla de la red interna.", "Quien entra a la red abierta puede intentar llegar a la red interna.", "Separa la red de visitas y protégela."),
              ("Revisar solo el canal y no el cifrado ni la contraseña.", "Una falla de seguridad puede ser más grave que una de calidad.", "Revisa las cuatro cosas de la lista.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es una red abierta?", "Una red sin clave ni cifrado", "Una red con WPA3", "Una red solo para empleados", "La red abierta no protege el tráfico."),
        ("abc", "En Telecomunicaciones: ¿qué es una contraseña robusta?", "Una contraseña larga y difícil de adivinar, sin datos personales", "Una contraseña corta que se recuerda fácil", "La fecha de nacimiento del dueño", "La robustez la da la longitud y la dificultad de adivinarla."),
        ("abc", "¿Por qué dos puntos en canales 1 y 3 se interfieren?", "Porque los canales están tan cerca que se superponen", "Porque están en distintas bandas", "Porque no tienen SSID", "Los canales cercanos se pisan entre sí."),
        ("abc", "{F} ¿Qué punto tiene un canal que se superpone con otros?", "P2, con el canal 3", "P1, con el canal 1", "P3, con el canal 6", "El canal 3 se superpone con el 1 y con el 6."),
        ("abc", "{F} ¿Qué hallazgo de seguridad tiene P3?", "Está abierta, sin clave", "Tiene WPA2", "Tiene canal 11", "La ficha dice que P3 es una red abierta."),
        ("abc", "{F} ¿Qué problema tiene la contraseña «1234» anotada en la ficha?", "Es débil y fácil de adivinar", "Es demasiado larga", "Tiene datos personales", "Una contraseña tan corta es adivinable."),
        ("=", "{F} De los 3 puntos, uno tiene canal superpuesto y uno red abierta. ¿Cuántos puntos no presentan ninguno de esos dos problemas?", "3-1-1", "Se restan los puntos con problema a los tres.", " punto"),
        ("abc", "{F} ¿Qué canal conviene asignar a P2 para evitar la superposición?", "11", "2", "3", "Los canales 1, 6 y 11 no se superponen; el 11 queda libre."),
        ("abc", "{F} P3 usa el SSID «Biblioteca2», distinto de los otros. ¿Qué efecto tiene en el roaming?", "El dispositivo no pasa solo de P2 a P3", "Mejora el roaming", "No cambia nada", "Con SSID distinto hay que cambiar de red manualmente."),
        ("abc", "{F} ¿Qué debe hacer la persona que revisa la configuración con los hallazgos?", "Informarlos al administrador de red y esperar autorización", "Cambiar todo en la red real sin avisar", "Guardar silencio", "Los cambios en la red real se autorizan."),
        ("=", "{F} Si cada uno de los 3 puntos atiende a 25 personas, ¿cuántas personas se conectan en total?", "3*25", "Se multiplican los puntos por las personas de cada uno.", " personas"),
        ("abc", "{F} La queja «la señal se corta en el fondo» puede deberse a la falta de roaming o a la distancia. ¿Qué dato de la ficha apoya la primera causa?", "Los SSID distintos y la configuración diferente entre puntos", "Que todos usen WPA2", "Que haya tres puntos", "El roaming requiere el mismo SSID y la misma configuración."),
        ("abc", "El administrador de ejemplo anota la contraseña de la red en un cartel visible para todos los visitantes. ¿Qué corresponde?", "Quitarlo y dar la clave solo a quien corresponde", "Dejarlo para evitar preguntas", "Agrandar el cartel", "La clave no se expone en público."),
    ],
    ctx=("abc", "La directora de ejemplo pregunta por qué lo mejor no es dejar todo sin clave para evitar problemas de acceso. ¿Qué responde el técnico?", "Que una red sin clave expone los datos y permite usos indebidos", "Que sí, que es lo mejor", "Que depende del color del equipo", "La seguridad básica exige cifrado y clave."),
    sc=[
        ("En Telecomunicaciones: ¿qué es una red abierta?", "Una red sin clave ni cifrado", "Sin cifrado ni clave no se protege el tráfico."),
        ("¿Qué canales de 2,4 GHz no se superponen?", "1, 6 y 11", "Esos canales no se superponen y evitan la interferencia."),
        ("¿Qué se hace con los hallazgos?", "Se informan al administrador y se espera autorización", "No se corrige una red real sin permiso del responsable."),
    ],
    op=("Una veterinaria de ejemplo tiene dos puntos de acceso en 2,4 GHz: V1 canal 6, SSID «Vet», WPA3; V2 canal 7, SSID «Vet», red abierta. Contraseña anotada de V1: «gato». Escribe una lista de hallazgos (qué está mal y por qué) y la corrección que propondrías al administrador.",
        "Hallazgos: 1) V2 usa el canal 7, que se superpone con el 6 de V1. 2) V2 es red abierta, sin cifrado. 3) La contraseña «gato» es débil. Propuesta: cambiar V2 a un canal sin superposición (por ejemplo, el 1 o el 11), activar WPA2 o WPA3 en V2 y poner una contraseña robusta. Todo con autorización.",
        ["detecta la superposición", "detecta la red abierta y la contraseña débil", "propone correcciones con autorización"],
        ["lista de tres hallazgos con su corrección"],
        ["no ver la superposición", "no ver la red abierta", "corregir sin autorización"],
        "Pregunta: «¿qué canal conviene para V2?». Si no responde, pídele que recuerde los canales 1, 6 y 11."),
    reinforce="Escribe un hallazgo de ejemplo sobre una contraseña débil y la corrección que propondrías.",
    extend="Explica con un ejemplo inventado por qué los puntos de acceso con distinto SSID dificultan el roaming.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 12 (criterio técnico con datos de ejemplo, inventados). El «Centro Cívico Lago Azul» (ficticio) planifica la red inalámbrica de un salón de 600 m² con 90 personas simultáneas. Datos de ejemplo: cada punto de acceso cubre hasta 200 m² con buena señal; "
     "cada punto ofrece una velocidad total de 300 Mbps compartida entre sus usuarios (de ejemplo); cada persona necesita 10 Mbps para trabajar bien; se desea un margen de al menos 1 punto de acceso de reserva. "
     "Canales de ejemplo en 2,4 GHz: 1, 6 y 11 sin superposición.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular cuántos puntos de acceso hacen falta por cobertura y por capacidad.",
    prior=["Sé qué es cobertura, banda y canal.", "Sé dividir y multiplicar.", "Sé redondear hacia arriba."],
    explain=[
        "Para decidir cuántos puntos de acceso hacen falta se hacen dos cálculos. El primero es por cobertura: se divide el área por el área que cubre cada punto. El segundo es por capacidad: se calcula cuántos usuarios soporta cada punto dividiendo su velocidad total por lo que necesita cada persona, y luego se divide la cantidad de personas por esa cifra. En ambos casos, si no da exacto, se redondea hacia arriba.",
        "Se elige el mayor de los dos resultados, porque debe cumplirse cobertura y capacidad a la vez. Después se agrega la reserva que pide el proyecto. Con la cantidad final de puntos se asignan canales sin superposición, y si hay más puntos que canales sin superposición, se reutilizan canales en puntos lejanos entre sí.",
        "La conclusión se escribe con los números y se entrega a la jefatura. Los valores reales de alcance y velocidad dependen del equipo, del lugar y de la norma vigente; aquí se usan solo cifras de ejemplo. La instalación de los puntos exige personal autorizado, sobre todo si es en altura. " + AVISO,
    ],
    vocab=[("cálculo por cobertura", "puntos necesarios según el área que cubre cada uno"), ("cálculo por capacidad", "puntos necesarios según la velocidad que comparten los usuarios"), ("usuarios por punto", "cuántas personas soporta bien un punto de acceso"), ("reserva", "punto de acceso extra para cubrir imprevistos")],
    worked=[
        ("Por cobertura", "Un salón de ejemplo mide 400 m² y cada punto cubre 150 m². ¿Cuántos puntos hacen falta por cobertura?", ["400 entre 150 es un poco más de 2.", "Se redondea hacia arriba: 3."], "3 puntos"),
        ("Usuarios por punto", "Un punto de ejemplo ofrece 100 Mbps y cada persona necesita 5 Mbps. ¿Cuántas personas soporta?", ["Se divide la velocidad por lo que necesita cada persona.", "100 entre 5."], "20 personas"),
    ],
    mistakes=[("Calcular solo la cobertura y olvidar la capacidad.", "Un salón con muchas personas puede quedarse sin velocidad aunque tenga señal.", "Haz los dos cálculos y elige el mayor."),
              ("Redondear hacia abajo cuando el resultado no es exacto.", "Quedarían áreas o personas sin atender.", "Redondea hacia arriba al siguiente número entero.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué se calcula por cobertura?", "Los puntos necesarios según el área que cubre cada uno", "La velocidad de cada persona", "El precio del equipo", "La cobertura relaciona el área del lugar con el área que cubre cada punto."),
        ("abc", "En Telecomunicaciones: ¿qué se calcula por capacidad?", "Los puntos necesarios según los usuarios y la velocidad compartida", "El área del salón", "La cantidad de canales del mundo", "La capacidad mide cuántas personas soporta cada punto."),
        ("abc", "Si el cálculo no da un número entero, ¿cómo se redondea al decidir cuántos puntos poner?", "Hacia arriba", "Hacia abajo", "Siempre al más cercano", "Redondear hacia abajo dejaría una zona sin cobertura."),
        ("=", "{F} ¿Cuántos puntos hacen falta por cobertura para el salón de 600 m²?", "600//200", "Se divide el área del salón por lo que cubre cada punto.", " puntos"),
        ("=", "{F} ¿Cuántas personas soporta bien un punto, con 300 Mbps y 10 Mbps por persona?", "300//10", "Se divide la velocidad total por lo que necesita cada persona.", " personas"),
        ("=", "{F} ¿Cuántos puntos hacen falta por capacidad para 90 personas?", "90//30", "Se divide las personas por las que soporta cada punto.", " puntos"),
        ("abc", "{F} Por cobertura hacen falta 3 puntos y por capacidad 3 puntos. ¿Cuántos se necesitan antes de agregar la reserva?", "3", "6", "2", "Se elige el mayor de los dos resultados, que es 3."),
        ("=", "{F} ¿Cuántos puntos se instalan en total al agregar la reserva de 1 punto?", "3+1", "Se suma la reserva al mayor de los dos cálculos.", " puntos"),
        ("abc", "{F} Con 4 puntos y solo 3 canales sin superposición, ¿qué corresponde?", "Reutilizar un canal en dos puntos lejanos entre sí", "Poner dos puntos cercanos en el mismo canal", "Quitar un punto", "Los canales se reutilizan en puntos distantes."),
        ("=", "En otro salón de ejemplo hay 100 personas y cada punto soporta 30. ¿Cuántos puntos hacen falta por capacidad, redondeando hacia arriba?", "(100+29)//30", "100 entre 30 no es exacto y se redondea hacia arriba.", " puntos"),
        ("abc", "{F} Un salón de 700 m² con 90 personas. Cobertura: 700 entre 200 da 3,5. Capacidad: 3 puntos. ¿Cuántos puntos antes de la reserva?", "4", "3", "5", "Por cobertura se redondea hacia arriba a 4, que es mayor que 3."),
        ("abc", "{F} El director propone colgar un punto de acceso en una viga alta del salón. ¿Qué corresponde?", "Que lo haga personal autorizado, con norma vigente y protección", "Que un profesor suba a una escalera", "Que lo haga un apoderado voluntario", "El trabajo en altura es de personal autorizado."),
        ("abc", "Una persona calcula 90 personas entre 10 Mbps y obtiene 9 puntos. ¿Cuál es su error?", "Dividió las personas por la necesidad en Mbps en vez de usar los usuarios que soporta cada punto", "Usó la reserva", "Olvidó el canal", "La capacidad se calcula dividiendo las personas por las que soporta cada punto."),
    ],
    ctx=("abc", "El presupuesto de ejemplo del centro solo alcanza para 3 puntos y el cálculo con reserva da 4. ¿Qué recomienda el técnico?", "Informar que sin la reserva queda sin respaldo y que la jefatura decida con los números", "Poner 3 y no decir nada", "Poner 4 sin autorización", "La decisión se toma con los números a la vista."),
    sc=[
        ("En Telecomunicaciones: ¿cómo se calculan los puntos por cobertura?", "Dividiendo el área por lo que cubre cada punto", "Si no da exacto, se redondea hacia arriba al entero siguiente."),
        ("¿Qué se elige entre cobertura y capacidad?", "El mayor de los dos resultados", "Deben cumplirse la cobertura y la capacidad a la vez."),
        ("¿Quién instala puntos en altura?", "Personal autorizado", "El cuaderno no habilita para instalar."),
    ],
    op=("Una escuela de ejemplo planea la red de un gimnasio de 500 m² para 120 personas simultáneas. Cada punto cubre 250 m², ofrece 400 Mbps compartidos y cada persona necesita 10 Mbps; se pide 1 punto de reserva. Calcula (a) los puntos por cobertura, (b) las personas por punto y los puntos por capacidad, (c) el total con reserva y (d) qué tipo de persona instalaría los puntos en altura.",
        "(a) 500 entre 250 son 2 puntos. (b) 400 entre 10 son 40 personas por punto; 120 entre 40 son 3 puntos. (c) El mayor es 3; con la reserva son 4. (d) Personal autorizado, con norma vigente y protección.",
        ["calcula los puntos por cobertura", "calcula los puntos por capacidad", "suma la reserva y nombra a quien instala"],
        ["hoja con los cálculos y la conclusión"],
        ["calcular solo la cobertura", "olvidar la reserva", "proponer que cualquiera instale en altura"],
        "Pregunta: «¿cuál de los dos cálculos es mayor?». Si no responde, pídele que los compare lado a lado."),
    reinforce="Calcula cuántos usuarios soporta un punto de 200 Mbps si cada persona necesita 10 Mbps.",
    extend="Explica con un ejemplo inventado por qué un salón puede tener buena cobertura y aun así mala velocidad.",
)

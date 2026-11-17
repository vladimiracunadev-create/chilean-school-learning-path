"""Refrigeración y Climatización TP 3.º y 4.º medio: OAE-04 (redes de ductos y cañerías: documentos, riesgos y calidad) y OAE-05 (instalación de equipos y componentes: documentos, control automático y recepción). Solo conceptos y planillas, con datos de ejemplo; sin procedimientos de ejecución."""
from __future__ import annotations

from tp_recl_common import AVISO, EMER, build

O4 = "TP-RECL-3y4-OAE-04"
O5 = "TP-RECL-3y4-OAE-05"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Centro Norte» (ficticio): redes de cañerías de refrigerante y de ductos de aire en un local de 200 m². Tareas de la obra, en lista: colgar ductos, instalar cañerías, "
     "unir tuberías con soldadura (trabajo en caliente), aislar cañerías y ductos, y revisar la hermeticidad de las uniones. Riesgos anotados: quemadura y fuego por el trabajo en caliente, humos, alta presión, cortes con planchas, caída desde altura y descarga eléctrica.")
build(
    O4, 1, F,
    use="Aprenderé qué riesgos tiene armar redes de ductos y cañerías, qué es el trabajo en caliente, cómo se ordenan las medidas de control y por qué un permiso de trabajo no se omite.",
    prior=["Sé qué documentos forman un proyecto.", "Sé qué es una red de cañerías y una de ductos.", "Sé qué es un EPP."],
    explain=[
        "Armar una red de ductos o de cañerías es unir piezas para formar un recorrido por donde circulan aire, agua o refrigerante. Una unión soldada junta dos piezas metálicas con calor y un metal de aporte. La hermeticidad es la condición de que el fluido no se escapa por las uniones; de ella dependen la seguridad, el rendimiento y la protección del medio ambiente. Las tareas de unión con llama o calor intenso se llaman trabajo en caliente, y se hacen siguiendo la norma de buenas prácticas vigente.",
        "El trabajo en caliente produce llama, chispas o calor y puede causar quemaduras, incendios y humos. Por eso exige un permiso de trabajo: un documento firmado por quien autoriza, que dice qué tarea se hará, dónde y con qué medidas. Solo lo realiza personal calificado y autorizado. Las medidas de control se ordenan en una jerarquía, de la más a la menos eficaz: eliminar el riesgo, sustituirlo por uno menor, aislarlo con barreras o ingeniería, organizar el trabajo con reglas y capacitación, y por último usar EPP.",
        f"Este cuaderno no explica cómo ejecutar uniones ni soldaduras: solo conceptos y documentos. {EMER} {AVISO}",
    ],
    vocab=[("unión soldada", "unión de dos piezas metálicas con calor y un metal de aporte"), ("hermeticidad", "condición de que el fluido no se escapa por las uniones"), ("trabajo en caliente", "tarea que produce llama, chispas o calor intenso"), ("permiso de trabajo", "documento firmado que dice qué tarea riesgosa se hará, dónde y con qué medidas"), ("jerarquía de controles", "orden de las medidas contra un riesgo, de la más eficaz a la menos eficaz"), ("personal calificado", "personas evaluadas y autorizadas para una tarea riesgosa")],
    worked=[
        ("Clasificar un control", "En una obra de ejemplo se instala una barrera física que separa a las personas de una zona riesgosa. ¿Qué nivel de la jerarquía es?", ["Una barrera aísla el riesgo con ingeniería.", "No elimina el riesgo ni solo da protección personal."], "Aislar con barreras o ingeniería"),
        ("Identificar el trabajo en caliente", "Una tarea de ejemplo consiste en colgar una rejilla con tornillos. ¿Es trabajo en caliente?", ["El trabajo en caliente produce llama, chispas o calor intenso.", "Atornillar no produce ninguno de los tres."], "No, no es trabajo en caliente"),
    ],
    mistakes=[("Omitir el permiso de trabajo porque la tarea es corta.", "El riesgo de incendio o quemadura no depende de cuánto dure.", "Exige el permiso siempre que haya trabajo en caliente."),
              ("Creer que con EPP ya no hacen falta otros controles.", "El EPP es el último nivel de la jerarquía y no elimina el riesgo.", "Usa EPP junto con controles más eficaces.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es el trabajo en caliente?", "Toda tarea que produce llama, chispas o calor intenso", "Toda tarea que se hace en verano", "Toda tarea que se hace con equipos encendidos", "Lo que define el trabajo en caliente es la llama, la chispa o el calor intenso, no la estación ni el equipo."),
        ("abc", "¿Qué significa que una red tenga hermeticidad?", "Que el fluido no se escapa por las uniones", "Que la red es liviana y fácil de transportar", "Que la red se puede desarmar rápidamente", "La hermeticidad es impedir que el fluido se escape; no se refiere al peso ni a la facilidad de desarmar."),
        ("abc", "¿Qué es un permiso de trabajo?", "Un documento firmado que dice qué tarea riesgosa se hará, dónde y con qué medidas", "Una autorización del cliente para comprar materiales", "Un certificado de que el EPP es nuevo", "El permiso describe tarea, lugar y medidas de una labor riesgosa; no es una compra ni un certificado de EPP."),
        ("=", "{F} La empresa cobra $3.500 por m² por las redes del local. ¿Cuánto cobra por los 200 m²?", "200*3500", "Se multiplica el valor por m² por la superficie del local.", " pesos"),
        ("abc", "{F} ¿Qué tarea de la lista exige permiso de trabajo en caliente?", "Unir tuberías con soldadura", "Colgar ductos", "Aislar cañerías y ductos", "Solo la soldadura produce llama o calor intenso entre las tareas de la lista."),
        ("abc", "{F} ¿Qué riesgo anotado en la ficha se asocia directamente al trabajo en caliente?", "Quemadura y fuego", "Corte con planchas", "Caída desde altura", "La llama y el calor producen quemaduras e incendios; los cortes y las caídas tienen otras causas."),
        ("=", "Un jefe de obra de ejemplo asigna 1 supervisor por cada 5 trabajadores. Si trabajan 25 personas, ¿cuántos supervisores hay?", "25//5", "Se divide el número de trabajadores por la cantidad que cubre cada supervisor.", " supervisores"),
        ("abc", "{F} Un ayudante propone unir una tubería «rápido» sin permiso porque el trabajo es corto. ¿Qué corresponde?", "No hacerlo: el trabajo en caliente exige permiso, personal calificado y medidas contra incendio", "Hacerlo si dura menos de diez minutos", "Hacerlo si otra persona lo mira", "El riesgo existe aunque la tarea sea corta o haya público; el permiso y la calificación son obligatorios."),
        ("abc", "{F} Para el riesgo de caída de una obra de ejemplo, ¿qué medida es la más eficaz según la jerarquía de controles?", "Eliminar el riesgo, por ejemplo prefabricando el tramo a nivel del suelo", "Dar una charla de seguridad antes de empezar", "Usar casco durante la jornada", "Eliminar el riesgo está al tope de la jerarquía; la charla y el casco están más abajo."),
        ("ab", "{F} Un compañero dice: «con EPP ya no hace falta ningún otro control». ¿Es correcto?", "No: el EPP es el último nivel de la jerarquía y se usa junto con otros controles", "Sí: con EPP el riesgo desaparece por completo", "El EPP protege a la persona pero no elimina el riesgo, que sigue ahí."),
        ("abc", "{F} Aparece un humo espeso en la zona de trabajo y una persona se siente mal. ¿Qué indican las reglas generales?", "No entrar ni tocar, avisar a un adulto responsable y llamar a emergencias", "Entrar a ayudar sin protección porque es urgente", "Esperar a que el humo baje para avisar", "Entrar sin protección puede sumar más afectados; se avisa de inmediato."),
        ("=", "{F} La obra tiene 24 trabajadores y el 25 % necesita capacitación en trabajo en caliente. ¿Cuántos trabajadores son?", "24*25//100", "Se calcula el 25 % de 24 trabajadores.", " trabajadores"),
        ("abc", "{F} El cliente pide terminar una semana antes y propone omitir el permiso de trabajo en caliente. ¿Qué responde el jefe de obra?", "Que el permiso no se omite: protege a las personas y lo exige la norma vigente", "Que lo omitirá solo esta vez", "Que lo omitirá si el cliente firma una carta", "Un plazo o una carta del cliente no reemplazan un requisito de seguridad."),
    ],
    ctx=("abc", "Un estudiante de ejemplo ve que unos instaladores van a unir tuberías sin permiso y sin extintor cerca. ¿Qué corresponde?", "No participar, avisar al jefe de obra o a un adulto responsable", "Ayudar para que terminen rápido", "Grabar un video y subirlo a redes", "La actuación correcta es avisar a quien tiene autoridad; ayudar suma riesgo y publicar no resuelve nada."),
    sc=[
        ("En Refrigeración: ¿qué es la hermeticidad de una red?", "Que el fluido no se escapa por las uniones", "De ella dependen la seguridad y el rendimiento."),
        ("¿Qué exige el trabajo en caliente?", "Permiso de trabajo, personal calificado y medidas contra incendio", "El riesgo existe aunque la tarea sea corta."),
        ("¿Cuál es el último nivel de la jerarquía de controles?", "Los elementos de protección personal (EPP)", "El EPP protege a la persona pero no elimina el riesgo."),
    ],
    op=("Proyecto de ejemplo «Quiosco Faro» (ficticio): se debe unir un tramo de cañería con soldadura, aislar un ducto con planchas de bordes filosos y colgar un ducto a 3 m de altura. "
        "Escribe (a) cuál tarea es trabajo en caliente y qué documento exige, (b) un riesgo de cada tarea, (c) un control de cada nivel de la jerarquía para el riesgo de caída (de eliminar a EPP) y (d) quién puede ejecutar estas tareas.",
        "(a) Unir con soldadura; exige permiso de trabajo. (b) Soldadura: quemadura o incendio; planchas: cortes; altura: caída. (c) Eliminar: preparar el tramo a nivel del suelo; sustituir: reemplazar una escala por una plataforma estable; aislar: barandas; organizar: reglas de trabajo y capacitación; EPP: arnés y casco. (d) Personal calificado y autorizado, con norma vigente.",
        ["identifica el trabajo en caliente y el permiso", "nombra un riesgo por tarea", "ordena los controles según la jerarquía", "indica quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["poner EPP como primer control", "omitir el permiso", "decir que cualquiera puede ejecutar"],
        "Pregunta: «¿por qué el EPP es el último nivel?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe los cinco niveles de la jerarquía de controles, del más eficaz al menos eficaz, con un ejemplo de cada uno.",
    extend="Explica con un ejemplo por qué una obra bien planificada necesita menos EPP que una mal planificada.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Línea L1, cañería de refrigerante: cobre, 12 m. Línea L2, cañería de agua: acero, 8 m. Ducto D1: plancha galvanizada, 10 m. "
     "Precios de ejemplo por metro: cobre $5.000; acero $3.000; ducto $4.500. Documentos: especificación de materiales (revisión B), isométrico (revisión C), certificado de calificación del soldador (vence en 2 meses; la obra durará 4 meses) y registro de inspección de uniones (en blanco). "
     "Regla de ejemplo: un soporte cada 2 m de cañería, contando ambos extremos.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de las redes de cañerías y ductos: materiales, soportes, aislación, y los documentos y roles que respaldan una instalación.",
    prior=["Sé qué es una red de ductos y de cañerías.", "Sé qué es un permiso de trabajo.", "Sé sumar y multiplicar costos."],
    explain=[
        "Las cañerías pueden ser de metal o de plástico y el material lo fija la especificación de materiales. Un soporte es la pieza que sostiene una cañería o un ducto; la regla de separación entre soportes la entrega el proyecto. La aislación es un revestimiento que reduce las pérdidas de energía y, en superficies frías, evita que se forme agua por condensación, que moja y daña. El isométrico es un dibujo en perspectiva de una red, con sus tramos, accesorios y medidas.",
        "La calidad de una instalación se respalda con documentos. El certificado de calificación acredita que una persona fue evaluada para hacer uniones soldadas y tiene fecha de vencimiento. El registro de inspección de uniones deja constancia de que cada unión fue revisada y firmada. Los roles son el instalador, que arma la red; el soldador calificado, que hace las uniones soldadas; el inspector, que revisa y firma; y el supervisor, que libera el trabajo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("soporte", "pieza que sostiene una cañería o un ducto"), ("aislación", "revestimiento que reduce las pérdidas de energía y evita la condensación en superficies frías"), ("condensación", "agua que se forma cuando el aire húmedo toca una superficie fría"), ("isométrico", "dibujo en perspectiva de una red, con sus tramos, accesorios y medidas"), ("certificado de calificación", "documento que acredita que una persona fue evaluada para una tarea y tiene fecha de vencimiento"), ("registro de inspección", "documento donde cada unión revisada queda anotada y firmada")],
    worked=[
        ("Cantidad de soportes", "Con una regla de ejemplo de un soporte cada 3 m, contando ambos extremos, ¿cuántos soportes necesita una cañería de 9 m?", ["9 dividido por 3 son 3 espacios.", "Con ambos extremos hay un soporte más que espacios: 4."], "4 soportes"),
        ("Documento que falta", "Una obra de ejemplo termina las uniones y no hay constancia de que se revisaron. ¿Qué documento falta?", ["La constancia de revisión de uniones se anota en un documento.", "Es el registro de inspección de uniones."], "El registro de inspección de uniones"),
    ],
    mistakes=[("Pensar que el aislante es solo un adorno.", "Reduce pérdidas de energía y evita la condensación.", "Considéralo parte de la función del sistema."),
              ("Dejar sin llenar el registro de inspección porque «todo se hizo bien».", "Sin registro no queda prueba de la revisión.", "Anota y firma cada inspección.")],
    T=[
        ("abc", "En Refrigeración: ¿qué muestra un isométrico?", "La red dibujada en perspectiva, con sus tramos, accesorios y medidas", "El costo de cada tramo de la red", "La lista de personas que trabajan en la obra", "El isométrico es un dibujo de la red; los costos van al presupuesto."),
        ("abc", "¿Para qué sirve la aislación de una cañería fría?", "Para reducir las pérdidas de energía y evitar la condensación", "Para aumentar la presión del fluido", "Para sostener la cañería en su lugar", "La aislación cuida la energía y evita agua en la superficie; sostener es función de los soportes."),
        ("abc", "¿Qué acredita un certificado de calificación de soldador?", "Que la persona fue evaluada para hacer uniones soldadas y tiene fecha de vencimiento", "Que la obra tiene seguro contra incendios", "Que la persona puede dirigir la obra", "El certificado acredita la calificación de una persona para una tarea, no un seguro ni una jefatura."),
        ("=", "{F} ¿Cuántos metros de cañería suman las líneas L1 y L2?", "12+8", "Se suman las longitudes de las dos líneas.", " m"),
        ("=", "{F} ¿Cuánto cuesta la cañería L1?", "12*5000", "Se multiplica el precio por metro por los metros de la línea.", " pesos"),
        ("abc", "{F} ¿Qué línea de la ficha lleva refrigerante?", "L1", "L2", "D1", "Según la ficha, L1 es la cañería de refrigerante; L2 lleva agua y D1 es un ducto de aire."),
        ("=", "{F} Con la regla de la ficha, ¿cuántos soportes necesita la línea L2?", "8//2+1", "Se divide el largo por la separación y se suma un soporte por contar ambos extremos.", " soportes"),
        ("abc", "{F} El certificado del soldador vence en 2 meses y la obra durará 4. ¿Qué corresponde?", "Renovar o reemplazar el certificado antes de que venza para seguir con las uniones", "Continuar sin problema porque la obra ya empezó", "Usar el certificado de otra persona", "La calificación debe estar vigente mientras se hagan las uniones."),
        ("abc", "{F} La obra avanza y el registro de inspección de uniones sigue en blanco. ¿Qué problema hay?", "No queda constancia de que las uniones fueron inspeccionadas", "Ninguno, porque se inspeccionó de memoria", "Falta el plano de las líneas", "Sin registro no hay prueba de la revisión, aunque se haya hecho."),
        ("abc", "{F} Un compañero dice que el aislante del ducto es «puro adorno». ¿Qué respuesta es correcta?", "No: reduce pérdidas de energía y, en superficies frías, evita la condensación", "Sí: solo sirve para que se vea ordenado", "Sí, porque los ductos nunca se enfrían", "El aislante cumple una función energética y de protección contra la humedad."),
        ("abc", "{F} La especificación pide cobre para L1 y la lista de materiales trae acero. ¿Qué corresponde?", "Informar la diferencia al proyectista antes de comprar", "Comprar acero porque es más barato", "Comprar ambos para estar seguros", "Una diferencia entre documentos se informa; no se elige por precio."),
        ("=", "{F} Con acero a $3.000 el metro en L2 y ducto a $4.500 el metro en D1, ¿cuánto cuestan en total L1, L2 y D1?", "12*5000+8*3000+10*4500", "Se suman el costo de cada línea: metros por precio por metro.", " pesos"),
        ("abc", "{F} La especificación está en la revisión B y el isométrico en la revisión C. ¿Qué verificación se hace?", "Confirmar que ambos documentos corresponden a la misma versión vigente del proyecto", "Usar el que tenga la letra más cercana a la A", "Ignorar la letra y usar el más reciente impreso", "Las revisiones distintas pueden indicar versiones diferentes; se confirma con el proyectista."),
    ],
    ctx=("abc", "Una supervisora de ejemplo descubre que el soldador asignado tiene el certificado vencido hace una semana. ¿Qué hace?", "No lo autoriza a hacer uniones hasta que renueve el certificado", "Lo autoriza porque venció hace poco", "Lo autoriza si promete que lo renovará", "Un certificado vencido invalida la calificación, sin importar cuánto tiempo haya pasado."),
    sc=[
        ("En Refrigeración: ¿para qué sirve un soporte?", "Para sostener una cañería o un ducto", "La separación entre soportes la fija el proyecto."),
        ("¿Qué deja constancia de que las uniones fueron revisadas?", "El registro de inspección de uniones", "Sin registro no hay prueba de la revisión."),
        ("¿Qué acredita la calificación de un soldador?", "Un certificado vigente", "El certificado tiene fecha de vencimiento."),
    ],
    op=("Datos de ejemplo del «Local Alerce» (ficticio): línea de refrigerante de 16 m a $5.000 el metro; ducto de 12 m a $4.500 el metro; regla: un soporte cada 4 m de cañería, contando ambos extremos; certificado del soldador vence en 1 mes y la obra durará 3. "
        "Escribe (a) el costo de cada línea, (b) los soportes de la cañería, (c) qué problema detectas con el certificado y qué corresponde, (d) para qué sirve el registro de inspección.",
        "(a) Cañería: 16 por 5.000 son 80.000; ducto: 12 por 4.500 son 54.000. (b) 16 dividido por 4 son 4 espacios, más 1: 5 soportes. (c) El certificado vence antes de terminar la obra; hay que renovarlo antes de que venza. (d) Deja constancia de que cada unión fue inspeccionada y firmada.",
        ["calcula los costos", "calcula los soportes con ambos extremos", "detecta el certificado por vencer", "explica el registro"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el soporte del extremo", "ignorar el vencimiento", "decir que el registro es opcional"],
        "Pregunta: «¿por qué son 5 soportes y no 4?». Si no responde, pídele que relea la regla de contar ambos extremos."),
    reinforce="Escribe cuatro documentos de una instalación de cañerías y, junto a cada uno, quién lo firma o lo usa.",
    extend="Explica con un ejemplo qué problema causa una cañería fría sin aislación en un cielo falso.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (registro de inspección de ejemplo, inventado, de 12 uniones de una línea: U1 a U12). Resultados: 9 aprobadas; U4 y U9 observadas por un defecto visible; U11 sin firma del responsable. "
     "Regla de la obra de ejemplo: toda unión observada o sin firma queda pendiente y no se cubre con aislante hasta que el supervisor la libere. Costo de ejemplo de rehacer una unión observada: $18.000. "
     "Este caso solo lee el registro; las pruebas de hermeticidad las hace personal autorizado.")
build(
    O4, 3, F,
    use="Aprenderé a leer un registro de inspección de uniones, a distinguir uniones aprobadas y pendientes y a decidir qué se informa sin intervenir.",
    prior=["Sé qué es un registro de inspección.", "Sé calcular porcentajes sencillos.", "Sé que el supervisor libera el trabajo."],
    explain=[
        "Un registro de inspección lista cada unión con su resultado, la firma de quien la revisó y la fecha. Una unión aprobada cumple lo exigido. Una unión observada tiene un defecto que debe corregirse y una unión sin firma no tiene responsable. Ambas quedan pendientes. La liberación es la autorización escrita del supervisor para continuar, por ejemplo cubriendo la unión con aislante.",
        "No se cubre una unión pendiente porque el aislante taparía un posible defecto antes de revisarlo. Un porcentaje alto de uniones aprobadas no reemplaza la liberación unión por unión. El registro debe ser completo: resultado, firma y fecha. La inspección visual y las pruebas de hermeticidad las hace personal autorizado; este cuaderno solo enseña a leer sus resultados y a decidir qué informar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("unión aprobada", "unión que cumple lo exigido"), ("unión observada", "unión con un defecto que debe corregirse"), ("unión pendiente", "unión observada o sin firma que no puede cubrirse hasta ser liberada"), ("liberación", "autorización escrita del supervisor para continuar con el trabajo"), ("inspección visual", "revisión de una unión mirándola, hecha por personal calificado"), ("trazabilidad", "posibilidad de saber quién hizo y revisó cada cosa y cuándo")],
    worked=[
        ("Contar pendientes", "Un registro de ejemplo tiene 2 uniones observadas y 3 sin firma. ¿Cuántas quedan pendientes?", ["Las observadas y las sin firma quedan pendientes.", "2 más 3 son 5."], "5 uniones"),
        ("Porcentaje de aprobadas", "De 10 uniones de un registro de ejemplo, 8 están aprobadas. ¿Qué porcentaje es?", ["8 dividido por 10 son 0,8.", "Multiplicado por 100 es 80 %."], "80 %"),
    ],
    mistakes=[("Cubrir una unión observada porque «por fuera se ve bien».", "Un defecto visible o la falta de firma exigen liberación antes de cubrir.", "Espera la liberación escrita del supervisor."),
              ("Aprobar todo porque la mayoría de las uniones está aprobada.", "El porcentaje no libera las uniones pendientes.", "Libera unión por unión según el registro.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una unión pendiente en un registro de inspección?", "Una unión observada o sin firma que no puede cubrirse hasta ser liberada", "Una unión que se hará el próximo mes", "Una unión que ya fue cubierta con aislante", "Pendiente es la unión observada o sin firma; no es una fecha futura ni una unión cubierta."),
        ("abc", "¿Por qué no se cubre con aislante una unión pendiente?", "Porque taparía un posible defecto antes de revisarlo", "Porque el aislante se desperdicia si se pone antes", "Porque el aislante solo se usa en ductos", "Cubrir una unión sin liberar impide que el defecto se vea y se corrija."),
        ("abc", "¿Quién libera una unión pendiente?", "El supervisor, por escrito", "El instalador que la hizo", "El cliente de la obra", "La liberación es una autorización del supervisor; quien hizo el trabajo no se autoriza a sí mismo."),
        ("=", "{F} ¿Cuántas uniones quedan pendientes según las reglas de la ficha?", "2+1", "Se suman las dos observadas y la que no tiene firma.", " uniones"),
        ("=", "{F} ¿Qué porcentaje de las 12 uniones está aprobado?", "9*100//12", "Se divide el número de aprobadas por el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué uniones tienen un defecto visible?", "U4 y U9", "U9 y U11", "U4 y U11", "La ficha dice que U4 y U9 están observadas y U11 no tiene firma."),
        ("=", "{F} Si se rehacen las dos uniones observadas, ¿cuánto cuesta rehacerlas?", "2*18000", "Se multiplica el costo de rehacer una unión por las dos observadas.", " pesos"),
        ("abc", "{F} U11 no tiene firma del responsable. ¿Qué corresponde?", "Pedir que el responsable la revise y firme; mientras tanto queda pendiente", "Firmarla otro compañero para completar el registro", "Cubrirla porque no tiene defectos visibles", "Una unión sin firma sigue pendiente y firma quien la revisó."),
        ("abc", "{F} Un compañero propone cubrir U4 porque «se ve bien». ¿Qué respuesta es correcta?", "No: está observada; se cubre solo después de que el supervisor la libere", "Sí: si se ve bien, no hay problema", "Sí, pero solo en la parte que no tiene defecto", "La regla de la obra no permite cubrir una unión observada sin liberación."),
        ("abc", "{F} Un residente dice que 9 de 12 es un buen porcentaje y pide cubrir todas las uniones. ¿Qué responde el supervisor?", "Que las 3 pendientes no se cubren; el porcentaje no reemplaza la liberación", "Que se cubran todas, porque el porcentaje es alto", "Que se cubran las 3 pendientes y se revisen después", "La regla se aplica unión por unión, sin importar el porcentaje."),
        ("abc", "{F} El registro muestra que una unión aprobada fue hecha por una persona con el certificado vencido. ¿Qué corresponde?", "Informar al supervisor, porque no se cumplió la regla de personal calificado", "No hacer nada, porque la unión salió aprobada", "Borrar el nombre de la persona del registro", "Aprobada no significa que se cumplió la calificación exigida; se informa."),
        ("=", "{F} La espera de la liberación por el supervisor dura 3 días y rehacer las dos uniones agrega 1 día más. Si cada día de retraso cuesta $60.000, ¿cuánto cuesta el retraso?", "(3+1)*60000", "Se suman los días de retraso y se multiplican por el costo diario.", " pesos"),
        ("abc", "{F} Una unión aparece con la firma del responsable pero sin fecha. ¿Qué problema hay?", "No se puede comprobar cuándo se revisó: el registro queda incompleto", "Ninguno, porque la firma basta", "Que la unión debe rehacerse siempre", "La fecha es parte de la trazabilidad; sin ella el registro no es completo."),
    ],
    ctx=("abc", "Una ayudante de ejemplo nota que alguien borró un resultado «observada» de una unión del registro y escribió «aprobada». ¿Qué hace?", "Avisa al supervisor, porque cambiar un registro es adulterarlo", "Lo deja así para no generar conflicto", "Borra también otras observaciones para que todas parezcan iguales", "Adulterar un registro oculta riesgos; se informa a quien corresponde."),
    sc=[
        ("En Refrigeración: ¿cuándo queda pendiente una unión?", "Cuando está observada o sin firma", "Mientras esté pendiente no se cubre."),
        ("¿Quién libera una unión pendiente?", "El supervisor, por escrito", "Nadie se autoriza a sí mismo."),
        ("¿Quién hace la inspección visual y las pruebas de hermeticidad?", "Personal autorizado", "Este cuaderno no enseña a probar uniones."),
    ],
    op=("Registro de ejemplo de la «Línea Roble» (ficticia): 10 uniones; 7 aprobadas; U3 observada; U6 y U8 sin firma. Regla: toda unión pendiente no se cubre hasta ser liberada. Rehacer una unión observada cuesta $16.000. "
        "Escribe (a) cuántas uniones están pendientes, (b) qué porcentaje está aprobado, (c) cuánto cuesta rehacer la observada, (d) qué haces con U6 y U8 y quién decide si se cubren.",
        "(a) 1 observada y 2 sin firma: 3 pendientes. (b) 7 por 100 dividido por 10 son 70 %. (c) 16.000 pesos. (d) Pido que el responsable las revise y firme; el supervisor decide por escrito si se liberan, y mientras tanto no se cubren.",
        ["cuenta bien las pendientes", "calcula el porcentaje", "calcula el costo", "indica quién decide y que no se cubre"],
        ["hoja con las cuatro respuestas"],
        ["no contar las sin firma como pendientes", "decir que cubriría para avanzar", "decidir sin el supervisor"],
        "Pregunta: «¿quién decide si se cubren U6 y U8?». Si no responde, pídele que relea el papel del supervisor."),
    reinforce="Inventa un registro de ocho uniones con dos pendientes y calcula el porcentaje de aprobadas.",
    extend="Explica con un ejemplo por qué la firma y la fecha forman parte de la trazabilidad de una instalación.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Una cañería fría de 30 m. Sin aislación, la ganancia de calor de ejemplo es de 40 W por metro; con aislación, de 10 W por metro. El sistema funciona 3.000 horas al año. "
     "Tarifa de ejemplo: $150 por kWh. Costo de ejemplo de aislar: $2.500 por metro. Equivalencia: 1 kW son 1000 W. "
     "Simplificación de ejemplo, solo para esta planilla: se supone que cada W de calor que entra gasta 1 W de energía eléctrica.")
build(
    O4, 4, F,
    use="Aprenderé a estimar con datos de ejemplo cuánta energía y dinero se ahorra al aislar una cañería fría y a decidir si conviene.",
    prior=["Sé calcular kWh.", "Sé que 1 kW son 1000 W.", "Sé qué es la aislación."],
    explain=[
        "La ganancia de calor es el calor que entra a una cañería fría desde el ambiente y que el sistema debe volver a retirar, lo que gasta energía. Se mide en vatios (W). Si se conoce la ganancia por metro, se multiplica por el largo para obtener la ganancia total. La aislación reduce esa ganancia y, además, evita la condensación. El ahorro de potencia es la diferencia entre la ganancia sin aislación y con ella.",
        "Para pasar de potencia a dinero se hace una cadena de cuentas: la potencia en W se divide por 1000 para obtener kW; los kW se multiplican por las horas de funcionamiento y se obtienen kWh; los kWh se multiplican por la tarifa y se obtiene el costo. Con el ahorro anual y el costo de aislar se compara la inversión: si el ahorro de un año supera el costo de aislar, la inversión se recupera en menos de un año. En este cuaderno, para simplificar, cada W de calor que entra se toma como 1 W de energía eléctrica gastada; en un sistema real el gasto depende de la eficiencia del equipo y los datos de ganancia los entrega el proyecto.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("ganancia de calor", "calor que entra a una cañería fría desde el ambiente"), ("vatio (W)", "unidad de potencia; 1000 W son 1 kW"), ("ahorro de potencia", "diferencia entre la ganancia sin aislación y con ella"), ("inversión", "dinero que se gasta una vez para obtener un beneficio después"), ("tarifa", "precio de cada kWh de energía")],
    worked=[
        ("Ahorro de potencia", "Una cañería de ejemplo de 10 m gana 20 W por metro sin aislación y 5 W por metro con ella. ¿Cuántos W se ahorran?", ["Sin aislación: 10 por 20, que son 200 W. Con aislación: 10 por 5, que son 50 W.", "La diferencia es 150 W."], "150 W"),
        ("Pasar a dinero", "Un ahorro de ejemplo de 150 W funciona 2.000 horas y la tarifa es $100 por kWh. ¿Cuánto se ahorra?", ["150 W son 150 por 2.000 dividido por 1000, que son 300 kWh.", "300 por 100 son 30.000."], "$30.000"),
    ],
    mistakes=[("Multiplicar W por horas y por tarifa sin dividir por 1000.", "El resultado queda mil veces mayor, porque la tarifa es por kWh.", "Pasa los W a kW dividiendo por 1000 antes de usar la tarifa."),
              ("Decidir no aislar porque el aislante «cuesta plata».", "El ahorro de energía puede superar el costo.", "Compara el costo de aislar con el ahorro de un año.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la ganancia de calor de una cañería fría?", "El calor que entra desde el ambiente y que el sistema debe retirar", "El calor que el sistema entrega al recinto", "La energía que consume la bomba de la red", "La ganancia es el calor que entra a lo frío desde el ambiente; no es el calor entregado ni el consumo."),
        ("abc", "¿Por qué la aislación puede ahorrar dinero?", "Porque reduce la ganancia de calor y el sistema gasta menos energía", "Porque la cañería deja de necesitar soportes", "Porque el aislante produce frío por sí mismo", "Al ganar menos calor, el sistema debe retirar menos y consume menos energía."),
        ("abc", "¿Cómo se pasa de W a kW?", "Dividiendo por 1000", "Multiplicando por 1000", "Sumando 1000", "Un kilovatio equivale a 1000 vatios, por eso se divide."),
        ("=", "{F} ¿Cuántos W de ganancia de calor tiene la cañería sin aislación?", "30*40", "Se multiplica la ganancia por metro por el largo de la cañería.", " W"),
        ("=", "{F} ¿Cuántos W de ganancia de calor tiene la cañería con aislación?", "30*10", "Se multiplica la ganancia por metro con aislación por el largo.", " W"),
        ("=", "{F} ¿Cuántos W de potencia se ahorran al aislar la cañería?", "30*40-30*10", "Se resta la ganancia con aislación de la ganancia sin aislación.", " W"),
        ("=", "{F} ¿Cuántos kWh se ahorran en un año?", "(30*40-30*10)*3000//1000", "Se multiplica el ahorro en W por las horas y se divide por 1000 para pasar a kWh.", " kWh"),
        ("=", "{F} ¿Cuánto dinero se ahorra en un año con la tarifa de ejemplo?", "(30*40-30*10)*3000//1000*150", "Se multiplican los kWh ahorrados en el año por la tarifa de cada kWh.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta aislar los 30 m de cañería?", "30*2500", "Se multiplica el costo por metro por el largo.", " pesos"),
        ("abc", "{F} Comparando el ahorro de un año con el costo de aislar, ¿qué conclusión es correcta?", "El ahorro de un año supera el costo de aislar, así que la inversión se recupera en menos de un año", "Aislar nunca conviene, porque cuesta dinero", "No se puede concluir nada sin el color del aislante", "El ahorro anual calculado es mayor que el costo de aislar los 30 metros."),
        ("=", "{F} Si el sistema funcionara solo 2.000 horas al año, ¿cuántos kWh se ahorrarían?", "(30*40-30*10)*2000//1000", "Se repite el cálculo del ahorro con las nuevas horas de funcionamiento.", " kWh"),
        ("abc", "{F} Un compañero multiplica el ahorro en W por las horas y por la tarifa, sin dividir por 1000. ¿Cuál es su error?", "El resultado queda mil veces mayor, porque la tarifa es por kWh y no por Wh", "No hay error, porque W y kWh son lo mismo", "Debió dividir por las horas en vez de multiplicar", "La tarifa corresponde a kWh; los W deben pasarse a kW antes de usarla."),
        ("abc", "El aislante de una cañería fría en altura debe reponerse. Un ayudante propone subir a un techo sin arnés ni autorización «porque es rápido». ¿Qué corresponde?", "No hacerlo: el trabajo en altura lo realiza personal autorizado, con norma vigente y protección contra caídas", "Hacerlo si solo son cinco minutos", "Hacerlo si otro compañero sostiene la escala", "Un trabajo en altura es riesgoso aunque sea corto o haya quien sostenga una escala."),
    ],
    ctx=("abc", "El dueño de un local de ejemplo dice que prefiere no aislar una cañería para ahorrar en la obra. ¿Qué le responde el instalador?", "Que se compare el costo de aislar con el ahorro de energía y se informe al proyectista", "Que no aislar nunca causa problemas", "Que aislar siempre es obligatorio sin importar el costo", "La decisión se apoya en la comparación de costo y ahorro, y la define el proyecto."),
    sc=[
        ("En Refrigeración: ¿cómo se obtiene la ganancia total de una cañería?", "Multiplicando la ganancia por metro por el largo", "El total depende del largo de la cañería."),
        ("¿Cómo se pasa de W a kWh?", "Dividiendo por 1000 y multiplicando por las horas", "Así se obtiene la energía consumida o ahorrada."),
        ("¿Quién trabaja en techos o en altura?", "Personal autorizado, con protección contra caídas", "Este cuaderno no enseña trabajos en altura."),
    ],
    op=("Datos de ejemplo de la «Sala Nogal» (ficticia): cañería fría de 20 m; sin aislación gana 30 W por metro y con aislación 10 W por metro; funciona 2.500 horas al año; tarifa de ejemplo $120 por kWh; aislar cuesta $2.000 por metro. "
        "Escribe (a) el ahorro de potencia en W, (b) los kWh ahorrados en un año, (c) el dinero ahorrado en un año, (d) si el ahorro de un año supera el costo de aislar.",
        "(a) Sin aislación: 20 por 30 son 600 W; con ella: 20 por 10 son 200 W; ahorro de 400 W. (b) 400 por 2.500 dividido por 1000 son 1.000 kWh. (c) 1.000 por 120 son 120.000 pesos. (d) Aislar cuesta 20 por 2.000, o sea 40.000; el ahorro de un año supera ese costo.",
        ["calcula el ahorro de potencia", "pasa a kWh", "calcula el dinero ahorrado", "compara con el costo"],
        ["hoja con los cálculos"],
        ["no dividir por 1000", "olvidar multiplicar por el largo", "no comparar con el costo"],
        "Pregunta: «¿por qué divides por 1000?». Si no responde, pídele que relea cómo se pasa de W a kW."),
    reinforce="Inventa una cañería con su largo y su ganancia de calor con y sin aislación, y calcula el ahorro de potencia.",
    extend="Explica con un ejemplo por qué el ahorro por aislar también depende de las horas de funcionamiento.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Para una línea de agua helada de 20 m (no de refrigerante) se comparan tres opciones. Opción A: precio $5.000 por metro. Opción B: $3.000 por metro. Opción C: $1.500 por metro. "
     "Puntajes de 1 a 5 (5 es lo mejor), costo / facilidad de manejo / durabilidad: A, 2 / 4 / 5; B, 4 / 2 / 4; C, 5 / 5 / 2. Pesos de los criterios: costo 2, facilidad de manejo 1, durabilidad 3. "
     "Lista de control de calidad de ejemplo con 5 puntos: documentos vigentes, uniones firmadas, aislación completa, soportes revisados, registro archivado; en la entrega se cumplieron 4.")
build(
    O4, 5, F,
    use="Aprenderé a comparar alternativas de materiales con costos y puntajes, y a verificar la calidad de una instalación con una lista de control.",
    prior=["Sé calcular un puntaje ponderado.", "Sé qué es un registro de inspección.", "Sé calcular costos por metro."],
    explain=[
        "Cuando hay varias opciones de material se comparan con criterios, como el costo, la facilidad de manejo y la durabilidad. Cada opción recibe un puntaje en cada criterio; el puntaje se multiplica por el peso del criterio y se suma, y el resultado es el puntaje ponderado. El costo total se calcula aparte, con el precio por metro y el largo. La mejor opción no siempre es la más barata, ni la de mayor puntaje si no cumple lo que exige la especificación.",
        "La calidad de lo ejecutado se verifica con una lista de control: una lista de puntos que se revisan uno por uno. Un punto no cumplido es una no conformidad y se registra para corregirla; el porcentaje de cumplimiento resume el resultado, pero no reemplaza la corrección de cada punto. El acta de entrega se firma solo cuando los puntos críticos están cumplidos. Las pruebas del sistema las realiza personal autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("criterio", "característica que se usa para comparar opciones"), ("puntaje ponderado", "suma de cada puntaje multiplicado por el peso de su criterio"), ("lista de control de calidad", "lista de puntos que se revisan uno por uno al terminar un trabajo"), ("porcentaje de cumplimiento", "proporción de puntos cumplidos sobre el total"), ("acta de entrega", "documento firmado que deja constancia de lo entregado"), ("punto crítico", "punto cuyo incumplimiento puede afectar la seguridad o el funcionamiento")],
    worked=[
        ("Puntaje ponderado", "La opción M de ejemplo tiene puntajes 3 en costo (peso 2) y 5 en durabilidad (peso 1). ¿Cuál es su puntaje ponderado?", ["Cada puntaje se multiplica por su peso: 3 por 2 y 5 por 1.", "6 más 5 son 11."], "11 puntos"),
        ("Porcentaje de cumplimiento", "De 8 puntos de una lista de control de ejemplo se cumplieron 6. ¿Qué porcentaje es?", ["6 dividido por 8 es 0,75.", "Multiplicado por 100 es 75 %."], "75 %"),
    ],
    mistakes=[("Elegir la opción más barata sin mirar la durabilidad.", "Puede fallar antes y costar más después.", "Compara todos los criterios con su peso."),
              ("Firmar el acta de entrega aunque falte un punto crítico, porque el porcentaje es alto.", "Un punto crítico incumplido puede afectar la seguridad.", "Corrige y verifica el punto antes de firmar.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una lista de control de calidad?", "Una lista de puntos que se revisan uno por uno al terminar un trabajo", "Una lista de los precios de los materiales", "Una lista de las personas que trabajaron", "La lista de control verifica puntos de calidad; los precios y las personas se registran en otros documentos."),
        ("abc", "¿Qué es un punto crítico en una lista de control?", "Un punto cuyo incumplimiento puede afectar la seguridad o el funcionamiento", "Un punto que se revisa al final de la lista", "Un punto que ya está cumplido", "Lo crítico depende de las consecuencias, no del orden ni de si ya está cumplido."),
        ("abc", "¿Qué es el porcentaje de cumplimiento?", "La proporción de puntos cumplidos sobre el total de puntos", "El porcentaje de descuento sobre el precio", "El porcentaje de horas trabajadas", "Resume cuántos puntos de la lista se cumplieron respecto del total."),
        ("=", "{F} ¿Cuánto cuesta la línea de 20 m con la opción A?", "20*5000", "Se multiplica el precio por metro por el largo de la línea.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la línea de 20 m con la opción C?", "20*1500", "Se multiplica el precio por metro por el largo de la línea.", " pesos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de la opción A?", "2*2+4*1+5*3", "Cada puntaje de A se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de la opción B?", "4*2+2*1+4*3", "Cada puntaje de B se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de la opción C?", "5*2+5*1+2*3", "Cada puntaje de C se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("abc", "{F} Según los puntajes ponderados, ¿qué opción aparece primera?", "La opción A, con 23 puntos", "La opción B, con 22 puntos", "La opción C, con 21 puntos", "A suma 23, B suma 22 y C suma 21 con los pesos de la ficha."),
        ("=", "{F} ¿Qué porcentaje de los 5 puntos de la lista de control se cumplió en la entrega?", "4*100//5", "Se divide el número de puntos cumplidos por el total y se multiplica por 100.", " %"),
        ("abc", "{F} Un compañero dice: «la opción C es la más barata, así que es la mejor». ¿Qué respuesta es correcta?", "No necesariamente: C tiene la durabilidad más baja y ese criterio pesa más", "Sí: lo más barato siempre es lo mejor", "Sí, porque la durabilidad no se cuenta", "El criterio de durabilidad tiene el mayor peso y C es la peor en él."),
        ("=", "{F} Si el peso de la durabilidad subiera de 3 a 4, ¿cuál sería el nuevo puntaje ponderado de la opción C?", "5*2+5*1+2*4", "Se repite la suma de C con el nuevo peso de la durabilidad.", " puntos"),
        ("abc", "{F} En la entrega, el único punto no cumplido es «uniones firmadas». ¿Qué corresponde?", "Registrar la no conformidad y no firmar el acta hasta que las uniones estén firmadas", "Firmar el acta porque el cumplimiento es alto", "Firmar el acta y anotar el punto en una nota aparte", "Las uniones firmadas son un punto crítico: se corrige antes de firmar."),
    ],
    ctx=("abc", "Una jefa de obra de ejemplo recibe la instalación terminada con 9 de 10 puntos cumplidos y falta el registro de inspección de uniones. ¿Qué hace?", "Exige completar el registro antes de aceptar la entrega", "Acepta porque 9 de 10 es suficiente", "Acepta y pide el registro después de pagar", "Un registro faltante impide comprobar la calidad; se completa antes de aceptar."),
    sc=[
        ("En Refrigeración: ¿para qué sirve una lista de control de calidad?", "Para revisar punto por punto lo ejecutado y registrar lo que no cumple", "Así se detectan no conformidades antes de entregar."),
        ("¿Cuándo se firma el acta de entrega?", "Cuando los puntos críticos están cumplidos", "Un porcentaje alto no reemplaza lo crítico."),
        ("En refrigeración: ¿cómo se calcula un puntaje ponderado?", "Multiplicando cada puntaje por su peso y sumando", "Así los criterios importantes pesan más."),
    ],
    op=("Alternativas de ejemplo para el «Taller Boldo» (ficticio), línea de 10 m: opción P a $4.000 por metro, opción Q a $2.500 por metro. Puntajes costo / durabilidad: P, 2 / 5; Q, 5 / 2. Pesos: costo 1 y durabilidad 3. Lista de control de 10 puntos, 9 cumplidos. "
        "Escribe (a) el costo de cada opción, (b) el puntaje ponderado de cada una, (c) qué opción propones y por qué, (d) el porcentaje de cumplimiento y qué haces con el punto no cumplido.",
        "(a) P: 10 por 4.000 son 40.000; Q: 10 por 2.500 son 25.000. (b) P: 2 por 1 más 5 por 3 son 17; Q: 5 por 1 más 2 por 3 son 11. (c) Propongo P por su mayor puntaje, aunque cuesta más; lo informo con ambos datos. (d) 9 de 10 es 90 %; registro el punto no cumplido y lo corrijo antes de firmar el acta si es crítico.",
        ["calcula los costos", "calcula los puntajes ponderados", "justifica la propuesta", "registra el punto no cumplido"],
        ["hoja con los cálculos y la propuesta"],
        ["olvidar el peso", "elegir solo por costo", "firmar el acta con un punto crítico pendiente"],
        "Pregunta: «¿por qué P gana aunque cuesta más?». Si no responde, pídele que relea el papel del peso de cada criterio."),
    reinforce="Inventa tres opciones de material con puntajes y pesos, y calcula cuál tiene el mayor puntaje ponderado.",
    extend="Explica con un ejemplo por qué un alto porcentaje de cumplimiento no basta si falla un punto crítico.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Hotel Los Arrayanes» (ficticio): se instalará una unidad exterior de aire acondicionado de 85 kg, 3 unidades interiores, un controlador de pared y 3 sensores de temperatura. "
     "Documentos: especificaciones del proyecto, manual del fabricante (de ejemplo), plano de montaje y orientaciones escritas del profesional encargado. Riesgos anotados: manipulación de cargas, caída desde techos o altura, descarga eléctrica, "
     "refrigerante a presión y ruido. Límite de ejemplo para manipular una carga a mano: 20 kg, solo para este cálculo; el límite real lo fija la norma vigente.")
build(
    O5, 1, F,
    use="Aprenderé qué equipos y componentes se instalan en un sistema de climatización, quién da las orientaciones y qué riesgos exigen personal autorizado.",
    prior=["Sé qué documentos forman un proyecto.", "Sé qué es una especificación técnica.", "Sé qué es un EPP."],
    explain=[
        "Instalar un equipo es ubicarlo, fijarlo y dejarlo conectado siguiendo las especificaciones técnicas del proyecto, el manual del fabricante y las orientaciones del profesional encargado, que es quien responde por la obra. Un sistema de climatización tiene una unidad exterior, que se ubica fuera del recinto, y unidades interiores, que se ubican dentro. Los dispositivos de control automático, como el controlador y los sensores, deciden cuándo funciona el sistema. Los equipos no se modifican en la obra.",
        "Instalar equipos tiene riesgos importantes: mover cargas pesadas, trabajar en techos o en altura, la descarga eléctrica y el refrigerante a presión. Cada riesgo se controla con la jerarquía de controles: por ejemplo, las cargas pesadas se mueven con medios mecánicos y personal capacitado. La conexión a la red eléctrica la realiza un instalador eléctrico autorizado, según la norma vigente de la entidad fiscalizadora. Ante una duda se consulta al profesional encargado; no se improvisa.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("unidad exterior", "equipo que se ubica fuera del recinto y que intercambia calor con el exterior"), ("unidad interior", "equipo que se ubica dentro del recinto y que reparte el aire tratado"), ("controlador", "dispositivo que decide cuándo funciona el sistema"), ("sensor", "dispositivo que mide una magnitud, como la temperatura"), ("profesional encargado", "persona que responde por el proyecto y da las orientaciones de la obra"), ("manual del fabricante", "documento que indica cómo debe ser la instalación y los valores de cada equipo")],
    worked=[
        ("Peso sobre el límite", "Un equipo de ejemplo pesa 60 kg y el límite de ejemplo para cargar a mano es 25 kg. ¿Cuántos kg lo superan?", ["Se resta el límite del peso del equipo.", "60 menos 25 son 35."], "35 kg"),
        ("Quién da las orientaciones", "Una duda de ejemplo: el plano de montaje y el manual del fabricante dicen cosas distintas sobre la ubicación. ¿A quién se consulta?", ["La duda no se resuelve por cuenta propia.", "Se consulta al profesional encargado."], "Al profesional encargado"),
    ],
    mistakes=[("Modificar un equipo para que quepa en el espacio disponible.", "Cambia sus condiciones de seguridad y puede anular la garantía.", "Consulta al profesional encargado y respeta el manual."),
              ("Conectar un controlador a la red eléctrica porque «es solo un cable».", "Esa conexión exige un instalador eléctrico autorizado.", "No intervengas conexiones; avisa a quien corresponde.")],
    T=[
        ("abc", "En Refrigeración: ¿quién da las orientaciones durante la instalación de un equipo?", "El profesional encargado del proyecto", "El cliente que paga la obra", "El vendedor del equipo", "El profesional encargado responde por la obra; el cliente o el vendedor no dirigen la instalación."),
        ("abc", "¿Qué es una unidad exterior de un sistema de climatización?", "El equipo que se ubica fuera del recinto e intercambia calor con el exterior", "El equipo que reparte el aire dentro del recinto", "El dispositivo que mide la temperatura del recinto", "La unidad exterior está fuera; la interior reparte aire y el sensor mide."),
        ("abc", "¿Quién realiza la conexión eléctrica de un equipo?", "Un instalador eléctrico autorizado, según la norma vigente", "Cualquier ayudante de la obra", "El vendedor del equipo", "La conexión eléctrica es una tarea con riesgo de descarga y la hace personal autorizado."),
        ("=", "{F} ¿Cuántos kg superan el límite de ejemplo para manipular a mano la unidad exterior?", "85-20", "Se resta el límite del peso del equipo.", " kg"),
        ("abc", "{F} ¿Qué corresponde para mover la unidad exterior?", "Medios mecánicos y personal capacitado, según la norma vigente", "Que dos personas la carguen rápido", "Que una persona la arrastre por el suelo", "El peso supera el límite, por lo que se usan medios mecánicos y personal capacitado."),
        ("abc", "{F} ¿Qué riesgo de la ficha se asocia a trabajar en los techos?", "La caída desde altura", "El ruido", "La manipulación de cargas", "Trabajar en techos expone a caídas; el ruido y las cargas son otros riesgos."),
        ("=", "{F} ¿Cuántas piezas llegan en total (unidad exterior, interiores, controlador y sensores)?", "1+3+1+3", "Se suman la unidad exterior, las tres interiores, el controlador y los tres sensores.", " piezas"),
        ("abc", "{F} Un técnico propone conectar el controlador a la red eléctrica «porque es solo un cable». ¿Qué corresponde?", "No hacerlo: lo realiza un instalador eléctrico autorizado, con norma vigente", "Hacerlo si usa guantes", "Hacerlo si apaga la luz de la sala", "Los guantes o apagar una luz no reemplazan la autorización ni la norma vigente."),
        ("=", "{F} Se contratan 2 personas capacitadas por 3 días para mover la unidad, a $45.000 por persona por día. ¿Cuánto cuesta?", "2*3*45000", "Se multiplican las personas, los días y el valor por persona por día.", " pesos"),
        ("ab", "{F} Un instalador sugiere modificar la unidad exterior para que «quepa» en el espacio. ¿Es correcto?", "No: los equipos no se modifican; se consulta al profesional encargado", "Sí: si queda firme, se puede modificar", "Modificar un equipo cambia sus condiciones de seguridad y no lo decide quien instala."),
        ("abc", "{F} El manual del fabricante y la especificación indican espacios libres distintos alrededor del equipo. ¿Qué corresponde?", "Informar al profesional encargado antes de instalar", "Elegir el espacio más pequeño para ahorrar lugar", "Instalar y medir después", "Una diferencia entre documentos se informa antes de ejecutar."),
        ("=", "{F} La base soporta un máximo de ejemplo de 120 kg. Con la unidad exterior y 2 accesorios de 10 kg cada uno, ¿cuántos kg quedan de margen?", "120-(85+10+10)", "Se suma el peso total sobre la base y se resta del máximo.", " kg"),
        ("abc", "Una persona cae de un techo durante una instalación y no se mueve. ¿Qué indican las reglas generales?", "No tocarla ni moverla, avisar a un adulto responsable y llamar a emergencias", "Moverla rápido para que respire mejor", "Esperar a que se levante sola", "Ante un accidente grave no se mueve a la persona: se avisa a emergencias."),
    ],
    ctx=("abc", "Una estudiante de ejemplo en práctica ve que un técnico va a subir un equipo al techo sin medios mecánicos ni protección. ¿Qué corresponde?", "No participar y avisar al supervisor o a un adulto responsable", "Ayudar a empujar el equipo para que termine rápido", "Subir al techo a vigilar", "Intervenir sin protección agrava el riesgo; se avisa a quien tiene autoridad."),
    sc=[
        ("En Refrigeración: ¿quién da las orientaciones de la instalación?", "El profesional encargado del proyecto", "Él responde por la obra y resuelve las dudas."),
        ("¿Cómo se mueve una carga que supera el límite para manipular a mano?", "Con medios mecánicos y personal capacitado", "El límite real lo fija la norma vigente."),
        ("¿Quién conecta un equipo a la red eléctrica?", "Un instalador eléctrico autorizado", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Proyecto de ejemplo «Sala Ulmo» (ficticia): una unidad exterior de 70 kg, 2 unidades interiores y un controlador. Límite de ejemplo para cargar a mano: 20 kg. Se contratan 2 personas capacitadas por 2 días a $40.000 por persona por día. "
        "Escribe (a) cuántos kg supera la unidad exterior el límite, (b) cómo se debe mover, (c) cuánto cuestan las personas contratadas, (d) quién conecta el controlador a la red y a quién consultas una duda del plano.",
        "(a) 70 menos 20 son 50 kg. (b) Con medios mecánicos y personal capacitado. (c) 2 por 2 por 40.000 son 160.000 pesos. (d) Un instalador eléctrico autorizado; la duda se consulta al profesional encargado.",
        ["calcula el exceso de peso", "indica medios mecánicos y personal capacitado", "calcula el costo", "indica quién conecta y a quién se consulta"],
        ["hoja con las cuatro respuestas"],
        ["decir que se carga entre varios a mano", "decir que cualquiera conecta", "resolver la duda por su cuenta"],
        "Pregunta: «¿a quién consultas una duda del plano?». Si no responde, pídele que relea el papel del profesional encargado."),
    reinforce="Escribe los riesgos de instalar un equipo y, junto a cada uno, quién debe encargarse de él.",
    extend="Explica con un ejemplo por qué es riesgoso modificar un equipo en la obra para que quepa.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo, inventada, equipo ficticio «Modelo ZA»). Capacidad de enfriamiento: 8 kW. Potencia eléctrica: 2 kW. Masa: 40 kg. Componentes del sistema: compresor, condensador, evaporador y dispositivo de expansión. "
     "Control automático: sensor, termostato, controlador y actuador. COP (coeficiente de rendimiento) = calor que mueve el equipo dividido por la energía eléctrica que consume.")
build(
    O5, 2, F,
    use="Aprenderé la función de cada componente de un sistema de enfriamiento y de los dispositivos de control automático, y a leer una ficha técnica.",
    prior=["Sé qué es una unidad exterior e interior.", "Sé qué es una especificación técnica.", "Sé dividir."],
    explain=[
        "Un sistema de enfriamiento mueve calor del recinto hacia el exterior con un refrigerante que cambia de presión y de estado. El compresor hace circular el refrigerante y aumenta su presión. El condensador entrega al exterior el calor que el refrigerante transportó. El dispositivo de expansión reduce la presión del refrigerante antes de que entre al evaporador. El evaporador absorbe calor del recinto, y el ciclo vuelve a empezar. Esto es solo el concepto: este cuaderno no enseña a intervenir esos componentes.",
        "El control automático usa cuatro dispositivos. El sensor mide una magnitud, como la temperatura. El termostato compara la medida con la consigna, que es la temperatura deseada. El controlador decide qué hacer y el actuador ejecuta la acción, por ejemplo encender un compresor. La ficha técnica entrega los datos del equipo. El COP mide el rendimiento: un equipo que mueve 6 kW de calor y consume 2 kW de energía eléctrica tiene un COP de 3. Un COP mayor significa más calor movido por cada kW consumido.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("compresor", "componente que hace circular el refrigerante y aumenta su presión"), ("condensador", "componente que entrega calor al exterior"), ("evaporador", "componente que absorbe calor del recinto"), ("dispositivo de expansión", "componente que reduce la presión del refrigerante antes del evaporador"), ("consigna", "temperatura deseada que el sistema intenta mantener"), ("COP", "calor que mueve el equipo dividido por la energía eléctrica que consume"), ("actuador", "dispositivo que ejecuta la acción que decide el controlador")],
    worked=[
        ("Calcular un COP", "Un equipo de ejemplo mueve 6 kW de calor y consume 2 kW. ¿Cuál es su COP?", ["El COP es calor movido dividido por energía consumida.", "6 dividido por 2 son 3."], "COP de 3"),
        ("Identificar el dispositivo", "En un sistema de ejemplo, un dispositivo mide la temperatura del recinto. ¿Cuál es?", ["El que mide una magnitud es el sensor.", "El termostato compara; el controlador decide."], "El sensor"),
    ],
    mistakes=[("Decir que el termostato «enfría».", "El termostato compara la temperatura con la consigna; enfriar lo hace el sistema.", "Distingue qué mide, qué compara, qué decide y qué ejecuta."),
              ("Confundir el condensador con el evaporador.", "Uno entrega calor al exterior y el otro lo absorbe del recinto.", "Relaciona cada componente con la dirección del calor.")],
    T=[
        ("abc", "En Refrigeración: ¿qué función cumple el evaporador?", "Absorbe calor del recinto", "Expulsa calor al exterior", "Aumenta la presión del refrigerante", "El evaporador absorbe calor del recinto; expulsarlo es función del condensador."),
        ("abc", "¿Qué función cumple el condensador?", "Entrega al exterior el calor que transportó el refrigerante", "Absorbe calor del recinto", "Mide la temperatura del aire", "El condensador cede calor al exterior; absorberlo lo hace el evaporador."),
        ("abc", "¿Qué función cumple el compresor?", "Hace circular el refrigerante y aumenta su presión", "Reduce la presión antes del evaporador", "Decide cuándo enciende el sistema", "El compresor aumenta la presión; reducirla es del dispositivo de expansión y decidir es del controlador."),
        ("abc", "{F} ¿Qué hace el dispositivo de expansión?", "Reduce la presión del refrigerante antes de que entre al evaporador", "Aumenta la presión del refrigerante", "Mide la temperatura del recinto", "La expansión baja la presión; subirla es función del compresor."),
        ("=", "{F} ¿Cuál es el COP del Modelo ZA?", "8//2", "Se divide el calor que mueve el equipo por la energía eléctrica que consume.", ""),
        ("=", "{F} ¿Cuántos kWh de energía eléctrica consume el Modelo ZA en 6 horas de funcionamiento?", "2*6", "Se multiplica la potencia eléctrica por las horas de funcionamiento.", " kWh"),
        ("=", "{F} ¿Cuántos kWh de calor mueve el Modelo ZA en 6 horas de funcionamiento?", "8*6", "Se multiplica la capacidad de enfriamiento por las horas de funcionamiento.", " kWh"),
        ("abc", "{F} ¿Qué dispositivo del control automático mide la temperatura del recinto?", "El sensor", "El actuador", "El compresor", "El sensor mide; el actuador ejecuta y el compresor no pertenece al control."),
        ("abc", "{F} ¿Qué dispositivo decide si se debe encender o apagar el compresor?", "El controlador", "El sensor", "El evaporador", "El controlador decide; el sensor solo mide y el evaporador es un componente del ciclo."),
        ("abc", "{F} Un compañero dice que el termostato «enfría el recinto». ¿Cuál es su error?", "El termostato compara la temperatura con la consigna; enfriar lo hace el sistema", "El termostato no existe en estos sistemas", "El termostato calienta, no enfría", "El termostato es un dispositivo de control, no un componente que enfríe."),
        ("abc", "{F} La placa del equipo indica una tensión distinta de la que pide el proyecto. ¿Qué corresponde?", "Informar al profesional encargado antes de instalar", "Instalarlo y comprobar después", "Cambiar el dato de la placa", "Una diferencia entre equipo y proyecto se informa antes de ejecutar."),
        ("=", "{F} Otro equipo de ejemplo mueve 9 kW de calor y consume 3 kW de energía eléctrica. ¿Cuál es su COP?", "9//3", "Se divide el calor movido por la energía eléctrica consumida.", ""),
        ("abc", "{F} Comparando el COP del Modelo ZA con el de otro equipo que mueve 9 kW y consume 3 kW, ¿cuál tiene mejor rendimiento según su COP?", "El Modelo ZA, porque su COP es mayor", "El otro equipo, porque mueve más calor en total", "Rinden igual, porque ambos consumen energía", "El Modelo ZA tiene COP 4 y el otro 3: mueve más calor por cada kW consumido."),
    ],
    ctx=("abc", "Una técnica de ejemplo lee en la ficha técnica que el equipo tiene una masa de 40 kg y en la especificación una de 55 kg. ¿Qué hace?", "Informa la diferencia al profesional encargado antes de definir la fijación", "Usa el valor mayor sin avisar", "Usa el valor menor para ahorrar soportes", "Una diferencia entre documentos se informa; elegir un valor puede afectar la seguridad de la fijación."),
    sc=[
        ("En Refrigeración: ¿qué función cumple el condensador?", "Entrega calor al exterior", "El evaporador, en cambio, absorbe calor del recinto."),
        ("¿Cómo se calcula el COP?", "Dividiendo el calor que mueve el equipo por la energía eléctrica que consume", "Un COP mayor significa más calor movido por kW consumido."),
        ("¿Qué dispositivo ejecuta la acción que decide el controlador?", "El actuador", "El actuador enciende o apaga, por ejemplo, un compresor."),
    ],
    op=("Ficha técnica de ejemplo del equipo ficticio «Modelo XB»: capacidad de enfriamiento 12 kW; potencia eléctrica 3 kW; funciona 5 horas al día. "
        "Escribe (a) el COP, (b) los kWh eléctricos que consume al día, (c) el nombre y la función de dos componentes del ciclo, (d) qué dispositivo mide la temperatura y cuál ejecuta la acción de encender.",
        "(a) 12 dividido por 3 es 4. (b) 3 por 5 son 15 kWh. (c) Compresor: hace circular el refrigerante y aumenta su presión; evaporador: absorbe calor del recinto. (d) El sensor mide la temperatura; el actuador enciende.",
        ["calcula el COP", "calcula el consumo diario", "nombra dos componentes con su función", "distingue sensor y actuador"],
        ["hoja con las cuatro respuestas"],
        ["confundir condensador y evaporador", "dividir al revés el COP", "decir que el sensor ejecuta"],
        "Pregunta: «¿qué dispositivo mide y cuál ejecuta?». Si no responde, pídele que relea los cuatro dispositivos de control."),
    reinforce="Dibuja un esquema simple del ciclo con los cuatro componentes y una flecha que muestre hacia dónde va el calor.",
    extend="Explica con un ejemplo por qué un equipo con un COP mayor puede costar menos en energía.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (recepción de ejemplo, inventada). Especificación: 1 unidad exterior de 6 kW, 3 unidades interiores de 2 kW cada una, 3 sensores y 1 controlador, tensión 220 V. "
     "Guía de despacho (documento que acompaña la entrega): 1 unidad exterior de 5 kW, 3 interiores de 2 kW, 4 sensores y 1 controlador, tensión 220 V. La placa del equipo exterior coincide con la guía. Precio de ejemplo de un sensor: $12.000.")
build(
    O5, 3, F,
    use="Aprenderé a recibir equipos en papel: comparar la especificación con la guía de despacho y la placa, detectar diferencias y decidir qué informar.",
    prior=["Sé hacer una revisión cruzada de documentos.", "Sé qué es una especificación técnica.", "Sé sumar y multiplicar."],
    explain=[
        "La recepción de equipos es el momento en que se comprueba que lo entregado coincide con lo pedido. Se comparan tres documentos: la especificación, que dice qué se pidió; la guía de despacho, que dice qué se entregó; y la placa del equipo, que es la etiqueta que lleva escritos sus datos. Si todo coincide, la recepción es conforme y se firma el acta. Si hay diferencias, se anotan en el acta de recepción, que es el documento donde se registra lo recibido y lo observado.",
        "Un equipo distinto del especificado no se instala aunque «sirva igual»: cambiarlo exige la aprobación escrita del profesional encargado, porque afecta la capacidad, el consumo y el costo. Un descuento del proveedor no cambia la decisión técnica. Mientras se aclara, los equipos se guardan sin instalarse y la espera se registra. Las cantidades de más también son una diferencia: se informan y se devuelven o se aceptan por escrito.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("recepción", "momento en que se comprueba que lo entregado coincide con lo pedido"), ("guía de despacho", "documento que acompaña la entrega y dice qué se envió"), ("placa del equipo", "etiqueta del equipo con sus datos, como capacidad y tensión"), ("acta de recepción", "documento donde se registra lo recibido y lo observado"), ("recepción conforme", "recepción en que lo entregado coincide con lo pedido"), ("capacidad", "cantidad de calor que un equipo puede mover, medida en kW")],
    worked=[
        ("Comparar cantidades", "Una especificación de ejemplo pide 5 filtros y la guía de despacho trae 4. ¿Qué diferencia hay?", ["Se compara lo pedido con lo entregado.", "Faltó 1 filtro: 5 menos 4."], "Falta 1 filtro; se anota en el acta"),
        ("Total de capacidad", "Dos unidades interiores de ejemplo tienen 3 kW cada una. ¿Cuántos kW suman?", ["Se multiplica la capacidad de una por el número de unidades.", "2 por 3 son 6."], "6 kW"),
    ],
    mistakes=[("Instalar un equipo de menor capacidad porque «sirve igual».", "Puede no enfriar lo diseñado y consumir distinto.", "Informa la diferencia y espera la aprobación escrita."),
              ("Aceptar la entrega por un descuento sin consultar.", "La decisión técnica no se compra con un descuento.", "Consulta al profesional encargado antes de aceptar.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una guía de despacho?", "El documento que acompaña la entrega y dice qué se envió", "El plano que muestra dónde se instalará el equipo", "La lista de precios del proveedor", "La guía describe lo enviado; el plano y la lista de precios cumplen otras funciones."),
        ("abc", "¿Qué es una recepción conforme?", "Aquella en que lo entregado coincide con lo pedido", "Aquella en que el proveedor acepta todo sin revisar", "Aquella en que se paga antes de revisar", "Conforme significa que lo entregado cumple lo pedido, comprobado en la revisión."),
        ("abc", "Quien recibe un equipo y encuentra una diferencia con la especificación, ¿qué hace?", "La anota en el acta e informa antes de instalar", "Instala el equipo y avisa al terminar", "Cambia la especificación para que coincida", "Una diferencia se registra e informa antes de ejecutar."),
        ("=", "{F} ¿Cuántos kW de capacidad suman las tres unidades interiores?", "3*2", "Se multiplica la capacidad de una unidad interior por el número de unidades.", " kW"),
        ("=", "{F} ¿Cuántos kW le faltan a la unidad exterior entregada respecto de la especificada?", "6-5", "Se resta la capacidad entregada de la capacidad especificada.", " kW"),
        ("abc", "{F} ¿Qué diferencia hay en los sensores?", "Llegaron 4 y la especificación pide 3", "Llegaron 3 y la especificación pide 4", "Llegaron 2 y la especificación pide 3", "La guía trae 4 sensores y la especificación pide 3, uno de más."),
        ("=", "{F} ¿Cuánto vale el total de los 4 sensores recibidos?", "4*12000", "Se multiplica el precio de un sensor por los 4 recibidos.", " pesos"),
        ("abc", "{F} ¿Qué corresponde hacer con la unidad exterior de 5 kW?", "No instalarla hasta que el profesional encargado confirme si es válida", "Instalarla porque la placa y la guía coinciden", "Instalarla y cambiar la especificación", "La placa y la guía coinciden entre sí, pero no con lo que pide la especificación."),
        ("abc", "{F} Un instalador dice que la unidad de 5 kW «sirve igual» y quiere instalarla. ¿Qué respuesta es correcta?", "Instalar un equipo distinto del especificado exige aprobación escrita del profesional encargado", "Sirve igual, porque 1 kW de diferencia es poco", "Se instala si el cliente no lo nota", "Un cambio de capacidad afecta el diseño y debe aprobarse por escrito."),
        ("abc", "{F} La placa y la guía coinciden en 5 kW, pero la especificación pide 6 kW. ¿Qué indica eso?", "Que la diferencia viene del pedido o del despacho, no de la placa, y se informa", "Que la placa está equivocada", "Que la especificación debe borrarse", "Si placa y guía coinciden, el error está antes: en el pedido o el despacho."),
        ("abc", "{F} El proveedor ofrece un descuento de $150.000 por aceptar la unidad exterior de 5 kW. ¿Cambia la decisión?", "No: la decisión técnica la toma el profesional encargado, no el descuento", "Sí: un descuento justifica cualquier cambio", "Sí, si el descuento es mayor que el precio de un sensor", "Un descuento no reemplaza la aprobación técnica por escrito."),
        ("=", "{F} La espera de la aclaración retrasa la obra 4 días y cada día de obra cuesta $50.000. ¿Cuánto cuesta la espera?", "4*50000", "Se multiplican los días de espera por el costo diario.", " pesos"),
        ("abc", "{F} ¿Dónde queda registrada correctamente la diferencia de la unidad exterior?", "En el acta de recepción, con fecha y firma", "En un mensaje verbal al chofer", "En una nota personal de quien recibe", "El acta deja constancia escrita, fechada y firmada de lo observado."),
    ],
    ctx=("abc", "Una bodeguera de ejemplo recibe los equipos un viernes tarde y el profesional encargado no está. La guía no coincide con la especificación. ¿Qué hace?", "Registra la diferencia en el acta, guarda los equipos sin instalarlos y avisa al profesional encargado", "Instala igual para no perder el fin de semana", "Rechaza toda la entrega sin registrar nada", "Lo correcto es registrar, resguardar y avisar; no instalar ni rechazar sin constancia."),
    sc=[
        ("En Refrigeración: ¿qué tres documentos se comparan en la recepción de un equipo?", "La especificación, la guía de despacho y la placa", "Así se comprueba que lo entregado coincide con lo pedido."),
        ("¿Qué se hace con un equipo distinto del especificado?", "No se instala hasta contar con aprobación escrita", "Un cambio afecta capacidad, consumo y costo."),
        ("¿Dónde se registra la diferencia?", "En el acta de recepción", "El acta deja constancia escrita y firmada."),
    ],
    op=("Recepción de ejemplo del «Local Mirador» (ficticio): la especificación pide 2 unidades interiores de 3 kW, 1 exterior de 8 kW y 2 sensores; la guía de despacho trae 2 interiores de 3 kW, 1 exterior de 7 kW y 3 sensores. Un sensor cuesta $10.000. "
        "Escribe (a) la capacidad interior total, (b) las diferencias entre especificación y guía, (c) el valor de los sensores recibidos, (d) qué haces con la unidad exterior y dónde dejas constancia.",
        "(a) 2 por 3 son 6 kW. (b) La exterior es de 7 kW y se pidió de 8 (falta 1 kW); llegó 1 sensor de más. (c) 3 por 10.000 son 30.000 pesos. (d) No la instalo; informo al profesional encargado y registro la diferencia en el acta de recepción con fecha y firma.",
        ["calcula la capacidad", "detecta las dos diferencias", "calcula el valor", "registra en el acta y no instala"],
        ["hoja con las cuatro respuestas"],
        ["decir que instalaría porque sirve igual", "no ver el sensor de más", "dejar la constancia solo de palabra"],
        "Pregunta: «¿dónde dejas constancia de la diferencia?». Si no responde, pídele que relea el papel del acta de recepción."),
    reinforce="Inventa una recepción con tres equipos y una diferencia, y escribe lo que anotarías en el acta.",
    extend="Explica con un ejemplo por qué una cantidad de más también se informa en una recepción.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (control de ejemplo, inventado). Un termostato de ejemplo con consigna de 24 °C y diferencial de ±1 °C: el sistema de enfriamiento se enciende cuando la lectura es de 25 °C o más y se apaga cuando es de 23 °C o menos; con lecturas intermedias mantiene su estado anterior. "
     "Estado inicial: apagado. Lecturas cada hora, en orden: 24, 25, 26, 25, 24, 23, 24 y 25 °C. Cuando está encendido, el sistema consume 1 kW.")
build(
    O5, 4, F,
    use="Aprenderé la lógica de un control automático encendido-apagado con diferencial y a seguir su comportamiento con una tabla de lecturas escrita.",
    prior=["Sé qué es una consigna.", "Sé qué hacen el sensor, el controlador y el actuador.", "Sé calcular kWh."],
    explain=[
        "Un control encendido-apagado compara cada lectura del sensor con la consigna y decide si el actuador enciende o apaga el sistema. Si encendiera y apagara exactamente en la consigna, el sistema cambiaría de estado sin pausa. Para evitarlo se usa un diferencial, también llamado histéresis: un margen alrededor de la consigna. Con un diferencial de ±1 °C se enciende al subir por encima del margen superior, se apaga al bajar del margen inferior y entre ambos se mantiene el estado anterior.",
        "Cada vez que el sistema se enciende se produce un arranque. Demasiados arranques desgastan los equipos y gastan energía. Para seguir la lógica en papel se anota el estado después de cada lectura. Una lectura imposible, como una temperatura que ningún recinto tiene, indica un sensor con falla: se registra e informa, y lo revisa personal autorizado. Los ajustes reales de consigna y diferencial los fija el proyecto o el manual del fabricante.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("diferencial (histéresis)", "margen alrededor de la consigna que evita encender y apagar sin pausa"), ("arranque", "cada vez que el sistema pasa de apagado a encendido"), ("estado", "situación del sistema: encendido o apagado"), ("lectura imposible", "valor que no puede ser real, señal de falla del sensor"), ("control encendido-apagado", "control que solo enciende o apaga el sistema según la lectura")],
    worked=[
        ("Estado tras una lectura", "Un control de ejemplo con consigna de 20 °C y diferencial de ±2 °C enciende en 22 °C o más y apaga en 18 °C o menos. Estado apagado. Lectura 22 °C. ¿Qué estado queda?", ["22 °C llega al margen superior.", "El sistema se enciende."], "Encendido"),
        ("Estado intermedio", "Con el mismo control de ejemplo, el sistema está encendido y la lectura es 20 °C. ¿Qué estado queda?", ["20 °C está entre 18 y 22: es intermedia.", "Mantiene su estado anterior: encendido."], "Encendido"),
    ],
    mistakes=[("Pensar que con la lectura igual a la consigna el sistema siempre se apaga.", "En los valores intermedios mantiene su estado anterior.", "Revisa si la lectura llegó a un margen antes de cambiar el estado."),
              ("Aceptar una lectura imposible como si fuera real.", "Indica un sensor con falla.", "Regístrala e informa para que personal autorizado revise el sensor.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la consigna de un control?", "La temperatura deseada que el sistema intenta mantener", "La temperatura máxima que soporta el equipo", "La hora en que se enciende el sistema", "La consigna es el valor deseado; no es un límite del equipo ni una hora."),
        ("abc", "¿Para qué sirve el diferencial (histéresis) de un control?", "Para evitar que el sistema encienda y apague sin pausa", "Para hacer que el sistema consuma más energía", "Para medir la humedad del aire", "El diferencial crea un margen que reduce los arranques innecesarios."),
        ("abc", "¿Qué es un arranque?", "Cada vez que el sistema pasa de apagado a encendido", "Cada vez que se mide una temperatura", "Cada vez que se cambia la consigna", "Un arranque es un cambio de apagado a encendido, no una medición ni un cambio de consigna."),
        ("abc", "{F} Después de la 2.ª lectura (25 °C), ¿en qué estado queda el sistema?", "Encendido, porque 25 °C llega al margen superior", "Apagado, porque 25 °C es mayor que la consigna", "Apagado, porque aún no pasó una hora", "Con 25 °C se alcanza el margen superior y el sistema se enciende."),
        ("abc", "{F} Después de la 5.ª lectura (24 °C), ¿en qué estado queda el sistema?", "Encendido, porque 24 °C es intermedia y mantiene el estado anterior", "Apagado, porque 24 °C es igual a la consigna", "Apagado, porque bajó de 25 °C", "Una lectura intermedia mantiene el estado, que venía encendido."),
        ("abc", "{F} Después de la 6.ª lectura (23 °C), ¿en qué estado queda el sistema?", "Apagado, porque 23 °C llega al margen inferior", "Encendido, porque está cerca de la consigna", "Encendido, porque 23 °C es intermedia", "23 °C llega al margen inferior y el sistema se apaga."),
        ("=", "{F} Si el sistema estuvo apagado en 3 de las 8 lecturas, ¿en cuántas lecturas quedó encendido?", "8-3", "Se resta de las 8 lecturas las que dejaron el sistema apagado.", " lecturas"),
        ("=", "{F} Si cada lectura representa una hora con el estado que quedó y el sistema quedó apagado en 3 de las 8 lecturas, ¿cuántos kWh consume en las 8 horas?", "(8-3)*1", "Se multiplican las horas encendido por el consumo de 1 kW.", " kWh"),
        ("abc", "{F} ¿Cuántos arranques tiene el sistema durante las 8 lecturas?", "2 arranques: en la 2.ª y en la 8.ª lectura", "1 arranque: en la 2.ª lectura", "3 arranques: en la 2.ª, la 6.ª y la 8.ª lectura", "El sistema se enciende en la 2.ª lectura, se apaga en la 6.ª y se enciende de nuevo en la 8.ª."),
        ("abc", "{F} Un compañero dice que sin diferencial el sistema funcionaría mejor. ¿Qué respuesta es correcta?", "Sin diferencial se encendería y apagaría muy seguido, lo que desgasta los equipos", "Con diferencial el sistema nunca se apaga", "Sin diferencial el sistema consume menos siempre", "El diferencial evita cambios de estado continuos que desgastan los equipos."),
        ("abc", "{F} Si el diferencial fuera ±2 °C (encender en 26 °C o más y apagar en 22 °C o menos) con las mismas lecturas, ¿cuántas veces se encendería el sistema?", "1 vez, en la 3.ª lectura", "2 veces", "3 veces", "Solo la lectura de 26 °C alcanza el nuevo margen de encendido y nunca baja a 22 °C."),
        ("=", "{F} Si el patrón de consumo de 5 kWh por jornada se repitiera durante 30 jornadas con una tarifa de ejemplo de $150 por kWh, ¿cuánto costaría la energía?", "5*30*150", "Se multiplican los kWh por jornada, las jornadas y la tarifa.", " pesos"),
        ("abc", "{F} En la 7.ª hora el sensor entrega −40 °C, un valor imposible para el recinto. ¿Qué corresponde?", "Dudar de la lectura, registrarla e informar para que personal autorizado revise el sensor", "Apagar el sistema por completo sin avisar", "Tomar la lectura como válida y bajar la consigna", "Un valor imposible indica una falla del sensor, que se informa."),
    ],
    ctx=("abc", "Un cliente de ejemplo pide que el diferencial sea cero «para que mantenga justo 24 °C». ¿Qué responde el instalador?", "Que los ajustes los define el proyecto o el manual, y que sin diferencial el sistema arrancaría seguido y se desgastaría", "Que lo configura de inmediato porque el cliente manda", "Que lo configura cuando nadie mire", "El ajuste lo fija el proyecto o el fabricante; un diferencial nulo causa arranques continuos."),
    sc=[
        ("En Refrigeración: ¿qué hace un control con diferencial cuando la lectura es intermedia?", "Mantiene el estado anterior", "El margen evita cambios de estado continuos."),
        ("¿Qué es un arranque?", "El paso de apagado a encendido", "Muchos arranques seguidos desgastan los equipos y gastan energía."),
        ("¿Qué se hace con una lectura imposible?", "Se registra y se informa para revisar el sensor", "Indica una posible falla del sensor."),
    ],
    op=("Control de ejemplo para el «Salón Pehuén» (ficticio): consigna de 22 °C y diferencial de ±1 °C; enciende en 23 °C o más y apaga en 21 °C o menos; entre ambos mantiene el estado. Estado inicial apagado. Lecturas por hora: 22, 23, 24, 22, 21, 22. El sistema consume 2 kW encendido. "
        "Escribe (a) el estado tras cada lectura, (b) cuántas lecturas queda encendido, (c) los kWh consumidos, (d) cuántos arranques hay.",
        "(a) Apagado, encendido, encendido, encendido, apagado, apagado. (b) 3 lecturas. (c) 3 por 2 son 6 kWh. (d) 1 arranque, en la 2.ª lectura.",
        ["sigue correctamente la lógica", "cuenta las lecturas encendido", "calcula los kWh", "cuenta los arranques"],
        ["hoja con la tabla de estados y los cálculos"],
        ["apagar en una lectura intermedia", "contar mal los arranques", "olvidar multiplicar por los kW"],
        "Pregunta: «¿qué pasa con la lectura de 22 °C cuando el sistema estaba encendido?». Si no responde, pídele que relea la regla de lecturas intermedias."),
    reinforce="Inventa un control con consigna, diferencial y cinco lecturas, y escribe el estado del sistema después de cada una.",
    extend="Explica con un ejemplo por qué un diferencial demasiado pequeño aumenta el desgaste de un equipo.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Equipo A: precio $900.000 y consumo de ejemplo de 1.200 kWh al año. Equipo B: precio $1.100.000 y consumo de ejemplo de 800 kWh al año. Tarifa de ejemplo: $150 por kWh. Horizonte de evaluación: 10 años. "
     "Lista de verificación de la instalación (6 puntos): documentos entregados, ubicación según plano, soportes revisados, conexión eléctrica certificada por instalador autorizado, controles configurados según especificación y acta firmada. En la revisión se cumplieron 5 de 6; falta la certificación eléctrica.")
build(
    O5, 5, F,
    use="Aprenderé a comparar dos equipos por su costo total de propiedad y a verificar una instalación con una lista de verificación antes de firmar el acta.",
    prior=["Sé calcular kWh y costo de energía.", "Sé qué es una lista de control.", "Sé qué es un punto crítico."],
    explain=[
        "El costo total de propiedad suma el precio de compra y el costo de la energía durante los años que se evalúan. Un equipo más caro al comprar puede costar menos en total si consume menos. El horizonte de evaluación es el número de años que se consideran, y se fija antes de comparar. El costo anual de energía es el consumo en kWh multiplicado por la tarifa; en el horizonte se multiplica por los años. La mejor opción cumple la especificación y tiene el menor costo total.",
        "La verificación de la instalación se hace con una lista de puntos revisados uno por uno. Algunos son críticos: por ejemplo, la certificación de la conexión eléctrica, que un instalador autorizado entrega según la norma vigente de la entidad fiscalizadora. Si un punto crítico no se cumple, no se firma el acta de entrega ni se pone el equipo en servicio; se registra la no conformidad y se corrige. El porcentaje de cumplimiento no reemplaza ese requisito.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("costo total de propiedad", "precio de compra más el costo de la energía durante los años de uso"), ("horizonte de evaluación", "número de años que se consideran para comparar"), ("costo anual de energía", "consumo en kWh multiplicado por la tarifa"), ("certificación eléctrica", "documento de un instalador autorizado que acredita la conexión eléctrica"), ("poner en servicio", "dejar el equipo funcionando para el uso normal"), ("no conformidad", "incumplimiento de un requisito, que se registra para corregirlo")],
    worked=[
        ("Costo total", "Un equipo de ejemplo cuesta $500.000 y consume 400 kWh al año; la tarifa es $100 por kWh y el horizonte es 5 años. ¿Cuál es su costo total?", ["La energía cuesta 400 por 100 por 5, que son 200.000.", "500.000 más 200.000 son 700.000."], "$700.000"),
        ("Cumplimiento", "Una lista de ejemplo tiene 4 puntos y se cumplen 3. ¿Qué porcentaje es?", ["3 dividido por 4 es 0,75.", "Multiplicado por 100 es 75 %."], "75 %"),
    ],
    mistakes=[("Comparar solo el precio de compra y descartar el equipo que consume menos.", "Ignora el costo de la energía durante el uso.", "Compara el costo total en el horizonte de evaluación."),
              ("Firmar el acta con un punto crítico incumplido porque el porcentaje es alto.", "Un punto crítico puede afectar la seguridad.", "Corrige y verifica el punto antes de firmar.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es el costo total de propiedad de un equipo?", "El precio de compra más el costo de la energía durante los años de uso", "Solo el precio de compra del equipo", "El costo de transportar el equipo hasta la obra", "El costo total incluye compra y energía; el precio o el transporte por sí solos no bastan."),
        ("abc", "¿Qué es el horizonte de evaluación?", "El número de años que se consideran para comparar los equipos", "La fecha en que el equipo se instala", "La cantidad de equipos que se comparan", "El horizonte fija el período de comparación, no una fecha de instalación ni una cantidad."),
        ("abc", "¿Qué acredita la certificación de la conexión eléctrica de un equipo?", "Que un instalador autorizado verificó la conexión según la norma vigente", "Que el equipo es nuevo", "Que el equipo consume poca energía", "La certificación acredita la conexión eléctrica, no la antigüedad ni el consumo."),
        ("=", "{F} ¿Cuánto cuesta la energía de un año del equipo A?", "1200*150", "Se multiplica el consumo anual por la tarifa de cada kWh.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la energía de un año del equipo B?", "800*150", "Se multiplica el consumo anual por la tarifa de cada kWh.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de propiedad del equipo A en 10 años?", "900000+1200*150*10", "Se suma el precio de compra y la energía de 10 años.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de propiedad del equipo B en 10 años?", "1100000+800*150*10", "Se suma el precio de compra y la energía de 10 años.", " pesos"),
        ("=", "{F} ¿Cuánto menos cuesta el equipo B que el A en costo total a 10 años?", "(900000+1200*150*10)-(1100000+800*150*10)", "Se resta el costo total de B del costo total de A.", " pesos"),
        ("abc", "{F} Según el costo total a 10 años, ¿qué equipo conviene?", "El equipo B, porque su costo total es menor", "El equipo A, porque su precio de compra es menor", "Ambos, porque cuestan lo mismo", "B cuesta menos en total a pesar de su mayor precio de compra."),
        ("abc", "{F} Un compañero compara solo el precio de compra y elige el equipo A. ¿Cuál es su error?", "Ignora el costo de la energía durante 10 años, que hace más barato a B", "Ninguno, porque el precio de compra es lo único que cuenta", "No sumó el transporte del equipo", "El precio de compra es solo una parte del costo total de propiedad."),
        ("=", "{F} Con un horizonte de 5 años en vez de 10, ¿cuánto menos cuesta el equipo B que el A en costo total?", "(900000+1200*150*5)-(1100000+800*150*5)", "Se repite la comparación de costos totales con 5 años de energía.", " pesos"),
        ("=", "{F} Si la tarifa subiera a $200 por kWh, ¿cuál sería el costo total de B a 10 años?", "1100000+800*200*10", "Se suma el precio de compra y la energía a la nueva tarifa durante 10 años.", " pesos"),
        ("abc", "{F} En la revisión falta la certificación de la conexión eléctrica. ¿Qué corresponde?", "No firmar el acta ni poner el equipo en servicio hasta contar con la certificación", "Firmar el acta, porque se cumplieron 5 de 6 puntos", "Firmar y entregar la certificación después", "La certificación eléctrica es un punto crítico y debe cumplirse antes de firmar."),
    ],
    ctx=("abc", "El dueño de un local de ejemplo quiere poner en servicio el equipo hoy aunque falta la certificación de la conexión eléctrica. ¿Qué responde el instalador?", "Que no se pone en servicio sin la certificación de un instalador eléctrico autorizado", "Que lo pone en servicio si el dueño firma una carta", "Que lo pone en servicio y pide la certificación después", "Una carta del dueño no reemplaza una certificación exigida por la norma vigente."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el costo total de propiedad?", "Sumando el precio de compra y la energía de todos los años evaluados", "Un equipo caro puede costar menos si consume menos."),
        ("¿Cuándo se firma el acta de entrega?", "Cuando los puntos críticos están cumplidos", "Un porcentaje alto de cumplimiento no basta."),
        ("¿Quién certifica la conexión eléctrica?", "Un instalador eléctrico autorizado", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Alternativas de ejemplo para el «Taller Quila» (ficticio): equipo M a $600.000 con 500 kWh al año; equipo N a $750.000 con 300 kWh al año; tarifa de $120 por kWh; horizonte de 8 años. Lista de verificación de 5 puntos, 4 cumplidos; falta el acta firmada. "
        "Escribe (a) el costo total de M y de N, (b) cuál conviene, (c) el porcentaje de cumplimiento de la lista, (d) qué haces con el punto no cumplido.",
        "(a) M: 600.000 más 500 por 120 por 8, que son 480.000: total 1.080.000. N: 750.000 más 300 por 120 por 8, que son 288.000: total 1.038.000. (b) Conviene N, porque su costo total es menor. (c) 4 de 5 es 80 %. (d) El acta firmada se completa cuando se cumplan los puntos críticos; registro la no conformidad y no pongo el equipo en servicio hasta entonces.",
        ["calcula los costos totales", "elige con el costo total", "calcula el porcentaje", "registra la no conformidad"],
        ["hoja con los cálculos"],
        ["comparar solo el precio de compra", "olvidar los años de energía", "firmar con un punto pendiente"],
        "Pregunta: «¿por qué conviene N si es más caro?». Si no responde, pídele que relea el costo total de propiedad."),
    reinforce="Inventa dos equipos con precio y consumo anual, y calcula cuál cuesta menos en 5 años.",
    extend="Explica con un ejemplo por qué el horizonte de evaluación puede cambiar qué equipo conviene.",
)

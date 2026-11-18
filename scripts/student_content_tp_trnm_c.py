"""Tripulación de Naves Mercantes y Especiales TP 3.º y 4.º medio: OAE-05 (apoyo al gobierno de la nave como lectura, órdenes y registros) y OAE-06 (guardia segura: vigilancia, señales y planes de turnos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_trnm_common import AVISO, EMER, build

O5 = "TP-TRNM-3y4-OAE-05"
O6 = "TP-TRNM-3y4-OAE-06"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En el puente de la «Nave Demo» cada guardia dura 4 horas y la cumplen 1 oficial de guardia y 1 marinero de guardia. La nave puede gobernarse con piloto automático (equipo que mantiene un rumbo fijado) "
     "o con gobierno manual (una persona orienta el timón). Peligros anotados: fatiga, distracción, órdenes mal entendidas y poca visibilidad.")
build(
    O5, 1, F,
    use="Aprenderé qué es el gobierno de una nave, qué tareas de apoyo hay en el puente, quién da las órdenes y qué peligros tiene el trabajo en el puente.",
    prior=["Sé qué es el rumbo y qué es una guardia.", "Sé qué es la jerarquía de controles.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Gobernar una nave es dirigirla manteniendo o cambiando su rumbo. Se hace desde el puente. Hay dos modos: el piloto automático es un equipo que mantiene un rumbo fijado, y el gobierno manual es el que hace una persona orientando el timón. Las tareas de apoyo al gobierno son tareas simples que hace un marinero bajo las órdenes del oficial a cargo: leer datos, repetir las órdenes, vigilar y registrar. El paso de un modo a otro lo decide y lo ordena el oficial, y lo hace personal autorizado; este cuaderno no enseña esa maniobra.",
        "Las órdenes siguen una cadena de mando: las da el oficial y las recibe quien las cumple, que las repite para confirmar que las entendió. Los peligros del puente son la fatiga, la distracción, las órdenes mal entendidas y la poca visibilidad. Se previenen con la jerarquía de controles: alarmas automáticas que avisan cuando el rumbo se aleja (de ingeniería), descansos programados y reglas de comunicación (administrativos) y capacitación. Un ejemplo con otra nave: una alarma que suena sola cuando el rumbo se desvía no depende de que alguien lo note.",
        f"Un puesto de guardia es el lugar que ocupa una persona durante una guardia. {EMER} {AVISO}",
    ],
    vocab=[("gobernar", "dirigir una nave manteniendo o cambiando su rumbo"), ("piloto automático", "equipo que mantiene un rumbo fijado"), ("gobierno manual", "gobierno hecho por una persona que orienta el timón"), ("oficial de guardia", "oficial que está al mando durante una guardia"), ("cadena de mando", "orden en que se dan y reciben las órdenes"), ("puesto de guardia", "lugar que ocupa una persona durante una guardia"), ("fatiga", "cansancio que reduce la atención")],
    worked=[
        ("Identificar el modo", "En una nave de ejemplo un equipo mantiene un rumbo fijado sin que una persona oriente el timón. ¿Qué modo de gobierno es?", ["Un equipo que mantiene el rumbo es un piloto automático.", "No hay una persona orientando el timón."], "Piloto automático"),
        ("Clasificar un control", "Una nave de ejemplo instala una alarma que suena sola si el rumbo se aleja del fijado. ¿A qué nivel corresponde?", ["La alarma es un cambio del equipo y no depende de que alguien lo recuerde.", "Un cambio físico del sistema es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que cambiar el modo de gobierno lo puede hacer cualquier tripulante que sepa cómo.", "El paso de un modo a otro lo ordena el oficial y lo hace personal autorizado.", "Espera la orden del oficial y no cambies nada por cuenta propia."),
              ("Creer que repetir una orden es perder tiempo.", "Repetirla permite comprobar que se entendió y evita errores.", "Repite siempre la orden con las mismas palabras.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es el gobierno de una nave?", "Dirigirla manteniendo o cambiando su rumbo", "Cargar y descargar sus bodegas", "Mantener los equipos de máquinas", "Gobernar es dirigir el rumbo; las bodegas y las máquinas son otras tareas."),
        ("abc", "En Tripulación de Naves: ¿qué es un piloto automático?", "Un equipo que mantiene un rumbo fijado", "Un oficial que se encarga de la guardia de noche", "Un instrumento que mide la velocidad", "El piloto automático es un equipo y no una persona ni un instrumento de lectura."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las órdenes mal entendidas?", "Que se ejecute una acción distinta de la ordenada", "Que el oficial cambie de guardia", "Que el puente quede sin iluminación", "Una orden mal entendida lleva a una acción equivocada."),
        ("=", "{F} ¿Cuántas guardias de 4 horas hay en un día de 24 horas?", "24//4", "Se divide la duración del día entre la duración de la guardia.", " guardias"),
        ("=", "{F} ¿Cuántos puestos de guardia hay que cubrir en un día, con 2 personas por guardia?", "(24//4)*2", "Se multiplican las guardias del día por las personas de cada guardia.", " puestos"),
        ("abc", "{F} ¿Quién ordena pasar del piloto automático al gobierno manual?", "El oficial a cargo", "Cualquier tripulante del puente", "El tripulante que lleva más tiempo a bordo", "La orden la da el oficial a cargo, según la cadena de mando."),
        ("abc", "{F} Para el peligro de la fatiga, ¿cuál es un control administrativo?", "Programar descansos entre guardias", "Instalar una alarma de rumbo", "Entregar un chaleco a cada persona", "Los descansos programados son una regla de organización del trabajo."),
        ("abc", "{F} Una alarma que suena sola cuando el rumbo se aleja del fijado es un control de:", "Ingeniería, porque el equipo avisa sin depender de que alguien lo recuerde", "EPP, porque protege a quien la escucha", "Eliminación, porque quita la fatiga", "La alarma es una barrera técnica; no elimina la fatiga ni es EPP."),
        ("=", "{F} Si el marinero anota 6 lecturas de rumbo por hora, ¿cuántas lecturas anota en una guardia?", "6*4", "Se multiplican las lecturas por hora por las horas de la guardia.", " lecturas"),
        ("abc", "Durante una visita de ejemplo se anuncia por altavoz que una persona cayó al agua. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, dar la alarma y avisar a un adulto responsable y a emergencias", "Correr hacia la borda para ver dónde cayó", "Lanzarte al agua para ayudar", "Intervenir sin formación puede causar otro accidente; se da la alarma y se avisa."),
        ("abc", "{F} Un compañero dice que puede pasar el piloto automático a manual «para practicar» cuando el oficial no mira. ¿Qué respuesta es correcta?", "Es falso: el cambio lo ordena el oficial y lo hace personal autorizado", "Es cierto, si ya vio cómo se hace", "Es cierto, si lo anota en el registro después", "Practicar sin autorización pone en riesgo a la nave y a las personas."),
        ("=", "{F} Un marinero de ejemplo cumple una guardia de 4 horas y descansa 8 horas. ¿Cuántas guardias cumple en 24 horas?", "24//(4+8)", "Se divide el día entre lo que dura cada ciclo de guardia más descanso.", " guardias"),
        ("abc", "{F} Una persona nota que el oficial parece muy cansado y a punto de dormirse en el puente. ¿Qué corresponde?", "Avisar al capitán o a otro responsable, de forma respetuosa", "Callar para no molestar", "Tomar el timón por su cuenta", "La fatiga es un peligro; se avisa a un responsable y no se asume el gobierno."),
    ],
    ctx=("abc", "Un conocido que trabaja en un buque te propone dejarte «tomar el timón unos minutos» durante una visita. ¿Qué respondes?", "Que no, porque gobernar una nave exige instructor autorizado, norma vigente y elementos de protección, y que lo hablarás con un adulto responsable", "Que sí, si es solo unos minutos", "Que sí, si el mar está calmo", "La duración o el estado del mar no reemplazan la autorización ni la formación."),
    sc=[
        ("En Tripulación de Naves: ¿quién da las órdenes en el puente?", "El oficial a cargo", "Las órdenes siguen la cadena de mando."),
        ("¿Para qué se repite una orden?", "Para confirmar que se entendió", "Repetir permite detectar errores antes de actuar."),
        ("¿Qué modo de gobierno mantiene un rumbo fijado?", "El piloto automático", "El piloto automático mantiene un rumbo fijado."),
    ],
    op=("En el puente de la «Nave Ejemplo» (caso de ejemplo) el marinero de guardia lleva 7 horas sin descansar, hay poca visibilidad y las órdenes llegan por un intercomunicador con ruido. Escribe (a) los tres peligros, (b) el riesgo de cada uno, (c) un control administrativo y uno de ingeniería, (d) qué hace el marinero si no entiende una orden.",
        "(a) La fatiga, la poca visibilidad y el ruido del intercomunicador. (b) Que se pierda la atención; que no se vea otro objeto a tiempo; que una orden se entienda mal. (c) Administrativo: descansos programados; de ingeniería: un intercomunicador sin ruido o una alarma de rumbo. (d) Pide que la repitan y la repite él para confirmar, sin adivinar.",
        ["identifica los tres peligros", "señala el riesgo de cada uno", "propone un control administrativo y uno de ingeniería", "indica que pide repetir la orden"],
        ["hoja con las cuatro respuestas"],
        ["confundir peligro con riesgo", "proponer solo EPP", "decir que el marinero adivina la orden"],
        "Pregunta: «¿qué puede pasar si la orden se entiende mal?». Si no responde, pídele que relea la segunda parte de la explicación."),
    reinforce="Escribe tres peligros del puente y un control para cada uno.",
    extend="Explica con un ejemplo por qué repetir una orden ayuda a prevenir errores en el puente.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (órdenes y registro de ejemplo). Orden 1 del oficial: «Rumbo uno ocho cero» (180°). El marinero repite: «Rumbo uno ocho cero». Orden 2: «Timón diez grados a estribor». "
     "Registro de la bitácora a las 03:10: rumbo ordenado 180°, rumbo real 184°.")
build(
    O5, 2, F,
    use="Aprenderé el lenguaje técnico de las órdenes de gobierno, qué es el desvío de rumbo y qué se registra en la bitácora.",
    prior=["Sé qué es el rumbo y cómo se mide.", "Sé qué es la cadena de mando.", "Sé restar números enteros."],
    explain=[
        "El rumbo ordenado es el que indica el oficial y el rumbo real es el que la nave lleva según el compás. El desvío es la diferencia entre ambos: si el rumbo real es mayor que el ordenado, la proa se desvió hacia estribor, y si es menor, hacia babor. Los números de un rumbo se dicen de uno en uno, como «uno ocho cero», para evitar confusiones. Una orden de rumbo se repite igual para confirmarla. El timón es la pieza que orienta la nave, y su ángulo se dice en grados hacia babor (el lado izquierdo mirando hacia la proa) o hacia estribor (el lado derecho).",
        "La bitácora es el libro donde se anotan, con hora y firma, los hechos y datos de la navegación, como rumbos, lecturas y órdenes recibidas. Una anotación completa tiene hora, rumbo ordenado, rumbo real, desvío y firma de quien anota. Un ejemplo con otra nave: rumbo ordenado 270°, real 266°, desvío de 4°. Este cuaderno enseña a leer y registrar las órdenes; no enseña a mover el timón.",
        f"Si no se entiende una orden, se pide que se repita; nunca se adivina. {EMER} {AVISO}",
    ],
    vocab=[("rumbo ordenado", "rumbo que indica el oficial"), ("rumbo real", "rumbo que la nave lleva según el compás"), ("desvío", "diferencia entre el rumbo real y el ordenado"), ("timón", "pieza que orienta la nave"), ("babor", "lado izquierdo de la nave mirando hacia la proa"), ("estribor", "lado derecho de la nave mirando hacia la proa"), ("bitácora", "libro donde se anotan con hora y firma los hechos de la navegación")],
    worked=[
        ("Calcular un desvío", "Rumbo ordenado 270°; rumbo real 266°. ¿Cuál es el desvío?", ["El desvío es la diferencia entre los dos rumbos.", "Se resta 270 − 266."], "4°"),
        ("Leer un lado", "Una orden de ejemplo dice «timón cinco grados a babor». ¿Hacia qué lado se orienta el timón?", ["Babor es el lado izquierdo de la nave mirando hacia la proa.", "El ángulo es de cinco grados."], "Cinco grados hacia el lado izquierdo (babor)"),
    ],
    mistakes=[("Decir los números del rumbo seguidos, como «ciento ochenta», sin separarlos.", "Se pueden confundir con otros números; se dicen de uno en uno.", "Di «uno ocho cero»."),
              ("Adivinar una orden que no se entendió.", "Una orden adivinada puede ser distinta de la ordenada.", "Pide que se repita.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es el desvío de rumbo?", "La diferencia entre el rumbo real y el rumbo ordenado", "El ángulo del timón en grados", "La velocidad de la nave en nudos", "El desvío compara el rumbo real con el ordenado; el ángulo del timón y la velocidad son otros datos."),
        ("abc", "En Tripulación de Naves: ¿qué lado de la nave es estribor?", "El lado derecho mirando hacia la proa", "El lado izquierdo mirando hacia la proa", "La parte de atrás de la nave", "Estribor es el lado derecho; el izquierdo es babor."),
        ("abc", "En Tripulación de Naves: ¿para qué se repite una orden de rumbo?", "Para confirmar que se entendió igual que como se dio", "Para que el oficial no tenga que dar más órdenes", "Para anotarla dos veces en la bitácora", "Repetir permite comprobar que se entendió."),
        ("=", "{F} ¿Cuántos grados de desvío hay en el registro de las 03:10?", "184-180", "Se resta el rumbo ordenado al rumbo real.", "°"),
        ("abc", "{F} ¿Qué dice la orden 2 de la ficha?", "Orientar el timón diez grados hacia el lado derecho", "Orientar el timón diez grados hacia el lado izquierdo", "Mantener el timón en el centro", "Estribor es el lado derecho: la orden indica 10° hacia ese lado."),
        ("abc", "{F} ¿Qué datos debe tener una anotación completa del registro de las 03:10?", "Hora, rumbo ordenado, rumbo real, desvío y firma", "Solo el rumbo real", "Solo la firma", "Una anotación completa tiene los cinco datos para que sea útil."),
        ("abc", "{F} ¿Cómo se dice el rumbo 270° al repetir una orden?", "«Dos siete cero»", "«Doscientos setenta»", "«Veintisiete cero»", "Los rumbos se dicen cifra por cifra para evitar confusiones."),
        ("=", "{F} Si el rumbo ordenado es 180° y el real es 176°, ¿cuántos grados de desvío hay?", "180-176", "Se resta el rumbo menor al mayor para hallar la diferencia.", "°"),
        ("abc", "{F} Con el rumbo ordenado de 180° y el real de 176°, ¿hacia qué lado se desvió la proa?", "Hacia babor, porque el rumbo real es menor que el ordenado", "Hacia estribor, porque el rumbo real es menor que el ordenado", "No se desvió, porque la diferencia es pequeña", "Un rumbo menor indica que la proa se desvió hacia el lado izquierdo, es decir, a babor."),
        ("abc", "{F} Un marinero no entiende bien una orden de rumbo. ¿Qué corresponde?", "Pedir que la repitan y repetirla él para confirmar", "Adivinar el rumbo más probable", "Esperar la siguiente orden sin hacer nada", "Una orden dudosa se aclara; adivinar es peligroso."),
        ("abc", "{F} Un compañero dice: «da lo mismo decir 'ciento ochenta' que 'uno ocho cero'». ¿Qué respuesta es correcta?", "No da lo mismo: decirlo cifra por cifra reduce los errores", "Sí da lo mismo, porque son el mismo número", "Sí da lo mismo, si se escribe en la bitácora", "Dicho cifra por cifra, el rumbo se confunde menos con otras palabras."),
        ("=", "{F} Si el desvío crece 2° cada 10 minutos desde las 03:10, ¿cuántos grados de desvío habrá a las 03:40?", "(184-180)+2*3", "Se suma el crecimiento de tres intervalos de 10 minutos al desvío de las 03:10.", "°"),
        ("abc", "{F} Si el desvío llega a 10°, ¿qué se informa al oficial?", "La hora, el rumbo ordenado, el rumbo real y el desvío", "Solo que el rumbo cambió", "Nada, porque el piloto automático lo corrige", "Un informe completo da los cuatro datos para decidir."),
    ],
    ctx=("abc", "Un compañero de ejemplo te dice: «en la bitácora anota el rumbo ordenado como real, así no hay desvío». ¿Qué respondes?", "Que se anota lo que marca el compás y se informa el desvío", "Que sí, porque se ve más prolijo", "Que sí, pero solo si el desvío es pequeño", "Alterar la bitácora oculta información y puede ocultar un problema."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el desvío?", "Diferencia entre el rumbo real y el ordenado", "El desvío mide cuánto se alejó la nave del rumbo ordenado."),
        ("¿Qué lado es babor?", "El izquierdo mirando hacia la proa", "Babor es el lado izquierdo mirando hacia la proa."),
        ("¿Qué es la bitácora?", "El libro donde se anotan los hechos de la navegación", "La bitácora registra con hora y firma lo que ocurre."),
    ],
    op=("Registro de ejemplo de la «Nave Ejemplo» a las 05:20: rumbo ordenado 045°; rumbo real 051°. Orden del oficial: «Timón cinco grados a babor». Escribe (a) cómo se dice el rumbo ordenado al repetir la orden, (b) el desvío y hacia qué lado se fue la proa, (c) qué dice la orden del timón, (d) qué datos tiene la anotación completa de la bitácora.",
        "(a) «Cero cuatro cinco». (b) 051 − 045 = 6°; la proa se fue hacia estribor, porque el rumbo real es mayor que el ordenado. (c) Orientar el timón cinco grados hacia el lado izquierdo (babor). (d) Hora, rumbo ordenado, rumbo real, desvío y firma.",
        ["dice el rumbo cifra por cifra", "calcula el desvío y su lado", "interpreta la orden", "indica los datos de la anotación"],
        ["hoja con las cuatro respuestas"],
        ["decir el rumbo como un solo número", "confundir babor con estribor", "olvidar la firma"],
        "Pregunta: «¿qué rumbo es mayor, el real o el ordenado?». Si no responde, pídele que repase el último ejemplo resuelto."),
    reinforce="Escribe tres órdenes de rumbo de ejemplo y di cada rumbo cifra por cifra.",
    extend="Explica por qué la bitácora debe llevar hora y firma en cada anotación.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (registro de rumbos de ejemplo). Rumbo ordenado: 090°. Registro cada 10 minutos: 00:00, rumbo real 090°; 00:10, 092°; 00:20, 095°; 00:30, 091°. "
     "Regla de la planilla de ejemplo: se informa al oficial todo desvío mayor que 3°.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un registro de rumbos, a detectar los desvíos que se deben informar y a redactar el informe al oficial.",
    prior=["Sé calcular un desvío.", "Sé qué es la bitácora.", "Sé sumar y dividir números enteros."],
    explain=[
        "Un registro de rumbos anota el rumbo real a intervalos de tiempo. Con el rumbo ordenado se calcula el desvío de cada lectura. La planilla puede fijar una regla de aviso: por ejemplo, informar todo desvío mayor que cierto número de grados. Una lectura se informa si su desvío supera ese número; si es igual o menor, solo se registra. Cuando el rumbo real es mayor que el ordenado, la proa se desvió hacia estribor; cuando es menor, hacia babor.",
        "Para analizar un registro también se miran la tendencia y el promedio. El promedio de los desvíos es la suma de los desvíos dividida entre el número de lecturas. Un promedio bajo no oculta un desvío alto puntual: cada lectura que supera la regla se informa por separado. Un ejemplo con otro registro: desvíos de 1°, 4° y 1° suman 6° y su promedio es 2°, pero la lectura de 4° se informa si la regla es 3°.",
        f"El marinero informa y registra; el oficial decide si se corrige y cómo. {EMER} {AVISO}",
    ],
    vocab=[("registro de rumbos", "anotación del rumbo real a intervalos de tiempo"), ("regla de aviso", "valor sobre el cual se informa un desvío"), ("promedio", "suma de valores dividida entre el número de valores"), ("lectura puntual", "una lectura aislada dentro de un registro"), ("informe al oficial", "comunicación que da los datos necesarios para decidir")],
    worked=[
        ("Aplicar la regla", "Rumbo ordenado 100°; lecturas 102°, 106° y 101°; se informa todo desvío mayor que 4°. ¿Qué lectura se informa?", ["Los desvíos son 2°, 6° y 1°.", "Solo 6° supera 4°."], "La lectura de 106°"),
        ("Calcular un promedio", "Los desvíos de ejemplo son 2°, 6° y 1°. ¿Cuál es el promedio?", ["Se suman los desvíos: 2 + 6 + 1 = 9.", "Se divide 9 entre las 3 lecturas."], "3°"),
    ],
    mistakes=[("Creer que si el promedio es bajo no hay que informar un desvío alto.", "Cada lectura que supera la regla se informa por separado.", "Compara cada lectura con la regla de aviso."),
              ("Informar solo el rumbo real sin el ordenado ni el desvío.", "El oficial necesita los tres datos para decidir.", "Informa hora, rumbo ordenado, rumbo real y desvío.")],
    T=[
        ("=", "{F} ¿Cuántos grados de desvío hay a las 00:10?", "92-90", "Se resta el rumbo ordenado al rumbo real.", "°"),
        ("=", "{F} ¿Cuántos grados de desvío hay a las 00:20?", "95-90", "Se resta el rumbo ordenado al rumbo real.", "°"),
        ("abc", "{F} ¿Qué lectura debe informarse según la regla de la planilla?", "La de las 00:20, porque su desvío de 5° supera 3°", "La de las 00:10, porque su desvío es de 2°", "Ninguna, porque todas están cerca del rumbo", "Solo el desvío de las 00:20 es mayor que 3°."),
        ("=", "{F} ¿Cuántos grados suman los desvíos de las cuatro lecturas?", "0+2+5+1", "Se suman los desvíos de las 00:00, 00:10, 00:20 y 00:30.", "°"),
        ("=", "{F} ¿Cuál es el promedio de los desvíos de las cuatro lecturas?", "(0+2+5+1)//4", "Se divide la suma de los desvíos entre las 4 lecturas.", "°"),
        ("abc", "{F} A las 00:20 el rumbo real es 95° y el ordenado, 90°. ¿Hacia qué lado se desvió la proa?", "Hacia estribor, porque el rumbo real es mayor que el ordenado", "Hacia babor, porque el rumbo real es mayor que el ordenado", "No se desvió, porque el desvío no supera 10°", "Un rumbo mayor que el ordenado indica un giro hacia el lado derecho, estribor."),
        ("=", "{F} ¿Cuántos grados sobre la regla de aviso estaba el desvío de las 00:20?", "(95-90)-3", "Se resta la regla de aviso al desvío de las 00:20.", "°"),
        ("abc", "{F} ¿Cuál es el informe correcto para la lectura de las 00:20?", "«A las 00:20, rumbo ordenado 090°, rumbo real 095°, desvío de 5° a estribor»", "«A las 00:20 el rumbo estaba bien»", "«A las 00:20, 095°»", "El informe completo da hora, rumbo ordenado, real, desvío y lado."),
        ("=", "{F} ¿Cuántas lecturas de rumbo se registran en una hora, si se anota una cada 10 minutos?", "60//10", "Se divide la hora entre el intervalo de registro.", " lecturas"),
        ("abc", "{F} A las 00:30 el desvío bajó a 1°. ¿Qué se informa respecto de las 00:20?", "Que a las 00:20 hubo un desvío de 5° y a las 00:30 bajó a 1°", "Nada, porque ya se corrigió", "Solo el desvío de las 00:30", "El desvío de las 00:20 se informa aunque después baje."),
        ("abc", "{F} Un compañero dice que no hace falta informar el desvío de las 00:20 porque el promedio es 2°. ¿Qué respuesta es correcta?", "Es falso: cada lectura sobre la regla se informa por separado", "Es cierto, porque el promedio es menor que 3°", "Es cierto, si el piloto automático lo corrigió", "Un promedio bajo no oculta un desvío puntual mayor que la regla."),
        ("=", "{F} Si el desvío siguiera creciendo 3° cada 10 minutos desde las 00:20, ¿cuántos grados habría a las 00:50?", "(95-90)+3*3", "Se suma el crecimiento de tres intervalos al desvío de las 00:20.", "°"),
        ("abc", "{F} ¿Quién decide si se corrige el rumbo tras informar el desvío?", "El oficial a cargo", "El marinero que registró la lectura", "El primero que lo note", "El marinero informa y el oficial decide."),
    ],
    ctx=("abc", "A las 00:20 una persona de ejemplo te dice: «no anotes el 95°, anota 92° para que no te reten». ¿Qué respondes?", "Que se anota el valor leído e informas el desvío", "Que sí, para evitar problemas", "Que anotas 92° y avisas después", "Alterar el registro oculta un desvío que el oficial debe conocer."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el promedio de los desvíos?", "Suma de los desvíos dividida entre el número de lecturas", "El promedio resume varias lecturas en un valor."),
        ("¿Cuándo se informa un desvío?", "Cuando supera la regla de aviso", "La regla fija desde qué valor se informa."),
        ("¿Quién decide la corrección del rumbo?", "El oficial a cargo", "El marinero informa y no decide."),
    ],
    op=("Registro de ejemplo: rumbo ordenado 270°. Lecturas cada 10 minutos: 02:00, 271°; 02:10, 275°; 02:20, 273°; 02:30, 273°. Regla de aviso de ejemplo: se informa todo desvío mayor que 3°. Escribe (a) el desvío de cada lectura, (b) qué lecturas se informan, (c) el promedio de los desvíos (ignora si es hacia babor o estribor), (d) el informe de la lectura más grave.",
        "(a) 1°, 5°, 3°, 3°. (b) La de las 02:10, porque 5° supera 3°; las de las 02:20 y 02:30 tienen 3°, que no supera la regla. (c) (1 + 5 + 3 + 3) ÷ 4 = 3°. (d) «A las 02:10, rumbo ordenado 270°, rumbo real 275°, desvío de 5° a estribor».",
        ["calcula los desvíos", "aplica la regla de aviso", "calcula el promedio", "redacta el informe"],
        ["hoja con las cuatro respuestas"],
        ["no aplicar la regla a cada lectura", "informar solo el rumbo real", "olvidar el lado del desvío"],
        "Pregunta: «¿cuántos grados supera cada desvío la regla de aviso?». Si no responde, pídele que los compare uno a uno."),
    reinforce="Inventa un registro de cuatro rumbos y marca cuáles se informarían con una regla de 2°.",
    extend="Explica por qué un promedio bajo no basta para decidir si hay que informar.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (datos de ejemplo). La «Nave Demo» navega a 12 nudos y a las 06:00 está a 60 millas náuticas de un punto de ejemplo. Un nudo es una milla náutica por hora, y la milla náutica es la unidad de distancia en el mar.")
build(
    O5, 4, F,
    use="Aprenderé a calcular en papel distancia, tiempo y velocidad con datos de ejemplo, y a informar una hora estimada de llegada.",
    prior=["Sé qué es un nudo y una milla náutica.", "Sé multiplicar y dividir números enteros.", "Sé leer una hora en formato de 24 horas."],
    explain=[
        "Con tres datos se calculan los otros: distancia = velocidad × tiempo; tiempo = distancia ÷ velocidad; velocidad = distancia ÷ tiempo. Si la velocidad está en nudos y el tiempo en horas, la distancia queda en millas náuticas. La hora estimada de llegada es la hora actual más el tiempo que falta. Es una estimación porque supone que la velocidad se mantiene igual.",
        "Un ejemplo con otros valores: a 10 nudos, una nave tarda 3 horas en recorrer 30 millas; si sale a las 08:00, llega a las 11:00. Para pasar horas a minutos se multiplica por 60: 2 horas son 120 minutos. En el puente, estos cálculos se hacen en papel para informar al oficial; la decisión sobre la velocidad y el rumbo es del oficial, y este cuaderno no enseña a manejar los equipos del puente.",
        f"Todo valor de esta clase es de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("distancia", "longitud del recorrido, en millas náuticas en el mar"), ("velocidad", "distancia recorrida en una hora, en nudos"), ("tiempo", "duración del recorrido, en horas o minutos"), ("hora estimada de llegada", "hora actual más el tiempo que falta, suponiendo velocidad constante"), ("estimación", "cálculo aproximado basado en un supuesto")],
    worked=[
        ("Calcular el tiempo", "Una nave de ejemplo debe recorrer 36 millas a 9 nudos. ¿Cuánto tarda?", ["Tiempo = distancia ÷ velocidad.", "36 ÷ 9."], "4 horas"),
        ("Hora de llegada", "Esa nave de ejemplo sale a las 07:00. ¿A qué hora llega?", ["El tiempo de viaje es de 4 horas.", "Se suman 4 horas a las 07:00."], "A las 11:00"),
    ],
    mistakes=[("Dividir la velocidad entre la distancia para hallar el tiempo.", "El tiempo se obtiene dividiendo la distancia entre la velocidad.", "Escribe la fórmula antes de calcular."),
              ("Presentar la hora de llegada como una hora segura.", "Si la velocidad cambia, la hora cambia.", "Informa que es una estimación.")],
    T=[
        ("=", "{F} ¿Cuántas horas tarda la nave en llegar al punto de ejemplo a la velocidad indicada?", "60//12", "Se divide la distancia entre la velocidad.", " horas"),
        ("abc", "{F} ¿Cuál es la hora estimada de llegada si la velocidad se mantiene?", "11:00", "10:00", "12:00", "Salen a las 06:00 con 5 horas de viaje: se llega a las 11:00."),
        ("=", "{F} ¿Cuántas millas náuticas recorre la nave en 2 horas?", "12*2", "Se multiplica la velocidad por el tiempo.", " millas"),
        ("=", "{F} ¿Cuántas millas faltan a las 08:00?", "60-12*2", "Se restan las millas recorridas en 2 horas a la distancia inicial.", " millas"),
        ("abc", "{F} Si la velocidad bajara a 10 nudos, ¿cuál sería la hora estimada de llegada?", "12:00", "11:00", "10:00", "A 10 nudos se tardan 6 horas, y 6 horas después de las 06:00 son las 12:00."),
        ("=", "{F} ¿Cuántas horas tardaría a 10 nudos?", "60//10", "Se divide la distancia entre la nueva velocidad.", " horas"),
        ("=", "{F} A 12 nudos, ¿cuántos minutos tarda la nave en recorrer 6 millas?", "6*60//12", "Se calcula la fracción de hora y se pasa a minutos multiplicando por 60.", " minutos"),
        ("=", "{F} Si la nave recorrió 45 millas en 3 horas, ¿cuál fue su velocidad media?", "45//3", "Se divide la distancia entre el tiempo.", " nudos"),
        ("abc", "{F} El oficial pide la hora estimada de llegada. ¿Cómo la informas?", "«Hora estimada de llegada 11:00, si se mantiene la velocidad de 12 nudos»", "«Llegamos a las 11:00 sin falta»", "«Llegamos cuando lleguemos»", "Se informa la hora con el supuesto en que se basa."),
        ("abc", "{F} Un compañero calcula el tiempo dividiendo 12 entre 60 y obtiene 0 horas con resto 12. ¿Cuál es el error?", "Dividió la velocidad entre la distancia en vez de la distancia entre la velocidad", "Debió multiplicar las dos cantidades", "No hay error, porque la división es la misma", "El tiempo es la distancia dividida entre la velocidad, no al revés."),
        ("abc", "{F} Un compañero propone anotar 10:00 como hora de llegada «para que se vea mejor» aunque el cálculo da 11:00. ¿Qué corresponde?", "Informar la hora calculada y no cambiarla", "Anotar 10:00 si el oficial lo pide", "Anotar 10:30 como promedio", "Un cálculo no se altera para que parezca mejor."),
        ("=", "{F} Si la nave navega 4 horas a 12 nudos, ¿cuántas millas faltan para el punto de ejemplo?", "60-12*4", "Se restan las millas recorridas a la distancia inicial.", " millas"),
        ("abc", "{F} ¿Por qué la hora estimada de llegada es una estimación?", "Porque supone que la velocidad se mantiene igual, y puede cambiar", "Porque el reloj de la nave no es exacto", "Porque la distancia nunca se conoce", "La estimación depende de un supuesto: velocidad constante."),
    ],
    ctx=("abc", "El oficial de ejemplo te pide la hora estimada de llegada y no estás seguro de tu cálculo. ¿Qué haces?", "Revisar la operación con calma y, si la duda sigue, decirle al oficial que lo vuelves a calcular", "Dar una hora al azar para responder rápido", "Decirle la hora del compañero sin revisarla", "Un dato dudoso se revisa; una hora al azar puede llevar a una mala decisión."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el tiempo de viaje?", "Distancia dividida entre velocidad", "El tiempo es distancia ÷ velocidad."),
        ("¿Qué es un nudo?", "Una milla náutica por hora", "El nudo mide velocidad en el mar."),
        ("¿Por qué la hora de llegada es una estimación?", "Porque supone velocidad constante", "Si la velocidad cambia, la hora cambia."),
    ],
    op=("Datos de ejemplo: una nave navega a 15 nudos y debe recorrer 90 millas náuticas; sale a las 09:00. Escribe (a) cuántas horas tarda, (b) a qué hora llega, (c) cuántas millas habrá recorrido a las 12:00, (d) cómo informarías la hora estimada de llegada al oficial.",
        "(a) 90 ÷ 15 = 6 horas. (b) 09:00 + 6 horas = 15:00. (c) A las 12:00 habrán pasado 3 horas: 15 × 3 = 45 millas. (d) «Hora estimada de llegada 15:00, si se mantiene la velocidad de 15 nudos».",
        ["calcula el tiempo", "calcula la hora de llegada", "calcula las millas recorridas", "informa con el supuesto"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar sumar a la hora de salida", "presentar la hora como segura"],
        "Pregunta: «¿qué operación da el tiempo?». Si no responde, pídele que relea la primera parte de la explicación."),
    reinforce="Inventa tres pares de distancia y velocidad y calcula cuánto tarda cada recorrido.",
    extend="Explica qué cambia en la hora estimada de llegada si la velocidad baja a la mitad.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Nave Demo» mantiene dos guardias en paralelo: una en el puente, con 2 personas, y una en la cámara de máquinas, con 2 personas. Cada guardia dura 4 horas. "
     "Peligros anotados: fatiga, distracción, ruido que impide oír las alarmas, poca visibilidad y comunicaciones internas confusas.")
build(
    O6, 1, F,
    use="Aprenderé qué es una guardia segura, qué se vigila en el puente y en la cámara de máquinas, y cómo se usan las comunicaciones internas y las alarmas.",
    prior=["Sé qué es una guardia y un puesto de guardia.", "Sé qué es la cadena de mando.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Una guardia segura es un turno de vigilancia en que se observa y se escucha de forma continua. En el puente se vigilan las señales acústicas (sirenas, campanas y silbatos), las luces y los objetos que aparecen en el mar. En la cámara de máquinas, que es la sala de los motores y equipos, se vigilan los procesos, es decir, las lecturas y el funcionamiento de los equipos. Lo que se detecta se informa de inmediato al oficial de guardia.",
        "Las comunicaciones internas son los medios para hablar dentro de la nave, como teléfonos e intercomunicadores. Una alarma es un aviso sonoro o luminoso que indica un peligro o un valor fuera de límite. Al cambiar de guardia, quien entrega informa a quien recibe las novedades, las lecturas y lo pendiente: eso es el relevo. Un ejemplo con otra nave: si el ruido impide oír la alarma, se agrega una luz que también avise, que es un control de ingeniería.",
        f"La fatiga baja la atención: los descansos son parte de la seguridad. {EMER} {AVISO}",
    ],
    vocab=[("guardia segura", "turno de vigilancia continua con descanso suficiente"), ("vigilar", "observar y escuchar de forma continua"), ("señal acústica", "sonido que comunica o avisa, como una sirena o una campana"), ("cámara de máquinas", "sala donde están los motores y los equipos"), ("comunicaciones internas", "medios para hablar dentro de la nave"), ("alarma", "aviso sonoro o luminoso de un peligro"), ("relevo", "traspaso de la guardia con las novedades y lo pendiente")],
    worked=[
        ("Vigilar por vista y oído", "Durante una guardia de ejemplo se oye una sirena lejana. ¿Qué tipo de señal es y qué se hace?", ["La sirena es una señal acústica.", "Se informa de inmediato al oficial de guardia."], "Señal acústica; se informa de inmediato al oficial"),
        ("Contar puestos", "Una nave de ejemplo tiene 3 guardias de 4 horas con 2 personas cada una. ¿Cuántos puestos de guardia hay?", ["Cada guardia tiene 2 puestos.", "Se multiplican 3 guardias por 2 personas."], "6 puestos"),
    ],
    mistakes=[("Creer que si no se ve nada raro no hace falta prestar atención.", "La vigilancia es continua; un peligro puede aparecer sin aviso.", "Mantén la atención durante toda la guardia."),
              ("Entregar la guardia sin informar las novedades.", "El relevo exige que quien recibe sepa lo pendiente.", "Informa novedades, lecturas y pendientes al relevar.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es vigilar durante una guardia?", "Observar y escuchar de forma continua", "Revisar los equipos solo al comenzar la guardia", "Esperar a que suene la alarma", "Vigilar es continuo; no se limita al inicio ni espera la alarma."),
        ("abc", "En Tripulación de Naves: ¿qué es una alarma?", "Un aviso sonoro o luminoso de un peligro", "Un libro donde se anotan las lecturas", "Un tipo de rumbo", "La alarma avisa un peligro; el libro y el rumbo son otras cosas."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al ruido que impide oír las alarmas?", "Que una alarma no sea escuchada a tiempo", "Que el motor consuma más", "Que el puente se vea más oscuro", "El riesgo es no oír el aviso a tiempo."),
        ("=", "{F} ¿Cuántos puestos de guardia hay en cada período de 4 horas, sumando el puente y la cámara de máquinas?", "2+2", "Se suman las personas de las dos guardias.", " puestos"),
        ("abc", "{F} Para el ruido que impide oír alarmas, ¿cuál es un control de ingeniería?", "Agregar una luz que avise junto con el sonido", "Poner un letrero que diga «preste atención»", "Entregar tapones para los oídos", "La luz agrega una señal sin depender de que alguien oiga."),
        ("abc", "{F} Una persona detecta una luz que no esperaba durante la guardia. ¿Qué corresponde?", "Informar de inmediato al oficial de guardia con lo que vio", "Esperar a ver si la luz se repite", "Anotarlo para el final de la guardia", "Lo detectado se informa de inmediato; esperar puede ser tarde."),
        ("=", "{F} ¿Cuántos puestos de guardia hay que cubrir en un día, sumando el puente y la cámara de máquinas?", "(24//4)*(2+2)", "Se calculan las guardias del día y se multiplican por los puestos de cada período.", " puestos"),
        ("=", "{F} Si cada persona de un período cumple 4 horas de guardia, ¿cuántas horas de guardia suman las 4 personas?", "4*4", "Se multiplican las personas por las horas de la guardia.", " horas"),
        ("abc", "En la cámara de máquinas de ejemplo suena una alarma de incendio. ¿Qué corresponde a una persona en formación según las reglas generales?", "No acercarte a la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarte para buscar el origen del fuego", "Esperar a que suene una segunda vez", "Un incendio exige formación y equipo; se da la alarma y se avisa."),
        ("abc", "{F} Un compañero dice que si todo parece normal no hace falta mirar el horizonte. ¿Qué respuesta es correcta?", "Es falso: la vigilancia es continua", "Es cierto, si el equipo tiene alarmas", "Es cierto, si hay otra persona", "Un peligro puede aparecer sin aviso; las alarmas no reemplazan la vigilancia."),
        ("abc", "{F} ¿Qué debe informar quien entrega la guardia a quien la recibe?", "Las novedades, las lecturas y lo pendiente", "Solo la hora del cambio", "Solo quién estuvo de guardia", "El relevo traspasa lo necesario para continuar con seguridad."),
        ("=", "{F} Si en cada cambio de guardia el relevo dura 10 minutos, ¿cuántos minutos de relevo hay en un día?", "(24//4)*10", "Se multiplican los cambios de guardia del día por los minutos de cada relevo.", " minutos"),
        ("abc", "{F} Una persona de la guardia siente mucho sueño y le cuesta mantenerse atenta. ¿Qué corresponde?", "Avisar al oficial de guardia para que se tome una decisión", "Seguir sola y no decir nada", "Dormir un momento sin avisar", "La fatiga es un peligro; se informa a quien está al mando."),
    ],
    ctx=("abc", "Un conocido te invita a pasar una noche en el puente de una nave para «hacer la guardia con él» como práctica. ¿Qué respondes?", "Que no, porque hacer guardia exige instructor autorizado, norma vigente y elementos de protección, y que lo hablarás con un adulto responsable", "Que sí, si él te enseña", "Que sí, si es una noche tranquila", "Una guardia es una responsabilidad que exige autorización y formación."),
    sc=[
        ("En Tripulación de Naves: ¿qué es una señal acústica?", "Un sonido que comunica o avisa", "Una sirena o una campana son señales acústicas."),
        ("¿Qué es un relevo?", "El traspaso de la guardia con las novedades y lo pendiente", "El relevo asegura que quien recibe esté informado."),
        ("¿Qué se hace al detectar algo en la guardia?", "Se informa de inmediato al oficial", "El oficial decide qué hacer con lo informado."),
    ],
    op=("En la cámara de máquinas de la «Nave Ejemplo» (caso de ejemplo) el ruido es alto, la alarma de nivel de un tanque es solo sonora y el relevo se hace en solo un minuto sin informar lecturas. Escribe (a) los tres peligros, (b) el riesgo de cada uno, (c) un control de ingeniería y uno administrativo, (d) qué debería informar quien entrega la guardia.",
        "(a) El ruido alto, la alarma solo sonora y el relevo sin información. (b) No oír una alarma; no enterarse de un nivel fuera de límite; que quien recibe ignore lo pendiente. (c) Ingeniería: agregar una luz a la alarma; administrativo: un relevo con una lista de novedades. (d) Las novedades, las lecturas y lo pendiente.",
        ["identifica los tres peligros", "señala el riesgo de cada uno", "propone controles", "indica qué informa quien entrega la guardia"],
        ["hoja con las cuatro respuestas"],
        ["confundir peligro con riesgo", "proponer solo EPP", "no mencionar el relevo"],
        "Pregunta: «¿qué debe saber quien recibe la guardia?». Si no responde, pídele que relea el último párrafo de la explicación."),
    reinforce="Escribe tres cosas que se vigilan en el puente y tres que se vigilan en la cámara de máquinas.",
    extend="Explica con un ejemplo por qué el descanso es parte de una guardia segura.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (informes de vigía, de ejemplo). Informe 1: «Luz verde a estribor, lejos.» Informe 2: «Sonido de sirena por la proa.» Informe 3: «Objeto flotante a babor, cerca.» "
     "Informe 4: «Alarma de nivel en un tanque, cámara de máquinas.»")
build(
    O6, 2, F,
    use="Aprenderé a describir lo que se ve y se oye con un lenguaje técnico claro: luces, sonidos, objetos, su ubicación y sus datos básicos.",
    prior=["Sé qué es vigilar y qué es una alarma.", "Sé qué son babor y estribor.", "Sé restar números enteros."],
    explain=[
        "Para informar un avistamiento se dice qué es, dónde está, cuándo se detectó y a qué distancia aproximada. La ubicación se dice con la marcación relativa, que indica dónde está algo respecto de la proa: por la proa (adelante), por la popa (atrás), a estribor (a la derecha), a babor (a la izquierda) o por el través (de costado, a un lado). Las naves llevan luces de navegación de noche: una luz verde se coloca en el costado de estribor y una luz roja, en el de babor.",
        "Las señales acústicas, como la sirena, la campana o el silbato, comunican o avisan. Con poca visibilidad, como en niebla, se vigila con más atención y se informa al oficial, que decide. Las alarmas de equipos, como la de nivel de un tanque, avisan que un valor salió de lo normal. Un ejemplo con otra nave: «Luz roja por la proa, cerca, a las 22:05» tiene qué, dónde, distancia y hora.",
        f"El vigía informa lo que ve y oye y no decide maniobras. {EMER} {AVISO}",
    ],
    vocab=[("avistamiento", "cosa que se ve o se oye y se informa"), ("marcación relativa", "ubicación de algo respecto de la proa de la nave"), ("por el través", "de costado, hacia un lado de la nave"), ("luces de navegación", "luces que muestran la posición de una nave de noche"), ("vigía", "persona que observa y escucha e informa lo detectado")],
    worked=[
        ("Ubicar un objeto", "Un vigía de ejemplo ve un objeto delante de la nave. ¿Cómo informa su ubicación?", ["Lo que está adelante está por la proa.", "La marcación relativa se dice respecto de la proa."], "Por la proa"),
        ("Completar un informe", "Un informe de ejemplo dice «Sonido de sirena.» ¿Qué datos le faltan?", ["Falta dónde se oyó y cuándo.", "También conviene decir si está cerca o lejos."], "Falta la ubicación, la hora y la distancia aproximada"),
    ],
    mistakes=[("Informar un objeto sin decir dónde está.", "Sin ubicación el oficial no puede mirar hacia el lugar correcto.", "Di siempre la marcación relativa."),
              ("Decidir por cuenta propia qué hacer con lo avistado.", "Las maniobras las decide el oficial a cargo.", "Informa lo detectado y espera la orden.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué significa «por la proa»?", "Adelante de la nave", "Atrás de la nave", "A la derecha de la nave", "La proa es la parte delantera, por lo tanto «por la proa» es adelante."),
        ("abc", "En Tripulación de Naves: ¿qué es un vigía?", "Una persona que observa y escucha e informa lo detectado", "Un oficial que decide las maniobras", "Un instrumento que mide la profundidad", "El vigía observa e informa; no decide maniobras."),
        ("abc", "{F} ¿En qué lado de la nave se ve la luz del informe 1?", "A la derecha, porque estribor es el lado derecho", "A la izquierda, porque estribor es el lado izquierdo", "Adelante, porque es una luz verde", "Estribor es el lado derecho mirando hacia la proa."),
        ("abc", "{F} ¿Qué informe de la ficha indica que hay que revisar un equipo y no el mar?", "El informe 4", "El informe 3", "El informe 2", "El informe 4 habla de una alarma de nivel en un tanque."),
        ("abc", "{F} ¿Qué dato falta en todos los informes de la ficha?", "La hora en que se detectó", "El nombre de la nave", "El color del mar", "Ningún informe de la ficha indica la hora de la detección."),
        ("abc", "{F} ¿Dónde está el objeto del informe 3?", "A babor, es decir, a la izquierda y cerca", "A estribor, es decir, a la derecha y lejos", "Por la proa y lejos", "Según el informe, el objeto está a babor y cerca."),
        ("=", "{F} Una señal se detectó a las 02:15 y se informó a las 02:17. ¿Cuántos minutos pasaron entre ambas?", "17-15", "Se resta el minuto de la detección al minuto del informe.", " minutos"),
        ("=", "{F} Si el vigía registra 3 avistamientos por hora, ¿cuántos registra en una guardia de 4 horas?", "3*4", "Se multiplican los avistamientos por hora por las horas de la guardia.", " avistamientos"),
        ("abc", "{F} ¿Cuál es el informe más completo de un objeto avistado?", "«A las 22:05, objeto flotante por la proa, a unas 2 millas»", "«Hay un objeto»", "«Algo se ve»", "El informe completo da hora, qué es, dónde está y a qué distancia."),
        ("abc", "{F} Con niebla, el vigía casi no ve objetos. ¿Qué corresponde?", "Informar al oficial de la poca visibilidad y vigilar con más atención", "Dejar de vigilar, porque no se ve", "Decidir por su cuenta cambiar de velocidad", "La poca visibilidad se informa; las decisiones de maniobra son del oficial."),
        ("abc", "{F} Un compañero dice que no es necesario informar una sirena lejana porque no se ve. ¿Qué respuesta es correcta?", "Es falso: las señales acústicas también se informan", "Es cierto, porque lo que no se ve no importa", "Es cierto, si es de día", "Una señal acústica es información sobre lo que hay en el entorno."),
        ("=", "{F} Si cada informe lleva 4 datos (qué, dónde, hora y distancia) y hay 4 informes, ¿cuántos datos se registran?", "4*4", "Se multiplican los informes por los datos de cada uno.", " datos"),
        ("abc", "{F} Dos vigías informan el mismo objeto: uno dice a babor y otro a estribor. ¿Qué corresponde?", "Informar ambas versiones al oficial y volver a observar", "Elegir una versión al azar", "No informar hasta que coincidan", "Con versiones distintas se informan las dos y se verifica."),
    ],
    ctx=("abc", "Estás de visita en una nave de ejemplo y notas un objeto en el mar cerca de la proa mientras el vigía conversa con otra persona. ¿Qué haces?", "Avisarle al vigía o al oficial de guardia de inmediato, sin acercarte a la borda", "Esperar a que él lo note", "Acercarte a la borda para verlo mejor", "Avisar de inmediato es lo correcto; acercarse a la borda es riesgoso."),
    sc=[
        ("En Tripulación de Naves: ¿qué datos tiene un informe de avistamiento?", "Qué es, dónde está, hora y distancia aproximada", "Esos cuatro datos permiten al oficial decidir."),
        ("¿Qué indica una luz verde de navegación?", "El costado de estribor", "La luz verde se coloca en el costado derecho."),
        ("¿Quién decide las maniobras?", "El oficial a cargo", "El vigía informa y no decide."),
    ],
    op=("Informes de ejemplo de la «Nave Ejemplo»: A) «Luz roja por la proa, cerca, 23:10.» B) «Sirena a estribor, lejos, 23:12.» C) «Alarma de temperatura en un motor, cámara de máquinas, 23:15.» Escribe (a) en qué costado de una nave se coloca la luz roja de navegación, (b) cuántos minutos pasaron entre el primer y el último informe, (c) cuál informe se refiere a un equipo y no al mar, (d) cómo mejorarías el informe B.",
        "(a) La luz roja de navegación se coloca en el costado de babor, el izquierdo. (b) 23:15 − 23:10 = 5 minutos. (c) El informe C. (d) Diciendo qué tipo de señal acústica es, por ejemplo una sirena, cuántas veces suena y a qué distancia aproximada, además de la hora.",
        ["identifica el lado de la luz", "calcula los minutos", "distingue mar y equipo", "mejora el informe"],
        ["hoja con las cuatro respuestas"],
        ["confundir babor con estribor", "no restar bien las horas", "no mencionar distancia"],
        "Pregunta: «¿qué luz va en cada costado?». Si no responde, pídele que relea la primera parte de la explicación."),
    reinforce="Escribe tres informes de vigía completos con qué, dónde, hora y distancia.",
    extend="Explica por qué la marcación relativa se dice respecto de la proa y no respecto de la persona.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (plan de guardia de ejemplo, inventado). En un día hay 6 guardias de 4 horas, cada una con 2 personas, entre tres personas llamadas A, B y C. Guardia 1 (00:00 a 04:00): A y B. Guardia 2: B y C. Guardia 3: C y A. "
     "Guardia 4: A y B. Guardia 5: B y C. Guardia 6: C y A. Regla de ejemplo: nadie debe cumplir más de 8 horas de guardia al día.")
build(
    O6, 3, F,
    use="Aprenderé a leer un plan de guardias, a calcular las horas de cada persona y a detectar si el plan cumple una regla de descanso.",
    prior=["Sé qué es una guardia y un puesto de guardia.", "Sé multiplicar y dividir números enteros.", "Sé comparar un valor con una regla."],
    explain=[
        "Un plan de guardia es una tabla que dice quién cumple cada guardia y cuándo. Con él se calculan las horas de guardia de cada persona: se cuentan sus guardias y se multiplican por la duración de cada una. Una persona-hora es una hora de trabajo de una persona. Las horas totales de un día son los puestos de guardia por las horas de cada guardia. Si una regla fija un máximo de horas por persona, se compara cada persona con ese máximo.",
        "Un ejemplo con otro plan: 4 guardias de 4 horas con 2 personas son 8 puestos y 32 persona-horas; repartidas entre 4 personas, son 8 horas por persona. La fatiga aumenta el riesgo de errores, por lo que un plan que supera la regla debe informarse al oficial y rehacerse; la persona en formación no cambia el plan por su cuenta. El mínimo de personas necesarias se obtiene dividiendo las persona-horas totales entre el máximo por persona.",
        f"Estos números son de ejemplo; los reales dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("plan de guardia", "tabla que dice quién cumple cada guardia y cuándo"), ("persona-hora", "una hora de trabajo de una persona"), ("regla de descanso", "máximo de horas de guardia por persona al día"), ("reparto", "forma en que se distribuyen las guardias entre las personas"), ("fatiga", "cansancio que reduce la atención")],
    worked=[
        ("Horas de una persona", "En un plan de ejemplo una persona cumple 3 guardias de 4 horas. ¿Cuántas horas de guardia cumple?", ["Se multiplican las guardias por la duración de cada una.", "3 × 4."], "12 horas"),
        ("Personas necesarias", "Un plan de ejemplo suma 24 persona-horas y la regla permite 6 horas por persona. ¿Cuántas personas hacen falta como mínimo?", ["Se dividen las persona-horas entre el máximo por persona.", "24 ÷ 6."], "4 personas"),
    ],
    mistakes=[("Creer que cumplir más horas es «ayudar» y no es un riesgo.", "La fatiga aumenta los errores y pone en riesgo a toda la tripulación.", "Respeta la regla de descanso y avisa si el plan la supera."),
              ("Cambiar el plan por cuenta propia para que cuadre.", "El plan lo fija el oficial o el jefe responsable.", "Informa el incumplimiento y espera que lo rehagan.")],
    T=[
        ("=", "{F} ¿Cuántas guardias hay en un día, según la ficha?", "24//4", "Se divide el día entre la duración de cada guardia.", " guardias"),
        ("=", "{F} ¿Cuántos puestos de guardia hay en un día?", "6*2", "Se multiplican las guardias por las personas de cada una.", " puestos"),
        ("abc", "En Tripulación de Naves: ¿qué es un plan de guardia?", "Una tabla que dice quién cumple cada guardia y cuándo", "Un registro de las lecturas de los instrumentos", "Una lista de los repuestos de la nave", "El plan de guardia asigna personas y horarios."),
        ("=", "{F} Si las guardias-persona del día se reparten por igual entre A, B y C, ¿cuántas guardias cumple cada una?", "(6*2)//3", "Se multiplican las guardias por las personas de cada una y se divide entre las 3 personas.", " guardias"),
        ("=", "{F} ¿Cuántas horas de guardia cumple la persona A en el día?", "4*4", "Se multiplican las guardias de A por las horas de cada una.", " horas"),
        ("abc", "{F} ¿Cumple el plan con la regla de descanso de la ficha?", "No, porque cada persona cumple 16 horas y el máximo es 8", "Sí, porque cada guardia dura solo 4 horas", "Sí, porque hay 2 personas por guardia", "Cada persona cumple 4 guardias de 4 horas, es decir, 16 horas, y la regla permite 8."),
        ("=", "{F} ¿Cuántas horas sobre la regla cumple cada persona?", "16-8", "Se resta el máximo permitido a las horas que cumple cada persona.", " horas"),
        ("=", "{F} ¿Cuántas persona-horas de guardia suma el día completo?", "6*2*4", "Se multiplican guardias, personas por guardia y horas de cada guardia.", " persona-horas"),
        ("=", "{F} ¿Cuántas personas hacen falta como mínimo para cumplir la regla de 8 horas?", "(6*2*4)//8", "Se dividen las persona-horas totales entre el máximo por persona.", " personas"),
        ("abc", "{F} Un compañero dice que no importa pasarse de las 8 horas porque «todos están acostumbrados». ¿Qué respuesta es correcta?", "Es falso: la fatiga aumenta los errores y la regla se respeta", "Es cierto, si todos están de acuerdo", "Es cierto, si hay café a bordo", "El acuerdo o la costumbre no eliminan el riesgo de la fatiga."),
        ("abc", "{F} Una persona en formación nota que el plan supera la regla de descanso. ¿Qué corresponde?", "Informar al oficial o al responsable para que se rehaga el plan", "Cambiar el nombre de una persona en el plan", "Callar para no molestar", "El plan lo rehace el responsable; se informa el incumplimiento."),
        ("=", "{F} Si el plan se rehace con 8 personas repartidas por igual, ¿cuántas horas de guardia cumple cada persona?", "(6*2*4)//8", "Se dividen las persona-horas totales entre las personas.", " horas"),
        ("abc", "{F} Si el plan se rehace con 8 personas repartidas por igual, ¿cumple la regla?", "Sí, porque cada persona cumple 6 horas, menos de las 8 permitidas", "No, porque son más de 6 personas", "No, porque faltan guardias en el día", "Con 8 personas cada una cumple 6 horas, por debajo del máximo."),
    ],
    ctx=("abc", "Una persona de ejemplo te dice: «prefiero hacer 12 horas seguidas para tener después varios días libres, no avises». ¿Qué corresponde?", "Informar al responsable, porque la regla de descanso protege a todos", "No avisar, porque ella lo pidió", "Avisar solo si ocurre un accidente", "La regla de descanso no se negocia por preferencia personal."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calculan las horas de una persona?", "Guardias que cumple por la duración de cada una", "Se multiplican sus guardias por las horas."),
        ("¿Qué es una persona-hora?", "Una hora de trabajo de una persona", "Con persona-horas se calcula el total del plan."),
        ("¿Por qué se respeta la regla de descanso?", "Porque la fatiga aumenta los errores", "El descanso protege la atención de toda la guardia."),
    ],
    op=("Plan de ejemplo: 4 guardias de 4 horas al día, cada una con 3 personas, repartidas entre 4 personas (P, Q, R y S) en partes iguales. Regla de ejemplo: máximo 9 horas de guardia por persona al día. Escribe (a) los puestos de guardia del día, (b) las persona-horas totales, (c) cuántas horas cumple cada persona y si cumple la regla, (d) cuántas personas harían falta como mínimo para cumplir una regla de 6 horas.",
        "(a) 4 × 3 = 12 puestos. (b) 12 × 4 = 48 persona-horas. (c) 48 ÷ 4 = 12 horas por persona; no cumple la regla de 9 horas. (d) 48 ÷ 6 = 8 personas.",
        ["calcula los puestos", "calcula las persona-horas", "compara con la regla", "calcula las personas mínimas"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por las horas", "no comparar con la regla", "no dividir las persona-horas"],
        "Pregunta: «¿cuántas persona-horas hay que repartir?». Si no responde, pídele que escriba la multiplicación."),
    reinforce="Inventa un plan de guardia con 3 guardias y 3 personas y calcula las horas de cada una.",
    extend="Explica qué ocurre con las horas por persona si se suman personas al plan.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (datos de ejemplo). La «Nave Demo» navega a 12 nudos. A las 02:00 un vigía informa un objeto flotante por la proa, a 9 millas náuticas. A las 02:30 otro vigía informa una señal acústica por babor. "
     "El relevo de guardia es a las 04:00. Se supone que el objeto está quieto y que la nave mantiene su velocidad.")
build(
    O6, 4, F,
    use="Aprenderé a calcular tiempos de aproximación con datos de ejemplo, a priorizar lo que se informa y a ordenar la información para el relevo.",
    prior=["Sé calcular tiempo, distancia y velocidad.", "Sé qué es un avistamiento y un relevo.", "Sé pasar horas a minutos."],
    explain=[
        "Con un avistamiento se puede estimar cuánto falta para llegar a la posición del objeto: tiempo = distancia ÷ velocidad. Si la velocidad está en nudos y la distancia en millas, el resultado es en horas; para pasarlo a minutos se multiplica por 60. Es una estimación que supone que la nave y el objeto no cambian; el oficial decide qué hacer, y el vigía solo informa.",
        "Se prioriza lo que informa un riesgo más cercano en el tiempo. Un ejemplo con otra nave: una boya de ejemplo a 6 millas con una velocidad de 12 nudos está a 30 minutos; a esa hora se informa sin esperar. En el relevo, quien entrega informa los avistamientos pendientes con sus horas y datos. Los valores de esta clase son de ejemplo y este cuaderno no enseña a evitar objetos ni a maniobrar la nave.",
        f"Si no se sabe qué hacer, se informa y se espera la orden. {EMER} {AVISO}",
    ],
    vocab=[("tiempo de aproximación", "tiempo que falta para llegar a la posición de un objeto"), ("objeto flotante", "objeto que está sobre el agua"), ("prioridad", "orden en que se informa, de lo más cercano en el tiempo a lo más lejano"), ("estimación", "cálculo aproximado con un supuesto"), ("pendiente", "tarea o dato que falta resolver")],
    worked=[
        ("Tiempo de aproximación", "Un objeto de ejemplo está a 8 millas y la nave va a 16 nudos. ¿En cuánto tiempo llega a su posición?", ["Tiempo = distancia ÷ velocidad = 8 ÷ 16 de hora.", "Media hora son 30 minutos."], "30 minutos"),
        ("Priorizar", "Dos avistamientos de ejemplo están a 20 y a 5 minutos de distancia. ¿Cuál se informa primero?", ["Se informa primero lo más cercano en el tiempo.", "5 minutos es menor que 20."], "El de 5 minutos"),
    ],
    mistakes=[("Dividir la velocidad entre la distancia.", "El tiempo es distancia ÷ velocidad.", "Escribe la fórmula antes de calcular."),
              ("Decidir qué maniobra hacer al ver un objeto.", "Las maniobras las decide el oficial a cargo.", "Informa y espera la orden.")],
    T=[
        ("=", "{F} A las 02:00, ¿cuántos minutos tardaría la nave en llegar a la posición del objeto?", "9*60//12", "Se divide la distancia entre la velocidad y se pasa a minutos multiplicando por 60.", " minutos"),
        ("abc", "{F} ¿A qué hora la nave llegaría a la posición del objeto, si todo se mantiene?", "02:45", "03:00", "02:30", "Pasan 45 minutos después de las 02:00."),
        ("=", "{F} ¿Cuántas millas recorre la nave en 30 minutos?", "12*30//60", "Se calcula la parte de la hora y se multiplica por la velocidad.", " millas"),
        ("=", "{F} A las 02:30, ¿cuántas millas faltan para la posición del objeto?", "9-6", "Se restan las millas recorridas en 30 minutos a la distancia inicial.", " millas"),
        ("=", "{F} A las 02:30, ¿cuántos minutos faltan para llegar a la posición del objeto?", "3*60//12", "Se divide la distancia que falta entre la velocidad y se pasa a minutos.", " minutos"),
        ("abc", "{F} Al detectar el objeto a las 02:00, ¿qué hace el vigía?", "Informar de inmediato al oficial de guardia", "Cambiar el rumbo por su cuenta", "Esperar a las 02:30 para ver si se acerca", "El vigía informa; no maniobra ni espera."),
        ("=", "{F} ¿Cuántas horas faltan entre el avistamiento de las 02:00 y el relevo de las 04:00?", "4-2", "Se resta la hora del avistamiento a la hora del relevo.", " horas"),
        ("abc", "{F} ¿Qué debe informar quien entrega la guardia a las 04:00 sobre lo avistado?", "El objeto y la señal acústica, con sus horas, ubicaciones y lo pendiente", "Solo la hora del relevo", "Nada, porque ya se informó al oficial", "El relevo traspasa lo avistado y lo pendiente con sus datos."),
        ("=", "{F} Si la nave redujera a 6 nudos, ¿cuántos minutos tardaría en recorrer las 9 millas?", "9*60//6", "Se divide la distancia entre la nueva velocidad y se pasa a minutos.", " minutos"),
        ("abc", "{F} Un compañero calcula el tiempo dividiendo 12 entre 9. ¿Cuál es el error?", "Dividió la velocidad entre la distancia en vez de la distancia entre la velocidad", "Debió restar 9 de 12", "No hay error, porque da lo mismo", "El tiempo es distancia ÷ velocidad, no al revés."),
        ("abc", "{F} A las 02:30 hay dos datos: el objeto a 15 minutos y una señal acústica por babor. ¿Qué se informa primero?", "Ambos de inmediato; el objeto con su tiempo estimado y la señal con su ubicación", "Solo el objeto, porque es lo más cercano", "Solo la señal, porque es más nueva", "Los dos se informan sin demora; el oficial decide la prioridad."),
        ("=", "{F} ¿Cuántos minutos faltan entre la señal acústica de las 02:30 y el relevo de las 04:00?", "4*60-(2*60+30)", "Se pasan las dos horas a minutos y se restan al tiempo hasta el relevo.", " minutos"),
        ("abc", "{F} ¿Por qué el tiempo de aproximación es una estimación?", "Porque supone que la nave y el objeto no cambian su situación", "Porque el reloj puede estar atrasado", "Porque las millas no se pueden medir", "La estimación depende de que la velocidad y la posición se mantengan."),
    ],
    ctx=("abc", "Un compañero te dice que, como el objeto está lejos, no hace falta informar hasta que esté «muy cerca». ¿Qué respondes?", "Que se informa de inmediato para que el oficial decida con tiempo", "Que sí, mejor esperar", "Que lo informas después del relevo", "Informar tarde le quita tiempo al oficial para decidir."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el tiempo de aproximación?", "Distancia dividida entre velocidad", "Es la misma fórmula del tiempo de viaje."),
        ("¿Qué se prioriza al informar?", "Lo más cercano en el tiempo", "El riesgo más cercano en el tiempo se informa primero."),
        ("¿Quién decide la maniobra?", "El oficial a cargo", "El vigía informa y no decide."),
    ],
    op=("Datos de ejemplo: una nave navega a 24 nudos. Un vigía informa a las 21:00 una boya de ejemplo por la proa a 8 millas náuticas y a las 21:10 una señal acústica por estribor. Escribe (a) cuántos minutos tardaría la nave en llegar a la boya si no cambia nada, (b) a qué hora sería, (c) cuántas millas faltan a las 21:10, (d) qué informarías al oficial.",
        "(a) 8 ÷ 24 de hora son 20 minutos. (b) A las 21:20. (c) En 10 minutos recorre 4 millas, por lo que faltan 4 millas. (d) «Boya por la proa, a unas 4 millas a las 21:10, llegaría hacia las 21:20; señal acústica por estribor a las 21:10».",
        ["calcula el tiempo", "calcula la hora", "calcula las millas que faltan", "redacta el informe"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar pasar a minutos", "decidir una maniobra"],
        "Pregunta: «¿qué operación da el tiempo?». Si no responde, pídele que repase el primer ejemplo resuelto."),
    reinforce="Inventa tres avistamientos con su distancia y calcula el tiempo de cada uno a 12 nudos.",
    extend="Explica por qué informar pronto un avistamiento da más tiempo al oficial para decidir.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas de ejemplo). Hay 12 puestos de guardia por día (6 guardias de 4 horas con 2 personas). Plan A: 6 personas. Plan B: 4 personas. Plan C: 12 personas. "
     "Criterio obligatorio: nadie cumple más de 8 horas de guardia al día. Criterio de elección: menor número de personas. Bitácora de ejemplo: línea 1, 02:00, objeto por la proa, informado al oficial, firma del vigía. Línea 2, 02:30, señal acústica por babor, sin informar, sin firma.")
build(
    O6, 5, F,
    use="Aprenderé a comparar planes de guardia con criterios y a verificar que una bitácora esté completa.",
    prior=["Sé calcular horas por persona de un plan de guardia.", "Sé qué es una bitácora.", "Sé calcular un porcentaje simple."],
    explain=[
        "Para comparar planes de guardia se aplican los mismos criterios a todos. El criterio obligatorio es una regla que debe cumplirse: por ejemplo, que nadie supere un máximo de horas de guardia al día; un plan que no la cumple se descarta. El criterio de elección sirve para escoger entre los que quedan, como usar menos personas. Las horas por persona se calculan dividiendo las persona-horas totales del día entre las personas del plan.",
        "Verificar la calidad de una bitácora es comprobar que cada línea esté completa: hora, hecho, si se informó y firma. Una línea incompleta se devuelve a quien la hizo para que la complete, sin inventar datos. El porcentaje de líneas completas es las completas ÷ las totales × 100. Un ejemplo con otro registro: de 5 líneas, 4 completas son el 80 %, y la línea incompleta igual se corrige.",
        f"La decisión final del plan es del oficial o del responsable; la persona en formación calcula e informa. {EMER} {AVISO}",
    ],
    vocab=[("criterio obligatorio", "regla que debe cumplirse para que un plan siga en la comparación"), ("criterio de elección", "regla para escoger entre los planes que cumplen"), ("persona-horas", "horas de trabajo sumadas de todas las personas"), ("línea completa", "línea de bitácora con hora, hecho, si se informó y firma"), ("verificar", "comprobar con datos que algo cumple")],
    worked=[
        ("Horas por persona", "Un plan de ejemplo suma 40 persona-horas con 5 personas. ¿Cuántas horas cumple cada una?", ["Se dividen las persona-horas entre las personas.", "40 ÷ 5."], "8 horas"),
        ("Descartar un plan", "Un plan de ejemplo exige 10 horas por persona y la regla permite 8. ¿Se descarta?", ["10 horas supera el máximo de 8.", "Un plan que no cumple el criterio obligatorio se descarta."], "Sí, se descarta"),
    ],
    mistakes=[("Elegir el plan con menos personas sin revisar si cumple la regla de descanso.", "El criterio obligatorio va primero.", "Aplica primero el criterio obligatorio y después el de elección."),
              ("Completar una línea de bitácora con datos inventados.", "Un dato inventado falsea el registro.", "Devuelve la línea a quien la hizo para que la complete.")],
    T=[
        ("=", "{F} ¿Cuántas persona-horas de guardia suma el día?", "12*4", "Se multiplican los puestos de guardia por las horas de cada guardia.", " persona-horas"),
        ("=", "{F} ¿Cuántas horas de guardia cumple cada persona en el plan A?", "(12*4)//6", "Se dividen las persona-horas entre las personas del plan.", " horas"),
        ("abc", "{F} ¿Cumple el plan A con el criterio obligatorio?", "Sí, porque cada persona cumple 8 horas, que no supera el máximo", "No, porque 8 horas es demasiado", "No, porque tiene menos personas que el plan C", "Cada persona cumple 8 horas, igual al máximo permitido."),
        ("=", "{F} ¿Cuántas horas de guardia cumple cada persona en el plan B?", "(12*4)//4", "Se dividen las persona-horas entre las personas del plan.", " horas"),
        ("abc", "{F} ¿Cumple el plan B con el criterio obligatorio?", "No, porque cada persona cumple 12 horas y el máximo es 8", "Sí, porque usa menos personas", "Sí, porque 12 es el número de puestos", "12 horas por persona supera el máximo de 8."),
        ("=", "{F} ¿Cuántas horas de guardia cumple cada persona en el plan C?", "(12*4)//12", "Se dividen las persona-horas entre las personas del plan.", " horas"),
        ("abc", "{F} ¿Qué plan se elige según los criterios de la ficha?", "El plan A, porque cumple el criterio obligatorio y usa menos personas que el plan C", "El plan B, porque usa menos personas", "El plan C, porque cada persona cumple menos horas", "B queda descartado y entre A y C se elige el de menos personas."),
        ("=", "{F} ¿Cuántas personas menos usa el plan A que el plan C?", "12-6", "Se resta el número de personas del plan A al del plan C.", " personas"),
        ("abc", "{F} ¿Qué le falta a la línea 2 de la bitácora?", "Informar al oficial y la firma", "La hora y el hecho", "Nada, porque tiene hora y hecho", "La línea tiene hora y hecho, pero no dice que se informó y no está firmada."),
        ("abc", "{F} ¿Qué corresponde con la línea 2 incompleta?", "Devolverla a quien la hizo para que la complete, sin inventar datos", "Completarla con una firma que parezca correcta", "Borrarla de la bitácora", "Una línea incompleta la completa su autor; no se inventan datos."),
        ("abc", "{F} Un compañero dice: «elijamos el plan B porque ocupa menos personas, y la regla ya la revisaremos después». ¿Qué respuesta es correcta?", "Es falso: la regla obligatoria se revisa primero y B no la cumple", "Es cierto, porque el menor número de personas manda", "Es cierto, si se informa al oficial después", "El criterio obligatorio se aplica antes que el de elección."),
        ("=", "{F} ¿Qué porcentaje de las líneas de la bitácora está completo?", "1*100//2", "Se divide la línea completa entre las líneas totales y se multiplica por 100.", " %"),
        ("abc", "En Tripulación de Naves: ¿por qué una bitácora con una línea incompleta no es confiable?", "Porque no permite saber si lo avistado se informó ni quién lo anotó", "Porque tiene demasiadas firmas", "Porque las horas no se registran", "Sin informe ni firma no se puede reconstruir qué ocurrió."),
    ],
    ctx=("abc", "El oficial de ejemplo te pide comparar dos planes de guardia y a ti te parece mejor uno que no cumple la regla de descanso, pero usa menos personas. ¿Qué haces?", "Presentas los cálculos de ambos y le informas que uno no cumple la regla, para que decida", "Le presentas solo el plan que te parece mejor", "Le presentas ambos pero ocultas que uno no cumple", "Una comparación honesta muestra los datos y los incumplimientos."),
    sc=[
        ("En Tripulación de Naves: ¿qué se aplica primero al comparar planes?", "El criterio obligatorio", "Los planes que no lo cumplen se descartan."),
        ("¿Qué datos tiene una línea completa de bitácora?", "Hora, hecho, si se informó y firma", "Con esos datos se reconstruye lo ocurrido."),
        ("¿Qué se hace con una línea incompleta?", "Se devuelve a quien la hizo para que la complete", "Se corrige sin inventar datos nuevos."),
    ],
    op=("Alternativas de ejemplo: hay 8 puestos de guardia al día de 6 horas cada uno. Plan X: 4 personas. Plan Y: 8 personas. Criterio obligatorio: máximo 12 horas de guardia por persona al día. Criterio de elección: menor número de personas. Bitácora de ejemplo: línea 1, 10:00, luz por estribor, informado, firma; línea 2, 10:20, alarma de nivel, informado, sin firma. Escribe (a) las horas por persona de cada plan, (b) cuál se elige, (c) el porcentaje de líneas completas de la bitácora, (d) qué haces con la línea 2.",
        "(a) Persona-horas: 8 × 6 = 48. Plan X: 48 ÷ 4 = 12 horas; plan Y: 48 ÷ 8 = 6 horas. (b) Ambos cumplen el máximo de 12 horas; se elige el plan X, que usa menos personas. (c) 1 de 2 líneas: 50 %. (d) Se devuelve a quien la hizo para que la firme, sin inventar la firma.",
        ["calcula las horas por persona", "aplica los criterios", "calcula el porcentaje de líneas completas", "indica qué hacer con la línea incompleta"],
        ["hoja con las cuatro respuestas"],
        ["no calcular las persona-horas", "elegir sin aplicar el criterio obligatorio", "inventar la firma"],
        "Pregunta: «¿cuántas persona-horas hay que repartir?». Si no responde, pídele que escriba la multiplicación."),
    reinforce="Inventa dos planes de guardia con un criterio obligatorio y otro de elección y escribe cuál se elige.",
    extend="Explica por qué la bitácora completa ayuda a que el relevo de guardia sea seguro.",
)

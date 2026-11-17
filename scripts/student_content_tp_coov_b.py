"""Construcción TP, mención Obras Viales e Infraestructura, 4.º medio: OAM-03 (controlar el movimiento de tierra) y OAM-04 (verificar saneamientos, muros y defensas). Solo conceptos, lectura de documentos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_coov_common import AVISO, EMER, build

O3 = "TP-COOV-4-OAM-03"
O4 = "TP-COOV-4-OAM-04"

# ============================================================ OAM-03, clase 1
F = ("Ficha 10 (obra de ejemplo, inventada). Camino «Las Vertientes» (ficticio). Movimiento de tierra: despeje de franja de 10.000 m²; corte de 2.400 m³; terraplén de 1.800 m³. "
     "Máquinas anotadas en el parte diario: 2 excavadoras, 1 motoniveladora y 6 camiones. Riesgos anotados: atropello, vuelco de máquinas, derrumbe de talud, atrapamiento y contacto con redes enterradas.")
build(
    O3, 1, F,
    use="Aprenderé qué es el movimiento de tierra en una obra vial, qué significa controlarlo y qué riesgos y reglas de seguridad hay que reconocer.",
    prior=["Sé qué es un corte y un terraplén.", "Sé leer progresivas.", "Sé dividir y multiplicar."],
    explain=[
        "El movimiento de tierra es el conjunto de faenas que sacan, trasladan y colocan suelo para dar forma al terreno de una obra vial. Incluye el despeje de la franja, que es dejar libre de vegetación y de obstáculos la zona donde irá la obra; los cortes, donde el terreno queda más alto que el camino; y los terraplenes, donde el camino se levanta con material. Estas faenas las hacen máquinas, como excavadoras, motoniveladoras y camiones. Controlar el movimiento de tierra es comprobar, con planos, registros y mediciones, que se ejecuta según lo proyectado y según la norma vigente; no es operar las máquinas.",
        "Los riesgos son el atropello, el vuelco de máquinas, el derrumbe de taludes, el atrapamiento y el contacto con redes enterradas, como tuberías o cables que no se ven. Las reglas generales son no acercarse a la zona de maniobra de las máquinas ni al borde de cortes y taludes sin autorización, respetar la señalización y que el trabajo en terreno lo haga solo personal autorizado, con EPP y acompañado. El mandante exige además cuidar el medio ambiente, por ejemplo depositando los sobrantes solo en lugares autorizados.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("movimiento de tierra", "faenas que sacan, trasladan y colocan suelo en una obra"), ("despeje de franja", "dejar libre de vegetación y obstáculos la zona de la obra"), ("corte", "zona donde el terreno queda más alto que el camino"), ("terraplén", "zona donde el camino se levanta con material"), ("parte diario", "registro diario de las máquinas y su trabajo"), ("red enterrada", "tubería o cable bajo el suelo que no se ve desde la superficie")],
    worked=[
        ("Volumen total", "En un sector de ejemplo hay un corte de 500 m³ y otro de 300 m³. ¿Cuántos m³ de corte hay en total?", ["Ambos cortes se miden en m³.", "500 más 300 son 800."], "800 m³"),
        ("Viajes", "Un camión de ejemplo lleva 10 m³ por viaje. ¿Cuántos viajes se necesitan para 250 m³?", ["Se divide el volumen por lo que lleva cada viaje.", "250 entre 10 son 25."], "25 viajes"),
    ],
    mistakes=[("Creer que controlar el movimiento de tierra es manejar las máquinas.", "Controlar es comprobar con documentos y mediciones; operar exige autorización y capacitación.", "Aprende el control en papel y deja la operación a personal autorizado."),
              ("Acercarse al borde de un corte para ver mejor.", "El borde puede ceder y el talud puede derrumbarse.", "Mantén distancia y avisa a un adulto responsable.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es el despeje de la franja?", "Dejar libre de vegetación y obstáculos la zona donde irá la obra", "Rebajar el terreno hasta la cota del camino", "Levantar el camino con material", "El despeje prepara la zona; rebajar es un corte y levantar con material es un terraplén."),
        ("abc", "¿Qué es el parte diario de maquinaria?", "El registro diario de las máquinas y su trabajo", "El plano con los perfiles del camino", "El informe del laboratorio con resultados", "El parte anota máquinas y trabajo por día; los perfiles y los resultados están en otros documentos."),
        ("abc", "En una obra vial, ¿qué significa controlar el movimiento de tierra?", "Comprobar con planos, registros y mediciones que se ejecuta según lo proyectado", "Operar las máquinas para acelerar la faena", "Dirigir el tránsito de camiones en la calle", "Controlar es verificar con evidencia; operar o dirigir el tránsito son tareas de otras personas autorizadas."),
        ("=", "{F} ¿Cuántos m³ suman el corte y el terraplén?", "2400+1800", "Ambos volúmenes se miden en m³, así que se suman.", " m³"),
        ("abc", "{F} ¿Cuál de estos riesgos aparece anotado en la ficha?", "Derrumbe de talud", "Descarga eléctrica en un tablero", "Intoxicación en un espacio confinado", "La ficha nombra el derrumbe de talud; los otros riesgos no están anotados."),
        ("abc", "{F} ¿Qué parte del movimiento de tierra se mide en m² en la ficha?", "El despeje de la franja", "El corte", "El terraplén", "La ficha da el despeje en m², una superficie; corte y terraplén están en m³."),
        ("=", "{F} Un camión de ejemplo lleva 12 m³ por viaje. ¿Cuántos viajes se necesitan para transportar los 2.400 m³ del corte?", "2400//12", "Se divide el volumen total por lo que lleva cada viaje.", " viajes"),
        ("abc", "{F} Un visitante quiere acercarse al borde del corte para sacar fotos. ¿Qué corresponde?", "No acercarse: el borde puede ceder y el acceso solo lo hace personal autorizado", "Acercarse si usa casco", "Acercarse si no hay máquinas trabajando en ese momento", "El casco o la ausencia de máquinas no evitan que el borde ceda; se mantiene distancia."),
        ("ab", "{F} Una compañera dice: «estudié el control del movimiento de tierra, así que puedo dirigir a un operador de excavadora». ¿Qué respuesta es correcta?", "No: dirigir y operar máquinas exige autorización y capacitación, no basta con el control en papel", "Sí: quien conoce el control puede dirigir máquinas", "Entender un control no reemplaza la autorización para dirigir máquinas."),
        ("abc", "En una obra de ejemplo, un camión retrocede y una persona queda atrapada entre el camión y un muro. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse a mover a la persona de inmediato", "Esperar a que el camión se detenga solo y avisar al final del turno", "Acercarse sin control puede causar otro accidente; se avisa de inmediato a un adulto responsable y a emergencias."),
        ("abc", "{F} El plano muestra una tubería enterrada bajo la franja, pero el parte diario no la menciona. ¿Qué corresponde?", "Informar al ITO y al prevencionista de riesgos antes de que se trabaje en ese sector", "Ignorar el plano porque el parte diario manda", "Trabajar el sector con cuidado y avisar después", "Una red enterrada es un riesgo grave; se informa antes de trabajar y no se ignora un documento."),
        ("=", "{F} Los 6 camiones hacen 5 viajes por día, cada uno con 12 m³ (datos de ejemplo). ¿Cuántos días se estiman para transportar los 1.800 m³ del terraplén?", "1800//(6*5*12)", "Se calcula lo que mueven al día los 6 camiones y se divide el volumen por esa cantidad.", " días"),
        ("abc", "{F} Para el riesgo de atropello en la zona de maniobra de los camiones, ¿qué medida es de nivel más alto en la jerarquía de controles?", "Cerrar el paso peatonal por esa zona con barreras y desviar a las personas", "Entregar un chaleco reflectante a cada persona", "Pedir a los peatones que miren antes de cruzar", "Aislar el peligro con barreras está sobre pedir atención (organización) y sobre el EPP."),
    ],
    ctx=("abc", "Un conocido ofrece a un estudiante dinero por «manejar un rato» una máquina de una obra porque «es solo mover tierra». ¿Qué responde?", "Agradece y explica que no está autorizado ni capacitado y que eso lo hace personal designado", "Acepta si el conocido se hace responsable", "Acepta si trabaja un rato corto", "Operar una máquina exige autorización y capacitación; asumir la responsabilidad otro o el tiempo corto no la reemplazan."),
    sc=[
        ("En movimiento de tierra: ¿qué es un terraplén?", "Una zona donde el camino se levanta con material", "El terraplén agrega material al camino, mientras que el corte lo rebaja."),
        ("¿Qué es controlar el movimiento de tierra?", "Comprobar con planos, registros y mediciones que se ejecuta según lo proyectado", "Controlar es verificar con evidencia y no consiste en operar máquinas."),
        ("¿Qué se hace ante un atrapamiento en la obra?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse sin control puede causar otro accidente con más víctimas."),
    ],
    op=("Obra de ejemplo «Camino El Boldo» (ficticio): despeje de 6.000 m², corte de 1.500 m³, terraplén de 900 m³. Un camión de ejemplo lleva 10 m³ por viaje. Escribe (a) cuántos m³ suman corte y terraplén, (b) cuántos viajes necesita el corte, (c) un riesgo de la obra y una medida de la jerarquía de controles, (d) qué haces si ves que un compañero se acerca al borde del corte.",
        "(a) 1.500 más 900 son 2.400 m³. (b) 1.500 entre 10 son 150 viajes. (c) Derrumbe de talud: no acercarse, delimitar la zona con barreras y señales. (d) Le aviso que no se acerque, aviso a un adulto responsable y, si hay un accidente, a emergencias.",
        ["suma los volúmenes", "calcula los viajes", "nombra un riesgo y un nivel de control", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["sumar m² con m³", "dividir al revés", "acercarse a ayudar en un accidente"],
        "Pregunta: «¿qué haces ante un accidente en un corte?». Si no responde, pídele que relea la regla de no acercarse y avisar."),
    reinforce="Escribe con tus palabras qué es un corte, un terraplén y un despeje de franja, con un dibujo simple de cada uno.",
    extend="Explica por qué una tubería enterrada que no aparece en un documento es un riesgo antes de mover tierra.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 11 (documentos de ejemplo, inventados). Camino «Las Vertientes» (ficticio). Perfil transversal del Km 0+200: área de corte de 18 m². Perfil transversal del Km 0+240: área de corte de 22 m². "
     "Guía de despacho N.º 31: 12 m³ de material suelto, desde el Km 0+200 hasta el botadero autorizado «B1». Esponjamiento de ejemplo: el material suelto ocupa 20 % más volumen que en su lugar original.")
build(
    O3, 2, F,
    use="Aprenderé los documentos y conceptos del control del movimiento de tierra: perfiles transversales, volumen, esponjamiento, guías de despacho y botaderos.",
    prior=["Sé qué es un corte y un terraplén.", "Sé calcular promedios.", "Sé calcular porcentajes."],
    explain=[
        "El perfil transversal es un corte perpendicular al eje del camino; muestra el área de corte o de relleno en una progresiva. Para estimar el volumen entre dos perfiles se usa el método de las áreas medias: se promedian las dos áreas y se multiplica por la distancia entre ellas. Por ejemplo, áreas de 10 y 14 m² separadas 30 m dan 12 por 30, es decir, 360 m³. Es un cálculo en planilla, no un procedimiento de trabajo.",
        "El esponjamiento es el aumento de volumen que tiene el suelo al sacarlo de su lugar: el material suelto ocupa más espacio que en su lugar original. Con un esponjamiento de ejemplo de 20 %, 100 m³ en su lugar pasan a ser 120 m³ sueltos. La guía de despacho es el documento que acompaña cada viaje de material. El botadero autorizado es el lugar habilitado para depositar sobrantes, como exige la normativa ambiental. Los roles son: el ITO verifica; el topógrafo mide; el jefe de movimiento de tierra coordina las faenas; el prevencionista vigila la seguridad.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("perfil transversal", "corte perpendicular al eje que muestra el área de corte o relleno"), ("áreas medias", "método que promedia dos áreas y multiplica por la distancia entre ellas"), ("esponjamiento", "aumento de volumen del suelo al sacarlo de su lugar"), ("guía de despacho", "documento que acompaña cada viaje de material"), ("botadero autorizado", "lugar habilitado para depositar sobrantes"), ("topógrafo", "persona que mide terrenos y niveles")],
    worked=[
        ("Volumen entre perfiles", "Dos perfiles de ejemplo tienen áreas de 8 y 12 m² y están separados 50 m. ¿Qué volumen hay entre ellos?", ["Se promedian las áreas: 8 y 12 dan 10.", "10 por 50 son 500."], "500 m³"),
        ("Esponjamiento", "Con un esponjamiento de ejemplo de 20 %, hay 50 m³ de suelo en su lugar. ¿Cuántos m³ sueltos son?", ["El 20 % de 50 es 10.", "50 más 10 son 60."], "60 m³"),
    ],
    mistakes=[("Sumar las dos áreas sin promediarlas y multiplicar por la distancia.", "Eso duplica el volumen estimado.", "Promedia las áreas (suma dividida por 2) y luego multiplica por la distancia."),
              ("Contar los m³ sueltos de las guías como si fueran m³ en su lugar.", "El material suelto ocupa más volumen.", "Convierte con el esponjamiento antes de comparar con el proyecto.")],
    T=[
        ("abc", "En Obras Viales: ¿qué muestra un perfil transversal?", "El área de corte o de relleno en una progresiva, vista perpendicular al eje", "Las alturas del camino a lo largo de todo el eje", "El camino visto desde arriba", "El perfil transversal es un corte perpendicular al eje; las alturas a lo largo del eje son del perfil longitudinal."),
        ("abc", "¿Qué es un botadero autorizado?", "Un lugar habilitado para depositar sobrantes", "Un lugar donde se guardan las máquinas por la noche", "Un lugar donde se toman las muestras de laboratorio", "El botadero autorizado recibe sobrantes cumpliendo la normativa ambiental."),
        ("abc", "¿Qué es el esponjamiento del suelo?", "El aumento de volumen que tiene el suelo al sacarlo de su lugar", "La pérdida de humedad del suelo al secarse", "El aumento de resistencia del suelo al excavarlo", "El suelo suelto ocupa más espacio; no se trata de humedad ni de resistencia."),
        ("=", "{F} ¿Qué volumen hay entre los perfiles del Km 0+200 y del Km 0+240 por el método de áreas medias?", "(18+22)*40//2", "Se promedian las áreas y se multiplica por la distancia de 40 m entre perfiles.", " m³"),
        ("abc", "{F} ¿Qué documento acompaña cada viaje de material hacia el botadero?", "La guía de despacho", "El perfil transversal", "El itemizado", "La guía acompaña cada viaje; el perfil y el itemizado son otros documentos."),
        ("abc", "{F} ¿Por qué la guía N.º 31 declara el material como «suelto»?", "Porque, al sacarlo de su lugar, ocupa más volumen que antes", "Porque el material estaba húmedo", "Porque el camión iba a velocidad baja", "El adjetivo suelto alude al aumento de volumen por esponjamiento."),
        ("=", "{F} Con el esponjamiento de ejemplo, ¿cuántos m³ ocupaba en su lugar el material de la guía N.º 31?", "12*100//120", "Los 12 m³ sueltos son 120 % del volumen original; se divide por 120 y se multiplica por 100.", " m³"),
        ("=", "{F} Si el volumen entre los perfiles es de 800 m³ en su lugar, ¿cuántos m³ sueltos serán, con el esponjamiento de ejemplo?", "800*120//100", "El material suelto es 120 % del volumen original.", " m³"),
        ("abc", "{F} La guía N.º 31 menciona un botadero que no figura entre los autorizados del proyecto. ¿Qué corresponde?", "Informar al ITO y no dar por válido el viaje hasta aclararlo", "Aceptar el viaje porque la guía está firmada", "Cambiar el nombre del botadero en la guía", "Un botadero no autorizado incumple la normativa ambiental; se informa y no se corrige la guía por cuenta propia."),
        ("ab", "{F} Un compañero calcula el volumen entre perfiles sumando 18 y 22 y multiplicando por 40, sin dividir por 2. ¿Qué respuesta es correcta?", "No: hay que promediar las áreas, es decir, dividir la suma por 2", "Sí: se suman las áreas y se multiplican por la distancia", "El método usa el promedio de las dos áreas; sin dividir se duplica el volumen."),
        ("abc", "Un proveedor de ejemplo dice que el esponjamiento «no importa» al contar los camiones. ¿Por qué sí importa?", "Porque el material suelto ocupa más volumen y se necesitan más viajes", "Porque cambia el color del material", "Porque no importa: solo se cuentan los camiones", "Con más volumen suelto que en su lugar, se transportan más m³ y se requieren más viajes."),
        ("=", "{F} Si cada viaje lleva 12 m³ de material suelto y hay 800 m³ en su lugar entre los perfiles, ¿cuántos viajes se necesitan?", "800*120//100//12", "Se pasa a volumen suelto con el 20 % y se divide por lo que lleva cada viaje.", " viajes"),
        ("abc", "{F} El conteo de guías de un sector muestra 70 viajes, pero la estimación daba 80. ¿Qué conclusión es la más prudente?", "Revisar la diferencia con los registros e informar al ITO, sin concluir por suposición", "Concluir que sobraron 10 camiones", "Agregar 10 guías para que cuadre", "Una diferencia puede deberse a viajes sin guía, cálculos distintos o errores; se aclara con evidencia."),
    ],
    ctx=("abc", "Un conductor de ejemplo le pide a una estudiante en práctica que firme una guía de despacho «en blanco» para ganar tiempo. ¿Qué responde?", "Que no firma guías incompletas y que lo consulte con el ITO o el responsable de la obra", "Que firma si el material parece correcto", "Que firma si el conductor promete llenarla después", "Una guía en blanco permite declarar lo que sea; se rechaza y se consulta."),
    sc=[
        ("En Obras Viales: ¿qué es la guía de despacho?", "El documento que acompaña cada viaje de material", "La guía permite contar y rastrear cada uno de los viajes."),
        ("¿Cómo se calcula el volumen entre dos perfiles?", "Promediando las áreas y multiplicando por la distancia", "El método de áreas medias usa el promedio de dos áreas."),
        ("¿Qué le ocurre al volumen de un suelo al sacarlo de su lugar?", "Aumenta por el esponjamiento", "El suelo suelto ocupa más espacio que en su lugar."),
    ],
    op=("Documentos de ejemplo de «Camino El Boldo» (ficticio). Perfiles transversales: Km 0+100 con 10 m² de corte y Km 0+130 con 14 m² de corte. Esponjamiento de ejemplo: 20 %. Cada viaje lleva 12 m³ sueltos. Escribe (a) el volumen entre los perfiles, (b) cuántos m³ sueltos son, (c) cuántos viajes se necesitan, (d) qué haces si una guía nombra un botadero no autorizado.",
        "(a) Promedio 12 por 30 m son 360 m³. (b) 360 por 120 entre 100 son 432 m³ sueltos. (c) 432 entre 12 son 36 viajes. (d) No la doy por válida e informo al ITO.",
        ["promedia las áreas", "aplica el esponjamiento", "calcula los viajes", "informa el botadero no autorizado"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por 2", "usar m³ sueltos como si fueran en su lugar", "corregir la guía por cuenta propia"],
        "Pregunta: «¿cómo pasas de m³ en su lugar a m³ sueltos?». Si no responde, pídele que relea el ejemplo del esponjamiento."),
    reinforce="Inventa dos perfiles con sus áreas y la distancia entre ellos y calcula el volumen.",
    extend="Explica por qué se necesita contar guías de despacho para controlar el movimiento de tierra.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 12 (registro semanal de ejemplo, inventado). Camino «Las Vertientes» (ficticio). Programa de la semana: 1.500 m³ de corte, medidos en su lugar. Guías de despacho de la semana, cada viaje con 12 m³ de material suelto: lunes 20 viajes; martes 24; miércoles 18; jueves 0 (lluvia, sin trabajo según el libro de obra); viernes 22. "
     "Esponjamiento de ejemplo: 20 %. Excavadora 1: 45 horas pagadas en la semana; el parte diario registra 40 horas. Tarifa de ejemplo: $30.000 por hora.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel un registro semanal de movimiento de tierra: contar viajes, convertir volúmenes, comparar con el programa y detectar diferencias en horas.",
    prior=["Sé qué es el esponjamiento.", "Sé calcular porcentajes.", "Sé leer registros."],
    explain=[
        "En un caso de control se parte de los registros: las guías de despacho dicen cuántos viajes hubo y el parte diario dice cuántas horas trabajó cada máquina. Con los viajes se calcula el volumen suelto transportado: viajes por m³ de cada viaje. Para compararlo con el programa, que se mide en su lugar, se convierte: con un esponjamiento de ejemplo de 20 %, volumen en su lugar es volumen suelto por 100 y dividido por 120.",
        "Luego se calcula el porcentaje del programa cumplido y se comparan las horas pagadas con las registradas. Una diferencia sin respaldo es un hallazgo que se informa al ITO. Un día sin trabajo por lluvia no es un hallazgo si el libro de obra lo registra: después de la lluvia los taludes pueden estar inestables, así que nadie se acerca y la reanudación la deciden el ITO, el prevencionista y personal autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("volumen suelto", "volumen del material ya sacado, que ocupa más que en su lugar"), ("volumen en su lugar", "volumen del suelo antes de sacarlo"), ("programa", "plan de lo que debe ejecutarse en un período"), ("horas pagadas", "horas de máquina que se cobran"), ("horas registradas", "horas anotadas en el parte diario"), ("hallazgo", "diferencia o falta detectada en la verificación")],
    worked=[
        ("Convertir un volumen", "Se transportaron 240 m³ sueltos de ejemplo. Con esponjamiento de 20 %, ¿cuántos m³ eran en su lugar?", ["Los suelto son el 120 % del volumen original.", "240 por 100 entre 120 son 200."], "200 m³"),
        ("Diferencia de horas", "Una máquina de ejemplo tiene 30 horas pagadas y 26 registradas. ¿Cuántas horas no tienen respaldo?", ["Se resta lo registrado a lo pagado.", "30 menos 26 son 4."], "4 horas"),
    ],
    mistakes=[("Comparar los m³ sueltos de las guías directamente con el programa en su lugar.", "Son volúmenes que no se pueden comparar sin convertir.", "Convierte los m³ sueltos a m³ en su lugar con el esponjamiento."),
              ("Tratar el día de lluvia como una falta de la constructora sin mirar el libro de obra.", "El libro registra por qué no se trabajó.", "Revisa el registro antes de anotar un hallazgo.")],
    T=[
        ("abc", "En Obras Viales: ¿para qué se cuentan las guías de despacho de una semana?", "Para estimar el volumen movido y compararlo con lo programado", "Para decidir el precio de cada máquina", "Para dibujar el perfil transversal", "Las guías cuentan viajes y permiten estimar volumen; no definen precios ni dibujan perfiles."),
        ("abc", "¿Qué diferencia hay entre horas pagadas y horas registradas?", "Las pagadas son las que se cobran y las registradas son las anotadas en el parte diario", "Son lo mismo con otro nombre", "Las registradas son las del contrato y las pagadas las del libro de obra", "Se comparan precisamente porque pueden diferir y la diferencia sin respaldo es un hallazgo."),
        ("=", "Con un esponjamiento de ejemplo de 20 %, hay 180 m³ de material suelto. ¿Cuántos m³ eran en su lugar?", "180*100//120", "El suelto es 120 % del volumen original; se multiplica por 100 y se divide por 120.", " m³"),
        ("=", "{F} ¿Cuántos viajes se registraron en toda la semana?", "20+24+18+0+22", "Se suman los viajes de cada día.", " viajes"),
        ("=", "{F} ¿Cuántos m³ de material suelto se transportaron en la semana?", "84*12", "Se multiplican los 84 viajes por los 12 m³ de cada viaje.", " m³"),
        ("abc", "{F} ¿Por qué los 0 viajes del jueves no son un hallazgo?", "Porque el libro de obra registra que no se trabajó por lluvia", "Porque nunca se trabaja los jueves", "Porque los viajes del jueves se contaron el viernes", "El libro justifica el día sin trabajo; sin registro sí sería una diferencia."),
        ("=", "{F} Con el esponjamiento de ejemplo, ¿cuántos m³ en su lugar se movieron en la semana (1.008 m³ sueltos)?", "1008*100//120", "Se convierte el volumen suelto a volumen en su lugar.", " m³"),
        ("=", "{F} ¿Qué porcentaje del programa semanal se cumplió (840 m³ en su lugar)?", "840*100//1500", "Se divide lo ejecutado por lo programado y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué hallazgo corresponde por las horas de la excavadora 1?", "Hay 5 horas pagadas sin respaldo en el parte diario", "No hay hallazgo porque 45 es mayor que 40", "Hay 45 horas de más en el parte diario", "Se pagaron 45 horas y solo 40 están registradas, así que 5 no tienen respaldo."),
        ("ab", "{F} Para recuperar el atraso, el jefe de obra propone trabajar el jueves aunque el talud sigue húmedo. ¿Qué respuesta es correcta?", "No: tras la lluvia el talud puede estar inestable; nadie se acerca hasta que lo evalúen el ITO, el prevencionista y personal autorizado", "Sí: recuperar el atraso es más importante que esperar", "Un talud húmedo puede derrumbarse; la decisión de reanudar no la toma quien tiene el atraso."),
        ("abc", "{F} El jefe de obra declara 90 viajes en la semana, pero hay 84 guías. ¿Qué corresponde?", "Dar por verificados los 84 viajes respaldados e informar la diferencia al ITO", "Aceptar los 90 viajes declarados", "Promediar y aceptar 87 viajes", "Solo se verifica lo respaldado; el promedio no corresponde a ninguna evidencia."),
        ("=", "{F} ¿Cuánto suman, en pesos, las horas pagadas sin respaldo de la excavadora 1?", "5*30000", "Se multiplican las 5 horas sin respaldo por la tarifa de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuántos m³ en su lugar faltan para completar el programa semanal?", "1500-840", "Se resta lo ejecutado en su lugar al volumen programado.", " m³"),
    ],
    ctx=("abc", "Un operador de ejemplo le pide a un estudiante en práctica que «ajuste» el parte diario para que coincidan las horas pagadas. ¿Qué responde?", "Que no cambia registros y que la diferencia se informa al ITO", "Que lo ajusta si son pocas horas", "Que lo ajusta si lo hacen todos", "Un registro se corrige solo con una anotación fechada; modificarlo para que cuadre oculta la diferencia."),
    sc=[
        ("En Obras Viales: ¿cómo se pasa de m³ sueltos a m³ en su lugar?", "Se multiplica por 100 y se divide por 120 (con el 20 % de ejemplo)", "El volumen suelto es mayor que el volumen en su lugar."),
        ("¿Qué se hace con horas pagadas sin respaldo?", "Se registran como hallazgo e informan al ITO", "Una diferencia sin respaldo no se oculta ni se corrige por cuenta propia."),
        ("¿Se reanuda un trabajo cerca de un talud húmedo por lluvia solo porque hay atraso?", "No, lo decide personal autorizado tras evaluar el talud", "Un talud húmedo tras la lluvia puede derrumbarse sin aviso."),
    ],
    op=("Registro de ejemplo de «Camino El Boldo» (ficticio). Programa: 500 m³ en su lugar. Guías: 40 viajes de 12 m³ sueltos cada uno. Esponjamiento de ejemplo: 20 %. La excavadora tiene 20 horas pagadas y 18 registradas; la tarifa de ejemplo es $30.000 por hora. Escribe (a) cuántos m³ sueltos se transportaron, (b) cuántos m³ en su lugar son, (c) qué porcentaje del programa se cumplió, (d) cuánto suman las horas sin respaldo y qué haces.",
        "(a) 40 por 12 son 480 m³ sueltos. (b) 480 por 100 entre 120 son 400 m³. (c) 400 por 100 entre 500 son 80 %. (d) 2 horas por 30.000 son 60.000 pesos; las registro como hallazgo e informo al ITO.",
        ["calcula los m³ sueltos", "convierte a m³ en su lugar", "calcula el porcentaje", "calcula el monto e informa"],
        ["hoja con las cuatro respuestas"],
        ["no convertir el volumen", "olvidar informar al ITO", "modificar el parte diario"],
        "Pregunta: «¿por qué conviertes antes de comparar con el programa?». Si no responde, pídele que relea la regla del esponjamiento."),
    reinforce="Inventa un registro de cuatro días con viajes de 10 m³ y calcula cuántos m³ sueltos se movieron en total.",
    extend="Explica por qué un día sin trabajo por lluvia debe estar registrado en el libro de obra.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 13 (planilla de cubicación de ejemplo, inventada). Sector A del camino «Las Vertientes» (ficticio). Perfiles cada 20 m con áreas de corte: P0 12 m²; P1 16 m²; P2 20 m²; P3 24 m² (tres tramos de 20 m). "
     "Terraplén requerido en el sector: 1.100 m³ en su lugar. Esponjamiento de ejemplo: 20 %. Rendimiento de ejemplo de la excavadora: 60 m³ en su lugar por hora. Tarifa de ejemplo: $40.000 por hora de excavadora. Horas aprobadas en el presupuesto: 15.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: cubicar entre perfiles, equilibrar corte y terraplén y estimar horas y costos de máquina en una planilla.",
    prior=["Sé calcular el volumen entre dos perfiles.", "Sé aplicar el esponjamiento.", "Sé calcular horas con un rendimiento."],
    explain=[
        "Una planilla de cubicación calcula el volumen de cada tramo con el método de áreas medias y suma todos los tramos. Después se hace un balance entre corte y terraplén: se compara el volumen que entrega el corte con el que necesita el terraplén. Si el corte no alcanza, la diferencia se completa con material de préstamo, que es material traído de un lugar autorizado por el proyecto; si sobra, el sobrante va al botadero autorizado.",
        "Con el rendimiento de ejemplo se estiman las horas de máquina: horas = volumen dividido por rendimiento. El costo es horas por tarifa. Si el cálculo difiere de lo aprobado en el presupuesto, no se ajustan los números para que calcen: se informa la diferencia al ITO con el cálculo a la vista. Todos los valores son de ejemplo y sirven para calcular en papel.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("balance de corte y terraplén", "comparación entre el volumen que entrega el corte y el que necesita el terraplén"), ("material de préstamo", "material traído de un lugar autorizado cuando el corte no alcanza"), ("sobrante", "material que queda sin usar y va a un botadero autorizado"), ("tarifa", "valor de ejemplo por hora de máquina"), ("tramo", "parte del camino entre dos perfiles"), ("presupuesto", "documento que reúne los costos aprobados")],
    worked=[
        ("Balance", "Un corte de ejemplo entrega 900 m³ y el terraplén necesita 1.000 m³. ¿Cuánto material de préstamo falta?", ["Se resta lo disponible a lo necesario.", "1.000 menos 900 son 100."], "100 m³"),
        ("Costo de máquina", "Una máquina de ejemplo trabaja 12 horas a $35.000 la hora. ¿Cuánto cuesta?", ["Se multiplican las horas por la tarifa.", "12 por 35.000 son 420.000."], "$420.000"),
    ],
    mistakes=[("Ajustar las horas calculadas al presupuesto para que coincidan.", "Eso oculta una diferencia que puede ser importante.", "Informa la diferencia al ITO con el cálculo."),
              ("Usar material de préstamo de cualquier terreno cercano.", "El lugar de préstamo debe estar autorizado por el proyecto y la normativa ambiental.", "Usa solo el lugar autorizado y deja la guía de despacho.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es el método de áreas medias?", "Promediar las áreas de dos perfiles y multiplicar por la distancia entre ellos", "Sumar las dos áreas y dividir por la distancia", "Multiplicar las dos áreas entre sí", "El método promedia dos áreas y multiplica por la distancia; las otras opciones no representan un volumen."),
        ("abc", "¿Qué es el balance entre corte y terraplén?", "Comparar el volumen que entrega el corte con el que necesita el terraplén", "Comparar el precio del corte con el del terraplén", "Contar cuántos camiones tiene la obra", "El balance compara volúmenes para saber si sobra o falta material."),
        ("abc", "¿Qué es el material de préstamo?", "Material traído de un lugar autorizado cuando el corte no alcanza", "Material que se presta a otra obra sin registro", "Material sobrante que se lleva al botadero", "El préstamo completa lo que falta y debe venir de un lugar autorizado."),
        ("=", "{F} ¿Qué volumen de corte hay en el primer tramo, entre P0 y P1?", "(12+16)*20//2", "Se promedian las áreas de P0 y P1 y se multiplica por 20 m.", " m³"),
        ("=", "{F} ¿Qué volumen total de corte hay en los tres tramos?", "(12+16)*20//2+(16+20)*20//2+(20+24)*20//2", "Se calcula cada tramo con áreas medias y se suman.", " m³"),
        ("abc", "{F} Al comparar el corte con el terraplén requerido, ¿qué ocurre?", "El corte no alcanza y faltan 20 m³", "El corte alcanza y sobran 20 m³", "El corte alcanza justo", "El corte total es 1.080 m³ y se requieren 1.100 m³, así que faltan 20."),
        ("=", "{F} Con el rendimiento de ejemplo, ¿cuántas horas de excavadora se estiman para el volumen total de corte?", "1080//60", "Se divide el volumen del corte por lo que rinde la excavadora cada hora.", " horas"),
        ("=", "{F} ¿Cuál es el costo de esas horas de excavadora con la tarifa de ejemplo?", "18*40000", "Se multiplican las 18 horas por la tarifa por hora.", " pesos"),
        ("abc", "{F} Los 20 m³ de préstamo que faltan, ¿de dónde deben provenir?", "De un lugar autorizado por el proyecto, con su guía de despacho", "De cualquier terreno cercano que parezca adecuado", "Del botadero de la misma obra", "El préstamo debe estar autorizado y documentado; el botadero recibe sobrantes y no entrega material."),
        ("ab", "{F} Para estimar cuánto material suelto hay que transportar, un compañero resta 20 % a los 1.080 m³ de corte. ¿Qué respuesta es correcta?", "No: el suelto ocupa más, así que se suma 20 %, es decir, 1.296 m³", "Sí: al excavar el material pierde volumen", "El esponjamiento aumenta el volumen, no lo disminuye."),
        ("abc", "{F} Si el rendimiento de ejemplo baja a 40 m³ por hora, ¿qué ocurre con las horas y el costo del corte?", "Aumentan, porque se ejecuta menos por hora para el mismo volumen", "Disminuyen, porque el rendimiento es un número menor", "No cambian, porque el volumen es el mismo", "Con menos volumen por hora se necesitan más horas y, con la misma tarifa, más costo."),
        ("=", "{F} Con el rendimiento bajado a 40 m³ por hora, ¿cuánto costarían las horas de excavadora del corte?", "1080//40*40000", "Se calculan las horas con el nuevo rendimiento y se multiplican por la tarifa.", " pesos"),
        ("abc", "{F} El presupuesto aprueba 15 horas de excavadora y el cálculo da 18. ¿Qué corresponde?", "Informar la diferencia al ITO con el cálculo a la vista", "Usar 15 horas y no mencionar el cálculo", "Cambiar el rendimiento hasta que den 15 horas", "No se ajustan los datos para que calcen; la diferencia se informa con su respaldo."),
    ],
    ctx=("abc", "Un amigo de un estudiante ofrece vender «tierra barata» de un terreno cercano para completar un terraplén de ejemplo. ¿Qué responde?", "Que el material de préstamo debe venir de un lugar autorizado por el proyecto y con guía de despacho", "Que sirve si el precio es bajo", "Que sirve si nadie lo ve", "Solo se usa material de lugares autorizados y documentados."),
    sc=[
        ("En Obras Viales: ¿qué es el balance de corte y terraplén?", "La comparación del volumen del corte con el que necesita el terraplén", "El balance indica si sobra o si falta material en la obra."),
        ("¿Cómo se estiman las horas de una máquina con un rendimiento de ejemplo?", "Volumen dividido por rendimiento", "El rendimiento indica qué cantidad se ejecuta por cada hora."),
        ("¿Se ajustan los datos para que el cálculo coincida con el presupuesto?", "No, se informa la diferencia al ITO", "Ajustar datos para que calcen oculta información que es relevante."),
    ],
    op=("Planilla de ejemplo del «Camino El Boldo» (ficticio). Perfiles cada 10 m con áreas de corte: P0 6 m²; P1 10 m²; P2 14 m² (dos tramos de 10 m). Terraplén requerido: 250 m³ en su lugar. Rendimiento de ejemplo: 40 m³ por hora; tarifa de ejemplo $30.000 por hora. Escribe (a) el volumen de cada tramo y el total, (b) si el corte alcanza para el terraplén y cuánto falta o sobra, (c) las horas y el costo del corte, (d) de dónde sale el material de préstamo si falta.",
        "(a) Tramo 1: (6+10)*10/2 = 80 m³; tramo 2: (10+14)*10/2 = 120 m³; total 200 m³. (b) No alcanza: faltan 50 m³. (c) 200 entre 40 son 5 horas; 5 por 30.000 son 150.000 pesos. (d) De un lugar autorizado por el proyecto y con guía de despacho.",
        ["calcula cada tramo con áreas medias", "hace el balance", "calcula horas y costo", "indica el lugar autorizado"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por 2", "no comparar con el terraplén", "aceptar préstamo sin autorización"],
        "Pregunta: «¿cómo calculaste el volumen de un tramo?». Si no responde, pídele que relea el método de áreas medias."),
    reinforce="Calcula el volumen entre dos perfiles de áreas 5 y 9 m² separados 20 m.",
    extend="Explica qué harías si el cálculo de horas da más que lo aprobado en el presupuesto.",
)

# ============================================================ OAM-04, clase 1
F = ("Ficha 14 (obra de ejemplo, inventada). Camino «Las Vertientes» (ficticio). Partidas: cuneta revestida, 1.200 m; alcantarilla de cruce, 2 unidades; muro de contención, 60 m de largo; defensa fluvial con gaviones, 80 m de largo; protección de talud, 900 m². "
     "Riesgos anotados: derrumbe de zanja y de talud, caída a distinto nivel, crecida del río, atrapamiento y manejo de cargas.")
build(
    O4, 1, F,
    use="Aprenderé qué son los saneamientos, los muros de contención y las defensas fluviales y de talud, qué significa verificar sus faenas y qué riesgos y reglas de seguridad hay que reconocer.",
    prior=["Sé qué es una partida.", "Sé leer un itemizado.", "Sé qué hace el ITO."],
    explain=[
        "Los saneamientos de una vía son las obras que recogen y conducen el agua para que no dañe el camino: las cunetas, que son canales laterales; las alcantarillas, que son conductos por donde el agua cruza bajo el camino; y los colectores, que reúnen el agua de varias obras. Un muro de contención es una estructura que sostiene tierra. Una defensa fluvial protege el camino de la erosión de un río; un gavión es una caja de malla rellena de piedras que se usa en este tipo de defensa. Una defensa de talud protege la pendiente lateral del terreno.",
        "Verificar estas faenas es comprobar, con planos, especificaciones, registros e instrumental de medición, que lo construido corresponde a lo proyectado. Los riesgos son el derrumbe de zanjas y taludes, la caída a distinto nivel, la crecida del río, el atrapamiento y el manejo de cargas. Las reglas generales son no acercarse a zanjas, taludes ni orillas sin autorización, no entrar a un cauce, respetar la señalización y dejar el trabajo en terreno a personal capacitado, con EPP y acompañado. Cuidar el cauce y el entorno es parte de la norma vigente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("saneamiento", "obras que recogen y conducen el agua de una vía"), ("cuneta", "canal lateral que recoge el agua"), ("alcantarilla", "conducto por donde el agua cruza bajo el camino"), ("muro de contención", "estructura que sostiene tierra"), ("defensa fluvial", "obra que protege el camino de la erosión de un río"), ("gavión", "caja de malla rellena de piedras"), ("talud", "pendiente lateral de un corte o de un terraplén")],
    worked=[
        ("Elegir la obra", "Un camino de ejemplo necesita que el agua pase de un lado al otro por debajo de la calzada. ¿Qué obra corresponde?", ["El agua debe cruzar bajo el camino.", "Eso lo hace una alcantarilla."], "Una alcantarilla de cruce"),
        ("Monto de una partida", "Una cuneta de ejemplo de 300 m se paga a $10.000 por metro. ¿Cuál es el monto?", ["Se multiplica el largo por el precio.", "300 por 10.000 son 3.000.000."], "$3.000.000"),
    ],
    mistakes=[("Acercarse a la orilla de un río «solo a mirar» una defensa.", "La orilla puede ceder y una crecida es impredecible.", "Mantén distancia y deja la visita a personal autorizado y acompañado."),
              ("Dar por buena una obra de drenaje solo porque «se ve bien».", "La verificación necesita medidas y registros, no solo la apariencia.", "Compara lo construido con planos y especificaciones y registra los datos.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es una alcantarilla de cruce?", "Un conducto que permite que el agua pase bajo el camino", "Un canal lateral junto a la calzada", "Una estructura que sostiene tierra", "La alcantarilla cruza bajo el camino; el canal lateral es la cuneta y la estructura que sostiene tierra es el muro."),
        ("abc", "¿Qué es un gavión?", "Una caja de malla rellena de piedras que se usa en defensas", "Un canal que recoge el agua de la calzada", "Un instrumento para medir niveles", "El gavión es una caja de malla con piedras; el canal es la cuneta y el instrumento es otra cosa."),
        ("abc", "¿Para qué sirve una defensa fluvial?", "Para proteger el camino de la erosión de un río", "Para sostener la tierra de un corte", "Para recoger el agua de la calzada", "La defensa fluvial protege del río; sostener tierra es el muro y recoger agua es la cuneta."),
        ("=", "{F} ¿Cuántos metros de largo suman el muro de contención y la defensa fluvial?", "60+80", "Ambos se miden en metros de largo, así que se suman.", " m"),
        ("abc", "{F} ¿Qué partida de la ficha se mide en m²?", "La protección de talud", "La cuneta revestida", "La defensa fluvial", "La ficha da la protección de talud en m², una superficie; las otras se miden en metros."),
        ("abc", "{F} ¿Cuál de estos riesgos aparece anotado en la ficha?", "Crecida del río", "Descarga eléctrica en un tablero", "Intoxicación en un espacio confinado", "La ficha nombra la crecida del río; los otros riesgos no están anotados."),
        ("=", "{F} La cuneta se paga a $12.000 por metro (valor de ejemplo). ¿Cuál es el monto de la partida?", "1200*12000", "El monto es el largo por el precio de cada metro.", " pesos"),
        ("abc", "{F} Un visitante sin autorización quiere bajar a la orilla para «ver de cerca» los gaviones. ¿Qué corresponde?", "No hacerlo: la visita a terreno la hace personal autorizado, acompañado y con EPP", "Bajar si el río lleva poca agua", "Bajar si usa casco", "Una crecida o un derrumbe de la orilla no avisan; ni el poco caudal ni el casco reemplazan la autorización."),
        ("ab", "{F} Un compañero dice: «estudié la verificación de muros de contención, así que ya puedo entrar a una zanja a revisar». ¿Qué respuesta es correcta?", "No: entrar a una zanja exige autorización y control del riesgo de derrumbe, no basta con conocer la verificación", "Sí: quien sabe verificar puede entrar a una zanja", "Una zanja puede derrumbarse; conocer la verificación no es una autorización para entrar."),
        ("abc", "En una obra de ejemplo se derrumba la pared de una zanja y una persona queda atrapada. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a la zanja a sacarla de inmediato", "Tirar de la persona desde el borde mientras llega ayuda", "Entrar o acercarse al borde puede provocar un nuevo derrumbe; se avisa de inmediato y se mantiene distancia."),
        ("abc", "{F} El plano muestra 3 alcantarillas de cruce, pero el itemizado de la ficha pide 2 unidades. ¿Qué conclusión es la más prudente?", "Hay una diferencia entre documentos: se informa al proyectista o al ITO antes de verificar", "Se sigue el itemizado porque tiene precio", "Se sigue el plano porque es un dibujo", "Ningún documento manda por sí solo: la diferencia se informa a quien decide."),
        ("=", "{F} El muro de contención se paga a $250.000 por metro de largo (valor de ejemplo). ¿Cuál es el monto del muro?", "60*250000", "Se multiplica el largo del muro por el precio de cada metro.", " pesos"),
        ("abc", "{F} Antes de una visita autorizada a verificar, ¿qué conviene revisar en papel?", "Los riesgos anotados, las zonas donde no se puede entrar y los EPP exigidos", "Solo el itemizado de precios", "Solo el estado de pago", "Preparar la visita incluye conocer riesgos, zonas restringidas y EPP; los precios no protegen a nadie."),
    ],
    ctx=("abc", "Un vecino de ejemplo invita a un estudiante a «ayudar» a apilar piedras en la orilla del río para reforzar una defensa porque «es solo mover piedras». ¿Qué responde?", "Agradece y explica que esa faena exige personal capacitado y norma vigente, y que no está autorizado", "Acepta si trabaja con guantes", "Acepta si el río está bajo", "Intervenir un cauce exige capacitación y norma vigente; guantes o poco caudal no reemplazan eso."),
    sc=[
        ("En Obras Viales: ¿qué es una cuneta?", "Un canal lateral que recoge el agua", "La cuneta conduce el agua de la calzada lejos del camino."),
        ("¿Qué es un muro de contención?", "Una estructura que sostiene tierra", "El muro evita que la tierra se deslice hacia el camino."),
        ("¿Qué se hace ante un derrumbe con una persona atrapada?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse puede provocar otro derrumbe y más víctimas."),
    ],
    op=("Obra de ejemplo «Camino El Boldo» (ficticio): cuneta de 800 m, 2 alcantarillas, muro de contención de 40 m, defensa de talud de 500 m². Precio de ejemplo de la cuneta: $11.000 por metro. Escribe (a) qué obra lleva el agua bajo el camino, (b) el monto de la cuneta, (c) un riesgo de la obra y una medida de la jerarquía de controles, (d) qué haces si ves que alguien se acerca al borde de una zanja.",
        "(a) La alcantarilla de cruce. (b) 800 por 11.000 son 8.800.000 pesos. (c) Derrumbe de zanja: cercar y señalizar el borde para que nadie se acerque. (d) Le aviso que no se acerque y aviso a un adulto responsable; si hay un accidente, a emergencias.",
        ["nombra la obra correcta", "calcula el monto", "nombra riesgo y medida", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["confundir cuneta con alcantarilla", "acercarse a ayudar", "proponer solo el EPP"],
        "Pregunta: «¿qué diferencia hay entre una cuneta y una alcantarilla?». Si no responde, pídele que relea las definiciones."),
    reinforce="Dibuja un esquema simple de un camino con una cuneta, una alcantarilla y un muro de contención y rotula cada obra.",
    extend="Explica por qué el agua mal conducida puede dañar un camino aunque la calzada esté bien terminada.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 15 (planos de detalle de ejemplo, inventados). Alcantarilla A1: largo 20 m; cota de fondo de entrada 100 m; cota de fondo de salida 99 m; diámetro de ejemplo 80 cm. Cuneta C1: largo 500 m; cota inicial 120 m; cota final 115 m. "
     "Tolerancia de ejemplo para las cotas: 2 cm. Los planos de detalle de A1 están a escala 1:50.")
build(
    O4, 2, F,
    use="Aprenderé a leer planos de detalle y a calcular pendientes y tolerancias de obras de drenaje, con datos de ejemplo, para verificarlas en papel.",
    prior=["Sé qué es una cota.", "Sé qué es una escala.", "Sé calcular porcentajes."],
    explain=[
        "Un plano de detalle muestra con más precisión una obra pequeña, como una alcantarilla, con sus medidas. La cota de fondo es la altura del fondo de un canal o de un conducto. La pendiente es la inclinación de una obra y se calcula como desnivel dividido por longitud, por 100, para expresarla en porcentaje. El desnivel es la diferencia de cota entre el inicio y el final. Por ejemplo, un canal de 200 m que baja 4 m tiene una pendiente de 2 %. Si el final está más bajo que el inicio, el agua puede escurrir por gravedad.",
        "La tolerancia es la diferencia máxima que se acepta entre lo proyectado y lo medido; una medida cumple si su diferencia con el plano, sin importar el signo, es igual o menor que la tolerancia. Una diferencia fuera de tolerancia se registra e informa al ITO; no se corrige el plano ni la medida por cuenta propia. Los roles: el proyectista aclara el diseño, el topógrafo mide cotas, el ITO verifica y el prevencionista cuida la seguridad. Los valores de este cuaderno son de ejemplo, no reales.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("plano de detalle", "plano que muestra con más precisión una obra pequeña"), ("cota de fondo", "altura del fondo de un canal o conducto"), ("desnivel", "diferencia de cota entre el inicio y el final"), ("pendiente", "inclinación de una obra, desnivel dividido por longitud, en %"), ("tolerancia", "diferencia máxima aceptada entre lo proyectado y lo medido"), ("gravedad", "fuerza que hace escurrir el agua hacia lo más bajo")],
    worked=[
        ("Calcular una pendiente", "Una cuneta de ejemplo de 200 m baja 4 m desde el inicio hasta el final. ¿Cuál es su pendiente?", ["El desnivel es 4 m y la longitud 200 m.", "4 por 100 entre 200 son 2 por ciento."], "2 %"),
        ("Revisar una tolerancia", "Con una tolerancia de ejemplo de 2 cm, una cota medida difiere 1 cm del plano. ¿Cumple?", ["Se compara la diferencia con la tolerancia.", "1 cm es menor que 2 cm."], "Cumple"),
    ],
    mistakes=[("Calcular la pendiente como desnivel por longitud.", "La pendiente es una razón: se divide el desnivel por la longitud.", "Divide el desnivel entre la longitud y multiplica por 100."),
              ("Decir que −3 cm cumple una tolerancia de 2 cm porque es negativo.", "La tolerancia mira la diferencia sin importar el signo.", "Usa el valor absoluto: 3 cm es mayor que 2 cm y no cumple.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es la cota de fondo de una alcantarilla?", "La altura del fondo del conducto", "El diámetro del conducto", "El largo de la alcantarilla", "La cota es una altura; el diámetro y el largo son medidas de tamaño."),
        ("abc", "¿Cómo se calcula la pendiente de una cuneta?", "Desnivel dividido por longitud, por 100", "Longitud dividida por desnivel", "Desnivel multiplicado por longitud", "La pendiente compara cuánto baja con la distancia en que baja."),
        ("abc", "¿Qué es la tolerancia en una verificación?", "La diferencia máxima aceptada entre lo proyectado y lo medido", "La diferencia entre dos planos distintos", "El error del topógrafo que debe corregir", "La tolerancia fija cuánto puede alejarse lo medido del plano y aun así cumplir."),
        ("=", "{F} ¿Cuál es la pendiente de la alcantarilla A1?", "(100-99)*100//20", "El desnivel es 1 m en 20 m de largo; se divide y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la pendiente de la cuneta C1?", "(120-115)*100//500", "El desnivel es 5 m en 500 m de largo; se divide y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Por qué el agua puede escurrir por gravedad en la cuneta C1?", "Porque su cota final (115 m) es menor que la inicial (120 m)", "Porque su cota final es mayor que la inicial", "Porque tiene 500 m de largo", "El agua escurre hacia lo más bajo; el largo por sí solo no basta."),
        ("=", "{F} En el plano de detalle de A1, un tramo mide 4 cm. ¿Cuántos metros reales representa?", "4*50//100", "Se multiplica por 50 y se pasa de centímetros a metros dividiendo por 100.", " m"),
        ("abc", "{F} Un revisor mide la cota de fondo de salida de A1 y encuentra −3 cm respecto del plano. ¿Qué conclusión corresponde?", "No cumple, porque 3 cm supera la tolerancia de 2 cm", "Cumple, porque el signo es negativo", "Cumple, porque 3 cm es poco", "La tolerancia se compara con la diferencia sin signo: 3 es mayor que 2."),
        ("abc", "{F} El revisor encuentra que el plano de A1 parece tener un error de cota. ¿Quién aclara el diseño?", "El proyectista, a través del ITO", "El topógrafo, corrigiendo el plano", "El jefe de obra, decidiendo qué cota usar", "Solo el proyectista aclara el diseño; los demás informan y no corrigen el plano."),
        ("ab", "{F} Una compañera dice que la cuneta C1 tiene pendiente 5 % porque baja 5 m. ¿Qué respuesta es correcta?", "No: hay que dividir el desnivel por la longitud, y da 1 %", "Sí: la pendiente es igual a cuántos metros baja", "La pendiente es una razón entre el desnivel y la longitud, no el desnivel solo."),
        ("abc", "{F} Si la cuneta C1 se construyera con una pendiente menor que la proyectada, ¿qué consecuencia es posible?", "El agua podría escurrir más lento y acumularse", "El agua escurriría más rápido sin ningún problema", "No cambiaría nada porque la cuneta mide lo mismo", "Con menos pendiente la gravedad empuja menos y el agua tarda más en salir."),
        ("=", "{F} Si el plano pidiera que C1 tuviera una pendiente de 2 % en sus 500 m, ¿cuántos metros debería bajar de principio a fin?", "500*2//100", "Se multiplica la longitud por la pendiente y se divide por 100.", " m"),
        ("abc", "{F} Para el registro de verificación de A1, ¿qué debe incluir como mínimo?", "Cotas proyectadas y medidas de entrada y salida, la diferencia, la tolerancia, la fecha y quién midió", "Solo la palabra «ok»", "Solo la pendiente calculada", "Un registro útil reúne lo proyectado, lo medido, la diferencia, el criterio, la fecha y el responsable."),
    ],
    ctx=("abc", "Un estudiante de ejemplo mide con una huincha de juguete una cuneta de su barrio y quiere «corregirla» con pala. ¿Qué responde un adulto responsable?", "Que no intervenga la obra: medir en papel no habilita a modificarla y debe avisar al municipio o a quien la administra", "Que está bien si lo hace un domingo", "Que está bien si junta a sus amigos para ayudarlo", "Intervenir una obra pública exige autorización y capacitación; el día o la ayuda de otros no la reemplazan."),
    sc=[
        ("En Obras Viales: ¿cómo se calcula una pendiente?", "Desnivel dividido por longitud, por 100", "La pendiente compara cuánto baja con la distancia recorrida."),
        ("¿Cuándo cumple una medida frente a una tolerancia?", "Cuando su diferencia con el plano es igual o menor que la tolerancia", "La diferencia se mira sin importar el signo."),
        ("¿Qué se hace con una medida fuera de tolerancia?", "Se registra e informa al ITO", "El plano y la medida no se corrigen por cuenta propia."),
    ],
    op=("Planos de detalle de ejemplo de «Camino El Boldo» (ficticio). Alcantarilla A1: largo 40 m; cota de entrada 80 m y de salida 78 m. Cuneta C1: largo 300 m; cota inicial 60 m y final 57 m. Tolerancia de ejemplo: 2 cm. Una medición de la cota de salida de A1 difiere +3 cm del plano. Escribe (a) la pendiente de A1, (b) la pendiente de C1, (c) si la medición cumple la tolerancia y por qué, (d) a quién informas y qué registras.",
        "(a) 2 por 100 entre 40 son 5 %. (b) 3 por 100 entre 300 son 1 %. (c) No cumple: 3 cm es mayor que 2 cm. (d) Informo al ITO y registro cotas proyectadas y medidas, diferencia, tolerancia, fecha y quién midió.",
        ["calcula la pendiente de A1", "plantea la razón de C1", "compara con la tolerancia sin signo", "informa y registra"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar en vez de dividir", "decir que cumple por pocos centímetros", "corregir el plano por cuenta propia"],
        "Pregunta: «¿cómo se calcula la pendiente?». Si no responde, pídele que relea la definición de desnivel y longitud."),
    reinforce="Inventa una cuneta con su longitud y sus dos cotas y calcula su pendiente en porcentaje.",
    extend="Explica por qué una diferencia de 3 cm puede importar en una obra de drenaje aunque parezca pequeña.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 16 (lista de verificación de ejemplo, inventada). Camino «Las Vertientes» (ficticio). Tolerancia de ejemplo para cotas: 2 cm. Alcantarilla A1: diferencia con el plano en la cota de entrada +1 cm y en la de salida −3 cm. "
     "Alcantarilla A2: entrada 0 cm y salida +2 cm. Cuneta C1 en cinco tramos de 100 m, con pendiente mínima exigida de 1 % (de ejemplo) y pendientes medidas: T1 1 %, T2 2 %, T3 0 %, T4 1 %, T5 1 %. "
     "Muro M1 de 60 m: desviación de la vertical de 1 cm (tolerancia 2 cm), juntas registradas 6 de 6, informe de ensayo del hormigón presente y cumple. Defensa D1 de gaviones: 80 m construidos de 80 m proyectados; sin informe de ensayo del material de relleno.")
build(
    O4, 3, F,
    use="Aprenderé a analizar en papel una lista de verificación de saneamientos, muros y defensas: detectar mediciones fuera de tolerancia y respaldos faltantes, y resumir los hallazgos.",
    prior=["Sé calcular pendientes.", "Sé comparar una medida con una tolerancia.", "Sé qué es un hallazgo."],
    explain=[
        "Una lista de verificación de obras de drenaje, muros y defensas recoge, para cada obra, lo medido, lo proyectado y los respaldos. Una medición con tolerancia cumple si su diferencia con el plano, sin importar el signo, es igual o menor que la tolerancia; igualar la tolerancia cumple y superarla no. Una pendiente con mínimo exigido cumple si es igual o mayor que ese mínimo. Un respaldo, como un informe de ensayo, debe estar presente y cumplir.",
        "Cada diferencia o falta es un hallazgo y se registra con la obra, el dato, lo exigido, la fecha y quién lo detectó. Los hallazgos se informan al ITO; la decisión sobre cómo resolverlos la toman el ITO y el proyectista, y nadie corrige los datos para que cuadren. El resumen que se entrega debe ser fiel: nombra todos los hallazgos, no solo los más fáciles de explicar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("lista de verificación", "tabla con lo proyectado, lo medido y los respaldos de cada obra"), ("desviación de la vertical", "cuánto se aparta un muro de una línea perfectamente vertical"), ("junta", "separación planificada entre partes de un muro"), ("tramo", "parte de una obra con medición propia"), ("informe de ensayo", "documento del laboratorio con resultados medidos"), ("hallazgo", "diferencia o falta detectada")],
    worked=[
        ("Medición con tolerancia", "Con una tolerancia de ejemplo de 2 cm, una medida difiere +2 cm del plano. ¿Cumple?", ["Se compara 2 con la tolerancia de 2.", "Igualar la tolerancia cumple."], "Cumple"),
        ("Pendiente con mínimo", "Un tramo de ejemplo exige pendiente mínima de 1 % y mide 0 %. ¿Cumple?", ["Un mínimo se iguala o se supera.", "0 es menor que 1."], "No cumple"),
    ],
    mistakes=[("Decir que +2 cm no cumple una tolerancia de 2 cm porque «llega al límite».", "Igualar la tolerancia cumple; solo superarla no cumple.", "Compara la diferencia con la tolerancia: igual o menor cumple."),
              ("Resumir «en general todo cumple» cuando hay hallazgos.", "El resumen debe ser fiel a la lista.", "Nombra todos los hallazgos con su dato y su obra.")],
    T=[
        ("abc", "En Obras Viales: ¿cuándo cumple una medición frente a una tolerancia?", "Cuando su diferencia con el plano, sin signo, es igual o menor que la tolerancia", "Cuando su diferencia es negativa", "Solo cuando la diferencia es exactamente cero", "La tolerancia admite diferencias hasta cierto límite y se mira sin signo."),
        ("abc", "En una lista de verificación, ¿qué significa una diferencia de «+1 cm»?", "La medida es 1 cm mayor que la del plano", "La medida es 1 cm menor que la del plano", "La medida es el 1 % de la tolerancia", "El signo positivo indica que la medida supera a la del plano."),
        ("abc", "Una medida de ejemplo queda fuera de tolerancia. ¿Qué corresponde?", "Registrarla e informar al ITO", "Cambiarla en la lista por un valor dentro de tolerancia", "Esperar a que nadie lo note", "Un hallazgo se registra y se informa; la lista no se modifica para que cuadre."),
        ("=", "{F} ¿Cuántos cm se pasa la cota de salida de A1 de la tolerancia?", "3-2", "Se resta la tolerancia a la diferencia medida sin signo.", " cm"),
        ("abc", "{F} ¿Qué mediciones de cota de la alcantarilla A2 cumplen la tolerancia?", "Ambas, entrada y salida", "Solo la entrada", "Ninguna", "La entrada tiene 0 cm y la salida +2 cm, que iguala la tolerancia y cumple."),
        ("abc", "{F} ¿Qué tramo de la cuneta C1 no cumple la pendiente mínima exigida?", "T3, con 0 %", "T1, con 1 %", "T2, con 2 %", "T3 queda bajo el mínimo de 1 %; T1 lo iguala y T2 lo supera."),
        ("=", "{F} ¿Qué porcentaje de los tramos de la cuneta C1 cumple la pendiente mínima?", "4*100//5", "Cumplen 4 de 5 tramos: se divide entre 5 y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué hallazgo corresponde para la defensa D1?", "Falta el informe de ensayo del material de relleno", "La defensa mide menos de lo proyectado", "La defensa tiene demasiadas piedras", "D1 coincide en largo con el proyecto; lo que falta es el informe de ensayo."),
        ("abc", "{F} ¿Qué conclusión corresponde para el muro M1?", "Conforme: su desviación está dentro de la tolerancia, tiene las 6 juntas y el informe cumple", "Con hallazgo: tiene desviación", "Con hallazgo: falta una junta", "La desviación de 1 cm es menor que 2 cm, hay 6 de 6 juntas y el informe cumple."),
        ("ab", "{F} Un compañero dice que A2 no cumple porque +2 cm «llega» a la tolerancia de 2 cm. ¿Qué respuesta es correcta?", "No: igualar la tolerancia cumple, solo superarla no cumple", "Sí: debe quedar por debajo de la tolerancia", "La tolerancia fija un límite que se puede igualar; superarlo es lo que no cumple."),
        ("abc", "{F} El jefe de obra pide registrar la salida de A1 como −2 cm «para que cuadre». ¿Qué corresponde?", "Mantener el −3 cm medido e informar la diferencia al ITO", "Aceptar el −2 cm porque lo pide el jefe de obra", "Promediar −3 y −2 cm", "Una medida no se modifica por pedido de quien tiene interés en el resultado."),
        ("abc", "{F} Si la tolerancia fuera de 3 cm en vez de 2 cm, ¿cuántas de las 4 mediciones de cota de A1 y A2 cumplirían?", "Las 4", "3 de 4", "2 de 4", "Las diferencias son 1, 3, 0 y 2 cm, y todas son iguales o menores que 3."),
        ("abc", "{F} Para el informe al ITO sobre la lista, ¿qué resumen es fiel?", "Hay 3 hallazgos: la cota de salida de A1, el tramo T3 de C1 y el informe faltante de D1", "En general todo cumple", "Hay 1 hallazgo: el informe de D1", "El resumen debe nombrar todos los hallazgos de la lista, no solo uno."),
    ],
    ctx=("abc", "Una estudiante en práctica nota que el tramo T3 de una cuneta no cumple, y el jefe de obra le dice que «seguro con la lluvia se arregla solo». ¿Qué hace?", "Registra el hallazgo y lo informa al ITO", "No lo registra para no atrasar la obra", "Lo registra solo si vuelve a llover", "Un hallazgo se registra e informa independiente de lo que se espere que ocurra después."),
    sc=[
        ("En Obras Viales: ¿cumple una medición que justo iguala la tolerancia?", "Sí, igualar la tolerancia cumple", "Solo la diferencia mayor que la tolerancia incumple."),
        ("¿Qué datos lleva el registro de un hallazgo?", "La obra, el dato, lo exigido, la fecha y quién lo detectó", "Esos datos permiten ubicar y revisar el problema."),
        ("¿Se cambia un dato para que la lista cuadre?", "No, se informa la diferencia al ITO", "Cambiar datos oculta información que es necesaria para decidir."),
    ],
    op=("Lista de verificación de ejemplo de «Camino El Boldo» (ficticio). Tolerancia de ejemplo: 2 cm. Alcantarilla A1: entrada −1 cm, salida +4 cm. Cuneta C1 con pendiente mínima de 1 % en cuatro tramos medidos: 2 %, 1 %, 0 % y 1 %. Muro M1: juntas registradas 5 de 6; informe de ensayo presente y cumple. Escribe (a) qué mediciones de A1 cumplen, (b) qué porcentaje de los tramos de C1 cumple, (c) qué hallazgos hay en M1, (d) cómo resumes la lista al ITO.",
        "(a) Solo la entrada (1 cm); la salida (4 cm) supera los 2 cm. (b) 3 de 4 son 75 %. (c) Falta registrar una junta (5 de 6). (d) Hay 3 hallazgos: la salida de A1, el tramo de 0 % de C1 y la junta sin registrar de M1.",
        ["compara con la tolerancia sin signo", "calcula el porcentaje", "detecta la junta faltante", "resume todos los hallazgos"],
        ["hoja con las cuatro respuestas"],
        ["usar el signo para decidir", "omitir un hallazgo", "decir que todo cumple"],
        "Pregunta: «¿cuántos hallazgos hay en total?». Si no responde, pídele que repase cada obra una por una."),
    reinforce="Inventa una lista con una alcantarilla, una cuneta y un muro, y marca qué cumple y qué es hallazgo.",
    extend="Explica por qué un resumen que omite un hallazgo menor puede causar un problema mayor más adelante.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 17 (planilla de ejemplo, inventada). Camino «Las Vertientes» (ficticio). Muro de contención M1: largo 60 m; altura 3 m; espesor 30 cm; hormigón colocado a $120.000 por m³ (valor de ejemplo). "
     "Defensa fluvial D1: largo 80 m; cada gavión mide 2 m de largo; se disponen 3 hileras (filas) a lo largo; $60.000 por gavión. Protección de talud: 900 m² a $9.000 por m². Cuneta C1: 900 m a $11.000 por metro.")
build(
    O4, 4, F,
    use="Aprenderé a cubicar y presupuestar en una planilla de ejemplo un muro, una defensa de gaviones, una protección de talud y una cuneta, y a verificar el resultado contra lo aprobado.",
    prior=["Sé calcular volúmenes y montos.", "Sé pasar centímetros a metros.", "Sé comparar un cálculo con un presupuesto."],
    explain=[
        "Cubicar es calcular las cantidades de una partida. El volumen de un muro con forma de prisma es largo por altura por espesor, con todas las medidas en metros; si el espesor está en centímetros se divide por 100. La cantidad de gaviones se calcula con el largo de la defensa dividido por el largo de cada gavión, que da los gaviones de una hilera, y se multiplica por el número de hileras, que son las filas dispuestas a lo largo. Una superficie se calcula con largo por ancho y se mide en m².",
        "El monto de una partida es la cantidad por el precio unitario y el total de la obra es la suma de los montos. Si el total calculado difiere del presupuesto aprobado, no se ajustan las cantidades para que calcen: la diferencia se informa al ITO con el detalle del cálculo. Todos los números son de ejemplo y sirven para calcular en papel, no para construir.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular las cantidades de una partida"), ("prisma", "cuerpo con forma de caja, cuyo volumen es largo por ancho por altura"), ("hilera", "fila de gaviones dispuesta a lo largo de la defensa"), ("espesor", "medida del grosor de un muro"), ("monto", "cantidad por precio unitario"), ("presupuesto aprobado", "monto que el mandante autorizó")],
    worked=[
        ("Volumen de un muro", "Un muro de ejemplo mide 20 m de largo, 2 m de alto y 25 cm de espesor. ¿Cuántos m³ tiene?", ["El espesor es 25 dividido por 100 metros.", "20 por 2 por 25 son 1.000; entre 100 son 10."], "10 m³"),
        ("Cantidad de piezas", "Una defensa de ejemplo de 30 m usa piezas de 2 m y 2 hileras. ¿Cuántas piezas necesita?", ["Por hilera: 30 entre 2 son 15.", "Con 2 hileras: 15 por 2 son 30."], "30 piezas"),
    ],
    mistakes=[("Multiplicar el espesor en centímetros directamente por largo y altura en metros.", "Las tres medidas deben estar en la misma unidad.", "Pasa los centímetros a metros dividiendo por 100 antes de multiplicar."),
              ("Olvidar multiplicar por el número de hileras al contar gaviones.", "Cada hilera necesita sus propios gaviones.", "Calcula los gaviones de una hilera y multiplica por las hileras.")],
    T=[
        ("abc", "En Obras Viales: ¿cómo se calcula el volumen de un muro con forma de prisma?", "Largo por altura por espesor, con las medidas en metros", "Largo más altura más espesor", "Largo por altura, sin el espesor", "El volumen necesita las tres dimensiones multiplicadas; sumar o ignorar una da otra magnitud."),
        ("abc", "El espesor de un muro está en centímetros y el largo y la altura en metros. ¿Qué se hace antes de multiplicar?", "Se divide el espesor por 100", "Se multiplica el espesor por 100", "Se deja igual porque da lo mismo", "Un metro tiene 100 cm; las tres medidas deben estar en metros."),
        ("abc", "¿Cómo se calcula la cantidad de gaviones de una defensa con varias hileras?", "Largo dividido por el largo de cada gavión, por el número de hileras", "Largo multiplicado por el número de hileras", "Largo dividido por el número de hileras", "Primero se obtienen los gaviones de una hilera y luego se multiplican por las hileras."),
        ("=", "{F} ¿Cuántos m³ tiene el muro de contención M1?", "60*3*30//100", "Se multiplican largo, altura y espesor en metros (30 cm son 30/100 m).", " m³"),
        ("=", "{F} ¿Cuál es el monto del hormigón del muro M1?", "54*120000", "Se multiplican los 54 m³ por el precio de cada m³.", " pesos"),
        ("=", "{F} ¿Cuántos gaviones entran en una hilera de la defensa D1?", "80//2", "Se divide el largo de la defensa por el largo de cada gavión.", " gaviones"),
        ("=", "{F} ¿Cuántos gaviones necesita la defensa D1 en total?", "(80//2)*3", "Se multiplican los gaviones de una hilera por las 3 hileras.", " gaviones"),
        ("=", "{F} ¿Cuál es el monto de la protección de talud?", "900*9000", "Se multiplican los m² por el precio de cada m².", " pesos"),
        ("abc", "{F} Llegan gaviones de 4 m de largo, pero el diseño de D1 especifica gaviones de 2 m. ¿Qué corresponde?", "Informar la diferencia al proyectista o al ITO antes de aceptar la entrega", "Aceptarlos porque son más grandes", "Aceptarlos y recalcular la cantidad sin avisar", "Cambiar una pieza especificada altera el diseño; se informa a quien lo decide."),
        ("ab", "{F} Un compañero calcula el volumen del muro como 60 por 3 por 30 y obtiene 5.400 m³. ¿Qué respuesta es correcta?", "No: el espesor está en cm y hay que dividir por 100, lo que da 54 m³", "Sí: 5.400 m³ es el volumen correcto", "El espesor debe pasarse a metros antes de multiplicar; así el resultado es 54 m³."),
        ("abc", "{F} El volumen de hormigón realmente medido del muro resulta mayor que el calculado. ¿Qué conclusión es la más prudente?", "Revisar las medidas y el cálculo e informar la diferencia al ITO", "Concluir que el muro quedó mejor", "Reducir el volumen medido para que coincida", "Una diferencia puede ser un error de medida o de cálculo; se revisa y se informa."),
        ("=", "{F} ¿Cuál es el monto total de las cuatro partidas: muro, defensa, talud y cuneta?", "54*120000+120*60000+900*9000+900*11000", "Se calcula el monto de cada partida y se suman.", " pesos"),
        ("abc", "{F} El presupuesto aprobado para estas cuatro partidas es de $31.000.000 y el cálculo da $31.680.000. ¿Qué corresponde?", "Informar la diferencia al ITO con el detalle del cálculo", "Reducir una cantidad hasta que coincida", "Usar el presupuesto aprobado sin avisar", "No se ajustan los datos para que calcen: la diferencia se informa con su respaldo."),
    ],
    ctx=("abc", "Una estudiante de ejemplo encuentra un error de cálculo propio en una planilla que ya entregó al ITO. ¿Qué hace?", "Avisa al ITO del error y entrega la planilla corregida con la fecha real", "Lo deja así porque ya la entregó", "Cambia la planilla del archivo sin avisar", "Un error propio se informa y se corrige dejando registro; ocultarlo o cambiarlo sin aviso es peor."),
    sc=[
        ("En Obras Viales: ¿cómo se calcula el volumen de un muro?", "Largo por altura por espesor, en metros", "Se necesitan las tres dimensiones en la misma unidad."),
        ("¿Cómo se calcula la cantidad de gaviones con varias hileras?", "Gaviones de una hilera por el número de hileras", "Cada hilera necesita su propia cantidad de gaviones."),
        ("¿Se ajustan las cantidades para que coincidan con el presupuesto?", "No, se informa la diferencia al ITO", "Ajustar cantidades oculta una diferencia que importa."),
    ],
    op=("Planilla de ejemplo de «Camino El Boldo» (ficticio). Muro M1: largo 40 m, altura 2 m, espesor 25 cm, hormigón a $100.000 por m³. Defensa D1: largo 60 m con gaviones de 2 m y 2 hileras, a $55.000 por gavión. Escribe (a) el volumen del muro, (b) el monto del hormigón, (c) cuántos gaviones necesita D1 y su monto, (d) qué haces si el total supera el presupuesto aprobado.",
        "(a) 40 por 2 por 25 son 2.000; entre 100 son 20 m³. (b) 20 por 100.000 son 2.000.000 pesos. (c) 60 entre 2 son 30 por hilera; con 2 hileras son 60 gaviones; 60 por 55.000 son 3.300.000 pesos. (d) Informo la diferencia al ITO con el detalle del cálculo; no ajusto cantidades.",
        ["pasa los cm a m", "calcula el monto", "multiplica por las hileras", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["no dividir el espesor por 100", "olvidar las hileras", "ajustar cantidades para que calcen"],
        "Pregunta: «¿cuántas hileras tiene la defensa y cómo las usaste?». Si no responde, pídele que relea el cálculo de gaviones."),
    reinforce="Calcula el volumen de un muro de ejemplo de 10 m de largo, 2 m de alto y 20 cm de espesor.",
    extend="Explica por qué cambiar el largo de una pieza especificada puede afectar la cantidad y el costo de una defensa.",
)

# ============================================================ OAM-04, clase 5
F = ("Ficha 18 (alternativas de ejemplo, inventadas). Defensa fluvial de 80 m de largo. Alternativa A (gaviones): $400.000 por metro, vida útil de ejemplo 20 años, mantención de $5.000 por metro al año. "
     "Alternativa B (enrocado, es decir, piedras grandes apiladas): $350.000 por metro, vida útil de ejemplo 10 años, mantención de $10.000 por metro al año. "
     "Alternativa C (muro de hormigón): $700.000 por metro, vida útil de ejemplo 40 años, mantención de $2.000 por metro al año. Informe del proyectista (de ejemplo): A y C son adecuadas; B no. Presupuesto disponible: $40.000.000.")
build(
    O4, 5, F,
    use="Aprenderé a comparar alternativas de defensa fluvial con un requisito de calidad primero y con costos de ejemplo después, y a verificar la calidad con una lista de verificación.",
    prior=["Sé qué es un requisito excluyente.", "Sé calcular costos totales.", "Sé qué es una lista de verificación."],
    explain=[
        "Al comparar alternativas de una obra se aplica primero el requisito excluyente: el informe del proyectista dice cuáles son adecuadas, y la que no lo es queda fuera aunque sea más barata. Con las que pasan se comparan el costo inicial, que es el precio por el largo, y el costo anual equivalente, que en este cuaderno es una forma simple: costo inicial dividido por la vida útil, más la mantención de un año. La vida útil es el número de años durante los cuales se espera que la obra cumpla su función; aquí es un dato de ejemplo.",
        "Además hay que mirar el presupuesto disponible: una alternativa que lo supera no se puede elegir sin una decisión del mandante. La elección final la toma el mandante con el proyectista y el ITO. Para verificar la calidad de la alternativa elegida se usa una lista de verificación con el informe del proyectista, los informes de ensayo del material, los registros del libro de obra y las medidas contra el plano. Todos los números son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("costo inicial", "precio por metro por el largo de la obra"), ("vida útil", "años durante los cuales se espera que la obra cumpla su función"), ("mantención", "gasto anual para conservar la obra"), ("costo anual equivalente", "costo inicial dividido por la vida útil, más la mantención de un año"), ("enrocado", "defensa hecha con piedras grandes apiladas"), ("presupuesto disponible", "monto máximo que el mandante puede gastar")],
    worked=[
        ("Costo anual equivalente", "Una obra de ejemplo cuesta $600.000 por metro, tiene vida útil de 30 años y mantención de $1.000 por metro al año. ¿Cuál es su costo anual equivalente por metro?", ["Se divide 600.000 entre 30: 20.000.", "Se suma la mantención: 21.000."], "$21.000 por metro al año"),
        ("Aplicar el filtro", "Dos alternativas de ejemplo: X tiene informe del proyectista aprobado y Z no. Z es más barata. ¿Cuál se compara?", ["Primero se aplica el requisito excluyente.", "Z no lo cumple y queda fuera."], "Solo X"),
    ],
    mistakes=[("Elegir la alternativa más barata antes de ver si el proyectista la aprobó.", "El informe del proyectista es un requisito excluyente.", "Aplica primero el filtro y compara después solo las que pasan."),
              ("Comparar solo el costo inicial.", "Una alternativa barata puede durar menos y costar más al año.", "Compara también el costo anual equivalente y revisa el presupuesto disponible.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es la vida útil de una obra de defensa?", "Los años durante los cuales se espera que cumpla su función", "Los años que tardó en construirse", "Los años de garantía que paga la constructora", "La vida útil mide cuánto se espera que dure su función; no es el plazo de construcción ni una garantía."),
        ("abc", "¿Qué es el costo anual equivalente simple de este cuaderno?", "El costo inicial dividido por la vida útil, más la mantención de un año", "El costo inicial multiplicado por la vida útil", "La mantención de un año dividida por la vida útil", "Reparte el costo inicial en los años de vida útil y suma el gasto anual de mantención."),
        ("abc", "Al comparar alternativas, ¿qué se aplica primero?", "El requisito excluyente, como el informe del proyectista", "El precio más bajo", "La vida útil más larga", "El filtro de calidad va antes de comparar costos o duración."),
        ("=", "{F} ¿Cuál es el costo inicial de la alternativa A para los 80 m?", "400000*80", "Se multiplica el precio por metro por el largo de la defensa.", " pesos"),
        ("=", "{F} ¿Cuál es el costo inicial de la alternativa C para los 80 m?", "700000*80", "Se multiplica el precio por metro por el largo de la defensa.", " pesos"),
        ("abc", "{F} ¿Qué alternativa queda fuera por el informe del proyectista?", "La alternativa B", "La alternativa A", "La alternativa C", "El informe dice que A y C son adecuadas y que B no lo es."),
        ("=", "{F} ¿Cuál es el costo anual equivalente por metro de la alternativa A?", "400000//20+5000", "Se divide el costo por metro entre la vida útil y se suma la mantención anual.", " pesos"),
        ("=", "{F} ¿Cuál es el costo anual equivalente por metro de la alternativa C?", "700000//40+2000", "Se divide el costo por metro entre la vida útil y se suma la mantención anual.", " pesos"),
        ("abc", "{F} Entre las alternativas que pasan el filtro, ¿cuáles caben en el presupuesto disponible de $40.000.000?", "Solo la alternativa A", "Solo la alternativa C", "Las dos, A y C", "A cuesta 32.000.000 y C cuesta 56.000.000, que supera el presupuesto."),
        ("ab", "{F} Un compañero dice que C es mejor porque su costo anual por metro es menor y que por eso se elige. ¿Qué respuesta es correcta?", "No es suficiente: también se mira el presupuesto disponible y la decisión la toma el mandante", "Sí: el menor costo anual decide siempre", "El costo anual es solo un criterio más y C supera el presupuesto disponible."),
        ("abc", "{F} Si la vida útil de A fuera de 10 años en vez de 20, ¿qué pasaría con su costo anual por metro?", "Aumentaría, porque el costo inicial se repartiría en menos años", "Disminuiría, porque la vida útil es un número menor", "No cambiaría, porque el precio es el mismo", "Dividir el mismo costo entre menos años da un costo anual mayor."),
        ("=", "{F} ¿Cuántos pesos al año se ahorran, para los 80 m, con C en comparación con A?", "(25000-19500)*80", "Se multiplica la diferencia de costo anual por metro por el largo de 80 m.", " pesos"),
        ("abc", "{F} Antes de aprobar la alternativa elegida, ¿qué verificación de calidad corresponde en papel?", "Una lista con el informe del proyectista, los informes de ensayo, los registros del libro de obra y las medidas contra el plano", "Solo una fotografía de la obra terminada", "Solo la firma del jefe de obra", "La calidad se verifica con varias evidencias contrastadas, no con una foto ni con una firma."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece a un estudiante en práctica un regalo si «ayuda» a que su alternativa B sea considerada pese al informe del proyectista. ¿Qué responde?", "Rechaza el regalo e informa a su supervisor, porque las alternativas se evalúan con el requisito excluyente", "Acepta si no cambia ningún número", "Acepta y propone un descuento", "Aceptar regalos compromete la imparcialidad; el informe del proyectista no se negocia."),
    sc=[
        ("En Obras Viales: ¿qué se aplica primero al comparar alternativas?", "El requisito excluyente, como el informe del proyectista", "Si no cumple, queda fuera aunque sea más barata."),
        ("¿Cómo se calcula el costo anual equivalente simple?", "Costo inicial dividido por vida útil, más mantención anual", "Reparte el costo inicial en los años de vida útil."),
        ("¿Quién decide si una alternativa supera el presupuesto disponible?", "El mandante, con el proyectista y el ITO", "La constructora no puede decidir sola sobre el presupuesto."),
    ],
    op=("Alternativas de ejemplo para una defensa de 50 m. X (gaviones): $300.000 por metro, vida útil de ejemplo 20 años, mantención de $4.000 por metro al año; el proyectista la aprueba. Y (enrocado): $200.000 por metro, vida útil de ejemplo 10 años, mantención de $8.000 por metro al año; el proyectista no la aprueba. Presupuesto disponible: $20.000.000. Escribe (a) qué alternativa queda fuera y por qué, (b) el costo inicial de X, (c) su costo anual equivalente por metro, (d) si X cabe en el presupuesto.",
        "(a) Y, porque el proyectista no la aprueba, aunque sea más barata. (b) 300.000 por 50 son 15.000.000 pesos. (c) 300.000 entre 20 son 15.000; más 4.000 son 19.000 por metro al año. (d) Sí, 15.000.000 es menor que 20.000.000.",
        ["aplica primero el filtro", "calcula el costo inicial", "calcula el costo anual equivalente", "compara con el presupuesto"],
        ["hoja con las cuatro respuestas"],
        ["elegir por el precio más bajo", "olvidar sumar la mantención", "ignorar el presupuesto disponible"],
        "Pregunta: «¿qué haces primero, comparar costos o mirar el informe del proyectista?». Si no responde, pídele que relea el requisito excluyente."),
    reinforce="Escribe dos criterios excluyentes y dos criterios de comparación para elegir una defensa fluvial, con tus palabras.",
    extend="Explica con un ejemplo inventado cuándo una alternativa más cara al inicio puede costar menos al año.",
)

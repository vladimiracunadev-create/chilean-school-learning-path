"""Obras Viales e Infraestructura TP 4.º medio: OAM-05 (verificar faenas de producción, transporte, colocación y compactación), OAM-06 (seguridad en la vía) y OAM-07 (conservación y mantenimiento). Solo conceptos, documentos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_coov_common import AVISO, EMER, build

O5 = "TP-COOV-4-OAM-05"
O6 = "TP-COOV-4-OAM-06"
O7 = "TP-COOV-4-OAM-07"

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Camino rural ficticio «Ruta Lomas», tramo de 1.800 m. Documentos de la faena: plano de trazado (1 lámina), especificaciones técnicas (8 páginas), "
     "guías de despacho (una por cada viaje de camión), bitácora de obra (1 cuaderno) y plan de prevención de riesgos (5 páginas). Se usan 4 camiones tolva y, el día de la ficha, cada camión hizo 6 viajes. "
     "Cada viaje trae 12 m³ de material de ejemplo. Riesgos anotados: atropello, atrapamiento por maquinaria, vuelco, polvo y ruido.")
build(
    O5, 1, F,
    use="Aprenderé qué son las faenas de producción, transporte, colocación y compactación de una obra vial, qué documentos las respaldan y qué riesgos hay que reconocer antes de verificarlas.",
    prior=["Sé leer una tabla y un plano simple.", "Sé sumar, multiplicar y dividir números enteros.", "Sé que un trabajo se registra por escrito."],
    explain=[
        "En una obra vial de mediana envergadura el material se prepara y se pone en el camino por etapas, llamadas faenas. La producción es preparar el material en una planta. El transporte lo lleva hasta la obra en camiones. La colocación lo pone sobre el trazado, que es la línea y la medida del camino marcadas en el plano. La compactación hace que el material quede más denso y firme. Verificar una faena es comparar lo que se hizo con el plano y las especificaciones, y dejarlo anotado.",
        "Cada faena deja documentos: el plano de trazado, las especificaciones técnicas, la guía de despacho de cada viaje, la bitácora (cuaderno donde se anotan los hechos del día) y el plan de prevención de riesgos. Los riesgos más comunes son el atropello, el atrapamiento entre equipos y el vuelco de vehículos. La jerarquía de controles ordena las medidas: primero eliminar el peligro, luego sustituirlo, después proteger con barreras o separar zonas, luego organizar el trabajo y, al final, usar elementos de protección personal (EPP).",
        f"El manual de carretera y la norma vigente fijan lo que se exige; aquí no se usan valores reales. {EMER} {AVISO}",
    ],
    vocab=[("faena", "etapa de trabajo de una obra"), ("trazado", "línea y medidas del camino marcadas según el plano"), ("guía de despacho", "documento que respalda cada viaje de material"), ("bitácora", "cuaderno donde se anotan los hechos del día en la obra"), ("camión tolva", "camión con caja que se inclina para descargar material"), ("atropello", "golpe de un vehículo o equipo a una persona"), ("vuelco", "caída de un vehículo de lado o de espaldas"), ("atrapamiento", "aprisionamiento de una persona entre equipos o contra una estructura"), ("EPP", "elementos de protección personal, como casco y chaleco"), ("jerarquía de controles", "orden de las medidas de seguridad, de la más eficaz a la menos eficaz")],
    worked=[
        ("Elegir el documento", "Un jefe de faena de ejemplo quiere comprobar cuántos metros cúbicos entregó un camión en un solo viaje. ¿Qué documento revisa?", ["Cada viaje se respalda con un documento propio.", "Ese documento es la guía de despacho."], "La guía de despacho"),
        ("Contar viajes", "Dos camiones de otra obra de ejemplo hicieron 5 viajes cada uno. ¿Cuántos viajes suman?", ["Se multiplican los camiones por los viajes de cada uno.", "2 por 5 son 10."], "10 viajes"),
    ],
    mistakes=[("Acercarse a un camión que retrocede para «guiarlo» sin ser el encargado autorizado.", "Quien está detrás del vehículo puede ser atropellado.", "Mantente fuera de la zona de maniobra y avisa al supervisor."),
              ("Creer que verificar en papel una faena habilita para operar los equipos.", "Operar maquinaria exige autorización y capacitación.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En una obra vial: ¿qué documento respalda cada viaje de material que llega a la faena?", "La guía de despacho", "El plano de trazado", "El plan de prevención de riesgos", "La guía de despacho acompaña cada viaje; el plano muestra el trazado y el plan trata la prevención."),
        ("abc", "En la verificación de una faena de colocación, ¿qué hace la persona que verifica?", "Compara lo ejecutado con el plano y las especificaciones, y lo registra", "Decide por su cuenta cambiar las medidas del proyecto", "Opera el equipo para ayudar a terminar antes", "Verificar es comparar y registrar; cambiar medidas o manejar equipos no es su función."),
        ("abc", "Una persona a pie cruza por detrás de un camión tolva que retrocede. ¿Qué riesgo corre?", "Atropello", "Vuelco del camión sobre ella", "Atrapamiento por falta de EPP", "El riesgo de quien está detrás de un vehículo que retrocede es ser golpeada: atropello."),
        ("=", "{F} ¿Cuántos viajes de camión se hicieron en total ese día?", "4*6", "Se multiplican los 4 camiones por los 6 viajes de cada uno.", " viajes"),
        ("abc", "{F} Quieres saber en qué línea y con qué medidas debe quedar el camino. ¿Qué documento consultas?", "El plano de trazado", "Las guías de despacho", "La bitácora de obra", "El trazado y sus medidas están en el plano; las guías y la bitácora registran hechos de la faena."),
        ("abc", "{F} ¿Qué riesgo nombra la ficha para un vehículo que cae de lado?", "Vuelco", "Atropello", "Polvo", "El vuelco es la caída de un vehículo de lado; el atropello es un golpe a una persona."),
        ("=", "{F} ¿Cuántos m³ de material llegaron a la obra ese día?", "4*6*12", "Se multiplican camiones, viajes por camión y metros cúbicos por viaje.", " m³"),
        ("abc", "{F} Una persona nueva quiere ayudar a dirigir los camiones sin tener autorización. ¿Qué corresponde?", "Mantenerse fuera de la zona de maniobra y avisar al supervisor", "Dirigirlos si lleva chaleco reflectante", "Dirigirlos si el operador se lo pide con un gesto", "El chaleco o un gesto del operador no reemplazan la autorización para dirigir maquinaria."),
        ("abc", "{F} Una guía de despacho anota 14 m³ y la bitácora anota 12 m³ para el mismo viaje. ¿Qué se hace?", "Anotar la diferencia e informarla al supervisor", "Usar la cifra mayor sin avisar", "Borrar la guía porque la bitácora manda", "Cuando dos documentos se contradicen no se elige uno por cuenta propia: se informa."),
        ("ab", "{F} Una estudiante dice: «ya verifiqué la faena en papel, así que puedo manejar el equipo». ¿Qué respuesta es correcta?", "No: operar maquinaria exige autorización y capacitación, no basta leer documentos", "Sí: conocer la faena la habilita para operar", "Leer y comprobar documentos es distinto de estar autorizada para operar equipos."),
        ("abc", "Una obra vial tiene el riesgo de atropello. Según la jerarquía de controles, ¿qué medida es más eficaz que dar un chaleco a cada trabajador?", "Separar la zona de las personas de la zona de maniobra de los camiones", "Pedir que cada persona esté muy atenta", "Entregar un EPP más a cada persona", "Separar zonas actúa sobre el peligro; la atención y el EPP quedan al final de la jerarquía."),
        ("=", "{F} Un camión falló y solo hizo 2 viajes; los otros 3 hicieron 6 cada uno. ¿Cuántos viajes hubo ese día?", "3*6+2", "Se suman los viajes de los tres camiones sanos y los 2 del camión que falló.", " viajes"),
        ("abc", "{F} Llega un camión sin guía de despacho. ¿Qué es lo más prudente?", "Registrar el hecho y consultar al supervisor antes de recibir el material", "Recibirlo y anotar la guía después de memoria", "Rechazarlo sin avisar a nadie", "Sin guía no hay respaldo; se registra y se consulta, sin decidir solo."),
    ],
    ctx=("abc", "Un trabajador queda atrapado entre un equipo en movimiento y un muro de la obra. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse rápido a tirarlo de la ropa", "Esperar a ver si logra salir solo", "Acercarse puede causar otro accidente; se avisa de inmediato y se espera a quien está autorizado."),
    sc=[("En una obra vial: ¿qué es la bitácora?", "El cuaderno donde se anotan los hechos del día", "La bitácora registra hechos; no contiene el trazado ni los precios."),
        ("¿Qué se hace si dos documentos de la faena se contradicen?", "Anotar la diferencia e informar al supervisor", "No se elige uno al azar porque podría ser el equivocado."),
        ("¿Quién opera la maquinaria de una obra vial?", "Personal autorizado y capacitado, con norma vigente", "Este cuaderno no habilita para operar equipos.")],
    op=("Obra de ejemplo «Camino Piedra Blanca»: 3 camiones hicieron 5 viajes cada uno, con 10 m³ de material por viaje. Hay una guía de despacho con 9 m³ para un viaje, pero la bitácora anota 10 m³. Escribe (a) cuántos m³ llegaron según el cálculo, (b) qué haces con la diferencia y a quién informas, (c) un riesgo de la faena y una medida de la jerarquía de controles para reducirlo, (d) quién debe operar los camiones.",
        "(a) 3*5*10 son 150 m³. (b) Anoto la diferencia (9 en la guía y 10 en la bitácora) y la informo al supervisor; no elijo una cifra por mi cuenta. (c) Atropello; separar la zona de personas de la zona de maniobra. (d) Personal autorizado y capacitado.",
        ["calcula 150 m³", "informa la diferencia sin decidir por su cuenta", "nombra un riesgo con una medida de la jerarquía", "indica que opera personal autorizado"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "elegir una cifra sin avisar", "decir que puede operar los camiones"],
        "Pregunta: «¿qué haces si la guía y la bitácora no coinciden?». Si no responde, pídele que relea la regla de informar la diferencia."),
    reinforce="Escribe las cuatro faenas (producción, transporte, colocación y compactación) y, junto a cada una, una frase que diga qué hace.",
    extend="Explica con un ejemplo inventado por qué una faena bien registrada en papel puede ser riesgosa si las personas entran a la zona de maniobra.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (extracto de especificaciones técnicas, de ejemplo, inventado). Capa de base granular de un camino ficticio. Espesor de proyecto: 20 cm. Tolerancia de espesor: más o menos 2 cm. "
     "Ancho de la capa: 6 m. Largo del tramo: 500 m. Exigencia de compactación: 92 % de la densidad de referencia. Todos los valores son de ejemplo y no son valores reales de ninguna norma. "
     "Responsables: el jefe de faena (coordina), el operador (maneja el equipo, si está autorizado), el laboratorista (entrega resultados de ensayos) y el inspector (revisa y firma el registro).")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario y los roles de la verificación de una faena vial: espesor, tolerancia, ensayo y registro de control.",
    prior=["Sé qué son las faenas de producción, transporte, colocación y compactación.", "Sé multiplicar y restar números enteros.", "Sé pasar de centímetros a metros."],
    explain=[
        "El espesor es la medida de alto de una capa del camino. Las especificaciones técnicas fijan un espesor de proyecto y una tolerancia: la diferencia máxima que se acepta hacia arriba o hacia abajo. Un ensayo es una prueba de laboratorio que entrega un resultado numérico, por ejemplo la densidad. El resultado se compara con la exigencia de las especificaciones. El registro de control es la hoja donde se anotan fecha, lugar del tramo, medida o resultado, si cumple y quién lo firmó.",
        "Cada persona tiene un rol. El jefe de faena coordina el trabajo; el operador maneja el equipo solo si está autorizado; el laboratorista entrega los resultados de los ensayos; el inspector revisa el registro y firma. Quien verifica no cambia las exigencias: si un valor queda fuera de la tolerancia, lo anota y lo informa. Las exigencias reales las fijan el manual de carretera y la norma vigente, no este cuaderno.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("espesor", "medida de alto de una capa"), ("tolerancia", "diferencia máxima aceptada respecto del valor de proyecto"), ("ensayo", "prueba de laboratorio que entrega un resultado numérico"), ("registro de control", "hoja donde se anota qué se midió, dónde, cuándo, si cumple y quién firmó"), ("densidad de referencia", "valor de laboratorio con el que se compara el material colocado"), ("jefe de faena", "persona que coordina el trabajo"), ("laboratorista", "persona que realiza ensayos y entrega resultados"), ("inspector", "persona que revisa y firma el registro")],
    worked=[
        ("Rango aceptado", "En una capa de ejemplo el espesor de proyecto es 15 cm y la tolerancia es más o menos 1 cm. ¿Qué espesores se aceptan?", ["Se resta y se suma la tolerancia al valor de proyecto.", "15 menos 1 son 14 y 15 más 1 son 16."], "Entre 14 cm y 16 cm"),
        ("Elegir al responsable", "En una obra de ejemplo se necesita el resultado numérico de un ensayo de densidad. ¿Quién lo entrega?", ["Los ensayos los realiza el laboratorio.", "Entonces lo entrega el laboratorista."], "El laboratorista"),
    ],
    mistakes=[("Aceptar un espesor fuera de la tolerancia «porque falta poco».", "La tolerancia es el límite; fuera de ella no cumple.", "Anota el valor, indica que no cumple e informa al jefe de faena y al inspector."),
              ("Modificar la exigencia de las especificaciones para que el tramo cumpla.", "Las exigencias las fija el proyecto y la norma vigente.", "Registra lo medido y consulta a quien corresponde.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es la tolerancia de espesor de una capa?", "La diferencia máxima aceptada respecto del espesor de proyecto", "El espesor más grande que se puede colocar sin avisar", "El tiempo que se espera antes de medir la capa", "La tolerancia es un margen de diferencia; no es un tiempo ni un permiso para cambiar el proyecto."),
        ("abc", "Un resultado numérico de laboratorio sobre el material de la capa se llama:", "Ensayo", "Bitácora", "Trazado", "El ensayo es la prueba de laboratorio con resultado numérico; la bitácora y el trazado son otros documentos."),
        ("abc", "¿Quién revisa el registro de control y lo firma?", "El inspector", "El operador del equipo", "El laboratorista que hizo el ensayo", "El inspector revisa y firma; el operador maneja el equipo y el laboratorista entrega resultados."),
        ("=", "{F} ¿Cuál es el espesor mínimo aceptado, en cm?", "20-2", "Al espesor de proyecto se le resta la tolerancia.", " cm"),
        ("=", "{F} ¿Cuál es el espesor máximo aceptado, en cm?", "20+2", "Al espesor de proyecto se le suma la tolerancia.", " cm"),
        ("abc", "{F} Una medida registrada es 23 cm. ¿Qué conclusión corresponde?", "No cumple: supera el máximo aceptado; se anota e informa", "Cumple, porque el espesor está cerca de 20 cm", "Cumple, porque es mayor que el mínimo", "El máximo aceptado es 22 cm; 23 cm queda fuera de la tolerancia."),
        ("=", "{F} ¿Cuántos metros cuadrados de superficie tiene la capa del tramo?", "500*6", "La superficie es el largo del tramo multiplicado por el ancho.", " m²"),
        ("abc", "{F} Un operador quiere cambiar la exigencia de compactación a 90 % para que el tramo cumpla. ¿Qué corresponde?", "No cambiarla: la fija el proyecto y se informa lo medido", "Cambiarla si el jefe de faena está de acuerdo en la obra", "Cambiarla si el tramo está casi cumpliendo", "La exigencia viene del proyecto y la norma vigente; no se ajusta para que algo cumpla."),
        ("abc", "{F} Se necesita saber qué resultado entregó el ensayo de densidad. ¿A quién se lo pides?", "Al laboratorista", "Al inspector, porque él mide la densidad", "Al operador, porque él maneja el equipo", "Los ensayos los entrega el laboratorista; el inspector revisa y el operador maneja el equipo."),
        ("ab", "{F} Un compañero dice: «si la medida da 18 cm, cumple». ¿Qué respuesta es correcta?", "Sí: 18 cm es justo el mínimo de la tolerancia", "No: 18 cm es menor que 20 cm y por eso no cumple", "El rango aceptado va de 18 a 22 cm, así que 18 cm está dentro del límite."),
        ("abc", "{F} Un registro de control trae la medida pero no tiene fecha ni lugar del tramo. ¿Qué se concluye?", "Está incompleto: falta información para ubicar y respaldar la medida", "Está completo, porque lo importante es la medida", "Está completo si lo firma el operador", "Un registro útil deja constancia de qué, dónde, cuándo y quién; sin fecha y lugar no se puede respaldar."),
        ("=", "{F} Se mide un punto cada 100 m del tramo, incluidos ambos extremos. ¿Cuántos puntos de medida hay?", "500//100+1", "Se divide el largo por la separación y se suma el punto del extremo.", " puntos"),
        ("abc", "{F} Dos medidas del mismo punto son 19 cm en el registro y 21 cm en la bitácora. ¿Qué es lo más prudente?", "Informar la diferencia al inspector antes de dar el tramo por aceptado", "Promediar ambas medidas y aceptar sin avisar", "Usar siempre la del registro porque es más formal", "Una diferencia entre documentos se informa; no se arregla con un promedio decidido por cuenta propia."),
    ],
    ctx=("abc", "Una trabajadora nueva ve que a un tramo le faltan 2 cm de espesor y propone corregirlo ella misma con un equipo estacionado. ¿Qué responde un compañero?", "Que informe al jefe de faena, porque corregir el tramo y operar equipos corresponde a personal autorizado", "Que lo haga rápido antes de que llegue el inspector", "Que lo haga si el equipo parece fácil de manejar", "Corregir y manejar equipos exige autorización; esconder el problema al inspector tampoco es una opción."),
    sc=[("En Obras Viales: ¿qué es un ensayo?", "Una prueba de laboratorio que entrega un resultado numérico", "El ensayo se compara con la exigencia de las especificaciones."),
        ("Si el espesor de proyecto es 12 cm y la tolerancia es 1 cm, ¿cuál es el máximo aceptado?", "13 cm", "Se suma la tolerancia de 1 cm a los 12 cm de proyecto."),
        ("¿Quién coordina el trabajo de la faena?", "El jefe de faena", "El jefe de faena coordina; el inspector revisa y el laboratorista ensaya.")],
    op=("Especificaciones de ejemplo «Camino Cerro Alto»: espesor de proyecto 10 cm, tolerancia más o menos 1 cm. Registro de un punto: medida 12 cm, sin firma del inspector. Escribe (a) el rango aceptado, (b) si la medida cumple, (c) qué falta en el registro, (d) a quién informas y qué papel tiene el laboratorista.",
        "(a) Entre 9 cm y 11 cm. (b) No cumple: 12 cm supera el máximo de 11 cm. (c) Falta la firma del inspector (y conviene verificar fecha y lugar). (d) Informo al jefe de faena y al inspector; el laboratorista entrega los resultados de ensayos, no corrige el tramo.",
        ["calcula el rango 9 a 11 cm", "concluye que no cumple", "nombra lo que falta en el registro", "indica a quién informa y el papel del laboratorista"],
        ["hoja con las cuatro respuestas"],
        ["usar 10 cm como único valor", "aceptar 12 cm por estar cerca", "decir que corrige el tramo por su cuenta"],
        "Pregunta: «¿hasta cuántos cm se acepta en este ejemplo?». Si no responde, pídele que sume la tolerancia al espesor de proyecto."),
    reinforce="Inventa un espesor de proyecto y una tolerancia; escribe el rango aceptado y una medida que cumpla y otra que no.",
    extend="Explica con un ejemplo por qué el inspector, el laboratorista y el jefe de faena no deberían ser la misma persona en una verificación.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (planilla de control de espesor, de ejemplo, inventada). Camino ficticio «Ruta Quebrada». Espesor de proyecto: 20 cm; tolerancia más o menos 2 cm (valores de ejemplo). "
     "Medidas registradas en cinco puntos del tramo por el equipo de control (el cuaderno solo entrega los datos): P1 = 19 cm; P2 = 22 cm; P3 = 17 cm; P4 = 20 cm; P5 = 21 cm. "
     "Observación de la bitácora: el punto P3 queda en una curva donde hubo lluvia ese día.")
build(
    O5, 3, F,
    use="Aprenderé a analizar en papel una planilla de control de espesor: comparar cada punto con la tolerancia, decidir si cumple y qué se informa.",
    prior=["Sé qué es el espesor y la tolerancia.", "Sé comparar números con un rango.", "Sé restar números enteros."],
    explain=[
        "Para analizar un caso de verificación se sigue un orden de lectura. Primero se anota el valor de proyecto y la tolerancia. Luego se calcula el rango aceptado: el mínimo es el valor de proyecto menos la tolerancia y el máximo es el valor de proyecto más la tolerancia. Después se compara cada punto con el rango y se marca cumple o no cumple. Un punto que queda justo en el límite cumple, porque el límite pertenece al rango.",
        "Al final se escribe la conclusión: cuántos puntos no cumplen, en qué lugar están y qué observaciones tiene la bitácora. Quien verifica no corrige el tramo: informa al jefe de faena y al inspector, que deciden qué hacer. Una observación, como una lluvia o una curva, ayuda a entender la causa, pero no cambia el resultado de la medida ni la tolerancia.",
        f"Las cifras de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("rango aceptado", "valores entre el mínimo y el máximo permitidos por la tolerancia"), ("punto de control", "lugar del tramo donde se registra una medida"), ("cumple", "la medida está dentro del rango aceptado, incluidos los límites"), ("observación", "nota de la bitácora que explica una situación del tramo"), ("planilla de control", "tabla donde se anotan las medidas por punto")],
    worked=[
        ("Rango y comparación", "Una planilla de ejemplo tiene espesor de proyecto 16 cm y tolerancia 1 cm. Un punto mide 17 cm. ¿Cumple?", ["El rango aceptado va de 15 a 17 cm.", "17 cm está justo en el límite, que pertenece al rango."], "Sí, cumple"),
        ("Contar puntos", "En otra planilla de ejemplo, de 8 puntos controlados, 2 no cumplen. ¿Cuántos cumplen?", ["Se restan los que no cumplen del total.", "8 menos 2 son 6."], "6 puntos"),
    ],
    mistakes=[("Marcar «no cumple» un punto que está justo en el límite del rango.", "El límite pertenece al rango aceptado.", "Compara con el mínimo y el máximo y acepta los valores iguales a ellos."),
              ("Dar por cumplido un punto malo porque la bitácora dice que llovió.", "La observación explica la causa pero no cambia la medida.", "Registra que no cumple y anota la observación para quien decide.")],
    T=[
        ("abc", "En una planilla de control: ¿qué es un punto de control?", "El lugar del tramo donde se registra una medida", "El máximo de espesor que se puede aceptar", "La firma del inspector en el registro", "Un punto de control es un lugar con su medida; el máximo y la firma son otra cosa."),
        ("abc", "Con espesor de proyecto 10 cm y tolerancia 1 cm, ¿qué medida cumple?", "11 cm", "12 cm", "8 cm", "El rango va de 9 a 11 cm; 12 y 8 quedan fuera."),
        ("abc", "En una planilla de control, una observación de la bitácora sirve para:", "Entender la posible causa de una medida, sin cambiar el resultado", "Cambiar la tolerancia cuando el clima fue malo", "Aceptar cualquier medida de ese día", "La observación aporta contexto; no modifica la tolerancia ni el resultado."),
        ("=", "{F} ¿Cuál es el mínimo del rango aceptado, en cm?", "20-2", "Al espesor de proyecto se le resta la tolerancia.", " cm"),
        ("abc", "{F} ¿Cuántos puntos tienen una medida dentro del rango aceptado, incluidos los límites?", "4 puntos: P1, P2, P4 y P5", "3 puntos: P1, P4 y P5", "5 puntos: todos", "P2 mide 22 cm, que es el límite y cumple; solo P3 (17 cm) queda fuera."),
        ("abc", "{F} ¿Qué punto no cumple?", "P3", "P2", "P5", "P3 mide 17 cm, menos que el mínimo de 18 cm; P2 y P5 están dentro del rango."),
        ("=", "{F} ¿Cuántos cm separan la medida mayor de la menor?", "22-17", "Se resta la medida menor de la mayor.", " cm"),
        ("abc", "{F} El punto P3 queda en una curva donde llovió. ¿Qué se hace con el resultado?", "Se registra que no cumple y se anota la observación para quien decide", "Se marca que cumple porque llovió", "Se borra el punto de la planilla", "La lluvia explica una posible causa; no cambia la medida ni autoriza a borrarla."),
        ("abc", "{F} ¿A quién se informa que P3 no cumple?", "Al jefe de faena y al inspector", "Solo al camionero que trajo el material", "A nadie, porque es un solo punto", "La medida fuera de tolerancia se informa a quienes coordinan y revisan, aunque sea un solo punto."),
        ("ab", "{F} Un compañero dice: «P2 no cumple porque mide 22 y el proyecto pide 20». ¿Qué respuesta es correcta?", "No: 22 cm es el máximo del rango y cumple", "Sí: cualquier medida distinta de 20 cm incumple", "Con tolerancia de 2 cm el rango llega hasta 22 cm, límite incluido."),
        ("abc", "{F} Se hacen dos mediciones nuevas en el mismo tramo. ¿Cómo se registran?", "Se agregan a la planilla sin borrar las medidas anteriores", "Reemplazan a P3 sin dejar constancia", "Se promedian con P3 y se anota solo el promedio", "Las nuevas medidas se suman al registro; no se reemplazan ni promedian los datos anteriores."),
        ("=", "{F} Si P3 se corrigiera hasta quedar en el mínimo del rango, ¿cuántos cm tendría que aumentar?", "18-17", "Se resta la medida actual del mínimo aceptado.", " cm"),
        ("abc", "{F} El inspector pide una conclusión escrita. ¿Cuál es la más completa?", "Cuatro de cinco puntos cumplen; P3 mide 17 cm (mínimo 18) y se informa con la observación de la lluvia", "Todo está bien porque la mayoría cumple", "Hay un problema en el camino", "La conclusión completa dice cuántos cumplen, cuál no, su valor, el límite y la observación."),
    ],
    ctx=("abc", "Un joven que visita la obra pregunta si puede subirse a un rodillo estacionado solo para ver el tramo desde arriba. ¿Qué corresponde?", "Pedirle que no lo haga: solo personal autorizado se sube a los equipos", "Dejarlo si se queda quieto unos minutos", "Dejarlo si lleva casco", "Subir a un equipo exige autorización; el casco no reemplaza esa autorización."),
    sc=[("¿Un punto que mide justo el valor máximo del rango cumple?", "Sí, porque los límites pertenecen al rango", "La tolerancia incluye el máximo y el mínimo."),
        ("En una planilla con proyecto 30 cm y tolerancia 3 cm, ¿cuál es el mínimo?", "27 cm", "Se resta la tolerancia de 3 cm a los 30 cm de proyecto."),
        ("¿Quién corrige un tramo que no cumple?", "Se informa; decide quien corresponde con personal autorizado", "Quien verifica informa y no corrige el tramo por su cuenta.")],
    op=("Planilla de ejemplo «Camino Los Pinos»: espesor de proyecto 15 cm, tolerancia más o menos 1 cm. Medidas: Q1 = 14 cm; Q2 = 16 cm; Q3 = 18 cm; Q4 = 15 cm. Observación de la bitácora: en Q3 se acopió material. Escribe (a) el rango aceptado, (b) qué puntos cumplen y cuáles no, (c) la conclusión escrita, (d) a quién informas.",
        "(a) De 14 a 16 cm. (b) Cumplen Q1, Q2 y Q4; no cumple Q3 (18 cm supera 16). (c) Tres de cuatro puntos cumplen; Q3 mide 18 cm, máximo 16, observación: se acopió material. (d) Al jefe de faena y al inspector.",
        ["calcula el rango", "clasifica los cuatro puntos", "redacta una conclusión completa", "indica a quién informa"],
        ["hoja con las cuatro respuestas"],
        ["marcar Q1 como no cumple", "omitir la observación", "corregir el tramo por su cuenta"],
        "Pregunta: «¿cumple un punto que mide justo el límite?». Si duda, pídele que relea la regla de los límites."),
    reinforce="Inventa una planilla de tres puntos con su espesor de proyecto y tolerancia; escribe el rango y marca cumple o no cumple en cada punto.",
    extend="Explica por qué una lluvia no cambia la tolerancia, pero sí conviene anotarla como observación.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cubicación de una capa, de ejemplo, inventada). Camino ficticio «Ruta del Llano». Tramo de 400 m de largo y 7 m de ancho. Espesor de proyecto: 20 cm, es decir 0,2 m. "
     "Cada camión tolva transporta 14 m³ por viaje. Precio de ejemplo del material colocado: $18.000 por m³. En la planilla se usa volumen = largo por ancho por espesor, con el espesor en metros.")
build(
    O5, 4, F,
    use="Aprenderé a calcular en una planilla el volumen de una capa, los viajes de camión y un costo de ejemplo.",
    prior=["Sé calcular superficies de rectángulos.", "Sé pasar de centímetros a metros.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La cubicación calcula cuánta cantidad de material necesita una obra. En una capa de camino, el volumen se calcula multiplicando el largo por el ancho y por el espesor, con todo en metros. El resultado se da en metros cúbicos (m³). Si el espesor está en centímetros, primero se pasa a metros: 20 cm son 0,2 m. Para evitar decimales también se puede multiplicar largo por ancho por los centímetros y dividir por 100.",
        "Con el volumen se calculan los viajes: se divide el volumen total por lo que lleva un camión por viaje. Si la división no es exacta, el último viaje sale incompleto, pero igual se cuenta como un viaje más. El costo de ejemplo es el volumen por el precio por m³. Estas cuentas se hacen en una planilla con datos de ejemplo; los valores reales de espesor y de precio los fijan el proyecto y el mercado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cubicación", "cálculo de la cantidad de material que necesita una obra"), ("volumen", "cantidad de espacio de una capa; se mide en metros cúbicos"), ("m³", "metro cúbico, unidad de volumen"), ("viaje", "traslado de un camión cargado hasta la obra"), ("planilla", "tabla donde se ordenan datos y cálculos")],
    worked=[
        ("Volumen de una capa", "Un tramo de ejemplo mide 100 m de largo y 5 m de ancho, con espesor 10 cm (0,1 m). ¿Cuántos m³ tiene la capa?", ["Se multiplican largo, ancho y espesor en metros.", "100 por 5 es 500 y 500 por 0,1 es 50."], "50 m³"),
        ("Viajes", "Un volumen de ejemplo de 60 m³ se transporta en camiones de 12 m³ por viaje. ¿Cuántos viajes hacen falta?", ["Se divide el volumen por la carga de un viaje.", "60 dividido en 12 son 5."], "5 viajes"),
    ],
    mistakes=[("Multiplicar con el espesor en centímetros y entregar el resultado en m³.", "Las unidades no coinciden y el volumen sale 100 veces mayor.", "Pasa el espesor a metros o divide por 100 al final."),
              ("Redondear hacia abajo los viajes y quedarse con material sin transportar.", "Un último viaje incompleto sigue siendo un viaje.", "Si la división no es exacta, suma un viaje más.")],
    T=[
        ("abc", "En una cubicación: ¿qué mide el volumen de una capa?", "La cantidad de espacio de la capa, en metros cúbicos", "La longitud de la capa, en metros", "El precio de la capa, en pesos", "El volumen es espacio en m³; la longitud y el precio son otras magnitudes."),
        ("abc", "Un espesor de 30 cm, ¿cuántos metros es?", "0,3 m", "3 m", "0,03 m", "Un metro tiene 100 cm; 30 cm son 30 centésimas de metro, o 0,3 m."),
        ("abc", "Para calcular el volumen de una capa rectangular se multiplican:", "Largo, ancho y espesor", "Largo, ancho y precio", "Ancho, espesor y número de camiones", "El volumen de una capa rectangular usa tres medidas de longitud: largo, ancho y espesor."),
        ("=", "{F} ¿Cuántos m² de superficie tiene el tramo (largo por ancho)?", "400*7", "La superficie se calcula multiplicando el largo por el ancho.", " m²"),
        ("=", "{F} ¿Cuántos m³ tiene la capa? (largo por ancho por espesor en cm, dividido por 100)", "400*7*20//100", "Se multiplica la superficie por el espesor en cm y se divide por 100.", " m³"),
        ("abc", "{F} Si por error se multiplicara por 20 en vez de por 0,2, ¿cómo saldría el volumen?", "100 veces mayor", "100 veces menor", "Igual, porque 0,2 y 20 se parecen", "Pasar de 0,2 a 20 multiplica el factor por 100, y el volumen sale 100 veces mayor."),
        ("=", "{F} ¿Cuántos viajes de camión hacen falta?", "(400*7*20//100)//14", "Se divide el volumen de la capa por los 14 m³ de cada viaje.", " viajes"),
        ("=", "{F} ¿Cuánto cuesta el material de la capa, en pesos, con el precio de ejemplo?", "400*7*20//100*18000", "Se multiplica el volumen de la capa por el precio de cada m³.", " pesos"),
        ("abc", "{F} Si el tramo se alargara a 450 m con el mismo ancho y espesor, ¿qué ocurre con el volumen?", "Aumenta, porque el largo es un factor del volumen", "Queda igual, porque el espesor no cambió", "Disminuye, porque hay más camino", "El largo multiplica al volumen: más largo, más volumen."),
        ("ab", "{F} Un compañero propone calcular el volumen como largo por ancho por 20, sin pasar a metros. ¿Qué respuesta es correcta?", "Es incorrecto: da un resultado 100 veces mayor, falta pasar el espesor a metros", "Es correcto: los números se multiplican igual en cualquier unidad", "El resultado solo vale en m³ si el espesor se expresa en metros o se divide por 100."),
        ("abc", "{F} Un proveedor de ejemplo entrega solo camiones de 10 m³ por viaje. ¿Cuántos viajes harían falta?", "56 viajes", "55 viajes", "560 viajes", "El volumen de la capa es 560 m³; con 10 m³ por viaje se necesitan 56 viajes exactos."),
        ("=", "{F} Se pide un 10 % más de material como reserva. ¿Cuántos m³ se piden en total?", "400*7*20//100*110//100", "Se calcula el volumen de la capa y se multiplica por 110 sobre 100.", " m³"),
        ("abc", "{F} Un compañero dice: «con el cálculo ya sé cuántos viajes son, así que puedo manejar el camión». ¿Qué corresponde?", "No: conducir exige licencia y autorización; el cálculo solo ordena cantidades", "Sí, porque ya conoce los viajes", "Sí, si va despacio", "Un cálculo de planilla no reemplaza la licencia ni la autorización para conducir."),
    ],
    ctx=("abc", "Un supervisor de ejemplo recibe una planilla donde el volumen de una capa sale 100 veces mayor de lo normal. ¿Cuál es la causa más probable?", "Se usó el espesor en centímetros sin pasarlo a metros", "El camión llevaba poca carga", "El precio por m³ estaba muy bajo", "Un error de unidad en el espesor multiplica el volumen por 100; el precio no cambia el volumen."),
    sc=[("¿Cuántos m³ tiene una capa de 50 m de largo, 4 m de ancho y 0,1 m de espesor?", "20 m³", "50 por 4 por 0,1 da 20 metros cúbicos."),
        ("Si un volumen necesita 4,2 viajes de camión, ¿cuántos viajes se programan?", "5 viajes", "El último viaje incompleto igualmente cuenta como viaje."),
        ("¿Quién conduce y opera los camiones de la obra?", "Personal con licencia y autorización", "Este cuaderno no habilita para conducir ni operar.")],
    op=("Planilla de ejemplo «Camino El Roble»: tramo de 200 m de largo y 6 m de ancho, espesor 15 cm, camiones de 9 m³ por viaje y precio de ejemplo $20.000 por m³. Escribe (a) el volumen en m³, (b) los viajes necesarios, (c) el costo del material y (d) un riesgo de la faena de transporte con una medida preventiva.",
        "(a) 200*6*0,15 = 180 m³. (b) 180 dividido en 9 son 20 viajes. (c) 180*20.000 = $3.600.000. (d) Atropello; separar la zona de maniobra de las personas.",
        ["calcula 180 m³", "calcula 20 viajes", "calcula el costo", "nombra un riesgo con medida"],
        ["hoja con las cuatro respuestas"],
        ["no pasar 15 cm a metros", "redondear mal los viajes", "decir que él conduce el camión"],
        "Pregunta: «¿en qué unidad va el espesor al multiplicar?». Si no responde, pídele que relea el paso a metros."),
    reinforce="Calcula el volumen de una capa inventada de 80 m de largo, 5 m de ancho y 10 cm de espesor y los viajes con camiones de 10 m³.",
    extend="Explica por qué un error de unidad en una planilla puede hacer que se pidan cantidades de material equivocadas.",
)

# ============================================================ OAM-06, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Reparación de un camino ficticio «Ruta Mirador» con una pista de dos habilitada para el tránsito. Documentos: plano de señalización de la obra (1 lámina), "
     "plan de desvío (3 páginas) y plan de prevención de riesgos (6 páginas). Riesgos anotados: atropello de trabajadores por vehículos de paso, choque contra equipos detenidos, visibilidad reducida en la tarde y ruido. "
     "El plano de señalización lista 6 señales de advertencia, 20 conos y 2 barreras.")
build(
    O6, 1, F,
    use="Aprenderé por qué una obra vial necesita señalización, qué riesgos busca reducir y qué documentos la respaldan, sin aprender a instalarla.",
    prior=["Sé qué documentos forman un proyecto de obra.", "Sé sumar y restar números enteros.", "Sé qué es el atropello."],
    explain=[
        "Cuando una obra vial se hace junto a vehículos que circulan, las personas que trabajan y las que conducen corren riesgo. La señalización informa a quien conduce que hay una obra y le indica cómo avanzar. Una señal da un mensaje con forma, color y símbolo que fija el manual de carretera vigente. Un dispositivo de seguridad, como un cono o una barrera, separa o canaliza el tránsito y protege la zona de trabajo. La señalización de una obra se diseña en un plano de señalización y en un plan de desvío.",
        "Instalar o retirar señales con vehículos circulando es una tarea peligrosa: la hace personal capacitado y autorizado, con un plan aprobado. Este cuaderno solo enseña a leer los documentos y a reconocer riesgos. En la jerarquía de controles, lo primero es eliminar o alejar el peligro (por ejemplo, cerrar la vía si es posible), luego separar con barreras, luego organizar el trabajo y por último el EPP, como el chaleco reflectante.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("señalización", "conjunto de señales y dispositivos que ordenan el tránsito y avisan de la obra"), ("señal", "mensaje con forma, color y símbolo fijados por el manual de carretera"), ("dispositivo de seguridad", "elemento como un cono o una barrera que separa o canaliza el tránsito"), ("plan de desvío", "documento que indica por dónde circulan los vehículos mientras dura la obra"), ("visibilidad", "capacidad de ver y ser visto"), ("jerarquía de controles", "orden de las medidas de seguridad, de la más eficaz a la menos eficaz"), ("EPP", "elementos de protección personal")],
    worked=[
        ("Elegir el documento", "Un jefe de obra de ejemplo necesita saber por dónde pasarán los vehículos mientras dure una reparación. ¿Qué documento consulta?", ["La ruta alternativa de los vehículos se explica en un documento propio.", "Ese documento es el plan de desvío."], "El plan de desvío"),
        ("Contar elementos", "Un plano de ejemplo lista 4 señales y 9 conos. ¿Cuántos elementos de señalización suma?", ["Se suman las señales y los conos.", "4 más 9 son 13."], "13 elementos"),
    ],
    mistakes=[("Instalar un cono en la calzada «solo un momento» sin autorización ni plan.", "Quien invade la calzada con tránsito corre riesgo de atropello.", "La instalación la hace personal capacitado y autorizado, con plan aprobado."),
              ("Creer que el chaleco reflectante es suficiente protección frente a los vehículos.", "El EPP es la última medida de la jerarquía de controles.", "Primero se aleja o separa el peligro; el chaleco complementa.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es un dispositivo de seguridad de una obra con tránsito?", "Un elemento como un cono o una barrera que separa o canaliza el tránsito", "Un documento que fija el precio de las señales", "El mensaje con símbolo que ve quien conduce", "Un dispositivo es un elemento físico; el mensaje es la señal y el precio va en otro documento."),
        ("abc", "¿Qué documento indica por dónde circulan los vehículos mientras dura una obra?", "El plan de desvío", "La bitácora de combustible", "La guía de despacho", "El desvío se define en el plan de desvío; la guía respalda viajes de material."),
        ("abc", "Un trabajador está en la calzada junto a vehículos que pasan. ¿Qué riesgo principal corre?", "Atropello", "Hundimiento del suelo", "Incendio de la calzada", "El principal riesgo de estar en la calzada con tránsito es ser golpeado por un vehículo."),
        ("=", "{F} ¿Cuántos elementos de señalización lista el plano en total (señales, conos y barreras)?", "6+20+2", "Se suman las señales, los conos y las barreras.", " elementos"),
        ("abc", "{F} ¿Qué riesgo de la ficha se agrava cuando oscurece por la tarde?", "La visibilidad reducida", "El ruido de los equipos", "El choque con el plan de desvío", "Al oscurecer se ve menos, por eso la visibilidad reducida aumenta el riesgo de ser atropellado."),
        ("abc", "{F} ¿Cuál es el primer paso de la jerarquía de controles frente al atropello?", "Eliminar o alejar el peligro, por ejemplo cerrando la vía si es posible", "Entregar chalecos reflectantes a todo el equipo", "Pedir a cada persona que mire hacia atrás", "Eliminar o alejar el peligro es más eficaz que el EPP o el cuidado individual."),
        ("=", "{F} Se agregan 4 señales de advertencia a las del plano. ¿Cuántas señales de advertencia habrá en total?", "6+4", "Se suman las señales nuevas a las 6 que ya lista el plano.", " señales"),
        ("abc", "{F} Un trabajador quiere instalar una señal en plena calzada «porque es rápido». ¿Qué corresponde?", "No hacerlo: lo realiza personal capacitado y autorizado con un plan aprobado", "Hacerlo con chaleco reflectante", "Hacerlo si otro compañero vigila los autos", "El chaleco o un vigilante informal no reemplazan la autorización ni el plan."),
        ("abc", "{F} El plan de desvío dice una cosa y el plano de señalización dibuja otra ruta. ¿Qué se hace?", "Anotar la diferencia e informar al jefe de obra o al prevencionista", "Seguir el plano y no avisar", "Seguir el plan sin comparar con el plano", "Un conflicto entre documentos se informa; no se resuelve por cuenta propia."),
        ("ab", "{F} Una estudiante dice: «sé leer el plano de señalización, así que ya puedo instalar los conos con tránsito». ¿Qué respuesta es correcta?", "No: leer el plano no habilita; instalar con tránsito exige personal autorizado y plan aprobado", "Sí: leer el plano la habilita para instalar", "Entender un plano es distinto de estar autorizada para trabajar junto al tránsito."),
        ("abc", "El jefe de obra dice: «con tener chalecos para todos ya cumplimos con la seguridad». ¿Qué falla en esa idea?", "El chaleco es la última medida; faltan medidas de separar la zona y organizar el trabajo", "Los chalecos no son útiles en ninguna obra", "El chaleco reemplaza al plan de desvío", "El EPP complementa, pero antes deben aplicarse medidas más eficaces sobre el peligro."),
        ("=", "{F} Se cambian por barreras 5 de los 20 conos del plano. ¿Cuántas barreras habría en total?", "2+5", "A las 2 barreras del plano se suman las 5 nuevas.", " barreras"),
        ("abc", "{F} Un conductor cruza a alta velocidad y casi golpea a un trabajador. ¿Qué es lo más prudente?", "Informar el hecho al prevencionista para revisar las medidas de la zona", "No decir nada porque no pasó nada", "Ponerse a dirigir el tránsito por cuenta propia", "Un cuasi accidente se informa para corregir medidas; dirigir el tránsito sin autorización es peligroso."),
    ],
    ctx=("abc", "Un vehículo choca contra un equipo detenido en la obra y hay una persona caída cerca de la calzada. ¿Qué haces según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Cruzar corriendo la calzada para levantarla", "Mover el vehículo para despejar la vía", "Acercarse sin protección puede producir otro atropello; se avisa a emergencias y a un adulto responsable."),
    sc=[("En Obras Viales: ¿qué es una señal?", "Un mensaje con forma, color y símbolo fijado por el manual de carretera", "La señal informa a quien conduce; el cono y la barrera son dispositivos."),
        ("¿Quién instala señales en una vía con tránsito?", "Personal capacitado y autorizado con un plan aprobado", "Este cuaderno no habilita para trabajar junto al tránsito."),
        ("¿Dónde queda el EPP en la jerarquía de controles?", "Al final, como último recurso", "Primero se actúa sobre el peligro y luego se protege a la persona.")],
    op=("Obra de ejemplo «Puente Río Claro»: el plano de señalización lista 3 señales de advertencia y 12 conos; el plan de desvío indica una ruta de 4 km. Hay riesgo de atropello y de visibilidad reducida. Escribe (a) cuántos elementos de señalización suma el plano, (b) un riesgo y una medida de la jerarquía de controles, (c) qué documento dice por dónde circulan los vehículos, (d) quién instala las señales.",
        "(a) 3+12 son 15 elementos. (b) Atropello; separar la zona de trabajo con barreras. (c) El plan de desvío. (d) Personal capacitado y autorizado, con plan aprobado.",
        ["suma 15 elementos", "nombra un riesgo con medida", "nombra el plan de desvío", "indica que instala personal autorizado"],
        ["hoja con las cuatro respuestas"],
        ["incluir el desvío de 4 km en la suma", "poner el EPP como primera medida", "decir que él instala las señales"],
        "Pregunta: «¿quién instala las señales con tránsito?». Si no responde, pídele que relea la regla de autorización."),
    reinforce="Escribe tres riesgos de trabajar junto al tránsito y, junto a cada uno, una medida de la jerarquía de controles.",
    extend="Explica con un ejemplo inventado por qué las señales no bastan si las personas siguen entrando a la calzada sin autorización.",
)

# ============================================================ OAM-06, clase 2
F = ("Ficha 2 (extracto del plano de señalización de una obra de ejemplo, inventado). Camino ficticio «Ruta Los Olivos». Leyenda de ejemplo: SA = señal de advertencia; SR = señal reglamentaria; SI = señal informativa; "
     "CO = cono; BA = barrera. Cantidades del plano: SA 4; SR 2; SI 1; CO 24; BA 3. El plano está firmado por el proyectista y la última revisión es la revisión B. Responsables: el prevencionista (revisa la seguridad) y el jefe de obra (coordina).")
build(
    O6, 2, F,
    use="Aprenderé a leer la leyenda y las cantidades de un plano de señalización y los roles de quienes lo revisan.",
    prior=["Sé qué es una señal y un dispositivo de seguridad.", "Sé leer una tabla de cantidades.", "Sé sumar números enteros."],
    explain=[
        "Un plano de señalización dibuja y lista las señales y los dispositivos de la obra. Las señales de advertencia avisan de un peligro adelante. Las señales reglamentarias indican una obligación o prohibición. Las señales informativas entregan datos, como la dirección de un desvío. La leyenda explica qué es cada sigla; sin ella el plano no se entiende. El cuadro de cantidades dice cuántas piezas de cada tipo hay que tener. La revisión es la versión del plano, identificada con una letra.",
        "Dos roles importan aquí. El prevencionista de riesgos revisa que las medidas protejan a trabajadores y conductores. El jefe de obra coordina el trabajo y tiene que contar con el plano en su última revisión. Quien lee un plano no agrega ni quita señales: si ve una falta, la anota e informa. Los detalles de forma y color los fija el manual de carretera vigente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("señal de advertencia", "avisa de un peligro adelante"), ("señal reglamentaria", "indica una obligación o prohibición"), ("señal informativa", "entrega datos, como la dirección de un desvío"), ("leyenda", "tabla que explica qué significa cada sigla del plano"), ("cuadro de cantidades", "lista de cuántas piezas de cada tipo se necesitan"), ("revisión", "versión del plano, identificada con una letra"), ("prevencionista de riesgos", "profesional que revisa que las medidas protejan a las personas"), ("jefe de obra", "persona que coordina el trabajo de la obra")],
    worked=[
        ("Clasificar una señal", "Un plano de ejemplo incluye una señal que avisa «curva peligrosa adelante». ¿Qué tipo de señal es?", ["Avisa de un peligro adelante.", "Es una señal de advertencia."], "Señal de advertencia"),
        ("Sumar señales", "Un plano de ejemplo trae 3 señales de advertencia, 1 reglamentaria y 2 informativas. ¿Cuántas señales hay?", ["Se suman los tres tipos.", "3 más 1 más 2 son 6."], "6 señales"),
    ],
    mistakes=[("Usar una revisión antigua del plano porque «es la que tenía impresa».", "La revisión antigua puede tener señales distintas.", "Comprueba la letra de la revisión en el rótulo y usa la vigente."),
              ("Agregar una señal al plano por iniciativa propia.", "El plano lo modifica el proyectista, no quien lo lee.", "Anota la observación e infórmala al prevencionista o al jefe de obra.")],
    T=[
        ("abc", "En un plano de señalización: ¿qué tipo de señal indica una obligación o una prohibición?", "Reglamentaria", "Informativa", "De advertencia", "Las reglamentarias fijan obligaciones o prohibiciones; las informativas dan datos y las de advertencia avisan de peligros."),
        ("abc", "Una señal que indica la dirección de un desvío es:", "Informativa", "Reglamentaria", "De advertencia", "Entregar un dato de dirección corresponde a una señal informativa."),
        ("abc", "¿Para qué sirve la leyenda de un plano de señalización?", "Para explicar qué significa cada sigla del plano", "Para fijar el precio de cada señal", "Para indicar cuántos camiones llegan a la obra", "Sin la leyenda no se entiende qué es SA, CO o BA; el precio y los camiones son otros documentos."),
        ("=", "{F} ¿Cuántas señales (de los tres tipos) hay en el plano?", "4+2+1", "Se suman las señales de advertencia, reglamentarias e informativas.", " señales"),
        ("=", "{F} ¿Cuántos dispositivos de seguridad (conos y barreras) lista el plano?", "24+3", "Se suman los conos y las barreras.", " dispositivos"),
        ("abc", "{F} Según la leyenda, ¿qué significa la sigla CO?", "Cono", "Barrera", "Señal reglamentaria", "La leyenda dice CO = cono; la barrera se rotula BA."),
        ("abc", "{F} ¿Qué revisión del plano es la última?", "La revisión B", "La revisión A", "No se puede saber", "La ficha indica que la última revisión es la B."),
        ("abc", "{F} Una persona ve que el plano no incluye señales informativas en una curva y quiere dibujarlas. ¿Qué corresponde?", "Anotar la observación e informar al prevencionista o al jefe de obra", "Dibujarlas ella, porque conoce la curva", "Colocar las señales en el terreno sin avisar", "El plano lo modifica el proyectista; quien detecta una falta la informa."),
        ("abc", "{F} Se necesita revisar si las medidas protegen a trabajadores y conductores. ¿Quién cumple ese rol?", "El prevencionista de riesgos", "El camionero de la obra", "El proveedor de conos", "Revisar la seguridad corresponde al prevencionista; los otros no tienen ese rol."),
        ("ab", "{F} Un compañero dice: «con la revisión A impresa da lo mismo». ¿Qué respuesta es correcta?", "No: la última revisión es la B y la A puede haber cambiado", "Sí: todas las revisiones son iguales", "Cada revisión es una versión; la vigente es la última, que aquí es la B."),
        ("abc", "{F} El plano pide 24 conos y en bodega hay 20. ¿Qué es lo más prudente?", "Informar la falta de 4 conos antes de iniciar la faena", "Iniciar la faena con 20 y no avisar", "Usar objetos cualquiera como conos", "Una falta de dispositivos se informa; improvisar con objetos no cumple el plano."),
        ("=", "{F} Faltan 4 conos. Si cada cono de ejemplo cuesta $7.500, ¿cuánto cuesta reponerlos?", "4*7500", "Se multiplica la cantidad que falta por el precio de un cono.", " pesos"),
        ("abc", "{F} Un jefe de obra pide dejar 2 barreras de las 3 porque «no se nota». ¿Qué respuesta es correcta?", "Corresponde consultar al proyectista y al prevencionista antes de cambiar el plano", "Se puede, porque el jefe de obra coordina", "Se puede, si el chaleco reflectante compensa", "Quien coordina no modifica por sí solo un plano firmado; se consulta a quien diseña y a quien revisa seguridad."),
    ],
    ctx=("abc", "Un trabajador nuevo quiere mover una barrera «un poco» hacia la calzada para despejar su paso con una carretilla. ¿Qué responde un compañero?", "Que no la mueva y avise al jefe de obra, porque la posición de la barrera está definida en el plano", "Que la mueva rápido mientras no pasan autos", "Que la mueva si la devuelve después", "Mover una barrera cambia la protección; la posición la fija el plano y se consulta antes."),
    sc=[("En Obras Viales: ¿qué es una señal reglamentaria?", "Una señal que indica una obligación o una prohibición", "No avisa un peligro ni entrega un dato: fija una regla."),
        ("¿Qué se hace si el plano no tiene todas las señales necesarias?", "Anotar la observación e informar", "El plano lo modifica solo quien lo diseña."),
        ("¿Para qué sirve el cuadro de cantidades?", "Para saber cuántas piezas de cada tipo se necesitan", "Muestra el número de piezas, no el dibujo ni el precio total.")],
    op=("Plano de ejemplo «Camino Las Palmas», revisión C: SA 5; SR 3; SI 2; CO 30; BA 4. Bodega: 28 conos y 4 barreras. Escribe (a) cuántas señales hay en total, (b) cuántos conos faltan, (c) a quién informas la falta y por qué no la resuelves tú, (d) qué mira la revisión del plano.",
        "(a) 5+3+2 son 10 señales. (b) 30-28 son 2 conos. (c) Al jefe de obra y al prevencionista; el plano y su cumplimiento los decide quien corresponde. (d) Que usas la versión vigente (la C).",
        ["suma 10 señales", "calcula 2 conos faltantes", "informa a quien corresponde", "nombra la revisión vigente"],
        ["hoja con las cuatro respuestas"],
        ["sumar conos con señales", "improvisar conos", "usar una revisión antigua"],
        "Pregunta: «¿qué hace la persona que ve un cono faltante?». Si no responde, pídele que relea la regla de informar."),
    reinforce="Escribe los tres tipos de señales y, junto a cada uno, un ejemplo de mensaje inventado.",
    extend="Explica con un ejemplo por qué es riesgoso trabajar con una revisión antigua de un plano de señalización.",
)

# ============================================================ OAM-06, clase 3
F = ("Ficha 3 (lista de verificación de señalización, de ejemplo, inventada). Camino ficticio «Ruta Los Cóndores». Plano: 5 señales de advertencia, 20 conos, 2 barreras y 1 señal informativa de desvío. "
     "Inspección del prevencionista (datos entregados, el cuaderno no enseña cómo se instala): señales de advertencia presentes 4; conos presentes 20, de los cuales 3 están caídos; barreras presentes 2; señal informativa presente 1, pero tapada por un cartel de proveedor. "
     "Hora de la inspección: 17:40, con luz de tarde.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel una lista de verificación de señalización: qué cumple, qué falta y qué se informa.",
    prior=["Sé leer un plano de señalización.", "Sé comparar lo planificado con lo observado.", "Sé restar números enteros."],
    explain=[
        "Una lista de verificación compara lo que dice el plano con lo que observa quien inspecciona. Para cada elemento se anotan tres datos: cantidad planificada, cantidad presente y estado. El estado puede ser conforme (cumple lo del plano) o no conforme (falta, está dañado, caído o tapado). Una señal presente pero tapada no cumple su función, aunque esté en su lugar: sigue siendo no conforme. Se inspecciona con luz y a la hora en que hay más tránsito, porque la visibilidad cambia.",
        "Al terminar se anota la conclusión y se informa al jefe de obra y al prevencionista, quienes deciden las correcciones con personal autorizado. Quien revisa en papel no corrige en la calzada. Un registro útil dice qué elemento, cuántos, qué estado, quién inspeccionó, fecha y hora.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("lista de verificación", "tabla que compara lo planificado con lo observado"), ("conforme", "cumple lo que dice el plano"), ("no conforme", "falta, está dañado, caído o tapado, y no cumple el plano"), ("cantidad planificada", "cantidad que indica el plano"), ("cantidad presente", "cantidad observada en la inspección")],
    worked=[
        ("Clasificar", "En una lista de ejemplo, el plano pide 6 conos y la inspección encuentra 6, pero 1 está roto. ¿Cuántos son conformes?", ["Se restan los dañados del total presente.", "6 menos 1 son 5."], "5 conos"),
        ("Faltantes", "Una lista de ejemplo pide 3 señales y hay 2. ¿Cuántas faltan?", ["Se resta lo presente de lo planificado.", "3 menos 2 es 1."], "1 señal"),
    ],
    mistakes=[("Contar como conforme una señal presente pero tapada.", "Si no se ve, no cumple su función.", "Márcala como no conforme e informa."),
              ("Anotar solo «todo bien» sin cantidades ni hora.", "Un registro sin datos no respalda nada.", "Anota qué elemento, cuántos, estado, quién, fecha y hora.")],
    T=[
        ("abc", "En Obras Viales: ¿qué estado se anota para un cono presente pero caído?", "No conforme", "Conforme", "Informativo", "Un cono caído no cumple su función: es no conforme."),
        ("abc", "En una lista de verificación, la cantidad planificada es:", "La que indica el plano", "La que encontró quien inspecciona", "La que decide el camionero", "Lo planificado viene del plano; lo encontrado es la cantidad presente."),
        ("abc", "Una señal presente pero tapada por un cartel se anota como:", "No conforme", "Conforme porque está en su lugar", "Conforme si es de día", "Si la señal no se ve, no cumple su función aunque esté en su lugar."),
        ("=", "{F} ¿Cuántas señales de advertencia faltan?", "5-4", "Se resta lo presente de lo planificado.", " señal"),
        ("=", "{F} ¿Cuántos conos están conformes (presentes y no caídos)?", "20-3", "A los conos presentes se les restan los caídos.", " conos"),
        ("abc", "{F} ¿Cuántas barreras faltan?", "Ninguna: hay 2 y el plano pide 2", "Una", "Dos", "El plano pide 2 barreras y la inspección encontró 2."),
        ("abc", "{F} ¿Qué estado tiene la señal informativa de desvío?", "No conforme, porque está tapada por un cartel", "Conforme, porque está presente", "No aplica, porque es informativa", "Está presente pero tapada, por lo que no cumple su función."),
        ("=", "{F} ¿Cuántos elementos no conformes hay en total, contando señales que faltan, conos caídos y la señal tapada?", "(5-4)+3+1", "Se suman las señales que faltan, los conos caídos y la señal tapada.", " elementos"),
        ("abc", "{F} Se inspeccionó a las 17:40, con luz de tarde. ¿Por qué conviene anotar la hora?", "Porque la visibilidad cambia durante el día y la hora ayuda a interpretar el estado", "Porque la hora cambia la cantidad planificada", "Porque la hora reemplaza la firma", "La visibilidad depende de la hora; la hora no modifica el plano ni reemplaza la firma."),
        ("ab", "{F} Un compañero dice: «los 20 conos están presentes, entonces todo cumple». ¿Qué respuesta es correcta?", "No: 3 conos están caídos y son no conformes", "Sí: presente significa conforme", "La inspección debe mirar el estado de cada elemento, no solo si está presente."),
        ("abc", "{F} ¿Quién corrige las no conformidades en la calzada?", "Personal autorizado, decidido por el jefe de obra y el prevencionista", "La persona que hizo la inspección, de inmediato", "Cualquier trabajador con chaleco", "Corregir en la calzada exige autorización; quien inspecciona en papel informa."),
        ("=", "{F} Si cada señal de advertencia de ejemplo cuesta $12.000, ¿cuánto cuesta reponer las que faltan?", "(5-4)*12000", "Se multiplica la cantidad que falta por el precio de una señal.", " pesos"),
        ("abc", "{F} El prevencionista debe dejar un registro. ¿Cuál es el más completo?", "Elemento, cantidad planificada y presente, estado, quién inspeccionó, fecha y hora", "Solo «faltan señales»", "Solo el nombre de quien inspeccionó", "Un registro útil respalda cada hallazgo con datos y responsable."),
    ],
    ctx=("abc", "Al revisar una lista, ves que un cono caído está en plena calzada. ¿Qué haces según las reglas generales?", "No acercarte a la calzada, avisar al prevencionista o a un adulto responsable", "Cruzar corriendo a levantarlo", "Esperar a que un auto lo mueva", "Entrar a la calzada sin autorización es riesgoso; se avisa para que lo resuelva personal autorizado."),
    sc=[("En una lista de verificación: ¿qué es «no conforme»?", "Un elemento que falta, está dañado, caído o tapado", "No cumple lo que dice el plano."),
        ("Si el plano pide 8 conos y hay 5, ¿cuántos faltan?", "3 conos", "Se resta lo presente de lo planificado."),
        ("¿Quién corrige una no conformidad en la calzada?", "Personal autorizado", "Quien inspecciona en papel informa, no corrige.")],
    op=("Lista de ejemplo «Camino El Sauce»: el plano pide 4 señales de advertencia, 16 conos y 3 barreras. Inspección: señales presentes 4, una de ellas con el símbolo borrado; conos presentes 14, de los cuales 2 caídos; barreras presentes 3. Escribe (a) cuántos conos faltan, (b) cuántos conos están conformes, (c) qué estado tiene la señal con símbolo borrado, (d) a quién informas.",
        "(a) 16-14 son 2 conos que faltan. (b) 14-2 son 12 conos conformes. (c) No conforme, porque no se entiende su mensaje. (d) Al jefe de obra y al prevencionista.",
        ["calcula 2 conos faltantes", "calcula 12 conformes", "marca la señal no conforme", "informa a quien corresponde"],
        ["hoja con las cuatro respuestas"],
        ["contar los caídos como conformes", "decir que la señal borrada cumple", "decir que corrige él en la calzada"],
        "Pregunta: «¿una señal presente con símbolo borrado cumple?». Si duda, pídele que relea el criterio de función."),
    reinforce="Inventa una lista con tres elementos, cantidades planificadas y presentes, y marca conforme o no conforme en cada uno.",
    extend="Explica por qué una cantidad correcta de elementos no basta para decir que la señalización cumple.",
)

# ============================================================ OAM-06, clase 4
F = ("Ficha 4 (cálculo de dispositivos para un tramo, de ejemplo, inventada). Camino ficticio «Ruta Pehuén». Tramo de obra de 240 m. Criterio de ejemplo para esta planilla: un cono cada 8 m, incluidos ambos extremos del tramo. "
     "Precio de ejemplo: cono $7.500 (compra); arriendo de una barrera $3.000 por día. Se necesitan 2 barreras durante 10 días. Cada señal de advertencia de ejemplo cuesta $12.000 y se compran 6.")
build(
    O6, 4, F,
    use="Aprenderé a calcular en una planilla cuántos dispositivos y cuánto presupuesto necesita una señalización, con datos de ejemplo.",
    prior=["Sé leer un plano de señalización.", "Sé multiplicar y dividir números enteros.", "Sé calcular un costo total."],
    explain=[
        "Para presupuestar una señalización se cuentan las piezas y se multiplican por su precio. Cuando los elementos van repartidos a distancia fija, la cantidad se calcula dividiendo el largo del tramo por la separación y sumando 1 si se cuenta también el extremo final. Por ejemplo, si un tramo mide 30 m y hay un elemento cada 10 m, incluidos ambos extremos, hay 30 dividido en 10, más 1: cuatro elementos.",
        "Algunos elementos se compran y otros se arriendan. El arriendo se calcula multiplicando el valor por día, la cantidad de piezas y los días. Todos los criterios de este ejemplo son solo para practicar la planilla; la separación y las cantidades reales las fija el manual de carretera vigente y el plano de la obra. La planilla ayuda a presupuestar, no a instalar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("separación", "distancia fija entre un elemento y el siguiente"), ("extremo", "punto donde empieza o termina un tramo"), ("arriendo", "pago por usar una pieza durante días sin comprarla"), ("presupuesto", "cálculo del costo total de una compra o un servicio"), ("planilla", "tabla donde se ordenan datos y cálculos")],
    worked=[
        ("Elementos a distancia fija", "En un tramo de ejemplo de 60 m hay un elemento cada 10 m, incluidos ambos extremos. ¿Cuántos elementos son?", ["Se divide el largo por la separación y se suma 1.", "60 dividido en 10 son 6 y 6 más 1 son 7."], "7 elementos"),
        ("Arriendo", "Se arriendan 3 piezas de ejemplo a $2.000 por día durante 4 días. ¿Cuánto cuesta?", ["Se multiplican piezas, valor por día y días.", "3 por 2.000 son 6.000 y 6.000 por 4 son 24.000."], "$24.000"),
    ],
    mistakes=[("Olvidar sumar 1 cuando se cuentan ambos extremos del tramo.", "Hay un elemento más que tramos entre ellos.", "Divide el largo por la separación y suma 1."),
              ("Multiplicar el arriendo por piezas pero no por los días.", "El arriendo se cobra por cada día de uso.", "Multiplica piezas, valor diario y número de días.")],
    T=[
        ("abc", "En una planilla de señalización: ¿qué es la separación entre conos?", "La distancia fija entre un cono y el siguiente", "El precio de un cono", "El número de conos del plano", "La separación es una distancia; el precio y la cantidad son otros datos."),
        ("abc", "Un tramo de 20 m con un elemento cada 5 m, incluidos ambos extremos, tiene:", "5 elementos", "4 elementos", "20 elementos", "20 dividido en 5 son 4 espacios, y con ambos extremos hay 5 elementos."),
        ("abc", "El arriendo de una pieza se calcula multiplicando el valor por día por:", "Los días de uso y la cantidad de piezas", "Solo la cantidad de piezas", "Solo el largo del tramo", "El arriendo depende de los días y de cuántas piezas se arriendan."),
        ("=", "{F} ¿Cuántos conos se necesitan según el criterio de ejemplo?", "240//8+1", "Se divide el largo por la separación y se suma 1 por el extremo final.", " conos"),
        ("=", "{F} ¿Cuánto cuesta comprar esos conos?", "(240//8+1)*7500", "Se multiplica la cantidad de conos por el precio de uno.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el arriendo de las barreras?", "2*3000*10", "Se multiplican barreras, valor por día y días.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan las 6 señales de advertencia?", "6*12000", "Se multiplica la cantidad de señales por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de conos, barreras y señales?", "(240//8+1)*7500+2*3000*10+6*12000", "Se suman los tres costos calculados.", " pesos"),
        ("abc", "{F} Si el tramo se alargara a 320 m con el mismo criterio, ¿qué ocurre con la cantidad de conos?", "Aumenta, porque el largo dividido por la separación es mayor", "Queda igual, porque el precio no cambia", "Disminuye, porque hay más espacio", "Un tramo más largo con la misma separación necesita más elementos."),
        ("ab", "{F} Un compañero calcula 240 dividido en 8 y dice que son 30 conos. ¿Qué respuesta es correcta?", "Le falta sumar 1 por el cono del extremo final: son 31", "Está bien: son 30 conos", "Con ambos extremos incluidos, los espacios son 30 y los conos son uno más."),
        ("abc", "{F} Con un criterio de un cono cada 10 m en el mismo tramo, incluidos ambos extremos, ¿cuántos conos serían?", "25 conos", "24 conos", "240 conos", "240 dividido en 10 son 24 y se suma 1 por el extremo final."),
        ("=", "{F} Si el arriendo de las barreras se extendiera a 15 días, ¿cuánto costaría?", "2*3000*15", "Se multiplican barreras, valor por día y días.", " pesos"),
        ("abc", "{F} Un supervisor pide que el presupuesto incluya «un margen por si algo falla». ¿Cuál es la forma más clara de hacerlo?", "Anotar el margen como una línea separada, con su porcentaje o cantidad de ejemplo", "Subir los precios de cada pieza sin decirlo", "Eliminar las barreras del cálculo", "Un margen se muestra como línea propia para que la planilla sea transparente."),
    ],
    ctx=("abc", "Un proveedor ofrece reducir el precio del cono a la mitad si se reduce a la mitad la cantidad que pide el plano. ¿Qué corresponde?", "No cambiar la cantidad del plano sin consultar al prevencionista y al proyectista", "Aceptar, porque cuesta menos", "Aceptar si el chaleco reflectante compensa", "Reducir dispositivos por ahorro puede aumentar el riesgo; el plano solo se cambia con quien lo diseña y revisa."),
    sc=[("Un tramo de 50 m con un elemento cada 10 m, incluidos ambos extremos: ¿cuántos elementos?", "6 elementos", "50 dividido en 10 son 5 y se suma 1."),
        ("¿Cómo se calcula el arriendo de piezas?", "Piezas por valor diario por días", "Piezas, valor diario y días son tres factores que se multiplican."),
        ("¿Para qué sirve una planilla de presupuesto?", "Para calcular costos con datos de ejemplo, no para instalar", "Ordena cantidades y precios; no reemplaza el plano ni la autorización.")],
    op=("Planilla de ejemplo «Camino Los Aromos»: tramo de 180 m, un cono cada 6 m incluidos ambos extremos, cono $7.500; arriendo de 3 barreras a $2.500 por día durante 8 días. Escribe (a) cuántos conos, (b) el costo de los conos, (c) el costo del arriendo, (d) el total y una advertencia de quién instala.",
        "(a) 180 dividido en 6 son 30, más 1 son 31 conos. (b) 31*7.500 = $232.500. (c) 3*2.500*8 = $60.000. (d) $292.500; la instalación la hace personal autorizado.",
        ["calcula 31 conos", "calcula el costo de los conos", "calcula el arriendo", "suma el total y advierte la autorización"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar 1", "no multiplicar por los días", "decir que él instala"],
        "Pregunta: «¿por qué se suma 1?». Si no responde, pídele que dibuje 3 conos y cuente los espacios."),
    reinforce="Calcula cuántos conos hay en un tramo inventado de 70 m con un cono cada 10 m, incluidos ambos extremos.",
    extend="Explica por qué ahorrar dispositivos para bajar el presupuesto puede aumentar el riesgo de atropello.",
)

# ============================================================ OAM-07, clase 1
F = ("Ficha 1 (programa de conservación de ejemplo, inventado). Camino ficticio «Ruta Altos del Valle», de 12 km. Documentos: programa de conservación (4 páginas), registro de inspección (1 planilla) y plan de prevención de riesgos (5 páginas). "
     "Tareas del programa: inspección visual del camino a razón de 3 km por día con un equipo; toma de muestras de la carpeta de rodado, a cargo de personal autorizado del laboratorio; y verificación de desplazamientos de 1 muro de contención, 1 defensa, 1 corte y 1 terraplén. "
     "Daños anotados: grietas, baches y erosión del talud. Riesgos anotados: atropello por el tránsito, caída de material del talud, polvo y ruido.")
build(
    O7, 1, F,
    use="Aprenderé qué es la conservación de un camino, qué tareas incluye, qué documentos la respaldan y qué riesgos hay que reconocer, sin aprender a ejecutarlas.",
    prior=["Sé qué es una faena vial y qué es un registro de control.", "Sé multiplicar y dividir números enteros.", "Sé qué es el atropello."],
    explain=[
        "La conservación vial reúne las tareas periódicas que mantienen un camino en buen estado después de construido. La carpeta de rodado es la capa superior por donde circulan los vehículos. Con el tiempo aparecen daños: grietas, baches y erosión del talud, que es la ladera inclinada junto al camino. Un muro de contención sostiene un terreno; una defensa protege el camino de ríos o caídas de material; un corte es una excavación hecha en un cerro junto al camino; un terraplén es un relleno elevado que sostiene el camino.",
        "El programa de conservación dice qué tareas se hacen, cuándo y con qué exigencias, según el manual de carretera, las normas del laboratorio vial y las normas ambientales vigentes. Las tareas con equipos, muestras o cerca de taludes las realiza personal autorizado. Los riesgos principales son el atropello por el tránsito, la caída de material de un talud y el atrapamiento con equipos. El plan de prevención de riesgos ordena las medidas; el EPP va al final de la jerarquía de controles.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("conservación vial", "tareas periódicas que mantienen un camino en buen estado"), ("carpeta de rodado", "capa superior del camino por donde circulan los vehículos"), ("talud", "ladera inclinada junto al camino"), ("muro de contención", "muro que sostiene un terreno"), ("defensa", "obra que protege el camino de un río o de caídas de material"), ("corte", "excavación hecha en un cerro junto al camino"), ("terraplén", "relleno elevado que sostiene el camino"), ("erosión", "desgaste del terreno por el agua o el viento"), ("registro de inspección", "planilla donde se anotan los daños observados")],
    worked=[
        ("Elegir el documento", "Una jefa de conservación de ejemplo quiere saber qué tareas y qué fechas tiene el trabajo del año. ¿Qué documento consulta?", ["Las tareas y sus plazos se escriben en el programa.", "Ese documento es el programa de conservación."], "El programa de conservación"),
        ("Contar días", "Un equipo de ejemplo inspecciona 4 km por día. ¿Cuántos días necesita para 20 km?", ["Se divide el largo por lo que se avanza cada día.", "20 dividido en 4 son 5."], "5 días"),
    ],
    mistakes=[("Acercarse al pie de un talud con grietas nuevas para «mirar mejor».", "Puede caer material y provocar un accidente grave.", "Mantente lejos de la zona de riesgo y avisa al responsable."),
              ("Creer que leer el programa habilita para tomar muestras o manejar equipos.", "Esas tareas exigen personal autorizado.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es la conservación vial?", "Las tareas periódicas que mantienen en buen estado un camino ya construido", "La construcción de un camino nuevo desde cero", "El cambio completo del trazado de un camino", "Conservar es mantener lo existente; construir o cambiar el trazado son otras tareas."),
        ("abc", "¿Cómo se llama la capa superior del camino por donde circulan los vehículos?", "Carpeta de rodado", "Terraplén", "Talud", "La carpeta de rodado es la capa de circulación; el terraplén es un relleno y el talud una ladera."),
        ("abc", "Una persona se ubica al pie de un talud con grietas nuevas. ¿Qué riesgo principal corre?", "Caída de material del talud", "Pérdida de las guías de despacho", "Aumento del precio del material", "Un talud agrietado puede desprender material sobre quien está debajo."),
        ("=", "{F} ¿Cuántos días necesita un equipo para inspeccionar todo el camino a ese ritmo?", "12//3", "Se divide el largo del camino por lo que se avanza cada día.", " días"),
        ("abc", "{F} ¿En qué documento se anotan los daños observados durante la inspección?", "En el registro de inspección", "En el plan de prevención de riesgos", "En las normas ambientales", "El registro de inspección es la planilla de daños; el plan trata la prevención."),
        ("abc", "{F} ¿Quién toma las muestras de la carpeta de rodado según el programa?", "Personal autorizado del laboratorio", "Cualquier estudiante que visite la obra", "El conductor de un camión que pasa", "El programa asigna esa tarea a personal autorizado del laboratorio."),
        ("=", "{F} Un día no se inspecciona por lluvia. ¿Cuántos días de calendario toma terminar la inspección completa?", "12//3+1", "A los días de trabajo se suma el día perdido por lluvia.", " días"),
        ("abc", "{F} Un visitante quiere tomar una muestra «para ayudar». ¿Qué corresponde?", "No hacerlo: la toma de muestras la realiza personal autorizado", "Hacerlo si usa casco", "Hacerlo si el jefe lo mira de lejos", "El casco o la mirada de otro no reemplazan la autorización para esa tarea."),
        ("ab", "{F} Un estudiante dice: «ya leí el programa, así que puedo hacer la verificación del terraplén en terreno». ¿Qué respuesta es correcta?", "No: leer el programa no habilita; en terreno lo hace personal autorizado", "Sí: el programa lo habilita", "Entender un programa es distinto de estar autorizado para trabajar en terreno."),
        ("abc", "{F} Se debe reducir el riesgo de caída de material del talud. Según la jerarquía de controles, ¿qué es lo más eficaz?", "Evitar que haya personas en la zona expuesta mientras el talud no esté controlado", "Entregar un casco más a cada persona", "Pedirles que corran si cae material", "Alejar a las personas actúa sobre el peligro; el casco y correr quedan al final."),
        ("=", "{F} Dos equipos inspeccionan a la vez, cada uno a 3 km por día. ¿Cuántos días se necesitan para los 12 km?", "12//(2*3)", "Se divide el largo por el avance diario combinado de los dos equipos.", " días"),
        ("abc", "{F} Un inspector propone caminar por la calzada para ver mejor las grietas mientras pasan vehículos. ¿Qué corresponde?", "Consultar al prevencionista: trabajar junto al tránsito exige señalización y personal autorizado", "Hacerlo con chaleco reflectante", "Hacerlo si es de día", "El chaleco o la luz del día no reemplazan las medidas de separación del tránsito."),
        ("abc", "{F} Un registro de inspección tiene daños anotados pero no tiene fecha ni lugar. ¿Qué se concluye?", "Está incompleto: no se puede ubicar ni respaldar lo observado", "Está completo, porque lo importante son los daños", "Está completo si lo firma el conductor", "Un registro útil deja constancia de qué, dónde, cuándo y quién."),
    ],
    ctx=("abc", "Cae material desde un talud y una persona queda atrapada junto al camino. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse a sacarla a mano rápidamente", "Esperar sin avisar a nadie", "Acercarse puede provocar una nueva caída de material; se avisa de inmediato a quienes están autorizados."),
    sc=[("En Obras Viales: ¿qué es un talud?", "La ladera inclinada junto al camino", "El talud es una ladera; el terraplén es un relleno que sostiene el camino."),
        ("¿Qué se hace si el programa y el registro se contradicen?", "Anotar la diferencia e informar al responsable", "No se elige uno al azar porque podría ser el equivocado."),
        ("¿Quién toma muestras y trabaja cerca de taludes?", "Personal autorizado con norma vigente", "Este cuaderno no habilita para intervenir caminos.")],
    op=("Programa de ejemplo «Camino Las Vertientes»: 18 km, inspección a 6 km por día; un talud con grietas nuevas junto al km 7. Escribe (a) cuántos días de inspección hacen falta, (b) en qué documento anotas las grietas, (c) un riesgo del talud y una medida de la jerarquía de controles, (d) quién toma muestras de la carpeta de rodado.",
        "(a) 18 dividido en 6 son 3 días. (b) En el registro de inspección. (c) Caída de material; alejar a las personas de la zona expuesta. (d) Personal autorizado del laboratorio.",
        ["calcula 3 días", "nombra el registro de inspección", "nombra riesgo y medida", "indica quién toma muestras"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar en vez de dividir", "poner el EPP como primera medida", "decir que él toma muestras"],
        "Pregunta: «¿cuál es la medida más eficaz frente a un talud agrietado?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe cuatro tipos de daño de un camino (grieta, bache, erosión y otro) y qué documento los registra.",
    extend="Explica con un ejemplo inventado por qué un registro con fecha y lugar ayuda a comparar el estado de un camino de un año a otro.",
)

# ============================================================ OAM-07, clase 2
F = ("Ficha 2 (ficha de muestra y de hitos, de ejemplo, inventada). Camino ficticio «Ruta El Boldo». Ubicación por estación: «km 3+200» significa 3 kilómetros y 200 metros desde el inicio. "
     "Ficha de muestra M-07: carpeta de rodado, estación km 3+200, fecha 10/03 (de ejemplo), tomada por personal autorizado del laboratorio, destino: laboratorio vial (de ejemplo). Sin firma de quien la recibe. "
     "Hitos de control del muro de contención: H1 y H2 (puntos fijos con marca). Desplazamiento = cambio de posición del hito respecto de su referencia, en milímetros (mm).")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario de las muestras y de los desplazamientos: estación, ficha de muestra, hito de control y referencia.",
    prior=["Sé qué es la conservación vial.", "Sé pasar de kilómetros a metros.", "Sé restar números enteros."],
    explain=[
        "Una muestra es una porción de material que representa al resto y se envía al laboratorio para ensayarla. Cada muestra lleva una ficha con código, estación (ubicación en el camino), fecha, quién la tomó y a dónde va. La estación «km 3+200» significa 3 kilómetros y 200 metros desde el inicio, es decir 3.200 m. Sin código ni ubicación, la muestra pierde su valor, porque no se sabe de qué parte del camino viene.",
        "Un hito de control es un punto fijo con marca, puesto en un muro, defensa, corte o terraplén. El desplazamiento es el cambio de posición del hito respecto de su referencia, que es un punto que no se mueve. Se anota en milímetros (mm) y se compara con un valor de alerta que fija el proyecto. Quien lee los datos no los modifica: si algo falta, lo informa. Las normas del laboratorio vial y el manual de carretera fijan los detalles reales.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("muestra", "porción de material que representa al resto y se envía al laboratorio"), ("ficha de muestra", "hoja con el código, la estación, la fecha, quién tomó la muestra y su destino"), ("estación", "ubicación en el camino medida desde el inicio, como km 3+200"), ("hito de control", "punto fijo con marca para medir si una obra se mueve"), ("desplazamiento", "cambio de posición de un hito respecto de su referencia"), ("referencia", "punto que se supone que no se mueve"), ("valor de alerta", "valor fijado por el proyecto que, si se supera, se debe informar")],
    worked=[
        ("Pasar la estación a metros", "Una estación de ejemplo es km 2+500. ¿A cuántos metros desde el inicio está?", ["2 kilómetros son 2.000 m.", "Se suman los 500 m: 2.000 más 500 son 2.500."], "2.500 m"),
        ("Calcular el desplazamiento", "Un hito de ejemplo marcaba 1 mm respecto de su referencia y ahora marca 4 mm. ¿Cuánto se desplazó entre las dos lecturas?", ["Se resta la posición inicial de la actual.", "4 menos 1 son 3."], "3 mm"),
    ],
    mistakes=[("Archivar una muestra sin código ni estación.", "No se sabe de qué parte del camino viene y no sirve como respaldo.", "Exige que cada ficha tenga código, estación, fecha, quién y destino."),
              ("Medir el desplazamiento contra un punto que también se mueve.", "Si la referencia se mueve, la medida no es confiable.", "Compara siempre con la referencia fija del proyecto.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es una muestra de carpeta de rodado?", "Una porción de material que representa al resto y se envía al laboratorio", "El plano donde se dibuja el camino", "Una medida del desplazamiento de un muro", "Una muestra es material representativo; el plano y el desplazamiento son otra cosa."),
        ("abc", "¿Qué dato de una ficha de muestra indica de qué parte del camino viene?", "La estación", "El destino", "La firma de recepción", "La estación es la ubicación en el camino; el destino dice adónde va."),
        ("abc", "Un hito de control sirve para:", "Medir si una obra, como un muro, se mueve", "Pesar el material de un camión", "Pagar a la empresa", "Un hito es un punto fijo con marca para detectar desplazamientos."),
        ("=", "{F} ¿A cuántos metros desde el inicio está la estación km 3+200?", "3*1000+200", "Cada kilómetro tiene 1.000 m; se suman los 200 m.", " m"),
        ("abc", "{F} ¿Qué dato falta en la ficha de la muestra M-07?", "La firma de quien la recibe", "La fecha", "La estación", "La ficha trae fecha y estación, pero indica que no tiene firma de recepción."),
        ("abc", "{F} ¿Respecto de qué se mide el desplazamiento de los hitos H1 y H2?", "Respecto de su referencia", "Respecto del camión más cercano", "Respecto de la fecha de la muestra", "El desplazamiento es el cambio de posición respecto de un punto que no se mueve."),
        ("=", "{F} Una segunda muestra se tomó en el km 5+700. ¿Cuántos metros hay entre las dos estaciones?", "(5*1000+700)-(3*1000+200)", "Se pasan ambas estaciones a metros y se resta la menor de la mayor.", " m"),
        ("abc", "{F} La estudiante recibe la ficha M-07 sin firma de recepción y la archiva. ¿Qué es lo más prudente?", "Informar que falta la firma antes de archivarla", "Firmarla ella en nombre de otra persona", "Borrar la muestra del registro", "No se firma por otra persona ni se borra; se informa lo que falta."),
        ("abc", "{F} Un compañero no recuerda el código de otra muestra y propone «inventar uno parecido». ¿Qué corresponde?", "No inventarlo: se consulta el registro del laboratorio", "Inventarlo si es parecido", "Usar el de la muestra M-07", "Un código inventado rompe el respaldo; se busca el dato original."),
        ("ab", "{F} Un joven dice: «H1 se movió 4 mm, entonces el muro se rompió». ¿Qué respuesta es correcta?", "No: 4 mm es un dato; se compara con el valor de alerta del proyecto y se informa", "Sí: cualquier movimiento significa que se rompió", "Un desplazamiento se interpreta comparándolo con el valor de alerta y por personal competente."),
        ("abc", "{F} El hito H1 estaba a 2 mm de su referencia y ahora está a 5 mm. ¿Cuánto se desplazó entre las dos lecturas?", "3 mm", "7 mm", "5 mm", "Se resta la lectura anterior de la actual: 5 menos 2 son 3."),
        ("=", "{F} H2 estaba a 6 mm de su referencia y ahora está a 15 mm. ¿Cuántos mm se desplazó entre las dos lecturas?", "15-6", "Se resta la lectura anterior de la actual.", " mm"),
        ("abc", "{F} Un dato de desplazamiento parece «raro» porque es muy distinto del anterior. ¿Qué se hace?", "Se registra tal cual y se informa al responsable para que lo revise", "Se corrige el número para que se parezca al anterior", "Se borra la lectura", "Los datos no se modifican; se registran e informan para que los revise quien corresponde."),
    ],
    ctx=("abc", "Alguien propone subirse a la parte alta de un muro de contención para «medir mejor» el hito H2. ¿Qué respuesta es la más prudente?", "No hacerlo: las mediciones en altura o sobre estructuras las realiza personal autorizado y con plan de seguridad", "Hacerlo rápido, mientras nadie mira", "Hacerlo si lleva casco", "Subirse a una estructura sin autorización ni plan es riesgoso; el casco no lo resuelve."),
    sc=[("En Obras Viales: ¿qué es una estación como «km 2+100»?", "La ubicación en el camino: 2 kilómetros y 100 metros", "Equivale a 2.100 m desde el inicio."),
        ("¿Qué es el desplazamiento de un hito?", "El cambio de posición respecto de su referencia", "Se mide contra un punto que no se mueve."),
        ("¿Qué se hace si falta la firma en una ficha de muestra?", "Informar que falta, sin firmar por otra persona", "Firmar por otro altera el respaldo del registro.")],
    op=("Ficha de ejemplo: muestra M-12, carpeta de rodado, estación km 6+400, fecha 22/04 (de ejemplo), sin quién la tomó. Hito H3 de un terraplén: lectura anterior 2 mm, lectura actual 6 mm. Escribe (a) la estación en metros, (b) qué dato falta en la ficha, (c) cuántos mm se desplazó H3, (d) a quién informas.",
        "(a) 6.400 m. (b) Falta quién tomó la muestra. (c) 6-2 son 4 mm. (d) Al responsable del laboratorio y al jefe de conservación.",
        ["calcula 6.400 m", "nombra el dato que falta", "calcula 4 mm", "indica a quién informa"],
        ["hoja con las cuatro respuestas"],
        ["sumar 6 más 400", "decir que inventa el dato", "decir que el hito se rompió"],
        "Pregunta: «¿qué haces si falta un dato en la ficha?». Si no responde, pídele que relea la regla de informar."),
    reinforce="Pasa a metros las estaciones km 1+300, km 4+050 y km 9+900.",
    extend="Explica por qué una muestra sin estación pierde valor aunque el ensayo del laboratorio esté bien hecho.",
)

# ============================================================ OAM-07, clase 3
F = ("Ficha 3 (planilla de lecturas de desplazamiento, de ejemplo, inventada). Muro de contención ficticio del camino «Ruta Las Vegas». Valor de alerta de ejemplo: desplazamiento acumulado de 10 mm o más. "
     "Lecturas acumuladas respecto de la referencia, en mm (datos entregados por el equipo de control; el cuaderno no enseña cómo se miden): "
     "Hito H1: enero 0, abril 2, julio 3, octubre 4. Hito H2: enero 0, abril 3, julio 8, octubre 14. Hito H3: enero 0, abril 0, julio 1, octubre 1. "
     "Observación de la bitácora: en julio hubo lluvias fuertes cerca del hito H2.")
build(
    O7, 3, F,
    use="Aprenderé a analizar en papel una planilla de lecturas de desplazamiento: ver la tendencia, comparar con el valor de alerta y decidir qué se informa.",
    prior=["Sé qué es un hito de control y un desplazamiento.", "Sé restar números enteros.", "Sé comparar un valor con un límite."],
    explain=[
        "Una planilla de lecturas muestra cómo cambia la posición de cada hito en el tiempo. La lectura acumulada es el desplazamiento total desde la primera lectura. La variación entre lecturas es la diferencia entre una lectura y la anterior; si crece cada vez más, la tendencia es de aceleración y merece más atención. El valor de alerta es un límite fijado por el proyecto: cuando una lectura lo alcanza o lo supera, se informa de inmediato al responsable.",
        "Quien analiza la planilla no decide qué obra de reparación hacer, ni se acerca al muro para comprobar: informa con los datos. Una observación, como una lluvia fuerte, ayuda a entender la posible causa, pero no cambia el resultado. Si hay riesgo de colapso o caída de material, nadie se acerca a la zona hasta que lo indique personal autorizado.",
        f"Las cifras de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("lectura acumulada", "desplazamiento total desde la primera lectura"), ("variación", "diferencia entre una lectura y la anterior"), ("tendencia", "forma en que cambian los datos a lo largo del tiempo"), ("valor de alerta", "límite fijado por el proyecto que, si se alcanza, se informa de inmediato"), ("colapso", "caída o derrumbe de una estructura")],
    worked=[
        ("Variación entre lecturas", "Un hito de ejemplo marcó 3 mm en una lectura y 7 mm en la siguiente. ¿Cuál es la variación?", ["Se resta la lectura anterior de la actual.", "7 menos 3 son 4."], "4 mm"),
        ("Comparar con la alerta", "Con un valor de alerta de ejemplo de 12 mm, un hito marca 12 mm. ¿Se informa?", ["La alerta se alcanza cuando la lectura es igual o mayor.", "12 es igual a 12."], "Sí, se informa"),
    ],
    mistakes=[("Esperar a superar el valor de alerta para informar cuando ya se alcanzó.", "Alcanzar el valor ya activa la alerta.", "Informa cuando la lectura sea igual o mayor que el valor de alerta."),
              ("Dar por normal un hito porque «el total aún es bajo» aunque la variación crece cada vez más.", "Una tendencia que se acelera es una señal de atención.", "Mira la variación entre lecturas, no solo el total.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es la lectura acumulada de un hito?", "El desplazamiento total desde la primera lectura", "La diferencia entre dos hitos distintos", "El precio de medir el muro", "La lectura acumulada suma todo el movimiento desde el inicio."),
        ("abc", "La variación entre lecturas es:", "La diferencia entre una lectura y la anterior", "La suma de todos los hitos", "El valor de alerta del proyecto", "La variación compara una lectura con la anterior."),
        ("abc", "Si una lectura es igual al valor de alerta, ¿qué corresponde?", "Informar de inmediato al responsable", "Esperar a la siguiente lectura", "Ignorarla, porque no lo supera", "Alcanzar el valor de alerta ya obliga a informar."),
        ("=", "{F} ¿Cuál es la variación de H2 entre julio y octubre?", "14-8", "Se resta la lectura de julio de la de octubre.", " mm"),
        ("abc", "{F} ¿Qué hitos alcanzan o superan el valor de alerta en octubre?", "Solo H2", "H1 y H2", "Ninguno", "H2 marca 14 mm, sobre los 10 mm; H1 marca 4 y H3 marca 1."),
        ("abc", "{F} ¿Qué hito se desplazó menos en total hasta octubre?", "H3", "H1", "H2", "H3 marca 1 mm, menos que H1 (4) y H2 (14)."),
        ("=", "{F} ¿Cuántos mm superó H2 el valor de alerta en octubre?", "14-10", "Se resta el valor de alerta de la lectura de octubre.", " mm"),
        ("abc", "{F} Las variaciones de H2 por período son 3, 5 y 6 mm. ¿Qué tendencia se observa?", "Aumenta cada período: se acelera", "Disminuye cada período", "Se mantiene igual", "Las variaciones 3, 5 y 6 crecen en cada período."),
        ("abc", "{F} ¿Qué se hace con el hito H2 en octubre?", "Informar de inmediato al responsable, con los datos y la observación de la lluvia", "Solo anotar el dato y esperar a enero", "Acercarse al muro para medir de nuevo", "Un hito sobre el valor de alerta se informa de inmediato; acercarse no está autorizado."),
        ("ab", "{F} Un compañero dice: «H2 se movió por la lluvia, así que no es necesario informar». ¿Qué respuesta es correcta?", "No: la lluvia explica una posible causa, pero el dato igual se informa", "Sí: si hay una causa natural no se informa", "Una observación ayuda a entender el dato, no lo reemplaza ni lo anula."),
        ("abc", "{F} El jefe quiere saber si H1 requiere alerta. ¿Qué respuesta es correcta?", "No la alcanza: su lectura de octubre es 4 mm y la alerta es 10 mm", "Sí: hay lecturas en todos los períodos", "Sí: tiene más lecturas que H3", "La alerta se compara con el valor, no con la cantidad de lecturas."),
        ("=", "{F} ¿Cuántos mm suman en octubre las lecturas acumuladas de los tres hitos?", "4+14+1", "Se suman las lecturas de octubre de H1, H2 y H3.", " mm"),
        ("abc", "{F} Hay riesgo de colapso del muro cerca de H2. ¿Qué se hace según las reglas generales?", "Nadie se acerca a la zona de riesgo; se avisa a un adulto responsable y a emergencias", "Se manda a un trabajador a revisar el muro de cerca", "Se espera a ver si el muro aguanta una semana", "Con riesgo de colapso no se acerca nadie; se avisa de inmediato."),
    ],
    ctx=("abc", "Un conductor ve caer material del talud junto a un muro y se detiene a mirar desde cerca. ¿Qué respuesta es la más prudente?", "Alejarse de la zona, avisar a un adulto responsable y a emergencias", "Bajar a tomar fotos de cerca", "Intentar remover el material con las manos", "Acercarse a un talud inestable puede provocar un accidente; se avisa a quienes pueden actuar."),
    sc=[("¿Qué se hace cuando una lectura alcanza el valor de alerta?", "Se informa de inmediato", "La alerta se activa al alcanzar el valor, no solo al superarlo."),
        ("Lecturas 2 y 5 mm: ¿cuál es la variación?", "3 mm", "Se resta la lectura anterior de la actual."),
        ("¿Una lluvia cambia el resultado de una lectura?", "No, solo ayuda a entender la causa", "La observación da contexto, pero el dato sigue igual.")],
    op=("Planilla de ejemplo «Defensa Río Hondo», valor de alerta 8 mm: hito K1: marzo 0, junio 2, septiembre 5, diciembre 9; hito K2: marzo 0, junio 1, septiembre 2, diciembre 2. Observación: en septiembre hubo crecida del río. Escribe (a) la variación de K1 entre septiembre y diciembre, (b) qué hito supera la alerta en diciembre, (c) la tendencia de K1, (d) qué haces y quién debe acercarse a la obra.",
        "(a) 9-5 son 4 mm. (b) K1 (9 mm, sobre 8). (c) Aumenta en cada período: 2, 3 y 4 mm de variación; se acelera. (d) Informo de inmediato al responsable con los datos y la crecida; no me acerco, solo personal autorizado.",
        ["calcula 4 mm", "nombra K1", "describe la tendencia", "informa y no se acerca"],
        ["hoja con las cuatro respuestas"],
        ["decir que K2 supera la alerta", "ignorar la tendencia", "acercarse a medir"],
        "Pregunta: «¿qué hito alcanza la alerta?». Si no responde, pídele que compare cada lectura con 8 mm."),
    reinforce="Con lecturas inventadas de 0, 3, 4 y 9 mm y una alerta de 8 mm, calcula las tres variaciones y marca cuándo se alcanza la alerta.",
    extend="Explica por qué la variación entre lecturas puede avisar de un problema antes de que se alcance el valor de alerta.",
)

# ============================================================ OAM-07, clase 4
F = ("Ficha 4 (presupuesto de conservación, de ejemplo, inventado). Camino ficticio «Ruta Los Quillayes», 10 km. Partidas de la planilla (precios y cantidades de ejemplo): "
     "reparación de 14 baches a $45.000 cada uno; sellado de 600 m de grietas a $1.500 por metro; limpieza de 2.000 m de cunetas a $400 por metro. "
     "Plan de muestras de la carpeta de rodado: una muestra cada 2 km, incluidos ambos extremos del camino, con un ensayo de ejemplo a $35.000 por muestra.")
build(
    O7, 4, F,
    use="Aprenderé a presupuestar en una planilla las partidas de conservación y a contar las muestras de un plan, con datos de ejemplo.",
    prior=["Sé qué tareas incluye la conservación vial.", "Sé multiplicar y sumar números enteros.", "Sé que un elemento cada cierta distancia, con ambos extremos, lleva un elemento más."],
    explain=[
        "Un presupuesto de conservación se arma por partidas. Una partida es una tarea con su cantidad, su unidad y su precio unitario. El costo de una partida es la cantidad por el precio unitario, y el total es la suma de todas. Una planilla ordenada tiene una columna por partida, cantidad, unidad, precio unitario y subtotal. Las unidades importan: no se multiplica un precio por metro con una cantidad en kilómetros sin convertir antes.",
        "Para las muestras de un plan, si hay una muestra cada cierta distancia y se cuentan ambos extremos, la cantidad es el largo dividido por la separación más 1. Cada muestra tiene un costo de ensayo. Todos los precios y cantidades de este cuaderno son de ejemplo; los valores reales dependen del proyecto. La planilla sirve para presupuestar y priorizar, no para ejecutar las tareas.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("partida", "tarea del presupuesto con su cantidad y su precio unitario"), ("precio unitario", "precio por cada unidad de medida, como un metro o un bache"), ("subtotal", "costo de una partida: cantidad por precio unitario"), ("cuneta", "canal al borde del camino que lleva el agua"), ("sellado de grietas", "partida de conservación que cubre grietas de la carpeta de rodado"), ("ensayo", "prueba de laboratorio con resultado numérico")],
    worked=[
        ("Subtotal de una partida", "Una partida de ejemplo repara 5 baches a $30.000 cada uno. ¿Cuál es el subtotal?", ["Se multiplica la cantidad por el precio unitario.", "5 por 30.000 son 150.000."], "$150.000"),
        ("Muestras de un plan", "En un camino de ejemplo de 6 km hay una muestra cada 3 km, incluidos ambos extremos. ¿Cuántas muestras son?", ["Se divide el largo por la separación y se suma 1.", "6 dividido en 3 son 2 y 2 más 1 son 3."], "3 muestras"),
    ],
    mistakes=[("Multiplicar metros por un precio por kilómetro sin convertir.", "Las unidades no coinciden y el costo sale mal.", "Convierte las unidades antes de multiplicar."),
              ("Olvidar sumar 1 al contar muestras con ambos extremos.", "Hay una muestra más que espacios entre muestras.", "Divide el largo por la separación y suma 1.")],
    T=[
        ("abc", "En un presupuesto de conservación: ¿qué es una partida?", "Una tarea con su cantidad y su precio unitario", "El total de todas las tareas", "El nombre del laboratorio", "La partida es una tarea con cantidad y precio; el total es la suma de todas."),
        ("abc", "El subtotal de una partida se calcula como:", "Cantidad por precio unitario", "Cantidad más precio unitario", "Precio unitario dividido en la cantidad", "Cada unidad cuesta su precio unitario; el subtotal multiplica por la cantidad."),
        ("abc", "Un camino de 8 km con una muestra cada 4 km, incluidos ambos extremos, tiene:", "3 muestras", "2 muestras", "4 muestras", "8 dividido en 4 son 2 espacios, y con ambos extremos hay 3 muestras."),
        ("=", "{F} ¿Cuál es el subtotal de la reparación de baches?", "14*45000", "Se multiplica la cantidad de baches por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el subtotal del sellado de grietas?", "600*1500", "Se multiplican los metros de grietas por el precio por metro.", " pesos"),
        ("=", "{F} ¿Cuál es el subtotal de la limpieza de cunetas?", "2000*400", "Se multiplican los metros de cuneta por el precio por metro.", " pesos"),
        ("=", "{F} ¿Cuál es el total de las tres partidas?", "14*45000+600*1500+2000*400", "Se suman los subtotales de las tres partidas.", " pesos"),
        ("=", "{F} ¿Cuántas muestras hay en el plan?", "10//2+1", "Se divide el largo por la separación y se suma 1 por el extremo final.", " muestras"),
        ("=", "{F} ¿Cuánto cuestan los ensayos de todas las muestras?", "(10//2+1)*35000", "Se multiplica la cantidad de muestras por el costo de un ensayo.", " pesos"),
        ("abc", "{F} ¿Cuál es la partida de mayor subtotal?", "El sellado de grietas", "La reparación de baches", "La limpieza de cunetas", "Los subtotales son 630.000, 900.000 y 800.000: el mayor es el del sellado de grietas."),
        ("ab", "{F} Un compañero afirma: «la partida más cara es la de baches porque cada bache cuesta más». ¿Qué respuesta es correcta?", "No: se compara el subtotal, y el sellado de grietas tiene el subtotal mayor", "Sí: la partida más cara tiene el precio unitario mayor", "El costo de una partida depende de la cantidad por el precio, no solo del precio unitario."),
        ("abc", "{F} Se agregan 4 baches más a la partida de baches. ¿Cuánto sube el subtotal?", "$180.000", "$45.000", "$630.000", "Cada bache cuesta $45.000; 4 baches suben el subtotal en $180.000."),
        ("abc", "{F} Un supervisor pide ejecutar una reparación «con el personal de la planilla» sin autorización de seguridad. ¿Qué corresponde?", "Recordar que la planilla solo presupuesta: la ejecución exige personal autorizado y plan de prevención", "Hacerlo porque la partida está presupuestada", "Hacerlo si hay chaleco reflectante", "Una partida presupuestada no autoriza a ejecutar sin las condiciones de seguridad."),
    ],
    ctx=("abc", "Un presupuesto de ejemplo suma mal: multiplicó 2 km de cunetas por un precio por metro sin convertir. ¿Qué debe hacer quien revisa?", "Señalar el error de unidad e informar al responsable de la planilla", "Dejar el total como está para no atrasar", "Cambiar el precio por metro por uno inventado", "Un error de unidad cambia el total; se informa y corrige con quien elabora la planilla."),
    sc=[("¿Cómo se calcula el subtotal de una partida?", "Cantidad por precio unitario", "Se multiplica cuánto se hace por lo que cuesta cada unidad."),
        ("Un camino de 12 km con una muestra cada 6 km, incluidos ambos extremos: ¿cuántas muestras?", "3 muestras", "12 dividido en 6 son 2, y se suma 1 por el extremo final."),
        ("¿Qué hace una planilla de presupuesto?", "Calcula costos con datos de ejemplo, no ejecuta tareas", "Presupuestar no habilita para trabajar en terreno.")],
    op=("Planilla de ejemplo «Camino Los Maitenes», 8 km: reparación de 10 baches a $40.000; sellado de 400 m de grietas a $1.800 por metro; plan de una muestra cada 4 km con ambos extremos y ensayo de $30.000 por muestra. Escribe (a) el subtotal de baches, (b) el subtotal de grietas, (c) el costo de los ensayos, (d) el total y quién ejecuta las tareas.",
        "(a) 10*40.000 = $400.000. (b) 400*1.800 = $720.000. (c) 8 dividido en 4 son 2, más 1 son 3 muestras: 3*30.000 = $90.000. (d) $1.210.000; las tareas las ejecuta personal autorizado.",
        ["calcula $400.000", "calcula $720.000", "calcula 3 muestras y $90.000", "suma el total y nombra personal autorizado"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar 1", "sumar en vez de multiplicar", "decir que él ejecuta las tareas"],
        "Pregunta: «¿cuántas muestras hay en 8 km con una cada 4 km?». Si no responde, pídele que dibuje el camino con las muestras."),
    reinforce="Inventa tres partidas con cantidad y precio unitario y calcula el subtotal de cada una y el total.",
    extend="Explica por qué dos partidas con el mismo precio unitario pueden tener subtotales muy distintos.",
)

# ============================================================ OAM-07, clase 5
F = ("Ficha 5 (comparación de dos alternativas de conservación, de ejemplo, inventada). Tramo ficticio «Ruta Los Algarrobos». "
     "Alternativa A: tratamiento de la carpeta de rodado con costo de $24.000.000 y duración esperada de 6 años. "
     "Alternativa B: tratamiento más simple con costo de $15.000.000 y duración esperada de 3 años. "
     "Los costos y las duraciones son de ejemplo. Lista de chequeo del informe: fecha, estación, quién inspeccionó, evidencia descrita y firma del inspector. El informe de la alternativa B trae fecha, estación, quién inspeccionó y evidencia, pero no tiene firma.")
build(
    O7, 5, F,
    use="Aprenderé a comparar dos alternativas de conservación por costo por año y a verificar si un informe está completo antes de dar el trabajo por recibido.",
    prior=["Sé calcular subtotales de una planilla.", "Sé dividir números enteros.", "Sé qué datos tiene un buen registro."],
    explain=[
        "Para comparar dos alternativas no basta mirar el costo total. Una alternativa barata puede durar menos y terminar costando más a lo largo del tiempo. Una forma sencilla de compararlas es calcular el costo por año: el costo total dividido en los años de duración esperada. La alternativa con menor costo por año resulta más económica, siempre que ambas cumplan lo que pide el proyecto. Los costos y duraciones de este cuaderno son de ejemplo.",
        "La calidad se verifica con una lista de chequeo que revisa si el informe está completo: fecha, estación, quién inspeccionó, evidencia y firma. Un informe sin firma o sin ubicación no respalda el trabajo. La decisión final sobre qué alternativa se ejecuta corresponde al ingeniero responsable, no a quien compara en la planilla. Y la ejecución exige personal autorizado, norma vigente y medidas de seguridad.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones posibles para resolver un problema"), ("duración esperada", "años que se calcula que durará un tratamiento"), ("costo por año", "costo total dividido en los años de duración esperada"), ("lista de chequeo", "tabla que revisa si un informe tiene todos sus datos"), ("evidencia", "datos o descripciones que respaldan lo informado"), ("ingeniero responsable", "profesional que decide qué se ejecuta")],
    worked=[
        ("Costo por año", "Una alternativa de ejemplo cuesta $12.000.000 y dura 4 años. ¿Cuánto cuesta por año?", ["Se divide el costo total en los años de duración.", "12.000.000 dividido en 4 son 3.000.000."], "$3.000.000 por año"),
        ("Revisar un informe", "Un informe de ejemplo trae fecha, estación y firma, pero no dice quién inspeccionó. ¿Está completo?", ["Falta uno de los datos que pide la lista de chequeo.", "Entonces no está completo."], "No, falta quién inspeccionó"),
    ],
    mistakes=[("Elegir siempre la alternativa de menor costo total.", "Puede durar menos y costar más por año.", "Compara el costo por año además del total."),
              ("Dar por recibido un informe sin firma «porque la información está».", "Sin firma no hay responsable que lo respalde.", "Pide la firma antes de aceptarlo.")],
    T=[
        ("abc", "En conservación vial: ¿qué es el costo por año de una alternativa?", "El costo total dividido en los años de duración esperada", "El costo del primer año solamente", "La suma de todos los años de lluvias", "El costo por año reparte el costo total entre los años que dura."),
        ("abc", "Una alternativa de $10.000.000 que dura 5 años cuesta por año:", "$2.000.000", "$50.000.000", "$5.000.000", "10.000.000 dividido en 5 son 2.000.000."),
        ("abc", "¿Quién decide qué alternativa de conservación se ejecuta?", "El ingeniero responsable", "Quien compara en la planilla", "El conductor de un camión", "La decisión final corresponde al ingeniero responsable."),
        ("=", "{F} ¿Cuánto cuesta por año la alternativa A?", "24000000//6", "Se divide el costo total en los años de duración esperada.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta por año la alternativa B?", "15000000//3", "Se divide el costo total en los años de duración esperada.", " pesos"),
        ("abc", "{F} ¿Qué alternativa resulta más económica por año?", "La A", "La B", "Cuestan lo mismo por año", "A cuesta $4.000.000 por año y B cuesta $5.000.000 por año."),
        ("=", "{F} ¿Cuánto más cuesta por año B que A?", "15000000//3-24000000//6", "Se restan los costos por año de B y A.", " pesos"),
        ("abc", "{F} ¿Qué dato falta en el informe de la alternativa B?", "La firma del inspector", "La fecha", "La estación", "El informe trae fecha, estación, quién inspeccionó y evidencia; no trae firma."),
        ("abc", "{F} ¿Qué se hace con el informe de B sin firma?", "Pedir la firma antes de dar por recibido el informe", "Recibirlo y firmarlo quien lo compara", "Descartar la alternativa B sin avisar", "Sin firma no hay respaldo; se pide al responsable, sin firmar por otra persona."),
        ("ab", "{F} Un compañero dice: «B es mejor porque cuesta menos en total». ¿Qué respuesta es correcta?", "No siempre: por año B cuesta más que A, así que A es más económica", "Sí: el menor costo total siempre es mejor", "El costo por año de B es mayor, aunque su costo total sea menor."),
        ("abc", "{F} Si la alternativa A durara 8 años en vez de 6, con el mismo costo, ¿qué pasa con su costo por año?", "Disminuye", "Aumenta", "Queda igual", "Si el costo total se reparte en más años, el costo por año baja."),
        ("=", "{F} Si A durara 8 años, ¿cuánto costaría por año?", "24000000//8", "Se divide el costo total en los nuevos años de duración.", " pesos"),
        ("abc", "{F} Un jefe pide ejecutar la alternativa A «porque es más barata por año» sin consultar al ingeniero. ¿Qué respuesta es correcta?", "La planilla ayuda a comparar; la decisión y la ejecución las define el ingeniero con personal autorizado", "Se puede ejecutar, porque la planilla decide", "Se puede ejecutar si es temporada seca", "El costo por año es un criterio, no una autorización."),
    ],
    ctx=("abc", "Un contratista ofrece «ahorrar» sin firmar los informes para terminar antes. ¿Qué responde quien recibe el trabajo?", "Que no se puede recibir sin informe completo y firmado", "Que está bien si el trabajo parece correcto", "Que firme él mismo por el contratista", "Un informe completo y firmado es el respaldo del trabajo; no se omite ni se firma por otro."),
    sc=[("En obras viales: ¿cómo se calcula el costo por año?", "Costo total dividido en los años de duración", "Se reparte el costo total en la duración esperada."),
        ("¿Qué datos pide la lista de chequeo del informe de la ficha?", "Fecha, estación, quién inspeccionó, evidencia y firma", "Son los datos que respaldan el trabajo."),
        ("¿Quién ejecuta la alternativa elegida?", "Personal autorizado con norma vigente", "Este cuaderno no habilita para trabajar en caminos.")],
    op=("Comparación de ejemplo «Camino Las Acacias»: alternativa X cuesta $18.000.000 y dura 6 años; alternativa Y cuesta $10.000.000 y dura 2 años. El informe de Y no tiene fecha. Escribe (a) el costo por año de X, (b) el costo por año de Y, (c) qué alternativa es más económica por año, (d) qué falta en el informe y quién decide qué se ejecuta.",
        "(a) 18.000.000 dividido en 6 son $3.000.000. (b) 10.000.000 dividido en 2 son $5.000.000. (c) La alternativa X. (d) Falta la fecha; decide el ingeniero responsable.",
        ["calcula $3.000.000", "calcula $5.000.000", "elige X", "nombra el dato que falta y al ingeniero responsable"],
        ["hoja con las cuatro respuestas"],
        ["elegir por el costo total", "olvidar el dato faltante", "decir que decide la planilla"],
        "Pregunta: «¿qué alternativa es más barata por año?». Si no responde, pídele que divida cada costo en sus años."),
    reinforce="Inventa dos alternativas con costo y duración y calcula cuál es más económica por año.",
    extend="Explica por qué la duración esperada puede cambiar la elección aunque el costo total de una alternativa sea menor.",
)

"""Atención de Enfermería TP 3.º medio (tronco): OAE-04 (condiciones sanitarias y de seguridad de las dependencias), OAE-05 (prevención y control de infecciones, asepsia y antisepsia: solo conceptos) y OAE-06 (registro de información y privacidad en el ingreso, la permanencia y el egreso). Todo en papel: fichas, planillas y personas inventadas y rotuladas «de ejemplo»; sin técnicas clínicas ni procedimientos."""
from __future__ import annotations

from tp_aten_common import LIM, build

O4 = "TP-ATEN-3-OAE-04"
O5 = "TP-ATEN-3-OAE-05"
O6 = "TP-ATEN-3-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (servicio de ejemplo, inventado). Un servicio tiene 5 salas comunes. En cada sala se revisan 8 puntos del entorno en cada ronda: piso seco y despejado, vía de evacuación libre, señalética visible, residuos separados, ventilación, iluminación, ropa limpia separada de la sucia y extintor con etiqueta al día. "
     "Hay una ronda cada 4 horas en el turno de 12 horas. Revisar una sala toma 15 minutos. El personal de aseo limpia pisos y superficies; el técnico revisa el entorno, mantiene el orden y avisa de los riesgos a la enfermera.")
build(
    O4, 1, F,
    use="Aprenderé qué condiciones sanitarias y de seguridad debe tener una sala, quién hace qué y por qué se avisa de un riesgo en vez de resolverlo a solas.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé leer una ficha con horarios.", "Conozco el trabajo del técnico en enfermería."],
    explain=[
        "En Atención de Enfermería, las dependencias son los lugares donde están las personas bajo cuidado: salas, pasillos, baños y bodegas. Las condiciones sanitarias son la limpieza, el orden, la ventilación y el manejo correcto de residuos y ropa, que reducen el riesgo de infecciones. Las condiciones de seguridad son los pisos secos, las vías de evacuación libres, la señalética visible y los equipos de emergencia al día, que reducen el riesgo de caídas, incendios y accidentes.",
        "Estas condiciones se revisan con rondas periódicas y una pauta de revisión. El técnico revisa, mantiene el orden y avisa de lo que no puede o no le corresponde resolver, por ejemplo un cable suelto, un derrame o una luz quemada. Cada servicio tiene un protocolo sobre quién limpia qué y cómo se avisa. Un riesgo avisado a tiempo y registrado con hora, lugar y a quién se avisó se puede corregir.",
        "Si hay humo, fuego, un cable que echa chispas o una persona herida, no se actúa por cuenta propia: se avisa de inmediato a la enfermera o profesional responsable y a emergencias, y se sigue el plan de emergencia." + LIM,
    ],
    vocab=[("dependencias", "lugares donde están las personas bajo cuidado: salas, pasillos, baños"), ("condiciones sanitarias", "limpieza, orden, ventilación y manejo correcto de residuos y ropa"), ("condiciones de seguridad", "pisos secos, vías libres, señalética y equipos de emergencia al día"), ("ronda", "revisión periódica del entorno con una pauta"), ("señalética", "carteles y símbolos que indican salidas, riesgos y equipos de emergencia"), ("vía de evacuación", "recorrido que debe estar libre para salir con seguridad")],
    worked=[
        ("Quién resuelve un riesgo", "En una ronda de ejemplo, un técnico ve que una ampolleta del pasillo está quemada. ¿Qué corresponde?", ["La luz del pasillo es una instalación del edificio.", "El técnico la anota y avisa a la enfermera o a mantención; no la cambia por su cuenta."], "Anotarla y avisar a la enfermera o a mantención"),
        ("Rondas de un turno", "En otro servicio de ejemplo hay una ronda cada 3 horas en un turno de 12 horas y 4 salas por revisar. ¿Cuántas revisiones de sala se hacen en el turno?", ["12 ÷ 3 = 4 rondas.", "4 rondas × 4 salas = 16."], "16 revisiones de sala"),
    ],
    mistakes=[("Dejar un carro de insumos frente a la salida de emergencia «solo un momento».", "En una emergencia, un solo obstáculo puede impedir una salida segura.", "Devuelve el carro a su lugar y mantén la vía libre siempre."),
              ("Decidir limpiar por cuenta propia un derrame de un líquido desconocido.", "Puede exponerse a un riesgo y el protocolo dice quién y cómo lo limpia.", "Avisa al personal de aseo o a la enfermera y señala el lugar a quienes pasan.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué son las condiciones sanitarias de una sala?", "Limpieza, orden, ventilación y manejo correcto de residuos y ropa", "La cantidad de camas y su numeración", "El horario de visitas de la sala", "Las condiciones sanitarias reducen el riesgo de infecciones; las camas y las visitas son otros asuntos."),
        ("abc", "{F} ¿Quién limpia pisos y superficies según la ficha?", "El personal de aseo", "El técnico, durante cada ronda", "La visita de cada paciente", "La ficha dice que el personal de aseo limpia pisos y superficies; el técnico revisa y avisa."),
        ("abc", "{F} En una ronda, el técnico ve una camilla frente a una vía de evacuación. ¿Qué corresponde?", "Dejar la vía libre, devolver la camilla a su lugar y avisar si no puede moverla", "Dejarla, porque se retirará al final del turno", "Taparla con una sábana para que no se vea", "Una vía de evacuación debe estar siempre libre porque en una emergencia no se puede improvisar."),
        ("=", "{F} ¿Cuántas rondas se hacen en un turno?", "12//4", "Se divide la duración del turno entre el intervalo entre rondas.", " rondas"),
        ("=", "{F} ¿Cuántos puntos del entorno se revisan en una ronda en todas las salas?", "5*8", "Se multiplica la cantidad de salas por los puntos que se revisan en cada una.", " puntos"),
        ("=", "{F} ¿Cuántos minutos se dedican a revisar las 5 salas en una ronda?", "5*15", "Se multiplica el tiempo de cada sala por la cantidad de salas.", " minutos"),
        ("=", "{F} ¿Cuántas revisiones de puntos del entorno se hacen en todo el turno entre las 5 salas?", "12//4*5*8", "Se multiplican las rondas del turno por las salas y por los puntos de cada sala.", " revisiones"),
        ("abc", "{F} Un técnico ve que el extintor de una sala tiene la etiqueta de revisión vencida. ¿Qué corresponde?", "Avisar a la enfermera y registrar el hallazgo con la hora", "Cambiar él mismo el extintor por otro de otra sala", "Retirar el extintor para que no confunda a nadie", "Un equipo de emergencia con revisión vencida se informa para que lo repongan; el técnico no lo reemplaza por su cuenta."),
        ("abc", "{F} Durante la ronda, el técnico siente olor a quemado en el pasillo y ve humo saliendo de una puerta. ¿Qué hace?", "Avisa de inmediato a la enfermera y a emergencias y sigue el plan de emergencia del servicio", "Abre la puerta para ver qué ocurre y trata de apagar", "Termina la ronda y avisa al final", "Ante humo no se actúa por cuenta propia: se avisa de inmediato y se sigue el plan de emergencia."),
        ("abc", "{F} Un compañero dice: «Como no hubo accidentes este mes, podemos hacer las rondas una sola vez por turno». ¿Qué corresponde responder?", "Que las rondas se hacen según la pauta del servicio, porque previenen los accidentes", "Que sí, mientras todo esté ordenado", "Que sí, si lo anota en la planilla", "Las rondas son preventivas: se hacen aunque no haya habido accidentes."),
        ("abc", "{F} Al registrar un riesgo, un técnico escribe «hay peligro en la sala 3». ¿Qué le falta al registro?", "La hora, el lugar exacto, qué se vio y a quién se avisó", "Una opinión sobre quién tuvo la culpa", "Una lista de lo que debería hacer la enfermera", "Un registro útil dice dónde, cuándo y qué se vio, y a quién se avisó."),
        ("=", "{F} Si en una ronda 3 de las 5 salas tienen todos sus puntos en regla, ¿qué porcentaje de las salas cumple?", "3*100//5", "Se divide el número de salas que cumplen entre el total de salas y se multiplica por 100.", " %"),
        ("abc", "En Atención de Enfermería: ¿qué hace el técnico cuando ve un riesgo que no le corresponde resolver?", "Lo anota y avisa a quien corresponde", "Lo ignora y espera a que otro lo vea", "Lo resuelve de la forma que le parezca más rápida", "Un riesgo avisado a tiempo y registrado se puede corregir por quien corresponde."),
    ],
    ctx=("abc", "{F} Una visita derrama un líquido de color oscuro en el pasillo y se va sin avisar. Un adulto mayor camina hacia esa zona con su bastón. ¿Qué hace el técnico?", "Se interpone con calma para avisar al adulto mayor y llama de inmediato al personal de aseo y a la enfermera", "Seca el líquido con una sábana de un paciente", "Sigue su ronda y avisa al terminar", "Se protege a la persona de inmediato y se avisa a quienes limpian y supervisan; no se improvisa con material de los pacientes."),
    sc=[
        ("En Atención de Enfermería: ¿qué haces si ves un riesgo que no te corresponde resolver?", "Lo anoto y aviso a la enfermera", "El aviso a tiempo permite que lo corrija quien corresponde."),
        ("¿Qué debe estar siempre libre en una sala?", "La vía de evacuación", "En una emergencia no se puede improvisar la salida."),
        ("¿Qué haces ante humo o fuego?", "Aviso de inmediato a la enfermera y a emergencias, y sigo el plan", "No actúo por cuenta propia y pido ayuda a quien corresponde."),
    ],
    op=("Pauta de ejemplo: una sala de 6 camas con estos hallazgos en la ronda de las 10:00: el piso del baño está mojado; hay un carro frente a la salida de emergencia; un tomacorriente tiene la tapa rota; todo lo demás está en orden. "
        "Escribe: qué riesgo representa cada hallazgo; qué haría el técnico en cada caso; a quién avisaría; y una frase de registro con hora, lugar y hecho, sin opinión.",
        "Piso mojado: riesgo de caída; avisar al personal de aseo y señalar el lugar. Carro frente a la salida: obstruye la evacuación; devolverlo a su lugar o pedir ayuda. Tomacorriente roto: riesgo eléctrico; no tocarlo y avisar a la enfermera y a mantención. Registro: «10:00, sala 3, tomacorriente con tapa rota junto a la cama 4; se avisó a la enfermera».",
        ["identifica un riesgo por hallazgo", "avisa a quien corresponde", "no manipula la instalación eléctrica", "el registro lleva hora, lugar y hecho"],
        ["hoja con tres hallazgos, acciones, a quién avisa y una frase de registro"],
        ["tocar o arreglar el tomacorriente", "no avisar a la enfermera", "escribir una opinión en vez de un hecho"],
        "Pregunta: «¿tu frase dice dónde, cuándo y qué se vio?». Si no, pídele completarla."),
    reinforce="Escribe tres condiciones sanitarias y tres condiciones de seguridad que debe tener una sala.",
    extend="Explica con un ejemplo inventado por qué una ronda se hace aunque la sala parezca ordenada.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (residuos y señalética de un servicio de ejemplo). Tipos de residuos del servicio: común (por ejemplo, restos de una colación y papeles), de riesgo biológico (por ejemplo, un guante manchado con sangre) y cortopunzante (por ejemplo, una aguja usada), que se deposita en un contenedor rígido especial. "
     "Señalética por color: rojo, prohibición o incendio; azul, obligación; amarillo, advertencia de riesgo; verde, salida o emergencia. Residuos de un turno de ejemplo, en bolsas: comunes 12, de riesgo biológico 3; contenedores de cortopunzantes usados: 2.")
build(
    O4, 2, F,
    use="Aprenderé a clasificar residuos, a leer la señalética por color y a usar una pauta de revisión del entorno.",
    prior=["Conozco las condiciones sanitarias y de seguridad.", "Sé sumar y comparar números.", "Sé leer una ficha."],
    explain=[
        "Los residuos de un servicio de salud se clasifican según el riesgo. Los residuos comunes son los que no tienen contacto con sangre ni fluidos, como papeles o restos de una colación. Los residuos de riesgo biológico son los que estuvieron en contacto con sangre u otros fluidos del cuerpo. Los cortopunzantes son objetos que pueden cortar o pinchar, y se depositan en contenedores rígidos especiales. Cada tipo tiene su bolsa o contenedor, su color o etiqueta y su retiro, según la norma vigente.",
        "Mezclar los residuos es un error grave: un residuo de riesgo en la bolsa común convierte el contenido en riesgoso y puede exponer a quien lo retira. La señalética también usa colores: el rojo indica prohibición o incendio, el azul obligación, el amarillo advertencia y el verde salida o emergencia. Una pauta de revisión del entorno es una lista de puntos que se marcan como cumplidos o no.",
        "En esta clase se clasifica y se lee; no se enseña cómo manejar los residuos con técnica." + LIM,
    ],
    vocab=[("residuo común", "residuo sin contacto con sangre ni fluidos del cuerpo"), ("residuo de riesgo biológico", "residuo que estuvo en contacto con sangre u otros fluidos"), ("cortopunzante", "objeto que puede cortar o pinchar"), ("contenedor rígido", "recipiente resistente a pinchazos para los cortopunzantes"), ("pauta de revisión", "lista de puntos que se marcan como cumplidos o no"), ("señalética", "carteles y colores que indican riesgos, salidas y equipos")],
    worked=[
        ("Clasificar un residuo", "En una sala de ejemplo hay una servilleta de papel limpia. ¿A qué tipo de residuo pertenece?", ["No tuvo contacto con sangre ni fluidos.", "Es un residuo común."], "Residuo común"),
        ("Contar residuos", "En un turno de ejemplo hubo 9 bolsas de residuos comunes y 2 de riesgo biológico. ¿Cuántas bolsas hubo en total?", ["Se suman los dos tipos.", "9 + 2 = 11."], "11 bolsas"),
    ],
    mistakes=[("Poner un guante manchado con sangre en la bolsa común «porque no cabe en la otra».", "Convierte la bolsa común en un riesgo para quien la retira.", "Usa el recipiente de riesgo biológico o avisa a la enfermera si está lleno."),
              ("Pensar que cualquier cartel rojo es «incendio».", "El rojo también indica prohibición; hay que leer el símbolo y el texto.", "Lee el símbolo, el texto y el color juntos.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un residuo de riesgo biológico?", "Un residuo que estuvo en contacto con sangre u otros fluidos del cuerpo", "Un residuo de papel o de una colación", "Cualquier residuo que huela mal", "El riesgo biológico se define por el contacto con sangre o fluidos, no por el olor."),
        ("abc", "{F} ¿Dónde se deposita una aguja usada?", "En el contenedor rígido especial de cortopunzantes", "En la bolsa de residuos comunes", "En la bolsa de riesgo biológico, junto con los guantes", "Los cortopunzantes van en contenedor rígido para evitar cortes y pinchazos."),
        ("abc", "{F} ¿Qué color de señalética indica obligación?", "Azul", "Rojo", "Amarillo", "En la ficha, el azul indica obligación; el rojo, prohibición o incendio, y el amarillo, advertencia."),
        ("abc", "{F} ¿Qué indica un cartel verde con una flecha?", "Una salida o una emergencia", "Una prohibición", "Una advertencia de riesgo", "En la ficha, el verde señala salida o emergencia."),
        ("=", "{F} ¿Cuántas bolsas de residuos hubo en el turno entre comunes y de riesgo biológico?", "12+3", "Se suman las bolsas comunes y las de riesgo biológico.", " bolsas"),
        ("abc", "¿Cuál de estos residuos es común?", "Un envoltorio de papel de una colación", "Una gasa con sangre", "Un guante manchado con sangre", "El envoltorio no tuvo contacto con fluidos; la gasa y el guante manchado sí."),
        ("abc", "¿Cuál de estos residuos es de riesgo biológico?", "Un guante manchado con sangre", "Un vaso plástico limpio", "Una hoja de la planilla", "El guante manchado tuvo contacto con sangre; el vaso limpio y la hoja son comunes."),
        ("=", "{F} ¿Cuántas bolsas más de residuos comunes que de riesgo biológico hubo en el turno?", "12-3", "Se resta la cantidad de bolsas de riesgo de las bolsas comunes.", " bolsas"),
        ("abc", "{F} Un compañero tiró una bolsa de riesgo biológico en el contenedor de residuos comunes. ¿Qué corresponde?", "Informar a la enfermera y a quien retira los residuos para que se manejen como corresponde", "Callar, porque ya no se puede cambiar", "Sacar la bolsa con las manos para separarla", "Un error de separación se informa para que el contenido se maneje con el riesgo adecuado."),
        ("abc", "{F} Un cartel rojo con un cigarrillo tachado, ¿qué indica?", "Una prohibición", "Una obligación", "Una salida de emergencia", "El rojo indica prohibición; el cigarrillo tachado lo confirma."),
        ("abc", "{F} Un compañero quiere reutilizar el contenedor de cortopunzantes para guardar lápices. ¿Qué corresponde?", "No hacerlo: está destinado a cortopunzantes y su manejo lo define el protocolo", "Hacerlo, si lo lava primero", "Hacerlo, si lo cambia de lugar", "Un contenedor de cortopunzantes es de uso exclusivo y no se reutiliza para otros fines."),
        ("=", "{F} Si un turno genera esa cantidad de bolsas comunes y de riesgo biológico, ¿cuántas bolsas generarían 2 turnos iguales?", "(12+3)*2", "Se calcula el total de un turno y se multiplica por 2.", " bolsas"),
        ("abc", "En Atención de Enfermería: ¿para qué sirve una pauta de revisión del entorno?", "Para marcar punto por punto si el entorno cumple, y dejar registro de lo que falla", "Para decidir quién tiene la culpa de un accidente", "Para reemplazar las indicaciones de la enfermera", "La pauta ordena la revisión y deja trazabilidad de lo que se encontró."),
    ],
    ctx=("abc", "{F} Una técnica ve que el contenedor de cortopunzantes de la sala está lleno hasta el borde y que una compañera quiere presionar la tapa con la mano para que entre una aguja más. ¿Qué hace?", "Le pide que no lo haga, avisa a la enfermera y al personal responsable del retiro, y no manipula el contenedor", "La ayuda a presionar con un lápiz", "Deja la aguja encima de la bandeja", "Un contenedor lleno se reemplaza según el protocolo; manipularlo aumenta el riesgo de pinchazo."),
    sc=[
        ("En Atención de Enfermería: ¿dónde va un cortopunzante usado?", "En un contenedor rígido especial", "El contenedor rígido evita cortes y pinchazos a las personas."),
        ("En Atención de Enfermería: ¿qué indica el color azul en la señalética de una sala?", "Obligación", "Rojo es prohibición o incendio; azul es obligación."),
        ("¿Qué haces si ves un residuo de riesgo en la bolsa común?", "Informo a la enfermera", "El contenido debe manejarse según su riesgo."),
    ],
    op=("Lista de ejemplo de residuos de una sala en un turno: «papel de colación, guante con sangre, vaso plástico limpio, gasa con sangre, aguja usada, envase de jugo vacío, caja de cartón vacía». "
        "Clasifica cada uno como común, de riesgo biológico o cortopunzante; cuenta cuántos hay de cada tipo; escribe a dónde va cada tipo; y a quién avisarías si un residuo de riesgo estuviera en la bolsa común.",
        "Comunes: papel de colación, vaso plástico, envase de jugo, caja de cartón (4). Riesgo biológico: guante con sangre, gasa con sangre (2). Cortopunzante: aguja usada (1). Cada tipo va a su recipiente: bolsa común, bolsa de riesgo o contenedor rígido. Ante un error de separación, se avisa a la enfermera.",
        ["clasifica los siete residuos", "cuenta 4, 2 y 1", "indica el recipiente de cada tipo", "avisa a la enfermera"],
        ["hoja con la clasificación, tres cantidades y a quién avisa"],
        ["poner la aguja en la bolsa común", "olvidar contar un residuo", "no avisar ante un error"],
        "Pregunta: «¿la gasa con sangre va con los residuos comunes?». Debe responder que no, es de riesgo biológico."),
    reinforce="Escribe un ejemplo de cada tipo de residuo y el color de señalética que indica una salida.",
    extend="Explica con un ejemplo inventado qué riesgo tendría una persona que retira una bolsa mezclada.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (pauta de revisión del entorno, de ejemplo). Seis puntos: (1) piso seco y despejado; (2) vía de evacuación libre; (3) señalética visible; (4) residuos separados por tipo; (5) ventilación adecuada; (6) iluminación en buen estado. "
     "Hallazgos de la ronda: Sala A cumple los puntos 1, 2, 3, 5 y 6 (falla el 4: una bolsa de riesgo biológico estaba en el contenedor de residuos comunes). Sala B cumple los puntos 1, 3, 4, 5 y 6 (falla el 2: una camilla frente a la salida). "
     "Sala C cumple los seis puntos. Sala D cumple solo los puntos 2 y 3 (fallan el 1, un piso mojado; el 4, una caja mal ubicada con residuos; el 5, una ventana trabada; y el 6, una luz quemada).")
build(
    O4, 3, F,
    use="Aprenderé a analizar los hallazgos de una ronda con una pauta, a calcular el cumplimiento y a decidir qué se avisa primero y a quién.",
    prior=["Conozco las condiciones sanitarias y de seguridad.", "Sé calcular porcentajes de números enteros.", "Sé qué es un riesgo."],
    explain=[
        "Analizar los hallazgos de una ronda es comparar lo observado con cada punto de la pauta, marcar si cumple y describir lo que falla con hechos. Con los resultados se calcula el cumplimiento: los puntos cumplidos sobre los puntos revisados, en porcentaje. Pero el porcentaje no basta: también se decide qué se avisa primero, según qué tan grave y cercano es el riesgo.",
        "Un riesgo que puede causar una lesión inmediata, como un piso mojado frente a personas que caminan, o una vía de evacuación bloqueada, se avisa primero. Un riesgo que no amenaza de inmediato, como una luz quemada en un pasillo con otra iluminación, se registra y se avisa en el mismo turno. El técnico propone un orden, pero la enfermera decide las prioridades del servicio.",
        "No se buscan culpables: se describen hechos y se corrige el entorno." + LIM,
    ],
    vocab=[("cumplimiento", "puntos que cumplen respecto de los puntos revisados, en porcentaje"), ("hallazgo", "hecho observado en la ronda"), ("prioridad", "orden en que se atiende o se avisa algo según su urgencia"), ("riesgo inmediato", "riesgo que puede causar una lesión en cualquier momento"), ("corrección", "acción que repara una falla del entorno")],
    worked=[
        ("Contar lo que falla", "En una sala de ejemplo se revisan 6 puntos y cumplen 5. ¿Cuántos puntos fallan y qué se hace con ellos?", ["Cumplen 5 de 6, así que falla 1 punto.", "El punto que no cumple se describe con hechos y se avisa."], "1 punto, descrito con hechos y avisado a la enfermera"),
        ("Priorizar", "En una sala de ejemplo hay una bombilla quemada y un cable pelado en el suelo junto a una cama. ¿Qué se avisa primero?", ["El cable pelado puede causar una lesión inmediata.", "La bombilla quemada se avisa después."], "El cable pelado en el suelo"),
    ],
    mistakes=[("Avisar los hallazgos en el orden en que se encontraron.", "Un riesgo grave puede quedar al final y causar un accidente mientras se avisa lo menos urgente.", "Ordena los avisos del riesgo más inmediato al menos inmediato."),
              ("Escribir «la sala D está mal cuidada por el equipo de la mañana».", "Es una opinión que culpa; no describe hechos y no ayuda a corregir.", "Describe: «sala D, piso mojado en el baño a las 10:00»; no culpes.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un hallazgo en una ronda?", "Un hecho observado en la ronda", "Una opinión sobre el equipo", "Una instrucción de la enfermera", "Un hallazgo es lo que se observa: un hecho, no una opinión."),
        ("abc", "{F} ¿Qué punto no cumple la sala A?", "El punto 4: residuos separados por tipo", "El punto 2: vía de evacuación libre", "El punto 6: iluminación", "La ficha dice que en la sala A falla el punto 4 por una bolsa de riesgo en el contenedor común."),
        ("abc", "{F} ¿Qué punto no cumple la sala B?", "El punto 2: vía de evacuación libre", "El punto 1: piso seco y despejado", "El punto 5: ventilación adecuada", "En la sala B, una camilla frente a la salida bloquea la vía de evacuación."),
        ("=", "{F} ¿Cuántos puntos cumplen en total las salas A, B, C y D?", "5+5+6+2", "Se suman los puntos cumplidos de cada sala.", " puntos"),
        ("=", "{F} Si cada sala tiene 6 puntos, ¿qué porcentaje de los puntos cumplen en total las cuatro salas?", "(5+5+6+2)*100//(4*6)", "Se suman los puntos cumplidos, se multiplica por 100 y se divide por el total de puntos revisados.", " %"),
        ("=", "{F} ¿Cuántos puntos fallan en total entre las cuatro salas?", "(6-5)+(6-5)+(6-6)+(6-2)", "Se resta de los 6 puntos de cada sala la cantidad que cumple y se suman las fallas.", " puntos"),
        ("abc", "{F} Si el técnico debe avisar primero el hallazgo más urgente, ¿cuál elige entre los de las salas A y B?", "La camilla frente a la salida de la sala B", "La bolsa de riesgo en el contenedor común de la sala A", "Cualquiera, porque son igual de urgentes", "Una vía de evacuación bloqueada impide salir en una emergencia; el error de separación se corrige después."),
        ("abc", "{F} ¿Cuál es el hallazgo más urgente de la sala D?", "El piso mojado", "La luz quemada", "La ventana trabada", "Un piso mojado puede causar una caída de inmediato; la luz y la ventana no son riesgos inmediatos."),
        ("abc", "{F} Un técnico quiere decir a la enfermera: «la sala D está mal cuidada por el equipo de la mañana». ¿Qué corresponde?", "Describir los hallazgos con hechos, hora y lugar, sin culpar", "Decirlo así, porque resume el problema", "No decir nada, para no generar conflictos", "Los hallazgos se informan con hechos para corregir, no para culpar."),
        ("abc", "{F} La enfermera pide corregir primero la sala C. ¿Qué hace el técnico?", "Le informa que la sala C cumple los seis puntos y le consulta por las demás", "Corrige algo en la sala C para tener qué hacer", "No le dice nada y empieza por la sala A", "La sala C no tiene fallas: la información precisa permite priorizar donde hace falta."),
        ("abc", "{F} Un compañero propone marcar el punto 4 de la sala A como cumplido porque «ya se retiró la bolsa». ¿Qué corresponde?", "Dejar constancia del hallazgo y de su corrección, con hora y firma", "Marcarlo como cumplido, para que la pauta quede perfecta", "Borrar el hallazgo para que no se note", "El hallazgo ocurrió y debe quedar registrado junto con lo que se hizo para corregirlo."),
        ("=", "{F} Si se corrigen todos los hallazgos de la sala D menos la luz quemada, ¿cuántos puntos cumpliría esa sala?", "2+3", "Se suman a los 2 puntos que ya cumplía los 3 que se corrigen.", " puntos"),
        ("abc", "En Atención de Enfermería: ¿quién decide las prioridades de corrección del servicio?", "La enfermera o el profesional responsable", "El técnico que hizo la ronda", "El primer visitante que ve el problema", "El técnico propone un orden y la enfermera decide las prioridades."),
    ],
    ctx=("abc", "{F} Durante la ronda, el técnico ve que en la sala D el baño tiene el piso mojado y que un paciente con bastón camina hacia él. Al mismo tiempo, la enfermera lo llama desde otra sala por un asunto no urgente. ¿Qué hace?", "Se acerca primero al paciente para evitar la caída, pide ayuda y avisa al personal de aseo; luego atiende a la enfermera", "Atiende a la enfermera porque es su superior", "Termina de anotar la pauta y avisa del piso después", "El riesgo inmediato para una persona se atiende primero; lo urgente se prioriza sobre lo no urgente."),
    sc=[
        ("En Atención de Enfermería: ¿cómo se describe un hallazgo?", "Con hechos: dónde, cuándo y qué se vio", "Los hechos permiten corregir sin culpar."),
        ("¿Qué se avisa primero?", "El riesgo más inmediato", "Un riesgo inmediato puede causar una lesión en cualquier momento."),
        ("¿Qué porcentaje es 5 puntos cumplidos de 10?", "50 %", "5 × 100 ÷ 10 = 50."),
    ],
    op=("Hallazgos de ejemplo de una ronda en una sala de 8 puntos: cumple 6; no cumple el punto «vía de evacuación libre» (hay una silla de ruedas frente a la salida) ni el punto «piso seco» (un charco junto a la puerta del baño). "
        "Escribe: el cumplimiento en porcentaje; el orden en que avisarías los dos hallazgos y por qué; una frase de registro con hechos; y a quién avisarías.",
        "Cumplimiento: 6 × 100 ÷ 8 = 75 %. Orden: primero el charco junto a la puerta del baño, porque puede causar una caída de quien pase en ese momento, y luego la silla de ruedas frente a la salida; ambos se avisan a la enfermera y el charco, además, al personal de aseo. Registro: «10:30, sala 4, charco junto a la puerta del baño y silla de ruedas frente a la salida; se avisó a la enfermera y al personal de aseo».",
        ["calcula 75 %", "ordena los avisos con una razón", "el registro lleva hora, lugar y hechos", "avisa a la enfermera"],
        ["hoja con un porcentaje, un orden razonado y una frase de registro"],
        ["calcular mal el porcentaje", "no justificar el orden", "culpar al equipo"],
        "Pregunta: «¿tu orden dice por qué un riesgo va antes que otro?». Si no, pídele agregar la razón."),
    reinforce="Con 7 de 8 puntos cumplidos, calcula el porcentaje de cumplimiento, y cuál sería si se corrigiera uno más.",
    extend="Explica con un ejemplo inventado la diferencia entre un riesgo inmediato y uno que puede esperar unas horas.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (planilla de residuos de un servicio de ejemplo, durante 4 días). Bolsas de residuos comunes por día: 18, 24, 18 y 24. Bolsas de riesgo biológico por día: 4, 6, 2 y 4. "
     "Cada contenedor de residuos comunes del servicio recibe hasta 6 bolsas y cada contenedor de riesgo biológico recibe hasta 2 bolsas; al final de cada día se retiran los contenedores utilizados y quedan vacíos. "
     "Regla: si por error se mezclan bolsas comunes con una bolsa de riesgo, todo el contenedor se trata como riesgo biológico.")
build(
    O4, 4, F,
    use="Aprenderé a calcular volúmenes de residuos y contenedores necesarios con enteros, a leer una planilla de varios días y a ver el efecto de mezclar residuos.",
    prior=["Conozco los tipos de residuos.", "Sé sumar, dividir y calcular promedios de números enteros.", "Sé leer una tabla."],
    explain=[
        "Con una planilla de residuos se hacen cuentas para organizar el retiro. El total de bolsas de un tipo se calcula sumando los días. El promedio diario se calcula dividiendo el total por el número de días. La cantidad de contenedores necesarios se calcula dividiendo las bolsas del día por la capacidad de cada contenedor: por ejemplo, 18 bolsas con capacidad de 6 por contenedor requieren 3 contenedores.",
        "Estas cuentas ayudan a que haya contenedores suficientes y a que el retiro no se acumule. También muestran el efecto de un error: si se mezcla una bolsa de riesgo con bolsas comunes, todo el contenedor pasa a tratarse como riesgo biológico, con más peligro y más costo de manejo. Por eso separar bien es una medida de seguridad y también de orden.",
        "La planilla es de ejemplo; el cuaderno no enseña cómo se manipulan, rotulan ni transportan los residuos." + LIM,
    ],
    vocab=[("capacidad", "cantidad máxima de bolsas que recibe un contenedor"), ("promedio diario", "total de bolsas dividido por el número de días"), ("retiro", "salida de los contenedores del servicio para su manejo posterior"), ("mezcla", "error de poner residuos de distinto tipo en el mismo recipiente"), ("planilla de residuos", "tabla con las bolsas de cada tipo por día")],
    worked=[
        ("Contenedores necesarios", "Un servicio de ejemplo generó 20 bolsas comunes en un día y cada contenedor recibe 5 bolsas. ¿Cuántos contenedores usó?", ["Se divide el total de bolsas entre la capacidad.", "20 ÷ 5 = 4."], "4 contenedores"),
        ("Efecto de una mezcla", "En un contenedor de ejemplo con capacidad de 6 bolsas se pusieron 5 comunes y 1 de riesgo biológico. ¿Cuántas bolsas se tratan como riesgo?", ["Por la regla, todo el contenedor se trata como riesgo.", "5 + 1 = 6 bolsas."], "6 bolsas")],
    mistakes=[("Contar solo las bolsas de riesgo biológico para saber cuántos contenedores usar.", "Se necesitan contenedores para cada tipo de residuo, por separado.", "Calcula los contenedores de cada tipo con su propia capacidad."),
              ("Decir «da lo mismo mezclar porque total se retira todo».", "La mezcla hace que bolsas comunes se traten como riesgo y expone a quien las maneja.", "Separa por tipo siempre y avisa si hubo un error.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿cómo se calcula el promedio diario de bolsas?", "Se divide el total de bolsas entre el número de días", "Se suman las bolsas de dos días", "Se multiplica el total por el número de días", "El promedio diario es el total dividido entre la cantidad de días."),
        ("=", "{F} ¿Cuántas bolsas de residuos comunes hubo en los 4 días?", "18+24+18+24", "Se suman las bolsas comunes de los cuatro días.", " bolsas"),
        ("=", "{F} ¿Cuántas bolsas de riesgo biológico hubo en los 4 días?", "4+6+2+4", "Se suman las bolsas de riesgo biológico de los cuatro días.", " bolsas"),
        ("=", "{F} ¿Cuál fue el promedio diario de bolsas de riesgo biológico?", "(4+6+2+4)//4", "Se divide el total de bolsas de riesgo entre los 4 días.", " bolsas"),
        ("=", "{F} ¿Cuántos contenedores de residuos comunes se usaron el día 2?", "24//6", "Se dividen las bolsas del día entre la capacidad de cada contenedor.", " contenedores"),
        ("=", "{F} ¿Cuántos contenedores de riesgo biológico se usaron el día 2?", "6//2", "Se dividen las bolsas del día entre la capacidad de cada contenedor.", " contenedores"),
        ("=", "{F} ¿Cuántos contenedores de residuos comunes se usaron en los 4 días?", "18//6+24//6+18//6+24//6", "Se calculan los contenedores de cada día y se suman.", " contenedores"),
        ("abc", "{F} ¿En qué día hubo más bolsas de residuos de riesgo biológico?", "El día 2", "El día 1", "El día 4", "El día 2 tuvo 6 bolsas; los días 1 y 4 tuvieron 4 y el día 3, 2."),
        ("=", "{F} Si en un contenedor con capacidad de 6 bolsas se mezclaron 4 bolsas comunes y 1 de riesgo, ¿cuántas bolsas se tratan como riesgo biológico según la regla?", "4+1", "Todo el contenedor se trata como riesgo, así que se suman las bolsas mezcladas.", " bolsas"),
        ("abc", "{F} Al ver la planilla, un compañero dice: «Sobran contenedores de riesgo, podemos usar los comunes para guardar riesgo». ¿Qué corresponde?", "No mezclar: cada tipo de residuo se maneja en su propio recipiente", "Hacerlo, si los comunes son más grandes", "Hacerlo, pero solo por un día", "Los recipientes están destinados a un tipo de residuo; mezclar expone a quien los maneja."),
        ("abc", "{F} El día 3 se generaron 18 bolsas comunes. Un técnico propone usar 2 contenedores «apretando» las bolsas. ¿Qué corresponde?", "Usar los 3 contenedores que indica el cálculo, sin sobrepasar la capacidad", "Apretar las bolsas para ahorrar contenedores", "Dejar las bolsas fuera del contenedor", "Sobrepasar la capacidad aumenta el riesgo de derrame y no se debe hacer."),
        ("abc", "{F} El técnico nota que otro compañero anotó 24 bolsas comunes el día 4, igual que el día 2, sin haberlas contado. ¿Qué corresponde?", "Contar de nuevo y corregir la planilla si es necesario, dejando constancia", "Dejar el dato, porque es parecido", "Borrar el dato del día 4", "Se anotan datos contados, no supuestos; un dato dudoso se verifica."),
        ("=", "{F} ¿Cuál fue el promedio diario de bolsas de residuos comunes?", "(18+24+18+24)//4", "Se divide el total de bolsas comunes entre los 4 días.", " bolsas"),
    ],
    ctx=("abc", "{F} Al preparar la planilla del día, la técnica descubre que 2 bolsas de riesgo biológico fueron puestas por error en un contenedor de residuos comunes que ya estaba cerrado. ¿Qué hace?", "Informa de inmediato a la enfermera y a quien retira los residuos, y deja el contenedor señalado sin abrirlo", "Abre el contenedor y saca las bolsas con las manos", "Deja el contenedor y no dice nada", "No se manipula un contenedor cerrado con error; se informa para que se trate según el protocolo."),
    sc=[
        ("En Atención de Enfermería: ¿cómo calculas los contenedores necesarios?", "Divido las bolsas entre la capacidad de cada contenedor", "Así se sabe cuántos contenedores hacen falta."),
        ("¿Qué pasa si se mezcla una bolsa de riesgo con bolsas comunes?", "Todo el contenido se trata como riesgo", "La mezcla vuelve riesgoso el contenedor completo."),
        ("¿Qué haces si hay un error de separación?", "Informo a la enfermera", "El error debe corregirse según el protocolo."),
    ],
    op=("Planilla de ejemplo (3 días): «bolsas comunes: 15, 20, 10; bolsas de riesgo biológico: 3, 6, 3. Cada contenedor común recibe 5 bolsas y cada contenedor de riesgo biológico recibe 1 bolsa». "
        "Calcula: el total de cada tipo de bolsas; cuántos contenedores de cada tipo se usan por día y en total; el promedio diario de cada tipo. Escribe qué avisarías a la enfermera si el día 2 se mezclara una bolsa de riesgo con 4 comunes.",
        "Totales: comunes 45, riesgo 12. Contenedores comunes: 3, 4, 2 (9 en total); de riesgo: 3, 6, 3 (12 en total). Promedios: comunes 45 ÷ 3 = 15; riesgo 12 ÷ 3 = 4. Aviso: se mezclaron 4 bolsas comunes con 1 de riesgo, y las 5 bolsas se tratan como riesgo biológico.",
        ["calcula los totales", "calcula los contenedores por día", "calcula los promedios 15 y 4", "avisa a la enfermera de la mezcla"],
        ["hoja con totales, contenedores por día, los promedios y un aviso"],
        ["dividir mal", "olvidar la capacidad de cada contenedor", "no avisar la mezcla"],
        "Pregunta: «¿tu aviso dice cuántas bolsas se mezclaron y de qué tipo?». Si no, pídele agregar ambos datos."),
    reinforce="Con 36 bolsas comunes en un día y capacidad de 6 por contenedor, calcula los contenedores necesarios.",
    extend="Explica con un ejemplo inventado por qué separar bien los residuos protege a quien los retira.",
)


# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (servicio de ejemplo, inventado). Un servicio de 20 camas lleva un registro semanal de higiene de manos: se observaron 50 oportunidades en que el personal debía higienizarse las manos y se cumplieron 40. "
     "Meta del servicio (de ejemplo): al menos 90 % de cumplimiento. El servicio tiene una enfermera que coordina la prevención de infecciones y un protocolo para personal con síntomas. "
     "Regla: el personal que tenga fiebre, diarrea o lesiones en la piel que no puede cubrir avisa a su jefatura antes de atender.")
build(
    O5, 1, F,
    use="Aprenderé qué es una infección asociada a la atención de salud, por qué la prevención es una responsabilidad de todo el equipo y qué reglas generales protegen a pacientes y personal.",
    prior=["Sé qué hace un técnico en enfermería.", "Sé calcular porcentajes de números enteros.", "Conozco las condiciones sanitarias de una sala."],
    explain=[
        "En Atención de Enfermería, una infección asociada a la atención de salud es la que una persona adquiere mientras recibe cuidados en un establecimiento de salud y que no tenía al ingresar. Se llama así porque puede transmitirse entre pacientes, visitas y personal. Prevenirla es una responsabilidad de todo el equipo y se rige por las normas vigentes de la autoridad sanitaria y por los protocolos de cada establecimiento.",
        "La medida más importante es la higiene de manos. Otras reglas generales son usar los elementos de protección personal según el protocolo, mantener limpio el entorno, separar los residuos y tratar con cuidado los cortopunzantes. El personal que tenga síntomas, como fiebre o diarrea, avisa a su jefatura antes de atender, porque podría transmitir una infección. Cada establecimiento tiene una enfermera que coordina el programa de prevención.",
        "Si un trabajador se pincha o se expone a sangre o fluidos, no actúa por cuenta propia: avisa de inmediato a la enfermera o profesional responsable y a emergencias, y sigue el protocolo del establecimiento." + LIM,
    ],
    vocab=[("infección asociada a la atención de salud", "infección que la persona adquiere durante la atención y no tenía al ingresar"), ("higiene de manos", "medida más importante para evitar la transmisión de infecciones"), ("elementos de protección personal", "elementos como guantes y mascarilla que protegen a quien trabaja y a las personas"), ("protocolo", "conjunto de reglas escritas que se siguen en un establecimiento"), ("meta", "porcentaje que el servicio se propone alcanzar"), ("transmitir", "pasar una infección de una persona o un objeto a otra persona")],
    worked=[
        ("Calcular un cumplimiento", "En otro servicio de ejemplo se observaron 40 oportunidades de higiene de manos y se cumplieron 30. ¿Qué porcentaje se cumplió?", ["30 × 100 = 3.000.", "3.000 ÷ 40 = 75."], "75 %"),
        ("Decidir ante un síntoma", "Una técnica de ejemplo despierta con fiebre antes de su turno. ¿Qué corresponde?", ["El protocolo pide avisar antes de atender.", "Avisa a su jefatura y no atiende pacientes mientras no se lo indiquen."], "Avisar a su jefatura antes de atender"),
    ],
    mistakes=[("Ir a trabajar con fiebre «porque falta personal y no puedo faltar».", "Puede transmitir una infección a personas que ya están enfermas o vulnerables.", "Avisa a tu jefatura antes de atender y sigue lo que indique."),
              ("Pensar que la prevención de infecciones es solo tarea de la enfermera del programa.", "La transmisión ocurre en cada contacto, y todo el equipo participa.", "Cumple las reglas generales en cada contacto y avisa de lo que veas.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es una infección asociada a la atención de salud?", "La que una persona adquiere mientras recibe cuidados y no tenía al ingresar", "La que una persona tiene cuando llega al hospital", "La que solo se transmite por el aire", "Se llama así porque se adquiere durante la atención de salud."),
        ("abc", "{F} ¿Cuál es la meta del servicio para el cumplimiento de la higiene de manos?", "Al menos 90 %", "Al menos 80 %", "Exactamente 100 %", "La ficha indica una meta de al menos 90 %."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tuvo la semana?", "40*100//50", "Se divide lo cumplido entre las oportunidades observadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas oportunidades de higiene de manos no se cumplieron?", "50-40", "Se restan las oportunidades cumplidas de las observadas.", " oportunidades"),
        ("abc", "{F} ¿La semana alcanzó la meta del servicio?", "No: el cumplimiento fue menor al 90 %", "Sí: cumplió más de la mitad", "Sí: cumplió el 100 %", "El cumplimiento fue 80 %, menor que la meta de 90 %."),
        ("=", "{F} Para alcanzar el 90 % con las mismas 50 oportunidades, ¿cuántas se habrían tenido que cumplir en total?", "50*90//100", "Se calcula el 90 % de las oportunidades observadas.", " oportunidades"),
        ("=", "{F} ¿Cuántas oportunidades más se debieron cumplir para llegar a la meta?", "50*90//100-40", "Se resta lo cumplido de lo necesario para llegar a la meta.", " oportunidades"),
        ("abc", "{F} Una técnica tiene una lesión abierta en la piel de una mano que no puede cubrir y su turno comienza en dos horas. ¿Qué corresponde según la regla?", "Avisar a su jefatura antes de atender", "Ir al turno y usar guantes todo el día", "Ir al turno y atender solo a pacientes que no estén graves", "La regla pide avisar antes de atender cuando hay lesiones en la piel que no se pueden cubrir, para evitar transmitir una infección."),
        ("abc", "Un compañero dice: «La higiene de manos solo importa con pacientes infectados». ¿Qué corresponde responder?", "Que importa con todos los pacientes y en todos los contactos", "Que tiene razón, porque los otros no contagian", "Que solo importa en las salas de aislamiento", "Una persona puede transmitir microbios sin saberlo; la higiene de manos se cumple siempre."),
        ("abc", "Un técnico se pincha accidentalmente con un objeto cortopunzante de una bandeja. ¿Qué hace?", "Avisa de inmediato a la enfermera o profesional responsable y a emergencias, sin actuar por cuenta propia", "Se cura solo y no cuenta nada", "Termina su tarea y avisa al final del turno", "Un accidente con cortopunzantes se avisa de inmediato para recibir la atención que corresponde."),
        ("abc", "En Atención de Enfermería: ¿para qué se usan los elementos de protección personal?", "Para proteger a quien trabaja y a las personas cuidadas, según el protocolo", "Para reemplazar la higiene de manos", "Para adornar el uniforme", "Los elementos protegen, pero no reemplazan la higiene de manos."),
        ("=", "{F} Si el servicio observa 80 oportunidades la semana siguiente y cumple 72, ¿cuál es el porcentaje de cumplimiento?", "72*100//80", "Se divide lo cumplido entre lo observado y se multiplica por 100.", " %"),
        ("abc", "{F} Una visita le pregunta al técnico si el paciente de la cama 4 tiene una infección. ¿Qué responde?", "Que la información la entrega el profesional responsable", "Que sí o que no, según lo que haya visto", "Que mire la planilla", "Los datos de salud son confidenciales y los entrega el profesional."),
    ],
    ctx=("abc", "{F} En un turno muy ocupado, un técnico ve que un compañero pasa de un paciente a otro sin higienizarse las manos. ¿Qué hace?", "Se lo recuerda con respeto y, si se repite, lo informa a la enfermera", "No dice nada, para no incomodar", "Lo anota en la planilla con el nombre del compañero", "Recordarlo con respeto protege a los pacientes; si se repite, se informa a quien coordina la prevención."),
    sc=[
        ("En Atención de Enfermería: ¿cuál es la medida más importante para evitar la transmisión?", "La higiene de manos", "Las manos son una vía frecuente de transmisión."),
        ("¿Qué haces si tienes fiebre antes del turno?", "Aviso a mi jefatura antes de atender", "Con fiebre podría transmitir una infección a pacientes vulnerables."),
        ("En Atención de Enfermería: ¿qué haces si te pinchas con un cortopunzante del servicio?", "Aviso de inmediato a la enfermera o profesional responsable y a emergencias", "No actúo por cuenta propia: el aviso inmediato permite recibir la atención que corresponde."),
    ],
    op=("Registro de ejemplo de dos servicios: «Servicio X: 60 oportunidades observadas y 45 cumplidas; Servicio Y: 80 oportunidades observadas y 64 cumplidas. Meta: al menos 80 %». "
        "Calcula el porcentaje de cada servicio y di cuál alcanza la meta. Escribe: tres reglas generales de prevención de infecciones y qué hace una técnica con fiebre antes de su turno.",
        "X: 45×100÷60 = 75 %, no alcanza. Y: 64×100÷80 = 80 %, alcanza. Tres reglas: higiene de manos, usar elementos de protección según protocolo, separar bien los residuos. Con fiebre: avisa a su jefatura antes de atender.",
        ["calcula 75 % y 80 %", "indica qué servicio alcanza la meta", "nombra tres reglas generales", "indica avisar a la jefatura"],
        ["hoja con dos porcentajes, una conclusión y tres reglas"],
        ["calcular mal el porcentaje", "decir que X alcanza la meta", "olvidar avisar a la jefatura"],
        "Pregunta: «¿cuántas oportunidades más debería cumplir el servicio X para llegar a 80 %?». Debe calcular 48 − 45 = 3."),
    reinforce="Escribe tres reglas generales para evitar la transmisión de infecciones y una situación en que avisarías a tu jefatura.",
    extend="Explica con un ejemplo inventado por qué una persona sin síntomas también puede transmitir una infección.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (cadena de transmisión, de ejemplo). Los seis eslabones: agente (el microbio), reservorio (donde vive y se multiplica), puerta de salida (por donde sale del reservorio), vía de transmisión (cómo se desplaza), puerta de entrada (por donde entra a otra persona) y huésped susceptible (la persona que puede enfermar). "
     "Situaciones de ejemplo: 1, la bacteria que causa una infección; 2, una persona portadora del microbio; 3, la tos; 4, las manos contaminadas que pasan el microbio de una persona a otra; 5, una herida abierta; 6, una persona con las defensas bajas. "
     "Definiciones del servicio: asepsia, conjunto de medidas para evitar la presencia de microbios; antisepsia, uso de un producto sobre la piel viva para reducir microbios; desinfección, reducción de microbios en superficies u objetos; esterilización, eliminación de toda forma de vida microbiana de un objeto.")
build(
    O5, 2, F,
    use="Aprenderé los eslabones de la cadena de transmisión, la diferencia entre asepsia, antisepsia, desinfección y esterilización, y los elementos de protección personal.",
    prior=["Sé qué es una infección asociada a la atención.", "Sé ordenar una secuencia.", "Sé leer una ficha."],
    explain=[
        "Una infección se transmite por una cadena de seis eslabones: el agente (microbio), el reservorio donde vive, la puerta de salida, la vía de transmisión, la puerta de entrada y el huésped susceptible. Si se corta cualquier eslabón, la cadena se interrumpe. La higiene de manos corta la vía de transmisión; una vacuna protege al huésped; cubrir una herida cierra una puerta de entrada.",
        "Cuatro palabras se confunden con facilidad. Asepsia es el conjunto de medidas para evitar la presencia de microbios. Antisepsia es usar un producto sobre la piel viva para reducirlos. Desinfección es reducir microbios en superficies y objetos. Esterilización es eliminar toda forma de vida microbiana de un objeto. Las precauciones estándar son reglas que se aplican con todas las personas, y los elementos de protección personal incluyen guantes, mascarilla, delantal y protección ocular.",
        "En esta clase se aprenden los conceptos; el uso correcto de cada elemento lo enseña un instructor autorizado con práctica supervisada." + LIM,
    ],
    vocab=[("cadena de transmisión", "seis eslabones por los que pasa una infección para llegar a una persona"), ("vía de transmisión", "forma en que el microbio pasa de un lugar a otro, como las manos"), ("huésped susceptible", "persona que puede enfermar al recibir un microbio"), ("asepsia", "medidas para evitar la presencia de microbios"), ("antisepsia", "uso de un producto sobre la piel viva para reducir microbios"), ("desinfección", "reducción de microbios en superficies u objetos"), ("esterilización", "eliminación de toda forma de vida microbiana de un objeto"), ("precauciones estándar", "reglas que se aplican con todas las personas, sin importar su diagnóstico")],
    worked=[
        ("Ubicar un eslabón", "En una situación de ejemplo, un microbio sale del cuerpo de una persona con diarrea junto con sus deposiciones. ¿Qué eslabón es esa salida?", ["Es por donde el microbio sale de quien lo porta.", "Es la puerta de salida."], "Puerta de salida"),
        ("Nombrar una medida", "En una sala de ejemplo se limpia una mesa con un producto para reducir los microbios de su superficie. ¿Cómo se llama esa medida?", ["Se actúa sobre una superficie, no sobre la piel viva.", "Reducir microbios en superficies u objetos es desinfección."], "Desinfección"),
    ],
    mistakes=[("Decir que «desinfectar» y «esterilizar» son lo mismo.", "La desinfección reduce microbios; la esterilización los elimina todos.", "Recuerda: desinfectar reduce y esterilizar elimina toda forma de vida microbiana."),
              ("Pensar que los guantes reemplazan la higiene de manos.", "Los guantes pueden contaminarse y no evitan por sí solos la transmisión.", "Cumple la higiene de manos, además de usar guantes según el protocolo.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es el huésped susceptible?", "La persona que puede enfermar al recibir un microbio", "El microbio que causa la infección", "El lugar donde vive el microbio", "El huésped susceptible es la persona; el microbio es el agente."),
        ("abc", "{F} ¿Qué eslabón es la situación 1, la bacteria que causa la infección?", "El agente", "El reservorio", "La puerta de entrada", "La bacteria es el microbio que causa la infección, es decir, el agente."),
        ("abc", "{F} ¿Qué eslabón es la situación 2, una persona portadora del microbio?", "El reservorio", "La vía de transmisión", "El huésped susceptible", "Una persona portadora es donde el microbio vive y se multiplica."),
        ("abc", "{F} ¿Qué eslabón es la situación 4, las manos contaminadas que pasan el microbio?", "La vía de transmisión", "La puerta de salida", "La puerta de entrada", "Las manos llevan el microbio de una persona a otra: son la vía de transmisión."),
        ("abc", "{F} ¿Qué eslabón es la situación 5, una herida abierta?", "La puerta de entrada", "La puerta de salida", "El agente", "Una herida abierta es un lugar por donde un microbio puede entrar."),
        ("abc", "{F} ¿Qué eslabón es la situación 6, una persona con las defensas bajas?", "El huésped susceptible", "El reservorio", "La vía de transmisión", "Una persona con defensas bajas puede enfermar con facilidad."),
        ("abc", "{F} ¿Cuántos eslabones tiene la cadena de transmisión descrita en la ficha?", "Seis", "Cuatro", "Ocho", "La ficha enumera agente, reservorio, puerta de salida, vía de transmisión, puerta de entrada y huésped susceptible: seis."),
        ("abc", "{F} ¿Qué definición corresponde a la antisepsia?", "Usar un producto sobre la piel viva para reducir microbios", "Eliminar toda forma de vida microbiana de un objeto", "Reducir microbios en superficies u objetos", "La antisepsia es sobre la piel viva; las otras definiciones son esterilización y desinfección."),
        ("abc", "{F} ¿Qué definición corresponde a la esterilización?", "Eliminar toda forma de vida microbiana de un objeto", "Reducir microbios en superficies u objetos", "Usar un producto sobre la piel viva", "La esterilización elimina toda forma de vida microbiana, no solo la reduce."),
        ("abc", "{F} ¿Qué eslabón se interrumpe con la higiene de manos?", "La vía de transmisión", "El agente", "El huésped susceptible", "Las manos son una vía de transmisión; la higiene de manos la interrumpe."),
        ("abc", "{F} Un compañero dice: «Con guantes no hace falta lavarse las manos». ¿Qué corresponde responder?", "Que los guantes no reemplazan la higiene de manos", "Que tiene razón, porque los guantes protegen del todo", "Que solo importa lavarse las manos si hay sangre", "Los guantes pueden contaminarse; la higiene de manos es una medida distinta e imprescindible."),
        ("abc", "En Atención de Enfermería: ¿qué son las precauciones estándar?", "Reglas que se aplican con todas las personas, sin importar su diagnóstico", "Reglas que solo se aplican con pacientes infectados", "Reglas que fija cada técnico para su trabajo", "Las precauciones estándar protegen en todos los contactos, porque no siempre se sabe quién porta un microbio."),
        ("abc", "{F} Una técnica quiere «esterilizar» el piso con un paño. ¿Qué corresponde?", "Aclarar que en un piso se desinfecta; esterilizar es para objetos específicos y lo hace el personal responsable", "Aceptarlo, porque es lo mismo", "Esterilizar solo con agua", "En superficies se habla de desinfección; la esterilización es para objetos y la hace el personal formado."),
    ],
    ctx=("abc", "{F} Una técnica nueva dice: «Me pondré guantes siempre, así no necesito lavarme las manos entre pacientes». ¿Qué le corresponde responder a su compañero?", "Que los guantes no reemplazan la higiene de manos y que debe seguir el protocolo del servicio", "Que es una buena idea para ahorrar tiempo", "Que solo sirve si cambia el uniforme", "La higiene de manos es insustituible; los guantes se usan según el protocolo, no en su lugar."),
    sc=[
        ("En Atención de Enfermería: ¿qué eslabón interrumpe la higiene de manos?", "La vía de transmisión", "Las manos son una vía de transmisión frecuente."),
        ("¿Qué diferencia hay entre desinfectar y esterilizar?", "Desinfectar reduce los microbios; esterilizar elimina toda forma de vida microbiana", "La esterilización es más completa que la desinfección."),
        ("¿Qué son las precauciones estándar?", "Reglas que se aplican con todas las personas", "Se aplican siempre y no dependen del diagnóstico de la persona."),
    ],
    op=("Caso de ejemplo: una persona con un resfrío tose cerca de otra, que tiene una herida abierta en una mano y las defensas bajas; luego un trabajador toca a la primera sin higienizarse las manos y después a la segunda. "
        "Escribe: los seis eslabones de esta situación, con una frase para cada uno; qué eslabón cortarías con la higiene de manos; y qué avisarías a la enfermera.",
        "Agente: el microbio del resfrío. Reservorio: la persona con resfrío. Puerta de salida: la tos. Vía de transmisión: las manos del trabajador. Puerta de entrada: la herida abierta. Huésped susceptible: la persona con defensas bajas. Con la higiene de manos se corta la vía de transmisión. Avisaría a la enfermera de la situación.",
        ["ubica los seis eslabones", "identifica la vía de transmisión", "relaciona la higiene de manos con la vía", "avisa a la enfermera"],
        ["hoja con seis frases, un eslabón cortado y un aviso"],
        ["confundir reservorio con agente", "decir que los guantes reemplazan la higiene de manos", "no avisar a la enfermera"],
        "Pregunta: «¿cuál eslabón se cortaría si cubren la herida?». Debe responder la puerta de entrada."),
    reinforce="Escribe los seis eslabones en orden y una medida que corte uno de ellos.",
    extend="Explica con un ejemplo inventado por qué se habla de «precauciones estándar» y no solo de precauciones con pacientes infectados.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (observación de higiene de manos, de ejemplo). Una enfermera observó al personal de un servicio durante una semana. Resumen por momento: (M1) antes de tocar a un paciente, 3 observaciones, 2 cumplidas; (M2) antes de una tarea limpia, 2 observaciones, 2 cumplidas; "
     "(M3) después de un posible contacto con fluidos, 2 observaciones, 2 cumplidas; (M4) después de tocar a un paciente, 2 observaciones, 1 cumplida; (M5) después de tocar el entorno del paciente, 1 observación, 1 cumplida. "
     "Otros hallazgos: un técnico usó los mismos guantes con dos pacientes; otro salió de la sala con los guantes puestos y tocó una manilla de la puerta.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso con datos de observación, a calcular el cumplimiento por momento y a decidir cómo se informa y se mejora sin culpar a nadie.",
    prior=["Conozco la cadena de transmisión.", "Sé calcular porcentajes de números enteros.", "Conozco los elementos de protección personal."],
    explain=[
        "Observar es mirar una conducta y anotar si se cumple o no. La higiene de manos tiene cinco momentos en que se espera hacerla: antes de tocar a un paciente, antes de una tarea limpia, después de un posible contacto con fluidos, después de tocar a un paciente y después de tocar el entorno del paciente. Con una planilla de observación se calcula cuántas veces se cumplió en cada momento.",
        "Analizar el caso es comparar el cumplimiento de cada momento y ver cuál es el más bajo, para proponer una mejora. También se revisan otras conductas, como el uso de guantes: los guantes se usan para un paciente y una tarea y se retiran antes de tocar otra persona o superficies como las manillas. Los guantes usados con dos pacientes o llevados fuera de la sala pueden transmitir microbios.",
        "La observación sirve para mejorar el servicio y no para castigar; los resultados se informan sin nombres." + LIM,
    ],
    vocab=[("observación", "mirar una conducta y anotar si se cumple o no"), ("momento de higiene de manos", "situación en que se espera higienizarse las manos"), ("adherencia", "proporción de veces que una conducta se cumple cuando correspondía"), ("planilla de observación", "documento donde se anota lo observado por momento"), ("mejora", "cambio propuesto para aumentar el cumplimiento")],
    worked=[
        ("Calcular la adherencia de un momento", "En otro servicio de ejemplo, en el momento «antes de tocar a un paciente» hubo 4 observaciones y se cumplieron 3. ¿Qué porcentaje es?", ["3 × 100 = 300.", "300 ÷ 4 = 75."], "75 %"),
        ("Elegir el momento más bajo", "En una planilla de ejemplo: M1 cumple 2 de 4 y M2 cumple 3 de 4. ¿Cuál tiene menor cumplimiento?", ["M1 cumple el 50 % y M2 el 75 %.", "El menor es M1."], "M1")],
    mistakes=[("Anotar el nombre de cada persona que no se higienizó para «llamarle la atención».", "La observación busca mejorar el servicio y no castigar; los nombres inhiben el aprendizaje.", "Informa los resultados por momento y sin nombres."),
              ("Creer que los guantes «ya protegen» y llevarlos a otra sala.", "Pueden contaminar manillas y otros pacientes.", "Cámbialos según el protocolo y haz la higiene de manos.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la adherencia a la higiene de manos?", "La proporción de veces que se cumple cuando correspondía", "El número de dispensadores del servicio", "La cantidad de pacientes de una sala", "La adherencia es qué parte de las oportunidades se cumple."),
        ("abc", "{F} ¿Cuántas observaciones hizo la enfermera en el momento M1?", "3", "2", "1", "La ficha indica 3 observaciones en M1."),
        ("=", "{F} ¿Cuántas observaciones hubo en total en los cinco momentos?", "3+2+2+2+1", "Se suman las observaciones de cada momento.", " observaciones"),
        ("=", "{F} ¿Cuántas observaciones se cumplieron en total?", "2+2+2+1+1", "Se suman las cumplidas de cada momento.", " observaciones"),
        ("=", "{F} ¿Qué porcentaje de las observaciones se cumplió en total?", "(2+2+2+1+1)*100//(3+2+2+2+1)", "Se divide el total de cumplidas entre el total de observaciones y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje se cumplió en el momento M4?", "1*100//2", "Se divide lo cumplido entre lo observado y se multiplica por 100.", " %"),
        ("abc", "{F} ¿En qué momento fue más baja la adherencia?", "En M4: después de tocar a un paciente", "En M1: antes de tocar a un paciente", "En M5: después de tocar el entorno", "M4 cumplió 1 de 2, solo la mitad; M1 cumplió 2 de 3, más de la mitad; M5 cumplió su única observación."),
        ("abc", "{F} Un técnico usó los mismos guantes con dos pacientes. ¿Qué riesgo representa?", "Puede transmitir microbios de un paciente al otro", "Ninguno, porque los guantes protegen del todo", "Solo gasta más guantes", "Los guantes pueden llevar microbios de un paciente a otro si no se cambian."),
        ("abc", "{F} Otro técnico salió de la sala con los guantes puestos y tocó una manilla. ¿Qué corresponde?", "Informar el hallazgo sin nombres y reforzar el cambio de guantes según el protocolo", "Anotar su nombre para sancionarlo", "No informar, porque es poco importante", "Se informa el hecho para mejorar el servicio, sin nombres."),
        ("abc", "{F} La enfermera propone mejorar M4. ¿Qué mejora es razonable para el técnico proponer?", "Dejar recordatorios y dispensadores visibles junto a las camas", "Poner un listado con los nombres de quienes fallan", "Eliminar M4 de la planilla", "Facilitar el acceso y recordar ayuda a cumplir sin culpar."),
        ("abc", "{F} Un compañero dice: «Con 8 de 10 cumplidas ya estamos bien». ¿Qué corresponde responder?", "Que es un 80 % y que se compara con la meta del servicio", "Que sí, porque más de la mitad es suficiente", "Que no importa, porque el resultado es de ejemplo", "Para saber si es suficiente se compara con la meta; 8 de 10 es 80 %."),
        ("=", "{F} Si se mejora M4 y se cumplen las dos observaciones, ¿cuántas observaciones cumplidas habría en total?", "2+2+2+2+1", "Se suman las cumplidas con M4 corregido a 2.", " observaciones"),
        ("abc", "En Atención de Enfermería: ¿por qué los resultados de una observación se informan sin nombres?", "Porque el objetivo es mejorar el servicio y no castigar a las personas", "Porque las personas no deben saber que las observan", "Porque solo importa el resultado de la enfermera", "Informar sin nombres favorece el aprendizaje y la confianza."),
    ],
    ctx=("abc", "{F} Una técnica ve que otra, con quien trabaja, no se higieniza las manos después de tocar a un paciente. La enfermera no está cerca. ¿Qué hace?", "Se lo recuerda con respeto y, si se repite, avisa a la enfermera", "Lo anota con su nombre y se lo muestra a todos", "No dice nada, para evitar conflictos", "Recordarlo con respeto protege a los pacientes; si se repite se informa a quien coordina la prevención."),
    sc=[
        ("En Atención de Enfermería: ¿cómo se calcula la adherencia?", "Cumplidas × 100 ÷ observadas", "Compara lo cumplido con lo que se observó."),
        ("¿Qué haces con los resultados de la observación?", "Los informo sin nombres para mejorar", "El objetivo es aprender, no castigar."),
        ("¿Los guantes reemplazan la higiene de manos?", "No", "Pueden contaminarse y deben cambiarse según el protocolo."),
    ],
    op=("Planilla de ejemplo: «M1 antes de tocar a un paciente: 4 observaciones, 3 cumplidas. M2 antes de una tarea limpia: 3 observaciones, 3 cumplidas. M3 después de un posible contacto con fluidos: 2 observaciones, 1 cumplida. M4 después de tocar a un paciente: 5 observaciones, 4 cumplidas. M5 después de tocar el entorno: 2 observaciones, 1 cumplida». "
        "Calcula: el porcentaje en cada momento; el total y el porcentaje general; y cuál es el momento más bajo. Escribe una mejora que propondrías a la enfermera, sin culpar a nadie.",
        "M1 75 %, M2 100 %, M3 50 %, M4 80 %, M5 50 %. Total: 4+3+2+5+2 = 16 observaciones y 3+3+1+4+1 = 12 cumplidas; 12 × 100 ÷ 16 = 75 %. Los momentos más bajos son M3 y M5, empatados en 50 %. Mejora: dispensadores visibles y recordatorios, sin nombres.",
        ["calcula el porcentaje de cada momento", "calcula el total 75 %", "identifica los momentos más bajos (M3 y M5)", "propone una mejora sin culpar"],
        ["hoja con cinco porcentajes, un total, los momentos más bajos y una mejora"],
        ["dividir mal", "decir que hay un único momento más bajo", "proponer una sanción con nombres"],
        "Pregunta: «¿hay un solo momento más bajo?». Debe notar que M3 y M5 empatan en 50 %."),
    reinforce="Con 6 observaciones y 5 cumplidas, calcula la adherencia; luego escribe una mejora para el momento más bajo de la ficha.",
    extend="Explica con un ejemplo inventado por qué una sanción individual puede empeorar el cumplimiento de la higiene de manos.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (indicadores semanales de un servicio de ejemplo, inventado). Pacientes atendidos en la semana: 250. Infecciones asociadas a la atención registradas: 5. Observaciones de higiene de manos: 120, con 96 cumplidas. Meta de cumplimiento (de ejemplo): 85 %. "
     "Insumos: 6 cajas de guantes con 100 unidades cada una; consumo diario de ejemplo: 75 guantes. Regla del servicio: cuando el stock llega a 2 días de consumo, se avisa a la enfermera para reponer.")
build(
    O5, 4, F,
    use="Aprenderé a calcular indicadores simples de prevención de infecciones, a comparar con una meta y a controlar el stock de insumos con enteros.",
    prior=["Sé calcular porcentajes.", "Conozco la adherencia a la higiene de manos.", "Sé dividir números enteros."],
    explain=[
        "Un indicador es un número que resume cómo va una actividad. La tasa de infecciones es la cantidad de casos dividida por los pacientes atendidos y multiplicada por 100: se expresa por cada 100 pacientes. Por ejemplo, 3 casos en 150 pacientes son 2 casos por cada 100 pacientes. La adherencia a la higiene de manos es otro indicador: las cumplidas por 100 divididas por las observadas.",
        "Un indicador se compara con una meta para saber cuánto falta. También se controla el stock de insumos: los días que dura el stock se calculan dividiendo la cantidad de unidades entre el consumo diario. Si el stock llega al mínimo que fija la regla del servicio, se avisa a la enfermera, que gestiona la reposición.",
        "Los datos son inventados; los indicadores sirven para mejorar los procesos y no para evaluar personas." + LIM,
    ],
    vocab=[("indicador", "número que resume cómo va una actividad"), ("tasa por 100 pacientes", "casos divididos por pacientes atendidos y multiplicados por 100"), ("meta", "valor que el servicio se propone alcanzar"), ("stock", "cantidad de unidades de un insumo disponible"), ("consumo diario", "unidades que se usan en un día"), ("reposición", "compra o entrega de insumos para volver al stock necesario")],
    worked=[
        ("Calcular una tasa", "Un servicio de ejemplo atendió a 200 pacientes y registró 4 infecciones. ¿Cuántos casos hay por cada 100 pacientes?", ["Se multiplican los casos por 100: 4 × 100 = 400.", "400 ÷ 200 = 2."], "2 casos por cada 100 pacientes"),
        ("Días de stock", "Una sala de ejemplo tiene 300 mascarillas y usa 60 por día. ¿Para cuántos días alcanza?", ["Se divide el stock entre el consumo diario.", "300 ÷ 60 = 5."], "5 días")],
    mistakes=[("Decir que 5 infecciones es «mucho» o «poco» sin saber cuántos pacientes se atendieron.", "Un número solo no se puede comparar; hay que relacionarlo con el total de pacientes.", "Calcula la tasa por 100 pacientes."),
              ("Esperar a que se acaben los guantes para avisar.", "Un stock agotado deja al personal sin protección.", "Avisa cuando el stock llega al mínimo que fija la regla.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un indicador?", "Un número que resume cómo va una actividad", "Un diagnóstico del paciente", "Una instrucción de la enfermera", "Un indicador es un número que resume y permite comparar."),
        ("=", "{F} ¿Cuántas infecciones por cada 100 pacientes registró el servicio?", "5*100//250", "Se multiplican los casos por 100 y se dividen entre los pacientes atendidos.", " casos por 100 pacientes"),
        ("=", "{F} ¿Qué porcentaje de cumplimiento de higiene de manos tuvo el servicio?", "96*100//120", "Se divide lo cumplido entre lo observado y se multiplica por 100.", " %"),
        ("abc", "{F} ¿El servicio alcanzó la meta de higiene de manos?", "No: su cumplimiento fue 80 %, menor que la meta de 85 %", "Sí, porque cumplió más de la mitad", "Sí, porque tuvo 96 cumplidas", "Con 80 % no se alcanza la meta de 85 %."),
        ("=", "{F} ¿Cuántas oportunidades de las 120 se habrían debido cumplir para llegar a la meta del 85 %?", "120*85//100", "Se calcula el 85 % de las observaciones.", " oportunidades"),
        ("=", "{F} ¿Cuántas oportunidades más se debieron cumplir para llegar a la meta?", "120*85//100-96", "Se resta lo cumplido de lo necesario para la meta.", " oportunidades"),
        ("=", "{F} ¿Cuántos guantes hay en el stock?", "6*100", "Se multiplican las cajas por las unidades de cada caja.", " guantes"),
        ("=", "{F} ¿Para cuántos días alcanza el stock de guantes?", "6*100//75", "Se divide el stock entre el consumo diario.", " días"),
        ("=", "{F} ¿Cuántos guantes corresponden a 2 días de consumo, el mínimo que fija la regla?", "2*75", "Se multiplica el consumo diario por los 2 días del mínimo.", " guantes"),
        ("=", "{F} ¿Cuántos guantes quedarían después de 5 días de consumo?", "6*100-5*75", "Se resta del stock el consumo de 5 días.", " guantes"),
        ("abc", "{F} Al cabo de 6 días, el stock queda en 150 guantes. ¿Qué corresponde según la regla?", "Avisar a la enfermera para reponer, porque el stock llegó a 2 días de consumo", "Esperar a que se acaben", "Racionar los guantes para que duren más", "La regla dice avisar cuando el stock llega a 2 días de consumo: 150 guantes."),
        ("abc", "{F} Un compañero propone usar menos guantes para que el stock dure más. ¿Qué corresponde?", "No reducir el uso necesario; avisar para reponer según la regla", "Usar la mitad para ahorrar", "Comprar guantes por su cuenta", "El uso de elementos de protección sigue el protocolo; el stock se repone avisando a quien corresponde."),
        ("abc", "{F} Una visita pregunta cuántas infecciones hubo en el servicio. ¿Qué responde el técnico?", "Que las cifras las entrega la enfermera responsable del programa", "Que dos, sin dar más detalles", "Que no sabe nada de eso", "Las cifras del programa las informa quien las coordina; el técnico no entrega datos por su cuenta."),
    ],
    ctx=("abc", "{F} Al contar los guantes, la técnica ve que quedan 140, menos que el mínimo de 2 días (150 guantes). La enfermera está en una reunión. ¿Qué hace?", "Deja el aviso escrito a la enfermera con la cantidad contada y, si es urgente, avisa a su jefatura", "Pide guantes prestados a otro servicio sin avisar", "Espera a que la enfermera salga de la reunión sin dejar aviso", "El aviso con la cantidad contada permite reponer a tiempo, sin improvisar."),
    sc=[
        ("En Atención de Enfermería: ¿cómo calculas la tasa por 100 pacientes?", "Casos × 100 ÷ pacientes atendidos", "Relaciona los casos con el total de pacientes."),
        ("¿Cómo calculas los días que dura el stock?", "Divido el stock entre el consumo diario", "Así se sabe cuándo avisar para reponer."),
        ("¿Qué haces si el stock llega al mínimo?", "Aviso a la enfermera", "La regla del servicio pide avisar en ese punto."),
    ],
    op=("Datos de ejemplo de una semana: «150 pacientes atendidos; 3 infecciones registradas; 100 observaciones de higiene de manos con 90 cumplidas; meta 85 %; stock de 4 cajas de mascarillas de 50 unidades; consumo diario de 40 mascarillas; mínimo para reponer: 2 días de consumo». "
        "Calcula: casos por 100 pacientes, porcentaje de higiene de manos y si alcanzó la meta, días de stock y cuántas mascarillas son el mínimo. Escribe a quién avisarías y cuándo.",
        "Casos: 3 × 100 ÷ 150 = 2 por cada 100 pacientes. Higiene de manos: 90 %, sí alcanza la meta de 85 %. Stock: 200 mascarillas; 200 ÷ 40 = 5 días. Mínimo: 80 mascarillas. Avisaría a la enfermera cuando el stock llegue a 80.",
        ["calcula 2 casos por 100 pacientes", "calcula 90 % y compara con la meta", "calcula 5 días y 80 mascarillas", "indica avisar a la enfermera al llegar al mínimo"],
        ["hoja con la tasa, un porcentaje, los días de stock y el aviso"],
        ["calcular mal los días de stock", "decir que 90 % no alcanza", "no avisar a la enfermera"],
        "Pregunta: «¿tu tasa sale de multiplicar los casos por 100 y dividir entre los pacientes?». Si no, pídele rehacerla."),
    reinforce="Con 600 guantes y un consumo de 50 por día, calcula los días del stock y cuántos guantes son 3 días de consumo.",
    extend="Explica con un ejemplo inventado por qué un indicador se debe comparar con el total de pacientes.",
)


# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (registro de un hospital de ejemplo, inventado). La ficha clínica de cada paciente está en papel y en un sistema digital. Cada trabajador tiene una clave personal e intransferible y el sistema deja constancia de cada ingreso a una ficha. "
     "En un servicio de 20 camas, cada técnico tiene a su cargo 7 pacientes; por paciente, en el turno, anota 4 registros de control y 2 anotaciones de cuidados. Cada anotación toma 2 minutos. "
     "Reglas del hospital: nadie entra a la ficha de un paciente que no atiende; las claves no se comparten; se cierra la sesión al retirarse del computador; las fichas en papel no quedan a la vista.")
build(
    O6, 1, F,
    use="Aprenderé qué es la ficha clínica, por qué es confidencial, qué reglas protegen la privacidad en un registro manual y digital y por qué hay que registrar a tiempo.",
    prior=["Sé qué es un registro fiel.", "Sé multiplicar y sumar números enteros.", "Conozco los derechos del paciente."],
    explain=[
        "En Atención de Enfermería, la ficha clínica es el documento donde se registra la información de salud de una persona: lo que le ocurre, lo que se le indica y lo que se hace. Es confidencial, porque los datos de salud son datos personales sensibles. Solo pueden verla las personas del equipo que atienden a esa persona, y la norma vigente regula quién puede acceder a ella y cómo se entrega a un paciente o a su representante.",
        "El registro puede ser manual, en papel, o digital, en un sistema. En ambos se registra a tiempo, con hechos, hora y firma. En el sistema digital la clave personal funciona como una firma: quien la comparte responde por lo que otro haga con ella. Se cierra la sesión al retirarse y la ficha en papel no se deja a la vista. Registrar de forma oportuna significa anotar lo ocurrido cerca del momento en que ocurrió, para no olvidar ni inventar datos.",
        "El técnico no divulga datos de salud por teléfono, mensajes ni redes sociales." + LIM,
    ],
    vocab=[("ficha clínica", "documento con la información de salud de una persona, confidencial"), ("dato personal sensible", "dato de salud o íntimo que requiere una protección especial"), ("clave personal", "contraseña individual e intransferible que identifica a quien accede"), ("registro oportuno", "anotación hecha cerca del momento en que ocurrió el hecho"), ("acceso a la ficha", "posibilidad de ver o anotar en la ficha, solo para quien atiende al paciente"), ("sesión", "tiempo en que alguien está dentro del sistema con su clave")],
    worked=[
        ("Quién puede ver una ficha", "Un técnico de ejemplo atiende a los pacientes de la cama 1 a la 6. Siente curiosidad por la ficha de un paciente de la cama 15, a cargo de otro equipo. ¿Puede abrirla?", ["Solo se accede a la ficha de quien se atiende.", "La curiosidad no es una razón para acceder."], "No: solo se accede a la ficha de los pacientes que atiende"),
        ("Carga de registros", "En otro servicio de ejemplo, un técnico tiene 5 pacientes y anota 3 registros por paciente, de 2 minutos cada uno. ¿Cuántos minutos le toma registrar?", ["5 pacientes × 3 registros = 15 registros.", "15 × 2 = 30 minutos."], "30 minutos"),
    ],
    mistakes=[("Prestar la clave personal a un compañero «solo para esta anotación».", "La clave identifica a quien la tiene: lo que el otro haga quedará a nombre del dueño.", "Cada persona usa solo su clave; si hay una dificultad, se avisa a la enfermera."),
              ("Contar por teléfono a un «familiar» cómo está un paciente.", "No se puede comprobar quién es la persona; los datos de salud son confidenciales.", "Deriva la consulta a la enfermera o al profesional que corresponde.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la ficha clínica?", "El documento con la información de salud de una persona, que es confidencial", "La lista de camas del servicio", "El carné de identidad del paciente", "La ficha clínica contiene datos de salud y por eso es confidencial."),
        ("abc", "{F} ¿Qué identifica a cada trabajador que entra a una ficha en el sistema?", "Su clave personal e intransferible", "El número de cama", "El nombre del paciente", "La ficha dice que cada trabajador tiene una clave personal y que el sistema deja constancia de cada ingreso."),
        ("abc", "{F} ¿Qué debe hacer un técnico al retirarse del computador, según las reglas?", "Cerrar la sesión", "Dejar la sesión abierta para volver rápido", "Pedir a un compañero que cuide la sesión", "La regla del hospital pide cerrar la sesión al retirarse."),
        ("=", "{F} ¿Cuántas anotaciones hace un técnico por paciente en el turno (registros de control y de cuidados)?", "4+2", "Se suman los registros de control y las anotaciones de cuidados de cada paciente.", " anotaciones"),
        ("=", "{F} ¿Cuántas anotaciones hace un técnico en el turno entre sus 7 pacientes?", "7*(4+2)", "Se multiplican las anotaciones por paciente por la cantidad de pacientes.", " anotaciones"),
        ("=", "{F} ¿Cuántos minutos le toma a un técnico hacer todas sus anotaciones del turno?", "7*(4+2)*2", "Se multiplican las anotaciones del turno por los minutos de cada una.", " minutos"),
        ("abc", "{F} Una compañera pide la clave del técnico «porque la suya no funciona y hay un registro urgente». ¿Qué corresponde?", "No prestarla, avisar a la enfermera y registrar con su propia clave cuando se repare", "Prestarla, porque es urgente", "Prestarla y cambiarla después", "La clave es personal; si hay una dificultad, se avisa y se usa la vía que indique el hospital."),
        ("abc", "{F} Al terminar el turno, un técnico quiere llevarse a casa una copia de la planilla de su sala «para estudiar». ¿Qué corresponde?", "No llevarla: los datos de los pacientes no salen del hospital", "Llevarla si la devuelve al día siguiente", "Llevarla si tapa los nombres con corrector", "La información de los pacientes es confidencial y se maneja solo dentro del establecimiento."),
        ("abc", "{F} Una visita pide al técnico una foto de la ficha de su familiar «para mostrarla a otro médico». ¿Qué corresponde?", "Derivar la solicitud a la enfermera, que indicará cómo se entrega según la norma vigente", "Fotografiarla con su celular", "Mostrarla un momento y que la fotografíe la visita", "La entrega de la ficha o de copias la regula la norma vigente y la gestionan quienes corresponde."),
        ("abc", "Un técnico decide anotar al final del turno todo lo que ocurrió desde la mañana. ¿Qué riesgo tiene?", "Puede olvidar o inventar datos al anotar tan tarde", "Ninguno, porque anota todo junto", "Que gaste menos tiempo", "El registro oportuno evita olvidos y errores."),
        ("abc", "{F} Una técnica deja la ficha en papel de un paciente abierta sobre el mesón de la entrada. ¿Qué falla tiene?", "Cualquier persona puede leer datos de salud", "Se arruga el papel", "Nadie encuentra la ficha", "Dejar la ficha a la vista expone datos confidenciales."),
        ("=", "{F} Si un técnico tuviera 5 pacientes en vez de 7, ¿cuántos minutos le tomarían sus anotaciones del turno?", "5*(4+2)*2", "Se multiplican los pacientes por las anotaciones y por los minutos de cada una.", " minutos"),
        ("abc", "En Atención de Enfermería: ¿por qué los datos de salud son «sensibles»?", "Porque su difusión puede perjudicar a la persona y requiere una protección especial", "Porque solo los entiende el médico", "Porque cambian cada día", "Su difusión puede afectar la dignidad, el trabajo o las relaciones de la persona."),
    ],
    ctx=("abc", "{F} Un técnico recibe un mensaje de un conocido que le pregunta si un paciente de su servicio ingresó anoche, porque «es amigo de la familia». ¿Qué hace?", "No confirma ni niega nada y le indica que consulte por los canales oficiales del hospital", "Le confirma, porque es un conocido de confianza", "Le cuenta el motivo del ingreso para que apoye", "Confirmar o negar un ingreso ya entrega un dato de salud; solo se informa por los canales oficiales."),
    sc=[
        ("En Atención de Enfermería: ¿quién puede acceder a la ficha de un paciente?", "El equipo que lo atiende", "La ficha es confidencial y solo la ve el equipo tratante."),
        ("¿Puedes prestar tu clave personal?", "No", "La clave es intransferible y responde por quien la tiene."),
        ("¿Qué haces si te piden datos de un paciente por teléfono?", "Derivo a la enfermera o al profesional", "No se puede comprobar quién llama."),
    ],
    op=("Caso de ejemplo: un técnico atiende a 6 pacientes y anota 5 registros por paciente en el turno, de 2 minutos cada uno. Una persona que dice ser hija de un paciente lo llama por teléfono y le pide que le diga qué le pasó a su padre. "
        "Escribe: cuántos registros hace el técnico y cuántos minutos toman; qué responde a la persona que llama y por qué; a quién avisa; y una frase de registro del hecho, sin datos de salud.",
        "Registros: 6 × 5 = 30; minutos: 30 × 2 = 60. Responde que no puede entregar información por teléfono y que consulte por los canales del hospital, porque no puede comprobar quién es y los datos son confidenciales. Avisa a la enfermera. Registro: «Llamada telefónica de una persona que pidió información de la cama 8; se derivó a la enfermera».",
        ["calcula 30 registros y 60 minutos", "no entrega datos y explica por qué", "avisa a la enfermera", "el registro no incluye datos de salud"],
        ["hoja con cálculos, una respuesta, a quién avisa y una frase de registro"],
        ["dar información por teléfono", "incluir datos de salud en el registro del hecho", "calcular mal"],
        "Pregunta: «¿tu frase de registro contiene algún dato de salud del paciente?». Si sí, pídele quitarlo."),
    reinforce="Escribe tres reglas que protegen la privacidad de la ficha clínica y una razón para cada una.",
    extend="Explica con un ejemplo inventado qué podría ocurrirle a una persona si sus datos de salud se difunden sin su autorización.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (documentos de un hospital de ejemplo, inventado). Ingreso: formulario de admisión (identificación y datos de contacto), consentimiento informado (lo firma la persona o su representante después de que el profesional le explicó), pulsera de identificación y hoja de ingreso de enfermería. "
     "Permanencia: hoja de indicaciones (la escribe el profesional), hoja de control de signos, registro de cuidados y censo diario de camas. Egreso: resumen de alta (lo escribe el profesional), indicaciones al alta (las entrega el profesional) y hoja de egreso administrativa. "
     "El técnico registra lo que le corresponde en las hojas de control y de cuidados; no escribe el resumen de alta ni entrega indicaciones de tratamiento.")
build(
    O6, 2, F,
    use="Aprenderé las etapas de ingreso, permanencia y egreso, qué documentos se usan en cada una, quién escribe cada uno y qué es el consentimiento informado.",
    prior=["Conozco la ficha clínica y su confidencialidad.", "Sé leer una ficha.", "Sé contar elementos de una lista."],
    explain=[
        "Un paciente pasa por tres etapas en un establecimiento: el ingreso, la permanencia y el egreso. El ingreso es cuando la persona entra al servicio y se registra su identificación y sus datos, se confirma su identidad con una pulsera y se firma el consentimiento informado. La permanencia es el tiempo en que está en el servicio, con hojas de indicaciones, de control y de cuidados. El egreso es la salida del establecimiento, por alta, traslado o fallecimiento, con un resumen y sus documentos.",
        "El consentimiento informado es la aceptación libre de la persona, o de su representante, luego de que el profesional le explica lo que se le propone. No lo obtiene el técnico: él puede, a lo más, acompañar la entrega del documento a quien corresponde. La identificación correcta es una regla de seguridad: el nombre y el número de ficha del paciente deben coincidir en todos sus documentos.",
        "Los datos de las personas son de ejemplo en esta clase, y el trabajo con documentos reales exige la supervisión de un profesional." + LIM,
    ],
    vocab=[("ingreso", "momento en que una persona entra al establecimiento y se registran sus datos"), ("permanencia", "tiempo en que la persona está en el servicio, con sus cuidados y controles"), ("egreso", "salida del establecimiento, por alta, traslado o fallecimiento"), ("consentimiento informado", "aceptación libre de la persona luego de recibir información del profesional"), ("identificación del paciente", "nombre y número de ficha que deben coincidir en todos los documentos"), ("censo diario", "recuento diario de camas ocupadas, ingresos y egresos")],
    worked=[
        ("Ubicar un documento", "En un hospital de ejemplo, la «hoja de control de signos» se usa mientras la persona está en el servicio. ¿A qué etapa pertenece?", ["Se usa durante los días de atención.", "Es un documento de la permanencia."], "Permanencia"),
        ("Contar documentos", "En un servicio de ejemplo, el ingreso usa 4 documentos y el egreso, 3. ¿Cuántos documentos suman entre ambas etapas?", ["Se suman los de ingreso y los de egreso.", "4 + 3 = 7."], "7 documentos")],
    mistakes=[("Pensar que el consentimiento informado es «la firma de cualquier papel».", "Es la aceptación libre después de recibir información comprensible del profesional.", "Recuerda: primero información del profesional, después la decisión y la firma."),
              ("Escribir el resumen de alta «para ayudar a la enfermera».", "El resumen de alta es un documento profesional que el técnico no redacta.", "Registra solo lo que te corresponde en las hojas de control y de cuidados.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es el consentimiento informado?", "La aceptación libre de la persona luego de recibir información del profesional", "La firma de la visita en la hoja de ingreso", "La autorización del técnico para realizar un cuidado", "El consentimiento es de la persona o de su representante, después de que el profesional le explica."),
        ("abc", "{F} ¿A qué etapa pertenece la pulsera de identificación?", "Al ingreso", "Al egreso", "A la permanencia", "La ficha incluye la pulsera entre los documentos del ingreso."),
        ("abc", "{F} ¿A qué etapa pertenece el resumen de alta?", "Al egreso", "Al ingreso", "A la permanencia", "El resumen de alta se hace cuando la persona sale del establecimiento."),
        ("abc", "{F} ¿Quién escribe el resumen de alta?", "El profesional", "El técnico en enfermería", "La visita", "La ficha dice que el resumen de alta lo escribe el profesional."),
        ("abc", "{F} ¿Cuántos documentos hay en la etapa de ingreso?", "Cuatro", "Tres", "Cinco", "La ficha asigna al ingreso la admisión, el consentimiento, la pulsera y la hoja de ingreso de enfermería."),
        ("=", "{F} ¿Cuántos documentos hay en total entre ingreso, permanencia y egreso?", "4+4+3", "Se suman los documentos de las tres etapas.", " documentos"),
        ("abc", "{F} ¿En qué documentos registra el técnico lo que le corresponde durante la permanencia?", "En las hojas de control y de cuidados", "En el resumen de alta", "En el formulario de admisión", "La ficha dice que el técnico registra en las hojas de control y de cuidados."),
        ("abc", "{F} Un paciente del servicio tiene la pulsera con el nombre «Carlos Rojas» y la hoja de control dice «Carlos Rojo». ¿Qué corresponde?", "Avisar a la enfermera para verificar la identificación antes de registrar", "Corregir la hoja sin avisar", "Seguir registrando, porque son nombres parecidos", "Los datos de identificación deben coincidir; se verifica antes de seguir registrando para evitar errores."),
        ("abc", "{F} Un familiar pide al técnico que le entregue «las indicaciones al alta». ¿Qué corresponde?", "Derivar a la enfermera o al profesional, porque esas indicaciones las entrega el profesional", "Entregarlas, porque ya están escritas", "Explicarle qué debe hacer en casa", "Las indicaciones al alta las entrega el profesional que las indica."),
        ("abc", "{F} Un paciente dice «no sé qué firmé en admisión». ¿Qué corresponde?", "Avisar a la enfermera para que el profesional le explique sus documentos", "Decirle que no se preocupe", "Explicarle los documentos él mismo", "El consentimiento requiere información del profesional; se avisa para que se aclare."),
        ("=", "{F} Si cada ingreso genera los 4 documentos de ingreso y cada egreso los 3 de egreso, ¿cuántos documentos se generan con 3 ingresos y 2 egresos?", "3*4+2*3", "Se multiplican los ingresos por sus documentos y los egresos por los suyos, y se suman.", " documentos"),
        ("abc", "{F} ¿Qué documento permite saber cuántas camas están ocupadas cada día?", "El censo diario", "El consentimiento informado", "La pulsera de identificación", "El censo diario cuenta camas ocupadas, ingresos y egresos."),
        ("abc", "En Atención de Enfermería: ¿qué significa que un paciente tenga un egreso por traslado?", "Que sale de este servicio hacia otro lugar de atención", "Que fue dado de alta definitiva en su casa", "Que sigue en el mismo servicio", "El traslado es un tipo de egreso: la persona sale hacia otro establecimiento o servicio."),
    ],
    ctx=("abc", "{F} Un paciente se prepara para su alta y la técnica nota que el resumen de alta no tiene la firma del profesional que debe entregar las indicaciones. ¿Qué hace?", "Avisa a la enfermera antes de que la persona se retire y no entrega documentos por su cuenta", "Entrega los documentos tal como están", "Firma ella para que no se retrase el alta", "Un documento incompleto se informa a quien corresponde; el técnico no firma por otro."),
    sc=[
        ("En Atención de Enfermería: ¿cuáles son las tres etapas de un paciente en el establecimiento?", "Ingreso, permanencia y egreso", "Representan la entrada, el tiempo de atención y la salida."),
        ("¿Quién obtiene el consentimiento informado?", "El profesional", "El técnico no lo obtiene porque lo explica el profesional."),
        ("¿Qué datos deben coincidir en todos los documentos?", "El nombre y el número de ficha", "Así se evita confundir a una persona con otra."),
    ],
    op=("Ficha de ejemplo: «Documentos de un servicio: formulario de admisión, hoja de control de signos, consentimiento informado, resumen de alta, registro de cuidados, hoja de egreso administrativa, pulsera de identificación, censo diario, indicaciones al alta». "
        "Clasifica cada documento por etapa (ingreso, permanencia o egreso); cuenta cuántos hay por etapa; escribe cuáles registra el técnico y cuáles no; y a quién avisarías si el nombre de la pulsera no coincide con el de la hoja de control.",
        "Ingreso: formulario de admisión, consentimiento informado, pulsera (3). Permanencia: hoja de control, registro de cuidados, censo diario (3). Egreso: resumen de alta, hoja de egreso, indicaciones al alta (3). El técnico registra en la hoja de control y en el registro de cuidados; no escribe el resumen de alta ni entrega las indicaciones. Si el nombre no coincide, avisa a la enfermera antes de registrar.",
        ["clasifica los nueve documentos", "cuenta 3 por etapa", "indica qué registra y qué no el técnico", "avisa a la enfermera ante el error de identidad"],
        ["hoja con una clasificación, tres cantidades, los documentos del técnico y un aviso"],
        ["asignar el consentimiento al técnico", "no verificar la identidad", "clasificar mal el censo diario"],
        "Pregunta: «¿quién entrega las indicaciones al alta?». Debe responder el profesional."),
    reinforce="Escribe dos documentos de cada etapa y quién los escribe.",
    extend="Explica con un ejemplo inventado por qué un nombre mal escrito en un documento puede ser un riesgo de seguridad.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (situaciones de ejemplo y pauta de privacidad). Pauta de cinco buenas prácticas: (1) acceder solo a la ficha de quien se atiende; (2) no compartir la clave; (3) cerrar la sesión al retirarse; (4) no dejar fichas ni datos a la vista; (5) no entregar información de salud por canales no autorizados. "
     "Situación A: un técnico abre la ficha de un vecino que se hospitalizó en otro servicio. Situación B: una técnica le dice su clave a un compañero para que anote por ella. Situación C: un técnico se va a colación y deja la sesión abierta en el computador de la sala. "
     "Situación D: una técnica deja la planilla de pacientes sobre el mesón de entrada. Situación E: un técnico envía por mensajería una foto de una hoja de control con el nombre del paciente a un amigo. "
     "Situación F: una técnica cierra su sesión, guarda las fichas en su lugar y deriva a la enfermera las consultas de las visitas.")
build(
    O6, 3, F,
    use="Aprenderé a analizar situaciones de registro con una pauta de privacidad, a reconocer qué práctica se vulneró y a decidir qué se informa y a quién.",
    prior=["Conozco la ficha clínica y los documentos de cada etapa.", "Sé calcular porcentajes de números enteros.", "Conozco las claves personales."],
    explain=[
        "Analizar un caso de registro es comparar lo que ocurrió con una pauta. Cada práctica de la pauta protege un aspecto de la privacidad: el acceso solo a quien se atiende evita la curiosidad indebida; la clave personal asegura que se sepa quién hizo qué; cerrar la sesión impide que otra persona use la clave de alguien; no dejar datos a la vista evita que los lea quien pasa; y los canales autorizados protegen los datos al comunicarlos.",
        "Una falta de privacidad no se esconde. Se informa a la enfermera o a la jefatura, con hechos, para que se tomen las medidas que corresponden según el protocolo y la norma vigente. Algunas faltas, como compartir una clave, pueden tener consecuencias para quien la compartió, porque lo que otro haga con ella queda a su nombre. La confidencialidad se mantiene incluso después de terminar el trabajo.",
        "Esta clase es conceptual: no enseña a tomar medidas disciplinarias ni legales." + LIM,
    ],
    vocab=[("pauta de privacidad", "lista de buenas prácticas para proteger los datos de salud"), ("falta de privacidad", "conducta que expone o usa indebidamente datos de salud de una persona"), ("canal autorizado", "medio oficial del establecimiento para comunicar información"), ("confidencialidad", "deber de reservar los datos que se conocen por el trabajo"), ("incidente", "hecho que afecta o pudo afectar la seguridad de los datos")],
    worked=[
        ("Aplicar la pauta", "Una técnica de ejemplo deja el computador con la sesión abierta mientras atiende a un paciente en la otra sala. ¿Qué práctica incumple?", ["Debe cerrar la sesión al retirarse.", "Incumple la práctica 3."], "La práctica 3: cerrar la sesión al retirarse"),
        ("Calcular un cumplimiento", "En una revisión de ejemplo, un servicio cumplió 4 de las 5 prácticas. ¿Qué porcentaje es?", ["4 × 100 = 400.", "400 ÷ 5 = 80."], "80 %")],
    mistakes=[("Pensar que enviar una foto de una hoja a un amigo «no hace daño» si el amigo no conoce al paciente.", "Se difunden datos de salud por un canal no autorizado, fuera de control.", "Nunca envíes datos de pacientes por mensajería personal."),
              ("Callar una falta de privacidad propia porque «nadie se dio cuenta».", "Ocultar el incidente impide protegerse y proteger a la persona afectada.", "Informa a la enfermera o a la jefatura con los hechos.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la confidencialidad?", "El deber de reservar los datos que se conocen por el trabajo", "El deber de compartir los datos con todo el equipo", "El derecho del técnico a ver cualquier ficha", "La confidencialidad obliga a reservar los datos de las personas atendidas."),
        ("abc", "{F} ¿Qué práctica incumple la situación A?", "La práctica 1: acceder solo a la ficha de quien se atiende", "La práctica 3: cerrar la sesión", "La práctica 4: no dejar datos a la vista", "Abrir la ficha de un vecino que no atiende vulnera el acceso limitado a quien se atiende."),
        ("abc", "{F} ¿Qué práctica incumple la situación B?", "La práctica 2: no compartir la clave", "La práctica 1: acceder solo a la ficha de quien se atiende", "La práctica 5: canales autorizados", "Decir la clave a un compañero incumple el deber de no compartirla."),
        ("abc", "{F} ¿Qué práctica incumple la situación E?", "La práctica 5: no entregar información por canales no autorizados", "La práctica 2: no compartir la clave", "La práctica 3: cerrar la sesión", "Enviar una foto por mensajería personal difunde datos por un canal no autorizado."),
        ("abc", "{F} ¿Qué práctica incumple la situación D?", "La práctica 4: no dejar fichas ni datos a la vista", "La práctica 1: acceder solo a quien se atiende", "La práctica 2: no compartir la clave", "Dejar la planilla en el mesón expone datos a quien pase."),
        ("abc", "{F} ¿Qué situación cumple todas las prácticas?", "La situación F", "La situación C", "La situación A", "Solo la situación F cierra la sesión, guarda las fichas y deriva las consultas."),
        ("=", "{F} Si cada situación de la A a la F se evalúa con una sola práctica, ¿cuántas situaciones incumplen alguna práctica?", "6-1", "Se restan de las seis situaciones la que cumple todas.", " situaciones"),
        ("=", "{F} En una revisión de ejemplo de 15 puestos de trabajo, 12 cumplieron la práctica 3 (cerrar la sesión). ¿Qué porcentaje de los puestos la cumplió?", "12*100//15", "Se divide la cantidad de puestos que cumplen entre el total de puestos y se multiplica por 100.", " %"),
        ("abc", "{F} La técnica de la situación B dice: «Fue solo una vez y era urgente». ¿Qué corresponde?", "Informar la situación a la enfermera y registrar el cambio de clave según el protocolo", "No decir nada, porque no hubo daño", "Pedir a su compañero que no cuente nada", "Compartir una clave debe informarse para que se cambie y se proteja el sistema."),
        ("abc", "{F} Un técnico ve que una compañera dejó una ficha en papel sobre una silla del pasillo. ¿Qué hace?", "Avisa a su compañera para que la guarde y, si se repite, informa a la enfermera", "Lee la ficha para saber de quién es", "No hace nada, porque no es su ficha", "Una ficha a la vista puede ser leída por cualquiera; se corrige con respeto y se informa si se repite."),
        ("abc", "{F} Una técnica descubre que envió por error a un amigo una foto con datos de un paciente. ¿Qué hace?", "Avisa de inmediato a su jefatura y a la enfermera, con los hechos", "Borra la foto y no dice nada", "Le pide al amigo que no la mire", "Informar permite tomar medidas para proteger a la persona afectada."),
        ("abc", "{F} Un compañero dice: «Mientras no se difundan los datos, da igual mirar fichas». ¿Qué corresponde responder?", "Que mirar sin atender ya es una falta, aunque no se difunda", "Que tiene razón, mientras no cuente nada", "Que solo es falta si la persona es famosa", "El acceso a una ficha solo se justifica por la atención de la persona."),
        ("abc", "En Atención de Enfermería: ¿por qué la clave personal es como una firma?", "Porque identifica a quien hizo cada acción en el sistema", "Porque se escribe a mano", "Porque la pide el paciente", "El sistema registra con la clave quién hizo cada acción."),
    ],
    ctx=("abc", "{F} Una técnica nota que una de sus compañeras anotó una indicación en la ficha de un paciente con la clave de otra persona que no estaba ese día. ¿Qué hace?", "Informa a la enfermera con los hechos observados, sin acusar", "Borra la anotación", "Se lo cuenta a otras personas del servicio", "Un uso indebido de claves se informa a quien corresponde con hechos; no se resuelve entre compañeros."),
    sc=[
        ("En Atención de Enfermería: ¿qué haces si cometiste una falta de privacidad?", "Lo informo a la enfermera o a la jefatura con los hechos", "Ocultarlo impide proteger a la persona."),
        ("¿Se puede compartir la clave personal?", "No", "La clave identifica a quien la tiene."),
        ("¿Se pueden enviar datos de pacientes por mensajería personal?", "No", "No es un canal autorizado del establecimiento."),
    ],
    op=("Situaciones de ejemplo en un servicio: «(1) una técnica deja una ficha en papel en el carro de insumos mientras sale a otra sala; (2) un técnico cierra la sesión del computador y guarda las fichas al irse; (3) un técnico pide la clave a una compañera porque olvidó la suya; (4) una técnica responde a una visita que debe consultar a la enfermera». "
        "Usa la pauta de la ficha. Escribe: qué práctica incumple cada situación que falla; cuántas de las cuatro cumplen la pauta; y qué informarías a la enfermera, sin juzgar a nadie.",
        "(1) incumple la práctica 4, (2) cumple, (3) incumple la práctica 2 (se pide y se comparte la clave) y (4) cumple. Cumplen 2 de 4. Informaría los hechos de (1) y (3) a la enfermera, sin juzgar.",
        ["identifica las prácticas incumplidas", "cuenta 2 de 4", "informa hechos sin juzgar", "avisa a la enfermera"],
        ["hoja con prácticas incumplidas, un conteo y una frase de informe"],
        ["no reconocer el riesgo de la ficha a la vista", "decir que pedir la clave no es una falta", "juzgar a las personas"],
        "Pregunta: «¿tu informe describe lo que pasó o califica a la persona?». Si califica, pídele reescribirlo con hechos."),
    reinforce="Escribe las cinco buenas prácticas de la pauta con tus palabras y un ejemplo de cada una.",
    extend="Explica con un ejemplo inventado por qué una falta de privacidad pequeña puede tener consecuencias grandes.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (censo de camas de un servicio de ejemplo, inventado). Servicio de 20 camas. Al comenzar el día había 16 camas ocupadas. Durante el día: 5 ingresos, 3 egresos por alta y 1 egreso por traslado a otro servicio. "
     "Estadías de las 4 personas dadas de alta en la semana, en días: 5, 3, 7 y 9. Regla del censo: camas ocupadas al cierre = ocupadas al inicio + ingresos − egresos (altas y traslados). Porcentaje de ocupación = camas ocupadas × 100 ÷ camas totales.")
build(
    O6, 4, F,
    use="Aprenderé a hacer un censo de camas con enteros, a calcular la ocupación y la estadía promedio y a anotar los procedimientos administrativos de ingreso y egreso.",
    prior=["Conozco el ingreso, la permanencia y el egreso.", "Sé calcular porcentajes y promedios de números enteros.", "Sé leer una ficha."],
    explain=[
        "El censo diario es el recuento de camas ocupadas, disponibles, ingresos y egresos de un servicio. Las camas ocupadas al cierre se calculan sumando los ingresos a las ocupadas al inicio y restando los egresos, sean altas o traslados. Las camas disponibles son las totales menos las ocupadas. El porcentaje de ocupación es el cociente entre las ocupadas y las totales, multiplicado por 100.",
        "La estadía es el número de días que una persona permanece en el servicio, desde el ingreso hasta el egreso. La estadía promedio se calcula sumando las estadías de varias personas y dividiendo por la cantidad. El censo ayuda a organizar los turnos y las camas, y se registra con exactitud, porque un error en el censo puede significar que no haya cama para quien la necesita.",
        "Los datos son inventados y no incluyen nombres de personas." + LIM,
    ],
    vocab=[("censo diario", "recuento diario de camas ocupadas, disponibles, ingresos y egresos"), ("camas disponibles", "camas totales menos camas ocupadas"), ("porcentaje de ocupación", "camas ocupadas por 100 divididas por las camas totales"), ("estadía", "días que una persona permanece en el servicio"), ("estadía promedio", "suma de las estadías dividida por la cantidad de personas"), ("traslado", "salida de una persona hacia otro servicio o establecimiento")],
    worked=[
        ("Camas al cierre", "Un servicio de ejemplo tenía 10 camas ocupadas, tuvo 4 ingresos y 2 egresos en el día. ¿Cuántas camas ocupadas hay al cierre?", ["Se suman los ingresos: 10 + 4 = 14.", "Se restan los egresos: 14 − 2 = 12."], "12 camas"),
        ("Estadía promedio", "Tres personas de ejemplo estuvieron 4, 6 y 8 días. ¿Cuál fue la estadía promedio?", ["4 + 6 + 8 = 18.", "18 ÷ 3 = 6."], "6 días")],
    mistakes=[("Olvidar restar los traslados al calcular las camas ocupadas.", "Un traslado también libera una cama.", "Resta todos los egresos: altas y traslados."),
              ("Calcular el porcentaje dividiendo entre las camas ocupadas en vez de las totales.", "El porcentaje de ocupación se mide sobre el total de camas del servicio.", "Divide siempre entre las camas totales.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es el censo diario?", "El recuento diario de camas ocupadas, disponibles, ingresos y egresos", "La lista de indicaciones de cada paciente", "El horario de visitas", "El censo cuenta camas e ingresos y egresos."),
        ("=", "{F} ¿Cuántos egresos hubo en el día entre altas y traslados?", "3+1", "Se suman los egresos por alta y por traslado.", " egresos"),
        ("=", "{F} ¿Cuántas camas ocupadas hay al cierre del día?", "16+5-(3+1)", "Se suman los ingresos a las camas ocupadas al inicio y se restan los egresos.", " camas"),
        ("=", "{F} ¿Cuántas camas disponibles hay al cierre del día?", "20-(16+5-(3+1))", "Se restan las camas ocupadas al cierre de las camas totales.", " camas"),
        ("=", "{F} ¿Qué porcentaje de ocupación hay al cierre del día?", "(16+5-(3+1))*100//20", "Se multiplican las camas ocupadas por 100 y se dividen entre las camas totales.", " %"),
        ("abc", "{F} Un técnico calcula 16 + 5 − 3 = 18 camas al cierre. ¿Qué error cometió?", "No restó el egreso por traslado", "No sumó los ingresos", "No consideró las camas totales", "Un traslado también es un egreso y libera una cama."),
        ("=", "{F} ¿Cuántos días de estadía suman las 4 personas dadas de alta en la semana?", "5+3+7+9", "Se suman las estadías de cada persona.", " días"),
        ("=", "{F} ¿Cuál fue la estadía promedio de esas 4 personas?", "(5+3+7+9)//4", "Se divide la suma de las estadías entre la cantidad de personas.", " días"),
        ("abc", "{F} ¿Qué estadía fue la más larga de la semana?", "9 días", "7 días", "5 días", "La estadía más larga fue de 9 días entre las cuatro personas."),
        ("=", "{F} Si al día siguiente hubiera 2 ingresos y 4 egresos, ¿cuántas camas ocupadas quedarían al cierre de ese día, partiendo del cierre del día anterior?", "(16+5-(3+1))+2-4", "Se parte de las camas del cierre anterior, se suman los ingresos y se restan los egresos.", " camas"),
        ("abc", "{F} La enfermera pide una cama para un ingreso urgente y el técnico, al revisar el censo, ve que quedan 3 disponibles. ¿Qué corresponde?", "Informar a la enfermera que hay camas disponibles según el censo y esperar su indicación", "Asignar él mismo la cama a la persona que llegó", "Decir que no hay camas sin revisar", "El técnico informa los datos del censo y la enfermera decide la asignación."),
        ("abc", "{F} El técnico se da cuenta de que anotó 6 ingresos en vez de 5. ¿Qué corresponde?", "Corregir con una línea, el valor correcto, hora y firma, y avisar a la enfermera", "Dejar el error, porque el total es parecido", "Borrar el dato y escribir el correcto", "Los errores de registro se corrigen con trazabilidad y se informan."),
        ("abc", "En Atención de Enfermería: ¿por qué el censo se registra con exactitud?", "Porque un error puede significar que no haya cama para quien la necesita", "Porque el censo reemplaza la ficha clínica", "Porque el paciente lo exige", "El censo organiza el uso de las camas; un error afecta la atención."),
    ],
    ctx=("abc", "{F} Una técnica no logra cuadrar el censo: según sus anotaciones hay 18 camas ocupadas, pero en la sala cuenta 17 personas. ¿Qué hace?", "Verifica sus anotaciones, informa la diferencia a la enfermera y no modifica el censo hasta aclararla", "Anota 17 sin avisar, para que coincida con lo que vio", "Anota 18 sin avisar, porque es lo que registró", "Una diferencia se verifica y se informa, sin ajustar a ojo el dato."),
    sc=[
        ("En Atención de Enfermería: ¿cómo se calcula el porcentaje de ocupación?", "Camas ocupadas × 100 ÷ camas totales", "Se mide sobre el total de camas."),
        ("¿Qué se resta al calcular las camas al cierre?", "Los egresos: altas y traslados", "Tanto un alta como un traslado liberan una cama."),
        ("¿Cómo se calcula la estadía promedio?", "Se suman las estadías y se divide por la cantidad de personas", "Es el promedio de los días de permanencia."),
    ],
    op=("Censo de ejemplo: «Servicio de 25 camas. Al inicio había 15 ocupadas; durante el día hubo 6 ingresos, 4 altas y 2 traslados. Estadías de las 3 personas dadas de alta en la mañana: 5, 7 y 9 días». "
        "Calcula: camas ocupadas y disponibles al cierre; el porcentaje de ocupación; la estadía promedio. Escribe cómo corregirías un error en el número de ingresos.",
        "Egresos: 4+2 = 6. Ocupadas al cierre: 15+6−6 = 15. Disponibles: 25−15 = 10. Ocupación: 15 × 100 ÷ 25 = 60 %. Estadía promedio: (5+7+9) ÷ 3 = 7 días. Corrección: línea sobre el dato, valor correcto, hora y firma, y aviso a la enfermera.",
        ["calcula 15 ocupadas y 10 disponibles", "calcula 60 %", "calcula 7 días", "describe la corrección con trazabilidad"],
        ["hoja con cuatro cálculos y la forma de corregir"],
        ["no restar los traslados", "dividir mal el porcentaje", "borrar el dato con corrector"],
        "Pregunta: «¿restaste las altas y los traslados?». Si no, pídele rehacer el cálculo."),
    reinforce="Con 12 camas ocupadas al inicio, 3 ingresos y 5 egresos, calcula las camas ocupadas al cierre.",
    extend="Explica con un ejemplo inventado cómo un error en el censo puede afectar a una persona que necesita una cama.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (comparar alternativas, de ejemplo). Lista de verificación de calidad de una nota de registro, ocho puntos: (1) fecha y hora; (2) identificación del paciente; (3) hechos observables; (4) valor con su unidad; (5) sin opiniones ni diagnósticos; (6) redacción clara; (7) firma; (8) sin abreviaturas no estandarizadas. "
     "Nota A: «Cama 6, 14:00, pulso 76 latidos por minuto, presión sistólica 118 mmHg, firma M. P. (técnica)»; no incluye la fecha. Nota B: «La de la cama 6 parece nerviosa, debe estar mal de la presión, la vi rara»; no tiene hora, fecha, valores ni firma. "
     "Modos de registro: manual, 6 minutos por paciente; digital, 4 minutos por paciente más 10 minutos al iniciar y cerrar la sesión. Pacientes del turno: 12.")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos notas de registro y dos modos de registrar con criterios, a verificar la calidad con una lista y a decidir qué corrección proponer.",
    prior=["Conozco la ficha clínica, la privacidad y el censo.", "Sé calcular porcentajes y tiempos.", "Sé leer una lista de verificación."],
    explain=[
        "Comparar alternativas es ponerlas frente a los mismos criterios y ver cuál cumple mejor y por qué. Para una nota de registro se usa una lista de verificación: fecha y hora, identificación, hechos observables, valor con unidad, sin opiniones, redacción clara, firma y sin abreviaturas no estandarizadas. Cada punto cumplido suma, y la nota con más puntos es de mejor calidad.",
        "También se comparan los modos de registro. El manual no depende de equipos, pero puede tener letra difícil de leer y fichas expuestas. El digital deja constancia automática de quién entró y cuándo, pero exige una clave segura y cerrar la sesión. Ningún modo es mejor en todo: cada uno requiere sus reglas de privacidad. El tiempo también se compara con cuentas simples, sumando el tiempo por paciente y el de inicio y cierre.",
        "Verificar la calidad es revisar con la lista antes de dar por terminado un registro." + LIM,
    ],
    vocab=[("lista de verificación", "conjunto de puntos que se marcan como cumplidos o no"), ("registro manual", "registro escrito a mano en papel"), ("registro digital", "registro hecho en un sistema con clave personal"), ("hecho observable", "algo que se puede ver, oír o medir y que otro puede comprobar"), ("opinión", "juicio personal que no es un hecho comprobable"), ("calidad del registro", "grado en que una nota cumple los puntos de la lista")],
    worked=[
        ("Aplicar un punto de la lista", "Una nota de ejemplo dice: «El paciente de la cama 3 está insoportable». ¿Qué punto de la lista incumple?", ["La frase es un juicio personal.", "Incumple el punto 5: sin opiniones ni diagnósticos."], "El punto 5"),
        ("Comparar tiempos", "En otro servicio de ejemplo, el registro manual toma 5 minutos por paciente y hay 10 pacientes. ¿Cuántos minutos toma?", ["Se multiplican los minutos por paciente por la cantidad de pacientes.", "5 × 10 = 50."], "50 minutos")],
    mistakes=[("Elegir un modo de registro por ser «más moderno» sin revisar sus riesgos.", "Cada modo tiene riesgos de privacidad y de calidad que requieren reglas.", "Compara con criterios: tiempo, calidad, privacidad y trazabilidad."),
              ("Dar por buena una nota porque «se entiende lo que quiere decir».", "Si faltan hora, firma o valores, la nota no es confiable aunque se entienda.", "Verifica los ocho puntos antes de cerrarla.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un hecho observable?", "Algo que se puede ver, oír o medir y que otro puede comprobar", "Una impresión personal sobre el estado de ánimo", "Un diagnóstico escrito por el técnico", "Un hecho es comprobable; una impresión o un diagnóstico no lo son para el técnico."),
        ("abc", "{F} ¿Qué punto de la lista incumple la nota A?", "El punto 1: fecha y hora, porque no tiene fecha", "El punto 4: valor con unidad", "El punto 7: firma", "La nota A tiene hora, valores con unidad y firma, pero no incluye la fecha."),
        ("=", "{F} ¿Cuántos puntos de los 8 cumple la nota A?", "8-1", "La nota A solo incumple el punto 1; los otros siete se cumplen.", " puntos"),
        ("=", "{F} La nota B incumple los puntos 1, 3, 4, 5 y 7. ¿Cuántos puntos de los 8 cumple?", "8-5", "Se restan de los 8 puntos los 5 que incumple.", " puntos"),
        ("=", "{F} ¿Cuántos puntos más que la nota B cumple la nota A?", "(8-1)-(8-5)", "Se restan los puntos que cumple la nota B de los que cumple la nota A.", " puntos"),
        ("=", "{F} Si cada punto cumplido de la lista vale 5 puntos de calidad, ¿cuántos puntos de calidad suma la nota A?", "(8-1)*5", "Se multiplican los puntos cumplidos por el valor de cada uno.", " puntos de calidad"),
        ("abc", "{F} ¿Qué punto de la lista incumple la frase «parece nerviosa, debe estar mal de la presión» de la nota B?", "El punto 5: sin opiniones ni diagnósticos", "El punto 8: abreviaturas", "El punto 6: redacción clara", "La frase es una opinión y un diagnóstico que el técnico no debe escribir."),
        ("=", "{F} ¿Cuántos minutos toma registrar a los 12 pacientes en modo manual?", "12*6", "Se multiplican los minutos por paciente por la cantidad de pacientes.", " minutos"),
        ("=", "{F} ¿Cuántos minutos toma registrar a los 12 pacientes en modo digital, incluyendo los 10 minutos de inicio y cierre de sesión?", "12*4+10", "Se multiplican los minutos por paciente y se suman los de inicio y cierre.", " minutos"),
        ("=", "{F} ¿Cuántos minutos menos toma el modo digital que el manual?", "12*6-(12*4+10)", "Se resta el tiempo del modo digital del tiempo del modo manual.", " minutos"),
        ("abc", "{F} Un compañero dice: «El digital es mejor, porque es más rápido». ¿Qué corresponde responder?", "Que es más rápido, pero requiere clave segura, cerrar la sesión y reglas de privacidad", "Que sí, y por eso no necesita reglas", "Que no, porque tarda más siempre", "El tiempo no es el único criterio: ambos modos exigen privacidad y calidad."),
        ("abc", "{F} La enfermera pide a la técnica que corrija la nota B. ¿Qué corrección corresponde?", "Reescribir con hechos: hora, valores con unidad, firma, y sin opiniones, indicando la corrección con hora y firma", "Agregar más opiniones para explicar mejor", "Tapar la nota con corrector y escribir encima", "Una nota se corrige con hechos y con trazabilidad, sin borrar lo anterior."),
        ("abc", "{F} Un técnico escribió «presión alta, hay que avisar al doctor» en una nota. ¿Qué corresponde?", "Anotar el valor medido con su unidad y avisar a la enfermera, sin escribir el diagnóstico", "Dejar la nota, porque es útil", "Agregar la causa probable", "El técnico registra hechos y avisa; no diagnostica ni decide a quién avisar fuera de su cadena."),
    ],
    ctx=("abc", "{F} Al cerrar el turno, la técnica revisa sus notas con la lista y descubre que olvidó anotar la hora en tres de ellas. Nadie lo ha notado. ¿Qué hace?", "Las corrige con una línea y la hora real si la recuerda con certeza, las firma y avisa a la enfermera; si no recuerda, anota que no se registró la hora", "Inventa horas parecidas para completarlas", "Deja las notas como están y no dice nada", "Se corrige con trazabilidad y honestidad: no se inventan horas."),
    sc=[
        ("En Atención de Enfermería: ¿qué se compara en una lista de verificación?", "Cuántos puntos de calidad cumple una nota", "Cada punto cumplido de la lista suma calidad a la nota."),
        ("¿Qué es mejor, el registro manual o el digital?", "Ninguno es mejor en todo; ambos exigen reglas de privacidad", "Cada modo tiene ventajas y riesgos."),
        ("¿Qué haces si olvidaste anotar la hora?", "La corrijo con trazabilidad o informo que no se registró", "No se inventan datos: se corrige o se informa lo que falta."),
    ],
    op=("Notas de ejemplo: «Nota 1: 10:15, cama 4, pulso 72 latidos por minuto, firma R. T.; sin fecha. Nota 2: Cama 4 está bien, no hay nada que decir, firma R. T.». Modos de registro: manual, 6 minutos por paciente; digital, 3 minutos por paciente más 8 minutos de inicio y cierre; 10 pacientes. "
        "Usa la lista de la ficha. Escribe: qué puntos incumple cada nota; cuál es mejor y por qué; cuántos minutos toma cada modo y cuál es más rápido; y una condición de privacidad que exige cada modo.",
        "Nota 1 incumple el punto 1 (sin fecha); cumple 2, 3, 4, 5, 6, 7 y 8 (7 de 8). Nota 2 incumple 1, 3, 4 y 5 (no hay hechos ni valores ni hora; «está bien» es una opinión). La nota 1 es mejor. Manual: 6 × 10 = 60 minutos. Digital: 3 × 10 + 8 = 38 minutos, más rápido. Privacidad: en el manual, no dejar fichas a la vista; en el digital, clave personal y cerrar la sesión.",
        ["identifica los puntos incumplidos de cada nota", "elige la mejor con razón", "calcula 60 y 38 minutos", "indica una condición de privacidad por modo"],
        ["hoja con puntos incumplidos, una elección, dos cálculos y dos condiciones"],
        ["no ver que «está bien» es una opinión", "olvidar sumar los minutos de inicio y cierre", "decir que un modo no necesita reglas"],
        "Pregunta: «¿tu comparación dice por qué una nota es mejor, no solo cuál?». Si no, pídele agregar los puntos."),
    reinforce="Reescribe la nota B de la ficha con hechos, hora, valores con unidad y firma, sin opiniones.",
    extend="Explica con un ejemplo inventado por qué una nota con hora, valor y firma ayuda más al equipo que una con opiniones.",
)


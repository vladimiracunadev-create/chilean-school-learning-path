"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 11 (uso responsable de energía eléctrica)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _x(items):
    return [ex(*i) if isinstance(i, tuple) else i for i in items]


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": w[0], "problem": w[1], "steps": w[2], "answer": w[3]} for w in worked],
        mistakes=[{"wrong": m[0], "why": m[1], "fix": m[2]} for m in mistakes],
        tiers={"recovery": _x(rec), "understand": _x(und), "apply": _x(app), "reason": _x(rea), "challenge": _x(cha)},
        context=_x(context), selfcheck=_x(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )




OA11 = "CN05 OA 11"

# ---------------------------------------------------------------- OA 11
L(OA11, 1,
  materials="Este cuaderno y lápiz. Opcional: una lista de los artefactos eléctricos que usas en un día. No toques enchufes ni cables conectados.",
  use="Aprenderé por qué la energía eléctrica es importante en la vida cotidiana y a separar lo que observo de lo que supongo. Sirve para valorar la electricidad y usarla con cuidado.",
  prior=["Sé que los artefactos transforman la energía eléctrica en luz, calor, sonido o movimiento.", "Sé separar observaciones de interpretaciones."],
  explain=[
      "La energía eléctrica está presente en casi todo lo que hacemos. Ilumina las casas y las calles. Hace funcionar el refrigerador que conserva los alimentos, la radio, el televisor y los computadores. Carga los teléfonos, mueve ventiladores y bombas de agua y permite que funcionen los semáforos, los hospitales y las escuelas.",
      "Para ver cuán importante es, podemos observar qué pasa cuando falta. En un corte de luz las ampolletas se apagan, el refrigerador deja de enfriar y los aparatos conectados dejan de funcionar. Una observación es lo que se ve o se cuenta, como «durante 3 horas se apagaron 6 ampolletas». Una interpretación es lo que se supone, como «todos sufrieron mucho». Solo la observación es evidencia.",
      "La energía eléctrica se produce en centrales y llega a las casas por cables. Como tiene un costo y su producción puede afectar al ambiente, conviene usarla de manera responsable: encender solo lo necesario y por el tiempo necesario. En esta clase no manipulamos cables ni enchufes; trabajamos con registros escritos.",
  ],
  vocab=[("corte de luz", "momento en que se interrumpe el suministro eléctrico"), ("central eléctrica", "lugar donde se produce energía eléctrica"), ("uso responsable", "usar solo lo necesario y con cuidado"), ("artefacto", "aparato que funciona con energía"), ("registro", "lista ordenada de lo que se observó o contó")],
  worked=[
      ("Identificar la importancia", "Durante un corte de luz, el refrigerador deja de enfriar. ¿Qué actividad de la vida cotidiana se ve afectada?", ["El refrigerador conserva los alimentos.", "Sin energía no enfría.", "La conservación de alimentos se afecta."], "La conservación de los alimentos"),
      ("Observación o interpretación", "«Durante el corte se apagaron 6 ampolletas» y «Todos estaban de mal humor». ¿Cuál es observación?", ["Pregunto qué se contó.", "Las 6 ampolletas se cuentan.", "El humor es una suposición."], "La primera frase"),
  ],
  mistakes=[
      ("Pensar que la electricidad es gratis e infinita.", "Producirla tiene costos y efectos en el ambiente.", "Piensa en usarla de manera responsable."),
      ("Anotar «fue horrible» como observación del corte de luz.", "Es una opinión; no se puede contar.", "Anota lo que dejó de funcionar."),
  ],
  rec=[
      ("¿El refrigerador usa energía eléctrica?", "Sí", "La necesita para enfriar."),
      ("Cuando hay un corte de luz, ¿la ampolleta enciende o se apaga?", "Se apaga", "No recibe energía eléctrica."),
      ("Completa con «registro» o «adivinanza»: lo que se cuenta y se anota forma un ______.", "Registro", "Permite revisar los datos."),
  ],
  und=[
      ("Nombra dos servicios que dependen de la electricidad.", "Dos entre iluminación, refrigeración, hospitales, semáforos o escuelas", "Todos usan energía eléctrica."),
      ("¿Por qué conviene usar la electricidad de manera responsable?", "Porque producirla tiene costos y efectos en el ambiente", "Usar solo lo necesario ayuda."),
      ("Marca la observación: A) Durante el corte se apagaron 6 ampolletas. B) Fue el peor día del año.", "A", "A se cuenta; B es opinión."),
  ],
  app=[
      arith("Dato de ejemplo. En una casa se encienden 4 ampolletas en el living, 3 en la cocina y 2 en el pasillo. ¿Cuántas ampolletas hay encendidas en total?", "4+3+2", "Se suman las de cada lugar."),
      ("Lista de artefactos: televisor, refrigerador, ventilador, cargador. ¿Cuántos usan energía eléctrica?", "4", "Los cuatro necesitan electricidad."),
      ("Durante un corte de luz, una persona anota: no hay luz, el refrigerador no enfría y el teléfono no carga. ¿Cuántas observaciones anotó?", "3", "Son tres cosas que dejaron de funcionar."),
  ],
  rea=[
      ("Ema dice: «La electricidad no es importante porque yo puedo vivir sin ella un día». ¿Tiene razón? Responde Sí o No y explica con un ejemplo.", "No; por ejemplo, los hospitales y los refrigeradores dependen de ella", "Muchos servicios básicos la necesitan."),
      ("Un registro del corte dice: «Se apagaron 6 ampolletas y todos tuvieron miedo». ¿Qué parte es evidencia?", "Se apagaron 6 ampolletas", "El miedo es una interpretación."),
  ],
  cha=[
      ("Escribe una observación y una interpretación sobre un corte de luz de 2 horas.", "Observación: se apagaron las ampolletas durante 2 horas. Interpretación: fue aburrido", "La observación se cuenta; la interpretación es una suposición."),
      ("Explica por qué los hospitales necesitan energía eléctrica aunque haya cortes.", "Porque muchos equipos que cuidan la salud necesitan electricidad continua", "Por eso tienen sistemas de respaldo."),
  ],
  context=[("Dato de ejemplo. Una clase hizo una lista de 5 artefactos eléctricos de su escuela y 3 de su casa. ¿Cuántos artefactos listaron?", "8", "5 + 3 = 8.")],
  selfcheck=[("Nombra tres usos de la energía eléctrica.", "Tres entre iluminar, refrigerar, cargar aparatos, mover ventiladores o hacer funcionar semáforos", "Son usos de la vida cotidiana."), ("¿Qué pasa con el refrigerador en un corte de luz?", "Deja de enfriar", "Necesita energía eléctrica."), ("¿Una opinión es evidencia? Responde Sí o No.", "No", "Solo lo observado es evidencia.")],
  open_task=task("Con una persona de tu casa, anota en una tabla cinco artefactos eléctricos que usas en un día y para qué sirve cada uno. Después imagina un corte de luz de dos horas y escribe tres cosas que dejarían de funcionar. Agrega una observación y una interpretación sobre tu tabla. No toques enchufes ni cables conectados.", "Ampolleta: iluminar. Refrigerador: conservar alimentos. Televisor: informarse. Cargador: cargar el teléfono. Ventilador: refrescar. Sin luz: se apagan las ampolletas, el refrigerador deja de enfriar y el cargador no funciona. Observación: anoté 5 artefactos. Interpretación: no podría vivir sin electricidad.", ["cinco artefactos con uso", "tres cosas que dejan de funcionar", "observación e interpretación diferenciadas"], ["tabla", "frases"], ["tocar artefactos conectados", "anotar opiniones como datos"], "Pregunta qué artefacto sería más difícil de reemplazar y por qué."),
  reinforce="Escribe tres actividades de tu día que dependen de la electricidad.",
  extend="Explica por qué los semáforos necesitan electricidad para ordenar el tránsito.")

L(OA11, 2,
  materials="Este cuaderno y lápiz. Opcional: un registro de las horas en que se encienden las luces de tu casa durante tres días.",
  use="Aprenderé a plantear preguntas y predicciones sobre cuánta energía usa un artefacto. Sirve para decidir qué medidas de ahorro valen la pena.",
  prior=["Sé que los artefactos usan energía eléctrica.", "Sé que una predicción lleva una razón."],
  explain=[
      "La cantidad de energía eléctrica que usa un artefacto depende de dos cosas: su potencia y el tiempo que está encendido. La potencia se mide en vatios, con el símbolo W, y dice cuánta energía usa el artefacto cada hora que funciona. La energía consumida se calcula multiplicando la potencia por las horas: consumo (Wh) = potencia (W) × tiempo (h). Los valores de esta clase son de ejemplo.",
      "Por ejemplo, una ampolleta de 10 W encendida 5 horas consume 10 × 5 = 50 Wh. Si la apagamos 2 horas antes, consume 10 × 3 = 30 Wh, es decir, 20 Wh menos. Una pregunta comprobable es: «¿Cuántas horas al día están encendidas las ampolletas del living?». Una predicción es: «Si reducimos 2 horas el uso, ahorraremos 20 Wh por ampolleta, porque el tiempo baja».",
      "Un registro de varios días permite comprobar. Una sola medición puede no ser típica: un día de visitas se parece poco a un día normal. Y las predicciones se comparan con los registros, no con las opiniones.",
  ],
  vocab=[("potencia", "energía que usa un artefacto cada hora que funciona"), ("vatio (W)", "unidad con la que se mide la potencia"), ("consumo", "energía que se usa en un tiempo"), ("Wh", "vatio-hora, unidad de energía consumida"), ("ahorro", "energía que se deja de usar")],
  worked=[
      ("Calcular el consumo", "Una ampolleta de 10 W está encendida 5 horas. ¿Cuántos Wh consume?", ["Uso la fórmula potencia por tiempo.", "Multiplico 10 por 5.", "Escribo el resultado con su unidad."], "50 Wh"),
      ("Predicción con razón", "Si una ampolleta de 10 W se enciende 2 horas menos, ¿se ahorrará energía?", ["El consumo depende del tiempo.", "Menos horas son menos consumo.", "Calculo 10 por 2."], "Sí; se ahorran 20 Wh"),
  ],
  mistakes=[
      ("Pensar que una ampolleta apagada sigue consumiendo lo mismo.", "Cuando está apagada no consume energía.", "Calcula con las horas que está encendida."),
      ("Olvidar la unidad en el resultado.", "El número solo no dice qué se midió.", "Escribe Wh."),
  ],
  rec=[
      ("¿La potencia se mide en vatios o en metros?", "En vatios", "El símbolo es W."),
      ("Una ampolleta apagada, ¿consume energía o no?", "No", "Solo consume cuando está encendida."),
      ("Completa con «potencia» o «color»: el consumo depende del tiempo y de la ______.", "Potencia", "Son los dos datos de la fórmula."),
  ],
  und=[
      ("¿Con qué operación se calcula el consumo en Wh?", "Multiplicando la potencia por las horas", "Consumo = potencia × tiempo."),
      ("¿Por qué conviene registrar varios días?", "Porque un día puede no ser típico", "Los hábitos cambian de un día a otro."),
      ("¿Cuál pregunta se puede comprobar? A) ¿Cuántas horas se enciende la luz del living? B) ¿Qué luz es más linda?", "A", "Las horas se registran."),
  ],
  app=[
      arith("Una ampolleta de 10 W está encendida 4 horas. ¿Cuántos Wh consume?", "10*4", "Se multiplica la potencia por las horas.", " Wh"),
      arith("Un televisor de 100 W está encendido 3 horas. ¿Cuántos Wh consume (dato de ejemplo)?", "100*3", "Se multiplica la potencia por las horas.", " Wh"),
      arith("Una ampolleta de 10 W se enciende 6 horas y otro día 4 horas. ¿Cuántos Wh se ahorran el segundo día?", "10*6-10*4", "Se compara el consumo de los dos días.", " Wh"),
  ],
  rea=[
      ("Nico dice: «Una ampolleta de 10 W encendida 5 horas gasta más que un televisor de 100 W encendido 3 horas». ¿Es correcto? Responde Sí o No y explica.", "No; la ampolleta consume 50 Wh y el televisor 300 Wh", "Hay que multiplicar potencia por tiempo."),
      ("Lía registró un solo día con muchas visitas y concluyó que en su casa se usa mucha luz. ¿Qué problema tiene?", "Un solo día puede no ser típico", "Conviene registrar varios días."),
  ],
  cha=[
      ("Escribe una predicción con razón sobre qué pasa con el consumo si una ampolleta de 10 W se enciende 3 horas menos.", "Disminuye 30 Wh, porque baja el tiempo de uso", "10 × 3 = 30."),
      ("Escribe una pregunta comprobable sobre el uso de luz en tu casa, indicando qué registrarás.", "¿Cuántas horas están encendidas las ampolletas de mi dormitorio cada día durante tres días?", "Nombra lo que se registra y el período."),
  ],
  context=[("Dato de ejemplo. Un grupo registró cuántas horas estuvo encendida la luz del pasillo durante 3 días: 4, 5 y 6 horas. Si la ampolleta es de 10 W, ¿cuántos Wh consumió en los tres días?", "150", "4 + 5 + 6 = 15 horas, y 10 × 15 = 150 Wh.")],
  selfcheck=[("¿De qué dos cosas depende el consumo?", "De la potencia y del tiempo", "Ambos datos se multiplican."), ("¿Qué unidad tiene el consumo en esta clase?", "Wh", "Es la unidad vatio-hora."), ("¿Por qué registrar varios días?", "Porque un día puede no ser típico", "Así el dato es más confiable.")],
  open_task=task("Con una persona de tu casa, anota durante tres días cuántas horas está encendida una luz que uses (por ejemplo, la de tu pieza). Antes escribe tu predicción con razón sobre qué día tendrá más horas. Si la ampolleta fuera de 10 W, calcula los Wh de cada día. No toques las ampolletas encendidas ni los enchufes.", "Predicción: el domingo tendrá más horas porque estoy más en casa. Registro: viernes 4 h, sábado 5 h, domingo 6 h. Con 10 W: 40, 50 y 60 Wh. Se cumplió.", ["predicción con razón", "tres días de registro", "cálculo de Wh"], ["tabla con horas y Wh", "frase de conclusión"], ["olvidar la unidad", "registrar un solo día"], "Pregunta qué día se pareció más a su predicción y qué otros factores influyen."),
  reinforce="Calcula el consumo de una ampolleta de 10 W encendida 7 horas.",
  extend="Explica por qué dos artefactos de igual potencia pueden consumir distinto.")

L(OA11, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a usar un modelo del camino de la electricidad hasta la casa y a calcular consumos con una tabla. Sirve para entender de dónde viene la electricidad y cómo se mide.",
  prior=["Sé calcular consumo con potencia y horas.", "Sé que un modelo tiene límites."],
  explain=[
      "La energía eléctrica se produce en centrales. Hay centrales hidroeléctricas, que usan la fuerza del agua; solares, que usan la luz del Sol; eólicas, que usan el viento; y térmicas, que queman combustibles. Desde las centrales viaja por cables de líneas de transmisión hasta las ciudades y llega a las casas, donde un medidor registra la energía consumida en kWh. Un kWh equivale a 1.000 Wh.",
      "Un modelo simple de este camino es un esquema con flechas: central → líneas de transmisión → medidor de la casa → artefactos. Otro modelo es una tabla de consumo con cuatro columnas: artefacto, potencia en W, horas de uso y consumo en Wh. Las columnas ayudan a sumar el consumo de varios artefactos y a ver cuál pesa más.",
      "Los modelos tienen límites. El esquema no muestra todas las etapas ni las pérdidas de energía en el camino. La tabla usa valores de ejemplo y no incluye todos los artefactos de una casa. Un buen modelo dice qué muestra y qué deja fuera.",
  ],
  vocab=[("central hidroeléctrica", "central que usa la fuerza del agua para producir electricidad"), ("central solar", "central que usa la luz del Sol"), ("central eólica", "central que usa el viento"), ("medidor", "aparato que registra la energía consumida en una casa"), ("kWh", "kilovatio-hora, igual a 1.000 Wh")],
  worked=[
      ("Leer el esquema", "Esquema: central → líneas de transmisión → medidor → artefactos. ¿Qué viene justo después de las líneas de transmisión?", ["Sigo las flechas.", "Después de las líneas viene el medidor.", "Escribo el nombre."], "El medidor de la casa"),
      ("Completar la tabla", "Una tabla muestra: ampolleta, 10 W, 5 horas. ¿Cuántos Wh consume?", ["Multiplico 10 por 5.", "Obtengo 50.", "Escribo la unidad."], "50 Wh"),
  ],
  mistakes=[
      ("Pensar que la electricidad se produce en el medidor de la casa.", "El medidor solo registra el consumo.", "Recuerda: central, líneas y casa."),
      ("Sumar potencia y horas en vez de multiplicar.", "El consumo es el producto de ambos.", "Multiplica."),
  ],
  rec=[
      ("¿La central eólica usa el viento o el agua?", "El viento", "La hidroeléctrica usa el agua."),
      ("¿El medidor registra el consumo o produce la energía?", "Registra el consumo", "No produce electricidad."),
      ("Completa con «1.000» o «10»: 1 kWh equivale a ______ Wh.", "1.000", "El prefijo kilo significa mil."),
  ],
  und=[
      ("¿Qué usa una central solar para producir electricidad?", "La luz del Sol", "Es la fuente de energía de esa central."),
      ("¿Para qué sirve una tabla de consumo?", "Para ordenar el consumo de varios artefactos", "Permite sumar y comparar."),
      ("¿Qué no muestra el esquema del camino de la electricidad? A) Las pérdidas de energía. B) El medidor.", "A", "El esquema está simplificado."),
  ],
  app=[
      arith("Tabla de ejemplo. Ampolleta 10 W por 5 horas; ventilador 40 W por 3 horas. ¿Cuántos Wh consumen entre los dos?", "10*5+40*3", "Se calcula cada consumo y se suman.", " Wh"),
      arith("Una casa consume 3.000 Wh en un día. ¿Cuántos kWh son? (1 kWh = 1.000 Wh)", "3000//1000", "Se divide entre 1.000.", " kWh"),
      ("El televisor de la tabla consume 300 Wh y la ampolleta 50 Wh. ¿Cuál consume más?", "El televisor", "300 es mayor que 50."),
  ],
  rea=[
      ("Teo dice que si el esquema no muestra las pérdidas, entonces no hay pérdidas. ¿Tiene razón? Responde Sí o No y explica.", "No; el esquema simplifica y no las muestra", "Todo modelo deja cosas fuera."),
      ("Una tabla de consumo no incluye el refrigerador. ¿Qué límite tiene?", "No muestra todo el consumo de la casa", "Faltan artefactos que también consumen."),
  ],
  cha=[
      ("Escribe dos límites del esquema central → líneas → medidor → artefactos.", "No muestra las pérdidas de energía y no muestra todas las etapas", "Un esquema simplifica."),
      arith("Dato de ejemplo. Una casa consume 150 Wh con las luces, 300 Wh con el televisor y 200 Wh con otros artefactos. ¿Cuántos Wh consumen en total?", "150+300+200", "Se suman los tres consumos.", " Wh"),
  ],
  context=[("Dato de ejemplo. Un curso hizo la tabla de consumo de 4 artefactos y cada uno tuvo 3 datos (potencia, horas y consumo). ¿Cuántos datos anotaron?", "12", "4 × 3 = 12.")],
  selfcheck=[("Nombra dos tipos de centrales eléctricas.", "Dos entre hidroeléctrica, solar, eólica o térmica", "Usan fuentes distintas."), ("¿Qué registra el medidor?", "La energía consumida", "Se expresa en kWh."), ("¿Qué límite tiene una tabla de consumo?", "Solo incluye los artefactos anotados", "No muestra el consumo total de la casa.")],
  open_task=task("Haz una tabla de consumo con cuatro artefactos de tu casa. Para cada uno escribe una potencia de ejemplo (puedes usar: ampolleta 10 W, ventilador 40 W, televisor 100 W, cargador 5 W), las horas que lo usas al día y calcula los Wh. Suma el total, di si es más o menos de 1.000 Wh (1 kWh) y escribe dos límites de tu tabla. No toques enchufes ni artefactos conectados.", "Ampolleta 10 W × 5 h = 50 Wh; ventilador 40 W × 3 h = 120 Wh; televisor 100 W × 2 h = 200 Wh; cargador 5 W × 4 h = 20 Wh. Total 390 Wh, que es menos de 1 kWh. Límites: potencias de ejemplo y faltan otros artefactos.", ["cuatro artefactos con cálculo", "total y comparación con 1 kWh", "dos límites"], ["tabla", "cálculos y frases"], ["sumar en vez de multiplicar", "no escribir límites"], "Pregunta qué artefacto pesa más en el total y por qué."),
  reinforce="Dibuja el camino de la electricidad desde una central hasta una ampolleta de tu casa.",
  extend="Explica por qué una central solar no produce electricidad de noche.")

L(OA11, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar medidas de ahorro de energía con un criterio común y a proponer un plan de uso responsable. Sirve para decidir qué medida ahorra más y es segura.",
  prior=["Sé calcular el consumo con potencia y horas.", "Sé que para comparar uso un mismo criterio."],
  explain=[
      "Para comparar medidas de ahorro usamos un criterio común: cuántos Wh se ahorran por día. Imagina que se cambia una ampolleta de 60 W por una LED de 10 W, encendida 5 horas. El consumo baja de 60 × 5 = 300 Wh a 10 × 5 = 50 Wh. El ahorro es de 250 Wh al día. Si otra medida apaga un televisor de 100 W durante 2 horas, ahorra 100 × 2 = 200 Wh. Los valores son de ejemplo.",
      "Otras medidas de uso responsable son apagar las luces de una pieza vacía, aprovechar la luz del día, desenchufar los cargadores cuando no se usan y mantener cerradas las puertas del refrigerador. También es importante no conectar demasiados artefactos a un mismo alargador, porque puede calentarse y ser peligroso. Los cambios de ampolletas o enchufes los hace una persona adulta.",
      "Una buena comparación escribe la medida, el cálculo y la conclusión, usando el mismo criterio para todas. También debe decir la limitación: los números son de ejemplo y las horas reales cambian en cada casa. Por eso se propone un plan, se prueba y se revisa.",
  ],
  vocab=[("medida de ahorro", "acción para usar menos energía"), ("criterio", "característica que se mira igual en todos los casos"), ("alargador", "cable que prolonga un enchufe"), ("sobrecarga", "conectar más artefactos de los que el enchufe soporta"), ("plan", "conjunto de acciones para lograr algo")],
  worked=[
      ("Calcular un ahorro", "Cambiar una ampolleta de 60 W por una LED de 10 W, encendida 5 horas. ¿Cuántos Wh se ahorran al día?", ["Antes: 60 × 5 = 300 Wh.", "Después: 10 × 5 = 50 Wh.", "Resto: 300 − 50."], "250 Wh al día"),
      ("Comparar dos medidas", "Medida A ahorra 250 Wh. Medida B ahorra 200 Wh. ¿Cuál ahorra más?", ["Comparo los números.", "250 es mayor que 200.", "La medida A ahorra más."], "La medida A"),
  ],
  mistakes=[
      ("Comparar una medida en Wh y otra en horas.", "No tienen el mismo criterio.", "Calcula ambas en Wh."),
      ("Conectar muchos artefactos en un solo alargador.", "Puede calentarse y ser peligroso.", "Reparte los artefactos y no sobrecargues."),
  ],
  rec=[
      ("¿Qué criterio se usa para comparar medidas en esta clase: Wh ahorrados o color?", "Wh ahorrados", "Es el mismo para todas las medidas."),
      ("¿Apagar la luz de una pieza vacía ahorra energía?", "Sí", "La ampolleta apagada no consume."),
      ("Completa con «una persona adulta» o «un niño»: los cambios de ampolletas o enchufes los hace ______.", "Una persona adulta", "Es lo más seguro."),
  ],
  und=[
      ("¿Por qué no se deben conectar muchos artefactos a un alargador?", "Porque puede calentarse y ser peligroso", "El alargador se sobrecarga."),
      ("¿Qué hace más pequeño el consumo de una ampolleta: bajar la potencia o bajar las horas?", "Ambas", "El consumo es potencia por tiempo."),
      ("¿Qué comparación es justa? A) Wh ahorrados de cada medida. B) Wh de una y horas de otra.", "A", "En A se usa el mismo criterio."),
  ],
  app=[
      arith("Cambiar una ampolleta de 60 W por una LED de 10 W durante 5 horas. ¿Cuántos Wh se ahorran al día?", "60*5-10*5", "Se resta el consumo nuevo al antiguo.", " Wh"),
      arith("Apagar un televisor de 100 W durante 2 horas al día. ¿Cuántos Wh se ahorran?", "100*2", "Se multiplica la potencia por las horas ahorradas.", " Wh"),
      arith("Apagar una luz de 10 W durante 3 horas al día. ¿Cuántos Wh se ahorran?", "10*3", "Se multiplica la potencia por las horas ahorradas.", " Wh"),
  ],
  rea=[
      ("Ordena de mayor a menor ahorro estas tres medidas de ejemplo: LED (250 Wh), apagar la luz de una pieza vacía (30 Wh), apagar el televisor 2 horas (200 Wh). Escribe el orden.", "LED, televisor, luz de la pieza", "250 > 200 > 30."),
      ("Un compañero dice que la medida que más ahorra siempre es la mejor para todas las casas. ¿Qué respondes?", "Depende de los artefactos y horas de cada casa", "Los datos de ejemplo no valen para todas."),
  ],
  cha=[
      ("Escribe una conclusión con los datos de ejemplo: LED ahorra 250 Wh y apagar el televisor 2 horas ahorra 200 Wh.", "En estos datos de ejemplo, cambiar a LED ahorra 50 Wh más que apagar el televisor", "Compara con el mismo criterio."),
      ("Propón un plan de tres medidas de ahorro seguro para tu casa y di una razón para cada una.", "Apagar luces sin uso, aprovechar la luz del día y desenchufar cargadores; así se reduce el tiempo de consumo", "Cada medida reduce el tiempo o la potencia usada."),
  ],
  context=[("Dato de ejemplo. Una casa ahorró 250 Wh por día cambiando una ampolleta. ¿Cuántos Wh ahorró en 4 días?", "1.000", "250 × 4 = 1.000.")],
  selfcheck=[("¿Qué criterio se usa para comparar medidas?", "Los Wh ahorrados por día", "Es el mismo para todas."), ("Nombra una medida de uso responsable.", "Apagar las luces sin uso o aprovechar la luz del día", "Reduce el tiempo de consumo."), ("¿Por qué no sobrecargar un alargador?", "Porque puede calentarse y ser peligroso", "Es un riesgo de seguridad.")],
  open_task=task("Escribe un plan de tres medidas de ahorro de energía eléctrica para tu casa o tu sala. Para cada una calcula con datos de ejemplo cuántos Wh ahorras al día (por ejemplo, apagar una luz de 10 W durante 3 horas). Compara las tres y escribe una conclusión y una limitación. Incluye una medida de seguridad con los enchufes.", "1) Apagar la luz de 10 W 3 horas menos: 30 Wh. 2) Apagar un televisor de 100 W 1 hora menos: 100 Wh. 3) Apagar un ventilador de 40 W 2 horas menos: 80 Wh. Conclusión: la medida 2 ahorra más. Limitación: valores de ejemplo. Seguridad: no sobrecargar el alargador.", ["tres medidas con cálculo", "comparación con el mismo criterio", "limitación y medida de seguridad"], ["tabla", "frases"], ["comparar con criterios distintos", "manipular enchufes sin ayuda adulta"], "Pregunta cuál medida es más fácil de mantener y qué haría si el ahorro fuera menor al esperado."),
  reinforce="Calcula cuántos Wh ahorras al apagar una ampolleta de 10 W durante 6 horas.",
  extend="Explica por qué el ahorro de energía también ayuda al ambiente.")

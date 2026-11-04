"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 05 (factores que regulan poblaciones) y OA 06 (ciclos biogeoquímicos, flujo de energía y contaminantes)."""
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


OA5 = "CN1M OA 05"
OA6 = "CN1M OA 06"

# ---------------------------------------------------------------- OA 05

L(OA5, 1,
  materials="Este cuaderno y lápiz. Todos los datos de poblaciones están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé qué hace crecer o disminuir una población y cómo se escribe una pregunta investigable sobre ello. Sirve para predecir cambios en un ecosistema.",
  prior=["Sé qué es una población y qué es la densidad.", "Sé que una pregunta investigable se contesta con datos."],
  explain=[
      "El tamaño de una población cambia por cuatro procesos. Aumenta con la natalidad (nacimientos) y la inmigración (individuos que llegan desde otro lugar). Disminuye con la mortalidad (muertes) y la emigración (individuos que se van). Se puede escribir: tamaño final = tamaño inicial + nacimientos + inmigrantes − muertes − emigrantes.",
      "Estos procesos dependen de factores del ambiente. La disponibilidad de alimento y de agua limita cuántos individuos pueden vivir. La propagación de enfermedades aumenta la mortalidad, sobre todo cuando hay muchos individuos juntos. Las sequías reducen el pasto y el agua. Un factor limitante es aquel que impide que la población siga creciendo.",
      "Una pregunta investigable sobre una población indica qué factor se estudia y qué se mide. «¿Cuántos nacimientos hubo por año en una colonia de aves cuando había más alimento?» se contesta con registros. «¿Es justo que haya sequías?» no se contesta con datos.",
  ],
  vocab=[("natalidad", "número de nacimientos en un tiempo"), ("mortalidad", "número de muertes en un tiempo"), ("inmigración", "llegada de individuos a una población"), ("emigración", "salida de individuos de una población"), ("factor limitante", "factor que impide que la población siga creciendo")],
  worked=[
      ("Calcular el tamaño final", "Una colonia de aves tiene 200 individuos. En un año nacen 50, mueren 30, llegan 10 y se van 5. ¿Cuál es el tamaño final?", ["Sumo lo que aumenta: 200 + 50 + 10 = 260.", "Resto lo que disminuye: 260 − 30 − 5 = 225."], "225 aves"),
      ("Reconocer un factor", "Tras una sequía quedan pocas plantas y los herbívoros emigran. ¿Qué factor actuó?", ["La sequía redujo el alimento.", "La falta de alimento hizo que los individuos se fueran."], "La disponibilidad de alimento"),
  ],
  mistakes=[
      ("Sumar las muertes en vez de restarlas.", "Las muertes disminuyen la población.", "Marca con + lo que aumenta y con − lo que disminuye."),
      ("Pensar que una población crece sin límite si hay hembras y machos.", "El alimento, el agua y la enfermedad limitan el crecimiento.", "Pregunta qué factor limitante actúa."),
  ],
  rec=[
      ("¿Qué proceso aumenta una población por llegada de individuos de otro lugar?", "La inmigración", "Los inmigrantes llegan y suman individuos."),
      ("Completa: la salida de individuos de una población se llama ______ (emigración o natalidad).", "Emigración", "Los que se van disminuyen la población."),
      ("Verdadero o falso: la mortalidad disminuye el tamaño de una población.", "Verdadero", "Las muertes restan individuos."),
  ],
  und=[
      ("¿Cuál de estos procesos aumenta el tamaño de una población? A) La natalidad; B) La emigración.", "A", "Los nacimientos suman individuos."),
      ("¿Por qué una enfermedad se propaga más fácil cuando hay muchos individuos juntos? A) Porque hay más contactos entre individuos; B) Porque los individuos son más fuertes.", "A", "El contagio depende de los contactos."),
      ("¿Qué es un factor limitante?", "Un factor que impide que la población siga creciendo", "Puede ser el alimento, el agua o una enfermedad."),
  ],
  app=[
      arith("Una población de ejemplo de guanacos tiene 120 individuos. En un año nacen 30 y mueren 18. ¿Cuántos individuos hay al final, sin migración?", "120+30-18", "Se suman los nacimientos y se restan las muertes."),
      arith("Una colonia de ejemplo de 80 lobos marinos recibe 12 inmigrantes y pierde 7 por emigración, sin nacimientos ni muertes. ¿Cuántos hay al final?", "80+12-7", "Se suma lo que llega y se resta lo que se va."),
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos ratones hay por hectárea en un año de sequía y en otro con lluvia?; B) ¿Es triste que haya menos ratones?", "A", "La primera se contesta contando; la segunda es de opinión."),
  ],
  rea=[
      ("Un compañero dice: «Si hay más nacimientos que muertes, la población crece siempre». ¿Qué falta considerar? A) La emigración y la inmigración también cambian el tamaño; B) Nada, siempre es así.", "A", "El resultado depende de los cuatro procesos."),
      ("En un lago de ejemplo hay muchos peces y se detecta una enfermedad. ¿Por qué esta enfermedad se propaga más rápido que en un lago con pocos peces? A) Porque la densidad es alta y hay más contactos; B) Porque los peces comen más.", "A", "Más individuos juntos facilitan el contagio."),
  ],
  cha=[
      ("Una población de 500 ratones de ejemplo cambió así en un año: nacieron 220, murieron 340, llegaron 20 y se fueron 60. ¿Cuántos ratones quedaron?", "340", "500 más 220 más 20 menos 340 menos 60 da 340."),
      ("Un estudio registra la misma cantidad de nacimientos en dos años, pero en uno hubo sequía. ¿Qué dato falta medir para explicar la diferencia de tamaño final? A) La mortalidad y la emigración en cada año; B) El color de los individuos.", "A", "Los nacimientos iguales no bastan: hay que ver lo que resta."),
  ],
  context=[arith("En una reserva de ejemplo, el registro anual muestra 45 nacimientos, 22 muertes y 3 emigrantes. Si había 200 animales, ¿cuántos hay al final del año?", "200+45-22-3", "Se suman los nacimientos y se restan muertes y emigrantes.")],
  selfcheck=[("¿Cuáles son los cuatro procesos que cambian el tamaño de una población?", "Natalidad, mortalidad, inmigración y emigración", "Dos suman y dos restan."),
             ("Da un ejemplo de factor que aumente la mortalidad.", "Una enfermedad o una sequía", "Reducen la supervivencia."),
             ("¿Qué indica una pregunta investigable?", "Qué factor se estudia y qué se mide", "Se contesta con datos.")],
  open_task=task("Lee esta situación de ejemplo: una población de 300 liebres tuvo en un año 90 nacimientos, 120 muertes por una enfermedad, 10 inmigrantes y 20 emigrantes. Calcula el tamaño final, indica qué proceso tuvo más peso en la disminución y escribe una pregunta investigable sobre el factor que lo explica.", "Tamaño final: 300 + 90 + 10 − 120 − 20 = 260. La mortalidad (120) pesó más. Pregunta: «¿Cuántas liebres murieron por semana mientras se propagaba la enfermedad?»", ["calcula 260", "identifica la mortalidad", "la pregunta indica qué se mide"], ["cálculo, proceso y pregunta"], ["restar los nacimientos", "preguntar por una opinión"], "Pregunta qué cambiaría si la enfermedad se detuviera a la mitad del año."),
  reinforce="Escribe la ecuación del tamaño final de una población con los cuatro procesos.",
  extend="Explica por qué un factor como la sequía actúa aunque la población sea pequeña.")

L(OA5, 2,
  materials="Este cuaderno, lápiz y regla. Las tablas de crecimiento están escritas en los ejercicios y son de ejemplo.",
  use="Aprenderé a leer una tabla de crecimiento de población y a reconocer la capacidad de carga. Sirve para interpretar datos y representarlos.",
  prior=["Sé qué factores cambian el tamaño de una población.", "Sé leer tablas y comparar valores."],
  explain=[
      "Cuando hay abundante alimento y espacio, una población puede crecer rápido: cada año duplica su tamaño, por ejemplo. A este patrón se le llama crecimiento exponencial. En una tabla se ve porque los aumentos son cada vez mayores.",
      "Pero ningún ambiente tiene recursos infinitos. Cuando la población se acerca a lo que el ambiente puede sostener, el crecimiento se frena y el tamaño se estabiliza. Ese valor máximo se llama capacidad de carga. Cuando se grafica, se ve una curva que sube y luego se aplana.",
      "Para interpretar datos, observa las diferencias de un periodo al siguiente. Si la diferencia disminuye hasta ser cero, la población llegó a la capacidad de carga. Si baja bruscamente, puede haber actuado un factor como una enfermedad o una sequía. Una tabla muestra los valores; un gráfico de líneas muestra la tendencia.",
  ],
  vocab=[("crecimiento exponencial", "aumento en que cada periodo se suma más que en el anterior"), ("capacidad de carga", "tamaño máximo de población que el ambiente puede sostener"), ("tendencia", "dirección en que cambian los datos"), ("diferencia", "resultado de restar dos valores"), ("estabilizarse", "dejar de cambiar y quedar casi constante")],
  worked=[
      ("Leer la capacidad de carga", "Tabla de ejemplo: año 1, 20; año 2, 40; año 3, 80; año 4, 140; año 5, 180; año 6, 190; año 7, 190. ¿Cuál parece ser la capacidad de carga?", ["Busco el valor donde la población deja de cambiar.", "Se mantiene en 190 en los años 6 y 7."], "190 individuos"),
      ("Calcular una diferencia", "En la misma tabla, ¿cuánto creció la población entre el año 3 y el año 4?", ["Resto el valor del año 3 al del año 4.", "140 menos 80 es 60."], "60 individuos"),
  ],
  mistakes=[
      ("Pensar que la población seguirá duplicándose siempre.", "El alimento y el espacio son limitados.", "Busca el punto donde la curva se aplana."),
      ("Confundir el valor más alto de un año con la capacidad de carga.", "Un máximo puntual puede ser pasajero; la capacidad de carga es el valor al que tiende la población.", "Revisa varios años seguidos."),
  ],
  rec=[
      ("¿Cómo se llama el tamaño máximo de población que un ambiente puede sostener?", "Capacidad de carga", "Es el límite que imponen los recursos."),
      ("Completa: cuando una población se acerca a la capacidad de carga, el crecimiento ______ (se frena o se acelera).", "Se frena", "Los recursos escasean."),
      ("Verdadero o falso: el crecimiento exponencial agrega siempre la misma cantidad cada año.", "Falso", "Agrega cantidades cada vez mayores."),
  ],
  und=[
      ("¿Qué forma tiene la curva de crecimiento hasta llegar a la capacidad de carga? A) Sube y luego se aplana; B) Baja y luego sube.", "A", "El crecimiento se frena al agotarse los recursos."),
      ("¿Por qué una población no puede crecer sin límite? A) Porque el alimento y el espacio son limitados; B) Porque los individuos dejan de nacer por voluntad.", "A", "Los recursos fijan un máximo."),
      ("Si la diferencia entre dos años seguidos es cero, ¿qué está ocurriendo?", "La población se estabilizó", "No cambia entre los dos años."),
  ],
  app=[
      ("Tabla de ejemplo: año 1, 10; año 2, 20; año 3, 40; año 4, 80; año 5, 150; año 6, 210; año 7, 230; año 8, 230. ¿Cuál es la capacidad de carga aproximada?", "230", "Es el valor que se mantiene en los años 7 y 8."),
      arith("Con la misma tabla de ejemplo (año 4, 80; año 5, 150), ¿cuánto creció la población entre el año 4 y el año 5?", "150-80", "Se resta el valor del año 4 al del año 5."),
      ("Con la misma tabla (año 1, 10; año 2, 20; año 3, 40; año 4, 80), ¿qué patrón sigue el crecimiento en esos cuatro años? A) Duplica cada año; B) Aumenta siempre 10.", "A", "Cada valor es el doble del anterior."),
  ],
  rea=[
      ("Tabla de ejemplo: año 1, 100; año 2, 180; año 3, 260; año 4, 120; año 5, 160. Un estudiante dice que la capacidad de carga es 260. ¿Cuál es la crítica? A) El 260 bajó a 120 al año siguiente, por lo que fue un máximo pasajero; B) El 260 es un número demasiado pequeño.", "A", "La capacidad de carga es un valor sostenido, no un máximo puntual."),
      ("Una tabla de ejemplo muestra que la población baja de 300 a 150 en un año de sequía. ¿Cómo se identifica ese cambio en un gráfico? A) Con una caída brusca de la línea; B) Con una línea recta y horizontal.", "A", "Una caída rápida muestra un factor que actuó."),
  ],
  cha=[
      arith("Dos poblaciones de ejemplo parten con 50 individuos. La A duplica su tamaño cada año durante 3 años. La B suma 50 individuos cada año durante 3 años. ¿Cuántos individuos más tiene A que B al final?", "50*2*2*2-(50+50*3)", "A llega a 400 y B llega a 200; se restan ambos valores."),
      ("Un gráfico de ejemplo muestra una población que llegó a la capacidad de carga de 400 y luego una sequía la redujo a 250. ¿En cuánto se redujo?", "150", "400 menos 250 es 150."),
  ],
  context=[arith("En un lago de ejemplo, una población de peces creció de 60 a 90 en un año, y de 90 a 120 al siguiente. ¿Cuánto creció en los dos años?", "120-60", "Se resta el valor inicial al final.")],
  selfcheck=[("¿Qué es la capacidad de carga?", "El tamaño máximo de población que el ambiente puede sostener", "La imponen los recursos."), ("¿Cómo se ve en un gráfico?", "Una curva que sube y luego se aplana", "El crecimiento se frena."), ("¿Qué muestra una caída brusca en la curva?", "Que actuó un factor como una enfermedad o una sequía", "La población disminuye rápido.")],
  open_task=task("Con esta tabla de ejemplo, haz un gráfico de líneas y escribe una conclusión de dos oraciones. Tabla: año 1, 25; año 2, 50; año 3, 100; año 4, 180; año 5, 240; año 6, 270; año 7, 280; año 8, 280.", "Gráfico con el año en el eje horizontal y el tamaño en el vertical. Conclusión: la población creció rápido hasta el año 4 y luego se frenó. Se estabilizó en 280, que sería su capacidad de carga.", ["gráfico con ejes rotulados", "cita al menos dos datos", "identifica la capacidad de carga"], ["gráfico y conclusión"], ["no rotular ejes", "confundir el máximo con una tendencia"], "Pregunta qué factor podría explicar el valor de 280."),
  reinforce="Dibuja la curva de crecimiento de una población que llega a la capacidad de carga.",
  extend="Explica por qué la capacidad de carga puede cambiar entre un año lluvioso y uno seco.")

L(OA5, 3,
  materials="Este cuaderno y lápiz. Los factores y sus ejemplos están escritos en los ejercicios.",
  use="Aprenderé a clasificar los factores que regulan una población (dependientes e independientes de la densidad) y a usar un modelo de balance. Sirve para predecir efectos de una enfermedad, la falta de alimento o una sequía.",
  prior=["Sé la ecuación del tamaño de una población.", "Sé qué es la densidad."],
  explain=[
      "Los factores que regulan una población se clasifican según su relación con la densidad. Un factor dependiente de la densidad actúa más fuerte cuando hay más individuos por área: la competencia por alimento, la propagación de enfermedades y la depredación. Un factor independiente de la densidad actúa igual sin importar cuántos individuos hay: una sequía extrema, un incendio o una erupción volcánica.",
      "Un modelo de regulación usa el balance de la clase anterior y agrega el factor. Por ejemplo, una enfermedad aumenta la mortalidad; la falta de alimento aumenta la emigración y baja la natalidad; una sequía aumenta la mortalidad de toda la población. Con el modelo puedes predecir, pero hay que comprobar con datos.",
      "Todo modelo tiene límites: simplifica el ambiente y supone que los factores actúan por separado, aunque en la naturaleza actúan juntos. Por eso las predicciones son estimaciones. Un buen modelo se contrasta con observaciones y se ajusta.",
  ],
  vocab=[("factor dependiente de la densidad", "actúa más cuando hay más individuos por área"), ("factor independiente de la densidad", "actúa igual sin importar la densidad"), ("sobrepastoreo", "consumo excesivo del pasto por demasiados herbívoros"), ("regulación", "control del tamaño de una población"), ("predicción", "estimación de lo que ocurrirá")],
  worked=[
      ("Clasificar un factor", "Una sequía mata al 30 % de una población sin importar su densidad. ¿Qué tipo de factor es?", ["Pregunto si depende de cuántos individuos hay.", "La sequía actúa igual con pocos o muchos individuos."], "Independiente de la densidad"),
      ("Aplicar el modelo", "Una población de 400 individuos pierde 80 por enfermedad y 20 emigran por falta de alimento. ¿Cuántos quedan, sin nacimientos?", ["Resto los dos grupos que disminuyen.", "400 − 80 − 20 = 300."], "300 individuos"),
  ],
  mistakes=[
      ("Pensar que una enfermedad actúa igual en poblaciones densas y poco densas.", "En poblaciones densas hay más contactos y se contagia más.", "Pregunta si el factor cambia con la densidad."),
      ("Usar el modelo como si fuera exacto.", "Simplifica y supone factores separados.", "Presenta el resultado como estimación."),
  ],
  rec=[
      ("¿Cómo se llama el factor que actúa igual sin importar la densidad?", "Independiente de la densidad", "Ejemplos son la sequía extrema o un incendio."),
      ("Completa: la competencia por alimento es un factor ______ (dependiente o independiente) de la densidad.", "Dependiente", "Aumenta cuando hay más individuos."),
      ("Verdadero o falso: una erupción volcánica es un factor independiente de la densidad.", "Verdadero", "Afecta a la población sin importar su densidad."),
  ],
  und=[
      ("¿Por qué la propagación de una enfermedad es dependiente de la densidad? A) Porque hay más contactos cuando hay más individuos; B) Porque ocurre solo en verano.", "A", "El contagio depende del contacto."),
      ("¿Qué efecto puede tener la falta de alimento en una población? A) Menor natalidad y mayor emigración; B) Mayor natalidad.", "A", "Con menos alimento nacen menos individuos y algunos se van."),
      ("Un incendio mata la mitad de los individuos de una zona. ¿Qué tipo de factor es?", "Independiente de la densidad", "Afecta igual aunque haya pocos o muchos."),
  ],
  app=[
      arith("Una población de ejemplo tiene 500 individuos y una enfermedad mata al 10 % (50 individuos). ¿Cuántos quedan?", "500-50", "Se restan los individuos muertos."),
      arith("Una colonia de ejemplo de 240 aves pierde 60 por sequía y 40 por emigración. ¿Cuántas quedan?", "240-60-40", "Se restan los dos grupos que disminuyen."),
      ("En una isla de ejemplo, los conejos aumentan y comen casi todo el pasto. ¿Qué factor empezará a regular su población? A) La falta de alimento; B) La lluvia de otro continente.", "A", "El sobrepastoreo reduce el recurso."),
  ],
  rea=[
      ("Dos poblaciones de ejemplo tienen la misma enfermedad: A con 1.000 individuos en 10 km² y B con 100 individuos en 10 km². ¿En cuál se propagaría más rápido? A) La A, por la mayor densidad; B) La B, por la menor densidad.", "A", "Mayor densidad significa más contactos."),
      ("Un estudiante predice: «Si hay sequía, la población disminuirá lo mismo en cualquier ambiente». ¿Qué limitación tiene su predicción? A) Ambientes distintos tienen recursos distintos y reaccionan diferente; B) Las sequías no existen.", "A", "El modelo simplifica el ambiente."),
  ],
  cha=[
      ("Una población de ejemplo de 800 individuos sufre este año una enfermedad que mata al 20 %. ¿Cuántos individuos mueren?", "160", "El 20 % de 800 es 160."),
      ("Un modelo supone que los factores de regulación actúan separados. ¿Cuál es un ejemplo de que actúan juntos? A) Una sequía reduce el alimento y además aumenta la propagación de enfermedades por la concentración en pocos bebederos; B) La lluvia no afecta nada.", "A", "Los factores se combinan."),
  ],
  context=[arith("Un guardaparque de ejemplo estima que 12 de cada 100 animales enferman. En un grupo de 300, ¿cuántos enferman?", "300//100*12", "Hay 3 grupos de 100 y en cada uno enferman 12.")],
  selfcheck=[("¿Qué diferencia hay entre factor dependiente e independiente de la densidad?", "El dependiente actúa más cuando hay más individuos y el independiente actúa igual", "Cambia con la densidad o no."), ("Da un ejemplo de factor independiente.", "Una sequía extrema o un incendio", "Afecta sin importar la densidad."), ("¿Por qué las predicciones del modelo son estimaciones?", "Porque simplifica el ambiente y los factores actúan juntos", "Debe contrastarse con datos.")],
  open_task=task("Clasifica estos cuatro factores de ejemplo en dependientes o independientes de la densidad: (1) competencia por alimento; (2) incendio que quema un valle; (3) enfermedad contagiosa; (4) erupción volcánica. Después calcula una población: 600 individuos, 100 mueren por el factor 3 y 50 emigran por el factor 1. ¿Cuántos quedan?", "1 dependiente; 2 independiente; 3 dependiente; 4 independiente. Población: 600 − 100 − 50 = 450.", ["cuatro clasificaciones", "cálculo correcto", "justifica con la densidad"], ["clasificación y cálculo"], ["confundir el tipo de factor", "sumar en vez de restar"], "Pregunta qué cambiaría si el factor 3 no existiera."),
  reinforce="Escribe un factor dependiente y uno independiente de la densidad.",
  extend="Explica por qué las poblaciones densas son más vulnerables a ciertas enfermedades.")

L(OA5, 4,
  materials="Este cuaderno, lápiz y regla. Las tablas de datos son de ejemplo y están escritas en los ejercicios.",
  use="Aprenderé a relacionar variables, como lluvia, pasto y número de herbívoros, y a describir la relación con datos. Sirve para predecir el efecto de una sequía.",
  prior=["Sé qué es una variable y qué es un patrón.", "Sé que los factores regulan una población."],
  explain=[
      "En un ecosistema, las variables se encadenan. La cantidad de lluvia (variable 1) afecta la cantidad de pasto (variable 2), y el pasto afecta cuántos herbívoros se alimentan (variable 3). Una relación positiva ocurre cuando al aumentar una variable aumenta la otra. Una relación negativa ocurre cuando al aumentar una, disminuye la otra.",
      "Para estudiar la relación, se construye una tabla con pares de datos y se compara. Por ejemplo: con 100 mm de lluvia hay 200 g de pasto por m² y con 300 mm hay 600 g por m². La razón entre las dos variables es constante (2 g de pasto por mm de lluvia), por lo que la relación es proporcional en esa tabla de ejemplo.",
      "Una relación observada no demuestra por sí sola la causa. Hay que ver si otros factores cambian a la vez y si el mecanismo es razonable. Los datos sirven para predecir dentro del rango medido; fuera de ese rango, la predicción es dudosa.",
  ],
  vocab=[("relación positiva", "al aumentar una variable, aumenta la otra"), ("relación negativa", "al aumentar una variable, disminuye la otra"), ("razón", "cociente entre dos cantidades"), ("rango", "intervalo entre el valor mínimo y el máximo medidos"), ("extrapolar", "predecir fuera del rango medido")],
  worked=[
      ("Reconocer el tipo de relación", "Tabla de ejemplo: lluvia 100 mm, pasto 200 g; lluvia 200 mm, pasto 400 g; lluvia 300 mm, pasto 600 g. ¿Qué tipo de relación hay?", ["Al aumentar la lluvia, aumenta el pasto.", "Las dos variables cambian en el mismo sentido."], "Relación positiva"),
      ("Calcular la razón", "En la misma tabla, ¿cuántos gramos de pasto hay por cada mm de lluvia?", ["Divido el pasto entre la lluvia.", "200 dividido por 100 es 2."], "2 g por mm"),
  ],
  mistakes=[
      ("Decir que la relación es negativa porque una variable es «mala».", "La relación se define por el sentido del cambio de los datos.", "Compara cómo cambian los números."),
      ("Predecir valores muy fuera del rango medido.", "No se sabe si la relación se mantiene.", "Declara que la predicción es dudosa fuera del rango."),
  ],
  rec=[
      ("Si al aumentar una variable aumenta la otra, la relación es ______ (positiva o negativa).", "Positiva", "Las dos cambian en el mismo sentido."),
      ("¿Qué variable influye en la cantidad de pasto: la lluvia o el color del cielo?", "La lluvia", "El pasto necesita agua."),
      ("Verdadero o falso: una relación entre variables demuestra por sí sola una causa.", "Falso", "Hay que descartar otros factores."),
  ],
  und=[
      ("Si baja la lluvia y baja el pasto, ¿qué tipo de relación hay? A) Positiva; B) Negativa.", "A", "Las dos variables disminuyen juntas."),
      ("Más depredadores se asocian con menos presas. ¿Qué tipo de relación es? A) Negativa; B) Positiva.", "A", "Una sube y la otra baja."),
      ("¿Qué significa extrapolar?", "Predecir fuera del rango medido", "Es arriesgado porque no se sabe si la relación se mantiene."),
  ],
  app=[
      ("Tabla de ejemplo: lluvia 150 mm, pasto 300 g; lluvia 250 mm, pasto 500 g; lluvia 350 mm, pasto 700 g. ¿Cuántos gramos de pasto hay por mm de lluvia?", "2", "300 dividido por 150 es 2, y se mantiene en cada fila."),
      arith("Con una razón de 2 g de pasto por mm de lluvia, ¿cuántos gramos se esperan con 220 mm de lluvia (dentro del rango medido de 150 a 350 mm)?", "2*220", "Se multiplica la razón por la lluvia."),
      arith("Un guanaco de ejemplo necesita 3.000 g de pasto por día. Si el pasto de un campo es de 15.000 g, ¿para cuántos días alcanza para un guanaco?", "15000//3000", "Se divide el pasto disponible entre el consumo diario.", " días"),
  ],
  rea=[
      ("Un estudiante dice: «Con 350 mm hay 700 g; entonces con 1.000 mm habrá 2.000 g». ¿Cuál es la crítica? A) Está fuera del rango medido y no se sabe si la relación se mantiene; B) 1.000 mm no existe.", "A", "Extrapolar es dudoso."),
      ("Tabla de ejemplo: año 1, lluvia 300 mm, guanacos 80; año 2, lluvia 200 mm, guanacos 60; año 3, lluvia 100 mm, guanacos 40. ¿Qué conclusión es prudente? A) Los guanacos aumentan con la lluvia en estos tres años, pero faltan datos para asegurar la causa; B) La lluvia produce guanacos directamente.", "A", "La relación es positiva; la causa necesita el mecanismo del pasto."),
  ],
  cha=[
      ("Con los datos de ejemplo de 300, 200 y 100 mm de lluvia y 80, 60 y 40 guanacos, ¿cuántos guanacos más hay con 300 mm que con 100 mm?", "40", "80 menos 40 es 40."),
      ("En una tabla de ejemplo los gramos de pasto son 100, 200 y 300 con lluvias de 100, 200 y 300 mm. Se agrega un cuarto dato: lluvia 400 mm y pasto 250 g. ¿Qué podría explicarlo? A) Un factor distinto, como una plaga de insectos que comió pasto; B) Un error de la lluvia.", "A", "El dato rompe la proporcionalidad y exige buscar otro factor."),
  ],
  context=[arith("Un productor de ejemplo mide 5 parcelas de 4 m² con 600 g de pasto por m². ¿Cuántos gramos de pasto hay en total?", "5*4*600", "Se multiplican parcelas, metros cuadrados y gramos por metro cuadrado.")],
  selfcheck=[("¿Qué es una relación positiva?", "Cuando al aumentar una variable aumenta la otra", "Las dos cambian en el mismo sentido."), ("¿Qué es extrapolar?", "Predecir fuera del rango medido", "No hay datos que lo respalden."), ("¿Por qué una relación no prueba una causa?", "Porque otros factores pueden cambiar a la vez", "Hay que revisar el mecanismo.")],
  open_task=task("Con esta tabla de ejemplo, describe la relación en dos oraciones, calcula la razón de pasto por mm y predice el pasto con 200 mm de lluvia. Tabla: lluvia 100 mm, pasto 300 g; lluvia 300 mm, pasto 900 g; lluvia 500 mm, pasto 1.500 g. Declara un límite de tu predicción.", "Al aumentar la lluvia aumenta el pasto: relación positiva. Razón: 3 g por mm (300 dividido por 100). Con 200 mm se esperan 600 g. Límite: la tabla tiene solo tres datos y puede haber otros factores.", ["describe la relación", "calcula la razón y la predicción", "declara un límite"], ["descripción, cálculos y límite"], ["extrapolar sin advertir", "olvidar la unidad"], "Pregunta qué dato extra agregarías para confiar más en la predicción."),
  reinforce="Escribe una relación positiva y una negativa entre variables de un ecosistema.",
  extend="Explica por qué una sequía afecta a los depredadores aunque ellos no coman pasto.")

L(OA5, 5,
  materials="Este cuaderno y lápiz. Los casos de cascadas de efectos están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé a explicar los mecanismos con que un cambio en una población afecta a todo el ecosistema (efecto en cascada). Sirve para predecir consecuencias de una enfermedad o una sequía.",
  prior=["Sé qué factores regulan poblaciones.", "Sé leer redes tróficas."],
  explain=[
      "Un cambio en una población puede afectar a muchas otras. A esto se le llama efecto en cascada. Si una enfermedad reduce a los herbívoros, el pasto crece más, pero los depredadores de esos herbívoros tienen menos alimento y disminuyen. Si desaparece un depredador, los herbívoros pueden aumentar demasiado y agotar el pasto.",
      "Para explicar el mecanismo se sigue la cadena paso a paso: factor → población afectada → recurso → otra población. Por ejemplo: sequía → menos pasto → menos guanacos → menos alimento para el puma. Cada flecha es una relación que se puede medir.",
      "Las consecuencias también incluyen el ambiente físico: demasiados herbívoros dejan el suelo sin cobertura y aumentan la erosión, que es el desgaste y arrastre del suelo por el agua y el viento. Predecir estas consecuencias exige datos y declarar los límites del modelo.",
  ],
  vocab=[("efecto en cascada", "cambio en una población que afecta a otras en cadena"), ("erosión", "desgaste y arrastre del suelo"), ("cobertura vegetal", "plantas que cubren el suelo"), ("consecuencia", "resultado de un cambio"), ("equilibrio", "estado en que las poblaciones se mantienen sin grandes cambios")],
  worked=[
      ("Seguir una cascada", "Una enfermedad mata a casi todas las liebres. ¿Qué ocurre con el zorro que se alimenta de ellas?", ["Las liebres son su alimento.", "Con menos liebres, el zorro tiene menos alimento."], "La población de zorros tiende a disminuir"),
      ("Predecir una consecuencia", "Se elimina al depredador de los conejos de una isla. ¿Qué podría pasar con el pasto?", ["Sin depredador, los conejos aumentan.", "Más conejos comen más pasto."], "El pasto disminuye por sobrepastoreo"),
  ],
  mistakes=[
      ("Pensar que quitar un depredador siempre beneficia a las presas a largo plazo.", "Sin control, pueden agotar su alimento y luego disminuir.", "Sigue la cadena hasta el recurso."),
      ("Ignorar el ambiente físico en las consecuencias.", "El suelo y el agua también cambian.", "Agrega erosión, humedad y cobertura a tu cadena."),
  ],
  rec=[
      ("¿Cómo se llama el cambio en una población que afecta a otras en cadena?", "Efecto en cascada", "Cada cambio provoca el siguiente."),
      ("Completa: sin plantas que cubran el suelo, aumenta la ______ (erosión o lluvia).", "Erosión", "Nada sujeta el suelo."),
      ("Verdadero o falso: si desaparece una presa, su depredador puede disminuir.", "Verdadero", "Pierde su alimento."),
  ],
  und=[
      ("Si baja la población de herbívoros por una enfermedad, ¿qué suele pasar con el pasto? A) Aumenta; B) Se acaba.", "A", "Hay menos animales que lo coman."),
      ("¿Qué mecanismo explica la cadena sequía → menos pasto → menos guanacos? A) Menos alimento reduce la supervivencia de los guanacos; B) Los guanacos migran por gusto.", "A", "El recurso limita la población."),
      ("Un depredador desaparece. ¿Qué puede ocurrir con sus presas?", "Pueden aumentar demasiado", "Pierden su control natural."),
  ],
  app=[
      arith("Una isla de ejemplo tiene 40 conejos y, sin depredadores, la población se duplica cada año durante 3 años. ¿Cuántos conejos habrá al final?", "40*2*2*2", "Se duplica el total tres veces seguidas."),
      ("Cadena de ejemplo: sequía → menos pasto → menos liebres → menos alimento para el zorro culpeo. ¿Cuál es el primer factor que afecta a la cadena? A) La sequía; B) El zorro culpeo.", "A", "Es el origen del cambio."),
      ("Si una plaga de insectos mata árboles de un cerro, ¿qué efecto ambiental es probable en una lluvia fuerte? A) Mayor erosión del suelo; B) Mayor cobertura vegetal.", "A", "Sin raíces ni hojas, el suelo queda expuesto."),
  ],
  rea=[
      ("Un compañero sostiene que una enfermedad en los herbívoros solo afecta a los herbívoros. ¿Qué corrección haces? A) Afecta también a los depredadores y al pasto por las relaciones alimentarias; B) No afecta a nadie más.", "A", "Las poblaciones están conectadas."),
      ("Dos cadenas de ejemplo. 1: sequía → menos pasto → menos guanacos. 2: sequía → pasto seco → incendio. ¿Cuál termina en un factor que afecta a plantas y animales sin importar cuántos haya? A) La 2, por el incendio; B) La 1, por los guanacos.", "A", "El incendio es un factor independiente de la densidad; la baja de guanacos es una consecuencia."),
  ],
  cha=[
      ("Datos de ejemplo: la población de liebres cae de 600 a 150. Cada zorro necesita 30 liebres al año y la población de zorros era de 20. ¿Cuántos zorros podrían alimentarse ahora con las liebres que quedan?", "5", "150 dividido entre 30 es 5."),
      ("Una propuesta dice: «Eliminemos a los depredadores para salvar a las presas». ¿Qué evidencia mostrarías en contra? A) Que sin depredadores las presas pueden agotar su alimento y luego disminuir; B) Que las presas no necesitan comer.", "A", "El equilibrio depende de las relaciones."),
  ],
  context=[arith("Un parque de ejemplo registra 18 incendios en 6 años por sequías. ¿Cuántos incendios hubo en promedio por año?", "18//6", "Se divide el total de incendios entre los años.")],
  selfcheck=[("¿Qué es un efecto en cascada?", "Un cambio en una población que afecta a otras en cadena", "Las poblaciones están conectadas."), ("¿Qué ocurre si desaparece un depredador?", "Las presas pueden aumentar demasiado", "Pueden agotar su alimento."), ("Da una consecuencia ambiental del sobrepastoreo.", "Mayor erosión del suelo", "El suelo queda sin cobertura.")],
  open_task=task("Con esta red de ejemplo: pasto → guanaco → puma; pasto → liebre → zorro culpeo. Escribe dos cascadas posibles: una a partir de una sequía y otra a partir de una enfermedad que mata a los guanacos. En cada una, anota al menos tres pasos con flechas y una consecuencia sobre el suelo.", "Sequía → menos pasto → menos guanacos y liebres → menos alimento para el puma y el zorro; suelo con más erosión. Enfermedad en guanacos → menos alimento para el puma → el puma puede disminuir o cambiar de presa; el pasto sufre menos pastoreo de guanacos y puede recuperarse.", ["dos cadenas con tres pasos o más", "flechas coherentes con la red", "una consecuencia sobre el suelo"], ["dos cadenas escritas"], ["invertir las flechas", "omitir el suelo"], "Pregunta qué dato necesitarías para saber cuánto bajará el puma."),
  reinforce="Escribe una cascada de cuatro pasos que parta de un incendio.",
  extend="Explica por qué las predicciones de cascadas deben hacerse con prudencia.")

# ---------------------------------------------------------------- OA 06

L(OA6, 1,
  materials="Este cuaderno y lápiz. Todos los datos están escritos en los ejercicios.",
  use="Aprenderé qué son los ciclos del carbono, nitrógeno, agua y fósforo y por qué son importantes para los seres vivos. Sirve para formular preguntas investigables sobre ellos.",
  prior=["Sé qué es una red trófica.", "Sé que la materia se conserva."],
  explain=[
      "La materia de los seres vivos se recicla. Los ciclos biogeoquímicos describen cómo elementos como el carbono, el nitrógeno y el fósforo, y el agua, pasan entre los seres vivos y el ambiente (aire, agua, rocas, suelo). La materia circula; la energía, en cambio, fluye en un solo sentido.",
      "Cada ciclo es importante para la vida. El carbono forma las moléculas de todos los seres vivos, como azúcares y proteínas. El nitrógeno es parte de las proteínas y del ADN. El agua participa en casi todas las reacciones de las células. El fósforo es parte del ADN, de las membranas y de los huesos. En el ciclo del agua, el agua pasa a gas por evaporación (y desde las plantas por transpiración), se condensa y cae como lluvia; parte se infiltra en el suelo y parte escurre hacia los ríos.",
      "Una pregunta investigable sobre un ciclo indica qué se mide. «¿Cuánta agua se evapora de un vaso con tapa y de uno sin tapa en 24 horas?» se contesta midiendo el nivel. «¿Es más importante el carbono que el agua?» no, porque depende de opiniones.",
  ],
  vocab=[("ciclo biogeoquímico", "recorrido de un elemento entre seres vivos y ambiente"), ("carbono", "elemento que forma las moléculas de los seres vivos"), ("nitrógeno", "elemento de las proteínas y del ADN"), ("fósforo", "elemento del ADN, las membranas y los huesos"), ("reciclaje de materia", "uso repetido de los mismos elementos"), ("transpiración", "agua que las plantas liberan al aire como vapor"), ("infiltración", "paso del agua de lluvia hacia el interior del suelo"), ("escurrimiento", "agua que corre sobre el suelo hacia los ríos")],
  worked=[
      ("Importancia biológica", "¿Por qué los seres vivos necesitan nitrógeno?", ["Pienso en las moléculas que lo contienen.", "Forma parte de las proteínas y del ADN."], "Porque forma parte de las proteínas y del ADN"),
      ("Mejorar una pregunta", "Mejora «¿Es genial el ciclo del agua?» para que se pueda investigar.", ["Quito la palabra de opinión.", "Indico qué se mide: el nivel de agua en un vaso destapado.", "Queda: «¿Cuántos milímetros baja el nivel de agua de un vaso destapado en 24 horas?»"], "«¿Cuántos milímetros baja el nivel de agua de un vaso destapado en 24 horas?»"),
  ],
  mistakes=[
      ("Decir que la energía también circula como la materia.", "La energía fluye en un solo sentido y se pierde como calor.", "Recuerda: la materia circula y la energía fluye."),
      ("Pensar que los elementos se «gastan» en un ciclo.", "Se transforman y cambian de lugar, pero no desaparecen.", "Sigue dónde queda el elemento en cada etapa."),
  ],
  rec=[
      ("¿Qué elemento forma las moléculas de todos los seres vivos?", "Carbono", "Es la base de los azúcares y las proteínas."),
      ("Completa: el elemento que forma parte de las proteínas y del ADN es el ______ (nitrógeno o fósforo).", "Nitrógeno", "Es parte de ambas moléculas."),
      ("Verdadero o falso: la materia circula en los ciclos.", "Verdadero", "Se recicla entre seres vivos y ambiente."),
  ],
  und=[
      ("¿Qué diferencia hay entre materia y energía en un ecosistema? A) La materia circula y la energía fluye en un sentido; B) Ambas circulan igual.", "A", "La energía se disipa como calor."),
      ("¿Para qué sirve el fósforo en los seres vivos? A) Forma parte del ADN y de las membranas; B) Es el gas que respiramos.", "A", "Es un componente de moléculas importantes."),
      ("¿Qué es un ciclo biogeoquímico?", "El recorrido de un elemento entre seres vivos y ambiente", "Muestra cómo se recicla la materia."),
  ],
  app=[
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos mm baja el nivel de agua en un vaso destapado en 24 horas?; B) ¿Es lindo el ciclo del agua?", "A", "Se contesta midiendo el nivel."),
      arith("Un vaso de ejemplo tiene 150 mm de agua y baja 3 mm cada día por evaporación. ¿Cuántos mm quedan después de 5 días?", "150-3*5", "Se resta la evaporación total de los 5 días."),
      ("Una persona dice que las plantas obtienen su carbono del suelo. ¿Cuál es la fuente más importante del carbono para su fotosíntesis? A) El dióxido de carbono del aire; B) Las piedras del suelo.", "A", "Las plantas toman CO2 del aire para fabricar azúcares."),
  ],
  rea=[
      ("Un compañero dice que, como la materia circula, los seres vivos nunca necesitan energía nueva. ¿Qué respondes? A) La energía no se recicla: llega como luz y se pierde como calor; B) Tiene razón, porque todo circula.", "A", "La energía fluye en un solo sentido."),
      ("Un estudiante tapa un vaso con agua y lo deja al sol; aparecen gotas en la tapa. ¿Qué parte del ciclo del agua muestra? A) La evaporación y la condensación; B) La infiltración.", "A", "El agua se evapora y vuelve a líquido al enfriarse en la tapa."),
  ],
  cha=[
      ("Un estudio de ejemplo mide el agua evaporada: vaso con tapa pierde 1 mm y vaso sin tapa pierde 4 mm en 24 horas. ¿Cuántos mm más pierde el vaso sin tapa?", "3", "4 menos 1 es 3."),
      ("Un bosque de ejemplo pierde su vegetación por un incendio. ¿Qué ciclo se altera más inmediatamente en esa zona? A) El del agua, porque sin plantas hay menos transpiración y más escurrimiento; B) El del fósforo, que desaparece.", "A", "Las plantas participan en el ciclo del agua."),
  ],
  context=[arith("Una familia de ejemplo recoge agua lluvia en 3 baldes y cada uno junta 8 litros. ¿Cuántos litros recoge en total?", "3*8", "Se multiplica el número de baldes por los litros de cada uno.")],
  selfcheck=[("¿Qué circula en los ciclos y qué fluye en un solo sentido?", "La materia circula y la energía fluye", "Es una diferencia básica."), ("¿Para qué sirve el carbono?", "Forma las moléculas de los seres vivos", "Es la base de azúcares y proteínas."), ("¿Qué hace investigable a una pregunta sobre un ciclo?", "Que indica qué se mide", "Se contesta con datos.")],
  open_task=task("Elige uno de estos ciclos: agua, carbono, nitrógeno o fósforo. Escribe (a) una frase sobre su importancia para los seres vivos y (b) dos preguntas investigables que podrías contestar con datos, por ejemplo midiendo el nivel de agua de un vaso o contando cuántas gotas se forman en una tapa en 1 hora. Para el ciclo del agua, usa un vaso con tapa y otro sin tapa.", "Agua: participa en casi todas las reacciones de las células. Preguntas: «¿Cuánto baja el nivel de un vaso destapado en 24 horas?» y «¿Cuántas gotas aparecen en la tapa en 1 hora?».", ["frase de importancia correcta", "dos preguntas con algo que medir", "no son de opinión"], ["frase y dos preguntas"], ["preguntas de opinión", "frase sin elemento"], "Pregunta qué materiales de casa usarías para medir una de tus preguntas."),
  reinforce="Escribe para qué sirve el fósforo y para qué sirve el nitrógeno.",
  extend="Explica por qué la materia puede reciclarse pero la energía no.")

L(OA6, 2,
  materials="Este cuaderno y lápiz. Las pirámides y los datos de energía son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a leer redes y pirámides tróficas y a explicar cómo fluye la energía en un ecosistema. Sirve para entender por qué hay menos depredadores que presas.",
  prior=["Sé qué es una red trófica.", "Sé que los productores fabrican alimento con luz."],
  explain=[
      "La energía entra al ecosistema como luz y los productores la almacenan en sus moléculas. Cuando un consumidor come, recibe parte de esa energía. En cada paso de un nivel trófico al siguiente, solo pasa en promedio cerca del 10 % de la energía. El resto se usa para funciones como moverse y respirar, y se pierde como calor.",
      "Una pirámide de energía muestra esto con barras: la base es el productor (mayor energía) y arriba están los consumidores. Si los productores tienen 10.000 unidades, los consumidores primarios tienen cerca de 1.000, los secundarios cerca de 100 y los terciarios cerca de 10. Por eso hay pocos depredadores en la cima.",
      "Una red trófica es más realista que una cadena porque muestra que un animal puede comer varias especies y ser comido por varias. La energía fluye en un solo sentido: del Sol a los productores, a los consumidores, y se pierde como calor. La materia, en cambio, se recicla gracias a los descomponedores.",
  ],
  vocab=[("nivel trófico", "posición de un organismo en la cadena alimentaria"), ("productor", "organismo que fabrica su alimento"), ("consumidor primario", "herbívoro; se alimenta de productores"), ("consumidor secundario", "carnívoro que se alimenta de herbívoros"), ("pirámide de energía", "gráfico de barras de la energía por nivel trófico")],
  worked=[
      ("Calcular la energía que pasa", "Los productores de un ecosistema de ejemplo tienen 20.000 unidades de energía. ¿Cuánto llega a los consumidores primarios si pasa cerca del 10 %?", ["Calculo el 10 % de 20.000.", "20.000 dividido por 10 es 2.000."], "Cerca de 2.000 unidades"),
      ("Ubicar un nivel", "En la cadena pasto → liebre → zorro, ¿qué nivel trófico ocupa el zorro?", ["El pasto es el productor.", "La liebre es consumidor primario y el zorro come a la liebre."], "Consumidor secundario"),
  ],
  mistakes=[
      ("Pensar que pasa el 100 % de la energía al siguiente nivel.", "Gran parte se usa en funciones vitales y se pierde como calor.", "Recuerda la regla del 10 % aproximado."),
      ("Creer que la energía se recicla como la materia.", "La energía fluye en un solo sentido.", "Dibuja la energía con flechas que no vuelven."),
  ],
  rec=[
      ("¿Qué porcentaje de energía pasa en promedio al siguiente nivel trófico?", "Cerca del 10 %", "El resto se pierde como calor."),
      ("Completa: el herbívoro es un consumidor ______ (primario o secundario).", "Primario", "Se alimenta directamente de productores."),
      ("Verdadero o falso: en una pirámide de energía, la base es el productor.", "Verdadero", "Tiene la mayor energía."),
  ],
  und=[
      ("¿Por qué hay menos depredadores en la cima de la pirámide? A) Porque llega poca energía a ese nivel; B) Porque son más lentos.", "A", "La energía disponible disminuye en cada paso."),
      ("¿Qué le pasa a la mayor parte de la energía en cada nivel? A) Se usa en funciones vitales y se pierde como calor; B) Se guarda toda en el cuerpo.", "A", "Solo una parte pasa al siguiente nivel."),
      ("En la cadena pasto → guanaco → puma, ¿qué nivel ocupa el puma?", "Consumidor secundario", "Come a un herbívoro."),
  ],
  app=[
      arith("Los productores tienen 50.000 unidades de energía. ¿Cuántas llegan a los consumidores primarios si pasa el 10 %?", "50000//10", "Se divide la energía entre 10."),
      arith("Siguiendo el ejemplo, si los consumidores primarios tienen 5.000 unidades, ¿cuántas pasan a los secundarios con el 10 %?", "5000//10", "Se divide la energía entre 10."),
      ("En una red de ejemplo, el pasto es comido por ratones y por conejos; un zorro come ambos. ¿Cuántos consumidores primarios hay? A) 2; B) 3.", "A", "Son el ratón y el conejo."),
  ],
  rea=[
      ("Un estudiante dice que un ecosistema podría tener tantos depredadores como herbívoros. ¿Qué evidencia lo contradice? A) La energía disminuye en cada nivel, por lo que la cima no puede mantener tantos individuos; B) Los depredadores no comen herbívoros.", "A", "La pirámide se angosta."),
      ("Datos de ejemplo: productores 40.000, consumidores primarios 4.000, consumidores secundarios 400. Un compañero afirma que se cumple el 10 % aproximado. ¿Es correcto? A) Sí, porque cada nivel tiene un décimo del anterior; B) No, porque los valores de cada nivel son distintos.", "A", "4.000 es un décimo de 40.000 y 400 es un décimo de 4.000."),
  ],
  cha=[
      arith("Una pirámide de ejemplo tiene 100.000 unidades en los productores. Aplicando el 10 % tres veces seguidas, ¿cuántas llegan al tercer nivel de consumidores?", "100000//10//10//10", "Se divide entre 10 en cada nivel."),
      ("Un proyecto propone criar peces carnívoros en un estanque pequeño con pocas algas. ¿Qué problema anticipas con la pirámide? A) Habrá muy poca energía en la base para sostener a los carnívoros; B) Los peces no comen.", "A", "La energía disponible en los niveles altos es mucho menor."),
  ],
  context=[arith("Una granja de ejemplo tiene 4 estanques con 25 peces herbívoros cada uno. ¿Cuántos peces tiene en total?", "4*25", "Se multiplica el número de estanques por los peces de cada uno.")],
  selfcheck=[("¿Cuánta energía pasa al siguiente nivel en promedio?", "Cerca del 10 %", "El resto se pierde como calor."), ("¿Por qué las pirámides se angostan hacia arriba?", "Porque la energía disminuye en cada nivel", "Pasa poca energía a los niveles altos."), ("¿Qué es un consumidor secundario?", "Un carnívoro que come a herbívoros", "Está en el tercer nivel.")],
  open_task=task("Con una red de ejemplo (pasto → conejo → zorro; pasto → ratón → zorro; pasto → ratón → búho), identifica los productores, los consumidores primarios y los secundarios. Dibuja una pirámide con 30.000 unidades en los productores y calcula las unidades en los dos niveles siguientes con el 10 %. Explica por qué hay solo un puñado de zorros comparado con los conejos.", "Productor: pasto. Primarios: conejo y ratón. Secundarios: zorro y búho. Pirámide: 30.000 → 3.000 → 300. Hay pocos zorros porque llega poca energía al nivel de los secundarios.", ["clasifica los niveles", "calcula 3.000 y 300", "explica con la energía"], ["lista, pirámide y explicación"], ["pasar el 100 % de la energía", "dibujar flechas al revés"], "Pregunta qué pasaría con el zorro si desapareciera el ratón."),
  reinforce="Dibuja una pirámide de energía con cuatro niveles.",
  extend="Explica por qué los alimentos de origen vegetal permiten alimentar a más personas con la misma superficie.")

L(OA6, 3,
  materials="Hojas y lápices de colores. Si no tienes, usa solo lápiz y escribe los nombres en cajas con flechas.",
  use="Aprenderé a construir modelos de los ciclos del carbono, del nitrógeno, del agua y del fósforo. Sirve para explicar cómo circula la materia entre seres vivos y ambiente.",
  prior=["Sé qué es un ciclo biogeoquímico.", "Sé qué hacen productores, consumidores y descomponedores."],
  explain=[
      "Ciclo del carbono: las plantas toman dióxido de carbono (CO2) del aire y lo usan en la fotosíntesis para formar azúcares. Los animales comen las plantas. Los seres vivos liberan CO2 al respirar, y los descomponedores lo liberan al descomponer restos. La quema de combustibles también libera CO2. Ciclo del agua: el agua se evapora, se condensa en nubes, cae como precipitación y vuelve a los mares y suelos.",
      "Ciclo del nitrógeno: el aire tiene alrededor de 78 % de nitrógeno (N2), pero las plantas no lo usan directamente. Algunas bacterias del suelo lo transforman en formas que las plantas absorben (fijación). Los animales obtienen nitrógeno al comer plantas. Los descomponedores devuelven nitrógeno al suelo y otras bacterias lo devuelven al aire. Ciclo del fósforo: no tiene una fase importante en el aire; el fósforo pasa de las rocas al suelo y al agua, a las plantas, a los animales y de vuelta al suelo y a los sedimentos.",
      "Un modelo de ciclo usa cajas (almacenes) y flechas (flujos). Contrastar un modelo con otro permite ver qué incluyen y qué dejan afuera. Ningún modelo muestra todos los procesos; sirve para razonar con claridad.",
  ],
  vocab=[("fotosíntesis", "proceso en que las plantas forman azúcares con luz, agua y CO2"), ("evaporación", "paso del agua de líquido a gas"), ("condensación", "paso del vapor de agua a líquido"), ("fijación de nitrógeno", "transformación del N2 del aire en formas usables"), ("almacén", "lugar donde queda un elemento por un tiempo")],
  worked=[
      ("Seguir el carbono", "El pasto absorbe CO2 y forma azúcares. Un guanaco come ese pasto. ¿Cómo vuelve el carbono al aire?", ["El guanaco respira.", "Al respirar libera CO2 al aire."], "Como CO2 por la respiración"),
      ("Seguir el nitrógeno", "¿Por qué las plantas necesitan bacterias del suelo para usar el nitrógeno del aire?", ["El N2 del aire no es usable por las plantas.", "Ciertas bacterias lo transforman en formas que las raíces absorben."], "Porque las bacterias fijan el N2 en formas usables"),
  ],
  mistakes=[
      ("Pensar que el nitrógeno del aire es usado directamente por las plantas.", "Necesita ser transformado por bacterias.", "Incluye en tu modelo la fijación."),
      ("Dibujar el ciclo del fósforo con una etapa en el aire.", "El fósforo casi no tiene fase gaseosa.", "Muestra que pasa por rocas, suelo, agua y seres vivos."),
  ],
  rec=[
      ("¿Qué gas toman las plantas del aire para la fotosíntesis?", "Dióxido de carbono", "Con él forman azúcares."),
      ("Completa: el paso de vapor de agua a líquido se llama ______ (condensación o evaporación).", "Condensación", "Ocurre cuando el vapor se enfría."),
      ("Verdadero o falso: las plantas absorben directamente el N2 del aire.", "Falso", "Necesitan bacterias que lo transformen."),
  ],
  und=[
      ("¿Qué proceso libera CO2 al aire? A) La respiración; B) La fotosíntesis.", "A", "La fotosíntesis lo toma; la respiración lo libera."),
      ("¿Por qué el ciclo del fósforo es distinto de los demás? A) Casi no tiene fase gaseosa en el aire; B) No lo usan los seres vivos.", "A", "Circula por rocas, suelo, agua y seres vivos."),
      ("¿Qué función tienen los descomponedores en los ciclos?", "Devolver los elementos de restos al suelo o al aire", "Reciclan la materia de los restos."),
  ],
  app=[
      ("Un modelo de ejemplo del carbono muestra: aire (CO2) → planta → animal → aire (CO2). ¿Qué proceso lleva el carbono de la planta al aire? A) Respiración; B) Evaporación.", "A", "La planta también respira y libera CO2."),
      ("Con el modelo del agua: mar → vapor → nube → lluvia → río → mar. ¿Qué etapa es la evaporación? A) De mar a vapor; B) De nube a lluvia.", "A", "El líquido pasa a gas."),
      arith("El aire tiene alrededor de 78 % de nitrógeno (N2). En una muestra de ejemplo de 200 partes de aire, ¿cuántas partes son N2?", "200*78//100", "Se calcula 78 de cada 100 partes."),
  ],
  rea=[
      ("Un estudiante dibuja el ciclo del carbono sin descomponedores. ¿Qué parte falta? A) El retorno del carbono de restos al suelo y al aire; B) La fotosíntesis.", "A", "Los descomponedores cierran el ciclo."),
      ("Dos modelos del agua: el A tiene evaporación, condensación y lluvia; el B suma infiltración al suelo. ¿Cuál explica mejor el agua subterránea? A) El B, porque incluye la infiltración; B) El A, porque es más corto.", "A", "La infiltración lleva el agua al subsuelo."),
  ],
  cha=[
      ("Una granja de ejemplo agrega fertilizante con fósforo y parte llega a un río. ¿Qué almacén recibe el fósforo? A) El agua del río; B) El aire.", "A", "El fósforo no pasa por el aire."),
      ("Un modelo de ejemplo propone que el nitrógeno del aire pase directo a los animales. ¿Cuál es la corrección? A) Pasa a las plantas por fijación bacteriana y luego a los animales al comerlas; B) No pasa nunca.", "A", "Los animales obtienen nitrógeno de sus alimentos."),
  ],
  context=[arith("En un huerto de ejemplo, 6 plantas de leguminosas fijan cada una 4 unidades de nitrógeno por mes. ¿Cuántas unidades se fijan en 3 meses?", "6*4*3", "Se multiplican plantas, unidades por mes y meses.")],
  selfcheck=[("¿Qué gas usan las plantas del ciclo del carbono?", "Dióxido de carbono", "Lo toman del aire."), ("¿Por qué las bacterias son importantes en el ciclo del nitrógeno?", "Porque fijan el nitrógeno del aire", "Lo transforman en formas usables."), ("¿Qué diferencia tiene el ciclo del fósforo?", "No tiene fase importante en el aire", "Pasa por rocas, suelo y agua.")],
  open_task=task("Dibuja un modelo con cajas y flechas del ciclo del carbono usando estos elementos: aire (CO2), planta, animal, descomponedores y combustibles. Marca con una flecha cada proceso: fotosíntesis, respiración y descomposición. Agrega una limitación de tu modelo.", "Aire (CO2) → planta por fotosíntesis; planta → animal por alimentación; planta, animal y descomponedores → aire por respiración; restos → descomponedores; combustibles → aire (CO2) por combustión. Limitación: no muestra el carbono disuelto en el mar.", ["incluye los cinco elementos", "rotula los tres procesos", "declara una limitación"], ["dibujo con cajas y flechas"], ["flechas sin rotular", "olvidar a los descomponedores"], "Pregunta qué proceso agregarías para mostrar la quema de combustibles."),
  reinforce="Dibuja el ciclo del agua con cinco etapas.",
  extend="Explica por qué los ciclos conectan a los seres vivos con el aire, el agua y las rocas.")

L(OA6, 4,
  materials="Este cuaderno y lápiz. Los datos de contaminantes son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé cómo viaja un contaminante por una red trófica y por qué se acumula en los niveles altos (bioacumulación). Sirve para comprender los riesgos de ciertos contaminantes.",
  prior=["Sé que la energía disminuye en cada nivel trófico.", "Sé leer tablas de datos."],
  explain=[
      "Un contaminante es una sustancia que daña a los seres vivos. Algunos, como ciertos metales pesados y plaguicidas persistentes, no se descomponen fácilmente ni se eliminan del cuerpo. Cuando un organismo los absorbe, se acumulan en sus tejidos: eso es la bioacumulación.",
      "Cuando un consumidor come muchos individuos contaminados, recibe la suma de sus contaminantes. Por eso, la concentración aumenta de un nivel trófico al siguiente: se llama biomagnificación. Los depredadores de la cima tienen las concentraciones más altas, aunque en el ambiente la concentración sea baja.",
      "La trayectoria de un contaminante sigue el ciclo del agua y la red trófica: se disuelve en un río, lo absorben las algas, los toman pequeños animales y luego peces y aves. Para estudiarla se miden las concentraciones en cada nivel y se comparan. Las medidas de prevención incluyen reducir los vertidos y no tirar residuos al agua.",
  ],
  vocab=[("contaminante", "sustancia que daña a los seres vivos"), ("bioacumulación", "acumulación de una sustancia en el cuerpo de un organismo"), ("biomagnificación", "aumento de la concentración al subir por la red trófica"), ("concentración", "cantidad de sustancia por cantidad de masa o volumen"), ("persistente", "que no se descompone fácilmente")],
  worked=[
      ("Calcular una magnificación", "Un contaminante de ejemplo mide 2 unidades por kg en algas y se multiplica por 5 en cada nivel. ¿Cuánto hay en el consumidor primario?", ["Multiplico la concentración de las algas por 5.", "2 por 5 es 10."], "10 unidades por kg"),
      ("Reconocer el nivel de mayor riesgo", "Niveles: algas, pez pequeño, pez grande, ave. ¿Cuál tiene la mayor concentración esperada?", ["La concentración aumenta hacia la cima.", "El ave está en el nivel más alto."], "El ave"),
  ],
  mistakes=[
      ("Pensar que un contaminante en cantidad pequeña en el agua es inofensivo.", "Puede acumularse y magnificarse en los niveles altos.", "Mira la concentración en los depredadores."),
      ("Confundir bioacumulación con biomagnificación.", "La primera es en un organismo; la segunda aumenta al subir de nivel.", "Piensa: uno solo versus de nivel en nivel."),
  ],
  rec=[
      ("¿Cómo se llama el aumento de la concentración al subir por la red trófica?", "Biomagnificación", "Se suma lo que traen las presas."),
      ("Completa: una sustancia que se acumula en el cuerpo de un organismo produce ______ (bioacumulación o fotosíntesis).", "Bioacumulación", "Se queda en los tejidos."),
      ("Verdadero o falso: los depredadores de la cima suelen tener las mayores concentraciones.", "Verdadero", "Reciben la suma de muchas presas."),
  ],
  und=[
      ("¿Por qué los contaminantes persistentes son peligrosos? A) Porque no se descomponen ni se eliminan fácilmente; B) Porque se evaporan.", "A", "Se acumulan en los tejidos."),
      ("¿Dónde es mayor la concentración esperada: en el plancton o en un ave que come peces? A) En el ave; B) En el plancton.", "A", "Acumula lo de sus presas."),
      ("¿Por qué conviene medir la concentración en cada nivel trófico?", "Para ver cómo aumenta de nivel en nivel", "Así se reconoce la biomagnificación."),
  ],
  app=[
      arith("Un contaminante de ejemplo mide 3 unidades por kg en algas y se multiplica por 5 en cada nivel. ¿Cuánto hay en el segundo consumidor (algas, pez pequeño, pez grande)?", "3*5*5", "Se multiplica por 5 dos veces."),
      arith("En una tabla de ejemplo: algas 3, pez pequeño 15, pez grande 75, ave 375 (unidades por kg). ¿Cuántas veces mayor es la concentración del ave que la de las algas?", "375//3", "Se divide el valor del ave entre el de las algas."),
      ("Un río recibe un vertido con un contaminante persistente. ¿Qué medida es más efectiva a largo plazo? A) Evitar el vertido; B) Esperar a que los peces lo eliminen.", "A", "Si se evita la fuente, no se acumula."),
  ],
  rea=[
      ("Un estudiante dice: «Si el agua tiene muy poco contaminante, los peces grandes no estarán afectados». ¿Cuál es la crítica? A) La biomagnificación puede concentrar el contaminante en los peces grandes; B) Los peces grandes no comen peces pequeños.", "A", "La concentración aumenta por nivel."),
      ("Tabla de ejemplo: algas 5, pez pequeño 20, pez grande 80, ave 320 (unidades por kg). Un compañero dice que la concentración se multiplica por 5 de un nivel al siguiente. ¿Es correcto? A) No, se multiplica por 4 en cada paso; B) Sí, se multiplica por 5 en cada paso.", "A", "5 por 4 es 20, 20 por 4 es 80 y 80 por 4 es 320."),
  ],
  cha=[
      ("Un pez grande de ejemplo tiene 50 unidades por kg de un contaminante y un límite de ejemplo es 40 unidades por kg. ¿Cuántas unidades se pasa del límite?", "10", "50 menos 40 es 10."),
      ("Un equipo mide el contaminante solo en el agua y concluye que el ecosistema está sano. ¿Qué falta medir? A) La concentración en los organismos de distintos niveles tróficos; B) El color del agua.", "A", "La medición en el agua no refleja la magnificación."),
  ],
  context=[arith("Un monitoreo de ejemplo toma 4 muestras de peces por mes durante 6 meses. ¿Cuántas muestras toma en total?", "4*6", "Se multiplica el número de muestras por los meses.")],
  selfcheck=[("¿Qué es la bioacumulación?", "La acumulación de una sustancia en el cuerpo de un organismo", "No se elimina fácilmente."), ("¿Por qué los depredadores de la cima tienen más contaminante?", "Porque reciben el de todas sus presas", "Es la biomagnificación."), ("¿Qué medida previene la contaminación del agua?", "Reducir los vertidos", "Evita que el contaminante entre a la red trófica.")],
  open_task=task("Con estos datos de ejemplo, ordena y grafica la concentración de un contaminante persistente (unidades por kg): algas 4; pez pequeño 20; pez grande 100; ave 500. Calcula por cuánto se multiplica en cada paso, escribe una conclusión de dos oraciones y propone una medida de prevención.", "Se multiplica por 5 en cada paso. La concentración aumenta hacia la cima de la red trófica: el ave tiene 125 veces la de las algas. Medida: evitar los vertidos al río.", ["calcula el factor 5", "conclusión con dos datos", "medida de prevención coherente"], ["gráfico, cálculo y medida"], ["decir que disminuye hacia la cima", "no proponer medida"], "Pregunta qué dato más necesitarías para confiar en la conclusión."),
  reinforce="Explica con tus palabras qué es la biomagnificación.",
  extend="Explica por qué un contaminante persistente puede llegar a lugares lejos de donde se vertió.")

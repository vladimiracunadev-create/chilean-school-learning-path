"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 05 (pubertad) y OA 06 (actividad física e higiene en la pubertad)."""
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


OA5, OA6 = "CN06 OA 05", "CN06 OA 06"

# ---------------------------------------------------------------- OA 05
L(OA5, 1,
  materials="Este cuaderno y lápiz. Los datos de crecimiento están escritos en los ejercicios y no son de ninguna persona real.",
  use="Aprenderé qué es la pubertad y a separar lo que muestran los datos de lo que se supone. Sirve para entender que los cambios del cuerpo son normales y varían de una persona a otra.",
  prior=["Sé que las personas crecen y cambian durante la vida.", "Sé que una observación es lo que se mide o se cuenta."],
  explain=[
      "La pubertad es una etapa del desarrollo humano entre la niñez y la adultez. En ella el cuerpo crece rápido y se prepara para la reproducción. Comienza más o menos entre los 8 y 13 años en las mujeres y entre los 9 y 14 años en los hombres, pero cada persona tiene su propio ritmo. Empezar antes o después es normal.",
      "Los cambios los ordenan las hormonas, mensajeros químicos que viajan por la sangre. En las mujeres actúan sobre todo los estrógenos que producen los ovarios, y en los hombres la testosterona que producen los testículos. En ambos aumenta la estatura de forma rápida: es el estirón. También aparece vello en las axilas y en la zona genital, la piel se vuelve más grasa y el sudor tiene olor más fuerte.",
      "Para estudiar la pubertad con datos, se separa lo observado de lo supuesto. Una observación es «entre los 11 y los 12 años creció 7 cm». Una interpretación es «esa persona es la más madura de su curso». Los datos de una sola persona no sirven para decir cómo son todas. Las comparaciones entre personas pueden hacer sentir mal a alguien, por eso se hacen con respeto.",
  ],
  vocab=[("pubertad", "etapa en que el cuerpo cambia y se prepara para la reproducción"), ("hormona", "mensajero químico que viaja por la sangre"), ("estirón", "período de crecimiento rápido de la estatura"), ("estrógeno", "hormona de los ovarios"), ("testosterona", "hormona de los testículos")],
  worked=[
      ("Calcular el crecimiento", "Los datos de ejemplo de una persona muestran 140 cm a los 10 años y 147 cm a los 11 años. ¿Cuánto creció en ese año?", ["Identifico la estatura final: 147.", "Identifico la inicial: 140.", "Resto 147 − 140."], "Creció 7 cm"),
      ("Observación o interpretación", "Dos frases: (1) «Entre los 11 y los 12 años creció 6 cm». (2) «Está creciendo más rápido porque es muy trabajador». ¿Cuál es la observación?", ["Pregunto cuál se mide.", "La frase 1 tiene un dato.", "La frase 2 supone una causa."], "La frase 1"),
  ],
  mistakes=[
      ("Pensar que quien empieza la pubertad antes o después tiene algún problema.", "Cada persona tiene su ritmo y existe un rango normal amplio.", "Recuerda que los rangos de edad son aproximados."),
      ("Usar los datos de una persona para decir cómo son todas.", "Una persona no representa a las demás.", "Di que el dato solo vale para ese caso."),
  ],
  rec=[
      ("La etapa entre la niñez y la adultez en que el cuerpo cambia se llama ______. Completa con «pubertad» o «vejez».", "Pubertad", "Es la etapa de cambios del cuerpo."),
      ("¿Quién ordena los cambios de la pubertad: las hormonas o los zapatos?", "Las hormonas", "Son mensajeros químicos."),
      ("¿El crecimiento rápido en la pubertad se llama estirón o ciclo?", "Estirón", "Es el aumento rápido de la estatura."),
  ],
  und=[
      ("¿Es normal empezar la pubertad a los 9 años o a los 13 años? Responde Sí o No.", "Sí", "Cada persona tiene su ritmo."),
      ("¿Cuál es una interpretación? A) Creció 5 cm en un año. B) Es la persona más madura de su curso.", "B", "La madurez no se mide con un dato."),
      ("¿Qué órganos producen la mayor parte de la testosterona?", "Los testículos", "Son productores de la hormona masculina."),
  ],
  app=[
      arith("Una persona de ejemplo medía 150 cm a los 12 años y 158 cm a los 13. ¿Cuántos centímetros creció?", "158-150", "Se restan las estaturas."),
      arith("En 3 años seguidos, una persona de ejemplo creció 6 cm, 8 cm y 7 cm. ¿Cuánto creció en total?", "6+8+7", "Se suman los tres crecimientos."),
      ("Datos de ejemplo: a los 9 años, 130 cm; a los 10, 135 cm; a los 11, 143 cm. ¿En qué año creció más: entre los 9 y 10 o entre los 10 y 11?", "Entre los 10 y los 11", "Creció 8 cm frente a 5 cm."),
  ],
  rea=[
      ("Un compañero dice: «Como el mío creció más que el tuyo, tú tienes algo malo». ¿Es una conclusión válida? Responde Sí o No y explica.", "No; cada persona tiene su propio ritmo", "Las diferencias de ritmo son normales."),
      ("Un registro de una niña de ejemplo muestra 6 cm de crecimiento. Alguien dice que todas las niñas crecen 6 cm al año. ¿Qué error tiene?", "Generaliza desde un solo caso", "Los datos de una persona no sirven para todas."),
  ],
  cha=[
      ("Una persona de ejemplo crece 4 cm, 5 cm, 8 cm y 3 cm en cuatro años seguidos. ¿En cuál de esos años ocurrió el estirón?", "En el tercero", "Es el año de mayor crecimiento: 8 cm."),
      ("Sobre el dato «creció 7 cm entre los 11 y los 12 años», ¿cuál frase es la interpretación? A) Creció 7 cm en un año. B) Está en su estirón.", "B", "Agrega una explicación que el dato solo no prueba."),
  ],
  context=[("Dato de ejemplo. Una persona midió 148 cm en marzo y 154 cm en diciembre del mismo año. ¿Cuántos centímetros creció?", "6", "154 − 148 = 6.")],
  selfcheck=[("¿Qué es la pubertad?", "La etapa en que el cuerpo cambia y se prepara para la reproducción", "Ocurre entre la niñez y la adultez."), ("¿Por qué las edades de inicio son aproximadas?", "Porque cada persona tiene su ritmo", "Hay un rango normal."), ("¿Qué son las hormonas?", "Mensajeros químicos que viajan por la sangre", "Ordenan los cambios del cuerpo.")],
  open_task=task("Lee estos datos de ejemplo de estatura (cm): 9 años, 132; 10 años, 137; 11 años, 144; 12 años, 152; 13 años, 157. Calcula cuánto creció cada año, indica en cuál año fue mayor el crecimiento y escribe una observación y una interpretación, rotuladas.", "Crecimientos: 5, 7, 8, 5. El mayor fue entre los 11 y los 12 años (8 cm). Observación: entre los 11 y 12 años creció 8 cm. Interpretación: ese puede ser su estirón.", ["cuatro diferencias correctas", "indica el año mayor", "observación e interpretación rotuladas"], ["lista de cálculos", "dos frases"], ["generalizar a todos", "mezclar observación e interpretación"], "Pregunta qué dato nuevo haría más confiable la interpretación."),
  reinforce="Escribe dos cambios de la pubertad que se comparten entre mujeres y hombres.",
  extend="Explica por qué se dice que los rangos de edad de la pubertad son aproximados.")

L(OA5, 2,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo.",
  use="Aprenderé a formular preguntas y predicciones sobre los cambios de la pubertad. Sirve para planificar cómo comprobar ideas con datos y sin juzgar a las personas.",
  prior=["Sé qué es la pubertad.", "Sé que una predicción lleva una razón."],
  explain=[
      "Además de los cambios comunes, hay cambios propios de cada grupo. En las mujeres se desarrollan las mamas, las caderas se ensanchan y ocurre la menarquia, que es la primera menstruación. Suele aparecer entre los 9 y los 15 años. En los hombres crecen los testículos y el pene, la voz se vuelve más grave, aparece vello en la cara y los hombros se ensanchan. También ocurren las primeras eyaculaciones.",
      "También hay cambios en las emociones y en la forma de relacionarse. Las personas pueden sentirse más sensibles, con más energía o con sueño, porque las hormonas cambian. Es normal y conversarlo con una persona de confianza ayuda. Los cambios no son una competencia: cada persona avanza a su ritmo.",
      "Las preguntas comprobables nombran lo que se mide. Por ejemplo: «¿Cuántos centímetros crece en promedio un grupo en el año del estirón?». Una predicción tiene razón: «Entre personas del mismo sexo, quien empieza la pubertad antes comenzará antes su estirón, porque las hormonas actúan antes». La predicción se comprueba con una tabla de datos, no con comentarios sobre las personas.",
  ],
  vocab=[("menarquia", "primera menstruación"), ("eyaculación", "salida de semen por la uretra"), ("vello", "pelo fino del cuerpo"), ("voz más grave", "voz de tono más bajo por cambios en la laringe"), ("comprobable", "que se puede probar con datos")],
  worked=[
      ("Elegir la pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Quién se ve mejor durante la pubertad? B) ¿Cuántos centímetros crece un grupo de 20 estudiantes en un año?", ["Pregunto si hay un número.", "En B se miden centímetros.", "En A la respuesta es un gusto."], "B"),
      ("Predecir con razón", "Una persona empieza su pubertad antes. ¿Qué predices sobre cuándo comenzará su estirón y por qué?", ["Recuerdo que las hormonas ordenan los cambios.", "Si actúan antes, los cambios empiezan antes.", "Escribo la predicción con su razón."], "Probablemente comience antes, porque las hormonas actúan antes"),
  ],
  mistakes=[
      ("Predecir sin razón: «seguro será igual para todos».", "No tiene respaldo y las personas varían.", "Agrega «porque» y usa hormonas y ritmo."),
      ("Usar comentarios sobre una persona como dato.", "Un comentario no es una medición y puede ofender.", "Usa mediciones anónimas, como centímetros o años."),
  ],
  rec=[
      ("La primera menstruación se llama ______. Completa con «menarquia» o «eyaculación».", "Menarquia", "Es un cambio de la pubertad en mujeres."),
      ("¿La voz más grave aparece más en las mujeres o en los hombres?", "En los hombres", "Es un cambio propio de la pubertad masculina."),
      ("Una pregunta comprobable, ¿se responde con datos o con gustos?", "Con datos", "Se mide o cuenta."),
  ],
  und=[
      ("¿Cuál pregunta se puede comprobar? A) ¿Cuántos cm crece un grupo en un año? B) ¿Quién es el más interesante del curso?", "A", "Los centímetros se miden."),
      ("Una predicción dice: «El estirón será mayor en el grupo que empezó antes, porque las hormonas actuaron antes». ¿Cuál es la razón?", "Porque las hormonas actuaron antes", "La razón va después de «porque»."),
      ("¿Por qué los cambios emocionales son normales?", "Porque las hormonas cambian", "Influyen en cómo se siente una persona."),
  ],
  app=[
      arith("Un grupo de ejemplo de 5 estudiantes creció 6, 7, 8, 7 y 7 cm en el año del estirón. ¿Cuántos centímetros crecieron en total?", "6+7+8+7+7", "Se suman todos los crecimientos."),
      arith("Con ese total de 35 cm entre 5 estudiantes, ¿cuál es el crecimiento promedio?", "35//5", "El promedio es el total dividido por 5."),
      ("Un curso tiene estudiantes de la misma edad. ¿Todos tendrán su estirón exactamente al mismo tiempo? Responde Sí o No.", "No", "Cada persona tiene su propio ritmo, aunque tenga la misma edad."),
  ],
  rea=[
      ("Un estudiante predice: «Quien sea más alto a los 10 años será más alto a los 20». ¿Qué falta para poder comprobarlo? A) Datos de estatura años después. B) La opinión de los amigos.", "A", "Sin datos de después no se comprueba."),
      ("Alguien dice que la pregunta «¿Quién cambió más?» es comprobable. ¿Qué le falta para serlo? Responde con una palabra.", "Un criterio", "Hay que definir qué se mide, por ejemplo centímetros."),
  ],
  cha=[
      ("Una predicción dice: «Entre los 13 y los 14 años el grupo crecerá menos que entre los 11 y los 12, porque el estirón ya habrá pasado». Datos de ejemplo: crecieron 8 cm entre los 11 y 12, y 4 cm entre los 13 y 14. ¿Se cumple la predicción? Responde Sí o No.", "Sí", "4 cm es menos que 8 cm."),
      ("Un grupo midió a 4 personas: crecieron 5, 9, 7 y 7 cm. ¿Cuál es el promedio?", "7", "(5 + 9 + 7 + 7) ÷ 4 = 7."),
  ],
  context=[("Dato de ejemplo. Un curso midió que en un año el promedio de crecimiento fue 7 cm y el máximo fue 10 cm. ¿Cuántos centímetros más que el promedio creció el máximo?", "3", "10 − 7 = 3.")],
  selfcheck=[("¿Qué tipo de preguntas se pueden comprobar?", "Las que se responden con datos", "Se miden o cuentan."), ("¿Qué efecto tienen las hormonas sobre el ánimo en la pubertad?", "Pueden hacer que las emociones cambien con más facilidad", "Influyen en cómo se siente una persona."), ("¿Se pueden comparar personas con respeto?", "Sí, con datos anónimos y sin juzgar", "Cada persona tiene su ritmo.")],
  open_task=task("Escribe una pregunta comprobable y una predicción con razón sobre el estirón, usando estos datos de ejemplo: un grupo creció en promedio 5 cm a los 10 años, 7 cm a los 11 y 8 cm a los 12. Calcula cuántos cm más creció a los 12 que a los 10.", "Pregunta: ¿cuánto crece un grupo en promedio por año entre los 10 y los 12? Predicción: a los 13 crecerá menos o igual que a los 12 porque el estirón suele pasar. Cálculo: 8 − 5 = 3 cm.", ["pregunta con algo medible", "predicción con razón", "cálculo correcto"], ["tres frases escritas"], ["predecir sin razón", "hablar de personas concretas"], "Pregunta cómo comprobaría la predicción con datos reales y anónimos."),
  reinforce="Escribe una pregunta comprobable sobre cambios de la pubertad.",
  extend="Explica por qué las comparaciones deben hacerse con datos y con respeto.")

L(OA5, 3,
  materials="Este cuaderno, lápiz y regla. Opcional: papel cuadriculado para el gráfico.",
  use="Aprenderé a representar con un modelo gráfico y con un esquema causal los cambios de la pubertad. Sirve para explicar por qué ocurren y cuánto cambian.",
  prior=["Sé que las hormonas ordenan los cambios de la pubertad.", "Sé leer una tabla de datos."],
  explain=[
      "Un modelo puede ser un esquema de causas. Primero, una zona del cerebro envía una señal que activa los ovarios o los testículos. Estos producen hormonas: estrógenos en las mujeres y testosterona en los hombres. Las hormonas viajan por la sangre y causan los cambios: crecimiento, vello, cambios en la voz o desarrollo de las mamas. El esquema es: cerebro → ovarios o testículos → hormonas → cambios.",
      "Otro modelo es un gráfico de líneas de crecimiento. En el eje horizontal se escribe la edad y en el vertical, la estatura. Cada punto es un dato. Si los puntos suben más rápido entre dos edades, hay un estirón. Un gráfico muestra de un vistazo cuándo creció más una persona de ejemplo.",
      "Los modelos tienen límites. El gráfico de una persona no representa a todas. El esquema causal no explica todas las diferencias, como la alimentación o la herencia familiar, que también influyen en la estatura. Por eso conviene decir qué muestra y qué no.",
  ],
  vocab=[("eje", "línea de un gráfico que indica la edad o la medida"), ("punto", "marca que representa un dato en un gráfico"), ("esquema causal", "dibujo con flechas que une causas y efectos"), ("herencia", "características que se reciben de la familia"), ("pendiente", "inclinación de una línea en un gráfico")],
  worked=[
      ("Leer el gráfico", "Un gráfico de ejemplo muestra 140 cm a los 10 años, 146 cm a los 11 y 155 cm a los 12. ¿Entre qué edades hay más inclinación?", ["Calculo el crecimiento: 146 − 140 = 6.", "Calculo el siguiente: 155 − 146 = 9.", "El mayor es entre 11 y 12."], "Entre los 11 y los 12 años"),
      ("Seguir el esquema causal", "Ordena: hormonas, cambios del cuerpo, ovarios o testículos, cerebro.", ["Empieza la señal del cerebro.", "Luego ovarios o testículos producen hormonas.", "Las hormonas causan los cambios."], "Cerebro → ovarios o testículos → hormonas → cambios del cuerpo"),
  ],
  mistakes=[
      ("Ubicar la edad en el eje vertical y la estatura en el horizontal.", "Por convención, la edad va en el eje horizontal.", "Escribe qué mide cada eje antes de poner puntos."),
      ("Pensar que el esquema explica todas las diferencias entre personas.", "También influyen la alimentación y la herencia.", "Menciona estos factores como límite."),
  ],
  rec=[
      ("En el gráfico de crecimiento, ¿qué va en el eje horizontal: la edad o la estatura?", "La edad", "Es la convención."),
      ("¿Qué producen los ovarios y los testículos que causan los cambios?", "Hormonas", "Viajan por la sangre."),
      ("Si los puntos suben más rápido, ¿hay más o menos crecimiento?", "Más", "Mayor inclinación indica más crecimiento."),
  ],
  und=[
      ("¿Qué indica un punto en el gráfico de crecimiento?", "La estatura a una edad", "Es un dato."),
      ("¿Qué órgano parte la señal en el esquema causal?", "El cerebro", "Activa ovarios o testículos."),
      ("¿Por qué el gráfico de una persona no representa a todas?", "Porque cada persona tiene su ritmo", "Los datos de uno no valen para todos."),
  ],
  app=[
      arith("Datos de ejemplo: 138 cm a los 10 años, 145 a los 11 y 151 a los 12. ¿Cuántos cm creció en total entre los 10 y los 12?", "151-138", "Se resta la estatura inicial de la final."),
      ("Con los mismos datos de ejemplo (138, 145 y 151 cm), ¿entre qué edades creció más? Responde 10–11 u 11–12.", "10–11", "Creció 7 cm y luego 6 cm."),
      arith("En un gráfico cada cuadrito vertical vale 2 cm. Entre las marcas de 140 cm y 150 cm, ¿cuántos cuadritos hay?", "(150-140)//2", "Se calcula la diferencia y se divide por el valor de un cuadrito."),
  ],
  rea=[
      ("Una compañera marcó la edad en el eje vertical. ¿Cuál es el error y cómo se corrige? Responde con una frase.", "La edad va en el eje horizontal", "Es la convención para gráficos de crecimiento."),
      ("Otro dice: «El esquema explica por qué una persona mide 170 cm». ¿Qué falta? A) Alimentación y herencia. B) El color del gráfico.", "A", "Esos factores también influyen."),
  ],
  cha=[
      ("Datos de ejemplo: 10 años, 138; 11, 145; 12, 156; 13, 162; 14, 164. ¿En qué año hubo el mayor crecimiento?", "Entre los 11 y los 12 años", "Creció 11 cm."),
      ("¿Cuál es un límite de un gráfico hecho con los datos de una sola persona? A) No representa a todas las personas. B) Tiene dos ejes.", "A", "Cada persona crece distinto."),
  ],
  context=[("Dato de ejemplo. Una persona midió 139 cm a los 10 años y 163 cm a los 14 años. ¿Cuántos cm creció en esos 4 años?", "24", "163 − 139 = 24.")],
  selfcheck=[("¿Qué muestra el esquema causal?", "Cómo el cerebro y las hormonas causan los cambios", "Cerebro → ovarios o testículos → hormonas → cambios."), ("¿Cómo se ve un estirón en un gráfico?", "Los puntos suben más rápido", "Hay más inclinación."), ("¿Qué límite tiene un gráfico de una persona?", "No representa a todas", "Cada una tiene su ritmo.")],
  open_task=task("Con estos datos de ejemplo de estatura haz un gráfico de puntos (edad en el eje horizontal, estatura en el vertical): 10 años, 136 cm; 11 años, 142; 12 años, 150; 13 años, 156; 14 años, 159. Une los puntos y escribe entre qué edades hay más inclinación y un límite.", "Crecimientos: 6, 8, 6, 3. Más inclinación entre los 11 y 12 años. Límite: son datos de una sola persona.", ["gráfico con ejes rotulados", "indica el tramo de mayor inclinación", "escribe un límite"], ["gráfico de puntos", "frases"], ["invertir los ejes", "olvidar el límite"], "Pregunta qué dato agregaría para saber si el estirón terminó."),
  reinforce="Dibuja el esquema causal de la pubertad con cuatro pasos.",
  extend="Explica por qué la alimentación y la herencia también influyen en la estatura.")

L(OA5, 4,
  materials="Este cuaderno y lápiz. Las tablas están escritas en los ejercicios.",
  use="Aprenderé a describir y comparar los cambios de la pubertad en mujeres y hombres con un criterio. Sirve para ver semejanzas y diferencias sin juzgar.",
  prior=["Conozco los cambios de la pubertad.", "Sé comparar con una tabla."],
  explain=[
      "Para comparar los cambios de la pubertad se usan criterios. Un criterio es si el cambio ocurre en ambos grupos o en uno solo. Cambios en ambos: estirón, vello en axilas y zona genital, piel más grasa, sudor con olor más fuerte y cambios de ánimo. Cambios de las mujeres: desarrollo de mamas, caderas más anchas y menarquia. Cambios de los hombres: voz más grave, vello facial, hombros más anchos y eyaculaciones.",
      "Otro criterio es la edad aproximada de inicio. En las mujeres comienza en promedio uno o dos años antes que en los hombres: más o menos entre los 8 y 13 años en ellas y entre los 9 y 14 años en ellos. Pero hay personas que empiezan antes o después y es normal. Un rango es la distancia entre la edad menor y la mayor.",
      "Comparar no es medir quién es mejor. Es describir cómo se parecen y cómo se diferencian los cambios para entender que la pubertad es una etapa natural. Una buena comparación usa un criterio por fila y dice un límite: los rangos son aproximados.",
  ],
  vocab=[("criterio", "regla para comparar"), ("rango", "distancia entre el valor menor y el mayor"), ("semejanza", "algo igual en ambos"), ("diferencia", "algo que cambia entre ambos"), ("natural", "propio de la vida humana")],
  worked=[
      ("Clasificar cambios", "Clasifica: estirón, menarquia, voz más grave. ¿Cuáles ocurren en ambos y cuál en uno solo?", ["Recuerdo que el estirón ocurre en todos.", "La menarquia es de mujeres.", "La voz más grave es de hombres."], "Estirón en ambos; menarquia en mujeres; voz más grave en hombres"),
      ("Calcular un rango", "Las mujeres inician entre los 8 y 13 años. ¿Cuál es el rango?", ["Edad menor: 8.", "Edad mayor: 13.", "Resto 13 − 8."], "5 años"),
  ],
  mistakes=[
      ("Pensar que quien empieza más tarde está «atrasado».", "Cada persona tiene su ritmo dentro de un rango amplio.", "Usa la palabra rango y no juzgues."),
      ("Poner un cambio de uno solo en la columna «ambos».", "Hay cambios propios de cada grupo.", "Revisa si el cambio ocurre en los dos."),
  ],
  rec=[
      ("¿El vello en las axilas aparece en ambos grupos: Sí o No?", "Sí", "Es un cambio de ambos."),
      ("¿La menarquia es un cambio de mujeres o de hombres?", "De mujeres", "Es la primera menstruación."),
      ("¿La voz más grave es un cambio más propio de los hombres o de las mujeres?", "De los hombres", "Es un cambio de la pubertad masculina."),
  ],
  und=[
      ("¿Cuál cambio ocurre en ambos grupos? A) Estirón. B) Menarquia.", "A", "La menarquia es solo de mujeres."),
      ("¿Qué es un rango?", "La distancia entre el valor menor y el mayor", "Se calcula restando."),
      ("¿Quién inicia en promedio antes, las mujeres o los hombres?", "Las mujeres", "En promedio, uno o dos años antes."),
  ],
  app=[
      arith("Los hombres inician entre los 9 y 14 años. ¿Cuál es el rango en años?", "14-9", "Se resta la edad menor de la mayor."),
      ("Cuenta cuántos de estos cambios ocurren en ambos grupos: estirón, mamas, vello en axilas, voz grave, piel grasa.", "3", "Son estirón, vello en axilas y piel grasa."),
      arith("En una tabla hay 5 cambios de ambos, 3 de mujeres y 4 de hombres. ¿Cuántos cambios hay en total?", "5+3+4", "Se suman las tres columnas."),
  ],
  rea=[
      ("Un compañero dice que quien empieza a los 13 años en las mujeres está atrasada. ¿Es correcto? Responde Sí o No y explica.", "No; 13 está dentro del rango normal", "El rango va de 8 a 13."),
      ("Una tabla dice que la menarquia aparece en ambos grupos. ¿Qué error tiene?", "Es solo de mujeres", "Es la primera menstruación."),
  ],
  cha=[
      ("Un grupo estima que, en promedio, los hombres comienzan 1 año después que las mujeres. Si en las mujeres el promedio es 10 años, ¿cuál es en los hombres?", "11", "10 + 1 = 11."),
      ("Marca la mejor conclusión. A) Las mujeres cambian mejor que los hombres. B) Algunos cambios se comparten y otros son propios de cada grupo.", "B", "La A juzga y la B describe con un criterio."),
  ],
  context=[("Dato de ejemplo. En una tabla de clase hay 9 cambios en total: 5 son de ambos y el resto son propios de un grupo. ¿Cuántos son propios de un grupo?", "4", "9 − 5 = 4.")],
  selfcheck=[("¿Qué cambios ocurren en ambos grupos?", "Estirón, vello, piel grasa, sudor y cambios de ánimo", "Son cambios que aparecen en todos."), ("¿Qué cambios son solo de las mujeres?", "Mamas, caderas más anchas y menarquia", "Son propios de ellas."), ("¿Por qué se dice que los rangos son aproximados?", "Porque cada persona tiene su ritmo", "Hay variación normal.")],
  open_task=task("Completa una tabla de tres columnas (ambos, solo mujeres, solo hombres) con estos cambios: estirón, voz más grave, menarquia, vello en axilas, caderas más anchas, vello facial, piel más grasa. Escribe además el rango de inicio de cada grupo y un límite.", "Ambos: estirón, vello en axilas, piel más grasa. Mujeres: menarquia, caderas más anchas. Hombres: voz más grave, vello facial. Rangos: mujeres 8 a 13 años (5 años); hombres 9 a 14 (5 años). Límite: los rangos son aproximados.", ["siete cambios bien ubicados", "dos rangos correctos", "escribe un límite"], ["tabla de tres columnas"], ["poner un cambio en la columna equivocada", "juzgar quién es mejor"], "Pregunta por qué un cambio queda en la columna «ambos»."),
  reinforce="Escribe tres cambios que ocurran en ambos grupos.",
  extend="Explica por qué la pubertad se considera una etapa natural del desarrollo.")

# ---------------------------------------------------------------- OA 06
L(OA6, 1,
  materials="Este cuaderno y lápiz. Opcional: un reloj con segundero para tomar el pulso. Los datos están escritos en los ejercicios.",
  use="Aprenderé los beneficios de la actividad física y la higiene en la pubertad y a separar lo observado de lo supuesto. Sirve para cuidar mi cuerpo.",
  prior=["Sé que el corazón late y que el pulso se puede contar.", "Sé que una observación se mide o se cuenta."],
  explain=[
      "La actividad física es cualquier movimiento del cuerpo que gasta energía, como correr, andar en bicicleta o jugar. Hacerla de forma regular, es decir, varios días a la semana, fortalece el corazón, los músculos y los huesos. También ayuda a dormir mejor, a concentrarse y a sentirse con más ánimo. Las niñas y los niños de tu edad necesitan, en total, al menos 60 minutos diarios de actividad física de intensidad moderada a fuerte.",
      "Durante la pubertad el cuerpo suda más y su olor cambia. Las bacterias de la piel transforman el sudor en un olor más fuerte. Por eso la higiene corporal es muy importante: ducharse todos los días con agua y jabón, lavar bien axilas y zona genital externa, cambiarse la ropa interior y la ropa deportiva, lavarse la cara y el cabello, y lavarse los dientes después de comer. Las personas que menstrúan deben cambiar su toalla higiénica o producto cada pocas horas.",
      "Para saber si el ejercicio cambia algo en el cuerpo se pueden hacer mediciones. El pulso, es decir cuántas veces late el corazón en un minuto, se puede contar en la muñeca. Una observación es «mi pulso subió de 80 a 130 latidos por minuto». Una interpretación es «mi corazón trabaja más para llevar oxígeno a los músculos». Esa explicación es posible, pero necesita más evidencia.",
  ],
  vocab=[("actividad física", "movimiento del cuerpo que gasta energía"), ("pulso", "número de latidos del corazón en un minuto"), ("higiene corporal", "hábitos de limpieza del cuerpo"), ("intensidad", "qué tan fuerte es el esfuerzo"), ("regular", "que se hace de forma repetida, todas las semanas")],
  worked=[
      ("Calcular el cambio del pulso", "En un registro de ejemplo, el pulso en reposo es 78 latidos por minuto y después de correr 5 minutos es 126. ¿Cuánto subió?", ["Identifico el final: 126.", "Identifico el inicial: 78.", "Resto 126 − 78."], "Subió 48 latidos por minuto"),
      ("Observación o interpretación", "Dos frases: (1) «Mi pulso subió de 78 a 126». (2) «Mi corazón está cansado». ¿Cuál es la observación?", ["Pregunto qué frase se midió.", "La frase 1 tiene números.", "La frase 2 supone algo."], "La frase 1"),
  ],
  mistakes=[
      ("Pensar que basta ducharse una vez a la semana en la pubertad.", "El sudor aumenta y hay más olor y riesgo de irritación.", "Ducharse a diario y cambiarse la ropa."),
      ("Decir que hacer deporte un día largo sirve igual que un poco cada día.", "La actividad regular es la que da los beneficios.", "Reparte la actividad en varios días."),
  ],
  rec=[
      ("¿Cuántos minutos diarios de actividad física se recomiendan, como mínimo, para tu edad: 60 o 10?", "60", "Es la recomendación para niños y niñas."),
      ("¿Con qué se cuentan los latidos del corazón en un minuto: con el pulso o con el peso?", "Con el pulso", "El pulso mide latidos por minuto."),
      ("¿Hay más olor corporal por el sudor en la pubertad: Sí o No?", "Sí", "Las glándulas de sudor se activan más."),
  ],
  und=[
      ("¿Cuál es una observación? A) El pulso subió de 80 a 130. B) El corazón está cansado.", "A", "Tiene números medidos."),
      ("¿Para qué sirve ducharse todos los días en la pubertad?", "Para eliminar sudor y bacterias que causan olor", "Disminuye el olor."),
      ("¿Qué órganos fortalece la actividad física regular?", "El corazón, los músculos y los huesos", "Son los beneficios principales."),
  ],
  app=[
      arith("Un registro de ejemplo muestra un pulso de 84 en reposo y 132 después de saltar. ¿Cuántos latidos por minuto subió?", "132-84", "Se resta el pulso en reposo del pulso final."),
      arith("Se cuentan 18 latidos en 15 segundos. ¿Cuál es el pulso en un minuto?", "18*4", "Un minuto tiene cuatro períodos de 15 segundos."),
      ("¿Cuál de estas es actividad física? Correr, ver televisión, andar en bicicleta, dormir. Cuenta cuántas son.", "2", "Correr y andar en bicicleta."),
  ],
  rea=[
      ("Una estudiante dice: «Como mi pulso subió, el ejercicio me hizo mal». ¿Es una conclusión válida? Responde Sí o No y explica.", "No; es normal que suba con el ejercicio", "El corazón trabaja más para llevar oxígeno."),
      ("Dos personas hacen ejercicio. A suda y se cambia de ropa; B no se cambia. Después de unas horas, ¿cuál tendrá más olor corporal probablemente?", "B", "La ropa con sudor mantiene bacterias y olor."),
  ],
  cha=[
      ("Un compañero hizo 3 días de 20 minutos y otro 7 días de 10 minutos. ¿Quién suma más minutos en la semana?", "El segundo", "60 minutos contra 70 minutos."),
      ("¿Cuál es una interpretación prudente de por qué el pulso sube con el ejercicio? A) Es posible que el corazón lata más rápido para llevar oxígeno a los músculos. B) Es seguro que el corazón se está dañando.", "A", "La A se presenta como posible y coincide con lo que se sabe."),
  ],
  context=[("Dato de ejemplo. Una estudiante registró 25 minutos de actividad el lunes, 35 el miércoles y 40 el sábado. ¿Cuántos minutos hizo en total?", "100", "25 + 35 + 40 = 100.")],
  selfcheck=[("¿Qué beneficios tiene la actividad física regular?", "Fortalece corazón, músculos y huesos, y ayuda a dormir y a concentrarse", "Mejora la salud."), ("¿Por qué la higiene es más importante en la pubertad?", "Porque aumenta el sudor y cambia su olor", "Las bacterias lo transforman."), ("¿Qué es el pulso?", "El número de latidos del corazón por minuto", "Se cuenta en la muñeca.")],
  open_task=task("Lee estos datos de ejemplo: en reposo el pulso es 80; tras 3 minutos de saltar la cuerda es 128; tras 5 minutos de descanso es 88. Escribe tres observaciones con números, una interpretación y tres hábitos de higiene para después de hacer ejercicio. Si quieres, mide tu pulso en 15 segundos y multiplica por 4.", "Observaciones: subió 48; bajó 40 al descansar; después del descanso aún es 8 más que en reposo. Interpretación: el corazón trabajó más durante el ejercicio. Higiene: ducharse, cambiarse la ropa, lavarse las manos.", ["tres observaciones con números", "una interpretación rotulada", "tres hábitos de higiene"], ["lista escrita"], ["mezclar observación con interpretación", "olvidar la higiene"], "Pregunta cómo supo que una frase era interpretación."),
  reinforce="Escribe tres actividades físicas que puedas hacer en casa.",
  extend="Explica por qué la actividad regular da más beneficios que una sola vez.")

L(OA6, 2,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a formular preguntas y predicciones sobre actividad física e higiene. Sirve para pensar cómo comprobar que un hábito hace bien.",
  prior=["Conozco los beneficios de la actividad física.", "Sé qué hábitos de higiene se necesitan en la pubertad."],
  explain=[
      "Una pregunta comprobable puede ser: «¿Cuántos latidos por minuto baja el pulso en reposo después de 8 semanas de actividad regular?». Se responde midiendo el pulso. En cambio, «¿Qué deporte es el mejor?» depende de gustos. Para comprobar un efecto, se mide antes y después.",
      "Una predicción dice qué ocurrirá y por qué: «Si una persona hace actividad física 5 días a la semana durante 8 semanas, su pulso en reposo probablemente bajará un poco, porque su corazón se fortalece y bombea más sangre en cada latido». Otra predicción sobre higiene: «Si no se cambia la ropa deportiva sudada, tendrá más olor, porque las bacterias descomponen el sudor».",
      "Las predicciones deben ser prudentes, porque el cuerpo de cada persona responde distinto y hay otros factores, como la alimentación y el sueño. Si una medición no cambia, se revisa la idea y se buscan más datos. Nunca se ajustan los números para que coincidan.",
  ],
  vocab=[("pulso en reposo", "latidos por minuto sentado y tranquilo"), ("fortalecer", "hacer más fuerte"), ("bacteria", "ser vivo muy pequeño, de una célula"), ("medir antes y después", "comparar el valor inicial con el final"), ("factor", "cosa que puede influir en un resultado")],
  worked=[
      ("Pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Cuántos minutos de actividad hizo un grupo cada semana? B) ¿Qué actividad es más aburrida?", ["Busco una pregunta con números.", "En A se miden minutos.", "En B es una opinión."], "A"),
      ("Predicción con razón", "Una persona se ducha y se cambia de ropa después de hacer deporte. ¿Qué predices sobre el olor y por qué?", ["Con la ducha se elimina sudor y bacterias.", "Con ropa limpia no hay sudor acumulado.", "Escribo la predicción con razón."], "Probablemente tendrá menos olor, porque se eliminan el sudor y las bacterias"),
  ],
  mistakes=[
      ("Predecir «todos mejorarán igual».", "El cuerpo de cada persona responde distinto.", "Usa «probablemente» y agrega factores que influyen."),
      ("Cambiar los números para que coincidan con la predicción.", "Se deja de hacer ciencia: los datos mandan.", "Si no coinciden, corrige la idea, no el dato."),
  ],
  rec=[
      ("¿Se mide el pulso en reposo con la persona sentada y tranquila o corriendo?", "Sentada y tranquila", "Es el valor de reposo."),
      ("Fortalecer el corazón, ¿lo hace más fuerte o más débil?", "Más fuerte", "Eso significa fortalecer."),
      ("¿Se mide antes y después para comparar: Sí o No?", "Sí", "Así se ve el cambio."),
  ],
  und=[
      ("¿Cuál predicción tiene razón? A) El pulso en reposo bajará, porque el corazón se fortalece. B) El pulso bajará porque sí.", "A", "La A explica el motivo."),
      ("¿Por qué una predicción debe ser prudente?", "Porque cada cuerpo responde distinto y hay otros factores", "Evita afirmar demasiado."),
      ("Si una medición no coincide con la predicción, ¿qué se hace: cambiar el dato o revisar la idea?", "Revisar la idea", "Los datos no se cambian."),
  ],
  app=[
      arith("Un grupo de ejemplo hace 30 minutos de actividad física 5 días a la semana. ¿Cuántos minutos hace en una semana?", "30*5", "Se multiplican los minutos por los días."),
      arith("Si lo hacen durante 8 semanas, ¿cuántos minutos suman en total?", "(30*5)*8", "Cada semana suman 30 × 5 minutos."),
      ("Una persona con pulso en reposo de 80 predice que bajará 4 latidos tras 8 semanas. ¿Cuál será el pulso si se cumple la predicción?", "76", "80 − 4 = 76."),
  ],
  rea=[
      ("Luz predice que si no se lava las manos antes de comer, se enfermará siempre. ¿Qué palabra de la predicción es demasiado fuerte?", "Siempre", "No es seguro que ocurra en todos los casos."),
      ("Un estudiante mide su pulso una sola vez después de correr y concluye que el ejercicio no sirve porque estaba cansado. ¿Qué error cometió?", "Midió solo una vez y no comparó con el reposo", "Faltaban más mediciones y la comparación."),
  ],
  cha=[
      ("¿Cuál pregunta sobre higiene es comprobable? A) ¿Cuántas veces al día se lavan las manos los estudiantes del curso? B) ¿Qué jabón es más simpático?", "A", "Las veces se pueden contar."),
      ("Si el pulso en reposo bajó de 82 a 76, ¿cuánto bajó?", "6", "82 − 76 = 6."),
  ],
  context=[("Dato de ejemplo. Un curso registró que 22 estudiantes se lavan los dientes 3 veces al día y 6 lo hacen 2 veces. ¿Cuántos estudiantes se lavan los dientes al menos 2 veces?", "28", "22 + 6 = 28.")],
  selfcheck=[("¿Qué se hace para comprobar un efecto?", "Medir antes y después", "Así se compara."), ("¿Qué lleva una buena predicción?", "Lo que ocurrirá y su razón", "Así se puede comprobar después."), ("¿Se pueden cambiar los datos para que coincidan?", "No", "Los datos mandan.")],
  open_task=task("Escribe una pregunta comprobable y una predicción con razón sobre actividad física y una pregunta comprobable y una predicción con razón sobre higiene. Usa estos datos de ejemplo como apoyo: pulso en reposo 82; 5 días de 30 minutos durante 8 semanas.", "Pregunta 1: ¿cuántos latidos baja el pulso en 8 semanas? Predicción: bajará un poco porque el corazón se fortalece. Pregunta 2: ¿cuántas veces al día se lavan las manos? Predicción: bajarán las infecciones porque se eliminan microbios.", ["dos preguntas comprobables", "dos predicciones con razón", "usa números"], ["cuatro frases"], ["predecir sin razón", "preguntar por gustos"], "Pregunta qué factor, aparte del ejercicio, podría influir."),
  reinforce="Escribe una predicción con razón sobre el sudor y el olor.",
  extend="Explica por qué se mide antes y después de una actividad.")

L(OA6, 3,
  materials="Este cuaderno y lápiz. Opcional: papel para armar el calendario semanal.",
  use="Aprenderé a modelar con un calendario y con un esquema los beneficios de la actividad física y de la higiene. Sirve para planificar mis hábitos.",
  prior=["Sé que se recomiendan 60 minutos diarios de actividad física.", "Sé qué hábitos de higiene necesita el cuerpo en la pubertad."],
  explain=[
      "Un calendario semanal es un modelo de hábitos. En cada día se anotan los minutos de actividad física. Una semana completa con 60 minutos diarios suma 420 minutos. El calendario ayuda a ver si se cumple la recomendación y en qué días falta.",
      "Un esquema causal muestra cómo el hábito produce un beneficio: actividad física → corazón y músculos más fuertes → más resistencia, mejor sueño y mejor ánimo. Y para la higiene: sudor + bacterias → olor y posibles irritaciones; ducha, ropa limpia y desodorante, si se usa → menos olor. El esquema simplifica, pero ayuda a entender por qué un hábito sirve.",
      "El modelo tiene límites. El calendario no dice cuánto esfuerzo hizo cada día, y el esquema no incluye otros factores, como la alimentación o el sueño. Al construir un modelo conviene escribir qué muestra y qué no muestra, y evitar compararse con otras personas.",
  ],
  vocab=[("calendario semanal", "tabla con los siete días de la semana"), ("resistencia", "capacidad de mantener un esfuerzo por más tiempo"), ("desodorante", "producto para disminuir el olor del sudor"), ("hábito", "acción que se repite todos los días o semanas"), ("esquema causal", "dibujo con flechas de causa y efecto")],
  worked=[
      ("Sumar minutos", "Un calendario de ejemplo anota 40, 60, 0, 50, 70, 30 y 20 minutos. ¿Cuántos minutos suma en la semana?", ["Escribo los siete valores.", "Los sumo uno a uno.", "40 + 60 + 0 + 50 + 70 + 30 + 20."], "270 minutos"),
      ("Seguir una flecha causal", "Ordena: más resistencia, actividad física, corazón y músculos más fuertes.", ["Parte la causa: actividad física.", "Luego se fortalecen corazón y músculos.", "Finalmente hay más resistencia."], "Actividad física → corazón y músculos más fuertes → más resistencia"),
  ],
  mistakes=[
      ("Sumar solo los días con actividad y olvidar los días con 0.", "Los días con 0 también cuentan en el calendario.", "Escribe los siete días antes de sumar."),
      ("Pensar que el calendario muestra qué tan fuerte fue el esfuerzo.", "Solo registra minutos.", "Agrega una nota de esfuerzo si quieres."),
  ],
  rec=[
      ("Una semana tiene ______ días. Completa con 7 o 5.", "7", "Una semana completa tiene siete días."),
      ("¿Qué se anota en el calendario de ejemplo: los minutos o los colores?", "Los minutos", "Muestran la actividad."),
      ("Según el esquema, ¿la higiene disminuye el olor: Sí o No?", "Sí", "Se eliminan sudor y bacterias."),
  ],
  und=[
      ("¿Cuántos minutos suma una semana si se cumplen 60 diarios?", "420", "60 × 7 = 420."),
      ("¿Qué muestra un esquema causal?", "Cómo un hábito produce un beneficio", "Usa flechas de causa y efecto."),
      ("¿Qué no muestra un calendario de minutos?", "Cuánto esfuerzo se hizo", "Solo registra tiempo."),
  ],
  app=[
      arith("Un calendario de ejemplo anota 45, 60, 30, 55, 20, 0 y 80 minutos. ¿Cuántos minutos suma en la semana?", "45+60+30+55+20+0+80", "Se suman los siete días."),
      arith("A esa persona le faltan para cumplir los 420 minutos semanales. Si suma 290, ¿cuántos minutos le faltan?", "420-290", "Se resta lo hecho de la meta."),
      ("¿Cuántos días tienen 60 minutos o más en este calendario: 40, 60, 0, 70, 90, 30, 60?", "4", "Son los días de 60, 70, 90 y 60."),
  ],
  rea=[
      ("Un estudiante suma 400 minutos en la semana y dice «cumplí todos los días 60 minutos». ¿Es correcto? Responde Sí o No y explica.", "No; 60 por 7 son 420", "Con 400 hay días con menos de 60."),
      ("Dos personas suman 300 minutos. Una los hizo en 3 días y otra en 7 días. ¿Cuál cumple mejor el hábito regular?", "La que los hizo en 7 días", "La actividad regular se reparte en la semana."),
  ],
  cha=[
      ("Un calendario de ejemplo tiene 35, 50, 0, 60, 25, 70 y 40 minutos. ¿Cuántos minutos le faltan para llegar a 420?", "140", "La suma es 280 y 420 − 280 = 140."),
      ("¿Qué no muestra un calendario de minutos? A) El esfuerzo hecho cada día. B) Cuántos días tiene la semana.", "A", "Solo registra el tiempo."),
  ],
  context=[("Dato de ejemplo. Una estudiante hizo 50 minutos de actividad por día durante 6 días. ¿Cuántos minutos suma?", "300", "50 × 6 = 300.")],
  selfcheck=[("¿Cuántos minutos suma una semana si haces 60 al día?", "420", "60 × 7."), ("¿Qué muestra el esquema causal?", "Cómo un hábito produce un beneficio", "Se dibuja con flechas."), ("¿Qué límite tiene un calendario?", "No muestra el esfuerzo", "Solo registra minutos.")],
  open_task=task("Arma un calendario semanal con estos datos de ejemplo: lunes 30 minutos de caminata, martes 45 de bicicleta, miércoles 0, jueves 60 de fútbol, viernes 20 de baile, sábado 80 de juegos, domingo 25 de caminata. Suma los minutos, compáralos con 420 y escribe un esquema causal de dos pasos para un beneficio.", "Total: 260 minutos. Faltan 160. Esquema: actividad regular → corazón más fuerte → más resistencia. Límite: no muestra el esfuerzo.", ["suma correcta", "compara con 420", "esquema de dos pasos"], ["calendario escrito", "esquema"], ["olvidar el día con 0", "esquema sin flechas"], "Pregunta qué día podría sumar más minutos."),
  reinforce="Arma un calendario de siete días con actividades que te gusten.",
  extend="Explica por qué la actividad física debe ser regular.")

L(OA6, 4,
  materials="Este cuaderno y lápiz. Las tablas están escritas en los ejercicios.",
  use="Aprenderé a comparar hábitos con un criterio y a decidir qué cambios ayudan más. Sirve para evaluar mis rutinas de actividad y de higiene.",
  prior=["Conozco la recomendación de 60 minutos diarios.", "Conozco los hábitos de higiene de la pubertad."],
  explain=[
      "Para comparar rutinas se usa un criterio. En actividad física, el criterio puede ser cumplir 420 minutos por semana. En higiene, el criterio puede ser una lista de hábitos: ducha diaria, ropa interior limpia, lavado de manos antes de comer y después de ir al baño, y lavado de dientes después de comer. Se cuenta cuántos hábitos de la lista se cumplen.",
      "Por ejemplo, la persona A suma 350 minutos y la persona B suma 450. Con el criterio de 420, B cumple y A no. A le faltan 70 minutos. En higiene, si una rutina cumple 4 de 5 hábitos, le falta uno. La comparación indica qué cambiar: en vez de culpar, se propone un cambio concreto.",
      "Los criterios tienen límites. 420 minutos es una recomendación para la mayoría de las personas, y algunas necesitan adaptaciones por salud. Si alguien tiene una condición médica, un profesional debe orientarla. Una conclusión sólida dice qué criterio se usó y qué no mide.",
  ],
  vocab=[("criterio", "regla para comparar y decidir"), ("meta", "cantidad o resultado que se quiere lograr"), ("rutina", "conjunto de hábitos que se repiten"), ("recomendación", "consejo basado en evidencia"), ("adaptación", "cambio para que una actividad se ajuste a una persona")],
  worked=[
      ("Comparar con la meta", "Persona A suma 350 minutos y persona B suma 450 (datos de ejemplo). Con la meta de 420, ¿quién cumple y cuánto falta al otro?", ["Comparo 450 con 420: cumple.", "Comparo 350 con 420: no cumple.", "Resto 420 − 350."], "B cumple; a A le faltan 70 minutos"),
      ("Contar hábitos", "Una rutina cumple: ducha diaria, lavar manos, dientes, pero no cambia la ropa interior ni la deportiva. De 5 hábitos (ducha, manos, dientes, ropa interior, ropa deportiva), ¿cuántos cumple?", ["Marco los que cumple: ducha, manos, dientes.", "Cuento tres.", "Los otros dos no se cumplen."], "Cumple 3 de 5"),
  ],
  mistakes=[
      ("Culpar a la persona que no llega a la meta.", "La comparación debe proponer un cambio, no juzgar.", "Escribe qué cambio pequeño ayudaría."),
      ("Usar el mismo criterio para todas las personas sin considerar adaptaciones.", "Algunas personas necesitan orientación profesional.", "Menciona que existen adaptaciones."),
  ],
  rec=[
      ("¿Cuál es la meta semanal de minutos para tu edad: 420 o 100?", "420", "60 minutos por 7 días."),
      ("¿Se compara con un criterio o con el color de la ropa?", "Con un criterio", "Define cómo decidir."),
      ("Si se cumplen 4 de 5 hábitos, ¿falta uno: Sí o No?", "Sí", "5 − 4 = 1."),
  ],
  und=[
      ("¿Quién cumple la meta de 420: quien suma 380 o quien suma 430?", "Quien suma 430", "430 supera 420."),
      ("¿Qué debe hacer una comparación: proponer un cambio o culpar?", "Proponer un cambio", "La finalidad es mejorar."),
      ("¿Por qué algunas personas necesitan adaptaciones?", "Porque tienen condiciones de salud distintas", "Un profesional las orienta."),
  ],
  app=[
      arith("Una persona de ejemplo suma 320 minutos en una semana. ¿Cuántos le faltan para llegar a 420?", "420-320", "Se resta lo hecho de la meta."),
      arith("Otra persona suma 70 minutos por día durante 6 días. ¿Cuántos minutos suma?", "70*6", "Se multiplican minutos por días."),
      ("Persona A suma 400 minutos y persona B suma 430. Con la meta de 420, ¿cuántas personas cumplen?", "1", "Solo B supera 420."),
  ],
  rea=[
      ("Una rutina cumple 2 de 5 hábitos de higiene y otra cumple 4 de 5. ¿Cuál necesita más cambios?", "La que cumple 2", "Le faltan 3 hábitos."),
      ("Alguien dice que, si no llega a 420 minutos una semana, nunca será saludable. ¿Qué palabra es demasiado fuerte?", "Nunca", "Un solo registro no decide la salud."),
  ],
  cha=[
      ("Una semana suma 300 minutos y la siguiente 360. ¿Cuántos minutos más sumó la segunda?", "60", "360 − 300 = 60."),
      ("Marca la mejor conclusión. A) Esta persona es perezosa. B) Con 330 minutos, le faltan 90 minutos para la meta.", "B", "La B usa un criterio y un dato."),
  ],
  context=[("Dato de ejemplo. Un curso de 30 estudiantes anotó que 18 cumplieron la meta semanal. ¿Cuántos no la cumplieron?", "12", "30 − 18 = 12.")],
  selfcheck=[("¿Cuál es la meta semanal de minutos?", "420", "60 por 7."), ("¿Para qué sirve comparar con un criterio?", "Para decidir qué cambiar", "Orienta la mejora."), ("¿Qué debe hacer una persona con una condición de salud antes de seguir la meta?", "Consultar a un profesional que la oriente", "Puede necesitar una adaptación.")],
  open_task=task("Compara estas dos rutinas de ejemplo. Persona 1: 30, 50, 60, 20, 0, 80, 45 minutos y cumple 3 de 5 hábitos de higiene (ducha, manos, dientes, ropa interior, ropa deportiva). Persona 2: 60 minutos todos los días y cumple 5 de 5. Calcula los minutos de cada una, compáralos con 420 y propone un cambio concreto para la persona 1.", "Persona 1: 285 minutos; faltan 135; 3 de 5 hábitos. Persona 2: 420 minutos y 5 de 5. Cambio: sumar 20 minutos diarios y cambiarse la ropa deportiva.", ["suma correcta de ambas", "compara con la meta", "propone un cambio concreto"], ["cálculos escritos", "propuesta"], ["culpar a la persona", "sumas incorrectas"], "Pregunta qué cambio pequeño sería fácil de mantener."),
  reinforce="Calcula cuántos minutos hace una persona que suma 50 minutos por 5 días.",
  extend="Explica por qué una meta debe adaptarse a cada persona.")

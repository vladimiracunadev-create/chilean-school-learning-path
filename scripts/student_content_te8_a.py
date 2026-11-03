"""Cuaderno del estudiante, 8.º básico Tecnología: OA 01 (oportunidades personales, grupales y locales para crear productos), clases 1 a 4.

Seguridad: las tareas son de lectura, cálculo y escritura; no se manipulan herramientas ni materiales.
Cifras enteras. Los casos, las encuestas y los precios son inventados («de ejemplo») para practicar y no nombran marcas ni personas reales.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE08 OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    def conv(i):
        return i if isinstance(i, dict) else ex(*i)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [conv(i) for i in R], "understand": [conv(i) for i in C], "apply": [conv(i) for i in A], "reason": [conv(i) for i in Z], "challenge": [conv(i) for i in D]},
        context=[conv(ctx)], selfcheck=[conv(i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01, clase 1
reg(
    OA1, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus respuestas.",
    use="Aprenderé a distinguir si una necesidad es personal, grupal o local, a separarla de un simple deseo y a decidir si pide crear un producto tecnológico. Sirve para elegir bien el problema antes de diseñar.",
    prior=["Sé que una necesidad es algo que falta o que no funciona bien.", "Sé que un usuario es quien usa un objeto o servicio.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "Una oportunidad, en Tecnología, es una situación que se puede mejorar creando un producto tecnológico. Un producto tecnológico es un objeto, un sistema o un servicio creado para resolver una necesidad; puede ser un cartel con un mapa, un soporte de cartón o una aplicación. No siempre necesita pantallas ni enchufes.",
        "Según a cuántas personas afecta, una necesidad puede ser personal (una persona), grupal (un grupo que se conoce, como un curso, un equipo o una familia) o local (las personas que comparten un lugar, como un pasaje, una población o una escuela). Una necesidad es algo que falta para estar seguro, para funcionar o para participar. Un deseo es algo que se quiere, pero cuya falta no impide hacer lo importante.",
        "No toda necesidad pide un producto. Si lo que falta es una regla o un acuerdo entre personas, se resuelve conversando. Si lo que falta es un objeto, un sistema o un servicio, hay una oportunidad tecnológica. Para mostrar que una necesidad local es real se usan datos. Un porcentaje dice cuántas personas de cada 100 lo viven: 30 de 40 personas es 75 %, porque 30 ÷ 40 × 100 = 75.",
    ],
    vocab=[("oportunidad", "situación que se puede mejorar creando un producto"), ("producto tecnológico", "objeto, sistema o servicio creado para resolver una necesidad"), ("necesidad local", "la que afecta a quienes comparten un lugar"), ("deseo", "algo que se quiere, pero no impide hacer lo importante"), ("porcentaje", "cuántas personas de cada 100")],
    worked=[
        ("Clasificar el alcance", "Un pasaje de 12 casas no tiene luz en la noche porque los focos del poste se quemaron. ¿Qué alcance tiene la necesidad?", ["Pregunto a cuántas personas afecta: a todas las que usan el pasaje.", "Comparten un lugar, no son un grupo cerrado: es local."], "Es una necesidad local"),
        ("Decidir si pide un producto", "En un curso, los estudiantes se atrasan porque nadie sabe cuándo termina el recreo en el patio trasero, donde no se escucha el timbre. ¿Pide un producto tecnológico?", ["Lo que falta es una forma de avisar la hora en ese lugar: un objeto o servicio.", "No es un problema de reglas, sino de falta de un medio."], "Sí, hay una oportunidad tecnológica"),
    ],
    mistakes=[
        ("Pensar que un producto tecnológico siempre es un aparato electrónico.", "Se confunde tecnología con electrónica.", "Un cartel, un soporte o un servicio también son productos tecnológicos."),
        ("Llamar necesidad a todo lo que se quiere.", "Un deseo no impide hacer lo importante.", "Pregunta qué pasa si falta: si no pasa nada grave, es un deseo."),
    ],
    R=[
        ("Clasifica según su alcance (personal, grupal o local): «los vecinos de una población no tienen dónde dejar la basura y se acumula en la esquina».", "Local", "Afecta a las personas que comparten un lugar, la población."),
        ("¿Qué es un producto tecnológico? A) un objeto, sistema o servicio creado para resolver una necesidad B) solo un aparato con pantalla o enchufe", "A", "Incluye objetos simples, sistemas y servicios, no solo aparatos electrónicos."),
        ("Tomás escribe: «Quiero una mochila con luces de colores». ¿Es una necesidad o un deseo?", "Un deseo", "Sin las luces de colores puede cargar sus cosas igual."),
    ],
    C=[
        ("¿Cuál es una necesidad local? A) a una estudiante se le perdió su regla B) en la plaza del barrio faltan basureros y se llena de papeles", "B", "La segunda afecta a quienes comparten la plaza; la primera, a una sola persona."),
        ("Dos compañeros discuten cada día por quién se sienta junto a la ventana. ¿Se resuelve mejor con un producto tecnológico o con un acuerdo entre ellos?", "Con un acuerdo", "Lo que falta es una regla de convivencia, no un objeto ni un servicio."),
        ("¿Cuál es la diferencia entre una necesidad grupal y una local? A) la grupal afecta a un grupo conocido y la local a quienes comparten un lugar B) la grupal ocurre en la casa y la local siempre en la escuela", "A", "El alcance se define por quiénes están afectados y no por el edificio donde ocurre."),
    ],
    A=[
        arith("En una encuesta de ejemplo a 40 vecinos de un pasaje, 28 dicen que lo que más les falta es iluminación en la noche. ¿Qué porcentaje de los vecinos lo dice?", "28*100//40", "Se calcula cuántos de cada 100 piensan eso.", " %"),
        ("Escribe en orden el alcance (P personal, G grupal o L local): (1) a una niña le queda corto el cable de su cargador, (2) el equipo de básquetbol de la escuela no tiene dónde guardar los balones, (3) en una feria de barrio no hay baños accesibles para personas en silla de ruedas.", "1 P, 2 G, 3 L", "La primera afecta a una persona, la segunda a un grupo conocido y la tercera a quienes comparten la feria."),
        ("Separa necesidad de deseo: (1) faroles para un pasaje sin luz, (2) un parlante de colores para la sala, (3) una rampa en la entrada de la sede vecinal para quien usa andador. ¿Cuáles son necesidades?", "1 y 3", "Sin los faroles y sin la rampa se pierde seguridad o acceso; el parlante es un gusto."),
    ],
    Z=[
        ("Un grupo escribe: «Necesitamos una aplicación para el curso». Otro: «Necesitamos que todos sepan las tareas a tiempo, aunque estén ausentes». ¿Cuál enuncia la necesidad y cuál ya propone una solución?", "El segundo enuncia la necesidad; el primero ya propone la solución", "La necesidad dice qué lograr; nombrar la aplicación ya es elegir una solución."),
        ("Una vecina propone una aplicación para avisar cortes de agua, pero 15 de las 20 familias del pasaje no tienen celular con internet. ¿Qué falla tiene esa idea como producto?", "No llega a la mayoría de los usuarios", "Quince de veinte es el 75 %: la mayoría no podría usarla."),
    ],
    D=[
        arith("En un barrio se consultó a 5 grupos de 24 vecinos. 90 dijeron que hay poca luz y 18 que no hay ningún problema. ¿Cuántos no dijeron ninguna de las dos cosas?", "5*24-90-18", "Se calcula el total consultado y se restan los dos grupos.", " vecinos"),
        ("Regla: se atiende primero la necesidad que afecta a más personas y, si empatan, la de riesgo más alto. X: 45 personas, riesgo bajo. Y: 60 personas, riesgo medio. Z: 60 personas, riesgo alto. W: 30 personas, riesgo alto. ¿Cuál se atiende primero?", "Z", "Z empata con Y en 60 personas y gana por su riesgo alto."),
    ],
    ctx=ex("En una calle sin vereda, 18 de 24 vecinos de ejemplo dicen que es peligroso caminar de noche. ¿Qué porcentaje lo dice y qué alcance tiene la necesidad?", "75 %; es una necesidad local", "Se calcula 18 ÷ 24 × 100 = 75, y la calle la comparten todos los vecinos.", calc="18*100//24"),
    sc=[
        ("¿Qué es una oportunidad en Tecnología?", "Una situación que se puede mejorar creando un producto", "Es la definición de oportunidad."),
        ("Una persona quiere un color distinto para su cuaderno, ¿es necesidad o deseo?", "Deseo", "Con cualquier color puede usar el cuaderno."),
        ("¿Qué alcance tiene una necesidad que afecta a los vecinos de un pasaje?", "Local", "Comparten un lugar."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: en la entrada de una sede vecinal hay 3 escalones y una vecina con andador no puede entrar. Caso 2: en el patio de una escuela, 30 de 40 estudiantes dicen que no hay un lugar con sombra para el recreo de verano. Caso 3: un taller de barrio guarda sus herramientas en cajas sin rótulo y tarda mucho en encontrarlas. Escribe el alcance, si es necesidad o deseo, si pide un producto tecnológico (y por qué) y una oportunidad en una oración sin nombrar la solución.",
        "Caso 2: alcance local; es necesidad porque falta protección del sol; pide un producto (algo que dé sombra). Oportunidad: el 75 % de los estudiantes necesita un lugar protegido del sol durante el recreo",
        ["clasifica el alcance", "distingue necesidad de deseo", "decide si pide un producto y lo justifica", "redacta la oportunidad sin nombrar la solución"],
        ["ficha con alcance, necesidad o deseo, decisión y oportunidad"],
        ["llamar necesidad a un deseo", "nombrar el objeto de la solución dentro de la oportunidad"],
        "Pregunta: «¿esta frase dice qué lograr o ya dice qué construir?». Si dice qué construir, pídele reescribirla.",
    ),
    reinforce="Mira tu calle o tu patio y anota dos situaciones: una que sea necesidad y una que sea solo un deseo, explicando la diferencia.",
    extend="Piensa en una necesidad local que se resuelva mejor con un acuerdo que con un producto, y explica por qué.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y las tablas escritas en este cuaderno.",
    use="Aprenderé a reunir datos locales con observación, encuesta y entrevista, a leerlos como porcentajes y a priorizar con una matriz con pesos. Sirve para elegir con evidencia la oportunidad que conviene atender.",
    prior=["Sé qué es una oportunidad y distingo una necesidad de un deseo.", "Sé calcular un porcentaje.", "Sé leer una tabla de frecuencias."],
    explain=[
        "Para saber si una oportunidad es real se reúnen datos del lugar. La observación anota lo que ocurre, cuántas veces y dónde. La encuesta hace las mismas preguntas, con alternativas, a muchas personas. La entrevista es una conversación con pocas personas y sirve para entender sus razones. Se registran los datos en una tabla de frecuencias, que cuenta cuántas veces aparece cada respuesta. Si se observa varias veces, el promedio es la suma de los valores dividida entre las veces observadas.",
        "Las personas consultadas forman la muestra. Una muestra es más confiable cuando es más grande y cuando incluye a distintos grupos del lugar. Si solo se pregunta a amigos que piensan parecido, hay un sesgo: la muestra deja fuera a otros y el resultado engaña. Una pregunta que empuja a contestar de cierta manera también engaña, así que debe ser neutra. El porcentaje de una respuesta es la cantidad que la eligió, multiplicada por 100 y dividida entre el total.",
        "Si hay varias oportunidades, se priorizan con una matriz con pesos. El peso dice qué tan importante es cada criterio: 3 es muy importante y 1 es poco. Cada necesidad recibe un puntaje en cada criterio. El puntaje ponderado de un criterio es peso × puntaje, y se suman todos. Gana la oportunidad con el total más alto. Si se cambian los pesos, el resultado puede cambiar.",
    ],
    vocab=[("encuesta", "mismas preguntas con alternativas a muchas personas"), ("muestra", "personas consultadas"), ("sesgo", "error por consultar solo a un tipo de personas"), ("frecuencia", "cuántas veces aparece una respuesta"), ("peso", "importancia que se da a un criterio")],
    worked=[
        ("Calcular un porcentaje en una encuesta", "En una encuesta de ejemplo a 60 personas del barrio, 18 eligieron «más iluminación». ¿Qué porcentaje es?", ["Multiplico 18 por 100: 1.800.", "Divido entre el total: 1.800 ÷ 60 = 30."], "30 %"),
        ("Priorizar con pesos", "Pesos: personas afectadas 3, riesgo 2, facilidad 1. Necesidad X puntajes 2, 3, 1. Necesidad Y puntajes 3, 1, 3. ¿Cuál se prioriza?", ["X: 3×2 + 2×3 + 1×1 = 6 + 6 + 1 = 13.", "Y: 3×3 + 2×1 + 1×3 = 9 + 2 + 3 = 14."], "Se prioriza Y, con 14 puntos contra 13"),
    ],
    mistakes=[
        ("Preguntar solo a mis amigos y generalizar a todo el barrio.", "La muestra tiene sesgo: deja fuera a otros grupos.", "Incluye a personas de distintas edades y zonas del lugar."),
        ("Comparar solo porcentajes sin mirar cuántas personas respondieron.", "Con muy pocas respuestas, un porcentaje alto puede ser casualidad.", "Mira siempre el porcentaje y el tamaño de la muestra."),
    ],
    R=[
        ("La encuesta, ¿hace las mismas preguntas a muchas personas o conversa largo con una sola?", "Hace las mismas preguntas a muchas personas", "Esa es la diferencia con la entrevista."),
        ("Se pregunta solo a los 5 amigos del mismo equipo de fútbol qué necesita el barrio. ¿La muestra es confiable?", "No", "Deja fuera a otros grupos del barrio y tiene sesgo."),
        ("Para contar cuántos estudiantes cruzan por un tramo de barro durante un recreo, ¿qué técnica sirve: observación o encuesta?", "Observación", "Cuenta lo que ocurre, sin necesidad de preguntar."),
    ],
    C=[
        ("Una pregunta dice: «¿Está de acuerdo con que el parque necesita luz, ya que es evidentemente peligroso sin ella?». ¿Qué defecto tiene? A) empuja a una respuesta B) no deja alternativas para responder", "A", "La pregunta ya sugiere lo que se debe contestar."),
        ("Una encuesta tuvo 12 respuestas y 10 pedían techo en la parada. Otra tuvo 120 respuestas y 70 pedían techo. ¿Cuál aporta evidencia más sólida? A) la de 120 respuestas B) la de 12 respuestas, porque tiene mayor porcentaje", "A", "Una muestra más grande es más confiable que un porcentaje alto con muy pocos datos."),
        ("¿Por qué no basta una sola entrevista para decidir que una oportunidad existe? A) porque una persona puede no representar al resto del lugar B) porque las entrevistas solo sirven para contar cuántas veces ocurre algo", "A", "Una opinión puede no ser la de todos."),
    ],
    A=[
        arith("En una encuesta de ejemplo a 80 estudiantes, 52 dicen que el patio tiene pocos lugares para sentarse. ¿Qué porcentaje es?", "52*100//80", "Se multiplica por 100 y se divide entre el total.", " %"),
        arith("Pesos: personas afectadas 3, riesgo 2, facilidad 1. La necesidad «bancas» tiene puntajes 1, 3 y 2. ¿Cuál es su puntaje ponderado total?", "3*1+2*3+1*2", "Se multiplica cada puntaje por su peso y se suman los resultados.", " puntos"),
        ex("Tabla de problemas del barrio (de ejemplo): luz 24, basura 36, veredas 12, ruido 8; total 80. ¿Qué problema aparece más veces y qué porcentaje del total es?", "Basura, 45 %", "Basura tiene la mayor frecuencia y 36 × 100 ÷ 80 = 45.", calc="36*100//80"),
    ],
    Z=[
        ("Un compañero dice: «La encuesta de 12 personas es mejor porque en ella el 83 % pidió techo y en la de 120 solo el 58 %». ¿Qué le respondes? A) que 12 respuestas son muy pocas para confiar en ese porcentaje B) que 83 % siempre es mejor que 58 %", "A", "Con una muestra tan pequeña, un par de respuestas cambia el porcentaje."),
        ("Pesos personas 1, riesgo 3, facilidad 1. Necesidad S: puntajes 3, 1, 1. Necesidad T: puntajes 1, 3, 2. ¿Cuál gana con estos pesos?", "T", "S suma 3 + 3 + 1 = 7 y T suma 1 + 9 + 2 = 12, porque el riesgo pesa más."),
    ],
    D=[
        arith("Se encuestó a 5 cursos de 36 estudiantes. 99 eligieron «más bancas» y 45 «más basureros»; el resto eligió «más sombra». ¿Qué porcentaje eligió sombra?", "(5*36-99-45)*100//(5*36)", "Se calcula el total, se restan las otras opciones y se pasa a porcentaje.", " %"),
        ("Pesos: personas 3, riesgo 3, facilidad 2. Luz: puntajes 3, 3, 1. Veredas: 2, 3, 2. Basura: 3, 1, 3. ¿Cuál se prioriza y con cuántos puntos?", "Luz, con 20 puntos", "Luz suma 9 + 9 + 2 = 20; veredas, 19; basura, 18."),
    ],
    ctx=ex("La junta de vecinos anota qué piden 50 familias de ejemplo: 20 más iluminación, 15 mejores veredas, 10 contenedores de reciclaje y 5 otra cosa. ¿Qué porcentaje pidió contenedores de reciclaje?", "20 %", "Se calcula 10 × 100 ÷ 50 = 20.", calc="10*100//50"),
    sc=[
        ("¿Qué es una muestra?", "El grupo de personas consultadas", "Es quien aporta los datos."),
        ("¿Qué porcentaje son 15 personas de 60?", "25 %", "15 × 100 ÷ 60 = 25."),
        ("¿Para qué sirve el peso en una matriz?", "Para dar más importancia a un criterio", "Un criterio con más peso influye más en el resultado."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: encuesta de ejemplo a 60 personas sobre un parque: sombra 27, bancas 21, basureros 12. Registro 2: observación de ejemplo de cuántos estudiantes cruzan por un tramo de barro en 5 recreos: 14, 18, 16, 20 y 17. Calcula los porcentajes (registro 1) o el promedio por recreo (registro 2), y escribe qué oportunidad detectas y por qué la evidencia te convence o no.",
        "Registro 1: sombra 45 %, bancas 35 %, basureros 20 %; la oportunidad es dar sombra, y la evidencia convence porque 60 personas es una muestra razonable",
        ["calcula bien porcentajes o promedio", "señala la oportunidad", "juzga la evidencia (tamaño, repetición)", "usa los datos en su argumento"],
        ["hoja con cálculos y conclusión"],
        ["comparar porcentajes sin mirar el tamaño de la muestra", "olvidar la repetición de la observación"],
        "Pregunta: «¿cuántas personas respondieron o cuántas veces observaste?». Si no lo menciona, pídele agregarlo.",
    ),
    reinforce="Haz una mini encuesta de ejemplo con tres alternativas a cinco personas de tu casa o de tu curso y calcula el porcentaje de cada una.",
    extend="Explica cómo cambiarías los pesos de una matriz si el objetivo fuera cuidar la seguridad antes que el costo.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y las fichas escritas en este cuaderno.",
    use="Aprenderé a reflexionar sobre los aportes posibles de un producto: a quiénes beneficia, cuánto cuesta por persona y qué efectos no deseados podría tener. Sirve para decidir si una oportunidad vale la pena.",
    prior=["Sé formular una oportunidad con datos locales.", "Sé calcular porcentajes.", "Sé dividir cantidades de dinero."],
    explain=[
        "Reflexionar sobre los aportes de un producto es preguntarse qué cambia para las personas si existe. El beneficiario directo es quien lo usa o lo recibe; el indirecto se favorece sin usarlo, como la familia que sale ganando cuando un vecino usa una rampa. Los aportes pueden ser de seguridad, salud, autonomía, ahorro, convivencia o cuidado del ambiente. Algunos se notan a corto plazo, otros a largo plazo.",
        "Todo aporte tiene un costo: dinero, materiales, tiempo de trabajo y mantención. Para comparar propuestas se calcula el costo por persona, que es el costo total dividido entre las personas beneficiadas. Una propuesta con costo bajo por persona usa mejor los recursos, pero hay que mirar también la calidad del aporte.",
        "También se revisan los impactos no deseados: efectos negativos que nadie buscaba, como dejar fuera a un grupo, ocupar un espacio de paso o afectar la privacidad. Una buena reflexión dice a quiénes ayuda, cómo se comprobará la mejora, cuánto cuesta por persona y a quiénes podría afectar.",
    ],
    vocab=[("beneficiario directo", "quien usa o recibe el producto"), ("beneficiario indirecto", "quien se favorece sin usarlo"), ("costo por persona", "costo total dividido entre las personas beneficiadas"), ("impacto no deseado", "efecto negativo que nadie buscaba"), ("largo plazo", "efecto que se nota después de mucho tiempo")],
    worked=[
        ("Calcular el costo por persona", "Una cubierta para la parada cuesta $60.000 y la usan 30 personas. ¿Cuánto cuesta por persona?", ["Divido el costo total entre las personas: 60.000 ÷ 30.", "60.000 ÷ 30 = 2.000."], "$2.000 por persona"),
        ("Identificar beneficiarios", "Se instala una rampa en la entrada de la sede vecinal. ¿Quién es beneficiario directo y quién indirecto?", ["Directo: quien usa la rampa, como una persona con andador.", "Indirecto: quien la acompaña y ya no necesita cargar el andador por la escala."], "Directo: quien usa la rampa; indirecto: su acompañante"),
    ],
    mistakes=[
        ("Evaluar un producto solo por cuánto me sirve a mí.", "Se ignora a las demás personas del lugar.", "Pregunta a quiénes beneficia y a quiénes podría afectar."),
        ("Decir «ayudará mucho» sin cifras.", "Una frase vaga no se puede comprobar.", "Indica cuántas personas ayuda y cómo se medirá la mejora."),
    ],
    R=[
        ("Se instala una rampa en la entrada de un consultorio. Una señora en silla de ruedas la usa a diario; su vecino solo se alegra de verla. ¿Quién es la beneficiaria directa?", "La señora que la usa", "El beneficiario directo es quien usa el producto."),
        ("En un huerto de barrio, «hay que dedicar tres sábados a prepararlo». ¿Es un aporte o un costo?", "Un costo", "Es tiempo de trabajo que hay que invertir."),
        ("Un cobertor de esquinas para las mesas de un jardín infantil evita golpes. ¿Qué tipo de aporte es: seguridad o ahorro?", "Seguridad", "Su función es evitar lesiones."),
    ],
    C=[
        ("Una aplicación avisa cuándo llega la micro, pero los adultos mayores sin celular no pueden usarla. Esto es: A) un impacto no deseado, porque deja fuera a un grupo B) un aporte para todos los vecinos", "A", "Una parte de los usuarios queda sin acceso."),
        ("Marta dice: «Un producto es bueno si me sirve a mí». ¿Qué le falta a su razonamiento? A) revisar a quiénes beneficia y a quiénes afecta B) pedir que todos opinen igual", "A", "Un aporte se evalúa pensando en todas las personas del lugar."),
        ("¿Cuál de estos aportes se nota a corto plazo? A) con luz en el pasaje, los vecinos pueden caminar de noche desde la primera noche B) con los años, los niños aprenden a cuidar su barrio", "A", "El primero ocurre apenas se instala; el segundo aparece con el tiempo."),
    ],
    A=[
        ex("Una cubierta para otra parada cuesta $96.000 y la usarán 32 personas. ¿Cuánto cuesta por persona?", "$3.000", "Se divide el costo total entre las personas: 96.000 ÷ 32 = 3.000.", calc="96000//32"),
        ("Unas bancas cuestan $120.000 y benefician a 40 personas. Unos basureros cuestan $150.000 y benefician a 75 personas. ¿Qué proyecto tiene menor costo por persona?", "Los basureros", "Bancas: $3.000 por persona; basureros: $2.000 por persona."),
        arith("En la sede vecinal hay 150 visitas por semana y un pasamanos lo usan 30 de ellas. ¿Qué porcentaje de las visitas lo usa?", "30*100//150", "Se calcula la parte entre el total y se multiplica por 100.", " %"),
    ],
    Z=[
        ("Un video-timbre ayuda a 30 familias a saber quién llega, pero graba también a las personas que pasan por la vereda. ¿Cuál es su impacto no deseado más directo? A) afecta la privacidad de quienes pasan por la vereda B) que cueste dinero instalarlo", "A", "Registra imágenes de personas que no lo pidieron."),
        ("Un curso afirma: «Nuestro producto ayudará mucho». ¿Qué lo convierte en un aporte comprobable? A) indicar a cuántas personas ayudará y cómo se medirá la mejora B) decir que se verá bonito", "A", "Un aporte necesita cifras y una forma de medirlo."),
    ],
    D=[
        ex("Tres proyectos benefician a 24, 36 y 60 personas, sin repetirse, y juntos cuestan $420.000. ¿Cuánto cuesta por persona beneficiada?", "$3.500", "Se suman las personas (120) y se divide: 420.000 ÷ 120 = 3.500.", calc="420000//(24+36+60)"),
        ("Se da 1 punto por cada criterio cumplido: beneficia a más de 30 personas, cuesta menos de $3.000 por persona, no tiene impacto no deseado conocido. K: 45 personas, $108.000, sin impacto. L: 50 personas, $200.000, sin impacto. M: 28 personas, $56.000, con impacto. ¿Cuál obtiene más puntos?", "K, con 3 puntos", "K cumple los tres; L falla el costo (4.000 por persona) y M falla en personas e impacto."),
    ],
    ctx=ex("Una junta de vecinos evalúa una rampa de madera de ejemplo: cuesta $135.000 y la usarán 27 personas. Calcula el costo por persona y nombra un impacto no deseado posible.", "$5.000 por persona; por ejemplo, puede resbalar con la lluvia", "Se calcula 135.000 ÷ 27 = 5.000, y la madera mojada sin superficie antideslizante es un riesgo.", calc="135000//27"),
    sc=[
        ("¿Qué es el costo por persona?", "El costo total dividido entre las personas beneficiadas", "Permite comparar propuestas distintas."),
        ("¿Quién es un beneficiario indirecto?", "Quien se favorece sin usar el producto", "Recibe un beneficio de forma indirecta."),
        ("¿Qué es un impacto no deseado?", "Un efecto negativo que nadie buscaba", "Aparece aunque la intención sea buena."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un techo para una parada de micro cuesta $160.000 y lo usan 40 personas por día. Caso 2: unos farolitos solares para un pasaje cuestan $90.000 y benefician a 30 vecinos. Caso 3: un mural de orientación en la plaza cuesta $60.000 y lo consultan 20 personas por día. Escribe el costo por persona, un beneficiario directo y uno indirecto, un aporte a corto plazo, uno a largo plazo y un posible impacto no deseado.",
        "Caso 2: $3.000 por persona; directo: un vecino que camina de noche; indirecto: su familia, que se queda más tranquila; corto plazo: ve el camino; largo plazo: el pasaje se usa más tarde con seguridad; impacto: la luz puede molestar a una casa cercana",
        ["calcula bien el costo por persona", "nombra beneficiarios directo e indirecto", "distingue corto y largo plazo", "señala un impacto no deseado"],
        ["ficha de aportes con cálculo"],
        ["no calcular el costo por persona", "no nombrar ningún impacto no deseado"],
        "Pregunta: «¿a quién podría molestar o dejar fuera?». Si no responde, pídele pensar en otro grupo.",
    ),
    reinforce="Elige un objeto de tu casa y escribe a quiénes beneficia directa e indirectamente y qué costo tuvo.",
    extend="Explica por qué dos proyectos con el mismo costo total pueden tener costo por persona muy distinto.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a escribir una oportunidad bien formulada: con usuario, situación actual con un dato, meta medible y restricciones, sin nombrar la solución. Sirve para que todo el diseño parta de una meta clara.",
    prior=["Sé distinguir una necesidad de un deseo.", "Sé calcular porcentajes.", "Sé que un aporte se comprueba con datos."],
    explain=[
        "Una oportunidad bien formulada tiene cuatro partes: el usuario (quién tiene la necesidad), la situación actual con un dato, la meta medible y las restricciones. La situación actual medida antes de intervenir se llama línea base. La meta dice qué valor se espera lograr y se puede comprobar con un indicador, que es un dato medible, como «cuántos estudiantes» o «cuántos minutos».",
        "La formulación no debe nombrar la solución. «Necesitamos un reloj» ya decide el objeto; «los 32 estudiantes necesitan saber cuánto tiempo queda de cada actividad» deja abiertas varias soluciones posibles. Una meta como «que estén contentos» no es medible, porque no tiene cantidad; se mejora con «al menos 27 de 30 dicen que encuentran sus materiales».",
        "Las restricciones son límites que la solución debe respetar: costo máximo, tiempo disponible, materiales o seguridad. Antes de crear un producto conviene preguntar si hay una alternativa no tecnológica, como un acuerdo. Si lo que falta es un medio, un objeto o un servicio, se sigue con la solución tecnológica.",
    ],
    vocab=[("línea base", "situación medida antes de intervenir"), ("meta", "valor que se espera lograr"), ("indicador", "dato medible que muestra si se logró la meta"), ("restricción", "límite que la solución debe respetar"), ("formulación", "forma de escribir la oportunidad")],
    worked=[
        ("Reescribir sin nombrar la solución", "Un grupo escribe: «Necesitamos una aplicación para el horario de la basura». Reescribe la oportunidad con usuario, dato y meta, si hoy 12 de 30 vecinos conocen el horario y se busca que al menos 27 lo conozcan.", ["Usuario: los 30 vecinos del pasaje. Línea base: 12 de 30 conocen el horario.", "Meta medible: al menos 27 de 30. No digo cuál es la solución."], "Los 30 vecinos necesitan conocer el horario del camión; hoy lo conocen 12 y la meta es que al menos 27 lo conozcan"),
        ("Revisar si una meta es medible", "La meta es «que el curso esté más ordenado». ¿Es medible?", ["Pregunto: ¿hay una cantidad que pueda contar?", "«Más ordenado» no tiene número ni unidad."], "No es medible; falta una cantidad, como cuántos materiales están en su lugar"),
    ],
    mistakes=[
        ("Escribir «necesitamos un cartel» como si fuera la necesidad.", "Se nombra la solución antes de entender el problema.", "Escribe qué se debe lograr y deja abierta la solución."),
        ("Poner una meta sin número, como «mejorar mucho».", "No se puede comprobar si se cumplió.", "Define un indicador con cantidad y, si puedes, un plazo."),
    ],
    R=[
        ("La línea base, ¿es la situación antes de intervenir o lo que se espera lograr al final?", "La situación antes de intervenir", "Sirve de punto de comparación."),
        ("¿Cuál enunciado no nombra una solución? A) «Las 20 familias necesitan enterarse de un corte de agua con una hora de anticipación» B) «Las 20 familias necesitan una alarma en el pasaje»", "A", "El primero dice qué lograr; el segundo ya elige un objeto."),
        ("Un indicador de logro, ¿es un dato que se puede medir o una opinión personal?", "Un dato que se puede medir", "Permite comprobar si se cumplió la meta."),
    ],
    C=[
        ("Un enunciado dice: «Mejorar mucho el patio». ¿Qué le falta para estar bien formulado? A) un usuario, una situación concreta y un indicador medible B) un dibujo del patio", "A", "Sin esos elementos no se sabe a quién ayuda ni cómo se comprobará."),
        ("¿Es medible la meta «que los vecinos estén contentos»?", "No", "Contento no tiene cantidad; hay que decir cuántos y cómo se sabe."),
        ("En «Dos familias necesitan una rampa que cueste menos de $50.000», ¿cuál es la restricción? A) que cueste menos de $50.000 B) que las familias puedan entrar sin esfuerzo", "A", "Es un límite del costo; la segunda opción es el propósito."),
    ],
    A=[
        arith("Línea base: 12 de 40 estudiantes llegan a tiempo después del recreo. La meta es que lleguen 34 de 40. ¿Cuántos estudiantes más deben llegar a tiempo?", "34-12", "Se resta la línea base de la meta.", " estudiantes"),
        arith("Un curso tiene 30 estudiantes y 18 conocen hoy la ruta de evacuación. La meta es que la conozca el 90 %. ¿Cuántos estudiantes deben conocerla para cumplir la meta?", "30*90//100", "Se calcula el 90 % de 30.", " estudiantes"),
        ("Elige la mejor reescritura de «Necesitamos un reloj para la sala». A) «Los 32 estudiantes necesitan saber cuánto tiempo queda de cada actividad para terminar a la hora» B) «Los estudiantes necesitan un reloj digital grande»", "A", "La primera describe lo que se debe lograr; la segunda nombra el objeto."),
    ],
    Z=[
        ("Antes, 15 de 50 personas conocían las normas de la biblioteca. Tras una semana de una campaña, 35 de 50 las conocen. La meta era que al menos 40 de 50 las conocieran. ¿Se cumplió?", "No", "Hay 35 personas y la meta pedía al menos 40."),
        ("La oportunidad es que los perros ensucian la plaza. ¿Cuál es una solución tecnológica? A) instalar dispensadores de bolsas con un basurero B) pedir a los dueños que se comprometan", "A", "Un dispensador es un objeto; el compromiso es un acuerdo."),
    ],
    D=[
        arith("En un curso de 40 estudiantes, 20 usan bien el reciclaje y la meta es llegar a 30. ¿Qué porcentaje del curso son los 10 estudiantes que se deben agregar?", "10*100//40", "Se calcula la parte entre el total y se multiplica por 100.", " %"),
        ("Un enunciado válido cumple cuatro condiciones: nombra al usuario, da la situación actual con un dato, fija una meta medible y no nombra la solución. Revisa: «Los 25 estudiantes de un curso pierden 6 minutos en cada recreo buscando la pelota; se busca bajar ese tiempo a 2 minutos o menos comprando una caja con candado». ¿Cuántas condiciones cumple y cuál no?", "3 de 4; no cumple la última porque nombra la caja con candado", "Tiene usuario, dato y meta medible, pero ya decidió la solución."),
    ],
    ctx=ex("En una sala de ejemplo, 9 de 30 estudiantes saben dónde se guardan los materiales de ciencias y la meta es que lo sepan 27. ¿Cuántos más deben saberlo? Escribe también la oportunidad.", "18 estudiantes más; los 30 estudiantes necesitan encontrar rápido los materiales: hoy 9 saben dónde están y la meta es que 27 lo sepan", "Se calcula 27 − 9 = 18 y la oportunidad lleva usuario, línea base y meta sin nombrar la solución.", calc="27-9"),
    sc=[
        ("¿Qué es la línea base?", "La situación medida antes de intervenir", "Permite saber cuánto se mejoró."),
        ("¿Qué partes tiene una oportunidad bien formulada?", "Usuario, situación con un dato, meta medible y restricciones", "Son las cuatro partes de la formulación."),
        ("¿Una restricción es un límite o una meta?", "Un límite", "Marca lo que la solución debe respetar."),
    ],
    open_task=(
        "Escoge un caso con sus datos. Caso 1: en una biblioteca de curso de 40 libros se pierden 12 libros al año; se busca perder 4 o menos. Caso 2: en un pasaje de 30 vecinos, 12 conocen el horario del camión de basura; se busca que 27 lo conozcan. Caso 3: en un patio de 200 estudiantes, 30 caben en la sombra; se busca que quepan 100. Escribe la oportunidad con usuario, situación actual con dato, meta medible y una restricción que tú inventes, sin nombrar la solución.",
        "Caso 2: los 30 vecinos del pasaje necesitan conocer el horario del camión de basura; hoy lo conocen 12 y la meta es que lo conozcan al menos 27, con un gasto máximo de $20.000",
        ["incluye usuario", "da la situación actual con dato", "fija una meta medible", "agrega una restricción", "no nombra la solución"],
        ["oportunidad escrita en una o dos oraciones"],
        ["nombrar la solución en el enunciado", "fijar una meta sin número"],
        "Pregunta: «¿cómo sabrías con un número que se logró?». Si no puede responder, pídele agregar el indicador.",
    ),
    reinforce="Elige un problema de tu casa o de tu barrio y escribe su usuario, la línea base con un dato de ejemplo y una meta medible.",
    extend="Explica por qué la misma oportunidad puede tener varias soluciones posibles y qué restricciones ayudarían a elegir entre ellas.",
)

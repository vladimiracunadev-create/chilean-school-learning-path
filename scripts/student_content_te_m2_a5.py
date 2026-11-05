"""Cuaderno del estudiante, 2.º medio Tecnología: OA 05 (evaluar críticamente cómo las innovaciones tecnológicas actuales afectan a la sociedad y al ambiente, con criterios éticos, económicos, ambientales y sociales), clases 1 a 5.

Seguridad: las tareas son de lectura, cálculo y escritura. Las innovaciones se nombran por tipo (riego con sensores, reparto a domicilio, paneles solares, asistente automático), sin marcas. Todas las cifras son datos de ejemplo.
Vacío declarado: no se profundiza en el funcionamiento técnico de cada innovación ni en normativa concreta; las fuentes reales y los casos actuales los aporta el docente.
"""
from __future__ import annotations

from student_content_te_m2_a import reg
from student_lessons import arith, ex

OA5 = "TE2M OA 05"

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a reconocer qué es una innovación, a distinguir efectos esperados y no esperados y a hacer preguntas críticas. Sirve para analizar una novedad tecnológica sin aceptarla ni rechazarla solo por ser nueva.",
    prior=["Sé las cinco dimensiones para evaluar una propuesta.", "Sé qué es un efecto perjudicial.", "Sé calcular porcentajes."],
    explain=[
        "Una innovación es algo nuevo, un producto, un proceso o un servicio, que se adopta y cambia la forma de hacer algo. No toda tecnología nueva llega a ser innovación: solo lo es si se usa y produce un cambio. Una innovación puede ser incremental, si mejora algo que ya existía, o radical, si cambia profundamente la manera de hacer algo.",
        "Toda innovación tiene efectos esperados, que son los que busca quien la crea, y efectos no esperados, que aparecen después y no estaban en el plan. Un sistema de reparto a domicilio acorta traslados (esperado) y puede aumentar los envases desechados (no esperado). También puede beneficiar a unas personas y perjudicar a otras, por eso se pregunta quién gana y quién pierde.",
        "El análisis crítico no es rechazar lo nuevo ni aplaudirlo. Consiste en hacer preguntas y buscar evidencia: ¿qué problema resuelve?, ¿para quién?, ¿a qué costo y quién lo paga?, ¿qué pasa si muchas personas la usan?, ¿qué datos lo demuestran? Una frase como «es genial porque es nueva» no usa evidencia, y «es mala porque es nueva» tampoco.",
    ],
    vocab=[("innovación", "novedad que se adopta y cambia cómo se hace algo"), ("efecto esperado", "el que busca quien crea la innovación"), ("efecto no esperado", "el que aparece después y no estaba previsto"), ("análisis crítico", "preguntar y buscar evidencia antes de aceptar o rechazar"), ("incremental", "mejora pequeña de algo que ya existía"), ("radical", "cambio profundo en la forma de hacer algo")],
    worked=[
        ("Esperado o no esperado", "Un riego con sensores usa menos agua en un huerto, pero sus baterías se desechan al final de su vida útil. Clasifica ambos efectos.", ["Usar menos agua es lo que se buscaba.", "El desecho de baterías no estaba en el plan."], "Menos agua: esperado; desecho de baterías: no esperado"),
        ("Preguntas críticas", "Un video dice que un asistente automático «hará mejor todas las tareas». Escribe dos preguntas críticas.", ["Pregunto por la evidencia: «¿qué datos lo demuestran?».", "Pregunto por los costos: «¿para quién y a qué costo?»."], "¿Qué datos lo demuestran? ¿Para quién y a qué costo?"),
    ],
    mistakes=[
        ("Decir que una innovación es buena porque es nueva.", "Lo nuevo no es bueno ni malo por sí solo; depende de sus efectos.", "Revisa los efectos con evidencia."),
        ("Pensar que una innovación solo tiene los efectos que su creador anunció.", "Los efectos no esperados aparecen con el uso.", "Pregunta qué pasaría si muchas personas la usaran."),
    ],
    R=[
        ("Una innovación es… A) algo nuevo que se adopta y cambia cómo se hace algo B) cualquier idea que alguien tiene", "A", "Para ser innovación debe usarse y producir un cambio."),
        ("«El riego con sensores usa menos agua». Ese efecto es… A) esperado B) no esperado", "A", "Es lo que busca quien lo crea."),
        ("El análisis crítico consiste en… A) preguntar y buscar evidencia antes de aceptar o rechazar B) rechazar todo lo nuevo", "A", "No es rechazar ni aplaudir, es evaluar con evidencia."),
    ],
    C=[
        ("Un reparto a domicilio reduce el tiempo de entrega, pero produce más envases. Los envases son… A) un efecto no esperado B) el objetivo del reparto", "A", "No estaban en el plan de quien lo creó."),
        ("Una persona dice «es genial porque es nueva» y otra «es mala porque es nueva». ¿Qué tienen en común? A) ninguna usa evidencia B) ambas son críticas", "A", "Las dos juzgan por la novedad y no por los efectos."),
        ("¿Qué pregunta ayuda a descubrir efectos no esperados? A) ¿qué pasa si muchas personas la usan? B) ¿cuánto brilla?", "A", "Con uso masivo aparecen efectos que no se ven en una prueba pequeña."),
    ],
    A=[
        ("Innovación: paneles solares en techos de casas. Efectos: (1) menor cuenta de luz, (2) residuos de equipos al terminar su vida útil, (3) menos energía comprada a la red. ¿Cuál es un efecto perjudicial?", "El 2", "Los residuos son un costo ambiental; los otros dos son beneficios."),
        arith("En una encuesta de ejemplo a 200 personas, 140 usan una innovación. ¿Qué porcentaje la usa?", "140*100//200", "Se divide entre el total y se pasa a porcentaje.", " %"),
        arith("Un huerto de ejemplo gasta 1.200 litros de agua por semana y el riego con sensores reduce 25 %. ¿Cuántos litros gasta ahora?", "1200-1200*25//100", "Se calcula el 25 % y se resta del total.", " litros"),
    ],
    Z=[
        ("Un video afirma que una innovación «resuelve todos los problemas de energía». ¿Qué pregunta crítica es la más importante?", "¿Qué evidencia presenta y quién la produjo?", "Una afirmación tan amplia necesita datos y fuente verificables."),
        ("¿Por qué una innovación puede beneficiar a unas personas y perjudicar a otras?", "Porque sus efectos no llegan por igual a todos", "Por ejemplo, un reparto rápido beneficia a clientes y puede cargar a quienes reparten."),
    ],
    D=[
        arith("De 500 pedidos de ejemplo, el 20 % llega con un envase plástico extra. ¿Cuántos envases extra hay?", "500*20//100", "Se calcula el 20 % de 500.", " envases"),
        arith("Un huerto de ejemplo tiene 8 camas y el sensor reduce 20 % un riego de 60 litros semanales por cama. ¿Cuántos litros ahorra en total por semana?", "8*60*20//100", "Se calcula el ahorro por cama y se multiplica por las camas.", " litros"),
    ],
    ctx=arith("De 48 estudiantes de ejemplo, 36 usan un asistente automático para sus tareas. ¿Qué porcentaje es?", "36*100//48", "Se divide entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("En Tecnología: ¿qué es un efecto no esperado?", "El que aparece después y no estaba previsto", "Es la definición de la clase."),
        ("¿Una innovación es buena solo por ser nueva?", "No", "Depende de sus efectos y de la evidencia."),
        ("Nombra una pregunta crítica sobre una innovación.", "¿Para quién y a qué costo?", "Cualquier pregunta sobre evidencia, beneficiarios o costos sirve."),
    ],
    open_task=(
        "Escoge una innovación de ejemplo. Caso 1: riego con sensores en un huerto escolar. Caso 2: reparto de comida a domicilio con motos. Caso 3: paneles solares en los techos de un barrio. Escribe: (1) el problema que dice resolver, (2) dos efectos esperados, (3) dos efectos no esperados que podrían aparecer y (4) tres preguntas críticas que harías para decidir si conviene.",
        "Caso 2: resuelve el tiempo de traslado; esperados, entrega rápida y más ventas; no esperados, más envases y más ruido; preguntas, quién paga los costos, qué datos hay de residuos y quiénes reparten con qué condiciones",
        ["dice qué problema resuelve", "distingue efectos esperados y no esperados", "las preguntas piden evidencia o costos", "no juzga por ser nueva"],
        ["hoja con las cuatro partes"],
        ["decir «es buena porque es moderna»", "no escribir efectos no esperados"],
        "Pregunta: «¿qué pasaría si todo el barrio la usara?». Debe aparecer al menos un efecto que no se ve con pocos usuarios.",
    ),
    reinforce="Escribe una innovación que uses a diario y un efecto no esperado que podría tener.",
    extend="Explica por qué «es nueva» no es un argumento a favor ni en contra de una tecnología.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir hecho, opinión y publicidad, a evaluar fuentes y a leer cifras con su base de comparación. Sirve para reunir evidencia confiable antes de juzgar una innovación.",
    prior=["Sé qué es una fuente confiable.", "Sé calcular porcentajes.", "Sé qué es una afirmación verificable."],
    explain=[
        "Un hecho es una afirmación que se puede comprobar con datos, como «el taller gastó 120 kWh en marzo». Una opinión es un juicio personal, como «me parece cómodo». La publicidad es un mensaje cuyo fin es vender, como «¡compra hoy y ahorra sin esfuerzo!». Para evaluar una innovación se usan hechos; las opiniones y la publicidad se leen con cuidado.",
        "Una fuente es más confiable si tiene autoría, fecha, datos y método, y si no gana dinero con lo que afirma. Un conflicto de intereses aparece cuando quien informa se beneficia si tú le crees, como una empresa que financia un estudio sobre su propio producto. Para contrastar, se comparan al menos dos fuentes independientes.",
        "Las cifras necesitan su base. «Aumentó 50 %» no dice cuánto: pasar de 2 a 3 reclamos es 50 %, y pasar de 200 a 300 también. Hay que mirar la cantidad inicial, el período y la unidad. Además, que dos cosas ocurran juntas no prueba que una cause la otra: puede haber una tercera causa.",
    ],
    vocab=[("hecho", "afirmación que se puede comprobar con datos"), ("opinión", "juicio personal que no se comprueba con datos"), ("publicidad", "mensaje cuyo fin es vender"), ("conflicto de intereses", "quien informa gana si le crees"), ("contrastar", "comparar fuentes independientes"), ("base de comparación", "cantidad inicial sobre la que se calcula un cambio")],
    worked=[
        ("Clasificar afirmaciones", "Clasifica: «el consumo bajó de 80 a 60 hojas», «es la mejor idea del año».", ["La primera se puede comprobar con datos.", "La segunda es un juicio personal."], "Hecho; opinión"),
        ("La base de un porcentaje", "Dos servicios «aumentaron 50 %»: uno pasó de 2 a 3 reclamos y otro de 200 a 300. ¿Es igual de grave?", ["En el primero hay 1 reclamo más.", "En el segundo hay 100 reclamos más."], "No, la base cambia el tamaño del aumento"),
    ],
    mistakes=[
        ("Creer una cifra solo porque tiene un porcentaje grande.", "Sin base ni período, el porcentaje no dice cuánto es.", "Pregunta: ¿50 % de qué cantidad y en cuánto tiempo?"),
        ("Pensar que si dos cosas ocurren juntas, una causa la otra.", "Puede haber una tercera causa o una casualidad.", "Busca evidencia de causa antes de afirmarla."),
    ],
    R=[
        ("¿Cuál es un hecho? A) «el consumo bajó de 80 a 60 hojas» B) «es la mejor idea del año»", "A", "Se puede comprobar con datos."),
        ("Un conflicto de intereses es… A) cuando quien informa gana si tú le crees B) cuando dos personas discuten", "A", "Quien tiene interés en vender puede sesgar su información."),
        ("Contrastar fuentes es… A) comparar lo que dicen dos o más fuentes independientes B) copiar la primera que aparece", "A", "La coincidencia independiente da más confianza."),
    ],
    C=[
        ("Un informe dice «aumentó 50 %» sin más datos. ¿Qué falta? A) saber de qué cantidad inicial y en qué período B) un color más llamativo", "A", "Sin base no se sabe cuánto aumentó."),
        ("En un liceo de ejemplo, las semanas con más lluvia tuvieron más ausentes y más uso de calefactores. Un compañero dice que los calefactores causan ausencias. ¿Qué falla? A) que dos cosas ocurran juntas no prueba que una cause la otra B) nada, es correcto", "A", "La lluvia puede explicar ambas cosas."),
        ("Un aviso dice «estudios demuestran…» sin citar ninguno. ¿Es evidencia? A) no, hasta saber qué estudio es, quién lo hizo y cómo B) sí, porque dice estudios", "A", "Una referencia vaga no se puede comprobar."),
    ],
    A=[
        ("Clasifica como hecho, opinión o publicidad: (1) «el taller gastó 120 kWh en marzo», (2) «me parece muy cómodo este sistema», (3) «¡compra hoy y ahorra sin esfuerzo!».", "1 hecho, 2 opinión, 3 publicidad", "Solo la primera se comprueba con datos; la tercera busca vender."),
        arith("Un informe de ejemplo dice que las emisiones de un servicio «aumentaron 50 %». Si antes eran 240 unidades, ¿cuántas son ahora?", "240+240*50//100", "Se calcula el 50 % de 240 y se suma.", " unidades"),
        arith("De 5 fuentes de ejemplo, 3 tienen autoría, fecha y datos. ¿Qué porcentaje es?", "3*100//5", "Se divide entre el total y se pasa a porcentaje.", " %"),
    ],
    Z=[
        ("Una empresa financia un estudio que concluye que su producto es el mejor. ¿Qué se hace antes de aceptarlo?", "Contrastarlo con fuentes independientes y revisar el método", "Hay un conflicto de intereses que puede sesgar el resultado."),
        ("Una fuente dice «bajó 20 %» y otra «subió 10 %» sobre lo mismo. ¿Qué se revisa primero?", "Qué período, qué unidad y qué base usó cada una", "Las diferencias suelen venir de medir cosas distintas."),
    ],
    D=[
        arith("Dos servicios suben 50 %: uno de 2 a 3 reclamos y otro de 200 a 300. ¿Cuántas veces más reclamos nuevos tiene el segundo que el primero?", "(300-200)//(3-2)", "Se divide el aumento del segundo entre el del primero.", " veces"),
        ex("Un estudio de ejemplo midió a 40 personas y 30 mejoraron; otro midió a 400 y 300 mejoraron. ¿Qué se puede decir de ambos?", "Ambos muestran 75 %, pero el de 400 personas es más confiable", "Ambos cumplen 30 de 40 y 300 de 400, pero más casos dan más confianza."),
    ],
    ctx=arith("De 10 fuentes de ejemplo revisadas, 7 coinciden en el dato. ¿Qué porcentaje coincide?", "7*100//10", "Se divide entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("En Tecnología: ¿qué es un hecho?", "Una afirmación que se puede comprobar con datos", "Es lo que se usa para evaluar."),
        ("¿Qué se pregunta ante «aumentó 50 %»?", "50 % de qué cantidad y en qué período", "El porcentaje necesita base."),
        ("¿Qué es contrastar fuentes?", "Comparar fuentes independientes", "Aumenta la confianza en el dato."),
    ],
    open_task=(
        "Revisa estas tres fuentes de ejemplo sobre un sistema de riego con sensores. Fuente A: una empresa que lo vende dice que «reduce 90 % el agua en cualquier huerto». Fuente B: un informe de una universidad, con autoría, fecha y método, midió 18 % menos de agua en 12 huertos. Fuente C: un comentario anónimo en una red dice «a mí no me sirvió». Clasifica cada una (hecho, opinión o publicidad), evalúa su confiabilidad con al menos tres criterios y concluye qué cifra usarías y qué más buscarías.",
        "A: publicidad con conflicto de intereses y sin método; B: hecho medido, con autoría, fecha y método; C: opinión anónima; se usaría 18 % de B y se buscaría otra fuente independiente",
        ["clasifica las tres fuentes", "usa al menos tres criterios de confiabilidad", "elige una cifra con razones", "propone qué más buscar"],
        ["hoja con la tabla de fuentes y la conclusión"],
        ["creer la cifra más grande", "no mencionar el conflicto de intereses"],
        "Pregunta: «¿quién gana si le crees a esta fuente?». Debe notar el interés de la empresa.",
    ),
    reinforce="Elige una afirmación que hayas visto sobre una tecnología y anota si es hecho, opinión o publicidad.",
    extend="Explica por qué un porcentaje sin su cantidad inicial puede engañar.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los datos escritos en este cuaderno.",
    use="Aprenderé a comparar innovaciones con criterios éticos, económicos, ambientales y sociales, a calcular un costo por uso y a reconocer los costos que recaen en otras personas. Sirve para emitir un juicio ordenado y no por impresión.",
    prior=["Sé usar una matriz con pesos y puntajes.", "Sé calcular el costo por uso.", "Sé qué es el ciclo de vida de un producto."],
    explain=[
        "Para evaluar una innovación con criterios se usan indicadores. En lo económico, el costo por uso (precio ÷ veces que se usa). En lo ambiental, los kilogramos de residuo que deja al final de su vida útil. En lo social, el porcentaje de personas que puede acceder a ella. En lo ético, si respeta la privacidad y trata con justicia a las personas. Los indicadores permiten comparar innovaciones distintas con las mismas reglas.",
        "Una externalidad es un costo o un beneficio que recae en personas que no participaron en la decisión. Por ejemplo, una fábrica que ahorra energía pero contamina el río cercano genera una externalidad negativa para quienes viven allí. Evaluar bien una innovación incluye mirar las externalidades, no solo lo que ve quien la usa.",
        "Con una matriz de decisión se asignan pesos a los criterios y puntajes de 1 a 3 a cada innovación. El total es la suma de peso × puntaje. Un puntaje total alto no basta si hay un incumplimiento ético grave, como recolectar datos sin permiso: eso se corrige antes de recomendar. Si algo es más barato, no necesariamente es mejor.",
    ],
    vocab=[("indicador", "dato medible que representa un criterio"), ("costo por uso", "precio dividido entre las veces que se usa"), ("externalidad", "costo o beneficio que recae en quienes no decidieron"), ("acceso", "porcentaje de personas que pueden usarla"), ("matriz de decisión", "tabla que compara opciones con pesos y puntajes"), ("incumplimiento grave", "falta que impide recomendar la innovación mientras no se corrija")],
    worked=[
        ("Costo por uso", "Un aparato de ejemplo cuesta $90.000 y se usará 300 veces. ¿Cuál es su costo por uso?", ["Divido el precio entre los usos.", "90.000 ÷ 300 = 300."], "$300 por uso"),
        ("Reconocer una externalidad", "Un reparto rápido genera ruido en los pasajes de un barrio. ¿Quiénes soportan el costo?", ["El ruido no lo paga quien pide ni quien vende.", "Lo soportan los vecinos."], "Los vecinos, que no participaron en la decisión"),
    ],
    mistakes=[
        ("Elegir la innovación más barata sin mirar nada más.", "Puede dejar residuos, excluir a personas o violar la privacidad.", "Compara con indicadores de los cuatro criterios."),
        ("Ignorar a quienes no usan la innovación pero la sufren.", "Las externalidades también cuentan.", "Pregunta quién soporta costos sin haber decidido."),
    ],
    R=[
        ("Una externalidad es… A) un costo o beneficio que recae en personas que no decidieron B) el precio de un producto", "A", "Los terceros la soportan o reciben sin haber participado."),
        arith("Un aparato de ejemplo cuesta $60.000 y se usará 200 veces. ¿Cuál es su costo por uso?", "60000//200", "Costo por uso = precio ÷ veces de uso.", " pesos"),
        ("Un indicador ambiental es… A) los kg de residuo que deja al final de su vida útil B) el precio de venta", "A", "El precio es económico; el residuo es ambiental."),
    ],
    C=[
        ("Una innovación ahorra energía a quien la usa, pero su fabricación contamina un río cercano. Eso es… A) una externalidad negativa que afecta a quienes viven cerca B) un beneficio para todos", "A", "El costo recae en terceros."),
        ("¿Para qué sirve una matriz de decisión? A) para comparar con las mismas reglas y no por impresión B) para elegir siempre la más cara", "A", "Los criterios y pesos ordenan el juicio."),
        ("Un indicador social adecuado es… A) el porcentaje de la población que puede acceder B) la potencia del motor", "A", "Mide quiénes pueden usarla."),
    ],
    A=[
        arith("Pesos: económico 2, ambiental 3, social 2, ético 3. La innovación P recibe 3, 2, 1 y 2. ¿Cuántos puntos suma?", "2*3+3*2+2*1+3*2", "Se multiplica cada peso por su puntaje y se suman los aportes.", " puntos"),
        arith("Con los mismos pesos (económico 2, ambiental 3, social 2, ético 3), la innovación Q recibe 2, 3, 3 y 2. ¿Cuántos puntos suma?", "2*2+3*3+2*3+3*2", "Se multiplica cada peso por su puntaje y se suman los aportes.", " puntos"),
        ("P suma 20 puntos y Q suma 25 con esos pesos. La innovación R recibe 3, 1, 2 y 3 (económico, ambiental, social, ético). ¿Cuál de las tres puntúa mejor y cuántos puntos suma?", "Q, con 25 puntos", "R suma 2 × 3 + 3 × 1 + 2 × 2 + 3 × 3 = 22, menos que Q."),
    ],
    Z=[
        ("Una innovación puntúa alto en lo económico, pero recolecta datos de las personas sin permiso. ¿Se recomienda solo por su total?", "No: el incumplimiento ético grave se corrige antes de recomendar", "Un total alto no compensa una falta grave."),
        ("Alguien dice: «Si es más barata, es mejor». ¿Qué falta considerar?", "Los efectos ambientales, sociales y éticos y los costos que recaen en otros", "El precio es solo uno de los criterios."),
    ],
    D=[
        arith("Una innovación de ejemplo cuesta $200.000 y se usa 100 veces al año durante 4 años. ¿Cuál es su costo por uso?", "200000//(100*4)", "Se calculan los usos totales y se divide el precio.", " pesos"),
        arith("En un barrio de ejemplo, cada pedido genera 2 envases, hay 150 pedidos al día y se reparte 6 días a la semana. ¿Cuántos envases genera por semana?", "150*2*6", "Se multiplican pedidos, envases y días.", " envases"),
    ],
    ctx=arith("De 40 viviendas de ejemplo, 32 tienen un techo apto para instalar paneles solares. ¿Qué porcentaje tiene acceso?", "32*100//40", "Se divide entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("En Tecnología: ¿qué es una externalidad?", "Un costo o beneficio que recae en quienes no decidieron", "Es la definición de la clase."),
        ("¿Cómo se calcula el costo por uso?", "Precio ÷ veces que se usa", "Permite comparar productos de distinta duración."),
        ("¿Qué se hace con un incumplimiento ético grave?", "Se corrige antes de recomendar", "Un total alto no lo compensa."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Pesos: económico 2, ambiental 3, social 2, ético 3. Innovación A (paneles solares de techo): costo $600.000, se usa 10 años; deja residuos al final; accesible al 60 % de las viviendas; no recolecta datos. Innovación B (aplicación de reparto): costo por uso bajo; genera muchos envases; accesible al 90 %; recolecta la ubicación de los usuarios sin avisar. Puntúa cada una de 1 a 3, calcula el total, señala una externalidad de cada una y di qué corregirías antes de recomendarla.",
        "A: económico 2, ambiental 2, social 2, ético 3, total 4 + 6 + 4 + 9 = 23; B: económico 3, ambiental 1, social 3, ético 1, total 6 + 3 + 6 + 3 = 18; externalidades, A residuos y B envases y ruido; B debe pedir consentimiento para la ubicación",
        ["puntúa los cuatro criterios", "calcula bien los totales", "nombra una externalidad por innovación", "propone una corrección ética"],
        ["hoja con la matriz y las conclusiones"],
        ["sumar sin pesos", "ignorar la falta ética"],
        "Pregunta: «¿quién soporta un costo sin haber decidido?». Debe encontrar a un tercero en cada caso.",
    ),
    reinforce="Elige un objeto tecnológico de tu casa y calcula su costo por uso estimando precio y veces que se usa.",
    extend="Explica por qué una innovación barata para quien la usa puede ser cara para la sociedad.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a analizar los efectos de una innovación en la sociedad: empleo, brecha digital, privacidad e inclusión. Sirve para detectar quiénes ganan y quiénes pierden con una tecnología.",
    prior=["Sé qué es una externalidad.", "Sé calcular porcentajes.", "Sé que los datos personales se usan con consentimiento."],
    explain=[
        "Las innovaciones cambian el trabajo: algunos puestos desaparecen, otros se crean y otros se transforman. El saldo de empleo es los puestos creados menos los eliminados. Pero el saldo no basta: también importa si quienes pierden el puesto pueden ocupar los nuevos, para lo cual muchas veces necesitan capacitación.",
        "La brecha digital es la diferencia entre quienes tienen acceso a tecnología y habilidades para usarla y quienes no. Si una innovación solo funciona con internet, deja fuera a los hogares que no tienen conexión o a quienes no han tenido cómo aprender a usarla. La privacidad es el control que tiene una persona sobre qué datos suyos se recogen y cómo se usan: una innovación que pide más datos de los que necesita afecta la privacidad.",
        "La inclusión es diseñar para que personas muy distintas, también con discapacidad, puedan participar en igualdad. Para evaluar un efecto social se pregunta quién gana, quién pierde y quién decide. Si una parte de la población queda fuera, se propone una alternativa, como un servicio presencial o apoyo para aprender a usarla. Si algo que ves en línea te inquieta, conversa con una persona adulta de confianza.",
    ],
    vocab=[("saldo de empleo", "puestos creados menos puestos eliminados"), ("brecha digital", "diferencia de acceso a tecnología y a habilidades para usarla"), ("privacidad", "control sobre qué datos personales se recogen y usan"), ("inclusión", "diseñar para que todas las personas puedan participar"), ("capacitación", "formación para ocupar nuevos puestos"), ("alternativa presencial", "forma de recibir el servicio sin depender de la tecnología")],
    worked=[
        ("Calcular una brecha", "De 40 hogares de ejemplo, 30 tienen internet. ¿Qué porcentaje no tiene?", ["Hogares sin internet: 40 − 30 = 10.", "10 × 100 ÷ 40 = 25."], "25 %"),
        ("Saldo de empleo", "Un servicio elimina 20 puestos y crea 5. ¿Cuál es el saldo?", ["Creados menos eliminados.", "5 − 20 = −15."], "−15 puestos"),
    ],
    mistakes=[
        ("Medir el empleo solo con el saldo.", "Los puestos nuevos pueden requerir estudios que los afectados no tienen.", "Pregunta quién ocupará los puestos nuevos y qué capacitación necesita."),
        ("Pensar que, si la mayoría puede usar la innovación, ya es inclusiva.", "Quienes quedan fuera siguen sin acceso.", "Propone una alternativa para ese grupo."),
    ],
    R=[
        ("La brecha digital es… A) la diferencia en acceso a tecnología y a habilidades para usarla B) una falla técnica de internet", "A", "Se trata de desigualdad, no de una avería."),
        arith("En 80 hogares de ejemplo, 56 tienen internet. ¿Qué porcentaje no tiene?", "(80-56)*100//80", "Se calculan los hogares sin internet y se pasa a porcentaje.", " %"),
        ("La privacidad es… A) el control sobre qué datos personales se recogen y cómo se usan B) la velocidad de la conexión", "A", "Se refiere a los datos de las personas."),
    ],
    C=[
        arith("Un servicio de ejemplo elimina 8 puestos y crea 5. ¿Cuál es el saldo de empleo?", "5-8", "Saldo = puestos creados menos eliminados.", " puestos"),
        ("¿Por qué incluir a personas con discapacidad en el diseño? A) porque una innovación inclusiva permite que más personas participen en igualdad B) porque así es más barata", "A", "La inclusión amplía quiénes pueden participar."),
        ("Una aplicación pide la ubicación permanente sin necesitarla para funcionar. ¿Qué se afecta? A) la privacidad, por recoger más datos de los necesarios B) la rapidez", "A", "Recoge información personal sin necesidad."),
    ],
    A=[
        arith("Un servicio de ejemplo elimina 14 puestos y crea 9. ¿Cuántos puestos hay de menos al final?", "14-9", "Se restan los puestos creados de los eliminados.", " puestos"),
        ("Une cada situación con el efecto (brecha digital, privacidad o empleo): (1) personas mayores sin celular no pueden pedir hora, (2) la empresa recolecta datos de ubicación, (3) se crean puestos de mantención.", "1 brecha digital, 2 privacidad, 3 empleo", "Cada situación apunta a un efecto social distinto."),
        arith("En una encuesta de ejemplo a 120 personas, el 45 % usa la innovación. ¿Cuántas personas son?", "120*45//100", "Se calcula el 45 % de 120.", " personas"),
    ],
    Z=[
        ("Una innovación beneficia al 70 % de la población, pero deja sin acceso a personas mayores. ¿Qué se recomienda?", "Mantener una alternativa presencial o dar apoyo a ese grupo", "Quienes quedan fuera no deben perder el servicio."),
        ("Un informe dice que se crean más puestos de los que se pierden, pero los nuevos exigen estudios que los afectados no tienen. ¿Qué falta considerar?", "La capacitación y quién ocupará los puestos nuevos", "El saldo no dice quién se beneficia."),
    ],
    D=[
        arith("En 2.000 hogares de ejemplo, 1.500 tienen internet. Si una innovación solo funciona con internet, ¿qué porcentaje de hogares queda fuera?", "(2000-1500)*100//2000", "Se calculan los hogares sin internet y se pasa a porcentaje.", " %"),
        arith("En la zona A se eliminan 14 puestos y se crean 9; en la zona B se eliminan 6 y se crean 10. ¿Cuál es el saldo de ambas zonas juntas?", "(9-14)+(10-6)", "Se calcula el saldo de cada zona y se suman.", " puestos"),
    ],
    ctx=arith("De 45 estudiantes de ejemplo, 36 aceptan compartir sus datos solo si se les explica para qué se usan. ¿Qué porcentaje es?", "36*100//45", "Se divide entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("En Tecnología: ¿qué es la brecha digital?", "La diferencia de acceso a tecnología y a habilidades para usarla", "Es la definición de la clase."),
        ("¿Qué se pregunta para analizar un efecto social?", "Quién gana, quién pierde y quién decide", "Revela los efectos desiguales."),
        ("¿Qué haces si algo que ves en línea te inquieta?", "Converso con una persona adulta de confianza", "No se guarda en secreto."),
    ],
    open_task=(
        "Escoge un caso de ejemplo. Caso 1: un servicio municipal solo permite pedir hora médica por una aplicación. Caso 2: una cadena instala cajas de autoservicio y elimina 12 puestos de caja pero crea 4 de mantención. Caso 3: una aplicación escolar registra la ubicación de los estudiantes todo el día. Para el caso elegido escribe: quién gana, quién pierde, qué efecto social aparece (empleo, brecha digital, privacidad o inclusión), un cálculo con los datos del caso o con 100 personas de ejemplo y una medida para corregir el efecto negativo.",
        "Caso 1: ganan quienes tienen celular; pierden personas mayores o sin internet; efecto, brecha digital; si 30 de 100 no tienen acceso, quedan fuera 30 %; medida, mantener una ventanilla presencial",
        ["nombra quién gana y quién pierde", "identifica el efecto social", "incluye un cálculo correcto", "propone una medida concreta"],
        ["hoja con las cuatro partes"],
        ["no nombrar a quién pierde", "proponer una medida vaga"],
        "Pregunta: «¿quién queda fuera si esto cambia mañana?». Debe nombrar un grupo concreto.",
    ),
    reinforce="Piensa en un servicio que hoy se hace por internet y anota quién podría tener dificultades para usarlo.",
    extend="Explica por qué crear puestos nuevos no soluciona por sí solo la pérdida de otros.",
)

# ------------------------------------------------------------------ OA 05, clase 5
reg(
    OA5, 5,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a construir un juicio crítico con tesis, argumentos con evidencia, contraargumento y conclusión, y a detectar errores de razonamiento. Sirve para expresar una posición matizada sobre una innovación.",
    prior=["Sé evaluar una innovación con criterios.", "Sé distinguir hecho y opinión.", "Sé calcular porcentajes."],
    explain=[
        "Un juicio crítico bien construido tiene cuatro partes. La tesis es la postura que se defiende. Los argumentos son razones apoyadas en evidencia que se puede revisar, por ejemplo datos de los cuatro criterios. El contraargumento es una razón que va en contra de la tesis: se reconoce y se responde. La conclusión cierra con la postura final y, si corresponde, las condiciones para adoptar la innovación.",
        "Una postura matizada evita los extremos: «conviene adoptarla si se protegen los datos y se ofrece una alternativa presencial» es más útil que «es siempre buena» o «es siempre mala». Los matices salen de la evidencia, no de la duda por duda. Un buen juicio muestra también lo que no se sabe y qué datos faltarían.",
        "Hay errores de razonamiento frecuentes. La apelación a la novedad dice «es nueva, luego es mejor». El falso dilema presenta solo dos opciones cuando hay más, como «o se prohíbe todo o se usa sin límites». La generalización apresurada concluye algo general a partir de un caso, como «lo probé una vez y funcionó, entonces siempre funciona».",
    ],
    vocab=[("tesis", "postura que se defiende"), ("argumento", "razón apoyada en evidencia"), ("contraargumento", "razón en contra de la tesis que se reconoce y responde"), ("postura matizada", "posición con condiciones, sin extremos"), ("falso dilema", "presentar solo dos opciones cuando hay más"), ("generalización apresurada", "concluir algo general desde un solo caso")],
    worked=[
        ("Armar un juicio", "Escribe las partes de un juicio sobre paneles solares de techo, con datos de ejemplo.", ["Tesis: conviene adoptarlos con condiciones.", "Argumento: ahorran energía en el 70 % de 50 hogares de ejemplo; contraargumento: generan residuos al final; conclusión: adoptarlos con un plan de reciclaje."], "Tesis, argumento con dato, contraargumento y conclusión con condición"),
        ("Detectar un falso dilema", "«O prohibimos los asistentes automáticos o dejamos que hagan todas las tareas». ¿Qué error tiene?", ["Presenta solo dos opciones extremas.", "Existen opciones intermedias, como usarlos con reglas."], "Falso dilema"),
    ],
    mistakes=[
        ("Presentar solo los argumentos a favor.", "Sin contraargumentos no hay análisis crítico.", "Incluye al menos una razón en contra y respóndela."),
        ("Defender una postura extrema sin evidencia.", "No se puede revisar ni discutir.", "Apóyate en datos de los cuatro criterios y agrega condiciones."),
    ],
    R=[
        ("La tesis es… A) la postura que se defiende B) un dato de una tabla", "A", "Los datos son evidencia; la tesis es la postura."),
        ("Un contraargumento es… A) una razón en contra de mi postura que debo reconocer y responder B) una repetición de mi tesis", "A", "Reconocerlo hace más sólido el juicio."),
        ("Un argumento sólido se apoya en… A) evidencia que se puede revisar B) la insistencia", "A", "Repetir no es probar."),
    ],
    C=[
        ("«Es nueva, por lo tanto es mejor» es… A) una apelación a la novedad, no a la evidencia B) un dato medido", "A", "La novedad no prueba que sea mejor."),
        ("«O se prohíbe por completo o se usa sin límites» es… A) un falso dilema, porque hay opciones intermedias B) una conclusión sólida", "A", "Ignora alternativas como usarla con reglas."),
        ("«Lo probé una vez y funcionó, entonces siempre funciona» es… A) una generalización apresurada B) un argumento sólido", "A", "Un caso no basta para una conclusión general."),
    ],
    A=[
        ("Ordena las partes de un juicio: (a) conclusión, (b) tesis, (c) argumentos con evidencia, (d) contraargumento y respuesta.", "b, c, d, a", "Se parte con la postura y se termina con la conclusión."),
        ("Clasifica como tesis (T), evidencia (E) o contraargumento (C): (1) «conviene adoptarla con condiciones», (2) «el 70 % de 50 hogares de ejemplo ahorró energía», (3) «algunos hogares no tienen cómo instalarla».", "1 T, 2 E, 3 C", "La primera es la postura, la segunda un dato y la tercera una razón en contra."),
        arith("Una innovación se evalúa en 4 criterios (ético, económico, ambiental y social) y resulta favorable en 3. ¿Qué porcentaje de criterios son favorables?", "3*100//4", "Se divide entre el total y se pasa a porcentaje.", " %"),
    ],
    Z=[
        ("Alguien afirma que una innovación «siempre es buena». ¿Cómo se reformula con matiz?", "Es útil si se cumplen ciertas condiciones y se protege a quien queda fuera", "Una postura matizada incluye condiciones."),
        ("Un texto cita solo las ventajas de una innovación. ¿Qué le falta para ser crítico?", "Contraargumentos y evidencia sobre los perjuicios", "Un juicio crítico mira ambos lados."),
    ],
    D=[
        arith("Cada criterio vale 25 puntos. La innovación logra ético 25, económico 15, ambiental 20 y social 10. ¿Cuántos puntos suma en total?", "25+15+20+10", "Se suman los puntos de los cuatro criterios.", " puntos"),
        ex("¿Cuál es la mejor tesis? A) «Las innovaciones siempre mejoran la vida» B) «Esta innovación conviene si se protegen los datos y se ofrece una alternativa presencial» C) «No sirve porque nadie la quiere»", "B", "Es matizada, tiene condiciones y se puede discutir con evidencia."),
    ],
    ctx=arith("Un debate de ejemplo tiene 3 rondas de 4 minutos para cada una de 2 posturas. ¿Cuántos minutos dura en total?", "3*4*2", "Se multiplican rondas, minutos y posturas.", " minutos"),
    sc=[
        ("¿Cuáles son las cuatro partes de un juicio crítico?", "Tesis, argumentos, contraargumento y conclusión", "Son las partes de la clase."),
        ("En Tecnología: ¿qué es un falso dilema?", "Presentar solo dos opciones cuando hay más", "Oculta alternativas intermedias."),
        ("¿Qué es una postura matizada?", "Una posición con condiciones, sin extremos", "Se apoya en la evidencia."),
    ],
    open_task=(
        "Escoge una innovación de ejemplo. Opción 1: paneles solares en los techos de un barrio, con datos de ejemplo (ahorran energía en 35 de 50 hogares; generan residuos al final de su vida útil; 12 de 50 hogares no tienen techo apto). Opción 2: reparto a domicilio (acorta traslados; aumenta envases; 40 de 100 repartidores no tienen contrato de ejemplo). Opción 3: asistente automático para tareas (ahorra tiempo en 30 de 40 estudiantes; 10 de 40 dejan de practicar sin él). Escribe un juicio de 8 a 10 oraciones con tesis matizada, dos argumentos con datos, un contraargumento respondido y una conclusión con una condición.",
        "Opción 1: tesis, conviene adoptarlos con un plan de reciclaje; argumento, 35 de 50 hogares ahorran, es decir 70 %; contraargumento, 12 de 50 no pueden instalarlos, y se responde con un sistema comunitario; conclusión, adoptarlos si el barrio acuerda esa condición",
        ["tesis matizada", "dos argumentos con datos", "un contraargumento respondido", "una conclusión con condición"],
        ["texto de 8 a 10 oraciones"],
        ["postura extrema", "sin contraargumento"],
        "Pregunta: «¿qué dato te haría cambiar de postura?». Muestra si la postura se apoya en evidencia.",
    ),
    reinforce="Escribe una oración con tesis sobre una tecnología que uses y una razón en contra de tu propia postura.",
    extend="Explica por qué reconocer un contraargumento hace más fuerte un juicio y no más débil.",
)

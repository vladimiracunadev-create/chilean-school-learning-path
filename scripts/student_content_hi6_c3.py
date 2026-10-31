"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 25 (evaluar soluciones y justificar la elección)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI06 OA 25"
MAT = "Lápiz y papel. Los casos, las tablas y los datos están escritos en cada ejercicio; no necesitas internet ni comprar nada."

CASO = "Colegio San Martín (inventado): cada día de lluvia se forma un charco en la entrada. Opción A, instalar un canal de desagüe: cuesta $60.000 y tarda 3 semanas. Opción B, poner tarimas de madera sobre el charco: cuesta $25.000 y tarda 1 semana. Opción C, esperar que el municipio lo arregle: cuesta $0 y no se sabe cuándo ocurrirá. El colegio tiene $30.000 y 2 semanas."

# ---------------------------------------------------------------- Clase 1
build(
    OA, 1, "",
    use="Aprenderé a describir un problema, ubicar dónde y cuándo ocurre, y fijar criterios para comparar posibles soluciones. Sirve para elegir una solución con razones y no por gusto.",
    prior=["Sé hacer un plan y un presupuesto simples.", "Sé revisar la procedencia de un dato.", "Sé que un problema tiene causas y consecuencias."],
    explain=[
        "Un problema es la diferencia entre la situación actual y la situación que deseamos. Para evaluar soluciones primero lo describo bien: ¿qué ocurre?, ¿dónde?, ¿cuándo? y ¿a quiénes afecta? Si el problema está mal descrito, las soluciones no calzan. Por ejemplo, un charco en la entrada de un colegio ocurre cuando llueve y afecta a todos los que entran.",
        "Luego busco varias soluciones posibles. Escribir solo una nos obliga a aceptarla aunque no sea buena. Una vez que tengo opciones, fijo los criterios, que son las reglas con las que voy a compararlas: cuánto cuesta, cuánto tarda, cuántas personas se necesitan y qué efecto tiene. Los criterios se definen antes de comparar, para no elegir por simpatía.",
        "Después reviso cada opción con los mismos criterios. Una opción cumple un criterio si queda dentro del límite que tenemos. Si tengo $30.000 y la opción cuesta $60.000, no cumple el criterio de costo. Si no se sabe cuándo ocurrirá, no puedo asegurar que cumpla el plazo. Solo con datos conocidos puedo evaluar bien.",
    ],
    vocab=[("problema", "diferencia entre la situación actual y la que se desea"), ("solución", "acción que busca resolver un problema"), ("criterio", "regla con la que se comparan las opciones"), ("alternativa", "una de las opciones posibles"), ("límite", "valor máximo que se puede gastar, tardar o usar")],
    worked=[
        ("Describir el problema", "Cada día de lluvia se forma un charco en la entrada del colegio y los estudiantes se mojan los zapatos. ¿Cuándo ocurre y a quiénes afecta?",
         ["Busco cuándo: los días de lluvia.", "Busco a quiénes: a los estudiantes que entran."], "Ocurre los días de lluvia y afecta a los estudiantes que entran"),
        ("Aplicar un criterio de costo", "Una solución cuesta $15.000 y el colegio tiene un límite de $20.000. ¿Cumple el criterio de costo?",
         ["Comparo el costo con el límite.", "15.000 es menor que 20.000."], "Sí, cumple"),
    ],
    mistakes=[
        ("Elegir la primera solución que suena bien.", "No se comparó con otras ni con criterios.", "Escribe varias opciones y compáralas con los mismos criterios."),
        ("Definir los criterios después de elegir.", "Se acomodan los criterios para justificar lo que ya se quería.", "Fija los criterios antes de comparar."),
    ],
    T=[
        ("En Historia: ¿qué es un problema?", "La diferencia entre la situación actual y la que se desea", "Es lo que se quiere cambiar."),
        ("¿Qué es un criterio para evaluar soluciones?", "Una regla con la que se comparan las opciones", "Permite juzgar todas del mismo modo."),
        ("En Historia: ¿Qué es una alternativa?", "Una de las opciones posibles para resolver el problema", "Se necesita más de una para comparar."),
        ("¿Por qué se describe dónde y cuándo ocurre un problema antes de buscar soluciones?", "Para que las soluciones calcen con la situación real", "Un problema mal descrito lleva a soluciones que no sirven."),
        ("¿Por qué se escriben varias soluciones antes de elegir?", "Para poder compararlas", "Con una sola no hay comparación."),
        ("¿Por qué los criterios se fijan antes de comparar?", "Para no elegir por simpatía", "Así todas se juzgan con las mismas reglas."),
        (CASO + " ¿Qué opciones caben dentro del límite de $30.000?", "La B y la C", "A cuesta más que el límite."),
        ("=", "Para la opción A del caso del charco, que cuesta $60.000, y un colegio con $30.000, ¿cuántos pesos faltan?", "60000-30000", "Se resta el dinero disponible al costo."),
        (CASO + " ¿Qué opción asegura estar lista dentro del plazo de 2 semanas?", "La B", "Tarda 1 semana, mientras A tarda 3 y de C no se sabe."),
        ("En el caso del charco, ¿por qué no se puede evaluar bien la opción C con el criterio de tiempo?", "Porque no se sabe cuándo el municipio la hará", "Falta un dato conocido."),
        ("Un compañero elige la opción A «porque suena más profesional». ¿Qué error comete?", "No usa criterios para elegir", "Decide por gusto y no por razones."),
        ("Para un problema de ruido en la biblioteca, el límite es $10.000 y 10 días. Opción X, carteles: $5.000 y 2 días. Opción Y, alfombra: $90.000 y 7 días. Opción Z, turnos de silencio: $0 y 7 días. ¿Cuáles opciones cumplen ambos límites?", "X y Z", "Y supera el costo."),
        ("=", "Las 20 familias de un curso comparten por partes iguales el costo de $25.000 de una solución. ¿Cuánto aporta cada una?", "25000//20", "Se reparte el costo entre las familias."),
    ],
    ctx=("En tu colegio, el patio se llena de papeles después del recreo. Un curso propone poner más basureros, otro propone una campaña de afiches. Antes de elegir, ¿qué debe hacer el equipo con esas opciones?", "Compararlas con los mismos criterios", "Sin criterios se elige por gusto."),
    sc=[("En Historia: ¿qué es un criterio?", "Una regla con la que se comparan las opciones", "Es la idea de la clase."),
        ("¿Cuándo cumple una opción el criterio de costo?", "Cuando cuesta igual o menos que el límite", "Se compara con el dinero disponible."),
        ("¿Por qué conviene tener varias alternativas?", "Para poder comparar y elegir mejor", "Una sola no permite elegir.")],
    op=("Lee este problema: en el patio de un colegio no hay sombra en el verano y los estudiantes no pueden jugar al mediodía. Límite: $40.000 y 3 semanas. Opción 1, toldo: $35.000 y 1 semana. Opción 2, plantar árboles pequeños: $20.000 y 2 semanas, pero crecen en años. Opción 3, techo fijo: $120.000 y 6 semanas. Escribe cuándo ocurre el problema y a quiénes afecta. Luego escribe qué opciones cumplen el costo y el plazo, y con una frase di cuál preferirías.",
        "El problema ocurre en verano, al mediodía, y afecta a los estudiantes. Cumplen costo y plazo la opción 1 y la 2. La 3 no cumple. Prefiero la 1 porque da sombra de inmediato, mientras los árboles tardan años.",
        ["describe cuándo y a quiénes", "revisa costo y plazo de cada opción", "elige con una razón"], ["un texto breve con descripción, revisión de cada opción y elección"], ["elegir sin revisar el plazo", "no descartar la opción que pasa el límite"], "Lee tu elección a una persona de tu casa y pídele que repita los límites."),
    reinforce="Describe un problema pequeño de tu casa y escribe tres alternativas para resolverlo.",
    extend="Escribe dos criterios que usarías para elegir una solución a un problema de tu barrio.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
FUENTES = "Fuente 1: informe firmado por el director de la Escuela Río, de este año: con salida por turnos, el tiempo de salida bajó de 25 a 10 minutos. Fuente 2: volante sin firma que dice «los turnos no sirven». Fuente 3: aviso de una empresa de portones que dice «un portón nuevo lo resuelve todo»."
build(
    OA, 2, "",
    use="Aprenderé a buscar y revisar evidencia sobre si una solución funciona. Sirve para evaluar soluciones con datos confiables y no con promesas.",
    prior=["Sé describir un problema y fijar criterios.", "Sé revisar la procedencia de una fuente.", "Sé calcular restas y promedios simples."],
    explain=[
        "Evidencia es un dato o una experiencia que muestra si una solución funciona. Por ejemplo, un informe que cuenta que, en otra escuela, la salida por turnos bajó el tiempo de salida de 25 a 10 minutos. Para usarla reviso su procedencia: quién la hizo, cuándo y para qué. Un informe firmado y fechado es más confiable que un volante sin firma o un aviso que quiere vender.",
        "Hay que tener cuidado al copiar soluciones. Lo que funcionó en una escuela de 1.200 estudiantes puede no funcionar igual en una de 150. Por eso conviene hacer una prueba piloto: probar la solución a pequeña escala, por ejemplo una semana, y medir. Con los datos de la prueba calculo el promedio, que es la suma de los datos dividida por el número de datos.",
        "Un solo caso no es suficiente evidencia. «A mí me funcionó en mi casa» sirve como pista, pero no prueba nada para un colegio. Es más fuerte tener varias fuentes que coinciden y una prueba propia. Anoto siempre de dónde viene cada evidencia para poder justificar mi elección.",
    ],
    vocab=[("evidencia", "dato o experiencia que muestra si una solución funciona"), ("prueba piloto", "ensayo de una solución a pequeña escala antes de adoptarla"), ("promedio", "suma de los datos dividida por el número de datos"), ("fuente", "origen de la información"), ("medir", "obtener un número que describe un resultado")],
    worked=[
        ("Elegir la mejor evidencia", "Informe firmado por el director del Liceo Alba, este año: una prueba de 5 días con filas ordenadas redujo los atrasos de 30 a 12 por semana. Aviso sin firma: «el nuevo método es perfecto». ¿Cuál es mejor evidencia?",
         ["Reviso quién y cuándo.", "El informe tiene firma, fecha y números."], "El informe del director"),
        ("Calcular un promedio", "En una prueba, el tiempo de salida fue de 20, 18 y 16 minutos. ¿Cuál es el promedio?",
         ["Sumo: 20 + 18 + 16 = 54.", "Divido por 3 datos: 54 ÷ 3."], "18 minutos"),
    ],
    mistakes=[
        ("Creer una promesa de venta como si fuera evidencia.", "Quien vende gana si la gente le cree.", "Pide datos de una fuente que no gane con la venta."),
        ("Copiar una solución sin probarla en tu lugar.", "Cada lugar tiene tamaños y condiciones distintas.", "Haz una prueba piloto y mide."),
    ],
    T=[
        ("En Historia: ¿qué es la evidencia sobre una solución?", "Un dato o experiencia que muestra si la solución funciona", "Permite evaluar con razones."),
        ("¿Qué es una prueba piloto?", "Un ensayo de la solución a pequeña escala antes de adoptarla", "Sirve para medir antes de decidir."),
        ("¿Qué es el promedio de unos datos?", "La suma de los datos dividida por el número de datos", "Resume los datos en un valor."),
        ("¿Por qué una evidencia de otra escuela puede no calzar con tu colegio?", "Porque el tamaño y las condiciones pueden ser distintos", "El contexto cambia el resultado."),
        ("¿Por qué conviene hacer una prueba piloto antes de adoptar una solución?", "Para ver si funciona en tu lugar con pocos recursos", "Reduce el riesgo."),
        ("¿Por qué «a mí me funcionó en mi casa» es una evidencia débil para un colegio?", "Porque es un solo caso", "No representa a un grupo grande."),
        (FUENTES + " ¿Cuál es la mejor evidencia sobre si los turnos sirven?", "La fuente 1", "Está firmada, fechada y trae números."),
        ("=", "Según la fuente 1, el tiempo de salida bajó de 25 a 10 minutos. ¿Cuántos minutos bajó?", "25-10", "Se resta el tiempo final al inicial."),
        (FUENTES + " ¿Qué sesgo tiene la fuente 3?", "Busca vender portones", "Su interés es la venta."),
        ("La Escuela Río tiene 1.200 estudiantes y tu colegio tiene 150. ¿Qué conviene hacer antes de copiar sus turnos?", "Hacer una prueba piloto en tu colegio", "El tamaño es muy distinto."),
        ("Un vecino dice: «A mí me funcionó, así que sirve para todos». ¿Qué le respondes?", "Que un caso no basta y hay que probar en el grupo", "Un caso no representa a los demás."),
        ("Ordena los pasos: A) buscar evidencia con procedencia, B) comparar la solución con los criterios, C) hacer una prueba piloto, D) decidir.", "A, B, C, D", "Primero evidencia, luego comparación, prueba y decisión."),
        ("=", "En una prueba piloto de 5 días, el tiempo de salida fue de 12, 11, 10, 9 y 8 minutos. ¿Cuál es el promedio en minutos?", "(12+11+10+9+8)//5", "Se suman los datos y se divide por 5."),
    ],
    ctx=("Tu curso quiere probar una nueva forma de entregar los libros de la biblioteca. Una amiga cuenta que en su colegio funcionó, pero no tiene datos. ¿Qué evidencia pedirías para decidir?", "Un informe con datos, fecha y quién lo hizo", "Así se puede comprobar."),
    sc=[("En Historia: ¿qué es una prueba piloto?", "Un ensayo a pequeña escala antes de adoptar la solución", "Es la idea de la clase."),
        ("¿Qué se pregunta para saber si una fuente sirve?", "Quién, cuándo y para qué", "Es su procedencia."),
        ("En Historia: ¿Cómo se calcula un promedio?", "Se suman los datos y se divide por cuántos son", "Es la definición.")],
    op=("Lee: Fuente A, informe firmado por la encargada de una biblioteca, este año: con préstamos por turnos, las filas bajaron de 40 a 16 minutos en 5 días de prueba. Fuente B, mensaje sin nombre que dice «esa idea no sirve». Tu biblioteca es más chica. Escribe cuál fuente usarías y por qué, qué prueba piloto harías (cuántos días y qué medirías) y una opinión sobre si adoptar la solución.",
        "Uso la fuente A porque tiene firma, fecha y números. Haría una prueba de 5 días midiendo el tiempo de fila. Mi biblioteca es más chica, así que probaré primero. Si las filas bajan, adoptaré los turnos.",
        ["elige la mejor fuente con una razón", "describe una prueba piloto con días y medida", "opina con la evidencia"], ["elección de fuente, prueba piloto y opinión"], ["usar el mensaje anónimo", "no medir nada"], "Muéstrale a una persona de tu casa tu prueba piloto y pídele que encuentre qué mides."),
    reinforce="Anota tres datos que mediste en tu casa esta semana, como minutos que tardas en llegar al colegio, y calcula el promedio.",
    extend="Escribe dos preguntas para descubrir si una solución de otro colegio sirve para el tuyo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
TABLA = "Tabla de puntos (3 es lo mejor, 1 lo peor). A, más basureros: costo 1, efecto 3, facilidad 2. B, campaña de afiches: costo 3, efecto 1, facilidad 3. C, turnos de limpieza voluntarios: costo 3, efecto 2, facilidad 1."
build(
    OA, 3, "",
    use="Aprenderé a evaluar una solución mirando sus efectos, quiénes se benefician o se perjudican y sus riesgos. Sirve para comparar opciones con una tabla de puntos y no dejar efectos ocultos.",
    prior=["Sé fijar criterios y revisar evidencia.", "Sé sumar puntos de una tabla.", "Sé distinguir beneficios y costos."],
    explain=[
        "Para evaluar una solución me pregunto qué causará. Un efecto es lo que ocurre a raíz de la solución. Algunos son buscados, como menos basura en el patio. Otros son efectos secundarios, que ocurren además y no siempre se esperan. Por ejemplo, más basureros pueden atraer insectos si nadie los vacía. También pienso en los actores: quiénes ganan, quiénes pierden y quiénes deben encargarse.",
        "Un riesgo es algo que podría salir mal. Para cada solución pienso un riesgo y cómo reducirlo. También miro los efectos a corto plazo, que ocurren pronto, y a largo plazo, que ocurren después. Una campaña de afiches puede notarse rápido pero perder fuerza en un mes, mientras que un hábito nuevo puede tardar en llegar y durar años.",
        "Una tabla de puntos ayuda a comparar. Asigno 1, 2 o 3 puntos a cada criterio, siendo 3 lo mejor, y sumo. La opción con más puntos cumple mejor los criterios, pero reviso los efectos y riesgos antes de decidir. La tabla ordena mi razonamiento, no lo reemplaza.",
    ],
    vocab=[("efecto", "lo que ocurre a raíz de una solución"), ("efecto secundario", "efecto no buscado que ocurre además del esperado"), ("riesgo", "algo que podría salir mal"), ("factibilidad", "qué tan posible es llevar a cabo una solución"), ("puntaje", "total de puntos que suma una opción")],
    worked=[
        ("Sumar una tabla", "Solución D: costo 2, efecto 3, facilidad 3. ¿Cuánto suma?",
         ["Sumo los tres puntos.", "2 + 3 + 3 = 8."], "8 puntos"),
        ("Detectar un efecto secundario", "Se instalan basureros nuevos en una plaza y nadie los vacía durante semanas. ¿Qué efecto secundario puede aparecer?",
         ["Pienso qué pasa con basureros llenos.", "Pueden atraer insectos y dar mal olor."], "Insectos y mal olor"),
    ],
    mistakes=[
        ("Mirar solo el efecto buscado.", "Los efectos secundarios pueden anular el beneficio.", "Pregunta qué más puede ocurrir y a quién afecta."),
        ("Elegir solo por el puntaje sin pensar en los riesgos.", "La tabla no incluye todos los riesgos.", "Revisa riesgos y quién se encarga antes de decidir."),
    ],
    T=[
        ("¿Qué es un efecto secundario?", "Un efecto no buscado que ocurre además del esperado", "Aparece junto al efecto principal."),
        ("En Historia: ¿Qué es un riesgo?", "Algo que podría salir mal", "Se anticipa para reducirlo."),
        ("¿Qué indica el puntaje total en una tabla de puntos?", "Qué tan bien cumple la opción los criterios", "Más puntos significa mejor cumplimiento."),
        ("¿Por qué se pregunta quiénes ganan y quiénes pierden con una solución?", "Porque afecta a actores distintos", "Una solución puede ayudar a unos y perjudicar a otros."),
        ("¿Por qué no basta mirar solo el costo de una solución?", "Porque también importan su efecto y su factibilidad", "Un criterio solo no basta."),
        ("¿Por qué se miran efectos a corto y a largo plazo?", "Porque algunos ocurren pronto y otros mucho después", "Un efecto puede cambiar con el tiempo."),
        ("=", TABLA + " ¿Cuántos puntos suma la opción A?", "1+3+2", "Se suman costo, efecto y facilidad.", ""),
        ("=", TABLA + " ¿Cuántos puntos suma la opción B?", "3+1+3", "Se suman costo, efecto y facilidad.", ""),
        (TABLA + " ¿Cuál opción tiene el puntaje más alto?", "La B", "Suma 7, mientras A y C suman 6."),
        ("Más basureros pueden atraer insectos si nadie los vacía. ¿Qué medida reduce el riesgo: A) vaciarlos cada día, B) ponerlos más lejos de la plaza?", "A", "Retira la basura antes de que atraiga insectos."),
        ("La opción C depende de que 10 estudiantes hagan turnos cada semana y solo 4 se inscriben. ¿Qué criterio se ve afectado?", "La facilidad o factibilidad", "No hay suficientes personas para hacerla."),
        ("=", "Otra tabla: D tiene costo 3, efecto 3 y facilidad 1; E tiene costo 2, efecto 2 y facilidad 2. ¿Cuántos puntos más tiene D que E?", "(3+3+1)-(2+2+2)", "Se comparan los dos totales."),
        ("Ordena la cadena de efectos: A) disminuye la basura, B) se instalan más basureros, C) los basureros se vacían cada día.", "B, C, A", "Primero la acción, luego su uso y después el resultado."),
    ],
    ctx=("Un curso quiere evitar que se rayen las mesas de la sala. Propone una campaña de afiches y turnos de limpieza semanal. ¿Qué riesgo debe prever en los turnos?", "Que se olviden o que nadie los haga", "Un riesgo es algo que puede salir mal."),
    sc=[("En Historia: ¿qué es un efecto secundario?", "Un efecto no buscado que ocurre además del esperado", "Es la idea clave."),
        ("¿Para qué sirve una tabla de puntos?", "Para comparar opciones con los mismos criterios", "Ordena el razonamiento."),
        ("¿Qué se revisa antes de decidir aunque una opción tenga más puntos?", "Los riesgos y los efectos secundarios", "La tabla no los muestra todos.")],
    op=("Un curso debe elegir entre dos soluciones para reducir el ruido en el pasillo. Solución 1, carteles: costo 3, efecto 1, facilidad 3. Solución 2, pasillo en filas: costo 3, efecto 2, facilidad 2. Suma los puntos de cada una. Escribe un efecto secundario posible de la solución 2 y un riesgo con una forma de reducirlo. Luego escribe cuál elegirías y por qué.",
        "Solución 1 suma 7 y solución 2 suma 7. Un efecto secundario de la solución 2: los pasillos se hacen más lentos. Riesgo: que se olviden las filas; lo reduzco con un recordatorio. Elijo la 2 porque su efecto es mayor aunque ambas suman igual.",
        ["suma los puntos de cada solución", "nombra un efecto secundario y un riesgo", "elige con una razón"], ["dos sumas, un efecto secundario, un riesgo y una elección"], ["decidir solo por el puntaje", "no pensar en riesgos"], "Pide a una persona de tu casa que revise tu suma."),
    reinforce="Piensa en una norma nueva en tu casa y escribe un efecto buscado y un efecto no buscado.",
    extend="Escribe dos riesgos de una solución y una medida para cada uno.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
build(
    OA, 4, "",
    use="Aprenderé a comparar cómo ven una solución distintas personas y distintos lugares. Sirve para elegir soluciones inclusivas y adecuadas al territorio.",
    prior=["Sé evaluar con criterios y evidencia.", "Sé sumar votos en una tabla.", "Sé que cada persona tiene una perspectiva."],
    explain=[
        "Una solución no es igual para todos. Para evaluarla escucho a distintos grupos: estudiantes, familias, docentes y personas con necesidades especiales. La inclusión significa diseñar para que todas las personas puedan participar. Por ejemplo, una rampa permite que una persona en silla de ruedas entre sola a un gimnasio, mientras que depender de que alguien la cargue no respeta su autonomía.",
        "Si votamos, la mayoría es la opción con más votos. Pero la mayoría no basta si deja sin respuesta una necesidad importante de un grupo más pequeño. Primero cuento los votos de todos los grupos y luego reviso si la opción ganadora cubre lo esencial de cada grupo. A veces se puede combinar partes de dos opciones para atender a más personas.",
        "El territorio también cambia lo que conviene. Un colegio de una zona lluviosa del sur puede necesitar techar la entrada para proteger de la lluvia. Uno de una zona desértica del norte puede necesitar sombra para protegerse del sol. Dos soluciones distintas pueden ser buenas si cada una responde a las condiciones de su lugar.",
    ],
    vocab=[("inclusión", "diseñar para que todas las personas puedan participar"), ("autonomía", "poder hacer algo por uno mismo sin depender de otros"), ("mayoría", "la opción con más votos"), ("territorio", "espacio con rasgos propios, como clima y recursos"), ("combinar", "juntar partes de dos opciones")],
    worked=[
        ("Contar votos de grupos", "Opción A: estudiantes 10, familias 4. Opción B: estudiantes 5, familias 11. ¿Cuántos votos tiene la opción B?",
         ["Sumo los votos de B.", "5 + 11 = 16."], "16 votos"),
        ("Revisar la inclusión", "Una escuela propone entrar al gimnasio solo por una escalera de 6 peldaños. ¿Qué grupo queda excluido?",
         ["Pienso quién no puede subir escaleras.", "Personas en silla de ruedas o con movilidad reducida."], "Las personas que no pueden subir escaleras"),
    ],
    mistakes=[
        ("Decidir solo por la mayoría sin mirar las necesidades de un grupo pequeño.", "Una necesidad esencial puede quedar sin respuesta.", "Revisa si la opción ganadora atiende lo esencial de cada grupo."),
        ("Copiar la solución de otro territorio.", "El clima y las condiciones cambian lo que sirve.", "Pregunta qué necesita tu lugar."),
    ],
    T=[
        ("¿Qué significa inclusión?", "Diseñar para que todas las personas puedan participar", "Nadie queda excluido."),
        ("¿Qué es la mayoría en una votación?", "La opción con más votos", "Se compara el total de cada opción."),
        ("¿Qué es la autonomía?", "Poder hacer algo por uno mismo sin depender de otros", "Es lo que busca una rampa."),
        ("¿Por qué se debe considerar a las personas con discapacidad al evaluar una solución?", "Para que también puedan participar", "La inclusión es un criterio."),
        ("¿Por qué la mayoría no basta para decidir siempre?", "Porque puede dejar sin respuesta una necesidad importante de un grupo", "Hay que revisar lo esencial de cada grupo."),
        ("¿Por qué lo que sirve en un territorio puede no servir en otro?", "Porque el clima y los recursos son distintos", "Cada lugar tiene sus condiciones."),
        ("=", "Votos por la opción A: estudiantes 18, familias 5, docentes 4. ¿Cuántos votos suma A?", "18+5+4", "Se suman los votos de los tres grupos."),
        ("=", "Votos por la opción B: estudiantes 6, familias 15, docentes 2. ¿Cuántos votos suma B?", "6+15+2", "Se suman los votos de los tres grupos."),
        ("Con A = 27 votos y B = 23 votos, ¿qué opción tiene la mayoría?", "La A", "Tiene más votos."),
        ("Para entrar al gimnasio hay tres ideas: A) rampa, B) puerta lateral plana abierta en horario, C) voluntarios que cargan a la persona. ¿Cuál no permite entrar con autonomía?", "La C", "Depende de que otras personas la carguen."),
        ("Un colegio del sur lluvioso techa la entrada y uno del norte desértico construye un sombreadero. ¿Por qué ambas soluciones pueden ser buenas?", "Porque cada una responde a las condiciones de su lugar", "El territorio es distinto."),
        ("=", "Entre las familias, B tiene 15 votos y A tiene 5. ¿Cuántos votos de diferencia hay?", "15-5", "Se resta el menor al mayor."),
        ("Los estudiantes prefieren A por comodidad y las familias prefieren B por costo. ¿Qué paso conviene: A) ignorar a uno de los grupos, B) buscar una solución que cumpla lo esencial de ambos?", "B", "Combinar atiende a más personas."),
    ],
    ctx=("Dos colegios, uno en una ciudad costera lluviosa del sur y otro en un pueblo seco del norte, quieren mejorar el patio. Uno propone techos y el otro sombra. Antes de copiar el proyecto del otro, ¿qué debe revisar cada colegio?", "Si el proyecto responde a las condiciones de su propio lugar", "El territorio cambia lo que conviene."),
    sc=[("En Historia: ¿qué es inclusión?", "Diseñar para que todas las personas puedan participar", "Es el criterio de la clase."),
        ("¿Qué se revisa además de la mayoría?", "Si se atiende lo esencial de cada grupo", "Evita dejar a alguien sin respuesta."),
        ("¿Por qué importa el territorio?", "Porque el clima y los recursos cambian la solución", "Cada lugar tiene sus condiciones.")],
    op=("Un club de barrio debe elegir entre dos canchas: Opción A, cancha techada, $150.000, protege de la lluvia. Opción B, cancha abierta con sombreaderos, $90.000. Votos: niños 20 por A y 8 por B; adultos mayores 4 por A y 9 por B; familias 6 por A y 5 por B. Suma los votos de cada opción y escribe qué grupo se beneficiaría con cada una. Propón una solución que atienda lo esencial de más de un grupo.",
        "A suma 30 votos y B suma 22. A beneficia a los niños, que juegan con lluvia. B beneficia a los adultos mayores por la sombra y el costo menor. Propongo cancha abierta con una parte techada, que cuida de la lluvia y del sol.",
        ["suma los votos de cada opción", "nombra qué grupo se beneficia", "propone una solución que combine necesidades"], ["dos sumas y una propuesta combinada"], ["decidir solo por el total de votos", "ignorar a un grupo"], "Pide a una persona de tu casa que revise tus sumas y diga qué grupo olvidaste."),
    reinforce="Pregunta a una persona de tu casa qué cambiaría de un lugar público de tu barrio para que más personas lo usen.",
    extend="Explica con tus palabras por qué una rampa es una solución inclusiva.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
TABLA5 = "Tabla con pesos (importancia): costo peso 1, efecto peso 3, facilidad peso 2. Puntos de 1 a 3, donde 3 es lo mejor. Opción A: costo 2, efecto 3, facilidad 1. Opción B: costo 3, efecto 2, facilidad 3."
JUST = "«Elegimos instalar afiches y turnos de limpieza porque cuestan $15.000, menos que el límite de $20.000. En la prueba de una semana, la basura bajó de 40 a 22 envoltorios por día. El riesgo es que los turnos se olviden; si ocurre, un responsable los recordará cada lunes.»"
build(
    OA, 5, "",
    use="Aprenderé a elegir una solución con una tabla con pesos y a justificar mi elección con criterios, evidencia y riesgos. Sirve para defender una decisión con razones que otras personas puedan revisar.",
    prior=["Sé comparar opciones con una tabla de puntos.", "Sé revisar la evidencia de una prueba.", "Sé calcular sumas, restas y multiplicaciones."],
    explain=[
        "No todos los criterios pesan igual. El peso es la importancia que le damos a un criterio. Si el efecto es lo más importante, le damos peso 3; si el costo importa menos, peso 1. Para calcular el puntaje multiplico cada punto por su peso y sumo. Así la opción que mejor cumple lo más importante obtiene más puntos.",
        "Justificar una elección es explicar con razones por qué elegí esa opción. Una buena justificación nombra los criterios que usé, entrega la evidencia que los apoya, reconoce un riesgo y dice cómo lo reduciré. También incluye un plan alternativo, que es qué haré si la solución no funciona. No sirve decir «porque me gusta más» ni «porque todos la quieren».",
        "Antes de entregar una justificación hago tres preguntas: ¿los criterios eran claros desde el comienzo?, ¿la evidencia viene de una fuente confiable? y ¿dije qué podría salir mal? Si cambia un peso o aparece un dato nuevo, reviso mi decisión. Cambiar una elección con buenas razones es una decisión madura.",
    ],
    vocab=[("peso", "importancia que se da a un criterio"), ("justificar", "explicar con razones por qué se eligió una opción"), ("plan alternativo", "lo que se hará si la solución no funciona"), ("evidencia", "dato que apoya una razón"), ("puntaje ponderado", "suma de los puntos multiplicados por su peso")],
    worked=[
        ("Puntaje ponderado", "Peso: costo 1, efecto 3. Opción X: costo 3, efecto 2. ¿Cuánto suma X?",
         ["Multiplico cada punto por su peso: 3 x 1 y 2 x 3.", "3 + 6 = 9."], "9 puntos"),
        ("Reconocer una buena justificación", "«Elegimos la B porque cuesta menos que el límite y en la prueba bajó el ruido. El riesgo es que se olviden las filas; pondremos un recordatorio.» ¿Qué partes tiene?",
         ["Hay criterio (costo) y evidencia (bajó el ruido).", "Hay un riesgo y una medida."], "Criterio, evidencia, riesgo y medida"),
    ],
    mistakes=[
        ("Justificar con «me gusta más» o «todos la quieren».", "No entrega criterios ni evidencia que se puedan revisar.", "Nombra el criterio y el dato que lo apoya."),
        ("No decir qué haremos si la solución falla.", "La decisión queda sin plan alternativo.", "Escribe un plan alternativo."),
    ],
    T=[
        ("¿Qué es el peso de un criterio?", "La importancia que se le da a ese criterio", "Un criterio más importante pesa más."),
        ("¿Qué es un plan alternativo?", "Lo que se hará si la solución no funciona", "Prepara una salida si falla."),
        ("¿Qué significa justificar una elección?", "Explicar con razones por qué se eligió esa opción", "Se apoya en criterios y evidencia."),
        ("¿Por qué «me gusta más» no es una buena justificación?", "Porque no entrega criterios ni evidencia que se puedan revisar", "Es una preferencia personal."),
        (JUST + " ¿Cuántos envoltorios por día bajó la basura según la prueba?", "18", "La basura bajó de 40 a 22 envoltorios, es decir, 18 menos."),
        (JUST + " ¿Qué parte es el riesgo?", "Que los turnos se olviden", "Es lo que podría salir mal."),
        ("=", TABLA5 + " ¿Cuántos puntos ponderados suma la opción A?", "2*1+3*3+1*2", "Se multiplica cada punto por su peso y se suma.", ""),
        ("=", TABLA5 + " ¿Cuántos puntos ponderados suma la opción B?", "3*1+2*3+3*2", "Se multiplica cada punto por su peso y se suma.", ""),
        (TABLA5 + " Con A suma 13 y B suma 15, ¿cuál opción cumple mejor los criterios según esta tabla?", "La B", "Tiene mayor puntaje ponderado."),
        ("Un compañero propone elegir A «porque siempre se ha hecho así». ¿Qué respondes?", "Que debe justificar con criterios y evidencia", "La costumbre no es una razón."),
        ("Si el peso del costo sube de 1 a 4 en la tabla (efecto 3, facilidad 2), A suma 19 y B suma 24. ¿Sigue ganando B?", "Sí", "B tiene 24 puntos, más que los 19 de A."),
        ("=", "Una solución cuesta $15.000 y el límite es $20.000. ¿Cuánto dinero sobra?", "20000-15000", "Se resta el costo al límite."),
        ("Ordena una justificación: A) el riesgo y cómo se reduce, B) la elección, C) los criterios y la evidencia que la apoyan.", "B, C, A", "Elección, razones y riesgos."),
    ],
    ctx=("Tu curso eligió una solución con la tabla de puntos, pero en la prueba de una semana el resultado fue peor de lo esperado. ¿Qué debe hacer el curso según lo aprendido?", "Aplicar el plan alternativo o revisar la decisión con los datos nuevos", "Cambiar con buenas razones es válido."),
    sc=[("En Historia: ¿qué es justificar una elección?", "Explicar con razones por qué se eligió una opción", "Es la idea de la clase."),
        ("¿Cómo se calcula un puntaje ponderado?", "Multiplicando cada punto por su peso y sumando", "Considera la importancia de cada criterio."),
        ("¿Qué incluye una buena justificación?", "Criterios, evidencia, un riesgo y una medida", "Permite que otros la revisen.")],
    op=("Un curso debe elegir cómo reducir el desorden del patio al terminar el recreo. Pesos: costo 1, efecto 3, facilidad 2. Opción 1, aviso con campana y filas: costo 3, efecto 2, facilidad 3. Opción 2, nuevos juegos ordenados por turnos: costo 1, efecto 3, facilidad 2. Calcula el puntaje ponderado de cada una. Escribe una justificación de la que elijas con criterios, la evidencia de una prueba de un día en la que el desorden bajó de 25 a 15 estudiantes fuera de fila, un riesgo y un plan alternativo.",
        "Opción 1: 3x1 + 2x3 + 3x2 = 15. Opción 2: 1x1 + 3x3 + 2x2 = 14. Elijo la 1 porque cuesta menos y es fácil. Evidencia: en la prueba de un día, el desorden bajó de 25 a 15 estudiantes fuera de fila. Riesgo: que se olvide la campana. Plan alternativo: encargar la campana a un responsable.",
        ["calcula los dos puntajes", "justifica con criterios y evidencia", "incluye riesgo y plan alternativo"], ["dos cálculos y una justificación completa"], ["justificar con gusto personal", "olvidar el plan alternativo"], "Lee tu justificación a una persona de tu casa y pídele que marque el riesgo."),
    reinforce="Elige un problema de tu casa y escribe una solución con una razón y un plan alternativo.",
    extend="Cambia un peso de la tabla de la tarea abierta y comprueba si cambia la opción ganadora.",
    materials=MAT,
)

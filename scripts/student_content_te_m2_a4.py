"""Cuaderno del estudiante, 2.º medio Tecnología: OA 04 (comunicar propuestas de solución proyectando escenarios de cambio, con herramientas TIC, según objetivos y audiencias, con ética y normas de cuidado y seguridad), clases 1 a 5.

Seguridad: las tareas son de lectura, cálculo y escritura. Las herramientas TIC se nombran por tipo (presentación, infografía, documento); su uso real con equipos y cuentas queda para el docente. Todos los datos son de ejemplo.
"""
from __future__ import annotations

from student_content_te_m2_a import reg
from student_lessons import arith, ex

OA4 = "TE2M OA 04"

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir los objetivos de una comunicación (informar, persuadir, instruir), a describir a la audiencia y a elegir formato y lenguaje. Sirve para que una propuesta llegue a quien debe entenderla.",
    prior=["Sé qué es una propuesta de solución.", "Sé calcular porcentajes.", "Sé qué es un dato medido."],
    explain=[
        "Comunicar una propuesta es hacer llegar un mensaje a otras personas con un propósito. El objetivo puede ser informar (dar a conocer datos), persuadir (convencer de aprobar o apoyar algo) o instruir (enseñar cómo hacer algo paso a paso). El mismo tema cambia de forma según el objetivo. La audiencia es el grupo que recibe el mensaje: compañeros, docentes, directivos, familias o vecinos.",
        "Antes de preparar el mensaje se responden tres preguntas sobre la audiencia: qué sabe del tema, qué necesita saber y qué se quiere que haga después. Con eso se decide el lenguaje (simple o técnico), el nivel de detalle, el formato (afiche, infografía, resumen de una página, presentación) y el tiempo disponible. El mensaje central es la idea principal, dicha en una oración, que la audiencia debe recordar.",
        "Un mensaje se adapta, pero no se distorsiona. Se puede cambiar la forma de explicar los datos, no los datos mismos. Persuadir con exageraciones o culpando a personas no es ético. Un buen mensaje persuasivo usa datos verdaderos, dice qué se pide y qué beneficio traería.",
    ],
    vocab=[("objetivo", "propósito del mensaje: informar, persuadir o instruir"), ("audiencia", "personas que reciben el mensaje"), ("mensaje central", "idea principal que la audiencia debe recordar"), ("formato", "forma del mensaje, como afiche o resumen de una página"), ("persuadir", "convencer con razones y datos verdaderos"), ("instruir", "enseñar cómo hacer algo paso a paso")],
    worked=[
        ("Elegir el objetivo", "Un equipo quiere que estudiantes nuevos aprendan a separar los residuos en el patio. ¿Qué objetivo tiene?", ["Quiere enseñar un procedimiento.", "Eso es instruir."], "Instruir"),
        ("Elegir el formato", "Debe presentar una propuesta a directivos que solo tienen 5 minutos. ¿Qué formato conviene?", ["La audiencia tiene poco tiempo y debe decidir.", "Un resumen de una página con costo, ahorro y la decisión que se pide."], "Un resumen de una página"),
    ],
    mistakes=[
        ("Usar el mismo discurso para todas las audiencias.", "Cada grupo sabe y necesita cosas distintas.", "Pregúntate qué sabe, qué necesita y qué quieres que haga cada audiencia."),
        ("Exagerar un dato para convencer.", "Engaña a la audiencia y rompe la honestidad.", "Usa el dato medido y explica por qué importa."),
    ],
    R=[
        ("Convencer a la dirección de aprobar un punto de acopio es un objetivo de… A) persuadir B) instruir", "A", "Busca que la dirección apoye una decisión."),
        ("Mostrar los pasos para usar el punto de acopio es un objetivo de… A) instruir B) persuadir", "A", "Enseña cómo hacer algo paso a paso."),
        ("La audiencia es… A) las personas que recibirán el mensaje B) quien lo escribe", "A", "El mensaje se prepara pensando en quien lo recibe."),
    ],
    C=[
        ("Quieres explicar tu propuesta a vecinos que no conocen el tema técnico. ¿Qué lenguaje conviene? A) palabras simples y ejemplos cercanos B) vocabulario técnico con siglas", "A", "El lenguaje se ajusta a lo que la audiencia sabe."),
        ("Debes presentar ante directivos con 5 minutos. ¿Qué conviene preparar? A) una página con costo, ahorro y decisión pedida B) un informe de 40 páginas", "A", "Poco tiempo exige ir a lo esencial."),
        ("El mensaje central es… A) la idea principal, dicha en una oración, que la audiencia debe recordar B) el título del archivo", "A", "Es lo que más importa que quede en la memoria."),
    ],
    A=[
        ("Une cada situación con el formato más adecuado (afiche, resumen de una página, infografía de pasos): (1) invitar a vecinos a una jornada, (2) explicar costos a la dirección, (3) mostrar los pasos a estudiantes nuevos.", "1 afiche, 2 resumen de una página, 3 infografía de pasos", "Cada formato responde al objetivo y a la audiencia."),
        arith("Una presentación de ejemplo dura 12 minutos y reserva el 25 % para preguntas. ¿Cuántos minutos quedan para exponer?", "12-12*25//100", "Se calcula el tiempo de preguntas y se resta del total.", " minutos"),
        arith("Se encuesta a 25 personas del barrio y 20 prefieren recibir la información en un afiche. ¿Qué porcentaje es?", "20*100//25", "Se divide entre el total y se pasa a porcentaje.", " %"),
    ],
    Z=[
        ("Un equipo usa el mismo discurso técnico para vecinos y para ingenieros. ¿Qué error comete?", "No adapta el lenguaje y el detalle a lo que sabe cada audiencia", "El mensaje debe ajustarse al grupo que lo recibe."),
        ("Un afiche dice «¡Si no reciclas, destruyes el planeta!». ¿Qué problema ético tiene?", "Exagera y culpa a las personas en vez de informar con datos", "Un mensaje honesto usa datos verdaderos y no culpa."),
    ],
    D=[
        arith("Para la dirección, el equipo traduce el dato a dinero: se usan 90 vasos al día, a $30 cada uno, durante 5 días. ¿Cuánto cuesta por semana?", "90*30*5", "Se multiplican vasos, precio y días.", " pesos"),
        ex("El dato es 90 vasos al día, unos $13.500 por semana, y la meta es bajar 40 %. ¿Cuál frase es mejor para la dirección? A) «Gastamos 90 vasos al día, una cifra enorme que daña el planeta» B) «Gastamos unos $13.500 por semana en vasos; bajar 40 % ahorra $5.400» C) «Con otro sistema podríamos ahorrar muchísimo dinero en vasos»", "B", "La mejor frase trae el dato en dinero, la meta y el beneficio; las otras exageran o no entregan cifras.", calc=None),
    ],
    ctx=arith("A una reunión de ejemplo asisten 120 personas y el 30 % son familias. ¿Cuántas familias son?", "120*30//100", "Se calcula el 30 % de 120.", " familias"),
    sc=[
        ("Nombra los tres objetivos de comunicación de la clase.", "Informar, persuadir e instruir", "Son los propósitos posibles de un mensaje."),
        ("¿Qué tres preguntas se hacen sobre la audiencia?", "Qué sabe, qué necesita y qué se quiere que haga", "Con ellas se elige lenguaje y formato."),
        ("¿Se puede cambiar el dato para convencer mejor?", "No, solo se cambia la forma de explicarlo", "Distorsionar datos es poco ético."),
    ],
    open_task=(
        "Escoge un caso de ejemplo. Caso 1: un curso bajó 20 % sus hojas por semana, de 100 a 80, y quiere que la dirección compre cuadernillos reutilizables. Caso 2: un equipo debe enseñar a un 1.º medio a usar un punto de acopio de papel y cartón. Caso 3: un grupo quiere informar a las familias que el consumo de energía de la sala bajó 15 kWh en un mes. Define el objetivo, describe la audiencia (qué sabe, qué necesita y qué debe hacer), escribe el mensaje central en una oración y elige formato y lenguaje.",
        "Caso 1: objetivo persuadir; audiencia, la dirección, que no conoce el consumo; debe aprobar la compra; mensaje central, bajamos 20 % las hojas y podemos seguir bajando; formato, resumen de una página con datos",
        ["define el objetivo", "describe qué sabe, qué necesita y qué debe hacer la audiencia", "el mensaje central cabe en una oración", "formato y lenguaje coherentes con la audiencia"],
        ["hoja con las cuatro partes"],
        ["no distinguir objetivo y audiencia", "un mensaje central largo"],
        "Pregunta: «¿qué quieres que haga esta audiencia cuando termine?». Si no puede responder, el objetivo no está claro.",
    ),
    reinforce="Escribe cómo contarías el consumo de energía de tu casa a tu familia y cómo se lo contarías a una autoridad del barrio.",
    extend="Explica por qué adaptar un mensaje a la audiencia no es lo mismo que cambiar los datos.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los datos escritos en este cuaderno.",
    use="Aprenderé a proyectar escenarios de cambio (base, optimista y pesimista), a calcular una proyección simple y a explicar sus supuestos. Sirve para comunicar qué podría pasar si se aplica la propuesta y qué podría pasar si no.",
    prior=["Sé calcular porcentajes.", "Sé qué es una meta y una línea base.", "Sé multiplicar y restar números enteros."],
    explain=[
        "Un escenario es una descripción de lo que podría ocurrir en el futuro si se cumplen ciertas condiciones. El escenario base muestra qué pasaría sin hacer ningún cambio. El escenario optimista supone que la propuesta funciona muy bien, el pesimista supone que funciona poco, y uno intermedio supone un cumplimiento parcial. Compararlos muestra el impacto posible de actuar.",
        "Una proyección simple usa un cambio constante por período: valor futuro = valor actual ± cambio por período × número de períodos. Por ejemplo, si hoy se gastan 200 kWh y bajan 15 cada mes, en 4 meses se gastarán 200 − 15 × 4 = 140 kWh. Esto es una aproximación, no una certeza.",
        "Toda proyección descansa en supuestos: cosas que se dan por ciertas para poder calcular, como que el número de estudiantes no cambia. Los supuestos se escriben junto al resultado. Como el futuro es incierto, conviene comunicar un rango entre el escenario pesimista y el optimista, y decir que se medirá para comprobarlo.",
    ],
    vocab=[("escenario", "descripción de lo que podría ocurrir bajo ciertas condiciones"), ("escenario base", "lo que pasaría sin hacer ningún cambio"), ("proyección", "cálculo del valor futuro a partir de un cambio constante"), ("supuesto", "condición que se da por cierta para poder calcular"), ("rango", "intervalo entre el escenario pesimista y el optimista"), ("incertidumbre", "lo que no se puede saber con certeza del futuro")],
    worked=[
        ("Proyectar a varios meses", "Hoy un taller gasta 200 kWh al mes y baja 15 kWh cada mes. ¿Cuánto gastará dentro de 4 meses?", ["Cambio total: 15 × 4 = 60.", "Resto: 200 − 60 = 140."], "140 kWh"),
        ("Comparar dos escenarios", "Escenario base: 90 vasos al día, 5 días, 4 semanas. Con la propuesta bajan 40 %. ¿Cuántos vasos se evitan en 4 semanas?", ["Base: 90 × 5 × 4 = 1.800 vasos.", "Se evita el 40 %: 1.800 × 40 ÷ 100 = 720."], "720 vasos"),
    ],
    mistakes=[
        ("Presentar la proyección como si fuera una certeza.", "El futuro depende de supuestos que pueden cambiar.", "Comunica un rango y escribe los supuestos."),
        ("Comparar la propuesta solo con la situación ideal.", "Sin escenario base no se ve cuánto cambia realmente.", "Calcula siempre qué pasaría sin cambios."),
    ],
    R=[
        ("El escenario base es… A) lo que ocurriría si no se hace nada B) lo que ocurre si se logra toda la meta", "A", "Es el punto de comparación."),
        arith("Un curso de ejemplo usa 120 hojas por semana y baja 10 hojas cada semana. ¿Cuántas usará después de 5 semanas?", "120-10*5", "Se resta el cambio total del valor actual.", " hojas"),
        ("Un supuesto es… A) algo que se da por cierto para poder proyectar B) un dato medido en la prueba", "A", "Los supuestos hacen posible calcular, pero pueden cambiar."),
    ],
    C=[
        ("¿Por qué se comunica un rango, por ejemplo entre 700 y 900, y no un solo número? A) porque el futuro es incierto y los supuestos pueden cambiar B) porque así se evitan los cálculos", "A", "Un rango refleja honestamente lo que se sabe."),
        ("Un equipo proyecta el ahorro de todo un año con los datos de un solo día. ¿Qué problema tiene? A) un día no representa al resto del año B) ninguno, porque los datos de un día son exactos", "A", "Un solo dato no sustenta una proyección larga."),
        ("Los escenarios optimista y pesimista sirven para… A) mostrar los extremos posibles B) elegir el que más gusta", "A", "Muestran el rango de lo que podría ocurrir."),
    ],
    A=[
        arith("Escenario base: 300 hojas al mes. Con la propuesta bajan 30 %. ¿Cuántas hojas se ahorran en 6 meses?", "300*30//100*6", "Se calcula el ahorro mensual y se multiplica por los meses.", " hojas"),
        arith("Una propuesta de ejemplo ahorra 15 kWh al mes y el precio es $200 por kWh. ¿Cuánto dinero ahorra en 12 meses?", "15*12*200", "Se multiplica los kWh de los meses por el precio.", " pesos"),
        ("Une cada situación con su escenario (base, optimista, parcial): (1) nadie cambia sus hábitos, (2) todos cumplen la propuesta, (3) la mitad cumple la propuesta.", "1 base, 2 optimista, 3 parcial", "Cada uno describe un nivel distinto de cumplimiento."),
    ],
    Z=[
        ("Un equipo afirma que ahorrará 30 % durante 10 años, sin explicar sus supuestos. ¿Qué falla tiene?", "No explica qué se supone constante y no reconoce que el futuro es incierto", "Una proyección sin supuestos no se puede revisar."),
        ("Un compañero dice: «El escenario con la propuesta es una promesa». ¿Qué se responde?", "Es una proyección basada en supuestos que se comprobará midiendo", "Las proyecciones se verifican con datos posteriores."),
    ],
    D=[
        arith("Un curso de ejemplo usa hoy 80 hojas por semana. Si nada cambia, el consumo sube 5 hojas cada semana; con la propuesta, baja 4 cada semana. ¿Cuántas hojas de diferencia habrá entre ambos escenarios al cabo de 6 semanas?", "(80+5*6)-(80-4*6)", "Se calcula cada escenario y se resta.", " hojas"),
        arith("De 500 kg de residuos de ejemplo, el escenario optimista ahorra 30 % y el pesimista 10 %. ¿Cuántos kg separan a ambos escenarios?", "500*30//100-500*10//100", "Se calcula el ahorro de cada uno y se resta.", " kg"),
    ],
    ctx=arith("En un curso de ejemplo, 30 estudiantes ahorran 2 hojas al día, 5 días a la semana, durante 4 semanas. ¿Cuántas hojas se ahorran?", "30*2*5*4", "Se multiplican estudiantes, hojas, días y semanas.", " hojas"),
    sc=[
        ("En Tecnología: ¿qué es un escenario base?", "Lo que pasaría sin hacer ningún cambio", "Sirve para comparar el efecto de la propuesta."),
        ("¿Para qué se escriben los supuestos?", "Para que la proyección se pueda revisar", "Muestran bajo qué condiciones vale el cálculo."),
        ("¿Cómo se calcula una proyección simple?", "Valor actual ± cambio por período × períodos", "Es la fórmula de la clase."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Un curso usa hoy 100 hojas por semana. Escenario base: sube 2 hojas por semana. Escenario optimista: baja 8 hojas por semana. Escenario pesimista: baja 2 hojas por semana. Calcula las hojas por semana al cabo de 5 semanas en cada escenario, escribe dos supuestos, redacta una frase para comunicar el rango y di cómo comprobarías cuál ocurrió.",
        "Base: 110; optimista: 60; pesimista: 90; supuesto: el curso mantiene el mismo número de estudiantes; frase: en 5 semanas se usarían entre 60 y 90 hojas por semana con la propuesta; se mide cada semana",
        ["calcula los tres escenarios", "escribe dos supuestos", "comunica un rango", "propone cómo comprobar"],
        ["hoja con cálculos y frase"],
        ["presentar un solo número como certeza", "omitir el escenario base"],
        "Pregunta: «¿qué tendría que cambiar para que tu proyección ya no valga?». Eso son sus supuestos.",
    ),
    reinforce="Mide cuántas bolsas de basura se llenan en tu casa en una semana y proyecta cuántas serán en cuatro semanas si nada cambia.",
    extend="Explica por qué un buen informe muestra el escenario base y no solo el escenario con la propuesta.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja, lápiz, regla y los datos escritos en este cuaderno.",
    use="Aprenderé a elegir el gráfico adecuado para un dato, a escribir un título que diga la conclusión y a diseñar una diapositiva o infografía clara y honesta. Sirve para representar los datos de una propuesta sin engañar a la audiencia.",
    prior=["Sé calcular porcentajes.", "Sé leer una tabla de datos.", "Sé a quién va dirigido un mensaje."],
    explain=[
        "El gráfico se elige según lo que se quiere mostrar. Las barras comparan categorías, como el consumo de varios aparatos. La línea muestra cómo cambia un valor en el tiempo. El gráfico circular muestra las partes de un total y sirve con pocas partes, cuyos porcentajes suman 100 %. La tabla se usa cuando importan los valores exactos.",
        "Un gráfico claro tiene un título que dice la conclusión, ejes rotulados con unidades, la fuente de los datos y una nota que diga «datos de ejemplo» si lo son. En una diapositiva se pone una sola idea y, como regla práctica, no más de unas 40 palabras, con letra grande y buen contraste. En una infografía se ordenan las ideas en pasos y se usan iconos simples.",
        "Un gráfico también puede engañar. Si el eje de las barras no parte desde cero, una diferencia pequeña parece enorme. Con un eje que parte en 140, las barras de 150 y de 200 miden 10 y 60 unidades, y la segunda parece seis veces más larga cuando en realidad es poco más de una vez y un tercio. Honestidad significa dibujar las escalas sin exagerar.",
    ],
    vocab=[("gráfico de barras", "compara categorías"), ("gráfico de líneas", "muestra cambios en el tiempo"), ("gráfico circular", "muestra partes de un total"), ("eje", "línea del gráfico con escala y unidad"), ("título conclusión", "título que dice lo que el gráfico demuestra"), ("distorsión", "forma de dibujar que exagera o esconde una diferencia")],
    worked=[
        ("Elegir el gráfico", "Se quiere mostrar cómo cambió el consumo semana a semana durante 8 semanas. ¿Qué gráfico conviene?", ["Hay una variable que cambia en el tiempo.", "Eso lo muestra una línea."], "Gráfico de líneas"),
        ("Pasar a gráfico circular", "En un registro de ejemplo hay 120 residuos y 30 son botellas. ¿Qué porcentaje del círculo ocupa la parte de botellas?", ["Divido 30 entre 120.", "30 × 100 ÷ 120 = 25."], "25 %"),
    ],
    mistakes=[
        ("Poner como título «Gráfico 1».", "No dice qué muestra ni qué se debe concluir.", "Escribe un título con la conclusión: «Las hojas bajaron de 80 a 60»."),
        ("Cortar el eje para que la baja se vea más grande.", "Distorsiona los datos y engaña a la audiencia.", "Haz que el eje de las barras parta desde cero."),
    ],
    R=[
        ("Para comparar el consumo de cuatro aparatos conviene un gráfico de… A) barras B) líneas", "A", "Las barras comparan categorías."),
        ("Para mostrar cómo cambia el consumo semana a semana conviene un gráfico de… A) líneas B) circular", "A", "La línea muestra la evolución en el tiempo."),
        ("Para mostrar qué parte del total es cada tipo de residuo conviene un gráfico… A) circular B) de líneas", "A", "El gráfico circular muestra partes de un total."),
    ],
    C=[
        ("¿Cuál es un buen título? A) «Reducción de hojas por semana: de 80 a 60» B) «Gráfico 1»", "A", "Dice la conclusión y los datos clave."),
        ("Un eje parte en 78 y las barras de 80 y 82 parecen muy distintas. ¿Qué problema hay? A) exagera una diferencia pequeña B) ninguno, porque se ve claro", "A", "Un eje cortado distorsiona la comparación."),
        ("¿Para qué se anota la fuente o «datos de ejemplo»? A) para que la audiencia sepa de dónde vienen los datos y pueda revisarlos B) para llenar espacio", "A", "La fuente permite comprobar la información."),
    ],
    A=[
        arith("Residuos de ejemplo: papel 24 kg, plástico 36 kg y orgánicos 20 kg. ¿Qué porcentaje del total es plástico?", "36*100//(24+36+20)", "Se suma el total y se calcula la parte en porcentaje.", " %"),
        arith("Una diapositiva tiene 55 palabras y la regla práctica es máximo 40. ¿Cuántas palabras sobran?", "55-40", "Se resta el máximo recomendado.", " palabras"),
        arith("Registro de ejemplo de cuatro semanas: 80, 74, 68 y 60 hojas. ¿Qué porcentaje bajó entre la semana 1 y la 4?", "(80-60)*100//80", "Se calcula la diferencia sobre el valor inicial.", " %"),
    ],
    Z=[
        ("Un grupo usa un gráfico circular con 9 partes muy pequeñas. ¿Qué problema tiene?", "Es difícil de leer; conviene usar barras", "El círculo sirve con pocas partes."),
        ("Para persuadir, el equipo recorta el eje y la baja luce mayor. ¿Es aceptable?", "No: distorsiona los datos y rompe la honestidad", "La persuasión debe usar los datos como son."),
    ],
    D=[
        arith("Con un eje que parte en 140, las barras de 150 y 200 miden 10 y 60 unidades. ¿Cuántas veces más larga parece la barra de 200 que la de 150?", "60//10", "Se divide el largo de la barra grande entre el de la pequeña.", " veces"),
        arith("Una presentación de 8 minutos tiene 10 diapositivas de igual duración. ¿Cuántos segundos dura cada una?", "8*60//10", "Se pasan los minutos a segundos y se divide entre las diapositivas.", " segundos"),
    ],
    ctx=arith("En una encuesta de ejemplo, 27 de 36 personas entendieron mejor el gráfico de barras. ¿Qué porcentaje es?", "27*100//36", "Se divide entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("¿Qué gráfico muestra cambios en el tiempo?", "El de líneas", "La línea une los puntos de cada período."),
        ("¿Qué debe decir el título de un buen gráfico?", "La conclusión que se quiere mostrar", "Evita títulos vacíos como «Gráfico 1»."),
        ("¿Desde dónde debe partir el eje de las barras?", "Desde cero", "Así las longitudes son proporcionales."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Consumo de papel de un curso, en hojas por semana: semana 1, 90; semana 2, 84; semana 3, 78; semana 4, 72. Elige el gráfico adecuado y dibuja el borrador con título conclusión, ejes con unidades y nota de «datos de ejemplo». Calcula el porcentaje de baja entre la semana 1 y la 4. Después describe en cuatro líneas una diapositiva con una sola idea y como máximo 40 palabras.",
        "Gráfico de líneas con eje desde 0; título, el consumo bajó de 90 a 72 hojas en cuatro semanas; baja de 20 %; diapositiva, una idea con el gráfico y una frase corta",
        ["elige el gráfico correcto", "título con conclusión y ejes con unidades", "calcula bien el porcentaje", "la diapositiva tiene una idea y pocas palabras"],
        ["borrador del gráfico y descripción de la diapositiva"],
        ["eje cortado", "título vacío", "demasiado texto"],
        "Pregunta: «¿entendería tu gráfico alguien que no leyó el informe?». Si no, falta título o rótulos.",
    ),
    reinforce="Busca un gráfico en una noticia o libro y revisa si tiene título claro, unidades, fuente y un eje honesto.",
    extend="Explica cómo un eje cortado puede hacer que una diferencia pequeña parezca enorme.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. No se necesita conectarse a ningún servicio.",
    use="Aprenderé a aplicar normas de cuidado y de seguridad al comunicar: datos personales, consentimiento, fuentes, honestidad y cuidado ante contactos desconocidos. Sirve para publicar y compartir información sin dañar a nadie.",
    prior=["Sé que los datos personales se usan con consentimiento.", "Sé citar una fuente.", "Sé que debo avisar a una persona adulta de confianza cuando algo me incomoda."],
    explain=[
        "Antes de compartir un mensaje se revisan varias cosas. No se publican datos personales como la dirección, el horario de una persona, su teléfono o fotos de compañeros sin su consentimiento. Para publicar fuera del colegio se pide la revisión de una persona adulta responsable, como el docente. Se elige el canal según la audiencia: un canal interno para el curso y uno público solo si es necesario.",
        "También hay normas éticas. Las imágenes y los textos ajenos se citan y solo se usan si la licencia lo permite. Los datos se muestran como se midieron: cambiar una cifra para que se vea mejor es falsear. Las burlas y los mensajes que culpan a personas no corresponden. Antes de reenviar una cifra que llegó por mensaje se verifica su fuente, porque un dato errado se multiplica al compartirse.",
        "Si en un espacio compartido una persona desconocida pide datos o presiona para que hagas algo, no respondas, bloquea a esa persona, guarda una captura del mensaje (nunca de imágenes íntimas) y avisa a una persona adulta de confianza. No se confronta ni se guarda el secreto. Si te sientes mal por algo que viste en línea, también puedes hablar con una persona adulta de confianza; en Chile, el Fono Niños 147 atiende a niños, niñas y adolescentes.",
    ],
    vocab=[("dato personal", "información que identifica a una persona, como dirección o fotos"), ("consentimiento", "permiso claro de la persona"), ("canal", "medio por el que se comparte un mensaje"), ("licencia", "permiso que dice cómo puede usarse una obra"), ("verificar", "comprobar la fuente de un dato antes de compartirlo"), ("falsear", "cambiar un dato para que parezca mejor")],
    worked=[
        ("Revisar un afiche", "Un afiche trae el nombre completo de una estudiante con su foto, sin su permiso, y una imagen sin fuente. ¿Qué dos correcciones son necesarias?", ["Se pide consentimiento o se retiran nombre y foto.", "Se cita la fuente o se cambia la imagen."], "Consentimiento y cita de la fuente"),
        ("Corregir un dato", "El equipo midió 12 % de reducción, pero el afiche dice 40 %. ¿Qué se hace?", ["Se compara el afiche con el dato medido.", "Se corrige a 12 % y se explica el plan para mejorar."], "Se corrige al dato medido"),
    ],
    mistakes=[
        ("Publicar una foto «porque salió bien».", "Que salga bien no reemplaza el consentimiento de la persona.", "Pide permiso antes de publicar su imagen."),
        ("Reenviar una cifra porque otros ya la reenviaron.", "Los errores se multiplican al compartirse.", "Verifica la fuente antes de compartir."),
    ],
    R=[
        ("Antes de publicar la foto de un compañero, debes… A) pedir su consentimiento B) publicarla si sale bien", "A", "La imagen de una persona se usa con su permiso."),
        ("¿Cuál es un dato personal? A) la dirección de una casa B) el nombre del proyecto", "A", "Identifica o ubica a una persona."),
        ("Para publicar fuera del colegio, ¿quién revisa antes? A) una persona adulta responsable, como el docente B) nadie, para ir más rápido", "A", "La revisión previa evita errores y riesgos."),
    ],
    C=[
        ("Un afiche dice 40 % pero se midió 12 %. ¿Qué corresponde? A) corregirlo al dato medido B) dejarlo porque motiva", "A", "Falsear un dato rompe la honestidad."),
        ("Una publicación se burla de un compañero que no recicla. ¿Qué corresponde? A) cambiarla por un mensaje que explique sin culpar a personas B) dejarla si es un chiste", "A", "El mensaje debe respetar a las personas."),
        ("Llega por mensaje una cifra espectacular sin fuente. ¿Qué haces antes de compartirla? A) verificar de dónde viene B) reenviarla porque otros la reenviaron", "A", "Compartir sin verificar multiplica los errores."),
    ],
    A=[
        ("Revisa estas piezas: (1) gráfico con datos de ejemplo rotulados, (2) foto con nombre completo de un compañero sin permiso, (3) texto con la fuente citada, (4) mensaje con una burla. ¿Cuáles se pueden publicar tal como están?", "1 y 3", "Las piezas 2 y 4 incumplen normas de datos personales y de respeto."),
        arith("De 40 imágenes de un informe de ejemplo, 6 no tienen autor ni fuente. ¿Qué porcentaje es?", "6*100//40", "Se divide entre el total y se pasa a porcentaje.", " %"),
        ("En la plataforma del equipo, una persona desconocida pide la dirección y el horario de entrenamiento del grupo. ¿Qué haces? A) no respondes, la bloqueas, guardas la captura del mensaje y avisas a una persona adulta de confianza B) respondes sin dar datos, solo para averiguar quién es", "A", "No se da información ni se confronta; se bloquea y se pide ayuda adulta."),
    ],
    Z=[
        ("El equipo quiere subir la foto del curso a un perfil público para ganar seguidores, pero dos estudiantes dijeron que no. ¿Qué corresponde?", "No publicarla, o publicar una versión sin esas personas", "Sin consentimiento no se usa la imagen."),
        ("Un compañero propone poner 30 % en vez de 18 % porque nadie lo comprobará. ¿Qué respondes?", "Que no: falsear datos rompe la honestidad y engaña a quien decide", "Un dato falsificado daña la confianza."),
    ],
    D=[
        arith("Un mensaje de ejemplo llega a 6 personas y cada una lo comparte con 3 personas nuevas. ¿Cuántas personas lo habrán recibido en total?", "6+6*3", "Se suman las primeras con las que lo reciben después.", " personas"),
        arith("En un caso de ejemplo, 1 de cada 4 mensajes de ese tipo tiene una cifra errónea. Si se comparten 24 mensajes, ¿cuántos tendrían una cifra errónea?", "24//4", "Se divide el total entre 4.", " mensajes"),
    ],
    ctx=arith("El afiche dice 40 % y el dato medido es 12 %. ¿Cuántos puntos de porcentaje exagera?", "40-12", "Se resta el dato medido del dato publicado.", " puntos"),
    sc=[
        ("¿Qué se necesita antes de publicar la imagen de una persona?", "Su consentimiento", "Es un dato personal."),
        ("Una persona desconocida te pide datos. ¿Qué haces?", "No respondo, bloqueo, guardo la captura del mensaje y aviso a una persona adulta de confianza", "No se confronta ni se guarda el secreto."),
        ("¿Se puede cambiar una cifra para que la propuesta se vea mejor?", "No", "Falsear datos es poco ético."),
    ],
    open_task=(
        "Revisa este material de ejemplo antes de publicarlo: un afiche que dice «Redujimos 35 % las hojas» (el dato medido es 22 %), muestra la foto de dos compañeros, uno de ellos con su nombre completo y curso, usa un dibujo copiado de otro autor sin nombre y dice «Los que no reciclan son unos flojos». Escribe una lista de cuatro correcciones y quién debe revisar el afiche antes de publicarlo.",
        "Corregir a 22 %; pedir consentimiento o retirar la foto y el nombre completo; citar al autor del dibujo o cambiarlo; reemplazar la burla por un mensaje respetuoso; revisión del docente",
        ["identifica los cuatro problemas", "propone una corrección concreta para cada uno", "nombra a quién revisa antes de publicar", "mantiene el dato medido"],
        ["hoja con la lista de correcciones"],
        ["dejar pasar el dato falso", "no pedir revisión adulta"],
        "Pregunta: «¿qué dato personal podría ubicar a alguien?». Debe encontrar el nombre completo con el curso.",
    ),
    reinforce="Revisa un mensaje que hayas recibido con una cifra llamativa y anota qué fuente tendrías que comprobar antes de compartirlo.",
    extend="Explica por qué un dato falso se vuelve más dañino mientras más se comparte.",
)

# ------------------------------------------------------------------ OA 04, clase 5
reg(
    OA4, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los registros escritos en este cuaderno.",
    use="Aprenderé a evaluar una comunicación con una rúbrica, a dar y recibir retroalimentación útil, a comprobar con la audiencia si el mensaje se entendió y a mejorarlo. Sirve para que la propuesta llegue mejor la próxima vez.",
    prior=["Sé qué es una audiencia y un mensaje central.", "Sé calcular porcentajes.", "Sé qué es una rúbrica."],
    explain=[
        "Una rúbrica es una tabla con criterios y niveles de logro conocidos antes de evaluar. Para una comunicación se pueden usar cinco criterios: claridad, evidencia, adecuación a la audiencia, diseño y ética. Cada uno recibe un puntaje de 1 a 4. El total se compara con el máximo posible, que aquí es 5 × 4 = 20. La rúbrica permite ver qué criterio está más débil y mejorarlo primero.",
        "La retroalimentación útil es específica, observable y con una sugerencia: «la diapositiva 3 tiene 60 palabras; reduce a una idea y agrega el gráfico». Frases como «no me gustó» no dicen qué cambiar. Quien recibe retroalimentación la registra y decide qué mejorar, sin tomarla como un ataque.",
        "Para saber si la audiencia entendió se hacen dos o tres preguntas de comprensión al final y se cuenta qué porcentaje responde bien. Se prueba con un grupo pequeño antes de la presentación final. Al mejorar, conviene cambiar una cosa a la vez, para saber cuál cambio funcionó.",
    ],
    vocab=[("rúbrica", "tabla de criterios y niveles de logro"), ("retroalimentación", "comentario que dice qué está bien y qué mejorar"), ("pregunta de comprensión", "pregunta para comprobar si se entendió el mensaje"), ("prueba piloto", "ensayo con un grupo pequeño antes de la presentación final"), ("iteración", "ciclo de probar, mejorar y volver a probar"), ("nivel de logro", "puntaje que describe qué tan bien se cumple un criterio")],
    worked=[
        ("Puntaje de rúbrica", "Un equipo obtiene 4, 3, 3, 2 y 4 en los cinco criterios (máximo 4 cada uno). ¿Qué porcentaje del máximo logró?", ["Suma: 4 + 3 + 3 + 2 + 4 = 16.", "Máximo 20; 16 × 100 ÷ 20 = 80."], "80 %"),
        ("Retroalimentación útil", "Reescribe «tu afiche es feo» para que sirva.", ["Indico qué parte y qué se puede cambiar.", "«El afiche tiene 5 colores y el texto se pierde; usa 2 colores y letra más grande»."], "«El texto se pierde con 5 colores; usa 2 y letra más grande»"),
    ],
    mistakes=[
        ("Dar retroalimentación como «está mal».", "No dice qué, dónde ni cómo mejorar.", "Señala una parte concreta y agrega una sugerencia."),
        ("Cambiar varias cosas y creer que se sabe cuál funcionó.", "No se puede separar el efecto de cada cambio.", "Mejora una cosa por vez y vuelve a probar."),
    ],
    R=[
        ("¿Cuál es la mejor retroalimentación? A) «La diapositiva 3 tiene mucho texto; reduce a una idea y agrega el gráfico» B) «No me gustó»", "A", "Es específica y trae una sugerencia."),
        arith("Un equipo obtiene 9 puntos de un máximo de 12 en una rúbrica. ¿Qué porcentaje es?", "9*100//12", "Se divide el puntaje entre el máximo.", " %"),
        ("Para saber si la audiencia entendió, conviene… A) hacer dos preguntas de comprensión al final B) preguntar solo si se vio bonito", "A", "La comprensión se mide con preguntas sobre el contenido."),
    ],
    C=[
        ("Una rúbrica sirve para… A) evaluar con criterios conocidos de antemano B) decidir según el gusto del jurado", "A", "Los criterios previos hacen la evaluación justa."),
        ("Solo 3 de 20 personas recuerdan el mensaje central. ¿Qué se mejora primero? A) hacer el mensaje más claro y repetirlo B) agregar más datos", "A", "El problema está en lo central del mensaje."),
        ("La prueba piloto se hace… A) antes de la presentación final, para mejorarla B) después de terminar todo", "A", "Sirve para corregir a tiempo."),
    ],
    A=[
        arith("Rúbrica de 5 criterios (de 1 a 4): claridad 4, evidencia 3, audiencia 4, diseño 2 y ética 2. ¿Qué porcentaje del máximo logró?", "(4+3+4+2+2)*100//20", "Se suman los puntajes y se divide entre el máximo de 20.", " %"),
        arith("En un grupo de 30 personas, 21 contestan bien la pregunta de comprensión. ¿Qué porcentaje es?", "21*100//30", "Se divide entre el total y se pasa a porcentaje.", " %"),
        ("Puntajes de ejemplo: claridad 4, evidencia 2, audiencia 3, diseño 3 y ética 4. ¿Qué criterio conviene mejorar primero?", "Evidencia", "Es el que tiene el puntaje más bajo."),
    ],
    Z=[
        ("Alguien comenta: «Tu presentación está mal». ¿Por qué no sirve?", "No dice qué parte, por qué ni cómo mejorarla", "La retroalimentación debe ser específica."),
        ("El equipo mejora tres cosas a la vez y la comprensión sube de 40 % a 70 %. ¿Qué no sabe?", "Cuál de los tres cambios produjo la mejora", "Sin cambiar una cosa por vez no se puede atribuir el efecto."),
    ],
    D=[
        arith("De 20 personas, 8 comprendieron el mensaje en la primera prueba y 14 en la segunda. ¿Cuántos puntos de porcentaje subió la comprensión?", "(14*100//20)-(8*100//20)", "Se compara el porcentaje de cada prueba.", " puntos"),
        arith("La meta es que al menos el 80 % de 25 personas conteste bien. ¿Cuántas deben acertar como mínimo?", "25*80//100", "Se calcula el 80 % de 25.", " personas"),
    ],
    ctx=arith("Un equipo dispone de 90 minutos: el 60 % lo usa en ensayar y el resto en ajustar. ¿Cuántos minutos dedica a ajustar?", "90-90*60//100", "Se calcula el tiempo de ensayo y se resta del total.", " minutos"),
    sc=[
        ("En Tecnología: ¿qué es una rúbrica?", "Una tabla de criterios y niveles de logro", "Permite evaluar con criterios conocidos."),
        ("¿Qué debe tener una buena retroalimentación?", "Ser específica, observable y con sugerencia", "Así se sabe qué cambiar."),
        ("¿Cuántas cosas conviene cambiar a la vez al mejorar?", "Una", "Así se sabe cuál cambio funcionó."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Un equipo presentó su propuesta a 20 personas. Rúbrica (1 a 4): claridad 3, evidencia 4, audiencia 2, diseño 3, ética 4. En la pregunta «¿cuál era el mensaje central?» respondieron bien 9 de 20. Un comentario fue «hay mucho texto». Calcula el porcentaje de la rúbrica y el de comprensión, escribe dos comentarios de retroalimentación específicos y propone una sola mejora con la meta que esperas lograr en una segunda prueba.",
        "Rúbrica: 16 de 20, 80 %; comprensión: 45 %; criterio más débil, audiencia; mejora, reducir el texto y decir el mensaje central en una oración; meta, que al menos 16 de 20 contesten bien",
        ["calcula ambos porcentajes", "escribe dos comentarios específicos", "propone una sola mejora", "fija una meta medible"],
        ["hoja con cálculos y plan de mejora"],
        ["comentarios vagos", "cambiar varias cosas a la vez"],
        "Pregunta: «¿qué cambiarás primero y cómo lo vas a medir?». Debe nombrar una sola mejora y su indicador.",
    ),
    reinforce="Pide a una persona de tu casa que te cuente con sus palabras el mensaje central de tu última presentación y anota qué recordó.",
    extend="Explica por qué la prueba piloto es más útil que una opinión sobre si la presentación se vio bonita.",
)

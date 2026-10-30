"""Cuaderno del estudiante, 1.º básico Ciencias Naturales: OA 07 (hábitos de vida saludable) y OA 08 (materiales, propiedades y usos)."""
from __future__ import annotations

from student_content_cn_a import task
from student_lessons import arith, ex, register

OA7, OA8 = "CN01 OA 07", "CN01 OA 08"

# ---------------------------------------------------------------- OA 07
register(
    OA7, 1,
    materials="Este cuaderno con la rutina de un día de Tomás (horas y actividades), lápiz y colores.",
    use="Aprenderé qué son los hábitos saludables y cómo ayudan a mi cuerpo. Sirve para cuidarme todos los días y enfermarme menos.",
    prior=["Sé que mi cuerpo necesita agua, alimento y aire.", "Sé leer las horas en punto."],
    explain=[
        "Un hábito es algo que haces muchas veces, casi todos los días. Un hábito saludable es uno que cuida tu cuerpo, como lavarte las manos, comer frutas y verduras, hacer ejercicio y dormir lo suficiente.",
        "Cuando repites un hábito saludable, tu cuerpo se mantiene fuerte y se enferma menos. Por ejemplo, lavarte las manos con agua y jabón antes de comer saca los gérmenes que no se ven y que pueden enfermarte.",
        "Para saber si una rutina es saludable, revisa qué hábitos incluye. La rutina de Tomás tiene: 7:00 se levanta, 7:15 se lava los dientes, 8:00 desayuna, 16:00 juega a correr, 20:30 se lava los dientes y 21:00 se duerme. Cada hábito cuida una parte de su cuerpo.",
    ],
    vocab=[("hábito", "algo que haces muchas veces"), ("saludable", "que cuida tu cuerpo y te ayuda a estar sano"), ("rutina", "lo que haces cada día en orden"), ("gérmenes", "seres muy pequeños que pueden enfermarte"), ("enfermarse", "tener el cuerpo mal por un tiempo")],
    worked=[
        {"title": "Reconocer un hábito saludable", "problem": "Tomás se lava los dientes a las 7:15 y a las 20:30. ¿Cuántas veces al día? ¿Es un hábito saludable?", "steps": ["Se lava dos veces.", "Los dientes limpios no se enferman tan fácil.", "Es un hábito que cuida el cuerpo."], "answer": "Dos veces al día; es un hábito saludable"},
        {"title": "Contar horas de sueño", "problem": "Tomás se duerme a las 21:00 y se levanta a las 7:00. ¿Cuántas horas duerme?", "steps": ["De 21:00 a 24:00 son 3 horas.", "De 0:00 a 7:00 son 7 horas.", "3 + 7 = 10."], "answer": "Duerme 10 horas"},
    ],
    mistakes=[
        {"wrong": "Pensar que lavarse las manos solo sirve si se ven sucias.", "why": "Los gérmenes no se ven.", "fix": "Lávalas con agua y jabón antes de comer y después del baño, aunque se vean limpias."},
        {"wrong": "Creer que un hábito saludable se hace un solo día.", "why": "Se confunde con una acción única.", "fix": "Un hábito se repite casi todos los días."},
    ],
    tiers={
        "recovery": [
            ex("¿Lavarse las manos antes de comer es un hábito saludable?", "Sí", "Saca los gérmenes que enferman."),
            ex("¿Comer frutas y verduras es un hábito saludable?", "Sí", "Aportan lo que el cuerpo necesita."),
            ex("¿Dormir lo suficiente ayuda al cuerpo?", "Sí", "El cuerpo descansa y se recupera."),
        ],
        "understand": [
            ex("¿Qué es un hábito?", "Algo que haces muchas veces", "Se repite casi todos los días."),
            ex("¿Por qué lavarse las manos ayuda a no enfermarse?", "Porque saca los gérmenes", "Los gérmenes pueden enfermar."),
            ex("¿Qué es una rutina?", "Lo que haces cada día en orden", "Tiene una secuencia."),
        ],
        "apply": [
            arith("Tomás se lava los dientes 2 veces al día. ¿Cuántas veces se los lava en 7 días?", "2*7", "Se multiplican las veces al día por los 7 días.", " veces"),
            arith("Tomás se duerme a las 21:00 y se despierta a las 7:00. Duerme 3 horas hasta medianoche y luego 7 horas. ¿Cuántas horas duerme en total?", "3+7", "Se suman las dos partes de la noche.", " horas"),
            ex("En la rutina de Tomás, ¿qué hace a las 16:00?", "Juega a correr", "Es el dato de la rutina."),
        ],
        "reason": [
            ex("Ana dice que no necesita lavarse las manos si no tocó nada sucio. ¿Qué le respondes?", "Que los gérmenes no se ven, así que conviene lavarse igual", "No se puede saber si hay gérmenes."),
            ex("Beto come solo dulces todos los días. ¿Es un hábito saludable? Explica.", "No, porque el cuerpo necesita también frutas y verduras", "Un solo tipo de comida no alcanza."),
        ],
        "challenge": [
            ex("Escribe tres hábitos saludables que puedes hacer hoy.", "Por ejemplo lavarme las manos, comer una fruta y dormir temprano", "Son hábitos de la clase."),
            ex("Una rutina tiene 4 hábitos de aseo y 3 de comida. ¿Cuántos hábitos tiene?", "7", "Cuatro más tres son siete."),
        ],
    },
    context=[ex("En tu casa te lavas las manos 5 veces en el día. En otra casa se las lavan 3 veces. ¿Cuántas veces más te las lavas tú?", "2", "Cinco menos tres son dos.")],
    selfcheck=[ex("¿Qué cuida un hábito saludable?", "El cuerpo", "Ayuda a estar sano."), ex("¿Con qué te lavas las manos?", "Con agua y jabón", "Así salen los gérmenes."), ex("¿Los gérmenes se ven siempre?", "No", "Son muy pequeños.")],
    open_task=task("Mira esta rutina de Ema: 7:30 se levanta; 8:00 desayuna con leche y pan; 12:30 almuerza ensalada y pollo; 16:00 juega en la plaza una hora; 21:00 se acuesta sin lavarse los dientes. Marca con una estrella los hábitos saludables y escribe uno que falta.", "Saludables: desayuna, almuerza ensalada y juega en la plaza. Falta lavarse los dientes antes de dormir.", ["marca los hábitos saludables", "dice qué falta", "usa la rutina"], ["lista marcada", "una frase"], ["marcar el no lavarse los dientes como saludable", "no ver lo que falta"], "Reconoce los hábitos y pide explicar por qué falta el aseo."),
    reinforce="Escribe tu propia rutina de mañana con las horas.",
    extend="Explica por qué repetir un hábito es mejor que hacerlo solo un día.",
)

register(
    OA7, 2,
    materials="Este cuaderno con una tabla de actividad física, sueño y aseo, lápiz y colores. En casa: un reloj o un cronómetro.",
    use="Aprenderé cuánto movimiento, descanso y aseo ayudan a mi cuerpo. Sirve para armar un día con energía y salud.",
    prior=["Sé qué es un hábito saludable.", "Sé sumar y restar números pequeños."],
    explain=[
        "El cuerpo necesita moverse. Para niños y niñas se recomienda al menos 60 minutos de actividad física al día, como correr, saltar, bailar o jugar. Se puede hacer de a partes: por ejemplo 30 minutos en la mañana y 30 en la tarde.",
        "El cuerpo también necesita descanso. Una niña o un niño de tu edad necesita dormir entre 9 y 12 horas cada noche. Dormir bien ayuda a crecer, a aprender y a tener energía.",
        "El aseo es importante. Lávate las manos con agua y jabón durante 20 segundos, que es el tiempo de cantar dos veces el «cumpleaños feliz». Cepíllate los dientes dos veces al día, por unos 2 minutos cada vez.",
    ],
    vocab=[("actividad física", "moverse con el cuerpo, como correr o saltar"), ("descanso", "tiempo en que el cuerpo se recupera"), ("aseo", "limpieza del cuerpo"), ("minuto", "unidad de tiempo; 60 segundos"), ("recomendar", "decir qué es mejor hacer")],
    worked=[
        {"title": "Sumar minutos de movimiento", "problem": "Ema juega a la pelota 25 minutos en el recreo y baila 35 minutos en la tarde. ¿Llega a 60 minutos?", "steps": ["25 + 35 = 60.", "60 es igual a 60."], "answer": "Sí, llega justo a 60 minutos"},
        {"title": "Revisar el sueño", "problem": "Luis duerme 8 horas. Lo recomendado es de 9 a 12. ¿Duerme lo suficiente?", "steps": ["8 es menor que 9.", "Le falta al menos 1 hora."], "answer": "No, le falta al menos 1 hora"},
    ],
    mistakes=[
        {"wrong": "Creer que moverse solo cuenta si es una hora seguida.", "why": "Se piensa que debe ser todo junto.", "fix": "Se puede juntar en partes: 30 minutos y otros 30 minutos."},
        {"wrong": "Cepillarse los dientes solo una vez al día.", "why": "No se sabe que se recomienda dos veces.", "fix": "Cepíllate al despertar y antes de dormir."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos minutos de actividad física se recomiendan al día?", "60 minutos", "Es la recomendación de la clase."),
            ex("¿Cuántas veces al día debes cepillarte los dientes?", "Dos", "Una en la mañana y otra antes de dormir."),
            ex("¿Cuántos segundos debes lavarte las manos?", "20", "Es el tiempo recomendado."),
        ],
        "understand": [
            ex("¿Para qué sirve dormir bien?", "Para crecer, aprender y tener energía", "El cuerpo descansa."),
            ex("¿Qué es la actividad física?", "Moverse con el cuerpo, como correr o saltar", "Es mover el cuerpo con energía."),
            ex("¿Se pueden juntar los minutos de movimiento en el día?", "Sí", "Se puede hacer en partes."),
        ],
        "apply": [
            arith("Ema juega 25 minutos en el recreo y baila 35 minutos en la tarde. ¿Cuántos minutos se mueve?", "25+35", "Se suman los dos momentos.", " minutos"),
            arith("Un niño debe moverse 60 minutos y ya se movió 40. ¿Cuántos minutos le faltan?", "60-40", "Se resta lo hecho de lo recomendado.", " minutos"),
            arith("Pilar se lava las manos 4 veces al día, 20 segundos cada vez. ¿Cuántos segundos se lava en total?", "4*20", "Se multiplica las veces por los segundos.", " segundos"),
        ],
        "reason": [
            ex("Luis duerme 8 horas y está cansado en clases. ¿Qué dato puede explicarlo?", "Que duerme menos de las 9 horas recomendadas", "Le falta descanso."),
            ex("Camila se lavó las manos solo 5 segundos. ¿Por qué conviene lavarse más tiempo?", "Para sacar mejor los gérmenes", "20 segundos limpia mejor."),
        ],
        "challenge": [
            ex("Un día tienes 20 minutos de bicicleta, 15 de baile y 10 de saltar la cuerda. ¿Llegas a 60 minutos?", "No, son 45 minutos", "Veinte más quince más diez son cuarenta y cinco."),
            ex("Escribe una actividad física que puedas hacer en casa.", "Por ejemplo bailar o saltar", "Ambas mueven todo el cuerpo."),
        ],
    },
    context=[ex("Carlos duerme de las 21:00 a las 7:00. Eso son 10 horas. Su hermano se duerme a las 23:00 y se levanta a las 7:00, o sea 8 horas. ¿Cuántas horas más duerme Carlos?", "2", "Diez menos ocho son dos.")],
    selfcheck=[ex("¿Cuántas horas de sueño se recomiendan?", "Entre 9 y 12", "Es lo recomendado para tu edad."), ex("¿Cuántos segundos dura un buen lavado de manos?", "20", "Es el tiempo recomendado en esta clase."), ex("¿Cuántos minutos son una hora?", "60", "Una hora tiene 60 minutos.")],
    open_task=task("Arma tu día con esta tabla: mañana, recreo, tarde y noche. Completa cuántos minutos de movimiento hace Luis: mañana 10, recreo 20, tarde 25. Calcula cuántos faltan para 60 y escribe un juego que puede hacer. Escribe también a qué hora debería acostarse para dormir 10 horas si se levanta a las 7:00.", "Total 10 + 20 + 25 = 55 minutos; faltan 5 minutos. Puede saltar la cuerda 5 minutos. Para dormir 10 horas debería acostarse a las 21:00.", ["suma los minutos", "calcula lo que falta", "calcula la hora de acostarse"], ["cálculo escrito", "hora"], ["errores al sumar", "olvidar la hora"], "Reconoce el cálculo y pide verificar la hora de acostarse contando horas."),
    reinforce="Mide cuántos minutos juegas hoy sumando todos los momentos.",
    extend="Explica por qué dormir poco puede cambiar tu ánimo.",
)

register(
    OA7, 3,
    materials="Este cuaderno con una lista de ocho alimentos y dos columnas, lápiz y colores. En casa: frutas y verduras y un lavaplatos con agua limpia, con un adulto.",
    use="Aprenderé a elegir alimentos saludables y a lavarlos y lavarme las manos antes de comer. Sirve para evitar enfermedades del estómago.",
    prior=["Sé que el cuerpo necesita alimento.", "Sé qué es un hábito saludable."],
    explain=[
        "Una alimentación saludable incluye frutas, verduras, legumbres, pescado, pan, leche y mucha agua. En Chile se recomienda comer 5 porciones de frutas y verduras al día. Los dulces y bebidas azucaradas son para algunas veces, no todos los días.",
        "Antes de comer una fruta o una verdura, lávala con agua limpia. Así se sacan tierra y gérmenes. Después de lavarla, no la dejes en el suelo ni la toques con las manos sucias.",
        "Antes de comer, lávate las manos con agua y jabón. Después de ir al baño también. Un adulto puede ayudarte con el cuchillo y la cocina. Tú no uses cuchillos ni estufas solo.",
    ],
    vocab=[("alimentación saludable", "comer variado y con muchas frutas y verduras"), ("porción", "una parte de alimento, como una manzana"), ("legumbre", "alimento como lenteja o poroto"), ("lavar", "limpiar con agua"), ("de vez en cuando", "algunas veces, no todos los días")],
    worked=[
        {"title": "Elegir alimentos", "problem": "Lista: manzana, galletas con azúcar, zanahoria, jugo azucarado, lentejas, pan. ¿Cuáles son para todos los días?", "steps": ["Manzana, zanahoria, lentejas y pan.", "Las galletas con azúcar y el jugo azucarado son de vez en cuando."], "answer": "Manzana, zanahoria, lentejas y pan"},
        {"title": "Orden para comer una fruta", "problem": "Ordena: comer la fruta, lavarte las manos, lavar la fruta.", "steps": ["Primero te lavas las manos.", "Luego lavas la fruta.", "Al final la comes."], "answer": "Lavarte las manos, lavar la fruta y comerla"},
    ],
    mistakes=[
        {"wrong": "Pensar que si la fruta tiene cáscara no hay que lavarla.", "why": "La cáscara también tiene tierra y gérmenes que pasan a las manos.", "fix": "Lava la fruta antes de pelarla o comerla."},
        {"wrong": "Creer que la comida saludable es solo ensalada.", "why": "Se piensa en pocos alimentos.", "fix": "También son saludables legumbres, pescado, pan, leche y fruta."},
    ],
    tiers={
        "recovery": [
            ex("¿Es una manzana un alimento para todos los días?", "Sí", "Es una fruta."),
            ex("¿Son las lentejas una legumbre?", "Sí", "Las lentejas son legumbres."),
            ex("¿Cuándo te lavas las manos: antes de comer o después de jugar?", "Las dos veces", "Hay que lavarse antes de comer y después de jugar o ir al baño."),
        ],
        "understand": [
            ex("¿Cuántas porciones de frutas y verduras se recomiendan al día?", "5", "Es lo recomendado en Chile."),
            ex("¿Por qué se lavan las frutas y verduras?", "Para sacar la tierra y los gérmenes", "Los gérmenes pueden enfermar."),
            ex("¿Los dulces son para todos los días?", "No", "Son de vez en cuando."),
        ],
        "apply": [
            ex("Alimentos: palta, torta, tomate, bebida azucarada, pescado. ¿Cuántos son para todos los días?", "3", "Palta, tomate y pescado."),
            arith("Hoy comiste 2 frutas y 1 verdura en el almuerzo. Si comes 2 verduras más en la cena, ¿cuántas porciones comiste?", "2+1+2", "Se suman las porciones.", " porciones"),
            arith("Se recomiendan 5 porciones y llevas 3. ¿Cuántas faltan?", "5-3", "Se restan las que llevas.", " porciones"),
        ],
        "reason": [
            ex("Lila dice que no necesita lavar la manzana porque la va a pelar. ¿Qué le respondes?", "Que lave la fruta igual, porque la cáscara toca el cuchillo y las manos", "Los gérmenes pasan de la cáscara."),
            ex("Teo tomó un jugo azucarado en cada comida. ¿Qué bebida es mejor para todos los días?", "El agua", "El agua no tiene azúcar."),
        ],
        "challenge": [
            ex("Escribe un menú de almuerzo con tres alimentos saludables.", "Por ejemplo lentejas, ensalada y fruta", "Son alimentos de la clase."),
            ex("En una cesta hay 4 peras, 3 manzanas y 2 plátanos. ¿Cuántas frutas son?", "9", "Cuatro más tres más dos son nueve."),
        ],
    },
    context=[ex("En el colegio, la colación de Ema es una manzana, un pan y un jugo azucarado. ¿Qué cambiarías por algo más saludable?", "El jugo por agua", "El agua no tiene azúcar.")],
    selfcheck=[ex("¿Con qué se lavan las frutas?", "Con agua limpia", "Saca la tierra."), ex("¿Cuándo te lavas las manos?", "Antes de comer", "Para sacar gérmenes."), ex("¿Cuántas porciones de frutas y verduras al día?", "5", "Es la recomendación.")],
    open_task=task("Arma un menú de un día con esta lista: manzana, pan, lentejas, leche, pollo, galletas con azúcar, ensalada, jugo azucarado, agua, plátano. Elige para desayuno, almuerzo y cena y deja los dulces solo de vez en cuando. Escribe también los 3 pasos para comer una fruta con seguridad.", "Desayuno: pan, leche y plátano. Almuerzo: lentejas, ensalada y agua. Cena: pollo y manzana. Pasos: me lavo las manos, lavo la fruta, la como.", ["arma tres comidas", "deja los dulces para algunas veces", "ordena 3 pasos de higiene"], ["tabla de tres comidas", "tres pasos"], ["poner dulces todos los días", "olvidar lavarse las manos"], "Reconoce el menú y pide poner los pasos de higiene en orden."),
    reinforce="Con un adulto, lava una fruta bajo el chorro de agua y cómela.",
    extend="Explica por qué el agua es mejor para beber todos los días.",
)

register(
    OA7, 4,
    materials="Este cuaderno con una tabla semanal de hábitos (lunes a viernes) y cuatro hábitos para marcar, lápiz y colores.",
    use="Aprenderé a hacer un plan posible de hábitos saludables y a revisar si lo cumplo. Sirve para cuidar mi salud con acciones pequeñas.",
    prior=["Sé qué hábitos cuidan mi cuerpo.", "Sé contar hasta 20."],
    explain=[
        "Un plan de hábitos dice qué vas a hacer cada día. Es mejor elegir pocos hábitos y que sean posibles. Por ejemplo: lavarte los dientes en la mañana y en la noche, comer una fruta y moverte 30 minutos.",
        "Para revisar tu plan, usa una tabla semanal. Cada día marcas con una cruz el hábito que hiciste. Al final de la semana cuentas las cruces. Si hiciste 4 de 5 días, ¡lo hiciste muy bien!",
        "Si un día no lo hiciste, no pasa nada. Piensa por qué y busca una forma de recordarlo, como pegar un papel en el espejo. Lo importante es seguir intentándolo.",
    ],
    vocab=[("plan", "lista de lo que voy a hacer"), ("posible", "que se puede cumplir"), ("semana", "siete días"), ("cumplir", "hacer lo que dije que haría"), ("recordar", "no olvidar algo")],
    worked=[
        {"title": "Contar cruces", "problem": "Tabla de lavarse las manos antes de almorzar: lunes ✓, martes ✓, miércoles ✗, jueves ✓, viernes ✓. ¿Cuántos días lo cumplió?", "steps": ["Cuento las cruces marcadas: lunes, martes, jueves y viernes.", "Son 4 días."], "answer": "4 de 5 días"},
        {"title": "Mejorar el plan", "problem": "El miércoles no cumplió porque se olvidó. ¿Qué puede hacer?", "steps": ["Pensar la causa: se olvidó.", "Pegar un papel recordatorio cerca del baño."], "answer": "Poner un recordatorio, como un papel en el espejo"},
    ],
    mistakes=[
        {"wrong": "Ponerse diez hábitos nuevos de una vez.", "why": "Se piensa que mientras más, mejor.", "fix": "Empieza con dos o tres que puedas cumplir."},
        {"wrong": "Rendirse porque falló un día.", "why": "Se cree que un fallo arruina todo.", "fix": "Retoma al día siguiente y busca cómo recordarlo."},
    ],
    tiers={
        "recovery": [
            ex("Si marcas una cruz cada vez que cumples, ¿qué cuentas al final?", "Las cruces", "Muestran los días cumplidos."),
            ex("¿Una semana cuántos días tiene?", "Siete", "Lunes a domingo."),
            ex("¿Es posible cumplir un plan con dos hábitos?", "Sí", "Pocos hábitos se pueden cumplir."),
        ],
        "understand": [
            ex("¿Por qué conviene elegir pocos hábitos?", "Porque así se pueden cumplir", "Muchos son difíciles."),
            ex("¿Qué haces si un día no cumpliste?", "Busco cómo recordarlo y sigo", "Se retoma al día siguiente."),
            ex("¿Para qué sirve la tabla semanal?", "Para revisar cuántos días cumplí", "Muestra el avance."),
        ],
        "apply": [
            arith("En una semana cumpliste el hábito 4 días de 5. ¿Cuántos días no lo cumpliste?", "5-4", "Se resta lo cumplido del total.", " día"),
            arith("Lavaste tus dientes 2 veces al día durante 5 días. ¿Cuántas veces fueron?", "2*5", "Se multiplica por los días.", " veces"),
            ex("Tabla: lunes ✓, martes ✓, miércoles ✓, jueves ✗, viernes ✓. ¿Cuántos ✓ hay?", "4", "Cuento las cruces marcadas."),
        ],
        "reason": [
            ex("Sara cumplió 1 día de 5. Dice «no sirve». ¿Qué le propones?", "Elegir un hábito más fácil y poner un recordatorio", "Se puede mejorar con ayuda."),
            ex("¿Por qué es mejor un plan de 3 hábitos que uno de 10?", "Porque es más fácil de cumplir", "Poco se cumple mejor."),
        ],
        "challenge": [
            ex("Escribe un plan de dos hábitos para tu semana.", "Por ejemplo lavarme los dientes en la noche y comer una fruta", "Son hábitos pocos y posibles."),
            ex("Cumpliste 3 días un hábito y 4 días otro. ¿Cuántas veces cumpliste en total?", "7", "Tres más cuatro son siete."),
        ],
    },
    context=[ex("Camila marcó estas cruces en una semana: lavar manos 5, comer fruta 4, mover el cuerpo 3. ¿Cuántas cruces marcó en total?", "12", "Cinco más cuatro más tres son doce.")],
    selfcheck=[ex("¿Cuántos hábitos conviene elegir al comienzo?", "Pocos", "Se cumplen mejor."), ex("¿Qué haces si un día falló el plan?", "Lo retomo al día siguiente", "No se abandona."), ex("¿Qué marcas cuando cumples?", "Una cruz", "Se cuenta al final.")],
    open_task=task("Completa este plan: elige dos hábitos de esta lista (lavarse los dientes de noche, comer una fruta, moverse 30 minutos, tomar agua en la mañana). Dibuja una tabla de lunes a viernes, marca estas cruces de ejemplo y escribe cuántos días lo cumplió: lavar dientes lunes, martes, miércoles y viernes; fruta lunes, jueves y viernes.", "Lavar dientes: 4 días de 5. Comer fruta: 3 días de 5. Para mejorar: pegar un papel en el espejo.", ["elige dos hábitos", "cuenta las cruces", "propone una mejora"], ["tabla semanal", "frase"], ["contar mal", "no proponer mejora"], "Reconoce el plan y pide verificar el conteo de cruces."),
    reinforce="Haz una tabla de una semana para un hábito y márcala cada día.",
    extend="Explica cómo ayudar a un amigo a cumplir su hábito.",
)

# ---------------------------------------------------------------- OA 08
register(
    OA8, 1,
    materials="Este cuaderno con una tabla de objetos y los materiales de que están hechos, lápiz y colores. En casa: una cuchara, un vaso, una botella y un cuaderno para mirar y tocar.",
    use="Aprenderé a diferenciar un objeto del material del que está hecho. Sirve para entender por qué usamos cada cosa de cierta manera.",
    prior=["Sé nombrar objetos de la casa.", "Sé describir si algo es duro o blando."],
    explain=[
        "Un objeto es una cosa que puedes tocar y usar, como una cuchara, una botella o una silla. Un material es de lo que está hecho un objeto, como madera, metal, vidrio, plástico, tela, papel o goma.",
        "Un mismo objeto puede estar hecho de materiales distintos. Una cuchara puede ser de metal, de madera o de plástico. Y un mismo material sirve para muchos objetos: el vidrio sirve para vasos, ventanas y botellas.",
        "Para saber el material, mira y toca con cuidado: ¿es frío o tibio?, ¿es duro o blando?, ¿se ve a través de él? Con esos datos puedes decir de qué está hecho.",
    ],
    vocab=[("objeto", "cosa que se puede tocar y usar"), ("material", "aquello de lo que está hecho un objeto"), ("madera", "material que viene de los árboles"), ("vidrio", "material duro que deja pasar la luz"), ("metal", "material duro y frío, como el hierro")],
    worked=[
        {"title": "Objeto y material", "problem": "Un vaso de vidrio. ¿Cuál es el objeto y cuál el material?", "steps": ["El objeto es el vaso, lo que uso para tomar.", "El material es el vidrio, de lo que está hecho."], "answer": "Objeto: vaso. Material: vidrio"},
        {"title": "Un objeto, varios materiales", "problem": "Una cuchara puede ser de metal, madera o plástico. ¿Es el mismo objeto?", "steps": ["En los tres casos se usa para comer.", "Cambia el material."], "answer": "Es el mismo objeto con tres materiales distintos"},
    ],
    mistakes=[
        {"wrong": "Decir que la silla es el material.", "why": "Se confunde la cosa con de qué está hecha.", "fix": "La silla es el objeto; la madera puede ser el material."},
        {"wrong": "Pensar que todos los objetos de una misma forma son del mismo material.", "why": "Se mira solo la forma.", "fix": "Toca y mira: puede ser distinto material."},
    ],
    tiers={
        "recovery": [
            ex("Una botella de vidrio. ¿Cuál es el material?", "Vidrio", "Es de lo que está hecha."),
            ex("Un lápiz de madera. ¿Cuál es el objeto?", "El lápiz", "Es lo que uso para escribir."),
            ex("Una pelota de goma. ¿Cuál es el material?", "Goma", "Es lo que la forma."),
        ],
        "understand": [
            ex("¿Qué es un material?", "De lo que está hecho un objeto", "El objeto se hace con él."),
            ex("¿Qué es un objeto?", "Una cosa que se puede tocar y usar", "Por ejemplo una silla."),
            ex("¿Un mismo objeto puede ser de materiales distintos?", "Sí", "Por ejemplo una cuchara."),
        ],
        "apply": [
            ex("Tabla: tijera, polera, ventana, mesa. Materiales: tela, madera, metal y plástico, vidrio. ¿De qué material es la polera?", "Tela", "La polera se hace con tela."),
            ex("Objeto: ventana. ¿Qué material de la lista deja pasar la luz: madera o vidrio?", "Vidrio", "El vidrio es transparente."),
            arith("En la mesa hay 3 objetos de madera, 2 de metal y 4 de plástico. ¿Cuántos objetos hay?", "3+2+4", "Se suman los objetos de cada material.", " objetos"),
        ],
        "reason": [
            ex("Dani dice que el vaso y el material de vidrio son lo mismo. ¿Qué le explicas?", "Que el vaso es el objeto y el vidrio es el material", "Uno es la cosa y el otro de qué está hecha."),
            ex("Si una cuchara de metal y una de plástico sirven para comer, ¿qué cambia entre ellas?", "El material", "Se usan igual pero están hechas de cosas distintas."),
        ],
        "challenge": [
            ex("Escribe un objeto de tu casa y su material.", "Por ejemplo la mesa y la madera", "Une objeto con material."),
            ex("Una caja tiene 5 objetos de vidrio y 3 de plástico. ¿Cuántos objetos de vidrio más que de plástico hay?", "2", "Cinco menos tres son dos."),
        ],
    },
    context=[ex("En la cocina hay una olla de metal, un plato de loza, un vaso de vidrio y una cuchara de madera. ¿Cuántos objetos hay y cuántos materiales distintos?", "4 objetos y 4 materiales", "Cada objeto es de un material distinto.")],
    selfcheck=[ex("¿La silla es un objeto o un material?", "Un objeto", "Es una cosa que uso."), ex("¿La madera es un objeto o un material?", "Un material", "Se usa para hacer objetos."), ex("¿De qué material es un vaso de vidrio?", "Vidrio", "Es lo que lo forma.")],
    open_task=task("Mira esta lista de seis objetos: tijera (metal y plástico), mesa (madera), ventana (vidrio), polera (tela), pelota (goma), cuaderno (papel). Haz una tabla con objeto y material y dibuja un objeto con dos materiales.", "Tabla: tijera-metal y plástico, mesa-madera, ventana-vidrio, polera-tela, pelota-goma, cuaderno-papel. Dibujo: la tijera con metal y plástico.", ["une cada objeto con su material", "dibuja un objeto con dos materiales", "usa una tabla"], ["tabla", "dibujo"], ["confundir objeto y material", "olvidar un objeto"], "Reconoce la diferencia y pide revisar los dos materiales de la tijera."),
    reinforce="Mira cinco objetos de tu cocina y escribe de qué material están hechos.",
    extend="Explica por qué la madera sirve para hacer muchos objetos distintos.",
)

register(
    OA8, 2,
    materials="Este cuaderno con los datos de un experimento de gotas (datos de ejemplo) y una lista de propiedades, lápiz y colores. En casa: gotas de agua con una cuchara y tres objetos: bolsa plástica, papel y tela.",
    use="Aprenderé a describir propiedades de los materiales: flexible, rígido, impermeable, transparente, áspero y liso. Sirve para elegir el material adecuado para cada cosa.",
    prior=["Sé la diferencia entre objeto y material.", "Sé comparar con las palabras duro y blando."],
    explain=[
        "Una propiedad es algo que puedes observar de un material. Un material es flexible si se dobla sin quebrarse, como la goma. Es rígido si no se dobla, como la madera dura. Es transparente si se ve a través de él, como el vidrio.",
        "Un material es impermeable si no deja pasar el agua, como el plástico de las botas de lluvia. Es permeable si deja pasar el agua, como la tela o el papel. También puede ser liso o áspero, según cómo se sienta.",
        "Un experimento de gotas sirve para ver si un material es impermeable. En el ejemplo, se pone una gota de agua sobre cada material y se mira durante 30 segundos. Plástico: la gota sigue entera. Papel: la gota se absorbe en 5 segundos. Tela: se absorbe en 10 segundos.",
    ],
    vocab=[("propiedad", "algo que se puede observar de un material"), ("flexible", "se dobla sin quebrarse"), ("rígido", "no se dobla"), ("impermeable", "no deja pasar el agua"), ("transparente", "se ve a través de él")],
    worked=[
        {"title": "Leer el experimento de gotas", "problem": "Gota sobre plástico: sigue entera a los 30 s. Sobre papel: se absorbe en 5 s. Sobre tela: se absorbe en 10 s. ¿Cuál es impermeable?", "steps": ["El plástico no absorbió la gota.", "El papel y la tela sí."], "answer": "El plástico es impermeable"},
        {"title": "Elegir la propiedad", "problem": "Una regla de madera no se dobla. ¿Es flexible o rígida?", "steps": ["No se dobla.", "Un material que no se dobla es rígido."], "answer": "Es rígida"},
    ],
    mistakes=[
        {"wrong": "Decir que todo lo suave es flexible.", "why": "Se confunde suave con flexible.", "fix": "Flexible es lo que se dobla; prueba doblarlo."},
        {"wrong": "Decir que un material es impermeable sin hacer la prueba.", "why": "Se supone por la apariencia.", "fix": "Pon una gota de agua y mira qué pasa."},
    ],
    tiers={
        "recovery": [
            ex("¿El vidrio es transparente u opaco?", "Transparente", "Se ve a través de él."),
            ex("¿La goma se dobla? ¿Es flexible o rígida?", "Flexible", "Se dobla sin quebrarse."),
            ex("¿Una regla de madera dura es flexible o rígida?", "Rígida", "No se dobla."),
        ],
        "understand": [
            ex("¿Qué significa impermeable?", "Que no deja pasar el agua", "El agua se queda afuera."),
            ex("¿Qué es una propiedad de un material?", "Algo que se puede observar de él", "Por ejemplo flexible o liso."),
            ex("¿Cómo se comprueba si un material es impermeable?", "Con una gota de agua", "Se mira si la absorbe."),
        ],
        "apply": [
            arith("El papel absorbió la gota en 5 segundos y la tela en 10 segundos. ¿Cuántos segundos más tardó la tela?", "10-5", "Se resta el tiempo del papel al de la tela.", " segundos"),
            ex("Resultados: plástico gota entera, papel 5 s, tela 10 s, esponja 2 s. ¿Cuál absorbe más rápido?", "La esponja", "Tardó solo 2 s."),
            ex("Una bolsa de plástico no deja pasar el agua. ¿Es permeable o impermeable?", "Impermeable", "El agua no pasa."),
        ],
        "reason": [
            ex("Carla dice que el papel es impermeable porque se ve seco. ¿Qué dato del experimento la contradice?", "Que absorbió la gota en 5 segundos", "Un material impermeable no absorbe."),
            ex("Una botella de plástico se dobla un poco al apretarla. ¿Es flexible o rígida?", "Flexible", "Se dobla sin quebrarse."),
        ],
        "challenge": [
            ex("Escribe un material flexible y uno rígido.", "Por ejemplo goma y madera", "Uno se dobla y el otro no."),
            ex("Tres materiales son transparentes y dos opacos. ¿Cuántos son?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("Un niño prueba tres chaquetas bajo una gota de agua: una la absorbe en 8 segundos, otra en 20 segundos y otra no la absorbe. ¿Cuál elegirías para la lluvia?", "La que no absorbe la gota", "Es la impermeable.")],
    selfcheck=[ex("¿Qué es flexible?", "Algo que se dobla sin quebrarse", "Como la goma."), ex("¿Qué material deja ver a través?", "El transparente", "Como el vidrio."), ex("¿Cómo se llama el material que no deja pasar agua?", "Impermeable", "El agua se queda afuera.")],
    open_task=task("Lee estos resultados de una gota de agua: aluminio, la gota sigue entera; servilleta de papel, se absorbe en 3 segundos; calcetín de algodón, se absorbe en 12 segundos; hoja de plástico, la gota sigue entera. Escribe cuáles son impermeables, cuál absorbe más rápido y qué conclusión sacas.", "Impermeables: aluminio y plástico. La servilleta absorbe más rápido (3 s). Conclusión: el metal y el plástico no dejan pasar el agua; el papel y la tela sí.", ["nombra los impermeables", "nombra el más rápido", "escribe una conclusión con datos"], ["frases con números", "tabla"], ["decir que el algodón es impermeable", "no usar los segundos"], "Reconoce los resultados y pide citar los segundos en la conclusión."),
    reinforce="Con una gota, prueba un papel y una bolsa plástica y mira la diferencia.",
    extend="Explica por qué las ventanas son de vidrio y no de madera.",
)

register(
    OA8, 3,
    materials="Este cuaderno con una tabla de ocho objetos con sus propiedades, lápiz y colores.",
    use="Aprenderé a clasificar materiales por una propiedad. Sirve para ordenar cosas y para elegir la adecuada.",
    prior=["Sé las propiedades flexible, rígido, transparente e impermeable.", "Sé clasificar con un criterio."],
    explain=[
        "Clasificar materiales es ponerlos en grupos según una propiedad. Si el criterio es «flexible o rígido», pones la goma y la tela con los flexibles, y la madera y el vidrio con los rígidos.",
        "Si cambias la propiedad, cambian los grupos. Con «transparente u opaco», el vidrio va en transparente, y la madera, el metal y la tela van en opaco. Un material puede estar en grupos distintos según el criterio.",
        "La tabla de hoy tiene ocho objetos. Tijera (metal, rígida, opaca). Vaso (vidrio, rígido, transparente). Pelota (goma, flexible, opaca). Bolsa (plástico, flexible, transparente). Mesa (madera, rígida, opaca). Calcetín (tela, flexible, opaca). Botella (plástico, flexible, transparente). Regla (plástico, rígida, transparente).",
    ],
    vocab=[("clasificar", "poner en grupos con una regla"), ("opaco", "no se ve a través de él"), ("propiedad", "algo que se observa de un material"), ("criterio", "regla para formar los grupos"), ("grupo", "conjunto de objetos con la misma propiedad")],
    worked=[
        {"title": "Clasificar por flexible o rígido", "problem": "Con la tabla: tijera rígida, vaso rígido, pelota flexible, bolsa flexible, mesa rígida, calcetín flexible, botella flexible, regla rígida. Clasifica.", "steps": ["Rígidos: tijera, vaso, mesa, regla (4).", "Flexibles: pelota, bolsa, calcetín, botella (4)."], "answer": "4 rígidos y 4 flexibles"},
        {"title": "Cambiar el criterio", "problem": "Con transparente u opaco: ¿cuántos objetos transparentes hay?", "steps": ["Transparentes: vaso, bolsa, botella, regla.", "Son 4."], "answer": "4 transparentes"},
    ],
    mistakes=[
        {"wrong": "Mezclar dos propiedades en un grupo.", "why": "Se usan dos criterios a la vez.", "fix": "Usa una propiedad por clasificación."},
        {"wrong": "Clasificar por el objeto y no por el material.", "why": "Se mira la cosa y no de qué está hecha.", "fix": "Pregúntate: ¿de qué material es y cómo es?"},
    ],
    tiers={
        "recovery": [
            ex("Tabla: la pelota es flexible. ¿A qué grupo va: flexible o rígido?", "Flexible", "La pelota se dobla sin quebrarse."),
            ex("Tabla: el vaso es transparente. ¿A qué grupo va: transparente u opaco?", "Transparente", "Se ve a través."),
            ex("Tabla: la mesa es rígida. ¿A qué grupo va: flexible o rígido?", "Rígido", "No se dobla."),
        ],
        "understand": [
            ex("¿Qué es un criterio de clasificación?", "Una regla para formar grupos", "Es una propiedad."),
            ex("¿Puede un mismo material estar en dos clasificaciones distintas?", "Sí, con otra propiedad", "Cambia el criterio."),
            ex("¿Qué significa opaco?", "Que no se ve a través de él", "Es lo contrario de transparente."),
        ],
        "apply": [
            ex("Con la tabla de hoy, ¿cuántos objetos son opacos: tijera, pelota, mesa y calcetín?", "4", "Los cuatro son opacos."),
            arith("Hay 4 objetos rígidos y 4 flexibles. ¿Cuántos objetos son en total?", "4+4", "Se suman los dos grupos.", " objetos"),
            ex("Clasifica botella y regla por rígido o flexible. ¿Cuál es flexible?", "La botella", "Se dobla; la regla no."),
        ],
        "reason": [
            ex("Pía puso la botella en flexibles y transparentes en el mismo grupo. ¿Qué error cometió?", "Usó dos criterios a la vez", "Debe usar solo uno."),
            ex("Si la bolsa y la regla son de plástico, ¿por qué una es flexible y la otra rígida?", "Porque el plástico puede ser de distinto tipo y grosor", "Las propiedades cambian aunque el material se llame igual."),
        ],
        "challenge": [
            ex("Inventa un criterio para clasificar la tijera, el vaso y la mesa.", "Por ejemplo rígidos", "Los tres son rígidos."),
            ex("En una caja hay 3 objetos transparentes y 4 opacos. ¿Cuántos objetos hay?", "7", "Tres más cuatro son siete."),
        ],
    },
    context=[ex("En el taller hay 2 cajas con 5 objetos flexibles cada una. ¿Cuántos objetos flexibles hay?", "10", "Dos cajas por cinco objetos son diez.")],
    selfcheck=[ex("¿Cuántos criterios usas a la vez?", "Uno", "Un criterio por clasificación."), ex("¿El vidrio es transparente?", "Sí", "Se ve a través."), ex("¿La madera es opaca?", "Sí", "No se ve a través.")],
    open_task=task("Clasifica estos cinco objetos por transparente u opaco y luego por flexible o rígido: vaso (rígido, transparente), calcetín (flexible, opaco), regla de plástico (rígida, transparente), globo (flexible, transparente), mesa (rígida, opaca). Escribe los grupos y cuántos hay en cada uno.", "Transparentes: vaso, regla, globo (3). Opacos: calcetín, mesa (2). Rígidos: vaso, regla, mesa (3). Flexibles: calcetín, globo (2).", ["hace dos clasificaciones", "cuenta cada grupo", "usa un criterio por vez"], ["dos tablas", "totales"], ["mezclar criterios", "olvidar un objeto"], "Reconoce que usa un criterio por clasificación y pide verificar los totales."),
    reinforce="Clasifica cuatro objetos de tu mochila por rígido o flexible.",
    extend="Haz una tercera clasificación con otra propiedad y compárala.",
)

register(
    OA8, 4,
    materials="Este cuaderno con cinco necesidades (paraguas, ventana, bota de lluvia, cuerda de saltar y tapa de olla) y una tabla de materiales con propiedades, lápiz y colores.",
    use="Aprenderé a elegir el material adecuado según para qué se va a usar. Sirve para decidir con razones qué material usar.",
    prior=["Sé las propiedades de los materiales.", "Sé clasificar materiales."],
    explain=[
        "Para elegir un material, primero piensa para qué lo vas a usar y qué propiedad necesitas. Un paraguas necesita ser impermeable. Una ventana necesita ser transparente. Una cuerda de saltar necesita ser flexible.",
        "Luego mira la tabla de materiales: tela de algodón (flexible, permeable), plástico fino (flexible, impermeable), vidrio (rígido, transparente), madera (rígida, opaca), goma (flexible, impermeable), metal (rígido, opaco).",
        "Explica tu elección con una razón: «Elijo plástico fino para el paraguas porque es impermeable». Una buena razón nombra la propiedad. Si dos materiales sirven, elige el que sea más seguro y más barato.",
    ],
    vocab=[("elegir", "decidir cuál es mejor"), ("necesitar", "hacer falta para un uso"), ("uso", "para qué sirve un objeto"), ("razón", "explicación de mi decisión"), ("adecuado", "que sirve bien para algo")],
    worked=[
        {"title": "Elegir para un paraguas", "problem": "Un paraguas necesita ser impermeable y flexible. ¿Qué material eliges: algodón o plástico fino?", "steps": ["Algodón es permeable.", "Plástico fino es impermeable y flexible."], "answer": "Plástico fino, porque es impermeable y flexible"},
        {"title": "Elegir para una ventana", "problem": "Una ventana necesita ser transparente. ¿Qué eliges: madera o vidrio?", "steps": ["La madera es opaca.", "El vidrio es transparente."], "answer": "Vidrio, porque es transparente"},
    ],
    mistakes=[
        {"wrong": "Elegir un material porque tiene un color lindo.", "why": "No se mira la propiedad que se necesita.", "fix": "Piensa primero qué propiedad necesita el objeto."},
        {"wrong": "Elegir un material sin dar una razón.", "why": "Se decide sin explicar.", "fix": "Escribe «elijo… porque es…» con la propiedad."},
    ],
    tiers={
        "recovery": [
            ex("Un paraguas necesita ser impermeable. ¿Sirve un material permeable?", "No", "Dejaría pasar la lluvia."),
            ex("Una ventana necesita ser transparente. ¿Sirve el vidrio?", "Sí", "El vidrio es transparente."),
            ex("Una cuerda de saltar necesita doblarse. ¿Debe ser flexible o rígida?", "Flexible", "Tiene que doblarse al saltar."),
        ],
        "understand": [
            ex("¿Qué se hace primero para elegir un material?", "Pensar qué propiedad necesita el objeto", "Eso guía la decisión."),
            ex("¿Qué debe tener una buena razón?", "La propiedad del material", "Explica por qué sirve."),
            ex("Si dos materiales sirven, ¿qué más se puede mirar?", "Que sea más seguro y más barato", "Ayuda a decidir."),
        ],
        "apply": [
            ex("Una bota de lluvia necesita ser impermeable. ¿Eliges goma o algodón?", "Goma", "La goma es impermeable."),
            ex("Una tapa de olla se toma con la mano y no debe quemar. ¿Elegirías metal puro o metal con mango de madera?", "Metal con mango de madera", "La madera no se calienta tan rápido."),
            arith("Un paraguas tiene 8 varillas de metal y 1 tela de plástico. ¿Cuántas partes tiene?", "8+1", "Se suman las varillas y la tela.", " partes"),
        ],
        "reason": [
            ex("Beto quiere hacer la bolsa de la compra con papel. ¿Qué pasa con la lluvia y por qué?", "Se moja y se rompe, porque el papel es permeable", "El papel absorbe el agua."),
            ex("Marta eligió una tela de algodón para un impermeable. ¿Qué le dices?", "Que no sirve porque es permeable", "Dejaría pasar el agua."),
        ],
        "challenge": [
            ex("Escribe un material para una ventana de invernadero y su razón.", "Por ejemplo plástico transparente, porque deja pasar la luz", "Necesita dejar pasar la luz."),
            ex("Una tienda vende 3 paraguas de plástico y 2 de tela. ¿Cuántos paraguas vende?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("Para proteger una planta de la lluvia, Sofía debe elegir entre una tapa de plástico transparente y una de cartón. ¿Cuál deja pasar la luz y protege del agua?", "La de plástico transparente", "Es transparente e impermeable.")],
    selfcheck=[ex("¿Qué propiedad necesita un paraguas?", "Impermeable", "No deja pasar el agua."), ex("¿Qué propiedad necesita una ventana?", "Transparente", "Deja ver y pasar la luz."), ex("¿Qué debe tener una razón?", "Una propiedad", "Explica la elección.")],
    open_task=task("Elige un material para cada necesidad con una razón, usando la tabla de la clase. A) un paraguas, B) una ventana, C) una cuerda de saltar, D) la mesa de la cocina. Escribe: «Elijo… porque es…».", "A: Elijo plástico fino porque es impermeable. B: Elijo vidrio porque es transparente. C: Elijo goma porque es flexible. D: Elijo madera porque es rígida.", ["elige un material por necesidad", "da una razón con propiedad", "usa la tabla"], ["cuatro frases", "dibujo de un objeto"], ["elegir por el color", "no dar razón"], "Reconoce la razón y pide nombrar la propiedad en cada una."),
    reinforce="Elige un material para una caja de zapatos y di por qué.",
    extend="Explica por qué las botas de lluvia no se hacen de tela de algodón.",
)

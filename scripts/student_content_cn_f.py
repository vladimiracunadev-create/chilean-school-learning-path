"""Cuaderno del estudiante, 1.º básico Ciencias Naturales: OA 11 (ciclo diario, día y noche) y OA 12 (estaciones del año)."""
from __future__ import annotations

from student_content_cn_a import task
from student_lessons import arith, ex, register

OA11, OA12 = "CN01 OA 11", "CN01 OA 12"

# ---------------------------------------------------------------- OA 11
register(
    OA11, 1,
    materials="Este cuaderno con un registro del cielo en cuatro momentos del día (datos de ejemplo), lápiz y colores. En casa: una ventana desde donde ver el cielo. Nunca mires directo al Sol.",
    use="Aprenderé a observar el cielo en distintos momentos del día y a registrar lo que veo. Sirve para describir el día y la noche con datos.",
    prior=["Sé las horas en punto.", "Sé que el Sol da luz y calor."],
    explain=[
        "En el día vemos el Sol en el cielo y hay mucha luz. En la noche no vemos el Sol; vemos la Luna y las estrellas, y hay poca luz. Entre el día y la noche el cielo cambia poco a poco: amanece y atardece.",
        "Para registrar el cielo, anota la hora, qué ves y cuánta luz hay. Registro de ejemplo: a las 8:00 se ve el Sol bajo y hay luz suave; a las 13:00 el Sol está alto y hay mucha luz; a las 19:00 el Sol está bajo y la luz es naranja; a las 22:00 se ven la Luna y estrellas y hay poca luz.",
        "Seguridad: nunca mires directo al Sol, porque daña los ojos. Para saber dónde está, mira la sombra que hace un objeto o la luz en el suelo.",
    ],
    vocab=[("día", "parte del tiempo en que hay luz del Sol"), ("noche", "parte del tiempo con poca luz, sin Sol"), ("amanecer", "momento en que sale el Sol"), ("atardecer", "momento en que el Sol se va escondiendo"), ("luminosidad", "cuánta luz hay")],
    worked=[
        {"title": "Leer el registro", "problem": "A las 13:00 el Sol está alto y hay mucha luz. A las 22:00 se ven la Luna y las estrellas. ¿Cuál es de día y cuál de noche?", "steps": ["El Sol alto y mucha luz: es de día.", "Luna, estrellas y poca luz: es de noche."], "answer": "13:00 es de día y 22:00 es de noche"},
        {"title": "Contar horas de luz", "problem": "El Sol se ve desde las 7:00 hasta las 19:00. ¿Cuántas horas hay de luz?", "steps": ["De 7:00 a 19:00 pasan 12 horas.", "7 + 12 = 19."], "answer": "12 horas"},
    ],
    mistakes=[
        {"wrong": "Mirar el Sol para ver cómo está en el cielo.", "why": "Se quiere observar bien.", "fix": "Mira la sombra o la luz en el suelo; nunca mires directo al Sol."},
        {"wrong": "Decir que la Luna solo se ve de noche.", "why": "Se generaliza desde la noche.", "fix": "A veces la Luna también se ve de día; pero hay más luz del Sol."},
    ],
    tiers={
        "recovery": [
            ex("A las 13:00 se ve el Sol y hay mucha luz. ¿Es día o noche?", "Día", "El Sol y la luz son del día."),
            ex("A las 22:00 se ven estrellas y hay poca luz. ¿Es día o noche?", "Noche", "Sin Sol y con estrellas."),
            ex("Para saber dónde está el Sol, ¿miras directo a él o miras la sombra de un objeto?", "Miro la sombra de un objeto", "Mirar directo al Sol daña los ojos."),
        ],
        "understand": [
            ex("¿Qué cosas se ven en el cielo de noche?", "La Luna y las estrellas", "No se ve el Sol."),
            ex("¿Qué es el atardecer?", "El momento en que el Sol se va escondiendo", "Termina el día."),
            ex("¿Qué tres datos anotas en un registro del cielo?", "La hora, qué ves y cuánta luz hay", "Son los datos de la clase."),
        ],
        "apply": [
            arith("El Sol se ve desde las 7:00 hasta las 19:00. Son 12 horas. Si una noche dura 24 horas menos esas 12 horas, ¿cuántas horas de noche hay?", "24-12", "Se resta el día del total de 24 horas.", " horas"),
            ex("Registro: 8:00 Sol bajo y luz suave; 13:00 Sol alto y mucha luz. ¿A qué hora hay más luz?", "A las 13:00", "El Sol está más alto."),
            ex("Registro: 19:00 luz naranja y Sol bajo. ¿Qué momento del día es?", "El atardecer", "El Sol se va escondiendo."),
        ],
        "reason": [
            ex("Juan dice que a las 3 de la tarde es de noche porque hace frío. ¿Qué dato muestra que es de día?", "Que se ve el Sol y hay mucha luz", "La luz es la pista."),
            ex("En un lugar con una luz de calle potente, ¿cómo sabes si es de noche?", "Porque no se ve el Sol y se ven las estrellas", "El Sol es la pista del día."),
        ],
        "challenge": [
            ex("Escribe tres cosas que ves en el cielo de día.", "Por ejemplo el Sol, nubes y pájaros", "Son visibles de día."),
            ex("Hay 5 estrellas visibles a las 21:00 y 3 más a las 22:00. ¿Cuántas estrellas ves?", "8", "Cinco más tres son ocho."),
        ],
    },
    context=[ex("Una niña anota que a las 8:00 salió el Sol y a las 20:30 ya casi no hay luz. ¿Cuántas horas y media de luz anotó? Cuenta de 8:00 a 20:30.", "12 horas y media", "De 8:00 a 20:00 son 12 horas y 30 minutos más.")],
    selfcheck=[ex("¿Qué se ve de noche?", "La Luna y las estrellas", "No hay Sol."), ex("¿Qué se ve de día?", "El Sol", "Da mucha luz."), ex("¿Qué es luminosidad?", "Cuánta luz hay", "Se anota en el registro.")],
    open_task=task("Mira este registro y escribe si cada hora es día o noche y por qué: 6:30 (el Sol sale, luz suave), 12:00 (Sol alto, mucha luz), 18:30 (Sol bajo, luz naranja), 23:00 (Luna y estrellas, poca luz). Dibuja el cielo de dos horas.", "6:30 día porque el Sol sale; 12:00 día con mucha luz; 18:30 día que termina; 23:00 noche con Luna y estrellas. Dibujo: Sol alto a las 12:00 y estrellas a las 23:00.", ["clasifica cada hora", "da una razón con el Sol o la luz", "dibuja dos momentos"], ["tabla", "dibujos"], ["decir que 6:30 es noche sin razón", "mirar al Sol"], "Reconoce las pistas y pide dar una razón con la luz o el Sol."),
    reinforce="Mira desde la ventana a tres horas distintas y dibuja el cielo.",
    extend="Explica por qué hay momentos del día en que no es ni muy claro ni muy oscuro.",
)

register(
    OA11, 2,
    materials="Este cuaderno con una tabla de la sombra de un lápiz a distintas horas (datos de ejemplo), seis tarjetas del ciclo del día, lápiz y colores. En casa: un lápiz parado con plasticina y una regla.",
    use="Aprenderé a ordenar las partes de un día y a ver cómo cambia la sombra. Sirve para entender que el día siempre sigue el mismo ciclo.",
    prior=["Sé qué hay en el cielo de día y de noche.", "Sé medir con una regla."],
    explain=[
        "El día sigue un ciclo, que se repite todos los días. El orden es: amanecer, mañana, mediodía, tarde, atardecer y noche. Después de la noche viene otro amanecer.",
        "El Sol parece moverse en el cielo: sale por el lado del oriente (este), sube hasta lo más alto al mediodía y baja hasta esconderse por el poniente (oeste). En realidad es la Tierra la que gira.",
        "La sombra de un objeto cambia con el Sol. Datos de ejemplo de un lápiz de 10 cm: a las 9:00 su sombra mide 14 cm; a las 13:00 mide 4 cm; a las 18:00 mide 16 cm. Al mediodía la sombra es más corta porque el Sol está más alto.",
    ],
    vocab=[("ciclo", "algo que se repite siempre en el mismo orden"), ("mediodía", "momento en que el Sol está más alto"), ("oriente", "lado por donde sale el Sol"), ("poniente", "lado por donde se esconde el Sol"), ("sombra", "zona oscura que deja un objeto cuando le da luz")],
    worked=[
        {"title": "Ordenar el ciclo", "problem": "Ordena: noche, mediodía, amanecer, atardecer, mañana, tarde.", "steps": ["Amanecer, mañana, mediodía.", "Tarde, atardecer, noche."], "answer": "Amanecer, mañana, mediodía, tarde, atardecer y noche"},
        {"title": "Leer la sombra", "problem": "Sombras del lápiz: 9:00 = 14 cm, 13:00 = 4 cm, 18:00 = 16 cm. ¿Cuándo es más corta?", "steps": ["Comparo 14, 4 y 16.", "4 es la menor."], "answer": "A las 13:00; el Sol está más alto"},
    ],
    mistakes=[
        {"wrong": "Pensar que el Sol sale por un lugar distinto cada día.", "why": "Se mira poco tiempo.", "fix": "Sale por el oriente y se esconde por el poniente."},
        {"wrong": "Decir que la sombra es más larga al mediodía.", "why": "Se confunde con la tarde.", "fix": "Al mediodía el Sol está alto y la sombra es corta."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué viene después de la noche?", "El amanecer", "El ciclo se repite."),
            ex("¿Por dónde sale el Sol: oriente o poniente?", "Oriente", "Sale por el oriente."),
            ex("¿Cuándo está más alto el Sol: al mediodía o al atardecer?", "Al mediodía", "Está en lo más alto."),
        ],
        "understand": [
            ex("¿Qué es un ciclo?", "Algo que se repite siempre en el mismo orden", "Como el ciclo del día."),
            ex("¿Por qué la sombra es más corta al mediodía?", "Porque el Sol está más alto", "Cae casi de arriba."),
            ex("¿Por dónde se esconde el Sol?", "Por el poniente", "Es el lado contrario del oriente."),
        ],
        "apply": [
            arith("A las 9:00 la sombra mide 14 cm y a las 13:00 mide 4 cm. ¿Cuántos centímetros más corta es a las 13:00?", "14-4", "Se resta la sombra del mediodía a la de la mañana.", " cm"),
            arith("A las 13:00 la sombra mide 4 cm y a las 18:00 mide 16 cm. ¿Cuántos centímetros más larga es a las 18:00?", "16-4", "Se resta la sombra corta a la larga.", " cm"),
            ex("Ordena las sombras de más corta a más larga: 9:00 = 14 cm, 13:00 = 4 cm, 18:00 = 16 cm.", "4 cm, 14 cm, 16 cm", "Cuatro, catorce y dieciséis."),
        ],
        "reason": [
            ex("Pedro midió la sombra a las 10:00 y a las 15:00 y dijo que eran iguales. Si son 12 cm y 11 cm, ¿qué dato le falta ver?", "Que son parecidas pero no iguales", "Doce y once no son lo mismo."),
            ex("Si por la mañana la sombra de un árbol cae hacia el poniente, ¿por dónde sale el Sol?", "Por el oriente", "La sombra cae al lado contrario del Sol."),
        ],
        "challenge": [
            ex("Escribe qué hora creerías que es: la sombra de un poste es muy larga y el Sol está bajo.", "Amanecer o atardecer", "El Sol bajo da sombras largas."),
            ex("En un día se anotan 6 momentos del ciclo y mañana otros 6. ¿Cuántos son en dos días?", "12", "Seis más seis son doce."),
        ],
    },
    context=[ex("Un niño mide la sombra de su lápiz a las 10:00: 9 cm; a las 13:00: 3 cm; a las 17:00: 12 cm. ¿A qué hora es la sombra más corta?", "A las 13:00", "Tres es el menor.")],
    selfcheck=[ex("¿Cuántos momentos tiene el ciclo del día que vimos?", "6", "Amanecer, mañana, mediodía, tarde, atardecer y noche."), ex("¿Por dónde sale el Sol?", "Por el oriente", "Por el este."), ex("¿Cuándo es corta la sombra?", "Al mediodía", "El Sol está alto.")],
    open_task=task("Ordena las seis tarjetas del día y pega cada una en una tabla con la sombra que le corresponde: amanecer (sombra muy larga), mañana (larga), mediodía (muy corta), tarde (larga), atardecer (muy larga), noche (sin sombra). Dibuja el Sol sale por el oriente.", "Amanecer-muy larga, mañana-larga, mediodía-muy corta, tarde-larga, atardecer-muy larga, noche-sin sombra. Dibujo: Sol sube por la izquierda (oriente) y baja por la derecha (poniente).", ["ordena las seis tarjetas", "une cada una con la sombra", "marca oriente y poniente"], ["tabla", "dibujo"], ["poner la sombra más larga al mediodía", "olvidar la noche"], "Reconoce el orden y pide explicar la sombra del mediodía."),
    reinforce="Con ayuda de un adulto, mide la sombra de un lápiz a tres horas del día.",
    extend="Explica por qué en la noche no hay sombra del Sol.",
)

register(
    OA11, 3,
    materials="Este cuaderno con una tabla de seres vivos en el día y la noche y datos de temperatura (ejemplo), lápiz y colores.",
    use="Aprenderé cómo el día y la noche cambian la vida de las personas, los animales y las plantas. Sirve para entender por qué dormimos de noche y cómo se organizan los seres vivos.",
    prior=["Sé el ciclo del día.", "Sé que los seres vivos responden a estímulos como la luz."],
    explain=[
        "Los seres vivos cambian lo que hacen entre el día y la noche. La mayoría de las personas trabajan o estudian de día y duermen de noche. Muchos pájaros cantan al amanecer. Los gallos cantan al salir el Sol.",
        "Algunos animales son nocturnos, es decir, están activos de noche, como el búho y el murciélago. Otros son diurnos, activos de día, como las abejas. Algunas flores abren de día y se cierran de noche.",
        "El ambiente también cambia. De día hace más calor y de noche más frío. Datos de ejemplo: a las 14:00 hay 24 grados, y a las 4:00 hay 12 grados. Por eso de noche necesitamos más abrigo.",
    ],
    vocab=[("nocturno", "que está activo de noche"), ("diurno", "que está activo de día"), ("abrigo", "ropa que da calor"), ("ambiente", "lo que rodea a los seres vivos"), ("temperatura", "qué tan caliente o frío está algo")],
    worked=[
        {"title": "Animales nocturnos y diurnos", "problem": "El búho caza de noche y la abeja visita flores de día. ¿Cuál es nocturno?", "steps": ["El búho está activo de noche.", "La abeja está activa de día."], "answer": "El búho es nocturno y la abeja es diurna"},
        {"title": "Cambio de temperatura", "problem": "A las 14:00 hay 24 grados y a las 4:00 hay 12 grados. ¿Cuántos grados más hace a las 14:00?", "steps": ["24 menos 12 son 12.", "Hace 12 grados más de día."], "answer": "12 grados más"},
    ],
    mistakes=[
        {"wrong": "Pensar que todos los animales duermen de noche.", "why": "Se generaliza desde las personas.", "fix": "Los nocturnos, como el búho, están activos de noche."},
        {"wrong": "Pensar que de noche hace tanto calor como de día.", "why": "No se mide.", "fix": "Sin Sol, el ambiente se enfría; mira los grados."},
    ],
    tiers={
        "recovery": [
            ex("¿El búho es activo de día o de noche?", "De noche", "El búho es un animal nocturno."),
            ex("¿La abeja visita flores de día o de noche?", "De día", "La abeja es un animal diurno."),
            ex("¿Cuándo canta el gallo?", "Al amanecer", "Responde a la luz del Sol."),
        ],
        "understand": [
            ex("¿Qué quiere decir nocturno?", "Que está activo de noche", "Vive de noche."),
            ex("¿Por qué de noche necesitas más abrigo?", "Porque hace más frío", "Sin Sol baja la temperatura."),
            ex("¿Qué hacen muchas flores de noche?", "Se cierran", "Responden a la falta de luz."),
        ],
        "apply": [
            arith("A las 14:00 hay 24 grados y a las 4:00 hay 12 grados. ¿Cuántos grados menos hace a las 4:00?", "24-12", "Se resta la temperatura de la noche a la del día.", " grados"),
            ex("Animales: búho, abeja, murciélago, mariposa de día. ¿Cuántos son nocturnos?", "2", "El búho y el murciélago."),
            ex("Tabla: a las 8:00 hay 14 grados y a las 16:00 hay 22 grados. ¿A qué hora hace más calor?", "A las 16:00", "Veintidós es mayor que catorce."),
        ],
        "reason": [
            ex("Ana dice que el murciélago está dormido de noche. ¿Qué respondes?", "Que está despierto, porque es nocturno", "Los nocturnos están activos de noche."),
            ex("Mario dice que las personas duermen de noche porque hay poca luz. ¿Qué otra razón ayuda?", "Que el cuerpo necesita descansar", "El descanso se hace de noche."),
        ],
        "challenge": [
            ex("Escribe un animal diurno y uno nocturno.", "Por ejemplo abeja y búho", "Uno vive de día y el otro de noche."),
            ex("En un jardín hay 4 flores abiertas de día y 4 que se cierran de noche. ¿Cuántas flores hay?", "8", "Cuatro más cuatro son ocho."),
        ],
    },
    context=[ex("Una familia sale de campamento: de día 26 grados y de noche 11 grados. ¿Cuántos grados baja la temperatura?", "15 grados", "Veintiséis menos once son quince.")],
    selfcheck=[ex("¿Qué animal es nocturno?", "El búho", "Está activo de noche."), ex("¿Qué es abrigo?", "Ropa que da calor", "Sirve de noche."), ex("¿Cuándo hace más frío?", "De noche", "No hay Sol.")],
    open_task=task("Completa una tabla de día y noche para estos seres vivos: abeja, búho, gallo, murciélago, persona, flor abierta. Escribe si están activos de día o de noche y dibuja uno.", "Abeja: día. Búho: noche. Gallo: día (canta al amanecer). Murciélago: noche. Persona: día (duerme de noche). Flor abierta: día.", ["clasifica los seis", "usa día o noche", "dibuja uno"], ["tabla", "dibujo"], ["poner al búho de día", "no explicar el caso de la persona"], "Reconoce la clasificación y pide una razón para la persona."),
    reinforce="Escucha qué animales se oyen de noche en tu barrio y anótalos.",
    extend="Explica por qué las plantas necesitan el día para fabricar su alimento.",
)

register(
    OA11, 4,
    materials="Este cuaderno con instrucciones para un modelo de día y noche con una linterna y una pelota, una pauta de comunicación, lápiz y colores. En casa: una linterna o lámpara y una naranja o pelota, en una pieza oscura, con un adulto.",
    use="Aprenderé a hacer un modelo del día y la noche y a explicarlo. Sirve para entender por qué hay día y noche.",
    prior=["Sé el ciclo del día.", "Sé qué es un modelo."],
    explain=[
        "La Tierra es como una gran pelota que gira sobre sí misma. Tarda 24 horas, un día completo, en dar una vuelta. El Sol ilumina siempre el lado de la Tierra que mira hacia él. Ese lado tiene día. El otro lado queda a oscuras y tiene noche.",
        "Para hacer un modelo, usa una linterna como el Sol y una naranja como la Tierra. Marca con un palito un punto: esa es tu casa. Gira la naranja lentamente. Cuando tu punto recibe la luz, es de día. Cuando queda a oscuras, es de noche.",
        "Todos los modelos tienen límites. En tu modelo, la naranja es mucho más pequeña que la Tierra y la linterna está muy cerca del Sol real. Aun así, el modelo ayuda a entender por qué hay día y noche.",
    ],
    vocab=[("girar", "dar vueltas sobre uno mismo"), ("iluminar", "dar luz"), ("modelo", "cosa que representa algo real"), ("límite del modelo", "algo que el modelo no muestra bien"), ("vuelta completa", "giro que vuelve al mismo lugar")],
    worked=[
        {"title": "Usar el modelo", "problem": "Con la linterna y la naranja, tu punto queda mirando a la luz. ¿Es día o noche?", "steps": ["El punto recibe luz.", "Si recibe luz, es de día."], "answer": "Es de día"},
        {"title": "Decir un límite", "problem": "La naranja mide 8 cm y la Tierra es enorme. ¿Es un límite del modelo?", "steps": ["El tamaño no es real.", "El modelo no muestra tamaños reales."], "answer": "Sí, es un límite: el tamaño no es real"},
    ],
    mistakes=[
        {"wrong": "Pensar que el Sol gira alrededor de la Tierra todos los días.", "why": "Se ve moverse el Sol en el cielo.", "fix": "Es la Tierra la que gira; por eso parece que el Sol se mueve."},
        {"wrong": "Decir que el modelo es igual a la realidad.", "why": "Se olvidan los límites.", "fix": "Di qué muestra bien y qué no."},
    ],
    tiers={
        "recovery": [
            ex("En el modelo, ¿qué representa la linterna?", "El Sol", "La linterna da luz como el Sol."),
            ex("En el modelo, ¿qué representa la naranja?", "La Tierra", "Es la que gira."),
            ex("Tu punto en la naranja queda a oscuras. ¿Es día o noche?", "Noche", "No recibe luz."),
        ],
        "understand": [
            ex("¿Cuánto tarda la Tierra en dar una vuelta completa?", "24 horas", "Es un día."),
            ex("¿Por qué hay noche en una parte de la Tierra?", "Porque esa parte no recibe la luz del Sol", "Queda a oscuras."),
            ex("En el modelo de día y noche, ¿qué es un límite?", "Algo que el modelo no muestra bien", "Por ejemplo el tamaño real."),
        ],
        "apply": [
            arith("La Tierra tarda 24 horas en dar una vuelta. ¿Cuántas horas tardan 2 vueltas?", "24*2", "Se multiplica por dos vueltas.", " horas"),
            arith("En una ciudad es de día 12 horas y de noche el resto del día de 24 horas. ¿Cuántas horas de noche hay?", "24-12", "Se resta el día del total.", " horas"),
            ex("En el modelo giras la naranja y el punto pasa de la luz a la sombra. ¿Pasó de día a noche o de noche a día?", "De día a noche", "Pasó de recibir luz a estar a oscuras."),
        ],
        "reason": [
            ex("Luis dice que el Sol se apaga de noche. ¿Qué le muestra el modelo?", "Que el Sol sigue alumbrando y el lugar gira a la sombra", "La linterna siempre está prendida."),
            ex("¿Por qué el modelo no es igual a la Tierra real?", "Porque el tamaño y las distancias no son reales", "Esos son límites del modelo."),
        ],
        "challenge": [
            ex("Escribe qué verías en el modelo si dejas el punto 6 horas sin girar frente a la luz.", "Que sigue siendo de día en ese punto", "Sigue recibiendo luz."),
            ex("Una clase hace 4 modelos con linterna y 3 con lámpara. ¿Cuántos modelos hay?", "7", "Cuatro más tres son siete."),
        ],
    },
    context=[ex("Marta gira la naranja una vuelta completa en 24 segundos para representar 24 horas. Cada segundo es una hora. Si el punto está en la sombra 12 segundos, ¿cuántas horas de noche representa?", "12 horas", "Doce segundos son doce horas en el modelo.")],
    selfcheck=[ex("¿Qué gira en realidad: la Tierra o el Sol?", "La Tierra", "Gira sobre sí misma."), ex("¿Qué lado de la Tierra tiene día?", "El que mira al Sol", "Recibe la luz."), ex("¿El modelo de la naranja muestra bien el tamaño real de la Tierra?", "No", "Tiene un límite en el tamaño.")],
    open_task=task("Presenta tu modelo del día y la noche en cuatro frases con estas ideas: la linterna es el Sol; la naranja es la Tierra; el punto marcado recibe luz y es de día; al girar queda a oscuras y es de noche. Termina con un límite del modelo.", "La linterna representa el Sol y la naranja la Tierra. Cuando mi punto recibe luz es de día. Al girar la naranja el punto queda a oscuras y es de noche. Un límite es que la naranja es mucho más pequeña que la Tierra.", ["escribe cuatro frases", "explica día y noche", "dice un límite"], ["frases", "dibujo del modelo"], ["decir que el Sol gira", "olvidar el límite"], "Reconoce el modelo y pide aclarar qué gira."),
    reinforce="Con ayuda de un adulto, haz el modelo con una linterna y una pelota.",
    extend="Explica por qué cuando aquí es de día, en otro lado de la Tierra es de noche.",
)

# ---------------------------------------------------------------- OA 12
register(
    OA12, 1,
    materials="Este cuaderno con una tabla de las cuatro estaciones y sus meses aproximados en Chile, lápiz y colores.",
    use="Aprenderé el orden de las cuatro estaciones y cómo cambia el año. Sirve para entender cuándo hace calor, frío, llueve o florecen las plantas.",
    prior=["Sé los meses del año.", "Sé el ciclo del día."],
    explain=[
        "Un año tiene cuatro estaciones: verano, otoño, invierno y primavera. Se repiten siempre en ese orden. Cuando termina la primavera vuelve el verano.",
        "En Chile, estos son los meses aproximados: verano de diciembre a marzo, otoño de marzo a junio, invierno de junio a septiembre y primavera de septiembre a diciembre. Cada estación dura unos 3 meses.",
        "En cada estación el ambiente cambia: en verano hace calor, en otoño caen hojas de algunos árboles, en invierno hace frío y llueve más en la zona centro y sur, y en primavera aparecen muchas flores.",
    ],
    vocab=[("estación", "una de las cuatro partes del año"), ("verano", "estación cálida"), ("otoño", "estación en que caen las hojas de algunos árboles"), ("invierno", "estación fría"), ("primavera", "estación en que hay muchas flores")],
    worked=[
        {"title": "Ordenar las estaciones", "problem": "Después de la primavera, ¿qué estación viene?", "steps": ["El orden es verano, otoño, invierno, primavera.", "Después de la primavera comienza otra vez el verano."], "answer": "El verano"},
        {"title": "Calcular duración", "problem": "Si cada estación dura 3 meses, ¿cuántos meses tienen las cuatro juntas?", "steps": ["3 + 3 + 3 + 3 = 12.", "Son los 12 meses del año."], "answer": "12 meses"},
    ],
    mistakes=[
        {"wrong": "Pensar que en enero hace frío porque es el comienzo del año.", "why": "Se confunde el comienzo del año con el comienzo del invierno.", "fix": "En Chile enero es verano."},
        {"wrong": "Pensar que el orden de las estaciones cambia cada año.", "why": "No se mira el ciclo.", "fix": "El orden se repite siempre."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué estación viene después del verano?", "El otoño", "El orden es verano, otoño, invierno, primavera."),
            ex("¿En qué estación hace más frío?", "En invierno", "Es la estación fría."),
            ex("¿En qué estación aparecen muchas flores?", "En primavera", "Las plantas florecen."),
        ],
        "understand": [
            ex("¿Cuántas estaciones tiene un año?", "Cuatro", "Verano, otoño, invierno y primavera."),
            ex("¿Qué es un ciclo de estaciones?", "Un orden que se repite cada año", "Siempre vuelve al verano."),
            ex("¿Por qué enero es verano en Chile?", "Porque el verano va de diciembre a marzo", "Son los meses aproximados."),
        ],
        "apply": [
            arith("Cada estación dura 3 meses. ¿Cuántos meses duran el verano y el otoño juntos?", "3+3", "Se suman los meses de las dos estaciones.", " meses"),
            ex("Mes: julio. Tabla: invierno de junio a septiembre. ¿En qué estación está julio?", "En invierno", "Julio está entre junio y septiembre."),
            ex("Mes: octubre. Tabla: primavera de septiembre a diciembre. ¿En qué estación está octubre?", "En primavera", "Octubre está entre septiembre y diciembre."),
        ],
        "reason": [
            ex("Rosa dice que el verano viene después del invierno. ¿Qué estación falta en medio?", "La primavera", "El orden es invierno, primavera, verano."),
            ex("Si hoy es abril, ¿en qué estación estás y cómo lo sabes?", "En otoño, porque abril está entre marzo y junio", "La tabla lo indica."),
        ],
        "challenge": [
            ex("Escribe los 12 meses agrupados por estación.", "Verano: diciembre, enero y febrero; otoño: marzo, abril y mayo; invierno: junio, julio y agosto; primavera: septiembre, octubre y noviembre", "Cada estación tiene tres meses."),
            ex("Una estación tiene 3 meses; ¿cuántas estaciones caben en 9 meses?", "3", "Nueve dividido en tres son tres."),
        ],
    },
    context=[ex("Tu cumpleaños es en julio. ¿En qué estación es?", "En invierno", "Julio está entre junio y septiembre.")],
    selfcheck=[ex("¿Qué estación viene después de la primavera?", "El verano", "El ciclo vuelve a empezar."), ex("¿Cuántos meses dura cada estación?", "Unos 3 meses", "Cuatro por tres son doce."), ex("¿Qué estación es fría?", "El invierno", "Hay frío y lluvia.")],
    open_task=task("Completa el reloj de las estaciones con estos meses: enero, abril, julio, octubre. Dibuja un círculo con cuatro partes: escribe la estación de cada mes y un dibujo del ambiente de cada una.", "Enero: verano (sol y calor). Abril: otoño (hojas cayendo). Julio: invierno (lluvia y frío). Octubre: primavera (flores).", ["une cada mes con su estación", "dibuja el ambiente", "respeta el orden"], ["círculo de estaciones", "dibujos"], ["poner enero en invierno", "desordenar las estaciones"], "Reconoce el orden y pide explicar con un dibujo cada estación."),
    reinforce="Escribe qué estación es hoy y cómo lo sabes.",
    extend="Explica qué cambia en tu calle de una estación a otra.",
)

register(
    OA12, 2,
    materials="Este cuaderno con una tabla de datos de ejemplo de las cuatro estaciones (temperatura máxima y horas de luz), lápiz y colores.",
    use="Aprenderé a comparar las estaciones con datos de temperatura y horas de luz. Sirve para explicar por qué se sienten distintas.",
    prior=["Sé el orden de las estaciones.", "Sé comparar números."],
    explain=[
        "Las estaciones se diferencian por la temperatura, las horas de luz y la lluvia. En verano hace más calor y los días son más largos. En invierno hace más frío y los días son más cortos.",
        "Datos de ejemplo cercanos a la zona central de Chile: verano, 30 grados y unas 14 horas de luz; otoño, 20 grados y unas 11 horas; invierno, 13 grados y unas 10 horas; primavera, 22 grados y unas 13 horas.",
        "Con una tabla puedes comparar. Verano tiene 17 grados más que invierno, porque 30 menos 13 son 17. Y tiene 4 horas de luz más, porque 14 menos 10 son 4. Estos datos explican por qué en verano jugamos hasta tarde.",
    ],
    vocab=[("temperatura", "qué tan caliente o frío está"), ("grado", "unidad para medir la temperatura"), ("horas de luz", "tiempo en que hay luz del Sol"), ("comparar", "ver en qué se parecen y en qué se diferencian"), ("máxima", "la más alta del día")],
    worked=[
        {"title": "Comparar temperaturas", "problem": "Verano 30 grados, invierno 13 grados. ¿Cuántos grados más hace en verano?", "steps": ["30 menos 13.", "Son 17."], "answer": "17 grados más"},
        {"title": "Comparar horas de luz", "problem": "Verano 14 horas, invierno 10 horas. ¿Cuántas horas más de luz hay en verano?", "steps": ["14 menos 10.", "Son 4."], "answer": "4 horas más"},
    ],
    mistakes=[
        {"wrong": "Decir «el verano es mejor» como comparación.", "why": "Es una opinión.", "fix": "Compara con datos de la tabla."},
        {"wrong": "Mezclar grados con horas.", "why": "Se pierden las unidades.", "fix": "Escribe siempre la unidad: grados u horas."},
    ],
    tiers={
        "recovery": [
            ex("Tabla: verano 30 grados, invierno 13 grados. ¿En cuál hace más calor?", "En verano", "Treinta es mayor que trece."),
            ex("Tabla: invierno 10 horas de luz, verano 14. ¿Cuándo hay menos luz?", "En invierno", "Diez es menor que catorce."),
            ex("Tabla: otoño 20 grados, primavera 22 grados. ¿Cuál es más cálida?", "La primavera", "Veintidós es mayor que veinte."),
        ],
        "understand": [
            ex("¿Qué dos datos usamos para comparar las estaciones?", "La temperatura y las horas de luz", "Son los datos de la tabla."),
            ex("¿Por qué en verano se juega hasta más tarde?", "Porque hay más horas de luz", "Oscurece más tarde."),
            ex("¿Qué unidad usamos para la temperatura?", "Grados", "Se mide en grados."),
        ],
        "apply": [
            arith("Verano tiene 30 grados y otoño 20 grados. ¿Cuántos grados más tiene el verano?", "30-20", "Se resta la temperatura menor a la mayor.", " grados"),
            arith("Primavera tiene 13 horas de luz e invierno 10. ¿Cuántas horas más de luz hay en primavera?", "13-10", "Se resta la luz de invierno.", " horas"),
            ex("Ordena de más fría a más cálida: verano 30, otoño 20, invierno 13, primavera 22.", "Invierno, otoño, primavera, verano", "Trece, veinte, veintidós y treinta."),
        ],
        "reason": [
            ex("Juan dice que en otoño y primavera hace igual de calor. ¿Qué dato lo contradice?", "Otoño 20 grados y primavera 22 grados", "Son 2 grados de diferencia."),
            ex("¿Qué estación tiene más horas de luz y cómo lo sabes?", "El verano, con unas 14 horas", "Es el número mayor de la tabla."),
        ],
        "challenge": [
            ex("Escribe una semejanza entre otoño y primavera con los datos.", "Ambas tienen temperaturas medias, 20 y 22 grados", "Están entre el calor y el frío."),
            ex("Suma las horas de luz de las cuatro estaciones de la tabla: 14, 11, 10 y 13.", "48 horas", "Catorce más once más diez más trece son cuarenta y ocho."),
        ],
    },
    context=[ex("Una familia viaja en verano y en invierno. En verano oscurece a las 21:00 y en invierno a las 18:00. ¿Cuántas horas más tarde oscurece en verano?", "3 horas", "Veintiuno menos dieciocho son tres.")],
    selfcheck=[ex("¿Cuándo hay más horas de luz?", "En verano", "Los días son más largos."), ex("¿Cuál estación es la más fría del año?", "El invierno", "Su temperatura es la más baja de la tabla."), ex("¿Qué se escribe junto al número 30 en la tabla?", "Grados", "Es la unidad de la temperatura.")],
    open_task=task("Con la tabla de la clase (verano 30 grados y 14 horas; otoño 20 y 11; invierno 13 y 10; primavera 22 y 13), escribe tres comparaciones con números: una entre verano e invierno, una entre otoño y primavera y una de horas de luz. Dibuja una barra para cada estación.", "Verano tiene 17 grados más que invierno. Primavera tiene 2 grados más que otoño. Verano tiene 4 horas de luz más que invierno.", ["escribe tres comparaciones", "usa números con unidad", "dibuja barras"], ["tres frases", "gráfico de barras"], ["olvidar la unidad", "calcular mal"], "Reconoce las comparaciones y pide revisar la unidad en cada una."),
    reinforce="Anota la temperatura de tu pieza esta semana y compárala.",
    extend="Explica por qué las estaciones del hemisferio norte son al revés que las de Chile.",
)

register(
    OA12, 3,
    materials="Este cuaderno con una tabla de seres vivos y alimentos en cada estación, lápiz y colores.",
    use="Aprenderé cómo las estaciones cambian a las plantas, los animales y las personas. Sirve para entender por qué usamos distinta ropa y comemos distintas frutas.",
    prior=["Sé las cuatro estaciones.", "Sé que los seres vivos necesitan agua, alimento y aire."],
    explain=[
        "Las plantas cambian con las estaciones. En primavera aparecen flores y brotes nuevos. En verano hay frutos, como la sandía y los duraznos. En otoño los árboles de hojas caducas, como el álamo, pierden las hojas. En invierno hay lluvia y muchas plantas crecen menos.",
        "Los animales también cambian. Algunas aves viajan a lugares más cálidos cuando llega el frío. Otros animales cambian su pelaje y otros pasan más tiempo escondidos. Las personas usamos ropa de abrigo en invierno y ropa fresca en verano.",
        "Los alimentos de estación son los que maduran en cierta época. Sandía y durazno son del verano. Zapallo, de otoño. Mandarinas y naranjas, de invierno. Frutillas, de primavera.",
    ],
    vocab=[("hoja caduca", "hoja que cae en otoño"), ("brote", "hoja o flor nueva que aparece"), ("migrar", "viajar a otro lugar según la estación"), ("pelaje", "pelo de un animal"), ("de estación", "que maduran en cierta época del año")],
    worked=[
        {"title": "Efecto en las plantas", "problem": "El álamo pierde las hojas en otoño. ¿Qué tipo de hoja tiene?", "steps": ["Las hojas caen en una estación.", "Se llaman caducas."], "answer": "Hojas caducas"},
        {"title": "Elegir ropa", "problem": "Es julio, invierno, hace 13 grados y llueve. ¿Qué ropa eliges?", "steps": ["Hace frío.", "Llueve.", "Elijo abrigo y chaqueta impermeable."], "answer": "Abrigo y chaqueta impermeable"},
    ],
    mistakes=[
        {"wrong": "Pensar que los árboles se mueren en otoño.", "why": "Se ve que pierden las hojas.", "fix": "Siguen vivos; en primavera les salen hojas nuevas."},
        {"wrong": "Pensar que todos los árboles pierden las hojas.", "why": "Se generaliza.", "fix": "Algunos, como el pino, mantienen sus hojas todo el año."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué estación aparecen más flores?", "En primavera", "Las plantas florecen."),
            ex("¿En qué estación pierde sus hojas el álamo?", "En otoño", "Es una hoja caduca."),
            ex("¿Qué ropa usas en invierno?", "Ropa de abrigo", "En invierno hace frío y llueve."),
        ],
        "understand": [
            ex("¿Qué es una hoja caduca?", "Una hoja que cae en una estación del año", "Cae en otoño."),
            ex("¿Qué significa migrar?", "Viajar a otro lugar según la estación", "Algunas aves lo hacen."),
            ex("¿Qué es un alimento de estación?", "El que madura en cierta época del año", "Por ejemplo la sandía en verano."),
        ],
        "apply": [
            ex("Alimentos: sandía, mandarina, zapallo, frutilla. ¿Cuál es del invierno?", "La mandarina", "Madura en invierno."),
            arith("En un jardín hay 5 árboles de hojas caducas y 3 pinos. ¿Cuántos árboles son?", "5+3", "Se suman los dos tipos.", " árboles"),
            ex("Es enero y hace 30 grados. ¿Qué ropa eliges: abrigo o ropa fresca?", "Ropa fresca", "En verano hace mucho calor."),
        ],
        "reason": [
            ex("Ema vio un álamo sin hojas en julio y dijo que se murió. ¿Qué le dices?", "Que sigue vivo y le saldrán hojas en primavera", "Es una planta de hojas caducas."),
            ex("¿Por qué comer frutas de estación es buena idea?", "Porque están maduras y frescas en su época", "Maduran cuando corresponde."),
        ],
        "challenge": [
            ex("Escribe una cosa que cambia en las plantas y una en las personas en invierno.", "Por ejemplo las plantas crecen menos y las personas usan abrigo", "Cada estación cambia la vida."),
            ex("En el huerto hay 4 plantas con flores en primavera y 6 en verano. ¿Cuántas más en verano?", "2", "Seis menos cuatro son dos."),
        ],
    },
    context=[ex("En el mercado ves sandías en enero y mandarinas en julio. ¿Qué estación es cada mes?", "Enero es verano y julio es invierno", "La sandía es de verano y la mandarina de invierno.")],
    selfcheck=[ex("¿Qué estación tiene más flores?", "La primavera", "Las plantas florecen."), ex("¿Qué hacen algunas aves en invierno?", "Viajan a lugares más cálidos", "Migran cuando llega el frío."), ex("¿Qué fruta es de verano?", "La sandía", "Madura con el calor.")],
    open_task=task("Completa una tabla con las cuatro estaciones: escribe una ropa, una fruta y un cambio de las plantas para cada una. Opciones: ropa (polera, chaleco, abrigo, chaqueta ligera); frutas (sandía, zapallo, mandarina, frutilla); cambios (flores, hojas que caen, lluvia, frutos maduros).", "Verano: polera, sandía, frutos maduros. Otoño: chaleco, zapallo, hojas que caen. Invierno: abrigo, mandarina, lluvia. Primavera: chaqueta ligera, frutilla, flores.", ["completa las cuatro estaciones", "une ropa, fruta y cambio", "usa las opciones"], ["tabla de 4 filas", "dibujo"], ["poner abrigo en verano", "repetir la misma fruta"], "Reconoce el uso de las opciones y pide justificar una elección."),
    reinforce="Mira un árbol de tu calle durante un mes y anota si cambia.",
    extend="Explica por qué algunos árboles pierden sus hojas en otoño.",
)

register(
    OA12, 4,
    materials="Este cuaderno con una ficha para un informe de las estaciones de un barrio imaginario (datos escritos), una pauta y lápiz y colores.",
    use="Aprenderé a hacer un informe corto con datos de las estaciones. Sirve para comunicar a otras personas cómo cambia el año.",
    prior=["Sé comparar estaciones con datos.", "Sé los efectos de las estaciones en los seres vivos."],
    explain=[
        "Un informe de estaciones cuenta cómo cambia un lugar durante el año. Debe tener cuatro partes: el nombre del lugar, un dato de cada estación, un efecto en los seres vivos y una conclusión.",
        "Ejemplo con la plaza de un barrio: verano, 29 grados y mucha sombra de los árboles; otoño, 19 grados y hojas en el suelo; invierno, 11 grados y poca gente; primavera, 21 grados y flores en los jardines. Los datos muestran que el calor sube de invierno a verano.",
        "Una buena conclusión resume lo más importante: «La plaza cambia durante el año por la temperatura y la luz. En invierno hay menos gente y en primavera aparecen flores». Usa los datos para apoyarla.",
    ],
    vocab=[("informe", "texto corto que cuenta lo observado"), ("dato", "número o hecho observado"), ("efecto", "cambio que causa algo"), ("conclusión", "idea final que resume lo aprendido"), ("barrio", "zona de la ciudad donde vivimos")],
    worked=[
        {"title": "Elegir el dato de cada estación", "problem": "Plaza: verano 29 grados, otoño 19, invierno 11, primavera 21. ¿Cuál es la estación más fría?", "steps": ["Comparo 29, 19, 11 y 21.", "11 es el menor."], "answer": "El invierno"},
        {"title": "Escribir la conclusión", "problem": "Con los datos de la plaza, escribe una conclusión.", "steps": ["Dato 1: de 11 a 29 grados hay 18 grados de diferencia.", "Dato 2: en primavera hay flores.", "Resume: la plaza cambia con el año."], "answer": "La plaza cambia durante el año: más calor en verano, flores en primavera"},
    ],
    mistakes=[
        {"wrong": "Escribir un informe sin datos.", "why": "Se piensa que basta con opiniones.", "fix": "Incluye al menos un número por estación."},
        {"wrong": "Terminar sin conclusión.", "why": "Se olvida resumir.", "fix": "Agrega una frase que una los datos."},
    ],
    tiers={
        "recovery": [
            ex("Plaza: invierno 11 grados, verano 29 grados. ¿En cuál estación hace más frío?", "En invierno", "Once es menor que veintinueve."),
            ex("¿Qué efecto hay en primavera en los jardines de la plaza?", "Hay flores", "Está en el informe."),
            ex("¿Qué parte del informe resume lo aprendido?", "La conclusión", "Cierra el informe."),
        ],
        "understand": [
            ex("¿Cuántas partes tiene el informe de la clase?", "Cuatro", "Lugar, un dato de cada estación, un efecto y una conclusión."),
            ex("¿Por qué un informe necesita datos?", "Para apoyar lo que cuenta", "Los números se pueden comprobar."),
            ex("¿Qué es un efecto?", "Un cambio que causa algo", "Por ejemplo, las flores en primavera."),
        ],
        "apply": [
            arith("Plaza: verano 29 grados e invierno 11 grados. ¿Cuántos grados más hace en verano?", "29-11", "Se resta la temperatura de invierno.", " grados"),
            arith("Otoño 19 grados y primavera 21 grados. ¿Cuántos grados más hace en primavera?", "21-19", "Se resta la de otoño.", " grados"),
            ex("Ordena las estaciones de la plaza de más cálida a más fría: verano 29, otoño 19, invierno 11, primavera 21.", "Verano, primavera, otoño, invierno", "Veintinueve, veintiuno, diecinueve y once."),
        ],
        "reason": [
            ex("Pía escribió «la plaza es lindísima» como conclusión. ¿Qué le falta?", "Datos que la apoyen", "Lindísima es una opinión."),
            ex("¿Por qué conviene decir de qué lugar es el informe?", "Para que se sepa de dónde vienen los datos", "El lugar da contexto."),
        ],
        "challenge": [
            ex("Escribe una conclusión de dos frases para el informe de la plaza.", "La plaza es más cálida en verano y fría en invierno. En primavera tiene flores", "Resume datos y efectos."),
            ex("Un informe tiene 4 datos de temperatura y 2 efectos. ¿Cuántos datos en total?", "6", "Cuatro más dos son seis."),
        ],
    },
    context=[ex("En tu informe anotas 29 grados en verano y 11 en invierno. Ema anotó 29 en verano y 14 en invierno. ¿Quién dice que hace menos frío en invierno?", "Ema", "Catorce es mayor que once.")],
    selfcheck=[ex("¿Qué incluye un informe de estaciones?", "Lugar, datos, efectos y conclusión", "Son las cuatro partes."), ex("¿Qué va al final?", "La conclusión", "Resume lo aprendido."), ex("¿Una opinión es un dato?", "No", "Un dato se puede comprobar.")],
    open_task=task("Escribe un informe corto de la plaza con estos datos: verano 29 grados y sombra de árboles; otoño 19 grados y hojas en el suelo; invierno 11 grados y poca gente; primavera 21 grados y flores. Incluye lugar, un dato de cada estación, un efecto y una conclusión.", "En la plaza del barrio, en verano hace 29 grados, en otoño 19, en invierno 11 y en primavera 21. En otoño caen hojas y en primavera hay flores. La plaza cambia por la temperatura y la luz del año.", ["incluye lugar y cuatro datos", "nombra un efecto", "escribe una conclusión"], ["informe de 4 frases", "dibujo de dos estaciones"], ["omitir la conclusión", "no incluir números"], "Reconoce las partes y pide una conclusión apoyada en un dato."),
    reinforce="Elige un árbol de tu calle y escribe cómo se ve en esta estación.",
    extend="Compara tu informe con el de un compañero y busca una diferencia.",
)

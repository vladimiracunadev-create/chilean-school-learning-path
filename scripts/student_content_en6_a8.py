"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 08 (reaccionar ante lo leído: esquemas, ilustraciones, dramatizaciones, párrafos y tiras cómicas).

Todos los textos están escritos en el enunciado y son originales; llevan pista en español.
Cada palabra o estructura nueva se explica antes de usarla. Sin audio externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA8 = "EN06 OA 08"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- clase 1: esquemas y organizadores gráficos
OTTO = "«Otto has a new bike, but one wheel is flat. He asks his neighbour for a pump. His neighbour helps him inflate the wheel. Otto rides to school happily.» (wheel = rueda, flat = desinflada, neighbour = vecino, pump = bomba de aire, inflate = inflar, happily = contento)"
SPORTS = "«Football is played on a field with a ball. Players kick the ball. Swimming is done in a pool, and swimmers move in the water. Both sports need practice and give exercise. Football is a team sport, but swimming can be done alone.» (field = cancha, kick = patear, pool = piscina, practice = práctica, exercise = ejercicio, alone = solo)"

lesson(
    OA8, 1,
    "Los textos escritos en cada ejercicio, lápiz, una hoja y reglas o líneas dibujadas a mano.",
    "Aprenderé a mostrar lo que leí con un esquema u organizador gráfico, como un mapa del cuento o un diagrama de comparación. Sirve para reaccionar ante un texto de forma visual y ordenada.",
    ["Sé identificar personajes, problema y solución.", "Conozco palabras como both, alone y practice."],
    [
        "Un organizador gráfico (graphic organizer) es un dibujo donde ordenas la información de un texto. El mapa del cuento (story map) tiene cuatro casillas: Characters (personajes), Setting (lugar y tiempo), Problem (problema) y Solution (solución). Se completa con palabras clave, no con oraciones largas.",
        "Para comparar dos cosas se usa un diagrama de Venn: dos círculos que se cruzan. En cada círculo se anotan las diferencias de cada cosa, y en la parte común se anota lo que tienen igual (both significa ambos). También existen tablas de dos columnas y esquemas con flechas para mostrar causa y efecto.",
        "Al hacer un organizador, escribe solo lo que el texto dice. Si el texto no menciona el lugar, escribe «no se dice» en lugar de inventarlo. Un esquema bien hecho te permite explicar el texto a otra persona en un minuto. También sirve para expresar tu opinión: puedes agregar una casilla «My opinion» al final.",
    ],
    [("graphic organizer", "organizador gráfico"), ("story map", "mapa del cuento"), ("Venn diagram", "diagrama de Venn: dos círculos para comparar"), ("both", "ambos"), ("difference", "diferencia"), ("same", "igual")],
    [
        ("Completar un mapa del cuento", "Lee: «Tina has a small garden. Birds eat her seeds. She makes a scarecrow. Now the birds do not eat the seeds.» (seeds = semillas, scarecrow = espantapájaros). Completa: personajes, lugar, problema y solución.", ["Personaje: Tina (y los pájaros).", "Lugar: su jardín pequeño.", "Problema: los pájaros comen las semillas. Solución: hace un espantapájaros."], "Personajes: Tina; lugar: jardín; problema: pájaros comen semillas; solución: espantapájaros"),
        ("Usar la parte común", "Lee: «Cats and dogs are pets. Both need food and water. Cats are quiet, and dogs bark.» (pets = mascotas, bark = ladran). ¿Qué va en la parte común del diagrama?", ["La parte común lleva lo que ambos tienen.", "Ambos son mascotas y necesitan comida y agua.", "Quiet y bark son diferencias."], "Son mascotas y necesitan comida y agua"),
    ],
    [
        ("Llenar el esquema con detalles que el texto no dice.", "Se inventa información.", "Escribe «no se dice» si falta un dato."),
        ("Poner una diferencia en la parte común del diagrama.", "No se revisa qué comparten.", "En el centro va solo lo que ambos tienen igual."),
    ],
    [
        ("Lee: " + OTTO + " ¿Quién es el personaje principal? a) Otto b) el vecino", "a) Otto", "Otto es quien tiene el problema."),
        ("Lee: " + OTTO + " ¿Cuál es el problema para el mapa del cuento? a) Una rueda está desinflada b) Perdió su bicicleta", "a) Una rueda está desinflada", "Dice one wheel is flat."),
        ("Lee: " + OTTO + " ¿Cuál es la solución?", "Su vecino lo ayuda a inflar la rueda", "Dice his neighbour helps him inflate the wheel."),
    ],
    [
        ("Lee: " + OTTO + " En el casillero Setting (lugar), ¿qué escribes? a) no se dice un lugar exacto; solo se menciona el colegio b) en una playa", "a) no se dice un lugar exacto; solo se menciona el colegio", "El texto no describe el lugar donde ocurre."),
        ("Lee: " + SPORTS + " ¿Qué va en la parte común del diagrama? a) necesitan práctica y dan ejercicio b) se juega con pelota", "a) necesitan práctica y dan ejercicio", "Dice both sports need practice and give exercise."),
        ("Lee: " + SPORTS + " ¿Qué va solo en el círculo del fútbol? a) se juega en una cancha con pelota b) se mueve en el agua", "a) se juega en una cancha con pelota", "La pelota y la cancha son propias del fútbol."),
    ],
    [
        ("Lee: " + SPORTS + " ¿Qué va solo en el círculo de la natación?", "Se hace en una piscina", "Dice swimming is done in a pool."),
        ("Lee: " + SPORTS + " ¿Cuál de los dos deportes puede hacerse solo?", "La natación", "Dice swimming can be done alone."),
        ("Lee: " + SPORTS + " Si el diagrama tiene 2 diferencias del fútbol, 2 de la natación y 2 semejanzas, ¿cuántas anotaciones hay en total?", "6", "Se suman todas las anotaciones.", "2+2+2"),
    ],
    [
        ("Un compañero puso «Football is a team sport» en la parte común. ¿Qué error cometió?", "Es una diferencia: solo el fútbol es deporte de equipo", "La natación puede hacerse sola."),
        ("Una compañera completó Setting con «the sea» en el cuento de Otto. ¿Qué falta?", "Que el texto no dice el mar", "No hay evidencia en el texto."),
    ],
    [
        ("Haz un esquema con flechas de causa y efecto: «The wheel is flat → ___ → Otto rides happily.» ¿Qué va en el medio? a) his neighbour inflates the wheel b) Otto sleeps", "a) his neighbour inflates the wheel", "La ayuda conecta el problema con el final."),
        ("Un esquema tiene 4 casillas (personajes, lugar, problema, solución). Si el cuento de Otto llena todas excepto una porque falta el dato, ¿cuántas casillas llena con información del texto?", "3", "Una casilla queda con no se dice.", "4-1"),
    ],
    [("Tu profesor te pide un organizador para comparar dos cuentos. ¿Cuál organizador es más útil? a) un diagrama de Venn b) una lista de compras", "a) un diagrama de Venn", "Sirve para ver semejanzas y diferencias.")],
    [
        ("¿Qué es un mapa del cuento?", "Un esquema con personajes, lugar, problema y solución", "Ordena el cuento."),
        ("¿Qué va en la parte común de un diagrama de Venn?", "Lo que ambos tienen igual", "Both significa ambos."),
        ("¿Qué escribes si el texto no dice un dato?", "No se dice", "No se inventa."),
    ],
    task("Lee: «Two friends, Nora and Bruno, want to build a birdhouse. Nora has wood, and Bruno has paint. They work on Saturday morning in Nora's garden. The paint is not dry by the afternoon, so they wait one day. On Sunday, the birdhouse is ready, and a small bird visits it.» (birdhouse = casa de pájaros, wood = madera, paint = pintura, dry = seca, wait = esperan, ready = lista). Dibuja un mapa del cuento con cuatro casillas y completa cada una con palabras clave. Agrega una casilla «My opinion» con una frase en inglés.", "Personajes: Nora y Bruno. Lugar y tiempo: jardín de Nora, sábado y domingo. Problema: la pintura no está seca. Solución: esperan un día. My opinion: I like the story because it is about friends.", ["completa cuatro casillas con palabras clave", "no inventa datos", "agrega una opinión con because"], ["hoja con el mapa", "nota del adulto"], ["escribir oraciones muy largas", "confundir problema con solución"], "Reconoce las casillas bien completadas y revisa que cada palabra salga del texto."),
    "Haz un diagrama de Venn con dos animales que conoces y anota dos diferencias y una semejanza.",
    "Elige un cuento que hayas leído y completa su mapa del cuento con cuatro casillas.",
)

# ---------------------------------------------------------------- clase 2: ilustraciones
MARKET = "«On a rainy Sunday, the market is full of people with colourful umbrellas. A woman sells red apples and green pears. A boy holds a yellow umbrella and eats an apple. A dog sleeps under a table.» (market = feria, colourful = de colores, sells = vende, holds = sostiene, umbrella = paraguas, pears = peras)"

lesson(
    OA8, 2,
    "Los textos escritos en cada ejercicio, lápiz, una hoja y lápices de colores si hay.",
    "Aprenderé a dibujar o elegir una ilustración que represente lo que leí, y a escribir una leyenda corta en inglés. Sirve para demostrar comprensión y expresar lo que te gustó de un texto.",
    ["Sé nombrar colores y frutas en inglés.", "Conozco palabras como umbrella, dog y table."],
    [
        "Una ilustración (illustration) muestra un texto con un dibujo. Para ilustrar bien, primero lee y subraya los detalles: personas, objetos, colores, lugares, acciones. Luego decide qué dibujarás. Cada detalle del dibujo debe poder encontrarse en el texto. Si el texto dice yellow umbrella, tu paraguas debe ser amarillo.",
        "La leyenda (caption) es una frase corta debajo del dibujo que dice qué muestra. Una leyenda clara usa palabras del texto: «A boy with a yellow umbrella at the market». También puedes escribir una leyenda que exprese tu reacción: «I love this rainy day!». Una ilustración que respeta el texto demuestra que lo comprendiste.",
        "Antes de entregar tu dibujo, revisa con una lista: ¿incluí los personajes?, ¿los colores coinciden?, ¿está el lugar?, ¿mi leyenda dice lo mismo que el texto? Si algo falta, agrégalo. No hace falta dibujar con perfección; lo importante es la fidelidad al texto.",
    ],
    [("illustration", "ilustración"), ("caption", "leyenda: frase bajo un dibujo"), ("detail", "detalle"), ("colourful", "de colores"), ("umbrella", "paraguas"), ("market", "feria")],
    [
        ("Detalle que se debe dibujar", "Lee: «A girl with a green hat feeds two ducks near the lake.» (feeds = alimenta, ducks = patos). ¿Cuántos patos dibujas y de qué color es el sombrero?", ["Busco cantidades: two ducks.", "Busco color: green hat.", "Dibujo dos patos y un sombrero verde."], "Dos patos y un sombrero verde"),
        ("Elegir una leyenda", "Para esa ilustración, ¿qué leyenda calza mejor? a) A girl feeds two ducks near the lake. b) A boy eats pizza.", ["La leyenda debe decir lo mismo que el dibujo.", "La a) nombra a la niña, los patos y el lago.", "La b) no se relaciona."], "a) A girl feeds two ducks near the lake."),
    ],
    [
        ("Dibujar un detalle que el texto no menciona.", "Se agrega algo propio.", "Dibuja solo lo que está en el texto, aunque puedes decorar sin cambiar el sentido."),
        ("Cambiar un color.", "No se revisa el texto.", "Comprueba cada color con el texto antes de colorear."),
    ],
    [
        ("Lee: " + MARKET + " ¿De qué color es el paraguas del niño? a) amarillo b) rojo", "a) amarillo", "Dice a yellow umbrella."),
        ("Lee: " + MARKET + " ¿Dónde duerme el perro?", "Debajo de una mesa", "Dice a dog sleeps under a table."),
        ("Lee: " + MARKET + " ¿Qué día de la semana es? a) domingo b) lunes", "a) domingo", "Dice a rainy Sunday."),
    ],
    [
        ("Lee: " + MARKET + " ¿Qué frutas vende la mujer? a) manzanas rojas y peras verdes b) naranjas y plátanos", "a) manzanas rojas y peras verdes", "Dice red apples and green pears."),
        ("Lee: " + MARKET + " Una ilustración muestra un niño con paraguas amarillo, manzanas rojas y un perro dormido. ¿Qué falta?", "Las peras verdes", "El texto también dice green pears."),
        ("Lee: " + MARKET + " ¿Qué leyenda representa mejor la escena? a) A rainy day at the market b) A sunny day at the beach", "a) A rainy day at the market", "Es la que coincide con el texto."),
    ],
    [
        ("Lee: " + MARKET + " ¿Cuántos tipos de frutas distintos hay en la feria según el texto?", "2", "Son manzanas y peras."),
        ("Lee: " + MARKET + " ¿Qué hace el niño con la fruta?", "Se come una manzana", "Dice a boy holds a yellow umbrella and eats an apple."),
    ],
    [
        ("Un compañero dibujó un perro despierto jugando con una pelota. ¿Qué detalle del texto no respeta?", "Que el perro duerme", "Dice a dog sleeps under a table."),
        ("Otro compañero dibujó un sol brillante. ¿Qué dice el texto del clima?", "Que llueve", "Dice a rainy Sunday."),
    ],
    [
        ("Ordena los pasos para ilustrar un texto. A) Reviso mi dibujo con el texto. B) Subrayo los detalles. C) Dibujo y coloreo.", "B, C, A", "Primero se leen los detalles, luego se dibuja y al final se revisa."),
        ("Lee: " + MARKET + " ¿Cuántos animales se mencionan en el texto?", "1", "Solo aparece un perro."),
    ],
    [("Para el diario mural del colegio, debes ilustrar este texto: «A snowman has a red scarf and two black buttons.» (scarf = bufanda, buttons = botones). ¿Qué color es la bufanda?", "Roja", "Dice a red scarf.")],
    [
        ("¿Qué es una leyenda?", "Una frase corta bajo un dibujo", "Dice qué muestra."),
        ("¿Qué debe respetar una ilustración?", "Lo que dice el texto", "Es la evidencia de la comprensión."),
        ("¿Qué significa «colourful»?", "De colores", "Describe algo con muchos colores."),
    ],
    task("Lee: «At the school party, the room has blue balloons and a long table with three cakes. A girl in a purple dress dances with a boy in a green shirt. A teacher takes photos near the door.» (balloons = globos, cakes = tortas, dress = vestido, shirt = polera, takes photos = saca fotos). Dibuja la escena con todos los detalles del texto y escribe una leyenda en inglés. Agrega una frase de opinión con I like... because....", "Dibujo con globos azules, tres tortas, niña con vestido morado y niño con polera verde, profesora con cámara. Leyenda: A happy party at school. I like this party because there are blue balloons.", ["incluye todos los detalles del texto", "los colores y cantidades coinciden", "escribe leyenda y opinión"], ["hoja con dibujo y leyenda", "nota del adulto"], ["cambiar colores o cantidades", "agregar una opinión sin because"], "Reconoce los detalles bien dibujados y comprueba con el texto los colores y cantidades."),
    "Ilustra el texto del mercado con una leyenda en inglés y pide a una persona que compruebe tres detalles.",
    "Ilustra tu cuento favorito en tres dibujos con una leyenda corta en inglés.",
)

# ---------------------------------------------------------------- clase 3: dramatización
BUS = "«Ana and Leo are at a bus stop. Ana is worried because the bus is late. Leo says: Don't worry, the bus is coming. Then the bus arrives, and they smile.» (bus stop = paradero, worried = preocupada, late = atrasado, don't worry = no te preocupes, arrives = llega)"
SHOP = "«In a bakery, a customer asks for two rolls. The seller says they cost one thousand pesos. The customer pays with a two-thousand-peso note and receives one thousand pesos back.» (bakery = panadería, customer = cliente, rolls = marraquetas, seller = vendedor, pays = paga, note = billete, receives = recibe, back = de vuelto)"

lesson(
    OA8, 3,
    "Los textos escritos en cada ejercicio, lápiz y una hoja; opcionalmente una persona de tu casa para representar.",
    "Aprenderé a transformar un texto en una dramatización con turnos, tono de voz y gestos. Sirve para demostrar comprensión y expresar sentimientos con el cuerpo.",
    ["Sé que en un diálogo se habla por turnos.", "Conozco frases como Don't worry y Thank you."],
    [
        "Una dramatización (role play) representa un texto con voz y cuerpo. Para prepararla, escribe un guion (script): el nombre del personaje, entre paréntesis cómo habla o qué hace (la acotación, stage direction) y su frase. Por ejemplo: ANA (worried, looking at her watch): «The bus is late!». LEO (calm, smiling): «Don't worry, the bus is coming.»",
        "El tono y el gesto deben calzar con el sentimiento del personaje. Si Ana está preocupada, habla más rápido y mira el reloj. Si Leo está tranquilo, habla despacio y sonríe. Un buen guion indica quién habla, qué dice y cómo lo dice. Cada turno debe estar en el texto original o ser una idea coherente con él.",
        "Cuando representes, mira a la persona con quien hablas, habla con voz clara y haz pausas. No necesitas memorizar todo: puedes mirar el guion al comienzo. Después, comenta con tu compañero: ¿se entendió quién estaba preocupado? ¿qué gesto ayudó? Así conviertes la lectura en una experiencia que te permite expresar lo que sentiste.",
    ],
    [("role play", "dramatización"), ("script", "guion"), ("stage direction", "acotación: cómo hablar o actuar"), ("character", "personaje"), ("tone", "tono de voz"), ("gesture", "gesto")],
    [
        ("Leer un guion", "Lee: «PEDRO (angry): I lost my keys! MARTA (calm): Let's look in your bag.» (angry = enojado, calm = tranquila, lost = perdí, keys = llaves). ¿Quién está enojado y quién está tranquila?", ["Leo las acotaciones entre paréntesis.", "Pedro: angry. Marta: calm.", "Reúno ambas."], "Pedro está enojado y Marta tranquila"),
        ("Elegir una acotación", "La frase es «I won the race!» (won = gané, race = carrera). ¿Qué acotación corresponde: (jumping with joy) o (crying sadly)?", ["Ganar una carrera provoca alegría.", "Jumping with joy muestra alegría.", "Crying sadly no calza."], "(jumping with joy)"),
    ],
    [
        ("Representar una frase alegre con voz triste.", "No se cuida el tono.", "Revisa la acotación y usa el tono indicado."),
        ("Escribir el guion sin indicar quién habla.", "Se pierde el orden de turnos.", "Escribe el nombre del personaje antes de cada frase."),
    ],
    [
        ("Lee: " + BUS + " ¿Quién está preocupada? a) Ana b) Leo", "a) Ana", "Dice Ana is worried."),
        ("Lee: " + BUS + " ¿Por qué está preocupada Ana?", "Porque el bus está atrasado", "Dice because the bus is late."),
        ("Lee: " + BUS + " ¿Qué le dice Leo? a) Don't worry b) Goodbye", "a) Don't worry", "Dice Don't worry, the bus is coming."),
    ],
    [
        ("Lee: " + BUS + " ¿Qué acotación pondrías a Ana en su primera frase? a) (worried, looking at her watch) b) (laughing loudly)", "a) (worried, looking at her watch)", "Coincide con su estado de ánimo."),
        ("Lee: " + BUS + " ¿Qué acotación pondrías a Leo? a) (calm, smiling) b) (shouting)", "a) (calm, smiling)", "Leo tranquiliza a Ana."),
        ("Lee: " + BUS + " ¿Cuántos personajes tiene la dramatización?", "2", "Son Ana y Leo."),
    ],
    [
        ("Lee: " + SHOP + " ¿Cuántos personajes necesitas para dramatizarlo?", "2", "El cliente y el vendedor."),
        ("Lee: " + SHOP + " ¿Cuánto cuestan las dos marraquetas?", "1.000 pesos", "Dice one thousand pesos."),
        arith("Lee: " + SHOP + " ¿Cuánto vuelto recibe el cliente si paga con un billete de 2.000 pesos?", "2000-1000", "Se resta el precio al billete."),
    ],
    [
        ("Lee: " + SHOP + " ¿Qué acotación calza con la frase «Thank you!» del cliente al recibir el vuelto? a) (smiling) b) (angry)", "a) (smiling)", "Es una frase de agradecimiento."),
        ("Lee: " + BUS + " Un compañero dice que Leo está enojado. ¿Qué tono muestra el texto?", "Tranquilo", "Leo dice Don't worry."),
    ],
    [
        ("Ordena los turnos del guion del paradero. A) LEO: Don't worry. B) ANA: The bus is late! C) Both smile when the bus arrives.", "B, A, C", "Primero el problema, luego la calma y después el final."),
        ("Si tu guion del paradero tiene 3 turnos de Ana y 2 de Leo, ¿cuántos turnos tiene en total?", "5", "Se suman los turnos de ambos.", "3+2"),
    ],
    [("En el acto del colegio, representas a un guardia que dice: «Please walk, don't run!» (walk = camina, run = corre). ¿Qué tono y gesto calzan mejor? a) voz firme y mano levantada b) voz suave y dormido", "a) voz firme y mano levantada", "Es una indicación de cuidado.")],
    [
        ("¿Qué es una acotación?", "La indicación de cómo hablar o actuar", "Va entre paréntesis."),
        ("¿Qué debe tener un guion antes de cada frase?", "El nombre del personaje", "Muestra quién habla."),
        ("¿Qué tono usas para una frase de enojo?", "Voz fuerte y firme", "Debe coincidir con el sentimiento."),
    ],
    task("Lee: «Two friends, Tamara and Gabo, are at a park. Tamara cannot find her ball. She is sad. Gabo helps her look. They find the ball under a bench. Tamara is very happy and says thank you.» (park = parque, bench = banca, look = buscar). Escribe un guion de cuatro turnos con el nombre del personaje, una acotación y una frase en inglés. Después represéntalo ante una persona de tu casa.", "TAMARA (sad): I can't find my ball! GABO (kind): Let's look together. GABO (pointing): It's under the bench! TAMARA (happy): Thank you, Gabo!", ["escribe cuatro turnos", "agrega acotaciones coherentes", "las frases coinciden con el texto"], ["hoja con el guion", "nota de quien presenció"], ["acotaciones que no calzan", "olvidar el nombre del personaje"], "Reconoce el guion completo y practica con la persona el tono de cada acotación."),
    "Representa con una persona de tu casa el diálogo del paradero, cambiando el sentimiento de Ana a happy.",
    "Escribe un guion de tres turnos con la escena de una panadería usando Thank you y How much?",
)

# ---------------------------------------------------------------- clase 4: párrafos y resúmenes breves
SWIM = "«My favourite sport is swimming. First, it is relaxing. Also, it is good exercise. For example, I swim twice a week. In conclusion, swimming makes me happy.» (favourite = favorito, relaxing = relajante, exercise = ejercicio, twice = dos veces, conclusion = conclusión)"

lesson(
    OA8, 4,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un párrafo o un resumen breve sobre un texto, con una idea principal, razones, un ejemplo y una opinión, usando conectores. Sirve para expresar lo que pienso de una lectura.",
    ["Sé escribir oraciones con because.", "Conozco first, then y finally."],
    [
        "Un párrafo (paragraph) está formado por varias oraciones que hablan de una misma idea. La primera, la oración temática (topic sentence), dice la idea principal: «My favourite sport is swimming». Las siguientes dan razones y ejemplos. La última cierra con una conclusión (conclusion), a veces con tu opinión.",
        "Los conectores (connectors) unen las ideas. First (primero), Also (además) y Then (luego) ordenan. Because (porque) da una razón. For example (por ejemplo) introduce un ejemplo. But (pero) muestra un contraste. In conclusion (en conclusión) cierra. Con ellos, el párrafo se lee fluido y claro, como una cadena de ideas.",
        "Un resumen breve (short summary) cuenta lo que dice un texto en pocas oraciones con tus palabras. Un párrafo de opinión da tu postura. No los confundas: el resumen no incluye I think; el párrafo de opinión sí. Antes de entregar, revisa que cada oración se conecte con la idea principal y que usaste al menos dos conectores.",
    ],
    [("paragraph", "párrafo"), ("topic sentence", "oración temática"), ("connector", "conector"), ("for example", "por ejemplo"), ("in conclusion", "en conclusión"), ("short summary", "resumen breve")],
    [
        ("Reconocer la oración temática", "Lee: «My city has many parks. There is a big park near my school. Also, there is a small park near the market. In conclusion, I love my city.» (city = ciudad, parks = parques). ¿Cuál es la oración temática?", ["La primera oración presenta la idea principal.", "Habla de que la ciudad tiene muchos parques.", "Las demás dan ejemplos y cierran."], "My city has many parks."),
        ("Elegir un conector", "Completa: «I like my city. ___, there are many parks.» Opciones: For example, But.", ["Falta un ejemplo o una razón.", "For example introduce un ejemplo.", "But marca contraste."], "For example"),
    ],
    [
        ("Mezclar un resumen con una opinión.", "No se separa lo que dice el texto de lo que pienso.", "En el resumen cuenta el texto; en el párrafo de opinión usa I think."),
        ("Escribir oraciones sueltas sin conectores.", "Falta unión entre las ideas.", "Agrega First, Also, For example o In conclusion."),
    ],
    [
        ("Lee: " + SWIM + " ¿Cuál es la oración temática? a) My favourite sport is swimming. b) In conclusion, swimming makes me happy.", "a) My favourite sport is swimming.", "Presenta la idea principal."),
        ("Lee: " + SWIM + " ¿Qué conector introduce un ejemplo?", "For example", "For example significa por ejemplo."),
        ("Lee: " + SWIM + " ¿Qué conector cierra el párrafo?", "In conclusion", "In conclusion significa en conclusión."),
    ],
    [
        ("Lee: " + SWIM + " ¿Cuántas veces nada el autor a la semana?", "Dos veces", "Dice twice a week."),
        ("Lee: " + SWIM + " ¿Qué razón da primero para elegir la natación? a) es relajante b) es cara", "a) es relajante", "Dice First, it is relaxing."),
        ("Lee: " + SWIM + " ¿Cuántas oraciones tiene el párrafo?", "5", "Se cuentan cinco puntos finales."),
    ],
    [
        ("Completa con un conector: «I like pizza ___ it is delicious.» Opciones: because, but.", "because", "Da una razón."),
        ("Completa con un conector: «Football is fun, ___ swimming is more relaxing.» Opciones: but, because.", "but", "Marca el contraste."),
        ("Completa: «There are two reasons. ___, it is cheap. Also, it is fast.» Opciones: First, Finally.", "First", "Es el primer conector de la secuencia."),
    ],
    [
        ("Ordena el párrafo. A) Also, it helps me sleep well. B) I like running. C) First, it gives me energy.", "B, C, A", "Primero la idea principal y luego las razones."),
        ("Un compañero escribió: «I think the story is boring» dentro de un resumen. ¿Qué error cometió?", "Mezcló una opinión con un resumen", "El resumen solo cuenta el texto."),
    ],
    [
        ("Lee: «Maya has a problem. Her dog is lost. She puts posters in the park. A boy calls her.» Escoge el mejor resumen en una oración. a) Maya looks for her lost dog with posters and a boy calls her. b) I think Maya is funny.", "a) Maya looks for her lost dog with posters and a boy calls her.", "Cuenta lo que ocurre sin opinión."),
        ("Cuenta los conectores del párrafo: «First, I wake up. Then I eat. Finally, I go to school.»", "3", "First, Then y Finally."),
    ],
    [("Tu profesor pide un párrafo sobre tu mascota. ¿Cuál es una buena oración temática? a) I have a cat named Nube. b) Yesterday it rained.", "a) I have a cat named Nube.", "Presenta el tema del párrafo.")],
    [
        ("¿Qué es la oración temática?", "La que dice la idea principal", "Abre el párrafo."),
        ("¿Para qué sirve for example?", "Para dar un ejemplo", "Es un conector."),
        ("¿Incluye un resumen tu opinión?", "No", "Solo cuenta el texto."),
    ],
    task("Lee: «Animal shelters take care of dogs and cats without homes. Volunteers walk the dogs and clean the cages. People can adopt a pet for free or for a small payment. Shelters also teach children to respect animals.» (shelters = refugios, volunteers = voluntarios, cages = jaulas, adopt = adoptar, payment = pago, respect = respetar). Escribe un párrafo de opinión de cinco oraciones: una oración temática, dos razones con First y Also, un ejemplo con For example y una conclusión con In conclusion.", "I think animal shelters are important. First, they take care of animals without homes. Also, they teach children to respect animals. For example, volunteers walk the dogs. In conclusion, shelters help animals and people.", ["escribe una oración temática", "usa al menos tres conectores", "cierra con una conclusión"], ["párrafo escrito", "nota del adulto"], ["no usar conectores", "copiar el texto original"], "Reconoce el párrafo ordenado y revisa con la persona que cada oración se conecte con la idea principal."),
    "Relee el párrafo de la natación y subraya cada conector.",
    "Escribe un resumen de tres oraciones de un cuento que leíste y un párrafo de opinión sobre él.",
)

# ---------------------------------------------------------------- clase 5: tiras cómicas y exposición oral breve
PIANO = "«Lucas wants to play the piano at the school show, but he is afraid. His friend Mia practises with him every afternoon. On the day of the show, Lucas plays well and everyone claps. He feels proud and thanks Mia.» (piano, show = presentación, afraid = con miedo, practises = practica, claps = aplauden, proud = orgulloso, thanks = agradece)"

lesson(
    OA8, 5,
    "Los textos escritos en cada ejercicio, lápiz, una hoja y reglas o líneas dibujadas a mano.",
    "Aprenderé a transformar un texto en una tira cómica y a presentar oralmente mi opinión sobre él con una estructura clara. Sirve para expresar preferencias, sentimientos y opiniones sobre lo que leíste.",
    ["Sé que una tira cómica tiene viñetas y globos de diálogo.", "Conozco I like y I think."],
    [
        "Para convertir un texto en tira cómica (comic strip), divide la historia en cuatro partes y dibuja una viñeta para cada una. Elige las frases más importantes para los globos de diálogo (speech bubbles), con pocas palabras. Pon un dibujo, un globo y, si hace falta, una palabra de sonido o de sentimiento, como Wow! u Oh no!",
        "Para presentar tu opinión oralmente, sigue una estructura: 1. Saluda y di el título. 2. Cuenta el tema en una oración. 3. Di tu parte favorita con My favourite part is... because... 4. Expresa un sentimiento con I felt... 5. Cierra con Thank you. Practica frente a un espejo o a una persona de tu casa y habla con voz clara.",
        "Una buena presentación usa tus dibujos como apoyo visual. Muéstralos mientras hablas y señala la viñeta de la que hablas. No leas el papel: usa palabras clave. Si olvidas algo, mira tu tira cómica. Así combinas texto, imagen y voz para expresar lo que pensaste y sentiste al leer.",
    ],
    [("comic strip / panel", "tira cómica / viñeta"), ("speech bubble", "globo de diálogo"), ("My favourite part is...", "mi parte favorita es..."), ("I felt...", "yo sentí..."), ("presentation", "presentación"), ("visual support", "apoyo visual")],
    [
        ("Dividir en viñetas", "Lee: «Dani finds a seed. He plants it. It grows into a flower. He gives the flower to his teacher.» (seed = semilla, grows = crece, gives = entrega). ¿Cuántas viñetas necesitas para contar un hecho en cada una?", ["Cuento los hechos: encuentra, planta, crece, entrega.", "Son cuatro hechos.", "Necesito cuatro viñetas."], "4 viñetas"),
        ("Estructura de una presentación", "¿Qué frase usas para decir tu parte favorita: «My favourite part is...» o «Goodbye»?", ["Busco la frase para parte favorita.", "My favourite part is... la expresa.", "Goodbye es una despedida."], "My favourite part is..."),
    ],
    [
        ("Escribir en cada globo una oración muy larga.", "No cabe en el globo y se pierde el efecto.", "Usa frases cortas."),
        ("Leer el papel durante toda la presentación.", "Se pierde el contacto con la audiencia.", "Usa palabras clave y mira tu dibujo."),
    ],
    [
        ("Lee: " + PIANO + " ¿Cuántos hechos importantes cuentas en una tira de cuatro viñetas? a) cuatro b) diez", "a) cuatro", "Cada viñeta representa uno."),
        ("Lee: " + PIANO + " ¿Qué quiere hacer Lucas? a) tocar el piano en la presentación b) ganar una carrera", "a) tocar el piano en la presentación", "Dice Lucas wants to play the piano at the school show."),
        ("Lee: " + PIANO + " ¿Quién practica con Lucas?", "Su amiga Mia", "Dice his friend Mia practises with him."),
    ],
    [
        ("Lee: " + PIANO + " Viñeta 1: Lucas mira un piano con cara de miedo. ¿Qué globo calza? a) I'm afraid! b) I'm hungry!", "a) I'm afraid!", "Dice he is afraid."),
        ("Lee: " + PIANO + " Viñeta 3: Lucas toca y la gente aplaude. ¿Qué palabra de sonido calza? a) Clap, clap! b) Zzz!", "a) Clap, clap!", "Dice everyone claps."),
        ("Lee: " + PIANO + " Viñeta 4: Lucas sonríe y mira a Mia. ¿Qué globo calza? a) Thank you, Mia! b) I lost my ball!", "a) Thank you, Mia!", "Dice he thanks Mia."),
    ],
    [
        ("Ordena las viñetas del texto del piano. A) Lucas plays and everyone claps. B) Lucas is afraid. C) Mia practises with him.", "B, C, A", "Primero el miedo, luego la práctica y finalmente la presentación."),
        ("Ordena una presentación oral. A) Thank you. B) My favourite part is the show because everyone claps. C) Hello, my story is about Lucas.", "C, B, A", "Se saluda, se da la opinión y se cierra."),
        ("Completa con una razón: «My favourite part is when Mia helps Lucas ___ she is a good friend.» Opciones: because, but.", "because", "Da la razón de la preferencia."),
    ],
    [
        ("Un compañero dice en su presentación: «I felt proud of Lucas.» ¿Qué parte de la estructura es? a) un sentimiento b) un saludo", "a) un sentimiento", "I felt expresa lo que sintió."),
        ("Una compañera lee su papel completo y no mira a la audiencia. ¿Qué debería hacer? a) usar palabras clave y mirar a las personas b) hablar más bajo", "a) usar palabras clave y mirar a las personas", "Así conecta con la audiencia."),
    ],
    [
        ("Lee: " + PIANO + " Si cada viñeta tiene un globo de diálogo y una de ellas tiene dos globos, ¿cuántos globos hay en la tira?", "5", "Cuatro viñetas con un globo más uno extra.", "4+1"),
        ("Preparas una presentación de 2 minutos con 4 partes iguales. ¿Cuántos segundos dura cada parte?", "30", "Dos minutos son 120 segundos divididos en cuatro partes iguales.", "120//4"),
    ],
    [("En la feria del libro del colegio debes presentar tu opinión sobre «The Little Seed». Para apoyarte, ¿qué usas? a) un dibujo de la semilla creciendo b) un papel largo con todo el poema", "a) un dibujo de la semilla creciendo", "El apoyo visual ayuda a explicar.")],
    [
        ("¿Para qué sirven los globos de diálogo?", "Para mostrar lo que dicen los personajes", "Contienen sus palabras."),
        ("¿Cómo se dice «mi parte favorita es»?", "My favourite part is", "Frase para opinar."),
        ("¿Qué apoyo visual usas al presentar?", "Una tira cómica o un dibujo", "Ayuda a explicar."),
    ],
    task("Lee: «Gaby has a small fish named Bubbles. One morning, Bubbles is not in the bowl! Gaby looks under the table and behind the sofa. Then she hears a splash: Bubbles is in the kitchen sink. Gaby puts him back in the bowl and smiles.» (fish = pez, bowl = pecera, splash = chapoteo, sink = lavaplatos). Dibuja una tira cómica de cuatro viñetas con un globo corto en cada una. Luego prepara una presentación de cuatro frases: saludo, tema, My favourite part is... because... y Thank you.", "Viñetas: Gaby ve la pecera vacía; busca; oye un ruido; lo encuentra. Presentación: Hello! My story is about a fish. My favourite part is the splash because it is funny. Thank you!", ["dibuja cuatro viñetas en orden", "escribe globos cortos", "presenta con la estructura indicada"], ["hoja con tira cómica y frases", "nota del adulto"], ["globos muy largos", "olvidar el cierre"], "Reconoce el orden de las viñetas y practica la presentación con la persona en voz alta."),
    "Presenta ante una persona de tu casa tu tira cómica del pez y pide que te diga qué parte entendió mejor.",
    "Crea una tira cómica de cuatro viñetas sobre un día en el colegio, con un globo en inglés en cada una.",
)

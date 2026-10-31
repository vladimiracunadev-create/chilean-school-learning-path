"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 03 (estrategias antes, durante y después de escuchar).

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Las acciones del hablante (gestos, imágenes) van entre corchetes. Los textos son originales y llevan pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import ADULT, lesson

OA3 = "EN07 OA 03"

# ---------------------------------------------------------------- clase 1: propósito y predicción
VET = "«Welcome to the Rojas Vet Clinic. Our opening hours are from nine to six, Monday to Saturday. For emergencies, call the number on the door. A check-up for a dog costs fifteen thousand pesos.» (vet = veterinaria, opening hours = horario de atención, emergencies = urgencias, check-up = control, costs = cuesta)"
WEATHER = "«Weather report for tomorrow. It will be cloudy in the morning and rainy in the afternoon. The temperature will be twelve degrees. Please take an umbrella.» (cloudy = nublado, rainy = lluvioso, temperature = temperatura, degrees = grados, umbrella = paraguas)"
MARKET = "«Welcome to Fresh Market. Today apples are on sale: two thousand pesos per kilo. Tomatoes cost three thousand five hundred pesos per kilo. The market closes at six o'clock.» (on sale = en oferta, per kilo = por kilo, closes = cierra)"

lesson(
    OA3, 1,
    "Los avisos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a usar dos estrategias antes de escuchar: fijar un propósito (para qué escucho) y hacer predicciones con el título y el contexto. Sirve para escuchar con atención un aviso o una charla y encontrar el dato que necesito.",
    ["Sé que las preguntas what time y how much piden una hora y un precio.", "Conozco palabras como dog, rain y apple."],
    [
        "Escuchar en inglés es más fácil si te preparas antes. La primera estrategia es escuchar con un propósito (listening purpose): decides qué dato necesitas. Si quieres saber a qué hora abre un lugar, tu propósito es encontrar una hora; si quieres comprar fruta, buscas un precio. Con un propósito, tu atención se enfoca en pocas palabras clave y no intentas entenderlo todo.",
        "La segunda estrategia es hacer predicciones (predictions): pensar qué palabras y datos vas a oír, usando el título (title), la imagen o el contexto (context). Si el título es «At the Vet», esperas palabras como dog, sick, medicine y check-up. Una predicción es una idea probable, no una certeza: después, al escuchar, se confirma o se corrige.",
        "El orden de la estrategia es: primero fijas el propósito, luego predices y por último escuchas y comprueba. Escribe tu propósito en una frase corta, por ejemplo: «I want to know the price» (quiero saber el precio). Mientras escuchas, anota solo el dato que buscas: una hora, un precio o un lugar.",
    ],
    [("purpose", "propósito: para qué escucho"), ("prediction", "predicción: idea de lo que voy a oír"), ("title", "título"), ("context", "contexto: situación"), ("key word", "palabra clave"), ("I want to know…", "Quiero saber…")],
    [
        ("Predecir con el título", "El adulto va a leer un aviso con el título «At the Airport». ¿Qué palabras puedes predecir? a) flight, gate, suitcase b) goal, referee, whistle (flight = vuelo, gate = puerta de embarque, suitcase = maleta, referee = árbitro, whistle = silbato)", ["Pienso en un aeropuerto: hay vuelos y maletas.", "La opción a nombra cosas de un aeropuerto.", "La opción b habla de fútbol."], "a) flight, gate, suitcase"),
        ("Fijar un propósito", "Escucharás: «The movie starts at seven thirty. The ticket costs four thousand pesos.» (movie = película). Tu propósito es saber la hora. ¿Qué dato anotas?", ["Mi propósito pide una hora.", "Busco un número con thirty o o'clock.", "La hora es seven thirty."], "Siete y media (7:30)"),
    ],
    [
        ("Pensar que una predicción siempre se cumple.", "Se confunde una idea probable con un dato cierto.", "Compara la predicción con lo que realmente oyes y corrígela."),
        ("Escuchar sin propósito y tratar de anotar todo.", "Se pierde el dato que importa.", "Fija una pregunta antes de escuchar y anota solo esa respuesta."),
    ],
    [
        ("El adulto va a leer un aviso con el título «At the Vet». ¿Qué palabras puedes predecir? a) dog, medicine, check-up b) teacher, notebook, homework", "a) dog, medicine, check-up", "Una clínica veterinaria se relaciona con animales y salud."),
        ("Quieres saber a qué hora abre una clínica. ¿Qué dato necesitas escuchar? a) una hora b) un precio", "a) una hora", "El propósito pide a qué hora, que se responde con una hora."),
        ("El título es «Weather Report». ¿Qué palabras esperas oír? a) rainy, cloudy, temperature b) passport, ticket, suitcase", "a) rainy, cloudy, temperature", "Un informe del tiempo habla de clima."),
    ],
    [
        (ADULT + VET + " ¿Qué días y a qué hora atiende la clínica?", "De lunes a sábado, de nueve a seis", "Dice from nine to six, Monday to Saturday."),
        (ADULT + VET + " ¿Cuánto cuesta el control de un perro?", "$15.000", "Dice fifteen thousand pesos."),
        (ADULT + WEATHER + " ¿Cuál será la temperatura?", "12 grados", "Dice twelve degrees."),
    ],
    [
        ("Tu propósito es saber cuánto cuestan las manzanas. " + MARKET + " Si compras 3 kilos, ¿cuánto pagas, en pesos?", "$6.000", "Cada kilo cuesta dos mil pesos.", "3*2000"),
        ("Tu propósito es saber el precio de los tomates. " + MARKET + " Si compras 2 kilos, ¿cuánto pagas, en pesos?", "$7.000", "Cada kilo cuesta tres mil quinientos pesos.", "2*3500"),
        (ADULT + MARKET + " Quieres comprar a las cinco y media. ¿Todavía está abierto el mercado? Responde sí o no.", "Sí", "El mercado cierra a las seis."),
    ],
    [
        (ADULT + MARKET + " Ana busca ofertas de fruta y Bruno busca la hora de cierre. ¿Qué dato necesita Ana y Bruno no? a) las manzanas están en oferta b) cierra a las seis", "a) las manzanas están en oferta", "Ana busca un descuento; Bruno, una hora."),
        ("Un compañero predijo que el aviso de la clínica veterinaria hablará de pizza. ¿Por qué es poco probable?", "Porque el título y el contexto no se relacionan con comida", "Una clínica veterinaria trata de animales y salud."),
    ],
    [
        ("Ordena la estrategia para escuchar. A) Escuchar y comprobar. B) Fijar un propósito. C) Predecir con el título.", "B, C, A", "Primero el propósito, luego la predicción y al final se escucha."),
        (ADULT + VET + " Si llevas a 2 perros a control, ¿cuánto pagas en total, en pesos?", "$30.000", "El control de un perro cuesta quince mil pesos.", "2*15000"),
    ],
    [(ADULT + "«Attention, passengers. The train to the south leaves from platform three at eight twenty. Please do not cross the yellow line.» (passengers = pasajeros, platform = andén, leaves = sale, cross = cruzar, line = línea). Tu propósito es saber el andén. ¿Cuál es? a) el tres b) el ocho", "a) el tres", "Dice platform three.")],
    [
        ("¿Para qué sirve fijar un propósito?", "Para saber qué dato buscar", "Enfoca la atención."),
        ("Antes de escuchar en inglés, ¿qué es una prediction?", "Una idea probable de lo que se va a oír", "Se confirma o se corrige al escuchar."),
        ("¿Qué frase sirve para decir tu propósito en inglés?", "I want to know…", "Expresa qué quieres averiguar."),
    ],
    task("Un adulto lee dos veces: «Good morning. This is the school radio. Tomorrow the school bus will leave at seven fifteen, not at seven thirty. The reason is a road repair near the bridge.» (leave = salir, repair = reparación, bridge = puente). Antes de escuchar, escribe tu propósito y dos palabras que esperas oír con el título «School Bus News». Después escribe qué cambió, a qué hora y por qué.", "Propósito: saber la hora del bus. Palabras: bus, time. Cambio: sale a las 7:15 en lugar de 7:30 por una reparación del camino.", ["escribe un propósito claro antes de escuchar", "anota dos palabras de predicción relacionadas con el título", "responde qué, cuándo y por qué con datos del texto"], ["hoja con propósito y respuestas", "nota del adulto"], ["anotar 7:30 como hora nueva", "escribir predicciones sin relación con el título"], "Reconoce lo que acertó y revisa con la persona qué dato pedía su propósito."),
    "Pide a un adulto que lea el informe del tiempo y subraya solo los datos que responden a tu propósito.",
    "Escribe un título de aviso y tres palabras que predices para él.",
)

# ---------------------------------------------------------------- clase 2: conocimientos previos y palabras clave
VOLCANO = "«A volcano is a mountain with an opening at the top. Under the ground, there is hot melted rock called magma. When the pressure grows, the magma comes out as lava. Ash and gas also rise into the air. Chile has many active volcanoes.» (opening = abertura, melted = derretida, rock = roca, pressure = presión, comes out = sale, ash = ceniza, gas = gas, active = activos)"
TIRE = "«If your bike has a flat tire, follow these steps. First, remove the wheel. Second, find the hole in the inner tube. Third, put a patch on the hole and wait five minutes. Finally, put the wheel back on the bike.» (flat tire = neumático desinflado, remove = sacar, inner tube = cámara, patch = parche, wait = esperar)"
TICKET = "«To buy a train ticket, go to the machine. Choose your city. Select adult or student. Pay with coins or a card. Take your ticket and your change.» (machine = máquina, select = seleccionar, coins = monedas, card = tarjeta, change = vuelto)"

lesson(
    OA3, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a usar mis conocimientos previos y a enfocarme en palabras clave para entender un texto oral. Sirve para entender explicaciones y procedimientos aunque no conozca todas las palabras.",
    ["Sé fijar un propósito antes de escuchar.", "Conozco palabras como mountain, bike y ticket."],
    [
        "Los conocimientos previos (prior knowledge) son lo que ya sabes sobre un tema, aunque no lo sepas en inglés. Si sabes que un volcán echa lava caliente, entenderás más rápido un texto sobre volcanes. Antes de escuchar, piensa: ¿qué sé de este tema? Esa información te ayuda a adivinar palabras nuevas con el contexto.",
        "Las palabras clave (key words) son las que sostienen el significado: sustantivos, verbos de acción y números. En «Pay with coins or a card», las palabras clave son pay, coins y card. Las palabras pequeñas, como the o a, se oyen menos y no hace falta anotarlas. Enfoca tu atención en las palabras que se repiten y en las que se pronuncian con más fuerza.",
        "Si aparece una palabra desconocida, no te detengas. Usa tus conocimientos previos y las palabras vecinas. En «Put a patch on the hole», si sabes cómo se arregla un neumático, entiendes que patch es un parche. Para comprobar tu idea, ve si encaja con el resto del procedimiento.",
    ],
    [("prior knowledge", "conocimientos previos"), ("key words", "palabras clave"), ("context", "contexto: palabras vecinas"), ("guess", "adivinar un significado"), ("repeat", "repetirse"), ("stress", "énfasis al pronunciar")],
    [
        ("Usar conocimientos previos", ADULT + "«A bee lives in a hive. It makes honey from the nectar of flowers.» (bee = abeja, hive = colmena, nectar = néctar). No conoces nectar. ¿Qué te ayuda a adivinar su significado?", ["Sé que las abejas visitan flores.", "El texto dice flowers justo después de nectar.", "Concluyo que nectar es un líquido de las flores."], "Que las abejas hacen miel con algo de las flores"),
        ("Palabras clave", "En «Select adult or student» escucha las palabras clave. ¿Cuáles son?", ["Los verbos y sustantivos principales son select, adult y student.", "Or conecta las opciones.", "Las palabras pequeñas son menos importantes."], "select, adult, student"),
    ],
    [
        ("Intentar entender todas las palabras y quedarse atrás.", "Se pierde el hilo del texto.", "Anota solo las palabras clave y sigue escuchando."),
        ("Responder usando lo que uno sabe aunque el texto diga otra cosa.", "Se mezcla el conocimiento previo con el texto.", "Primero comprueba que tu idea encaje con lo que dice el texto."),
    ],
    [
        ("Sabes que las erupciones sueltan lava. ¿Qué palabra de VOLCANO esperarías oír? a) lava b) iceberg", "a) lava", "Con tu conocimiento previo de volcanes, lava es esperable."),
        ("¿Qué palabras son clave en «Remove the wheel»? a) remove y wheel b) the", "a) remove y wheel", "El verbo y el sustantivo sostienen el significado."),
        ("Sabes que se paga con dinero. En TICKET, ¿qué palabras indican con qué se paga? a) coins y card b) city y student", "a) coins y card", "Pay with coins or a card nombra las dos formas de pago."),
    ],
    [
        (ADULT + VOLCANO + " ¿Cómo se llama la roca caliente que está bajo la tierra?", "Magma", "Dice hot melted rock called magma."),
        (ADULT + TIRE + " ¿Cuánto tiempo se espera después de poner el parche?", "Cinco minutos", "Dice wait five minutes."),
        (ADULT + TICKET + " ¿Qué se recibe al final?", "El boleto y el vuelto", "Dice take your ticket and your change."),
    ],
    [
        (ADULT + VOLCANO + " ¿Qué sale de la tierra cuando aumenta la presión? a) lava b) agua helada", "a) lava", "Dice when the pressure grows, the magma comes out as lava."),
        (ADULT + TIRE + " ¿Qué se hace en el segundo paso? a) encontrar el agujero en la cámara b) poner el parche", "a) encontrar el agujero en la cámara", "Dice Second, find the hole in the inner tube."),
        (ADULT + TICKET + " ¿Qué se elige primero? a) la ciudad b) adulto o estudiante", "a) la ciudad", "Dice Choose your city antes de select."),
    ],
    [
        (ADULT + TIRE + " No conoces patch. Por el contexto (hole), ¿qué crees que es? a) algo para tapar el agujero b) una herramienta para inflar", "a) algo para tapar el agujero", "Se pone sobre el hoyo y se espera cinco minutos."),
        (ADULT + TIRE + " Si te saltas el segundo paso, ¿qué problema tendrías? a) no sabrías dónde poner el parche b) no tendrías rueda", "a) no sabrías dónde poner el parche", "Primero se encuentra el agujero y luego se pone el parche encima."),
    ],
    [
        ("Un boleto de estudiante cuesta $1.200 (dato de ejemplo). Pagas con un billete de $2.000 y la máquina entrega el vuelto (change). ¿Cuánto vuelto recibes, en pesos?", "$800", "Se resta el precio del boleto al billete.", "2000-1200"),
        (ADULT + TIRE + " ¿Cuántos pasos tiene el procedimiento? Cuenta los pasos marcados con first, second, third y finally.", "4", "Son first, second, third y finally."),
    ],
    [(ADULT + "«The astronaut wears a space suit because the moon has no air to breathe. She walks slowly because gravity is weaker there.» (astronaut = astronauta, space suit = traje espacial, air to breathe = aire para respirar, gravity = gravedad, weaker = más débil). Con tu conocimiento previo, ¿por qué usa traje espacial? a) porque en la luna no hay aire para respirar b) porque en la luna llueve mucho", "a) porque en la luna no hay aire para respirar", "El texto lo dice con because.")],
    [
        ("Al escuchar un texto en inglés, ¿qué es el prior knowledge?", "Lo que ya sabes sobre un tema", "Ayudan a entender textos nuevos."),
        ("¿Qué palabras conviene anotar?", "Las palabras clave", "Sostienen el significado."),
        ("¿Qué haces con una palabra desconocida?", "Usar el contexto y seguir escuchando", "Así no pierdes el hilo."),
    ],
    task("Un adulto lee dos veces: «To make a paper airplane: first, fold the paper in half. Second, open it and fold the top corners to the center. Third, fold the edges again. Finally, hold the plane and throw it gently.» (airplane = avión, fold = doblar, corners = esquinas, hold = sostener, throw = lanzar, gently = suavemente). Escribe tus conocimientos previos sobre aviones de papel y las cinco palabras clave del texto.", "Sé que los aviones de papel se doblan y vuelan al lanzarlos. Palabras clave: fold, paper, corners, plane y throw.", ["escribe un conocimiento previo coherente", "anota cinco palabras clave que sí están en el texto", "no copia oraciones completas"], ["hoja con respuestas", "nota del adulto"], ["anotar solo artículos o conectores", "anotar palabras que no aparecen"], "Reconoce lo que acertó y subraya con la persona verbos y sustantivos para elegir las palabras clave."),
    "Pide a un adulto que lea el texto del volcán y escribe tres cosas que ya sabías sobre volcanes.",
    "Escribe en español qué sabes de las abejas y qué palabras te ayudarían a entender un texto sobre ellas.",
)

# ---------------------------------------------------------------- clase 3: apoyos visuales y preguntas para clarificar
MAPTALK = "«[The speaker holds a map and points to a blue dot.] Look at this map. We are here. [She points to a green area.] The park is here. Do you see the river? [She draws a line with her finger.] The path goes along the river. [She holds up two fingers.] It takes two hours to walk.» (map = mapa, dot = punto, area = zona, river = río, path = sendero, along = a lo largo de, takes = demora)"
LABTALK = "«[The teacher shows a thermometer.] This is a thermometer. It measures temperature. [She points to the red line.] The red line shows the temperature. [She shakes her head.] Do not touch the glass. [She smiles.] Now, who can read it?» (thermometer = termómetro, measures = mide, line = línea, glass = vidrio, read = leer)"
COOKTALK = "«[The cook holds a lemon.] First, I cut the lemon into two halves. [He makes a squeezing gesture.] Then I squeeze the lemon into a bowl. [He shows a small cup.] I add this much sugar. [He puts his thumb up.] The lemonade is ready.» (cut = corto, halves = mitades, squeeze = exprimir, bowl = bol, cup = taza, sugar = azúcar, ready = lista)"

lesson(
    OA3, 3,
    "Los textos con gestos e imágenes escritos en cada ejercicio, que lee un adulto en voz alta mostrando los gestos entre corchetes; una hoja para tapar el guion y lápiz.",
    "Aprenderé a usar apoyos como imágenes y gestos del hablante, y a preguntar para clarificar o confirmar información. Sirve para entender a una persona que habla inglés cuando no entiendo todas las palabras.",
    ["Sé reconocer palabras clave.", "Conozco palabras como map, river y lemon."],
    [
        "Cuando alguien habla, no solo usa palabras: también mueve las manos, muestra imágenes, señala objetos y cambia la cara. Estos apoyos (supports) ayudan a entender. Si el hablante apunta a un punto azul y dice «We are here», entiendes que here es ese punto aunque no oigas todas las palabras. Un gesto de negación, como mover la cabeza, suele indicar «no», y un pulgar arriba indica que algo está bien.",
        "Si aun así no entiendes, puedes preguntar para clarificar (clarify). Algunas frases útiles son: «Could you repeat that, please?» (¿puede repetir?), «Could you speak more slowly?» (¿puede hablar más despacio?), «What does path mean?» (¿qué significa path?) y «Do you mean the blue dot?» (¿se refiere al punto azul?). La última sirve para confirmar (confirm) que entendiste bien.",
        "Una estrategia útil es combinar tres fuentes: lo que oyes, lo que ves y lo que sabes. Si las tres coinciden, tu comprensión es segura. Si no coinciden, haz una pregunta corta. Preguntar no es una falla: es una estrategia que usan también las personas que hablan bien inglés.",
    ],
    [("support", "apoyo: imagen o gesto"), ("gesture", "gesto"), ("clarify", "aclarar"), ("confirm", "confirmar"), ("Could you repeat that?", "¿Puede repetir eso?"), ("Do you mean…?", "¿Se refiere a…?")],
    [
        ("Gesto como apoyo", ADULT + "«[The speaker opens her arms very wide.] The fish was this big!» (fish = pez, big = grande). ¿Qué te dice el gesto?", ["El gesto muestra el tamaño del pez.", "Los brazos muy abiertos significan grande.", "Se confirma con la palabra big."], "Que el pez era muy grande"),
        ("Pregunta para confirmar", "El hablante dice: «Meet me at the station at five.» No estás seguro de si dijo five o fifteen. ¿Qué pregunta haces?", ["Quiero confirmar la hora exacta.", "Puedo preguntar con Do you mean…?", "Pregunto: Do you mean five o'clock?"], "Do you mean five o'clock?"),
    ],
    [
        ("Ignorar los gestos del hablante.", "Se pierde información que no está en las palabras.", "Observa qué señala o muestra y relaciónalo con lo que dice."),
        ("Quedarse callado cuando no se entiende.", "Se pierde el mensaje.", "Pide con calma que repita o aclare."),
    ],
    [
        (ADULT + MAPTALK + " ¿Qué significa el punto azul? a) el lugar donde están b) el parque", "a) el lugar donde están", "Dice We are here mientras señala el punto azul."),
        (ADULT + LABTALK + " ¿Qué muestra la línea roja? a) la temperatura b) la hora", "a) la temperatura", "Dice the red line shows the temperature."),
        (ADULT + COOKTALK + " ¿Qué indica el pulgar arriba al final? a) que la limonada está lista b) que falta azúcar", "a) que la limonada está lista", "El hablante dice The lemonade is ready con el gesto."),
    ],
    [
        (ADULT + MAPTALK + " ¿Qué muestra el hablante con el área verde?", "El parque", "Dice The park is here mientras señala el área verde."),
        (ADULT + LABTALK + " ¿Qué gesto indica que no se debe tocar el vidrio? a) mover la cabeza de lado a lado b) sonreír", "a) mover la cabeza de lado a lado", "La docente niega con la cabeza al decir Do not touch the glass."),
        (ADULT + COOKTALK + " ¿Para qué hace el gesto de exprimir?", "Para mostrar que aprieta el limón", "El gesto acompaña squeeze the lemon."),
    ],
    [
        (ADULT + MAPTALK + " ¿Cuánto demora la caminata? Fíjate en el gesto de los dedos.", "Dos horas", "Muestra dos dedos y dice two hours."),
        (ADULT + MAPTALK + " No entendiste la palabra path. ¿Qué pregunta de las siguientes la aclara? a) «What does path mean?» b) «Where is the river?»", "a) What does path mean?", "Pide el significado de la palabra."),
        (ADULT + COOKTALK + " ¿Cuántas mitades hace el cocinero al cortar el limón?", "2", "Dice two halves."),
    ],
    [
        (ADULT + MAPTALK + " ¿Qué sendero se menciona? a) uno que va a lo largo del río b) uno que sube un cerro", "a) uno que va a lo largo del río", "Dice the path goes along the river."),
        ("Quieres que una persona hable más lento. ¿Qué dices? a) «Could you speak more slowly, please?» b) «Where is the station?»", "a) Could you speak more slowly, please?", "Pide aclarar la velocidad."),
    ],
    [
        (ADULT + LABTALK + " Un compañero dice que el termómetro mide el peso. Con el gesto y el texto, ¿qué mide? ", "La temperatura", "La docente dice It measures temperature."),
        (ADULT + COOKTALK + " Ordena los gestos. A) pulgar arriba. B) exprimir. C) mostrar la taza pequeña.", "B, C, A", "Primero exprime el limón, luego muestra el azúcar y al final dice que está lista."),
    ],
    [(ADULT + "«[The guide points to the left.] The library is on this side. [She points to the right.] The gym is over there. [She holds up three fingers.] The gym has three courts.» (guide = guía, side = lado, over there = allá, courts = canchas). ¿Qué hay a la derecha? a) el gimnasio b) la biblioteca", "a) el gimnasio", "La guía señala a la derecha cuando habla del gimnasio.")],
    [
        ("¿Qué frase sirve para pedir que repitan?", "Could you repeat that, please?", "Es una forma cortés de pedir repetición."),
        ("¿Para qué sirve decir «Do you mean…?»", "Para confirmar lo que entendiste", "Verificas tu comprensión."),
        ("¿Qué apoyos ayudan a entender sin entender cada palabra?", "Imágenes y gestos", "Dan pistas visuales."),
    ],
    task("Un adulto lee dos veces: «[The speaker holds a calendar.] Today is Monday. [She taps Wednesday.] The test is on Wednesday. [She holds up one finger.] Study one hour each day. [She makes a writing gesture.] Write your questions in your notebook.» (calendar = calendario, taps = toca, study = estudiar, each day = cada día). Escribe: qué día es la prueba, cuántas horas estudiar y qué hay que escribir. Después escribe en inglés una pregunta para confirmar el día.", "La prueba es el miércoles. Hay que estudiar una hora cada día y escribir las preguntas en el cuaderno. Pregunta: Do you mean Wednesday?", ["responde con los datos correctos del guion", "relaciona el gesto con cada dato", "escribe una pregunta de confirmación en inglés"], ["hoja con respuestas", "nota del adulto"], ["decir que la prueba es el lunes", "no escribir ninguna pregunta de confirmación"], "Reconoce lo que acertó y repasa con la persona qué gesto acompañó cada dato."),
    "Pide a un adulto que lea de nuevo el texto del mapa y dibuja el mapa con el punto azul, el parque y el río.",
    "Inventa un gesto para decir «no sé» y una frase en inglés para pedir ayuda.",
)

# ---------------------------------------------------------------- clase 4: confirmar predicciones
PARTY = "«Happy birthday, Tomás! The surprise party starts at four o'clock in the garden. There is a chocolate cake with ten candles. Everyone brings a small gift. We hide behind the big tree. When Tomás arrives, we shout: Surprise!» (surprise = sorpresa, cake = torta, candles = velas, gift = regalo, hide = escondernos, shout = gritamos)"
PICNIC = "«On Sunday, the Vega family goes to the lake. They take sandwiches, juice and a ball. At noon, it starts to rain, so they eat inside the car. After the rain stops, they play with the ball near the water. They go home at six, tired and happy.» (lake = lago, ball = pelota, starts to rain = empieza a llover, stops = para, tired = cansados)"
RACE = "«The school race is on Friday at ten. There are three groups: the fast runners, the medium runners and the slow runners. Everybody gets a green number. The winner gets a medal, and all the runners get a bottle of water.» (race = carrera, groups = grupos, runners = corredores, medium = medios, slow = lentos, winner = ganador, medal = medalla)"

lesson(
    OA3, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a confirmar mis predicciones después de escuchar: comparar lo que pensé con lo que realmente dijo el texto, y corregir lo que no coincide. Sirve para comprobar si entendí bien y aprender de mis errores.",
    ["Sé hacer una predicción con el título.", "Conozco palabras como party, cake y rain."],
    [
        "Antes de escuchar hiciste predicciones (predictions). Después de escuchar, vas a confirmar (confirm) o corregir (correct) cada una. Una predicción se confirma cuando el texto dice lo mismo. Se corrige cuando el texto dice algo distinto. También puede quedar sin respuesta si el texto no habla de ese punto.",
        "Un buen método es una tabla con tres columnas: «Predicted» (lo que predije), «Heard» (lo que oí) y «Result» (resultado: confirmed, corrected o not mentioned). Por ejemplo, si predijiste que habría pizza en la fiesta y el texto dice chocolate cake, la predicción se corrige: la fiesta tiene torta, no pizza. Si el texto no nombra la comida, el resultado es not mentioned.",
        "Predecir mal no es un error grave: es parte del aprendizaje. Lo importante es detectar la diferencia y ajustar tu comprensión. Después de confirmar o corregir, pregúntate: ¿qué pista me engañó? ¿Qué palabra me habría ayudado a predecir mejor?",
    ],
    [("confirm", "confirmar: el texto dice lo mismo"), ("correct", "corregir: el texto dice algo distinto"), ("not mentioned", "no mencionado"), ("predicted", "predicho"), ("heard", "oído"), ("result", "resultado")],
    [
        ("Confirmar o corregir", "Predicción: «The weather will be sunny.» El texto dice: «Tomorrow will be cloudy.» (sunny = soleado, cloudy = nublado). ¿Qué resultado corresponde?", ["Comparo sunny con cloudy.", "No coinciden.", "La predicción se corrige."], "Corregida: será nublado"),
        ("No mencionado", "Predicción: «The family brings a dog.» El texto dice: «They take sandwiches and juice.» ¿Qué resultado corresponde?", ["Busco dog en el texto.", "No aparece.", "El resultado es not mentioned."], "No mencionado"),
    ],
    [
        ("Pensar que una predicción corregida es un fracaso.", "No se ve como parte del aprendizaje.", "Corrige la predicción y anota qué pista del texto la corrigió."),
        ("Confirmar una predicción solo porque se parece a lo oído.", "No se compara con el dato exacto.", "Comprueba el número, el color o el lugar dichos."),
    ],
    [
        (ADULT + PARTY + " Predicción: «Habrá una torta.» ¿Resultado? a) confirmada b) corregida", "a) confirmada", "Dice a chocolate cake."),
        (ADULT + PICNIC + " Predicción: «La familia va a la playa.» ¿Resultado? a) corregida: va al lago b) confirmada", "a) corregida: va al lago", "Dice goes to the lake."),
        (ADULT + RACE + " Predicción: «El ganador recibe una medalla.» ¿Resultado? a) confirmada b) corregida", "a) confirmada", "Dice the winner gets a medal."),
    ],
    [
        (ADULT + PARTY + " Predicción: «La fiesta empieza a las cinco.» ¿Qué hora dice el texto?", "A las cuatro", "Dice at four o'clock."),
        (ADULT + PICNIC + " Predicción: «Comerán afuera todo el día.» ¿Qué pasó realmente a mediodía?", "Empezó a llover y comieron dentro del auto", "Dice it starts to rain, so they eat inside the car."),
        (ADULT + RACE + " Predicción: «Hay dos grupos de corredores.» ¿Cuántos grupos dice el texto?", "Tres", "Dice three groups."),
    ],
    [
        (ADULT + PARTY + " Predicción: «Los invitados traen globos.» ¿Resultado? a) no mencionado: el texto habla de regalos b) confirmada", "a) no mencionado: el texto habla de regalos", "El texto dice small gift, no balloons."),
        (ADULT + PICNIC + " Predicción: «Después de la lluvia no pueden jugar.» ¿Resultado? a) corregida: juegan con la pelota b) confirmada", "a) corregida: juegan con la pelota", "Dice they play with the ball near the water."),
        (ADULT + RACE + " Predicción: «Los números son rojos.» ¿Qué color dice el texto?", "Verde", "Dice a green number."),
    ],
    [
        (ADULT + PARTY + " Una compañera confirmó «Hay doce velas». ¿Tiene razón? Responde sí o no.", "No", "El texto dice ten candles."),
        (ADULT + PICNIC + " Ana confirmó «La familia vuelve a casa a las seis». ¿Tiene razón? Responde sí o no.", "Sí", "Dice they go home at six."),
    ],
    [
        (ADULT + PARTY + " Marca las predicciones corregidas. A) La torta es de vainilla. B) La fiesta es en el jardín. C) Todos traen un regalo pequeño. D) La fiesta empieza a las tres.", "A y D", "El texto dice chocolate y las cuatro; el jardín y el regalo coinciden."),
        (ADULT + RACE + " Todos los corredores reciben una botella de agua y el ganador una medalla. Si hay 3 grupos de 8 corredores, ¿cuántas botellas se reparten?", "24", "Cada corredor recibe una botella.", "3*8"),
    ],
    [(ADULT + "«Tomorrow our class will visit a farm. We will see cows, sheep and chickens. We will leave school at nine o'clock and return at two.» (farm = granja, cows = vacas, sheep = ovejas, chickens = gallinas, return = volver). Predijiste que verían caballos. ¿Qué resultado corresponde? a) no mencionado b) confirmada", "a) no mencionado", "El texto nombra vacas, ovejas y gallinas, no caballos.")],
    [
        ("¿Qué haces si el texto dice algo distinto a tu predicción?", "La corriges", "El resultado es corrected."),
        ("¿Cuántas columnas tiene la tabla de confirmación?", "3", "Son predicho, oído y resultado."),
        ("¿Qué resultado da un dato que el texto no nombra?", "No mencionado", "El texto no habla de ese punto."),
    ],
    task("Antes de escuchar, escribe dos predicciones para el título «A Day at the Zoo» (por ejemplo, un animal y una hora). Después un adulto lee dos veces: «At the zoo, we saw monkeys, parrots and two small tigers. The tigers were sleeping at noon. We ate lunch at one o'clock near the lake. The zoo closes at five.» (monkeys = monos, parrots = loros, tigers = tigres, sleeping = durmiendo, lunch = almuerzo). Completa una tabla con Predicted, Heard y Result para cada predicción.", "Predicción 1: veremos leones. Oído: monos, loros y tigres. Resultado: corregida. Predicción 2: cierra a las cinco. Oído: closes at five. Resultado: confirmada.", ["escribe dos predicciones antes de escuchar", "anota lo oído con datos del texto", "clasifica cada resultado de forma coherente"], ["tabla con tres columnas", "nota del adulto"], ["escribir las predicciones después de escuchar", "marcar como confirmada una predicción que no coincide"], "Reconoce lo que acertó y repasa con la persona qué dato exacto confirmó o corrigió cada predicción."),
    "Pide a un adulto que lea de nuevo la fiesta sorpresa y marca con verde lo confirmado y con rojo lo corregido.",
    "Escribe una predicción sobre un partido de fútbol escolar y cómo la comprobarías.",
)

# ---------------------------------------------------------------- clase 5: resumir con esquemas
CLIMB = "«Last Saturday, Elena and her brother climbed a small hill near their town. They left at eight in the morning. First, they walked through a forest. Then they crossed a stream. At the top, they ate sandwiches and looked at the town. They returned at four in the afternoon and were very tired.» (climbed = subieron, hill = cerro, forest = bosque, crossed = cruzaron, stream = arroyo, top = cima, returned = volvieron)"
COMPOST = "«To make compost, you need three things: kitchen waste, dry leaves and a container. Put a layer of leaves, then a layer of waste. Repeat the layers. Wait two months. After that, the compost is ready to feed the plants.» (compost = compostaje, waste = restos, leaves = hojas, container = recipiente, layer = capa, feed = alimentar)"
LIBRARY = "«The school library has new rules. Students can borrow two books for fourteen days. If a book is late, the student must wait one week to borrow again. The library is open from eight to four. Silence is important because many students study there.» (rules = reglas, borrow = pedir prestado, late = atrasado, must wait = debe esperar, silence = silencio)"

lesson(
    OA3, 5,
    "Los textos y esquemas escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a resumir una idea de un texto oral con apoyo de esquemas: línea de tiempo, tabla y mapa de ideas. Sirve para recordar y explicar lo que escuché usando pocas palabras.",
    ["Sé confirmar predicciones.", "Conozco first, then y finally."],
    [
        "Un resumen (summary) cuenta lo más importante de un texto con pocas palabras. Un esquema (organizer) es un dibujo o una tabla que ordena las ideas. Hay tres esquemas muy útiles: la línea de tiempo (timeline), para hechos en orden; la tabla (table), para comparar o clasificar datos; y el mapa de ideas (mind map), con el tema al centro y las ideas alrededor.",
        "Para elegir el esquema, mira el tipo de texto. Si el texto tiene first, then y finally, usa una línea de tiempo. Si tiene reglas o datos de varias categorías (cuánto, cuándo, dónde), usa una tabla. Si el texto explica un tema con ideas que salen de una idea central, usa un mapa de ideas. Anota solo palabras clave en el esquema, no oraciones completas.",
        "Después, usa el esquema para decir el resumen en una oración: «The text explains that…» (El texto explica que…). Revisa que tu resumen incluya la idea principal y uno o dos datos clave. Un buen resumen es más corto que el texto, no cambia el significado y no agrega opiniones.",
    ],
    [("summary", "resumen"), ("organizer", "esquema: línea de tiempo, tabla o mapa"), ("timeline", "línea de tiempo"), ("table", "tabla"), ("mind map", "mapa de ideas"), ("The text explains that…", "El texto explica que…")],
    [
        ("Elegir el esquema", ADULT + "«First, Mario wakes up. Then he has breakfast. Finally, he goes to school.» (wakes up = despierta, breakfast = desayuno). ¿Qué esquema conviene: línea de tiempo o mapa de ideas?", ["Veo las palabras first, then y finally.", "Indican orden de los hechos.", "Conviene una línea de tiempo."], "Una línea de tiempo"),
        ("Completar una tabla", ADULT + "«On Monday, Ema has swimming. On Tuesday, she has piano. On Wednesday, she has English.» (piano = piano). Completa: Monday – ?, Tuesday – ?, Wednesday – ?", ["Voy día por día.", "Monday es swimming, Tuesday es piano.", "Wednesday es English."], "Monday – swimming, Tuesday – piano, Wednesday – English"),
    ],
    [
        ("Copiar el texto completo en el esquema.", "No se seleccionan palabras clave.", "Escribe solo una o dos palabras por casilla."),
        ("Agregar al resumen una opinión que no dice el texto.", "Se confunde resumir con opinar.", "Cuenta solo lo que dice el texto."),
    ],
    [
        (ADULT + CLIMB + " ¿Qué esquema conviene para este relato? a) línea de tiempo b) un mapa de ideas sobre alimentos", "a) línea de tiempo", "El relato cuenta hechos en orden con first y then."),
        (ADULT + COMPOST + " ¿Qué esquema conviene para organizar los materiales? a) una lista o tabla b) una línea de tiempo con horas", "a) una lista o tabla", "Hay tres materiales que se pueden ordenar."),
        (ADULT + LIBRARY + " ¿Qué tema irá al centro de un mapa de ideas? a) The library rules b) The school bus", "a) The library rules", "Todo el texto trata de las reglas de la biblioteca."),
    ],
    [
        (ADULT + CLIMB + " Completa la línea de tiempo: 8:00 salen – bosque – ? – cima – 4:00 vuelven. ¿Qué falta?", "Cruzan un arroyo", "Dice then they crossed a stream."),
        (ADULT + COMPOST + " ¿Qué tres materiales se necesitan?", "Restos de cocina, hojas secas y un recipiente", "Dice kitchen waste, dry leaves and a container."),
        (ADULT + LIBRARY + " Completa la tabla. Préstamo máximo: ? libros. Duración: ? días.", "2 libros y 14 días", "Dice two books for fourteen days."),
    ],
    [
        (ADULT + CLIMB + " ¿Cuántas horas pasaron entre las 8:00 y las 16:00?", "8", "De 8:00 a 16:00 pasan ocho horas.", "16-8"),
        (ADULT + COMPOST + " ¿Cuánto hay que esperar para que el compost esté listo?", "Dos meses", "Dice wait two months."),
        (ADULT + LIBRARY + " ¿Por qué es importante el silencio? a) porque muchos estudiantes estudian ahí b) porque los libros son frágiles", "a) porque muchos estudiantes estudian ahí", "Dice because many students study there."),
    ],
    [
        (ADULT + CLIMB + " Elige el mejor resumen. a) Elena y su hermano subieron un cerro cruzando un bosque y un arroyo, y volvieron cansados b) Elena y su hermano se perdieron en el bosque y no pudieron volver.", "a) Elena y su hermano subieron un cerro cruzando un bosque y un arroyo, y volvieron cansados.", "Incluye la idea principal y datos clave."),
        (ADULT + LIBRARY + " Un resumen dice: «Si un libro llega tarde, no puedes pedir otro por una semana». ¿Es correcto? Responde sí o no.", "Sí", "El texto dice that the student must wait one week to borrow again."),
    ],
    [
        (ADULT + COMPOST + " Ordena la línea de tiempo del compost. A) Esperar dos meses. B) Poner capas de hojas y restos. C) Alimentar las plantas.", "B, A, C", "Primero se hacen las capas, después se espera y luego se usa."),
        (ADULT + LIBRARY + " Si 3 estudiantes piden el máximo de libros permitido cada uno, ¿cuántos libros salen de la biblioteca en total?", "6", "Cada estudiante puede llevar dos libros.", "2*3"),
    ],
    [(ADULT + "«Plants need four things: light, water, air and soil. Light gives energy. Water carries nutrients. Air gives carbon dioxide. Soil holds the roots.» (nutrients = nutrientes, carbon dioxide = dióxido de carbono, holds = sostiene, roots = raíces). ¿Qué esquema conviene? a) mapa de ideas con «plants» al centro b) línea de tiempo con horas", "a) mapa de ideas con «plants» al centro", "Cuatro ideas salen de un tema central.")],
    [
        ("¿Qué esquema ordena hechos en orden?", "La línea de tiempo", "Muestra qué ocurre primero y después."),
        ("¿Qué frase introduce un resumen en inglés?", "The text explains that…", "Sirve para resumir."),
        ("¿Qué conviene escribir en un esquema?", "Palabras clave", "Son breves y sostienen el significado."),
    ],
    task("Un adulto lee dos veces: «At the school fair, there are three stands. The first stand sells juice for five hundred pesos. The second stand sells cookies for one thousand pesos. The third stand has games, and each game costs three hundred pesos. The fair finishes at four.» (fair = feria, stands = puestos, sells = vende, cookies = galletas, games = juegos, finishes = termina). Haz una tabla con tres filas (puesto 1, 2 y 3) y las columnas «qué hay» y «precio». Escribe después un resumen de una oración que empiece con «The text explains that…».", "Puesto 1: jugo, $500. Puesto 2: galletas, $1.000. Puesto 3: juegos, $300 cada uno. Resumen: The text explains that the fair has three stands with juice, cookies and games.", ["tabla con las tres filas correctas", "precios exactos", "resumen de una oración sin copiar todo el texto"], ["tabla y resumen", "nota del adulto"], ["intercambiar los precios", "escribir un resumen más largo que el texto"], "Reconoce lo que acertó y revisa con la persona cada precio contra el texto."),
    "Pide a un adulto que lea de nuevo el texto de la biblioteca y haz un mapa de ideas con tres ramas.",
    "Resume en una oración, en español, el texto del compostaje.",
)
